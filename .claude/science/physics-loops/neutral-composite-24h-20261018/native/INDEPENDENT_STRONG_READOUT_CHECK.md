# Independent strong-column neutral-readout check

Disposition: PASS for the even-length exact selection rule and the restricted leading-order uniform-composite implication. No formal audit, pack edit or bulk inference. Root retains authorship. Reviewed the independent minimal tunneling proof and native strong-tunnel source; separately constructed the plane representation below.

## Even L: multiplicity-free plane representation

Use aligned column signs z0,z1,z2,z3 with product+1, giving eight basis states. The two X planes flip column pairs(0,1),(2,3); the two Y planes flip(0,2),(1,3), with phase(-z_a z_b)^L. For even L all phases equal+1. The four flip masks span the rank-three even-flip group and have one product relation. Their action on the eight configurations is free and transitive, i.e. the regular representation of (Z2)^3. It contains each of eight one-dimensional characters exactly once. All longitudinal Z planes are+I in this selected parity band and add no degeneracy.

Every fully plane-neutral observable commutes with this representation. Its restriction to the band is therefore diagonal in the common character basis. The Hamiltonian is diagonal in that same basis. This proves the projected observable has no matrix element between distinct energy eigenspaces INSIDE this band, even when the Hamiltonian's tunneling coefficients split the characters. Accidental equal energies do not create inelastic transitions; character-diagonal matrix elements remain diagonal. It does not rule out different static expectation values between characters, elastic weight, response involving states outside the band, or charged observables.

For an isolated continuously/analytically continued eight-state spectral band, the physical symmetry operators preserve its projector. Character multiplicities are discrete and cannot change along the isolated continuation. Equivariant Kato/polar identification consequently carries the same multiplicity-free representation throughout. Thus the no-intraband-inelastic statement is exact on that connected isolated branch, not only at leading tunneling order. Isolation and continuation from the aligned band are premises, not a proof that the branch remains the lowest or isolated at isotropic coupling. No volume-uniform isolation is established.

## Odd L: why the inference changes

For odd L the Y-pair phases remain. The X planes commute mutually and Y planes commute mutually, but each X plane anticommutes with each Y plane. The restricted binary span has dimension3, symplectic rank2 and one central bit. Its representation on the eight-state band is therefore two central blocks, each protected dimension2 times multiplicity dimension2. The neutral commutant contains M2 on each multiplicity space and is NONCOMMUTATIVE. Fully neutral H and O need not commute there; neutral inelastic transitions are allowed. The even-L multiplicity-free conclusion cannot be transferred.

Independent explicit eight-state matrices at L3 and L4 verify all these phases and pairwise commutators. For even L, a generic weighted sum of the four commuting generators has eight distinct eigenvalues, checking one-dimensional joint characters. Both commutants happen to have linear dimension8, but only the even one is commutative; equal dimension alone is not sufficient for the no-inelastic conclusion. Output is /private/tmp/neutral-strong-plane-control.json.

## Uniform longitudinal next-neighbor composite

Let O=sum_(columns a,rungs j=0..L-3) Z_(a,j)Z_(a,j+2), with open ends. On an aligned configuration O0=4(L-2), for L>=2 (zero at L2). Add only a differentiation probe H(eta)=H-eta O. For a minimum-order edge-flip path with reversed-rung subset S, define w1(S) as nearest-neighbor domain walls and w2(S) as the number of j,j+2 pairs with exactly one endpoint in S. Then E(S)-E0=4Jz w1(S)+4eta w2(S). This depends on the rung subset but not which transverse edge is used or the initial aligned signs. The microscopic Y phase remains the same edge phase as in the tunneling proof.

Consequently differentiation of the complete minimum-order path sum gives the SAME real coefficient multiplying every one of the four edge tunneling operators. The leading nonconstant effective O is therefore proportional to the same four-edge operator T as the leading effective H, with coefficient -t'(0) in the convention H-eta O. Scalar diagonal corrections are allowed. Transitivity of the plane actions enforces their equality on aligned configurations; a shorter off-diagonal process is excluded by the minimum2L-spin Hamming-distance argument.

