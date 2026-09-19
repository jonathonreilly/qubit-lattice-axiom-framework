# lightcone-sixaxis-order, attempt 2 (worker w-macbookpro90c72-j848f, model grok-4.6)

Independent of a3 (cube Peierls, 6+7 pairing). Route: C4 contour ratios for `π∝∏ Z`; 6-nn pairing without self.

## (1) The statement attempted

**(a)** Reversibility of six-axis `(p,q,r)` holds for any symmetric `W` on a symmetric neighbourhood; the site itself need **not** be included (6-nn pairing CHECKED on L=2). Self-loop pairing is the trivial bilinear `s·s'`.

**(b)** On C4, sync `π` at `(p,1,2)`: one orthogonal defect has weight ratio `144/169<1`, antipodal `121/169<1`, both decreasing at `p=5,10`. This is a contour cost, not yet a Peierls bound on `Z^3` (ASSUMED: a chessboard/Peierls on `Z^3` would use these local ratios). Six stationary aligned laws are plausible for large `p`; the C4 ratios already favour alignment at `p=3`.

**(c)** Static six-axis threshold (block 17, under repair) is not recomputed. Executed formation thresholds `10.5–11` are far above `p=3` where C4 already likes alignment.

**(d)** For a reversible automaton the six aligned configurations are candidate *stationary* laws, not transients; “memory of the initial plane” is convergence to the corresponding ergodic component.

## (2) Steps

**Step 1 — C4 ratios (CHECKED as E1).** `Z(a,b)=∑_s W(s,a)W(s,b)`; `π(cfg)∝∏_i Z(s_{i-1},s_{i+1})`.

**Step 2 — 6-nn pairing (CHECKED as E2).**

## (3) First failing step

A full Peierls bound on `Z^3` with an explicit `p_c` on `(p,1,2)` is not proved (C4 is too small to control contours).

## (4) What would finish it

A chessboard estimate or contour counting on `Z^3` using the 6-nn star potential, with a proved `p_c`.
