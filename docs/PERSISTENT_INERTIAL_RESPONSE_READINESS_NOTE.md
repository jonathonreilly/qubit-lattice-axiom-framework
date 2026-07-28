# Persistent Inertial-Response Readiness Note

**Date:** 2026-04-04 (status line rephrased + claim narrowed 2026-04-28 per audit-lane verdict; further narrowed 2026-05-24 per audit `or-keep-as-support` repair target to a non-derivational support/meta index only; 2D dependency scope narrowed 2026-07-28).
**Claim type:** meta
**Status:** non-derivational support / meta index only. This note is a cross-note pointer summary over the cited surrogate, relaunch, localization, threshold, backreaction, and multistage controls; it is not a theorem-grade closure, not a registered-runner readiness frontier, and not a tier-ratifiable readiness ranking. No persistent-mass theorem is asserted; no readiness theorem is asserted; no frontier ranking is asserted as a closure. The note's role is purely to index the cited authorities and record where they sit in this lane.

## Purpose (support/meta index only)

This note is a non-derivational support/meta index. It collects pointers
to the cited surrogate, relaunch, localization, threshold, backreaction,
and multistage controls so that a downstream reader can find them in
one place. It does not answer any closure question and does not assert
any readiness theorem.

The pointer-level observation that motivates the index is that the
listed authorities do not, on their own faces, present a persistent or
quasi-persistent inertial-response object on the retained ordered-lattice
family; this observation is descriptive, not derivational, and is owned
by the cited authorities themselves rather than by this index.

## What is already available

The nearest reusable pieces are:

- [`scripts/equivalence_principle_harness.py`](../scripts/equivalence_principle_harness.py)
  - amplitude-level invariance and packet-shape dependence on the retained
    3D ordered-lattice family
- [`scripts/two_body_momentum_harness.py`](../scripts/two_body_momentum_harness.py)
  - bounded two-body momentum comparison on the same family
- [`scripts/composite_source_additivity_harness.py`](../scripts/composite_source_additivity_harness.py)
  - weak-field same-site and disjoint-source additivity on the same family
- [`scripts/amplitude_packet_mobility.py`](../scripts/amplitude_packet_mobility.py)
  - older packet-motion machinery on a different rectangular/DAG lane
- [`scripts/gravity_pulsating_source.py`](../scripts/gravity_pulsating_source.py)
  - older persistent-source exploration on a different rule-driven lane
- [`scripts/ordered_lattice_packet_reidentification.py`](../scripts/ordered_lattice_packet_reidentification.py)
  - localized packet re-identification control on the retained 3D ordered-
    lattice family
  - frozen log:
    [`logs/2026-04-04-ordered-lattice-packet-reidentification.txt`](../logs/2026-04-04-ordered-lattice-packet-reidentification.txt)
  - result: the packet is easy to re-identify under weak fields on the tested
    family, with best-shift scores at `1.000` and width ratios staying near
    `1.000` for `valley-linear`; `spent-delay` broadens slightly but still
    remains re-identifiable on this bounded control
- [`scripts/ordered_lattice_quasi_persistent_relaunch.py`](../scripts/ordered_lattice_quasi_persistent_relaunch.py)
  - minimal ordered-lattice packet carry-through / relaunch probe on the same
    retained valley-linear family
  - frozen log:
    [`logs/2026-04-04-ordered-lattice-quasi-persistent-relaunch.txt`](../logs/2026-04-04-ordered-lattice-quasi-persistent-relaunch.txt)
  - result: compact packets can be re-identified and relaunched with high
    overlap (`0.9516` and `0.9839` on the frozen rows), but this is still a
    surrogate rather than a persistent-mass theorem
- [`scripts/ordered_lattice_quasi_persistent_relaunch_2d.py`](../scripts/ordered_lattice_quasi_persistent_relaunch_2d.py)
  - 2D cross-family sanity check for the same surrogate idea
  - frozen log:
    [`logs/2026-04-04-ordered-lattice-quasi-persistent-relaunch-2d.txt`](../logs/2026-04-04-ordered-lattice-quasi-persistent-relaunch-2d.txt)
  - result: the surrogate idea is family-generic enough to remain useful, but
    still only as a bounded control
- [`scripts/quasi_persistent_relaunch_probe.py`](../scripts/quasi_persistent_relaunch_probe.py)
  - smallest support-compression probe on the retained ordered-lattice family
  - frozen log:
    [`logs/2026-04-04-quasi-persistent-relaunch-probe.txt`](../logs/2026-04-04-quasi-persistent-relaunch-probe.txt)
  - result: moderate compression keeps the downstream response similar, but
    sharp localization fails and the best bounded surrogate still needs a broad
    support (roughly `196-225` sites on the frozen rows)
