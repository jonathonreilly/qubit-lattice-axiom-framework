# Goal

Unblock as much of the current audit surface as possible with source-note,
runner, and cache repairs only.

This branch does not change `docs/audit/**`, does not set audit status, and
does not add axioms. It prepares three repaired packets for independent review:

- Higgs-channel effective `N_taste`: synchronize with the current parent
  `u_0 = 0.877681381` input and rerun the channel table.
- Wilson-corrected `V_taste`: remove stale `+40 r^2/u_0^4` runner prose from
  the docstring/header while preserving the verified `60` coefficient.
- Observable-principle Shannon/Khinchin bridge: remove the arbitrary additive
  offset under exact additivity and align runner labels with what is actually
  computed.
