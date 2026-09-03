---
claim_id: emergent_fermion_pi_flux_sector_staggered_kinetic_form
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3, carrying one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, with the Kawamoto-Smit link signs eta_1 = 1, eta_2(x) = (-1)^{x_1}, eta_3(x) = (-1)^{x_1+x_2} of the landed staggered kinetic-form clause read on that lattice, and on the named finite blocks and tori only: (T1) with one 2x2x2 cell of coarse sites as the unit cell the hopping has Bloch Hamiltonian H(q) = sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a], Gamma = (Y_1, Z_1 Y_2, Z_1 Z_2 Y_3) and Xi = (X_1, Z_1 X_2, Z_1 Z_2 X_3) a Cl(6) set of anticommuting hermitian involutions, hence H(q)^2 = (6 + 2 sum_a cos q_a) I and tr H(q) = 0 symbolically; the coarse torus L = 4 spectrum is exactly -2sqrt3 x4, -2sqrt2 x12, -2 x12, 0 x8 with its mirror over 64 modes, and L = 6 (216 modes, 0 zero modes) and L = 8 (512 modes, 8 zero modes) reproduce the same Bloch prediction eigenvalue by eigenvalue at 1e-9. (T2) The intertwiner U with U Gamma_a U^dag = +- sigma_a (x) T, T = diag(1,1,-1,-1), and U Xi_a U^dag = I (x) B_a, B = (XX, XY, XZ), exists with entries in Z[i] by Clifford averaging and satisfies U U^dag = 16 I; the 384x64 intertwining system has rank 63 over a prime field with a square root of -1, so each branch nullspace is exactly one-dimensional and U is unique up to a phase; U H(pi + p) U^dag = sum_a sin p_a (sigma_a (x) T) + sum_a (1 - cos p_a)(I (x) B_a) over 300 random p at 1e-12, the taste-mixing term carrying the identity on the spin factor. (T3) Every plaquette holonomy of the KS signs is -1: all 24 coordinate-parity-class and plane combinations, and all 192, 648 and 1536 plaquettes of the coarse tori L = 4, 6, 8; no site gauge carries the plain signs to them, by loop invariance and by exhaustion of all 2^8 sign patterns on the open 2x2x2 coarse block; the fine-mod-2 role pattern of a coarse cell takes exactly 1 value over all coarse sites while the KS sign varies, and the KS sign is a function of the fine coordinates 2v mod 4 over an 8^3 coarse block. (T4) All 24 proper cubic rotations lift to signed permutations with C_R H C_R^T = H on the L = 4 coarse torus, all 576 products close exactly at the 64x64 level and all 576 on the eight zero modes with 0 pairs carrying -1, a genuine representation of O; its characters (E, 8C3, 3C2, 6C4, 6C2') = (8, 2, 0, 4, 0) decompose as 2 A1 + 2 T1 against a character table checked orthonormal in the runner; in the B basis every lift factorises as a 2x2 spin factor times a 4x4 taste factor at singular-value ratio 9e-17, both factors carrying one and the same sign cocycle with 208 of the 576 pairs at -1 under the runner's determinant normalisation, and that cocycle is not a coboundary, so each factor is individually projective while the product is genuine. (T5) epsilon = Z_1 Z_2 Z_3 anticommutes with all six generators, hence with H(q) at every q, and U epsilon U^dag = I (x) (+- T B_1 B_2 B_3) on the two branches and never +- I (x) T. (T6) (B_j - B_i) = 2 on exactly the legal steps, so the encoded hop T_ji = (i/2) A_ji (B_j - B_i) acts there as i A_ji, and the ordered product of four encoded hops around a coarse face equals the face stabilizer S_f exactly with its Z4 phase on 6, 36, 81 and 192 faces of the open 2x2x2, the open 3x3x3 and the tori 3^3 and 4^3; every F2 relation among the S_f has ordered product exactly +I on all twelve blocks and tori tested, so the sector S_f = -1 for every f is consistent exactly when every relation has even support, which holds on every open block and on an L1xL2xL3 coarse torus exactly when every pairwise product L_a L_b is even, verified against an independent F2 solve for a pi-flux edge sign field over all 2424 faces of the twelve; the sign field eta' read off that sector with no input from KS has holonomy -1 on every plaquette and admits a gauge witness s(v) carrying it to the KS signs on the open 2x2x2, 3x3x3 and 4x4x4 blocks and the 4x4x4 coarse torus, with 4, 7, 32 and 24 sites at s = -1, and the one-particle spectra of eta' and of KS agree there at 1e-9. (T7) On the open 2x2x2 coarse cube with 12 edge qubits and dimension 4096, prod_i B_i = +I, the six face stabilizers have F2 rank 5, the joint S_f = -1 eigenspace is one-dimensional on each of the 128 B-configurations giving 128 = 2^(V-1) states, and the encoded hopping restricted there matches the even-parity many-body spectrum of sum_ij eta'_ij c_i^dag c_j on all 128 levels at 1e-13. Nothing here is derived from any axiom, no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/emergent_fermion_pi_flux_sector_staggered_kinetic_form_check_2026_09_02.py
---

# The staggered kinetic form is the other flux sector of the emergent fermion's own gauge structure

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/emergent_fermion_pi_flux_sector_staggered_kinetic_form_check_2026_09_02.py`](../scripts/emergent_fermion_pi_flux_sector_staggered_kinetic_form_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/emergent_fermion_pi_flux_sector_staggered_kinetic_form_check_2026_09_02.txt`](../logs/runner-cache/emergent_fermion_pi_flux_sector_staggered_kinetic_form_check_2026_09_02.txt)
**Parents:** none. Every premise used below is declared in this note.

