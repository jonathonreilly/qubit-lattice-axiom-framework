# F-measure and F-contour: pass 2

Provenance: Codex (GPT-6), 2026-11-04, pass 2 of Claude's `f-meas-draft.md`, checkout `cf64a26d19eef6b3a4fb58f5dd1d7fb018ccb749`. Research text, not an audit; grants no status. Written proofs only. Not yet refereed.

This checks and distils our draft. It does not correct the Sussman–Alpoge text.
The coarea identity, the change of reference, and the fixed-boundary deformation hold.
The draft does not establish its full stored-presentation or actual-conditional-mean claims.
Their remaining obligations are marked **Outstanding** below.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
SA means [`YM4_sketch_500.tex`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex),
CA-I means [`theorem_0_complete_account_raw_I.tex`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex),
and Y3 means [`YM3/YM3_I.tex`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex), all at `31a47c543775`.
The averaging, gauge and stage methods originate with Tadeusz Bałaban.
The literature search in `lit-balaban.md` and `lit-large-field.md` was reused.
No assertion below depends on a numerical calculation.

## 1. Setting and imports

Use ST1's finite, aligned four-dimensional geometry, with odd \(L\ge13\).
Fix one passing stage, its retained rows, and its new datum \(W=D_+\).
Write \(E,C,F\) for removed rows, added rows and free removed rows.
There is one pivot \(p(c)\) for each \(c\in C\), and \(F=E\setminus p(C)\).
Put \(g=g_j>0\), \(\delta'=\delta'_j\), \(b=\delta'/g\), and \(N=|F|\).
The map \(F_{\rm av}\) takes old data to new data; the letter \(F\) alone denotes free rows.

The following imports have exactly the scope stated in `st1-r4.md`:

* **GEO, CH and F2:** the regional pivot graph and its full-coordinate converse.
  In particular \(q_V(a)=K_Va+R_V(a)\), \(K_Vh_V=I\),
  \(K_V\mathsf C_V=0\), \((\mathsf C_Vu)|_F=u\), and
  \(a_V(u)=\Psi_V(\mathsf C_Vu)\), where
  \(d(t)=R_V(t-h_Vd(t))\) and \(\Psi_V(t)=t-h_Vd(t)\).
  The radii are \(r_1,r_u,r_{\rm sol}\); \(\|a_V(u)\|\le C_{\rm ch}L^4\|u\|\).
  Each pivot equation contains only its own pivot. The bounds hold uniformly in the admitted complex reference chart.
* **A1/F0/REG, OPS/SLICE/UNQ, DR and (15):** the critical orbit, its continuation,
  uniqueness, and the stated physical response and derivative bounds. They are not proved here.
* **AV/CURV, PROF/RCG4, RUN, RUN-low, ST-test and LOC:** as in ST1 §§2 and 7.
  Real LOC is required throughout the real chart used below, in the same representative and gauge.
* **GEO-slot [new input]:** CA-I's independent collar bonds (74314–74316) are exactly \(F\),
  and its rim integration bonds (74317–74320) are the recorded rim slots of this stage.
  The correspondence includes orientations, units, fixed parameters and recorded transports.
  It asserts a correspondence of variables, not equality of densities or Gaussian forms.
* **ST-test\(^{\rm hol}\) [new input]:** the localized-datum rule is holomorphic and real on real data.
  Both backgrounds use Amendment CV. On a fixed raw-datum ball of radius \(r_{\rm hol}>0\),
  contained in their admitted continuation charts, their relative row logarithm is holomorphic
  and bounded by a fixed \(M_*>0\). This ball has a real slice on which LOC holds.
  Data in use have coordinates \(X+iY\), with \(\|X\|<r_{\rm hol}/4\) and \(\|Y\|\le C_Qr_1(i)\).
  Here \(r_1(i)\) is ST1's running radius, not the fixed F2 radius \(r_1\).
  The fixed ball and bound are part of the input. Holomorphy of a boundary rule alone
  does not prove that its patched datum remains admitted.

The outline index was read before its source passages: chunks 07, 09 and 16,
their neighbouring rows and `obligations.md`; CA-I's index README and chunk 10.
SA QC22–QC25 already prove the local pivot/coarea calculation, conditionally on their chart bounds.
SA 9669–9676 permits the mean representative. The stage reconstruction is stated or sketched;
CA-I 54290 cites Bałaban's stage formula. Y3 supplies the coarea and contour proof templates.
The new work here is the check of our proposed identification and its ST1 use.

## 2. F-measure

Identify traceless Hermitian matrices with \(\mathbb R^3\) using the Pauli basis.
Set \(Q(a)=\tfrac12\operatorname{tr}a^2\) and
\(s(z)=(\sin\sqrt z/\sqrt z)^2\), defined by its entire power series.
For Haar probability measure, \(\sigma_H=1/(2\pi^2)\) in these coordinates.
Indeed \(SU(2)=S^3\), whose polar volume is \(\sin^2r\,dr\,d\Omega_2\);
its total volume is \(4\pi\int_0^\pi\sin^2r\,dr=2\pi^2\). Division gives
\[
 d(e^{ia}V)=\sigma_Hs(Q(a))\,d^3a,\qquad
 \delta_G(e^{iv})=\sigma_H^{-1}\delta_{\mathbb R^3}(v).
 \tag{FM1}
\]
These formulas apply in the injective ball \(|a|<\pi\). Only the density coefficients,
not a measure or delta distribution, are continued to complex arguments.

### FM2. Local coarea

Fix a real reference \(V_0\), with \(W_0=F_{\rm av}(V_0)\). On a sufficiently small open set put
\[
 t=\mathsf C_0u+h_0v,\quad a=\Psi_0(t),\quad
 \Lambda_0(u,v)=e^{ia}V_0,\quad W=e^{iv}W_0.
\]
Then \(F_{\rm av}(\Lambda_0(u,v))=W\) and the free entries of \(a\) equal \(u\).
For every nonnegative Borel \(f\) supported in this chart,
\[
 \int f(D)\,dD=\int dW\,\mu_W[f],
\]
where the fibre integral is over the chart preimage and
\[
 \mu_W[f]=\sigma_H^N
 \frac{\prod_{c\in C}\det J_c(V_0)^{-1}}{\prod_{c\in C}s(Q(v_c))}
 \int du\,\det D\Psi_0(t)\prod_{e\in E}s(Q(a_e))\,f(\Lambda_0(u,v)).
 \tag{FM2}
\]

**Proof.** F2 gives \(q_0(\Psi_0(t))=K_0t=v\).
The map \((u,v)\mapsto t\) has inverse \(t\mapsto(t|_F,K_0t)\)
and determinant \(\prod_c\det J_c^{-1}\).
The inverse of the straightening is \(a\mapsto a+h_0R_0(a)\), by its fixed-point equation.
Thus the composite is a diffeomorphism on a smaller neighbourhood.
Real determinants are positive: the pivot matrices, in unitary frames, are near \(L^{-3}I_3\),
and \(D\Psi\) is joined to the identity through invertible matrices.
Apply (FM1) to every old row and then to every new row.
The latter supplies \(dW=\sigma_H^{|C|}\prod_cs(Q(v_c))\,dv\).
Ordinary changes of variables and Tonelli give (FM2). ∎

### FM3. The continuous fibre kernel; normalization

At \(W_1\), choose any real in-fibre reference \(V\), and put \(u=gB\).
The resulting local kernel is
\[
 d\nu_W(B)=(\sigma_Hg^3)^N z_V\,
 \det D\Psi_V(\mathsf C_VgB)\prod_{e\in E}s(Q(a_V(gB)_e))\,dB,
 \qquad z_V=\prod_c\det J_c(V)^{-1}.
 \tag{FM3}
\]
Its pushforward to configurations is independent of the in-fibre reference on common chart regions.
It is the unique local coarea kernel continuous on compactly supported continuous tests.
It is generally **not a probability conditional law**.

**Proof.** In (FM2) based at \(V\), set \(v=0\), and use \(du=g^{3N}dB\).
On overlapping charts both fibre integrals of a compactly supported continuous test are continuous in \(W\).
Their difference integrates to zero against every continuous function of \(W\), by (FM2).
Haar measure has positive density, so the continuous difference vanishes at every \(W\).
Equality on continuous tests implies equality of the Radon measures.
An exhaustion by compact supports handles a whole open chart; a finite cover is not assumed.

For a fixed nonnegative stored density \(\omega\), let
\(p_\omega(W)=\nu_W[\omega]\). Where \(0<p_\omega(W)<\infty\),
\[
 \mathbb P_\omega(dD\mid W)=\frac{\omega(D)\,d\nu_W(D)}{p_\omega(W)},
 \qquad F_{{\rm av}*}(\omega\,dD)=p_\omega(W)\,dW.
 \tag{FM3n}
\]
This is verified by integrating a test function and using (FM2).
No normalization is needed in a stored Haar/delta integral. ∎

### FM4–FM6. Coordinate uniqueness and reference changes

**FM4.** If \((Cu)|_F=u\) and \(K_VCu=0\), then \(C=\mathsf C_V\).
If also \(q_V(a)=0\), \(a|_F=u\), \(\|a\|<r_{\rm sol}\) and \(\|u\|<r_u\),
then \(a=a_V(u)\).

**Proof.** The pivot values of \(Cu-\iota u\) must be
\(-J_c^{-1}(K_V\iota u)(c)\); this determines \(C\).
The nonlinear assertion is F2's small-solution converse. ∎

**FM5.** Let \(V'\) be another real free-row reference in the same logarithm chart;
it need not be in the fibre. Set
\[
 u(B')_e=i^{-1}\operatorname{Log}(e^{igB'_e}V'_eV_e^{-1}),\quad
 \Pi_V(u)=z_V\det D\Psi_V(\mathsf C_Vu)
                      \prod_{c\in C}s(Q(a_V(u)_{p(c)})).
\]
On the common chart,
\[
 d\nu_W=(\sigma_Hg^3)^N\prod_{e\in F}s(g^2Q(B'_e))\,
                \Pi_V(u(B'))\,dB'.                         \tag{FM5}
\]
**Proof.** In (FM3) separate the free-row Haar measures from \(\Pi_V\).
Each free-row measure is unchanged by replacing \(e^{iu_e}V_e\) with \(e^{igB'_e}V'_e\).
This gives (FM5), including the full change-of-reference Jacobian.
Continuation of its coefficient identity is holomorphic on a common complex chart. ∎

**FM6.** Under GEO-slot and the same constraint/pivot chart, CA-I's collar coordinate
in 81735–81756, 81829 is \(B\) when \(V^{(j)}=V\).
Its full logarithm is \(\Psi_V(\mathsf C_VgB)\), not \(gB\) on pivot rows.
For a different reference, use (FM5) on the overlap.

**Proof.** CA-I keeps \((CB)|_F=B\) and removes the linearized constraints.
FM4 identifies \(C\). The pivot correction solves the same small nonlinear constraint,
so FM4 identifies it as well. If two new backgrounds represent the same regular orbit,
they differ by a gauge residual for \(M_+\). Covariance gives
\(F_{\rm av}(M_-(U_+^w))=D_+\), so both are in-fibre references.
Orbit equality does not put them in a common small chart; (FM5) requires that chart separately. ∎

### Theorem FM. Exact real stage rewrite

Let \(\mathfrak a\) denote the recorded rim coordinates. Keep the actual stored integrand
\(\Theta(\mathfrak a,D)=\Xi(\mathfrak a,D)e^{\mathcal A(\mathfrak a,D)}\) fixed.
It includes every earlier normalizer, Gaussian weight, gauge factor, strip Jacobian and test.
For nonnegative Borel integrands, the passing Haar/delta operation is exactly
\[
 I(W)=\int d\mathfrak a\int\chi_\sharp(D(B))\Theta(\mathfrak a,D(B))\,d\nu_W(B),
 \qquad D(B)=e^{ia_V(gB)}V.                               \tag{FM}
\]
The formula is local to the passing chart; ST-test and F4 put its support there.
It is also an identity after integration against \(f(W)dW\).
The failing operation keeps its original integrand with \(1-\chi_\sharp\).

Here is exact Gaussian bookkeeping without identifying unlike constants.
Define **new chart factors**
\[
 E_{\rm ch}=N\log(\sigma_Hg^3),\quad z_{\rm elim}=z_V,
\]
\[
 J_{\rm rel}(B)=\sum_c\operatorname{tr}\log
  [I_3-J_c^{-1}\partial_{t(p(c))}d(c)]_{t=\mathsf C_VgB}
       +\sum_{e\in E}\log s(Q(a_V(gB)_e)).                  \tag{FMd}
\]
These logarithms use continuation from zero. The matrix logarithms converge because their
matrix increments have norm below \(1/2\). This does not assert that each determinant
itself is within \(1/2\) of one. For the Haar logarithms use
\(|s(Q(a))-1|\le C_s\|a\|^2<1/2\), from the convergent power series on a fixed ball.

For any declared split \(\mathcal A=\mathcal W+\mathcal K\), and symmetric forms \(S_a,S_B\), put
\[
 K_{\rm inc}=\mathcal K(\mathfrak a,D(B))-\mathcal K(0,V),
\]
\[
 P_{\rm rem}=\mathcal W(\mathfrak a,D(B))-\mathcal W(0,V)
       +\tfrac12\langle\mathfrak a,S_a\mathfrak a\rangle
       +\tfrac12\langle B,S_BB\rangle+J_{\rm rel}(B).
\]
Then (FM) equals
\[
 e^{\mathcal A(0,V)+E_{\rm ch}}z_{\rm elim}
 \int d\mathfrak a\,e^{-\langle\mathfrak a,S_a\mathfrak a\rangle/2}
 \int dB\,\chi_\sharp\Xi\,
             e^{-\langle B,S_BB\rangle/2+P_{\rm rem}+K_{\rm inc}}.       \tag{FMg}
\]

**Proof.** FM2–FM3 give (FM), and Tonelli handles the rim variables.
Pivot independence makes the determinant the product of the blocks in (FMd).
Insert that identity in (FM), then add and subtract the two quadratic forms.
Their contributions cancel exactly. No rim variable or stored weight has been removed. ∎

**Outstanding FM-match.** This closes the real measure change for the specified Haar/delta operation,
including SA 17531 with its full stored density. It does not prove term-by-term equality with a
separately frozen CA-I (1.60) by assigning its symbols new values.
CA-I's \(\mathfrak K^{(n)}\) is specifically the increment of
\(A^{(n)}+g_j^{-2}A\) at its specified shifted background.
The draft instead put gauge exponents and stored rim weights into its \(\mathcal K\),
then called its increment the same \(\mathfrak K^{(n)}\). Those definitions need not agree.
The older \(z^{(j)}\) in SA 17531 is already a stored factor; it must not be overwritten by \(z_{\rm elim}\).
To close the stronger F-measure identification, match the actual shifted background,
old normalizers, gauge factors, rim form and remainder allocation to (FMg).
SA 7487 confirms the Jacobian convention for its local small-field identity;
it does not perform this whole stage matching. GEO-slot alone does not do it either.

### FM7. A pivot Haar factor cannot be dropped

For a nontrivial stage with an added row and a free internal bond in its double block,
omitting the pivot Haar product from (FM3) changes the integral for some nonnegative Borel test.

**Proof.** At the identity choose a free positive \(e_\mu\)-bond on the segment from
the initial block centre towards its pivot. In SA QC15 its contribution to the initial
contour term is nonnegative, its straight-segment contribution is at least \(L^{-4}\),
and the final block's contour term does not read it.
Thus \(K_I\iota u\) is nonzero for a one-colour value on this bond.
Since \(J_c(I)=L^{-3}I_3\),
\(a_I(tu)_{p(c)}=-tJ_c^{-1}(K_I\iota u)(c)+O(t^2)\ne0\) for some arbitrarily small real \(t\).
Use the mirrored bond if the new block is the final block.
The same nonzero coefficient persists on a sufficiently small neighbourhood of the identity.
For the admitted regular real references, Lemma 3's auxiliary real gauge puts the double block
in that neighbourhood after a fixed curvature ceiling, using AV/CURV.
Unitary covariance conjugates the input and output coefficient and preserves its nonvanishing.
On an open neighbourhood of this point the pivot angle is nonzero and less than \(\pi\).
There \(0<(\sin r/r)^2<1\); every other real Haar factor is positive and at most one.
Integrating a nonzero nonnegative test supported there gives a strict difference.
No description of an analytic zero set as a submanifold is needed. ∎

## 3. Amendment CV and the Gaussian centre

A **new-member block** is an aligned level-\((j+1)\) block
\(B(y)\subset\Omega^+_{j+1}\setminus\Omega^-_{j+1}\).
GEO and the row convention put it inside \(\Omega_j\).
Its internal level-\(j\) bonds were old determining rows and are removed by this stage.
Every noncentre level-\(j\) site in it is an old node but no new node: lower-level rows
have no endpoints inside \(\Omega_j\), and higher-level row endpoints lie on the coarser grids.
Its new parent is \(y\). Pivots cross block faces, so internal bonds are free.
These are the regional geometry facts used below, as in ST1 Lemma 12 and SA QC18.

**Amendment CV.** Select each canonical background by setting
\((\mathcal M^nU)(z,x)=I\) at every nonnode with parent \(z\), using the contour mean.
Use this convention for towers, localized references and the stored transports already defined by means.
Auxiliary comb gauges used only to prove curvature bounds remain available.
This is a changed representative and test convention; it is not equality of the old and new passing branches.

### Lemma CV. Port of the affected ST1 steps

Assume the imports in §1. The representative change preserves ST1's conditional proofs,
after fixed increases of its gauge constants and the subsequent fixed constants and ceilings.
The affected lines below refer to the pinned `st1-r3.md`.

**Proof.** At nodes set \(u=I\). Descending through each pillar, solve
\(u(x)=u(z)(\mathcal M^nU)(z,x)\).
Covariance makes the transformed mean equal to \(I\). Each nonnode has one parent,
so this constructs a unique residual gauge. The mean is holomorphic on the F2/AV branch,
real on real fields, local to its block, and equal to \(I\) on the identity field.
This is the construction in `a1-balaban.md` 2492–2524, including its summable conjugator bound.

1. **41, 128, 345, 1064:** replace the representative definition and its A1 and Lemma 5 uses.
   REG is an orbit/local-gauge condition. Real uniqueness, centre independence by the identity theorem,
   and restriction modulo the smaller system's residual gauge use the same argument.
   SA 9676 does not transfer all its comb theorems automatically; the local port here is required.
2. **276–277:** the auxiliary tree gauge in Lemma 3 still kills tree bonds and proves its plaquette bound.
   It is not the selected representative. The Federbush contraction and AV iteration are unchanged.
3. **339:** LEV already pins means through (28). Its covariance identity, real tie and holomorphic
   forced-levelling argument are unchanged. It now pins the selected contour convention too.
4. **581:** for \(W_B=e^{i\eta H(B)}U_0\), with \(U_0\) mean axial, use
   \(u_B(x)=u_B(z)(\mathcal M^nW_B)(z,x)\).
   Each path has at most \(2(L-1)\) bonds. Product differentiation and the mean contraction give
   a fixed Lipschitz constant \(C_{\rm av}(L)\) for its relative change, on a smaller common ball.
   At zero its mean is \(I\), even when individual paths are not \(I\).
   The bound is therefore on the *change of the mean*, not on an arbitrarily selected path.
   The sum \(\sum_{n<q}2(L-1)\xi_n<2\xi_q\) bounds the product and its inverse by
   \(\exp(C\xi_q\sup|H|)\). Differencing the product gives
   \(|\Delta u_B(x)|\le C'_u\xi_q\sup|\Delta H|\).
   Both constants are fixed before \(\kappa\); no fixed loss is multiplied once per level.
   Thus (52), (49), CORE and all later half-gap/source budgets retain their form.
   The draft's numerical claim that exactly \(2C_u\) suffices was not proved.
5. **CRIT, DR and (15):** these are assumed at arbitrary admitted real regular bases.
   Apply them at the new mean base and its own raw datum; do not transfer old datum values.
   At a fixed base, if the target representative changes by \(w\),
   \((E^{u_B})^w=E^{wu_B}\). Thus the target gauge becomes \(wu_B\), not \(u_Bw\).
   Its top values stay fixed because \(w=I\) at nodes. The reduced response equations,
   multiplier algebra and independent-current identity do not change.

Formation and real drift use real gauge covariance and orbit restriction. The tower proof uses the
complex conjugator bounds just established. Lemma 12's kernel inclusion and pivot graph use the
actual average, which is unchanged. LEV still preserves every surviving stored slot.
These are all downstream uses touched by CV. No invariance of the soft gauge Hessian under an
arbitrary change of base is assumed. ∎

### FC3–FC5. Criticality, zero modes and the mean-axial stationary point

Let \(U_+\) be the new regular critical background and \(V=M_-(U_+)\).
Set \(\mathcal S(D)=S_{\Omega_0}(\Phi_-(D))\).
The derivative of \(B\mapsto\mathcal S(e^{ia_V(gB)}V)\) vanishes at zero.
Indeed its curve lies in the fixed \(M_+\)-fibre, by \(M_+=F_{\rm av}\circ M_-\).
At zero, uniqueness identifies its background with \(U_+\) modulo a residual \(M_-\)-gauge.
Criticality and gauge invariance annihilate that derivative. The identity theorem gives the complex version.

**FC4.** In a new-member block take a noncentre site all of whose incident bonds are internal.
Such a site exists for \(L\ge5\), hence for ST1's \(L\ge13\); the draft's \(L\ge3\) claim was false.
A gauge \(e^{is\lambda}\) at that site fixes coarse nodes and retained rows.
Its orbit is in the stage fibre, and \(\mathcal S\) is invariant on that orbit.
All its incident rows are free since pivots cross block faces.
For \(\lambda\ne0\) its tangent is nonzero.
Differentiating \(d\mathcal S_D(\xi(D))=0\) at the critical point gives
\(\operatorname{Hess}\mathcal S_V(\xi,v)=0\) for every fibre tangent \(v\).
Thus the Wilson Hessian alone has gauge zero modes. A strictly positive Gaussian precision
requires a gauge treatment; FC4 does not prove positivity of a particular gauge-fixed precision.

**FC5.** For this critical reference \(V\), put \(u(x)=V(y,x)\) on the noncentres
of the new blocks, \(u=I\) elsewhere, and \(V_{\rm ax}=V^u\).
Then \(V_{\rm ax}\) is in the same fibre, agrees on retained rows, and has \(V_{\rm ax}(y,x)=I\).
It is the \(M_-\)-datum of a gauge transform of \(U_+\) residual for \(M_+\).
For the soft gauge exponent
\[
 \Gamma(D)=x_j\sum_{(y,x)\in\mathcal P}[1-\tfrac12\operatorname{tr}D(y,x)],       \tag{FC5}
\]
use only the pairs \(\mathcal P\) actually carrying a factor.
If these varying pairs are in those blocks, \(d(\kappa_j\mathcal S+\Gamma)=0\) at \(V_{\rm ax}\).
The first term is stationary by gauge invariance. Each varying gauge term attains its real minimum zero
there, so has zero derivative. Under CV, \(V_{\rm ax}=V\), also on the complex chart by continuation.

The premise that \(V\) comes from the new critical orbit is essential.
An arbitrary point in its fibre does not become critical merely by axial gauge fixing.
Also, SA 7178–7181 inserts no factor where a mean is undefined. Gauge-factor coverage of a
particular stored stage, and its resulting precision, must be checked, not assumed from the notation \(\Gamma\).

### FC6. What the comb calculation does and does not prove

Take the central plaquette with vertices \(y,y+e_1,y+e_1+e_2,y+e_2\) in a new-member block.
In the comb order \((4,3,2,1)\), the two root bonds and the upper \(e_1\)-bond are \(I\).
The remaining bond \(e=(y+e_1,y+e_1+e_2)\) is \(e^{iF_p}\).
All four are free removed rows.
The two distinct paths to the opposite corner have products \(I,e^{iF_p}\), with equal weights.
Their small-branch mean is exactly \(e^{iF_p/2}\): substitution in the defining logarithmic equation gives zero,
and uniqueness of the mean applies. Hence
\[
 V_{\rm ax}(e)=e^{iF_p/2},\qquad
 i^{-1}\operatorname{Log}(V_{\rm ax}(e)V(e)^{-1})=-F_p/2.             \tag{FC6a}
\]
For the reversed comb order the corresponding row/sign is exchanged.
Let \(V^\sharp\) be the comb test reference and
\(h=\max_E|i^{-1}\operatorname{Log}(V(V^\sharp)^{-1})|\).
The real group distance gives
\[
 \left|g^{-1}i^{-1}\operatorname{Log}(V_{\rm ax}(e)V^\sharp(e)^{-1})\right|
       \ge (|F_p|/2-h)/g.                                          \tag{FC6b}
\]
Therefore \(|F_p|\ge2(\delta'+h)\) puts this **stationary point** outside the open test ball;
at equality it may be on its boundary. This local implication is exact.

**Outstanding FC6-history and FC-mean-match.** FC6 is not, as stated in pass 1, a proved counterexample
for the actual conditional mean of an admitted stored history.
A stationary point and the mean obtained by completing a specified quadratic form are different objects.
After a nonlinear change to test coordinates a Gaussian need not remain Gaussian.
One can choose a new Gaussian centred at (FC6b), putting the exact difference into its remainder;
that choice does not identify the old Gaussian or prove a bound on the new remainder.
Here a Gaussian mean means its centre before the cutoff. The expectation of a normalized positive
passing law cannot leave these convex balls: \(|\mathbb E Z_e|\le\mathbb E|Z_e|<b\).

For example, if the mean to a site is \(e^{i\alpha\tau}\), a gauge \(e^{is\tau}\)
at that site turns it into \(e^{i(\alpha-s)\tau}\), with \(\tau\) a unit Pauli matrix.
The associated gauge term on this commuting orbit is \(x_j[1-\cos(\alpha-s)]\).
Its stationary point is \(s=\alpha\).
The quadratic Taylor polynomial at \(s=0\) has centre \(s=\tan\alpha\), for \(|\alpha|<\pi/2\).
Thus stationarity alone does not identify even that quadratic centre exactly.
For a stored quadratic form with exterior coordinate \(a\),
\[
 \tfrac12 B^{\mathsf T}SB+B^{\mathsf T}Ra+\ell^{\mathsf T}B
 \quad\hbox{has centre}\quad -S^{-1}(Ra+\ell).                       \tag{FC6c}
\]
Nothing in a representative choice sets \(R\) or \(\ell\) to zero.
Stored forms may instead be assigned to the remainder, as in `shift-map.md` §14;
this is exact bookkeeping, with a separate analytic bound to prove.

There is no constructed nonzero-weight admitted history satisfying FC6's antecedent in the draft.
Three checks distinguish the issues. First, the local four-bond example proves the gauge geometry,
but does not produce a constrained critical background or a history. Second,
\(\varepsilon_j/\delta'_j\to\infty\) shows compatibility of upper bounds, not existence.
Third, invoking A1 for chosen regular data supplies an orbit, but neither prescribes this interior plaquette
nor verifies the older tests, failures, slot support and stage selection.
Those history rules are deliberately supplied inputs in ST1, not a specified probability law there.
They could exclude such data without violating their upper bounds.
Thus an admitted-history realization is **not established**, and impossibility is not established either.
The exact missing witness is a nonzero-weight passing history, its new critical datum, and its
matched quadratic form satisfying (FC6b) and the stated threshold.
The draft's further claim that no alternative Gaussian split can work is withdrawn.

## 4. F-contour in test coordinates

Under CV put
\[
 \eta_e=i^{-1}\operatorname{Log}(V_e(V_e^\sharp)^{-1}),\quad
 Z_e=g^{-1}i^{-1}\operatorname{Log}(D_e(V_e^\sharp)^{-1}),\quad
 u_e(Z)=i^{-1}\operatorname{Log}(e^{igZ_e}e^{-i\eta_e}),\quad m_e=\eta_e/g.
 \tag{FC0}
\]
Then \(u(m)=0\). The norm of \(\eta\) agrees with the discrepancy used in F4,
since reversing its product takes the inverse on the same logarithm branch.

**FC1 (exact new test).** Assume \(h=\|\eta\|\le\delta'/8\) at real data and
\[
 \tfrac98\delta'<r_u,\qquad
 \tfrac98C_{\rm ch}L^4\delta'+\delta'/8<r_{\rm sol}/4.                \tag{FC1}
\]
The ST-test passing domain in the fibre is exactly
\(D_b=\{Z\in(\mathbb R^3)^F:|Z_e|<b\}\).
Indeed the free test is its definition. The real group triangle inequality gives
\(|u_e|<9\delta'/8\); F2 and (FC1) make every pivot test automatic.
Conversely, ST-test bounds all logarithms relative to \(V\) by
\(r_{\rm sol}/4+h<r_{\rm sol}/2\). F2's converse then identifies the same graph. ∎

**FC2 (fixed-domain identity and its precise analytic premise).** At real data, (FM5) gives
\[
 I(W)=(\sigma_Hg^3)^N\int d\mathfrak a\int_{D_b}dZ\,
 \prod_{e\in F}s(g^2Q(Z_e))\Pi_V(u(Z))
 \Theta(\mathfrak a,e^{ia_V(u(Z))}V).                                \tag{FC2}
\]
For fixed Borel parameters, if the full integrand remaining after the new test is removed
is jointly holomorphic in \(Z,W\) on a neighbourhood of the integration contours,
and the outer integral has a locally uniform integrable majorant, this formula is holomorphic in \(W\).
It is the unique continuation on a connected chart containing an open real slice.
To prove this, integrate the Cauchy formula under the common majorant; uniqueness follows by
successive one-variable identity theorems at a real point and then connectedness.
A bounded integrand alone is insufficient on an unbounded rim domain. ∎

**Outstanding FC-test.** The cited ST1 inputs do not supply FC2's premise for every stored stage.
They retain older indicators exactly. F4 and CI give holomorphic coordinate maps and activities,
not holomorphy of an older indicator depending on \(Z\).
Such an indicator may be retained as a Borel parameter only if it is independent of moved coordinates,
or proved redundant there. The outline's older-test implication at 17369–17396 and 17624
is the relevant additional statement; F7 explicitly does not prove it for the designed ST-test.

This is a real obstruction to the proposed inference, not a boundary regularity convention.
In one coordinate, \(\int_{-b}^{b}\mathbf1_{\{|z+x|<b\}}\,dz=2b-|x|\) for \(|x|<b\).
The coordinate map is entire and the new domain fixed, but the result has no holomorphic extension at zero.
This example refutes that inference; it is not claimed to be a Yang–Mills history.

### FC7. Uniform smallness of the geometric centre

Under CV, ST-test\(^{\rm hol}\), real LOC, RUN and RUN-low,
\[
 |m_e|\le b/16                                                    \tag{FC7}
\]
at every datum in use after a ceiling on \(\gamma\).
This concerns the centre in (FC0), independently of any Gaussian identification.

**Proof.** F6 gives on the real chart
\(\|\eta\|\le H_{\mathbb R}=C_F e^{-aR_\sharp}\), with fixed \(C_F,a>0\);
for LOC-form, (15), AV and the shell sum (22) supply this bound.
Write the datum as \(e^{i(X+iY)}D^r\) in ST-test\(^{\rm hol}\)'s coordinates.
For \(y=\|Y\|>0\), restrict to \(D(\zeta)=e^{i(X+\zeta Y)}D^r\),
\(|\zeta|<R=r_{\rm hol}/(2y)\). Its coordinates have norm less than \(3r_{\rm hol}/4\).
Assume \(R>1\) by a coupling ceiling.
For any norm-one scalar linear functional of a row matrix, its value \(f(\zeta)\)
is bounded by \(M_*\) on this disc and by \(H_{\mathbb R}\) on its real diameter.
The map \((R+\zeta)/(R-\zeta)\) sends the upper half-disc to a quadrant.
Its logarithm has imaginary part in \((0,\pi/2)\).
The maximum principle applied to the logarithmic modulus, or to its regularization at zeros,
gives the two-boundary estimate
\[
 |f(i)|\le H_{\mathbb R}^{1-\alpha}M_*^\alpha,
 \qquad \alpha=\frac4\pi\arctan(1/R)\le\frac{8y}{\pi r_{\rm hol}}.
\]
One may first use a slightly smaller radius and then take its limit.
Taking the supremum of the scalar functionals proves the same matrix-norm bound.
With \(H_{\mathbb R}\le M_*\) and \(\alpha\le1/2\), it is at most
\(\sqrt{M_*C_F}\,e^{-aR_\sharp/2}\). For \(Y=0\) use the real estimate.
This avoids taking a logarithm of a matrix-valued function.

Finally \(R_\sharp\ge c_N\ell_t^r/4\), \(r>1\).
RUN gives \(|\theta_j-\theta_t|\le C\ell_t^r\) in the stage window,
so \(\theta_j/\theta_t\in[1/2,2]\) after a ceiling.
The quotient \(e^{-c\ell_t^r}/(A_1\theta_j^{-1/2}\ell_j^{p_1})\) tends uniformly to zero:
its logarithm has leading term \(-c\ell_t^r+\ell_t/2\).
Choose its supremum below the fixed required constant. This proves (FC7). ∎

### FC8–FC9. Tube and fixed-boundary deformation

Let \(T^\sharp_\rho=\{Z:|\Re Z_e|+|\Im Z_e|<\rho\}\).
If \(\|\eta\|\le\delta'/8\), \(2C_\ell\delta'\le1/2\), and the logarithm balls hold, then
\[
 Z\in T^\sharp_{2b}\quad\Longrightarrow\quad
 \|u(Z)\|<2\delta'+\delta'/8+\delta'/16<9\delta'/4.                  \tag{FC8}
\]
This is (24) applied to \(igZ,-i\eta\). It places \(u(Z)/g\) inside F4's tube,
with room for Cauchy estimates on the smaller test tube.

**FC9.** Let \(\Phi\) be holomorphic on a neighbourhood of the relevant closed tube,
bounded there, and let \(\nu=\Im m\), with \(|\nu_e|\le b/16\).
Put \(d_0=3/4\), \(r_-=7/16\), \(r_+=13/16\),
\[
 \phi(\beta)=\min\{1,\max\{0,2d_0^{-1}(r_+-|\beta|/b)\}\},\qquad
 T_\nu(\beta)_e=\beta_e+i\phi(\beta_e)\nu_e.
\]
Then
\[
 \int_{D_b}\Phi(\beta)d\beta
 =\int_{D_b}\Phi(T_\nu(\beta))\prod_e
    [1+i\langle\nu_e,\nabla\phi(\beta_e)\rangle]\,d\beta,             \tag{FC9}
\]
the image is in \(T^\sharp_b\), and each Jacobian factor has modulus at most
\(\exp(2/(16^2d_0^2))\). The contour is unchanged for \(|\beta_e|\ge r_+b\);
for \(|\beta_e|\le r_-b\), \(\Im(T_\nu(\beta)_e-m_e)=0\).

**Proof.** Where the bump is nonzero, \(|\beta_e|+|\nu_e|<(r_++1/16)b<b\).
Its real gradient has norm at most \(2/(d_0b)\).
The determinant is the rank-one determinant displayed in (FC9), and
\(\sqrt{1+a^2}\le e^{a^2/2}\) proves the bound.
For one bond align its first real coordinate with \(\nu_e\) and fix the two transverse coordinates.
The real interval is \([-a,a]\), \(a=\sqrt{b^2-|\beta_\perp|^2}\).
Its homotopy is \(\gamma_s(x)=x+is|\nu_e|\phi(x,\beta_\perp)\).
Both endpoints remain fixed. On each smooth piece,
\[
 \frac d{ds}\int_{-a}^a f(\gamma_s)\gamma_s'\,dx
 =\int_{-a}^a\partial_x[f(\gamma_s)\partial_s\gamma_s]\,dx=0.
\]
The piece boundaries cancel by continuity. Boundedness gives Fubini over the transverse coordinates
and over the finitely many bonds. This proves (FC9); the bulk assertion follows from \(\phi=1\).
For outer rim integration use FC2's common integrable majorant. ∎

### Theorem FC. Proved contour implication and the remaining matching

Under the stated inputs and ceilings, the designed ST-test has the exact domain (FC1),
the real identity (FC2), the small geometric centre (FC7), and the containment (FC8).
For an integrand satisfying FC2's analytic premise, (FC9) gives an exact deformation and continuation.
These assertions are uniform in parameters for which those premises and bounds hold uniformly.

At a CV critical reference, the Hessian \(S\) of \(\kappa_j\mathcal S+\Gamma\) in the
free coordinate \(\beta=u/g\) has zero linear term, by FC3–FC5.
One may use the Gaussian factor with centre \(m\) in test coordinates exactly by retaining
\[
 R_{\rm rec}(Z)=\tfrac12(Z-m)^{\mathsf T}S(Z-m)
                         -\tfrac12\beta(Z)^{\mathsf T}S\beta(Z)       \tag{FCr}
\]
in the remainder. The exponent then sums to the original one.
If \(S\) has row-sum bound \(s_1\), (24) gives
\(\|\beta-(Z-m)\|\le2C_\ell b\|\eta\|\) on \(T^\sharp_{2b}\), hence
\(|R_{\rm rec}|\le C s_1N b^2\|\eta\|\), with an absolute fixed \(C\).
This follows by factoring the difference of the two symmetric quadratic forms.
It estimates this correction only, not all stored terms.

**Outstanding F-contour.** Full closure for the actual stored stage still requires
**FC-mean-match** (its Gaussian, linear/seam terms, slot coupling and switch/external-pair dependence)
and **FC-test** (every remaining moved-variable factor satisfies the analytic premise).
CV alone proves neither. If a matched Gaussian has exactly the split (FCr), then its chosen mean has
\(m_r=0\), \(\theta_m=0\), \(\varepsilon_m=1/16\); otherwise its additional conditional force must be bounded.
The positive reference precision, its complex perturbation bound, and the full remainder bound
remain the NL1/LF1 inputs. CI is unchanged. No Gaussian estimate is proved by this contour identity.

## 5. Order of constants

First fix ST1's geometry, \(L\), exponents, CH/AV/A1/derivative constants, and fixed logarithm balls.
Fix \(C_s,C_\ell,C_{\rm av},C_u,C'_u\), the resulting tower/substitution constants,
\(r_{\rm hol},M_*\) of ST-test\(^{\rm hol}\), and \(C_F,a\) of real LOC before \(\kappa\).
The contour numbers \(1/16,1/4,3/4,7/16,13/16\) are absolute.
Then choose \(\kappa,\bar\kappa\), \(M\), BOX constants and test/running amplitudes in ST1's order.
The frame-increment bound may follow those amplitudes, as the referee required.
Finally choose one \(\gamma\)-ceiling for (FC1), (FC7), (FC8), all F2/F4 balls,
\(\alpha\le1/2\), and all inherited source budgets.
\(M\) enters the localization proof only through its lower bound on \(R_\sharp\).
No constant fixed before \(\kappa\) reads \(b_f,C_0,C_1,A_0,A_1\).

## 6. Source checks

The three raw files were fetched once to `/tmp/sa_ym4.tex`, `/tmp/sa_ca_I.tex`,
and `/tmp/sa_YM3_I.tex`. Only bounded ranges were read.
The requested line checks are:

| Passage | Checked content and limit |
|---|---|
| SA 7178–7181 | Soft block gauge uses contour means; factors are inserted only where defined. |
| SA 7487 (context 7479–7499) | Local coarea Jacobians enter the remainder. This is a local identity. |
| SA 9669–9676 | Both axial choices exist; Theorems 3 and 5 still refer to combs. |
| CA-I 54291–54300 | Two fluctuation integrals with specified forms and normalizers. |
| CA-I 81735–81756, 81829 | Relative collar logarithm, pivot correction and independent free entries. |
| Y3 46302–46386 | Integrated coarea, including pivot Haar factors and Borel tests. |
| Y3 52091–52134 | Boundary-fixed bump deformation; failed Borel variables stay fixed. |
| `a1-balaban.md` 2501 (context 2492–2524) | The recursion explicitly permits either contour variable. |

Additional bounded reads: SA 7133–7139, 7593–7619, 7658–7673,
8165–8241, 8255–8360, 8373–8381, 17355–17405, 17516–17564, 17583–17591, 17612–17630;
CA-I 54226–54335, 74309–74324, 78470–78591;
Y3 46258–46301, 51901–51950, 52060–52090.
They distinguish stored weights, conditional forces, gauge conventions and analytic premises.
No unread Bałaban definition is silently identified with an algebraically assigned name.

## Result

Proved from named inputs: FM2–FM6's local coarea and coordinate identities, Theorem FM's exact real
rewrite with all stored factors, FM7's necessity of pivot Haar factors, Lemma CV's ST1 port,
FC3–FC5's criticality statements, FC6's geometric implication, and Theorem FC's stated contour implication.
These are a check/correction of our draft and a use of the cited proof templates, not a correction of SA.

The imports are listed in §1; the contour also needs its explicitly stated analytic/majorant premise.
**FM-match, FC-mean-match, FC-test and FC6-history remain Outstanding.**
Thus full F-measure/F-contour for the previously specified CA-I presentation are not declared closed.
CI and the NL1/LF1 precision/remainder estimates are unchanged.

Corrections to pass 1: distinguished an unnormalized kernel from a conditional probability;
used local overlaps and compact exhaustion; kept existing normalizers distinct from new chart factors;
did not redefine CA-I's interaction bracket; required a common reference chart;
used matrix trace-log branches and a valid complex Haar bound; simplified FM7 to a direct open-set proof;
stated the new-member node geometry; corrected FC4's block size; restricted FC5 to a critical reference;
distinguished FC6's stationary point from an actual Gaussian mean and from the passing-law expectation,
and left history realization open;
removed its unsupported assertion about every Gaussian split; corrected gauge-composition order;
replaced the unproved factor-two CV bound by fixed Lipschitz/product bounds;
stated common holomorphic room for the localization argument and applied it to scalar functionals;
kept older Borel tests and outer-integral majorants explicit; retained the exact recentring correction.

All proofs are written by hand. Tools served only retrieval, text navigation, editing and consistency checks.
This is research text, not an audit, grants no status, and is **not yet refereed**.
