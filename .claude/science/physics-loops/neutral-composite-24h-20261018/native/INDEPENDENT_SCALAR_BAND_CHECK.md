# Complete scalar two-wall sector: focused check

The proposed all-even-length symmetry-sector count and closure argument check, with a necessary distinction between physical and compressed XOR labels. This is exact closure of the symmetry-restricted UNPERTURBED E8 space and its equivariant canonical effective operator, not invariance of the bare E8 subspace under the full Hamiltonian. Full-H coupling to other energy bands remains present.

## Complete band and exact symmetries

In the positive-rung-parity periodic tube, distinct rung configurations differ at two or four physical sites. A longitudinal interface costs twice that Hamming distance in Jz units. Periodicity requires at least two interfaces. Total excitation energy8 therefore consists exactly of two distance-two interfaces: a contiguous interval of one color b in a background a, with physical Hamming distance(a,b)=2. There are no other configurations at this unperturbed energy. Color complements and interval orientation give duplicate descriptions and must be identified.

The physical X planes become compressed flips6 and1, with no phase. The physical Y0Y2 plane becomes compressed flip5 with local phase -(-1)^popcount(x&5); multiplication over all rungs gives precisely the script's global phase. The flip masks6,1,5 have binary rank three and act transitively on eight background colors. For even L their global plane operators commute; local anticommutation phases cancel over the length. The square/spin operation and transverse x reflection are also exact native symmetries, preserving both the transverse h and each longitudinal dot product of corresponding Z columns.

I independently constructed physical16-dimensional rung matrices. The square/spin map commutes with h on the even-parity space exactly, and the x reflection commutes with h exactly. On physical configurations0000 and0110, Rx*S fixes each configuration with phases -1 and+1 respectively. These controls use physical Pauli matrices and permutations rather than importing the root orbit code.

## Odd diagonal elimination and existence

The representative diagonal color difference called XOR6 in the proof must mean the FOUR-PHYSICAL-BIT mask0110. It is compressed label3, not compressed XOR6 (which is a native edge). The code's reported color_xors are physical bits[a]^bits[b] and are consistent with this distinction.

For background0000 and diagonal0110 on an interval of length ell, Rx*S fixes every color and spatial configuration. Its total phase is (-1)^(L-ell)=(-1)^ell for even L. Thus an invariant vector supported on an odd-ell diagonal orbit is impossible. Group conjugation transfers that obstruction to all equivalent backgrounds and either diagonal difference.

For even ell, both color multiplicities L-ell and ell are even. Every Py and square sign is a product of a fixed local sign raised to these even multiplicities and hence equals+1. Therefore equal amplitudes on the whole orbit are consistent. Translation and reflection introduce no additional q0 sign. There is exactly one allowed diagonal orbit at each even minimum length.

There is one edge-color orbit at each minimum length. The four physical edges are related by the square, and backgrounds by plane flips. Its invariant vector exists, for example from the scalar vacuum source and successive length-increasing native H1 moves at q0. Extending either end by one rung has the same nonzero edge matrix element; the highest-length component does not cancel at q0. This establishes existence rather than relying on an unsigned orbit count alone. Since signed transitive orbits have at most one invariant vector, existence also gives uniqueness. For nonzero q one may instead use the signed translation-orbit construction; the Krylov construction must not be used at q=pi, where its hopping vanishes.

## Counts and folded terminal orbit

Color exchange identifies ell and L-ell. At q0, minimum lengths1,...,L/2 supply L/2 bright states. Even minimum lengths supply floor(L/4) dark states. Thus

dim P_scalar,q0=L/2+floor(L/4)

for even L>=4. This is an all-length finite-group argument, consistent with the supplied exact signed-orbit enumeration L4..24.

For q=2pi m/L, a nonterminal interval has no nontrivial translation stabilizer modulo the on-site color operations. The terminal ell=L/2 interval is carried to its color complement by translationL/2. The color-exchange operation has plus phase for the allowed edge orbit and for the even-ell diagonal orbit. Hence the terminal orbit exists only when exp(iqL/2)=(-1)^m=+1. It follows that

bright dimension=L/2-(m mod2),
dark dimension=floor(L/4)-1_{L divisible by4 and m odd}.

The odd-ell diagonal obstruction is on-site and does not depend on q. At q=pi the orbit dimensions remain valid even though a source-generated H1 Krylov chain can collapse. For q!=0 these statements refer to a fixed complex momentum representation; longitudinal reflection would exchange q and -q, but the transverse Rx used here does not.

## Meaning of closure

The span of all these allowed orbits exhausts the complete E8 band in the specified plane/square/transverse-reflection/momentum sector. Every exact effective operator constructed equivariantly within that band, at any order for which the finite-band continuation is defined, must remain in this space. Consequently additional same-symmetry E8 color channels cannot be silently omitted once this whole bright-plus-even-domain basis is retained. This is stronger than checking K4 leakage on a few vectors.

It does not show that the bright chain alone closes, that the dark matrix remains nearest-neighbor beyond K4, or that its proposed hopping/diagonal coefficients are correct. All matrix elements within the counted space still need derivation. Other symmetry sectors are not eliminated physically; the restriction comes from the chosen invariant state and scalar source. A general source or symmetry-breaking state can access them.

Finally, the bare E8 projector does not commute with full H. Canonical elimination still requires finite-band isolation and can fail to be uniform as length grows. The exact count removes a degeneracy/completeness ambiguity within the chosen unperturbed sector; it does not certify an infinite native resonance, an isolated full-H band at fixed coupling, an observational scalar or a cosmological bridge.
