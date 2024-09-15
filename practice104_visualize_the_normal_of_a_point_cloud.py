# Import the required libraries
import polyscope as ps
import numpy as np

# Load the horse mesh and normal vectors from the file
horse = np.loadtxt("./data/horse.txt")
V_horse, N_horse = horse[:, :3], horse[:, 3:]

# Initialize Polyscope for visualization
ps.init()
ps.set_ground_plane_mode("none")

# Register the horse mesh with Polyscope as a point cloud (horse doesn't have faces)
ps_pcd_horse = ps.register_point_cloud("Horse", V_horse, radius=0.001)

# Add the normal vectors for the horse, scaling them down to be smaller
ps_pcd_horse.add_vector_quantity("Horse Vertex Normals", N_horse, enabled=True, radius=0.00068, length=0.01118)

# Display the visualization window
ps.show()
