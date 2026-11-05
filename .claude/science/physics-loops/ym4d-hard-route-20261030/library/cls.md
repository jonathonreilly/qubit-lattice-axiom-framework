# (Cls+) and proposed IN1 Amendment 2

Provenance: Codex, 2026-11-05, checkout 6d32a8426981c641476b4e92af838ac65220796e. Pass 2 distillation of Claude's cls-draft.md; research text, not an audit, granting no status. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the source constructions used below. This text is not yet refereed.

The draft's uniform width estimate is valid under explicit geometry. Its claim that **(Cls+) follows with no strengthened imports is not established**. The main statement separates these conclusions. Frozen IN1, including Amendment 1, is not edited.

## 1. Definitions and main statement

Write IN1, TD, TD2, DRL and AG1 for in1.md, td.md, td2.md, drlocp-draft.md and ag1.md. SA denotes the outline at upstream revision 31a47c543775. The assembly position is IN-C4/IN-order, through CI's exempt-term filing.

**D1 (units and lengths).** At level \(j\), \(\mathcal C_j\) is the graph of aligned level-\(j\) \(M\)-cubes, with corner adjacency, degree at most 80, and distance \(d\). Use consistent nonwrapping lifts for boxes. Write \(N_uA=\{x:d(x,A)\le u\}\), \(s(A)\) for the largest side of the least coordinate box, and \(\pi_j\) for coarsening by \(L\). The early unit comparison imported by TD is required; \(M^{-1}\) times continuum tree length is not silently identified with an edge count.

For nonempty finite \(X\) and a finite family \(\mathsf F_0\) of nonempty sets, define \(\delta_{\mathsf F_0}(X)\) by minimizing \(|E(T)|\) over subfamilies \(\mathsf F\subset\mathsf F_0\), every \(F\subset X\), and ordinary trees meeting each \(F\) and every cube of \(X\setminus\bigcup\mathsf F\). Extra vertices are allowed. Crossings cost edges. Define \(d_{\mathsf F_0}(X)\) with the additional requirement \(T\subset X\), and value infinity if no such tree exists. Then \(\delta_{\mathsf F_0}\le d_{\mathsf F_0}\). Superscript “old” below means the same graph convention with only the \(H_j\)'s excused. Transferring a source's continuum-normalized bound to this convention, including its rate, is part of the unit-conversion import.

This distinction is necessary. SA 5865–5867 and IN1 define the ordinary tree inside its domain. SA 6191–6198 adds the exempt-family rule without explicitly removing that restriction. CA-II 16026–16029 and CA-III 3519–3524, 12287–12288 require an in-domain tree, though their relative-domain convention differs from SA's selectable family. Below \(d^+\) retains the in-domain requirement for IN1. The ambient length \(\delta^+\) is used where DRL constructs an ambient tree. Their equality is not assumed.

**D2 (geometry, owned by LF1).** Fix \(C=C_{\rm isl}\ge1\), \(c=c_{\rm col}\in\mathbb N_0\), and \(C_{\rm pr}\ge1\) before \(\kappa\), independently of \(M,\bar\kappa\). Constants used to choose \(L\) are uniform in \(L\); choose odd \(L\ge27\). Histories are finite, as in IN1. Assume at every relevant level:

* **G:** standing hulls \(H_j(\alpha)\) have hubs \(U_j=N_2H_j\), with \(s(U_j)\le D_j:=CL\check R_j+6\); distinct hubs have distance at least \(\check R_j-4\). Every gas cube has distance at least \(G_j:=10L\check R_j-2\) from every hub **and from the live set**. This does not say that the live set is far from the hubs.
* **Drop:** \(\check R_j/\check R_{j+1}\in\{1,L\}\), with no consecutive drops. Hence \(\check R_{j-k}\le L^{\lceil k/2\rceil}\check R_j\). These are the source's stated running-minimum properties.
* **Mon:** each standing island has one standing successor \(\beta\), possibly a swallowing island, with \(\pi_jH_j(\alpha)\subset U_{j+1}(\beta)\), or is retired by healing. A successor can have several predecessors. The history specifies this map. Its uniform realization remains an LF1 import.
* **Lift:** every box and neighbourhood used below embeds with its read margins. This is a torus condition for the enlarged sets, not a consequence of a side bound alone.

Matching TD2's step-\(i\) fine cubes (level \(i-1\)) to these level-\(j\) cubes remains the named scale conversion. A level-\(j\) cell has side \(M\check R_j\) in its own units, hence \(\check R_j\) of its own \(M\)-cubes, or \(L\check R_j\) preceding-level fine cubes. The draft interchanges these conventions.

**D3 (recursive members).** Fix
\[
0<\eta\le\eta_\sharp:=\min\{[16(C+1)^2L]^{-1},(4+2c)^{-1}\}.
\]
At every birth or continuation, including a new island swallowing predecessors, define
\[
 R_j(\beta)=N_cU_j(\beta)\ \cup
 \bigcup_{\alpha\mapsto\beta}\pi_{j-1}M_{j-1}(\alpha),\qquad
 \rho_j=\lceil\eta s(R_j)\rceil,\qquad
 \widehat R_j=N_{\rho_j+2}R_j,\quad M_j=N_{\rho_j+3}R_j.       \tag{1}
\]
Only an island with no predecessors starts with \(R_j=N_cU_j\). This resolves the draft's conflicting birth and swallowing rules. Set
\[
 \mathsf H_j^+=\{H_j(\alpha),M_j(\alpha):\alpha\text{ standing}\},
 \qquad d_j^+=d_{\mathsf H_j^+},\quad\delta_j^+=\delta_{\mathsf H_j^+}. \tag{2}
\]
A slot retains its formation-time family record and length, together with its function and analytic domain. Later read projection and later filing are separate operations.

**D4 (consumer imports).** Retain TD2's R, A, X, RUN and G-ord in full: actual response on its product source ball; arbitrary-shift admission with complete stencils, pins and stored reads; the complex island deficit; and
\[
 \widetilde\omega_f\le\widehat\omega_fe^{-\kappa d_f},\qquad
 \sup_z\sum_{f:X(f)\ni z}\widehat\omega_fe^{-\kappa d_f/2}
 \le N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}.            \tag{3}
\]
Here \(X(f)\subset X_f\) is the complete read set, \(d_f\) its supplied old length, and \(\ell=\log\theta_{i-1}\). RUN includes \(\check R_i\ge(\ell-1)^{r_R}\), \(r_R\ge2\). Replace X° by the supplied ordinary-tree condition
\[
 |E(T_f)|\le C_{\rm pr}(1+d_f),\quad
 X_f\subset N_cT_f\ \cup\!\!\bigcup_{\alpha:T_f\cap R_i(\alpha)\ne\varnothing}R_i(\alpha),
 \quad X_f\cap(\text{hubs}\cup\text{live set})\ne\varnothing. \tag{4}
\]

