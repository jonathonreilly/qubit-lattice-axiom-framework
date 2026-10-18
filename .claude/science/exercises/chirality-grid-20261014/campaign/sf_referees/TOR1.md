**TOR-1 referee record (same-family referee: Claude Opus 5.5, so not independent of the worker)**

**VERDICT: CONFIRMED WITH CORRECTIONS.**

**Correct fixed reading: OPEN.** The failing item is kernel power: no kernel sign is resolved, and the vector-like O reference is not converged-negative. PREREG.md:137-138 requires the reference to be converged-negative, and a value inside the error does not meet that. G-LEG-T passes as it was registered, but item (b), locality, is weaker than "passes on every item" says.

**Spot checks.** My scripts are `ref_TOR1/sf/chk_kernel.py`, `chk_first.py` and `chk_toron.py`; each used under 20 MB with OMP_NUM_THREADS=2. I did not write REFEREE.md.
- **Kernel, recomputed from the saved log-kernels.** λ_min at level B is chi −6.5128e-7, mod −6.5287e-7, O −2.2323e-7, vec0 −2.2189e-7, W −3.6543e-6. E is 1.087e-3, 2.42e-4, 2.09e-5, 2.11e-5 and 1.26e-4 in the same order. |Z_chi − Z_mod| = 3.96e-7, Δλ = +1.59e-9, and the chi B→B′ change is 1.7e-10. All of these match POST3.out:1-8.
- **Toron data** match TORON_sq.out. The local decay rates are 0.710, 0.699, 0.696 and 0.695 per site, tending to ln 2; L1 behaves the same way.

**Per-item findings**

1. **Measure legitimacy: confirmed as a construction.**
   - The toron phase is S_t(w_x) = (Γ_t(w_x) − Γ_t(0))/2π with S_x(·,0) = 0 (tor1_lib.py:314). This is exactly Lüscher's eqs. 9.10–9.12 for n = 2 with B° = 0 (luscher_text.txt:1494-1556). Its integral along the code's L-shaped path is w_t·S_t.
   - C(11112) = 0 is confirmed by independent code (B2C_Lx4_Lt8_g16.out:11-12).
   - Caveat 1: the code's own algebra (tor1_lib.py:13-15) makes closure equivalent to h_x(0) = h_t(0) = 1 plus winding 0. The base holonomies come only from the worker's code.
   - Caveat 2: Lüscher's premise "L exceeds a certain multiple of ρ" (luscher_text.txt:1984) does not hold at Lx = 4, where the finite-volume part is O(1) (0.22).

2. **Gauge invariance: confirmed.**
   - The 4e-14 figure (T0_Lx4_Lt8.out:21) holds by construction (tor1_lib.py:89).
   - The real test is the un-fixed Ward test. It converges as Ns⁻⁴ with s_k = −1 and stalls at 3.36e-3 with s_k = +1 (WARD_Lx4_Lt8.out:8-19).
   - The JCUR Ward ratio tends to 1 as Ns⁻² (JCUR_WARD_Lx4_Lt8_Ns16.out:8-13). Any gauge-invariant measure satisfies this identity, so it identifies the measure term but does not test locality.

3. **Locality (b): correction.**
   - The registered kbb statistic also passes for the anomalous L1 control, at 3.2σ and 3.9σ (LOC_Lx4_Lt8_L1.out:6, LOC_Lx8_Lt8_L1.out:4). It cannot tell the two apart.
   - At Lx = 4 the 11112 measure-current response has a plateau of 1.0–1.8e-3 at d = 3–5 (JCUR_Lx4_8_11112_2_7402.out:11,16). That is 0.4–0.7 times L1's plateau of 2.5e-3 (JCUR_Lx4_8_L1_1_7402.out:11). The report leaves this out.
   - The two separate only at 8×8, by at least 22× (JCUR_Lx8_8_*:11-12). Even there the profile drops in a step at d = 4→5 rather than decaying as a clean exponential.
   - So exponential locality is supported at 8×8 and not shown at Lx = 4, the size the kernel uses.

