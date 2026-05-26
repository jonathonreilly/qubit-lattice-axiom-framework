# Handoff

This PR repairs `action_normalization_note`.

The previous row depended on admitted convention bridges. The repair makes the
negative result explicit: the current finite propagator-Poisson packet does not
select `c` convention-free.

Preserved checks:

- all seven tested positive `c` values converge;
- rescaling rows with `c*G = 1` keep `c*phi_max` approximately invariant;
- PPN gamma readout is algebraically independent of positive `c` under
  `Phi = c*f/2`;
- massive-probe deflection increases with `c` but is not a null-ray c-fixing
  channel.

Independent audit should evaluate this as a no-go boundary only.
