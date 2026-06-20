# Claim Status Certificate — Block 01 (single-clock B-AXIS fresh attempts)

```yaml
actual_current_surface_status: no_go-supporting (branch-local stretch-attempt; B-AXIS stays live)
target_claim_type: derivation_of_B_AXIS_from_A_min (single physical clock: axis-label N4, absolute unit N2b, no-second-clock N5)
trace_class: negative_route_pruning
reachability_to_target: does_not_reach
conditional_surface_status: "four strongest never-built positive routes genuinely worked and either walled on a named A_min boundary (R-N5-IRR, R-N2b-JOINT, R-N4-AUT) or relocated to the record-production-dynamics / arrow open gate (R-N4-REGDIR); no crack"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Branch records honestly-run fresh attempts to close the N1 >=5-route enumeration and N7 steelman; it does not perform the independent audit and sets no status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: >
  Every route terminates on a named load-bearing wall with retained authority or
  on an explicit open gate, with a clean runner (TOTAL PASS, FAIL=0) — none
  derives B-AXIS, a second physical clock, an absolute clock unit, or a
  non-transportable axis-selector from A_min. The contribution is route pruning /
  steelman falsification (negative_route_pruning), not a closure or promotion.
```

## Machine-certificate index

| route | runner | PASS/FAIL | outcome | crack |
|---|---|---|---|---|
| R-N5-IRR | `scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py` | PASS=36 FAIL=0 | walled_named | no |
| R-N4-REGDIR | `scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py` | PASS=20 FAIL=0 | relocated_to_open_gate | no |
| R-N2b-JOINT | `scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py` | PASS=17 FAIL=0 | walled_named | no |
| R-N4-AUT | `scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` | PASS=16 FAIL=0 | walled_named | no |

Aggregate: 89 checks PASS, 0 FAIL, 0 cracks.

## Section / note references

- Stretch note: `docs/SINGLE_CLOCK_BAXIS_FRESH_ATTEMPTS_STRETCH_NOTE_2026-06-20.md`
- Per-route sections: `.claude/science/physics-loops/single-clock-baxis-wall/block01_section_{R-N5-IRR,R-N4-REGDIR,R-N2b-JOINT,R-N4-AUT}.md`
- Ledger update: `.claude/science/physics-loops/single-clock-baxis-wall/NO_GO_LEDGER.md` (## Block 01 fresh-attempt results)

## Scope boundary

R-N4-AUT's `|G_bare|=384` automorphism certificate and S4-isotropy enrichment
table are scoped to the EVEN-extent cubic staggered block (odd-L falsifier resid
6.000). Odd extent is a separate surface not covered.

Independent audit lane remains the sole status authority. This certificate sets
no audit or publication status.
