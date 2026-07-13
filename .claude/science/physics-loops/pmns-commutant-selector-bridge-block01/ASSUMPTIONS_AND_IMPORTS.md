# Assumptions And Imports

## Ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Displayed `hw=1` staggered corner Hamiltonians and their positive projectors | Defines the three-corner profile | explicit finite-matrix condition; not derived from the four axioms by this note | target runner | yes | yes for this conditional finite theorem | exact projector calculation | disclosed condition |
| Literal profile `v_i = Tr(Q_i Q_1 M Q_1)` | Object whose Fourier modes are tested | local definition | target note | yes | yes | exact overlap theorem | retained in scope |
| Eigenoperator normalization/sign | Needed if selector values depend on `M` rather than its line | unsupported import in the old map | absent | yes for old `q/tau` maps | yes for a positive bridge | prove projective invariance or supply a carrier normalization theorem | exposed blocker |
| Identification of corner transport with passive-block offset | Would turn a corner label into PMNS `q` | unsupported import | absent and explicitly not used in the no-go | no | yes for a future positive bridge | carrier theorem | exposed open bridge |
| Identification of corner reflection with lepton-sector exchange | Would turn an odd corner mode into PMNS `tau` | unsupported import | absent and explicitly not used in the no-go | no | yes for a future positive bridge | inter-sector bridge theorem | exposed open bridge |
| Observed PMNS values or fitted branch labels | Could anchor the selector maps | fitted/observational input | forbidden | no | no | none allowed | excluded |
| Active five-real PMNS source | Parent ambition beyond selector bridge | open downstream object | current PMNS package | no | no | separate source/transport derivation | excluded from claim |

The primitive-registry check found no registered primitive that supplies a
PMNS readout context, selector, normalization, carrier identification, or
inter-sector map. The scale-reference, kinetic-isotropy, and realized-state
primitives are irrelevant to this dimensionless finite selector problem.

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| The lifted operator is supported at the first corner | Transport the lift to either other corner | `Q_j M Q_j`, `j=2,3` | Tests whether the stated `q` map distinguishes the full `C_3` orbit | live and tested | 3 |
| The generator's displayed sign is meaningful | Treat `M` and `-M` as the same eigenoperator line | projective quotient | Tests whether `q/tau` are normalization-independent | live and tested | 3 |
| `Re(v_+)` is orientation-odd | Use the actual corner reflection `v_2 <-> v_3` | conjugation `v_+ <-> conjugate(v_+)` | Separates real and imaginary reflection characters | live and tested | 3 |
| A corner label is the passive offset | Compare with the passive-block moment definition | `q = argmax_r |Tr(B C^{-r})|` | Tests existence of a factorization through the corner profile | live and tested | 3 |
| A corner odd mode is the sector bit | Compare both lepton-sector orientations at fixed corner profile | swap active/passive sector pair while holding `M` fixed | Tests existence of a factorization through the corner profile | live and tested | 3 |
| A non-Hermitian generator phase could carry orientation | Allow `M -> exp(i alpha) M` | complex eigenoperator ray | Exposes continuous phase gauge rather than a discrete native bit | live and tested | 2 |

The selected route uses the sign counterfactual for the load-bearing exact
no-go. The cyclic/reflection counterfactuals are internal diagnostics only;
the physical factorization counterfactuals expose future bridge obligations
and are not claimed as no-go results.
