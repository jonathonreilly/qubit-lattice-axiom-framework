---
claim_id: the_tick_fraction_and_every_edge_answering_the_full_hinge_sum_fix_the_second_order_clock_rate_so_ppn_beta_is_one_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Static, spherically symmetric exterior of a count geometry under the tick-fraction rule: the site tick fraction N and every spatial edge are response variables of the full (untruncated) static hinge sum S/dt = (1/8 pi G) sum_e N_e l_e delta_e, whose continuum form is (1/16 pi G) int N sqrt(h) R3. Exact (sympy, continuum): with h = a^2 dr^2 + b^2 r^2 dOmega^2, the tick equation is 2a (r(1 - 1/a^2))' = 0, so a = (1-2m/r)^(-1/2); the radial-edge equation then gives N = sqrt(1-2m/r) (N -> 1); the tangential-edge equation holds identically. The exterior is a one-parameter family for any source coupling, and in isotropic radius it reads g00 = -(1 - 2U + 2U^2 + ...), g_ij = (1 + 2U) delta_ij: PPN beta = 1 and gamma = 1, Nordtvedt eta = 0. The conformal (density-only) family phi = 1 + A/r, N = 1 - C/(r+A) satisfies the tick and density equations for every A, C; the radial-edge equation is 4r(2A - C)/(A + r)^2 = 0 and forces C = 2A. In that family beta - 1 = (gamma - 1)/2, so the second order is slaved to the first once the edges respond. Finite diagnostic (radial ODE, uniform ball): if only the site density responded (edges locked conformal), gamma - 1 = +0.60 GM/R and beta - 1 = +0.30 GM/R, body-dependent. A quadratic truncation of the hinge sum leaves beta undetermined (beta = 1/2, 1, 3/2, 0 for N = 1+Phi, e^Phi, 1/(1-Phi), sqrt(1+2Phi)). Not derived: the discrete-to-continuum error at order (a/r)^2, the interior (static dust needs stresses), the vector and tensor sectors, G in SI units."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_tick_fraction_and_every_edge_answering_the_full_hinge_sum_fix_the_second_order_clock_rate_so_ppn_beta_is_one_2026_10_23.py
---

# The tick fraction and every edge answering the full hinge sum fix the second-order clock rate, so PPN beta is one

Claim type: bounded_theorem.
Primary runner: `scripts/the_tick_fraction_and_every_edge_answering_the_full_hinge_sum_fix_the_second_order_clock_rate_so_ppn_beta_is_one_2026_10_23.py` (15 PASS, 0 FAIL, ~1 s, small memory).

## Question

The tick-skip-gamma probe showed that the tick-fraction rule ("a site's tick fraction is a response variable: like the edges, it takes the value that makes the total phase stationary") gives gamma = 1 at first order. Does the same rule fix the second-order clock rate, g00 at order (GM/r)^2, and does it give PPN beta = 1? The rule has to decide this itself: how the source responds to its own field, and whether field energy sources the hinge sum. No metric or field equation is imported as the answer.

## Setup (rules used, rederived where used)

- CL-3 response: the full hinge sum. It is kept exact, not truncated at quadratic order. Its static prism reduction, from tick-skip-gamma, is S/dt = (1/8 pi G) sum_e N_e l_e delta_e. The timelike hinge over spatial edge e has area l_e times the endpoint-averaged taken-tick time, and its deficit is the 3D deficit. Regge's limit sum l delta -> (1/2) int sqrt(h) R3 gives S/dt -> (1/16 pi G) int N sqrt(h) R3.
- The tick-fraction rule: N (taken ticks per reference tick) is varied as a site response.
- CL-3: every spatial edge is a response variable. In spherical symmetry the edges reduce to a radial factor a(r) and a tangential factor b(r).
- Readout: N is proper time per reference tick (the same identification tick-skip-gamma used), so g00 = -N^2.
- Source: a record's phase per taken tick (-m N), or any variant. It enters only through the exterior integration constant.

## Results

### Theorems (exact, sympy)

