# Handoff

Branch target: `codex/koide-q-reduced-cycle-edge-20260618`

This PR repairs a source-graph cycle edge for the Koide Q-reduced carrier
physical-identification obstruction. The audit queue's cycle target says the
obstruction's co-cycle citation to the parent reduced-observable row should be
informational/see-also, not load-bearing, and that a source-graph repair pass
must strip or rewrite the markdown link before the cycle can clear.

What changed:

- The obstruction note now says the parent claim id is context-only trace
  metadata and not a load-bearing dependency.
- The purpose section no longer has a markdown link target to the parent note.
- A guard runner checks that the context-only wording remains and that the
  markdown dependency target is absent.
- Runner cache is refreshed.

What did not change:

- No audit ledger, audit queue, audit result, publication status, front-door,
  active review queue, or lane registry file was edited.
- No audit verdict or effective status is claimed.
- The physical charged-lepton reduced-carrier/readout bridge remains open.
- The `D_red = I_2` physical source-unit normalization remains open.

Exact next action: reviewer should inspect this as source-edge hygiene and, if
accepted, let the auditor/reviewer reprocess the source graph and cycle queue.
