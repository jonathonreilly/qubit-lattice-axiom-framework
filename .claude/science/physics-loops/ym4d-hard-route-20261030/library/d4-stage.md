# d4-stage: stage margins and transported domains
Provenance: Codex (GPT-6 family; assigned effort max; runtime variant and effort not exposed); checkout `313310d007bc5903fecff474fc508cc11eb2cd4f`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit; grants no status.

## 1. Sources and target

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's constructions.
Balaban supplies the stage and background method.
This note addresses queue row 240.
It reads rows 226, 236 and 239, `d4-budget.md`, `loc-4.md` §5, and `r-inv.md`'s Result.

The [pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex) requires the (R5) tower to exist in its continuation domain.
Its L6155–6157 calls stage inclusions “analytic inclusion hypotheses”.
Its L6122–6148 defines the (R22) radii.
Its L17610–17630 sketches the real stage comparison.
The lead's row 240 classifies the requested inclusion as assumed.

The target is admission on the larger input core, uniformly over earlier parameters and preceding structures.
Each comparison must use one target chart and the actual changed determining sequence.
Spatial naturality from `r-inv.md` does not estimate this transport.
Equations (5)–(7) of `d4-budget.md` require transported increment bounds as hypotheses.

## 2. What the stage margins pay

Fix a point, a level \(m\), and one chart.
Keep its layer assignment and lift fixed in this calculation.
Write \(N=\mathsf N_t\ge1\) and \(g=\mathsf g_t(m)\).
Suppose a stage records new levels \(E_n\), without deleting earlier marks.
Direct subtraction of (R22) gives
\[
 d_n(m):=c_n(m)-c_{n+1}(m)
 =\frac{g}{2N}+\beta_R\sum_{l\in E_n}2^{-|m-l|}.                 \tag{1}
\]
If the recorded levels are distinct, then
\[
 \sum_{n=0}^{N-1}d_n(m)\le \frac g2+3\beta_R,
 \qquad
 \sum_{l\ge0}2^{-|m-l|}
 \le1+2\sum_{q\ge1}2^{-q}=3.                                  \tag{2}
\]
Thus the stage count does not itself exhaust these coefficients.
Also \(c_\sigma\ge1-\beta_s-3\beta_R\), when its recorded levels form a set as specified.

Here is the exact local expenditure test.
Let \(r_m\) include the fixed lift and the clause's units.
Start with that clause below \(c_{n+1}(m)r_m\).
If a transported clause changes by less than \(d_n(m)r_m/2\), its new value fits the earlier radius.
Indeed, its norm is less than
\[
 c_{n+1}(m)r_m+d_n(m)r_m/2
 =c_n(m)r_m-d_n(m)r_m/2.                                      \tag{3}
\]
This leaves half the coefficient gap unused.

A response bound \(Cr_mu_l\sqrt{1+|m-l|}e^{-D|m-l|}\) fits half a new level's margin if
\(D\ge\log4\) and \(Cu_l<\beta_R/2\).
For \(q\ge0\), \(q+1\le4^q\), so \(\sqrt{1+q}e^{-Dq}\le2^{-q}\).
This proves the comparison by hand.
For a phase-only stage, the required allowance is instead \(g r_m/(4N)\).
A bound centred at the remade level cannot silently replace that smaller allowance.

These calculations concern coefficients in one chart.
If the layer, lift, real reference, or determining sequence changes, (3) requires their actual transported radii.
Equation (2) does not bound the transported field or the continuation datum.

## 3. The continuation comparison that is still missing

Fix a preceding chart \(\tau\), its real reference \(U_\tau\), and one tower \(\mathcal B_\tau\).
Write \(w_{n,\tau}\) for the actual prefix expressed in this chart, when that expression exists.
Its (R5) datum is
\[
 b_{n,\tau}=\frac1i\log\!\left[
 M_{\mathcal B_\tau}(e^{i\eta w_{n,\tau}}U_\tau)
 M_{\mathcal B_\tau}(U_\tau)^{-1}\right].                       \tag{4}
\]
The supremum below must include the larger input core and every retained earlier parameter.
For a target continuation ball of radius \(r_{B,\tau}\), the sufficient budget is
\[
 \sup\|b_{0,\tau}\|\le r_{B,\tau}-\epsilon_\tau,
 \qquad
 \sum_n\sup\|b_{n+1,\tau}-b_{n,\tau}\|<\epsilon_\tau.           \tag{5}
\]
The triangle inequality proves admission of every prefix under (5).
The (R22) coefficient difference is not a bound for either term in (5).
In particular, (R22) does not assign a distance to the boundary of the (R5) continuation domain.

