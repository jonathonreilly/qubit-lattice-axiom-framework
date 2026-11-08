# Repo search

Codex, 2026-11-08. FINISH row 568. Checkout `b7000edcdf91bdb061d1f8998cd1d9f31c427cc0`.
Research text. Not an audit. Grants no status. No computer-assisted proof.
New arguments here have not been checked by another provider.
The checkout advanced concurrently to `60ddc80b9` during this work.
Its diff from the pin changes only FINISH and the unrelated `out-live2-check.md`.
The mathematical source files read here are unchanged from the pin.

`library/prior/leaf-cbr.md` is absent. I used the lead's
`prior/repo-search-2026-11-08.md`, especially §§2 and 8.
That search covered main and PRs #10114, #10133, #10134 and #10141.
It found related conditional results, but no supplier of the changed-boundary comparison.
I fetched main at `43a1fcc374711ca50626eca667441d3ca575c7d1` and read its workflow.
I fetched #10141 at `c73ad7b177d94f89ff37b77386936e3d52b48b05` and checked these hits:

| Hit | What it supplies | Distance from CBR |
|---|---|---|
| `research/ym4d/library/out-mu.md`, 8–32, 69–82, 180–189 | Unique regular axial minimizer and holomorphic nesting on admitted windows, using literal Bałaban averages. | Reusable there. It expressly supplies no derivative decay or changed-boundary admission. |
| `research/ym4d/library/fp1.md`, D1–D7, Lemmas 4–7 | Exact flat-fibre comparison, a current-scale gap, and exponential current-scale kernels. | Reuse these results. The correcting gauge and fine-mesh pointwise densities are outside their conclusions. |
| `library/leaf-tbflat.md`, §§2–5 | Actual-box null-space calculation, constant-flux face/corner probes, exact coupled force (11), and primitive inverse (14). | Already done. Its three routes leave CBR (15) open. |

The snapshot is prior work from this project, not independent evidence.
Credit its named authors and checks. The local registry keeps H-C-MARK open and unowned.
Searches for CBR and TB-FLAT in the registry, `open-core.md` and `l17c.md` found no separate owner.
FINISH row 568 is the present assignment. No existing proof is reopened.

## 1. Target and ports

