# Trace Gate: DM Neutrino Vsel Trace-Dimension No-Go Repair

```yaml
trace_class: direct_blocker_closure
target_claim_id: dm_neutrino_vsel_curvature_taste_to_dirac_transport_obstruction_no_go_note_2026-06-07
target_blocker_text: "supply a retained trace-normalization or representation bridge for the Dirac V_sel computation, or revise T2/T3 to the representation-independent d=Tr(I) form and rerun the audit"
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: no_go
next_trace_action: "Independent audit re-runs the repaired source note/runner and decides whether the no-go route-pruning row is clean."
```

The repair follows the auditor's second path. It does not try to supply or
admit a special Dirac trace normalization. Instead it removes the trace
normalization as a load-bearing premise.

The repaired no-go uses only:

- the retained premise form `M^2 = |phi|^2 I`;
- the symbolic trace dimension `d = Tr(I)`;
- the taste-cube selector already supported on its own graph-shift surface.

Under those premises,

```text
Tr M^(2n) = d |phi|^(2n)
Tr M^4 - (1/8)(Tr M^2)^2 = d(1-d/8)|phi|^4
Hess_e1 = diag(12c, 4c, 4c), c = d(1-d/8)
```

Thus the transported Dirac polynomial remains radial for arbitrary admissible
`d`, with equal transverse Hessian entries. The taste-cube curvature packet
`diag(0,64,64)` / `m_perp=32` still does not transport natively to the Dirac
Higgs family.
