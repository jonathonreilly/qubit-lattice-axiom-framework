---
claim_id: link_register_photon_gives_the_light_copy_schwingers_one_loop_magnetic_moment_with_an_exact_dressed_hop_ward_identity_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's cube tick in its small-step (Hamiltonian) limit on a flat cell, with odd-cube hops dressed by the site phase of each site's own link register: the dressed-hop vertex obeys an exact Ward identity for pure-gauge register modes, to all orders in the site phase (checked at random finite momenta to 7e-16); at one loop the zero-transfer vertex plus seagulls plus tadpole equals the field derivative of the self-energy at fixed loop momentum (relative miss 1e-10, vertex alone misses by 1.03). With the links' Gaussian (large-register) photon on the skew-loop law, a Lorenz-type gauge fixing w = 4/3 and a Stueckelberg photon mass lam = r m, the light copy's one-loop F2/(alpha/2pi), alpha = 3 e^2/(4 pi), approaches the continuum value at r = 1 (0.20920) as m a -> 0, with a deviation that shrinks monotonically like m a ln(m a) (-0.381 at m a = 0.2 to -0.030 at 0.00625; extrapolations 0.2079 to 0.2137); the deviation is ultraviolet (within 10% between r = 1 and r = 1/4) and not set by the copy mass. The same engine reproduces the continuum Dirac F2 with a massive Feynman-Stueckelberg photon to 0.2% (r = 1) and 0.005% (r = 1/4). Supplied model, finite diagnostic: small-step limit, flat cell, Gaussian registers, supplied gauge fixing and photon mass, straight-bond external field, one loop; the finite-step (Floquet) correction and the cone (step) counterterm are not included."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/link_register_photon_gives_the_light_copy_schwingers_one_loop_magnetic_moment_with_an_exact_dressed_hop_ward_identity_2026_10_22.py
---

# The link-register photon gives the light copy Schwinger's one-loop magnetic moment, with an exact dressed-hop Ward identity

