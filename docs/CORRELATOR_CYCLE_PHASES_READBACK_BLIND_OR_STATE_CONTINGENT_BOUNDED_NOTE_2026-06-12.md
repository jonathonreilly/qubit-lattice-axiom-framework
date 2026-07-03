# Tested Identity/Projector/Thermal Correlator Cycle Phases on the Circulant Surface Are Readback, Blind, or State-Contingent (Bounded)

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit any audit-lane-owned
registry, ledger, queue, or publication-status surface.
**Primary runner:** `scripts/frontier_correlator_cycle_phases_dichotomy_2026_06_12.py`
**Status:** source proposal; the audit lane grades. Runner
`PASS=30 FAIL=0`.

## Boundary

This note proves four bounded facts on the supplied three-site Hermitian
circulant surface: the identity-function readback case, the spectral-projector
blind case, the thermal state-contingent case, and the direct symmetric
inversion of `|delta|` on the stated branch. These checks rule out the tested
identity/projector/strictly mixing thermal classes as state-independent
derived-angle middlemen on this surface. They do not provide a carrier-class
exhaustion theorem, do not close the R-eta derivation question, do not probe
non-circulant surfaces, and do not claim the identification is underivable. The
note makes no R-eta claim either way. No fixed value of `r` is used, selected,
or preferred.

State-contingent cycle-phase values are registered state data under the
realized-state interface; they are not universal readout identifications, and
no universality is claimed.

## The supplied surface

Let

```text
H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T,
```

where `C` is the directed three-cycle shift, `a` is real, and `B > 0`. For a
spectral function `f`, set `G = f(H)`. The directed cycle phase is

```text
phi(delta) = arg(G_01 G_12 G_20).
```

On this circulant surface the three directed edge correlators are equal, so
`phi(delta) = 3 arg g(-1)` modulo the principal branch. The runner checks this
directed-product route and the polar-link route.

## Theorem

**Readback case.** For `f(x) = x`, so `G = H`,

```text
G_01 G_12 G_20 = B^3 exp(3 i delta),
```

hence `phi(delta) = 3 delta` exactly on the stated branch. This is a
consistency identity, not an independent derivation of the hopping phase; it
reads the supplied hopping phase back out of the object that already contains
it. Check tags: `readback-symbolic`, `readback-scan`.

**Projector-blind case.** For any nonzero band spectral projector on the
circulant family, `phi` is delta-independent. The structural reason is that
every member of the family has the same delta-independent Fourier eigenvectors.
The rank-one projectors are

```text
(P_k)_{xy} = omega^{k(x-y)} / 3,
```

with no `delta` anywhere. All delta-dependence of the family lives in the
eigenvalue multiset, not in the projector entries. Check tags:
`projector-symbolic`, `projector-scan`.

**Thermal state-contingent case.** For strictly mixing thermal functions

```text
f_beta(lambda) = 1 / (1 + exp(beta lambda)),  beta in {1, 4},
```

the phase is genuinely `K-ODD`: `phi(-delta) = -phi(delta)` on the wrapped
principal branch. It is also magnitude- and state-class-contingent. At
`delta = 2/9`, the runner prints the `(a,B)` grid spread
`1.3489178109943467` for `beta = 1` and `3.032326580315915` for `beta = 4`;
the cross-`f` spread reaches `1.6551489257862082`. The comparison table at
`delta = 2/9` keeps every tested thermal class farther than `0.1` from the
candidate constants tested by the runner. Per the realized-state interface,
these thermal values are registered state data, not universal readout
identifications. Check tags: `thermal-K-odd`, `thermal-grid`,
`thermal-comparison`.

**Tested-class middleman boundary.** The registered symmetric data determine
`|delta|` through the inversion

```text
e_3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta),
cos(3 delta) = (e_3 - a^3 + 3 a B^2) / (2 B^3),
|delta| = arccos(cos(3 delta)) / 3   on (0, pi/3).
```

