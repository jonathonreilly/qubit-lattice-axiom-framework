# Handoff

The campaign is on branch `physics-loop/postmark-moving-index-central-match-20260924`, fast-forwarded to `origin/main` revision `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`, in worktree `/Users/jonreilly/Projects/Physics-worktrees/postmark-moving-index-central-match-20260924`. The earlier supporting notes remain hash-identical to their recorded sources; their recorded source base is `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`.

The strongest proved new result is the quantitative prepared-profile bound

\[
\|\widehat\eta_S(1/4)-\eta_\infty(1/4)\|_2<1.12\times10^4/S^2,
\]

which yields an actual-readout reduction error below (1.50\times10^4/S^2). The work also establishes exact path reflection and an energy-buffered endpoint eigenfunction barrier. The radius-24 Cauchy profile tail is below (6\times10^{-12}). These are conditional results for the supplied model.

The endpoint barrier now combines with the prepared state's spectral measure to give

    limsup_{S->infinity} sup_{theta in R} ||1_{E_(S,delta)} exp(i theta N_S) eta_S(t)||_2^2
      <= arccos(1-8 delta)/pi,  0 < delta <= 1/4.

The proof uses strong convergence of the zero-extended Jacobi matrices, the arcsine spectral law of N_infinity, and the fixed-energy endpoint barrier. Since the readout is diagonal in the path basis, this removes the endpoint-strip contribution after delta tends to zero, uniformly in the long phase. It does not control the interior phase sum.

The final exact-side note also transfers this endpoint bound to the endpoint term in the reduced scalar q_S(1/4): truncate eta_infinity to I_S, use (11) to show the truncated profile differs from eta_S by o(1), and evolve both by the same unitary. The endpoint/interior split then has no cross terms because V commutes with the spatial strip projector. Thus the endpoint part of q_S vanishes in the double limit; the interior part remains the target.

The remaining target is the real part of one profile scalar. Its finite spectral diagonal/off-diagonal split is emitted by the exact runner. At S=512, the diagonal term is much smaller than the off-diagonal term, but this finite diagnostic does not show convergence. The exact open obligation is a uniform bound on off-diagonal near-resonant phases in the interior, including the two mod-three crossings and the central layer. Endpoint mass is now reduced to the strip bound above.

An earlier ten-worker campaign-selection review chose the fixed-time scalar/readout target. That selection was not scientific review. No axiom or primitive update is supported. The supplied model remains an import.

## 2026-09-24 next-route selection checkpoint

The requested next-route comparison covered ten approaches: seven isolated worker reports (five-site Fourier/differential, operator phase sensitivity, reversible Markov, transfer/WKB, Jacobi/Weyl, arithmetic aliases, and randomized-phase concentration) plus three author-only checks (exact residue conservation, primitive five-cell cross-fiber geometry, and the axiom-to-model boundary). The app refused additional agent and follow-up threads after its thread cap; the three author checks are not independent reviews. None reviewed the final authored source files.

The selected next campaign is the **primitive five-site transfer and cross-fiber readout route**. The exact signed Casimir coefficients satisfy one five-site family. In the frozen principal symbol, `V` shifts the five-cell Bloch fiber by `4 pi/3`, while the readout phase difference has two nondegenerate joint stationary points. This shows that the period-three readout couples distinct primitive fibers; a 15-site frozen gap alone is not a global scattering law. The actual finite-spin coefficient gradients, genuine five-cell Bragg gaps, central layer, and discrete aliases still need control.

The first executed exact tests checked the signed five-site Casimir identity on 2,001 edges, the character's Bloch shift on the three-point cell Fourier transform, the 5x5 principal Bloch eigenvalues, and the stationary Hessian determinant `24` at both critical points. Their limits are local/principal: they prove no fixed-time readout limit. A first direct shift test on the raw negative labels failed because those labels shift in the opposite direction; the corrected all-spin identity uses the exact Casimir reflection `m -> -m-1`.

No axiom change follows. The native axioms and registered primitives do not select the supplied six-site dynamics, first-mark preparation, or period-three observable. A separate native derivation remains an upstream obligation.

This checkpoint's next action was completed: the exact five-site theorem note and paired deterministic runner are now present. The actual weighted finite-profile lag/alias criterion is the current route.

An unweighted diagnostic of the exact eigenvalue list confirms the scale issue but is not evidence for cancellation: for S=64,128,256,512,768 the adjacent increments of C lambda_j/4 span from about 0.060 to about 0.2S, and roughly 2.7–3.8% lie within 0.1 radians of a multiple of 2 pi. The probe does not include the prepared spectral coefficients or V_jk, so it measures neither the readout nor its resonant weight. Its script and output are preserved under `outputs/postmark_moving_index_2026_09_24/attempt_logs/discrete_phase_alias_probe.*`.

Full execution streams and prior failures are under `outputs/postmark_moving_index_2026_09_24/attempt_logs/`. The exact runner JSON is `outputs/postmark_moving_index_2026_09_24/EXACT_SIDE_FIXED_INDEX_KERNEL_RESULTS.json`. Earlier pipeline, strict lint, evidence, mutation, and vocabulary checks passed on an earlier candidate. Source notes, runner output, pack state, and the weighted-alias diagnostic have since changed, so those results are stale for the current tree and the combined final pass must be rerun. Independent reviewer confirmation and formal audit remain pending.

## 2026-09-24 weighted-phase checkpoint

The five-site note now records its exact target, proof-dependency table, the
uniform compact-bulk hypothesis, degenerate/crossing scope, and strongest
missing global phase/overlap lemma. It adds the exact signed five-site Casimir
family, four first-order same-fiber compressions and principal slope
magnitudes, the five-cell character shift, the two nondegenerate cross-phase
stationary points, the principal lobe area with the factor of five in physical
site coordinates, and the noncrossing (1/S) scalar correction. None of these
is a global propagation or readout result.

