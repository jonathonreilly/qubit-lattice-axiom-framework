The harness blocked writing `c7/hard/photon/REPORT.md` from this sub-agent ("Subagents should return findings as text, not write report files"), so the full report is below. Please save it to that path. I ran no code, made no repo edits and ran no git write commands.

**10-line summary**
1. [ARGUED] No analytic argument settles V = 0. RK is exact but sits at z = 2 with zero electric stiffness. There is no weak-coupling regime: the landed α_G is about 0.28. The 3D literature splits: the diamond QDM is ordered at V = 0, pyrochlore quantum ice is a liquid there.
2. [EXACT core + ARGUED adiabatic step] LSM-type constraint. On zero-flux tori with L_x, L_y even and L_z odd, the gauge map that removes a uniform 2π xy-flux anticommutes with T_x. So a trivially gapped symmetric phase is ruled out, and confinement at V = 0 requires a crystal or topological order.
3. [ARGUED, EXACT Clifford core] Half-integer E puts π flux on every dual plaquette for monopoles, so a monopole condensate breaks translation. The predicted Bragg momenta for a-normal plaquettes have π in the two in-plane directions. The landed scans did not resolve orientations and skipped (π,0,π) and (0,π,π).
4. [EXACT] A link-disjoint plaquette-tiling crystal exists. It gives u ≥ 1/4 variationally, PT2 adds 3/128 and PT3 = 0, so u = 35/128 = 0.2734 against the landed u ≈ 0.287. A crystal would need at least 0.013 g per plaquette from fourth order and beyond.
5. [EXACT] Any transverse gap Δ forces χ(k) ≤ 4u s²/Δ². A Matsubara family of bounds Ω(ω_m) ≥ ω_min contains the landed energy-only bound as its ω_m → ∞ member. Ω(k_min, ω_1) is the decisive observable.
6. [ARGUED arithmetic] At 16³ the projector's guide bias (8.4 g, open PR 9434) is about 74× the Coulomb flux-sector gap (about 0.11 g). Flux gaps and Wilson loops are out of reach with that estimator.
7. [EXACT] Bubble updates in a periodic path integral conserve the net-flip cocycle Δh. Fixing Δh is the same as averaging over static fractional monopoles in every cube, so the ensemble is wrong. An explicit cube 6-cycle exists (hand-checked), and cube moves fix the problem.
8. [ARGUED] Spec: continuous-time path integral with weight g^n and a cube-block uniformized forward-filter/backward-sample (FFBS) heat-bath. Measure χ, G̃(ω_m), Ω, S and 21 Bragg weights. Under 100 MB; roughly 0.3–1 s per sweep at 16³ (estimate).
9. [to be CHECKED] First gate on the exact 864-state 2³ component, with and without cube cycles. Then run L = 8, 12, 16 at β = 2L.
10. Verdict: Coulomb is neither established nor excluded. Gaps above about 0.27 g are excluded, conditional on the landed χ. The path-integral run decides between Ω·L flat (Coulomb) and Bragg growth (crystal).

---

# REPORT — Lane D: is the supplied pure ring model in a Coulomb phase?
c7/hard/photon, 2026-10-01. Derivation only. Labels: EXACT (proof), CHECKED (finite exact test), FLOAT (cited finite numerics), ARGUED.

