import cv2
import numpy as np
from google.colab.patches import cv2_imshow

NO_CORNERS = 78

def first_correct_scale(I):
    """Find smallest scale with 78 corners using image pyramid"""
    Pyr = [I]  # Start with original image
    for _ in range(5):  # Build 6 levels (0 to 5)
        I = cv2.pyrDown(I)
        Pyr.append(I)
    
    for k in range(6):  # Check each scale
        G = cv2.cvtColor(Pyr[k], cv2.COLOR_BGR2GRAY)
        G = np.float32(G)
        corners = cv2.goodFeaturesToTrack(G, maxCorners=1000, qualityLevel=0.001, minDistance=2, blockSize=4, useHarrisDetector=True, k=0.04)
        nc = len(corners) if corners is not None else 0
        print(f"Scale {k}: Found {nc} corners")
        if nc == NO_CORNERS:
            return k
    return 5  # Fallback to max scale

# Load images
I1 = cv2.imread('/content/1.PNG')
I2 = cv2.imread('/content/3.PNG')

if I1 is None or I2 is None:
    print("Error: Could not load images.")
else:
    # Resize to same height
    h1, w1 = I1.shape[:2]
    h2, w2 = I2.shape[:2]
    target_height = min(h1, h2)
    I1_resized = cv2.resize(I1, (int(w1 * target_height / h1), target_height))
    I2_resized = cv2.resize(I2, (int(w2 * target_height / h2), target_height))

    # Get scales
    sc1 = first_correct_scale(I1)
    sc2 = first_correct_scale(I2)
    J = np.concatenate((I1_resized, I2_resized), 1)

    # Determine text
    if sc1 < sc2:
        txt = f'Logo 1 is {2**(sc2-sc1):.2f} times larger than logo 2'
    elif sc1 > sc2:
        txt = f'Logo 1 is {2**(sc1-sc2):.2f} times smaller than logo 2'
    else:
        txt = 'Logo 1 is about the same size as logo 2'

    # Add text and display
    cv2.putText(J, txt, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2_imshow(J)
    print(f"Scales: I1 = {sc1}, I2 = {sc2}")
    print(txt)
