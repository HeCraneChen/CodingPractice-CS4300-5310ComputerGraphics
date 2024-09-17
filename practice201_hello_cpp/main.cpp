#include <igl/read_triangle_mesh.h>
#include <igl/principal_curvature.h>

#include <Eigen/Geometry>
#include <Eigen/StdVector>
#include <vector>
#include <algorithm>
#include <iostream>

#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"
#include "polyscope/curve_network.h"



int main(int argc, char *argv[])
{
  using namespace Eigen;
  using namespace std;

  // variable definition
  Eigen::MatrixXd V, PD1, PD2, PV1, PV2;
  Eigen::MatrixXi F;
  Eigen::VectorXd total_curvature, total_curvature_vis;

  // calculate total curvature
  igl::read_triangle_mesh("../data/BigBuckBunny.ply",V,F);
  igl::principal_curvature(V, F, PD1, PD2, PV1, PV2);
  total_curvature = PV1.array().square() + PV2.array().square(); 
  total_curvature_vis = total_curvature.array().pow(0.01);

  // visualization
  polyscope::init();
  polyscope::options::groundPlaneMode = polyscope::GroundPlaneMode::ShadowOnly;
  auto psMesh = polyscope::registerSurfaceMesh("bunny", V, F);
  auto TotalCurvature = polyscope::getSurfaceMesh("bunny");
  auto ScalarQuantity1 = TotalCurvature->addVertexScalarQuantity("TotalCurvature", total_curvature_vis);
  ScalarQuantity1->setColorMap("jet");
  ScalarQuantity1->setEnabled(true);
  polyscope::options::shadowDarkness = 0.1; 
  polyscope::show();

}