The framework's landed staggered kinetic clause fixes a sign on every nearest-neighbour link and calls the resulting sign field unique as a local `Z2` gauge class. A
separate construction supplies a fermion on the coarse sublattice `2Z^3`, one mode per coarse vertex, with a `Z2` gauge structure of its own whose gauge-invariant
content on a face is a face stabilizer of eigenvalue `+-1`. The question this note answers is whether those two sign structures are the same object. They are:
transport of one encoded excitation around a coarse face equals that face's stabilizer exactly, phase included, so the staggered sign field is the sector in which
every face stabilizer is `-1`, and the plain field is the sector in which every one is `+1`.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems identifying the landed staggered kinetic sign field with the all-minus face-stabilizer sector of the coarse-lattice emergent fermion, together with the exact Clifford, spin-taste, point-group and chirality structure of that kinetic form. Every statement is symbolic, integer, Z[i], F2/Z4 or exhaustive; the tagged numerical items are cross-checks of statements already established exactly."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: which flux sector a dynamical clause would select."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the seven statements below, exactly the runner's check groups `A`-`G`. Groups `A`-`C`, `E` and the structural content of `F` are
exact -- symbolic identities in `sympy`, integer and `Z[i]` matrix arithmetic at zero tolerance, rank over a finite field, `F2` and `Z4` symplectic bit arithmetic,
exhaustive enumeration -- and the items tagged `[numerical]` are floating-point cross-checks, at the stated tolerance, of what those groups establish.

1. `T1` (`A`). The kinetic form: a `Cl(6)` operator on the eight-site coarse cell, with its exact square, trace and torus spectra.
2. `T2` (`B`). The spin-taste split: an exact intertwiner, unique up to a phase, taking the operator to `sum sin p (sigma (x) T) + sum (1 - cos p)(I (x) B)`.
3. `T3` (`C`). The sign field is a flux class, not a local gauge choice, and is a function of the fine coordinates mod `4`.
4. `T4` (`D`). The proper cubic group on the eight zero modes is the genuine representation `2 A1 + 2 T1`, factorising into individually projective factors.
5. `T5` (`E`). The chirality grading is `I (x) (+- T B_1 B_2 B_3)`, distinct from the taste pseudoscalar.
6. `T6` (`F`). Face transport equals the face stabilizer, the all-`(-1)` sector exists exactly when at most one coarse period is odd, and in it the encoded hopping
   is in the staggered local gauge class, with a witness and the same one-particle spectrum.
