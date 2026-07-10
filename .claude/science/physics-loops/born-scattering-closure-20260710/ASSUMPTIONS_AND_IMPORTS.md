# Assumptions and Imports

## First-principles reset

`A_min` permits only the supplied finite directed propagation harness, complex
linearity, differentiation of the detector centroid, elementary finite-sum
algebra/calculus, and explicitly named audited dependencies. It does not permit
the comparison target to enter the proof.

Forbidden imports are the numerical target `-1.43`, target-selected `beta`, an
unproved eikonal/Fermat/dispersion identification, the centered surrogate, and
an incoherent ray mixture substituted for the coherent propagator.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---:|---:|---|---|
| Plane-wave finite-path formula | candidate analytic observable | support-only | target note / runner | yes for old claim | no for negative boundary | derive from literal functional or prove mismatch | active test |
| `L=15, x_src=5, beta=0.8, b={3,4,5,6}` | old fixed comparison envelope | admitted normalization / fitted input mix | target note | yes for old numerical comparison | no for formula-class no-go | quantify scale covariance and remove target comparison | forbidden as general proof input |
| Lattice slope `-1.43` | old comparator | observational comparator | prior lensing runs | yes for old conclusion | no | recompute inside literal runner or remove from theorem premise | forbidden as proof input |
| 2D Gaussian angular average | candidate correction | unsupported import as literal observable | `gaussian_beam_eikonal.py` | yes for old beam claim | no | derive from amplitude propagation or classify as surrogate | active test |
| 3D Gaussian correction | candidate correction | unsupported import | `eikonal_3d_corrected.py` | yes for old table | no | derive angular measure and observable in 3D or remove | active test |
| Exact adjoint edge identity | literal finite-harness observable | retained support | `LENSING_ADJOINT_KERNEL_NOTE.md` (`audited_clean`) | yes | yes | one-hop dependency plus direct algebraic replay | allowed |
| Centered finite-path negative | prior route pruning | retained no-go | `LENSING_FINITE_PATH_EXPLANATION_NOTE.md` (`audited_clean`) | yes for no-go synthesis | yes | preserve its narrow scope | allowed |
| Nonnegative scalar-path multipole no-go | route-family obstruction | retained no-go | `LENSING_CENTROID_MULTIPOLE_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md` (`audited_clean`) | yes | yes | prove target eikonal/beam class lies inside its hypotheses | allowed |
| Fine-harness four-point slope | possible falsifier, never a premise | computed lattice input | exact Kubo/adjoint runners | no for formula-class theorem | no | compute after prediction is fixed | blinded diagnostic only |
| Minimal framework axioms | ontology baseline | zero-input structural | `MINIMAL_AXIOMS_2026-06-29.md` | no for finite-harness algebra | no | none; they do not supply dynamics | allowed but insufficient |

## Nature-grade boundary

The four framework axioms supply no Hamiltonian, transfer rule, source/action
bridge, detector observable, beta value, or packet geometry. Therefore a
positive claim that derives the numerical slope from those axioms is presently
blocked before any calculation. A clean theorem can still close on the named
finite harness or as an exact negative boundary over a specified analytic model
class; it must say so explicitly.
