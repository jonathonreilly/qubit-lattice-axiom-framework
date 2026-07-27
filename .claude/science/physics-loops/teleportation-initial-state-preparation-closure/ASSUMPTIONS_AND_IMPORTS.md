# Assumptions and Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Default 1D `N=8` and 2D `4x4` periodic lattices | Defines the finite claim surface | admitted normalization | target note and runner | yes | yes | fixed scope | explicit |
| `mass=0`, `G=0`, `t_hop=1` | Fixed control surface reducing the Hamiltonian to `H1=-A` and a Kronecker sum | admitted normalization / boundary condition | target note and runner defaults | yes | yes | explicit finite claim scope plus matrix-identity checks | disclosed and checked |
| `build_H1` / `build_H2_tensor` implementation | Constructs the finite matrices | computed lattice input | `scripts/frontier_bell_inequality.py` | yes | yes | executable residuals against independently written matrix identities | retired by certificate |
| Distinguishable-species tensor-product basis `|i,j>` | Fixes the two-species Hilbert-space convention | admitted normalization / boundary condition | `scripts/frontier_bell_inequality.py` | yes | yes | explicit constructor docstring and Kronecker-sum residual | disclosed and checked |
| Periodic Fourier spectrum of adjacency | Proves unique uniform ground and exact gap | zero-input structural | derivation in target note | yes | yes | analytic derivation | closed |
| `factor_sites` logical/environment indexing | Defines the audited separability split | admitted normalization / boundary condition | `scripts/frontier_teleportation_resource_from_poisson.py` | yes | yes | explicit indexing plus exact uniform-factor residual | disclosed and checked |
| Dense eigensolver output | Independent finite numerical cross-check | computed lattice input | SciPy `eigh` in runner | no | no | analytic spectrum | confirmation only |
| Cooling/control/readout protocol | Would establish operational preparation | unsupported import | absent | no, for finite open-gate boundary | no | future physical protocol | explicitly open |
| Noise and preparation-time scaling | Would extend beyond the finite diagnostic | unsupported import | absent | no, for finite open-gate boundary | no | future model/theorem | explicitly open |

No observed target values, fitted selectors, literature values, or admitted
unit conversions enter the finite derivation.

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| Periodic 1D `N=8` and 2D `4x4` geometry | The Fourier spectrum and gap formulas change | Other sizes or boundary conditions | A separate scaling or boundary study, not this finite claim | live but outside scope | 1 |
| `mass=0`, `G=0`, `t_hop=1` | The uniform vector need not be the same ground state | Nonzero mass/coupling or rescaled hopping | A different initial-state theorem with new spectral inputs | live but outside scope | 1 |
| Distinguishable ordered species registers | Symmetrization restricts the Hilbert space | Bosonic or fermionic two-particle sector | A different resource encoding and ground-space analysis | live but outside scope | 1 |
| `factor_sites` split defines the audited logical/environment cut | Another encoding changes the factorization diagnostic | Different logical axis or encoding map | Encoding-portability analysis, not native-site support | live but outside scope | 1 |
| Native-basis localization uses `PR/dim <= 0.25` | The qualitative threshold label changes | Another declared threshold | Does not change the exact result `PR/dim=1` | insensitive nuisance | 0 |
| No operational preparation model is supplied | A concrete protocol could close part of the open gate | Cooling/control/noise/readout model with scaling bounds | Operational preparation theorem | live hard residual outside authorized target | 2 |
