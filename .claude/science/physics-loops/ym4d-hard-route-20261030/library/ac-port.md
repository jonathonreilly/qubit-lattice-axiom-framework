# All-order rotation invariance in four dimensions (row 200)
Provenance: Codex (GPT-6; exact runtime variant and effort unavailable; queue requests max), checkout `21e16df4a47ea19af3296599b0fa024072a89c70`, Sussman–Alpoge commit `31a47c543775`. Research text; not an audit; grants no status.

## 1. Claim and inputs

The target is S11, the final implication on O7's rotation path.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
The proof ports [YM3_I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), L76680–77017, especially IV-37-27/30/34.
Its distributional step follows [the YM4 outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), L30582–30848.
These are sources for the argument, not discharged physical premises.

Take [S9](ak-port.md), Result and (12)–(16), and [S10](tu-port.md), Result, conditionally in their common moment setting.
That setting includes O2's local bounds, symmetries and coordinate Hilbert pictures, and O6's joint cone.
The diagonal-flat conclusion uses the existing continuous extension in [s4-s6.md](s4-s6.md), Section 6.
It does not infer existence of an extension from harmonic data alone.

Here is the input interface, read directly from those results.
In the plane \((t,u)=(x_4,x_1)\), real labels are \(\varphi\in C_c^\infty(\mathbb R^2)\).
Extend identities to complex labels by multilinearity.
For distinct planar points, S9 supplies real-analytic coefficients \(c_m\), symmetric in labelled slots and invariant under common translations, with
\[
 c_m(R_vY)=e^{4imv}c_m(Y),\qquad c_{-m}=\overline{c_m},
 \qquad 4|m|\le5n.                                      \tag{1}
\]
Their sum represents the moment on ordinary ordering charts.
Let \(b_n=M(n)\) denote the largest occurring absolute index, or zero if none occurs; set \(b_0=b_1=0\).
S9 and S10 give
\[
 2b_{r+s}\le b_{2r}+b_{2s}\quad(r,s\ge0),\qquad
 0\le b_n\le\lfloor5n/4\rfloor,\qquad b_2=0.             \tag{2}
\]
For \(H=c_{-b_{2k}}^{(2k)}\), every oriented line \(\ell\) also gives
\[
 |H(\theta_\ell X,Y)|^2
 \le |H(\theta_\ell X,X)|\,|H(\theta_\ell Y,Y)|,          \tag{3}
\]
for real-labelled \(k\)-point configurations on one strict side.
The underlying kernel is positive after multiplication by its fixed line phase.
Thus a zero diagonal makes its whole row zero.
No input fails at this interface; all inputs retain their stated conditional scope.

## 2. Polygon divisibility, including arbitrary labels

We prove \(k\mid2b_{2k}\). It is immediate if \(b_{2k}=0\), or \(k=1\).
Otherwise suppose divisibility fails, and put \(H=c_{-b_{2k}}^{(2k)}\).
Give every vertex of a regular \(2k\)-gon the same real label \(\varphi\).
Rotation through \(\pi/k\) permutes these labelled vertices. Equation (1) yields
\[
 H(Y;\varphi,\ldots,\varphi)
   =e^{-4\pi i b_{2k}/k}H(Y;\varphi,\ldots,\varphi)=0.   \tag{4}
\]
The phase differs from one precisely under the assumed failure of divisibility.

Call a labelled set \(S\) zero if every distinct \(2k\)-point completion has zero \(H\).
Suppose \(S\) is zero and \(S\subset\theta_\ell Q\cup Q\), with matching reflected labels and \(j=|Q|\le k\).
All points of \(Q\) lie strictly on one side of \(\ell\).
Add any \(k-j\) points \(A\) on that side, with arbitrary real labels.
The diagonal for \(X=Q\cup A\) contains \(S\), so (3) gives
\[
                    H(\theta_\ell(Q\cup A),B)=0         \tag{5}
\]
for every \(k\)-point \(B\) on that same side, with arbitrary real labels.

Fix the labels of all free slots. Equation (5) holds on an open set of their positions.
Their configuration domain, excluding coincidences and fixed \(\theta_\ell Q\), is connected.
Indeed, move points individually to auxiliary positions, then to their targets, avoiding the finite occupied set.
In the plane, two segments suffice for each move: choose their bend outside the finitely many forbidden lines.
Real analyticity therefore extends (5) throughout this domain.
Hence \(\theta_\ell Q\) is zero, with no restrictions on the other labels or positions.
This releases the labels; vanishing only on equal-label polygons would not suffice.

