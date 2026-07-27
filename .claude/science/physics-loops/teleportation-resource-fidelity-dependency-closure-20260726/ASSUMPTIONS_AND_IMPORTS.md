# Assumptions and imports

## Import ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Physical `rho_RB` | Supplied input to the universal finite-dimensional theorem | supplied physical input | `TELEPORTATION_DYNAMICAL_RESOURCE_GENERATION_NOTE.md` gives explicit non-vacuous finite instances | yes, as quantified input | yes | keep supplied; do not claim universal preparation | explicit bounded supplier edge |
| Bell projectors and `Z^z X^x` correction | Defines and implements the fixed ideal logical protocol | retained support | `TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md` T2/T3/T7/T8 | yes | yes | already retired on the ideal logical surface | explicit retained-bounded edge |
| Two-bit classical record interface | Carries `(z,x)` to Bob before correction | retained support | `TELEPORTATION_CAUSAL_CHANNEL_NOTE.md` | yes | yes | already retired for an explicit positive-latency ideal channel | explicit retained-bounded edge |
| Haar-average/entanglement-fidelity identity | Standard finite-dimensional channel algebra used in the proof | standard correction | proved/checked within the target note and runner packet | yes | yes | existing algebra and Choi verification | closed in target packet |

The primitive-registry check found no approved primitive that supplies resource
dynamics, measurement dynamics, record production, or a probability rule.
None is claimed here.

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
| --- | --- | --- | --- | --- | --- |
| Fixed `Phi+` frame | The resource is aligned to another Bell label | Pre-agreed Pauli-frame relabeling | A different fixed-frame theorem, outside this claim | live but unnecessary | 1 |
| Ideal operations | Measurement, record, or correction is noisy | Explicit CPTP fault channels | A separate noisy-protocol bounded theorem | live, already separate lane | 1 |
| Supplied resource | A particular physical source is required | Compose with one finite retained resource generator | Produces a special-case consumer, not a stronger universal theorem | live but corollary-only | 1 |

No counterfactual improves this narrow repair over direct supplier wiring.
