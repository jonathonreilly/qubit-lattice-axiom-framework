---
claim_id: the_lattice_theta_density_is_odd_under_the_kept_antiunitary_and_zoom_three_characters_give_theta_bar_zero_at_renormalisable_order_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "On quantum rishon link registers: on one cube of 12 spin-1/2 U(1) links the lattice theta density q = sum_k E_k B_k (B = Im U_p) is gauge invariant (commutes with every corner Gauss generator to 0e+00) and odd under complex conjugation K and under inversion, while the ring term is real and invariant, so an exact kept antiunitary (or exact inversion) forbids a theta coefficient; with K kept and a theta coefficient present, spec H(c q) = spec H(-c q) and <q> is nonzero (finite diagnostic on a two-state Gauss sector). On one SU(3) rishon link with quarks (12 modes) the det term is the only term charged under the odd-cluster fermion number, so its uniform phase is removed by e^{i chi N_y} (equal 924-level spectra to 2e-14). In a 1+1D quantum link Schwinger chain (L = 8) spin S = 1/2 gives two vacua with flux +-1/2 (theta = pi) and S = 1 one vacuum with flux 0 (theta = 0) (finite chain). With real coefficients and one doublet, its vacuum phase is a hypercharge rotation: J = 0 and arg det(M_u M_d) in {0, pi} (50 x 3 random samples, heavy vector-like copies included); two doublets give J != 0 with theta_bar of order one. With zoom-3 translation characters (light families (j,j,j), heavy copies off the diagonal) every doublet-filled light-heavy entry is forbidden, and singlet vacua carrying heavy-coset characters give arg det(M_u M_d) = 0 or pi exactly at renormalisable order while J != 0 (200 random samples per case); the first leak at dimension five scales as theta_bar ~ eps for full vector-like copies and eps^2 for singlet-only copies (fitted slopes 1.01 and 2.04). Estimates against the EDM bound on theta_bar and LHC vector-like-quark searches are estimates with a supplied unit map. Supplied model, finite diagnostic: the link spins, cube and chain sizes, the coupling values, the random coefficient ensembles, the heavy-copy content, the vacuum characters, the theta_bar bound and the unit map."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_lattice_theta_density_is_odd_under_the_kept_antiunitary_and_zoom_three_characters_give_theta_bar_zero_at_renormalisable_order_2026_10_22.py
---

# The lattice theta density is odd under the kept antiunitary, and zoom-3 characters give theta_bar = 0 at renormalisable order

