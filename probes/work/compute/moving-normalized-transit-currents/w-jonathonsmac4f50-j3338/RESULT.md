# Normalized transit: stationary law, currents, cycles — run 1

Worker `w-jonathonsmac4f50-j3338`, model `claude-opus-5-5`. Block 39 was written by the same model family (Claude). The log is `logs/probes/C:moving-normalized-transit-currents:a1/w-jonathonsmac4f50-j3338__651e26cf__20260925T044050Z.*`.

## As landed on main

Block 39 (#8530), T3 defines **normalized transit**: a bond with exactly one occupied end is visited, and the record (content a) at x moves to the empty y with probability `K(a | records around y, x excluded)`. The scale c cancels. The landed note gives one four-move cycle with products 1/2592 and 1/2376, as an example at (3,1,2) on the 2×3 window. Nothing withdrawn is used.

## Method

**Exact.**
- Rates are rational.
- The stationary law comes from an exact rational solve of the chain **lumped by the window's symmetry group**. The chain commutes with the grid automorphisms, so π is constant on orbits; the group is D2 on 2×3 and D4 on 3×3.
- Currents `J(s→t) = π(s)q(s,t) − π(t)q(t,s)` are exact.
- Detailed-balance tests are exact.

**Floating point.**
- Greedy cycle decompositions of the current, in two orders.
- Scans over the weights.

**Check.** Block 39's cycle `(+z,+z,−z,+x,_,_)`, moves 3→4 and 2→5, gives products **1/2592** and **1/2376** exactly (PASS).

## (1) Stationary laws (exact)

| window, contents, weights | states / orbits | π from … to (uniform) | TV from static law | TV from uniform | record–record bonds: stationary / random / static |
|---|---|---|---|---|---|
| 2×3, 2 vac, six-axis (+z,+z,−z,+x), (3,1,2) | 180 / 46 | 0.00170 … 0.01214 (0.00556) | 0.1647 | 0.1988 | 2.7408 / 2.8 / 3.0292 |
| 2×3, 2 vac, two-valued (+,+,−,−), (3,1) | 90 / 27 | 477/683468 … 32175/683468 (1/90) | 0.1461 | 0.3324 | 939081/341734 = 2.7480 / 2.8 / 2.9942 |
| 3×3, 2 vac, two-valued (+×4,−×3) | 1260 / 174 | 1.30e−6 … 0.00752 | 0.2468 | 0.5411 | 6.9205 / 7 / 7.3551 |
| 3×3, 3 vac, two-valued (+×3,−×3) | 1680 / 228 | 2.88e−6 … 0.00606 | 0.2380 | 0.4469 | 4.8913 / 5 / 5.4093 |
| 3×3, 2 vac, six-axis (+z×4,−z×2,+x) | 3780 / 492 | 4.19e−6 … 0.00214 | 0.2577 | 0.4071 | 6.9365 / 7 / 7.4216 |
| 3×3, 3 vac, six-axis (+z×3,−z×2,+x) | 5040 / 648 | 7.37e−6 … 0.00118 | 0.2627 | 0.3438 | 4.8910 / 5 / 5.5038 |

**Link to block 39's numbers.** Block 39's control numbers (total variation 0.146 from the static law, 2×2 clump 0.1195) are those of the **two-valued** (+,+,−,−) window at (3,1): here 0.146127 and 20427/170867 = 0.11955. The six-axis (+z,+z,−z,+x) window gives 0.1647 and 0.1097.

The exact rationals of the larger windows have denominators of 136–1151 digits. They are summarized, not printed.

## (2) Currents and the cycles that carry them

**Decomposition-free comparison.** The circulation of the exact current around each elementary four-move cycle, averaged per cycle:

| window | "two records hop out and back" squares (block 39's type): count, mean \|Γ\| | "two equal records exchange around a plaquette through the two vacancies": count, mean \|Γ\| | ratio |
|---|---|---|---|
| 2×3 six-axis | 132, 4.41e−5 | 8, 4.86e−5 | 1.1 |
| 2×3 two-valued | 66, 5.5e−4 | 8, 2.53e−3 | 4.6 |
| 3×3 2 vac two-valued | 1540, 6.01e−5 | 120, 1.15e−4 | 1.9 |
| 3×3 3 vac two-valued | 4400, 4.1e−5 | 320, 8.7e−5 | 2.1 |
| 3×3 2 vac six-axis | 4620, 2.02e−6 | 280, 3.27e−6 | 1.6 |
| 3×3 3 vac six-axis | 13200, 1.35e−6 | 640, 2.54e−6 | 1.9 |

**Reading.** Per elementary cycle, the current circulates **more strongly around two records exchanging places through the vacancies**, by 1.1–4.6×. This bears out the task's expectation.

**Greedy decompositions** (share of Σ current × length carried by cycles in which record identities are exchanged; the two orders are largest-current first and smallest-current first):

| window | exchange share (largest first / smallest first) | two-record cycles | leading cycle types (largest first) |
|---|---|---|---|
| 2×3 six-axis | 0.118 / 0.220 | 0.346 | (4 moves, 2 records, no exchange) 0.318; (6, 3, no) 0.297 |
| 2×3 two-valued | 0.103 / **0.000** | 0.707 | (4, 2, no) 0.707; (8, 4, no) 0.190 |
| 3×3 2 vac two-valued | 0.570 / 0.615 | 0.353 | (4, 2, yes) 0.178; (4, 2, no) 0.176 |
| 3×3 3 vac two-valued | 0.537 / 0.513 | 0.183 | (8, 4, no) 0.120; (4, 2, no) 0.116 |
| 3×3 2 vac six-axis | 0.541 / 0.556 | 0.203 | (4, 2, no) 0.162; (6, 3, no) 0.084 |
| 3×3 3 vac six-axis | 0.421 / 0.423 | 0.145 | (4, 2, no) 0.126; (6, 3, no) 0.099 |

**Caveat.** A cycle decomposition of a current is not unique. On the 2×3 two-valued window the exchange share moves from 0.10 to 0.00 with the order. The aggregate shares are therefore descriptive only; the per-cycle circulations above are the decomposition-free statement.

On 3×3 about half of the aggregate is in long "sliding" cycles that move 5–7 records and permute them.

## (3) One vacancy

| window, contents | states (orbits) | detailed balance, exact |
|---|---|---|
| 2×3 six-axis (+z,+z,−z,+x,+y) | 360 (90) | holds on all 840 edges: **reversible** |
| 2×3 two-valued (+×4,−) | 30 (8) | reversible |
| 2×4 two-valued (+×4,−×3) | 280 (70) | reversible |
| 2×4 six-axis (+z×4,−z,+x,+y) | 1680 (420) | reversible |
| **3×3 two-valued (+×5,−×3)** | 504 (72) | **fails on 1248 of 1344 edges** |
| **3×3 six-axis (+z×5,−z,+x,+y)** | 3024 (378) | **fails on 7872 of 8064 edges** |

**Proof of irreversibility on 3×3.** The hole makes a 14-move cycle, `+.-/+-+/-++ → … → +.-/+-+/-++` (in the log). Its Kolmogorov products are `243/6553600000` one way and `81/1835008000` the other, a ratio of **21/25**. So no law is reversible for one vacancy on the 3×3 window. Single plaquette loops and loops around the eight-site ring pass the test, so the failure needs a composite hole walk.

**Closed form.** On the ladders, π = μ·Φ with `Φ(ζ')/Φ(ζ) = Y_x^{(y)}/Y_y^{(x)}` for the move x → y. Here `Y_u^{(v)}` is the rule's normalizer at u from its recorded neighbours other than v. This is a well-defined potential exactly when the chain is reversible.

No **local** closed form was found. The candidates tested on 2×3 and 2×4, all failing: the hole's normalizer; products of the neighbours' normalizers; products of the rule's probabilities of the neighbours' contents; and combinations of these. Scratch tests, not in run.py: states with identical hole neighbourhoods have different π/μ.

**Answer to (3).** Reversibility is a property of these ladders, not of normalized transit with one vacancy.

## (4) Clumping against random placement

**2×3, two vacancies, 2×2-clump probability** (random 2/15 = 0.1333):

| two-valued p/q | 0.05 | 0.10 | 0.20 | 0.32 | 0.50 | 0.80 | 1 | 1.25 | 2 | 3 | 5 | 10 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| clump | 0.1059 | 0.1315 | **0.1496** | **0.1548** | **0.1515** | **0.1397** | 0.1333 | 0.1282 | 0.1229 | 0.1195 | 0.1088 | 0.0837 | 0.0437 |

**Six-axis (+z,+z,−z,+x):**
- (3,1,2) 0.1097; **(1,3,2) 0.1382**; (2,3,1) 0.1225; (3,2,1) 0.1176; (1,2,3) 0.1058; (2,1,3) 0.0852; (1,1,3) 0.0726; (3,3,1) 0.1108; (5,1,1) 0.1017; (1,5,1) 0.1087; (1,1,5) 0.0427; (1,1,1) 0.1333.
- 60 random weight sets: 21 lie above random, from 0.0088 to 0.1548.

**3×3, mean record–record bonds** (random 7, resp. 5):
- two vacancies: 6.976, **7.015**, 7, 6.953, 6.921, 6.884, 6.853, 6.830 at p/q = 0.2, 0.5, 1, 2, 3, 5, 10, 30;
- three vacancies: **5.053, 5.049**, 5, 4.933, 4.891, 4.834, 4.736, 4.512.

**Answer to (4).** No. The law clumps less than random when like neighbours are favoured. It clumps **more** when unlike neighbours are favoured: two-valued p/q ≈ 0.12–0.9, six-axis (1,3,2), and 3×3 at p/q = 0.2–0.5.

## Verdict

There is no HIT. The expectation (currents circulate around pairs of records exchanging places through the vacancies) is borne out per elementary cycle, and that statement does not depend on a decomposition. The aggregate shares depend on the decomposition.

Two further findings:
- The one-vacancy chain is reversible only on the ladders (2×3, 2×4) and **not** on the 3×3 window, shown by an exact 14-move cycle with product ratio 21/25.
- The law clumps less than random only when like neighbours are favoured.
