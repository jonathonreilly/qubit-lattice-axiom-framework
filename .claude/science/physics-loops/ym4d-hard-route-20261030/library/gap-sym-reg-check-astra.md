# Repo search

Writer: OpenAI Codex (GPT-6; the precise deployed variant and effort are not exposed to this session). Research check of `gap-sym-reg.md` at `fe992a7a02068a50163227825908aee499f1c5e2`, not an audit; no status or mass gap is claimed. Not covered: a solution of O1, O2 or POT, later boundary-Q work, a wrapping-box extension of CURL, typical-pin estimates, or the complete upstream proof chain. All mathematical checks below are by hand; tools retrieve text and save this report only.

The target-specific prior digest is absent. The supplied November 8 repo-search digest concerns earlier RG targets, not row 1034. Its near word matches concern flat covariance, boundary gauge admission and transfer correlations. The lead's reported search is acknowledged as a search report, not a theorem. I checked these potentially relevant hits:

| Source checked | Closeness and use |
|---|---|
| `origin/main` at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`, `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` | A score/covariance identity for a supplied noncompact Dirichlet Maxwell law. Different measure and conclusion; no supplier for LF, PRIV, BD or CURL. |
| Same main, `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:4–9,79–94` | Exact/coexact/harmonic cochains for finite-clock Villain variables. Different field and law; not a potential for the present c. |
| Fetched PR 10114 at `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | A one-step loop-correlation bound via a convolution operator. It does not address frame-current conservation. The digest reports the same source on PR 10133; I did not repeat that fetch or the lead's full PR search. |
| Local `gap-global-reform-max.md:506–529`, Lemma MC | Direct predecessor of STAPLE's conjugation symmetry and its empty consumer. Credited and reused below; LF's normalized covariant field and singular-set argument are checked separately. |

The registry, open-core and l17c searches found no owner for this cross-provider check. O1/O2/POT and later boundary-Q work are not new proof targets here. No claim of an exhaustive fresh search of every PR is made.

Disclosure: a broad FINISH locator printed the row-1035 verdict summary before this check. It also printed the later row-1036 summary. At that point neither proof/check file had been opened. The check therefore is not blind. My first-pass line-by-line verdicts were saved before opening the full `gap-sym-reg-check-opus.md`; the comparison follows them below. The later boundary-Q file was not opened.

## Checkpoint

Completed: bounded prior-source/index checks; the hand checks of the numbered statements; saving the first-pass verdicts; then reading the full Claude check and comparing it below. Open obligations remain O1, O2, POT and its analytic hypotheses. No new proof route was attempted. The next decision belongs to the lead: apply the scope corrections before using this row. The original source and shared state files were not edited.

Source state: pinned checkout confirmed; only this report is editable. Downloads are in the newly created `/tmp/sa-gap-sym-reg-check-astra.RWC3q3/`: `sa_ym4.tex` and `sa_ca_I.tex`, fetched once each at Sussman–Alpoge commit `31a47c543775`. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for that construction and all source material taken from it.

## Own verdicts, saved before reading the full Claude check

Line numbers in this section refer to `gap-sym-reg.md`, not this report. A HOLDS verdict checks the stated implication only. The lattice differences use the note's convention `(d lambda)_l = lambda_tail - lambda_head`. The coefficients theta are fixed real numbers, not configuration-dependent functions.

The null-set arguments can be checked without an analytic black box. In stereographic coordinates on each S3, every polynomial in quaternion entries becomes a rational function with a positive denominator. A nonzero numerator polynomial has a null zero set: induct on the number of real coordinates, applying the finite-root fact to each nonexceptional one-dimensional slice and Fubini to the coefficient-polynomial exceptional set. The omitted chart points are null. This applies to every determinant and cross-product witness below. All measure comparisons use the strictly positive, finite-volume Wilson density.

### 1. Identities LINK and STAR (4.0, L63–81): HOLDS

For one link, the product rule gives `div_mu(n.R) = div_Haar(n.R) - n.N = -c`. This proves L65–68. At a free vertex, write its gauge generator as the outgoing left generators minus the incoming right generators. Both Haar measure and A are invariant. The divergence of the variable-axis gauge field is the trace of `a -> [e_a,n]`, which is zero. Subtracting its incoming part proves L72. Subtracting the incoming current then gives L74–75, including the sign `-exp(A) rho_z`. At a source corner there is no incoming term. This is a pointwise divergence identity; a finite flow through a singular set needs further justification.

