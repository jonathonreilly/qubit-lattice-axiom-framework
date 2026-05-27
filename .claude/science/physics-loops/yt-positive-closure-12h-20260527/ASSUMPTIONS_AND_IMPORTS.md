# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Transfer/Feynman-Hellmann response identity | Reduces pole response to sector matrix elements | retained support | `YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md` | yes | yes | already exact support | available |
| Same-source W row `dM_W/dell = g_2 A/2` | Denominator for local ratio | retained/exact support conditional row | strict W/Z and FH support stack | yes | yes | strict same-source certificate | available as support, not full closure |
| C3 source direction `B_x` | Supplies candidate top-source tangent | exact support | `YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md` | yes for C3 route | yes for C3 route | already exact support | available |
| Nontrivial C3 top-line assignment | Selects response magnitude `1/sqrt(6)` rather than singlet `2/sqrt(6)` | unsupported import on actual surface; current real same-surface shortcut pruned | current branch C3 finite algebra | yes | yes | derive accepted C3 circulant dynamics/source law or strict pole rows | open blocker |
| Same-surface top generator factorization `(A/sqrt(2)) B_x` | Turns C3 response into `A/sqrt(12)` matrix element | unsupported import on actual surface | new factorization boundary | yes | yes | derive accepted transfer/action generator or strict pole rows | open blocker |
| Physical top pole/projector | Identifies the sector whose matrix element is read | unsupported import on actual surface | top-sector projector obstruction stack | yes | yes | non-mass-ordering top-line theorem, dynamics, or pole certificate | open blocker |
| Base C3 circulant dynamics and orientation/phase law | Supplies spectral ordering and isolates physical top line | unsupported import on actual surface | C3 dynamics ordering/source-law boundary | yes | yes | derive microscopic dynamics theorem or strict pole rows | next active blocker |
| Positive real C3 transfer/Perron top-line selection | Would use positivity to select the physical top line | pruned on current surface | `YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md` | yes | yes | add accepted orientation/phase/top-ordering dynamics or strict pole rows | no-go for positive real shortcut |
| Nontrivial C3 phase-ordering cone membership | Places the top line in `P_omega` or `P_omega2` instead of `P_0` | exact support/open import | `YT_C3_PHASE_ORDERING_CONE_SUPPORT_BOUNDARY_NOTE_2026-05-27.md` | yes | yes | derive `y_0 > sqrt(3) x_0` or `-y_0 > sqrt(3) x_0` from accepted microscopic dynamics | open blocker |
| Orientation-odd same-surface C3 phase law | Supplies nonzero `y_0` strong enough to isolate a nontrivial complex line | unsupported import on actual surface; reflection-even route pruned | `YT_C3_ORIENTATION_PHASE_DYNAMICS_NECESSITY_NO_GO_NOTE_2026-05-27.md` | yes for C3 route | yes for C3 route | derive accepted orientation-odd base dynamics with `|y_0| > sqrt(3) x_0` and W/top matrix elements, or bypass with strict pole rows | open blocker |
| Quantitative C3 phase-strength law | Upgrades orientation sign/nonzero `B_y` to strict nontrivial cone membership | unsupported import on actual surface; sign-only route pruned | `YT_C3_ORIENTATION_PHASE_STRENGTH_BOUNDARY_NO_GO_NOTE_2026-05-27.md` | yes for C3 route | yes for C3 route | derive accepted same-surface law proving `|y_0| > sqrt(3) x_0` on signed branch | open blocker |
| Quantitative C3 phase-angle selector | Selects where the unit-normalized base operator lies on the signed `(x_0,y_0)` circle | unsupported import on actual surface; unit-norm plus sign route pruned | `YT_C3_QUANTITATIVE_PHASE_STRENGTH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md` | yes for C3 route | yes for C3 route | derive an accepted phase-angle/strength dynamics law, or bypass with strict pole rows | open blocker |
| Primitive C3 character phase angle `phi=+/-2pi/3` | Gives a concrete nontrivial-cone target on the unit base circle | conditional support/open import | `YT_C3_PRIMITIVE_CHARACTER_PHASE_ANGLE_CANDIDATE_NOTE_2026-05-27.md` | yes if used for C3 route | yes for C3 route | derive an accepted same-surface Y_T phase-angle law selecting this angle, or bypass with strict pole rows | open blocker |
| Finite C3 representation/character phase selection | Would select the physical phase from C3 algebra alone | pruned on current surface | `YT_C3_REPRESENTATION_PHASE_SELECTION_NO_GO_NOTE_2026-05-27.md` | yes if used as shortcut | yes for shortcut | add accepted same-surface dynamics/readout law, or bypass with strict pole rows | no-go for representation-only shortcut |
| Contact/FV/IR/model-class checks | Certify strict pole-row evidence | missing certificate fields | sparse response contract | yes for strict evidence route | yes | direct sparse pole-response certificate | open blocker |
| Accepted strict top/W pole rows | Bypass C3 line assignment and read coefficient directly | absent | strict sparse availability audit | yes | yes | produce accepted pole-row data/certificate | open blocker |
| Microscopic backend/projector/matrix-element shortcut | Would derive the physical row from source law, carrier amplitude, C3 algebra, W row, and no-kappa candidate | pruned on current surface | `YT_MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY_NOTE_2026-05-27.md` | yes | yes | derive accepted backend, W/top projectors, and source-generator matrix elements, or produce strict pole rows | no-go for current shortcut |
| `H_unit`, old Ward authority, `yt_ward_identity`, `y_t_bare`, observed top/W/Z masses, PDG targets, `alpha_LM`, plaquette/u0, Planck, alpha_s, fitted selectors | Forbidden proof inputs | forbidden | user campaign instruction | no | no | must remain absent | not used |

Current block results: the exact finite algebra shows how `A/sqrt(12)` would
follow if the same-surface generator factorization and nontrivial top-line
assignment were supplied; the real same-surface C3 shortcut does not derive
that top-line assignment; and the derived `B_x` source tangent does not derive
base C3 dynamics or spectral ordering; and current branch artifacts do not
contain accepted strict pole-response evidence; and the current microscopic
shortcut does not derive the accepted backend, physical top projector, or
source-generator matrix element; and positive real C3 transfer/Perron
selection picks the singlet `P_0` rather than a nontrivial physical top line.
The exact residual C3 phase-ordering cone is now characterized, but accepted
base-operator cone membership remains open. Reflection-even base dynamics is
now pruned as a route to that cone because it forces `y_0 = 0`, leaving either
the singlet line or a degenerate nontrivial block. The next active import is
accepted strict pole-row data or a genuinely new orientation-odd microscopic
dynamics theorem deriving `|y_0| > sqrt(3) x_0` on a signed nontrivial branch
plus W/top projectors and source-generator matrix elements on one
same-surface backend. Orientation sign or nonzero `B_y` alone is now pruned;
the remaining C3 theorem must be quantitative. Unit-normalized connected C3
base dynamics plus orientation sign is now also pruned: the signed unit circle
contains both singlet-top and nontrivial-top witnesses, so an accepted
phase-angle selector remains load-bearing.
The primitive nontrivial C3 character angles are now conditional support:
`phi=+/-2pi/3` lies inside the target cone and gives `A/sqrt(12)`, but the
accepted same-surface phase-angle law selecting that value for the physical
Y_T base operator is still an open import.
Finite C3 representation/character facts alone are now pruned as that
selector: C3-native unit Hermitian choices include both target-row and
singlet-row witnesses.