The coefficient `3` is derived from the three-cycle determinant term and is
reproved here. For the classes actually tested by the runner, the only
outcomes are readback, blindness, or state-contingent registered data:
readback phases return the supplied hopping phase; projector phases are blind;
strictly mixing thermal phases are state-contingent registered data.

This does not exhaust all possible carrier-angle constructions. It says only
that the tested identity/projector/thermal classes do not supply a universal
state-independent middleman on this circulant surface. A full carrier-class
exhaustion theorem, or a new untested middleman construction, remains outside
this packet. Check tags: `inversion`, `dichotomy`.

## The next paths

Open-target update: the named residual is the **circulant-carrier phase
dichotomy wall for the tested classes**. The next paths are:

- a carrier-class exhaustion theorem for the circulant surface, if the goal is
  to rule out every state-independent middleman on that surface;
- non-circulant carriers, meaning surfaces where the eigenvectors move with
  the dynamics, including the full staggered lattice realization;
- the direct multiset-to-geometry equation, with no derived-angle middleman.

These paths remain open and are not probed here except for the tested
identity/projector/thermal classes.

## No-Go Discipline Gate

This gate applies only to the narrowed tested-class negative claim: on the
supplied circulant surface, the identity/projector/strictly mixing thermal
classes do not provide a state-independent derived-angle middleman between the
multiset-determined `|delta|` and the R-eta fixed-locus arithmetic. It is not a
carrier-class exhaustion theorem and not a global no-go for R-eta,
non-circulant carriers, untested carrier-angle constructions, or direct
multiset-to-geometry routes.

**N1 - Alternative route enumeration.**

| route | attempt | status for this surface | marker |
|---|---|---|---|
| Identity readback phase | Use `f(x)=x` and the directed cycle product. | Exact, but it reads back the supplied hopping phase already present in `H(delta)`. | ATTEMPTED |
| Spectral-projector phase | Use band projectors as state-independent spectral data. | Delta-blind because the Fourier eigenvectors do not move with `delta`. | ATTEMPTED |
| Thermal functional phase | Use strictly mixing thermal functions. | K-odd but state-contingent; values are registered state data under the realized-state primitive, not universal readout identifications. | ATTEMPTED |
| Candidate-constant matching | Search tested thermal classes at `delta=2/9` for a fixed value. | No tested class lands within `0.1` of the runner's candidate constants; this remains a bounded finite test, not a global exclusion. | ATTEMPTED |
| Direct multiset inversion | Use the derived `cos(3 delta)` relation to recover `|delta|`. | This bypasses a middleman rather than supplying one; direct matching to fixed-locus arithmetic remains open. | ATTEMPTED |
| Circulant carrier-class exhaustion | Prove every state-independent carrier-angle functional on the supplied circulant surface falls into readback, blind, or state-contingent behavior. | Not supplied here; explicitly left open. | NOT TESTED HERE |
| Non-circulant moving-eigenvector carriers | Move to surfaces whose eigenvectors vary with the dynamics. | Not tested here and explicitly left open. | NOT TESTED HERE |

**N2 - Wall-independence audit.** The wall set collapses to one surface-local
tested-class wall: none of the tested circulant phase carriers supplies a
state-independent derived-angle middleman. Readback, projector blindness, and
thermal state contingency are three faces of that one wall for the three tested
classes, not three independent framework admissions, and not a claim that every
carrier on this surface falls into one of these three faces.

**N3 - Hidden-wall scan.** "Supplied surface" is load-bearing and explicit;
"registered state data" is exactly the realized-state primitive boundary and
does not supply a state, selector, measure, weighting, probability, or typical
state; "candidate constants" are finite runner comparators only.

**N4 - Residual matching.** The residual matched here is the circulant-surface
tested-class middleman route. The note does not use this residual as evidence
against untested carrier-angle constructions, non-circulant carriers, the
direct multiset-to-geometry route, or R-eta itself.

