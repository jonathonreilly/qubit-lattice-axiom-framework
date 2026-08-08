# The parent note's operator preference is correct and its own diagnostic is inverted, under a far-field protocol on the tested operator family

**Type:** repair packet (positive on the physics, demotion on the diagnostic)
**Claim type:** `bounded_theorem` for the far-field separation; `no_go` for the parent diagnostic
**Status:** repair — recovers the parent note's Bounded Claim 1 conclusion on a
different diagnostic, and shows its own diagnostic reverses the ranking

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: >
  The far-field separation is measured on a periodic lattice, which removes the
  Dirichlet boundary rather than modelling it. The inversion of the parent
  diagnostic is demonstrated on the parent note's own Dirichlet operators.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: >
  PR #5662 named the fixed-source far-field measurement as the successor. This
  cycle performs it. The result is positive on the physics the parent note
  claimed and negative on the evidence it offered, and both halves are measured
  rather than argued. Poisson's own far field is landed repo content and is used
  here only as a protocol control.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Runner: `scripts/physical_poisson_far_field_protocol_repair_cycle712_2026_07_27.py`

## What this cycle is

Parent: `self_consistency_forces_poisson_note` — `criticality: critical`, a root,
`transitive_descendants: 727`, `load_bearing_score: 18.092`.

Two prior cycles on this row were demotions. PR #5656 showed its two operator
discriminators are empty. PR #5662 showed its finite-size caveat cannot defend
its exponent, and named the successor:

> "a localized source of fixed extent and fixed total mass, with the exponent
> fitted at radii **outside** it."

This is that measurement. It reverses the direction of the arc: **the parent
note's conclusion is right.** Its evidence was not, and the reason is sharper
than either prior cycle found.

## What is new here, and what is not

Poisson's own far field is **already landed repo content**. Both
`LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`
and `GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md`
establish

```text
G(r) = 1/(4 pi r) + [5/(32 pi)] K4(nhat)/r^3 + O(1/r^5)
```

on `Z^3`. **U1 is therefore a control, not a result** — it validates this
runner's protocol against content the repo already has, so the rival rows can be
trusted. What the repo does not have, and what this cycle supplies, is the same
measurement for the rival operators (U5–U8) and the demonstration that the parent
note's window protocol inverts the ranking (U2, U4).

## A. A fixed window recovers the landed asymptotic; a scaling window does not

Same operator, same boundary-free lattice, only the fit window differs.

**Fixed window, radii 4..10 (U1, control):**

| N | 32 | 48 | 64 | 96 | 128 | 192 |
|---|---|---|---|---|---|---|
| `beta` | 2.329 | 1.642 | 1.427 | 1.259 | 1.189 | **1.126** |
| `4πrG` at r=10 | 0.190 | 0.432 | 0.568 | 0.709 | 0.782 | **0.855** |

`beta → 1` and `4πrG → 1`, monotonically, matching the landed theorem.

**Scaling window, radii `N/16..N/4` (U2):**

The last three sizes agree to within `0.02` — it looks converged — and it is
converged to `beta ≈ 1.66` with `4πrG ≈ 0.65`. **A window whose radii scale with
the box never leaves the region where the periodic images matter, so it measures
a box property and reports it as a stable exponent.** That is worse than failing
to converge: it is a diagnostic that looks trustworthy and is wrong.

## B. The parent note uses a scaling window, and it inverts the ranking

`check_field_physics` fits `for dy in range(1, mid - 2)` with `mid = N//2`, then
masks to `r > 1` — window radii `2..N//2-3`, whose outer edge is a fixed fraction
of the lattice (U3). That is a scaling window in exactly the sense U2 measures.

Run on the parent note's **own Dirichlet operators**, with its **own window**
(U4):

| N | 16 | 20 | 24 | 32 | 40 |
|---|---|---|---|---|---|
| Poisson `beta` | 1.849 | 1.819 | 1.796 | 1.764 | 1.742 |
| biharmonic `beta` | 1.065 | 1.031 | **1.005** | 0.969 | 0.943 |

**The parent note's diagnostic scores the biharmonic rival as the Newtonian
operator** — `beta = 1.005` at N=24 — and scores Poisson at `≈1.8`. Under the
far-field protocol the truth is the reverse: Poisson is exactly `1/r` and
biharmonic is asymptotically flat.

The diagnostic is **inverted, not merely noisy.** That is why PR #5656 measured
the biharmonic rival as closer to the target on the self-consistent field: the
diagnostic favours it by construction.

