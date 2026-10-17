---
claim_id: spinful_majorana_per_direction_cubic_code_emergent_fermion_doublet_carries_spin_half_class_on_all_cubic_rotations_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: five qubits per site of Z^3 carrying ten Majoranas (Jordan-Wigner inside the site): six link Majoranas b_d, one per direction, and four matter Majoranas forming two complex modes c_up, c_dn. Commuting Pauli stabilizers D_v (total parity at v), W_p (product of u_e = b_{v,+a} b_{v+e_a,-a} around p), P_up,v and P_dn,v (matter-mode parities); H = -K sum D - J sum W - mu sum (P_up + P_dn) with K > mu > 0. Exact (L = 6): a commuting group with no -1 and log2 code dimension 3; a single matter Majorana flips exactly D_v and P_up,v, and no operator in a radius-2 ball flips P_up,v alone, so the matter excitation is the nontrivial gauge charge; up and down at a site are related by a local operator (one anyon type with two states, degenerate in H); the gauge-dressed matter hops create only the end charges and give Levin-Wen T-junction sign -1 on all 20 triples (a fermion). Rotation action: the link sector as in the Majorana-per-direction note (site permutation plus on-site signed Majorana permutation, a consistent action of O up to fermion parity); on the matter pair the spin rotation U(u) = exp(-i theta n.S), S = c^dag sigma c / 2, for the 48 lifts u in 2O, verified exactly to be a representation with U(-1) equal to the matter parity (a stabilizer), preserving n_up + n_dn and the matter parity, with c_s^dag transforming as the spin-1/2 doublet. With the link sector's clean pair eigenvalue lambda_f = -1 (axis and edge C2), a pair of doublets in a common eigenvector of a C2 lift has eigenvalue lambda_f m^2 = +1 (m = +-i), so eta(C2, C2) = -1 for both C2 classes: the doublet carries the spin-1/2 class w2 on all of O, over a vacuum (no matter, link stabilizer state) that is invariant under the action. Not claimed: a framework derivation of the matter content or of the spin action (the matter pair transforms as 1/2 + 0 + 0, not as two soldered qubits), dynamics beyond the commuting H, gap stability, or any physical identification."
upstream_dependencies:
  - majorana_per_direction_cubic_fermion_code_has_one_species_covariant_under_all_cubic_rotations_bounded_theorem_note_2026-10-17
runner: scripts/spinful_majorana_per_direction_cubic_code_emergent_fermion_doublet_2026_10_17.py
---

# A spinful Majorana-per-direction cubic code has an emergent fermion doublet with the spin-1/2 class on all cube rotations

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact for the stated model. Nothing
is adopted.

## Question

The companion notes reached two conclusions.
- **A single-state fermion cannot be spin-1/2 under all 24 cube rotations.**
  A one-dimensional local action with fermion parity acting as -1 would be
  a character of the binary octahedral group 2O that sends -1 to -1. None
  exists, because -1 is a commutator.
- **So a cube-symmetric spin-1/2 fermion must be a doublet.**

Is there a site-local commuting code, with a cube-covariant action and a
symmetric vacuum, whose emergent fermion is such a doublet?

## Result

1. **The code (exact, L = 6).**
   - Five qubits per site carry ten Majoranas: six link Majoranas b_d (one
     per direction) and four matter Majoranas forming c_up and c_dn.
   - Stabilizers:
     - D_v, the total parity at v;
     - W_p, the product of u_e = b_{v,+a} b_{v+e_a,-a} around a plaquette;
     - P_up and P_dn, the matter-mode parities.
   - They form a commuting group with no -1 and log2 code dimension 3, the
     same topological order as the Majorana-per-direction code.
2. **One fermionic anyon with two states (exact).**
   - A single matter Majorana flips exactly D_v and P_up,v. So "one up
     matter fermion" is in the sector of the gauge charge.
   - No operator within a radius-2 ball flips P_up,v alone. So the charge
     is nontrivial.
   - The local bilinear c_up c_dn-type operator converts up to down at a
     site. So up and down are one anyon type with two states.
   - The gauge-dressed hops c_up(v) u_e c_up(w) create only the two end
     charges. Their Levin–Wen T-junction sign is -1 on all 20 triples: a
     fermion.
   - With H = -K sum D - J sum W - mu sum (P_up + P_dn) and K > mu > 0,
     the cheapest charged excitations are the degenerate pair (up, down),
     at energy 2 mu. The bare gauge charge costs 2K.
3. **The rotation action.**
   - The link sector is acted on as in the Majorana-per-direction note:
     site permutation plus an on-site signed Majorana permutation, a
     consistent action of O up to fermion parity. It maps D, W and the
     link vacuum to themselves.
   - The matter pair is acted on by the spin rotation
     U(u) = exp(-i theta n.S), with S = c^dagger sigma c / 2, for the 48
     lifts u in 2O. Verified exactly:
     - U is a representation of 2O;
     - U(-1) is the matter parity, a stabilizer, so the action is an O
       action on the code space;
     - n_up + n_dn and the matter parity are preserved;
     - c_s^dagger transforms as the spin-1/2 doublet;
     - all 18 C2 lifts square to -1 on the doublet.
   - The matter vacuum (no matter fermion) is a spin singlet. So the vacuum
     is invariant, and the Hamiltonian is invariant term by term.
