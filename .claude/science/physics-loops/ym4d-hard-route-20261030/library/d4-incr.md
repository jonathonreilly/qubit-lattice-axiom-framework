# d4-incr: transported stage increments
Provenance: Codex (GPT-6 family; queue effort max; runtime variant and effort not exposed); checkout `40fc679e214f303dac16632cfa80f741dd26d882`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit; grants no status.

## 1. Sources and target

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's constructions.
Balaban supplies the underlying stage method.
This note addresses row 245 and `d4-stage.md` (6), following rows 236 and 240.
It tests (D4), the domain input to (LOC).
The literature records `lit-large-field.md` §1 and `lit-balaban.md` identify Balaban's CMP 122 stage arguments.
Those two papers are absent from the supplied paper folder; their stage estimates are not imported here.

The [pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), L17610–17630, compares real stage tests.
L17904–17926 sketches complex interpolation using “the response and hereditary-domain estimates”.
The new argument, gauge factor, and stored data “are formed together”.
L6149–6157 calls stage inclusions “analytic inclusion hypotheses”.
Thus the requested complex estimate is sketched, with inclusion assumed.
It is not supplied by the real curvature comparison.

Fix an old chart \(\tau\), including its real reference, logarithm, tower, and units.
For a single-layer tower of depth \(d\le p\), set \(\|w\|_*=L^{d-p}\|w\|_\infty\).
Take \(C_AR<r_{B,\tau}\), as in `d4-stage.md` §3.
The target is
\[
 \sup\|w_{0,\tau}\|_*<R/4,\qquad
 \sum_n\sup\|w_{n+1,\tau}-w_{n,\tau}\|_*<R/4.
 \tag{I}
\]
Each supremum includes the larger source core and every retained earlier parameter.
The same estimate is required for every preceding chart and both erosion rules.
All prefixes must exist there before tower admission can follow from (I).

## 2. What the library estimates give

`ld-decoupled.md` (5) bounds the nonlinear response in a weighted first-order norm.
Equation (6) converts distance from its datum support into layer decay.
Both use one admitted determining sequence and its specified response equations.
They do not identify a stage difference with that response.
They do not bound derivatives of the full earlier composition.

`wf-room-2.md` Theorem L gives tower existence and curvature/current response bounds.
It fixes the real reference and requires memberwise containment in an ambient separated sequence.
It covers both erosion rules under those hypotheses.
Its input is a potential difference; its output is a tower observable difference.
It cannot recover a potential difference from the real curvature tests.

`o1-decoupled.md` §3.1 requires common coordinates and an admitted transported pair, (H-pair).
It separately requires (H-node) for comparisons in the assigned representatives.
The removed-map estimate consumes these bounds; it does not construct the stage transport that must satisfy them.

`c1-repr.md` §8 bounds the raw averaging datum by \(C_A\|w\|_*\).
Its endpoint factors correct the straightened-average estimate.
It fixes one real reference and proves the larger analytic ball for either tower rule.
It does not compare two stage references.

`d4-budget.md` (5)–(7) sums transported increments once they are bounded.
`d4-stage.md` (6) then admits every prefix in the continuation ball.
Neither supplies the required increment bound.
These are implications from their named inputs, not independently checked results of this note.

## 3. The first remade shell

Let \(C\) be eligible at level \(t\), with at least one completed stage before drop-out.
Put \(a=t-\mathsf N_t\), \(j=a\), and \(l=a+1\).
Stage \(0\to1\) integrates stored fields of level \(j\), after their sharper tests.
By (R21), its determining sequence changes by
\[
 \Omega_l^0\cap C=\Omega_l^\circ\cap C,
 \qquad \Omega_l^1\cap C=C\setminus Z''_l(C).
 \tag{1}
\]
All other members stay fixed.
The action sequence stays fixed too.
By (R2), this can change determining rows at both levels \(l-1\) and \(l\).
Thus this is not a datum change on an unchanged determining set.

