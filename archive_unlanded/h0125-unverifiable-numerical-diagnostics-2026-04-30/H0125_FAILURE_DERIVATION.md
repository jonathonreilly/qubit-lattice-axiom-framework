# Historical h=0.125 Failure-Diagnosis Packet (Retracted)

**Date:** 2026-04-06
**Status:** RETRACTED 2026-04-30 — audit failed; this note is archived under `archive_unlanded/h0125-unverifiable-numerical-diagnostics-2026-04-30/`. Claims below are NOT supported by current runners or current audit lane. See `## Retraction` section.

## Current-surface certificate (2026-06-12 source firewall)

**Actual current-surface status:** archived `audited_failed` / retracted
historical artifact. This file is kept only as audit history for a failed
or inconsistent route. It may not be cited as retained, bounded, conditional,
supporting, or methodological authority for any live framework chain.

## Retraction

- **Date archived:** 2026-04-30
- **Archive directory:** `archive_unlanded/h0125-unverifiable-numerical-diagnostics-2026-04-30/` (failure reason: unverifiable numerical diagnostics — the load-bearing numerical diagnosis is unsupported by any declared runner or one-hop derivation, and the explicit `P_det = (retention)^nl` formula is inconsistent with the printed P_det table by tens to more than one hundred orders of magnitude)
- **Audit verdict_rationale (quoted verbatim from [audit_ledger.json](../../docs/audit/data/audit_ledger.json)):**

  > Issue: the note's load-bearing numerical diagnosis is unsupported by any declared runner or one-hop derivation, and the explicit formula `P_det = (retention)^nl` is inconsistent with the printed P_det table by tens to more than one hundred orders of magnitude. Why this blocks: the retained negative claim depends on those numbers to distinguish boundary leakage, beam spreading, compounded loss, and statistical-noise AWAY behavior; without a reproducible computation or internally consistent formula, the diagnosis is not auditable. Repair target: add an executable h=0.125 failure diagnostic that computes T_interior/T_corner, beam sigma, detector probability including any geometric-spreading factor, and centroid SNR from the same propagation model, then update the note so every table entry follows from that runner. Claim boundary until fixed: safely claim only that boundary leakage and beam spreading are plausible failure hypotheses and that h=0.125 has not been retained by this note; do not retain the quantified root-cause diagnosis or SNR=0.5 noise conclusion.

- **Do-not-cite warning:** Do NOT cite the numerical results, tables, or threshold values in the original content below as live framework claims. The runners referenced in this note have been superseded or are no longer reproducible at the time of audit. If a future investigation revisits this physics, treat it as starting from scratch rather than as continuation of a "closed no-go".

## 2026-06-16 archive firewall

This archived packet is historical / diagnostic and retired as evidence. It is
not a retained h=0.125 failure derivation, not a quantified root-cause
diagnosis, and not authority for the printed detector-probability or SNR rows.

**Firewall runner:**
[`scripts/h0125_archive_firewall_2026_06_16.py`](../../scripts/h0125_archive_firewall_2026_06_16.py)
(`PASS: h0125 archive firewall holds`; cached at
[`logs/runner-cache/h0125_archive_firewall_2026_06_16.txt`](../../logs/runner-cache/h0125_archive_firewall_2026_06_16.txt)).

The old negative story is also not the current live h=0.125 status. The live
computable reduced-family lane is documented separately in
`docs/LATTICE_3D_L2_NUMPY_H0125_AUDIT_NOTE.md` with
`scripts/lattice_3d_l2_numpy_h0125_audit.py`; this archive does not supersede
or contradict that executable lane.

The only safe residue is the audit boundary: boundary leakage and beam
spreading remain plausible hypotheses, but the quantified root-cause diagnosis
and SNR=0.5 noise conclusion are not retained.

## Historical root-cause diagnosis (retracted)

The old body claimed that three independent mechanisms compound to destroy the
signal. The following sections are retained only as historical failed
diagnostic prose:

### 1. Historical boundary-leakage table (retracted)

The interior transfer norm T is used to normalize ALL nodes, but boundary
nodes have fewer valid edges. The corner transfer norm is only 44% of
interior T:

| h | T_interior | T_corner | corner/interior |
| ---: | ---: | ---: | ---: |
| 0.500 | 5.081 | 2.458 | 0.484 |
| 0.250 | 5.802 | 2.651 | 0.457 |
| 0.125 | 6.468 | 2.824 | 0.437 |

Boundary nodes retain only 44% of their amplitude per layer instead of 100%.

### 2. Historical beam-width table (retracted)

| h | beam sigma (mid) | W_phys | sigma/W |
| ---: | ---: | ---: | ---: |
| 0.500 | 3.10 | 10.0 | 0.31 |
| 0.250 | 3.06 | 10.0 | 0.31 |
| 0.125 | **6.10** | 10.0 | **0.61** |

At h=0.125, the beam sigma DOUBLES compared to h=0.5. This pushes
amplitude into boundary nodes where it leaks.

The sigma increase is from the finer lattice: more layers (241 vs 61)
means more steps for the beam to spread. The beam width grows as
sqrt(N) ~ sqrt(L/h), so sigma ~ sqrt(1/h). At h=0.125: sigma ~
sqrt(8) * sigma(h=1) ~ 2.8 * sigma(h=1).

### 3. Historical per-layer probability-loss table (retracted)

| h | nl | retention/layer | P_det |
| ---: | ---: | ---: | ---: |
| 0.500 | 61 | 0.890 | 3.7e-59 |
| 0.250 | 121 | 0.812 | 1.1e-88 |
| 0.125 | 241 | 0.727 | 1.6e-136 |

The printed `P_det` rows are not derived by this archive. The explicit
`P_det = (retention)^nl` formula is inconsistent with the printed table, which
is the load-bearing audit failure.

### 4. Historical AWAY/SNR explanation (retracted)

At P_det = 1.6e-136, the centroid measurement has SNR = 0.5 (below
the significance threshold of 3.0). The "AWAY" direction is statistical
noise from the 10^-136 amplitude, not a real physical effect.

## Historical proposed fixes (not live guidance)

Two things would resolve h=0.125:

1. **Per-node T normalization**: use T_i (the actual transfer norm for
   node i, accounting for its boundary position) instead of T_interior.
   This was tested and partially helps (P_det improves from 1e-137 to
   7e-99) but doesn't fully fix it because even the per-node T doesn't
   account for the beam spreading into more boundary nodes.

2. **Wider lattice**: W must scale as sqrt(1/h) to keep sigma/W constant.
   At h=0.125: need W ~ 10 * sqrt(4) = 20. This gives ~25M nodes,
   which is feasible with numpy but slow (~2 hours).

The old alternative to accept `h=0.25` as the finest confirmed spacing is not
current guidance from this archive. Consult the live h=0.125 audit note and
runner cache for the current executable reduced-family status.
