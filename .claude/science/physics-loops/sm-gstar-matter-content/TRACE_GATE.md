# TRACE GATE — SM g_* matter-content derivation

```yaml
trace_class: direct_blocker_closure
target_claim_id: sm_relativistic_dof_count_import_note_2026-05-17
target_blocker_text: "The declared Standard Model inventory remains an external physical input. This finite declared-inventory arithmetic certificate is not a framework derivation of which particles nature contains."
source_of_blocker_text: source_note_and_audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "After audit ratification of this bounded assembly, queue retirement of the named residuals (U(1)_Y existence, single-Higgs-doublet minimality, one-generation matter completion, full fermionic-SB, massless-vector 2-pol pending emergent-Lorentz) so the assembly's residual fraction shrinks toward a fully framework-sourced census."
```

## How the artifact retires the import

The target note `sm_relativistic_dof_count_import_note_2026-05-17`
(`retained_bounded`) is an exact arithmetic certificate that, GIVEN the
*declared* SM inventory (bosonic 28, fermionic 90, weight 7/8), yields
`g_* = 106.75`. Its load-bearing limitation, stated in its own Boundary
section, is that there is **no framework derivation of the inventory** — the
particle census is a monolithic external SM physical input.

This artifact retires the **monolithic external** status of that inventory:

1. **Bosonic 28 = gauge 24 + Higgs 4.** Gauge 24 is sourced as SU(3) (8 gen,
   **retained** via graph_first_su3 / cl3_color_automorphism / native_gauge) *
   2 transverse pol (massless-vector note, residual R-POL) = 16; SU(2) (3 gen,
   **retained** via native_gauge Cl(3) bivectors) * 2 = 6; U(1)_Y (1 gen,
   **residual R-U1Y**, hypercharge-uniqueness note unaudited) * 2 = 2. Higgs 4
   = one complex doublet (4 real scalar dof; single-doublet is **residual
   R-HIGGS**).
2. **Fermionic 90 = 3 generations (retained, I6) * 30 per generation.** The 30
   is sourced from one-generation matter content (one_generation_matter_closure
   unaudited + anomaly singlet completion retained_bounded + hypercharge values)
   with N_c=3 (retained) and Dirac/Weyl spin*antiparticle counts (spin-1/2
   audited_conditional + cardinality retained).
3. **Weight 7/8** sourced from the **retained** ratio
   hierarchy_seven_eighths (+ unaudited substrate fermionic-SB, residual R-FSB).

The result: the inventory is no longer an opaque external SM census. It is a
**framework-internal assembly** in which the gauge-group structure (SU(3),
SU(2)), the generation count (3), the color count (3), the spin-statistics
cardinality, and the 7/8 ratio are sourced from **retained** framework
authorities, and the remaining pieces (U(1)_Y existence, single Higgs doublet,
one-generation matter completion, full fermionic-SB, massless-vector 2-pol,
per-site spin-1/2) are **named residuals that are themselves framework-
derivation targets** — NOT external SM imports.

## Why partially_closes, not closes

`reachability_to_target: partially_closes` is the honest classification:

- The **monolithic external** status of the census is retired (the genuine
  advance). The census is replaced by a framework assembly with named internal
  residuals.
- But the census is **not fully framework-derived**: U(1)_Y existence, single
  Higgs doublet, one-generation matter completion, full fermionic-SB, and
  massless-vector 2-polarization remain unaudited/convention-bearing residuals.
  These are framework-derivation targets, not external SM imports, but they are
  not yet retained.

So the blocker is **partially** retired: the inventory's external-import status
is converted to a framework-internal assembly, while the residual derivations
are queued (HANDOFF.md) on the legitimate import -> bounded -> retire path.

## Trace-rule compliance

- `direct_blocker_closure` requires an exact quoted blocker (provided above
  from the target note's own text) and a concrete statement of how the artifact
  retires it (provided: the per-dof sourcing decomposition).
- The proposed claim type is `bounded_theorem`, NOT retained/positive, so the
  retained-grade certification chain is not invoked; the certificate
  (CLAIM_STATUS_CERTIFICATE.md) records `audit_required_before_effective_retained:
  true` and `bare_retained_allowed: false`.
