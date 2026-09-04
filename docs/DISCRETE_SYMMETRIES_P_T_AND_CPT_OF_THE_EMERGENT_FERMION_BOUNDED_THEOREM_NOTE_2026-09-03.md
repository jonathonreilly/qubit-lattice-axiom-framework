---
claim_id: discrete_symmetries_p_t_cpt_emergent_fermion
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3, carrying one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, with the Kawamoto-Smit link signs eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}, for the ONE DECLARED Hamiltonian H(t,m) = -t sum_<ij> eta_ij T_ij - (m/2) sum_v eps_v B_v whose coefficients t and m are supplied and are fixed by nothing quoted here, and on the named finite geometries only -- the open 2x2x2 coarse cube and the 4^3 coarse torus: EVERY PARITY STATEMENT BELOW IS CONDITIONAL ON THE LAW CARRYING IMPROPER POINT ELEMENTS, which the Lattice axiom does not name; it names 'nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site'. Conditional on the improper map being applied: (T1) the direction order -x < -y < -z < +x < +y < +z is carried cyclically by three under inversion, so the bare site relabelling V_P does not send A_ij to +-A_{P(i)P(j)}; the exact discrepancy is a pure-Z factor depending only on the image edge -- the three positive-direction edges at its upper endpoint together with the three negative-direction edges at its lower endpoint, degree 6 on the torus -- and no product of Z's can supply it, since a Z-Pauli only signs A_e whose X-support is its own edge; that adjacency is symmetric and loop-free, so U_P = G_g D_CZ V_P with G_g a Z2 gauge factor, D_CZ a diagonal Clifford CZ network and V_P the relabelling, satisfies U_P A_ij U_P^-1 = sigma_ij A_{P(i)P(j)} with sigma_ij = eta_ij eta_{P(i)P(j)}, U_P B_v U_P^-1 = +B_{P(v)} with no sign at any corner, U_P S_f U_P^-1 = +S_{P(f)} on every face so the pi-flux code space is preserved, and U_P J_ij U_P^-1 = o_ij J_{P(i)P(j)} with o the image-bond orientation, both inversions reversing all 192 torus bonds. (T2) For inversion about a corner sigma_ij = +1 on every one of the 192 bonds, the sign field eta is carried to itself bond by bond with 0 of 192 differing and 0 flipped corners in the one-particle gauge -- not merely gauge-equivalent -- and H(t,m) is exactly P-symmetric for every t and every m; inversion about a cube centre and the three mid-plane reflections send m -> -m, carrying -1 on 64 and 128 bonds respectively; the uniform rule is eps_{P(v)} = (-1)^{sum of the shift components} eps_v, depending on the shift parity alone and never on the rotation or reflection part, and U_P H_hop U_P^-1 = H_hop exactly for every map on both geometries. (T3) Time reversal is T = Z_E K with Z_E = prod_e Z_e = prod over the corners with eps_v = -1 of B_v, the unique pure-Z choice because A_ij has X-support exactly its own edge and the bond-to-edge map is onto; A_ij -> -A_ij, B_v -> +B_v, T_ij -> +T_ij, S_f -> +S_f, J_ij -> -J_ij, Q -> +Q, and H(t,m) is invariant for every t and every m with no m -> -m; T^2 = +1 exactly on the 4096-dimensional cube space, on its 128-dimensional pi-flux code space and on the Dirac point. (T4) [numerical, 1e-12] on the 4^3 torus the one-particle operator is real symmetric with 8 zero modes gapped to exactly 2m; the symmetry class is BDI with T^2 = +1 and C^2 = +1 and chiral S = CT = Eps; in the canonical cell basis inversion about a corner is represented by exactly the same 8x8 matrix as the staggered mass, eps = Z1 Z2 Z3, the emergent gamma^0, anticommuting with the chirality X = -(Y x X x Y); CPT built from corner inversion is +1 times the identity on the Dirac-point subspace; a Kramers sign appears only as (PT)^2 = -1 for cube-centre inversion and (CP)^2 = -1 for the x = 1/2 reflection, and only at m = 0. (T5) The exact transformation table on the 4^3 torus for the rows B_v, n_v, A_ij, S_f, T_ij, H_hop, H_m, H(t,m), J_ij, Q, eps_v against the columns C, P about a corner, P about a cube centre, the x = 1/2 mid-plane reflection, T, CP, CT, PT and CPT: every entry is a sign on the same operator at the image index, B_v, S_f, H_hop, H_m, Q and eps_v are uniform in every column, and in the odd-shift columns A_ij, T_ij and J_ij carry the bond-dependent pattern sigma_ij = eta_ij eta_{P(i)P(j)} rather than a uniform sign; B_v, Q and H_m are pure Z hence record-diagonal, while A_ij, S_f, T_ij and J_ij have identically zero record-basis diagonal on both geometries. The values of t and m are supplied data; no interaction, no chiral sector, no gauge field beyond the encoding's own Z2 structure and no continuum limit is treated. Nothing here is derived from any axiom, no axiom is amended, no status is set, no hypothesis is adopted, and no registry entry is created; whether an improper element belongs in the Lattice axiom's symmetry list remains an axiom-level question for the owner."
upstream_dependencies: []
runner: scripts/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.py
---

