---
claim_id: conjugate_zoom_three_families_stay_degenerate_under_the_cube_tick_and_its_chiral_generator_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's cube tick (spin-3/2 edge hop on 2 x 2 x 2 cubes, two tilings offset by (1,1,1), with the copy-mass factor) on a 6^3 torus, single-particle sector, with the families read as the characters of T(2 e_i) on the turn-fixed line a = j(1,1,1), j = 1, 2: the spin-S overlap gives each cube face flux 2 pi S/3 (pi at S = 3/2), so the cube reflection R is real in a gauge with R^2 = 1, and the copy sign s = i R1 R2 R3 R is purely imaginary with [s, R] = 0 and s^2 = 1, so complex conjugation K maps s to -s; among the 48 cube-centred point maps (each unitary or composed with K), those sending j to -j with quasi-energy kept number 12 without the copy mass, 6 with it, 3 after adding the chiral generator Hc = (i/2)[W_o, W_e], and none after adding the inversion-odd pseudoscalar eta s; inversion about a cube centre commutes with R, each R_i, s and Hc to 1e-14; the families j = 1, 2 stay isospectral to 1e-15 for the tick, with Hc at every tested strength and with eta s, and the free Hc alone has identical family spectra; a nonzero linear intertwiner between the j = 1 and j = 2 sectors exists for the generator set {both tilings' reflections, s, Hc, eta s} (dimensions 16, 8, 8, 4 as generators are added), a per-sector algebraic map not shown to be a lattice operator; a polar cube potential along the turn axis splits the pair only when combined with a time-ordering or chiral breaking, at first order in each (split about 1.59 kap lam). On the Z_3 family group pair differences are psi, psi, psi^2, so at most two spurion distances arise, and with unit coefficients and eps <= 1/2 a Z_3 circulant Dirac matrix gives a largest mass ratio of 4.0. Estimates against supplied measured masses: the needed relative splitting of the two lighter families is order one (0.904-0.996). Supplied model, finite diagnostic: the torus size, eps, mu, MN and the term strengths, the test terms, the zoom-3 family reading, the unit coefficients and the masses."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/conjugate_zoom_three_families_stay_degenerate_under_the_cube_tick_and_its_chiral_generator_2026_10_22.py
---

# The conjugate zoom-3 families stay degenerate under the cube tick and its chiral generator

