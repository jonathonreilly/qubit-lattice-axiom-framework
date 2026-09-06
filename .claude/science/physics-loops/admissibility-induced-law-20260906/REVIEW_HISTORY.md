# Review history — admissibility-induced-law-20260906

## block 01 — supervisor control computation (before the primary launched, 2026-09-06)
`specs/supervisor_control_verify_core.py` (exact rationals + sympy): static law's full conditionals equal the product rule on path3/star4/cycle4 (weights 3,1,2); formation law equals the static law for exactly the orders with at most one recorded neighbor at every site (path3 4/6, star4 12/24, cycle4 0/24); distinct formation laws 2/5/4; two-neighbor normalizer orbit values p^2+q^2+4r^2, 2pq+4r^2, 2pr+2qr+2r^2 with differences (p-q)^2, 2(p-r)(q-r), (p-r)^2+(q-r)^2; one-neighbor normalizer p+q+4r; sum-rule Brook cycle at lambda=1/4 gives 27/25; product-rule Brook cycles all exactly 1 (symbolic).

## block 01 — physics panel (four Opus lenses on the dossier; synthesis by the supervisor)
(to be recorded after the lenses deliver)

### Panel synthesis (supervisor, 2026-09-06T18:15Z; lenses L1 rigor, L2 foundations, L3 strategy, L4 refuter — all Opus 5, each with its own exact computations; files in `specs/panel_*.md`; the supervisor's own Fable thread = the two control scripts and the proof below)

Verdict: BUILD WITH CHANGES, unanimous. Every lens independently reproduced the supervisor's control numbers (path3 4/6, star4 12/24, cycle4 0/24; the three `Z_2` differences; the one-neighbor normalizer `p+q+4r`; the formation identity pointwise; the sum-rule Brook defect of order `λ²`). No lens refuted a numbered claim.

Defects found and their disposition:
- D1 (L1 D7, L3 D1, L4 §5.2 — load-bearing): the inference from one non-constant normalizer to `μ_σ ≠ μ` skipped the product-level lemma. CLOSED by the supervisor's single-site variation lemma (GOAL.md Theorem B, B2 ⇒), valid for every arity; verified exactly for `j = 1,2,3` (`specs/supervisor_control_verify_lemma.py`) and on eight cube orders. L1's ANOVA argument covers arity ≤ 2 and is superseded.
- D2 (L4 §5.1 — fatal to the axiom-level sentence): a rule can vary on `M_2(C)` and be constant on the six-point menu (`f(x) = 1 + x²(1−x²)`). ACCEPTED: the hypothesis is stated on the menu; the reading "variation clause restricted to the declared menu" is named; the witness is executed as the boundary.
- D3 (L2, L3 D2): "varies with" forbidding the constant rule is a reading. ACCEPTED: named reading (B4).
- D4 (L2 §2, L3 D3): records-only is one of three readings, not "the natural reading". ACCEPTED: three readings named; the absence-factor readings computed (L2's sympy solve; L4's rank-6 closure); the marginal reading computed as window-dependent (`219/866` vs `1/4`, supervisor).
- D5 (L2 D3, L3 D4, L1 D9): the Gaussian remark conflated precision/covariance, conditional/marginal, and `herm(Q^{-1})` vs `(herm Q)^{-1}`. ACCEPTED: rewritten as a three-sentence cross-carrier analogy with a real-symmetric positive-definite hypothesis and "conditional-then-marginal block"; no bearing on the 2026-08-26 gate claimed.
- D6 (L3 D0, V-gate): the static half is the landed binary compatibility note with a six-value menu. ACCEPTED: Theorem A cites and generalizes; Hammersley–Clifford's converse is referenced, not used; the positivity counterexample dropped; the partition identity demoted to a runner consistency line.
- D7 (L2 §7, L3 D6): the block does not address the infinite lattice and must say it does not fire the parked bridge's wake condition. ACCEPTED verbatim; the "specification / action, not a law" paragraph added as a remark; the DLR block queued.
- D8 (L1 D1–D4, L4 §5.4–5.8): boundary convention, positivity as premise, pair-weight symmetry via the edge-flip element, the gauge class, the sum rule's degree dependence and `|λ| < 1/deg`. ACCEPTED, all executed or stated.
- D9 (L4 §5.3): "distinct orders give distinct laws" is false. ACCEPTED: census reported (P4 added), sentence banned.
- L2 §1 "the order is physical" is an unlicensed claim. ACCEPTED: banned; layman's paragraph reworded.
- L1 §7 (e) order-independence theorem: the executed census already shows order dependence on the plaquette; a general theorem is not claimed.

Ranking (all four lenses): this block, amended, first; the record-matter formation-law lane second or third; the U(1) time-selection fork next; the gravity queue last. L3's V1–V5 reading: passes as upstream support/falsifier, not closure; T2 is the headline.

Misses by the cheaper tier, recorded per the worker-tier rule: none of the four lenses found the general product-level proof (L1 reached arity ≤ 2; L4 searched 40,320 cube orders for a counterexample); the supervisor's Fable thread supplied it. No lens missed a defect the supervisor had found.
