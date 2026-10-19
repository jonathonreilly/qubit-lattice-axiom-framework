<!-- Original PR9818 source SHA256 f8903bf967c96a8b2d4691688551b3bce7d2c3f48d4cf0adc2f2c0309fff8c33. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Character-independent collision: focused final check

Disposition: PASS within the stated fixed-height, weak-coupling, positive-Z, matched-low-energy preparation and invariant-readout scope. No formal audit or repository changes. The inherited local normal-form and collision estimates remain inputs; this review checks their character extension, not a new proof of microscopic scattering at fixed coupling.

## Exact algebra

The flat group is F2^(2R-1), acting freely on the aligned reference. Its minimum nonzero column-flip weight is R: a(R-b)+(R-a)b, with the redundant simultaneous complements removed. For even R and L=10, the - sign of each aligned whole-Y column cancels across a plane. Positive physical Z planes and the product relation between the X/Y generator families follow. All compatible characters occur exactly once in the flat subspace. These are distinct physical sectors, not gauge-identifications.

Direct evaluation of X_A Z_B on a flat Fourier vector gives the stated sign (-1)^(B dot T) in the pair matrix element, followed by the flat-group membership and G-perpendicular conditions. For invariant words, bounded total flip count less than R makes the only possible group element zero. In particular the two-column basis is orthonormal for R>4 and all such retained matrix elements are character-independent. Across characters orthogonality is exact because the column X preparations commute with the plane generators in the aligned representation. The physical equivariant dressing preserves that decomposition.

Replayed neutral_flat_character_control.py successfully: group sizes 128, 2048, 32768 at R=4,6,8; minimum weights 4,6,8; 360 sampled pair checks and 3072 direct finite-orbit checks. The direct checks cover flat diagonal matrix elements; the pair identity also follows analytically by replacing the flat group element with T xor T' xor A. The script correctly keeps the support-R and noninvariant-observable counterexamples.

## Uniform vacua and composed reductions

At any chosen fixed order, the flip count of a composition is bounded by the sum of its factor flip counts. Diagonal charge/shape projectors and denominators can depend on configurations, but introduce no new flips and are equivariant. Apply the exact orbit argument to every intermediate configuration along each finite path; once R exceeds the total bound plus four, no path can acquire a nontrivial character holonomy. This justifies the composition step without treating inverse denominators as arbitrary strictly local operators. Bounded row sums and charge-relative bounds inherited from the local construction are uniform in character.

The Q=0 rank is one in every compatible positive-Z sector. The inherited lower defect bound c J lambda^4 and order-J wall bound therefore isolate one state in each block. For remainder delta=C J R^2 lambda^M, ordinary isolated-projector perturbation gives eigenvalue error O(delta) and normalized-vector error O(delta/(J lambda^4))=O(R^2 lambda^(M-4)), uniformly in character. The global direct-sum norm is the supremum of block norms, with no exponential character count. This establishes unique sector minima in the indicated low-energy setting; it does not identify all of them as exact global grounds. The proof correctly states that distinction.

For R~lambda^-1 and physical time O(J^-1 lambda^(-10-3/4)), the remainder phase bound is lambda^(M-51/4); ground matching is lambda^(M-6). Both are small compared with the logarithmic collision signal for M>=20. Any common scalar phase is removed consistently. There is no need for an exact physical momentum fibre in an arbitrary character: translations can permute sectors. The retained defect-coordinate generator and its uniform-center packet are well-defined, while wrapping terms remain in the controlled error.

## Statistical scope

Invariant microscopic readouts commute with all sector projectors, so coherent cross-character terms vanish exactly. A uniform error bound then passes to arbitrary mixtures, and to coherent superpositions with the same matched packet in every occupied block. No probability measure over characters is required. Different packets correlated with characters, noninvariant probes, or arbitrary high-energy states are outside the result. The proof explicitly preserves these exclusions and does not assert thermalization, full state independence, cosmological selection, or universal force laws.

No required fix found.

## Reviewed SHA-256 identities

- `CHARACTER_INDEPENDENT_COLLISION_PROOF.md`: `f5ffe3204fd7fe63414d49f6a168dd5161008baf1671141598b84d706f42b656`
- `neutral_flat_character_control.py`: `1fe6522c9a1e9676c34d2c4137936bea6ef240748a5059f487e94f5446fa95d2`
- `POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md`: `c2d8e32ef8eb9e2e2866f3ed5ed73f324973e8be0d0fc00b03e5b28c702642e0`
- `NATIVE_PAIR_SCATTERING_PROOF.md`: `a9d371c8f0594d8bd25a4f4975f904c19b9a8c50f661daaaba7debdd6466fbb4`
