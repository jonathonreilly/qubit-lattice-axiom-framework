# Original independent source review

**Source disposition: PASS WITH BOUNDED CLAIMS, source only.** No material
finding was identified in this one coherent unit. This accepts the stated
conditional fixed-four-particle theorem for its supplied Hamiltonian. It is
not a landing PASS, an audit verdict, Nature-grade retention, or a physical
identification of that Hamiltonian. Final committed-head confirmation and
the combined current-main integration gates remain pending.

Reviewer session: `/root/native_four_particle_source_review`, dispatched as
`gpt-6-astra`, low. One review iteration; no author edits, commits, PR actions,
audit workers, audit application, or primary/helper science reruns. The
reviewer read the full current canonical note, both current supporting
proofs, both scripts, the actual same-model parent and necessary premise
authority. The author packet and previous check exposure were supplied;
this is independent mathematical review, not a blind experiment. Earlier
campaign checks and author preflights are not used as a substitute for it.

The original base and HEAD are `30a9461ee19a49b99fa6628fe942f08e504e8903`;
the original staged tree is `d4774b427e5c9ed059d64dd01bc5aefc636c261e`.
The index and working bytes agree, with no unstaged or untracked author
paths. All 134 original paths have explicit reviewer-owned dispositions in
`ORIGINAL_REVIEW.json`. That map is independently reconciled with Git's
no-renames delta and the author's inventory; the count is not the coverage
argument. The unchanged main parent and input hashes are bound there too.

## Mathematical reconstruction

The independent route was an analytic reconstruction in physical occupation
and positive-row spaces, followed by exact rational inspection of emitted
matrices. No scientific function from either proposed runner was imported.

1. **Full carrier and gradients.** The axial projector is `I-J/3`, whereas
   the four signed plane amplitudes use `J/4`. Subtracting the attractions
   from the directed occupied-neighbor count leaves the axial singlet with
   coefficient `2mu` and each plane orthogonal complement with coefficient
   `mu`. The remaining diagonal at a vertex is
   `1-m+m(m-1)/2=(m-1)(m-2)/2`, nonnegative for integer degrees. Thus the
   gradient estimate consumes only `S+W`; the diagonal term remains available
   simultaneously. This verifies the crucial use of the sum in (9), rather
   than adding two separate lower bounds on the same energy.

2. **Physical normalization and source duality.** An actual matching of four
   sites contributes twice in the ordered creator product. The prefactor
   `1/sqrt(2)` therefore gives `sqrt(2) U A U^T` on separated pairs. A
   symmetric off-diagonal basis matrix has both entries `1/sqrt(2)`. A
   physical orbit with `m` perfect matchings has `2m` ordered removal
   coordinates; assigning `r(S)/(2m)` yields the adjoint lift without a
   bosonic replacement. If no matching exists, a four-vertex graph either
   has an isolated vertex or is the three-leaf star, and the diagonal is
   at least one. These facts give the full compact-source dual estimate,
   including nonmatching sources.

3. **Capacity and completion.** On the Brillouin cube,
   `ell>=4|k|^2/pi^2`; integration of `pi^2/(4|k|^2)` over the containing
   radius-`sqrt(3) pi` sphere with measure `(2pi)^-3 dk` gives
   `g<=sqrt(3) pi/8`. Compact-source duality is enough for the finite
   zero-energy resolvent quadratic forms and Riesz representatives in the
   energy completion. It does not require an inverse bounded on all l2.
   Finite-support positive rows and continuous coordinate evaluations make
   the completion faithful. Applying the point capacity to every ordered
   field at its common hard-core pin gives
   `2a ||UAU^T||_HS^2/g=2a ||A||_HS^2/g`. No torus constant-mode inverse
   enters this infinite-lattice statement.

4. **Compact source and rational correction.** Removing a local edge from
   the incoming occupation polynomial leaves its uncrossed product plus
   precisely the two crossed products. Overlap instead deletes the
   uncrossed product. The listed candidate residuals exhaust those cases.
   The SOS adjoint can consequently generate nonmatching source outputs,
   which the code retains. Independently expanding the projectors gives
   the literal action coefficients `12 delta_ij-4` for axial words and
   `3 s t s' t'` for plane words; the respective onsite attraction factors
   are `-2,-1`, and the gradient stencil is `6,-1`. These agree with the
   code. The source builder's coefficients `8`, `3`, `12,-4`, and `3`
   follow by multiplying the same positive forms by 12, using a different
   algebraic route from its defect loops.

