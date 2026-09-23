---
claim_id: admissibility_rule_cubic_walk_return_sum_and_sphere_static_magnetization_sufficient_bound_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "V1\u2013V3 prove the exact cubic-walk identity and scalar interval 75/100 < 3G(0) < 76/100 with the unchanged N=1000 rational certificate. Conditional on the corrected zero-field sphere static parent and its explicit mathematical imports, beta>76/100 gives M\u00b2>=1\u22123G(0)/beta>0 and the corresponding component Fourier bounds. This is a sufficient model condition, not a true transition threshold, physical kernel window or exclusion of other proof routes."
upstream_dependencies:
  - admissibility_rule_sphere_static_law_zero_field_component_fourier_bounds_bounded_theorem_note_2026-09-15
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.py
---

# Cubic-walk return sum and a sufficient sphere-static magnetization bound

**Type:** bounded_theorem

**Status:** bounded-support; conditional model; unaudited.

## Result up front

V1–V3 prove the exact cubic-walk identity and scalar interval 75/100 < 3G(0) < 76/100 with the unchanged N=1000 rational certificate. Conditional on the corrected zero-field sphere static parent and its explicit mathematical imports, beta>76/100 gives M²>=1−3G(0)/beta>0 and the corresponding component Fourier bounds. This is a sufficient model condition, not a true transition threshold, physical kernel window or exclusion of other proof routes.

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
conditional_surface_status: "V1–V3 prove the exact cubic-walk identity and scalar interval 75/100 < 3G(0) < 76/100 with the unchanged N=1000 rational certificate. Conditional on the corrected zero-field sphere static parent and its explicit mathematical imports, beta>76/100 gives M²>=1−3G(0)/beta>0 and the corresponding component Fourier bounds. This is a sufficient model condition, not a true transition threshold, physical kernel window or exclusion of other proof routes."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

V1–V3 concern the defined number, without a physical model premise. V4 uses the [corrected zero-field component Fourier note](ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md), G2–G5, with its uniform S² measure, exponential interaction, even three-dimensional torus and Gaussian-domination import (Theorem 4.6 with parameter 3beta/2). The [axioms memo](MINIMAL_AXIOMS_2026-06-29.md) and [possibility representation context](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md) select neither that measure nor the interaction.


