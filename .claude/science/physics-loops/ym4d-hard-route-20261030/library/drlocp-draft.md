# DRLOCP: pair-locality of the decoupled response, the joint composition, and the P-labelled gas — pass 1 (long draft)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, one session, working in a clone of the planning folder. Pass 1 of the two statements that now stand at the front of CI (ST1's consumer interface, with NL1/LF1) in our proof of T0. Research text. It is not an audit and grants no status. No other model has read it. Method: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen. Read before finishing: Codex's distil `td2.md` (Result and Corrections 9–10), which arrived during this session; §4.5 and §5 answer its Correction 10.

No step rests on a computation. Every argument is a finite sum, a finite Möbius inversion, Banach's fixed-point theorem with its uniqueness clause, a Cauchy estimate on a polydisc, the one-variable Schwarz lemma, a tree or forest count (Cayley's formula and the exponential formula for labelled forests), or a comparison of explicit numbers. Each is meant to be Lean-formalisable.

Credit. The decoupled response (R9), its walk-parameter mechanism, the splitting over wall-components, the relative length, the class rule and the switch interpolation are the work of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the outline `ym4.tex` ("SA") and the three-dimensional manuscript `YM3_I.tex` ("Y3"), revision `31a47c543775`. The component argument of §2 is the four-dimensional form of Y3 Proposition I-91-59 (Y3 49131–49168) and of our `loc-3.md` Lemma C. The random-walk expansion with local inverses on cut-down sequences is Tadeusz Balaban's (CMP 89, 95, 96, 99, 116); Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable versions. Bird's allocation (TD Lemma 1) is J. C. Bird's. Library notes keep their authors: `h-walk.md`, `o1-decoupled.md`, `loc-3.md`, `p81-crit-draft.md`, `td2-draft.md` (Claude); `td.md`, `td2.md`, `dec-field.md`, `d3-local.md`, `nl-r9.md` (Codex).

Line references. SA L = `scratchpad/sa/ym4.tex`; Y3 L = `scratchpad/sa/YM3_I.tex`. Library notes by short name: TD = `td.md`; TD2d = `td2-draft.md`; TD2 = `td2.md`; CI = `ci-form.md`; NL1-L, IN1, ST1 = frozen `nl1-L.md`, `in1.md`, `st1-r3.md`; HW = `h-walk.md`; HWF = `h-walk-fix.md`; HWG = `gates/h-walk-gate.md`; O1D = `o1-decoupled.md`; L3 = `loc-3.md`; L3C = `gates/loc-3-check.md`; D3L = `d3-local.md`; NR9 = `nl-r9.md`; DF = `dec-field.md`; CRIT = `p81-crit-draft.md`. I quote the line before I say what a source states. "States" means that the text at those lines says so; it does not mean that the source proves it.

Status words: **[P]** proved here, not checked; **[I]** import, with owner; **[R]** reading of a source, flagged; **[O]** Outstanding; **[CE]** counterexample to an implication; **[design]** a choice we are free to make.

---

## 0. Result

