# Final bounded prose and mathematics review

Read DERIVATION.md and RESULTS.md completely, plus plot_transfer.py including its caption. Reused the exact-source independent raw-readout and six-return matrix-exponential evidence in INDEPENDENT_REVIEW.md, independent_results.json and independent_sequential_results.json. No code/data or author prose was changed. No necessary mathematical or empirical-scope correction found for these versions. This is not a PR-opening or audit verdict.

The population generator has correct downward-rate placement, conservation and positivity hypotheses. Direct integration gives the stated F(t), its continuous degenerate limit, the pure-|2> calibration vector and equal-population target Pexc. The formula includes zero rates without singular physical-rate division. Jump operators sqrt(kij)|j><i| match the source-to-destination rate notation, under the stated diagonal free Hamiltonian. The projector commutator/trace argument correctly requires a final unitary confined to the 1–2 subspace; pulse losses and inaccurate initial populations are explicitly outside that identity. Affine IQ inversion is correctly conditional on invertible reference geometry and pure-state reference interpretation, with no clipping.

The full chain is expressly imported canonical dynamics. Equal coherent superposition and incoherent mixture yield the same observed sum; both files explicitly reject a coherence, native-TOE, unique-model or assumption-validation claim. Source condition changes and the 10h42m02s gap remain explicit. The reference membership, 61×197 calibration grid and 31×380 target grid agree with the independently checked source. The 36,051 calibration population coordinates are constrained/correlated; the prose does not present them as independent statistical observations or a likelihood.

Checked every headline/table numerical quantity against saved independently reconstructed evidence: six RMS/mean rows, rates, three-rate calibration RMS .03151155, gradient-termination limitations, absence of active full-model bounds, first/last prediction and measured mean, maximum absolute residual 7.1561 percentage points, and 33.1447%/4.5756% simplex departures. The local condition number ~4.97 matches saved Jacobian singular-value ratios; this review does not independently recompute the numerical Jacobian. Reconstructed the fixed no-decay control directly from independent target populations: RMS .0516417984504014, supporting 5.1642 percentage points. No-decay and sequential-only controls are correctly labeled post hoc. The original target prediction is distinguished from the later control; there is no claim that the latter choice was blinded to the original outcome or establishes direct-channel necessity.

The figure source uses calibration-cost selection, all gate traces and an unweighted gate mean, with residuals expressed in percentage points. Caption says traces are not confidence bands and discloses omitted nearly coincident sequential curves. Its wording remains conditional and does not attribute coherence evidence to Pexc. Scope inspection only: no independent image-layout assessment is claimed here.

SHA256 identities:

- DERIVATION.md: `baaae10a870e38c13a5f4dca7e22b491c3a2c2b1dfcff28ae95f91588cd4f438`
- RESULTS.md: `2aa38daf080cd5e479f5d426405fb59f5b0b1257fb56987014febf8a823d68ad`
- plot_transfer.py: `3ee19579f009c895855894a4b60278f935a387a6b343f3befd283d6ab437492d`
- preparation_transfer.png: `ffb17d3fa95709679a528258faa34da13ca5055b07a7dbe9e29e54a9c85f512f`
- INDEPENDENT_REVIEW.md: `fbc6ae5ecde5214e7c75b2719f08f35042787cac27cb3f16a6606751726e770e`
- evaluation.json: `d4e04739275b20e94fd5c246e835bb1a59b1eb7420a53d9d2357c02e16b7e45d`
- NO_DECAY_CONTROL.json: `449895e8828bb3dc95df679bf146d6b91d2250b4edd5ebbcb9f4ff0e36e8951d`

Hashes and code paths support the recorded access boundary; they do not independently establish absence of every possible historical human access. Close multistart results and low residuals remain descriptive outcomes under the stated preparation, readout and stationarity assumptions.
