# Native one-qubit dynamics route

Previous goal turn was progress: reviewed and published PR9699 (5cdd70258b12145ac4a894cb9aa78b1d024d36cd), attached to the chat. That exact fixed-Q result concerns the supplied quadratic candidate. Do not turn it into a universal one-qubit obstruction.

Current branch codex/neutral-native-dynamics-20261018 starts from that milestone. Primary checkout unchanged. Current root personally authors this route; no detached research jobs.

## Source and premise refresh

Read current MINIMAL_AXIOMS_2026-06-29.md: it expressly supplies no Hamiltonian, time metric, state selector or scalar branch. Read the September24 record-field and relaxed-compass-carving notes and their dependencies. The native compass Hamiltonian is an existing supplied alternative: H=K sum_(x,a) sigma_x^a sigma_(x+ea)^a, one actual qubit at every site. It is not derived from the axioms or identified with the corner model's microscopic completion. K=1 fixes model energy units and positive sign; the choice of the compass point among J,K,D and the preparation remain imports. No extra interaction is added to this candidate.

The previous corner class conserves central flux labels and lacks virtual-sector transitions; PR9694 remains a provisional checked source, not silently landed. C20 remote README supplies charge repulsion U rather than derives it. Do not import it to answer the no-added-interaction question.

## New constructive calculation

Define local energy e_x=(K/2)sum_a sigma_x^a(sigma_(x-ea)^a+sigma_(x+ea)^a). Pauli anticommutation cancels cross-axis terms in e_x², leaving (3K²/2)I+(K²/2)sum_a sigma_(x-ea)^a sigma_(x+ea)^a. The summed latter composite is a cubic scalar under the supplied soldered transformation law and time-reversal even; physical electromagnetic neutrality and scalar-particle identification are not yet derived. Independent identity check requested.

Personally implemented physical spin matrices directly in native/compass_scalar.py. Periodic size2 directions keep their parallel oriented bonds; no hidden six-qubit cell. Sizes2x2x2,3x2x2,4x2x2 have8,12,16qubits and24,36,48bonds. K=1, no record compression, no added fields. Ground preparation is supplied development input, full diagonalization for8 and lowest24 Ritz vectors for12/16; sparse degeneracy completeness is not certified. Connected response removes the entire computed ground eigenspace. Total-H inelastic response null control passes.

Results: 8site composite is exactly constant geometrically (all opposite neighbors coincide), with numerical inelastic weight2.5e-27. At12sites, weight10.20855, mean15.72071, width1.68103. At16sites, weight60.49001, mean8.32296, width3.84746. Thus the apparent narrow12site feature does not remain narrow on the next shape. Do not advertise a scalar pole. These anisotropic tori do not establish a3D thermodynamic limit. Lowest computed energies and residuals are in the JSON; no observed values are matched.

Next: validate the composite identity independently; compute resolved spectral response and spatial/dispersive information for this existing native model, retaining finite-geometry and prepared-state scope. Consider whether record/background features within this same Hamiltonian have a derived static interaction before any dynamical-scalar claim. A chosen background or inserted repulsion must not count as an assumption retired.

## Spectral and operator-growth checkpoint

Independent identity check is in INDEPENDENT_COMPOSITE_CHECK.md. It highlights that C=H_x/K+2N I on3x2x2 and antipodal pairs double at4x2x2. Those geometries are not generic3D scalar tests. Krylov spectra in compass_spectral.json resolve the3x2x2 uniform response into two main lines near14.23 and17.27;4x2x2 has a dominant line near6.65 plus appreciable higher weight. At4x2x2,qx=pi/2, C_q vanishes by geometric cancellation; this is not an absent physical propagator. Per-site weights now reported. The original moments were computed by full H action, not truncating the response to24 eigenstates.

A20site5x2x2 solve is actively running through tool session34254, PID12540 as observed at01:21:19UTC. Script compass_twenty.py uses a separate matrix-free Pauli implementation, checked against CSR on an8spin fixture. It avoids large sparse assembly on this16GB host. Poll the same session; do not restart merely on output silence. It will save compass_twenty.json and ground_5x2x2.npz when complete. This remains a thin-torus finite-state diagnostic.

Root also derived exact physical Pauli operator growth, implemented in compass_commutators.py. J=i[H,C] consists of3spin terms; its coefficients follow the existing bonds, not an added H term. On L4/L5 cubic tori the normalized Hilbert-Schmidt frequency moments are m2=32,m4=3072, so variance of omega²=2048. Thus C does not close as a single-frequency oscillator in that metric. This does not exclude a pole plus background, nor a different state. On L3 C=H globally and all dynamic moments vanish, another exact finite-size alias. Plane-parity commutation with H and C is checked. Independent localcount/binary-Pauli verification requested. These are maximally-mixed structure-factor moments; its retarded commutator response is zero, so do not call them finite-temperature force response.

## Infinite-lattice transport checkpoint

20site solve completed exit0; no root jobs running. ground energy−31.218556192893434, computed ground2, residual2.39e−13; C weight15.2826825619, mean13.8855011885, std3.72611039374. Still no pole identification. Root infinite-coordinate local Pauli runner now obtains exact offsite overlaps first at derivativeorder4, hence timeorder8; see TRANSPORT_DERIVATION.md. Independent check requested from environment_equations. Global L8 m2/m4 q-independence was insufficient to detect this transport. Jacobi coefficients derived from moments, not interpreted as matter coupling. Next: checked native transport milestone and state/large-feature coupling route.

20spin spectral followup now running in session76260, compass_twenty_spectral.py, 64steps with full reorthogonalization, q0 and2pi/5 and both computed ground vectors. Poll existing session; do not duplicate. Independent binary infinite-lattice check matches all transport coefficients, report being finalized. First-beta response is not full finite-beta leading short-time behavior.

20spin spectral followup completed exit0. At q=2pi/5, mean7.96454557016 and variance6.25643805457; dominant finite-volume quadrature line near6.636023143 with weight15.098667223 per ground-mixture component, plus higher lines. Low-imaginary-axis resolvents converge from32 to64steps; individual high-energy nodes are not all converged. Atq0, several lines remain; mean13.8855,width3.7261. No3D spectral pole inferred. Exact transport and canonical runner passed independent focused review; see REVIEW.md. Canonical milestone is exact local algebra; finite spectra remain exploratory development calculations.
