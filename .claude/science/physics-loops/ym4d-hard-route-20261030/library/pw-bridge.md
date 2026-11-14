# pw-bridge: pointwise regularity for the current-corrected first system
Provenance: OpenAI Codex (GPT-6; finer runtime model and effort identifiers are not exposed here; requested effort: max), source commit 805db53a78e75c7ccecf16c43770176708dd9cf9, Sussman–Alpoge commit 31a47c543775. Research text, not an audit; grants no status.

## 1. Contract, sources and proof boundary

Queue row 135, sa-ledger rank 4. The target [PW] is the bound from the row-data space to the **first-order** supremum space for the specified decoupled operators \(H,H_1\), and from the force space to that same space for \(\mathfrak G\). Thus it includes both \(m|A|\) and \(m^2|\nabla_{\mathbf U}A|\). All constants must be independent of mesh, depth, volume and \(M_1\) above its fixed floor. A value bound alone is insufficient.

The requested source passages and repairs are read at the provenance pin. In particular dec-field Proposition 2.1 refutes a pointwise coefficient estimate, not [PW]; its Lemma 3.1 is a weak, divergence-form estimate. A proof must retain that distinction. No differentiation bound on the independent current is assumed. No De Giorgi–Nash–Moser theorem for systems is invoked. File retrieval, searches and transcription are not proof steps.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's regular-pair domain, current continuation, operators, R9, norms and decoupling specification. Their outline was fetched once, at the named commit, to `/tmp/sa_ym4.tex`. T. Balaban is credited for the background propagator and local-inverse expansion architecture. The library notes keep their attributed authorship and the conditional standing of their named inputs.

The checkout is pinned as requested. Its root `AGENTS.md` points to `docs/ai_methodology/SCIENCE_WORKFLOW.md`, absent from the sparse working tree but available and read in bounded ranges from this pinned Git object. No planning-branch content is imported. The task-specific GOAL and FINISH passages govern this research note. Only this output file is edited in the repository.

## 2. Literature check and counterexample tests

The source map is `a3-balaban.md` Section 2: Balaban, CMP **99** (1985), 389–434, Theorems 3.1–3.4 concern scalar and vector propagators; 3.7–3.10 construct local-inverse walks; 3.12 treats the current-corrected objects and excludes their covariant-Laplacian estimate. The outline, SA 10531, distinguishes that paper's physical-current/second-difference hypotheses from the independent-current domain attributed to Balaban, CMP **109**, p. 262. Neither source pointer proves an estimate on the present domain. The named paper folder `/Users/jonreilly/ym4d-papers` is absent in this environment; its exact replacement was requested while work continued. No primary-paper read is claimed. The targeted search of the permitted repository literature found no discrete Calderón–Zygmund/Morrey proof for this mixed system. SA 11074 explicitly warns against an unrestricted bounded-flux mixed-gradient bound. Sections 4–5 below rebuild the needed lattice estimates; they do not import a literature theorem as evidence.

The following are the counterexample tests, before using the proposed bridge.

1. **Staggered independent current.** The configuration in dec-field Proposition 2.1 is admissible and its coefficient grows like \(\gamma _0/\eta\). We retain it. It precludes putting the current's divergence into a bounded pointwise force. It does not preclude an \(L^p\) bound on the flux followed by a further inverse in the field equation.
2. **Energy concentration.** The one-bond spike in dec-field Section 4 has bounded energy and unbounded field supremum. Thus the equations, not an energy embedding, must supply the upgrade.
3. **A generic divergence source.** For \(\Delta u=D^{\mathsf T}g\), a first-order \(L^p\) estimate gives a value bound for \(u\), not a supremum bound on \(Du\). The field equation below instead has \(Dp\) as an \(L^p\) force after the scalar equation has controlled \(Dp\). A second-order estimate is then available for the field.
4. **Rough average transposes.** Even at identity, \(Q'^{\mathsf T}\) is piecewise constant across pillar faces. Differentiating \([Q'^{\mathsf T}aQ',\chi]\lambda\) pointwise is not legitimate uniformly in mesh. The source combination in Section 3 cancels this derivative before any estimate. An argument that bounds \(Dg'_h\) separately would fail this test.

Route 2 is not assumed: the regular-pair definition SA 10129–10137 and R9's holomorphy in an independent current do not provide a scale-weighted difference bound on that current. Restricting to such a smaller ball would require a new consumer/domain argument. Everything below retains the original current ball.

## 3. The source combination and the exact reduced equations

Write \(A_s=\Delta_{\mathbf U}+M\), \(M=Q'^{\mathsf T}aQ'\), and \(E=\Delta^{(2)}[j]\). Use precisely h-walk Section 4's polarized form and physical bilinear transposes. Separate its lower-order blocks by writing
\[
 q_{AA}=\Delta^{\rm W}+Q^{\mathsf T}aQ+V_{AA},\quad
 q_{A\lambda}=\tfrac12DA_s+V_{A\lambda},\quad
 q_{\lambda A}=\tfrac12A_sD^{\mathsf T}+V_{\lambda A},\quad
 q_{\lambda\lambda}=V_{\lambda\lambda}.
 \tag{3.1}
\]
Here the \(V\)'s come only from \(-c_J\) and \(-\langle A-D\lambda,E(A-D\lambda)\rangle\). The one-half in each mixed block is essential.

