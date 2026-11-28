# rf10-incr: the comparison between successive depths
Provenance: OpenAI Codex (GPT-6; exact backend identifier unavailable), effort max requested; commit `fe1de94201099f97c79df5dd573edbc1d2c2a32d`; Sussman–Alpoge commit `31a47c543775`. Research text, not an audit; grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, supply RF10 and RF14. Claude's `prefactor-loc.md` supplies Theorem S and Corollary T. Codex's `b-value.md` supplies Theorem V. The latter remains unexamined by the other model. Balaban's CMP **109**, 249–301, and **119**, 243–285, are the literature sources below. All arguments here are by hand.

## 1. The exact reduction

Write \(A_k=b[\Psi_k]\), \(A_0=0\), and \(z_k=L^{-2k}\). Theorem S and Corollary T give
\[
 b_k^0=A_k-A_{k-1},\qquad
 b_{k+1}^0-b_k^0=A_{k+1}-2A_k+A_{k-1}.                 \tag{1}
\]
Their substitution error is zero. No estimate of that error remains to prove.

Section 5 of `b-value.md` gives
\[
 A_k=F(z_k)+e_k,\quad
 F(z)=\widetilde\beta(z)-z\widetilde\beta'(z)
                  +\tfrac12z^2\widetilde\beta''(z),\quad |e_k|\le C_L.
                                                               \tag{2}
\]
Thus a bound on each \(e_k\) cannot replace a bound on its differences.
For example, \(A_k=kc_0+a((-1)^k-1)\), with \(a\ne0\), satisfies \(A_0=0\) and Theorem V's bound. Yet
\[
 b_k^0=c_0+2a(-1)^k,\qquad |b_{k+1}^0-b_k^0|=4|a|.
\]
This is a counterexample to that inference, not to the actual Yang–Mills sequence.

## 2. The explicit massive term does have a geometric error

The formulas in `b-value.md`, Section 6, give more than boundedness. Put \(\gamma=11/(6\pi^2)\). Then
\[
 F(z)=\gamma\log(1/z)+C_F+O(\sqrt z),\qquad 0<z\le1.       \tag{3}
\]
Here is the additional hand estimate. Write \(\rho=|q|\) on a fixed small momentum ball. The displayed Wilson numerators give
\[
 \widetilde\beta(z)=\tfrac{88}{3}I_2(z)+r(z),\qquad
 r(z)=\int\left(\frac{N_1(q)}{\psi(q)+z}
                    +\frac{N_2(q)}{(\psi(q)+z)^2}\right)
                    \frac{dq}{(2\pi)^4},
 \quad |N_1|\le C,\quad |N_2|\le C\rho.                    \tag{4}
\]
Explicitly, with the Wilson symbols \(S,T\) of that section,
\(N_1=-8\operatorname{tr}T+\tfrac12(\widehat q_1^2+\widehat q_2^2)\) and
\(N_2=4(\operatorname{tr}S^2-8)-\tfrac83(\cos q_1\cos q_2-1)\), where \(\widehat q_\mu=2\sin(q_\mu/2)\).
They are independent of \(z\) and retain the neutral Wilson term. Away from this ball all denominators have a fixed lower bound.

It suffices to treat \(z\le\delta^2\); the remaining compact mass interval has bounded derivatives. Split each integral at \(\rho=\sqrt z\), using \(c\rho^2\le\psi(q)\le C\rho^2\).
For the first denominator, the inner contribution to \(r(z)-r(0)\) is \(O(z)\). The outer contribution is bounded by
\(Cz\int_{\sqrt z}^{\delta}\rho^{-1}d\rho\).
For the second denominator, the corresponding bounds are
\(C\int_0^{\sqrt z}d\rho\) and
\(Cz\int_{\sqrt z}^{\delta}\rho^{-2}d\rho\).
For \(j=1,2\), differentiate the denominators and multiply by \(z^j\).
The first type is bounded by
\(C_jz^j\int_0^\delta\rho^3(\rho^2+z)^{-1-j}d\rho\).
The second is bounded by
\(C_jz^j\int_0^\delta\rho^4(\rho^2+z)^{-2-j}d\rho\).
The same split bounds these by \(Cz(1+|\log z|)\) and \(C\sqrt z\), respectively. Hence
\[
 |r(z)-r(0)|+|zr'(z)|+|z^2r''(z)|\le C\sqrt z.             \tag{5}
\]

