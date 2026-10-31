# Check x1: criteria (written 2026-10-27, before the script x1_hodge_flow.py exists)

Purpose: exact/numeric support for Lemma X-FLOW-NL (EXISTENCE.md): the linearised Wilson flow of the
gauge-invariant curvature is the heat flow of the cubical-lattice Hodge Laplacian on 2-forms, which acts
componentwise as the scalar lattice Laplacian, and its kernel couples every pair of parallel plaquettes.

Setting: periodic 4D lattice of side n = 4 (and n = 5 for parity), forward-difference d on 0-,1-,2-forms,
d^T its adjoint (standard inner products). Float64, numpy, one process, nice 10, threads = 1.

Pre-registered criteria (all must hold; tolerance 1e-10 absolute on matrix entries):
- A1: d∘d = 0 on 0-forms and on 1-forms (exact complex property).
- A2: the Hodge Laplacian on 2-forms, D2 = d1 d1^T + d2^T d2 (d1: 1-forms -> 2-forms, d2: 2-forms -> 3-forms),
      equals the block-diagonal matrix with the scalar Laplacian -sum_mu (shift_mu + shift_mu^T - 2) on each of the
      6 components.
- A3: the same for 1-forms (D1 = d0 d0^T + d1^T d1 equals componentwise scalar Laplacian).
- B1: for tau in {0.5, 2.0}, every entry of exp(-tau * Lap_scalar) on the side-5 lattice is > 0 (strict positivity of
      the heat kernel; the smallest entry is printed).
- B2: for tau in {0.5, 2.0}, the response of the flowed plaquette F_{12}(tau, 0) to a unit 1-form perturbation on a
      link b at the antipodal-ish position (distance >= 2 in every coordinate on side 5) is non-zero (|value| > 1e-12);
      value printed.
Pass = A1-A3 and B1-B2 all hold. Any failure is recorded as a failure; criteria are not changed after running.
