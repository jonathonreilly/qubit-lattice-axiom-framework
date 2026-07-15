# Assumptions and imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|:---:|:---:|---|---|
| Fixed constants `MASS`, `G`, `S`, `DT` | Define the finite card evaluated | computed lattice input | canonical runner source | yes | yes | inspect and execute the named source | explicit theorem scope |
| Canonical runner implementation | Constructs Hamiltonians, potentials, evolutions, observables, and predicates | computed lattice input | `scripts/frontier_staggered_17card.py` | yes | yes | include as restricted-packet helper | retired by this repair |
| NumPy and SciPy | Numerical linear-algebra runtime | tooling dependency | installed Python environment | yes for replay | yes for replay | clean import and live execution checks | explicit tooling dependency |
| Physical-gravity interpretation | Not part of the finite certificate | unsupported bridge outside scope | excluded by source note | no | no | separate science theorem | excluded |

No observed target score, fitted selector, or literature value is used to
generate an expected score inside the canonical implementation.