- [`scripts/mesoscopic_surrogate_backreaction_harness.py`](../scripts/mesoscopic_surrogate_backreaction_harness.py)
  - one-step source/backreaction extension of the broad surrogate lane on the
    retained 3D ordered-lattice family
  - frozen log:
    [`logs/2026-04-04-mesoscopic-surrogate-backreaction.txt`](../logs/2026-04-04-mesoscopic-surrogate-backreaction.txt)
  - result: the broad surrogate sources an additive weak field and supports
    bounded one-step two-body symmetry, but still only as a broad mesoscopic
    control object
- [`scripts/broad_surrogate_point_source_compare.py`](../scripts/broad_surrogate_point_source_compare.py)
  - 3D interpretive diagnostic comparing the broad surrogate source against an
    equivalent-strength point source on the retained family
  - frozen log:
    [`logs/2026-04-04-broad-surrogate-point-source-compare.txt`](../logs/2026-04-04-broad-surrogate-point-source-compare.txt)
  - result: on the tested retained 3D family, the broad surrogate behaves like
    a soft point source to high accuracy
- [`scripts/mesoscopic_surrogate_source_2d.py`](../scripts/mesoscopic_surrogate_source_2d.py)
  - 2D companion check for the surrogate-source idea
  - frozen log:
    [`logs/2026-04-04-mesoscopic-surrogate-source-2d.txt`](../logs/2026-04-04-mesoscopic-surrogate-source-2d.txt)
  - result: the source stays stable as a mesoscopic control, but its breadth
    still materially changes the response amplitude on the retained 2D family
- [`scripts/mesoscopic_surrogate_threshold_2d.py`](../scripts/mesoscopic_surrogate_threshold_2d.py)
  - implementation-specific evaluation of 19 requested 2D support rows
  - frozen legacy log:
    [`logs/2026-04-04-mesoscopic-surrogate-threshold-2d.txt`](../logs/2026-04-04-mesoscopic-surrogate-threshold-2d.txt)
  - result: all 19 requested `topN` rows pass two programmed stability gates
    for the source-identity-pinned implementation; the result does not identify
    a retained 2D framework family, cover unlisted supports, or establish the
    absence of a threshold

## Pointer-level open list (descriptive, not a closure)

For reader orientation only, the cited authorities individually describe
test-particle-regime controls (amplitude-level invariance, packet
re-identification, weak-field additivity, surrogate-source diagnostics,
support/threshold sweeps, and so on). None of the cited authorities, on
its own face, currently presents a single retained object on the
ordered-lattice family that simultaneously:

1. remains localized enough to be treated as a persistent or quasi-persistent pattern
2. sources a field with a well-defined strength parameter
3. has an inertial response that can be measured separately from ordinary
   test-particle steering

This is an index-level reading of the cited authorities, not a theorem
or closure: the absence of a single such object inside the indexed set
is owned at the level of the cited authority statuses, not at this
note's level.

## Per-authority pointer summary (descriptive, not a closure)

The bulleted summary below is reader-orientation-only commentary on the
cited authorities' own stated scopes; it is not a re-derivation, not a
readiness frontier, and not a tier-promotable ranking. Each bullet only
restates what the cited authority itself records:

The current Newton-selection lane is now strong enough to say:

- amplitude-level equivalence is frozen
- same-family momentum is frozen
- same-family additivity is frozen

But it is **not** strong enough to say:

- persistent-pattern inertial mass has been produced or measured

So the one-parameter-mass step remains open.

The new packet re-identification control narrows the blocker slightly:

- localized packets on the retained ordered family do stay recognizable after
  propagation
  - that makes a future inertial-response experiment plausible
  - but the control does **not** by itself produce a persistent pattern with a
    separately measurable inertial mass

The relaunch probe narrows the blocker further:

- the quasi-persistent surrogate survives re-identification well enough to be
  relaunched
- the relaunch overlap is high enough to be interesting
- but we still do not have a self-maintaining object that carries its own
  inertial mass in the model

The compression probe narrows it further:

- the surrogate only remains faithful when the support is still mesoscopic
- the best bounded surrogate is broad, not sharply localized
- that is progress beyond the readiness note, but still not persistent-mass
  closure

The 2D control suggests this is not a one-off 3D artifact:

- the compressed surrogate survives on a second ordered-lattice family too
- that makes the control more credible
- but it still stops short of a persistent-mass experiment

The broader relaunch probe sharpens the remaining gap:

- moderate compression is tolerable
- sharp compression is not
- so the missing inertial-response object is still not in hand

