# Factorial growth on diagonal-flat tests (row 188)
Provenance: Codex (GPT-6; exact variant and runtime effort not exposed; requested effort max), checkout `4c89161c00abdeef3b2bc041f1aea342c208ed7b`, Sussman–Alpoge commit `31a47c543775`. Research text; not an audit; grants no status.

## 1. Claim and named premise

Conditional on D2, every existing separated-tuple limit has a unique diagonal-flat extension satisfying
\[
 |S_n(\varphi)|\le C^n(n!)^{k+32}p_{20n}(\varphi),\qquad
 p_r(\varphi)=\max_{|\beta|\le r}\sup_x
 (1+|x|^2)^{r/2}|\partial^\beta\varphi(x)|.                 \tag{1}
\]
Here \(n\ge1\), and \(C\) is independent of \(n\), cutoff, state and support positions.
Set \(S_0(1)=1\). Thus the requested prefactor \(c\) can be one.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
The construction below rebuilds their YM4 QF1–QF22 (L24920–25381), H1 (L4572), and constrained density (L31589).
Their YM3_I, Propositions IV-25-55 and IV-26-24/37, and Lemma IV-26-17, supply the three-dimensional comparison.
Both manuscripts were read at the commit above. This note proves the implication by hand; no run supplies a proof step.

Write \(\Delta_n=\bigcup_{i<j}\{x_i=x_j\}\).
The domain \(\mathcal S_{\Delta,n}\) consists of Schwartz functions whose every derivative vanishes on \(\Delta_n\).
For \(n=1\), it is the full Schwartz space.

**D2 is a premise**, including its one-point comparison clause (SA L4138–4162, GS12–GS13 at L24290–24332).
For radius-one supports at separation \(\delta>0\), its cumulant bound is
\[
 |K_r(f_1,\ldots,f_r)|\le a^r(r!)^k
 \max(1,\delta^{-5r})\prod_i\|f_i\|_\sharp,
 \qquad k\ge1.                                           \tag{2}
\]
For \(r=1\), use the centered one-point difference bound.
Centering is at the specified reference state; other states need not have zero first moment.

Here is the passage from cumulants to moments without an extra factorial.
For a partition \(\pi\) of \(n\), \(\prod_{D\in\pi}|D|!\le n!\), and
\[
 \begin{aligned}
 \sum_\pi\prod_{D\in\pi}(|D|!)^k
 &\le(n!)^{k-1}\sum_{m=1}^n\frac{n!}{m!}\binom{n-1}{m-1}\\
 &\le2^{n-1}(n!)^k.                                      \tag{3}
 \end{aligned}
\]
For the equality used here, order the blocks, choose their positive sizes, then assign their labels.
There are \(\binom{n-1}{m-1}\) size lists, and each contributes \(n!\) after multiplication by the block factorials.
Divide by \(m!\) to forget their order.
The moment–cumulant partition formula and (2) therefore give
\[
 |S_n(f_1,\ldots,f_n)|\le b^n(n!)^k
 \max(1,\delta^{-5n})\prod_i\|f_i\|_1,\qquad
 \|f\|_1=\max(\|f\|_\infty,\|\nabla f\|_\infty).           \tag{4}
\]
The fixed norm equivalence and the \(2^n\) real/imaginary expansion only enlarge \(b\).
Alternatively, D2's full-moment clause GS12 gives (4) directly.
For each fixed tuple, taking its limit preserves (4).
The same applies to components realized as limits of the all-state centered moments.
No existence of these limits or component realization is proved here.
Below, numerical constants may increase after each estimate; the final \(C\) depends only on \(b\) and the fixed cutoffs.

## 2. Cutoffs and tensor consistency

