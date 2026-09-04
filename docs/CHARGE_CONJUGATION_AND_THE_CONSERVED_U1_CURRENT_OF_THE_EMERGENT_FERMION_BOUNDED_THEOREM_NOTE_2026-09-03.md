---
claim_id: charge_conjugation_and_conserved_u1_current_emergent_fermion
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3, carrying one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, with the Kawamoto-Smit link signs eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}, for the ONE DECLARED Hamiltonian H(t,m) = -t sum_<ij> eta_ij T_ij - (m/2) sum_v eps_v B_v whose coefficients t and m are supplied and are fixed by nothing quoted here, and on the named finite blocks and tori only: (T1) with n_i = (I - B_i)/2 the lattice continuity equation dn_i/dt = i[H, n_i] = - sum_{j~i} J_ij holds with the bond current J_ij = eta_ij (t/2) A_ij (I - B_i B_j) at residual identically 0 at all 27 corners of the open 3x3x3 block and all 64 corners of the 4^3 torus; equivalently J_ij = i eta_ij T_ij B_j = -i eta_ij T_ij B_i = (eta_ij/4) A_ij (B_i - B_j)^2 on every bond; the candidate (t/2) A_ij (B_i + B_j) fails structurally because B_i + B_j annihilates the sector B_i = -B_j in which the hop acts, leaving 12 and 24 nonzero residual terms on the two lattices; every J_ij is Hermitian with J_ji = -J_ij while T_ji = +T_ij, is exactly two Pauli monomials, has X-support on exactly one qubit -- its own edge site -- and total support 11 qubits in the bulk = star(i) union star(j), 6, 8 or 10 at the open boundary; [J_ij, S_f] = 0 for every bond-face pair, so the current is a gauge-legal observable of the code; every Pauli monomial of J_ij carries nonzero X-support, so its record-diagonal part is identically zero, verified over all 12 bonds and all 4096 record patterns of the 2x2x2 cube; and [H, N] = [H, Q] = 0 with the bond currents cancelling in pairs. (T2) With C_0 = the product over a perfect matching M of the A_ij and Z_E = the product of all Z_e = the product over the odd-sublattice corners of B_v = (-1)^{N_odd}, the operator C = Z_E C_0 satisfies, on the 2x2x2 cube, the open 4x4x4 block and the 4^3 torus, with x-dimers and independently with y-dimers: B_v -> -B_v, n_v -> I - n_v, rho_v = n_v - 1/2 -> -rho_v, A_ij -> -A_ij, S_f -> +S_f with no sign so the code space is preserved, T_ij -> +T_ij, H_hop -> +H_hop, H_m -> -H_m, hence H(t,m) -> H(t,-m) and C is an exact symmetry at m = 0; J_ij -> -J_ij and Q -> -Q; C^2 = +I; the grading eps_v is a supplied corner label and is unchanged; C_0 alone flips B_v, T_ij, H_hop and H_m and fixes A_ij and J_ij, while Z_E alone is the chiral or sublattice symmetry flipping A_ij, T_ij and H_hop and fixing B_v, H_m and Q; the action is matching-independent up to phase and independent of the bond weights, holding verbatim for the KS signs, for all-+1 weights and for generic rational weights. (T3) The product over all corners of B_v equals I identically on every block and torus tested, each edge carrying a Z from both of its endpoints, so B_v -> -B_v at every corner forces I -> (-1)^{|V|} I: for a region with an odd number of corners, the open 3x3x3 block with |V| = 27, no unitary C exists on the code space at all, not merely no Pauli one, the code space being one parity sector and C sending N -> |V| - N; in edge-flip form the same condition reads that flipping every B_v needs a T-join with T = V, odd degree at every corner, while sum_v deg_S(v) = 2|S| is even; such an operator exists exactly when |V| is even, minimally along a perfect matching. (T4) Q = sum_v (n_v - 1/2) = -(1/2) sum_v B_v is conserved, C-odd and a pure Z-operator, hence diagonal in the record basis; on all 4096 record patterns of the 2x2x2 cube Q equals the number of corners whose six incident edge records hold an odd number of the value 1, minus |V|/2, at deviation 0, taking the integer values -4, -2, 0, 2, 4. (T5) On the one-particle 4^3 torus {M, Eps} = 0 and eps (I - P(m)) eps = P(-m) at m = 0, 0.5, 1, 2, so at m = 0 the sea projector is C-invariant, <n_v>_{-m} = 1 - <n_v>_m site by site, and <n_v> = 1/2 is the C fixed point; on the 2x2x2 cube's 128-dimensional even-N code space C is unitary with C N C^-1 = |V| - N and C H(t,m) C^-1 = H(t,-m) at m = 0, 0.7, 1.5, the m = 0 many-body spectrum is exactly E -> -E, the ground state has E = -6.928203230 = -4 sqrt 3 with <N> = 4 = |V|/2 and |<g|C|g>| = 1, with the corollary <J_ij> = 0 on every bond, while for the empty state |<N=0|C|N=0>| = 0 and C|N=0> lies entirely at N = 8 with unit overlap. The values of t and m are supplied data; no interaction, no gauge field beyond the encoding's own Z2 structure and no continuum limit is treated, and no claim is made that this U(1) is electromagnetism. Nothing here is derived from any axiom, no axiom is amended, no status is set, no hypothesis is adopted, and no registry entry is created."
upstream_dependencies: []
runner: scripts/charge_conjugation_and_conserved_u1_current_check_2026_09_03.py
---

