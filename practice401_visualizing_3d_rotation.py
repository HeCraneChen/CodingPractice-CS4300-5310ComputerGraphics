# Import the required libraries
import igl
import polyscope as ps
import numpy as np

# Read a 3D mesh using libigl
V, F = igl.read_triangle_mesh("./data/camel_b.obj")

# Initialize Polyscope for visualization
ps.init()
ps.set_ground_plane_mode("shadow_only")

# Function to apply rotation around Y-axis
def rotate_mesh_y(V, angle_deg):
    angle_rad = np.radians(angle_deg)
    rotation_matrix = np.array([
        [np.cos(angle_rad), 0, np.sin(angle_rad)],
        [0, 1, 0],
        [-np.sin(angle_rad), 0, np.cos(angle_rad)]
    ])
    return V @ rotation_matrix.T

# Rotate and register 10 versions of the mesh
for i in range(10):
    angle = i * 9  # 10 meshes rotating from 0 to 90 degrees
    V_rotated = rotate_mesh_y(V, angle)
    ps.register_surface_mesh(f"camel rotated {angle} degrees", V_rotated, F, color=(252/255, 221/255, 129/255))

# Display the visualization window
ps.show()
