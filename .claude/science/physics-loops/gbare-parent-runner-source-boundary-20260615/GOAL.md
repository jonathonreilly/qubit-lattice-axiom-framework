# Goal

Repair `g_bare_derivation_note` so the parent bounded route is source/audit
ready without runner failures caused by stale generated ledger state.

The repair does not attempt to convert the parent into an unbounded theorem.
It preserves the bounded surface and removes runner dependence on audit
verdict fields.
