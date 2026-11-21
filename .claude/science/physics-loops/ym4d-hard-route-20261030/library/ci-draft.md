# CI: CI-base and CI-form for the actual construction (pass 1, long draft)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05. Pass 1 (Claude draft) of critical-path item 8 of `library/assembly-status.md` (L189). Not distilled, not refereed, not checked by another model. Research text; it grants no status. Source constructions are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (revision `31a47c543775`); the renormalization-group and large-field method is Tadeusz Bałaban's, and the expositions used by the library are credited to Jonathan Dimock. All arguments are hand proofs, written to be Lean-formalizable. No run discharges a step. A line number "L" refers to the named file in this clone; "SA n" refers to `ym4.tex` in the scratchpad copy.

Read for this note: `assembly-status.md` (whole); `nl1-L.md` L1–240, L296–742; `ci-form.md`, `td.md`, `td2.md`, `drlocp.md`, `cls.md` (whole); `in1.md` L7–239, L336–375, L660–699; `st1-r4.md` L41, L82–89, L295–312, L1533–1560, L1696–1710; `hma-draft.md` L86–305, L408–520; `dom.md` L71, L111, L355–404; `dr.md` L170–200, L592–628; grep maps of `geoh.md`, `descent.md`. SA 17255–17300, 19555–19680, and grep hits at SA 254–255, 2719, 17066.

## 0. Result and status

The table lists every clause of item 8 and its status in this pass. "Proved" means proved here, or checked here in a distilled text, as an implication from the named imports (§2). "Outstanding" means not proved.