An edge-bisector reflection pairs all polygon vertices, with none on its line.
The reduction first leaves a consecutive arc of \(k\) vertices.
For an arc indexed \(0,\ldots,j-1\), \(2\le j\le k\), use the reflection
\[
 i\longmapsto j-1-i\quad(j\text{ even}),\qquad
 i\longmapsto j-i\quad(j\text{ odd})\pmod{2k}.
\]
In the odd case add vertex \(j\). The paired union then contains the original arc.
Each chosen half has \(\lceil j/2\rceil\) consecutive vertices, strictly on one side.
Both index sums are odd, so neither reflection fixes a polygon vertex.
Repeated reduction reaches one point labelled \(\varphi\).
Translation invariance moves that point anywhere. The other labels remain arbitrary.
Since the initial \(\varphi\) was arbitrary, every labelled configuration has zero \(H\).
This contradicts the definition of the nonzero highest coefficient. Therefore
\[
                              k\mid2b_{2k}.             \tag{6}
\]

The number 5 supplies a finite highest coefficient through (1).
It does **not** enter the polygon phase or change the divisor in (6).
The argument takes place in the same two-dimensional plane in both ambient dimensions.

## 3. Discrete convexity eliminates every order

Put \(a_k=b_{2k}\), \(a_0=0\). Taking \((r,s)=(k-1,k+1)\) in (2) gives
\[
 2a_k\le a_{k-1}+a_{k+1},\qquad 0\le a_k\le5k/2.       \tag{7}
\]
Thus \(d_k=a_k-a_{k-1}\) are nondecreasing integers, with \(d_1\ge0\).
If some \(d_j\ge3\), then \(a_N\ge a_{j-1}+3(N-j+1)>5N/2\) for large \(N\).
Therefore \(d_k\in\{0,1,2\}\); this is the quantitative use of the band constant 5.
They eventually equal an integer \(d\). Set
\[
 D=\sum_{j\ge1}(d-d_j)\ge0.
\]
Only finitely many terms are nonzero, and eventually \(a_k=dk-D\).
Equation (6) implies \(k\mid2D\) for every sufficiently large \(k\).
Choose such a \(k>2D\). It forces \(D=0\).
Every nonnegative summand then vanishes, so every increment equals \(d=a_1=b_2\).
Using the empty-tuple cut in (2) now gives
\[
                 b_{2k}=kb_2,\qquad 2b_n\le b_{2n}=nb_2. \tag{8}
\]
S10 says \(b_2=0\), including the critical index \(|m|=2\).
Hence every \(b_n=0\), and the ordinary kernels are rotation invariant.
No bound strictly below 4 is used. Without (6), the convex sequence \(a_k=\max(0,k-1)\) would survive.

## 4. Local translations across a coordinate cut

Split a compact separated tuple into products \(F_-,F_+\), below and above a strict coordinate cut \(x_j=0\).
Choose \(a,b>0\) smaller than their respective distances from the cut.
In the coordinate-\(j\) Hilbert space set
\[
 \Phi=[\tau_{-ae_j}\theta_j\overline{F_-}],\qquad
 \Psi=[\tau_{-be_j}F_+],\qquad d=a+b.
\]
These are products of separated test fields, not coincident point fields.
Reflection and common translation invariance in the Hilbert dictionary give, for small real \(z\),
\[
 \sigma(F_-\cdot\tau_zF_+)
 =\langle\Phi,e^{-(d+z_j)H_j}U_{z_\parallel}\Psi\rangle. \tag{9}
\]
Indeed, reflecting the first vector translates \(F_-\) by \(ae_j\).
The second vector becomes \(\tau_{ae_j+z}F_+\); the common translation cancels.

For any real \(v\in\mathbb R^4\), put \(z=sv\).
On joint spectral values \((E,p)\), O6 gives \(|p_r|\le E\) for each \(r\ne j\).
Thus the spectral exponential has modulus at most \(e^{-\eta E}\), where
\[
 \eta=d+v_j\Re s-\sum_{r\ne j}|v_r|\,|\Im s|>0.        \tag{10}
\]
On a smaller domain take \(\eta\ge\epsilon>0\).
Writing \(L=\sum_r|v_r|\), the \(q\)-th derivative is bounded in operator norm by
\[
 L^q\sup_{E\ge0}E^qe^{-\epsilon E}\le L^q q!\epsilon^{-q}.
\]
The last inequality follows from the \(q\)-th term of \(e^{\epsilon E}\).
The spectral power series therefore converges in norm for \(L|h|<\epsilon\).
Equation (9) is holomorphic in \(s\), locally uniformly for fixed vectors.
No complex translation of a test function is asserted.

