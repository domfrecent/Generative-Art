# This is my first piece of generative art.
# The program creates a set of horizontal lines, and randomly perturbs those lines 

import numpy as np
from PIL import Image
import cv2

def create_image(img_width=1080, aspect_ratio=1):
    img_height = img_width * aspect_ratio
    return np.full([img_height, img_width, 3], 0.0)


def draw_lines(image, n_lines=40, n_points=80, vertical_buffer=0.2, horizontal_buffer=0.15):
    img_width, img_height = image.shape[:2]
    starting_x = int(horizontal_buffer * img_width)
    starting_y = int(vertical_buffer * img_height)
    ending_x = int((1 - horizontal_buffer) * img_width)
    ending_y = int((1 - vertical_buffer) * img_height)
    line_width = (ending_y - starting_y) / (n_lines-1)

    y_center = int(image.shape[0] / 2)
    x_center = int(image.shape[1] / 2)

    distance_between_points = int((ending_x - starting_x) / (n_points - 1))
    distance_between_lines = int((ending_y - starting_y) / (n_lines - 1))

    for j in range(n_lines):
        y_coord_start = starting_y + distance_between_lines * j
        prev_y = y_coord_start
        for i in range(n_points - 1):
            x_coord = starting_x + distance_between_points * i
            y_distance_from_center = abs(y_coord_start - y_center)
            x_distance_from_center = abs(x_coord - x_center)
            y_coord = y_coord_start + int(line_width/10 * np.random.randn())
            cv2.line(image, (x_coord, prev_y), (x_coord + distance_between_points, y_coord), (245, 245, 245), 2)
            prev_y = y_coord

    return image


if __name__ == '__main__':
    out_path = 'images/shaky_lines.png'
    aspect_ratio = 1
    img_width = 3840
    image = create_image(img_width, aspect_ratio)

    vertical_buffer = 0.2
    horizontal_buffer = 0.15
    n_lines = 20
    n_points = 40
    image = draw_lines(image, n_lines, n_points, vertical_buffer, horizontal_buffer)

    cv2.imwrite(out_path, image)
