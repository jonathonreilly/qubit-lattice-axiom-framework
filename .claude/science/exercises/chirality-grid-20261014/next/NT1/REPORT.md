# NT-1 report: does gauged reflection positivity also fail for a chiral measure? (route 1 / set B)

**Reading: CHI-RP-FAIL.**

**Provenance.**
- One Opus 5.5 agent (xhigh), working 20:44–22:15Z. It is the same model family as K2, K2c, X3 and the supervisor, so nothing here is independent. Not refereed.
- The harness blocked the worker from writing this file, so the supervisor saved it from the worker's final message, lightly condensed. Every number and file reference is the worker's.
- **Memory:** each run peaked at 196 MB or less, under the 0.4 GB cap. One process at a time.

## 0. Plain words

1. **The chiral measure.** A genuinely chiral, anomaly-free 2D U(1) lattice measure was built: the "11112" model, with four left-handed charge-1 Weyl fermions and one right-handed charge-2 fermion.
   - The Weyl determinants come from the overlap.
   - The phase comes from Lüscher's abelian construction: parallel transport along the straight path from zero field, plus a gauge-restoring current.
   - The weight is exactly gauge invariant (to 1e-7–1e-8).
   - It satisfies the reflection condition ρ(θU) = conj ρ(U) (to 1e-13). So the RP kernel is Hermitian, and reflection positivity has a clean meaning: Hermitian and PSD.
2. **The kernel has a negative eigenvalue.** This holds on W-matched gauge-invariant witnesses in all 4 pools, with open time and Lt = 12 and 20. Each negative eigenvalue is 4,600–13,600 times the error estimate.
   - The vector-like K2c witness, used as the power reference, reproduces K2c's numbers to every printed digit on the same pools.
   - The chiral violation is about 4.5 times larger.
3. **The phase plays no role on these witnesses.**
   - The chiral kernel equals the kernel built from |ρ_χ| alone to every printed digit (Im Zn ≤ 1.4e-7).
   - Single Weyl determinants have a constant phase here, to about 1e-8.
   - |ρ_χ| = |det D(1)|²·|det D(2)|^{1/2}, a product of fractional powers of vector-like overlap determinants (checked to 7e-14).

   So the failure sits in the part of the weight that does not depend on the measure term. It is the overlap's own failure (K2c) carried over to the chiral theory.
4. **Caveat.** At Lx = 2 the lattice is effectively one-dimensional, so this test cannot probe anomaly cancellation: the same construction gives a gauge-invariant weight even for an anomalous single Weyl fermion. Only open time in 2D was tested.

## 1. Verdict

| Item | Verdict | Basis |
|---|---|---|
| Gauge-invariant chiral measure (11112) satisfying the reflection condition | built | gates G1–G7 (checked) |
| RP kernel Hermitian | yes | h ≤ 8.3e-14 on every pool, with K(a,b) and K(b,a) computed independently (checked) |
| **NT-1** | **CHI-RP-FAIL** | certified negative on 4/4 gated pools; the Wilson and pure-gauge controls are PSD (checked) |
| Phase contribution | none, within error | chiral kernel = modulus kernel; P1 (checked) |
| Anomaly cancellation's role | not tested by this proxy | anomalous L1 is also gauge invariant here; D1′ inconclusive (reading) |

## 2. The measure

"Proved" means the worker's own derivation, unrefereed; "checked" means by script.

**Weyl determinant (proved).**
- In K2's conventions D = 1 + γ5·sign(H_W), so Lüscher's γ̂5 = −S.
- The left-handed space is the positive spectral subspace of H_W(U^e); the right-handed space is the negative one.
- D V = 2 P₊ V, so det M_L = 2^n det(V restricted to the γ5 = +1 rows). This is the Narayanan–Neuberger overlap, with the phase set by the basis V.
- G1: |det M_L|·|det M_R| = |det D| and |M_L| = |M_R| to 2e-14.

