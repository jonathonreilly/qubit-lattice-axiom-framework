# Handoff

This PR is a source repair, not an audit verdict.

What changed:

- The `g_bare_constraint_vs_convention` note now declares both retained
  one-hop dependencies needed for its bounded algebraic step.
- `beta = 6` is explicitly scoped as a local Wilson evaluation input.
- A constraint-specific runner was added to avoid changing the shared
  retained upstream runner.

What reviewers should check:

- No new axiom was introduced.
- No ledger row was manually retagged.
- The audit pipeline resets the touched row to unaudited for independent
  re-audit.
- The parent `G_BARE_DERIVATION_NOTE.md` remains untouched.

Downstream implication if audit passes:

The parent constraint-vs-convention ambiguity gains a retained bounded
support route on the CN + WM + local beta surface. Downstream rows may cite
that bounded route only after independent audit accepts it.
