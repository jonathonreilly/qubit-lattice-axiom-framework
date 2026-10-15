# Supervisor's own thread on OBS-3 (written before the worker returns)

**Argument (a sketch; unchecked).** I assume the velocity residual of a chiral field depends only on the corner-diagonal entries (W y² W†)_cc. This holds when off-diagonal corner couplings need a Higgs or flavon at nonzero momentum, which is heavy for a nearest-neighbour Higgs.

1. **Cancellation needs flatness.** The residual cancels for every set of eigenvalues only if W is unbiased to the corner basis: |W_ci|² = 1/3.
2. **Flat 3×3 matrices are Fourier.** Every 3×3 complex Hadamard matrix is equivalent to the Fourier matrix F (Haagerup). So W_u = D₁ F D₂ P and W_d = D₁′ F D₂′ P′.
3. **CKM would have to be circulant.** V_CKM = W_u†W_d would then be equivalent, up to rephasing and permutation, to F†ΔF, a circulant unitary. The moduli of a circulant form a Latin square with only three distinct values. The observed CKM moduli are not of that form: the off-diagonal values |V_us| ≈ 0.225, |V_cb| ≈ 0.041 and |V_td| ≈ 0.0086 differ by orders of magnitude.
4. **So both sectors cannot be flat.**
   - Keep up flat, so the y_t² part stays universal. The down residual is then of order y_b²·O(|V_cb|)·K, about 1e-8–1e-9, which matches OBS-2.
   - Keep down flat instead. The up residual is then of order y_t²·O(|V_cb|)·K, which is larger.

**Prediction.** TEXTURE-FORCED, with a minimum of about 1e-9 to 1e-8 against 1e-22, unless:
- the loop tensor K can be made corner-universal by the choice of symbols, which I doubt; or
- off-diagonal corner couplings, through flavons, add a term that cancels.

**What I would check in the worker's report.**
- Is the diagonal-entry assumption valid, or do flavon loops contribute to corner-diagonal velocities at the same order?
- Does the minimisation really include the right-handed freedom?
- Is the bound applied to the vector combination c = (c_L + c_R)/2, and to the axial one?
