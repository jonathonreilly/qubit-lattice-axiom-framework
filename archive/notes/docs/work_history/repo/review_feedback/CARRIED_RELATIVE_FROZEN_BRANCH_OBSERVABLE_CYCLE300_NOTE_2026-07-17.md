# Carried relative frozen branch and observable — Cycle 300 (2026-07-17)

Authority: none
Audit: unset
Constitutional effect: none

## Decisive question and answer

Can training `L=3,4` alone freeze one nonzero-momentum carried eigenbranch and
one proper-cubic scalar observable, then predict Green-shape behavior on
declared held-size `L=5,6` without per-size adaptive coefficients?

The result separates two questions.

1. **Branch tracking closes constructively on the declared finite search.** A
   fixed axis momentum, normalized contact-block fingerprint, and
   training-fitted dimensionless phase trend identify the same held eigenpair
   under three branch trackers. Fingerprint overlaps exceed `0.91`, and both
   held selector-score gaps are above `0.21`.
2. **The frozen scalar observable does not pass the declared held Green-shape
   gate.** Its overlap drops from training values near `0.880` and `0.545` to
   about `0.340` at `L=5` and `0.120` at `L=6`, below the frozen `0.50` gate.

This is a route-specific predictive-observable failure on one tracked branch,
not a failure to find the branch and not a broad no-go. The result creates no
axiom pressure.

The executable is
`scripts/carried_relative_frozen_branch_observable_cycle300_2026_07_17.py`.

## Training-only freeze

The physical update is the Cycle-298 actual carried relative block in the
one-matter `Q=N_e+N_f=1` domain. Cycle 300 fixes the nonzero total-momentum
index to the axis representative `(1,0,0)` for every size. Its direction under
proper-cubic frames is the full axis shell; no preferred physical axis is
claimed.

Only training `L=3,4` participates in the freeze. Nine supplied target windows
return eight sparse eigenpairs each. Every size first gets a spectral candidate
pool using only forward phase, pole margin, eigen-residual, returned-window
local gap, and eigenvalue deduplication. The held candidate pool has no adaptive
projection. Adaptive scalar analysis enters only when training candidate pairs
are scored, and after a held eigenpair has already been selected for the
fixed-versus-adaptive benchmark. Training candidate pairs are scored by

```text
S_pair = F_contact
         exp(-|p_3-p_4|/0.12)
         sqrt(O_adapt,3 O_adapt,4),

p_L = eigenphase / first-pole-phase(L).
```

Here `F_contact` is the phase-agnostic overlap of the normalized first `42`
relative-block amplitudes: six internal-excitation directions plus the `36`
matter/field direction pairs at relative contact. This contact-block
fingerprint is analysis structure, not a physical measurement observable.

The winning training pair has

```text
p_3 = 0.8646393127548384
p_4 = 0.8707133009541764
fingerprint overlap = 0.8887154631614543.
```

The pair freezes:

- the phase-aligned average contact-block fingerprint;
- the affine two-point fit `p(L)=a+b/L`;
- one fixed proper-cubic scalar coefficient vector, obtained by phase-aligning
  and averaging the two training adaptive coefficient vectors; and
- every window, threshold, and tracker width.

The coefficient vector acts on the same/opposite/perpendicular direction-pair
orbit contractions. There is no held-size coefficient adaptation.

## Frozen branch rule and held test

For a held candidate, the primary score is

```text
S_track = F_template exp(-|p-p_predict(L)|/0.05).
```

Two alternate branch trackers are also executed: fingerprint overlap alone and
phase-trend distance alone. All three select the same candidate at both
declared held sizes. Thus the branch choice is not being rescued by the held
Green comparator or by the frozen observable score.

The spectral results are dimensionless spectral data only:

| `L` | domain | eigenphase | `p(L)` | predicted `p(L)` | fingerprint overlap | tracker gap | returned-window eigenvalue gap |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | training | 0.905448 | 0.864639 | 0.864639 | 0.971781 | 0.658986 | 0.0386872 |
| 4 | training | 0.732330 | 0.870713 | 0.870713 | 0.971781 | 0.693782 | 0.0423931 |
| 5 | declared held-size | 0.640527 | 0.924991 | 0.874358 | 0.933629 | 0.278901 | 0.00195135 |
| 6 | declared held-size | 0.552656 | 0.943605 | 0.876787 | 0.912234 | 0.218034 | 0.0147557 |