4. **Closure, L1 control, reflection: confirmed** (T0_Lx4_Lt8.out:6,23-31). 11112 closes to 5e-14 around x and 2e-10 around t. For L1, arg Q = −w_t exactly. The reflection constant is c = 0 to 8.5e-14.

5. **Is E honest? Yes; it is not inflated.**
   - The diagonals are normalised to 1, so q_plane rests on one off-diagonal entry for chi, (0,5), and two for the cheap kernels, (0,4) and (1,3), out of 15. E is therefore a sampled estimate and could be low.
   - Separate check: a first-order eigenvalue shift using only those measured plane changes gives −4.0e-6 (chi), −2.1e-6 (mod), +1.9e-7 (O) and +8.3e-6 (W). Each is at least as large as the λ_min it would shift, so quadrature error controls the sign. OPEN does not depend on the k·max form of E.

6. **No power from the O reference.**
   - Pool P2 was found by searching on λ_min(O) at plane level n = 2 (tor1_search.py:1-3), the same plane level as the reported kernel. At that level the per-entry plane error (3.5e-6) is about 15× the final |λ_min(O)| of 2.2e-7, so the search was tuning quadrature noise.
   - The random pool P1 is PSD in every kernel (POST_partial1.out).

7. **The phase finding is right but narrow.**
   - At Lt = 4 every kernel node has w_x ≡ 0, so the S-phase is identically 0 (PHASE_probe.out:1-3). The kernel never tests the Lemma 9.2 toron sector. "The phase does not matter" applies only to this degenerate geometry.
   - The off-diagonal entries are real to 3e-14 even though node phases reach ±1.6e-2. I found no symmetry that explains this exact realness. It does not affect the reading.

8. **Wilson side finding: correction.**
   - REPORT.md:31 says "K2c's Lx = 2 positivity argument does not carry over." The data do not support this, and it should be withdrawn.
   - The measured plane refinements push the W λ_min positive at first order (+8.3e-6 against −3.65e-6). W is also PSD on the random pool P1 (+1.6e-5, POST_partial1.out:10).
   - Correct wording: the sign is unresolved, and the negative value is likely an n = 2 plane-quadrature artifact picked up by the O search. TESTS.md:701 needs the same qualifier.

9. **Minor.**
   - `…_TOR1_Zchi_B.npy` actually holds the level-A (2,8) chi kernel (λ = −6.4457e-7). tor1_post2.py:38,50 wrote it before the chi B level existed.
   - REPORT.md:121 lists `_F3/_F7` files, but there is no F7 file; the saved files are `_B` and `_F3`.
   - "1–4 orders below E" (REPORT.md:25) should be 1.5–3.2.
   - The toron fit "±0.0017 (409σ)" is a fit to an exact, drifting sequence, so its error bar means little; ln 2 is the limit the rate approaches.

**Strongest correct statement.** On a 4×Lt torus, a Lüscher-type measure for 11112 was built and checked. It consists of the canonical decomposition, a toron sector from Lemma 9.2 (n = 2), and straight-ray transverse transport with the eq. 5.8 phase. It is gauge invariant (the un-fixed Ward residual converges as Ns⁻⁴). It is single-valued around both Wilson-line cycles, with C = 0 confirmed by independent code. It satisfies the reflection condition with c = 0. The anomalous L1 control fails integrability with winding 1. The measure's finite-volume toron part decays at ln 2 per site but is O(1) at Lx = 4. At that size the measure current does not separate 11112 from L1; the separation (at least 22×) appears only at 8×8. The RP kernel at Lx = 4, Lt = 4, k = 6 is unresolved: every λ_min (about 1e-7 to 6e-7 of the largest eigenvalue) lies 1.5–3 orders of magnitude inside a plane-quadrature error, and even partial refinement shows that error sets the sign. The vector-like reference provides no power. The toron sector is never exercised on the kernel nodes, since w_x ≡ 0 there. Nothing is established about Wilson + hard-weight positivity at Lx = 4. Reading: **OPEN (kernel power).**