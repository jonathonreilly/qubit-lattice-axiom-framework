# Native composite transport: focused independent source review

Disposition: PASS for conditional exact local algebra in the supplied native compass Hamiltonian. No unresolved material finding. This does not certify a particle pole, canonical coupling, cosmological identification, retained grade or formal audit. Root remains author; reviewer made no repository edits.

Read the complete final note, aggregate runner, both local Pauli implementations and independent report. Replayed the exact aggregate runner with both scripts in a relocated temporary tree. Both implementations agree; aggregate JSON is byte-identical to submitted output. Final identities are below. Thin-torus diagnostics were not used as proof.

## Clarification resolved

The initial note used e_x without specifying its local energy convention. The author added e_x=(K/2) sum_a sigma_x^a(sigma_(x-e_a)^a+sigma_(x+e_a)^a), with sum e_x=H. I verified this final definition. Direct local Pauli multiplication confirms4 e_x^2=6I+2C_x at K=1. The composite is consequently a polynomial of the already supplied interaction algebra; constructing it does not add a term to H.

## Exact-support and algebra assessment

The root derivative enumerates all bonds touching a Pauli word's support, including both orientations at each site, and deduplicates each physical bond. Bonds disjoint from support commute and cannot contribute. Products retain exact unit phases and integer coefficients; cancellation removes only exact zeros. Iterating four derivatives is therefore complete for the claimed hierarchy.

Translation grouping uses the lexicographically first support coordinate as an anchor, which is translation covariant. It enumerates every matching translated word, hence every possible overlap displacement, rather than checking only selected nearby centers. The independent mask implementation uses a different multiplication representation. Its finite coordinate index box[-5,5]^3 contains all supports reachable from radius1 through four nearest-neighbor commutators; it introduces neither periodic wrapping nor boundary truncation.

The exact norms, term counts and offsite correlations agree. A further reviewer computation collapsed D^2 C0 into translation classes: adding32C leaves only four-spin words, orthogonal to C, with per-cell squared norm divided by<C,C> equal2048. Thus the note's uniform remainder statement is supported, not inferred merely from one local coefficient.

D=i[H,.] is skew-adjoint in the normalized HS inner product. Moving n derivatives between the factors gives(-1)^n F_n(r), and translation symmetry relates the local correlation orientations. Odd overlaps vanish also by Pauli support parity, independently of a physical spin time-reversal interpretation. Since every offsite even overlap through n=3 is zero and n=4 is nonzero, the t8 coefficients and their positive signs are correct. The t8 assertion is a local Taylor coefficient with a remainder, not a certified finite-time transport interval or extrapolation from a torus eigenvalue.

Fourier summation correctly gives six axial displacements as2 sum cos(q_a), and twelve face diagonals as4 sum cos(q_a)cos(q_b). Dividing by the zeroth norm3 yields the stated m8. Independently evaluated squares of the supplied monic orthogonal polynomials against m0,m2,m4,m6,m8: norms are1,32,2048,204800,m8-88113152. Their ratios give the stated Jacobi coefficients. K scaling is correct. These moment/recursion coefficients are not pole residues or matter couplings; the note explicitly avoids that identification.

## State and physical interpretation

Nonzero unequal-time tracial correlation is compatible with a stationary maximally mixed state and identically zero tracial retarded commutator. The note distinguishes those facts correctly. With the stated perturbation-sign convention, expanding the normalized Gibbs state to first order gives chi=-beta theta(t) S'_r(t)+O(beta^2). Trace cyclicity supplies the sign. The nearest-center linear-beta coefficient starts at negative beta*247808*K^8*t7/7!, but higher beta orders can start earlier in t; the note explicitly retains that ordering caveat and claims no finite-beta error bound.

This is a different supplied microscopic candidate from the quadratic corner Hamiltonian. The note does not smuggle in a new interaction under the name of the four-spin remainder, treat a formal response probe as a physical mediator, derive a state, or identify spin/space rotational invariance with electromagnetic neutrality. It derives exact local growth and spatial response coefficients only. Stable scalar excitations, long coherent features, a canonical matter coupling and the cosmological bridge remain open. No pole-plus-continuum or low-energy-state possibility is excluded by failure of one-coordinate closure.

## SHA-256 identities

```text
0c71df68e939e0b2b72b5b49bf6e68297eead45e83e26ea1e9d0311fabf557b2  docs/NATIVE_COMPOSITE_TRANSPORT_NOTE_2026-10-18.md
a6d9d965a655676041109bdf03f6377f109ce7c77f666c86a66fd135457de25c  scripts/native_composite_transport.py
f58ce08d4eb9b16e24a977c9c2c4a8d867521266f034c81a33b47d6c50f74b52  outputs/native_composite_transport/result.json
3f025982118f00fab1e96412d77eb9f2080fe1a086f4a5f3b5c9583d77f0c53e  .claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_local_transport.py
f1fb484e6cca7dc2a1e03c7d268e93fde13809aaf3b19424e1207074e905c9d5  .claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_local_transport.json
90cb33c8e1e12b3a91e44b368ae6fd6b3cf16730625d4de2f01a9d5491e87c8f  .claude/science/physics-loops/neutral-composite-24h-20261018/native/independent_transport.py
da9490e0ddc2a7663b82a0c85053dae3fce268d3acc9f7d6a95fd785c3907b77  .claude/science/physics-loops/neutral-composite-24h-20261018/native/independent_transport.json
fc402620cb6a5504588936be1b1672e4fcb5b7c7983f70bb7b9f1174d57174c5  .claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_TRANSPORT_CHECK.md
```
