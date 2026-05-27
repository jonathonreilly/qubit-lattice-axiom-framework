# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Transfer/Feynman-Hellmann response identity | Reduces pole response to sector matrix elements | retained support | `YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md` | yes | yes | already exact support | available |
| Same-source W row `dM_W/dell = g_2 A/2` | Denominator for local ratio | retained/exact support conditional row | strict W/Z and FH support stack | yes | yes | strict same-source certificate | available as support, not full closure |
| C3 source direction `B_x` | Supplies candidate top-source tangent | exact support | `YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md` | yes for C3 route | yes for C3 route | already exact support | available |
| Nontrivial C3 top-line assignment | Selects response magnitude `1/sqrt(6)` rather than singlet `2/sqrt(6)` | unsupported import on actual surface; current real same-surface shortcut pruned | current branch C3 finite algebra | yes | yes | derive accepted C3 circulant dynamics/source law or strict pole rows | open blocker |
| Zero-singlet nontrivial C3 block membership | Weakens the coefficient-row requirement from an individual complex line to support in `P_nt = P_omega + P_omega2` | exact support/open import | `YT_C3_NONTRIVIAL_BLOCK_MATRIX_ELEMENT_SUPPORT_NOTE_2026-05-27.md` | yes | yes | derive accepted physical top-block law excluding `P_0`, or bypass with strict pole rows | open blocker |
| Same-surface sign/order/readout law excluding `P_0` | Would turn `P_nt` support into physical zero-singlet top-block membership | unsupported import on actual surface; current real/reflection-even block-algebra shortcut pruned | `YT_C3_ZERO_SINGLET_TOP_BLOCK_MEMBERSHIP_NO_GO_NOTE_2026-05-27.md` | yes | yes | derive a new accepted dynamics/order/readout theorem or bypass with strict pole rows | open blocker |
| Source-orientation/sign selector for `P_nt` | Would choose the sign of `B_x` that makes `P_nt` largest | unsupported import on actual surface; source-orientation sign-selector shortcut pruned | `YT_C3_SOURCE_ORIENTATION_SIGN_SELECTOR_NO_GO_NOTE_2026-05-27.md` | yes if used | yes for sign route | derive accepted physical source-orientation/sign/readout law or bypass with strict pole rows | no-go for sign-choice shortcut |
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
| Accepted C3 cubic phase potential and orientation branch | Would select the primitive nontrivial character phase from the cubic trace invariant | conditional support/open import | `YT_C3_CUBIC_INVARIANT_PHASE_SELECTOR_SUPPORT_BOUNDARY_NOTE_2026-05-27.md` | yes if used for cubic route | yes for C3 route | derive accepted same-surface Y_T cubic phase dynamics/orientation, or bypass with strict pole rows | open blocker |
| C3-invariant cubic phase potential structure alone | Would derive the physical phase law from invariance and cubic trace data | pruned on current surface | `YT_C3_CUBIC_PHASE_POTENTIAL_SIGN_BRANCH_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md` | yes if used as shortcut | yes for shortcut | derive accepted sign, variational convention, and orientation branch, or bypass with strict pole rows | no-go for invariance-only shortcut |
| C3-invariant scalar phase-orbit selection alone | Would derive the physical nontrivial top line from a selected C3 phase orbit | pruned on current surface | `YT_C3_PHASE_ORBIT_SELECTOR_UNDERDETERMINATION_NO_GO_NOTE_2026-05-27.md` | yes if used as shortcut | yes for shortcut | derive an accepted same-surface orbit-member/top-line law excluding `P_0`, or bypass with strict pole rows | no-go for scalar orbit-selector shortcut |
| C3 orbit-member/readout covariance alone | Would derive the physical nontrivial top line after a C3 phase orbit has been selected | pruned on current surface | `YT_C3_ORBIT_MEMBER_READOUT_COVARIANCE_NO_GO_NOTE_2026-05-27.md` | yes if used as shortcut | yes for shortcut | derive an accepted physical orientation/basepoint/orbit-member readout law, or bypass with strict pole rows | no-go for covariance-only member-readout shortcut |
| Existing C3/dihedral reflection-basepoint structure | Would supply the missing physical basepoint/orbit-member law from already-present reflection data | pruned on current surface | `YT_C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION_NOTE_2026-05-27.md` | yes if used as shortcut | yes for shortcut | derive a genuinely new accepted physical basepoint law beyond the existing reflection axis, or bypass with strict pole rows | no-go for existing-reflection basepoint shortcut |
| Orientation-biased C3 scalar phase potential | Would supply the missing physical nontrivial top-line member from a reflection-odd `sin(3 phi)` phase-bias term | pruned on current surface | `YT_C3_ORIENTATION_BIASED_PHASE_POTENTIAL_ORBIT_MEMBER_NO_GO_NOTE_2026-05-27.md` | yes if used as shortcut | yes for shortcut | derive an accepted physical basepoint/readout law beyond scalar orientation bias, or bypass with strict pole rows | no-go for orientation-biased scalar-potential shortcut |
| Source-response extremal readout | Would use extrema of the already-derived same-surface `B_x` response as a non-scalar physical top-line member law | pruned on current surface | `YT_C3_SOURCE_RESPONSE_EXTREMAL_READOUT_NO_GO_NOTE_2026-05-27.md` | yes if used as shortcut | yes for shortcut | derive an accepted physical basepoint/readout law beyond source-response extrema, or bypass with strict pole rows | no-go for source-response extremal shortcut |
| Strict W/Z plus conditional C3 top-row splice | Would splice denominator-side W/Z support with the conditional C3 target row to form a strict top/W pole-response certificate | pruned on current surface | `YT_STRICT_WZ_C3_TOP_ROW_SPLICE_NO_GO_NOTE_2026-05-27.md` | yes if used as shortcut | yes for strict route | derive accepted same-surface splice authority, physical top-line/projector authority, and strict pole-row controls | no-go for strict-splice shortcut |
| Contact/FV/IR/model-class checks | Certify strict pole-row evidence | missing certificate fields | sparse response contract | yes for strict evidence route | yes | direct sparse pole-response certificate | open blocker |
| Accepted strict top/W pole rows | Bypass C3 line assignment and read coefficient directly | absent, including current-branch repository discovery scan | strict sparse availability audit; strict pole-row repository discovery no-go | yes | yes | produce accepted pole-row data/certificate | open blocker |
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
The cubic C3 trace invariant is now conditional support: on the unit connected
base circle `Tr(H^3)=sqrt(6)cos(3phi)/6`, so cubic maximization plus an
accepted nonzero orientation branch would select `phi=+/-2pi/3` and give
`A/sqrt(12)`. The actual surface still lacks the accepted same-surface cubic
phase potential/variational law and physical orientation branch.
C3-invariant cubic phase-potential structure alone is now pruned as that
missing law: sign, variational convention, singlet extremum, degenerate
extrema, and physical orientation branch remain open.
General C3-invariant scalar phase dynamics is now also pruned as a physical
top-line selector: it selects phase orbits, and those orbits contain singlet
and nontrivial top-line witnesses. The remaining C3 route needs an accepted
orbit-member/top-line readout law that excludes `P_0`, plus W/top matrix
elements, or strict pole rows.
C3 orbit-member/readout covariance alone is now pruned as that missing law:
a free C3 phase orbit has no equivariant section, and the three
symmetry-breaking sections include a `P_0` row as well as the two nontrivial
target-row witnesses. The remaining C3 route needs an accepted physical
orientation/basepoint/orbit-member readout law that excludes `P_0`, plus W/top
matrix elements, or strict pole rows.
The existing C3/dihedral reflection-basepoint shortcut is now also pruned:
full C3/D3 naturality has no section of the selected free orbit, and the
already-derived real-record reflection axis fixes `P_0`; rotated reflection
axes are additional basepoint imports rather than derived physical authority.
The strict-route repository discovery audit now also prunes the
hidden-existing-certificate shortcut: current Y_T strict/response/backend or
projector outputs do not contain a complete accepted strict top/W pole-row
packet.
The orientation-biased phase-potential shortcut is now pruned too: adding a
reflection-odd `sin(3 phi)` phase-bias term selects a C3 phase orbit rather
than a physical orbit member, and generic selected orbits still contain a
`P_0` singlet-row witness. The remaining C3 import is an accepted physical
basepoint/readout law beyond scalar orientation bias, with W/top matrix
elements, or strict pole rows.
The source-response extremal readout shortcut is now also pruned: signed and
absolute maxima of the derived `B_x` response select `P_0 -> A/sqrt(3)`, while
signed and absolute minima give the target row only after adding a
minimum-response selector and still leave the nontrivial complex pair
degenerate. The remaining C3 import is an accepted physical basepoint/readout
law beyond source-response extrema, with W/top matrix elements, or strict pole
rows.
The strict W/Z plus C3 top-row splice shortcut is now pruned: the formal
splice gives `1/sqrt(6)` only after same-surface authority and the physical
nontrivial top line are supplied, while the same denominator/source scale also
admits the `P_0` singlet readout `sqrt(2/3)`. The remaining strict import is
accepted same-surface splice/backend/projector/source-generator authority or
accepted strict pole-row data with controls.
The nontrivial C3 block matrix-element support theorem now narrows the C3
matrix-element import: complex-line isolation is not needed for the
coefficient row once zero `P_0` singlet weight is supplied, because `B_x` is
scalar on `P_nt`. The remaining physical import is accepted zero-singlet
top-block membership plus same-surface generator factorization or strict
pole-row data with controls.
The direct current-surface shortcut to that membership is now pruned:
real/reflection-even C3 block algebra has eigenvalues
`lambda(P_0)=a+2x` and `lambda(P_nt)=a-x`, so excluding `P_0` requires an
accepted sign/order/readout law or strict pole rows rather than another
algebraic restatement of the same block.
The immediate sign-choice refinement is now also pruned: selecting the sign of
`B_x` that makes `P_nt` largest imports an unaccepted source-coordinate
orientation law. The same-source ratio is invariant under `ell -> -ell`,
largest absolute response selects `P_0`, and minimum-response selection
remains an extra convention.
