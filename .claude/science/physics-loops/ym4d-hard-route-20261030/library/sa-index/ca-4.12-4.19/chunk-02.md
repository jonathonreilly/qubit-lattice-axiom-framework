# Chunk 02: lines 43939-45237
Sections: Continuation of item 4.12 (no section heading appears); item 4.13 lemmas (45162, 45203); “Route.” paragraph (45228); “Levels, territories, covers and the form at free current” definition begins (45236). No section or subsection title is printed in this excerpt.

The excerpt starts inside a proof and ends at a definition heading. Labels below retain their source spelling; unnumbered named steps are indexed separately. Conditional statuses record reliance on the stated inputs, without deciding their validity. The source repeatedly reserves an incomplete step marked $(\ast)$; the excerpt does not identify that step explicitly.

| Lines | Name / tag | Kind | What it states (one plain sentence, your words) | Status here | Reads (inputs it uses, by tag or name) | Key phrase |
|---|---|---|---|---|---|---|
| 43939–43995 | Perturbed-plaquette proof, continuation | proof | The remaining expansion bounds the perturbed plaquette by the background curvature, derivatives, and quadratic error. | proved conditionally | 4.12:eq-perturbed-plaquettes-3; preceding definitions of Xi and w0; smallness hypothesis | "yields" |
| 43944–43951 | 4.12:eq-perturbed-plaquettes-4 | identity | The sum Sigma equals the covariant curl plus a background-holonomy correction. | proved in detail | Preceding expressions for X1+X2 and X3+X4 | "therefore gives" |
| 43952–43959 | Adjoint-difference bound | estimate | Conjugation by g changes A by at most twice the product of their relevant norms. | proved in detail | Unitary g; matrix norm | "because" |
| 43961–43965 | 4.12:eq-perturbed-plaquettes-5 | estimate | Sigma is bounded by two covariant derivatives and four times background curvature times w0. | proved in detail | perturbed-plaquettes-4; adjoint-difference bound | "give" |
| 43967–43982 | Expansion of the four exponentials | proof | Scalar exponential series bound all terms of total degree at least two. | proved conditionally | s ≤ 4 eta w0 ≤ 1 | "by hypothesis" |
| 43979–43982 | 4.12:eq-perturbed-plaquettes-6 | estimate | The exponential product differs from one by at most eta times Sigma plus twelve eta-squared w0-squared. | proved in detail | Scalar remainder estimate | "Consequently" |
| 43984–43995 | Conclusion of perturbed-plaquette proof | proof | Multiplication by the unitary background yields the desired full plaquette estimate. | proved conditionally | perturbed-plaquettes-3, -5, -6 | "yields" |
| 43997–44008 | Gauge covariance of the constrained minimiser; 4.12:lem-minimiser-covariance | lemma | Gauge-transformed admissible data have gauge-equivalent constrained minimisers. | proved conditionally | determining-sets-a,c; constrained-minimisers-a,b; gauge invariance | "This is the assertion" |
| 44010–44065 | Proof of minimiser covariance | proof | A blockwise gauge bijects constraint manifolds and preserves criticality so uniqueness up to gauge applies. | proved conditionally | constrained-minimisers-b(i),(ii); determining-sets-c | "applies to" |
| 44016–44029 | Blockwise extension of g | construction | Extending g constantly on each block produces inverse maps between the two constraint manifolds. | proved conditionally | determining-sets-c | "maps" |
| 44042–44049 | 4.12:eq-minimiser-covariance-1 | estimate | The transformed minimiser retains the curvature bound needed for uniqueness. | proved conditionally | constrained-minimisers-b(i); B3 epsilon1 ≤ epsilon0 | "the strict inequality is the bound" |
| 44067–44084 | An arithmetic bound on the gain factors; 4.12:lem-gain-arithmetic | lemma | The two gain functions obey uniform bounds above and below k0. | proved in detail | L ≥ 3 L0²; L0 ≥ 2; N0 ≥ 1 | "It therefore suffices" |
| 44068–44072 | k0, f1, f2 | definition | k0 is k minus N0 and the gain functions are square-root factors times inverse powers of L. | definition | k; N0; L | "put" |
| 44076–44078 | 4.12:eq-gain-arithmetic-1 | estimate | Dividing either gain by the intermediate-level L0 factor gives at most L0 to minus twice N0. | proved in detail | Gain lemma hypotheses | "this gives" |
| 44080–44082 | 4.12:eq-gain-arithmetic-2 | estimate | Below k0 both gains are bounded by the first gain at N0. | proved in detail | Gain lemma hypotheses | "monotonicity gives" |
| 44086–44125 | Proof of gain arithmetic | proof | Comparison with f1 and decreasing successive ratios prove both bounds. | proved in detail | Definitions of f1 and f2 | "The bound for" |
| 44127–44197 | Re-blocking inside admissible boxes; 4.12:prop-reblocking-inside | proposition | Sufficiently small couplings give consumer minimisers and bounds strictly inside their real derived-slot radii. | named open | Source-space standing conditions; Phi0–Phi2; Gamma0–Gamma3; determining sets; constrained minimisers; consumer radii | "proof incomplete at the step marked" |
| 44130–44147 | Inside-box parameter hypotheses and threshold | hypothesis | The source standing conditions and floors are imposed and N0 must exceed an existential threshold activating Gamma0–Gamma3. | assumed | not-admissible-boxes; def-coupling-thresholds; B-CMP122a coupling relation | "Suppose" |
| 44149–44164 | Consumer minimiser UE(p,X'') | definition | UE minimises with the averages of the real source factor on the consumer determining set. | definition | def-determining-sets; def-constrained-minimisers | "Write" |
| 44167–44169 | Inside-box clause (a) | construction | Balaban's theorem supplies UE with epsilon1 equal to twice the running radius times ell-p squared. | proved conditionally | B-CMP102b Theorem 1; reblocking-inside-1; coupling-thresholds-d | "It is obtained from" |
| 44170–44186 | Inside-box clause (b) | estimate | Curvature and current have separate explicit bounds for consumer levels above and below the slot level. | named open | Inside proposition and its incomplete-step proviso; above/below-slot lemmas | "proof incomplete at the step marked" |
| 44183–44186 | Kb | definition | Kb collects the geometric and averaging constants with the box diameter. | definition | d; cQ; cd; L; DQ | "Here the constant" |
| 44187–44195 | Inside-box clause (c) | estimate | Both real derived slots lie strictly within the consumer target radii. | named open | Inside proposition incomplete-step proviso; consumer radii | "proof incomplete at the step marked" |
| 44199–44208 | 4.12:eq-reblocking-inside-c | estimate | The box-gauge datum is first order in each coarse bond length. | proved conditionally | Axial gauge; determining-sets-d; below-slot steps (i)–(ii) | "The proof establishes two further bounds" |
| 44209–44218 | 4.12:eq-reblocking-inside-d | estimate | Below the slot level both target ratios have a square-root times inverse-L gain divided by vartheta. | proved conditionally | below-slot steps (vi)–(viii); running-radii-a | "The second holds" |
| 44220–44308 | Proof of clause (a) and block-scale bound | proof | Averaging verifies the minimiser theorem and interior geometry controls the local block scale. | proved conditionally | admissible-boxes-a; determining-sets-a,b,e; coupling-thresholds-b,d; constrained-minimisers-b | "This proves clause" |
| 44238–44243 | 4.12:eq-reblocking-inside-1 | estimate | Averaged data satisfy the coarse plaquette hypothesis with epsilon1 = 2 alpha0,k ell-p². | proved conditionally | determining-sets-e; coupling-thresholds-d(i) | "It gives" |
| 44247–44258 | Imported minimiser existence theorem | theorem | Balaban's theorem yields the constrained minimiser after the smallness conditions are checked. | cited | B-CMP102b (7), Theorem 1; constrained-minimisers-a,b | "That clause is" |
| 44261–44268 | 4.12:eq-reblocking-inside-a | estimate | UE has curvature and current bounds expressed using its local determining-set scale. | proved conditionally | constrained-minimisers-b(i); epsilon1 | "it satisfies" |
| 44271–44303 | The block scale on the interior | proof | Boundary depth and neighboring block levels give the scale lower bound without asserting a neighbor bound for cE. | proved conditionally | consumer-radii-b; Phi1; determining-sets-a,b | "The following two facts suffice instead" |
| 44300–44303 | 4.12:eq-reblocking-inside-b | estimate | The smallest nearby block has size at least ell-min(p,nE) divided by L. | proved conditionally | Interior block-level argument | "Thus" |
| 44310–44318 | Real-factor interpretation of clause (c) | remark | Clause (c) supplies the real half of consumer clause (iv) for all four composites off the core. | proved conditionally | Inside clause (c); composites' real factor equals bar-U | "The reason is" |
| 44320–44338 | Points at or above the slot level; 4.12:prf-above-slot-level | lemma | For n ≥ p the real curvature and current bounds use at most half the consumer radii. | proved conditionally | Inside hypotheses and clause (a); reblocking-inside-a,b; consumer radii; Gamma thresholds | "Assume the hypotheses" |
| 44327–44331 | 4.12:eq-above-slot-level-1 | estimate | At n ≥ p curvature is bounded at unit scale and current carries ell-p inverse. | proved conditionally | reblocking-inside-a,b | "then give" |
| 44333–44337 | 4.12:eq-above-slot-level-2 | estimate | Both above-slot target ratios are at most one half. | proved conditionally | above-slot-level-3; gain arithmetic; coupling-thresholds-e,g | "In both cases" |
| 44340–44421 | Proof above the slot level | proof | Substituting the block scale and splitting n ≤ k−1 from n = k proves the half-radius bound. | proved conditionally | running-radii-a; consumer-radii-d,e; gain-arithmetic; coupling-thresholds-e,g,h | "which completes the proof" |
| 44364–44372 | 4.12:eq-above-slot-level-3 | estimate | The ratios reduce to the running-radius ratio times ell-n squared divided by vartheta. | proved conditionally | above-slot-level-1; def-consumer-radii | "therefore gives" |
| 44380–44406 | Theta and lower-level comparison | construction | A supremum of the squared-L gains is bounded by W(N0) and then by the half-radius threshold. | proved conditionally | consumer-radii-d; gain-arithmetic; coupling-thresholds-e,h | "Hence" |
| 44408–44418 | Level-k comparison | proof | Only K4 points on B5 occur at level k and their L0 gain gives the half-radius bound. | proved conditionally | def-consumer-radii observation; consumer-radii-e; coupling-thresholds-g | "By the observation recorded" |
| 44423–44456 | Points below the slot level: direct expansion; 4.12:prf-below-slot-level | lemma | A box-gauge datum yields improved below-slot curvature and current bounds and half-radius ratios. | proved conditionally | Inside hypotheses; axial gauge; averaging and minimiser inputs; Gamma thresholds | "Assume the hypotheses" |
| 44433–44437 | a-max and Kb for direct expansion | definition | The two constants package the running radius and geometric box-gauge factors. | definition | DQ; alpha0,k; cQ; cd; L | "put" |
| 44440–44443 | Below-slot clause (a) | construction | Data V admit a real gauge representation by e-to-ib with pointwise and weighted bounds on b. | proved conditionally | below-slot steps (i)–(iv) | "This completes the proof of (a)" |
| 44444–44452 | Below-slot clause (b) | estimate | Curvature loses one ell-n power and current two in the below-slot case. | proved conditionally | constrained-minimisers-c; perturbed-plaquettes; lattice-configurations-c | "completes the proof of (b)" |
| 44453–44454 | Below-slot clause (c) | estimate | The stated gain ratios hold and are at most one half. | proved conditionally | running-radii-a; gain-arithmetic; coupling-thresholds-f | "This proves (c)" |
| 44458–44754 | Eight-step direct-expansion proof | proof | Global box gauge and expansion at the trivial background establish the three below-slot conclusions. | proved conditionally | Axial gauge; determining sets; constrained minimisers; current and plaquette inputs; thresholds | "proceeds in" |
| 44468–44491 | (i) The box gauge | construction | An axial gauge writes bar-U as an exponential of a uniformly small real one-form. | proved conditionally | lem-axial-gauge; admissible-boxes-a; coupling-thresholds-d | "The lemma provides" |
| 44488–44491 | 4.12:eq-below-slot-level-1 | estimate | The box-gauge one-form is bounded by a-max. | proved conditionally | lem-axial-gauge | "its bound" |
| 44493–44544 | (ii) The data in the box gauge | construction | Averaging and gauge covariance produce b and varsigma and verify admissibility of e-to-ib. | proved conditionally | determining-sets-c,d; coupling-thresholds-d; constrained-minimisers-a,b | "It follows that" |
| 44509–44512 | 4.12:eq-below-slot-level-2 | estimate | Every averaged bond datum is bounded by cQ times a-max times its length. | proved conditionally | determining-sets-d, including interface reading | "It yields" |
| 44546–44571 | (iii) The minimiser in the box gauge | construction | UE is gauge equivalent to the trivial-background exponential response H. | proved conditionally | lem-minimiser-covariance; constrained-minimisers-c | "Hence" |
| 44567–44571 | 4.12:eq-below-slot-level-3 | identity | Gauge transformations leave the relevant plaquette and current norms unchanged. | proved conditionally | not-lattice-configurations; lattice-configurations-b | "Together they give" |
| 44573–44633 | (iv) The size of the weighted datum norm | proof | Splitting bonds by scale and summing separated larger scales bounds the weighted norm at every site. | proved conditionally | below-slot-level-2; constrained-minimisers-d; consumer-radii-a; coupling-thresholds-c | "Adding the two contributions" |
| 44618–44623 | 4.12:eq-below-slot-level-a | estimate | The weighted datum norm is bounded by Kb alpha0,k times the consumer length. | proved conditionally | Scale-separated summation in step (iv) | "we obtain" |
| 44635–44655 | (v) The size of H near xi | estimate | The response and its first and second differential quantities are bounded at the local consumer scale. | proved conditionally | constrained-minimisers-c; reblocking-inside-b; below-slot-level-a | "These give" |
| 44657–44685 | (vi) The plaquette bound | proof | The left-perturbation estimate at the trivial background absorbs the quadratic term into the desired curvature bound. | proved conditionally | lem-perturbed-plaquettes; step (v); coupling-thresholds-d | "So the lemma applies" |
| 44687–44723 | (vii) The current bound | proof | The current estimate applies at ell-n/L and its nonlinear correction is absorbed by smallness. | proved conditionally | lattice-configurations-c; constrained-minimisers-c; coupling-thresholds-d | "completes the proof of (b)" |
| 44725–44754 | (viii) Comparison with the radii | proof | Dividing by the targets and using arithmetic gains gives both half-radius ratios. | proved conditionally | consumer-radii-d; running-radii-a; gain-arithmetic; coupling-thresholds-f,h | "This proves (c)" |
| 44756–44775 | Conclusion and uniformity; 4.12:prf-uniform-constants | lemma | Both slot cases cover all points with uniform constants and half-radius margins subject to the incomplete-step proviso. | proved conditionally | Above/below-slot lemmas; inside proposition proviso; Gamma0–Gamma3; running-radii-b | "subject to this" |
| 44777–44801 | Proof of uniformity | proof | The two slot cases exhaust the domain and the constants have no consumer or level dependence. | proved conditionally | Above/below-slot lemmas; DQ ≤ 204M; coupling thresholds | "except at the step marked" |
| 44803–44826 | Real-factor slot bounds; 4.12:cor-real-factor-slots | corollary | All four composites satisfy the real half of clause (iv) for consumers inside admissible boxes off the core. | proved conditionally | Explicit hypotheses (a),(b); admissible-boxes-b; consumer radii | "Assume the following two statements" |
| 44804–44812 | Real-factor corollary hypotheses (a),(b) | hypothesis | The incomplete inside-box proposition and equality of off-core real factors with bar-U are assumed. | assumed | prop-reblocking-inside; theorem fixing composites; not-admissible-boxes | "Assume the following two statements" |
| 44828–44844 | Proof of real-factor corollary | proof | Equality of real factors transfers the assumed proposition's consumer bounds to every composite. | proved conditionally | Corollary hypotheses (a),(b) | "By hypothesis (a)" |
| 44846–44938 | The minimiser on a refined determining set; 4.12:rem-refined-minimiser | remark | Refinement yields a conditional response identity but the comparison route lacks the required crossing-bond control. | sketched | Composition property; general-base response; B-CMP98 Propositions 6,7; axial gauge | "the route through" |
| 44850–44861 | Source determining set and source minimiser | definition | B-nu has level min(p,t) and U-nu minimises with the source averages on it. | definition | def-determining-sets; def-constrained-minimisers | "be the corresponding constrained minimiser" |
| 44863–44865 | Re-blocked block | definition | A source block is re-blocked when the consumer set subdivides it at a lower level. | definition | B-nu; BE; cE | "we say" |
| 44867–44872 | D1, D2 and re-block datum B-rb | definition | B-rb is the gauge-adjusted difference between refined averages of bar-U and U-nu. | definition | M-B; U-nu; bar-U; gauge v | "is called the" |
| 44874–44875 | Composition under refinement | hypothesis | Coarse averages are taken to be determined by refined averages. | assumed | Averaging maps under refinement | "Grant the composition property" |
| 44876–44878 | 4.12:eq-refined-minimiser-1 | identity | UE is a gauge transform of U-nu twisted by the response to B-rb. | proved conditionally | Granted composition; constrained-minimisers-b(ii); general-base response | "Grant the composition property" |
| 44879–44880 | General-base response H-B(b;U0) | definition | H-B denotes the constrained minimiser's response one-form around a base configuration. | definition | Determining set B; datum b; base U0 | "denotes the response" |
| 44887–44897 | Why the refined identity is unnecessary inside a box | remark | Consumer gains absorb the constants without using the source's sharp radius. | sketched | consumer radii; Gamma1–Gamma3; constrained-minimisers-b,c | "Thus nowhere inside" |
| 44899–44909 | First-order refined-datum requirement | requirement | The comparison needs a gauge making every refined bond discrepancy first order in ell-i. | named open | B-rb; U-nu; level-p block and level-i bonds | "It would require" |
| 44911–44930 | Crossing-bond obstruction | remark | Blockwise estimates only give an ell-p-squared flux on crossing bonds and no small response ratio at low levels. | sketched | B-CMP98 Propositions 6,7; determining-sets-e; axial gauge | "The reason for the second item" |
| 44932–44937 | Global-gauge alternative | remark | The box's global gauge makes the data small enough to expand directly at the trivial background. | proved conditionally | reblocking-inside-c and proviso; constrained-minimisers-c; below-slot lemma | "This is the route taken" |
| 44940–44982 | Proof of refined-minimiser identity | proof | Constraint inclusion gives criticality and a base-response formula yields the identity. | proved conditionally | Granted composition; constrained-minimisers-b(ii); response around a general base | "under refinement, which we grant" |
| 44984–45025 | What re-blocking does not assert; 4.12:rem-reblocking-not-asserted | remark | The real inside-box result excludes core and non-box consumers, complex minimisers, and holomorphy claims. | definition | Inside proposition scope; consumer spaces; composites | "is delimited as follows" |
| 44985–44987 | Re-block region | definition | The re-block region consists of points where the consumer level is below the slot level. | definition | cE; p; X'' | "is the set of points" |
| 44991–45003 | Excluded consumers | remark | Core consumers, mixed K4 domains, and certain old collar or B5 terms receive no inside-box assertion. | named open | Composite construction; not-admissible-boxes; axial gauge | "Nothing is asserted" |
| 45004–45017 | Complex half at the induction base | remark | No result is supplied for complex consumer minimisers or their alpha1,k comparison term at the base of level induction. | named open | Analyticity-space clause (iv); consumer-radii-c | "Nothing is asserted" |
| 45018–45021 | No holomorphy and no source clause-(iv) dependence | remark | The real argument uses only source curvature on admissible boxes and makes no holomorphy assertion. | proved conditionally | admissible-boxes-a; inside proof | "No holomorphy statement is made" |
| 45022–45023 | Existential thresholds | remark | N-star, M-star, and gamma-star have no asserted numerical values. | definition | Inside-box thresholds | "The thresholds" |
| 45027–45083 | Proof of scope and obstruction | proof | Real minimisers explain the scope and the missing box gauge or refined datum prevents extension. | sketched | Inside proposition proviso; consumer-radii-c; axial gauge; B-CMP98 Propositions 6,7 | "describe where" |
| 45047–45052 | Slot-radius consistency | remark | The E4 weakening handles p ≤ n while consumer block scale applies for p > n. | sketched | reblocking-inside-a; consumer-radii-c | "gives the consistency" |
| 45061–45066 | Box required by axial-gauge route | requirement | The route needs a containing healed box with the source curvature radius but may not impose a domain diameter bound. | named open | lem-axial-gauge; admissible-boxes-a; Kb | "such a bound is not admitted" |
| 45068–45080 | Missing outside-box comparison datum | requirement | The alternative needs ell-i times ell-p curvature control across subdivided-block boundaries that the cited inputs do not supply. | named open | B-CMP98 Propositions 6,7; lem-axial-gauge | "the comparison cannot be completed" |
| 45085–45101 | Re-blocking outside admissible boxes; 4.12:prop-reblocking-outside | proposition | The inside proposition's existence and explicit estimates are requested for off-core non-box consumers with nonempty re-block regions. | named open | Inside standing hypotheses; consumer radii; stated geometric assumptions | "Proof outstanding" |
| 45086–45098 | Outside-box hypotheses | hypothesis | The domain avoids the core, fits no healed box of side 204M, and has a nonempty re-block region. | assumed | Inside standing hypotheses without box inclusion | "Assume the following" |
| 45108–45111 | Route to outside-box re-blocking | proof | Either a refined-datum lemma or real-data tower localisation is proposed to extend the inside argument. | sketched | Inside proposition, itself incomplete; proposed alternatives (i),(ii) | "Either of the following two statements would suffice" |
| 45114–45133 | (i) A re-block datum lemma | requirement | Equal level-p averages and curvature bounds should yield gauge-aligned level-j data with first-order length control including crossing bonds. | named open | def-block-average; B-CMP98 Propositions 6–7; B-CMP99a (1.7)–(1.19) | "The statement required is the following" |
| 45124–45126 | 4.12:eq-reblocking-outside-1 | identity | The proposed gauge aligns level-j averages by an exponential datum B. | named open | Proposed re-block datum lemma | "The statement required is the following" |
| 45129–45131 | 4.12:eq-reblocking-outside-2 | estimate | The proposed datum is bounded by C-rb ell-j ell-p times the sum of curvatures. | named open | Proposed re-block datum lemma, including crossing bonds | "the bonds crossing" |
| 45135–45160 | (ii) Tower localisation at real data | requirement | Restricting a real minimiser to an admissible box should change local observables by an exponentially small error. | named open | B-CMP119; B-CMP116 (1.8)–(1.10); cluster localisation; boundary-tower lemma | "The statement required is that" |
| 45143–45150 | 4.12:eq-reblocking-outside-3 | estimate | The full-domain curvature should be bounded by the restricted minimiser's curvature plus a decaying boundary error. | named open | Tower localisation proposal; real averaged datum | "The statement required is that" |
| 45151–45154 | Current version of tower localisation | requirement | An analogous local current estimate is required with the inverse-cube block-scale factor. | named open | Proposed outside-3 analogue | "the analogous" |
| 45154–45157 | Coarse/fine boundary-constraint compatibility | requirement | New restriction-boundary coarse constraints must be compatible with the finer determining set. | named open | B-E(p,X'''); tower-localisation route | "is not proved here" |
| 45162–45175 | Uniqueness and locality; 4.13:lem-minimizer-unique | lemma | Every field admitted by Balaban's Lemma 4 should have a unique minimiser and arbitrary-subdomain nesting. | named open | B-CMP109 Lemma 4, (3.38); B-CMP98 averaging | "Proof outstanding" |
| 45164–45165 | Uniqueness/locality admission hypotheses | hypothesis | Constants and admitted fields are those of Balaban's Lemma 4. | assumed | B-CMP109 Lemma 4 | "let the" |
| 45179–45197 | Route to uniqueness and locality | proof | Orbit uniqueness must be connected to admitted minimisers and averaging locality must imply nesting on arbitrary domains. | sketched | B-CMP102b Theorem 1; B-CMP109 Lemma 4, (3.38); B-CMP98; def-domains | "A proof of (a)" |
| 45185–45187 | Admission-to-curvature bridge | requirement | Every admitted field must meet the curvature and constant-smallness hypotheses of the uniqueness theorem. | named open | B-CMP109 Lemma 4; B-CMP102b Theorem 1 | "would have to establish three things" |
| 45187–45189 | Critical-space bridge | requirement | Every relevant minimiser must be critical in the space where the critical orbit is unique. | named open | B-CMP109 Lemma 4; B-CMP102b Theorem 1 | "would have to establish three things" |
| 45189–45191 | Orbit-to-minimiser bridge | requirement | Unique gauge orbit must imply the precise uniqueness of minimiser used by Lemma 4. | named open | B-CMP109 Lemma 4; B-CMP102b Theorem 1 | "uniqueness of the orbit yields uniqueness" |
| 45192–45197 | Arbitrary-subdomain locality bridge | requirement | Locality from averaging and uniqueness must justify nesting on every Z in Dj. | named open | B-CMP98; B-CMP109 (3.38); 1.5:def-domains | "A proof would have to extract" |
| 45199–45201 | One-power hereditary-class input | hypothesis | The hereditary-class statement uses both uniqueness and locality through arbitrary-subdomain nesting. | assumed | 4.13:lem-minimizer-unique; B-CMP109 (3.38) | "The lemma is an input" |
| 45203–45224 | Own-curvature gauge condition reproduced by one step; 4.13:lem-own-constant | lemma | Printed small and real-background pairs should obey the widened gauge bound at their own curvature constant and retain it after one step. | named open | B-CMP109 (1.12), §§3–5; B-CMP116 §§1–2; widened reading | "Proof outstanding" |
| 45205–45217 | B, c-square, admitted pairs, alpha0-prime | definition | The constants and pair classes are taken from the printed gauge condition, widened reading, and published membership. | definition | B-CMP109; B-CMP116; chapter's widened reading | "let" |
| 45219–45223 | Own-constant bound and reproduction | requirement | Every cube up to c-square LM must satisfy the single gauge bound c-square LMB alpha0-prime throughout one step. | named open | Printed small and real-background pairs | "Proof outstanding" |
| 45228–45234 | Route to own-constant lemma | proof | The own-curvature estimate and its one-step preservation are to be derived together with the thin-cube gradient bound. | sketched | Chapter's thin-cube gradient bound; B-CMP109 §§3–5; B-CMP116 §§1–2 | "A proof would have to establish two things" |
| 45236–45237 | Levels, territories, covers and the form at free current; 4.14:not-free-current-notation | definition | The next definition is introduced but none of its content is present in this chunk. | definition | Content continues beyond chunk | "Levels, territories, covers and the form at free current" |

## Forward and backward references

Each entry gives the reference location in this chunk and its target. Repeated references are retained by location; references to results proved earlier or later within this same chunk are included. Bibliographic keys are recorded as printed, without consulting other files.

- 43960: `4.12:eq-perturbed-plaquettes-4`, used to bound Sigma.
- 43991: `4.12:eq-perturbed-plaquettes-3`, identifies the perturbed plaquette product (before this chunk).
- 43993–43994: `4.12:eq-perturbed-plaquettes-6`, `-5`, and the conclusion `-1` (the last precedes this chunk).
- 43998–44001: `4.12:def-determining-sets`, `4.12:eq-determining-sets-a`, `4.12:def-constrained-minimisers`, `4.12:eq-constrained-minimisers-b`, defining sets and minimiser hypotheses.
- 44012–44014: `4.12:eq-constrained-minimisers-a`, conjugation-invariant admissibility condition.
- 44017–44019 and 44023–44024: `4.12:eq-determining-sets-c`, averaging covariance, used in both directions.
- 44050–44051: `4.12:eq-constrained-minimisers-b` clause (i), minimiser curvature bound and its constants.
- 44053–44055: `4.12:eq-constrained-minimisers-b` clause (ii) and `4.12:eq-minimiser-covariance-1`, critical-orbit uniqueness application.
- 44103–44104: `4.12:eq-gain-arithmetic-1`, proved by the decreasing sequence argument.
- 44123–44124: `4.12:eq-gain-arithmetic-2`, proved by monotonicity.
- 44133–44136: `4.12:not-admissible-boxes` and the unnamed theorem constructing the source space fix two standing conditions; `4.12:def-coupling-thresholds` supplies Phi0–Phi2.
- 44142–44146: `B-CMP122a` relates N0 to running couplings; `4.12:def-coupling-thresholds` establishes Gamma0–Gamma3.
- 44149–44152: `4.12:not-admissible-boxes` defines the source point, real factor, admissible box and core.
- 44153 and 44157–44159: `4.12:def-consumer-radii` defines K1–K5, slot levels and read subdomains; `4.12:def-determining-sets` defines BE.
- 44160–44163: `4.12:def-constrained-minimisers`, definition of UE.
- 44167–44169: `B-CMP102b`, Theorem 1, as `4.12:eq-constrained-minimisers-b`, supplies existence.
- 44194–44195: `4.12:def-consumer-radii`, real derived-slot targets.
- 44199–44201: Forward reference to the later construction of b in the proof of `4.12:prop-reblocking-inside` (44503–44514).
- 44228–44233: `4.12:eq-admissible-boxes-a`, the source's real curvature bound.
- 44235–44236: `4.12:eq-determining-sets-e` and `4.12:eq-coupling-thresholds-d` condition (i), admissible averaging estimate.
- 44247–44255: `4.12:eq-constrained-minimisers-a` reads `B-CMP102b` (7); `4.12:eq-reblocking-inside-1` verifies it; `4.12:eq-coupling-thresholds-d` condition (ii) verifies smallness; `4.12:eq-constrained-minimisers-b` clause (i) is `B-CMP102b` Theorem 1.
- 44272–44283: `4.12:eq-consumer-radii-b`, `4.12:eq-coupling-thresholds-b` (Phi1), and `4.12:eq-determining-sets-b,a`, supply interior depth and the block level.
- 44286–44288: `4.12:eq-determining-sets-a`, neighboring block levels differ by at most one.
- 44305–44307: `4.12:eq-reblocking-inside-a,b` are inputs to clauses (b),(c) and to `-c,d`, to be derived below.
- 44311–44317: `4.12:prop-reblocking-inside` clause (c), consumer space DE clause (iv), and the source-space construction of W1–W4, whose real factors equal bar-U off the core.
- 44321–44324: `4.12:prop-reblocking-inside`, its hypotheses, incomplete-step proviso, and minimiser existence clause (a).
- 44342–44343: `4.12:eq-reblocking-inside-a,b` from that proposition.
- 44350–44351: `4.12:eq-above-slot-level-1` identified with the n ≥ p part of inside clause (b).
- 44353–44359: `4.12:def-consumer-radii`, target formulas.
- 44363: `4.12:eq-above-slot-level-1`, divided by those targets.
- 44373–44376: `4.12:eq-running-radii-a` in `4.12:not-running-radii`, running-radius ratio.
- 44377 and 44386: `4.12:eq-above-slot-level-3`, common upper-bound comparison.
- 44381–44382: `4.12:eq-consumer-radii-d` in `4.12:def-consumer-radii`, lower bound on vartheta.
- 44389–44396: `4.12:lem-gain-arithmetic`, two bounds for f2.
- 44398–44401: `4.12:eq-coupling-thresholds-h` defines W; `4.12:eq-coupling-thresholds-e` in `4.12:def-coupling-thresholds` supplies the half-radius smallness condition.
- 44406: `4.12:eq-above-slot-level-2`, concluded in the lower-level case.
- 44408–44413: Observation with `4.12:def-consumer-radii` restricts level-k points to K4 on B5; `4.12:eq-consumer-radii-e` supplies their gain.
- 44415–44418: `4.12:eq-above-slot-level-3` and `4.12:eq-coupling-thresholds-g` in `4.12:def-coupling-thresholds`, finish the level-k case.
- 44420: `4.12:eq-above-slot-level-2`, final conclusion.
- 44424–44428: `4.12:prop-reblocking-inside`, hypotheses and data for the below-slot lemma.
- 44442–44443: `4.12:eq-reblocking-inside-c` and forward reference to `4.12:eq-below-slot-level-a`, datum bounds.
- 44453–44454: `4.12:eq-reblocking-inside-d`, ratios to be proved.
- 44459–44465: Recall of eta, ell-m and cE(x0) ≤ n; no explicit external label is supplied.
- 44468–44470: `4.12:lem-axial-gauge`, invoked with the box's diameter and curvature radius.
- 44472–44477: `4.12:eq-admissible-boxes-a` and `4.12:eq-coupling-thresholds-d`, axial-gauge hypotheses.
- 44495–44500: `4.12:eq-determining-sets-c`, covariance of averaging.
- 44503–44506: `4.12:eq-determining-sets-d`, including interface-bond reading in `4.12:def-determining-sets`; `4.12:eq-coupling-thresholds-d` makes it applicable.
- 44513: `4.12:eq-reblocking-inside-c`, identified with the datum bound just obtained.
- 44516–44520: `4.12:def-consumer-radii` bounds slot levels by k; `4.12:eq-below-slot-level-2` and `4.12:eq-coupling-thresholds-d` give sup-norm smallness.
- 44537–44538: `4.12:eq-coupling-thresholds-d`, the one-tenth bound.
- 44540–44544: `4.12:eq-constrained-minimisers-a,b` and `4.12:eq-coupling-thresholds-d`, admissibility of e-to-ib.
- 44546–44548: `4.12:lem-minimiser-covariance`, identifies gauge-related minimisers.
- 44554–44561: `4.12:eq-constrained-minimisers-c,b`, response representation and its hypotheses; step (ii) has checked them.
- 44564–44566: `4.12:not-lattice-configurations` and `4.12:eq-lattice-configurations-b`, plaquette invariance and current covariance.
- 44579–44581: `4.12:eq-below-slot-level-2` and `4.12:eq-constrained-minimisers-d`, small-bond contribution.
- 44588–44593: `4.12:def-consumer-radii`, cited here for construction of BE and its boundary tower.
- 44595–44597: `4.12:eq-consumer-radii-a`, separation across scales.
- 44602–44604: `4.12:eq-below-slot-level-2` and `4.12:eq-constrained-minimisers-d`, large-bond summation.
- 44614: `4.12:eq-coupling-thresholds-c`, convergence of the geometric series.
- 44632–44633: `4.12:eq-below-slot-level-a`, extended to every site and completing clause (a).
- 44635–44644: `4.12:eq-constrained-minimisers-c`, `4.12:eq-reblocking-inside-b`, and `4.12:eq-below-slot-level-a`, the three response-bound inputs.
- 44657–44659: `4.12:lem-perturbed-plaquettes`, applied at the trivial background.
- 44662–44665: Step (v) and `4.12:eq-coupling-thresholds-d`, verify perturbation smallness.
- 44667–44668: Step (v) supplies the derivative bound.
- 44681–44685: `4.12:eq-coupling-thresholds-d`, `4.12:eq-below-slot-level-3`, and inside proposition clause (b), identify the curvature conclusion.
- 44687–44690: `4.12:eq-lattice-configurations-c`, the imported current bound.
- 44698–44705: `4.12:eq-below-slot-level-a`, `4.12:eq-coupling-thresholds-d`, and `4.12:eq-constrained-minimisers-c`, verify its hypotheses.
- 44718–44722: `4.12:eq-coupling-thresholds-d`, `4.12:eq-below-slot-level-3`, and inside proposition clause (b), identify the current conclusion.
- 44725–44727: `4.12:def-consumer-radii` and steps (vi),(vii), targets and established bounds.
- 44736–44738: `4.12:eq-running-radii-a` yields `4.12:eq-reblocking-inside-d`.
- 44742–44744: `4.12:eq-consumer-radii-d` and `4.12:lem-gain-arithmetic`, radius and gain inputs.
- 44747–44753: `4.12:eq-coupling-thresholds-h,f`, W and the half-radius inequality.
- 44757–44769: `4.12:prop-reblocking-inside`, with its explicit incomplete-step proviso, clauses (b),(c), and constants from its inputs.
- 44771–44774: `4.12:def-coupling-thresholds` Gamma0–Gamma3 and `4.12:eq-running-radii-b`, uniform level control.
- 44782–44788: `4.12:prf-above-slot-level` and `4.12:prf-below-slot-level`, exhaustive cases.
- 44797–44800: `4.12:def-coupling-thresholds`, `4.12:eq-running-radii-b`, and `4.12:prop-reblocking-inside`, conclusion with the unresolved step retained.
- 44806–44812: `4.12:prop-reblocking-inside` is expressly assumed; the unnamed theorem fixing W1–W4 and their consumers supplies the real-factor assumption; source datum is from `4.12:not-admissible-boxes`.
- 44814–44818: `4.12:def-consumer-radii`, `4.12:not-admissible-boxes`, and `4.12:eq-admissible-boxes-b`, include all consumers in Z''k off the core even at the cut band.
- 44824–44825: Composite construction identifies U2 on the core; no explicit label is given.
- 44830–44831: Corollary hypothesis (b), off-core real factor.
- 44833–44843: `4.12:prop-reblocking-inside` is used through corollary hypothesis (a) to establish DE clause (iv)'s real half.
- 44847–44850: `4.12:prop-reblocking-inside` and `4.12:def-consumer-radii`, refined-minimiser setup.
- 44855 and 44859: `4.12:def-determining-sets` and `4.12:def-constrained-minimisers`, B-nu and U-nu.
- 44874–44882: The composition property under refinement is granted without a cited source; the general-base response notation is explained locally.
- 44884–44885: `4.12:eq-refined-minimiser-1` is explicitly not used in `4.12:prop-reblocking-inside`.
- 44889–44895: `4.12:def-consumer-radii`, Gamma1–Gamma3, and `4.12:eq-constrained-minimisers-b,c`, explain the available gains.
- 44899–44909: `4.12:eq-refined-minimiser-1`, comparison route requiring a stronger datum bound.
- 44911–44914: `B-CMP98`, Propositions 6,7 (sup-norm form), `4.12:eq-determining-sets-e`, and `4.12:lem-axial-gauge`, proposed blockwise tools.
- 44932–44937: `4.12:eq-reblocking-inside-c` of the incomplete `4.12:prop-reblocking-inside`, `4.12:eq-constrained-minimisers-c`, and `4.12:prf-below-slot-level`, global-gauge alternative.
- 44940–44941: `4.12:eq-refined-minimiser-1`, identity whose proof follows.
- 44943–44945: Local definition of D2 supplies refined admissibility.
- 44947–44962: Criticality of U-nu on its original constraint manifold is used; composition under refinement is again explicitly granted.
- 44962–44967: `4.12:eq-constrained-minimisers-b` clause (ii), gauge identification of the refined minimiser.
- 44969–44981: The general-base constrained-minimiser response statement is invoked without a bibliographic or equation label to obtain `4.12:eq-refined-minimiser-1`.
- 44985–44989: `4.12:def-consumer-radii` and the incomplete `4.12:prop-reblocking-inside`, scope setup.
- 44991–44996: Construction of composites gives U2 on the core; `4.12:not-admissible-boxes` defines the admissible boxes.
- 45002–45003: `4.12:lem-axial-gauge`, unavailable for the excluded consumers.
- 45004–45017: Analyticity-space clause (iv), explicitly distinguished from Theorem 0 clause (iv); `4.12:prop-reblocking-inside` and `4.12:def-consumer-radii`, especially `4.12:eq-consumer-radii-c`, concern the real half only.
- 45019–45021: Source clause (iv) is not used; only `4.12:eq-admissible-boxes-a` is used.
- 45028–45034: Items (3),(4),(2),(1) of the preceding remark, scope of the ensuing justification.
- 45036–45040: `4.12:eq-admissible-boxes-a` and incomplete `4.12:prop-reblocking-inside`, independence from source clause (iv).
- 45042–45050: `4.12:prop-reblocking-inside`, `4.12:eq-reblocking-inside-a`, and `4.12:eq-consumer-radii-c`, slot-radius consistency.
- 45054–45062: Item (1), `4.12:prop-reblocking-inside`, `4.12:lem-axial-gauge`, and `4.12:eq-admissible-boxes-a`, the missing containing-box step.
- 45074–45080: `B-CMP98`, Propositions 6,7 in sup norm, and `4.12:lem-axial-gauge`, insufficient crossing-bond estimates.
- 45082: Forward reference to the two proposed lemmas below, re-block datum and tower localisation (45114–45160).
- 45086–45100: `4.12:prop-reblocking-inside` supplies standing assumptions and target conclusions (a),(b), while `4.12:def-consumer-radii` supplies the consumers.
- 45103–45104: `4.12:rem-reblocking-not-asserted`, examples of outside-box consumers.
- 45108–45111: `4.12:prop-reblocking-inside`, the incomplete argument proposed for extension by either ensuing requirement.
- 45114–45115: `1.5:def-block-average`, Balaban's level-m map.
- 45132–45133: `B-CMP98`, Propositions 6–7, and `B-CMP99a` (1.7)–(1.19), proposed discrete Coulomb-gauge inputs.
- 45138–45140: `4.12:prop-reblocking-inside`, real datum bar-U and determining-set averages.
- 45157–45159: `B-CMP119` tower analysis; `B-CMP116` (1.8)–(1.10); an unnamed localisation lemma for its cluster expansions; an unnamed boundary-tower lemma, proposed tower-localisation inputs.
- 45162–45169: `B-CMP109`, Lemma 4, the published constrained problem, its restrictions, and admitted fields.
- 45170–45173: `B-CMP98` averaging operations and `B-CMP109` (3.38), requested locality and arbitrary-subdomain nesting.
- 45179–45191: `B-CMP102b`, Theorem 1, provides minimal-orbit and critical-orbit statements; `B-CMP109`, Lemma 4, is the target application for three missing bridges.
- 45192–45197: `B-CMP98`, `B-CMP109` (3.38) and Lemma 4, and `1.5:def-domains`, requested locality for arbitrary Z in Dj.
- 45199–45201: Forward reference to the unnamed one-power hereditary-class statement, which assumes this lemma through `B-CMP109` (3.38).
- 45205–45207: `B-CMP109` (1.12) and the chapter's unnamed definition of its widened reading, constants B and c-square.
- 45209–45217: `B-CMP109` §§3–5 and `B-CMP116` §§1–2, one-step analysis and printed membership of small and real-background pairs.
- 45219–45223: `B-CMP109` (1.12), required own-constant gauge bound; `B-CMP109` §§3–5 and `B-CMP116` §§1–2, one-step reproduction target.
- 45229–45234: The chapter's thin-cube gradient bound, `B-CMP109` (1.12), §§3–5, and `B-CMP116` §§1–2, proposed joint derivation.
- 45236–45237: `4.14:not-free-current-notation` begins; its defining content is beyond the chunk.

## Obligations named here

- 44127–44129, 44321–44322, 44757–44759, 44799–44800: The inside-box re-blocking proposition retains a proof gap at the step marked $(\ast)$; the step itself is not identified in this excerpt.
- 44130–44147: Impose the two source-space standing conditions, floors Phi0–Phi2, and N0 ≥ N-star (equivalently sufficiently small running couplings), activating Gamma0–Gamma3.
- 44153–44158: The inside-box assertion requires a consumer domain contained in the admissible box off the core and a subdomain read at its slot level.
- 44311–44317: The real half of consumer space clause (iv) requires the two target bounds; this is the claimed use of inside clause (c).
- 44804–44812: The real-factor corollary explicitly assumes both the incomplete inside proposition's conclusion and equality of the four off-core real factors with bar-U.
- 44824–44825, 44991–45003: Core consumers and consumers not contained in an admissible box remain outside the asserted result, including mixed K4 domains and old collar/B5 terms reading higher slots.
- 44874–44875, 44949–44953: Composition of averages under refinement is granted for the refined-minimiser identity.
- 44899–44909: The refined comparison requires a first-order ell-i bound on B-rb on every refined bond and a gauge producing that order of discrepancy.
- 44916–44930: Crossing bonds only receive an ell-p-squared curvature estimate from the proposed blockwise tools, leaving an uncontrolled low-level response ratio.
- 44932–44934, 44834–44835, 44988–44989, 45014–45015, 45038–45039, 45042–45043, 45057–45058: Uses of inside re-blocking continue to carry its explicit incomplete-step qualification.
- 45004–45013: The complex half of consumer clause (iv) at the induction base, including the alpha1,k comparison term, is not asserted.
- 45018: No holomorphy statement is made; the source also says none is needed here.
- 45022–45023: No numerical thresholds are supplied; N-star, M-star and gamma-star are only existential.
- 45061–45066: The axial-gauge extension needs a containing box with the source curvature radius; its existence is unavailable and a diameter bound on the consumer domain is not admitted.
- 45068–45080: The outside comparison requires a re-blocking datum of order ell-i times ell-p alpha0,k and further terms, including on crossing bonds; the named inputs do not establish it.
- 45085–45106: The outside-box re-blocking proposition has an outstanding proof.
- 45090–45098: That proposition assumes an off-core domain fitting no healed box of side 204M and a nonempty re-block region for the chosen pair.
- 45114–45133: The proposed re-block datum lemma must produce the gauge relation and C-rb ell-j ell-p (F1+F2) bound on all level-j bonds, including those crossing the block boundary.
- 45135–45150: The proposed real-data tower-localisation lemma must prove the curvature comparison with an exponentially decaying boundary error.
- 45151–45154: The same route requires the analogous current comparison with inverse-cube block scale.
- 45154–45157: Compatibility of coarse constraints across the new boundary with the finer determining-set constraints must be proved and is expressly not proved here.
- 45158–45159: The tower route names a cluster-expansion localisation lemma and a boundary-tower lemma among its inputs, without proving either here.
- 45162–45177: Uniqueness and locality completing Balaban's Lemma 4 have outstanding proofs.
- 45185–45187: Every field admitted by B-CMP109 Lemma 4 must be shown to meet B-CMP102b Theorem 1's curvature and smallness hypotheses.
- 45187–45189: Every minimiser in that application must be shown to be a critical point in the theorem's critical-orbit uniqueness space.
- 45189–45191: Gauge-orbit uniqueness must be converted to the minimiser uniqueness used by B-CMP109 Lemma 4.
- 45192–45197: Locality must be extracted from B-CMP98 and combined with uniqueness to prove B-CMP109 (3.38) for arbitrary Z in Dj.
- 45199–45201: The one-power hereditary-class statement takes both parts of this still-outstanding lemma as an input.
- 45203–45226: The own-curvature gauge-condition lemma and its one-step reproduction have outstanding proofs.
- 45229–45234: Together with the thin-cube gradient bound, prove the widened own-constant gauge condition for all printed small and real-background pairs and prove its preservation under one step.

## For the stage question

The chunk contains no explicit analytic-ball radius statement and no explicit statement about “drop-outs” or “prepared shells.” It does contain the following domain, admission, minimiser, old-term, shell, and one-step statements; the entries preserve their scope rather than extending real results to complex backgrounds.

| Lines | Statement relevant to stages, domains or admission | Status here |
|---|---|---|
| 43997–44065 | Gauge transformation preserves admissibility of constrained-minimiser data and gives a gauge-equivalent real minimiser, using the previously stated minimiser hypotheses. | proved conditionally |
| 44130–44164 | At step k, the source point lies in the complex-named source space, but the minimiser considered uses its G-valued factor bar-U and each consumer's own determining set. | definition |
| 44167–44195, 44220–44308 | Real consumer minimisers inside an admissible box off the core are constructed from averaged bar-U and estimated at each slot p; the overall proposition retains its incomplete-step proviso. | proved conditionally |
| 44310–44318 | For all four composites, equality of their off-core real factor with bar-U transfers inside clause (c) to the real half of consumer space clause (iv). | proved conditionally |
| 44320–44421 | At consumer level n ≥ p, the minimiser's real derived slots fit with a factor-one-half margin under the named thresholds. | proved conditionally |
| 44408–44418 | Level-k points inside the box occur only for K4 consumers on B5, whose extra gain supplies the radius comparison. | proved conditionally |
| 44423–44754 | At n < p, a global box gauge permits direct minimiser expansion at the trivial background and gives half-radius real-slot bounds. | proved conditionally |
| 44516–44520, 44693–44695 | Slot levels are at most k and consumer levels at least one, as used to verify response/current hypotheses. | assumed |
| 44540–44562 | The exponential datum e-to-ib satisfies the minimiser admission hypotheses and admits a real response about the trivial background; gauge covariance transfers this to UE. | proved conditionally |
| 44756–44801 | The estimates' constants are independent of k, consumer, slot, and subdomain; k enters through N0(k) and the running radius controlled by Gamma0–Gamma3. | proved conditionally |
| 44803–44825 | Assuming the incomplete proposition and real-factor equality, all four composites satisfy only the real half of clause (iv) off the core, including consumers in Z''k meeting the cut band; on the core their real factor is U2 and the corollary does not cover them. | proved conditionally |
| 44850–44865 | The source minimiser uses blocks of level min(p,t), while the consumer determining set refines them wherever cE is smaller. | definition |
| 44867–44882, 44940–44982 | Given composition under refinement, the consumer minimiser is a gauge-adjusted response around the source minimiser U-nu to the re-block datum. | proved conditionally |
| 44887–44897 | Inside an admissible box the larger consumer radii absorb constants, so the source's sharp radius and the refined-base identity are unnecessary. | sketched |
| 44899–44930 | Comparison around the source minimiser fails to close with the named blockwise tools because crossing-bond errors yield no small ratio at low-level shell points when p is near k. | named open |
| 44932–44937 | The global box gauge instead makes the data themselves small enough for the trivial-background response, subject to the inside proposition's proviso. | proved conditionally |
| 44985–44987 | A pair's re-block region consists precisely of points with consumer level below slot p. | definition |
| 44991–45003 | No assertion covers consumers meeting the core, K4 domains meeting both Z''k and the old region, or old B(j), R(j), E(j) terms with k0 < j < k on cleaned collars or B5 reading slots p > o(x). | named open |
| 45004–45013 | At the base of induction over levels, no assertion establishes the complex half of consumer clause (iv), namely the minimisers of the complex composite averages; the alpha1,k term in comparison with the source minimiser belongs to this unaddressed half. | named open |
| 45014–45017 | The real-half bounds are stated to be consistent with consumer radii at every slot level p, subject to incomplete re-blocking. | proved conditionally |
| 45018, 45031–45034 | No holomorphy is asserted or needed for the argument about real constrained minimisers at source points. | definition |
| 45019–45021, 45036–45040 | The real argument does not use source clause (iv) along source determining sets; it uses only the admissible-box curvature bound. | proved conditionally |
| 45047–45052 | The E4 slot weakens by L to the positive part of n−p at p ≤ n, whereas for p > n the determining scale is the consumer scale. | sketched |
| 45054–45066 | Outside admissible boxes the needed global gauge is unavailable and bounding the consumer domain diameter is expressly not admitted. | named open |
| 45068–45080 | Comparing with the source minimiser on low-level shells would need first-order refined data across adjacent subdivided source blocks, which the named inputs do not supply. | named open |
| 45085–45111 | Re-blocking for off-core consumers not fitting a bounded healed box, with a nonempty re-block region, is an outstanding proposition. | named open |
| 45114–45133 | A proposed real-field lemma would compare lower-level averages of two configurations with identical level-p averages, including crossing bonds. | named open |
| 45135–45159 | Real-data tower localisation would compare full and box-restricted consumer minimisers; compatibility of coarse and finer constraints at the new boundary is expressly unproved. | named open |
| 45162–45175 | Uniqueness is requested at every field admitted by B-CMP109 Lemma 4, and locality must permit nesting on arbitrary subdomains. | named open |
| 45179–45191 | The admission bridge must place every admitted field within the curvature theorem's hypotheses, every minimiser in its unique-critical-orbit space, and then turn orbit uniqueness into the required minimiser uniqueness. | named open |
| 45192–45201 | Arbitrary-domain nesting must be derived from locality and uniqueness; both are inputs to the later one-power hereditary-class statement. | named open |
| 45203–45224 | Small pairs and real-background pairs whose class membership is printed in the cited one-step analyses must satisfy the widened gauge condition at their own printed curvature constant, and that property must reproduce under one renormalisation step. | named open |
| 45228–45234 | The proposed proof jointly develops the thin-cube gradient bound, verifies admission at the own-curvature gauge constant, and establishes one-step preservation. | sketched |
| 45236–45237 | The heading for levels, territories, covers, and the form at free current begins, but supplies no stage definitions within this chunk. | definition |