## 5. Removal of exceptional support

Write \(\mathcal C_n=\{x\in(\mathbb R^4)^n:x_i\ne x_l\ (i\ne l)\}\).
Let \(T_n\) be the moment distribution there, supplied by the common setting.
For a planar rotation \(R_u\), define
\[
 D_u(f_1\otimes\cdots\otimes f_n)
 =\sigma(f_1,\ldots,f_n)-\sigma(R_uf_1,\ldots,R_uf_n),
 \qquad R_uf(x)=f(R_u^{-1}x).                            \tag{11}
\]

First take a configuration with distinct original and rotated times.
Choose product boxes preserving both strict time orders.
Within these boxes, smooth slot tests admit plate approximations \(\sum\alpha(t,u)\varphi(x_2,x_3)\) in \(C^1\).
To construct them, extend a compact smooth test periodically inside a larger box and use its Fourier series.
Multiply by fixed product cutoffs supported in the chosen box and equal to one near the test support.
Integration by parts gives coefficient bounds \(C_N(1+|q|)^{-N}\) for every \(N\).
For derivative order \(r\) in \(D\) variables, choose \(N>D+r\).
The absolute shell sum is bounded by \(C\sum_{j\ge1}j^{D+r-1-N}<\infty\).
Thus the series converges in every derivative, with \(D=4\) for slot tests and \(D=4n\) for full tests.
Each Fourier term factors between the plane and transverse coordinates.
Equation (8) and the ordinary-chart representation give equality for these plates.
The local \(C^1\) bound passes equality to slot tests.
The same Fourier construction on product boxes approximates general tests by sums of slot tensors.
It converges in every derivative, proving \(D_u=0\) as a distribution on this ordinary open set.

Fix any \(y\in\mathcal C_n\).
For each coordinate, put threshold cuts halfway between successive distinct levels of \(y_1,\ldots,y_n\).
Together they separate every pair of indices. Each cut has a positive distance from every point.
Choose a product neighborhood \(W\subset\mathcal C_n\) and \(0<u_0<\pi/3\).
Make them small enough that every cut preserves its index partition for both \(x\) and \(R_ux\), throughout \(W\), whenever \(|u|<u_0\).
This follows by bounding rotation displacements and box widths below one quarter of the smallest cut distance.
All cuts then retain uniform positive gaps in both frames.

Fix \(|u|<u_0\), and count time ties by
\[
 q(x)=\#\{i<l:x_{i,4}=x_{l,4}\}
      +\#\{i<l:(R_ux_i)_4=(R_ux_l)_4\}.                \tag{12}
\]
The subsets \(\{x\in W:q(x)\le q_0\}\) are open: the finitely many existing inequalities persist locally.
We induct on \(q_0\), starting with the ordinary set \(q_0=0\).

At a point with \(q=q_0>0\), select a tied pair and a fixed common cut separating it.
Let \(A\) be the positive side of that cut. Translate precisely those slots by \(se_4\).
Cross-group time differences have slopes \(\pm1\) in the original frame and \(\pm\cos u\) in the rotated frame.
Both are nonzero. Internal differences remain unchanged.
For sufficiently small nonzero \(s\), old nonzero differences remain nonzero and all cross-group ties disappear.
At least the selected tie disappears, so the count decreases.

Choose one such \(s_*\), an interval \(I\) about it, and a smaller product neighborhood \(V\) of the point.
Keep its translated boxes in \(W\), preserve every old nonzero difference, and remove every cross-group tie for all \(s\in I\).
Any remaining ties came from internal pairs counted at the original point.
Thus every translated configuration has \(q\le q_0-1\) on \(I\).
The induction hypothesis makes (11) zero there for arbitrary slot tests supported in \(V\).

As a function of \(s\), their difference is holomorphic near the segment from zero to \(I\).
For the first term use (9)–(10) with \(v=e_4\).
For the second use the same common cut and \(v=R_ue_4\), since \(R_u\tau_{se_4}=\tau_{sR_ue_4}R_u\).
Shrink the segment if needed; both gaps then give a connected complex neighborhood satisfying (10).
The identity theorem carries its zero values on \(I\) to zero.
Tensor density gives \(D_u=0\) throughout \(V\), completing the induction.
Since \(q\le n(n-1)\), it terminates.

Thus \(D_u=0\) on \(W\) for every \(|u|<u_0\).
This also covers coincident plane projections whose transverse coordinates differ.
It removes possible distributions on all time-tie sets, not merely their values on a dense ordinary set.