For \(F=(f;g_h,g_\lambda,g_\mu;g'_h,g'_\lambda,g'_\mu;f_\nu)\), set
\[
 p=h'+\tfrac12D^{\mathsf T}A,\qquad
 f_\circ=f-\tfrac12Dg'_h.
 \tag{3.2}
\]
The second definition is an identity of sources, including divergence sources; it does **not** ask that either summand be pointwise bounded. Direct substitution in the eight rows gives
\[
\begin{aligned}
 (\Delta^{\rm W}+DD^{\mathsf T})A
   &=f_\circ+Dp+\tfrac12Dh-Q^{\mathsf T}aQA-Q^{\mathsf T}\nu
                         -V_{AA}A-V_{A\lambda}\lambda,\\
 A_sh&=g'_\lambda+Q'^{\mathsf T}\mu,\\
 A_sp&=g_\lambda+Q'^{\mathsf T}\mu'
                         -V_{\lambda A}A-V_{\lambda\lambda}\lambda,\\
 A_s\lambda&=D^{\mathsf T}A+g'_h-h,\\
 A_s\lambda'&=g_h-p+\tfrac12D^{\mathsf T}A,\\
 Q'\lambda&=-g'_\mu,\qquad Q'\lambda'=-g_\mu,\qquad QA=f_\nu .
\end{aligned}
 \tag{3.3}
\]
In particular there is no derivative of \(g'_h\) in the field equation after (3.2), and no derivative of the rough scalar \(p\) is required in a supremum norm.

For clarity, use local units \(m=1\) on a fixed enlarged pillar neighbourhood; adjacent scales differ by at most a fixed power of \(L\). The current terms have the exact form
\[
 V_{AA}A+V_{A\lambda}\lambda=F_A,\qquad
 V_{\lambda A}A+V_{\lambda\lambda}\lambda=F_\lambda+D^{\mathsf T}Z_\lambda,
 \tag{3.4}
\]
with, for every \(2\le q\le8\),
\[
 \|F_A\|_q+\|F_\lambda\|_q+\|Z_\lambda\|_q
 \le C_L(\gamma _0+\gamma_j)
              (\|A\|_q+\|\lambda\|_q+\|D\lambda\|_q).
 \tag{3.5}
\]
Norms on the right include the fixed carrier enlargement. To verify this, polarize the three brackets of \(c_J\), as in dec-field (3.2). Variation in \(A\) gives endpoint products of \(J\) and \(\lambda\). Variation in \(\lambda\) gives endpoint products of \(J\) with \(A,D\lambda\), and the bilinear transpose of \(D\) applied to a bracket of \(J,\lambda\). Keep that last transpose outside the product. Bounded transports and \(|[u,v]|\le C|u||v|\) give (3.5) for these terms. The other form has variations \(-E(A-D\lambda)\) and \(D^{\mathsf T}E(A-D\lambda)\). Its absolute local row/column coefficient bound gives the same inequality by the weighted Schur calculation below. No difference of \(J\) or of a second-jet coefficient is taken.

The averaging/coefficient inputs used here are the local averaging bounds of p82-curved Sections 3–4 and a3-clauses Step 5, and h-walk-gate Section 5's **all-scale absolute second-jet coefficient premise**. In local units their precise uses are: averaging masses and transposed row/top sources map the local energy data to bounded forces; \(E\) has bounded absolute row and column sums and a fixed carrier; \(\Delta^{\rm W}+DD^{\mathsf T}\) is the componentwise covariant Laplacian plus a bounded local zeroth-order operator. These are named inputs, not consequences of the four inverse bounds alone. The last identity is the forward-curl Weitzenböck identity and Wilson remainder used in a3-clauses Step 5 and (B1).

More explicitly, the second-jet premise is a2-curved (8.3), not merely its concluding form bound (8.10). Multiplying its leg sum \(C_L\xi_c(\eta/\xi_c)^4\) by the physical row weight \(\xi_c^4|j_c|\le\gamma_j\xi_c\), and dividing by the fine operator pairing weight \(\eta^4\), gives \(C_L\gamma_j\xi_c^{-2}\). Only boundedly many adjacent-scale row carriers meet a fixed bond. Thus after local rescaling the absolute row sum is \(C_L\gamma_j\); symmetry gives the column sum. This verifies the precise stronger consequence of the named coefficient premise used below.

For a kernel \(e(x,z)\) with physical-measure absolute row and column sums at most \(C\), Hölder gives
\[
 |Eu(x)|^q\le C^{q-1}\sum_z\eta^4|e(x,z)||u(z)|^q.
\]
Sum over \(x\), interchange the finite sums and use the column bound to obtain \(\|Eu\|_q\le C\|u\|_q\). This is the only \(L^q\) estimate on \(E\) used in (3.5).

## 4. The lattice estimates, proved here

All sums in this section use measure \(\eta^4\) on \(\eta\mathbb Z^4\). Forward and backward differences include \(\eta^{-1}\). Write \(\Delta=\sum_iD_i^*D_i\), with positive sign. Constants below are independent of \(\eta\). We need only exponents \(2,3,8\), and strict, nonendpoint Sobolev embeddings.

### 4.1 Green kernels and the discrete Calderón–Zygmund bound

**Lemma CZ.** For finitely supported lattice functions and \(1<q<\infty\),
\[
 \|D_iD_j^*\Delta^{-1}v\|_q\le C_q\|v\|_q.
 \tag{4.1}
\]
The same statement holds with either orientation of either difference, and componentwise for a fixed finite number of complex components.

*Proof.* At mesh one the Green function has Fourier multiplier
\[
 \Lambda(t)^{-1},\qquad
 \Lambda(t)=4\sum_{i=1}^4\sin^2(t_i/2),\quad t\in[-\pi,\pi]^4.
\]
The singularity is integrable. The multiplier of a product of \(k\) differences, \(0\le k\le3\), is of order \(|t|^{k-2}\) near zero, and its derivative of order \(a\) is bounded by \(C_{k,a}|t|^{k-2-a}\). These inequalities follow by differentiating the finite products \(e^{\pm it_i}-1\), using \(c|t|^2\le\Lambda(t)\le C|t|^2\) near zero, and the quotient rule. Away from zero every derivative is bounded.

For \(|x|_\infty=R>4\), split the integral by a smooth cutoff at \(|t|=R^{-1}\). The small ball contributes at most \(CR^{-2-k}\). On the complement integrate \(k+3\) times in a coordinate with \(|x_i|=R\). The absolute integral of the differentiated multiplier is at most
\(C\int_{R^{-1}}^1 t^{3}t^{-5}\,dt+C\le CR\).
Each integration contributes \(R^{-1}\). Derivatives of the cutoff have the same scaling. Periodicity removes the boundary terms. For bounded \(R\), absolute integration suffices. Rescaling to physical density gives
\[
 |D^kG_\eta(x)|\le C_k(|x|+\eta)^{-2-k},\qquad 0\le k\le3.
 \tag{4.2}
\]
For \(T=D_iD_j^*\Delta^{-1}\), the Fourier multiplier has absolute value at most one, because
\(|e^{it_i}-1||e^{it_j}-1|\le\Lambda(t)\). Parseval therefore gives \(\|T\|_{2\to2}\le1\). Its kernel \(K\) satisfies (4.2) with \(k=2\). Telescoping a lattice path and using \(k=3\) gives
\[
 |K(x-z)-K(x-z_0)|
       \le C|z-z_0|(|x-z_0|+\eta)^{-5}
 \tag{4.3}
\]
when \(|x-z_0|\) is at least a fixed multiple of \(|z-z_0|+\eta\).

Here is the weak \((1,1)\) proof, including its uniformity. At height \(t>0\), select maximal dyadic lattice cubes whose average of \(|v|\) exceeds \(t\). They are disjoint; their total physical volume is at most \(\|v\|_1/t\); their parent averages are at most \(t\), so their own averages are at most \(16t\). Put \(g=v\) off these cubes and equal to each cube's average vector on it, and put \(b_Q=(v-v_Q)1_Q\). Then
\[
 |g|\le16t,\quad \|g\|_1\le\|v\|_1,\quad
 \|g\|_2^2\le16t\|v\|_1,\quad
 \sum_Q\|b_Q\|_1\le2\|v\|_1,\quad
 \sum_{x\in Q}\eta^4b_Q(x)=0\quad\text{for each }Q.
\]
The last equality is understood separately on each cube. Atoms of side \(\eta\) have zero bad part. For a larger cube, subtract \(K(x-z_Q)\) inside \(Tb_Q\), where \(z_Q\in Q\). By (4.3), summing outside a fixed enlargement of \(Q\) yields
\[
 \sum_{x\notin cQ}\eta^4|Tb_Q(x)|
 \le C\|b_Q\|_1.
\]
Indeed, the shell of radius \(2^n\operatorname{side}(Q)\) contributes at most \(C2^{-n}\|b_Q\|_1\). Enlarged cubes have total volume at most \(C\|v\|_1/t\). Chebyshev on \(Tg\), using its \(L^2\) bound, and Chebyshev on the summed bad parts off these cubes prove
\(\operatorname{vol}\{|Tv|>t\}\le C\|v\|_1/t\).
No cube-count constant depends on mesh.

For completeness interpolate without importing a theorem. When \(1<q<2\), split \(v=v_{>t}+v_{\le t}\). Apply the weak bound to the first part and the \(L^2\) bound to the second, with threshold \(t/2\). Multiply the resulting distribution inequality by \(q t^{q-1}\) and integrate. Interchanging nonnegative integrals gives respectively constants proportional to
\[
 \int_0^{|v(x)|}t^{q-2}|v(x)|\,dt
       =\frac{|v(x)|^q}{q-1},\qquad
 \int_{|v(x)|}^{\infty}t^{q-3}|v(x)|^2\,dt
       =\frac{|v(x)|^q}{2-q}.
\]
This proves the strong bound below two. The transpose multiplier has the same kernel and \(L^2\) bounds, so duality with \(q'=q/(q-1)<2\) proves it above two. Truncation and the same bounds extend from finite supports; the bilinear complex transpose can equivalently be checked componentwise. This proves (4.1). \(\square\)

### 4.2 Interior estimates with an \(L^2\) anchor

On cubes with fixed concentric margins, in units where their radii are fixed numbers, Lemma CZ implies, for \(q=2,3,8\),
\[
\begin{aligned}
 \|u\|_{W^{2,q}(Q)}
   &\le C_q(\|u\|_{2,Q^+}+\|F\|_{q,Q^+}),
       &&\Delta u=F,\\
 \|u\|_{W^{1,q}(Q)}
   &\le C_q(\|u\|_{2,Q^+}+\|F\|_{q,Q^+}+\|Z\|_{q,Q^+}),
       &&\Delta u=F+D^*Z.
\end{aligned}
 \tag{4.4}
\]
Here all second differences, not merely the Laplacian, occur in \(W^{2,q}\).

*Proof.* Cut off the sources outside an intermediate cube and solve in full space by convolution with \(G_\eta\), moving the divergence onto its kernel. On the fixed outer cube, (4.2) and summation over shells bound the value and first-gradient convolutions whose kernels have orders two and three by their integrable-kernel norms. The remaining derivatives are exactly (4.1). Thus the particular solution has the asserted \(L^q\) derivative bounds and a controlled local \(L^2\) norm. The difference from \(u\) is harmonic on the intermediate cube.

For that harmonic difference, test its equation against a squared cutoff times its complex conjugate and take the real part. Finite summation by parts and \(2ab\le a^2/2+2b^2\) give
\(\|Dh\|_{2,Q_1}\le C\operatorname{gap}(Q_1,Q_2)^{-1}\|h\|_{2,Q_2}\).
Flat differences commute with \(\Delta\); iterate this estimate on a fixed number of nested cubes for every mixed difference needed. In one dimension telescoping from an averaged point gives
\(|v(x)|\le C(r^{-1}\|v\|_1+\|Dv\|_1)\).
Applying this in all four coordinates, then Cauchy–Schwarz and the iterated energy estimate, bounds \(D^a h\) in supremum by \(C_a r^{-2-a}\|h\|_2\) for \(a=0,1,2\). This also bounds its \(L^q\) norm. If there are too few sites for these nested cubes, \(r/\eta\) is bounded by the fixed number of margins; direct point evaluation and finite differences give the same scaled estimates. This proves (4.4), with no maximum principle for a system. \(\square\)

### 4.3 The strict Sobolev steps actually needed

On fixed nested cubes,
\[
 W^{1,2}\longrightarrow L^3,\qquad
 W^{1,3}\longrightarrow L^8,\qquad
 W^{1,8}\longrightarrow L^\infty,
 \tag{4.5}
\]
uniformly in mesh. In particular \(W^{2,8}\) controls both a field and its first differences in supremum.

*Proof.* Multiply by a smooth cutoff and extend by zero. The Fourier identity
\(v=\Delta^{-1}D^*Dv\) represents its value by first differences of \(G_\eta\) convolved with \(Dv\). For output on the inner cube only a fixed-radius truncation of that kernel is needed. By (4.2), this kernel is uniformly in \(L^a\) whenever \(a<4/3\): the dyadic sum near zero has ratio \(2^{-(4-3a)}<1\), including the innermost shell of radius \(\eta\). Use respectively
\(a=6/5,24/19,8/7\).
They satisfy \(1+1/q=1/p+1/a\) for \((p,q)=(2,3),(3,8),(8,\infty)\).

The convolution inequality used here is elementary. For finite \(q\ge p,a\), split the integrand into
\((|k|^a|v|^p)^{1/q}|k|^{1-a/q}|v|^{1-p/q}\)
and apply Hölder with reciprocal exponents \(1/q,1/a-1/q,1/p-1/q\), which sum to one. Raise to \(q\), sum over the output and interchange sums. This gives \(\|k*v\|_q\le\|k\|_a\|v\|_p\). The infinite case is Hölder directly. Derivatives of the cutoff contribute the \(\|u\|_p\) part of the local \(W^{1,p}\) norm. Apply the same argument to each first difference for the last assertion. \(\square\)

These proofs cover a finite number of components by summing component norms. They use neither De Giorgi–Nash–Moser regularity nor an \(L^\infty\) bound for a Calderón–Zygmund operator.

## 5. A source norm closed under the actual walk

### 5.1 Norms and the local regularity lemma

Set \(q=8>4\). In local units define the source norm \(\mathcal S\) using representations
\[
 f=f_\circ+\tfrac12Dg'_h,\qquad
 g_\lambda=u_\lambda+D^{\mathsf T}z_\lambda.
 \tag{5.1}
\]
It is the sum of the local \(L^8\) norms of
\(f_\circ,g_h,g'_h,u_\lambda,z_\lambda,g'_\lambda\), and the local maximum norms of \(g_\mu,g'_\mu,f_\nu\). The support of a represented source is the union of the supports of these densities, including their stencils; one may take the infimum over representations on that declared support. All supported-source statements below use this convention. Every source in this norm is in \(\mathcal X^*\): pair each divergence against the first difference of its test field, use Hölder on the fixed-volume patch, and use the corresponding energy/graph component. Thus \(\|F\|_*\le C_L\|F\|_{\mathcal S}\) for a supported source.

Define the solution norm \(\mathcal R\) by
\[
 \|A\|_{W^{2,8}}+\|\lambda\|_{W^{2,8}}
 +\|\lambda'\|_{W^{2,8}}+\|h\|_{W^{2,8}}
 +\|p\|_{W^{1,8}}
 +\max(|\mu|+|\mu'|+|\nu|),
 \tag{5.2}
\]
with absent multipliers omitted. The fields have the rescalings
\[
 (mA,\lambda,\lambda',m^2h,m^2p,m^4\mu,m^4\mu',m^3\nu).
 \tag{5.3}
\]
Derivatives in (5.2) are in \(x/m\), and local \(L^q\) norms use normalized measure \(m^{-4}\eta^4\). The corresponding source rescalings are
\[
 (m^3 f_\circ,m^2g_h,m^2g'_h,m^4u_\lambda,
       m^3z_\lambda,m^4g'_\lambda,g_\mu,g'_\mu,mf_\nu).
 \tag{5.4}
\]
These powers follow directly from (3.3), rather than from a continuum dimensional analogy. On comparable neighbouring pillars they change constants only by \(C_L\).

**Lemma R (local mixed regularity).** On every admitted local model, on a fixed inner pillar neighbourhood,
\[
 \|\Psi\|_{\mathcal R,y}
 \le C_L\left(\sum_{x\in y^{++}}\|\Psi\|_{\mathcal X,x}
                         +\|F\|_{\mathcal S,y^{++}}\right).
 \tag{5.5}
\]
The fixed enlargement includes the averaging carriers. Its diameter and number of pillars depend only on \(L\). The constant is uniform in the fine mesh, depth, volume and walk-cell size.

*Proof.* Work first in an interior cube in the class gauge, with local scale one. The gauge and its complex perturbation have uniformly bounded potential and first differences. Expansion of opposite transported shifts, as in a3-clauses Step 5, writes
\[
 \Delta_{\mathbf U}u=\Delta u+B\nabla u+Cu,
 \qquad |B|+|\nabla B|+|C|\le C_L(\alpha_0+\alpha_1).
 \tag{5.6}
\]
The displayed derivative bound is on the drift coefficient \(B\), not on \(C\). Alternatively, the drift is a divergence of a bounded coefficient times \(u\), plus a bounded zeroth-order term: use the exact finite-difference product identity and the bound on \(\nabla B\). This alternative needs only \(u\in L^q\), and is used to start the bootstrap. The field operator in (3.3) has the same componentwise principal part and an additional bounded finite-stencil zeroth-order term. No regularity of a current coefficient is needed for (5.6).

Let \(N\) be the right side of (5.5), before its constant. Local energy controls \(A\) and its first differences in \(L^2\); it controls \(\lambda,\lambda'\) in the graph norm, and \(h,h'\) in \(L^2\). Hence \(p=h'+D^{\mathsf T}A/2\) is in \(L^2\) with bound \(C_LN\). Each multiplier on a nearby row or top is bounded by its local weighted \(\ell^2\) norm. The averaging coefficient bounds then give bounded forces of size \(C_LN\) for every mass and transposed row/top term in (3.3). This includes \(Mp\): \(p\) is already controlled in local \(L^2\). All subsequent statements use successively smaller fixed cubes; finitely many margins suffice for the following explicit list.

1. From the graph bounds, (5.6), and the first estimate of (4.4), \(\lambda,\lambda'\in W^{2,2}\) with bound \(C_LN\). Their first differences were already in the graph norm, so this step does not solve for an uncontrolled drift.
2. In the equations for \(h,p\), put the drift into divergence form. The known \(L^2\) values of \(h,p\) control its flux. Equation (3.5) controls the other flux and force of the \(p\)-equation using the known \(A,\lambda,D\lambda\in L^2\). The second estimate of (4.4) yields \(h,p\in W^{1,2}\). Now the \(h\)-equation has an \(L^2\) force even with its drift written in nondivergence form; the first estimate gives \(h\in W^{2,2}\). The field equation has \(Dp,Dh\in L^2\), and every other term is in \(L^2\), so it gives \(A\in W^{2,2}\).
3. Apply the first embedding (4.5) to each field and each controlled first difference. Thus \(A,\lambda,\lambda',h\), and their first differences, are in \(L^3\); \(p\in L^3\). Put the drift of the \(p\)-equation into divergence form again. Both of its source types are in \(L^3\), by (3.5), so \(p\in W^{1,3}\). The four equations for \(A,h,\lambda,\lambda'\), now in nondivergence form, have \(L^3\) forces, including \(Dp\). They give \(W^{2,3}\) for these four fields.
4. The second embedding (4.5) gives all their first differences in \(L^8\), and gives \(p\in L^8\). Equation (3.5) and the divergence form of the drift now put the \(p\)-equation in the second case of (4.4) with \(q=8\). Hence \(p\in W^{1,8}\). Each of the other four equations has an \(L^8\) force, so its solution is in \(W^{2,8}\).

Each step multiplies the bound by a fixed constant; the number of steps is fixed. This proves (5.5). Smallness of \(\gamma_0,\gamma_j\) is used for the already named energy inverse and its coercive perturbation, not for the false pointwise absorption of \(DJ\). The local bootstrap itself works for bounded lower-order coefficients. On the stipulated small ceiling those bounds are fixed constants.

The gauge patches and comparable-scale neighbourhoods are those of p82-curved Proposition 6.2. At a bare output, or when the local scale is at most a fixed number of mesh steps, direct point evaluation in \(\mathcal X\) controls every derivative in (5.2) after (5.3); the ratio \(m/\eta\) is bounded there. Nonbare outputs have the full interior stencil. No assertion about continuum corner regularity is made. Cut-down models are used only on their cutoff/read neighbourhoods, where their scales agree with the original sequence. These observations give the stated uniformity. Finally (4.5) controls \(m|A|+m^2|\nabla_{\mathbf U}A|\) by \(C_L\|\Psi\|_{\mathcal R}\); the covariant-to-ordinary correction is bounded multiplication. \(\square\)

### 5.2 Cutoffs and tree vertices preserve the source type

**Lemma C (the needed closure, including the dangerous term).** A smooth scalar cutoff with its first two scaled differences bounded by \(C/M_1\) satisfies
\[
 \|[\mathbb K,\chi]\Psi\|_{\mathcal S,y}
       \le {C_L\over M_1}\sum_{x\in y^+}\|\Psi\|_{\mathcal R,x}.
 \tag{5.7}
\]
Multiplication of a source by any of the walk or pillar cutoffs is bounded in \(\mathcal S\); multiplication of a solution is bounded in \(\mathcal R\). The coefficient vertex satisfies
\[
 \|V_\beta\Psi\|_{\mathcal S,y}
 \le C_L\sup_{c\text{ near }y}m_c^3|j_\beta(c)|
                         \sum_{x\in y^+}\|\Psi\|_{\mathcal R,x}.
 \tag{5.8}
\]

*Proof.* Use commutator convention \([T,\chi]=T\chi-\chi T\). For \(F=[\mathbb K,\chi]\Psi\), its third-group first entry is
\[
 g'_h=-[D^{\mathsf T},\chi]A+[A_s,\chi]\lambda.
\]
The principal part of its field entry contains \(\tfrac12[DA_s,\chi]\lambda\). Therefore its source combination is
\[
\begin{aligned}
 f_\circ={}&[\Delta^{\rm W}+Q^{\mathsf T}aQ,\chi]A
 +\tfrac12[D,\chi]A_s\lambda
 +\tfrac12D[D^{\mathsf T},\chi]A-[D,\chi]h'
 +[Q^{\mathsf T},\chi]\nu\\
 &+[V_{AA},\chi]A+[V_{A\lambda},\chi]\lambda .
\end{aligned}
 \tag{5.9}
\]
This is exact, from \([DA_s,\chi]=[D,\chi]A_s+D[A_s,\chi]\). In particular **the entire derivative of \([A_s,\chi]\lambda\), including its averaging mass, cancels**. Every term remaining in (5.9) is in \(L^8\) with the claimed factor: \(A_s\lambda\) uses \(W^{2,8}\); \(D[D^{\mathsf T},\chi]A\) uses at most two differences of \(\chi\) and one of \(A\); \(h'=p-D^{\mathsf T}A/2\) is in \(L^8\). The Wilson commutator has the ordinary first-order Laplacian commutator and bounded lower-order terms, so it uses at most \(\nabla A,A\).

For the second-group scalar-dual entry, combine its two principal commutators **before** estimating:
\[
 \tfrac12[A_sD^{\mathsf T},\chi]A+[A_s,\chi]h'
       =[A_s,\chi]p+\tfrac12A_s[D^{\mathsf T},\chi]A.
 \tag{5.10}
\]
The first term uses \(p,\nabla p\in L^8\). Write the kinetic part of the second as a divergence of the first covariant difference of \([D^{\mathsf T},\chi]A/2\), with bounded lower-order terms; its flux is in \(L^8\). Its mass is a bounded averaging operator. Thus (5.10) is of the form required for \(g_\lambda\); it requires neither a second difference of \(p\) nor a third difference of \(A\). The current commutators are obtained from (3.4) by the finite-difference product identity: their fluxes and forces gain a cutoff oscillation or one cutoff difference. No difference of \(J\) occurs. The same argument works for \(E\), since its carrier has fixed diameter and its absolute coefficients obey the stated bounds.

The remaining differential entries are
\([A_s,\chi]\lambda'\) in \(g_h\),
\([A_s,\chi]h-[Q'^{\mathsf T},\chi]\mu\) in \(g'_\lambda\), and the displayed \(g'_h\). All are \(L^8\) forces with the required factor. The three constraint entries are averaging commutators on \(\lambda',\lambda,A\), bounded by the cutoff oscillation on their carriers. Top/row multipliers are already bounded by (5.2). These exhaust the eight rows and prove (5.7).

For source multiplication, the new field combination is exactly
\[
 (\chi F)_\circ=\chi f_\circ-\tfrac12[D,\chi]g'_h.
 \tag{5.11}
\]
Multiplication of \(u_\lambda+D^{\mathsf T}z_\lambda\) has the same flux representation plus a bounded cutoff-difference term. Thus no derivative of \(g'_h\) or \(z_\lambda\) is introduced. For solution multiplication,
\(p(\chi\Psi)=\chi p+\tfrac12[D^{\mathsf T},\chi]A\);
two differences of the cutoff suffice for (5.2). Finally a vertex has only the \(V\)-entries of (3.4), zero \(g'_h\), and the coefficient bound with \(j_\beta\) in place of \(j\). This proves (5.8). \(\square\)

The identities (5.9)–(5.11) are also a check independent of the bootstrap: they identify exactly which apparent higher derivatives must cancel. Estimating the eight raw source entries separately would lose this property and would not prove this lemma.

## 6. Pointwise walk and tree bounds for \(H,H_1\)

Retain these named inputs, with their scope unchanged:

- **[Energy]** h-walk Lemma L, its cut-down uniformity and the graph-norm repair in h-walk-gate Section 5; equivalently the cited conjugation/invertibility package (I1), including its complex domain. Its local decay rate is \(\tau_L\).
- **[Coefficients]** the averaging, Wilson principal-part and absolute second-jet coefficient inputs listed after (3.5), on the same cut-downs. The second-jet input is needed for \(H_1\), not for \(H\) at \(j=0\).
- **[Walk geometry]** h-walk's bounded overlap, two-difference cutoffs, local coefficient agreement and cut-down metric domination; the repaired fixed-region field carriers, counts and coefficient factors in h-walk-gate Sections 6–8. No failed cross-sequence locality or single-term reflection assertion is imported.
- **[Parameter geometry]** o1-decoupled Definition D and hypothesis (P), with full tree hulls and the \(j^{(0)}\) read sets. The fixed-region hull radius is \(R_*=C_LM_1\).

The small ceiling and separation are those required by these inputs. In particular \(\tau_L\rho'\ge256\log L\); all constants below depend on their fixed \(L\)-dependent constants. This is a research implication from these inputs, not their revalidation.

**Lemma W\(_\infty\).** For a source supported near \(z\), each local inverse used by the walk satisfies
\[
 \|\mathbb K_\kappa^{-1}F\|_{\mathcal R,y}
       \le C_Le^{-\tau_Ld_{\mathbf B}(y,z)}\|F\|_{\mathcal S}.
 \tag{6.1}
\]
Here the output is in the region where that local inverse is used by a cutoff or a commutator. Consequently the actual terms of h-walk obey
\[
\begin{aligned}
 \|T_\omega F\|_{\mathcal R,y}
   &\le C_L(C_L/M_1)^n
                    e^{-(\tau_L/2)t_\omega(y,z)}\|F\|_{\mathcal S},\\
 \|T^{(1)}_\omega F\|_{\mathcal R,y}
   &\le C_L(C_LM_1^{-1/3})^{|\omega|}
                    e^{-(\tau_L/4)t_\omega(y,z)}\|F\|_{\mathcal S}.
\end{aligned}
 \tag{6.2}
\]

*Proof.* Apply Lemma R to the local solution. [Energy] bounds each energy term on its fixed enlargement by \(C_Le^{-\tau_Ld(y,z)}\|F\|_*\). The local source term is zero unless \(d(y,z)\le C_L\); in that case the same estimate follows by enlarging its constant. The source-to-dual bound following (5.4) proves (6.1). The use of local gauges does not change constants on overlaps: first and second covariant differences are equivalent to the displayed ordinary differences by the bounded potential and its first differences. Alternatively the transition between two admitted real gauges has bounded first and second differences, as follows by differentiating its link transformation once; the real gauge itself is isometric.

For a walk, decompose each commutator source into a smooth pillar partition. Source multiplication is bounded by (5.11). Apply (5.7), then (6.1), successively. For fixed intermediate pillars the resulting bound is
\[
 C_L(C_L/M_1)^n
 \sum_{y_1,\ldots,y_n}
 \exp\{-\tau_L[d(y,y_1)+\cdots+d(y_n,z)]\}
                  \|F\|_{\mathcal S},
 \tag{6.3}
\]
with the same support restrictions as W. Half the exponent pays the path visiting the required cells. Sum the other half from the last intermediate pillar backwards, dropping the last leg before summing. Each sum is bounded by \(K_{\tau_L/2}\). The output cutoff is bounded in \(\mathcal R\). This proves the first line of (6.2).

For a tree vertex, use (5.8) and repaired Lemma J's coefficient estimate
\(m_c^3|j_\beta(c)|\le C_L\gamma_0(C_L/M_1)^{m_\beta}
 e^{-(\tau_L/4)t_\beta(c)}\).
The trunk/branch construction is exactly h-walk Section 7. If there are \(v\) vertices among \(n\) trunk steps and their branch lengths are \(m_i\ge1\), the power supplied is
\[
 p_*=n-v+\sum_i m_i,\qquad
 |\omega|=n+\sum_i(m_i+1),\qquad
 3p_*-|\omega|=2(n-v)+2\sum_i(m_i-1)\ge0.
\]
Keep the coefficient factor \(C_L^{n+\sum_i m_i}\), as required by the gate. Join the trunk paths and branch paths at their interacting pillars. Their union contains a tree meeting the required cells. Reserve \(\tau_L/4\) for its length; the remaining trunk exponent sums the intermediate pillars, just as in (6.3). Fixed joining offsets cost \(C_L^{|\omega|+1}\), not \(e^{cM_1}\). The displayed arithmetic proves the second line. The bounded backward branch choices and the compositions of the total length give at most \(C_0C_1^{|\omega|}\) terms per root, including a fixed multiplicity at length zero. \(\square\)

**Normalization.** A source for the counting-measure column \(H(\cdot,c)e\) is \(f_\nu=e\delta_c/\xi_c\). Its \(\mathcal S\) norm is at most \(C_L|e|\), by (5.4); its dual norm is \(|e|\), since the unnormalized source has dual norm \(\xi_c|e|\). Thus no source-scale factor remains. The same statement holds for \(H_1\). A force supported in one pillar with \(\sup m^3|f|\le1\) also has \(\mathcal S\) norm at most \(C_L\).

**Decoupling and summation.** A tree of length \(t\) has full read hull within \(R_*\) of it. Traverse its edges twice and split the traversal into arcs of length at most \(\ell_{\mathsf P}/4\). If \(\ell_{\mathsf P}>8R_*\), each thickened arc has diameter less than \(\ell_{\mathsf P}/2\), and (P) gives at most sixteen parameter cubes. Hence
\[
 \#\mathsf P(\omega)\le16+128t/\ell_{\mathsf P},\qquad
 |s^\omega|\le e^{16\bar\kappa}e^{128\bar\kappa t/\ell_{\mathsf P}}.
 \tag{6.4}
\]
The root is within its fixed hull radius of the output, so it is included in this count. All tags are included, also for a length-zero term. Choose
\[
 \ell_{\mathsf P}>8R_*,\qquad
 \ell_{\mathsf P}\ge2048\bar\kappa/\tau_L,
 \tag{6.5}
\]
and increase the fixed \(M_1\) floor so the exponential count times \(C_LM_1^{-1/3}\) is at most \(1/2\). Equations (6.2)–(6.4), and the last embedding in (4.5), give the column bound
\[
 \|H_{(1)}(s)(\cdot,c)\|_{X,y}
   \le C_Le^{16\bar\kappa}e^{-(\tau_L/8)d(y,c)}.
 \tag{6.6}
\]
Here \(X\) is exactly dec-field's value-and-first-difference norm; the exponent has been weakened to leave common room for Section 7. For weights of rate at most \(\tau_L/16\), summing columns leaves \(K_{\tau_L/16}<\infty\), by the stated separation and pillar count. Therefore
\[
 \|H(s)\|_{Y_w\to X_w}+\|H_1(s)\|_{Y_w\to X_w}
       \le C_Le^{16\bar\kappa}.
 \tag{6.7}
\]
Every term is the original algebraic term; only its estimate has changed. Uniform majorants on smaller open pair/parameter domains allow passage of Cauchy integrals through the series. This proves joint holomorphy in the original independent-current ball, with no added difference condition on \(J\). The source norm is a proof device, not a restriction on that pair domain.

Weights multiply the local norms and endpoint majorants throughout this argument. No exponential distance weight is differentiated or asserted to preserve a scalar graph norm; the graph-norm obstruction in h-walk-gate Section 5 is therefore not reintroduced.

## 7. The composed source expansion: \(\mathfrak G\)

This is the composition left open in dec-field (5.3), following its Proposition 5.1. The \(H_1\) expansion above is the constrained \(A\nu\) block. Its \(AA\) companion is only
\[
 P_1=\mathsf G_1-\mathsf H_1Q\mathsf G_1.
\]
It does not contain the remaining term \(\mathsf G_1DRD^{\mathsf T}\mathsf G_1\). We now supply that term's own expansion.

### 7.1 Two further block expansions

Delete the \(\nu\) row and column of the unfolded system, keeping the same coefficient \(j=\mathsf H^{\mathsf T}J\). Lemma U's elimination then gives field block \(\mathsf G_1\). Its local inverse estimate follows from the same finite inverse words, with the row-Gram factors omitted; [Energy] includes the required \(\mathsf G_1\) inverse. Lemmas R and C apply with the row multiplier absent. Use the identical zero-length coefficient \(j^{(0)}\) and the identical branches \(j_\beta\). Denote the resulting field terms by \(G_\alpha\), and the constrained \(AA\) terms by \(P_\omega\). Thus at physical parameters,
\[
 \mathsf G_1=\sum_\alpha G_\alpha,\qquad P_1=\sum_\omega P_\omega.
 \tag{7.1}
\]
Both families have the second line of (6.2) for an \(L^8\) force source.

Next use the three-unknown scalar system \(\mathbb X\) itself. Its inverse is h-walk (4.2), a finite sum of words in \(G'\) and the scalar Gram inverse. The graph-norm repair and the same weighted composition argument give its local energy decay, with a rate at least \(\tau_L\). Use the same cut-down scalar systems, cutoffs and parametrix identity to expand its \(h\)-output from an \(h\)-slot source:
\[
 P_{\rm sc}:=1-R=[\mathbb X^{-1}]_{hh}=\sum_\sigma L_\sigma.
 \tag{7.2}
\]
The equality is the explicit elimination in Lemma U(a): for source \((v,0,0)\), \(h=G'Q'^{\mathsf T}NQ'G'v=(1-R)v\).

Here no new regularity premise is needed. Give scalar sources \((s_h,s_\lambda,s_\mu)\) the local norm \(\|s_h\|_8+\|s_\lambda\|_8+\max|s_\mu|\), with scalings \((m^2s_h,m^4s_\lambda,s_\mu)\). The equations
\(A_sh=s_\lambda+Q'^{\mathsf T}\mu\), \(A_s\lambda=s_h-h\)
and the bootstrap of Section 5 put both \(h,\lambda\) in \(W^{2,8}\). The commutator sources are
\([A_s,\chi]\lambda\),
\([A_s,\chi]h-[Q'^{\mathsf T},\chi]\mu\), and
\(-[Q',\chi]\lambda\).
They are all in the same source norm with factor \(C_L/M_1\). Thus scalar terms \(L_\sigma\) have the first line of (6.2), including their first and second output differences. In particular they accept \(v=D^{\mathsf T}A\in L^8\) without asking for a pointwise second derivative of \(A\).

### 7.2 Compose before tagging

Since \(R=I-P_{\rm sc}\), form the following three families of **undecoupled coefficients**:
\[
 P_\omega,\qquad
 U_{\alpha\beta}=G_\alpha DD^{\mathsf T}G_\beta,\qquad
 V_{\alpha\sigma\beta}=G_\alpha D L_\sigma D^{\mathsf T}G_\beta.
 \tag{7.3}
\]
All derivatives act on the indicated complete factor, including its output cutoff. Give a composite coefficient the union of its factors' full read hulls and connecting derivative stencils. Tag each parameter cube meeting that union **once**. Define
\[
 \mathfrak G(s)=
 \sum_\omega s^{\mathsf P(\omega)}P_\omega
 -\sum_{\alpha,\beta}s^{\mathsf P(\alpha,\beta)}U_{\alpha\beta}
 +\sum_{\alpha,\sigma,\beta}s^{\mathsf P(\alpha,\sigma,\beta)}
                                      V_{\alpha\sigma\beta}.
 \tag{7.4}
\]
This supplies the previously unspecified composed expansion under o1-decoupled Definition D's instruction to use each operator's own expansion. It does not replace the already specified \(H(s)\) or \(H_1(s)\), and does not multiply independently decoupled factors. In particular repeated parameter tags have exponent one, not two or three.

At \(s=1\), the absolute convergence proved below permits multiplication and summation of (7.1)–(7.2), so
\[
 \mathfrak G(1)=P_1-\mathsf G_1DD^{\mathsf T}\mathsf G_1
                  +\mathsf G_1DP_{\rm sc}D^{\mathsf T}\mathsf G_1
 =\mathsf G_1-\mathsf H_1Q\mathsf G_1
                  -\mathsf G_1DRD^{\mathsf T}\mathsf G_1.
 \tag{7.5}
\]
This checks the exact operator, order of factors and sign in dec-field (5.3).

### 7.3 Bounds on the composed sources

Let \(f_z\) be an \(L^8\) force supported in a pillar and normalized in the units (5.4). The right factor \(G_\beta f_z\) is in \(W^{2,8}\) locally, by (6.2). Therefore \(DD^{\mathsf T}G_\beta f_z\) is an \(L^8\) force locally, with the same estimate times \(C_L\). Indeed a second covariant difference is an ordinary second difference plus bounded coefficients times first differences and values; only the first difference of the connection is used. Decompose this force into smooth pillar-supported pieces and apply the left factor with (6.1)–(6.2). This proves the required bound on \(U_{\alpha\beta}f_z\).

For \(V\), first form \(v=D^{\mathsf T}G_\beta f_z\), whose local \(L^8\) norm is controlled. Decompose \(v\) into pillar-supported pieces and use the scalar estimate of 7.1 for \(L_\sigma v\). Its first covariant difference is an \(L^8\) force of the right scale. Localize that force and apply \(G_\alpha\). The scaling chain is
\[
 m^3 f\ \xrightarrow{G_\beta}\ mA
 \ \xrightarrow{D^{\mathsf T}}\ m^2v
 \ \xrightarrow{L_\sigma}\ m^2h
 \ \xrightarrow D\ m^3Dh
 \ \xrightarrow{G_\alpha}\ mA_{\rm out}.
 \tag{7.6}
\]
Every arrow here was bounded above in a local \(L^8\)/\(\mathcal R\) norm. There is no differentiation of \(J\), and no use of the false \(L^\infty\) mixed-gradient estimate.

Here is the length and count bookkeeping needed for (7.4). A nonzero composition requires the terminal input cutoff of the left factor to meet the output cutoff of the next factor, up to the fixed derivative stencil. Hence its constituent trees join at those intermediate pillars. The union contains a tree through the two endpoints and meeting all its cells. If \(t_i\) are the factor lengths, then \(\sum_i t_i\) bounds that tree length up to fixed stencil offsets. Each factor has rate at least \(\tau_L/4\). Reserve \(3\tau_L/16\) for the combined tree and use the remaining \(\tau_L/16\) to sum the one or two intermediate pillars. Successive sums are bounded by \(K_{\tau_L/16}\) or its square, by dropping the final endpoint leg. Fixed offsets are absorbed in \(C_L\). Thus each composite satisfies
\[
 \|O_\omega f_z\|_{X,y}
 \le C_L(C_LM_1^{-1/3})^{n(\omega)}
             e^{-(3\tau_L/16)t_\omega(y,z)}\|f_z\|_{\mathcal S}.
 \tag{7.7}
\]
Here \(n\) is the sum of the factors' walk/tree sizes. There are at most two joining edges with no \(M_1\) power; these are a fixed multiplicity, not charged as smallness factors.

For a fixed outer root, choose each successive constituent root among the bounded number of cells overlapping the preceding terminal cell. Count its trunk and branches by the repaired tree count. Splitting a total size \(n\) among at most three factors costs at most \((n+1)^2\le4^{n+1}\). Thus the total number is at most \(C_0C_1^n\). The intermediate pillars were summed inside a coefficient; they are not falsely counted as one additional finite list of size independent of volume. This is also why their two summable exponential factors were retained.

The combined hull is within \(C_LM_1\) of its combined tree. Enlarge \(R_*\) by this fixed factor before (6.5). Equations (6.4)–(6.5) spend at most \(\tau_L/16\) of (7.7), leaving \(\tau_L/8\). After increasing the fixed \(M_1\) floor, \(\sum_nC_1^n(C_LM_1^{-1/3})^n\le2\). This proves normal convergence of (7.4), its joint holomorphy, and
\[
 \|\mathfrak G(s)f_z\|_{X,y}
       \le C_Le^{16\bar\kappa}e^{-(\tau_L/8)d(y,z)}
                                      \|f_z\|_{\mathcal S}.
 \tag{7.8}
\]
At a fixed finite lattice, the convergence in the displayed local derivative norms also justifies every difference and composition in (7.5). Finally partition any force with \(\|f\|_{F,w}<\infty\) into pillar-supported forces. Each has local \(\mathcal S\) norm at most \(C_Lw(z)^{-1}\|f\|_{F,w}\); the weight changes by a bounded factor within a pillar. Sum (7.8) and use \(K_{\tau_L/16}\). The result is
\[
 \boxed{\displaystyle
 \|\mathfrak G(s)\|_{F_w\to X_w}\le C_Le^{16\bar\kappa}.}
 \tag{7.9}
\]
Together (6.7) and (7.9) are [PW], for all weights of rate at most \(\tau_L/16\), on the whole specified open polydisc \(|s_\Delta|<e^{\bar\kappa}\), with the uniform majorant also valid at its closed radius wherever the pair remains in the admitted class. The constant is independent of depth, mesh, volume and \(M_1\) above the fixed floors. It is not independent of the fixed \(L\), coefficient and energy constants, or of the explicit factor \(e^{16\bar\kappa}\).

## 8. Dependency and recovery checkpoint

The source revision is the provenance pin. GOAL, FINISH and the seven requested library/gate dependencies remain unchanged against that pin; the only repository addition is this note. The outline was fetched once. Source identity and text checks are bookkeeping, not proof evidence. No computation, enumeration, interval certificate, subagent, audit, commit, push, PR or post was used.

The decisive identities for recovery are (3.2)–(3.3) and (5.9)–(5.11). Retain the represented-source norm if continuing this proof: replacing it by separate bounds on the raw eight entries loses the cancellation of the differentiated averaging mass. Retain \(p\) only in \(W^{1,8}\), not in a first-derivative supremum norm. Retain all-scale absolute second-jet coefficients when invoking [Coefficients], and tag the union in (7.4) once. These are substantive hypotheses/constructions, not optional simplifications.

Author checks: re-elimination fixes both factors \(1/2\); the source and solution rescalings in (5.3)–(5.4) match every row of (3.3); the independent-current flux is never differentiated as a coefficient; the bootstrap uses only the strict embeddings \(2\to3\to8\); both intermediate sums in the three-factor composition retain \(K_{\tau_L/16}\); and the tag count leaves the common endpoint rate \(\tau_L/8\). These are hand checks by this author, not an independent review.

Literature coverage remains limited as stated in Section 2: the primary Balaban files were unavailable and no replacement path was supplied during this work. The proof uses the named repository inputs and the explicit lattice rebuild, not an assertion that those papers have been independently checked here.

## Result

**Proved by hand in this note:** the lattice Calderón–Zygmund estimate (4.1), the local estimates (4.4), the strict discrete Sobolev steps (4.5), and the exact source cancellation (3.2), (5.9)–(5.11). From the specified principal part and bounded divergence-form coefficients, Lemma R proves the \(2\to3\to8\) local bootstrap. Lemma C proves closure under the actual cutoffs and tree vertices. No bound on a difference of the independent current is added. The staggered-current obstruction of dec-field Proposition 2.1 remains valid and is compatible with this proof.

**Proved implication for [PW]:** [Energy], [Coefficients], [Walk geometry] and [Parameter geometry] of Section 6, with the fixed smallness/floor choices there and (6.5), imply
\[
 \|H(s)\|_{Y_w\to X_w},\quad
 \|H_1(s)\|_{Y_w\to X_w},\quad
 \|\mathfrak G(s)\|_{F_w\to X_w}
       \le B=Ce^{16\bar\kappa}.
\]
This holds for the original independent-current domain and all weights of rate at most \(\tau_L/16\), uniformly in depth, mesh, volume and \(M_1\) above the fixed floors. \(H,H_1\) use their specified walk/tree expansions. For \(\mathfrak G\), (7.4) supplies the required composed expansion and (7.5) verifies its physical-parameter value; the proof does not assert identities between independently decoupled factors. These are conditional research conclusions, without independent review or status.

**Where rank 4 then stops:** the next first-system obligation is **[NL] for R9's actual specified \(\mathsf W_s,\mathcal C\)**. Theorem \(\Sigma\) in a3-clauses Section 4 concerns its separately specified pair system and does not by itself supply that assertion. If [NL] is rebuilt for the same operator data, dec-field Proposition 5.1 now yields the R9 field and weighted first-response bounds on \(\|B'\|<cB^{-4}\), as an implication from the same named inputs. For the removed-field comparison, term-norm control is supplied here, but cross-sequence compatibility and all changed nonlinear/data residuals in dec-field (6.3) are still required; no failed o1 comparison claim is restored. The later complex box-localisation clause 6(c) and Landau node-lift comparison also remain. No unconditional R9 theorem, completed rank 4, or Yang–Mills existence conclusion is claimed.
