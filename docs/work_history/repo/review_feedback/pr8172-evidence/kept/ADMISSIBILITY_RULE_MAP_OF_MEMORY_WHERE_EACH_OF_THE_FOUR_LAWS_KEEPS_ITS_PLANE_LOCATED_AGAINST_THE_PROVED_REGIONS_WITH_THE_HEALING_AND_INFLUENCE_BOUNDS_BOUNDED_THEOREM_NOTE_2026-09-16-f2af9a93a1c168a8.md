---
claim_id: admissibility_rule_map_of_memory_where_each_of_the_four_laws_keeps_its_plane_located_against_the_proved_regions_with_the_healing_and_influence_bounds_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "For the covariant product rule on the six-axis menu with weights (p, q, r) and on the unsoldered sphere menu with weight e^{beta s.s'}, under the static reading (the Gibbs law on Z^3) and the formation reading in level order (the level automaton on Z^2): (T1) at (p, 1, 2), block 08's uniqueness criterion 3c < 1 for the formation law holds at p = 37/10 and fails at p = 19/5 (c the exact total-variation sensitivity of the conditional to one predecessor), and block 25's ordering condition epsilon(p, 1, 2) <= 7/10^6 holds from p = 285718 (proved; exact rationals); (T2) for the noisy majority automaton at noise epsilon, an island of ones at level 0 with coordinate maxima M_i, D = M_1 + M_2 + M_3, is empty at level D + 1 under the noiseless rule, and under noise it has a one in its forward cone at level D + 1 only if a noise site lies in a region of at most 18 (D + 1)^3 sites, so the island survives with probability at most 18 (D + 1)^3 epsilon (proved; the eroder bound re-proved, the region counted exactly on random islands); (T3) for the sphere formation law, two initial planes differing at one site x_0 give coupled records at x of level t at expected chordal distance at most 2 (sqrt3 beta)^t p_t(x - x_0), p_t the level walk's law (proved). Executed, not proved (the map): on periodic planes and lattices, the six-axis formation law at (p, 1, 2) keeps its aligned plane from a strength between 10.5 and 11 (128^2 and 256^2 planes, 4000-8000 levels) against the proved region p >= 285718 and uniqueness for p <= 37/10; the six-axis static law keeps a majority value from a strength between 3.6 and 3.7 (16^3, 24^3, 32^3 lattices, aligned and random starts, heat bath and single-site proposals) against the proved region p >= 432 at (p, 1, 2) and uniqueness at (3, 1, 2); the sphere static law keeps a magnetization from beta between 0.66 and 0.72 (16^3, 24^3) against the proved region beta > 76/100 and uniqueness for beta < sqrt3/6; the sphere formation law loses its plane at every beta tried (block 26) against uniqueness for beta < 1/sqrt3 (block 27). The static reading keeps memory at about a third of the preference strength the formation reading needs on the six-axis menu. No menu, reading, order or coupling is selected as physical; exact arithmetic throughout the runner."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_bounds_2026_09_16.py
---

# The map of memory: where each of the four laws keeps its plane, located against the proved regions, with the healing and influence bounds

**Date:** 2026-09-16
**Type:** bounded_theorem (T1–T3); frontier discovery for the executed map
**Status:** bounded-support (exact; conditional on the named supplied readings; the located strengths executed on finite planes and lattices, not proved; unaudited)

## Result up front

The campaign has, for each of its four laws — two menus (the six axes and the
sphere) under two readings (static and formation) — a proved region of weak
preference where every arrangement of records forgets where it started, and,
for three of them, a proved region of strong preference where a plane of
identical records is kept. The proved regions are far apart: on the six-axis
menu at weights `(p, 1, 2)` the formation law is proved to forget for
`p ≤ 3.7` (block 08) and to keep its plane for `p ≥ 285718` (block 25); the
static law is proved to forget at `(3, 1, 2)` (block 03) and to keep a majority
for `p ≥ 432` (block 17); the sphere static law forgets for `β < 0.289` (block
21) and keeps a magnetization for `β > 0.76` (block 22); the sphere formation
law forgets for `β < 0.577` (block 27) and, in the runs of block 26, at every
`β` tried. This note locates the actual strengths by simulation and places the
proved regions against them.