**Phase.** The construction follows Lüscher, NPB 549 (1999) 295, hep-lat/9811032. The worker checked the title and scope on arXiv; the formulas are the worker's own derivation within that framework.
1. W0 parallel-transports a fixed free-field basis along U_t = e^{iteA} (`nt1_lib.py:102-128`). This is Lüscher's straight-line homotopy measure term, which vanishes along that path.
2. The anomaly density is 𝒜 = Σ_L e·q_e − Σ_R e·q_e, with q_e(x) = −½ tr S_e(x,x) (`:109-118`).
3. The gauge-restoring current k solves div k = ∫₀¹ 𝒜(tA) dt (`:75-89`).
   - Its time component is the one-dimensional cumulative sum, which exists because Σ𝒜 = 0 (to 3e-15).
   - Each slice's x-links carry ±(𝒜(0,t) − 𝒜(1,t))/4.
4. W = W0 + i·s_k·Σ A·k̄ (`:130`).
   - Proved: L = L0 + dΨ with Ψ = −Σ A·k̄ has the right curvature (integrability) and the right gauge-direction values. So W is exactly gauge invariant.
   - The sign s_k = −1 is a convention, fixed by gate G2.

**Model choice.** 11112 was used instead of 3-4-5-0 because charge 5 is not admissible at K2c's δ = 0.6 (min |H_W| = 0.003, `D1p_Lt12.out`). Charge 2 stays gapped, at 0.132 or more on every ray.

**Gates** (`gates_Lt12_1401.out`, `g4r_Lt12.out`, and the G2/G3 line of every kernel run):

| Gate | Check | Result |
|---|---|---|
| Builder | against `lat2d.full_D` | identical (0.0) |
| G2 | gauge invariance | 1.6e-8 to 1.1e-7 per pool. For comparison: the other sign of s_k gives 5.6e-3, and W0 alone gives 2.8e-3, so the current does the work |
| G3 | reflection condition | constant c, spread ≤ 1.4e-13 |
| G4 | path discretisation | **failed as registered**: plain transport converges only as Ns⁻². With Richardson extrapolation (follow-up F1), R(8)→R(16) moves by 3.1e-8 and R(16)→R(32) by 1.9e-9 |
| G5 | spectral gap at every charge and ray point | ≥ 0.455 / 0.502 / 0.132 / 0.503 |
| G6/G7 | index 0; Σ𝒜 = 0 | pass |

**Anomaly cancellation is not tested (reading).**
- At Lx = 2 the current equation is always solvable, so the anomalous single charge-1 Weyl fermion ("L1") also passes G2 (1.3e-8).
- The bottom-boundary locality diagnostic D1 is absorbed at the open boundary for both models.
- D1′ (flux inserted mid-lattice, `D1p_Lt12.out`): L1 shows a non-decaying plateau of about 4.6e-3, while 11112 grows toward the top. But at Lx = 2 a flux insertion must shift the Wilson lines on one side, so this cannot tell non-locality from a local response. Inconclusive.

## 3. Reflection positivity for a complex weight

**Proved:** with Θ = θ∘conj, K(b,a) = conj K(a,b) for all witnesses if and only if ρ(θU) = conj ρ(U), up to one global constant. The proof substitutes U → θU. RP then means K is Hermitian and PSD.

**How the condition was handled:**
- It was never assumed. G3 measures it, and every kernel computes both orderings, with the Hermiticity defect h folded into the error estimate E.
- The global constant fixes the weight only up to a sign. The physical sign is the one with K(a,a) > 0, which every diagonal entry satisfied (follow-up F3).
- The continuum counterpart is CRT: conj det D_L[A] = ±det D_L[θA].
- Had the condition failed, the pre-registered reading would have been OPEN, not FAIL.

## 4. Results

**Settings (as in K2c):**
- 2D U(1), Lx = 2, open time; M = 1, β_g = 0;
- hard crossing weight δ = 0.6, link reflection;
- W-matched witnesses with plaquette margin 0.55.

**Numerics:**
- Quadrature GL n = 16/32, plus n = 48 on a 24-entry subset.
- Path discretisation R(8), with q_PT measured against R(16).
- Error estimate E = k·max(q, q3, q_PT, h) + 1e-13.
- "Certified negative" means λ_min < −10E.