We use cutoffs in \([0,1]\) with derivative bound \(C^q(q!)^2\) for \(q\ge1\).
Here is their construction.
Set \(a(t)=e^{-1/t}\) for \(t>0\), and zero otherwise.
On \(|z-t|=t/2\), \(\Re(1/z)\ge2/(9t)\); hence
\[
 |a^{(q)}(t)|\le q!(2/t)^q e^{-2/(9t)}
 \le C^{q+1}(q!)^2.
\]
The last inequality maximizes \(t^{-q}e^{-c/t}\) and uses \((q/e)^q\le q!\).
The derivatives tend to zero at the join.
Put \(s(t)=a(t)/(a(t)+a(1-t))\), extended by zero and one beyond \([0,1]\).
Its denominator is at least \(e^{-2}\) there.
The reciprocal has the same derivative bound: differentiating \(DH=1\) gives, after factorial division,
\[
 \frac{|H^{(q)}|}{(q!)^2}
 \le d_0^{-1}\sum_{r=1}^q
 \frac{|D^{(r)}|}{(r!)^2}
 \frac{|H^{(q-r)}|}{((q-r)!)^2}\binom qr^{-1}.
\]
If \(|D^{(r)}|/(r!)^2\le AB^r\), induction closes with
\(|H^{(q)}|/(q!)^2\le d_0^{-1}L^q\) and \(L=B(1+2A/d_0)\).
Indeed, \((A/d_0)\sum_{r\ge1}(B/L)^r\le1/2\).
Leibniz's rule now gives the stated bound for \(s\) and its fixed products.

Choose an even cutoff \(\eta\), one on \([-1,1]\), zero outside \([-2,2]\), using \(s(2-|t|)\) in between.
Put \(\psi(t)=\eta(2t)\) and \(\chi_1(t)=\psi(t)/\sum_{z\in\mathbb Z}\psi(t-z)\).
The denominator is at least one, with at most three local terms.
Thus \(\sum_z\chi_1(t-z)=1\).
In four dimensions put
\[
 \chi(u)=\prod_{a=1}^4\chi_1(u_a),\quad
 \chi^+(u)=\prod_{a=1}^4\eta(u_a),\quad \zeta=1-\chi^+.
\]
These retain the derivative bounds; \(\chi^+=1\) on \(\operatorname{supp}\chi\).
For a product of \(N\) such factors at scale \(h\), Leibniz gives
\[
 |\partial^\beta F|\le(CN)^q(q!)^2h^{-q},\qquad |\beta|=q. \tag{5}
\]
The multinomial coefficients sum to \(N^q\), and the product of derivative-order factorials is at most \(q!\).
Undifferentiated factors cost one. Thus (5) contains no \(C^N\) loss.
Pair differences introduce only signs in this argument.

Tensor relations are consistent with the supplied multilinear forms.
For a finite relation, choose \(\delta\) below all its support separations.
Partition each slot into sets of diameter less than \(\delta/8\).
If two slot sets have distance below \(\delta/2\), every original tensor has a zero localized factor.
Otherwise the slot spaces are separated, and ordinary multilinearity defines a map on their algebraic tensor product.
That tensor product embeds in functions: on each finite-dimensional factor span, point evaluations span its dual.
Choosing an evaluation basis in each slot recovers every tensor coefficient.
Thus a zero function has zero value; summing the localization proves the assertion.

## 3. Local Fourier construction

