# CH: localized CMP 122b holomorphic bridge

Provenance: Research text in checkout 54a81c4f8c65053df89cb445101a6cf2ef1f1359, written for bridge lane CH. Source material from the Yang–Mills outline and complete account by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, is credited where used; their source revision is 31a47c543775. This document grants no audit or retained status. No computation discharges a proof obligation.

Author: Codex. This is an author proof attempt, not an independent check. Credit Tadeusz Bałaban for the underlying background and localization constructions. All local references below are relative to this `library/` at the checkout above. SA, I and II denote source lines of the pinned outline and complete accounts I and II.

## 1. Target and source checkpoint

The target is CH in `open-core.md` §4, exactly PH-L in `ph.md` §6. Its input does **not** include the complex per-link readings or the memberships sought. The term's original bounded analytic domain remains an input. The target uses the three localized CMP 122b maps, including their auxiliary fields and kept gauge. It does not permit replacement by the global carriers.

The two PH rounds were read, including (11)–(14), (19)–(20) and their failure conditions. They already prove conditional coefficient, contour and Boolean-endpoint estimates. None identifies different determining systems. This note does not promote those conditions to conclusions.

The source index was consulted before bounded SA reads: chunks 10 and 13 and `obligations.md`, for regular pairs, R9, walk tags and full-polydisc membership. Relevant source passages are SA 10129–10155, 10354–10403, 10552–10579, 15145–15174 and 15240–15250. They retain regular-pair admission and complex-core membership. The CA index's mechanical `PROVED` entry for `5.6:prop-polydisc-holomorphy` is not its source status: II:46167 says “Proof outstanding.”

The source files were fetched once as requested. The pre-existing `/tmp/sa_ca_II.tex` was reused after checking its hash against `open-core.md`'s pinned identity. SHA-256:

| Source | Hash |
|---|---|
| SA | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| II | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |

The repository workflow and physics-loop entry point were read from `git show HEAD:...`, since these paths are absent from the sparse worktree. The user's pinned, one-file research assignment controls the scope; no audit, dispatch, PR or ledger change is made.

## 2. Exact link dictionary and its limit

II:47976–48142 defines the following dictionary. These are identities of names and slots, not newly proved analytic identities.

| Link | Localized determining set | CMP representation / response | Input background → output |
|---|---|---|---|
| 4 | \(\mathbf B_k(Y_3)=\mathbf B(Y_3)\cup\mathbf B_k\) | (1.63), \(\mathbf H^{(4)}=H_k\) from (1.64) | \(U_k|_{Y_4}\to U_{k,\Lambda}|_{Y_3}\) |
| 3 | \(\mathbf B_1(Y_2)=\mathbf B(Y_2)\cup\mathbf B_1\) | (1.62), \(\mathbf H^{(3)}=H_B\) from (1.57) | \(U_{k,\Lambda}|_{Y_3}\to U''_{k,Z}|_{Y_2}\) |
| 2 | \(\mathbf B_k(Y_1)\) in II's definition | (1.61), \(\mathbf H^{(2)}\) from (1.51), (1.54), with \(u_k\) | \(U''_{k,Z}|_{Y_2}\to U_k^0|_{Y_1}\) |

