# PR8010 independent source review

Frozen original f29251ea68ba2bcd96c807881eae7bc8c6cfd48e; current-main candidate at 5deabeb698a27c2c3f68c5df685af2521ef15307. Review in progress. No verdict yet.

Complete changed notes and runners read. Conditional multiplier proof and Gaussian sandwich spectral constants are undergoing independent reconstruction; transitive analytic input closure remains under inspection.

## Finding 8010-1 — resolved in the original reviewer session

The initial source-only proposal dropped every historical native-wall diagnostic file while the note said the frozen preregistration and pre-run correction were preserved. Its short canonical cache omitted the 21 numerical rows. This was a preservation defect, not a counterexample to the theorem.

The coordinator restored all seven native-wall-check files byte-for-byte under `docs/work_history/repo/review_feedback/pr8010-native-wall/`, added a historical-provenance README, and replaced the note's missing-pack assertion with a live archive link. I inspected the final note, README, historical source, preregistration/correction, full result and source receipt. Historical SHA values remain unchanged and are explicitly not current execution or audit authority. The issue is resolved.

## Independent mathematical reconstruction

**Divided multiplier.** The target is uniform over all actual shifted dominant labels, for every real beta at least 2048. The finite alternant is smooth on the full plane and vanishes on all three reflection lines. Factoring two coordinate zeros by FTC gives F=xyB; B(x,-x)=0, including the origin by continuity. Integrating its y derivative gives the extra (x+y) and factor 1/2, precisely H=xy(x+y)/2. Dual Weyl coordinate-square bounds give the derivative bound16 a^(3/2)/sqrt3. The six-image average therefore controls |Delta A/H|/6 by5a^3 before any endpoint-independent estimate is divided by H.

Torus averaging applies to actual integral shifted labels, not arbitrary real endpoint extensions. The periodic object is the complete alternant Delta B, and the dual Weyl maps are integral unimodular torus automorphisms. The low ellipse is invariant and stays within the chosen square, so low and complementary exact terms can be averaged separately. Gaussian comparison terms use whole-plane linear changes of variables. These facts remove the otherwise serious torus-boundary concern.

The parent PN terms arise by multiplying the sinc/product and exponential remainders: the cubic coefficient is exactly1/810+1/1440+1/144=23/2592. The extra a^3 gives radial powers5,6,7; direct independent radial integration agrees with the exact primary rational value. Both high tails fit within the actual remaining margin below21201. The denominator subtraction is rN+D0 P2 E/beta²-rD(E+P2 E/beta). D0>14, D/D0>.999 and |P2 E|<4 produce the claimed ceiling1710. At the origin d=1 and H(x)=beta^-3/2; the failed old29/H estimate is accurately described as only29/sqrt(beta). It is not used in this proof.

**Gaussian spectrum.** The coordinate transformation has Jacobian2/sqrt3 and sends the heat generator to Delta/4; hence the unitary kernel prefactor is1/pi. Direct independent real integrals on Hermite degrees0–6 at three endpoints confirm the one-dimensional eigenvalues theta^(n+1/2). Analytically, the complete Hermite basis separates in the plane; the odd extension to the pi/3 wedge has normalization1/sqrt6. Its angular sine modes3k and radial Laguerre degree2n give the complete spectrum theta^(3k+2n+1), with simple degrees3 and5 and no degree4. There is no factor6 eigenvalue multiplier.

Multiplication by sqrt(w), followed by heat time1/2, maps the B eigenfunctions to H exp(-2Q/sqrt5) and H(4-4Q/sqrt5) exp(-2Q/sqrt5), rather than carrying the old radial polynomial through unchanged. Independent quadrature of q³ exp(-sqrt5 q) with the two Laguerre weights yields means4/sqrt5,6/sqrt5 and second moments4,10. Applying the radial differential operator qF''+4F' and integrating its square gives heat norms4,10. Combining multiplier and heat terms yields k0=5-7/sqrt5, k1=8-21/(2sqrt5), and positive relative ratio coefficient3-7/(2sqrt5).

**Discrete assembly and proof-input closure.** I read the actual parent multiplier, killed heat and full-top analytic arguments. The full-top input is used for quadrature/quasimode and isolation machinery, not its different H-weighted Perron coefficient or its discrete-heat-insertion dependency. With w=exp(-Q), the quadrature product has two wall zeros, sufficient for f(0)=f'(0)=0 in both coordinates. Smooth Gaussian derivative envelopes control the fourth derivatives and corners, giving O(h4) sampled eigenvector and norm errors. General two-sided weighted heat bound(D), rather than the parent's specialized sqrt(W) estimate(E), applies because the Gaussian sampled mass is bounded. Qualitative compact convergence identifies both isolated branches. The uniform multiplier error remains O(h4) after contraction by the two discrete heat factors; first-order perturbation then gives only the stated o(h²) remainder. No forbidden step-function operator O(h²) expansion is needed.

