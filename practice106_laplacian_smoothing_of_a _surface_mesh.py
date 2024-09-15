# Import the required libraries
import open3d as o3d
import polyscope as ps
import numpy as np

# Read the original mesh
mesh_in = o3d.io.read_triangle_mesh("./data/BigBuckBunny.ply")

# Define the number of iterations for smoothing
iterations = [5, 10, 40, 60]
smoothed_meshes = {}

# Perform Laplacian smoothing for each iteration count
for i in iterations:
    print(f'Filtering with Laplacian for {i} iterations')
    smoothed_mesh = mesh_in.filter_smooth_laplacian(number_of_iterations=i)
    smoothed_mesh.compute_vertex_normals()
    smoothed_meshes[i] = smoothed_mesh

# Convert the original and smoothed meshes to numpy arrays
V_in = np.asarray(mesh_in.vertices)
F_in = np.asarray(mesh_in.triangles)

# Initialize Polyscope for visualization
ps.init()
ps.set_ground_plane_mode("none")

# Register the original mesh with Polyscope for rendering
ps.register_surface_mesh("Original Mesh", V_in, F_in)

# Register smoothed meshes for each iteration count
for i, mesh_out in smoothed_meshes.items():
    V_out = np.asarray(mesh_out.vertices)
    F_out = np.asarray(mesh_out.triangles)
    ps.register_surface_mesh(f"Smoothed Mesh - {i} iterations", V_out, F_out)

# Display the visualization window
ps.show()