| Clause | Where | Status |
|---|---|---|
| CI-base (nl1-L L570–572) | Theorem 3.1 | **proved** (no import beyond the definitions) |
| Order-k switched localization (replaces nl1-L Lemma 3's affine-read hypothesis for W) | Lemma 4.1 | **proved** |
| Gas-distance oscillation (shells) | Lemma 4.2, Corollary 4.3 | **proved** (from Theorem 4's component locality) |
| H-W: Wilson cubic remainder W3 | Theorem 5.1 | **proved** conditional on [DR], [DOM-curv]; needs \(q>3p_0\) (row 1) |
| H-W: Jacobians, profile/coupling differences | Propositions 5.2–5.3 | **proved** conditional on [JAC] and IN1 (3) |
| H-W: linear and quadratic Gaussian defects | Theorem 5.4 | **proved** conditional on [HOL-K] and hma G-ID(cov) |
| H-C, single family (any level) | Lemma 6.1 | **proved**; corrects ci-form's weight \(\kappa/2\) to \(\kappa/(2c_X)\) |
| H-C, all carried families (multilevel sum) | Theorem 6.2 | **proved conditional on OSF-loc**; **OSF-loc Outstanding** (§14: three attacks) |
| H-I and the complex island amplitude (td (5)) | Theorem 7.1 | **proved** conditional on IN1 H-O (18) and [DOM-I]; island terms become two-sided |
| X° for exempt terms filed at the current level | Lemma 8.1 | **proved** with \(C_{\rm pr}=C_{\rm tr}\), \(c=c_{\rm rd}\) |
| X° for older exempt terms with standing successors | Lemma 8.2 | **proved** (member form); retired islands **Outstanding** (Match-heal/LD) |
| X per-read sums | Lemma 8.3 | current level **proved**; multilevel and **AGE Outstanding** |
| Ordinary TD (td2 Theorem 3) | §8.4 | **checked**, no failing step; conditional on R, A, X, G, RUN, X°, G-ord |
| Regular gas, normal (Mayer) domination (18) on the global fibre | Theorem 9.1 | **proved** conditional on the potentials of §§5–8 and [HM] |
| Filing: (Cls+), Match-SF/O, Match-read/file, Match-heal/LD | §10 | **Outstanding** (cls.md's matching hypotheses stand) |
| nl1-L full-source distance bound (L494–502, first point) | Theorem 11.1 | **proved**: the needed distance is to the fluctuation, and Lemma 4.2 supplies it |
| nl1-L L504–512 (age factor) | §11.1 | **Outstanding** (AGE) |
| H-FL (6) stored-datum bound | Lemma 11.2 | **proved** conditional on [TEST-v0] |
| H-ACT on the changed domains | §11.3 | reduced to CI-old, [DOM], the definition of §2.3 and three named imports |
| UM1-rest (hma L300), total norm \(\le W_0/4\) | Theorem 12.1 | **proved conditional on OSF-loc and AGE** (and the imports) |
| Constant order (IN1 rows 1–10, Amendment 1) | §13 | **checked**; no cycle; additions listed by row |

**First remaining Outstanding statement, in item 8's own order:** OSF-loc (§14), the multilevel class-carrier sum that H-C needs for families carried from older levels. It is SA's OSF3–OSF4 in the fluctuation-oscillation form. SA 19666–19667 calls OSF3 "the renormalisation assertion". Three attacks fail (§14). The supply needs P82M's derivative bound (item 1) and H-OL's pointed-Hessian cancellation (item 9). So item 8 cannot close before those parts of items 1 and 9. The assembly-status ordering "Each depends only on earlier items" (L178) does not hold for this clause.

## 1. The clauses exactly as the frozen consumers read them

### 1.1 NL1 (frozen `nl1-L.md`, Theorem 7)

**D4** (L545–550): "CI at a structure \(\sigma\) means that every activity formed there is defined on the full specified chain domain \(\mathcal D_{a|\sigma}\), with its bound and the complete H-ACT interface. The domain includes continuation, gauge witnesses and stored-slot clauses. Activity amplitudes may be chosen after \(M,\bar\kappa\); they cannot feed any constant that was required earlier."

**Local normal domination** (L552–565), display (18):
\[
 f(P)=\sum_\nu\int G_\nu(P,\xi)\,d\mu_\nu(\xi),\qquad
 \sum_\nu\int\sup_{P\in K}|G_\nu(P,\xi)|\,d\mu_\nu(\xi)<\infty
\]
"for every compact polydisc \(K\) in that fibre. Use fixed positive \(\sigma\)-finite measures, placing all external-parameter dependence in \(G_\nu\); the displayed supremum has a Borel integrable majorant."

**Theorem 7** (L567–590). The four hypotheses:

1. **CI-base** (L570–572): "all initial activities satisfy CI, on their specified initial domains. Bare Wilson plaquette functions satisfy their holomorphic clause; other initial factors and bounds are included in this assumption."
2. **CI-maps** (L573–577): "at each main step, Theorem 4's hypotheses other than the old activity bounds hold uniformly on every fibre of the entire new chain domain. … At stages and outputs supply the corresponding admissible, holomorphic, local maps on their own required fluctuation domains."
3. **CI-Gauss** (L578–581): "the actual precision/comparison package holds … of frozen IN1 **H-M**; a real-background inverse alone is insufficient."
4. **CI-form** (L582–587): "NL1/LF1's actual formation formulas on the *whole new domain* are built from these maps and earlier activities. Given their bounds and CI-Gauss, the formulas have (18) and return the required \(b_f\), or the stated oscillation/one-sided bound. They preserve realness, real ties, gauge covariance, restriction consistency, and the near/far stored-slot rules. Branches and formulas agree on overlaps of fibre charts."

Item 8 owns CI-base and CI-form. CI-maps belongs to items 4–5 (DR, DOM) and CI-Gauss to item 6 (HM). The Outstanding paragraph L608–617 names what CI-form must contain: "The actual locally normal Mayer estimate, and LF1's external-parameter-independent Borel domination, must be supplied."

**nl1-L's three further item-8 clauses.**

- **H-FL** (L140–157), with Outstanding L154: "F8 leaves the stored-threshold comparison explicit; a small completed source alone is not the raw-datum bound (6)." Bound (6) (L146): \(\|v_0\|_\infty\le\delta_0:=C_{\rm st}A_1g\ell^{p_0}\).
- **H-ACT** (L176–198), with Outstanding L195: "H-ACT on the changed domains is CI plus the actual term identifications. … In particular the strip identification, W decomposition, logarithm branches, kept-form oscillation, and island-domain inclusion remain explicit." Its I-row (L188): "\(\Psi=\Phi-\Phi^\circ\) is holomorphic and \(\operatorname{Re}\Psi\le B_f:=C_\Psi V^\circ\); the restricted chain domain lies in its full fixed creation domain."
- **Full-source distance** (L494–502): "PAN's G-gap separates that activity from the *integrated* source; it does not show \(D_f\ge10LM\check R_i-C\) for this full source. … One needs a spatial difference-response estimate about the nonzero stored source, with compatible pinning, or another argument." Second point (L504–512): "A retained age gain is required."

### 1.2 ST1 (frozen `st1-r4.md`)

L1533: "**CI (external consumer interface; Outstanding, owned by NL1/LF1).** Every carried activity must be defined and bounded by its declared \(b_f\) on the **whole** ST1 chain domain with (Tq0), the permanent ledger, R1 cores, frozen intrinsic tower functions and the prescribed witness carriers/constants. It must have the holomorphic, Borel, covariance, stored-variable and tie properties in Section 1. **No constant fixed before \(\kappa\) reads \(b_f\); in the quantitative substitution conclusion, \(b_f\) enters only the output bound (77).**"

Theorem 14, hypothesis 4 (L1544): "CI supplies the activity \(f\) on the target domain with bound \(b_f\). Every endpoint pillar and full read carrier is included in (71). … No earlier domain or precision constant depends on \(b_f\)."

### 1.3 The sub-clauses (distilled texts; read as drafts to check)

- **H-C** (`ci-form.md` L58–65): connected complete carrier \(X_f\), presentation \(F_f(P;s,\zeta)\) with \(F_f(P;s,0)=f_0(P)\), component locality, and (5): \(|F_f-f_0|\le\omega_f\) on \(\mathbb S_{X_f}\times\mathbb D_R\), \(\sup_\Delta\sum_{f:X_f\ni\Delta}\omega_fe^{\alpha|X_f|}\le N_C\), \(\alpha=\kappa/2\), \(N_C\) "fixed before \(\gamma\)".
- **H-W** (`ci-form.md` L69–83): NL1-L Lemma 3 at every complex input, (6)–(7), \(\sup a_W\to0\). Outstanding (L85): CA-II "does not prove (6), finite range of the coupling-profile background dependence, or those vanishing orders at independent currents." Also nl1-L L375–379: "The coupling-profile term there reads a background map; the finite range of the pivot correction alone does not make it a local function of the free field."
- **H-I** (`ci-form.md` L372–378), (32): \(\Phi_\omega=\Phi_\omega^\circ-\tfrac12q_\omega+V_\omega\), \(\Phi^\circ\) real, \(q\ge0\), \(|V_\omega|\le C_IN_0(\omega)\); consumed through (33): \(\operatorname{Re}\Psi_\omega\le C_IN_0(\omega)\).
- **TD** (`ci-form.md` L87–94), (8); **ordinary TD** is `td2.md` Theorem 3 (L111–158) with **X°** (L76–80) and **G-ord** (L73–74); its Outstanding L82.
- **Complex island amplitude** (`td.md` L51–63), (5): \(A_f-\operatorname{Re}\Phi_f(P,h_0(P))\le B_f\) on \(\mathcal O_\sigma(U)\); Outstanding L63.
- **Filing** (`cls.md` L371–378): Match-SF/O, Match-read/file, Match-heal/LD, Match-history; Proposition 12 (L380–382) transfers IN1 only under them.
- **UM1-rest** (`hma-draft.md` L300): "the potential types other than the gauge type are holomorphic on their declared boxes and cores and satisfy UM1 with total norm \(a_{\rm rest}\le W_0/4\), with the structural interface of ci-form H-S." hma L306 assigns it to item 8.

### 1.4 The constant order

IN1 rows 1–10 (`in1.md` L227–236) and Amendment 1 (L666–675: "\(L>L_0^\natural\)" in row 2, "\(\kappa\ge\kappa_0^\natural(L)\)" in row 4). Row 1 (L227) reads "\(q>\max(p_0+2r,Cp_0)\)" with power-count constant \(C\). nl1-L's own order (L200–209) and the CI rule above (no constant fixed before \(\kappa\) reads \(b_f\)) are retained.

## 2. The actual construction and the imports

### 2.1 The construction

- **Gauge form: D-Y3** (`hma-draft.md` L111–117, which reads frozen `descent.md` Theorem B, L196ff). The soft-gauge exponent is \(-x\Phi^{\rm Y}_V(D)\), relative to the averaged contour, and the precision is \(\mathsf A^{\rm Y}(P)=X(\mathbf p(P))+\mathsf C_V^{\mathsf T}\mathsf G^{\rm Y}_V\mathsf C_V\) (hma L107). At block-axial \(V\) this is SA's step (hma L117).
- **Domains: ST1 with Tq0, CV and GS** (frozen `st1-r4.md`). Tq0 (L82–89): \(r_\iota(m)=C_\iota g_m\ell_m^q\), \(\lambda_\tau\equiv1\), \(\Lambda_Q=1\). CV (L41): the averaged contour variable is the canonical representative. GS (L1701–1710): SLOT-ST replaces GEO-slot.
- **Main step.** Fix a finite admissible history and a main step \((i-1,{\rm out})\to(i,{\rm in})\). Fine cubes have side \(M\) at level \(i-1\); coarse cubes have side \(LM\). \(I\) is the set of integrated free bonds; \(\mathcal G\) is the set of fine cubes owning a bond of \(I\) (the *gas cubes*). Notation as in nl1-L (1)–(5): \(g=\theta_{i-1}^{-1/2}\), \(\ell=\log\theta_{i-1}\), \(R=\ell^q\), fluctuation polydisc \(\mathbb D_R\), box \(\mathfrak b=C_{\rm win}A_1\ell^{p_0}<R\), switches \(\mathbb S_X\) (nl1-L (2)). The centred substitution is nl1-L (5): \(\Pi_f(P;s,\zeta)=\rho_f^{\rm res}(P\dotplus\mathcal P_P(H_f(P;s,\zeta)))\).

### 2.2 Named imports (owner item, status)

Each is a hypothesis of this note. None is proved here.

| Name | Statement used | Source and status |
|---|---|---|
| [NL1-L] | Theorem 4 (L381–402) and Lemma 2 (L323–341) for every carried term, uniformly on the fibres used | frozen, conditional on H-ST, H-FL, H-DR, H-ACT |
| [DR] | H-DR (nl1-L L159–171): joint holomorphy, (7), face-component row locality | frozen `dr.md` Theorem 4 (L170–188) and its Lemmas 1–3; conditional on W, ONE, PW, NL, admission; PW for \(H_1,\mathfrak G\) and complex references Outstanding (dr L596): **item 4** |
| [DOM] | every pair used below lies in its declared domain: substituted pairs in the target chain domain (Theorem 4's half-gap admission, using CI-maps), and the target chain fibre inside \(\mathrm{R4}(Z;a_0,a_1,j_0)\) with descent (7) | `dom.md` Theorems 3, 6–8 conditional; actual roster, coverage and input membership Outstanding (dom L111, L221, L359): **item 5** |
| [DOM-curv] | on the target chain domain every plaquette \(p\) of input layer \(m\) satisfies \(\|\partial\mathbf U(p)-1\|_{\rm op}<\alpha_{0}(m)\eta_m^2\), with \(\alpha_0(m)=C_0g_m\ell_m^q\) | the R4 defect clause (hma L93; SA 5665–5694) for Tq0 radii: **item 5** |
| [DOM-I] | every pair at which a standing island term is evaluated (substituted pairs on the target fibre, admitted shift balls of td A) lies in the island's fixed creation domain | nl1-L L188 ("the restricted chain domain lies in its full fixed creation domain"): **item 5** |
| [HM] | hma Theorem 3.2 (L178–192): H-M, CI-Gauss, ci-form H-G and H-S's Gaussian half, td J's matrix part, on R4 with (7); hma Theorem 4.3 (gauge type, \(a_{\rm GF}\le W_0/4\)); hma Theorem 6.6 and Corollary 6.7 (G-ID(cov)) | `hma-draft.md`, pass 1, **unrefereed**; rests on frozen hm, descent, cp12: **item 6** |
| [HOL-K] | stated in §5.4 | new, named here: **items 4 and 6** |
| [JAC] | stated in §5.2 | part of W/AV's chart data (hm L42; pr-lay L95): **items 4–5** |
| [GEOH] | IN1 H-G and the hub geometry G of td/td2 for the actual history | frozen `geoh.md` Theorem 1 (L169) conditional; remaining identification Outstanding (geoh L167): **item 3** |
| [RUN] | \(\check R_i\ge(\ell-1)^r\), \(r\ge2\), uniformly | frozen `dom.md` Theorem 1 (RUN-low) and `geoh.md` Lemma 1 |
| [H-O] | IN1 H-O (18) (in1 L197–203) on fixed creation domains | IN1 import, Outstanding (in1 L204): **item 10** |
| [OSF-loc] | stated in §6.2 | Outstanding (§14): **items 1 and 9** |
| [CI-old] | CI for every activity formed earlier in the finite history | the induction hypothesis of nl1-L Theorem 7 |

### 2.3 The formation rule at complex pairs (a definition)

nl1-L L447–450 says the identification of Theorem 4's family "with an actual formation integrand at every complex external pair remains part of Theorem 7's formation hypothesis." I resolve this by definition. The actual construction is specified by its real formula, and at complex pairs the step's exponent **is** the following analytic family, with every summand given by Theorem 4's centred substitution:
\[
 \psi(P;s,\zeta)
 =\underbrace{-\sum_{p}x_p\,a_p\bigl(\Pi^{\rm W}(P;s,\zeta)\bigr)}_{\text{Wilson, profile}}
 \;\underbrace{-\,x\,\Phi^{\rm Y}_V(C_V(g\zeta))}_{\text{gauge (D-Y3)}}
 +\underbrace{\sum_f F_f(P;s,\zeta)}_{\text{S,Z,E,R,B,K,I}}
 +\underbrace{\log j(P;g\zeta)}_{\text{Jacobians}} .
 \tag{2.1}
\]
Here \(\Pi^{\rm W}\) is nl1-L (5) with the identity activity, so that \(a_p(\Pi^{\rm W})\) is the plaquette function of the substituted background, and \(x_p\) is the step's Wilson profile. At \(s=\mathbf1\) on the physical locus, H-FL's identification (nl1-L L150–152) and ST1 Lemma 12 make (2.1) the actual step exponent. This removes the "complex-pair identification" item of ci-form H-D (L38) **as an identification problem**. It does not remove any bound: every estimate below is proved for (2.1) itself. The splitting into a Gaussian part and potentials is fixed in §5.4.

## 3. CI-base

**What the initial activities are.** IN1 L219: "The bare presentation has only \(x_0=\beta\) and Wilson density, with no regular terms or islands." So the only initial activities are the plaquette functions. SA 2719 gives their holomorphic continuation: \(a_p(U)=1-\tfrac12\operatorname{tr}U_p\) (real form SA 254, \(1-\tfrac12\operatorname{Re}\operatorname{tr}U_p\); IN1 L11–13 uses the same convention). There are no boundary terms, kept forms, stored slots or islands at level zero. Initial ST1 records carry their own radius indices (nl1-L L69); CI-base asks only that the activity be defined and bounded on whatever initial chain domain those records declare.

**Theorem 3.1 (CI-base).** For a triple \(P=(U,A',\mathbf J)\) at level zero, with \(U\) real and \(A'\) in the complexified Lie algebra \(\mathfrak{sl}(2,\mathbb C)\) on each bond, put \(\mathbf U=e^{i\eta A'}U\), \(W_p=\partial\mathbf U(p)\) and \(a_p(P)=1-\tfrac12\operatorname{tr}W_p\). Then:

1. \(a_p\) is an entire function of \(A'\) at fixed \(U\), and does not depend on \(\mathbf J\).
2. \(a_p\) depends on \(P\) only through the pair \((\mathbf U,\mathbf J)\). So it takes equal values at any two splittings of one pair (the real tie and complex splitting descent).
3. \(a_p\) is real at real triples (\(A'\) Hermitian).
4. \(a_p(P^g)=a_p(P)\) for every real gauge \(g\), with \(P^g=(U^g,\operatorname{Ad}(g)A',\operatorname{Ad}(g)\mathbf J)\).
5. \(a_p\) is continuous, hence Borel, in \((U,A')\). It reads only the four bonds of \(p\), so it is restriction-consistent and agrees on common lifts across tori and cutoffs.
6. \(W_p\in SL(2,\mathbb C)\) and \(a_p=\tfrac12\det(1-W_p)\). Hence \(|a_p|\le\tfrac12\|W_p-1\|_{\rm op}^2\). On any domain whose plaquette defect clause is \(\|W_p-1\|_{\rm op}<a\eta^2\), \(|a_p|\le b_p:=\tfrac12a^2\eta^4\). Without a defect clause, \(|a_p|\le\tfrac12(1+e^{4\eta\|A'\|_\infty})^2\).

So CI holds at the initial structure, on every initial chain domain, with bound \(b_p\). The bound \(b_p\) contains only the initial domain radius \(a\). It enters only output bounds, as st1-r4 L1533 requires.

*Proof.* (1) The matrix exponential is entire, and \(W_p\) is a product of four such factors and fixed real matrices. (2) \(a_p\) is a function of \(\mathbf U\) alone; two splittings of a pair have the same \(\mathbf U\). (3) If \(A'\) is Hermitian and traceless, \(e^{i\eta A'}\in SU(2)\), so \(W_p\in SU(2)\) and \(\operatorname{tr}W_p\in\mathbb R\). (4) \(\partial(\mathbf U^g)(p)=g(x)W_pg(x)^{-1}\) for the base point \(x\) of \(p\), since \(e^{i\eta\operatorname{Ad}(g)A'}=ge^{i\eta A'}g^{-1}\). The trace is conjugation invariant. (5) Composition of continuous maps; the read set is the boundary of \(p\). (6) \(\det e^{i\eta A'}=e^{i\eta\operatorname{tr}A'}=1\), so \(\det W_p=1\). For a \(2\times2\) matrix \(W\) with \(\det W=1\), \(\det(1-W)=1-\operatorname{tr}W+\det W=2-\operatorname{tr}W\) (this is SA's (OSF8), SA 19651–19654). For any \(2\times2\) matrix \(X\), \(|\det X|=\sigma_1\sigma_2\le\|X\|_{\rm op}^2\). For the last bound, \(\|W_p\|_{\rm op}\le\prod\|e^{i\eta A'(b)}\|_{\rm op}\le e^{4\eta\|A'\|_\infty}\). \(\square\)

*Status: proved.* No import is used. The phrase in L571, "other initial factors and bounds are included in this assumption", is empty at level zero by IN1 L219.

## 4. Two analytic tools

Throughout this section, \(X\) is a nonempty connected set of fine cubes (corner adjacency), \(\kappa_\star>0\), and
\[
 \mathbb S_X(\kappa_\star)=\{s\in\mathbb C^{\mathcal C}:s|_X=1,\ |s_\Delta|<e^{\kappa_\star}\}.
\]
A function \(\Phi:\mathbb S_X(\kappa_\star)\times\mathbb D_R\to\mathbb C\) is **component-local** if it has nl1-L Theorem 4's clause 2 (L390–392): when \(K_X(s)=K_X(s')=K\), \(s|_K=s'|_K\) and \(\zeta|_{I\cap K}=\zeta'|_{I\cap K}\), then \(\Phi(s,\zeta)=\Phi(s',\zeta')\). Theorem 4 gives this for every carried term \(F_f\), with \(X=X_f\) and \(\kappa_\star=\bar\kappa\).

### 4.1 Order-k switched localization

**Lemma 4.1.** Let \(\Phi\) be holomorphic and component-local on \(\mathbb S_X(\kappa_\star)\times\mathbb D_R\), with \(|\Phi|\le B\), and \(D_\star:=e^{\kappa_\star}-1>0\). Fix an integer \(k\ge1\). Let \(T_{k-1}\Phi(s,\zeta)=\sum_{|\alpha|<k}\partial_\zeta^\alpha\Phi(s,0)\zeta^\alpha/\alpha!\) and \(\mathsf R_k\Phi=\Phi-T_{k-1}\Phi\). For \(Y\supset X\) put \(s_Y(\tau)=\mathbf 1_X+\tau\) with \(\tau\in[0,1]^{Y\setminus X}\) and zero off \(Y\), and
\[
 f^{(k)}_Y(\zeta)=\int_{[0,1]^{Y\setminus X}}\partial_\tau^{\,Y\setminus X}\,
      \mathsf R_k\Phi(s_Y(\tau),\zeta)\,d\tau
 \qquad(f^{(k)}_X(\zeta)=\mathsf R_k\Phi(\mathbf 1_X,\zeta)).
 \tag{4.1}
\]
Then:

(a) \(\sum_{Y\supset X}f^{(k)}_Y=\mathsf R_k\Phi(\mathbf1,\cdot)\), the sum being finite;
(b) \(f^{(k)}_Y=0\) unless \(Y\) is connected;
(c) \(f^{(k)}_Y\) depends on \(\zeta\) only through \(\zeta|_{I\cap Y}\);
(d) for \(\|\zeta\|_\infty\le r<R\),
\[
 |f^{(k)}_Y(\zeta)|\le(k+1)B\,(r/R)^k\,D_\star^{-|Y\setminus X|};
 \tag{4.2}
\]
(e) each \(f_Y^{(k)}\) is holomorphic in \(\zeta\) and in every external parameter in which \(\Phi\) is holomorphic with the bound \(B\) locally uniform; it is real when \(\Phi\) is real at real arguments.

*Proof.* (a) For a \(C^1\) function \(g\) on \([0,1]^A\), \(A\) finite, repeated use of the fundamental theorem of calculus in each coordinate gives \(g(\mathbf1)=\sum_{B\subset A}\int_{[0,1]^B}\partial_\tau^Bg(\tau_B,0_{A\setminus B})\,d\tau_B\). Apply this to \(g(\tau)=\mathsf R_k\Phi(\mathbf1_X+\tau,\zeta)\) with \(A=\mathcal C\setminus X\), and write \(Y=X\cup B\).

(b) Since \(X\) is connected, a disconnected \(Y\supset X\) has a component \(C\) with \(C\cap X=\varnothing\). At \(s=s_Y(\tau)\) the cubes adjacent to \(C\) outside \(Y\) have switch zero. So for every value of \(\tau|_C\), including zeros, \(K_X(s)\) and \(s|_{K_X(s)}\) do not change, and \(C\cap K_X(s)=\varnothing\). Component locality makes \(\Phi(s_Y(\tau),\zeta)\) independent of \(\tau|_C\). The Taylor coefficients \(\partial^\alpha_\zeta\Phi(s,0)\) inherit this. Hence \(\partial_{\tau_c}\mathsf R_k\Phi=0\) for \(c\in C\).

(c) At \(s=s_Y(\tau)\), \(K_X(s)\subset Y\), and component locality gives dependence on \(\zeta|_{I\cap K_X(s)}\) only.

(d) Fix real \(\tau\). For complex \(\sigma\) with \(|\sigma_c-\tau_c|\le\rho'<D_\star\) (\(c\in Y\setminus X\)), \(|\sigma_c|<1+\rho'<e^{\kappa_\star}\), so \(s=\mathbf1_X+\sigma\) lies in \(\mathbb S_X(\kappa_\star)\). At such \(s\) and \(\zeta\ne0\), put \(e=\zeta/\|\zeta\|_\infty\) and \(\phi(t)=\Phi(s,te)\), \(|t|<R\). Its Taylor coefficients satisfy \(|c_j|\le BR^{-j}\) by Cauchy's estimate on circles \(|t|=R'\uparrow R\). So \(|T_{k-1}\Phi(s,\zeta)|\le\sum_{j<k}B(\|\zeta\|_\infty/R)^j\le kB\) and \(|\mathsf R_k\Phi(s,\cdot)|\le(k+1)B\) on \(\mathbb D_R\). The function \(t\mapsto\mathsf R_k\Phi(s,te)\) has a zero of order at least \(k\) at \(t=0\); dividing by \(t^k\) and applying the maximum principle on \(|t|=R'\uparrow R\) gives \(|\mathsf R_k\Phi(s,\zeta)|\le(k+1)B(\|\zeta\|_\infty/R)^k\). The map \(\sigma\mapsto\mathsf R_k\Phi(\mathbf1_X+\sigma,\zeta)\) is holomorphic (the Taylor coefficients are holomorphic in \(s\) by Cauchy's integral formula in \(\zeta\)). Cauchy's formula for the mixed first derivative on the polycircle of radius \(\rho'\) about \(\tau\) gives \(|\partial_\tau^{Y\setminus X}\mathsf R_k\Phi|\le(k+1)B(r/R)^k\rho'^{-|Y\setminus X|}\). There is no factorial because each derivative is of first order in a distinct variable. Let \(\rho'\uparrow D_\star\) and integrate over the unit cube.

(e) The integrand of (4.1) is a finite combination of Cauchy integrals of \(\Phi\), uniformly bounded on compact sets; integrating Cauchy's formula over the compact real cube preserves holomorphy. Real arguments give real Taylor coefficients and real integrands. \(\square\)

*Status: proved.* For \(k=1\), \(\mathsf R_1\Phi=\Phi-\Phi(s,0)\), and Theorem 4 clause 3 (\(F_f(s,0)=f_0\)) makes (4.1) exactly ci-form Lemma 1's pieces (L197–204); (4.2) with \(k=1\) is ci-form (21) with \(\omega_f=2B\). I checked ci-form Lemma 1's summation step (L206–214): from \(d_f(Y)\le|Y|\) and \(D_\star\ge e^{\lambda+1}\), \(\lambda d_f(Y)-(\lambda+1)|Y\setminus X_f|\le-|Y|+(\lambda+1)|X_f|\), and \(|Y|e^{-|Y|}\le1\). It is correct **provided** the carrier weight in (5) is at least \(e^{(\lambda+1)|X_f|}\); see Lemma 6.1 for why the weight \(e^{(\kappa/2)|X_f|}\) of (5) must be read with \(\kappa/2\) replaced by \(\kappa/(2c_X)\).

### 4.2 Distance to the gas: switched shells

For a carrier \(X\) put \(G(X)=\min\{d(X,c):c\in\mathcal G\}\), the fine-cube graph distance from \(X\) to the gas cubes (\(+\infty\) if \(\mathcal G=\varnothing\)).

**Lemma 4.2 (shell Schwarz).** Let \(\Phi\) be holomorphic and component-local on \(\mathbb S_X(\kappa_\star)\times\mathbb D_R\), \(|\Phi|\le B\). Let \(0\le\kappa_1<\kappa_\star\). Then for every \(s\in\mathbb S_X(\kappa_1)\) and \(\zeta\in\mathbb D_R\),
\[
 |\Phi(s,\zeta)-\Phi(s,0)|\le2B\,e^{-(\kappa_\star-\kappa_1)G(X)} .
 \tag{4.3}
\]

*Proof.* Let \(n=G(X)\); if \(n=0\) the bound is the triangle inequality, and if \(n=\infty\) the component of \(X\) never meets \(I\), so the difference is zero. For \(1\le k\le n\) let \(\mathrm{Sh}_k=\{c:d(c,X)=k\}\). For \(t\in\mathbb C^n\) define \(s(t)_c=t_ks_c\) for \(c\in\mathrm{Sh}_k\) and \(s(t)_c=s_c\) otherwise. If \(|t_k|<e^{\kappa_\star-\kappa_1}\) for all \(k\), then \(s(t)\in\mathbb S_X(\kappa_\star)\), since the shells miss \(X\). Put \(\Delta(t)=\Phi(s(t),\zeta)-\Phi(s(t),0)\). It is holomorphic and \(|\Delta|\le2B\).

Suppose \(t_k=0\). Along a corner-adjacency path the distance to \(X\) changes by at most one per step. So every path from \(X\) to a cube at distance greater than \(k\) meets \(\mathrm{Sh}_k\), where the switch is zero. Hence \(K_X(s(t))\subset N_{k-1}(X)\). Since \(k\le n=G(X)\), this set contains no gas cube, so \(I\cap K_X(s(t))=\varnothing\). Component locality applied to \(\zeta\) and \(0\) gives \(\Delta(t)=0\).

So \(\Delta\) vanishes on every coordinate hyperplane of the polydisc of radius \(\varrho=e^{\kappa_\star-\kappa_1}>1\). Divide by \(t_1\) (removable singularity) and use the maximum principle on \(|t_1|=\varrho'\uparrow\varrho\): \(|\Delta(t)|\le2B|t_1|/\varrho\). The quotient \(\Delta/t_1\) still vanishes on the other hyperplanes; iterate. At \(t=\mathbf1\), \(|\Delta(\mathbf1)|\le2B\varrho^{-n}\). \(\square\)

*Status: proved.* It uses only component locality and the switch polydisc. It does not use the response bound (7), animal counts or the layer metric.

**Corollary 4.3 (gas-distance oscillation of carried terms).** Let \(F_f\) be a carried term of nl1-L Theorem 4, with \(|F_f-f_0|\le\omega_f\) on \(\mathbb S_{X_f}(\bar\kappa)\times\mathbb D_R\) (two-sided kinds and, by Theorem 7.1, islands). Put \(\kappa_s:=\bar\kappa-\bar\kappa_1\) for a chosen \(0<\bar\kappa_1<\bar\kappa\). Then on \(\mathbb S_{X_f}(\bar\kappa_1)\times\mathbb D_R\),
\[
 |F_f(s,\zeta)-f_0|\le\omega_fe^{-\kappa_sG(X_f)}\cdot\frac{\|\zeta\|_\infty}{R}\cdot2 .
 \tag{4.4}
\]
*Proof.* Lemma 4.2 with \(\Phi=F_f-f_0\), \(B=\omega_f\), and \(\Phi(s,0)=0\) (Theorem 4 clause 3), gives \(|F_f-f_0|\le2\omega_fe^{-\kappa_sG}\) on \(\mathbb D_R\). This function vanishes at \(\zeta=0\); Schwarz's lemma on complex lines through zero gives the factor \(\|\zeta\|_\infty/R\). \(\square\)

So a carried term at fine-cube distance \(G\) from the gas behaves as if its fluctuation radius were \(Re^{\kappa_sG}/2\). There is no cap like nl1-L's \(R_{\rm cap}\) (L470–473), because the radius is not enlarged; the oscillation is reduced. The stored source \(S(v_0)\), wherever it lies, enters only \(f_0\), which does not depend on \(\zeta\). This is the use made of it in §11.1.

## 5. The W kinds and their UM1 norms

nl1-L Lemma 3 (L343–367) assumes each W term is \(\phi_f(w_f(\zeta))\) with an *affine* read \(w_f\) of range \(R_W\). Its Outstanding (L375–379) says that the coupling-profile term "reads a background map", so it is not of that form. Under (2.1) the Wilson and profile terms are plaquette functions **composed with the centred substitution**. Lemma 4.1 handles such compositions directly, with switches. So the affine-read hypothesis is not needed. The gauge term and the Jacobians are local in the fluctuation and need no switches.

Common notation. \(\mathcal P\) is the set of plaquettes whose value changes with \(\zeta\). For \(p\in\mathcal P\), \(X_p\) is the set of fine cubes meeting the bonds of \(p\) and the pin read sets \(\mathrm{Rd}(y)\) of its endpoint tops (st1-r4 Lemma 4, L295–297; nl1-L L43: "All carriers include the stencils, endpoint pillars and pinning reads they use"). Let \(c_{\rm rd}\) be an early bound for the lattice diameter of these read sets, and impose the floor \(M>2c_{\rm rd}+2\). Then \(X_p\) meets at most two grid intervals per coordinate, so it is a connected set of at most 16 cubes, \(d_f(X_p)\le15\). Write
\[
 C_{\rm pl}:=\sup_\Delta\sum_{p:\,X_p\ni\Delta}\eta_{m(p)}^4\,M^{-4},
\]
where \(m(p)\) is the input layer of \(p\) and \(\eta_m\) its chart mesh in level-\((i-1)\) units. A cube of side \(M\) and its 80 neighbours contain at most \(6\cdot3^4M^4\eta_m^{-4}\) plaquettes of layer \(m\). So \(C_{\rm pl}\le486\,C_{\rm lay}\), where \(C_{\rm lay}\) is an early bound for the number of layers meeting one fine cube and its neighbours (part of the separated longer sequence, H-ST).

Bound on the defect radius. By IN1 (1)–(2) and \(\theta_{i-1}-\theta_i\le\bar B\), \(\theta_m\ge\theta_{i-1}/2\) for every input layer \(m\le i\) once \(\gamma^{-2}\ge2\bar B\). For \(m\le i-1\) and \(\theta\ge e^{2q}\) the map \(\theta\mapsto\theta^{-1/2}(\log\theta)^q\) is decreasing (its derivative is \(\theta^{-3/2}(\log\theta)^{q-1}(q-\tfrac12\log\theta)\)). Hence, after the ceiling \(\gamma^{-2}\ge\max(2\bar B,e^{2q})\),
\[
 \alpha_0(m)\le\sqrt2\,C_0g\ell^q\qquad(m\le i).
 \tag{5.0}
\]

### 5.1 The Wilson cubic remainder

**Theorem 5.1 (W3).** Assume [NL1-L] (Theorem 4 on the target fibre), [DOM-curv], (5.0), \(x_p\le\tfrac54\theta_{i-1}\) (IN1 tube (3)), \(M>2c_{\rm rd}+2\) and \(\log(e^{\bar\kappa}-1)\ge\lambda+1\). For \(p\in\mathcal P\) let \(\Phi_p(s,\zeta)=-x_pa_p(\Pi^{\rm W}(P;s,\zeta))\), and let \(f^{(3),p}_Y\) be the pieces (4.1) with \(k=3\), \(X=X_p\), \(\kappa_\star=\bar\kappa\). Put \(V^{\rm W3}(Y)=\sum_{p:X_p\subset Y}f^{(3),p}_Y\). Then:

1. \(\sum_YV^{\rm W3}(Y)=\Phi_{\rm W}(\mathbf1,\zeta)-T_2\Phi_{\rm W}(\mathbf1,\zeta)\), where \(\Phi_{\rm W}=\sum_p\Phi_p\) is the Wilson part of (2.1) and \(T_2\) its second-order Taylor polynomial in \(\zeta\).
2. \(V^{\rm W3}(Y)\) vanishes unless \(Y\) is connected, reads \(\zeta\) only on \(I\cap Y\), is jointly holomorphic on the fixed-\(U\) fibre and in \(\zeta\), real at real data, and gauge covariant.
3. On the box \(\|\zeta\|_\infty\le\mathfrak b\),
\[
 |V^{\rm W3}(Y)|\le a_{\rm W3}\,e^{-\lambda d_f(Y)},\qquad
 a_{\rm W3}=10\,e^{16(\lambda+1)}C_{\rm pl}C_0^2(C_{\rm win}A_1)^3M^4\,\ell^{3p_0-q}.
 \tag{5.1}
\]
4. If \(q>3p_0\) (row 1, §13), then \(\sup_{\theta\ge\gamma^{-2}}a_{\rm W3}\to0\) as \(\gamma\downarrow0\), with every earlier constant fixed.

*Proof.* (1) is Lemma 4.1(a) for each \(p\), summed; \(\mathsf R_3\) is linear and \(T_2\) commutes with the finite sum. (2) is Lemma 4.1(b), (c), (e). Holomorphy on the fibre is Theorem 4's uniform version (nl1-L L442–446); covariance holds because \(a_p\) is gauge invariant (Theorem 3.1(4)) and \(\Pi^{\rm W}\) has ST1's covariance (nl1-L L171). (3) On \(\mathbb S_{X_p}\times\mathbb D_R\) the substituted pair lies in the target domain (Theorem 4's half-gap admission, nl1-L L421). So [DOM-curv], Theorem 3.1(6) and (5.0) give
\[
 B_p:=\sup|\Phi_p|\le\tfrac54\theta\cdot\tfrac12\cdot2C_0^2g^2\ell^{2q}\eta_{m(p)}^4
 =\tfrac54C_0^2\ell^{2q}\eta_{m(p)}^4 .
\]
Lemma 4.1(d) with \(k=3\), \(r=\mathfrak b\): \(|f^{(3),p}_Y|\le4B_p(\mathfrak b/R)^3(e^{\bar\kappa}-1)^{-|Y\setminus X_p|}\). As in ci-form L206–214, for connected \(Y\), \(d_f(Y)\le|Y|\) and \((e^{\bar\kappa}-1)\ge e^{\lambda+1}\) give
\[
 e^{\lambda d_f(Y)}|V^{\rm W3}(Y)|
 \le4(\mathfrak b/R)^3e^{-|Y|}\sum_{p:X_p\subset Y}B_pe^{(\lambda+1)|X_p|}
 \le4(\mathfrak b/R)^3e^{16(\lambda+1)}|Y|e^{-|Y|}\sup_\Delta\sum_{p:X_p\ni\Delta}B_p .
\]
The last supremum is at most \(\tfrac54C_0^2\ell^{2q}C_{\rm pl}M^4\), and \(|Y|e^{-|Y|}\le1\). With \(\mathfrak b/R=C_{\rm win}A_1\ell^{p_0-q}\) this is (5.1) (\(4\cdot\tfrac54\cdot2=10\) allows for \(x_p\) versus \(\theta\)). (4) The prefactor of \(\ell^{3p_0-q}\) is fixed once \(M\) and the late amplitudes \(C_0,A_1\) are fixed; \(\ell\ge\log\gamma^{-2}\to\infty\). \(\square\)

*Status: proved*, conditional on [NL1-L] and [DOM-curv]. **Constant-order requirement:** \(q>3p_0\). IN1 row 1 has \(q>\max(p_0+2r,Cp_0)\) with an unspecified power-count constant \(C\); W3 needs \(C\ge3\). Enlarging \(C\) before choosing the exponents keeps row 1 feasible: its other conditions \(p_0>3Cr\) and \((p_0+Cr)/2<p_1<p_0-Cr\) are nonempty for \(p_0>3Cr\).

### 5.2 Jacobians

**[JAC] (import, items 4–5).** The chart and Haar Jacobian of the step's fluctuation coordinates is a finite product \(j(P;u)=\prod_\nu j_\nu(P;u|_{\mathrm{st}_\nu})\) over stencils of lattice diameter at most \(c_{\rm rd}\), at most \(C_{\rm jac}M^4\) of them meeting a fine cube. Each \(j_\nu\) is holomorphic in \(u\) on \(\|u\|_\infty<\rho_J\) and in the pair on the fibre, real and positive at real data, and \(|\log j_\nu(P;u)-\log j_\nu(P;0)|\le C_J\) there, with the branch continued from the real value. The constants \(\rho_J,C_J,C_{\rm jac}\) are early.

**Proposition 5.2.** Under [JAC], with \(u=x^{-1/2}\zeta\) and the ceiling \(4g\mathfrak b\le\rho_J\), the potentials \(V^{\rm J}(X_\nu)=\log j_\nu(P;u)-\log j_\nu(P;0)\) on the cube sets \(X_\nu\) meeting \(\mathrm{st}_\nu\) satisfy, on the box, \(|V^{\rm J}(X_\nu)|\le4C_Jg\mathfrak b/\rho_J\), and
\[
 \sup_Y e^{\lambda d_f(Y)}\sum_{\nu:X_\nu=Y}|V^{\rm J}(X_\nu)|\le a_{\rm J}:=
 4e^{15\lambda}C_{\rm jac}C_JM^4\,g\mathfrak b/\rho_J\longrightarrow0 .
\]
*Proof.* \(x\ge\tfrac34\theta\) gives \(\|u\|_\infty\le2g\|\zeta\|_\infty\le2g\mathfrak b\le\rho_J/2\). For fixed direction, \(t\mapsto\log j_\nu(u_0t/\|u_0\|)-\log j_\nu(0)\) vanishes at zero and is bounded by \(C_J\) on \(|t|<\rho_J\); Schwarz gives \(C_J\|u\|/\rho_J\). Each \(X_\nu\) has at most 16 cubes, \(d_f\le15\). \(g\mathfrak b=C_{\rm win}A_1g\ell^{p_0}\to0\). \(\square\) *Status: proved*, conditional on [JAC]. The vanishing order 1 suffices; this is NL1-L's listed case \((O(1),1)\).

### 5.3 Profile and coupling differences

**Proposition 5.3.** Write the Wilson part as \(-x\sum_pa_p(\Pi^{\rm W})-\sum_p(x_p-x)a_p(\Pi^{\rm W})\), with \(x\) the step's scalar coupling and \(|x_p-x|\le2t(\theta)\) (both lie in the tube (3)). Apply Lemma 4.1 with \(k=1\) to \(\Phi^{\rm pr}_p=-(x_p-x)a_p(\Pi^{\rm W})\). The resulting potentials \(V^{\rm pr}\) obey, on the box,
\[
 |V^{\rm pr}(Y)|\le a_{\rm pr}e^{-\lambda d_f(Y)},\qquad
 a_{\rm pr}=8e^{16(\lambda+1)}C_{\rm pl}C_0^2C_{\rm win}A_1M^4\,(t/\theta)\,\ell^{q+p_0}.
\]
By IN1 (3), \(t\alpha_0\delta=C_0A_1(t/\theta)\ell^{q+p_0}\to0\); hence \(\sup a_{\rm pr}\to0\).

*Proof.* As in Theorem 5.1, with \(B_p\le2t\cdot\tfrac12\cdot2C_0^2g^2\ell^{2q}\eta^4=2(t/\theta)C_0^2\ell^{2q}\eta^4\), \(k=1\) (factor \(2(\mathfrak b/R)\)). \(\square\) *Status: proved*, conditional as Theorem 5.1. This is the "coupling-profile term" of nl1-L L377: the background-map read is the response inside \(\Pi^{\rm W}\), and Lemma 4.1 localizes it.

### 5.4 The Gaussian part and the two defects

At \(s=\mathbf1\), write the second-order Taylor polynomial of the Wilson-plus-gauge exponent of (2.1) in the normalized coordinates as \(c(P)+\langle L(P),\zeta\rangle+\tfrac12\langle\zeta,H(P)\zeta\rangle\). The gauge part contributes exactly \(-\tfrac12\langle\zeta,\mathsf C_V^{\mathsf T}\mathsf G^{\rm Y}_V\mathsf C_V\zeta\rangle\) and nothing linear (hma Lemma 4.1, L236–238, checked: \(\widehat W(tD)=e^{iH(t)}\), \(\operatorname{tr}H=0\)). **Gaussian part (definition).** \(-\tfrac12\langle\zeta,\mathsf A^{\rm Y}(P)\zeta\rangle\), with \(\mathsf A^{\rm Y}\) as in [HM]. The **linear defect** is \(V^{\rm lin}=\langle L(P),\zeta\rangle\) and the **quadratic defect** is \(V^{\rm quad}=\tfrac12\langle\zeta,K(P)\zeta\rangle\), \(K:=H+\mathsf A^{\rm Y}\). The constant \(c(P)\) is a normalization.

hma proves G-ID(cov) only at physical pairs: Theorem 6.6 (L509–513) at a block-axial physical pair \(P_W=(U_+,0,J(U_+))\), extended to all of R4 by Corollary 6.7. Its Definition (L415) defines the Gaussian part "At a physical pair". So hma does **not** give \(K=0\), \(L=0\) at the complex points of the fibre. The UM1 norm of these defects is part of UM1-rest. I bound it by analyticity in the pair, with one new import.

**[HOL-K] (import, items 4 and 6).** There are early \(\rho_K>0\), \(K_H\ge1\), \(c_H>0\) such that, for every main step and every real input factor \(U_+\) of the actual history (the block-axial critical background, satisfying hma PH1–PH4), the maps \(P\mapsto L(P)\), \(P\mapsto K(P)\) are holomorphic on
\[
 \mathcal N_K(U_+)=\{(U_+,A',\mathbf J):\|A'\|_{w}<\rho_K,\ \|\mathbf J-J(U_+)\|_{w}<\rho_K\}
\]
(the weighted norms of R4), with \(|L_\beta|\le K_H\) and \(|K_{\beta\beta'}|\le K_He^{-c_Hd(\beta,\beta')}\) there (\(d\) in lattice units). This asks for the background map, the response and the operator chain of \(\mathsf A^{\rm Y}\) on a ball of **fixed** radius, not only on the running chain domain. For \(\mathsf A^{\rm Y}\) this is descent Theorem 5 on R4 with fixed ceilings (7); for \(H\) it is the P81 chart's holomorphy (cp12 D3) with walk decay.

**Theorem 5.4 (defect potentials).** Assume [HM] (G-ID(cov) at \(P_W\)) and [HOL-K]. Let the step's fibre satisfy \(\|A'\|_w<a_1\), \(\|\mathbf J-J(U_+)\|_w<j_1\), with \(a_1+j_1\le\rho_K/2\). Then on the fibre
\[
 |L_\beta|\le\epsilon_K:=K_H(a_1+j_1)/\rho_K,\qquad
 |K_{\beta\beta'}|\le\epsilon_Ke^{-c_Hd(\beta,\beta')} .
 \tag{5.2}
\]
Group \(V^{\rm lin}\) by the fine cube owning \(\beta\), and assign each pair \((\beta,\beta')\) of \(V^{\rm quad}\) to the cube set \(Y_{\beta\beta'}\) of a fixed shortest cube path between their owning cubes. If \(M\ge2\lambda/c_H\), these potentials satisfy UM1:
\[
 |V(Y)|\le a_Ye^{-\lambda d_f(Y)}\Bigl(1+M^{-4}\sum_{b\subset Y}|\zeta(b)|^2\Bigr),\quad
 a_{\rm lin}\le6\,\epsilon_KM^4,\quad
 a_{\rm quad}\le e^{\lambda}C_{\rm dec}\epsilon_KM^4,
 \tag{5.3}
\]
with \(C_{\rm dec}=\sup_\beta\sum_{\beta'}e^{-c_Hd(\beta,\beta')/2}\) (early). Since \(a_1=\alpha_{1}(i-1)=C_1g\ell^q\to0\) and \(j_1\to0\) under the running ceilings, \(\sup(a_{\rm lin}+a_{\rm quad})\to0\) as \(\gamma\downarrow0\) at fixed \(M\).

*Proof.* Fix \(P\) on the fibre and put \(P(t)=P_W+t(P-P_W)\). For \(|t|<T:=\rho_K/(a_1+j_1)\ge2\), \(P(t)\in\mathcal N_K(U_+)\). At \(t=0\), hma Theorem 6.6 gives no linear term and Hessian \(-\mathsf A^{\rm Y}(P_W)\), so \(L(P_W)=0\), \(K(P_W)=0\). Each entry is holomorphic in \(t\), bounded by \(K_H\) (times \(e^{-c_Hd}\) for \(K\)) and zero at \(t=0\). The Schwarz lemma at \(t=1\) gives (5.2).

For \(V^{\rm lin}\) on a cube \(\Delta\) (at most 12\(M^4\) coordinates, hma \(n_c=12\)): \(|z|\le\tfrac12(1+|z|^2)\) gives \(|\sum_{\beta\in\Delta}L_\beta\zeta_\beta|\le\epsilon_K(6M^4+\tfrac12\sum|\zeta_\beta|^2)\le6\epsilon_KM^4(1+M^{-4}\sum|\zeta|^2)\); \(d_f=0\).

For \(V^{\rm quad}\): if \(d_f(Y)=n\), the assigned pairs have \(d(\beta,\beta')\ge(n-1)M\). Use \(|\zeta_\beta\zeta_{\beta'}|\le\tfrac12(|\zeta_\beta|^2+|\zeta_{\beta'}|^2)\) and split \(e^{-c_Hd}=e^{-c_Hd/2}e^{-c_Hd/2}\). The first half is at most \(e^{-c_H(n-1)M/2}\le e^{-\lambda(n-1)}\) by \(M\ge2\lambda/c_H\). The second half, summed over the partner, is at most \(C_{\rm dec}\). So \(e^{\lambda n}|V^{\rm quad}(Y)|\le e^{\lambda}\tfrac12\epsilon_KC_{\rm dec}\sum_{b\subset Y}|\zeta_b|^2\le e^\lambda C_{\rm dec}\epsilon_KM^4\cdot M^{-4}\sum_{b\subset Y}|\zeta_b|^2\). \(\square\)

*Status: proved*, conditional on [HOL-K] and hma Theorem 6.6/Corollary 6.7 (unrefereed). If [HOL-K] fails, UM1-rest has an unbounded quadratic defect and hma's handoff is incomplete; see §15.

### 5.5 The gauge type (checked)

hma Theorem 4.3 (L264–282): I checked the proof. The order-three vanishing of \(f_{b,x}\) in (4.1) holds because the gradient vanishes (hma Lemma 4.1) and the subtracted quadratic term is the \((b,x)\) summand of the Hessian, with no pivot-curvature term since the gradient is zero. The scaling step \(x|f|\le F_*\rho'^{-3}\delta_jx\nu^2\) uses \(\nu\le\delta_j\) on the box and \(x\nu^2=|b|^2_{{\rm st},\infty}\). No failing step. Its norm is \(a_{\rm GF}=e^{32\lambda_V}F_*\rho'^{-3}N_{\rm ov}M^4\delta_j\), and \(a_{\rm GF}\le W_0/4\) is a row-9 ceiling.

## 6. Class terms (H-C)

The class terms are the carried S, Z, E, R, B (non-exempt) and K kinds. Under (2.1) each is \(F_f=f(\Pi_f;\mathfrak q_f)\) with nl1-L Theorem 4's switched presentation. Theorem 4 clause 4 gives \(|F_f-f_0|\le\omega_f=2b_f\), where \(b_f\) is the bound of the old activity on its declared domain ([CI-old]). H-C asks for the carrier sum (5). Two things must be checked: the carrier weight, and the sum over all carried families.

### 6.1 One family

**Geometric fact (G1).** Let \(X\) be a connected union of level-\((i-1)\) \(M\)-cubes with \(d=d_{i-1}(X)\) (IN1 L44: tree length in \(X\) meeting its cubes, divided by \(M\)), and let \(X_f\) be the fine cubes meeting the \(c_{\rm rd}\)-neighbourhood of \(X\), \(c_{\rm rd}<M\). Then
\[
 |X|\le|X_f|\le c_X(1+d),\qquad c_X:=2\cdot7^4=4802 .
\]
*Proof.* Let \(T\) be a minimal tree, of length \(dM\). Its doubled Euler walk is a closed path of length \(2dM\). Points at arc-length spacing \(M\) along it, at most \(2d+2\) of them, lie within \(M\) of every point of \(T\). Every cube of \(X\) meets \(T\), so lies in the sup-ball of radius \(2M\) about one of these points; its \(c_{\rm rd}\)-neighbourhood lies in the ball of radius \(3M\). A box of side \(6M\) meets at most \(7^4\) cubes of side \(M\). So \(|X_f|\le7^4(2d+2)\le c_X(1+d)\). \(\square\)

**Entropy (G2).** Let \(\mathcal X_n(\Delta)\) be the set of connected level-\((i-1)\) polymers \(X\) with \(n\le d_{i-1}(X)<n+1\) and \(X_f\ni\Delta\). Since \(X\) contains one of the 81 cubes within distance one of \(\Delta\), and \(|X|\le c_X(2+n)\) by (G1), the rooted animal count (td Lemma 1(1): at most \(6400^{k-1}\) rooted connected sets of \(k\) cubes) gives \(\#\mathcal X_n(\Delta)\le81\sum_{k\le c_X(2+n)}6400^{k-1}\le162\cdot6400^{c_X(2+n)}\).

**Lemma 6.1 (single family).** Let \(G\) be a family carried from level \(j=i-1-\nu\) with class norm \(\|G\|_{j,\kappa}\le E_*\) (IN1 (4), L46–49), pointed or not, and let its carried terms have the presentations of Theorem 4 with \(\omega_f=2b_f\), \(b_f\le E_*e^{-\kappa d_j(X)}\). Put \(\alpha'=\kappa/(2c_X)\).

(a) If \(\nu=0\) and \(\kappa\ge\kappa_{\rm ent}:=4c_X\log6400+4\), then
\[
 \sup_\Delta\sum_{f\in G:X_f\ni\Delta}\omega_fe^{\alpha'|X_f|}\le N_C^{(0)}:=972\,c_X\,e^{\kappa/2}\,6400^{2c_X}E_* .
 \tag{6.1}
\]
(b) For \(\nu\ge1\) the same argument gives the bound \(L^{4\nu}N_C^{(0)}\), and no bound uniform in \(\nu\) follows from \(\omega_f=2b_f\): a family whose members on single level-\(j\) cubes attain \(|f|=E_*\) has at least \(L^{4\nu}\) members with carrier through \(\Delta\), each with \(\omega_f\) up to \(2E_*\).

*Proof.* (a) A pointed member \((X,z)\) has \(|X|\le c_X(1+d)\) choices of \(z\). By (G1), \(\omega_fe^{\alpha'|X_f|}\le2E_*e^{-\kappa d}e^{(\kappa/2)(1+d)}=2E_*e^{\kappa/2}e^{-\kappa d/2}\). Summing with (G2),
\[
 \sum\le2E_*e^{\kappa/2}\sum_{n\ge0}c_X(2+n)\cdot162\cdot6400^{c_X(2+n)}e^{-\kappa n/2}.
\]
Since \(\kappa/2\ge2c_X\log6400+2\), \(6400^{c_X(2+n)}e^{-\kappa n/2}\le6400^{2c_X}e^{-2n}\). Also \(\sum_{n\ge0}(2+n)e^{-2n}=2/(1-e^{-2})+e^{-2}/(1-e^{-2})^2<3\). So the sum is at most \(2E_*e^{\kappa/2}\cdot162\cdot3c_X\cdot6400^{2c_X}=N_C^{(0)}\). (b) The projection to level \(i-1\) does not increase tree length (cls Lemma 2), so the per-member estimate is unchanged; the count of level-\(j\) polymers whose projected carrier meets \(\Delta\) gains the factor \(L^{4\nu}\) (the number of level-\(j\) cubes in a level-\((i-1)\) cube). The example shows the factor is attained by \(\omega_f=2b_f\). \(\square\)

*Status: proved.* **Correction to ci-form H-C (5).** (5) uses \(\alpha=\kappa/2\) on complete carriers. A member at class rate \(\kappa\) pays \(e^{(\kappa/2)|X_f|}\) only if \(|X_f|\le2(1+d)\), which fails for complete carriers (already \(|X_f|\) can be \(81|X|\)). With \(\alpha'=\kappa/(2c_X)\), ci-form Lemma 1 needs \(\lambda+1\le\alpha'\). This holds if, in ci-form (15)/IN1 (24), \(C_h^{\rm WF}\ge c_X\): then \(\lambda<\kappa/(2C_h^{\rm WF})-\varepsilon_{\rm rate}\le\kappa/(2c_X)-1\). \(C_h^{\rm WF}\) is enlarged before \(L\) (ci-form row 1, L138), so this is a row-2 floor and creates no cycle (§13).

### 6.2 All carried families

The main step's exponent carries the regular families \(E^{(j)}\), the remainders \(R^{(j)}\), the defects and the non-exempt boundary terms of **every** earlier level \(j\le i-1\). IN1's class (L217) bounds each family separately, \(\|E^{(j)}\|\le E_0\), and its list size (L127) weights them by \(f_{n+1-j}\), with \(f_\nu\le C_{\rm age}\nu^aL^{-b_{\rm age}\nu}\) (IN1 (13), L138–139). SA's Theorem 2.1 writes the action as \(-A+\mathbf E_k+\mathbf R_k+\mathbf B_k-\mathcal E_{k,\mathcal S}\) with these families (SA 17263), and "Neither \(E^{(j)}\) nor \(R^{(j)}\) carries a label index" (SA 17280). By Lemma 6.1(b), H-C needs, for older families, a gain beyond \(\omega_f=2b_f\). The gain is the one SA states for its localization rule.

**OSF-loc (the needed input).** For every \(\nu\ge0\) and every family \(G\) carried from level \(j=i-1-\nu\) into the main step (pointed regular members after their own-coefficient tent subtraction, IN1 L64; defects; remainders; non-exempt boundary terms), grouped into **pointed totals** per base point, the presentations of Theorem 4 satisfy
\[
 \sup_\Delta\sum_{f\in G:\,X_f\ni\Delta}\ \sup_{\mathbb S_{X_f}\times\mathbb D_R}|F_f-f_0|\;e^{\alpha'|X_f|}
 \le C_{\rm OSF}\,f_\nu\,\|G\|_{j,\kappa},
 \tag{6.2}
\]
with \(f_\nu\) as in IN1 (13) (and \(f_0\ge1\)), and \(C_{\rm OSF}\) fixed before \(\gamma\). For remainders and defects the right side may instead be \(C_{\rm OSF}(1+\nu)\|G\|\) with \(\|G\|\) as in SA (OSF5) (SA 19609–19611), whose \(\nu\)-sum SA (OSF6)–(OSF7) bounds (SA 19613–19645).

This is SA's OSF3–OSF4 (SA 19581–19595) in the form H-C reads: OSF3 bounds "to a window of level \(n\), after its vacuum and quadratic subtractions" a member's contribution by \(C\|G_{j,z}\|\rho_{jn}^3\epsilon_{jn}^{4+\alpha}\), \(\epsilon_{jn}=L^{-(n-j)}\), and "A window of level \(n\) contains at most \(C\epsilon_{jn}^{-4}\) base points of level \(j\)" (SA 19597–19599). Their product is \(\rho^3\epsilon^\alpha\), which is the form of \(f_\nu\).

**Theorem 6.2 (H-C, conditional).** Assume [CI-old], [NL1-L] for every carried term, OSF-loc, and IN1's list-size bound \(\sum_jf_{i-j}\|E^{(j)}\|+\sum_jw_{i-1,j}\|R^{(j)}\|\le N_*\) (IN1 L127). Then H-C (5) holds with \(\alpha'\) in place of \(\kappa/2\) and
\[
 N_C\le C_{\rm OSF}(N_*+C_{\rm R})+N_C^{\rm cur},
\]
where \(C_{\rm R}\) is SA (OSF6)'s remainder sum and \(N_C^{\rm cur}\) is Lemma 6.1(a) applied to the current-level strip and elimination kinds (bounds \(b_f\) from H-ACT's S/Z rows). All are fixed in rows 7–8, before \(\gamma\).

*Proof.* Sum (6.2) over families; the list-size bound and (OSF6) bound the sum of the right sides. Connectivity, exact component locality and \(F_f(s,0)=f_0\) are Theorem 4 clauses 2–3. \(\square\)

*Status:* the reduction is **proved**; **OSF-loc is Outstanding**. It is the first item-8 statement I cannot prove; §14 gives the three attacks. With \(N_C\) bounded, ci-form Lemma 1 gives the class potentials \(|V^C(Y)|\le(\mathfrak b/R)N_Ce^{-\lambda d_f(Y)}\) (ci-form (19)), which tend to zero with \(\gamma\).

## 7. Standing islands: H-I and the complex island amplitude

ci-form H-I (L372–378) asks for a pointwise decomposition (32) on the whole fibre, and td A (L51–63) asks for the complex deficit (5). td L63 says neither the real base value nor PAN's real estimate supplies (5), and gives the example \(-N(1+z/2)/(1-z/2)\). I show that IN1's **two-sided** oscillation import H-O supplies both consumer bounds, so that islands become two-sided exempt terms.

IN1's island data (L86–92, L217): \(\Phi_\omega(\xi;\mathbf p)=\Phi^\circ_\omega(\xi)+\sum_f\Phi_{\omega,f}(\xi;\mathbf p)\), each \(\Phi_{\omega,f}\) supported on a carrier \(R_f\), Borel in \(\xi\), holomorphic in \(\mathbf p\) on the fixed creation domain \(\mathcal D^{\rm cr}_\omega\), real at real pairs. The oscillation (8) is \(\sup_{\xi,\mathbf p,\mathbf p'}|\Phi_{\omega,f}(\xi;\mathbf p)-\Phi_{\omega,f}(\xi;\mathbf p')|\) over **complex** \(\mathbf p,\mathbf p'\in\mathcal D^{\rm cr}_\omega\). H-O (18) bounds \(\sum_{f:R_f=R}\operatorname{osc}\Phi_{\omega,f}\le B_\Phi(\log\theta_m)^{2p_0}e^{-\kappa d^\natural_m(\mathcal S;R)}\), with \(m\) the creation level.

**Theorem 7.1 (islands from H-O).** Assume [H-O] and [DOM-I]. Fix a real reference pair \(\mathbf p_\omega\in\mathcal D^{\rm cr}_\omega\) (the step's real input pair, restricted). For each carrier piece put \(\Phi^{\rm ref}_{\omega,f}(\xi)=\Phi_{\omega,f}(\xi;\mathbf p_\omega)\) (real), and \(\Psi'_\omega=\Phi_\omega-\Phi^\circ_\omega-\sum_f\Phi^{\rm ref}_{\omega,f}\). Let \(O_\omega=\sum_f\operatorname{osc}\Phi_{\omega,f}\). Then, at every pair where the step evaluates the island:

1. \(|\Psi'_\omega|\le O_\omega\). In particular \(\operatorname{Re}\Psi'_\omega\le O_\omega\), which is ci-form (33) with \(C_IN_0\) replaced by \(O_\omega\), and \(\sup|e^{\Phi_\omega}|\le e^{\Phi^\circ_{\omega,*}+\sum_f\Phi^{\rm ref}_{\omega,f}+O_\omega}\).
2. Each carrier piece \(\Phi_f(P,h):=\Phi_{\omega,f}(\xi;\rho^{\rm res}(P\dotplus h^\delta))\), on td A's admitted shift ball, satisfies td (5) with \(A_f:=\sup\operatorname{Re}\Phi_f\) and \(B_f=2\operatorname{osc}\Phi_{\omega,f}\).
3. Hence each piece is a **two-sided** exempt term in td's sense, with \(\widetilde\omega_f\le2\operatorname{osc}\Phi_{\omega,f}\), old length \(d_f^{\rm old}=d^\natural_m(\mathcal S;R_f)\), and \(\widehat\omega_f=2B_\Phi(\log\theta_m)^{2p_0}\) in td X (6).

*Proof.* (1) By [DOM-I] every evaluated pair and \(\mathbf p_\omega\) lie in \(\mathcal D^{\rm cr}_\omega\); the definition of oscillation bounds each \(|\Phi_{\omega,f}(\xi;\mathbf p)-\Phi^{\rm ref}_{\omega,f}(\xi)|\); sum over \(f\). The exponential bound follows from \(|e^w|=e^{\operatorname{Re}w}\). (2) For \(h\) in the shift ball and \(P\) in the fibre, both \(\rho^{\rm res}(P\dotplus h^\delta)\) and \(\rho^{\rm res}(P\dotplus h_0(P)^\delta)\) are evaluated pairs. So \(\operatorname{Re}\Phi_f(P,h)\le\Phi^{\rm ref}_f+\operatorname{osc}\) and \(\operatorname{Re}\Phi_f(P,h_0(P))\ge\Phi^{\rm ref}_f-\operatorname{osc}\). Subtract. (3) Two-sided: \(|\Phi_f(P,h)-\Phi_f(P,h')|\le\operatorname{osc}\) for any two admitted shifts, so the oscillation form of td A applies with \(\omega_f=\operatorname{osc}\). Group the pieces of one carrier and use (18). \(\square\)

*Status: proved*, conditional on [H-O] (IN1 import, item 10) and [DOM-I] (item 5). Three consequences:

- td's Outstanding "complex island amplitude" (L63) and ci-form's H-I (L394) are **not separate item-8 obligations**: H-O, which IN1 already imports, supplies the consumer bounds, provided [DOM-I] holds. td's counterexample function \(-N(1+z/2)/(1-z/2)\) has unbounded oscillation, so H-O excludes it.
- H-I's own pointwise form (32), with \(\Phi^\circ\) real and \(q\ge0\), is not needed by any CI consumer. It may still be needed by IN1's mass (Theorem 10), which is item 10's.
- The island pieces carry their **true** old length \(d^\natural_m(R_f)\), not zero as td X (L71) puts it. With zero length the per-read sum would count all carriers in the hull at no cost.

**Remark (what H-O does not give).** nl1-L's I-row bound \(\operatorname{Re}\Psi\le C_\Psi V^\circ\) (L188) is linear in \(\log x\) through \(V^\circ\) (IN1 (6)), whereas \(O_\omega\) carries \((\log\theta_m)^{2p_0}\) with \(p_0>6r\ge12\). Theorem 4 does not use the size of \(B_f\), and td X allows polynomial \(\ell\) factors, so the weaker form suffices for CI. The creation level \(m\) can, however, be arbitrarily old: \(\ell_m\) is not bounded by a power of the current \(\ell\). This is the age problem of nl1-L L504–512; see §11.1 (AGE).

## 8. Exempt terms: X°, X and ordinary TD

The exempt terms are the boundary terms whose relative tree excuses a hull, the kept forms, and the island pieces of Theorem 7.1, all of whose carriers meet a hub or the live set. Ordinary TD is td2 Theorem 3 (L111–158). Its imports are td's R, A, X, G, RUN and the two added hypotheses X° (L76–80) and G-ord (L73–74). R is [DR]; A is Theorem 4's admission plus, for islands, Theorem 7.1(2); G is [GEOH]; RUN is [RUN]. This section supplies X° and the current-level part of X, and checks td2 Theorem 3.

### 8.1 X° at the current level

**Lemma 8.1 (X° from a relative tree).** Let an exempt term \(f\) be filed at level \(i-1\) on a domain \(X\) with an admissible relative tree \(T\) in SA's in-domain convention (SA 6191–6198; cls D1, L13–15): \(T\subset X\) has lattice length \(d_f^{\rm old}M\), meets every unexcused cube of \(X\) and each chosen hull \(H_k\subset X\). Let its complete reads lie within lattice distance \(c_{\rm rd}<M\) of \(X\). Then X° holds with
\[
 C_{\rm pr}=2,\qquad c=2 .
\]
*Proof.* As in (G1), choose points \(w_0,\dots,w_n\), \(n\le2d_f^{\rm old}+1\), at arc-length spacing \(M\) along the doubled Euler walk of \(T\). Consecutive points are at sup-distance at most \(M\), so their owning cubes are equal or corner-adjacent. These cubes form a walk with at most \(n\le2(1+d_f^{\rm old})\) steps; let \(T_f\) be a spanning tree of it. Every point \(y\in T\) is within \(M\) of some \(w_k\), so its cube is within cube distance one of \(T_f\).

Take a read \(x\in X_f\); it is within \(c_{\rm rd}<M\) of a cube \(\Delta\subset X\), so its cube is within distance one of \(\Delta\). If \(\Delta\) is unexcused, \(T\) meets \(\Delta\), so \(\Delta\) is within one of \(T_f\), and \(x\) is within two. If \(\Delta\subset H_k\), then \(x\)'s cube lies in \(N_1(H_k)\subset\widetilde H_k=N_2(H_k)\subset\widetilde H_k^+\). Since \(T\) meets \(H_k\), \(T_f\) meets \(N_1(H_k)\subset\widetilde H_k\), so the hub is met by \(T_f\). Exemptness gives that \(X_f\) meets a hub or the live set. \(\square\)

*Status: proved.* \(C_{\rm pr}=2\) and \(c=2\) are geometric, independent of \(L,M,\kappa,\bar\kappa\), as G-ord requires (td2 L73). This discharges td2's Outstanding L82 for terms filed at the current level: the scale conversion is the walk argument, read coverage is the \(c_{\rm rd}<M\) floor, and hull containment is \(H_k\subset\widetilde H_k\).

### 8.2 X° for older exempt terms (member form)

**Lemma 8.2.** Let \(f\) be an exempt term carried from level \(j<i-1\) with a formation-time record in cls's recursive family (cls D3, L26–42), and suppose every chosen member has a standing successor. Then X° holds in the **member form**: \(|E(T_f)|\le C_{\rm pr}(1+d_f)\), and every read cube lies within \(c=2\) of \(T_f\) or in a member \(M_{i-1}(\alpha)\) whose core is met by \(T_f\). With the member form, td2 Lemmas 1–2 and Theorem 3 hold with \(\eta\) replaced by \(\eta_M=1+C_{\rm isl}/4\), provided \(\check R_{i-1}\ge R_\sharp\) (cls (5)) and \(\check R_{i-1}\ge R_M:=1+16(c+12)\) (a RUN ceiling).

*Proof.* cls Lemma 5 (L143–145, checked: members project into successor cores, cls (8)) gives a projected tree with at most \(d_f\) edges meeting every projected unexcused cube or a successor core. A read within \(c_{\rm rd}\) (level-\(j\) units) of the old domain lies within cube distance one of its projection; so it is within two of the projected tree, or in \(N_1(R_{i-1})\subset M_{i-1}=N_{\rho+3}(R_{i-1})\). For the connector inequality of td2 Lemma 1, cls (8) gives \(s(M)\le2C_{\rm isl}L\check R+6\) and \(d({\rm gas},M)\ge10L\check R-2-w^*\), \(w^*=\check R/(6(C_{\rm isl}+1))+c+12\). Then \(s(M)+2c\le\eta_M(d({\rm gas},M)-c)\) holds once \((C_{\rm isl}/4)(10L-1/6)\check R\ge2C_{\rm isl}L\check R+(1+C_{\rm isl}/4)(16+3c)\), true for \(L\ge27\) and \(\check R\ge R_M\). \(\square\)

*Status: proved* for standing successors. For **retired** (healed) islands the excused set has no successor member; their containment in the healed region is cls's Match-heal/LD, **Outstanding**. This is the precise residue of cls L147 ("Retired islands require healed-component containment").

### 8.3 X: per-read sums

**Lemma 8.3 (current-level per-read sums).** For exempt terms filed at level \(i-1\), with one slot per carrier and the class bounds (boundary \(\widetilde\omega_f\le2\mathsf Be^{-\kappa d^\natural}\); kept forms with H-ACT's \(O_f\le O_*e^{-\kappa d^\natural}\); island pieces by Theorem 7.1(3)), and \(\kappa\ge2\log76800\),
\[
 \sup_c\sum_{f:X(f)\ni c}\widehat\omega_fe^{-\kappa d_f^{\rm old}/2}
 \le N_{\rm ex}^{\rm cur}:=24(1+2(2C_{\rm isl}L^2\ell^r+6)^4)\,
   \bigl(\mathsf B+O_*+B_\Phi(\log\theta_{m_*})^{2p_0}\bigr),
\]
where \(m_*\) is the oldest creation level among the standing islands met.

*Proof.* cls Lemma 6 (L151–173, checked: rooted traversal codes \(6400^n\), at most three choices per island, \(6^{n+1}\) choices of excused data) gives \(\sum_{X\ni z}e^{-\kappa\delta^+(X)/2}\le12(1+2V_*)\), \(V_*=(D^*)^4\), and \(d^+\ge\delta^+\). Use \(\check R\le L\ell^r\) (nl1-L L374). \(\square\)

*Status:* proved for the current level. The **multilevel** sum (exempt terms from all earlier levels) and the **age** dependence through \(\log\theta_{m_*}\) are not bounded by a power of the current \(\ell\). Both are part of AGE (§11.1), **Outstanding**. IN1 L136 states the intended mechanism: "old boundary data enter only through a vanishing difference factor, a long-domain exponential, or a volume cost chosen after \(\mathsf B\)." It is not proved for the actual construction.

### 8.4 Check of td2 Theorem 3 (ordinary TD)

I checked td2 Lemma 1 (L86–102), Lemma 2 (L104–109) and Theorem 3 (L111–158) line by line against td Lemmas 1–4 (L94–172).

- td Lemma 2 (DR-row): the switch expansion around \(B_b\), the connectedness cancellation and repeated Schwarz in the source scalings are correct; the animal sum \(\sum_{n\ge n_0}6400^{n-1}D^{16-n}\le2D^{15}Q^{n_0-1}\) needs \(Q\le1/2\), which (33) gives.
- td Lemma 4 for islands uses the Borel–Carathéodory step about \(h_0\). With Theorem 7.1 the island pieces are two-sided, so that step is no longer needed.
- td2 Theorem 3: from (6) and (9), \(e^{\lambda_T{\rm St}(W)}|f_W|\le e^{\lambda_TC_{\rm pr}}\widehat\omega_f\vartheta_T^{|W|}e^{-(\kappa-\lambda_TC_{\rm pr})d_o-a_1m}\). Reserving \(\kappa d_o/2+a_1m/2\) and using \(\lambda_TC_{\rm pr}\le\kappa/4\) leaves exponent \(\ge\kappa d_o/4+a_1m/2\ge\nu(C_{\rm pr}d_o+m)\ge\nu(G_0-C_{\rm pr}-2c)\) by (10). The \(f\)-sum uses \(a_1/2\ge6\) and td Lemma 1's \(\sum_ye^{-6d(x,y)}\le2\). The tail limit uses RUN and \(e^x\ge x^n/n!\). **No failing step.**
- td2 (14)'s floor gives \(a_1\ge12\) for \(\eta=1+C_{\rm isl}/10\). With the member form (Lemma 8.2) replace \(C_{\rm isl}/10\) by \(C_{\rm isl}/4\) in (14); this is a larger floor on \(\bar\kappa\) only.

So **ordinary TD holds** (td2 Theorem 3), with amplitude \(a_T(\ell)\to0\), conditional on [DR], [NL1-L] admission, [GEOH], [RUN], Theorem 7.1, Lemmas 8.1–8.2, and X with \(N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}\). The last is proved at the current level (Lemma 8.3) and Outstanding in age (AGE). td2 Corollary 4 then gives connected exempt potentials with norm \(2a_T^*\).

## 9. The regular gas and normal (Mayer) domination

**Theorem 9.1 (CI-form for the main-step gas on the global fibre).** Assume the potential types of §§5–8 (W3, J, pr, lin, quad, GF, class, exempt) with UM1 bounds (25) at rate \(\lambda\) and total amplitude \(a\le a_*/2\) (Theorem 12.1), [HM] for H-G and H-S's Gaussian half, and ci-form's constant choices (12)–(18) with the corrections of §13. Then the gas (9)–(11) of ci-form satisfies ci-form (28)–(29) on the supplied fixed-\(U\) fibre, and each \(E(X)\) has a representation (18) with fixed \(\sigma\)-finite measures and an integrable \(P\)-independent majorant on every compact polydisc.

*Proof.* ci-form Lemmas 2–4 and Theorem 5 give (28)–(29). I checked Lemma 2 (L218–239): \(D_*\ge K^{-1}\), \(\|D_*\|\le K+K^4\), \(\|D-D_*\|\le5(K+1)^3\varepsilon\) by telescoping four factors, \(\|D^{-1}-D_*^{-1}\|\le10K^2(K+1)^3\varepsilon\le c_K/2\) under (13), hence \(\operatorname{Re}b^{\mathsf T}D^{-1}b\ge(c_K/2)|b|^2\) and the integrand bound \(e^{-c_K|b|^2/8}\) for \(\rho\le c_K/8\); (22) adds three terms each \(\le1/3\). Lemma 4's selection sum (L300–312) and the rooted tree bound (L323–328) are correct as written.

For (18), write every analytic operation as an integral against a fixed measure, keeping absolute values inside:
- the Gaussian functional is \(\int_{\mathbb R^m}F(P;b)\varrho_{D(P,t)}(b)\,db\), Lebesgue measure on the fixed real space (ci-form L46), density holomorphic in \((P,t)\);
- each coarse \(t\)-derivative and each switch derivative in Lemma 4.1 is a Cauchy integral over circles of fixed radius (arc-length measure), and each \([0,1]\)-integration is Lebesgue measure;
- each Mayer factor \(e^{V(Y)}-1\) is written as \(\oint_{|z|=\mathcal R_Y}(e^{zV(Y)}-1)\,\frac{dz}{2\pi i\,z(z-1)}\), which is exact since \(e^{zV}-1\) vanishes at \(z=0\) and \(\mathcal R_Y\ge2\).

The integrand's modulus, with the supremum over \(P\in K\) inside, is bounded by the same factors as in Lemma 4, except that each Mayer circle contributes \(2/\mathcal R_Y\) instead of \(1/\mathcal R_Y\). This replaces \(2a/W_0\) by \(4a/W_0\) in (26), i.e. \(A_a\) by \(2A_a\); the ceiling \(a\le a_*/2\) restores \(\tau\le1/2\). Lemma 2's density bound is uniform on compact \(K\). The cutoff factors are nonnegative and \(P\)-independent. Summing the absolute majorants over all lists, selections and pieces converges by Lemma 4's rooted bound. This is (18). \(\square\)

*Status: proved*, conditional on the potentials and [HM]. This is the "actual locally normal Mayer estimate" of nl1-L L615 for the main step's gas. It is a statement on the supplied global fibre. Three things are not supplied by it: activities on every declared **local** fibre, which needs filing (§10); LF1's Borel domination over stored-variable evaluation fibres, IN1 H-E (16), which is item 10's; and the stage and output formation rules, which CI-maps names (nl1-L L619–627).

## 10. Filing: (Cls+) and the matching hypotheses

CI requires the new activities to be IN1 class members on their full local domains (D4; td Theorem 9, L365–371). The gas logarithm \(E(X)\) of Theorem 9.1 reads the external pair on the presentation sets \(X_f\) of the exempt terms, which contain hubs, not only on the raw union \(X\) (td L375–377: "Boolean localization of \(B\) is not localization of \(P\)"). So it must be refiled on a carrier containing every pair read.

**What is proved, and by whom.** Pair locality of the response is frozen `dr.md` (Result L594: "DR algebraic, vanishing, component, fixed-pair row-locality and DR-locP implications for the specified ST1 current"). drlocp Theorem 3 (L428–454) gives a summable pair-labelled bound for the exempt potentials on filed labels \(Z_{f,W,V}\), using the collared excused family \(F_H\) of (24). cls (L61–69, Lemmas 2–8) replaces \(F_H\) by recursive members with bounded width (cls (7)) and repairs the nonbox shell count (cls (15), F4*). I checked cls Lemmas 2–5 (projection, no accumulation (6)–(7) by the rational series, member geometry (8)) and Lemma 8's shell sum (15) (ratio \(27e^{-12}<1/2\)). No failing step.

**Why the existing class cannot absorb the output.** Pair reads include a collar of width \(\rho_H\simeq\eta s_H\) around each hub (drlocp (24); needed for the forest sum, drlocp Lemma 5.3). With SA's family of uncollared hulls, every relative tree must meet each of the \(\gtrsim s_H^3\rho_H\) collar cubes, so the class weight \(e^{-\kappa d^\natural}\) costs at least \(e^{-\kappa s_H^3\rho_H}\), against the gain \(e^{-\nu G_0}\) with \(G_0\simeq10L\check R\) linear in \(s_H\). Shrinking the collar fails too: td2 (26) and drlocp L381 show the boundary-attachment majorant then diverges. So a changed excused family is needed (cls Amendment 2, L433–472, **not applied**).

**What remains (Outstanding).** cls Proposition 12 (L380–382) transfers IN1 Theorems 10–12 to the enlarged class only under Match-SF/O, Match-read/file, Match-heal/LD and Match-history (L371–378). cls Lemma 11 (L361–367) proves that core containment does not give scale filing. So Match-read/file's scale/rate transfer is a genuine obligation, not a bookkeeping step. Lemma 8.2 above supplies the read-coverage part of Match-read/file for standing successors. Retired islands and the long-domain bound \(d_j^+(X)\ge c_{\rm LD}\check R_k\) (cls L324–325) remain. drlocp's "formation and class matching" (L522–523) also remains: Theorem 3 bounds **potentials**, while class membership concerns the **activities** after Gaussian and Mayer formation; the weighted transfer is drlocp Proposition 6.2, conditional on G-P.

*Status:* **Outstanding.** I did not attack the matching hypotheses three times in this pass; they come after OSF-loc in item 8's order (§0), and OSF-loc already blocks H-C.

## 11. nl1-L's full-source distance bound, H-FL and H-ACT

### 11.1 The distance bound, and AGE

**Theorem 11.1 (the needed distance is to the fluctuation).** Let \(f\) be an exempt carried term of Theorem 4 with complete carrier \(X_f\), at fine-cube distance \(G(X_f)\) from the gas cubes. Under td G (gas cubes at distance \(\ge G_0=10L\check R_i-2\) from every hub and the live set) and \(c_{\rm rd}<M\), \(G(X_f)\ge G_0-2\). Hence, on \(\mathbb S_{X_f}(\bar\kappa_1)\times\mathbb D_R\),
\[
 |F_f-f_0|\le2\omega_f\,e^{-\kappa_s(G_0-2)}\,\|\zeta\|_\infty/R .
 \tag{11.1}
\]
In lattice units the distance is \(M(G_0-2)\ge10LM\check R_i-4M\), the size nl1-L L498 asks for, now measured to the fluctuation support.

*Proof.* Every read of \(f\) lies in a cube within one of a cube of its hub or live-set carrier (Lemma 8.1), and gas cubes are at distance \(\ge G_0\) from those. Apply Corollary 4.3. \(\square\)

So the stored source \(S(v_0)\), which nl1-L L495–497 notes "can meet the stored region near the activity", does not obstruct: by Lemma 4.2 it affects only \(f_0(P)\). No difference-response estimate about the stored source and no modified pinning is needed, because the pin reads only \(\mathrm{Rd}(y)\) (st1-r4 Lemma 4, L297) and these reads are inside \(X_f\). This answers the **first** point of nl1-L L494–502. *Status: proved*, conditional on Theorem 4 and td G.

**AGE (Outstanding).** The **second** point (L504–512) remains. The amplitude \(\omega_f\) of an old exempt term can carry \(\ell_m^\tau\) at its creation level \(m\) (for islands, \(\tau=2p_0\) by Theorem 7.1), and \(\ell_m\) is not bounded by a power of the current \(\ell\). The gain in (11.1), \(e^{-\kappa_s(G_0-2)}\) with \(G_0\ge10L(\ell-1)^r-2\), depends only on the current \(\ell\). Precisely, AGE is:

> For every main step, \(\sup_c\sum_{f\ \rm exempt,\ all\ creation\ levels}\widehat\omega_fe^{-\kappa d_f^{\rm old}/2}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}\), with \(C_{\rm ex},t_{\rm ex}\) fixed before \(\gamma\).

Lemma 8.3 proves it at one level and for creation levels with \(\ell_m\le\ell^{t'}\). The general case needs a retained age gain (nl1-L L512), for example a factor in the stored-island class decaying with age. Owner: LF1 (item 10), as part of H-O's creation-domain bound. Not attacked further here.

### 11.2 H-FL (6)

**Lemma 11.2 (stored-datum bound).** Assume **[TEST-v0]**: every free row of the stored datum \(v_0\) read by the step passed a free-row fluctuation test \(\|v_0(b)\|<\delta'_m=A_1g_m\ell_m^{p_1}\) at some level \(m\le i-1\), in the same unscaled matrix norm (dom Theorem 13, L291, uses this test form). If \(\gamma^{-2}\ge2e^{2p_1}\) and \(p_1\le p_0\) (IN1 row 1: \(p_1<p_0-Cr\)), and \(\gamma^{-2}\ge2c_5\), then \(\|v_0\|_\infty\le\sqrt2A_1g\ell^{p_0}\), i.e. (6) with \(C_{\rm st}=\sqrt2\).

*Proof.* Frame (1) gives \(\theta_m\ge\theta_{i-1}-c_5\ge\theta_{i-1}/2\) for \(m\le i-1\). The function \(\theta\mapsto\theta^{-1/2}(\log\theta)^{p_1}\) is decreasing for \(\log\theta>2p_1\) (derivative \(\theta^{-3/2}(\log\theta)^{p_1-1}(p_1-\tfrac12\log\theta)\)). So \(\delta'_m\le A_1(\theta_{i-1}/2)^{-1/2}(\log\theta_{i-1})^{p_1}\le\sqrt2A_1g\ell^{p_0}\), using \(\ell\ge1\) and \(p_1\le p_0\). (If \(\theta_{i-1}/2<e^{2p_1}\) the monotonicity is not available; the ceiling \(\gamma^{-2}\ge2e^{2p_1}\) excludes this.) \(\square\)

*Status: proved* conditional on [TEST-v0] (owner: ST1/DOM, the stored-threshold record F8 of nl1-L L154). This reduces H-FL's Outstanding to the record statement [TEST-v0]. The remaining H-FL clauses (holomorphy of \(S=b_V\circ a_V\), source-row range \(R_\sigma\), physical identification) are [DR]/[NL1-L] inputs.

### 11.3 H-ACT on the changed domains

nl1-L L195 lists five items. Their status here:

1. *Strip identification*: ST1's STRIP discrepancy bound (st1-r4 L156) is the strip row's \(b_f\); identification is part of (2.1)'s definition. **Reduced** to [ST1].
2. *W decomposition*: §5. **Proved** conditionally (Theorems 5.1, 5.4; Propositions 5.2–5.3).
3. *Logarithm branches* (Z kind): if \(|z^{(j)}-1|\le1/2\) on the declared domain, the principal \(\operatorname{Log}\) is holomorphic there, real at real points where \(z^{(j)}>0\), and \(|\operatorname{Log}z|\le2|z-1|\) (power series). The bound \(|z^{(j)}-1|\le1/2\) is an import ([ST1] elimination-factor bound). **Reduced.**
4. *Kept-form oscillation*: `gates/kept-cov-check.md` Defects 1–2 (relative-form carriage, native action). **Import**, unchanged.
5. *Island-domain inclusion*: [DOM-I]. **Import** (item 5).

The interface part of H-ACT (holomorphic, Borel, stored-slot, real tie, real gauge, real on real triples) for carried activities is [CI-old], as nl1-L Theorem 7's proof says (L593).

## 12. UM1 for the non-gauge types (hma's UM1-rest)

**Theorem 12.1 (UM1-rest, conditional).** Assume the hypotheses of Theorems 5.1, 5.4, 6.2, 7.1, Propositions 5.2–5.3, td2 Theorem 3 with Lemmas 8.1–8.2, and AGE. The non-gauge potential types of the main step are:
\[
 \text{W3 (5.1)},\ \text{J (5.2)},\ \text{pr (5.3)},\ \text{lin, quad (5.3)},\
 \text{class }V^C\ (\text{ci-form (19)}),\ \text{exempt }V^\circ\ (\text{td2 (15)}),
\]
with no free type (\(a_F=0\): (2.1) has none) and no insertion at zero source (\(w=0\); hma L300 is stated for the step without insertion). Each is holomorphic on its declared box and core, real at real data, gauge covariant, and satisfies UM1 (SA 14303–14318 form, ci-form (25)) at rate \(\lambda\), with total norm
\[
 a_{\rm rest}=a_{\rm W3}+a_{\rm J}+a_{\rm pr}+a_{\rm lin}+a_{\rm quad}+(\mathfrak b/R)N_C+2a_T^* .
\]
Every summand tends to zero uniformly in \(\theta\ge\gamma^{-2}\) as \(\gamma\downarrow0\), with \(M,\bar\kappa\) and all earlier constants fixed. Hence \(a_{\rm rest}\le W_0/4\) is a row-9 coupling ceiling, and with hma's \(a_{\rm GF}\le W_0/4\) the total is \(a\le W_0/2\). If also \(a\le a_*/2\) (Theorem 9.1), ci-form Lemma 4 and Theorem 5 apply.

*Proof.* The limits: \(a_{\rm W3}\propto\ell^{3p_0-q}\) with \(q>3p_0\); \(a_{\rm J}\propto g\ell^{p_0}\); \(a_{\rm pr}\propto(t/\theta)\ell^{q+p_0}\to0\) by IN1 (3); \(a_{\rm lin},a_{\rm quad}\propto a_1+j_1\to0\); \((\mathfrak b/R)N_C\propto\ell^{p_0-q}\) with \(N_C\) bounded by Theorem 6.2 (this is where OSF-loc enters); \(a_T^*\to0\) by td2 Theorem 3 (this is where AGE enters, through \(N_{\rm ex}\)). Each prefactor is fixed after \(M\) and before \(\gamma\) (§13). Holomorphy, reality and covariance are in the cited results. The structural interface of ci-form H-S for these potentials is inherited from the presentations: exact component locality and the real tie come from Theorem 4, restriction consistency from Lemma 4.1(c). \(\square\)

*Status:* **proved conditional on OSF-loc and AGE**, besides the named imports of items 3–6 and 10. Since OSF-loc fails to be supplied (§14), the honest conclusion is that hma's Corollary 4.5 (UM cost) holds for the actual gas exactly when OSF-loc and AGE do, and the imports hold.

## 13. Constant order (IN1 rows 1–10, with Amendment 1)

IN1's rule (in1 L223): "A returned constant must precede every choice it bounds." Below, "early" means fixed before \(\kappa\) and independent of \(M,\bar\kappa\). Every constant introduced here, with its row.

| Row | Constants fixed there (new or newly used here) | Reads |
|---|---|---|
| 1 | power-count \(C\ge3\), so \(q>3p_0\) (Theorem 5.1) in addition to IN1's \(q>\max(p_0+2r,Cp_0)\) | nothing later |
| 2 | geometric: \(c_{\rm rd}\) (read diameter), \(c_X=4802\) (G1), \(C_{\rm pr}=2\), \(c=2\) (Lemma 8.1), \(C_{\rm isl}\), \(\eta_M=1+C_{\rm isl}/4\) (Lemma 8.2), \(C_{\rm pl}\), \(C_{\rm lay}\); **\(C_h^{\rm WF}\ge c_X\)** (Lemma 6.1 correction), then odd \(L\) above IN1's floor \(4C_h^{\rm WF}C_h^{\rm UM}c_\ell(1+4\beta_s)\), Amendment 1's \(L_0^\natural\), td (32) and td2 (13)'s windows | row-1 exponents |
| 3 | [JAC]'s \(\rho_J,C_J,C_{\rm jac}\); (PIV), AV; [HOL-K]'s \(\rho_K,K_H,c_H\) and \(C_{\rm dec}\); [DR]'s base constants \(C_D,\mu,\epsilon_D\) (dr (9)) | \(L\) |
| 4 | \(\kappa\ge\max\{\kappa_0^\natural(L),\ \kappa_{\rm ent}=4c_X\log6400+4,\ 2\log76800\}\) and all IN1/td/td2/cls \(\kappa\)-floors; then \(\Theta\), \(\lambda\) in (24) (now \(\lambda+1\le\kappa/(2c_X)\)), \(\lambda_V,\lambda_T=\lambda_V+1\) | rows 1–3 |
| 5 | \(\bar\kappa\) with \(\log(e^{\bar\kappa}-1)\ge\lambda+1\), td (33), td2 (14) with \(C_{\rm isl}/4\) in place of \(C_{\rm isl}/10\), cls (16); then \(\bar\kappa_1=\bar\kappa-1\) (so \(\kappa_s=1\) in Lemma 4.2); fix \(s_D=\epsilon_De^{-64\bar\kappa}\), \(E_{\bar\kappa}=e^{48\bar\kappa}\) (dr (9)); then \(M\), a power of \(L\), with \(M>2c_{\rm rd}+2\), \(M\ge2\lambda/c_H\) (Theorem 5.4), and the IN1 (23), source and collar floors | rows 1–4 |
| 6 | late radii \(a_0=\alpha_0\), \(a_1=\alpha_1\), current ceiling \(j_0\); \(A_1\), then \(A_0\); \(C_0\), then \(C_1\) (nl1-L (8)) | rows 1–5 |
| 7–8 | \(E_N,E_0,N_*\), \(\mathsf B\), \(O_*\), \(B_\Phi\), \(C_{\rm OSF}\), \(C_{\rm R}\), hence \(N_C\) (Theorem 6.2); \(C_{\rm ex}(M),t_{\rm ex}\) (AGE); the prefactors of \(a_{\rm W3},a_{\rm J},a_{\rm pr},a_{\rm lin},a_{\rm quad}\) | rows 1–6 |
| 9 | \(\gamma\) small enough that: \(\gamma^{-2}\ge\max(2\bar B,e^{2q},2e^{2p_1},2c_5)\) ((5.0), Lemma 11.2); \(4g\mathfrak b\le\rho_J\); \(a_1+j_1\le\rho_K/2\); \(\check R\ge\max(R_\sharp,R_M)\); \(a_{\rm rest}\le W_0/4\), \(a_{\rm GF}\le W_0/4\), \(a\le a_*/2\); and all retained IN1/ST1/td/td2/drlocp/cls ceilings | everything before |
| 10 | torus, grid and \(\beta\) as in IN1 | — |

**No cycle.** Each new floor is on a constant chosen after the constants it reads. The only early change is \(C_h^{\rm WF}\ge c_X\), which precedes \(L\) and raises the \(L\)-floor; Amendment 1 says such floors "weaken no step" (in1 L674). The late amplitudes \(b_f\) enter only output bounds and the row-7–9 constants, as st1-r4 L1533 requires. In particular \(N_C\) is fixed in row 7–8 from \(N_*\) and \(C_{\rm OSF}\), and is read only by the row-9 ceiling \((\mathfrak b/R)N_C\le W_0/4\). \(M\) and \(\bar\kappa\) do not enter any early constant: the switch-shell rate \(\kappa_s=\bar\kappa-\bar\kappa_1\) is fixed in row 5, and Lemma 4.2's conclusion is used only in row-9 ceilings.

## 14. The first remaining Outstanding statement: OSF-loc

**Statement (OSF-loc).** For every main step, every age \(\nu\ge0\) and every family \(G\) carried from level \(j=i-1-\nu\) (pointed regular members grouped with their own tent counterterms, defects, remainders, non-exempt boundary terms), the presentations \(F_f\) of nl1-L Theorem 4 satisfy (6.2):
\[
 \sup_\Delta\sum_{f\in G:\,X_f\ni\Delta}\ \sup_{\mathbb S_{X_f}\times\mathbb D_R}|F_f-f_0|\;e^{\alpha'|X_f|}
 \le C_{\rm OSF}\,f_\nu\,\|G\|_{j,\kappa},\qquad f_\nu\le C_{\rm age}\nu^aL^{-b_{\rm age}\nu},
\]
with \(C_{\rm OSF},C_{\rm age},a,b_{\rm age}\) fixed before \(\gamma\) (remainders and defects: OSF5–OSF6 form).

By Lemma 6.1(b) the trivial bound \(\omega_f=2b_f\) gives the factor \(L^{4\nu}\) instead of \(f_\nu\). Three attacks follow, each new in this text, with the exact reason it fails.

**Attack 1: layer separation.** nl1-L Lemma 2 (L323–341) proves that a read \(b\) of input layer \(m_+(b)\) sees the substituted shift damped by \(e^{-\mu d_+(b,\mathcal S_{\rm src})/2}\), with \(d_+\ge\rho_0(i-1-m_+(b)-3)_+-C_{\rm car}\) (L130–131). If every read of an age-\(\nu\) member had \(m_+(b)\le i-1-\nu+3\), Schwarz would give \(|F_f-f_0|\le\omega_fCe^{-\mu\rho_0(\nu-3)_+/2}\), and the floor \(\mu\rho_0\ge2(4+b_{\rm age})\log L+2\log16\) (a legitimate choice after \(L\), since nl1-L's order fixes \(\rho_0\) after \(\mu\), L205) would give \(f_\nu\). *Why it fails:* the input layer is a property of the **bond's region** in ST1's separated longer sequence ("Input layers satisfy \(m_+(b)\le i\)", nl1-L L132), not of the creation level of the term that reads it. Old regular members whose domains lie in the current integration region are acted on by the current step: "Consider the part of the regular terms on a domain of level \(m\) that this integration takes" (SA 17459). Their reads are current-layer bonds, \(d_+(b,\mathcal S_{\rm src})\) can be zero, and there is no damping in \(\nu\).

**Attack 2: the member's own radius and field scaling.** A level-\(j\) member is holomorphic on \(\mathcal D_j(X)\) with radii \(\alpha_{\iota,j}\) in level-\(j\) units. For a field slowly varying on level-\(j\) scales, a level-\((i-1)\) link angle is the sum of \(L^\nu\) level-\(j\) angles to leading order, so a level-\((i-1)\) shift of size \(g\|\zeta\|\) induces a level-\(j\) shift of size about \(L^{-\nu}g\|\zeta\|\). Schwarz in the induced shift would give \(|F_f-f_0|\le2b_f\,C L^{-\nu}(\mathfrak b/R)(\theta_j/\theta)^{1/2}\). *Why it fails:* (i) The count of age-\(\nu\) base points per fine cube is \(L^{4\nu}\) (Lemma 6.1(b); SA 19597–19599), so the product is \(L^{3\nu}\): first-order vanishing supplies one power of \(\epsilon_{jn}=L^{-\nu}\), and four are needed. (ii) Even the one power is not available from the imports: [DR]'s (7) bounds the response's size, uniformly across layers within the same layer distance; it gives no gain \(L^{-\nu}\) for the induced fine-level field. That gain is a derivative bound on the background response on all layered levels, which is P82M's (15) (assembly-status item 1).

**Attack 3: gauge invariance, lattice symmetry, and order four.** Push the Taylor expansion in the induced shift to order four and use the members' structure. (a) Each member is gauge invariant (IN1 class, L217). So its first variation annihilates pure-gauge shifts, and in a smooth gauge the shift is bounded by the curvature change \(\delta F\sim L^{-2\nu}\) times the member's diameter. (b) Lattice hypercubic symmetry and charge conjugation leave no invariant 2-form at a flat background, so the first-order coefficient of \(\delta F\) is \(O(F_{\rm bg})=O(L^{-2\nu}\alpha)\). Then the first- and second-order terms are \(O(\|G\|\rho^2\epsilon^4)\) per base point, which is SA's (OSF4) (SA 19586–19590). Times \(\epsilon^{-4}\) base points, each age contributes \(O(\|G\|\rho^2)\). *Why it fails:* (i) The sum over ages of \(O(\|G\|\rho^2)\) diverges: at fixed current \(\theta\) the number of ages is \(\ge(\theta_0-\theta-c_5)/\bar B\), unbounded since \(\theta_0=\beta\) is arbitrary. The extra \(\epsilon^\alpha\) of (OSF3) needs the marginal (dimension-four) part removed: "subtracting its own coefficient times its own tent action cancels its marginal affine quadratic term at that base point" (SA 19566–19568), under "the full hypotheses of Section ch:pointed-hessian-cancellation, including gauge invariance, the actual normalized response, absolute Hessian moments and covariance of its pointed total under unit translations and the full hypercubic group" (SA 19562–19566). That is the coefficient identification of IN1 H-OL (in1 L110–118, Outstanding L118) and OL1's Ward and covariance hypotheses (in1 L64), assembly-status item 9. (ii) Steps (a)–(b) need the induced shift to be smooth with level-uniform derivative bounds, which is again P82M (15), item 1. (iii) The order-four Taylor step needs a lattice Poincaré bound for the gauge-invariant expansion with constants uniform in \(\nu\); I did not prove it here. SA itself says these summations "do not prove (OSF3). That estimate contains the renormalisation assertion: covariance of the pointed Hessian, the correct counterterm, regularity of the background within the window and uniform membership after substitution must be proved for the actual formation rule" (SA 19666–19670).

**Conclusion.** OSF-loc is the precise remaining lemma for H-C. Attack 3 reduces it to three inputs: P82M's level-uniform derivative bound (item 1); H-OL's pointed-Hessian cancellation with its coefficient identification (item 9); and a \(\nu\)-uniform lattice Poincaré expansion of gauge-invariant members (not attempted). The first two are owned by other critical-path items. **Consequence for the critical path:** item 8 (CI) depends on parts of items 1 and 9 through H-C. The order of assembly-status §3 ("Each depends only on earlier items", L178) must place OSF-loc before item 8, or move H-C's multilevel clause into item 9.

## 15. Statements in other texts used wrongly or more strongly than supplied

Frozen texts:

1. **nl1-L L188 (H-ACT I-row), frozen.** It requires \(\operatorname{Re}\Psi\le B_f:=C_\Psi V^\circ\), linear in \(\log x\) through IN1 (6). The supplier IN1 H-O (18) gives \(O_\omega\propto(\log\theta_m)^{2p_0}\), with \(p_0>6r\ge12\) (Theorem 7.1). No consumer of Theorem 4 uses the size of \(B_f\) (Theorem 4 clause 4 only defines \(\omega_f=B_f-f_0\)), and td X allows polynomial factors. So the I-row is **stronger than supplied and than needed**; read \(B_f=O_\omega\). This is not an error in Theorem 4's proof.
2. **nl1-L Lemma 3 (L343–367), frozen.** Its affine-read hypothesis is not satisfied by the actual Wilson and profile terms, which read the background map (as L377 says). It is not wrong; §5 replaces it by Lemma 4.1, which needs no affine read.
3. **nl1-L L494–498, frozen.** Correct as stated. The obstacle it names (the stored source near the activity) does not affect the oscillation (Lemma 4.2, Theorem 11.1). The age point (L504–512) stands (AGE).
4. **nl1-L L127, frozen (stale import, already in assembly-status §4.1).** It cites st1-r3 Lemmas 5, 8, 11; Lemma 5 is touched by Amendment CV. Nothing in this note depends on the comb versus mean choice: Lemmas 4.1–4.2 use only Theorem 4's clause 2.
5. **IN1 row 1 (in1 L227), frozen.** Not wrong; the power-count constant \(C\) must be at least 3 for W3 (Theorem 5.1).

Unrefereed texts (for the lead):

6. **ci-form H-C (5), L58–65.** The weight \(e^{(\kappa/2)|X_f|}\) on complete carriers is not paid by class rate \(\kappa\) (Lemma 6.1). Corrected to \(\alpha'=\kappa/(2c_X)\), with \(C_h^{\rm WF}\ge c_X\).
7. **ci-form H-C, scope.** N_C fixed before \(\gamma\) is not available for families carried from older levels without OSF-loc (Lemma 6.1(b)). ci-form does not say this.
8. **hma-draft §0 (L22) and L415.** "No item-6 statement is left Outstanding", but its Gaussian part is defined only "At a physical pair". UM1-rest's Wilson type contains the linear and quadratic defects off the physical locus; Theorem 5.4 bounds them only under the new import [HOL-K] (items 4 and 6).
9. **td L63 and td X (L71).** The complex island amplitude follows from IN1 H-O (Theorem 7.1). Island lengths should be the carrier lengths \(d^\natural_m(R_f)\), not zero.
10. **assembly-status L178.** The ordering claim fails for item 8 (§14).

## 16. Source checks

All SA lines refer to `ym4.tex` (the outline of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text) in the scratchpad copy. Each was read in a bounded range; the indexes were not needed for these anchors.

| SA lines | What they say, as used here |
|---|---|
| 254–255, 2719 | \(a_p=1-\tfrac12\operatorname{Re}\operatorname{tr}U_p\), \(A=\sum_pa_p\); the holomorphic form \(1-\tfrac12\operatorname{tr}U_p\). |
| 17257 | thresholds \(\varepsilon_k=g_kp_0(g_k)\), \(\delta_k=(A_1/A_0)\varepsilon_k\). |
| 17259–17278 | Theorem 2.1: action \(-A+\mathbf E_k+\mathbf R_k+\mathbf B_k-\mathcal E_{k,\mathcal S}\) (17263), class bounds on \(E^{(j)},R^{(j)},B^{(j)}\) and the mass. SA 17290 credits the core of the theorem to Bałaban, CMP 119 (1988) 243. |
| 17280 | "Neither \(E^{(j)}\) nor \(R^{(j)}\) carries a label index"; one family on \(\mathbb Z^4\). |
| 17459 | the main-step integration "takes" "the part of the regular terms on a domain of level \(m\)". |
| 19561–19570 | per-site families, pointed-Hessian cancellation and its hypotheses. |
| 19571–19600 | \(\epsilon_{jn}=L^{-(n-j)}\), \(\rho_{jn}\), (OSF3), (OSF4); the domain inclusion is "a separate hypothesis"; base-point count \(\epsilon^{-4}\). |
| 19603–19647 | Proposition (uniform ordinary input), (OSF5)–(OSF7). |
| 19651–19654 | (OSF8): \(1-\tfrac12\operatorname{tr}W=\tfrac12\det(1-W)\) on \(SL(2,\mathbb C)\). |
| 19666–19670 | "These summations do not prove (OSF3). That estimate contains the renormalisation assertion". |

## Result

**Proved here** (as implications from the named imports, and with distilled texts checked where used): CI-base (Theorem 3.1, no import); the order-\(k\) switched localization (Lemma 4.1) and the switched-shell gas-distance bound (Lemma 4.2, Corollary 4.3); the W kinds with their UM1 norms (Theorem 5.1 under \(q>3p_0\), Propositions 5.2–5.3, Theorem 5.4 under [HOL-K]); H-C for one family at any level and its exact multilevel requirement (Lemma 6.1, Theorem 6.2); islands, including td's complex island amplitude and ci-form's H-I consumer bound, from IN1 H-O (Theorem 7.1); X° at the current level and for standing successors (Lemmas 8.1–8.2); current-level per-read sums (Lemma 8.3); ordinary TD (td2 Theorem 3, checked); normal (Mayer) domination (18) for the main-step gas on the global fibre (Theorem 9.1); the first point of nl1-L's full-source distance Outstanding (Theorem 11.1); H-FL (6) from a stored-test record (Lemma 11.2); UM1-rest conditional on OSF-loc and AGE (Theorem 12.1); and the constant order (§13), with no cycle.

**Outstanding, in item 8's order.** (1) **OSF-loc** (§14), the first, with three failed attacks; it needs P82M (item 1) and H-OL (item 9). (2) **AGE** (§11.1). (3) Filing: Match-SF/O, Match-read/file (scale/rate transfer; retired islands), Match-heal/LD, Match-history (§10). (4) The stage and output formation rules of CI-maps (nl1-L L619–627), not treated here. Imports owned by items 3–6 and 10 ([DR], [DOM], [DOM-curv], [DOM-I], [HM], [HOL-K], [JAC], [GEOH], [H-O], [TEST-v0]) remain hypotheses.

This is a pass-1 research draft. It has not been distilled or refereed, and it grants no status.
