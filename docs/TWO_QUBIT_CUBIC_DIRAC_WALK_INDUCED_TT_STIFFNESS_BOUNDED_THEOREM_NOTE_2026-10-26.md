# Static spin-2 vacuum stiffness of the supplied two-qubit cubic Dirac walk

**Date:** 2026-10-26
**Type:** bounded_theorem
**Status authority:** independent audit only; no retained status asserted.
**Primary runner:** `scripts/two_qubit_cubic_dirac_walk_induced_tt_stiffness_2026_10_26.py`
**Cached output:** `logs/runner-cache/two_qubit_cubic_dirac_walk_induced_tt_stiffness_2026_10_26.txt`

## Claim boundary

For the supplied walk and supplied metric couplings, this note computes the
coefficient of q^2 in the static second-order vacuum response to a
transverse-traceless (TT) spatial metric perturbation, shows that it is positive
in every computed channel, cubic-anisotropic, and not fixed by the continuum
limit of the coupling. It does **not** derive a Newton constant: the q^0 sector
and the conformal channel, discussed below, block that reading.

## Supplied premises

- **Walk.** The site, walk family, named points b*, b_iso, b_gold and scaling of
  [the continuum-limit note](TWO_QUBIT_CUBIC_DIRAC_WALK_MASSIVE_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-26.md),
  whose exact generator H_a(k) = -rho(f) x(k).Gamma (U = exp(-i H_a) at unit
  spacing, rho = arccos f / sqrt(1 - f^2), Gamma = (tau1, tau2, tau3 sigma_a),
  x = (h1, h2, g1, g2, g3)) is used here. The family itself is that of the
  two-qubit cubic-tick note cited there. Two qubits per site are outside the
  one-qubit axiom and remain a supplied premise.
- **Metric coupling (supplied).** A static spatial metric gamma = 1 + h(x),
  lapse 1, shift 0, symmetric triad e = gamma^{-1/2}. Coupling M1: every hop of
  the spin part alpha_j P_j(k), P_j = rho g_j, is multiplied by the triad at the
  link midpoint, so the O(h) vertex between k and k + q is
  V = -(1/2) eps_ij alpha_i P_j(k + q/2) for h_ij = eps_ij exp(i q.x). The
  flavour part is not modulated. Variants with the same continuum limit:
  M2 (P_j = g_j), M3 (P_j = s sin k_j), M4 (V = -(1/2) eps_ij sin k_j d_{k_i} H_a,
  which also couples the flavour sector). M1 was declared before any coefficient
  was computed; M2-M4 serve only to expose non-uniqueness.
- **Observable (supplied).** The induced static action is identified with the
  energy of the filled lower band of H_a in the background (Sakharov). With
  h = 2 lambda eps cos(q.x), eps:eps = 1, the static Einstein-Hilbert energy per
  volume is lambda^2 q^2/(32 pi G), so a positive q^2 coefficient means positive
  TT stiffness. Lattice units a = tick = 1 with light speed s; physical c = 1
  needs the tick s a, so c_G := a^2/(16 pi G) = 2 c2/s, with c2 the q^2
  coefficient of the second-order energy per volume and lambda^2.

## 1. Exact identities

- For a single TT Fourier mode the cell average of sqrt(gamma) R^(3) at O(h^2)
  is -(1/4) <(d h)^2>, and the O(h) term integrates to zero (both
  polarisations); this fixes the normalisation above.
- The half-density form of the covariant Dirac Hamiltonian with the symmetric
  triad, gamma^{1/4} [-i alpha^a e_a^i (d_i + Gamma_i)] gamma^{-1/4}, equals
  (1/2){alpha^a e_a^i, p_i} + O(h^2) for arbitrary symmetric h(x); the axial
  spin-connection term vanishes at O(h) in symmetric gauge.
- Heat kernel: Gamma_E = -(1/2) log det D^2 with tr a_1 = -R/3 and proper-time
  cutoff s > 1/Lambda^2 gives 1/(16 pi G) = Lambda^2/(96 pi^2) per Dirac fermion,
  i.e. c_G = 1/96 at Lambda = pi/a.
- The same second-order bubble in the continuum (H = alpha.p, minimal-coupling
  vertex, sharp cutoff |k| < Lambda) gives c_G = 13 Lambda^2/(840 pi^2), that is
  52/35 of the heat-kernel value. The continuum estimate is itself
  scheme-dependent at order one.
- The Clifford trace identity
  Tr[P+(a) O P-(b) O] = o^2 (1 + a.b) - 2 (a.o)(b.o), O = o.Gamma, and the
  series of rho and rho' at f = 1 used by the quadrature.

