Provenance: Codex (gpt-6-astra); effort setting not exposed; checkout `8754e2c957b3fc3554fdf6b7de2041ba7f1df40e`; 2026-11-06. Research check, not an audit; grants no status.

# CA and its replacement step F

## 1. Scope and sources

This is one check of `library/ca-claude.md` and `library/ca-f.md`, for FINISH rows 382 and 386. The earlier gate and `library/prior/ca-gate.md` are absent. The registry assigns CA to `ca-claude`; this is its requested check, not a competing proof lane. Inputs owned elsewhere are identified, not attacked.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`. Credit Tadeusz Balaban for the cited constructions and operator theorems. Credit Claude's Mini worker for the two texts checked here.

The [outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), [CA-I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex), [CA-II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex) and [CA-III](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_III.tex) were fetched once. References below use their raw line numbers. Searches and excerpt extraction locate evidence only; no computation discharges a mathematical step. The specified Balaban paper folder is absent, so CMP 119 (2.10)–(2.14) is checked through the account's quotations, as requested.

`ADVANCE` below means the displayed implication is correct with its named hypotheses. It does not prove those hypotheses or establish CA without them. `REVISE` supplies the required correction. `BLOCK` identifies an implication or source identification that remains unsupported.

## 2. Seed and final algebra

| Statement or step in ca-claude.md | Verdict | Check |
|---|---|---|
| Lemma A, steps 1–2 | ADVANCE | Component separation and the cut buffer put the full stratum bond outside the graded layer. I:91991–92024, 92095–92097; the splice quoted from CMP 119 (2.13)–(2.14) at I:92515–92532. |
| Lemma A, step 3 | ADVANCE | I:138407–138411 supplies the seed's datum restriction. CMP 119 (2.10)–(2.11), quoted at I:142680–142690, makes its level-zero row the identity. |
| Lemma A, steps 4–5 | ADVANCE | The small-field input I:142611–142625 and trivial rotation I:142310–142317 give the pinned bound and \(A'=0\), on the real scaffold of the prescribed sources. |
| Lemma B(i) | ADVANCE from (B-in), (S-B) | The level-one, weight-one classification agrees with I:142736–142760. \((0.098/64)(0.164)<0.00026\). No application at a raw cell occurs. |
| Lemma B(ii) | ADVANCE | Six plaquettes, projection norm at most two, and unitary transports give \(12(0.04)\alpha_{0,0}=0.48\alpha_{0,0}\). |
| Lemma B(iii) | ADVANCE from whole-cube (S-B) | The two ceilings I:142646–142659 give the axial-gauge proviso and the bounds \(3M\alpha_{0,0}\), \(6M\alpha_{0,0}\). The axial-gauge estimate remains an input. |
| Proposition C, both local-algebra applications | ADVANCE | I:141265–141508 supplies the exact increments. \(1.06/85<1/80\) and \(0.04/24+4/85<1/10\). |
| Proposition C, totals and compatibility | ADVANCE | The largest normalised entry is \(0.48+3=3.48<3.65<f_0(d^t)\). Principal logarithms agree on overlaps. The unchanged unitary factor preserves whole-cube gauges. |
| Lattice estimate, line 137 | ADVANCE | The full neighbouring stencil suffices. \(e^{1/40}\le40/39\) implies \(1+e^{1/40}<2.03\). |
| L1, section 6.1 | ADVANCE as a diagnosis | Its \(\sqrt{k}\) majorant is not uniform from a lower bound on \(\check R_k\) alone. This does not refute (CL). |
| Lemma E | ADVANCE under its metric and every-label geometry | Disjoint level-\(j\) crossings each cost \(L-2\), inside \(\Omega_h^c\subset Z_h\). The final portion after the last visit to \(Z_h\) contributes \(\check R_k-1\) separately. I:63571–63586 supplies thickness; I:114355–114357 includes thin zones. |
| Lemma D, unused | ADVANCE under arrest timing | Leaving the earlier completed component forces a visit to its then small-field region. I:133477–133482 and 134967–134968 preserve the resulting lower bound on the level. |

(S-B) must cover **whole cubes**, not just one-bond current stencils. These conclusions concern CA's five entries, not other hereditary clauses.

**REVISE “48 times weaker.”** Only the current-controlled branch grows by 48, from \(\alpha_{*,0}/(16K_{\rm cur})\) to \(3\alpha_{*,0}/K_{\rm cur}\). The other branch changes from \(1/160\) to \(1/85\). No proof estimate uses that description.

## 3. Step F, including partial segments

### 3.1 Original Proposition F

**BLOCK at lines 182–186 as a derivation from the cited response theorem.** The supremum-only route is correct under (c1)–(c7), (R) and Lemma E. The second route sharply restricts a field datum to cubes. Its cited norm reads derivatives, I:72532–72537 and 142537; the original pointwise estimate does not control those restrictions in that norm. The passage to associated fields is unsupported.

The full-solution current identity also does not define associated fields for \(tH\). These are D1 and D2 of ca-f.md, correctly identified. Exponential absorption repairs neither. The replacement addresses both through explicit premises.

### 3.2 Lemma S

**ADVANCE, steps 1–3 and both endpoints.** I:111538–111545 defines the cut-layer partner. With constant cut \(\chi=t\), I:111590–111612 makes its commutator zero. The incomplete count I:111614–111626 is not used.

The three linear entries contribute \(3tE_y\); the \(\mathsf K\) term contributes \(18dtE_y\), using \(\mathsf p(W)\le1\). I:111580–111586 bounds the remainder by \(2.1K_JtE_y\), hence by \(2.2K_JtE_y\). This gives the stated \(K_{\rm cur}\). The associated fields are \(tA'\), \(tX\); no nonlinear solution at datum \(t\mathsf d\) is asserted.

This is the constant-cut current of I:142563–142577, with the layer construction interpreted by (N6). The linear interpolation I:141764–141767 is a different family. Its bound also holds, but it cannot replace the actual current. Lemma S's main proof does not make that substitution.

### 3.3 Proposition R

**ADVANCE from the displayed (N1)–(N5), (N8), (G-sep), and Lemma E.** Add Lemma E and the local read-set convention (N9) to its hypothesis list; the proof already uses them.

| Step | Verdict | Check |
|---|---|---|
| 1: weight \(p_T\) | ADVANCE from (N5) | The triangle inequality and \(d^\wedge\ge w d_{\rm sc}\) give its weight ratio when \(\delta_R\le w\delta\). This uses the sufficient membership rule of (N5). |
| 2: current contribution | ADVANCE from (N2), (N4), (N8) | The restricted object is a current with a supremum norm. \(p_T=1\) on its support. The field datum is not cut. |
| 2: decoupling bracket | ADVANCE from (N3) | \(T\supset\Lambda^c\), \(\delta_R\le\delta_{\rm br}\) imply \(p_T\ge p_{\rm br}\). The weighted norm decreases with its denominator. |
| 2: block data | ADVANCE | Their supports lie in \(S\subset T\), so weighted norms equal scaled suprema. |
| 3: response tuple | ADVANCE from (N1) | Compare the actual admissible datum with zero at the same kernel and weight. All four entries are in (N1). |
| 4: distance | ADVANCE | (G-sep) loses one unit, the move to \(y'\) loses two. This gives \(e^{3\delta_R}\); Lemma E supplies the remaining distance. |

Keep the actual-frame identification in step 1. I:92515–92532 gives finer blocks at the cut and unchanged deep blocks. Refinement increases the path-length density of I:63975–63981. Operators and weights must use that same geometry.

**REVISE the source claim for (N8).** I:92454–92456 bounds the arguments of the layers. It does not state, in the required scaled norms,
\[
 K_uB_H\max\{\|\widehat J^{b_2}\|_\infty,\|J_2\|_\infty\}
 \le\varepsilon_{\mathfrak Q}(k). \tag{N8-current}
\]
I:92612–92618 collects current amplitudes into its final constant but supplies no conversion from current size to the argument budget.

This is a real distinction: \(G''Q''^*=0\) at \(\sigma=1\). Adding \(Q''^*\lambda\) to \(J\) leaves \(G''J\) unchanged. For example, \(Q=(1,0)\), \(G=\operatorname{diag}(0,1)\), \(J=(a,0)\) give \(GQ^*=GJ=0\), but \(\|J\|=|a|\). This refutes that inference between norms, not the actual Yang–Mills estimate.

The repair is to retain (N8-current) as an **independent uniform input**, as the display of (N8) permits, and delete its claimed deduction from (d'). A fixed extra constant can instead be included in \(C_D\). Without this input, R's step 2 remains blocked as an application to the account.

**REVISE the source claim for (N2)–(N3).** I:72532–72535 invokes the field-datum lemma for \(\tilde G_0J\); I:142537 invokes it in the alternative construction. Neither proves the displayed all-weight derivative estimate for \(G''J^c\). Retain both the operator identification and (N2)'s estimate. I:92560–92582 uses its walk theorem only for pointwise bracket and field bounds. The full datum-norm estimate (N3) is additional.

The Laplacian exception recorded at ca-f.md:69 matters: a difference theorem for an operator type excluding that entry cannot supply it. This check does not independently verify the absent CMP 99b pages, or promote their quotation into a proof of (N2) or (N3).

### 3.4 Proposition F'

**ADVANCE from R, S and all its displayed premises**, over the whole square \([0,1]^2\).

1. **Sizes.** \(F_s=2.03\sup E_{y'}(H_s)\) covers the read-sets in (N9). Start with the unitary first base. The first local-algebra step gives \(\eta|A'_3|\le1.06F_3<1/80\) throughout these sets. Then the lattice estimate controls the second factor at every \(t_3\). This order avoids assuming its own intermediate bound.
2. **Currents.** Apply S at each fixed kernel, with (N7), for every \(t_s\). This is independent of the base used to estimate the other left factor.
3. **Budget.** \(e^{4\delta_R}\) is correct: R contributes three units and its distance's \(-1\) contributes one. I:77947–77954 declares \(k=h+\check R_k\). Use \(\sqrt{k}\le\sqrt h+\sqrt{\check R_k}\) and the finite supremum \(S_R\).
4. **Ceiling.** Constants precede \(\gamma\), and \(R_\gamma\to\infty\). The extra fixed polynomial for \(p_1>q\) is also absorbed. This gives (CL) uniformly; Proposition C applies.

**REVISE one unnecessary numerical step.** Both F proofs write \(1/(24M)\le1/170\) without naming its needed floor on \(M\). Use only \(M\ge1\):
\[
 \frac{3}{K_{\rm cur}}\alpha_{*,0}
 \le\frac1{25}\frac1{24M}\le\frac1{600}<\frac1{85}.
\]
The required branch follows without another hypothesis.


## 4. Does the account or library prove (B-in)?

**REVISE “printed nowhere” / “stated nowhere as a proved result.”** Literally, no: clause (b) of the unqualified lemma 4.27:prf-room-dissolving, I:138348–138387, states the base conclusion. The structural index marks that lemma PROVED. I:136724–136733 also uses the conclusion.

**BLOCK as an independently supplied estimate.** The proof of clause (b), I:138438–138450, invokes the own-level bound of the sealing construction with exactly the required \(1/64\), all-entry and cube content. It does not derive it. I:138472–138483 says which arrest inputs that absent bound uses; this is a dependency assertion, not its proof. Thus the room/spend lemma cannot discharge its own base input.

The corrected statement is:

> The account asserts (B-in) as the base conclusion of its room/spend lemma, and uses it in ambient inclusion. Its proof invokes a separate own-level estimate for the actual completion seed. No independent supplier of that estimate was found in CA-I, CA-II, CA-III or this checkout's library.

This finding used the full statement index and searches for the bound, the sealing construction, its floors, its shares and \(U_2\), followed by the relevant source passages. CA-II 1128–1147 and 1212 invoke the sealing theorem without supplying it. CA-II 44300–44307 invokes a sealing statement for different remainder relations; it supplies no core base bound. No corresponding supplier was found in CA-III.

The nearest candidates do not change this:

- I:137035–137088 and ARR §9.3 give positive-level real admission **using** the completion-base and assignment/refinement inputs. They do not prove (B-in) for the spliced \(U_2(V'')\). Choosing a smaller fraction in that conditional result does not remove its inputs.
- The real-point collar lemma concerns \(U(\mathfrak B_d,V)\), with its real-datum and regularity hypotheses. It does not identify that minimiser with the spliced seed on side plaquettes. A proves the required identity only on the surviving raw rows.
- The frozen mu and oc results require admitted real data, matching determining rows and the required enlarged cubes. PDA supplies geometry. The operator port requires an admitted pair. None supplies those analytic hypotheses for this seed. ARR §§5, 14–15 states these boundaries explicitly; mu §§1, 5 and oc §2 retain them.
- I:94185–94240 expressly imposes its real-core membership beyond the cited CMP 122b support statement. It cannot be used as a proof of that membership.
- The outline's BGR32–BGR33, lines 12309–12381, requires the reference to be admitted before bounding its displacement. Its general core criterion cannot generate (B-in). The outline also retains actual nonlinear core inclusion at 4036–4037.
- The other library label “(B-in)” in nl1-L-draft.md:473 concerns boundary-term norms. It is a different input.

This is a finding of **no noncircular supplier**, not a counterexample to (B-in). The account explicitly excludes raw-cell thresholds in I:136339–136341; B's use at positive levels respects that restriction. Without (B-in), both its side-plaquette application and its whole-cube application need suppliers. “Only B(i) is missing” is too narrow unless all of B(iii)'s cube plaquettes have separately been covered.

## 5. Inputs not proved by the account in the form CA uses

The immediate input list is longer than “(L), Theorem 3.14, source placement.” The following retains the actual domains, norms and parameter quantifiers. Published citations are distinguished from unsupported applications; neither is discharged by this check.

| Input | What is still imported or unproved |
|---|---|
| **(B-in) and (S-B)** | The independent \(1/64\) estimate for the actual \(U_2\), including derived entries and whole-cube gauges. Also the placement of every required positive-level stencil and whole index-zero cube inside \(D_2\setminus B_S\). Collar-point containment alone is weaker. See §4. |
| **(N1), the full layer theorem (L)** | Uniform weighted Lipschitz bounds for all four response entries, zero datum, admissibility on the actual completion kernels, full complex parameter range, and uniform constants. I:141777–141785 and 112588–112610 state these as inputs/conventions. The cited subfamily lemma assumes the layer and field-datum theorems at I:72392–72400. |
| **(N2), the field-datum estimate** | The all-weight derivative-norm bound for the actual \(G''(\sigma)J\), including the identification with the operator called \(\tilde G_0\). I:72532–72535 and 142537 invoke it. They do not prove this full application. The norm structure and sufficient weight-class rule in (N1), (N5) must remain explicit with it. |
| **(N3), the decoupling bracket** | The full datum-norm bound, uniform in the stated complex decouplings, with exterior-distance decay. The account cites CMP 99b Theorems 3.13–3.14 in I:92457–92463 and uses pointwise decay. Passing to every datum-norm entry is additional. The Laplacian qualification cannot be ignored. Registry B99b-T314 remains an imported theorem. |
| **(G-sep) and actual construction matching** | The placement of every source in \(J^c\), the boundary correction \(r\), and \(\Lambda^c\) beyond the cut up to one unit; the actual layer arguments and kernels; the full-domain seed and cut-current identifications. I:92401–92447, 92496–92497, 92569–92587 and 142292–142317 state or use them through the completion construction. The pointwise localisation conclusion alone does not prove this stronger source-set assertion. No equality with the alternative construction at I:142529–142546 has been supplied or used. |
| **(N7)** | \(\mathsf p(W_s)\le1\) at each actual layer kernel, throughout the prescribed source/parameter domain. I:115406–115407 takes this as an input. The pinned seed bound is not by itself an admission theorem for every such kernel. |
| **(N8)** | The argument budget is already a hypothesis (d') of current localisation. Its stronger scaled **current** budget is separate, as §3.3 explains. It must be uniform before \(\gamma\) is chosen. |
| **Other published/application inputs** | Existence and the stated real-data class of the completion minimiser; raw-data identification and characteristic-function smallness; the small-field statement and axial cube-gauge estimate; the averaging-operator bounds controlling \(Q^*\) and \((QQ^*)^{-1}Q\); and the quantitative \(\mathsf K\) bound on the actual kernel. These are quoted or assumed at I:92417–92447, 92511–92513, 94992–95020 and 142611–142659. The CMP 119 row/splice formulas fix the construction; they are not additional analytic estimates. Generic regularity does not supply their actual-data hypotheses. |
| **Every-label geometry and metric readings** | In particular (c7)(d) after earlier R operations, the source/collar buffers and component separation, and the compatible path metrics/weight class on the actual determining sets. I:63571–63586 states the every-label geometry with a Balaban citation; I:91723–91728 supplies the metric comparison; II:6179–6189 and 57620–57626 use the weight rule. PDA may be reused on precisely its admitted nests; geometry alone supplies no analytic base bound. |

The stage-claude lane owns (L); this check does not reopen it. Its §4 already gives a conditional layer/current estimate for **block datum \((0,b)\)** under (M-chart). Therefore “no layer result has been rebuilt” is inaccurate. That result does not supply the full two-component datum theorem, arbitrary-weight estimate and separate associated-field entries of (N1) needed here. Likewise, existing real gauge results are useful under their hypotheses; they do not admit this completion seed automatically.

What the account **does** supply is retained. The cancellation identity in (N4) is proved at I:92500–92558 from criticality and the quoted averaging facts. The real-current formula is worked out at I:10335–10347. The account gives remainder lemmas at I:10350 and 14083 on their named classes; their application to the actual kernels remains within (N1), (N6), (N7), not a new missing algebra argument. The constant-cut commutator calculation, local algebra and level-zero ratio implications are proved. The allowance sum gives \(f_0>3.65\). Stage counts, radii and ceilings are declared choices with the stated flow hypotheses; the final small-\(\gamma\) absorption is valid. None needs a new proof in this lane.

## 6. Disposition

**ADVANCE: the combined proof is a valid implication from its complete displayed inputs**, with the explicit repairs above. Lemmas A, B, D, E, Proposition C, Lemma S, Proposition R and Proposition F' pass at that conditional level. The earlier version of F remains blocked at its weighted-datum/current passage; ca-f replaces that passage successfully.

**REVISE the dependency claims.** (B-in) is asserted but lacks an independent proof. (N2), the actual norm/operator identifications, the current-budget part of (N8), and kernel admission must not disappear behind the three-item open list. (N3) is a stronger input than the pointwise theorem application shown in the account.

Thus the two former step-F inference gaps are repaired **conditional on these inputs**. CA itself remains open. No source domain, birth domain or parameter range has been shrunk, and no scientific status is granted.

Checked line by line by Codex (gpt-6-astra).
