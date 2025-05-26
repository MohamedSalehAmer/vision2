
# Logo Size Estimation via Image Pyramid and Harris Corner Detection

This project estimates the relative size (or detail) of two logos by using image pyramids and Harris corner detection. It determines the smallest image scale at which exactly 78 corners can be detected, then compares the two images based on these scales.

## 🧠 Purpose

The goal is to compare two logos and determine which is larger or more detailed by evaluating how much downscaling is needed to detect a fixed number of corners.

## 📦 Requirements

Install the required packages:

```bash
pip install opencv-python numpy
```

For Google Colab users, use `cv2_imshow` instead of `cv2.imshow`.

## 🖼️ Input

Place your logo images in the following paths:

- `/content/1.PNG`
- `/content/3.PNG`

Modify paths accordingly if not using Colab.

## 🛠️ How It Works

1. Builds an image pyramid for each logo with 6 levels (from original down to 1/32 scale).
2. At each level, it applies Harris corner detection using `cv2.goodFeaturesToTrack`.
3. It finds the smallest scale where **exactly 78 corners** are detected.
4. The two images are resized to the same height and displayed side-by-side with a text overlay.
5. Size comparison is based on scale:
   - If one logo achieves 78 corners at a higher resolution, it is considered more **detailed/larger**.
   - If it needs more downscaling, it is considered **less detailed/smaller**.

## 📊 Output

- A side-by-side comparison of the logos with size comparison text overlay.
- Printed output showing:
  - Number of corners at each pyramid level.
  - Final scale level used for each image.
  - Textual conclusion comparing the logos.

## 📎 Example Output

```
Scale 0: Found 102 corners  
Scale 1: Found 89 corners  
Scale 2: Found 78 corners  
Scales: I1 = 2, I2 = 4  
Logo 1 is 4.00 times larger than logo 2
```

## 📄 Notes

- The number of corners (`NO_CORNERS = 78`) is adjustable.
- The downscale factor is `2^scale_difference` for intuitive size ratio.

## 🔗 References

- [OpenCV Image Pyramids](https://docs.opencv.org/4.x/d4/d1f/tutorial_pyramids.html)
- [OpenCV Harris Corner Detection](https://docs.opencv.org/4.x/dc/d0d/tutorial_py_features_harris.html)

---

This method offers a scale-based perspective on visual complexity and size estimation between logos.
