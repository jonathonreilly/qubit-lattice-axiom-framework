---
claim_id: spinful_majorana_per_direction_cubic_code_emergent_fermion_doublet_carries_spin_half_class_on_all_cubic_rotations_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: five qubits per site of Z^3 carrying ten Majoranas (Jordan-Wigner inside the site): six link Majoranas b_d, one per direction, and four matter Majoranas forming two complex modes c_up, c_dn. Commuting Pauli stabilizers D_v (total parity at v), W_p (product of u_e = b_{v,+a} b_{v+e_a,-a} around p), P_up,v and P_dn,v (matter-mode parities); H = -K sum D - J sum W - mu sum (P_up + P_dn) with J > 0 and K > mu > 0. Exact (L = 6): a commuting group with no -1 and log2 code dimension 3; a single matter Majorana flips exactly D_v and P_up,v, and no operator in a radius-2 ball flips P_up,v alone, a finite control; the dressed P-only endpoint inherits the parent gauge-charge class through D = B_link P_up P_dn; up and down at a site are related by a local operator (one anyon type with two states, degenerate in H); the gauge-dressed matter hops create only the end charges and give Levin-Wen T-junction sign -1 on all 20 triples (a fermion). Rotation action: the link sector as in the Majorana-per-direction note (site permutation plus on-site signed Majorana permutation, a consistent action of O up to fermion parity); on the matter pair the spin rotation U(u) = exp(-i theta n.S), S = c^dag sigma c / 2, for the 48 lifts u in 2O, proved by the exterior-algebra action to be a representation (with floating-point runner checks) with U(-1) equal to the matter parity (a stabilizer), preserving n_up + n_dn and the matter parity, with c_s^dag transforming as the spin-1/2 doublet. With the link sector's clean pair eigenvalue lambda_f = -1 (axis and edge C2), a pair of doublets in a common eigenvector of a C2 lift has eigenvalue lambda_f m^2 = +1 (m = +-i), the relative pair factor is +1. Conditional on a consistent symmetry-localization relation lambda = theta eta for the dressed charge and compatible vacuum reference, eta(C2,C2) = -1 for both C2 classes and the inferred class is w2 on O. Local matter spinors change the pair factor, so the inferred sign is representative-dependent rather than an established fractionalization invariant. The matter-only action is 2O; no full combined-group identification is claimed. The code subspace and empty matter state are invariant; a common invariant link ground vector and full symmetry localization are not constructed here. Not claimed: a framework derivation of the matter content or of the spin action (the matter pair transforms as 1/2 + 0 + 0, not as two soldered qubits), dynamics beyond the commuting H, gap stability, or any physical identification."
upstream_dependencies:
  - majorana_per_direction_cubic_fermion_code_has_one_species_covariant_under_all_cubic_rotations_bounded_theorem_note_2026-10-17
runner: scripts/spinful_majorana_per_direction_cubic_code_emergent_fermion_doublet_2026_10_17.py
---

# A spinful cubic code has a matter doublet with an exact on-site spin action and a conditional spin-class identification

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
- **Its local symmetry representation must have dimension at least two; a doublet suffices.**

Is there a site-local commuting code, with a cube-covariant action and a
symmetric vacuum, whose emergent fermion is such a doublet?

## Result

1. **The code (exact, L = 6).**
   - Five qubits per site carry ten Majoranas: six link Majoranas b_d (one
     per direction) and four matter Majoranas forming c_up and c_dn.
   - Stabilizers:
     - D_v = (-i)^5 product_k chi_(v,k), the total occupation parity at v;
     - W_p, the product of u_e = b_{v,+a} b_{v+e_a,-a} around a plaquette;
     - P_s = -i gamma_(s,1) gamma_(s,2), the matter-mode occupation parities (+Z_s).
   - They form a commuting group with no -1 and log2 code dimension 3, the
     same topological order as the Majorana-per-direction code.
2. **One fermionic anyon with two states (exact).**
   - A single matter Majorana flips exactly D_v and P_up,v. So "one up
     matter fermion" creates a local neutral pair of D and P defects, not an isolated nontrivial charge.
   - No operator within a radius-2 ball flips P_up,v alone (a finite control). The dressed P-only endpoint inherits the parent gauge-charge class by the exact stabilizer identity below.
   - The local bilinear c_up c_dn-type operator converts up to down at a
     site. So up and down are one anyon type with two states.
   - The gauge-dressed hops c_up(v) u_e c_up(w) create only the two end
     charges. Their Levin–Wen T-junction sign is -1 on all 20 triples: a
     fermion.
   - For H = -K sum D - J sum W - mu sum (P_up + P_dn), with K,J,mu positive, compare three explicit charge representatives: the degenerate matter pair at 2mu, the bare D defect at 2K, and the four-plaquette flux-loop representative at 8J. The doublet is cheapest among these three when mu<K and mu<4J; no exhaustive minimum over all excitations is claimed.
