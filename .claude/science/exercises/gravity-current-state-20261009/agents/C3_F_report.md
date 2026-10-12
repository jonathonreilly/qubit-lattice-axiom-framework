# C3 lane F: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. **Codex sol referee: CONFIRMED WITH CORRECTIONS. This is a bounded FAIL, not a universal no-go. Three classes cannot reproduce 4D sprinkling: exchangeable generating-subset growth (link means), frontier-only growth (L <= N-1), and every classical DGC+Bell dynamics including VR towers (asymptotically, since 2+2 and 3+1 densities vanish). A surviving rule must use the order non-exchangeably, or leave the Markovian, classical or Bell-causal scope** (C3_F_referee.md).

**Verdict (worker):** FAIL, under stated hypotheses. The class is sequential growth in which each new element's set of direct ancestors is exchangeable over the existing elements. That class contains every Markovian, label-invariant, Bell-causal (Rideout-Sorkin CSG) model, at any couplings, including couplings that vary with N. Frontier-only rules are also excluded, and Varadarajan-Rideout era towers are excluded asymptotically through Brightwell-Georgiou. Rules outside these classes are not excluded. needs_referee = true; the codex sol referee must confirm before this is recorded.

**Plain summary:** No growth rule of the kind tested can make the event set by itself, and two of the reasons are proved, not fitted. If a new event picks its immediate ancestors without preferring any existing event (this covers every classical sequential growth model, including transitive percolation, at any couplings), each event ends up with on average at most 1 + ln N links to later events. In a 4D sprinkling the link count per event grows like the square root of N: 17.75 against a ceiling of 7.9 at N = 1000, and 64 against 10 at N = 8000. So these rules miss the 4D link structure at every N of 300 or more, with no extrapolation. Rules that only attach a new event on top of the current newest events give each event at most one later link, which is worse still. Brightwell-Georgiou's published theorem independently says every such model's orders become nearly one-dimensional "semiorders" at large N. Numerically, every rule tuned to the 4D ordering fraction (dimension 4 by Myrheim-Meyer) still misses link density, interval counts and height by z = 13 to 1356, so the supplied sprinkling remains a price unless a rule that prefers particular events (one that encodes geometry) is found.

# Lane F report: can records forming produce the event set themselves?

**Worker:** Claude Opus 5.5, maximum effort, campaign C3.
**Run:** 2026-10-10, 00:53Z to 01:40Z.
**Status:** test setting only. No repository file was edited.
**Pre-registration:** `PREREG.md`, stamped `Sat Oct 10 01:00:10 UTC 2026`, before any computation.

## 1. Verdict against the fixed reading (TESTS.md, "Campaign C3, added lanes")

**FAIL under stated hypotheses. It needs the codex sol referee before it is recorded (TESTS.md:9).**

The reading's FAIL is "a no-go under stated hypotheses (referee). For example, Markovian label-invariant growth gives non-manifold orders." The verdict rests on three no-gos and a numerical sweep.