# Discrete symmetries `P`, `T` and `CPT` of the emergent fermion

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.py`](../scripts/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.txt`](../logs/runner-cache/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.txt)
**Parents:** none load-bearing. Every premise used below is declared in this note; the context notes are plain-text pointers listed in "Imports and authority".

**The conditional, stated first.** The Lattice axiom names *proper* cubic rotations and nothing improper. Every parity statement in this note is therefore of the form "if the improper point element is applied, the encoded algebra does *this*". Landing the note does not license adding an improper element to the axiom; it supplies exactly the evidence the owner would need to decide whether the law *could* carry one at no cost. Whether it should is an axiom-level question for the owner, and this note does not decide it.

PR #7892 built charge conjugation `C` and named `T` and `CPT` as an interface it did not compute. This note computes them, and computes parity alongside: which of `P`, `T` and `CPT` the emergent matter carries exactly, at what mass, and which of the resulting signs the records register. `T` is exact at every mass with `T^2 = +1`; parity about a lattice corner is exact at every mass, costing the encoding a Clifford network but no obstruction; and on the low-energy doublet the parity operator and the mass term are literally the same matrix.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems about one declared Hamiltonian on the coarse-lattice emergent fermion: the Clifford correction that realises an improper point element on the superfast encoding, the shift-parity rule governing the mass sign, the time-reversal operator and its full table, the Dirac-point representations, and the complete C/P/T transformation table with its record reading. The symplectic Pauli statements are exact Gaussian-rational arithmetic on F2 supports with Z4 phases; the tagged numerical items are floating-point cross-checks at the stated tolerance. Every parity statement is conditional on the law carrying improper point elements, which the Lattice axiom does not name."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the axiom-level question this note does not decide: whether an improper point element belongs in the Lattice axiom's symmetry list."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. Groups `A`, `B`, `C` and `E` are exact -- Gaussian-rational coefficients on
symplectic Pauli monomials, `F2` supports and `Z4` phases, complete sweeps over both geometries -- and the items tagged `[numerical]` are floating-point cross-checks at the stated
tolerance.

1. `T1` (`A`). Parity needs a Clifford network on the encoding, and what that network is.
2. `T2` (`B`). Inversion about a corner is exact at every mass; the shift-parity rule for the mass sign.
3. `T3` (`C`). Time reversal `T = Z_E K`, its full table, and `T^2 = +1`.
4. `T4` (`D`). The Dirac point: the mass is the parity operator, and `CPT` is the identity there.
5. `T5` (`E`). The full transformation table, and which of its rows the records register.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the Altland-Zirnbauer class labels, and the `CZ`-network form of a
diagonal Clifford are standard methodology; every object is redeclared here and the runner recomputes every statement. No fitted number and no framework premise enters any proof.
Non-load-bearing pointers, carrying no grade and no weight:

- `CHARGE_CONJUGATION_AND_THE_CONSERVED_U1_CURRENT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7892): `C = Z_E C_0`, the bond current `J_ij`, the charge `Q`,
  and the table format used here. Its named interface "`T` and `CPT`" is what this note computes.
- `A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7890): `H(t,m)`, the grading `eps_v`, and its `T2` on
  translations and the 24 proper rotations, of which `T2` here is the improper analogue.
- `LORENTZ_AT_THE_DIRAC_POINT_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7888): the 8-fold Dirac point and the `2x2x2` cell basis reused in `T4`.
- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844) and
  `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): the encoding, the sign field, the superlattice role
  pattern, and the coarse sublattice `2Z^3`.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting". No grade of theirs is cited and no hypothesis is adopted.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and
proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has algebraic presentation `M_2(C)`".
**Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations", and "For each site, the probability
distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions" -- the law supplies the odds. **Record**: "Records form", "a record locks exactly
one admissible local possibility", "records are permanent", "Only records are readable", and "A readout value is determined by record content alone."

