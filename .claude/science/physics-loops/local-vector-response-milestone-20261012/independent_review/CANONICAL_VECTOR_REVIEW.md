# Independent review of the canonical local vector response milestone

2026-10-12. Reviewer session: `/root/direct_field_check`. This continues the
original independent proof check in the same session. The parent remains the
scientific author. This is a focused source review, not a formal audit,
retained-grade decision, integration gate or permission to land.

**Source disposition: accepted unchanged within the stated conditional
theorem.** I found no material mathematical, provenance or output-handling
correction needed in the frozen eleven-file addition. The supplied action
realizes the stated homogeneous static response with three positive-energy
propagating fields and finite front speed. It does not establish a nonlinear
gravitational theory, a physical background direction, or observational
acceptance. Those limits remain explicit in the canonical source.

## Frozen scope and complete coverage

The reviewed base is `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`; the reviewed
head is `68a7fa78907c2737e9f850679ba5a1c8db0df819`, tree
`884e265476be4febb1744735dbb49cc2968d2736`. At entry the working tree was clean.
The original delta contains eleven additions and no changes or deletions of
preexisting main paths. The locally available `origin/main` equals the frozen
base. This confirms preservation at that exact main snapshot; it is not a
claim about a future remote or integration tree.

I read the complete canonical note and runner, all five packet metadata notes,
the complete IO-control and raw-run receipts, all fields and all 64 numerical
rows in the scientific sidecar, and the complete canonical cache. This is
47,234 bytes of original changed source/evidence. All eleven working-copy
files matched the frozen Git blobs at capture and after the controls.

The [source manifest](source_manifest_v1.json) records each path, exact SHA-256,
Git mode/blob, base absence and complete local byte snapshot. The
[reviewer-owned dispositions](original_dispositions.json) cover every original
path, with its judgment, recovery location and unchanged final path/hash.
The [original binary diff](original_delta.patch) is also preserved. These maps
were generated and checked by this reviewer, not inferred from a file count
or supplied author verdict.

The load-bearing canonical identities are:

| Source | SHA-256 |
|---|---|
| Canonical theorem note | `12a23ea9bafeac2ade4afffb1d9bd27bacc5da7915c3148543a4fc45edcf979e` |
| Canonical runner | `03af913f6eedbfa710dc752cbb0fb8fa1c1a78e198e9e2658e6c4d40a38b1b5b` |
| Declared-note cache fingerprint | `282714dce24892a4b1102fa5950b1b66843fb552b4d999a0abbb9259ae6b1c68` |

The canonical runner reads no scientific data file or repository science
helper. It uses NumPy, SciPy and SymPy for synthetic mathematical controls.
Its paired note is a declared package-integrity input; it is not parsed into
the numerical answers. The supplied physical readout, constant unit direction,
quadratic action, positive parameters and decaying/retarded boundary choice
are disclosed hypotheses. No measured, fitted or framework-derived value is
silently imported.

## Original campaign mapping and reuse

The original argument lives in the campaign's
`gravity/solar_kernel_inversion/direct_vector_response_completion` packet.
Its complete protocol, note, runner, result and previous independent report,
programs and receipts are preserved byte-for-byte under `snapshots/campaign/`.
The earlier constrained-dynamics note is also preserved there as context.
Original full paths and hashes remain in the manifest; portable local
snapshots remove dependence on the originating worktree.

| Canonical content | Original content and disposition |
|---|---|
| Theorem note | `DIRECT_VECTOR_COMPLETION.md`, SHA `0fb24c2072b5fcac16b991d8a29b6999531edfb6bc1041b73afb1cd377685ca8`; complete action/energy/static/retarded proof preserved. |
| Scientific runner functions | `direct_vector_check.py`, SHA `6205aa512256262fc1d10e6b854773d2a20f177825a82459fb1b2bde63189ce1`; `symbolic`, `real_green_fourier` and `numeric` have exactly identical location-independent ASTs. |
| Scientific sidecar payload | Original `evidence_v1/RESULTS.json`, SHA `d3210caf5904bcdf4997b04156645745444b413590b3264d5bccd5cd68cd123c`; the entire `symbolic` and `numerical` objects are equal. New identities/environment/family metadata are checked separately. |
| Independent proof and controls | Original `VECTOR_COMPLETION_REVIEW.md`, SHA `8fc03fa3df92265b086c4688eaddcd49b37cbf9dd5b9e9eef9eeb6e02c2bb2ae`, plus its pinned independent calculations; reused only for unchanged mathematics under the same hypotheses. |
| Packet metadata, CLI and cache | New canonical packaging, read and checked in this review. |

