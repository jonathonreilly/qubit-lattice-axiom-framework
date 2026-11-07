# Old-depth composition and the removed WF7 factor (row 137)
Provenance: OpenAI Codex, GPT-6 family (exact deployment identifier and runtime effort not exposed; queue request: max); checkout `573194aba3eede8dfbfb9126499daf80865eea08`; Sussman–Alpoge commit `31a47c543775`, `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`. Research text, not an audit; no status is granted.

## 0. Scope and source conventions

The target is rank 4's old-depth composition step, not the existence or mass-gap problem. All arguments below are mathematical arguments; text extraction, searches and file editing supply no proof evidence. The fixed checkout is the source revision for every local note. Only this research note is changed.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the nonlinear average, constrained backgrounds, first-rule tower, WF3–WF7 and WF13a, the independent-current response and its parameter-domain requirements. Credit Tadeusz Balaban for restriction at a background's own averages and for composing background maps in renormalization steps. The particular Current-I readout and Definition D used below are Claude's local specifications in `wf-room-2.md` and `o1-decoupled.md`, with the corrections of their Codex gates; they are not formulas uniquely imposed by the outline. Credit the authors and gate readers of the other local notes wherever a named input is used.

`removed-fix.md` is Codex's same-model text; its Claude gate (row 136) is pending at this checkout. Its conclusions are **named conditional inputs**, not independently established premises here. In particular **RF-G** means its Lemma G and (7.4), **RF-CD** means its Theorems C–D under all their hypotheses, and **RF-Loc** means its local coefficient assumptions and anchored-current specification (5.3). An implication using these names inherits their qualifications. Its Section 1.3 distinguishes a depth mismatch from a counterexample to WF7; that distinction is retained.

The two candidate mechanisms must be kept separate. Restriction of a constrained critical background at its own averages is an exact orbit identity. Applying the old constrained critical map to the nonlinear averages of an arbitrary response field is a projection to a critical orbit. Equality of those two fields is an additional assertion. Also, an identity on the physical locus does not automatically extend in variables that were fixed on that locus, such as independent currents or decoupling parameters.

## 1. Counterexample first: the current has the wrong parameter degree

Here is the obstruction to be realized in an admissible window below. It uses the **adopted** specification of `wf-room-2.md` (6.1), retained with its corrections in `removed-fix.md` (5.3). It is not a counterexample to every possible choice of a reduced current.

Use the flat pair \((\mathbf U,\mathbf J)=(1,0)\). Let \(K\) be the derivative of the raw **straightened** determining rows, \(H\) their undecoupled lift, and \(\mathscr L=D^{\mathsf T}D\) the Wilson Hessian, with the usual fixed positive action normalization. Take a real physical response direction
\[
 h=Hb,\qquad Kh=b,\qquad RD^{\mathsf T}h=0,
 \qquad \mathscr Lh=K^{\mathsf T}\lambda=:f\ne0.       \tag{1.1}
\]
The saddle characterization (I-a) of `o1-decoupled.md`, with its gate, supplies uniqueness of this lift. Section 4 constructs \(h,b,f\) explicitly, including a next-step fluctuation constraint.

Take the allowed parameter partition consisting of one torus cube \(\Delta_*\), and call its parameter \(z\). Definition D of `o1-decoupled.md` attaches \(\prod_{\Delta\in\mathsf P(\omega)}s_\Delta\) to each walk. Every nonempty walk hull meets \(\Delta_*\), exactly once in this **set** product. Therefore, by absolute convergence,
\[
 H(z)=zH,\qquad H_1(z)=zH_1=zH.                         \tag{1.2}
\]
The last equality is at the flat zero-current pair: both current corrections vanish. It holds irrespective of differences between the two walk expansions, since every term in either expansion has the same monomial \(z\). This is precisely the one-cube case admitted in `gates/o1-decoupled-gate.md` Section 2.1; (P) is automatic. It is not the operation of setting all parameters equal in a many-cube expansion, which would give different powers on different walks.

