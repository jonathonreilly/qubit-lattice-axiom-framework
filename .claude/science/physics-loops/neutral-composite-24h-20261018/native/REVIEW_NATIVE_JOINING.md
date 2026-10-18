# Final focused native joining review

Disposition: PASS for the packaged finite restored-bond test. No material fix found. This is a focused scientific/source review, not a formal audit or landing authorization. No repository edits performed.

Reused the independent derivation in /private/tmp/neutral-native-join-check.md and its exact subset controls; confirmed the canonical note, runner and packaged proof retain its boundaries. The 4x6x10 object has 240 physical spins. Restoring the 24 existing vertical ZZ bonds at g=Jz produces the stated native geometry; g is only a comparison parameter, not an adopted weak coupling.

The 8g minimum is correctly restricted to pairs of plaquette-positive gauge patterns. The canonical note explicitly distinguishes the 2g cost for an unrestricted single-column mismatch. All asymptotics keep g positive and fixed; neither the coefficient's 1/g factor nor band continuation is extrapolated through g=0. The note correctly avoids tracking particular odd-half levels through that singular limit.

Even joined height removes the projective plane phase: the aligned positive-plaquette pattern band is the 512-dimensional regular row/column quotient representation, with one state per allowed character. The exact symmetry-preserving isolated-band continuation retains these integer ranks. Full-plane-neutral observables are diagonal inside this band, so the old-half, full-array and interface-crossing ZZ diagnostics cannot have inelastic intraband matrix elements. This does not forbid transitions to other bands or claim every response vanishes. It also does not prove an infinite-lattice embedding or an exclusion of all connected features.

The inhomogeneous pair-column denominator is consistent with the independent minimal-word/Ising-chain derivation. Eight Jz bonds and one g bond give Jperp^10/[(2Jz)^8(2g)], reducing to Jz lambda^10/512 at the native endpoint. This is pair-column tunneling outside the plaquette-positive subspace, not direct ground-band motion; the canonical text explicitly preserves that distinction.

Runner inspection confirms exact Fraction recursion over all proper flipped subsets, with cost 4 times the sum of crossed longitudinal couplings, and no final zero denominator. Its three g values give 3/512,1/512,1/1024 in Jz=1 units, as independently checked previously. Enumerated gauge-fixed patterns are unique, number 512, and have minimum nonzero mismatch four. The final Walsh orthogonality loop checks the abstract Z2^9 character table; the identification of physical plane actions with that regular representation is supplied by the proof, not independently reconstructed by this loop. This division of evidence is acceptable and does not constitute a 240-spin eigensolver calculation.

The runner declares the root proof as a source input. The canonical note and proof state fixed finite size, sufficiently small transverse coupling, supplied Hamiltonian and geometry, and absence of observational calibration. The result is a narrow failure of this restored-boundary neutral-line route, not a universal force or scalar no-go. Existing independent checks were reused; no expensive or redundant replay was needed. Root remains responsible for aggregate source-bound replay and publication mechanics.

## Source hashes

- `docs/NATIVE_JOINED_NEUTRAL_BAND_NOTE_2026-10-18.md`: `56c9810dfb1281a6cdf2c5b3539edc92ac1423297f54832527172ace8b0f1583`
- `scripts/native_joining.py`: `708b896ca4eaef8c75a519c05119913ef68c28ccc9eccbcdd11cb8c98823998d`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_JOINING_PROOF.md`: `7419d440d8da923c151f35baa0fe49a5386616cb649f5a007965c27d79f3e7ea`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_NATIVE_JOINING.md`: `9121bb82e0ff30baada062c63ee2b545ba41febc398b28a474c9f30c5a488447`
- `outputs/native_joining/result.json`: `49c0c896c35aa333e23421498d2857dfc614c43066a034558b9acc114e7c078f`
