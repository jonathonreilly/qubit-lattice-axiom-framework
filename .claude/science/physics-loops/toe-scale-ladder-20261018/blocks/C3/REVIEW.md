# C3 independent review

**Reviewer:** independent mathematical review (a Claude reviewer subagent, same model as the author; not the author session). Date: 2026-10-18.
**Object:** `blocks/C3/NOTE.md` (author draft, commit 649091ce3) and its scripts and logs.
**Method:** each load-bearing step was re-derived by hand (below). Separate code was written in `review_scripts/`. It uses different methods from the author's runner, and none of the author's code is imported.
**Evidence:** `review_scripts/run_review.sh` → `review_scripts/logs/review_all.log`, ending `TOTAL: PASS=75 FAIL=0`. The per-script logs are `logs/r1.log` … `logs/r4.log`. The full run takes about 70 s on one core, niced.

## Overall verdict

The mathematics of Theorems A, A′, B, C and D is **correct as stated**. Theorem F's arithmetic is correct, conditional on I-16. I found **no blocking errors**.

The non-blocking findings fall into three groups:
- the wording of the **necessity corollary of Theorem G**, which is false as worded;
- the "trichotomy", the title and §0 item 4, which overstate what was shown;
- the interpretation of F, plus several claim-type and scope labels.

All are fixable in the text. None changes a proof.

## Per-claim verdicts