# Charge conjugation and the conserved `U(1)` current of the emergent fermion

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/charge_conjugation_and_conserved_u1_current_check_2026_09_03.py`](../scripts/charge_conjugation_and_conserved_u1_current_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/charge_conjugation_and_conserved_u1_current_check_2026_09_03.txt`](../logs/runner-cache/charge_conjugation_and_conserved_u1_current_check_2026_09_03.txt)
**Parents:** none load-bearing. Every premise used below is declared in this note; the context notes are plain-text pointers listed in "Imports and authority".

The coarse-lattice emergent fermion has a number operator, a hop, and a mass term. What it has not been given is the pair of objects a conserved quantity actually
consists of: a charge and the local flow of that charge between neighbouring corners. The question here is what that pair is inside the readable algebra, what
conjugation exchanges matter and its absence, and which of the two the records register. The charge turns out to be a parity count on six records at a corner,
readable directly; the current turns out to be a two-monomial bond operator with no record-diagonal part at all.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems about one declared Hamiltonian on the coarse-lattice emergent fermion: the lattice continuity equation and its bond current, the charge-conjugation operator and its full transformation table, the parity condition governing that operator's existence on a finite region, the charge as a record readout, and the half-filled sea as the conjugation fixed point. The symplectic Pauli statements are exact Gaussian-rational arithmetic on F2 supports with Z4 phases; the record-readout statements are exact integer arithmetic over all 4096 cube patterns; the tagged numerical items are floating-point cross-checks at the stated tolerance."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: whether anything couples to this U(1)."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. Groups `A`, `B`, `C` and `D` are exact -- Gaussian-rational
coefficients on symplectic Pauli monomials, `F2` supports and `Z4` phases, complete sweeps, and integer record arithmetic, with no floating-point step anywhere --
and the items tagged `[numerical]` in group `E` are floating-point cross-checks at the stated tolerance.

1. `T1` (`A`). The lattice continuity equation, the bond current, and what the naive candidate does instead.
2. `T2` (`B`). Charge conjugation `C = Z_E C_0` and the full transformation table, with the `C_0` and `Z_E` columns.
3. `T3` (`C`). The parity condition: an operator flipping every `B_v` exists exactly when the region has an even number of corners.
4. `T4` (`D`). The charge as a record readout: a six-bit parity count per corner.
5. `T5` (`E`). The half-filled sea is the conjugation fixed point; the empty state is not.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the Majorana form of fermionic charge
conjugation, and the T-join characterisation of a degree-parity edge set are standard methodology; every object is redeclared here and the runner recomputes every
statement. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7890): the Hamiltonian `H(t,m)`, the
  grading `eps_v`, and the `4^3` one-particle machinery. Its `T8`, that conjugation by the grading exchanges `+-m` on the one-particle operator, is the one-particle
  shadow of what `T2` here establishes at the operator level.