7. `T7` (`G`). The many-body cross-check on the open `2x2x2` coarse cube.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the Dirac-Kahler spin-taste basis and the
character table of `O` are standard methodology; every object is redeclared here and the runner recomputes every statement, the table's orthonormality included. No
observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): the role pattern, the coarse
  sublattice `2Z^3` and the superfast encoding on it. Pointer only; the encoding is redeclared below and recomputed by this runner.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`: the kinetic-form clause and the corner-structure clause quoted below.
- `CHIRAL_CONTENT_IS_THE_EPSILON_D_CHIRALITY_IMPORT_DISTINCT_FROM_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md`: the chirality-grading row quoted below.
- `STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md`: the labelling no-go, cited as a pointer only.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting". This note cites none of their grades and adopts no hypothesis.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has
algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." **Record**:
"Records form", "a record locks exactly one admissible local possibility", "records are permanent", "Only records are readable."

The landed kinetic clause under test reads, verbatim:

> **Kinetic-form clause.** Within the declared kinetic class (the naive-Dirac kinetic form on nearest-neighbor `Z^3` links, made
> compatible with the matter-statistics clause by site-local spin diagonalization), the kinetic operator is the staggered operator
> `D = (1/2) Σ_{x,μ} η_μ(x) (χ̄_{x+μ̂} χ_x − χ̄_x χ_{x+μ̂})` with the Kawamoto-Smit phases `η_1 = 1, η_2(x) = (−1)^{x_1},
> η_3(x) = (−1)^{x_1+x_2}`, unique as a local Z2 gauge class.

and its corner-structure clause reads:

> **Corner-structure clause.** The free staggered operator has the 8-element BZ-corner (taste-cube) doubler set, decomposing uniquely
> by Hamming weight as `1 + 3 + 3 + 1`; the hw=1 triplet carries an exact irreducible `M_3(C)` algebra (translations + `C_3[111]`)
> with no proper exact quotient.

Everything below reads that sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex. Composition is **ordinary** throughout: the algebra of a
region is the tensor product of its sites' algebras and no graded clause is used anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the KS sign field
on it, the eight-site cell, the superfast encoding, the encoded hop and the face stabilizers. `P1` (`A`) is the `Cl(6)` form, its square and trace and the torus
spectra; `P2` (`B`) the intertwiner, its uniqueness and the spin-taste Hamiltonian; `P3` (`C`) the flux class and the mod-`4` structure of the sign; `P4` (`D`) the
cubic lift, its closure, characters and factorisation; `P5` (`E`) the chirality grading and its image; `P6` (`F`) face transport, the sector's existence condition,
the induced sign field and its gauge witness; `P7` (`G`) the many-body cross-check. The strongest supported scope is precisely `P0`-`P7`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_ax` sits at the fine site `2v + e_ax`. The
**KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`, the clause's phases read in coarse coordinates.
The **plain sign** is `+1` on every bond.

The **cell** is one `2x2x2` block of coarse vertices, eight modes, so the Bloch Hamiltonian of the KS hopping is an `8x8` matrix `H(q)`. The **encoding** is the
Bravyi-Kitaev superfast encoding on the coarse lattice, code qubits on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`.

```text
Gamma = (Y_1, Z_1 Y_2, Z_1 Z_2 Y_3),  Xi = (X_1, Z_1 X_2, Z_1 Z_2 X_3),  epsilon = Z_1 Z_2 Z_3,  T = diag(1,1,-1,-1),  B = (XX, XY, XZ)
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_i  = product of the Z's on the edges incident to i,   S_f = the ordered product of the four A's around a coarse face f
```

`B_i = -1` marks the excitation; the **encoded hop** across `(i, j)` is `T_ji = (i/2) A_ji (B_j - B_i)`. A step is **legal** on a configuration when its source is
occupied and its target empty. A **flux sector** is a choice of eigenvalue `+-1` for every `S_f` that is consistent with the `F2` relations among them.

