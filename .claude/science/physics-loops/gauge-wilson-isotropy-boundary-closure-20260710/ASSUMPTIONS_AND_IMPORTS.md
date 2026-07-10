# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| One-site `M_2(C) ~= Cl(3,0)` algebra | Supplies the three Pauli generators and central pseudoscalar | zero-input structural | `minimal_axioms` Qubit node | yes | yes | already an approved axiom node | closed |
| One common coefficient on six Wilson orientations | Defines the accepted input subspace `I_iso` and the `3+1` orientation set | retained support | `GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md` | yes | yes | already retained | closed |
| Standard staggered phase formula | Defines the tested six-entry orientation signature only | exact definition | target note, section 2 | yes | yes | in-line definition plus exhaustive parity proof | closed as mathematics |
| Staggered determinant/source-action map | Would be needed to turn eta signs into a physical Wilson-coefficient correction | unsupported import | none | no | no | separate retained theorem | excluded from the claim |
| Constant-lift obstruction | Rules out the exact nonunit constant observable reduction `P(beta)=P_1plaq(Gamma beta)` | retained no-go support | `GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md` | no | no | already retained | non-load-bearing context only |

No observational value, fitted selector, admitted unit convention, metric
identification, source/action map, or literature value enters the proof.

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| The input Wilson surface has one common coefficient. | The input action is already anisotropic. | Start from six independent `c_mu_nu`. | Studies propagation of pre-existing anisotropy, not its derivation by these routes. | live but outside claim | 1 |
| The stated eta phases are the proposed mechanism. | A different phase or hopping kernel is used. | Replace eta by an orientation-dependent link field. | Could carry an anisotropic signature, but is a different mechanism requiring its own theorem. | live separate lane | 1 |
| Eta signs directly update physical Wilson coefficients. | The correction is a determinant-induced additive term. | Derive a staggered determinant/hopping expansion and source/action bridge. | Could test a physical effective-action correction. | open separate lane; not imported here | 2 |
| The pseudoscalar is the proposed fourth generator. | Another enlarged operator supplies time. | Add a separately derived anticommuting operator outside the one-site algebra. | Could evade the pseudoscalar route-specific wall. | live separate lane | 1 |

The selected route scores highest for this bounded task because it strips the
unsupported physical map and proves only the formal orientation-sign result.
The determinant/source-action alternative is the highest-value separate
physics opportunity, but it is not needed for this narrow no-go and cannot be
silently imported.