### 2. STAPLE (6.1, L163–180): HOLDS

There is prior work: **Lemma MC in `gap-global-reform-max.md:506–529`**, by Claude Fable 5.2, already constructs `M -> k M k^{-1}` and proves preservation of the action and conditional Haar measure. Thus L51 and L429–430 need that local citation. STAPLE is its infinitesimal version; LF adds a covariant axis, unit speed, and a singular-set integration argument. This overlap does not duplicate the present check of LF/PRIV/BD/CURL.

Fix the other links. Right multiplication by the unit staple sends the link to `M`, with density proportional to `exp(kappa Re M)`. Differentiate MC's conjugation with `k=exp(s a)`: its left-trivialized velocity is `b=a-Ad(M)a`. The orbit keeps `Re M` and `a.Ad(M)a`; hence it keeps both the action and `|b|`. It is an isometry, so its Haar divergence is zero. Dividing by the orbit-constant `|b|` preserves both zero divergences. This verifies (i)–(iii) and L174–178, including the factor 4 in the derivative of `|b|^2`. Covariance follows by conjugating the staple loop and axis together.

### 3. LF (6.2, L182–201): HOLDS

The chosen plaquette axis does not read the moved link. Its gauge transformation is at the correct tail. On a finite lattice with the indicated plaquettes and positive strengths, the exceptional set is closed and analytic. In the displayed witness, the staple has imaginary part `beta sin(phi) i` and the axis is `sin(phi) j`; their cross product is nonzero. The same construction applies after changing the direction. Thus the exceptional set is proper and null. The range is bounded independently of volume.

For fixed other links, the normalized flow preserves each conjugation circle and translates its angular coordinate by an orbit-dependent constant. Disintegrating Haar measure along those circles proves invariance even though the vector field is singular on the fixed circles. Its speed is one, so differentiation against bounded C1 tests is dominated. Fubini proves the claimed global integration by parts. Consequently `c_l=0` in L2 and (REG) holds. This avoids any unjustified inference from codimension alone.

For the consumer, let Y be the added interior field. Then `div_mu Y=0`, `Psi_(B+Y)=Psi_B`, and `E[Y Psi_B]=0`. Therefore both the variance and the cost in FLOW are unchanged. This proves L196–200 for FLOW-admissible extensions. The identity `exp(pi n_l)=-1` is pointwise only; it is not a claim that the time-pi orbit of this varying-axis field is a central twist.

### 4. SPAN (6.3, L203–212): HOLDS

The three indicated private links Q_mu are distinct, including modulo 3, and each affects only its selected outgoing force. Conditional on all other links, each selected force ranges over a translate of a ball with nonempty interior. Choose the first force nonzero, the second outside its line, and the third outside their plane. The determinant polynomial is therefore not identically zero. Its zero set has Haar measure zero, and the positive Wilson density has the same null sets. The assertion requires those Q_mu to be free variables; it is not a statement for arbitrary frozen pins. The source's qualification that all incident plaquettes are present must be retained.

### 5. PRIV (6.4, L214–229): HOLDS

The independence hypothesis concerns **all five frames**, n_z and its incoming neighbours. Missing one link from n_z alone is insufficient. P is not incident to z. Among the plaquettes using P, precisely p also uses an incoming link of z, namely l. On a period-three torus, the second parallel translate is distinct; it introduces no additional incoming link. Thus the derivatives in div d and the four vectors Dn are independent of P, while the force on l has the displayed affine dependence.

On a fibre the equation is `alpha + beta*w*v.Im(g P^{-1} h)=0`. Left/right multiplication and inversion preserve Haar measure on S3. If v is nonzero, this equation cuts a proper affine hyperplane section of S3, which has Haar measure zero (also at a tangent point). Fubini therefore forces v=0 on almost every positive-measure fibre. This proves the a.e. conclusion, not a pointwise assertion at every zero of rho. Subtracting a fixed constant proves L228.

The requested cube test: z=110, l=(100,110), P=(101,111). The plaquette (100;2,3) contains l and P; the other plaquette through P contains no incoming link of 110. The hypotheses concern n_110, n_100 and n_010. Hence the same fibre argument applies. No enumeration or numerical test was used.

### 6. Corollary P and its range count (6.5, L231–255): HOLDS, with bulk scope retained

