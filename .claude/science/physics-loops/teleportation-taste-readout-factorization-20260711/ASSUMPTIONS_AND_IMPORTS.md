# Assumptions and Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Even side and `x_i = 2c_i + eta_i` | Defines the finite KS cell/taste basis | zero-input structural for this operator model | Target note and runner | Yes | Yes | Explicit enumeration | Verified |
| Retained axis `r = dim - 1` | Selects the logical bit under audit | explicit scope condition | Target note and runner | Yes | Yes | Keep scope explicit | Verified |
| `Z_native(x) = (-1)^(sum_i x_i)` | Defines native sublattice parity | zero-input structural for this operator model | Target runner | Yes | Yes | Direct matrix construction | Verified |
| Tolerance `1e-12` | Detects floating representation error in an integer-valued matrix identity | insensitive nuisance | Target runner CLI | No | No | Exact entries give zero error | Verified |

No measured, fitted, observational, literature, normalization, or physical-apparatus input enters the factorization certificate.