### Branch crossings and gaps

These gaps expose rather than hide the crossing boundary. No exact
crossing occurs among the returned candidates at the selected windows, and the
three finite trackers agree. The runner does not exclude a crossing between
sampled sizes, outside the supplied windows, or under a different continuation
parameter. It therefore establishes a finite candidate-family identity, not an
analytic infinite-volume eigenbranch theorem.

The eigenphase and its normalized phase fraction are not physical energy, not
a rate, and not mass. No bridge earns any such interpretation.

## Fixed-versus-adaptive residual comparison

The frozen vector is evaluated without refitting. The adaptive column is an
analysis-only upper benchmark recomputed on the same selected eigenstate; it
does not participate in held branch selection.

| `L` | fixed weight | fixed contact | fixed overlap | fixed residual | same-state adaptive overlap | adaptive residual |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 2.816e-3 | 0.362422 | 0.880199 | 0.489491 | 0.889066 | 0.471029 |
| 4 | 2.872e-3 | 0.065582 | 0.545455 | 0.953462 | 0.551554 | 0.947044 |
| 5 | 1.924e-3 | 0.026527 | 0.339573 | 1.149284 | 0.659474 | 0.825259 |
| 6 | 1.563e-3 | 0.313867 | 0.120371 | 1.326370 | 0.153089 | 1.301469 |

The fixed projection remains above its supplied weight floor and below its
contact maximum at held sizes. The failed condition is specifically the
`0.50` Green-shape overlap gate. At `L=5`, same-state adaptation materially
improves the score; at `L=6`, even the same-state adaptive span is weak. The
Cycle-298 per-size global adaptive tournament can select a different `L=6`
eigenstate, which is exactly why Cycle 300 does not call the present result a
universal absence statement.

The comparator shift remains residual-matched to each selected eigenphase for
evaluation. It is not independently scale-fitted, but it is supplied analysis
structure and not a predicted physical source kernel.

## Proper-cubic covariance

Every one of all 24 proper-cubic frames is executed. At `L=3`, the runner
checks operator intertwining between the axis representative and every rotated
momentum index. At held `L=5,6`, it checks the rotated selected eigenstates, the
rotated contact fingerprint, and the frozen fixed-coefficient scalar profile.

Because same/opposite/perpendicular are the complete simultaneous
direction-pair orbits, the one fixed coefficient vector is a proper-cubic
scalar choice. Frame covariance does not make that supplied observable
physically preferred; it only removes a preferred-frame defect.

## Lawful domain and deletion controls

At `L=3`, the nonzero-`K` lift spans the complete relative basis of its one
discrete momentum sector. It is an isometry and satisfies
`G_full E_K = E_K G_K`. The `K=0` block agrees exactly with the predecessor
carried update. `L=2` and fractional momentum indices are rejected.

This is basis-spanning inside the declared one-matter `Q=1` sector. It is not a
test of leakage into other `Q` sectors and not a full-Fock compiler.

At the `theta=0` endpoint, none of the four selected finite-coupling
eigenpairs is retained unchanged. This is a coupling-dependence/deletion
control for the selected eigenpairs, not deletion of the update and not an
energy, rate, or mass statement.

## Supplied structure inventory

Load-bearing supplied structure is:

1. the Cycle-298 actual carried relative update and sparse-window machinery;
2. the one-matter `Q=1` sector and fixed nonzero axis momentum index;
3. training `L=3,4` and declared held-size `L=5,6`;
4. nine axis target fractions and eight returned eigenpairs per window;
5. phase/pole/residual/local-gap/deduplication-only spectral pools, with no
   held adaptive projection filter;
6. the `42`-amplitude contact-block fingerprint and its normalization;
7. branch-pair width `0.12`, held tracker width `0.05`, and fingerprint weight
   floor `10^-4`;
