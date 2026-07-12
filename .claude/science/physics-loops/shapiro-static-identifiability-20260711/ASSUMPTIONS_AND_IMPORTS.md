# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Deterministic spatial amplitude kernel | Maps a node field array to detector amplitudes | computed lattice input | `scripts/shapiro_static_discriminator.py::_propagate` | yes | yes | exact source inspection plus independent toy reduction | allowed on the runner-bounded surface |
| Detector normalized-overlap phase | Observable applied to detector amplitudes | computed lattice input | `_phase_lag_against_baseline` | yes | yes | exact functional factorization | allowed on the runner-bounded surface |
| Configured grown families and seeds | Finite portability/control domain | explicit normalization/boundary condition | runner constants | no for exact no-go; yes for numeric control | no for exact no-go | keep as bounded control domain | explicit finite scope |
| `c`-indexed cone mask | Old purported causal comparator | unsupported import as causal dynamics | `_causal_field` | no for exact no-go | no | demote to a static field snapshot | exposed; must not be called propagated history |
| Fixed-delay schedule rows | Secondary finite control | computed lattice input | `_static_schedule_field` plus completed sweep | no for exact no-go | no | assert bounded spread and mismatch on all configured rows | bounded control only |
| Configured numeric/control bundle: `BETA`, `K`, `H`, `NL`, `PW`, `MAX_D_PHYS`, `MASS_Z`, `FIELD_STRENGTH`, `SOURCE_LAYER`, `+0.1` core offset, detector-normalized cone rule, fixed cone index `1.0`, and assertion thresholds | Defines the finite scheduling-control grid and reported numbers | explicit normalization/boundary condition | runner constants and formulas | no for exact no-go; yes for finite control values | no for exact no-go | keep every value visible and forbid physical-unit interpretation | bounded configured-control input |
| Time coordinate / detector clock | Required for a physical delay history | missing import | absent from runner | no for exact no-go; yes for positive causality | only for a positive causal discriminator | add an explicit temporal model in a future claim | excluded here |
| Source history and initial/boundary data | Required for a retarded field | missing import | absent from runner | no for exact no-go; yes for positive causality | only for a positive causal discriminator | derive or explicitly supply in a future temporal extension | excluded here |
| Literature or observed Shapiro values | Possible physical comparator | observational/literature comparator | none used | no | no | not needed | forbidden as proof input |

## Minimal Premise Set

The exact result uses only: one fixed configured instance, the runner's
unconstrained node-array input class, a deterministic map from that array to
detector amplitudes, and a deterministic detector phase. It does not use the
displayed phase values, any observed target, a physical static-solution class,
or a physical interpretation of `c`.

## Import Firewall

The absence of time, source history, and detector sampling protocol is not
filled by prose. Those objects are necessary for a future positive causal
claim but irrelevant to the exact statement that a snapshot-only observable
cannot identify the history that produced its input snapshot.
