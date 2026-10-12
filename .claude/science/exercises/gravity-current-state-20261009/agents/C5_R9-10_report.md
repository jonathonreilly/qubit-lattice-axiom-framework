# C5 R9-10 report: a symmetric (Belinfante) stress for the interacting d = 2 box law, and the fall of spinning bound bodies

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 17:16Z to about 18:05Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R9-10/`. Script and outputs in `S/scripts/` (`OMP_NUM_THREADS=2`, about 4 min):
- `r910_belinfante_d2.py` → `r910_belinfante_d2.out` (= `.log`): the final run;
- `r910_belinfante_d2_run1.log`, `_run2.log`: earlier runs, superseded. They differ only in the moving-body velocity matching (run 1 none, run 2 to about 1e-11). Their unmatched raw η values (up to 1.6e-3) came from unequal velocities, not from physics;
- `r81_common.py`: R8-1's module, copied unchanged.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: C5 method (`:2302-2330`); R7-1 (`:3242-3256`, `:3398-3407`); R8-1/R8-2 (`:3445-3466`, `:3550-3557`); round 9 (`:3575-3700`); round 8 referee results (`:3793-3820`); R9-10 (`:3874-3885` at the time of the final read).
- R8-1: `agents/C5_R8-1_report.md` in full and `C5_R8-1_referee_verdict.md`.
- R8-2: `agents/C5_R8-2_report.md:1-200` and `C5_R8-2_referee_verdict.md`.
- R9-2: report `scratchpad/C5/R9-2/R9-2_report.md` and referee verdict `scratchpad/C5/ref_R9-2/REFEREE_VERDICT.md` (CONFIRMED WITH CORRECTIONS, PASS WITH SCOPE in d = 1 only; it appeared during this run).
- R8-1 scripts `r81_common.py`, `r81_d2_chart_algebra.{py,out}`, `r81_d2_lattice_algebra.py`. R9-2 `r92_fall_d1.py`.

**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED. TESTS.md was edited concurrently during the run: line numbers are as read (they shifted by 4 after line ~3800 between reads).

---

## 0. In plain words

- **A symmetric stress tensor exists for R8-1's interacting d = 2 law (proved, construction).** I build T⁰⁰ explicitly. Its total is H, and its energy dipole is exactly R8-1's interacting boost K, spin term included. I then build an energy current and a symmetric momentum flux by a division lemma (Lemma KB, §2). The lemma says when a symmetric flux can exist: the momentum current's angular moment must be conserved. It is satisfied once the momentum density's angular moment is the true angular momentum J, so spin included. Arranging that is the Belinfante step.
- **Where the Belinfante term sits.** In the explicit box-sector form, the momentum density is "energy × velocity" plus half the curl of a spin density SM/(2H) (plain Belinfante). Without the curl, a bound body at rest carries none of its spin in its momentum density. Checked: J_T/S = 0.005–0.010 without it, and 0.999999999999 with it.
- **Scope, the same as R9-2's refereed d = 1 result.**
  - Energy conservation (ν = 0) is exact on all two-particle states.
  - Momentum conservation (ν = i) with a symmetric flux is exact between box-sector states. A source sits only off the box sector: in R8-1's transition shell, and in a torque term in the same region.
- **Spinning bound bodies fall universally (proved; checked).** In a uniform field the centre of energy of every box-sector state accelerates at exactly −g + 2(g·V)V at linear order, whatever its binding, spin or velocity. Checked for the bound doublet (S = +1 and −1) at binding fractions 0.05, 0.15 and 0.30, at rest and moving at a common V = (0.28, 0.11):
  - residual against the formula ≤ 1.3e-14 for all 12 bodies;
  - raw Eötvös η between binding fractions ≤ 4.7e-15 at rest and ≤ 1.5e-14 moving;
  - spin η (S = +1 vs −1) ≤ 3.1e-15.

  That is the double-precision floor. The proved value is 0.
- **Comparator: if binding energy does not gravitate**, η = 0.16–0.46.
- **The spin couplings take the elevator (special-relativity-in-a-uniform-field) values, checked.**
  - Lapse spin–orbit energy: the stress's dipole gives exactly the Thomas/BT term ε_ab g_a P_b S/(M + H). Ratio 0.999999999999. At low velocity this is ½ (g × V) S.
  - Gravitomagnetic ratio (spin's coupling to a uniform rotation, relative to orbital): 0.999999999999.
  - The spin-dependent sideways "hidden-momentum" drift of the centre of energy equals the elevator value to 10 digits. Without the spin term in the dipole it is half that.
- **Spin does not enter the fall at linear order.** Dropping the spin term from the energy dipole leaves Ẍ_E unchanged (checked). In 2+1 dimensions spin is a conserved scalar here. So a MICROSCOPE-type test of these bodies at O(g) does not probe the Belinfante term. Only the spin couplings above do.
- **What is not shown.**
  - GR's curved-field geodetic coupling (the 3/2 factor) is not computed. "GR value" here means the uniform-field values, which GR shares with special relativity (reading). Also, linearized 2+1 GR has no Newtonian field of a mass (RECALLED).
  - The global lattice stress is proved to exist. Its T⁰⁰ is explicit, but its currents come from a division and were not evaluated numerically on the lattice. The numerics use R8-1's canonical chart.
  - N ≥ 3, d = 3 and loops are outside the class.

**Against the FIXED readings (`TESTS.md:3882-3885`): worker reading PASS WITH SCOPE (d = 2, two-body, box-to-box, uniform fields, linear order).**
- If the referee requires either of the following, the reading is **INCONCLUSIVE**:
  - a lattice-native numerical construction of the global T^{0i} and T^{ij} (the d = 2 lattice-native run is resolution-limited, as in R8-1);
  - GR's curved-field geodetic coupling, rather than the uniform-field couplings.
- **FAIL is not available.** §3 is an explicit construction in the stated class.

---

## 1. Hypotheses and class (stated before any title)

- **H-law.** R8-1's d = 2 interacting two-body box law (`C5_R8-1_report.md:118-134`; referee CWC, PASS WITH SCOPE, `C5_R8-1_referee_verdict.md:1-3,15-20,35-36`).
  - One CAR mode per site of Z², graded composition, continuous time; two-particle sector.
  - Mass operator M = M₀ + λΣ_a|g_a⟩⟨g_a|, with g_a = q_a b(|q|²), the p-wave doublet; m = 0.5, κ = 0.8.
  - H = H₀ + cW₁, where W₁ = √(M² + P²) − √(M₀² + P²) and c is the plateau.
  - K_a = K₀,a + ½{cW₁, X_NW,a} + ε_ab P_b ½{S, cF}, with F = f(M) − f(M₀) and f(M) = 1/(M + √(M² + P²)) (`:134`). J = J₀.
  - On the box sector (c = 1): H = √(M² + P²), J = X_NW × P + S, K_a = ½{H, X_NW,a} + ε_ab P_b S/(M + H) (`:122-124`).
- **H-free.** The free stress is R8-2's Construction A, T_A (`C5_R8-2_report.md:73-94`; confirmed `C5_R8-2_referee_verdict.md:5-21`). Its first moment is ½{X, ε} per leg, so K₀ summed. D(Q) is R8-2's generalized forward difference: D = Q for |Q_i| ≤ 1, zero only at Q = 0, D(q)* = −D(−q).
- **Conventions.** T(Q) raises the total lattice momentum by Q. With T(Q) = Σ_x e^{iQ·x}T(x):
  - continuity reads [H, T^{0ν}(Q)] = Σ_j D_j(Q_j) T^{jν}(Q);
  - first moment = −i∂_Q T(Q)|₀;
  - Hermiticity: T(Q)† = T(−Q).
  - X = i∇_P with [X_a, P_b] = iδ_ab, so e^{iQ·X} shifts P by +Q. ε_xy = +1. R8-1's measured conventions apply: [K_x, K_y] = −iJ.
- **H-box.** "Box-to-box" means matrix elements ⟨φ|·|ψ⟩ with φ and ψ in R8-1's common domain 𝒟₂: |P| < Π₁, legs in the box, no umklapp (`C5_R8-1_report.md:64`). The box set is convex in P at fixed relative data. This is the scope the R9-2 referee fixed: P_B s P_B = 0 (`ref_R9-2/REFEREE_VERDICT.md:7`).
- **H-grav.**
  - Uniform static lapse: H_g = H + g·D₁, where D₁ is the first moment of T⁰⁰.
  - Uniform gravitomagnetic field (rigid rotation, h_0i = (Ω × x)_i): H_Ω = H − Ω J_T, with J_T = ε_ab ∫x_a T^{0b}.
  - Linear order is O(g) and O(Ω).
- **Excluded, not addressed:**
  - N ≥ 3 (R9-3);
  - d = 3 (R9-6);
  - pair creation and loops (R8-4, R7-5, R9-7);
  - gauge fields (R8-5);
  - graviton dynamics (R9-9);
  - local (non-uniform) lapse and tidal fields (second moments);
  - curved h_ij (the geodetic factor);
  - ungraded ⊗M₂.
- **Outside realizations not excluded.** The stress is not unique: improvements with vanishing zeroth and first moments are free. Every observable used here depends only on ∫T⁰⁰ = H, on the dipole D₁ = K and on J_T. All realizations sharing these give identical results (proved: H_g and H_Ω depend on T only through them).

## 2. Prior art (each counted once)

- **R9-2** (d = 1; referee CWC, PASS WITH SCOPE d = 1 only; `ref_R9-2/REFEREE_VERDICT.md:1-20`):
  - Weyl-midpoint interaction density;
  - exact ν = 0 identity;
  - ν = 1 identity box-to-box, with a shell source;
  - Ẍ_E = −g(1 − 2V²);
  - R7-4 escape: global source-free momentum conservation is the missing hypothesis (`:17`).

  R9-2 §7 named the d = 2 route (improvement densities for εP½{S, cF}, plus "a Belinfante-type step … not checked", `R9-2_report.md:271`). This report carries it out.
- **R8-1** (the law, K, J, the spin coefficient α = +1, global self-adjoint K; `C5_R8-1_report.md:118-146`; referee `:15-23`).
- **R8-2** (Construction A, D, Lemma U, Theorem E; `C5_R8-2_report.md:73-124`).
- **Block 138**, `docs/ADMISSIBILITY_RULE_THE_COINS_SPIN_ENTERS_THE_SOURCE_LINK_THROUGH_ITS_CURL_..._2026-09-25.md` (claim scope, lines 1–15). A lattice Belinfante identity, "symmetric momentum = canonical momentum + ½ curl of the spin", for block 54's coin walk on Z³. It is the same mechanism in a different law (no box, no BT). Counted once here.
- **RN-L1** (`agents/RN_L1_report.md:58`). The suggested module criterion: "a symmetric T exists if a local spin density exists". Lemma KB below is a proved 2D version, for operator-valued symbols with the D of R8-2.
- **RN-L2** (`TESTS.md:857-858`). No conserved quasi-local momentum for nearest-neighbour KG or tight-binding bands with scattering in d ≥ 2. The hypotheses differ: the band here is non-analytic and exactly relativistic in the box, the momentum is the exactly additive box momentum (R6-1/R7-1), and conservation is claimed only box-to-box.
- **Literature.**
  - Lev, Pace and Salmè, *Electromagnetic and weak current operators for interacting systems within the front-form dynamics*, hep-ph/9807255 (abstract verified by web search this run: currents must commute properly with the Poincaré generators and be Hermitian).
  - Lev, hep-ph/9403222 (exact construction of a conserved, cluster-separable EM current for relativistic composites via Sokolov packing; abstract verified).
  - The point-form BT current work of Biernat, Klink and Schweiger (arXiv 1011.00170 and 1404.2440; verified, they report spurious BT cluster contributions to currents).

  These are comparators only; the construction below is direct. Polyzou's relativistic-current-operator slides were found, with commutator constraints for covariance and conservation; content not read in full.
- **Belinfante (1940) / Rosenfeld (1940)** symmetrization: RECALLED, comparator.
- **Kobzarev–Okun** (JETP 16 (1963) 1343): no anomalous gravitomagnetic moment. Citation verified via Obukhov gr-qc/0112080; content RECALLED, comparator.

---

## 2b. Lemma KB (two-dimensional Koszul–Belinfante division): proved

**Statement.** Let R^i(Q), i = 1, 2, be C^∞ (resp. Gevrey-s) functions on T², valued in operators (kernels) on the two-particle space. Suppose:
- (i) R(0) = 0;
- (ii) τ := ε_ab ∂_a R^b(0) = 0;
- (iii) R^i(Q)† = −R^i(−Q).

Then there is a C^∞ (resp. Gevrey-max(s, 2)) symmetric T^{ij}(Q) with T^{ij}(Q)† = T^{ij}(−Q) and Σ_j D_j(Q_j) T^{ji}(Q) = R^i(Q).

(i) and (ii) are also necessary. Given a symmetric smooth T, R(0) = D(0)·T(0) = 0, and ε_ab ∂_a R^b(0) = ε_ab T^{ab}(0) = 0, since D = Q near 0.

If P_B R(Q) P_B = 0 for all Q (box-to-box, in the Weyl-midpoint labelling), T can be chosen with P_B T P_B = 0.

**Proof.**
- **Far from 0.** Set a_j := D̄_j/Σ_k|D_k|², so that Σ_j a_j D_j = 1. Then
  T_far := R aᵀ + a Rᵀ − (Σ_k R^k D_k) a aᵀ
  is symmetric and satisfies T_far·D = R. It is smooth wherever D ≠ 0, i.e. away from Q = 0.
- **Near 0** (where D = Q). By Hadamard, R^i = Q_j A^{ji}(Q), with A^{ji}(Q) = ∫₀¹ ∂_j R^i(tQ) dt.
  - Split A = A_s + αε. Then α(0) = ½τ = 0, so α = Q_k β_k (Hadamard again).
  - Y^{ji} := −(β_j ε^{ik} + β_i ε^{jk}) Q_k is symmetric, and Q_j Y^{ji} = −(Q·β) ε^{ik} Q_k = α Q_j ε^{ji}.
  - So T_near := A_s + Y is symmetric with Q_j T_near^{ji} = R^i. This is the Belinfante step: the antisymmetric part becomes a divergence of a curl.
- **Glue and Hermitize.** T = ζ T_near + (1 − ζ) T_far, with ζ a Gevrey-2 cutoff supported in |Q_i| < 1. Then T → ½(T(Q) + T(−Q)†). This keeps the identity because D(Q)* = −D(−Q) and (iii).
- **Box-to-box.** Hadamard integrals use R(tQ) at the same midpoint P̄, with P̄ ± tQ/2 in the convex box set. The far formula is pointwise. So P_B T P_B = 0 is inherited. ∎

**Meaning.** A symmetric momentum flux exists iff the momentum current's angular moment J_T := ε_ab(−i∂_a)T^{b0}|₀ is conserved, up to the allowed source torque. (Since R^b = [H, T^{0b}] − s^b, condition (ii) reads [H, J_T] = torque of s.)

---

## 3. The construction

### 3.1 T⁰⁰ with ∫T⁰⁰ = H and dipole K, globally (proved)

T⁰⁰ := T⁰⁰_A + T⁰⁰_I, where

  T⁰⁰_I(Q) := e^{iQ·X_NW/2} χ(Q) [ cW₁ + i Q_a B_a ](P̄) e^{iQ·X_NW/2},  with B_a := ε_ab P_b ½{S, cF}.

- **Well defined.** X_NW = i∇_P|_q in R8-1's canonical chart, so the Weyl factors shift P at fixed q.
  - All interaction kernels are supported in supp g × supp g (referee lemma f(M) − f(M₀) = Q_G[·]Q_G, `C5_R8-1_referee_verdict.md:26-28`) and in |P̄| < Π₂.
  - χ cuts at |Q| ≤ 2. All momenta involved then have legs inside the exact box (|k| ≲ 0.8 + 1.1 < B = 2.6), where the chart holds (R8-1 chart identity to 1e-14).
- **Moments (proved).**
  - ∫T⁰⁰ = H₀ + cW₁ = H.
  - −i∂_Q T⁰⁰|₀ = K₀ + ½{X_NW, cW₁} + B = K. This uses R8-1's lattice-native form `:134`.
  - Both are exact operator identities on all two-particle states.
- **Hermitian.** cW₁ and B_a are Hermitian, and χ is real and even. **Translation covariant**, since the Weyl density uses momentum shifts.
- **Quasi-local.**
  - Gevrey-2 in Q, from χ and the sstep cutoffs.
  - In the relative coordinate, quasi-local through the compact q-support of every interaction kernel.
  - X_NW is the pair's centre of energy corrected by a relative-local spin term.

### 3.2 Energy current: exact on all states, with J_T = J box-to-box (proved)

T^{j0} := T^{j0}_A + C^j, where Σ_j D_j C^j = N(Q) := [H, T⁰⁰(Q)] − [H₀, T⁰⁰_A(Q)] = [cW₁, T⁰⁰_A] + [H, T⁰⁰_I].

- **Existence.** N(0) = [cW₁, H₀] + [H, cW₁] = 0, so a smooth solution C⁽⁰⁾ exists. Use the scalar version of §2b: far, a_j N; near, Hadamard. Then ∫T^{j0} = J′_j := i[H, K_j]. On 𝒟₂ this equals P_j, by R8-1's algebra.
- **Belinfante fix (the transverse freedom).** Add −i ε^{jk} D_k(Q) σ(Q). It is divergence-free identically, since Σ_j D_j ε^{jk} D_k = 0. Its angular moment is 2σ(0).
  - Choose σ := the Weyl(X_NW) density of Σ_C := −½(J_T[C⁽⁰⁾] − ε_ab ½{X_NW,a, C⁽⁰⁾b(0)}). This combination is translation-invariant.
  - Then J_T = J_T,A + ε_ab ½{X_NW,a, C⁽⁰⁾b(0)}.
- **The angular moment.** J_T,A := Σ_legs ε_ab ½{X_a, ε∂_bε}.
  - (a) It equals J₀ = J on legs in the box (p = k there).
  - (b) [H₀, J_T,A] = 0 globally (proved: Σ ε_ab ∂_aε · ε∂_bε = 0).
  - (c) [cW₁, J_T,A] = 0, because W₁ is rotation-invariant (p-wave doublet, `C5_R8-1_report.md:197`).
  - C⁽⁰⁾(0) = J′ − J_E vanishes on 𝒟₂ (both equal P there), and X_NW preserves P-support. **So J_T = J box-to-box.**

### 3.3 Symmetric momentum flux: exact box-to-box, sources off it (proved)

R^i(Q) := [H, T^{0i}(Q)] − s^i(Q), with s = s₁ + s₂:
- s₁ = the Weyl(X_NW) density of [H, J′_i]. This is R9-2's source. It is supported in the transition shell and the interaction region, since [H, J′] = [H, J′ − J_E] and [H, J_E] = [cW₁, P] = 0 on legs in the box.
- s₂ = −i ε^{ik} D_k × (the Weyl density of ½τ₀), with τ₀ := [H, J_T] − ε_ab ½{X_NW,a, [H, J′_b]}. This is a pure torque source with zero integral.
- **Box-to-box (proved).**
  - [H, J′]ψ = 0 on 𝒟₂.
  - [H, J_T] = [H, J] = 0 on 𝒟₂ (R8-1).
  - X_NW preserves 𝒟₂.
  - So P_B s P_B = 0.
- **Hypotheses of Lemma KB.** R(0) = 0 and the torque condition (ii) hold by construction, and (iii) holds. So a symmetric, Hermitian, Gevrey-quasi-local T^{ij} exists with Σ_j D_j T^{ji} = [H, T^{0i}] − s^i.

**Result (proved; construction plus Lemma KB).** T^{μν} is symmetric, Hermitian, translation covariant and quasi-local, and:
- ν = 0 is exact on all two-particle states;
- ν = i is exact box-to-box;
- ∫T⁰⁰ = H, first moment = K (global);
- J_T = J (box-to-box).

The sources live only where R8-1's law is switched off (the shell) or in the interaction region off 𝒟₂. This is R9-2's price, now including a torque.

### 3.4 Explicit box-sector form, used for the numbers (proved algebra; checked)

On 𝒟₂ all of H, S, M and f commute (`[S, M] = 0`). That allows a closed form in R8-1's chart:

- T⁰⁰(Q) = e^{iQX/2} 𝒯 e^{iQX/2}, with 𝒯 = H(P̄) + i Q_a ε_ab P̄_b S f(P̄)
- T^{b0}(Q) = e^{iQX/2} [𝒯Δ_b − i Σ ε_bk Q_k] e^{iQX/2}, with **Σ = S M/(2H) (the Belinfante curl)**
- T^{ij}(Q) = e^{iQX/2} [𝒯Δ_iΔ_j − i Σ (Δ_i ε_jk + Δ_j ε_ik) Q_k] e^{iQX/2}

Here Δ_b is the staircase-symmetrized divided difference of h = √(μ² + P²), even in Q, with Σ_b Q_b Δ_b = h(P̄ + Q/2) − h(P̄ − Q/2) =: ω (telescoping, as R8-2's dust kernel).

**Proofs (algebra).**
- ν = 0: Σ_b Q_b T^{b0} = 𝒯ω + 0 = [H, T⁰⁰].
- ν = i: ω𝒯Δ_i = Σ_j Q_j(𝒯Δ_jΔ_i), and ω ε_ik Q_k Σ = Σ_j Q_j Σ(Δ_j ε_ik + Δ_i ε_jk) Q_k, because Q_j ε_jk Q_k = 0.
- Dipole: K.
- J_T = X×P + S(H − M)/H (dust part) + S M/H (curl) = X×P + S = J.

**Caveat on locality (reading, important).** The free part of this closed form (Δ and 𝒯 with M = M₀) is diagonal in the relative momentum q. It assigns a separated free pair's energy to its centre of energy, so it is **not relative-quasi-local on scattering states**. It is a box-sector model with the right moments, used to check the moments, the Ward algebra and the Belinfante coefficient. The quasi-local stress is §3.1–3.3: constituent T_A for the free part, interaction densities for the rest.

**Same observables (proved).** Both realizations have ∫T⁰⁰ = H, D₁ = K and J_T = J on 𝒟₂. §§4–5 depend only on these.

Suggested, not proved: on box-to-box elements the §3.3 interaction current can be taken as the composite difference [closed form at M] − [closed form at M₀], plus the division of [W, T_A − T_comp(M₀)]. The latter is O(Q²) at Q = 0, with zero angular moment because its second-order coefficient is symmetric. On that reading the Belinfante curl carried by the interaction is ½S(M/H − M₀/H₀).

### 3.5 Checks of §3.4 (`r910_belinfante_d2.out:1-25`)

**Setup.**
- R8-1's chart representation: spectral P-grid 64², window ±1; polar q-grid 40 × 16; the joint (M, S) eigenbasis. M is block-diagonal in l to 6.1e-15.
- Bound masses 0.9499882908, 0.8499777351 and 0.6999622357 (R8-1's 0.8499777351 reproduced).
- Packets: the bound doublet S = ±1 plus a continuum admixture in l = 0, ±1, ±2, at rest and moving.
- K and J are R8-1's formulas, independent of the stress.

| check | result |
|---|---|
| T⁰⁰(0) = H | 5.5e-16 – 6.0e-16 |
| first moment −i∂_QT⁰⁰ (8th-order FD) vs K_x, K_y | 4.1e-12 (spin-term share of K: 5.7e-3 – 8.9e-3, so resolved) |
| ∫T^{b0} = P_b | ≤ 2.1e-15 |
| J_T (FD) vs J (Belinfante) | 5.1e-12 – 7.0e-12; ⟨J_T⟩ = ⟨J⟩ to 1e-12 |
| J_T without the curl (dust comparator) | ⟨J_T⟩ = 0.0031 against ⟨J⟩ = 0.5318 (rest, S = +1 mix) |
| ν = 0 Ward identity at Q = (0.13, −0.07), (−0.21, 0.17) | 1.7e-14 – 3.0e-11 relative |
| ν = x, y Ward identity | ≤ 9.7e-13 absolute, against scale 1.5e-2 – 4.7e-2 |
| symmetry T^{xy} − T^{yx} | ≤ 3.3e-16 |
| Hermiticity T(Q)† = T(−Q) (T⁰⁰, T^{0x}, T^{xy}) | ≤ 2.7e-15 |

The 3.0e-11 is the one moving-packet case. It is consistent with band-limited shift interpolation of the mixed packet; the identities are exact algebra.

---

## 4. Fall of spinning bound bodies (proved; checked)

### 4.1 Theorem (box sector, linear order)

Take H_g = H + g·K, X_E := ⟨K⟩/⟨H⟩ and V := ⟨P⟩/⟨H⟩. On 𝒟₂, R8-1's algebra holds: [K_a, P_b] = iδ_ab H, [K_a, H] = iP_a, [K_x, K_y] = −iJ, [J, K_a] = iε_ab K_b. So:
- d⟨P⟩/dt = −g⟨H⟩ and d⟨H⟩/dt = −g·⟨P⟩;
- d⟨K_b⟩/dt = ⟨P_b⟩ + ε_ab g_a⟨J⟩ and d⟨J⟩/dt = O(g).

Therefore:
- **Ẍ_E = −g + 2(g·V)V + O(g²).** It is independent of binding, spin and internal state (proved).
- **Ẋ_E = V + [ε_ab g_a ⟨J⟩ + ⟨K_b⟩(g·⟨P⟩)/⟨H⟩]/⟨H⟩ + O(g²).** This is a spin-dependent sideways drift: velocity without momentum (hidden momentum).

### 4.2 Checks

`r910_belinfante_d2.out:26-129`. The expectations of nested commutators are evaluated from operator actions, not from the algebra.

| body (f_B = 0.05, 0.15, 0.30; S = ±1) | residual of Ẍ_E/g against −e_x + 2V_xV | w_P − 1 |
|---|---|---|
| at rest (12 bodies) | ≤ 5.3e-15 | ≤ 4.7e-15 |
| moving, V = (0.28, 0.11) matched to ≤ 2.3e-16 | ≤ 1.3e-14 | ≤ 1.6e-15 |

- **Raw Eötvös η = |a₁ − a₂|/|a| at equal V.**
  - Between binding fractions: 2.5e-15 – 4.7e-15 at rest and 2.0e-15 – 1.5e-14 moving (`:76-87`).
  - Between S = +1 and −1: ≤ 3.1e-15 (`:88-93`).
  - These numbers are at the double-precision floor of the commutator evaluation. The 1e-15 bar is met by the proved zero, not resolved numerically. This follows the R9-2 referee's point 4 (`ref_R9-2/REFEREE_VERDICT.md:11`).
- **Comparators.**
  - D₁ = K₀ (binding energy does not gravitate): η = 0.160, 0.439 and 0.241 at rest, and 0.167, 0.457 and 0.248 moving. Weights w_P = 1.27, 1.47 and 1.82 (`:28,:112-123`).
  - D₁ = ½{H, X_NW}, i.e. the spin term omitted from the energy dipole: Ẍ_E is unchanged at the floor (`:94-111`). **Spin does not enter the O(g) fall.**
- **Hidden-momentum drift.** At rest, S = ±1, f_B = 0.05, the O(g) Ẋ_E is (0, ±1.046990298) = ε g J/H (`:29,:33`). Moving, it equals the full elevator formula to 10 digits (`:37,:53,:69`). The spin-omitted comparator gives exactly half (0.5234951).

---

## 5. Spin couplings against GR (checked; GR identification is a reading)

- **(a) Lapse spin–orbit.** E_SO := ⟨g·D₁⟩(S=+1) − ⟨g·D₁⟩(S=−1), with D₁ the FD dipole of T⁰⁰ (not K), for bodies at X = 0 moving with P₀ = M_b(0.30, 0.12).
  - E_SO = 0.116468704205, 0.116334325937 and 0.116017398704, against the BT/elevator value 2⟨P_y f⟩.
  - Ratio 0.999999999999 for all three (`:130-133`).
  - The low-velocity form ½(g × V)·2 = V_y = 0.1137 shows the expected γ-factor excess.
  - Comparator (spin term omitted): E_SO = 0.
- **(b) Gravitomagnetic ratio.** A uniform rotation couples as −ΩJ_T. ⟨J_T⟩/⟨S⟩ = 0.999999999999 at rest, for all binding fractions and both S (`:134-140`). Dust comparator: 0.0053, 0.0066 and 0.0097, i.e. ≈ ⟨1 − M/H⟩.
- **(c) The GR value (reading, elementary; comparator RECALLED).**
  - A uniform static lapse and a uniform rotation are flat at linear order (zero linearized Riemann).
  - GR's linear couplings there are those of special relativity in an accelerated or rotating frame: H + g·K and H − Ω·J. K's spin term is fixed with coefficient +1 by [K_x, K_y] = −iJ (R8-1, referee-confirmed `C5_R8-1_referee_verdict.md:15-20`).
  - So (a) and (b) are GR's values in these fields: the Thomas term, and gravitomagnetic ratio 1, the absence of an anomalous gravitomagnetic moment (Kobzarev–Okun, RECALLED).
- **Not checked.**
  - The curved-field spin–orbit (geodetic, 3/2 in 3+1 GR). It needs the dipole of T^{ij} against a curved h_ij. By Dixon/Mathisson–Papapetrou universality (RECALLED, comparator), any symmetric conserved T with these moments gives GR's dipole-order coupling, but that is not computed here.
  - In 2+1 GR a point mass makes no Newtonian or geodetic field (Deser–Jackiw–'t Hooft, RECALLED). So a "GR value" for d = 2 exists only for supplied external fields.

---

## 6. R7-4 and the edge

- **R7-4's conditional exclusion.** As in R9-2 (referee item 7), the missing hypothesis is global source-free momentum conservation. Here the ν = i identity has the shell source s₁ and the torque source s₂, both off 𝒟₂.
  - K is globally self-adjoint (R8-1).
  - Møller intertwining is not examined. R9-10 lies outside R7-4's no-go, not against it.
- **Edge.** T_A is R8-2's universal box⊕edge stress, so edge energy gravitates. Theorem E's wrong-way fall of edge quanta stands (`C5_R8-2_referee_verdict.md:31-47`). It is unchanged here, because the bodies are box-sector states.

## 7. Prices (named, not adopted)

- **P-W2 (extends R9-2's P-W).** Linearized gauge invariance (the momentum Ward identity with a symmetric flux) is exact only box-to-box. The sources are at lattice-scale total momentum (the shell, Π₁ < |P̄| < Π₂ in units of 1/a) and include a torque source.
- **Inherited:**
  - non-quasi-analytic band and kernels;
  - the frame-fixed box;
  - form-factor (invariant-mass) interactions;
  - graded fermions;
  - R8-2's edge (Theorem E) and Lemma U;
  - BT's N ≥ 3 cluster problem (R9-3).
- **No axiom text changes.** Admissibility supplies no dynamics or stress (`AX:116-123`). Source/action and physical-observable identification are outside the axioms (`AX:187`).

## 8. Scope and strong-word check

- **"Exact"** is used only for:
  - ∫T⁰⁰ = H and dipole = K (operator identities on all two-particle states);
  - ν = 0 (all states);
  - ν = i and J_T = J (box-to-box);
  - Ẍ_E = −g + 2(g·V)V at O(g) on 𝒟₂;
  - the §3.4 algebra.
- **"Proved"** for §3.2–3.3 is the construction plus Lemma KB. The division step is constructive but not evaluated on the lattice. Its Gevrey class is inherited from the cutoffs (proof sketch level, as R9-2's Hadamard step).
- **"Checked"** numbers are in R8-1's canonical chart on the box sector, where the lattice free generators equal the BT ones to 1e-14 (R8-1, referee-confirmed). As in R8-1, a lattice-native d = 2 run was not attempted; R8-1 found it resolution-limited.
- **"Spin coupling equal to GR's"** means the uniform-lapse and uniform-rotation couplings (§5(c)), not the curved-field geodetic one.
- **"η below 1e-15"** rests on the proof. The numerics agree to 1.5e-14 (floor).
- **Two-body, d = 2, linear order, uniform fields only.**

## 9. For the referee

1. Lemma KB: the near-zero symmetric Y^{ji} = −(β_jε^{ik} + β_iε^{jk})Q_k; the necessity of (ii); Hermitization with D(Q)* = −D(−Q); box-to-box inheritance via convexity.
2. §3.1: dipole of T⁰⁰_I = ½{X_NW, cW₁} + εP½{S, cF}, so the total is K by R8-1 `:134`.
3. §3.2: the Belinfante fix σ, and J_T = J box-to-box. In particular [H₀, J_T,A] = 0 globally and [cW₁, J_T,A] = 0.
4. §3.3: the torque source s₂, and P_B s P_B = 0.
5. §3.4 closed form and the locality caveat: the closed form is a box-sector model, not the quasi-local stress.
6. Whether d = 2 PASS WITH SCOPE is met by an existence construction for T^{0i} and T^{ij}, with explicit T⁰⁰ and an explicit, numerically checked box-sector form with identical moments.
7. Whether the uniform-field (elevator) couplings meet "spin coupling equal to GR's".

Runtime: `r910_belinfante_d2.py` takes about 230 s at OMP_NUM_THREADS = 2.

**Sources (web-verified this run):**
- [Lev, Pace, Salmè hep-ph/9807255](https://www.arxiv.org/abs/hep-ph/9807255)
- [Lev hep-ph/9403222](https://ar5iv.labs.arxiv.org/html/hep-ph/9403222)
- [Biernat–Klink–Schweiger 1011.00170](https://arxiv.org/pdf/1011.00170.pdf)
- [Biernat–Schweiger 1404.2440](https://arxiv.org/pdf/1404.2440v1)
- [Polyzou et al., relativistic current operators (slides)](https://indico.him.uni-mainz.de/event/150/contributions/1245/attachments/734/1113/mainz_12.pdf)
- [Obukhov gr-qc/0112080 (cites Kobzarev–Okun)](https://arxiv.org/pdf/gr-qc/0112080)
