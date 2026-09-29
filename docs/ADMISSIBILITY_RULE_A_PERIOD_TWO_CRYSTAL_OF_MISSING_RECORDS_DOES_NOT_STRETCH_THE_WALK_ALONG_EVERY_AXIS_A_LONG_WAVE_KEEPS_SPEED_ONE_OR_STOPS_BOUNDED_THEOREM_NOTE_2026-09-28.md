---
claim_id: admissibility_rule_a_period_two_crystal_of_missing_records_does_not_stretch_the_walk_along_every_axis_a_long_wave_keeps_speed_one_or_stops_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk H = sum_a sigma_a S_a on Z^3 as landed, with a supplied reading of 'a lower density of records at held sites' as a periodic set of sites with no record, and two supplied rules for the walker at such a site: R1 (its amplitude lives only on sites with a record; bonds to a site with no record are cut) and R3 (a hop goes to the nearest record along the axis). (T1) For a vacancy pattern whose period lattice lies in 2Z^3, the eight species fold to one point; if the zero-energy space there is exactly the species states that vanish on the vacancies (the kernel condition, which can fail: in the period-4 cell with vacancies (1,2,0), (1,3,0), (3,2,0) there are 14 zero modes, not 12, and first-order long waves along x and z of speed 5/sqrt(109)), then at first order in the wave number the long waves are h(q) = sum_a q_a A_a x sigma_a on the corners of {0,1}^3 not occupied by the vacancies' parity classes, A_a the direction-a adjacency of the remaining corners; for period 2 this holds at every wave number with q_a -> sin(Q_a/2), up to a phase change. (T2) For the taste cube with any set of corners removed (the long waves exactly at period 2, and at first order for longer periods that meet the kernel condition), along every coordinate axis every speed is exactly 1 or 0; for all but 24 of the 256 sets every characteristic polynomial is lambda^(2z) prod_S (lambda^2 - q_S^2)^(m_S), so every moving long wave has group speed exactly 1 within a coordinate line, plane or all of space; the 24 others (one class: the four remaining corners on a path turning through all three axes) have lambda^4 - |q|^2 lambda^2 + q_a^2 q_b^2 = 0 and slow oblique waves only; every wave is frozen exactly when the remaining corners are pairwise non-adjacent, first with the four classes of one sublattice (frozen means exactly flat at period 2, and at first order otherwise). (T3) Exact zero-energy flat bands number twice the sublattice imbalance in the checked period-4 cells; with period 3 one vacancy per cell removes the zero-energy doublet of every species. (T4) Under R3, with vacancies filling whole lines along the hop axis, the walk on the records is the undiluted walk, so in grid units its long waves move at the mean spacing, above one; with point vacancies in three dimensions R3's hops along different axes do not commute, so it is not a relabelling of the cubic walk. (T5) Random vacancies under R1: removing one site changes the resolvent by G T G with the local, coin-scalar T = -(E gbar(E))^-1, gbar(E) the mean of 1/(E^2 - eps_k^2); at first order in the concentration p the averaged self-energy is -p/(E gbar(E)), so the averaged energies depend on the wave only through its bare energy, their relative shift is not one number, and inside the band it is complex (waves damped); this first-order expansion holds only where |E|^2 is large against p/|gbar(E)|, so it says nothing about the longest waves. Exact (sympy, Gaussian rationals; all 256 sets; period 2 for all 21 classes; six period-4 cells including the counterexample; period 3; one vacancy on the 4^3 torus); T5's first-order average uses the concentration expansion (named). The supervisor's own derivation, unrefereed; nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_a_crystal_of_missing_records_does_not_stretch_the_walk_2026_09_28.py
---

