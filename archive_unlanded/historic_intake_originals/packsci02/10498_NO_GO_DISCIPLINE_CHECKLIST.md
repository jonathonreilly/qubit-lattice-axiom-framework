# No-Go Discipline Checklist

Claim under gate:

> With `H=-Delta_lat` and `G_0=H^{-1}` fixed as a complete inverse graph, the
> current framework premises do not force the independent field operator to
> obey `L^{-1}=G_0`.

## N1 — Alternative routes

| Route | Attempt | Why it does not defeat the narrow claim | Marker and evidence |
|---|---|---|---|
| direct inversion | invert `L^{-1}=H^{-1}` to obtain `L=H` | inversion consumes the equality being derived; it does not supply it | ATTEMPTED; [source section 2](../../../../docs/GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md) |
| weak-field response | identify the field response with first-order propagator response | a supplied field kernel responds through `L^{-1}`; equating it to `H^{-1}` is the missing bridge | ATTEMPTED; source sections 1 and 6 |
| variational action | derive the field equation from stationarity | variation returns the chosen field kernel; `H`, `2H`, and `H(I+H)` arise from different allowed quadratic kernels | ATTEMPTED; exact countermodels in source section 1 |
| symmetry/Ward | impose translation, proper-cubic, self-adjoint, finite-range, and `Cl(3)` covariance | fixed-`H` fields `2H` and `H(I+H)` preserve every named symmetry | ATTEMPTED; [runner](../../../../scripts/frontier_gravity_full_self_consistency.py) |
| fixed point/backreaction | derive the Green map from convergence of the matter-field loop | the update map already contains its field-response kernel | ATTEMPTED; source section 6 |
| Record/readout | derive the field operator from fixed additive records | the premise source excludes source/action identification and dynamics | ATTEMPTED; [minimal axioms, lines 103-118 and 128-134](../../../../docs/MINIMAL_AXIOMS_2026-06-29.md) |
| static sector | equate field and propagator kernels after restricting to zero frequency | restriction leaves two independent spatial kernels and does not identify them | ATTEMPTED; `H` versus `H(I+H)` witness |
| convention/target | choose unit normalization or the `1/r` tail to set the field kernel | `c=1` cannot exclude the non-rescaling `H(I+H)` witness; `1/r` is the desired output | ATTEMPTED; source sections 1 and 6 |

N1 passes with eight distinct attempted routes directed at the audited
field/propagator bridge.

## N2 — Wall independence

The analysis exposes two independent questions:

- W1: with the massless propagator fixed, derive `L^{-1}=G_0`;
- W2: derive the propagator selector `H=-Delta_lat` from the minimal surface.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| W1, W2 | no: equality of field and propagator Green maps can hold for a massive `H_m` | no: fixing `H=-Delta_lat` still permits `L=2H` and `L=H(I+H)` | yes |

The headline theorem closes W1 negatively by holding W2 fixed as a
strengthening grant. The separate `H_m` family closes W2 negatively as a
secondary result. Neither wall is counted as evidence for the other.

## N3 — Hidden-wall scan

| Phrase/context | Classification | Action |
|---|---|---|
| fixed `H=-Delta_lat` and `G_0` | strengthening grant matching the audited packet | stated in the claim; not described as framework-derived |
| complete inverse graph | explicit domain/codomain condition | `H,L:X->Ran(H)` and inverses `Ran(H)->X` written out |
| conservative extension | model-theoretic construction | auxiliary `H,L,G` symbols do not modify any axiom fact |
| finite-torus inverse | non-load-bearing numerical companion | exact infinite-lattice Fourier/stencil proof remains decisive |
| `c` and `m^2` values | countermodel choices, not physical inputs | any allowed value suffices; integer representatives are runner witnesses |
| "natural" / "obvious" / "standard QFT" | absent from proof | no hidden premise |

No hidden condition changes the one-wall headline.

## N4 — Residual matching

| Witness | Witness residual and locator | Current residual | Match? | Use |
|---|---|---|---|---|
| quoted audit blocker | field Green map `L^{-1}` is identified with propagator `G_0` without derivation; `docs/audit/data/audit_ledger.json:408959-408977` | W1 | exact | target being closed negatively |
| [minimal axioms](../../../../docs/MINIMAL_AXIOMS_2026-06-29.md) | no Hamiltonian/transfer selection and no source/action identification; lines 103-118, 128-134, and 156-170 | W1 supplier scan | exact | load-bearing premise authority |
| [June weak-field response note](../../../../docs/GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md) | same-`H` gravitational mediation remains an irreducible primitive; lines 13-19 and 86-92 | W1 | exact | prior route warning only |
| [May hostile review](../../../../docs/CLOSURE_T2_GNEWTON_REAUDIT_NOTE_2026-05-10_t2gnewton.md) | static-sector privilege replaces rather than derives closure; lines 84-104 | W1 route | exact | prior route warning only |
| [finite preference note](../../../../docs/SELF_CONSISTENCY_FORCES_POISSON_NOTE.md) | preference within a tested family | logical W1 non-forcing | no | dropped as proof witness |
| [finite enumeration note](../../../../docs/POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md) | 21-candidate finite diagnostic | logical W1 non-forcing | no | dropped as proof witness |

