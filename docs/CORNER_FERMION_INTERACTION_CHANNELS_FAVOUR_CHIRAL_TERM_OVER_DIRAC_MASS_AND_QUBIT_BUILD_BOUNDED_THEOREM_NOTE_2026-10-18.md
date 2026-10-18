---
claim_id: corner_fermion_interaction_channels_favour_chiral_term_over_dirac_mass_and_qubit_build_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied model only: the corner fermion of the companion notes (flux square = plaquette = tube = pi, triangle = 0, translation-invariant gauge, L = 4 torus), number-conserving, with the C19 one-fermion terms (hoppings t1, t2, a conjugation-odd O_h-invariant term X, an imaginary A2 staggered on-site mass M). (A, exact Pauli algebra on sampled instances) In the 48-qubit-per-site corner code with flux 1011 and the three noncontractible Wilson loops added as stabilizers with the fermion gauge's holonomies, the image G_P (1 + B_q)(1 - B_r)/4 of c^dag_q c_r commutes with the sampled stabilizers, satisfies the bilinear algebra mod stabilizers (25/25 random triples, 15 disjoint pairs, 15 density commutators), is path independent on the code space (7/7), is covariant under the code's rotation operators with the fermion-level PSG signs (36/36), and gives nonzero Hermitian images for 12 sampled entries of X and M; not a proof for every pair, not other L or flux. (B1, exact) The site-charge interaction (U/2) N_v^2 is invariant under the on-site U(12); its Fock energy (U/2)[(tr rho)^2 + tr rho - tr rho^2] has second variation -U ||delta rho||^2 in every traceless on-site direction, so the exchange attraction is equal in all 143 traceless channels and channel selection is decided by the bare susceptibility. (B2, numerical evidence on one supplied metallic model, t1 = -1, t2 = 0.2, 0.05 X, chemical potential at the node, N = 12 grid, T = 0.01, O_h-symmetrized quadrature; the ranking is robust for T <= 0.03 and unresolved above T ~ 0.07, where all channels become nearly degenerate) The leading static bare susceptibility over the traceless on-site channels is the q = 0 A1u imaginary channel (chi = 1.197), whose 3-dimensional sector contains the C18 chiral triangle term (overlap 0.82 with the leading vector); at Q = (pi,pi,pi) the leading channels are T2u/T2g (1.005); the pseudoscalar Dirac-mass channel A2u at Q has chi = 0.588; the RPA/Landau thresholds are U_c = 0.835, 0.995 and 1.700 (unchanged when the Hartree charge term is kept); the ranking persists at N = 16, T = 0.005. Condensing the leading q = 0 channel shifts the two Weyl doublets oppositely in energy and does not gap them. This is a mean-field ranking on a supplied model, not a theorem about spontaneous symmetry breaking. (C, exact corollary) The dressed C2x, C2y lifts anticommute and fix the eight momenta (+-pi/2)^3, so for any translation-invariant Hamiltonian commuting with them every Bloch level there is even-degenerate; at node filling nu = 1 a pocket-free state therefore has its Fermi level on touchings at all eight points, so +-k* can never be the only Fermi-level feature; under O the six other points form two triples, joined by the site inversion. (C0, exact count) The O_h- and translation-invariant Hermitian one-fermion terms of range |shift|_inf <= 1 form a space of dimension 81 = 38 conjugation-even + 43 conjugation-odd. (C, numerical) The best supplied optimisation point has no electron pocket and its only hole pocket is the forced six-point doublet, 8.72e-3 above the node. (D, numerical, uncertified gap search) With the C19-type staggered mass the optimisation point is a clean insulator at nu = 1 for m = 0.02 and 0.05 (global gaps 0.025 and 0.055), but the global gap is smaller than the direct Dirac gap at k* (0.042, 0.106), so the lowest excitation is not the Dirac fermion; the C20 metallic model with m = 0.02 stays metallic. Not claimed: a spontaneous Dirac mass, any statement beyond mean field, a clean vacuum whose lowest excitation is the Dirac fermion, other interactions, flux patterns or L, any physical identification."
upstream_dependencies:
  - corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_bounded_theorem_note_2026-10-17
  - corner_fermion_qubit_code_genuine_cube_rotation_action_emergent_fermion_carries_spin_half_class_bounded_theorem_note_2026-10-17
  - corner_fermion_long_wavelength_theory_is_one_isotropic_spin_half_doublet_and_one_qubit_block_embedding_bounded_theorem_note_2026-10-17
runner: scripts/corner_fermion_interaction_channels_and_qubit_build_2026_10_18.py
---