Differentiating an energy-dependent basis must be handled carefully: for a canonical isometry U(eta), -dH_eff/deta equals O_eff up to a connection commutator with H_eff. Here the isolated unperturbed subspace P is eta-independent, the canonical connection starts at positive transverse order (in fact at least quadratic), and lower effective H coefficients are scalar until the first tunneling order. Therefore this connection cannot change the leading nonconstant order-L readout. This justifies using the denominator derivative as an operator statement at that order, rather than merely a diagonal Hellmann–Feynman statement. It is not an all-orders identification of O_eff with a scalar function of H_eff.

Since leading H and leading nonconstant O share T, no leading-order inelastic readout follows even for odd L. Degenerate eigenspaces of T do not invalidate that statement because the leading O is scalar within each such eigenspace. Higher effective terms can rotate/split them and create subleading neutral transitions for odd L; they are not excluded. The L2 next-neighbor source is identically zero, so this part is trivial there. Different spatial profiles or different neutral composites need not share this proportionality.

The assumptions are the supplied finite open tube, positive rung-parity sector, Jz>0, and perturbatively small Jperp/Jz for the leading-source expansion. Even-L exact symmetry selection only needs continued band isolation once established. None of these results selects a cosmological state, produces a detector vertex, excludes all neutral spectral response, or proves a bulk scalar/phase statement.

## Evidence hashes

- `/private/tmp/neutral-strong-tunnel-check.md`: `7a0b0c23af2ccce2fa1c7e3afd721e3602eb309c121f433d5a8ca3882f4ac23f`
- `/private/tmp/neutral-strong-plane-control.json`: `7de7d29ee2726e1ba1b956af7ce71412ea9c24475a5ba86119460c53e09d8f0c`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_strong_tunnel.py`: `f7e6f7865c6ba6e942db3311b5dc6b4287e7ed67e3cc2986aee002c94bfbfd5d`

## Follow-up: square-invariant odd-L readout

Exact additional calculation CONFIRMS the stronger selection implication, with a dimension correction. Adding the physical square rotation (x,y)->(y,1-x) and uniform spin Z rotation by pi/2 gives a commutative commutant of dimension FOUR, not three, on the aligned eight-state band, for both odd and even L. It is not exhausted by I,T,T², whose span has dimension3.

In column order(0,0),(0,1),(1,0),(1,1), the square permutation sends indices0,1,2,3 to1,3,0,2. The per-rung Z-rotation phase is-1 on0000/1111 and+1 on the other even-parity configurations; the aligned L-rung phase is its Lth power. This explicitly constructs the exact signed8x8 S without importing an unverified local matrix. The original X planes flip(0,1),(2,3), Y planes flip(0,2),(1,3). Note that the physical tunneling X/Y edges are the opposite families: X edges(0,2),(1,3), Y edges(0,1),(2,3). Their distinction matters for odd L.

Exact SymPy linear constraints [A,G]=0 for all four planes and S give four basis matrices; all six pairwise basis commutators vanish exactly. The physical T lies in this commutant. Odd-L T has eigenvalues ±2sqrt(2) each twice and0 four times; I,T,T² has rank3. Even-L T has±4 once and0 six times. The fourth commutant direction can distinguish states not distinguished by T, so the dimension3 conjecture must not be used.

Both the native H and the uniform longitudinal next-neighbor composite commute with these planes AND the square/spin rotation: the latter simply permutes its four column ZZ sums, with no Z sign. Their band restrictions therefore belong to this COMMUTATIVE algebra. Hence they commute and there are no inelastic matrix elements within the isolated continued band, now also for odd L. The exact statement survives symmetry-preserving isolated continuation by unchanged representation multiplicities, just as above. It requires square symmetry of the observable and the transverse coupling pattern. Arbitrary plane-neutral nonscalar observables on odd L are still not covered; their larger commutant remains noncommutative.

This replaces the merely leading-order conclusion for this particular uniform square-invariant readout, not the general odd-L caveat. It is still finite-band, conditional on continuation/isolation, and does not exclude transitions out of the band or prove a bulk conclusion. The root's approximately1e-25 inelastic values are consistent with this exact algebra but were not used to infer it.

Control output: `/private/tmp/neutral-strong-square-control.json`, SHA256 `6c793ec0af597fcc58164d58fbf5bd0d1abc8d7b05d570a3e5a8f3fe648bc95b`.