1. **The rule decides the nonlinear completion.** The tick equation is the Hamiltonian constraint 2a (r(1 - 1/a^2))' = 0, which gives a = (1-2m/r)^(-1/2) with one constant m (A4, A5). The radial-edge equation then gives N = C1 sqrt(1-2m/r), with C1 = 1 from N -> 1 (A6). The tangential-edge equation adds nothing (A7). Schwarzschild-form N and a = b in isotropic radius solves all three (A1).
2. **beta = 1, forced** (A8, A9). In isotropic radius, g00 = -(1 - 2U + 2U^2) and g_ij = (1 + 2U) delta_ij, with U = m/rho and m the Kepler mass. So beta = gamma = 1 and Nordtvedt eta = 4 beta - gamma - 3 = 0 (C2).
3. **Why the second order is slaved to the first** (A2, A3, B1). Every conformal pair phi = 1 + A/r, N = 1 - C/(r+A) solves the tick equation and the density (trace) equation. Only the anisotropic radial-edge equation, E_a = 4r(2A - C)/(A + r)^2, selects C = 2A. Across the family beta = 1/2 + A/C and gamma = 2A/C, so beta - 1 = (gamma - 1)/2. gamma = 1 and beta = 1 are one condition: every edge answers the hinge sum.
4. **The source question is answered.** Field energy is not a separate source. The full hinge sum already contains the self-coupling: outside the source, the edge equation reads div(phi^2 grad N) = 0, a field-energy term with a coefficient fixed by the rule. Adding field energy again would double-count. The tick fraction multiplying the source, or a record that also counts sites (-m N Omega^k), changes only the relation between m and the bare source, never beta (B3, INFO).

### Finite diagnostics

- **Density-only response** (B4). Here the edges are locked to conformal and only the site density and tick fraction respond. For a uniform ball the result is gamma - 1 = +5.99e-4 and beta - 1 = +3.00e-4 at GM/R = 1e-3, scaling as 0.60 and 0.30 GM/R. This is body-dependent and violates the strong equivalence principle. It is not the rule, because CL-3 edges respond.
- **Quadratic truncation** (B2). Truncating the hinge sum to linear field equations makes beta depend on the choice of field variable: 1/2, 1, 3/2 or 0. The rule's hinge sum is not truncated, so this freedom does not exist.

### Against measurement (test only)

- Full rule: beta - 1 = 0, inside the |beta - 1| < ~1e-4 bound from perihelion and lunar ranging. Nordtvedt eta = 0 meets lunar ranging.
- The density-only option would give beta - 1 ~ 6e-7 for the Sun. That is also inside the bound, so the solar-system data alone does not discriminate. Compact bodies (GM/R ~ 0.1-0.2) would.

## Proposed working rule and gate

- No new rule. The tick-fraction rule plus CL-3 (all edges respond, full hinge sum) suffices.
- Gate for the tick-fraction rule, updated:
  - (1) no measured number is chosen;
  - (2) no observed structure is inserted;
  - (3) beta = 1 and eta = 0 are predictions the rule was not built for (it was built on the first order only);
  - (4) bends CL-1 (every site every tick), with the axioms unchanged.
- PASSES on beta.

## Smuggling review

Supplied, not forced:
- that the static prism reduction stays exact at nonlinear order (the trapezoid hinge area is exactly linear in endpoint N; the deficit = 3D deficit for static prisms is carried over from tick-skip-gamma);
- the continuum limit (discretisation corrections O(a^2/r^2), not computed);
- the readout g00 = -N^2, with perihelion read through a record phase -m int sqrt(N^2 - Omega^2 v^2) dt;
- asymptotic flatness (N -> 1);
- spherical symmetry.

Forced: the one-parameter exterior, beta = gamma = 1, eta = 0, and beta - 1 = (gamma - 1)/2 on the conformal family. No Schwarzschild metric or GR field equation is input; the solution is derived from the rule's Euler-Lagrange equations.

## Boundary

- The interior is not built. Static pressureless records cannot be stationary, so a holding stress is needed and its rule is open.
- No lattice-level nonlinear check: the 14^3 Kuhn grid of tick-skip-gamma was not reused at second order.
- No frame dragging, waves or vector sector.
- G in SI units is not fixed (the count-Jacobson tension is unchanged).

## Uses / narrows

- Uses: agents/tick-skip-gamma (static prism reduction, readout, gamma = 1) and CANDIDATE_LAWS_v3 CL-3.
- Narrows: the tick-fraction rule's "beta UNTESTED" now reads beta = 1, forced given that all edges respond and the hinge sum is untruncated.
- Sharpens: the isotropic consistent truncation of tick-skip-gamma C4 is exact at first order only. At second order the anisotropic edge equation is what fixes C = 2A.
