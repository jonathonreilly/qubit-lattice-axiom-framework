# Route Portfolio

## Current Cycle

Selected routes: same-surface top sector matrix-element factorization boundary,
then non-mass-ordering real same-surface C3 top-line law obstruction.
The third route tested the C3 circulant dynamics/source-law shortcut.

| Route | Type | Claim movement | Result |
|---|---|---:|---|
| Factorize `dM_t/dell` as `(A/sqrt(2)) * Tr(P_top B_x)` | bounded theorem / upstream support | 2 | Landed conditional-support boundary |
| Treat `B_x` alone as coefficient certificate | no-go shortcut test | 2 | Pruned: `P_0` gives `A/sqrt(3)` |
| Non-mass-ordering C3 top-line law | no-go shortcut test | 3 | Pruned on current real/reflection-even C3 support |
| Accepted C3 circulant dynamics/source law for `a(h), x(h), y(h)` | no-go shortcut test | 3 | Pruned as source-derivative shortcut; base dynamics/order still open |
| Strict sparse top/W pole-response evidence | exact runner/certificate | 3 | Best next bypass route; current harness exists but no accepted backend/pole rows |

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

Conclusion: the campaign has narrowed the C3 algebraic routes to a new
microscopic base-dynamics/orientation theorem or strict pole rows. It does not
close the coefficient row.
