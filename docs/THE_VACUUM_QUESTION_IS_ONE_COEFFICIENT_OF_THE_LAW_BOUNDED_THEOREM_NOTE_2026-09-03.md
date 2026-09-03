---
claim_id: vacuum_question_one_coefficient_occupancy_cost
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3 carrying one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, with free nearest-neighbour hopping of strength t = 1 and the encoding's own site operator B_i given a coefficient -- the occupancy term -J_B sum_i B_i, declared here and not derived -- on the named finite blocks and tori only: (T1) sum_i B_i commutes with every encoded hop T_ij = (i/2) A_ij (B_i - B_j), exactly, over all 16029 (hop, site) Pauli-string sign pairs on the open 2x2x2 and 3x3x3 blocks and the tori 3^3 and 4^3, by the identity [sum_k B_k, T_ij] = -i (B_i^2 - B_j^2) A_ij = 0, while a single B_i does not, ||[B_i, T_ij]|| = 2 against ||[sum_k B_k, T_ij]|| = 0 on a dense 16-dimensional block; and (V I - sum_i B_i)/2 is the record-number operator there, so -J_B sum_i B_i = -J_B V + 2 J_B N is a pure chemical potential of 2 J_B per fermion and adds no dynamics. (T2) At J_B = 0 the global minimum over record numbers and flux sectors is the half-filled staggered sea: every cluster here is bipartite with all degrees 6, so its spectrum is symmetric about 0 to 3.4e-14 and min_N E_N = E_{V/2} for every link-sign field, attained on the tie range [#neg, #neg + #zero] (plain 4^3 untwisted: 20 zero modes, ties N in [22, 42]); on the open 2x2x2 cube all 32 consistent sectors at all N give -4 sqrt3 uniquely at the all-(-1) sector and N = 4, by a margin of 0.456067; on the 4^3 torus the minimum is -32 sqrt6, the Cauchy-Schwarz floor over ALL link-sign fields, checked against 8 twists times 2 uniform sectors, 5 structured sectors and 1000 random fields; elsewhere the same sector wins as a search result, -258.857540 on 6^3 (8 twists times 2 plus 300 random, best random -230.81), -611.811768 on 8^3, and -26.040600 against -21.213203 on the open 3x3x3. (T3) With W(J_B) = sum over levels below -2 J_B of (eps + 2 J_B), twist-minimised at each J_B, the ground state moves continuously from the half-filled staggered sea to the empty lattice, and the optimal Wilson twist changes with J_B. (T4) The plain sector overtakes the staggered one at J_B* = sqrt3/2 exactly on the 4^3 torus -- the staggered KS twist has W = -24 - 24 sqrt2 - 8 sqrt3 + 56 J against the plain (0,1,1) twist's W = -24 - 24 sqrt2 + 40 J, difference 16 J - 8 sqrt3 -- at 0.849332 on 6^3, 0.867676 on 8^3 and 0.8654003 +- 3e-6 in the thermodynamic limit, where the fillings there are 0.4417 and 0.2521; the emptying thresholds J_B >= |eps_min|/2 are 3 exactly for the plain sector, band bottom -6 at (pi, pi, pi), and sqrt3 for the staggered one, on all three tori and in the limit; 3 sqrt2/2 and sqrt6/2 on the open 3x3x3; 3/2 on the cube, where all 32 sectors tie at W = 0; and on the cube the all-(-1) sector loses to the 2-flux class at sqrt3 - (1 + sqrt2)/2 = 0.524944. (T5) For ANY link-sign field on a bipartite degree-6 cluster, tr M^2 = 6V and D M D = -M give W(J) >= min_m [-sqrt(3 V m) + 2 J m] = -V sqrt(3/2) + J V for J <= sqrt(3/8) = 0.612372 and -3V/(8J) above; the 4^3 flat-twist staggered sea has W = 64 J - 32 sqrt6 and attains that floor with slack at most 7e-15 at every J_B <= sqrt(3/8), so it is a global minimiser over all link-sign fields AND all record numbers on that interval. (T6) Exactly half filling survives for J_B < 4 sqrt6 - 3 - 3 sqrt2 - sqrt3 = 0.823267 twist-minimised on 4^3 and for J_B < sqrt6/2 within the half-filling twist, for J_B < 2 sqrt3 - 3 = 0.464102 on 6^3 and J_B < 0.306846 on 8^3; in the thermodynamic limit the staggered band is gapless at q = (pi, pi, pi), so exactly half filling survives only at J_B = 0, with 1/2 - n(J_B) -> (2/(3 pi^2)) J_B^3. T2 away from the cube and the 4^3 torus is a search result, not a theorem. The occupancy term and its coefficient are declared by this note, not derived from any axiom; no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py
---

