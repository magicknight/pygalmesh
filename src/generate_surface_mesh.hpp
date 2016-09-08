#ifndef GENERATE_SURFACE_MESH_HPP
#define GENERATE_SURFACE_MESH_HPP

#include "domain.hpp"

#include <memory>
#include <string>

namespace frentos {

void generate_surface_mesh(
    const std::shared_ptr<frentos::DomainBase> & domain,
    const std::string & outfile,
    const double bounding_sphere_radius = 0.0,
    const double angle_bound = 0.0,
    const double radius_bound = 0.0,
    const double distance_bound = 0.0,
    const bool verbose = true
    );

} // namespace frentos

#endif // GENERATE_SURFACE_MESH_HPP
