---
claim_id: scale_ladder_gravity_orthoscheme_zero_action_curvature_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Finite supplied-model numerical fixtures and explicitly stated constructive identities only; all universal, asymptotic, physical and unexecuted census claims are deferred."
runner: scripts/scale_ladder_gravity_orthoscheme_zero_action_curvature_2026_10_18.py
---

# Constructive carrier geometry and corrected analytic P1 sources

Claim type: bounded_theorem.

Primary runner: `scripts/scale_ladder_gravity_orthoscheme_zero_action_curvature_2026_10_18.py`.

These are supplied-model calculations under review, not adopted physical claims. The bounded claim is exactly the constructive algebra and finite fixture inventory below. Historical stronger statements are excluded from the live claim and preserved with exact original bytes in `archive/gravity_review_2026_10_18/MANIFEST.json`.

## Geometry retained

The D4 construction starts from integer sites, half-body centres and the six half-face centres. Coning the 16-cell facets produces 96 four-simplices, eight vertex types, 72 edge classes and total fundamental volume one. All 384 signed axis permutations are explicitly tested. G7 preserves these constructive data; no uniqueness claim follows.

G0 compares the generic simplex Hessian with the imported Kuhn helper at one momentum. G1 checks three Kuhn momenta; G2 checks two barycentric momenta. G3 compares the P1 scalar with the NN symbol on six fixtures and three roots. G4 and G5 compare tilted/skewed carriers at two scales. G6 performs the stated finite Einstein-Hilbert span fit. G8 computes the D4 displacement rank/nullity at three momenta. G9 uses Richardson values .02/.01. G10 compares four scalar shell directions at .2/.1. G11 searches 241 frequency samples near |k|=.05, then refines the detected minima on axis, face and body directions. Its reported coefficients near +/-1/12 and +/-1/16 are finite estimates, not a root-completeness or exact dispersion proof.

## Corrected P1 bilinear variation

Let S(k) be the P1 scalar symbol. Translation symmetry gives S(-k)=S(k)^T. At complex k, use a unit right null vector of S(-k1) as a transpose-left vector l1 of S(k1), and a unit right vector r2 of S(k2). The simplex values are l1[type] exp(-i k1.anchor) and r2[type] exp(i k2.anchor), without conjugating l1 again. For edge Gram matrix g and differences d1,d2,

Psi = volume [g^-1 (d1^T g^-1 d2)/2 - sym((g^-1 d2)(g^-1 d1)^T)],

and J_e is the contraction of Psi with the edge-induced variation of g. The code checks both l1^T S(k1) and S(k2)r2. A deterministic largest-component phase fixes reproducibility without changing normalized absolute source magnitudes.

G12 keeps the two-scale soft-eigenvalue count (eight in the selected index window). Its corrected bilinear projection onto the numerically selected nonmetric subspace is printed as a diagnostic, with no claimed scaling law. G13 uses seed 9 and scales .1,.05,.025. The corrected all-displacement fractions are approximately 1.5990e-5,1.9995e-6,2.4993e-7; uniform fractions 2.2588e-5,2.8269e-6,3.5343e-7. The finite predicate checks residuals below 1e-10, fractions below 3e-5 and successive ratios in (7.5,8.5). These three values do not establish a cubic asymptotic theorem. The former O(1) obstruction and forced block-reading conclusion are withdrawn.

G14 and G16 retain the explicit face/relative-strain reading maps and their constant-metric identities and blindness to non-site displacements at the specified fixtures. G15/G17 compute static responses at two/three momenta. They compare supplied readings, not a derivation of general relativity or of a physical matter-reading rule.

## Mathematical construction and scope

The Euclidean lengths, finite simplicial carrier, action orientation, tick coordinate (index 3), matter discretization and metric reading are supplied choices. No primitive selects them. For each triangle t the code constructs area and deficit derivatives a_t(k), d_t(k). The analytic Hessian is the symmetrized sum of a_t(-k)^T d_t(k); at real k this is Hermitian. Vertex displacements give the edge map G(k), while M(k) is the line-integrated metric-to-edge map. Nullities use the stated numerical thresholds, not exact rank certificates. Complex momenta use analytic transpose pairings, not Hermitian continuation.

The generic carriers use finite differences of simplex geometry with step 1e-6. Small eigenvalues, shell searches and fitted coefficients therefore carry conditioning and finite-difference error. A low singular value at a sampled point is not a certified zero, and a two-scale ratio is not a uniform asymptotic estimate. Every predicate below is limited to its literal finite fixtures in the primary source. The source prints measured values on both success and failure.

The original Regge parent is used only for its explicitly invoked area/dihedral/classification helper code where imported. Its historical physical-graviton, complete-classification and OS wording is not a premise here. The present calculations do not establish a positive physical Hilbert space, a real-time Hamiltonian, absence of additional roots, general universality, nonlinear consistency, or a microscopic selection mechanism.

## Reproduction and failure meaning

The primary declares a 300-second cap and literal input paths. It reports each finite predicate and its measured diagnostic, then `TOTAL: PASS=... FAIL=...`; nonzero failures return exit code one. A failure means the stated finite numerical predicate was not reproduced, including possible conditioning/tolerance failure. It does not establish a universal countertheorem. Source identity, a fresh runtime capture and the combined mechanical gate are separate obligations. The historical caches are recovery artifacts, not evidence for this corrected source.

The deferred register is `docs/work_history/repo/review_feedback/GRAVITY_REVIEW_SCOPE_AND_RECOVERY_2026-10-18.md`. Original PR 9714 remains a recovery branch until its deferred content has an explicit later disposition. No audit verdict or retained status is asserted here.