The source/backreaction extension sharpens it further:

- the broad surrogate can now source a weak additive field
- one-step two-body symmetry stays at the sub-percent level on the tested 3D
  rows
- but this still only closes a mesoscopic control object, not a localized
  persistent mass

The 3D vs 2D source diagnostics keep the boundary honest:

- on the retained 3D family, the broad surrogate behaves almost like a soft
  point source
- on the retained 2D family, the same source idea stays stable but its breadth
  still matters materially for the response amplitude
- so the surrogate-source lane is real, but still bounded and family-sensitive

The multistage probe sharpens the positive side:

- on the retained 3D family, the broad surrogate survives a second sourced
  response stage with high best-shift score and a stable centroid-shift scale
- so the mesoscopic source lane is now more than a one-step curiosity
- but it is still broad-control physics, not localized persistent-mass closure

The 2D two-stage companion sharpens the family-generic side:

- the broad surrogate also survives two sourced-response stages on the
  retained 2D family
- so the mesoscopic-source picture is not just a one-family 3D quirk
- but it still remains a bounded control picture rather than a persistent-mass
  theorem

The fixed 2D support-list computation adds one finite pointer:

- all 19 requested `topN` rows pass the two programmed stability gates for one
  source-identity-pinned implementation
- those requests contain 17 distinct normalized source profiles because
  `topN=49`, `64`, and `81` saturate the same 49-bin profile
- this does not close a threshold question for a retained 2D framework family
  or for any unlisted support value

The constrained 3D compact-family sweep sharpens it again:

- compact Gaussian and tapered compact families can survive explicit
  support/capture floors on the retained 3D `h = 0.5` family
- but they still do not beat the broad `topN` control on the admissible
  score/capture tradeoff
- so merely excluding degenerate point-like winners does not reopen the
  retained coarse 3D family

The constrained 3D annular / hollow / tapered sweep sharpens it one more time:

- no admissible non-degenerate annular, hollow, or tapered ellipsoid family
  beats the broad `topN` frontier on the retained 3D `h = 0.5` family
- so that family now looks closed as a broad-source control lane rather than a
  hidden sharp-localization lane

The cited authorities individually record, as their own stated scopes:

- the fixed 2D threshold fixture reports only that all 19 requested `topN`
  rows pass its two programmed gates, with no retained-family or unlisted-row
  threshold conclusion
- on the retained 3D `h = 0.5` family, the cited compact-floor and
  annular/hollow sweep authorities individually report that no admissible
  non-degenerate family beats the broad `topN` control on those cards
- on the retained 3D `h = 0.25` family, the cited constrained-localization
  authority individually reports that the broad `topN 196` control is
  not beaten under its support/capture floors
- the cited localized source-response sweep authority individually reports
  that smaller source objects can remain admissible without beating the
  broad `topN 196` control on its retained card
- the cited surrogate authorities individually note the breadth/strength
  trade for compact versus broad sources

This is a per-authority pointer summary; it does not assert a
cross-authority frontier theorem and does not assert any closure of the
localization lane at this note's level.

## Pointer to follow-on work (descriptive only, no priority ranking)

For reader orientation, the cited authorities individually leave open the
construction of a retained object that simultaneously satisfies the three
test-particle-versus-pattern conditions enumerated above. This note does
not prioritize, sequence, or rank any candidate follow-on experiment, and
does not assert which (if any) of the cited lanes is the right next step;
those judgments are owned at the level of the cited authorities, not
this index.

## Audit boundary (2026-04-28)

Audit verdict (`audited_failed`, leaf criticality):

> Issue: The retained-style readiness synthesis imports a large set
> of surrogate, relaunch, localization, and threshold artifacts, but
> those named support rows are not all audit-clean; they include
> bounded/unaudited notes, audited_conditional rows, and audited_failed
> rows such as `MESOSCOPIC_SURROGATE_THRESHOLD_2D_NOTE`,
> `LOCALIZED_SOURCE_RESPONSE_SWEEP_NOTE`,
> `MESOSCOPIC_SURROGATE_COMPACT_FLOOR_SWEEP_NOTE`,
> `MESOSCOPIC_SURROGATE_ANNULAR_TAPERED_SWEEP_NOTE`, and
> `MESOSCOPIC_SURROGATE_H025_CONSTRAINED_LOCALIZATION_NOTE`. Why this
> blocks: a canonical retained readiness/frontier summary cannot be
> ratified from inputs that are not themselves audit-clean.

The note has been re-tiered to `support` (cross-note readiness index).

## Audit boundary (2026-05-24 — narrowed to support/meta index only)

This revision addresses the generated-audit repair target:

> missing_bridge_theorem: add a registered runner or explicit bridge
> theorem that asserts the readiness/frontier criteria from audit-clean
> dependency rows, or keep this note as a support/meta index only.

This revision takes the second branch of the repair target. The status
line, Purpose section, Minimal blocker → "Pointer-level open list"
section, the Safe read → "Per-authority pointer summary" rephrasing, the
former "localization frontier" / "Best next experiment" sections
(replaced by a non-prioritizing "Pointer to follow-on work" section),
and the "What this note does NOT claim" list are rescoped so that this
note is explicitly a non-derivational support/meta index only. The note
no longer asserts a readiness frontier, a structural ranking among the
cited authorities, a "best next experiment" prioritization, or any
theorem-grade closure on the persistent / quasi-persistent
inertial-response lane. No registered runner is added, no bridge
theorem is added, no new mathematics is introduced, and the audit
dependency repair links section is unchanged.

## What this note does NOT claim

- A persistent-mass theorem.
- A readiness theorem of any tier.
- A theorem-grade closure on the persistent / quasi-persistent
  inertial-response lane.
- A frontier ranking, ratifiable comparison, or priority ordering among
  the cited authorities.
- A registered-runner readiness criterion.
- That any of the cited surrogate / relaunch / localization /
  threshold notes are audit-clean, individually or jointly.
- That this note's status can be promoted on the back of the cited
  authorities' statuses.

## What would close this lane (Path A future work)

A tier-promotable readiness frontier would require, at minimum, both:
(a) auditing or repairing each cited authority first, and (b) a
registered runner or explicit bridge theorem that asserts the readiness
criteria from audit-clean dependency rows. This note is not that runner
and is not that bridge theorem; it remains a support/meta index only.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `MESOSCOPIC_SURROGATE_COMPACT_FLOOR_SWEEP_NOTE.md` (downstream sweep note;
  backticked to break cycle-0187 through compact_floor -> localization_sweep
  -> quasi_persistent_relaunch_probe -> ordered_lattice_packet_reidentification
  -> this_note)
- `LOCALIZED_SOURCE_RESPONSE_SWEEP_NOTE.md` (downstream sweep note;
  backticked to break cycle-0186 through localized_source -> h025_constrained
  -> annular_tapered -> this_note)
- `BROAD_SURROGATE_POINT_SOURCE_COMPARE_NOTE.md` (downstream surrogate note;
  backticked to break newborn cycle through this_note -> broad_surrogate ->
  ordered_lattice_packet_reidentification -> this_note)
- `MESOSCOPIC_SURROGATE_ANNULAR_TAPERED_SWEEP_NOTE.md` (downstream sweep note;
  backticked to break newborn length-2 cycle through this_note <->
  annular_tapered)
- `MESOSCOPIC_SURROGATE_H025_CONSTRAINED_LOCALIZATION_NOTE.md` (downstream
  sweep note; backticked alongside siblings for consistency)
- `MESOSCOPIC_SURROGATE_BACKREACTION_NOTE.md` (downstream surrogate note;
  backticked alongside siblings for consistency)
- `MESOSCOPIC_SURROGATE_MULTISTAGE_NOTE.md` (downstream surrogate note;
  backticked alongside siblings for consistency)
- `MESOSCOPIC_SURROGATE_THRESHOLD_2D_NOTE.md` (downstream surrogate note;
  backticked alongside siblings for consistency)
- [mesoscopic_surrogate_threshold_2d_note](MESOSCOPIC_SURROGATE_THRESHOLD_2D_NOTE.md)
- [localized_source_response_sweep_note](LOCALIZED_SOURCE_RESPONSE_SWEEP_NOTE.md)
- [mesoscopic_surrogate_compact_floor_sweep_note](MESOSCOPIC_SURROGATE_COMPACT_FLOOR_SWEEP_NOTE.md)
- [mesoscopic_surrogate_annular_tapered_sweep_note](MESOSCOPIC_SURROGATE_ANNULAR_TAPERED_SWEEP_NOTE.md)
- [mesoscopic_surrogate_h025_constrained_localization_note](MESOSCOPIC_SURROGATE_H025_CONSTRAINED_LOCALIZATION_NOTE.md)
- [broad_surrogate_point_source_compare_note](BROAD_SURROGATE_POINT_SOURCE_COMPARE_NOTE.md)
- [mesoscopic_surrogate_backreaction_note](MESOSCOPIC_SURROGATE_BACKREACTION_NOTE.md)
- [mesoscopic_surrogate_multistage_note](MESOSCOPIC_SURROGATE_MULTISTAGE_NOTE.md)
