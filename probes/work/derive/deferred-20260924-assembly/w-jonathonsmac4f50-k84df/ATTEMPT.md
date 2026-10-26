# J:derive:deferred-20260924-assembly:a1 -- one arrow of the assembly graph: ONE_VERTEX_INVARIANTS -> T_GRAVITY

Worker: Claude Sonnet 5.5 (same family as the earlier lane workers; unrefereed). Provisional.

## Plain-language summary

The landed assembly note proves a statement about a made-up yes/no graph and says so. A stronger sentence was cut from it before landing: "one-vertex scalar invariants for one neutral statistic feed gravity (PR 8918)". I took exactly that arrow and asked what it would have to mean physically.

What I found:
1. In the graph the arrow does nothing. Delete it and no answer changes. The node it starts from is "true" only because an empty AND is true, not because anything was derived.
2. In the supplied Gaussian stand-in for ice, the only non-trivial one-vertex statistic (the landed alignment statistic f) does give an attraction between two identical inclusions, and the attraction is exact in sign. But it falls off as the inverse sixth power of distance, not as one over distance. A 1/r pull that also attracts like sources is not available from this node. It appears in the other parent of the same target (the tensor-model note) only through a scalar sector that is unbounded below.
3. No premise in the sources turns a record statistic into a curvature or a source of gravity. So the physical implication is not derived and the missing premise is named below.

Nothing here restores the cut sentence, and nothing here proves the opposite (the review already withdrew "excludes gravity", finding U11-R6).

## Setting and what was read

