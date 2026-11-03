# Removed-map comparison: symmetric agreement and native tails (row 131)
Provenance: OpenAI Codex, GPT-6 family (exact deployment identifier and effort setting not exposed; row 131 requests max); checkout `93daedf9188c2f8563462be67404383a144724fe`; Sussman–Alpoge `31a47c543775`, `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`. Research text, not an audit; no status is granted.

## 0. Scope and inputs

This repairs Section 3 of Claude's `o1-decoupled.md`, using the three corrections in `gates/o1-decoupled-gate.md` Section 3. It concerns rank 4 of `sa-ledger.md`: the removed response/current comparison required by WF7 and OA7. Theorem C below is an interior comparison with two separate exterior estimates; it is not the old globally transported operator inequality (3.1)–(3.2). Theorem D concerns the anchored specification (6.1) of Claude's `wf-room-2.md`, including its dependence on the independent current.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline's R9 response specification, box backgrounds, WF maps, OA7, and the proposed removed-field consumer. Credit Tadeusz Balaban for the local-inverse/walk comparison method and the separate treatment of box backgrounds and their data. Credit Claude for `o1-decoupled.md`, `h-walk.md`, and `wf-room-2.md`, and Codex for their gate corrections. All SA line references below refer to the one pinned download. No calculation or run supplies a mathematical premise.

The named analytic inputs retained here are:

* **W:** `h-walk.md` Theorem W(a),(b), field holomorphy and covariance, with the graph-norm and localization corrections of its gate Sections 5–6. Its false region-trace assertion is excluded. The underlying (I1) package must hold uniformly on the specified cut-downs. The coefficient is \(j=0\).
* **AB:** `o1-decoupled.md` Theorems A and B, Definition D and Lemma P, under their stated hypotheses, including the common parameter partition's geometric condition (P). Thus the walk bound and (O1) are available in **each system's own** spaces. This is an implication from those inputs, not a new proof of (I1).
* **Loc:** the fixed local coefficient discs for rows, the Wilson action remainder, and chart conversion used in `wf-room-2.md` Section 6 and `o1-decoupled.md` Lemma K. Section 5 below proves the comparison estimates from these local inputs, with the stronger response form of F1.
* **Pair, Field, Node:** the separately stated pair, field, and representative comparisons below. In particular, no complex version of SA 6\(c\), pointwise decoupled response theorem, or Landau representative comparison is assumed proved by (O1).

All statements are finite-volume statements with constants uniform in volume, mesh and depth under these inputs. Zero extension is used only to write finite sums, not to compare exterior norms or to identify constraint spaces.

## 1. Counterexamples before the repair

### 1.1 One-sided agreement does not match inner walks

Let the original sequence have local scale one throughout a sufficiently large neighbourhood, and let the second have local scale \(L^{-n}\) there. Use common nested grids and the flat pair \((1,0)\). Constant layers have no internal separation obstruction; put all nonempty boundaries farther away than the required gaps. Choose a cube \(G\) containing the fourth enlargement of a fine walk cube but no fourth enlargement of a scale-one walk cube. This is possible by taking \(L^n\) larger than their fixed enlargement ratio. The old union over **original** cubes is empty. Its (H-seq) therefore holds, but the second system has an inner zero-step walk and the first has none. This refutes the inference that the inner walk families coincide. It does not refute a propagator theorem with a genuinely common interior.

### 1.2 The two ball counts cannot be mixed

Let an exterior physical cube \(Q\), of fixed positive side, consist of bare pillars of side \(\eta\) in system 0 and scale-one pillars in system 1. Both systems can agree near a fixed row \(c\). Interpose successively separated layers outside that neighbourhood; their physical widths are bounded by a fixed multiple of

\[
 \rho\sum_{r=0}^{n}L^{-r}<\rho\frac L{L-1}.
\]

Choose the torus large enough once. In system 1 all points of \(Q\) then have distance at most a depth-independent constant \(D_0\) from \(c\). A fixed subcube of \(Q\) contains at least \(c_Q\eta^{-4}\) original pillars (take its side to be an integral multiple of \(\eta\)). Consequently

\[
 \sum_{y\in\mathcal B_0\cap Q}
 e^{-a\min(d_0(y,c),d_1(y,c))}
 \ge c_Q\eta^{-4}e^{-aD_0}.
\]

Neither native ball-count constant has this factor. The sum uses \(\mathcal B_0\); the second ball count uses \(\mathcal B_1\). Replacing one by the other is false. Likewise a gradient in system 1's exterior reference does not bound a gradient in system 0's unrelated exterior reference. The repair below never makes either replacement.

### 1.3 The actual old-level box need not agree with the step sequence

Here is a box sequence, not just an unspecified alternative localization. Work in level-\(k\) units, \(k>j\ge1\), with \(\xi_q=L^{q-k}\). On a sufficiently large torus put \(\Omega_q=\mathbb T\) for \(0\le q\le k\), and \(\Omega_{k+1}=\varnothing\). Choose a non-wrapping current window of side \(M\), let \(R_z\) be its fixed concentric enlargement, and place \(z\) in its central cell. All gaps of the ambient sequence are vacuous. Use the flat datum, zero independent current and identity representatives.

