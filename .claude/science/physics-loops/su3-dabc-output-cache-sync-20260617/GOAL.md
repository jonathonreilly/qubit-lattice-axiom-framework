# Goal

Synchronize the canonical `outputs/su3_dabc_symmetric_check_2026-05-02.txt`
log with the already-repaired `scripts/su3_dabc_symmetric_check.py` runner and
`docs/SU3_DABC_SYMMETRIC_THEOREM_NOTE_2026-05-02.md` note.

The audit blocker named the C2 cubic-Casimir scalar as wrong. Current
`origin/main` already repairs the theorem text and runner to check
`d^abc T^a T^b T^c = (10/9) I3`; this branch updates the paired output log so
the source packet is internally consistent.