- `THE_VACUUM_QUESTION_IS_ONE_COEFFICIENT_OF_THE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7885): `sum_i B_i` commutes with every hop, and the occupancy term
  read as a chemical potential.
- `MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7879): the sea, and
  `<n_v> = 1/2` exactly.
- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844) and
  `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): the encoding, the superlattice
  role pattern, and the coarse sublattice `2Z^3`.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting". No grade of theirs is cited and no hypothesis is adopted.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has
algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions" -- the law
supplies the odds. **Record**: "Records form", "a record locks exactly one admissible local possibility", "records are permanent", "Only records are readable", and
"A readout value is determined by record content alone."

The lattice is physical. Everything below reads the Kawamoto-Smit sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, on the superlattice
role pattern's sublattice. Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used
anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the KS sign field
on it, the superfast encoding with its face stabilizers, the encoded hop, the grading `eps_v`, and the Hamiltonian `H(t,m)` with its supplied coefficients. `P1`
(`A`) is the continuity equation and the bond current; `P2` (`B`) the conjugation operator and its table; `P3` (`C`) the parity condition on the region; `P4` (`D`)
the record readout of the charge; `P5` (`E`) the sea as the fixed point. `P2` uses `P0` only; `P3` uses the single relation among the `B_v` established in it; `P4`
uses `P1`'s form of `Q`; `P5` uses `P2`. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The **KS
sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`. The **encoding** is the Bravyi-Kitaev superfast
encoding on the coarse lattice, code qubits on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`.

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_v  = the product of the six Z's at corner v = I - 2 n_v,   S_f = the ordered product of the four A's around a coarse face f
n_v  = (I - B_v)/2                     the occupation of coarse vertex v; B_v = -1 marks the excitation
T_ij = (i/2) A_ij (B_i - B_j)          the encoded hop across (i, j),  T_ji = +T_ij
eps_v = (-1)^{v_1+v_2+v_3}             the supplied corner grading
H(t,m) = -t sum_<ij> eta_ij T_ij - (m/2) sum_v eps_v B_v          THE DECLARED LAW; t and m are supplied
J_ij = eta_ij (t/2) A_ij (I - B_i B_j)                            THE BOND CURRENT
N = sum_v n_v,   Q = sum_v (n_v - 1/2) = -(1/2) sum_v B_v         the number and the charge
C_0 = prod over a perfect matching M of A_ij,  Z_E = prod over all edges of Z_e,  C = Z_E C_0
```

The **star** of a corner is the set of edge sites incident to it, six in the bulk. A **record pattern** is one assignment of a value to every edge record; the record
basis is the joint eigenbasis of the `Z_e`. An operator is **record-diagonal** when it is diagonal in that basis, so that its value is fixed by record content alone.
A **perfect matching** is a set of bonds meeting every corner exactly once; a **T-join with `T = V`** is an edge subset of odd degree at every corner.

## Theorem 1 -- the continuity equation and the bond current

**Conclusion.** (1) `dn_i/dt = i[H, n_i] = - sum_{j~i} J_ij` with `J_ij = eta_ij (t/2) A_ij (I - B_i B_j)`, at residual identically `0` at all `27` corners of the
open `3x3x3` block and all `64` corners of the `4^3` torus. (2) Equivalently, on every bond, `J_ij = i eta_ij T_ij B_j = -i eta_ij T_ij B_i = (eta_ij/4) A_ij (B_i -
B_j)^2`. (3) The candidate `(t/2) A_ij (B_i + B_j)` fails structurally: `B_i + B_j` annihilates the sector `B_i = -B_j` in which the hop acts, and the residual
carries `12` and `24` nonzero Pauli terms on the two lattices. (4) Every `J_ij` is Hermitian; `J_ji = -J_ij` while `T_ji = +T_ij`; it is exactly two Pauli monomials
with `X`-support on exactly one qubit, its own edge site, and total support `11` qubits in the bulk, `= star(i) union star(j)`, and `6`, `8` or `10` at the open
boundary. (5) `[J_ij, S_f] = 0` for every bond-face pair on both lattices. (6) Every monomial of `J_ij` carries nonzero `X`-support, so its record-diagonal part is
identically zero -- confirmed over all `12` bonds and all `4096` record patterns of the `2x2x2` cube. (7) `[H, N] = [H, Q] = 0`, the corner equations summed with the
bond currents cancelling in pairs, and `Q` is a pure `Z`-operator.