5. **Operator bound and upper form.** The positive occupation interaction
   is at most `12mu` in N=4. The pair map has norm squared at most two;
   the gradient has norm squared at most 12; resolving the six removed
   pairs gives `W<=144tau`. Hence the benchmark bound is 160. For any
   compact trial profile with residual `r`, the correction `-r/160`
   changes energy by `-2||r||^2/160+<r,Hr>/160^2`, at most
   `-||r||^2/160`. Substituting `H12=12H` and denominator `d` gives exactly
   `(1920 Qnum-Rnum^T Rnum)/(23040 d^2)`. For E1, the raw monomial vector
   is one-half of `(1,-1,1)` on `(u1^2,u1u2,u2^2)`; for T12 it is
   one-half on `v12^2`. The additional incoming factor two therefore
   leaves the code's one-half directional contraction. Exact inspection
   recovered both quoted fractions and checked all 225 symmetry entries,
   residual/upper numerator compatibility and positive rational LDL pivots
   of the emitted upper matrix. This last check is evidence consistency,
   not a second full source computation or an evaluation of T0.

6. **Local estimate and isolation.** Neumann point differences remove the
   constant mode. Counting nonnegative modes by their maximum coordinate
   yields at most `7r^2` per shell and the stated 448 bound for aspect
   ratio two. The enlarged-box volume and overlap bounds give
   `125 D+14000000 R^3 Egrad` for the close-triple count. Combining the
   pointwise `B_R<=4D+2F_R` with the simultaneous gradient bound is safely
   below the stated loose `28000322 R^3 H/a`. Pins are imposed on fixed
   annihilation outputs, so no number projector is commuted through an
   annihilator.

7. **Guarded frame and gap.** At fixed N=4, removing an isolated edge
   leaves its distant environment unchanged, proving the auxiliary
   annihilation identity on the actual isometric image. It does not claim
   canonical pair commutators. Guard disagreement has stencil width at
   most four; edges in the intervening isolation shell are disjoint. The
   forward-edge row incidences are bounded by 15. Poincare on mean-zero
   edge fields, together with the four high constant modes of S, controls
   the excited-edge occupation. Empty environment and two particles in
   five soft modes have rank `dim Sym^2 C^5=15`. The excluded-anchor
   bound applies separately to every pair orientation and hence to all
   entangled internal matrices. It gives an invertible Gram form and the
   physical complement gap without discarding momentum sectors.

8. **Schur/eigenvalue comparison.** In block form the complement is
   `C>=Delta`. For `0<=lambda<=theta`, the resolvent increment is bounded
   by `lambda C^-1/(Delta-lambda)`, and its sandwich is at most the
   trial block `theta`. Inertia of the block congruence consequently gives
   `lambda_j<=s_j<=lambda_j(1+theta/(Delta-theta))`. Since
   `theta=O(L^-3)` and `Delta=O(L^-2)`, the rescaled difference is
   `O(L^-1)`. All other momenta are in the complement. This justifies
   exactly fifteen low levels and the claimed sixteenth-level bound.

9. **Torus normalization and limit.** Odd-order translations act freely on
   four-sets because a stabilizer order divides four. Thus a normalized
   orbit basis has physical coefficients divided by `sqrt(V)`; the
   normalized frame has raw profile divided by `sqrt(V)` in that basis
   and divided by `V` on physical occupations. The constrained raw energy
   is `V S_L`, and contraction of two ordered matchings gives the limit
   proof's overlap identity with no extra factor two. The mean-zero
   discrete Sobolev estimate is uniform after the Poincare term is
   absorbed. Its point evaluation at the hard-core pin bounds the means;
   the separate S estimate controls high rows and, by exchange, columns.

10. **Both cutoff directions.** Away from the fixed collision core, the
    only matching exterior has three relative coordinates; nonmatching
    amplitudes have an l2 bound. On matching shells the logarithmic cutoff
    has `sum |delta eta|^3=O(J^-2)`. Holder with the l6 response bound
    yields squared row-commutator cost `O(J^-4/3)` and therefore energy
    error `O(J^-2/3)`. The construction cuts a single physical profile,
    preserving shared removal amplitudes. Periodizing the compact
    infinite response leaves a constraint error bounded by
    `r_+^(5/2)/V=O(L^-7/4)`, which the guarded frame corrects at smaller
    energy cost. The two variational inequalities imply norm convergence
    on every complex symmetric channel. The local-response corollary
    follows from the same energy-completion stationarity; it makes no
    full-l2 convergence assertion.

