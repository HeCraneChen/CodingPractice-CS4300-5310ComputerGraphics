# Import the required libraries
import igl
import polyscope as ps
import numpy as np

# Read a 3D mesh using libigl
V, F = igl.read_triangle_mesh("./data/camel_b.obj")

# Initialize Polyscope for visualization
ps.init()
ps.set_ground_plane_mode("shadow_only")

# Function to apply translation along the X-axis
def translate_mesh_x(V, translation_distance):
    translation_matrix = np.array([0, 0, translation_distance])  # Move along Z-axis
    return V + translation_matrix  # Add the translation vector to each vertex

# Translate and register 10 versions of the mesh
for i in range(10):
    translation_distance = i * 10  # 10 meshes, moving in 0.5 unit steps along the X-axis
    V_translated = translate_mesh_x(V, translation_distance)
    ps.register_surface_mesh(f"camel translated {translation_distance} units", V_translated, F, color=(252/255, 221/255, 129/255))

# Display the visualization window
ps.show()
