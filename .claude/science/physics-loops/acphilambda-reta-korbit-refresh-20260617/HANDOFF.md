# Handoff

Branch: `physics-loop/acphilambda-reta-korbit-refresh-20260617`

This PR updates the ACPHILAMBDA R-eta narrowing packet after the K-orbit
determinant/orientation note became audited-clean at retained-bounded scope.
The old source note still treated that dependency as `audited_conditional`,
which made the ACPHILAMBDA row carry a stale conditional dependency.

What moved:

- The ACPHILAMBDA note now routes K/CPT sign-flip algebra through the
  retained-bounded K-orbit note.
- The honest-auditor soft spot now names the real remaining context: physical
  charged-lepton carrier/readout identification and carrier-gate realization.
- The runner adds source guards and now reports `TOTAL: PASS=51 FAIL=0`.

What did not move:

- `A_R-eta` remains admitted: h-class plus h-unit.
- The physical readout context remains supplied/open.
- The carrier-gate realization remains open.
- No audit ledger, audit queue, Tier-A registry, publication status, or
  repo-wide authority surface was edited.

Next action:

Open a ready review PR. The reviewer/auditor can decide whether this hash drift
is enough to re-audit the ACPHILAMBDA R-eta row with the K-orbit dependency
removed from its conditional perimeter.
