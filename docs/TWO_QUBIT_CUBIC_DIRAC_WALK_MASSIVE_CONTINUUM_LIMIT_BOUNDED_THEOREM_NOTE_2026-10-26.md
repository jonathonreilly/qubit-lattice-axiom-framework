# Massive continuum limit of the supplied two-qubit cubic Dirac walk

**Date:** 2026-10-26
**Type:** bounded_theorem
**Status authority:** independent audit only; no retained status asserted.
**Primary runner:** `scripts/two_qubit_cubic_dirac_walk_continuum_limit_2026_10_26.py`
**Cached output:** `logs/runner-cache/two_qubit_cubic_dirac_walk_continuum_limit_2026_10_26.txt`

## Supplied premises

Nothing below is derived from the framework axioms. The premises are named and
stay supplied.

- **Site.** Each site carries C^2 (flavour, Pauli matrices tau) (x) C^2
  (spin, Pauli matrices sigma), and proper cubic rotations act as 1 (x) D(R).
  Two qubits per site lie outside the one-qubit site algebra of the axioms; the
  enlargement is a parked owner decision and is not adopted here.
- **Walk family.** The Clifford cell family of
  [the two-qubit cubic-tick note](TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md):
  U(k) = f + i(h1 tau1 + h2 tau2) + i tau3 (x) g.sigma with
  (f, h1, h2) = F phi(k), phi = (1, sum c, sum cc, c1 c2 c3), c_a = cos k_a,
  g = b0 v0 + b1 v1 + b2 v2 and F^T F = G(b). From that note this note imports
  unitarity and exact cubic covariance of the family, and the fact that G(b)
  determines F up to a constant O(3) rotation. The cone speed is
  s = b0 + 2 b1 + b2.
- **Scaling (a choice).** Lattice spacing a, one walk step per tick of length
  a, b held fixed, mass angle theta = m a with m fixed, mass direction hhat in
  the (tau1, tau2) plane held fixed.
- **Named points.** b* (s = 0.91442, the explicit member of the two-qubit
  note), b_iso (s = sqrt(2/3), quartic-isotropic) and b_gold (s = 1, the
  light-speed member). Statements hold for any admissible b under the
  hypotheses each one states.

## 1. The massive walk is already in the family (exact)

Every member at fixed b is O F0 with O in O(3) and F0 phi0 = e_f a massless
member (U(0) = 1). Writing O e_f = (cos theta, sin theta hhat),

```
U_{theta,hhat}(k) = M U0(k) M,   M = exp(i theta hhat.tau / 2).
```

M is a constant flavour coin commuting with every 1 (x) D(R), so covariance is
kept; U(0) = exp(i theta hhat.tau) gives rest mass theta/a = m. The mass is
therefore the O(3)-orbit coordinate that the two-qubit note fixed to zero, not
a new parameter. The massless member carries the flavour Wilson vector W with
|W| = |s| sqrt(1 - s^2) exactly. The twist angle chi is the angle between hhat
and W (chi = 0: Wilson-aligned mass; chi = pi/2: maximal twist).

## 2. Vertex lemma: nodes and gap minima sit at the eight TRIMs (exact)

For every member f is multilinear in (c1, c2, c3) and the bands are
cos omega = f, each doubly degenerate. A multilinear function on [-1, 1]^3
attains its extrema at vertices, which are the eight time-reversal-invariant
momenta (TRIMs) k_a in {0, pi}. Hence:

1. min omega and min (pi - omega) over the Brillouin zone are attained at
   TRIMs, so a member has a node of either type iff some TRIM is one. If no two
   TRIMs adjacent on the cube are nodes of the same type, every node is a TRIM
   (otherwise f is constant on that edge). b*, b_iso and b_gold satisfy this:
   only Gamma has f = 1, and at b_gold the f = -1 set is the three axis points
   X, which pairwise differ in two coordinates.
