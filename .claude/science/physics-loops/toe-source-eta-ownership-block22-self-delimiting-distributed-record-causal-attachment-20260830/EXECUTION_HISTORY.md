# Block 22 execution history

There was one authoritative execution of each pinned runner and no discarded
or superseded runner attempt.

| role | pinned source SHA-256 | exit | checks | hostile mutations | cache SHA-256 |
|---|---|---:|---:|---:|---|
| primary | `80c646f09c8066c60a9ebcb3cb2413d3476c13091064512e4cee3d2f0e7ecc75` | 0 | 17/17 | 27/27 | `c4ad88865d6b503ba819e861b2210f2a7876cd6a6983d1ed425bafcb1697e596` |
| independent | `2b4116ad201b71d609e71b97b8884a4cffe277c7e5d9562e90b22e58984581c7` | 0 | 20/20 | 33/33 | `3f454af7e03dbd07d3cc1b021ca8af2e6c3706cb76267b96c455e00b19bdd76a` |

The primary and independent implementations agree on the exact Block09 POVM
lift, positivity and completeness, all 24 proper cubic frames, the 32-site
isolated writer geometry, the radial 26-Record code, the 90 Ready/Locked words,
the five pair-orbit sizes, instrument CP/TP including STOP, phase-gauge branch
covariance, and the complete-M2-QND boundary.  The independent runner adds a
tomographic uniqueness check and a correlated positive-semidefinite extension
not imported by the primary source.

The caches landed in commit
`ab26ddf55d76fbb40cb41c32ff76b4ebda244c26`.

