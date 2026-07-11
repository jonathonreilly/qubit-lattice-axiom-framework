# Theta Mass Determinant Axiom-Update No-Go

**Date:** 2026-07-04
**Type:** no_go
**Claim type:** no_go
**Scope boundary:** bounded no-go against retiring the theta mass-side
determinant-readout bridge by appeal to the updated four axioms or approved
primitives. This note does not derive, refute, re-grade, retire, or remove
theta, does not set `theta_bar = 0`, and does not create any admission registry,
axiom, primitive, audit verdict, or publication-status surface.
**Audit boundary:** independent audit lane only.
**Current-main posture (2026-07-11):** theta's gauge-side retained disposition
remains; its mass-side K-real leg is conditional on the open AC occupancy and
quark-determinant cross-sector readout obligations. The AC governance-only channel was withdrawn;
that correction does not affect this historical mass-side result.
**Primary runner:**
[`scripts/theta_mass_determinant_axiom_update_no_go_2026_07_04.py`](../scripts/theta_mass_determinant_axiom_update_no_go_2026_07_04.py)

## Target

The admission-era decision history recorded two residual atoms:

```text
gauge_side_winding_account
mass_side_orientation_determinant_readout_bridge
```

This note attacks the second atom only. The question is whether the updated
axioms or approved primitives already supply the determinant-channel interface
and physical-exhaustion bridge needed to remove the mass-side orientation
premise. They do not.

## Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  four approved axioms: Lattice, Qubit, Admissibility, and Record.
- [`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) is the
  retained-bounded selected-surface theta parent; it is explicitly conditional
  on a theta-free Wilson-plus-staggered scalar-mass surface and positive real
  mass orientation.
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  supplies pointwise realized-state evaluation only.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  supplies only the structural kinetic-form ratio `c_t = c_s`.
- `docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`
  names the theta mass-side determinant-readout bridge.

Context only, not dependency links: the June determinant-character and
determinant-readout bridge notes prove useful conditional algebra, but they
are not used as load-bearing dependencies here. The small determinant-channel
facts needed below are rechecked directly by the runner.

## Theorem

The updated axiom/premise surface does not supply the theta mass-side
determinant-readout bridge. More explicitly:

```text
Lattice + Qubit + Admissibility + Record
+ approved primitives
do not supply
  the physical determinant-channel readout interface,
  independent-block determinant multiplication as the physical mass readout,
  K/CPT orbit registration for that channel,
  or exhaustion of arg det(M_u M_d) by the phase-free determinant character.
```

The Record axiom supplies readable fixed records and finite scalar additivity
over disjoint records. It does not supply a readout context, determinant
channel, `K`/CPT structure, central-sector decomposition, action/mass surface,
or physical observable identification. The Qubit axiom's `M_2(C)` one-site
possibility algebra, and its equivalent `Cl(3,0)` presentation, does not
select the quark mass determinant channel or a positive real orientation.
Admissibility supplies nearest-neighbor availability, not a scalar-mass action
class, determinant-order selector, or topological-sector bridge.

Thus the determinant phase-erasure algebra is a conditional tool, not an
axiom consequence.

## Exact Determinant-Character Check

If a determinant-channel interface is supplied, independent blocks compose by

```text
det(M_1 direct_sum M_2) = det(M_1) det(M_2).
```

A continuous multiplicative phase readout on the determinant phase circle has
the character form

```text
chi_k(e^{i phi}) = exp(i k phi),  k in Z.
```

If the supplied channel also registers `K`/CPT orbits by identifying
`phi` and `-phi`, then an admissible determinant phase character must obey

```text
exp(i k phi) = exp(-i k phi) for all phi.
```

The only character satisfying that condition is `k = 0`; within the supplied
determinant-character class, the registered phase character is erased.

This does not follow from K-evenness alone. `cos(phi)` is K-even and
phase-sensitive. It is excluded only after the determinant-channel
multiplicative/block-composition law is supplied, because

```text
cos(phi + psi) != cos(phi) cos(psi)
```

for generic independent phases. Record additivity alone also permits K-even
phase-sensitive sums over disjoint records, such as
`cos(phi_1) + cos(phi_2)`. The determinant-channel homomorphism boundary is the
extra bridge.

## What This Moves

| Before | After |
|---|---|
| The updated Qubit/Record text could be over-read as supplying the mass determinant readout. | It is certified as non-supplying the determinant-channel interface and exhaustion bridge. |
| K-real phase erasure could be mistaken for a theta mass-side retirement. | It is classified as conditional algebra inside a supplied determinant-channel class. |
| The retained theta parent could be read as an unconditional axiom derivation. | It remains a selected-surface theorem conditional on theta-free action and real positive mass orientation. |

## What Does Not Move

- Theta is not retired.
- No admission registry is created.
- The gauge-side winding account is untouched.
- No physical quark-sector determinant readout is derived.
- No positive real mass orientation is derived from the axioms.
- Future determinant-channel or scalar-mass action-surface theorems remain
  open.

## Remaining Live Routes

1. **Mass determinant-channel theorem.** Derive that the physical
   `arg det(M_u M_d)` contribution is exhausted by the determinant-channel
   record readout whose phase character has `k = 0`.
2. **Scalar-mass action-surface theorem.** Derive the scalar-mass-only,
   positive-orientation surface rather than supplying it as a selected
   surface.
3. **Joint gauge/mass theorem.** Keep the invariant combination
   `theta_bar = theta_gauge + arg det(M_u M_d)` honest while moving the mass
   side.
4. **Approved-primitive route.** Approve a narrow determinant-readout primitive.
   That would be governance, not derivation.

## No-Go Discipline Gate

**N1 alternative route enumeration.** Each route is tested against current
foundation text and direct runner evidence:

| Route | Marker | Evidence and disposition |
|---|---|---|
| Qubit/Admissibility/Record shortcut | ATTEMPTED | The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) withholds K/CPT structure, quark determinant carrier, action, and physical readout; runner sections C-D. |
| realized-state shortcut | ATTEMPTED | The [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) supplies pointwise evaluation only, not the determinant channel; runner section D. |
| kinetic-isotropy shortcut | ATTEMPTED | The [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) fixes only kinetic graining; runner section D. |
| K/CPT determinant-character route | ATTEMPTED | Runner sections F-G independently recover `k=0` inside the explicit multiplicative character class; this does not identify the physical quark channel. |
| scalar-mass action route | ATTEMPTED | Signed-mass pairing algebra is preserved as conditional support; the physical scalar-mass action remains open. |
| cross-sector determinant-readout route | ATTEMPTED | The exact zero-weight [theta obligation](THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md) records the missing carrier/readout theorem without supplying it. |
| joint gauge/mass route | ATTEMPTED | The runner preserves `theta_bar`; no mass-side step closes the gauge-side winding account. |

**N2 wall independence.** The mass-side target contains four independently
closable steps:

| Step | Closing it does not close |
|---|---|
| scalar-mass action surface | determinant-channel identification, K/CPT registration, exhaustion |
| determinant-channel identification | action selection, K/CPT registration, exhaustion |
| K/CPT registration | action selection, determinant identification, exhaustion |
| physical-channel exhaustion | action selection, determinant identification, K/CPT registration |

This note establishes only their joint non-supply by the current foundation;
it does not collapse them into one wall.

**N3 hidden-wall scan.** The note and runner were scanned for `assume`,
`supplied`, `registered`, `canonical`, `standard`, `background`, `naturally`,
`obviously`, `primitive`, and `by construction`.

| Hit | Classification |
|---|---|
| supplied determinant/mass channel wording | explicit theorem condition, not foundation content |
| registered determinant character/readout | scoped mathematical class or target vocabulary, not physical carrier authority |
| approved-primitive route | future governance path, not used in the proof |
| historical decision text | provenance only and non-evidence |

No measured neutron-EDM bound, comparator, fitted value, axion assumption,
determinant-channel primitive, or positive mass-orientation primitive is
imported.

**N4 residual matching.** The cited surfaces are matched to the exact current
residual:

| Surface | Residual there | Residual here | Match/disposition |
|---|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | no K/CPT, quark determinant carrier, action, or readout | the four independent mass walls | exact foundation-boundary match |
| `THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md` | `k=0` inside a conditional determinant-character class | K/CPT registration only | partial closure; does not supply carrier/exhaustion |
| `THETA_MASS_SIDE_COMPOSITION_CLOSE_ON_SHARED_OCCUPANCY_BRIDGE_BOUNDED_NOTE_2026-07-03.md` | occupancy and cross-sector readout are independent conditions | cross-sector determinant readout | exact split match |
| [theta cross-sector obligation](THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md) | construct carrier, readout, and cross-sector correspondence | same physical-channel exhaustion wall | exact target match; zero premise weight |
| historical decision text | former target wording | none | provenance, dropped as evidence |

**N5 proven surface.** Proven here is an axiom/primitives non-supply result
plus exact determinant-character checks. It is not a universal no-go against
future determinant-channel or scalar-mass action-surface theorems.

**N6 partial closure.** The target is sharpened: derive the action,
determinant-channel, K/CPT registration, and exhaustion steps. Partial closure
is recorded stepwise.

**N7 steelman.** A reviewer can say the determinant-character `k = 0` algebra
is exactly the right mass-side route. Correct: this note preserves that route.
It only says the route's interface is not in the current axioms/primitives.

**N8 cross-cycle echo.** Repo cross-cycle inventory:

| Cycle | Prior retirement/closure mechanism | Applicability here |
|---|---|---|
| AC occupancy | remains a zero-weight statistical-grain obligation | closing it does not identify the quark determinant channel |
| R-eta | same-observable/readout theorem remains open after countermodels | confirms that algebraic equality is not physical readout authority |
| theta mass composition | explicitly split into occupancy and cross-sector obligations | exact current mechanism; both must close independently |
| determinant-character phase erasure | closes the character coefficient only inside its stated class | does not construct the physical carrier, action, or exhaustion theorem |

No prior cycle provides a retained mechanism that closes all four mass walls.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_mass_determinant_axiom_update_no_go_2026_07_04.py
```

Expected close: `FAIL=0` with at least 100 checks.

## Current Dependency Routing (2026-07-11)

Historical decision records have zero premise weight. The unresolved content
used by this note is routed through the following current foundation or
zero-weight open obligation:

- [`THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md`](THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md)