- **The symbol and the constant.** `φ(k) = (1/3)Σ_{i=1}^3 cos k_i` on the cube `Q = [−π, π]³`; `E(k) = Σ_i 2(1 − cos k_i) = 6(1 − φ(k))`; `G(0) = (2π)^{−3}∫_Q dk/E(k)` (the corrected component Fourier parent's constant: the limit of `N^{−1}Σ_{k≠0} 1/E(k)` on tori).
- **Return probabilities.** `P_{2n}(0,0) = (2π)^{−3}∫_Q φ(k)^{2n} dk` for `n ≥ 0`; `S_N = Σ_{n=0}^N P_{2n}(0,0)`.
- **Constants of the tail.** `T_1(N) = (36/11)^{3/2}/(2π^{3/2}√N)`; `T_2(N) = 2e^{−4(N+1)/(3π²)}/(1 − e^{−4/(3π²)})`; their rational majorants `T_1(N)² ≤ (36/11)³/(108N)` (from `π ≥ 3`) and `T_2(N) ≤ (225/14)(197/225)^{N+1}` (from `π² ≤ 10` and `e^{−2/15} ≤ 197/225`).



## Prior art and what is new


The integral `(2π)^{−3}∫ dk/(1 − φ(k))` is Watson's (1939) for the simple cubic lattice, with a closed form in Gamma values found by Glasser and Zucker (1977); its value `1.5163860…` is standard. None of this is used: the value is neither cited nor needed. The retained contribution is the exact rational interval with its full tail proof.

## Theorem V1 — the constant is half the return sum

**Statement.** `3G(0) = (1/2)Σ_{n≥0} P_{2n}(0,0)`, and for every `n ≥ 0`,
```
P_{2n}(0,0) = 6^{−2n} C(2n, n) Σ_{a=0}^{n} C(n, a)² C(2(n−a), n−a).
```

**Proof.** (i) On `Q`, `|φ| ≤ 1` and `φ = 1` only at `k = 0`, so for almost every `k`, `1/(1 − φ) = (1 + φ)/(1 − φ²) = Σ_{m≥0} (1 + φ) φ^{2m}`, a series of nonnegative terms; integrating termwise (the monotone limit theorem for series of nonnegative functions, named under Imports), `(2π)^{−3}∫_Q dk/(1 − φ) = Σ_m (2π)^{−3}∫_Q (1 + φ)φ^{2m} dk`. (ii) `φ^j = 6^{−j} Σ e^{ik·(x_1 + … + x_j)}` over the `6^j` sequences of unit steps, so `(2π)^{−3}∫_Q φ^j dk = 6^{−j} · #{sequences with zero total displacement}`; for odd `j` this is `0` (an odd walk cannot close), and for `j = 2n` it is `P_{2n}(0,0)`. Hence `(2π)^{−3}∫_Q (1 + φ)φ^{2m} = P_{2m}(0,0)`, and `G(0) = (1/6)Σ_m P_{2m}(0,0)`, i.e. `3G(0) = (1/2)Σ_m P_{2m}`. (iii) A closed walk of length `2n` has `a` steps in each of `±e_1`, `b` in each of `±e_2`, `c` in each of `±e_3` with `a + b + c = n`; the number of such walks is `(2n)!/(a!a!b!b!c!c!)`, so `#{closed} = Σ_{a+b+c=n} (2n)!/(a!b!c!)² = C(2n, n) Σ_{a+b+c=n} (n!/(a!b!c!))²`. With `n!/(a!b!c!) = C(n, a) C(n−a, b)` and `Σ_b C(m, b)² = C(2m, m)`: `Σ_{a+b+c=n} (n!/(a!b!c!))² = Σ_a C(n, a)² C(2(n−a), n−a)`. ∎

Executed: the closed-walk count by enumeration of all `6^{2n}` walks for `n ≤ 3` (`1, 6, 90, 1860` closed walks), the Vandermonde form against the multinomial sum for `n ≤ 12`, and the paired geometric series symbolically (B1–B2).

## Theorem V2 — the tail bound

**Statement.** For every `n ≥ 1`, `P_{2n}(0,0) ≤ (36/11)^{3/2}/(4π^{3/2} n^{3/2}) + 2e^{−4n/(3π²)}`.

**Proof.** (i) *Two cosine inequalities.* For all real `u`, `1 − cos u ≥ u²/2 − u⁴/24`: the function `g(u) = 1 − u²/2 + u⁴/24 − cos u` has `g(0) = g'(0) = 0` and `g''(u) = cos u − 1 + u²/2 ≥ 0` (since `h(u) = cos u − 1 + u²/2` has `h(0) = 0` and `h'(u) = u − sin u`, which is `≥ 0` for `u ≥ 0` and `≤ 0` for `u ≤ 0`), so `g ≥ 0`. Hence on `|u| ≤ 1`, `1 − cos u ≥ u²(1/2 − 1/24) = 11u²/24`. For `|u| ≤ π`, `1 − cos u = 2 sin²(u/2) ≥ 2(u/π)²` because `sin v ≥ 2v/π` on `[0, π/2]` (the chord below the concave arc). (ii) *A lower bound for `1 − φ` on the cube.* If `|k|_∞ ≤ 1`, `1 − φ(k) = (1/3)Σ_i (1 − cos k_i) ≥ (11/72)|k|²`; if `|k|_∞ > 1`, some `|k_j| ∈ (1, π]` and `1 − φ(k) ≥ (1/3)(1 − cos k_j) ≥ (1/3)(2k_j²/π²) ≥ 2/(3π²)`. Call the right sides `g(k)`. (iii) *The two regions.* `φ^{2n} = |φ|^{2n} ≤ e^{−2n(1 − |φ|)}`, and `1 − |φ(k)| = min(1 − φ(k), 1 + φ(k))` with `1 + φ(k) = 1 − φ(k − π⃗)`, `π⃗ = (π, π, π)`; so `e^{−2n(1−|φ(k)|)} ≤ e^{−2n(1−φ(k))} + e^{−2n(1−φ(k−π⃗))}`, and by periodicity both terms have the same integral over `Q`: `(2π)^{−3}∫_Q φ^{2n} ≤ 2(2π)^{−3}∫_Q e^{−2n g(k)} dk`. (iv) *The Gaussian integral.* `∫_{|k|_∞≤1} e^{−(11n/36)|k|²} dk ≤ ∫_{R³} e^{−(11n/36)|k|²} dk = (36π/(11n))^{3/2}`, and `∫_{Q∖[−1,1]³} e^{−4n/(3π²)} dk ≤ (2π)³ e^{−4n/(3π²)}`. Hence `P_{2n} ≤ 2(2π)^{−3}(36π/(11n))^{3/2} + 2e^{−4n/(3π²)}`, and `2(2π)^{−3}(36π/11)^{3/2} = (36/11)^{3/2}/(4π^{3/2})`. ∎

Executed: the derivative identities of (i) and sample points; the Gaussian integral and the constant's identity; the two-region step on the symbol (C1–C3).

## Theorem V3 — the certificate: `75/100 < 3G(0) < 76/100`

**Statement.** With `N = 1000`: `3G(0) ≤ (S_N + T_1(N) + T_2(N))/2 < 76/100`, where `T_1(N)² ≤ (36/11)³/(108N)` and `T_2(N) ≤ (225/14)(197/225)^{N+1}`; and `3G(0) ≥ S_N/2 > 75/100`.

**Proof.** By V1, `3G(0) = (1/2)(S_N + Σ_{n>N} P_{2n})`, and the second half is nonnegative, so `3G(0) ≥ S_N/2`. By V2, `Σ_{n>N} P_{2n} ≤ (36/11)^{3/2}/(4π^{3/2}) Σ_{n>N} n^{−3/2} + 2Σ_{n>N} e^{−4n/(3π²)}`. Since `n^{−3/2} ≤ ∫_{n−1}^{n} t^{−3/2} dt`, `Σ_{n>N} n^{−3/2} ≤ ∫_N^∞ t^{−3/2} dt = 2/√N`, giving the first term `T_1(N) = (36/11)^{3/2}/(2π^{3/2}√N)`; with `π ≥ 3`, `T_1(N)² ≤ (36/11)³/(4 · 27 · N) = (36/11)³/(108N)`. The second term is the geometric series `T_2(N) = 2e^{−4(N+1)/(3π²)}/(1 − e^{−4/(3π²)})`; with `π² ≤ 10`, `e^{−4/(3π²)} ≤ e^{−2/15}`, and `e^{−x} ≤ 1 − x + x²/2` for `x ≥ 0` (the function `1 − x + x²/2 − e^{−x}` vanishes at `0` with derivative `−1 + x + e^{−x} ≥ 0`) gives `e^{−2/15} ≤ 1 − 2/15 + 2/225 = 197/225`; hence `T_2(N) ≤ 2(197/225)^{N+1}/(1 − 197/225) = (225/14)(197/225)^{N+1}`. The runner evaluates `S_N` exactly (V1's closed form with the common denominator `6^{2N}`), and checks the two rational inequalities `152/100 − S_N − T_2 > 0` and `(152/100 − S_N − T_2)² > (36/11)³/(108N)`, which together give `(S_N + T_1 + T_2)/2 < 76/100`; and `S_N > 150/100`. ∎

Executed: `S_{1000}` as one rational (a `1553`-digit denominator), the integer decimal `⌊10^6 S_N⌋ = 1501637`, the majorant `T_1 < 181/10⁴`, and both comparisons exactly (D1–D4).

## Corollary V4 — a sufficient zero-field magnetization condition

Under the corrected parent's supplied model and imports, let beta>76/100. V3 and parent G3 give `M²=liminf_L M_N² ≥ 1−3G(0)/beta > 0`. Parent G2 and G4 then give, for every component and every sequence of nonzero torus momenta tending to a fixed nonzero k, `(M²/3)²/(beta E(k)) ≤ liminf <|ŝ^e(k_L)|²> ≤ limsup <|ŝ^e(k_L)|²> ≤ 1/(beta E(k))`.

Proof: substitute V3 in the parent G3 inequality. The proof of parent G5 uses only positivity of M², the finite-volume bounds G2/G4 and continuity of E at nonzero k; its stated coarse sufficient condition can therefore be replaced here by beta>76/100. In detail, for any 0<eta<M², all sufficiently large volumes obey M_N²≥M²−eta. Insert this in G4, use M_N²≤1 in its denominator, take the liminf and then eta down to zero; G2 gives the upper bound. Component symmetry supplies each component. No selected transverse state or pointwise real-space law is asserted.

## No-Go Discipline Gate

Broad negative certification is withheld. The scalar lower bound remains valid, but it excludes neither alternative proofs nor physical models. Original N1 proof checks and an unattempted alternative route do not constitute five independent exact-target attacks. Original full arguments and branches remain in recovery. The prior physical kernel-window comparison is withdrawn.

## Falsifiers
- A count of closed walks for some `n ≤ 3` other than `1, 6, 90, 1860`, or a Vandermonde form differing from the multinomial sum for some `n ≤ 12` (B1); a paired-series identity that fails, or an odd integral that does not vanish at sample wavevectors (B2).
- A failure of `g'' = cos u − 1 + u²/2`, of `h' = u − sin u`, of the sample-point inequalities, of the Gaussian integral `(36π/(11n))^{3/2}`, of the constant's identity, or of the two-region step (C1–C3).
- `⌊10^6 S_{1000}⌋ ≠ 1501637`, a failed rational comparison, `S_{1000} ≤ 150/100`, or a majorant identity that fails (D1–D3).

## Boundaries and non-claims

V1–V3 prove the exact cubic-walk identity and scalar interval 75/100 < 3G(0) < 76/100 with the unchanged N=1000 rational certificate. Conditional on the corrected zero-field sphere static parent and its explicit mathematical imports, beta>76/100 gives M²>=1−3G(0)/beta>0 and the corresponding component Fourier bounds. This is a sufficient model condition, not a true transition threshold, physical kernel window or exclusion of other proof routes. No physical rule is selected and no clause is adopted.

No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

All mathematical imports are explicit; no physical selection follows from the scalar interval.

## Imports
- Re-proved at scope: V1 (termwise integration of the paired series; closed-walk counting; Vandermonde), V2 (the two cosine inequalities; the two-region split; the Gaussian integral), V3 (the integral comparison; the rational majorants).
- Named standard imports at definition level (never as authority for physics): the monotone limit theorem for integrals of series of nonnegative functions; the elementary bounds `3 < π < 22/7` (hence `π² < 10`).
- Reference only (named, not used): Watson (1939); Glasser–Zucker (1977).


The corrected parent supplies V4 and its declared Gaussian-domination import; its model hypotheses remain explicit.

## Review record

[Original recovery manifest](work_history/review_loop/pr8154/original-manifest.json) and [recovery instructions](work_history/review_loop/pr8154/README.md) preserve the complete original versions. The canonical execution address is [runner cache](../logs/runner-cache/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.txt); execution evidence must match the current source and declared inputs; historical caches are not restamped.

Original programs, outputs, complete proofs and mutation census remain byte-exact in the archive. They are historical finite evidence, not a new execution or a negative certificate.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.py --mutation certificate_target_wrong
```

Families: A authority and inputs; B the closed-walk counts, the Vandermonde form and the paired series; C the cosine inequalities, the Gaussian integral and the two-region step; D the exact partial sum, the majorants and the certificate; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. The historical mutation census assigned each of the 13 declared mutations to one family; no new mutation census is claimed. Expected final line: `TOTAL: PASS=20 FAIL=0`.