For \(I_2\), replace \(\psi(q)\) by \(\rho^2\) inside the ball. Their difference is \(O(\rho^4)\). For its integral correction, the same split gives convergence to a constant with error \(O(z(1+|\log z|))\). Indeed, the inner difference is bounded by \(C\rho^{-2}\). The outer change from \(z=0\) is bounded by \(Cz\rho^{-4}\). Its differentiated integrands are bounded by
\(C_jz^j\rho^4(\rho^2+z)^{-3-j}\), for \(j=1,2\).
Radial integration gives the same error bound. The continuum integral is exactly
\[
 \frac1{16\pi^2}\left[
 \log\frac{\delta^2+z}{z}+\frac{z}{\delta^2+z}-1\right].
\]
Thus \(B(z)=\widetilde\beta(z)-\gamma\log(1/z)\) has a limit \(B_0\), and
\(|B(z)-B_0|+|zB'(z)|+|z^2B''(z)|\le C\sqrt z\).
Applying \(1-z\partial_z+z^2\partial_z^2/2\) proves (3), with \(C_F=B_0+3\gamma/2\).

Since \(2\gamma\log L=c_0\), equations (1)–(3) give, for \(k\ge2\),
\[
 b_{k+1}^0-b_k^0
   =e_{k+1}-2e_k+e_{k-1}+O_L(L^{-k}).                       \tag{6}
\]
The explicit massive trace therefore leaves exactly the second difference of the comparison remainder.

## 3. What the cited Balaban papers supply

CMP **109**, p. 259, Theorem 2 and the paragraph after (0.31), defer the perturbative coupling asymptotics to another paper. Page 264, (1.22), and p. 297, (5.42), define the coupling coefficient through a Hessian moment. CMP **119**, p. 262, Theorem 1, assumes bounds on the running couplings. Its (3.33)–(3.36), pp. 273–274, give the Gaussian determinant and its resolvent representation. These are not a proof of the comparison between depths required here.

The identities used from these sources have short direct proofs. Diagonalizing a positive finite precision \(K\) gives
\(\log Z=\sum_c\log z(c)-\tfrac12\log\det K+\mathrm{constant}\), retaining the pivot factors \(z(c)\).
Differentiating \(KK^{-1}=1\) gives \(dK^{-1}=-K^{-1}(dK)K^{-1}\). Thus, with \(G=K^{-1}\),
\[
 D^2(-\tfrac12\log\det K)[h,h']
 =-\tfrac12\operatorname{Tr}(G K_{hh'})
   +\tfrac12\operatorname{Tr}(G K_hG K_{h'}).                \tag{7}
\]
The derivative identity also holds for an invertible saddle matrix on its fixed logarithm branch.
For an absolutely summable Hessian kernel with two distance moments, termwise differentiation gives
\[
 b[\pi]=-\partial_1\partial_2\widehat\pi_{12}(0)
       =\sum_u u_1u_2\pi_{12}(u).                           \tag{8}
\]
These proofs justify the determinant calculus and extraction used below. No unproved coupling-convergence theorem is imported.

## 4. The first missing input

Identify the unit coarse lattices and exponential charts at successive depths. For an \(n\)-leg kernel, let \(t\) be the shortest tree length joining its legs. A sufficient weighted norm is
\[
 \|T\|_{m,2}=\max_i\sup_{b_i}\sum_{(b_j)_{j\ne i}}
             e^{mt}(1+t)^2\|T(b_1,\ldots,b_n)\|,
 \qquad m\ge0.
\]
Colour and direction indices have fixed finite dimension. The same norm applies to the saddle's site and constraint indices. Already \(m=0\) controls (8).

Here is the continuity requirement, stated conditionally. Suppose the actual triples and one-step saddle inverses have norms at most \(M\), uniformly in depth. Keep the actual one-step average and gauge vertices fixed in these units. Then RF14's Hessian depends Lipschitz continuously on the triple, with constant depending only on \(L,M\).

To prove this assertion, use
\(\widetilde G-G=-\widetilde G(\widetilde K-K)G\).
The weighted matrix norm is submultiplicative: the triangle inequality bounds the exponential weight, and
\(1+a+b\le(1+a)(1+b)\) bounds its polynomial part.
Thus the inverse difference is bounded by \(M^2\|\widetilde K-K\|_{m,2}\).
The response \(H\) is a block column of this inverse. The vertices \(V_3,V_4\) depend linearly on the corresponding action jets, plus the fixed constraint and gauge vertices.
Expand each product difference in RF14 by replacing one factor at a time. Each trace contraction is connected to an external leg. Root its sums there. The union of the factor trees spans its external legs, so their weights dominate the external weight. Successive absolute sums, with surplus loop factors bounded by their supremum, bound each contraction by the product of the factor norms. There is no free volume factor. This proves the claimed Lipschitz bound. Equation (8) preserves it after extraction.

Applying that lemma still requires, for every \(0<\alpha<1\), a common such norm with
\[
 \delta_k:=\sum_{n=2}^4
 \big\|D^n(\mathcal S_{k+1}-\mathcal S_k)(0)\big\|_{m,2}
       \le C_\alpha L^{-\alpha k}.                         \tag{9}
\]
Fixed Taylor factorials make (9) equivalent to the corresponding bound on \(\mathfrak J_{k+1}-\mathfrak J_k\).
RF14 would then compare \(b_{k+2}^0\) with \(b_{k+1}^0\); shifting the index gives RF10.

**First failed input in directly reusing Theorem V: smallness between meshes in its energy norm.** This premise is false even for its flat massive precision. Let \(\eta=L^{-k}\). Identify the old Fourier modes with the same modes on mesh \(\eta/L\), by the isometry \(I\). Write
\[
 P_\eta=K_{0,\eta}+1,\qquad W_\eta=P_\eta^{1/2},\qquad
 \psi_\eta(q)=4\eta^{-2}\sum_\mu\sin^2(\eta q_\mu/2).
\]
The direct energy-norm resolvent estimate would need a small bound on
\(W_\eta^{-1}(I^*P_{\eta/L}I-P_\eta)W_\eta^{-1}\).
Take \(q=(-\pi/\eta,0,0,0)\). This is an allowed Bloch alias: \(p_1=-\pi\) and \(n_1=-(L^k-1)/2\). It also occurs on a torus of side two in coarse units. On its normalized Fourier vector the last operator has eigenvalue
\[
 \frac{4L^2\sin^2(\pi/(2L))-4}{4+\eta^2}\ \ge\ 1.        \tag{10}
\]
Indeed, concavity of sine on \([0,\pi/6]\) gives \(\sin t\ge3t/\pi\). Since \(L\ge3\), the numerator is at least \(9-4=5\), and the denominator is at most five. Thus no bound \(C_\alpha\eta^\alpha\) holds in this norm. This is a hand counterexample to the smallness premise, not to (9).

A comparison after the actual averages could suppress these modes. Theorem V does not prove that comparison for the constrained Taylor triples. Its constant-curvature derivatives also do not determine the full cubic and quartic vertices. Differentiating the mass in \(F\) does not compare the depth-dependent averages or background responses in \(e_k\). Corollary T cancels the substitution error, without canceling this remainder. The cited Balaban passages supply no replacement for (9). I stop at the failure (10); the actual weighted comparison and its uniform continuity hypotheses remain unproved here.

## 5. Row 185: compare the actual averaged remainder

Continuation by OpenAI Codex, at `e3b29b44b90411632bf731eb63eae205bc288048`. Research text; all calculations below are by hand.

Take the remainder route in (6). Theorem V remains an input, not yet checked by the other model. Its stopped expansion contains the actual finite-rank perturbation
\[
 E_\eta=Q_\eta^*Q_\eta-D_\eta R_\eta^*R_\eta D_\eta^*.
\]
At zero flux put
\[
 g_\eta=(K_{0,\eta}+1)^{-1/2},\qquad
 X_\eta=Q_\eta g_\eta,\qquad
 Y_\eta=g_\eta D_\eta R_\eta^*.
\]
Then, exactly,
\[
 g_\eta E_\eta g_\eta=X_\eta^*X_\eta-Y_\eta Y_\eta^* .       \tag{11}
\]
Thus a comparison of the averaged factors must retain \(Y_\eta\). Dropping it drops the gauge correction.

The source check follows FINISH's item 5. Ethan Sussman and Levent Alpoge, with Claude and Codex as their text's authors, use these factors in `YM3_II.tex`, Section “Geometric convergence of the Gaussian one-loop coefficient”, at `31a47c543775`. Its Theorem III-12-105 states rate \(L^{-k/6}\); its averaging estimate `eq:loop-R-tail` has rate \(\Lambda^{-1/2}\). These are **unchecked** source statements, not a four-dimensional proof. Their `QED3.tex`, “Block averaging in Maxwell's theory”, supplies the linear minimisation setting. Neither excerpt supplies RF10's rate for every \(\alpha<1\).

Test a direct Lipschitz comparison of the stopped remainder using these factors. Let \(J\) extend common Fourier modes by zero to mesh \(\eta/L\). The input this route would use is
\[
 \sup_{p\in[-\pi,\pi]^4}
 \|Y_{\eta/L}(p)-JY_\eta(p)\|
       \le C_\alpha\eta^\alpha\qquad(0<\alpha<1),           \tag{12}
\]
together with its flux derivatives and the other determinant factors. This is a factor estimate for the proposed comparison, not a necessary consequence of RF10.

## 6. First failed input: the averaged factor comparison

**Equation (12) is false for every \(\alpha>1/2\).** This already fails at zero flux, with the actual site average.

Put \(N=\eta^{-1}=L^k\), \(h=\eta/L\), and fix the coarse momentum \(p=(\pi/2,0,0,0)\). Use one unit colour vector as the coarse input. The alias sets have coordinate bounds \((N-1)/2\) and \((LN-1)/2\). Thus
\[
 m=(n,0,0,0),\qquad (N+1)/2\le n\le N
\]
are added modes. There are \((N+1)/2\ge N/2\) of them. Their momenta are \(q_n=(\pi/2+2\pi n,0,0,0)\).

The flat symbols in `b-value.md`, Section 4, give
\[
 R_h(q_n)=\frac{h\sin(q_{n,1}/2)}{\sin(hq_{n,1}/2)},\qquad
 d_h(q_n)=2ih^{-1}\sin(hq_{n,1}/2),\qquad
 K_{0,h}(q_n)=|d_h(q_n)|^2 I.
\]
The other three averaging factors equal one. These formulas also follow by summing the centred geometric series. Midpoint phases have modulus one and do not affect this calculation. Since \(|\sin(q_{n,1}/2)|=1/\sqrt2\), the first component of \(Y_h\) on each added mode has modulus
\[
 \frac{|d_h(q_n)R_h(q_n)|}{\sqrt{1+|d_h(q_n)|^2}}
 =\frac{\sqrt2}{\sqrt{1+4h^{-2}\sin^2(hq_{n,1}/2)}}
 \ge \sqrt{\frac25}\,h\ge\frac h2.                       \tag{13}
\]
Here \(h\le1\) and \(|\sin|\le1\). The physical Fourier pairing makes these alias vectors orthonormal. The vector \(JY_\eta\) vanishes on every added mode. Therefore
\[
 \|Y_h-JY_\eta\|^2
 \ge\|(1-JJ^*)Y_h\|^2
 \ge\frac N2\frac{h^2}{4}
 =\frac{\eta}{8L^2}.                                      \tag{14}
\]
For \(\alpha>1/2\), (12) and (14) would imply
\(\eta^{1/2-\alpha}\le2\sqrt2 L C_\alpha\) for all \(k\). Its left side diverges. This proves the failure by hand.

This is a failure after averaging, beyond the unaveraged obstruction (10). It blocks the proposed factor estimate before flux differentiation. It does not bound the second difference of \(e_k\) from below: a trace can pair two small tails. Such trace estimates could bypass (12), but none is proved here. Per row 185, stop at this first failed input.

## Result

RF10's second clause remains **open**. Theorem S and Corollary T reduce it to (6); Theorem V bounds \(e_k\), without controlling its second difference. Row 185's first failed input is (12): the actual averaged gauge factor has the lower bound (14), excluding every \(\alpha>1/2\) in that norm. This does not refute RF10 or the Taylor comparison (9). A direct trace comparison of \(e_k\), or (9) with RF14's uniform bounds, remains unproved. This continuation is not checked by the other model and grants no status.