# Corner-fermion interaction channels favour a chiral term over the Dirac mass; clean-vacuum obstruction; qubit build

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact statements are marked exact. The others are numerical evidence on supplied parameters. Nothing is adopted.

## Question

The Dirac-pair note (C19) left three things open.

1. Can interactions generate the pseudoscalar Dirac mass spontaneously?
2. Can the Dirac point be the global low-energy feature, so that filling the lower bands gives a clean Dirac vacuum?
3. Can the new terms X and M be built at the qubit level?

## Result

1. **Qubit build.**
   - **The images.** In the 48-qubit-per-site corner code (flux 1011, L = 4), each bilinear c†_q c_r has the Pauli image G_P (1 + B_q)(1 − B_r)/4. Here G_P is i^n times the product of code hops along a path P, divided by the gauge phase along P.
   - **The logical sector.** The three noncontractible Wilson loops are added as stabilizers with the fermion gauge's holonomies. This fixes the logical sector, and it makes the image path independent on the code space (7/7 random pairs, two paths each).
   - **What is checked.** All checks are exact Pauli-algebra checks on sampled instances:
     - commutation with the sampled stabilizers;
     - [Q(c†_a c_b), Q(c†_b c_c)] = Q(c†_a c_c) mod stabilizers (25/25 triples);
     - disjoint bilinears commute (15/15);
     - [Q(n_a), Q(c†_a c_b)] = Q(c†_a c_b) (15/15);
     - covariance under the code's rotation operators with the fermion-level PSG signs (36/36).
   - **X and M.** The C19 terms are sums of such bilinears: X has range ≤ 1 site and M is on-site and staggered. For twelve sampled entries, h c†_q c_r + h.c. with complex h gives nonzero, Hermitian images that commute with the stabilizers.
   - **Scope.** This is not a proof for every pair, for other L, or for other flux patterns. The construction is the standard Bravyi–Kitaev superfast dictionary on the corner graph.
2. **The interaction does not choose a channel; the bands do.**
   - **Exact.** N_v commutes with every on-site bilinear, so (U/2) N_v² is invariant under the on-site U(12).
     - Its Fock energy is (U/2)[(tr ρ)² + tr ρ − tr ρ²].
     - In every traceless direction δρ the second variation is −U‖δρ‖².
     - So the exchange attraction is the same in all 143 traceless on-site channels, at q = 0 and at Q alike, and the bare susceptibility decides.
   - **Numerical, one supplied metallic model.** The model is t1 = −1, t2 = 0.2, 0.05 X, with X a fixed normalized combination of six sampled invariant conjugation-odd terms. The chemical potential sits at the node. Static Lindhard susceptibilities use N = 12, T = 0.01, quadrature symmetrized over O_h (raw asymmetry 4e−4), resolved into O_h irreps:

     | channel | q | χ | U_c = 1/χ |
     |---|---|---|---|
     | A1u, imaginary (contains the C18 chiral term i λ) | 0 | 1.197 | 0.835 |
     | T1u / T1g | 0 | 0.803 / 0.801 | |
     | A1g (trace removed) | 0 | 0.781 | |
     | T2u / T2g | Q | 1.005 / 1.005 | 0.995 |
     | **A2u, imaginary: the pseudoscalar Dirac mass** | Q | **0.588** | **1.700** |

   - **The ranking.**
     - The leading channel is the uniform imaginary A1u channel. It has full imaginary weight, and its 3-dimensional sector contains the C18 chiral triangle term (overlap 0.82 with the leading vector).
     - The Dirac-mass channel is subleading, and not even the leading staggered channel.
     - Keeping the Hartree charge term leaves U_c unchanged (0.835 at q = 0, 0.995 at Q).
     - The control at N = 16, T = 0.005 with a shifted grid keeps the order: 1.358 (A1u, q = 0), 1.120 (max at Q), 0.607 (A2u, Q). The values grow as T falls, which is the metallic Fermi-surface contribution.
   - **What the leading order does.** Condensing the leading q = 0 channel (strength 0.05) keeps the doublets at k* and −k* degenerate and shifts them by ∓0.025. This is a valley energy splitting, like a chiral chemical potential, not a gap.
   - **Temperature scope (from the independent check).** The ranking A1u(0) > T2u(Q) > A2u(Q) is robust for T ≤ 0.03 on every grid tested (N = 12–28): 1.359 / 1.120 / 0.607 at T = 0.005. It is not robust at high temperature.
     - χ_max(T) is non-monotonic.
     - Above T ≈ 0.07 all channels are degenerate to within about 1%. At T = 0.1 the A2u Dirac-mass channel is marginally the largest (1.0135 against 1.0108), likely because the bands near μ are very flat (Weyl velocity 0.04).
     - So for U ≳ 0.99 mean-field cooling becomes unstable near T ≈ 0.1 with no clear channel selection, and U_c(A2u) = 1.70 is not a meaningful threshold there.
   - **Conclusion.** In mean-field/RPA on this supplied model, for T ≲ 0.03 (or U below about 0.98) the first instability is not the Dirac mass. At higher temperature the channel selection is unresolved.
   - **Correction to the campaign log.** The exploratory log listed a real A1 value of 1.1977 at q = 0. That is not the traceless A1g value, which is 0.781. The independent check finds 1.211 for A1g including the charge channel, and notes that 1.1977 matches the imaginary A1u value (1.1974 at zero offset). So the entry was most likely a mislabel; either way it is not a real-channel instability.
