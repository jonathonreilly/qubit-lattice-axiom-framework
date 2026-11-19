---
claim_id: the_cube_filtered_quartic_toy_is_sign_free_and_pairs_at_strong_coupling_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the supplied one-quartic SU(4) toy (four modes per site, H = -t sum a^+ a - g sum_x (c1 c2 c3 c4 + h.c.) with c_x = sqrt8 times the cube average, any real free band): the interaction expansion has configuration weights g^2n det(M)^4 with M real, so the toy is sign-free at every g, L and beta (a complex hop restores the sign problem). Finite diagnostics on L^3 tori at g -> infinity: translations stay unbroken (the cube-term susceptibility stays below 1 and falls with beta), the energy per term lies below every translation-breaking mode-product state and below the uniform pair state (-1/2), and the charge-2 pair correlation has a plateau with a correlation length growing faster than L (L = 4, 6 live; L = 8 recorded), i.e. a pair condensate breaking SU(4) x Z4, not a symmetric phase; at g/t = 4 the pair order is weakened at L = 4 and absent at L = 6 at T = 1/8 (recorded). The toy is not Spin(10); no symmetric mass generation is established or excluded for the Weyl 16."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_strong_coupling_face_composite_has_no_atomic_limit_and_stays_gapped_on_sheared_tori_bounded_theorem_note_2026-10-22
runner: scripts/the_cube_filtered_quartic_toy_is_sign_free_and_pairs_at_strong_coupling_2026_10_22.py
---

# The cube-filtered quartic toy is sign-free and pairs at strong coupling

