# No-Go Discipline Checklist

Target negative claim: on the two declared fine-H finite harnesses, the old
plane-ray and unregularized 2D/3D Gaussian ray formulas do not derive the
literal first-order detector-centroid response. This is not a no-go against
geometric optics, coherent 3D propagation, a finite source core, or a different
observable.

## N1 — Alternative route enumeration

| Route | Attempt | Why it does not rescue the declared bridge | Honesty marker |
|---|---|---|---|
| Old asymmetric plane finite-path gradient | compute the endpoint-matched exact ray integral on both supplied paths | target-constant-free slopes change by `0.282053262`, while the rebuilt adjoint slopes at supplied, historically tuned `beta=0.8` change by `0.002093528` | ATTEMPTED |
| 2D Gaussian angular ray mixture | integrate the plane-ray response over `exp(-beta theta^2)` | a zero-impact ray lies inside every declared angular family and gives `I~2/b_eff`; the one-sided integrals diverge | ATTEMPTED |
| 3D Gaussian angular ray mixture | use the old positive `theta_y` marginal with its `cos^2(theta)` factor | the marginal is strictly positive at the same zero-impact pole, so it does not regularize the integral | ATTEMPTED |
| Centered finite-path surrogate | replace the literal asymmetric path by a centered segment | the geometry is not literal and its short-path regime-transition prediction is falsified by [`LENSING_FINITE_PATH_EXPLANATION_NOTE.md`](../../../../docs/LENSING_FINITE_PATH_EXPLANATION_NOTE.md) | RULED OUT BY PRIOR |
| Literal full-path and remaining-distance gradient reductions | integrate the supplied field gradient, optionally with a detector lever arm | the retained negative-boundary packet computes shallower slopes and does not obtain the detector adjoint | RULED OUT BY PRIOR — same linked note |
| Nonnegative scalar-potential path/layer reduction | reproduce the detector response with nonnegative `1/r` weights | the distinct fixed-harness signed-centroid multipole obstruction in `LENSING_CENTROID_MULTIPOLE_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md` requires signed cancellation | RULED OUT BY PRIOR for that distinct scalar-potential class; context only |
| Exact signed-adjoint edge response | derive the actual source derivative and detector sensitivity | this succeeds as the literal finite-harness response but is not a rescue of the ray formula; it is the preserved positive route | ATTEMPTED |

Two live constructions are deliberately outside the negative scope: a
finite-core/principal-value ray model and a coherent 3D amplitude/adjoint
limit. They may define new models and are named in N6/N7.

## N2 — Wall-independence audit

Collapsed wall set:

- `W_shape`: the plane finite-path law has the wrong cross-path four-point
  shape response for the two declared detector-centroid harnesses.
- `W_integrability`: the old unregularized Gaussian ray expressions do not
  define ordinary angular expectations.

| Pair | Closing first automatically closes second? | Closing second automatically closes first? | Independent? |
|---|---|---|---|
| `W_shape`, `W_integrability` | no — a new observable map could fix the plane shape without defining the singular mixtures | no — a core/PV prescription could define the mixtures without making their shape equal the adjoint response | yes |

The signed-adjoint identity is evidence used to evaluate `W_shape`, not a third
independent wall. The raw wall count is therefore collapsed to two.

## N3 — Hidden-wall scan

