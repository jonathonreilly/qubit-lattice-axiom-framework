---
claim_id: corner_eigenvector_two_mode_spectral_condition_not_general
claim_type: bounded_theorem
claim_scope: "On TWO finite subgraphs of the cubic lattice with qubits on the EDGE sites, ordinary composition, the superfast encoding and the corner parity dictionary n_v = (1 - B_v)/2, in the staggered (pi-flux) Kawamoto-Smit sector H = -sum_e eta_e T_e at half filling -- the 2x2x2 cube (8 corners, 12 edge sites, 6 faces, every corner degree 3, code space 128, sea E = -4 sqrt 3) and the 2x2x3 slab of two stacked cubes open in z (12 corners, 20 edge sites, 11 faces, corner degrees 3 and 4, code space 2048, record space 2^20 = 1048576, sea E = -(8 + 2 sqrt 2)), with the 2x2x3 slab periodic in z and the two 2x2x4 slabs carried at the one-particle level only -- and for the STIPULATED unit of record formation of PR #7900, in which the records of a corner's own record set star(v) form together as one event with the odds of the pre-record object: (T1) the record layer factors out EXACTLY and for any degree, P_w |sea> = 2^-(d-1) (sum_T eps_T Z_T) Pi_{n_v} |sea> with Pi_{n_v} = (1 + b_v B_v)/2, because a face through v carries exactly two of star(v)'s edges so the only logical Z_T are I and B_v, and every Z_T commutes with H_R; the residual of that identity is 0.0e+00 / 8.7e-19 and every outcome's weight is exactly 2^-d, so the question is purely fermionic. (T2) The conditioned sea is an H_R eigenvector IFF the corner's site vector satisfies h e_v in span(e_v, P_W e_v) -- e_v a superposition of exactly TWO one-particle eigenmodes of h, one occupied and one empty -- and the pi-flux cube satisfies it because both bands are flat (h^2 = 3I), giving eigenvalue -(N-1) sqrt 3 = -5.196152423 at all 8 corners x 8 outcomes (residual 1.9e-14) with overlap 1.000000000 with the non-degenerate H_R ground state of that record sector. (T3) It is NOT general: on the 2x2x3 slab it holds exactly at the four degree-4 middle-layer corners (16/16 outcomes, residual 2.9e-13, <H_R> = -(6 + 2 sqrt 2)) and at the 14-edge closed star of one (15360/15360, 2.7e-15), and FAILS at all eight degree-3 corners (0.207107 = (sqrt 2 - 1)/2), at a single edge (0.6124), at a face (0.9440) and at a degree-3 closed star (up to 0.4460); the V x V criterion predicts every verdict in advance and its invariance residual 2.071e-01 matches the many-body failure to three digits; the PERIODIC 2x2x3 slab has every corner of degree 4 and fails at every corner, so the condition is spectral and not a matter of degree. (T4) A staggered mass preserves it exactly (it anticommutes with the bipartite h, keeping h^2 = (3 + m^2) I flat; residual 1.5e-15), while two DECLARED FIXED hop-sign-flip tables, a DECLARED FIXED on-site table at two scales and the zero-flux sector break it at 0.023 to 0.707, every one-particle verdict reproduced many-body. (T5) The two-corner marginal test on two disjoint stars is BLIND -- total variation 1e-14 whether the property holds or fails -- because the sea's joint record law there is exactly uniform (<B_v> = 0, <B_v B_w> = 0 on non-adjacent pairs), while the full 2^20 record law discriminates (1.9e-15 where it holds against 0.020 / 0.087 at tau = 0.5 / 2.0 where it fails, the propagated object leaving the sea's Z-support by 16384 patterns); the bincount variance form of the residual identity is named as a cancellation trap with a ~1e-6 floor and every headline residual is computed directly. This note NARROWS a result of the same day and the same session -- PR #7900's corner eigenvector mechanism -- to its exact condition; it forecloses no unit, no rule and no neighbourhood tick, states nothing about what the framework's tick is, and derives nothing from any axiom. No seeds anywhere: the Lanczos start vector and every perturbation are explicit fixed tables written out in the runner."
upstream_dependencies: []
runner: scripts/corner_eigenvector_two_mode_spectral_condition_check_2026_09_03.py
---

