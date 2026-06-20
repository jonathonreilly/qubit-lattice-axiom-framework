# Goal

Continue the audit-unblock campaign by making source-side repair branches and
review PRs only.

This block repairs `causal_impact_parameter_note` so the audit pipeline no
longer has to infer the claim class from migration hints. It does not run the
audit worker, apply a verdict, or push to `main`.