# A period-two crystal of missing records does not stretch the walk: along every axis a long wave keeps speed one or stops; longer periods can slow some waves

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 54's walk as landed and two supplied rules for the walker at a site with no record; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within block 54's walk as landed and a supplied reading of a lower density of records; it reports whether an ordered pattern of sites with no record acts on the walk as a stretch of the lattice (third version, after a referee's corrections); nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The coupling axis of the third column asks how the walk responds when the lattice stretches with its sites held. Two answers are on the table.
- Under the frame, every energy scales down together.
- Under the free-particle rule (block 184, pushed), each wave slows continuously, while the band top stays fixed.

A panel (2026-09-28, same model family) proposed testing the owner's own reading. Records are the grain, so a stretch with sites held could mean fewer records on the same sites. That turns the supplied answer into a computation. The panel pre-registered five outcomes:
- the frame class;
- the free-particle class;
- a pure relabelling;
- waves speeding up;
- neither.

This note does the computation for an ordered pattern of sites with no record ("vacancies"), under two rules for the walker at such a site: R1, no amplitude there; R3, hop on to the next record.

- **T1: the long waves are the taste cube with corners removed.**
  - The walk's eight species sit at `K ∈ {0, π}³`. In the basis of parity classes (`x mod 2`) their long waves are `h(q) = Σ_a q_a X_a ⊗ σ_a` on the eight corners of the unit cube.
  - A vacancy constrains the species only through its parity class. Under R1 it deletes that corner.
  - For period 2 the long waves are exactly `Σ_a q_a A_a ⊗ σ_a` on the remaining corners, at every wave number, with `q_a → sin(Q_a/2)`.
  - For a longer period lattice in `2Z³` the same holds at first order when the zero-energy space is exactly the species states that vanish on the vacancies (the kernel condition). The condition can fail. In the period-4 cell with vacancies `(1,2,0), (1,3,0), (3,2,0)` there are 14 zero modes, not 12, and first-order long waves along `x` and `z` move at speed `5/√109 ≈ 0.48`.
- **T2: in the taste cube, along every axis a long wave keeps speed one or stops.** This describes the long waves exactly at period 2, and at first order for longer periods that meet the kernel condition.
  - Along any axis the speeds are exactly `1` or `0`, for every one of the 256 sets of occupied corners.
  - For all but 24 sets, every moving long wave has group speed exactly `1` within a coordinate line, a plane or all of space. The characteristic polynomial is `λ^{2z} Π_S (λ² − q_S²)^{m_S}`.
  - The 24 exceptions form one class: the four remaining corners lie on a path that turns through all three axes. Its waves obey `λ⁴ − |q|²λ² + q_a²q_b² = 0` and are slowed only off the axes. At `q = (1, 2, 3)` the squared speeds are `13/20 ∓ 3√5/20`.
  - Every wave is frozen exactly when the remaining corners are pairwise non-adjacent. That first happens with the four classes of one sublattice. Frozen means exactly flat at period 2, and flat at first order otherwise; a period-4 cell leaving only corners `000, 111` has bands quadratic in `Q`.
- **T3: flat bands and odd periods.**
  - The exact zero-energy states at a generic wave number number twice the sublattice imbalance in the four checked period-4 cells. A balanced pair leaves none.
  - With period 3, one vacancy per cell removes every species' zero-energy doublet.
- **T4: R3 is a relabelling only for line vacancies.**
  - When the vacancies fill whole lines along the hop axis, the walk on the records is the undiluted walk, and in grid units its long waves move at the mean spacing `n/(n − 1) > 1`.
  - With point vacancies in three dimensions, R3's hops along different axes do not commute, so it is not a relabelling of the cubic walk.
- **T5: random missing records damp the waves.**
  - Under R1, one missing record changes the walk's resolvent by `G T G`, with the local, coin-scalar `T = −(E ḡ(E))⁻¹`. Here `ḡ(E)` is the mean over wave numbers of `1/(E² − ε_k²)`. This is exact on the `4³` torus.
  - At first order in the concentration `p` of independently placed vacancies, the averaged energies solve `E + p/(E ḡ(E)) = ±ε(k)`. They depend on the wave only through its bare energy.
  - Their relative shift is not one number, and inside the band it is complex, so every wave there is damped.
  - A stretch does none of this.
  - The first-order expansion holds only where `|E|²` is large against `p/|ḡ(E)|`, so it says nothing about the longest waves.

What this means for the pre-registered outcomes.
- **R1, period 2: "neither".** No wave slows along an axis. Waves are removed, confined to lines or planes, or frozen, and the band top `√3` survives whenever a three-dimensional band does.
- **R1, longer periods: not settled.** Some patterns slow some waves (speed `5/√109` in the counterexample). Whether such slowing follows either class has not been compared.
- **R1, random patterns:** at first order in the density and away from the longest waves, damping and a shift set by the bare energy alone. That is neither class.
- **R3:** a relabelling or a speed-up (the panel's third and fourth outcomes) for line vacancies, and not a relabelling for point vacancies.

Reading lengths as record density therefore does not answer the coupling-axis question in the cases settled here. The member's lengths stay a supplied field.

In plain terms: suppose "the lattice stretched with its sites held" meant "some sites lost their records". Then, if the walker simply cannot sit where there is no record, a pattern of empty sites that repeats every two sites never makes a long wave slower along any axis. Each wave either keeps its full speed or stops. Patterns with longer repeats can trap extra states at the empty sites, and then some waves do slow. The empty sites remove some of the walker's ways of moving: some waves can then move only along a line or within a plane, and some cannot move at all. That is not what a stretch does to a wave under either answer on the table. If instead the walker skips empty sites, nothing changes except the labels, and the waves cover more ground per tick than the grid allows.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-28.
  - "Records form."
  - "A site never carries more than one record; records are permanent."
  - "A site with no record cannot be read."
  - The walk, the reading of a lower density of records, and the rules R1 and R3 are supplied clauses. Nothing is adopted.
- **The walk** (block 54 as landed, stated in landed block 135).
  - `(T_aψ)(x) = ψ(x + e_a)`, `S_a = (T_a − T_a⁻¹)/(2i)`, `H = Σ_aσ_aS_a`.
  - Near `K ∈ {0, π}³` it is `Σ_a cos K_a q_a σ_a`.
- **The reading, supplied.** "The lattice stretched with its sites held" is read as "some sites carry no record" (vacancies). The owner's reading is that records are the grain. Here the pattern of vacancies is periodic.
- **Rule R1, supplied.** The walker's amplitude lives only on sites with a record, and bonds to a site with no record are cut. For this continuous-time walk it coincides with "the coin loses that direction".
- **Rule R3, supplied.** A hop goes to the nearest record along the axis.
- **The pre-registered classes** (panel of 2026-09-28; its memory `panel-20260928b-dilution-and-tolman`).
  - Frame: the band top and the long-wave speed scale together.
  - Free particle: the band top fixed, each wave slowing continuously.
  - Relabelling.
  - Speeding up.
  - Neither.
- **Imports, named at definition level.**
  - The zero-energy count of a bipartite hopping operator, at least the sublattice imbalance (Lieb's theorem), used only as a named comparator for T3's exact counts.
  - The parity-class Fourier transform on `{0, π}³` (the Walsh–Hadamard transform).
  - Degenerate first-order perturbation theory.
  - The concentration expansion of the averaged resolvent: at first order in the density of independently placed vacancies, the averaged self-energy is the density times one vacancy's T-matrix.
  - The coarea formula: the density of states of `ε` is positive for `0 < E < √3`.
  - The Schur complement.
  - Exact linear algebra over the Gaussian rationals. The exact wave number uses the phases `(3 + 4i)/5`, `(5 + 12i)/13` and `(−7 + 24i)/25`, which are Pythagorean triples.

## Prior art and what is new

- **Known.**
  - The eight species of this walk are the staggered lattice's tastes, and their parity-class structure is standard (Kogut and Susskind).
  - Zero modes forced by sublattice imbalance are standard for bipartite lattices (Lieb).
  - Vacancy superlattices in two-dimensional Dirac lattices are known to open gaps or leave flat bands.
- **Nearest in the repository.**
  - The viability campaign's note on a sharp one-site lock (PR #9363, open) prices the energy of a single locked site in the walker's sea. It does not compute a pattern's band structure.
  - Block 126 (landed) concerns records that move with vacancies, not the walker on them.
- **New here.**
  - The reduction of an ordered vacancy pattern's long waves to the taste cube with corners removed.
  - The theorem that in the taste cube, along every axis, a long wave keeps speed one or stops, with the full table of all 256 corner sets and its single exceptional class. It is exact for period-two patterns.
  - The use of all this to answer the panel's question about the coupling axis.

## Theorem T1 — the taste cube with corners removed

*Statement.*
- (a) At the eight species points the walk is `⊕_K Σ_a cos K_a q_a σ_a`. In the parity basis `|p⟩ = 8^{−1/2} Σ_K e^{−iK·p}|K⟩`, with `p ∈ {0, 1}³`, this is `h(q) = Σ_a q_a X_a ⊗ σ_a`, where `X_a` flips bit `a`. On the full cube `h(q)² = |q|²`.
- (b) A site `x` enters the species space only through its parity class `x mod 2`.
- (c) Let the vacancies' period lattice lie in `2Z³`, so all eight species fold to `Q = 0`. Let `Π` be the set of occupied parity classes. The species states that vanish on every vacancy are the states on the corners not in `Π`, and they are zero-energy states of the walk under R1.
  - If they are all of its zero-energy states at `Q = 0` (the kernel condition), then at first order in the wave number the long waves are `h_Π(q) = Σ_a q_a A_a^Π ⊗ σ_a`, where `A_a^Π` is the direction-`a` adjacency of the remaining corners.
  - The condition can fail. Extra zero modes bound to the vacancies then enter the first-order problem. In the period-4 cell with vacancies `(1,2,0), (1,3,0), (3,2,0)` (classes `100`, `110`), the kernel has 14 states, not 12. The first-order characteristic polynomial along `x` and along `z` is `λ²(λ² − 1)⁴(109λ² − 25)²/109²`, so some long waves move at speed `5/√109`.
- (d) For period 2 the band structure at every wave number `Q` is that of `h_Π(q)` with `q_a = sin(Q_a/2)`.

*Proof.*
- (a) `e^{iK_a} = cos K_a` on `{0, π}`. Multiplication by it is the shift of `p` by `e_a`.
- (b) `e^{−iK·x}` depends on `x mod 2`.
- (c) If `ψ` is in the species space and vanishes on the vacancies, then `P H P ψ = P H ψ = 0`, where `P` removes the vacancies. For two such states the matrix element of `∂_Q(PHP)` equals that of `∂_Q H`, since neither has amplitude at a cut bond's vacant end. Degenerate first-order perturbation theory then gives `h` restricted to the remaining corners.
- (d) For period 2 the hop across the cell carries `(1 − e^{−iQ_a})/(2i) = e^{−iQ_a/2} sin(Q_a/2)`. The phase `e^{iQ·x/2}` on corner `x` removes the factor.
- Runner B1–B4 and C1:
  - (a) and (b) symbolically.
  - (c) for five period-4 cells: every kernel is exactly the constrained taste space, except for two vacancies in one class, which add two exact zero modes. There the first-order velocity's characteristic polynomial equals the taste cube's times `λ²`; in the other four cells it equals the taste cube's.
  - The counterexample cell (runner B5): the kernel condition fails and a speed `5/√109` appears. A referee's random search found the condition failing in about a third of random `4³` cells with one to eight vacancies.
  - (d) at the generic wave number for all 21 classes of vacancy sets. ∎

## Theorem T2 — in the taste cube, along every axis a long wave keeps speed one or stops

*Statement.* These are statements about the taste cube `h_Π`. By T1 they describe the long waves exactly at period 2, and at first order for longer periods that meet the kernel condition.
- (a) For every `Π`, `h_Π(e_a)³ = h_Π(e_a)`, so along every axis each long-wave speed is exactly `1` or `0`.
- (b) For every `Π` outside one class of 24 sets, the characteristic polynomial of `h_Π(q)` is `λ^{2z} Π_S (λ² − q_S²)^{m_S}`, with `q_S² = Σ_{a∈S} q_a²`. A band `λ = |q_S|` has group velocity `q_S/|q_S|`, of length exactly one, in the span of the axes in `S`.
- (c) The exceptional class is the set of four remaining corners on a path that turns through all three axes, for example `011, 111, 110, 100`. Its bands obey `λ⁴ − |q|²λ² + q_a²q_b² = 0`, with `a` and `b` the axes of the path's two end edges. At `q = (1, 2, 3)` the squared group speeds are `13/20 ∓ 3√5/20`, both below one.
- (d) `h_Π = 0` exactly when the remaining corners are pairwise non-adjacent. The fewest occupied classes that achieve this is four, reached only by the two sublattices. At period 2 the frozen bands are exactly flat. For longer periods they are flat at first order only, unless a sublattice imbalance protects them (T3).

The table, up to the cube's symmetries: `xyz × m` means `m` factors of `λ² − |q|²`, `yz × m` means `m` factors of `λ² − q₂² − q₃²`, and so on; each factor carries two states.

| occupied classes | long waves |
|---|---|
| none | xyz × 8 |
| 000 | xyz × 6, frozen × 1 |
| 000, 001 | xyz × 4, z × 2 |
| 000, 011 | xyz × 4, frozen × 2 |
| 000, 111 | xyz × 4, frozen × 2 |
| 000, 001, 010 | xyz × 2, yz × 2, frozen × 1 |
| 000, 001, 110 | xyz × 2, z × 2, frozen × 1 |
| 000, 011, 101 | xyz × 2, frozen × 3 |
| 000, 001, 010, 011 (a face) | yz × 4 |
| 000, 001, 010, 100 | xyz × 2, frozen × 2 |
| 000, 001, 010, 111 | yz × 2, frozen × 2 |
| 000, 001, 110, 111 | z × 4 |
| 000, 011, 101, 110 (a sublattice) | frozen × 4 |
| 000, 001, 010, 101 | the exceptional quartic, twice |
| 000, 001, 010, 011, 100 | yz × 2, frozen × 1 |
| 000, 001, 010, 100, 111 | frozen × 3 |
| 000, 001, 010, 101, 110 | x × 2, frozen × 1 |
| six corners, leaving an edge | z × 2 |
| six corners, leaving two non-adjacent corners | frozen × 2 (two classes) |
| seven corners | frozen × 1 |

*Proof.*
- (a) `h_Π(e_a) = A_a^Π ⊗ σ_a`. Each corner has at most one `a`-neighbour, so `(A_a^Π)³ = A_a^Π`.
- (b)–(d) are an exhaustive exact computation over all 256 sets (runner D1–D4).
- For (b), `∇|q_S| = q_S/|q_S|`. ∎

## Theorem T3 — flat bands and odd periods

*Statement.*
- (a) In the period-4 cells with vacancies `{000}`, `{000, 222}`, `{000, 221}` and `{000, 011, 101, 110}`, the exact number of zero-energy states at the generic wave number is `2, 4, 0, 8`. That is twice the sublattice imbalance per cell.
- (b) With period 3, each species point carries a zero-energy doublet. One vacancy per cell leaves no zero-energy state at any of the eight species points.

*Proof.* Exact ranks over the Gaussian rationals (runner E1, E2). Per (a), a sublattice imbalance forces at least that many zero-energy states (the named import); the runner finds equality in these cells. With an odd period the sublattice sign is not periodic, and a vacancy imposes `c e^{iK·x_v} = 0` on each species' coin `c`. ∎

## Theorem T4 — R3 is a relabelling only for line vacancies

*Statement.*
- (a) Along a line with one vacancy every `n` sites, the hop going to the next record, the walk on the records in record labels is the undiluted walk. So when the vacancies fill whole lines along the hop axis, the long waves move `n/(n − 1)` grid sites per tick.
- (b) With point vacancies in three dimensions, R3's hops along different axes need not commute. With the class-`000` sites of a `4³` torus vacant, starting at `(1, 0, 0)`, hopping `y` then `x` reaches `(2, 1, 0)`, while `x` then `y` reaches `(3, 1, 0)`. So R3 is not a relabelling of the cubic walk there.

*Proof.*
- (a) The next-record map on the ring's positions is built from the positions and compared with the ring of records (runner F1, `n = 2, 3, 4, 6` on a ring of 12).
- (b) Direct (runner F2). ∎

## Theorem T5 — random missing records damp the waves

*Statement.*
- (a) Under R1, removing the site `0` changes the walk's resolvent `G(E) = (E − H)⁻¹` on the remaining sites to `G − G P₀ G₀₀⁻¹ P₀ G`. That is, `G T G` with `T = −G₀₀(E)⁻¹`, where `P₀` projects on site `0`'s coin.
- (b) `G₀₀(E) = E ḡ(E) · 1`, a multiple of the coin identity, the same at every site, with `ḡ(E) = mean_k 1/(E² − ε_k²)` and `ε_k² = Σ_a sin² k_a`.
- (c) At first order in the concentration `p` of independently placed vacancies, the averaged self-energy is `Σ(E) = −p/(E ḡ(E))`. It does not depend on `k` and is scalar in the coin. So the averaged energies solve `E + p/(E ḡ(E)) = ±ε(k)`, and depend on `k` only through `ε(k)`.
- (d) Two waves of bare energy `1`, at `k = (π/2, 0, 0)` and at `sin² k_a = 1/3`, have squared speeds `0` and `2/3`. At first order they shift alike, where the free-particle rule's law shifts them by `−λ|u|²E`, differently.
- (e) The relative shift `p/(E² ḡ(E))` is not one number: `E² ḡ` differs at `E = 1/2 + i/3` and `1 + i/3` on the `4³` torus. In the long-lattice limit `ḡ(0) = −mean_k 1/ε_k²` is finite, so the relative shift grows without bound as `E → 0`, where the frame needs a constant.
- (f) Inside the band, `Im ḡ(E + i0) = −(π/2E) ρ(E) < 0` for `0 < E < √3`, with `ρ` the density of states of `ε`. So the self-energy is complex and every wave there is damped, while a stretch rule is a unitary relabelling or rescaling and damps none.
- (g) **Regime.** The first-order expansion needs the correction small against `E`, that is `|E|²` large against `p/|ḡ(E)|`. The growth in (e) as `E → 0` marks where the expansion fails, not a physical divergence. T5 therefore says nothing about the longest waves.

*Proof.*
- (a) The inverse of a two-by-two block matrix, taken for the removed block.
- (b) `mean_k (E + H(k))/(E² − ε_k²)`, where the odd part `H(k)` averages to zero.
- (c) By translation invariance each vacancy carries the same `T`. The first-order average of `Σ_v P_v T P_v` is `p T`, diagonal in `k` (the named concentration expansion).
- (d) Direct.
- (e) The torus values are exact rationals over the Gaussian integers. The limit uses integrability of `1/ε²` at the eight species points in three dimensions.
- (f) `1/(E² − ε²) = (1/2E)(1/(E − ε) + 1/(E + ε))`, and the density of states is positive in the open band (the coarea formula; `ε` is real-analytic with nonzero gradient off a null set).
- Runner R1–R4 for (a), (b), (d) and (e) on the `4³` torus at `E = 1/2 + i/3`. ∎

## What this settles and what it does not

- **Settled** (within block 54's walk and the supplied rules).
  - Under R1, a period-two pattern of sites with no record never changes a long wave's speed along an axis. It removes waves, confines them to lines or planes, or freezes them (exactly flat), and one class of arrangements slows oblique waves.
  - At period 2 the band top `√3` survives whenever a three-dimensional band does (runner C2 and T1(d)).
  - That is neither the frame nor the free-particle class of the panel's pre-registration.
  - Longer periods can slow some waves when vacancy-bound zero modes enter (T1(c), speed `5/√109`).
  - Under R3 with line vacancies, the waves outrun the grid: the relabelling or speed-up classes.
  - A random pattern, at first order in its density and away from the longest waves, shifts waves by their bare energy alone and damps them (T5). Neither class does that.
- **For the owner's third column.**
  - The coupling-axis question ("with the sites held, must each wave slow as a free particle does?") is not answered by reading lengths as record density in the cases settled here. Period-two missing records do not act as a stretch under R1. R3 relabels or speeds up.
  - The member's lengths therefore stay a supplied field, and the question stays the owner's.
- **Not settled.**
  - Random patterns beyond first order in the density, where vacancies' scatterings interfere and the flat-band states of imbalanced regions overlap.
  - Periods whose lattice is not in `2Z³`, other than the cubic period 3.
  - Rules other than R1 and R3.
  - How the member would couple to a diluted walk.
  - Longer periods that fail the kernel condition: which waves slow, and whether that slowing follows either class.
  - The longest waves of random patterns.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
- T2 covers all 256 corner sets, and its exceptional class is named.
- T1(c) is first order, under the stated kernel condition, which a counterexample shows can fail.
- T1(d) holds at every wave number for period 2 only.
- T2 is a statement about the taste cube. Physically it is exact at period 2 only.
- T4(a) is for line vacancies.
- T5 is first order in the density, away from the longest waves.
- T3 covers the listed cells.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
- The reading of a lower density of records as vacancies and the rules R1 and R3 are supplied.
- The walk is block 54's as landed.

### N4 — Dependencies
The axioms memo and landed block 135's statement of the walk. The panel's pre-registration is recorded in the supervisor's memory and the decision record, not as a premise.

### N5 — Resolution
- per_element: executed - the taste-cube reduction of the eight species' long waves
- per_site: executed - period-4 kernels and first-order velocities for five vacancy sets; period 3 kernels at all eight species points
- per_mode: executed - all 256 corner sets: axis speeds, factorisation of every characteristic polynomial, the exceptional class
- per_block: executed - period 2 at a generic wave number for all 21 classes; flat bands at a generic wave number for period 4; one vacancy's exact scalar T-matrix on the 4^3 torus
- lattice_wide: checked and not executed - random vacancy patterns beyond first order in the concentration; periods whose lattice is not in 2Z^3 other than period 3; rules other than R1 and R3; the member's coupling to a diluted walk

### N6 — Primitive boundary
No new primitive, selection, filling rule or physical interpretation is adopted.

### N7 — Strongest objection
A stretch is uniform, and a periodic pattern is not; a random pattern might act as a uniform slowing on average. T5 answers this only in part. At first order in the density, and away from the longest waves, a random pattern shifts every wave by an amount set by its bare energy alone and damps it inside the band, which is not the free-particle law. The longest waves and higher orders are open. A second objection, from the referee, is that longer periods can slow waves. That is conceded (T1(c)).

### N8 — Earlier claims
The first and second versions' headline, "along every axis a long wave keeps speed one or stops" for any ordered pattern, is withdrawn. It holds at period 2, and at first order under the kernel condition.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "the coupling axis: with the sites held, must each wave slow as a free particle does? (panel 2026-09-28: test the owner's reading of a stretch as fewer records)"
source_of_blocker_text: decision record addendum 67 (the coupling axis reduced to one owner question)
reachability_to_target: advances
next_trace_action: "other-family referee; random patterns; the member's coupling to a diluted walk"
```

## Review record

- **Author checks (not a review PASS).** Runner exact, `TOTAL: PASS=27 FAIL=0` (third version). Mutation census 11/11, each failing in its own family only.
- **Referee (2026-09-28; Claude Sonnet 5, same vendor family as the author, a separate model and session).** Verdict: confirmed with scope corrections.
  - Independently checked: T1(d) for all 255 sets at random wave numbers, T2's table and exceptional class, T3's counts, and T5's algebra with a random-vacancy average on `8³`. The runner reran at 25/0.
  - Corrections, all applied in this third version:
    - the kernel condition fails often (the counterexample with speed `5/√109`);
    - "frozen" means first-order frozen beyond period 2;
    - R3 is not a relabelling for point vacancies in three dimensions, and the runner's F1 compared two identically built matrices;
    - T5's expansion excludes the longest waves;
    - "neither" holds for R1 only;
    - the band-top statement is for period 2.
- **Provenance.**
  - The supervisor's own derivation (Claude), prompted by a same-family panel's pre-registered test (Claude Fable 5.1 lenses: lattice and strategy).
  - Unrefereed; a referee of another family is owed.
  - Uses the Kogut–Susskind taste structure and Lieb's count as named comparators only.
