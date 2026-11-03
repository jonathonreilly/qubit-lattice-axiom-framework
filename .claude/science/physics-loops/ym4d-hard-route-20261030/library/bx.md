# BX: the critical box package (row 209)
Provenance: OpenAI Codex, GPT-6 family (exact deployment and runtime effort not exposed; requested effort: max); checkout `8fb4bd5e6a0ed7e8013d05814f88ee27ac84a8a9`; Sussman–Alpoge commit `31a47c543775`. Research text, not an audit; no status is granted.

## 1. Target and inputs

This note addresses (BX) in `b2-extract.md` Section 7. It is an input to B4's older-origin bound (19).
Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**.
Their pointed-window argument supplies the proposed method (SA 13427 onward; 15821–15826).
The box-first construction and WF-c implications retain their stated premises and authorship.

Write \(\sigma=L^{-(k-j)}\), \(a=\alpha_k\), and \(h=\alpha_H\in(0,1]\).
All distances below use level-\(j\) units. The required bounds, throughout the WF6 disc, are
\[
 B_z=\ell_z+E_z^H+E_z^N,\qquad
 |\nabla\ell_z|\le Ca\sigma^2,
\]
\[
 |E_z^H(x)|\le Ca\sigma^{2+h}|x-z|^{1+h},\qquad
 |E_z^N(x)|\le Cr_{B,j}^{-1}a^2\sigma^4(1+|x-z|)^2.
\]
The package also requires a box-to-infinite Hessian difference with moments
\(Cg_j\alpha_j^{-2}e^{-cM/\sigma}\).
Neither room nor the pointed quadratic cancellation alone proves these bounds.

## 2. The first input

The missing input is **SA (PW6), spatial Hölder regularity of the complete window field at scale \(k\)**.
It includes the unperturbed field (SA 15824–15825).
It is not the Hölder estimate for the response to level-\(j\) data.

The checked box-first identity keeps the actual datum map, including boundary rows (`wf7-bf.md` Section 2).
Rule W supplies containment (`cond-c.md` Theorem C2).
WF-c supplies the common complex chart, boundary comparison and core admission.
Its Theorem A uses (R4), which bounds first differences, and (R6), which bounds tower curvatures and currents.
Neither clause states (PW6).
SA derives (PW7)–(PW13) *from* (PW6); those formulas do not supply it.
Balaban uses an explicit Hölder hypothesis in CMP **109**, (3.32), to obtain (4.18).
That method is credited to Tadeusz Balaban.

The following example tests this input on the full local core used by Proposition W.
It uses a real input, independent current zero, and fluctuation datum zero.
The reconstructed box pair is still an actual constrained critical pair.

## 3. A real input in the core

Fix an admissible odd blocking factor \(L\ge3\) above the standing floors, and take \(j=1\), \(\xi_k=1\).
Then \(\sigma=L^{1-k}\) and the bare spacing is \(\eta=\sigma/L\).
Use a periodic torus of fixed, sufficiently large, even side in level-\(k\) units.
There are no seams. Put \(T=\operatorname{diag}(1,-1)\) and
\[
 A_2(x)=\varepsilon a\sigma\cos(\pi x_1/\sigma)T,
 \qquad A_1=A_3=A_4=0,\qquad U_b=e^{i\eta A_b}.
 \tag{1}
\]
The period divides the torus. All matrices commute.
The elementary inequality \(|\cos(u+v)-\cos u|\le |v|\) gives
\[
 |A|\le\varepsilon a\sigma,\quad
 |\nabla A|\le\pi\varepsilon a,\quad
 |\partial U-1|\le\pi\varepsilon a\eta^2.
 \tag{2}
\]
Thus \(P=(1,A,0)\), with \(U_+(P)=U\), satisfies (R4) for a fixed small \(\varepsilon>0\).
The last zero is the independent current; it need not equal \(J(U)\).
The real reference is the identity, so its real-gauge clause holds with potential zero.
The prescribed relation \(M\alpha_0\ll\alpha_1\) gives room for both bounds on \(A\) in (2).

Here is the hereditary check. It uses only real A1 and AV, already used by WF-c.
For a level-\(p\) restriction put \(\tau=L^{p-k}\le1\).
Its real curvature radius is \(b_p=\pi\varepsilon a\tau^2\).
The real argument of `a3-close.md`, Lemma T, Step 1, gives for either tower rule
\[
 |\partial U_n-1|\le Kb_p\eta_p^2,\qquad
 |J_n(U_n)|\le Kb_pL^{2(n-p)}.                 \tag{3}
\]
Specifically, AV makes its datum \(C_1L^2b_pL^{2(n-p)}\)-regular.
A1 multiplies that radius by \(B\); take \(K=BC_1L^2\).
On the inner region, converting curvature from scale \(n\) to scale \(p\) cancels \(L^{2(n-p)}\).
This proves (3), uniformly in the region, depth and both rules.
It does not use Lemma T's defective complex Step 3.