2. Global dispersion bound:
   1 - cos omega(k) >= (1 - cos theta) + c_theta sum_a (1 - cos k_a), with
   c_theta = min over TRIMs K != 0 of [cos theta - cos omega_K(theta)]/(2|K|),
   |K| the number of pi entries. The difference of the two sides is multilinear
   in x_a = 1 - c_a in [0, 2], vanishes at x = 0 (where f = cos theta) and is
   non-negative at the other vertices by the choice of c_theta, so it is
   non-negative everywhere. At theta = 0 the X-vertex term equals s^2, the cone
   coefficient.

TRIM data of the massless member (exact in b): cos theta_X = 1 - 2 s^2 at the
three axis points, cos theta_M = 1 - 8 s (b0 - b2) at the three face points,
cos theta_R = 1 - 6(3 b0^2 + 2 b0 b2 + 3 b2^2 - 8 b1^2) at the corner. At b_iso
these are -1/3, -7/9 and a value in (-1, 1); at b_gold cos theta_X = -1 exactly
(massless axis pi-modes) and the face and corner values exceed -1; the b*
values are floating-point evaluations of explicit algebraic numbers, at least
0.83 rad from 0 and pi. The Jacobian determinants of g at the eight zeros of g
(s^3 at Gamma, -s (b0 - b2)^2 on the axes, (b0 - b2)^2 (b0 - 2 b1 + b2) on the
faces, -(b0 - 2 b1 + b2)^3 at the corner) have signs summing to zero at the
named points, and every node is a Dirac node (the tau3 = +-1 blocks carry
opposite index), so the walk is vector-like.

**Massive doublers.** At a TRIM K, g(K) = 0, so U(K) is a pure flavour element
and |omega_K(theta) - theta_K| <= theta for all hhat (bi-invariance of the
S^3 metric). At b_gold, U0(X) = -1 gives U_theta(X) = -U_theta(0) exactly: the
X triplet becomes three massive pi-modes at quasienergy pi - m a.

## 3. Exact generator and its expansion

**Theorem 1 (exact generator).** Wherever f > -1,
U(k) = exp(-i a H_a(k/a)) with H_a(p) = -(omega/(a sin omega)) X(a p), X the
Clifford part, and H_a(p)^2 = (omega/a)^2 1 exactly. omega/sin omega is
real-analytic at cos omega = 1, so H_a is real-analytic near the physical
node.

**Theorem 2 (expansion).** With alpha_a = -tau3 sigma_a, beta = -hhat.tau and
H_D(p) = s alpha.p + m beta,

```
H_a(p) = H_D(p) + (a/2) |p|^2 W.tau + R_a(p),   ||R_a(p)|| <= C3 a^2 (|p| + m)^3
```

for a(|p| + m) <= kappa0. The displayed coefficients are exact
(g = s k + O(k^3), the gradient of phi vanishes at every TRIM, and the flavour
part is theta hhat - (k^2/2) W + O(3)). C3 and kappa0 exist by analyticity.
Their values are not computed: the runner reports sample maxima of the
remainder ratio (lower estimates of the supremum, about 0.03-0.05 on |p| <= 2,
m = 1), and kappa0 has no computed value.

**Dirac identification (exact).** V = ((tau1 - tau3)/sqrt 2) (x) 1 is a constant
unitary commuting with 1 (x) D(R); it maps alpha_a to tau1 (x) sigma_a and
beta = -tau1 to tau3 (the standard Dirac representation). So the cubic spin
action is the Dirac spinor rotation.

## 4. Continuum-limit theorem

Use the band-limited embedding J_a: phi_hat -> psi_hat(k) = a^{-3/2} phi_hat(k/a)
of L^2(R^3; C^4) into l^2(Z^3) (x) C^4 (isometric on momentum support in
(-pi/a, pi/a)^3), the band-limit projection P_a, and
T_a(t) = (V J_a)^* U_theta^{floor(t/a)} (V J_a) P_a.

**Theorem 3 (conditional on the supplied premises).**

1. *Strong convergence.* For every phi in L^2,
   sup over 0 <= t <= T of ||T_a(t) phi - exp(-i t H_D) phi|| -> 0 as a -> 0
   (fibrewise convergence, the uniform bound 2, dominated convergence and
   P_a -> 1). The same holds for lattice translations by floor(x/a).
