---
claim_id: one_mode_free_sites_carry_no_exact_3450_charge_and_rotor_matter_admits_an_exact_depth_three_chiral_disentangler_in_1plus1d_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "In 1+1D: on chains of one-mode fermion sites with the staggered hop, the vector charge and the Kitaev-pairing axial charge are exact, but the chiral 3450 combination has non-integer one-body and many-body spectra, so no circuit, free or interacting, on-site or not, makes it an exact U(1) (spectral obstruction). With non-slipping rotor matter (an angle per site and a winding integer per link), the rederived Thorngren-Preskill-Fidkowski disentangler (one on-site and two link layers) maps the 3450 symmetry exactly onto an on-site ancilla symmetry, checked in exact rational arithmetic; anomalous charge sets (sum q_V q_A != 0) fail by exactly the predicted phase and carry endpoint charge; the dressed charges are local integers; linking gives an exact Gauss law that eats the ancillas, a Schwinger term proportional to sum q_V q_A, and, in a Gaussian reading, one massless neutral mode plus a massive photon; the Trotterised Gaussian update has one zero per flavour (no doublers) and the zero modes carry the chiral charges L(3,4), R(5,0). With Z_5 clocks only Z_5 is exact. In 3+1D, the 16 Weyl fields of one family with the right-handed neutrino group into four blocks of the source construction with vanishing mixed anomalies, and the Kuhn triangulation count is stated. Source construction: arXiv:2601.04304. Supplied model, finite diagnostic; no chiral SU(2), no V - A structure and no derivation of rotor matter from the axioms."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/one_mode_free_sites_carry_no_exact_3450_charge_and_rotor_matter_admits_an_exact_depth_three_chiral_disentangler_in_1plus1d_2026_10_22.py
---

# One-mode free sites carry no exact 3450 charge, and rotor matter admits an exact depth-three chiral disentangler in 1+1D

