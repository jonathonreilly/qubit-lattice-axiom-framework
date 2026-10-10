# C3 lane M-A: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. Codex sol referee: pending if the verdict is a FAIL or no-go.

**Verdict (worker):** M-PASS, bounded to the pre-registered grid (electron 1 keV/c to 10 GeV/c, proton 1 MeV/c to 7 TeV/c, sigma and sigma_d in {1 nm, 1 um, 1 mm}, L = 1 km, l = l_P). Worst case Var/mean^2 = 2.0e-78 (proton at 1 MeV/c, sigma = sigma_d = 1 nm), against the bar of 0.1. Every grid point meets the pre-registered "controlled-PASS" conditions: every small parameter is below 0.1, and the result holds for any chain-rate coefficient k <= 3.1 k_0, while the derived k is k_0 (1 + O((m l)^2)). Two caveats. (1) Two steps of the upper side are ARGUED: the bound on the vertex-disjoint stretch kernel, and the O(1) end factor. (2) The same law predicts loss of coherence below 1 km for protons slower than about 0.32 MeV/c, and microsecond decoherence for heavy particles if they were elementary Johnston scalars. Both cases are off the grid and need a dated follow-up test; they are not a reinterpretation of this one.

**Plain summary:** E1-prime found the massive path sum noisy between single events; this lane computed the physical object instead: a wavepacket sent into a smeared detector, with every regeneration event along the way included. Smearing at both ends removes the single-event noise. What remains has two parts: one-regeneration noise, which adds up linearly with distance and is suppressed by (m l)^4; and a part that grows exponentially at exactly 0.2549 m^2 l per unit of proper time but starts from a prefactor of order (m l)^6. Both come from exact Poisson tools: an exact add-one formula, the chaos lower bound, the Poincare upper bound, and an exact renewal factorization of the second moment. Simulation checks them in the accessible range, where the one-regeneration term accounts for the whole variance to within about 10-15%. At l = l_Planck and L = 1 km, Var/mean^2 is below 2e-78 for electrons (1 keV/c to 10 GeV/c) and protons (1 MeV/c to 7 TeV/c), so the fixed reading gives M-PASS on the pre-registered grid. The same law says a proton or neutron at rest loses coherence after about 10 ms of proper time, so protons slower than about 0.3 MeV/c lose it before 1 km, and atoms would lose it within microseconds if they were treated as elementary Johnston scalars; those cases are off the grid and need their own dated test.

## Verdict against the fixed M-reading

**Lane:** M-A, Johnston massive path sum, packet plus detector (Campaign C3, lane M). The readings are the E1-prime M-readings, used unchanged. **The pre-registration is in `PREREG.md`, stamped Sat Oct 10 01:04:39 UTC 2026, before any computation.**

**Verdict: M-PASS, bounded to the pre-registered grid.**
- **Grid:** electron p = 1 keV/c to 10 GeV/c and proton p = 1 MeV/c to 7 TeV/c, in decades plus 7 TeV; sigma, sigma_d in {1 nm, 1 um, 1 mm}; L = 1 km; l = l_P.
- **Worst case:** R = Var F/|E F|^2 = 2.0e-78, for the proton at 1 MeV/c with sigma = sigma_d = 1 nm. The fixed bar is R < 0.1.
- **Pre-registered conditions:** every grid point is "controlled-PASS".
  - Every small parameter is below 0.1 there.
  - The outcome does not change for any chain-rate coefficient k <= 3 k_0. The smallest margin is k_crit = 3.1 k_0, at the proton's lowest grid momentum.
  - Section 3 shows that the rate is k_0 (1 + O((m l)^2)); the O((m l)^2) bound is ARGUED.
- **Two ARGUED steps on the upper side** (labels below):
  - the bound on the vertex-disjoint stretch kernel E_2;
  - the O(1) end factor C of the chain term.

  Neither can move a grid point: both enter the threshold only logarithmically, and C was scanned from 1/16 to 100.