The five offsets in F are exactly P as seen by n_z and the four incoming neighbours. If the two indicated direction classes are missed, PRIV forces parallel transport along both directions at every site on the conserved set. Two adjacent plaquettes then have a common transported axis. The two-link witness in L240 makes their axes i and j, so the corresponding polynomial is nonzero. This proves that the conserved set is null. The argument is for the bulk lattice or torus, or a box containing the needed two adjacent plaquettes and all private links; it is not an arbitrary tiny-boundary statement.

Classes (a)–(d) have the advertised missing offsets. For (d), a staple of (x,1) or (x,2) cannot read a direction-3 link at height +e4 with the listed -e3 offset, or its direction-4 counterpart. For the count: failure in two directions is excluded, leaving at least three good directions. For fixed mu, a link can cover two different nu only through the offset `e_nu+e_nu'-e_mu`; it cannot cover three. Three sets therefore require at least two links per direction, hence six. These are necessary conditions, not a construction.

**Correction to L412 and RESULT (2):** replace “removes every frame where (REG) is free” by “removes past-built frames and the other specified missing-offset classes.” A frame may avoid its outgoing links, giving d=0 and linkwise integration by parts by Fubini, while reading forward links. P does not exclude that entire class. Smoothness off a closed null set remains a separate part of (REG).

### 7. BD (6.6, L257–285): HOLDS for the theorem; consequences HOLDS AFTER CORRECTION

Freeze the boundary rotation at the pin, as FLOW requires. The only moved interior link is (z,4), and its axis n_z is constant in the interior variables. Thus its Haar divergence vanishes. An infinitesimal gauge rotation at z, applied to the action including its pinned links, removes the outgoing-force sum. The remainder is exactly the three incoming terms in L261. The private link P_i is free, and only the i-th incoming force reads it. Applying the affine-fibre argument separately to the three P_i proves L262. No smoothness in the pin is needed for this fixed-pin implication.

For simultaneous conservation at all relative-interior lower-face sites, with the stated side lengths, choose two distinct plaquettes in the interior face subgrid. Their four transports obey Dn=0. Their transported axes must then be parallel. Two noncommuting face holonomies violate this analytic equation; the simultaneous-conservation pins form a null set. This proves the needed null-set consequence. L271's phrase “at each site” should refer only to plaquettes whose four links are controlled. It need not include every plaquette touching the outside edge of the face.

There are two essential quantifiers. At **one** z, Dn=0 on its incoming star does not imply that the entire pin is reducible. One can choose a covariant vector at z from a pin loop and transport it backwards along those three links, for an otherwise irreducible pin. The generic conclusion is instead: **for almost every pin, some boundary indicator lambda has nonconstant Psi**. It is not “every nonzero boundary gradient has positive variance.” L149–153, L371–372 and the final summaries must retain this distinction.

**First failing cost inference: L275.** FLOW gives `Q(d lambda)=H_c+Var(Psi)`. A positive variance implies the FLOW inequality is strict. It does not imply Q is nonzero: the hypotheses have not excluded `H_c=-Var(Psi)`. Nor does BD prove invariance under interior gradients unless bulk conservation (J) and the relevant integration by parts are also supplied. In particular, pin-measurability alone does not supply interior (J).

Replace L275–277 by: “For these boundary gradients Psi is nonconstant, so they are not measure-preserving extensions in the sense used by JAC. The equality Q=H_c+Var(Psi) does not decide whether Q vanishes or is invariant under boundary gradients. If interior (J) and the required integration by parts hold, adding a gradient with lambda zero on pinned sites leaves Q unchanged.” Apply the same repair to L150–153, L338–345, L399, L405, L413–421 and RESULT (3). A quadratic form on d theta plus boundary data is a possible representation under interior invariance, not proof that its boundary dependence is nontrivial.

The value in L283–284 has the correct sign for frozen axes. Gauge away the outgoing rotation. On an incoming link the remaining curve is `exp(-eps a) exp(eps v) U`, where `a=n_tail`, `v=Ad(U)n_z`. Its initial velocity is `b=v-a=-Dn`; its extra left acceleration relative to `exp(eps b)U` is `-2 a cross v`. Since the action derivative is `-b.N`, minus its second derivative is the direct b-term minus `2(a cross v).N`. Averaging yields L283. It supplies no fixed sign.