# The vacuum question is one coefficient of the law

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py`](../scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.txt`](../logs/runner-cache/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

Three notes sit next to each other. One says that on the coarse lattice the half-filled staggered sea is what the hopping term prefers, and that the filling which selects it is a supplied datum. The other says that the empty state and the
half-filled sea have different and incompatible consequences, and asks which of them the framework calls its vacuum. A third says that the encoding's site operator `B_i` is a term type of the declared law and that no coefficient is attached to it
anywhere. Put those three together and the vacuum question has a shape: give `B_i` the coefficient the law leaves blank, and the answer is a number. This note computes what that number does.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems on the ground state of free coarse-lattice hopping plus an occupancy term -J_B sum_i B_i: exact Pauli-string commutation making the term a pure chemical potential, exhaustive enumeration on the open 2x2x2 cube, exact surd crossings on the 4^3 torus, and an extended Cauchy-Schwarz certificate valid at every J_B <= sqrt(3/8). The sampling items are declared search results, not theorems, and the thermodynamic items are converged Bloch quadrature. The occupancy term and its coefficient are declared, not derived."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: what value the dimensionless coefficient J_B/t takes."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`F`. Group `A` is exact Pauli-string and dense matrix arithmetic at zero tolerance; the surd statements of `B`, `C`, `D` and `E` are exact in `sympy`;
and the items tagged `[numerical]` are floating-point statements at the stated tolerance. Global minimality is a theorem on the cube and on the `4^3` torus and a **search result** elsewhere, labelled so wherever it appears.

The six are `T1` (`A`), the occupancy term as a pure chemical potential of `2 J_B` per fermion; `T2` (`B`), the half-filled staggered sea as the global ground state at `J_B = 0` over all record numbers and all sectors; `T3` (`C`), the ground state as
a function of `J_B`, twist-minimised at each `J_B`; `T4` (`C`), the crossover `J_B*` and the emptying thresholds; `T5` (`D`), the extended certificate on the `4^3` torus for `J_B <= sqrt(3/8)`; and `T6` (`E`, `F`), the half-filling persistence
windows and the gapless thermodynamic limit.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering and the tight-binding dispersion are standard methodology; every object is redeclared here and the runner recomputes every statement.
No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): the declared law and its term census, quoted below. Pointer only; the encoding, `B_i` and the hop are redeclared here
  and recomputed by this runner.
- `HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7874): the supplied-filling sentence quoted below.
- `MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7879): the vacuum question as that note names it, quoted below.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting". This note cites none of their grades and adopts no hypothesis.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." **Qubit**: "Each site has
a domain of local possibilities", whose "full one-site possibility domain has algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." **Record**: "Records form", "a record locks exactly one admissible local possibility", "records
are permanent", "Only records are readable."

The law whose coefficient is in question is the one PR #7834 declares. Its term census reads, verbatim:

> 1. Of the `16` quantum term types (three `A_ij`, six hop components, three hop totals, `B_i`, three face stabilizers) and the `49` marker term types (the `48`
>    templates and the no-role penalty), `4` are star-local -- `A_x`, the `A B_i` component along `x` and along `z`, and `B_i` -- `61` are through with an
>    explicitly constructed `6`-connected hub chain, and `0` are across.

and that note states what it does not supply, verbatim:

> - It supplies no update rule, no formation site, no formation rate, and no values. No coupling, no absolute unit, and no dynamical clause appears anywhere.

So `B_i` is a term type of the law with no coefficient attached to it. The question this note asks is what happens when it has one. The question it is asking about is the one PR #7879 names, whose Corollary item 3 reads, verbatim:

> 3. **The two landed results are consistent with each other and not with a single vacuum.** Which state is the framework's vacuum is a decision about the framework,
>    named here for its owner, not a residual to compute away. The exact consequences of each choice are supplied. **If the vacuum is empty**: the positive number
>    density `n_v` sources gravity and meets every clause; all flux sectors tie, so the kinetic clause's staggered field is a free choice; and there is no Dirac
>    structure. **If the vacuum is the half-filled sea**: the staggered sector is selected by the hopping energy; the spectrum has a gapless point at the reduced-zone
>    corner; matter comes in pairs; the energy density is the object that carries the monopole; and the number-density deviation carries a dipole and no monopole.

and the sentence from PR #7874 that this note sharpens reads, verbatim:

> So the question "which sector" is answered by "how much matter", and the filling is a supplied datum, not something this note derives.

The object declared here, and derived from nothing, is the **occupancy term**

```text
H = - t sum_<ij> eta_ij c_i^dag c_j  -  J_B sum_i B_i,      t = 1,
```

with `J_B >= 0` a single dimensionless coefficient. Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the superfast encoding, the two uniform sign fields, the flux sectors, the occupancy term and the
functional `W(J_B)`. `P1` (`A`) is the commutation making the occupancy term a chemical potential; `P2` (`B`) the `J_B = 0` ground state; `P3` (`C`) the `J_B`-dependence, the crossover and the thresholds; `P4` (`D`) the extended certificate; `P5`
(`E`, `F`) the half-filling windows and the limit. `P3` uses `P1` to know that the term only shifts occupancies; `P4` uses nothing from `P3` but its numbers; `P5` uses `P2`'s bipartite lemma. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` at `2v + e_a`. The **KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1
+ v_2}`; the **plain sign** is `+1` on every bond. The **encoding** is the Bravyi-Kitaev superfast encoding on the coarse lattice, code qubits on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`, with

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_i  = product of the Z's on the edges incident to i,   T_ij = (i/2) A_ij (B_i - B_j),   S_f = the ordered product of the four A's around a coarse face f
```

A **flux sector** is a choice of eigenvalue `+-1` for every `S_f` consistent with the `F2` relations among them, realised as a link-sign field `eta` by spanning-tree gauge fixing followed by fundamental-cycle transport. The **hopping matrix** is
`M_ij = eta_ij` on nearest-neighbour coarse bonds and `0` elsewhere, `E_N` is the sum of its `N` lowest eigenvalues, and the **filling** is `n = N/V`. On a torus the three **Wilson lines** are gauge-invariant data that no `S_f` fixes; a **twist**
flips the signs on one cut plane and changes one Wilson line without changing any face. The **occupancy cost** functional, measured from the empty lattice, is

```text
W(J_B) = min_N [ E_N + 2 J_B N ] = sum over levels eps < -2 J_B of (eps + 2 J_B),
```

and `n(J_B) = N/V` at the minimising `N`. Every torus quantity below is minimised over the eight twists **at each `J_B` separately**.

## Theorem 1 -- the occupancy term is a pure chemical potential

**Conclusion.** On the open `2x2x2` and `3x3x3` coarse blocks and the coarse tori `3^3` and `4^3`:

1. Every `B_i` squares to the identity and any two of them commute, and `A_ij` anticommutes with exactly `B_i` and `B_j`: `0` wrong signs over all `16029` `(hop, site)` Pauli-string pairs.
2. Hence `[sum_k B_k, T_ij] = i (B_i + B_j) A_ij (B_i - B_j) = -i (B_i^2 - B_j^2) A_ij = 0` for every hop: `sum_i B_i` commutes with the whole hopping term.
3. A single `B_i` does not. On a dense `16`-dimensional block, `||[sum_k B_k, T_ij]|| = 0` and `||[B_i, T_ij]|| = 2` over every hop, with `T_ij` Hermitian.
4. `(V I - sum_i B_i)/2` is the record-number operator there, with integer spectrum in `[0, V]`. So `-J_B sum_i B_i = -J_B V + 2 J_B N`.

**Proof.** Items 1 and 2 are `F2`/`Z4` symplectic bit arithmetic at zero tolerance, the sign of a commutator of two Pauli strings read off the symplectic form. Item 3 builds the four-qubit block explicitly as complex matrices and takes the
commutators. Item 4 diagonalises `(V I - sum_i B_i)/2` on that block; its eigenvalues are integers, and `sum_i B_i` commuting with every hop makes them conserved.

**Reading, not theorem.** The extra term counts particles and does nothing else. It cannot move one, it cannot make one, and it cannot destroy one; adding it to the law changes no motion, only the price of standing still. One particle costs `2 J_B`,
and `N` of them cost `2 J_B N`. That is the whole content of the coefficient: a charge for occupancy.

## Theorem 2 -- at zero cost the ground state is the half-filled staggered sea

**Conclusion.** At `J_B = 0`:

1. Every cluster here is bipartite with all degrees `6`, so every link-sign field on it has a spectrum symmetric about `0` -- `max |eps + reverse eps| < 4e-14` over all `82` spectra -- and therefore `min_N E_N = E_{V/2}`, attained exactly on the tie
   range `[#neg, #neg + #zero]`. On the plain `4^3` field at the untwisted Wilson line there are `20` zero modes and the ties run over `N` in `[22, 42]`.
2. On the open `2x2x2` cube, exhaustively over all `32` consistent sectors and all `N`, the global minimum is `-4 sqrt3`, attained **only** by the all-`(-1)` sector at `N = 4`, by a margin of `0.456067` to the next distinct value.
3. On the `4^3` torus the global minimum over `8` twists times `2` uniform sectors, `5` structured sectors and `1000` random link-sign fields is `-32 sqrt6`, which is the Cauchy-Schwarz floor over **all** link-sign fields on that torus.
4. Elsewhere the same sector wins as a **search result**: `-258.857540` on `6^3` against a best random field of `-230.81`, `-611.811768` on `8^3`, and `-26.040600` against the plain sector's `-21.213203` on the open `3x3x3`.

**Proof.** Item 1 is `[numerical, 4e-14]` for the symmetry and exact in structure: a spectrum symmetric about `0` makes the partial sums of the sorted levels decrease exactly while the levels are negative and increase after, so the minimum sits at
the last negative level and ties across the zeros. Item 2 enumerates the `32` sectors from the `F2` relations among the `S_f`, realises each as a sign field, and compares the exact ladders. Item 3 evaluates the fields and compares against the bound
of Theorem 5 at `J = 0`. Item 4 is direct evaluation at the runner's fixed seed and is a statement about the fields drawn, not about the whole space.

**Reading, not theorem.** With nothing to pay for a particle, the lattice fills every level that costs less than nothing, and half the levels do, because the box is two-colourable and its levels come in plus-minus pairs. So the cheapest state is
exactly half full whatever the signs on the links, and among the sign patterns the cheapest is the one with a minus around every square. On the smallest box that is the cheapest arrangement there is; on the `4^3` box it is as cheap as anything could
be.

## Theorem 3 -- the ground state as a function of the cost

**Conclusion.** With `W(J_B)` twist-minimised at each `J_B`, on the `4^3` torus:

| `J_B` | `w` plain | `n` plain | twist | `w` stag | `n` stag | twist |
|---|---|---|---|---|---|---|
| `0` | `-1.060660` | `0.50000` | `111` | `-1.224745` | `0.50000` | `111` |
| `0.5` | `-0.593750` | `0.34375` | `000` | `-0.724745` | `0.50000` | `111` |
| `0.823267` | `-0.390788` | `0.31250` | `011` | `-0.401477` | `0.50000` | `111` |
| `sqrt3/2` | `-0.364064` | `0.31250` | `011` | `-0.364064` | `0.43750` | `000` |
| `sqrt6/2` | `-0.224144` | `0.12500` | `111` | `-0.134464` | `0.25000` | `000` |
| `sqrt3` | `-0.097317` | `0.12500` | `111` | `0` | `0` | `000` |
| `3` | `0` | `0` | `000` | `0` | `0` | `000` |

and in the thermodynamic limit, by Bloch quadrature at `L = 224`:

| `J_B` | `w` plain | `n` plain | `w` stag | `n` stag |
|---|---|---|---|---|
| `0` | `-1.0024184` | `0.500028` | `-1.1938011` | `0.500000` |
| `0.4` | `-0.6480922` | `0.385838` | `-0.7946948` | `0.495420` |
| `0.8654003` | `-0.3510864` | `0.252133` | `-0.3510874` | `0.441724` |
| `1.2` | `-0.2126531` | `0.167895` | `-0.1051182` | `0.267308` |
| `sqrt3` | `-0.0810372` | `0.085917` | `0` | `0` |
| `3` | `0` | `0` | `0` | `0` |

The optimal Wilson twist is not fixed: the staggered sector's minimising twist changes from `(1,1,1)` to `(0,0,0)` as `J_B` rises through the table, and the plain sector's takes three distinct values across it.

**Proof.** `[numerical, 1e-9]` throughout, with the occupancy set at each `J_B` read off the sorted spectrum and the eight twisted fields built explicitly. The Bloch formulas `2 sum_a cos q_a` and `+-sqrt(6 + 2 sum_a cos q_a)`, with a half-integer
momentum shift on each twisted axis, reproduce the real-space spectra at `L = 4, 6, 8` to `2.7e-14`.

**Reading, not theorem.** Raise the price and the sea drains. At no price the lattice is half full; at a middling price it is a third or a quarter full; past a certain price it is empty. Nothing else about the arrangement changes -- the same links,
the same signs, the same motion -- only how much of the lattice is in use.

## Theorem 4 -- the crossover and the emptying thresholds

**Conclusion.**

1. On the `4^3` torus the plain sector overtakes the staggered one at `J_B* = sqrt3/2` **exactly**: the staggered sector's KS twist has `W = -24 - 24 sqrt2 - 8 sqrt3 + 56 J` and the plain sector's `(0,1,1)` twist has `W = -24 - 24 sqrt2 + 40 J`, both
   valid across `J = sqrt3/2`, with difference `16 J - 8 sqrt3`.
2. `J_B* = 0.849332` on `6^3`, `0.867676` on `8^3`, and `0.8654003 +- 3e-6` in the thermodynamic limit, where the fillings at the crossover are `0.4417` for the staggered sector and `0.2521` for the plain one.
3. A sector empties at `J_B >= |eps_min|/2`. That is `3` **exactly** for the plain sector -- band bottom `-6` at `q = (pi, pi, pi)` -- and `sqrt3` for the staggered one, on all three tori and in the limit; `3 sqrt2/2` and `sqrt6/2` on the open
   `3x3x3`; and `3/2` on the open `2x2x2` cube, where all `32` sectors tie at `W = 0` from there up.
4. On the cube the all-`(-1)` sector stops being the strict global minimiser at `sqrt3 - (1 + sqrt2)/2 = 0.524944`, where the two-flux class takes over.

**Proof.** Item 1 is exact: the `L = 4` spectra `0 x8, +-2 x12, +-2sqrt2 x12, +-2sqrt3 x4` and `0 x16, +-2 x8, +-2sqrt2 x8, +-(2 + 2sqrt2) x4, +-(2sqrt2 - 2) x4` are verified against the numeric ones to `1e-13`, the occupancy sets are constant across
`J = sqrt3/2`, and the difference is a `sympy` identity whose only root is `sqrt3/2`. Items 2 and 3 are `[numerical, 1e-9]` by bisection on the twist-minimised difference and by reading the band bottoms, with the surd values checked to `1e-9`. Item 4
bisects on the cube's exhaustive sector list.

**Reading, not theorem.** There is a price at which the two arrangements cost the same, and it is close to nine tenths of a hopping unit however large the box. Below it the minus-on-every-square arrangement is cheaper, above it the plain one is, and
the reason is simple: the staggered arrangement holds its levels in a narrow band and so gives them all up at once, while the plain one has a few very deep levels that survive a much higher price. The plain arrangement is the last to empty, and it
empties at three.

## Theorem 5 -- the extended certificate

**Conclusion.** On any bipartite cluster of `V` sites with every degree `6`, for **any** link-sign field:

1. `tr M^2 = 2|E| = 6V` and `D M D = -M` for the colour involution `D`, so the spectrum is symmetric about `0` and the squares of the negative levels sum to `3V`.
2. If `m` levels are occupied, Cauchy-Schwarz gives `sum_occ |eps| <= sqrt(3 V m)`, hence `W(J) >= min_{0 <= m <= V/2} [-sqrt(3 V m) + 2 J m]`, which equals `-V sqrt(3/2) + J V` for `J <= sqrt(3/8) = 0.612372` and `-3V/(8J)` above it.
3. On the `4^3` torus the staggered sector at its flat twist has `W = 64 J - 32 sqrt6` and **attains** that floor with slack at most `7e-15` at every `J_B <= sqrt(3/8)`. It is therefore a global minimiser over all link-sign fields **and** all record
   numbers on that whole interval, not only at `J_B = 0`.
4. All `1021` fields evaluated -- `16` twisted uniform, `5` structured, `1000` random -- respect the floor at `16` values of `J_B`: `0` violations.

**Proof.** Item 1 is a zero-tolerance integer matrix identity. Item 2 minimises a one-dimensional function of `m` with the interior stationary point `m = 3V/(16 J^2)`, which lies inside `[0, V/2]` exactly when `J >= sqrt(3/8)`. Item 3 is exact: the
flat-twist spectrum is `+-sqrt6` with multiplicity `32` each, so every occupied level has the same size, which is the equality case, and the occupancy stays at `32` for all `J < sqrt6/2`. Item 4 is `[numerical, 1e-9]` verification of the bound, not a
proof of it.

**Reading, not theorem.** Two facts about the box -- six neighbours per site and two colours -- fix a floor that no arrangement of signs and no number of particles can go below, at any price. On the `4^3` box, and for every price up to about `0.61`,
the half-filled minus-on-every-square sea sits exactly on that floor. It is not merely the best thing tried; nothing could be better.

## Theorem 6 -- how long exactly half filling survives

**Conclusion.**

1. Exactly half filling survives on the `4^3` torus for `J_B < 4 sqrt6 - 3 - 3 sqrt2 - sqrt3 = 0.823267` when the twist is chosen freely at each `J_B`, and for `J_B < sqrt6/2 = 1.224745` within the half-filling twist itself.
2. On `6^3` the twist-minimised window is `J_B < 2 sqrt3 - 3 = 0.464102`, and on `8^3` it is `J_B < 0.306846`. The window shrinks with the box.
3. In the thermodynamic limit it closes. The staggered band `-sqrt(6 + 2 sum_a cos q_a)` vanishes at `q = (pi, pi, pi)` and only there, and near that point `6 + 2 sum_a cos q_a = |k|^2 + O(|k|^4)`, so for every `J_B > 0` the emptied region `|k| < 2
   J_B` has positive measure: exactly half filling survives only at `J_B = 0`, with `1/2 - n(J_B) -> (2/(3 pi^2)) J_B^3`. The measured ratio of `1/2 - n(J_B)` to that cubic is `0.9663, 1.0215, 1.0258` at `J_B = 0.15, 0.2, 0.3`.

**Proof.** Items 1 and 2 bisect on the twist-minimised occupancy and check the surds to `1e-8`. Item 3's series expansion is exact in `sympy`; the ratios are `[numerical]` on the `L = 224` Bloch grid. At `J_B = 0.001` that grid cannot resolve the
effect: the emptied ball has radius `0.002` against a grid spacing of `2 pi / 112`, so the grid reports `n = 0.4999996`, which is its own `n(0)`. The statement that the sea is doped at every positive `J_B` is the analytic one, not a grid reading.

**Reading, not theorem.** In a finite box exactly half filling is stable: it takes a real price to empty the topmost level, because the topmost level is a real distance below zero. In an unbounded lattice there is no such distance -- the band touches
zero -- so any price at all, however small, empties a little of the sea. The window in which the lattice is exactly half full closes as the box grows.

## Corollary -- the vacuum question is the value of one coefficient

Within the setting declared above, and on the finite blocks and tori named:

1. The law's `B_i` term type, given the coefficient the law leaves blank, is a **pure chemical potential**: `-J_B sum_i B_i = -J_B V + 2 J_B N`, a price of `2 J_B` per fermion and nothing else. It adds no motion, no interaction and no scale beyond
   the ratio `J_B/t`.
2. At `J_B = 0` the law's own ground state, over all record numbers and all flux sectors, is the **half-filled staggered sea** -- provably on the cube, provably against all link-sign fields on the `4^3` torus, and as a search result elsewhere.
3. At `J_B/t >= 3` the ground state is the **empty lattice**, on every cluster here and in the limit. The plain sector is the last to empty and it empties exactly at `3`.
4. Between the two the ground state is a partially filled sea whose filling falls continuously with `J_B`, and which changes flux sector at `J_B* ~ 0.865`: `sqrt3/2` exactly on `4^3`, `0.8654003` in the limit.
5. So the two branches PR #7879 names are the two ends of one interval, and the framework's vacuum question is the value of a single dimensionless coefficient `J_B/t` that the law as written does not fix. What PR #7874 calls a supplied datum
   sharpens: **`J_B/t` is the supplied datum, and the filling follows from it.** The owner's decision is therefore the size of the occupancy cost; nothing here chooses it and nothing here narrows it.

**Reading, not theorem.** Ask how much it costs to have a particle at a site. If the answer is nothing, the lattice fills itself halfway with a sea of matter and the minus-sign pattern comes with it. If the answer is more than three hopping units,
the lattice stays empty. In between it fills part way. The law as written does not say what the cost is; that one number is the vacuum question.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. No status value is set, predicted, or implied, and no premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The coarse lattice, the encoding, the sign fields, the occupancy term and its coefficient are declared objects, and the theorems are about them.
- No vacuum is chosen and no value of `J_B/t` is preferred, proposed, estimated or bounded by anything physical. Both ends of the interval are supplied and neither is adopted.
- No mass, no absolute unit, no interaction, no temperature, no formation rate and no dynamical clause appears anywhere. `t = 1` is a choice of unit for the ratio `J_B/t`, not a value.

## Interfaces named for other lanes, not moved here

- **The value of `J_B/t`.** This is a science question, not a residual: which known physics the coarse lattice must reproduce is what would fix it. A lane owning the framework's ground state should decide it; Corollary items 2 to 4 hand that lane the
  full consequence map, and nothing here narrows the choice.
- **Interactions.** Only free hopping plus a diagonal occupancy term is compared. A four-fermion term, or any interaction, could move the crossover and the thresholds, and no such term is examined.
- **The gapless limit.** Theorem 6 item 3 is an infinite-volume subtlety and is named as one: in a finite box exactly half filling has a window, and in the limit the window is the single point `J_B = 0`. A lane wanting a half-filled sea at positive
  cost in infinite volume owns that tension.
- **Global minimality beyond `4^3` and the cube.** Theorem 5 is a theorem on the `4^3` torus for `J_B <= sqrt(3/8)` and Theorem 2 item 2 an exhaustion on the cube. Everywhere else the corresponding statement is a search result at the runner's fixed
  seeds.
- **The Wilson-line convention.** Every torus quantity is minimised over the eight twists at each `J_B`; which twist a physical setting selects is not decided here.
- **The many-body energetics.** Only the one-particle ladder is used, the ground state of the free problem at fixed `J_B`.

## Remaining live routes

1. The interval's interior. The crossover and the thresholds are computed; what a partially filled sea implies for the results conditioned on either vacuum is not.
2. Larger blocks and other geometries. Three tori, two open blocks and the Bloch limit are what is here.
3. Finite temperature. Everything is a ground-state energy at fixed coefficient, and every sector ties at `W = 0` once the lattice is empty.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one mode per coarse vertex, BK superfast encoding, free nearest-neighbour hopping t = 1 plus the declared occupancy term -J_B sum_i B_i; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
chemical_potential: [sum_k B_k, T_ij] = -i (B_i^2 - B_j^2) A_ij = 0 exactly; 0 wrong signs over 16029 (hop, site) Pauli pairs on open 2x2x2, open 3x3x3, torus 3^3, torus 4^3; dense 16-dim block ||[sum B, T]|| = 0 vs ||[B_i, T]|| = 2; (V I - sum B)/2 = N integer; -J_B sum_i B_i = -J_B V + 2 J_B N
bipartite: every cluster bipartite degree 6; spectra symmetric to 3.4e-14; min_N E_N = E_{V/2} with ties [#neg, #neg + #zero]; plain 4^3 untwisted 20 zero modes, ties N in [22, 42]
j0_cube: all 32 sectors x all N -> -4 sqrt3, unique at all-(-1), N = 4, margin 0.456067
j0_tori: 4^3 -32 sqrt6 = the Cauchy-Schwarz floor over ALL link-sign fields (16 twisted uniform + 5 structured + 1000 random); 6^3 -258.857540 (16 + 300 random, best random -230.81); 8^3 -611.811768; open 3x3x3 -26.040600 vs plain -21.213203
crossover: J_B* = sqrt3/2 exactly on 4^3 (stag KS W = -24 - 24 sqrt2 - 8 sqrt3 + 56 J, plain (0,1,1) W = -24 - 24 sqrt2 + 40 J, difference 16 J - 8 sqrt3); 0.849332 on 6^3; 0.867676 on 8^3; 0.8654003 +- 3e-6 in the limit, fillings 0.4417 and 0.2521
thresholds: plain empties at J_B = 3 exactly (bottom -6 at (pi,pi,pi)), staggered at sqrt3, on 4^3, 6^3, 8^3 and in the limit; open 3x3x3 3 sqrt2/2 and sqrt6/2; cube 3/2 with all 32 tying at W = 0; cube all-(-1) loses to the 2-flux class at sqrt3 - (1 + sqrt2)/2 = 0.524944
certificate: any bipartite degree-6 field has tr M^2 = 6V and D M D = -M, so W(J) >= -V sqrt(3/2) + J V for J <= sqrt(3/8) = 0.612372 and -3V/(8J) above; the 4^3 flat-twist staggered sea has W = 64 J - 32 sqrt6 and attains it with slack <= 7e-15 at every J_B <= sqrt(3/8); 0 violations over 1021 fields at 16 values of J_B
half_filling_windows: 4^3 J_B < 4 sqrt6 - 3 - 3 sqrt2 - sqrt3 = 0.823267 twist-minimised and sqrt6/2 within the half-filling twist; 6^3 2 sqrt3 - 3 = 0.464102; 8^3 0.306846; limit only J_B = 0, gapless at (pi,pi,pi), 1/2 - n(J_B) -> (2/(3 pi^2)) J_B^3, ratios 0.9663, 1.0215, 1.0258 at J_B = 0.15, 0.2, 0.3
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=24 FAIL=0
```

## Proof boundary

The content is **free nearest-neighbour hopping plus one declared diagonal term**, on **finite** clusters and a converged Bloch grid. The occupancy term `-J_B sum_i B_i` and its coefficient are **declared by this note**; no axiom supplies them, no
axiom forbids them, and nothing here derives either. `t = 1` fixes the unit in which `J_B` is read and is not a physical value.

Global minimality over all link-sign fields is a **theorem on exactly two clusters**: the open `2x2x2` cube, by exhaustion of its `32` sectors at every `N`, and the `4^3` coarse torus, by the extended Cauchy-Schwarz certificate, and there only for
`J_B <= sqrt(3/8)`. On `6^3`, on `8^3` and on `4^3` above `sqrt(3/8)` the corresponding statement is a **search result** -- a statement about the fields drawn at the runner's fixed seed, not about the whole space.

The crossover value is exact only on the `4^3` torus. `0.849332`, `0.867676` and `0.8654003` are numerical, the last from Bloch quadrature whose `L` sequence `128, 160, 192, 224` settles within `3e-6`. Nothing here claims a limit theorem; the limit
numbers are converged quadrature.

Theorem 6 item 3 is the one place a finite-cluster reading and an infinite-volume reading differ, and the difference is stated rather than smoothed: on every finite cluster exactly half filling survives a positive window of `J_B`, and in the limit it
survives only at `J_B = 0`. At `J_B = 0.001` the `L = 224` grid cannot see the doping at all, and the runner says so rather than reporting the grid's own `n(0)` as a physical value.

No claim is made that any value of `J_B/t` is right, likely, natural or excluded. The interval `[0, 3]` and its interior structure are what is computed; which point of it the framework means is not a residual this note leaves open by accident, but a
decision it hands over on purpose.

## Review record

An honest auditor should come away with: one exact commutation theorem showing that the law's uncoefficiented `B_i` term, given any coefficient, is a chemical potential and nothing more; one exhaustive statement that at zero coefficient the law's own
ground state is the half-filled staggered sea, with a genuine certificate making that a global statement over all link-sign fields on the `4^3` torus and, extended, over all fillings too for every `J_B` up to `sqrt(3/8)`; one exact crossover at
`sqrt3/2` on that torus with its thermodynamic value `0.8654003`; the exact emptying threshold `3`; a clearly labelled band of search results away from the two certified clusters; and the honest limit that the half-filling window closes as the box
grows because the staggered band is gapless.

The three things most likely to be over-read are flagged in the proof boundary: the occupancy term is declared and not derived, so nothing here says the framework *has* such a term; global minimality is a theorem on two clusters and, on `4^3`, only
below `sqrt(3/8)`; and the gapless limit means the *exactly* half-filled sea is not the ground state at any positive cost in infinite volume. This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no
hypothesis is adopted, and the four context notes in "Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at `PASS=24 FAIL=0`, runtime under the declared
`120` seconds, stdout under `5500` characters, and passing pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