8. the two-point affine `1/L` phase-fraction fit;
9. the phase-aligned average of training adaptive coefficients;
10. same/opposite/perpendicular orbit normalization inherited from Cycle 298;
11. fixed overlap minimum `0.50`, contact maximum `0.60`, and projection-weight
    floor `10^-6`;
12. the residual-matched shifted-Green comparator used only for scoring; and
13. every numerical tolerance, deduplication rule, and finite domain.

The train/held partition is declared in the artifact, not a prospective
preregistration claim. The supplied fingerprint and coefficient vector are not
promoted to physical observables.

## No-Go Discipline Gate

The candidate broad negative is: “no fixed proper-cubic observable on a
continuing carried branch can produce a Green-like held response.”  The
present two-size test cannot establish it.

**Gate status: FAIL for the candidate broad negative; do not ship it.**

The retained result is one route-specific frozen-observable falsification on
one finite tracked candidate family.  No broad no-go is shipped.

### N1 — Alternative routes

| route | marker | disposition |
|---|---|---|
| combined fingerprint/phase tracker | **ATTEMPTED** | selects a separated held candidate, but the frozen scalar overlap fails; runner lines 530--560 |
| fingerprint-only tracker | **ATTEMPTED** | selects the same held candidates, so changing the tracker does not rescue this vector |
| phase-only tracker | **ATTEMPTED** | also selects the same candidates |
| global per-size adaptive search | **ATTEMPTED** | Cycle 298 finds other finite-volume witnesses, directly defeating universality |
| continuous-`K` full-state overlap continuation | **OPEN / UNTESTED** | may traverse avoided crossings and select a different analytic family |
| Riesz spectral-projector branch label | **OPEN / UNTESTED** | may define a stable subspace where a fixed observable behaves differently |
| transfer-matrix or coupling continuation | **OPEN / UNTESTED** | supplies another branch identity independent of the finite feature tracker |
| independently selected physical observable | **OPEN / UNTESTED** | a coupling or operational detector could choose a different proper-cubic contraction |

N1 fails for a no-go because at least four distinct constructive routes remain
open.

### N2 — Wall-independence audit

There is one failed acceptance condition, fixed Green overlap on this branch.
Branch identification, projection weight, contact fraction, and covariance
pass and are not inflated into separate walls.  With only `W_fixed_overlap`,
the unordered pair table is empty; there is no pair to call independent or to
collapse.  No multiwall or independence claim is made.

### N3 — Hidden-condition scan

Every supplied window, phase normalization, fingerprint, tracker width,
coefficient average, comparator, threshold, size split, and numerical
tolerance is inventoried above.  No continuum, physical-observable, energy,
rate, mass, gravity, or hidden prior-metric premise enters the test.

The literal rhetoric-trigger scan returned zero hits across the runner and
note.  This scan is a prose control, not a physics premise.

### N4 — Residual matching

| witness and file line | residual attacked | residual claimed here | match? |
|---|---|---|---:|
| tracker agreement/gaps, `scripts/carried_relative_frozen_branch_observable_cycle300_2026_07_17.py:530` | finite held candidate identity under three frozen trackers | branch selection succeeds | yes |
| fixed overlap rejection, `scripts/carried_relative_frozen_branch_observable_cycle300_2026_07_17.py:558` | one training-frozen scalar misses `0.50` on held `L=5,6` | route-specific observable failure | yes |
| same-state adaptive comparison, `scripts/carried_relative_frozen_branch_observable_cycle300_2026_07_17.py:563` | adaptive upper benchmark on the already selected state | universal mode absence | no; dropped as negative support |
| Cycle-298 adaptive witnesses, `scripts/carried_relative_extended_green_branch_hunt_2026_07_17.py:540` | per-size existence inside an adaptive scalar span | fixed-rule prediction | no; used only as counter-authority |
| nonzero-`K` lift, `scripts/carried_relative_frozen_branch_observable_cycle300_2026_07_17.py:713` | sector isometry/intertwining | Green shape | no; kept as domain validation only |

Cycle 298 and the nonzero-`K` lift attack different residuals and are not cited
as witnesses for the present negative.  After unmatched witnesses are
dropped, only the narrow frozen-vector rejection remains.

### N5 — Rhetoric and resolution audit