## 6. All angles, all planes, and diagonal-flat tests

Let \(F\in C_c^\infty(\mathcal C_n)\) and fix an angle \(v\).
Its supports under rotations between zero and \(v\) have compact union in \(\mathcal C_n\).
Cover this union by finitely many neighborhoods \(W\) from Section 5.
Take the minimum of their positive angle bounds and divide \(v\) into smaller increments.
At each increment a smooth partition of unity on that cover gives equality on the current support.
Composing these equalities proves invariance through \(v\).
Smooth approximation in fixed separated neighborhoods and O2's local bound then give every compact separated \(C^1\) tuple.

Hypercubic conjugation gives this result in each of the six coordinate planes.
These rotations generate \(\mathrm{SO}(4)\): rotate pairs of rows to clear entries below each diagonal, choosing positive pivots.
Orthogonality leaves the identity matrix; determinant one fixes the final diagonal entry.
Reversing these row operations expresses the original matrix as a product of plane rotations.
One coordinate reflection, already in O2, gives the other component of \(\mathrm O(4)\).
The empty moment is constant. The one-point moment is \(c\int f\), hence invariant.
Restoring a mean to a centered field expands into finitely many lower moments and factors \(c\int f_i\).
Each factor is invariant, so the same conclusion holds before centering.

Let \(\Delta_n=\bigcup_{i<l}\{x_i=x_l\}\) and let \(\mathcal S_{\Delta,n}\) denote Schwartz functions flat there.
Use the existing continuous extension \(\Sigma_n\) specified in Section 1.
For clarity, the required density argument is by hand.
Cut off a flat Schwartz test at large radius; its tails vanish in each Schwartz seminorm.
Next multiply by a smooth cutoff that vanishes within distance \(\epsilon\) of \(\Delta_n\).
It can be a product of pair cutoffs in \(|x_i-x_l|^2/\epsilon^2\).
Derivatives of total order \(r\) cost at most \(C_r\epsilon^{-r}\).
Flatness and Taylor's formula give an arbitrary factor \(\epsilon^M\) on their supports.
Thus the error in any fixed seminorm of order \(s\) is \(O(\epsilon^{M-s})\); choose \(M>s\).
The remaining test has compact support away from \(\Delta_n\).
Partition it into product boxes with separated slot supports and use the Fourier construction of Section 5.
This gives finite sums of separated smooth tensors converging in every Schwartz seminorm, by a diagonal choice of errors.

Simultaneous rotations preserve \(\Delta_n\) and flatness.
They act continuously on Schwartz space: the chain rule bounds each transformed seminorm by finitely many original ones.
Apply the already proved invariance to the tensor approximants and pass through \(\Sigma_n\)'s continuity.
Therefore \(\Sigma_n(RF)=\Sigma_n(F)\) for every \(F\in\mathcal S_{\Delta,n}\) and \(R\in\mathrm O(4)\).
This proves invariance of the given extension; no new growth estimate is needed.

## 7. Dimension and the first input

The polygon and convexity proofs remain planar; transverse labels now have two coordinates instead of one.
The four-dimensional plate bound is 5, giving \(b_n\le5n/4\) and increments at most two in (7).
Divisibility itself is unchanged. It uses finiteness of that band, never the unavailable strict bound below 4.
The translation estimate now sums three tangential spectral coordinates in (10).
The exceptional-set argument uses all four coordinate cuts, including cuts separating equal plane projections.
Fourier tensor approximation uses \(4n\) variables and the summability choice stated in Section 5.
The final group has six coordinate rotation planes.

**First failing input within the stated conditional setting: none.**
For an unconditional theorem, the first unavailable source input remains rooted **D1**, whose cited construction starts at **C1/OH1**.
S10 also retains **TU10** as a premise, and **E1** must supply the cutoff sequence.
These are the upstream limits in the AK and TU Results; AC does not discharge them.

## Result

**S9 and S10, in their stated common moment setting, imply S11 in \(d=4\).**
The hand proof gives polygon divisibility, \(M(2k)=kM(2)=0\), local analytic translations, and removal of exceptional support.
All orders are \(\mathrm O(4)\)-invariant on separated compact \(C^1\) tuples and their existing continuous diagonal-flat extension.
The band constant 5 is sufficient; no sharper plate bound is assumed.
Proved here by Codex as a conditional research statement; not yet checked by the other model.
No computer-assisted deduction, audit, or scientific status is claimed. The upstream inputs and T0 remain open.