| Pool | Chiral λ_min (relative to λ_max) | E | \|λ\|/E | Modulus kernel | Vector O, m = 0.05 (K2c) | Massless vector | Wilson / pure gauge |
|---|---|---|---|---|---|---|---|
| Lt12 wsearch 1401 | **−1.0783e-2** (−5.39e-4) | 7.9e-7 | 13,600 | identical | −2.4215e-3 (= K2c) | −2.438e-3 | PSD / PSD |
| Lt12 wgsearch 4401 | **−5.309e-3** (−2.65e-4) | 7.0e-7 | 7,600 | identical | −1.1324e-3 (= K2c) | −1.141e-3 | PSD / PSD |
| T2 chiral search, seed 7401, k = 19 | **−9.629e-3** (−5.07e-4) | 2.1e-6 | 4,600 | identical | −2.155e-3 | −2.171e-3 | PSD / PSD |
| Lt20 wsearch 1420 | **−1.1435e-2** (−5.71e-4) | 1.3e-6 | 8,800 | identical | −2.575e-3 (= K2c −2.58e-3) | −2.593e-3 | PSD / PSD |

- The chiral-to-vector ratio is 4.4–4.7 on every pool.
- Error budget: the largest term is q_PT (≤ 1.1e-7); q ≤ 6e-14 and h ≤ 8.3e-14.
- T2: the random 8-member W-matched start is already negative (−2.45e-4), and the objective falls monotonically.
- P1 (`P1_phase_Lt12.out`): the phase of ρ is constant to 1e-8 or better over nodes and entries, for 11112, L1, L2 and R2.
- `modcheck_Lt12.out`: ln|ρ_χ| − [2 ln det D(1) + ½ ln det D(2)] is constant to 7e-14.

## 5. What it means

- **Route 1 / set B.** The exercise branch's `SUMMARY.md:58` names "the chiral-measure RP test" as the first test. The chiral measure fails just as the vector-like one does in this proxy, so it is no escape from K2c's L3g failure.
- **X3 contingency.** It stays triggered: Π-W for matter, or 5D fermions without Pauli–Villars fields (F2-R's finite-n price, AX:47).
- **Mechanism (reading).** On these witnesses the 2D abelian chiral weight is real and equals det D(1)²·det D(2)^{1/2}. It therefore inherits the overlap's own non-positivity (K2c §2(d), §3.3), scaled by the fermion content.
- **Measure-term freedom (suggested).** This is unlikely to rescue RP, because the failure is carried by the basis-independent modulus. Local counterterms were not scanned.
- **Not shown:** the torus; infinite volume; Lx ≥ 4, where anomaly cancellation becomes testable; 4D; non-abelian groups; 3-4-5-0; Kikukawa-type mirror sectors.

## 6. Deviations

- **F1.** The registered gate G4 failed. Richardson extrapolation was adopted before any kernel was computed.
- **F2.** The first R(32) run was killed for speed before it produced a kernel number. R(8) was used thereafter.
- **F3/F4.** A worker bug gave the normalisation the wrong global sign.
  - The first 1401 run printed −20.0, the sign-flipped kernel, together with an invalid modulus row.
  - The first search had a wrong objective and was restarted with the same seed.
  - After the fix, the 1401 rerun matches the re-read saved kernel exactly. Either sign would have given FAIL.
- **F5.** The last search member closed the gap to 0.060, below the 0.1 gate, so the k = 19 pool was used.
- **Timestamps.** The F1 header time was typed ahead of the clock; a correcting note is appended.
- **Warnings.** numpy slogdet RuntimeWarnings appear in the `.err` files, as in K2/K2c. The affected values are corroborated by G1 (2e-14) and by exact reproduction of K2c's numbers.
- **Not run:** the Lt20 pool 5401, the torus, and 3-4-5-0 at reduced δ.

## Files (`NT1/scripts/`)

**Code:**
- `nt1_lib.py`, `nt1_gates.py`, `nt1_g4r.py`, `nt1_kernel.py`, `nt1_search.py`, `nt1_d1p.py`, `nt1_phase.py`, `nt1_modcheck.py`;
- `lat2d.py`, `k2b_lib.py`, `k2c_lib.py` (sha1-equal to the K2c copies).

**Outputs:**
- `gates_Lt12_1401`, `g4r_Lt12`;
- `T1_Lt12_wsearch1401`, `T1_Lt12_wgsearch4401`, `T1_Lt20_wsearch1420`;
- `T2_search_Lt12_7401`, `T2_kernel_Lt12_7401_k19`;
- `D1p_Lt12`, `P1_phase_Lt12`, `modcheck_Lt12` (all `.out`);
- killed and buggy runs, kept as `*_killed*` / `*signbug*`.

**Data:** pools `pool_*.npz`; chiral kernels `*_Zchi.npy`.
