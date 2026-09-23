---
claim_id: admissibility_rule_sphere_static_law_finite_torus_magnetization_bounds_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For a supplied uniform-sphere exponential nearest-neighbour static model in independent dimensions d=1,2,3, on even tori with L>=2: H1 is a finite-volume Fourier lower bound in terms of M_N; H2 supplies explicit lattice sums; H3 gives M_N^4 <= (3 pi^2 beta+1)/H_(L-1) in dimension two and M_N^4 <= (6 pi^2 beta+4)/sqrt(L) in dimension one. These bounds imply vanishing of this torus magnetization-square sequence. No universal state, kernel, gravity or dimension-selection conclusion is retained."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.py
---

# Sphere Static Law Finite Torus Magnetization Bounds

**Type:** bounded_theorem

**Status:** bounded-support; conditional supplied model; unaudited.

## Result up front

For a supplied uniform-sphere exponential nearest-neighbour static model in independent dimensions d=1,2,3, on even tori with L>=2: H1 is a finite-volume Fourier lower bound in terms of M_N; H2 supplies explicit lattice sums; H3 gives M_N^4 <= (3 pi^2 beta+1)/H_(L-1) in dimension two and M_N^4 <= (6 pi^2 beta+4)/sqrt(L) in dimension one. These bounds imply vanishing of this torus magnetization-square sequence. No universal state, kernel, gravity or dimension-selection conclusion is retained.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Quantitative mathematical bounds for explicitly supplied sphere static models; no physical channel classification."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Original independent affected-source confirmation and bounded finite evidence capture; retained-grade audit remains separate."
conditional_surface_status: "For a supplied uniform-sphere exponential nearest-neighbour static model in independent dimensions d=1,2,3, on even tori with L>=2: H1 is a finite-volume Fourier lower bound in terms of M_N; H2 supplies explicit lattice sums; H3 gives M_N^4 <= (3 pi^2 beta+1)/H_(L-1) in dimension two and M_N^4 <= (6 pi^2 beta+4)/sqrt(L) in dimension one. These bounds imply vanishing of this torus magnetization-square sequence. No universal state, kernel, gravity or dimension-selection conclusion is retained."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The linked repository context is [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md); [POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md). The possibility parent supplies conditional representation vocabulary; it does not select this probability law. We explicitly supply the uniform surface measure on S², beta>0, the exponential pair weight and the static specification. These are mathematical model premises, not consequences selecting physics from the axioms. The independent d-dimensional nearest-neighbour model omits all couplings outside that dimension; a two-dimensional model is not the marginal of a plane in an interacting three-dimensional model. All torus claims below use L>=2 (side at least four), so neighbours are distinct.

Declared objects.
- **Dimension and torus.** `d ∈ {1, 2, 3}`; the torus `T_L^{(d)} = (Z/2LZ)^d` with `N = (2L)^d` sites and `dN` nearest-neighbour bonds (`N` per direction). Here dimensions one and two mean independent nearest-neighbour models, with no out-of-dimension couplings; all tori have L ≥ 2.
- **The law.** Records `s_x ∈ S²`; the overlap `e^{β s·s'}` with `β > 0` supplied; the torus law `μ_L ∝ Π_{⟨xy⟩} e^{β s_x·s_y} Π_x dσ(s_x)` with `dσ` the uniform surface measure. `μ_L` is invariant under every simultaneous rotation of all records (the overlap and `dσ` are).
- **Transforms.** `ŝ(k) = N^{−1/2} Σ_x e^{ik·x} s_x` for `k = (π/L)n`, `n ∈ {−L+1, …, L}^d`; `E(k) = Σ_{i=1}^d 2(1 − cos k_i)`; `m̂ = N^{−1}Σ_x s_x³`; `M_N² = N^{−2}⟨|Σ_x s_x|²⟩`; `u(k) = ⟨|ŝ¹(k)|²⟩`. By the rotation invariance, `⟨m̂²⟩ = M_N²/3` and `⟨(s_x¹)²⟩ = 1/3`.
- **The generator.** `L_x = (e₂ × s_x)·∇_x`, the rotation about `e₂` acting on site `x`: `L_x s_x³ = −s_x¹`, `L_x s_x¹ = s_x³`, `L_x s_x² = 0`; `L = Σ_z c_z L_z` with `c_z = e^{−ik·z}` and `L̄ = Σ_z c̄_z L_z`.
- **Harmonic sums.** `H_n = Σ_{j=1}^n 1/j`; `H_0 = 0`.



## Prior art and what is new


