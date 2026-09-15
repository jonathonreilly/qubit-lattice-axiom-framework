---
claim_id: admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_of_the_cubic_walk_three_g_zero_below_seventy_six_hundredths_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the constant 3 G(0) = 3 (2 pi)^{-3} int_{[-pi,pi]^3} dk/E(k), E(k) = sum_i 2(1 - cos k_i), which is the ordering threshold of the unsoldered sphere static law's infrared route (block 19, PR #8153: long-range order and the Green-function channel for beta > 3 G(0)): (V1) 3 G(0) = (1/2) sum_{n >= 0} P_{2n}(0,0), with P_{2n}(0,0) = 6^{-2n} C(2n, n) sum_a C(n, a)^2 C(2(n-a), n-a) the return probability of the simple random walk on Z^3 (proved; the closed-walk count executed by enumeration for n <= 3 and the Vandermonde form to n = 12); (V2) for every n >= 1, P_{2n}(0,0) <= (36/11)^{3/2}/(4 pi^{3/2} n^{3/2}) + 2 e^{-4n/(3 pi^2)}, from 1 - cos u >= 11 u^2/24 on |u| <= 1, 1 - cos u >= 2 u^2/pi^2 on [-pi, pi], |phi|^{2n} <= e^{-2n(1 - |phi|)} and the two-region split (proved; the inequalities and the Gaussian integral executed symbolically); (V3) with N = 1000, the exact partial sum S_N = sum_{n <= N} P_{2n} and the tail bound give 3 G(0) < 76/100 as an exact rational comparison (pi >= 3, e^{-2/15} <= 197/225), and S_N/2 > 75/100 gives 3 G(0) > 75/100 (proved; executed exactly); (V4) hence block 19's ordering threshold is beta > 76/100 in place of 3 sqrt(3) pi/8 (about 2.04), the route's constant lies in (75/100, 76/100), and with block 21 (PR #8155) the kernel's coupling window on Z^3 is [sqrt(3)/6, 76/100] (a placement corollary conditional on the referenced open blocks). Two standard mathematical imports named at definition level; no coupling, reading or rule is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.py
---

# Block 19's ordering threshold sharpened to `β > 76/100`: the lattice Green function at the origin is half the return sum of the cubic walk, its partial sums are exact, and an elementary tail bound pins `3G(0)` between `75/100` and `76/100`

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings for the placement; unaudited)

## Result up front

