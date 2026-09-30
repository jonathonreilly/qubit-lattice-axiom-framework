# T66 pre-registration (written BEFORE running the degree-2 solve)

Author: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check, not a referee).

## What is tested

Test A1-planar: the specification of the map's test A1 restricted to the planar sector
S1 = {h_xx, h_yy, h_zz} (all on sites, functions of x only; y-, z-dependence and face
components h_xy, h_xz, h_yz set to zero after differentiation). Restriction gives a NECESSARY
condition for the full 3D problem: any range-r local 3D solution restricts to a range-r local
planar solution (unknown families below already include every monomial that can survive the
restriction, see engine notes). A PASS here does NOT imply a 3D PASS.

Fixed pieces (block 112 / block 62, reconstructed in real space and controlled against the
landed runner's stencil):
- C1[N] = K sum_n (-Delta_x N)(n) (h_yy + h_zz)(n)   (R1 in S1; lapse N on sites)
- T2[N] = (1/4 alpha) sum_n N(n) [P_xx^2 + P_yy^2 + P_zz^2 - c (P_xx+P_yy+P_zz)^2], c = 1/2
- R2 in S1 = (1/2) sum_n (D h_yy)(D h_zz) (from the landed symbol, hand-expanded)
- G1[xi] = sum_n P_xx(n) * 2 (xi(n) - xi(n-1)), xi on x-bonds
- degree-1 closure {C[N],C[M]}_1 = G1[xi0], xi0(n) = (K/4alpha)(N(n+1)M(n) - N(n)M(n+1))

Unknown (all local, translation-invariant, support radius r in sites, time-reversal fixed:
C even in P, G odd in P):
 V2[N] (quadratic potential with lapse; constraint V2[1] = K R2), T3[N] (P P h cubic kinetic),
 G2[xi] (P h xi), xi1 (linear in h, antisymmetric in N,M), chi (linear in P, antisymmetric).
Degree-2 identity (first-class form):
 {T2[N],V2[M]} + {V2[N],T2[M]} + {C1[N],T3[M]} + {T3[N],C1[M]}
     = G2[xi0(N,M)] + G1[xi1(N,M;h)] + C1[chi(N,M;P)].

## Pass and fail readings (fixed now)

- CONTROL 1 (engine): degree-1 bracket reproduces G1[xi0] exactly for c = 1/2, and fails for
  c != 1/2 (block 112 T1). If not, the engine is wrong and nothing below counts.
- CONTROL 2 (uniform lapse, "reading U"): restrict to M = 1 (all N). Expected solvable if the
  engine and ansatz are sane (the continuum solution exists and is local). If it fails, the
  ansatz/engine is too tight and a FAIL of the main test is not informative.
- MAIN, r = 1, 2, 3:
  - PASS_r: the linear system (unknowns above, V2 normalisation as equations) is consistent in
    exact modular arithmetic AND float least squares residual ~ 1e-10. Reading: no planar
    obstruction at range r; the wall's expected FAIL is NOT found in this sector; the obstruction,
    if any, lives in transverse (3D) structure or in matter coupling.
  - FAIL_r: inconsistent (a left-null certificate exists), stable across two primes and float.
    Reading: an order-2 obstruction exists already in the planar sector at range r. Report the
    certificate's monomial support (the failing terms) and whether it persists as r grows.
  - MIXED (FAIL at small r, PASS at larger r): the obstruction is a range obstruction, not an
    algebraic one; report the minimal r.
- If PASS: add the continuum-limit conditions (G2 -> Lie derivative in the ADM variables g=1+h,
  T3 -> DeWitt expansion) as extra equations and re-run; a PASS that only exists with G2 = 0
  (no self-coupling) counts as a FAIL for gravity.

## Prediction (mine, before running)

Prior: FAIL at r = 1 (about 65 percent), 40 percent that FAIL persists to r = 3. Reason: the planar
sector is a 1D reparametrisation system; the lapse-lapse bracket must produce (N M' - M N')/a^2
with a^2 = 1 + h_xx on bonds, and the lattice Leibniz failure should show up as a residual
involving h_xx(n) vs h_xx(n+1). Controls decide whether a FAIL is trustworthy.