The classical no-order theorem for continuous symmetries in two dimensions is due to Mermin and Wagner (1966) for quantum spins and Mermin (1967) for classical ones, with Hohenberg (1967) for superfluids; algebraic decay in two dimensions is McBryan–Spencer (1977); Fröhlich–Pfister (1981) and Dobrushin–Shlosman (1975) give the infinite-volume forms. None is used; H1–H3 are re-proved at scope for the record law.  The contribution retained here is the explicit mathematical bounds for the supplied model. No comparison with physical channels is used.

## Theorem H1 — the zero-field lower bound in every dimension

**Statement.** For `d ∈ {1, 2, 3}`, `β > 0`, `L ≥ 2` and every `k ≠ 0`,
```
u(k) ≥ (2M_N²/3)² / [(βE(k))^{1/2} + (βE(k) + 4M_N²/(3N))^{1/2}]² ≥ (M_N²/3)² / (βE(k) + 4/(3N)).
```

**Proof.** (i) *Integration by parts.* The flow of `L_x` is a rotation of `s_x` about `e₂`, which preserves `dσ`; hence `∫_{S²} L_x G dσ = 0` for every smooth `G`, and for the density `w = Π_{⟨xy⟩} e^{β s_x·s_y}` of `μ_L` against `Π dσ`: `⟨L G⟩ = −⟨G · L log w⟩`. (ii) *The quadratic-form inequality.* For `F = ŝ¹(k) m̂`: `|⟨LF⟩|² = |⟨F · L log w⟩|² ≤ ⟨|F|²⟩ ⟨|L log w|²⟩`, and `⟨|F|²⟩ ≤ u(k)` because `|m̂| ≤ 1`. (iii) *The right factor.* Applying (i) with `G = L̄ log w`: `⟨|L log w|²⟩ = ⟨(L̄ log w)(L log w)⟩ = −⟨L L̄ log w⟩`. On a single bond, `L_x(s_x·s_y) = e₂·(s_x × s_y) = −L_y(s_x·s_y)` and
```
−(c_x L_x + c_y L_y)(c̄_x L_x + c̄_y L_y)(s_x·s_y) = |c_x − c_y|² (s_x¹ s_y¹ + s_x³ s_y³),
```
so `−L L̄ log w = β Σ_{⟨xy⟩} |c_x − c_y|² (s_x¹s_y¹ + s_x³s_y³)`. For a bond in direction `i`, `|c_x − c_y|² = |1 − e^{−ik_i}|² = 2(1 − cos k_i)`, and `|s_x¹s_y¹ + s_x³s_y³| ≤ 1`. There are `N` bonds in each of the `d` directions, so `⟨|L log w|²⟩ ≤ βN Σ_{i=1}^d 2(1 − cos k_i) = βN E(k)`. This is the only place the dimension enters. (iv) *The left factor.* `L ŝ¹(k) = N^{−1/2} Σ_x e^{ik·x} c_x s_x³ = N^{1/2} m̂` and `L m̂ = −N^{−1} Σ_y c_y s_y¹ = −N^{−1/2} \overline{ŝ¹(k)}`, so `LF = N^{1/2} m̂² − N^{−1/2} |ŝ¹(k)|²` and `⟨LF⟩ = N^{1/2} M_N²/3 − N^{−1/2} u(k)`. (v) *The quadratic.* If `⟨LF⟩ < 0` then `u > N M_N²/3`, which exceeds the claimed bound. Otherwise (ii)–(iv) give `M_N²/3 − u/N ≤ (βE u)^{1/2}`; with `v = u^{1/2}` this is `v²/N + (βE)^{1/2} v − M_N²/3 ≥ 0`, so `v` is at least the positive root, `v ≥ (2M_N²/3)/[(βE)^{1/2} + (βE + 4M_N²/(3N))^{1/2}]`, which is the first inequality. (vi) *Simplification.* With `a = βE` and `b = (a + 4M_N²/(3N))^{1/2} ≥ a^{1/2}`: `4b² − (a^{1/2} + b)² = (b − a^{1/2})(3b + a^{1/2}) ≥ 0`, so the first bound is at least `(M_N²/3)²/(a + 4M_N²/(3N))`, and `M_N² ≤ 1` gives the second inequality. ∎

*Finite verification.* The identities of (iii), (iv) and (vi) are executed symbolically (D1–D4).

## Theorem H2 — the lattice sums

**Statement.** (a) *Plane.* For `d = 2`, `L ≥ 2`: `Σ_{k≠0} |k|^{−2} ≥ (N/π²) H_{L−1}`. (b) *Dyadic growth.* `H_{2^m} ≥ 1 + m/2` for every `m ≥ 0`; hence `H_{L−1} ≥ 1 + m/2` whenever `L ≥ 2^m + 1`. (c) *The symbol.* `E(k) ≤ |k|²` for every `k`. (d) *The small term on the plane.* `4/(3N) = |k_min|²/(3π²) ≤ |k|²/(3π²)` for every `k ≠ 0`, where `|k_min| = π/L` and `N = 4L²`. (e) *Line.* For `d = 1`, `N = 2L`, `L ≥ 2`, `m = ⌊√L⌋` and every `n` with `1 ≤ |n| ≤ m`: `βE(k) + 4/(3N) ≤ (βπ² + 2/3)/L` at `k = πn/L`; there are exactly `2m ≥ √L` such wavevectors in the range.