## C. The rivals' true far fields

Fixed window, boundary-free, N up to 192:

| operator | `beta` | verdict |
|---|---|---|
| **unscreened Poisson** | **1.126 → 1** | Newtonian |
| biharmonic | `0.138 → 0` (`beta·N ≈ 26`, so `beta ~ 26/N`) | asymptotically **flat** — no decay at all |
| `1/r^2` kernel | `2.000000000` exactly | its own defining exponent, not 1 |
| local | no extended field (1 nonzero site) | no exponent to compare |
| screened, `mu^2 = 0.01 … 2.0` | `1.68, 3.10, 5.60, 7.39, 9.74` monotone | only `mu^2 = 0` is near 1 |

A vanishing exponent for biharmonic means **no decay**: its potential is
asymptotically constant, which is maximally un-Newtonian rather than nearly
Newtonian. And the screened sweep confirms the parent note's Test 4 conclusion on
a far-field diagnostic, consistent with PR #5656 R13.

So **unscreened Poisson uniquely gives the Newtonian exponent, with a margin of
order 1** (U8) — against the `0.156` that PR #5656 measured inside a finite-size
budget. The parent note's Bounded Claim 1 asserted exactly this preference. It
holds.

## D. But it cannot be obtained self-consistently

PR #5662's successor required a fixed localized source. The parent construction
cannot supply one (U9):

| N | 16 | 24 | 32 | 40 | 48 |
|---|---|---|---|---|---|
| normalized `RMS/N` | 0.3406 | 0.3190 | 0.3096 | 0.3046 | 0.3014 |
| un-normalized `RMS/N` | 0.5288 | 0.5172 | 0.5119 | 0.5090 | 0.5072 |
| un-normalized total mass | `4.19e6` | `9.37e9` | `2.22e13` | `5.46e16` | `1.38e20` |

