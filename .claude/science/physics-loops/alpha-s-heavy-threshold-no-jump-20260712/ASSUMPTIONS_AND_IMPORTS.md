# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Continuum SU(3) QCD with one heavy fundamental quark | Defines the bounded theorem domain and the heavy loop | explicit normalization/boundary condition | target note section 4 | yes | yes | explicit action/Feynman-integral theorem surface | disclosed condition; does not chain-satisfy |
| MSbar subtraction | Fixes the logarithmic decoupling convention | explicit normalization/boundary condition | target note section 4 | yes | yes | explicit subtracted one-loop expression plus primary-source convention check | disclosed condition; does not chain-satisfy |
| `T_F=1/2` | Supplies the SU(3) fundamental trace normalization | exact algebraic input | target note and primary runner | yes | yes | exact runner check | closed |
| Feynman weight integral `int_0^1 x(1-x) dx=1/6` | Determines the heavy-loop logarithm coefficient | exact subderivation | primary runner | yes | yes | exact rational evaluation | closed |
| Mass-fixed matching point `M=m_h(M)` | Sets the one-loop logarithm to zero | explicit normalization/boundary condition | target note section 4 | yes | yes | theorem is explicitly restricted to this matching convention | disclosed condition; does not chain-satisfy |
| Chetyrkin--Kniehl--Steinhauser equations (7), (18), (23) | Checks direction, normalization, and perturbative order | background context | `LITERATURE_BRIDGES.md` | no | no | self-contained displayed derivation is load-bearing | non-derivation cross-check |
| Physical heavy-quark mass values | Would place thresholds in a phenomenological chain | unsupported import | none | no | no | separate retained derivation or explicitly supplied phenomenological-input lane | excluded; supplied data would not chain-satisfy |
| Two-loop and higher decoupling constants | Would extend accuracy beyond this kernel | standard correction | none | no | no | separate higher-loop theorem | excluded |
| Positive perturbative domain and leading-power EFT projection | Keeps every segment above its one-loop Landau pole and excludes `q^2/m_h^2` operators | explicit normalization/boundary condition | target note sections 3, 4, and 6 | yes | yes | explicit theorem hypothesis plus runner guards | disclosed condition; does not chain-satisfy |

No observed coupling, fitted selector, physical mass value, or downstream
`alpha_s(M_Z)` value enters the proof.
