# Gate of a3-close and meet-6c — queue row 106
Provenance: OpenAI Codex (GPT-6; exact backend and runtime effort not exposed; requested gate effort xhigh), checkout 8d897ee40d916315811ae26035b6e42a10055dca; Sussman–Alpoge outline 31a47c543775; research text, not an audit, no status granted.

Scope: `a3-close.md` §§1, 3, 4 and every section of `meet-6c.md`. The pointed-core argument in `a3-close.md` §2 is excluded. Source credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's constructions and conventions; Tadeusz Balaban for the regular-class and local-gauge results. The outline was fetched once to `/tmp/sa_ym4.tex`; the Balaban OCR is read in place. All mathematical checks below are by hand. No numerical or machine proof is used.

This gate decides whether the reference-class, joined-localisation and meet-localisation premises of real-critical nonlinear A3 can be consumed. Verdicts distinguish the submitted assertion from any explicitly proved repair. Existing flat/A1/P82° results are named premises, not re-certified here.

## A. `a3-close.md` §1 — ADVANCE as an implication

First failing step: none, with A1 (8.2) and its reference-1 local-gauge port retained as premises. The gap condition works for an arbitrary separated sequence; it does not assume that the original first member is a cube or a torus.

1. **The current condition is genuinely checked.** The OCR drops the left side of CMP 99a (1.9). Reading just p. 77 of the local scan confirms
   \[
   |D_U^{\eta *}\partial U(b)|<\alpha_0L^{-2j}(L^j\eta)^{-1}.
   \]
   After multiplication by \(\eta^{-2}\), the right side is \(\alpha_0\xi_j^{-3}\). At a bond with its six incident plaquettes present, the anti-Hermitian part is the Wilson current (with the fixed action normalization absorbed). For each incident holonomy \(P\), \(\operatorname{Re}(P)-1=-\tfrac12(P-1)^*(P-1)\). The constant terms cancel in the covariant difference. A1's curvature estimate therefore bounds the remaining Hermitian part by \(CB^2\varepsilon_1^2\eta\mathsf L(b)^{-4}\le CB^2\varepsilon_1^2\mathsf L(b)^{-3}\). Every incident plaquette contains the bond's endpoints, so its largest-corner scale is at least the bond's scale. The current estimate in (8.2) supplies the other part. If a corner belongs to \(\Omega_j\), the largest-corner scale is at least \(\xi_j\). Thus both of Balaban's inequalities hold wherever the local construction reads them, with \(\alpha_0=C_L(B\varepsilon_1+B^2\varepsilon_1^2)\). Strict inequalities are obtained by a harmless enlargement of this constant.