- **Off-grid consequence, which I flag and do not fold into the verdict.** The same law gives R >= 1 before 1 km for protons with p below about 0.32 MeV/c (kinetic energy below about 50 eV). The coherence proper time of a proton or neutron is tau* = 3.0e6 m (10 ms). Heavy particles treated as elementary Johnston scalars decohere much faster: tau* = 1.2 us for Rb-87. Using either case would need a dated new test; TESTS.md says readings are never changed after a run.
- **Referee requested anyway** (needs_referee = true), for three reasons:
  - the PASS reverses the refereed E1-prime M-INCONCLUSIVE;
  - it rests partly on ARGUED steps;
  - the law carries a FAIL-type prediction just off the grid.

## Plain summary

E1-prime found the massive path sum noisy between single events; this lane computed the physical object instead: a wavepacket sent into a smeared detector, with every regeneration event along the way included. Smearing at both ends removes the single-event noise. What remains has two parts:
- **one-regeneration noise**, which adds up linearly with distance and is suppressed by (m l)^4;
- **a part that grows exponentially** at exactly 0.2549 m^2 l per unit of proper time, but starts from a prefactor of order (m l)^6.

Both come from exact Poisson tools: an exact add-one formula, the chaos lower bound, the Poincare upper bound, and an exact renewal factorization of the second moment. Simulation checks them in the accessible range, where the one-regeneration term accounts for the whole variance to within about 10-15%.

At l = l_P and L = 1 km, Var/mean^2 is below 2e-78 for electrons and protons on the grid, so the fixed reading gives M-PASS. The same law says:
- a proton or neutron at rest loses coherence after about 10 ms of proper time, so protons slower than about 0.3 MeV/c lose it before 1 km;
- atoms would lose it within microseconds if they were treated as elementary Johnston scalars.

## What I read (in full)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 233 lines).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, including all 3 approved primitives. None is used here, beyond scale_reference for l = l_P units.
- In the packet:
  - TESTS.md in full: the rules, T0-T2, E1-E3, E1-prime and its results, E1-prime-b, and Campaign C3.
  - SUMMARY.md sections 7-9.
  - agents/E1p_report.md, agents/E1p_referee.md, agents/supervisor_E1p_b.md, agents/E1p_b_referee.md.
- Code: scripts/E1p/e1p_core.py, E1p_3_massive4d.py, E1p_3b_analyse4d.py, E1p_5_mean4d.py, E1p_6_renewal4d.py, E1p_6b_renewal_rate.py, E1p_6c_KJ_seed.py, E1p_7_translate.py, and the output E1p_6_renewal4d.out.
- No papers were downloaded.

## Setting and observable (test setting only)

- **Substrate:** a Poisson process Pi on M^{1,3} with intensity rho = l^-4.
- **Kernel:** K = aL(I - abL)^-1, with a = sqrt(rho)/(2 pi sqrt6) and b = -m^2/rho.
- **Fields and amplitude:**
  - phi_s = rho^-1 K psi_s (forward);
  - phi_a = rho^-1 psi_d^T K (adjoint, backward);
  - F = rho^-1 sum_x psi_d(x) phi_s(x).
- **Source:** psi_s is a Gaussian envelope (rms width sigma of |psi|^2) times the on-shell mode e^{-ik.y}.
- **Detector:** psi_d is a Gaussian of width sigma_d times e^{+ik.x}, centred on the classical arrival point after lab distance L.
- **Quantity:** R = Var F/|E F|^2, where Var F = E|F - EF|^2.
- **Proper time:** tau = L/(beta gamma) = L m/p.
- **Axiom conflicts:** as in E1 and E1-prime.

## Method and derivation

### 1. Exact tools

- **(EXACT) Add-one resolvent identity.** Write dL for the change in L when a point z is added: the links of z are added, and the links (u,v) with z in I(v,u) are removed. Then K' - K = a (I + bK') dL (I + bK). Specialised to F, this gives D_z F = V_z + Kill_z, with:
  - V_z = rho^-1 [psi_d(z) phi_s'(z) + psi_s(z) phi_a'(z)] + b phi_a'(z) phi_s'(z), where phi_s'(z) = a sum over the maximal past of z of [rho^-1 psi_s + b phi_s], and phi_a'(z) likewise over the minimal future;
  - Kill_z = - sum over links v <. u with v < z < u of [rho^-1 psi_d(u) + b phi_a(u)] a [rho^-1 psi_s(v) + b phi_s(v)].
