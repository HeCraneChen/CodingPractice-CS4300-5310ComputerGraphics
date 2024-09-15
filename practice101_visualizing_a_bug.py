# Import the required libraries
import igl
import polyscope as ps

# Read a 3D mesh using libigl
V, F = igl.read_triangle_mesh("./data/BUG.ply")

# Initialize Polyscope for visualization
ps.init()
ps.set_ground_plane_mode("none")  

# Register the mesh with Polyscope for rendering
ps.register_surface_mesh("My Bug", V, F)

# Display the visualization window
ps.show()