## Theorem 1 -- the kinetic form is a Clifford operator with an exact spectrum

**Conclusion.** On the coarse lattice with the KS signs, with one `2x2x2` cell as unit cell:

1. `Gamma_x, Gamma_y, Gamma_z, Xi_x, Xi_y, Xi_z` are six mutually anticommuting hermitian involutions -- a `Cl(6)` set -- and the Bloch block built from the hopping
   rules equals `H(q) = sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a]` identically in `q`.
2. Hence `H(q)^2 = (6 + 2 sum_a cos q_a) I` and `tr H(q) = 0`, so `E(q) = +- sqrt(6 + 2 sum_a cos q_a)`, each eigenvalue fourfold.
3. On the coarse torus `L = 4`, `64` modes, the spectrum is exactly `-2sqrt3` with multiplicity `4`, `-2sqrt2` with `12`, `-2` with `12`, `0` with `8`, and its
   mirror. On `L = 6` (`216` modes) and `L = 8` (`512` modes) the real-space spectra reproduce the same Bloch prediction eigenvalue by eigenvalue, with `0` and `8`
   zero modes.

**Proof.** Item 1 is an exact matrix identity over `Z[i]` for the Clifford relations and a symbolic identity in the three momenta for the closed form, expanded term
by term against the hopping rules. Item 2 follows because a real combination `sum_k c_k M_k` of anticommuting involutions squares to `(sum_k c_k^2) I`, and here
`sum_a [(1 + cos q_a)^2 + sin^2 q_a] = 6 + 2 sum_a cos q_a`; the `8x8` product and the trace are also verified symbolically, and item 3 evaluates item 2 at the
allowed cell momenta with exact surds. Items 1 and 2 exact; item 3 exact at `L = 4` and `[numerical, 1e-9]` at `L = 6, 8`.

**Reading, not theorem.** The eight modes of one small cube carry an algebra with six independent anticommuting directions. That is exactly the algebra a Dirac
operator needs, and it is here without being put in by hand: it is what the alternating signs on the links leave behind.

## Theorem 2 -- an exact spin-taste split, with the mixing term a spin singlet

**Conclusion.** With `T = diag(1,1,-1,-1)` and `B = (XX, XY, XZ)`:

1. `sigma_a (x) T` and `I (x) B_a` are a `Cl(6)` set, and Clifford averaging produces `U` with entries in `Z[i]` and `U U^dag = 16 I`, satisfying
   `U Gamma_a U^dag = +- sigma_a (x) T` and `U Xi_a U^dag = I (x) B_a` exactly, one `U` for each sign branch.
2. The `384x64` linear system of the intertwining equations has rank `63` over a prime field carrying a square root of `-1`, so its nullity over `C` is at most `1`;
   the exact `U` is a nonzero solution, so the branch nullspace is exactly one-dimensional and `U` is unique up to a phase.
3. `U H(pi + p) U^dag = sum_a sin p_a (sigma_a (x) T) + sum_a (1 - cos p_a)(I (x) B_a)`. The first sum is the free Dirac operator in the spin factor; the second
   carries the identity on the spin factor, so the taste-mixing term is a spin singlet.

**Proof.** Item 1 uses `U = sum_S N_S M G_S^dag` over the `64` Clifford words, which intertwines because both sets satisfy the same relations with the same structure
constants, with the elementary `M` that makes `U` invertible; all entries are sums of at most `64` terms from `{0, +-1, +-i}`, checked at zero tolerance. Item 2 uses
that rank can only drop under reduction to a finite field, so rank `63` there forces rank at least `63` over `C`; irreducibility of `Cl(6)_C = M_8(C)` on `C^8` is
the structural reason. Item 3 follows from item 1 at `q = pi + p`, checked `[numerical, 1e-12]` over `300` random momenta.

**Reading, not theorem.** One `2x2x2` cell holds a two-component spin and a four-component taste label, and the operator splits along that seam without remainder.
What mixes the taste labels does not touch the spin.