3. **A clean two-node vacuum is impossible; the best optimization shows the forced residue.**
   - **Exact.** The dressed lifts of the commuting half-turns C2x and C2y anticommute on the whole one-particle space, with the same permutation and opposite sign on every mode.
     - Both fix the eight momenta (±π/2)³. There the restricted 12 × 12 unitaries anticommute, so every Bloch level of a translation-invariant H commuting with them is even-degenerate.
     - At node filling ν = 1, a pocket-free state needs E0(k) ≤ μ ≤ E1(k) everywhere. Since E0 = E1 at all eight points, all eight must touch μ.
     - So ±k* can never be the only Fermi-level feature. Either six more touchings sit at μ, which is non-generic, or there are pockets.
     - Under O the six other points form two triples. The site inversion joins them into one orbit of six.
     - The same mechanism underlies the lane's odd-filling theorem, which is not used as a premise here.
   - **Exact count.** The O_h- and translation-invariant Hermitian one-fermion terms of range |shift|∞ ≤ 1 span a space of dimension 81: 38 conjugation-even and 43 conjugation-odd.
     - The exploratory optimization's conjugation-even basis was identically zero, because of a construction error (it symmetrized antisymmetric seeds).
     - So it actually varied t2 and the 43 conjugation-odd terms only. The obstruction makes the missing terms irrelevant to its conclusion.
   - **Best numbers (supplied optimization point).** The point is embedded in the runner as 45 orbit coefficients.
     - Node doublets sit at E_N = −2.1134 with Weyl velocity 0.565.
     - There is no electron pocket: the minimum of band 1 is E_N, at the node.
     - The refined maximum of band 0 is E_N + 8.72e−3, attained exactly at the forced six-point doublet. It is the only residual pocket found.
     - The other two tested models have the doublet 0.096 (C20 model) and 0.162 (C19 model) above the node. The C20 model's band-0 maximum (0.140 above the node) lies elsewhere. The C19 model's measured velocity, 0.1096, agrees with the C19 note.
4. **With the staggered mass, a clean massive vacuum, but not a Dirac one.**
   - The C19-type A2 mass breaks odd translations and folds the six points in pairs.
   - **Numerical results.** The global gaps come from a grid plus local refinement and are not certified.
     - The optimization point is a band insulator at ν = 1 for m = 0.02 and m = 0.05. Its global gaps, 0.025 and 0.055, are smaller than the direct Dirac gaps at k*, 0.042 and 0.106.
     - The C20 metallic model stays metallic at m = 0.02 (global gap −0.116). At m = 0.1 it has a gap of 0.014, against a direct gap of 0.212.
   - **So** in every tested case the lowest excitation is not the Dirac fermion at k*.

## How this bears on the lane (interpretation, not a claim)

- **Spontaneous mass.** A channel-blind local repulsion favours the uniform chiral (valley-splitting) term before the Dirac mass. That term keeps the Weyl nodes, so it does not give the electron-like massive phase.
  - A spontaneous pseudoscalar mass would need a microscopic interaction that favours the staggered A2u channel, or a different band structure. Neither is derived here.
  - This fits the lane's filling constraint: a gap at ν = 1 needs translation breaking or loss of the commuting C2s, and the leading q = 0 order breaks neither.
- **Clean vacuum.** The massless target "±k* is the only Fermi-level feature at ν = 1" is ruled out by symmetry, not merely unreached.
  - The physically interesting object is a massive vacuum whose lowest excitation is the Dirac fermion.
  - The tested supplied masses gap the system but put the lowest excitation elsewhere.
  - Whether some mass direction in the five-dimensional sampled A2 space, or a longer-range kinetic term, puts the minimum gap at k* is open.
