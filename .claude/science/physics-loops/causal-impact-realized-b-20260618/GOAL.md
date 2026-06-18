# Goal

Repair the `causal_impact_parameter_note` audited-failed row by making the
source packet fit against realized source-detector impact parameters rather
than nominal target labels.

The repair is source-side only. It does not edit audit ledgers, queue files,
publication effective-status surfaces, lane registries, or front-door status.
