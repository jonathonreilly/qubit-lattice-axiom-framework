# Intrinsic stage response

Provenance: Codex (GPT-6), effort not exposed, 2026-11-04; checkout `52217c1ba651738d52bc0923473d13983001c98f`. Research text, not an audit; grants no status. Not yet checked by the other model.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the stage construction and response method. SA and CA-I mean their outline and complete account at `31a47c543775`. Balaban's stage theorem is used there as an input, not proved here.

## 1. Source finding and the fixed-system step

The requested five Result sections were read first. The index, neighbouring rows and cited source passages were read next. This reuses `lit-large-field.md:47–51`'s source search: “behind a bot check” and “a paywall”.

The first-exit method already occurs at SA 12356–12366. It assumes a “uniform continuation radius” (12359) and the response bounds (BGR32)–(BGR33). This is a conditional proof. The stage application is sketched: SA 17908–17911 invokes “response and hereditary-domain estimates”. CA-I 54987–54992 explicitly assumes “the stage theorem”. None supplies the missing stage estimate by defining a domain.

There is a useful intrinsic consequence. `intrinsic-dom.md:128–156` constructs the tube from canonical continuations on full \(r_B\)-balls. Its line 155 states that \(T_e\) “is well-defined and holomorphic”. Fix one determining set \(e\), one output norm and a chart derivative bound \(K\), uniform over those admitted real centres. This last bound remains an input.

At a tube point write \(D=e^{iB}V\), \(\|B\|<\delta\le1/40\), and freeze \(V\) locally. Put \(E=DV^{-1}-I\). For a differentiable datum path,
\[
 \dot B=i^{-1}D\Log(I+E)[\dot D V^{-1}],\qquad
 \|\dot B\|_{Y,w}\le4\|\dot D D^{-1}\|_{Y,w}.
 \tag{1}
\]
Indeed, differentiating the logarithm series gives norm at most
\(\sum_{k\ge1}\|E\|^{k-1}\le2\). Also \(\|DV^{-1}\|\le e^\delta\le2\).
The calculation is rowwise, so it preserves every scalar row weight.
Thus the intrinsic derivative has bound \(4K\).
Overlap agreement makes the derivatives agree. Integrate on successive local patches of any admitted path.
No earlier centre enters this estimate. It applies to **one fixed determining system** with the stated uniform chart estimate.

This does not supply all the premises of a response theorem.
`dec-field.md:247` says “Assume [PW], [NL]”. Its derivative at 274–279 varies the datum with the operators fixed.
The later [PW] proof retains “[Energy]”, “[Coefficients]”, “[Walk geometry]” and “[Parameter geometry]” (`pw-bridge.md:314–321`).
The [NL] theorem is for the specified reduced map: “under [RED]” (`nl-r9.md:332–333`).
Use these as their stated implications. Tube membership alone neither identifies that map nor proves those operator premises.

## 2. The first open stage input

CA-I 53806–53814 integrates \(Z_{j+1}\setminus Z''_{j+1}\), then replaces the member of level \(j+1\).
Its exact phrase is “the member of level” (53812), followed by \(j+1\) (53813).
This does not mean that only one **row level** changes.
SA 5615–5617 defines a row at level \(m\) by two tests: “at least one endpoint lies in $\Omega_j$, and neither lies in $\Omega_{j+1}$” (with \(j=m\)).
Hence changing \(\Omega_{j+1}\) can change both \(\Gamma_j\) and \(\Gamma_{j+1}\).
This proves the distinction by direct substitution in (R2).

The intrinsic gluing fixes \(e\); it does not glue different constraint problems.
SA 9776–9780 gives a restriction identity for memberwise nested sequences and “a real $\varepsilon_1$-regular $\mathbf V$”.
It is a possible bridge, with its stated regularity assumptions.
It does not identify every independently decoupled pair with a physical critical background.
In particular, the new variables must reproduce the old read: SA 17564 says “both written in the new variables”.

