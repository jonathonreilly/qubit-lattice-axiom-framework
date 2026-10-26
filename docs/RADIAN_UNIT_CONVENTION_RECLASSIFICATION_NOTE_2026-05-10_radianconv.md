# Radian and cycle coordinates: documentary correction

**Date:** 2026-05-10 (scope corrected 2026-10-25)
**Type:** meta
**Claim type:** meta
**Status authority:** independent audit lane; this source does not assign an audit outcome.
**Primary runner:** [`scripts/frontier_radian_unit_convention_reclassification_2026_05_10_radianconv.py`](../scripts/frontier_radian_unit_convention_reclassification_2026_05_10_radianconv.py)
**Cached output:** [`logs/runner-cache/frontier_radian_unit_convention_reclassification_2026_05_10_radianconv.txt`](../logs/runner-cache/frontier_radian_unit_convention_reclassification_2026_05_10_radianconv.txt)

## Coordinate correction

The SI radian is dimensionless: `[rad] = L/L = 1`. Dimensionlessness does
not fix a numerical angular coordinate. For the same angle,
`theta_rad = 2pi*theta_cycle`; equivalently
`cos(theta_rad)=cos(2pi*theta_cycle)`. A radian coordinate 2/9 therefore
corresponds to cycle coordinate `1/(9pi)`. A cycle coordinate 2/9 instead
corresponds to radian coordinate `4pi/9`. Holding the numerical value
2/9 fixed in both coordinates changes the angle; it is not a unit conversion
of the same angle. The primary checks these finite coordinate identities
separately from its documentary checks.

A supplied rational quotient `n_eff/d²=2/9` does not by itself identify
an angle. This note does not force that physical identification, claim a
measured phase, or certify the historical Brannen/probe24 argument.
It does not load PDG data. No theorem is promoted by this vocabulary correction.

## Withdrawal of the old rule

The former reclassification of P as mere bookkeeping, reduction of an
admission count from two to one, and embedded Review-loop rule are withdrawn.
They are historical claims, not instructions for future reviews. No retained
status, axiom sufficiency, physical closure, or impossibility follows from
this note. The audit lane retains authority over scientific status.

The former Brannen, Probe24 and campaign references are historical context,
not proof premises. The runner retains seven file-availability checks as
explicit documentary checks. It reads this note and the minimal-axioms note;
the latter's two wording observations are historical and unscored. Availability
and substring matches do not certify any cited argument. The minimal-axioms
text is not used to prove an angular coordinate or physical result.

Historical context paths (plain catalogue, not imported scientific premises):
`CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md`,
`PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08.md`,
`KOIDE_BAE_PROBE_PHI_FROM_Z3_CHARACTER_NOTE_2026-05-09_probe24.md`,
`KOIDE_BAE_PROBE_RADIAN_FROM_DIMENSIONS_BOUNDED_NOTE_2026-05-09_probe30.md`,
`KOIDE_BAE_30_PROBE_CAMPAIGN_NOTE_2026-05-09.md`,
`MINIMAL_AXIOMS_2026-05-03.md`.

## Evidence limits

Metadata, empirical-token absence and the inherited short-window negation
heuristic are lexical checks only, not scientific certification. The primary
resets its counters on each invocation and fails closed on missing declared
files. Original source, predicates, false authority routes and cache remain
in recovery; the cache is not fresh evidence for this revised source. This
is a documentary correction with illustrative coordinate calculations,
not a new physical theorem or a change to an audit verdict.
