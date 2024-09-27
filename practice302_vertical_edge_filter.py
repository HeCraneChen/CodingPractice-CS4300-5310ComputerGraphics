from PIL import Image
import numpy as np
from scipy.ndimage import convolve

def apply_vertical_edge_filter(image_path, amplification_factor=10):
    # Load the image and convert to grayscale
    image = Image.open(image_path).convert("L")
    
    # Convert the image to a NumPy array
    image_array = np.array(image, dtype=np.float32)
    
    # Define the vertical edge detection filter
    vertical_edge_filter = np.array([[0, 0, 0], [-1, 1, 0], [0, 0, 0]])
    
    # Apply the convolution with the vertical edge filter
    filtered_array = convolve(image_array, vertical_edge_filter)
    
    # Amplify the result to make edges more prominent
    filtered_array = amplification_factor * filtered_array
    
    # Rescale the filtered array to highlight edges
    filtered_array = filtered_array / 2 + 128
    
    # Clip values to ensure they remain in 0-255 range
    filtered_array = np.clip(filtered_array, 0, 255)
    
    # Convert back to uint8 type and to an image
    filtered_image = Image.fromarray(filtered_array.astype(np.uint8))
    
    # Save the filtered image
    filtered_image.save("./result.jpg")

# Example usage
image_path = "./data/ginevra_de'_benci__obverse__1967.6.1.a.jpg"
apply_vertical_edge_filter(image_path, amplification_factor=20)