**Proof.** Item 1 expands `i[H, n_i]` and `sum_j J_ij` as Pauli sums with Gaussian-rational coefficients and compares key by key; both sides carry two monomials per
incident bond, by item 4, and the keys and coefficients agree. Items 2 and 3 are the same comparison on one bond and at one corner. Items 4 to 7 are `F2`
support arithmetic with `Z4` phases: a monomial commutes with another exactly when their symplectic form vanishes, and a monomial is diagonal exactly when its
`X`-support is empty. All exact.

**Reading, not theorem.** The quantity that flows is the same corner parity that says whether a particle is there. What flows along one bond is an operator supported
on the two corner stars that meet at it, and it changes the record on that one edge -- so no single pattern of records shows it. The natural first guess, the sum of
the two corner parities, is exactly wrong: it vanishes precisely where a particle would be passing.

## Theorem 2 -- charge conjugation, and the whole transformation table

**Conclusion.** With `C_0` the product over a perfect matching of the `A_ij` and `Z_E = prod_e Z_e = prod over the odd-sublattice corners of B_v = (-1)^{N_odd}`, the
operator `C = Z_E C_0` acts, on the `2x2x2` cube, the open `4x4x4` block and the `4^3` torus, with `x`-dimers and independently with `y`-dimers, as:

```text
                B_v      n_v        rho_v    A_ij     S_f     T_ij     H_hop     H_m     J_ij     Q
   C            -B_v     I - n_v    -rho_v   -A_ij    +S_f    +T_ij    +H_hop    -H_m    -J_ij    -Q
   C_0          -B_v     I - n_v    -rho_v   +A_ij    +S_f    -T_ij    -H_hop    -H_m    +J_ij    -Q
   Z_E          +B_v     n_v        +rho_v   -A_ij    +S_f    -T_ij    -H_hop    +H_m    -J_ij    +Q
```

Hence `C H(t,m) C^-1 = H(t,-m)`, an exact symmetry at `m = 0`; `C^2 = +I`; `S_f -> +S_f` with no sign, so the code space is preserved; the grading `eps_v` is a
supplied corner label and is unchanged; the action is matching-independent up to phase; and the whole table is independent of the bond weights, holding verbatim for
the KS signs, for all-`+1` weights and for generic rational weights.

**Proof.** Fermionic conjugation is the particle-hole map on the Majoranas, implemented by their total product; pairing the Majoranas along any perfect matching and
using `gamma_i gamma_j = i A_ij` gives the purely Pauli operator `C_0`, and `Z_E` is the diagonal dressing that restores the sign of the hop. Every entry is then
conjugation of a Pauli sum by a Pauli monomial, a sign per key fixed by the symplectic form, compared exactly. Matching-independence is checked directly by rebuilding
`C` from a second matching; weight-independence by rebuilding `H_hop` with two further weight assignments. All exact.

**Reading, not theorem.** Exchanging matter with its absence is one operation on the records: flip the parity at every corner. Doing it along a set of edges that
touches every corner once is enough. The law's hopping part does not notice; the price term reverses; so the sign of a mass is not something the exchange preserves,
and at zero mass the exchange is an exact symmetry of the law.

## Theorem 3 -- when such an exchange exists on a finite region

**Conclusion.** (1) The product over all corners of `B_v` equals `I` identically, on every block and torus tested: each edge carries a `Z` from both of its
endpoints. This is the one relation the encoded corner operators obey. (2) Hence `B_v -> -B_v` at every corner forces `I -> (-1)^{|V|} I`: on a region with an odd
number of corners -- the open `3x3x3` block, `|V| = 27` -- no unitary `C` exists on the code space at all, not merely no Pauli one. Equivalently, the code space is a
single fermion-parity sector and `C` sends `N -> |V| - N`, changing parity by `(-1)^{|V|}`. (3) In edge-flip form the same condition reads: flipping every `B_v`
requires an edge subset of odd degree at every corner, a T-join with `T = V`, while `sum_v deg_S(v) = 2|S|` is even. Such a subset exists exactly when `|V|` is even,
minimally a perfect matching -- as built in Theorem 2 for `|V| = 8` and `|V| = 64`.