Let \(0<h\le1/16\), \(\ell=h/64\), and let expanded slot cubes
\(Q_i^+=c_i+[-2\ell,2\ell]^4\) have separation at least \(h/2\).
Each fits in a unit ball.
For \(u\) supported in \(\prod_i(c_i+[-\ell,\ell]^4)\), expand on cubes of period \(8\ell\).
On \(Q=\prod_i(c_i+[-4\ell,4\ell]^4)\), the coefficients are
\[
 \widehat u(\mathbf v)=(8\ell)^{-4n}\int_Q u(x)
 \exp\!\left(-\frac{i\pi}{4\ell}\sum_i v_i\cdot(x_i-c_i)\right)dx.
\]
In variables \(y_i=(x_i-c_i)/(4\ell)\), integration by parts with
\(\prod_i(1-\pi^{-2}\Delta_{y_i})^4\) gives
\[
 |\widehat u(\mathbf v)|\le C^nJ_{8n,\ell}(u)
       \prod_i(1+|v_i|^2)^{-4},\qquad
 J_{q,\ell}(u)=\max_{|\beta|\le q}\ell^{|\beta|}
                        \|\partial^\beta u\|_\infty.       \tag{6}
\]
Each slot operator has a fixed coefficient sum; their product costs only \(C^n\).
Multiply the Fourier exponentials by \(\chi^+((x_i-c_i)/\ell)\).
Their norms are at most \(C\ell^{-1}(1+|v_i|)\), and their supports are separated.
The sum
\(\sum_{v\in\mathbb Z^4}(1+|v|)(1+|v|^2)^{-4}\) is finite:
the shell \(|v|_\infty=r\ge1\) contributes at most \(Cr^3r^{-7}=Cr^{-4}\).
Consequently (4) defines an absolutely convergent linear sum \(T(u)\), with
\[
 |T(u)|\le(Cb)^n(n!)^k h^{-6n}J_{8n,\ell}(u).             \tag{7}
\]

These Fourier series converge with every derivative.
Indeed, extra integrations by parts give absolute convergence for each differentiated series.
Product Fejér kernels identify its sum with the original function.
In one period, \(F_N(t)=N^{-1}|\sum_{r=0}^{N-1}e^{i\pi rt}|^2\) has normalized integral one by orthogonality.
For \(\varepsilon\le|t|\le1\), the geometric sum gives
\(F_N(t)\le[N\sin^2(\pi\varepsilon/2)]^{-1}\).
Thus its mass concentrates at zero; products retain this property in each fixed dimension.
Uniform continuity controls the near part; vanishing kernel mass controls the far part.
For a tensor, the coefficients factor, and the one-slot sums converge in \(C^1\).
Multilinearity and (4), applied to the telescoping difference, show that \(T\) has the given tensor value.

The local functionals agree on overlaps.
Cover any compact overlap by smaller product boxes whose expanded closures stay inside it.
Their Fourier tensors converge in every derivative and are evaluated identically by both functionals.
Their finite-order bounds (7) pass this equality to the limit.
A finite partition of unity and a common refinement now glue them to \(T\) on \(C_c^\infty(\Delta_n^c)\).
Partitioning each entry of a larger separated tensor into small pieces shows that \(T\) retains all prescribed tensor values.

## 4. Extension and the factorial loss

Set \(h_j=2^{-j}/16\), \(\ell_j=h_j/64\), and
\[
 P_h(x)=\prod_{i<l}\zeta((x_i-x_l)/h),\quad
 D_0=P_{h_0},\quad D_j=P_{h_j}-P_{h_{j-1}}\ (j\ge1).
\]
Off the diagonals, \(\sum_jD_j=1\).
A fine layer, including the support of its derivatives, has
\[
 h_j\le\min_{i<l}|x_i-x_l|_\infty\le4h_j.                \tag{8}
\]
Use the product partition \(\chi_{j,z}(x)=\prod_i\chi(x_i/\ell_j-z_i)\).
Retain only boxes where \(\chi_{j,z}D_j\) is nonzero.
At a point of such a box all pair distances in the sup norm exceed \(h_j\).
Thus its centers have separation at least \(h_j-2\ell_j\).
Its expanded cubes have separation at least \(h_j-6\ell_j>h_j/2\), so (7) applies.

There are at most \(Cn^2\) cutoff factors.
Equation (5), at order \(8n\), has cost
\[
 (Cn^2)^{8n}((8n)!)^2\le C^n(n!)^{32}.                  \tag{9}
\]
Indeed, \(n^{16n}\le e^{16n}(n!)^{16}\), by integrating \(\log t\).
Also \((8n)!/(n!)^8\le8^{8n}\), since this multinomial coefficient counts some words of length \(8n\).
Squaring the second estimate accounts for the other sixteen factorial powers.