The current localized background uses the second-rule tower (SA 9783), whereas the old inner substitution of SA 9769 explicitly uses the **first** rule cut at \(j\). Keep these distinct. For the latter use exactly Definition A:
\[
 T_0=R_z,\qquad
 T_{q+1}=\bigcup\{Q:\ Q\text{ is an aligned }\mathfrak M\xi_{q+1}
 \text{-cube},\ d_\infty(Q,T_q^c)>\rho\xi_q\},\quad 0\le q<j,
 \tag{1.1}
\]
\[
 S^{\rm old\,box}=(T_0,\ldots,T_j,\varnothing,\ldots).
\]
For definiteness take \(\mathfrak M=M_1\) above W's size threshold, \(\rho=R_1M_1\) with the required \(R_1\), and then choose \(M\gg\rho+L^2M_1\) in the permitted hierarchy with common nested grids. This is the actual first-rule tower of the current box, cut at the old level, not an invented erosion. All flat pairs are regular at every positive ceiling. For the preliminary single-part localization, the second rule replaces the cell side by \(M_1'\xi_{q+1}\) and the gap by \(M_1'\xi_{q+1}\); its flat background is also 1. Either tower has the truncation obstruction below.

An induction shows that points deeper than
\[
 e_j=\sum_{q=0}^{j-1}(\rho\xi_q+\mathfrak M\xi_{q+1})
 \le\frac{\rho+L\mathfrak M}{L-1}\xi_j
 \le\rho\xi_j                                             \tag{1.2}
\]
belong to \(T_j\). Indeed, subtracting the side of the level-\((q+1)\) cell containing the point still leaves distance greater than the required gap from \(T_q^c\). Induct on \(q\). For the last inequality use \(L\ge3\), \(\rho\ge L\mathfrak M\). For the second rule the same argument instead gives \(e'_j\le3M_1'\xi_j\). Thus \(z\in T_j\), while its physical distance from \(R_z^c\) is at least \(cM\) for a fixed \(c>0\).

Nevertheless \(\Omega_{j+1}\) contains the entire window and \(S^{\rm old\,box}_{j+1}=\varnothing\). They disagree at \(z\) itself. Thus **no** region \(G\ni z\) satisfies memberwise agreement, let alone (H-seq-sym). In the box interior there are level-\(j\) rows of spacing \(\xi_j\); the original sequence has none there, since its definition excludes rows touching \(\Omega_{j+1}\). Its local rows have level \(k\). This is a mismatch of determining problems even though both zero-data backgrounds equal 1.

The geometric depth in old-level Euclidean units is at least \(cM/\sigma_j\), \(\sigma_j=\xi_j\); the distance to any genuine agreement region's complement at \(z\) is zero. Merely converting units cannot change that fact. The original native density is 1 in level-\(k\) units; expressed in level-\(j\) units it is \(\sigma_j\), so its native distance to the box boundary is still of order \(M\), not \(M/\sigma_j\).

For comparison with the pre-step depth-\((k+1)\) background rather than the depth-\(k\) response, set \(\Omega_{k+1}=\mathbb T\) as well and \(\Omega_{k+2}=\varnothing\). The same central mismatch holds; its top native scale in these units is simply \(L\).

This refutes applying the step-to-box lift comparison directly to the **old-level WF4 map**. It does not refute WF7, which states estimates for specified composite maps and treats them as hypotheses. A same-depth localization of the first response is a different comparison, proved conditionally in Section 7. One must not call the old-level inner map that same-depth response. The required nonlinear averages, and derivatives of their gauge representatives, cannot be deleted.

## 2. Published comparison and what is used from it

Balaban, *Propagators for Lattice Gauge Theories in a Background Field*, CMP **99** (1985), 389–434: pp. 408–410 construct local inverses on cut-down sequences before the walk expansion, (3.87)–(3.90). Page 412, (3.97), pays for changing the localization domain by the distance to the changed set. Pages 426–427, Theorem 3.14 and (3.154), compare two domain sequences at points in their common top region: walks localized there cancel, while a surviving walk visits the complement. The local copy read was `~/ym4d-papers/cmp99b.txt`, especially lines 1037–1145, 1267–1288 and 2080–2120. These are primary-source excerpts, not a theorem imported with its hypotheses omitted.

Balaban, *Renormalization Group Approach to Lattice Gauge Field Theories. I. Generation of Effective Actions in a Small Field Approximation and a Coupling Constant Renormalization in Four Dimensions*, CMP **109** (1987), 249–301: pp. 273–275, (3.18)–(3.23), construct the box tower, pass its nonlinear averaged datum to the box background, and remove exterior pieces using response decay. In particular the datum is changed along with the box problem. Pages 277–280, (3.38)–(3.52), treat restriction, endpoint and independent datum room separately. The local copy is `~/ym4d-papers/cmp109.txt`. CMP 116 is not present in the permitted paper directory; no result from it is used as a proved input here.

Most directly, CMP 109 p. 290, immediately after (4.35), compares \(H_j(\square_0)\) with the free-boundary \(H_j\) on \(X\times\operatorname{supp}\zeta_\square\), obtaining an exponential with length \(M/(L^j\eta)\). The index \(j\) is the same on both operators. Balaban then estimates the exterior part of the extended spatial sum separately. The local text at lines 2113–2126 makes this distinction explicit. Equations (4.4)–(4.12) and Lemma G below re-prove precisely this cancellation/tail mechanism for the stated inputs, and (7.4) recovers its old-scale length. It is not a citation for comparing \(H_k\) directly to \(H_j(\square_0)\).

Here is the portion of Balaban's mechanism needed below, re-proved without assuming identical exterior spaces. For a column at a common row, extend each native fine field by zero to the underlying lattice. For two absolutely convergent walk sums let \(I\) be a bijectively matched collection of walks with identical local formulas and monomials. Then, as an algebraic column identity, write

\[
 H_0-H_1=(H_{0,I}-H_{1,I})+H_{0,I^c}-H_{1,I^c}.
 \tag{2.1}
\]

This identity is first true for finite partial sums and then for the absolute limits. If the pairs agree on every matched read set, the first term is zero, term by term. Otherwise it is estimated by holomorphic variation on that read set. Every walk in the last two sums reaches a changed localization, but its bound, source normalization, energy norm and subsequent sum remain those of its own system. The distance estimate and all summations establishing the quantitative version of (2.1) are given in Section 4. Thus the citation supplies the method; the argument actually used is written here.

## 3. The corrected comparison hypotheses

Write \(i=0,1\) for the original and box systems. Each has its own sequence \(S_i\), regular complex pair \(P_i=(\mathbf U_i,\mathbf J_i)\), pillars \(\mathcal B_i\), local scale \(\xi_i\), metric \(d_i\), row set \(\mathcal C_i\), inner-plaquette action, and energy norm

\[
 \|A\|_{E_i,y}^2
 =\eta^4\sum_{b\ {\rm based\ in}\ y}
   (|\nabla_i A(b)|^2+\xi_i(b)^{-2}|A(b)|^2).
 \tag{3.1}
\]

Using the full complex connection in the gradient gives an equivalent norm on the admitted pair class: changing a link by \(e^{i\eta A'}\) changes a divided transport by at most \(C|A'|\le C\alpha_1\xi_i^{-1}\). This follows by integrating the derivative of the matrix exponential, and is absorbed by the mass term in (3.1). We use this equivalence when transporting a norm on the common interior. No such transport is made outside it.

Both systems satisfy **AB** with the same fixed thresholds and walk cube size \(M_1\). Their actual gap parameters must satisfy W; being called a tower is not a replacement for this hypothesis. They use the same nested grids, orientations, contours, node conventions, row-length normalization, boundary convention, cutoff profiles, deterministic cut-down rule, parameter cubes and parameters. All differing actions are the inner-plaquette actions of their respective first members. A different interior action would be an additional source, not a geometric comparison.

Extend each metric density by the bare density outside its first member, as in W. This defines distances to complements on a common underlying torus, without defining any exterior field norm in the other system.

**(H-seq-sym).** For a specified physical region \(G\) with nonempty complement, the two sequences agree member by member on

\[
 E_G=G\ \cup\!
 \bigcup_{\substack{\kappa\in K_0\cup K_1\\
                         \kappa^{(4)}\subset G}}
                 \kappa^\sharp,
 \qquad
 \kappa^\sharp:
 \text{concentric side }8L^2M_1\xi_\kappa.
 \tag{3.2}
\]

Absent members above a sequence's depth mean the empty set. In particular (3.2) includes equality of depths wherever a higher member of either sequence is nonempty. Impose the separation/enlargement hypotheses of C1, including \(R_1\ge8L^3\). The union is over **both** native cube families, whether or not a cube has yet been matched.

On \(G\) the metric densities are identical. Define

\[
 D(x)=d_0(x,G^c)=d_1(x,G^c)\quad(x\in G),
 \qquad D=0\quad\hbox{on }G^c.                 \tag{3.3}
\]

To prove the equality, truncate any path at its first exit from \(G\). Its length before that exit uses the common density. Taking infima over these initial paths proves (3.3). This does **not** identify distances between two interior points: a minimizing path between them can leave \(G\). The function \(D\), extended by zero, is 1-Lipschitz in each native metric. Indeed the distance to a fixed set is 1-Lipschitz by concatenating paths; the same statement across its boundary follows by first exit. For a pillar \(D_y\) is its infimum; at a row \(D_c\) is evaluated at the chosen base point. Replacing a base point by its source support changes these distances by at most the fixed carrier radius, which is included in all margins below.

**(H-pair).** Only on \(G\), identify the pairs in the prescribed common gauge:

\[
 (\mathbf U_1)^{g^{-1}}=e^{i\eta X}\mathbf U_0,
 \qquad (\mathbf J_1)^{g^{-1}}=\mathbf J_0+\delta\mathbf J,
\]
\[
 x(x):=\xi|X|+\xi^2|\nabla_0X|+\xi^3|\delta\mathbf J|
       \le\varepsilon_P e^{-\theta_PD(x)},
 \quad \varepsilon_P\le c_P a_{\min},
 \quad a_{\min}=\min(\alpha_0,\alpha_1,\gamma_0)>0.
 \tag{3.4}
\]

The first pair has half-ceiling room on these local read sets. The constant \(c_P\) is chosen below the fixed BCH/local-class threshold, as in C1's accepted analytic repair. Both \(g\) and \(g^{-1}\) have a fixed condition-number bound. The comparison is assumed on the entire parameter domain consumed, including independent currents; a real-slice assertion is insufficient. Gauge identification is used on \(G\) only. Exterior column estimates are in system 1's original gauge, with its source at the common row transformed by (g(c)). Covariance and the bounded adjoint at that row cost a fixed constant, not an extension of \(g\) to the exterior.

Fix a finite native carrier radius \(r_0=C_L\) containing a pillar, a row carrier, its adjacent plaquettes, and the stencils used by Loc. It can be enlarged a fixed number of times below. Let \(\mathcal I\) be the common pillars whose required stencil enlargements lie in \(G\), and let \(\mathcal C\) be the common rows whose required carriers lie in \(G\). A pillar or row discarded inside \(G\) has \(D\le r_0\), after increasing \(r_0\). A native source produced by a discarded row has \(D\le2r_0\). These assertions follow by joining a point in the carrier to its first point outside \(G\); the carrier diameter is bounded by \(r_0\). Common pillars form a subset of each native partition. Partial boundary pillars go to the respective native tails, never to a newly invented common partition.

**Lemma C1-sym.** The collections of walks all of whose \(\kappa^{(4)}\) lie in \(G\) coincide, with identical local formulas and decoupling monomials.

*Proof.* Take a cube from either family with fourth enlargement in \(G\). Its membership test reads the regions on the cube. A competing cube contributing to its cutoff denominator can have only scale \(\xi_\kappa/L,\xi_\kappa,L\xi_\kappa\): separation excludes more distant scales, using the excluded candidate's own cutoff reach for a coarser candidate. The entire membership tests of the remaining candidates, including an absent candidate, lie in \(\kappa^\sharp\). Equality there makes both denominators identical. The cut-downs and local matrices read \(\kappa^{(4)}\), and the commutator stencils lie within \(\kappa^{(5/2)}\); their rules are common. This is precisely C1, applied first with 0 as original and then with 1 as original. Thus the injections are inverse identifications of cubes, cutoffs and admissible transitions. The same finite cube list is a walk in both systems. Its enlarged physical hull meets exactly the same parameter cubes, so Definition D gives the same monomial. The local inverse functions are identical; they are evaluated at the two local pairs. This proves a bijection, not just one injection. \(\square\)

## 4. Theorem C: interior difference and two native tails

Choose

\[
 \beta=\tau_L/4,\qquad
 \theta=\min(\theta_P/2,\tau_L/32),\qquad a=\tau_L/16.
 \tag{4.1}
\]

The smaller rate leaves room for collars and subsequent weighted sums. Let \(r_*=C_LM_1+4r_0\) bound the native diameter of a fourth enlargement and its endpoint supports. The two-/three-layer bounds in Definition D supply this in either system. Constants below may depend on the fixed gauge condition bound. Set

\[
 B_s=C_LB_Le^{16\bar\kappa},\qquad
 A_*=C_LB_s e^{\tau_Lr_*}(1+\varepsilon_P/a_{\min}),
\]
\[
 C_{\rm cmp}=C_L A_*\bigl(K_{0,a}+K_{1,a}\bigr),\qquad
 C_H=\max(C_{H,0},C_{H,1},1).
 \tag{4.2}
\]

Here \(K_{i,a}=\sup_c\sum_{y\in\mathcal B_i}e^{-a d_i(y,c)}\). AB's ball count makes these finite uniformly, since \(a\rho'\ge16\log L\) follows from \(\tau_L\rho'\ge256\log L\). Increasing \(C_L\) absorbs the fixed support shifts. No \(K_{1,a}\) is ever used to sum over \(\mathcal B_0\).

**Theorem C.** Assume (3.2)–(3.4), common specifications, W and AB. Write

\[
 H_i=H_{i,\mathrm{in}}+H_{i,\mathrm{out}},\qquad
 L_i=D_{\mathbf U_i}H_i,
 \tag{4.3}
\]

where “in” means every fourth enlargement is in \(G\). At common interior endpoints (y,c), after the stated gauge identification,

\[
 \|(H_{0,\mathrm{in}}-H_{1,\mathrm{in}})(\cdot,c)\|_{E_0,y}
 \le C_LB_s e^{\tau_Lr_*}{\varepsilon_P\over a_{\min}}
 e^{-\theta(D_y+D_c)}e^{-a d_0(y,c)},                 \tag{4.4}
\]
\[
 \|H_{i,\mathrm{out}}(\cdot,c)\|_{E_i,y}
 \le C_LB_s e^{\tau_Lr_*}
 e^{-\theta(D_y+D_c)}e^{-a d_i(y,c)},\quad i=0,1.
 \tag{4.5}
\]

Equation (4.4) is asserted only at common interior pillars. Equation (4.5) also holds at any native pillar \(y\in\mathcal B_i\), with \(D_y=0\) when it meets \(G^c\). Its two norms stay native. At a common interior pillar they can be compared at a fixed cost using (3.4): the difference of divided covariant transports is \(O(|X|)\), controlled by the mass part of (3.1). At exterior pillars only the appropriate native estimate is asserted. The same conclusions, in local \(L^2\), hold for \(L_{0,\mathrm{in}}-L_{1,\mathrm{in}}\) and \(L_{i,\mathrm{out}}\). The first of these is the difference of the **whole** curls in (4.3).

For sources define their own norms

\[
 \|f_i\|_{F_i}=\sup_b\xi_i(b)^3|f_i(b)|,
 \qquad \|q_i\|_{Q_i}=\sup_p\xi_i(p)^2|q_i(p)|.
\]

On the common interior define \(\|\delta f\|_{F,w}=\sup w\xi^3|f_0-f_1|\), \(\|\delta q\|_{Q,w}=\sup w\xi^2|q_0-q_1|\), with \(w=e^{\theta D}\). Sources may be unrelated in the two exteriors. On common rows, with \(\|v\|_{Y,w}=\sup_{c\in\mathcal C}w(c)|v(c)|\),

\[
 \|H_0^{\mathsf T}f_0-H_1^{\mathsf T}f_1\|_{Y,w}
 \le C_{\rm cmp}(\|f_0\|_{F_0}+\|f_1\|_{F_1})
       +C_LC_H\|\delta f\|_{F,w},                   \tag{4.6}
\]
\[
 \|L_0^{\mathsf T}q_0-L_1^{\mathsf T}q_1\|_{Y,w}
 \le C_{\rm cmp}(\|q_0\|_{Q_0}+\|q_1\|_{Q_1})
       +C_LC_H\|\delta q\|_{Q,w}.                   \tag{4.7}
\]

All transposes use the physical fine pairing and the fixed counting convention for raw rows. Each source is paired only where its own action or field is defined. Boundary strips omitted from the common interior are included in the native terms. These are the replacements for the unrestricted old (3.2).

*Proof of the walk estimates.* For a raw row column, the source in the unfolded \(\nu\)-slot has norm \(\xi_c\). The definition \(H=\mathsf H\mathsf m^{-1}\) divides by exactly \(\xi_c\). W and Lemma P therefore give, for a walk of \(n\) transitions in system \(i\),

\[
 \|s^\omega[T_\omega]_{A\nu}\mathsf m^{-1}(\cdot,c)\|_{E_i,y}
 \le B_s(C_W/M_1)^n e^{-\beta\ell_i(\omega;y,c)}.
 \tag{4.8}
\]

At most \(N_L\nu_1^n\) terms have a given output pillar, and \(\nu_1C_W/M_1\le1/2\). Their sum is bounded by the geometric series \(\sum_{n\ge0}2^{-n}=2\). The factor \(e^{16\bar\kappa}\) has already paid for the initial parameter cubes; the remaining parameter count used at most half the exponent of W. This explains every summation constant in (4.8).

For an inner walk let \(\delta_\omega=\inf_{[[\omega]]}D\), and \(S=D_y+D_c\). A path visiting its required cells comes within \(r_*\) of a point attaining this infimum; the root cell is covered by the endpoint allowance. The 1-Lipschitz property of \(D\) gives

\[
 \ell_0\ge d_0(y,c),\qquad
 \ell_0\ge S-2\delta_\omega-2r_*.
 \tag{4.9}
\]

The local path of pairs is \(P(t)=(e^{i\eta tX}\mathbf U_0,\mathbf J_0+t\delta\mathbf J)\). Its local complex disc has radius

\[
 R_\omega=c\,a_{\min}/\varepsilon_\omega,\qquad
 \varepsilon_\omega=\sup_{[[\omega]]}x
 \le\varepsilon_Pe^{-\theta_P\delta_\omega}.
\]

Choose \(c_P\le c/4\), so \(R_\omega\ge4\). BCH and its first divided difference bound the complex potential by its half ceiling plus \(C|t|\varepsilon_\omega\). The plaquette product expansion bounds its normalized curvature increment by \(C(|t|\varepsilon_\omega+|t|^2\varepsilon_\omega^2)\); the current increment is linear. Decreasing \(c\), then \(c_P\), leaves all ceilings free. The real reference and its gauge clauses stay fixed. C4 and W apply locally; no extension of this disc to an exterior pair is required. The local energy norms along this disc are uniformly equivalent to the fixed real-reference energy norm, by the mass-term argument after (3.1), so Cauchy's inequality is taken in a fixed normed space. If \(\varepsilon_\omega=0\), the difference is zero. Otherwise the Cauchy derivative bound on circles about \(t\in[0,1]\) of radius at least \(R_\omega/2\), followed by integration, gives the extra factor \(C\varepsilon_\omega/a_{\min}\) in (4.8).

Allocate half of \(\beta\ell_0\) to \(d_0(y,c)\). The other half together with \(\theta_P\delta_\omega\) supplies \(\theta S-\beta r_*\). To check this without assuming a sign, if \(\delta_\omega\ge S/2\), its pair factor alone gives \(\theta_PS/2\). If \(\delta_\omega<S/2\), use (4.9) and

\[
 \theta_P\delta_\omega+(\beta/2)(S-2\delta_\omega)
 \ge\min(\theta_P/2,\beta/2)S.
\]

Taking the nonnegative path length when the right side of (4.9) is negative gives the same estimate with the displayed \(\beta r_*\) loss. Since \(a\le\beta/2\) and \(\theta\le\min(\theta_P/2,\beta/2)\), the geometric walk sum proves (4.4).

For an outer walk some fourth enlargement meets \(G^c\). The visiting path comes within \(r_*\) of that complement. If this is the root, \(D_y\le r_*\), and \(\ell_i\ge|D_c-D_y|\ge S-2r_*\); otherwise the two pieces through the visited cell give the same inequality. Thus

\[
 \ell_i\ge d_i(y,c),\qquad \ell_i\ge S-2r_*.
\]

Allocate half of \(\beta\ell_i\) to each inequality and sum (4.8) in system \(i\). This proves (4.5) with its own metric and norm. For the curl, its local \(L^2\) norm is bounded by the energy on a fixed neighbouring set of pillars. The analytic argument can equivalently be applied to the holomorphic local expression \(D_{\mathbf U(t)}T_\omega(P(t))\). Its stencil is in the same fourth enlargement; fixed neighbouring-pillar shifts are already in \(r_*\). This proves the whole-curl version with no missing base-curl term.

*Proof of the source estimates.* The pillar calculation, in each system separately, is

\[
 \eta^4\sum_{b\in y}\xi_i^{-3}|A(b)|
 \le\Big(\eta^4\sum_{b\in y}\xi_i^{-4}\Big)^{1/2}
     \Big(\eta^4\sum_{b\in y}\xi_i^{-2}|A(b)|^2\Big)^{1/2}
 \le C_L\|A\|_{E_i,y}.                             \tag{4.10}
\]

There are at most \(4(\xi_y/\eta)^4\) bonds, with adjacent scales comparable by \(L\); this proves the last bound directly. For \(D_iA\), use the same calculation with \(\xi_i^{-2}\), the physical volume of the pillar, and the gradient component of \(E_i\); neighbouring supports cost a fixed constant.

Split the physical sums into common full pillars \(\mathcal I\) and each native remainder. On \(\mathcal I\), telescope the integrand as

\[
 (H_0-H_1)^{\mathsf T}f_0+H_1^{\mathsf T}(f_0-f_1).
 \tag{4.11}
\]

Use (4.4) and the two (4.5)'s for the first term. After multiplying by \(e^{\theta D_c}\), (4.10) leaves sums of \(e^{-a d_0(y,c)}\) and \(e^{-a d_1(y,c)}\) **only over common pillars**. This set embeds in both native partitions, so these sums are at most \(K_{0,a}\) and \(K_{1,a}\), respectively. The second term is (O1) with the weight \(e^{\theta D}\), which is admissible in system 1 by (3.3).

For the native remainder of system \(i\), \(D_y\le2r_0\), including the fixed stencil margin. First exit gives \(d_i(y,c)\ge D_c-2r_0-C_L\). The full native column estimate of AB has exponent \(\beta d_i\). Hence

\[
 e^{\theta D_c}e^{-\beta d_i(y,c)}
 \le e^{\theta(2r_0+C_L)}e^{-(\beta-\theta)d_i(y,c)}.
 \tag{4.12}
\]

Equations (4.10), (4.12) and **that system's** ball count bound the remainder by \(C_LC_H\|f_i\|_{F_i}\). There is no common force measured with the wrong exterior scale. This proves (4.6). Repeating (4.11) for \(L_i,q_i\) and using its curl version proves (4.7). Both arguments apply to scalar pairings with arbitrary unit colour vectors, hence to the stated vector norms. \(\square\)

## 5. Theorem D: anchored currents, including the node factor

Write \(A_i\) for the first-system **response field**, reserving \(H_i\) for its linear lift. Put
\[
 h_i=\|A_i\|_{X_i},\quad h=h_0+h_1,\qquad
 \|A\|_{X_i}=\sup_b\max(\xi_i|A|,\xi_i^2|\nabla_iA|).
\]
Use native norms globally and the common chart only on \(G\). Add:

* **(H-field)** \(\varepsilon_H=\|A_0-A_1\|_{X,w;G}<\infty\), with the derivative in the common reference. Proportionality to the fluctuation amplitude remains a separate response input.
* **Small response ball:** \(h_i\le r\le1/2\), \(C_LC_Hr\le1/4\), for the localized row product constant below. Local coefficient ceilings, including \(\alpha_0\), are at most 1. This does **not** impose \(C_H\alpha_0=O(1)\).
* **(H-node), only for assigned representatives:** \(|g(x)-1|\le\varepsilon_Ne^{-\theta_PD(x)}\). Bounded condition number alone does not imply this.

### 5.1 Local estimates, with the response factor retained

At a common stencil put
\[
 e_b=\sup_{N(b)}\max(\xi|A_0-A_1|,\xi^2|\nabla(A_0-A_1)|),
 \quad x_b=\sup_{N(b)}x,\quad r_b=\max_i\|A_i\|_{X_i;N(b)}.
\]
Set \(Z_i=K_{i,A_i}-K_{i,0}\), \(R_i=R_{A_i}\), \(D_i=D_{\mathbf U_i}\). For a common row vector \(v\), the local comparisons are
\[
 \begin{aligned}
 \xi^3|(K_{0,A_0}^{\mathsf T}-K_{1,A_1}^{\mathsf T})v|
   &\le C_L(e_b+x_b)\sup_{N(b)}|v|,\\
 \xi^3|(Z_0^{\mathsf T}-Z_1^{\mathsf T})v|
   &\le C_L(e_b+r_bx_b)\sup_{N(b)}|v|,\\
 |R_0-R_1|&\le C_L\eta|A_0-A_1|,\\
 \xi^2|\mathcal F_0-\mathcal F_1|&\le C_Lx_b,\\
 \xi^2|(D_0-D_1)A_1|&\le C_Lx_br_b,\\
 \xi^3|\mathcal N_0(A_0)-\mathcal N_1(A_1)|
   &\le C_L(\alpha_0+r_b)e_b+C_L(r_b+r_b^2)x_b.
 \end{aligned}                                                   \tag{5.1}
\]
The last line is **F1 in response form**, with \(r_b\) an actual local field size. Replacing it by a fixed ball radius would conceal the vanishing at zero response. Here
\(\mathcal N_i(A)=\Delta'_{\mathbf U_i}A+N_{\mathbf U_i}(A)\).
The native bounds are
\[
 \|Z_i^{\mathsf T}v\|_{F_i}\le C_Lh_i\|v\|_Y,\quad
 |R_i-I|\le C_L\eta|A_i|,\quad
 \|\mathcal N_i(A_i)\|_{F_i}\le C_L(\alpha_0+h_i)h_i.       \tag{5.2}
\]

*Proof.* Loc bounds normalized holomorphic row coefficients on a fixed enlarged disc. Integrating their derivatives on a smaller coordinate ball bounds an increment by its coordinate distance. The BCH base change costs \(C_Lx_b\). The transpose row density is \(\eta^4\xi_c^{-3}\), and bounded carrier overlap gives the first line. Since \(K_A-K_0=0\) at \(A=0\) for every base,
\[
 \partial_P(K_A-K_0)
   =\int_0^1\partial_P\partial_AK_{tA}[A]\,dt.
\]
The fixed second-derivative bound gives the response factor in the second line. A weight can be put on either the local field or the multiplier, since its ratio on a stencil is at most \(e^{\theta r_0}\).

The exponential-series differential \(E_A\) is invertible on the chart ball. Differentiating \(R_A=(E_A^{\mathsf T})^{-1}\) gives \(|dR_A|\le C_L\eta|dA|\), and integrating from zero gives (5.2). Expanding a plaquette's four perturbed links gives the covariant curl of \(X\) plus quadratic field and curvature-times-field terms. Their normalized sizes are bounded by \(C_L(x_b+x_b^2)\le2C_Lx_b\), proving the plaquette line. Also
\[
 \eta^{-1}(\operatorname{Ad}e^{i\eta X}-I)
 =\int_0^1\operatorname{Ad}e^{it\eta X}\,i\operatorname{ad}X\,dt
\]
proves the curl line.

For F1, Loc bounds the field derivatives of \(\Delta'_PA\) and \(N_P(A)\) by \(C_L\alpha_0\) and \(C_Lr_b\), respectively. The base derivative of the first retains its factor \(A\). For the second, \(N_P(0)=D_AN_P(0)=0\), so
\[
 N_P(A)=\int_0^1(1-t)D_A^2N_P(tA)[A,A]\,dt.
\]
Differentiate in the base on the fixed larger coefficient disc and apply Cauchy's derivative bound. This retains two factors of \(A\). Integrating first in the field, then in the base, proves F1 with \(C_L(\alpha_0+r_b)e_b+C_L(r_b+r_b^2)x_b\). These are local coordinate discs, not a presumed common segment between different boundary problems. \(\square\)

### 5.2 Individual multipliers and the anchor convention

For each system use specification (6.1):
\[
 T_i=Z_iH_i,\quad
 (I+T_i^{\mathsf T})\lambda_i=H_i^{\mathsf T}F_i'(A_i),\quad
 \lambda_{0i}=H_i^{\mathsf T}F_i'(0),\quad
 j_i=R_iK_{i,A_i}^{\mathsf T}\lambda_i-K_{i,0}^{\mathsf T}\lambda_{0i}.
 \tag{5.3}
\]
The first subscript in \(\lambda_{0i}\) means anchor. Pairing the Wilson first variation plaquette by plaquette gives
\[
 F_i'(0)=D_i^{\mathsf T}\mathcal F_i,\qquad
 \lambda_{0i}=L_i^{\mathsf T}\mathcal F_i,\qquad
 \|\mathcal F_i\|_{Q_i}\le C_L\alpha_0.                     \tag{5.4}
\]
To verify the identity, differentiate the four-link product, move the other factors cyclically in the trace, and collect the four transported potential values into \(D_iA\). The physical normalization leaves the traceless plaquette field, of size \(C\eta^{-2}|\partial\mathbf U_i-1|\). This algebraic identity in links and inverses also holds at complex links. Missing plaquettes simply do not occur. No force-norm bound on the full \(J(\mathbf U_i)\) is used.

On common plaquettes the **exact** anchor subtraction is
\[
 (L_0-L_1)^{\mathsf T}\mathcal F_0
       +L_1^{\mathsf T}(\mathcal F_0-\mathcal F_1).           \tag{5.5}
\]
Add the two native exterior integrals. There is no extra
\(((D_0-D_1)H_1)^{\mathsf T}\mathcal F_0\): it is already in \(L_0-L_1\).
Equations (4.7), (5.1), (5.4) give
\[
 B_{\rm anc}:=\|\lambda_{00}-\lambda_{01}\|_{Y,w}
 \le C_L(C_{\rm cmp}\alpha_0+C_H\varepsilon_P),\qquad
 \|\lambda_{0i}\|_Y\le C_LC_H\alpha_0.                       \tag{5.6}
\]
This includes both action changes, using native scales on boundary plaquettes.

Put \(\mu_i=\lambda_i-\lambda_{0i}\). Subtract within each system:
\[
 (I+T_i^{\mathsf T})\mu_i
 =L_i^{\mathsf T}D_iA_i+H_i^{\mathsf T}\mathcal N_i(A_i)
                -T_i^{\mathsf T}\lambda_{0i}.               \tag{5.7}
\]
The local product bound followed by native (O1) yields
\[
 \|T_i^{\mathsf T}v\|_{Y,w_i}\le C_LC_Hh_i\|v\|_{Y,w_i},
 \qquad w_i=e^{\theta d_i(\cdot,G^c)}.                       \tag{5.8}
\]
There is also the version with the weight on the field. The norm is at most \(1/4\); the Neumann inverse has norm at most \(\sum_{n\ge0}4^{-n}=4/3\). Estimate the curl term through \(L_i\), the lower-order term through \(H_i\), and the anchor product through (5.8). This gives
\[
 \|\mu_i\|_Y+\|j_i\|_{F_i}
 \le C_LC_H(1+C_H\alpha_0)h_i=:M_Hh_i.                       \tag{5.9}
\]
For the current use the exact anchored expansion
\[
 j_i=R_iK_{i,A_i}^{\mathsf T}\mu_i
    +R_iZ_i^{\mathsf T}\lambda_{0i}
    +(R_i-I)K_{i,0}^{\mathsf T}\lambda_{0i}.                 \tag{5.10}
\]
Its estimate follows from the local row bound and (5.2). In particular, small \(C_Hr\) does not remove \(1+C_H\alpha_0\).

### 5.3 Subtraction on common rows

Let \(P_i\) restrict native rows to \(\mathcal C\), and \(E_i\) extend common rows by zero. Define
\[
 A_{1,G}=P_1T_1^{\mathsf T}E_1,\qquad
 \|A_{1,G}\|_{Y,w\to Y,w}\le1/4.                            \tag{5.11}
\]
Restriction and extension have norm one, so (5.8) proves this without identifying the two full row spaces.

For native vectors \(v_i\), let \(V=\max(\|v_0\|_Y,\|v_1\|_Y)\). Form \(\widetilde v_1\) by copying \(P_0v_0\) onto the common rows and retaining \(v_1\) on system 1's other rows. Thus \(\|\widetilde v_1\|_Y\le V\). Exactly,
\[
 P_0T_0^{\mathsf T}v_0-P_1T_1^{\mathsf T}v_1
 =A_{1,G}(P_0v_0-P_1v_1)+\mathcal R(v_0,v_1).              \tag{5.12}
\]
The remainder compares \(H_0^{\mathsf T}Z_0^{\mathsf T}v_0\) with
\(H_1^{\mathsf T}Z_1^{\mathsf T}\widetilde v_1\).
On common stencils the read row values match, so (5.1) bounds the force difference by
\(C_L(e_b+r_bx_b)V\xi^{-3}\). Native force norms are at most \(C_Lh_iV\).
A stencil reading an excluded row lies in \(D\le2r_0\); keep it in its native tail.
Theorem C, with this fixed enlarged boundary strip, therefore gives
\[
 \|\mathcal R(v_0,v_1)\|_{Y,w}\le Z_*V,\qquad
 Z_*=C_L\{(C_{\rm cmp}+C_H\varepsilon_P)h+C_H\varepsilon_H\}.
 \tag{5.13}
\]
Increasing the fixed constant in (4.2) pays for the strip enlargement. No exterior row has been measured in the other system's norm.

Let \(\mathcal B_i^{\rm rsp}=L_i^{\mathsf T}D_iA_i+H_i^{\mathsf T}\mathcal N_i(A_i)\).
Equations (4.6)–(4.7) and (5.1) give
\[
 \|P_0\mathcal B_0^{\rm rsp}-P_1\mathcal B_1^{\rm rsp}\|_{Y,w}
 \le Z_*                                                     \tag{5.14}
\]
with a fixed increase of its constant. Indeed the native curl sources have norm \(C_Lh_i\), and their common difference has weighted norm \(C_L(\varepsilon_H+\varepsilon_Ph)\). The native lower-order sources have norm \(C_L(\alpha_0+h_i)h_i\); their common difference has norm
\(C_L[(\alpha_0+r)\varepsilon_H+(h+h^2)\varepsilon_P]\).
Since \(\alpha_0\le1\), \(h\le1\), these are exactly the terms allowed in (5.13). There is no base-only error at zero response.

Subtract (5.7), applying (5.12) first to \(\mu_i\), then to \(\lambda_{0i}\).
With \(\delta\mu=P_0\mu_0-P_1\mu_1\), this gives
\[
 (I+A_{1,G})\delta\mu
 =\delta\mathcal B^{\rm rsp}-A_{1,G}\delta\lambda_0
   -\mathcal R(\lambda_{00},\lambda_{01})
   -\mathcal R(\mu_0,\mu_1).                                \tag{5.15}
\]
Consequently
\[
 \|\delta\mu\|_{Y,w}\le\frac43\left[
 Z_*\{1+C_LC_H\alpha_0+M_H\max(h_0,h_1)\}
       +C_LC_Hh_1B_{\rm anc}\right].                         \tag{5.16}
\]
This uses (5.6), (5.9), (5.11)–(5.14). Each term contains \(h\) or \(\varepsilon_H\). The two anchors and the two row complements are all retained.

### 5.4 The current and the assigned representatives

On a common stencil the first term of (5.10) subtracts as
\[
 R_0K_{0,A_0}^{\mathsf T}\delta\mu
 +(R_0K_{0,A_0}^{\mathsf T}-R_1K_{1,A_1}^{\mathsf T})\mu_1.
\]
Its weighted force norm is at most
\(C_L\|\delta\mu\|_{Y,w}+C_L(\varepsilon_H+\varepsilon_P)M_Hh_1\).
For the second term subtract as
\[
 (R_0Z_0^{\mathsf T}-R_1Z_1^{\mathsf T})\lambda_{00}
       +R_1Z_1^{\mathsf T}(\lambda_{00}-\lambda_{01}).
\]
The bound is
\(C_L(\varepsilon_H+\varepsilon_Ph)C_H\alpha_0+C_Lh_1B_{\rm anc}\).
For the third term the exact subtraction is
\[
 \begin{split}
 &(R_0-R_1)K_{0,0}^{\mathsf T}\lambda_{00}\\
 &\quad +(R_1-I)(K_{0,0}^{\mathsf T}-K_{1,0}^{\mathsf T})\lambda_{00}
       +(R_1-I)K_{1,0}^{\mathsf T}(\lambda_{00}-\lambda_{01}).
 \end{split}
\]
Its bound has the same form, by (5.1)–(5.2). The changed base row map always multiplies a response multiplier or \(R_1-I\), so no bare anchor error remains. On the fixed boundary strip, use (5.9) separately; there \(w\le e^{C_L\theta}\), and the two local scales agree at the compared bond. This also covers bonds whose incident common rows were discarded.

**Theorem D.** Under Theorem C, Loc, (H-field), and the small response ball, the common-gauge comparison is
\[
 \|j_0-j_{1,g}\|_{F,w;G}
 \le C_D(\varepsilon_H+h_0+h_1),\qquad
 C_D=C_L(1+C_{\rm cmp}+C_H)^4(1+\varepsilon_P).              \tag{5.17}
\]
The enlarged polynomial bounds (5.16) and the displayed readout terms, since
\(h\le1\), \(\alpha_0\le1\), \(\varepsilon_P\le1\). Constants are independent of mesh, depth and volume.

Under (H-node), in the assigned representatives,
\[
 \begin{split}
 \xi_b^3|j_0(b)-j_1(b)|
 \le{}&C_De^{-\theta D_b}(\varepsilon_H+h_0+h_1)\\
 &+C_L\varepsilon_N C_H(1+C_H\alpha_0)
                 e^{-\theta_PD_b}h_1.                     \tag{5.18}
 \end{split}
\]
To prove the last term, covariance gives
\(j_1=\operatorname{Ad}(g)j_{1,g}\), with datum and independent current transported by the same gauge. The identities
\[
 gvg^{-1}-v=(g-I)vg^{-1}+v(g^{-1}-I),\qquad
 g^{-1}-I=-g^{-1}(g-I)
\]
bound its norm by the fixed condition bound times \(|g-I||v|\).
Use (H-node) and **the full** (5.9). This retains \(1+C_H\alpha_0\).

Holomorphy follows from the locally uniform walk sums, local formulas and multiplier Neumann series, with the independent current still a variable. At zero response \(T_i=0\), \(R_i=I\), \(\mu_i=0\), and each current vanishes, irrespective of its anchor. Thus the response factor is also an exact algebraic fact. \(\square\)

## 6. The two endpoint radii and the two substitution discs

This comparison does not identify the simple-curvature radius with the hereditary tower radius. Write them as \(a_{\rm s}\) and \(a_{\rm t}\), respectively. In the endpoint input [E] of the gate's Section 4, with \(m=k+1-j\), \(\tau=L^{-m}\), the two estimates are
\[
 \|B_{\rm end}\|\le C_BM a_{\rm s}\tau,\qquad
 \|f(B_{\rm end})\|\le(1+\beta)a_{\rm t}\tau^2.              \tag{6.1}
\]
Here \(f\) is an endpoint curvature/current quantity in its prescribed normalization. The first estimate comes from the simple curvature bound used in axial preparation; the second comes from the input tower clause. The response-ball radius \(r\) in Theorem D is a third, different quantity.

For completeness, the radial argument used with these inputs is elementary. Suppose \(f(0)=0\) on the fixed datum ball, its first derivative is bounded there by \(C_f\), and use a smaller ball on which Cauchy's inequality gives \(\|D^2f\|\le C C_f/r_B\). Put \(g(t)=f(tB)\). Twice integrating \(g''\) shows
\[
 |g(\varsigma)-\varsigma g(1)|
 \le C C_f\|B\|^2/r_B,\qquad 0\le\varsigma\le1.
\]
For example subtract the affine interpolation of \(g\), solve the scalar second-derivative equation with zero endpoint values by its integral kernel, and bound the integral of the absolute kernel by 1. This applies after every unit dual functional, hence in the stated norm. Integrating the first derivative for the extra datum \(B'\) then gives, with the constants used in the gate,
\[
 \begin{split}
 \|f(\varsigma B_{\rm end}+B')\|
 \le{}&\left[(1+\beta)a_{\rm t}
      +4C_fC_B^2M^2a_{\rm s}^{\,2}/r_B\right]\tau^2
       +3C_f\|B'\|.                                      \tag{6.2}
 \end{split}
\]
The whole path and its fixed complex neighbourhood must lie in the datum ball. One sufficient nonlinear allowance is
\[
 4C_fC_B^2M^2a_{\rm s}^{\,2}/r_B\le\beta a_{\rm t}.          \tag{6.3}
\]
There is no replacement of \(a_{\rm s}^2\) by \(a_{\rm t}^2\) without a hypothesis.

Alternatively enlarge both input bounds to the explicit envelope
\[
 \bar a=\max(a_{\rm s},a_{\rm t}),\qquad
 \bar a\le\lambda_a\alpha_{0,k}.                            \tag{6.4}
\]
Choose \(L\) after a fixed \(\lambda_a\), or explicitly assume
\(L^2\ge6\sqrt2\lambda_a\). Require the running-coupling floor
\(x_i\ge X_0\ge\max(C_x,e^{2q},e^2)\), with the named running radii
\(\alpha_{0,i}=C_\alpha x_i^{-1/2}(\log x_i)^q\) and the flow bound
\(x_j\le x_k+C_x(k-j)\) for \(j\le k\).
For \(h(x)=x^{-1/2}(\log x)^q\),
\[
 h'(x)=x^{-3/2}(\log x)^{q-1}(q-\tfrac12\log x)\le0
 \quad(x\ge e^{2q}).
\]
If \(x_j\ge x_k\), the flow bound gives \(x_j/x_k\le m\) and the logarithmic ratio is at most one. If \(x_j<x_k\), monotonicity gives the radius ratio at most one. Thus the gate's weaker bound
\(\alpha_{0,k}/\alpha_{0,j}\le2\sqrt m\) follows. Also
\(\sqrt{m+1}L^{-2(m+1)}/(\sqrt mL^{-2m})\le\sqrt2/L^2<1\);
hence
\[
 \lambda_a\sqrt mL^{-2m}\le\lambda_a\sqrt2L^{-2}\le1/6.
\]
For a fully specified sufficient choice take \(\beta=1/8\),
\(\|B'\|\le c_{B'}\min(\alpha_{0,j-1},\alpha_{0,j})\), and require
\[
 4C_fC_B^2M^2\lambda_a\alpha_{0,k}\le r_B/8,\qquad
 3C_fc_{B'}\le1/8,\qquad C_{\mathcal H}c_{B'}\le1/4,
\]
\[
 C_g(C_BM\bar a L^{-m}+c_{B'}\alpha_{0,j})\le\log(9/8).
\]
Applying (6.2) with the envelope in both places, the normalized curvature/current bound after the condition-number factor is at most
\[
 \frac98\left(\frac54\,2\sqrt2\lambda_a L^{-2}+\frac18\right)
 \le\frac98\left(\frac5{12}+\frac18\right)
 =\frac{39}{64}<1.
\]
This is hand arithmetic, using the displayed choice of \(L\). The potential margin still requires
\[
 C_BM\bar a L^{-m}+\|B'\|<\min(r_I,r_B/4),\qquad
 \alpha_{1,j}\ge\alpha_{0,j},\qquad
 \alpha_{1,j}>4C_{\mathcal H}C_BM\lambda_a L^{-1}\alpha_{0,j},
\]
with both inequalities imposed throughout the admitted datum ball. Indeed \(\sqrt mL^{-m}\le L^{-1}\) for \(L\ge2\), by the same successive-ratio estimate; the endpoint potential is at most \(2C_{\mathcal H}C_BM\lambda_aL^{-1}\alpha_{0,j}\), and the independent datum adds at most \(\alpha_{0,j}/4\). These conditions are not consequences of Theorem D. Nor does (6.2) replace the hereditary restriction identity: Balaban's (3.38), or the named RI input, is what transfers all lower tower clauses.

Keep gauge products in their actual order. With \(U^g(b)=g(b_-)U(b)g(b_+)^{-1}\), one has \((U^u)^{\widetilde v}=U^{\widetilde v u}\). The raw-to-lower-tower factor is therefore \(g_Zu^{-1}\widetilde v^{-1}\), not a reordered product. Multiplying their separate condition bounds is valid; commuting the factors is not. These restriction factors do not themselves prove (H-node) between two independently assigned Landau maps.

Finally the inner datum disc and each removed-map disc remain separate. SA 15953 and R11 (5823–5825) explicitly distinguish them. Theorem D applies on a specified common parameter domain on which **its** Pair/Field/Node hypotheses hold; it does not extend a removed map by using the larger inner endpoint radius.

## 7. Which box the window uses, and the smaller true application

### 7.1 Exact source locations and the type of each map

The relevant pinned SA locations are:

| SA lines | Map or assertion actually specified |
| --- | --- |
| 5596–5610 | Two erosion assignments, with actual sets required; their gap inequalities alone do not specify a map. |
| 5612–5627 | Determining rows and their nodes, including exclusion of inward rows entering the next member. |
| 5762–5785 | R9 and its specified propagators; the independent-current multiplier is a separate required component. |
| 9759–9772 | Inner background of a current box; the **first-rule** tower is truncated at the old depth \(j\), at its nonlinear averaged datum. |
| 9776–9781 | Sequence restriction is an identity at the restricted background's **own** determining datum, modulo the prescribed residual gauge. |
| 9783–9789 | Joined localization: retain the old sequence inside, use towers in collars; the single-part, one-lattice localized background uses the \(M_1'\) tower and the lifted datum. The quoted decay is in the determining sequence's weighted distance. |
| 15753–15779 | WF3 forms the actual nonlinear average; WF4 takes its old-level critical box background and its actual current, with node/gauge representatives. |
| 15821–15834 | Weighted first-response, Hölder and compatible boundary comparison for those maps are assumptions of the window package. |
| 15850–15866 | WF7 requires the removed factor \(e^{-cM/\sigma_j}\), and retains an actual-distance version for outer sums. |
| 15947–15959 | Distinguishes outer response, inner background, and the two replacements generating removed fields; requires assigned nodes and prescribed reduced currents off the physical locus. |
| 15961–15971 | Inner datum \(\varsigma B+B'\), Landau representative, and restriction over its own averages. |
| 16137–16176 | WF13a: one current window, one enlarged \(R_z\), one old-level constrained critical box map used for all near \(X\); its domain is a local pair at the current resolved level \(k\). |
| 16826–16852 | OA7 and the still-required compatible boundary comparison for actual box backgrounds. |

These lines do not specify the window by simply restricting the rows of the original \(H_k\). They explicitly insert a nonlinear average and then an old-level determining problem. The counterexample of Section 1.3 respects precisely this old-depth truncation and all the simple/tower field bounds at zero data.

In particular, the two changes must be distinguished:

1. Localize a response or background **at its existing depth**, retaining the original members on a central region. This can satisfy (H-seq-sym), with the collar/read-set loss proved below.
2. Form the old-level WF4/WF13a background from the current-level field. This changes depth and rows even in the centre of a perfectly flat window. The step sequence and this old box do not satisfy (H-seq-sym). Their comparison has to pass through the old truncated problem and the actual averaging/transport map.

This is a counterexample to the proposed direct application, not a counterexample to the window identities or their explicitly assumed response estimates.

### 7.2 Same-depth localization: symmetric agreement with a quantified loss

Here is a useful true statement that also identifies the distance a consumer may read.

**Lemma G (box geometry).** Let \(S=(\Omega_q)_{0\le q\le n}\) have top scale \(\xi_n\), and let \(R\) be an aligned non-wrapping cube. Let \(T_q(R)\) be either adopted tower, **at the same absolute levels and cut at the same depth \(n\)**. Put
\[
 \Omega'_q=\Omega_q\cap T_q(R),\qquad
 e_n=\sum_{q<n}c_q,\qquad
 c_q=\begin{cases}
 \rho\xi_q+\mathfrak M\xi_{q+1},&\text{first rule},\\
 2M_1'\xi_{q+1},&\text{second rule}.
 \end{cases}                                               \tag{7.1}
\]
Assume the two resulting systems meet the W/AB geometric thresholds and common conventions. Define
\[
 b_*=4L^2M_1,\qquad
 G=\{x\in R:\ d_\infty(x,R^c)>e_n+b_*\xi_n\}.               \tag{7.2}
\]
Then (H-seq-sym) holds on \(G\). For every \(x\in G\),
\[
 D(x)\ge
 \frac{[d_\infty(x,R^c)-e_n-b_*\xi_n]_+}{\xi_n}.             \tag{7.3}
\]
Empty \(G\) gives no interior claim. A pure tower in place of the meet has the same conclusion only if \(S\) is constant at top depth \(n\) on the needed enlarged interior.

*Proof.* The induction used for (1.2), with the two displayed \(c_q\), proves
\(\{d_\infty(\cdot,R^c)>e_q\}\subset T_q\).
Since \(e_q\le e_n\), all \(T_q\) contain
\(E=\{d_\infty(\cdot,R^c)>e_n\}\).
Thus every \(\Omega'_q\) equals \(\Omega_q\) on \(E\). Members above \(n\) are empty in both systems.

Consider any cube of either walk family with \(\kappa^{(4)}\subset G\).
Its centre has depth greater than \(e_n+b_*\xi_n\).
Its sharp enlargement has half-side \(4L^2M_1\xi_\kappa\le b_*\xi_n\).
Every point of that enlargement therefore lies in \(E\).
Agreement holds on \(G\) and on **every** such sharp enlargement from **both** families, proving (3.2). This checks absent candidates as well as present ones.

All native scales are at most \(\xi_n\), including the bare extension outside the determining region. Hence every path has native length at least its physical sup displacement divided by \(\xi_n\). The function \(d_\infty(\cdot,R^c)\) is 1-Lipschitz. A path from \(x\) to \(G^c\) must lower it to at most \(e_n+b_*\xi_n\), so its length has the lower bound (7.3). Taking the infimum proves the claim. No comparison of exterior pillar counts enters. For a pure tower, equality with \(S\) on \(E\) requires all \(\Omega_q\) to contain \(E\), which is precisely the stated constant-top condition. \(\square\)

For the specified joined sequence \(\Omega'_q=\Omega_q\cap\bigcap_aT^a_{\min(q,j_a)}(R_a)\), a sufficient common region is
\(\bigcap_a\{d_\infty(\cdot,R_a^c)>e^a_{j_a}+b_*\xi_n\}\).
Every tower factor contains the corresponding less-eroded region, and every sharp enlargement has half-side at most \(b_*\xi_n\). These two facts prove (3.2) exactly as above, including all indices \(q>j_a\). An arbitrary pure tower cannot replace this meet over a layered region.

**Corollary G-D.** For the same-depth meet of Lemma G, assume AB/Loc, the Pair/Field bounds and, for assigned representatives, Node, on the region (7.2). Then Theorems C and D hold with the actual distance (3.3), hence with the lower bound (7.3) substituted in the output exponential. This is a proved implication, by Lemma G and Theorems C–D; it introduces no actual-map identification.

For example, if the compared original has already been truncated to depth \(j\), \(R\) is a current-scale box, and the readout lies physical distance at least \(cM\xi_k\) from its boundary, then \(\xi_n=\xi_j=\sigma_j\xi_k\) and
\[
 D\ge cM/\sigma_j-e_j/\xi_j-b_*.
 \tag{7.4}
\]
The collar loss is bounded by
\((\rho+L\mathfrak M)/(L-1)+b_*\) for the first rule, or
\(3M_1'+b_*\) for the second. Choose \(M\) after these fixed sizes. The harmless prefactor in (4.2) is also fixed before \(M\). Thus (7.4) yields an exponential \(C e^{-c'\! M/\sigma_j}\) for **this old-depth comparison**, when its pair/field assumptions and response amplitude estimates hold.

If the compared systems instead remain at depth \(k\), the same lemma gives only
\[
 D\ge cM-e_k/\xi_k-b_* .                                  \tag{7.5}
\]
Expressing their potentials in old units multiplies the potential amplitude by \(\sigma_j\) (and currents by its cube); it does not replace the exponent in (7.5) by the exponent in (7.4). This is the smaller statement justified by the same-depth response comparison.

### 7.3 What is still required to apply (7.4) to the actual composite

A real critical restriction identity can equate the *values* of a larger background and a smaller background at its own averages. Its differentiated identity retains every map in the composition. Writing \(\rho\) for restriction, one has, in a common representative when such an identity has been established,
\[
 \Phi_{\rm old}\big(M_{\rm old}(\rho\Phi_{\rm current}(v))\big)
       =(\rho\Phi_{\rm current}(v))^{u(v)}.                 \tag{7.6}
\]
Differentiating a curve \(v(t)\) gives on the left
\[
 D\Phi_{\rm old}\big(M_{\rm old}(\rho\Phi_{\rm current})\big)
 \;DM_{\rm old}(\rho\Phi_{\rm current})
 \;\rho D\Phi_{\rm current}[\dot v].                       \tag{7.7}
\]
On the right there is the transported restricted response **and** the derivative of \(u(v)\). Formula (7.7) follows by subtracting the value at \(t=0\), dividing by \(t\), and using the defining first-derivative remainders for each finite-dimensional holomorphic map; their product remainder tends to zero. Thus even where (7.6) is known, (7.7) does not identify the old lift with the current lift. Their raw row spaces already differ in Section 1.3.

At decoupled parameters the constraint identity \(K_0H(s)=I\) is not available; Definition D was not specified to preserve it. A physical restriction identity alone therefore supplies neither (7.6) for arbitrary independent-current responses nor its decoupled version. This is why Theorem D used only the anchored equations rather than that constraint identity.

The true alternatives are consequently explicit. One may compare the two old-depth backgrounds **after** proving the required holomorphic composition and node/current transport identities on the independent fine-parameter discs, and then verify Pair/Field for that old-depth comparison. Or one may retain the same-depth response comparison (7.5), with its actual distance and native norms, and prove separately that the remaining window estimates suffice with that weaker exponential. This note proves the geometric and current comparisons in both stated conditional forms; it does not change the maps or assert that either missing composition has been established.

## Result

**Proved, as implications from named inputs:**

* **C1-sym and Theorem C:** from W, AB, common specifications, (H-seq-sym) and (H-pair), the common-interior lift/whole-curl differences and their transposed-source bounds (4.4)–(4.7). Exterior contributions use their own energy norms, gradients, scales, pillars and ball counts.
* **Theorem D:** from Theorem C, Loc, the small response ball and (H-field), the anchored removed-current bound (5.17); with (H-node), the assigned-representative bound (5.18). It keeps the response form of F1, counts the curl change once, and retains \(C_H(1+C_H\alpha_0)\) in the node term.
* **Endpoint bookkeeping:** (6.2) follows from the two distinct endpoint inputs (6.1) and their admitted holomorphic derivative bounds. It does not identify \(a_{\rm s}\) with \(a_{\rm t}\), or an inner disc with a removed-map disc.
* **Actual geometry:** the old-level WF box of Section 1.3 need not agree with the step sequence at even one central point. Lemma G proves symmetric agreement for a specified **same-depth meet**, with the exact collar/read-set loss. Corollary G-D gives the smaller true current comparison with that complement distance. The age-enhanced exponent follows only for the old-depth comparison (7.4), not by changing units in (7.5).

**Where rank 4 stops.** The abstract removed-current comparison is repaired under its explicit hypotheses. The old assertion that it already matches all actual WF removed maps is not proved: the old-level box and the current response are different determining problems. A compatible old-depth composition/restriction identity, including actual nonlinear averages, independent-current readouts and assigned node transport on the full decoupling discs, is still required to use the \(M/\sigma_j\) consumer. Independently, the named analytic inputs remain open where previously open: pointwise decoupled first-system response bounds supplying (H-field), complex 6(c) for the actual box pair, and the Landau (H-node) comparison. No audit result, retained-grade status, or rank-4 closure follows from this research text.