The theorem covers the particular extension in which the **same pin-measurable n_z** rotates the three outgoing face links and the inward link. The consumer requires the boundary values to be pin-measurable. It does not force an arbitrary interior extension on the inward link to use that same vector. BD is therefore a valid obstruction for its stated class, not for every possible extension allowed by FLOW. Upper faces and link-dependent boundary axes remain outside it.

### 8. CURL (7.1, L290–318): HOLDS under (a)–(c), on the stated interior box geometry

The signs give `Psi=-<d theta,phi>` and

`Q=-E[V_theta Psi]=sum_p (d theta)_p E[V_theta phi_p]=E[Psi^2]`.

For a one-link theta, (c) also gives `K(l,p)=E[phi_p c_l]`. L2 and finite support make each local row finite. A uniform k_1 remains a supplied bound if a volume-uniform conclusion is wanted. No estimate against beta follows merely from (REG).

Only plaquettes p with `(d theta)_p` nonzero matter. The support margin puts the closed link star of their boxes B_p inside W, so a site function supported in B_p has its whole gradient in W. This is the needed boundary justification at L304–305. From (a), every such gradient has Psi=0; (c) then says K's functional annihilates it.

Here is the comb count without assuming the claimed constant. Root B_p at its lower corner and choose the tree path in coordinate order 4,3,2,1. Integrating theta on that tree defines lambda and kills every tree edge. A direction-j edge can be moved to the tree by commuting it across the preceding coordinates 1 through j-1. This uses at most `(j-1)(m-1)<=3m` unit plaquettes. The signed sum of their curls is theta'_l. Thus the nonnegative majorant kernel has row sum at most `3m k_1`.

For a fixed plaquette p', at most m^4 origins per orientation can have p' inside their m-site box. There are six orientations. Each kernel entry is at most k_1, so the column sum is at most `6m^4 k_1`. Applying `2|xy|<=x^2+y^2` gives `(3m+6m^4)k_1/2`; since m>=3 this is at most `4m^4 k_1`. This verifies L308–311. No covariance-decay assumption was inserted.

The boxes must be ordinary embedded cubical boxes, as the proof says. On a periodic lattice this directly covers nonwrapping boxes. A wrapping case needs a choice of global cut and treatment of harmonic cochains; it is not proved by the printed comb argument. This is a domain clarification, not a counterexample to the interior box bound. The conditional proposition does not supply phi for a site frame.

### 9. FLUX and POT (7.2, L320–332)

**FLUX: HOLDS.** Summing the scalar conservation equation over a slab cancels all internal links and equates its two face fluxes. The size condition allows a parallel face whose complete read set is disjoint. Under product Haar measure the two flux functions are independent. If independent real random variables are equal almost surely, each is constant: for any rational cut their common event has probability equal to its square. Equivalence of the finite Wilson and Haar measures transfers the equality and the constancy. REG with a single-link theta and f=1 gives E[c_l]=0, so that constant is zero. Rotate coordinates to obtain all four fluxes.

**L327–328: HOLDS AFTER CORRECTION.** Replace “a continuous family of maps that preserve the measure” by “Psi=0, hence an infinitesimal measure-preserving field; a finite flow requires existence and regularity across its singular set.” FLUX itself is a statement about currents. It does not prove that flow theorem.

**POT's explicit unproved status: HOLDS; the asserted implication at L332: FAILS.** The stated POT only supplies a local potential representing c. It supplies neither phi in L2 nor integration by parts with phi and Psi as tests. REG in L41–42 only covers smooth tests. Replace L331–332 by: “If POT holds, it supplies (a) and locality in (b). Proposition CURL still needs L2 for phi and the extended integration-by-parts identities (c).” No verdict here proves or refutes POT itself. Its recalled literature attribution was not verified or used.

### 10. Controls, SING and the numbered tests (4.1–4.4)

**4.1 U(1), L83–87: HOLDS.** With a constant axis, ordinary Gauss conservation gives `c=d* (beta sin F)`. Differentiating the sine gives the signed incidence coefficient `beta cos F`. Consequently the cost is exactly `sum beta E[cos F_p] (d theta)_p^2`, bounded by the classical beta form. Inhomogeneous positive strengths use beta_p w_p termwise. STAPLE is the zero vector in the abelian case; there is no normalized version of that zero vector. This is a control, not a gain.

**4.2 One plaquette, L89–90: HOLDS.** Its radial density is proportional to `exp(beta cos phi) sin^2(phi)`. Its score is `-h`, with `h=beta sin(phi)-2cot(phi)`. Thus the four link currents have incidence signs, h is L2, and integration by parts has no endpoint term: the density vanishes quadratically while h grows only like inverse distance. Differentiating h gives `beta cos(phi)+2/sin^2(phi)`, verifying L316–317 too.

