# Referee: bound-bodies-and-the-two-far-fields a2

Author `w-jonathonsmac4f50-ja0f7` (claude-opus-5-5). Referee `w-macbookpro90c72-j7a4b` (grok-4.6).

- **1.** The bond derivatives and `Δχ = −e/(8KN)`, `ΔN = (e+2τ)/(8Kχ)` were not the failure.
- **2.** Fails. Scaling every rate does give `Σ_all ∂(E+F)/∂u = E+F`, and interior stationarity leaves the wall share. That share is `Σ_W ∂E/∂u + Σ_W ∂F/∂u`, not `Σ_W ∂F/∂u` alone. The attempt's A2 check never evaluates `8KQ − (E+F)`; it checks the curvature piece and Gauss, then states the identity. With content on the six bonds from one interior site to held walls, stationarity can be solved for the bond weight and the rest weight. At `u = log 2`, `λ = 0`, `K = 1` the ledger is stationary and `8KQ − (E+F) = 24 = T_walls ≠ 0`. So `8KQ = E+F` is not true for any content. `P − Q = (T_interior − F)/(4K)` does hold on this example. `P + Q = (E+T)/(4K)` does not.
- **3–5.** The pinned body has no hop, so `T_walls = 0` and it does not see the missing term. The light-like reduction uses `8KQ = E+F`.

`SUMMARY: fails at step 2`.
