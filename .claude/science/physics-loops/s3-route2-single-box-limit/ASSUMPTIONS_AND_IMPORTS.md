# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `q_E(15)` measured E-center shell/center quotient | Single finite-box support datum used as the challenged input | computed lattice input | `logs/runner-cache/frontier_tensor_support_center_excess_law.txt` | Yes, for the challenged route | No, not enough for exact status | Box-size scan or convergence theorem | Preserved as support; not an exact limit proof |
| `q_E = 15/8` | Exact target fingerprint from prior Route-2 readout packets | retained support / exact-support candidate | `docs/QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md`, block54 fingerprint PR | Yes, as target value | Yes | Independent source/readout derivation or exact accepted bridge | Still open as derivation target |
| `rho_E = 6(q_E - 1)` | Endpoint conversion from quotient to rho | framework-derived on supplied quotient | endpoint quotient/readout surfaces | Yes, conditional on exact quotient | Yes | Already checked by parent runner when quotient is supplied | Reused; not the blocker |
| Finite-size law `q_L(N)=L+(q_15-L)15/N` | Counter-witness family showing one datum does not identify the limit | zero-input mathematical witness | block55 runner | Yes, for no-go | No, it is a route-pruning witness | None needed; explicit construction | Used only to disprove single-box exactification |
| Alternate limit `469/250` | Nearby non-target exact limit sharing the same finite datum | zero-input mathematical witness | block55 runner | Yes, for separation | No | None needed; explicit construction | Demonstrates underdetermination |
| Observed quark masses or fitted target values | Not used | forbidden import | none | No | No | Keep excluded | Excluded |

## Import Boundary

The block does not use observed quark masses, fitted selectors, or an admitted
physical target value to prove the no-go.  It uses only the already-landed
single-box calibration datum and explicit mathematical counter-witness laws.

