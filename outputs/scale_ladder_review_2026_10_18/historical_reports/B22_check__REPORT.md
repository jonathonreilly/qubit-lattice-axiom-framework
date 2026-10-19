# B22 check: local lapse for a QCA step

Provenance: a fresh-context checker of the same model family. All code is its own: exact sympy momentum-space bracket elements, dense real-space Schur log and expm, and a separately written circuit. Saved by the supervisor from the hand-back.

**Results:** 22 PASS, 3 FAIL. All three FAILs are the checker's own predictions (a preset packet tolerance, massive-walk convergence of A, a residual-growth guess).

| Runner | Result |
|---|---|
| `chk1_moyal.py` | 8/0 |
| `chk2_generator_1d.py` | 6/1 |
| `chk3_cut_1d.py` | 4/1 |
| `chk3b_tilt_scan.py` | informational |
| `chk4_3d_exact.py` | 4/1 |

## Verdicts

1. **The bracket formula is confirmed, and sharpened.**
   - The exact matrix element is expanded around the midpoint momentum.
   - Order 1 is −i w_j ½{h, ∂_j h} = ½∂_j(h²), for any matrix structure. h² = ω²·1 because det W = 1.
   - In 1D, order 2 is identically zero.
   - In more than one dimension, order 2 is −¼∂_iN∂_jM [∂_ih, ∂_jh]: the spin (Kosmann) term. For h = σ·k the bracket is exact at all orders, including the Kosmann term.
   - **Correction 1.** All of B22's lapse pairs have ∇N ∥ ∇M, so the spin term vanished in its tests. The check tests it on the 3D steps:
     - the residual drops from 3–8% to 1e−4;
     - the term tends to the node-triad Kosmann form;
     - for the uniaxial toy cof(e) = diag(2,2,1), which confirms B17_check's spin-part rejection on a step.
   - The energy-offset term is confirmed. The factor 6.2 is π/ω̃.
   - **Correction 2.** For a node at k* ≠ 0, G must be built from the momentum measured from the node. With lattice momentum an extra +i(g k*)·w density term appears: deviation 34, against 2e−4 with relative momentum.
2. **The numbers are confirmed.**
   - cos ω = cos θ cos k, so ½(ω²)″ = θ cot θ.
   - 1D bracket residuals are 4e−14 to 3e−4, also for non-uniform w.
   - Packets give 0.93–1.08.
   - The 3D uniaxial best-fit κ is (0.993, 3.983); off-axis gradients give 2.46 and 1.97.
   - **Correction 3.** In the gapless case W_N has non-summable 1/r tails for non-integer N, so it is not quasi-local.
3. **Defect lemma: true, and elementary.**
   - **Correction 4.** T must be defined as the sum, over consecutive even runs, of the change in λ/2. "Each odd wire flips chirality" holds only at θ = 0.
   - **θ = 0:** the failure is intrinsic for any bounded-range chirality-preserving identification. A chirality-imbalance count grows as O(A).
   - **Massive walk:** a 5–15% deviation that does not converge; not gross failure.
   - **Scope:** the 1D brickwork walk, wire-label composition, and staircase or real lapses.
   - AFF clock QCAs and gate-modulation lapses (Di Molfetta–Brachet–Debbasch 2013) are untested alternatives.
4. **"Only via B" is not established.** It should read "of the two definitions examined". Met via B is close to tautological. The content is the conditions B adds:
   - the node at quasi-energy 0;
   - node-relative momentum;
   - the branch cut in a gap;
   - spin and interband parts (spin settled for 2-band Weyl nodes).