That symmetry clause, and the identical clause in Admissibility, name **"proper cubic rotations"** and no improper element; grepping the axioms file for
`reflect|inversion|improper|parity|O_h|octahedral|point group` returns nothing. So every `P` statement below is conditional, as stated at the top.

The lattice is physical. Everything below reads the Kawamoto-Smit sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, on the superlattice role pattern's
sublattice. Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the sign field on it, the superfast
encoding with its face stabilizers, the encoded hop, the grading `eps_v`, and `H(t,m)` with its supplied coefficients. `P1` (`A`) is the Clifford correction `U_P` and its action; `P2`
(`B`) the shift-parity rule; `P3` (`C`) time reversal; `P4` (`D`) the Dirac-point representations; `P5` (`E`) the full table and the record reading. `P2` uses `P1`; `P3` uses `P0` only;
`P4` uses `P0` and the one-particle reduction; `P5` uses `P1`, `P2`, `P3` and `C`, rebuilt here. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The **sign field** of the
coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`. The **encoding** is the Bravyi-Kitaev superfast encoding on the coarse lattice, code
qubits on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`.

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_v  = the product of the six Z's at corner v = I - 2 n_v,   S_f = the ordered product of the four A's around a coarse face f
n_v  = (I - B_v)/2,   T_ij = (i/2) A_ij (B_i - B_j),   eps_v = (-1)^{v_1+v_2+v_3},   Q = sum_v (n_v - 1/2) = -(1/2) sum_v B_v
H(t,m) = -t sum_<ij> eta_ij T_ij - (m/2) sum_v eps_v B_v          THE DECLARED LAW; t and m are supplied
J_ij = eta_ij (t/2) A_ij (I - B_i B_j)                            the bond current of PR #7892
C    = Z_E C_0,  C_0 = prod over a perfect matching of A_ij,  Z_E = prod over all edges of Z_e     conjugation, from PR #7892
P: v -> M v + c    a signed permutation M and an integer shift c; improper when det M = -1
V_P  = the bare relabelling of the code qubits induced by P        D_CZ = prod_{{e,f} in N} CZ_ef
G_g  = prod_{v in S} B_v, the Z2 gauge factor                      U_P  = G_g . D_CZ . V_P          THE PARITY OPERATOR
T    = Z_E . K,  K complex conjugation in the record basis         THE TIME-REVERSAL OPERATOR
```

The **star** of a corner is the set of edge sites incident to it, six in the bulk. A **record pattern** is one assignment of a value to every edge record; the record basis is the joint
eigenbasis of the `Z_e`. An operator is **record-diagonal** when it is diagonal in that basis; one whose every Pauli monomial carries `X`-support has identically zero record-basis
diagonal and registers only through correlations. A **cut** is an edge set `XOR_{v in S} star(v)`. The two geometries are the **open `2x2x2` coarse cube** (8 corners, 12 code qubits,
4096-dimensional, 6 faces, 128-dimensional code space) and the **`4^3` coarse torus** (64 corners, 192 code qubits, 192 bonds, 192 faces).

## Theorem 1 -- parity needs a Clifford network on the encoding

**Conclusion.** Conditional on the improper element being applied: (1) `4` of the `10` point maps tested are automorphisms of the open cube -- the corner-centred ones leave the block --
and all `10` are automorphisms of the torus; each induces a permutation of the code qubits. (2) Inversion carries the direction order `-x < -y < -z < +x < +y < +z` cyclically by three,
so the bare relabelling `V_P` does **not** send `A_ij` to `+-A_{P(i)P(j)}`: the exact discrepancy is a **pure `Z`** factor, nontrivial on all `192` torus bonds. (3) No product of `Z`'s
can absorb it: a `Z`-Pauli only supplies a **sign** to `A_e`, whose `X`-support is its own edge. The factor depends only on the **image edge** and is exactly the three
positive-direction edges at its upper endpoint together with the three negative-direction edges at its lower endpoint -- degree `6` on the torus, truncated at the open boundary. (4)
That adjacency is symmetric and loop-free for every map and geometry, so it is realised by the diagonal Clifford `D_CZ = prod CZ_ef`. (5) Hence `U_P = G_g D_CZ V_P` satisfies
`U_P A_ij U_P^-1 = sigma_ij A_{P(i)P(j)}` with `sigma_ij = eta_ij eta_{P(i)P(j)}` on every bond, `G_g`'s `Z`-mask always solving as a cut -- `|S| = 32` for both torus inversions -- so
`G_g` is a `Z2` gauge factor, diagonal in the record basis. (6) `U_P B_v U_P^-1 = +B_{P(v)}` with no sign at any corner, so `n_v -> n_{P(v)}` and `Q -> +Q`; and
`U_P S_f U_P^-1 = +S_{P(f)}` on every face, zero sign flips, so `U_P` is legal in the `pi`-flux code space. (7) `U_P J_ij U_P^-1 = o_ij J_{P(i)P(j)}` with `o` the image-bond
orientation: both inversions reverse all `192` bonds and the `x`-reflections only the `64` `x`-bonds, so the current is a polar vector.

**Proof.** Items 1 and 2 are `F2` support arithmetic on the induced edge permutation, with the residual monomial's `X`-part and phase parity read off directly. Item 3's necessity is the
fact that conjugation by a `Z`-Pauli changes no `Z`-tail; the neighbourhood claim is checked edge by edge against the closed form. Item 4 is a symmetry and loop test. Item 5 conjugates
each `A_ij` by the assembled Clifford, compares monomials exactly, then solves the mask over `F2` against the corner stars. Items 6 and 7 are the same comparison on the corner
operators, face loops and bond currents. All exact.

**Reading, not theorem.** The encoding fixes an order on the six directions at each site, and that order is not itself symmetric under a mirror. Repairing the mismatch is not a matter
of signs: it takes a fixed pattern of two-record couplings, one per pair of neighbouring edges. Once that pattern is in place, the mirror is a legal operation of the code -- no face
constraint is disturbed, and no record is ever flipped, only relabelled.

## Theorem 2 -- inversion about a corner, and the shift-parity rule

**Conclusion.** Conditional as above: (1) For inversion about a **corner**, `sigma_ij = +1` on every one of the `192` torus bonds, while inversion about a **cube centre** carries `-1`
on `64` and the `x = 1/2` reflection on `128` -- a bond-dependent pattern, not a uniform sign. (2) The sign field is carried to **itself** bond by bond by corner inversion, `0` of `192`
differing, and with `0` flipped corners in the one-particle gauge: it is not merely gauge-equivalent to its image. The odd-shift maps differ on `64` and `128` bonds and need a genuine
gauge factor, `32` of the `64` corners at `g_v = -1`. (3) `U_P H_hop U_P^-1 = H_hop` **exactly** for every map on both geometries. (4)
`eps_{P(v)} = (-1)^{sum of the shift components} eps_v` at every corner: the rule depends only on the shift parity, never on the rotation or reflection part, because a signed
permutation preserves `v_1 + v_2 + v_3 mod 2`. (5) Hence `U_P H_m U_P^-1 = (-1)^{sum c} H_m`: `H(t,m)` is **exactly** `P`-symmetric at every `t` and `m` under corner inversion and the
corner-plane reflections, and `P`-symmetric only with `m -> -m` under cube-centre inversion and the mid-plane reflections.

**Proof.** Item 1 reads the signs produced by Theorem 1's construction. Item 2 compares `eta` bond by bond under the induced edge map, and independently solves the one-particle gauge by
propagation over the torus. Item 3 conjugates the kinetic sum, item 5 the mass term. Item 4 is the parity of a signed permutation on the coordinate sum. All exact.

**Reading, not theorem.** There are two kinds of mirror on this lattice: those centred on a corner and those centred half a cell away. The first kind leaves the sign field alone, bond
for bond, and leaves the whole law alone at any mass. The second kind reverses the mass and nothing else. Which kind a given mirror is depends on one bit -- the parity of its shift --
and on nothing else about it, which is the same bit that governs the translations of PR #7890.

## Theorem 3 -- time reversal, exactly, at every mass

**Conclusion.** (1) Every `A_ij` is a **real** Pauli, so `K A_ij K = +A_ij`, `K T_ij K = -T_ij` and `K H_hop K = -H_hop`: bare conjugation is an *anti*-symmetry of the hop, not a
symmetry. (2) `Z_E = prod_e Z_e = prod over the corners with eps_v = -1 of B_v` as Pauli operators, an exact identity because the lattice is bipartite and every edge is covered once;
and it is the **unique** pure-`Z` repair, since `A_ij` has `X`-support exactly its own edge and the bond-to-edge map is onto. (3) `T = Z_E K` acts as `A_ij -> -A_ij`, `B_v -> +B_v` --
the records are `T`-even -- `n_v -> n_v`, `T_ij -> +T_ij`, and `S_f -> +S_f` on every face, so the `pi`-flux code space is `T`-invariant. (4) `T H(t,m) T^-1 = H(t,m)` for **every** `t`
and **every** `m`, with no `m -> -m`. (5) `T J_ij T^-1 = -J_ij` on every bond, so the conserved bond current is `T`-odd, while `T Q T^-1 = +Q`. (6) `T^2 = +1` exactly: `Z_E` is a real
diagonal involution on the `4096`-dimensional cube space, so `T^2 = Z_E Z_E^* = +I`; the code projector is real of rank exactly `128` and commutes with `Z_E`, so `T` carries the code
space onto itself; and `T H T^-1 = Z_E H^* Z_E = H` at residual `0` for `m = 0, 0.7`. `[numerical, 1e-12]` for item 6.

**Proof.** Item 1 is the reality of each monomial's coefficient after the phase is folded in. Item 2 is `F2` support arithmetic; the `X`-support condition is one linear equation per
edge. Items 3 to 5 conjugate Pauli sums by `Z_E` and conjugate coefficients, key by key. Item 6 builds the `4096`-dimensional sparse algebra, projects onto the joint `+1` eigenspace of
the six face stabilizers, and compares `Z_E H^* Z_E` with `H`.

**Reading, not theorem.** Running the law backwards is not simply conjugating the numbers: doing that alone reverses the hopping term. The repair is a single fixed pattern of signs over
the records -- the same object that distinguishes the two sublattices -- and once it is included, the law reads the same backwards as forwards, at any mass. Doing it twice returns
exactly what one started with, so nothing here forces the doubling that a spin-half particle would show.

## Theorem 4 -- the Dirac point: the mass is the parity operator

**Conclusion.** `[numerical, 1e-12]` on the `4^3` torus throughout. (1) The one-particle operator is real symmetric with `{h_0, Eps} = 0`, has exactly `8` zero modes, and the staggered
mass gaps them to exactly `2m` at `m = 0.2, 0.5, 1.0`. (2) The cell basis `psi_s(v) = (-1)^{sum(v div 2)} delta_{v mod 2, s}` is an orthonormal real basis of the kernel and the
`q = (pi,pi,pi)` cell block of PR #7888, with velocities `M_a = -Gamma_a`. (3) The chirality `X = -i m_1 m_2 m_3 = -(Y x X x Y)` is a hermitian involution of spectrum `{+1 x4, -1 x4}`
-- two right- and two left-handed Weyl doublets -- and the mass restricts to exactly `eps = Z1 Z2 Z3`, anticommuting with it: a chirality-mixing Dirac mass. (4) `U h_0 U^T = h_0` and
`U Eps U^T = (-1)^{sum c} Eps` at residual `0` for both inversions, both `x`-reflections and the proper `C4`, with `0` flipped corners at a corner and `32` at a cube centre. (5)
**Inversion about a corner is represented on the Dirac point by exactly the same `8x8` matrix as the staggered mass**, `eps = Z1 Z2 Z3` -- the emergent `gamma^0`, with
`H_m|_D = m gamma^0` -- and it anticommutes with the chirality, exchanging the two handednesses. (6) The class is `BDI`: `T = K` restricted is the identity times `K` with `T^2 = +1`,
`C = Eps.K` is `eps` times `K` with `C^2 = +1`, chiral `S = CT = Eps`. (7) `CPT` built from corner inversion is `+1` times the **identity** on the Dirac-point subspace; no other
improper choice tested gives a scalar. (8) A Kramers sign appears only in the half-cell-shifted combinations and only at `m = 0`: `(PT)^2 = -1` for cube-centre inversion and
`(CP)^2 = -1` for the `x = 1/2` reflection, against `+1` for both at a corner -- and those products send `m -> -m`, so they are not symmetries at `m =/= 0`.

**Proof.** Item 1 diagonalises the `64x64` real symmetric operator. Item 2 verifies the closed-form kernel vectors and evaluates the cell Bloch matrix at `q = (pi,pi,pi)`. Items 3 and 5
restrict the relevant `64x64` operators to the kernel and compare with explicit Pauli words on the three cell qubits. Item 4 builds the one-particle representation by propagating the
gauge over the torus. Items 6 to 8 use `(A K)(B K) = A B^*` and the phase-invariant squares.

**Reading, not theorem.** At low energy the lattice carries two doublets, one of each handedness, and a mass term that exchanges them. The mirror through a corner turns out to be that
same exchange -- the same matrix, with no fitting -- which is the lattice form of the textbook relation between the parity operator and the mass. Combining the three operations,
exchange of matter with its absence, mirror and time reversal, leaves the doublet exactly as it was.

## Theorem 5 -- the full table, and what the records register

**Conclusion.** Exact on the `4^3` torus, for the rows `B_v, n_v, A_ij, S_f, T_ij, H_hop, H_m, H(t,m), J_ij, Q, eps_v` and the columns `C`, `P` about a corner, `P` about a cube centre,
the `x = 1/2` mid-plane reflection, `T`, `CP`, `CT`, `PT` and `CPT` (the products using corner inversion):

```text
        C     Pcor  Pcen  Ref   T     CP    CT    PT    CPT