**Proof.** Item 1 is `F2` support arithmetic: the symmetric difference of all corner stars is empty. Item 2 is item 1 conjugated. Item 3 is the handshake identity on
the degree sum. All exact.

**Reading, not theorem.** Whether matter and its absence can be exchanged at all is a property of the region, not of the law: it takes an even number of corners. On
a block with an odd count there is no such operation to be had, and the parity of the corner count is worth stating whenever a finite block is used for anything
downstream.

## Theorem 4 -- the charge is a record readout

**Conclusion.** `Q = sum_v (n_v - 1/2) = -(1/2) sum_v B_v` is conserved, `C`-odd, and a pure `Z`-operator, hence record-diagonal. On all `4096` record patterns of
the `2x2x2` cube, `Q` equals the number of corners whose six incident edge records hold an odd number of the value `1`, minus `|V|/2`, at deviation `0`; it takes the
integer values `-4, -2, 0, 2, 4`, symmetric about `0`. By contrast every `J_ij` has an identically zero diagonal over all `12` bonds and all `4096` patterns.

**Proof.** `n_v = (I - B_v)/2` and `B_v` is the product of six `Z`'s, whose eigenvalue on a record pattern is `+1` or `-1` according to the parity of the six values
read there; summing gives the count. Conservation and `C`-oddness are Theorems 1 and 2. The current's zero diagonal is Theorem 1 item 6. Exact integer arithmetic
throughout; the spectrum is even-valued because the relation of Theorem 3 item 1 makes the total number of odd corners even.

**Reading, not theorem.** Count, at each corner, whether an odd number of its six records read `1`. That count minus half the corners is a conserved charge, and it
can be read straight off the records. The flow of that charge between two corners is also an exact lattice quantity, but no single pattern of records shows it; it
shows only in how records at neighbouring places correlate.

## Theorem 5 -- the sea is the fixed point, the empty state is not

**Conclusion.** (1) One-particle `4^3` torus: `{M, Eps} = 0` and `eps (I - P(m)) eps = P(-m)` at `m = 0, 0.5, 1, 2`; at `m = 0` the sea projector is `C`-invariant,
`<n_v>_{-m} = 1 - <n_v>_m` site by site, and `<n_v> = 1/2` is the `C` fixed point. (2) Cube many-body, on the `128`-dimensional even-`N` code space of the `2x2x2`
cube: `C` is unitary there with `C N C^-1 = |V| - N`, and `C H(t,m) C^-1 = H(t,-m)` at `m = 0, 0.7, 1.5`; the `m = 0` spectrum is exactly `E -> -E`. (3) The `m = 0`
ground state has `E = -6.928203230 = -4 sqrt 3`, `<N> = 4 = |V|/2` and `|<g|C|g>| = 1`: the sea is the `C` fixed point, with the corollary `<J_ij> = 0` on every bond.
(4) For the empty state, `|<N=0|C|N=0>| = 0` and `C|N=0>` lies entirely at `N = 8` with unit overlap.

**Proof.** Item 1 diagonalises the `64x64` one-particle operator `M + m Eps` and compares projectors. Items 2 to 4 build the `4096`-dimensional cube algebra, project
onto the joint `+1` eigenspace of the six face stabilizers -- dimension `128 = 2^{|V|-1}`, carrying only even `N` by the relation of Theorem 3 item 1 -- and
diagonalise there. Item 3's current corollary is forced at `m = 0`, where `J_ij` is `C`-odd and the state is `C`-even. `[numerical, 1e-12]` for item 1 and
`[numerical, 1e-10]` for items 2 to 4.

