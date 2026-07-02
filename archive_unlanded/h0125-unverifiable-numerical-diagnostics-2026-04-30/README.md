# Archive: h0125 failure derivation — unverifiable numerical diagnostics

**Archived:** 2026-04-30 (README added 2026-05-01)
**Audit verdict:** audited_failed (terminal; ACCEPT)

## 2026-06-16 archive firewall

This directory is historical / diagnostic and retired as evidence. The old
negative diagnosis is not a retained h=0.125 failure theorem, and it should
not be used to override the current computable h=0.125 audit lane in
`docs/LATTICE_3D_L2_NUMPY_H0125_AUDIT_NOTE.md`.

The source firewall is executable:

- runner: [`scripts/h0125_archive_firewall_2026_06_16.py`](../../scripts/h0125_archive_firewall_2026_06_16.py)
- cache: [`logs/runner-cache/h0125_archive_firewall_2026_06_16.txt`](../../logs/runner-cache/h0125_archive_firewall_2026_06_16.txt)
- expected output: `PASS: h0125 archive firewall holds`

The safe use is narrow: this archive records a failed diagnosis pattern. The
current live question must be answered from executable runners and their
current caches, not from the stale `P_det`/SNR table below.

## Why this is here

`H0125_FAILURE_DERIVATION.md` was a proposed_retained negative claim
("h=0.125 failed, diagnosed by boundary leakage + beam spreading +
compounded probability loss + SNR=0.5"). The audit found it does not
close on its own terms:

- The note has **no runner** and **no cited authority** for the transfer
  norms, beam widths, detector probabilities, or SNR figures it tabulates.
- The explicit formula `P_det = (retention)^nl` printed in the note is
  inconsistent with the printed P_det column by tens to **more than one
  hundred orders of magnitude** (e.g. retention^nl ≈ 8.18e-4 vs printed
  3.7e-59 for one row).

The diagnosis is therefore not auditable as written. The repair target
(per the audit) is to write an executable h=0.125 failure diagnostic that
computes T_interior/T_corner, beam sigma, detector probability with any
geometric-spreading factor, and centroid SNR from the same propagation
model — and then update the note so every table entry follows from that
runner.

That repair has not been done. Until it is done, the safe scope is:
"boundary leakage and beam spreading are plausible failure hypotheses for
h=0.125; the quantified root-cause diagnosis and the SNR=0.5 noise
explanation are NOT retained."

## Status

Archived as a terminal-failed historical record. The audit row
`h0125_failure_derivation` will remain `audited_failed` until and unless
the repair runner is written and the note is rewritten against it.