I personally implemented `outputs/postmark_moving_index_2026_09_24/weighted_alias_diagnostic.py` to compute the finite-profile cosine-character double sum by (a) direct evolution and (b) actual spectral weights grouped by positive lag. At S=24,48,96 the two evaluations agree within (3.1\times10^{-15}), and the Hermitian positive-lag decomposition closes within (3\times10^{-17}). The twice-positive-lag per-lag Abel upper bounds are 96.97, 213.99, and 475.73; the absolute weight on first-difference aliases within 0.01 radians is 0.0117, 0.0137, and 0.0193. These are finite float64 diagnostics only. The one-lag triangle estimate is numerically too broad to show decay on these samples; that does not prove the sufficient criterion cannot hold asymptotically or that the physical readout fails to converge.

The next selected analytic object was the exact two-energy Schur/Weyl pencil.
I have now independently derived its cell determinant recurrence and
anchor-to-anchor Schur link. If the four interior sites of cell `j` are
eliminated at spectral parameter `z`, their block is

    K_j(z) = [[A+B-z,-sqrt(AB),0,0],[-sqrt(AB),2A-z,-A,0],
              [0,-A,A+B-z,-B],[0,0,-B,2B-z]],
    A=R_j, B=R_(j+1), R_m=C-m(m+1).

Writing `D_j(z)=det K_j(z)`, its continuant gives
`(K_j(z)^-1)_(1,4)=A^(3/2)B^(3/2)/D_j(z)`, hence the reduced anchor link is
`-A^3 B^2/D_j(z)`. The exact period-three overlap between energy `z` and
energy `w` has the reduced matrix weight

    Q_V(z,w)=V_A + H_AI (z-H_II)^(-1) V_I (w-H_II)^(-1) H_IA.

When `V=I`, this weight is the negative divided difference of the Schur
pencil and at equal energies is its positive normalization metric `-S'(z)`.
Four finite-spin reconstruction checks (S=1,2,3,5) agree below `5e-14`.
This formula is defined away from the eliminated-block poles; it is an exact
representation, not a uniform bound on residues or on the actual O(S^2)-time
phase sum. The prepared-profile readout therefore remains open. Full probe
source and output are in `outputs/postmark_moving_index_2026_09_24/attempt_logs/`.

I reread the current minimal-axiom memo at source base
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. It explicitly says Admissibility
does not choose a Hamiltonian and Record does not specify record-production
dynamics. This confirms that the model-to-axiom bridge is an import boundary;
the present conditional readout work does not force an axiom edit.

The no-go skill was checked against current main and matches the installed
copy byte-for-byte. Its N1-N8 gate is not invoked for this bounded positive
support note: the note does not declare a route absent or claim an impossibility;
it scopes its own theorem and names the separate target it does not prove.
This applicability decision is not a no-go-gate PASS.

At the 13:26 UTC checkpoint, the authorized 12h window had about 3h12m
remaining. Current base after fetch is still
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. The current note/runner hashes,
canonical caches, current-hash mutation checks, vocabulary, and citation
manifest have been refreshed. The external-log full pipeline passed the source
fingerprint, classification, and strict audit-lint stages; repository
invariant stage 18 then required the reviewed manifest delta to be staged. The
initial in-worktree-log runs are preserved as failed attempts, and the
external-log run is at
`outputs/postmark_moving_index_2026_09_24/attempt_logs/final_pipeline_author_source_external_v3.log`.
I also tightened the five-site crossing-slope check to sample away from its
zero factor, reran its three-mutation suite, and force-refreshed all four
runner caches. The five-site current-source receipt and all caches now match.
The next full pipeline uses `--stage-citation-manifest` and redirects live
output outside this worktree. No PR has been opened; after that preflight, a
non-draft review PR may be opened without merging.


## 2026-09-24 cold-read and isolated-validation checkpoint (13:50 UTC)

I personally cold-read the complete four theorem notes and all four primary
runners at candidate base `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. The
mathematical claims stay bounded: the prepared-profile and electric-endpoint
contributions are controlled, while the interior two-energy phase sum remains
open. The local-symbol, central-core, and five-site geometry notes do not state
a global propagation theorem, finite-spin limit, separated subsequences, or
axiom-level result. The exact Schur probe is a finite identity check away from
eliminated-block poles; no pole-uniform result or phase cancellation follows.

For review-only combined validation, the disposable worktree
`/Users/jonreilly/Projects/Physics-worktrees/postmark-candidate-validation-20260924`
was overlaid from the author candidate and checked against its base. All 129
changed paths matched byte-for-byte and by mode; the author index was clean.
Full-pipeline pass 1 completed all 18 stages with
`--stage-citation-manifest`, strict audit lint ended `OK: no errors`, and
`check_changed_audit_evidence.py --base origin/main --include-worktree` reported
`checked=4 failures=0 control_failures=0`. Logs are retained outside both
worktrees under `/Users/jonreilly/Documents/Codex/research_runs/postmark_campaign_20260924/`,
with hashes in the corresponding checkpoint record. This pass predates this
pack edit, so the final frozen packaged candidate must receive one combined
pass; its three complete logs are assigned stable names in that external
receipt directory. No independent science review, formal audit, merge, or
axiom change is claimed.

Next: final frozen-candidate pipeline/lint/evidence pass; explicit-source
staging and PR creation as a ready-for-review (non-draft) PR; then resume the
pole-aware Schur/Weyl phase route personally before the authorized
`2026-09-24T16:38:00Z` deadline.