The complete [note difference](campaign_to_canonical_note.diff) was inspected.
The port explicitly requires G>0, removes an undefined illustrative speed
symbol in favor of uncalibrated alpha, removes numerical fitted-response
examples, and adds standalone scope/reproduction metadata. The omitted fitted
examples are recoverable and do not supply a premise of the theorem.
The strict D>0 restriction and lack of nonlinear/empirical inheritance remain.
No proof was discarded or replaced by a reference to inaccessible campaign
results.

## Independent mathematical conclusion

Direct differentiation of the supplied action gives

`alpha u_tt - mu Delta u - beta grad div u = -4 pi G rho e`,

with `mu=1/N`, `beta=1/D-1/N>=0`. The kinetic Hessian is
`alpha I/(4 pi G)>0`; it supplies three unconstrained configuration degrees
of freedom. With gravitational-potential units for u, alpha has units of
inverse speed squared. The source sign yields the attractive isotropic
potential. The positive field energy has work term `-rho phi_t`; it does
not bound matter plus interaction energy.

For `Q(H)=mu|H|²+beta(tr H)²`, take the test gradient `n outer v`. Its
quadratic-form norm is `mu|v|²+beta(n.v)²`, and its bilinear pairing with H
is `v.T_n`. Cauchy-Schwarz and the arithmetic-geometric mean inequality give
the sharp local bound `|S.n|<=c_L energy`, where
`c_L=1/sqrt(alpha D)`. A longitudinal wave jet saturates it. Integrating
this inequality gives the compact **full-vector-data** domain of dependence;
the local projection e.u and its derivatives cannot enlarge support.
Compact scalar readout alone, with unspecified other initial fields, is not
being claimed sufficient.

Independently diagonalizing `B=mu k² I+beta k k^T` gives two transverse
eigenvalues k²/N and one longitudinal eigenvalue k²/D. Therefore

`B^-1=(N P_T+D P_L)/k²`,

`e.B^-1.e=(N k_perp²+D k_parallel²)/k^4`.

This matches elimination of the displayed two-potential static equations at
every nonzero wave vector. Fourier inversion gives
`B^-1_ij(x)=[(N+D)delta_ij+(N-D)n_i n_j]/(8 pi r)` and the stated negative
point potential. The point source is a distributional fundamental solution,
not a finite-energy smooth-data example.

The retarded Fourier oscillator solution has `G(0+)=0` and
`G_t(0+)=I/alpha`, fixing the unit impulse normalization. Independently in
real space, each scalar shell `delta(t-r/c)/(4 pi c² r)` has spatial mass t.
Solving `Delta h=g_L-g_T` gives

`r² h'=t[H(r-c_L t)-H(r-c_T t)]/(4 pi)`.

Its Hessian supplies the intervening tensor term and the two signed surface
jumps. The conversion `delta(t-r/c)=c delta(r-c t)` gives the printed powers
of wave speed. Equal shell masses cancel the external Poisson field, so the
complete tensor vanishes outside the c_L cone. Omitting the intervening term
destroys the Fourier and static match. Its time integral, including both
fronts, reproduces the full static inverse. The Fourier zero-frequency
integral is understood in the retarded/Abel sense, not as an absolutely
convergent undamped sine integral.