**Proof.** (a) The wavevectors are `k = (π/L)n` with `n ∈ {−L+1, …, L}²`. Sort `n ≠ 0` by `j = |n|_∞`. For `1 ≤ j ≤ L−1` the whole shell `{|n|_∞ = j}` lies in the range and has `8j` points; every point of shell `j` has `|n|² ≤ 2j²`. Hence `Σ_{n≠0} |n|^{−2} ≥ Σ_{j=1}^{L−1} 8j/(2j²) = 4H_{L−1}` (the truncated shell `j = L`, with `4L − 1` points, is dropped), and `Σ_{k≠0}|k|^{−2} = (L²/π²) Σ_{n≠0}|n|^{−2} ≥ (4L²/π²) H_{L−1} = (N/π²) H_{L−1}`. (b) The block `2^{i−1} < j ≤ 2^i` has `2^{i−1}` terms, each at least `2^{−i}`, so it contributes at least `1/2`; summing `i = 1, …, m` and adding the term `j = 1` gives `H_{2^m} ≥ 1 + m/2`; `H_n` is increasing in `n`. (c) `2(1 − cos u) = 4 sin²(u/2) ≤ 4(u/2)² = u²` by `|sin t| ≤ |t|`; sum over `i`. (d) `4/(3N) = 1/(3L²) = (π/L)²/(3π²)`, and `|k| ≥ π/L` for `k ≠ 0`. (e) `4/(3N) = 2/(3L)`; for `n² ≤ L`, `βE(k) ≤ β|k|² = βπ²n²/L² ≤ βπ²/L`; so the sum is at most `(βπ² + 2/3)/L`. Both `n` and `−n` lie in the range `{−L+1, …, L}` for `1 ≤ n ≤ m` because `m ≤ L − 1` (at `L = 2`, `m = 1`; for `L ≥ 3`, `m ≤ √L ≤ L − 1`), so the count is exactly `2m`; at `L = 1` only `n = 1` is in the range, which is why `L ≥ 2` is required. Finally `4m² ≥ L` because `m + 1 > √L` gives `L < (m+1)² ≤ 4m²` for `m ≥ 1`. ∎

The shell counts `8j` and `4L − 1`, the norm bound and the resulting inequality are executed exactly for `L = 2, …, 12` (B1); the dyadic bound for `m ≤ 12` (B2); `4⌊√L⌋² ≥ L` and the count `2⌊√L⌋` of wavevectors in the block for `2 ≤ L ≤ 400`, and the line's per-term inequality symbolically (B3); the half-angle identity and the small-term identities symbolically (C1–C2).

## Theorem H3 — bounds on the torus magnetization-square sequence

**Statement.** For every `β > 0`: on the plane torus `(Z/2LZ)²` with `L ≥ 2`,
```
M_N⁴ ≤ (3π²β + 1)/H_{L−1}, hence M_N⁴ ≤ (3π²β + 1)/(1 + m/2) for L ≥ 2^m + 1;
```
on the line torus `Z/2LZ` with `L ≥ 2`, `M_N⁴ ≤ (6π²β + 4)/√L` (at `L = 1` the right side exceeds `1 ≥ M_N⁴`). In both cases `M_N² → 0` as `L → ∞`: this particular one- or two-dimensional torus magnetization-square sequence tends to zero.

**Proof.** *The sum rule.* The transform is unitary, `Σ_k |ŝ¹(k)|² = Σ_x (s_x¹)²`, so `Σ_k u(k) = N⟨(s_0¹)²⟩ = N/3` by rotation invariance; dropping the term `k = 0` (which is `N M_N²/3 ≥ 0`), `Σ_{k≠0} u(k) ≤ N/3`. *Plane.* By H1 and H2(c)–(d), for `k ≠ 0`: `u(k) ≥ (M_N²/3)²/((β + 1/(3π²))|k|²)`. Summing and using H2(a): `(M_N²/3)² (β + 1/(3π²))^{−1} (N/π²) H_{L−1} ≤ N/3`, i.e. `(M_N²/3)² ≤ π²(β + 1/(3π²))/(3H_{L−1})`, and multiplying by `9`: `M_N⁴ ≤ (3π²β + 1)/H_{L−1}`. The dyadic form is H2(b). *Line.* By H1 and H2(e), each of the `2m` wavevectors with `1 ≤ |n| ≤ m` has `u(k) ≥ (M_N²/3)² L/(βπ² + 2/3)`, so `(M_N²/3)² · 2m L/(βπ² + 2/3) ≤ N/3 = 2L/3`, i.e. `M_N⁴ ≤ 3(βπ² + 2/3)/m ≤ 6(βπ² + 2/3)/√L = (6π²β + 4)/√L`. ∎

