# VERDICT: CONFIRMED WITH CORRECTIONS

1. **Branch interpretation:** The unrestricted spectrum-preserving field redefinition is \(H\to VHV^\dagger\), equivalently \(D\to\gamma_0V\gamma_0DV^\dagger\). It equals literal \(VDV^\dagger\) when \([V,\gamma_0]=0\). Correction: literal conjugation always preserves the spatial \(D\)’s spectrum; noncommuting \(V\) instead breaks canonical \(\gamma_0\)-hermiticity and the fixed-time Hamiltonian/pole interpretation. `F3_report.md:54-59,83-86`; `scripts/f3_lit.out:29-30`.

2. **Linearity and symmetry:** Confirmed:
   \[
   \mathrm{Hess}(a)=\mathrm{Hess}_{F1}+2aL[G].
   \]
   Within the S19/range-\(\le\)NNN cubic-scalar class, only \(G_1\) and \(G_2\) have nonzero response, modulo commuting and symmetry-odd generators. This is not range-independent: S27 and S33 add further directions. `F3_report.md:96-127`; `scripts/f3_sym.out:10-43`.

3. **Numerics:** My independent analytic differentiation—without importing `f3_lib.py`—gives:
   - \(L[G_1]=-0.858582973037\,e^2\), \(a^*=0.0141163479601\)
   - \(L[G_2]=-1.502128367962\,e^2\), \(a^*=0.00806858871619\)

   These agree with the worker to \(4\times10^{-11}\). `referee_f3_independent.out:1-2`. The reported \(-1.2\times10^{-12}\) full-law residual uses the 156-node root \(a=0.01411544\), not the separately converged \(0.01411635\); this is a minor reporting distinction. `scripts/f3_tcheck_156.out:1-5`.

4. **Clover mechanism:** Confirmed structurally. Psym covariantization is not an algebra homomorphism, so \(([G,H])_A-[G_A,H_A]\), together with \([D_\tau,G_A]\), leaves transverse magnetic/electric field-strength vertices. These are Pauli/clover-type interactions that survive the loop and can move the critical mass. `F3_report.md:140-153`.

5. **Other changes:** Free energies, the unstrained law, UD/W1, Ward identity, gauge-parameter cancellation and locality remain unchanged. But the dressing also changes \(O(t^2)\) eigenprojectors, transverse photon vertices, form factors, momentum-dependent/multiplicative self-energy pieces, photon vacuum polarization and scattering amplitudes. Thus “nothing observed changes except the targeted channel” is unproved. The \(6.2\times10^{-9}\) tuning is correct only conditional on F2’s 1D Earth-medium sensitivity. `F3_report.md:196-208`; `C5_F2_referee_verdict.md:3-7`.

6. **Fixed reading:** **DRESS-SHIFTS is met on the intended H-conjugation branch.** The literal canonical \([V,\gamma_0]=0\), range-\(\le\)NNN sub-branch is DRESS-INVARIANT. That branch qualifier is mandatory because the fixed wording conflates the two transformations. `TESTS.md:9255-9259`; `F3_report.md:210-218`.

**Strongest correct statement:** For F1’s one-loop Psym law, the nearest-neighbour canonical-Hamiltonian dressing \(H_t\mapsto e^{iat^2G_1}H_te^{-iat^2G_1}\), \(G_1=-\sum_j\gamma_j\sin k_j\), preserves the free SF spectrum and all first-order strain data but changes the interacting transverse gauge vertices; the additive-mass Hessian is \(0.024240112e^2+2a(-0.858582973037e^2)\) and vanishes at \(a^*=0.01411634796\). The shift is caused by the Pauli/field-strength remainder left when Psym minimal coupling fails to commute with momentum-dependent conjugation. Therefore DRESS-SHIFTS is established for the intended H branch, while the literal commuting NNN branch remains invariant; the Earth-crossing tuning price is conditional and other quadratic interacting observables remain uncomputed.

Full referee record: [F3_referee_verdict.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_F3/F3_referee_verdict.md:1>). Independent checker: [referee_f3_independent.py](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_F3/referee_f3_independent.py:1>). Peak RSS was 294 MB.