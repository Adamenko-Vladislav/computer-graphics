import cv2
import numpy as np

def bernsen_thresholding(image, e=15, r=15):
    processed_image = np.copy(image)
    half_r = r // 2
    for x in range(half_r, image.shape[1] - half_r):
        for y in range(half_r, image.shape[0] - half_r):
            pixel_values = []
            for i in range(x - half_r, x + half_r + 1):
                for j in range(y - half_r, y + half_r + 1):
                    pixel_values.append(image[j, i])

            jlow = np.min(pixel_values)
            jhigh = np.max(pixel_values)

            threshold = (jhigh - jlow) / 2

            if threshold <= e:
                processed_image[y, x] = 0
            else:
                processed_image[y, x] = 255

    return processed_image

def niblack_thresholding(image, r=15, k=-0.2):
    processed_image = np.copy(image)
    half_r = r // 2
    for x in range(half_r, image.shape[1] - half_r):
        for y in range(half_r, image.shape[0] - half_r):
            neighborhood = image[y - half_r:y + half_r + 1, x - half_r:x + half_r + 1]
            mean_value = np.mean(neighborhood)
            std_deviation = np.std(neighborhood)
            threshold = mean_value + k * std_deviation

            if image[y, x] <= threshold:
                processed_image[y, x] = 0
            else:
                processed_image[y, x] = 255

    return processed_image

def adaptive_thresholding(image, constant=2 / 3, block_size=11):
    processed = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, 1 / constant)
    return processed

def global_thresholding_by_histogramm(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    total_pixels = image.shape[0] * image.shape[1]
    cumulative_sum = np.cumsum(hist)
    threshold = 0
    max_variance = 0

    for t in range(256):
        w0 = cumulative_sum[t] / total_pixels
        w1 = (total_pixels - cumulative_sum[t]) / total_pixels
        mu0 = np.sum(np.multiply(hist[:t + 1], np.arange(t + 1))) / (cumulative_sum[t] + 1e-8)
        mu1 = np.sum(np.multiply(hist[t + 1:], np.arange(t + 1, 256))) / (cumulative_sum[255] - cumulative_sum[t] + 1e-8)
        variance = w0 * w1 * (mu0 - mu1) ** 2

        if variance > max_variance:
            max_variance = variance
            threshold = t

    processed = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]
    return processed

def global_thresholding_otsu(image):
    _, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresholded

def logarithmic_transformation(image):
    max_value = np.max(image)
    transformed = 255 * (np.log1p(image) / np.log1p(max_value))
    transformed = np.round(transformed).astype(np.uint8)
    return transformed

def linear_contrast(image):
    min_value = np.min(image)
    max_value = np.max(image)
    transformed = 255 * ((image - min_value) / max((max_value - min_value), 1))
    transformed = np.round(transformed).astype(np.uint8)

    return transformed

import tkinter as tk
from tkinter import filedialog
import os

def select_input_directory():
    input_directory = filedialog.askdirectory(title="Select Input Directory")
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_directory)

def select_output_directory():
    output_directory = filedialog.askdirectory(title="Select Output Directory")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_directory)

def process_images():
    input_directory = input_entry.get()
    output_directory = output_entry.get()

    methods = [bernsen_thresholding, niblack_thresholding, adaptive_thresholding, logarithmic_transformation, linear_contrast]

    for method in methods:
        method_output_directory = os.path.join(output_directory, method.__name__)
        os.makedirs(method_output_directory, exist_ok=True)

        image_files = os.listdir(input_directory)
        for image_file in image_files:
            if image_file.endswith('.png') or image_file.endswith('.jpg'):
                image_path = os.path.join(input_directory, image_file)
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

                processed_image = method(image)

                output_image_path = os.path.join(method_output_directory, image_file)
                cv2.imwrite(output_image_path, processed_image)

    print("Processing complete!")

root = tk.Tk()

button1 = tk.Button(root, text="Select Input Directory", command=select_input_directory)
button1.pack()

input_entry = tk.Entry(root)
input_entry.pack()

button2 = tk.Button(root, text="Select Output Directory", command=select_output_directory)
button2.pack()

output_entry = tk.Entry(root)
output_entry.pack()

button3 = tk.Button(root, text="Process Images", command=process_images)
button3.pack()

root.mainloop()
