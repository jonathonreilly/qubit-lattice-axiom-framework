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
The ninth route pruned orientation sign/nonzero `B_y` alone as a derivation of
that cone.
The tenth route pruned unit-normalized connected C3 base dynamics plus
orientation sign as a derivation of that cone.
The eleventh route checked primitive nontrivial C3 character phase angles as a
concrete candidate for the still-open phase-angle law.
The twelfth route tested whether finite C3 representation/character facts
alone select that phase law.
The thirteenth route tested whether the cubic C3 trace invariant supplies a
phase-selector route.

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
| Orientation sign / nonzero phase to phase cone | no-go shortcut test | 3 | Pruned: same sign can select `P_0` or a nontrivial line depending on phase strength |
| Unit-normalized signed C3 base phase | no-go shortcut test | 3 | Pruned: the signed unit circle contains both `P_0` and nontrivial-line witnesses |
| Primitive nontrivial C3 character phase angle `phi=+/-2pi/3` | conditional support | 2 | Landed: selects `P_omega2` or `P_omega` and gives `A/sqrt(12)`, but accepted phase law is open |
| Finite C3 representation/character phase selection | no-go shortcut test | 3 | Pruned: C3-native unit Hermitian choices include both target and singlet rows |
| Cubic C3 trace invariant phase selector | conditional support | 2 | Landed: cubic maximization plus accepted nonzero orientation would select primitive nontrivial angles, but accepted cubic dynamics/branch are open |

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
| Orientation sign only | Try to derive cone membership from nonzero signed `B_y` | Fails; `x_0=1,y_0=1` keeps `P_0` largest despite positive sign |
| Unit-normalized signed base dynamics | Add `x_0^2+y_0^2=1` to the signed branch | Fails; `(0,1)` selects `P_omega2`, but `(sqrt(3)/2,1/2)` selects `P_0` with the same sign and unit norm |
| Primitive character angle | Test `phi=+/-2pi/3` on the unit base circle | Succeeds conditionally; it hits the target row, but deriving that phase for the physical Y_T base operator remains open |
| Representation-only selection | Ask C3 character/projector facts or functions of `C` to choose the phase | Fails; the same C3-native family contains `phi=0` and `phi=pi/6` singlet witnesses |
| Cubic trace invariant | Extremize `Tr(H(phi)^3)` on the unit C3 base circle | Succeeds conditionally; cubic maxima include `phi=+/-2pi/3`, but also the singlet `phi=0`, so accepted orientation/cubic dynamics remain load-bearing |

Conclusion: the campaign has narrowed the C3 algebraic routes to a new
same-surface cubic phase dynamics/orientation theorem selecting a
nontrivial-cone angle with accepted backend/projectors and matrix elements, or
accepted strict pole rows. It does not close the coefficient row.