Here is the exact forcing that a bridge must control.
On a fixed slice let \(\mathcal C(A,p)=0\) be the constraints and
\(\mathcal E(A,\lambda,p)=F'_p(A)-\mathcal C_A^{\mathsf T}\lambda=0\) the critical equation.
Differentiation gives
\[
 \begin{pmatrix}\mathcal K&-\mathcal C_A^{\mathsf T}\\
                 \mathcal C_A&0\end{pmatrix}
 \binom{\dot A}{\dot\lambda}
 =\binom{-\partial_p\mathcal E\,\dot p}
              {-\partial_p\mathcal C\,\dot p}
 =:\binom{f}{b}.
 \tag{2}
\]
This is the chain rule, including the constraint Hessian in \(\mathcal K\).
It is also SA 11784–11796 (BGR6), which says differentiation is “before substituting the solution”.
Moving slices require their own gauge equation.
One cannot differentiate a discrete row selector as if \(p\) were already such a bridge.

**First open input:** realize the actual stage \(0\to1\), on each previous read, by a compatible fixed-system path or an equivalent comparison identity. Bound its complete forcing \((f,b)\) in the weighted A3 norms, uniformly over the full earlier-parameter and switch domains. Its output must be the prescribed returned pair, including the assigned independent current. The bound must have the small source size and shell support used in section 4 below.

CA-I 54247–54248 names a response map, but 54287 leaves the required identification as this instruction:

> Express $U^{(n)}_k$ through the new background $U^{(n+1)}_k$ and the fluctuation $(A_j,B_j)$ on the collar $R_n$,

That passage cites Balaban; it does not bound this map's full complex forcing.
The matching warning is also explicit in `a3-derivative.md:33`: “without a common restriction problem, matched collar rows, and an admitted interpolation.”
Replacing the old reference balls removes the old-centre requirement. It does not remove this matching requirement.
Before a first exit, membership admits the **listed** intrinsic towers. It does not bound \(\partial_p\mathcal C\), \(\partial_p\mathcal E\), or derivatives of earlier compositions in (2).
This is the first failed implication in the proposed route, not a counterexample to the stage map.

## 3. What fails in the layered extension

`wf-c.md:36` requires a collar in “the single layer j of B”. Its Lemma C requires a local regular real gauge and “\(\|w\|_*\le r_C\)” (68).
Under those hypotheses it bounds the datum mismatch and gauge (71–75).
This can supply a comparison for a matched single-layer collar. Intrinsic membership does not identify every prepared shell with that collar.

The proof uses a concrete geometric sum. With fixed ambient layer \(j\), `wf-c.md:77–83` gives
\[
 \sum_{q<j}\kappa L^{2(q-j)}\le\frac{\kappa}{L^2-1},
 \qquad
 \sum_{q<j}L^{q-j}\|w\|_*\le\frac{\|w\|_*}{L-1}.
 \tag{3}
\]
Both follow by summing geometric series. They control the lift defect and the gauge product.
Across a seam, replacing \(j\) by the ambient layer \(h_q\) gives terms \(\kappa_q L^{2(q-h_q)}\).
These do not have the displayed geometric majorant. Bounds with \(h_q=q\) give only a sum of the \(\kappa_q\).
This diagnoses the estimate; it does not assert an actual bad stage history.

The reference proof also loses \(T'_q\subset\Omega_q\), which `a3-close.md:68` uses for restriction.
Its line 60 names the loss as “factors up to \(L^{2(q-j_{\rm amb})}\)”; line 99 leaves “the layered case” open.
A proof must replace that lost comparison, using the actual layer lifts and profile decay.
It must also keep a positive distance from the boundary of every intrinsic datum tube.
The seven value bounds alone do not ensure that distance: they are imposed only where the tower exists (`intrinsic-dom.md:237–241`: “does not prove coverage”).
Thus no layered extension is proved here.

## 4. The expenditure and first-exit implication

Write each of the seven entries as \(q_a=\|F_a\|\).
Here \(r_a\) includes the old read's lift; convert both endpoints to those units first.
The target is `intrinsic-dom.md` (11), with
\[
 d_n(m)=c_n(m)-c_{n+1}(m)
 =\frac{g_k(m)}{2N}+\beta_R\sum_{l\in E_n}2^{-|m-l|}.
\]
Its line 279 says this “supplies an allowance, not the estimate (11)”.
Fix a finite history and every retained complex parameter \(\zeta\).
Suppose a locally defined stage path \(X_t\) starts at \(P\in D_{n+1}^{\rm int}\) and ends at the prescribed \(S_n(P;\zeta)\).
Suppose its **full** readout derivatives, before any exit, obey
\[
 \left\|\frac d{dt}F_a(X_t)\right\|
 \le Cr_a u_l\sqrt{1+|m-l|}\,e^{-D|m-l|},
 \quad D\ge\log4,\quad \sup_l Cu_l<\beta_R/2.
 \tag{4}
\]
The constants include the earlier compositions and are uniform over \(P,\zeta,t,a\).
This is a hypothesis here, not a bound proved for the actual stage.

Its mechanism on a fixed admitted system is precise.
The weighted response bound in `dec-field.md:253–255` is
“\(\|D_{B'}\mathbf H[\beta]\|_{X,w}\le2B\|\beta\|_{Y,w}\)”.
For data supported on \(K\), take \(w(y)=e^{\theta d(y,K)}\).
The output at \(y\) is then at most \(2B\|\beta\|_Y e^{-\theta d(y,K)}\).
To obtain (4), the actual forcing must have that support, the shell distance must bound \(|m-l|\), and the radius conversion must give the stated square root.
SA 17618–17624 sketches this for real stage curvature, with source ratio \(\delta'_j/\varepsilon_j\): “The margin between consecutive stages pays for the error”.
It does not establish (4) for all seven complex entries.
An earlier composition also contributes its derivative: `d4-incr.md:138` says “That fact does not remove \(K_n\).”

Integration and the reverse triangle inequality give
\[
 q_a(X_t)-q_a(P)
 \le\int_0^t\|\dot F_a(X_s)\|\,ds
 <\tfrac12\beta_R r_a2^{-|m-l|}.
 \tag{5}
\]
For integer \(q\ge0\), induction gives \(q+1\le4^q\); hence
\(\sqrt{1+q}e^{-Dq}\le2^{-q}\).
This proves (5) by hand: it “fits half a new level's margin” (`d4-stage.md:54–57`).
For several distinct new marks, assume the derivative bound is the sum of (4), then sum (5).

**No new mark.** Then the entire allowance is \(g_k(m)r_a/(4N)\).
The required separate estimate is
\[
 \sup_{P,\zeta}\int_0^1\|\dot F_a(X_t)\|\,dt
 <g_k(m)r_a/(4N).
 \tag{6}
\]
An unchanged read has zero expenditure. Otherwise (4)'s new-mark smallness does not imply (6).
For example, (R22) reads “$\theta_{\rm s}\beta_{\rm s}2^{-(t-m)}$” for \(m<t\) (SA 6130–6133).
At \(m=l<k=t\), this gives \(g_k(l)=\theta_s\beta_s2^{-(k-l)}\).
Thus \(Cu_l<\beta_R/2\) gives no bound below \(g_k(l)/(4N)\).
This includes reads outside the component, where no new mark is recorded (`d4-incr.md:104`: “only the phase allowance remains”).

**First exit.** Assume (5)–(6) spend less than \(d_n(m)r_a/2\), with a uniform strict factor.
Also assume the branch has a limit and local continuation at a possible first exit.
Its tube membership, real gauge witnesses and stored-slot domains must retain room there.
At an exit time \(t_*\), continuity gives
\[
 q_a(X_{t_*})\le q_a(P)+\epsilon_{n,a}
 <c_{n+1}(m)r_a+d_n(m)r_a/2
 =c_n(m)r_a-d_n(m)r_a/2.
 \tag{7}
\]
Every numerical clause is strictly interior. The other room assumptions permit continuation past \(t_*\), a contradiction.
This is the intrinsic version of SA's conditional first-exit proof, not a new stage theorem.
A boundary of the datum tube cannot be excluded by (7) alone.

## 5. Returns and stored slots

Unitary factors have condition number one and cost nothing.
For the remaining return factors \(g_i\), set \(a_i=\max(\|g_i-I\|,\|g_i^{-1}-I\|)\) and \(A=\sum_i a_i\).
Submultiplicativity and \(1+x\le e^x\) prove `d4-stage.md` (7):
\(\operatorname{cond}(g_s\cdots g_1)\le e^{2A}\).
Consequently a matrix entry with \(\|X\|\le c_*r_a\) and \(\|\Delta\|\le Er_a\) obeys
\[
 \|\operatorname{Ad}(g)(X+\Delta)\|-\|X\|
 \le r_a\{(e^{2A}-1)c_*+e^{2A}E\}.
 \tag{8}
\]
For instance, \(A\le\min\{1/4,d_n/(32c_*)\}\) and \(E<d_n/8\) make (8) less than \(3d_nr_a/8\).
Indeed, \(e^{2A}\le2\) and \(e^{2A}-1\le4A\), by the exponential series.
This gives a sufficient return budget. No such bound for the prescribed returns has been proved above.
If a response was estimated before return, its smaller budget \(E<d_n/8\) must be proved separately.
Equation (4), in contrast, concerns the complete returned read.
In particular, the independent current must use its assigned return and multiplier response.
SA 17922–17925 requires argument, gauge and stored data to be formed “together”.

Stored-slot admission is a separate condition.
SA 6160–6173 specifies “real bond forms”, near-variable “Borel” dependence, and far-variable analytic radii fixed by the kernel range.
A small complex conjugation need not preserve a real bond form.
For real \(t\ne0\), \(g=\operatorname{diag}(e^t,e^{-t})\) sends the Hermitian matrix
\(X=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) to
\(\left(\begin{smallmatrix}0&e^{2t}\\e^{-2t}&0\end{smallmatrix}\right)\), which is not Hermitian.
Thus (8) alone cannot admit a near slot; the prescribed representation must retain its real argument.
For a far slot of real range \(R\), one must bound the actual transported argument below \(\lambda^{\rm st}R\).
The switch disc and its zero identities must also persist.
SA 17946–17947 prescribes “evaluated at field zero” after integration, with the switch removed.
These facts do not follow from the seven entry bounds.

## Result

**Partial proof (first open input), for the stage step sketched by the sources.**
Equation (1) transfers a uniform fixed-system derivative bound to the intrinsic tube.
Equations (5)–(8) prove the margin, continuity and conjugation implications by hand.
The first open input is section 2's compatible realization and weighted forcing bound for the actual stage, starting at \(0\to1\), as requested by CA-I 54287.
The layered comparison, phase-only expenditure and stored-slot admission remain unproved.

If these inputs and continuation room hold, (7) gives \(S_0(D_1^{\rm int};\zeta)\subset D_0^{\rm int}\), with half the numerical margin left.
No actual (D4) inclusion at stage \(0\to1\) is proved here. No exiting stage history is claimed.
No run discharges any step. This text is not yet checked by the other model.