B_v     -1    +1    +1    +1    +1    -1    -1    +1    -1
n_v     1-nP  n_P   n_P   n_P   n_P   1-nP  1-nP  n_P   1-nP
A_ij    -1    +1    e.e'  e.e'  -1    -1    +1    -1    +1
S_f     +1    +1    +1    +1    +1    +1    +1    +1    +1
T_ij    +1    +1    e.e'  e.e'  +1    +1    +1    +1    +1
H_hop   +1    +1    +1    +1    +1    +1    +1    +1    +1
H_m     -1    +1    -1    -1    +1    -1    -1    +1    -1
H(t,m)  -m    inv   -m    -m    inv   -m    -m    inv   -m
J_ij    -1    +1    e.e'  e.e'  -1    -1    +1    -1    +1
Q       -1    +1    +1    +1    +1    -1    -1    +1    -1
eps_v   +1    +1    -1    -1    +1    +1    +1    +1    +1
```

(1) Every entry is a sign on the **same** operator at the image index -- `B_v -> s B_{P(v)}`, `A_ij -> s A_{P(i)P(j)}`, `S_f -> s S_{P(f)}`, `T_ij -> s T_{P(i)P(j)}`,
`J_ij -> s J_{P(i)P(j)}` at the ordered image bond -- and no entry is lost; `B_v`, `S_f`, `H_hop`, `H_m`, `Q` and `eps_v` are uniform in every column. (2) In the two **odd-shift**
columns the rows `A_ij`, `T_ij` and `J_ij` are *not* a uniform sign but the bond-dependent pattern `sigma_ij = eta_ij eta_{P(i)P(j)}`, at `-1` on `64` of the `192` bonds for the
cube-centre inversion and on `128` for the `x = 1/2` reflection; `e.e'` marks that pattern in the table. (3) `H(t,m)` is invariant under `P` about a corner, under `T` and under `PT`,
and goes to `H(t,-m)` under `C`, the two odd-shift parities, `CP`, `CT` and `CPT`. (4) `S_f -> +S_f` in every column. (5) **What the records register**: `B_v`, `Q` and `H_m` are pure
`Z`, hence record-diagonal, and carry the table's `P` and `T` signs; `A_ij`, `S_f`, `T_ij` and `J_ij` have identically zero record-basis diagonal on both geometries, so they are
correlation-only. Since both inversions reverse every bond, the current *vector* is carried to its opposite even where the table reads `+1`.

