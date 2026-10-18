# Independent R5 four-layer momentum numerical check

Disposition: PASS for the residual-qualified finite coefficient-model diagnostics. Repeated lowest gaps are reproduced in distinct verified momentum sectors; they are not evidence by themselves of an all-size symmetry or flat dispersion. No R6 calculation or repository edits performed.

I reconstructed the full 2^16 all-plus row/column-parity basis, lifted the saved D4-invariant ground with u_orbit/sqrt(orbit_size) after an explicit float conversion, and obtained norm 1.0000000000000022 and full-matrix residual 4.34874e-13. Both physical translations leave it invariant to 5.35e-16. The float conversion is essential to avoid the earlier low-precision square-root issue; the current script contains it.

I independently built translations by expanding the 16 free bits into the 25 even-row/even-column physical X-basis bits, translating that physical array, and reading back the free bits. For every tested source q, q(translated_state)=exp(-iQ_a)q(state) to relative error at most 1.61e-14. Thus the state-action translation convention has the corresponding exp(+iQ_a) character. All six requested momenta pass, including both repeated-gap pairs. Source means at nonzero momentum are numerical zero. The geometry's edge and plaquette lists match the order in which Fourier coefficients are appended.

The source coefficients -18 on edges and -12 on plaquettes are those of the periodic four-layer original readout, in the X-basis representation. At Q0, using H=-4P-5E gives the connected source exactly -3(E-<E>)g, as asserted. The numbers in this output are unnormalized coefficient-model source weights: restoring the physical normalized original diagnostic requires its lambda^4/(128sqrt(V)) prefactor (hence lambda^8/(128^2 V) for weights), and energy gaps require Jlambda^4/128 at leading order. They are not already physical spectral weights or microscopic exact gaps.

For an independent low-mode check I used 55 fully reorthogonalized Krylov vectors, formed the FULL dense Rayleigh matrix B†(H-E0)B rather than assuming the three-term tridiagonal projection, and computed source overlaps directly with the reconstructed vectors. Results:

| momentum | gap | direct weight | full residual |
|---|---:|---:|---:|
| (1,0) | 77.03850322814164 | 103.97805212668911 | 4.67e-12 |
| (2,0) | 77.03850322813332 | 257.04438272347755 | 4.43e-12 |
| (1,1) | 79.20412824958642 | 593.4078629792835 | 3.30e-12 |
| (2,2) | 79.2041282495911 | 123.91896075428885 | 1.86e-12 |

Krylov Gram errors were below 1.04e-13. These reproduce the root's lowest peaks and weights. Equality of these gaps is a valid observed R5 coincidence across distinct characters, not momentum contamination; its exact algebraic explanation was not established here. D4 alone does not map (1,0) to (2,0), so do not attribute this equality to ordinary square point symmetry without further proof.

The root's weight formula norm(q)^2 |u_0|^2 is correct for its orthonormal Krylov basis and initial vector q/norm(q). Its direct full-H residual is the appropriate acceptance diagnostic. Nodes flagged accepted=false, including visibly large residuals, are quadrature/Ritz approximants and must not be advertised as converged eigenlines. A residual threshold alone is not an interval-certified eigenvector-weight error bound without spectral separation; the independently reproduced low weights are strong numerical controls, not rigorous certified individual weights in an unresolved degeneracy. In a degenerate eigenvalue, interpret the source cyclic-space result as the source-visible weight/cluster, not uniqueness of an eigenstate.

The saved ground comes from the all-plus invariant sector. Positivity and connected plaquette flips justify its ground role within that sector, but these numerics alone do not compare every other subsystem-charge sector. Nothing here establishes thermodynamic dispersion, propagation, a full 100-spin microscopic diagonalization, or observed-particle data.

Independent scratch: /tmp/check_momentum_review.py, /tmp/check_momentum_review.json, /tmp/check_momentum_ritz_review.json.

## SHA-256 reviewed inputs

- `/tmp/neutral_four_layer_momentum.py`: `23d8e2f5f80fbe64aee01bafdd8f0dc5c32cfaf7cc2ecd15d0ce2ad06f6d030a`
- `/tmp/neutral_four_layer_momentum.json`: `05a70de8c11bc8317e242659935277487b8575a2fd780ce4d493defac7220f19`
- `/tmp/neutral_four_layer_periodic.py`: `646e3f8fe16d44c39b7877f1a63980779df791764c37326e344525d5b5adec64`
- `/tmp/neutral_four_layer_periodic/R5.npz`: `aba6728a15640f6fe45bdd11f62a1fd8a02cfe0c35d708d98e36777cc0d52b2c`
