# Handoff — gauged-mass-equivalence

Campaign 2026-07-08. Owner: Jon. Supervisor: Claude (Fable), workhorse split
with codex workers. Predecessor: matter-mass-wep (verdict under owner
direction A: the framework yields mass). This campaign attacked that
campaign's named frontier #1: the mediator requirement from the
static-comparator no-go, on the record-preservation-forced covariant-hopping
class instantiated as the d=1 U(1) staggered lattice gauge comparator.

CAMPAIGN VERDICT: the separation clause of the success bar is met and gated;
the equivalence-identity clause is met only at fit-consistency level, with
the tautology-free identity test deferred to a named follow-up (level
crossings block the second-band identification). The mediator hypothesis is
supported: the static truncation of the same model is pinned far from
equivalence exactly as the sum rule requires, the full field-mediated
dynamics is not, and the difference is attributed to the pair-creation
channel (rank correlation 0.857).

## PRs in review order (each verifiable by its stated runner command)

1. #5066 block01 (stacked on #5065) — ED engine + validation.
   `python3 scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py`
   -> TOTAL PASS (~6s). Machinery only, no physics claim.
2. #5067 block02 (stacked on #5066) — separation measurement + campaign
   close. `python3 scripts/gauged_meson_mass_energy_equivalence_2026_07_08.py`
   -> TOTAL PASS (~15 min).

Nothing is landed; the review lane owns landing. Every claim is bounded off
the declared comparator import; the comparator is a bridge instantiation of
the forced interaction class, not a derivation of the gauged surface.

## What the campaign showed (plain language)

- The earlier no-go proved that no instantaneous interaction can put
  binding energy into a composite's inertia — binding must be carried by a
  dynamical field. The framework's own Record axiom already forces exactly
  that kind of interaction. This campaign built the smallest honest model
  of that forced interaction (a one-dimensional gauge theory solved
  exactly on the computer) and measured whether the field actually does
  the job.
- It does, in the precise sense measurable at this size: cutting the field
  fluctuations out of the model (keeping only the static two-body channel)
  leaves the bound pair's inertia wildly wrong — off the equivalence value
  by factors of two to twelve — while the full field-mediated dynamics
  sits at the equivalence line after accounting for the emergent speed of
  light, at every point that passes the finite-size validity discipline.
- The strongest tautology-free positive: the emergent speed of light
  measured independently from two different particle species agrees to a
  few percent at every coupling. Different masses, same light cone — the
  equivalence-principle flavor of the result.
- Honesty items, recorded in the note rather than hidden: the simplest
  single-particle equivalence ratio is forced toward 1 by the fitting
  algebra itself and is therefore labeled a consistency check, not
  evidence; the stronger two-band identity test could not be run because
  the second excited band cannot yet be reliably tracked across momentum
  sectors (its levels cross); one strong-coupling grid point excluded
  itself via the finite-size validity gate.

## Post-campaign frontier (named for the next campaign)

1. Operator-tagged band identification, then the two-band identity test
   (M2/M1)(E01/E02) = 1 — the tautology-free equivalence identity this
   campaign designed but could not gate. Highest-value next step on this
   comparator.
2. Noether energy-current source identification in the window (inherited
   from matter-mass-wep frontier #2) — unchanged, still the supplied step
   for the gravitational source.
3. Scaling-window push of the gauged comparator: weaker coupling and
   larger N (the emergent speed trends to 1 as g weakens; the window
   statement wants that limit quantified with the same validity
   discipline).
4. Smaller: d=3 composite lift; unequal-mass composite gates.

## Resume

Read STATE.yaml. The campaign is closed; both PRs await the review lane.
Any follow-up starts a fresh loop pack (frontier items above), not a
continuation of this one.