The exact fixed-`H` countermodel is self-contained and does not depend on a
nonmatching prior no-go.

## N5 — Rhetoric audit

| Resolution | What is established | What is not claimed |
|---|---|---|
| operator graph | `H,G_0` fixed and two `L` graphs have unequal inverses | no claim about arbitrary unequal domains |
| per mode | exact multipliers differ at `k=(pi,0,0)` and on nonzero-measure momentum sets | no normalizable plane-wave eigenvector claim |
| finite stencil | `2H` remains nearest-neighbor; `H(I+H)` is range two | no all-finite-range classification |
| finite torus | massive inverse companions reproduce the algebra | finite quotients are not substituted for the infinite proof |
| lattice-wide | translation/proper-cubic/self-adjoint/internal-`Cl(3)` properties hold | no interacting nonlinear-gravity or empirical-viability claim |

The phrase "not forced" is restricted to logical implication from the named
current premise set. Future field-selection dynamics remain open.

## N6 — Partial-closure and primitive scan

The complete registry and every registered source were read:

- [`minimal_axioms`](../../../../docs/MINIMAL_AXIOMS_2026-06-29.md) supplies
  the four named axioms but no dynamics or source/action bridge;
- [`scale_reference_primitive`](../../../../docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md)
  supplies units only;
- [`kinetic_isotropy_primitive`](../../../../docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  supplies `c_t=c_s` form only, with no dynamics or selector;
- [`realized_state_primitive`](../../../../docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  supplies pointwise evaluation only, with no state or operator selector.

The open record-faithful dynamics PRs #5178, #5237, and #5250 were inspected.
They classify conditional dynamics families but explicitly leave physical
process selection open. They do not identify a separate field kernel with the
propagator kernel and are not proof dependencies.

A later reviewed field/action/response theorem could retire W1 without an
axiom amendment. Choosing `c=1` by convention would settle only normalization;
it cannot remove `H(I+H)`. The source therefore asks for a separate theorem,
not a new axiom.

## N7 — Steelman

The strongest objection is that the framework has one lattice and therefore
one natural scalar response kernel: once the propagator is fixed to the graph
Laplacian, self-consistency should require every weak scalar field to use the
same Green map. Differences such as `2H` are normalization, while `H(I+H)`
adds a higher-gradient term that a nearest-neighbor admissibility rule should
exclude.

This does not defeat the narrow theorem. "One lattice" supplies common
covariance, not equality of two independently named response operators.
`H(I+H)` is built entirely from the same graph operator, preserves every named
symmetry, and is not excluded because the premise source expressly says
Admissibility is not dynamics and chooses no Hamiltonian or transfer operator.
The steelman becomes a positive route only if a theorem turns common substrate
and field self-consistency into equality of the full inverse graphs; that is
exactly the missing bridge, not a premise of the countermodel.

## N8 — Cross-cycle echo

Prior gravity cycles replaced the bridge with "single lattice," weak-field
response, or static-sector language. The June response note still names
same-`H` gravitational mediation as primitive, and the May hostile review
still names static-sector privilege as modeling content. Neither residual has
been retired on `origin/main`.

The analogous
[`staggered-dirac-a1a2-realization-closure-20260710` no-go ledger](../staggered-dirac-a1a2-realization-closure-20260710/NO_GO_LEDGER.md)
constructs a current-minimal-surface Hamiltonian-selection countermodel. It is
not an authority for this result and does not identify field and propagator
operators; its relevant lesson is only that symmetry-compatible operator
families require a physical selector.

The open record-faithful dynamics PR stack was checked in N6. Its family
classification mechanism could inform a future selector theorem, but it has
not supplied the W1 bridge. The source boundary explicitly allows that future
mechanism to retire this no-go.

## Gate disposition

`PASS` for the narrow exact fixed-propagator non-forcing theorem. The checklist
does not support—and the source does not make—a universal claim that Poisson or
a future field-selection theorem is impossible.
