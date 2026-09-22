---
claim_id: admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_chessboard_or_axis_stripes_on_sites_alternating_lengths_give_one_rest_energy_exclusion_cages_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk on Z³ (open PR #8570; not adopted) with supplied backgrounds on sites and on bonds, the axioms' scalar hop (block 77, open PR #8612) and the Record axiom's exclusion (blocks 78, 80; open PRs #8613, #8615): the coin representation of the proper rotations, exact symbolic algebra on the 4- and 16-dimensional blocks of the species at every wave vector, the on-site recurrence on the 2×2×2 torus, exact elimination for the projected walk on the 4³ torus; least branch separations and the free sea's energies executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_stripes_alternating_lengths_rest_energy_exclusion_cages_2026_09_22.py
---

# What can gap the walk inside the qubit: no invariant term at any reach; on sites only the chessboard or axis stripes; alternating lengths give one rest energy to all eight species; under exclusion a chessboard is a cage

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (representation-theoretic and symbolic identities for every wave vector; exact classification on the even torus; exact nullities; executed numbers labelled; nothing adopted or registered; unaudited)

This note works within block 54's walk and supplied backgrounds on sites and bonds, the axioms' scalar hop and the Record axiom's exclusion; it reports which backgrounds can separate the walk's two branches at the species points and which cannot; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 81 (PR #8626) left rest energy without an in-framework source and a panel of four lenses (2026-09-22, written by the supervisor's dossier, synthesized by the supervisor) named the remaining routes. This note settles what a rest energy can be inside the site algebra `M₂(ℂ)`: the complete map of backgrounds that separate the walk's two branches at its eight species points, and what the Record axiom's exclusion does to the one background the lane had in hand.

1. **No covariant translation-invariant term of any reach (T1).** The proper rotations permute the eight species points in orbits of sizes `1, 1, 3, 3`; at each, the stabiliser's action on the coin is irreducible (its commutant is the scalars, exactly). So every covariant translation-invariant generator, whatever its reach, is a multiple of the identity at each species point: the two branches touch there. Block 54 T1(d) (no on-site term) and block 77 (the scalar hop only offsets) are the reach-zero and reach-one cases. A rest energy needs a background that breaks one-step translation.
2. **On sites: the chessboard scalar and the axis stripes, nothing else (T2).** The on-site backgrounds `M(x) = m₀(x) + m(x)·σ` that anticommute with the walk form exactly a four-dimensional space: the chessboard scalar `c₀ε` (block 77's staggered term; block 79's record background) and the three axis stripes `c_j(−1)^{x_j}σ_j` — a content read by the coin that leans along one axis and alternates along that axis only. The three stripes anticommute pairwise: together they give one rest energy `√(c₁² + c₂² + c₃²)` to all eight species. A chessboard mixed with stripes gaps by `||c₀| − |c||`. Block 81 T4's "content order gives no gap" holds for the uniform and chessboard contents it examined; the stripe is the content order that does gap — and the six-axis static law never weighs it heaviest (`qp²` per site against `p³` and `q³`).
3. **On bonds: alternating lengths give every species the same rest energy (T3).** If the hop amplitude along axis `j` alternates, `t_j(x) = 1 + δ(−1)^{x_j}`, then `H² = β²Σ_j(sin²k_j + δ²cos²k_j)` exactly: `E² = 3β²δ²` at all eight species points, one rest energy `√3β|δ|`, opposite senses paired, no zero anywhere. With the axioms' scalar hop through the same lengths the sixteen corner energies are `±√(4a² + 3β²δ²)` (four each) and `±4a ± √(4a² + 3β²δ²)` (two each). A scalar hop with a staggered phase, `iε·2aΣcos k`, gaps as well, by an amount that varies over the zone. Lengths are the lane's own field (blocks 59–61); the alternation is not derived here.
4. **The scalar hop does not add to the rest energy (T3(c)).** With `A = 2aΣcos k` and the chessboard, `(A + H + mε)² = (A + H)² + m²` exactly: the branches are `±√(m² + (A ± |s|)²)`, their least separation is `2m`, attained on the shell `A = ∓|s|` around each species point (at `a = 1/2` the point `(π/3, π/3, π/3)` lies on it), while at the corners it is `2√(m² + A(k₀)²)`. Block 77's `√(m² + 36a²)` and `√(m² + 4a²)` are corner values; the rest energy is `m`, and quanta at rest sit on a momentum shell.
5. **Under exclusion a chessboard is a cage (T4).** If the moving record cannot enter recorded sites (one record per site), the walk restricted to the vacant sublattice of a chessboard is exactly zero — every neighbour of a vacant site is recorded — and block 79's finite `c` presupposes a record that can be entered. In general the projected walk joins the two sublattices of the vacant set only, so it has at least `2|even − odd|` exact zero modes; on the `4³` torus with one or two chessboard layers emptied the exact nullity equals that bound (`48`, `32`).
6. **Executed (control; floating point).** The alternating-length gap is not protected by the scalar hop: over a `24³` grid of the reduced zone the least `|E|` is `√3δ` at `a = 0` (`0.217, 0.433, 0.866` for `δ = 1/8, 1/4, 1/2`) but falls to `0.001`, `0.038`, `0.474` at `a = 1/10` and to zero within the grid's resolution at `a = 1/4` and `1/2` — the chessboard's `2m`, by contrast, is exact for every `a`. The free sea's energy per site falls under all three backgrounds, monotonically to unit strength; its second-order coefficient at strength `0.1` is `1.55` for the alternating lengths, `0.93` for the chessboard and `2.73` for the stripes on `16³` (`1.91, 1.17, 3.09` on `8³`; still drifting with size). Under exclusion the chessboard's `216` states on `6³` are all zero modes; three random half fillings give `16, 12, 20` zero modes against bounds `16, 4, 12`.

So: inside `M₂(ℂ)` a rest energy is a broken one-step translation, and the complete list of what breaks it usefully is short — a chessboard of something content-blind, a stripe of content read by the coin, or an alternation of the lengths. The record gas supplies none (block 81); the static law's content order supplies none (T2 remark); the only candidate built from a field the lane already carries is the alternating length, and whether anything in the framework alternates the lengths is the next question (the sea's response to that alternation is executed here).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 81 (PR #8626): 'rest energy (fork 5) remains without an in-framework source; where one could still come from is named under Boundaries'; panel of 2026-09-22 on the routes"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the complete map: translation-invariant terms never (Schur at each corner's stabiliser); on sites exactly the chessboard scalar and the axis stripes; alternating lengths give one rest energy to all eight species; the scalar hop only moves the rest momentum to a shell; under exclusion the chessboard cages; next: does the lane's own length dynamics alternate the lengths (the sea's second-order response against the lengths' field energy of blocks 60/64 — a condition on constants); the two-record exclusion problem on 4³ (bound state or anti-binding); the owner's fork on rest energy"
conditional_surface_status: "T1 by the representation argument for every covariant translation-invariant term of finite reach; T2 exact on the 2×2×2 torus and, by the recurrence M(x + e_j) = −σ_j M(x) σ_j, on every even torus; T3 and T3(c) symbolic for every wave vector; T4 for every vacant set; the executed separations and sea energies are the control's"
hypothetical_axiom_status: "the walk; supplied backgrounds on sites and bonds and their coupling clauses; the scalar hop; the exclusion reading; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (translations and the 24 proper rotations; no inversion), the Qubit axiom (`M₂(ℂ)` at each site; the coin transforms under rotations by their `SU(2)` lifts, as block 54's covariance requires), and the Record axiom (one record per site at a time, in the owner's reading). Blocks 54, 77, 78, 79, 80, 81 (open PRs #8570, #8612, #8613, #8614, #8615, #8626) supply the walk, the scalar hop, the exclusion, the chessboard background and the record-gas result. The parked larger site algebra is not touched.

- **The walk.** `H = βΣ_a σ_a S_a`, `(S_aψ)(x) = (ψ(x + e_a) − ψ(x − e_a))/2i`, symbol `s = sin k`; eight species at `k₀ ∈ {0, π}³`; `β = 1` unless written.
- **Covariance.** A rotation `r` acts as `ψ(x) → U_r ψ(r⁻¹x)` with `U_r ∈ SU(2)`, `U_r σ_a U_r⁻¹ = Σ_b r_ab σ_b`. A translation-invariant term has a symbol `M(k)`; covariance gives `M(rk) = U_r M(k) U_r⁻¹`.
- **On-site backgrounds.** `M(x) = m₀(x) + m(x)·σ`, real coefficients. Anticommutation with every `σ_jS_j` is the recurrence `M(x + e_j) = −σ_j M(x) σ_j`.
- **The doubled bases.** `ε = (−1)^{x+y+z}` sends `k` to `k + (π, π, π)`, where `s → −s`; `(−1)^{x_j}` sends `k` to `k + πe_j`, where `sin k_j → −sin k_j` and `cos k_j → −cos k_j`. Three such doublings give the `16`-dimensional block of the eight species at a reduced wave vector, with `τ^{(j)}` the matrices acting on the `j`-th pair.
- **Alternating lengths.** Hop amplitudes `t_j(x) = 1 + δ(−1)^{x_j}` in `D_jψ(x) = t_j(x)ψ(x + e_j)`; the σ-hop `(β/2i)Σ_j σ_j(D_j − D_j†)` and the scalar hop `aΣ_j(D_j + D_j†)`. On the `j`-th pair `D_j = e^{−ik_j}(τ_z + iδτ_y)`.
- **The scalar hop (block 77).** `A(k) = 2aΣ_j cos k_j` plus an offset `a₀` (dropped: it commutes with everything and shifts every energy).
- **Exclusion.** The projected walk: the walk restricted to the vacant sites, with hops between vacant sites only (`PHP` of block 80 for one moving record).
- **Control.** `16 × 16` blocks over a grid of the reduced zone; the free sea's energy `Σ_{E<0}E/N` on `L³` tori; dense projected walks on `6³`.

Fermion doubling and the pairing of opposite senses by every mass are the comparators of Nielsen and Ninomiya and of Karsten and Smit; the staggered-phase scalar hop is the staggered-Wilson form of Adams; alternating hop amplitudes are the dimerisation of Su, Schrieffer and Heeger and the bond-order masses of the Kekulé kind; zero modes counted by a sublattice imbalance are the theorem of Sutherland and of Lieb; the stripe content is a taste-vector mass in the language of Golterman and Smit. None is used as authority.

## Prior art and what is new

Block 54 T1(d) (no on-site term anticommutes with all three σ's) and block 77 (the scalar hop offsets the species 1:3:3:1 and the staggered term is a rest energy) are the reach-zero and reach-one facts; block 79 the chessboard record background; block 81 T4 the uniform and chessboard contents. In the comparators' language the classification of on-site "masses" of naive lattice fermions is Golterman and Smit's, and the zero-mode count is Sutherland's and Lieb's. New, inside the framework's vocabulary: the representation argument at each corner's stabiliser (which a first draft, following one lens, stated for the whole group at every corner — false, since the rotations permute six of the corners; the stabilisers, of order `8`, still act irreducibly); the exact four-dimensional on-site classification with the stripes as the content order that gaps; the alternating-length rest energy for all eight species with the scalar hop's corner spectrum; the shell identity that corrects the reading of block 77's mass table; and the cage under exclusion. No gravitational claim is made.

## Exact target and obligation graph

Target: the complete map of what can separate the walk's branches at the species points inside `M₂(ℂ)`. Obligations: (O1) translation-invariant terms of any reach; (O2) on-site backgrounds; (O3) bond backgrounds and the scalar hop; (O4) exclusion. T1–T4 discharge O1–O4 at the stated scope.

## Theorem T1 — no covariant translation-invariant term of any reach separates the branches at a species point

*Statement.* Let `M(k)` be the symbol of a covariant translation-invariant generator of finite reach (a trigonometric polynomial with `2 × 2` matrix coefficients). At every `k₀ ∈ {0, π}³`, `M(k₀)` is a multiple of the identity. Hence the two branches of `H + M` coincide at every species point: no such term is a rest energy.

*Proof.* The rotations act on the corners mod `2π`: `(0,0,0)` and `(π,π,π)` are fixed by all `24`; the three corners with one `π` form an orbit, as do the three with two, each with a stabiliser of order `8` (the rotations preserving the axis). For `r` in the stabiliser of `k₀`, covariance gives `M(k₀) = U_r M(k₀) U_r⁻¹`. The stabiliser's lifts have commutant exactly the scalars (family B: the linear system `XU_r = U_rX` over all lifts of each stabiliser has a one-dimensional solution space, at every corner), so `M(k₀) ∝ 1`. ∎

*Remark.* The argument uses only covariance and translation invariance; it holds for terms that do not anticommute with `H` as well (the scalar hop, whose corner values `a₀ + 2a(3 − 2|n|)` are block 77's offsets). A term that is only translation-invariant, not covariant, could still gap: the classification below is of what breaks translation.

## Theorem T2 — on-site backgrounds: the chessboard scalar and the axis stripes

*Statement.* (a) `M(x) = m₀(x) + m(x)·σ` anticommutes with every `σ_jS_j` iff `M(x + e_j) = −σ_jM(x)σ_j` for all `x, j`, i.e. `m₀(x + e_j) = −m₀(x)`, `m_j(x + e_j) = −m_j(x)`, `m_l(x + e_j) = m_l(x)` for `l ≠ j`. On any even torus the solutions are exactly `M = c₀ε + Σ_j c_j(−1)^{x_j}σ_j` (dimension `4`; family C on `2×2×2`). (b) In the `16`-dimensional block, `ε` and the three stripes anticommute with `H`; the stripes anticommute pairwise and `(Σc_j(−1)^{x_j}σ_j)² = Σc_j²`: `(H + M)² = |s|² + Σc_j²`, one rest energy `√(Σc_j²)` for all eight species. (c) `ε` commutes with each stripe, so a mixed background squares to `c₀² + |c|² + 2c₀(stripe)`, with gap `||c₀| − |c||`. (d) `εσ_z` (block 81's chessboard content), `σ_z` (uniform content) and `(−1)^{x+y}σ_z` are not solutions.

*Proof.* (a) `(σ_jS_jMψ + Mσ_jS_jψ)(x) = [σ_jM(x + e_j) + M(x)σ_j]ψ(x + e_j)/2i − [σ_jM(x − e_j) + M(x)σ_j]ψ(x − e_j)/2i`; both brackets must vanish, and `σ_j(m₀ + m·σ)σ_j = m₀ + m_jσ_j − Σ_{l≠j}m_lσ_l`. The recurrence fixes `M` on a torus from its value at one site up to the four constants; family C solves it exactly. (b)–(d) Symbolic identities in the `16`-dimensional block (family C): `(−1)^{x_j}` acts as `τ_x^{(j)}` and reverses `sin k_j`. ∎

*Remark (the static law and the stripe).* On a full lattice a stripe along `j` (contents `±e_j` alternating along `j`, equal across) weighs `qp²` per site under the six-axis static law, against `p³` for one content and `q³` for the content chessboard: `9` against `27` and `1` at `(3,1,2)`, `144` against `1728` at `(12,1,2)`, `3` against `1` and `27` at `(1,3,2)`. The stripe is never the heaviest pattern; the static law's ordered states (block 17 and its sublattice mirror) are the two that do not gap (block 81 T4).

## Theorem T3 — bond backgrounds: alternating lengths, a staggered phase, and what the scalar hop does

*Statement.* (a) With `t_j(x) = 1 + δ(−1)^{x_j}` on every axis, the σ-hop's block is `H = βΣ_j σ_j(−sin k_j τ_z^{(j)} + δ cos k_j τ_y^{(j)})` and `H² = β²Σ_j(sin²k_j + δ²cos²k_j)` exactly; at every species point `E² = 3β²δ²`; for `δ ≠ 0` there is no zero. With the scalar hop through the same lengths, `2aΣ_j(cos k_j τ_z^{(j)} + δ sin k_j τ_y^{(j)})`, the sixteen corner energies are `±√(4a² + 3β²δ²)` (four each) and `±4a ± √(4a² + 3β²δ²)` (two each). (b) `M = iε·2aΣ_j cos k_j` is Hermitian, anticommutes with `H`, and `(H + M)² = |s|² + 4a²(Σ_j cos k_j)²`: no zero (the corners have `Σcos = ±3, ±1`), a gap `6a` at two corners and `2a` at six. (c) With `A = 2aΣcos k` and the chessboard `mε`: `(A + H + mε)² = (A + H)² + m²`; the branches are `±√(m² + (A ± |s|)²)`; their least separation is `2m`, on the shell `A = ∓|s|`; at the corners it is `2√(m² + A(k₀)²)`.

*Proof.* (a) On the `j`-th pair `D_j = e^{−ik_j}(τ_z + iδτ_y)`, so `(β/2i)(D_j − D_j†) = β(−sin k_j τ_z + δ cos k_j τ_y)` and `a(D_j + D_j†) = 2a(cos k_j τ_z + δ sin k_j τ_y)`. The `h_j` act on different pairs and commute; the `σ_j` anticommute; cross terms cancel and `h_j² = β²(sin²k_j + δ²cos²k_j)`. The corner spectrum with the scalar hop is an exact eigenvalue computation of the `16 × 16` matrix at `k = 0` (family D). (b) `ε` anticommutes with the one-step hop `C = 2aΣcos k` and commutes with `H`'s symbol up to `s → −s`; `(εC)† = Cε = −εC`. (c) `A` commutes with `H` and anticommutes with `ε`, `H` anticommutes with `ε`; the cross terms vanish. The shell at `a = 1/2`: `2a·3cos t = √3|sin t|` at `t = π/3`. ∎

*Remark.* (c) corrects the reading of block 77's mass table: `√(m² + 36a²)` and `√(m² + 4a²)` are the branch separations at the corners; the rest energy — half the least separation — is `m` for every species, and the least separation sits on a shell of radius about `6a` (one corner) or `2a` (the others) around each species point. For (a) with `a ≠ 0` the least separation is not closed-form; it is executed (control W1).

## Theorem T4 — under exclusion a chessboard is a cage

*Statement.* (a) With records on one sublattice of a torus, the walk restricted to the vacant sites is exactly zero: the vacant sublattice's `2N/2` states are all zero modes; no rest energy, no motion. (b) For any vacant set with `n_e` even and `n_o` odd sites, the projected walk has at least `2|n_e − n_o|` exact zero modes. (c) On the `4³` torus with the chessboard's records removed from one layer (`n_e = 8, n_o = 32`) or two (`16, 32`), the exact nullity equals the bound: `48` and `32`.

*Proof.* (a) Every neighbour of a vacant site is recorded. (b) The walk joins each site to its six neighbours, which lie on the other sublattice; in the split even/odd the projected matrix is `[[0, B], [B†, 0]]` with `B` of size `2n_e × 2n_o`, whose rank is at most `2 min(n_e, n_o)`. (c) Exact elimination over the Gaussian rationals (family E). ∎

*Consequence for block 79.* Block 79's `m = c/2` needs a moving record that can enter a recorded site at a finite cost `c`; under the Record axiom's exclusion the cost is not finite, and the chessboard blocks every hop. Its odd-layer zero modes are a statement about the penetrable model; the exclusion count is (b).

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block82_gap_map.py`, output in `.out.txt`; disjoint machinery: floating-point `16 × 16` blocks over the reduced zone, zone sums, dense diagonalisation).

*W1 — alternating lengths with the scalar hop.* `β = 1`; both hops through the same lengths; the spectrum is symmetric about zero (`ε` anticommutes with both hops), so the least `|E|` over the zone is half the gap. Grid `24³`.

| `δ` | `a = 0` | `a = 1/10` | `a = 1/4` | `a = 1/2` |
|---|---|---|---|---|
| `1/8` | `0.2165` (`= √3δ`) | `0.0009` | `0.0032` | `0.0010` |
| `1/4` | `0.4330` (`= √3δ`) | `0.0383` | `0.0007` | `0.0005` |
| `1/2` | `0.8660` (`= √3δ`) | `0.4737` | `0.0000` | `0.0002` |

At `a = 0` the gap is T3(a)'s exactly; with the scalar hop through the same lengths the bands `±4a ∓ √(4a² + 3δ²)` disperse through zero once `a` is comparable with `δ`. The chessboard's least separation `2m` is exact at every `a` (T3(c)): the two rest energies differ in kind.

*W2 — the free sea's energy against the background.* `E_sea/N = Σ_{E<0}E/N` on `L³` tori (`a = 0`), three backgrounds of the same strength `g`: alternating lengths (`δ = g`), the chessboard scalar (`m = g`), the axis stripes (`c_j = g`).

| `g` | lengths (`8³` / `16³`) | chessboard | stripes |
|---|---|---|---|
| `0` | `−1.1902 / −1.1936` | same | same |
| `0.1` | `−1.1997 / −1.2014` | `−1.1960 / −1.1983` | `−1.2056 / −1.2073` |
| `0.4` | `−1.3034 / −1.3035` | `−1.2626 / −1.2632` | `−1.3886 / −1.3888` |
| `1` | `−1.7321 / −1.7321` | `−1.5686 / −1.5687` | `−2.1163 / −2.1163` |

Second-order coefficient `−2(E(0.1) − E(0))/0.01`: lengths `1.91 / 1.55`, chessboard `1.17 / 0.93`, stripes `3.09 / 2.73` (`8³ / 16³`; the drift with size is the slowly settling response of the corners, where the density of states vanishes as `E²`); all three decrease monotonically to `g = 1` (at `δ = 1` every state has `|E| = √3`, the lattice falls apart into `2×2×2` cubes). The sea lowers its energy under any of the three; whether one is selected is a comparison with the cost of the background, which the sea does not set (the lengths' field energy of blocks 60/64 with its constant; the gas's weights for the chessboard, block 81; the static law's for the stripe, T2 remark).

*W3 — exclusion on `6³`.* Chessboard: `108` vacant sites, `216` zero modes, bound `216` (the cage). Three random half fillings: `16, 12, 20` zero modes against bounds `16, 4, 12` — the bound holds and is attained in one case.


## No-Go Discipline Gate

The note's negative sentences: no covariant translation-invariant term of any reach separates the branches at a species point; no on-site background outside the four-dimensional space anticommutes with the walk; the scalar hop does not add to the rest energy; under exclusion a chessboard gives no propagating quantum.

### N1 — Routes by which the sentences could fail or mislead
1. *Covariance.* T1 needs the coin to transform by the `SU(2)` lifts (block 54's covariance). A term covariant under a smaller group (e.g. only translations) is outside T1 and inside T2/T3's "backgrounds".
2. *Anticommutation is sufficient, not necessary.* T2 classifies backgrounds that anticommute with `H`; a site background that gaps without anticommuting is not excluded by T2 (T1 excludes it only when translation-invariant and covariant). The executed least separations bear on this for the cases tried only.
3. *Bond backgrounds are not classified.* T3 exhibits two; a finite linear solve of the bond recurrence is the next exact step.
4. *The value of `δ`.* Nothing here fixes it; the control's sea response is a second-order coefficient, not a selection.
5. *Exclusion reading.* T4 assumes the moving record is excluded from recorded sites; block 79's clause assumes it is not. Which the axioms mean is the owner's reading; both are stated.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Even tori; `β = 1`; `a₀` dropped; the `16`-dimensional block assumes the same `δ` on every axis (the one-axis case is contained in T2's stripe algebra by the same identities).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Lattice axiom's rotations and the coin's transformation; the Record axiom | yes (premise) |
| blocks 54, 77 (open PRs #8570, #8612) | the walk; the scalar hop and the staggered term | yes (restated; block 77's table re-read) |
| blocks 78, 79, 80, 81 (open PRs #8613, #8614, #8615, #8626) | exclusion; the chessboard background; the record-gas result | yes (placed) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no invariant term at any reach; on sites only the chessboard and the stripes; alternating lengths gap all eight; the scalar hop only moves the rest momentum to a shell; exclusion cages" | executed: every rotation's lift; the recurrence at every site of `2×2×2` | executed: every vacant pair of `4³` | executed: symbolic blocks at every wave vector; control grids and sea sums | executed: exact nullities against the bound | T1 by proof; T2 by the recurrence; T3 by identity; T4 by the bipartite argument

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Alternating lengths are just another supplied background; nothing is gained over block 79." Reply: two things are gained — the background is a field the lane already carries (lengths, blocks 59–61) rather than a record pattern the gas refuses to make, and exclusion does not cage it (no site is forbidden). What is not gained is a reason for `δ ≠ 0`; the note says so. Second objection: "T1 is the doubling theorem restated." Reply: it is the in-framework proof at the level the axioms give (covariance + translation), and it is what makes the map complete rather than a list.

### N8 — Cross-cycle echo
Block 54: no on-site term. Block 77: the scalar hop offsets; the staggered term is a rest energy. Block 79: a chessboard of records is one. Block 81: the gas never makes it; content order of two kinds does not gap. Here: the whole map, the third content order that does gap, the bond route, and the cage.

## Falsifiers

- A covariant translation-invariant term of finite reach whose symbol at some corner is not a multiple of the identity.
- An on-site background anticommuting with the walk outside the span of `ε` and the three axis stripes.
- A wave vector at which `H² ≠ β²Σ(sin²k_j + δ²cos²k_j)` for the alternating lengths, or at which `(A + H + mε)² ≠ (A + H)² + m²`.
- A vacant set whose projected walk has fewer than `2|n_e − n_o|` zero modes.

## Boundaries and non-claims

Bond backgrounds are exhibited, not classified; `δ` is not fixed; the least separations with `a ≠ 0` and the sea's responses are executed; the exclusion reading and block 79's penetrable reading are both stated and neither adopted. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice, Qubit and Record axioms. Blocks 54, 77, 78, 79, 80, 81 (open PRs): restated or placed.
- Named standard imports at definition level: Schur's lemma; `SU(2)` lifts of rotations; block matrices and exact symbolic algebra; rank–nullity for bipartite block matrices; dense diagonalisation and zone sums for the control.

## Review record
Supervisor-run block, the thirtieth of the source-link direction; the seventh after the fork probe; the first after the rest-energy panel (four lenses on the supervisor's dossier; synthesis by the supervisor). Lens pass, in writing, by the supervisor: a foundations lens — the walker's coupling to records is a supplied clause, and exclusion is the axioms'; both readings are kept apart; a rigour lens — one panel lens stated that every corner is fixed by all `24` rotations; the runner's first check of that statement failed, because the rotations permute six of the corners; the theorem was restated with each corner's stabiliser (order `8` or `24`), whose lifts still have a scalar commutant, and the proof is the stabiliser's. The dimerised-hop algebra, the stripe classification and the cage were each re-derived by the supervisor before the block was built (scratch computations), and the claim that `(H + mε)` with the scalar hop has rest energy `√(m² + 36a²)` was tested and replaced by the exact shell identity. Mutation census: nine mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_stripes_alternating_lengths_rest_energy_exclusion_cages_2026_09_22.py
```

Expected: `TOTAL: PASS=18 FAIL=0`.