3. **The rotation action.**
   - The link sector is acted on as in the Majorana-per-direction note:
     site permutation plus an on-site signed Majorana permutation, a
     consistent action of O up to fermion parity. It preserves the link code subspace and the corresponding D/W constraints; no selected invariant link ground vector is established here.
   - The matter pair is acted on by the spin rotation
     U(u) = exp(-i theta n.S), with S = c^dagger sigma c / 2, for the 48
     lifts u in 2O. The exterior-algebra action proves:
     - U is a representation of 2O;
     - U(-1) is the matter parity, a stabilizer, so the action is an O
       action on the code space;
     - n_up + n_dn and the matter parity are preserved;
     - c_s^dagger transforms as the spin-1/2 doublet;
     - all 18 C2 lifts square to -1 on the doublet.
   - The empty on-site matter state is a spin singlet. The total code subspace is invariant; a selected common invariant link ground vector is not established. The Hamiltonian preserves the sum P_up + P_dn; generic rotations mix the individual matter-parity terms.
4. **Exact relative pair factor; conditional class identification.**
   - In the link sector, the companion note's clean pair test under its
     consistent action gives lambda_f = -1 for an axis C2 and an edge C2.
     The runner recomputes this at L = 8.
   - **Pair states.** A doublet pair is c_e^dagger(x) c_e^dagger(Rx) S_f|vac>.
     Here S_f is the link pair creator and e is an eigenvector of the C2
     lift on the doublet, with eigenvalue m = +-i.
     - Matter operators at different sites commute in this site-local
       encoding, and the matter and link actions factorize.
     - The relative pair transformation factor is lambda_f m^2 = +1. This does not itself construct a common invariant ground vector.
     - The runner evaluates this for all 18 C2 lifts and both
       eigenvectors.
   - **Conditional class.** If consistent symmetry localization for the dressed charge supplies lambda = theta eta with a compatible vacuum reference, exchange sign -1 gives eta(C2,C2)=-1 for both C2 classes. These detect w2 on O. The full localization relation is an explicit unresolved input, as in the repaired companion notes; finite pair signs alone do not prove it.
   - **Consistency with the companion no-go.** A doublet can carry the
     quaternion class on the axis D2, since Q8 acts on two dimensions. So
     this does not contradict the single-state no-go.

## Local dressing prevents an unconditional fractionalization claim

Matter parity conjugates the local creation operator c_s^dagger to its
negative; link parity similarly flips a local link Majorana b_d. These
operators create local excitations, so a nontrivial central action is not
confined to the isolated charge sector. Attaching the local matter spinor
to a clean pair changes its relative C2 factor by m^2=-1. The displayed
pair signs are therefore representative-dependent; the supplied on-site
spin action is not a derivation of an anyon-invariant fractional spin class.
The exact matter-only group is 2O. This does not establish that the full
combined link/matter action has group 2O; no such identification is used.

A link Majorana flips a D defect and four adjacent plaquettes. Combining it
with a bare charge endpoint yields the four-plaquette representative at
energy 8J, which must be included in energy comparisons. The stronger target
is a genuine O action with ordinary local representations and a consistently
localized fractional doublet. That construction remains open.

The incoming author exploration packet, including its fuller group and
vacuum checks, is preserved under
`.claude/science/physics-loops/toe-campaign-20261017/c15_doublet/independent_check/`.
Its finite matrix checks use floating-point tolerances; its reports do not
supply independent landing authority. An invariant stabilizer ray is distinct
from a specified vector transforming with phase +1 under every rotation.

## Stabilizer identity and charged sector

Use the explicit occupation-parity convention P_s = -i gamma_(s,1) gamma_(s,2)
and D = (-i)^5 chi_0 ... chi_9. Then D = B_link P_up P_dn, with
B_link = (-i)^3 b_0 ... b_5. Therefore the stabilizer groups generated by
(D,W,P_up,P_dn) and (B_link,W,P_up,P_dn) are identical. The empty matter
state has P_up=P_dn=+1 and reduces D=+1 to the parent's B_link=+1 sector.
The code ground space is the parent link code tensor the empty matter state;
the L=6 eightfold torus degeneracy is inherited, not removed.
A dressed endpoint with D=+1 and one P_s=-1 has B_link=-1, identifying
its charge with the parent link gauge charge. A single on-site Majorana flips
both D and P_s and is a local neutral composite. The radius-2 linear-system
check is a finite corroboration, not a proof for arbitrary support.

## Exact on-site matter representation