| Claim | Verdict | Severity of findings |
|---|---|---|
| A1 (finite ancestors, uniqueness, any clock law) | correct; the claim-type label needs a fix (F6) | non-blocking |
| A2 (`P(L≥n) ≤ c_n/(n+1)!`, with atoms allowed) | correct | – |
| A3 (`R ≤ L+1`; the map's `R`-constant is false) | correct | – |
| A4, A′ (stationarity, law-independence, exchangeable tie-free) | correct | – |
| B1 (half-distance covariance bound and Stirling form) | correct | – |
| B2 (stopping-set coupling, `exp(−r ln r+O(r))`) | correct, with a small scope fix (F7) | non-blocking |
| B3 (mixing, entire structure factor, no LRO/SSB/power law) | correct, with a citation fix (F7) | non-blocking |
| C1–C3 (rate-dependent coding-radius bound) | correct | – |
| C4 | correct, with a wording fix (F8) | non-blocking |
| C5 | correct (thinning; the Liggett identification is imported) | – |
| D (finite-range-factor clocks) | correct | – |
| F (covariant-in-law ordered witness) | correct conditional on I-16; interpretation needs fixes (F2, F3) | non-blocking |
| G-I, G-II, G-III | correct as listed | – |
| G necessity corollary, "Concretely (i)–(iii)" | **incorrect as worded**; correct with fix (F1) | non-blocking (no proof depends on it) |
| "Trichotomy" label, title, §0 item 4 | overstated (F4) | non-blocking |
| Novelty table (§8) | accurate (F6) | – |

## Load-bearing steps: independent derivations and evidence

### 1. Theorem C (neighbour-dependent rates)

**(a) Cutoff at the first sure point.**
- A point with `V ≤ λmin/λmax ≤ λ_x(η)/λmax` is accepted whatever `η` is.
- So if `x` is still blank at `σ_x`, it forms there. Hence `τ_x ≤ σ_x`.
- Points after `τ_x` are inert, because acceptance is only tested at blank sites.
- So the relevant points `Π_x ∩ (0,σ_x]` contain every point that can matter. The points in `(τ_x, σ_x]` are harmless over-counting.

Evidence: r2 adds post-σ points at every site and re-runs the forward simulation; `ξ_0` is unchanged in all samples.

**(b) Unexplored neighbours are blank.**
- If `z` has no relevant point before `s`, then `z` has no point at all before `s`, because the first point of `Π_z` is always relevant.
- Its formation point lies in `(0,σ_z]`, so `z` is blank at `s−`. The inference is correct.
- The exploration reads `Π_z` on `(0,s)` at boundary sites, which is within `C(x) ∪ ∂C(x)`.
- The event `{ρ ≤ m−1}` is determined by the data on `B(x,m)`, so `R ≤ ρ+1`.

Evidence (r2) is a **forward** time-ordered event simulation. This is a different method from the author's backward recursion. It was run on Z with κ=4 (3000 samples) and κ=7 (1500 samples), and on Z² with κ=3 (299 samples). The rule makes both rates and contents depend on neighbour contents: content is the XOR of formed neighbours, and the rate rises with the number of 1-neighbours.
- Data outside `B(0,ρ+1)` was replaced in three ways: fresh data, fresh data plus inert points, and an **adversarial** exterior that forms at time ≈0 with sure points. `ξ_0` changed in **0** cases.
- Power control: resampling outside `B(0,ρ−1)` changes `ξ_0` in 518/2651, 157/1393 and 30/277 samples. So the test has power, and `ρ+1` is close to tight.

**(c) Intensity `λmax e^{−λmin t}`.**
- Sure points are an independent λmin-thinning of `Π_x`.
- By Mecke, `E Σ_{t∈Π} 1{no sure point of Π in (0,t)} = ∫ λmax P(no sure point in (0,t)) dt`. Adding the point `t` does not change the event on `(0,t)`. This gives `λmax e^{−λmin t}`.
- For distinct sites the processes are independent, so the multivariate factorial-moment formula is the product.
- The integral over `t_0>…>t_n>0` equals `κ^{n+1}·P(Z_0>…>Z_n) = κ^{n+1}/(n+1)!`.

Evidence: r2 runs a Monte Carlo of the number of rightward chains of lengths 1–5 on Z. It agrees with `κ^{n+1}/(n+1)!` within 4 SE for κ=4 and κ=7.

**(d) Loop erasure.**
- Take a minimal-length chain ending at `(y,s)` and suppose `y_j = y_k` with `j<k`. Splicing out steps `j…k−1` keeps everything needed:
  - adjacency, since `y_k = y_j ∈ N(y_{j−1})`;
  - strict time decrease, since `t_{j−1} > t_j > t_k`;
  - relevance, which is a property of the point.
- When `j=0`, the spliced chain starts at the relevant point `(x,t_k)`, which the definition allows (`t_0` is any relevant point of `x`).
- So the endpoint set of all chains equals that of distinct-site chains, and the factorial count from (C1) applies to the reach.

Evidence: on Z the distinct-site chains are exactly the straight chains. In every sample of r2, the space-time point reach found by a BFS over all chains, with revisits, **equals** the straight-chain reach, with 0 failures.

**(e) Tail.** In r2, `P(ρ≥n)` stays below `D(D−1)^{n−1}κ^{n+1}/(n+1)!` wherever the bound is below 1. The bound is very loose; for example at κ=4 it gives `P(ρ≥10)=0.001` against a bound of 0.21.

**(f) C5.** r3 computes the exact Markov jump-chain final law on the 3-site path with κ=3, as an exact rational recursion. The graphical construction matches it (worst |z| = 2.59 over 8 atoms, 40 000 samples).

### 2. B2 resampling

The argument is:
- `{S_A=S} ∈ σ(ω|_S)`;
- `ω|_{S^c}` and `ω′|_{S^c}` are both independent of `ω|_S` and have the same law;
- so `P(S_A(ω)=S, ω*∈E) = P(S_A(ω)=S, ω∈E)`, and summing over the countably many finite `S` gives `ω* ~ ω`.

The other steps:
- `S_A(ω*) = S_A(ω)` holds by the stopping property.
- `S_B(ω*) = S_B(ω′)` holds on the disjointness event, again by the stopping property applied to `ω′`.

The proof is correct. It relies on `S_x` including the boundary `∂Anc(x)`; `Anc(x)` alone is not a stopping set.

Evidence (r3) uses exact enumeration on the path 0–1–2–3, with `T` uniform on {1,2,3} (so ties occur), bits `U`, and a deterministic parity rule with zeros, over all 1.68 M pairs `(ω,ω′)`:
- `ω*` has exactly the law of `ω`;
- the three identities hold;
- `E f g(ω*) = E fg` and `E f g(ω′) = EfEg` exactly;
- `|Cov| = 1/81 ≤ P(meet) = 5/9`.
- **Negative control:** resampling outside `Anc` only, without the boundary, gives a wrong law, with 768 atoms differing.

### 3. XOR certificate

The extensions are admissible:
- An exterior site later than every window site cannot be an ancestor of any window site, because the first step out of the window would have to go to an earlier time.
- So the blank-exterior window computation is exact on that event.
- Under any continuous clock law with an interval support, the event has positive conditional probability given the window values, and so does every relative-order completion.
- This holds under the conditional-law ("a.s.") reading of `R`. Under the literal "every modification" reading the lower bound is even easier, and the upper bound `R ≤ L+1` holds pointwise under both readings: the boundary clocks of `S_x` lie inside `B(x,m)`.

Evidence (r1) uses a different method from the author. The XOR rule is linear over F₂, so `ξ_0 = ⟨c(order), U⟩`. A window pattern is undetermined if and only if some completion puts nonzero weight on an exterior mark, or two completions give different window parities.
- Results: `P(R≥2)=2/3`, `P(R≥3)=17/60`, and additionally `P(R≥4)=5/63`. In each case the lower bound equals `P(L≥m)`, so the values are exact.
- The closed form `2/(m+1)! − 1/((2m+1)m!²)` is confirmed.
- All three values exceed the map's `2/(m+2)!`.

The map's statement `P(R≥n) ≤ 2d(2d−1)^{n−1}/(n+1)!` is therefore **false** within the map's own domain: it includes nearest-neighbour rules with zeros, and the XOR rule is one. The corrected `P(R≥n+1)` is right.

### 4. Other derivations

- **A2.** Conditional on the times being distinct, the ranks are uniform, so `P(strictly decreasing) = P(distinct)/(n+1)!`. A union bound over the `c_n ≤ D(D−1)^{n−1}` SAWs finishes it, since `N_0` is symmetric and the walk cannot return. Correct with atoms.
- **B1.** Disjoint windows give `|Cov| ≤ 2‖f‖‖g‖(P(E_A)+P(E_B))`. The Stirling form holds without the condition `r ≥ 2e(D−1)`: `e(D−1)/q ≤ 2e(D−1)/r` for `q = ⌈r/2⌉`. r4 checks it numerically on a grid.
- **B2 term inequality.** `a(k_1−1)a(k_2−1) ≤ D²(2(D−1))^s s/s!`, including the boundary cases, checked in r4.
- **A′.** de Finetti on a countable index set gives a random directing law `Q`. Tie-freeness gives `Q` atomless a.s., and then A4 applies. Correct. Tie-freeness is essential; see F1.
- **D.** For a greedy kept site, every later conflicting site satisfies `y−x ∈ K−K`, and `K−K` is symmetric and contains 0. So each kept site discards at most `b−1` others, the kept windows are pairwise disjoint, and the kept clocks are iid. Correct.
  - Own enumeration (r4): `max(ζ_x,ζ_{x+1})` on Z gives `2/(n+2)!` for n ≤ 5, in both directions.
  - By hand, the constraints are `ζ_0>…>ζ_{n−1}` above both `ζ_n` and `ζ_{n+1}`.
  - Z² path shapes with `K={0,e1,e2}` respect the bound, but trivially, since b=7.
- **F arithmetic.** `|Stab_{O_h}(e_1)| = 8`, and `(1/6)(1−6·10⁻⁵) − 1/36 = 124991/900000`, both verified in r4.
  - I checked I-16 (09-16 T7(c)): it states six translation-invariant invariant laws `μ_a` with `μ_a(v≠a) ≤ 3/10⁵`, obtained by Cesàro limits.
  - It also states that the level rule draws from `K(·|v_{x−e1},v_{x−e2},v_{x−e3})`, and its placement paragraph identifies stationary level laws with translation-invariant formation laws. This matches the import.
- **09-22 κ values.** 7, 49 and 7 are correct for `k ∈ {0..6}`.

## Findings

**F1 (non-blocking, a genuine error): the necessity corollary's "Concretely, one of (i)–(iii)" is false as worded.**
- Counterexample (exact, r4):
  - with probability ½ every `T_x = ½` (all tied); with probability ½ the `T_x` are iid U[0,1];
  - the rule on Z is `r(·|∅)=δ_0`, and content 1 if some neighbour is strictly earlier.
- This clock field is exchangeable, a mixture of iid laws. It is translation-covariant and O_h-covariant in law, and it has pairwise **uncorrelated** clocks (`Cov(T_x,T_y)=0`).
- Yet `Cov(ξ_0,ξ_r) = 1/9` for every r ≥ 3, which is long-range order by the note's §1 definition.
- It falls under none of (i)–(iii): (i) excludes "an exchangeable family", and (ii) and (iii) concern rates.
- The first sentence ("outside every class in G-I") survives, because A′ needs tie-free clocks.
- **Fix:**
  - In (i), replace "or to an exchangeable family" with "or to a tie-free exchangeable family".
  - Add "(iv) a non-trivial mixture of clock laws inducing different record laws (e.g. exchangeable clocks with atoms)", or fold this into (i) as "infinite-range *dependence*".
  - Replace "correlation" by "dependence" throughout §0 item 4 and G.

**F2 (non-blocking): F's "long-range order survives O_h-averaging" is weaker than it reads.**
- Under the §1 covariance definition, *any* non-trivial mixture of laws with different one-site marginals has covariance-LRO; F1 is an unconditional example with FFIID components.
- What F actually shows is that `W` is a covariant-in-law record field whose ergodic components are the non-unique level-order phases of I-16. Uniqueness given the data fails there, which never happens in G-I.
- **Fix:**
  - State F's content as non-uniqueness or phase coexistence inherited from I-16.
  - Note that covariance-LRO of a non-ergodic law is automatic once the components differ.
  - Optionally restrict the §1 LRO notion to ergodic (extremal) laws, or add "of an ergodic component".

**F3 (non-blocking): wording of "covariant in law" in F.**
- `T_x = ⟨w,x⟩` is not translation-invariant in law as a real-valued field: `T_0 ≡ 0`. It is covariant only modulo a global time shift, i.e. as an order.
- In `W`, the phase `g e_1` is coupled to the clock direction: `⟨g e_1, w⟩ = +1` always (r4).
- The record is not a function of clock and marks; the phase is extra randomness.
- **Fix:** say "covariant in law up to a global time shift (as an order relation)", and state that the phase is extra randomness coupled to `w`.

**F4 (non-blocking): the "trichotomy", the title and §0 item 4 overstate what was shown.**
- The three regimes are not exhaustive; §7 itself lists OPEN classes.
- "An ordered record phase needs a nonlocal clock" and "Order needs an infinite-range clock correlation" contradict the corollary's own open alternatives (ii) λmin=0 / λmax=∞ and (iii) non-Markov rates.
- "Local clocks" (G-I) includes exchangeable clocks, which are not local.
- **Fix:**
  - Call it a "three-regime classification (non-exhaustive)".
  - Qualify the title and item 4 with "within bounded-rate Markov rates".
  - Rename G-I "clock classes with finite ancestry tails".

**F5 (non-blocking): C3's "Status" line says that no independent check has been run.** Update it after this review. The author's `logs/run_all.log` was not relied on.

**F6 (non-blocking): claim-type labels.**
- On main, (A1) and the first part of (A2) are stated for iid **Exp(λ)** clocks in d=3:
  - 09-07, "Infinite recursive construction", lines 45–49;
  - 10-08 §2, line 60.
- The any-law, atoms, general-`D` and arbitrary-rule versions are COROLLARY (the same proof), not ON-MAIN. §8's table already says this; align the §2 claim-type line with it.
- Novelty check: I grepped `docs/` for "finitary factor", "coding radius", "FFIID" and "superexponential", and for infinite-volume state-dependent-rate constructions. Nothing found. 10-08 line 84 explicitly leaves feedback-dependent rates open. So "new in repo" for the FFIID/coding-radius statement, B1/B2 and Theorem C is accurate. The disclaimer of methodological novelty (Penrose 2002) is appropriate.

**F7 (non-blocking): scope of B2 and B3.**
- The count "`(2s+1)^d` sites with `k_1+k_2=s`" holds for nearest-neighbour `N_0`. For a general finite `N_0` of ℓ∞-range `h`, use `(2hs+1)^d`; the asymptotic is unchanged.
- "Mixing of all orders" does not follow from the two-set bound B2 alone. Cite that factors of iid are mixing of all orders, or extend B2 to k sets (the same coupling works).

**F8 (non-blocking): C4 says "A4 holds verbatim".** Only the covariance and stationarity parts carry over. The last sentence of A4 (the law does not depend on the clock law) is false under rate modulation. **Fix:** say "the stationarity/symmetry parts of A4".

## Files

- `review_scripts/rv_common.py`: check harness.
- `review_scripts/r1_xor_linear_coding_radius.py`: the F₂-linear exact XOR coding radius, m=1,2,3.
- `review_scripts/r2_rate_dependent_forward_mc.py`: the forward-simulation determinacy test for Theorem C, with adversarial exteriors, power control, the loop-erasure point-reach identity, C1 chain means and the tail.
- `review_scripts/r3_stopping_set_exact_and_markov.py`: exact B2 resampling with ties, the negative control, and C5 against the exact jump chain.
- `review_scripts/r4_clocks_bounds_witness.py`: Theorem D enumeration, the B1/B2 inequalities, F arithmetic, κ values, and the F1 counterexample.
- `review_scripts/run_review.sh` → `review_scripts/logs/review_all.log` (`TOTAL: PASS=75 FAIL=0`).

## Correction confirmation

I re-read the complete corrected `NOTE.md`, §0–§12. The proofs of A–D and the import of F are unchanged from the version reviewed above. The author's `logs/run_all.log` ends `TOTAL: PASS=59 FAIL=0`; the new check s3(f) is the W-tie witness, and it agrees with my r4 value `Cov = 1/9`. I did not re-run the author's suite, and my own evidence is unchanged (`review_scripts/logs/review_all.log`, `TOTAL: PASS=75 FAIL=0`).

| Finding | Resolved? |
|---|---|
| F1 | **Yes.** (i) now says "tie-free exchangeable" and "dependence". W-tie is recorded with correct values: `Eξ = 1/3`, `Eξ_0ξ_r = 2/9`, `Cov = 1/9`. Adding (ii), mixtures of clock laws inducing different record laws, is correct. It is a special case of (i): a non-ergodic clock law is not a finite-range factor of iid, and tie-free exchangeable mixtures induce one record law by A′. Items (iii) and (iv) are the old open options. The new disclaimer, "a restatement of 'outside G-I', not a sufficiency claim, not exhaustive", is accurate. |
| F2 | Yes (§6 "What F does and does not show"). |
| F3 | Yes (Theorem F bullets; §0 item 4). |
| F4 | **Yes.** "Three-regime classification (not exhaustive)" is now accurate. The new title, "within bounded-rate Markov clocks, an ordered record phase needs infinite-range clock dependence", is true: it excludes the open options (iii) and (iv) by its qualifier. |
| F5–F8, B1 remark | Yes. |

**New issues introduced: minor, all non-blocking.**
- **N-a.** §6 now says the §1 LRO notion "is meant for ergodic laws", but the §1 definition is unchanged, and the necessity corollary cites the non-ergodic W-tie and `W` as LRO examples.
  - The corollary is true under either reading, because every G-I law is ergodic.
  - Fix: keep §1 as stated and change the remark to "for non-ergodic laws, covariance-LRO only signals a non-trivial mixture".
- **N-b.** The W-tie block sits between the statement of Theorem F and its `*Proof.*`, so the proof now reads as if it were W-tie's. Fix: move W-tie after F's proof.
- **N-c.** Residual wording:
  - N1 route 3 still says "Exchangeable … closed by A′"; it should say tie-free, consistent with route 5.
  - N2 still says "infinite-range clock correlation"; W-tie's clocks are pairwise uncorrelated, so this should say "dependence".
  - W-tie lives on Z, so "O_h-covariant" should read "reflection-covariant on Z (the construction works on any Z^d)".
  - Pre-existing: N1 says "five distinct" routes but lists seven.

**Final verdict: READY.** No mathematical defect remains, and every claim is correct as stated with its domain and quantifiers. N-a to N-c are editorial and can be fixed in the same pass without re-review.