- **(CHECKED)** Brute-force insertion and full recomputation on a 4D diamond with N = 871, at 12 probe points and 3 masses. The maximum relative deviation is 5e-9 (`out/test_addone.out`). The forward and adjoint F agree to 3e-15.
- **(EXACT) Bounds** (Last-Penrose Thms 18.6 and 18.7, for F in L^2; complex F by real and imaginary parts):
  - first-chaos lower bound FC = rho int |E D_z F|^2 <= Var F;
  - Poincare upper bound Var F <= PC = rho int E|D_z F|^2.
- **(EXACT) First-chaos kernel.**
  - phi_a'(z) and phi_s'(z) depend on Pi in future(z) and past(z), which are independent. So E V_z = rho^-1 (psi_d phibar_s + psi_s phibar_a) + b phibar_a phibar_s.
  - By Mecke, and independence of past(v), I(v,u) and future(u): E Kill_z = - rho^2 int int Phibar_a(u) a P1(u-v) 1{z in I(v,u)} Phibar_s(v), with Phibar = rho^-1 psi + b phibar.
  - The fields phibar are the exact finite-density means (Johnston eq. 3.15).

### 2. The one-regeneration (first-chaos) law

**Bulk coefficient.** For an on-shell mode, E Kill_z = -c_D b phibar_a phibar_s in the bulk, where:
- c_D = b rho^2 a int d^4X P1(X) V(X) e^{-ik.X}, with P1 = e^{-rho V};
- in the rest frame, c_D = -m^2 a 4 pi int dtau tau^3 P1 V K_1(i m tau)/(i m tau), the Abel continuation of int sinh^2(eta) e^{-z cosh eta} d eta = K_1(z)/z.

Leading order (EXACT as m l -> 0): int = -pi sqrt6/m^2, so **c_D = 1/2**. Numerically (CHECKED, `out/cD_planewave.out`):

| m l | 0.01 | 0.03 | 0.1 | 0.2 | 0.3 |
|---|---|---|---|---|---|
| c_D | 0.50036 | 0.50246 | 0.5179-0.012i | 0.549-0.048i | 0.579-0.106i |

A direct convergence-factor integral at m l = 0.3 gives 0.545+0.073i at eps = 0.05 and 0.576-0.031i at eps = 0.02, approaching the Bessel value.

**First-chaos law.** Hence E D_z F = (b/2) phibar_a phibar_s (1 + O(m l) + O((m sigma)^-2)) in the bulk, and:
- **R_FC = (m^4 l^4/4) int |phibar_a phibar_s|^2 d^4z / |Fbar|^2**, plus endpoint (Mecke-diagonal) terms of order (l/sigma)^4.
- This is a rigorous lower bound up to the controlled asymptotic evaluation (EXACT inequality + CONTROLLED ASYMPTOTIC).

**For quasi-monochromatic packets** (ARGUED, standard paraxial step):
- Fbar = 2E int phibar_a phibar_s d^3z, the Klein-Gordon product, on any slice.
- So R_FC = m^4 l^4 L/(16 E p V_eff), with V_eff = (4pi)^3 s^6/((2pi)^{3/2} s^3) = 126.0 s^3 and 1/s^2 = 1/sigma^2 + 1/sigma_d^2.
- Lorentz-invariant form: R_FC = m^2 l^4 tau/(16 V_eff,rest).
- The minimal width gives an upper value; packet spreading only increases V_eff.
- **Regeneration accumulates diffusively, proportional to L.**

### 3. Exact renewal of the second moment, and the growth rate

**(EXACT) Factorization.** Expand E|F|^2 over pairs of link paths (Mecke).
- The common vertices z_1 < ... < z_n of the two replicas are totally ordered.
- Between consecutive common vertices, either the replicas share the single link, or they run vertex-disjoint segments of at least 2 links each. A direct link plus an indirect path is impossible, because the link needs an empty interval.
- Each stretch lies in I(z_i, z_{i+1}). These intervals are disjoint, and the end stretches lie in past(z_1) and future(z_n). So the presence probability factorizes exactly over stretches:

  E|F|^2 = T_0 + sum_n int A_s(z_1) Prod (b^2 rho) S_true(z_{i+1} - z_i) A_d(z_n),

  with S_true = a^2 P1 + E_2. Here E_2 is the joint weight of vertex-disjoint segment pairs, including their mutual overlap and exclusion corrections. **The E1-prime "overlap-free" omission affects only E_2.**

