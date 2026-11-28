# Gate of `o1-decoupled.md` — queue row 129
Provenance: OpenAI Codex (GPT-6), effort xhigh (row-129 assignment); checkout `8fac7b66059b7951e8691344c772a0c5ebef69bd`; Sussman–Alpoge outline commit `31a47c543775`; research text, not an audit, granting no status.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's current continuation, response specification, decoupling mechanism and hereditary-domain statements used here. Credit Tadeusz Balaban for the local-inverse walk construction and restriction method. SA line numbers refer to the outline fetched once into `/tmp/sa_ym4.tex`; library line numbers refer to this checkout. Named inputs are checked for their use, not re-proved or promoted. All mathematical checks below are written arguments; source retrieval and text extraction supply no mathematical discharge. The entry-point `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent from the sparse working tree; its rules were read from the pinned Git object.

## 0. Result — WRONG as a completion claim

First failing claim: “All three parts of row 126 are proved as implications” (source line 16). The lift identification and Theorems A–B advance under their named premises. C1 proves its stated enlarged-read-set identity, but Theorem C changes between two native metrics, pillar partitions and energy norms without the required comparison; Theorem D inherits this gap. Lemma RI and Theorem I advance conditionally; the actual-datum constants and gauge-product order have explicit repairs below. Five defect groups are recorded, without reopening the declared input theorems. All source sections, including their counterexample discussions and final dependency claims, were checked.

## 1.1. Identification — ADVANCE as an implication

**(I-a): first failing step: none.** Write \(G^{-1}=M_J+Q^{\mathsf T}aQ\), \(W=QGQ^{\mathsf T}\). Then \(QGQ^{\mathsf T}W^{-1}f=f\) and \(G^{-1}GQ^{\mathsf T}W^{-1}f=Q^{\mathsf T}W^{-1}f\). The annihilator of \(\ker Q\), for the nondegenerate bilinear physical pairing, is \(\operatorname{ran}Q^{\mathsf T}\), also over the complex numbers. A difference \(v\) of two constrained stationary fields satisfies \(v=GQ^{\mathsf T}\nu\), \(W\nu=0\); hence \(v=0\). Removing the row mass changes only the multiplier. Thus \(K_0H=mQ\mathsf Hm^{-1}=I\), with no assumption \(J=J(\mathbf U)\).