4. **The class: spin-1/2 on all of O (exact composition).**
   - In the link sector, the companion note's clean pair test under its
     consistent action gives lambda_f = -1 for an axis C2 and an edge C2.
     The runner recomputes this at L = 8.
   - **Pair states.** A doublet pair is c_e^dagger(x) c_e^dagger(Rx) S_f|vac>.
     Here S_f is the link pair creator and e is an eigenvector of the C2
     lift on the doublet, with eigenvalue m = +-i.
     - Matter operators at different sites commute in this site-local
       encoding, and the matter and link actions factorize.
     - So the pair eigenvalue is lambda_f m^2 = +1.
     - The runner evaluates this for all 18 C2 lifts and both
       eigenvectors.
   - **The class.** With exchange sign -1, eta(C2, C2) = -1 for every C2 of
     O. H^2(O; Z2) is detected by the axis and edge C2 classes, so the
     doublet carries w2, the spin-1/2 class, on the full cube group.
   - **Consistency with the companion no-go.** A doublet can carry the
     quaternion class on the axis D2, since Q8 acts on two dimensions. So
     this does not contradict the single-state no-go.

## How this bears on the lane (interpretation, not a claim)

- **An electron-like emergent fermion.** It is a Z2-charged fermion that
  comes as a spin-1/2 doublet, transforms with the spin-1/2 class under all
  24 cube rotations, moves by nearest-neighbour hops, and sits over a
  symmetric, unique vacuum.
- **The price is matter content and a spin action.**
  - Each site carries one matter mode per spin state, coupled to a single
    shared Z2 gauge field.
  - Rotations act on that pair as a spin-1/2 doublet, the representation
    1/2 + 0 + 0 on the two matter qubits. This is not two independently
    soldered qubits, whose representation would be 1/2 x 1/2 = 0 + 1.
  - So a framework that wants an emergent electron must contain, or
    derive, a site degree of freedom that rotates this way.
- **The spin-charge link.** The full 2pi rotation acts as the matter
  parity, a stabilizer that is +1 on the vacuum and -1 on one matter
  fermion. Rotation by 2pi equals fermion parity on the doublet, the
  lattice form of spin-statistics for this particle.
- **The chain of results.**
  - Star-supported rules give no fermion.
  - Plaquette rules give fermions, whose spin depends on the rotation
    action.
  - A single-state fermion can never be cube-spin-1/2.
  - A matter doublet coupled to one gauge field gives it.

## Premises

- **Axioms used.** Lattice (Z^3, unit translations, proper cubic rotations
  about sites).
- **Supplied model.** Five qubits per site, with the stated stabilizers and
  Hamiltonian. Qubit is read as five qubits per site, a declared
  enlargement.
- **Declared choices.**
  - The link action of the companion note.
  - The spin-1/2 action on the matter pair, which is a non-Clifford
    on-site unitary for the C3 elements.

## Relation to prior work

- Majorana-fermion constructions with spinful matter coupled to a Z2 gauge
  field are known:
  - the SU(2)-invariant exactly solvable spin model of Yao, Zhang and
    Kivelson, PRL 102, 217202 (2009);
  - "orthogonal metals" of Nandkishore, Metlitski and Senthil, PRB 86,
    045128 (2012);
  - the Γ-matrix models of Wu, Arovas and Hung, PRB 79, 134427 (2009).
- Generalized superfast encoding: Setia, Bravyi, Mezzacapo and Whitfield,
  PRR 1, 033033 (2019).
- **New here.**
  - The exact checks in a site-local cubic code.
  - The cube-covariance accounting.
  - The class computation, which yields w2 on all of O.
  - The placement of this construction as the minimal escape from the
    single-state no-go.

## No-Go Discipline Gate

- **N1 — routes around the claim.** Other matter contents, such as a single
  spin-1/2 qubit per site, run into a Lieb–Schultz–Mattis-type obstruction
  to a symmetric product vacuum. Other gauge groups and dynamics are not
  treated.
- **N2/N3 — scope.** One code, one action, the class on O.
- **N4 — inputs.**
  - Exact Pauli algebra at L = 6.
  - Exact 4x4 matrix algebra for the matter action.
  - The link-sector pair test at L = 8 (recomputed, from the companion
    note).
  - The composition step uses factorization of the matter and link
    actions and site-local commutation of matter operators.
- **N5 — wording.** "Spin-1/2 class" means eta = w2 on O for the stated
  action. The doublet's two states are exactly degenerate in the stated H.
- **N6/N7 — strongest objection.** The spin action on the matter pair is
  put in by hand, as is the matter content. The note claims realizability,
  not derivation.
- **N8 — earlier claims.** Consistent with the single-state no-go of the
  Majorana-per-direction note, which this construction evades by carrying
  two states.

## Verification

```bash
python3 scripts/spinful_majorana_per_direction_cubic_code_emergent_fermion_doublet_2026_10_17.py
```

Expected: `TOTAL: PASS=11 FAIL=0` (under a minute).

## Load-bearing sources

- [Majorana-per-direction note](MAJORANA_PER_DIRECTION_CUBIC_FERMION_CODE_HAS_ONE_SPECIES_COVARIANT_UNDER_ALL_CUBIC_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
