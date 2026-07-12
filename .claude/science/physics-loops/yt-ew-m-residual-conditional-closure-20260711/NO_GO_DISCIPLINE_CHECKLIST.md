# No-Go Discipline Checklist

**Claim under review:** a map whose entire action on the color propagator is
`G_prime = a G` cannot select the adjoint Fierz channel by changing its weight
relative to the singlet channel.

## N1 — Alternative route enumeration

| Route ID/class | Attack on the no-go | Test and outcome | Marker |
|---|---|---|---|
| R1 algebraic phase/sign | A negative or complex `a` might act differently on the two traces | Both traces are linear in the same `a`; both absolute squares acquire `|a|^2` | ATTEMPTED |
| R2 singular scalar | The value `a=0` might count as adjoint selection | It sends both `S` and `C` to zero, erasing the correlator rather than retaining `C` | ATTEMPTED |
| R3 exceptional matrix | A traceless, pure-singlet, pure-adjoint, or zero matrix might evade the argument | The homogeneous equalities remain defined; ratios are asserted only for nonzero denominators | ATTEMPTED |
| R4 representation/basis | A different `N_c` or normalized generator basis might change the scaling power | The proof uses only trace linearity; basis choice changes coefficients but not degree-two homogeneity | ATTEMPTED |
| R5 alternative readout | An absolute threshold or channel-specific projector applied after scaling might select one channel | It can, but that extra readout is not common scalar multiplication alone and is outside the claim | ATTEMPTED |
| R6 dynamical/non-scalar escape | A nonlinear map induced by the link-dependent Dirac inverse might change relative weights | It can; this defeats only the old broad CMT reading and is explicitly outside the scalar-map no-go | ATTEMPTED |

Equations (3)-(5) close R1-R4 analytically. The runner separately exercises
real/complex phase and sign choices (R1), `a=0` (R2), generic nonzero-ratio
cases, and the stated SU(2)/SU(3) generator normalizations (representative
cases of R4). R3 is an analytic boundary statement, not a claimed exhaustive
runner sweep over pure-channel matrices. R5 is excluded by the phrase
"common scalar multiplication alone," and R6 fixes the dynamical boundary.

## N2 — Wall-independence audit

There are no walls or load-bearing open conditions inside the theorem. The
single physical gate—deriving the map on `G` from `U -> u_0 V`—is excluded
from the premise and conclusion. With one external gate, no pairwise wall
table is applicable and no inflated wall count is claimed.

## N3 — Hidden-wall scan

The scan covered the source note, direct runner, downstream matching note, and
downstream runner using
`we assume|by construction|as is standard|the framework provides|bridge context|background|naturally|obviously|standard QFT|registered|canonical`.
It found `registered primitive` in the downstream note, where it explicitly
says the supplied channel/readout premises are **not** registered primitives,
and `CANONICAL_HARNESS_INDEX.md` in a downstream motivation-only guard. Both
are non-load-bearing context. The source proof contains one explicit premise,
`G_prime = a G`; no hidden wall was found.

## N4 — Residual matching

| Witness | Witness residual | Current repair | Match? |
|---|---|---|---|
| `docs/audit/AUDIT_LEDGER.md`, claim `yt_ew_m_residual_note_2026-05-02` | No derivation of `G_full = u_0 G_V` from link factorization; repair may narrow to the conditional algebra | The source removes that implication and claims only the explicit scalar-map theorem | Yes |
| `docs/EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md` | Physical channel-weight selector remains supplied/open | The source leaves that selector open | Yes |

No earlier no-go is cited as proof that a broader CMT route fails.

## N5 — Rhetoric audit

The negative result is proved only at the color-matrix/propagator-map
resolution. It is not asserted at the link, Dirac-operator, Wilson-line,
current-construction, renormalization, or lattice-wide dynamical resolutions.
The source repeats those exclusions in the header, proof boundary, closure
table, and runner output.

## N6 — Partial-closure path scan

The clean partial-closure path is exactly the chosen scope repair: retain the
matrix algebra while removing the unsupported physical bridge. No new axiom,
primitive, convention ratification, or imported value is needed. A future
explicit Dirac/EW-current theorem could broaden the result, but its absence is
not described as a universal impossibility.

The primitive registry was checked; none of its supplied premises is invoked
or misclassified as a wall.

## N7 — Steelman

The strongest objection is that an actual CMT link replacement acts inside a
Dirac operator before inversion, so its induced transformation on `G` need not
be scalar. Such a transformation could change singlet and adjoint weights and
might even realize the physical selector. This objection is decisive against
the old CMT-level no-go. It is not a counterexample to the present theorem,
because the present theorem names common scalar multiplication as the entire
route it excludes and explicitly leaves all non-scalar maps open.

## N8 — Cross-cycle echo

The search covered all physics-loop `NO_GO_LEDGER.md` and `HANDOFF.md` files,
plus `docs/*.md`, for `link-to-propagator`, `G_full = u_0`, propagator
nonlinearity, and common-scalar/rescaling language. The original
`audit-backlog-campaign-20260502` cycle and
`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md` name the same physical
matching residual; it remains open. The hypercharge common-rescaling ledger,
generation-moduli rescaling note, and PMNS uniform-scalar note contain similar
scale-invariance algebra but attack different residuals and do not retire this
physical bridge. No echo supplied an unconsidered retirement mechanism.

## Author/review preflight result

**PASS for branch review.** N1-N8 support the narrowly stated
scalar-propagator no-go. They do not support a no-go for arbitrary CMT link
dynamics or the physical EW-current matching rule. This author/reviewer
preflight is not an audit verdict and does not substitute for the independent
auditor's structured no-go-discipline gate.