## Theorem 3 -- the sign is a flux class, and it lives on the fine coordinates mod 4

**Conclusion.**

1. Every plaquette holonomy of the KS signs is `-1`: all `24` combinations of coordinate-parity class and plane, and all `192`, `648` and `1536` plaquettes of the
   coarse tori `L = 4, 6, 8`.
2. No site relabelling `c_v -> s(v) c_v` carries the plain signs to the KS signs. Each `s(v)` occurs twice in any closed loop, so every loop holonomy is gauge
   invariant; plain gives `+1` and KS gives `-1` on every plaquette. Exhaustion of all `2^8` sign patterns on the open `2x2x2` coarse block finds none.
3. Every coarse site `2v` is a fine corner and the fine-mod-`2` role pattern of its cell takes exactly `1` value over all coarse sites, so any function of that
   pattern is constant, while the KS sign is not. The KS sign is instead a function of the fine coordinates `2v mod 4`, verified over an `8^3` coarse block.

**Proof.** Item 1 is a symbolic evaluation over the eight parity classes and three planes, then an exhaustive plaquette sweep on the three tori. Item 2 is the
loop-invariance argument with an exhaustive `2^8` search. Item 3 enumerates the role patterns of every coarse cell and the sign at every coarse site of an `8^3`
block against the four-row `mod 4` table the runner prints. All exact.

**Reading, not theorem.** A sign on each link is not itself meaningful, because a relabelling of the modes can move it around. What survives relabelling is the
product around a small square. For the staggered field that product is minus one on every square, and no relabelling of the plain field can reach it.

## Theorem 4 -- the proper cubic group on the eight zero modes

**Conclusion.** On the `L = 4` coarse torus:

1. All `24` proper cubic rotations lift to signed permutations with `C_R H C_R^T = H`, each orthogonal with entries in `{0, +1, -1}` and one nonzero entry per row
   and column.
2. All `576` products close on the nose, `C_R C_R' = C_{RR'}`, both at the `64x64` level and on the eight zero modes: a genuine representation of `O`, not
   projective.
3. Its characters `(E, 8C3, 3C2, 6C4, 6C2') = (8, 2, 0, 4, 0)` decompose as `2 A1 + 2 T1` against a character table of `O` whose orthonormality the runner checks.
4. In the `B` basis every lift factorises as a `2x2` spin factor times a `4x4` taste factor. With determinant-normalised factors the two carry one and the same sign
   cocycle, `208` of the `576` pairs at `-1` under the runner's normalisation, and that cocycle is not a coboundary: each factor is individually projective while the
   product is genuine.

**Proof.** Item 1 solves for each lift's signs by breadth-first propagation, then verifies the symmetry and the orthogonality directly. Item 2 compares all `576`
products against the composed rotation with both signs. Item 3 projects onto the exact kernel basis at the corner momentum, checked orthonormal and annihilated by
`H`, and applies the orthogonality relations. Item 4 is a rank-one reshaping test, `[numerical, singular-value ratio 9e-17]`, and an `F2` coboundary test on the sign
cocycle; the count of `-1` pairs depends on the branch chosen per factor, the cocycle **class** does not.

**Reading, not theorem.** The landed clause grades the eight corner states by Hamming weight, `1 + 3 + 3 + 1`. Under the rotations themselves those eight states
carry two invariant directions and two vector triples. The vector triples are the `3`s of the grading; the two invariants are the `1`s.

## Theorem 5 -- the chirality grading is not the pseudoscalar

**Conclusion.** `epsilon = Z_1 Z_2 Z_3` anticommutes with all six `Cl(6)` generators, hence with `H(q)` at every momentum, and on the two branches
`U epsilon U^dag = I (x) (+- T B_1 B_2 B_3)` -- never `+- I (x) T`.

**Proof.** Both statements are exact matrix identities over `Z[i]`, and the anticommutation with `H(q)` follows from the anticommutation with each generator.

