# dec-field: the decoupled first system and the current-regularity obstruction
Provenance: OpenAI Codex (GPT-6; finer runtime model and effort identifiers are not exposed here; requested effort: max), source commit 109d75dfbc26922de045d388e9c0e9cc4984564b, Sussman–Alpoge commit 31a47c543775. Research text, not an audit; grants no status.

## 1. Contract and source discipline

Queue row 130, sa-ledger rank 4. The target is existence and weighted first response for R9 in the SA 10380–10404 first-order supremum norms, uniformly on the specified decoupling polydisc and in depth, mesh, volume and \(M_1\). The proposed bridge is a pointwise upgrade of the local-energy walk terms for the eight-unknown system.

**Outcome:** the proposed direct use of Lemma 6.1′ fails: an admissible independent current produces an unbounded pointwise coefficient in a scalar equation. Section 2 gives the configuration. Section 3 proves the smaller divergence/weak-form statements. Section 4 proves conditional decoupled **energy**, not supremum, bounds. Sections 5–6 give the exact conditional contraction and comparison implications, keeping their unproved pointwise premises visible. The requested uniform R9 field theorem is not proved or refuted here.

All repository references mean their versions at the source commit above. The relevant FINISH rows are 113, 116, 125, 126, 129 and 130. In particular:

- o1-decoupled.md is Claude's same-model research text with row 129's Codex gate pending at this pin. Its claims are named inputs, not independently established facts here.
- h-walk.md Lemma U is distinguished from its conditional Lemma L and Theorems W, T. The graph-norm, second-jet coefficient and tree-count repairs in h-walk-gate.md remain part of those hypotheses.
- p82-curved.md Proposition 6.2 concerns a different lift. a3-clauses.md Section 4.3 explicitly leaves the current correction and its transpose outside its completed pointwise package.
- wf-room-2.md Section 6 is read with wf-room-2-gate.md Section 6: the readout depends on the independent current through the actual propagators; its bounds require (O1) and the first-system field separately.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's regular-pair class, explicit current continuation, R9, norms and decoupling mechanisms. The outline was fetched once to /tmp/sa_ym4.tex at the requested commit. T. Balaban is credited for the local-inverse, differentiated-source and random-walk methods. The named library notes and their gate repairs retain their authorship and conditional standing. File retrieval and source comparisons below are bookkeeping, never mathematical discharge.

During writing another process switched this checkout from 109d75dfb to 6a1fad49b and the initially written untracked output disappeared. Comparison against the pin showed no change to the mathematical sources used here; FINISH.md changed. This note was restored from the session, with a recovery copy in /tmp/dec-field-109d75dfb.t9Awm1. No checkout, commit or other repository edit was made by this worker.

## 2. Counterexample to the proposed pointwise perturbation step

The unfolded form of h-walk Section 4 contains
\[
 c_J(A,\lambda)=\langle i[\lambda,A]-i[A,\lambda^+]
                         -i[\lambda,D\lambda],J\rangle_f .
 \tag{2.1}
\]
The regular-pair class (SA 10129–10137) bounds \(m^3|J|\) but imposes no difference bound on the **independent** \(J\). Its variation in \(\lambda\) is therefore materially different from a small bounded pointwise coefficient.

**Proposition 2.1.** There is no mesh-independent constant \(C\) making the current part of the unfolded local system a Lemma 6.1′-type pointwise first-order perturbation of size \(C\gamma _0\) on the stated class. The failure occurs with flat links, \(j=0\), fixed \(M_1\), and arbitrarily small positive \(\gamma _0\).

*Proof.* Set the local scale to one. One may take all nonempty regions \(\Omega_0,\ldots,\Omega_k\) equal to a sufficiently large torus with top scale one, and \(\eta=L^{-k}\). Separation is vacuous before forming the cut-down. Take \(U=\mathbf U=1\). Every potential, curvature and local-gauge condition holds identically.

Choose unit colour vectors \(Z,W,J_0\) with
\[
 b_0=\langle i[Z,W],J_0\rangle\ne0;
\]
the three Pauli directions give such a triple. Put \(a=\gamma _0/2\). In an interior patch set
\[
 J_1(x)=a(-1)^{x_1/\eta}J_0,\qquad J_\mu(x)=0\quad(\mu\ne1),
 \tag{2.2}
\]
and set \(J=0\) outside a slightly larger patch contained in the scale-one layer. This local definition does not require an even torus period. Everywhere \(m^3|J|\le\gamma _0/2<\gamma _0\), including its jumps. It is an admissible independent current, not the physical current of the flat connection.

