lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-10T02:06Z

# ch-r2: second round on CH4-AUX

Started 2026-11-09T14:06Z at commit cdc9a2fc8 on branch claude/ym4d-hard-route. Research-stage working state; no status.

(Sections follow as they are written.)

Provenance: Claude Opus 5.5 (max effort), Mac mini worker 2. Research text, not an audit, not an independent check, no status. Every deduction below is a written hand argument; searches and hashes discharge nothing.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline (SA), the complete account (CA-I, CA-II, CA-III) at `31a47c543775`, and the newer upstream files read in §1. Tadeusz Bałaban for the background, localization and large-field constructions (CMP 102, 109, 116, 119, 122a, 122b). Codex for `ch-bridge.md`, `ch-r1.md`, `prior/ch.md`, `mu.md`, `ui.md`, which this note builds on.

## 1. Repo search and sources

**Task.** FINISH row 415: second round on CH4-AUX (`ch-r1.md:355-368`, `ch-bridge.md:270-277`, `open-registry.md:23`). Not to repeat attacks A, B, C of `ch-r1.md`, nor PH 1-6 (`ph.md`) and Bridge 1-3 (`ch-bridge.md`).

**Read whole first:** `prior/ch.md`, `ch-r1.md`. Also read: `ch-bridge.md` §§1, 5-7 and Result; FINISH sections 1-84, 299-351 and rows 412-415; GOAL.md.

**Duplicate check (rule 0a).** CH4-AUX appears in `open-registry.md:23`, `t0-tree.md:347`, FINISH rows 331, 411, 412, 415. No other live lane attacks it. `open-core.md` and `l17c.md` do not name it.

**Repo prior work used here.**

| Note | Standing | Use here |
|---|---|---|
| `mu.md` §§5-6, Result | frozen; checked line by line by Claude (`gates/mu-gate.md`), first failing step none | Nesting identity of constrained minimizers, real and complex, with the curvature/current identities (6.3). Ported in §3. |
| `ui.md:549-572` | checked by Claude (`gates/ui-gate.md`), first failing step none | Proof of CA-I `4.5:lem-uniform-increment`: condition (iv) of CMP 109 is reproduced under a twist with a depth-free constant. Used in §5. |
| `ch-bridge.md` (6)-(9) | Codex, not refereed | Uniform contraction and ceiling arithmetic. Reused in §5 with a fixed system. |
| `uses-old.md:194`, `port/p4-operator.md:202`, `wd.md:49` | records | CA-I `4.5:lem-window-minimiser` (19267-19374) has a written proof at real data; `wd.md` records that the later 4.29 window proposition needs the whole window in the top stratum. |

**Primary sources read for this note** (hashes match `prior/ch.md:9-14`):

* CA-II 46131-46216 (target), 47976-48155 (links), 48156-48330 (readings), 48330-48620 (spaces and hypotheses (a)-(e)).
* CA-I 12936-13030 (class 𝔖 of the response chart), 14370-14540 (chart definition and Theorem `4.5:thm-chart-existence`), 15879-16020 (remark on condition (iv)), 19267-19300 (window-minimiser lemma), 19775-19840 (where condition (iv) is consumed), 20186-20250 (spaces), 43195-43530 and 44100-44260 (consumer radii, re-blocking step), 49480-49630 (seven entries), 73530-73640 (global carriers), 148120-148210 (CMP 122a conditions).
* **Bałaban's printed pages, read from the page images** (owner's copies in `~/ym4d-papers`, rendered with PyMuPDF; the OCR layer garbles formulas): CMP 122b pp. 370-376, CMP 122a pp. 189-191, CMP 119 pp. 261-262, CMP 109 pp. 262-263 (text layer, legible there). No earlier CH lane read CMP 122b itself: `ch-bridge.md` §7 and `prior/ch.md:164` used only the account's quotations.
* **Upstream at HEAD** `3ac0bf4f` (2026-11-09T13:10Z), listed through the GitHub API. New today: `YM4/BA/YM4_BA.tex` ("Block averaging and gauge geometry", sha256 `26f00014…`); it treats block averaging and gauges, not the localization links. `YM4/YM4_1400.tex` (sha256 `222ef1bd…`, = `2bc0658f9` copy) defines its own hereditary core with tower configurations `U_n(Z;P)=Φ_{M_{B'}(U)}((1/i)log{M_{B'}(𝐔)M_{B'}(U)^{-1}})` and bounds (YM4_1400:766-790); it does not treat the CMP 122b links (1.61)-(1.63). The Theorem 0 account moved to `YM4/Old/` with unchanged sizes.