2. **The new gap pays for the entire enlargement.** Rounding a cube of side \(c_{\rm reg}M\xi_j\) to the \(W\xi_j\) grid gives side at most \(M'\xi_j\). The additional nested-cube cover is contained in its \(2W\xi_j\) enlargement, hence in \(Z+4W\xi_j\). For \(j\ge1\),
   \[
   \operatorname{dist}(Z,\Omega_{j-1}^c)>\rho\xi_j/L\ge(4W+2)\xi_j.
   \]
   The strict first inequality comes from separatedness, so the hypothesis **\(\rho\ge4LW+2L\)** suffices; the proof's later strict sign on \(\rho\) is unnecessary. All incident plaquettes used by (1.9) remain inside \(\Omega_0\), even at a hole. Extending by 1 is permissible only outside this protected read set; it does not establish Balaban's class across the original boundary.
3. **The local-gauge invocation has the right scale.** Drop the deeper members, rescale \(\xi_j=1\), and use the bounds on the enlarged cube inside \(\Omega_{j-1}\). The curvature and current losses are \(L^2\) and \(L^3\), fixed in \(L\). The reference-1 construction in A1 §3.8 then gives each of \(\xi_j|A|\), \(\xi_j^2|\nabla A|\) bounded by \(C_LM'\varepsilon_1\), after the stated smallness choice. Their sum costs only another fixed factor. No accumulating depth factor enters.
4. **The bottom layer does not need a current estimate.** In complete axial gauge, each link is a product of conjugated plaquettes across at most three strips of length \(n=c_{\rm reg}M\); unitarity gives \(|U_b-1|\le3nB\varepsilon_1\). The principal-log inequality \(|\theta|\le(\pi/2)|e^{i\theta}-1|\), followed by the one-mesh difference estimate, gives the displayed value and derivative bounds. This also handles cubes touching an arbitrary first-member boundary.

Choose all fixed lengths, then \(B\), then \(\varepsilon_1\) with \(C_LM'\varepsilon_1\le\min(a_L,\alpha_*)\). The torus floor must contain the whole enlargement, as already assumed. This proves the advertised Reg implication; it does not prove A1 or F0 afresh.

## B. `a3-close.md` §3 — WRONG for source identification; ADVANCE for the explicitly defined meet

**D1 — a compatible construction is identified with an unspecified source construction.** First failing step: “the tower must be cut at depth \(j_a\) … (SA 9646, 9769).” Those two passages cut *tower configurations*. SA 9786 says which rows may be new and gives qualitative agreement in the collar and interior; it neither specifies maximal erosion nor gives \(\Omega'_q=\Omega_q\cap\bigcap_bT^b_{\min(q,j_b)}\). The new-row clause rules out genuinely new higher-level rows. It does not select the erosion or determine every member. More decisively, SA 5598–5610 explicitly makes the actual erosion assignment auxiliary data and says that the choice cannot be recovered from gap inequalities; it allows either a supplied assignment or quantification over admissible assignments. For example, sufficiently small extra aligned erosion near a face of a large part leaves the same qualitative collar/interior and row-level properties, while changing the sequence. The literal full-tower reading is indeed incompatible with the row clause when a thick layer-\(j\) collar contains level-\(j+1\) tower tops. Rejecting that reading does not prove uniqueness of the proposed replacement.

**Repair (proved construction, unproved source identification):** explicitly *define* the cut-meet by the formula in the note. Call it an auxiliary/replacement joined sequence, and retain identification with the outline as an additional premise wherever that identification is needed. The four-comparison argument can use such an auxiliary sequence without asserting equality to SA's joined sequence. The following verifies the mathematical construction.

- **J(a): none fails.** If \(d(x,A_b^c)>e_{q+1}\), every point of its aligned next-level cube is farther than \(e_q+\rho\xi_q\) from \(A_b^c\). By the induction hypothesis the complement of \(T_q^b\) lies within depth \(e_q\); the 1-Lipschitz distance function gives the next gap. Summing the geometric series gives \(e_q\le(\rho+L\mathfrak M)\xi_q/(L-1)\le\rho\xi_q\). For the second rule the two costs at step \(q\) are each \(\mu\xi_{q+1}\), giving \(e'_q\le3\mu\xi_q\).
- **J(b): none fails.** Above \(j_b\), \(\Omega_q\cap A_b\) cannot enter the single-layer collar. It is at least \((n_c\mu-\rho)\xi_{j_b}\) from \(A_b^c\cup S_b\). For \(q\ge j_b+2\), a path to that set crosses \(\Omega_{q-1}^c\), giving the stronger strict gap \(>\rho\xi_{q-1}\). Thus the frozen factor does not destroy higher-level separation. A coarse cube of \(\Omega_q\) crossing \(\partial A_b\) would meet the forbidden collar, so intersections remain whole aligned cubes, including above the cut. The complement-of-intersection identity then proves every gap, not merely the first one.
- **J(c): none fails on its intended domain \(W\).** Outside the strips, every tower factor contains the point; inside one collar, all other factors contain it by boundary separation, and the original layer is exactly \(j_b\). The statement must read “off the strips **within \(W\)**”; it is plainly not an equality of sequences outside \(W\).
- **J(d): none fails for rows whose endpoints are in \(W\).** A row touching \(S_b\) cannot have level \(q>j_b\): its length is \(\xi_q\), whereas the preceding gap exceeds that length. For \(q\le j_b\), its whole bond lies in the collar. There original rows have level \(j_b\); they survive precisely when an endpoint remains in \(T^b_{j_b}\). New rows have \(q<j_b\) and neither endpoint in \(T^b_{q+1}\), hence both endpoints in \(S_b\). A surviving row's change from interior to outward changes the straightened representation, not the prescribed geometric constraint. Its reduced seam datum must still be computed from that constraint.
- **J(e): none fails as a containment.** Adding the double-block carriers costs at most a fixed multiple of \(\xi_{j_b}\), giving the stated \(S_b^+\) (the extra \(3\xi_{j_b}\) is sufficient). Old/new row differences are confined there. This does not include all original rows outside \(W\), which have been restricted away and are not datum mismatches of the comparison.

**D2 — the asserted two-sided weight equivalence does not follow.** First failing step in Consequence 2: deducing that the boundary and mismatch weights “differ by at most” the stated factor from \(\mathcal C\subset\bigcup S_b^+\). Containment proves only
\[
d_{\mathbf B}(y,\mathcal C)\ge d_{\mathbf B}(y,W^c)-C_{L,\rho,\mu}.
\]
It supplies no reverse bound. The statement also permits a level-zero part: its cut-meet has no added or dropped rows inside \(W\), so \(\mathcal C=\varnothing\), while \(d(y,W^c)\) can be finite. This is a hand counterexample to the unqualified two-sided assertion. Repair: use only the displayed one-sided inequality, proved by connecting each carrier to its part's complement through its single-layer collar and using the triangle inequality. This is exactly the direction needed for decay. Section E below supplies the explicit constant for one part.

For 2.8, the cut at top level \(k\) is vacuous. At the W3 inner cut, equality of a *maximally eroded* full meet and the cut meet follows if \(d(\Omega_q\cap A,A^c)>e_q\) for \(q>k_\flat\); the nested-box gap \(d(C,\Omega_q)\ge M\xi_q\), with \(M>\rho\), is sufficient. It is a geometric premise, not a consequence of merely saying “tower”. The actual-localisation identification and (SEP-L) require the qualification in Section H below. Thus row 103's unrestricted source-identification conclusion does not pass, although its explicit auxiliary construction does.

## C. `a3-close.md` §4 — WRONG in its exclusive-pairing conclusion; repaired result ADVANCE

Lemma M(i)–(iii): **ADVANCE**. First failing step: none, with the source variation kept in SA Theorem 4's **raw dimensionless datum** \(B\). The first failing step of the section's closing conclusion is its assertion that the bound holds “exactly” in the counting pairing: the pairing \(\mu_c\equiv2\), for example, halves every multiplier and has the same bound. Replace “exactly” by “in counting normalization; not uniformly for physical cell weights tending to zero”. This wording correction changes no consumer.

The hand check is independent of any curved inverse estimate:
\[
K^\sharp=K^{\mathsf T}\mu,\qquad
\omega_\mu=\mu^{-1}\omega_1,
\]
by the definition of transpose and injectivity of \(K^{\mathsf T}\). Surjectivity of \(K\) is the named P82° premise. Dividing rows by \(\ell\) changes the multiplier to \(\ell\omega\); it does not change the force.

At the flat datum choose a bare plaquette whose whole stencil is farther than \(3L\eta\) from \(\Omega_1\). Such a stencil exists for every depth: put the deeper nested cubes in a sufficiently large torus and leave a bare outer region. At zero, \(\omega(0)=0\), so differentiation contributes no \(DK\)-term. For a raw perturbation \(e_c\), the reduced datum derivative is exactly \(e_c\): no outward-row block factor reads that distant bond. Hence
\[
K_0h=e_c,\quad \eta h(c)=e,\quad h(b)=0\ (b\in\partial p\setminus\{c\}),
\]
\[
(e,\dot\omega_1(c))=\langle h,F''(0)h\rangle_f
=\kappa\eta^4\sum_{p'}|(dh)_{p'}|^2
\ge\kappa\eta^4|\eta^{-2}e|^2=\kappa|e|^2.
\]
Use the real positive colour inner product (equivalently the positive trace convention for Hermitian potentials). The Wilson Hessian is nonnegative at the identity, so all other plaquettes can be dropped. Neither a gauge choice nor a cancellation elsewhere can remove this one plaquette's contribution. Cauchy–Schwarz and the pairing identity give
\[
|\dot\omega_\mu(c)|\ge\kappa\mu_c^{-1}|e|
=\kappa L^{4k}|e|\qquad(\mu_c=\xi_c^4=\eta^4).
\]
The diagonal distance is zero. This contradicts a depth-independent unweighted value bound. For per-length **output multipliers**, with the same raw input \(B\), the factor is \(\eta\cdot\eta^{-4}=L^{3k}\). If one also reparametrizes the *input* by per-length coordinates, a second factor \(\eta\) appears; the note's \(L^{3k}\) must not be quoted for that different derivative.

SA 9740 supplies the raw-datum derivative and unweighted multiplier norm; SA 10012–10016 and 11761–11773 explicitly use cell-weighted transposes. The counterexample applies to their physical-weight interpretation \(\mu_c=\xi_c^4\). It is not necessary to infer a missing numerical definition of \(\mu_c\) from the word “weighted”: the exact conclusion for any chosen pairing is the \(\mu_c^{-1}\) bound above. Repair the statement by specifying counting multipliers, or bounding \(\mu_{c'}\dot\omega_\mu(c')\). The force, the paired constraint Hessian and the scalar pairing \(\lambda\cdot Dq\) are unchanged. This settles the normalization issue at real critical references, conditional on the existing counting bound; it does not certify the separate complex-reference clauses.

## D. `meet-6c.md` §§0–2 — verdicts and the hole test

| Section | Verdict | First failing step |
|---|---|---|
| §0, result | WRONG as a claim about the unspecified outline localisations | Treating Proposition 7.1's chosen maximal erosion as the supplied outline assignment (D1). The analytic implication below survives. |
| §1, statement and inputs | CORRECT-NO-ADVANCE | None as an explicitly defined auxiliary problem. Formula (1.1) is a choice, not a quotation of SA 9646/9783. |
| §2, counterexample attempts | ADVANCE as a check of the boundary input | None under the stated geometry and analytic premises. “No counterexample” alone is not the argument; the exact bare model is. |

**2.1–2.2, hole boundary.** A tile meeting any component of \(\partial\Omega'_0\), together with its full operator/gauge read enlargement, is disjoint from \(\Omega'_1\) when its fixed diameter is smaller than the first gap. The repaired P82° construction chooses the gap after that diameter. Thus all its rows are bare, including at reentrant corners and narrow components. In the fine and counting pairings,
\[
Q'=I,\quad K=\eta I,\quad K^{\mathsf T}K=\eta^{-2}I,\quad R=0.
\]
Unitarity and the finite incidence count give \(0\le D^{\mathsf T}D\le16\eta^{-2}\) and \(0\le\mathfrak d^{\mathsf T}\mathfrak d\le24\eta^{-2}\). The curl form plus row mass is consequently between \(\eta^{-2}I\) and \(25\eta^{-2}I\) (at most \(41\eta^{-2}I\) if the enlarged vector block also includes \(DD^{\mathsf T}\)); removing allowed coordinates or using zero extension preserves these form bounds. The constraint directly fixes the vector variable in the bare saddle system. Scaled energy and derivative norms remove the remaining mesh powers. This uses the **actual curved curl**, exactly the D3 repair in `p82-curved-gate.md`, not a small-curvature perturbation where Reg is vacuous. Interior tiles use Reg on their full gauge cubes. Neither argument knows whether the boundary component surrounds a hole. Separation of the explicit meets is checked next.

**2.3, topology.** For the class component in question, SA 17317's boxing operation and the small-component/quarantine assumptions at 17576 make the core a box; \(X\) is the later enlarged box. In four dimensions a box with a strictly interior box removed has the homotopy type of a three-sphere. This observation is unnecessary to the inverse argument. Nontrivial global holonomy in W4 causes no obstruction: on each embedded contractible gauge cube a flat connection is gauged to 1 by path transport; transitions are unitary, and the exact bare calculation handles the boundary. No global gauge or global Poincaré estimate is being inferred.

**2.4–2.5, collar regularity.** A fine plaquette across four coarse blocks of a lifted datum has precisely the old coarse plaquette holonomy: internal links cancel and the four crossing links are the coarse values. In a newly bare strip this can have size \(\varepsilon\), whereas the original background's bound is \(B\varepsilon(\eta/\xi_j)^2\). Thus the warning about original-scale regularity is correct. In the meet's own units it is allowed, and Section A supplies Reg with those units. The fact that new datum tests reduce to coarse tests is checked in Section F; it must precede applying A1.

**2.6–2.7, global scope.** Global \(P,H\) require globally regular label data. A completely prescribed bare plaquette with three links 1 and one link \(-1\) has holonomy \(-1\), so no compatible small-curvature background exists; local regularity near \(X\) cannot replace I5. This elementary counterexample is independent of a run. The decay-set problem at other holes is real and is repaired in Section G, rather than by deleting those holes from the domain.

## E. `meet-6c.md` §3 — ADVANCE for the explicit meets, conditional on the stated geometry

First failing step: none for Lemmas G and J* and Lemma 3.2 **with the explicit maximal localisations of Section H**. Applying G(c) to a different, unspecified source assignment inherits D1; it is not supplied by this calculation.

**Lemma G, line by line.** For W1/W2, aligned \(\mu\)-cube membership is the definition of \(X^-\). For W3, \(\check R_{k_\flat}\le L^{\mathsf N}\check R_k\) and the power-of-\(L\) convention make each coarse cell a union of the smaller cells; complements and intersections preserve this alignment. For W4, the box and its added \(M\)-cube layer are unions of \(\mu\)-cubes. These statements need no smooth boundary. The W1/W2 collars have distance to \(X^c\) between \(M\check R/4\) and \(M\check R/4+6\mu+2\). The W4 collar is within \(5\mu+2\) of \(\Lambda\). The gap \(d_\infty(\Lambda,X^c)\ge2M\check R-M\), with \(M\ge80\mu\) and \(\check R\ge2\), puts all three collars in \(X\setminus\Lambda\), hence in the prepared and healed top layer. They also avoid the localisation collar.

For W3, a point of its thickened collar is in \(X\setminus C\). Since \(\Omega_{k_\flat}^c\subset Z_{k_\flat}\), it is in \(\Omega_{k_\flat}\). Since \(C\subset Z_{k_\flat}\) and \(d_\infty(Z_{k_\flat},\Omega''_{k_\flat+1})\ge LM\xi_{k_\flat}\), it cannot lie in the next member. This proves the single-layer assertion, including the extra double-block margin. Prepared members have the claimed \(M\)-cube gaps by Proposition 2.3; label members have its cell gaps. Take \(M\) above the fixed thresholds making both \(LM\) and \(2cM\check R_j\) exceed \(\rho\) (or increase the subsequent lower ceiling on \(\check R_j\)). This is an explicit constant choice, not an inference that an unspecified positive \(c\) is 1. Localisation separatedness follows independently from the meet argument of Section H, so there is no circular use of G(c).

**Lemma J*.** Parts (a)–(e) repeat the valid geometry of Section B, now on \(\Omega_0\cap A\). The change of first member causes no new failure: (a)'s induction is entirely in \(A\); for \(q>j\), the single-layer collar excludes \(\Omega_q\) and restores the gap of the frozen tower factor; the complement identity includes both \(\Omega_q^c\) and \(T_{\min(q,j)}^c\). Cube alignment then gives (b) at every level. In (c), \(d(x,A^c)>e_j\) forces all tower memberships. In (d), a row touching the strip cannot reach any higher member across a distance greater than its length; all remaining differences are the dropped level-\(j\) rows and added lower rows. Their endpoints lie in \(S\). Enlarging to double blocks yields (e). Pre-existing holes of \(\Omega_0\) far from \(\partial A\) introduce no added rows: on that part the entire sequence is unchanged. Corollary 3.1 follows; equality of the two joined data is supplied by Lemma C, not by separation alone.

**Lemma 3.2.** The metric in SA 9600 uses weight \(\eta^{-1}\) everywhere outside \(\Omega_1\), including outside \(\Omega_0\). Thus memberwise containment compares the path integrands on the **whole torus**, giving \(d_{\mathbf B}\le d_{\mathbf B'}\). For \(z\in\mathcal C_A\subset S^+\), take a nearest point of \(A^c\) and stop the segment at its first exit. All preceding points have distance at most \((\rho+3)\xi_j\) from \(A^c\), so are in the layer-\(j\) collar. In four dimensions the segment has Euclidean length at most \(2(\rho+3)\xi_j\); its metric cost is at most \(2\rho+8\), allowing endpoints. For every \(z\in\mathcal C_A\),
\[
d_{\mathbf B}(y,A^c)\le d_{\mathbf B}(y,z)+2\rho+8.
\]
Taking the infimum proves (c). This is the needed **one-sided** comparison and does not assume D2's false equivalence. If the forcing set is empty, the comparison is exact; no infinite exponential weight is needed.

## F. `meet-6c.md` §§4–5 — ADVANCE as implications for the specified meets

**§4, Lemmas C and D. First failing step: none under EXT, I5 and the explicit localisation convention.** For W1/W2 the \(X^-\) collar is farther from \(X^c\) than \(3\mu+3\), so all original members and geometric row data there survive localisation. For W3 both backgrounds use the same sequence: shell data are \(e^{ig_kB}V_0\); exterior top-level data and outer collar lifts agree by EXT. Core data are excluded. For W4 both prepared and healed sequences are top-level throughout \(X\setminus\Lambda\), while outside \(X\) they are the unchanged history; EXT supplies datum equality. Intersecting either member of a pair with the same tower therefore gives the same members and the same old and lifted new data.

Only the **distances to \(A_i^c\)** are equal for the two original metrics: stop any path on its first exit from \(A_i\), where the layer weights have agreed up to that exit. Equality of distances between arbitrary pairs of interior points is neither needed nor implied, since a shortest path could leave \(A_i\).

For Lemma D, a fine lift plaquette stays in one coarse block, crosses one face, or meets four coarse blocks. Its product is respectively 1, \(V1V^{-1}1=1\), or a conjugate/oriented copy of the coarse plaquette. The norm of the last is exactly a datum test. At each finer seam, nested blocks ensure that internal contours see only identities and crossing contours see the same coarse link; their closed ratios are 1. Hence one averaging step returns the next lift exactly. Repeating this reduces a mixed test to one of those three cases, without a loss per level. Old seams away from the modified strips retain their original tests.

The comparison gauge is constructed down complete old level-\(j\) blocks, fixes their centres and is 1 outside their union. It fixes **every old node**; hence all old geometric rows keep their prescribed values even if their interior/outward type changes. The mismatch logarithm lives on the added rows. The one-step error recursion is
\[
E_q\le E_{q+1}+C_L\varepsilon_1L^{2(q-j)},\qquad E_j=0,
\]
so \(E_q\le C_L\varepsilon_1/(L^2-1)\). This supplies the small \(B_0\) required for admission. Each datum test reads four rows and at most a finite one-step mean; its uniform local Lipschitz estimate makes \(e^{itB_0}\mathbf V^J\) regular at \(C_L\varepsilon_1\) for all \(0\le t\le1\). The radius ceiling is imposed before using the holomorphic chart.

**§5, Proposition 5.1. First failing step: none at this same input boundary.** Its clauses are checked in their logical order:

- (a) Lemma J* supplies all gaps and aligned cubes. The admitted torus has half-side at least \(CM\check R_k\), with \(M\gg\mu,\rho,M_{\rm P},W\); all smaller-level read cubes also fit. This verifies the three floors, including the whole gauge enlargement.
- (b) The geometry and Lemma D, with the small radius, meet A1's hypotheses; an arbitrary first member and its holes are allowed. This gives P81, not merely a candidate reference.
- (c) Apply Section A in the meet's units and absorb Lemma D's fixed enlargement into \(C_L\). Thus \(\alpha=C_LM'\varepsilon_1\le\alpha_*\).
- (d) Apply the repaired P82° theorem, including its supported-source and exact-bare-model repairs. Its fixed constants do not depend on the number or topology of holes.
- (e) Restriction preserves constraints by the averaging induction: level-zero rows without an endpoint in the next member are fixed; at higher levels either the row is directly constrained or its averaging carrier is already covered by the previous induction. A new boundary has a strip of fixed bare rows, so crossing plaquettes have no allowed variation and criticality restricts. Curvature bounds only improve under refinement. At a new action boundary the current changes, but the at most six surviving plaquettes give \(|J_W(b)|\le C\varepsilon_1\eta^{-3}\), exactly the new bare-scale bound. Apply uniqueness only after this regularity enlargement.

The order of constants must include a common response rate \(\theta\le\theta_0\); choose \(\delta_0\) below the input decay rates before setting \(\theta=\delta_0/8\). The fixed geometric thresholds precede the coupling ceiling. No constant is chosen from the depth or the history. None of these steps repairs D1's identification with an unspecified source assignment.

## G. `meet-6c.md` §6 — Theorem M ADVANCE; Corollary 6.1 needs a distance repair

First failing step of Theorem M: none under Proposition 5.1, Lemmas C–D and the explicit geometry just checked. In particular the change of decay set in the note's D1 is justified; it does **not** follow by replacing \(W^c\) in the statement of 6(c) without redoing its forcing argument.

Let \(\mathcal C=\mathcal C_{A_i}\), and use
\[
w(y)=\exp(\theta d_{\mathbf B}(y,\mathcal C)).
\]
For any two tops,
\[
\frac{w(y)}{w(z)}\le e^{\theta d_{\mathbf B}(y,z)}
\le e^{\theta d_{\mathbf B'}(y,z)}.
\]
Thus it is an allowed **all-weights** weight on the joined problem. After the collar gauge, \(B_0\) vanishes on every old row. The exact reduced datum has forcing \(D\mathsf b(tB_0)B_0\) only within its fixed read enlargement \(D_L\) of the added rows. Therefore
\[
\|D\mathsf b(tB_0)B_0\|_{Y,w}
\le C_b e^{\theta D_L}C_L\varepsilon_1.
\]
This is a supremum estimate for one whole source vector; there is no factor counting collar rows. Apply the weighted saddle inverse and the uniformly small nonlinear perturbation, whose Neumann inverse is bounded by \(4/3\). Integrate the response along \(tB_0\). Apply the fixed-reference second-derivative equation (39) before integration. These operations give all three members of (6.1) with decay from \(\mathcal C\).

Section E then gives
\[
e^{-\theta d_{\mathbf B}(y,\mathcal C)}
\le e^{\theta(2\rho+8)}e^{-\theta d_{\mathbf B}(y,A_i^c)}.
\]
The common meet and common datum give one \(U_i^\circ\). The restriction and alignment gauges fix old nodes, yielding the claimed top values of the final gauge. The two original distances to \(A_i^c\) agree by Lemma C(e). This proves the stated constant \(E\), up to the already named fixed analytic constants.

**Why old holes do not become sources.** In W4, near a pre-existing hole away from \(\Lambda\), the members, rows and data of both backgrounds and the meet are unchanged. Those rows are old, so \(B_0=0\) there. No part of the forcing estimate measures distance to that hole. The same bare model still controls the inverse there, with the large allowed weight. Consequently the estimate decays from \(\Lambda=A_4^c\) even at such tops. By contrast, decay from \((\Omega_0\setminus\Lambda)^c\) would indeed lose the required smallness at them. The proof establishes the note's D1 repair as an implication, not merely as a suggested substitution.

**Corollary 6.1 as literally stated: WRONG; repaired consumer implication: ADVANCE. D3 — endpoint-to-top loss.** First failing step: the R7 assertion that every assigned top has crossed all \(n_{\rm c}\) margin shells, giving the exact lower bound \(LMn_{\rm c}\). The consumer assigns a plaquette to its **finest** corner pillar (`sa-2.8-terms.md`, opening of §4). A plaquette crossing the outer face of the last margin shell has \(\psi(p)=0\), hence belongs to \(\operatorname{supp}\phi\), but is assigned to the fine top *inside* that last shell. Here is an explicit aligned-face construction: write the successive right faces as \(b_0,\ldots,b_n\), \(n=n_{\rm c}\), choose \(b_n\) on the last coarse cube grid, and recursively set \(b_r=b_{r+1}-LM\xi_{k_\flat+r}\). Each face is on its own cube grid, because the grid ratios are odd powers of \(L\). Choose nested rectangular boxes with these faces and with the other faces admitting the same normal segment. The finest assigned top at a plaquette crossing \(b_n\) is the centre of the last finer pillar inside that face, a positive fraction \(\delta\) of a local spacing short of it. The normal path to the core then costs \(LMn-\delta<LMn\). Only this upper bound on the distance is needed; no shortest-path assertion is required. This is a hand counterexample to the exact stronger bound, not to the required decay. **Repair, proved:** retain a fixed stencil loss \(C_L\), then use the weaker \(Mn_{\rm c}\) bound after enlarging the fixed \(M\). For R3/R6, a top supporting the cutoff has depth at least \(3M\check R/4-O(1)\) in \(X\); the cubical \(X^-\) boundary has depth at most \(M\check R/4+\mu\). The metric dominates Euclidean distance, yielding \(M\check R/2-\mu-O(1)\), and the displayed \(-2\) covers the nearest-pillar/stencil convention. For R7 every path to \(C\) crosses the nested margin shells. Between \(Z_j\) and \(\Omega_{j+1}\) the gap is at least \(LM\xi_j\) and the layer weight is \(\xi_j^{-1}\); each full crossing costs at least \(LM\). Assigning an endpoint plaquette to its pillar can cost only a fixed number of local units. Even retaining that loss, \(LMn_{\rm c}-C_L\ge Mn_{\rm c}\) after the fixed choice of \(M\), which is the bound used by 5.4. No exact endpoint version of the stronger \(LMn_{\rm c}\) is needed. R1's cutoff lies at distance at least \(M\check R-O(1)\) from \(\Lambda\) by GEO1, with the same harmless stencil allowance.

All these tops avoid their meet's changed strip, so the original and meet scales agree there. Replacing \(E\) by the fixed multiples just obtained leaves the estimates 5.2–5.5 in their stated form, including the global R1 sum with the already supplied counting lemma. This checks the transfer of I1, not the independent proof of that counting lemma or the other six terms of 2.8. For the *actual* localised backgrounds, the source-assignment qualification in Section H remains necessary.

## H. `meet-6c.md` §7 — WRONG for identification; ADVANCE for the specified maximal localisation

First failing step: “This is the outline's localisation.” SA 9776 does say that localisations are cube-wise meets, but SA 5598–5610 requires an **actual supplied erosion assignment**. SA 9783 does not identify that assignment with maximal second-rule erosion. Separation and a lower gap do not imply the upper erosion-depth bound used for (SEP-L).

This is D1 again, now at the consumer that actually needs it. A translation-compatible assignment returning \(T_0=X\) and \(T_q=\varnothing\) for all \(q\ge1\) satisfies both the nested-cube and lower-gap conditions (empty members are allowed). On an original constant torus sequence, its meet is all bare and does not agree with the original sequence deep inside \(X\). Thus lower-gap information alone cannot prove (SEP-L). This example is not asserted to satisfy the separate qualitative interior-agreement clause of SA 6(c); it isolates precisely why the quoted erosion inequalities do not select or certify that clause.

**Visible repair, proved for a chosen assignment.** Supply
\[
T_0=X,\qquad
T_{q+1}=\bigcup\{Q:\ Q\text{ aligned of side }\mu\xi_{q+1},\
 d_\infty(Q,T_q^c)\ge\mu\xi_{q+1}\},\qquad
(\mathcal L_X\Omega)_q=\Omega_q\cap T_q.
\]
Use this as the actual localisation definition, or retain its identification with the previously chosen source assignment as an unproved premise. Intersecting aligned cube unions preserves cubes of size \(\mathfrak M\xi_q\); the two gap lower bounds are \(>\rho\xi_q\) and \(\ge L\mu\xi_q>\rho\xi_q\). Their minimum gives separation and (G1)–(G3). The same distance induction as J(a) now gives
\[
e'_q=2\mu\sum_{r=1}^q\xi_r\le3\mu\xi_q\le3\mu.
\]
Every point farther than \(3\mu\) from \(X^c\) survives every factor. A row whose endpoint membership changes has length at most 1; extending to its double-block carrier stays within \(3\mu+3\). Hence (SEP-L), including old row and datum equality off that strip, holds for this assignment. The collar lies in the top layer: \(X=H_k^{[10]}\), \(\Omega_k^c\cap X=H_k^{[8]}\), and the two cell layers dominate \(5\mu+2\); preparation only removes the inner nest, and healing fills \(X\). The torus floors were checked in §5. No other property of a hole is needed.

The repair can also be expressed without choosing maximal erosion: assume an explicit assignment with a proved erosion-depth upper bound \(e'_q\le C\mu\xi_q\), then widen the fixed collar constant accordingly. Merely assuming Proposition 2.3's geometry of the prepared/healed sequences does not supply this missing property of the separate tower assignment. The note's unconditional “given Proposition 2.3” identification therefore does not pass.

## I. `meet-6c.md` §8 — WRONG as an unqualified closure; repaired implication retained

First failing step: the table's promotion of (SEP)/(SEP-L) for the **outline's** localisations as proved from Proposition 2.3 alone. It inherits the unprovided erosion-assignment identification of §7 (D1). The subsequent assertion that `a3-close.md` Consequence 3 is confirmed inherits the same problem. The three substantive defects, in order of effect, are:

1. **D1, source assignment:** a proven auxiliary maximal cut-meet is not an identification of the source's supplied erosion rule. It blocks the claimed closure for the existing localised backgrounds. A concrete valid construction is written in Sections B and H; adopting it as the definition, or proving equality/appropriate upper-erosion bounds for the actual assignment, remains necessary. No source file is changed by this gate.
2. **D2, weight equivalence:** collar containment supplies only the one-sided distance inequality. Replace the stronger claim by that inequality; Sections E–G prove it is sufficient. This repair is complete.
3. **D3, shell-distance endpoint:** the literal \(LMn_{\rm c}\) bound at every assigned top drops an endpoint loss. Retain \(C_L\), then spend the factor \(L\) to obtain the consumed \(Mn_{\rm c}\) bound. This repair is complete after the fixed constant choice.

The multiplier's final “exactly counting” wording also needs the elementary scope correction in Section C; the lower bound and consumer-invariant pairings pass. This is not an additional analytic obstruction.

The note's own D1 (decay from \(A_i^c\), especially \(\Lambda\)) is **ADVANCE as an implication** by Section G. Its D2 (intersect the first member with the part), D3 (cubical \(X^-\)), D4 (rename the collar count), and D5 (global I5) are **CORRECT-NO-ADVANCE** as scope/definition corrections, with no failing step. None certifies Proposition 2.3, EXT or global I5 themselves.

| Scoped section | Submitted verdict | What survives / first failure |
|---|---|---|
| `a3-close` §1 | ADVANCE | Reg implication; no failing step. |
| `a3-close` §3 | WRONG | First failure is identifying the cut with SA's definition. Explicit Lemma J geometry passes; use the one-sided mismatch bound. |
| `a3-close` §4 | WRONG in the closing exclusivity phrase | Lemma M passes, including \(\kappa L^{4k}|e|\); the corrected normalization conclusion is ADVANCE. |
| `meet-6c` §0 | WRONG | Source-localisation closure inherits D1. |
| `meet-6c` §1 | CORRECT-NO-ADVANCE | Valid auxiliary statement and input boundary; no failure as such. |
| `meet-6c` §2 | ADVANCE as an implication | Exact bare-boundary argument; no failing step under the geometric premises. |
| `meet-6c` §3 | ADVANCE for the specified meets | Lemmas G, J*, 3.2 pass with the explicit maximal localisations and the stated source geometry. |
| `meet-6c` §4 | ADVANCE as an implication | Coincidence, lift tests and datum admission pass under EXT and the specified localisations. |
| `meet-6c` §5 | ADVANCE as an implication | Proposition 5.1 passes on that same boundary. |
| `meet-6c` §6 | WRONG in the exact R7 top-distance claim | Theorem M passes; Corollary 6.1's consumed estimates pass after D3. |
| `meet-6c` §7 | WRONG for source identification | Maximal-assignment Proposition 7.1 is proved; equality to the unspecified source assignment is not. |
| `meet-6c` §8 | WRONG as an unqualified closure | Retain the repaired analytic implication and the assignment obligation. |

Research disposition: the analytic comparison on explicitly specified meets, including domains with holes and decay from the actual modified part, can be used with its named premises. Rows 103/104 cannot be promoted in their unqualified “outline's actual localisation” form from these notes alone. This gate grants no scientific or audit status. Section 2 of `a3-close.md` was not reviewed. Only this gate file was edited in the checkout.