I read `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines) on origin/main. Their relevant content: the four axioms supply a lattice Z^3, a one-site possibility domain, a nearest-neighbour rule for the distribution of a forming record, and records (MINIMAL_AXIOMS L35-83). L85-90 and L108-112 say anything else, including dynamics, a source/action, or a physical identification, needs its own derivation. Approved primitives: scale reference, kinetic isotropy, realized state (PRIMITIVE_REGISTRY_CHECK L29-130); none supplies a gravitational source or a Gaussian ice measure.

Pinned revisions: origin/main = `3e1a2dd2531590dabf85bee8db56175ba9b96e90` (fetched at run time; the read-only checkout was at `a77a3449c9`; the graph note, runner and the two cited notes are byte-identical in both, checked by diff stat). Landing commit named by the manifest: `1cb2a082bf`. Frozen PR 8648 head: `fe1e7a925c5b66b669b69afe57581cac0e60b404`, fetched; it is not an ancestor of main (squash landing).

Existing work consulted before calculating: `probes/work/derive/axioms-and-the-event-lattice/` (a1, a2, a3 and three referee reports). They are readings of the axiom memo about the past of a record; none concerns the assembly graph or any arrow into T_GRAVITY (grep for "assembly", "8648", "candidate": no hits). Open PRs searched (`gh pr list --state open`, 200 most recent, title filter assembly/ice/neutral scalar/gravity/decision): no open PR on this question (10055, 10029, 9948, 9890 are other candidate-law blocks). origin/main grep for the quadratic-inclusion argument below: no hit in the ice notes. The sign problem for gravity is landed elsewhere: `docs/GRAVITY_SIGN_FROM_REFLECTION_POSITIVITY_UNITARITY_REDUCES_TO_EMERGENT_DIFFEOMORPHISM_NARROW_THEOREM_NOTE_2026-06-08.md:45` and `docs/GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md:30,53`. I rely on neither.

## The arrow and the statement to be settled

Graph (landed runner, line 18 data): ONE_VERTEX_INVARIANTS is a "landed" reference node pointing to `docs/UNIFORM_ICE_CARRIES_THE_LATTICE_GREEN_FUNCTION_IN_ITS_CHARGED_SECTOR_WHILE_NEUTRAL_SCALAR_RECORDS_ARE_SHORT_RANGED_BOUNDED_THEOREM_NOTE_2026-09-23.md` (the landing of PR 8918). It is an AND-parent of T_GRAVITY. Frozen original of PR 8648 (`docs/CANDIDATE_ASSEMBLY...NOTE_2026-09-22.md` at `fe1e7a9`, claim_scope) says: "one-vertex scalar invariants for one neutral statistic feed gravity (PR 8918)". The review finding for PR 8648 and the U11-R6 finding (batch-15.json findings; review-unit11-v1.json) demoted it.

Residual R, stated sharply.
- Domain: the supplied divergence-free zero-flux Gaussian link field on a periodic cubic L^3 torus, energy (K/2) sum B^2 (the landed comparator in the unit-link-field note), together with the rotation-invariant one-vertex statistics of 3-in/3-out vertex states.
- Question: does the arrow supply a source channel with the two qualitative properties of Newtonian gravity: (g1) like sources attract, (g2) potential ~ 1/r?
- Success witness: a theorem that such a channel exists in the comparator, or an exact account of which property fails and which premise would restore it.

## Proof steps

Labels: PROVED (argument given), CHECKED (executed by check.py), ASSUMED, READING.

1. ASSUMED. Graph semantics as in the landed note L21: decisions true iff chosen, source true, OR for choices, AND otherwise, empty AND true, empty OR false.
2. CHECKED (A1-A2). The graph has 117 nodes, 40 menu entries, 210 edges; an independent brute force over all 4096 decision subsets reproduces the four landed minimal families of T_GRAVITY. Not new.
3. CHECKED (A3-A4). No decision lies in all four families, and each family has exactly one of order law (formation reading) or reading (static reading). Not new in content (landed predicate 8); no decision is individually necessary.
4. CHECKED (A5). Deleting the edge ONE_VERTEX_INVARIANTS -> T_GRAVITY changes no family; likewise GRAVITY_BOUNDARIES and HOLE_READS_CLOCK; deleting T_RECORD_DYNAMICS or T_GAUGE does. The landed runner checks this for ONE_VERTEX only (predicate 20); the five-parent comparison is new bookkeeping.
5. PROVED + CHECKED (A6, A7, A7b). Each of the 78 reference nodes carries an arrow from AX, but a parentless node is true anyway (empty AND): removing AX -> ONE_VERTEX leaves all families unchanged. Truth of the node enters only if one overrides it to false, and then T_GRAVITY has no family. Hence the Boolean value of this arrow is a convention of the encoding. T_GRAVITY depends on 59 of the 78 reference nodes (A8). This is consistent with the landed note's own disclaimer (L17: names and file existence supply no proofs) and is not a defect of that note; it fixes what "arrow" can mean.
6. CHECKED (A9, A10). The deferred sentence is in the frozen original and absent from the landed note.
7. CHECKED (A11-A13, quotes with path:line). The cited source says its models are not derived from the axioms (`UNIFORM_ICE_CARRIES...:16`), asserts no gravity conclusion (:16), and leaves the tail unresolved (:30). The other parent says the axioms do not supply its tensor pairs, constraints, Hamiltonian, source or phase (`LOCAL_FINITE_CLOCK...:42`). So neither parent derives its own premises from AX.
8. PROVED + CHECKED (B1-B7). The cubic rotations act transitively on the six outward directions; averaging the permutation representation gives J/6; the only invariant linear statistic is the sum of outward arrows, which is 0 on all 20 ice vertex states. Rotation orbits on the 20 states: two (sizes 8 and 12), by direct enumeration and Burnside. So there is exactly one non-constant invariant one-vertex statistic. Recovers the landed lemma; adds the count of the nonlinear remainder (the lemma's own caveat).
9. CHECKED (B8). The landed alignment statistic f takes values {-1, 3} and its level sets are exactly the two orbits. f is therefore not one of several choices; it is the whole non-constant invariant space of one vertex.
10. PROVED (Isserlis/Wick). For a centered Gaussian vector with covariance Sigma and symmetric positive semidefinite diagonal selectors Q_x, Q_y: Cov(B^T Q_x B, B^T Q_y B) = 2 tr(Q_x Sigma Q_y Sigma) = 2 sum_{a in x, b in y} Sigma_ab^2 >= 0. For s_x = lambda_x B^T Q_x B inserted in the weight, ln Z to second order gives F_int = -lambda_x lambda_y Cov + O(lambda^3).
11. CHECKED (C1-C7), exact rational arithmetic plus 50-digit determinants. On the 4^3 torus the zero-flux divergence-free covariance (K = 1) is an exact orthogonal projector of trace 126 (C2-C4). The vertex statistic s_v = sum of B^2 over the six incident links has C(r) > 0 at all 64 separations (min 1/256, C(1,0,0) = 3243/2560, C(2,0,0) = 1687/19200) (C5). The generating-function determinant gives F_int(lam,lam)/(-lam^2 C) = 1 and F_int(lam,-lam)/(lam^2 C) = 1 to 3e-8 and 1e-16 (C6). Conclusion in the comparator: identical inclusions attract at leading order whichever sign of coupling; opposite-sign inclusions repel. Property (g1) holds for this channel.
12. CHECKED (C'/C9-C11), floating point, not a proof. On a 112^3 torus (with the isotropic zero-mode correction) the axis covariance has local exponent 6.42 at d = 8, 6.12 at d = 14, 6.035 at d = 19, decreasing toward 6; the FFT construction matches the exact Sigma of step 11 to 1e-12. SUGGESTED analytic reason: Sigma_ij ~ (3 rhat_i rhat_j - delta_ij)/(4 pi K r^3), so C ~ r^-6. Property (g2) fails: exponent 6, not 1.
13. CHECKED (C8) and READING. For a linear coupling to the same Gaussian field through the lattice Green function (the charged sector of the cited note), the cross energy of two like unit sources is q^2 G0(r), strictly decreasing in r on 4^3 and 6^3 (exact). So that 1/r channel repels like sources: (g2) holds, (g1) fails. READING: this is the usual spin-1 versus spin-2 sign argument; the sources that supply it are the landed gravity-sign notes cited above.
14. CHECKED (D1-D6), recovered, not new. In the tensor-model parent: the same constraint complex with Hamiltonian H_L gives static scalar-source energy rho^2/4 (contact, no kernel), with H_N gives -rho^2/(4 k^2) (attractive inverse-Laplacian), at k = (1,2,2) symbolically; the unconstrained scalar block has det K = -J^2/2 < 0 for every finite U. So (g1)+(g2) appear in this graph's data only through an indefinite scalar sector, and only for a supplied noncompact Hamiltonian.
15. READING. Therefore the physical implication "ONE_VERTEX_INVARIANTS feeds gravity" cannot be derived from its source: in the comparator its one non-trivial channel has (g1) and fails (g2), the linear channel has (g2) and fails (g1), and no premise in either parent joins a source map to a curvature response.

## First failing step and exact next obligation

First failing step: 15, precisely the passage from "a one-vertex statistic of the record field exists and induces an interaction" (steps 8-12) to "that interaction is gravity".

Missing premise M (one statement): a source map taking the record field's neutral content to a stress-like source of a field whose static response kernel has an attractive 1/k^2 sign for like sources (step 14's H_N scalar sector or a non-Gaussian replacement that is bounded below), together with a compatibility statement that the ice measure of ONE_VERTEX_INVARIANTS and the tensor model of GRAVITY_BOUNDARIES are the same model (they are different supplied models: link arrows with a 3-in/3-out rule versus N-level symmetric tensor slots).

Exact next obligation (finite, checkable): decide whether the Gaussian comparator can be completed, with the divergence-free field B as the physical object, by a scalar mode of negative sign that keeps the Hamiltonian bounded below on the constrained quotient. Test: in the zero-flux sector on the 4^3 torus compute the exact quotient Hessian of H_N-type energy plus a coupling to s_v, and decide positivity of the reduced form. If the quotient is positive, the 1/r attractive channel exists in a model that includes the ice statistics; if not, the arrow has no physical implication in this comparator class. Not done here.

## What is new, and what is not

Not new: the graph combinatorics (A1-A4), the one-vertex lemma (B3, B5), the tensor-model facts (D1-D6), the demotion of the "feeds gravity" sentence, the disclaimer that edges are not implications.

New within the stated scope (unrefereed, same family):
- A5/A7/A7b: the five parents of T_GRAVITY compared edge by edge, and the observation that the AX arrows are themselves Boolean-vacuous (empty-AND convention). Bookkeeping, no physics.
- B6-B8: exactly one non-constant rotation-invariant one-vertex statistic on the 20 ice vertex states, equal to the landed f.
- Steps 10-12: in the supplied Gaussian comparator the neutral quadratic channel is like-attractive with exact sign and decays with exponent tending to 6. The statistical argument is standard fluctuation-induced interaction; no literature priority is claimed, and I found no repo note stating it for the ice comparator.

No HIT is printed: nothing here is a defect in a landed theorem and the comparator result is a standard identity applied to a supplied model.

## Limits

- The Gaussian field is a supplied comparator; the landed notes say the ice measure is not shown Gaussian (`UNIFORM_ICE_UNIT_LINK_FIELD...` calibration paragraph). The exponent 6 is therefore not a statement about uniform ice; for the ice measure the tail is unresolved (`UNIFORM_ICE_CARRIES...:30`).
- Exponents come from a 112^3 torus numerical run, with lattice corrections of relative order 1/r^2 and a finite-torus offset corrected by an isotropic average. Not a certified enclosure.
- Nothing in the argument selects ice, soldering, a reading or a clock. No physical gravity statement is made or excluded.
- Commit/run_probe/claim steps in the brief were not done: this worker was restricted to the scratch folder and may not touch the repository.

## Files

- `ATTEMPT.md` (this file), `check.py` (2.7 s, one process, about 0.35 GB), `RECOVERY_STATUS.json`.
