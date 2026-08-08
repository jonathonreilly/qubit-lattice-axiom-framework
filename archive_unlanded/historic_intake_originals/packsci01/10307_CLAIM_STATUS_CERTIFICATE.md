# Claim-status certificate

```yaml
actual_current_surface_status: exact support/boundary theorem
claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
retirement_claimed: false
registry_edited: false
primitive_edited: false
axiom_edited: false
audit_status_set: false
publication_status_set: false
proposal_allowed: false
proposal_allowed_reason: physical mass-operator origin and invariant alignment remain open
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Bounded claim: for a supplied nondegenerate quark mass-operator pair with the
standard CKM semantics, spectral-projector overlaps exactly equal CKM moduli
squared. The desired five-sixths relation is exactly equivalent to one scalar
relative-alignment law. No universal equivariant/invariant down-only scalar
construction can recover CKM mixing on the full stated domain. The positive
identity and negative boundary are one mixed-role bounded row; no separate
`no_go` row is proposed.

Excluded claims:

- the framework derives `M_u` or `M_d`;
- the five-sixths alignment law is derived;
- the atlas six-state carrier is identified with generation flavor;
- an absolute mass, CKM value, RG law, or empirical agreement is predicted;
- the entire CKM closure target is retired.

## N1 — Alternative-route enumeration

The tested negative claim is only the universal factorization through data
from `H_d` alone, with equivariant operator construction and invariant scalar
readout. Routes that change that input domain remain live.

| Attack route | What it attempts | Why it does not defeat the scoped claim | Marker | Evidence |
|---|---|---|---|---|
| Arbitrary down-spectrum scalar | Set `|V_cb|=f(spec H_d)` without the six-state packaging | Fixed `H_d` supports continuously varying up-sector orientations and hence varying `|V_cb|` | ATTEMPTED | source note §5, equations (5.1)-(5.2) |
| Down-equivariant operator followed by invariant readout | Let eigenvectors or nonlinear functions inside `Phi(H_d)` restore orientation information | Equivariance plus conjugacy-invariant scalar output still gives a class function of the unchanged `H_d` | ATTEMPTED | source note Theorem 2 |
| Rank-`(1+5)` normalized determinant | Encode `R` as `X_R=Q+R(I-Q)` and read `det(X_R)^(1/6)` | It fixes the exponent but remains identical for two pairs with the same `H_d` and different relative orientation | ATTEMPTED | source note §§4-5; paired runner down-only countermodels |
| `C3` circulant carrier reuse | Use a cyclic generation carrier to select both a hierarchy and CKM orientation | The retained carrier boundary leaves sector phases, relative scales, and quark readout open; it does not supply this alignment | RULED OUT BY PRIOR | [`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md`](../../../../docs/QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md), lines 122-145 |
| Fixed external reference projector | Supply `P_ref` and read an overlap with a down-sector eigenspace | This can work only after adding an orientation carrier; the input is `(H_d,P_ref)`, not down-only | ATTEMPTED | source note §5 boundary paragraph |
| Supplied pair projectors | Consume `(H_u,H_d)` and read `Tr(P_c^uP_b^d)` | This succeeds and is the strongest escape, but changes the theorem's input domain rather than refuting it | ATTEMPTED | source note Theorem 1 |
| Paired texture or source/action dynamics | Derive both sectors and their relative eigenbasis jointly | This remains a positive route outside the down-only class; no claim here rules it out | ATTEMPTED | source note §§5 and 7 |

Seven distinct attacks were considered. Four are direct constructions within
the class; three are domain-changing escapes used to check that the theorem's
rhetoric does not foreclose viable paired routes.

## N2 — Wall-independence audit

The positive bridge has the collapsed wall set below.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| `W1`: derive and physically type `M_u,M_d`; `W2`: derive `Tr(P_c^uP_b^d)=R^(5/3)` | No: derived operators need not obey the alignment law | No: a conditional alignment law does not derive the operators | Yes |

The generation-flavor to six-state lift is route-specific. It is not counted
as a universal third wall because the direct projector-overlap route does not
need it.

## N3 — Hidden-wall scan

| Trigger hit | Location | Classification | Treatment |
|---|---|---|---|
| “supplied” mass operators | source note §§1-2 | Explicit supplied condition; already `W1` in the collapsed set | Listed in theorem conditions and import ledger |
| “Assume simple positive ordered spectra” | source note equation (2.2) | Explicit algebraic condition | Degenerate case and naming consequence stated |
| “standard CKM definition” | source note equation (2.4) | Explicit supplied physical semantics | Not described as a framework-derived fact |
| ordered `u,c,t` and `d,s,b` names | source note equation (2.2) | Non-load-bearing labeling convention | The general `i,j` theorem is algebraic before names are attached |
| abstract six-state `Q` | source note §4 | Explicit nonphysical packaging condition | No generation-to-six-state lift is claimed |
| atlas/STRC carrier context | source note §6 | Genuine non-load-bearing context | Explicitly not consumed as a dependency |

The scan found no remaining hidden condition and did not change the collapsed
two-wall set.

## N4 — Residual matching

| Witness | Witness residual | Current residual | Match? | Use |
|---|---|---|---|---|
| Parent loop [`NO_GO_LEDGER.md`](../ckm-down-scale-covariance-20260712/NO_GO_LEDGER.md), lines 3-12 | Casimir-identity, QCD, and scale-rescue routes do not supply the bridge | Universal down-only equivariant/invariant scalar readout | Partial/No; its orientation countermodel is evidence inside a narrower route row, not a proof of this class theorem | Target handoff only; dropped as proof witness |
| [`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md`](../../../../docs/QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md), lines 122-145 | A `C3` carrier does not supply sector phases/scales and quark readout | Universal down-only orientation readout | No | Dropped as proof witness; retained only as route-specific N1 pruning |
| [`OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md`](../../../../docs/OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md), lines 33-56 | Record plus determinant algebra does not force determinant-only readout | Universal down-only orientation readout | No | Dropped as proof witness; informs readout-premise disclosure only |
| [`QUARK_GENERATION_STRATIFIED_WARD_FREE_MATRIX_NO_GO_NOTE_2026-04-28.md`](../../../../docs/QUARK_GENERATION_STRATIFIED_WARD_FREE_MATRIX_NO_GO_NOTE_2026-04-28.md), lines 108-150 | Fixed CKM data do not determine Yukawa singular values | Fixed down data do not determine relative CKM orientation | No; converse information direction | Dropped as proof witness |

After nonmatching witnesses are dropped, the current theorem stands on its own
fixed-`H_d`, varying-`H_u` countermodel and does not require a witness count.

## N5 — Rhetoric and resolution audit

| Resolution | Tested? | Result allowed here |
|---|---|---|
| Individual spectral element/eigenvalue | Yes | The full down spectrum is fixed in the countermodel |
| Down-sector `3 x 3` operator | Yes | The whole operator `H_d` is fixed exactly |
| Equivariant operator image `Phi(H_d)` | Yes, abstractly | It is fixed/equivalent whenever `H_d` is fixed |
| Invariant scalar readout | Yes, abstractly | It cannot distinguish the two mass pairs |
| Pair-based mass-operator map | No; explicit escape | No negative claim |
| Source/action dynamics or lattice-wide construction | No | No negative claim |
| Global CKM closure or all textures | No | No negative claim |

The source uses only “universal down-only equivariant/invariant class.” It does
not promote the finite operator-pair result to a per-site, action-level,
lattice-wide, or global CKM no-go.

## N6 — Partial-closure paths

| Candidate path | Current status | What it could close | Classification |
|---|---|---|---|
| Pair spectral-projector overlap in the new source note, §§2-3 | Exact supplied-context result; independent audit pending | Physical CKM readout once the pair is supplied | Positive theorem path, already executed |
| Fixed `P_ref` orientation carrier | Open and not framework-typed | Down-sector readout relative to a supplied ray | Explicit bounded bridge path |
| Paired NNI or broken-`C3` source/action | Open; coefficients/source law not derived | `W2`, the relative alignment law | Future source/action theorem path |
| [`OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md`](../../../../docs/OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md) | Source proposal; current effective status unaudited; not consumed | Readout selection in its stated Record context, not CKM orientation | Candidate reframe/context path with nonmatching residual |
| Scale-reference, kinetic-isotropy, realized-state primitives | Approved but non-supplying for this residual | Units, kinetic form, pointwise state evaluation only | Not walls and not CKM closure paths |

No convention-only reframe, meta-ratification, or in-flight convention proposal
was found that closes relative up/down orientation. The negative claim does not
say a new axiom is required; theorem, source/action, or explicit bounded-bridge
retirement paths remain open.

## N7 — Hostile steelman

A hostile reviewer should reject any suggestion that the down-only obstruction
blocks the physics: the mass problem is relational, so the correct input is the
pair `(H_u,H_d)`, or a source/action object that generates both. The strongest
authority is the new source note's Theorem 1, which gives the exact escape
`Tr(P_i^uP_j^d)=|V_ij|^2`. A derived reference projector could also carry the
missing orientation. This steelman succeeds against an overbroad CKM no-go but
does not touch the stated theorem, because every successful route changes the
input from `H_d` alone to orientation-carrying relational data. The claim is
therefore kept at the narrow down-only class.

## N8 — Cross-cycle echo

| Prior wall | Status/mechanism | Could the mechanism apply here? | Incorporation |
|---|---|---|---|
| Parent CKM down-scale loop [`NO_GO_LEDGER.md`](../ckm-down-scale-covariance-20260712/NO_GO_LEDGER.md), lines 3-12 | Kept typed determinant/source-action routes open after scale-only failures | Yes; replace down-only data with a relational pair | Executed as Theorem 1 |
| T1-d determinant-context source proposal [`OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md`](../../../../docs/OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md) | Current effective status unaudited; proposes richer supplied context for a determinant-readout independence wall | Only at the readout layer; it cannot manufacture CKM orientation | Recorded as an unaudited candidate mechanism, not authority or a proof witness |
| Retained `C3` carrier boundary [`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md`](../../../../docs/QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md), lines 122-167 | Leaves species source/readout theorem as the retirement path | Yes, a sector-specific paired source law could close `W2` | Kept live in the opportunity queue |

The recurring retirement mechanism is richer, explicitly typed relational
context. This block applies that mechanism to the readout while preserving the
remaining source/action alignment target.

No-go discipline status: `PASS`.