2. *Rate on band-limited states* (momentum support |p| <= P). For a(P + m) <= kappa0,
   ||T_a(t) phi - exp(-i t H_D) phi|| <= [a E_P + t((|W|/2) a P^2 + C3 a^2 (P + m)^3)] ||phi||,
   with E_P the supremum of ||H_a|| on that support; the first term is the
   floor (t - a floor(t/a)) ||H_a||, the second comes from Duhamel's formula.
   The O(a t) coefficient |W| P^2 / 2 = |s| sqrt(1 - s^2) P^2 / 2 is pinned to
   the axis-doubler gap (0.185 P^2 at b*, 0.236 P^2 at b_iso). C3 and kappa0
   are existential constants, as in Theorem 2.
3. *Light speed.* At b_gold, W = 0 and the error is O(a^2) for every twist.
4. *Maximal twist.* At chi = pi/2, W.tau = |W| Gamma_perp anticommutes with alpha
   and beta, and the momentum-dependent chiral rotation
   V_a(p) = exp((phi/2) beta Gamma_perp), tan phi = a |W| p^2 / (2 m), maps
   H_D + (a/2)|W| p^2 Gamma_perp to s alpha.p + sqrt(m^2 + a^2 |W|^2 p^4 / 4) beta
   exactly. The O(a) error is then removable by this p-dependent
   identification (O(a^2 t (p^4/m + (p + m)^3)) plus the floor term); the rate
   is not uniform as m -> 0.
5. *Wilson-aligned mass.* For cos chi != 0 the spectrum itself shifts:
   E_a^2 = E^2 - a m |W| cos chi p^2 + O(a^2). Since unitary conjugation does not
   change the spectrum and the matching distance of unitary spectra is bounded
   by the operator-norm distance, no identification, constant or p-dependent,
   removes the O(a t) error at times where |sin t E| is bounded away from zero.

The runner confirms these rates on 120 sampled momenta (|p| <= 2, m = 1,
t = 1, a from 0.04 to 0.005): slopes near 1 for b* and b_iso at both twists
with a constant identification; near 2 with V_a(p) at maximal twist; near 1
with V_a(p) at Wilson alignment; near 2 at b_gold; and the bound of item 2 holds
at every a with the sampled C3. These are numerical confirmations of the
proved rates, not certified constants.

## 5. Doubler decoupling

- **Momentum.** For band-limited phi the lattice momentum support is
  |k| <= a P and the walk conserves k, so the weight near any TRIM K != 0 is
  exactly zero for all times. A Gaussian packet of physical width Sigma has
  weight at most 3 erfc(kappa sqrt 2 Sigma / a) outside |k_a| < kappa; the
  runner checks the one-dimensional tail against an FFT.
- **Energy.** By the vertex lemma every lattice momentum with some
  |k_a| >= pi/2 has quasienergy at least arccos(1 - c_theta), so energy at
  least arccos(1 - c_theta)/a; c_theta -> c0 > 0 with c0 = 0.264, 0.318, 0.296
  at b*, b_iso, b_gold.
- **Temporal doublers at b_gold.** The X modes sit at energy pi/a - m in the
  principal branch and decouple for every fixed phi. On the X sector
  U^n = (-1)^n exp(-+ i n theta); for a two-tick clock (U^2) they would sit at
  quasienergy -2 m a and reappear as three extra light Dirac species of mass m.
  So decoupling at b_gold depends on resolving the single-tick clock. This
  caveat does not arise at b* or b_iso, which have no pi-modes.

## 6. Dispersion and Lorentz violation (exact symbolic, numerically confirmed)

```
E_a^2(p) = m^2 + s^2 |p|^2 - a m |W| cos chi |p|^2
           + a^2 [alpha |p|^4 + beta sum_a p_a^4 - (s^2/3) m^2 |p|^2] + O(a^3),
alpha = s (s^3 + 3 b0 - 6 b1 - 9 b2)/12,   beta = -s (b0 - b1 - 2 b2)/3.
```