Claim type: bounded_theorem.
Primary runner: `scripts/one_mode_free_sites_carry_no_exact_3450_charge_and_rotor_matter_admits_an_exact_depth_three_chiral_disentangler_in_1plus1d_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) puts one fermion mode on each site and lets links be carried by registers. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix the lattice and one qubit per site but no chiral charge. This note asks whether an exact chiral U(1), the 1+1D "3450" model with left charges 3, 4 and right charges 5, 0 (3^2 + 4^2 = 5^2 + 0^2), can be carried and linked. It rederives and tests the symmetry-disentangler construction of Thorngren, Preskill and Fidkowski (arXiv:2601.04304, cited as the source construction: its disentangler, block charges, Standard Model grouping and per-face fermion / per-vertex rotor layout).

## Statement

1. One-mode fermion chains. On a free chain with the staggered hop, the vector charge Q_V and the Kitaev-pairing axial charge Q_A are conserved and quantised (Q_A^2 = 1) and do not commute; K = 0 moves right with Q_A = +1 and K = pi moves left with Q_A = -1. The 3450 combination, 4 Q_V + Q_A on flavour 1 and 2 Q_V - 2 Q_A on flavour 2, is conserved with node charges L(3, 4), R(5, 0), but its one-body levels sqrt(17 + 8 cos K) and 4 |sin(K/2)| are not integers, and neither are its many-body levels. A U(1) generator must have integer spectrum, and conjugating by any unitary circuit, interacting or not, preserves the spectrum, so no circuit makes it a U(1).
2. Counting form (stated). A quantised one-body charge of a free one-mode update has #R(+-q) = #L(+-q). The 3450 assignment fails this, so no free one-mode lattice carries it, on-site or not.
3. Rotor matter. Give each flavour a rotor angle phi_j in [0, 1) per site and a winding integer n_j per link (non-slipping Villain matter). Then Q_V (turns) and Q_A (windings) are commuting integers, and the kinetic gate (turn phi_j, relabel windings) commutes with every e^{2 pi i b Q}, is a U(1) action and keeps Q_A.
4. Disentangler. W = [turn each flavour by q_V theta_j] x prod_j e^{-2 pi i theta_j y~_j}, one on-site layer and two link layers, satisfies W^dag e^{2 pi i b Q} W = e^{2 pi i b Q_anc} exactly when sum q_V q_A = 0, with Q_anc the on-site ancilla charge. It is single-valued on the rotor circle only with its -d round(sum q_A phi) term.
5. Anomalous sets. For c = sum q_V q_A != 0 the identity fails, exactly by the phase -c sum_j theta_j (k_{j+1} - k_j), where k counts ancilla wraps. Equivalently, the 2 pi axial turn cut to an interval is exactly e^{2 pi i sum q_A (phi_b - phi_a)}, with endpoint charges +-c; a nonzero c forbids every disentangler.
6. Dressed charges. rho_j = W L_j W^dag commute, are integers, touch sites j-1 .. j+1 only and sum exactly to Q for 3450; for an anomalous set they sum to a different U(1) action.
7. Finite clocks. With Z_5 clocks in place of rotors (all carriers finite) the same circuit disentangles the exact Z_5 chiral symmetry iff sum q_V q_A = 0 mod 5. Only Z_5 is exact; the chiral U(1) can at most emerge in a critical clock phase, which needs N >= 5 (cited).
8. Light content. The Trotterised Gaussian update has cos Omega_K = 1 - 2 (eps v)^2 sin^2(K/2), stable for eps v < 1, with one zero (K = 0) per flavour: no doublers. At the Dirac radius the lowest one-flavour spin +2 zero modes carry Q = +-6, +-8 and the spin -2 ones +-10, 0, 0, twice L(3, 4) and R(5, 0); the vector control gives equal sets.
9. Linking. With a link angle a and electric value E, Gauss's law G_j = E_{j+1/2} - E_{j-1/2} - rho_j holds exactly: the linked potential and the linked kinetic gate commute with every finite Gauss transformation and reduce to the unlinked gates at a = 0. In the on-site frame q_A acts only through whole flux units and Gauss's law eats the ancillas. The continuous chiral densities obey [rho_j, rho_{j-1}] = -i c/(2 pi), so the Gauss generators commute iff c = 0. In the Gaussian reading, 3450 keeps one massless neutral mode and a photon with m^2 = (g^2/pi)(sum q_L^2 + sum q_R^2)/2 = 25 g^2/pi; an anomalous set instead has a non-local chiral branch Omega ~ g^2 |c|/(pi K).
10. 3+1D grouping. With hypercharges times 6, the 16 left-handed Weyl fields of one family including the conjugate right-handed neutrino nu^c group into four blocks of four with (V, A) charges (1,1), (-1,1), (0,-1), (0,-1): three quark blocks -3V - A = (-4, 2, 1, 1) and one lepton block 3V + 3A = (6, 0, -3, -3), with sum Y = sum Y^3 = 0, vanishing mixed sum a^2 b over blocks, and 3(B - L) built from A, jointly anomaly-free with Y. Each block has only the AVV anomaly (value 2).

## Derivation

Item 1: the axial charge of Chatterjee, Pace and Shao (cited) is the Kitaev-pairing bilinear; any combination a Q_V + b Q_A is a quadratic form whose one-body levels are sqrt(a^2 + b^2 + 2ab cos K). For (4, 1) and (2, -2) these are not integers for generic K. Integer spectrum is a unitary invariant, which gives the obstruction for every circuit. Items 3-6 are identities between gates on configurations (angles, windings, ancilla angles), so the runner checks them in exact Fraction arithmetic on random rational configurations: both sides must give the same configuration and the same phase mod 1. The predicted anomalous phase and the endpoint formula are checked the same way. Item 8: the quadratic Villain update is a product of two shears; its trace gives the dispersion. Zero modes are enumerated over momenta p and windings w with E = (2 pi v/L) sum(p^2 + w^2/4) and P = (2 pi/L) sum p w. Item 9: the Schwinger term is the symplectic form evaluated on the density vectors; the linked normal modes come from the Gaussian quadratic form.

## Checks

The runner ends with `TOTAL: PASS=18 FAIL=0` in about 2.4 s. Exact checks:

- Free chain (12 sites): conservation and Q_A^2 = 1 to 1e-13, v(0) = +1.00, v(pi) = -1.00. 3450 levels match sqrt(17 + 8 cos K) and 4 |sin(K/2)|; largest distance to the integers 0.417 and 0.464, many-body (4 + 4 modes) 0.343.
- The counting form of item 2 is checked only as the multiset test (R = {5, 0} against L = {3, 4} fails; a vector control passes); the general statement is stated, not computed.
- Rotor gates, 300 random rational configurations on 5 sites: 0 failures of commutation, group law and Q_A conservation.
- Disentangler identity: 0 failures for 3450, for TPF's (3,3),(9,-1) and for a three-flavour anomaly-free set; single-valuedness on the circle 0 failures with the rounding term against 148 of 150 without it.
- Anomalous sets: Dirac (2,0) with c = 2 fails 182/300 and 3452 with c = -2 fails 191/300, while the predicted phase matches 300/300 in both. Endpoint charges +0, +2, -2 for 3450, Dirac (2,0), 3452 (150 configurations each).
- Dressed charges: 0 failures of the sum and of locality; for Dirac (2,0) the sum differs from Q in 92/150.
- Z_5 clocks (200 configurations each): failures 0 for 3450, 0 for (5,1) with c = 5, 135 for Dirac (2,0), 156 for 3452.
- Dispersion at eps = 0.5, v = 1: matches cos Omega_K = 1 - 2 (eps v)^2 sin^2(K/2), monotone, Omega(pi) = 1.047 < pi. Zero-mode charges: spin +2 [-8, -6, 6, 8], spin -2 [-10, 0, 0, 10].
- Linking, 300 configurations: 0 failures of Gauss covariance and reduction at a = 0; 0 failures of the on-site frame identities. Schwinger term max |C|: 0.0000 for 3450, 0.3183 for both anomalous sets (c/(2 pi) with |c| = 2).
- SM grouping: the listed sums are evaluated exactly. The runner also verifies that (1, 5, 9, -7, -8) is anomaly-free; the statements that it, and the 15 fields without nu^c, admit no block grouping, and that there is no SU(2)_L disentangler, are stated, not computed.
- Kuhn triangulation of a 4^3 torus: 7 edges, 12 triangles, 6 tetrahedra per vertex, Euler number 0. The per-site budget of the source layout (4 charged vertex rotors, 1 ancilla per linked U(1), 48 fermion modes, one per triangle per block, 7 link rotors per site per generation) is stated, not computed.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):

- Folding of the update: at eps 2 pi v/L = pi/8, zero modes with E = 16 m sit at quasi-energy 0; among the 288 such states with |p|, |w| <= 8, 6 have Q = 0, e.g. (-4, 0, 8, 0). That a rotor's kinetic phases come within any delta of 0 for every step (Weyl equidistribution, cited) is stated: unbounded carriers leave no quasi-energy gap above the vacuum.
- Linked Gaussian modes at g = 0.2, K = 0.005: photon mass 0.56421 against sqrt(25 g^2/pi) = 0.56419, plus one massless neutral mode; for 3452 the chiral branch is 5.16 against g^2 |c|/(pi K) = 5.09 (within the 3% tolerance).

## Costs and open items

- Rotor matter is not the register's one fermion mode per site: the exact chiral U(1) needs unbounded carriers (angles and winding integers). With finite carriers (Z_5 clocks) only Z_5 is exact.
- With unbounded rotors there is no quasi-energy gap above the vacuum in the update (folding), so the light content is a statement about the Gaussian sector with zero modes, not a gapped spectrum.
- The ancillas are supplied and only become harmless after linking (Gauss's law eats them).
- In 3+1D the grouping needs nu^c (the 16th field); it is then required but sterile. The construction gives abelian chiral charges only: it builds no chiral SU(2)_L and so no V - A charged current (the runner quotes the measured TWIST value P_mu xi = 1.0008 and N_nu = 2.984 +- 0.008 as measurements, not computations).
- Supplied: the 3450 charges and their pairing (L3, R5), (L4, R0), the Dirac radius, rounding half up, g and eps.

## Boundary

Forced, given the supplied inputs: the spectral obstruction on one-mode free sites; the exactness of the disentangler on rotor matter iff sum q_V q_A = 0; the anomalous phase and endpoint charge; local integer dressed charges; the exact Gauss law and the Schwinger-term condition; one zero per flavour of the Gaussian update; the chiral zero-mode charges; the anomaly sums of the 16-field grouping. Not claimed: that the register's update contains rotor matter or ancillas, any 3+1D lattice construction beyond the counting, chiral SU(2), a continuum limit, or any identification of the 1+1D model with measured particles.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix no chiral charge and no rotor matter.
- [Candidate-law register](CANDIDATE_LAWS.md): one fermion mode per site and link registers in the update law. Zero premise weight; results using it are conditional on it.
- Cited, not rederived beyond what is stated: Thorngren, Preskill and Fidkowski, arXiv:2601.04304 (source construction); Chatterjee, Pace and Shao (Onsager axial charge); bosonization at the Dirac radius; Weyl equidistribution; the N >= 5 critical phase of Z_N clocks.

## How to run

```
python3 scripts/one_mode_free_sites_carry_no_exact_3450_charge_and_rotor_matter_admits_an_exact_depth_three_chiral_disentangler_in_1plus1d_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120` (with an internal alarm 5 s earlier), runs in about 2.5 s with about 70 MB resident, prints about 5.5 kB and ends with `TOTAL: PASS=18 FAIL=0`.
