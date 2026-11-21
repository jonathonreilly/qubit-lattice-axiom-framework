# Collar block increments

Provenance: Codex (GPT-6 family; serving variant and runtime effort not exposed), repository commit `80be76d796e1bac564287c55950c1c3362244db0`, 2026-11-04; assigned FINISH row 258 (`collar-block`). Research text, not an audit; grants no status. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`; Tadeusz Balaban for the stage method; Claude for `wf-c.md`. Not yet checked by the other model.

## 1. The two estimates have different subjects

The switch gain bounds an activity difference. Applying it to the actual collar read needs a further hypothesis.
The Results of `dropout-bt.md`, `d4-stage.md`, `d4-chart.md` and `wf-c-stage.md` were read first.
Their common open input is the actual read in each old chart, uniformly over earlier parameters.
This note does not choose the stage spaces of row 257.

SA means `YM4_sketch_500.tex`; CA-I means `theorem_0_complete_account_raw_I.tex`.
Their line numbers refer to the pinned revision. Each file was fetched once.
The outline index, its neighbouring rows and `obligations.md` led to these passages:

- **Stages, definition.** SA 17585: “the stored variables of the outer shell” are “integrated out as in a small-field step”. SA 6108–6111 distinguishes the determining sequence, which “governs backgrounds”, from the action sequence.
- **Changing evaluations, sketch.** SA 17564 requires both backgrounds “written in the new variables”. SA 19518 says “differences in the collar field, taken one block of bonds at a time”. This concerns the boundary data introduced at SA 19515.
- **Response interpolation, sketch with domain input.** SA 17908–17911: “The response and hereditary-domain estimates give an analytic interpolation” with response size “divided by the room in the domain of \(f\)”. SA 17916–17919 bounds the resulting \(f_Y\), not its field argument.
- **Switches, definition and sketched gain.** SA 6166–6168 starts “A stored-field function is Borel” and gives analyticity in the switches. SA 17939–17943 says “the term” is analytic in a switch disc and that block differences gain \((\lambda^{\rm st}-1)^{-1}\). SA 17946–17947 evaluates carried terms “at field zero” after integration.
- **Admission, explicit hypothesis.** SA 6155–6158 calls stage maps “analytic inclusion hypotheses”. For the old tower, SA 5706–5707 says: “This expression is required to exist in the chosen continuation domain.”

CA-I does not supply this missing estimate through its preparatory-boundary theorem.
At CA-I 54987–54995 it assumes the stage theorem “holds under its standing hypotheses”.
CA-I 49498–49500 calls background-supply conditions “outside the implication” of its operator theorem.
These are conditional results, not a proof of the collar inclusion.

## 2. The block calculation

Fix one level-\(k\) operation, one preceding chart \(\tau\), and one old tower.
Use \(\|w\|_*=L^{d-p}\|w\|_\infty\), as in `d4-stage.md` line 86.
All suprema include the larger stage source and every retained earlier parameter.
They also include the full collar disc of `dropout-bt.md` (10):
\[
 |s_\Delta|<e^{\bar\kappa},\qquad
 |\nu|<\rho_F=c_FL^{k-j}a_{0,j}\delta(\theta_k)^{-1}e^{-C_F\bar\kappa}>1.
\]
Neither the old chart nor its logarithm branch changes.

At stage \(n\), of level \(j_n=k-\mathsf N_k+n\), list the bond blocks as \(B_1,\ldots,B_{m_n}\).
The required construction is a switch lift \(W_{n,\tau}(\mu)\) of the **full transported collar potential**, with
\[
 W_{n,\tau}(\mathbf1)=w_{n,\tau},\qquad
 W_{n,\tau}(\mathbf0)=w_{n+1,\tau}.                         \tag{1}
\]
These endpoint identities include the changed determining sequence and the assigned return gauge.
They are hypotheses here, not a consequence of switching off an activity.

Let \(\mu^{(a)}\) have its first \(a\) block switches zero and the rest one.
If the lift exists at these points, cancellation of consecutive endpoints gives
\[
 w_{n+1,\tau}-w_{n,\tau}
 =\sum_{a=1}^{m_n}\left[W_{n,\tau}(\mu^{(a)})-
                         W_{n,\tau}(\mu^{(a-1)})\right].    \tag{2}
\]
Thus each summand changes one block only.
Without the second identity in (1), (2) has the extra remainder
\(w_{n+1,\tau}-W_{n,\tau}(\mathbf0)\).

Here is the hand estimate that the switch argument actually provides.
Let \(F(\mu)\) take values in a finite-dimensional normed space.
Suppose it is holomorphic on the block switch discs and bounded by \(M_F\).
Set every bond switch in one block equal to \(z\); fix the other blocks at their telescope values.
Write the resulting function as \(h(z)=\sum_{q\ge0}h_qz^q\), for \(|z|<\lambda>1\).
Cauchy's formula on \(|z|=s<\lambda\) gives \(\|h_q\|\le M_Fs^{-q}\).
Let \(s\uparrow\lambda\) and sum the geometric series:
\[
 \|h(1)-h(0)\|
 \le\sum_{q\ge1}M_F\lambda^{-q}
 =\frac{M_F}{\lambda-1}.                                    \tag{3}
\]
This also proves the bound in the star norm.
The diagonal substitution introduces no factor counting bonds in the block.
Uniform hypotheses give the same bound after taking the earlier-parameter supremum.

For a carried activity, SA 6166–6173 specifies this switch structure.
For \(F=W_{n,\tau}\), the required extension and its bound have not yet been established.

## 3. The sum, conditional on that field estimate

Suppose (1) holds. Require joint holomorphy in each block disc and the analytic source parameters, with
\[
 \sup\|W_{n,\tau}\|_*\le C_W R,                              \tag{4}
\]
where \(C_W\) is independent of the chart, stage, history and earlier parameters.
Here \(R\) is the chosen chart's radius; the ratio in (4) must be uniform.

The source count is explicit: SA 17944–17945 chooses
“\(\lambda^{\rm st}=(\log\theta_j)^{6r+1}\)” for
“\(O(\check R_k^4)\) cubes in a component and the \(\mathsf N_k\) stages”.
Group the stage's bonds by their level-\(k\) \(M\)-cube, assigning boundary bonds once.
Write \(C_b\check R_k^4\) for this cube count.
SA 19410 specifies “\(\check{R}_j=\mathsf{N}_j\)” using the running minimum.
SA 17334 defines \(\check R_k\) as “the smallest power of \(L\)” above the logarithmic scale.
Thus, with \(t=\log\min_{i\le k}\theta_i\),
\[
 \sum_{n<\mathsf N_k}m_n\le C_b\check R_k^5\le C_bL^5t^{5r},\qquad
 \lambda_j^{\rm st}\ge t^{6r+1}\quad(j\le k).                 \tag{5}
\]
The first inequality uses precisely the component count stated above.
There is no count of individual bonds within a switched group.
For \(t^{6r+1}\ge2\), each block difference is at most \(2C_W R\,t^{-6r-1}\) in star norm.
Equations (2)–(5) then give
\[
 \begin{split}
 E_\tau
 &\le\sum_{n<\mathsf N_k}\sum_{a\le m_n}
                \frac{C_W R}{\lambda_{j_n}^{\rm st}-1}\\
 &\le 2C_bL^5C_W R\,t^{-r-1}<R/8,
 \qquad t^{r+1}>16C_bL^5C_W.                                 \tag{6}
 \end{split}
\]
Choose the coupling ceiling last so its frame floor implies both displayed conditions.
This choice is uniform, if \(C_W\) is fixed before that ceiling.
For comparison with \(\log\theta_k\), SA 19485 gives
“\(\underline\lambda(j-i)-c_5\le\theta_i-\theta_j\)”.
Hence \(t\ge\frac12\log\theta_k\) when \(\theta_k\ge\max(2c_5,4)\).
The residual gain is therefore a negative power of \(\log\theta_k\).

Retain the initial condition and averaging hypotheses of `d4-stage.md` (6):
“\(\sup\|w_{0,\tau}\|_*<R/4\)” and \(C_AR<r_{B,\tau}\).
Then every prefix lies below \(3R/8\).
Its Cauchy bound, `d4-stage.md` line 98, is “\(\|Db_\tau\|\le2C_A\)”.
Integrating along each segment gives
\[
 \sup\|b_{0,\tau}\|<r_{B,\tau}/4,\qquad
 \sum_n\sup\|\Delta b_{n,\tau}\|
 \le2C_AE_\tau<r_{B,\tau}/4.                                \tag{7}
\]
This proves its (5) with \(\epsilon_\tau=r_{B,\tau}/2\), **under (1) and (4)**.

## 4. First open input

**Construct and bound the actual block interpolation in each preceding chart, before using its old continuation domain.**
On this switch route that means (1) and (4), on the full source of Section 2.
The first required instance is stage \(0\to1\), including every old (R5) tower under both erosion rules.
An estimate for the last response alone omits the earlier compositions.

The named inputs do not supply this hypothesis:

- `wf-c.md` line 68 assumes “\(\|w\|_*\le r_C\)” in Lemma C. Its line 72 bounds the collar datum by \(C_C(\kappa+\|w\|_*)\). This bounds a datum **from an admitted potential**.
- Theorem \(6c^C\), lines 128–140, assumes a common datum ball. Its proof states: “The segment \(b_s\) … lies in the \(r'_B/2\)-ball.” Its bound is \(C_\mu(\varepsilon_1+\|\beta\|_\infty)e^{-\theta d}\). It supplies no switch factor unless the actual input and return have first been bounded there.
- A2-full, line 212, takes “a point of its complex datum polydisc” in the continued axial representative. A3's differentiated equations, `a3-derivative.md` line 358, keep “the reference \(U_0,D,R\) held fixed”. Their gap and response bounds apply on those domains. They do not identify the changed stage rows with an old chart.
- `kept-cov.md` (13) proves covariance of recorded returns. Its proof says, at line 196, “This calculation uses the endpoints, not the value of \(\tau_f\).” The checked version uses the relative kept form and native-orbit covariance (`gates/kept-cov-check.md`, lines 84–86). It supplies no norm bound for the complex return.

For example, the old-chart link difference includes
\[
 W_1-W_0=v(x)(\widetilde W_1-W_0)v(y)^{-1}
          +[v(x)W_0-W_0v(y)]v(y)^{-1}.
\]
This is `d4-chart.md` (4); insert and subtract \(v(x)W_0v(y)^{-1}\) to check it.
Its line 121 states: “the link estimate needs the covariant difference of the assigned gauge.”
Activity covariance does not bound that second term.

The exact unresolved source premise is SA 17908–17911:
> The response and hereditary-domain estimates give an analytic interpolation

The switch estimate cannot supply the hereditary-domain estimate used in this sentence without a further field bound.
A constant activity illustrates the distinction: its switch difference is zero for every argument change.
Also, for a linear read \(W(z)=az\), (3) uses \(M_F=\lambda\|a\|_*\); it does not make \(a\) small.
These are checks of the inference, not counterexamples to the actual stage map.

## Result

**Partial proof of the proposed block route, with its first open input stated above.**
The block Cauchy estimate and the sum (6) are proved by hand under the switch-extension hypotheses and stated component count.
The logarithmic exponent leaves room; the actual field estimate is still open.
Thus `d4-stage.md` (6), its (5), and actual collar admission are not established.
If that input is proved, (7) supplies the old (R5) continuation budget with room.
The other clauses of (D4), including the assigned current and stored arguments, still need their bounds.
No counterexample to stage admission is claimed. No run discharges any step.
This text is not yet checked by the other model.
