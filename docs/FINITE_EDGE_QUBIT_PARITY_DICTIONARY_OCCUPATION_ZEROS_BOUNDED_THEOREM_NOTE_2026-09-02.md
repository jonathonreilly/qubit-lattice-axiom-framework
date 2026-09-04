---
claim_id: finite_edge_qubit_parity_dictionary_occupation_zeros_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "Conditional finite-model result: for one fixed-order Bravyi-Kitaev superfast edge-qubit encoding on the named cube and open-grid graphs, the declared incidence-parity map is a constant-fibre map onto even vertex occupations; the encoded fixed-sector matrices are exactly diagonal-phase equivalent to the corresponding Jordan-Wigner matrices; exact free-fermion calculations give the listed occupation-probability zeros at g=0; and separate finite numerical scans, sign/flux calculations, and positive-control calculations give only the explicitly bounded results reported below. The encoding, dictionary, Hamiltonian, sectors, basis, and boundary conditions are supplied inputs, not emergent consequences of the framework axioms."
upstream_dependencies: []
runner: scripts/finite_edge_qubit_parity_dictionary_occupation_zeros_check_2026_09_02.py
---

# Finite edge-qubit parity dictionary and occupation-probability zeros

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** independent audit required
**Status:** proposed_retained
**Status authority:** effective status is pipeline-derived after independent audit ratification and dependency closure. This source sets no audit verdict.
**Primary runner:**
[`scripts/finite_edge_qubit_parity_dictionary_occupation_zeros_check_2026_09_02.py`](../scripts/finite_edge_qubit_parity_dictionary_occupation_zeros_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/finite_edge_qubit_parity_dictionary_occupation_zeros_check_2026_09_02.txt`](../logs/runner-cache/finite_edge_qubit_parity_dictionary_occupation_zeros_check_2026_09_02.txt)

This note retains a conditional finite algebraic result. It declares an edge-qubit encoding and an incidence-parity map, then computes their consequences on three named open graphs. Derivation of those inputs from framework axioms, physical lattice realization, emergent matter, and symmetry selection rules all lie outside its claim scope.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite Pauli, stabilizer, incidence-map, diagonal-gauge, and Q(sqrt2) calculations, together with explicitly labelled numerical scans on four couplings."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Independently audit the finite calculations and their declared import boundary."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The machine-bound target is the conjunction of runner groups `A` through `G`:

1. `A`: finite Pauli relations, face-stabilizer ranks, code dimensions, and the incidence-parity map on the three named graphs.
2. `B`: an exact diagonal phase gauge between each encoded fixed-sector matrix and its Jordan-Wigner reference matrix.
3. `C`: exact `g=0` occupation probabilities and their classified zero sets from Slater determinants over `Q(sqrt(2))`, with a complete one-particle spectrum certificate.
4. `D`: a floating-point witness at `g in {0, 0.5, 1, 2}`, evaluated at tolerance `1e-12`.
5. `E`: exact constant fibres from edge strings to even occupation patterns.
6. `F`: exact fixed-basis hop phases, their two-endpoint-star support, and closed-four-cycle phase products.
7. `G`: an exact finite positivity lemma for a separately declared bare-edge-flip control, plus a labelled four-coupling numerical check.

Groups `A`, `B`, `C`, `E`, `F`, and the structural part of `G` use finite integer, `F2`/`Z4`, Gaussian-integer, rational, or `Q(sqrt(2))` arithmetic. Group `D` and the final control checks use floating-point eigensolvers and make only tolerance-qualified claims.

## Supplied inputs and imported methods

The following inputs are load-bearing conditions of this theorem:

- the three finite open graphs, their numerical vertex labels, their listed edge and face sets, and the numerical neighbour ordering;
- one qubit for each abstract graph edge and the ordinary tensor-product computational basis `|y>` for `y in F2^E`;
- the displayed superfast operators, face-loop `+1` code space, incidence-parity map, hopping-plus-neighbour-interaction Hamiltonian, fixed occupation sectors, real coupling `g`, and the pendant auxiliary convention;
- the Jordan-Wigner reference ordering given by the numerical vertex labels; and
- open boundary conditions and the specific sampled couplings used by the numerical scan.

The Bravyi-Kitaev superfast operator construction and its fermionic interpretation are imported methodology; the finite operators and relations used here are redeclared and checked. A representative source is Setia, Bravyi, Mezzacapo, and Whitfield, [“Superfast encodings for fermionic quantum simulation”](https://arxiv.org/abs/1810.05274). Jordan-Wigner ordering, Slater-determinant free-fermion states, and the Perron-Frobenius theorem are standard mathematical imports. The runner checks their finite hypotheses and consequences here; derivations of the general methods from framework premises remain outside scope.

No observational value, fitted constant, accepted framework premise, Record readout, state-preparation rule, or physical edge-site realization enters the proof. In particular, the words “edge,” “vertex,” and “occupation” below have their declared graph and basis meanings.

## Declared finite models

Let `G=(V,E)` be one of:

- `cube`: the graph on `F2^3`, labelled `s=4a+2b+c`, with edges joining vertices that differ in one binary coordinate (`8` vertices, `12` edges, `6` square faces);
- `grid3x3`: the open `3x3` square grid (`9` vertices, `12` edges, `4` square faces); or
- `grid3x3+pendant`: the same grid with vertex `9` joined only to vertex `0` (`10` vertices, `13` edges, the same `4` square faces).

The first graph has three binary coordinate directions only in this finite combinatorial sense. The calculation supplies no translation action, proper-cubic-rotation representation, angular-momentum label, spin representation, thermodynamic limit, or physical embedding in `Z^3`.

For every undirected edge, one qubit has computational-basis bit `y_e`. At each vertex, neighbours are ordered by their numerical labels. For an ordered edge `(i,j)`, the supplied operators are

```text
A_ij = X_(ij) times Z on incident edges ordered before (i,j) at both endpoints,
A_ji = -A_ij,
B_i  = product of Z on star(i),
S_f  = ordered product of the four A operators around face f.
```

The code space is the simultaneous `+1` eigenspace of the `S_f`. The mathematical dictionary is the binary incidence map

```text
q_G : F2^E -> {n in F2^V : sum_i n_i = 0 mod 2},
q_G(y)_i = |{e in star(i) : y_e=1}| mod 2 = (1-B_i)/2 on |y>.
```

Thus the domain consists of edge-basis strings and the codomain consists of even vertex-occupation bit strings. This stipulated map has solely mathematical status here; framework Record semantics remain outside scope. For these connected graphs its kernel is the cycle space of dimension `E-V+1`, so every codomain point has `2^(E-V+1)` preimages.

For the graph edges included in the Hamiltonian,

```text
T_ij = (i/2) A_ij (B_i-B_j),
H_enc(g) = +sum_(i,j) T_ij + g sum_(i,j) n_i n_j,
H_F(g)   = -sum_(i,j) (c_i^dag c_j + c_j^dag c_i) + g sum_(i,j) n_i n_j.
```

Each displayed sum runs once over every listed undirected Hamiltonian edge in its `i<j` orientation. The reference matrix `H_F(g)` is the displayed spinless-fermion hopping-plus-neighbour-interaction matrix constructed with Jordan-Wigner ladders in numerical vertex order. The sectors are cube `N=4`, grid `N=6`, and pendant `n_9=1` with three occupied grid vertices. The pendant edge carries no Hamiltonian term. These choices intentionally encode the reference fermionic model; agreement with that model is a checked consequence of the supplied encoding, not evidence that the dictionary or statistics emerged independently.

## Finite results

### A. Pauli relations, stabilizers, and the parity dictionary

On all three graphs the runner exhaustively checks the declared `R0`-`R4` Pauli relations. The cube’s six face loops have one relation, their product `+I`, and rank `5`; each grid-based graph has four independent face loops. The stabilizer groups contain no `-I`, and only the identity has trivial `X` part. The code dimensions are therefore

```text
cube:              2^12 / 2^5 = 128 = 2^(8-1)
grid3x3:           2^12 / 2^4 = 256 = 2^(9-1)
grid3x3+pendant:   2^13 / 2^4 = 512 = 2^(10-1).
```

Every edge occurs in two vertex stars, so `prod_i B_i=I` and `q_G(y)` has even parity for all `4096`, `4096`, and `8192` edge strings. The face-stabilizer cosets map bijectively to the even occupation strings. The fixed pendant occupation makes the odd three-particle grid sector available while total parity remains even; it is an auxiliary boundary convention, not a derived necessity for other encodings.

### B. Exact diagonal-phase equivalence

The three code-sector matrices have dimensions `70`, `84`, and `84`. Their interaction diagonals equal the reference bond counts. After multiplying the encoded hopping matrices by the stabilizer-fibre sizes, their entries are Gaussian integers of maximum modulus `32`, `16`, and `16`.

For each matrix the runner constructs a diagonal `D` with entries in `{1,i,-1,-i}` and verifies entrywise

```text
D^dag H_enc(g) D = H_F(g)
```

for every real `g`. Hence the two supplied finite matrices have equal spectra and equal occupation-basis projector diagonals at every real coupling. The invariance claim is limited to diagonal rephasing; vertex order, neighbour order, encoding choice, and the occupation basis stay fixed inputs. Counts of real versus imaginary entries in a particular representative `D` carry no claim weight because a global phase changes them while leaving the identity unchanged.

### C. Exact free-point occupation probabilities

The runner checks a complete exact orthonormal one-particle eigenbasis and its full eigenvalue multiplicities before using the occupied orbitals. It then evaluates every Slater determinant over `Q(sqrt(2))`, verifies the many-body eigenvector and normalization exactly, and obtains:

- Cube, `N=4`: energy `-6`; probability multiset `0 x12`, `1/64 x56`, `1/16 x2`. The twelve zeros are exactly the six occupied cube faces and six four-vertex patterns that are unions of two disjoint adjacent pairs.
- Grid, three particles with fixed pendant occupation: energy `-4 sqrt(2)`; multiset `0 x8`, `1/256 x12`, `1/128 x32`, `1/64 x20`, `1/32 x8`, `9/256 x4`. The eight zeros are exactly the three rows, three columns, and two diagonals.
- Grid, `N=6`: the same multiset; the eight zeros are the complements of the three-particle zero patterns.

These are exact occupation-basis cancellations for these selected free-fermion states. The runner enumerates the zero sets. Group-representation selection rules and completeness beyond the named sectors and graphs remain outside scope.

### D. Four-coupling numerical witness

At `g in {0,0.5,1,2}`, the encoded and reference occupation statistics agree with `L1 < 1e-12`; their threshold-zero sets at `1e-12` coincide; and the ground eigenvalue is numerically simple. The zero-count sequences are `12/12/12/12` for the cube and `8/4/4/4` for each grid sector.

Across the three nonzero sampled couplings, all twelve cube threshold-zeros persist. Four of the eight grid threshold-zeros persist: `(3,4,5)`, `(1,4,7)`, `(0,4,8)`, and `(2,4,6)` in the three-particle grid sector, and their complements in the six-particle sector. This is a floating-point scan at four parameter values, not an exact all-coupling or larger-system statement.

### E. Constant fibres

Every face-stabilizer coset contains `32`, `16`, and `16` edge strings, respectively, all with unit-modulus code coefficient, and `q_G` is constant on each coset. Thus a code-basis state associated with occupation `n` assigns each edge string in its fibre probability `P(n)/|ker(q_G)|`. At `g=0`, the exact-zero fibres contain `384`, `128`, and `128` edge strings.

### F. Fixed-basis phase structure

Within the selected edge-string sectors, every nonzero elementary hop contribution is exactly `+i` or `-i`: `15360` contributions split `7680/7680` for the cube and `8064` split `4032/4032` for the grid. For each tested edge and every edge string on which that contribution is nonzero,

```text
sign(y) = s_e (-1)^(|y intersect Z(A_ij B_i)|)
```

with one constant `s_e` per edge. The `Z` support lies in `star(i) union star(j)`. It fits one endpoint star on `10` of `12` tested cube edges and `10` of `12` tested grid edges; two edges in each graph require both endpoint stars. The executable census deliberately rejects the stronger one-star statement.

For the fixed matrices, the product of amplitudes around a four-cycle of the configuration graph is negative on `144/444` cube cycles and `80/344` grid cycles, matching the Jordan-Wigner reference. These closed-cycle products are invariant under diagonal rephasing. Counts tied to a chosen spanning tree or representative phase gauge carry no claim weight. No covariance or invariance under a changed neighbour ordering, vertex relabelling, cubic rotation, or encoding is tested.

### G. Separate positive control

Replacing `A_ij` by the bare edge flip `X_e` anticommutes with `16/60` and `12/48` tested `(term, face-generator)` pairs, thereby mapping some code states outside the face-code space. On the separately selected full edge-string sectors of dimensions `2240` and `1344`, a diagonal phase gauge makes every nonzero off-diagonal matrix element `-1`; equivalently, all `7680` and `4032` undirected configuration-graph edges have weight `-1`. Each configuration graph has one connected component.

The standard finite Perron-Frobenius argument therefore gives a simple ground eigenvector with strictly positive components for every real `g` in each of these two declared control matrices. Its pushforward under `q_G` is consequently strictly positive. Numerical checks at the four sampled couplings confirm every occupation probability exceeds `1e-4`. Its evidentiary scope is solely those two fixed matrices; mechanism comparison and other encodings, controls, graphs, sectors, and Hamiltonians remain open.

## Proof-obligation disposition

The finite theorem is conditional on every supplied object listed above. Its executable obligation graph is acyclic:

1. `P0`: supplied graphs, labels/order, edge-qubit basis, operators, code space, dictionary, Hamiltonians, sectors, and boundary conditions.
2. `P1` (`A`): Pauli relations, stabilizer ranks, code dimensions, and incidence-map parity/fibres.
3. `P2` (`B`): exact matrix construction and entrywise diagonal-phase identity.
4. `P3` (`C`): complete one-particle spectrum, exact determinants, normalization, and exhaustive `g=0` classifications.
5. `P4` (`D`): tolerance-qualified four-coupling scan.
6. `P5` (`E`,`F`): fibre and phase/support/flux enumerations with their exact quantifiers.
7. `P6` (`G`): finite control commutators, connected sign gauge, and the imported Perron-Frobenius implication.

The runner closes those finite obligations. The claim boundary stops before these bridges: selection or formation of the encoding/dictionary; identification of graph-edge qubits with physical `Z^3` sites; a framework Record readout; state preparation or dynamics; translation or proper-cubic-rotation covariance; angular momentum, spin, or physical statistics; a gap uniform in system size; periodic or infinite-volume behavior; and classification of other encodings and Hamiltonians.

## Executable claim block

```text
model: fixed-order superfast edge-qubit encoding on cube, grid3x3, and grid3x3+pendant open graphs
dictionary: q_G:F2^E -> even F2^V, q_G(y)_i=sum_(e in star(i)) y_e mod 2; supplied mathematical map
state_spaces: ordinary edge-qubit tensor-product basis; face-loop +1 code space; named fixed-occupation sectors
relations_and_code: R0-R4; face ranks 5/4/4; code dimensions 128/256/512; prod_i B_i=I
gauge_identity: D^dag H_enc(g) D = H_F(g) entrywise for a constructed diagonal fourth-root phase D
g0_cube: energy -6; probabilities 0x12, (1/64)x56, (1/16)x2; classified 12-pattern zero set
g0_grid: energy -4sqrt(2); probabilities 0x8, (1/256)x12, (1/128)x32, (1/64)x20, (1/32)x8, (9/256)x4; rows/columns/diagonals and complements
numerical_scan: g in {0,0.5,1,2}; L1 < 1e-12; threshold-zero counts 12/12/12/12 and 8/4/4/4
fibres: 32/16/16 edge strings per even occupation; exact-zero fibres 384/128/128 at g=0
phase_support: nonzero hop signs obey the stated parity form; support within two endpoint stars; 2 of 12 edges in each tested graph require both stars
flux: negative four-cycle products 144/444 and 80/344 for the fixed matrices
control: two finite connected, sign-gauged matrices have strictly positive ground components for every real g; sampled occupation probabilities >1e-4
outside_scope: physical emergence; framework Record semantics; symmetry selection rules; infinite volume
runner_result: PASS=25 FAIL=0 required
```

## Review record

Hard landing conditions are a fresh runner/cache pair with `PASS=25 FAIL=0`, exact cache SHA binding, a current citation-graph manifest entry, clean conformance/pipeline/strict-audit-lint/changed-evidence gates, an independent finite recomputation, and decisive fail-closed mutations. Independent audit remains a separate lane; this note neither runs an audit worker nor sets or applies an audit verdict.