**Task 1 — (DR-locP) is proved** [P, as an implication] for the decoupled response that our library specifies: Definition D walk operators (O1D 105–114), the reduced nonlinear map (4.4) of NR9 (NR9 229), the multiplier current (3) of D3L (D3L 75), and the unique small fixed point of (R9) (DF Proposition 5.1; ST1 137, OPS/SLICE/UNQ). The collar is **\(c_P=0\)**: on every face-component \(K'\) of \(\operatorname{supp}s\), at every complex switch \(|s_c|<e^{\bar\kappa}\) and every source in the source ball, the response pair \((\mathbf H,\mathsf j)\) on the bonds of \(K'\) is a function of \(s|_{K'}\), the source rows of \(K'\) and \(P|_{\bigcup K'}\) only (Theorem 1). With the completed source \(S(v_0+u(s\odot\zeta))\), whose rows read the pair on their first neighbour layer, the collar is \(1\) (Corollary 1′). The local functions are holomorphic on the image of the restriction map and agree under restriction (Theorem 1(iii)).

The proof is a uniqueness transfer (Lemma 2.3) for a fixed point whose map is *tame*: every decoupled operator vanishes unless both its arguments lie deep inside one wall-component, and the local maps between consecutive decoupled operators have reach far below that depth (Lemmas 2.1–2.2, 3.1). This is SA's own mechanism: "The same contraction, by uniqueness, gives consistency and splitting over the wall-components" (SA 10400–10401), applied with two pairs instead of two switch vectors.

*What the decay rate does.* The decay of the walk coefficients against the switch radius \(e^{\bar\kappa}\) does **not** set the collar. It sets the convergence floor \(\ell_{\mathsf P}\ge\max\{8r_1+1,256\bar\kappa/\tau_L\}\) on the parameter-cube side (O1D Theorem B), that is ST1 row 8's \(M\ge C_{\rm dec}\bar\kappa\). Exact pair-locality comes from the walk supports. Proposition 3.2 shows it cannot come from bounds: a path-weighted global inverse (IN1 Lemma 2's construction) satisfies every clause of TD's R, with exponential decay, and violates (DR-locP) for every collar width. So (DR-locP) is a property of the walk specification, not of R.

*Constants.* \(c_P=0\) (or \(1\) with sources) is a pure number. The depth radius \(\rho_{\mathbf B}=3LM_1\) and the reach budget \(80r_0\le\rho_{\mathbf B}\) are row-2/3 constants (functions of \(L\), \(M_1\)), fixed before \(\kappa\), independent of \(M\) and \(\bar\kappa\). Nothing in Theorem 1 reads \(\kappa,\bar\kappa,M\).

*Imports of Theorem 1* (all already on the DR lane): (UNQ) the unique small (R9) fixed point on the switched polydisc, in sup-type weighted norms (DF Proposition 5.1 from [PW], [NL]; L3's (D1)); (D2) the read hulls of the walk terms (HW Theorem W(c) field part, kept by HWG 100; HWF 30, 116); the specifications (4.4) and (3), which NR9 61 calls [RED]. The extension of the local functions from the image of restriction to the *whole* declared local domain needs (UNQ-loc), the same fixed point on that domain. Source completion, pins and stored variables keep their own locality imports (S-loc), as TD2 300 requires.

**Task 2 — (JC).** TD2d's displayed (JC) (TD2d 405–408), with both the rate \(a-12\) and the factor \((C/D)^{|V|/2}\), is **not** proved here, and TD2 333–341 shows that its summation with the collapsed collar fails anyway. What is proved [P from R, A, (5)] is a stronger family (Theorem 2, (JC\(_\tau\))): for every \(\tau\in[5,2a-24]\),
\[
 |f_{W,V}(P;\zeta)|\le\omega^{N}_f\prod_{c\in W}\frac{2\beta_c(\zeta)}{\delta_J}\;\big(48e^{1-\tau}\big)^{|V|}\;e^{-(a-6-\tau/2)\,m_{X(f)}(W\cup V)},\qquad \delta_J=(24e)^{-1},
\]
with decay measured from the **read cubes** \(X(f)\), not from the collar. Here \(N\supset X_f\) is any base on which the switches are held at one, \(V\cap N=\varnothing\), and \(\omega_f^N\le3\widetilde\omega_f\). With \(\tau=12\) the rate is TD2d's \(a-12\); with \(\tau=a\) the switch factor is TD2d's \((C_*/D)^{|V|/2}\) and the rate is \(a/2-6\). The proof is a joint switch–fluctuation expansion that holds only the read stencils at one (Lemma 4.1) and a two-label form of TD Lemma 3 (Lemma 4.2). It needs no switched-polydisc amplitude and no connectivity of \(X_f\) (TD2 Correction 9).

**(5-sw) is not needed.** What Attack 3 used of it is (5) at one collared corner. Lemma 4.3 proves that from TD's (5) at \(s=1\), with \(B_f\) replaced by \(3B_f\), under one coupling ceiling.

**Task 3 — what remains of CI.** Proved here, as implications:

1. The exact decomposition \(f_W=\sum_Vf_{W,V}\) with pair-carriers \(Y_{f,V}\subset N_1(N_f\cup V)\) (Proposition 5.1′).
2. **A summation that keeps the collar-width decay** (Lemma 5.1, Theorem 3). It answers TD2 Correction 10. The root weight of every attachment is its distance to the reads, so each attachment cluster beyond a collar of width \(\rho\) pays \(e^{-s(\rho+1)}\) *once*, and the per-switch factor pays its internal cubes. TD2 (26) is the same sum with the root collapsed to the collar; it is unbounded, as TD2 shows, and is not used.
3. The filing bound (File-P°) (Theorem 3): \(\sum_f\sum_V\sup|f_{W,V}|e^{\lambda_P\ell^{\rm rel}(Y_{f,V})}\le a_Pe^{-\lambda_Td_f(W)}\), \(a_P\to0\), with SA's **literal** relative length (crossings charged), provided the excused members are the collared hubs \(\widehat H^+=N_{\rho+3}(\widetilde H^+)\) with a collar \(\rho=\lceil\eta s_H\rceil\) proportional to the hub side, \(\eta=4\lambda_P/(a/2-6)\).
4. Pair-carriers of class terms (H-C pieces) from Theorem 1 (Proposition 5.3), and the P-labelled cluster expansion given H-S's pair-heredity of the Gaussian (Proposition 5.4).

**The first remaining Outstanding statement of CI** is the class matching

> **(Cls)** [O, owner IN1/LF1]. IN1's class \(\mathfrak L_k(\theta)\), with the boundary bound (12) \(|B(X)|\le\mathsf Be^{-\kappa d^\natural(\mathcal S;X)}\) taken with the excused family \(\mathsf H_i=\{\widehat H_i^+(X)\}\) of collared hubs (SA 6191–6197 with this \(\mathsf H\), literal reading) in place of the level-\(j\) hulls of SA 6196, satisfies IN1's induction (its rows, (12), the per-cube sums (6) of TD's X, and formation), and TD's hub geometry G holds with \(\widehat H^+\) in place of \(\widetilde H\).

Three attacks on deriving (Cls) from SA's own family are recorded in §6.2 with the exact reason each fails: SA's hulls have no margin around the reads; a logarithmic collar does not pay literal crossings; SA's ten-cell box (SA 17579) puts its margin inside the island, not outside its reads. The remaining imports of CI that this note does not touch are listed in §6.1.

**Line count**: reported in the session reply.

---

## 1. Sources, quoted

### 1.1 SA: the decoupled response

- *The input* (SA 5762–5770). "A decoupled response input on a cubical region \(Y\) is a pair of maps \(\mathfrak h_Y(s;P,B')=(\mathbf H,\mathsf j)\), holomorphic in complex cube parameters \(|s(\Delta)|<e^{\bar\kappa}\), the complex triple variables, and the datum \(B'\)." Its first component "is the solution of the actual background equations with the propagators decoupled by these parameters" (SA 5766–5767), the system (R9).
- *Specified data* (SA 5782–5785): the operators are "specified linear maps between the finite-dimensional bond and constraint spaces, and specified holomorphic maps \(C_k,\mathsf W_s\) … They include their walk coefficients and convergence domains."
- *Splitting* (SA 5794–5797): "A wall-component is a component of cubes sharing three-dimensional faces. When \(s\) vanishes on separating cubes, the equations split over the remaining components, and the response on a component with no datum is zero." SA 5802: "Existence, uniqueness and these properties of (R9) are substantive response inputs."
- *Walk operators and contraction* (SA 10356–10402). "The decoupled response is formed from the operators of the walk expansions" (SA 10356–10357). "At arbitrary \(s\) it is this expression that defines the map; identities between the undecoupled operators are not imposed on their decoupled sums" (SA 10370–10372). The norms are weighted suprema \(\|A\|_\varpi=\sup_y\varpi(y)\max\{\xi_y|A|,\xi_y^2|\nabla_{\mathbf U}A|\}\) (SA 10373–10382). "Each decoupled operator has norm at most \(\widehat b=Ce^{16\bar\kappa}\)" (SA 10383–10384). The solution "is holomorphic in the parameters, the datum, the complex potential and the independent current" (SA 10393–10394). "The same contraction, by uniqueness, gives consistency and splitting over the wall-components" (SA 10400–10401).
- *Walk parameters* (SA 17904–17906): "Each walk in the response carries a parameter \(s(\Delta)\), \(|s(\Delta)|<e^{\bar\kappa}\), for every cube it visits. Setting a parameter to zero prevents a walk from crossing that cube." SA 17907–17920 then forms the switch interpolation and its brackets.
- *Relative length* (SA 6191–6197): "the tree meets each cube outside \(\bigcup\mathsf F\) and each member of \(\mathsf F\), but need not fill those members. For a label use the level-\(j\) hulls of its standing islands as \(\mathsf H\)." The class bound is (R23) (SA 6200–6205).
- *Class rule and boxes* (SA 17575–17583): \(H_i\) is "the hull, in level-\(i\) cells, of \(X\cap Z_{i-1}\)", and \(\Omega_i^c\cap X=H_i^{[8]}\), \(Z_i\cap X=H_i^{[10]}\).

SA does not prove the splitting or any pair-locality: SA 5802 lists them as inputs, and SA 10400–10401 is a one-sentence sketch.

### 1.2 Y3

Y3 49131–49168 (Proposition I-91-59, the component argument): "Each partial walk sum is carried strictly inside its wall component, with four \(N_L\)-neighbourhoods still inside that component" (Y3 49134–49136); "Every partition cube containing a point of the hull is included in its parameter set, so the hull lies in the interior of their union" (Y3 49154–49156); "The local nonlinear maps consequently agree with the component maps near each carrier" (Y3 49159–49160). This is the three-dimensional form of the depth-and-reach argument of §2.

### 1.3 Our notes

- *ST1.* DR is an import: "An actual regional response \((H,K)\), holomorphic in its complex input pair, datum and \(|s_\Delta|<e^{\bar\kappa}\), is given, with reality, covariance, restriction consistency, common-lift transport and splitting over face-connected components" (ST1 138). OPS/SLICE/UNQ: "The straightening and response fixed points have unique small solutions, uniformly on their stated balls" (ST1 137). ST1 Lemma 6 (CRIT) gives the specification at \(s=1\) and says: "These finite formulas specify what DR must resum to. They do not prove the weighted estimates for a decoupling of them" (ST1 471). ST1 is reopened only at the comb-representative uses (Amendment CV, ST1 1114); none of them is read here.
- *NL1-L H-DR* (NL1-L 159–171): the component reads hold "only on \(s|_{K'}\) and the source rows assigned to \(K'\), at fixed \(P\)" (NL1-L 168–169).
- *TD's R* (TD 25–33): the abstract response import, with component reads at fixed pair (TD 32) and source rows reading "only its cube and its first graph-neighbour layer" (TD 33). TD Lemmas 1–4 (TD 94–172) are used verbatim.
- *HW Theorem W* (HW 252–283): \(K^{-1}=\sum_\omega T_\omega\) over walks of cells \(X_\kappa=\kappa^{(3)}\); "(c) \(T_\omega\) depends on \((P,J)\) and on the data entering \(j\) only through their values on the hull \([\![\omega]\!]:=\bigcup_i\kappa_i^{(4)}\), enlarged by the read range of \(j\)" (HW 264). The gate found the region-trace part of (c) wrong (HWG 100) and kept the field part: "For fixed regions, the cutoffs are fixed scalar numbers: this failure does not introduce additional field reads or spoil holomorphy in the fields" (HWG 100). HWG 136 bounds the field read set of tree walks: "Joining through c bounds the entire additional field read set by \(O_L(M_1)\) from that cell." HWF 30: "The field-locality and field-holomorphy part of W(c) … passed the gate."
- *O1D Definition D and Theorem B* (O1D 105–156). \(\kappa^\sharp\) is the concentric cube of side \(8L^2M_1\xi_\kappa\), \([\![\omega]\!]^+=\bigcup_i\kappa_i^\sharp\), \(\mathsf P(\omega)=\{\Delta:\Delta\cap[\![\omega]\!]^+\neq\varnothing\}\), \(s^\omega=\prod_{\Delta\in\mathsf P(\omega)}s_\Delta\) (O1D 105–112). "\(H_1(s)\), \(\mathfrak G(s)\) and the walk data in \(\mathsf W_s\) are defined the same way from their own expansions" (O1D 114). Lemma WC (O1D 129–131): all cubes meeting a connected set whose cubes avoid \(\mathcal N\) lie in one wall-component. Theorem B(d) (O1D 140): "Each block of \(H(s)\) on a wall-component \(\mathcal W\) depends on the pair only through its values on \(\bigcup\mathcal W\)."
- *L3 Lemma C* (L3 147–157), checked "ADVANCE, conditional" by Codex (L3C §4): at Boolean \(s=\mathbf1_{\mathcal K}\), "on \(\operatorname{int}\bigcup K\) the response at \(s=\mathbf1_{\mathcal K}\) equals the response at \(s=\mathbf1_K\). That response reads the pair, the datum and the sequence only in \(\bigcup K\)" (L3 147). Its premises: (D1) unique fixed point, Definition D operators with HW's structure, and \(\mathsf W_s\) "a sum of terms, each carrying the factor \(s^\omega\) of its walk data and reading its argument and the pair, and writing its output, only on the hull of that data" (L3 147). L3C §4: "This includes the extra assumptions on \(\mathsf W_s\) and the separately specified current construction at L159. It does not establish either assumption for the actual moves."
- *NR9 (4.3)–(4.4)* (NR9 211–231): \(d=d_s(a)=\mathcal C(a-H(s)d)\), \(z=a-H(s)d\), \(Z=1-H(s)d_s'(a)\), \(p_s=H(s)^{\mathsf T}\mathbf J\), \(d_{3,s}=d_s-\mathcal C_2\), and
  \(W_s^{\rm red}(a)=-d_{3,s}'(a)^{\mathsf T}p_s-K^{\mathsf T}M_sd_s(a)-d_s'(a)^{\mathsf T}M_sKa+d_s'(a)^{\mathsf T}M_sd_s(a)+Z^{\mathsf T}N_0(z)\) (NR9 229). "\(M_s\) is its own walk sum, whereas \(\mathfrak G(s)\) in R9 remains the separately assigned composed expansion of `pw-bridge.md` Section 7" (NR9 231). NR9 61: [RED] is the identification of the consumer's \(\mathsf W_s\) with (4.4).
- *D3L (3)–(4)* (D3L 70–92): \(\lambda_s=(I+H_s^{\mathsf T}C_h'^{\mathsf T})^{-1}H_s^{\mathsf T}F'_U(h)\), \(\lambda^0_s=H_s^{\mathsf T}F'_U(0)\), \(\mathsf j_s=R_hK_h^{\mathsf T}\lambda_s-K_0^{\mathsf T}\lambda_s^0\) (D3L 75), with the Neumann series (4) (D3L 84). Checked by Claude: "Current (3): existence, walk form (4), component locality, zero where there is no datum, exact on the physical locus" — ADVANCE (`gates/d3-local-check.md`, verdict table).
- *DF Proposition 5.1* (DF 247–255): under [PW], [NL], "R9 has a unique solution in the balls below, jointly holomorphic in all the specified variables". [PW] and [NL] remain inputs (DF 365).
- *IN1 Lemma 2 and its Outstanding* (IN1 276–334): path decoupling \(B^s_{xy}=B_{xy}\prod_{\Delta\in D(x,y)}s_\Delta\) of global matrices; "heredity is stronger than block factorization. The entries of \(R(A)\) in (20) still depend on the full exterior matrix after the path weights are set to zero" (IN1 329). Proposition 3.2 is the response analogue.
- *TD2* (TD2 295–341, 396–411): Lemma 8's (23)–(24) are "the valid finite estimates"; Correction 10: "Collapsing the logarithmic collar loses the collar-width decay; (26) shows the resulting boundary-attachment majorant is unbounded" (TD2 411).

---

## 2. The split calculus

### 2.1 Objects

Fix a main step, its depth-\(k\) separated sequence, its layer metric \(d_{\mathbf B}\) (HW §1) and the parameter partition \(\mathcal P\) of O1D Definition D. **[R]** I read \(\mathcal P\) as the grid of TD's fine cubes (side \(M\) at level \(i-1\)): CI 26 calls the response switches "fine switches", ST1 row 8 puts the floor \(M\ge C_{\rm dec}\bar\kappa\) on that side, and O1D Theorem B's floor \(\ell_{\mathsf P}\ge256\bar\kappa/\tau_L\) is the same kind of floor. The torus has at least three cubes of \(\mathcal P\) per direction (SA 17583: no box wraps).

Every coordinate of an unknown field (bond, row, site, top) and of the pair \(P=(U,A',\mathbf J)\) has a base point (the convention of HW §3, "Cutoffs") and a base cube of \(\mathcal P\) containing it, fixed by a tie-breaking rule. Fix \(s\) with \(|s_\Delta|\le e^{\bar\kappa}\theta_0\), \(\theta_0<1\) (a closed sub-polydisc; every statement then holds on the open polydisc). Let \(\mathcal N=\{\Delta:s_\Delta=0\}\) and let \(\mathcal W(s)\) be the set of wall-components of \(\mathcal P\setminus\mathcal N\) (face adjacency, SA 5794–5795).

For \(W\in\mathcal W(s)\), the **\(W\)-data** of a triple \((Y;P,S)\) are: the coordinates of the unknown \(Y\) based in cubes of \(W\); the source rows assigned to cubes of \(W\); \(s|_W\); and \(P|_{\bigcup W}\), the pair coordinates based in \(\bigcup W\).

Put \(\rho_{\mathbf B}:=3LM_1\). A point \(q\) is **deep in \(W\)**, \(q\in\operatorname{Dp}(W)\), if every cube of \(\mathcal P\) that meets the closed ball \(B_{\mathbf B}(q,\rho_{\mathbf B})\) belongs to \(W\).

**Facts** [P]. (D-a) \(\operatorname{Dp}(W)\cap\operatorname{Dp}(W')=\varnothing\) for \(W\ne W'\): the cubes containing \(q\) meet the ball. (D-b) If \(q\in\operatorname{Dp}(W)\) and \(d_{\mathbf B}(q,p)\le\rho_{\mathbf B}\), every cube containing \(p\) lies in \(W\); in particular \(p\) is based in \(W\). (D-c) If \(q\in\operatorname{Dp}(W)\), \(p\in\operatorname{Dp}(W')\) and \(d_{\mathbf B}(p,q)\le\rho_{\mathbf B}\), then \(W=W'\): by (D-b) the cubes containing \(p\) lie in \(W\), and by definition they lie in \(W'\).

### 2.2 Decoupled operators are split

A linear map \(O\) between field spaces is **split** (for \(s\)) if \(O(q,p)\ne0\) implies that \(q,p\in\operatorname{Dp}(W)\) for one \(W\in\mathcal W(s)\), and then the entry \(O(q,p)\) is a function of \(s|_W\) and \(P|_{\bigcup W}\) only.

**(D2′) field hulls** [I: HW Theorem W(c) field part, HWG 100, HWF 30, 116; for tree walks HWG 136 with the computation below]. Every term \(T_\omega\) of every walk or tree-walk expansion used by the specification outputs on \(\operatorname{supp}\tilde h_{\kappa_0}\), reads its input within \(d_{\mathbf B}\)-distance \(r_0\) of \(\operatorname{supp}\theta_{\kappa_n}\) (L3 147 states this structure), and reads the pair only on a field hull \(F(\omega)\subset[\![\omega]\!]^+\). For tree walks \([\![\omega]\!]^+\) is the union of \(\kappa^\sharp\) over all trunk and branch cubes, and \(\mathsf P(\omega)\) and \(s^\omega\) are formed from it as in O1D Definition D.

*Check of \(F(\omega)\subset[\![\omega]\!]^+\) for tree walks* [P from HWG 136]. HWG 136: a zero-length multiplier contributing at a row \(c\) reads a box \(\lambda^{(4)}\) with \(c\in\operatorname{supp}\theta_\lambda\subset\lambda^{(1/4)}\), and \(c\in\kappa^{(7/2)}\) for the cell \(\kappa\) it supplies. The centre of \(\lambda\) is within \(0.75M_1\xi_\lambda\) of \(c\), so \(\lambda^{(4)}\) lies in the sup-ball of radius \(5.25M_1\xi_\lambda\le5.25LM_1\xi_\kappa\) about \(c\) (adjacent scales differ by \(L\)). The point \(c\) is within \(4M_1\xi_\kappa\) of the centre of \(\kappa\). So \(\lambda^{(4)}\) lies in the concentric cube of half-side \((4+5.25L)M_1\xi_\kappa\le4L^2M_1\xi_\kappa\), which is \(\kappa^\sharp\), for \(L\ge2\). Branch field reads are covered by the branch cubes' own \(\kappa^\sharp\). The \(\mathcal C\) and \(E\) stencils add \(O_L(1)\), inside the same margin.

**Lemma 2.1 (Definition D sums are split)** [P from (D2′), O1D Lemma WC, Definition D]. Let \(O(s)=\sum_\omega s^\omega T_\omega\) be an absolutely convergent Definition D sum satisfying (D2′). Then \(O(s)\) and \(O(s)^{\mathsf T}\) are split. If \(O_1,O_2\) are split and \(N\) is linear with \(N(m,m')=0\) for \(d_{\mathbf B}(m,m')>\rho_{\mathbf B}\), and \(N(m,m')\) is a function of the pair at points within \(d_{\mathbf B}\)-distance \(\rho_{\mathbf B}\) of \(m\), then \(O_1NO_2\) is split. Finite sums and absolutely convergent series of split maps are split.

*Proof.* (i) Let \(O(s)(q,p)\ne0\). Some term has \(s^\omega\ne0\) and \(T_\omega(q,p)\ne0\). Then \(\mathsf P(\omega)\subset\mathcal P\setminus\mathcal N\). The set \([\![\omega]\!]^+\) is connected: consecutive cells satisfy \(X_{\kappa_{i-1}}\cap X_{\kappa_i}\ne\varnothing\) (HW proof of Theorem W(a), HWG 102), \(X_\kappa\subset\kappa^\sharp\), and branch cells overlap their parents (HW §7, tree walks). Every cube meeting it is in \(\mathsf P(\omega)\). By O1D Lemma WC all these cubes lie in one wall-component \(W\).

(ii) *Depth of the output.* \(q\in\operatorname{supp}\tilde h_{\kappa_0}\subset\kappa_0^{(2)}\), a cube of side \(5M_1\xi_{\kappa_0}\) concentric with \(\kappa_0^\sharp\), of side \(8L^2M_1\xi_{\kappa_0}\). The sup-distance from \(\kappa_0^{(2)}\) to the complement of \(\kappa_0^\sharp\) is \((4L^2-2.5)M_1\xi_{\kappa_0}\). On \(\kappa_0^\sharp\) the local scale is at most \(L\xi_{\kappa_0}\), since \(\kappa^\sharp\) meets at most three consecutive layers (O1D 105, under \(R_1\ge8L^3\)). A path of \(d_{\mathbf B}\)-length at most \(\rho_{\mathbf B}\) from \(q\) therefore has physical length at most \(3L^2M_1\xi_{\kappa_0}\) while it stays in \(\kappa_0^\sharp\), which is less than the distance to the boundary. So \(B_{\mathbf B}(q,\rho_{\mathbf B})\subset\kappa_0^\sharp\subset[\![\omega]\!]^+\). Every cube meeting this ball meets \([\![\omega]\!]^+\), so it is in \(\mathsf P(\omega)\subset W\). Thus \(q\in\operatorname{Dp}(W)\).

(iii) *Depth of the input.* \(p\) is within \(d_{\mathbf B}\)-distance \(r_0\) of \(\kappa_n^{(1/4)}\). The same argument with the margin \((4L^2-0.75)M_1\xi_{\kappa_n}\) applies, since \((r_0+\rho_{\mathbf B})L\le(4L^2-0.75)M_1\) when \(M_1\ge r_0\). Thus \(p\in\operatorname{Dp}(W)\).

(iv) *Dependence.* \(s^\omega\) reads \(s\) on \(\mathsf P(\omega)\subset W\). \(T_\omega\) reads the pair on \(F(\omega)\subset[\![\omega]\!]^+\subset\bigcup\mathsf P(\omega)\subset\bigcup W\). An entry of \(O(s)\) is the absolutely convergent sum of such terms, and a pointwise limit of functions of \((s|_W,P|_{\bigcup W})\) is again one.

(v) *Transposes* exchange \(q\) and \(p\) and keep every term's hull.

(vi) *Products.* \((O_1NO_2)(q,p)=\sum_{m,m'}O_1(q,m)N(m,m')O_2(m',p)\). A nonzero summand has \(q,m\in\operatorname{Dp}(W_1)\), \(m',p\in\operatorname{Dp}(W_2)\) and \(d_{\mathbf B}(m,m')\le\rho_{\mathbf B}\). By (D-c), \(W_1=W_2=:W\). The factor \(N(m,m')\) reads the pair within \(\rho_{\mathbf B}\) of \(m\), hence on cubes meeting \(B_{\mathbf B}(m,\rho_{\mathbf B})\), which lie in \(W\). Sums and series: as in (iv). ∎

### 2.3 Faithful and tame expressions

An **expression** is a map \(E\colon(Y;P,S)\mapsto\) field, at fixed \(s\). A **local map** of reach \(r\) is a map \(N(F_1,\dots,F_k;P,S)\) whose value at \(q\) depends only on the values of its arguments and of \(P,S\) at points \(p\) with \(d_{\mathbf B}(p,q)\le r\).

- \(E\) is **\(r\)-faithful** if, for every \(W\) and every \(q\) such that every cube meeting \(B_{\mathbf B}(q,r)\) lies in \(W\), \(E(q)\) is a function of the \(W\)-data alone.
- \(E\) is **\(r\)-tame** if (i) \(E(q)\equiv0\) unless \(d_{\mathbf B}(q,\operatorname{Dp}(W))\le r\) for some \(W\); and (ii) if \(d_{\mathbf B}(q,\operatorname{Dp}(W))\le r\), then \(E(q)\) is a function of the \(W\)-data alone.

**Lemma 2.2 (calculus)** [P]. All radii below are at most \(\rho_{\mathbf B}/5\).

- (a) The coordinates of \(Y\), the pair and the source are \(0\)-faithful.
- (b) A local map of reach \(r\) applied to \(r_i\)-faithful arguments is \((r+\max_ir_i)\)-faithful.
- (c) If \(O\) is split and \(E\) is \(r\)-faithful, then \(OE\) is \(0\)-tame.
- (d) Let \(N\) have reach \(r\), let it be linear (or vanish at zero) in arguments \(E_t\) that are \(r_t\)-tame, and let its other arguments be \(f\)-faithful. If \(2r+2\max r_t+f\le\rho_{\mathbf B}\), then \(N\) is \((r+\max r_t)\)-tame.
- (e) An \(r\)-tame expression with \(r\le\rho_{\mathbf B}\) is \(0\)-faithful.
- (f) Finite sums, and pointwise limits of sequences, of \(r\)-faithful (\(r\)-tame) expressions are \(r\)-faithful (\(r\)-tame).

*Proof.* (a) The coordinate at \(q\) is based in a cube containing \(q\), which lies in \(W\) under the hypothesis.

(b) Let every cube meeting \(B_{\mathbf B}(q,r+\max r_i)\) lie in \(W\). \(N\) reads at points \(p\) with \(d_{\mathbf B}(p,q)\le r\). For such \(p\), \(B_{\mathbf B}(p,r_i)\subset B_{\mathbf B}(q,r+r_i)\), so \(F_i(p)\) is a function of \(W\)-data; and \(P(p),S(p)\) are based in cubes meeting the ball, hence in \(W\).

(c) \((OE)(q)=\sum_pO(q,p)E(p)\). If \(q\notin\bigcup_W\operatorname{Dp}(W)\) all coefficients vanish, so \(OE(q)\equiv0\). If \(q\in\operatorname{Dp}(W)\), only \(p\in\operatorname{Dp}(W)\) occur; for them every cube meeting \(B_{\mathbf B}(p,\rho_{\mathbf B})\supset B_{\mathbf B}(p,r)\) lies in \(W\), so \(E(p)\) is a function of \(W\)-data; the coefficients are functions of \(s|_W,P|_{\bigcup W}\). Points at distance \(\le0\) from \(\operatorname{Dp}(W)\) are its points.

(d) If \(d_{\mathbf B}(q,\operatorname{Dp}(W))>r+\max r_t\) for every \(W\), then every \(p\) with \(d_{\mathbf B}(p,q)\le r\) has \(d_{\mathbf B}(p,\operatorname{Dp}(W))>r_t\) for every \(W\), so \(E_t(p)\equiv0\), and \(N(0,F)=0\). Otherwise take \(p_0\in\operatorname{Dp}(W)\) with \(d_{\mathbf B}(q,p_0)\le r+\max r_t\). For a read point \(p\) (\(d_{\mathbf B}(p,q)\le r\)): if \(E_t(p)\not\equiv0\), there is \(p'\in\operatorname{Dp}(W')\) with \(d_{\mathbf B}(p,p')\le r_t\), so \(d_{\mathbf B}(p',p_0)\le2r+2\max r_t\le\rho_{\mathbf B}\), and \(W'=W\) by (D-c); then \(E_t(p)\) is a function of \(W\)-data. The ball \(B_{\mathbf B}(p,f)\) lies in \(B_{\mathbf B}(p_0,2r+\max r_t+f)\subset B_{\mathbf B}(p_0,\rho_{\mathbf B})\), so the faithful arguments at \(p\) are functions of \(W\)-data, and so are \(P(p),S(p)\).

(e) Let all cubes containing \(q\) lie in \(W\). If \(E(q)\not\equiv0\), there is \(p\in\operatorname{Dp}(W')\) with \(d_{\mathbf B}(q,p)\le r\le\rho_{\mathbf B}\); by (D-b) the cubes containing \(q\) lie in \(W'\), so \(W'=W\), and (ii) gives the claim. If \(E(q)\equiv0\) there is nothing to prove.

(f) A pointwise limit of functions that do not depend on some variables does not depend on them. ∎

### 2.4 Uniqueness transfer

Let \(\|Y\|=\sup_y\varpi(y)\,n_y(Y)\), where \(n_y\) is a seminorm that reads \(Y\) only at points within \(d_{\mathbf B}\)-distance \(1\) of \(y\). SA's norms have this form: \(\xi_y|A|\) and \(\xi_y^2|\nabla_{\mathbf U}A|\) at \(y\) read one fine bond around \(y\) (SA 10373–10382), and a fine bond has \(d_{\mathbf B}\)-length \(\eta/\xi\le1\).

**Lemma 2.3 (gluing)** [P]. Let \(\Phi_P\) be maps on the field space, for admitted pairs \(P\), at fixed \((s,S)\). Assume: (G1) for each \(P\), \(\Phi_P\) has exactly one fixed point \(Y^*(P)\) in \(B_r=\{\|Y\|<r\}\), with \(r\) independent of \(P\); (G2) \((Y,P,S)\mapsto\Phi_P(Y)\) is \(0\)-tame. If \(P,\widetilde P\) agree on \(\bigcup W\) for some \(W\in\mathcal W(s)\), then \(Y^*(P)\) and \(Y^*(\widetilde P)\) agree at every point based in a cube of \(W\).

*Proof.* \(Y^*(P)=\Phi_P(Y^*(P))\) vanishes off \(\bigcup_{W'}\operatorname{Dp}(W')\), by (G2)(i); likewise \(Y^*(\widetilde P)\). Define \(\widehat Y\) equal to \(Y^*(P)\) at points based in cubes of \(W\), and to \(Y^*(\widetilde P)\) elsewhere.

*\(\widehat Y\) is a fixed point of \(\Phi_{\widetilde P}\).* Let \(q\) be a point. If \(q\) is in no \(\operatorname{Dp}(W')\), then \(\Phi_{\widetilde P}(\widehat Y)(q)=0\), and \(\widehat Y(q)=0\) because both fixed points vanish there. If \(q\in\operatorname{Dp}(W)\), then \(q\) is based in \(W\), and \(\Phi_{\widetilde P}(\widehat Y)(q)\) is a function of the \(W\)-data of \((\widehat Y,\widetilde P,S)\). These equal the \(W\)-data of \((Y^*(P),P,S)\). So \(\Phi_{\widetilde P}(\widehat Y)(q)=\Phi_P(Y^*(P))(q)=Y^*(P)(q)=\widehat Y(q)\). If \(q\in\operatorname{Dp}(W'')\), \(W''\ne W\), then \(q\) and every point based in \(W''\) is based outside \(W\), so the \(W''\)-data of \((\widehat Y,\widetilde P,S)\) are those of \((Y^*(\widetilde P),\widetilde P,S)\), and the value is \(Y^*(\widetilde P)(q)=\widehat Y(q)\).

*\(\widehat Y\in B_r\).* Fix \(y\). Suppose \(n_y\) reads a point \(p\in\operatorname{Dp}(W_1)\) where \(\widehat Y\ne0\) and a point \(p'\in\operatorname{Dp}(W_2)\) where \(\widehat Y\ne0\). Then \(d_{\mathbf B}(p,p')\le2\le\rho_{\mathbf B}\), so \(W_1=W_2\) by (D-c). Hence the nonzero values of \(\widehat Y\) read at \(y\) are all at points deep in one component \(W_1\), or there are none. If \(W_1=W\), these points are based in \(W\), and every other point read at \(y\) is not deep in any component (it is within distance \(2\) of a \(W\)-deep point, so by (D-b) any deep component it belonged to would be \(W\)); there both \(\widehat Y\) and \(Y^*(P)\) vanish. So \(\widehat Y=Y^*(P)\) on the read set and \(n_y(\widehat Y)=n_y(Y^*(P))\). If \(W_1\ne W\), the same argument gives \(n_y(\widehat Y)=n_y(Y^*(\widetilde P))\). If there are none, \(n_y(\widehat Y)=0\). So \(\|\widehat Y\|\le\max\{\|Y^*(P)\|,\|Y^*(\widetilde P)\|\}<r\).

By (G1) for \(\widetilde P\), \(\widehat Y=Y^*(\widetilde P)\). At points based in \(W\) this reads \(Y^*(\widetilde P)=Y^*(P)\). ∎

**Variant (switch locality)** [P, same proof]. Let \(W\) be a wall-component of both \(\operatorname{supp}s\) and \(\operatorname{supp}\widetilde s\), with \(s|_W=\widetilde s|_W\), and let \(P=\widetilde P\) on \(\bigcup W\). If \(\Phi_{s,P}\), \(\Phi_{\widetilde s,\widetilde P}\) satisfy (G1)–(G2), each for its own component structure, the two fixed points agree at points based in \(W\). Indeed \(\operatorname{Dp}(W)\) is defined by \(W\) alone, and every other deep set of \(\widetilde s\) consists of points based outside \(W\).

---

## 3. (DR-locP)

### 3.1 The specification

**(Spec-D)** [design, as chosen by the DR lane; I: O1D Definition D, NR9 (4.3)–(4.4), D3L (3)].

- The decoupled operators \(H(s)\), \(H(s)^{\mathsf T}\), \(H_1(s)\), \(M_s\), \(\mathfrak G(s)\) are Definition D sums of HW walk or tree-walk terms, or finite products of such sums with local maps between them (NR9 231: "\(M_s\) is its own walk sum, whereas \(\mathfrak G(s)\) in R9 remains the separately assigned composed expansion of `pw-bridge.md` Section 7"), each satisfying (D2′).
- The local maps are \(\mathcal C,\mathcal C',\mathcal C'',\mathcal C_2,\mathcal C_2'\) (straightened constraint and its Taylor parts), \(K,K^{\mathsf T}\) (raw-row map), \(N_0\) (Wilson remainder), \(F'_U\) (Wilson force), \(R_h,K_h^{\mathsf T}\) (D3L 75), each holomorphic, with \(d_{\mathbf B}\)-reach at most \(r_0\le8L+1\) (HW §3: every pillar, row carrier and plaquette has \(d_{\mathbf B}\)-diameter \(\le4L\); a row's double block has side at most \(2L\xi\), L3 147).
- (R9) is NR9's system: \(a=H_1(s)B'+A\); \(A+\mathfrak G(s)W_s^{\rm red}(a)=0\); \(d=\mathcal C(a-H(s)d)\); response \(\mathbf H=z:=a-H(s)d\); current \(\mathsf j=\mathsf j_s\) by D3L (3) with \(h=\mathbf H\).

**Reduced unknowns.** Put \(Y=(A,Y_d)\) with \(Y_d:=H(s)d\). Then \(d=\mathcal C(a-Y_d)\), \(z=a-Y_d\), \(d_s'(a)=\mathcal C'_z\big(1+H(s)\mathcal C'_z\big)^{-1}\) (differentiate \(d=\mathcal C(a-H(s)d)\)), with transpose \(d_s'^{\mathsf T}=\big(1+\mathcal C_z'^{\mathsf T}H(s)^{\mathsf T}\big)^{-1}\mathcal C_z'^{\mathsf T}\), and \(Z^{\mathsf T}=1-d_s'^{\mathsf T}H(s)^{\mathsf T}\). The map is
\[
 \Phi(Y)=\Big(-\mathfrak G(s)\,W_s^{\rm red}\big(a;Y_d\big),\ H(s)\,\mathcal C(a-Y_d)\Big),\qquad a=H_1(s)B'+A .
\]
Solutions \((A,d)\) of NR9's system and fixed points \((A,Y_d)\) of \(\Phi\) correspond by \(Y_d=H(s)d\), \(d=\mathcal C(a-Y_d)\).

**(UNQ)** [I, owner DR lane: DF Proposition 5.1 from [PW], [NL]; ST1 137; L3 (D1)]. For every admitted \((s,P,S)\) on the closed switched polydisc and source ball, \(\Phi\) has exactly one fixed point in \(B_r\), a ball of the sup-type norms of §2.4 with \(r\) uniform, and the actual DR is \((z,\mathsf j_s)\) at it. **[R]** DF and L3 state uniqueness for the unknowns \((A,X)\), \(X=d\). The two balls correspond for small \(r\), since \(|\mathcal C(w)|\le C|w|^2\) (CRIT (I-UNQ)) and \(H(s)\) is bounded by \(\widehat b\) (SA 10383); I take (UNQ) in reduced variables as the import.

**(Bud)** \(80r_0\le\rho_{\mathbf B}\). It holds when \(M_1\ge240\), since \(r_0\le8L+1\le9L\); HW's floor \(M_1\ge M_C(L)=16L(\rho'+4M'+16Lr_0)\) (HW §3, (G0)) implies it.

**Lemma 3.1 (the specification is tame)** [P from (Spec-D), (D2′), (Bud), Lemmas 2.1–2.2]. \(\Phi\) is \(0\)-tame. At the fixed point, \(z\) is \(0\)-tame and \(\mathsf j_s\) is \(r_0\)-tame as functions of \((Y^*,P,S)\).

*Proof.* By Lemma 2.1 every decoupled operator is split. By Lemma 2.2(c),(e), each of their outputs on a faithful argument of radius \(\le\rho_{\mathbf B}\) is \(0\)-tame and \(0\)-faithful. By Lemma 2.2(a), \(A,Y_d,B',P\) are \(0\)-faithful. So \(a=H_1(s)B'+A\) and \(z=a-Y_d\) are \(0\)-faithful.

*Second component.* \(\mathcal C(a-Y_d)\) is \(r_0\)-faithful by (b); \(H(s)\mathcal C(\cdot)\) is \(0\)-tame by (c).

*First component.* \(\mathfrak G(s)\) is the outermost operator, so by (c) it suffices that \(W_s^{\rm red}(a;Y_d)\) be \(\rho_{\mathbf B}\)-faithful. Take its five terms (NR9 229).

1. \(-d_{3,s}'^{\mathsf T}p_s=-d_s'^{\mathsf T}p_s+\mathcal C_2'(a)^{\mathsf T}p_s\), \(p_s=H(s)^{\mathsf T}\mathbf J\) (\(0\)-faithful by (c),(e)). \(\mathcal C_2'(a)^{\mathsf T}p_s\) is \(r_0\)-faithful. For \(d_s'^{\mathsf T}w\) use the Neumann series \(d_s'^{\mathsf T}w=\mathcal C_z'^{\mathsf T}w+\sum_{n\ge1}(-1)^n\mathcal C_z'^{\mathsf T}\big(H(s)^{\mathsf T}\mathcal C_z'^{\mathsf T}\big)^nw\), absolutely convergent on the response ball (its majorant is D3L's \(\sum(Bcr)^n\), D3L 81–86). Each term is \(\mathcal C_z'^{\mathsf T}\) (reach \(r_0\), coefficient \(z\), \(0\)-faithful) applied either to \(w\) or to an output of \(H(s)^{\mathsf T}\) (\(0\)-faithful). So \(d_s'^{\mathsf T}w\) is \((r_0+\rho_w)\)-faithful when \(w\) is \(\rho_w\)-faithful and \(r_0+\rho_w\le\rho_{\mathbf B}\), by (b), (c), (f).
2. \(-K^{\mathsf T}M_sd_s\): \(d_s=\mathcal C(a-Y_d)\) is \(r_0\)-faithful; \(M_s(\cdot)\) is \(0\)-faithful; \(K^{\mathsf T}\) adds \(r_0\).
3. \(-d_s'^{\mathsf T}M_sKa\): \(Ka\) is \(r_0\)-faithful; \(M_s(\cdot)\) is \(0\)-faithful; \(d_s'^{\mathsf T}\) adds \(r_0\) by item 1.
4. \(d_s'^{\mathsf T}M_sd_s\): as 2–3.
5. \(Z^{\mathsf T}N_0(z)=N_0(z)-d_s'^{\mathsf T}H(s)^{\mathsf T}N_0(z)\): \(N_0(z)\) is \(r_0\)-faithful; \(H(s)^{\mathsf T}N_0(z)\) is \(0\)-faithful; \(d_s'^{\mathsf T}\) adds \(r_0\).

Every chain of local maps between two decoupled operators has reach at most \(2r_0\le\rho_{\mathbf B}\). So \(W_s^{\rm red}\) is \(2r_0\)-faithful and \(\Phi_1\) is \(0\)-tame.

*Readouts.* At the fixed point, \(A=\Phi_1(Y^*)\) and \(Y_d=\Phi_2(Y^*)\), so \(z=H_1(s)B'+\Phi_1(Y^*)-\Phi_2(Y^*)\) is \(0\)-tame. For the current, \(\lambda_s=H(s)^{\mathsf T}\big(1+\mathcal C_h'^{\mathsf T}H(s)^{\mathsf T}\big)^{-1}F'_U(h)\) (the identity \((1+XY)^{-1}X=X(1+YX)^{-1}\) moves the split operator outside) and \(\lambda_s^0=H(s)^{\mathsf T}F'_U(0)\) are \(0\)-tame, with \(h=z\). Then \(\mathsf j_s=R_hK_h^{\mathsf T}\lambda_s-K_0^{\mathsf T}\lambda_s^0\) is linear in \(\lambda\) with coefficients reading \(h\) within \(r_0\); by (d) with \(r=r_0\), \(r_t=0\), \(f=0\), it is \(r_0\)-tame. ∎

### 3.2 The theorem

**Theorem 1 ((DR-locP))** [P from (Spec-D), (D2′), (UNQ), (Bud), the torus floor]. Let \(|s_\Delta|<e^{\bar\kappa}\), let \(S\) lie in the source ball, and let \(K'\) be a face-component of \(\operatorname{supp}s\).

- (i) *Pair-locality, \(c_P=0\).* If admitted pairs \(P,\widetilde P\) agree on \(\bigcup K'\), then \((\mathbf H,\mathsf j)(s;P,S)=(\mathbf H,\mathsf j)(s;\widetilde P,S)\) at every bond and row based in a cube of \(K'\). In particular this holds on every stencil \(B_b\subset K'\), and on every stencil \(B_b\subset K'\cup\mathcal N\), where the response vanishes on the \(\mathcal N\)-cubes.
- (ii) *Switch and source locality.* The response there is a function of \(s|_{K'}\) and of the source rows assigned to \(K'\) only, among all \(s\) for which \(K'\) is a face-component. This recovers R's component clause (TD 32) for the specification.
- (iii) *Restriction.* For \(Q\) in \(\rho_{\bigcup K'}(\mathcal O_\sigma(U))\), the image of the declared restriction map (SA 5738–5739: restriction "discards bonds and variables outside \(X\)"), put \(h_{K'}(s|_{K'};Q,S_{K'}):=(\mathbf H,\mathsf j)(s;P,S)|_{K'}\) for any \(P\) with \(\rho_{\bigcup K'}P=Q\). It is well defined, holomorphic in \((s|_{K'},Q,S_{K'})\) on that open image, real at real arguments, and compatible with restriction: for \(N\subset N'\), \(\rho_N\circ\rho_{N'}=\rho_N\), so \(h_{K'}\) computed through \(\rho_{N'}\), \(N'\supset\bigcup K'\), equals \(h_{K'}\circ\rho_{\bigcup K'}\).
- (iv) *Full declared domain* [needs (UNQ-loc)]. If the \(K'\)-block of \(\Phi\), which by Lemma 3.1 is a function of \(K'\)-data alone, has a unique fixed point in \(B_r\) for every \(Q\) in the declared local domain \(\mathcal O_\sigma(\bigcup K';U)\), then \(h_{K'}\) extends holomorphically to that domain by the same formula.

*Proof.* (i) Lemma 3.1 gives (G2) and (UNQ) gives (G1). Lemma 2.3 gives \(Y^*(P)=Y^*(\widetilde P)\) at points based in \(K'\). The readouts \(z\) and \(\mathsf j_s\) are \(0\)-faithful there by Lemma 3.1 and Lemma 2.2(e), so at a bond based in \(K'\) they are functions of the \(K'\)-data of \((Y^*,P,S)\), which agree. At a point \(q\) based in an \(\mathcal N\)-cube, \(z(q)=0\) (no point of an \(\mathcal N\)-cube is deep), and \(\mathsf j_s(q)=0\): a deep point \(p\) with \(d_{\mathbf B}(p,q)\le r_0\) would force \(q\)'s cube into a component, by (D-b).

(ii) The variant of Lemma 2.3, with Lemma 3.1, gives switch locality; the source rows of \(K'\) are part of the \(K'\)-data.

(iii) Well defined by (i). The pair has coordinates \((A',\mathbf J)\) at fixed real \(U\), and \(\rho_{\bigcup K'}\) is the coordinate projection onto those based in \(\bigcup K'\). A coordinate projection of an open set is open. Fix \(P_0\) and write \(P=(Q,P^{\rm ext})\). For \(Q\) near \(Q_0=\rho P_0\), the pair \((Q,P_0^{\rm ext})\) lies in the open set \(\mathcal O_\sigma(U)\), and \(h_{K'}(Q)=(\mathbf H,\mathsf j)(s;(Q,P_0^{\rm ext}),S)|_{K'}\) by (i). The right side is holomorphic (SA 10393–10394; DF Proposition 5.1). Reality: at real \((s,Q,S)\) choose real \(P_0^{\rm ext}\). Compatibility is the composition rule of coordinate projections.

(iv) A uniformly contracting holomorphic family has a holomorphic fixed point (uniform limit of the holomorphic iterates). On the image of restriction it agrees with (iii) by uniqueness. ∎

**Corollary 1′ (with the completed source)** [P from Theorem 1 and (S-loc)]. **(S-loc)** [I, owner ST1/NL1: TD 33 reads "Each source row reads only its cube and its first graph-neighbour layer"; **[R]** I read this as including the pair, the stored data \(v_0\) and the pins]. Then the response at the source \(S(v_0+u(s\odot\zeta))\) on the bonds of \(K'\) depends on the pair only through \(P|_{N_1(K')}\), so \(c_P=1\). It reads \(\zeta\) only on cubes of \(N_1(K')\cap\operatorname{supp}s\). (A corner-adjacent component can lie in \(N_1(K')\); TD Lemma 2's proof uses the corner graph for this reason, TD 139.)

*On "at fixed \(P\)".* NL1-L 168–169 states the component reads "at fixed \(P\)". Theorem 1 removes that qualifier for the specification (Spec-D). For Boolean \(s\) the same conclusion is the last sentence of L3 Lemma C (L3 147), checked ADVANCE, conditional, by Codex (L3C §4). Theorem 1 adds complex \(s\), the current component written out through (4.4) and (3), the restriction statement, and the explicit budget.

### 3.3 Why bounds alone cannot give it

**Proposition 3.2 (R does not imply (DR-locP))** [CE]. There is a response satisfying every clause of TD's R that is checked below (joint holomorphy, vanishing at zero source, the bound (3), component reads at fixed pair, single-cube stencils, reality), for which the response on a single-cube component depends on the pair at every cube of the torus.

*Construction.* One bond and one row per fine cube; \(n_b(h)=|h_b|\). Pairs \(P=(p_c)\in\mathbb C^\Gamma\), \(|p_c|<1/8\). For face-adjacent \(c,c'\) put \(T(P)_{cc'}=t(1+p_c)(1+p_{c'})\), else \(0\); \(A(P)=I-T(P)\); \(B(P)=A(P)^{-1}=\sum_nT(P)^n\). In four dimensions each cube has \(8\) face neighbours, so every row of \(T\) has absolute sum at most \(8t(9/8)^2<11t\), and \(|(T^n)_{cc'}|\le(11t)^n\), zero for \(n<d_1(c,c')\), the face-graph distance. So \(|B_{cc'}|\le2(11t)^{d_1(c,c')}\) for \(11t\le1/2\). For each ordered pair fix a face-graph geodesic \(\pi(c,c')\), reversed for \((c',c)\). Path-weight it as in IN1 (20):
\[
 B^s_{cc'}=B(P)_{cc'}\prod_{\Delta\in\pi(c,c')}s_\Delta,\qquad h(s;P,S)=\epsilon B^s(P)S .
\]
*R holds.* Holomorphy, reality and vanishing at \(S=0\) are clear. With \(11te^{\bar\kappa}=e^{-\mu-8}\), \(|h_c|\le2\epsilon e^{\bar\kappa}\|S\|\sum_{c'\in\operatorname{supp}S}e^{-(\mu+8)d_1(c,c')}\le4\epsilon e^{\bar\kappa}\|S\|e^{-\mu d(c,\operatorname{supp}S)}\), using \(d_1\ge d\) and TD (9); this is (3) with \(C_DE_{\bar\kappa}=4\epsilon e^{\bar\kappa}\). If \(B^s_{cc'}\ne0\), every cube of \(\pi(c,c')\) is in \(\operatorname{supp}s\), and consecutive ones share a face, so \(c,c'\) lie in one face-component \(K\) and the entry reads \(s\) only on \(K\). So the response on \(K\) reads only the rows and switches of \(K\), at fixed \(P\).

*(DR-locP) fails.* Take \(s=\mathbf1_{\{c_0\}}\), \(K'=\{c_0\}\), \(S_{c_0}=1\). Then \(h_{c_0}=\epsilon B(P)_{c_0c_0}\). At \(P=0\), \(B=(I-t\,\mathrm{Adj})^{-1}\) has all entries positive (the face graph is connected and every term of the Neumann series is nonnegative), and \(\partial_{p_z}T|_{P=0}\) has nonnegative entries, not all zero. So \(\partial_{p_z}B_{c_0c_0}|_{P=0}=(B\,\partial_{p_z}T\,B)_{c_0c_0}>0\) for every cube \(z\). For small real \(\theta\ne0\), \(P=0\) and \(\widetilde P=\theta e_z\) agree on \(N_c(K')\) whenever \(d(z,c_0)>c\), but give different \(h_{c_0}\). ∎

*What the example shows.* The dependence is exponentially small, \(|\partial_{p_z}h_{c_0}|\le C(11t)^{2d_1(c_0,z)}\). It is exact locality that fails. The cause is the one IN1 329 names for the Gaussian root: the path weights multiply entries of a *global* inverse. If instead \(B^s\) is the walk sum \(\sum_\omega s^\omega\prod_iT_{c_ic_{i+1}}\) with \(s^\omega\) over the visited cubes, each term reads \(P\) only on its walk, and Theorem 1's argument applies. That is the difference between IN1 (20) and O1D Definition D.

*Why approximate locality would not do* **[R, heuristic, not used]**. Telescoping the example in collars \(N_n(K')\) gives pieces of size \(e^{-2\mu n}\) whose carriers contain \(N_n(K')\setminus K'\), about \(n|\partial K'|\) cubes, each to be met by a filing tree. For the large components that occur below (they contain collared hubs) the weights \(e^{\lambda_Pn|\partial K'|/81}\) are not paid by \(e^{-2\mu n}\).

### 3.4 Where the decay rate against \(e^{\bar\kappa}\) enters, and constant order

The walk sums converge on \(|s_\Delta|\le e^{\bar\kappa}\) because a walk of \(d_{\mathbf B}\)-length \(t\) meets at most \(2^4(1+4t/\ell_{\mathsf P})\) parameter cubes (O1D Lemma P, (2.2)), so \(|s^\omega|\le e^{16\bar\kappa}e^{(64\bar\kappa/\ell_{\mathsf P})t}\), against the walk decay \(e^{-(\tau_L/2)t}\). This needs \(\ell_{\mathsf P}\ge256\bar\kappa/\tau_L\) (O1D Theorem B): a floor on the cube side \(M\), chosen after \(\bar\kappa\) (ST1 row 8). It is a convergence floor and does not enter Theorem 1. The collar \(c_P=0\) comes from the supports: \(F(\omega)\subset\bigcup\mathsf P(\omega)\).

| Constant | Where fixed | Before \(\kappa\)? | Independent of \(M,\bar\kappa\)? |
|---|---|---|---|
| \(c_P=0\) (\(1\) with sources) | — (a number) | yes | yes |
| \(\rho_{\mathbf B}=3LM_1\), \(r_0\le8L+1\), (Bud) \(80r_0\le\rho_{\mathbf B}\) | rows 2–3 (\(L\), \(M_1\)) | yes | yes |
| \(\kappa^\sharp\) side \(8L^2M_1\xi\), \(R_1\ge8L^3\) | O1D 105, rows 2–3 | yes | yes |
| \(\ell_{\mathsf P}\ge\max\{8r_1+1,256\bar\kappa/\tau_L\}\) | row 8 (\(M\) after \(\bar\kappa\)) | no | floor in \(\bar\kappa\); read only by convergence |
| (UNQ) ball \(r\), source threshold \(s_D=\epsilon_De^{-c_D\bar\kappa}\) | DR lane, row 7–10 | no | used only through (G1) |

No cycle: Theorem 1 reads no constant chosen after \(M_1\) except through (UNQ), which is an existence statement.

---

## 4. The joint composition

TD2d's statement (TD2d 405–408): "(JC) joint composition [O]. Under R, A and (5-sw), for \(V\) outside \(N_\rho(X_f)\), \(|f_{W,V}|\le C\widetilde\omega_f^{\rm sw}\prod_{c\in W}\frac{2\beta_c}\delta\big(\frac CD\big)^{|V|/2}e^{-(a-12)m_{N_\rho(X_f)}(W\cup V)}\)." Its route (TD2d 410): "Treat each switch cube as a second Boolean variable of its cube … then TD Lemma 3 with two labels per cube." This section writes that route, with one change that matters: the expansion holds only the **read stencils** at one, not the whole base, so the decay is measured from the reads.

### 4.1 Setting

Notation is TD's (TD 25–61): \(D=e^{\bar\kappa}-1\), \(Q=6400/D\le\frac12\), \(a=\frac12\log(D/6400)\), so \(Q=e^{-2a}\); \(\delta=(8e)^{-1}\); \(\varrho,A_R,A_V,K_1,\beta_c,\vartheta\) as in TD (4); \(A_b=A_Ve^{-\mu_Rd_+(b,\mathcal S)}\). Put \(\delta_J:=\delta/3=(24e)^{-1}\) and
\[
 \eta_1:=\frac{C_DE_{\bar\kappa}C_A\delta_{\rm src}}{A_V}=\frac{\delta_{\rm src}}{3\delta_{\rm src}+c_Tge^{\bar\kappa}R}\le\frac{A_1\ell^{p_0-q}}{c_Te^{\bar\kappa}} .
\]
**(TJ)** \(8\eta_1D^{15}\le1\). It is a ceiling on \(\gamma\) at fixed \(\bar\kappa\), since \(q>p_0\) (TD 35).

Fix an exempt term \(f\) with complete reads \(\mathcal B_f\), read cubes \(X(f)\), presentation set \(X_f\supset X(f)\), and **complete stencils**: \(B_b\subset X_f\) for every \(b\in\mathcal B_f\) [I: CI 18 carrier definition; TD2 Lemma 8's premise "require \(B_b\subset X_f\) for every read", TD2 318]. Fix a **base** \(N\supset X_f\), a finite set \(V\) of fine cubes with \(V\cap N=\varnothing\), and a nonempty set \(W\) of gas cubes. Neither \(X_f\) nor \(N\) need be connected. For \(A\subset V\) put \(s_A=\mathbf1_{N\cup A}\), and
\[
 F_f(P;s,\zeta)=\Phi_f\big(P,h(s;P,S(v_0+u(s\odot\zeta)))\big),\qquad
 f_{W,V}(P;\zeta)=\sum_{A\subset V}(-1)^{|V\setminus A|}D_W\big[F_f(P;s_A,\cdot)\big](\zeta).
\]

**Proposition 4.0 (exact decomposition)** [P]. \(\sum_{V\subset\mathcal P\setminus N}f_{W,V}=f_W\), where \(f_W=D_W[\Phi_f(P,h_0+G(\mathbf1,\cdot))]\) is TD (14)'s piece.

*Proof.* Möbius inversion on the finite Boolean lattice of subsets of \(\mathcal P\setminus N\) at its top element: \(\sum_{V}\sum_{A\subset V}(-1)^{|V\setminus A|}g(A)=g(\mathcal P\setminus N)\). At \(A=\mathcal P\setminus N\), \(s_A=\mathbf1\), and \(F_f(P;\mathbf1,\zeta)=\Phi_f(P,h(\mathbf1;P,S(v_0+u(\zeta))))=\Phi_f(P,h_0+G(\mathbf1,\zeta))\) by TD (4). ∎

### 4.2 Joint response coefficients

For \(t\in\{0,1\}^W\) and \(\sigma\in\{0,1\}^V\) let \(s(\sigma)=\mathbf1_N+\sum_{v\in V}\sigma_v\mathbf1_v\) and
\[
 g(t,\sigma)=h\big(s(\sigma);P,S(v_0+u(s(\sigma)\odot(\zeta\mathbf1_t)))\big),\qquad
 g_{B,A}=\sum_{B'\subset B}\sum_{A'\subset A}(-1)^{|B\setminus B'|+|A\setminus A'|}g(\mathbf1_{B'},\mathbf1_{A'})
\]
for \(B\subset W\), \(A\subset V\). So \(g(\mathbf1_B,\mathbf1_A)=\sum_{B'\subset B,A'\subset A}g_{B',A'}\).

**Lemma 4.1 (joint coefficients)** [P from R (TD 25–33)]. Let \(\|\zeta\|_\infty<\varrho\) and \(b\in\mathcal B_f\).

- (a) \(n_b(g_{B,A})=0\) unless some set \(Y\), connected in the fine (corner) graph, satisfies \(B\cup A\cup B_b\subset Y\subset N\cup A\).
- (b) If \(B\ne\varnothing\): \(n_b(g_{B,A})\le A_Re^{-\mu_Rd_+(b,\mathcal S)}\,Q^{\operatorname{St}(B\cup A\cup\{\Delta_b\})}\prod_{c\in B}\frac{2|\zeta|_c}{\varrho}\).
- (c) If \(B=\varnothing\ne A\): \(n_b(g_{\varnothing,A})\le(A_b/4)\cdot8\eta_1D^{15}\,Q^{\operatorname{St}(A\cup\{\Delta_b\})}\).
- (d) \(g_{\varnothing,\varnothing}=h(\mathbf1_N;P,S(v_0))\) and \(n_b(g_{\varnothing,\varnothing})\le A_b/3\).

*Proof.* Fix a scalar linear functional \(\ell\) on the finite-dimensional readout at \(b\) with \(|\ell(\cdot)|\le n_b(\cdot)\); the seminorm bound follows by taking the supremum over such \(\ell\) (TD 129). Introduce complex scalings \(z\in\mathbb C^W\) and
\[
 \varphi(s;z)=\ell\Big(h\big(s;P,S(v_0+u(s\odot(z\odot\zeta)))\big)\Big),
\]
holomorphic on \(\{|s_c|<e^{\bar\kappa}\}\times\{|z_c\zeta_c|<\varrho\}\): by the choice of \(\varrho\) in TD (4), \(\|u(s\odot z\zeta)\|_\infty\le c_Tge^{\bar\kappa}\varrho\), so the datum stays in its chart and the completed source in its ball (TD 139). Then \(g(\mathbf1_{B'},\mathbf1_{A'})\) at \(b\) is \(\varphi(s_{A'};\mathbf1_{B'})\) read through \(\ell\).

*Step 1 (expansion holding only \(B_b\) at one).* For a \(\{0,1\}\)-vector \(s\) with \(s=1\) on \(B_b\),
\[
 \varphi(s;z)=\sum_{Y'\subset\operatorname{supp}s\setminus B_b}I_{Y'}(z),\qquad
 I_{Y'}(z)=\int_{[0,1]^{Y'}}\partial^{Y'}_{s}\varphi\big(\mathbf1_{B_b}+\tau_{Y'};z\big)\,d\tau ,
\]
where \(\mathbf1_{B_b}+\tau_{Y'}\) has switches \(1\) on \(B_b\), \(\tau_c\) on \(Y'\) and \(0\) elsewhere. *Proof:* induction on \(|\operatorname{supp}s\setminus B_b|\), using \(\psi(1)=\psi(0)+\int_0^1\psi'(\tau)d\tau\) in one switch and applying the induction hypothesis to both terms (in the second, to the function \(\partial_c\varphi\) of the remaining switches). This uses \(B_b\subset X_f\subset N\), so \(s=1\) on \(B_b\) at every corner.

*Step 2 (switch selection).* \(I_{Y'}\) does not depend on \(A'\); \(A'\) only restricts which \(Y'\) occur, namely \(Y'\subset(N\setminus B_b)\cup A'\). For fixed \(B'\),
\[
 \sum_{A'\subset A}(-1)^{|A\setminus A'|}\sum_{Y'\subset(N\setminus B_b)\cup A'}I_{Y'}
 =\sum_{Y'}I_{Y'}\sum_{Y'\cap V\subset A'\subset A}(-1)^{|A\setminus A'|}
 =\sum_{Y'\subset(N\setminus B_b)\cup A,\ Y'\cap V=A}I_{Y'} ,
\]
since the inner sum is \((1-1)^{|A\setminus(Y'\cap V)|}\) when \(Y'\cap V\subset A\).

*Step 3 (connectivity).* Put \(Y=B_b\cup Y'\). If some \(c\in Y'\) is not joined to \(B_b\) inside \(Y\) in the fine graph, then \(I_{Y'}=0\). Indeed, at every switch vector supported in \(Y\) with value \(1\) on \(B_b\), the face-components of the support that meet \(B_b\) lie inside the corner-component \(Y_b\) of \(B_b\) in \(Y\setminus\{c\}\), whatever the value of \(s_c\), and \(c\notin N_1(Y_b)\). By R's second bullet (TD 32: "when \(B_b\subset\operatorname{supp}s\), its stencil reads only components meeting \(B_b\)") the stencil of \(b\) reads only the switches and source rows of those components, and the source rows read \(v\) only on their first neighbour layer (TD 33), which does not contain \(c\). So \(\varphi\) does not depend on \(s_c\) on this set, and \(\partial_c\varphi=0\).

*Step 4 (masking).* If \(c\in B\setminus Y\), the integrand of \(I_{Y'}\) has \(s_c=0\), so \(z_c\) enters only through \(s_cz_c\zeta_c=0\); \(I_{Y'}\) does not depend on \(z_c\), and its \(B\)-difference in \(z\) vanishes. With Steps 2–3 this proves (a): a surviving \(Y\) is connected and contains \(B\cup A\cup B_b\), and \(Y\subset N\cup A\).

*Step 5 (bounds).* Let \(\Psi(s;z)=\varphi(s;z)-\varphi(s;0)\). On the polydisc, \(|\varphi(s;z)|\le C_DE_{\bar\kappa}s_De^{-\mu_Rd_+(b,\mathcal S)}\) by (3), since the source support lies in \(\mathcal S\); so \(|\Psi|\le2C_DE_{\bar\kappa}s_De^{-\mu_Rd_+(b,\mathcal S)}\). For \(B\ne\varnothing\), the \(z\)-difference \(D^z_B\) kills \(\varphi(s;0)\), so \(D_B^zI_{Y'}=\int D^z_B[\partial^{Y'}\Psi](\tau;\cdot)\,d\tau\). For fixed \(\tau\in[0,1]^{Y'}\), Cauchy circles of radius \(r<D\) about each \(\tau_c\) stay in \(|s_c|<e^{\bar\kappa}\) and give \(|\partial^{Y'}\Psi(\tau;z)|\le r^{-|Y'|}\sup|\Psi|\). The function \(z\mapsto D^z_B[\partial^{Y'}\Psi](\tau;z)\) vanishes on every hyperplane \(z_c=0\), \(c\in B\), and is bounded by \(2^{|B|}r^{-|Y'|}\sup|\Psi|\) on \(|z_c|<\varrho/|\zeta|_c\). The one-variable Schwarz lemma in each \(z_c\) in turn gives its value at \(z=\mathbf1\) at most \(2^{|B|}r^{-|Y'|}\sup|\Psi|\prod_{c\in B}|\zeta|_c/\varrho\). Let \(r\uparrow D\). For \(B=\varnothing\), use \(\varphi(s;0)\) itself: \(|\varphi(s;0)|\le C_DE_{\bar\kappa}\|S(v_0)\|e^{-\mu_Rd_+(b,\mathcal S)}\le C_DE_{\bar\kappa}C_A\delta_{\rm src}e^{-\mu_Rd_+(b,\mathcal S)}\) (TD 33), and Cauchy gives \(D^{-|Y'|}\) times this.

*Step 6 (count).* Distinct \(Y'\) give distinct \(Y\ni\Delta_b\), and \(|Y'|\ge|Y|-16\). A connected \(Y\) containing \(B\cup A\cup\{\Delta_b\}\) has at least \(n_0=\operatorname{St}(B\cup A\cup\{\Delta_b\})+1\) cubes, and rooted connected sets of \(n\) cubes number at most \(6400^{n-1}\) (TD Lemma 1). So \(\sum_YD^{-|Y\setminus B_b|}\le\sum_{n\ge n_0}6400^{n-1}D^{16-n}\le2D^{15}Q^{n_0-1}\) (TD 133–136). For \(B\ne\varnothing\) the product is \(2C_DE_{\bar\kappa}s_D\cdot2D^{15}=A_R\) times \(Q^{\operatorname{St}}\prod(2|\zeta|_c/\varrho)\): (b). For \(B=\varnothing\) it is \(2D^{15}C_DE_{\bar\kappa}C_A\delta_{\rm src}e^{-\mu_Rd_+}Q^{\operatorname{St}}=(A_b/4)\cdot8\eta_1D^{15}Q^{\operatorname{St}}\): (c).

(d) is (3) at \(s=\mathbf1_N\): \(n_b\le C_DE_{\bar\kappa}C_A\delta_{\rm src}e^{-\mu_Rd_+}=\eta_1A_b\le A_b/3\). ∎

*Remark (what is new against TD Lemma 2 and TD2 Lemma 8).* TD Lemma 2 expands at \(s=\mathbf1\). TD2 Lemma 8 holds \(X_f\) at one and bounds the switch cubes only by \(D^{-|V|}\), with no distance. Here the base \(N\) is expanded too, except for \(B_b\). So the switch cubes in \(A\) sit inside a connected set rooted at the read cube \(\Delta_b\), and they pay the tree length from the read.

### 4.3 Two labels per cube

**Lemma 4.2 (two-label composition)** [P; TD Lemma 3 with labels]. Let \(\Lambda\) be a finite label set with a map \(\pi\) to cubes, at most two labels per cube. Let \(\Phi\) be holomorphic on \(h_0+\{v:n_b(v)<A_b/4\ (b\in\mathcal B)\}\) with \(|\Phi-\Phi(h_0)|\le\omega\), and \(X=\{\Delta_b:b\in\mathcal B\}\). Let \(a_J\ge12\), \(0<\beta_\lambda<\delta_J\), and fixed shifts \(g_{\Lambda'}\), \(\varnothing\ne\Lambda'\subset\Lambda\), with
\[
 n_b(g_{\Lambda'})\le\tfrac{A_b}4\prod_{\lambda\in\Lambda'}\beta_\lambda\,e^{-a_J\operatorname{MST}(\pi\Lambda'\cup\{\Delta_b\})}.
\]
For \(F(t)=\Phi(h_0+\sum_{\Lambda'\ne\varnothing}t^{\Lambda'}g_{\Lambda'})\),
\[
 |D_\Lambda F(\mathbf1)|\le\omega\prod_{\lambda\in\Lambda}\frac{2\beta_\lambda}{\delta_J}\,e^{-(a_J-6)m_X(\pi\Lambda)} .
\]

*Proof.* Form the complete graph on \(\Lambda\cup\{*\}\) with \(w(\lambda,\lambda')=d(\pi\lambda,\pi\lambda')\) and \(w(\lambda,*)=d(\pi\lambda,X)\). Its MST value is \(m_X(\pi\Lambda)\): two labels of one cube are joined at weight \(0\), and merging them changes no other weight. Bird's allocation (TD (10)) gives parent costs \(l_\lambda\) with \(\sum_\lambda l_\lambda=m_X(\pi\Lambda)\) and \(\sum_{\lambda\in\Lambda'}l_\lambda\le\operatorname{MST}(\Lambda'\cup\{*\})\le\operatorname{MST}(\pi\Lambda'\cup\{\Delta_b\})\) for every \(b\) (TD 106). Take radii \(r_\lambda=(\delta_J/\beta_\lambda)e^{(a_J-6)l_\lambda}>1\). On \(|t_\lambda|\le r_\lambda\) each shift term is at most \((A_b/4)\delta_J^{|\Lambda'|}e^{-6\operatorname{MST}(\pi\Lambda'\cup\{\Delta_b\})}\). Group the \(\Lambda'\) by \(Z=\pi\Lambda'\): at most \(3^{|Z|}\) label sets project onto \(Z\), and \(\delta_J^{|\Lambda'|}\le\delta_J^{|Z|}\). So the total is at most \((A_b/4)\sum_{Z\ne\varnothing}(3\delta_J)^{|Z|}e^{-6\operatorname{MST}(Z\cup\{\Delta_b\})}\le(A_b/4)\cdot2\sum_{n\ge1}(2e\delta)^n=(A_b/4)\cdot\frac23\), by TD (9) and \(3\delta_J=\delta\). So \(F\) is admitted on the polydisc. The function \(\sum_{\Lambda''\subset\Lambda}(-1)^{|\Lambda\setminus\Lambda''|}[F(t\mathbf1_{\Lambda''})-\Phi(h_0)]\) vanishes on every hyperplane \(t_\lambda=0\) and is bounded by \(2^{|\Lambda|}\omega\). Repeated Schwarz at \(t=\mathbf1\) gives \(2^{|\Lambda|}\omega\prod r_\lambda^{-1}\). ∎

### 4.4 The theorem

**(5-N)** For the base \(N\) and an island term: \(A_f-\operatorname{Re}\Phi_f(P,h(\mathbf1_N;P,S(v_0)))\le B_f^N\) on \(\mathcal O_\sigma(U)\). Put \(\omega^N_f=2b_f\) (two-sided), \(\omega_f\) (kept forms), \(2B_f^N\) (islands).

**Theorem 2 ((JC\(_\tau\)))** [P from R, A with complete stencils, (5-N), (TJ)]. Let \(5\le\tau\le2a-24\), \(\vartheta<2/3\). Then on \(|\zeta|_c\le\mathfrak b\), uniformly in \(P\),
\[
 |f_{W,V}(P;\zeta)|\le\omega^N_f\prod_{c\in W}\frac{2\beta_c(\zeta)}{\delta_J}\,\big(48e^{1-\tau}\big)^{|V|}\,e^{-(a-6-\tau/2)\,m_{X(f)}(W\cup V)} .
\]
Also \(f_{W,V}=0\) unless \(W\subset N\cup V\) and every \(v\in V\) is joined to some \(B_b\) inside \(N\cup V\).

*Proof.* Labels: \((c,t)\) for \(c\in W\), \((v,\sigma)\) for \(v\in V\); \(\beta_{(c,t)}=\beta_c(\zeta)\), \(\beta_{(v,\sigma)}=e^{-\tau}\); \(a_J=a-\tau/2\ge12\). Shifts \(g_{\Lambda'}=g_{B,A}\) with \(B,A\) the two parts. Put \(\widehat g(t,\sigma)=\sum t^B\sigma^Ag_{B,A}\) and \(\widehat F=\Phi_f(P,\widehat g)\). At corners \(\widehat g(\mathbf1_{B'},\mathbf1_{A'})=g(\mathbf1_{B'},\mathbf1_{A'})\), so \(f_{W,V}=D_\Lambda\widehat F(\mathbf1)\).

*Coefficient form.* Since \(A\subset V\) misses \(N\ni\Delta_b\) and its cubes are distinct, a tree containing \(A\cup\{\Delta_b\}\) has at least \(|A|\) edges: \(|A|\le\operatorname{St}(B\cup A\cup\{\Delta_b\})\). With \(Q^{\operatorname{St}}=e^{-2a\operatorname{St}}\) and \(\operatorname{MST}\le2\operatorname{St}\) (TD Lemma 1),
\[
 Q^{\operatorname{St}}\le e^{-\tau|A|}e^{-(2a-\tau)\operatorname{St}}\le e^{-\tau|A|}e^{-(a-\tau/2)\operatorname{MST}} .
\]
For \(B\ne\varnothing\), Lemma 4.1(b) and \(4A_R/A_V\le K_1\) give \(n_b(g_{B,A})\le(A_b/4)K_1\prod_{c\in B}(2|\zeta|_c/\varrho)Q^{\operatorname{St}}\le(A_b/4)\prod_{c\in B}\beta_c\prod_{v\in A}e^{-\tau}e^{-a_J\operatorname{MST}}\), because \(K_1\ge1\) and \(|B|\ge1\). For \(B=\varnothing\), Lemma 4.1(c) and (TJ) give the same form. The cube set in the MST is \(B\cup A\), which is \(\pi\Lambda'\).

*Base.* By Lemma 4.1(d) \(n_b(h_0^N)\le A_b/3\), \(h_0^N:=h(\mathbf1_N;P,S(v_0))\). As in TD Lemma 4 (TD 170), the radius-\(A_b/4\) ball about \(h_0^N\), even doubled radially, lies in \(\mathcal A_f(P)\). Two-sided and kept bounds give \(\omega=\omega^N_f\) directly; for an island, \(\psi(z)=\Phi_f(P,h_0^N+zv)-\Phi_f(P,h_0^N)\) has \(\operatorname{Re}\psi\le B_f^N\) by (5-N), and Borel–Carathéodory at \(1/2\) gives \(|\psi(1)|\le2B_f^N\).

*Conclusion.* Lemma 4.2 with \(X=X(f)\) gives the bound, with \(2e^{-\tau}/\delta_J=48e^{1-\tau}\) and \(a_J-6=a-6-\tau/2\); \(\beta_c<\delta_J\) because \(\beta_c\le\delta\vartheta/2<\delta/3\). The support statement: Step 4 of Lemma 4.1 kills \(W\not\subset N\cup V\); if all coefficients with \(v\in A\) vanish, \(\widehat F\) does not depend on \(\sigma_v\) and \(D_\Lambda\widehat F=0\); Lemma 4.1(a) says when they vanish. ∎

*Two members of the family.* \(\tau=12\): factor \((48e^{-11})^{|V|}\), rate \(a-12\) (TD2d's rate). \(\tau=a\): factor \(48e\,(6400/D)^{1/2}\) per switch cube, that is \((C_*/D)^{|V|/2}\) with \(C_*=6400(48e)^2\), and rate \(a/2-6\). TD2d's (JC) asks for both at once and is not proved here; it is not needed.

**Lemma 4.3 ((5-N) from (5))** [P from TD's (5) at \(s=\mathbf1\), R, (TJ)]. For every \(N\supset X_f\), (5-N) holds with \(B_f^N=3B_f\).

*Proof.* Fix \(b\). By Step 1 at \(z=0\), \(\varphi(\mathbf1)-\varphi(\mathbf1_N)=\sum I_{Y'}\) over \(Y'\not\subset N\). Each surviving \(Y=B_b\cup Y'\) is connected, contains \(\Delta_b\) and a cube outside \(N\), so \(|Y|\ge d(\Delta_b,\mathcal P\setminus N)+1\ge2\). Steps 5–6 give \(n_b(h_0-h_0^N)\le(A_b/4)\,\epsilon\) with \(\epsilon:=8\eta_1D^{15}Q^{d(\Delta_b,\mathcal P\setminus N)}\le1\) by (TJ), uniformly in \(b\) after taking the minimum distance. If \(\epsilon=0\) there is nothing to prove. Otherwise let \(v=(h_0^N-h_0)/\epsilon\), so \(n_b(v)\le A_b/4\), and \(\psi(z)=\Phi_f(P,h_0+zv)-\Phi_f(P,h_0)\) on \(|z|<2\). The points \(h_0+zv\) lie in \(\mathcal A_f\) since \(n_b(h_0)\le A_b/3\). TD (5) and \(\operatorname{Re}\Phi_f\le A_f\) give \(\operatorname{Re}\psi\le B_f\). The Schwarz argument of TD 170 gives \(|\psi(2w)|\le2B_f|w|/(1-|w|)\) for \(|w|<1\); at \(2w=\epsilon\le1\), \(|\psi(\epsilon)|\le2B_f\epsilon\). Hence \(A_f-\operatorname{Re}\Phi_f(P,h_0^N)\le B_f+2B_f\epsilon\le3B_f\). ∎

So the switched-polydisc part of (5-sw) is not used anywhere, and its corner part reduces to TD's own Outstanding (5).

### 4.5 Against TD2 (23)–(26)

- TD2 (23)–(24) are the valid finite estimates for the base \(X_f\) (TD2 Correction 9). Theorem 2 replaces (24): it needs no switched amplitude \(\omega^{\rm sw}\), no geometric mean, and no connectivity of \(X_f\); it needs the complete stencils that TD2 requires and one corner amplitude, which Lemma 4.3 supplies.
- TD2 (25)–(26) refute the summation of a majorant decaying in \(m_C\), the MST with the collar \(C\) collapsed: a cube just outside \(C\) has root weight \(1\), so \(N\sim D_H^3\) face cubes give \((1+te^{-(a-12)})^N\) (TD2 333–341). Theorem 2's majorant decays in \(m_{X(f)}\), the MST rooted at the **reads**. A face cube \(v\) outside a collar of width \(\rho\) around an island hub has root weight \(d(v,X(f))\ge\rho+1\). A whole cluster of attached cubes pays that root weight once, and its other cubes pay the per-switch factor and their edges. Lemma 5.1 sums this. This is the "stronger joint estimate, matching the original reads" that TD2 341 asks for. TD2's own lower bound (26) does not apply to it: for TD2's family the sum of Theorem 2's majorant is bounded by \(\exp(2q\,\Xi)\), with \(\Xi\) the read-rooted shell sum of Lemma 5.1, which is at most \(16(D_H+O(\rho))^3e^{-12(\rho+1)}\).

---

## 5. The P-labelled bookkeeping

This section answers TD2 Correction 10: it gives a summation of the pieces \(f_{W,V}\) that keeps the collar-width decay, with SA's literal relative length, for a collar proportional to the hub. It uses TD2d's ordinary-distance results as distilled in TD2 (Theorem 3 there): (X°), G, (G-ord), and TD2d Lemmas 3.1–3.2. Notation: \(T_f\) the (X°) tree, \(\operatorname{Hub}(f)\) the hubs that \(T_f\) meets, \(\widetilde H^+=N_{c_{\rm col}}(\widetilde H)\), \(s_H\le D_H+2c_{\rm col}\) the side of the least box containing \(\widetilde H^+\) (it does not wrap, SA 17583).

### 5.1 The base and its geometry

Fix \(\eta\in(0,\eta_{\max}]\), \(\eta_{\max}:=1/(16(C_{\rm isl}+1)L)\), to be chosen in Theorem 3. For a hub put
\[
 \rho_H=\lceil\eta s_H\rceil,\qquad \widehat H=N_{\rho_H+2}(\widetilde H^+),\qquad \widehat H^+=N_1(\widehat H)=N_{\rho_H+3}(\widetilde H^+),
\]
and for an exempt term \(N_f:=X_f\cup\bigcup_{\widetilde H\in\operatorname{Hub}(f)}\widehat H\). The members of the excused family are the \(\widehat H^+\) [design].

**Lemma 5.0 (collar geometry)** [P from G (TD 73), (G-ord), under ceilings on \(\gamma\)]. If \(\check R_i\ge64+8c_{\rm col}\) and \(D_H\ge2c_{\rm col}\): (i) distinct members are disjoint, at distance at least \(s_0/2\); (ii) every gas cube has distance at least \(G_0/2\) from every member; (iii) a member lies in a non-wrapping box of side at most \((1+3\eta)s_H+8\).

*Proof.* \(\rho_H+3+c_{\rm col}\le\eta(C_{\rm isl}L\check R_i+6+2c_{\rm col})+4+c_{\rm col}\le\check R_i/16+6+2c_{\rm col}\), since \(\eta C_{\rm isl}L\le1/16\) and \(\eta(6+2c_{\rm col})\le1+c_{\rm col}\). (i) Hubs are at distance \(\ge s_0=\check R_i-4\), and \(2(\check R_i/16+6+2c_{\rm col})\le s_0/2\) under the ceiling. (ii) \(G_0=10L\check R_i-2\ge2(\check R_i/16+6+2c_{\rm col})\). (iii) Add \(2(\rho_H+3)\le2\eta s_H+8\) to \(s_H\). ∎

**Proposition 5.1′ (pieces and their pair-carriers)** [P from Proposition 4.0, Theorem 1, Corollary 1′, A]. With \(N=N_f\): \(f_W=\sum_{V\subset\mathcal P\setminus N_f}f_{W,V}\) exactly, and \(f_{W,V}\) is a function of \(P|_{Y_{f,V}}\), \(Y_{f,V}:=N_1(N_f\cup V)\), holomorphic on the image of restriction, with the bound of Theorem 2.

*Proof.* At a corner \(s_A=\mathbf1_{N_f\cup A}\) the response on every component of \(N_f\cup A\) reads the pair only on that component (Theorem 1), the source rows add one layer (Corollary 1′), and \(\Phi_f\) reads the pair on \(X_f\subset N_f\), including its pins (A's complete reads, TD 51–61). A finite alternating sum of functions of \(P|_{Y_{f,V}}\) is one. Holomorphy: Theorem 1(iii) at each corner. ∎

### 5.2 A read-rooted forest sum

For a nonempty cube set \(R\) and a finite set \(V\) of cubes, \(m_R(V)\) is the MST of \(V\cup\{*\}\) with \(w(v,v')=d(v,v')\), \(w(v,*)=d(v,R)\); \(m_R(\varnothing)=0\).

**Lemma 5.1 (read-rooted forests)** [P]. Let \(s\ge6\), \(0<q\le1/(4e)\), \(\mathcal V\) a finite set of cubes, and \(\Xi:=\sum_{v\in\mathcal V}e^{-s\,d(v,R)}\). Then
\[
 \sum_{V\subset\mathcal V}q^{|V|}e^{-s\,m_R(V)}\le\exp(2q\,\Xi).
\]

*Proof.* A spanning tree of \(V\cup\{*\}\) rooted at \(*\) is a rooted forest on \(V\) whose roots are joined to \(*\). The MST is one such forest, so \(e^{-sm_R(V)}\le\sum_F\prod_{v\in V}e^{-s\,w(v,p_F(v))}\), the sum over all rooted forests \(F\) on \(V\), with \(p_F(v)\) the parent of \(v\) (\(*\) for a root). Writing \(V\) as \(n!\) orderings of distinct points and then dropping distinctness,
\[
 \sum_{|V|=n}q^ne^{-sm_R(V)}\le\frac{q^n}{n!}\sum_{F\text{ on }[n]}\ \sum_{v_1,\dots,v_n}\prod_ie^{-s\,w(v_i,v_{p_F(i)})},
\]
with \(v_i\in\mathcal V\) for roots and \(v_i\) ranging over all cubes otherwise (an upper bound). For fixed \(F\), sum the positions from the leaves inward: a non-root vertex contributes \(\sum_ve^{-sd(v,v_{p})}\le2\) (TD (9), \(s\ge6\)); a root contributes \(\Xi\). So the forest \(F\) gives at most \(\Xi^{k(F)}2^{n-k(F)}\), \(k(F)\) its number of trees. By the exponential formula for labelled forests, \(\sum_n\frac{q^n}{n!}\sum_F\Xi^{k(F)}2^{n-k(F)}=\exp\big(\sum_{m\ge1}\frac{q^m}{m!}m^{m-1}\Xi\,2^{m-1}\big)\), since there are \(m^{m-1}\) rooted labelled trees on \(m\) vertices. With \(m^{m-1}/m!\le e^{m-1}\) the exponent is at most \(q\Xi\sum_{m\ge1}(2eq)^{m-1}\le2q\Xi\). ∎

*Why this keeps the collar-width decay.* The root weight is the distance to the reads. A cluster of attached cubes pays it once, at its root child; its other cubes pay \(q\) and their edges. TD2 (26) is the same sum with \(R\) replaced by the collar \(C\): then \(\Xi\ge N\) for \(N\) cubes on a face of \(C\), and the bound is \(e^{2qN}\), unbounded, as TD2 says. With \(R=X(f)\) and attachments outside \(N_f\), \(\Xi\) is a shell sum beyond distance \(\rho_H+2\) (Theorem 3, step (i)).

### 5.3 The relative length of a carrier

\(\ell^{\rm rel}(Y)\) is SA's relative length in fine-cube units with the family \(\mathsf H=\{\widehat H^+\}\), literal reading (TD Proposition 11, TD2d §1.1): the least edge count, over subfamilies \(\mathsf F\) of members contained in \(Y\), of a tree in the fine graph that meets every cube of \(Y\) outside \(\bigcup\mathsf F\) and meets each member of \(\mathsf F\). Crossings of members are charged.

**Lemma 5.2 (carrier length)** [P from (X°), G, Lemma 5.0]. Let \(m=m_{X(f)}(W\cup V)\), \(V\subset\mathcal P\setminus N_f\), \(W\subset N_f\cup V\) nonempty gas. Then
\[
 \ell^{\rm rel}(Y_{f,V})\le C_4(1+d_f)+(81+c_{\rm col}+1/\eta)\,m+c_{\rm col}|W|,\qquad C_4:=C_{\rm pr}+(2c_{\rm col}+3)^4(C_{\rm pr}+1).
\]

*Proof.* Take \(\mathsf F=\{\widehat H^+:\widetilde H\in\operatorname{Hub}(f)\}\); each is contained in \(Y_{f,V}\supset N_1(N_f)\). Build \(U\) from:

1. \(T_f\), with at most \(C_{\rm pr}(1+d_f)\) edges; it meets each \(\widetilde H\subset\widehat H^+\) of \(\mathsf F\).
2. For each vertex \(y\) of \(T_f\), a spanning tree of the ball \(N_{c_{\rm col}+1}(y)\): at most \((2c_{\rm col}+3)^4(C_{\rm pr}+1)(1+d_f)\) edges. By (X°)(a) every cube of \(X_f\) is within \(c_{\rm col}\) of \(T_f\) or lies in \(\widetilde H^+\) for \(\widetilde H\in\operatorname{Hub}(f)\); so every cube of \(N_1(X_f)\) outside \(\bigcup\mathsf F\) is met.
3. The fine subgraph \(Q\) of TD Lemma 1(3) for \(W\cup V\) rooted at \(X(f)\): at most \(m\) edges; it joins every cube of \(W\cup V\) to a root point \(x_c\in X(f)\) of a root child \(c\).
4. Connectors from each \(x_c\) to \(T_f\), as in TD2d Lemma 3.1. Case 1, \(x_c\) within \(c_{\rm col}\) of \(T_f\): at most \(c_{\rm col}\) edges. Case 2, \(x_c\in\widetilde H^+\) with \(\widetilde H\in\operatorname{Hub}(f)\): a path of at most \(s_H\) edges inside the box of \(\widetilde H^+\) to a vertex of \(T_f\cap\widetilde H\). In Case 2 the parent cost is \(l_c=d(c,x_c)\ge\rho_H+3\ge\eta s_H\): if \(c\in V\), because \(c\notin\widehat H\); if \(c\in W\), because gas cubes are at distance \(\ge G_0-c_{\rm col}\) from hubs. So Case 2 costs at most \(\sum_cs_H\le\eta^{-1}\sum_cl_c\le m/\eta\). Case 1 costs at most \(c_{\rm col}|W\cup V|\).
5. For each \(v\in V\), the star of its \(80\) neighbours: \(80|V|\) edges. Each \(v\notin X(f)\) has parent cost \(\ge1\), so \(|V|\le m\).

\(U\) is connected: every component of \(Q\) contains a root child, joined to \(T_f\) by its connector; the stars hang on vertices of \(U\). It meets every cube of \(Y_{f,V}=N_1(N_f)\cup N_1(V)\) outside \(\bigcup\mathsf F\): \(N_1(\widehat H)=\widehat H^+\in\mathsf F\); \(N_1(X_f)\) by item 2; \(N_1(V)\) by item 5. Cubes of other members that \(Y_{f,V}\) meets lie in \(N_1(V)\) or \(N_1(X_f)\) and are met. A spanning tree of \(U\) is admissible, and \(|W\cup V|\le|W|+m\). ∎

### 5.4 The filing bound

**Theorem 3 ((File-P°))** [P from Theorem 2 with \(\tau=a\), Lemmas 4.3, 5.0–5.2, (X°), G, (G-ord), X, RUN, TD2d Lemmas 3.1–3.2]. Let \(r:=a/2-6\), \(q:=48e^{1-a}\), \(\eta:=4\lambda_P/r\), and assume

- (F1) \(\lambda_PC_4\le\kappa/16\) and \(\lambda_TC_{\rm pr}\le\kappa/4\) (TD2d (T1));
- (F2) \(r/2\ge\lambda_P(81+c_{\rm col})+2\lambda_T(1+\eta_H)\) and \(r\ge96\);
- (F3) \(\eta\le\eta_{\max}\), i.e. \(r\ge64\lambda_P(C_{\rm isl}+1)L\);
- (F4) \(2q\,[2(2c_{\rm col}+1)^4(C_{\rm pr}+1)+16(C_{\rm pr}+1)\Theta_\eta]\le\kappa/16\), with \(\Theta_\eta:=\sup_{x\ge0}\big((1+2\eta)x+2c_{\rm col}+9\big)^3e^{-12\eta x}\);
- the ceilings (TJ), \(\vartheta<2/3\), \(\vartheta_P:=6\vartheta e^{(\lambda_P+\lambda_T)c_{\rm col}+1}<1\), those of Lemma 5.0, and TD2d (T4).

Then for every nonempty set \(W\) of gas cubes, every \(P\in\mathcal O_\sigma(U)\) and \(|\zeta|_c\le\mathfrak b\),
\[
 \sum_{f\ \rm exempt}\ \sum_{V\subset\mathcal P\setminus N_f}\ \sup|f_{W,V}|\;e^{\lambda_P\ell^{\rm rel}(Y_{f,V})}\le a_P\,e^{-\lambda_Td_f(W)},\qquad
 a_P:=6e^{\kappa/2}\vartheta_P\,N_{\rm ex}\,e^{-\nu_g(G_0-C_{\rm pr}-2c_{\rm col})},
\]
with \(\nu_g=\min\{\kappa/(8C_{\rm pr}),3\}\). Under RUN, \(a_P\to0\) as \(\gamma\downarrow0\), all earlier constants fixed.

*Proof.* Fix \(f\), \(V\) with \(f_{W,V}\ne0\) (so \(W\subset N_f\cup V\)) and put \(m=m_{X(f)}(W\cup V)\). Theorem 2 (\(\tau=a\), allowed since \(r\ge96\) gives \(a\ge24\)) and Lemma 4.3 (\(\omega^{N_f}_f\le3\widetilde\omega_f\le3\widehat\omega_fe^{-\kappa d_f}\)) give
\[
 |f_{W,V}|\le3\widehat\omega_fe^{-\kappa d_f}(3\vartheta)^{|W|}q^{|V|}e^{-rm},
\]
since \(2\beta_c/\delta_J=6\beta_c/\delta\le3\vartheta\). Lemma 5.2 and \(\lambda_P/\eta=r/4\) give
\(e^{\lambda_P\ell^{\rm rel}}\le e^{\lambda_PC_4(1+d_f)}e^{[\lambda_P(81+c_{\rm col})+r/4]m}e^{\lambda_Pc_{\rm col}|W|}\).
TD2d Lemma 3.1 gives \(d_f(W)\le(1+\eta_H)m_{X(f)}(W)+C_{\rm pr}(1+d_f)+c_{\rm col}|W|\), and \(m_{X(f)}(W)\le2m\): in the metric \(d_X(c,c')=\min\{d(c,c'),d(c,X)+d(c',X)\}\) with \(X\) collapsed, which has the same MST values, the MST is at most twice the Steiner length, and the Steiner length is monotone in the terminal set. By (F1)–(F2) the product is at most
\[
 3e^{5\kappa/16}\widehat\omega_fe^{-(11\kappa/16)d_f}\,\big(3\vartheta e^{(\lambda_P+\lambda_T)c_{\rm col}}\big)^{|W|}\,q^{|V|}e^{-(r/4)m},\qquad r/4\ge24 .
\]
Split \(e^{-24m}=e^{-12m}e^{-6m}e^{-6m}\).

(i) *Sum over \(V\).* Write \(V=V_W\sqcup V'\) with \(V_W=V\cap W\) (at most \(2^{|W|}\) choices, \(q^{|V_W|}\le1\)). Contracting \(W\cup V_W\) into the root lowers the MST, so \(m\ge m_R(V')\) with \(R=X(f)\cup W\). Lemma 5.1 with \(s=12\), \(\mathcal V=\mathcal P\setminus(N_f\cup W)\), gives \(\sum_{V'}q^{|V'|}e^{-12m_R(V')}\le\exp(2q\Xi_R)\), and \(\Xi_R\le\Xi_X+2|W|\), \(\Xi_X=\sum_{v\notin N_f}e^{-12d(v,X(f))}\). Split \(X(f)=X_1\cup X_2\), \(X_1\) within \(c_{\rm col}\) of \(T_f\), \(X_2\subset\bigcup_{\operatorname{Hub}(f)}\widetilde H^+\) ((X°)(a)). Then \(\sum_ve^{-12d(v,X_1)}\le2|X_1|\le2(2c_{\rm col}+1)^4(C_{\rm pr}+1)(1+d_f)\). For \(X_2\): \(v\notin N_f\) has \(d(v,\widetilde H^+)\ge\rho_H+3\) for each \(\widetilde H\in\operatorname{Hub}(f)\); the cubes at distance \(n\) from the box of \(\widetilde H^+\) number at most \(8(s_H+2n)^3\), and consecutive terms of \(\sum_{n\ge\rho_H+3}8(s_H+2n)^3e^{-12n}\) have ratio at most \(27e^{-12}<\frac12\), so each hub contributes at most \(16(s_H+2\rho_H+6)^3e^{-12(\rho_H+3)}\le16\Theta_\eta\) (use \(\rho_H\le\eta s_H+1\) and \(\rho_H\ge\eta s_H\)). There are at most \((C_{\rm pr}+1)(1+d_f)\) hubs in \(\operatorname{Hub}(f)\). By (F4), \(2q\Xi_X\le(\kappa/16)(1+d_f)\). The \(|W|\)-parts give \(2^{|W|}e^{4q|W|}\le e^{|W|}\).

(ii) *The gap.* With \(e^{-(\kappa/8)d_f}\) taken from the remaining \(e^{-(10\kappa/16)d_f}\): \(6m\ge3m_{X(f)}(W)\), and TD2d Lemma 3.2 gives \(m_{X(f)}(W)+C_{\rm pr}d_f\ge G_0-C_{\rm pr}-2c_{\rm col}\); so \((\kappa/8)d_f+6m\ge\nu_g(G_0-C_{\rm pr}-2c_{\rm col})\).

(iii) *Sum over \(f\).* Fix \(c_0\in W\); \(m\ge d(c_0,X(f))\) (TD Lemma 1(3)). Assign \(f\) to a nearest read cube. TD (6) and (9) give \(\sum_f\widehat\omega_fe^{-(\kappa/2)d_f}e^{-6d(c_0,X(f))}\le2N_{\rm ex}\).

Collecting: \(3e^{5\kappa/16+\kappa/16}\cdot\vartheta_P^{|W|}\cdot e^{-\nu_g(G_0-C_{\rm pr}-2c_{\rm col})}\cdot2N_{\rm ex}\le a_P\), since \(\vartheta_P^{|W|}\le\vartheta_P\). *Limit*: as in TD2d Theorem A (TD2d 193): \(N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}\), \(G_0\ge10L(\ell-1)^r-2\), \(\vartheta\to0\). ∎

*Remark (the choice \(\tau=a\)).* (F4) needs \(q\,\Theta_\eta\) small. \(\Theta_\eta\le4(2c_{\rm col}+9)^3+4(1+2\eta)^3(4e\eta)^{-3}\) grows like \(\eta^{-3}\sim(r/\lambda_P)^3\), polynomially in \(\bar\kappa\), while \(q=48e^{1-a}\) decays like \(e^{-\bar\kappa/2}\). So (F4) is a floor on \(\bar\kappa\). With \(\tau=12\) the factor \(q\) would be a fixed number and (F4) would fail for large \(\bar\kappa\): the per-switch factor \(D^{-1/2}\) of TD2d's (JC) is what pays the hub shell of small islands.

### 5.5 Class terms and the labelled cluster expansion

**Proposition 5.3 (pair-carriers of class terms)** [P from Theorem 1, Corollary 1′]. CI's switched presentation (CI 197: "For \(Y\supset X_f\), set switches to zero off \(Y\), to one on \(X_f\), and to \(s\in[0,1]^{Y\setminus X_f}\) elsewhere. Define \(f_Y\) by integrating the mixed switch derivative of \(F_f-f_0\)") gives pieces \(f_Y\) that are functions of \(P|_{N_1(Y)}\). *Proof.* At every switch vector in the integral, \(\operatorname{supp}s\subset Y\); Theorem 1 and Corollary 1′ make the response on each component a function of the pair on \(N_1\) of that component; \(\Phi_f\) reads \(X_f\subset Y\). Switch derivatives and integrals of such functions are such functions. ∎ This answers TD2d's remark (TD2d 362) that the same question arises for class terms. For connected \(Y\), \(\ell^{\rm rel}(N_1(Y))\le81|Y|\le81(\operatorname{St}(Y)+1)\).

**(G-P)** [I, owner CI H-S / IN1]. The assigned Gaussian functional of a polymer union \(X\) of gas cubes reads the pair only on \(N_{c_G}(X)\), \(c_G\) geometric, and factorizes over separated supports. **[R]** D3L §2 proves this conditionally ("\(C,\Gamma\) read only the live region and split over wall-components", checked ADVANCE in `gates/d3-local-check.md`), given tagged precision and inverse-root walk series; IN1 329 shows that a path-decoupled global root does not have it. For a Definition-D-tagged precision \(A(s)=\sum_\omega s^\omega A_\omega\) (HW §9), Lemma 2.1 makes \(A(s)\) block-diagonal over wall-components with pair-local blocks, and the inverse of a block-diagonal matrix has the inverses of the blocks as blocks (D3L §2); the inverse root needs its own tagged series.

**Proposition 5.4 (labelled cluster expansion)** [P from (G-P) and CI Theorem 5's absolute majorants, as an implication]. Write every gas activity as \(z(W)=\sum_Yz(W,Y)\), \(z(W,Y)\) a function of \(P|_Y\), \(W\subset Y\), and define \(\|z\|_P(W)=\sum_Y\sup|z(W,Y)|e^{\lambda_P\ell^{\rm rel}(Y)}\). Suppose \(e^{\lambda_P(c_{\rm inc}+1+(2c_G+1)^4|W|)}\|z\|_P(W)\) satisfies the activity bounds that CI Theorem 5 uses for \(|z(W)|\), where \(c_{\rm inc}\) is the incompatibility range. Then every cluster logarithm is \(E(X)=\sum_YE(X,Y)\), \(E(X,Y)\) a function of \(P|_Y\), and \(\sum_Y\sup|E(X,Y)|e^{\lambda_P\ell^{\rm rel}(Y)}\) obeys CI (28)'s bound with the same constants.

*Proof.* In the union-filed cluster formula (TD 355–362), expand each factor \(z(W_j)=\sum_{Y_j}z(W_j,Y_j)\) and file each term at \(Y=\bigcup_jY_j\cup N_{c_G}(X)\), \(X=\bigcup_jW_j\). The Gaussian integral is over fluctuation variables at fixed pair, so the term is a function of \(P|_Y\) by (G-P). Along an incompatibility tree, consecutive \(W_j\) lie within \(c_{\rm inc}\), and \(W_j\subset Y_j\); joining the trees of the \(Y_j\) costs at most \(c_{\rm inc}+1\) per join. The cubes of \(N_{c_G}(X)\) lie at distance \(\ge G_0/2-c_G\) from every member (Lemma 5.0(ii)), so they are outside \(\bigcup\mathsf H\); stars at the cubes of \(X\), which the trees already meet, cost at most \((2c_G+1)^4|X|\le(2c_G+1)^4\sum_j|W_j|\). Hence \(e^{\lambda_P\ell^{\rm rel}(Y)}\le\prod_je^{\lambda_P(\ell^{\rm rel}(Y_j)+c_{\rm inc}+1+(2c_G+1)^4|W_j|)}\). CI Theorem 5's convergence proof uses only absolute values of the activities and the tree-graph bound (TD 360–362; TD2 Theorem 9's proof: "These lemmas' Gaussian, collar, selection and tree estimates are uniform in the external parameter"). Replacing \(|z(W_j)|\) by the hypothesised majorant reproduces CI (28) for \(\sum_Y\sup|E(X,Y)|e^{\lambda_P\ell^{\rm rel}(Y)}\). ∎

*Feeding Theorem 3 into Proposition 5.4.* Theorem 3 bounds \(\|V^{\rm ex}\|_P(W)\) by \(a_Pe^{-\lambda_Td_f(W)}\). Corollary A′'s regrouping on connected supports (TD2d 195–204; TD2 Corollary 4 with its factor two) keeps the labels. The extra factor \(e^{\lambda_P(c_{\rm inc}+1+(2c_G+1)^4|W|)}\) is paid by the unit slack \(\lambda_T-\lambda_V=1\) once \(\lambda_P(2c_G+1)^4\le1/4\) and \(|W|\le d_f(W)+1\). So \(\lambda_P:=\min\{\kappa/(16C_4),\,(4(2c_G+1)^4)^{-1}\}\), fixed after \(\kappa\), before \(\bar\kappa\), independent of \(M\).

---

## 6. What remains of CI

### 6.1 The list

After this note, CI at an exempt main step (TD2 Theorem 9) needs, besides the imports already named in TD and TD2 (R, A, X, G, RUN, (X°), (G-ord), J°, the ordinary potential bounds, CI-base and the formation packages):

1. **(5)**, the complex island amplitude at \(s=\mathbf1\) [O, owner NL1-L/PAN; TD 63]. Lemma 4.3 reduces every corner amplitude used here to it.
2. **DR-lane imports of Theorem 1** [I, owner ST1/DR lane]: (UNQ) (DF Proposition 5.1 from [PW], [NL]); the identification [RED] of the consumer's \(\mathsf W_s\) with NR9 (4.4) (NR9 61); (D2′); and (UNQ-loc) for the full declared local domains.
3. **(S-loc)** for the completed source, stored data and pins [I, owner ST1/NL1].
4. **(G-P)**, pair-heredity of the assigned Gaussian [I, owner CI H-S/IN1].
5. **(Cls)**, the class matching [O, owner IN1/LF1] — §6.2.
6. TD2 Theorem 9's remaining filing clauses: restriction, overlap and covariance of the chosen carriers \(Y_{f,V}\) (they are built from \(T_f\) and the hubs; covariance needs a covariant choice of \(T_f\)), and the scale/hull comparison. Exact regrouping with summable multiplicity is Proposition 5.1′ with Theorem 3. [O/I, owner NL1-L/LF1].

### 6.2 The first remaining Outstanding statement: (Cls)

> **(Cls)** [O, owner IN1/LF1]. Replace, in IN1's class \(\mathfrak L_k(\theta)\) (IN1 217–219, boundary bound (12), IN1 131–134) and in TD's X, (X°) and G, the excused family of SA 6196 ("the level-\(j\) hulls of its standing islands") by \(\mathsf H_i=\{\widehat H_i^+(X)=N_{\rho_H(i)+3}(\widetilde H_i^+(X))\}\), \(\rho_H(i)=\lceil\eta s_H(i)\rceil\), with SA's literal relative length. Then IN1's class induction holds with \(C_{\rm isl}\) replaced by \(2C_{\rm isl}\) and all other constants unchanged.

*What is proved toward (Cls).* The producer side is Theorem 3 with Proposition 5.4: the new terms obey (12) on their filed carriers with this family. On the consumer side [P, sketch], TD2d Theorem A runs with \(\widehat H^+\) as hubs: Lemma 5.0 gives separation \(s_0/2\), gap \(G_0/2\), and box side \(\le(1+3\eta)s_H+8\le2D_H\), so (G-ord) holds with \(2C_{\rm isl}\), fixed early, since only \(\eta\le1/3\) is used. *Non-accumulation* [R, sketch]: a standing island is not moved (SA 19523), so in current fine units its hub side shrinks by \(L\) per step up to additive \(O(1)\), and \(\rho_H\) is proportional to it; a carrier \(N_{\rho_H(i)+3}(\widetilde H_i^+)\) of step \(i\), seen at step \(i+1\), lies in \(N_{(\rho_H(i)+3)/L+O(1)}(\widetilde H_{i+1}^+)\subset\widehat H_{i+1}^+\) once \(\eta O(1)+4/L\le2\), if hubs are monotone under coarsening (part of G-isl). The additive layers do not accumulate because each shrinks by \(L\) per step. *Not checked:* every other use of the excused family inside IN1's induction (island formation and its class rule, the per-cube sums (6) with the new lengths, the \(\mathbf R\) operation).

Three attacks on obtaining (Cls) without changing SA's family, that is, on proving \(\widehat H^+\) inside SA's excused member:

**Attack A — SA's family as written.** Excuse only the level-\(j\) hull \(H\). *Fails.* TD 73 sets \(\widetilde H=N_2(H)\), and (X°)(a) puts the island's read set \(X^\uparrow\) in \(\widetilde H^+=N_{2+c_{\rm col}}(H)\) (TD2d 99). So already the base piece \(f_{W,\varnothing}\) has a pair-carrier containing \(N_1(\widehat H)\), which leaves the hull along its whole boundary. A literal tree must meet every carrier cube outside \(H\): at least \(|\widehat H^+\setminus H|/81\ge c\,\eta\,s_H^4/81\) edges for a hub of side \(s_H\). The available decay is \(\widetilde\omega_f\) (no length decay for an island, TD 71) and the gap factor \(e^{-\nu G_0}\), with \(G_0\sim10L\check R_i\ll s_H^4\). *Exact reason:* SA's members contain no collar of the reads, and every piece's pair-carrier contains one.

**Attack B — the smallest enlargement: a logarithmic collar.** Take \(\rho_H=\lceil\frac14\log s_H\rceil\), the least width for which the hub shell sum \(16s_H^3e^{-12\rho_H}\) of Theorem 3(i) stays bounded, and members \(N_{\rho_H+3}(\widetilde H^+)\). *Fails with the literal length.* In Lemma 5.2, Case 2, the connector through the hub costs \(s_H\) while the attachment has paid only \(l_c\ge\rho_H+3\sim\frac14\log s_H\); the ratio \(s_H/\log s_H\) is unbounded, so \(\lambda_P\ell^{\rm rel}\) is not paid by \(e^{-rm}\). *Exact reason:* the literal relative length charges crossings of members, and two attachment clusters on opposite faces of a hub must be joined through or around it. With the contracted reading (members crossed free, TD's \(\ell^\natural\)) Lemma 5.2 holds without the \(m/\eta\) term and the logarithmic collar closes; but TD Proposition 11 fixes the literal reading of SA's class, and TD2d Proposition 6 (TD2 Correction 5) shows the contracted premise does not give ordinary decay. [R, not proved: a mixed pair-difference lower bound, as in TD2d Lemma 6.0, should show that every exact pair-local decomposition of an island term has pieces joining attachment points on opposite faces, so this failure is not an artefact of the construction.]

**Attack C — SA's ten-cell box.** At formation \(\Omega_i^c\cap X=H_i^{[8]}\) and \(Z_i\cap X=H_i^{[10]}\) (SA 17579–17580), so the island component carries a margin of two level-\(i\) cells, far more than \(\rho_H\le\eta s_H+1\). Try to place \(\widehat H^+\) inside that margin. *Fails.* The margin lies inside the island component \(X\), between \(H_i^{[8]}\) and its boundary. The island term's external reads are at and beyond \(\partial X\) (its read enlargement \(X^\uparrow\supset X\)), so their collar lies outside \(X\). After the formation window, SA 19523 refers the island's bounds to its creation level, and no line states a later margin (TD2d §5.4, "A separation I could not source"). *Exact reason:* SA's margin is interior to the island; the needed collar is exterior to its reads.

So (Cls) is a definition change in frozen IN1, not a consequence of SA's text. It is the first Outstanding statement on CI's path after this note.

---

## 7. Constant order

"Early" means fixed before \(\kappa\), independent of \(M\) and \(\bar\kappa\).

| Constant or condition | Where fixed | Before \(\kappa\)? | Independent of \(M,\bar\kappa\)? |
|---|---|---|---|
| \(c_P=0\) (\(1\) with sources) | — | yes | yes |
| \(\rho_{\mathbf B}=3LM_1\), \(r_0\), (Bud) | rows 2–3 | yes | yes |
| \(\delta_J=(24e)^{-1}\), \(48e\), \(16\), \(81\), \(\Theta\)-shell constants | numbers | yes | yes |
| \(C_4\), \(c_{\rm col}\), \(C_{\rm pr}\), \(C_{\rm isl}\) (doubled under (Cls)) | row 2 | yes | yes |
| \(c_G\), \(c_{\rm inc}\) | row 2 (H-S, CI) | yes | yes |
| \(\lambda_P=\min\{\kappa/(16C_4),(4(2c_G+1)^4)^{-1}\}\) | after \(\kappa\) | no | yes |
| \(\tau=a\); \(r=a/2-6\); \(q=48e^{1-a}\); \(\eta=4\lambda_P/r\) | with \(\bar\kappa\) | no | depend on \(\bar\kappa\); read only by (F2)–(F4) floors and \(\gamma\)-ceilings |
| (F2), (F3), (F4) | floors on \(\bar\kappa\) | — | independent of \(M\) |
| (TJ), \(\vartheta<2/3\), \(\vartheta_P<1\), Lemma 5.0, (T4) | ceilings on \(\gamma\) | — | — |
| \(N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}\) | after \(M\) | no | amplitude only |

No cycle. \(\eta\) and the collars \(\rho_H\) are late, but no early constant reads their value: (G-ord) under (Cls) uses only \(\eta\le1/3\). \(M\) enters only through \(N_{\rm ex}\) and the convergence floor of §3.4.

---

## 8. Status

### 8.1 Statements of this draft

| Statement | Status |
|---|---|
| Lemma 2.1 (Definition D sums are split) | [P] from (D2′), O1D Lemma WC |
| Lemma 2.2 (faithful/tame calculus) | [P] |
| Lemma 2.3 and variant (uniqueness transfer) | [P] |
| Lemma 3.1 ((4.4), (3), R9 are tame) | [P] from (Spec-D), (D2′), (Bud) |
| **Theorem 1 ((DR-locP), \(c_P=0\))** | **[P]** from (Spec-D), (D2′), (UNQ); (iv) needs (UNQ-loc) |
| Corollary 1′ (\(c_P=1\) with sources) | [P] from (S-loc) |
| Proposition 3.2 (R does not imply (DR-locP)) | [CE] |
| Proposition 4.0, Lemma 4.1, Lemma 4.2 | [P] from R, TD Lemma 1 |
| **Theorem 2 ((JC\(_\tau\)), read-rooted)** | **[P]** from R, A, complete stencils, (5-N), (TJ) |
| TD2d's (JC) with both \(a-12\) and \((C/D)^{|V|/2}\) | not proved; not needed |
| Lemma 4.3 ((5-N) from (5)) | [P] from TD (5), R, (TJ) |
| Lemma 5.0, Proposition 5.1′ | [P] |
| **Lemma 5.1 (read-rooted forest sum: keeps the collar decay)** | **[P]** |
| Lemma 5.2 (literal carrier length) | [P] from (X°), G |
| **Theorem 3 ((File-P°))** | **[P]** with the family \(\{\widehat H^+\}\) |
| Proposition 5.3 (class-term carriers) | [P] from Theorem 1 |
| Proposition 5.4 (labelled cluster expansion) | [P] from (G-P), CI Theorem 5 majorants |
| (Cls) | **[O] — first remaining**; three attacks §6.2 |

### 8.2 Corrections proposed to other notes (not made; no frozen file edited)

- **NL1-L H-DR** (NL1-L 168–169): for the specification (Spec-D), "at fixed \(P\)" can be dropped: Theorem 1 gives pair-locality with \(c_P=0\) under the DR-lane imports.
- **TD2d (JC)** (TD2d 405–408): replace by Theorem 2, which decays in \(m_{X(f)}(W\cup V)\), rooted at the reads, not in \(m_{N_\rho(X_f)}\). TD2d's closing paragraph (TD2d 412) is withdrawn, as TD2 Correction 10 says; Theorem 3 replaces it, with a collar proportional to the hub instead of logarithmic.
- **TD2d (5-sw)** (TD2d 382): not needed; Lemma 4.3 reduces its corner part to TD's (5).
- **IN1** (frozen): (Cls) is the change requested, for the lead.

### 8.3 Checks this draft needs (for the referee)

1. Lemma 2.1(ii)–(iii): the depth computation, the claim that \(\kappa^\sharp\) meets at most three consecutive layers (O1D 105), and the tree-walk field hull inside \([\![\omega]\!]^+\).
2. Lemma 2.3: the norm comparison for the glued field, using that \(n_y\) reads within \(d_{\mathbf B}\)-distance \(1\).
3. Lemma 3.1: that every term of NR9 (4.4) and D3L (3) has been listed, and the Neumann form of \(d_s'^{\mathsf T}\).
4. Lemma 4.1 Steps 1–3: the expansion holding only \(B_b\) at one, the switch selection identity, and the connectivity argument through R's component and source clauses (TD 32–33).
5. Lemma 4.2: the label-merging step in Bird's allocation and the count \(3^{|Z|}\).
6. Lemma 5.1: the leaf-first summation and the exponential formula.
7. Theorem 3: the exponent bookkeeping (F1)–(F4) and the Case-2 connector bound of Lemma 5.2.
8. Proposition 3.2: positivity of \(\partial_{p_z}B_{c_0c_0}\) at \(P=0\).

Only `library/drlocp-draft.md` is written. Retrieval, searches and file bookkeeping discharge no mathematical step. The text is not refereed, is not an audit and grants no status.