Write \(\operatorname{St}(W)\) for the least edge count of an ambient tree covering \(W\). For nonempty \(A\), \(m_A(W)\) is the MST of \(W\cup\{*\}\) with weights \(d(w,w')\) and \(d(w,A)\) to the root; \(m_A(\varnothing)=0\). Retain TD2 (4)–(5)'s source variables, \(\vartheta\), Boolean coefficients and admitted pair/source set \(P\in\mathcal O_\sigma(U)\), \(|\zeta|_c\le\mathfrak b\).

For pair filing also import DRL's admitted joint coefficient bound (Theorem 2, \(\tau=a\), Lemma 4.3), exact Boolean decomposition and pair-locality (Proposition 5.1′). Their inputs remain R/A, complete stencils, the corner deficit, TJ, DR-locP with UNQ, RED, walk support, UNQ-loc and S-loc. Supremums in (13) are on that common admitted global pair/source set. Locality on restrictions of global pairs does not establish bounds on every declared local pair. Gaussian pair-heredity G-P and CI's actual local Gaussian/formation packages are separate cluster-step imports.

**Theorem 1 (main statement, conditional).** Under D1–D3 and
\[
 \check R_j\ge R_\sharp:=\max\{10(c+12),64+8c\},              \tag{5}
\]
the cores obey the uniform width estimate (7), the members obey (8), and old member cubes project into the cores of their standing successors. These conclusions are independent of the number of steps and swallowings. Under D4 and §4's ordered rate conditions, ordinary TD and the ambient filing estimate (13) hold. Filling a carrier as in Lemma 8 gives an in-domain length bound as a geometric assertion.

The **full (Cls+) conclusion**, IN1 Theorems 10–12 for the enlarged class, additionally requires the matching conditions in §5 on every admissible prefix. Their supply from the unchanged imports is **Outstanding**. This is not the pass-1 “no new import” claim.

*Proof.* Lemmas 2–5 prove geometry and read containment. Lemmas 6–8 prove the entropy, ordinary-decay and filing implications. Lemmas 9–11 isolate the failed inferences. With the matching conditions supplied, Proposition 12 applies IN1's conditional induction. ∎

## 2. Geometry and persistence

**Lemma 2 (coarsening and monotonicity).** For integer \(u\ge0\),
\[
 d(\pi x,\pi y)\le\lceil d(x,y)/L\rceil,\quad
 \pi(N_uA)\subset N_{\lceil u/L\rceil}(\pi A),\quad
 s(\pi A)\le\lceil s(A)/L\rceil+1.
\]
A projected tree has a spanning tree with no more edges. Adding the \(M_j\)'s weakens both lengths: \(d_j^+\le d_j^{\rm old}\) and \(\delta_j^+\le\delta_j^{\rm old}\). A minimizing subfamily can be chosen to contain at most one of \(H_j(\alpha),M_j(\alpha)\).

*Proof.* Write \(b=qL+v\), \(0\le v<L\). Then
\(\lfloor(b+u)/L\rfloor-\lfloor b/L\rfloor\le\lceil u/L\rceil\).
Apply this in each coordinate, also to neighbourhoods and extreme coordinates of a box. Images of adjacent vertices coincide or remain adjacent, so delete cycles from the connected image graph. Every old admissible family/tree remains admissible after adding members. If both nested members are chosen, delete the smaller without changing covered cubes or the meeting requirement. ∎

**Lemma 3 (no accumulation).** Let \(e_j\) be the least integer with \(R_j\subset N_{e_j}(N_cU_j)\), and \(A_j=D_j+2c\). Then
\[
 e_{j+1}(\beta)\le\max_{\alpha\mapsto\beta}
 \left\{\frac{(1+2\eta)e_j(\alpha)+\eta A_j+1}{L}+\frac65\right\}, \tag{6}
\]
with \(e=0\) if there is no predecessor, and uniformly
\[
 e_j\le\frac{38}{33}\eta A_j+\frac{334}{255}
       <\frac{29}{25}\eta A_j+\frac{33}{25}.                  \tag{7}
\]

*Proof.* Since \(M_j\subset N_{e_j+\rho_j+c+5}H_j\), Lemma 2 and Mon put its image within
\(\max\{0,\lceil(e_j+\rho_j+c+5)/L\rceil-c\}\)
layers of \(N_cU_{j+1}\). This is at most \((e_j+\rho_j)/L+6/5\), since \(L\ge27\). Also \(\rho_j\le\eta(A_j+2e_j)+1\). Taking the maximum proves (6).

Follow maximizing predecessors through the finite history. Branching adds a maximum, not a sum. Iteration from a predecessor-free birth and Drop give
\[
 e_j\le\eta A_j\sum_{k\ge1}(3/2)^{k-1}L^{-\lfloor k/2\rfloor}
 +(L^{-1}+6/5)\sum_{k\ge1}(3/(2L))^{k-1}.
\]
Pair consecutive terms. The first sum is at most
\(1+(5/3)\sum_{m\ge1}(1/12)^m=38/33\).
The second contribution is at most
\((1/27+6/5)/(1-1/18)=334/255\).
These rational bounds imply (7). ∎

**Lemma 4 (member geometry).** Put
\[
 E_j=\frac{\check R_j}{13(C+1)}+4,\quad
 w_j^*=\frac{\check R_j}{6(C+1)}+c+12,\quad D_j^*=2CL\check R_j+6.
\]
Under (5),
\[
\begin{gathered}
 e_j\le E_j,\qquad \rho_j\le\frac{\check R_j}{15(C+1)}+3,\qquad
 M_j\subset N_{w_j^*}H_j,\qquad s(M_j)\le D_j^*,\\
 d(M_j(\alpha),M_j(\beta))\ge\check R_j/2\quad(\alpha\ne\beta),\\
 d(\text{gas},M_j)\ge G_j-w_j^*,\qquad
 d(\text{gas},R_j)\ge G_j-e_j-c,\qquad
 \pi_jM_j(\alpha)\subset R_{j+1}(\beta)\subset M_{j+1}(\beta).
                                                               \tag{8}
\end{gathered}
\]
Same-island members overlap. Nonwrapping uses Lift.

*Proof.* The \(\eta\)-ceiling gives \(\eta A_j\le\check R_j/[16(C+1)]+3/2\).
Use (7) and \(29/400<1/13\) to obtain \(e_j\le E_j\). Since \(\eta\le1/1728\),
\[
 \rho_j\le\eta A_j+2\eta E_j+1
 \le\left(\frac1{16}+\frac1{11232}\right)\frac{\check R_j}{C+1}
       +\frac52+\frac1{216}
 \le\frac{\check R_j}{15(C+1)}+3.
\]
Now \(M_j\subset N_{e_j+\rho_j+c+5}H_j\) and \(1/13+1/15<1/6\). Therefore
\(s(M_j)\le CL\check R_j+2+\check R_j/3+2(c+12)\le D_j^*\)
by (5). Its width over \(U_j\) is at most \(w_j^*-2\). Subtract twice this from \(\check R_j-4\), obtaining at least \(5\check R_j/6-2(c+12)\ge\check R_j/2\).
Subtracting the widths from the gas gap proves the next two bounds. The last is (1). ∎

**Lemma 5 (what read projection proves).** Let an old slot at \(j<t\) have \(d_f\ge\delta_j^+(X)\), and let all its chosen exempt islands have standing successors. A minimizing tree projects to a tree with at most \(d_f\) edges. Every cube of \(\pi^{t-j}X\) is on that tree or in a successor core met by it.

*Proof.* An unexcused cube was met by the original tree. A chosen member lies inside \(M_j\); (8), iterated, places its image in a current core. The original tree met the member, so the projected tree meets that core. Lemma 2 bounds its edges. ∎

**Outstanding — complete reads.** Lemma 5 proves member containment, not complete read coverage, endpoint/pin inclusion or unit conversion. To infer (4), prove that each additional stencil lies in a met core or within \(c\) of the projected tree. A \(c\)-neighbourhood of a core can leave that core. DRL Proposition 5.1′ supplies an upper carrier, not dependence on every cube of it. Retired islands require healed-component containment. These qualifications replace the draft's unconditional discharge of TD2's read-collar obligation.

## 3. Consumer estimates

**Lemma 6 (old sums and carrier entropy).** For an already supplied term with old length \(d_o\ge d_j^+(X)\), keeping \(d_o\) preserves (3). Alternatively use \(d_f=d_j^+(X)\) and \(\widehat\omega_f=\widetilde\omega_fe^{\kappa d_f}\); its old per-read sum still bounds the new sum. At one level, with one slot per carrier, if \(e^{\kappa/2}\ge76800\),
\[
 \sum_{\varnothing\ne X\subset A}e^{-\kappa\delta_j^+(X)}\le36|A|,
 \qquad
 \sum_{X\ni z}e^{-\kappa\delta_j^+(X)/2}\le12(1+2V_*),
 \quad V_*=(D_j^*)^4.                                      \tag{9}
\]
Both inequalities also hold with \(d_j^+\).

*Proof.* For amplitudes,
\[
 \widetilde\omega_fe^{\kappa d_f/2}
 \le\widehat\omega_f^{\rm old}e^{-\kappa d_o+\kappa d_f/2}
 \le\widehat\omega_f^{\rm old}e^{-\kappa d_o/2}.
\]
Reads are unchanged. For entropy, choose one minimizing tree and normal-form subfamily per \(X\). A tree with \(n\) edges from a specified root has at most \(80^{2n}=6400^n\) depth-first codes. It meets at most \(n+1\) islands, since different members are disjoint. Choose none, \(H\), or \(M\) at each island, then choose the unexcused subset of its vertices: at most \(6^{n+1}\) choices recovering \(X\).

For \(X\subset A\), root at its least unexcused cube, or at a meeting vertex of its first chosen member if every cube is excused. There are at most
\(|A|+\sum_{F\subset A}|F|\le3|A|\) labelled root choices. Sum
\(18|A|\sum_{n\ge0}(38400e^{-\kappa})^n\le36|A|\).
For \(X\ni z\), root at \(z\) if unexcused, or at a meeting vertex of one of the at most two members containing \(z\). There are at most \(1+2V_*\) choices, giving
\(6(1+2V_*)\sum_{n\ge0}(38400e^{-\kappa/2})^n\le12(1+2V_*)\).
Finally \(d^+\ge\delta^+\). ∎

**Outstanding — actual multiplicities.** (9) counts carriers at one level, not all old levels, origins or stored factors. Those multiplicities and (3) for new terms remain producer inputs. The universal “factor at most 40” is withdrawn; (9) gives explicit bounds without comparing unspecified old prefactors. Its half-rate estimate requires \(\kappa\ge2\log76800\), not merely \(\log76800\).

**Lemma 7 (ordinary TD and AG1 geometry).** Assume (3)–(4), G and (8), and put \(\eta_o=1+C/10\). If
\[
 (10L-3/13)\check R_i\ge18+2c+(1+C/10)(2+c)+2C/5,             \tag{10}
\]
then, with TD2's rooted MST \(m=m_{X(f)}(W)\),
\[
 \operatorname{St}(W)\le(1+\eta_o)m+C_{\rm pr}(1+d_f)+c|W|,
 \qquad m+C_{\rm pr}(1+d_f)+2c+E_i\ge G_i.                   \tag{11}
\]
TD2 Theorem 3 consequently holds with the same \(\eta_o\) and rate floors, replacing its tail gap by \(G_i-C_{\rm pr}-2c-E_i\).

For AG1, additionally assume its complete read-hull hypothesis with at most \(C_{\rm tr}(d_f+1)\) ordinary tree cubes and the chosen members. Use a common early bound \(C\) for its \(C_0^{\rm isl}\) and D2's geometry. If \(L\check R_i/10\ge w_i^*+4\), then for each gas cube \(\Delta\),
\[
 \operatorname{diam}X_f\le c_g^\sharp(d_f+1)+(20C/99)d(\Delta,X_f),
 \qquad c_g^\sharp=(2+6CL)C_{\rm tr}+7.                       \tag{12}
\]
Its boundary argument uses \(\kappa_P\le\kappa/(2c_g^\sharp)\) and \(\bar\kappa\ge8\kappa_PC\). Its N-B sum remains an import.

*Proof.* Realize the root MST by geodesics. A read endpoint near \(T_f\) costs at most \(c\) to join it. Otherwise it lies in a met core. A connector costs at most \(D_i+2c+2E_i\), while the root edge costs at least \(G_i-c-E_i\). Condition (10) implies
\[
 D_i+2c+2E_i\le\eta_o(G_i-c-E_i),\qquad
 (3+C/10)E_i\le(3/13)\check R_i+12+2C/5.
\]
At most \(m/(G_i-c-E_i)\) such connectors occur. This proves the first bound. To reach a hub from a core costs at most \(c+E_i\); otherwise traverse \(T_f\) to the hub or live-set read in (4). This proves the second.

Set \(\vartheta_T=\vartheta e^{\lambda_Tc}\), \(a_1=a-6-\lambda_T(1+\eta_o)\) and
\(\nu=\min\{\kappa/(4C_{\rm pr}),a_1/2\}\).
Under TD2 (11), reserve \(\kappa d_f/2+a_1m/2\) for summation. The remaining exponent is at least \(\nu(G_i-C_{\rm pr}-2c-E_i)\). Assign each \(f\) to a nearest read cube to a fixed cube of \(W\). Equation (3) and TD Lemma 1's hand bound \(\sum_z e^{-6d(z,z_0)}\le2\) give TD2's prefactor \(2e^{\kappa/4}N_{\rm ex}\vartheta_T\). RUN makes its uniform tail tend to zero.

For (12), contract each member in the connected read hull and take a simple path between the desired endpoints. Expand each visited member by an ambient geodesic of length at most its diameter. At most
\(1+|T_f|/(\check R_i/2-1)\) members are visited, since between successive members the path uses that many ordinary cubes. The expanded walk has length at most
\[
 \left[1+\frac{2CL\check R_i+7}{\check R_i/2-1}\right]|T_f|
       +2CL\check R_i+7.
\]
The bracket is at most \(2+5CL\) under (5), which gives \(\check R_i\ge120\). The draft's isolated assertion for every \(\check R_i\ge10\) was too strong. Start at a closest read to \(\Delta\) and stop at the first chosen member. The gas gap gives
\(10L\check R_i-2-w_i^*\le d(\Delta,X_f)+|T_f|+2\).
Thus \((99/10)L\check R_i\le d(\Delta,X_f)+|T_f|\). Substitute into the additive member diameter and use \(2+5CL+20C/99\le2+6CL\). With no member the tree suffices. Multiplying by AG1's \(2\mathsf Be^{-\kappa d_f}\) leaves its half-rate summand; the \(\bar\kappa\)-floor pays the distance term. ∎

**Lemma 8 (filing for actual, possibly nonconvex cores).** Put
\[
\begin{gathered}
 a=\tfrac12\log((e^{\bar\kappa}-1)/6400),\quad r_d=a/2-6,\quad
 q_s=48e^{1-a},\quad\eta=4\lambda_P/r_d,\\
 C_4=C_{\rm pr}+(2c+3)^4(C_{\rm pr}+1),\qquad
 \Psi_\eta=\sup_{x\ge0}x^4(2\eta x+9)^3e^{-12\eta x}.
\end{gathered}
\]
Assume D1–D4, (5), (10), DRL F1–F2, \(\eta\le\eta_\sharp\), its coupling ceilings, and the following replacement for F4:
\[
 2q_s(C_{\rm pr}+1)\{2(2c+1)^4+16\Psi_\eta\}\le\kappa/16.    \tag{F4*}
\]
Set \(N_f=X_f\cup\bigcup_{T_f\cap R_i(\alpha)\ne\varnothing}\widehat R_i(\alpha)\) and \(Y_{f,V}=N_1(N_f\cup V)\). For every nonempty gas set \(W\),
\[
 \sum_f\sum_{V\subset\mathcal C_i\setminus N_f}
 \sup|f_{W,V}|e^{\lambda_P\delta_i^+(Y_{f,V})}
 \le A_Pe^{-\lambda_T\operatorname{St}(W)},\qquad
 A_P=6e^{\kappa/2}\vartheta_PN_{\rm ex}
       e^{-\nu_g(G_i-C_{\rm pr}-2c-E_i)},                    \tag{13}
\]
where \(\nu_g=\min\{\kappa/(8C_{\rm pr}),3\}\) and
\(\vartheta_P=6\vartheta e^{(\lambda_P+\lambda_T)c+1}<1\).
The uniform envelope tends to zero with \(\gamma\).

*Proof.* Nonzero pieces have \(W\subset N_f\cup V\) by their Boolean definition. Let \(m=m_{X(f)}(W\cup V)\). Join \(T_f\), radius-\((c+1)\) balls about its vertices, root-MST geodesics, connectors from their read endpoints to \(T_f\), and the 80-edge neighbour stars at \(v\in V\). Excuse precisely the \(M_i(\alpha)\)'s whose cores meet \(T_f\); each lies in \(Y_{f,V}\).

A root endpoint in a core can be joined across its box in at most \(s(R_i)\) edges. A root child outside the base costs at least \(\rho_i+3\ge\eta s(R_i)\). A gas child has this bound by (8), (5). Other connectors cost at most \(c\). Since \(|V|\le m\), the constructed connected graph \(U_{f,V}\) has a spanning tree of length at most
\[
 C_4(1+d_f)+(81+c+1/\eta)m+c|W|.                             \tag{14}
\]
It covers all unexcused carrier cubes. This is an ambient-tree estimate: \(U_{f,V}\) can leave \(Y_{f,V}\).

A core need not be a box. Write \(s=s(R_i)\), so \(|R_i|\le s^4\). Assigning a nearest core point and overcounting by all core points gives
\[
 \sum_{v\notin N_{\rho_i+2}R_i}e^{-12d(v,R_i)}
 \le |R_i|\sum_{n\ge\rho_i+3}8(2n+1)^3e^{-12n}
 \le16s^4(2\rho_i+7)^3e^{-12(\rho_i+3)}
 \le16\Psi_\eta.                                           \tag{15}
\]
Consecutive shell terms have ratio at most \(27e^{-12}<1/2\). This covers holes and nonconvexity. Counting only shells outside the bounding box, as the draft does, omits possible cubes inside that box.

There are at most \((C_{\rm pr}+1)(1+d_f)\) met cores. Reads within \(c\) of \(T_f\) contribute at most
\(2(2c+1)^4(C_{\rm pr}+1)(1+d_f)\) to the shell sum. Hence (F4*) pays its exponent by \((\kappa/16)(1+d_f)\).

D4 bounds each piece by
\(3\widehat\omega_fe^{-\kappa d_f}(3\vartheta)^{|W|}q_s^{|V|}e^{-r_dm}\).
Multiply by (14), using \(\lambda_P/\eta=r_d/4\), (11) and F1–F2. The remaining majorant is
\[
 3e^{5\kappa/16}\widehat\omega_fe^{-11\kappa d_f/16}
 (3\vartheta e^{(\lambda_P+\lambda_T)c})^{|W|}q_s^{|V|}e^{-24m}.
\]
Here \(m_{X(f)}(W)\le2m\): take the metric closure through the root, double the spanning tree and shortcut to retained terminals. This closure has the original MST value, since shortcuts expand to walks through the already present root.

Split the last decay as \(e^{-12m}e^{-6m}e^{-6m}\). For the first factor contract \(W\) into the read root. DRL Lemma 5.1 sums the forests to \(\exp(2q_s\Xi)\): a nonroot contributes at most 2, a root contributes \(\Xi\), and \(n^{n-1}/n!\le e^{n-1}\) sums the exponent for \(q_s\le1/(4e)\). Equation (15) and (F4*) pay the read part. The \(W\)-part costs at most \(2^{|W|}e^{4q_s|W|}\le e^{|W|}\): \(r_d\ge96\) gives \(q_s\le1/16\), and \(e^{3/4}>2\) by its first three series terms.

Reserve \(\kappa d_f/8+6m\) for the gap (11), giving
\(\nu_g(G_i-C_{\rm pr}-2c-E_i)\).
The remaining \(\kappa d_f/2+6m\) sums to \(2N_{\rm ex}\) by (3), assigning a nearest read to a fixed gas cube. The factors give (13). RUN makes its gap exponential dominate every fixed polynomial, by \(e^x\ge x^n/n!\) for sufficiently large fixed \(n\).

Finally put \(Y^*_{f,V}=Y_{f,V}\cup V(U_{f,V})\). Every added cube is on the graph. Its tree lies in \(Y^*_{f,V}\), so (14) also bounds \(d_i^+(Y^*_{f,V})\), and (13) holds for these labelled filled carriers. Exact regrouping into slots, full-domain admission and covariance remain filing inputs. ∎

DRL Proposition 5.4's cluster argument remains conditional on the actual carriers and G-P. Write \(c_G^{\rm pair}\) for its Gaussian read radius, distinct from IN1's gain coefficient \(c_G\), and \(c_{\rm inc}\) for the incompatibility range. When \(G_i-w_i^*>c_G^{\rm pair}\), gas cubes lie outside every member, so their trees meet the gas supports. Incompatibility-tree joins and Gaussian-read stars have the stated bounded ambient cost; in-domain filing also needs contained paths or further filling. CI's absolute majorants and full local domains are still required. The smaller filing rate \(\lambda_P\) is not IN1's \(\kappa\) without a scale-filing comparison.

## 4. Order of constants

Retain every frozen IN1 floor, both windows in TD (32), and TD2's ordinary window. “Early” means before \(\kappa\), independently of \(M,\bar\kappa\). Derived bounds for members must not be used to select earlier constants through their actual \(\eta\)-dependent widths.

1. **IN1 rows 1–3:** fix \(C,c,C_{\rm pr}\) and the constants used in the \(L\)-floors uniformly in \(L\), then choose \(L\) by those floors. Fix \(C_{\rm tr},c_G^{\rm pair},c_{\rm inc}\), the remaining unit-conversion constants and the response/chart/admission base constants in their inherited order; form \(c_g^\sharp,C_4\) after \(L\). All precede \(\kappa\), independently of \(M,\bar\kappa\).
2. **Row 4:** choose \(\kappa\) by the retained floors and \(\kappa\ge2\log76800\). Choose TD2's \(\lambda_V\) so \(\lambda_T=\lambda_V+1\) satisfies \(\lambda_TC_{\rm pr}\le\kappa/4\). Set
   \[
    \lambda_P=\min\{\kappa/(16C_4),[4(2c_G^{\rm pair}+1)^4]^{-1}\},
    \qquad 0<\kappa_P\le\kappa/(2c_g^\sharp).
   \]
3. **Row 5:** choose \(\bar\kappa\) above the retained TD/TD2/response floors, \(\bar\kappa\ge8\kappa_PC\), and
   \[
   \begin{gathered}
    r_d\ge96,\qquad
    r_d/2\ge\lambda_P(81+c)+2\lambda_T(1+\eta_o),\\
    r_d\ge4\lambda_P\max\{16(C+1)^2L,4+2c\},\qquad\text{(F4*)}.
                                                               \tag{16}
   \end{gathered}
   \]
   Now determine \(\eta=4\lambda_P/r_d\). Choose the remaining response parameters and \(M\) in their existing order.
4. **Rows 6–8:** retain the late radii, amplitudes, \(\mathsf B\), then its volume cost \(c_{\mathsf B}\), and the corresponding \(c_1\)-floor. Recompute the carrier-count volume cost using (9), with actual multiplicities separately supplied. This is not a proof that its numerical value is unchanged.
5. **Row 9:** choose \(\gamma\) for (5), (10), \(L\check R_i/10\ge w_i^*+4\), \(G_i-w_i^*>c_G^{\rm pair}\), and all existing response, admission and amplitude ceilings. Retain DRL's TJ, \(\vartheta<2/3\), and \(\vartheta_P<1\). Explicitly, TJ is \(8\eta_1(e^{\bar\kappa}-1)^{15}\le1\), where \(\eta_1=\delta_{\rm src}/(3\delta_{\rm src}+c_Tge^{\bar\kappa}R)\) in TD's notation. Choose the final torus with Lift in row 10.

These numerical additions are acyclic. Indeed
\(\Psi_\eta=K_4\eta^{-4}\), where
\(K_4=\sup_{y\ge0}y^4(2y+9)^3e^{-12y}<\infty\).
Finiteness follows from the exponential series, for example its eighth term beyond \(y=1\). Thus \(q_s\Psi_\eta\le C_{\lambda_P}e^{-a}(a/2-6)^4\to0\); (F4*) is an eventual floor on \(\bar\kappa\). All other conditions in (16) are floors there. RUN makes the row-9 conditions uniform tail ceilings.

This corrects the draft's “only rows 5 and 9 change” claim: the explicit half-rate entropy floor belongs in **row 4**, F4 needs replacement for nonbox cores, and late volume constants are recomputed. There is also an unresolved geometric long-domain requirement below. Assigning that requirement to a row without proving its permitted dependence does not verify the full order.

## 5. What remains of class matching

**Lemma 9 (long-domain bound and its limitation).** If every member has diameter at most \(\Delta\), then, for \(p,q\in X\),
\[
 \delta_{\mathsf H}(X)\ge d(p,q)-2\Delta.                     \tag{17}
\]
Under (8), if \(j<k\), \(m=k-j\), and \(d(p,q)\ge b\check R_kL^m\), then
\[
 d_j^+(X)\ge
 [bL^m-4CL^{1+\lceil m/2\rceil}]\check R_k-10.               \tag{18}
\]

*Proof.* Each endpoint is either on the tree or within \(\Delta\) of a tree vertex in its chosen member. The path between those vertices costs at least \(d(p,q)-2\Delta\). Minimize. For (18), use \(\Delta\le2CL\check R_j+5\) and Drop. ∎

**Outstanding — exterior smallness.** This does not prove H-SF's exterior long-domain alternative. The bracket in (18) is positive by this method only when
\(b>4CL^{1-\lfloor m/2\rfloor}\); the worst case \(m=1\) requires \(b>4CL\), not the draft's \(b>4C\). A strict margin then permits a final radius floor to absorb 10. This is a sufficient condition for this estimate, not a necessary condition for the actual construction. SA 19499, 19519 states the long-domain mechanism but does not specify that \(b\) is a freely enlargeable constant in the required order. Supply the actual lower bound \(d_j^+(X)\ge c_{\rm LD}\check R_k\), with \(c_{\rm LD}>0\), or prove an admissible geometric enlargement rule. Calling this “only doubling \(C\)” does not supply it.

**Lemma 10 (the two fixed-family obstructions, with their correct scope).**
(a) Fixed collars need not supply a fresh margin beyond projected old carriers at a drop.
(b) Replacing hulls loses old scalar class bounds, whereas adjoining members preserves them.

*Proof of (a).* This is an explicit graph model, not a statement about every actual coefficient. Take a drop with \(\check R_{t+1}=n\), \(\check R_t=Ln\), where \(n\) ranges over large powers of \(L\). Use aligned boxes
\(H=[0,Ln-1]^4\), \(H'=[0,n-1]^4=\pi H\).
They can be one unchanged physical cell: CA-I's side \(M\check R_ju_j\) is the same at a drop. Place everything in a sufficiently large torus.

For the fixed rule, write
\[
 v=\lceil\eta(Ln+2c+4)\rceil+c+5,\quad
 u=\lceil v/L\rceil,\quad
 b'=\lceil\eta(n+2c+4)\rceil+c+4.
\]
The old member projects exactly to \(X'=N_uH'\), while the new base collar is \(N_{b'}H'\).
Since \(\eta(2c+4)\le1\),
\[
 \eta n\le u\le\eta n+(c+7)/L+1,\qquad
 u\le b',\qquad b'+1-u\le c+7.
\]
Thus a read set equal to \(X'\) has reads within \(c+7\) of the outside face of its next base. This is admissible carrier geometry; a function can depend on every coordinate there. It is not forced by the assertion that a function has that carrier.

The failure of the proposed numerical summation is also explicit. Take the \(n^3\) exterior face cubes with transverse indices in \([0,n-1]^3\), and one gas cube \(w\) at hub distance \(G_{t+1}\). Its distance to \(X'\) is at most \(10Ln\). For \(V=\{w\}\cup S\), with \(S\) any subset of that face, the rooted star gives
\(m_{X'}(\{w\}\cup V)\le10Ln+(c+7)|S|\).
Consequently the positive joint majorant contains
\[
 q_se^{-10r_dLn}(1+q_se^{-r_d(c+7)})^{n^3}\longrightarrow\infty.
\]
Its logarithm has a positive cubic term and a negative linear term. The proposed uniform bound from that majorant therefore fails, even without a carrier-length weight. This proves a route obstruction, not divergence of the actual pieces.

*Proof of (b).* Take one box hull \(H\) with at least two cubes and a proper member \(M\supsetneq H\), and put \(X=H\). The old family gives length zero. The replacement family cannot excuse \(M\), so a minimum covering tree has \(|H|-1\) edges. Thus an old bound \(\mathsf B\) does not imply \(\mathsf Be^{-\kappa d_{\rm rep}(H)}\). For a refiling obstruction take an \(n\)-box \(H\), and \(n^3\) adjacent face cubes \(z\). Distinct slots \(H\cup\{z\}\) have old length 1. Positive constant functions \(\mathsf Be^{-\kappa}\) meet those scalar bounds, but filing all at a member \(M\supset N_1H\) yields \(n^3\mathsf Be^{-\kappa}\), exceeding \(\mathsf B\) for large \(n\). This refutes refiling from scalar bounds alone, not the actual formation theorem. ∎

The draft's Proposition 7.1 is therefore **not correct as a universal statement**. It mistakes an upper carrier for mandatory reads, assumes the precise cell/unit matching, and infers growth of an individual hull from an upper bound and RUN. It also measures distance to a base which includes \(X_{f'}\), not just the new collar. A single attachment does not force the minimizing relative tree to pass through a previously selected \(T_{f'}\). Lemma 10 supplies the valid countermodel and avoids that extra inference. Its calculation also applies to any fixed multiple of the linear collar once its coefficients are fixed; it does not rule out every possible localization construction.

**Lemma 11 (core containment is not scale filing).** There is no uniform implication
\[
 d_j^+(X)=0\quad\Longrightarrow\quad d_{j+1}^+(\pi X)\le K
\]
from (1), G and Drop alone, for any fixed \(K\).

*Proof.* In Lemma 10's box model let \(X=M_t=N_vH\) at a predecessor-free birth. Its old length is zero. At the next step the recursive core contains \(X'=N_uH'\). The new recursive member strictly contains \(X'\), so is not eligible in \(X'\). The only eligible member is \(H'\). For large \(n\), \(u\ge1\), and \(X'\setminus H'\) contains a face with \(n^3\) cubes. Every relative tree must meet them, hence has at least \(n^3-1\) edges. This applies even to the ambient length. ∎

**Outstanding — scale/rate transfer.** A projected old member lies in the new core, but the new member need not lie in the projected carrier. Lemma 11 directly refutes the draft's claim that monotonicity makes this comparison no harder. Enlarging and regrouping carriers can address it only with actual multiplicity, rate, domain and covariance bounds.

The remaining matching conditions, each needed on the **enlarged input class**, are:

* **Match-SF/O:** H-SF and H-O, including formation and every boundary origin, hold with the new input norm and return \(d^+\) at rate \(\kappa\). Old output bounds imply new output bounds for the same input; they do not extend a theorem from the smaller old class to the larger new class.
* **Match-read/file:** complete read/stencil coverage (4), unit conversion, actual per-read multiplicities (3), admissible connected carriers and full local domains, exact covariant regrouping and the scale/rate comparison hold for the emitted terms. If a filled carrier is used, all these assertions refer to that carrier.
* **Match-heal/LD:** retired members lie inside the precise enlarged healed region; inside it the actual multilevel slot sum has its paid volume bound. Outside it the positive long-domain lower bound after (18) holds. SA's 8–10-cell preparation margins are not by themselves this statement for every later standing or swallowed island.
* **Match-history:** the recursive record is available to every permitted local history chart, including swallowed ancestry, and transports with it. Aligned coarsening commutes with partition-preserving charts; arbitrary unit-translation covariance and locality of a chosen minimizing tree do not follow from that fact.

These are explicit mathematical hypotheses, not new physical axioms. They are not discharged here.

**Proposition 12 (conditional IN1 transfer).** Suppose IN1's H-M, H-OL, H-LF, H-G, H-C, H-E and H-SUM retain their full scope, and the four matching conditions hold with H-SF/H-O on the enlarged class, the corrected order of §4, and torus-compatible companions. Then IN1 Theorems 10–12 apply to that class with fixed constants at every step.

*Proof.* At level zero there are no islands, so the class agrees with IN1's bare class. Its Lemma 5 gives the same regular-list bound. Match-SF/O supplies the next regular, remainder, boundary and oscillation clauses, including their domains and identifications. Match-read/file, Match-heal/LD and Match-history supply precisely their later uses and coherence. IN1 Theorem 10 uses the unchanged mass-envelope, geometry, certificate and measure hypotheses; it returns the mass clause with the recomputed late \(c_{\mathsf B}\) paid in \(c_1\). H-LF and H-SUM supply exactness, positivity and the floor. This is IN1 Theorem 11's proof. Its Theorem 12 then uses only that step, the one-loop interval information, scalar stopping argument and compatible torus choice. The next tube remains an assumption except on the run \(\theta=x\), exactly as in IN1. ∎

## 6. The seventeen uses

These are the draft's U1–U17, checked at the pinned checkout. A pointwise comparison is not a formation theorem.

| Use | Conclusion of the check |
|---|---|
| U1 — IN1 definition, line 44 | D1–D3 supply the family, units and frozen record. Distinguish ambient from in-domain length. |
| U2 — H-SF (12), class clause | Lemma 2 transfers an old bound on the same slot. Match-SF/O is Outstanding for new-class inputs and the new origin. |
| U3 — vanishing differences, IN1 136; SA 19517–19518 | A difference on the same admitted carrier preserves its length weight; the small factor remains H-SF's input. Later refiling needs Match-read/file. |
| U4 — long-domain decay, SA 19499, 19519 | Lemma 9 proves the endpoint inequality. Its application and the allowed order of the span constant remain Outstanding. |
| U5 — interior volume cost, IN1 233, 417 | Lemma 6 proves the single-level carrier count. Actual multilevel multiplicities and healed-member containment remain Match-heal/LD; recompute the late cost. |
| U6 — H-O (18) | Pointwise monotonicity holds. Creation of operations from the enlarged class requires Match-SF/O; mass does not supply oscillation. |
| U7 — row-2 geometry | \(C,c,C_{\rm pr}\) remain early. Use \(2C\) only in the proved member bounds; recompute derived AG geometry and keep Lift explicit. |
| U8 — IN1 Amendment 1 | Retain both natural and original window floors, including TD (32)'s interpretation of the \(\kappa\)-floor. Their algebra alone does not supply a changed geometric premise. |
| U9 — TD X, per-read sums | Lemma 6 handles already supplied terms. New-slot multiplicities, amplitudes and complex island deficits remain (3). |
| U10 — TD/TD2 G | Lemma 4 gives the weakened member separation and gas gap, while original hubs keep G. “Only double \(C\)” does not preserve the original numerical gap/separation for members. No live-set-to-hub gap is supplied. |
| U11 — G-ord and X° | \(\eta_o\) stays unchanged. Lemma 5 supplies projected member containment only; complete reads and unit conversion remain required. |
| U12 — TD2 Lemmas 1–2, Theorem 3 | Lemma 7 proves the modified inequalities, adds (10), and replaces the gap by \(G_i-C_{\rm pr}-2c-E_i\). |
| U13 — contracted TD-natural | Its original hub-contracted premise (8) is not implied by (4) for enlarged reads. Contracting the new members changes that graph and its entropy estimates. This extension is Outstanding; ordinary TD does not use it. |
| U14 — CI classification and filing | A carrier contains a new member only if it contains an old hull, and old hulls remain eligible: the exempt/nonexempt classification is unchanged. If it contains no hull, both lengths are ordinary. Scale filing is not monotone across levels: Lemma 11. |
| U15 — AG1 Lemma 2, L-B/N-B | Lemma 7 verifies the geometry with the supplied complete read hull. The \(\bar\kappa\)-floor is sufficient; N-B and the actual analytic amplitudes are still imports. |
| U16 — DRL Theorem 3 and cluster filing | Lemma 8 repairs the nonbox shell count with F4*. It proves the ambient bound and geometric filled-carrier bound. G-P, full local domains, covariance, actual regrouping and scale/rate transfer remain required. |
| U17 — persistence, SA 19523 | Lemma 3 proves bounded recursive width; (1) proves containment. Carried functions, domains and formation-time lengths stay frozen. Neither this nor the source proves every new read or filing assertion. |

The corrections proposed for other notes therefore have the following scope. **TD2:** replacing X° by (4), adding (10), and changing its gap are valid conditional changes; declaring read-collar coverage discharged is not. **DRL:** its per-step shrinkage sketch does not justify iteration; Lemma 10 supplies the fixed-collar route obstruction, and Lemma 3 proves the recursive repair. Its Theorem 3 additionally needs F4* or a proved box-shell property. **AG1:** the geometric correction is valid with its read-hull and N-B imports and the corrected radius threshold. **IN1:** the norm enlargement is pointwise safe; claiming full class preservation from that fact is not. **TD-natural:** being off the ordinary route does not prove its changed hypotheses.

P82's frozen real-reference inverse is not a response on all switched complex pairs. TP1 has no direct use of this excused family, but its AG import retains its qualifications. ST1-r2 Theorem 14, ST1-draft3 §6 and the later ST1-r4 interface require actual activity bounds on the entire chain domain. Changing a carrier does not supply them. ST1's permanent mark ledger is distinct from the recursive member record.

## 7. Source checks

The outline was located through sa-index/README.md, neighbouring rows in chunks 05, 16, 17, and obligations.md. CA-I was located through ca-4.12-4.19/README.md and neighbouring rows in chunks 06, 09, 10. Each of the five requested raw files was fetched once; only bounded source excerpts were read. All source line claims in cls-draft.md were checked directly. Its direct upstream citations are to SA; the additional CA/YM3 checks below resolve conventions and retain the cited consumer qualifications.

The common source revision is [31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/31a47c543775). Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. Their large-field construction follows Tadeusz Balaban; Jonathan Dimock's expositions are credited in the input notes. No additional Balaban or Dimock theorem is imported here from memory.

| Source and lines read | What the passage supports |
|---|---|
| SA 5586–5597, 5863–5872, 6183–6209 | Named partitions, hulls, connected domains, in-domain ordinary trees, retained slot domains, selectable exempt members and R23. These are definitions and requirements; no free crossing or automatic class transfer. |
| SA 6020–6036, 17315–17335 | Running-minimum radii, free evolution, cell hulls, nesting and the stated no-consecutive-drop rule. The latter has a short flow/small-coupling explanation, not a proof of recursive collar bounds. |
| SA 17415–17434 | The three fates and retirement by swallowing. This supports recording successors; it does not specify every complete read map. |
| SA 17558–17584 | Kept-form oscillation and stage differences; small quiet quarantined components and their nested 8–10-cell boxes. These are sketched formation claims for those components, not a shell theorem for recursive unions. Nonwrapping uses admissible torus room. |
| SA 19408–19425, 19435–19485 | Presentation class, coherence, class-step statement, ordered constants and uniform tail ceilings. The class step is a conditional/sketched construction; the order does not identify the long-domain span coefficient as free upward. |
| SA 19495–19523 | Difference, exterior-decay and interior-volume mechanisms, and unchanged creation bounds. The mechanisms are stated/sketched; later-domain admission remains a prerequisite. |
| CA-I 49495–49546, 54986–55005 | Gauge/domain supply and the stage theorem remain application hypotheses. These passages do not discharge Match-read/file. |
| CA-I 53633–53697, 53737–53764 | Cell side \(M R_i u_i\), compatible partitions and hulls, with cell-parameter properties imported; prepared sequences refer to one component. This fixes the draft's two cube conventions. |
| CA-II 16013–16045; CA-III 3510–3530, 12276–12292 | Relative-domain lengths retain in-domain trees and analytic-domain hypotheses. They support charged crossings, not identification of all their conventions with SA's family definition. |
| YM3-I 49131–49168, 52582–52589 | The component argument uses supported walk hulls and local nonlinear maps; switch products attach to individual hulls. These support the cited method, not a four-dimensional response or full read dependence. |

The local checks include the entire cls-draft.md; IN1's definitions, imports, order, Lemma 5, Theorems 10–12 and Amendment 1; TD's R/A/X/G, natural construction and literal-length correction; TD2's ordinary proof, filing hypotheses and corrections; DRL's joint coefficients, Theorem 3 and its consumer clauses; CI's carrier and filing interface; and AG1's L-B/N-B and Lemma 2. The relevant context and limitations in ym4-assembly.md, p82.md, tp1.md, st1-r2.md, st1-draft3.md and st1-r4.md were read. The cited in1-gate, ag1-gate, h-walk-gate, loc-3-check and d3-local-check passages preserve conditional scope. In particular loc-3-check separates component locality from admitted evaluation; h-walk-gate separates field locality from region-trace locality. None supplies the new matching conditions. This is not a rerefereeing of those unchanged dependency chains.

## 8. Amendment 2: exact proposed changes to in1.md

**Not applied.** The following is a conditional amendment, with stronger matching hypotheses exposed. The pass-1 amendment asserting unchanged imports and changes only to rows 5 and 9 is not justified. Locations refer to the pinned file; quoted blocks are the exact new text.

**A1 — length definition.** Replace the sentence “The supplied boundary hull length is \(d_j^\natural(\mathcal S;X)\).” in “Domains, norms and coefficients” by:

> The boundary length is \(d_j^+(\mathcal S;X)=d_{\mathsf H_j^+}(X)\), in the supplied cube convention of cls.md, D1, including its unit/rate-conversion hypothesis. Here \(\mathsf H_j^+=\{H_j(\alpha),M_j(\alpha):\alpha\text{ standing}\}\). Chosen members must be contained in \(X\); the tree lies in \(X\), meets each chosen member and every unexcused cube, and pays all crossings. Define \(U_j=N_2H_j\), \(R_j(\beta)=N_cU_j(\beta)\cup\bigcup_{\alpha\mapsto\beta}\pi_{j-1}M_{j-1}(\alpha)\), \(\rho_j=\lceil\eta s(R_j)\rceil\), and \(M_j=N_{\rho_j+3}R_j\), as in cls.md, D2–D3. The union includes every predecessor, also at the birth of a swallowing island; it is empty only at a predecessor-free birth. The formation-time family, function, length and analytic domain are stored together. Later projection does not redefine an old slot's length.

**A2 — the two norms and the class record.** In (12), replace only \(d_{k+1}^\natural(\mathcal S;X)\) by \(d_{k+1}^+(\mathcal S;X)\). In (18), replace only \(d_i^\natural(\mathcal S;R)\) by \(d_i^+(\mathcal S;R)\). In the paragraph “The class \(\mathfrak L_k(\theta)\)”, immediately after the sentence ending “with their specified domains, kernels and normalization factors.”, insert:

> Boundary slots and kept forms include the formation-time excused-family records specified above; the bounds (12) and (18) use those records.

**A3 — scope of the producer hypotheses.** Immediately before “**H-SF (small-field formation, NL1/ST1/OL1/SC1).**”, insert:

> **Amendment 2 matching hypotheses.** H-SF and H-O are required on every prefix of the enlarged class, not only on inputs satisfying the old boundary norm. Import cls.md §5's Match-SF/O, Match-read/file, Match-heal/LD and Match-history, with their stated uniformity and constant order. In particular these require the complete reads and actual multiplicities, full declared domains, exact covariant regrouping, conversion to the class rate \(\kappa\), the exterior long-domain bound and interior healed-region volume bound for the new members. These matches are Outstanding. Pointwise monotonicity of the two lengths proves none of their new-input or cross-scale assertions.

**A4 — geometry.** Immediately before “**Outstanding — actual genealogy.**”, insert:

> **Amendment 2 geometry.** Require cls.md D2's G, Drop, Mon and Lift at every relevant level, with the recursive family of D3 and the ordered conditions in its §4. In the notation there, cls.md Lemmas 3–4 give \(e_j\le(29/25)\eta(CL\check R_j+6+2c)+33/25\), \(M_j\subset N_{w_j^*}H_j\), \(w_j^*=\check R_j/[6(C+1)]+c+12\), and \(s(M_j)\le2CL\check R_j+6\). Members of different islands have distance at least \(\check R_j/2\); members of the same island are nested. Gas-to-member distance is at least \(10L\check R_j-2-w_j^*\), and \(\pi_jM_j(\alpha)\subset R_{j+1}(\beta)\) for a standing successor. Lift is required for the enlarged boxes. No live-set-to-member gap is asserted. These conditions supplement H-G; they do not prove its genealogy or coding hypotheses.

**A5 — constant-order table.** Append the following exact text to the choice cell of each named row, leaving its existing text and the internal order of other packages in place:

| Row | Text to append |
|---|---|
| 2 | Amendment 2: include \(C=C_{\rm isl}\), \(c=c_{\rm col}\), \(C_{\rm pr},C_{\rm tr},c_G^{\rm pair},c_{\rm inc}\) and the unit-conversion constants of cls.md. Fix \(C,c,C_{\rm pr}\) and the constants used to choose \(L\) uniformly in \(L\); also require odd \(L\ge27\). Choose the remaining early constants in their inherited dependency order and form \(C_4,c_g^\sharp\) after \(L\), as in cls.md §4. All precede \(\kappa\), independently of \(M,\bar\kappa\); \(c_G^{\rm pair}\) is the Gaussian read radius, not the gain coefficient \(c_G\) in row 7. |
| 4 | Amendment 2: in choosing \(\kappa\), also require \(\kappa\ge2\log76800\) and retain TD2 (13)'s ordinary window together with TD (32)'s two windows. After \(\kappa\), before \(\bar\kappa\), choose \(\lambda_V,\lambda_T=\lambda_V+1,\lambda_P,\kappa_P\) exactly as in cls.md §4. |
| 5 | Amendment 2: also impose cls.md (16), its F4*, and \(\bar\kappa\ge8\kappa_PC\). Determine \(a,r_d,q_s,\eta=4\lambda_P/r_d\) as in cls.md Lemma 8. These are floors on \(\bar\kappa\) in preceding constants; no earlier constant reads the resulting widths. Keep the remaining response choices and \(M\) afterwards. |
| 7 | Amendment 2: after \(\mathsf B\), recompute \(c_{\mathsf B}\) using cls.md (9) and the actual multilevel multiplicities and healed-region bound required by Match-heal/LD. Pay that value in the displayed \(c_1\)-floor. No universal factor of 40 or unchanged numerical volume cost is assumed. |
| 9 | Amendment 2: also meet cls.md (5), (10), \(L\check R_i/10\ge w_i^*+4\), \(G_i-w_i^*>c_G^{\rm pair}\), TJ, \(\vartheta<2/3\) and \(\vartheta_P<1\), uniformly over running levels, together with all retained response, admission and amplitude ceilings. These are coupling ceilings in the preceding constants. |
| 10 | Amendment 2: the admissible torus/grid must satisfy Lift for the enlarged members, their constructed carriers and complete read margins. |

The referenced equations specify every added numerical condition. In particular F4* replaces, rather than silently retaining, DRL's box-shell F4. The long-domain import has no newly certified placement: the failed deduction of its span constant from “double \(C\)” cannot be turned into an order assertion.

**A6 — amendment record.** Insert the following section after Amendment 1 and immediately before the final “## Result”:

> ## Amendment 2 (proposed; Codex, 2026-11-05)
>
> Source: cls.md, Pass 2, not yet refereed. The excused family adjoins recursive collared hubs to the standing-island hulls and retains formation-time records. Its no-accumulation estimate, ordinary-decay modification and ambient filing bound are hand implications under the named geometry and analytic imports. The corrected numerical conditions fit the order as stated in cls.md §4.
>
> Theorems 10–12 transfer only under cls.md Proposition 12's matching hypotheses on the enlarged class, which remain Outstanding. In particular projected-core containment is not scale/rate filing, and a weaker output norm does not extend a producer theorem to new inputs. This proposal does not establish the unchanged-import version of (Cls+), supply the long-domain geometric match, or change any scientific or referee status. Amendment 1 and both of its rate windows remain in force.

## 9. Definitions supplied

The definitions needed beyond the cited producer statements are:

1. The named cube graph, nonwrapping lift convention, \(N_u,s,\pi_j\); the separate ambient and in-domain family lengths \(\delta_{\mathsf F_0},d_{\mathsf F_0}\), including eligibility, paid crossings, infinity and the graph meaning of “old”.
2. The all-predecessor successor record; \(U_j,R_j,\rho_j,\widehat R_j,M_j,\mathsf H_j^+\); and the frozen formation-time record, distinct from projected reads and later filing.
3. The comparison quantities \(D_j,G_j,A_j,e_j,E_j,w_j^*,D_j^*\) and thresholds \(\eta_\sharp,R_\sharp\). These are bounds, not substitutes for actual hulls or for Lift.
4. The explicit distinction between reads \(X(f)\), presentation \(X_f\), and ordinary tree \(T_f\); \(\operatorname{St}\) and the read-rooted \(m_A\); the filing base \(N_f\), carrier \(Y_{f,V}\), constructed graph \(U_{f,V}\) and filled carrier \(Y^*_{f,V}\).
5. The renamed Gaussian radius \(c_G^{\rm pair}\); \(c_g^\sharp,C_4,\lambda_P,\kappa_P,\eta_o,a_1,\nu,\vartheta_T,r_d,q_s,\Psi_\eta,K_4,\nu_g,\vartheta_P,A_P\), with their displayed choices. The source variable \(a\) and \(\vartheta\) retain TD2's definitions.
6. Match-SF/O, Match-read/file, Match-heal/LD and Match-history, stating exactly what a full class-transfer theorem still requires.

## Result

The hand proofs establish bounded recursive core width through arbitrary finite ages and swallowings; separated enlarged members; same-level norm monotonicity and carrier entropy; conditional ordinary TD and AG1 geometry; and a corrected read-rooted filing bound in ambient length, with an in-domain bound for filled carriers. Proposition 12 is a conditional transfer of IN1, **not a proof of (Cls+) from unchanged imports**.

Imports are D2's actual geometry, scale conversion and lifts; D4's response, admission, complete reads, complex island deficit, per-read sums, joint coefficients and pair-locality; and, for the full induction, IN1's H-M, H-OL, H-LF, H-G, H-C, H-E and H-SUM, H-SF/H-O on the enlarged class, CI's Gaussian/formation packages, AG1's N-B and all four Outstanding matching conditions. Their ordered uniformity is part of the hypotheses.

Corrections to Pass 1, including its proposed changes to other notes:

* Separated ambient from in-domain trees and graph units from continuum normalization; retained rate conversion as an import.
* Included swallowed predecessors at a new island's birth; proved the exact rational width bound; required enlarged lifts and local ancestry data. Separation applies to different islands, and G supplies no live-set-to-hub/member gap.
* Restricted projection to the cubes it actually controls. Upper carriers do not force full read dependence; complete stencils, pins and later admission remain required.
* Replaced the invalid bounding-box shell count for recursive unions by (15) and F4*, whose cost grows as \(\eta^{-4}\).
* Gave explicit single-level entropy constants, corrected the half-rate floor to \(2\log76800\), withdrew the universal factor 40, and retained actual multilevel counts and a recomputed late volume cost.
* Verified the ordinary connector inequality with the unchanged \(\eta_o\), added (10) and the core-width gap loss; corrected AG1's radius threshold and retained its read-hull/N-B inputs.
* Restored the missing \(L\) in the sufficient long-domain condition, \(b>4CL\) in the worst case, and left its construction and placement Outstanding.
* Replaced Proposition 7.1's universal assertion by an explicit fixed-collar route countermodel. Its divergent positive majorant is not divergence of actual coefficients, and RUN does not force a lower bound on each hull's size.
* Replaced the draft's incorrect replacement-family excess formula by the \(X=H\) example and proved a scalar refiling countermodel without claiming that actual formation realizes it.
* Exhibited the failure of cross-scale length transfer even for recursive members; distinguished slotwise weakening from formation on the larger class, and kept connected carriers, domains, multiplicity, covariance and scale/rate filing explicit.
* Limited covariance to the charts actually preserving the partition/ancestry; kept TD-natural's changed contraction premise Outstanding. P82, TP1 and ST1 do not remove the analytic formation qualifications.
* Replaced the claimed rows-5-and-9-only amendment by the exact conditional edits above, retaining Amendment 1. The numerical additions are acyclic; the unresolved long-domain and class matches are not thereby proved.

Only cls.md is changed. All arguments are by hand; retrieval and file bookkeeping discharge no mathematical step. This research text grants no status and is **not yet refereed**.