For \(x\) on a fine layer, replace one member of a closest pair by the other.
The resulting point \(y\) is diagonal, and \(|x-y|\le8h_j\le1/2\).
All jets vanish at \(y\).
For \(|\beta|\le8n\), take \(m=10n+2\) in the one-dimensional Taylor remainder along this segment.
Only four coordinates change, with total displacement at most \(16h_j\).
Since \(8n+m\le20n\), it gives
\[
 |\partial^\beta\varphi(x)|
 \le\frac{(16h_j)^m}{m!}\,C^{20n}
       (1+|x|^2)^{-10n}p_{20n}(\varphi).                 \tag{10}
\]
For the weight, every segment point \(w\) satisfies
\(1+|x|^2\le3(1+|w|^2)\).
Thus all constants in (10) grow only exponentially in \(n\).

Put \(u_{j,z}=\chi_{j,z}D_j\varphi\).
In \(J_{8n,\ell_j}\), the scaled derivative factor cancels every cutoff derivative's power of \(h_j^{-1}\).
Remaining positive powers of \(h_j\) are at most one; Leibniz costs at most \(2^{8n}\).
Equations (9)–(10) therefore give
\[
 J_{8n,\ell_j}(u_{j,z})\le C^n(n!)^{32}h_j^{10n+2}
 p_{20n}(\varphi)
 \sup_{x\in\operatorname{supp}\chi_{j,z}}(1+|x|^2)^{-10n}.
                                                               \tag{11}
\]
On the coarse layer omit \(h_j^{10n+2}\) and use the ordinary Schwartz bound.
This also handles \(n=1\), when every fine layer is zero.

Position summation costs exactly \(C^nh_j^{-4n}\).
To see this, use
\[
 (1+\textstyle\sum_i|x_i|^2)^{-10n}
 \le\prod_i(1+|x_i|^2)^{-10},\qquad
 \sum_{z\in\mathbb Z^4}(1+|\ell z|^2)^{-10}\le C\ell^{-4}.
                                                               \tag{12}
\]
For the latter bound, compare the value at each center with the integral over its side-\(\ell\) cube.
Their weights have a fixed ratio because \(\ell\le1\).
The integral is finite: its exterior radial bound is \(C\int_1^\infty r^{3-20}\,dr\).
The same comparison controls the supremum inside each partition box.
Taking the product proves the claimed position sum without a factor depending on \(n^2\).

Combining (7), (11), and (12) yields
\[
 \sum_z|T(u_{j,z})|\le C^n(n!)^{k+32}p_{20n}(\varphi)
              h_j^{10n+2-6n-4n}
 =C^n(n!)^{k+32}p_{20n}(\varphi)h_j^2.                  \tag{13}
\]
The coarse bound lacks \(h_j^2\); its fixed powers of \(h_0\) enter \(C^n\).
Since \(\sum_{j\ge1}h_j^2<\infty\), define
\[
 \Sigma_n(\varphi)=\sum_{j\ge0}\sum_zT(u_{j,z}).           \tag{14}
\]
The absolute bound proves (1) and continuity.
On compact off-diagonal tests the sum is finite, and the partition identity makes it equal to \(T\).
Thus it has every prescribed separated tensor value.

## 5. Constrained density and uniqueness

Let \(Q_R(x)=\prod_i\chi^+(x_i/R)\), with \(R\ge1\).
For fixed \(n,r,L\), Leibniz and the extra Schwartz weight give
\[
 p_r((1-Q_R)\varphi)\le C_{n,r,L}R^{-L}p_{r+L}(\varphi).
                                                               \tag{15}
\]
Every contributing term has some \(|x_i|\ge R\); cutoff derivatives cost \(R^{-1}\).
For the diagonal cutoff, a contributing term has a pair within \(2h\) in the sup norm.
Taylor to that diagonal, with \(M\) extra derivatives, and (5) give
\[
 p_r((1-P_h)\varphi)\le C_{n,r,M}h^{M-r}p_{r+M}(\varphi).
                                                               \tag{16}
\]
Choose \(M>r\).
First use (15), then (16) on the compact cutoff.
This approximates \(\varphi\) by compact smooth tests supported away from all diagonals.
Cover each support by finitely many small product boxes.
Their Fourier partial sums from Section 3 converge with all derivatives and retain one compact support.
They are finite sums of smooth compact separated tensors.
Successively make the errors small in the first \(1,2,\ldots\) seminorms to obtain one Schwartz-convergent sequence.
This proves density and uniqueness of (14), independently of all cutoff and Fourier choices.