- **Qubits.** The C19 Hamiltonian terms have explicit local Pauli images on the corner code, with sampled exact checks. A full term-by-term certificate over all pairs and other L is not given.

## Independent check

A fresh-context agent of the same model family checked this note; it is not an independent human reviewer. Scripts are in `.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/`.

- **Confirmed.**
  - The 143-channel equal attraction, re-derived with Wick's theorem.
  - The susceptibility values, using its own Lindhard code and O_h projectors. A finite-difference χ = −∂²Ω/∂h² confirms U_c = 1/χ.
  - The anticommuting C2 lifts and the paired levels at all eight points, both for random D2-only and for O_h-symmetrised Hamiltonians.
  - The 38 + 43 term count.
  - The optimiser-point numbers on a 40³ grid.
  - The qubit-build relations, using its own Pauli algebra with randomized paths and a negative control.
- **Corrections, now applied:** the temperature scope of the channel ranking, and the wording of the log correction.

## Premises

- **Axioms used.** Lattice (Z³, unit translations, proper cubic rotations about sites).
- **Supplied.**
  - The corner model, its flux pattern and gauge.
  - The 48-qubit corner code with flux 1011.
  - The terms X and M, and the optimization point's coefficients.
  - The site-charge interaction (U/2) N_v².
  - The mean-field/RPA treatment, the temperature and the grid.
- **Standard facts used.**
  - Wick's theorem for quasi-free states.
  - The static Lindhard response and the RPA/Landau instability criterion.
  - Schur's lemma.
  - The Bravyi–Kitaev superfast encoding.

## Relation to prior work

- **Interaction-driven mass generation and chiral symmetry breaking for lattice Dirac fermions.**
  - Nambu and Jona-Lasinio, Phys. Rev. 122, 345 (1961).
  - Herbut, PRL 97, 146401 (2006).
- **Mean-field instabilities of Weyl semimetals, including charge-density-wave (axionic) mass.**
  - Wang and Zhang, PRB 87, 161107 (2013).
- **Even-degeneracy from anticommuting nonsymmorphic or projective lifts.**
  - Standard double-group arguments.
  - Bradlyn et al., Science 353, aaf5037 (2016).
- **The fermion-to-qubit dictionary.**
  - Bravyi and Kitaev, Ann. Phys. 298, 210 (2002).
- **New here.**
  - The channel ranking on the corner model.
  - The exact U(12) channel-blindness of the site-charge interaction in this 12-orbital setting.
  - The clean-node obstruction at the eight D2-fixed points, with the corrected invariant-term count.
  - The massive-vacuum gap comparison.
  - The sampled qubit images of X and M.

## No-Go Discipline Gate

- **N1 — routes.**
  - Other interactions: nearest-neighbour, Hund-like, or corner-resolved.
  - Beyond-mean-field treatments.
  - Other chemical potentials, and other X or M directions.
  - Longer-range kinetic terms.
  - Other flux patterns.
  - None of these is tested.
- **N2/N3 — scope.**
  - The channel ranking is on one supplied metallic model at two grid/temperature settings.
  - The obstruction is exact for every translation-invariant Hamiltonian commuting with the dressed C2x and C2y.
  - The massive-vacuum statements cover two models and four masses.
- **N4 — inputs.**
  - Floating-point Lindhard sums.
  - Nelder–Mead refinement of band extrema, which is not a certified global search.
  - Exact GF(2)/Pauli arithmetic for the qubit checks.
- **N5 — wording.**
  - "Favours" means a larger bare susceptibility, and so a lower RPA threshold. It does not mean a proved ground state.
  - "Clean" means no pockets at the stated filling.
- **N6/N7 — strongest objections.**
  - Mean field can mislead in a metal.
  - The ranking depends on the supplied band structure.
  - The obstruction rules out only the two-node massless vacuum, not a massive Dirac vacuum.
- **N8 — earlier claims.**
  - Extends the C19 note and does not change it.
  - Corrects two exploratory-log items: the A1 real value, and the conjugation-even basis count.

## Verification

```bash
python3 scripts/corner_fermion_interaction_channels_and_qubit_build_2026_10_18.py
```

Expected: `TOTAL: PASS=28 FAIL=0` (about 70 s).

## Load-bearing sources

- [Dirac-pair note (C19)](CORNER_FERMION_MASSLESS_DIRAC_PAIR_PROTECTED_BY_CUBE_ROTATIONS_AND_PSEUDOSCALAR_DIRAC_MASS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Corner-code note (C17)](CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Long-wavelength note (C18)](CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
