# Twelve supplied real PMNS representatives: finite rank test

**Type:** bounded_theorem
**Status:** supplied finite algebra/evidence; physical bridge open
**Primary runner:** `scripts/frontier_dm_pmns_asymptotic_source_no_go_2026_04_20.py`

Supply squared sines (0.307,0.0218,0.545), the six row permutations and the two real CP choices 0,pi. For each resulting real orthogonal U, put J=U diag(lambda) U^T. The specified real three-generator family obeys

    J22+J33=0,
    J13-J12-2*J22=0,
    2*J11-2*J23+J12+J13=0.

These give a 3x3 homogeneous linear system A(U)*lambda=0. If A(U) is nonsingular, only the zero eigenvalue vector is possible, including vectors with repeated entries. The runner checks numerical full rank at the twelve specified U and prints singular-value margins. Its floating-point SVD is numerical evidence, not an exact algebraic or interval certificate.

## Missing asymptotic bridge

A normalized affine sequence may converge to a real symmetric pure-source matrix, but that does not by itself imply its complex eigenbasis converges to one of the twelve real representatives. At eigenvalue degeneracy complex rotations within the limiting subspace remain possible. Passing mixing observables to a limit needs controlled spectral projectors/gaps or an explicit convergence premise. A fixed-U rank result cannot supply that premise.

Consequently this note does not assert that all basins lie in a compact region or that every infinity tail is excluded. Even a representative-restricted asymptotic implication is conditional on convergence of the relevant eigenbasis/observables to that representative. The finite chamber-sphere optimizer reports the smallest value it found; a positive sampled minimum is not a rigorous global lower bound. No target selection, complete basin enumeration, or physical lattice lift follows.

The earlier N1–N8 PASS declaration is withdrawn: permutations and the two phase values are one enumerated mechanism, not five independently closed route families. This is partial narrowing to a finite rank diagnostic and a conditional linear-algebra implication, not a universal no-go packet.

## Provenance

Prior text is recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under this path. Related definitions/context (no blanket status endorsement):