**(I-b): first failing step: none.** Re-eliminate the scalar subsystem: \(h=G'Q'^{\mathsf T}NQ'G'D^{\mathsf T}A=(1-R)D^{\mathsf T}A\), \(\lambda=G'RD^{\mathsf T}A\). Substitution in the quadratic form gives \(DRD^{\mathsf T}\). At equal arguments the three terms in \(c_J\) are exactly the three pairs in SA 10175–10190, each pair cancelling the prefactor \(1/2\). Setting the *row coefficient* \(j=0\) removes \(S^{\mathsf T}\Delta^{(2)}[j]S\), not the independent fine current \(J\). The remaining Schur equations are \(G^{-1}A+Q^{\mathsf T}\nu=0,\ QA=f\), whence \(\nu=-W^{-1}f\) and \(A=GQ^{\mathsf T}W^{-1}f\). Thus the block is \(\mathsf H\); the R9 lift is that block times \(m^{-1}\), exactly as SA 10356–10368 specifies.

**(I-c): first failing step: none in the resolvent identity.** Use the same raw constraint \(K_0A=B'\) for both lifts (or the same per-length constraint for both). Subtract the saddle systems to get \(H-H^\circ=-T^\circ E_JH\), hence \(H=(I+T^\circ E_J)^{-1}H^\circ\). This also shows what “differ at first order” means: the first variation is \(-T^\circ E_JH^\circ\), which can vanish for particular pairs, including the flat zero-current pair. The claim is a distinction between operators in general, not universal non-equality. No estimate for this resolvent is used in Theorem A.

## 1.2. Theorem A — ADVANCE as an implication

**First failing step: none.** The repaired Lemma L is used on exactly its declared complex, independent-current domain at coefficient \(j=0\). Its additional second-jet premise for nonzero \(j\) is therefore irrelevant here; the current-continuation bounds remain part of (I1).

For a unit colour \(e\), the physical row pairing of \(e\delta_c\) with \(\nu\) is \(\xi_c^4 e\cdot\nu_c\). Since \(\|\nu\|^2=\sum_c\xi_c^6|\nu_c|^2\), its dual norm is exactly \(\xi_c\). This is an operator source with value \(e\), not a coordinate functional with value one. Lemma U therefore produces the counting-measure column \(\mathsf H(\cdot,c)e\). Dividing by the input-row factor \(\xi_c\) gives the asserted bound for \(H\); no residual mesh or depth factor remains. A three-colour basis costs at most \(\sqrt3\).

On a pillar, Cauchy–Schwarz gives

\[
 \eta^4\sum_b\xi_b^{-3}|A_b|
 \le (\eta^4\sum_b\xi_b^{-4})^{1/2}
      (\eta^4\sum_b\xi_b^{-2}|A_b|^2)^{1/2}
 \le2\|m^{-1}A\|_{2,y}.
\]

For the curl, the real transport contributes first differences, and changing a link to \(e^{i\eta A'}U\) contributes \(O(|A'|)|A|\); the latter is absorbed by the mass term because \(\xi|A'|\le\alpha_1\). Adjacent pillars cost only \(C_L\). Multiplying by \(w(c)/w(b)\le e^{\theta(d(y,c)+4L)}\) leaves the summable rate \(\tau_L-\theta\ge\tau_L/2\). The stated ball count applies since \(\tau_L\rho'\ge256\log L\). This proves both absolute sums in (O1), rather than inferring columns from a row estimate. The three counterexample discussions do not introduce an additional premise.

## 2.1. Definition D and parameter cubes — ADVANCE as a specified construction

**First failing step: none, with (P) retained.** The enlarged physical hull includes the field read set and the normalization read set. Multiplication by its parameter monomial is a definition permitted by SA's operator-as-data convention; it does not preserve \(QH=I\), nor claim to. At \(s=1\) it changes no term.

(P) is satisfiable uniformly in depth. In top units \(\xi_{\max}=1\), choose a periodic grid of side \(s\ge\ell_{\mathsf P}/2\), on a torus with room for at least three such cubes in each direction. More generally use \(s\ge\ell_{\mathsf P}\xi_{\max}/2\). Weighted distance dominates periodic Euclidean distance divided by \(\xi_{\max}\). A set of weighted diameter \(<\ell_{\mathsf P}/2\) therefore projects into an arc of length \(<s\) in each coordinate and meets at most two intervals per coordinate. For the periodic assertion, a subset of a circle of length at least \(3s\) with pairwise distances \(<s\) lies in one arc of length \(<s\): otherwise its extreme points on opposite sides of any chosen point have separation in \([s,2s)\), whose circular distance is at least \(s\). Thus there are at most \(2^4\) cubes. Small tori can instead use a one-cube partition, for which (P) and splitting are trivial. A nontrivial grid on every torus requires the corresponding room assumption; its size is not allowed to track the finer local mesh.

Balaban CMP 99 (389–434), pp. 408–410, fixes the smaller local-inverse scales before the larger walk cells, constructs cut-down inverses, and pays walk counts with the commutator power while retaining decay. Those pages do not identify walk cells with parameter cubes or prove (P). The separate coarse parameter partition is consistent with that construction. The parameter estimate comes from SA 10552–10560 and the proof below, not from an unproved citation to CMP 99.

## 2.2. Lemmas P and WC — ADVANCE as implications

**Lemma P: first failing step: none.** Separation bounds the diameter of each \(\kappa^\sharp\) by \(16L^3M_1\). Each non-root cell meets an admissible path; the root is within one pillar of its starting point. Thus the enlarged hull lies in the \(r_1\)-neighbourhood of the path. An arc of length at most \(\ell_{\mathsf P}/4\) has neighbourhood diameter at most \(\ell_{\mathsf P}/4+2r_1<\ell_{\mathsf P}/2\). Cover a path of length \(t\) by \(\max(1,\lceil4t/\ell_{\mathsf P}\rceil)\) arcs and apply (P). Taking paths approaching the infimum gives
\[
 \#\mathsf P(\omega)\le16+64d_{\mathbf B}(\omega;y,z)/\ell_{\mathsf P}.
\]
This argument uses the **path distance of W**, not an unproved path representation of an arbitrary tree. That is sufficient here. To state the corresponding tree lemma, traverse each tree edge twice and replace 64 by 128. The stronger SA factor for cubes crossed without parameters is not proved here and is not used by B.

**Lemma WC: first failing step: none.** The cubes containing a point form a Cartesian product of one- or two-element index sets, connected by face steps. Every such cube must be included, including at a corner. If a connected set avoiding the removed cubes met two surviving wall-components, intersections with the two finite closed unions of cubes would separate it into two disjoint nonempty relatively closed sets. This proves the stated claim; it does not assert that the carrier cut by \(\Omega_0\) is connected.

## 2.3. Theorem B — ADVANCE as an implication, uniformly in depth

**First failing step: none in the claimed (O1) and splitting conclusions.** Multiplying W's bound by (2.2) spends at most \(\tau_L/4\) of its \(\tau_L/2\) rate. Summation over roots and then over \(n\) gives
\[
 C_LB_Le^{16\bar\kappa}e^{-\tau_Ld(y,c)/4}
 \sum_{n\ge0}(\nu_1C_W/M_1)^n,
 \qquad \sum_{n\ge0}(\nu_1C_W/M_1)^n\le2.
\]
For local energy terms whose forward difference crosses a pillar face, count roots in the adjacent pillar as well; this changes only the bounded-overlap constant and a fixed \(C_L\) rate factor. Repeating Theorem A with \(\theta\le\tau_L/8\) proves (O1). In particular \((\tau_L/8)\rho'\ge32\log L\), enough for the stated count.

At each fixed finite lattice the estimates give a locally uniform limit of holomorphic matrix entries. Uniformity of the localized constants in depth does not require a common infinite-dimensional holomorphic domain. Reality and covariance pass term by term and to the limit. At \(s=1\), W and (I-b) identify the sum. A nonzero term has both endpoints in its connected enlarged hull. If that hull touches a removed cube its monomial vanishes; otherwise WC places it in one wall-component. The retained terms read fields only there. No region-trace locality between different sequences is inferred.

The leftover \(e^{16\bar\kappa}\) is **retained**, not absorbed into the walk ratio or an \(L\)-only constant. It is paid by using
\(C_H=C_LB_LK_{\tau_L/8}e^{16\bar\kappa}\)
and then requiring \(CC_Hr<1/2\) for the current readout. A later R9 contraction must also use its \(\widehat b^{-4}\) datum radius. The source explicitly leaves that contraction and its supremum-norm inputs open. Its shortened formulas suppress \(K_{\tau_L/8}\) only as an \(L\)-dependent constant. None of these choices depends on depth; \(\ell_{\mathsf P}\) depends on \(M_1,\bar\kappa,L\) as stated.

## 3.1. Comparison inputs — CORRECT-NO-ADVANCE

**First failing step: none when these are treated as premises.** (H-pair), (H-node), (H-field), (Box) and (Spec) are additional hypotheses, not consequences of (O1). In particular neither the complex 6(c) estimate nor the Landau node comparison is supplied here. The explanation correctly leaves both open. But (H-seq), as written, is only agreement on a union formed from **original-system** cubes whose fourth enlargements fit in \(G\). It does not say that the regions agree everywhere on \(G\), or impose any comparison of scales outside \(G\). Those distinctions break the next theorem.

## 3.2. Lemma C1 — ADVANCE; Theorem C — WRONG as stated

**C1: first failing step: none for its stated one-way assertion.** For an original cube \(\kappa\) with \(\kappa^{(4)}\subset G\), its full \(\kappa^\sharp\) is in the agreement set. Membership of \(\kappa\) in the other sequence is therefore identical. For any candidate contributing to its cutoff denominator, separation excludes scales two or more steps away: a still coarser candidate is separated by at least \(\rho\xi_{r-1}\), larger than its own cutoff reach, not merely the reach of \(\kappa\). The remaining candidate cubes have scales \(\xi_\kappa/L,\xi_\kappa,L\xi_\kappa\), and their *entire membership tests* fit within \(\kappa^\sharp\). This checks candidates absent in either sequence as well as present ones. The denominator, local cut-down sequence, commutator and parameter monomial are then identical. The local field class is precisely the one admitted by C4 and the repaired W. This proves the needed enlarged-read-set version of (C5) **for these cubes**; it is not assumed.

**Defect 1 — first failing step of C: “the \(\mathcal W_{\rm in}\) families coincide” (line 206).** C1 gives an injection from the original family to the box family, not its converse. For example, take an original top layer of scale one throughout a large neighbourhood, and a second sequence of a much finer scale there. Choose a cube \(G\) large enough for a finer \(\kappa^{(4)}\), but smaller than every original \(\kappa^{(4)}\). Both sequences can be separated (constant layers, with distant boundaries); flat pairs meet (H-pair). The displayed union \(G^\sharp\) is empty, so (H-seq) is vacuous. There is a box inner walk of length zero and no original inner walk. The later assertion that the two metric densities agree on all of \(G\) also does not follow from that displayed hypothesis. If the informal words “agreement region” are intended to add agreement on all of \(G\), this particular omission disappears: any box cube inside \(G\) is then an original cube too, and C1 applies back. The theorem should say so. Defect 2 below persists even on that stronger reading.

**Visible repair:** require agreement on
\[
 G\ \cup\!
 \bigcup_{\kappa\in K\cup K^\square,\ \kappa^{(4)}\subset G}
 \kappa^\sharp,
\]
with common grids and row conventions. Apply C1 in both directions. Alternatively declare only matched cubes to be inner and prove that every unmatched cube is within the stated boundary margin in the appropriate metric. That second proof is absent. The symmetric agreement condition is a concrete sufficient replacement, not a consequence proved for the actual box map here.

The *inner-walk analytic estimate* itself passes under that repair. Set \(R=c\,a_{\min}/\varepsilon_\omega\), choosing the stipulated small constant in \(\varepsilon_P\le c_Pa_{\min}\) so \(R\ge4\). The BCH bounds, first derivatives of \(X\), and the free half of each ceiling admit the whole local complex disc. Cauchy between \(t=0\) and \(1\) costs \(C\varepsilon_\omega/a_{\min}\). The local inverses need no global extension of the interpolated pair. If \(S=D_y+D_c\) and \(\delta\le S/2\), then
\[
 \theta_P\delta+\tfrac{\tau_L}{8}(S-2\delta)
 \ge\min(\theta_P/2,\tau_L/8)S.
\]
For pillars meeting an endpoint support, use \(\delta\le S/2+O_L(1)\), absorbing the harmless offset in the already allotted \(e^{\tau_Lr''}\). This verifies the two-distance decay calculation; it is not the failing step.

**Defect 2 — native norms are replaced by a common norm without justification.** Even after repairing Defect 1, the outer-walk estimates are in the two systems' own energy norms, pillar partitions and scale weights. They do not imply (3.1) in the original energy norm at *every* exterior pillar, or (3.2) for arbitrary globally supported sources measured with only the original \(\xi\). The displayed summation
\[
 \sum_{y\in\mathcal B}e^{-a\min(d(y,c),d^\square(y,c))}
 \le K_{a/2}+K^\square_{a/2}
\]
is false as an application of the two ball counts: \(K^\square\) sums over \(\mathcal B^\square\), not \(\mathcal B\).

A hand obstruction to that counting step is a fixed physical exterior box \(Q\) containing original bare pillars of side \(\eta\), but box-system pillars of side one. The two sequences may agree on a fixed interior neighbourhood of \(c\); separated transitions have bounded total physical width \(\rho\sum_{r\ge0}L^{-r}\). Thus \(d^\square(y,c)\le D\) throughout \(Q\), with \(D\) independent of depth, whereas \(Q\) contains \(c_Q\eta^{-4}\) original pillars. The left side is at least \(c_Q\eta^{-4}e^{-aD}\); the two native ball-count constants stay depth independent. (Box) permits this configuration; it does not require the box sequence to be a cut-down. Moreover the covariant gradient of a box column outside \(G\) is controlled in its own reference, not in an arbitrary original real gauge.

**Visible repair sufficient for the consumer:** use a comparison only on a common interior and keep exterior tails in native norms. Split each anchor/action integral into a common interior and its complement. If the regions and scales agree on \(G\), an exterior source pillar in either system has native distance at least \(D_c\) from a common row \(c\). In each native summation,
\[
 e^{\theta'D_c}e^{-\tau_Ld_\bullet(y,c)/4}
 \le e^{-\tau_Ld_\bullet(y,c)/8}
 \quad(\theta'\le\tau_L/8,\ y\notin G).
\]
Theorem A's pillar calculation and that system's ball count then bound the tail by \(C_H\) times its **own** force/plaquette norm. On common interior pillars the two systems have common scales, so the checked inner-walk calculation applies. This avoids both the false mixed count and a gradient comparison in unrelated exterior gauges. Another sufficient route adds a monotone cut-down assumption plus explicit norm transport, but that transport must be proved. The unrestricted (3.1)–(3.2) in the source are not established.

## 3.3. Lemma K — WRONG under the printed geometry; local estimates survive

**First failing step:** “the same rows, plaquettes and stencils near \(b\), by (H-seq)” (line 221) uses agreement on \(G\) which (H-seq) does not supply. This is Defect 1, not a new defect. Under the symmetric/common-stencil repair above, K1, R1 and F2 follow with the displayed local scales: the row density is \(\eta^4\xi_c^{-3}\); \(R_A\) is a bondwise exponential-series inverse; and \(\eta^{-1}(\operatorname{Ad}e^{i\eta X}-1)=O(X)\).

For F1 the required useful form is slightly more precise than its printed upper bound:
\[
 \xi^3|\delta\mathcal N|
 \le C(\alpha_0+r)e_b+C(r+r^2)x_b.
\]
Indeed \(\mathcal N_U(A)=\Delta'_UA+N_U(A)\); the first part has field derivative \(O(\alpha_0)\) and base derivative \(O(|A|)\), while the second has field derivative \(O(r)\) and base derivative \(O(r^2)\). These are Cauchy estimates on the fixed local coefficient discs of the named inputs. The base derivative vanishes at \(A=0\) for every base. This proves the response factor needed in D; the weaker printed F1 alone does not display it. Outside the common-stencil interior, retain the two separate native estimates.

## 3.4. Theorem D — WRONG as printed; a repaired conditional comparison is visible

**First failing step:** Step 1 applies the unproved global (3.2). Defects 1–2 therefore prevent the claimed implication from the *printed* hypotheses. The anchored subtraction is otherwise the right method and includes the previously missing second anchor and differing action sets. The comparison must be assembled using common-interior differences and native exterior tails as just described.

**Defect 3 — two explicit bookkeeping corrections are also needed.**

1. With the definition immediately following (3.2), put
   \(L= D_{\mathbf U}H\), \(L^\square=D_{\mathbf U^\square}H^\square\).
   The exact anchor identity is
   \[
    \delta\lambda_0=(L-L^\square)^{\mathsf T}\mathcal F
                +(L^\square)^{\mathsf T}(\mathcal F-\mathcal F^\square).
   \]
   Step 1's additional \(((D_{\mathbf U}-D_{\mathbf U^\square})H^\square)^{\mathsf T}\mathcal F\) double-counts that change. Alternatively use three terms but define the first as
   \((D_{\mathbf U}(H-H^\square))^{\mathsf T}\mathcal F\).
   Either convention repairs the algebra; they cannot be mixed.

2. The assigned-gauge estimate must retain the corrected S5 factor:
   \[
    \|j^\square_g\|_F
      \le C C_H(1+C_H\alpha_0)\|\mathbf H^\square\|_X.
   \]
   Therefore the node term is bounded by
   \(C\varepsilon_N C_H(1+C_H\alpha_0)e^{-\theta_PD}
     \|\mathbf H^\square\|_X\),
   not the printed \(C\varepsilon_N C_H\) coefficient unless one additionally imposes \(C_H\alpha_0=O(1)\). The latter smallness is not a hypothesis of D. This matters because \(C_H\) contains \(e^{16\bar\kappa}\).

With these repairs the remaining subtraction has no further algebraic failure. On common rows, compression of \(T^{\square\mathsf T}\) has norm at most \(1/4\), so its inverse has norm at most \(4/3\); no inverse identity on two different row spaces is needed. Missing rows contribute separate native boundary sources. Differences of the curl term, \(\mathcal N\), \(T\lambda_0\), and \(T(\lambda-\lambda_0)\) exhaust the multiplier equation. K1 and R1 exhaust the three anchored readout terms. Every source contains either the field difference or one of the two field amplitudes; the corrected F1 above preserves this property. On the common interior the weight can be put on either local factor; exterior sources are bounded by the native-tail estimate. Finally (H-node) gives precisely the corrected node term.

This supplies a route to the intended conditional removed-current estimate, with the strengthened agreement geometry and native-norm formulation explicitly retained. It does not prove those extra geometric/transport facts for the actual removed maps, and it does not close the separately named complex 6(c), (H-field), or Landau (H-node) inputs.

## 4.1–4.2. Restriction mechanism and inputs — CORRECT-NO-ADVANCE

**First failing step: none in the declared setup.** Balaban CMP 109, pp. 277–280, uses (3.38) to transfer the hereditary clause, then separately budgets the endpoint, radial interpolation and independent datum in (3.39)–(3.52). The cited mechanism is accurately distinguished from an endpoint bound alone. Here [9.3] supplies an orbit identity for a separated subsequence at **real regular critical fields**; [Φ] supplies the chosen holomorphic branch. Neither is being read as an independent-current restriction theorem.

The use of [Φ] for \(u\) at all fine sites also needs the axial extension in wf-room-2.md Lemma D(i), as retained by its gate: a3-derivative.md 7.6 states that bound at tops. The extension follows by the same geometric-series product used in RI below, so no additional analytic premise is needed. The input [E] bounds \(B_{\rm end}\) using the simple curvature radius \(\alpha_0\), and its curvature/current endpoint using the tower radius \(a\). They must not be silently identified; see Defect 4.

## 4.3. Lemma RI — ADVANCE as an implication

**First failing step: none after making the radius choices explicit.** Choose \(r_I\) below the [Φ] radius, the [A′] bootstrap radius divided by \(C_{\mathcal H}\), and \(r_B/(4LC_{\mathcal H})\); also choose it so the real datum regularity \(C L^2r_I\) is below the existence radius in [9.3]. All are fixed positive thresholds from the named inputs.

For every allowed \(Z,p,n\), nesting gives
\(T'_q(Z)\subset Z\subset X\subset T'_j(\square_0)\subset T'_q(\square_0)\)
for \(q\le n\), and the smaller sequence is empty above \(n\). Thus [9.3] applies to precisely a separated subsequence. On its carriers the original top scale is one and the smaller scales are at most one. The [A′] bootstrap gives
\(\|B_Z(B)\|_\infty\le2LC_{\mathcal H}\|B\|_\infty<r_B/2\).
This proves existence and holomorphy of the *left-hand side* on the common datum ball before invoking an identity theorem.

For real \(B\), restriction of \(\Phi(B)\) is critical by [9.3]. Gauge covariance with node values carries this orbit to the restriction of \(\mathbf U_{\rm in}\) at its own datum; it does not pretend that the larger gauge is residual for the smaller problem. Fixing the smaller nodes to one and recursively imposing its canonical axial conditions gives the unique residual \(g_Z\). Thus the two representatives agree on the real datum ball. Both are holomorphic on the full complex ball: the right side is a finite product of averages, contour transports and inverses, and the left side is the already admitted composition. Expand their difference in a power series at a real interior point. All real derivatives vanish, hence all complex Taylor coefficients vanish; connectedness extends equality throughout the ball. This supplies the finite-dimensional identity theorem without asserting complex orbit uniqueness.

The condition number is independently bounded on that complex ball. For a level-\(q\) comb the bootstrap gives a logarithm at most \(2C_{\mathcal H}L^{q-j}\|B\|\) per averaged bond, and the comb has at most \(4L\) bonds. Multiplying down the pillar gives, for both \(g_Z\) and its inverse,
\[
 \|g_Z^{\pm1}\|
 \le \exp\!\left(8LC_{\mathcal H}\|B\|
               \sum_{q\le j}L^{q-j}\right)
 \le e^{16LC_{\mathcal H}\|B\|}.
\]
Their product is at most \(e^{32LC_{\mathcal H}\|B\|}\). There is no repeated fixed loss per level and no inference of a complex norm bound from real unitarity. This proves the advertised \(C_g\), uniformly in all the tower quantifiers.

## 4.4. Theorem I — ADVANCE as an implication

**First failing step: none.** The two simple potential bounds follow from [Φ] because the local scale on \(X\) is one. The real factor is the identity. Hypothesis (i) gives the simple complex curvature and current bounds.

For each lower tower, RI gives an actual gauge identity. On the doubly eroded test interior, all incident plaquettes lie inside its first member. Explicitly it is enough to take \(2M>3M_1'+2\): two layers of level-\((p-1)\) \(M\)-cubes provide distance at least \(2M\eta_j\), whereas the first erosion costs at most \(3M_1'\eta_j\) and a plaquette stencil costs at most \(2\eta_j\). This is an allowed choice of \(M\) after \(M_1'\). The local inner-action current therefore transforms by the same adjoint action as the original current, with no boundary-action discrepancy.

The unit conversions are correct:
\[
 L^{-(j-p)}\eta_p^2=L^{j-p}\eta_j^2,\qquad
 L^{3(j-n)}L^{-(j-p)}L^{2(n-p)}=L^{2j-p-n}.
\]
Since \(n\le p\le j\), both factors multiplying the target radius are at least one. The single bound \(e^{C_g\|B\|}|\phi|_X<\alpha_{0,j}\) implies every complex tower clause. The real towers are identically one. This checks both erosion rules and all truncations, not just the largest tower. The stated exclusion of a layered \(X\) meeting smaller-scale parts is necessary and is respected.

## 4.5. Actual datum and constants — WRONG literally; repaired application ADVANCES

**Defect 4 — first failing step:** the opening estimate replaces the input \(\alpha_0^2\) in \(4C_f\|B_{\rm end}\|^2/r_B\) by \(a^2\), without stating \(\alpha_0\le a\). [E] supplies two radii, not this inequality. Later, the claim that the logarithmic factor is at most two does not follow merely from \(x_k\ge\max(C_x,e^2)\) for a general fixed logarithmic exponent \(q\).

For the latter failure, take \(j=k-1\), \(x_j=e^2\), \(x_k=2e^2\), \(C_x=e^2\), \(q=8\). The displayed flow and lower-floor conditions hold. But
\[
 \frac{\alpha_{0,k}}{\alpha_{0,j}}
 =2^{-1/2}(1+\tfrac12\log2)^8
 >2^{-1/2}(5/4)^8>2\sqrt2.
\]
Here \(\log2>1/2\) follows by integrating \(1/t>1/2\) on \((1,2)\), and \((5/4)^4=625/256>2\). This refutes the displayed radius deduction from its explicit numerical floor, not the possibility of choosing sufficiently small couplings in SA 5(c).

**Written repair.** Use one input envelope
\[
 \bar a=\max(a,\alpha_0^{\rm input}),\qquad
 \bar a\le\lambda_a\alpha_{0,k},
\]
where \(\lambda_a\) includes both fixed enlargement factors of SA 5(c). Replace \(a\) by \(\bar a\) in this application only. Fix \(\lambda_a\) before choosing \(L\), or explicitly assume an \(L\) satisfying the displayed inequality; an unspecified \(L\)-dependent factor cannot be absorbed by saying “choose \(L\) large.”

Require all couplings to satisfy
\(x_i\ge X_0\ge\max(C_x,e^{2q},e^2)\).
This is an allowed small-coupling choice. For \(x_j\ge x_k\), the logarithmic ratio is at most one and \(x_j/x_k\le1+(k-j)=m\). For \(x_j<x_k\), the function
\(h(x)=x^{-1/2}(\log x)^q\)
is nonincreasing above \(e^{2q}\), because
\[
 h'(x)=x^{-3/2}(\log x)^{q-1}(q-\tfrac12\log x)\le0.
\]
Thus \(\alpha_{0,k}/\alpha_{0,j}\le\sqrt m\); the source's weaker \(2\sqrt m\) bound follows. This is the explicit floor already used in wf-room.md 4.1.

Choose the field and datum radii so that
\[
 \begin{gathered}
 4C_fC_B^2M^2\lambda_a\alpha_{0,k}\le r_B/8,\quad
 3C_fc_{B'}\le1/8,\quad C_{\mathcal H}c_{B'}\le1/4,\\
 C_BM\bar a\,L^{-m}+c_{B'}\alpha_{0,j}
   <\min(r_I,r_B/4),\\
 C_g(C_BM\bar a\,L^{-m}+c_{B'}\alpha_{0,j})
   \le\log(9/8),\\
 \alpha_{1,j}\ge\alpha_{0,j},\qquad
 \alpha_{1,j}>4C_{\mathcal H}C_BM\lambda_a L^{-1}\alpha_{0,j}.
 \end{gathered}
\]
These give the needed analytic balls, curvature ceiling and potential ceiling. The last inequality is the quantitative content of \(M\alpha_0\ll\alpha_1\); it cannot be replaced by \(\alpha_0\le\alpha_1\).

Finally \(\sqrt mL^{-2m}\le\sqrt2L^{-2}\) for \(m\ge1,L\ge2\): the ratio of successive terms is at most \(\sqrt2/L^2<1\). With
\(L^2\ge6\sqrt2\lambda_a\),
the source's final curvature arithmetic is valid:
\[
 \frac98\left(\frac54\,2\sqrt2\lambda_a L^{-2}+\frac18\right)
 \le\frac98\left(\frac5{12}+\frac18\right)
 =\frac{39}{64}<1.
\]
Also \(\sqrt mL^{-m}\le L^{-1}\), so the endpoint potential is at most
\(2C_{\mathcal H}C_BM\lambda_aL^{-1}\alpha_{0,j}\);
the independent datum adds at most \(\alpha_{0,j}/4\). The written radius relation makes their sum \(<\alpha_{1,j}\). This proves the actual-datum application of I with the repaired explicit choices, uniformly in \(j,k\). The scalar interpolation [7.1] is used on its \(r_B/4\) balls, not merely wherever \(f\) is holomorphic.

## 4.6. Datum transport — WRONG in product order; repaired transport ADVANCES

**Defect 5 — first failing step:** the first paragraph calls the gauge from the Landau field to \(\Phi(B)^{\tilde v}\) “\(u\cdot\tilde v\).” The convention in RI and the cited sources is \(U^g(b)=g(b_-)U(b)g(b_+)^{-1}\). Consequently
\[
 (U^u)^{\tilde v}=U^{\tilde v u},
\]
not \(U^{u\tilde v}\). Noncommuting node factors cannot be interchanged.

**Repair:** use \(h_{\rm raw}=\tilde v\,u\). From the raw field to the lower tower use
\(g_Zu^{-1}\tilde v^{-1}\).
The pillar-constant lift \(\tilde v\) has the same condition-number bound as its node values. The all-site bound for \(u\) follows from Lemma D(i)'s recursion, and RI bounds \(g_Z\). Their products are holomorphic throughout the already admitted independent datum disc and have condition numbers bounded by the product of the three displayed bounds. Reordering correctly changes no scalar estimate. The raw pair is thereby in the stated complex gauge orbit; no hereditary admission of its arbitrary raw splitting is claimed. With Defect 4 repaired, the Landau triple's admission itself is established by I.

## 5. Final disposition — WRONG as the source's completion claim

**First failing table entry:** the removed-map comparison is not proved from the hypotheses as printed. Even reading “agreement region” in its strongest intended sense, the mixed pillar sum and exterior norm conversion in C fail. D inherits that failure. The inner admission is recoverable by the explicit constant choices and transport-order correction above; those are repairs, not reasons to discard RI or I.

| Source section / statement | Verdict | First failure or retained scope |
|---|---|---|
| 0, all three tasks completed | WRONG | C's comparison is not established under its printed hypotheses |
| 1.1, (I-a)–(I-c) | ADVANCE | None; exact independent-current identification and resolvent identity |
| 1.2, A | ADVANCE | None; correct source norm and both (O1) sums |
| 2.1, D and (P) | ADVANCE | None for the specified coarse partition; no claim of other operator identities |
| 2.2, P and WC | ADVANCE | None; path count and wall splitting proved |
| 2.3, B | ADVANCE | None for (O1); the exponential prefactor remains in every consumer constant |
| 3.1, named inputs | CORRECT-NO-ADVANCE | Premises only; agreement must be stated on the required carriers |
| 3.2, C1 | ADVANCE | None for its stated direction, including absent cutoff candidates |
| 3.2, C | WRONG | One-sided agreement as literally specified; independently, mixed exterior norms and pillar count |
| 3.3, K | WRONG as stated | Common-stencil assertion needs the repaired agreement; local algebra survives |
| 3.4, D | WRONG as stated | Uses C's unproved global comparison; anchor convention and node factor also need correction |
| 4.1–4.2 | CORRECT-NO-ADVANCE | None as context and declared premises; keep the two endpoint radii distinct |
| 4.3, RI | ADVANCE | None on the explicitly admitted disc; identity theorem and node bound are valid |
| 4.4, I | ADVANCE | None; all hereditary quantifiers and scale conversions checked |
| 4.5 | WRONG literally; repaired implication ADVANCE | Endpoint radius substitution and insufficient explicit coupling floor |
| 4.6 | WRONG literally; repaired implication ADVANCE | Gauge factors multiplied in reverse order |
| 5 | WRONG as completion claim | Removed comparison still needs its geometry and native-norm repair |

The defects, ranked by what they obstruct, are: **2**, the depth-uniform operator/current comparison; **1**, its literal agreement hypothesis (resolved if agreement on all of \(G\) was intended); **4**, the quantitative admission of the actual datum (repaired here); **3**, the removed-current algebra and constant accounting; **5**, the exact representative transport (repaired here).

What moves is precise: the identification and (O1) for the specified decoupled lift advance conditionally, as do RI and the hereditary Landau admission with the written repairs. The first-system supremum-norm response estimates remain open exactly as the source says. The removed comparison has **additional** geometric/norm obligations beyond its named complex-background, response and Landau-node premises. Nothing here edits those premises, grants status, or updates a queue or ledger. No other repository file, commit, push, PR, audit, numerical proof or subagent work was produced.