## 0. What the axioms supply and what is supplied here
The axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`) give Z³, one M₂(C) per site, one nearest-neighbour admissibility distribution, and permanent records. They give no Hamiltonian, no time and no link variables.

Supplied pieces, as in every landed ring-model note:
- (S1) a qubit on every link, with E_l = σ^z_l/2 ∈ {±½};
- (S2) the Gauss law, 3 in and 3 out at each site;
- (S3) H = −g Σ_p R_p with R_p = U_p + U_p†, plus V Σ_p n_p at V = 0;
- (S4) the zero-winding seed flip component;
- (S5, for the QMC) a temperature 1/β.

Literature below is context, not premise.

## 1. The problem
In the thermodynamic limit of (S1–S4), is the ground state a Coulomb phase? That means:
- (C1) χ(k→0) = χ₀ > 0, with the lowest excitation coupled to the transverse field obeying ω(k) ≤ c|k|;
- (C2) no long-range order in any gauge-invariant local operator;
- (C3) flux-sector gaps of 2U/L with U = 1/χ₀, rather than σL.

Finite form: let Ω(L) be an exact upper bound on the lowest excitation coupled to the transverse mode at k_min = 2π/L. Does Ω(L)·L stay bounded while every orientation-resolved Bragg weight stays finite as N grows?

## 2. Obstructions, with exact scope

**O1 — no small parameter at V = 0 [ARGUED].**
- At V = g each component's ground state is the uniform superposition with E = 0 [EXACT]. That makes RK a z = 2 point with zero electric stiffness: all winding sectors are degenerate there.
- Near RK the dual stiffness is U_eff ∝ (g − V) > 0. This is the Moessner–Sondhi and Hermele–Fisher–Balents picture: a soluble point plus "stable over a finite extent".
- Continuity down to V = 0 is not guaranteed. The landed 8³ sweep is smooth (χ̄(π/4) runs from 1.08 at V = 0 to 14.5 near RK [FLOAT]) but uses a 6-point grid.
- In 3+1D, monopoles are particles, not Polyakov instantons. The Coulomb phase is therefore a stable phase, proven for small e² (Guth 1980; Fröhlich–Spencer 1982).
- The spin-½ truncation is not weak coupling. The bare electric term is effectively infinite, but the ice degeneracy generates an infrared coupling. The landed comparator gives α_G = 0.278–0.286 on 8³ [FLOAT], which is O(1).
- 3D precedents split at V = 0:
  - diamond QDM: liquid for about 0.75 < V/t < 1, so V = 0 is the ordered R state (arXiv:1105.1322);
  - pyrochlore quantum ice: liquid down to V/g ≈ −0.5 (figure from the search-indexed text of arXiv:1105.4196; I did not read the full text);
  - QSI's α is "more than an order of magnitude greater than 1/137" (arXiv:2009.04499, conventions differ from α_G);
  - for the cubic S = ½ link model, Wiese calls Coulomb "plausible" (arXiv:1305.1602) and Banerjee–Huffman–Rammelmüller propose one on 3+1D tubes (arXiv:2201.07171).
- Correction to the brief: the Sikora et al. window result is for the diamond lattice, not the cubic QDM.

**O2 — energy data bound excitations from above [EXACT].**
- If the transverse spectral measure has a gap Δ, then χ = 2m₋₁ ≤ 2m₀/Δ ≤ 2m₁/Δ² = 4u s²/Δ².
- So a flat χ excludes Δ > 2s√(u/χ) and nothing below that.
- At 24³ (χ = 1.114, u ≈ 0.2867, k = π/12 [FLOAT, landed]) this excludes Δ > 0.265 g, if χ is unbiased and converged.

**O3 — extensive estimator bias [ARGUED arithmetic].**
- Open PR 9434's guide split is 0.00068 per plaquette at 16³, i.e. 8.4 g in total.
- The Coulomb flux-sector gap there is about 2U/L ≈ 0.11 g (with U ≈ 1/1.11). The ratio is about 74.
- Static-pair and Wilson-type energies are similar O(1) differences of extensive energies.
- The field-curvature signal at h = 0.15 is about 3Nχh²/4 ≈ 76 g. The bias is about 11% of that, consistent with the landed "about a quarter" guide-scheme split.
- The slow late drift of χ is unresolved.

**O4 — closed-history QMC with bubble updates is non-ergodic [EXACT, see D4].** Landed note `THE_PURE_SPIN_HALF_LINK…2026-09-04` records PR #7942's (unverified) mod-2 version of this.

## 3. Escape routes, ranked
1. **R1 — unbiased continuous-time path-integral QMC with cube-block heat-bath (top).**
   - Supplies an algorithm and a finite β; no new physics premise.
   - Would show χ(k_min(L)), G̃(k, ω_m), the bound Ω(L), u, and orientation-resolved Bragg weights, all free of fields and populations.
   - Cheapest decisive test: the 2³ exact gate, then L = 8, 12, 16 (Section 5).
2. **R2 — LSM-type constraint plus π-flux monopoles (D2, done here).**
   - Supplies the adiabatic flux-insertion step and the effective monopole theory.
   - Shows that confinement at V = 0 must be a translation-breaking crystal or topological order, and predicts the Bragg momenta.
   - Cheapest test: re-analyse existing projector snapshots for the 21 orientation-resolved weights.
3. **R3 — crystal energetics (D3).**
   - Supplies the tiling-crystal ansatz.
   - Shows whether the crystal can reach u ≈ 0.287.
   - Test: an exact fourth-order linked-cluster count on 4³ (small combinatorial program).
4. **R4 — flux-sector or static-pair free-energy ratios via sector-switching moves.**
   - Would test the Coulomb identity U_W = 1/χ₀ directly.
   - Acceptance falls with L, so useful at L ≤ 10 only as a cross-check.

## 4. Derivations

**D1 — the decisive observable (answers ii) [EXACT].**
- Take O_a(k) = N^{−½} Σ_{a-links} e^{ik·x_{a+1}} σ^z (the landed cyclic triple) and G̃(k, ω_m) = (1/(3β)) Σ_a ⟨|∫₀^β e^{iω_m τ} O_a dτ|²⟩.
- Since χ″(ω)ω ≥ 0 at any temperature, G̃(z) = ∫dμ(w)/(w + z) with μ ≥ 0, w = ω², z = ω_m².
- G̃(0) = χ in the landed normalization, and ∫dμ = 2·(f-sum) = 4u s².
- Define Ω(z)² = z G̃(z) / (G̃(0) − G̃(z)).
- Because G̃(0) − G̃(z) = z ∫dμ/(w(w+z)), Ω² = ∫dν / ∫(dν/w) with dν = dμ/(w+z). That is a harmonic mean of w, so Ω(z) ≥ ω_min.
- Ω is non-decreasing in z, and Ω(∞)² = 4u s²/χ, which is exactly the landed energy-only bound.
- At T > 0, thermal transitions enter with weight about e^{−βΔ} [ARGUED].
- Consequences:
  - gapped phase: Ω(k_min, ω₁) ≥ Δ for every L;
  - Coulomb: Ω·L tends to a constant (about 2πc);
  - RK-like z = 2: Ω·L² tends to a constant.
- In a path integral, O is diagonal, so ∫e^{iωτ}O dτ is exact from the event list. The estimate is intensive, single-run, free of field fits and free of populations.
- Comparison with the alternatives:
  - photon speed from energy data is the weakest (z → ∞) member of this family, and its χ input carries the O3 bias;
  - flux gaps and Wilson loops discriminate in principle but need the O3/R4 machinery.

**D2 — LSM-type constraint [EXACT core; ARGUED adiabatic step].**
- Take an L_x × L_y × L_z torus with L_x, L_y even and L_z odd. All three section fluxes can be zero.
- Let H(B) carry a phase e^{iB} on every xy-plaquette, with B = 2π/(L_xL_y). It stays translation-invariant.
- Define W = exp(−iΣλE) with:
  - λ_x = −2πy/(L_xL_y) on all x-links;
  - λ_y = 2πx/L_x on the y-links leaving the row y = L_y − 1;
  - λ = 0 elsewhere.
- Checking the bulk, the seams and the xz/yz plaquettes by hand gives curl λ = B mod 2π, hence W H(B) W† = H(0).
- T_x shifts λ_y by −2π/L_x + 2πδ_{x,0}. Therefore T_x W T_x⁻¹ = (−1)^{L_z} e^{∓2πiΦ_y/L_x} W.
- The factor (−1)^{L_z} comes from summing L_z half-integers along one line. On Φ_y = 0 this means T_x W = −W T_x.
- The same holds for any translation-invariant diagonal term V Σ n_p.
- If a unique gapped ground state survived the path 0 → B, then W ψ(B) would be a second ground state of H(0) at momentum P_x + π. That is the Oshikawa–Hastings step [ARGUED].
- Hence no trivially gapped symmetric phase: the options are Coulomb, a crystal, or topological order.
- This is a sanity-checked statement: the uniform, frozen, maximal-flux state is allowed because its Φ_y cancels the phase. It parallels Kobayashi–Shiozaki–Kikuchi–Ryu (arXiv:1805.05367) for dimer models.
- π-flux monopoles [ARGUED]:
  - a unit monopole circling a dual plaquette picks up 2π·E_l = π mod 2π;
  - the magnetic translations therefore pairwise anticommute, which is the Clifford algebra Cl₃ with 2-dimensional irreps [EXACT];
  - no condensate is invariant; the bilinears n_b = ψ†σ_bψ are odd under T_{a≠b};
  - so b-normal plaquettes order at Q_x = (0,π,π), Q_y = (π,0,π), Q_z = (π,π,0).
- The landed check summed all orientations at (π,0,0), (π,π,0) and (π,π,π) with mixed estimators. It never measured (π,0,π) or (0,π,π), and it did not resolve orientations.

**D3 — tiling crystal [EXACT through third order].**
- Construction:
  - xy-plaquettes at (x,y) both even;
  - xz-plaquettes at x odd, z even;
  - yz-plaquettes at y odd, z odd.
- Each link lies in exactly one chosen plaquette (checked for x-, y- and z-links). Every corner meets three chosen plaquettes, so every circulation pattern satisfies the ice rule. Every section flux is zero.
- The product state Π_P (|↻⟩ + |↺⟩)/√2 has ⟨H⟩ = −3Ng/4, so **u ≥ 1/4** variationally.
- Second order: each of the 9N/4 non-chosen plaquettes q touches 4 distinct chosen ones. It circulates with probability 1/8, and flipping it costs exactly 4g. This gives E₂ = −9Ng/128, i.e. **3/128 per plaquette**.
- Third order is zero: on any mod-2 closed surface, the non-chosen faces are at least as many as the chosen ones (n_nc ≥ n_c). Three non-chosen faces would need a cube with three pairwise link-disjoint faces, which is impossible.
- Total u = 35/128 = 0.2734, against the landed u = 0.2867–0.2876. The crystal must gain at least 0.013 g per plaquette at fourth order or beyond.
- Three quarters of cubes have two opposite chosen faces, so fourth-order "cube-ring" terms exist. I did not sum them.
- Whether this state lies in the seed component is open.

**D4 — ergodicity of closed histories [EXACT].**
- A periodic history has a net signed flip count Δh_p per plaquette. Periodicity is equivalent to curl Δh = 0 on every link.
- So Δh is a closed integer 1-cochain on the dual torus: Δh = δφ + Σ_a w_a·(harmonic part), with φ living on cubes and w_a ∈ Z.
- Bubbles, time shifts and any single-plaquette resampling cannot change Δh: changing Δh_p alone would violate curl Δh = 0 on p's links.
- Fourier identity: fixing φ equals ∫Π dθ_c Z({θ_c}). Here θ_c = net background 2-form flux out of cube c, so the restricted ensemble is the model with static fractional monopoles in every cube.
- I estimate the energy bias at about T/6 per plaquette [ARGUED], i.e. about 0.005 g at β = 32.
- The cure exists. Starting from b1 = b2 = t1 = t2 = v00 = +, b3 = b4 = t3 = t4 = v10 = v11 = v01 = −, flipping bottom, y=0, x=1, y=1, x=0, top in that order is valid at every step and returns to the start. Each face has net Δh = +1 (hand-checked).
- Fixing w_a is the same as averaging over a uniform magnetic twist with weight about e^{−βKθ²/(2L)}. Its effect on local observables is suppressed [ARGUED].

## 5. Spec for the follow-up session (do not run here)

**Ensemble.** Z = Tr_comp e^{−βH} = Σ_n g^n ∫dτ₁…dτ_n. A history is a valid closed sequence of flips; at V = 0 its weight is g^n, with no sign problem.

**State.** 3N link initial values, per-link and per-plaquette sorted event lists. At 16³ and β = 32 that is about β·u·3N ≈ 1.1×10⁵ events, well under 100 MB.

**Move: cube-block heat-bath.**
1. Pick a cube c and a cut time τ_cut. Hold the 12 edge states at τ_cut fixed.
2. Enumerate the internal states allowed by the corner out-counts (S ≲ 20 expected) and the 6-face flip adjacency A.
3. The 24 external plaquettes become fixed events: each toggles one cube edge and imposes a circulation constraint.
4. Sample virtual times as a Poisson process of rate Λ = 6g. Candidate times are these plus the existing internal events.
5. Run FFBS (a bridge from x(τ_cut) back to x(τ_cut)) with B = I + (g/Λ)A. Non-self transitions become the new internal events. This is the uniformization Gibbs step of Rao & Teh (2013) [ARGUED exact].

**Conserved quantities.**
- Electric fluxes, the seed component, and w_a are conserved [EXACT].
- φ_c changes under the cube move, which removes O4. Ergodicity within the conserved labels is ARGUED and must be CHECKED.

**Estimators.**
- u = ⟨n⟩/(3Nβ).
- χ(k) and G̃(k, ω_{0..3}) for k_min and 2k_min, using both transverse triples.
- Ω(L) from D1; equal-time S(k).
- B_a(Q) = ⟨|Σ_{p⊥a} e^{iQ·r_p}(n_p − n̄)|²⟩/N_p for all 7 nonzero Q ∈ {0,π}³ and 3 orientations.
- ⟨φ_c²⟩/β as an ergodicity monitor.
- Normalization check: ω_m² G̃ → 4u s².

**Runs.**
1. Gate: exact 2³ seed component (864 states, landed) at β ∈ {1, 4, 16}, comparing u, χ(π) and G̃(π, ω₁). Code blocks generally, because cubes wrap on L = 2. Repeat with cube cycles disabled; a visible shift is the positive control for O4.
2. L = 8 at β ∈ {16, 32}. Compare with landed u and χ = 1.066–1.077.
3. L = 12 at β = 24 and L = 16 at β = 32. With ω(k_min) ≈ 2πc/L, βω ≈ 4πc, so contamination is about e^{−12}.

**Budget.** About 7×10⁴ operations per cube update and 4096 cubes per sweep at 16³: roughly 0.3–1 s per sweep in numba. If τ_auto ~ L² sweeps, χ to 5% takes about 1.5×10⁴ sweeps, i.e. 1.5–4 h [ARGUED]. Benchmark at L = 8 first. Single thread, nice, no BLAS.

**Outcomes.**

| Result | Meaning |
|---|---|
| χ(k_min) flat within 5% for L = 8–16, Ω·L constant, all B_a(Q) bounded | Consistent with Coulomb; Δ ≤ Ω(16) ≈ 0.3 g |
| Some B_a(Q)/N_p → constant, χ falls, Ω levels off | Crystal (confined) |
| χ ∝ L⁻², no Bragg peaks | Gapped topological state (allowed by D2) |
| u_PI(β → ∞) compared with 0.28687 / 0.28755 | Shows which guide in PR 9434 is biased |
| χ_PI compared with the late windows 1.06 / 1.11 | Resolves the slow drift |

## Literature (context only, not premises)
- Sikora et al. arXiv:1105.1322: https://arxiv.org/abs/1105.1322
- Shannon et al. arXiv:1105.4196: https://arxiv.org/abs/1105.4196
- Hermele–Fisher–Balents cond-mat/0305401: https://arxiv.org/abs/cond-mat/0305401
- Bergman–Fiete–Balents PRB 73, 134402: https://journals.aps.org/prb/abstract/10.1103/PhysRevB.73.134402
- Kobayashi–Shiozaki–Kikuchi–Ryu arXiv:1805.05367: https://arxiv.org/abs/1805.05367
- Pace et al. arXiv:2009.04499: https://arxiv.org/abs/2009.04499
- Wiese arXiv:1305.1602: https://arxiv.org/pdf/1305.1602
- Banerjee–Huffman–Rammelmüller arXiv:2201.07171: https://arxiv.org/abs/2201.07171
- Guth 1980, Fröhlich–Spencer 1982, Rao–Teh 2013, Moessner–Sondhi 2003: cited from memory, not fetched.