Claim type: bounded_theorem.
Primary runner: `scripts/link_register_photon_gives_the_light_copy_schwingers_one_loop_magnetic_moment_with_an_exact_dressed_hop_ward_identity_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) is a cube tick with a spin-3/2 edge hop W on even then odd 2^3 cubes, a mass angle mu and a copy mass M on the copy with copy sign -1; its links carry site-bond registers whose plaquette phase (part of the response law, CL-3) is a skew-loop law. At tree level the dressed hop already gives g = 2 for the light copy. This note asks whether the link registers' own photon, at one loop, gives the light copy the measured leading anomalous moment alpha/2pi, and how large the lattice part is. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Fermion rules (small-step limit: eps = eta e0, mu = eta m, M = eta M0, eta -> 0, e0 = sqrt3/2, so the fermion cone is c = 1 site per unit time).

1. The tick generator (i/eta) log U(K) tends to the Bloch Hamiltonian H(K) with even hop (e0 - mu/2) W - M PH W and odd hop -(e0 + mu/2) W, with error O(eta).
2. At K = 0 the light copy sits at +-m (twice) and the heavy copy at +-(m + M) (twice); at the zone corner the levels are +-|2 e0 - M| and +-2 e0; the copy sign commutes with W.
3. The light block at small momentum is the Dirac Hamiltonian c alpha.p + beta m with c = 1.
4. At tree level the dressed-hop vertex gives g = 2 against the kinetic cone (c_kin^2 = 1 - m^2/3 + ...), with the copy mass on.

B. Photon rules (Gaussian site-bond registers, skew-loop plaquettes, flat cell).

5. A bcc cell has 6 skew loops and the plaquettes are gauge invariant.
6. At small k the two transverse modes and the gauge mode lie on omega = |k| (c_gamma = c_fermion = 1), as does the A4 mode at w = 4/3, with error O(k^2); the fourth (copy-sign) mode is gapped.
7. The electric constant is eps_c = 4/3 per cell of volume 4, every small-k mode has Cartesian residue 1/eps_c, and so alpha = e^2 V_c/(4 pi eps_c c) = 3 e^2/(4 pi).

C. Ward identities.

8. Theorem (exact, all orders in the site phase). For a pure-gauge register mode, the contracted dressed-hop vertex equals i(Lambda G^-1(K) - G^-1(K + k) Lambda), with Lambda the site-phase gauge transformation and G the fermion propagator.
9. At one loop and fixed loop momentum, the zero-transfer vertex plus the two seagulls plus the tadpole equals d Sigma/dA, the derivative of the self-energy in a uniform field; the vertex alone does not.

D. Engine validation.

10. The residue formulas for the two- and one-propagator Euclidean frequency integrals agree with quadrature.
11. With the same engine, a continuum Dirac fermion and a Feynman-Stueckelberg photon of mass lam = r m (cutoff region the bcc zone) give F2/(alpha/2pi) = int_0^1 2z(1-z)^2/((1-z)^2 + z r^2) dz, which tends to 1 (Schwinger) as r -> 0.

E. Lattice one-loop F2/(alpha/2pi) (photon mass lam = r m, M = 0.6, e0 = sqrt3/2).

12. The external-leg spinor corrections and the mass-angle counterterm cancel, so tree g = 2 holds across the update-law family at this order; the one-loop structure fits the tree spin matrix.
13. As m a -> 0 the lattice F2 approaches the continuum value at r = 1; the deviation shrinks monotonically, roughly halving with m (m ln m), and fits F + m(a ln m + b) [+ c m^2] extrapolate to the continuum value within 3%.
14. The deviation is ultraviolet: at r = 1/4 it is within 10% of its r = 1 value. Taken with item 11, in the limit lam -> 0 the light copy's F2 is (alpha/2pi)(1 + dev) with dev the lattice term. (This limit is inferred from items 11 and 14, not computed at lam = 0.)
15. The deviation is not set by m/M: changing M among 0.3, 0.6 and 1.0 changes it by less than 15%, non-monotonically, so the copies enter only through the lattice term.

## Derivation

Item 1 compares (i/eta) logm of the product of the even and odd cube unitaries at eta = 2e-3 and 1e-3 with H(K). Items 2 to 4 diagonalise H at K = 0 and the zone corner, project onto the light block and test the Clifford relations of the numerical velocity matrices, and compute the tree spin-flip amplitude against the kinetic cone. Items 5 to 7 enumerate the skew loops of the bcc cell, build the register quadratic form with electric weight 1/(s.s) per bond and magnetic weight 1/6 per skew loop, add the gauge fixing, and diagonalise at small k. Item 8 evaluates both sides at three random (K, k, k0, omega). Item 9 compares the one-loop pieces at three random loop momenta with a central difference of the self-energy in the external field (step 1e-5, photon mass 0.05). Items 10 and 11 check the residue formulas against mpmath quadrature and run the continuum Dirac model on a 30 x 10 x 10 log-graded grid per pyramid of the zone. Items 12 to 15 compute F2 = C_mag - C_conv (the spin-flip coefficient at transfer q minus the convection coefficient at zero transfer, both relative to the tree vertex, which cancels F1, Z2 and every renormalisation of the dimension-4 terms) with vertex, two seagulls and tadpole from the exact BCH expansion of the dressed hop, on a rhombic-dodecahedron zone split into 12 pyramids, log-graded towards k = 0 (18 x 5 x 5 points per pyramid at m = 0.05, more radial points at smaller m).

## Finite checks

Exact or closed-form checks (the runner asserts each):
- Tick generator error 5.7e-04 at eta = 2e-3 and 2.8e-04 at eta = 1e-3 (ratio about 2, O(eta)).
- Levels at m = 0.1, M = 0.6: K = 0 gives +-0.1 (x2) and +-0.7 (x2); zone corner |levels| 1.1321 and 1.7321; [s, W] = 0 below 1e-13.
- Light block Clifford defect 4.4e-11.
- Tree level: g/2 - 1 = 8e-07, 8e-07, 9e-07 at m = 0.4, 0.2, 0.1; c_kin^2 = 0.9467, 0.9867, 0.9967.
- 6 skew loops per bcc cell; |K g| = 5e-16 at five random k.
- Photon cone: max |omega/k - 1| = 2.4e-06 at k = 0.005 (O(k^2) between k = 0.01 and 0.005, three directions); A4 mode 9.7e-06; gapped mode omega^2 >= 12.00.
- eps_c = 1.333333; residues x eps_c = 1.000000 for all three small-k modes.
- Exact Ward identity: maximum residual 7e-16.
- One-loop Ward identity: relative miss 1e-10; vertex alone misses by 1.03.
- Residue formulas against quadrature: 4e-16.
- Continuum engine: r = 1 (m = 0.05): 0.20955 against 0.20920; r = 0.25 (m = 0.02): 0.57190 against 0.57193 (asserted to 2e-3 relative).

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Parts at m = 0.05: vertex +0.43872, seagull -0.38926, tadpole +0.00000, legs -0.00052, counterterm -0.00000; mass counterterm dmu = -0.4000 e^2 = -1.676 alpha. Legs + counterterm = -5.2e-04; fit residual to the tree spin matrix 2e-09.
- Continuum limit (F(1) = 0.20920, continuum value at r = 1):

| m a | vertex | seagull | total | total - F(1) |
|---|---|---|---|---|
| 0.2 | +0.66521 | -0.83745 | -0.17224 | -0.38144 |
| 0.1 | +0.55181 | -0.60187 | -0.05006 | -0.25926 |
| 0.05 | +0.43872 | -0.38926 | +0.04946 | -0.15974 |
| 0.025 | +0.35226 | -0.23718 | +0.11508 | -0.09412 |
| 0.0125 | +0.29476 | -0.13932 | +0.15544 | -0.05376 |
| 0.00625 | +0.25869 | -0.07986 | +0.17883 | -0.03037 |

- Last deviation ratio 0.565; the six fits (three ranges, with and without m^2) extrapolate to 0.2079 to 0.2137 against 0.2092.
- Ultraviolet deviation: r = 1/4 against r = 1: -0.1724 against -0.1597 (m = 0.05), -0.0999 against -0.0941 (m = 0.025).
- Copy mass at m = 0.05: deviation -0.1490 (M = 0.3), -0.1469 (M = 1.0) against -0.1597 (M = 0.6).
- Zone-grid convergence at m = 0.05: total 0.04946 (18 x 5 x 5) to 0.04886 (24 x 7 x 7).

## Estimates against measurement

Estimates with supplied inputs (alpha = 1/137.035999, the measured a_e = 1.15965218059e-3 +- 1.3e-13, l_P = 1.616255e-35 m, the electron reduced Compton length 3.8615926796e-13 m, a site spacing of sqrt(8 pi) l_P):
- alpha/2pi = 1.161409734e-03, the Schwinger term; the rest of the measured a_e is higher-order QED.
- Lattice term: m a = 2.10e-22; a fit dev ~ m a (0.93 ln(m a) - 0.42) gives delta a ~ -1.1e-23, 9e-11 of the measurement precision.
- A degenerate second light copy (M = 0) would enter a_e at two loops through vacuum polarisation, (alpha/pi)^2 (119/36 - pi^2/3) = 8.464e-08, 6.5e+05 times the precision; the runner asserts this exceeds 1e5 times the precision.
- Heavy copy and zone-corner partners (mass about 0.6/a) enter at one loop only inside the lattice term; their two-loop vacuum polarisation, (alpha/pi)^2 (m a/M)^2/45, is about 1e-50.

## Boundary

Supplied: the small-step (Hamiltonian) limit of the update law's tick; a flat cell; the Gaussian (large-register) limit of the link registers with the skew-loop law in its flat-cell (Hodge) reading; continuous time; the Lorenz-type gauge fixing with w = 4/3; the Stueckelberg photon mass as an infrared regulator; the A4 coupling at even centres; a straight-bond external field along x; one loop; the identification alpha = 3 e^2/(4 pi) from item 7; the measured inputs of the estimates. Forced, given those: the exact Ward identity of the dressed hop; the one-loop Ward identity; the cancellation of legs and counterterm; the lattice F2 values, their approach to the continuum value at r = 1, and the ultraviolet, copy-mass-independent character of the deviation over the sampled range. Not claimed: the finite-step (Floquet) correction; the cone (step) counterterm; the limit lam -> 0 computed directly; higher loops; finite registers beyond the Gaussian limit; curved cells; any value of F2 at m a below 0.00625 beyond the fitted form.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's cube tick, mass angle and copy mass; the links' site-bond registers and skew-loop plaquette phase; the dressed rest phase that sets the mass-angle counterterm. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/link_register_photon_gives_the_light_copy_schwingers_one_loop_magnetic_moment_with_an_exact_dressed_hop_ward_identity_2026_10_22.py
```

Needs numpy, scipy and mpmath. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 60 to 65 s with about 220 MB resident, prints about 4.9 kB and ends with `TOTAL: PASS=17 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output apart from the two elapsed-time lines.