The stage datum belongs to level \(j=l-1\), not level \(t\).
The real sharper test uses \(\delta'_j\), not \(\delta_t\).
For an instance of `ld-decoupled.md` with datum level \(j\) and datum norm \(b_j\), its proof gives
\[
 \|h_j\|_{X,\omega}\le Cb_j,\qquad
 \xi_m|h_j|+\xi_m^2|\nabla_U h_j|
 \le Cb_j e^{-\theta_L(j-m-1)_+}.
 \tag{2}
\]
Here \(\omega=e^{\lambda d(\cdot,E_j)}\) uses that sequence's metric and datum support.
The second estimate requires its source support and layer-crossing hypotheses.
This does not establish that the internal stage is such an instance.
Replacing \(j\) by \(t\) would assume up to \(\mathsf N_t\) extra crossed layers.

The unresolved step precedes use of (2).
One must express the actual stage change, including its gauge, in the old chart for every earlier parameter.
One must then bound its datum on that larger complex source.
The real sharper test supplies neither statement at independent complex parameters.
`o1-decoupled.md` (H-pair) assumes the needed comparison instead of producing it.

For fixed layer and lift, (R22) gives the coefficient allowance
\[
 c_0(x\mid m)-c_1(x\mid m)
 =\frac{\mathsf g_t(m)}{2\mathsf N_t}
  +\beta_R\mathbf1_C(x)2^{-|m-l|}.
 \tag{3}
\]
Outside \(C\), only the phase allowance remains.
This subtraction bounds no potential increment.
Changes of layer or lift require conversion to the old units before comparing actual radii.

The same issue occurs for either erosion rule.
Theorem L applies after its real reference, containment, and potential hypotheses have been supplied for that rule.
It cannot supply the missing stage potential by bounding the resulting tower curvature.

## 4. The full composition: an exact correction

Write \(w_{n,\tau}=F_{n,\tau}(z_n;\zeta)\), if common source coordinates exist.
Here \(F_{n,\tau}\) includes every earlier substitution and transport into the old chart.
The tuple \(\zeta\) contains every retained earlier parameter.
Count a sequence change in \(z_n\) or in \(F_{n,\tau}\), without counting it twice.
For fixed \(\zeta\), the exact identity is
\[
\begin{aligned}
 w_{n+1,\tau}-w_{n,\tau}
 ={}&F_{n+1,\tau}(z_{n+1};\zeta)-F_{n+1,\tau}(z_n;\zeta)\\
 &+F_{n+1,\tau}(z_n;\zeta)-F_{n,\tau}(z_n;\zeta).
\end{aligned}                                                    \tag{4}
\]
Suppose the segment between the source points lies in the domain of \(F_{n+1,\tau}\).
Use fixed normalized norms on that source and the old target.
Let \(b_n\) bound \(\|z_{n+1}-z_n\|\).
Let \(K_n\) bound \(\|D_zF_{n+1,\tau}\|\) along the segment.
Let \(d_n\) bound the second line of (4) in \(\|\cdot\|_*\).
All three bounds take the required suprema over \(\zeta\) and the larger source core.
Integrating the derivative along the segment proves
\[
 \sup\|w_{n+1,\tau}-w_{n,\tau}\|_*
 \le K_n b_n+d_n.                                                \tag{5}
\]
If the earlier composite is unchanged as a function, \(d_n=0\).
That fact does not remove \(K_n\).
A bound for a single response cannot be substituted for the right side of (5) without these identifications.

Here is a sufficient derivative estimate, with its domain requirement explicit.
Suppose each earlier map is holomorphic and has form \(f_i=T_i+u_i\), with \(T_i\) linear and \(\|T_i\|\le1\).
Suppose every intermediate point has a complex ball of radius \(\rho_i\) in its domain.
On those balls assume \(\|u_i\|\le A_i\), uniformly over earlier parameters.
Cauchy's formula along a unit direction gives \(\|Du_i\|\le A_i/\rho_i\).
The chain rule therefore gives
\[
 \|D(f_1\circ\cdots\circ f_q)\|
 \le\prod_{i=1}^q(1+A_i/\rho_i)
 \le\exp\!\left(\sum_{i=1}^q A_i/\rho_i\right).                 \tag{6}
\]
This proof uses no computation.
The cited fixed-sequence estimates do not establish these common balls after (1).
Individual derivative bounds by a constant \(C>1\) would instead give \(C^q\).
That estimate is not uniform in the earlier depth.

## 5. General stage and summation

At stage \(n\to n+1\), put \(j=t-\mathsf N_t+n\) and \(l=j+1\).
Replace the member at \(l\) as in (1).
Again the rows at \(j\) and \(j+1\) can change.
The same identities (4)–(5) hold whenever their common domains have been established.
Thus the sufficient expenditure is
\[
 \sum_n(K_n b_n+d_n)<R/4.                                      \tag{7}
\]
Together with the initial bound in (I), this proves (I) by the triangle inequality.
For an entire earlier history, the sum must include its full ordered list of substitutions.
The estimate must hold for each old chart and each erosion rule.

The scalar decay sum is finite if its transported increments have the majorant from `d4-budget.md` (5).
Indeed, \(\sqrt{1+r}\le1+r\) gives
\[
 \sum_{r\ge0}\sqrt{1+r}L^{-r}\le(1-L^{-1})^{-2}.
\]
This sums a bound already expressed in the old chart.
It does not bound the factors \(K_n\) or the transport differences \(d_n\).
The real stage tests and the coefficient allowance (3) supply neither quantity.
Consequently a first-exit argument still lacks its estimate before the possible exit.

## Result

**Correction of the one-response proof attempt for the outline's sketched step.**
The stage uses the datum level \(l-1\) and can change two determining-row levels.
Its increment must pass through the earlier composition.
Equations (4)–(6) prove the required composition correction under their explicit domain hypotheses.
They do not prove `d4-stage.md` (6) for the actual stages.
No actual history with a divergent sum or a violated continuation clause has been established.

**First input still open:** the common-chart transition at stage \(0\to1\) of the eligible eventual drop-out in §3.
It must bound the prepared shell's transported pair and assigned gauge on the larger source, uniformly over earlier parameters.
It must also supply the common domains needed to differentiate the earlier composition.
The first unresolved consumer is the old tower's (R5) continuation clause, for each erosion rule.
The general stage and the all-history sum remain open.
The new identities and estimates are hand arguments by Codex, not independently checked.
