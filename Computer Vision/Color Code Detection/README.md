# Image Color Detection using OpenCV

## Overview
This project is a simple tool built using OpenCV that allows users to pick colors from an image by double-clicking on it. The tool then displays the RGB values and the corresponding hex code for the color at the clicked point. A small circle is drawn at the clicked point, and a box with the hex code is displayed for reference.

## Features
- Load any image and interact with it by double-clicking on the desired point.
- The RGB values and the hex color code are displayed on the image at the clicked location.
- A small red circle is drawn at the clicked point, and a rectangle box shows the hex code in a clean format.

## Code Explanation
- **get_hexcode(r, g, b)**: This function converts the RGB values into a hex color code.
- **get_color(event, x, y, flags, param)**: This is the OpenCV mouse callback function. It gets the RGB values at the clicked position and displays them along with the hex code on the image.
- **cv2.circle()**: Draws a small red circle at the clicked point.
- **cv2.rectangle()**: Draws a rectangle to display the hex code.
- **cv2.putText()**: Displays the hex code inside the rectangle.

## Example Output
- When you double-click on an area of the image, the following information will be printed in the terminal:
  ```bash
  255 128 64  # RGB values
  HexCode: #FF8040  # Hex code
  ```
## Demo
![Demo Screenshot](screenshot.png)
