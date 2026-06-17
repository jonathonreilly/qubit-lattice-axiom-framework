# Handoff

This branch repairs the `staggered_dirac_kinetic_class_two_component_exclusion`
source edge. The finite CAR obstruction was already strong; the audit blocker
was that the row still treated the unaudited realization-gate note as the
authority for the check-18 rival/residual context.

The branch now defines and rebuilds `D_2c` directly, removes the realization
gate from YAML upstream dependencies, and adds runner firewalls so the source
edge stays self-contained. The gate remains a downstream consumer/context
only.

Reviewer should inspect the source science and decide whether this is enough
to re-open/re-audit the conditional row. This branch is not an audit verdict,
ledger mutation, or status landing.

Ready PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4286