## 2. What CMP 122b prints for the three links

These are readings of Bałaban's printed text. They correct no statement of the account; they add the original wording that the account cites.

**(2a) Every link output is a localized constrained minimizer.** CMP 122b p. 374, (1.63):
\[
 U_{k,\Lambda}=U(\mathbf B_k(Y_3),M^{\cdot}(U_{k,\Lambda}))
 =U\bigl(\mathbf B_k(Y_3),\ ((u_{k,\Lambda})_-)^{-1}e^{i\tilde Q(\eta\mathbf H_k)}R((u_{k,\Lambda})_+)M^{\cdot}(U_k)\restriction_{(Y_3^0)^c\cap Y_3},\ V''\restriction_{\Lambda^c\cap Y_3},\ V^{(\Lambda)}_\Lambda\bigr),
\]
with \(\mathbf H_k=\mathbf H_k(-\tfrac1i\log V'_k\restriction_\Lambda)\) by (1.64). The same form holds at link 3, (1.62) on p. 373, with \(\mathbf B_1(Y_2)=\mathbf B(Y_2)\cup\mathbf B_1\) and \(\mathbf H_{\mathbf B_1}\), and at link 2, (1.61) on p. 373, with \(\mathbf B''_k(Y_1)=\mathbf B(Y_1)\cup\mathbf B''_k\) and \(\mathbf H''_k\). Bałaban (p. 373): "Y_1 \ Y_1^0 is a boundary layer at the boundary ∂Y_1, of the width 2M_1 at most, for the corresponding scale."

Consequence used below. The link-4 output is
\[
 w_3(\sigma)=U\bigl(\mathbf B_k(Y_3),D_\sigma\bigr),               \tag{2.1}
\]
a minimizer for **one fixed** determining system. The switches \(\sigma=\sigma^{(4)}\) enter only through \(\mathbf H_k(\sigma)\) in the data \(D_\sigma\) on the boundary layer \((Y_3^0)^c\cap Y_3\). The constraint rows do not depend on \(\sigma\); only their prescribed values do. On \(Y_3^0\) the data are \(V''\) and \(V^{(\Lambda)}\), which after the substitution of \((\mathbf U,\mathbf J)\) become \(M^{\cdot}(\mathbf U)\) and \(V^{(\Lambda)}(M^k(\mathbf U))\) (p. 374, last paragraph).

**(2b) Bałaban claims no stage-space membership for intermediate outputs.** CMP 122b p. 375: "the regularity properties of the configuration (1.63) are almost the same, as the regularity properties of \(U(\mathbf B_k(Y_3),(M^{\cdot}(\mathbf U)\restriction_{\Lambda^c},V^{(\Lambda)}(M^k(\mathbf U))))\)". The same words are used for (1.62). The only precise statement is (1.65), for the composite: \((\mathbf U,\mathbf J)\in\tilde U^c_k(Y_4,\tilde\alpha_0,\tilde\alpha_1)\mapsto U^0_k(\mathbf U,\mathbf J)\in\tilde U''^c_k(Y_1,\tilde\alpha_0,\tilde\alpha_1)\), "proved already, in a slightly less general form, in the proof of the equality (1.89) [IV] ... we do not repeat them here".

**(2c) Where the auxiliary clauses come from, and who reads them.** CMP 109 p. 263, after condition (iv) ((1.15)-(1.16)): "The last condition (iv) is connected with the fact that in some important constructions in the next sections we have to substitute the functions (1.15) in place of the variables U, J." The same page shows (i)-(iii) at smaller constants imply (iv), through CMP 102b Proposition 9 (CA-I 15912-15925 quotes this). CMP 122a p. 191: the stage spaces descend in \(n\), and "if \(\mathbf U\) is an element of the space \(\tilde U^{(n+1)c}_k\), then \(\exp i\eta\mathbb H^{(n)}_k(\cdot)\mathbf U\) is an element of the space \(\tilde U^{(n)c}_k\) ... we will not repeat it". CMP 119 p. 262: newly created terms "are defined on slightly larger spaces, with the coefficients in their definition bigger by β multiplied by a corresponding number".

**(2d) A dictionary difference, recorded only.** CA-II 48057 says link 2 "uses the determining set \(\mathbf B_k(Y_1)\)". CMP 122b (1.61) prints \(\mathbf B''_k(Y_1)=\mathbf B(Y_1)\cup\mathbf B''_k\). CA-I 73572 also writes \(\mathbf B''_k(Y^{\rm tr}_1)\). Nothing below depends on this; `prior/ch.md:67` already flags the decoration.

## 3. Attack D (candidate 1): restriction through the nesting identity

**Idea.** By (2.1) the link-4 output is a minimizer for one fixed system. An auxiliary minimizer built from the averages of a minimizer, on a finer nested tower, is that minimizer again. So most auxiliary reads need no separate continuation: they are restrictions of the output itself. This uses an identity already proved in the repository, not a reconstruction (attack A) and not a comparison of different constraint rows (Bridge 2).

**Setting.** A determining system \(\mathfrak B\) is a family of blocks with levels, its iterated averaging rows \(M_{\mathfrak B}\) (CMP 98 (42)-(43)), and a level-zero shell of prescribed bonds. For admitted real data \(D\) (CMP 102b (7), with the seam tests), \(U(\mathfrak B,D)\) is the axial minimizer of the Wilson action under \(M_{\mathfrak B}(U)=D\). CMP 102b Theorem 1 gives one critical orbit in the regular space (6) there; `mu.md` §5 proves that every attained minimizer in that space lies on it, and `mu.md` §6 continues the axial minimizer holomorphically to a complex ball of data.

Let \(\mathcal T\) be a second system (an auxiliary tower on a domain \(Z\)), with action domain \(A_Z\).

**(N) Nesting.** Every configuration curve \(V(t)\) that changes only bonds the \(\mathcal T\)-problem may change, and keeps the \(\mathcal T\)-rows fixed, also keeps every \(\mathfrak B\)-row fixed. Its full action changes as \(A_Z\) does: \(\tfrac{d}{dt}A(\hat V(t))|_0=\tfrac{d}{dt}A_Z(V(t))|_0\), where \(\hat V\) extends \(V\) by the fixed outside field.

(N) holds when every \(\mathfrak B\)-row that meets the changing bonds is an iterated average of \(\mathcal T\)-rows and shell bonds, and every plaquette with a changing bond lies in \(A_Z\). This is the induction in the proof of CA-I `4.5:lem-window-minimiser` (19267-19374) and `mu.md` (5.4).

**Lemma R (port of `mu.md` §§5-6).** Assume (N). Let \(W=U(\mathfrak B,D)\) for admitted real \(D\). Assume \(W\restriction_Z\) lies in the regular uniqueness space of the \(\mathcal T\)-problem and its datum \(M_{\mathcal T}(W\restriction_Z)\) is admitted. Then
\[
 U_{\mathcal T}\bigl(M_{\mathcal T}(W\restriction_Z)\bigr)=(W\restriction_Z)^{g},     \tag{3.1}
\]
with \(g\) the residual axial gauge factor (\(g=\bar u_{\mathcal T}^{-1}u\) in `mu.md` (6.2); \(g=1\) when the axial trees are aligned, `mu.md` §5). If both sides of (3.1) are holomorphic in \(D\) on a connected ball that contains an open set of admitted real data, then (3.1) holds on the whole ball, and
\[
 \partial U_{\mathcal T}-1=\mathrm{Ad}_g(\partial W-1),\qquad
 J(U_{\mathcal T})=c_{\mathcal T}\,\mathrm{Ad}_g\,J(W),                        \tag{3.2}
\]
on the plaquettes and bonds of \(A_Z\), with \(c_{\mathcal T}\) the change of current units (`mu.md` (6.3)).

*Proof.* Real case. \(W\restriction_Z\) satisfies the \(\mathcal T\)-rows, since they are its own averages. Let \(V(t)\) be a differentiable \(\mathcal T\)-admissible curve through \(W\restriction_Z\). By (N), \(\hat V(t)\) is \(\mathfrak B\)-admissible and \(\tfrac{d}{dt}A_Z(V(t))|_0=\tfrac{d}{dt}A(\hat V(t))|_0=0\), because \(W\) is critical for the \(\mathfrak B\)-problem. So \(W\restriction_Z\) is critical for the \(\mathcal T\)-problem and lies in its regular space. CMP 102b Theorem 1 ("This orbit is a unique critical orbit in the space (6)") puts it on the minimal orbit. Axial normalization fixes the representative up to \(g\), as in `mu.md` §5, last paragraph. Complex case. Both sides are holomorphic on the connected ball and agree on an open real set. The identity theorem in each real coordinate direction, then continuation in the ball, gives (3.1) everywhere (`mu.md` §6). Curvature and current transform covariantly under \(g\), which gives (3.2). \(\square\)

The scope is the scope of `mu.md`: Bałaban's regular space and the axial convention of CMP 109 Lemma 4. The only new content is the abstraction to a pair \((\mathfrak B,\mathcal T)\) satisfying (N). `mu.md` proves (N) for the towers of the one-power hereditary class inside a CMP 109 window.

**Corollary D1 (nested reads of the link-4 output).** Take \(\mathfrak B=\mathbf B_k(Y_3)\) and \(D=D_\sigma\) of (2.1). Let \(e=(p,X)\in\mathscr T_3\) be an auxiliary label whose tower, changing bonds and action domain lie in \(Y_3^0\), with tower level at most the level of \(\mathbf B_k\) at each of its blocks. Then (N) holds for \((\mathbf B_k(Y_3),\mathcal T_e)\). Wherever \(w_3\) is holomorphic in \(\sigma\) with data in the ball of Lemma R,
\[
 Q_{e,2}(w_3(\sigma))=\mathrm{Ad}_{g}\bigl(\partial w_3(\sigma)-1\bigr),\qquad
 Q_{e,4}(w_3(\sigma))=c_e\,\mathrm{Ad}_{g}\,J(w_3(\sigma)).                   \tag{3.3}
\]
So the nested auxiliary reads continue exactly where the link-4 germ continues. They are single-valued and compatible with the germ automatically. No auxiliary system needs its own continuation, branch or reference.

*Proof.* On \(Y_3^0\) the system \(\mathbf B_k(Y_3)\) coincides with \(\mathbf B_k\) (CMP 122b p. 374: "\(Y_3^0\) ... the domain on which the determining sets \(\mathbf B_k(Y_3)\) and \(\mathbf B_k\) coincide"). A tower whose levels are at most those of \(\mathbf B_k\) on each block has rows of which the \(\mathbf B_k\)-rows are iterated averages (CMP 98 (42)-(43)). Its changing bonds lie in \(Y_3^0\), so the level-zero shell of \(\mathbf B_k(Y_3)\) is not touched. This is (N). Lemma R applies at real \(\sigma\) and real source data, and its complex part continues (3.1) along the connected domain of \(w_3\). \(\square\)

**Where attack D stops.**

(D-i) *Labels that meet the boundary layer are not nested.* On \((Y_3^0)^c\cap Y_3\) the system \(\mathbf B_k(Y_3)\) refines toward its level-zero shell. Its fine rows there are not iterated averages of the rows of a tower of level \(p\). So (N) fails for every label whose tower meets that layer, and (3.1) is not available. The \(\sigma\)-dependence of \(D_\sigma\) sits exactly on that layer (2a). This is the part of \(\mathscr T_3\) where a separate argument would be needed.

(D-ii) *Nested labels still need a reference with margin.* By (3.3), CH4-AUX at a nested label is a first-order bound on \(w_3(\sigma)\) itself, at the inherited threshold \(r_{e,2}\) or \(r_{e,4}\). A proof needs a reference with a positive margin below that threshold, as in `ch-bridge.md` (7). The natural reference is the twist-free minimizer \(U(\mathbf B_k(Y_3),D_{\rm ref})\). It is not an auxiliary configuration of the source datum: its data inside \(\Lambda\) are \(V^{(\Lambda)}(M^k(\mathbf U))\), not the source averages (2a). So no clause of the source space \(\tilde U^c_k(Y_4,\tilde\alpha_0,\tilde\alpha_1)\) bounds it at the inherited threshold, and CMP 122b p. 375 asserts only "almost the same". I found no other supply of such a reference.

**Outcome of D.** Lemma R and Corollary D1 hold as stated, conditional only on the inputs of `mu.md` and on (N). They settle the continuation and compatibility clause of CH4-AUX for nested labels. They do not settle its bounds, and they do not reach the boundary-layer labels. CH4-AUX is not closed by D.

## 4. Attack F (candidate 3): what does link 3 actually read?

Candidate 3 asked for a counterexample showing that the route needs a different auxiliary prescription. I did not find a counterexample. I found something that settles the route question directly: the consumer of CH4-AUX does not read its auxiliary entries.

**Word clash.** In CA-II 48338-48345 and 48371-48378, "auxiliary data" means the extra fields of the datum (\(g_kB\), \(V''\), \(V'_\Lambda\), \(V'_k\), the data of (1.53), (1.56)). CH4-AUX's "auxiliary minimizer/current readouts" are different objects: \(U_{p,X}(M^{\cdot}(w))\) and \(J_{p,X}(M^{\cdot}(w))\), condition (iv) of CMP 109 and entries 2 and 4 of CMP 122a p. 190. Below, "auxiliary reads" means only the latter.

**Proposition F.** The link-3 map \(\mathcal E_3\) reads its input \(w\) only through the four objects (r1)-(r4) below. None of them is an auxiliary read of \(w\). Hence the reads \(e\in\mathscr T_3\) of CH4-AUX are not inputs of link 3, and CH as stated in `open-core.md:176-193` (PH-L, `ph.md:186-214`) does not require them.

*Proof.* The map is defined at CA-II 48463-48472: "the extended right-hand side of (1.62) on \(Y_2\) ... the localised function \(\mathbf H^{(3)}(\sigma^{(3)};w)=H_B\) ... is inserted at \(w\) both as the background field and in the argument, and the remaining fields in (1.62) are replaced by functions of \(\mathbf U\)". Bałaban's (1.62) (CMP 122b p. 373) and the definition of \(\mathbf H_{\mathbf B_1}\) (p. 374) give the reads of \(w=U_{k,\Lambda}\):

* (r1) block averages \(M^{\cdot}(w)\) on \((Y_2^0)^c\cap Y_2\), inside \((u_{1,-})^{-1}e^{i\tilde Q(\eta\mathbf H_{\mathbf B_1})}R(u_{1,+})M^{\cdot}(U_{k,\Lambda})\);
* (r2) block averages \(M^{\cdot}(w)\) on \(Z''_k\), in the argument \(-\tfrac1i\log M^{\cdot}(U_{k,\Lambda})\restriction_{Z''_k}\) of \(\mathbf H_{\mathbf B_1}\);
* (r3) \(w\), with the current slot carried with it, as the background of the response \(\mathbf H_{\mathbf B_1}\);
* (r4) the gauge factors \(u_{1,\pm}\), which are analytic functions of the response restricted to blocks (p. 373 for \(u^0_k\), "the same remarks apply" to (1.62) on p. 374).

The other entries of (1.62), \(V''\restriction_{\Lambda^c\cap Y_2}\), \(M^{\cdot}(U_0^{(AL)})\restriction_{\Lambda\cap\Omega''_k}\) and \(1\restriction_{Z''_k\cap\Omega''^{\sim}_{h+1}}\), are source data "replaced by functions of \(\mathbf U\)" (p. 375). They do not read \(w\). The outer map \(D\mapsto U(\mathbf B_1(Y_2),D)\) reads only its datum (CMP 102b Theorem 1).

(r1), (r2) and (r4) are averages and functions of the response. For (r3), the response \(\mathbf H_{\mathbf B_1}\) is the account's response chart for the system \(\mathbf B_1\): CA-I Definition `4.5:def-response-chart` identifies its field with "the field of \cite[(1.2)]{B-CMP116}" (14436-14437), and (K10) (15265-15300) is its switched form. Theorem `4.5:thm-chart-existence` asserts (K1)-(K10) "For every \((U,J)\in\mathfrak S\) ... and every \(B\) ... with \(|B|<c_9\)" (14523-14525), with constants "depending only on \(d\) and \(L\)" (14510), uniform in \(k\), \(K\), the tower, \(X\) and \(M_1\) (14518-14521). The class \(\mathfrak S\) is (S1)-(S3) (12936-13013), and CA-I 13016-13017 states: "Condition (iv) of \cite{B-CMP109} is not part of the definition of \(\mathfrak S\) and is not derived from (S1)--(S3); where it is used, it is supplied separately." So none of (r1)-(r4) reads an auxiliary minimizer of \(w\) or its current. \(\square\)

**Who does read the auxiliary entries.** The terms. CA-I 19791-19793: after the chart produces its pair, "the orbit of the produced pair lies in \(U^c_j(X,\alpha_0,\alpha_1)\). On this space \(\mathbf E^{(j)}\) is defined and analytic". CMP 109 p. 263 gives the reason for condition (iv): the functions (1.15) are substituted into the variables of later terms. In CH the only term is \(t\), read at the final composite through \(\mathcal A'_t\) (CA-II 48515-48520). The composite reads \(w_3\) only through \(\mathcal E_3\), that is through (r1)-(r4). So the auxiliary reads of \(w_3\) enter no requirement of CH. The term's clauses are conditions on the auxiliary minimizers of the final configuration \(\mathsf R(\sigma;\mathfrak d)\) itself.

**Consequences.**

1. CA-II hypothesis (a) asks only \(\mathcal E_4(\mathbb D_4\times\mathcal O_4)\subset\mathcal O_3\) for a relatively open \(\mathcal O_3\) on which \(\mathcal E_3\) is analytic (48447-48462). PH-L asks \(\Omega_3\) to be a set "on which the actual link formulas define single-valued jointly holomorphic maps"; its sentence "All stage entries, auxiliary fields and cube-gauge requirements are those of the actual inherited domains" concerns \(\mathcal A'_t\). Neither puts stage clauses at link 3's input. The phrase "tested in the stage domains needed at the input of link 3" (`ch-bridge.md` §7) has no source line behind it.
2. The sentence "This lemma is a necessary part of CH" (`ch-bridge.md` Result) is not correct as stated. CH4-AUX is one possible intermediate lemma for one proof strategy (carry the full stage space through every link). It is not an input of CH. `prior/ch.md:122` already hedged this.
3. The open question for link 4 is the weaker statement below. Its radii are constants of \((d,L)\) and of CMP 102b Theorem 1. The stage coefficient \(1-\beta\sum2^{-|m-i|}-\cdots\), the powers \(\mathsf L_0^{2\max(0,m-k_0)}\) of the thresholds, and the \(2^{-n}\) margins of `ch-bridge.md` §5 do not enter it. All tight thresholds move to the final membership (d), where the term reads them, and which CH required anyway.

**CH4-REG (replacement for CH4-AUX; my formulation).** Keep CH's admitted source-free inputs and exclude its sought complex readings and memberships. There is one positive coupling ceiling \(\gamma_4\), chosen last and depending only on the earlier constants and \(b\), with this property. For every admitted history, datum \(\mathfrak d\in\mathcal D_b\) and triple \((Y'_2,Y'_3,Y'_4)\), the link-4 output (2.1) has a single-valued holomorphic continuation \(w_3(\sigma)\) on \(P_4\) that agrees with the prescribed germ. For every \(\sigma\in P_4\):

* (R1) the pair \((w_3(\sigma),J_3(\sigma))\) carried to link 3 lies in the orbit class \(\mathfrak S^{\rm orb}\) (CA-I 12981-12986) of the response chart of the system \(\mathbf B_1(Y_2)\);
* (R2) \(\bigl|-\tfrac1i\log M^{\cdot}(w_3(\sigma))\restriction_{Z''_k}\bigr|<c_9/\mathfrak K\), with \(\mathfrak K=4\) of CA-I 12981;
* (R3) the averages \(M^{\cdot}(w_3(\sigma))\) on \((Y_2^0)^c\cap Y_2\) pass the plaquette and seam tests of CMP 102b (7) at half the radius admitted by CMP 102b Theorem 1.

The ceiling does not depend on history, label, depth, age or volume.
