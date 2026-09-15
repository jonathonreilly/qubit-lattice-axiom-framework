---
claim_id: admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_third_dimension_load_bearing_for_the_green_function_channel_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the static law of the exponential zonal rule on the pure-state sphere under the unsoldered reading, restricted to a coordinate plane or a coordinate line of the lattice — the torus law proportional to prod_{<xy>} exp(beta s_x . s_y) on (Z/2LZ)^d with the uniform surface measure — with the transform s^(k) = N^{-1/2} sum_x e^{ikx} s_x, the Laplacian symbol E(k) = sum_i 2(1 - cos k_i) and the long-range-order parameter M_N^2 = N^{-2} <|sum_x s_x|^2>: (H1) the zero-field lower bound <|s^1(k)|^2> >= (2 M_N^2/3)^2/[(beta E)^{1/2} + (beta E + 4 M_N^2/(3N))^{1/2}]^2 >= (M_N^2/3)^2/(beta E(k) + 4/(3N)) holds for every k != 0 in every dimension d <= 3, the dimension entering only through the bond count (proved; the generator, integration-by-parts, second-derivative, simplification and bond identities executed symbolically); (H2) on the plane sum_{k != 0} |k|^{-2} >= (N/pi^2) H_{L-1}, E(k) <= |k|^2 and 4/(3N) <= |k|^2/(3 pi^2), and on the line (L >= 2) the 2 floor(sqrt L) smallest wavevectors have beta E(k) + 4/(3N) <= (beta pi^2 + 2/3)/L (proved; the shell counts, the dyadic bound H_{2^m} >= 1 + m/2 and the identities executed exactly); (H3) hence, by the sum rule sum_k <|s^1(k)|^2> = N/3, the long-range-order parameter obeys M_N^4 <= (3 pi^2 beta + 1)/H_{L-1} on the plane (L >= 2) and M_N^4 <= (6 pi^2 beta + 4)/sqrt(L) on the line (L >= 2), so it tends to zero as L grows for every beta > 0: the unsoldered static law has no long-range order on any coordinate plane or line (proved; executed); (H4) consequently the transverse Green-function channel of the ordered law (block 19's sandwich, PR #8153, referenced as an evidence address for the three-dimensional half) exists on Z^3 above its threshold and on no plane or line, while the soldered six-axis static law orders on the plane (block 17, PR #8151): the third dimension of the Lattice axiom is load-bearing for the gravity node's kernel under the unsoldered static reading, and the continuous menu is what forbids order on planes (a placement corollary conditional on the referenced open blocks for their halves). Three standard mathematical imports named at definition level; no coupling, reading, rule or dimension is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.py
---

# The unsoldered sphere static law has no long-range order on any coordinate plane or line: the zero-field lower bound is dimension-free, the plane's lattice sum grows without bound, and the Green-function channel needs the third dimension

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Block 19 (PR #8153) found where the gravity lane's kernel can live inside the
axioms' readings: in the transverse channel of the ordered unsoldered static
law on `Z³`, where the record field picks a direction and its components
across that direction fluctuate like the inverse lattice Laplacian. The
Lattice axiom names `Z³`. Is the third dimension doing work there, or would a
plane do? This note answers: a plane never orders under that reading, at any
coupling strength, and neither does a line; so the channel of block 19 does
not exist on any plane or line, and the third dimension is load-bearing for
the kernel.

The proof is short because block 19's lower bound is already dimension-free.
That bound, a classical Bogoliubov inequality run at zero field against the
long-range-order parameter itself, reads `⟨|ŝ¹(k)|²⟩ ≥ (M_N²/3)²/(βE(k) +
4/(3N))` for every nonzero wavevector; nothing in its derivation knows the
dimension except the count of bonds per direction, which is `N` in every
dimension (H1). Summing it over wavevectors and comparing with the sum rule
`Σ_k ⟨|ŝ¹(k)|²⟩ = N/3` gives `(M_N²/3)² · N^{−1}Σ_{k≠0} 1/(βE(k) + 4/(3N)) ≤
1/3`. On the plane the lattice sum grows like the harmonic sum `H_{L−1}` of
the side (H2), so `M_N⁴ ≤ (3π²β + 1)/H_{L−1}` (H3): the long-range-order
parameter tends to zero as the plane grows, whatever `β`. On the line the
sum grows like `√L` and the same happens faster. In three dimensions the
sum stays bounded and the inequality says nothing, which is consistent with
block 19's order for `β > 3√3π/8`.

The contrast with block 17 is the point: the soldered six-axis static law,
with its discrete menu, *does* order on the plane (PR #8151). Whether a plane
can order is decided by the menu: a continuous possibility symmetry (block
18's unsoldered reading) forbids it, a discrete one does not. And the
channel that carries the Green function is exactly the one a continuous
symmetry supplies. So under the reading that produces the gravity node's
kernel, the kernel needs `Z³` (H4).

Exactly: H1 in `d ≤ 3`; `Σ_{k≠0}|k|^{−2} ≥ (N/π²)H_{L−1}` on the plane (H2);
`M_N⁴ ≤ (3π²β + 1)/H_{L−1}` on the plane and `M_N⁴ ≤ (6π²β + 4)/√L` on the
line (H3); the placement (H4). Executed with exact arithmetic: 20 checks,
13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the derivation campaign's gravity node (#8093): 'the covariant scalar record statistic whose two-point function on the formation law is the lattice Green function'; block 19 (PR #8153) locates it in the transverse channel of the ordered unsoldered static law on Z^3; the Lattice axiom's third dimension"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the dimension placement is settled for the unsoldered static reading: no long-range order on any coordinate plane or line at any beta > 0, so block 19's channel needs Z^3; the discrete six-axis law orders on the plane (block 17), so the menu decides. Open: the decay of the plane's correlations (not claimed); the kernel's normalization; the Born overlap. Consumers: #8093's assembly (the gravity node's dimension dependence); the campaign's queue"
conditional_surface_status: "H1 proved for d <= 3 and every beta > 0 on tori of even side; H2-H3 proved on every plane and line torus with explicit bounds; H4 a placement corollary conditional on blocks 19 and 17 (open PRs) for their halves; the algebraic skeleton executed exactly (shell counts to L = 12, the dyadic bound to m = 12, the identities symbolically, Parseval on the 4x4 torus); conditional on the sphere as the possibility domain, the unsoldered reading and the exponential overlap as supplied conditions; three standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "Each site has a domain of local possibilities.", "No possibility is privileged.", "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", and "Records form.". The landed possibility-covariance note (`docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md`, section "Empty-neighbourhood sphere laws") supplies the pure-state sphere `S²` as the possibility domain and the unsoldered reading (internal rotations act on values independently of the cube group on sites). Block 01 (on `main`) supplies the static reading: on a finite window the law is the normalized product of the rule's bond weights over the window's bonds. Both are proposed and unaudited; blocks 17 and 19 (PRs #8151, #8153, open) are referenced under Prior art as evidence addresses for the halves of H4 that are not re-proved here.

Declared objects.
- **Dimension and torus.** `d ∈ {1, 2, 3}`; the torus `T_L^{(d)} = (Z/2LZ)^d` with `N = (2L)^d` sites and `dN` nearest-neighbour bonds (`N` per direction). The plane and the line are the coordinate sublattices `Z²` and `Z¹` of the Lattice axiom's `Z³`; their static laws are the laws of the same rule on windows contained in the plane or the line, with no records outside the window (the convention of blocks 12 and 17).
- **The law.** Records `s_x ∈ S²`; the overlap `e^{β s·s'}` with `β > 0` supplied; the torus law `μ_L ∝ Π_{⟨xy⟩} e^{β s_x·s_y} Π_x dσ(s_x)` with `dσ` the uniform surface measure. `μ_L` is invariant under every simultaneous rotation of all records (the overlap and `dσ` are).
- **Transforms.** `ŝ(k) = N^{−1/2} Σ_x e^{ik·x} s_x` for `k = (π/L)n`, `n ∈ {−L+1, …, L}^d`; `E(k) = Σ_{i=1}^d 2(1 − cos k_i)`; `m̂ = N^{−1}Σ_x s_x³`; `M_N² = N^{−2}⟨|Σ_x s_x|²⟩`; `u(k) = ⟨|ŝ¹(k)|²⟩`. By the rotation invariance, `⟨m̂²⟩ = M_N²/3` and `⟨(s_x¹)²⟩ = 1/3`.
- **The generator.** `L_x = (e₂ × s_x)·∇_x`, the rotation about `e₂` acting on site `x`: `L_x s_x³ = −s_x¹`, `L_x s_x¹ = s_x³`, `L_x s_x² = 0`; `L = Σ_z c_z L_z` with `c_z = e^{−ik·z}` and `L̄ = Σ_z c̄_z L_z`.
- **Harmonic sums.** `H_n = Σ_{j=1}^n 1/j`; `H_0 = 0`.

## Prior art and what is new

The classical no-order theorem for continuous symmetries in two dimensions is due to Mermin and Wagner (1966) for quantum spins and Mermin (1967) for classical ones, with Hohenberg (1967) for superfluids; algebraic decay in two dimensions is McBryan–Spencer (1977); Fröhlich–Pfister (1981) and Dobrushin–Shlosman (1975) give the infinite-volume forms. None is used; H1–H3 are re-proved at scope for the record law. On `main`, three notes treat the theorem for *quantum Hamiltonians* on `Z¹`/`Z²` sublattices: the axiom-first Coleman–Mermin–Wagner packet (2026-04-29, the lattice sum's growth), the 2D-sublattice no-SSB note (2026-05-02, with the Ward-normalized order/charge pair as a hypothesis) and the textbook-import note (2026-05-18), which states that its order-parameter lower bound needs an unsupplied Ward-normalization lemma and that it does not treat the classical theorem. What is new here: (i) for the record law the order-parameter lower bound is the exact generator identity `L ŝ¹(k) = N^{1/2} m̂` (no Ward lemma is needed), so the no-order statement closes on planes and lines with explicit finite-volume bounds; (ii) H1 is block 19's inequality with the dimension made explicit, re-proved here so the note stands alone; (iii) the placement: block 19's Green-function channel needs the third dimension, and the discrete law of block 17 shows the menu, not the lattice, decides whether a plane orders.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| H1 | the zero-field lower bound for `k ≠ 0` in `d ≤ 3`, the dimension only in the bond count | generator, integration by parts, the second derivative, the quadratic | D |
| H2 | the plane's lattice sum `≥ (N/π²)H_{L−1}`; `H_{L−1} ≥ 1 + m/2` for `L ≥ 2^m + 1`; `E(k) ≤ |k|²`; the small-wavevector term; the line's block | shells in the sup norm; dyadic blocks; the half-angle identity | B, C |
| H3 | `M_N⁴ ≤ (3π²β + 1)/H_{L−1}` on the plane; `M_N⁴ ≤ (6π²β + 4)/√L` on the line | the sum rule with H1 and H2 | C, D |
| H4 | the placement: the channel needs `Z³`; the menu decides whether a plane orders | H3 with blocks 19 and 17 | — |

## Theorem H1 — the zero-field lower bound in every dimension

**Statement.** For `d ∈ {1, 2, 3}`, `β > 0`, `L ≥ 1` and every `k ≠ 0`,
```
u(k) ≥ (2M_N²/3)² / [(βE(k))^{1/2} + (βE(k) + 4M_N²/(3N))^{1/2}]² ≥ (M_N²/3)² / (βE(k) + 4/(3N)).
```

**Proof.** (i) *Integration by parts.* The flow of `L_x` is a rotation of `s_x` about `e₂`, which preserves `dσ`; hence `∫_{S²} L_x G dσ = 0` for every smooth `G`, and for the density `w = Π_{⟨xy⟩} e^{β s_x·s_y}` of `μ_L` against `Π dσ`: `⟨L G⟩ = −⟨G · L log w⟩`. (ii) *The quadratic-form inequality.* For `F = ŝ¹(k) m̂`: `|⟨LF⟩|² = |⟨F · L log w⟩|² ≤ ⟨|F|²⟩ ⟨|L log w|²⟩`, and `⟨|F|²⟩ ≤ u(k)` because `|m̂| ≤ 1`. (iii) *The right factor.* Applying (i) with `G = L̄ log w`: `⟨|L log w|²⟩ = ⟨(L̄ log w)(L log w)⟩ = −⟨L L̄ log w⟩`. On a single bond, `L_x(s_x·s_y) = e₂·(s_x × s_y) = −L_y(s_x·s_y)` and
```
−(c_x L_x + c_y L_y)(c̄_x L_x + c̄_y L_y)(s_x·s_y) = |c_x − c_y|² (s_x¹ s_y¹ + s_x³ s_y³),
```
so `−L L̄ log w = β Σ_{⟨xy⟩} |c_x − c_y|² (s_x¹s_y¹ + s_x³s_y³)`. For a bond in direction `i`, `|c_x − c_y|² = |1 − e^{−ik_i}|² = 2(1 − cos k_i)`, and `|s_x¹s_y¹ + s_x³s_y³| ≤ 1`. There are `N` bonds in each of the `d` directions, so `⟨|L log w|²⟩ ≤ βN Σ_{i=1}^d 2(1 − cos k_i) = βN E(k)`. This is the only place the dimension enters. (iv) *The left factor.* `L ŝ¹(k) = N^{−1/2} Σ_x e^{ik·x} c_x s_x³ = N^{1/2} m̂` and `L m̂ = −N^{−1} Σ_y c_y s_y¹ = −N^{−1/2} \overline{ŝ¹(k)}`, so `LF = N^{1/2} m̂² − N^{−1/2} |ŝ¹(k)|²` and `⟨LF⟩ = N^{1/2} M_N²/3 − N^{−1/2} u(k)`. (v) *The quadratic.* If `⟨LF⟩ < 0` then `u > N M_N²/3`, which exceeds the claimed bound. Otherwise (ii)–(iv) give `M_N²/3 − u/N ≤ (βE u)^{1/2}`; with `v = u^{1/2}` this is `v²/N + (βE)^{1/2} v − M_N²/3 ≥ 0`, so `v` is at least the positive root, `v ≥ (2M_N²/3)/[(βE)^{1/2} + (βE + 4M_N²/(3N))^{1/2}]`, which is the first inequality. (vi) *Simplification.* With `a = βE` and `b = (a + 4M_N²/(3N))^{1/2} ≥ a^{1/2}`: `4b² − (a^{1/2} + b)² = (b − a^{1/2})(3b + a^{1/2}) ≥ 0`, so the first bound is at least `(M_N²/3)²/(a + 4M_N²/(3N))`, and `M_N² ≤ 1` gives the second inequality. ∎

*Remarks.* The infrared upper bound `u(k) ≤ 1/(βE(k))` of block 19 (reflection positivity through bond planes and Gaussian domination) is dimension-free in the same way; it is not needed below. The identities of (iii), (iv) and (vi) are executed symbolically (D1–D4).

## Theorem H2 — the lattice sums

**Statement.** (a) *Plane.* For `d = 2`, `L ≥ 2`: `Σ_{k≠0} |k|^{−2} ≥ (N/π²) H_{L−1}`. (b) *Dyadic growth.* `H_{2^m} ≥ 1 + m/2` for every `m ≥ 0`; hence `H_{L−1} ≥ 1 + m/2` whenever `L ≥ 2^m + 1`. (c) *The symbol.* `E(k) ≤ |k|²` for every `k`. (d) *The small term on the plane.* `4/(3N) = |k_min|²/(3π²) ≤ |k|²/(3π²)` for every `k ≠ 0`, where `|k_min| = π/L` and `N = 4L²`. (e) *Line.* For `d = 1`, `N = 2L`, `L ≥ 2`, `m = ⌊√L⌋` and every `n` with `1 ≤ |n| ≤ m`: `βE(k) + 4/(3N) ≤ (βπ² + 2/3)/L` at `k = πn/L`; there are exactly `2m ≥ √L` such wavevectors in the range.

**Proof.** (a) The wavevectors are `k = (π/L)n` with `n ∈ {−L+1, …, L}²`. Sort `n ≠ 0` by `j = |n|_∞`. For `1 ≤ j ≤ L−1` the whole shell `{|n|_∞ = j}` lies in the range and has `8j` points; every point of shell `j` has `|n|² ≤ 2j²`. Hence `Σ_{n≠0} |n|^{−2} ≥ Σ_{j=1}^{L−1} 8j/(2j²) = 4H_{L−1}` (the truncated shell `j = L`, with `4L − 1` points, is dropped), and `Σ_{k≠0}|k|^{−2} = (L²/π²) Σ_{n≠0}|n|^{−2} ≥ (4L²/π²) H_{L−1} = (N/π²) H_{L−1}`. (b) The block `2^{i−1} < j ≤ 2^i` has `2^{i−1}` terms, each at least `2^{−i}`, so it contributes at least `1/2`; summing `i = 1, …, m` and adding the term `j = 1` gives `H_{2^m} ≥ 1 + m/2`; `H_n` is increasing in `n`. (c) `2(1 − cos u) = 4 sin²(u/2) ≤ 4(u/2)² = u²` by `|sin t| ≤ |t|`; sum over `i`. (d) `4/(3N) = 1/(3L²) = (π/L)²/(3π²)`, and `|k| ≥ π/L` for `k ≠ 0`. (e) `4/(3N) = 2/(3L)`; for `n² ≤ L`, `βE(k) ≤ β|k|² = βπ²n²/L² ≤ βπ²/L`; so the sum is at most `(βπ² + 2/3)/L`. Both `n` and `−n` lie in the range `{−L+1, …, L}` for `1 ≤ n ≤ m` because `m ≤ L − 1` (at `L = 2`, `m = 1`; for `L ≥ 3`, `m ≤ √L ≤ L − 1`), so the count is exactly `2m`; at `L = 1` only `n = 1` is in the range, which is why `L ≥ 2` is required. Finally `4m² ≥ L` because `m + 1 > √L` gives `L < (m+1)² ≤ 4m²` for `m ≥ 1`. ∎

The shell counts `8j` and `4L − 1`, the norm bound and the resulting inequality are executed exactly for `L = 2, …, 12` (B1); the dyadic bound for `m ≤ 12` (B2); `4⌊√L⌋² ≥ L` and the count `2⌊√L⌋` of wavevectors in the block for `2 ≤ L ≤ 400`, and the line's per-term inequality symbolically (B3); the half-angle identity and the small-term identities symbolically (C1–C2).

## Theorem H3 — no long-range order on planes and lines

**Statement.** For every `β > 0`: on the plane torus `(Z/2LZ)²` with `L ≥ 2`,
```
M_N⁴ ≤ (3π²β + 1)/H_{L−1}, hence M_N⁴ ≤ (3π²β + 1)/(1 + m/2) for L ≥ 2^m + 1;
```
on the line torus `Z/2LZ` with `L ≥ 2`, `M_N⁴ ≤ (6π²β + 4)/√L` (at `L = 1` the right side exceeds `1 ≥ M_N⁴`). In both cases `M_N² → 0` as `L → ∞`: the unsoldered static law with the exponential overlap has no long-range order on any coordinate plane or line.

**Proof.** *The sum rule.* The transform is unitary, `Σ_k |ŝ¹(k)|² = Σ_x (s_x¹)²`, so `Σ_k u(k) = N⟨(s_0¹)²⟩ = N/3` by rotation invariance; dropping the term `k = 0` (which is `N M_N²/3 ≥ 0`), `Σ_{k≠0} u(k) ≤ N/3`. *Plane.* By H1 and H2(c)–(d), for `k ≠ 0`: `u(k) ≥ (M_N²/3)²/((β + 1/(3π²))|k|²)`. Summing and using H2(a): `(M_N²/3)² (β + 1/(3π²))^{−1} (N/π²) H_{L−1} ≤ N/3`, i.e. `(M_N²/3)² ≤ π²(β + 1/(3π²))/(3H_{L−1})`, and multiplying by `9`: `M_N⁴ ≤ (3π²β + 1)/H_{L−1}`. The dyadic form is H2(b). *Line.* By H1 and H2(e), each of the `2m` wavevectors with `1 ≤ |n| ≤ m` has `u(k) ≥ (M_N²/3)² L/(βπ² + 2/3)`, so `(M_N²/3)² · 2m L/(βπ² + 2/3) ≤ N/3 = 2L/3`, i.e. `M_N⁴ ≤ 3(βπ² + 2/3)/m ≤ 6(βπ² + 2/3)/√L = (6π²β + 4)/√L`. ∎

Parseval with symbolic site values on the `4×4` torus and the sphere average `1/3` are executed (D5); the final algebra of both cases symbolically (C3).

## Corollary H4 — the placement: the Green-function channel needs the third dimension

**Statement (conditional on blocks 19 and 17 for their halves).** Under the unsoldered static reading with the exponential overlap, block 19's transverse channel — `(M²/3)²/(βE(k)) ≤ lim inf u(k) ≤ 1/(βE(k))` with `M² > 0` — exists on `Z³` for `β > 3√3π/8` (block 19, G3–G5) and on no coordinate plane or line at any `β > 0` (H3: the lower constant `M²` is zero in the limit, so the sandwich degenerates and no long-range order carries it). The soldered six-axis static law orders on the plane for `p ≥ 216·max(q, r)` (block 17, T5–T6). Hence: (i) the third dimension of the Lattice axiom is load-bearing for the gravity node's kernel under the reading that supplies it; (ii) whether a plane orders is decided by the menu (continuous forbids, discrete allows), not by the lattice.

**Proof.** (i) is H3 with block 19's G5; (ii) is H3 with block 17's T5–T6 and block 18's classification of the menus (continuous under the unsoldered reading, cube orbits under the soldered one). Nothing beyond H3 is proved here; the referenced halves are open PRs and are cited as evidence addresses, not as authority. ∎

*Not claimed.* How the plane's correlations decay (the infrared upper bound `u(k) ≤ 1/(βE(k))` still holds there and the sum rule then says nothing further); any statement for the Born overlap; the kernel's normalization on `Z³`.

## No-Go Discipline Gate

The negative sentence is H3: no long-range order for the unsoldered static law on any coordinate plane or line, at any `β > 0`. Its escapes are named, not closed: a discrete menu (block 17 orders on the plane), the formation reading (block 12 treats it separately), and `d = 3` (block 19 orders).

### N1 — Routes by which H3 could fail
1. *The lower bound H1 fails in `d < 3`* — closed: the derivation uses only the bond count per direction (D1–D4 executed; the counts on the `4×4` and `8` tori executed).
2. *The sum rule's constant* — closed: Parseval and the sphere average executed (D5); dropping `k = 0` only weakens the inequality in the safe direction.
3. *The lattice sum on the plane stays bounded* — closed: the shell bound gives `H_{L−1}`, which grows without bound (B1–B2).
4. *The small term `4/(3N)` dominates* — closed on the plane by H2(d) (it is `|k_min|²/(3π²)`) and on the line by the block of the `2⌊√L⌋` smallest wavevectors (B3).
5. *A discrete menu, the formation reading, or the third dimension* — escapes, named above; none contradicts H3, which is stated for the continuous menu on planes and lines.

### N2 — Wall-independence audit
No no-go wall of the repository is used; the argument is self-contained given the premises.

### N3 — Hidden-wall scan
No hidden dependence: the only inputs are the axioms' sentences, the parent note's sphere law and reading, block 01's static reading, and the supplied overlap.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the five sentences under Premises | yes (premise) |
| the possibility-covariance note (`main`) | the sphere domain and the unsoldered reading | yes (premise, proposed) |
| block 01 (`main`) | the static reading | yes (premise, proposed) |
| block 19 (PR #8153) | the three-dimensional half of H4; H1 re-proved here | H4 only (evidence address) |
| block 17 (PR #8151) | the discrete law's order on the plane, for H4(ii) | H4 only (evidence address) |
| block 18 (PR #8152) | the classification of the menus, for H4(ii) | H4 only (evidence address) |
| main's three quantum no-order notes | context only | no |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no long-range order on any coordinate plane or line" | executed: the generator identities; the single-bond second derivative; the root and its simplification; the bond identity | executed: Parseval with symbolic site values on the `4×4` torus; the sphere average of a component's square | executed: the shell counts `8j`, `4L−1` and the norm bound on every shell for `L ≤ 12`; the line's small-wavevector block | executed: the dyadic blocks of the harmonic sum to `m = 12`; the bond counts on the `4×4` and `8` tori | proved for every `β > 0` on every plane and line torus (H3); H1 for `d ≤ 3`; the decay rate not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling, overlap or dimension; none is a wall.

### N7 — Steelman
Hostile reviewer: "This is the 1966 theorem for the classical three-component model; the framework adds nothing, and the bound `M_N² ≲ (log L)^{−1/2}` is far from the truth." Reply: the framework question is whether the reading that supplies the gravity node's kernel needs the third dimension of the Lattice axiom, and the answer required the classical no-order statement for *this* record law with no open lemma; main's quantum versions leave the order-parameter lower bound to an unsupplied normalization lemma, which the classical generator identity replaces. Conceded: the rate is not sharp and is not claimed; the decay of the plane's correlations is not treated.

### N8 — Cross-cycle echo
Main's axiom-first no-order packets (2026-04-29, 2026-05-02, 2026-05-18) are the quantum-Hamiltonian counterparts, conditional on a Ward lemma; block 12's eroder statement that the formation law never orders on the plane is the same dimension dependence in the other reading, for a different reason (majority erosion); block 17's discrete order on the plane is the counterexample that fixes the cause here as the continuous menu.

## Falsifiers
- A side `L ≤ 12` at which a sup-norm shell of `{−L+1, …, L}²` has a count other than `8j` (`j < L`) or `4L − 1` (`j = L`), a point with `|n|² > 2j²`, or `Σ_{n≠0}|n|^{−2} < 4H_{L−1}` (B1); an `m ≤ 12` with `H_{2^m} < 1 + m/2` (B2); an `L ≤ 400` with `4⌊√L⌋² < L`, a count of wavevectors in the line's block other than `2⌊√L⌋` for some `2 ≤ L ≤ 400`, or a failure of the line's per-term inequality (B3).
- A failure of `2(1 − cos u) = 4 sin²(u/2)` or a sample point with `2(1 − cos u) > u²` (C1); `4/(3N) ≠ (π/L)²/(3π²)` at `N = 4L²` or `≠ 2/(3L)` at `N = 2L` (C2); a final-algebra identity that fails (C3).
- A generator identity, the single-bond second-derivative identity, the integration-by-parts identity for a polynomial, the root identity or the simplification identity that fails (D1–D3); the bond identity `|1 − e^{−iθ}|² = 2(1 − cos θ)` or a bond count other than `N` per direction on the `4×4` or `8` torus (D4); a Parseval residue or a sphere average other than `1/3` (D5).

## Boundaries and non-claims
This note proves, for the unsoldered static law with the exponential overlap on a coordinate plane or line of the lattice, that the long-range-order parameter tends to zero as the torus grows at every `β > 0`, with explicit bounds; it does not state the rate at which correlations decay on the plane, does not treat the Born overlap, does not re-prove the three-dimensional half of the placement (block 19's open PR), does not select a reading, rule, coupling or dimension as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- The possibility-covariance note and block 01 (both on `main`): the readings and the object; proposed, unaudited. PRs #8151, #8152 and #8153 (open) referenced as evidence addresses for H4 only.
- Re-proved at scope: H1 (integration by parts, the quadratic-form inequality, the second derivative, the quadratic and its simplification), H2 (shells, dyadic blocks, the half-angle identity, the small terms), H3 (the sum rule and the assembly).
- Named standard imports at definition level (never as authority for physics): the unitarity of the discrete torus transform; the integration-by-parts identity for the divergence-free rotation field on the sphere; the inequality `|sin t| ≤ |t|`.
- Reference only (named, not used): Mermin–Wagner (1966); Mermin (1967); Hohenberg (1967); McBryan–Spencer (1977); Fröhlich–Pfister (1981); Dobrushin–Shlosman (1975); main's three quantum no-order notes of 2026-04-29, 2026-05-02 and 2026-05-18.

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane at each conclusion; no subagents). The control (`specs/supervisor_control_block20_planes_lines.py`) checked the shell counts, the dyadic bound, the identities, the simplification chain, the sphere average, Parseval and the line's block before the contract, and corrected the contract's first draft, which had counted the last shell as if the wavevector range were `{−L, …, L}²` (the range is `{−L+1, …, L}²`; the last shell is truncated to `4L − 1` points and is dropped, so the bound is `4H_{L−1}`, not `4H_L`) and had applied the plane's small-term comparison to the line (where `4/(3N) = 2/(3L)` is not below `|k|²/(3π²)`; the line uses the block of the `2⌊√L⌋` smallest wavevectors instead); the lens pass is in `GOAL_block20.md`; the primary seat wrote H1–H4 and the runner; the refuting pass (`CHECKER_block20_findings.md`) checked H1 on the exactly solvable two-site instance, the plane's and the line's sums by direct floating-point evaluation of `N^{−1}Σ_{k≠0} 1/(βE(k) + 4/(3N))` against the proved lower bounds up to `L = 64`, the sphere average in a second parametrization and Parseval on a random real field; it caught that the line's count `2⌊√L⌋` fails at `L = 1` (where `−n` is outside the range `{−L+1, …, L}`), so H2(e) and the line half of H3 are stated for `L ≥ 2`, with the `L = 1` bound trivial. Facts settled while executing: the sum rule's constant is `N/3`, not `N` (rotation invariance), which improves the constant by `3`; the plane's bound only bites for `H_{L−1} > 3π²β + 1`, i.e. astronomically large sides at moderate `β`, which is the known weakness of this route and is stated as such.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.py --mutation claim_order_on_planes_injected
```

Families: A authority and inputs; B the plane's shells, the dyadic bound and the line's block; C the half-angle identity, the small terms and the final algebra; D the generator identities, integration by parts, the second derivative, the root and its simplification, the bond identity and counts, Parseval and the sphere average; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
