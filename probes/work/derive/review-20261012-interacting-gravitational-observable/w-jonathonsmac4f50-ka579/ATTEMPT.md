# J:derive:review-20261012-interacting-gravitational-observable:a1

Worker: Claude Sonnet 5.5, same family as every source. Unrefereed. Result: PARTIAL.

I read `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines, in full) and
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines, in full) on current main
(a77a3449c9) before choosing premises.

## In plain words

1. The earlier R9-2 attempt already builds, for a one-dimensional two-body law, a stress whose
   energy total is the full Hamiltonian (binding energy included) and whose first moment is the
   boost generator. In that law bound bodies of different binding fall the same way, as long as
   they stay in the "box" range of momenta. That work is real but sits on the lane's supplied model.
2. I show that the fall of a body in a uniform field depends on the stress only through two
   operators, H and the first moment K. Everything else about the stress (its locality, its
   higher moments) is invisible in a uniform field, but not in a tidal field. The Weyl-midpoint
   stress has one free number in its second moment that couples to binding energy.
3. I show, for a model with a finite number of internal channels, that no choice of stress and no
   switch-off profile can keep the fall universal through the region where the interaction is
   switched off, unless the trace of the squared mass operator is the same with and without the
   interaction. So the "box only" restriction in R9-2 is forced there, not a convenience.
4. Not done: the continuum (infinitely many channels) version, two or three dimensions, more
   than two bodies, a field that carries momentum, and any real composition (nuclei).

## Setting and premises (what the axioms say, what the lane supplied)

- Axioms (`MINIMAL_AXIOMS_2026-06-29.md:114-130`, `:173-190`): no Hamiltonian, stress, source
  bridge or gauge field is supplied. So every operator below is lane-supplied (ASSUMED).
- Approved primitives (`PRIMITIVE_REGISTRY_CHECK.md:21-130`): only `scale_reference_primitive`
  is touched, and only in the labelled reading "a = Planck length"; `kinetic_isotropy_primitive`
  and `realized_state_primitive` are not used.
- ASSUMED (lane model, R8-1 d=1 repaired Bakamjian-Thomas law as used in R9-2 at branch head
  c1728175): fibre over total lattice momentum P, internal matrix Hamiltonian
  H(P) = H0(P) + c(P)(H_M(P) - H0(P)), H0 = sqrt(M0^2+P^2), H_M = sqrt(M^2+P^2), M = M0 + rank-one;
  c = 1 on the plateau |P| <= Pi1, c = 0 for |P| >= Pi2.
- ASSUMED: uniform lapse, H_g = H + g K', K' = (1/2){H,X} + B(P), X = i d/dP, B any
  translation-invariant Hermitian (fibre-diagonal) completion (the freedom in the first moment).
- Definitions: J = i[H,K'], N = i[H,J], A = -i[K',J] - H.

## Reconciliation with the active R9-2 attempt (retrieval, not new)

- Pinned sources at 02b443f contain R8-2, R9-1 (report only), R7-4 referee, TESTS. The R9-2 report
  and referee verdict exist only at the later head c1728175 of the same branch
  (`agents/C5_R9-2_report.md` sha256 56c5af25...ef79; referee 6bc5d2c2...d2d5; R9-1 referee
  aa030b78...5fb2b). `RECOVERY_STATUS.json` records them separately. No open PR or
  `probes/work/derive` attempt on this task id was found.
- R9-2 (report:3-46, 100-150): Weyl-midpoint density T00_W(Q) = chi(Q) e^{iQX/2} W e^{iQX/2}; integral = H,
  first moment = K; T01 = [H,T00]/D; fall law Xdd = -g(1 - 2V^2) on the box sector; momentum Ward
  source N supported in the transition shell. Referee: CONFIRMED WITH CORRECTIONS, PASS WITH SCOPE
  d = 1 only (verdict:19-20). Numbers at 1e-13 are consistency checks, not resolution below 1e-15.
- R9-1 referee: Lemma Q valid in its narrow class; "G-in collapses to G-out" not established;
  momentum "goes into the field" not established; a complete isolated-system centroid is open.
- R7-4 referee: the scattering exclusion needs global exponentiation and Moller hypotheses; not used here.

## Steps

1. [PROVED, elementary; CHECKED S1] For any Hermitian H, K and J, N, A as above: dK/dt = J,
   dH/dt = -gJ, dJ/dt = N - g(H + A). Hence the centre-of-energy acceleration in a uniform field is
   X'' = -g(1 + <A>/<H>) + 2gV^2 + <N>/<H> (to O(g)), determined by (H,K) alone. Universal fall
   for a body is exactly A = N = 0 on its domain. The stress's locality never enters.
   (Retrieval of R9-2 section 4.1-4.2 in a general form; the content "depends only on H, K" is
   stated by R9-2 in its scope notes.)
2. [PROVED; CHECKED S2] In any finite-dimensional space, tr A = -tr H and tr N = 0. So no finite
   invariant sector with tr H > 0 closes the boost algebra. This is the operator form of the
   zone-mean statement (I2/C3, R8-2 Theorem E); not new in content.
3. [PROVED; CHECKED S3] Fibre calculus with generic H(P), B(P): J = (1/2){H,H'} + i[H,B] and
   A = (1/2){H,J_P} - (1/2){X,N} - i[B,J] - H, verified symbolically on a generic spinor.
4. [PROVED; CHECKED S4] On the plateau (constant M) J = P*1, N = 0, A = 0. This is R9-2's box-sector closure.
5. [PROVED; CHECKED S5a-d] NEW (relative to R9-2, which only says N is "generically nonzero").
   For a two-channel switch with mixing (C S (g1-g2)(h1-h2) != 0) and B = 0 the shell source is
   N_01 = -i C S (g1-g2)(h1-h2) [P c(c-1)(g1 g2 - h1 h2) - c' g1 g2 h1 h2] tr(H) / (2 g1 g2 h1 h2).
   N = 0 iff c' = -P c(1-c)(1/det H0 - 1/det H_M): a logistic law with bounded coefficient. In the
   instance M0 = diag(5,16), M = R diag(9,35) R^T (3-4-5 rotation), P = 12, the coefficient is 59/2405,
   and on [0,12] the odds c/(1-c) can change by a factor of at most e^{9/10} < 3. An exactly
   source-free profile therefore never reaches c = 0 or 1; a profile that is exactly 1 on a plateau
   and 0 beyond Pi2 has N != 0 on an open set of the shell (B = 0).
6. [PROVED; CHECKED S6] NEW in form. Any finite-dimensional fibre has a unique off-diagonal
   completion that conserves J: B_ik = i J_ik/(E_i - E_k) in the eigenbasis of H; then J_B is the
   H-dephased J_0 and [H,J_B] = 0, tr J_B = tr J_0. So in finite channels the shell source can be
   removed. Its kernel has a pole at E_i = E_k: it is quasi-local only if J_0 has no on-shell
   off-diagonal part. This identifies exactly what R9-2 calls a "principal-value gauge potential"
   (R9-2 section 3.3, "suggested, not proved"); here it is exact in finite dimension and the pole
   is explicit. Whether J_0 has on-shell off-diagonal elements in R8-1's continuum is NOT checked.
7. [PROVED; CHECKED S7a,b] Trace lemma: tr J = (1/2) d/dP tr(H^2) for every completion B.
8. [PROVED; CHECKED S8] In the eigenbasis (H nondegenerate) the diagonal of (1/2){H,J_P} is E_i j_i'
   and the diagonal of -i[B,J] is zero. So if N = 0 and A = 0 at P, then j_i' = 1.
9. [PROVED from 3, 7, 8; numbers CHECKED S7c,d] THEOREM (finite-channel, scoped). Let H(P) be an
   n-by-n family, nondegenerate on [Pi1, Pi2], with J = P*1 at Pi1 (plateau). If N = 0 and A = 0 on
   [Pi1, Pi2] for some completion B, then tr H(Pi2)^2 - tr H(Pi1)^2 = n (Pi2^2 - Pi1^2), i.e.
   tr M_eff^2 is the same at both ends.
   Proof. N = 0 makes J diagonal in the H-eigenbasis, J = sum j_i |e_i><e_i|. A = 0 gives j_i' = 1
   (step 8), so j_i = P + a_i; continuity and J = P*1 at Pi1 give a_i = 0 for all i. Then tr J = nP,
   and step 7 gives d/dP (tr H^2 - nP^2) = 0. QED.
   In the instance (n = 2, tr M^2 = 81 + 1225 = 1306 on the plateau, tr M0^2 = 25 + 256 = 281 in
   the free region, H nondegenerate at P = 12 for all c in [0,1]) the difference is 1025 != 0,
   so N = A = 0 across the switch is impossible for every profile and every B.
   Scope: the nondegeneracy hypothesis is checked at P = 12 only, not for all P in a given shell.
10. [READING] Meaning: in a finite-channel analogue, the box restriction of R9-2 (universal fall on
    plateau momenta only) is forced. Bodies whose momentum lies in the shell fall non-universally
    (R9-2 reports <A>/<H> = 0.06 to 0.63 there, numerically).
11. [PROVED; CHECKED S9, S10] The Weyl-midpoint family has the same zeroth and first moments for
    every even chi, and second moment f''(0) = chi''(0)<W> - (1/4)<{X,{X,W}}>. So chi''(0) is a free
    parameter that multiplies binding energy in a non-uniform field, invisible in a uniform one
    (R9-2 lists tidal fields as "not fixed"). Order of the effect: a W-density smeared over variance
    s^2 feels Phi + (1/2)s^2 Phi'' + ..., giving a relative force correction (1/2)s^2 Phi'''/Phi'
    (s^2/X^2 for Phi = x^3). READING: with s ~ lattice spacing a and a = Planck length (scale
    reference primitive, reading only) and a laboratory length R, the correction is (a/R)^2 times
    the binding fraction difference: not computed against any measurement.
12. [CHECKED S11, S12; reading] Recheck of R9-1 under an explicit stress.
    - Charge continuity: R9-1 Lemma Q needs only continuity and F00(k,k) > 0 of the free part
      (S12 arithmetic). The Weyl interaction density has matrix elements only between states whose
      legs are in the box (ASSUMED: supp g and the chi-range keep the legs shifted by Q/2 in the box).
      So it neither creates nor cures the box-to-edge element; the Lemma Q conclusion is unchanged.
    - Centroid: for two bodies with lapse-sourced exchange, dJ_E/dt = -lam e1 e2 u'(x1-x2)
      [Hess1 - Hess2] exactly, to all orders in lam; k1+k2 is conserved. J_E is a function of the
      momenta only, so for a bounded (bound) pair J_E stays bounded: the energy centroid does not
      secularly self-accelerate, it is non-conserved only through a net momentum transfer in
      scattering or through the shell source N. R9-1's "self-accelerating" is an instantaneous
      statement. Where the momentum goes is NOT answered: with the field integrated out there is no
      field momentum to account.
13. [NOT DONE] Continuum version of steps 6-9 (infinite channels: the trace is replaced by a relative
    trace and degeneracy is dense), d >= 2, N >= 3, gauge binding, composition-dependent real bodies.
    No numerical comparison with MICROSCOPE or any measurement was made; no source was fetched or
    verified by me. The registered bar 1e-15 and the MICROSCOPE number are quoted from the sources only.

## What is new relative to the sources

New (same-family, unrefereed): steps 5 (closed-form shell source and logistic law), 6 (explicit
completion and its pole), 9 (finite-channel obstruction theorem), 11 (second-moment parameter).
Retrieval or restatement: 1-4, 7-8 (elementary), 10, 12 (scope cleanup of R9-1). Historical referee
labels adopted: none.

## First unresolved step

Step 13: whether the box law's continuum has on-shell off-diagonal J_0 (so the completion of step 6
is non-quasi-local) and whether the trace obstruction of step 9 survives with the Krein relative
trace. Until then the claim "universal fall through the switch is impossible" is proved only in
finite channels.