The two-mode Fock space is the exterior algebra of C^2. In particle-number
order its induced action is U(u) = 1 direct-sum u direct-sum det(u).
For u in SU(2), det(u) = 1, so this is 1 direct-sum u direct-sum 1.
Functoriality of the exterior powers gives U(u)U(v) = U(uv) exactly.
U(-I) is +1 on the zero- and two-particle spaces and -1 on the
one-particle space, hence equals matter parity. Number is preserved, and
creation transforms by the defining doublet action. Each C2 lift satisfies
u^2 = -I and therefore squares to -I on the one-particle sector.
The runner's exponential, rounded group enumeration, and allclose tests are
numerical consistency checks of this proof, not exact matrix arithmetic.

## How this bears on the lane (interpretation, not a claim)

- **A supplied spinful matter construction.** The dressed fermionic charge has a two-state matter factor with the exact on-site spin-1/2 action and nearest-neighbour hops. Identifying its full symmetry-fractionalization class as w2 requires the stated localization input. The empty on-site matter state is unique; the L=6 torus ground space has dimension eight. A common invariant link ground vector is not supplied.
- **The price is matter content and a spin action.**
  - Each site carries one matter mode per spin state, coupled to a single
    shared Z2 gauge field.
  - Rotations act on that pair as a spin-1/2 doublet, the representation
    1/2 + 0 + 0 on the two matter qubits. This is not two independently
    soldered qubits, whose representation would be 1/2 x 1/2 = 0 + 1.
  - This construction supplies these modes and their action; whether the framework derives them remains open. No necessity theorem for other constructions is claimed.
- **The spin-charge link.** The full 2pi rotation acts as the matter
  parity, a stabilizer that is +1 on the vacuum and -1 on one matter
  fermion. Rotation by 2pi equals fermion parity on the doublet, the
  on-site representation identity. Its identification with the dressed charge's full fractionalization class remains conditional on localization.
- **The chain of results.**
  - The earlier star-supported searches exclude fermions only within their stated finite search and restricted model scopes.
  - Plaquette rules give fermions, whose spin depends on the rotation
    action.
  - A single-state fermion can never be cube-spin-1/2.
  - A supplied matter doublet gives the on-site spin action and conditional w2 identification for the dressed charge.

## Premises

- **Axioms used.** Lattice (Z^3, unit translations, proper cubic rotations
  about sites).
- **Supplied model.** Five qubits per site, with the stated stabilizers and
  Hamiltonian. Qubit is read as five qubits per site, a declared
  enlargement.
- **Declared choices.**
  - The link action of the companion note.
  - Consistent symmetry localization with lambda = theta eta and a compatible vacuum reference is an unresolved input for the full class identification.
  - The spin-1/2 action on the matter pair, which is a non-Clifford
    on-site unitary for the C3 elements.

## Relation to prior work

- Majorana-fermion constructions with spinful matter coupled to a Z2 gauge
  field are known:
  - the Gamma-matrix model of Yao, Zhang and Kivelson, PRL 102, 217202 (2009);
  - the SU(2)-symmetric model of Yao and Lee, arXiv:1010.3724;
  - "orthogonal metals" of Nandkishore, Metlitski and Senthil, PRB 86,
    045128 (2012);
  - the Γ-matrix models of Wu, Arovas and Hung, PRB 79, 134427 (2009).
- Generalized superfast encoding: Setia, Bravyi, Mezzacapo and Whitfield,
  PRR 1, 033033 (2019).
- **New here.**
  - The exact checks in a site-local cubic code.
  - The cube-covariance accounting.
  - The relative pair calculation and conditional w2 identification on O.
  - The placement of this construction as the minimal escape from the
    one-dimensional-representation obstruction; minimality of the qubit cost is not proved.

## No-Go Discipline Gate

- **N1 — routes around the claim.** A single on-site spinor has no invariant pure state. This is not a general Lieb–Schultz–Mattis theorem or an exclusion of entangled ground states. Other matter contents, gauge groups, and dynamics are not treated.
- **N2/N3 — scope.** One code and on-site action; exact finite-code/statistics and matter-representation results, conditional class on O.
- **N4 — inputs.**
  - Exact Pauli algebra at L = 6.
  - Exact exterior-algebra proof for the matter action; floating-point 4x4 checks in the runner.
  - The link-sector pair test at L = 8 (recomputed, from the companion
    note).
  - The relative composition step uses factorization of the matter and link actions and site-local commutation. Full class identification additionally assumes the stated unresolved localization relation.
- **N5 — wording.** "Spin-1/2 class" means the conditional inference eta = w2 on O under the stated localization input; full localization is not proved. The doublet's two states are exactly degenerate in the stated H.
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

Expected: `TOTAL: PASS=12 FAIL=0`; runtime depends on the host (declared cap 1800 seconds).

## Load-bearing sources

- [Majorana-per-direction note](MAJORANA_PER_DIRECTION_CUBIC_FERMION_CODE_HAS_ONE_SPECIES_COVARIANT_UNDER_ALL_CUBIC_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
