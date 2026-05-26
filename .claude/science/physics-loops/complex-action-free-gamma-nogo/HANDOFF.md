# Handoff

This PR repairs `complex_action_note`.

The previous row kept failing because the complex-action term
`S = L(1 - f) + i * gamma * L * f` introduced `gamma` by hand. The repair does
not try to hide that. It makes the current route a no-go certificate:

- finite gamma-sweep facts are preserved from the committed cache;
- `gamma=0` reduction and machine-small Born proxies are verified;
- positive gamma suppression is shown to be the imposed exponential weight;
- no horizon-specific observable or gravity-horizon theorem is claimed.

Independent audit should decide whether this is a retained no-go boundary for
the current complex-action packet.
