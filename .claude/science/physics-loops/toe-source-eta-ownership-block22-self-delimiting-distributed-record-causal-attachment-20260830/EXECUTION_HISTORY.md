# Block 22 execution history

There was one initial passing execution of each pinned runner, followed by one
strengthened primary execution after the completion audit found an explicit
coverage omission.  No physics failure or source attempt is hidden.

| role | pinned source SHA-256 | exit | checks | hostile mutations | cache SHA-256 |
|---|---|---:|---:|---:|---|
| primary, initial coverage | `80c646f09c8066c60a9ebcb3cb2413d3476c13091064512e4cee3d2f0e7ecc75` | 0 | 17/17 | 27/27 | `c4ad88865d6b503ba819e861b2210f2a7876cd6a6983d1ed425bafcb1697e596` |
| primary, authoritative strengthened coverage | `5a987385123b560c4851ed5cf0c1d6b2b2bd66c05320a78163c0fcf763bbf2cf` | 0 | 19/19 | 30/30 | `ebef20cc42958774f8bd67e9f592ccc203b8ef7576185b2ece08aa9cd67a71a4` |
| independent | `2b4116ad201b71d609e71b97b8884a4cffe277c7e5d9562e90b22e58984581c7` | 0 | 20/20 | 33/33 | `3f454af7e03dbd07d3cc1b021ca8af2e6c3706cb76267b96c455e00b19bdd76a` |

The authoritative primary and independent implementations agree on the exact Block09 POVM
lift, positivity and completeness, all 24 proper cubic frames, the 32-site
isolated writer geometry, the radial 26-Record code, the 90 Ready/Locked words,
the five pair-orbit sizes, instrument CP/TP including STOP, phase-gauge branch
covariance, and the complete-M2-QND boundary.  The strengthened primary adds
the explicit `14 x 64` square-root reconstruction, correlated/reference
Lueders branch control, and commuting classical QND escape required by the
frozen contract.  The independent runner adds a
tomographic uniqueness check and a correlated positive-semidefinite extension
not imported by the primary source.

The initial pair of caches landed in `ab26ddf55d76fbb40cb41c32ff76b4ebda244c26`.
The authoritative strengthened primary cache landed in
`7244b9da2e7d1baba91141b87ffa3d216a65fe6b`.
