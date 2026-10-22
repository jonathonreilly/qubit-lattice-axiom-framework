---
claim_id: fermion_parity_is_the_vector_su2_centre_not_the_chiral_half_and_two_singlet_rotors_give_jointly_chiral_su2_x_u1_with_on_site_gluing_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For an SU(2) doublet carried on fermion modes in 1+1D: on a cell of two complex modes the SU(2) centre is the cell fermion parity and the commuting charge SU(2) has centre minus it, and a supplied non-on-site chiral SU(2) on 3 cells also has centre equal to fermion parity up to a phase; in the vertex-lattice description the centre of any on-site SU(2) flows to the vector centre z_L z_R, which on the doublet is the fermion parity (Z_8 index 0), while the gluing of charge parity to SU(2) centre needs the left-mover centre z_L, which on the doublet is the chiral fermion parity (twisted spin 1/4, Z_8 index 4) and is not on-site; a spin carrier whose gapless sector is one SU(2)_1 per chirality has no fermionic operator, and in the half-filled Hubbard ring (L = 4, 6, U = 4) the lowest triplet carries momentum pi relative to the singlet ground state, so with the charge gapped the infrared spin half is lattice translation. A construction on fermion modes plus two supplied SU(2)-singlet compact rotors (charges (2, 4) and (-2, 4)) with one null locking term per rotor leaves exactly free Weyl modes L = (2,3) + 2(1,1), R = (2,1) + 2(1,3) (the swap content), anomaly-free with no invariant bilinear mass; the gluing generator equals the on-site singlet fermion parity on all 531441 sampled carrier states; the TPF rotor disentangler is exact for the anomaly-free rotor pair and fails for anomalous sets; the locking vertex is marginal at the free point and relevant under a supplied forward-scattering term. Supplied model, finite diagnostic: rotor matter, charges, locking couplings and forward scattering supplied; the flow to the locked phase is cited, not computed; 1+1D only."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/fermion_parity_is_the_vector_su2_centre_not_the_chiral_half_and_two_singlet_rotors_give_jointly_chiral_su2_x_u1_with_on_site_gluing_2026_10_22.py
---

# Fermion parity is the vector SU(2) centre, not the chiral half, and two singlet rotors give jointly chiral SU(2) x U(1) with on-site gluing