**Proof.** Every column is a conjugation of Pauli sums, exact and compared key by key against the image operator; the antiunitary columns compose by `(A K)(B K) = A B^*`. The record
statements are the `X`-support test on each Pauli sum, swept over both geometries. All exact.

**Reading, not theorem.** Under a mirror and under time reversal the records are only relabelled, never flipped: the corner parity that says whether matter is present at a place is
carried to the corner parity at the image place, with no sign. Under the exchange of matter with its absence, and under every product containing it, the record content is inverted
instead. The mass term is the one part of the law whose sign any of these operations can change, and it is record-readable; the hop, the current and the face constraints are not
readable from any single pattern of records, and register only in how records at neighbouring places correlate.

## Corollary -- a vector-like Dirac theory, if the law has mirrors

Within the setting declared above, on the two finite geometries named, and **conditional on the law carrying improper point elements, which the Lattice axiom does not name**:

1. If the law carries inversion, the emergent matter is exactly `P`-symmetric about a lattice corner at every mass, and exactly `T`-symmetric at every mass, with `T^2 = +1` and `CPT`
   the identity on the Dirac point: the discrete symmetries of a vector-like Dirac theory, with none of them broken.
2. The improper elements cost the encoding nothing: every face stabilizer and the sign field are carried to themselves, and the correction is a fixed Clifford network on the code qubits
   with a `Z2` gauge factor. The encoding does not obstruct them; whether to add them is an axiom-level decision.