Block 19 (PR #8153) proves that the unsoldered sphere static law orders, and
carries the Green-function channel, once `β` exceeds `3G(0)`, where `G(0)`
is the lattice Green function at the origin; it bounded `G(0)` by an
elementary inequality and got `β > 3√3π/8 ≈ 2.04`. Block 21 (PR #8155)
proves there is no channel below `√3/6 ≈ 0.289`. That leaves a band a
factor seven wide. This note shrinks it from the top: `3G(0) < 76/100`.

The mechanism is elementary. `1/E(k)` is `(1/6)/(1 − φ(k))` with `φ` the
characteristic function of the simple random walk on `Z³`, so `G(0)` is the
sum of the walk's return probabilities divided by six, and `3G(0)` is half
that sum. Each return probability is an exact rational — a count of closed
walks over `6^{2n}` — and the count has a closed form through a Vandermonde
identity. Summing the first thousand terms exactly gives `S_{1000}`, a single
rational with a `1553`-digit denominator; an explicit tail bound, from the
quartic Taylor bound on `1 − cos u` near zero and a Gaussian integral,
adds less than `0.019`; and the comparison `(S_N + tail)/2 < 76/100` is a
rational inequality checked exactly. The partial sum alone gives the other
side, `3G(0) > 75/100`. So the route's constant is pinned within about a
percent, and nothing short of a different route to order can push the
threshold below `75/100`.

Exactly: `3G(0) = (1/2)Σ P_{2n}(0,0)` (V1); the tail bound (V2);
`75/100 < 3G(0) < 76/100` (V3); the window `[√3/6, 76/100]` (V4).
Executed with exact arithmetic: 20 checks, 13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the derivation campaign's gravity node (#8093): blocks 19-21 (PRs #8153-#8155) locate its kernel in the ordered unsoldered static law on Z^3 with a coupling window [sqrt(3)/6, 3 sqrt(3) pi/8]; the width of that window"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the strong-coupling constant of block 19's route is pinned: 75/100 < 3G(0) < 76/100 by exact return counts and an elementary tail bound; the ordering threshold is beta > 76/100; the kernel's window is [sqrt(3)/6, 76/100]. Open: the band itself (a different route to order below 3G(0); the sharper weak-coupling coefficient); the normalization. Consumers: #8093's assembly (the gravity node's coupling window); the campaign's queue"
conditional_surface_status: "V1-V3 proved and executed exactly (the return-sum identity; the tail bound; the certificate at N = 1000); V4 a placement corollary conditional on blocks 19 and 21 (open PRs) for their halves; conditional on the sphere as the possibility domain, the unsoldered and static readings and the exponential overlap only through the placement; two standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "Each site has a domain of local possibilities.", "No possibility is privileged.", "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", and "Records form.". The landed possibility-covariance note (`docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md`, section "Empty-neighbourhood sphere laws") supplies the pure-state sphere and the unsoldered reading, which enter only through the placement V4. Blocks 19 and 21 (PRs #8153, #8155, open) are referenced under Prior art as evidence addresses for V4; V1–V3 are statements about a number and depend on nothing proposed.

Declared objects.
- **The symbol and the constant.** `φ(k) = (1/3)Σ_{i=1}^3 cos k_i` on the cube `Q = [−π, π]³`; `E(k) = Σ_i 2(1 − cos k_i) = 6(1 − φ(k))`; `G(0) = (2π)^{−3}∫_Q dk/E(k)` (block 19's constant: the limit of `N^{−1}Σ_{k≠0} 1/E(k)` on tori).
- **Return probabilities.** `P_{2n}(0,0) = (2π)^{−3}∫_Q φ(k)^{2n} dk` for `n ≥ 0`; `S_N = Σ_{n=0}^N P_{2n}(0,0)`.
- **Constants of the tail.** `T_1(N) = (36/11)^{3/2}/(2π^{3/2}√N)`; `T_2(N) = 2e^{−4(N+1)/(3π²)}/(1 − e^{−4/(3π²)})`; their rational majorants `T_1(N)² ≤ (36/11)³/(108N)` (from `π ≥ 3`) and `T_2(N) ≤ (225/14)(197/225)^{N+1}` (from `π² ≤ 10` and `e^{−2/15} ≤ 197/225`).

## Prior art and what is new

The integral `(2π)^{−3}∫ dk/(1 − φ(k))` is Watson's (1939) for the simple cubic lattice, with a closed form in Gamma values found by Glasser and Zucker (1977); its value `1.5163860…` is standard. None of this is used: the value is neither cited nor needed. Block 19 bounded `G(0)` by `√3π/8` from `1 − cos u ≥ 2u²/π²` alone; block 13 used the return probabilities of the same walk for a different purpose (the heat kernel's coincidence probabilities). What is new here: (i) the threshold constant of block 19's route rewritten as half the return sum and computed exactly to a thousand terms; (ii) an elementary tail bound with the quartic Taylor inequality near zero, which is what makes a thousand terms enough; (iii) the exact two-sided pinning `75/100 < 3G(0) < 76/100`, so the route's threshold is `β > 76/100` and cannot be below `75/100`; (iv) the placement: the kernel's window on `Z³` is `[√3/6, 76/100]`.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| V1 | `3G(0) = (1/2)Σ P_{2n}`; the closed form of `P_{2n}` | the paired geometric series; closed-walk counting; Vandermonde | B |
| V2 | `P_{2n} ≤ (36/11)^{3/2}/(4π^{3/2}n^{3/2}) + 2e^{−4n/(3π²)}` | the two cosine inequalities; the two-region split; a Gaussian integral | C |
| V3 | `75/100 < 3G(0) < 76/100` | `S_{1000}` exactly; the tail majorants; rational comparison | D |
| V4 | the threshold `β > 76/100`; the window | V3 with blocks 19 and 21 | — |

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

## Corollary V4 — the sharpened threshold and the window

**Statement (conditional on blocks 19 and 21 for their halves).** In block 19's G3–G5, the condition `β > 3G(0)` may be replaced by `β > 76/100`: the unsoldered sphere static law with the exponential overlap on `Z³` has long-range order and the Green-function channel for every `β > 76/100`. Together with block 21's `β < √3/6`, the kernel's coupling window on `Z³` is `[√3/6, 76/100]`, of width below `1/2`. The route's constant is not below `75/100`, so no sharper bound on `G(0)` can improve the threshold of that route by more than `1/100`.

**Proof.** V3 with block 19's G3 (`M² ≥ 1 − 3G(0)/β`) and block 21's W5–W6; the referenced halves are open PRs cited as evidence addresses, not as authority. ∎

*Not claimed.* The location of the true ordering threshold (a different route might order below `3G(0)`); the band `[√3/6, 76/100]` itself; the Born overlap; the normalization.

## No-Go Discipline Gate

The negative sentence is the lower half of V3: block 19's route cannot certify order below `β = 75/100`. Its escapes are named, not closed: a different route to order (not attempted); the band.

### N1 — Routes by which V3 could fail
1. *A closed-walk count or the Vandermonde form is wrong* — closed: enumeration for `n ≤ 3` and the multinomial sum to `n = 12` (B1).
2. *The return-sum identity misses the odd terms or the sign of `φ`* — closed: the paired series `(1 + φ)Σφ^{2m}` has nonnegative terms and the odd integrals vanish (B2).
3. *The tail bound's inequalities* — closed: derivative arguments executed symbolically, the Gaussian integral and the two-region step (C1–C3).
4. *The rational majorants of the tail* — closed: `π ≥ 3`, `π² ≤ 10`, `e^{−2/15} ≤ 197/225` from `e^{−x} ≤ 1 − x + x²/2` (C3, D2).
5. *A different route to order* — an escape, named.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: V1–V3 are statements about one number; V4 depends on blocks 19 and 21 as evidence addresses.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the five sentences under Premises | yes (premise, through the placement) |
| the possibility-covariance note (`main`) | the sphere domain and the unsoldered reading, through the placement | V4 only (proposed) |
| block 19 (PR #8153) | the route whose constant is pinned | V4 only (evidence address) |
| block 21 (PR #8155) | the weak-coupling half of the window | V4 only (evidence address) |
| block 13 (PR #8147) | context (the same walk's return probabilities) | no |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "`75/100 < 3G(0) < 76/100`" | executed: the closed-walk counts `1, 6, 90, 1860`; the Vandermonde form to `n = 12`; the cosine derivative identities | executed: the two-region step on the symbol at sample wavevectors | executed: the Gaussian integral; the constant's identity; the integral comparison for `Σ n^{−3/2}` | executed: `S_{1000}` exactly; the two rational comparisons; the majorants | proved: V1–V3 exact; V4 conditional on the referenced open blocks |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or overlap; none is a wall.

### N7 — Steelman
Hostile reviewer: "The value of the return sum is a classical constant known to many digits; computing a thousand terms is busywork." Reply: the value is not cited, because the lane's rule is to re-prove what is load-bearing; what the note supplies is an exact, machine-checked pinning of the route's threshold with an elementary tail bound, and the consequence that the kernel's window has width below one half. Conceded: the true threshold of the law is not located; only the route's constant is.

### N8 — Cross-cycle echo
Block 13's heat-kernel coincidence probabilities are the same walk's return probabilities in another role; block 19's crude bound is the `n → ∞` part of this note done with a single inequality; block 21's constant is the other end of the window.

## Falsifiers
- A count of closed walks for some `n ≤ 3` other than `1, 6, 90, 1860`, or a Vandermonde form differing from the multinomial sum for some `n ≤ 12` (B1); a paired-series identity that fails, or an odd integral that does not vanish at sample wavevectors (B2).
- A failure of `g'' = cos u − 1 + u²/2`, of `h' = u − sin u`, of the sample-point inequalities, of the Gaussian integral `(36π/(11n))^{3/2}`, of the constant's identity, or of the two-region step (C1–C3).
- `⌊10^6 S_{1000}⌋ ≠ 1501637`, a failed rational comparison, `S_{1000} ≤ 150/100`, or a majorant identity that fails (D1–D3).

## Boundaries and non-claims
This note proves, for the constant `3G(0)` of block 19's infrared route, the exact two-sided bound `75/100 < 3G(0) < 76/100`, so the route's ordering threshold for the unsoldered sphere static law is `β > 76/100`; it does not locate the true ordering threshold, does not treat the band `[√3/6, 76/100]`, does not treat the Born overlap, does not re-prove blocks 19 or 21, does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- The possibility-covariance note (on `main`): the sphere domain and the unsoldered reading, through the placement only; proposed, unaudited. PRs #8153 and #8155 (open) referenced as evidence addresses for V4 only; PR #8147 for context.
- Re-proved at scope: V1 (termwise integration of the paired series; closed-walk counting; Vandermonde), V2 (the two cosine inequalities; the two-region split; the Gaussian integral), V3 (the integral comparison; the rational majorants).
- Named standard imports at definition level (never as authority for physics): the monotone limit theorem for integrals of series of nonnegative functions; the elementary bounds `3 < π < 22/7` (hence `π² < 10`).
- Reference only (named, not used): Watson (1939); Glasser–Zucker (1977).

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane at each conclusion; no subagents). The control (`specs/supervisor_control_block22_return_sum.py`) computed the exact partial sums to `N = 2000` (timing: about ten seconds at `N = 1000`, two and a half minutes at `N = 2000`, so the runner uses `N = 1000`), compared the crude tail constant of block 19's inequality (`1.81/√N`) with the quartic one (`0.53/√N`), checked the tail bound against the exact `P_{2n}` for `n ≤ 60`, and ran the rational comparison at `N = 2000` against `77/100` before the contract fixed `N = 1000` and `76/100`; the lens pass is in `GOAL_block22.md`; the primary seat wrote V1–V4 and the runner; the refuting pass (`CHECKER_block22_findings.md`) recomputed the multinomial sums by direct enumeration of `(a, b, c)` for `n ≤ 300`, estimated the true tail by fitting `P_{2n} ≈ c n^{−3/2}` (the sum then lands within `10^{−4}` of the classical value, which is used there as a reference only), checked the tail bound against the exact `P_{2n}` for `n ≤ 1000`, the symbol's lower bound on a grid of the cube, and the exponential majorant. Facts settled while executing: the crude bound of block 19 is the `n → ∞` end of this argument done with one inequality; the quartic bound near zero is what makes a thousand terms sufficient.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.py --mutation certificate_target_wrong
```

Families: A authority and inputs; B the closed-walk counts, the Vandermonde form and the paired series; C the cosine inequalities, the Gaussian integral and the two-region step; D the exact partial sum, the majorants and the certificate; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