The composition order is 4, 3, 2. The expansions are introduced in the reverse order. At each link, every component of \(Y_i'\) contains a component of \(\Lambda\) and meets \(Y_{i-1}\setminus Y_{i-1}^0\). The new domain is \(Y_i=Y_{i-1}\cup Y_i'\). The three variable sets are disjoint copies, even for the same spatial cube:
\[
 \mathcal V_i=\{\Delta:\Delta\cap\Lambda=\varnothing,\ \Delta\subset Y_i'\},
 \qquad P_i=P_{\mathcal V_i}(e^{\kappa_1}).
\]
All other switches of that link's decoupling family are zero (II:48143–48223). This does not set the independent switches of another link equal to them.

Link 3 substitutes its response into both argument and background slots (II:48464–48470). Link 2 retains \(u_k\), evaluated on the restriction of its response to each block (II:48472–48487). Real auxiliary variables remain fixed parameters; the other complex slots must be included (II:48331–48421).

Two distinctions prevent a silent identification. First, II:48405–48407 explicitly distinguishes this \(H_k\) from CMP 116 (1.17). Second, I:73545–73635 uses global determining sets for its carriers. Its alternative localized reading has \(\mathbf B''_k(Y_1^{\rm tr})\), whereas II's link-2 definition names \(\mathbf B_k(Y_1)\). This note does not erase those decorations or prove their equivalence. The account's global-chain proof does not supply the localized reading.

The required matching is thus an equality of actual response equations, currents, branches, boundary rows and coefficient tags on these determining sets. Merely identifying the three names in the table does not complete check (i).

### What (1.66)–(1.71) supplies

The account's quotations have different roles. They do not all define link functions.

* II:44896–44937 reads (1.66) as inductive decay, three factors \(e^{-(\kappa_1-1)M^{-d}|Y_i'|}\), and a spatial third factor. These are estimates on expansion pieces. Using them to prove the prior analytic domain would reverse the argument.
* I:71813–71885 proves the geometric part of (1.67),
  \(d_{k,Z}(Y_4)\le d_k(Y_0)+c_l\sum_{i=2}^4M^{-d}|Y_i'|\),
  without that display's third term. This counts localization domains; it is not a bound on a configuration or a current.
* I:95910–95951 quotes (1.68)–(1.69): the resummed \(V(Y,(\mathbf U,\mathbf J))\) has an analytic extension on its declared space, with exponential size outside the large-field components and an old-cell count inside one. These do not identify the unintegrated function at arbitrary independent complex switches. The latter count may depend on depth; CH permits the original term's bound and does not require replacing it by a depth-free amplitude.
* I:21145–21206 records the coupling-profile and vacuum assignments of (1.70). I:51730–51766 records the new determining set and the top-integrated operation (1.71), with all its expressions localized in the component. Neither passage defines a new switched auxiliary current or supplies its stage-domain bound.

The primitive tag rule that is actually spelled out is I:15265–15468. It expands current insertions into primitive walks before switching. Each primitive walk receives one factor for each distinct cell meeting its whole localization domain, including branches. Subsequent composites are formed from those switched primitives. In contrast, PW (8.1) first forms its Green coefficients and tags their whole hull once. Later products in DR retain multiplicities. These prescriptions must be compared at the precise primitive boundary; they cannot be interchanged.

## 3. First attack: compare the response germs, including the current

The proposed transfer is not established even by equality of the unswitched physical response. Here is an exact test at the first source derivative.

Use DR's equations (4)–(5) on its admitted envelope. Fix the pair and the switches. Write \(Q=K_0\), \(p=H^{\mathsf T}\mathbf J\), \(B_2[h,v]=\mathcal C''(0)[h,v]\), and \(\mathcal L=F''(0)\). Thus \(B_2\) is the bilinear second derivative, not the quadratic polynomial \(\mathcal C_2\) of DR. For a source direction \(S\), put \(v=H_1(s)S\). Then
\[
 D_Sh(0)S=v,
\tag{1}
\]
and the derivative of its specified current is
\[
 D_Sj(0)S=
 R'_0[v]Q^{\mathsf T}p
 +(I-Q^{\mathsf T}H^{\mathsf T})B_2[v,\cdot]^{\mathsf T}p
 +Q^{\mathsf T}H^{\mathsf T}\mathcal L v.
\tag{2}
\]
All transposes use DR's bilinear pairings. Equation (2) is a formula for this current, not for a physical current at arbitrary switches.

**Hand proof.** ROWS (31)–(38) gives \(d'(0)=0\), \(d''(0)=\mathcal C''(0)\), and \(DW_s(0)=0\). Differentiate DR (4). Its outer equation gives \(D_S\alpha(0)S=H_1S\); its inner equation then gives (1). The multiplier equation in DR (5) gives
\[
 D_h\lambda(0)[v]=H^{\mathsf T}\mathcal L v-H^{\mathsf T}B_2[v,\cdot]^{\mathsf T}p.
\]
Differentiate \(j=R_hK_h^{\mathsf T}\lambda-Q^{\mathsf T}p\), using \(R_0=I\) and \(D_hK_h(0)[v]=B_2[v,\cdot]\). Collecting its three product derivatives proves (2). For completeness, DR's integral defining \(E_h\) gives \(E'_0[v]=(i\eta/2)\operatorname{ad}_v\). The bilinear trace pairing gives \(\operatorname{ad}_v^{\mathsf T}=-\operatorname{ad}_v\), so \(R'_0[v]=(i\eta/2)\operatorname{ad}_v\), bond by bond. No switched inverse identity was used. \(\square\)

Thus an identification with a CMP link must match (1) and (2), after its actual raw-to-reduced source conversion, gauge changes and unit changes, including chain-rule terms for any moving background. ST1 (6)–(8) explicitly distinguishes the raw datum from the reduced datum. The first derivative must include that conversion. A bound for \(\mathcal L v\) alone does not establish (2), and \(QH(s)=I\) is unavailable.

For example, if two primitive coefficients \(A,B\) read the same cell, their separately tagged product has source derivative \(s^2AB\). A once-tagged composite has derivative \(sAB\). Their derivatives already differ at non-Boolean switches when \(AB\ne0\). This is the PH tag test applied to the tangent map; it does not refute either construction.

I also tried the account's own chart to avoid this comparison. Its actual formulas are I:14376–14451, and its switched construction is I:15265–15468. Its current is
\[
 \mathfrak J(B)=\Lambda^J(B)-\Delta'\mathcal H^J(B)
                   +F(U,\mathcal H^J(B)).
\]
The chart proposition proves this current's bound on its admitted class. It restricts representation and exactness identities to switches one. Its class requires real cube gauges, a first-order complex twist, and an independent current bound (I:12945–13026). Its definition explicitly excludes deriving the auxiliary tower clause from those conditions.

**Failure of attack 1.** Neither current formula has been identified with the actual \(J_{p,X}\) read after link 4. I obtained the necessary tangent test (1)–(2), not the missing identity or admission. Even an identity between the main response fields would leave this auxiliary current. The coefficient estimate PH (11) can pay repeated tags only after its common-background and coefficient hypotheses have been proved for this readout.

## 4. Second attack: retain the changed constraint rows

I tried to obtain the auxiliary minimizer by comparing the old and localized determining systems directly. The following finite-dimensional calculation identifies the missing datum and inverse. It applies in a fixed gauge slice; it makes no assertion that a particular pair of CMP determining sets is literally an augmentation.

Let \(A\) be real symmetric positive definite, and let \(Q_0\) have independent rows. Define
\[
 G=A^{-1},\quad W_0=Q_0GQ_0^{\mathsf T},\quad
 x_0=GQ_0^{\mathsf T}W_0^{-1}b_0,\qquad
 G_0=G-GQ_0^{\mathsf T}W_0^{-1}Q_0G.
\]
Add rows \(Q_\partial\), assuming \((Q_0,Q_\partial)\) has independent rows. Set
\[
 D=Q_\partial G_0Q_\partial^{\mathsf T},\quad
 r=b_\partial-Q_\partial x_0.
\]
Then the minimizer of \(\tfrac12x^{\mathsf T}Ax\), subject to \(Q_0x=b_0\) and \(Q_\partial x=b_\partial\), is
\[
 x=x_0+G_0Q_\partial^{\mathsf T}D^{-1}r.
\tag{3}
\]

**Hand proof.** In the inner product defined by \(A\), \(x_0\) is perpendicular to \(\ker Q_0\), and \(Q_0x_0=b_0\). Direct multiplication gives \(Q_0G_0=0\) and \(G_0AG_0=G_0\). Equivalently,
\(G_0=A^{-1/2}(I-P)A^{-1/2}\), where \(P\) is the orthogonal projection onto \(\operatorname{ran}(A^{-1/2}Q_0^{\mathsf T})\).
Thus \(D\) is positive definite: a vector in its kernel would give a linear dependence between the combined rows. Let \(y=G_0Q_\partial^{\mathsf T}D^{-1}r\). It has \(Q_0y=0\) and \(Q_\partial y=r\). For \(z\) in the kernel of both row sets, multiplication by \(AG_0\) gives \(\langle Ay,z\rangle=0\). Hence \(x_0+y\) is the unique constrained minimizer. \(\square\)

This shows precisely why uniqueness on each determining system does not identify their minimizers. On \(\mathbb R^2\), take \(A=I\), \(Q_0=(1,0)\), \(b_0=0\), \(Q_\partial=(0,1)\), and \(b_\partial=\epsilon\). The two unique minimizers are \((0,0)\) and \((0,\epsilon)\). Agreement on the common row is exact. The new residual is not zero.

It also shows why an energy gap alone does not provide the required uniform datum estimate. Replace \(Q_\partial\) by \((1,\epsilon)\), with \(0<\epsilon<1\). The common Hessian still has gap one, but \(D=\epsilon^2\). The raw residual \(r\) produces a second coordinate \(r/\epsilon\). This is a diagnostic for the inference, not a model of the actual lattice rows. The prescribed row geometry may rule it out; that must be proved on the actual localized set.

For the nonlinear problem let \(v\) be the auxiliary field coordinates, \(\lambda\) its multiplier, and \(z\) the incoming configuration. In a fixed local gauge chart write the actual critical system as
\[
 \mathcal F_e(v,\lambda;z)=
 \begin{pmatrix}
 \partial_v S_e(v,z)-D_vq_e(v,z)^{\mathsf T}\lambda\\
 q_e(v,z)-d_e(z)
 \end{pmatrix}=0.
\tag{4}
\]
Here \(e=(p,X)\) includes the complete determining and boundary data. Differentiating a solution gives exactly
\[
 \begin{pmatrix}
 S_{e,vv}-\sum_a\lambda_a q_{e,a,vv}&-D_vq_e^{\mathsf T}\\
 D_vq_e&0
 \end{pmatrix}
 \binom{\dot v}{\dot\lambda}
 =-\partial_z\mathcal F_e\,\dot z.
\tag{5}
\]
Both the multiplier contribution and the changed boundary datum remain. Deleting either changes the derivative problem.

At an already admitted solution, an invertible matrix in (5) gives a local holomorphic branch by a hand contraction argument. Put \(A_e=D_{(v,\lambda)}\mathcal F_e\) at that solution. On a sufficiently small ball, the derivative of
\(h\mapsto h-A_e^{-1}\mathcal F_e((v,\lambda)+h;z)\)
has norm at most \(1/2\), and its value at zero has norm at most half the ball radius. It maps the ball into itself. Picard differences form a geometric series. Their local Cauchy formulas pass to the uniform limit, proving holomorphy. The radius in this argument depends on the base solution until uniform estimates are supplied.

**Failure of attack 2.** PW and ROWS control their specified systems on an admitted regular envelope. They do not supply the raw residual, the constrained inverse, or a common regular starting chart for every auxiliary system obtained from \(\mathbf B_k(Y_3)\). Equation (3) isolates those missing comparisons even before the nonlinear problem. Equation (5) shows what has to be estimated for the auxiliary current. ST1 Lemma 11 expressly keeps the tower function and its determining set fixed; it cannot perform this change of constraints. This is a failure to prove the actual comparison, not a counterexample to its validity.

## 5. Third attack: construct a uniform tube and pay for its radius

I tried to turn the local branch from (5) into a common tube on the full switch polydisc. This separates two operations that cannot be combined without proof: constructing the auxiliary branch, and keeping each of its readings below its own threshold.

Here is a sufficient quantitative construction. It is a hand implication, not an assertion about the CMP maps. For one auxiliary system let \(x=(v,\lambda)\), fix an admitted reference \(x_e\), and assume \(A_e=D_x\mathcal F_e\) at that reference is invertible. Let \(D_e\) be an invertible linear scaling of the unknowns. Suppose the exact residual is single-valued, with fixed branches, and holomorphic on a neighbourhood of every point of
\[
 \{x_e+D_ey:\|y\|\le1\}\times P_4\times\{|z|<1\}
\]
at fixed external datum. The outer parameter is denoted \(z=t_\square\), and is omitted for ordinary pieces. Assume uniformly on this set
\[
 \|D_e^{-1}A_e^{-1}\mathcal F_e(x_e;\sigma,z)\|\le\varepsilon,
 \quad
 \|I-D_e^{-1}A_e^{-1}D_x\mathcal F_e(x_e+D_ey;\sigma,z)D_e\|
       \le\tfrac12.
\tag{6}
\]
For \(\varepsilon<1/4\), the map
\[
 T_{\sigma,z}(y)=y-D_e^{-1}A_e^{-1}
                       \mathcal F_e(x_e+D_ey;\sigma,z)
\]
has Lipschitz constant \(1/2\), sends the unit ball into its interior, and has a unique fixed point with \(\|y\|\le2\varepsilon\). The proof is the geometric-series argument of §4, now with uniform constants. It gives single-valued joint holomorphy on the whole parameter domain. Agreement with the prescribed local branch follows from uniqueness **if that branch solves this same residual system in this ball**. Equality at a physical endpoint alone is insufficient.

For a stage readout \(Q_e\), let \(r_e\) be its exact threshold in its own units. Suppress any explicit \((\sigma,z)\)-dependence in the following inequalities, which must hold uniformly at fixed parameter values. Suppose its reference obeys \(\|Q_e(x_e)\|\le r_e-\Delta_e\), with \(\Delta_e>0\), and
\[
 \|Q_e(x_e+D_ey)-Q_e(x_e)\|\le L_e\|y\|,
 \qquad 2L_e\varepsilon\le\tfrac12\Delta_e.
\tag{7}
\]
Then the fixed point obeys \(\|Q_e\|\le r_e-\Delta_e/2<r_e\). This is just the triangle inequality. The reference, residual, norm and \(\Delta_e\) must refer to the **same** determining system. Applying this to every required finite read and to the chart conditions constructs the needed tube. Gauge witnesses also have to exist on their full cubes; a bound on a readout cannot create a missing witness. Once those hypotheses hold uniformly, (6)–(7) give the positive outer radius one without compactness over histories.

The coupling arithmetic can indeed pay for a uniform estimate of this form. Keep the account's notation
\[
 T_j=\log g_j^{-2},\quad
 \delta_j=A_1g_jT_j^{p_0},\quad
 \alpha_{*,j}=C_*g_jT_j^q,\quad
 a=(1+d+d\beta_0^{\rm pr})r_{\rm pr},\quad
 s=q-p_0-a\ge1.
\]
These are II:1754–1812 and the quantities used in PH §4. Suppose, after the actual stage-room and level comparisons, a normalized residual or readout cost is bounded by
\[
 K e^{c\kappa_1} T_j^a\frac{\delta_j}{\alpha_{*,j}}
       (1+C_o|z|)
 =\frac{KA_1}{C_*}e^{c\kappa_1}T_j^{-s}(1+C_o|z|).
\tag{8}
\]
Here \(K>0\), \(c,C_o\ge0\) are fixed, independent of the history and all scale labels. For any chosen \(\epsilon_0>0\), take
\[
 T_*\ge\max\left\{1,2p_0,
 \left(\frac{2KA_1(1+C_o)e^{c\kappa_1}}{C_*\epsilon_0}\right)^{1/s}\right\},
 \qquad \gamma_*\le e^{-T_*/2}.
\tag{9}
\]
For every \(g_j\le\gamma_*\) and \(|z|<1\), (8) is at most \(\epsilon_0/2\). This follows by substitution and monotonicity of \(T^{-s}\). It is simultaneous for arbitrarily many indices. A minimum of finitely many such ceilings handles finitely many **types** of estimate. It does not take a minimum over histories or individual records.

The word *after* in (8) matters. If \(\Delta_e\) contains a factor \(2^{-n}\), division by it can leave \(2^n\). No fixed small positive \(g\) makes \(2^n(\log g^{-2})^{-s}\) small for all integers \(n\). PH (5)–(6) explains how suitable geometric separation can pay this loss. It has to hold for the full carrier of the actual auxiliary record. The existence of three links does not bound the age of those records.

For the actual stage spaces there are seven entries (I:49593–49625):
\[
 |\partial\mathbb U-I|,\quad |\partial U_{p,X}-I|,\quad
 |\mathbb J|,\quad |J_{p,X}|,\quad |\partial U-I|,\quad
 |A'|,\quad |\nabla_U^\eta A'|.
\tag{10}
\]
The powers of \(\mathsf L_0\) multiply all seven. Their coefficient, radius index, powers of spacing and complete stencil must be kept. The frozen field/current response controls its own first-order slots; it does not supply the second and fourth entries of (10). The current counterexample in PH (15)–(17) already rules out replacing that fourth entry by a first-order field bound.

I checked the closer candidate, II:13933–14006, the response-dilation corollary. Its hypothesis (h) separately assumes the auxiliary-field bump estimate for exactly entries two and four. Its hypotheses (a), (b), (f), and (g) also retain map holomorphy, layer estimates, absorption and entry-domain conditions. Thus its conclusion cannot supply (6)–(7) for the localized tower without the new estimate. I:34726–34743 likewise distinguishes a re-minimization from restriction; its discussion does not prove complex tower locality.

There is a simple test against extracting uniform outer room from openness. Let
\(f_n(z)=1-1/n+z\) for integers \(n\ge2\), with target \(\{|w|<1\}\). Each function is entire and its value at zero is in the target. The supremal radius of an open centred disc mapped into the target is \(1/n\): the triangle inequality proves inclusion for \(|z|<1/n\), while the real point \(z=1/n\) disproves any larger radius. The infimum is zero. This example tests only the inference from pointwise openness; it is not a Yang–Mills counterexample.

**Failure of attack 3.** I proved the uniform contraction and room implication (6)–(9). I did not establish its references, normalized residual bounds and auxiliary readout estimates for the actual localized systems. Neither ST1's already-admitted input nor CA's assumed bump estimate supplies them. In particular, a final decrease of the coupling pays a verified bound like (8); it cannot supply its missing numerator, positive margins or carrier separation. This attack leaves check (ii) unresolved already at the first auxiliary current, and therefore does not establish check (iii).

## 6. Constant order and the conditional composition

All successful conditional estimates above respect II:2791–2873 and 48615–48762: fix earlier geometry and analytic constants; then \(\kappa\), \(\kappa_1\), the permitted block-size floors, the argument radii, and finally the coupling ceiling. The floors include \(\delta_1M\ge\kappa_1\). Frozen PW/ROWS obtain their local input bounds on a fixed larger regular envelope; these are not chosen after seeing a history. The argument-radius choices of II:48615–48762 do not themselves prove membership. Equation (9) changes only the last ceiling.

No proof here identifies the different early constants and geometric hypotheses of PW's IN1 order with all the account's localized systems. This is an additional application check, not permission to change an already fixed decay rate. Once those checks are supplied, the numeric size losses of three links can be absorbed without an upper bound on \(\kappa_1\), depth, age or volume.

For clarity, the composition that would finish the task is recorded with its antecedent intact. Assume the missing check has been supplied for **all** the actual links, all stage and cube clauses, and the outer variable. Let \(\Omega_i\) be the reached open domains in CH. For a fixed datum, \(w_3(\sigma^{(4)})=\mathcal E_4(\sigma^{(4)};\mathfrak d)\) is holomorphic. Its graph
\[
 (\sigma^{(3)},\sigma^{(4)})\longmapsto
                 (\sigma^{(3)},w_3(\sigma^{(4)}))
\]
is holomorphic into \(\Omega_3\). Composition with \(\mathcal E_3\) gives \(w_2\). The same graph argument with \(\Omega_2\) gives the final map \(\mathsf R\). These statements are local at every reached tuple, so no common rectangular background domain is needed. Single-valuedness of each supplied link makes the resulting global function single-valued.

Since \(\mathsf R\in\mathcal A'_t\), the original bounded analytic term gives
\[
 F_t=t\circ\mathsf R\text{ holomorphic on }P_2\times P_3\times P_4,
 \qquad |F_t|\le\sup_{\mathcal A'_t}|t|\le\sup_{\mathcal A_t}|t|.
\tag{11}
\]
There is no replacement term or switch-radius loss. This is `open-core.md` §6.4's implication, also given in PH §6 and the account's link-composition argument.

For an outer piece with the supplied joint domain \(|z|<R(\mathfrak d)\) and original uniform term bound \(\mathfrak b_t\) throughout that domain, fix \(0<r<R(\mathfrak d)\). Then
\[
 \partial_z F_t(\sigma,0;\mathfrak d)
 =\frac1{2\pi i}\int_{|z|=r}\frac{F_t(\sigma,z;\mathfrak d)}{z^2}\,dz.
\]
The local Cauchy formulas in the switch variables pass through this fixed contour integral. The derivative is holomorphic and bounded by \(\mathfrak b_t/r\). Letting \(r\uparrow R(\mathfrak d)\) gives \(\mathfrak b_t/R_*\) when \(R_*:=\inf_{\mathfrak d}R(\mathfrak d)>0\). This is conditional composition, not a proof of CH.

## 7. Recovery and the next precise test

The first unresolved stage supply can be isolated more narrowly than PH-L. For each actual domain triple, let \(\mathscr T_3\) be the auxiliary labels \(e=(p,X)\), with every prescribed evaluation location and full stencil, tested in the stage domains needed at the input of link 3. These are the \(U_{p,X},J_{p,X}\) entries of (10), at their inherited radius indices. For each entry let \(r_{e,2}(x)\), \(r_{e,4}(x)\) denote its **entire printed right-hand side**, including its stage coefficient, \(\mathsf L_0\) power, coupling radius and units. This notation changes no threshold.

The next test is to write (4) for these actual determining sets and their raw data after link 4. Its derivative is (5). One must produce the admitted reference, the actual boundary residual, and bounds in the entry units. Equations (1)–(2) test a proposed DR identification; (3) prevents dropping newly imposed rows; (6)–(9) specify a sufficient continuation argument. Repeating the field estimate, the weight lemma, or abstract composition will not supply this test.

The frozen-text comparison used PW §§1, 7–9 and Result; ROWS §§1, 6–8 and its freeze qualifications; DR §§1, 3 and its freeze qualifications; ST1 §§1–2, Lemma 11, the source-budget and real-admission statements, and Theorem 14 with its proof. In ST1 the hypothesis named **CH** means a pivot-chart hypothesis. It is not this note's CH. ST1 Theorem 14 also explicitly assumes complex input membership. Neither occurrence proves the present target.

The wider literature record `lit-balaban.md` was searched and reused for this narrow lane. All primary-source uses here are bounded excerpts of SA, I and II. CMP 122b was used only through the account's quotations. No independent reading of that missing original paper is claimed. No new independent review was performed. Searches and hashes are bookkeeping; every displayed deduction above is a written hand argument.

## Result

**Open lemma**

**CH4-Aux (the first localized auxiliary-stage supply).** Under CH's admitted source-free inputs, without its excluded complex-membership hypotheses, there is one positive last coupling ceiling \(\gamma_4\) with the following property. For every admitted history, datum \(\mathfrak d\in\mathcal D_b\), and actual localization triple with all relevant running couplings at most \(\gamma_4\), the prescribed link-4 germ and every auxiliary minimizer/current readout \(e\in\mathscr T_3\) have compatible single-valued holomorphic continuations near every tuple reached for \(\sigma^{(4)}\in P_4\). The link uses exactly \(\mathbf B_k(Y_3)\) and the original primitive tags. Each auxiliary map uses its own prescribed determining system and the raw data induced by that link, retaining its branches and boundary conditions. With \(w_3=\mathcal E_4(\sigma^{(4)};\mathfrak d)\), they satisfy
\[
 |\partial U_{p,X}(w_3)(x)-I|<r_{e,2}(x),\qquad
 |J_{p,X}(w_3)(x)|<r_{e,4}(x)
\]
at every required location, with the continuation domains and cube gauges required to define those same auxiliary maps. The ceiling depends only on the earlier constants and \(b\), and is independent of history, depth, age and volume. The branches must agree with the prescribed germs wherever initially defined; no replacement response or reduced current is allowed.

This lemma is a necessary part of CH, not a sufficient replacement for it. It remains open here even with the outer parameter set to zero. Three attacks above fail at, respectively, the actual auxiliary-current identification, the changed-constraint residual and uniform inverse/admission, and the uniform all-read room estimate. Checks (i)–(iii) are therefore not complete. Later links, their remaining stage clauses, final membership and uniform outer room must still be supplied; (11) shows exactly what would then follow. No counterexample to CH was obtained, and no scientific status or T0 closure is claimed.