This is the coarse-lattice form of the landed narrow theorem's row

> | `epsilon(x)=(-1)^(x+y+z)` | spatial `Z^3` site grading | even | staggered chirality grading; anticommutes with the tested nearest-neighbor Dirac hop |

and is consistent with its conclusion that "`omega = sign(Vandermonde) = epsilon` is not a valid identity": the grading and the pseudoscalar of the taste factor are
different operators here too.

## Theorem 6 -- the staggered field is the all-minus face sector

**Conclusion.** For the superfast encoding on the coarse lattice:

1. `(B_j - B_i) = 2` on exactly the legal steps, so the encoded hop `T_ji = (i/2) A_ji (B_j - B_i)` acts there as `i A_ji`, and the ordered product of four encoded
   hops around a coarse face equals `S_f` exactly, `Z4` phase `i^4 = +1` included: `6` faces on the open `2x2x2`, `36` on the open `3x3x3`, `81` on the torus `3^3`
   and `192` on the torus `4^3`.
2. Every `F2` relation among the `S_f` has ordered product exactly `+I`, on all twelve blocks and tori tested. So the sector `S_f = -1` for every `f` is consistent
   exactly when every relation has even support.
3. That holds on every open block, and on an `L1xL2xL3` coarse torus exactly when every pairwise product `L_a L_b` is even -- at most one odd period. Over the nine
   tori `3^3`, `3x3x4`, `3x4x5`, `4^3`, `4x4x5`, `4x4x6`, `4x5x6`, `5^3`, `5x5x6` this reproduces an independent `F2` solve for a `pi`-flux edge sign field.
4. The sign field `eta'` read off that sector -- spanning-tree gauge fixing, then fundamental-cycle transport, with no input from the KS phases -- has holonomy `-1`
   on every plaquette, and a gauge witness `s(v)` carries it to the KS signs on the open `2x2x2`, `3x3x3` and `4x4x4` blocks and the `4x4x4` coarse torus, with `4`,
   `7`, `32` and `24` sites at `s = -1`. The one-particle spectra of `eta'` and of KS agree on all four.

**Proof.** Item 1 is a `Z4` symplectic identity checked face by face, with an exact integer evaluation of the diagonal `(B_j - B_i)` over all `4096` configurations
of the open `2x2x2` cube: it is `2` on the legal steps, `-2` on their reverses and `0` elsewhere, so a legal traversal contributes `i` per step and `i^4 = +1` around
a face, while any other configuration is annihilated at some step. Item 2 computes the `F2` nullspace of the face-to-edge incidence and evaluates the ordered product
of each relation. Item 3 reads the parity of every relation's support and, independently, solves the face equations "the four edge signs sum to `1`". Item 4
expresses each fundamental-cycle transport operator in the stabilizer generators, reads its residual `Z4` phase -- real in every case -- and multiplies in the sector
values; the witness is found by breadth-first propagation and verified edge by edge. All exact but the spectra, `[numerical, 1e-9]`.

**Reading, not theorem.** Carry the particle once around a small square and it comes back with the square's own sign. Choosing that sign to be minus on every square
is the framework's staggered kinetic form; choosing plus is the plain one. The law as written does not choose.

## Theorem 7 -- the many-body cross-check

**Conclusion.** On the open `2x2x2` coarse cube, `12` edge qubits, dimension `4096`: `prod_i B_i = +I`, the six face stabilizers have `F2` rank `5`, the joint
`S_f = -1` eigenspace is one-dimensional on each of the `128` `B`-configurations, `128 = 2^(V-1)` states in all -- the even-parity Fock space of the eight coarse
modes -- and the encoded hopping restricted there is hermitian with its `128` levels equal to the even-parity spectrum of `sum_ij eta'_ij c_i^dag c_j`.

**Proof.** The stabilizer projection is applied by sparse Pauli action on state vectors, never by forming a dense operator; the sector states are checked to be `-1`
eigenvectors of all six faces, and the restricted hopping is compared against the free-fermion prediction built from the one-particle spectrum of `eta'`. Exact for
the dimensions and the rank, `[numerical, 1e-13]` for the level-by-level comparison.