These conclusions were established independently in the original full proof
check, whose exact source/evidence is copied here. Its raw angular/radial
tensor quadrature did not import the author runner or use its spherical-Bessel
reduction. It covered the 16 distinct parameter tuples behind the 64 scalar
rows, three extra tuples, four impulse/second-moment tensor controls and four
sharp flux fixtures. Maximum tensor error was 8.3441e-15; maximum discrepancy
with the saved scalar receipt was 8.5080e-15. The entire canonical scientific
payload and function bodies match those checked inputs, so no unchanged
complete scientific battery was rerun merely to change its path.

The isotropic case D=N gives three scalar wave equations and a vanishing
intervening term. D approaching zero gives unbounded c_L and is excluded at
D=0. The new three-field action lies outside the earlier restricted
two-scalar kinetic classification. The canonical theorem does not need that
classification as a premise and makes no universal negative statement about
all possible completions.

## New canonical controls and observed failures

The reviewer-owned [check program](check_canonical_port.py) and
[complete receipt](canonical_port_checks_v1.json) preserve the actual checks.
Seven isolated in-memory formula mutants were rejected by assertions:
swapped static projector coefficients, reversed dynamic sign, reversed static
point-kernel anisotropy, doubled intervening time integral, wrong Bessel sign,
removed intervening tensor term, and transverse speed substituted for the
outer flux speed. Author files were never modified.

The separately preserved original independent controls also reject seven
false alternatives by independently derived identities/counterexamples:
including an error invisible on both axes, wrong radial delta Jacobian,
reversed source coupling and an unmatched projector's explicit off-cone
tail. Thus the port checks do not rely solely on replaying the author's own
positive assertions.

Eight synthetic result fixtures confirm the new aggregation rejects a false
symbolic flag, an incomplete transform set, equality at the strict transform
threshold, an incomplete flux set, a flux-bound violation, an incomplete
off-cone set, a false off-cone flag and equality at the strict mutation
threshold. The reported ten families are six symbolic families plus four
numerical families, not an invented count of individual continuum claims.

The CLI/publishing path was tested with the pinned synthetic-science payload
in place of scientific execution. Repeated normal output was identical;
`--json` round-tripped to the complete pinned result; the same-invocation
sidecar equaled stdout; an existing sidecar raised `FileExistsError` and
remained byte-identical. Changing the working directory to the review folder
left repository-root resolution correct. These fixtures are explicitly IO
evidence, not new scientific executions.

The 60-second constant is a timeout declaration for the execution consumer;
it is not an internal alarm in the CLI. The raw recorded run used that cap,
exited zero in 1.3532 seconds, and recorded 10 passing families. The source
hash and independently reconstructed declared-input fingerprint match the
canonical cache. Cache stdout/stderr match the raw streams including the
cache writer's extra framing newline. The numerical sidecar reports maximum
transform error 1.7764e-15 and is identical to the prior scientific payload.

The first reviewer control attempt stopped at my overly strict comparison
which omitted that cache framing newline. The exact failed reviewer source
and explanation are retained in `reviewer_attempt1_source.py.snapshot` and
`reviewer_attempt1_failure.json`. Inspection of the cache writer resolved it;
no author-source change was needed. The corrected reviewer run passed in
2.3677 seconds. This operational correction is not a failed scientific test.

## Boundaries of this source disposition

All five packet notes consistently describe supplied conditional mathematics.
They do not promote the candidate action to a framework primitive, claim
retention, assert an empirical match, or issue an audit verdict. The proof
obligations of the stated constant-coefficient theorem close; the physical
identification and nonlinear source/background/matter completion remain open.
The runner's numerical diagnostics supplement the analytic proof and are not
proofs of continuum causality on their own.

This review accepts all eleven original paths unchanged. There are no material
findings awaiting repair and no skipped confirmed defect. There were zero
author edits, commits, full-pipeline executions, integration retries, model
changes, formal audits or galaxy calculations in this review. The inherited
reviewer configuration was not changed or relabeled. Unrelated campaign
results were not reopened. The original discovery deadline remains in force.

The later added receipt/manifest package still requires the requested final
identity and interaction confirmation. This report covers only the exact
original eleven-file milestone and the evidence explicitly listed above.
Combined integration validation and any landing remain the parent's separate
responsibility; no future head, main advance or uninspected manifest is
preapproved here.
