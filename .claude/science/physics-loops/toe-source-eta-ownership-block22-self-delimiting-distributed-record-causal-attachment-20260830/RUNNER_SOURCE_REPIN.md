# Block 22 primary-runner source re-pin

Status: **revised primary source frozen; revised execution not yet performed**

The first pinned primary source passed `17/17`, but the post-run completion
audit found that two preregistered controls were represented only implicitly:
the full commuting-projector square-root/Lueders poststate certificate and the
commuting orthogonal-Record escape from the complete-`M_2` QND boundary.  That
is an evidence-coverage defect, not a failed physics identity.  The first cache
remains committed and recorded in `EXECUTION_HISTORY.md`.

Before executing the revised source, the primary runner was extended to:

1. construct all `14 x 64` square-root sectors and verify their exact Walsh
   reconstruction, including absence of higher products;
2. check exact branch probability and normalized Lueders output on a
   correlated live/reference-entangled two-sector fixture for every effect;
3. execute a CNOT control showing that commuting orthogonal labels can be
   copied QND while a noncommuting superposition cannot; and
4. make the symbolic source-moment composition with distinct linear forward
   and actual-reverse consumers explicit.

Revised primary source:

| field | value |
|---|---|
| commit | `6ff70f75716448a7bdf2ecf9e2c3a01794ff881f` |
| path | `scripts/admissibility_d4_block09_povm_radial_record_writer_2026_08_30.py` |
| SHA-256 | `5a987385123b560c4851ed5cf0c1d6b2b2bd66c05320a78163c0fcf763bbf2cf` |

The independent source and its first authoritative cache are unchanged.  Any
result for the revised primary source is authoritative only if the source hash
above matches at execution.

