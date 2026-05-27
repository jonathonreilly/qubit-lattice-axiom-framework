# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Transfer/Feynman-Hellmann response identity | Reduces pole response to sector matrix elements | retained support | `YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md` | yes | yes | already exact support | available |
| Same-source W row `dM_W/dell = g_2 A/2` | Denominator for local ratio | retained/exact support conditional row | strict W/Z and FH support stack | yes | yes | strict same-source certificate | available as support, not full closure |
| C3 source direction `B_x` | Supplies candidate top-source tangent | exact support | `YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md` | yes for C3 route | yes for C3 route | already exact support | available |
| Nontrivial C3 top-line assignment | Selects response magnitude `1/sqrt(6)` rather than singlet `2/sqrt(6)` | unsupported import on actual surface; current real same-surface shortcut pruned | current branch C3 finite algebra | yes | yes | derive accepted C3 circulant dynamics/source law or strict pole rows | open blocker |
| Same-surface top generator factorization `(A/sqrt(2)) B_x` | Turns C3 response into `A/sqrt(12)` matrix element | unsupported import on actual surface | new factorization boundary | yes | yes | derive accepted transfer/action generator or strict pole rows | open blocker |
| Physical top pole/projector | Identifies the sector whose matrix element is read | unsupported import on actual surface | top-sector projector obstruction stack | yes | yes | non-mass-ordering top-line theorem, dynamics, or pole certificate | open blocker |
| C3 circulant dynamics/source law for `a(h), x(h), y(h)` | Could supply spectral ordering and source-generator matrix element | unsupported import on actual surface | C3 spectral source-response no-go plus new top-line obstruction | yes | yes | derive same-surface dynamics/source theorem or strict pole rows | next active blocker |
| Contact/FV/IR/model-class checks | Certify strict pole-row evidence | missing certificate fields | sparse response contract | yes for strict evidence route | yes | direct sparse pole-response certificate | open blocker |
| `H_unit`, old Ward authority, `yt_ward_identity`, `y_t_bare`, observed top/W/Z masses, PDG targets, `alpha_LM`, plaquette/u0, Planck, alpha_s, fitted selectors | Forbidden proof inputs | forbidden | user campaign instruction | no | no | must remain absent | not used |

Current block results: the exact finite algebra shows how `A/sqrt(12)` would
follow if the same-surface generator factorization and nontrivial top-line
assignment were supplied, and the real same-surface C3 shortcut does not
derive that top-line assignment. The next live algebraic import is an accepted
C3 circulant dynamics/source law for `a(h), x(h), y(h)`.