Claim type: bounded_theorem.
Primary runner: `scripts/the_lattice_theta_density_is_odd_under_the_kept_antiunitary_and_zoom_three_characters_give_theta_bar_zero_at_renormalisable_order_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its gauge content lives on quantum link registers (rishon links), its family structure is read from the zoom-3 translation characters of the update law's tick, and its terms are real in the occupation basis, so complex conjugation K is a kept antiunitary. This note asks where the strong-CP parameter theta_bar can enter: as a lattice theta density in the link sector, as a phase of the det term, as a vacuum phase in the mass matrices, or through heavy copies. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Link sector (one cube, 12 spin-1/2 U(1) links, E = S^z, U = S^+).

1. The ring exchange sum_p (U_p + U_p^dag) and the corner Gauss generators are real. B = Im U_p is imaginary antisymmetric, so the lattice theta density q = sum_k E_k B_k (E_k, B_k summed over links and faces of direction k) is K-odd (K q K = -q) and commutes with every Gauss generator.
2. q is odd under inversion and even under the proper turn C4 and under rishon particle-hole (E -> -E, U -> U^dag); the ring term is invariant under all three. An exact kept antiunitary, or exact inversion, therefore forbids a theta coefficient c q.
3. With K kept (real terms) and inversion and turns broken by a random real field, a theta coefficient is physical once present: spec H(c q) = spec H(-c q), <q> = 0 at c = 0, and <q> != 0 at c != 0.

B. Det-term phase (one SU(3) rishon link with quarks, 12 modes).

4. The hop and det terms are real in the occupation basis, and K maps each of the 8 colour generators to plus or minus itself, so K preserves the colour Gauss law: the link sector carries an exact antiunitary.
5. The det term is the only term charged under the odd-cluster fermion number N_y ([N_y, det] = 3 det, [N_y, hop] = 0). Hence e^{i chi N_y} maps H(phi) to H(phi + 3 chi): a uniform det-term phase is removable and is not theta.

C. 1+1D theta from the link spin (quantum link Schwinger chain, L = 8, staggered, Gauss law exact, t = 1, m = 4, g^2 = 1).

6. S = 1/2: two near-degenerate vacua carrying flux +-1/2, exchanged by E -> -E (theta = pi). S = 1: one vacuum with flux 0 (theta = 0). The flux offset, 2S mod 2, is the 1+1D theta. The runner states, and does not compute, that the splitting scales as (t/m)^L; it computes the splitting at L = 8 only.

D. Mass matrices with real coefficients (the kept antiunitary), CP broken only by vacuum phases.

7. One doublet with a vacuum phase, heavy vector-like copies and bare masses included: the phase is a hypercharge rotation (anomaly-free in SU(3)^2), so J = 0 and arg det(M_u M_d) lies in {0, pi}.
8. Two doublets with a relative vacuum phase: J != 0, but theta_bar is of order one.

E. Zoom-3 translation characters (light families at (j,j,j), heavy copies at off-diagonal characters h0 + L, h0 = (0,1,2)).

9. Translation characters forbid every doublet-filled light-heavy entry: H carries a character in the light subgroup L, light positions form L, and heavy positions lie outside it. The opposite Nelson-Barr block vanishes at renormalisable order.
10. At renormalisable order, with every coefficient real and CP broken only by singlet vacua sigma_kappa carrying heavy-coset characters, arg det(M_u M_d) is exactly 0 or pi, both for singlet-only copies and for full vector-like heavy copies, while J != 0. The runner states the reason (the blocks sigma fills close no determinant loop) and checks the consequence numerically.
11. The first leak is the dimension-five H sigma entry, with coefficient eps. A two-vacuum loop carries sigma_k sigma_k^* (real), so a complex loop needs three vacua whose characters sum to zero (stated). Full copies close one at first order (through the heavy-heavy H sigma entry), giving theta_bar ~ eps; singlet-only copies first close one at second order, giving theta_bar ~ eps^2 (fitted).

## Derivation

Items 1-3 build the 2^12-dimensional link space of one cube as sparse Kronecker products, form U_p on the six faces, q, the eight corner Gauss generators, and the inversion, C4 and particle-hole operators as signed permutations of links; item 3 diagonalises H = -ring + 0.3 field + c q in the Gauss sector of largest q norm (dimension 2) at c = 0, +-0.2. Items 4-5 build 12 fermionic modes by Jordan-Wigner, the 8 Gell-Mann colour generators, the hop and det operators, and compare spectra of H(0) and H(phi = 1.234) in the N = 6 sector (924 states). Item 6 enumerates Gauss-law states of the chain (dimension 47 for S = 1/2, 117 for S = 1), diagonalises, and reads the flux of the two lowest states. Items 7-11 build random real-coefficient mass matrices with the stated character selection rules, compute J from the light left-handed eigenvectors and arg det(M_u M_d) mod pi; item 11 fits log theta_bar against log eps over eps = 1e-6, 1e-5, 1e-4 (200 samples each, median).

## Finite checks

Exact or closed-form checks (the runner asserts each):
- Link sector: |Re q| = 0e+00; max |[q, G]| = 0e+00; |P q P + q| = 0e+00, |C4 q C4' - q| = 0e+00, |PH q PH - q| = 0e+00; ring term invariant under all three.
- Det-term phase: |U H(0) U' - H(phi)| = 3e-16; N = 6 spectra (924 levels) equal to 2e-14. Reality of hop and det terms and K-parity of the colour generators asserted.
- Translation-character selection rule (item 9): asserted combinatorially for both heavy characters and all light characters.

Finite diagnostics (supplied model, finite diagnostic):
- Theta coefficient present (item 3): sector dimension 2, max |dE| = 0e+00, <q>(0) = 0e+00, <q>(0.2) = -4.89e-02, gap 2.04.
- Schwinger chain (item 6): S = 1/2, dimension 47, splitting/gap 2e-06, fluxes -0.493, +0.493; S = 1, dimension 117, splitting/gap 1.00.
- One doublet (item 7): 50 samples x 3 phases (0, 0.9, 2.1): max |J| = 4e-15, max distance of arg det from {0, pi} = 4e-14.
- Two doublets (item 8): 400 samples: median J = 1.8e-02, median |theta_bar| = 0.68, minimum 8e-04.
- Zoom-3 characters at renormalisable order (item 10), 200 samples each: singlet-only copies median J = 7.2e-03, max distance 0e+00; full copies median J = 6.4e-03, max distance 9e-16.
- First leak (item 11): full copies slope 1.01 (theta_bar 3e-05 at eps = 1e-6); singlet-only copies slope 2.04 (6e-10 at eps = 1e-6).

The random ensembles use a fixed seed (20261022).

## Estimates against measurement

Estimates with supplied inputs: the unit map 1/a = 2.435e18 GeV, v = 246 GeV, m_u = 2.16e-3 GeV, and the bound |theta_bar| < 7.5e-11 (from the neutron electric dipole moment); eps = v sigma/(Lambda m_u) per unit coefficient.
- Full copies (theta_bar ~ eps) need sigma ~ M < 1.6e+03 GeV (1604 GeV); singlet-only copies (theta_bar ~ eps^2) need sigma ~ M < 1.9e+08 GeV.
- Copies and vacua at the cell scale give eps ~ v/m_u = 1e+05: no protection there.
- The full-copy scale sits at the quoted LHC vector-like-quark search bounds (about 1.3-1.5 TeV, quoted, not computed).

## Boundary

Not claimed: a derivation of the heavy-copy content, the vacuum characters or their scales from the register; a statement about the thermodynamic or continuum limit of the link models (one cube, one link, an L = 8 chain); the (t/m)^L scaling of the 1+1D splitting (stated, not computed); the loop-closure reason in item 10 and the three-vacuum statement in item 11 as theorems (stated; their consequences are checked numerically); theta_bar beyond dimension five or from running; the sign of a theta coefficient if the kept antiunitary is broken elsewhere; any experimental exclusion (the estimates are order-of-magnitude with supplied inputs).

## Supplied vs forced

Supplied: the spin-1/2 U(1) links on one cube, the random real field, the SU(3) rishon link with 12 modes and its couplings (t = 1, gamma = 0.7, m = 0.4, Casimir weight 0.3), the Schwinger chain parameters, the random coefficient ensembles, the heavy-copy content (singlet-only or full vector-like), the heavy characters h0 + L, the vacuum magnitudes, eps, the unit map, v, m_u, the theta_bar bound and the quoted LHC bounds. Forced, given those: the K-oddness, inversion-oddness and gauge invariance of q; the removability of the det-term phase; the flux 2S mod 2 at L = 8; J = 0 with one doublet; the vanishing of doublet-filled light-heavy entries; arg det(M_u M_d) in {0, pi} at renormalisable order with J != 0; the eps and eps^2 leak orders.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's tick translations (read at zoom 3 for the family characters), the quantum link registers with real terms (the kept antiunitary). Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/the_lattice_theta_density_is_odd_under_the_kept_antiunitary_and_zoom_three_characters_give_theta_bar_zero_at_renormalisable_order_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 100 MB resident, prints about 4.3 kB and ends with `TOTAL: PASS=12 FAIL=0`. Its random draws use a fixed seed; two repeated runs gave identical output.