3. The staggered mass and inversion about a corner are the **same matrix** on the Dirac point: the mass is the parity operator, and the chirality anticommutes with both -- the lattice
   form of the standard `gamma^0` relation, with no fitting.
4. The Kramers sign lives in the half-cell-shifted combinations, `PT` with cube-centre inversion and `CP` with the `x = 1/2` reflection, and only at `m = 0`. That is where the emergent
   doublet's spin-half character shows; `T` alone never produces it.
5. `B_v`, `Q` and `H_m` are record-diagonal and carry the table's `P` and `T` signs, while `A_ij`, `S_f`, `T_ij` and `J_ij` are correlation-only: a record history is `P`- and
   `T`-covariant with no extra structure, and inverted under `C`.
6. Owner-level, and not decided here: whether an improper element belongs in the Lattice axiom's symmetry list. This note reports only that the emergent matter would be parity-symmetric
   if it did, and says nothing about the weak sector, which has no chiral counterpart anywhere in this construction.

**Reading, not theorem.** Mirror the lattice through one of its corners, or run it backwards in time, and the emergent matter's law reads the same, whatever its mass. Mirror it through
the centre of a cell instead and the mass changes sign, which is the lattice's way of saying that the mass and the mirror are the same operation on the low-energy doublet. All three
operations together, matter-exchange, mirror and time reversal, act as nothing at all on that doublet. The lattice axiom lists turns but not mirrors; whether the law has mirrors is a
decision, and this note says only that nothing in the emergent matter stands in their way.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. In particular the Lattice axiom's symmetry clause is quoted as it stands, and no improper
  element is added to it.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms; the coarse lattice, the encoding, the sign field and the Hamiltonian are declared objects, and no coefficient is derived: `t` and `m` are
  supplied, and no update rule, formation site, formation rate, coupling, or absolute unit appears. Which Hamiltonian applies is designed, not derived -- see PR #7834.