## Corollary -- what this says about the framework's kinetic form

Within the setting declared above, and on the finite clusters named:

1. The framework's staggered kinetic form on the coarse lattice is the same one-qubit-per-site law as the plain form, read in the other flux sector of the fermion's
   own `Z2` gauge structure: the two differ by the eigenvalue of one gauge-invariant quantity per face, and by nothing else.
2. The law as written attaches no coefficient to any face term, and the role-pattern note states its own scope in the same terms: "The dynamical clause. This note
   gives a law and its zero-energy configurations, not a tick." So the two sectors are a free choice under the law as written; a face term `-J sum_f S_f` with
   negative `J` would select the staggered sector, and no such term is supplied by anything quoted here.
3. The staggered gate's residual "**Spin-statistics support tier.** Substep 1's bosonic exclusion rests on the spin-statistics support input", whose "full
   spin-statistics statement remains a support-tier authority pending its own audit chain", is supplied by construction on the coarse lattice: the modes of Theorem
   6 belong to an encoding whose excitations already exchange with `-1`. Whether that changes the residual's status is an audit question, not one this note answers.
4. The corner content sharpens: the eight zero modes carry `2 A1 + 2 T1` under the proper rotations, refining the landed `1 + 3 + 3 + 1` Hamming grading into
   representation content. No corner is thereby labelled; see the interfaces below.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The coarse lattice, the encoding and the sign fields are declared objects, and the theorems are about them.
- No update rule, formation site, formation rate, coupling, or absolute unit appears. No dynamical clause is supplied, and no flux sector is selected.
- No corner of the taste cube is identified with any named species. `STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md` is a pointer only.

## Interfaces named for other lanes, not moved here

- **The mod-4 structure versus the role pattern.** The KS sign is a function of the fine coordinates `mod 4`; the role pattern of PR #7834 has period `(4, 2, 2)`
  along one axis. Both carry a period of `4`. They are **not** shown here to be the same object, and a lane wanting them identified must supply that.
- **The many-body symmetry content.** Theorem 4 is the one-particle point-group content. What the proper rotations do to the many-body states of the encoded model,
  and whether the projective factors have a many-body shadow, is untouched.
- **The carrier locus of the labelling lane.** Theorem 4 gives representation content on the eight zero modes, not a labelled bijection; the no-go note states what
  is not derivable and nothing here narrows or widens it.
- **The choice of flux sector.** Which sector a dynamical clause selects is a science question this note leaves open, and Corollary item 2 states exactly what such a
  clause would have to supply.

## Remaining live routes