**(EXACT) Pure shared-link chains.** They sum to a times Johnston's finite-density propagator of a tachyon with M^2 = a b^2 rho = m^4 l^2/(2 pi sqrt6). So **M = k_0 m^2 l, with k_0 = (2 pi sqrt6)^-1/2 = 0.25490.**
- **(CHECKED)** The finite-density Volterra solution grows at 0.1013 for M = 0.1 and at 0.1967 for M = 0.2 (`out/pure_chain_tachyon.out`).
- The physical M l is about 1e-39.

**(ARGUED) The E_2 correction to the rate.** E_2 changes the rate only at relative O((m l)^2) + O(M l).
- Continuum: int d^3x Kbar_{>=2}^2 = m^2 t/(8 pi). The relative rate shift is therefore about 0.61 (m l)^2.
- Needle-overlap enhancement acts only on side-by-side distinct segments. Their phase space per hop of length R is about l/R, and the hops that set the rate have R ~ 1/M.
- So **M_true = k_0 m^2 l [1 + O((m l)^2) + O(M l)].**
- The chaos-chain value k_chaos = 0.2143 (P1^2 in place of P1) is the part captured by the chain terms of the chaos expansion. The link's own variance is redistributed into higher chaoses.

### 4. The packet-plus-detector law (ARGUED structure, with exact pieces)

R = R_FC + R_chain + R_delta + R_end + (massless direct part):
- **R_chain** = C k_0^2 (m l)^6 x h(x)/(16 pi), with x = M tau and h(x) = int_0^1 (1-s) I_1(xs)/s ds.
  - Checked against quadrature: log h(87.4) = 75.336 both ways.
  - The packet volume cancels.
  - C is the O(1) end factor (the analogue of (1-c_D)^2), scanned from 1/16 to 100.
