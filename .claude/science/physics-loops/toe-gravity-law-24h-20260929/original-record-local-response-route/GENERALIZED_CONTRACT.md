# Generalized local completion target, before its controls

The original CONTRACT.md and PRE_FREEZE.json remain unchanged. Its Omega-buffer preparation is sufficient but unnecessarily strong if the following Gauss-compatible completion works. The first local-prefix runner has already finished under its original narrower hypothesis; it is not claimed to check this new completion. Its exact coefficients/support bounds remain relevant.

Fix the common region D=B_R, consisting of its sites and links with both endpoints in D. Crossing links belong to the exterior. The original physical input is in global W1, with its hole in B_r, r<R. Impose only the local spectral support bound

    K_D=N_B(D)+|Q_D|<=K,
    Q_D=sum_(x in D)(q_x-1_A(x)).

No empty B annulus, frozen occupation mask, electric-field bound, zero crossing field, classical exterior, or core/exterior product state is assumed. The actual exterior may contain arbitrary occupation, charge and field coherence. The topology remains the entire first-original-mark instrument in integrated trace norm, retaining all original mark/time labels and bounded local postmark field observables, with arbitrary noninteracting ancilla. Use the same even torus for actual and reference, with L>=max(2R+6,4K), and the original H,G,j everywhere.

Candidate completion: for each boundary site set d_x=q_x-1_A-div_internal E; interior Gauss requires d_x=0 away from the boundary. Physical Gauss equates d to the joint commuting crossing-field divergences in the exterior. Hence the reduced regional density (including a noninteracting ancilla) is already block diagonal in d. Put Q=sum d. Add |Q| occupied exterior B sites of charge -sign(Q), keep every exterior A plus and all other exterior B vacant, choose crossing flows with divergence d at the boundary, and solve the remaining zero-sum integer divergence on a connected exterior tree. The exterior basis completion depends only on d, preserves the regional block, and gives a physical global reference with N_B^ref=N_B(D)+|Q_D|<=K. It must preserve within-block coherence and cannot be implemented by copying arbitrary nonsuperselected quantum field values. Boundary sectors are mathematical proof labels, not additional measured records.

If this completion is valid, the checked finite-global-k absorption bound applies to its entire direct sum over physical odd k<=K. Match purifications of the actual and completed states on the common regional algebra plus the spectator ancilla. Their exterior purifications can be aligned by an exterior isometry. Because all relevant early coefficients are operators only on D, the exact no-event/marked prefixes agree after that alignment even though the full exterior states differ. Both bounded generators and jumps retain their uniform norms; reference decay controls its late tail, and finite-prefix comparison controls the actual late mass.

Target quantitative bound: put b=delta*M+6kappa, m=floor((R-r-1)/2), n=m+1, T=n/(8b), q=exp(9/8)/8<1. With any uniform reference constants C_K,gamma_K valid on all physical odd global k<=K, aim to prove

    eta=4 sqrt(1+12kappa T) q^n
          +(C_K exp(-gamma_K T)+2q^n)^2
          +C_K^2 exp(-2gamma_K T)

for the all-time instrument difference, capped by its trivial norm2. This would be a genuine local-count/background-independent response estimate. It still need not control positive waiting-time moments or unbounded field-energy outputs. A source-state estimate for K_D, spatial hole localization, multiple holes and finite-spin transfer remain separate.

New bounded controls will construct integer exterior completions with nonzero boundary flux, verify every Gauss equation and the exact global count/parity, and check preservation of within-boundary-sector off-diagonal coherence. Sparse price below30 CPU seconds/150 MB, one thread. No older artifacts are edited. The theoretical proof, not finite sampling, must establish the CP completion and the purification/prefix comparison.