The target note and runner were searched for `we assume`, `by construction`,
`as is standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.

- No load-bearing hit uses one of those phrases to import physics.
- "supplied finite harness" is an explicit admitted finite-model domain, not a
  claim that the minimal axioms derive the transfer rule or parameters.
- Elementary calculus, finite sums, and OLS definitions are proved or encoded
  directly.
- The adjoint identity is both re-derived in the note and recomputed in the
  runner; the linked adjoint note is a retained witness, not a hidden premise
  supplying the four response values.
- The source position, `H`, `beta`, family, seed, drift, restore, transverse
  half-width, phase scale, connection cutoff, regularizer, impact window,
  literal endpoint, and detector functional are all exposed finite-harness
  inputs.

No hidden admission was promoted, so the two-wall set in N2 is unchanged.

## N4 — Residual matching

| Witness | Witness residual | Current residual | Match? | Use after check |
|---|---|---|---|---|
| [`LENSING_ADJOINT_KERNEL_NOTE.md`](../../../../docs/LENSING_ADJOINT_KERNEL_NOTE.md) | identify the literal first-order centroid as a signed adjoint edge sum rather than a local ray kick | identify the response against which the old ray formulas are tested | yes | load-bearing identity, also rebuilt by primary runner |
| [`LENSING_FINITE_PATH_EXPLANATION_NOTE.md`](../../../../docs/LENSING_FINITE_PATH_EXPLANATION_NOTE.md) | centered finite-path surrogate is not the literal detector-centroid explanation | exclude centered/literal gradient rescue of the ray bridge | yes, for that surrogate family | prior-route witness |
| `LENSING_CENTROID_MULTIPOLE_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md` | nonnegative scalar-potential `1/r` path/layer reductions cannot equal the fixed signed centroid functional | old plane-gradient and Gaussian-gradient formulas do not derive the two fine-harness centroid laws | not exact for the `b/r^3` gradient primitive | cross-cycle context only; not used to prove `W_shape` or `W_integrability` |

The non-matching scalar-potential witness is explicitly dropped from the
load-bearing proof. Both current walls are independently established by the
primary runner and note derivations.

## N5 — Rhetoric audit

### "The ray law is not the detector-centroid derivation"

- Per-formula: tested by deriving the plane scale law and the signed-adjoint
  functional.
- Per-impact parameter: computed at `b={3,4,5,6}` only.
- Per-path: computed at `T_phys={7.5,15}` only.
- Per-family/seed: Fam1, seed 0 only.
- Per-refinement: `H=0.25` only.
- Continuum/lattice-wide: not tested and not claimed.

The note therefore says "on the two supplied finite harnesses," not that no
ray limit can ever reproduce any framework readout.

### "The Gaussian expressions are not ordinary expectations"

- Per-formula: proved for the displayed unregularized 2D weight and old 3D
  positive marginal.
- Per-impact parameter: the theorem applies whenever the zero-impact angle is
  inside the chosen chart; the runner checks this for `b={3,4,5,6}`.
- Per-regularization: no negative claim is made against a finite core, PV,
  diffraction prescription, or coherent amplitude construction.
- Physical 3D/lattice-wide: not tested and not claimed.

The broadest rhetoric in the source is limited accordingly.

## N6 — Partial-closure path scan

- A symmetric Cauchy principal value can assign a finite number, but it is an
  added prescription and does not repair `W_shape` automatically.
- A finite source core can make the angular expectation absolutely integrable;
  its core law and scale would be explicit finite-model inputs needing a new
  bounded theorem and an import-retirement test.
- A coherent 3D construction can derive forward amplitudes, source derivative,
  and detector adjoint. It is a legitimate positive route and is explicitly
  outside the no-go.
- The exact signed-adjoint edge law already partially closes the positive lane
  on the supplied finite harness; it is the central result preserved by this
  block.
- No labeling convention or vocabulary change can make the two displayed
  functionals equal, and the note does not say a new axiom is required.
- The primitive registry was checked. Scale-reference, kinetic-isotropy, and
  realized-state primitives supply none of the missing transfer, source,
  detector, core, or coherent-3D laws and are not classified as walls.

## N7 — Steelman

A hostile reviewer can reasonably argue that the no-go attacks an
over-literal ray mixture: a physical beam never samples a point singularity
incoherently. Starting from the coherent complex propagator, a controlled
stationary-phase/WKB limit with a finite source profile and the detector
centroid carried through the adjoint could generate an effective ray law whose
core scale removes the pole and whose detector lever arm changes the naive
`b/L` response. The exact adjoint identity in
[`LENSING_ADJOINT_KERNEL_NOTE.md`](../../../../docs/LENSING_ADJOINT_KERNEL_NOTE.md)
is the strongest authority for that counter-route because it exposes precisely
the phase and detector weights a proper limit must retain.

This steelman is convincing against a global no-go. It does not defeat the
shipped claim, which is restricted to the old plane function and the old
unregularized 2D/3D angular expressions on two supplied harnesses. The coherent
finite-core construction remains open and is the exact positive successor.

## N8 — Cross-cycle echo

- The earlier centered finite-path wall was not retired by more ray fitting; it
  was narrowed by the exact signed-adjoint observable. This block applies that
  same successful mechanism directly.
- The nonnegative scalar-path wall was bypassed by allowing signed
  detector-adjoint coefficients. This block preserves that bypass and does not
  generalize the scalar no-go to signed weights.
- The beta-sweep near-ray point was later unstable under refinement. This
  block does not use sweep instability as proof; it supplies the stronger
  pole/existence theorem and leaves coherent regularization open.
- No similar prior wall found in the loop ledgers was retired merely by a
  convention change; observable construction, signed weights, or a new
  regularized model were the substantive mechanisms, all considered here.

## Gate result

`PASS` for the narrowly scoped negative claim. All N1-N8 checks are answered;
the live coherent/core-regularized routes are excluded rather than foreclosed,
the two walls are independent, and the non-matching multipole witness is not
used as load-bearing proof.
