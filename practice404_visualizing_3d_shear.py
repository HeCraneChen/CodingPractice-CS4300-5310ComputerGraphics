# Import the required libraries
import igl
import polyscope as ps
import numpy as np

# Read a 3D mesh using libigl
V, F = igl.read_triangle_mesh("./data/camel_b.obj")

# Initialize Polyscope for visualization
ps.init()
ps.set_ground_plane_mode("shadow_only")

# Function to apply shear transformation along X-axis
def shear_mesh(V, shear_factor):
    shear_matrix = np.array([
        [1, shear_factor, shear_factor],  # Shearing along X-axis
        [0, 1, 0],  # No shearing along Y-axis
        [0, 0, 1]   # No shearing along Z-axis
    ])
    return V @ shear_matrix.T  # Multiply the vertices by the shear matrix

# Shear and register 10 versions of the mesh
for i in range(10):
    shear_factor = i * 0.1  # 10 meshes, applying increasing shear factors
    V_sheared = shear_mesh(V, shear_factor)
    ps.register_surface_mesh(f"camel sheared {shear_factor}x", V_sheared, F, color=(252/255, 221/255, 129/255))

# Display the visualization window
ps.show()