The map. At `(p, 1, 2)` the six-axis static law keeps a majority value from a
preference strength between `3.6` and `3.7`, and the six-axis formation law keeps
its aligned plane from a strength between `10.5` and `11`: the static reading
keeps memory at about a third of the strength the formation reading needs. The
sphere static law keeps a magnetization from `β` between `0.66` and `0.72`; the
sphere formation law never does (block 26). Block 17's `432` is about a
hundred times the static strength; block 25's `285718` is twenty-five thousand
times the formation strength; block 22's `0.76` is within a tenth of the sphere's
strength; block 08's `3.7` for the formation law happens to sit where the
*static* law's strength lies — a coincidence of this line of weights, not a
relation. In plain words: laying records down one after another costs about
three times the preference for agreement that a single settled arrangement
costs, before a memory holds; and with a sphere of directions the settled
arrangement holds from a modest preference while the record-by-record one
never does.

Two exact corollaries anchor the map. The healing bound (T2): in the ordered
regime of the formation reading, an island of dissent of size `D` is erased
within `D + 1` levels unless a noise event falls in a region of `18(D + 1)³`
sites, so isolated errors heal with probability `1 − 18(D + 1)³ε`. The
influence bound (T3): under the sphere formation law, one changed initial
record influences the record at level `t` and in-plane displacement `y` by at
most `2(√3β)^t p_t(y)` — confined to the forward cone, spread like the directed
heat kernel, and, below `β = 1/√3`, shrinking exponentially with the level.

Exactly: the brackets of the proved regions at `(p, 1, 2)` (T1); the healing
bound (T2); the influence bound (T3). Executed with exact arithmetic: 14 checks,
8 mutations; the map in the control and refuter specs (two plane sizes, three
lattice sizes, two starts, two algorithms).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "the campaign's decision record: which reading and which menu keep memory at what strength of preference — the proved regions (blocks 03, 08, 17, 21, 22, 25, 27) leave the actual strengths unlocated"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem_plus_decisive_artifact
next_trace_action: "the map located: six-axis static from p in (3.6, 3.7), six-axis formation from p in (10.5, 11) at (p, 1, 2); sphere static from beta in (0.66, 0.72); sphere formation never (block 26). Open: the true strengths as theorems (the proved regions are 10^2 to 10^4 away on the six-axis menu); the six-axis formation law's transition on a larger plane. Consumers: the campaign's decision record; #8093's assembly"
conditional_surface_status: "T1-T3 proved as stated under the records-only reading, positivity, the six-axis and sphere menus and the monotone level order as supplied conditions; the located strengths executed on periodic planes (128^2, 256^2) and lattices (16^3, 24^3, 32^3), brackets not proved values; two standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and "Only records are readable.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the rule's product form and its one-site conditional given a recorded set; the menus, the two readings and the level automaton are declared below (blocks 03, 08, 12, 17, 18, 19, 21, 22, 25, 26, 27 — open PRs #8000, #8138, #8146, #8151, #8152, #8153, #8155, #8156, #8168, #8170, #8171 — are referenced as evidence addresses only). All proposed and unaudited.

