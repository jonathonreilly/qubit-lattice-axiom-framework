# Three-Generation Observable Theorem — Dep-Chain Audit

**Date:** 2026-05-02 (retired 2026-05-25 per audit-loop verdict)
**Status:** superseded / stale dep-chain status snapshot. Do **not** cite
this note for current dep-chain or effective-status information about
[`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md).
**Superseded:** the parent row `three_generation_observable_theorem_note`
was rewired in PR
[#1760](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1760)
(merged 2026-05-24), so the dependency boundary and per-dep effective
statuses recorded below are out of date. Audit-loop verdict at
2026-05-25 is `audited_failed` with auditor's repair hint:
*"other: refresh or retire this stale dep-chain audit note against the
current dependency boundary and effective-status table."* Following the
retire path. For the live dep boundary and effective statuses, consult
`docs/audit/data/audit_ledger.json` rows for
`three_generation_observable_theorem_note` and its current declared
dependencies, not this note.

---

**Date (original):** 2026-05-02
**Status (original):** dep-chain audit packet for
[`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
(currently `proposed_retained / audited_conditional`, td=302).

## 0. Audit context

Parent note has 5 deps. Verifying status at 2026-05-02:

| Dep | Status | Audit |
|---|---|---|
| `site_phase_cube_shift_intertwiner_note` | `support` | clean audit record ✓ |
| `s3_taste_cube_decomposition_note` | `proposed_retained` | clean audit record ✓ |
| `s3_mass_matrix_no_go_note` | `proposed_retained` | clean audit record ✓ |
| `z2_hw1_mass_matrix_parametrization_note` | `proposed_retained` | clean audit record ✓ |
| `generation_axiom_boundary_note` | `proposed_retained` | **audited_conditional** ❌ |

**4 of 5 deps have clean audit records.** Only `generation_axiom_boundary_note`
is conditional, blocking the parent's effective retention.

## 1. Implication for retention path

If `generation_axiom_boundary_note` lifts to retained (or its dep chain is
resolved per its audit verdict), `three_generation_observable_theorem_note`
becomes eligible for `proposed_retained` certification with all deps clean.

The blocking issue per `generation_axiom_boundary_note`'s verdict:
> *"the load-bearing move from exact observable separation to physical-
> species semantics, and the claim that substrate physicality is no longer
> a live boundary on the accepted one-axiom surface, rely on external
> accepted-Hilbert/physical-lattice-necessity inputs that are not
> dependencies of this row."*

This is the SAME shape as cycle 7 (`physical_lattice_necessity_note`'s
deps=[] but reads many upstream notes). Both rows need dep-declaration
repair.

## 2. Cluster identification

Two related lanes share the dep-declaration repair pattern:

- Cycle 7 (PR [#264](https://github.com/jonathonreilly/cl3-lattice-framework/pull/264)) — `physical_lattice_necessity_note` (td=301)
- This cycle — `generation_axiom_boundary_note` (td=303, would unblock `three_generation_observable_theorem_note` td=302)

Both cite the accepted-Hilbert / physical-lattice-necessity surface as
upstream authority but don't declare those as deps.

## 3. Recommended status correction

```yaml
# generation_axiom_boundary_note
deps: [
  single_axiom_hilbert_note,
  single_axiom_information_note,
  physical_lattice_necessity_note,
]   # was: []
current_status: bounded support theorem  # was: proposed_retained
```

After cycle 7 + this cycle's recommendations land:
- `physical_lattice_necessity_note`: deps declared, status `bounded support`
- `generation_axiom_boundary_note`: deps declared, status `bounded support`
- `three_generation_observable_theorem_note`: 4/5 deps have clean audit records; if
  the 5th (generation_axiom_boundary) is at least `bounded support` not
  `audited_conditional`, the parent's effective_status updates accordingly.

## 4. Seven retained-proposal certificate criteria

For `three_generation_observable_theorem_note` itself (after the
recommended dep cleanup):

| # | Criterion | Pass? |
|---|---|---|
| 1 | proposal_allowed | conditionally YES if all deps lift |
| 2 | No open imports | YES if generation_axiom lifts |
| 3 | No load-bearing observed/fitted | YES |
| 4 | Every dep retained | currently NO (1 of 5 conditional); could lift |
| 5 | Runner checks dep classes | runner exists at `scripts/frontier_three_generation_observable_theorem.py` |
| 6 | Review-loop disposition | PENDING |
| 7 | Independent audit required | YES |

## 5. What this review checks

- Dep-chain status verification (4/5 clean audit records)
- Cluster identification with cycle 7 (`physical_lattice_necessity_note`)
- Path to retention identified: lift `generation_axiom_boundary_note`

## 6. What this review does NOT close

- Lifting `generation_axiom_boundary_note` itself (separate work, similar
  to cycle 7 dep-declaration audit)
- Promotion of `three_generation_observable_theorem_note` (depends on the
  above)

## 7. Cross-references

- Parent: [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
- Bottleneck dep: `GENERATION_AXIOM_BOUNDARY_NOTE.md` (audited_conditional)
- Sister cycle: PR [#264](https://github.com/jonathonreilly/cl3-lattice-framework/pull/264) (cycle 7) — same-shape dep-declaration repair for `physical_lattice_necessity_note`

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [generation_axiom_boundary_note](GENERATION_AXIOM_BOUNDARY_NOTE.md)
- [site_phase_cube_shift_intertwiner_note](SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md)
- [s3_taste_cube_decomposition_note](S3_TASTE_CUBE_DECOMPOSITION_NOTE.md)
- [s3_mass_matrix_no_go_note](S3_MASS_MATRIX_NO_GO_NOTE.md)
- [z2_hw1_mass_matrix_parametrization_note](Z2_HW1_MASS_MATRIX_PARAMETRIZATION_NOTE.md)
- [physical_lattice_necessity_note](PHYSICAL_LATTICE_NECESSITY_NOTE.md)