For the positive-time subspace, all jets also vanish wherever some time coordinate is nonpositive.
Use
\[
 B_h(x)=\prod_{i=1}^n s(x_{i,4}/h-1).
\]
It vanishes when some time is at most \(h\), and equals one when all times are at least \(2h\).
Where a derivative of \((1-P_hB_h)\varphi\) contributes, a pair is close or a positive time is at most \(2h\).
Taylor to the corresponding diagonal or zero-time hyperplane proves (16) with \(P_hB_h\) in place of \(P_h\).
Thus \(Q_RP_hB_h\varphi\) gives the required compact approximation.
Choose its Fourier boxes with expanded closures strictly above time zero.
All their tensor factors then have strictly positive-time supports.

The boundary introduces no extra growth loss.
Replace \(P_h\) by \(P_hB_h\) in Section 4.
Every fine layer has a pair distance or time at most \(4h\), and all retained expanded boxes stay positive.
There are still at most \(Cn^2\) cutoff factors.
Taylor moves at most four coordinates, so (9)–(13) hold unchanged.
Uniqueness identifies this construction with the restriction of \(\Sigma_n\).

If the compact moments are reflection positive, that property also extends.
A reflected negative-time test tensored with a positive-time test is flat on every cross diagonal.
At positive common time the negative factor vanishes; at negative common time the positive factor vanishes.
At zero both have vanishing jets. Internal diagonals are already flat.
Moreover, \(p_r(f\otimes g)\le p_r(f)p_r(g)\), because
\(1+|x|^2+|y|^2\le(1+|x|^2)(1+|y|^2)\).
Approximate each component of a finite positive-time sequence by the tensors above.
Its finite reflection-positive quadratic form converges by (1) and this tensor inequality; hence its limit is nonnegative.
This uses compact reflection positivity as an additional premise, not as a consequence of D2.

## 6. What changes in four dimensions

The first failed input in a literal YM3_I port is its Fourier summability majorant at derivative order \(4n+1\).
In three dimensions it decays as \((1+|v|_\infty)^{-(3n+1)}\), after paying for the tensor norms.
In four dimensions its shell sum instead has the divergent power \(\sum_{r\ge1}r^{n-2}\).
The \(8n\) slotwise derivatives in (6) repair this step.
YM3_I's position weight \((1+|u|^2)^{-2}\) also has a logarithmically divergent integral in four dimensions.
Equation (12) replaces it with an integrable weight.

The grid now costs \(h^{-4n}\), rather than \(h^{-3n}\).
D2 costs \(h^{-5n}\), and the tensor norms cost \(h^{-n}\).
Thus Taylor order \(10n+2\) leaves \(h^2\), while the total derivative order is
\(8n+10n+2\le20n\).
Equation (9) records the full factorial loss; no factor \(e^{cn^2}\) is hidden in it.

## Result

**D2 implies QF3 and H1 for every existing separated limit:**
\[
 \boxed{c=1,\qquad k_{\mathrm E}=20,\qquad
        \kappa_{\mathrm E}=k+32.}
\]
The extension is unique on the diagonal-flat space, with the same constants for the stated all-state component limits.
Constrained tensor density holds, including the positive-time boundary.
This fills the implication S2 → S5 → O3 of the T0 skeleton.

First failing input in this implication: none, once the full named D2 premise and the separated limit are supplied.
D2 itself remains assumed; its upstream D1 source estimates are not established here.
The three-dimensional summability failure is repaired in Section 3.
No extension to unrestricted Schwartz tests or contact terms is claimed.
Proved by Codex, not yet checked by the other model. This does not establish T0.