- No interaction term is added, no second species appears, no chiral sector is constructed, and no continuum limit is taken.

## Interfaces named for other lanes, not moved here

- **The weak sector.** Nothing here bears on it. The construction has no chiral sector at all: the emergent content is a vector-like pair of doublets, and a parity-symmetric vector-like
  theory says nothing about a sector that is not.
- **The continuum.** Everything is a lattice operator or a finite-matrix restriction. Whether `U_P`, `T` or the `CPT` product has a continuum limit, and what it is, is not shown here.
- **The fine `(4,2,2)` pattern's own improper symmetries.** Not examined. Everything here is on the coarse lattice; what the fine superlattice role pattern does under an improper
  element is a separate question.
- **Whether the designed marker rule of PR #7834 is inversion-symmetric.** Not examined. This note treats the encoded algebra and the declared Hamiltonian only.

## Remaining live routes

1. Larger blocks and other geometries. The open `2x2x2` cube and the `4^3` torus are what is proved; nothing is claimed beyond them.
2. The many-body statements at nonzero `m` beyond the cube. Theorems 1, 2, 3 and 5 are exact at every `t` and `m`; the dense confirmation of `T^2 = +1` is on the eight-corner cube only.
3. The other improper elements of the full point group. Two inversions and six reflections are tested, with a proper rotation and a translation for contrast; the remaining improper
   elements are not enumerated here.