# The corner eigenvector property is a two-mode spectral condition: exact on flat bands, not general

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/corner_eigenvector_two_mode_spectral_condition_check_2026_09_03.py`](../scripts/corner_eigenvector_two_mode_spectral_condition_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/corner_eigenvector_two_mode_spectral_condition_check_2026_09_03.txt`](../logs/runner-cache/corner_eigenvector_two_mode_spectral_condition_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

`JOINT_FORMATION_ON_A_CORNERS_RECORD_SET_KEEPS_THE_SEAS_ZEROS_UNDER_THE_UNITARY_TICK_..._2026-09-03.md` (open PR #7900) let the three records at one corner of the `2x2x2` cube **form
together**, as one event, and found something sharp at its `T3`: *"After a corner's record set forms jointly, the Born-conditioned sea already lies in the restricted ground space
(`G = <psi|Pi_0|psi> = 1.000000000`, `deg = 1`) and is an **exact eigenvector of `H_R`** at `8` of `8` outcomes."* On the strength of that it offered, as a candidate wording and not as
axiom text, the sentence *"Records form together on a corner's record set; between formations the law runs on."* This note asks the two questions that result leaves open -- **why** does
a jointly formed corner set leave the sea an eigenvector, and **does it generalise** -- and answers both on the same cluster and on one cluster larger. The mechanism turns out to be
exact and two-step, and the property turns out to be **narrow**: it is a condition on the one-particle spectrum at that corner, and one cube taller it fails at two thirds of the corners
by a fifth of the norm. This note therefore **narrows a result of the same day and the same session to its exact condition, and the narrowing is the point.** It forecloses nothing: the
condition it supplies is a *test*, cheap enough to run on any lattice, and neighbourhood ticks remain entirely open below.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-sector statements on two named clusters -- the 2^12 record space of the 2x2x2 cube and the 2^20 record space of the 2x2x3 slab, in the staggered sector at half filling -- for the stipulated unit of record formation of PR #7900. T1 is exact symplectic Pauli and F2 algebra: which subsets of a corner's star are logical, and that they commute with the restricted Hamiltonian. T2's criterion is an exact two-line linear-algebra statement about the one-particle matrix; its verification, and everything in T3, T4 and T5, are deterministic double-precision evaluations of exactly specified quantities at the stated thresholds, from sparse Pauli-string application and Lanczos on the conserved half-filling sector -- no dense object above 4096 x 4096 is formed anywhere. Nothing is sampled, there is no seed anywhere in the runner, and every perturbation is an explicit fixed table written out in the file."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Carry the V x V two-mode screen into the tick lane: any candidate cluster and flux sector can now be tested for the corner eigenvector property by one eigendecomposition of the one-particle matrix, before any many-body run, and the tick lane's next computations should report the full record law rather than a two-corner marginal, which T5 shows is blind to the failure."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five theorems below, exactly the runner's check groups `A`-`F`: the setting and the two clusters (`A`); `T1` the record layer (`B`); `T2` the
criterion and the cube (`C`); `T3` the slab (`D`); `T4` robustness (`E`); `T5` the blind marginal (`F`). Groups `A1`, `A2` and `B1` are **exact**: symplectic Pauli algebra with phases
mod `4`, integer graph combinatorics, and `F2` parity arithmetic on the face masks. The rest are **deterministic double-precision evaluations** of exactly specified quantities at the
stated thresholds. Nothing is sampled: the Lanczos start vector is the fixed deterministic vector `cos(0.7 i + 0.3) + i cos(1.3 i + 1.1)` projected into the code space, written out in
the runner, and every perturbation of `T4` is an explicit fixed table -- `SIGN_FLIPS` and `ONSITE` -- also written out there. There is **no seed anywhere** and no Monte Carlo section.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggered link signs, Slater determinants, Lueders conditioning, Lanczos and
the total-variation distance are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's relations included. No observational
value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight: `JOINT_FORMATION_ON_A_CORNERS_RECORD_SET_KEEPS_THE_SEAS_ZEROS_...
_2026-09-03.md` (open PR #7900 -- the corner result whose exact condition this note supplies, the source of the stipulated unit of formation, and the source of the candidate formation
sentence this note narrows); `A_RELAXATION_TICK_IS_WELL_POSED_AND_LOSES_THE_SEAS_RECORD_STATISTICS_..._2026-09-03.md` (open PR #7895 -- the site-wise tick and the restriction identity
`P_S H P_S = H_R`); `RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_..._2026-09-03.md` (PR #7883 -- the sea as a Slater determinant, and the same `eta_ks`); PR #7888 (the
flat pi-flux bands, `h^2 = 3I` on the cube); `A_RECORD_NATIVE_STAGGERED_MASS_..._2026-09-03.md` (PR #7890 -- the staggered mass that anticommutes with `h`); and
`MINIMAL_AXIOMS_2026-06-29.md`, from which the axioms in "Setting" are quoted verbatim. This note cites no grade of any and consumes no ledger row.

## Setting

The four framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site." "No site is privileged." **The lattice is physical**; the cube and the slab below are finite open subgraphs of it,
drawn as graphs, so "edge site", "corner", "face" and "degree" have their graph meanings. **Qubit / Site Possibility**: "Each site has a domain of local possibilities." "The full
one-site possibility domain has algebraic presentation `M_2(C)`."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the
probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Reading note (2), interpretive and non-governing, is quoted with it
because it is what makes this note's subject a free choice: "Read with Record, the distribution concerns which possibility a forming record locks, conditional on formation at that site;
**it does not supply the formation site, probability, or rate.**"

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent."
"Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded clause is used anywhere. The
**record ontology** is used as declared: a record at an edge site **registers** a value there; it does not report one the site already carried. Because the axioms supply no formation
site and no rate, the **unit** in which records form is a free choice, and PR #7900 stipulated one -- a corner's own record set, forming together as one event with the odds of the
pre-record object. **This note adopts that stipulation unchanged and asks what makes it work.** It supplies no unit of its own and amends nothing.

**Reading, not theorem.** PR #7900's result reads naturally as a statement about shape: a corner is the right neighbourhood, and letting its records form together is what keeps the
sea's own statistics. The work below shows the shape is not what does it. What does it is a fact about where the particle's energy levels sit at that corner, and the corner's edges
never enter the condition at all.

## Definitions

The **cube** is the `2x2x2` cube graph: `8` corners, `12` edge sites, `6` faces, every corner of degree `3`. The **slab** is the `2x2x3` lattice open in `z` -- two stacked cubes --
`12` corners, `20` edge sites, `11` faces, degree `4` at the four middle-layer corners `v = 1, 4, 7, 10` and degree `3` at the other eight. Vertices are indexed `(x*Ly + y)*Lz + z`.
One qubit sits on each **edge site**, neighbours ordered by index:

```text
A_ij = X(edge ij) * prod Z(edges at i ordered before j) * prod Z(edges at j ordered before i),   A_ji = -A_ij,
B_v  = prod of the Z's on the edges incident to v,     S_f = the ordered product of the A's around a face f,
T_ij = (i/2) A_ij (B_i - B_j),     H = -t sum_e eta_e T_e,  t = 1,     star(v) = the edges incident to v.
```

`eta` are the **Kawamoto-Smit staggered link signs** `eta_x = 1`, `eta_y = (-1)^x`, `eta_z = (-1)^(x+y)`; their product round every face of **both** clusters is `-1`, the all-minus
(**pi-flux**) sector. The **code space** is all `S_f = +1`, of dimension `2^(V-1)` -- `128` on the cube, `2048` on the slab -- and the **sea** is the ground state of `H` there at half
filling `N = V/2`. A **record** at an edge site registers a `Z`-value. `H_R` is `H` restricted to a record subspace, which by the restriction identity is the sum of the hop terms on the
**unrecorded** edges. The **one-particle matrix** is `h_ij = -eta_ij`, `W` is the span of its `N` lowest eigenvectors, `P_W` the projector onto `W`, and `e_v` the site vector at `v`.
`P_w` is the projector onto the outcome `w` of the records on `star(v)`, `b_v` the product of the recorded signs, and `Pi_{n_v} = (1 + b_v B_v)/2`. The **residual** of a vector `psi`
under an operator `M` is `||M psi - <M> psi|| / ||psi||`; a vector is an eigenvector when it is below the stated threshold. `TV` is total variation, `(1/2) L1`.

## Theorem 1 -- the record layer factors out exactly, and the question is purely fermionic

**Conclusion.** `[exact]` A face through a corner `v` contains exactly **two** of `star(v)`'s edges, so among the `2^d` subsets `T` of `star(v)` the only ones whose `Z_T` commutes with
every face stabiliser -- the only **logical** ones -- are `T = empty` and `T = star(v)` (`Z_star(v) = B_v`). This holds at all `20` corners of both clusters and at degree `3` and degree
`4` alike, so the `2^d` subsets fall into `2^(d-1)` syndrome classes, each a pair `{T, star(v) \ T}` differing by `B_v`, lying in mutually orthogonal syndrome sectors.
`[numerical, 1e-15]` Therefore, exactly and verified directly rather than inferred,

> **`P_w |sea> = 2^-(d-1) * [ sum over class representatives T of eps_T Z_T ] * Pi_{n_v} |sea>`, `eps_T = prod_{e in T} s_e`,**

at `max |LHS - RHS| = 0.0e+00` (cube `v = 0`, `d = 3`), `8.7e-19` (slab `v = 1`, `d = 4`) and `0.0e+00` (slab `v = 0`, `d = 3`) over every outcome. `[numerical, 1e-9]` Every `Z_T` is
unitary and commutes with `H_R`, checked term by term, so `P_w|sea>` is an `H_R` eigenvector **iff `Pi_{n_v}|sea>` is**; and each outcome's odds are exactly `2^-d`
(`max |p - 2^-d| = 7.2e-16` on the cube, `1.8e-14` on the slab) because `<B_v> = 0` at half filling.

**Proof.** The face masks and the star masks are integers; `|T ∩ f|` parity is `F2` arithmetic over a complete enumeration of the `2^d` subsets, at every corner of both clusters. The
identity is then checked as stated, outcome by outcome, on the sea vectors of both clusters, with the `Z_T` applied as sparse Pauli strings on the half-filling index set.

**Reading, not theorem.** The records themselves drop out. Whatever the recorded values are, conditioning on a corner's whole record set does one thing to the sea: it splits it on
whether that corner is occupied, and then applies a phase pattern that the remaining law does not feel. The identity holds just as exactly at corners where the eigenvector property
**fails**, so it is a fact about the code and not about the sea. Everything that follows is about the particles.

## Theorem 2 -- the criterion: the corner's site vector must live in exactly two modes

**Conclusion.** `[numerical, 1e-12]` `H_R` is the hopping Hamiltonian with vertex `v` **deleted**, and the conditioned sea is a Slater determinant on the deleted graph -- `|1>_v` times
`Slater(W ∩ e_v^perp)` in the occupied branch, `|0>_v` times `Slater(R_v W)` in the empty one. Those subspaces are `R_v h R_v`-invariant **iff**

> **`h e_v ∈ span(e_v, P_W e_v)` -- the site vector `e_v` is a superposition of exactly TWO one-particle eigenmodes of `h`, one occupied and one empty.**

The corner's **degree does not appear**, and neither do its edges. Flat bands are **sufficient**: `h^2 = c I` gives `h = sqrt(c)(P_+ - P_-)` and hence `h e_v = sqrt(c) e_v - 2 sqrt(c)
P_W e_v` for **every** `v`. `[numerical, 1e-12]` The pi-flux cube has `h^2 = 3 I` exactly -- each face's two 2-step paths cancel under flux `-1` -- so the criterion residual is
`8.6e-16` at every corner, and many-body: all `8` corners `x` `8` outcomes are exact `H_R` eigenvectors, max residual `1.9e-14` over the `64`, at the predicted eigenvalue
`-(N-1) sqrt 3 = -5.196152423` in **both** branches; in its own record sector the conditioned sea is the **non-degenerate ground state** of `H_R`, degeneracy `1`, overlap
`1.000000000`. `[numerical, 1e-12]` The criterion sorts the cube's other units too: a single edge is an eigenvector at `0` of `2` outcomes (`0.5774 = 1/sqrt 3`), a face at `0` of `16`
(`0.8165`), while the `9`-edge closed corner star is one at `448` of `448` (`5.3e-16`, `<H_R> = -1.732050808`).

**Proof.** The invariance condition is two lines of linear algebra on `R_v h R_v` and is checked as a per-site residual of the projected components `P_W h e_v` against `P_W e_v` and
`(I - P_W) h e_v` against `(I - P_W) e_v`. The many-body side takes one sparse matvec `g = H_R |sea>` and reads every outcome's residual from it by a bincount over the record key, with
the difference `g_w - <H_R>_w psi_w` taken elementwise **before** summing; the ground-state overlap comes from a dense eigendecomposition of the record block, which is at most
`4096 x 4096`.

**Reading, not theorem.** This is the whole mechanism. Conditioning on a corner's records asks the sea whether that corner is occupied. If the corner sees exactly two energy levels,
answering removes one whole level and leaves the rest of the sea untouched -- so the law that is left has nothing to do to it. If the corner sees more than two, answering leaves a
mixture the remaining law does not sit still on.

## Theorem 3 -- one cube taller it fails, at eight of twelve corners, by a fifth of the norm

**Conclusion.** `[numerical, 1e-10]` The `V x V` criterion predicts every verdict on the `2x2x3` slab **in advance of any many-body run**: `HOLD` at the four degree-`4` middle-layer
corners `v = 1, 4, 7, 10` (residual `<= 5.3e-16`) and `FAIL` at the other eight (`1.196e-01`) -- and it does so although the slab's bands are **not** flat (`diag(h^2) = {3, 4}`), so
flat bands are sufficient and **not** necessary; the two-mode condition is the real statement. `[numerical, 1e-12]` Many-body, sparse on `2^20`: at `v = 1` and `v = 10` the conditioned
sea is an exact `H_R` eigenvector at `16` of `16` outcomes, max residual `2.9e-13`, `<H_R> = -8.828427125 = -(6 + 2 sqrt 2)`, and the `14`-edge closed star of `v = 1` holds at all
`15360` live outcomes (`2.7e-15`, `<H_R> = -3.414213562 = -(2 + sqrt 2)`). At the degree-`3` corner `v = 0` it **fails at all `8` outcomes**, residual `0.207107 = (sqrt 2 - 1)/2`; a
single edge fails at `0.6124 = sqrt(3/8)`, a face at `0.9440`, and the closed star of `v = 0` at all `1024` outcomes up to `0.4460` -- **the closed star makes the degree-`3` case worse,
not better**. `[numerical, 1e-9]` The one-particle layer predicts the **size** of the failure and not only the verdict: the trace of `h_R` on the deleted-site subspace reproduces every
many-body `<H_R>` (`-5.196152423` cube, `-8.828427125` slab `v = 1`, `-9.121320344` slab `v = 0`, both branches alike), while that subspace's invariance residual `||h_R B - B M||` is
`7.6e-16 / 2.1e-15` at the holding corners and `2.071e-01` at slab `v = 0` -- the many-body figure to three digits. `[numerical, 1e-10]` And the condition is **spectral, not a matter of
degree**: the **periodic** `2x2x3` slab has every corner of degree `4` and **fails at every corner** (`1.112e-01`), while the cube is degree `3` throughout and holds; both `2x2x4` slabs
fail as well (`1.106e-01` open, `1.830e-01` periodic).

**Proof.** The slab's `2^20` record space is touched by sparse Pauli-string application only. `H` is held on the conserved half-filling index set `J` (`473088` of `2^20`, `nnz`
`5160960`); the sea comes from Lanczos started at the declared deterministic vector, projected into the code space and polished by shifted power steps inside it, and matches the sum of
the six lowest one-particle levels `{-2 x4, -sqrt 2 x2}`. Because `H_R` never mixes record sectors, one matvec gives every outcome's residual, taken directly. The periodic slab and the
`2x2x4` slabs are reported at the one-particle level only, which is where the criterion lives.

**Reading, not theorem.** Stack a second cube on the first and the property does not survive the join. At the corners with three neighbours -- the same shape that worked on the cube --
the sea is genuinely disturbed by the law running on between formations, and disturbed by about a fifth of its norm, not by a rounding error. The four corners that do keep it are the
ones whose neighbourhood happens to see two energy levels, and that is the whole of what they have in common.

## Theorem 4 -- what preserves it and what breaks it, on declared fixed tables

**Conclusion.** `[numerical, 1e-9]` A **staggered mass preserves the property exactly**. It anticommutes with the bipartite `h`, so `h^2 = (3 + m^2) I` stays flat (`3.09 I` at
`m = 0.3`); the criterion stays at `1.8e-15 / 8.9e-16` and the many-body residual at cube corner `v = 0` over all `8` outcomes at `2.2e-14 / 1.5e-15` for `m = 0.3 / 1.0`, against
`1.8e-14` unperturbed. A uniform mass is a trivial shift at fixed `N` and also holds (`1.8e-14`). `[numerical, 1e-9]` It **breaks** wherever the bands are not flat, under perturbations
declared here as **explicit fixed tables and drawn from nothing**: two hop-sign-flip tables `(0,)` and `(0, 3, 7)`, an on-site table at scales `0.25` and `1.0`, and the zero-flux sector
`eta = +1`. Criterion / many-body residual pairs: `0.408/0.707`, `0.252/0.437`, `0.020/0.023`, `0.084/0.095`, `0.354/0.612`. **Every one-particle verdict is reproduced many-body and the
residual tracks the criterion in magnitude**; each perturbed sea matches its own one-particle sum to `2.7e-14` and its own eigen-equation to `2.8e-14`.

**Proof.** A mass term `m sum_v eps_v n_v = m sum_v eps_v (1 - B_v)/2` is diagonal in the `Z` basis, so it commutes with every record projector and simply adds to `H_R`; the perturbed
seas are recomputed from scratch on the cube's half-filling sector and checked against their own one-particle sums before any residual is read. The tables are literal tuples in the
runner.

**Reading, not theorem.** The property is not fragile in the sense that anything at all destroys it -- an arbitrary staggered mass leaves it exact, at any strength. It is tied to one
checkable spectral condition and to nothing else, and it goes when that condition goes.

## Theorem 5 -- the natural downstream test is blind, and the full record law is not

**Conclusion.** `[numerical, 1e-13]` Let a corner's record set form together, let `exp(-i tau H_R)` run, and let a disjoint corner's record set form together after it. Comparing the
resulting `8`-edge record law with the sea's own gives `TV = 9.4e-16 / 4.6e-15` at the degree-`4` pair `(1, 10)`, where the eigenvector property holds, and `1.8e-14 / 2.2e-14` at the
degree-`3` pair `(0, 11)`, where it **fails by `0.207`**, at `tau = 0.5 / 2.0` alike (control `tau = 0`: `7.8e-18 / 1.4e-17`). **The test cannot tell the two apart.**
`[numerical, 1e-12]` The reason is structural: the sea's joint record law on two disjoint stars is exactly uniform (`max |p - 2^-m| = 5.2e-16 / 1.4e-15 / 1.5e-15` at `(1,10)`, `(0,11)`,
`(0,2)`), because the only logical `Z_T` inside two stars are `I`, `B_v`, `B_w`, `B_v B_w`, and at half filling `max_v |<B_v>| = 2.8e-17` over all `12` corners while `<B_v B_w>` is
`1.4e-17` or smaller on those non-adjacent pairs -- against `-0.2500` on the adjacent pair `(0,1)`. Only a non-zero `<B_v B_w>` could fail that test, and this schedule generates none.
`[numerical, 1e-12]` The **full record law does** discriminate: record every remaining edge and compare all `2^20` patterns with the sea's, and `TV = 1.9e-15 / 4.6e-15` where the
property holds -- on the sea's own support `411648` -- against `0.020` and `0.087` at `tau = 0.5` and `2.0` where it fails, the propagated object leaving the sea's `Z`-support by
`16384` patterns (`428032` against `411648`). `[numerical]` Finally, a **cancellation trap** is named: the one-matvec bincount identity is exact, but read through the variance form
`<H_R^2> - <H_R>^2` it cancels catastrophically -- at the holding corner `v = 1` that difference comes out **negative** (`-1.3e-11`, an impossible variance) of magnitude `3.7e-06`,
a spurious `~1e-6` floor, where the direct form gives `2.8e-13`. The two agree at the failing corner (`0.2071` against `0.2071`). Every headline residual in this note is the direct form.

**Proof.** Each branch of the schedule is propagated with `expm_multiply` on its own record block of `H_R`; the `8`-edge marginal and the full `2^20` law are two bincounts of the same
propagated weights, so the blindness and the discrimination are read off one computation. `<B_v>` and `<B_v B_w>` are exact `Z`-diagonal sums against the sea's odds.

**Reading, not theorem.** A lane that checks a neighbourhood tick by forming records at two far-apart corners and comparing those eight records with the sea's will get agreement to
`1e-14` whether the tick is exactly right or wrong by a fifth. That marginal is uniform for reasons that have nothing to do with the tick. The thing to report is the residual itself, or
the whole record law.

## Corollary -- what this says about PR #7900's corner result

Within the setting declared above, on the two named clusters, in the staggered sector at half filling, and for PR #7900's stipulated unit of formation alone:

1. **The mechanism is exact and two-step.** The record layer factors out completely and commutes with what is left of the law (`T1`), and the rest is a **one-particle spectral
   condition**: the corner's site vector must live in exactly two eigenmodes of `h`, one occupied and one empty (`T2`). The corner's degree and the corner's edges never enter it.
2. **The cube satisfies it because pi flux makes both bands flat**, `h^2 = 3I`, and an arbitrary **staggered mass keeps them flat**, so the property survives that perturbation exactly
   (`T2`, `T4`).
3. **It is not general.** It fails at the eight degree-`3` corners of the `2x2x3` slab and at **every** corner of the periodic slab, by tenths of the norm (`T3`). So PR #7900's
   candidate sentence -- *"Records form together on a corner's record set; between formations the law runs on"* -- is **an exact property of flat-band clusters and not a principle of
   the lattice**. It is not called wrong anywhere here; its exact condition is supplied, and its condition is not met one cube taller.
4. **Any lattice can now be screened cheaply.** Whether a given corner of a given cluster in a given flux sector has the property is settled by a `V x V` eigendecomposition -- one line
   of one-particle linear algebra -- rather than a many-body run, and the same layer predicts the size of the failure to three digits where it fails (`T3`).
5. **The two-corner marginal test is blind**, and only the full record law discriminates (`T5`). That is a warning for the tick lane's next computations, and it is the practical
   consequence of this note most likely to matter.

## Reading, not theorem -- the whole thing in plain words

The earlier result looked like a principle: form a corner's records together and the sea's own statistics survive. It turns out to be a property of the small cube, where the particle's
energy bands happen to be flat, and of any corner whose neighbourhood sees only two energy modes. One cube taller, at the corners with three neighbours, it fails by a tenth. So the
neighbourhood tick is not yet a law of the lattice; it is an exact fact about where the bands are flat, and there is now a cheap test that tells, for any lattice, which corners have it.

## Interfaces named for other lanes, not settled here

- **Units that are not corner stars.** Everything above is about a corner's own record set and the units PR #7900 declared beside it. What a differently shaped unit -- a bond pair, a
  plaquette group, a region -- does is outside this note, and `T2`'s criterion is stated for a single deleted site only.
- **Ticks that reach beyond one corner.** The schedules here form one corner's records, run the law, and form a second, disjoint corner's. A tick that acts on overlapping or adjacent
  neighbourhoods, or on a whole layer at once, is named and not computed; `<B_v B_w> = -0.25` on adjacent corners says the adjacent case is a different computation.
- **The actual law's spectrum on the fine lattice.** The clusters here are emergent, and the one-particle matrix is the designed hopping matrix of a designed encoding. Whether the
  framework's own law has flat bands anywhere, or two-mode corners anywhere, is not touched.
- **Larger clusters and the limit.** The `2x2x4` slabs and the periodic slab are carried at the one-particle level only; the thermodynamic limit and the `3x3x3` cube are named and not
  computed.
- **Whether the criterion is also necessary for the record statistics.** `T2` characterises when the conditioned sea is an `H_R` eigenvector. Whether some corner could fail that and
  still reproduce the sea's record law for a different reason is not settled here.

## Remaining live routes

1. A neighbourhood tick built on a unit chosen **by** the criterion -- forming records at whichever corners of a given cluster satisfy `h e_v ∈ span(e_v, P_W e_v)` -- is not computed
   here and is a live construction, on this cluster and on others.
2. Whether some between-event rule other than the unitary one keeps the sea's record law at a failing corner. Only the unitary rule is run here.
3. Whether flat bands can be arranged on a physically motivated cluster and sector, rather than found on the smallest one; `T4` shows the staggered mass is one deformation that keeps
   them flat.

## Executable claim block

The canonical machine-bound restatement of the five theorem conclusions.

```text
setting: qubits on the EDGE sites of TWO finite subgraphs of the cubic lattice -- the 2x2x2 cube (8 corners, 12 edges, 6 faces, all degree 3) and the 2x2x3 slab open in z (12 corners, 20 edges, 11 faces, degree 4 at v = 1,4,7,10 and degree 3 at the other eight); ordinary (commuting) composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md with Admissibility reading note (2)
encoding: A_ij = X(edge ij) * Z's ordered before it at both endpoints; A_ji = -A_ij; B_v the Z's incident to v; S_f the ordered face loop; T_ij = (i/2) A_ij (B_i - B_j)
law: eta = Kawamoto-Smit staggered signs, flux -1 on every face of both clusters; H = -sum_e eta_e T_e, t = 1; code space all S_f = +1, dim 2^(V-1) = 128 / 2048; sea = its ground state at half filling, E = -4 sqrt 3 (cube) and -(8 + 2 sqrt 2) (slab), each the sum of the N lowest levels of h_ij = -eta_ij; H_R = the hops on the UNRECORDED edges = the hopping Hamiltonian with vertex v deleted
formation_unit: ADOPTED UNCHANGED from PR #7900 and derived from nothing -- the records of star(v) form together as one event with the odds of the pre-record object; this note stipulates no unit of its own
T1_record_layer [exact; numerical 1e-15]: a face through v carries exactly 2 of star(v)'s edges, so the only logical Z_T are T = empty and T = star(v) = B_v, at all 20 corners of both clusters and at degree 3 and 4 alike, and the 2^d subsets fall into 2^(d-1) syndrome classes; P_w|sea> = 2^-(d-1) (sum_T eps_T Z_T) Pi_{n_v}|sea> with Pi_{n_v} = (1 + b_v B_v)/2, at max |LHS - RHS| = 0.0e+00 / 8.7e-19 / 0.0e+00 (cube v=0; slab v=1; slab v=0); every Z_T commutes with H_R; each outcome's odds are exactly 2^-d, max |p - 2^-d| = 7.2e-16 / 1.8e-14
T2_criterion [numerical, 1e-12]: the conditioned sea is an H_R eigenvector IFF h e_v in span(e_v, P_W e_v) -- e_v a superposition of exactly TWO one-particle eigenmodes, one occupied and one empty; degree and edges do not enter. Flat bands are SUFFICIENT; the pi-flux cube has h^2 = 3I exactly, criterion residual 8.6e-16 at every corner, and many-body 8 corners x 8 outcomes at max residual 1.9e-14, eigenvalue -(N-1) sqrt 3 = -5.196152423 in both branches, H_R ground state of that record sector non-degenerate with overlap 1.000000000; single edge 0/2 at 0.5774, face 0/16 at 0.8165, closed corner star 448/448 at 5.3e-16
T3_not_general [numerical, 1e-12]: on the 2x2x3 slab the V x V criterion says HOLD at v = 1,4,7,10 (<= 5.3e-16) and FAIL at the other eight (1.196e-01) in advance, although diag(h^2) = {3,4} is not flat -- flat bands are sufficient, not necessary. Many-body on 2^20 (|J| = 473088, nnz 5160960): v=1 and v=10 hold at 16/16, max residual 2.9e-13, <H_R> = -(6 + 2 sqrt 2); the 14-edge closed star of v=1 holds at 15360/15360 at 2.7e-15, <H_R> = -(2 + sqrt 2); v=0 fails at all 8 at 0.207107 = (sqrt 2 - 1)/2, a single edge at 0.6124 = sqrt(3/8), a face at 0.9440, the closed star of v=0 at 1024/1024 up to 0.4460. The one-particle trace gives every <H_R> (-5.196152423 / -8.828427125 / -9.121320344, both branches) and its invariance residual 2.071e-01 at slab v=0 matches the many-body figure to three digits. The PERIODIC 2x2x3 slab is degree 4 at every corner and fails at every corner (1.112e-01); both 2x2x4 slabs fail (1.106e-01 open, 1.830e-01 periodic): the condition is spectral, not a matter of degree
T4_robustness [numerical, 1e-9]: a staggered mass anticommutes with the bipartite h, keeps h^2 = (3 + m^2) I flat (3.09 I at m = 0.3) and preserves the property exactly -- criterion 1.8e-15 / 8.9e-16 and many-body 2.2e-14 / 1.5e-15 at m = 0.3 / 1.0 against 1.8e-14 unperturbed; a uniform mass is a trivial shift and also holds (1.8e-14). DECLARED FIXED TABLES break it: hop-sign flips (0,) and (0,3,7), an on-site table at 0.25 and 1.0, and the zero-flux sector, at criterion/many-body 0.408/0.707, 0.252/0.437, 0.020/0.023, 0.084/0.095, 0.354/0.612; every one-particle verdict is reproduced many-body, each perturbed sea matching its own one-particle sum to 2.7e-14
T5_blind_marginal [numerical, 1e-13]: form star(v), run exp(-i tau H_R), form a disjoint star(w): the 8-edge record law agrees with the sea's at TV = 9.4e-16 / 4.6e-15 where the property holds AND 1.8e-14 / 2.2e-14 where it fails by 0.207, at tau = 0.5 / 2.0 -- BLIND -- because that joint law is exactly uniform (max |p - 2^-m| <= 1.5e-15), <B_v> <= 2.8e-17 at all 12 corners and <B_v B_w> <= 1.4e-17 on non-adjacent pairs against -0.2500 on adjacent (0,1). The full 2^20 record law discriminates: TV 1.9e-15 / 4.6e-15 on the sea's support 411648 where it holds, against 0.020 / 0.087 where it fails, leaving that support by 16384 patterns (428032). Cancellation trap named: the variance form <H_R^2> - <H_R>^2 comes out NEGATIVE (-1.3e-11) of magnitude 3.7e-06 at the holding corner where the direct form gives 2.8e-13
narrowing: this note narrows PR #7900's corner result of the same day and the same session to its exact condition; it calls that result wrong nowhere, forecloses no unit, rule, rate or neighbourhood tick, and says nothing about what the framework's tick is
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=20 FAIL=0
```

## Proof boundary

Every statement above is proved on **two finite clusters** -- the `2x2x2` cube graph and the `2x2x3` slab open in `z`, with the periodic `2x2x3` slab and the two `2x2x4` slabs carried
at the one-particle level only -- in **one flux sector** (all-minus, the Kawamoto-Smit staggered signs) at **one filling** (half). Nothing is claimed for other clusters, other sectors,
other fillings, infinite lattices, or any law family other than the one in "Definitions". The law is **designed**, not derived: the encoding is chosen so that the Majorana relations
`R0`-`R4` hold, the face constraints make that consistent, and the parity dictionary is one readout map among many, with no uniqueness claimed for either.

**The unit of record formation is stipulated, and it is PR #7900's, adopted unchanged and derived from nothing.** Reading note (2) is explicit that the axioms supply no formation site,
probability or rate; they supply no unit either. This note supplies none, adds none, and amends none. The between-event rule used in `T5` is the unitary `exp(-i tau H_R)` at
`tau in {0, 0.5, 2.0}`, declared here; no other rule is run. The `2x2x3` slab was chosen because it is the object of this family with exactly `20` edge sites -- `2x2x4` has `28` open
and `32` periodic, outside the memory stipulation of this session -- and because it carries degree-`3` and degree-`4` corners in one sea, so degree is controlled inside a single object.

Every line not tagged `[exact]` is a **deterministic double-precision evaluation** of an exactly specified quantity at the stated threshold. The `2^20` layer is touched by sparse Pauli
strings and Lanczos only; no dense object above `4096 x 4096` is formed anywhere. There is **no seed anywhere** in this note or its runner: the Lanczos start vector is a fixed
deterministic formula written out in the runner, and every perturbation of `T4` is an explicit fixed table, written out as `SIGN_FLIPS` and `ONSITE`. The one place a floating-point
identity was found to be untrustworthy -- the bincount variance form -- is **named in `T5` and not used** for any figure reported here.

**This note narrows a result of the same day and the same session, and the narrowing is the point.** It supplies the exact condition under which PR #7900's corner result holds, shows
that condition is met on the cube and not one cube taller, and gives a cheap test for it on any lattice. It calls PR #7900 wrong nowhere; its `T3` is reproduced here independently and
exactly. **No route is foreclosed:** a neighbourhood tick is not ruled out, a unit is not ruled out, a rate is not ruled out, and nothing here says what the framework's tick is. The
`T3` and `T4` figures are values on **declared finite sets** -- two clusters, twenty corners, seven declared units, five declared perturbations, three declared `tau` -- reached by
**complete enumeration** of the outcomes of each declared unit, and are labelled as such wherever they appear. No absolute unit appears anywhere, no axiom text is amended, extended,
reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

An honest auditor should come away with a **narrowing**, not a refutation and not a foreclosure: PR #7900's corner eigenvector result is reproduced exactly on its own cluster, its mechanism
is derived in two exact steps, and the condition that mechanism needs is stated and then shown to fail one cube taller at eight of twelve corners. The stipulated unit is PR #7900's,
adopted unchanged and declared as stipulated in the front matter, the setting, the claim block and the proof boundary alike; the candidate formation sentence is quoted as a candidate
wording and is nowhere called wrong -- what is reported is the exact condition under which it is true. The two-sided result is on the record: the property survives an arbitrary
staggered mass exactly, and it fails at a majority of the slab's corners and at every corner of the periodic slab. The disagreements with the naive reading are stated plainly -- degree
is not the governing quantity, the larger closed-star unit makes the degree-`3` case worse rather than better, and the natural downstream test of `T5` cannot see the difference at all.
The cancellation trap is named rather than quietly avoided.

Two deliberate departures from the scratch computation this note lands are stated here. First, that computation's perturbation rows used a seeded random generator; this session forbids
seeds, so those rows are replaced by **explicit fixed tables** and their numbers therefore differ -- same verdicts, same magnitude tracking, and the scratch caveat about one draw nearly
closing the Fermi gap does not arise here, every perturbed sea converging to `2.8e-14`. Second, the cancellation trap of `T5` shows up here as an **impossible negative** variance of
magnitude `3.7e-06` rather than the scratch's spurious positive of the same size; the floor is the same `~1e-6` and the conclusion -- use the direct form -- is unchanged.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the "Imports and authority" pointers are plain
text carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair at `PASS=20 FAIL=0`, runtime under the declared `150` seconds, a current
zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; audit remains a separate lane.
