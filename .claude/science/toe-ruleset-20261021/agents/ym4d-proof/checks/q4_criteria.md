# q4 criteria (lane G session 3; written 2026-10-28 before checks/q4_kernel_ids.py exists)

Purpose: exact identities used by SQ.md §13 (Lemmas CC-NA, RT-NA), on random data, by finite differences. Not a test of
any estimate; an identity check that catches sign, frame and convention errors.

Kernel (HIST Lemma KQ's form, LINEAR_PACKAGE §1.3): φ_M(V) := N⁻¹[Re tr(W_0(M)⁻¹M) - Re tr(V⁻¹M)], W_0(M) := the maximiser of
Re tr(W⁻¹M) over SU(N) (SU(2): the polar factor; SU(3): computed numerically to ≤ 1e-13). M := a weighted average of q
contour holonomies H_T = (product of p link matrices near 1, spread parameter y), V := W_0(M)e^{sX}.

Data: N ∈ {2, 3}; 20 random instances each; contour count q = 6, length p = 5; link matrices exp(η·random su(N)),
η ∈ {0.02, 0.1}; s ∈ {0, 0.003, 0.03}. Central differences with h = 1e-5 (error O(h²) ≈ 1e-10 relative).

- **K1 (bi-invariance).** |φ_{aMb}(aVb) - φ_M(V)| ≤ 1e-12 for Haar-random a, b ∈ SU(N).
- **K2 (M-gradient formula).** For random complex δ: |d/dt φ_{M+tδ}(V) - N⁻¹Re tr((W_0⁻¹ - V⁻¹)δ)| ≤ 1e-7·(1 + |value|).
- **K3 (zero at the polar point).** At s = 0 the M-gradient (K2's formula and the finite difference) is ≤ 1e-8 in every
  tested direction.
- **K4 (contour insertion, RT-NA's per-contour formula).** Insert e^{tμ} after the prefix P_T (first j factors) of contour T
  at a link shared by a subset of contours: |d/dt φ - Σ_{T∋b}w_T N⁻¹Re tr((W_0⁻¹ - V⁻¹)·Ad_{P_T}(μ)·H_T)| ≤ 1e-7·(1 + |value|).
- **K5 (opposite gradients, CC-NA).** d/dt φ_{e^{tμ}M}(e^{tμ}V) and d/dt φ_{Me^{-tμ}}(Ve^{-tμ}) are ≤ 1e-8; equivalently
  the left (right) V-gradient is minus the left (right) M-gradient.
- **K6 (proportional to the residual).** The max over a 20-direction sample of |M-gradient|/|μ| (left-multiplicative
  directions δ = μM̄) divided by s is constant to within 5% for s ∈ {1e-4, 1e-3, 1e-2} at fixed (M, X).

PASS = all of K1-K6 on every instance. Resources: < 1 min, < 200 MB; under the numeric lock; nice 10, threads 1.
