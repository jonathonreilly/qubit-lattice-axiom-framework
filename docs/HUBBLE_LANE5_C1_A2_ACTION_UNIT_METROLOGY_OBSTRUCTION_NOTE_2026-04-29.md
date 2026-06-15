# Lane 5 `(C1)` A2 Action-Unit Metrology Obstruction Note

**Date:** 2026-04-29
**Type:** bounded_theorem (axiom-reset retag 2026-05-03; was positive_theorem)
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane. This source note does not set,
predict, promote, or demote any audit outcome and does not edit audit-owned
registry, ledger, queue, or publication-status surfaces.
**Admitted context inputs:** (1) staggered-Dirac realization derivation target,
registered as Tier-A target `AC_phi_lambda` through canonical parent
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`; (2) supplied
`g_bare = 1` parent gate (canonical parent:
[`G_BARE_DERIVATION_NOTE.md`](G_BARE_DERIVATION_NOTE.md)). Neither input is
treated here as retained authority.
**Source scope:** current-surface negative boundary result. This note does not
close `(C1)`, does not close or promote `g_bare = 1`, and does not promote any
theorem or claim.
**Boundary summary:** supplied `g_bare = 1` parent gate; neither input is treated here as retained authority; registered Tier-A derivation target `AC_phi_lambda`; this note does **not** close that gate.
**Primary runner:** `scripts/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.py`
**Runner cache:** `logs/runner-cache/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.txt`
**Lane:** 5 -- Hubble constant derivation, `(C1)` absolute-scale gate

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency, context note, premise, or bridge. The
independent audit lane is the only status authority.

## Purpose

The A1 stretch attempt showed that bulk Grassmann/CAR structure does not
descend to `P_A H_cell` without a projection/morphism theorem. A2 tests the
other half of the `(C1)` residual:

```text
Can supplied `g_bare = 1`, the accepted plaquette/u_0 surface, and the
minimal APBC hierarchy block pin the absolute action unit on `P_A H_cell`?
```

The answer is no on the current surface. Those supplied inputs are support
for dimensionless lattice normalization, coupling transport, and hierarchy
scaling. They do not break the Target 3 `(S, kappa)` rescaling degeneracy.
This note does **not** claim retained `g_bare`; it only proves that even a
supplied `g_bare = 1` boundary does not determine dimensional action units.

## Minimal Premises Used

- `g_bare = 1` as a supplied-boundary input, not retained authority from this
  note.
- Wilson plaquette surface at `beta = 2 N_c / g_bare^2 = 6`.
- Same-surface plaquette constant `<P> = 0.5934` and
  `u_0 = <P>^(1/4)`.
- Minimal APBC hierarchy block, including the dimensionless factor
  `(7/8)^(1/4)` and the exact `m/u_0` homogeneity statement.
- `P_A H_cell` with `rank(P_A)=4` and `c_cell = 4/16 = 1/4`.

No measured value of `G`, `hbar`, `M_Pl`, `l_P`, `H_0`, or any cosmological
observable enters this obstruction.

## Result

The A2 inputs pin dimensionless data:

```text
g_bare = 1,
beta = 6,
u_0 = <P>^(1/4),
C_APBC = (7/8)^(1/4),
c_cell = 1/4.
```

They do not pin an absolute dimensional action quantum `kappa`. For any
positive scale `lambda`, the replacement

```text
S_dim -> lambda S_dim,
kappa -> lambda kappa
```

leaves all Hilbert phases and all Euclidean lattice weights determined by the
dimensionless action unchanged:

```text
exp(i S_dim/kappa) = exp(i lambda S_dim / lambda kappa).
```

The plaquette and APBC constants remain unchanged because they are
dimensionless observables of the lattice partition function. The primitive
trace `c_cell = 1/4` also remains unchanged. Therefore the A2 input set
admits a one-parameter family of action-unit readings with identical
dimensionless physics.

## Runner Witness

The runner checks eight facts.

1. `g_bare = 1` fixes the Wilson gauge point `beta = 6`.
2. The canonical plaquette surface gives dimensionless `u_0`, `alpha_LM`,
   and `alpha_s(v)`.
3. The APBC hierarchy factor is dimensionless.
4. Hilbert phases are invariant under common `(S_dim, kappa)` rescaling.
5. The Wilson/plaquette Boltzmann weight depends on the dimensionless
   lattice action, not on an external `kappa`.
6. The primitive `P_A` coefficient stays `1/4` under all action-unit readings.
7. A family of different `kappa` values gives the same projected phase on
   `P_A H_cell`.
8. Finite matrices still cannot realize a nonzero exact canonical action
   commutator on the rank-four block.

Current output:

```text
TOTAL: PASS=8, FAIL=0
```

## Claim Boundary

This note does **not** weaken or promote the `g_bare` packet, the plaquette
surface, the APBC hierarchy support theorem, or the conditional Planck packet.
It only closes the direct A2 shortcut, even when `g_bare = 1` is supplied:

```text
g_bare = 1 + plaquette/u_0 + APBC hierarchy + c_cell = 1/4
  => absolute action-unit metrology on P_A H_cell.