- The limiting speed is s sites per tick; choosing the tick as s a would set
  c = 1.
- The O(a) term is isotropic: for one species it only renormalises the speed,
  c'^2 = s^2 - a m |W| cos chi, a mass-dependent speed that violates Lorentz
  invariance only relative to other species. It vanishes at maximal twist and
  at b_gold.
- The first single-species violation is O(a^2): the cubic anisotropy
  coefficient beta is 0.0403 at b*, 0 at b_iso and 7/6 - sqrt5/2 = 0.0486 at
  b_gold. Continuous-rotation breaking of the generator enters only through the
  k^3 anisotropy (b1 + 2 b2 - b0)/6 k_a^3 of g, which vanishes on the
  quartic-isotropy plane b0 = b1 + 2 b2.

## 7. Boost generators (exact lemma only)

For any matrix function H(p) and K_j = (1/2){x_j, H} with x = i grad_p,
[K_j, P_l] = i delta_jl H, [K_j, H] = (i/2){H, d_j H}, and
[K_1, K_2] = -((1/2){H, d_1 H} d_2 - (1/2){H, d_2 H} d_1 + (1/4)[d_1 H, d_2 H])
(exact symbolic check). For a Clifford fibre {H, d_j H} = d_j(E_a^2). With
H = H_D this reproduces the speed-s Poincare algebra; for H_a the defects are
explicit operators of order a (order a^2 at b_gold or, for [K, H], at maximal
twist). Group-level convergence of lattice boosts is not proved here and is not
claimed.

## Claim types

| Claim | Type |
|---|---|
| massive members are M U0 M; mass is the O(3)-orbit coordinate | exact symbolic |
| vertex lemma, node locations, dispersion bound, doubler bounds, U_theta(X) = -U_theta(0) at b_gold | proved |
| TRIM data at b_iso and b_gold; Jacobian signs | exact algebraic |
| TRIM data at b* | numerical values of explicit algebraic numbers |
| exact generator; expansion coefficients; dispersion through O(a^2); Dirac identification; boost lemma | exact |
| existence of C3, kappa0 | proved (analyticity) |
| values of C3; convergence slopes | numerical, sample-based |
| continuum-limit theorem items 1-5, doubler decoupling | proved, conditional on the supplied premises |
| group-level boost convergence | not claimed (open) |

## Scope

The theorem concerns the supplied walk on the supplied two-qubit site with the
declared scaling. It does not derive the site, the walk, the tick-to-time
identification or any physical particle identification from the axioms, and it
does not address interacting dynamics. Quantum-walk continuum limits are
textbook in other settings (Arrighi-Forets-Nesme, J. Phys. A 47 (2014),
arXiv:1307.3524; D'Ariano-Perinotti, PRA 90, 062106 (2014); Bisio-D'Ariano-Tosini,
Ann. Phys. 354, 244 (2015)); the Duhamel and fibrewise arguments are standard,
and twisted-mass O(a) improvement is lattice-QCD practice. Specific here: the
mass as the O(3)-orbit coordinate, the multilinearity vertex lemma, the O(a)
coefficient pinned to the doubler gap, the twist dichotomy, and the temporal
doublers of the light-speed member.

## Source recovery

This is the canonical form of campaign block C7 of PR #9831, preserved at the
frozen head `e294c1dc745dad0c95b4c8688efc6f3f0be03613` under
`.claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C7/`. The runner
merges that block's reviewed exact and numeric scripts with only packaging
edits (sampling reduced from 4000 to 1500 points in one sanity check). Its
separate-context review (same model family as the author) re-derived the O(a)
term by a different route, accepted the vertex lemma with the adjacency
hypothesis, and fixed the quantifiers on C3 and kappa0 and the non-aliasing
condition in item 5; those corrections are included. That block also found the
arccos-squared series defect in the two-qubit note's runner; the correction
already landed on main and is not part of this note. Not carried over: the
numerical boost-defect slopes and the high-precision sextic comparison.
