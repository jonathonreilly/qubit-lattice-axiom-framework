# VERDICT: CONFIRMED WITH CORRECTIONS

### R2 — confirmed conditionally

- Every displayed X2 term is \(U(1)_X\)-invariant. The filtered quartic is safe because \(B^a\) transforms as the Spin(10) vector \(10_v=5_{-2}\oplus\bar5_{+2}\), and \(B^aB^a\) pairs opposite charges. The filter commutes with \(X\) because it is Spin(10)-blind and its \(G_{\rm SM}\) links commute with \(X\). See `X2_COMBO_REPORT.md:55–68`, `REPORT.md:88–93`.
- \(U(1)_X\) is the centralizer of \(SU(5)\subset Spin(10)\), so the commutation claim is correct.
- Electroweak breaking does not preserve bare \(X\); it preserves \(X+4Y=5(B-L)\). Thus the surviving physical global symmetry is \(U(1)_{B-L}\), modulo hypercharge gauge transformations (`REPORT.md:95`).
- Correction: anomaly cancellation alone does not protect a lattice action. The valid argument is the manifest finite-cutoff symmetry \([H_{X2},Q_X]=0\); the vanishing anomalies ensure no obstruction after integrating out fields. The symmetric mirror vacuum remains an unproved condition (`X2_COMBO_REPORT.md:169–188`, `REPORT.md:101–105`).
- Therefore \(\nu^c\nu^c\) is the correct minimal breaking operator, and Dirac neutrinos, zero ordinary \(0\nu\beta\beta\), and no \(n\!-\!\bar n\) follow conditionally.

### R1 — numerics confirmed; headline scope narrowed

- Fresh \(N=40\) runs reproduced \(L_0=0.0820790\), traceless leak \(0.00720946\), and on-site \(K=0.00150340\), using 83 MB RSS. A centered-\(\mu\), half-step check changed the leak by only 1.1%. This agrees with `scripts/r1_leak.out:9–24,41–48` and `scripts/r1_loop.out:55–81`.
- The staggered-reflection lemma is correct for on-site terms/\(\Delta=0\), but not after inserting the non-onsite mirror proxy (`scripts/r1_loop.out:1–18,82–99`).
- The circulant lemma is correct for a genuinely \(T\)-invariant sector. It does not suppress the CKM-broken down sector.
- An independent frequency-domain calculation reproduces all clock slopes in `scripts/sizes.out:4–8`; the adopted \(3.6\times10^{-17}/{\rm yr}\) clock uncertainty is correct. [Lange et al.](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.126.011102) The NANOGrav amplitude used is also correct. [NANOGrav 15-year result](https://arxiv.org/abs/2306.16213)
- The reported branch numbers are correct outputs of the chosen diagonal-\(E_g\) proxy: A \(=80\)–360, B \(=0.12\)–2.5, B′ \(=2\)–93 (`scripts/sizes.out:36–42`).
- Correction: these are explicitly lower bounds and \(T_{2g}\) was not computed (`REPORT.md:49,63–72`). Hence `FLAV-NEAR` is confirmed only for the registered \(E_g\), U(1), bilinear-proxy completion. The complete X2/SM reading remains `OPEN`. The Lorentz-violation residual is likewise only suggested (`REPORT.md:74–78`).

### R3 — arithmetic confirmed, with two qualifications

- The decay formula is correctly normalized; it matches the standard two-body expression. [Yoo et al., Eq. 2](https://arxiv.org/html/2111.01608v1)
- The Super-K bound \(2.4\times10^{34}\) yr is correct. [Super-Kamiokande](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.102.112011)
- Recalculation gives the stated unit-coefficient scale \(3.19\)–\(6.17\times10^{15}\) GeV and, for \(c_{\rm eff}=10\), \(1/a>1.95\times10^{16}\) GeV. Thus the rounded \(2\times10^{16}\) GeV floor is correct (`scripts/sizes.out:67–75`).
- The “4800×” correction is only the representative \(W_0=0.13\,{\rm GeV}^2,A_R=1\) point. Across the packet’s ranges it is approximately \(5.8\times10^2\)–\(8.1\times10^3\).
- `PDK-SAFE-AT-PLANCK` is conditional on the installed \(c_{\rm eff}\le10\) envelope; X2’s nonperturbative leakage coefficient was not derived (`X2_COMBO_REPORT.md:152–159`, `scripts/sizes.py:169–175`).

### Strongest correct statement

For the X2 Hamiltonian actually written, every microscopic term—including the filtered 10-channel quartic—preserves \(U(1)_X\); standard electroweak breaking leaves a gauge-equivalent exact \(U(1)_{B-L}\), so a symmetric mirror phase forbids Majorana masses, ordinary \(0\nu\beta\beta\), and neutron–antineutron oscillation. The rerun proxy calculation places the selected circulant branch at \(0.12\)–2.5 clock bounds in its diagonal-\(E_g\) channel, while the assumed \(c_{\rm eff}\le10\) proton-decay envelope gives \(1/a\gtrsim2\times10^{16}\) GeV. Neither numerical statement is yet a native X2 prediction because \(T_{2g}\), the chiral non-Abelian loop, the quartic mirror self-energy, and the leakage coefficient remain uncomputed.

Full referee record: [OBS1_REFEREE_VERDICT.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_OBS1/OBS1_REFEREE_VERDICT.md:1>)