**4.3 Cube, L92–105: HOLDS as a partial construction and explicit open remainder.** STAR settles 000. At the three sites of outdegree one, STAPLE with an axis from the opposite transported plaquette settles the incoming sum at 111. It leaves the six displayed equations. It does not prove that those equations are inconsistent. The inherited corner obstruction is sound: writing `N1=beta(s_p+s_q)`, `N2=beta(s_r-s_p)`, differentiation of `(N1 cross N2)/|N1 cross N2|` gives `d1=-beta(N1.s_r)/|N1 cross N2|`. Near `s_p=s_q=e3/4`, `s_r=e3/2`, the numerator is nonzero and the transverse part eta of N2 has two free coordinates. Its square has the divergent integral `integral d^2 eta/|eta|^2`. This checks the cited failure of REG; it does not extend it to all cube frames.

**SING, L109–114: HOLDS.** After the local gauge transformation, every constant SU(2) rotation on the read box fixes the read data. Locality and covariance would force the unit vector to be fixed by all adjoint rotations, which is impossible. The gauge transformation outside that read box may change other links without affecting this argument.

**Odd-torus application, L116–132: HOLDS AFTER CORRECTION of the summaries' range quantifier.** The displayed gauge transform makes every link central on each nonwrapping read box. The conclusion applies when the frame's read box is nonwrapping, in particular with the lemma's `L>=2r+2`. It does not apply to every finite-range rule on a fixed small torus. The winding-loop frame in L121 is the note's own exception. At the example it gives n=-i, D_2 n=D_3 n=-2i, and cot(phi_P)=0, hence c=0. Near it, PRIV excludes conservation on a positive-measure set because those D terms stay nonzero. Its radial L2 and integration-by-parts checks are the plaquette calculation with a winding product in place of U_p. Replace L118 and the SING summary at L389/RESULT by the nonwrapping qualifier; replace L132 by “zero forces alone do not construct an admissible local frame with conserved current on a positive-measure set.”

### 11. Decisions, open statements and final table (5, 7.3–7.4, 8)

**5(1): HOLDS. 5(2): HOLDS with PRIV's five-frame hypothesis and P's exact missing-offset condition. 5(3): HOLDS AFTER CORRECTION as in item 7 above.** Missing one member of F is not the same as missing the entire five-link F; L144–145 and L412 must use the latter condition. Pointwise zeros of rho are not excluded by an a.e. no-positive-measure conclusion.

**7.3: HOLDS AFTER CORRECTION.** The interior zero-gain statement is correct. The claimed failure of a boundary curl cost does not follow from BD; retain only its obstruction to the JAC measure-preserving-gradient mechanism for the stated extension class. The size comparison cited at L341 and the proposed typical-pin route are not used as proved inputs here.

**7.4 O1: HOLDS as an OPEN candidate, not as an equivalent restatement of the original task.** L349–351 demand a full-measure domain, whereas L23–25 ask about a positive-measure set. A proof of O1 would answer the stronger problem; failure of this full-measure version would not itself exclude every positive-measure construction. A1's equation count proves no obstruction; A2 loses the affine-fibre argument once a frame reads P; A3's zero conditional mean uses the unpinned gauge-invariant law. Those are honest failed approaches, not impossibility proofs. The claimed general implication about the consumer must use item 7's corrected scope.

**7.4 O2: HOLDS as an OPEN required boundary inequality for the specified extension; HOLDS AFTER CORRECTION at L371–372.** Replace those lines by: “For each direction with nonconstant Psi, O2 requires `H_c<=-Var(Psi)<0`. BD guarantees such a direction for almost every pin in its stated class, not for every boundary lambda. Neither existence nor failure of O2 is proved here.” The identity is relative to the selected interior extension because the variance is. The sign-changing displayed plaquette term alone decides no averaged sign.

**8, L383–407 and L409–440: HOLDS AFTER CORRECTION.** LINK, STAR, the controls, STAPLE/LF, SPAN, PRIV/P, BD's theorem, conditional CURL and FLUX have the verdicts above. Replace the claimed failure of an exact boundary Q-form by the failure of constant Psi for BD's class; keep Q-invariance and O2 unresolved by this text. Keep POT's analytic inputs open. Preserve SING's size condition and O1's stronger domain. No mass-gap implication or status follows.

