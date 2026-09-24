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

## 2026-09-24 follow-up selection and weighted-phase execution (15:15 UTC)

The prior support milestone is preserved on open non-draft [PR #9078](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9078), head `5171af01191cc2db9d5bad0f8eca2185114ebbe3`, based on current `origin/main` `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. Its author worktree and disposable validation copy were removed after the pushed branch hash was matched to `origin`; the current personal science lane is `physics-loop/postmark-electric-weighted-phase-20260924` at `/Users/jonreilly/Projects/Physics-worktrees/postmark-electric-weighted-phase-20260924`. Main was fetched again and remained at the recorded base. Repo lock is held by this task until `2026-09-24T18:01:11Z`.

The ten-route selection was seven isolated worker reports plus three author exact checks after the application refused more worker threads. Three focused follow-up lenses then preferred **direct deterministic cancellation of the prepared-weighted actual phase sum** over spending the next block only regularizing the Schur chart. The pole mass is a possible excision lemma, not a cancellation mechanism. Those route workers reviewed the probes and route claims, not the final theorem sources; the new science calculations below were performed by the author alone.

Two root-only probes initially labeled a linear-operator surrogate as the actual readout. They propagated `exp(-it C N_S)|0>` and omitted the `N_S^2` phase. A cold read caught this before those values were used as target evidence. The exact phase for an eigenvalue `E` of `H_S=C N_S` is `exp[-it(E^2/C^2-E)]`. Both probes were corrected and retained as `corrected_actual_generator_pole_mass_probe.py/.json` and `corrected_actual_generator_schur_probe.py/.json`. The corrected spectral readout agrees with an independent dense `expm` calculation to at most `1.12e-15` for S=1,2,3,5. The pole distances and prepared weights were unchanged because `N_S^2` changes phases, not eigenvectors or spectral weights.

The corrected actual period-three values at S=8,16,32,64,128,256,512 are respectively `0.302881`, `0.301003`, `0.330615`, `0.332377`, `0.308217`, `0.329723`, `0.341669`. The exact profile scalar at S=96,192,384,512 is `-0.0277534`, `0.00958924`, `0.0236422`, `0.0125036`; the corresponding actual-readout versus scalar-reduction differences from the primary runner are `1.90e-6`, `5.47e-7`, `5.02e-8`, `6.93e-8`. This finite sequence oscillates around the proposed `1/3` readout and neither proves convergence nor gives separated limiting subsequences. At relative pole radius `0.01` in adjacent full-spectrum-spacing units, prepared pole-neighborhood mass is about `1.0–2.1%` at S=16,...,512; at S=512 it is `1.34%` of prepared mass versus `1.58%` of modes. This looks counting-like in the sample and supplies no uniform pole-mass theorem.

I then extended the exact prepared-profile sum by spectral lag. With `c_j=<phi_j,P_S eta_infinity(1/4)>`, `v_jk=<phi_j,cos(2*pi*n/3)phi_k>`, and

    L_(S,h)=sum_j conjugate(c_j)c_(j+h)v_(j,j+h)
                    exp(i C(lambda_(j+h)-lambda_j)/4),
    Re(q_S)=d_S+2 Re sum_(h>=1) L_(S,h),

the `fixed_low_lag_phase_cancellation_probe_v1.py` result shows that the sum over tested lags h<=32 contributes only `0.00018` to `Re(q_512)=0.01250`. The changed `full_lag_scale_decomposition.py` computes every lag, bins lags by h/(10S-3), checks the full spectral sum against direct evolution, and records the per-bin alias weight. At S=96,192,384,512 the sum of individual `|L_(S,h)|` is `0.3887, 0.3781, 0.3716, 0.3720`; the signed real sum over h is `-0.01410, 0.004699, 0.01178, 0.006198`. The exact direct-versus-spectral error is at most `1.95e-13`. This points to a joint two-index or cross-lag stationary-phase mechanism; a proof for each fixed h alone will not close the readout. The one-lag Abel bound is still unhelpful, growing to `1385.7` at S=512. These are float64 diagnostics, not an asymptotic statement.

There is an exact phase-accuracy gate for any termwise WKB substitution. For an eigenvalue `lambda` of `N_S`, the actual generator phase at t=1/4 is

    Phi_C(lambda)=(C*lambda-lambda^2)/4.

For any proposed approximation `lambda_tilde`,

    Phi_C(lambda)-Phi_C(lambda_tilde)
      =(lambda-lambda_tilde)*(C-lambda-lambda_tilde)/4.

Since both eigenvalues stay bounded while `C=S(S+1)`, a generic `O(S^-2)` eigenvalue error produces only an `O(1)` phase guarantee, not an `o(1)` phase error; a uniform termwise replacement needs `o(S^-2)`, or a cancellation argument robust to order-one phase errors. This is an exact algebraic sensitivity statement. It does not show that an `O(S^-2)` WKB expansion cannot still be used in an averaged cancellation proof.

The next personal stretch is to derive a phase-accurate, weight-aware discrete stationary-phase/Poisson decomposition for the full `(j,k)` spectral sum, identify its nonzero alias charts, and test whether the five-site local cross-fiber stationary geometry controls those charts after global quantization. Keep the diagonal, central layer, Bragg crossings, and endpoint-tail result explicit. If the route yields only a target-equivalent missing estimate, record that wall and pivot to the next independent campaign opportunity. No axiom update is indicated: Admissibility and Record still do not choose the supplied Hamiltonian, preparation, or output map.

## 2026-09-24 discrete-alias checkpoint (15:28 UTC)

Source remains the dependent follow-up branch
`physics-loop/postmark-electric-weighted-phase-20260924`, worktree
`/Users/jonreilly/Projects/Physics-worktrees/postmark-electric-weighted-phase-20260924`,
parent head `5171af01191cc2db9d5bad0f8eca2185114ebbe3` and current main
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. The open parent PR #9078 remains
non-draft; it contains the conditional-support milestone only. The authorized
12-hour campaign deadline is `2026-09-24T16:38:00Z`.

I personally derived and computed a two-level alias census for the exact
prepared-profile scalar. With `theta_j=C lambda_j/4` and
`alpha_j=theta_(j+1)-theta_j`, the exact fixed-lag phase
`theta_(j+h)-theta_j` has forward difference
`alpha_(j+h)-alpha_j`. Individual-slope aliases and lag-derivative aliases
are distinct conditions. The probe
`outputs/postmark_moving_index_2026_09_24/attempt_logs/phase_alias_overlap_census.py`
uses the actual prepared coefficients and cosine-character overlaps, checks
lag reconstruction against direct evolution, and reports per-threshold and
per-scale bins. At S=96,192,384,512, the sampled one-index slopes visit 4,7,13,
17 distinct nearest alias integers. Prepared mass on modes whose left slope is
within 0.01 radians of an alias is 0.00444,0.00484,0.00454,0.00432. The sum
over all lag weights on pairs whose lag derivative is within 0.01 radians of
an alias is 0.01931,0.02603,0.03710,0.04243. This is not a bound on the
complement and is not an asymptotic result. The forward-difference census
separately reports its terminal pair per lag; the summed terminal-pair weight
L1 falls from 0.0357 at S=96 to 0.0157 at S=512, but its imaginary signed
contribution cannot be discarded in a real-part estimate without a further
pairing argument. Direct-versus-lag real reconstruction errors are below
`1.3e-13`.

An elementary conditional scale calculation explains why a principal
zero-alias stationary point is incomplete. If on a smooth quantized branch
`lambda_(j,S)=F(j/S)+...`, then
`alpha_(j,S)=(S/4)F'(j/S)+...`; for a macroscopic lag `h=rho S`,
`alpha_(j+h)-alpha_j=(S/4)[F'((j+h)/S)-F'(j/S)]+...`. Hence the reciprocal
integer can range over O(S) values when the bracket is nonzero. This scaling
is conditional on a sufficiently regular global branch quantization, which
is not established here. The local five-site action alone cannot certify it
through Bragg crossings, the central layer, and endpoints. A usable Poisson
argument needs phase-accurate branch quantization and the actual two-index
overlap weights, then a uniform sum over all alias charts and their boundary
terms. The exact termwise phase tolerance remains `o(S^-2)` in eigenvalue,
unless the cancellation estimate is proved robust to an order-one phase error.

I also extended direct spectral evaluation of the actual generator
`G_S=N_S^2-CN_S` to S=640,768,896,1024. Actual period-three values at
S=512,640,768,896,1024 are 0.341669,0.337053,0.337260,0.336208,0.328571.
The factorized/direct state check is within `2.6e-11` in vector norm and
`6.4e-13` in the character expectation, with norm preservation at double
precision. These values remain float64 diagnostics: they support neither a
limit claim nor a separated-subsequence wall.

Hashes for the new scripts and their JSON receipts:

    a063f40d31707df0edf46e9bc8751fa857a121e388b26f1420ed1886d9e20db2  phase_alias_overlap_census.py
    ef62f5fad6bb5281fa04860a4de59938edc9d0b7be908e15ee0e98b21be53463  phase_alias_overlap_census.json
    e07c81c11e1eb19c413df6ed11b1085972e1794666e4223f622aee9a60351896  actual_readout_extended_sizes.py
    0b7592c578361c77caa0fde730737511a190ce8c60d5942a6a62557e858024b3  actual_readout_extended_sizes.json

The next proof obligation is now narrower: produce a global branch action and
phase-accurate quantization through the crossings, then estimate the prepared
overlap-weighted sum uniformly over its O(S) reciprocal aliases; include the
diagonal and terminal terms. If no derivation closes before the authorized
deadline, preserve a bounded checkpoint explaining this wall instead of
promoting finite samples. No axiom change is supported by this work.

## 2026-09-24 principal-action alias discriminator (15:40 UTC)

I used the lobe action already proved in the five-site note to derive the
leading Weyl-count scale. The five folded bands obey
`E_l(u,theta)=2(1-u^2)-2(1-u^2)cos((theta+2*pi*l)/5)`. Summing the five bands
over `theta` is five times the integral over physical momentum
`nu(u,k)=4(1-u^2)sin^2(k/2)`. The superlevel area over positive `u` is
`A_+(lambda)=pi(2-sqrt(lambda))`; reflecting across `u=0` gives twice that
area. Therefore the principal Weyl law is

    N_{>lambda} ~ (5S/pi) A_+(lambda) = 5S(2-sqrt(lambda)),
    N_{<=lambda} ~ 5S sqrt(lambda),
    lambda_j ~ (j/(5S))^2,
    theta_j=C lambda_j/4 ~ (S+1)j^2/(100S).

The corresponding **smoothed** phase increment is
`alpha_j~(S+1)(2j+1)/(100S)`. Across the `10S-3` sorted levels this predicts
an O(S) alias index range with maximum about `S/(10*pi)`. The eigenvalue-only
probe `weyl_alias_scaling_probe.py` finds Pearson correlation 0.985, 0.993,
0.996, 0.997 between exact adjacent phase gaps and this leading increment at
S=96,192,384,512; the linear-fit slope is 0.020000 rad per sorted index at
all four sizes. The principal formula predicts 4,7,13,17 nearest alias
indices, exactly the observed distinct counts. This gives a concrete reason
the nonzero reciprocal aliases cannot be omitted. The derivation is a
phase-space counting law; differentiating it does **not** prove the adjacent
gap estimate pointwise or uniformly near band crossings.

The action-only phase is insufficient for the readout. In
`quadratic_phase_resonant_lag_probe.py`, fitting the best quadratic phase to
the exact eigenphases still leaves maximum phase residuals 3.56,4.94,6.70,7.88
radians and changes `q_S` by 0.02318,0.00030,0.02207,0.00417 at those four
spins. The predicted narrow (0.01-radian) resonant-lag sets carry only
0.0011--0.0018 of `sum_h |L_(S,h)|` (total 0.372--0.389); a 0.1-radian window
carries only 0.0120--0.0145. The principal quadratic action organizes the
alias scale but does not isolate the readout. Actual subprincipal phases and
the full prepared overlap weights remain decisive.

Hashes for the two new probes and JSON receipts:

    2e73b72e4b87ca035d37d522edef6fa6907ae6be36565adf4c3e5f3819c192bc  weyl_alias_scaling_probe.py
    b33f7d2c9062b552611d33405daa1563836df5a5539b4683bc2ea5935b6a9862  weyl_alias_scaling_probe.json
    74349b147bd2f3f3021249fcd3e8a8e8091303fb6bd9fd8a1ce9e81721e79bdd  quadratic_phase_resonant_lag_probe.py
    96f27aae8e1c18768bd9ab15bc0a192343a20678ae586e592e77f786023723aa  quadratic_phase_resonant_lag_probe.json

Campaign direction: derive a global phase expansion through the order-one
correction, resolving all branches, Bragg matchings, the central region, and
turning points, then keep the actual two-index overlaps in the alias sum. A
principal Weyl law alone proves neither a target limit nor a wall.

## 2026-09-24 fixed-moment theorem checkpoint (15:48 UTC)

I completed a bounded analytic theorem on the same supplied Jacobi family:
the empirical spectral measures of (N_S) converge weakly to

    dmu(lambda) = 1_(0,4)(lambda) d lambda / (4 sqrt(lambda)),
    F(lambda) = sqrt(lambda)/2.

The proof fixes each moment (m) first, freezes the finite-range Jacobi
coefficients on a compact bulk interval, and writes the diagonal of (N_S^m)
as a finite sum over closed nearest-neighbor walks. Its limit is the zero
Fourier coefficient of
`nu(x,k)^m`, with `nu=4(1-x^2)sin^2(k/2)`. The exact endpoint row-sum bound
controls the excluded endpoint strips by their normalized rank fraction; the
strip width is then sent to zero. The limiting moments are exactly
`4^m/(2m+1)`, which identify the density on the compact spectral support. The
continuous strictly increasing CDF then gives the macroscopic quantile
profile (lambda_{j_S,S}	o4rho^2) if (j_S/(10S-3)	o rho), hence
`C*lambda/(4*S^2) -> rho^2`.

This closes the global empirical spectral distribution and quantile profile
for the conditional supplied matrix. It does not differentiate weak
convergence into adjacent-gap control, and the actual two-index readout remains
open. The resulting quadratic *macroscopic* phase explains the O(S) alias
scale but cannot be substituted termwise modulo (2pi): the best finite
quadratic fits in the retained diagnostics have order-one to multi-radian
residuals and change `q_S` by up to 0.0232. The narrow next obligation is
phase-accurate global quantization plus overlap-weighted summation of every
reciprocal alias.

Paired finite diagnostic:
`scripts/postmark_electric_principal_weyl_count_2026_09_24.py`; cache:
`logs/runner-cache/postmark_electric_principal_weyl_count_2026_09_24.txt`;
receipt: `outputs/postmark_moving_index_2026_09_24/principal_weyl_count_2026_09_24.json`.
It checks empirical moments 0 through 8 and sample CDF values at S=8,16,32,64,128;
it is corroboration only. The note is
`docs/POSTMARK_ELECTRIC_PRINCIPAL_WEYL_COUNT_BOUNDED_THEOREM_NOTE_2026-09-24.md`.
Current source remains 5171af0 over origin/main 0e6ad82. Root review found
the normalization, endpoint rank, moment identity, and quantile consequence
consistent; this is author-only, not the independent review or audit.
