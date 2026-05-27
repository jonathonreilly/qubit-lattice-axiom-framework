# Route Portfolio

## Current Cycle

Selected routes: same-surface top sector matrix-element factorization boundary,
then non-mass-ordering real same-surface C3 top-line law obstruction.
The third route tested the C3 circulant dynamics/source-law shortcut.
The fourth route audited strict sparse pole-response evidence availability.
The fifth route tested the current microscopic source/backend/carrier/C3
shortcut to the accepted matrix element.
The sixth route tested positive real C3 transfer/Perron selection as a
nontrivial top-line law.
The seventh route characterized the residual C3 phase-ordering cone.
The eighth route pruned reflection-even base dynamics as a derivation of that
cone.

| Route | Type | Claim movement | Result |
|---|---|---:|---|
| Factorize `dM_t/dell` as `(A/sqrt(2)) * Tr(P_top B_x)` | bounded theorem / upstream support | 2 | Landed conditional-support boundary |
| Treat `B_x` alone as coefficient certificate | no-go shortcut test | 2 | Pruned: `P_0` gives `A/sqrt(3)` |
| Non-mass-ordering C3 top-line law | no-go shortcut test | 3 | Pruned on current real/reflection-even C3 support |
| Accepted C3 circulant dynamics/source law for `a(h), x(h), y(h)` | no-go shortcut test | 3 | Pruned as source-derivative shortcut; base dynamics/order still open |
| Strict sparse top/W pole-response evidence | availability audit | 3 | Audited absent on current branch; harness/candidate only |
| Microscopic backend/projector/matrix-element shortcut | no-go shortcut test | 3 | Pruned: current support does not derive accepted backend, top projector, or source-generator matrix element |
| Positive real C3 transfer/Perron selection | no-go shortcut test | 3 | Pruned: positivity selects `P_0`, not a nontrivial line |
| C3 phase-ordering cone | exact support boundary | 2 | Landed: nontrivial top line iff `|y_0| > sqrt(3) x_0` with nonzero sign branch |
| Reflection-even C3 base dynamics to phase cone | no-go shortcut test | 3 | Pruned: reflection forces `y_0 = 0`, giving `P_0` or degenerate nontrivial block |

## Stuck Fan-Out

| Attack frame | Attempt | Outcome |
|---|---|---|
| Minimal finite C3 algebra | Compute `Tr(P_k B_x)` and multiply by radial factor | Nontrivial lines give `A/sqrt(12)`, singlet gives `A/sqrt(3)` |
| First-principles transfer/FH | Reuse exact response identity without reproving it | Confirms sector matrix element remains load-bearing |
| Source normalization | Check whether Fisher/RN source unit fixes line/projector | Fails; fixes scale, not top-line assignment |
| Mass-ordering | Use top as heaviest/largest response | Fails; selects `P_0`, not target nontrivial line |
| Real same-surface C3 top-line law | Try to exclude `P_0` from current real/reflection-even support | Fails; support fixes `B_x` but not physical top sector |
| C3 circulant source law | Use derived `B_x` as source derivative to order top line | Fails; base dynamics and `y_0` phase/order remain load-bearing |
| Strict evidence route | Inspect current sparse certificate | Harness exists; accepted backend and pole rows absent |
| Microscopic backend/projector route | Combine source law, carrier amplitude, C3 algebra, W row, and no-kappa candidate | Fails; accepted backend, physical projector, and source-generator matrix element remain load-bearing |
| Positive real C3 Perron route | Use positivity to select the physical top line | Fails; Perron line is `P_0`, nontrivial block remains degenerate |
| Phase-ordering cone map | Classify exactly when complex C3 dynamics selects a nontrivial line | Succeeds as exact support; accepted cone membership remains open |
| Reflection-even base dynamics | Try to derive cone membership while preserving reflection symmetry | Fails; `y_0 = 0` forces singlet or nontrivial degeneracy |

Conclusion: the campaign has narrowed the C3 algebraic routes to a new
orientation-odd microscopic dynamics theorem with accepted backend/projectors,
nontrivial phase-ordering cone membership, and matrix elements, or accepted
strict pole rows. It does not close the coefficient row.
