# Check: `library/lfi-he.md` (H-E, stopped joint kernel SJ)

**Verdict: FIX.**

The proved steps hold. The ported citations read as stated. SJ is the right supplier for IN1 (16), with one over-specified clause.
The (c) stop is not yet earned. Route 2 does not fail where the note says. With the ported bound `||K|| <= C_w`, it reduces to the pivot problem of Route 1. So the three routes are not three distinct failures.
Route 1's failure locus is stated, not shown. No prescribing constraint is exhibited for the case where it stalls.

Scope. One line-by-line reading of the note (651 lines) at clone HEAD `04e7c612f`. I read prior/lfi.md rows H-E and H-C-KEPT, in1.md 150-220, gates/in1-gate.md, and the Y, SA and I lines cited below. Research text. Not an audit. Grants no status. No computation was used as a proof step.

## 1. Findings

**F1. SJ against IN1 (16) and the source envelope. Note 153-184. CONFIRMED, with one over-specified clause.**
- `sup_{zeta}` with fixed inner data is exactly what IN1 (16) needs. It is also what the source needs: Y 76988-76991 (`sup_{xi_in} int g dmu° <= e^{C_5 V°}`), Y 77011-77013 ("independent of all inner histories and all their variables"), and SA 18805-18823.
- An integrated-inner version would not do. Inner island measures are arbitrary positive Borel measures, so the bound must hold for all of them. That is equivalent to the pointwise sup. Note 229-232 is right.
- `sup_W` at a prescribed outgoing read matches Y 75140-75147 and 76052-76061. The drop-out keeps the field fixed, and spectators stay in the joint bound.
- SJ is not stronger in its p-uniformity. Y 76970-76974 fixes the reference maps before the supremum.
- **Over-specified:** SJ requires that `dnu_omega` be "a product on the genuinely free coordinates" (165). Y 74979-74984 says a direct nonnegative Borel `g` with the integral bound is enough. The reference measure must be fixed by record, geometry and branch, and independent of p (Y 76970-76974). It need not be a product.
- Repair: state SJ with any p-independent reference measure fixed by the record. Keep the product case as the expected realization.
- hi:pair-sup-envelope (Y 73362-73371) handles only the `V_X` part. SJ is the reference part. The note keeps them apart correctly (118-121, 182-184).

**F2. Reduction (2) and the scalar prices (3). Note 80-151. CONFIRMED.**
- `|z|^{-1} <= C theta^{3/2}` is at Y 74765.
- The per-length pivot convention `|L^{12} det m_c - 1| <= 1/2` is at Y 74794. It gives `J_* = 2L^{12}`, stated at **Y 75028**, outside the cited range 74698-74891. Y 76080 and 76513 use `eL^{12}`. Either constant works.
- The "no double count" remark is Y 74819-74821.
- SA 18816-18823 removes the integral excess after the outer integration, as cited.
- Repair: add Y 75028 to the citation.

**F3. Route 1 ports. Note 194-259. CONFIRMED.**
- Y 75217-75348: the middle-link degree argument holds on every branch. It gives `det >= L^{-9}` and kernel mass `2L^9`, or `2L^9+1` with the fallback version.
- Y 75591-75676: disjoint boxes.
- Y 76191-76230: the alternate pivot, `D_a f = L^{-3}I + E`, `||E|| <= L^{-3}/2`.
- Y 76232-76245: the straight-path fallback.
- Y 76373-76402: price (4). The source prints `(2L^9)^{N_raw}` and `prod int m_y`. The note correctly flags that this integrates the inner data.
- Y 134995-135018: the two-level case. It needs a restored box, an alternate in the same first stock, and the restored cutoff giving small curvature.
- Y 76180-76184 assumes the joint chart. Y 76304-76306 asks for a new joint read when the closure leaves the stock.

**F4. Route 1 failure locus. Note 261-288. UNCLEAR.**
- The source names the exact hole: "A tree-fixed alternative or the intermediate logarithmic branch outside the regular box requires its own chart" (**Y 76230-76231**). The note does not cite it. Its four-way alternative is less precise.
- The note says the stall occurs at a late open stop before restoration (269-273). It never shows which later constraint prescribes a fresh-box output there as a spectator.
- Y 76012-76046 argues that later tests and gauge reads miss the fresh box. Only outgoing averages and boundary weights read it. Boundary weights are test-only, so their slot is a graph value (Y 76277-76290).
- If no spectator is prescribed, the second level is the composed case. Y 76488-76494 then supplies Haar domination of the middle bond from the lower joint bound. No conflict arises.
- Repair: exhibit the prescribing constraint, or replace "stalls" by the precise open case: a prescribed middle link, an alternate on the intermediate or tree-fixed branch, and no restored cutoff.

**F5. Route 2 calculation (6)-(12). Note 297-389. CONFIRMED.**
- The block determinant is correct, and so is the density maximum `(2pi)^{-(r+m)/2} det Gamma^{-1/2}`.
- In (9), `S = epsilon^2` and the density is (10). The Jacobian is `1/epsilon`.
- The right inverse has second component `1/epsilon`.
- (12) is correct: `C(T_0 - R_C C T_0) = 0`.