## 2. Continuum limit of the couplings and the bubble formula

**Proposition 1 (conditional on the supplied premises).** For each of M1-M4,
uniformly for |p|, |q| <= P,
(1/a) V(a(p + q/2)) = -(1/2) eps_ij s alpha_i (p + q/2)_j + O(a). For M1-M3 the
O(a) term vanishes (g = s k + O(k^3), rho = 1 + O(k^2)), leaving O(a^2); for M4
it is -(a/2)(eps_ij p_i p_j) W.tau, the metric coupling of the Wilson term.
Midpoint quantisation of a symbol linear in p is Weyl ordering, so the
continuum operator is -(1/4){h_ij(x), s alpha_i p_j}, which by section 1 is the
standard minimal coupling at O(h). This is a symbol-level statement; the
operator-level convergence of the coupled dynamics would follow by the
fibrewise Duhamel argument of the continuum-limit note and is not written out.

**Lemma 2 (contact terms).** An O(h^2) coupling term that is a midpoint-local
function of h (such as the 3h^2/8 of M1) has a vacuum expectation equal to the
sum over x of (h h)(x + n/2) times a translation-invariant constant, which is
q-independent for a Fourier mode. In the continuum the O(h^2) remainder of the
minimal-coupling identity consists of a local term (q-independent), terms
proportional to alpha.(h dh) (zero, because the vacuum current vanishes by
parity) and the axial term (zero by time reversal). Hence c_G is determined by
the second-order bubble of the O(h) vertex alone: proved for M1 and for the
continuum; for M2-M4 it is part of their definition.

**Bubble formula.** Standard second-order perturbation theory with the Clifford
trace gives e2(q) = -int_BZ d^3k/(2 pi)^3 F(k, q/2) + (q-independent contact),
F(k, t) = 2[o^2 (1 + ahat.bhat) - 2 (ahat.o)(bhat.o)] / (E(k + t qhat) + E(k - t qhat)),
ahat = xhat(k + t qhat), bhat = xhat(k - t qhat), E = arccos f. The runner checks
this formula against an independent implementation (exact diagonalisation of
k-chains of i Log(M U0 M), explicit vertex matrices) on an L = 6 lattice, for
M1, M2, M4 and a lapse coupling at b* and for M1 at b_gold (theta > 0).

**Lemma 3 (lapse).** For any Clifford-form generator H = -rho x.Gamma (any b,
theta, twist, or the continuum) and any lapse vertex o(k, t) = c(k, t)[xhat(k) +
t^2 z + O(t^3)] even in t (both the midpoint prescription N H and (1/2){N, H}
are of this form), F(k, t) = O(t^4) pointwise, so the lapse response has no
O(q^2) term. Proof: write the numerator as o^T M(t) o with
M = (1 + ahat.bhat) 1 - (ahat bhat^T + bhat ahat^T), even in t; with
ahat = m + t v + t^2 w + O(t^3), |ahat| = 1, one finds m.v = 0, m.w = -v^2/2,
ahat.bhat = 1 - 2 t^2 v^2 and ahat.m = bhat.m = 1 - t^2 v^2/2, so
m^T M m = O(t^4), and M(0) m = 0 gives (m + t^2 z)^T M (m + t^2 z) = O(t^4). This
agrees with Einstein-Hilbert, for which a static lapse with flat gamma
contributes only a total derivative. It is structural and says nothing specific
about the walk.

## 3. Lattice values (numerical)

The Brillouin-zone integral of the pointwise t^2 coefficient of F (Richardson
extrapolation in t) uses a smooth partition of unity: a periodic midpoint grid
outside a ball at Gamma and a spherical Gauss rule inside, which absorbs the
1/|k| behaviour at the massless node. The source packet's production runs give
convergence certificates of at most 2e-7 relative over grids N = 96, 128, ball
radii 1, 1.4 and two inner rules; these are numerical, not interval-rigorous.
The runner recomputes the b* M1 channels at N = 96 and N = 64, b_iso and the
variants at N = 64, and checks one channel with a plain midpoint rule
extrapolated in h^2 (a different quadrature).

TT channels at theta = 0, in units of 1e-3 (z = q along (001), f = (110),
d = (111); A and B the two polarisations):

| b | coupling | zA | zB | fA | fB | dA = dB | c_G^iso |
|---|---|---|---|---|---|---|---|
| b* | M1 | 8.61015 | 8.30765 | 7.24188 | 6.93391 | 6.64891 | 7.36673 |
| b* | M2 | | | | | | 3.60420 |
| b* | M4 | | | | | | 9.52490 |
| b_iso | M1 | | | | | | 6.63451 |