1. Larger blocks and other geometries. The twelve blocks and tori named are what is proved; nothing is claimed beyond them.
2. Interacting terms. Only free hopping is compared; a four-fermion term could distinguish the sectors differently.
3. Mass and species. One spinless `Z2`-charged mode per coarse vertex is what the encoding supplies; no mass term, second species, or coupling appears.
4. The odd-parity sector. The encoded model carries `prod_i B_i = +I` and so has no odd-parity states; the bare staggered fermion has them.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one fermionic mode per coarse vertex, BK superfast encoding on it; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
sign_fields_and_cell_algebra: KS eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}, plain +1 on every bond; Gamma = (Y_1, Z_1 Y_2, Z_1 Z_2 Y_3), Xi = (X_1, Z_1 X_2, Z_1 Z_2 X_3), epsilon = Z_1 Z_2 Z_3, T = diag(1,1,-1,-1), B = (XX, XY, XZ); H(q) = sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a] a Cl(6) form with H^2 = (6 + 2 sum cos q_a) I and tr H = 0
spectra: L=4 exact -2sqrt3 x4, -2sqrt2 x12, -2 x12, 0 x8 and mirror over 64 modes; L=6 216 modes 0 zero modes; L=8 512 modes 8 zero modes
intertwiner_and_spin_taste: U with Z[i] entries, U U^dag = 16 I, from a 384x64 system of rank 63, nullity 1 per branch, unique up to a phase; U H(pi+p) U^dag = sum sin p_a (sigma_a x T) + sum (1 - cos p_a)(I x B_a), the taste-mixing term a spin singlet
flux_class_and_mod4: all 24 parity-class/plane holonomies -1; 192, 648, 1536 plaquettes of L = 4, 6, 8 all -1; no site gauge from plain to KS by 2^8 exhaustion; 1 fine-mod-2 role pattern over all coarse cells; KS sign a function of 2v mod 4 on an 8^3 block
cubic_group_and_factorisation: 24 signed-permutation lifts; 576 + 576 products exact, 0 with -1; characters (8, 2, 0, 4, 0) = 2 A1 + 2 T1; spin (x) taste at singular-value ratio 9e-17, one shared sign cocycle, 208 of 576 pairs -1, not a coboundary
chirality: epsilon anticommutes with all six generators and with H(q); U epsilon U^dag = I (x) (+- T B_1 B_2 B_3), never +- I (x) T
face_transport: (B_j - B_i) = 2 on exactly the legal steps; four-hop product = S_f exactly with Z4 phase on 6, 36, 81, 192 faces
relations_and_sector: every F2 relation among the S_f has ordered product +I on all 12 blocks and tori; sector exists on open blocks always and on an L1xL2xL3 torus iff every pairwise L_a L_b is even; independent F2 solve agrees over all 2424 faces
gauge_witness: eta' holonomy -1 everywhere; witness to KS on open 2x2x2, 3x3x3, 4x4x4 and torus 4x4x4 with 4, 7, 32, 24 minus sites; spectra equal
many_body: open 2x2x2, 12 edge qubits, dim 4096; prod B = +I; face rank 5; 128 B-configurations, 128 = 2^(V-1) sector states; levels match to 1e-13
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=23 FAIL=0
```

## Proof boundary

Everything is proved on the **coarse** lattice `2Z^3` only. Nothing is claimed for the fine lattice `Z^3`, for infinite lattices, or beyond the open `2x2x2`,
`3x3x3`, `4x4x4` blocks and the tori `3^3`, `3x3x4`, `3x4x5`, `4^3`, `4x4x5`, `4x4x6`, `4x5x6`, `5^3`, `5x5x6` named above; tori with a side of length `2` are
excluded as multigraphs, on which `A_ij` is not determined by its endpoint pair.

The content is **sign classes and free-hopping spectra**, not dynamics. No coefficient, coupling, mass, rate or unit appears; the statement that a face term would
select a sector names what such a term would do and supplies none. Nothing here is derived from the four axioms: the law is a declared object.

The identification of the encoded hopping with the staggered kinetic form is up to a **site relabelling**, which is exactly what a local `Z2` gauge class means; the
witness `s(v)` is exhibited on four blocks and is not claimed on any other. The encoded model carries `prod_i B_i = +I`, so it has no odd-parity sector, which the
bare staggered fermion does have; every many-body comparison in Theorem 7 is inside the even sector for that reason.

Theorem 4's count of `-1` pairs is normalisation-dependent -- the determinant normalisation fixes each factor only up to a sign -- while the statement that the
cocycle is not a coboundary is not. Only the latter is used.

## Review record

An honest auditor should come away with: one identification, proved on named finite clusters, between the framework's staggered sign field on the coarse lattice and
the all-minus face-stabilizer sector of a fermion construction already on the table; the exact Clifford, spin-taste, point-group and chirality structure of that
kinetic form; one existence condition, at most one odd coarse period, coinciding with the periodicity condition of the phases themselves; and one thing deliberately
not decided -- which sector a dynamical clause would pick. The one normalisation-dependent number is flagged in the proof boundary, and the labelling lane's no-go is
cited without being used.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the five context notes in
"Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at
`PASS=23 FAIL=0`, runtime under the declared `300` seconds, stdout under `5500` characters, a current zero-dependency citation-manifest entry, and passing
pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