**Reading, not theorem.** Exchanging matter with its absence is a symmetry of the half-filled sea and not of the empty state, which is one more reason the sea is the
vacuum. The empty state is carried by the exchange to the completely full one, as far from itself as it can be; the sea is carried to itself.

## Corollary -- a readable charge and an unreadable current

Within the setting declared above, and on the finite blocks and tori named:

1. A global `U(1)` with an exactly conserved, gauge-legal, local bond current exists in the emergent matter. The charge is readable from the records -- a six-bit
   parity count at each corner -- and the current is not: it has no record-diagonal part at all, and registers only through record correlations.
2. `C = Z_E C_0` is an exact symmetry at `m = 0` and exchanges `+-m`, so a mass sign is a `C`-odd supplied datum. The one-particle statement of PR #7890, that
   conjugation by the grading exchanges `+m` and `-m`, is the shadow of this operator-level table.
3. The existence of `C` is a parity condition on the region: an even corner count. This is a boundary of the encoding worth stating for any finite block used
   downstream, and it is a property of the region rather than of the law.
4. Neither the charge nor the current is coupled to any gauge field here. The gauge structure of the encoding is `Z2`; no photon is claimed, and nothing here
   identifies this `U(1)` with electromagnetism.
5. Read with the vacuum ruling of PR #7885 and the sea of PR #7879: the state that has a conjugation symmetry is the sea.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms; the coarse lattice, the encoding, the sign field and the Hamiltonian are declared objects, and no coefficient is derived:
  `t` and `m` are supplied, and no update rule, formation site, formation rate, coupling, or absolute unit appears. Which Hamiltonian applies is designed, not
  derived -- see PR #7834.
- No interaction term is added, no second species appears, and no continuum limit is taken.

## Interfaces named for other lanes, not moved here

- **`T` and `CPT`.** Not computed. Only `C` is built; time reversal and the combined operation are untouched, and nothing here bears on either.
- **Coupling to a gauge field.** Nothing couples to this `U(1)` in the declared law. What would gauge it, and whether the encoding's own `Z2` structure obstructs
  that, is a question for the lane that owns the dynamical clause.
- **The continuum current.** Everything is a lattice operator. Whether `J_ij` has a continuum limit, and what it is, is not shown here.
- **Anomalies.** No anomaly statement is made or implied. The chiral structure of the staggered fermion is not analysed here at all.

## Remaining live routes

