import numpy as np
from PIL import Image, ImageDraw

def generate_halftone(image_path, dot_radius=30, spacing=20):
    # Load the image and convert it to grayscale
    image = Image.open(image_path).convert("L")
    
    # Resize the image for the halftone effect (adjusting the number of dots)
    img_small = image.resize((image.width // spacing, image.height // spacing))
    
    # Create a new blank white image
    halftone_image = Image.new("RGB", image.size, "white")
    draw = ImageDraw.Draw(halftone_image)
    
    # Get the grayscale pixel values from the resized image
    grayscale_values = np.array(img_small)
    
    # Iterate over each pixel in the resized image
    for y in range(grayscale_values.shape[1]):
        for x in range(grayscale_values.shape[0]):
            # Calculate the radius of the dot based on the brightness (inverted)
            brightness = grayscale_values[x, y]
            radius = (1 - brightness / 255) * dot_radius
            
            # Calculate the center of the dot in the larger image
            center_x = x * spacing + spacing // 2
            center_y = y * spacing + spacing // 2
            
            # Draw the dot on the halftone image
            if radius > 0:
                draw.ellipse(
                    (center_x - radius, center_y - radius, center_x + radius, center_y + radius),
                    fill="black"
                )
    
    return halftone_image

# Example usage
image_path = "./data/ginevra_de'_benci__obverse__1967.6.1.a.jpg"
halftone_image = generate_halftone(image_path, dot_radius=15, spacing=30)
halftone_image.show()

# Save the result
halftone_image.save("./result.jpg" )