**F6. Route 2 failure statement. Note 341-343, 390-408. MISMATCH.**
- "A gap `K >= gamma I` … supplies no lower bound on (7)" is true. It is not the whole picture. §7 ports `||K_{j,D}|| <= C_w` (note 572; Y 76517-76518).
- An upper bound on K is what controls S. Write `Sigma >= C_w^{-1}` in the level's scaled units.
- Then `t^T S t = min_y (B^T t - C^T y)^T Sigma (B^T t - C^T y)`. This is at least `C_w^{-1} |P_{ker C} B^T t|^2`.
- Let J be any set of coordinates read by no spectator row. Then `span{e_j : j in J}` lies in `ker C`. Hence `S >= C_w^{-1} B_J B_J^T`.
- In (9), `K = I` and `C_w = 1`. The loss is purely geometric: `dist(B, span C) = epsilon`. It is not a coercivity loss.
- So Route 2 reduces exactly to the linear form of Route 1's question. One needs exclusive coordinates per row with a lower bound on `B_J B_J^T`. On the regular charts this is diagonal. The middle link of a level-i row is read by no other row (Y 76135-76136). A face alternate is read only by its own row (Y 76219-76220). Each gives `L^{-3}`, or `L^{-6}` through one composition.
- Route 2 is therefore not a distinct failure. It fails only where Route 1's pivot matching fails.
- Repair: replace 390-408 by this reduction. Name Route 2's open step as an injective assignment of rows to exclusive coordinates, which is combinatorial. Or find a different third route.

**F7. Route 3. Note 413-501. CONFIRMED.**
- (13) is Y 75803-75812.
- (14) is correct for exact graphs.
- The SU(2) example is correct: `a = r+h/2`, `|e^{ih}-1| = 2 sin(h/2) <= h`, and `r+h/2 < 2r`.
- (15) holds. The band volume `C r^2 h` follows from `sin^2` on an interval of length `2h` and radius `<= 3r/2`. It agrees with Y 134900-134903 (`C theta delta^3`, with `theta = h/delta`).
- The predicate citation Y 134875-134899 is correct.
- The return to SJ for constrained slots (486-491) is correct. This route is distinct and fails where stated.

**F8. §7, kept form in its original masks. Note 503-598. CONFIRMED.**
- The sets I and E are at Y 63278-63286. Carriage is at Y 63240-63259. The survival condition is at Y 63469-63473.
- (17) is Y 63537-63546, including the `r_P` condition. (18) and the `gamma/4` remainder are Y 63549-63556.
- (19) is a correct norm bound. The tube smallness is Y 76517-76530.
- One small step is unproved: keeping `kappa_keep > 0` on a smaller fraction of the complex chart (570). It needs one Schwarz-lemma line: holomorphic coefficients bounded by `C_w`, and a real gap `gamma/4`. Repair: add that line.

**F9. Remaining citations. CONFIRMED.**
- Y 73357-73371, 74941-74977, 75466-75473 (the tree slice changes the raw law), 75998-76014, 76466-76486 (cancellation before the new row), 76716-76757, 76968-77031 and 80320-80360 ("nor a common chart for an arbitrary history").
- I 157053-157060, (h5): integrating `V_k` removes the constraint.

## 2. Routes that may close SJ

**R-A. Finite classification of prescription types (the most promising).**
At fixed L and M, the backward closure of a row stays in two order-(q-u) blocks (Y 76308-76322). So only finitely many geometric patterns exist, each recording which slots of a double block are prescribed and by which kind of constraint.
Classify every constraint that can prescribe a generated slot. Use the remade-row ownership, Y 76012-76046, Y 76263-76306 and Y 76414-76426.
Show that each pattern is one of these:
- (i) test-only, so the slot is a graph value;
- (ii) the first outgoing stock, using the middle link (Y 134982-134993);
- (iii) the two-level restored-box case (Y 134995-135018);
- (iv) the composed case (Y 76488-76494);
- (v) a deterministic relation.

If the classification closes, SJ follows from ported results. The only remaining condition is a Hall matching of rows to exclusive coordinates (F6), which is finite at fixed L.
If it fails, the failing pattern is an explicit candidate counterexample history.

**R-B. Endpoint-gauge pivot for conflicts on the intermediate branch.**
Take a conflicted row c, whose middle link z is prescribed. Let x be an endpoint site of c with these properties:
- x is not incident to z or to any fixed exterior slot;
- every surviving weight is invariant under the site gauge at x, as on first-class components (I 157076, (h9));
- the field at x is not on a tree slice (compare Y 75466-75473).

Fix one link at x. Then Haar becomes (slice) × (g), and `W_c = g F_c(slice)`. The Jacobian in g is one, on every branch, by covariance (Y 75339-75346).
Solve the other rows at x by their middle links after g. This is triangular.
This gives one extra pivot per site. It closes SJ when each connected part of the conflict graph has no more conflicted rows than sites (a pseudoforest).
Not checked: gauge invariance of background-frame tests in prepared regions.

**R-C (Schur / Balaban block-diagonal).** This is F6. On regular charts it holds under the same matching as R-A. It adds nothing on the intermediate branch.

Checked line by line by Claude (Opus 5.5).