Claim type: bounded_theorem.
Primary runner: `scripts/the_cube_filtered_quartic_toy_is_sign_free_and_pairs_at_strong_coupling_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) leaves the chirality wall at one question: does the far-rung cube-filtered pair square have a symmetric phase whose composite band stays gapped at the zone faces? The [face-composite note](THE_STRONG_COUPLING_FACE_COMPOSITE_HAS_NO_ATOMIC_LIMIT_AND_STAYS_GAPPED_ON_SHEARED_TORI_BOUNDED_THEOREM_NOTE_2026-10-22.md) studied a supplied one-quartic SU(4) toy of it. On sheared tori the toy's face composite stays gapped, but mode-product states favour translation-breaking order about twice as strongly in 3D as in 1D, and the full 3D phase was beyond exact diagonalisation. This note settles the toy's 3D strong-coupling phase with a quantum Monte Carlo that has no sign problem. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged; the toy content is supplied.

## Statement

1. (Sign.) Expand e^(-beta H) in the quartic about any real free band. A term with n cube operators C_x = c1 c2 c3 c4 and n of their conjugates has weight g^2n det(M)^4, where M_ij is the free propagator from the i-th C-vertex to the j-th C^+-vertex. The four flavours see the same real matrix, and reordering even vertices gives sign +1. So the toy is sign-free at every coupling, size and temperature, for any real filter. A complex hop (a flux) makes the traces complex.
2. (No translation order.) At g -> infinity on L = 4 and 6 (beta = 4, 8, live; L = 8 and beta = 16 recorded) the susceptibility of the cube terms h_x = -(C_x + C_x^+) stays below 1 at every lattice momentum and falls as beta grows. Translation order of the best mode-product pattern would give about 18 at L = 4, beta = 8.
3. (Variational ordering, exact for the states named.) At g -> infinity on 4^3 the best translation-breaking mode-product state gives -0.368 per term. The uniform pair state with <c1c2> = <c3c4> = 1/2 gives exactly -1/2. The thermal energy -0.614 (beta = 8, live) and -0.621 (beta = 16, recorded) is an upper bound on the ground energy, so the true state lies at least 0.25 per term below every product state.
4. (Pair order.) At g -> infinity the charge-2 pair correlation <D_x D_y^+> (D = c1 c2, the 6 of SU(4)) is flat beyond one cube. At beta = 4, xi/L rises from 0.387 (L = 4) to 0.429 (L = 6) live, and to 0.521 at L = 8 recorded. At beta = 8 it rises 0.417, 0.509, 0.658 for L = 4, 6, 8 with a plateau pair(r_max) of about 0.05 at L = 6 and 8 (recorded). This is a pair condensate breaking SU(4) x Z4 (to a Z2 and an Sp(4)-type subgroup; the direction within the 6 is not measured), with translations unbroken: the bilinear phase, not a symmetric phase.
5. (Free band.) With a real nearest-neighbour band, at L = 4, beta = 8, pair(r_max) falls from 0.059 (t = 0) to 0.028 (t = 0.25, g/t = 4) live, and to 0.005 and 0.003 at g/t = 2 and 1 (recorded). At g/t = 4, from L = 4 to 6, xi/L falls from 0.451 to 0.299 and the plateau from 0.0275 to 0.0078 (recorded), so at T = 1/8 the order is absent there. The zero-temperature boundary is not located.

## Derivation

Statement 1. In the interaction picture every vertex is even. A configuration's trace factorises flavour by flavour into time-ordered free expectations of n annihilators c_f(x_i, tau_i) and n creators c_f^+(y_j, tau_j'). Each is +-det M with the same M for every f, because the free band is flavour-diagonal and SU(4)-blind; the +- is the same for all four flavours, so it cancels in the fourth power. Gathering the interleaved flavour strings costs 6 n(n-1)/2 transpositions per vertex type, an even number. The expansion sign (-1)^2n (-g)^2n is +1. A real symmetric band and a real filter make M real, so det(M)^4 >= 0. The runner checks the identity trace = det^4 on random configurations to 5e-16 and shows complex traces under a flux.

Statement 3. The product-state energy uses the identity E/term = -sum_m beta_m(y)^4 (face-composite note, B1), maximised by quartimax. For the pair state, Wick's theorem gives <C_x> = <c1x c2x><c3x c4x> = (K_xx/2)^2 with K_xx = 1, so E/term = -2(1/2)^2 = -1/2. A thermal average is never below the ground energy.

Statements 2, 4, 5 come from continuous-time interaction-expansion Monte Carlo (insertion and removal of C/C^+ pairs and vertex shifts, with the inverse matrix refreshed every 20 sweeps; drift <= 3e-11). The cube-term susceptibility uses vertex counts, chi_h(Q) = (<|n_Q|^2> - <n>)/(beta N). Pair correlations use the per-configuration propagator, <D_x D_y^+> = G_xy^2. The second-moment correlation length is xi = sqrt(P(0)/P(q_min) - 1)/(2 sin(pi/L)).

## Checks

- `[PASS] A1` exact traces = det(M)^4 >= 0 (max difference 5e-16); `[PASS] A2` a flux gives complex traces.
- `[PASS] B1` the engine reproduces exact diagonalisation of a 3-site ring (energy and pair correlator, within 4 sigma).
- `[PASS] C1` the 1D control (2-site filter, L = 16, g -> infinity) shows exponential pair decay (0.163, 0.040, 0.009, 0.0023 at d = 1, 2, 4, 8), so the 3D plateau is not an estimator artefact. 1D is symmetric, as in the face-composite note.
- `[PASS] D1` the Q-averaged cube-term susceptibility is <= 0.4 and the largest value <= 1.5 at t = 0, falling from beta = 4 to 8.
- `[PASS] D2` pair(r_max) >= 0.6 pair(1,1,1) and >= 0.025 at t = 0 (ratios 0.78, 0.82, 0.68).
- `[PASS] D3` xi/L rises by >= 0.02 from L = 4 to 6 at beta = 4 (0.387 -> 0.429).
- `[PASS] D4` t = 0.25 cuts pair(r_max) at L = 4, beta = 8 by more than 1.5x (0.059 -> 0.028).
- `[PASS] E1` product -0.368 > pair state -0.5 > QMC -0.614.

Recorded production values (separate resumable runs of the same engine, 900 to 9300 sweeps per point; printed by the runner as recorded, no PASS depends on them):

| run | E/term | pair(r_max) | xi/L |
|---|---|---|---|
| L = 4, beta = 4 | -0.5625(34) | 0.0501(12) | 0.387(4) |
| L = 6, beta = 4 | -0.5016(17) | 0.0359(15) | 0.436(10) |
| L = 8, beta = 4 | -0.4869(19) | 0.0323(20) | 0.521(14) |
| L = 4, beta = 8 | -0.6086(19) | 0.0597(22) | 0.417(7) |
| L = 6, beta = 8 | -0.5725(17) | 0.0493(22) | 0.509(9) |
| L = 8, beta = 8 | -0.5640(13) | 0.0484(29) | 0.658(21) |
| L = 4, beta = 16 | -0.6209(22) | 0.0571(9) | 0.409(3) |
| L = 4, beta = 8, t = 0.25 | -0.4826(39) | 0.0275(10) | 0.451(6) |
| L = 6, beta = 8, t = 0.25 | -0.4051(32) | 0.0078(22) | 0.299(14) |
| L = 4, beta = 8, t = 0.5 | -0.3391(83) | 0.0054(7) | 0.331(11) |
| L = 4, beta = 8, t = 1 | -0.1584(86) | 0.0030(2) | 0.320(14) |

In those runs the largest cube-term susceptibility is 0.16 to 0.54 at t = 0 and never grows with beta. At L = 4, t = 0, beta = 16, the face composites D(X), D(M), D(R) and the zone-centre elementary keep under 6% of their weight at tau = 1 (noisy; a gap scale of order 2 atom units or more, not a gap measurement).

## Estimates against measurement

None. This is a statement about a supplied toy's phase, not a prediction.

## Boundary

Supplied: the toy content (four modes per site and one SU(4)-singlet charge-4 quartic per cube on the cube filter, not the Spin(10) pair square on the Weyl 16), the real nearest-neighbour free band, the sizes (L <= 8), temperatures (beta <= 16), seeds and atom units (g = 1). The direction of the condensate within the 6, the zero-temperature phase boundary in g/t, and the composite gaps at nonzero t are not computed. For the register this narrows the open route: in this toy the overlapping-term strong-coupling limit (which has no atomic limit) is a pair-condensed phase, so a symmetric phase, if any, lies at intermediate coupling. Whether the Spin(10) content behaves the same is untested; its sign structure differs (it is not four identical flavours).
