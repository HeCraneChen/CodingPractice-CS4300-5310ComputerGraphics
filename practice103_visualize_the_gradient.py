import igl
import polyscope as ps
import numpy as np

# Read the mesh and scalar field
v, f = igl.read_triangle_mesh("./Data/cheburashka.off")
u = igl.read_dmat("./Data/cheburashka-scalar.dmat")
g = igl.grad(v, f)
gu = g.dot(u).reshape(f.shape, order="F")
gu_mag = np.linalg.norm(gu, axis=1)
# Initialize Polyscope for visualization
ps.init()
# Register the surface mesh
ps_mesh = ps.register_surface_mesh("Cheburashka", v, f)
ps.set_ground_plane_mode("none")
# Add the scalar field as a quantity on the vertices
ps_mesh.add_scalar_quantity("Scalar Field", u, defined_on="vertices", enabled=True, cmap='pink-green')
# Compute the barycenters of the triangles
bc = igl.barycenter(v, f)
# Normalize gradient vector field for better visualization
max_size = igl.avg_edge_length(v, f) / np.mean(gu_mag)
bcn = bc + max_size * gu
# Register the vector field as lines from the barycenters to the adjusted points
ps.register_curve_network("Gradient Field", bc, np.arange(bc.shape[0])[:, None].repeat(2, axis=1), radius=0.0012)
ps.get_curve_network("Gradient Field").add_vector_quantity("Gradients", bcn - bc, enabled=True, color=(0, 0, 0), 
radius=0.00086, length=0.09037)
ps.show()