No target-equivalent open terminal lemma remains inside the stated domain.
The exclusions of zero parameters, small/even tori, growing R and growing
particle number are preserved. The many-pair and physical-boundary questions
are outside this theorem and have not been silently discharged.

## Evidence, premise, preservation and lens dispositions

- **CodeRunnerReviewer: PASS at source scope.** Both entire scripts were
  read. The only nonstandard runtime dependency is NumPy; repository runtime
  reads are the owned integer trial and imported helper. Literal input pins
  also bind all three proofs and the same-model parent. Official cache APIs
  report both caches fresh and both timeouts 180 seconds. The primary has
  three finite check families, not three analytic proofs. All nine final
  mutation failures were inspected at their actual assertions and their
  mutated-source hashes reconstructed; the nine pre-footer histories were
  similarly reconciled. Successful identical science was not rerun.
- **PhysicsClaimReviewer / ImportSupportReviewer: disclosed conditional
  model.** Tensor-product quantum states, expectation, basis, Hamiltonian,
  positive mu/tau, N=4, incoming channel normalization and periodic boundary
  conditions are explicit supplied mathematical inputs. The integer Xi is
  a variational proposal, not an accuracy premise or fitted physical value.
  No empirical comparator or physical species/phase/scattering identification
  is imported. Actual minimal axioms, registry procedure/data and all three
  registered primitive sources were read; none supplies these extra choices.
- **ProofObligationReviewer: CLOSED within supplied hypotheses.** The two
  companion proofs are current scientific source owned by the canonical
  claim, fully reviewed here, and must remain schema-2 supporting proofs.
  They are not historical/non-science exclusions or autonomous claims.
- **NatureRetentionReviewer: bounded conditional result only.** This review
  grants no retained status or unconditional framework/TOE consequence.
- **NoGoDisciplineReviewer: not triggered by the actual positive theorem.**
  The no-go skill and source rhetoric were inspected. Statements identifying
  omitted extensions do not claim all such routes fail; no wall-independence
  count or universal impossibility is asserted. The finite inverse example
  is a concrete unequal pair, not a general no-go. No N1-N8 success is
  invented.
- **LabelingConventionReviewer: PASS.** This is an algebraic/analytic
  operator theorem with supplied conditions, not a naming stipulation.
- **RepoGovernanceReviewer: PASS at source scope.** Source statuses stay
  conditional-support. The conformance restatement's proposed-retained-only
  wording conflicts with the owning CLAIM_STATUS allowance for conditional
  model results; preserving the latter is correct and does not propose
  retention. No parked owner premise is adopted. Historical author records
  are preserved with their historical meaning, not treated as present review.
- **Audit compatibility: source structure compatible; integration pending.**
  The actual primary imports the one helper. All three scientific docs are
  explicit inputs, and the note links its parent and two proofs. The sole
  audit-data delta is the allowed topology manifest: three added nodes,
  three added edges, no removed or rewired old node. Schema-2 proof ownership
  must be retained in integration; the graph alone does not confer it.
  No verdict, ledger, queue or effective-status payload is proposed.
- **Preservation:** no original existing science is removed or modified.
  The sole existing-file change is the generated topology acknowledgment.
  Historical preflight trees and records were checked against their actual
  Git objects; compressed historical captures roundtrip to their recorded
  raw hashes. The pre-footer scripts differ only in success output, and
  their scientific JSON agrees after removing resource measurements. The
  early canonical note's actual diff was read, including the squared-norm
  wording correction and added source/bound details. Each original path is
  preserved and mapped, including empty failure stdout files, prior evidence,
  historical scientific candidates and author metadata.

The review used the selected procedure revision
`7146fe17a76de41badcaca3c3c7cac6d11eb2a00`; its bound procedure bytes agree
with the science base. Relevant setup, unit, lens, compatibility, fixes,
receipt, physics-claim, proof/import, no-go and authority instructions were
read. No methodology source is changed, so MethodologySkillReviewer is not
triggered. Focused compile and all three diff checks passed; exact evidence
inspection is saved separately. There are zero material findings, fixes or
skipped known findings. Full pipeline count and integration retry count are
zero in this reviewer session. No combined validation or final commit is
claimed. The canonical claim remains for independently governed audit only
after authorized source integration.
