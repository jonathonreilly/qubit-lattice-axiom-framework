# Supervisor's own thread on CLS-1 (written before the worker returns)

**(i) Labels under BCC.** A translation by v survives the three hw2 condensates only if K·v ∈ 2πZ for every K ∈ hw2. That needs v_x+v_y, v_y+v_z and v_x+v_z all even, so all components of v have the same parity: the BCC lattice.

Corners q and q′ then share a label exactly when q − q′ ∈ {0} ∪ hw2. That gives two classes:
- {hw0, hw2}, all right-handed per X2;
- {hw1, hw3}, all left-handed.

Each sector has a single chirality, so no translation-invariant bilinear (Dirac) mass can pair any two corners, and no Majorana mass exists either, since 16⊗16 has no singlet. The bilinear-level light protection of X2-L1 therefore **survives** BCC breaking, sector by sector: 4L in one sector, 4R in the other, per component.

**(ii) The light modes and the mirror interaction.** What protects the 3 light L modes is no longer a label. It is that the SMG interaction gaps an anomaly-free subset, and only couplings strong enough to pass the SMG threshold can gap more. With class-S mixing θ ≈ ε/M_mirror, the light modes couple to the quartic at about θ⁴W. For θ well below 1 that is below threshold, so they stay gapless.

The danger is θ of order 1: if ε ≈ g′f ≈ 0.03–0.3/a and M_mirror ≈ 1/a, then θ ≈ 0.03–0.3.
- At θ ≈ 0.3, θ⁴ ≈ 1e-2. The light coupling is W/100, likely below threshold if W is near critical.
- So I expect the light modes to stay gapless across the range, with no index argument guaranteeing it. The full 4L+4R set is anomaly-free, so strong enough coupling could in principle gap everything.

**(iii) Observables.** The admixture of hw3, a cubic-invariant point, changes each light generation's velocity tensor. But it does so the same way for all three, because cubic rotations permute both the hw1 corners and the hw2 condensates. Lemma S therefore suggests the zero survives in the S3-symmetric condensate configuration. Gauge couplings stay unitary, since both are 16s.

**Prediction.** CLS-SAFE or CLS-PRICE (a mild bound on f, or on g′). Probably not KILL.

**What I would check in the worker's report.**
- Is the hw3 mirror's "mass" modelled correctly? SMG gives no bilinear partner, so the auxiliary-partner proxy is only an infrared caricature.
- Does the index argument per BCC sector really hold with the filter? The filter vanishes only at hw1, not at hw3.