Declared objects.
- **The six-axis law.** Values in `{±e_1, ±e_2, ±e_3}`; `φ(v, v') = p, q, r` for equal, antipodal, orthogonal pairs (`p, q, r > 0`); the weights `(p, 1, 2)` throughout the map. **Static reading:** the Gibbs law on a periodic `L³` lattice with density `∝ Π_{bonds} φ(v_x, v_y)`; its single-site conditional given the six neighbours is `∝ Π_{6} φ(v, v_y)`. **Formation reading:** the level automaton of blocks 12 and 25 — the record at `x` drawn from `K(· | v_{x−e_1}, v_{x−e_2}, v_{x−e_3}) ∝ Π_3 φ(v, v_{x−e_j})`, read as a synchronous automaton on the periodic `L²` level plane after the bijection of each level.
- **The sphere law.** Values in `S²`, weight `e^{β s·s'}`. **Static reading:** the Gibbs law on a periodic `L³` lattice with density `∝ Π_{bonds} e^{β s_x·s_y}`, single-site conditional the exponential-overlap law with concentration `β|Σ_6 s_y|`. **Formation reading:** block 26's level automaton (the conditional with concentration `β|Σ_3 s_{x−e_j}|`).
- **Memory and order.** Formation: the aligned plane (all records equal to a value `a`, or a direction `e`) at level `0`; the **memory** at level `t` is the fraction of records equal to `a` (six-axis) or the mean of `s·e` (sphere). Static: from an aligned or random start, heat-bath sweeps (each site redrawn from its conditional given its six neighbours, on a checkerboard) or single-site proposals accepted with the ratio of weights; the **order** is the fraction of the majority value (six-axis) or `|mean s|` (sphere) over the second half of the sweeps.
- **The noisy majority automaton and islands.** As in block 25: `η_x = maj(η_{x−e_1}, η_{x−e_2}, η_{x−e_3}) ∨ ζ_x`, `ζ` i.i.d. Bernoulli(`ε`) on levels `≥ 1`; an **island** is a finite set `I` of ones on level `0` (zeros elsewhere), with coordinate maxima `M_i = max_I x_i`, `D = M_1 + M_2 + M_3 ≥ 0`; its **forward cone** at level `T` is `F_T(I) = {x : τ(x) = T, x ≥ i for some i ∈ I}` (coordinatewise); the **noise-sensitive region** `U(I) = {y : 1 ≤ τ(y) ≤ D + 1, y ≤ x for some x ∈ F_{D+1}(I)}`.
- **The level walk and the causal coupling.** As in blocks 26 and 27: `p_t(y)` the law of the three-predecessor walk after `t` steps; the causal coupling of two runs of the sphere formation law with per-site expected chordal distance `D_t(x)`.
- **Block 08's criterion.** `c(p) = max` over predecessor triples `(a, b, c)` and alternatives `a' ≠ a` of `TV(K(·|a, b, c), K(·|a', b, c))`; uniqueness holds when `3c < 1`. **Block 25's condition.** `ε(p, q, r) = max(d_1, d_2, d_3)` with the three deviations in closed form; the ordered phase is proved for `ε ≤ 7/10⁶`.

## Prior art and what is new

Locating transitions of lattice models by simulation is standard practice; the sphere static law is the classical Heisenberg model on the cubic lattice, whose transition is known in the literature (`β_c ≈ 0.693`), and the six-axis static law is a six-state model with cubic anisotropy of the Potts family; the formation law is a probabilistic cellular automaton of Toom's family. None of this is used as authority: the strengths are re-measured here with the campaign's own rules, on small lattices, and stated as brackets. What is new: (i) the map itself — the four laws' strengths on one line of weights, placed against the campaign's proved regions, with the ratio between the readings; (ii) the healing bound (T2), an exact corollary of block 12's eroder theorem with a coupling and a count; (iii) the influence bound (T3), an exact corollary of block 27's contraction with a localized initial difference; (iv) the exact brackets of blocks 08 and 25 at `(p, 1, 2)` (T1).

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | `3c < 1` at `37/10`, `> 1` at `19/5`; `ε ≤ 7/10⁶` from `285718` | exact rationals | B |
| T2 | the eroder bound; `|U(I)| ≤ 18(D + 1)³`; `P(survival) ≤ 18(D + 1)³ ε` | coordinate maxima; a coupling; a box count | C |
| T3 | `D_t(x) ≤ 2(√3β)^t p_t(x − x_0)` | block 27's contraction with a localized start | D |
| executed | the map | simulation (control, refuter) | — (specs) |

## Theorem T1 — the proved regions on the line `(p, 1, 2)`

**Statement.** `3c(37/10) = 406962630/413162167 < 1` and `3c(19/5) = 871815/862244 > 1`, so block 08's criterion on this line holds up to a `p` between `3.7` and `3.8`. `ε(p, 1, 2) ≤ 7/10⁶` holds at `p = 285718` and fails at `285717`.

**Proof.** `c(p)` is a maximum of finitely many rational functions of `p`, evaluated exactly at the two points over the `216` triples and the five alternatives at each (B1); the deviations are block 25's closed forms `d_1 = (q³ + 4r³)/(p³ + q³ + 4r³)`, `d_2 = 1 − p²q/(pq(p + q) + 4r³)`, `d_3 = 1 − p²r/(r(p² + q²) + r²(p + q) + 2r³)`, evaluated exactly (B2). ∎

## Theorem T2 — the healing bound

**Statement.** Under the noiseless majority rule an island `I` is empty at level `D + 1`. Under noise `ε`, `P(η has a one in F_{D+1}(I)) ≤ |U(I)| ε ≤ 18(D + 1)³ ε`.

**Proof.** *The eroder bound* (block 12's S2, re-proved). If `x` is a one at level `t + 1` with `x_i > M_i(t)` for some `i`, then its two predecessors `x − e_j`, `j ≠ i`, have `i`-th coordinate `x_i > M_i(t)` and are zeros, so `x` has at most one one-predecessor and is not a majority: the coordinate maxima never increase. A one at level `t` has `Σ_i x_i = t` and `x_i ≤ M_i`, so `t ≤ D`: level `D + 1` is empty (C1). *The coupling.* Run the noisy and the noiseless automata with the same island. If no noise site lies in `U(I)`, then by induction on the level every site of `U(I)` and every site of `F_{D+1}(I)` — whose predecessors down to level `1` lie in `U(I)` — carries the same value in both runs, so `F_{D+1}(I)` carries no one. Hence the event has probability at most `P(ζ = 1 somewhere in U(I)) ≤ |U(I)| ε`. *The count.* A site `y ∈ U(I)` at level `s ∈ [1, D + 1]` satisfies `y ≤ x` for some `x` at level `D + 1` with `x ≥ i`, `i ∈ I`; then `x_j = D + 1 − Σ_{k≠j} x_k ≤ D + 1 − Σ_{k≠j} i_k = D + 1 + i_j ≤ 2D + 1`, so `y_j ≤ 2D + 1 =: B` for each `j`. The number of `y` at level `s` with all `y_j ≤ B` is the number of non-negative `d_j = B − y_j` with `Σ d_j = 3B − s`, i.e. `C(3B − s + 2, 2) ≤ C(6D + 5, 2) = (6D + 5)(6D + 4)/2`; over `D + 1` levels, `|U(I)| ≤ (D + 1)(6D + 5)(6D + 4)/2 ≤ 18(D + 1)³`, the difference being `(D + 1)(9D + 8)` (C2). ∎ (Executed: the exact `|U(I)|` on `120` random islands is at most `4.05(D + 1)³`; the refuter tests the survival frequency of triangular islands at `ε = 10^{−3}` against the bound.)

*Reading.* In the ordered regime of the formation reading, dissent heals: an error of size `D` is gone within `D + 1` levels unless noise strikes a region of a few thousand sites around it. This is the mechanism behind block 25's stability, isolated as a finite statement.

## Theorem T3 — the influence bound

**Statement.** For the sphere formation law at any `β > 0`, let two initial planes differ at `x_0` only. Under the causal coupling of block 27, the per-site expected chordal distance at `x` of level `t` satisfies `D_t(x) ≤ 2(√3β)^t p_t(x − x_0)`, and `Σ_x D_t(x) ≤ 2(√3β)^t`.

**Proof.** Block 27's T2 gives `D_{t+1}(x) ≤ (β/√3) Σ_j D_t(x − e_j)` with `D_0 = 2·1{x = x_0}`; the linear recursion is solved by `2(β/√3)^t · 3^t p_t(x − x_0) = 2(√3β)^t p_t(x − x_0)` (the walk's law is the `t`-fold convolution of the uniform step over the three predecessors), and the sum over a level of `p_t` is `1` (D1). ∎

*Reading.* Influence is confined to the forward cone and spreads as the directed heat kernel of block 13; below `β = 1/√3` it also shrinks exponentially with the level. Above, the bound is trivial, and block 26's runs show the field itself forgetting.

## Executed: the map (frontier discovery, not proved)

Controls `specs/supervisor_control_block28_scan_formation_sixaxis.py` (the level automaton from the aligned plane; memory over the second half of the levels), `..._scan_static_sixaxis.py` (heat-bath sweeps on a checkerboard from aligned and random starts), `..._scan_static_sphere.py` (heat-bath sweeps with the exact conditional), `..._exact.py`; refuting spec `specs/supervisor_control_block28_refuter.py` (the formation law from a random start — spontaneous order; the static six-axis law by single-site proposals; the sphere static law from a random start; the healing bound tested). Outputs in `.out.txt`.

| law | runs | memory or order along the scan | located strength | proved regions (blocks) |
|---|---|---|---|---|
| six-axis formation `(p, 1, 2)` | `128²`, `4000` levels | `4`: 0.1666 `6`: 0.1662 `8`: 0.1670 `10`: 0.1660 `12`: 0.9325 `15`: 0.9792 `18`: 0.9902 `22`: 0.9953 `26`: 0.9974 `30`: 0.9984 `35`: 0.9990 `40`: 0.9994 `50`: 0.9997 `60`: 0.9998 `80`: 0.9999 | `p ∈ (10.5, 11)` | forgets for `p ≤ 3.7` (08); keeps for `p ≥ 285718` (25) |
| six-axis formation `(p, 1, 2)` | `256²`, `8000` levels | `15`: 0.9793 `18`: 0.9902 `22`: 0.9954 `26`: 0.9974 `30`: 0.9984 `35`: 0.9990; fine: `9`: 0.1663 `10`: 0.1670 `10.5`: 0.1706 `11`: 0.8443 `11.5`: 0.9064 `12`: 0.9324 `13`: 0.9582 | `p ∈ (10.5, 11)` | — |
| six-axis static `(p, 1, 2)` | `16³`, `1500` sweeps, aligned/random | `1.5`: 0.1747/0.1749 `2`: 0.1762/0.1764 `2.5`: 0.1785/0.1785 `3`: 0.1827/0.1825 `3.5`: 0.1963/0.2016 `4`: 0.8781/0.8775 `5`: 0.9794/0.9793 `6`: 0.9940/0.9939 `8`: 0.9990/0.4991 | `p ∈ (3.6, 3.7)` | forgets at `(3, 1, 2)` (03); keeps for `p ≥ 432` (17) |
| six-axis static `(p, 1, 2)` | `24³`, `1500`–`2000` sweeps | `2`: 0.1720/0.1719 `2.5`: 0.1733/0.1731 `3`: 0.1754/0.1755 `3.5`: 0.1842/0.1857 `4`: 0.8774/0.8766; fine: `3.5`: 0.1821/0.1844 `3.6`: 0.1908/0.1894 `3.7`: 0.6717/0.6744 `3.8`: 0.7837/0.7832 `3.9`: 0.8407/0.8408 `4`: 0.8772/0.8768 | `p ∈ (3.6, 3.7)` | — |
| six-axis static `(p, 1, 2)` | `32³`, `2000` sweeps | `3.6`: 0.1836/0.1826 `3.7`: 0.6764/0.6730 `3.8`: 0.7833/0.7845 `3.9`: 0.8401/0.8403 | `p ∈ (3.6, 3.7)` | — |
| sphere static | `16³`, `1500` sweeps | `0.5`: 0.0355 `0.6`: 0.0569 `0.65`: 0.0915 `0.7`: 0.3050 `0.75`: 0.4607 `0.8`: 0.5362 `0.9`: 0.6269 | `β ∈ (0.65, 0.70)` | forgets for `β < 0.289` (21); keeps for `β > 0.76` (22) |
| sphere static | `24³`, `1500`–`2000` sweeps | `0.6`: 0.0305 `0.65`: 0.0580 `0.7`: 0.2343 `0.75`: 0.4413; fine: `0.66`: 0.0676 `0.68`: 0.1144 `0.7`: 0.2534 `0.72`: 0.3607 | `β ∈ (0.66, 0.72)` | — |
| sphere formation | block 26 (`512²`, `20000` levels) | memory lost at `β = 3, 6, 12, 24` | none | forgets for `β < 0.577` (27) |


What the runs say. (i) The six-axis formation law at `(p, 1, 2)` forgets its plane (memory `1/6`) up to `p = 10.5` and keeps it from `p = 11` on the `256²` plane (`10` and `12` on `128²`); from a random start the majority fraction grows from `p ≈ 11` on, more slowly because domains must merge (refuter). (ii) The six-axis static law is disordered at `p = 3.6` and ordered at `p = 3.7` on all three lattice sizes, from both starts and under both algorithms. (iii) The sphere static law's magnetization rises between `β = 0.66` and `0.72` on both lattices (`0.11` at `0.68`, `0.25` at `0.70` on `24³`), consistent with the literature value named under Prior art. (iv) The healing frequencies of triangular islands at `ε = 10^{−3}` (`0.003, 0.055, 0.098, 0.198` for sides `1`–`4`, `D = 0, 2, 4, 6`) lie below the bound of T2 (`0.018, 0.49, 2.25, 6.2`). **The map (executed):** static six-axis `p ∈ (3.6, 3.7)`; formation six-axis `p ∈ (10.5, 11)`; static sphere `β ∈ (0.66, 0.72)`; formation sphere: none (block 26). The proved regions are placed in the table's last column.

## No-Go Discipline Gate

The executed sentence locates strengths; its escapes are named.

### N1 — Routes by which the map could be wrong
1. *Finite size.* Two plane sizes and three lattice sizes give the same brackets; the located strengths are stated as brackets, not digits.
2. *Hysteresis and equilibration of the static six-axis law.* Aligned and random starts agree at every strength in the table except at strong preference from a random start, where domains freeze (`p = 8` on `16³`: two domains of half the lattice each), which does not affect the bracket; heat bath and single-site proposals agree.
3. *The memory observable of the formation law.* The fraction of the initial value over the second half of the run; a plane that will forget later than the run cannot be excluded (block 26's `L²` scale is far beyond the run for the six-axis law's dissent-free plateaus).
4. *The proved regions.* Re-computed exactly where a number is quoted (T1); the others are evidence addresses.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's rule, the menus, readings and orders as declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the four sentences under Premises | yes (premise) |
| block 01 (`main`) | the rule and its one-site conditional | yes (premise, proposed) |
| blocks 08, 12, 25, 27 (open PRs) | the criterion, the eroder bound, the ordering condition, the contraction | re-computed or re-proved at scope where used (T1–T3) |
| blocks 03, 17, 19, 21, 22, 26 (open PRs) | the other proved regions; the sphere formation runs | placement only (evidence addresses) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "where each law keeps its plane" | executed: the exact sensitivity at two couplings; the deviations at two couplings | executed: the eroder bound on random islands; the influence recursion | executed: the region count on random islands; the polynomial inequality | executed: the map by simulation on two plane sizes, three lattice sizes, two starts, two algorithms | T1–T3 proved as stated; the strengths executed brackets |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling, menu or order; none is a wall.

### N7 — Steelman
Hostile reviewer: "Simulations on `16³` lattices and `128²` planes prove nothing; the theorems are corollaries." Reply: the map is the number the decision record needs and it is labelled executed with brackets; the corollaries are new statements (a finite healing bound, a finite influence bound) with proofs. Conceded: the true strengths are not theorems, and the proved regions on the six-axis menu are two to four orders of magnitude away from them.

### N8 — Cross-cycle echo
Blocks 03, 08, 21, 27 (the uniqueness table), 17, 22, 25 (the ordering regions) and 26 (the sphere formation runs) are the eight facts the map is drawn against; block 12's eroder is T2's core; block 27's contraction is T3's.

## Falsifiers
- `3c(37/10) ≥ 1` or `3c(19/5) ≤ 1`; `ε(285718, 1, 2) > 7/10⁶` or `ε(285717, 1, 2) ≤ 7/10⁶` (B1–B2).
- An island alive at level `D + 1` under the noiseless rule, a coordinate maximum that increases, a region `U(I)` above `18(D + 1)³`, or a negative coefficient in `18(D+1)³ − (D+1)(6D+5)(6D+4)/2` (C1–C2).
- An influence solution differing from `2(√3β)^t p_t` (D1).
- For the map: a plane kept below the stated bracket or lost above it on a larger plane or lattice or a longer run; a healing frequency above `18(D+1)³ε`.

## Boundaries and non-claims
This note proves, at `(p, 1, 2)`, the exact brackets of block 08's uniqueness criterion (`3c < 1` at `p = 37/10`, `3c > 1` at `19/5`) and of block 25's condition (`ε ≤ 7/10⁶` from `p = 285718`), the healing bound `P(an island with D = M_1 + M_2 + M_3 survives to level D + 1 in its forward cone) ≤ 18(D + 1)³ ε` for the noisy majority automaton, and the influence bound `2(√3β)^t p_t(x − x_0)` for the sphere formation law; the located strengths at which the four laws keep their planes are executed by simulation and are brackets, not proved values; it does not select a menu, reading, order or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

Further: the strengths on other lines of weights are not treated; the order of the static six-axis change (first or second order) is not claimed; nothing is claimed about which reading is physical.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and its conditional; proposed, unaudited. PRs #8000, #8138, #8146, #8151, #8152, #8153, #8155, #8156, #8168, #8170, #8171 (open) referenced as evidence addresses for the proved regions and the declared objects.
- Re-proved at scope: block 12's eroder bound; the coupling of noisy and noiseless runs on a noise-free region; block 27's contraction with a localized start.
- Named standard imports at definition level (never as authority for physics): the union bound; the heat-bath (Gibbs sampler) and single-site-proposal (Metropolis) chains as samplers of the static laws on finite lattices.
- Reference only (named, not used): the literature value of the classical Heisenberg model's transition on the cubic lattice (`β_c ≈ 0.693`); Toom's family of automata; the Potts family of models.

## Review record
Supervisor-run block (owner directive 2026-09-16: keep the campaign running twelve more hours). After block 27 the campaign held proved regions for all four laws but no located strengths; the map was the decision record's missing number and cheap to execute. The control ran the formation scan on `128²` (4000 levels) and `256²` (8000 levels), the static six-axis scan on `16³`, `24³`, `32³` from two starts, and the sphere scan on `16³`, `24³`, then fine scans around the changes; the exact control verified block 08's bracket, the eroder bound on `300` random islands, the exact region count (largest ratio `4.04(D+1)³` against the proved `18`), and the influence recursion. The lens pass is in `GOAL_block28.md`. Facts settled while executing: the first region count used a crude box (`16(D+1)³` unproved); the exact region and the proof's box give `18(D+1)³`; at `p = 8` from a random start on `16³` the static six-axis chain freezes into two domains (a known artifact of local dynamics at strong preference), which is why the aligned start is the map's reference. The refuting pass (`CHECKER_block28_findings.md`) used a random start for the formation law (spontaneous order), single-site proposals for the static six-axis law, a random start for the sphere law, and a direct test of the healing bound.

## Verification

```bash
python3 scripts/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_bounds_2026_09_16.py
python3 scripts/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_bounds_2026_09_16.py --list-mutations
python3 scripts/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_bounds_2026_09_16.py --mutation region_count_wrong
```

Families: A authority and inputs; B the brackets of the proved regions; C the healing bound; D the influence bound; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 8 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=14 FAIL=0`.