For a single-layer tower of depth \(d\le p\), put \(\|w\|_*:=L^{d-p}\|w\|_\infty\).
Retain the real-regularity and averaging hypotheses of `c1-repr.md` §8.
Its endpoint-factor correction gives \(\|b_\tau(w)\|\le C_A\|w\|_*\) on a fixed ball \(\|w\|_*<R\).
Choose \(C_AR<r_{B,\tau}\).
Assume the potentials are defined on the common larger source before concluding tower admission.
If
\[
 \sup\|w_{0,\tau}\|_*<R/4,
 \qquad E_\tau:=\sum_n\sup\|w_{n+1,\tau}-w_{n,\tau}\|_*<R/4,
                                                                    \tag{6}
\]
then every prefix has norm below \(R/2\).
Cauchy's estimate on discs of radius \(R/2\) gives \(\|Db_\tau\|\le2C_A\) there.
Integrating along each segment gives \(\sum_n\sup\|\Delta b_{n,\tau}\|\le2C_AE_\tau<r_{B,\tau}/2\).
Also \(\sup\|b_{0,\tau}\|<r_{B,\tau}/4\).
Thus (5) holds with \(\epsilon_\tau=r_{B,\tau}/2\).
This verifies the fixed-chart continuation mechanism used in `d4-budget.md` (5)–(7).

It does not establish (6) for a stage.
`ld-decoupled.md` (5)–(6) bounds a response on one admitted sequence.
`wf-room-2.md` Theorem L fixes its real reference and requires memberwise tower containment.
The removed-map comparison in `o1-decoupled.md` §3.1 assumes its common coordinates and transported-pair bounds.
None of these estimates alone bounds \(w_{n+1,\tau}-w_{n,\tau}\) for the full earlier composition.

A required instance is stage \(0\to1\) of an eligible component that later drops out at level \(t\).
Its first remade index in (R21) is \(l=t-\mathsf N_t+1\).
The comparison must use the old chart and the sequence after that shell has been prepared.
It must include every earlier parameter and both erosion rules.
SA L17610–17630 controls real stage tests.
SA L17904–17930 sketches the complex interpolation by invoking hereditary-domain estimates.
Neither passage supplies (5) for these transported data.
A first-exit proof would need uniform estimates in that common chart before the possible exit.
No such stage estimate is proved here.

## 4. The other domains need their own expenditure bounds

The assigned current cannot be replaced by the current of the complex field.
SA (R8) makes that distinction explicit.
The corrected `wf-room-2-gate.md` (6.4) bounds its increment by the response norm on an admitted fixed sequence.
Using it at every stage still requires the transported estimate from §3.

Stored fields also require a transport bound.
For successive gauge factors \(g_n\), put \(a_n=\max(\|g_n-I\|,\|g_n^{-1}-I\|)\).
Submultiplicativity gives
\[
 \operatorname{cond}(g_N\cdots g_1)
 \le\prod_n(1+a_n)^2\le e^{2\sum_na_n}.                         \tag{7}
\]
This controls conjugation only if that sum fits the stored-field room.
The actual Borel and analytic stored-variable domains must still be respected.
SA L6160–6174 and L17924–17946 specify those distinct domains and the switch removal.
They do not turn a field bound into a bound for every transported stored argument.

For a regional Gaussian matrix, the corresponding calculation is
\[
 \|I-c^{-1}A_n\|
 \le q_0+c^{-1}\sum_{i<n}\|A_{i+1}-A_i\|<1,                   \tag{8}
\]
provided \(\|I-c^{-1}A_0\|\le q_0<1\) and the sum is less than \(c(1-q_0)\).
Then the logarithm series in `regional-gauss.md` (7) converges on every prefix.
For uniform bounds, the right side of (8) must stay below a fixed \(q<1\).
These matrices must be the intrinsic regional matrices consumed by the stage.
`gamma-bx-check.md` §4 leaves their lifted-core admission and the profile-weighted patch precision open.
The small matrix logarithm in (4) does not prove this Gaussian estimate.

## Result

**Correction to the proposed closure from radius margins.**
The coefficient budget (1)–(3) is uniform under its stated fixed-chart conditions.
The continuation estimate (5) follows from (6), under §3's fixed-chart averaging hypotheses.
The requested uniform stage estimate, and hence (D4), remain unproved.
No actual history with an exhausted margin is established.
This is not a counterexample to stage inclusion or a correction of the outline's theorem.

**First input still open:** prove (5) for the actual transported (R5) datum on the larger core.
It must cover every earlier parameter, changed sequence, and preceding chart, with the clause margins in (3).
The assigned current, stored transport, and consumed Gaussian matrices then require their own uniform bounds.
The arguments here are by hand and have not been independently checked.