For a datum curve \(B'(\epsilon)=\epsilon b+O(\epsilon^2)\), R9 and its quadratic remainder imply
\[
 A_z(\epsilon)=\epsilon z h+O(\epsilon^2).              \tag{1.3}
\]
This follows by differentiating R9 at zero: \(DC_k(0)=0\) and \(D\mathsf W_z(0)=0\), so its other unknowns have zero first derivative. At this point \(F'(0)=0\), \(R_0=I\), and the current anchor is zero. Differentiating the adopted readout gives
\[
 \begin{split}
 \dot\lambda_z&=H(z)^{\mathsf T}\mathscr L(zh)
                  =z^2H^{\mathsf T}K^{\mathsf T}\lambda=z^2\lambda,\\
 \dot{\mathsf j}_z&=K^{\mathsf T}\dot\lambda_z=z^2f.
 \end{split}                                                   \tag{1.4}
\]
Dots mean \(\partial_\epsilon|_0\). Terms differentiating \(R_A\), \(K_A\), or the inverse \(I+[(K_A-K)H(z)]^{\mathsf T}\) multiply a zero anchor and contribute nothing. The transpose is bilinear, so its factor is \(z\), not \(\overline z\).

In contrast the **actual** current of the shifted field has derivative
\[
 \partial_\epsilon J(e^{i\eta A_z(\epsilon)})|_0=zf.    \tag{1.5}
\]
Consequently its difference from the assigned current has the nonzero bulk derivative
\[
 \partial_\epsilon\{\mathsf j_z-J(e^{i\eta A_z})\}|_0
                         =(z^2-z)f.                     \tag{1.6}
\]
For example \(z=1/2\) is strictly inside every required disc \(|z|<e^{\bar\kappa}\), and \(z^2-z=-1/4\). At \(z=1\) the defect vanishes, as physical exactness requires. Agreement there supplies no identity theorem in \(z\).

This does not contradict the readout's proved properties: it is anchored, holomorphic, covariant and physically exact. None requires equality to the current of an arbitrary decoupled field. It does obstruct composing that assigned **pair** with a map whose second component, by WF4, is the old constrained background's own current. A spatial boundary estimate cannot remove a bulk coefficient. Sections 4–6 check that this coefficient remains in the actual first-rule box and violates the proposed age-uniform WF7 bound.

## 2. What restriction and composition really prove

### 2.1 Published mechanism and the limits of this reading

The primary passages read were Balaban, CMP **109** (1987), pp. 269–280, especially (3.18)–(3.28) and (3.38)–(3.52), and p. 290 after (4.35); and CMP **119** (1988), pp. 275–276 and 279–280, including the transfer of the Section 3 construction and (3.48)–(3.49). The local OCR was read in bounded excerpts. CMP **116** is absent from `~/ym4d-papers` (including its README inventory); no direct reading or theorem from that paper is claimed. SA 10562 attributes the operators-as-data principle to its p. 3, (1.5). That attribution is a report of the outline, not an imported proof.

CMP 109 (3.38) takes a **generated critical box background**, restricts it to a smaller determining problem at its own averages, and includes the block-constant lift of its node gauge. It is used again after (3.52). Equations (3.39)–(3.47) separately retain the endpoint's two scale powers, and (3.48)–(3.52) separately allow an independent datum perturbation. They do not declare that every inserted fluctuation field is itself a critical background. Earlier, (3.20)–(3.23) removes **old datum** terms supported in a collar using an old response. After (4.35) both compared lifts have the same old index \(j\). CMP 119 changes the local units layer by layer; it does not replace an independently assigned current by an actual current on a full parameter disc.

Here is a reconstruction of the precise restriction/composition fact used in this note. Its analytic inputs are **BG**: existence and uniqueness of the regular real critical orbit, the specified holomorphic background branch, and covariance; and **T4**: its weighted datum response including the current, as in `a3-derivative.md` Sections 6–7 and the (T4) input of `wf-room-2.md`. These remain named library inputs with their P81/P82 dependencies. `a3-clauses.md` supplies continuations for its expressly specified pair systems; its force-only system is not R9, and is not substituted for R9 here.

In particular `a3-derivative.md` **Lemma 10.1** assumes a critical larger background and its (G1)–(G3), (R1)–(R3); its decay is in the **given larger sequence's** metric. Applying it with the depth-\(k\) sequence would retain the current-depth metric. It would not prove an old-depth exponential. Its smaller-tangent-space mechanism (Lemma 10.2) is re-proved next; the collar-response calculation needed after a genuine old projection is re-proved in Section 7.2. Neither use turns R9 at independent parameters into a critical field.

### 2.2 Restriction at a critical field's own averages

**Lemma CR.** Let \(S'=(\Omega'_q)\) be a separated, aligned, memberwise subsequence of \(S=(\Omega_q)\). Include its boundary level-zero rows, and use the inner-plaquette actions. Let \(U\) be a regular real constrained critical field for \(S\), with its restricted datum inside BG's radius. Then
\[
 \Phi_{S'}\big(M_{S'}(U|_{\Omega'_0})\big)
                  =(U|_{\Omega'_0})^{g},                 \tag{2.1}
\]
where \(g\) is the specified residual axial transformation, equal to one at the smaller problem's fixed nodes. The identity continues along any connected common holomorphic **critical-datum** chart on which both sides and that assigned \(g\) exist. On bonds with all incident plaquettes inside \(\Omega'_0\), the actual currents satisfy the corresponding adjoint identity.

*Proof.* A constraint-preserving variation in \(\Omega'_0\) fixes its collar bonds: sufficiently near the boundary there is no positive-level member, so each such bare bond is a determining level-zero row. Extend the variation by the unchanged field outside \(\Omega'_0\). Induct on \(q\). Every level-\(q\) average with no endpoint in \(\Omega'_{q+1}\) is unchanged: it is either a prescribed row, or its double block misses \(\Omega'_q\), in which case its finer constituent averages were unchanged by the induction hypothesis. Alignment by whole blocks is what justifies the latter alternative. The induction includes levels above the smaller depth, whose positive members are empty. An original row has no endpoint in \(\Omega_{q+1}\supset\Omega'_{q+1}\), so every original determining value is preserved.

A plaquette crossing the smaller first boundary sees only fixed collar bonds. Hence the first variation of the larger action equals that of the smaller inner action. It vanishes by criticality of \(U\). The restriction is therefore stationary at its own smaller datum; BG's regular-orbit uniqueness gives (2.1). Residual axial preparation fixes its representative. The same proof is the mechanism underlying `a3-derivative.md` Lemma 10.2, rather than an assumption of restriction compatibility.

For clarity about continuation, the axial transformation is defined by a fixed recursion of contour transports, not by a fresh existence choice of a real gauge. Each factor is a finite holomorphic expression in links, inverses and their allowed means. On an admitted datum ball, both sides of (2.1) are holomorphic. They agree on its real open ball. Expanding a matrix entry at a real interior point, all real derivatives of the difference vanish, so all complex Taylor coefficients vanish. Continue through overlapping balls in the connected chart. This proves the stated continuation; variables fixed throughout the real identity do not acquire a new identity by this argument.

The actual current is the first variation of the inner-plaquette action. On a bond with a complete incident stencil, the two action stencils agree; differentiating their link products gives \(J(U^g)(b)=\operatorname{Ad}g(b_-)J(U)(b)\). This proves the current assertion, including at complex points by the same algebra. It says nothing about an independently assigned reduced current. \(\square\)

### 2.3 The derivative retains the averaging and node terms

For a critical branch \(U(v)\), let \(m(v)=M_{S'}(\rho U(v))\), where \(\rho\) is restriction. In the representatives of (2.1), differentiating gives exactly
\[
 D\Phi_{S'}(m)\,DM_{S'}(\rho U)\,\rho DU
                            =D\big((\rho U)^g\big).       \tag{2.2}
\]
This is a composition identity, not \(D\Phi_{S'}=DU\). For a tangent \(\dot U_b\), write \(a_x=\dot g_xg_x^{-1}\). Directly differentiating \(g_-U_bg_+^{-1}\) gives
\[
 \dot U^g_b=a_-U^g_b+g_-\dot U_bg_+^{-1}-U^g_ba_+ .     \tag{2.3}
\]
For the current the extra term is \([a_-,J(U^g)_b]\). Products of gauge factors keep their order: \((U^u)^v=U^{vu}\). These formulas re-prove the transport part of the composition mechanism. At the flat branch base \(U=1,J=0,g=1\), the gauge contribution to the field is a gradient and that to the first current derivative is zero. This fact will make the counterexample independent of the permitted axial/Landau representative choice.

For the inner map alone, BG, its admitted datum balls and the explicit tower nesting give the same lemma at every lower tower. The geometric sum of contour lengths is at most \(C_L\xi_j\), so a potential bounded by \(C\|B\|/\xi_j\) gives a node condition number at most \(e^{C_L\|B\|}\), uniformly in depth. This is the content of `o1-decoupled.md` Lemma RI with its gate repairs, and of Balaban's (3.38). It admits the generated background and its **own** current hereditarily. It does not identify the assigned current (1.4) with (1.5).

## 3. Inputs needed for the counterexample, and those it avoids

The counterexample below is an implication from the following precisely matched inputs.

* **Flat lift:** the finite-volume flat constrained lift exists, is unique on the stated Landau slice, and has the physical datum interpretation. This is (I-a) of `o1-decoupled.md` and the flat instance of BG/T4. The algebra identifying its response is checked explicitly below.
* **D:** the specified walk decoupling is Definition D of `o1-decoupled.md`, including its one-cube case. Its sum at parameter one equals the corresponding undecoupled operator. Absolute convergence on the required discs is the named walk input; the one-cube computation (1.2) itself is exact algebra.
* **R9-local:** the specified finite-dimensional reduced expression is holomorphic in the small field, is built from its specified walk maps, and vanishes to second order at zero at the flat pair. The quadratic part is cancelled before parameters are inserted, as SA 10367–10373 stipulates. These are defining properties of R9, not its as-yet-open mesh-uniform supremum estimate. The walk sums used in this expression are among its specified convergent data. In the one-cube case every primitive walk sum is simply multiplied by \(z\); Section 5.3 gives a solution on the full parameter disc for each finite lattice.
* **Current-I:** the current is exactly (6.1) of `wf-room-2.md`, equivalently RF-Loc's (5.3), with the gate's current dependence and transport order retained. This is a **choice of extension**. The outline alone does not uniquely force it.
* **Old response:** T4 on the real flat first-rule box, including the normalized current response on its datum ball. Only its value at zero and its exponential row bound are needed. No complex-reference 6(c) is used.
* **Domain room:** the fixed near-identity simple-to-core lemma of `wf-room.md` Section 3, with its named Lemma T input, and the admitted old background/tower charts. The alternative for unamplified finite-volume discs is the elementary continuity argument in Section 5.3. No claim about independently closing these library inputs is made.

In particular RF-CD is **not** needed to prove the obstruction. Neither is an unproved comparison of exterior norms, the general pointwise decoupled propagator package, or a bound on the derivative of an arbitrary independent current. The zero input current is an allowed point of the independent-current domain. Failure at that point and one allowed \(z\) already disproves an identity asserted on the whole domain.

## 4. An explicit flat-based fluctuation with a nonzero current response

This adapts the Cartan critical family in `a3-profile.md` Section 3 (Codex, with its gate), re-proving the part used here and changing its profile to a zero-mean period-\(L\) fluctuation. No profile estimate from that note is used.

Fix odd \(L\ge\max(L_0,5)\). Use level-\(k\) units, bare mesh \(\eta=L^{-k}=1/N\), and a torus of a fixed side \(\ell\), a multiple of \(L\), large enough for all floors and a nonwrapping enlarged current window. Let all ambient members through level \(k+1\) be this torus; the pre-step background is \(1\). The depth-\(k\) response has only level-\(k\) determining rows. These are exactly the constant-layer sequences in RF Section 1.3.

Let \(T=\operatorname{diag}(1,-1)\), normalized by \(\tfrac12\operatorname{tr}T^2=1\). Define the periodic scalar profile, with period \(L\), by
\[
 q_0=0,\quad q_1=1,\quad q_2=0,\quad q_3=-1,
 \quad q_m=0\quad(4\le m<L).                            \tag{4.1}
\]
For bare integer coordinate \(i\in B_m=\{mN-(N-1)/2,\ldots,mN+(N-1)/2\}\), write \(i=mN-(N-1)/2+v\), \(0\le v<N\), and set
\[
 p_i(\epsilon)=\frac{\epsilon}{N^2}
       \left(q_m+\frac{v+1}{N}(q_{m+1}-q_m)\right),
 \quad \vartheta_i(\epsilon)=\arcsin p_i(\epsilon),
 \quad a_{i+1}-a_i=\vartheta_i.                         \tag{4.2}
\]
Use the branch of arcsine at zero. The values in blocks 0 and 2 are negatives, term by term, and the same holds for blocks 1 and 3. All other values vanish. Since arcsine is odd, \(\sum_{i\ {\mathrm{in\ one\ period}}}\vartheta_i=0\). Thus \(a\) is periodic with period \(LN\). Fix its additive constant by \(\sum_i a_i=0\) over that period. Define
\[
 U_2(\epsilon,x)=e^{ia_{x_1/\eta}(\epsilon)T},
 \qquad U_\mu(\epsilon,x)=1\quad(\mu\ne2).             \tag{4.3}
\]
Here a harmless translation identifies centered bare integer coordinates with the torus grid. For real \(|\epsilon|<1/8\),
\[
 |\vartheta_i|\le 2|\epsilon|/N^2,\quad
 |a_i|\le 8|\epsilon|/N,\quad
 |A_2|\le8|\epsilon|,\quad |\nabla A_2|\le2|\epsilon|,
 \quad A_2=Na_iT.                                    \tag{4.4}
\]
Indeed only four blocks have nonzero increments, so the total variation of \(a\) is at most \(8|\epsilon|/N\); its zero-mean choice lies between its minimum and maximum. The derivative bound follows by multiplying \(\vartheta_i\) by \(N^2\). The same estimates with a fixed larger constant hold on a small complex \(\epsilon\)-disc by the convergent arcsine series. The only nontrivial plaquettes are \(U_{12}=e^{i\vartheta_iT}\).

**The actual averages and the next-step constraint.** For fields (4.3), all group factors commute. Federbush's mean on its small branch is the exponential of the arithmetic mean of their angles: substituting that value in \(\sum\log(V_iV^{-1})=0\) verifies the defining equation. Each contour term in direction 2 is odd in the displacement \(x_2-y_2\) after the other displacements are fixed. Its centered average vanishes, so every site factor is one. A straight length-\(L\) segment in direction 2 has angle \(La_i\); averaging over its transverse coordinate replaces it by the sum of the \(L\) child angles. Other directions have zero angle. Induction through the actual iterate therefore gives
\[
 (\mathcal M^kU)_2(m)=e^{iB_{k,2}(\epsilon,m)T},\qquad
 B_{k,2}(\epsilon,m)=\sum_{i\in B_m}a_i(\epsilon),
 \qquad (\mathcal M^kU)_\mu=1\ (\mu\ne2).             \tag{4.5}
\]
The site factors are one at each intermediate step, not omitted after differentiation. Intermediate curvature angles are bounded by a fixed multiple of \(|\epsilon|\); decreasing \(\epsilon\) keeps every logarithm on its designated branch. The fine potential estimate also bounds every contour angle by a fixed multiple of \(|\epsilon|\), so no large-angle branch is used.

The \(B_k\) have period \(L\), and
\(\sum_{m=0}^{L-1}B_{k,2}(\epsilon,m)=\sum_i a_i(\epsilon)=0\).
Applying the same one-step average once more gives exactly
\[
                     \mathcal M^{k+1}U(\epsilon)=1.       \tag{4.6}
\]
Thus \(B_k(\epsilon)\), with \(\sup|B_k|\le8|\epsilon|\), is an actual small fluctuation in the next-step fibre. It is not an arbitrary datum incompatible with the free fluctuation coordinates. The pivot chart, if used, simply reads its nonpivot coordinates; its tangent has the same bounded coordinate size. Soft gauge penalties do not remove this allowed datum.

**Criticality and the current, by hand.** Across a block boundary as well as inside one,
\[
 p_i-p_{i-1}=\epsilon(q_{m+1}-q_m)/N^3\quad(i\in B_m).
                                                               \tag{4.7}
\]
For the action \(\sum_p(1-\tfrac12\operatorname{tr}U_p)\), its derivative with respect to the link angle \(a_i\) is
\(\sin\vartheta_{i-1}-\sin\vartheta_i
 =-\epsilon(q_{m+1}-q_m)/N^3\).
Changing from a link angle to its potential contributes \(\eta\); dividing by the fine pairing volume \(\eta^4\) contributes \(\eta^{-4}\). Hence the actual current in level-\(k\) units is exactly
\[
 J_2(U(\epsilon),x)=-\epsilon(q_{m+1}-q_m)T,
 \qquad J_\mu=0\quad(\mu\ne2).                         \tag{4.8}
\]
Direction-1 staples cancel because the field is independent of coordinate 2. The other plaquettes are trivial. A different fixed Wilson normalization multiplies (4.8) by a fixed positive constant, with no depth dependence.

To check constrained criticality against **all** variations, put the multiplier \(-\epsilon(q_{m+1}-q_m)T\) on each coarse direction-2 row. It is independent of coordinate 2. In the angle pairing, the adjoint straight average contributes \(L^{-3}\) per step: a link occurs in \(L\) segments, each with weight \(L^{-4}\). After \(k\) steps it contributes \(N^{-3}\), exactly (4.7). The site-factor variation is a coarse gradient; it pairs to zero with this divergence-free multiplier. For perpendicular colour variations both the action derivative and this paired average derivative vanish: invariance under every constant conjugation by \(e^{itT}\) forces their linear functionals to vanish on the rotating colour plane. This verifies the full Euler–Lagrange equation, not just its Cartan restriction. The chart at the flat reference has \(D^{\mathsf T}A=0\), because its sole component is independent of direction 2, so it also satisfies the Landau slice.

Differentiate at \(\epsilon=0\), and write \(h_k=\dot A\), \(b_k=\dot B_k\). Equations (4.4)–(4.8) prove
\[
 Kh_k=b_k,\quad RD^{\mathsf T}h_k=0,\quad
 h_k=Hb_k,\quad \|h_k\|_{1}\le C,\quad \sup|b_k|\le8,
 \quad (\mathscr Lh_k)_2(x)=-(q_{m+1}-q_m)T.             \tag{4.9}
\]
The equality \(h_k=Hb_k\) follows from Flat lift uniqueness applied to the displayed equations. In each block with \(q_{m+1}-q_m=1\), the norm of the last expression is **one for every bare mesh**. This is stronger than a nonzero but mesh-dependent test, and supplies the uniform lower bound needed below.

## 5. The actual old window, its nonlinear datum, and admissibility

### 5.1 Fixing the geometry before increasing the age

Fix the old level \(j=1\). Then
\[
             \sigma=\sigma_1=L^{1-k}=L\eta\longrightarrow0.
                                                               \tag{5.1}
\]
Choose all fixed local-inverse and tower sizes first, then \(M\), and a compatible torus side \(\ell\) larger than ten times the enlarged window diameter. They remain fixed as \(k\) increases. Use the one-cube parameter partition from Section 1; its side can be the fixed \(\ell\), and its parameter-cube hypothesis (P) and count hold at every depth. A local box may occupy only part of that parameter cube. Its fine-cube hull is the one cube, so the bounded number of fine cubes in WF13a is also respected. This instance uses the one-cube option of D; it makes no claim about a specification that expressly excludes that option.

Choose a bond \(b_*\) in a block where \(q_{m+1}-q_m=1\), and an old base point next to it. Translate the period of (4.1), if necessary, so the bond lies in the central part of an assigned current window. Group the finitely many partition directions prescribed in WF13a. Their cutoff \(\zeta\) equals one on a neighborhood of the tested old member and vanishes outside its fixed enlarged current window \(R\). More explicitly, include every partition function whose support meets the chosen central neighborhood; excluded supports miss it, so \(\sum\zeta_\square=1\) proves this plateau property. The grouping has bounded size because the original supports have bounded overlap and fixed current-scale reach. Enlarge \(R\) by the fixed amount allowed in WF13a. We may fix \(d>0\), independent of \(k\), so that
\[
 \zeta=1\text{ within distance }dM\text{ of }b_*,
 \quad \operatorname{supp}\zeta\subset R,
 \quad \operatorname{dist}_\infty(b_*,R^c)>2dM.          \tag{5.2}
\]
All stencils of the tested member lie in this plateau. The member can be a fixed number of old \(M\)-cubes around the base point; their physical diameter is \(O(M\sigma)\), which fits (5.2) for large age.

Use **exactly** the old first-rule tower,
\[
 T_0=R,\qquad
 T_1=\bigcup\{Q:\ Q\text{ is an aligned }
       \mathfrak M\sigma\text{-cube},\quad
       d_\infty(Q,R^c)>\rho\eta\},\qquad T_q=\varnothing\ (q>1).
                                                               \tag{5.3}
\]
Any point deeper than \(\rho\eta+\mathfrak M\sigma\) lies in \(T_1\): its containing aligned cube loses at most \(\mathfrak M\sigma\) of that depth. Thus the tested stencils lie in \(T_1\) for all sufficiently large ages. This is the depth-one instance of RF-G, proved here directly. Its local scales are at most \(\sigma\); every old weighted path has length at least its physical sup displacement divided by \(\sigma\). In particular a row whose averaging carrier misses the plateau is at weighted distance at least
\[
                         dM/\sigma-C_L                  \tag{5.4}
\]
from the test. The carrier correction is bounded by \(C_L\sigma\) because this tower has depth one. The sequence (5.3) is contained memberwise in the constant ambient sequence and satisfies the stated separation and alignment rules. No agreement of the depth-\(k\) and depth-one sequences in the center is asserted.

### 5.2 Differentiating the actual nonlinear box map

Let \(\mathcal C_R(V)\) denote the **actual current** of the old constrained critical background for (5.3), at the datum \(M_{T(R)}(V)\), returned in WF4's admitted Landau representative. This uses the actual nonlinear iterate on every determining carrier, including the lower collar rows. Consider the actual WF3 field at \(t=0\),
\[
             V_z(\epsilon,\nu)=e^{i\eta\nu\zeta A_z(\epsilon)}.
                                                               \tag{5.5}
\]
For a fixed finite lattice every displayed map is holomorphic near zero. Therefore the chain rule, applied to these **nonlinear** maps, gives
\[
 \partial_\epsilon\partial_\nu\mathcal C_R(V_z)|_{0,0}
 = z\,\mathcal J_R\,DM_{T(R)}(1)[\zeta h_k],          \tag{5.6}
\]
where \(\mathcal J_R\) is the current derivative of the old critical background with respect to its raw logarithmic datum at 1. This is a necessary Taylor coefficient of the nonlinear WF map. It is not a proposal to replace WF3 by a linear average at finite fields.

Apply Lemma CR to the exact real critical family (4.3), then differentiate at zero. It gives
\[
                  \mathcal J_R DM_{T(R)}(1)[h_k]=f_k
                  \quad\text{at the tested bonds},       \tag{5.7}
\]
where \(f_k=\mathscr Lh_k\). All currents here are initially in level-\(k\) units. Any assigned node/axial/Landau transformation equals the identity at the flat datum, and its differentiated conjugation multiplies the zero base current. Hence (5.7) is valid for the actual assigned current as well as for an auxiliary canonical representative.

The raw datum difference
\[
                   b^{\rm tail}=DM_{T(R)}(1)[(\zeta-1)h_k]
                                                               \tag{5.8}
\]
vanishes on every carrier in the plateau, by locality of the actual average. Its size is at most \(C\sigma\): a depth-one raw row is a mean of contour integrals of total physical length \(\le C_L\sigma\), and \(\sup|h_k|\le C\). A level-zero row has the smaller length \(\eta\). There are at most \(C_M\eta^{-4}\) rows, since there are only levels zero and one and finitely many orientations per fine site in a box of fixed current-scale size. No mixed native counting estimate is being used.

The old response input T4 gives for each unit datum component a current derivative bounded, in the test's old normalized units, by \(C e^{-\theta d_T(b_*,c)}\). Sum this finite set of components, use (5.4) and (5.8), and recall \(\eta=\sigma/L\). The result is
\[
 \left|\sigma^3\mathcal J_R b^{\rm tail}(b_*)\right|
       \le C_M\sigma^{-3}e^{-\theta dM/\sigma}.          \tag{5.9}
\]
The factor \(\sigma^{-3}\) is retained explicitly; it is harmless compared with this exponential. This elementary count is sufficient because the old depth is fixed at one. It is not asserted as a multiscale ball count at general depth.

Combining (5.6)–(5.9), the actual inner current has mixed derivative
\[
 \partial_\epsilon\partial_\nu
    [J^{\rm box}_{1,\square}]_{\rm old}(b_*)|_{0,0}
       =z\sigma^3 f_k(b_*)+\mathcal E_k(z),\qquad
 |\mathcal E_k(z)|\le C_M|z|\sigma^{-3}
                         e^{-\theta dM/\sigma}.          \tag{5.10}
\]
The raw-to-Landau axial preparation can make a **datum** change appear as a gauge gradient away from its original support. This does not invalidate the calculation: it was performed first in the raw datum, where (5.8) is localized. At the flat point a pure gauge datum has zero first current response, and conjugating the zero current adds no first derivative. Transporting afterwards therefore gives exactly the same coefficient. The reasoning includes the node factors without pretending that their condition-number bound implies proximity between two unrelated gauges.

### 5.3 Room on the parameter discs

All fixed input simple and tower clauses are strict at \((1,0,0)\). At each finite lattice they form a finite family: there are finitely many lattice regions, rules and truncations. BG gives their branches near the identity. For the single parameter \(z\), every primitive decoupled walk sum is \(z\) times its undecoupled sum, by (1.2)'s argument. Thus its entries are bounded even on the closed disc \(|z|\le R=e^{\bar\kappa}\). The finite reduced formula R9-local composes these entries with the near-zero nonlinear averages and action remainders. It is consequently defined on a common field neighborhood for this closed parameter disc, with finite coefficient and derivative bounds. This uses only finite-lattice analytic bounds; their constants may depend on \(k\). It uses neither a pointwise walk upgrade nor a mesh-uniform inverse estimate.

Here is the needed local existence argument, without a mesh-uniform estimate imported from a run. R9's equations at the flat pair have the form
\(X=O((|\epsilon|+|X|+|A_1|)^2)\),
\(A_1=O((|\epsilon|+|A_1|)^2)\),
uniformly on \(|z|\le R\), with finite constants that may depend on \(k\). Choose a ball of radius \(C_k|\epsilon|\), then choose \(|\epsilon|\) sufficiently small that the derivative norm is \(<1/2\) and the map sends the ball into itself. Successive substitution converges geometrically there, and the holomorphic iterates converge locally uniformly. The same argument in the current equation uses \(\|(K_A-K)H(z)\|<1/2\). This proves (1.3)–(1.4) uniformly on that closed disc and gives an actual small nonzero response holomorphic throughout its interior. No inverse of \(z\), and no identity \(KH(z)=I\), was used.

A proposed identity on the **full** open disc must in particular hold at \(z=1/2\). The construction just given supplies one common nonzero datum radius on the full disc for each finite \(k\); this radius may decrease with \(k\). It is not a proof of the general [PW] estimate or of its depth-independent existence radius. If a different prescription for the reduced expression lacks the defining analytic properties of R9-local, the counterexample is conditional on supplying them; that would also leave its response map undefined as a consumer here.

There is fixed amplified room for the example on the full parameter disc. The explicit jets (4.9) give uniform first-order field and current bounds; by reducing \(\epsilon=\epsilon_k\) further, the nonlinear remainders are smaller than those bounds uniformly there. Thus \(\|A_z\|_1+\|\mathsf j_z\|\le C_R|\epsilon|\). Choose fixed simple radii and then a smaller fixed \(c_\nu\) according to Domain room, and take \(\delta_k=C_b|\epsilon|\), with \(C_b\ge8\) also bounding the free coordinates. For
\(|\nu|<c_\nu\alpha_k/\delta_k\),
the complete shifts \(\nu\zeta A_z\) and \(\nu\zeta\mathsf j_z\) have norm \(\le C_Rc_\nu\alpha_k\). The cutoff's fixed derivative bound is included in \(C_R\). The extra unamplified term for \(0\le t\le1\) costs only \(C_R|\epsilon|\), and is admitted by decreasing \(\epsilon_k\). The simple-to-core lemma admits them with strict margins. The box map and its smaller towers lie in their admitted charts by the same small-radius choice, using BG, the simple-to-tower bound and Lemma CR for the generated background. One may take constant sufficiently small running radii, whose constant inverse couplings satisfy the stated flow inequality.

This constructs a genuine nonzero \(\epsilon_k\) for each finite lattice. It does not need a positive lower bound on these choices as \(k\to\infty\): a uniform WF7 inequality implies its derivative inequality at zero separately at every \(k\). The flat background, every hereditary input clause, the first-rule tower, the independent current, and the small-response domains are compatible with the test. No numerical computation is involved.

## 6. A removed-field lower bound, with the assigned transports

### 6.1 Which difference is being tested

Use the near-window replacement from the assigned outer R8/R10 pair to WF4's old critical box pair. At \(t=0\), the field in the latter is exactly (5.5). In the plateau (5.2), localizing the outer direction does not change its field or its independent-current increment: its current is \(\nu\mathsf j_z\). The complementary outer directions vanish on the tested member. Let \(\mathcal R_{j,k}(\epsilon,z,\nu)\) be the difference of these two local pairs in their admitted common coordinates, subtracting the value at \(\nu=0\). This is the composition/replacement difference whose identification is needed to apply RF (7.4) to this WF7 consumer.

At the flat datum the unshifted original background and every box background are exactly 1, with current zero. Thus replacing the unshifted background gives no term that could cancel the coefficient below. A decomposition that introduces another bulk term to cancel it is a different, enlarged removed-term statement; Section 7 writes that term explicitly.

The comparison uses the **assigned** current. It does not falsely assert that R8 requires the actual current of every shifted field. Precisely that distinction produces the obstruction: the inner map carries the actual current, while the input pair carries Current-I. If a proposed window uses a different off-physical current continuation, it must specify it and recheck this coefficient.

### 6.2 The lower bound

By (1.4), the outer current's mixed derivative, in old units, is \(z^2\sigma^3 f_k\). By (5.10), the inner one is \(z\sigma^3 f_k+\mathcal E_k\). Therefore
\[
 \partial_\epsilon\partial_\nu
        [\mathcal R_{1,k}]_J(b_*)|_{0,0}
       =(z^2-z)\sigma^3f_k(b_*)-\mathcal E_k(z).         \tag{6.1}
\]
Here \(|f_k(b_*)|=1\). Fix \(z=1/2\). Since
\[
 \sigma^{-3}e^{-a/\sigma}=o(\sigma^3)\quad(a>0),
                                                               \tag{6.2}
\]
the norm in (6.1) is at least \(\sigma^3/8\) for all sufficiently large \(k\). For a hand proof of (6.2), put \(x=a/\sigma\) and use the eighth term of the positive exponential series:
\(e^x\ge x^8/8!\).
Then \(\sigma^{-3}e^{-a/\sigma}\le8!a^{-8}\sigma^5\), whose ratio to \(\sigma^3\) tends to zero.

The proposed WF7 bound, with constants independent of \(j,k\), would imply
\[
 \big|\partial_\epsilon\partial_\nu
           [\mathcal R_{1,k}]_J(b_*)|_{0,0}\big|
             \le C_R C_b\sigma e^{-cM/\sigma}.          \tag{6.3}
\]
Indeed first divide its increment estimate by \(|\nu|\) and pass to \(\nu=0\), then divide by \(|\epsilon|\), using \(\delta_k=C_b|\epsilon|\), and pass to zero again. Both limits are derivatives of the actual admitted holomorphic maps.

Equations (6.1)–(6.3) contradict each other for every fixed \(C_R,c>0\). Explicitly, (6.3) and the lower bound would give
\(\sigma^2e^{cM/\sigma}\le8C_RC_b\).
But \(e^x\ge x^3/3!\) makes the left side at least
\((cM)^3/(6\sigma)\), which diverges along (5.1). Allowing \(c\) to depend on fixed \(M\), as SA does, does not change this argument as long as \(c>0\).

This derivative contradiction also gives finite nonzero windows. Choose a large \(k\) for which the displayed strict inequality holds. Continuity of the first derivative in \(\epsilon\), then the defining derivative limit in \(\nu\), gives sufficiently small nonzero real \(\epsilon,\nu\) violating WF7 inside the already chosen room. Thus the argument does not merely report nonidentical formal series.

### 6.3 Other natural cutoff conventions and node transport

If the direction is localized by **recomputing** Current-I at \(\zeta A_z\), rather than by multiplying its assigned increment by \(\zeta\), its mixed derivative is
\[
            z^2K^{\mathsf T}H^{\mathsf T}
                           \mathscr L(\zeta h_k).       \tag{6.4}
\]
At the tested bonds this equals \(z^2(f_k+r_k)\), where \(r_k\) is small at the **current** distance to the cutoff. Here is the estimate, including its hypothesis. Use the flat column gradient response from T4 at depth \(k\), and the local transpose-row bound from RF-Loc. For a row \(c\) within a bounded current distance of the test, integration by parts gives
\[
 [H^{\mathsf T}\mathscr L((\zeta-1)h_k)](c)
       =\eta^4\sum_p DH(p,c)D((\zeta-1)h_k)(p).         \tag{6.5}
\]
The second factor has bounded supremum by (4.9) and the cutoff bound, and vanishes within distance \(dM-O_L(1)\) of \(c\). The first is at most \(Ce^{-\theta d(c,p)}\). There are \(O(\ell^4\eta^{-4})\) plaquettes, so the physical sum is at most \(C\ell^4e^{-\theta dM}\). The local row transpose has bounded force norm and bounded carrier reach. Consequently
\[
                    |r_k(b_*)|\le C\ell^4e^{-\theta dM}.
                                                               \tag{6.6}
\]
Choose \(M\) large, and \(\ell\) a compatible fixed multiple of \(M\), so this is less than \(1/16\); the existence of this choice follows again from the exponential series dominating every fixed power. This choice precedes \(k\). Its contribution in old units is at most \(\sigma^3/64\) at \(z=1/2\), so the lower bound \(\sigma^3/8\) still follows after increasing the age. Formula (6.6) is a current-depth estimate, not an old-depth estimate in disguise. It also explains why the cutoff convention cannot repair the bulk factor.

Finally, all prescribed representative factors take the identity value at the flat pair. In a current expression \(\operatorname{Ad}(g)J\), differentiating in \(\epsilon,\nu\) adds only terms containing a zero lower-order current at \((0,0)\). The mixed coefficient is unchanged. Equivalently, (2.3) adds a pure gauge tangent whose flat current is zero. This includes the accumulated plain/straightened-average node factor, the direct-path axial preparation of the raw datum, the Landau factor, and their correctly ordered products. A bounded, nontrivial **constant unitary** choice would only conjugate (6.1) and preserve its norm. No assigned transport can change its parameter degree from two to one.

### 6.4 The two box currents must not be identified

Specification (6.1) of `wf-room-2.md` says that a removed current is the difference of its readouts for the original and box systems, each with its own lift and anchor. Its Section 6.3(S6) is consequently a comparison between **two reduced readouts**. It is not an assertion that the box readout is WF4's actual current on arbitrary parameter discs.

For example, apply the old one-cube readout, with lift \(zH_R\), to the *actual* WF4 box field in (5.5). At zero its field tangent is \(z h_R\), where \(h_R\) is the derivative of the actual box's Landau potential in the raw datum direction \(DM_{T(R)}(1)[\zeta h_k]\). After the prescribed raw-to-straightened and node-datum conversion, write this as \(h_R=H_Rb_R\); the conversion is retained, not replaced by the identity. Differentiated criticality gives \(\mathscr L_Rh_R=K_R^{\mathsf T}\lambda_R\). Its actual current tangent is \(z\mathscr L_Rh_R\). Its reduced readout tangent, by exactly (1.4), is \(z^2\mathscr L_Rh_R\). Thus the difference of the two reduced readouts can cancel the bulk coefficient to first order; replacing that reduced box current by WF4's current restores precisely the missing coefficient \((z^2-z)\mathscr L_Rh_R\). Decoupling the old field a second time is another map again, not WF4.

This supplies a useful scope test. The counterexample does **not** refute a same-depth instance of (S6), and it does not silently rename its second readout an actual current. It refutes the proposed identification of the *complete assigned step pair* with the old critical pair. The direct replacement window of Section 6.1 is an explicit instance: its field is the stipulated nonlinear WF3 field, its inner pair is WF4, and its outer current is Current-I. The completion of this replacement by differences between two reduced readouts must also carry the displayed bulk bridge term. If an off-physical window extension is instead defined afresh, without that complete-pair identity, no such conclusion about its separately specified removed terms follows. The outline asserts its global window identity only on complete physical pairs; it permits that latter possibility.

**Conclusion of the counterexample.** Under the matched inputs of Section 3, the requested old-depth identity for the complete assigned pair on the full decoupling discs is false for Current-I and D. The direct near-window replacement just defined has a bulk current defect of order \(\delta_k\sigma_j^3\) already at its first response coefficient, and cannot have only \(\delta_k\sigma_j e^{-cM/\sigma_j}\). This is a counterexample to this assigned-pair composition route to WF7, not to every window extension allowed by the outline. There is no claim that the outline's incompletely specified removed formulas have a unique continuation off the physical locus.

## 7. The smaller true statements

### 7.1 An exact identity with a bulk defect

Write all pairs in the same admitted member chart, with potentials in level-\(j\) units and currents in their corresponding cubic units. Let \(q\) be the assigned current-step pair, including its specified transports. Let \(V\) be its underlying shifted configuration, as in WF3. Form a second pair \(p\) by first applying the **global old truncated critical map** to the actual datum \(M_{S^{\le j}}V\), and taking that background's actual current. Transport it by the explicit restriction representative of Lemma CR to the chosen box chart. Let \(p_R\) be the actual old box pair WF4 in that chart. These definitions require their own admitted domains; they do not equate any of the maps.

Define the bulk defect and the anchored increment by
\[
 E_j=q-p,\qquad \Delta_\nu f=f(\nu)-f(0).
\]
Then ordinary addition in this fixed chart gives the exact identity
\[
 \Delta_\nu(q-p_R)
       =\Delta_\nu E_j+\Delta_\nu(p-p_R).               \tag{7.1}
\]
Every average in the definition of \(p\) and \(p_R\) is nonlinear; (7.1) changes none of them. If the assigned transport of \(p\) differs from its restriction transport, place that difference explicitly in \(E_j\). It cannot be discarded on the ground that both transports have bounded condition number.

In the example, the old global projection, just like the box projection, has mixed current coefficient \(z\sigma^3f_k\) up to the distant cutoff response. Thus
\[
 [\partial_\epsilon\partial_\nu E_1]_J(b_*)
            =(z^2-z)\sigma^3f_k(b_*)
                   +O(C_M\sigma^{-3}e^{-\theta dM/\sigma}).
                                                               \tag{7.2}
\]
This is why a theorem with an explicit defect is strictly smaller than the proposed theorem with an exponential alone. It has content even when the old comparison is perfect: the first summand need not vanish.

### 7.2 The old projection really does reduce to a collar problem

Here is the positive part of Balaban's composition mechanism, with its extra hypotheses visible. Let \(W=\Phi_{S^{\le j}}(M_{S^{\le j}}V)\), initially in a constraint representative in which its prescribed raw rows equal those of \(V\). On a same-old-depth meet with the first-rule tower, put
\[
 v_R=\operatorname{coord}_R(M_{T\cap S^{\le j}}V),\qquad
 w_R=\operatorname{coord}_R(M_{T\cap S^{\le j}}W),\qquad
 \beta=w_R-v_R.                                      \tag{7.3}
\]
Use logarithmic data in a common admitted chart for this subtraction. On every common determining row whose full carrier lies in the agreement region, the raw averages agree **exactly**, by the defining constraint on \(W\). Thus \(\beta\) is supported on the newly introduced collar rows. This statement is made before axial preparation, so no support property of a nonlocal gauge transformation is assumed.

Lemma CR, followed by its explicit representative recursion, gives
\[
 p=F_R(w_R),\qquad p_R=F_R(v_R),                       \tag{7.4}
\]
where \(F_R\) is one and the same old critical pair map, including its prescribed conversion to the output chart and its **actual** current. For a pure tower this argument requires the ambient old sequence to contain that tower memberwise and to be constant at its top in the enlarged interior; this holds in the counterexample. In a layered region the argument applies to the meet. If that meet is not the prescribed WF4 determining problem, (7.4) is a statement about the meet map and still needs a separate identification with WF4; no map is silently changed. This is the restriction used in CMP 109 (3.38), not a restriction of an arbitrary inserted field. The equality persists for complex old data by Lemma CR's identity-theorem argument. Dependence of \(V\) on an independent current or on decoupling parameters is harmless here: it is composed into the datum of an already defined old map, rather than used to claim that \(V\) is critical.

The first-rule erosion and the walk read-set loss from RF-G give
\[
 D_j\ge dM/\sigma_j-e_j/\sigma_j-b_*                 \tag{7.5}
\]
for this **old-to-old** comparison, with the constants and hypotheses of RF-G. In the depth-one example the elementary proof is (5.3)–(5.4), and needs no pending theorem. For general depth, the scalar erosion sum follows directly by summing a geometric series:
\[
 \frac{e_j}{\xi_j}
   =\sum_{q<j}\frac{\rho\xi_q+\mathfrak M\xi_{q+1}}{\xi_j}
   \le\frac{\rho+L\mathfrak M}{L-1}.                  \tag{7.6}
\]
Symmetric agreement on both families' full read sets, rather than just this scalar inequality, is still required when RF-CD is invoked. Equations (7.3)–(7.4) are the actual-map reduction; the quantitative estimate below states precisely what its datum and transport bounds must supply.

**Collar response lemma.** Let a finite-dimensional holomorphic old pair map \(F_R\), in its assigned output chart, obey
\[
 \|DF_R(u)e_c\|_x\le K e^{-\theta d(x,c)}               \tag{7.7}
\]
on the common datum neighborhood under discussion. Assume a datum ball of radius \(r>0\), in the normalized input supremum norm, remains available about every point of each segment from \(v(\nu)\) to \(w(\nu)=v(\nu)+\beta(\nu)\). Suppose \(\beta\) and \(\beta'\) are supported on a fixed set \(C\), with \(d(x,C)\ge D\), throughout the multiplier segment. Set
\[
 \begin{aligned}
 B&=\sup_\nu\sum_{c\in C}|\beta_c(\nu)|,
 &b&=\sup_\nu\sum_{c\in C}|\beta'_c(\nu)|,\\
 a&=\sup_\nu\max(\|v'(\nu)\|_\infty,\|w'(\nu)\|_\infty).
 \end{aligned}                                                 \tag{7.8}
\]
Coordinates in these sums are normalized datum coordinates; no foreign pillar count is substituted. Then
\[
 \|\Delta_\nu\{F_R(w)-F_R(v)\}\|_x
       \le K|\nu|\bigl(b+aB/r\bigr)e^{-\theta D}.      \tag{7.9}
\]
A fixed factor can be put in front if the available radius is stated with a strict fraction.

*Proof.* The fundamental theorem of calculus on the real segment in the datum ball gives
\[
 F_R(w)-F_R(v)=\int_0^1 DF_R(v+t\beta)\beta\,dt.
\]
Differentiate in \(\nu\). The derivative of the base point is \((1-t)v'+tw'\), of norm at most \(a\). For a unit input direction \(u_0\), apply the one-variable Cauchy formula to \(DF_R(u+zu_0)e_c\) on \(|z|<r\). By (7.7),
\[
 \|D^2F_R(u)[u_0,e_c]\|_x
                   \le (K/r)e^{-\theta d(x,c)}.
\]
Expand only the collar vector \(\beta\) in its coordinates; no expansion of the other direction is needed. The differentiated integral is therefore bounded by
\(K e^{-\theta D}(b+aB/r)\).
Integrating it from zero to \(\nu\) proves (7.9), also for a complex multiplier segment. All sums are finite. This proves the lemma without a mesh-uniform counting assertion. \(\square\)

The same proof can retain the weights \(e^{-\theta d(x,c)/2}\) in the two sums in (7.8) and put \(e^{-\theta D/2}\) outside. This follows by the elementary inequality
\(e^{-\theta d(x,c)}\le e^{-\theta D/2}e^{-\theta d(x,c)/2}\).
It is often the useful version: a **native** summation estimate can bound these weighted collar sums. Merely bounding each collar coordinate by a supremum does not bound an unweighted sum uniformly in the mesh.

In particular, if the actual averaged data and their representatives supply
\[
 b\le C\delta_k\sigma_j,\qquad
 a\le C\delta_k\sigma_j,\qquad B\le Cr,
                                                               \tag{7.10}
\]
in either justified version of those sums, then (7.5), (7.9) and (7.6) give the old-depth exponential for \(\Delta_\nu(p-p_R)\). Weighted response (7.7) must include all components claimed in the output pair; a current-only bound does not bound its assigned gauge. T4 together with the representative hypothesis (AX) in `wf-room-2.md` Lemma D is the relevant named input. The general actual-map bounds (7.10), all required core room and the external node comparison are not proved here. The lemma identifies them rather than concealing them in a purported composition identity.

### 7.3 What WF7 can state for the original assigned pair

Combining the proved algebra (7.1) with an old comparison supplied as in Section 7.2 yields the conditional, honest replacement
\[
 \|\Delta_\nu(q-p_R)\|_{j,X}
 \le \|\Delta_\nu E_j\|_{j,X}
       +C_R|\nu|\delta_k\sigma_j e^{-cM/\sigma_j}.     \tag{7.11}
\]
Use the native weighted version of (7.9) when summing over a member. If an assigned representative lies outside the common-chart comparison, its actual transport difference is another term on the right. RF-CD supplies its stated anchored-current/node estimate only after **all** its Pair, Field, Loc and Node hypotheses have been verified for the systems being compared. Its retained node factor \(C_H(1+C_H\alpha_0)\) does not disappear. RF-CD, including that conclusion, is pending same-model input here.

Without any old compatibility, individual first-response and current-readout bounds on the common multiplier disc give the still smaller, unconditional-in-composition statement
\[
 \|\Delta_\nu(q-p_R)\|_{j,X}
       \le C_R|\nu|\delta_k\sigma_j.                 \tag{7.12}
\]
Its analytic premises are explicit: each of the two increments on the left separately has the usual first-response bound in this norm and chart. The triangle inequality proves (7.12), with the sum of their constants. These bounds remain the named pointwise first-system and old-background inputs, not a conclusion of (O1) alone. Our example does not disprove (7.12): \(\sigma_j^3\le\sigma_j\).

For a genuine same-**current**-depth removed comparison satisfying RF-CD's hypotheses, RF-G instead gives
\[
 \|\Delta_\nu R^{\rm same}_{j,k}\|_{j,X}
       \le C_R|\nu|\delta_k\sigma_j e^{-cM}.          \tag{7.13}
\]
The proof is RF (7.5) followed by the change of units: the potential has one power of \(\sigma_j\), the current three, and neither operation changes the dimensionless distance in the exponential. This remains an implication from pending RF-CD; it is not a bound for the bulk bridge in Section 6.4. Statements (7.11)–(7.13) must not be interchanged.

### 7.4 A viable change of extension, not an identity already proved

Balaban's CMP 109 Section 3 route, with the hereditary admission checked on pp. 277–280, is to insert the global old critical map **before** comparing it with a box. On a physical real endpoint that is already critical, Lemma CR identifies that insertion with restriction. Along the interpolation it is simply the explicitly composed map
\[
 V\longmapsto \Phi_{S^{\le j}}(M_{S^{\le j}}V),
                                                               \tag{7.14}
\]
with its own current and its node transport. No assertion that the interpolating \(V\) itself is critical is needed.

For example, let \(V(t)\) join two complete physical critical endpoints whose determining sequences both contain this old truncation. Assume the projected path stays in the admitted charts, and let \(G_j\) be an old gauge-invariant action member on the pair domain. The endpoint identities and the one-variable fundamental theorem give
\[
 G_j(P_1)-G_j(P_0)
 =\int_0^1\frac{d}{dt}
   G_j\!\left(\Phi_{S^{\le j}}(M_{S^{\le j}}V(t)),
              J\bigl(\Phi_{S^{\le j}}(M_{S^{\le j}}V(t))\bigr)\right)dt,
                                                               \tag{7.15}
\]
with the stated representative factors included. The derivative of the integrand is linear in the direction of \(V(t)\). Inserting the finite identity \(\sum_\square\zeta_\square=1\) into that direction therefore decomposes (7.15) into window derivatives. The chain rule keeps both \(D\Phi\) and \(DM\), and (2.3) keeps the transport derivatives. This re-proves the relevant composition of steps; it is an endpoint action identity, not equality to Current-I at all complex interpolation points.

One may define an off-physical window extension by exactly these projected formulas, with complex \(s\) and independent currents entering through \(V\). The old box then compares to an old projection, as in (7.3)–(7.9), so an age-enhanced boundary estimate is possible. Doing this replaces the original assigned-pair continuation; compatibility with every local member, its read sets, its fine brackets and its declared domains must still be established. CMP 119's changes of local units do not supply those missing equalities. This live alternative is why the present result is not a no-go theorem for rank 4 or for the Sussman–Alpoge program.

## 8. Scope checks and remaining alternatives

The negative result has a narrow target: Current-I, Definition D including its one-cube case, and a direct replacement by WF4's actual critical pair. Its counterexample is not merely the mismatch of sequences already recorded in RF Section 1.3. It has compatible simple/tower domains, actual nonlinear averages in the next-step fibre, a nonzero current coefficient uniform in depth, and the assigned transports. Nor is the adapted Cartan family by itself a counterexample: it is critical and obeys the physical restriction identity. The obstruction is the additional decoupling factor in the current readout.

The relevant alternatives have different outcomes:

| Alternative | What the written argument establishes |
| --- | --- |
| Restrict a physical critical background, then continue in its critical datum | Lemma CR and (2.2) hold; this is a smaller domain than the asserted independent-parameter identity. |
| Keep Current-I and identify its box readout with WF4's current | Equations (1.4)–(1.6), (5.10) and (6.1) disprove this at \(z=1/2\); (6.4)'s recomputed-cutoff convention also fails under its stated extra inputs. |
| Use a different assigned gauge to cancel the defect | At the flat zero-current base the mixed current coefficient is unchanged, by (2.3) and Section 6.3. |
| Localize at depth \(k\) and then change units | RF-G gives (7.13), conditionally on RF-CD; the exponent remains a current-distance exponent. |
| Change the current extension or the decoupling prescription | A live specification change, not ruled out. It must be tested for physical exactness, splitting, first-order bounds, full-disc room and its actual old composition. No theorem here says all such choices fail. |
| Project to the old critical map first | The exact reduction (7.3)–(7.4) and endpoint identity (7.15) are available on admitted charts. The quantitative hypotheses of (7.9)–(7.10) and compatibility with the complete window filing remain to be proved. |

No evidence here rules out the last two alternatives, and no universal obstruction is inferred from the failure of the first proposed extension. The rows 113, 116, 126 and their gates 129 and 125 remain the sources of the named room, lift and current inputs; rows 131/136 are used only with RF's explicitly pending status. Reading those sources, or the published papers, is not a proof of their outstanding analytic premises. No audit, gate verdict or repository status is changed.

## Result

**Proved by the written arguments, with the indicated named inputs:**

* From **BG**, memberwise containment, whole-block alignment, the fixed collar and admitted datum charts: **Lemma CR**, restriction at a critical background's own nonlinear averages, with its residual node transport. Differentiation gives (2.2)–(2.3), not an equality of lifts with different row spaces. The endpoint composition (7.15) follows on those domains.
* From **Flat lift, D, R9-local and Current-I**: the one-cube first response has field coefficient \(zh_k\), assigned-current coefficient \(z^2f_k\), and actual-current coefficient \(zf_k\). Section 4 proves by hand an exact constrained critical family with \(\mathcal M^{k+1}U=1\), bounded fluctuation coordinates and \(|f_k(b_*)|=1\), for every depth.
* Adding **old T4 and Domain room**: Sections 5–6 give an admissible first-rule window, on the full decoupling disc, for which the direct assigned-pair replacement by WF4 has a mixed current coefficient at least \(\sigma_1^3/8\). This contradicts every age-uniform bound \(C\sigma_1e^{-cM/\sigma_1}\), \(c>0\). The independently assigned current and node factors are retained. The result refutes this proposed composition route; it does not refute every possible off-physical window extension or the comparison between two reduced readouts alone.
* Exact algebra gives the defect identity **(7.1)**. The weighted response premise (7.7), its datum room and the explicit collar sizes give **(7.9)** by integration and Cauchy's formula. With the additional bounds (7.10), this yields **WF7 with the bulk defect retained**, (7.11). Individual first-response bounds give (7.12). The same-depth exponential (7.13) is an implication from **RF-G/RF-CD**, whose Claude gate is pending, with all their Pair, Field, Loc and Node hypotheses retained.

**Where rank 4 then stops.** For the adopted Current-I and D, the requested full assigned-pair old-depth identity is false; improving the boundary estimate alone cannot supply it. A completion must either carry and control the bulk defect in a revised window estimate, or specify a different extension, for example the old-projection-first construction (7.14), and prove its compatibility with the actual window filing and all its domains. For that construction the required quantitative collar/response and assigned-node comparisons are still open here. The general pointwise decoupled R9 bounds, the actual complex box comparison and the node comparison retain their prior conditional standing. The explicit counterexample avoids needing their general forms; it does not prove them. No rank-4 closure, retained-grade status, or Yang–Mills existence or mass-gap result follows.
