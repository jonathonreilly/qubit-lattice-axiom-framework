# Log absolute determinant does not select a determinant sign

**Type:** bounded_theorem
**Date:** 2026-04-19; scope corrected 2026-10-21.
**Status:** bounded observable-level limitation; no general impossibility theorem for the framework and no physical selector closure.
**Companion:** [DPLE mathematical correction](DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md).
**Runner:** `scripts/frontier_dm_dple_theorem.py`.

## Exact invariant and its scope

For an odd-dimensional Hermitian pencil H(t), the second pencil -H(t) has opposite determinant sign but exactly the same W(t)=log|det H(t)| wherever defined. Thus any rule depending **only** on W and its derivatives assigns the same result to the pair. Such a rule cannot prefer a determinant sign on a class that includes both pencils.

The distinction “a class that includes both” is essential: negating H also negates its baseline. No invariance of a fixed source chamber, preparation, Hamiltonian dynamics or physical identification follows merely from Hermiticity. Additional structure may select one member. This argument does not prove that every axiom-based route to a physical sheet must fail.

An exact witness is H_plus(t)=diag(-1,B(t)), where B(t)=[[t-1/2,1],[1,-(t-1/2)]]. Its determinant is (t-1/2)^2+1>0. H_minus=-H_plus has negative determinant. Both have the same W, with W''(1/2)=2>0. Their polynomial curvatures have opposite signs. The runner verifies these identities symbolically; no sampling fraction or literal True is used as evidence.

## What the corrected DPLE statement does and does not imply

The polynomial/logarithmic-derivative proof gives an upper bound floor(d/2) on W's nondegenerate minima. It does not imply existence, a positive sign, or selection of a basin. d=2 and d=3 both have an at-most-one bound; d=2 has explicit nonvacuous examples. The former claim that DPLE derives conditions (1)–(3) of an existing-minimum selector is withdrawn.

At a critical point, W''=p''/p. The old p''>0 test agrees with a W minimum only when p>0. A positive-sign restriction remains an added chart predicate, not a consequence of a W-count theorem. Determinant-sign agreement at one point is also weaker than full inertia agreement or nonsingularity of an entire path. The companion gives explicit counterexamples.

## Baseline component and conditional PNS implication

Define C_base to be the connected component of the nonsingular source domain containing the supplied baseline. It is a subset of the positive-determinant locus when the baseline determinant is positive. Equality with the entire positive locus requires a separate connectedness argument and is not assumed here.

If H(t) is continuous and nonsingular for every t in [0,1], its inertia is constant. Thus a positive baseline determinant remains positive. This is the conditional PNS implication. Continuity alone allows zero crossings; invoking a path already chosen to end at Basin 1 does not select Basin 1 as physical. A finite scan of a path is numerical evidence, not a universal nonsingularity proof.

The [P3 note](DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md) addresses a specified path. Its physical endpoint identification, the source dynamics and PNS premise remain separate obligations. No experimental CP-phase exclusion is established by the present observable argument.

## Historical provenance and unresolved scope

The original April note referred to a T8 negative-sheet random campaign. The raw prompt capture `docs/ai_methodology/raw/prompts_session_b5ee8c6c_jonreilly.md` records that historical task, but the f24 runner contains T1–T7 and no T8. That historical claim is not fresh evidence for the current classifier. The present exact opposite-sign witness replaces the current evidentiary gap without editing raw prompts or historical logs.

The invariant leaves open physically supplied asymmetric dynamics, a proved nonsingular preparation path, or an independently justified physical sector. It does not add any such premise. The older “F4 axiom closed,” “d=3 uniquely binary,” and “single remaining input” summaries are superseded here. Stable filenames and identifiers are preserved; source corrections do not write audit verdicts.

## No-Go Discipline Gate

This is a **partial narrowing of the old no-go**, not a packet PASS or an exhaustive framework impossibility claim.

- **N1 — Routes:** one invariant family was actually checked: odd-dimensional negation, with exact opposite-sign determinant/log-derivative witness. A fixed baseline/chamber, asymmetric dynamics, a nonsingular preparation path, or a sector identification are admissible extra-structure routes outside the W-only domain; none is ruled out here. Fewer than five distinct attempted families means the procedural five-family packet requirement is not met. This does not invalidate the displayed invariant identity.
- **N2 — Walls:** no multiple-wall independence or minimal residual count is asserted. The sole theorem domain is a sign-paired pencil class and a W-only rule; relations among possible additional physical inputs are unresolved.
- **N3 — Hidden premises:** Hermiticity, odd dimension, invertible domain, sign-pair closure of the class and W-only dependence are explicit. A fixed chart need not obey sign-pair closure. The polynomial count theorem is not a physical premise.
- **N4 — Residual matching:** the companion's section 4 and exact runner sign-flip fixture address only W's lost determinant sign. P3 and PNS context address supplied path nonsingularity, not existence of a physical selector, and are not witnesses for a broader no-go.
- **N5 — Resolution:** individual matrix entries and determinant/curvature values are checked; finite eigenvalue/critical-point modes and 2/3/4-dimensional blocks are exercised. No site dynamics, all-chamber classification or lattice limit is tested or ruled out.
- **N6 — Partial closure:** choosing a sign convention can label the two members but does not physically select one. Additional physical asymmetry or a proved path may select a member. No new axiom is asserted necessary, no primitive absence is claimed, and no registration is proposed.
- **N7 — Steelman:** a physical preparation law might fix H0 and confine its source trajectory to a nonsingular component. That excludes the negated baseline, so the exact W symmetry on the enlarged pencil class cannot refute such a law. The actionable obligation is to derive nonsingularity for that preparation without selecting the desired endpoint first. This is outside the narrow invariant theorem and remains open.
- **N8 — Prior echo:** `DM_ABCC_PMNS_NONSINGULARITY_THEOREM_NOTE_2026-04-19.md` section 2 supplies the conditional IVT implication, while its opening calls PNS an input. That is a partial conditional route, not an established retirement by dynamics. The broader headline equivalence, physical-mass assertions and current empirical wording are not validated here. The raw April prompt records the same endpoint-circularity concern; it is history, not current proof.

No audit verdict, no-go ledger or historical snapshot is altered by this source correction. The unfulfilled packet requirement is reported for independent review; no fresh no-go promotion is requested.