Claim type: bounded_theorem.
Primary runner: `scripts/conjugate_zoom_three_families_stay_degenerate_under_the_cube_tick_and_its_chiral_generator_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It reads the three families as the turn-fixed characters (j,j,j) of the update law's tick translations T(2 e_i), and records that the k -> -k symmetry keeps two families degenerate. Measurement shows no two degenerate families in any sector. This note asks which operator ties j to -j, whether the copy mass or the chiral generator unties the pair, and what does split it. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

The supplied model is the update law's cube tick. The spin-3/2 edge hop W sits on 2 x 2 x 2 cubes, in two tilings offset by (1,1,1). Even cubes carry Cm exp(-i(eps - mu/2) R) Cm, with the copy-mass factor Cm = exp(i (MN/4)(1 - s) R), and odd cubes exp(+i(eps + mu/2) R). It runs on a 6^3 torus in the single-particle sector, with eps = 0.3, mu = 0.05 and MN = 0.2 unless stated. The family sectors are the characters of T(2 e_i) on the turn-fixed line a = j(1,1,1).

A. The cube.

1. Face flux. The spin-S overlap of the corner coherent states gives each face flux 2 pi S/3. The flux is T-even (0 or pi) only for S in (3/2)Z. The update law's S = 3/2 gives pi flux, so the cube reflection R = sum_i W_i is real in a gauge and R^2 = 1.
2. Copy sign. In that gauge the copy sign s = i R1 R2 R3 R (R_i = sqrt3 W_i) is purely imaginary, with [s, R] = 0 and s^2 = 1. So K maps s to -s: the copy mass breaks plain time reversal and keeps only K composed with an odd rotation.

B. Operators sending j to -j. These are the 48 cube-centred point maps x -> c + g(x - c), c = (1/2, 1/2, 1/2), each unitary or composed with K, with the gauge fitted.

3. Ties. Count the point maps that send j to -j and keep the quasi-energy (+ proper, - improper, K antiunitary):
   - no copy mass: 12 maps, 3 each of +, -, K+ and K-;
   - with the copy mass: 6 maps, 3 each of - and K-;
   - adding the chiral generator Hc = (i/2)[W_o, W_e]: 3 maps, all -;
   - adding the inversion-odd pseudoscalar eta s (sublattice sign times copy sign): none.

   The runner names these maps (the C2' rotations about face diagonals, inversion I, S6 = I C3, K and K C3, then I, S6 and K sigma_d, then I and S6). The counts are computed; the names are stated. Hc is imaginary in the real gauge, so it breaks the K-type ties.
4. Inversion. Inversion about a cube centre, with its gauge, maps both tilings to themselves. It fixes R, each R_i, s and Hc, so every update-law term and Hc commute with it. It flips the sublattice sign, so eta s is inversion-odd. The runner states, and does not check, that eta s is invariant under all 24 rotations.

C. Family spectra.

5. The families j = 1, 2 stay exactly isospectral (signed quasi-energies) for the tick, with and without the copy mass, with Hc at strengths 0.05, 0.2 and 0.5, with eta s (palindromic and once per tick), and with both together.
6. The free chiral generator alone has identical family spectra: [-0.866 x 4, +0.866 x 4] in each sector. Hence exp(-i t Hc) is family-degenerate for every t.
7. The tie that survives eta s is algebraic, not a point map. For the generator set {W_e, W_o, s, Hc, eta s} there is a nonzero linear map Y with Y G_(j=1) = G_(j=2) Y for every generator. The intertwiner-space dimensions are 16, 8, 8 and 4 as s, Hc and eta s are added. Every free tick that is a word in these generators therefore keeps families 1 and 2 degenerate. The runner states that Y can be taken unitary; it checks that the intertwiner space is nonzero. Y is a per-sector map, not shown to be a lattice operator, and interactions are not tested.

D. What splits the pair.

8. Take a polar cube potential graded by |c|. It carries a direction along the turn axis (the runner calls it an axial vector), breaks the rotations to C3v and breaks inversion.
   - Placed palindromically, it keeps K sigma_d and the families stay tied.
   - Placed once per tick, a time-ordering choice, it splits them at first order in its strength.
   - Placed palindromically together with Hc, the split is first order in each strength, bilinear at small strengths (split about 1.59 kap lam).
   - A generic cube term splits at about first order.
   - For {W_e, W_o, s, polar term} the intertwiner space is zero.
9. A T-odd hop alone does not split. The spin-1/2 overlap (flux pi/3 per face) keeps inversion.

E. Z_3 differences.

10. The family group is the order-3 subgroup {0, psi, psi^2}, so the pair differences are psi, psi and psi^2. With k -> -k there is one spurion distance; without it, at most two, since pairs 12 and 23 always share psi. Breaking k -> -k never gives three distances. The runner records this as a stated combinatorial check.
11. With k -> -k broken, a translation-invariant Dirac matrix on that group is a Z_3 circulant c0 + c1 eps P + c2 eps^n P^2 with eigenvalues |c0 + c1 eps w^j + c2 eps^n w^2j|. With unit coefficients, eps in {1/2, 1/3, 0.22} and n in {1, 2, 3}, the largest mass ratio is 4.0.

## Derivation

Item 1 builds the spin-S corner coherent states along the cube diagonals, the hop phases from their overlaps, and the plaquette products. Item 2 fixes the gauge by a spanning tree and inspects s. Item 3 builds the 48 signed permutation matrices about the cube centre, fits a diagonal gauge to each (with or without K), and tests whether the image of the tick's factor list equals the list, or its reversed adjoint, up to cyclic order. Item 4 compares conjugated operators. Items 5-6 project the 6^3 single-particle tick onto the two 8-dimensional family sectors (27 translates of the 8 cube corners) and compare sorted quasi-energies. Item 7 computes the null space of the stacked linear intertwiner equations by SVD. Item 8 measures the split at two strengths and fits its order as log(split ratio)/log 2; the generic cube term uses a seeded random Hermitian 8 x 8 matrix. Item 11 evaluates the circulant eigenvalues.

## Finite checks

Exact or enumerated checks (the runner asserts each):
- Face flux for S = 1/2, 1, 3/2, 3: 1.047, 2.094, 3.142, 0.000. The imaginary part of R in the real gauge is 4e-15 (asserted below 1e-12); R^2 = 1.
- s is purely imaginary in the gauge, [s, R] = 0 and s^2 = 1.
- Tie counts: [('+', 3), ('-', 3), ('K+', 3), ('K-', 3)] without copy mass; [('-', 3), ('K-', 3)] with it; [('-', 3)] with Hc; [] with eta s.
- Inversion: maximum commutator 1e-14 with R, R_i, s and Hc. eta s anticommutes with it.
- Intertwiner dimensions [16, 8, 8, 4], all nonzero.

Finite diagnostics (supplied model, finite diagnostic):
- Family split, maximum over the signed quasi-energies, all below 1e-12:

| case | split |
|---|---|
| tick | 8e-16 |
| no copy mass | 3e-16 |
| Hc 0.05 | 4e-16 |
| Hc 0.2 | 3e-16 |
| Hc 0.5 | 7e-16 |
| eta s 0.1 | 7e-16 |
| eta s 0.1, once per tick | 8e-16 |
| Hc 0.2 + eta s 0.3 | 1e-15 |

- Free Hc family spectrum: [-0.866 -0.866 -0.866 -0.866 0.866 0.866 0.866 0.866] in both sectors.
- Polar term:
  - palindromic: split 1e-15;
  - once per tick: fitted order 1.0, split 1.8e-03 at strength 0.04;
  - palindromic with Hc: order 1.0 in the polar strength and 1.0 in the chiral one, split = 1.59 kap lam at kap = 0.02, lam = 0.01;
  - generic seeded cube term: order 0.9;
  - intertwiner dimension 0.
- Spin-1/2 overlap tick: split 4e-16.

The random cube term uses a fixed seed (7).

## Estimates against measurement

- Circulant ratio. The largest Z_3-circulant mass ratio, 4.0, is set against the measured m_t/m_u = 1.4e5 and m_tau/m_e = 3.5e3.
- Needed splitting. Measurement shows no two degenerate families in any sector, so the rules must untie a conjugate pair. Read with the two lighter families as the pair, the needed relative splitting (m2 - m1)/(m2 + m1) is 0.990 (leptons), 0.996 (up) and 0.904 (down): order one, not a small breaking. The supplied masses are 0.000511, 0.10566 and 1.77686 GeV (leptons); 0.00123, 0.620 and 171.7 GeV (up); 0.00267, 0.0532 and 2.84 GeV (down).
- Consequence. In this model the pair splits only with a directed term together with a time-reversal or time-ordering breaker, first order in each. With small breakings the split is second order (kap lam), far below the order-one split needed. This is a reading of the diagnostics, not a theorem.

## Boundary

Not claimed: that the algebraic intertwiner of item 7 is a lattice operator or survives interactions; any statement beyond the single-particle sector on a 6^3 torus; the names attached to the counted point maps, the unitarity of Y and the rotation invariance of eta s (stated); a mechanism in the rules that supplies the directed term and the time-reversal breaker at order-one strength; any mass or mixing prediction; any reading of the families other than the turn-fixed zoom-3 characters. The Z_3 statements of items 10 and 11 are about translation-invariant mass matrices with unit coefficients only.

## Supplied vs forced

Supplied: the torus size L = 6; eps = 0.3, mu = 0.05, MN = 0.2; the strengths of Hc, eta s, the polar and generic terms; the test terms themselves (eta s, the polar |c|-graded potential, the seeded generic term, the spin-1/2 hop); their placement (palindromic or once per tick); the zoom-3 family reading; the unit coefficients and eps values in item 11; the measured masses. Forced, given those: the face flux 2 pi S/3 and the real gauge at S = 3/2; the imaginary copy sign and its K-oddness; the tie counts under each added term; inversion invariance of every update-law term and of Hc; exact family isospectrality for the tick, Hc and eta s; a nonzero intertwiner for the full generator set; first-order splitting by a directed term only together with a time-reversal or time-ordering breaker; at most two spurion distances on the Z_3 family group.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's cube tick (spin-3/2 edge hop, two tilings, the copy-mass factor), its translations T(2 e_i), the zoom-3 family reading, and the chiral generator built from the two tilings. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/conjugate_zoom_three_families_stay_degenerate_under_the_cube_tick_and_its_chiral_generator_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 150 MB resident, prints about 4.8 kB and ends with `TOTAL: PASS=12 FAIL=0`. Its random draw uses a fixed seed; two runs gave identical output.
