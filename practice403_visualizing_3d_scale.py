# Import the required libraries
import igl
import polyscope as ps
import numpy as np

# Read a 3D mesh using libigl
V, F = igl.read_triangle_mesh("./data/camel_b.obj")

# Initialize Polyscope for visualization
ps.init()
ps.set_ground_plane_mode("none")

# Function to apply scaling transformation
def scale_mesh(V, scale_factor):
    scaling_matrix = np.array([
        [scale_factor, 0, 0],
        [0, scale_factor, 0],
        [0, 0, scale_factor]
    ])
    return V @ scaling_matrix.T  # Multiply the vertices by the scaling matrix

# Scale and register 10 versions of the mesh
for i in range(10):
    scale_factor = 0.5 + i * 0.1  # 10 meshes, scaling from 0.5x to 1.4x
    V_scaled = scale_mesh(V, scale_factor)
    ps.register_surface_mesh(f"camel scaled {scale_factor}x", V_scaled, F, color=(252/255, 221/255, 129/255))

# Display the visualization window
ps.show()
