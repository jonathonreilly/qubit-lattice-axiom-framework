# The merged touching at the handover (exact, 2026-09-26)

Comparator of open PR 9350 (J_x = J_y = 1, J_z = J). At kappa_h^2 = J/[4(2 - J)] the plane family f1 + f2 = 1 hands over to f1 + f2 = 2 f3 at (x_h, 1 - x_h, 1/2) with cos 2 pi x_h = J - 1. There D = det H and its gradient vanish exactly and the Hessian has rank 1: at J = 1, 4 pi^2 * 384 along (1, -1, 0); at J = 3/2, 4 pi^2 * 1596.

With u = d1 - d2 (weight 2), v = d1 + d2, t = d3 (weight 1), at J = 1 the lowest weighted part is
D = 384 pi^2 u^2 + 256 pi^3 u t (v - t) + 64 pi^4 (v^2 - v t + t^2)^2 + (higher weighted order).
Completing the square in u leaves 64 (v^2 - vt + t^2)^2 - (128/3) t^2 (v - t)^2, whose quartic in s = v/t has no real roots: the form is positive definite. So the touching disperses linearly along (1, -1, 0) and quadratically across the transverse plane, consistent with the landed discrete fluxes of +-2 there.

Open: the charge (degree of the effective d-vector map, not only D), the local form for general J, and an interval-certified exact count at kappa_h (the Hessian test of open PR 9350 fails there; a weighted lower bound is needed).