Claim type: bounded_theorem.
Primary runner: `scripts/fermion_parity_is_the_vector_su2_centre_not_the_chiral_half_and_two_singlet_rotors_give_jointly_chiral_su2_x_u1_with_on_site_gluing_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its chirality work needs an SU(2) doublet whose Z_2 centre is glued to the parity of a U(1) charge, as in the Standard Model's (SU(2) x U(1))/Z_2, and the register records that this gluing splits into two anomalous halves. If the doublet is carried on fermion modes, the SU(2) centre is fermion parity, which is on-site; this note asks whether that makes the gluing local, and then builds a 1+1D lattice construction of jointly chiral SU(2) x U(1) in which it is. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. One cell of two complex modes (4 Majoranas), spin S^a = c^dag sigma^a c/2, pseudospin eta^+ = c_up^dag c_dn^dag.

1. The SU(2) centre e^{2 pi i S^z} is the cell fermion parity (-1)^n; the commuting charge SU(2) has centre -(-1)^n, so their product is -1 on every cell: on fermion modes the doublet gluing is an operator identity. The singlet pair c_up^dag c_dn^dag commutes with SU(2) and carries charge 2.
2. A supplied chiral SU(2) on 3 cells (12 Majoranas, with one Majorana per cell shifted to the next cell, so not on-site) also has centre e^{2 pi i T^3} equal to (phase) x (-1)^F, here with phase -1: internal, on-site and equal to fermion parity before any disentangler.

B. What fermion parity cannot do (vertex lattices v = (nL, mL, nR, mR), spin (nL^2 + mL^2 - nR^2 - mR^2)/4; F = the doublet, B = a charge times spin-rotor carrier).

3. An on-site SU(2) acts on both chiralities, so its centre flows to the vector centre z_V = z_L z_R = (-1)^{mL+mR}: on F it is (-1)^F (twisted spins 0 mod 1/2, Z_8 index 0), on B it is 1. The gluing needs the left-mover centre z_L = (-1)^{mL}, which on F is the chiral fermion parity (-1)^{F_L} of the doublet (twisted spin 1/4 = 4/16, Z_8 index 4; as a check, (-1)^{F_L} of one Dirac fermion gives 1/8 = 2/16) and equals the charge half (-1)^{nL} as an operator. So "SU(2) centre = fermion parity" supplies z_V, never z_L.
4. A spin carrier whose gapless sector is one SU(2)_1 per chirality (c = 1) has no fermionic operator: primaries with h in {0, 1/4} give spins in {0, 1/4, 3/4} mod 1. Its fermion parity acts as 1 on the whole gapless sector, so pairing the charge half with the fermion parity of a spin-only carrier never makes the gluing local.

C. Half-filled Hubbard ring (t = 1, U = 4, periodic, N_up = N_dn = L/2, exact diagonalisation).

5. With the charge gapped, a fermion-mode spin carrier is back under Lieb-Schultz-Mattis: the on-site centre (-1)^{n_j} multiplies to the c-number (-1)^N, and the lowest triplet carries momentum pi relative to the singlet ground state, so the infrared spin half is lattice translation, not fermion parity.

D. Construction: carrier = rotor (N, W) (hyperbolic pairing, Q = qV N + qA W) plus fermions (L1, L2, R1, R2) with Gram diag(1, 1, -1, -1), one block per rotor.

6. The locking term ell = (an SU(2)-singlet cell pair of left movers, spin 1) x (rotor vertex N = 1, W = -1, spin -1) is null, primitive, charge-neutral and T3-neutral, for the doublet block (vector charge 1, rotor (qV, qA) = (2, 4)) and the singlet-pair block (vector charge 3, rotor (-2, 4)). The residual ell^perp/ell has a unimodular basis with Gram diag(1, 1, -1, -1): exactly free Weyl modes with L = (2,3) + 2(1,1) and R = (2,1) + 2(1,3), written (SU(2) dimension, U(1) charge). This is the swap content (a, b) = (3, 1), and every residual mode is a fermion.
7. Anomalies: U(1)^2 (sum over L of q^2 minus sum over R) = 0, SU(2) doublets L - R = 0, gravitational 0. The doublet sector alone carries U(1)^2 = 16 = 2 qV qA of its rotor (the locking moves the anomaly from the rotor onto the doublet). No L-R pair has equal SU(2) representation and matching charge, so there is no invariant bilinear mass: the content is jointly chiral, and vector-like under U(1) alone and under SU(2) alone. The ultraviolet doublet mass c_L^dag c_R pairs to -1 with ell, so it is disordered in the locked phase.
8. The gluing generator e^{i pi Q} x (SU(2) centre) equals the singlet fermion parity on every carrier state: the rotor charges are all even, so e^{i pi Q} is 1 on both rotors and no winding parity enters. It is a product of on-site commuting involutions; the anomalous halves z_L and (-1)^{N+W} never appear.
9. The Thorngren-Preskill-Fidkowski rotor disentangler on the two rotors gives W^dag e^{2 pi i b Q} W = e^{2 pi i b Q_anc} exactly when c = sum qV qA = 8 - 8 = 0, and fails for anomalous sets (one rotor alone, or a mismatched partner). The fermions' vector charge is on-site and untouched by W, and SU(2) acts on the fermions only, so [W, SU(2)] = 0 and the gauged U(1) and SU(2) Gauss laws are both on-site and commute. (The vanishing of the Schwinger term with c is stated, not computed.)
10. The rotor half of the locking term is local and constraint-invariant: e^{2 pi i phi_j} and the link shift S_k (n_k -> n_k + s) commute with every Villain constraint and carry exact charges -qV - s qA, so e^{2 pi i phi_j} S_k^{-1} has charge -2 + 4 = 2, cancelled by the cell pair.
11. At the decoupled free point the locking vertex has dimension at least 2 (minimum 2 at rotor radius 1: marginal). An SU(2)-singlet, charge-neutral forward-scattering term between the doublet's charge current and the rotor acts as an O(3,3) boost in the null plane, keeps ell null and the SU(2)_1 currents at h = 1, and lowers the vertex dimension to 2 e^{-2 eta}: relevant.

## Derivation

Items 1 and 2 build the fermion operators by Jordan-Wigner and exponentiate the centres. Items 3 and 4 enumerate vertex vectors in the box [-4, 4]^4 with exact rationals and compute twisted spins and braiding phases. Item 5 diagonalises the Hubbard ring in the S^z = 0 sector, identifies the lowest triplet by S^2 = 2 and compares translation eigenvalues. Items 6 and 7 are integer lattice algebra on the 6-dimensional block lattices. Item 8 enumerates 3^12 = 531441 carrier charge assignments. Items 9 and 10 run the rotor disentangler in exact rationals on 5-site rings with 120 seeded random configurations per set. Item 11 embeds the lattice in R^{3,3}, scans the rotor radius over [0.5, 2] at 301 points and applies the boost at eta = 0.5.

## Finite checks

Exact checks (the runner asserts each):
- One cell: centre relations hold to below 1e-12; chiral SU(2) on 3 cells: centre = (-1) x (-1)^F to below 1e-10.
- Twisted spins mod 1/2 on F: z_V 0, z_L 1/4, charge half 1/4; one Dirac (-1)^{F_L}: 1/8. Braiding phases: z_V = (-1)^F on F; z_L times the charge half = 1 on F; z_V = 1 on B.
- SU(2)_1 spins mod 1: {0, 1/4, 3/4}; mL^2 - mR^2 mod 4 in {0, 1, 3}.
- Hubbard ring: relative translation eigenvalue of the lowest triplet -1 at L = 4 and L = 6; [T, H] = 0 below 1e-12.
- Locking term: null, primitive, neutral, unimodular completion with determinant 1, residual Gram diag(1, 1, -1, -1), for both blocks; L [(2, 3), (2, 3), (1, 1), (1, 1)], R [(2, 1), (2, 1), (1, 3), (1, 3)].
- Anomalies: doublet U(1)^2 16 = rotor 2 qV qA 16; total U(1)^2 and SU(2) doublet count balanced; no invariant bilinear.
- Gluing: identity on all 531441 carrier states.
- Rotor disentangler: (2,4) + (-2,4), c = 0: 0 of 120 failures; (2,4) alone, c = 8: 69 of 120; (2,4) + (-2,2), c = 4: 73 of 120; (-2,4) alone, c = -8: 63 of 120.
- Rotor half of the locking term: charges -6 (s = +1) and 2 (s = -1); commutes with the Villain constraints on all samples.
- Vertex dimension: minimum 2.0000 over the radius scan; boosted (eta = 0.5) 0.7358 = 2 e^{-1}; SU(2) current dimension 1.000.

Finite diagnostic (supplied model, finite diagnostic, no physical identification):
- Hubbard ring triplet gap 0.296 (L = 4) and 0.770 (L = 6). The gap grows from L = 4 to L = 6, so these two sizes are not read as a gap trend; only the translation eigenvalue is asserted.

## Boundary

Supplied: two complex modes per cell for the doublet and per singlet pair; vector charges 1 and 3; two SU(2)-singlet Villain rotors with charges (2, 4) and (-2, 4) and their ancillas; the locking couplings and the forward-scattering term; the chiral SU(2) of item 2; the Hubbard parameters. Cited, not rederived: the Thorngren-Preskill-Fidkowski rotor disentangler (arXiv:2601.04304, inlined), the Haldane null-vector gapping criterion (the lattice algebra is checked here; the flow to the locked phase is cited, not computed), the Else-Nayak argument and Lieb-Schultz-Mattis. Forced, given those: fermion parity as the vector SU(2) centre; the chiral fermion parity, Z_8 index 4, as the half the gluing needs; no fermionic operator in an SU(2)_1 spin carrier; momentum pi of the lowest triplet in the sampled Hubbard rings; the residual swap content, its anomaly cancellation and absence of an invariant bilinear; the on-site gluing on the sampled carrier states; exactness of the disentangler only for the anomaly-free rotor pair; the dimensions of the locking vertex. Not claimed: that the interacting model flows to the locked phase; any 3+1D statement; that rotor matter follows from the register's laws (it is supplied matter beyond one qubit per site); that this is the register's unique construction; a Hubbard statement beyond L = 4 and 6.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above; the rotors are supplied beyond one qubit per site.
- [Candidate-law register](CANDIDATE_LAWS.md): the fermion modes of the update law and the register's open chirality route and doublet gluing. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/fermion_parity_is_the_vector_su2_centre_not_the_chiral_half_and_two_singlet_rotors_give_jointly_chiral_su2_x_u1_with_on_site_gluing_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120` (with an internal alarm at 115 s), runs in about 1 s with about 80 MB resident, prints about 6.0 kB (5961 characters) and ends with `TOTAL: PASS=11 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output apart from the elapsed-time line.
