# Canonical endpoint correction and revised first successful-run attempt

NUMERICAL_DETAILS_v1.md and the first execution are immutable historical
records. The current runner is check_weak_field_inverse_v2.py and the current
protocol is PROTOCOL_v2.json. Source hashes bind both the failed history and
the present inputs.

The first attempt failed because its first absolute positive scalar step was
beyond the finite canonical endpoint. V2 first integrates the regular
remaining-distance formula (12), compares it with (13), then sets steps to
the declared fractions of that distance. A separate integral of the original
local kinetic line element supplies the endpoints to findroot. Root tolerances
are unchanged. Every endpoint is checked against the requested distance.

The exact fixed-theory derivative operator is
D_phi=2 sqrt(a) z(1+z)/sqrt(J) D_z.
Third and fourth derivatives of ln G_N are obtained by applying it before
substituting the null family. Central finite errors are compared to h^2
times these derivatives divided by6 and12. The ratios must be within1 percent
of1 on the frozen grid and both absolute errors must decrease at least20 fold
for a10 fold smaller step, except below1e-60. This replaces the unsupported
uniform100h^2 preliminary threshold before that old threshold was ever reached.
It changes a numerical-domain/error diagnostic, not the action or data.

All original forward/inverse, PPN, exact null-family, mass and observation
functions are unchanged. Original fixtures and90-digit precision remain.
New distance outputs are internal geometry calculations, not additional
physical measurements. Timeout180seconds and exclusive evidence writes remain.