Take \(A=0\) and a site function \(\lambda\) equal to \(Z\) near a point \(x\), cut off away from that neighbourhood. Vary it by \(v=W1_{\{x\}}\). On the two direction-1 bonds incident to \(x\), \(D\lambda=0\), while \(Dv\) is \(-W/\eta\) on the outgoing bond and \(W/\eta\) on the incoming bond. The physical pairing has cell volume \(\eta^4\), so direct differentiation of (2.1) gives
\[
 \eta^{-4}dc_J(0,\lambda)[0,v]
 =\eta^{-1}\langle i[Z,W],J_1(x)-J_1(x-\eta e_1)\rangle
 =\frac{2ab_0}{\eta}(-1)^{x_1/\eta}.
 \tag{2.3}
\]
The \(\lambda\lambda\) operator block of the symmetric quadratic form \(-c_J\) is half its gradient. Its pairing with \(W\) at \(x\) has magnitude \(a|b_0|/\eta\). This block occurs in the scalar dual slot of the \(Y\)-row of \(\mathbb K\). Subtract \(\mathbb K_0\) from \(\mathbb K_J\): at \(A=0\) all other current contributions to that slot vanish, so there is no cancellation.

On a fixed cube of side \(r\) inside the constant-\(\lambda\) patch, Lemma 6.1′ would require a bound by
\[
 C\gamma _0(r^{-2}|\lambda|+r^{-1}|D\lambda|)
 =C\gamma _0r^{-2}.
\]
Equation (2.3) exceeds it as \(\eta\downarrow0\). Rescaling components by fixed powers of the local scale or \(r\) cannot remove \(\eta^{-1}\). The point can lie inside the common interior of the original and cut-down systems, so the same obstruction holds in \(\mathbb K_\varkappa\). \(\square\)

