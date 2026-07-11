# Assumptions and Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Selected-axis abstract `SU(2) x SU(3)` action and `3 + 1` split | constructs representation modules | retained support | `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` | yes | yes | already retained-grade | chained |
| Structural groups/carrier read as SM weak, color, and LH fermions | supplies physical interpretation | bounded physical bridge | existing hypercharge/LHCM chain | yes for SM naming; no for module algebra | yes for physical SM claim | requires an independent carrier-realization theorem; otherwise keep conditional | explicit boundary |
| Traceless central ratio `1:-3` | fixes projective U(1) direction | retained support / decoration | LH-doublet ratio note | yes | yes | already retained-grade | chained |
| Neutral Higgs-vev stabilizer with nonzero `Y_H=h` | gives `Q=T_3+Y/(2h)` | retained bounded support | GMN L4 note | yes | yes | explicit bounded antecedent | chained |
| Lower color-singlet component has relative charge `q=-1` | fixes physical ratio `alpha/h=1/3` | admitted physical readout | alpha-third bridge premise packet | yes for SM charge pattern | yes for conventional SM table | requires an independent physical readout theorem; not retired here | explicit |
| `Y_H=+1` | displays `alpha/h=1/3` as `alpha=1/3` | vacuous normalization coordinate | Tier-A convention registry / GMN L4 coordinate | yes only for displayed coordinates | no for invariant charges | common `(Y,h,g_Y)` rescaling | explicit convention |
| Names `Q_L`, `L_L`, `e_L` | post-construction terminology | naming convention | SM representation terminology | no | no | not propositional | attach only after proof |

No measured PDG value, fitted selector, or literature numerical comparator is
used. The lower-singlet relative charge is an explicit bounded SM-readout
premise, not a result extracted from a target-value comparison.

## Counterfactual pass

| Assumption | What if it's wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| Structural `SU(3)` is physical color | It is only an internal symmetry | Keep abstract `(2,3)+(2,1)` modules with no quark/lepton names | Demotes the physical claim while preserving exact algebra | live | 3 |
| Lower color-singlet charge is `q=-1` | The readout has another relative charge `q` | Use `alpha/h = 2(q+1/2)/(-3)` | Exposes the unretired physical readout as the true normalization input | live | 3 |
| Higgs coordinate is `h=1` | A different nonzero coordinate is used | Common rescaling of all U(1) charges and reciprocal coupling | Shows `alpha/h` and `Q` are invariant | live | 3 |
| Lower Higgs component is the neutral vev direction | The upper component is supplied instead | Opposite-component vev | Gives the component-swapped conjugate table tested in Part 9 | live | 2 |
| One physical field realizes each module | Multiple copies/exotics realize it | Add another identical representation module | Demonstrates that representation content alone cannot select species identity | live | 2 |

Synthesis: the first three counterfactuals are the selected route. They force
the proof to stop at an abstract module decomposition, an explicit relative
charge premise, and the coordinate-free ratio `alpha/h`.