Removing the per-layer normalization — the obvious repair — does **not** localize
the source. It spreads *further* (`RMS/N ≈ 0.51` against `0.30`) **and** the total
mass diverges by 14 orders of magnitude over this range. With the normalization
the source is scale-locked (#5662 S5); without it the amplitude diverges.

**Neither branch supplies a fixed localized source.** The far-field measurement
therefore requires an externally prescribed source, which abandons
self-consistency for the source term. That is a structural limit of the parent
construction, not a tuning problem.

## Claim ledger

| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |
|---|---|---|---|---|---|
| **thesis** | Under a far-field protocol the parent note's operator preference holds — unscreened Poisson uniquely gives the Newtonian exponent among the tested family, with a margin of order 1 — while the parent note's own diagnostic inverts that ranking, scoring the asymptotically flat biharmonic rival as the Newtonian one. | U1, U2, U4, U5, U6, U7, U8 | the parent note's operator family and its `check_field_physics` window `2..N//2-3` **[satisfied]**; periodic boundaries for the far-field rows, which remove rather than model the Dirichlet boundary **[supplied]**; a fixed window of radii 4..10 **[supplied]**; lattice sizes up to 192 **[satisfied]**; Poisson's `1/(4 pi r)` asymptotic as landed repo content used as a control **[satisfied]** | Shown: Poisson `beta → 1.126` with `4πrG → 0.855` under a fixed window; `beta ≈ 1.66` under a scaling window; biharmonic `beta → 0`, `1/r^2 → 2`, local no field, screened monotone; and under the parent window on the parent Dirichlet operators biharmonic scores `1.005` where Poisson scores `1.796`. Claimed: the preference is correct and the diagnostic is inverted. Not claimed: that Poisson is the field equation of the lane, that the periodic result transfers verbatim to Dirichlet, or any self-consistent statement. | any rival landing within 0.5 of `beta = 1` under the fixed window, or Poisson scoring closer to 1 than biharmonic under the parent window at any tested size |
| U1 | With the window held fixed and the box grown, Poisson's periodic Green's function reproduces the repo's landed `1/(4 pi r)` asymptotic. | U1; `LATTICE_GREENS_1_OVER_R_...` and `GRAVITY_LEADING_LATTICE_CORRECTION_...` as the landed target | periodic boundaries **[supplied]**; fixed window radii 4..10 **[supplied]**; the parent runner's own nearest-neighbour stencil, verified in U0 **[satisfied]** | Shown: `beta` falls monotonically `2.329 → 1.126` and `4πrG` rises monotonically `0.190 → 0.855`. Claimed: this validates the protocol. **Not claimed as new**: the target asymptotic is already landed repo content and this row is a control on the protocol. | `beta` failing to approach 1 or `4πrG` failing to approach 1 |
| U2 | A scaling window converges to a wrong value on the same operator and the same boundary-free lattice. | U2 | periodic boundaries **[supplied]**; window radii `N/16..N/4` **[supplied]**; sizes 32..192 **[satisfied]** | Shown: the last three sizes agree to `<0.02` at `beta ≈ 1.66`, with `4πrG ≈ 0.65`. Claimed: a scaling window reports a box property as a stable exponent. Not claimed: that every scaling window fails, only this family of them. | the scaling window also converging to 1.0 |
| U3 | The parent note's decay diagnostic uses a window whose radii scale with the lattice. | U3, programmatic string check of `check_field_physics` | the parent source at this commit **[satisfied]** | Shown: `for dy in range(1, mid - 2)` with `mid = N//2`, masked to `r > 1`, giving radii `2..N//2-3`. Claimed: the parent diagnostic is a scaling window. | a window with N-independent endpoints in the parent source |
| U4 | Under the parent note's own window on its own Dirichlet operators, the biharmonic rival scores the Newtonian exponent and Poisson does not. | U4 | the parent runner's own Dirichlet operators via `build_laplacian_sparse` **[satisfied]**; the parent window `2..N//2-3` **[satisfied]**; point source **[supplied]**; sizes 16..40 **[satisfied]** | Shown: biharmonic reaches `beta = 1.005` at N=24; Poisson never comes closer than `0.742` from 1. Claimed: the ranking is inverted relative to the true far field. Not claimed: that the Dirichlet far field equals the periodic one, only that the parent diagnostic's ordering is opposite to it. | Poisson scoring closer to 1 than biharmonic at any tested size |
| U5 | The biharmonic rival's far field is asymptotically flat, its exponent vanishing like `1/N`. | U5 | periodic boundaries **[supplied]**; fixed window radii 4..10 **[supplied]**; sizes 32..192 **[satisfied]** | Shown: `beta` falls monotonically to `0.138` with `beta·N` roughly constant near 26. Claimed: no decay asymptotically, hence maximally un-Newtonian. Not claimed: an exact closed form for the biharmonic lattice Green's function. | `beta` converging to a nonzero constant, especially 1 |
| U6 | The `1/r^2` kernel returns exactly 2 and the local operator has no extended field. | U6 | minimum-image kernel on a periodic box **[supplied]**; fixed window **[supplied]** | Shown: `beta = 2.000000000`, `R^2 = 1`; local gives 1 nonzero site from a point source. Claimed: neither can give 1. | either giving 1 |
| U7 | Within the screened family the exponent rises monotonically with the mass, so the unscreened case is uniquely near-Newtonian. | U7 | periodic boundaries **[supplied]**; fixed window **[supplied]**; N=192 **[satisfied]**; six `mu^2` values **[supplied]** | Shown: `1.10, 1.68, 3.10, 5.60, 7.39, 9.74` for `mu^2 = 0 … 2`. Claimed: only `mu^2 = 0` is near 1, confirming the parent note's Test 4 on a far-field diagnostic. Not claimed: a continuum Yukawa derivation. | a screened member landing closer to 1 than the unscreened case |
| U8 | Unscreened Poisson uniquely gives the Newtonian exponent among the tested family, with a margin of order 1. | U8, and U1/U5/U6/U7 for the individual values | the tested family is the parent note's, not the space of all operators **[supplied]**; periodic boundaries **[supplied]**; fixed window **[supplied]** | Shown: Poisson `abs(beta-1) = 0.126`; every rival further than 0.5. Claimed: the parent note's Bounded Claim 1 preference holds on this diagnostic. Not claimed: a uniqueness theorem over all local operators — the parent note's own caveat that this is a finite family remains correct and this cycle does not remove it. | any rival within 0.5 of 1, or Poisson further than 0.15 from it |
| U9 | Removing the per-layer normalization does not localize the source: it spreads further and the total mass diverges. | U9, and #5662 S5 for the normalized branch | the parent propagator at `phi = 0` **[supplied]**; the switchable reimplementation verified bit-identical in #5656 R1 **[satisfied]**; sizes 16..48 **[satisfied]** | Shown: un-normalized `RMS/N` in `[0.507, 0.529]`, above the normalized `0.30`, with total mass growing by `3.3e13` over the range. Claimed: neither branch supplies a fixed localized source, so the far-field repair needs an externally prescribed source. Not claimed: that no modification of the propagator could localize it. | the un-normalized RMS saturating at a fixed absolute value with bounded total mass |

## The strongest objection, and how it lands

> "You measured the rivals on a **periodic** lattice and the parent note is
> Dirichlet. Your headline separation is therefore not a statement about the
> parent note's construction at all."

Correct, and it is why the claim is split. The **inversion** (U4) is measured on
the parent note's own Dirichlet operators with its own window, so that half needs
no transfer. The **far-field separation** (U1, U5–U8) is periodic, declared as
such in the thesis row's hypotheses and in the status block. The two halves do
not need to share a boundary condition to support the conclusion: U4 establishes
that the parent diagnostic orders the operators opposite to their far fields, and
U1/U5 establish what those far fields are. A reader who rejects the periodic rows
still has U4, which alone refutes the parent note's evidence — it just no longer
recovers the parent note's conclusion.

A second objection worth stating: the Dirichlet fixed-window series I measured
separately (`beta = 2.633, 1.695, 1.466` at N=24, 32, 40) descends in the same
direction as U1 but far too slowly to converge at reachable sizes, because at
N=40 the boundary sits only twice the window's outer radius away. That is the
honest reason the far-field rows are periodic rather than Dirichlet, and it is a
limitation of the measurement, not a result.

## Scope, and what this cycle does not claim

- Not a claim that Poisson is the field equation of the lane. It is a claim about
  which member of the parent note's tested family has a Newtonian far field.
- **Not a uniqueness theorem over all local operators.** The parent note's own
  caveat — "this is not a uniqueness theorem: the code tests a finite operator
  family" — remains correct, and this cycle does not remove it.
- The far-field rows are periodic, not Dirichlet. U4 is Dirichlet.
- U1 is a control against landed repo content, not a new derivation.
- Nothing here is self-consistent: U9 shows the parent construction cannot supply
  the source this measurement needs.

## Standing of the three cycles together

| | claim | status after this cycle |
|---|---|---|
| #5656 | the two operator discriminators are empty | **unchanged and reinforced.** U4 explains *why* the biharmonic rival scored better: the diagnostic is inverted. |
| #5656 R16 | refused to claim any rival is the better operator | **vindicated twice.** #5662 S3 showed the ranking is extrapolation-dependent; U5 now shows biharmonic's field is flat, so the rival was never better. Had R16 taken the stronger reading it would have been wrong. |
| #5662 | the finite-size caveat cannot defend the exponent | **unchanged.** U3 adds the mechanism: the window scales, so it cannot converge to a far field. |
| parent Bounded Claim 1 | Poisson is the best-supported operator in the tested family | **conclusion recovered** on a far-field diagnostic (U8); its own evidence still does not support it. |

## Proposed revision to the parent note

Recorded for the review process; this cycle does not edit the parent note or any
audit-lane surface.

- **Bounded Claim 1** — the *conclusion* stands on a far-field diagnostic (U8).
  Replace its supporting evidence: cite a fixed-window far-field measurement
  instead of the self-consistent `beta` table, which orders the operators
  backwards (U4).
- **The `beta` diagnostic** — record that its window scales with the lattice and
  that it scores the biharmonic rival as Newtonian. It should not be used to rank
  operators.
- **Caveat 1** — as #5662 proposed, withdraw the distance-law citation. U2 adds
  the reason a scaling window cannot be rescued by larger lattices.
- **Test 4** — unaffected, and now independently confirmed (U7).

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: self_consistency_forces_poisson_note
target_blocker_text: >
  "missing_bridge_theorem: compare susceptibility with the matched
  point-to-point inverse-Laplacian kernel, normalize alternative-operator source
  signs consistently, and revise the note to the resulting finite numerical
  scope before re-audit."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem
next_trace_action: >
  The three-cycle arc on this row is complete: the discriminators are empty
  (#5656), the finite-size caveat cannot defend the exponent (#5662), and the
  conclusion is nonetheless correct on a far-field diagnostic while the parent
  diagnostic inverts it (this cycle). The remaining open item is not on this row:
  U9 shows the self-consistent construction cannot supply a localized source, so
  any future self-consistency claim in this lane needs a source term that is not
  the normalized propagator density. That is the next target.
```