The example can also satisfy the homogeneous scalar constraint subsystem. In a flat pillar take two translated smooth bumps with equal discrete sums and disjoint supports, subtract them, and multiply by \(Z\), leaving \(\lambda=Z\) near \(x\) and \(Q'\lambda=0\). Replace the globally zero \(A\) by \(A=D\lambda\). It is still zero on all stencils used in (2.3). With \(h=\mu=0\),
\[
 \mathbb X(h,\lambda,\mu)
 =(A_s\lambda,0,-Q'\lambda)=(\Delta\lambda,0,0)
 =(D^{\mathsf T}A,0,0)=\mathbb B A.
\]
Thus the \(Z\)-row of the unfolded system holds, while the same current coefficient remains of order \(\gamma _0/\eta\). No claim that all other homogeneous equations hold is needed for the coefficient test.

**Precise scope.** This disproves the proposed direct absorption of \(c_J\) in the pointwise hypothesis of Lemma 6.1′. It disproves neither the field bounds nor a mixed-system estimate retaining divergence sources. The outline itself flags a divergence-admitting source in mechanism (f), SA 10540–10546. More smoothing after eliminating auxiliary variables could still prove the field theorem.

## 3. The smaller true statements

**Lemma 3.1 (weak-form smallness).** Let \(B_J\) be the symmetric polarization of \(c_J\). In h-walk's energy and graph spaces,
\[
 |B_J((A,\lambda),(C,\mu))|
 \le C_L\gamma _0
 (\|m^{-1}A\|_2+\|\lambda\|_\Lambda)
 (\|m^{-1}C\|_2+\|\mu\|_\Lambda).
 \tag{3.1}
\]
It also holds locally with a fixed stencil enlargement. The constant is independent of mesh, depth, volume and \(M_1\).

*Proof.* A fixed finite-dimensional colour algebra satisfies
\(|[u,v]|\le c_{\mathfrak g}|u||v|\): expand in an orthonormal basis and apply Cauchy–Schwarz to its finitely many structure constants. Polarization gives
\[
 2B_J=\langle i[\lambda,C]+i[\mu,A]
 -i[A,\mu^+]-i[C,\lambda^+]
 -i[\lambda,D\mu]-i[\mu,D\lambda],J\rangle_f .
 \tag{3.2}
\]
The first term is at most
\[
 C\gamma _0\|m^{-2}\lambda\|_{2,\mathrm{endpoints}}
                  \|m^{-1}C\|_2.
\]
An endpoint is counted a bounded number of times and its scale differs from the bond scale by at most an adjacent-layer factor. Forward transport has norm at most \(e^{c_{\mathfrak g}\eta|A'|}\le e^{c_{\mathfrak g}\alpha_1}\); the real transport is unitary and the exponential series bounds the other factor. These observations prove the same estimate for the other three mixed terms. The last two are bounded respectively by
\[
 C_L\gamma _0\|m^{-2}\lambda\|_2\|m^{-1}D\mu\|_2,\qquad
 C_L\gamma _0\|m^{-2}\mu\|_2\|m^{-1}D\lambda\|_2.
\]
All these factors occur in the graph norms. Restricting the six sums to a set uses only its endpoint/stencil enlargement and proves the local assertion. No derivative of \(J\) or number of pillars enters. \(\square\)

More precisely, at flat links
\[
 d_\lambda c_J(0,\lambda)[\mu]
 =-\langle i[\mu,D\lambda],J\rangle_f
  -\langle i[\lambda,D\mu],J\rangle_f .
 \tag{3.3}
\]
Transpose the finite colour bracket to write this as a source
\(f_0+D^{\mathsf T}f_1\), with
\[
 |f_0|\le C|J||D\lambda|,\qquad |f_1|\le C|J||\lambda|.
\]
This is an exact weak identity, not a bound on the divergence of \(f_1\). At complex links use the bilinear covariant transpose and the bounded endpoint transports.

The current part of the cutoff commutator is also small in the weak norm. Indeed
\[
 [D,\chi]\lambda(b)
 =\eta^{-1}(\chi(b_+)-\chi(b_-))\lambda^+(b).
 \tag{3.4}
\]
Multiplication by \(J\) commutes with a scalar cutoff. In (3.2), all other commutators are endpoint differences of \(\chi\), or (3.4) or its transpose. If \(|D\chi|\le C_L/(M_1m)\), the differentiated terms are bounded by \(C_L\gamma _0M_1^{-1}m^{-4}|\lambda||\mu|\); mixed terms acquire an endpoint oscillation at most \(C_L\eta/(M_1m)\le C_L/M_1\). The same Cauchy–Schwarz argument gives local \(\mathcal X\to\mathcal X^*\) norm at most \(C_L\gamma _0/M_1\). Thus Proposition 2.1 is consistent with h-walk's repaired energy commutator.

**Lemma 3.2 (divergence-source local regularity, smaller version).** On flat four-dimensional cubes with fixed concentric enlargements and \(r\ge16\eta\), suppose \(\Delta_\eta u=D^{\mathsf T}g+F\). On an inner cube,
\[
 |u|\le C(r^{-2}\|u\|_{2,\mathrm{outer}}+r|g|+r^2|F|),
 \tag{3.5}
\]
and without additional regularity of \(g\) the direct absolute-kernel proof gives
\[
 |Du|\le C\{r^{-3}\|u\|_{2,\mathrm{outer}}
           +(1+\log(r/\eta))|g|+r|F|\}.
 \tag{3.6}
\]
All source suprema are on the outer cube. Equation (3.6) is an upper bound, not a claim that the logarithm is attained in (2.2).

*Proof of the kernel and local estimates.* In unit mesh the full-space Green kernel is the Fourier integral with multiplier
\(\lambda(p)^{-1}\), \(\lambda(p)=4\sum_{\mu=1}^4\sin^2(p_\mu/2)\).
The singularity \(|p|^{-2}\) is integrable in four dimensions. A \(q\)-fold difference, \(q=0,1,2\), has multiplier \(O(|p|^{q-2})\). For \(|x|_\infty=R>4\), cut at frequency \(R^{-1}\). The small ball contributes \(CR^{-q-2}\). On its complement integrate by parts \(q+3\) times in a coordinate with \(|x_\mu|=R\). The differentiated multiplier is bounded by \(C|p|^{-5}\); its radial integral above \(R^{-1}\) is at most \(CR\). Multiplication by \(R^{-q-3}\) again gives \(CR^{-q-2}\). Cutoff derivatives obey the same scaling and periodicity cancels boundary terms. For bounded \(R\), integrate the absolute multiplier. Restoring mesh gives, in physical kernel-density convention,
\[
 |D^qG_\eta(x)|\le C_q(|x|+\eta)^{-2-q}.
 \tag{3.7}
\]

Choose a cutoff equal to one on an intermediate cube, supported in the outer cube, and put
\(v=G_\eta*(D^{\mathsf T}(\chi g)+\chi F)\).
Move the source difference onto the kernel by finite summation by parts. A dyadic shell of radius \(t\ge\eta\) has physical volume at most \(Ct^4\). Its contributions to \(|v|\) are at most \(Ct|g|\) and \(Ct^2|F|\); summing up to \(Cr\) gives \(C(r|g|+r^2|F|)\). For \(|Dv|\), the flux contributes at most \(C|g|\) on each shell, hence \(C(1+\log(r/\eta))|g|\); the force contributes \(Cr|F|\).

The difference \(h=u-v\) is harmonic on the intermediate cube. Here
\(|h|+r|Dh|\le Cr^{-2}\|h\|_2\). To verify this interior fact, one-dimensional telescoping gives
\(|f(x)|\le C(r^{-1}\|f\|_1+\|Df\|_1)\).
Apply it in four directions; a mixed difference of order \(j\) has coefficient \(Cr^{-(4-j)}\). Cauchy–Schwarz contributes \(Cr^2\). Test the harmonic equation against a squared cutoff times \(h\), sum by parts and use \(2ab\le a^2/2+2b^2\), obtaining
\(\|Dh\|_{2,\mathrm{inner}}\le Cr^{-1}\|h\|_{2,\mathrm{outer}}\).
Differences commute with the flat Laplacian, so repeat on a fixed number of nested cubes for each mixed difference and once more for \(Dh\). This proves the stated powers. Cubes of bounded mesh size follow directly from pointwise \(L^2\) evaluation. Finally
\(\|v\|_{2,\mathrm{intermediate}}\le Cr^2\sup|v|\).
Combining the estimates proves (3.5)–(3.6). \(\square\)

This rebuilds the value part of the differentiated-source method recorded in flat-port.md Section 4. Its stronger gradient estimate requires a positive Hölder seminorm of the flux, including jumps. For the flux in (3.3), \(\lambda=Z\) and (2.2) give a seminorm of size \(c\gamma _0\eta^{-\epsilon}\) for a nonzero colour component. The independent-current class does not bound it. Neither the P82 zero-divergence lemma nor this direct scalar replacement proves the desired uniform field gradient. This is the remaining mixed-system obligation, not an impossibility result.

## 4. Whole-polydisc bounds that do follow: local energy

Put
\[
 \|A\|_{\mathcal E,w}=\sup_yw(y)\|A\|_{E,y},\qquad
 \|b\|_{Y,w}=\sup_cw(c)|b(c)|.
\]
This \(\mathcal E\) norm is not the SA pointwise \(X\) norm.

**Named inputs.** Use h-walk Lemma L and Theorems W, T with their gate's graph-norm, second-jet coefficient and tree-count repairs, uniformly on every cut-down. In particular the all-scale absolute coefficient premise for \(\Delta^{(2)}[j]\) is needed; the four inverse inequalities alone do not provide it. For parameter geometry retain o1-decoupled **hypothesis (P)**:
every set of metric diameter less than \(\ell_{\mathsf P}/2\) meets at most 16 parameter cubes. Its compatibility with the intended parameter assignment is not established here. This is the precise pending o1 input used in this section.

Use Definition D for \(H\), and for \(H_1\) use the full decorated-tree hulls, including the read sets of \(j^{(0)}\). The fixed-region carrier construction in h-walk-gate Section 8 puts those read sets within \(R_*=C_LM_1\) of the cells. Increase this fixed \(C_L\) to include the output pillar. Choose \(\ell_{\mathsf P}>8R_*\). This does not assert the unrepaired cross-sequence locality clause (C5).

**Lemma 4.1 (tree parameter count).** If a tree of length \(t\) contains the endpoints and meets the required cells, its tagged hull lies within \(R_*\) of its image. Under (P),
\[
 \#\mathsf P(\omega)\le16(1+8t/\ell_{\mathsf P}),\qquad
 |s^\omega|\le e^{16\bar\kappa}
               e^{128\bar\kappa t/\ell_{\mathsf P}}.
 \tag{4.1}
\]
*Proof.* Traverse each edge in both directions, obtaining length \(2t\). Partition this traversal into at most \(1+8t/\ell_{\mathsf P}\) arcs of length at most \(\ell_{\mathsf P}/4\). Each arc's \(R_*\)-neighbourhood has diameter at most \(\ell_{\mathsf P}/4+2R_*<\ell_{\mathsf P}/2\), so meets at most 16 parameter cubes. These neighbourhoods cover the hull. Sum their counts and multiply \(|s_\Delta|\le e^{\bar\kappa}\) once per tag. Approximate the infimal tree length from above if it is not attained. A single traversal for a path gives 64 instead of 128. \(\square\)

**Theorem 4.2 (conditional decoupled energy bounds).** Under these named inputs, choose
\[
 \ell_{\mathsf P}\ge1024\bar\kappa/\tau_L,\qquad
 \nu_1C_W/M_1\le\tfrac12,\qquad C_T^2M_1^{-1/3}\le\tfrac12 .
\]
For \(O=H,H_1\) and every weight of rate at most \(\tau_L/16\),
\[
 \|O(s)(\cdot,c)\|_{E,y}
 \le C_Le^{16\bar\kappa}e^{-(\tau_L/8)d_{\mathbf B}(y,c)},\qquad
 \|O(s)b\|_{\mathcal E,w}\le C_Le^{16\bar\kappa}\|b\|_{Y,w}.
 \tag{4.2}
\]
The constants are independent of depth, mesh, volume and \(M_1\) above the floors. The specified sums are holomorphic on the whole open parameter polydisc and the admitted open pair domain.

*Proof.* A unit colour source in the \(\nu\)-slot at row \(c\) has dual norm \(\xi_c\). Forming \(H_{(1)}=\mathsf H_{(1)}\mathsf m^{-1}\) divides by \(\xi_c\), cancelling this factor. W bounds a term by
\(B_L(C_W/M_1)^n e^{-(\tau_L/2)t}\); T bounds it by
\(B_1(C_TM_1^{-1/3})^n e^{-(\tau_L/4)t}\).
Equation (4.1) spends at most \(\tau_Lt/8\). Thus both leave at least \(e^{-(\tau_L/8)t}\).
There are boundedly many roots at the output pillar; the numbers of continuations are at most \(\nu_1^n\) and \(C_T^n\), respectively. The two floors bound the resulting geometric series by 2. Since \(t\ge d(y,c)\), this proves the column bound, absorbing the fixed colour dimension.

Sum the columns by the triangle inequality in the local energy norm. Use
\(w(y)/w(c)\le C_Le^{(\tau_L/16)d(y,c)}\).
There are boundedly many rows per initial pillar, including adjacent-scale incidence factors. The remaining sum is at most
\(C_LK_{\tau_L/16}\) by the ball-count input of h-walk Section 5, with its stipulated \(\tau_L\rho'\ge256\log L\). This proves the second estimate. The same majorants give locally uniform convergence of holomorphic finite-dimensional terms; passing their Cauchy integrals to the limit proves holomorphy. \(\square\)

This reproduces the energy summation underlying o1-decoupled Theorem B and extends it to the repaired T estimate. It does not treat that pending Theorem B as an established pointwise bound.

There is no uniform energy-space embedding that can finish the task. On a flat scale-one pillar put a single component of a 1-form equal to \(\eta^{-1}Z\) at one interior bond, zero elsewhere. Its mass-norm square is \(\eta^2\). Each of the four forward differences has two nonzero values of magnitude \(\eta^{-2}\); their total physical squared norm is 8. Thus
\(\|A\|_E^2=8+\eta^2\), but
\(\sup|A|=\eta^{-1}\), \(\sup|\nabla A|=\eta^{-2}\).
This is not asserted to be a lift column; it rules out upgrading arbitrary energy bounds without using the equations.

Direct pointwise evaluation gives only
\[
 m_y|A|_y+m_y^2|\nabla A|_y
 \le C_L(m_y/\eta)^2\|A\|_{E,y^+},
 \tag{4.3}
\]
where the fixed enlargement includes the output stencils. Each physical squared-norm summand has coefficient \(\eta^4\), so \(|u(x)|\le\eta^{-2}\|u\|_2\); apply this to \(A\) and \(\nabla A\), with adjacent scales comparable. The resulting mesh/depth loss is forbidden by the target.

## 5. The exact R9 contraction implication

Now use the actual SA norm
\[
 \|a\|_{X,w}=\sup_yw(y)\max\{\xi_y|a|_y,\xi_y^2|\nabla_{\mathbf U}a|_y\},
 \qquad \|f\|_{F,w}=\sup_yw(y)\xi_y^3|f|_y.
\]
The following premises remain **open for the actual first system**:

- **[PW]:** its specified jointly holomorphic maps satisfy
  \(\|H\|_{Y_w\to X_w},\|H_1\|_{Y_w\to X_w},
  \|\mathfrak G\|_{F_w\to X_w}\le B\),
  \(B=Ce^{16\bar\kappa}\ge1\), uniformly on the whole polydisc, for all admitted weights and geometries.
- **[NL]:** its specified holomorphic \(W_s,\mathcal C\) vanish at zero and, on unweighted balls of radius \(r\le r_0/B\), satisfy
\[
 \|W_s(a)-W_s(v)\|_{F,w}\le C_WB^2r\|a-v\|_{X,w},\qquad
 \|\mathcal C(a)-\mathcal C(v)\|_{Y,w}\le C_Cr\|a-v\|_{X,w}.
 \tag{5.1}
\]

[PW] is the missing pointwise target, not Theorem 4.2. The \(W_s\) part of [NL] is the named SA assertion at 10368–10389 and 10562–10576; its quoted assertion does not constitute its rebuild. a3-clauses Section 4 proves nonlinear bounds for its explicitly specified \(\Sigma\) system, and Section 4.3 excludes the unchecked current-corrected operators needed here. Theorem \(\Sigma\) therefore cannot silently supply [NL] for R9.

**Proposition 5.1 (conditional existence and weighted first response).** Assume [PW], [NL]. For \(b=\|B'\|_{Y,1}<cB^{-4}\), where
\[
 c\le\min\{r_0/4,1/(16C_W),1/(16C_C)\},
\]
R9 has a unique solution in the balls below, jointly holomorphic in all the specified variables, and
\[
 \|\mathbf H\|_{X,1}\le2Bb,\qquad
 \|D_{B'}\mathbf H[\beta]\|_{X,w}\le2B\|\beta\|_{Y,w}.
 \tag{5.2}
\]
This proves an implication only.

*Proof.* Put \(R=2Bb\). First solve
\[
 a=H_1B'-\mathfrak G W_s(a)=:\Phi(a).
\]
On the closed \(R\)-ball its Lipschitz constant is
\(q=C_WB^3R=2C_WB^4b\le1/8\), while \(\|\Phi(0)\|\le Bb=R/2\). It maps the ball into itself. Iteration from zero has successive differences bounded by \(q^n\|\Phi(0)\|\); the geometric series converges. Its limit is a fixed point, two fixed points in this ball coincide by the same Lipschitz inequality, and \(\|a\|\le Bb/(1-q)\).

Next solve \(h=a-H\mathcal C(h)\) on the closed \(2R\)-ball. Here the Lipschitz constant is
\(q_C=2C_CBR=4C_CB^2b\le1/4\). The map takes this ball into itself: \(\|a\|\le R\) and its nonlinear part has size at most \(q_C(2R)\le R/2\). Also \(2R\le r_0/B\).
The same iterative argument gives a unique \(h\) in this ball, with
\[
 \|h\|\le\frac{Bb}{(1-q)(1-q_C)}\le2Bb.
\]
Set \(X=\mathcal C(h)\), \(\mathbf A=a-H_1B'\), \(\mathbf H=h\). These satisfy every R9 equation. Conversely an R9 solution with \(\|a\|\le R,\|h\|\le2R\) solves the two contractions.

The iterations are holomorphic and converge uniformly on smaller parameter/datum polydiscs; passing Cauchy integrals to the limit proves holomorphy. Differentiating gives
\[
 (1+\mathfrak G W_s'(a))\dot a=H_1\beta,\qquad
 (1+H\mathcal C'(h))\dot h=\dot a .
\]
Their two derivative norms are at most \(q,q_C\) in every weight by (5.1). The inverse geometric series have norms at most \((1-q)^{-1},(1-q_C)^{-1}\), proving (5.2). For \(w(y)=e^{\theta d_{\mathbf B}(y,y_c)}\) and \(\beta=e\delta_c\), the source norm is \(|e|\), giving exponential first-response decay. No identity such as \(\widehat QH(s)=1\) was used. \(\square\)

A further block distinction matters for \(\mathfrak G\). The outline specifies
\[
 \mathfrak G=\mathsf G_1-\mathsf H_1Q\mathsf G_1
                 -\mathsf G_1DRD^{\mathsf T}\mathsf G_1.
 \tag{5.3}
\]
Only the first two terms are the \(AA\) block in h-walk Lemma U(c). The last term needs its own composed expansion. At decoupled parameters (5.3) does not license multiplying independently decoupled factors. This source/composition obligation is part of [PW], not an algebraic consequence of the \(H_1\) energy estimate.

## 6. The comparison implication, with the collar retained

Here is the precise additional premise needed for a pointwise analogue of o1-decoupled (3.1). For a lift let \(f_z\) be a unit row datum. For \(\mathfrak G\), let \(f_z\) be any force supported in one pillar, with \(\|f_z\|_{F,1}\le1\).

**[PW-term], open:** the actual tagged terms obey
\[
 \|s^\omega O_\omega f_z\|_{X,y}
 \le A_*e^{16\bar\kappa}q^{|\omega|}
              e^{-a t(\omega;y,z)},
 \tag{6.1}
\]
on a fixed larger local complex class, with \(a,A_*\) independent of \(M_1\), count at most \(NC^{|\omega|}\) and \(Cq\le1/2\). For force sources this must hold uniformly over the stated ball. It includes the derivative of the output cutoff. An energy estimate does not imply it.

Assume compatible specifications: terms whose full read hulls stay in an agreement region \(G\) are the same holomorphic functions of their local pairs and have identical parameter tags. For \(H\), this is the named o1-decoupled Lemma C1 with its enlargement, still subject to its pending gate. For \(H_1,\mathfrak G\), compatibility must include all branches, \(j^{(0)}\) read sets and composed scalar blocks; the unrepaired W locality clause does not establish it.

Let \(G^c\ne\varnothing\), and set \(D_x=d(x,G^c)\), zero outside \(G\). If the metrics agree in \(G\), their distances to its complement coincide. Let \(R_*=C_LM_1\) bound the read hull's distance from its tree and set \(D_x^*=(D_x-R_*)_+\). Suppose the pair difference in common coordinates is at most \(\varepsilon e^{-\theta_PD_x}\), with fixed analytic room \(a_{\min}>0\) along its interpolation. Then these premises imply
\[
 \|(O-O^\square)(s)f_z\|_{X,y}
 \le C A_*e^{16\bar\kappa}(1+\varepsilon/a_{\min})
 e^{-\vartheta(D_y^*+D_z^*)}e^{-(a/2)d_*(y,z)},\qquad
 \vartheta\le\min\{\theta_P/2,a/4\}.
 \tag{6.2}
\]
Here \(d_*\) is the smaller endpoint distance for the two systems, and the prefactor is independent of \(M_1\).

*Proof.* For an unmatched/exterior term its hull meets \(G^c\); a point of its tree is within \(R_*\) of that meeting. Its length is at least each of \(D_y^*,D_z^*\), hence at least their half-sum, and is also at least the endpoint distance. Split \(at\) into equal parts to pay the two exponentials in (6.2). This half-sum is necessary in this argument: a branch tree can share the leg toward the boundary, unlike a path traversed from source to target.

For a common interior term let \(d_0\) be the distance of its full read hull to \(G^c\). Cauchy's formula, on a complex line circle whose radius is proportional to \(a_{\min}\) divided by the local size of the pair direction, bounds its derivative by (6.1) times \(C\varepsilon e^{-\theta_Pd_0}/a_{\min}\). Integrate along the interpolation. The stipulated larger local class and analytic room justify the circle at every interpolation point. Output derivatives and transports are included in the common-coordinate version of (6.1).

Each hull point is within \(R_*\) of the tree, so \(D_y^*,D_z^*\le d_0+t\). Consequently
\[
 \vartheta(D_y^*+D_z^*)\le\theta_Pd_0+(a/2)t.
\]
The remaining \((a/2)t\) pays the endpoint exponential. Sum both families with \(\sum_n(Cq)^n\le2\). \(\square\)

This supplies the conditional analogue for \(H_1,\mathfrak G\) only when their own [PW-term] and compatibility hypotheses are proved. To replace the buffered distances by \(D_y+D_z\), this proof costs \(e^{2\vartheta R_*}\). In particular the explicit \(e^{\tau_Lr''}=e^{C_LM_1}\) in o1-decoupled Theorem C is not uniform in \(M_1\). The buffer in (6.2) preserves a uniform prefactor. This is a limitation of the available implication, not a claim of optimality or a counterexample to every possible unbuffered comparison.

**(H-field) from the contraction.** Assume [PW], [NL] and common-coordinate extensions on which both systems and the following residuals are defined. Both pairs of compared fields must lie in the common small balls of Proposition 5.1, so its Lipschitz bounds apply to the segments being subtracted. Let their solutions be \((a,h)\), \((a^\square,h^\square)\) and their row data \(b,b^\square\). Define
\[
 \begin{split}
 r_a={}&H_1(b-b^\square)+(H_1-H_1^\square)b^\square
       -(\mathfrak G-\mathfrak G^\square)W^\square(a^\square)\\
       &-\mathfrak G\{W(a^\square)-W^\square(a^\square)\},\\
 r_h={}&-(H-H^\square)\mathcal C^\square(h^\square)
       -H\{\mathcal C(h^\square)-\mathcal C^\square(h^\square)\}.
 \end{split}
 \tag{6.3}
\]
These include changed nonlinear maps and data, not just changed propagators. Subtract the two equations of each contraction. Weighted Lipschitz constants at most \(1/4\) give
\[
 \|a-a^\square\|_{X,w}\le\tfrac43\|r_a\|_{X,w},
\quad
 \|h-h^\square\|_{X,w}
 \le\tfrac43\{\tfrac43\|r_a\|_{X,w}+\|r_h\|_{X,w}\}
 \le2(\|r_a\|_{X,w}+\|r_h\|_{X,w}).
 \tag{6.4}
\]
This is an exact subtraction argument, without identities between decoupled operators.

Equation (6.4) gives (H-field) if the residuals are controlled in \(w=e^{\vartheta D}\), or its buffered version if only \(e^{\vartheta D^*}\) is controlled. Source summation in (6.2) uses the same pillar count as Theorem 4.2. The changed local rows, action, datum and transports must bound the other terms of (6.3). This is precisely where the corresponding named inputs in o1-decoupled Section 3 would be used. Its Theorem D further reads (O1), the specified current readout and the node comparison. No bound on those quantities is manufactured by (6.4).

## 7. Literature coverage and recovery decision

The requested primary-paper read could not be completed. The repository identifies the paper folder as /Users/jonreilly/ym4d-papers; the exact paths cmp99b.txt and cmp109.txt there were absent in this session. A request for the actual paper-folder path was made while the analytic work continued. No whole-home or whole-/tmp search was made, and no access to a paper that was not available is claimed.

The bounded repository literature map in a3-balaban.md Section 2 distinguishes CMP 99b's local value/derivative estimates (3.42)–(3.47), random-walk Theorem 3.7/Corollary 3.8, and the later current-corrected objects. Section 10 distinguishes complex field continuation from independent decoupling. These are second-hand source pointers here, not imports of Balaban's theorems. The differentiated-source mechanism also appears in flat-port.md Section 4; Lemma 3.2 above rebuilds the portion actually used, including its limitation. The o1 and wf-room notes point to CMP 109's independent-current domains; the admissible-current counterexample here uses the outline's explicit class, not an unchecked transcription of that paper.

The next mathematical decision is a source-sensitive regularity proof for the \(A\)-output of \(\mathbb K_\varkappa^{-1}\), with scalar forcing of the form (3.3), and a source class closed under the actual commutators and tree vertices. The scalar value estimate is available; taking a pointwise divergence loses \(\eta^{-1}\), and the direct scalar-gradient estimate loses \(\log(r/\eta)\) unless an additional cancellation is proved. The latter loss is not a lower bound on the field output. Eliminating the scalar variables before estimating the field, or proving a mixed-system estimate with a retained flux component, are possible repairs; neither has been completed here. Assuming a bound on \(DJ\) would change the requested pair class and is not an adopted repair.

Source identities remain the pin in the provenance line and the single fetched outline. The mathematical source comparison after the external checkout change found no changed dependency among those used. All proof steps above are analytic; no numeric run, machine enumeration or computer-assisted certificate was used. Only this output was written in the repository. There was no subagent, audit, commit, push, PR or post.

## Result

- **Proved by hand from the explicit current continuation and regular-pair definition:** Proposition 2.1. The direct \(c_J=O(\gamma _0)\) *pointwise first-order* perturbation step is false, already in a flat scale-one patch. This is not a counterexample to the R9 field theorem.
- **Proved smaller statements:** Lemma 3.1 gives \(O(\gamma _0)\) weak-form smallness and \(O(\gamma _0/M_1)\) current commutators; (3.3) retains the current as a bounded flux. Lemma 3.2 gives the flat divergence-source value estimate and the displayed, nonuniform gradient upper bound.
- **Proved implication from named inputs:** Theorem 4.2 gives decoupled local-energy bounds for \(H,H_1\), uniformly in depth, mesh, volume and \(M_1\), assuming the repaired h-walk energy package, its coefficient premise, and o1-decoupled hypothesis (P) for the specified tagged hulls. It gives neither the first-line supremum bounds nor \(\mathfrak G\)'s missing field estimate.
- **Conditional consequences only:** [PW] plus the named SA nonlinear assertion [NL] imply R9 existence and weighted first response by Proposition 5.1. [PW-term] plus compatible local specifications and pair-comparison room imply (6.2); controlled residuals imply (H-field) through (6.4). Those open premises are not discharged here.

**Where rank 4 stops:** still at the uniform pointwise field upgrade for the actual current-corrected local systems, now with the failed absorption step identified and a correct divergence-source replacement specified. The actual \(H(s),H_1(s),\mathfrak G(s)\) supremum estimates, and therefore the unconditional first-system field and removed-field bounds, remain open. After that bridge, the complex box-localisation and Landau node-lift obligations named in o1-decoupled Section 5 remain; this note grants none of them status.
