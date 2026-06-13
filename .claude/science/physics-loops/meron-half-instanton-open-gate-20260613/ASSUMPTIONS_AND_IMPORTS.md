# Assumptions And Imports

Allowed imports:

- External BPST instanton half-action algebra in the cited 4D Euclidean SU(2)
  gauge-theory literature.
- External meron/fractional-instanton boundary context where a regulator, cap,
  pair, twist, or patching construction is load-bearing.

Forbidden hidden imports:

- Framework substrate identification.
- Framework observable identification.
- A framework-native derivation of the regulator/twist/patching sector.
- A finite-action theorem for the singular unregularized single meron.
- Any hierarchy closure, including `alpha_LM^16`, `v/M_Pl`, or a
  `4 pi^2` versus `ln(M_Pl/v)` identification.

This repair adds an explicit downstream firewall and a runner check for those
forbidden imports.