| resolution | tested | unresolved |
|---|---|---|
| eigenpair | one selected simple candidate per `L=3..6` | other eigenpairs and degenerate subspaces |
| branch | one finite axis-shell feature-tracked family | continuous `K`, coupling, or spectral-projector continuation |
| observable | one frozen scalar coefficient vector | other fixed proper-cubic contractions and operationally selected observables |
| size | training `L=3,4`; declared held `L=5,6` | further sizes and infinite-volume limit |
| semantics | dimensionless phase, fingerprint, normalized shape | energy, rate, mass, source, gravity, occurrence |

The only negative sentence is: “this frozen vector misses the held overlap
gate on this tracked family.”  No per-mode-universal, lattice-wide, or
framework-wide absence language is used.

### N6 — Partial-closure paths

Live non-axiom paths include a retained physical observable supplied by an
independent operational coupling, continuous-`K` continuation, a
spectral-projector branch definition, and a multi-size training fit followed by
new held sizes. Any could retire the present analysis-choice residual without
new physics axioms.

### N7 — Steelman

A hostile reviewer can correctly argue that the contact-block template is not
the eigenprojector and the two-point `1/L` fit is not analytic continuation.
Following a Riesz projector continuously in `K` or coupling could traverse the
finite avoided crossings and yield another branch on which a symmetry-fixed
single-orbit observable remains Green-like. Cycle 298 already proves that
other adaptively selected modes exist.  The strongest counter-authority is
`docs/work_history/repo/review_feedback/CARRIED_RELATIVE_EXTENDED_GREEN_BRANCH_HUNT_NOTE_2026-07-17.md:155`, which reports the declared adaptive witnesses and their selector freedom. This steelman is convincing, so a broad no-go would be premature.

### N8 — Cross-cycle echo

| earlier seam | retirement/search mechanism | resulting status |
|---|---|---|
| Cycle 297 selected stationary branch was contact-localized | widen spectral windows and momentum sectors; expose all three proper-cubic scalar channels | Cycle 298 finds finite adaptive mode-existence witnesses |
| Cycle 298 fixed held projections were weak | permit explicit per-eigenpair `CP^2` scalar adaptation | adaptive existence closes, but predictive observable remains open |
| Cycle 300 freezes one branch and scalar rule | remove held adaptation and compare three independent branch trackers | branch tracking survives; one observable prediction fails |

Because widening the spectral/observable selector retired earlier residuals,
continuous-projector and independently selected observable mechanisms must
remain live.  The cross-cycle echo therefore blocks a broad negative.

## Disposition and next test

The strongest result is a constructive finite branch tracker with a falsified
training-frozen scalar prediction. No source law or asymptotic `1/r` law is
earned. This is not gravity and earns no physical energy, rate, mass, no-go, or
axiom pressure.

The optimal next test is continuous-`K` or coupling continuation using a Riesz
spectral projector and explicit avoided-crossing audit, with one single-orbit
proper-cubic scalar contraction frozen before new held sizes are opened.

## Ledger effect

- `C_local` improves narrowly at the analysis interface: one finite
  nonzero-momentum candidate family now has a training-frozen, covariant
  tracker with held agreement. No physical observable or state compiler is
  added.
- `C_source` is unchanged: the training-frozen scalar fails its held
  Green-shape gate and no source law, normalization, or gravity bridge is
  supplied.
- `C_ref`, `C_num`, `C_wrap`, and `C_int` are unchanged.

No framework maturity score changes.

## Verification

```text
python3 -m py_compile \
  scripts/carried_relative_frozen_branch_observable_cycle300_2026_07_17.py

PYTHONPATH=scripts python3 \
  scripts/carried_relative_frozen_branch_observable_cycle300_2026_07_17.py
```

The final runner reports `SUMMARY: 10 passed, 0 failed`. Maximum covariance
residuals are `9.33e-16` for the `L=3` operator intertwiner, `8.77e-16` for
held rotated eigenstates, `1.99e-16` for held fixed profiles, `1.73e-16` for
held fingerprints, and `3.34e-16` for tracker-overlap invariance. The `L=3`
lift residuals are `6.95e-15` for isometry and `7.52e-15` for intertwining;
the `K=0` predecessor residual is exactly zero.
