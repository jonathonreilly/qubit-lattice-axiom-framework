# Independent review: finite Wilson transfer and normalized soft-loop transport

29 October 2026. The bounded mathematical claims are confirmed after three
narrow corrections. The physical Yang–Mills existence and mass-gap target
remains open. This is source review in a fresh restricted-input reviewer
context, requested as Astra/max; it is not cross-family review, an audit,
a retained-grade declaration, or a whole-PR landing approval.

The final scientific source is
[MASS_GAP_CONSTRUCTION_ASTRA.md](MASS_GAP_CONSTRUCTION_ASTRA.md), SHA256
`a5d31da82721607e0ba04fef84675706bd3f2c568644224cce7dc86b0bb968e2`,
at commit `0cf473e3ef0c96ad31f0ecb1443690486cfbedb8`.
The final runner SHA256 is
`f1ae35944486ac5b141fb7627ebdb629608af7b5ad095e268b45af86dcfbddbf`.
The original 503-line source, SHA256
`bc5be24f32bf9285ecab0140993eb9788c6f2736ecd9cbe91254d288cac79f8a`,
and original author controls remain at
`cdc877b0452bed2218e1cfdec79ef8fc2b4c27f5`.
Methodology and prior-art authority were read at
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`.

## Findings and affected-fix confirmation

1. **Oriented nonunitary means — normalization/domain clarification, fixed.**
   The original real-lambda instruction to use the adjoint gave the intended
   formula, but `M^(orientation)` could be misread as an inverse. The final
   paragraph following (14) explicitly defines the negative orientation as
   `M^dagger`, including `M=0`. Complex-lambda continuation keeps the same
   holomorphic scalar `f_lambda`; it does not conjugate lambda or that scalar.
   Direct Haar integration with noncentral, nonunit and zero quaternion means
   confirms the corrected convention. Replacing the adjoint by an inverse,
   or conjugating the complex coefficient, fails the reviewer controls.

2. **Finite-cycle implementation checks — runner BUG, fixed.**
   In the original runner, replacing the implemented four-link power `r^4`
   by `r`, or multiplying the implemented convolution eigenvalue by its
   representation dimension, still passed all 45 predicates. The separate
   named formula controls were disconnected from the implementation. Five
   other mutations correctly failed: omitted normalizer, omitted spatial
   factor, omitted Perron factor, wrong adjoint and dropped source-only log.
   The preserved [mutation results](checks/review_massgap_construction_mutation_results.json)
   record both surviving errors rather than hiding them.

   The repair compares the actual `cycle_transfer` output with a separately
   assembled coordinate-space operator: Gauss–Jacobi Haar integration,
   recurrence characters, raw character coefficients divided by dimension,
   four temporal links and both actual magnetic factors. Its ratio at
   beta=0.7 is approximately `0.000815159729885258`. The top-eigenvalue
   conversion `exp(beta)/c_0^4` correctly accounts for the two discarded
   field-independent normalizations. The repaired run has 47/47 passing
   predicates. This reviewer independently reran both formerly surviving
   mutations: each exits 1 at both new comparisons, with empty stderr.
   The wrong-power ratio is about `0.156509527014091`; the wrong-dimension
   ratio is about `0.0130033776800172`. The
   [same-context confirmation](checks/review_massgap_construction_fix_confirmation.json)
   binds the corrected source and exact mutation outputs.

3. **Order-eight coefficient — OVERCLAIM in one summary phrase, fixed.**
   Equation (18) identifies the order-eight coefficient. It does not prove
   that the actual Wilson covariance on its right is nonzero for every
   admissible loop pair. Section 3 now says “order-eight” rather than “first
   nonzero.” The formula, domain and proof are unchanged. The final source
   also distinguishes the original 45-check run from the repaired 47-check
   run and preserves the failed mutation evidence.

All three changes were confirmed in this same reviewer context. There are
no unresolved mathematical findings against the stated finite results.

## Independent proof assessment

**Finite Wilson transfer.** For a spatial edge x-to-y and temporal links h,
the temporal plaquette is `U_xy h_y V_xy^dagger h_x^dagger`. Its normalized
real trace equals the factor in `k(U,h.V)`. Integrating the independent
vertex h's therefore gives the actual Wilson temporal slab. Each adjacent
slab supplies half of every spatial plaquette weight. The omitted temporal
constant is exactly `exp(-beta |E_s|)` and cancels from eigenvalue ratios.
The projector is Haar averaging over the entire spatial gauge group;
it does not restrict the observable sector to plaquettes.

The positive tensor-character expansion gives strictly positive convolution
coefficients for every SU(N) irreducible representation when beta>0. The
Peter–Weyl eigenvalue is the coefficient divided by representation dimension.
The convolution commutes with the gauge projector. The gauge-invariant,
strictly positive multiplier is invertible on the finite compact space, so
the transfer is positive and injective on the full invariant Hilbert space.
Its continuous kernel is compact and strictly positive. The Rayleigh/modulus
argument yields a unique strictly positive top eigenvector. Spectral
calculus consequently defines a densely defined nonnegative logarithmic
Hamiltonian on that space. Nonconstant loop functions exist on the specified
cubic tori, and multiplication by the positive vacuum preserves density;
there is a nonzero excited sector with finite excited energies. The beta=0
rank-one endpoint is correctly excluded from this conclusion.

The Perron equation cancels the left magnetic factor only after retaining
the full denominator. With `nu proportional to A psi_0 dU`, the Doob kernel
is `K(U,V) nu(dV)/integral K(U,W)nu(dW)`. Bounds `exp(±beta |E_s|)` on K
therefore give minorization `exp(-2 beta |E_s|) nu`, without identifying nu
with the reversible measure `psi_0^2 dU`. Oscillation contraction applies to
every nonzero transfer eigenfunction divided by the vacuum: both are
continuous and the vacuum has positive minimum. Together with positivity
and compact spectral completeness this proves (9) for all invariant sectors.
The factor `a^-1` gives the stated physical time units. No uniformity in
volume or cutoff follows; the displayed lower bound tends to zero in the
stated limits. Its degeneration is not an upper bound on the actual gap.

The two-spin magnetic multiplier provides a valid counterexample to the
*general* kinetic-gap inheritance inequality. Its largest rescaled block
has eigenvalues tending to `1±r^2`, giving the claimed adverse ratio. It is
not an SU(N) counterexample. The ground-state semigroup estimate is also
correctly separated from the required finite-torus/continuum hierarchy.

**Normalized SU(2) filter and actual path means.** Writing `V` and `M` as
quaternions makes `w(V^-1 M)` their Euclidean inner product. Rotating M to
`r I`, SU(2) Haar becomes the uniform S3 law. Its second moment tensor is
`delta_ab/4`; its even scalar moments obey
`E[x^(2k)]/E[x^(2k-2)]=(2k-1)/(2k+2)`. These give the normalizer, its
logarithmic derivative, `I_2/I_1`, and the displayed coefficients. Division
by Z is essential. The limit at `M=0`, trace normalization, real and complex
orientation conventions, and `lambda=kappa/g_i^2` are consistent with the
actual Decision-4 kernel. The nonzero complex disk follows from the stated
uniform series bound on `Z-1`.

Conditional independence applies to distinct *coarse* random links under the
plain normalized joint measure. Multilinearity of the quaternion trace then
gives (15)–(17), with adjoints on negative orientations. A plaquette image
starts at `lambda^4 X_P/4^4`; every next correction is at least order six.
Both terms in the covariance therefore give (18) at order eight. The fine
law here is the original, fixed Wilson probability law, not a lambda-dependent
coarse effective action. Bounded path means and the common analytic disk
make the stated finite-loop remainder uniform in fine volume, beta and
separation. This uniform coefficient bound contains no separation decay.

The face-by-face fine lift in section 2.3 realizes the specified coarse links:
internal axial legs are identity and every straight length-L leg crosses one
corresponding face. Gauge averaging preserves the loop signs. The resulting
prior is singular and is correctly distinguished from a finite-beta Wilson
measure. Its positive-noise correlation refutes only the claimed kernel-only
clustering inference. Repeated-link products require the higher Haar moments,
as (20) states. Polynomial density supplies finite forward images; it does
not supply a controlled inverse source map.

**Source transport.** Integrating the normalized kernel in (21) returns the
original source partition function. At lambda=0 its entire logarithm is a
source-dependent constant in the coarse field, whose mixed derivative is
the original covariance. Dropping this term would change the observable.
For positive lambda, the two terms in total covariance use the reverse
conditional law, including its coarse-field-dependent normalizer. Coarse
clustering alone does not bound the conditional-covariance term. These are
exact identities; neither establishes source transport with decaying tails,
history-uniform returns or the missing infrared estimate.

The small-beta row count `18 beta` is consistent with six plaquettes per
four-dimensional link, three other links per plaquette, mixed oscillation
at most `4 beta`, and the normalized total-variation bound `tanh(beta)`.
It is an endpoint observation, not an extrapolation to a tuned continuum
trajectory or a comparison between stochastic time and physical time.

## Checks, coverage and limitations

[Independent criteria](checks/review_massgap_construction_precriteria.json)
were written before the author source/controls were inspected; the parent
brief had already disclosed the headline formulas and author check counts.
The independent implementation was written and executed before reading the
author runner. It uses actual 3^3 spatial-torus slab factors, coordinate-space
SU(2) quadrature, 38,400-point Hopf-coordinate Haar integration, explicit
S4' contour enumeration with 1,944 paired paths per coarse edge, and a
4,096-term Haar tensor sum for each oriented plaquette coefficient. It also
checks the source-only derivative for the actual one-plaquette Wilson law
after exact tree reduction, and uses a separately labelled finite scalar
model for the total-covariance control. The eight-link tensor identity is
pointwise in actual S4' fine fields; no sampled Wilson covariance is claimed.

The final [independent runner](checks/review_massgap_construction_independent.py)
and [output](checks/review_massgap_construction_independent_final.json)
have 50/50 predicates passing and empty stderr. The first attempt's 49/50
result is retained: sequential addition of the Haar second moment gave
`0.25000000000002337`, missing its fixed `2e-14` tolerance. Stable dot-product
summation gives `0.24999999999999994` with the same criterion. Original script,
stdout and stderr are preserved. A later final-version edit replaced a
bookkeeping-only scale equality with the actual nonzero eight-link
conditional coefficient comparison; earlier successful bytes also remain.
This is numerical diagnostic evidence, not an exhaustive lattice proof.

The coordinator's byte-identical original author replay is reused with its
source and manifest identities. All 45 original result rows, diagnostics,
runtime and resolution metadata are unchanged in the repaired result;
only the two independently checked comparisons are added. The successful
new run is reused from the coordinator's exact capture; the affected
mutation failures were independently executed here. No timeout, incomplete
run or failed numerical predicate is silently treated as scientific success.

The complete original source plus complete corrective diffs were read. Exact
read ranges and hashes are in the [read inventory](checks/review_massgap_construction_reads.json)
and the [final receipt](checks/review_massgap_construction_receipt.json).
PROOF header bookkeeping changed during coordination; the
[final read addendum](checks/review_massgap_construction_final_reads.json) verifies
that the consumed definitions are byte-identical and corrects their shifted
line ranges. PROOF is consumed only for its complete Setting and
Decision-4/D4-norm definitions; HIST only for the normalized chain definition
and conditional-independence section. SOURCE_LOCAL_RETURN is scope context,
not a premise. The complete four cited main-branch prior-art notes were read
for their actual claim boundaries, without adopting their uninspected
transitive proofs. The two cited status rows are unaudited at the pinned main.
No whole-PROOF, whole-source-return, whole-PR, ledger or theory certification
is implied by any whole-file hash in the inventory.

Only the abstracts were read for the
[Osterwalder–Seiler paper](https://www.sciencedirect.com/science/article/abs/pii/0003491678900398),
[Lüscher paper](https://link.springer.com/article/10.1007/BF01614090), and
[Shen–Zhu–Zhu paper](https://arxiv.org/abs/2204.12737).
They support the limited prior-art description, not an imported infrared
theorem. The direct DOI opens initially failed; publisher/arXiv access
recovered the abstracts. No global novelty conclusion is made.

## Claim and governance disposition

- Code/runner: the two implementation-validation defects are repaired and
  independently confirmed; finite diagnostic scope only.
- Proof obligations: CLOSED for the stated finite transfer, normalized SU(2)
  forward images and source identities under the supplied model. The uniform
  physical estimate and existence/reconstruction remain OPEN. Restating a
  uniform physical gap would leave the target-equivalent terminal gap intact.
- Imports/support: DISCLOSED. Wilson action, beta, regulator geometry and
  spacing, normalized soft kernel, and ordinary compact spectral/representation
  tools are explicit inputs. No observed mass, fitted target, new axiom or
  new primitive is used. The three registered primitives are neither missing
  walls nor suppliers of the required dynamics.
- Nature retention: bounded support only; no Nature-readiness or retained-grade
  statement. No MG0–MG5 row closes.
- Labeling: the positive claims are algebraic/analytic, not naming conventions.
- No-go discipline: **packet FAIL / stretch-attempt-with-honest-residual**.
  N1 has only three actual mechanism families; no five-family packet PASS is
  available. N2 asserts no independent-wall count. N3 inputs are disclosed;
  N4 prior-art residuals are not reused as universal obstructions. N5 finite
  resolutions are distinguished from the unexecuted continuum estimate.
  N6 the authority registry supplies no claimed dynamical bound. N7 a
  Wilson-specific block comparison or exact RG crossover with joint source
  control remains live. N8 the prior hard-fiber raw unit direction concerns
  a different map and does not foreclose the soft/rescaled construction.
  This procedural limitation does not falsify the positive finite results or
  the two explicitly quantified counterexamples, and is not repaired by
  inventing additional route families.
- Audit compatibility: no audit verdict/status or generated authority was
  changed. This is a bounded research-source confirmation, not full
  review-loop landing PASS. The five-route packet limitation and the
  coordinator's combined/current-main preservation gates remain separate.
  This reviewer ran no pipeline, audit worker, merge, commit, push or PR edit.
  Canonical publication placement and any future audit claim IDs are the
  coordinator's responsibility; none is fabricated here.

Review covered one unit, one complete initial pass and same-context affected
fix confirmations. Three findings were resolved; none is hidden or deferred
as a mathematical premise. The independent criteria, all original/mutated
executions, and source identities are preserved. The final scope remains
finite-volume and supplied-model support for the open physical target.