- **R_delta** = 4 R_FC (M s)^2 (1/2 + ln(2 gamma^2)/4): one shared link between shared vertices.
- **R_end** = about 2 l^4/(126 s^4): source and detector counting.
- **Massless direct part:** at most (3 + C' s/D)/Nbar_links, by E1-prime-b.
- **The mean's complex pole** (0.612 m^3 l^2) gives one e-fold per 7e22 m for the proton. Negligible.

### 5. Numerical check (rho = 1)

- Poisson diamonds of height 16 (N = 8,600) and 18.5 (N = 15,300).
- Gaussian blobs of width 1.2 or 1.6, rest-frame on-shell modulation, m l from 0.1 to 0.6.
- Per realization: F for every configuration and mass. At 240-400 fixed probe points: D_z F = V_z + Kill_z.
- FC and PC by importance sampling.
- **Sampler bug, found and fixed.** The first proposal's uniform component was drawn in the bounding box but weighted as uniform-in-diamond. I recomputed q for H16 and H18; the diamond-volume check now gives 8121 against the exact 8579 for CV16.
- **Coverage.** The H16 and H18 proposals under-sample the bulk and the light-cone waist. There, PC/Var < 1 in several columns, which is impossible since PC >= Var is a theorem. So only Var and the means are used from H16 and H18.
- **The full-coverage run CV16** (uniform-in-diamond weight 0.5) gives the sandwich.

## Results

### Table 1: in-range sandwich (CV16; 150 realizations, 400 probes; joint bootstrap 16/50/84%)

| config (t_s, sigma, t_d, sigma_d) | m l | m T | Var/|EF|^2 | Var/FC | PC/Var | bulk share of FC |
|---|---|---|---|---|---|---|
| (3.6, 1.2, 12.4, 1.2) | 0.15 | 1.32 | 7.1e-3 | 0.49 / 0.66 / 0.87 (*) | 1.24 / 1.61 / 2.15 | 0.04 |
| same | 0.30 | 2.64 | 6.7e-3 | 0.53 / 0.67 / 0.84 (*) | 1.30 / 1.62 / 2.05 | 0.07 |
| same | 0.45 | 3.96 | 1.05e-2 | 0.84 / 0.97 / 1.14 | 1.21 / 1.39 / 1.61 | 0.33 |
| same | 0.60 | 5.28 | 1.35e-2 | 0.96 / 1.13 / 1.36 | 1.38 / 1.61 / 1.84 | 0.48 |
| (4.8, 1.6, 11.2, 1.6) | 0.15 | 0.96 | 1.7e-3 | 0.98 / 1.14 / 1.33 | 0.91 / 1.05 / 1.21 | 0.02 |
| same | 0.30 | 1.92 | 2.9e-3 | 0.84 / 0.95 / 1.10 | 1.06 / 1.22 / 1.38 | 0.04 |
| same | 0.45 | 2.88 | 2.5e-3 | 0.86 / 0.99 / 1.17 | 1.07 / 1.24 / 1.43 | 0.05 |
| same | 0.60 | 3.84 | 2.8e-3 | 0.97 / 1.09 / 1.23 | 1.20 / 1.35 / 1.51 | 0.05 |

(*) Heavy-tailed: 5 probes carry 41-47% of FC. These rows are estimator-limited; the theorem requires Var >= FC.

**CHECKED:**
- **Var is about FC × (1.0-1.1)**, to the stated statistical precision, including rows where the bulk regeneration term is 33-48% of FC. The first chaos dominates; higher chaoses are small in the accessible range, where M tau is much less than 1.
- PC sits 5-60% above Var.
- **Per-realization relative noise of F:** sd/|mean| = 0.04-0.12 (CV16), 0.04-0.20 (H16), 0.05-0.24 (H18). In range it is dominated by counting at the endpoint blobs.
- **Not resolved in range:** the measured bulk kill ratio c_eff scatters from -0.5 to +0.33, with imaginary parts of about 0.1-0.3. Here m sigma < 1 and the diamond truncates links, so this is not the plane-wave regime of c_D = 1/2. c_D = 1/2 rests on the analytic limit in section 2.

### Table 2: physics at l = l_P, L = 1 km (`out/translate_ma.out`)

The worst case over sigma and sigma_d is always sigma = sigma_d = 1 nm. k_crit is the chain-rate coefficient at which R would reach 0.1.

| particle | p | beta gamma | tau [m] | x = k_0 m^2 l tau | R (worst) | k_crit/k_0 |
|---|---|---|---|---|---|---|
| electron | 1 keV/c | 1.96e-3 | 5.1e5 | 1.4e-5 | 3.3e-85 | 2e7 |
| electron | 1 MeV/c | 1.96 | 5.1e2 | 1.4e-8 | 1.5e-88 | > 1e8 |
| electron | 10 GeV/c | 1.96e4 | 5.1e-2 | 1.4e-12 | 1.7e-96 | > 1e8 |
| proton | 1 MeV/c | 1.07e-3 | 9.4e5 | 87.4 | 2.0e-78 (R_chain 1.2e-83) | 3.15 (3.10 at C = 100) |
| proton | 10 MeV/c | 1.07e-2 | 9.4e4 | 8.7 | 2.0e-79 | 31 |
| proton | 100 MeV/c | 0.107 | 9.4e3 | 0.87 | 2.0e-80 | 305 |
| proton | 1 GeV/c | 1.07 | 9.4e2 | 0.087 | 1.4e-81 | 3.0e3 |
| proton | 100 GeV/c | 107 | 9.4 | 8.7e-4 | 1.9e-85 | 2.9e5 |
| proton | 7 TeV/c | 7.5e3 | 0.13 | 1.2e-5 | 3.9e-89 | 2e7 |

Per-realization relative noise is sqrt(R): at most 1.4e-39.

### Table 3: thresholds (`out/translate_ma.out`, `out/slow_threshold.out`)

**Proton, threshold momentum p\* for R = 0.1 at 1 km:**

| k/k_0 | 0.841 (chaos chain) | 1 | 1.732 | 3 | 10 |
|---|---|---|---|---|---|
| p* | 0.264 MeV/c | 0.315 MeV/c | 0.547 MeV/c | 0.951 MeV/c | 3.2 MeV/c |

**Coherence proper time tau\*** (R = 1, C = 1; the C scan from 1/16 to 100 moves x* by at most 5):
- proton and neutron: x* = 280, tau* = 3.0e6 m = 10.0 ms;
- electron: tau* = 1.18e13 m = 11 h.

**Slow protons, lab distance L\* at which R = 1:**

| p | 1 keV/c | 10 keV/c | 43 keV/c (1 eV) | 100 keV/c | 300 keV/c (48 eV) | 1 MeV/c (533 eV) |
|---|---|---|---|---|---|---|
| L* | 3.2 m | 32 m | 139 m | 320 m | 961 m | 3.2 km |

**If heavier particles were elementary Johnston scalars** (ARGUED, `out/composite_note.out`):

| particle | muon | deuteron | He-4 | Rb-87 | Cs-133 |
|---|---|---|---|---|---|
| tau* | 0.83 s | 2.5 ms | 0.6 ms | 1.2 us | 0.5 us |

## Verdict in detail (pre-registered mapping)

**Small parameters at every grid point:**
- (m l)^2 <= 6e-39;
- (m sigma)^-2 <= 1.5e-7, for the electron at 1 nm;
- (M s)^2 <= 1e-14;
- M l ~ 1e-39;
- l/sigma <= 1.6e-26.

**R and the rate margin:**
- R < 0.1, indeed R <= 2e-78, at every (p, sigma, sigma_d).
- The outcome holds for every k <= 3 k_0: the minimum k_crit is 3.1 k_0, at the proton's 1 MeV/c point. Everywhere else k_crit >= 30 k_0.
- Section 3 makes the rate k_0 to relative O(1e-38) (ARGUED bound on E_2).

So every grid point of both particles is controlled-PASS, which is **M-PASS** under the fixed reading.

**What the PASS rests on, by label:**
- R_FC: the first-chaos lower bound and its evaluation. EXACT + CONTROLLED ASYMPTOTIC.
- The exact renewal factorization and the pure-chain tachyon. EXACT + CHECKED.
- The E_2 bound and the end factor C. ARGUED.
- The KG-product and V_eff step. ARGUED (standard).
- If a referee rejects the E_2 argument, the margin is still 3.1x in the rate at 1 MeV/c, and at least 30x for all proton p >= 10 MeV/c and all electrons.

**Not covered:**
- slow protons below the grid, and composites (above);
- the tensor bridge;
- initial-value dynamics;
- the axiom conflicts.

**Possible empirical tension, outside the reading** (COMPARATOR, from memory, unverified):
- ultracold-neutron gravitational-state experiments (qBounce), with coherent flight times of order 10-30 ms;
- atom interferometers, with interrogation times of about 1 s.

These would conflict with this law if neutrons or atoms propagated as single Johnston scalars of their full mass. That would be a strong constraint on how composites are carried on the substrate.

## What a referee should re-check

1. **The renewal factorization (section 3):**
   - total order of the common vertices;
   - the stretch classification;
   - disjointness and independence of the stretch intervals, and of the end stretches;
   - that the E1-prime overlap omission lives only in E_2.
2. **The E_2 light-cone-weight bound:**
   - the 0.61 (m l)^2 continuum estimate;
   - the side-by-side needle phase space l/R per long hop. This is the main ARGUED step.
3. **The end factor C** of the chain term, and the matched-packet derivation of R_chain, including that the packet volume cancels.
4. **c_D -> 1/2:**
   - the K_1 Abel continuation;
   - the finite-m l table;
   - its use for packets, with corrections O((m sigma)^-2).
5. **R_FC normalisation:** the factor 1/4, Fbar = 2E times the slice overlap, and V_eff = 126 s^3.
6. **The in-range sandwich:**
   - the corrected q;
   - heavy tails in the narrow-blob rows;
   - that the H16 and H18 FC/PC values are not used.
7. **Whether slow protons and composites** need a new dated test, given the off-grid prediction.

## Files

All files are under /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/M-A/.

- **Top level:** PREREG.md.
- **scripts/:**
  - ma_core.py, run_ma.py, run_ma2.py, analyse_ma.py, sandwich_boot.py;
  - test_addone.py, cD_planewave.py, pure_chain_tachyon.py;
  - translate_ma.py, slow_threshold.py, composite_note.py;
  - copies of the packet's e1p_core.py and E1p_5_mean4d.py.
- **out/:**
  - run logs: run_H16.log, run_H18.log, run_B16.log, run_BU16.log (aborted), run_CV16.log;
  - arrays: ma_H16.npz, ma_H18.npz, ma_B16.npz, ma_CV16.npz;
  - analyses: analyse_H16.out, analyse_H18.out, analyse_B16.out, analyse_CV16.out, sandwich_boot_CV16.out;
  - auxiliary outputs: test_addone.out, cD_planewave.out, pure_chain_tachyon.out, translate_ma.out, slow_threshold.out, composite_note.out.
- **No repository file was edited.**

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** False

**Corrected verdict:** M-INCONCLUSIVE.

At the nominal rate k0, the corrected law still gives R < 0.1 at L = 1 km at every grid point. The worst case is now about 1.5e-60, not 2e-78, and it comes from the chain term rather than the first chaos.

Under the worker's own pre-registered mapping:
- **Electrons, all grid momenta:** controlled-PASS. k_crit is above 1000 k0.
- **Protons at p >= 10 MeV/c:** controlled-PASS. k_crit is at least 25 k0.
- **Proton at 1 MeV/c:** NOT controlled-PASS. Once the source-detector overlap factor is included, k_crit falls to 2.49-2.58 k0 at the 1 nm/1 nm corner and to 2.65-2.97 k0 at the other mismatched corners. That is below the pre-registered k <= 3 k0 margin. By PREREG this alone makes the verdict M-INCONCLUSIVE.

Slow protons are inside the reading's scope ("the proton at laboratory momenta"). For them, the same law gives R >= 0.1 before 1 km when p < 0.32-0.40 MeV/c (kinetic energy below about 53-83 eV). For a thermal proton it gives R(1 km) ~ 10^5417. This is not an M-FAIL: the exponential chain term rests on ARGUED steps (the E_2 bound, the end factor C, and the overlap structure), has no simulation in the regime M tau >= 1, and is not a rigorous lower bound. Any FAIL would also need the codex referee first.

The worker's "M-PASS, bounded to the pre-registered grid" does not follow.

**Issues:** 1. MAIN ERROR: the chain term R_chain is missing the source-detector overlap factor, and this breaks the pre-registered margin.
- Structure: E|F|^2_chain ~ (b^2 rho)^2 a int int |phibar_s(z1)|^2 G_tach(zn - z1) |phibar_a(zn)|^2. The end integrals are packet norms, while |EF|^2 = 4E^2 |<psi_a, psi_s>|^2. So R_chain = (worker's formula) / P_tr, where P_tr = |<psi_d | U(T) psi_s>|^2 <= 1.
- "The packet volume cancels" is true only for matched packets with no spreading. translate_ma.py has no sigma dependence at all in R_chain.
- On the pre-registered grid (every sigma, sigma_d combination is required), for the proton at 1 MeV/c, L = 1 km:
  - with spreading, hbar T/2m = 9.9e-11 m^2, far above sigma^2 = 1e-18 m^2, so P_tr = 8.3e-24 at 1 nm/1 nm;
  - even without spreading, P_tr = 8e-18 at 1 nm/1 mm.
- Corrected worst case: R(k0) = 1.45e-60 (chain-dominated), against the worker's 2.0e-78.
- Corrected k_crit at 1 MeV/c: 2.55 k0 (C = 1), 2.58 (C = 1/16), 2.49 (C = 100) at 1 nm/1 nm; 2.65-2.97 at the other mismatched corners. The worker reported 3.15/3.10. This is below the 3 k0 margin, so that grid point is not controlled-PASS.
- At 10 MeV/c, k_crit is 25.7 k0, not 31.
- Other figures are also wrong: noise of at most 1.4e-39 should be about 1.2e-30; tau* = 10 ms holds only for P_tr = 1.
- R_FC is unaffected. I confirmed by Cauchy-Schwarz that spreading only lowers the per-slice ratio: (s^2 + s_d^2)(t^2/s^2 + (T - t)^2/s_d^2) >= T^2.

2. The reading's scope was narrowed.
- C3 says "Evaluate the electron and the proton at laboratory momenta". M-PASS needs both particles; M-FAIL is triggered by either.
- The worker's proton grid starts at 1 MeV/c (kinetic energy 533 eV). The electron grid starts at 1 keV/c (about 1 eV).
- The same law says protons with kinetic energy below about 50-80 eV lose coherence before 1 km. Examples: L* is about 139 m at 1 eV, and R(1 km) ~ 10^5417 for a thermal proton.
- Calling this "off-grid, would need a dated new test" misapplies the never-change-readings rule. Slow protons are inside the fixed reading; only the worker's PREREG grid left them out. Composites are genuinely outside.
- So "M-PASS for both particles" is not earned.

3. Reading text. The E1-prime M-PASS reads: "noise stays bounded (no exponential growth) and ...". The worker's own law grows as e^{k0 m^2 l tau}. The C3 restatement drops that clause. The worker says the E1-prime readings were "used unchanged" but never addresses it. Under the E1-prime wording, M-PASS is excluded outright. The supervisor should resolve this ambiguity.

4. The upper side is not controlled.
- R_FC is a rigorous lower bound. No Poincare upper bound was evaluated at physical parameters, and the full sum R_FC + R_chain + ... is "ARGUED structure".
- The in-range simulation checks only the generic statement Var ~ FC:
  - FC there is 52-98% endpoint counting (bulk share 0.02-0.48);
  - c_D = 1/2 is not resolved (c_eff runs from -0.51 to +0.34);
  - M tau << 1, so the exponential regime that decides the 1 MeV/c point is never simulated;
  - two rows violate the theorem Var >= FC (0.66, 0.67);
  - the diamond-volume check, 8121 against 8579 (5.3% low), is presented as fixed.
- "The one-regeneration term accounts for the whole variance to within 10-15%" overstates what was tested.

5. Confirmed (not refuting):
- the add-one identity;
- k0 = (2 pi sqrt6)^-1/2 = 0.2549;
- the c_D -> 1/2 limit (I re-derived it analytically);
- the R_FC prefactor 1/16, and V_eff = 126 s^3 including mismatched widths;
- log h(87.4) = 75.336;
- the proper-time conversion tau = L m/p;
- R_FC(worst) = 2.03e-78.

**Re-runs:** All checks are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/M-A/verify/ (OMP_NUM_THREADS=2, each run under 1 min).

(1) **rerun/test_addone.py**, run on copies of the worker's test_addone.py, ma_core.py and e1p_core.py. It reproduces:
- forward and adjoint F agree to 2.8e-15;
- D_zF = V + Kill to a maximum relative error of 5.4e-9 over 12 probes.

(2) **kcrit_overlap.py**, my own implementation of the worker's law plus the overlap factor 1/P_tr. P_tr comes from exact Gaussian free-evolution overlaps, per dimension 2 s s_d / |s^2 + s_d^2 + i hbar T/(2 m_eff)|. It gives:
- log h(87.4) = 75.336, matching the worker;
- the worker's k_crit = 3.15 reproduced when the overlap is dropped;
- with the overlap at proton 1 MeV/c: P_tr = 8.3e-24 and R_chain(k0) = 1.45e-60 at 1 nm/1 nm; k_crit/k0 = 2.55 (C = 1), 2.58 (C = 1/16), 2.49 (C = 100); 2.65-2.97 at the other mismatched corners; 3.10-3.18 only at matched 1 mm/1 mm;
- at 10 MeV/c: k_crit/k0 = 25.2-31.3.

(3) **pstar_overlap.py**: the proton threshold p* (R = 0.1 at 1 km, k0) is 0.315 MeV/c without the overlap and 0.33-0.40 MeV/c with it. For a thermal proton (6.85 keV/c), log10 R(1 km) = 5417. For the electron at 1 keV/c, k_crit is above 1000 k0, so the electron is safe.

(4) **Analytic re-derivations (not scripts):**
- c_D -> 1/2 in the limit m l -> 0, via int tau V e^{-rho V} d tau = (sqrt6/4) rho^{-3/2};
- R_FC = m^4 l^4 L/(16 E p V_eff), with V_eff = 8 (2 pi)^{3/2} s^3 = 126 s^3 for mismatched Gaussians;
- R_chain = k0^2 (m l)^6 x h(x)/(16 pi P_tr) at C = 1, from the tachyon chain G_tach containing M I_1(M tau)/(4 pi tau).