1. Larger blocks and other geometries. The `2x2x2` cube, the open `3x3x3` and `4x4x4` blocks and the `4^3` torus are what is proved; nothing is claimed beyond them.
2. The many-body statements at nonzero `m`. Theorems 1 to 4 are exact at every `m`; the many-body spectral statements of Theorem 5 are on the eight-corner cube only.
3. Current-current correlations. That the current registers only through correlations is shown; what those correlations are is not computed.
4. Other conserved quantities. Only `N` and `Q` are examined; whether the declared law carries further local conservation laws is not treated.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one fermionic mode per coarse vertex, BK superfast encoding on it; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md; H(t,m) declared here with supplied t and m
continuity: i[H, n_i] = -sum_{j~i} J_ij, J_ij = eta_ij (t/2) A_ij (I - B_i B_j), residual identically 0 at all 27 corners of the open 3x3x3 and all 64 of the 4^3 torus
closed_forms: J_ij = i eta T_ij B_j = -i eta T_ij B_i = (eta/4) A_ij (B_i - B_j)^2 on every bond
naive_candidate: (t/2) A_ij (B_i + B_j) fails; B_i + B_j annihilates the sector B_i = -B_j; 12 and 24 nonzero residual terms
current_properties: Hermitian; J_ji = -J_ij while T_ji = +T_ij; exactly 2 Pauli monomials; X-support 1 qubit (its own edge site); total support 11 in the bulk = star(i) u star(j), 6/8/10 at the open boundary; [J_ij, S_f] = 0 on every bond-face pair; record-diagonal part identically zero on all 12 bonds x 4096 cube patterns; [H, N] = [H, Q] = 0
conjugation: C = Z_E C_0, C_0 = prod_M A_ij, Z_E = prod_e Z_e = prod_{v odd} B_v = (-1)^{N_odd}; on the 2x2x2 cube, the open 4x4x4 and the 4^3 torus, x-dimers and y-dimers alike; C^2 = +I
table_C: B_v -> -B_v, n_v -> I - n_v, rho_v -> -rho_v, A_ij -> -A_ij, S_f -> +S_f, T_ij -> +T_ij, H_hop -> +H_hop, H_m -> -H_m, H(t,m) -> H(t,-m), J_ij -> -J_ij, Q -> -Q, eps_v unchanged
table_C0_ZE: C_0 flips B_v, T_ij, H_hop, H_m and fixes A_ij, J_ij; Z_E flips A_ij, T_ij, H_hop and fixes B_v, H_m, Q; matching-independent up to phase; independent of the bond weights (KS, all-+1, generic rational)
parity_condition: prod_v B_v = I identically, so B_v -> -B_v everywhere forces I -> (-1)^{|V|} I; |V| = 27 odd (open 3x3x3) admits no unitary C on the code space at all; T-join with T = V needs all degrees odd against an even degree sum; exists iff |V| even, minimally a perfect matching
charge_readout: Q = #{corners with an odd number of the value 1 among their six incident edge records} - |V|/2 on all 4096 cube patterns, deviation 0; integer values -4, -2, 0, 2, 4; Q pure Z
sea: one-particle 4^3, {M, Eps} = 0, eps(I - P(m))eps = P(-m) at m = 0, 0.5, 1, 2; <n_v>_{-m} = 1 - <n_v>_m; <n_v> = 1/2 the C fixed point at m = 0
cube_many_body: 128-dim even-N code space; C unitary, C N C^-1 = |V| - N; C H(t,m) C^-1 = H(t,-m) at m = 0, 0.7, 1.5; m = 0 spectrum E -> -E; ground state E = -6.928203230 = -4 sqrt 3, <N> = 4 = |V|/2, |<g|C|g>| = 1; <J_ij> = 0 on every bond
empty_state: |<N=0|C|N=0>| = 0 and C|N=0> lies entirely at N = 8 with unit overlap
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=32 FAIL=0
```

## Proof boundary

Everything is proved on the **coarse** lattice `2Z^3`: the `2x2x2` cube, the open `3x3x3` and `4x4x4` blocks, and the `4^3` torus. Nothing is claimed for `Z^3` and
nothing is claimed for any larger region.

The content is **free hopping plus one declared diagonal term**. No interaction appears, and the coefficients `t` and `m` are **supplied**: derived from no axiom and
fixed by no clause quoted here. Which Hamiltonian applies is a designed choice, not an axiom consequence.

Theorems 1 to 4 are many-body statements in the encoded algebra, exact at every `t` and `m`. Theorem 5's cube statements come from **one** eight-corner many-body
diagonalisation on a `128`-dimensional code space, and its one-particle statements from `64x64` tori; no larger many-body region is treated.

No continuum limit is taken, and no continuum current is constructed. No anomaly statement is made. No claim is made that this `U(1)` is electromagnetism or that
anything couples to it; the encoding's own gauge structure is `Z2` and no photon appears anywhere. The parity result of Theorem 3 is a condition on the region and is
stated as such: it says exactly when the exchange operator exists, and nothing about whether some other operation on some other region would serve.

## Review record

An honest auditor should come away with: one declared Hamiltonian, on named finite clusters, carrying a global `U(1)` whose charge is a parity count on the six
records at each corner -- readable directly, at deviation `0`, on every one of the `4096` patterns of the smallest cube -- and whose bond current is an exact,
Hermitian, gauge-legal two-monomial operator with no record-diagonal part, so that it registers only in correlations. The exchange of matter with its absence is the
Pauli operator `C = Z_E C_0`; its full transformation table is exact and independent of both the matching and the bond weights; it sends `H(t,m)` to `H(t,-m)`; it
exists exactly when the region has an even number of corners; and it fixes the half-filled sea while carrying the empty state to the completely full one.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the five context notes in
"Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at
`PASS=32 FAIL=0`, runtime under the declared `90` seconds, stdout under `5500` characters, and passing pipeline, strict-lint and changed-evidence gates; independent
audit remains a separate lane.
