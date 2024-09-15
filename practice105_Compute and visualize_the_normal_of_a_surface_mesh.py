# Import the required libraries
import igl
import polyscope as ps
import numpy as np

V, F = igl.read_triangle_mesh("./data/BigBuckBunny.ply")
N = igl.per_vertex_normals(V, F)

#Initialize Polyscope for visualization
ps.init()
ps.set_ground_plane_mode("none")

# Register the original bunny mesh with Polyscope
ps_mesh = ps.register_surface_mesh("Bunny", V, F)

# Add the per-vertex normals as vector quantities to visualize them
ps_mesh.add_vector_quantity("Vertex Normals", N, enabled=True)

# Optionally, you can set radius/length/color of the normal vectors for better visibility
ps_mesh.add_vector_quantity("Normals with options", N, radius=0.001, length=0.005, color=(0.2, 0.5, 0.5))


# Display the visualization window
ps.show()