Parseval with symbolic site values on the `4×4` torus and the sphere average `1/3` are executed (D5); the final algebra of both cases symbolically (C3).

## No-Go Discipline Gate

Broad negative certification is withheld. The original five-route tables listed proof obligations and changes of scope rather than five independent attacks on the exact exclusion. They do not establish a negative certificate. Full original arguments remain available in the archive and original branches are retained. H4 is withdrawn: vanishing M_N² degenerates this particular lower bound; it does not exclude every possible kernel or establish a statement about every infinite-volume state.

## Falsifiers
- A side `L ≤ 12` at which a sup-norm shell of `{−L+1, …, L}²` has a count other than `8j` (`j < L`) or `4L − 1` (`j = L`), a point with `|n|² > 2j²`, or `Σ_{n≠0}|n|^{−2} < 4H_{L−1}` (B1); an `m ≤ 12` with `H_{2^m} < 1 + m/2` (B2); an `L ≤ 400` with `4⌊√L⌋² < L`, a count of wavevectors in the line's block other than `2⌊√L⌋` for some `2 ≤ L ≤ 400`, or a failure of the line's per-term inequality (B3).
- A failure of `2(1 − cos u) = 4 sin²(u/2)` or a sample point with `2(1 − cos u) > u²` (C1); `4/(3N) ≠ (π/L)²/(3π²)` at `N = 4L²` or `≠ 2/(3L)` at `N = 2L` (C2); a final-algebra identity that fails (C3).
- A generator identity, the single-bond second-derivative identity, the integration-by-parts identity for a polynomial, the root identity or the simplification identity that fails (D1–D3); the bond identity `|1 − e^{−iθ}|² = 2(1 − cos θ)` or a bond count other than `N` per direction on the `4×4` or `8` torus (D4); a Parseval residue or a sphere average other than `1/3` (D5).

## Boundaries and non-claims

For a supplied uniform-sphere exponential nearest-neighbour static model in independent dimensions d=1,2,3, on even tori with L>=2: H1 is a finite-volume Fourier lower bound in terms of M_N; H2 supplies explicit lattice sums; H3 gives M_N^4 <= (3 pi^2 beta+1)/H_(L-1) in dimension two and M_N^4 <= (6 pi^2 beta+4)/sqrt(L) in dimension one. These bounds imply vanishing of this torus magnetization-square sequence. No universal state, kernel, gravity or dimension-selection conclusion is retained. This note does not select a physical reading, coupling, rule or dimension and adopts no clause.

No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The standard mathematical imports are stated explicitly; they supply mathematical tools, not physical selection.

## Imports
- Re-proved at scope: H1 (integration by parts, the quadratic-form inequality, the second derivative, the quadratic and its simplification), H2 (shells, dyadic blocks, the half-angle identity, the small terms), H3 (the sum rule and the assembly).
- Named standard imports at definition level (never as authority for physics): the unitarity of the discrete torus transform; the integration-by-parts identity for the divergence-free rotation field on the sphere; the inequality `|sin t| ≤ |t|`.
- Reference only (named, not used): Mermin–Wagner (1966); Mermin (1967); Hohenberg (1967); McBryan–Spencer (1977); Fröhlich–Pfister (1981); Dobrushin–Shlosman (1975); main's three quantum no-order notes of 2026-04-29, 2026-05-02 and 2026-05-18.


## Review record

[Original recovery manifest](work_history/review_loop/pr8154/original-manifest.json) and [recovery instructions](work_history/review_loop/pr8154/README.md) preserve the complete original versions. The canonical execution address is [runner cache](../logs/runner-cache/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.txt); execution evidence must match the current source and declared inputs; historical caches are not restamped.

The original branch, full note, runner, cache, historical programs and outputs are preserved byte-exact in the recovery archive. Historical controls are evidence of their recorded finite domains, not a new execution or a proof of an infinite-lattice statement. The canonical primary retains its original twenty finite checks and thirteen mutation definitions; the historical mutation census is not a new review.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.py --mutation claim_order_on_planes_injected
```

Families: A authority and inputs; B the plane's shells, the dyadic bound and the line's block; C the half-angle identity, the small terms and the final algebra; D the generator identities, integration by parts, the second derivative, the root and its simplification, the bond identity and counts, Parseval and the sphere average; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. The historical mutation census assigned each of the 13 declared mutations to one family; no new mutation census is claimed. Expected final line: `TOTAL: PASS=20 FAIL=0`.