```

The missing import is now explicit:

```text
a physical clock/source/action metrology map tying the dimensionless lattice
action and P_A boundary carrier to a particular dimensional kappa.
```

Equivalently, A2 can become positive only if a new theorem couples the
canonical dimensionless lattice action to the primitive boundary/action
carrier in a way that is not invariant under
`(S_dim, kappa) -> (lambda S_dim, lambda kappa)`.

## Surviving Routes

- A4 parity-gate-to-CAR audit: test whether the primitive parity-gate carrier
  route supplies a stronger bridge to the native CAR/coframe response.
- Prove the missing A1 `P_A` Clifford/CAR module-morphism theorem.
- Add a minimal carrier/metrology axiom and keep `(C1)` conditional rather
  than promoted.

## Review Boundary

Safe wording:

> The A2 stretch attempt exposes an action-metrology import: supplied
> dimensionless lattice normalizations (`g_bare`, `beta`, `u_0`, APBC) do not
> by themselves choose the dimensional action quantum on `P_A H_cell`.

Unsafe wording:

> The canonical plaquette/u_0 surface derives `hbar` or the absolute Planck
> action unit.

That stronger statement is blocked by the rescaling witness above.


## Hypothesis set used (source-boundary repair 2026-06-12)

Per the current minimal-axiom surface
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md), this note
depends on **both** open gates:

1. **Staggered-Dirac realization derivation target** — canonical parent note:
   `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`, routed through the
   registered Tier-A derivation target `AC_phi_lambda`.
2. **`g_bare = 1` parent gate** — canonical parent:
   [`G_BARE_DERIVATION_NOTE.md`](G_BARE_DERIVATION_NOTE.md), with supporting
   surfaces including
   `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`,
   `G_BARE_RIGIDITY_THEOREM_NOTE.md`,
   `G_BARE_TWO_WARD_CLOSURE_NOTE_2026-04-18.md`,
   `G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md`,
   `G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md`,
   `G_BARE_DYNAMICAL_FIXATION_OBSTRUCTION_NOTE_2026-04-18.md`, and
   `G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md`.

The note produces a negative boundary over supplied gauge-normalization and
carrier inputs. It does not independently derive `g_bare = 1`, and it does
not use `g_bare = 1` to make a positive metrology claim. The conclusion is
more conservative: even after supplying that dimensionless normalization,
the dimensional action quantum remains unselected by A2.

Therefore `claim_type: bounded_theorem` is the source-note classification
until the independent status process decides otherwise. The substantive
science content of this repair is unchanged: A2 is a no-go for dimensional
action-unit metrology from the listed dimensionless inputs.

## Registered Dependency Routing

This graph-bookkeeping section records the dependency-routing case without
asserting any audit or effective-status outcome.

- [staggered_dirac_realization_gate_note_2026-05-03](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- `AC_phi_lambda` in `docs/audit/data/tier_a_admissions.json`
- [g_bare_derivation_note](G_BARE_DERIVATION_NOTE.md)

The staggered-carrier input is routed through the registered Tier-A target.
The `g_bare = 1` input remains a supplied parent-gate boundary for this
obstruction, not retained authority. This note does **not** close that gate.
