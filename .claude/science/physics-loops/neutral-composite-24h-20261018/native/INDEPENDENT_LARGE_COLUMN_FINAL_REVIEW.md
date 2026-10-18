# Focused final review: exact internal dynamics and large-column tunneling

Disposition: no blocking scientific or provenance defect found within the stated finite, conditional scope. This is an independent consistency review, not a formal audit. I read the summary note, runner, detailed internal/strong-column notes, four probe sources/results, and three independent checks. I did not edit source files, rerun the native solve, or include unrelated growing-grid/MPS work.

## Exact versus conditional claims

The internal coordinate statement is exact in the supplied positive physical rung-parity space: dimension eight factors as two times four without adding physical qubits. The protected coordinate is protected under the on-rung Hamiltonian, not a spectator of the full chain. Both notes retain the native longitudinal vertices that act on it and on internal coordinates together. The signed YZZ, XIY, -ZYZ, -IXY conversion and h_internal=-IZ-XI-YY-ZX agree with the symbolic assertions and independent full two-rung contraction.

Vanishing vertex expectation is specifically in the unique internal ground state, and does not erase native interactions or justify freezing internal states at equal coupling. The projector and exact zero-energy transition identities yield the stated two-internal-excitation denominator 4sqrt(2) Jperp. The independent check correctly uses the ordered overlap squared, not its absolute square; its coefficient matches the previous collective XY interaction. The low-energy exchange remains a weak-longitudinal projection even though the coordinate change is exact at every ratio.

The all-finite-L tunneling coefficient has the complete minimum-flip path proof already independently derived. Open boundaries, Jz>0 and small Jperp/Jz are essential. The Ising/Majorana subproblem sums precisely the allowed minimal paths, with no claim that the entire four-column dynamics becomes that Ising chain. Its singular-value splitting proves the leading coefficient at each fixed L. The exact subset checks for L2..16 support, but do not replace, this proof. Y-edge phases and even/odd band spectra are consistent with the distinct physical edge versus plane-generator orientations.

The diagonal symmetry statement does not confuse equal aligned-basis diagonal entries with eigenvalue degeneracy: off-diagonal tunneling splits the band. Neither exponentially small leading amplitude as L grows nor convergence at the tested small ratios supplies a volume-uniform perturbation bound or an equal-coupling conclusion.

## Readout selection

The exact symmetry code computes a commutative dimension-four simultaneous plane/square commutant at both length parities, using the correct signed square action. At even L the plane representation alone is multiplicity-free; at odd L its dimension-eight commutant is noncommutative, and the square condition is necessary for the stated universal invariant-operator argument.

Both the uniform longitudinal distance-two composite and H preserve the isolated spectral band and commute with the physical symmetries. Their band restrictions therefore belong to the same commutative invariant algebra and commute. Representation multiplicities remain fixed along an isolated equivariant continuation from the aligned band. This gives zero matrix elements between distinct intraband energies for this readout, not merely a numerical small-weight observation. Elastic contributions, transitions out of the band, arbitrary plane-neutral odd-L observables, and other neutral excitation bands remain possible. The summary and detailed note preserve these qualifications.

The spectral source is the uniform longitudinal composite, not the complete three-dimensional local-energy-square composite with transverse contributions. The words “uniform longitudinal” are present where needed. The L2 distance-two readout is identically zero and is not informative by itself; the exact argument and longer-length checks are independent of that trivial case.

The saved finite spectral scan has 12 rows (L2..5, ratios .5,.35,.2), maximum recorded eigenpair residual 9.9625e-14, and decreasing scaled band errors toward the smaller ratio at every L. Those residuals are checks of the returned vectors, not a certificate that an iterative solver found every low eigenstate. Crucially the exact all-orders conditional selection rule is established by representation algebra rather than that spectral completeness assumption. The text's convergence description is appropriately finite and numerical.

## Runner provenance and excluded diagnostics

The runner invokes exactly the internal-factor, strong-tunnel, strong-symmetry and strong-spectrum probes. Its input manifest includes all four source files and the only local imported physics module, neutral_rung_model.py. Remaining imports are standard numerical/symbolic libraries. None of these probes consumes the frozen 32-site occupation state or its diagnostic results.

I read the completed outputs/native_large_column_dynamics/result.json without relaunching the runner. All five input hashes match current files, and all four embedded result objects exactly match their current probe JSON files. The result scope accurately identifies finite coordinate/symmetry/tunneling results and denies bulk/physical identification. The source-bound runner reproduces its advertised probes, rather than merely loading their outputs.

The selected 32-site internal occupations are explicitly separate frozen numerical context. They are not reproduced or hashed by this runner, and neither the summary nor detailed note uses them as a premise of the exact identities. Their quoted small residual and projector checks should remain tied to that frozen selected eigenstate; they do not certify its global ground status or particle abundances. No further replay was performed here.

Hashes are recorded after computation, so the runner is not a pre/post concurrent-mutation detector; no hash mismatch was observed. The independent check files and historical diagnostic provenance are supporting documents, not calculations claimed to be reproduced by this manifest.

## Conclusion within scope

The block derives native internal vertices, a finite large-feature tunneling process and an exact conditional obstruction for one uniform intraband readout. It does not supply a cosmological scalar, an observational test, dynamically selected parity/state, or bulk phase determination. The proposed domain-wall band is correctly marked as future research outside the proved low-band obstruction. No source changes are requested for the scoped claims.