Choose \(\varepsilon\) with \(K\pi\varepsilon C_\alpha<1/4\), where \(a\le C_\alpha\alpha_{0,k}\).
Since \(\tau^2\le\tau\), (3) is below one quarter of both (R6) bounds.
All continuations exist by real A1 at the same regular data.
The towers of the identity reference are identically one.
The fixed change to level-\((k+1)\) input units costs only fixed powers of \(L\).
Decrease \(\varepsilon\) once to cover those powers and the adjacent-radius ratio.
Thus the half-core and the additional box-tower clause also hold, uniformly in \(k\).

Set the fluctuation datum \(B'=0\). The specified response then vanishes (`dec-field.md` Proposition 5.1).
Consequently \(\mathbf U_{t,\nu}=U\) on the entire WF6 disc, for every fine parameter.
Rule W supplies a top-layer box of radius comparable with \(M/\sigma\).
Its critical map exists and retains the prescribed interior datum exactly.

## 4. The datum contradicts (BX)

The actual one-step average (SA R3) can be computed exactly here.
In direction 2, endpoint contours cancel because (1) is independent of \(x_2\).
The straight segment contributes \(\sigma A_2\).
In direction 1, every contour contribution is odd in the transverse block coordinate \(x_2\), so its average vanishes.
Directions 3 and 4 give zero. Commutativity makes every logarithm an ordinary sum.
Hence, on interior level-1 bonds, in level-1 coordinates,
\[
 V_2(n)=e^{i\beta(-1)^{n_1}T},\quad V_1=V_3=V_4=1,
 \qquad
 \beta=\varepsilon a\sigma^2 c_L,\quad
 c_L=\frac1L\sum_{r=-(L-1)/2}^{(L-1)/2}\cos(\pi r/L)\ge\frac1L.
 \tag{4}
\]
Every cosine is positive, and the central summand is one.
All contour logarithms stay on their near-identity branches by the fixed choice of \(\varepsilon\).
The box constraints enforce exactly (4); rebuilding its critical field cannot smooth its prescribed datum.

Take \(z=0\). The unitary gauge \(g(n)=e^{i\beta n_2T}\) puts (4) in the coordinate axial gauge of PW7:
\[
 \widehat B_2(n)=\beta[(-1)^{n_1}-1]T,\qquad
 \widehat B_1=\widehat B_3=\widehat B_4=0.
\]
Thus \(\widehat B_2(0)=0\), \(\widehat B_2(e_1)=-2\beta T\), and \(\widehat B_2(2e_1)=0\).
Its second difference has norm \(4\beta\); every affine field has second difference zero.
The two bounds in (BX) would therefore imply
\[
 \frac{4\varepsilon}{L}
 \le 36C\sigma^h
       +64C\frac{a}{r_{B,1}}\sigma^2.                 \tag{5}
\]
The three bonds have distance at most 3 from \(z\), including a midpoint convention.
The absolute difference weights sum to 4; hence \(4\cdot3^{1+h}\le36\) and \(4(1+3)^2=64\).
Residual constant conjugation preserves this norm.

WF1 gives \(a/r_{B,1}\le C_0\sqrt{k}\).
Put \(m=k-1\). Then \(\sigma=L^{-m}\) and \(\sqrt{m+1}\le2^{m/2}\) for \(m\ge1\).
Both terms on the right of (5) tend to zero geometrically.
For any proposed uniform \(C\), choose \(m\) so their sum is below \(4\varepsilon/L\).
This contradicts (5). The calculation is entirely by hand.

Another axial ordering cannot remove the obstruction.
The plaquette holonomies at \(0\) and \(e_1\), transported to \(z\), are \(e^{-2i\beta T}\) and \(e^{2i\beta T}\).
Their difference has norm \(2|\sin(2\beta)|\ge2\beta\).
Every normalized coordinate axial gauge fixes the root bonds to one.
The proposed affine approximation therefore has size \(O(a\sigma^2)+O(E)\) on these plaquettes.
Expanding their four factors gives the same affine curl, with error
\(C[a\sigma^{2+h}+r_{B,1}^{-1}a^2\sigma^4+a^2\sigma^4]\).
Indeed the product remainder is at most \(e^S S^2/2\), where \(S\) sums the four bond-log norms.
This follows by integrating the second derivative of \(\prod_e e^{itB_e}\).
Division by \(a\sigma^2\) again gives a right side tending to zero.

## Result

**(BX) fails on the full admitted local cores, under the same real A1 and AV inputs used by WF-c.**
The first failing input is (PW6) for the complete field, including the unperturbed input.
The real core and all hereditary tests admit (1), but its actual box datum violates the affine remainder bound.
The Hessian comparison clause is not reached.

This does not refute SA's theorem conditional on (PW6), or B4's bound (19).
Our input is not critical at scale \(k\), and its zero-fluctuation window derivative vanishes.
Restricting to scale-\(k\) critical inputs, or adding a Hölder core condition, changes the required domain.
Either repair must supply the complex extension and preservation under the step.
The counterexample is by Codex, not yet checked by the other model. No scientific status is granted.