The target is exactly CBR (15) of [leaf-tbflat.md](leaf-tbflat.md).
Keep its force (11), original linearized common domain, layer metric and prescribed node frame.
The output includes the potential, first differences and contracted second readout.
It includes currents only on the consumer's full stencils.
Y 13360–13427 weights those three potential readouts by \(\ell,\ell^2,\ell^3\).
An arbitrary uncontracted Hessian is not one of them.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the constrained variational and localization methods.
**SA** is [YM4_sketch_500.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
**I** is [theorem_0_complete_account_raw_I.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).
Both use commit `31a47c543775`.
**Y** is [YM4_1400.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex), at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
The supplied `/tmp` copies were present and were reused.
Their indices and neighbouring rows were consulted before bounded source reads.

| Port | Source lines | Use and standing |
|---|---|---|
| Original simple and hereditary domain | SA 5663–5727, R4–R6; index chunk 05, rows 73–78 | Definition. The independent current is a separate input. Every required tower retains its own existence and bounds. |
| Exact physical response and primitive inverse | SA 11718–11888, BGR1–BGR9; index chunk 11, rows 67–80 | Finite algebra, proved there under its inverse hypotheses. Already ported in `leaf-tbflat.md`. |
| Boundary difference equation | SA 12226–12292, BGR28–BGR30; index chunk 11, rows 120–124 | Its decay conclusion assumes the weighted inverse. It does not supply CBR. |
| Free-boundary criticality and quoted regularity | I 43098–43155; §4.12–4.19 index, chunk 01, rows 56–63 | Definition and cited block-scale input, “used here by statement”. No new free-boundary proof follows from that phrase. |
| Payment after a successful repair | `hcm-repair.md`, §3; `gates/hcm-repair-check.md`, findings 3–4 | Existing conditional implication. CBR alone does not supply its nonlinear and ownership premises. |

The requested TB-BC tree section, `hcm-tb.md`, `hcm-repair.md`, and its check were read in full.
The old arbitrary-surface-force logarithm is retained as prior work.
The new kill test below asks whether its force can arise from one bounded original input.

## 2. Kill test first: realize the bad trace, then check its cost

**Outcome: no counterexample to CBR.**
The following packet realizes the bad trace with a uniformly bounded first derivative.
Its bulk equation, however, has an unbounded force.
It cannot be inserted as a bounded physical-current input to (11).
This tests a new attempted realization of the previous packet, not the null-space calculation again.

Use the transverse polarization \(A_3=a\), independent of coordinates 3 and 4.
Let \(h=1/n\), \(n=L^m\ge32\), and make coordinate 2 periodic with period one.
Write its fine coordinate as \(hl\). Set
\[
 N=\lfloor n/16\rfloor,\quad \theta_j=2\pi j/n,\quad
 \alpha_j=2\operatorname{arsinh}(\sin(\theta_j/2)).
\]
On the two-sided normal lattice, set
\[
 a_{r,l}=hr\sum_{j=1}^N\frac{e^{-\alpha_j|r|}}j
                                      \sin(\theta_jl).                 \tag{1}
\]
The original curvature Hessian in this sector is the scalar lattice Laplacian.
This is a face model. It is not claimed to realize every boundary of an actual stage box.

Here \(\theta_j/4\le\alpha_j\le\theta_j\).
The partial sums of \(\sum_{j\le k}\sin(jt)/j\) are uniformly bounded.
Use the hand proof already given in `leaf-tbflat.md`, §5, Route 3.
Abel summation preserves that bound after multiplication by
\(e^{-(\alpha_j-\alpha_1)|r|}\), a decreasing sequence between zero and one.
Thus \(|a|\le C h|r|e^{-\alpha_1|r|}\le C\).

For a tangential first difference, absolute values give
\[
 |D_2a_{r,l}|
 \le C\frac{|r|}{n}\sum_{j=1}^N e^{-c j|r|/n}\le C.
\]
The last bound follows by comparison with the integral of the decreasing exponential.
At \(r=0\) this derivative is zero.
For a normal first difference, use
\[
 (r+1)e^{-\alpha(r+1)}-re^{-\alpha r}
 =e^{-\alpha r}\{e^{-\alpha}-r(1-e^{-\alpha})\}.
\]
The first term is bounded by Abel summation.
The second obeys the preceding geometric-sum bound since \(1-e^{-\alpha_j}\le2\pi j/n\).
Oddness in \(r\) treats the other half-line and the two differences meeting zero.
Consequently \(\|a\|_\infty+\|Da\|_\infty\le C\), uniformly in \(n\).

Every complete straight top row is zero, by the period-one sine sum in direction 2.
The literal-row correction in `leaf-tbflat.md`, §2, (1a), gives the same zero literal rows.
That correction has bounded derivatives through order three in this homogeneous model.
It changes neither curl nor its current. We reuse it; no new frame theorem is asserted.

The bulk equation detects the cost hidden by the first derivative bound.
For \(r\ge1\), direct substitution gives
\[
 (-\Delta_h a)_{r,l}
 =\sum_{j=1}^N\frac{2\sinh\alpha_j}{h j}
                         e^{-\alpha_jr}\sin(\theta_jl).                \tag{2}
\]
Indeed \(2+4\sin^2(\theta/2)=2\cosh\alpha\); the terms proportional to \(r\) cancel.
At \(r=l=1\), retain \(\lceil N/2\rceil\le j\le N\).
Then \(\theta_j\ge\pi/32\), \(\sin\theta_j\ge1/16\),
\(2\sinh\alpha_j/(hj)\ge\pi\), and \(e^{-\alpha_j}\ge1/2\).
All terms are positive. There are at least \(N/2\) retained terms, so
\[
 \|\Delta_h a\|_\infty\ge\pi N/64\ge\pi n/2048.                       \tag{3}
\]
These inequalities use \(N\ge n/32\) and \(\theta_j\le\pi/8<1/2\).
No numerical evaluation is used.

Cut at \(r=0\), keeping \(r\ge0\).
Since \(a_{0,l}=0\) and \(a_{-1,l}=-a_{1,l}\), the omitted-plaquette force is
\[
 ((RH_o-H_XR)a)_{0,l}
       =\frac1h\sum_{j=1}^N\frac{e^{-\alpha_j}}j\sin(\theta_jl).        \tag{4}
\]
If one sets \(j_o=H_oa\), \(j_X=Rj_o\), this is the exact force difference in this sector.
The Neumann solution from `leaf-tbflat.md`, (19)–(21), then has
\[
 (D_2w)_{0,0}
   =\sum_{j=1}^N\frac{e^{-\alpha_j}\sin\theta_j}
                            {j(e^{\alpha_j}-1)}
   \ge\frac18\sum_{j=1}^N\frac1j.                                  \tag{5}
\]
This curvature read is gauge invariant.
Making coordinate 4 a free half-line gives the same calculation at a two-face corner.
Its fourth-direction flux is zero.

But (3) makes the original forcing unbounded in this realization.
Rescaling it to bounded forcing removes (5)'s divergence.
Indeed its summands are also at most \(4/j\), so that read becomes \(O(n^{-1}\log n)\).
For the unforced physical map, this packet is not a critical zero-datum field.
Its nonzero curl already excludes that by the prior zero-mode result.
Nor can an independent current simply be declared equal to \(H_oa\).
SA 11798–11805 requires its defining operator to be matched first.
The hereditary tower and prescribed-frame conditions have not been verified for (1).

Thus a first-derivative bound alone cannot explain CBR's cancellation.
The attempted counterexample fails before it meets the original common-domain requirements.
The full CBR kill test remains unresolved; no universal pass is claimed.

## 3. Route A: use stationarity to regularize the incoming trace

This route derives trace regularity from the original equation.
It does not add a Hölder condition to the common domain.
The source already proves the scalar regularity step.
SA 12637–12726, BGH20, fixes \(0<\alpha<1\), \(R\ge64h\), and a field on \(Q_{2R}\).
Its conclusion on \(Q_{R/2}\), with right-hand norms on \(Q_{2R}\), is
\[
 \|Da\|_\infty+R^\alpha[Da]_\alpha
 \le C_\alpha(R^{-1}\|a\|_\infty+R\|\Delta_h a\|_\infty).
                                                                    \tag{6}
\]
Credit Sussman and Alpoge, with Claude and Codex, for this port.
Its proof is complete there. We do not rederive it.
SA 12753–12775 explicitly retains the gauge and componentwise Laplacian bound as premises.
Index chunk 11 and obligations 12644–12648, 12755–12775 make the same distinction.

The attempt is to supply those premises from the multiplier equation.
SA 11143–11150, PX93, proves full physical stationarity from slice criticality and the Ward identity.
Use it first in a homogeneous complete-block patch.
Write the literal row as \(Q=S-\mathcal D\sigma\), using the ported flat-fibre identity.
Here \(\mathcal D\) is coarse endpoint difference, and \(r\) evaluates fine scalars at top nodes.
Endpoint covariance gives \(QD=\mathcal D r\).
For an unforced physical solution,
\[
 H a+Q^*\lambda=0
 \quad\Longrightarrow\quad
 r^*\mathcal D^*\lambda=0
 \quad\Longrightarrow\quad
 \mathcal D^*\lambda=0.                                               \tag{7}
\]
The last implication uses surjectivity of node evaluation.
Consequently
\[
                         Q^*\lambda=S^*\lambda.                      \tag{8}
\]
Thus one must cancel the path terms before bounding their adjoints.
Bounding each path adjoint separately would discard an exact Ward cancellation.

In top units, the raw straight row has coefficients at most \(h^4\).
It reads two endpoint blocks, with bounded column multiplicity.
The physical fine adjoint therefore gives
\[
                        \|S^*\lambda\|_\infty\le C\|\lambda\|_\infty. \tag{9}
\]
This is also the homogeneous case of `fp1.md`, Lemma 8, (15).
For a homogeneous periodic problem, FP1's analytic coarse energy symbol bounds its multiplier kernel in current units.
That is a useful bulk input. It is not a new bound for the changed mixed boundary.

I tried to insert (9) into (6).
Two identifications remain essential at the actual mixed stage.
The Ward-cancelled force must have a weighted bound on its actual row and gauge blocks.
Also the prescribed potential must satisfy the componentwise Laplacian equation used in (6).
The Wilson current \(d^*da\) alone is not that Laplacian in an arbitrary frame.

Here is a direct check of this second issue.
On a homogeneous periodic patch take \(j=\lfloor n/4\rfloor\), \(\theta=2\pi j/n\), and
\[
 \phi_r=h^2\sin(\theta r),\qquad a=D\phi.
                                                                    \tag{10}
\]
Then \(\phi\) vanishes at every top node.
Hence \(Qa=0\), \(da=0\), and \(d^*da=0\), exactly.
But \(\|a\|_\infty\le2h\), \(\|Da\|_\infty\le4\), while
\[
                         \|\Delta_h a\|_\infty\ge c/h.                \tag{11}
\]
Indeed the Laplacian multiplier is \(4h^{-2}\sin^2(\theta/2)\),
and the amplitude of \(a\) is \(2h\sin(\theta/2)\).
Here \(\pi/4\le\theta\le\pi/2\).
The sampled squared cosine has average \(1/2\), so its maximum is at least \(1/\sqrt2\).
These facts give (11), for example with \(c=1/(8\sqrt2)\).

This is a pure gauge. The prescribed slice must remove it.
It is not a CBR counterexample.
It proves why the R4 first-difference and curvature bounds cannot alone supply (6)'s last premise.
Replacing the prescribed frame by an uncontrolled Coulomb representative would not prove the required gauge readout.

The same point prevents identifying an independent current with that Laplacian.
Its separate defining equations remain in force, as required at SA 11798–11805.
Neither FP1 nor `out-mu.md` supplies this mixed-boundary identification and its weighted bound.
The finite formula BGR9 retains the multiplier block \(E^*HT\); it does not bound it.

**Route A stops at this step of CBR:** obtain the required local Laplacian and gauge bounds
from the actual coupled equations on the original mixed-domain inputs.
The scalar regularity implication is already available.
It cannot be used by treating an independent-current coordinate as its missing source.

## 4. Route B: evolve with exact constraint feedback

This route keeps the constraint during a heat evolution.
It estimates that evolution before taking its stationary limit.
It differs from an energy-to-pointwise estimate and from reflection of the saddle operator.

At one fixed mesh, work on the actual gauge slice.
If its gauge condition is affine, translate it first and retain the resulting force.
Let \(\Pi_X\) be the orthogonal projection onto \(\ker q_X\).
Choose a field \(v\) with the required row and gauge data, and retain the actual force \(j_X\).
The affine flow is
\[
 \dot u=-\Pi_X(H_Xu-j_X),\qquad u(0)=v.                              \tag{12}
\]
It keeps those data exactly. On the tangent space put
\(A_X=\Pi_XH_X|_{\ker q_X}\).
The finite positivity from `leaf-tbflat.md` gives
\[
 u(t)-v=-\int_0^t e^{-sA_X}\Pi_X(H_Xv-j_X)\,ds.                     \tag{13}
\]
The limit solves the constrained equations.
After subtracting \(Ra_o\), it is the field in that note's (14), with its row and gauge lifts retained.
This is a new way to estimate the same coupled response, not a change of its force.

### A scalar feedback estimate which does work

Consider a rectangle tiled by complete unit blocks, with fine spacing \(h=1/n\).
For this paragraph only, \(Q\) is scalar block mean, \(H=-\Delta_{h,N}\), and
\(\Pi=I-Q^*Q\). The pairings give \(Q^*\) as piecewise constant extension.
Take \(j=0\). Thus
\[
 \dot u=\Delta_{h,N}u+Q^*QHu,
 \qquad Qu(t)=Qu(0).                                                  \tag{14}
\]
This is a scalar model, not an identification of the vector saddle.

Summing the Laplacian through one unit block leaves its face fluxes.
Each face has total physical area one. A missing outer face has zero flux.
Consequently
\[
                      \|QHu\|_\infty\le2d\|Du\|_\infty,
                      \qquad d=4.                                   \tag{15}
\]
There is no inverse mesh factor in (15).

Let \(E_N(t)=e^{t\Delta_{h,N}}\).
The scalar heat bounds needed here are
\[
 \|E_N(t)f\|_\infty\le\|f\|_\infty,
 \|DE_N(t)f\|_\infty\le C t^{-1/2}\|f\|_\infty,
 \|DE_N(t)u_0\|_\infty\le\|Du_0\|_\infty.                            \tag{16}
\]
Credit Sussman and Alpoge, with Claude and Codex, for the infinite-lattice kernel estimate,
SA 12438–12530, BGH5. Its two time ranges give the middle bound for every \(t>0\).
Their positive heat kernel and product Fourier formula are SA 12411–12433, BGH2–BGH4.
The short-time bound \(C/h\) is at most \(Ct^{-1/2}\) when \(t\le h^2\).

Here is the scalar free-box transfer used in (16).
On a path of \(K\) sites, sum the infinite transition kernel over images
\(r-s+2kK\) and \(r+s+1+2kK\), \(k\in\mathbb Z\).
The resulting kernel has the ghost equalities at \(-1,0\) and at \(K-1,K\).
It solves the free-end heat equation and has the identity initial matrix.
Uniqueness of that finite system identifies it with \(E_N(t)\).
The image sums preserve the derivative absolute-row bound, with a fixed multiplicity.
Tensor the four paths to obtain the rectangle and the first two bounds in (16).
For the third bound, difference the path heat equation.
Its first differences solve the heat equation with zero end values.
That positive, mass-decreasing evolution is a maximum-norm contraction.
The other directions retain their positive free-end heat equations.
This proves the third bound on every existing first-difference stencil, including corners.

Write \(x(t)=\|Du(t)\|_\infty\) and \(x_0=\|Du(0)\|_\infty\).
Duhamel's identity, (15), and (16) give
\[
 x(t)\le x_0+A\int_0^t(t-s)^{-1/2}x(s)\,ds.                           \tag{17}
\]
The constant \(A\) is independent of mesh and rectangle size.
Iterate this inequality once.
The convolution of \(t^{-1/2}\) with itself equals \(\pi\), by the substitution \(s=t\sin^2\theta\).
For \(0\le t\le1\), this gives
\[
 x(t)\le(1+2A)x_0+\pi A^2\int_0^t x(s)\,ds
       \le(1+2A)e^{\pi A^2t}x_0.                                    \tag{18}
\]
The last inequality follows by differentiating the integral upper envelope.
Using the first bound of (16) in Duhamel also bounds \(\|u(t)\|_\infty\).
Thus scalar block-mean feedback preserves the potential and first-difference bounds for \(0\le t\le1\), uniformly in \(h\).
This is a written auxiliary result. It uses the ported scalar heat lemma, not a numerical evolution.

The constrained flow itself is not positive.
On a path with blocks \(\{0,\ldots,n-1\}\) and \(\{n,\ldots,2n-1\}\), take \(u_0=1_{\{n\}}\).
At site zero, for \(n\ge3\), \(Hu_0=0\), while the first block's mean of \(Hu_0\) is \(-1/(nh^2)\).
Hence \(\dot u(0)_0=-1/(nh^2)<0\).
A scalar maximum principle for the *projected* generator would therefore be false.
The feedback estimate above avoids that false step.

### The attempted transfer to CBR

For the actual vector problem, \(\Pi_X\) projects onto the literal row kernel inside the prescribed gauge slice.
It is not \(I-Q^*Q\) for scalar means.
Even for onto rows its formula contains \(q_X^*(q_Xq_X^*)^{-1}q_X\) on that slice.
The Wilson Hessian is curl–curl; replacing it by the component Laplacian also changes the gauge block.

The precise step needed to copy (17) is a bound for that full feedback in local units.
It must map the weighted potential/first-difference norm to the weighted volume-source norm,
with one fixed constant and the required boundary-distance weights.
All row changes, gauge restoration, and independent-current terms must enter this same feedback.
One also needs its smoothing and decay beyond time one to take the limit in (13).

I tried the available scalar projector and the flat vector kernel as substitutes.
The scalar projector proves (15) only for scalar means.
FP1's vector kernel is in current-lattice coordinates and does not supply this fine-mesh projected evolution.
SA 11257–11312 proves a component Feynman comparison, but explicitly excludes the inner-Maxwell boundary form and Landau subtraction.
That exclusion applies here.
No bound for the actual feedback, or its stationary readout in the prescribed frame, has been obtained.

**Route B stops at this step of CBR.**
The scalar estimate (18) resolves the short-time scalar test.
It does not justify changing the actual projector, boundary form, or gauge in (12).

## 5. Route C: rescale a failed estimate and classify its limit

This is a compactness attempt, independent of the heat-flow estimate.
It tries to rule out an unbounded first-difference read by classifying its small-scale limit.
The potential, current and node reads would still need their own estimates if this step succeeded.

Suppose normalized inputs had \(\|z_k\|_{\rm original}\le1\), but a local first-difference read grew like \(M_k\to\infty\).
In a homogeneous rim patch, put the top spacing equal to one.
Choose a scale \(r_k\to0\) around the bad read, and consider
\[
 v_k(y)=\frac{w_k(x_k+r_ky)-w_k(x_k)}{M_kr_k}.                        \tag{19}
\]
Only lattice points and existing stencils are used before taking a limit.
If \(h_k/r_k\to0\), the proposed limiting region is a half-space or an orthant.
The route would need compactness strong enough to preserve a nonzero normalized derivative.
It would also need the scaled row, gauge and volume forces to vanish in the limiting equation.
Neither fact follows just from weak energy compactness.

Even granting both facts does not give the required zero-limit theorem.
Take the face \(y_1\ge0\), or the two-face corner \(y_1,y_4\ge0\), and put
\[
                  v_3(y)=y_2,\qquad v_1=v_2=v_4=0.                  \tag{20}
\]
Then \(d^*dv=0\), \(d^*v=0\), and \(\Delta v=0\).
Its normal potential and normal curvature traces vanish on both named faces.
It has bounded first derivatives and at most linear growth.
But \((dv)_{23}=1\). Thus it is not a gauge mode.
The same statements hold exactly for this affine field on every compatible lattice.
No limiting differential equation is needed to check them.

This refutes the proposed Liouville step with only linear growth.
It does not refute CBR. The affine field has nonzero physical coarse data.
Under (19), a top row has length \(1/r_k\); its carrier eventually leaves every fixed compact set.
Convergence on compact sets therefore does not pass that row constraint to the limit.
Its datum cannot simply be set to zero in the limiting problem.

I next tried subtracting the affine profile and iterating an improvement of flatness.
This would remove (20) from the local classification.
However, subtracting it changes coarse curvature.
For the raw straight row at unit spacing, \(S v_3\) increases by one between neighbouring direction-2 blocks.
Hence its coarse 23-plaquette curl is one.
The literal correction is a coarse gradient, so it has the same coarse curl.
No gauge fixing the prescribed nodes can undo that change.

One must therefore restore the exact rows after every affine subtraction.
That restoration must preserve the original common-domain input and node readout.
Its error must decrease sufficiently across the fine-to-top scales to sum all iterations.
The available flat-fibre identity preserves curl, but claims no norm bound for the restoring gauge.
The available smooth lift supplies a competitor, not the required mixed free-boundary minimizer with that frame.
Using the unknown CBR estimate for each restoration would be circular.

A global potential bound does not repair the compactness argument by itself.
Equation (19) only gives \(\|v_k\|_\infty\le2\|w_k\|_\infty/(M_kr_k)\).
At the fine scales where a derivative might concentrate, \(M_kr_k\) can tend to zero.
Choosing a larger \(r_k\) instead need not preserve the normalized derivative.
Uniform derivative compactness is precisely an estimate this argument has yet to prove.

**Route C stops at this step of CBR:** retain the actual row and frame information
through a quantitative boundary improvement of flatness.
The local zero-limit assertion fails by (20).
A corrected argument needs controlled row restoration; it has not been supplied here.

## 6. Result

**Stopping condition (c): CBR remains open after three distinct routes in this note.**
They are equation-based trace regularization, constrained heat evolution, and boundary rescaling.
They are not the earlier energy projection, reflected saddle inversion, or separate surface-kernel bound.

The exact remaining lemma is unchanged.
For every actual stage and every \(z\) in TF's original linearized common domain,
use the force (11) and field (14) of `leaf-tbflat.md` in the prescribed slice.
Construct its compatible row lift and node restoration and prove
\[
 \sup_{x\ {\rm read}} e^{c d(x,\partial_{\rm changed}X)}
 \mathsf N_x\bigl(w_X(z),\text{its prescribed node readout}\bigr)
 \le C\|z\|_{\rm original},                                          \tag{CBR}
\]
with \(C,c>0\) independent of mesh, depth and the old core.
All hereditary and independent-current requirements remain those of the original domain.
No Hölder assumption, smaller domain, or extra exterior datum has been added.

The new scalar result (18) is a possible ingredient for a later proof.
It does not establish CBR, TF, TB-BC, or the renewed-mark payment.
The failed routes are not an impossibility theorem.

The targeted literature check reused `lit-balaban.md` and the previous leaf's source record.
The supplied scratch paper directory was absent.
The explicitly permitted `~/ym4d-papers` copies were available.
CMP 96, p.229, text lines 274–322, distinguishes graded boundaries from local Neumann boundaries.
CMP 109, (4.35), text lines 2107–2129, compares an interior read with a free response.
Neither passage supplies the full-rim estimate above.
These are scope checks, not a claim that Bałaban proves CBR false.

| Item | Result | Remaining limit |
|---|---|---|
| Prior null-space and constant-flux tests | Reused from `leaf-tbflat.md` | Not repeated or enlarged here. |
| New face/corner packet, (1)–(5) | No admissible CBR counterexample | The realizing bulk force grows at least as \(c/h\); full hereditary and frame admission is absent. |
| Ward cancellation, (7)–(9) | Exact in the stated homogeneous physical setting | Does not bound the mixed-stage multiplier and gauge blocks. |
| Scalar block-mean evolution, (14)–(18) | Uniform potential and first-difference bounds for \(0\le t\le1\) | Uses the cited scalar heat lemma; not the actual vector evolution or its stationary limit. |
| Zero-limit argument with linear growth | False by the physical affine profile (20) | Exact coarse rows must survive any corrected rescaling argument. |
| CBR (15), hence TF through the prior finite identities | Open after Routes A–C | No counterexample and no complete proof. |
| TB-BC and H-C-MARK payment | Unchanged, conditional | Nonlinear comparison, original-domain admission and ownership are still separate. |

**First open input: CBR (15), for the exact coupled force (11) on TF's original common domain.**