**N5 - Rhetoric audit.** The negative is stated at tested-class surface
resolution: the identity/projector/strictly mixing thermal classes do not
supply a state-independent derived-angle middleman on the supplied circulant
surface. It is not stated at all-carrier, all-functional, all-state, or
framework-wide resolution.

**N6 - Partial-closure path scan.** No new axiom or primitive is requested.
The open closure paths are ordinary theory work: a carrier-class exhaustion
theorem on the circulant surface, non-circulant carriers with moving
eigenvectors, and a direct equation from multiset-determined `|delta|` to
fixed-locus arithmetic.

**N7 - Steelman.** A hostile reviewer could argue that the full staggered
realization is precisely the wrong object to model by a circulant surface: its
eigenvectors may move with the dynamics and create a genuine state-independent
carrier-angle functional. This note accepts that route as open.

**N8 - Cross-cycle echo.** The same pattern appears in the Hermitian-corner and
carrier-class eliminations: shortcuts can be ruled out on a named carrier while
the direct bridge remains open. This note preserves that distinction.

Gate outcome: PASS for the narrowed tested-class surface-local boundary; no
carrier-class exhaustion theorem and no global R-eta no-go are asserted.

## Repair (2026-06-20): narrowed to the tested bounded checks only

The audit lane re-audit asked for either a retained or packet-included
carrier-class exhaustion theorem, or a narrowing of the claim to the
identity/projector/thermal bounded checks only. This repair takes the narrowing
alternative; it does not attempt the carrier-class exhaustion theorem, which
remains an open bridge.

What changed:

- The title now reads "Tested Identity/Projector/Thermal Correlator Cycle
  Phases on the Circulant Surface Are Readback, Blind, or State-Contingent
  (Bounded)" instead of "Correlator Cycle Phases on the Circulant Surface Are
  Readback, Blind, or State-Contingent (Bounded)". The earlier title could be
  read as a trichotomy over every cycle-phase carrier on the surface; the new
  title scopes the trichotomy to the three classes actually computed and
  verified by the runner.
- The N2 wall-independence sentence now says the three behaviors are three faces
  of one wall "for the three tested classes ... and not a claim that every
  carrier on this surface falls into one of these three faces", instead of
  "three faces of that one wall on this surface". The earlier phrasing implied
  surface-wide coverage; the new phrasing restricts the trichotomy to the tested
  classes.

What did not change: every derived value, residual, and check in the runner is
unchanged. The carrier-class exhaustion question is framed throughout as an open
bridge that this packet does not supply, not as a theorem that is assumed. The
bounded facts verified are exactly the identity-readback case, the
spectral-projector blind case, the strictly mixing thermal state-contingent
case, and the direct symmetric inversion of `|delta|` on the stated branch.

The runner's dichotomy check is correspondingly stated only over the tested
classes (identity, rank-one/rank-two band projectors, thermal `beta in {1,4}`),
with no assertion that these classes exhaust the carrier-angle constructions on
the surface.

This source note does not set or predict an audit outcome.

## Does NOT

- Does not derive, refute, or grade R-eta.
- Does not set `r`, use a fixed `r`, or move the occupancy-selection question.
- Does not promote state-contingent thermal values to universal readout
  identifications.
- Does not exhaust all possible state-independent carrier-angle middlemen.
- Does not probe non-circulant carriers.
- Does not alter audit status, Tier-A registry text, or publication status.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  - registered-state-data interface used in the thermal state-contingent case.

## Context

Scope context, not dependency authority:
`INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md`
is the construction's home;
`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
is the determinant-holonomy Hermitian-corner companion;
`UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md`
is the carrier-class elimination context whose `cos(3 delta)` inversion is
reproved here;
`KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md`
is the R-eta chain context; and
`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
is where the fixed-locus arithmetic lives.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or context note. The independent audit lane is
the sole status authority.