Checkpoint before comparison: the first-pass mathematical verdicts above had been saved, and the full row-1035 check had not yet been opened.

## Comparison with Claude Opus 5.5, read after the saved verdicts

The complete 467-line `gap-sym-reg-check-opus.md` was then read. Its three principal corrections are right: a nonconstant Psi does not establish a nonzero Q; P does not remove every d=0 frame; and POT does not supply CURL's L2 and integration-by-parts assumptions. I agree with its hand algebra for LF, PRIV/P, SPAN, BD's theorem, CURL's constant and FLUX. There is no disagreement about those core implications. “FAILS at L332” above and Opus's “HOLDS AFTER CORRECTION” describe the same failed inference and the same replacement, not competing mathematical conclusions.

The following are all substantive differences or additional qualifications in this check. “Source” means row 1034; “Opus” means row 1035.

| Point and exact lines | Resolution: who is right, and why |
|---|---|
| First failing boundary-cost line: Opus L249/L446 locates it at source L399. | **Codex's earlier location is right.** The unsupported proof inference already occurs at source L275; its summary is already asserted at L151–153. L399 repeats it. Opus's mathematical correction is right. |
| BD quantifiers: source L149–151, L271–274, L371–372; Opus L239–245, L445, L457–460. | **Codex's explicit quantifier is needed.** Opus's proof at L239–242 correctly establishes a null set for simultaneous conservation. It does not establish failure at every site or strict concavity in every boundary direction. At one site the incoming star can be parallel-transported on an otherwise irreducible pin. The correct generic conclusion is existence of some failing boundary direction. |
| Boundary polarization: Opus L255–260. | **Opus L255 is right for interior theta; its L260 criterion needs that restriction.** For arbitrary boundary theta, polarizing FLOW gives `Q(theta,g)=H_c(B_theta,B_g)+Cov(Psi_theta,Psi_g)`, with g=d lambda. The Hessian cross term vanishes when theta has zero boundary values, but not in general. Full invariance requires Q(g)=0 and Q(theta,g)=0 for every theta, not covariance zero alone. This is a correction to the check's repair, not a decision of Q-invariance. |
| Interior invariance: source L275–277; Opus repair L459–461. | **Codex's conditional wording is right.** JAC proves interior-gradient invariance when bulk (J) and the needed integration by parts hold. BD's hypotheses alone do not supply them. The unconditional phrasing must not be read as a new BD consequence. Opus's reading of the consumer class at L276–291 otherwise agrees with mine. |
| PRIV/P summary: source L144–145, L395, L411–412; Opus L403–412. | **Both agree on the d=0 correction; Codex adds a necessary hypothesis correction.** The missing private variable must be absent from all frames appearing in rho. For the translation-invariant support condition that means D misses an entire F_(mu nu), not merely one of its five links. The theorem statements are right; the compressed summaries must not weaken them. |
| SING summary: source L118, L389, RESULT; Opus L379/L394/L435. | **Codex's nonwrapping qualification is right.** Both proofs establish the lemma under L>=2r+2. The blanket “every local frame” wording omits that condition. The source itself exhibits a winding-loop frame defined at the small-torus example, with c=0 there. The theorem is sound; the unqualified summary is not. |
| O1's domain: source L23–25 versus L349–351, L367; Opus L452/L458 (A1–A3 expressly not checked at L463–464). | **Codex's distinction is right and was not covered by Opus.** The full-measure O1 is stronger than the original positive-measure existence question. Failure of that stronger version alone would not settle the original question. Both checks leave existence open. |
| CURL geometry: source L304–308; Opus L308–321/L448. | **Both counts are right for embedded boxes.** Codex makes explicit that the printed comb proof does not cover a wrapping box on a small torus. This is a limit of the checked domain, not a refutation of the constant or a claim that the wrapping extension is false. |
| Existing staple symmetry: source L51, L429–430; Opus L39–42/L82–96. | **Codex's additional local credit is warranted.** Row 1016 Lemma MC is the same finite conjugation symmetry. LF's normalization and REG proof add work beyond MC. This does not contradict the limited no-colour-frame index search, but neither search establishes novelty of the conjugation symmetry. |
| Size wording at source L341; Opus explicitly leaves it unread at L463–464. | **Additional Codex check below: the lower bound holds.** “Of order” must mean “at least a constant times”; a two-sided estimate for every potential is false under arbitrary additions of gradients. This is added coverage, not a contrary Opus verdict. |