- **Sign.** c_G > 0 in every computed channel, coupling and parameter point.
- **Cubic anisotropy.** The polarisation-summed stiffness
  K(qhat) = A + B sum_a qhat_a^4 + C qhat_x^2 qhat_y^2 qhat_z^2 is the general
  O_h-invariant even polynomial of degree at most 6 on the sphere; the fit on
  z, (110), (111) predicts the generic (1,2,3) direction (a non-tautological
  test), and the (111) polarisations are degenerate. The isotropic projection
  c_G^iso = (1/2)(A + 3B/5 + C/105) is a convention used to compare with
  Einstein-Hilbert. K varies by about 25% over directions at b* (55% at b_iso in
  the source packet), so the induced static action is not Einstein-Hilbert at
  O(d^2): it carries order-one cubic, Lorentz-violating terms.
- **Non-uniqueness (underdetermination with explicit witnesses).** M1-M4 share
  the continuum vertex of Proposition 1 but their c_G^iso differ by a factor 2.6
  (M2 to M4 at b*; M3 gives 7.13e-3 in the source packet). The lattice number is
  fixed only once the ultraviolet completion of the coupling is fixed, because
  c_G integrates the vertex over the whole zone while Proposition 1 constrains
  only its O(p) part.
- **Comparison with the continuum.** In heat-kernel language c_G^iso(M1)
  corresponds to an effective cutoff Lambda_eff = sqrt(96 pi^2 c_G)/a = 0.84 pi/a
  (b*) and 0.80 pi/a (b_iso), inside the pre-declared order-one window.
- **Lapse.** The O(q^2) lapse response vanishes numerically (below 1e-10 in the
  runner), as Lemma 3 requires.

## 4. Why no Newton constant is claimed

- The source packet's diagnostics (not pre-registered, M1 only) give an induced
  vacuum energy of about -4.03 a^-4 and a destabilising TT q^0 term of about
  -2.39 a^-4 from the mismatch between the bubble plus contact term and the
  covariant sqrt(gamma) structure (a fixed coordinate lattice does not count
  modes covariantly). At physical q much smaller than 1/a both dominate the
  O(q^2) stiffness by a factor (q a)^-2. They would have to be cancelled by other
  sectors, which nothing here supplies.
- The conformal (Newtonian) channel, which carries the known wrong sign, was not
  computed.
- The static action is not Einstein-Hilbert (anisotropy above).
- If those three conditions were met, N_f copies of the walk would give
  a/l_P = sqrt(16 pi N_f c_G), that is 0.61 sqrt(N_f) for M1 at b* and
  0.43-0.69 sqrt(N_f) across M1-M4. This conversion is conditional arithmetic,
  not a derived value of l_P/a, and other sectors would add their own
  contributions to 1/G.

The heat-kernel half-factor of section 1 agrees with the determinant
half-factor addendum in
`UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17.md`,
which is checked there by its own runner.

## Claim types

| Claim | Type |
|---|---|
| EH normalisation, half-density minimal coupling at O(h), heat-kernel and sharp-cutoff coefficients, Clifford trace, rho series | exact |
| continuum limit of M1-M4 (symbol level) | proved, conditional on the supplied premises |
| contact-term lemma | proved for M1 and the continuum; definitional for M2-M4 |
| bubble formula | standard; independently cross-checked by exact diagonalisation |
| lapse lemma | proved; numerics agree |
| c_G values, anisotropy coefficients, Lambda_eff | numerical with convergence estimates, not interval-rigorous |
| positivity in all computed channels | numerical |
| factor-2.6 spread across couplings | underdetermination with explicit witnesses |
| coupling M1-M4 and the vacuum-energy identification | supplied premises |
| induced Newton constant, a/l_P | not claimed |

## Source recovery

This is the canonical, narrowed form of campaign block C8 of PR #9831, preserved
at the frozen head `e294c1dc745dad0c95b4c8688efc6f3f0be03613` under
`.claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C8/` (note,
review, pre-registration in the worklog, production results JSON, report and
review scripts). The helper module is that block's reviewed core with only
docstring edits; the runner re-uses its exact-diagonalisation and exact
checks. The block's separate-context review (same model family as the author)
reproduced c_G^iso(M1, b*) by two other quadratures, accepted the vertex,
normalisation, contact lemma and lapse lemma, and corrected the headline and the
light-speed-point analysis; those corrections are included. Not carried over as
checked claims: the massive-member dependence, the light-speed point b_gold
(theta -> 0 limit 3.889e-2, subject to the two-tick temporal-doubler caveat of
the continuum-limit note), and the q^0 diagnostics quoted in section 4.
