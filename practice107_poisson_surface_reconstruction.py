import numpy as np
import open3d as o3d
import polyscope as ps

# Load the horse data (XYZ coordinates + normals)
horse = np.loadtxt("./Data/horse.txt")

# Extract the vertices and normals
V, N = horse[:, :3], horse[:, 3:]

# Normalize the normal vectors (N)
N_norm = N / np.linalg.norm(N, axis=1, keepdims=True)

# Sample a smaller subset for testing (e.g., first 1000 points)
sampled_indices = np.random.choice(V.shape[0], size=1000, replace=False)
V_sampled = V[sampled_indices]
N_sampled = N_norm[sampled_indices]

# Create the point cloud with a smaller sample
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(V_sampled)
pcd.normals = o3d.utility.Vector3dVector(N_sampled)

# Create a mesh using Poisson surface reconstruction
mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=10)
V_reconstruction = np.asarray(mesh.vertices)
F_reconstruction = np.asarray(mesh.triangles)

# Visualization
ps.init()
ps.set_ground_plane_mode("none")
ps_pcd_horse = ps.register_point_cloud("The input (oriented point cloud)", V, radius=0.001)
ps_pcd_horse.add_vector_quantity("normal vector field", N, enabled=True, radius=0.00068, length=0.01118)
ps_mesh = ps.register_surface_mesh("The output (reconstructed horse mesh)", V_reconstruction, F_reconstruction)
ps.show()