The transitive SU3 recurrence source's section6 supplies the exact six-neighbor multiplication law and boundary omissions. The original reflection source gives the image signs, rho shift, Fourier beta powers and compact-sandwich limiting mechanism. Schur contraction supplies c/d; the earlier finite B4 note is not alone treated as an infinite-label theorem. The Wilson positivity note section4 also supplies the all-irrep normalization. None of these inputs identifies a multi-link physical transfer with the supplied one-link sandwich.

## Execution and adversarial controls

- Canonical spectral certificate:19 checks, about0.32seconds,64.2MiB.
- Canonical divided certificate:45 checks, about0.22seconds,63.3MiB.
- Canonical origin helper:47 checks on21rows, about8.38seconds,116.0MiB.
- Independent verification:30 direct-integral/symbolic/arithmetic checks, plus exact25x25 agreement between the helper action and a separately enumerated six-neighbor matrix, all21 row formulas, and symbolic ratio-subtraction identity.
- Ten primary mutants were rejected: Mehler branch, quartic/linear multiplier coefficient, heat exponent, heat normalization, angular degree, reflection sign, alternant sign, orbit factor and final ceiling.

The helper's box tail follows the coordinate MGF rate2beta/3 and maximal Chernoff bound. Added killing only lowers kernel entries. Writing infinite numerator/return as a+u,b+v gives difference (bu-av)/(b(b+v)), bounded by epsilon/b+a epsilon/b², divided by the exact dimension. No numerator<=return premise is used. Floating matrix exponentials and tail evaluations remain diagnostic, not interval proofs; the analytical theorem does not rely on their acceptance.

All three new runners are standalone: only ordinary Python/scientific libraries and their own source bytes are read. Source/cache hashes match. Historical result values are evidence provenance, not runtime inputs. Full command outputs and hashes are in `check8010/` and the companion JSON.

## Lens dispositions

- **CodeRunnerReviewer:** PASS for the stated finite symbolic/diagnostic scope. Independent checks above inspect signs, factors, moments, generator and normalization, rather than treating stdout PASS as mathematics.
- **PhysicsClaimReviewer:** PASS; both notes remain conditional-support proposals. No physical multi-link gap, finite-beta spectral onset or framework-derived Wilson action is asserted.
- **ProofObligationReviewer:** CONDITIONAL. All new analytic steps close under the explicit supplied model and identified mathematical lemmas. No target-equivalent unresolved lemma is disguised as progress.
- **ImportSupportReviewer:** PASS. Wilson SU3 action, normalized Haar, Dirichlet chamber and sandwich are explicit model/normalization conditions. Parent analytic results remain conditional mathematical source inputs. No fitted, observational, PDG or state-dependent value enters.
- **NatureRetentionReviewer:** BOUNDED conditional-support. This review grants no retained/audit status.
- **LabelingConventionReviewer:** PASS; genuine algebraic propositions, not naming conventions.
- **RepoGovernanceReviewer:** PASS for source scope. Both tooling changes add only the original helper mapping and preserve every current-main entry. I inspected their consumers: the entry exposes an existing sibling helper to packet inspection and does not execute it or supply a verdict. Stale generated citation manifest and historical status outputs are excluded from authority.
- **NoGoDisciplineReviewer:** Scope-checked using current no-go skill. This is not a no-go submission: heavy five-family packet NOT PASS is explicitly not represented as PASS. N1 only actual divided/spectral routes are claimed; N2 no independent wall count; N3 model imports explicit; N4 failed29/H residual is exact; N5 finite diagnostics do not cover physical lattice-wide conclusions; N6 no new axiom claimed necessary; N7 alternate physical models and quantitative spectral improvements remain unclosed; N8 the parent's fixed-embedding failure does not obstruct the successful eigenvalue route. No universal negative conclusion is approved.

## Frozen final source verdict

Original head: f29251ea68ba2bcd96c807881eae7bc8c6cfd48e.
Confirmation base:5deabeb698a27c2c3f68c5df685af2521ef15307.
Reviewed staged tree:9813ed85a685c93fafc16c564a1108cfcda5c0cd.
Reviewer session:/root/backlog_topology, unchanged through finding and correction confirmation.

The JSON maps all85 original constituent paths,18 final paths, claims, final blob/hash identities and consumed proof-input hashes. No original source claim is silently dropped: canonical mathematical bodies survive; unique diagnostic provenance is relocated; duplicate/historical planning and validation records are explicitly superseded with frozen Git recovery pointers. The stale generated manifest is rejected as authority.

The coordinator must still apply exact-current-main preservation/interaction checks, original-head provenance and the combined integration gates. No full pipeline or audit worker was run by this reviewer.

FINAL VERDICT: PASS