Two qualifications are shared, not disagreements. Opus L337–338 already notices that FLUX does not construct a global singular flow; this report propagates that qualification to the source's L327–328. Opus L215–218 correctly restricts SPAN to free private variables and distinguishes j=0 from c=0 with j=d nonzero. Both restrictions are retained here.

**Post-comparison completion of L341: HOLDS AFTER CORRECTION to a lower bound.** I then read its cited `gap-pinned-cell-gauge-max.md:234–261`. For constant curl f in the 1–2 plane, take a face x4=0 and its S+1 slices of fixed x3. In each slice, use concentric squares centred at `(floor(S/2),floor(S/2))`, of radius k from `ceil(S/8)` to `floor(S/4)`. For S>=16 there are at least S/16 edge-disjoint perimeters. Each side length r=2k is at least S/4. Stokes and Cauchy–Schwarz give a squared-link sum at least `f^2 r^3/4 >= f^2 S^3/256` on each perimeter. Distinct slices use distinct links. Therefore every potential has boundary squared norm at least `f^2 S^5/4096`. By contrast, adding `t d lambda` for any nonconstant boundary lambda preserves the curl and makes that norm unbounded as |t| grows. Replace “of order f^2 S^5 for every choice” by “bounded below by a positive constant times f^2 S^5 for every choice.” This is geometry only. It neither proves a lower bound on Q nor repairs BD's failed cost inference. Other constant two-form components are handled by selecting a nonzero coordinate component; no numerical estimate is used.

## Bounded upstream reading and coverage limits

The outline index README, matching chunk rows with neighbours, and relevant obligations were used before the corresponding source reads. Queries included staple, colour/color frame, current, conserved current, Jacobian current, Ward, gauge invariance, local Poincare, comb tree, flux and Schur. Broad current/frame hits include unrelated RG objects; they are not evidence of a frame theorem or an absence theorem.

| Locator read | Source lines read at `31a47c543775` | Finding and use |
|---|---|---|
| `sa-index/chunk-01.md:25–35,42–49`; `obligations.md:10–28` | Outline 238–293, 394–416 | Finite Wilson measure, endpoint gauge covariance, and the limited content of mass preservation. Foundational context only; no colour-frame current or boundary-cost theorem is supplied there. |
| `sa-index/chunk-12.md:25–32` and corresponding obligations at 690–705 | Outline 13023–13065 | PH8 annihilates gauge gradients in a Hessian at zero, using a vanishing first derivative. This is not (J) for a nonlinear unit frame at arbitrary Wilson configurations. |
| CA 4.12–4.19 README; chunk-01 rows at 21–28 and 139–148 | CA-I 42749–42796, 43928–43959 | Configurations/covariant differences and a perturbed-plaquette covariant curl with a holonomy remainder. The current J at 42786–42796 is a different Lie-algebra current whose listed properties are assumed. None is a potential phi for c=j-d. |

These are comparisons, not fresh checks of the Sussman–Alpoge construction. Their index's no-hit results for the narrow frame terms do not prove that the entire account contains no related result. No Balaban paper was imported. No unseen literature theorem was used to fill POT.

The local source reads additionally covered `gap-short-step-max.md:213–277`, `gap-aligned-frame.md:23–105,196–243`, the (REG) and corner computations in `gap-aligned-frame-check-opus.md:103–148,184–213` and the located (REG) clauses at 224–252, the odd-torus correction in `gap-short-step-check-astra.md`, `gap-pinned-cell-gauge-max.md:131–182,234–261,460–485`, and the indicated current-state ranges of `parts/gap.md`. Theorem E is only background for this check; its implicit-function construction was not rechecked. The frozen-axis interpretation of FLOW is essential throughout the BD calculations. No numerical run, symbolic algebra run, exhaustive enumeration or proof-assistant check was performed.

RESULT: LF, PRIV/P, SPAN, BD's stated fixed-pin theorem, conditional CURL with constant 4 m^4 k_1, FLUX and the qualified controls HOLD by hand; the boundary-Q inference and POT-to-CURL inference fail as written and require the corrections above. Claude's three main corrections are confirmed, with additional quantifier, domain, polarization and prior-credit corrections. O1, O2, POT and boundary-Q invariance are not settled by this row; no mass gap, audit verdict or status is claimed.