4. Correlation structure. That the hop, the current and the face constraints register only through correlations is shown; what those correlations are is not computed.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one fermionic mode per coarse vertex, BK superfast encoding on it; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md; H(t,m) declared here with supplied t and m
conditional: the Lattice axiom names "nearest-neighbor adjacency, standard translations, and proper cubic rotations" -- no improper element; every P statement below holds only if the improper map is applied, and this note does not decide whether the law carries one
geometries: open 2x2x2 coarse cube (8 corners, 12 code qubits, 4096-dim, 6 faces, 128-dim code space); 4^3 coarse torus (64 corners, 192 code qubits, 192 bonds, 192 faces)
parity_operator: U_P = G_g . D_CZ . V_P; V_P alone leaves a pure-Z factor per bond (direction order carried by three), nontrivial on all 192 torus bonds; no Z product can supply it, since a Z-Pauli only signs A_e; the factor depends only on the image edge = 3 +direction edges at its upper endpoint + 3 -direction edges at its lower, degree 6; symmetric and loop-free, so D_CZ is legal
parity_action: U_P A_ij U_P^-1 = sigma_ij A_{P(i)P(j)}, sigma_ij = eta_ij eta_{P(i)P(j)}; U_P B_v U_P^-1 = +B_{P(v)} (no sign, ever); U_P S_f U_P^-1 = +S_{P(f)} (0 flips, code space preserved); U_P J_ij U_P^-1 = o_ij J_{P(i)P(j)}, both inversions reversing all 192 bonds; G_g's mask is a cut with |S| = 32
corner_inversion: sigma = +1 on all 192 bonds; eta carried to itself bond by bond (0 of 192 differ, 0 flipped corners in the one-particle gauge); H(t,m) exactly P-symmetric for every t and m
odd_shift_rule: eps_{P(v)} = (-1)^{sum c} eps_v, shift parity alone; cube-centre inversion and the mid-plane reflections send m -> -m, carrying -1 on 64 and 128 bonds; U_P H_hop U_P^-1 = H_hop exactly for every map
time_reversal: T = Z_E K, Z_E = prod_e Z_e = prod_{v: eps_v = -1} B_v, the unique pure-Z choice; A -> -A, B_v -> +B_v, T_ij -> +T_ij, S_f -> +S_f, J -> -J, Q -> +Q; H(t,m) invariant for every t and m, no m -> -m; T^2 = +1 on the 4096-dim space, on the 128-dim code space and on the Dirac point
dirac_point: 8 zero modes, gap exactly 2m; class BDI (T^2 = +1, C^2 = +1, chiral S = CT = Eps); chirality X = -(Y x X x Y); corner inversion|_D = eps = Z1 Z2 Z3 = the staggered mass = the emergent gamma^0, anticommuting with X; CPT from corner inversion = +1 . I; (PT)^2 = -1 for cube-centre inversion and (CP)^2 = -1 for the x=1/2 reflection, only at m = 0
table_rows_columns: rows B_v, n_v, A_ij, S_f, T_ij, H_hop, H_m, H(t,m), J_ij, Q, eps_v; columns C, P_corner, P_centre, x=1/2 reflection, T, CP, CT, PT, CPT; every entry a sign on the SAME operator at the image index; B_v, S_f, H_hop, H_m, Q, eps_v uniform in every column; A_ij, T_ij, J_ij carry sigma_ij = eta_ij eta_{P(i)P(j)} in the odd-shift columns, not a uniform sign
records: B_v, Q and H_m are pure Z, hence record-diagonal, and carry the table's P and T signs; A_ij, S_f, T_ij and J_ij have identically zero record-basis diagonal on both geometries and register only through correlations
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=33 FAIL=0
```

## Proof boundary

Everything is proved on the **coarse** lattice `2Z^3`, on exactly two finite geometries: the open `2x2x2` coarse cube and the `4^3` coarse torus. Nothing is claimed for `Z^3`, for the
fine lattice, or for any larger region, and no thermodynamic limit is taken.

**Every parity statement is conditional on the law carrying improper point elements.** The Lattice axiom names proper cubic rotations only. What is proved is what the encoded algebra
does when an improper map is applied, together with the fact that applying it costs the encoding nothing: `H_hop` is invariant, every face stabilizer is carried to itself with no sign,
and the correction is a fixed Clifford network. That is evidence the law *could* carry improper elements at no cost; it is not a licence to add them, and whether to add them is an
axiom-level question for the owner. Time reversal carries no such condition: `T = Z_E K` is built from the encoding's own objects.

The content is **free hopping plus one declared diagonal term**. No interaction appears, and the coefficients `t` and `m` are **supplied**: derived from no axiom and fixed by no clause
quoted here. No sign statement anywhere depends on `t`. Which Hamiltonian applies is a designed choice, not an axiom consequence.

Theorems 1, 2, 3 and 5 are many-body statements in the encoded algebra, exact at every `t` and `m`. Theorem 3's dense confirmation is one `4096`-dimensional cube computation; Theorem 4
is a `64x64` one-particle computation and `8x8` restrictions of it, about the exact zero-mode subspace of a finite matrix and the `O(p)` term of the landed Bloch expansion. **No
continuum limit is taken**, and nothing is claimed about Lorentz covariance beyond PR #7888's own bound, about an interacting theory, or about an anomaly. The `CZ` network is a
construction on the encoding, not an axiom object. `C`'s existence still requires an even corner count, as PR #7892 established; both geometries satisfy it.

## Review record

An honest auditor should come away with: one declared Hamiltonian, on two named finite geometries, whose emergent matter carries time reversal exactly at every mass with `T^2 = +1` and
no Kramers doubling, and -- conditional on the law carrying improper point elements, which the Lattice axiom does not name -- parity about a lattice corner exactly at every mass,
realised as `U_P = G_g D_CZ V_P` because the encoding's direction order is not itself mirror-symmetric and no product of `Z`'s can repair it. On the Dirac point the corner parity
operator is literally the staggered-mass matrix and `CPT` built from it is the identity. The full table is exact, its uniform and bond-dependent rows are distinguished explicitly, and
the record reading is stated: `B_v`, `Q` and `H_m` register directly; the hop, the current and the face constraints register only through correlations.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the five context notes in "Imports and authority"
are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at `PASS=33 FAIL=0`, runtime under the declared `90` seconds,
stdout under `5500` characters, and passing pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.

