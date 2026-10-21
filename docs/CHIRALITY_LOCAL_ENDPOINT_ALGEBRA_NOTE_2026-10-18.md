# Local Spin(10) pairing endpoint algebra

Claim type: bounded_theorem.
Primary runner: [chirality_endpoint_algebra.py](../scripts/chirality_endpoint_algebra.py).

In the explicitly supplied 32-complex-mode vertex, the QMC-normalized pairing identity has coefficients kappa=(3/2,-1/2,0,0) in the singlet-8v, triplet-8v, singlet-56v and triplet-56v families. The construction and normalization are given in `outputs/chirality_exact_review_2026_10_18/proofs/majorana_square_conventions.md`. Q_QMC=Q_SIGN1/16; their coefficient conventions must not be interchanged.

The primary constructs the real Cl(9) matrices, checks all 35,960 ordered complex quartic coefficients, then compares the entire sparse 64-Majorana operator, including scalar and quadratic grades. It checks the 64 retained Hermitian channel parities under the explicit antiunitary whose square is -I. Arithmetic entries are exact dyadics; equality is exact, with no sampled fit or tolerance-based coefficient acceptance. The 180-second cap is a review execution bound, not a reported completed run.

This is a local endpoint identity. Sign-free lattice evolution additionally requires compatible kinetic factors, particle-hole frame, boundary conditions and auxiliary-field factorization. A wider coupling cone, nonzero-lambda1 density remainder, determinant positivity for an unspecified lattice model, interacting gap and symmetric mass generation are not conclusions. The complete square expansion and exact construction remain live; historical sampled fits and phase claims remain recoverable with their correction boundary in `outputs/chirality_exact_review_2026_10_18/README.md`.
