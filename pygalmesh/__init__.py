# -*- coding: utf-8 -*-
#
# https://github.com/pybind/pybind11/issues/1004
from _pygalmesh import (
    DomainBase,
    Translate,
    Rotate,
    Scale,
    Stretch,
    Intersection,
    Union,
    Difference,
    Ball,
    Cuboid,
    Ellipsoid,
    Tetrahedron,
    Cone,
    Cylinder,
    Torus,
    HalfSpace,
    Polygon2D,
    RingExtrude,
    generate_from_off,
)

from .__about__ import (
    __author__,
    __author_email__,
    __copyright__,
    __license__,
    __version__,
    __maintainer__,
    __status__,
)

__all__ = [
    "__author__",
    "__author_email__",
    "__copyright__",
    "__license__",
    "__version__",
    "__maintainer__",
    "__status__",
    #
    "DomainBase",
    "Translate",
    "Rotate",
    "Scale",
    "Stretch",
    "Intersection",
    "Union",
    "Difference",
    "Ball",
    "Cuboid",
    "Ellipsoid",
    "Tetrahedron",
    "Cone",
    "Cylinder",
    "Torus",
    "HalfSpace",
    "Polygon2D",
    "RingExtrude",
    "generate_from_off",
]
