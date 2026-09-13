# Nonlinear hyperdiagonal compatibility: working derivation before checks

2026-09-13. This is independent local geometry on the same supplied action,
not a downstream physical conclusion from the unreviewed Block7 spectrum.
Its target is the accidental extra null mode, not the four vertex gauges.

Vary only the squared main hyperdiagonal of each unit cube by lambda_x,
leaving every axis, face and body edge at its flat value. In one path simplex
the metric becomes I+(lambda_x/2)(e_first e_last^T+e_last e_first^T), positive
for |lambda_x|<2. A hinge containing the full hyperdiagonal has vertices
0,u,1111, with m=|u| in {1,2,3}, area
A_m=sqrt(m(4-m)/4-lambda_x^2/16). There are 8 hinges with m1 or3, and 6 with m2.
Their simplex stars lie entirely in the same cube; their sizes are 6 and4.

From the inverse metric and barycentric normals, proposed exact angles are

theta_1=acos(sqrt((4-lambda^2)/(2(8-lambda^2)))),
theta_2=acos(-2lambda/(8-lambda^2)).

The corresponding deficits are d1=2pi-6theta1 and d2=2pi-4theta2.
Schlaefli gives the exact action derivative per cube

f'(lambda)=-(lambda/16)[8 d1/A1+6 d2/A2].

The first manual expansion gives
f'=3lambda^2/8+lambda^3/8+O(lambda^4), hence
f=lambda^3/8+lambda^4/32+O(lambda^5).
This is a conjectured expansion at this checkpoint, to be independently checked.
The action variation along arbitrary hyper-only fields is additive over cubes,
since each derivative involves only its own full-hyperdiagonal hinge star.

If confirmed, every nonzero pure-hyperdiagonal linearized tangent fails the
second-order compatibility equation for a C^2 family of stationary Regge
solutions: the hyperdiagonal Hessian row vanishes identically for all directions,
so second-order corrections to other edge lengths cannot cancel the local
3v_x^2/8 coefficient in that equation. This is a precise linearization
instability of this special flat complex, not a physical energy instability,
not a no-go for Regge gravity, and not a contradiction of the framework axioms.

Next verify all normal-angle formulas against direct hinge Gram projections,
check the Taylor coefficients exactly, and verify a small nonlinear geometric
fixture. Then inspect mixed first-order metric/hyperdiagonal directions before
any wider conclusion. Tilted backgrounds, nonlinear constraint selection,
other simplicial variables, improved actions and different physical geometry
maps remain live alternatives.