**(1) Theorem L: a link-valency bound (EXACT; new here, proof in §6).**
- **Hypothesis H-exch:** given the history, the law of the new element's direct-ancestor set D is invariant under permuting the existing elements. The past of the new element is ↓D.
- **Result:** for every element i and every N, E[#future links of i] ≤ E[H_{|↑i|}] ≤ 1 + ln N. Hence E[L]/N ≤ 1 + ln N.
- **What it covers:** every Rideout-Sorkin CSG model (any t_k ≥ 0, including t_0 = 0 originary percolation, dust, forest and zero couplings). It also covers couplings that change with the stage or with N; that is the Rideout-Sorkin continuum-limit scaling p = p(N).
- **The 4D comparison:** a 4D sprinkled diamond has L/N = 7.55 ± 0.19 at N = 300, against a bound of 6.70. At N = 1000 it is 17.75 ± 0.11 against 7.91. At N = 8000 it is 63.98 ± 0.14 against 9.99. It grows roughly like √N.
- **So:** no rule in the class matches the 4D link statistics at any N ≥ 300. No fitted trend is extrapolated.

**(2) Frontier lemma (EXACT).** Consider any rule whose new element sits above a subset of the current maximal elements, with any probabilities, label-invariant or not. Each element then has at most one future link, so L ≤ N − 1.

**(3) Brightwell-Georgiou 2010 (COMPARATOR; read in the paper).**
- **Their Thm 1.5:** uniformly over all CSG models, for n ≥ n0(ε) the order is within εn² pairs of a semiorder.
- **Their proof of Thm 1.6:** this gives E λ(2+2) and E λ(3+1) < 12ε.
- **The 4D diamond:** λ(2+2) = 0.00476(3) and λ(3+1) = 0.00496(4), at every N.
- **Extension:** an ordinal-sum lemma (EXACT, elementary) carries this to the Varadarajan-Rideout era towers.
- **Limit:** this route is asymptotic only, because n0 is not explicit.

**(4) Numerics (CHECKED).** No rule tested matches, even with its parameter re-tuned at every N.
- Every rule was tuned to the exact 4D ordering fraction r = 0.1, which gives d_MM = 4.0.
- They still miss L/N by z = −140 to −286, n1/n0 by z = +110 to +776, and height by z = +13 to +74.

**Scope: what is not excluded.**
- Rules whose ancestor choice is neither exchangeable nor frontier-only, i.e. structure-aware rules that prefer particular existing events.
- Non-Markovian rules.
- Label-invariant rules without Bell causality (the Brightwell-Luczak order-invariant class), unless they are exchangeable.
- Quantum or complex sequential growth.
- Path-integral weightings over orders (the BD action).
- Rules that use extra qubit or admissibility data.

## 2. What I read

**In full:**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines);
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`;
- packet `TESTS.md`: all 546 lines, including the rules, E1, E1′, E1′-b, the C3 lanes and the "added lanes" readings for F;
- `SUMMARY.md` §7-9;
- `agents/prior_art_event_history.md`, `agents/E1p_report.md`, `agents/E1p_referee.md`;
- `scripts/E1/bd_core.py` and `scripts/E1p/e1p_core.py`.

**Repository prior art (one line).** The archived audits (`archive/.../EXACT_LAW_UNIQUENESS_SELECTION_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md` §8 and `CAUSAL_REVERSIBLE_ACTUALITY_WEIGHT_INDEPENDENCE_NOTE_2026-07-14.md`) record CSG only as "a broad family … couplings remain law data". Nobody had tested manifold-likeness.

**Literature, downloaded as untrusted data into new folders and never executed:**
- Brightwell and Georgiou, "Continuum limits for classical sequential growth models", RSA 36 (2010) 218-250 (`lit/bg2010/`): Thms 1.4-1.6 and 5.5, and the proofs of 1.5 and 1.6.
- Varadarajan and Rideout, gr-qc/0504066 (`lit/vr2006/`): the general solution with vanishing probabilities, i.e. t_k may vanish, plus "turtle" eras in which each new era lies to the future of all earlier ones.
- Abstracts via web: Ahmed and Rideout, arXiv:0909.4771.
- From memory, labelled COMPARATOR only: Rideout and Sorkin gr-qc/9904062 and gr-qc/0003117, Kleitman-Rothschild, Surya 2012, Glaser-O'Connor-Surya 2018, Loomis-Carlip 2018.

## 3. Setting and hypotheses

- **Reference ("4D Poisson sprinkling").** N uniform points (fixed N) in a 3+1 Minkowski causal diamond; only the causal order is kept. N ∈ {50, …, 8000}, with 12-32 realizations per N.
- **H-order:** the law sees only the order (no coordinates or labels).
- **H-seq:** elements are born one at a time, never removed, and are maximal at birth.
- **H-Markov:** transitions depend on the current order.
- **H-exch:** the direct-ancestor set is exchangeable over existing elements.
- **H-front:** the direct ancestors are current maximal elements.
- **DGC + Bell causality** (Rideout-Sorkin) give the CSG form (Rideout-Sorkin; Varadarajan-Rideout; COMPARATOR). CSG satisfies H-exch at every stage: given the history, |D| ~ w_n(k) ∝ C(n,k)t_k, and D is uniform given its size (EXACT).

**Rules run.**

| Rule | Definition |
|---|---|
| TP(p) | transitive percolation |
| OP(p) | originary percolation |
| FACT(t) | CSG with t_k = t^k/k! |
| CSGMIX(A, t) | CSG with t_0 = A + 1 and t_k = t^k/k! (two couplings) |
| FRONT0(p) | records form on the frontier: each current maximal element is selected with probability p, possibly none |

Each rule was run in two modes:
- **tuned per N** to r = 0.1 (generous: the law is allowed to know N);
- **fixed couplings** tuned at N = 1000 and then grown on (the honest growth reading).

## 4. Method

- **Representation.** Past bitsets in a natural labelling. The observables are computed from the order only:
  - R, r, d_MM;
  - links L;
  - interval abundances n_k (k = 0..12);
  - height H (longest chain);
  - minimal and maximal elements, posts, link degrees;
  - 4-element induced-suborder densities (2+2, 3+1), from 2×10⁵ random 4-subsets per realization.
- **Validation.** Brute-force agreement at N = 300 (`test_core.py`), and a transitivity check of the growth closure.
- **Tuning.** Bisection on mean r.
- **4D 4-point law.** Taken from 4×10⁶ iid 4-point samples, which is exact in law and N-independent.
- **Label invariance.** Exact enumeration of all labelled growth paths at N = 3 and 4 (`F7`).
- **Theorem L checks.** Exact enumeration at N = 6 (`F11`), and simulation (`F9`, `F5c`).

## 5. Results

**Table 1: tuned to r = 0.1 at each N.** Values are realization mean ± sd. z is (mean − 4D)/combined standard error. maxdeg is the maximum past-link degree.

| N = 1000 | n | r | L/N | H | nmin/N | n1/n0 | maxdeg | d_MM |
|---|---|---|---|---|---|---|---|---|
| 4D sprinkling | 32 | 0.0989 ± 0.0057 | 17.7 ± 0.6 | 9.81 ± 0.78 | 0.148 | 0.344 ± 0.009 | 129 | 4.01 |
| TP | 16 | 0.0985 (z −0) | 2.92 (z −140) | 17.4 (z +15) | 0.157 (z +2) | 1.82 (z +170) | 11 (z −68) | 4.02 |
| OP | 16 | 0.0987 (z −0) | 2.68 (z −142) | 21.8 (z +25) | 0.001 (z −47) | 1.76 (z +332) | 10.4 | 4.02 |
| FACT | 16 | 0.107 (z +4) | 2.69 (z −142) | 18.3 (z +25) | 0.068 (z −23) | 1.81 (z +289) | 7.8 | 3.92 |
| CSGMIX | 8 | 0.105 (z +1) | 2.75 (z −140) | 18.2 (z +13) | 0.100 (z −12) | 1.82 (z +110) | 8.5 | 3.94 |
| FRONT0 | 16 | 0.095 (z −1) | 0.99 (z −159) | 102 (z +50) | 0.364 (z +61) | 0.99 (z +368) | 5.5 | 4.06 |

At N = 4000 (4D: L/N = 42.6 ± 0.7, H = 14.9, n1/n0 = 0.400):

| Rule | L/N | H | n1/n0 |
|---|---|---|---|
| TP | 3.79 (z −267) | 23.8 | 2.36 (z +439) |
| OP | 3.59 (z −268) | 30.8 | 2.30 |
| FACT | 3.39 (z −270) | 25.5 | 2.30 |
| FRONT0 | 0.997 (z −286) | 390 | 0.997 (z +776) |

CSGMIX at its N = 1000 couplings drifts to r = 0.36. All values are CHECKED.

**Table 2: fixed couplings (tuned at N = 1000), the drift of d_MM and L/N (CHECKED).**

| Rule | N = 500 | N = 1000 | N = 2000 | N = 4000 | N = 8000 |
|---|---|---|---|---|---|
| TP | d = 5.62, L/N = 1.60 | 4.02, 2.92 | 2.45, 4.24 | 1.71, 4.96 | 1.35, 5.28 |
| OP | 4.61, 1.74 | 4.02, 2.68 | 2.78, 3.97 | 1.90, 4.90 | 1.45, 5.39 |
| FACT | 4.79, 1.89 | 3.92, 2.69 | 3.15, 3.52 | 2.53, 4.29 | 2.11, 5.03 |
| 4D sprinkling | 3.99, 11.28 | 4.01, 17.75 | 4.01, 27.48 | 3.99, 42.55 | 3.99, 63.98 |

A fixed growth law does not stay four-dimensional. TP and OP head toward a chain, consistent with BG Thm 1.4(i) and posts (COMPARATOR).

**Table 3: Theorem L bound against 4D.** The bound is EXACT; the 4D values are CHECKED.

| N | 50 | 100 | 200 | 300 | 500 | 1000 | 2000 | 4000 | 8000 |
|---|---|---|---|---|---|---|---|---|---|
| 4D L/N | 1.78 | 3.45 | 5.87 | 7.55 ± 0.19 | 11.28 | 17.75 | 27.48 | 42.55 | 63.98 |
| CSG bound 1 + ln N | 4.91 | 5.61 | 6.30 | 6.70 | 7.21 | 7.91 | 8.60 | 9.29 | 9.99 |
| TP-only bound B_loc = max_p min(p(N−1)/2, pΦ/q) | — | 3.37 | — | — | 4.61 | 5.17 | 5.75 | 6.34 | 6.94 |

**Checks of Theorem L.**
- **Exact enumeration at N = 6.** The bound holds for every label in TP(0.5), TP(0.2), FACT(2), and a non-CSG exchangeable rule whose selection size depends on the history.
  - TP(0.5), label 0: E[future links] = 1.4344 ≤ E H = 1.8963.
  - TP(0.2): 0.9133 ≤ 0.9556.
- **Simulation at N = 2000-8000.** Mean future links ≤ mean H_{|↑i|} in all 8 cases. Examples: 0.502 vs 0.502 (sparse, tight), 3.373 vs 3.492, 5.276 vs 7.848. The maximum future-link degree is 5-14.
- **TP exact identity** (infinite-window identity: E[#future links of i] = (p/q)Φ(p), Φ = Σ q^a/(1−q^a)), over 40 realizations:

  | p | measured (bulk elements) | (p/q)Φ(p) |
  |---|---|---|
  | 0.02 | 4.548 ± 0.014 | 4.530 |
  | 0.05 | 3.650 ± 0.011 | 3.653 |
  | 0.01 | 5.192 ± 0.015 | 5.206 |

**Table 4: 4-point (Brightwell-Georgiou) densities.**
- **4D law:** 2+2 = 0.00476 ± 0.00003, 3+1 = 0.00496 ± 0.00004. Sprinkled orders at N = 500-4000 reproduce them (ratios 0.93-1.05), so they are N-independent (CHECKED).
- **Tuned CSG.** Ratios to 4D for 2+2 / 3+1:

  | Rule | N = 500 | N = 4000 |
  |---|---|---|
  | TP | 1.74 / 1.19 | 0.99 / 0.34 |
  | OP | 1.30 / 1.27 | 0.77 / 0.40 |
  | FACT | 1.83 / 1.34 | 0.86 / 0.38 |

- **Reading.** The trend falls as BG predict. But at accessible N, 2+2 alone does not yet discriminate; 3+1 and the link statistics do (CHECKED).

**Table 5: large intervals I(x,y), with 400 ≤ |I| ≤ 1200, inside grown orders.**
- **4D diamonds at matched sizes:** r ≈ 0.10, d_MM ≈ 3.97, L/|I| = 9.9-18, H = 7.6-10.4, n1/n0 = 0.30-0.35.
- **Inside CSG orders:**
  - d_MM = 3.4-4.5, and 2+2/3+1 densities are comparable to 4D (an accident of single-number dimension estimators);
  - but L/|I| = 1.5-2.8, H = 20-27, n1/n0 = 1.3-1.8.
- **Inside FRONT0:** intervals are chains (r = 1).

So intervals of CSG orders are not 4D diamonds either (CHECKED at accessible sizes; the controlled local statement is in §6).

**Table 6: other checks.**
- **Label invariance by exact enumeration (N = 3, 4):** TP and FACT are invariant to 2e-16. FRONT0 is NOT invariant (spread 0.30 at p = 0.3). This matches a hand counterexample: the paths a, b, c give p(1−p)², but a, c, b gives p(1−p).
- **FRONT0 future-link degree:** at most 1 in every run, L ≤ N − 1. In a 4D sprinkling at N = 3000 the maximum is 251 and the mean 36.8.
- **CSGMIX grid** (45 coupling pairs at N = 1000, ln A from 0 to 120, t from 0.03 to 30): the largest L/N anywhere is 3.97. The 4D point (r = 0.1, L/N = 17.75) is unreachable, as Theorem L requires (bound 7.9).

## 6. Proofs

**Theorem L (EXACT).**
*Setting.* Let i be fixed, and for j > i let U_j = {i} ∪ {z < j : i ≺ z}, with A_j = |U_j|.

- **Step 1.** U_j is an up-set of C_j, and for any up-set V, ↓D ∩ V ≠ ∅ ⇔ D ∩ V ≠ ∅. So:
  - j ≻ i ⇔ D_j ∩ U_j ≠ ∅;
  - (i, j) is a link ⇔ i ∈ D_j and D_j ∩ (U_j∖{i}) = ∅.
- **Step 2.** By H-exch, given the history with A_j = a:
  - P(join) = J_j(a) := P(D ∩ S_a ≠ ∅) for any fixed a-set S_a;
  - P(link) = P(u ∈ D, D ∩ S_{a−1} = ∅) = J_j(a) − J_j(a−1) =: ℓ_j(a).
- **Step 3.** ℓ_j(a) is non-increasing in a, because the event shrinks as S_{a−1} grows. So J_j is concave with J_j(0) = 0. Then J_j(a−1) ≥ ((a−1)/a)J_j(a), so ℓ_j/J_j ≤ 1/a.
- **Step 4.** Write X_i = #future links of i. By the compensator identity, E X_i = E Σ_j 1{join at j}·ℓ_j(A_j)/J_j(A_j). Each level a = 1..|↑i| is left by exactly one join, and that join contributes at most 1/a. So E X_i ≤ E H_{|↑i|} ≤ 1 + ln N.
- **Step 5 (tail).** Each ξ_a is conditionally Bernoulli with mean ≤ 1/a. So E e^{θX_i} ≤ exp((e^θ − 1)H_{N−1}). Hence:
  - P(X_i ≥ K) ≤ e^{−μ}(eμ/K)^K, with μ = 1 + ln N;
  - by a union bound, max_i X_i ≤ e²(1 + ln N) with probability ≥ 1 − N^{1−e²}.
- **Step 6.** Σ_i X_i = L. ∎

*Local consequence (EXACT plus ARGUED arithmetic).*
- Links inside an interval are links of the whole order.
- So w.h.p. no interval of a CSG causet of N elements has elements with more than e²(1 + ln N) future links.
- A 4D diamond of N_I points has mean link degree ≈ 0.7√N_I (measured 0.715√N at N = 8000). Using that degree requires an extrapolation of the 4D reference, which is ARGUED.
- **Arithmetic for N ~ 10²⁴⁴** (Planck 4-volumes of a Hubble patch): no 4D-like interval of more than ~3×10⁷ elements, i.e. ~10² ℓ_P across (ARGUED arithmetic).

**Lemma TP (EXACT; sharper for TP).** The up-set size is an exact pure-birth chain with join probability 1 − q^A. This gives:
- E[#later elements incomparable to i] ≤ Φ(p);
- E[#future links] ≤ (p/q)Φ(p) ≤ (ln(1/p) + 1.582 + 0.582p)/q;
- links ⊆ edges, so E[L]/N ≤ p(N−1)/2.

For OP, the join probability is ≥ 1 − q^A and the edges per element are ≤ np + 1, so the same bounds hold with +1.

**Frontier lemma (EXACT).** If D_n ⊆ max(C_n), the covers of the new element are exactly D_n. An element y gains its only future link at the birth that selects it, after which y is no longer maximal. So L ≤ N − 1. ∎

**BG route (COMPARATOR plus EXACT glue).**
- Thm 1.5 holds uniformly in t, and the proof of Thm 1.6 gives E λ(H), E λ(L) < 12ε.
- Choosing ε = 3×10⁻⁴ gives < 0.0036, below the 4D values of 0.0048 and 0.0050, for n ≥ n0(ε).
- **VR towers.** An ordinal sum of semiorders is a semiorder, because elements of different summands are comparable, so any induced 2+2 or 3+1 lies inside one summand. Eras longer than n0 obey BG. Eras shorter than n0 contain ≤ N·n0/2 pairs. So Δ ≤ 1.5εN² once N ≥ n0/ε.
- **Positivity of the 4D values.** Both 2+2 and 3+1 occur on open sets of 4-point configurations in any region of M⁴ (EXACT).

**Asymptotic 4D abundance (ARGUED).** Near-null pairs have density ∝ v^{−1/2} in v = ρV. So n_k/n_0 → Γ(k+½)/(k!√π), giving n1/n0 → ½ from below. Measured: 0.31 → 0.42 for N = 500 → 8000. Every growth order here has n1/n0 ≈ 1 or more.

## 7. Comparators (state of the field)

- **Rideout-Sorkin 1999:** CSG is the general solution of internal temporality, DGC and Bell causality.
- **Varadarajan-Rideout 2006:** t_k may vanish, and "turtle" eras appear.
- **Rideout-Sorkin 2001** gave evidence of a TP continuum limit. **BG 2010** proved that the limit is a semiorder S_c, and that all CSG models are asymptotically semiorder-like. They conclude no CSG model approximates M^d for d ≥ 2.
- **Transitive percolation at fixed p** has posts and becomes chain-like (Alon-Bollobás-Brightwell-Janson; Bollobás-Brightwell). Here, d_MM drifts from 5.6 to 1.35 (Table 2).
- **Ahmed-Rideout 2010:** de Sitter-like expansion after posts in originary percolation. This is global; Theorem L shows the local link valency stays logarithmic regardless.
- **Kleitman-Rothschild:** 3-layer orders dominate the uniform measure.
- **Surya 2012 and Glaser-O'Connor-Surya 2018:** a BD-action path integral over 2D orders, a sample space that already supplies the dimension, has a continuum phase and a layered phase.
- **Loomis-Carlip 2018:** the BD action suppresses KR and bilayer orders.

None of these is a label-free growth rule that produces 4D manifold-like orders. The Surya, Glaser-O'Connor-Surya and Loomis-Carlip items are COMPARATOR from memory.

## 8. Meaning for the event substrate and the axioms

- **E1′'s gravity PASS** used Johnston's G₀ = aL, i.e. the sprinkling's link structure with valency ∝ (T/ℓ)². That is exactly what no exchangeable or frontier growth can produce (≤ 1 + ln N, or ≤ 1).
- **DGC is the dynamical form of A36** ("records carry no time": the birth order is gauge) (ARGUED).
- **H-exch is "no existing record is privileged"**, the growth analogue of the axioms' "no site/possibility is privileged" (ARGUED analogy).
- **Consequence:** a rule that works would have to privilege existing events by their place in the order, choosing ancestors near a cone-like layer. That supplies geometric selection, i.e. a price. The supplied sprinkling and order stay a price for the event route unless such a rule is exhibited and passes this lane's statistics.

## 9. What a referee should re-check

1. **Theorem L:**
   - the up-set characterisation;
   - exchangeability ⇒ ℓ non-increasing ⇒ ℓ/J ≤ 1/a;
   - the compensator identity over random level times;
   - the exponential-moment tail and the union bound;
   - that every CSG (t_0 = 0, zero couplings, stage- or N-dependent couplings) satisfies H-exch.
2. **The 4D link densities** (F1, F9) and the crossing N ≈ 300; whether L/N is admissible as the reading's "link statistics" (it was pre-registered as observable 2).
3. **The frontier lemma.**
4. **The BG use:** uniformity in t, the 12ε step, and the VR ordinal-sum extension (era lengths are fixed at era start; are cross-era pairs always comparable?).
5. **Whether the stated classes satisfy the reading.** The reading's example says "Markovian label-invariant". Theorem L needs Bell causality (via Rideout-Sorkin/Varadarajan-Rideout) or direct exchangeability. Label-invariant rules without Bell causality are not covered.
6. **Numerical code:**
   - bitset popcounts and the sub-order extraction (F6);
   - the four-point classifier;
   - the CSG sampler, i.e. the uniform k-subset given w_n(k);
   - per-realization statistics.

## 10. Files

All files are under `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/F/`:

- `PREREG.md`
- **`scripts/`:** fcore.py, fcore2.py, test_core.py, F1_reference.py, F2_growth.py, F2b_analyse.py, F3_fourpoint.py, F3b_analyse.py, F4_front0.py, F5_lemmaTP.py, F5b_locallinks.py, F5c_linkcheck.py, F6_intervals.py, F6b_analyse.py, F7_label_invariance.py, F7b_front_updegree.py, F8_csgmix.py, F8b_csgmix_grid.py, F9_valency_theorem.py, F10_tables.py, F11_theoremL_exact.py, pdf2txt.py
- **`out/`:** F1_reference.json/.log, F2_{TP,OP,FACT,FRONT0}.json and logs, F2b_analyse.out, F3_fourpoint.json/.log, F3b_analyse.out, F4_front0.log, F5_lemmaTP.out, F5b_locallinks.out, F5c_linkcheck.out, F6_intervals.json/.log, F6b_analyse.out, F7_label_invariance.out, F7b_front_updegree.out, F8_csgmix.json/.log, F8_csgmix_summary.out, F8b_csgmix_grid.out, F9_valency_theorem.out, F10_tables.out, F11_theoremL_exact.out
- **`lit/`** (untrusted data, never executed): bg2010/contlim.pdf and .txt; vr2006/vr.pdf and .txt


---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** True

**Corrected verdict:** FAIL under stated hypotheses, as a bounded no-go. It still needs the codex sol referee before it is recorded (TESTS.md:9). The scope must be narrower than the report's framing:

(a) Finite N, for every N ≥ 300. This is EXACT, proved by Theorem L and checked here. No rule whose direct-ancestor set is exchangeable given the history can match the 4D diamond's link density. The class includes all Rideout-Sorkin CSG with any t_k ≥ 0, couplings that depend on the stage or on N, and mixtures of CSG. The link-density bound on E L/N is H_{N−1}, slightly sharper than 1 + ln N.

(b) Any rule that only selects among the current maximal elements has L ≤ N − 1. This is EXACT.

(c) The full DGC + Bell class is NOT covered at finite N. That class is Rideout-Sorkin plus the Varadarajan-Rideout (VR) towers that appear when probabilities vanish. Towers are excluded only asymptotically, through Brightwell-Georgiou (BG) Thm 1.5 plus the ordinal-sum lemma, with n0 not explicit. For towers, ε must be below about 2.6e-4, not 3e-4.

(d) Not excluded:
- label-invariant Markovian rules without Bell causality (the reading's own example class);
- structure-aware, non-Markovian, quantum and action-weighted rules.

The lane answer is therefore "not by exchangeable, frontier or (asymptotically) CSG-tower growth". It is not "records forming cannot produce the event set".

**Issues:** 1. The report says or implies that DGC + Bell gives CSG and that CSG satisfies H-exch (§3, §1 "the class").
- With vanishing probabilities, DGC + Bell gives VR turtle towers: each later turtle lies above all earlier ones (VR §IV, read in lit/vr2006).
- Towers are not exchangeable and they break Theorem L's bound. Two dust turtles (53 ⊕ 947) at N = 1000 have r = 0.1005 and L/N = 50.2.
- The tower dust(48) ⊕ TP(952, p = 0.0027) at N = 1000 gives r = 0.0985, L/N = 17.3, H = 10.7, n1/n0 = 0.52, n2/n0 = 0.32. The 4D values are 0.100, 17.8, 9.9, 0.345 and about 0.24. So it matches the very link statistic the no-go rests on.
- That tower is still rejected, but by nmin/N (0.048 against 0.148) and by the 4-point densities (2+2 = 0.00009 and 3+1 = 0.00010, against 0.0048 and 0.0050). Theorem L does not reject it. The worker never ran towers numerically.
- So for the DGC + Bell class the no-go is asymptotic only: BG with non-explicit n0.

2. BG route for towers, an arithmetic slip.
- With Δ ≤ 1.5εN², the 4-point bound becomes 18ε, not 12ε.
- ε = 3e-4 then gives 0.0054, which is above both 4D values. ε must be below about 2.6e-4.
- This is easy to fix, because the result is asymptotic anyway.

3. Wrong class identification in the pre-registration.
- PREREG §4 identifies "Markovian label-invariant" with Rideout-Sorkin CSG. CSG also needs Bell causality.
- The reading's example class, label-invariant without Bell, is therefore not established. The worker concedes this (§9.5).
- So FAIL holds only if the referee accepts H-exch ∪ H-front (∪ DGC+Bell asymptotically) as the "stated hypotheses". It should be worded as a bounded no-go.

4. Notation and minor points.
- "7.55 ± 0.19" (Table 3) is a standard error; Table 1's "±" values are standard deviations.
- My independent rerun gives 4D L/N = 7.72 ± 0.07 (SE, 64 reps) at N = 300. At N = 250 it gives 6.78 ± 0.10 against H_249 = 6.10, so the exclusion already holds there. "N ≥ 300" is conservative.
- The local "~3×10⁷ elements" arithmetic extrapolates the 4D degree law. The coefficient of √N rises from 0.56 at N = 1000 to 0.72 at N = 8000, so the result is ARGUED, as the worker flagged.
- FRONT0 allows an empty selection, whereas PREREG's RF-front required at least one ancestor. The RF-tree control was not run. The frontier lemma covers both, so this does no harm.

5. Checked and found correct, with no refutation:
- Theorem L, step by step: the up-set characterisation; J − J(a−1) = ℓ; ℓ non-increasing by exchangeability; ℓ/J ≤ 1/a; the compensator sum ≤ H_{|↑i|}; the Chernoff tail and union bound, which are conservative.
- The frontier lemma.
- The ordinal-sum lemma, and VR cross-turtle comparability. VR states that each new element is to the future of all previous turtles; turtle length is fixed when the turtle starts.
- BG Thm 1.5 is uniform in t (lit text lines 175-181), and the 12ε step is in the Thm 1.6 proof.

**Re-runs:** All runs used OMP_NUM_THREADS=2, each under 2 minutes. Scripts are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/F/verify/.

- **v1_4d_links.py**: an independent 4D diamond sampler (ball rejection, a different method from the worker's) with a dense-matrix link count, separate from fcore.
  - N = 250: L/N = 6.78 ± 0.10
  - N = 300: 7.72 ± 0.07
  - N = 1000: 18.07 ± 0.12
  - N = 2000: 27.65 ± 0.46
  - r ≈ 0.100 throughout; n1/n0 = 0.27 / 0.29 / 0.35 / 0.37.
- **v1b_gen_compare.py**: my sampler against a re-implementation of the worker's cube sampler, 48 reps each at N = 1000. L/N = 17.87 ± 0.11 against 17.73 ± 0.10, H = 9.90 against 9.90. This agrees with the worker's F1 values (17.75 ± 0.11, H = 9.81).
- **v2_theoremL_adversarial.py**: exact rational enumeration of all growth paths at N = 5 (24 rules) and N = 6 (8 rules). The exchangeable rules have size laws given by an arbitrary hash of the labelled history, either dense or concentrated on 1-2 sizes. E X_i ≤ E H_{|↑i|} held for every label, with the worst ratio exactly 1.0, attained trivially at label N−2. Two non-exchangeable controls (min-or-dust, oldest) violate the bound, e.g. E X_0 = 2.5 against 1.595. So the hypothesis is necessary and the test can fail.
- **v3_vr_tower.py and v3b_tower_fourpoint.py**: VR towers at N = 1000.
  - Two dust turtles: L/N = 50.2 at r = 0.1005.
  - dust(m) ⊕ TP tuned to r = 0.1: L/N rises from 2.9 (m = 0) to 20.7 (m = 50).
  - dust(48) ⊕ TP(952): r = 0.0985, L/N = 17.3, H = 10.7, n1/n0 = 0.52, nmin/N = 0.048, 2+2 = 9e-5, 3+1 = 1e-4.
- **Reading, as untrusted data**: BG 2010 Thm 1.5 statement and proofs of 1.5 and 1.6 (contlim.txt lines 40-230 and 1570-1660); VR §IV and conclusions (vr.txt 574-780).
- The worker's scripts were not re-executed. The checks above are independent re-implementations.
