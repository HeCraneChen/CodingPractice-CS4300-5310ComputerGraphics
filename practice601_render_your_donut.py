import pyrender
import trimesh
import numpy as np

# Set up the objects
mesh = trimesh.creation.torus(major_radius=1.0, minor_radius=0.3)
metallic_color = np.array([0.8, 0.8, 0.8, 1.0])  
material = pyrender.MetallicRoughnessMaterial(
    baseColorFactor=metallic_color,
    metallicFactor=1.0, 
    roughnessFactor=0.1, 
    alphaMode='OPAQUE', 
    doubleSided=True  
)
mesh = pyrender.Mesh.from_trimesh(mesh, material=material)
scene = pyrender.Scene()
scene.add(mesh)
# Create lights
dir_light = pyrender.DirectionalLight(color=np.ones(3), intensity=1.0)
scene.add(dir_light, pose=np.array([
    [1, 0, 0, 0],
    [0, 1, 0, -1],
    [0, 0, 1, 3],
    [0, 0, 0, 1]
]))
point_light = pyrender.PointLight(color=np.ones(3), intensity=10.0)
scene.add(point_light, pose=np.array([
    [1, 0, 0, 2],
    [0, 1, 0, 2],
    [0, 0, 1, 2],
    [0, 0, 0, 1]
]))
spot_light = pyrender.SpotLight(color=np.ones(3), intensity=10.0, innerConeAngle=np.pi/16, outerConeAngle=np.pi/8)
scene.add(spot_light, pose=np.array([
    [1, 0, 0, -2],
    [0, 1, 0, -2],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]))
# Viewer to see the scene
pyrender.Viewer(scene, use_raymond_lighting=False)
