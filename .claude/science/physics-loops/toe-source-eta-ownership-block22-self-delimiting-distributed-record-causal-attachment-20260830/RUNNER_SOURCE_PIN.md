# Block 22 runner-source pin

Status: **source frozen; authoritative execution not yet performed**

The preregistration packet was frozen at `e210adbba5`.  The two independently
implemented runner sources were first committed together at `d5f3196417`.
Before either runner was executed, the methodology-freshness check found that
`origin/main` required the five canonical N5 resolution lines to land in the
primary runner cache.  Those output-only certificate lines were added and
committed at the final pre-execution source commit
`14b9ce42b21d0874750e27f82bc57cc0a8a52be0`.

Pinned sources:

| role | path | SHA-256 |
|---|---|---|
| primary | `scripts/admissibility_d4_block09_povm_radial_record_writer_2026_08_30.py` | `80c646f09c8066c60a9ebcb3cb2413d3476c13091064512e4cee3d2f0e7ecc75` |
| independent | `scripts/independent_admissibility_d4_block09_povm_radial_record_writer_2026_08_30.py` | `2b4116ad201b71d609e71b97b8884a4cffe277c7e5d9562e90b22e58984581c7` |

No compile, import, or runner execution occurred before this final pin.  Any
later source correction must receive a new commit and hash before its result
can be called authoritative; failed executions remain part of the cycle
history rather than being silently erased.

