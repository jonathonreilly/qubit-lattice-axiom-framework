# C5 R9-6 report: the d = 3 rotation-multiplet box law (p-wave triplet, spin term (P × S)/(M + H), cube vs ball)

**Author.** Claude Opus 5.5 probe (same family as the supervisor, R7-1's and R8-1's workers and every C5 worker). Unrefereed. 2026-10-12, 17:29Z to 18:00Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R9-6/`. Scripts and outputs in `S/scripts/`:
- `r81_common.py` (copied unchanged from R8-1: smooth steps, R7-1 box band, Woodbury BT kernel);
- `r96_d3_chart_algebra.{py}` with `_NP40_repaired.out` (main), `_NP28.out` (comparators, same packet rule), `_NP28_s0.09.{out,log}` (first run, narrower packet, resolution-limited);
- `r96_d3_lattice_mass.py` with `_L48/_L64/_L96/_L128/_L192.out` (probe b), `_L96/_L128_Pi1.80_2.20_B1.60_B2_3.0.out`, `_L96/_L128_Pi2.00_2.40_B1.60_B2_2.4_scan.out` (probe d stress test), `_B2_2.00` files (first stress-test version, superseded: band bends too fast, see §4.5);
- `r96_rotation_leak.{py,out}` (probe c, rotations); `r96_rotation_leak_dtcheck.{py,out}` and `r96_rotation_charcheck.{py,out}` (integrator floors); two superseded logs (`_firstrun_overlapfloor.log`, `_secondrun_partial.log`; see §4.3);
- `r96_leak_d3.py` with `_NP640.out`, `_NP960.out` (probe c, interacting boosts in d = 3);
- `r96_geometry.{py,out}` (leg geometry, invariant domain, budgets).

**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full. `TESTS.md:2302-2320` (C5 method, readings), `:3240-3260` (R7-1 registration), `:3396-3460` (R7-1 referee results, R8 registration), `:3575-3600` (Round 9 rules and overlap), `:3765-3790` (**R9-6 registration**), `:3793-3804` (R8-1 referee results). `agents/C5_R8-1_report.md` in full; `agents/C5_R8-1_referee_verdict.md` in full; `agents/C5_R7-1_report.md:1-200`; `agents/C5_R7-1_referee_verdict.md:90-180`. R8-1 scripts `r81_common.py`, `r81_d2_chart_algebra.{py,out}`, `r81_d2_lattice_mass.py` + `_L192.out`, `r81_leak.py`.
**Prior-art grep** (packet + `docs/` + `scripts/`, for "inscribed ball", "rotation budget", "p-wave triplet", "(P × S)"): the only hits are the R9-6 registration itself (`TESTS.md:3771-3788`, verbatim from `agents/C5_S8_synthesis.md:510-527`) and R8-1's one-line suggestion (`C5_R8-1_report.md:38,127,279`; `r81_d2_chart_algebra.py:9`). `scripts/R3_c1_window_boundary_lemma.py:88` uses "inscribed ball" for an unrelated window lemma. Counted once each.
**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED.

---

## 0. In plain words

- **The d = 3 interacting two-body box law closes.** With the p-wave triplet g_a(q) = q_a b(|q|²), a = 1..3, and the boost K = ½{H, X_NW} + (P × S)/(M + H), all 45 commutators of the ten generators {H, P_a, J_a, K_a} close in the canonical chart.
  - Proved: the spin coefficient must be +1. In d = 3 there is an extra S × S cross term that d = 2 does not have; it requires α² = α, and the d = 2 condition requires α(2Hf − P²f²) = α = 1. Both hold only at α = 1.
  - Checked: the 45 commutators close to ≤ 1.5e-10. The residual falls with the P-grid resolution, from 3.9e-4 to 5.5e-7 to 1.5e-10. The lattice's free two-body generators equal the BT free generators, spin term included, to 2e-14 at 12 random chart points.
  - Comparators fail at O(10⁻²–1):
    - the printed sign;
    - no spin term;
    - α = −1;
    - one g_z channel;
    - R8-1's d = 2 doublet carried into d = 3.
- **On the lattice the bound triplet has one invariant mass at every P and in every direction.** Its spread over axes, face diagonals, body diagonals and generic directions is 4.2e-4, 6.6e-5, 3.0e-6, 2.5e-7 and 4.0e-9 at L = 48, 64, 96, 128 and 192. The triplet stays degenerate to 2.5e-9 at L = 192. The Galilean comparator drifts by 0.094 (checked).
- **Rotations: on the ball the budget is unlimited, exactly; on the cube it is finite.**
  - Proved: each lattice rotation generator J0_n commutes with the full interacting H everywhere on the lattice, for every n and every particle number.
  - Proved: the "ball sector", in which every particle's momentum lies in the inscribed ball |k| < B, reduces H, P and J. On it the lattice rotations are the exact rotation group, for all angles and axes.
  - Corner states of the cube rotate exactly only until a particle's orbit hits a face. The rotation leakage bound ‖e^{−iθJ_n}ψ − U(R_θ)ψ‖ ≤ 2‖1_{E_θ}ψ‖ is proved and checked.
- **Boosts leak in both cases (proved; checked).**
  - The interacting leakage theorem (R8-1's Theorem L) carries over to d = 3. The Wigner rotation from the spin term preserves |q|, and the q-support set is rotation invariant. Checked with P_⊥ ≠ 0: the difference sits at the discretisation floor (6e-8, falling 20× from NP = 640 to 960) until the predicted η* = 0.317, and stays under the bound after.
  - The free boost budget of a particle at rest is direction dependent for the cube: asinh(B/(m max_a|n_a|)), so a body-diagonal boost gets about 0.54 more rapidity than an axis boost (tending to ln√3 = 0.549 for m ≪ B). For the ball it is isotropic.
- **The cube anisotropy of the bound state is zero for the registered law.** Wherever the interaction is on, its legs stay within |k| ≤ 1.548, well inside the inscribed ball (B = 2.6). A stress test that shrinks the exact cube to B = 1.6 (outside the registered law) shows what the cube would do. Along an axis the invariant mass leaves 0.85 from about |P| ≈ 1.6. Along face and body diagonals it stays at 0.85 to ≤ 4e-7 (L = 128) up to |P| ≈ 2.0 (checked).
- **Against the FIXED readings:**
  - (a) closes to a stated tolerance (1.5e-10, chart);
  - (b) the mass is P- and direction-independent to converging precision;
  - (c) the leakage bounds for rotations and boosts are proved and checked.

  Worker reading: **PASS**, referee required. Same caveat as R8-1: no direct lattice-native run of the 45 commutators in d = 3 (§5).

---

## 1. Hypotheses and classes (stated before any title)

- **H-lat (as R7-1/R8-1).**
  - One complex fermion mode per site of Z³, with the graded tensor product.
  - The one-site algebra is M₂(C) (`MINIMAL_AXIOMS_2026-06-29.md:47`). Cross-site composition is graded, as R7-1's PASS clause allows (`TESTS.md:3253`).
  - Continuous time.
  - The one-body law: s(k) = k and ε̃ = √(m² + |k|²) on the cube |k_a| ≤ B = 2.6, extended smoothly and periodically (`r81_common.py:25-33`, B₂ = 3.0). m = 0.5.
- **H-2.** The interacting statements concern the **two-particle sector**. N ≥ 3 is R9-3's item and is not claimed here, except where stated "every N" (rotations, §4.3).
- **H-int (d = 3).**
  - M = M₀ + λ Σ_{a=1..3} |g_a⟩⟨g_a|, with g_a = q_a b(|q|²) and b = sstep(1 − |q|²/κ²)/κ, κ = 0.8.
  - λ is tuned so that M_b = 0.85, the triplet bound mass.
  - Plateau: c(|P|) = 1 for |P| ≤ Π₁ = 0.6 and 0 for |P| ≥ Π₂ = 1.2.
  - W(P) = c[√(M² + P²) − √(M₀² + P²)] in the canonical chart (P, q), with the exact Woodbury kernel (`r81_common.py:6-11`, d = 3 normalisation ⟨g_x|f|g_x⟩ = (4π/3)∫r⁴b²f dr in `r96_d3_lattice_mass.py`).
- **H-gen.** "Exact algebra" means operator identities on the common invariant domain 𝒟₂³. This is the antisymmetric C_c^∞ two-particle wavefunctions supported in {|P| < Π₁, |q| < Q}, with Q chosen so that every leg lies in the open ball |k| < B.
  - Q_max ≈ 2.28 (sampled, `r96_geometry.out:1`); any κ < Q < Q_max will do.
  - 𝒟₂³ lies inside both exact regions (cube and ball).
  - Integrability on the box is **not** claimed (B1 Theorem U, `agents/C4_B1_referee.md:7-11`).
- **Exact region** (registration): (i) the cube |k_a| < B; (ii) the inscribed ball |k| < B.
- **Excluded realizations (not addressed):**
  - N ≥ 3;
  - pair creation and loops;
  - gauge fields;
  - local lapse and Ward identities W1–W4 (R9-2/R9-10);
  - the edge sector's gravity (R8-2/R9-1);
  - Euclidean Z⁴ and LRL;
  - ungraded qubit realizations (R9-5).

## 2. Prior art (each counted once)

- **R8-1** (CONFIRMED WITH CORRECTIONS, PASS WITH SCOPE; `TESTS.md:3795-3804`): d = 1 and d = 2 law and boost, Theorem L, chart method.
  - Its d = 3 line is a suggestion only (`C5_R8-1_report.md:127,279`).
  - The referee: "establishes nothing for d=3" (`C5_R8-1_referee_verdict.md:35-36`).
- **R7-1** (`TESTS.md:3398-3407`): Lemma L (box locality), P1 (free, every N), free leakage 2‖1_E ψ‖, rapidity budgets.
- **R7-1 referee:** d ≥ 2 needs a complete rotational multiplet (`C5_R7-1_referee_verdict.md:99-104`).
- **B1** (`agents/C4_B1_referee.md:7-11`): Theorem U (no bounded K-invariant exponentiating sector); Theorem R (no nontrivial effective circle action with a fixed point on T^d).
- **Comparators.** Bakamjian–Thomas 1953 and the canonical (Newton–Wigner) spin form, RECALLED as cited by the R8-1 referee (Polyzou's notes, eqs. (136)–(140)); not re-fetched.

---

## 3. The law in d = 3

- **Canonical chart.** q = k₁ + P[(P·k₁)/(M₀(H₀+M₀)) − ε₁/M₀], as in d = 2. The Jacobian |∂(k₁,k₂)/∂(P,q)| = ε₁ε₂M₀/(ω²H₀) holds in d = 3: FD check 1.3e-10, round trip 1.7e-16 (`r96_d3_chart_algebra_NP40_repaired.out:1`).
- **Generators** (R7-1's measured conventions: X = i∂_k, [K_a, K_b] = −iε_abc J_c, [J_a, V_b] = iε_abc V_c):
  - H = √(M² + P²);
  - J = X_NW × P + S, with S = −i q × ∇_q;
  - **K = ½{H, X_NW} + (P × S)/(M + H).**
- **Lattice-native forms** (proved, algebra from the free chart identity of §4.1 and unique solvability of ½{H₀, D} = A for H₀ > 0):
  - K₀ = ½{H₀, X_E}, with X_E = Σ_i ½{ε̃_i/H₀, X_i};
  - **X_NW = X_E − (P × S)/(H₀(M₀ + H₀));**
  - **S = (H₀/M₀)[A − P(P·A)/(H₀(M₀ + H₀))], with A = J₀ − X_E × P** (and P·S = P·A). In d = 2, P·S = 0, and this reduces to R8-1's S = (H₀/M₀)(J₀ − X_E × P) (`C5_R8-1_report.md:130`).
  - Then **K = K₀ + ½{cW, X_NW} + ½{(P × S), cF}**, with F = f(M) − f(M₀), and **J = J₀** (kinematic).
- **Fermionic.** Exchange is q → −q. The g_a are odd, so W, F and K preserve the odd sector.
- **Self-adjointness** (proved, R8-1 §3.3 + the referee's congruence lemma, unchanged).
  - K = ½{H, X_E} + B, with B = −½{cW, (P × S)/(H₀(M₀+H₀))} + ½{(P × S), cF}.
  - B is bounded: S differentiates smooth, compactly supported kernels, and the other factors are bounded multiplications.

## 4. Results

### 4.1 Probe (a): the ten-generator algebra in the chart — proved; checked

**Theorem P2‴ (d = 3).** On 𝒟₂³ the ten generators satisfy all Poincaré relations exactly.

**Proof.**
1. **Domain invariance.**
   - P is a multiplication, and X_NW = i∂_P at fixed q preserves the support.
   - S rotates q, so it preserves |q| < Q.
   - V and f(M) − f(M₀) = Q_G[f(M) − f(M₀)]Q_G (R8-1 referee's sharpening, `C5_R8-1_referee_verdict.md:26-30`) output |q| < κ < Q.
   - On |P| < Π₁, c = 1. The lattice operators equal the chart operators there, by Lemma L and the chart identity (§4.1 check).
2. **M is internal.** M commutes with P, with X_NW (it is P-independent at fixed q) and with S (V is a rotational scalar).
3. **[K_a, P_b] = iδ_ab H and [K_a, H] = iP_a.**
   - The spin term commutes with P and with H.
   - ½{H, [X_a, H]} = ½{H, iP_a/H} = iP_a.
4. **[K_a, K_b].** Write f = 1/(M+H), ∂_a f = −f²P_a/H, and K_a = ½{H, X_a} + α f (P × S)_a.
   - Orbital part: −iε_abc(X × P)_c.
   - Cross terms: iH[∂_a f (P×S)_b − ∂_b f (P×S)_a − 2fε_abd S_d] α. Using P_a(P×S)_b − P_b(P×S)_a = ε_abc(P(P·S) − P²S)_c, they give α[−if²ε_abc(P(P·S) − P²S)_c − 2iHfε_abc S_c].
   - Spin–spin term (new in d = 3): α²f²[(P×S)_a, (P×S)_b] = iα²f²ε_abc P_c(P·S).
   - Total spin part: −iε_abc[α(2Hf − P²f²) S_c + (α − α²) f² P_c(P·S)].
   - Since P² = (H − M)(H + M), 2Hf − P²f² = 1. So **[K_a, K_b] = −iε_abc J_c if and only if α = 1.** Both the S coefficient (α = 1) and the P(P·S) coefficient (α² = α) are needed. α = −1 fails both, and α = 0 fails the first.
5. **Vector rules.** [J_a, K_b] = iε_abc K_c, [J_a, P_b] = iε_abc P_c and [J_a, J_b] = iε_abc J_c hold because H and f are rotational scalars and X_NW, P, S are vectors with [S, M] = 0. [J, H] = [P, H] = [P_a, P_b] = 0 are immediate. ∎

**Chart identity** (`r96_d3_chart_algebra_NP40_repaired.out:2-11`; FD of 8th order, 12 random points, complex test function with l = 0, 1, 2 and P–q coupling). The free lattice generators K₀ = Σ_i ½{ε_i, X_i} and J₀ = Σ_i X_i × k_i, pulled into the chart, against the BT free generators with M = M₀:

| quantity | max relative difference |
|---|---|
| K₀,x / K₀,y / K₀,z vs BT (with spin term) | 1.9e-14 / 1.6e-14 / 2.0e-14 |
| J₀,x / J₀,y / J₀,z vs X_NW × P + S | 1.9e-14 / 1.9e-14 / 8.3e-15 |
| H₀ vs BT | 5.3e-17 |
| comparator: printed sign | 1.35 |
| comparator: spin term dropped | 4.2e-3 |
| comparator: α = −1 | 8.4e-3 |

The analytic statement behind this check (the free two-body generators in canonical variables have BT form) is RECALLED. It is checked here, not re-derived.

**All 45 commutators, interacting** (spectral P-grid NP³ on [−1.1, 1.1)³; q-basis = Gauss–Legendre radial (12 nodes on [0, 1.2]) × Y_lm, l ≤ 2; exact M diagonalisation per (l, m); test vector = two terms with different P-profiles, mixing the bound triplet (m = 0, ±1), scattering l = 0 and l = 2 components):

| run | max over the 45 | median | [S, M] |
|---|---|---|---|
| NP = 28, packet s = 0.09 (`_NP28_s0.09.out`) | 3.9e-4 ([K_x,K_y]) | 3.3e-5 | 1.7e-16 |
| NP = 28, balanced packet (`_NP28.out:4`) | 5.5e-7 | 3.8e-8 | 1.7e-16 |
| **NP = 40, balanced packet (`_NP40_repaired.out:14-15`)** | **1.5e-10** ([K_x,K_y]) | 1.1e-11 | 1.9e-16 |

- The residual is set by P-grid aliasing versus packet decay at the window edge. "Balanced" means s² = 1/(2k_Nyquist).
- Relations in which no P-derivative meets a P-dependent factor ([H, P_a], [P_a, P_b], [P_a, K_b] for a ≠ b) sit at 1e-16 to 1e-15.

**Comparators** (`_NP28.out`, same packet rule; "failing" = residual > 1e-6):

| case | failing relations (largest) |
|---|---|
| (c1) printed sign −½{H,X} + (P×S)f | [H,K_a], [P_a,K_a]: 2.0; [K,K]: 1.6–1.9 |
| (c2) spin term dropped | [K_a,K_b] only: 0.77–0.96 |
| (c3) α = −1 | [K_a,K_b] only: 1.6–1.9 |
| (c4) single rank-one g_z channel | 14 relations, up to 0.43; [S,M] = 0.40 |
| (c5) R8-1's d = 2 doublet (g_x, g_y) in d = 3 | 14 relations, up to 0.17; [S,M] = 0.17 |

(c4)–(c5) confirm, in d = 3, the R7-1 referee's requirement of a complete rotational multiplet (`C5_R7-1_referee_verdict.md:99-104`). In d = 3 the multiplet is the triplet, and the d = 2 doublet is not enough.

### 4.2 Probe (b): lattice spectrum, bound triplet vs |P| and direction — checked

- **Method** (`r96_d3_lattice_mass.py`).
  - Exact lattice H at fixed lattice P on an L³ torus of k₁. The supp-W block decouples because H₀ is diagonal in k₁.
  - W is applied in low-rank form: Ω is Chebyshev-interpolated in |q|², with error 5e-15 against the direct Woodbury kernel (`_L192.out:2`). The lowest eigenvalues come from Lanczos.
  - Thirteen P vectors: axes, face diagonal, body diagonals (two signs), generic directions; |P| up to 0.57 on the plateau, plus one transition-shell point.

| L | pair states in supp W | BT: spread of √(E² − P²), all P, all directions | BT: max triplet split | Galilean comparator: spread / split |
|---|---|---|---|---|
| 48 | 949–1012 | 4.2e-4 | 3.9e-4 | 0.080 / 1.7e-2 |
| 64 | 2240–2420 | 6.6e-5 | 6.5e-5 | 0.101 / 2.2e-2 |
| 96 | 7689–8117 | 3.0e-6 | 2.3e-6 | 0.094 / 2.0e-2 |
| 128 | 18037–19358 | 2.5e-7 | 2.1e-7 | 0.104 / 2.2e-2 |
| 192 | 61316–65360 | **4.0e-9** | **2.5e-9** | 0.094 / 2.0e-2 |

- Files: `r96_d3_lattice_mass_L{48,64,96,128,192}.out:16,30`. The L = 48 file comes from the first script version: same law, earlier output format.
- At L = 192 the body-diagonal rows (3,3,3), (9,9,9) and (10,10,−10) have splits of 2e-11 to 1.6e-10 (`_L192.out`).
- In the transition shell (|P| = 0.706, c = 0.988) the mass is 0.8558, as expected when c < 1.
- The triplet degeneracy at P ≠ 0 is a lattice test of [S, M] = 0, i.e. rotation invariance of the internal law.

### 4.3 Probe (c), rotations: global commutation, the ball sector, the cube budget, the leakage bound

Lattice rotations are R7-1's J0_a = dΓ(½ε_abc{X_b, j_c}), with j_c = s(k_c)s′(k_c). Since ∂_b j_c(k_c) = 0 for b ≠ c, one-body J0_n = i u·∇ with **u = j(k) × n**. This field is divergence-free, and equals k × n wherever the relevant components satisfy |k_c| ≤ B. Checked: max|j − k| = 3.6e-10 on the square (`r96_rotation_leak.out:1`).

**Proposition G (proved).** For every unit n, [J0_n, H] = 0 on the infinite lattice, for the full interacting law and every particle number.
- *Free part.* u = (∇G) × n with G = Σ_a s(k_a)²/2 = (ε̃² − m²)/2. So u·∇ε̃ = 0 everywhere on T³, and [J0_n, H₀] = 0 globally.
- *Interaction.* Wherever c ≠ 0, every leg of supp W has |k| ≤ 1.548 (`r96_geometry.out:2`; `r96_leak_d3_NP640.out:2`). That is inside the ball |k| < B = 2.6, where J0_n is the continuum rotation generator.
  - The kernel of cW is invariant under a joint rotation of all legs: c(|P|), (q′·q), |q|, |q′|, the half-density Jacobian and the chart map are all rotation covariant.
  - Integration by parts (the kernel is smooth and compactly supported inside the ball) gives [J0_n, W] = 0.
  - J0 = dΓ and W is pairwise, so this holds in every N-sector.
- **Limits.**
  - The three J0_a do **not** close to so(3) on the whole torus. The Lie bracket of the fields is [u_x, u_y] = j′_z(k_z) u_z, and j′ ≠ 1 off the cube.
  - Lattice "rotations" of corner states are exact symmetries of H, but they are not rotations: their orbits follow level sets of G that are not round.
  - The flows are ℝ-actions. They are 2π-periodic on the ball. That they are not 2π-periodic on corner orbits is suggested, not checked. This is consistent with B1 Theorem R (no nontrivial effective circle action with a fixed point on T^d).

**Proposition B (ball sector; proved).** Let ℋ_ball be the Fock states whose every leg lies in the open ball |k| < B.
- ℋ_ball reduces H, every P_a and every J0_n. On it, J0_a = dΓ(continuum L_a).
- So ℋ_ball carries an **exact unitary representation of E(3) × time translations**, commuting with H, for all angles, all axes and every N. The rotation budget is unlimited.
- Proof:
  - H₀ and P are multiplications.
  - W maps ℋ_ball into itself and annihilates any pair with a leg outside the ball (its support is in the ball). Being symmetric, it also preserves ℋ_ball^⊥.
  - The lattice orbit of a ball point is the rotation orbit, by ODE uniqueness, because the rotation orbit stays at fixed |k| < B inside the cube.
- ℋ_ball is not boost invariant (Theorem U). Only boosts leak.

**Rotation budget for the cube (proved, elementary).**
- For a leg at k and axis n, the continuum orbit is the circle {(k·n)n + cos θ k_⊥ + sin θ n × k_⊥}.
- It stays in the cube for all θ iff max_a [|k·n||n_a| + |k_⊥|√(1 − n_a²)] < B.
- It stays for all n and all θ iff |k| < B (the ball).
- For a support C and N legs: θ*(C, n) = inf over legs and points of the first angle at which the circle meets ∂cube.
- Example: for the corner centre (1.95, 1.95) about z, θ* = arcsin(B/|k_⊥|) − π/4 = 0.446 (`r96_rotation_leak.out:38`). The packet's tails start leaking earlier, as the tables below show.

**Theorem R (rotation leakage; proved).** For any N-particle lattice state ψ, any n and any θ:

  **‖e^{−iθJ0_n}ψ − ι U(R_n(θ))ψ‖ ≤ 2‖1_{E_θ}ψ‖,**

where E_θ = {configurations in which some leg's continuum orbit R_n(t)k, t ∈ [0, θ], leaves the open cube} (for the ball law: the open ball).
- Proof:
  - Off E_θ, the lattice flow of u and the rotation coincide pointwise (ODE uniqueness on the exact region), and both preserve volume (div u = 0). So the transported good part agrees exactly.
  - The bad part is bounded by unitarity.
- In BT, J is kinematic, so the interacting law has U_BT(R) = U(R) and the same bound holds verbatim.
- For ψ ∈ ℋ_ball, E_θ = ∅ for every θ.

**Checks.**
- **(A) Direct lattice operator, z axis.** The (k_x, k_y) slice is an L = 256 torus; X is the site position (FFT); RK4 in θ (`r96_rotation_leak.out`).
  - Ball packet (|k₀| = 1.70, σ = 0.10), compared with the continuum rotation:
    - leakage 1.8e-9 (θ = π/2), 2.5e-9 (π), 4.9e-9 (2π);
    - the Gaussian-tail bound is 8.1e-10;
    - ⟨ε̃⟩ is conserved to 1e-10.
    - Halving dt gives 7.0e-10 and 8.3e-10 (`r96_rotation_leak_dtcheck.out`). So this is the tail plus the integrator floor; no systematic leakage is seen.
  - Corner packet (k₀ = (1.95, 1.95), σ = 0.10):

    | θ | leakage | bound 2‖1_E ψ‖ | ⟨ε̃⟩ drift (resolution check) |
    |---|---|---|---|
    | 0.05 | 9.0e-6 | 2.4e-4 | < 1e-10 |
    | 0.10 | 1.5e-4 | 2.5e-3 | 3e-10 |
    | 0.15 | 1.4e-3 | 1.7e-2 | 3e-8 |
    | 0.20 | 8.9e-3 | 7.1e-2 | 1.8e-6 |
    | 0.25 | 3.7e-2 | 0.21 | 4.4e-5 |
    | 0.30 | 0.108 | 0.47 | 5.5e-4 |
    | 0.40 | 0.43 | 1.14 | 1.6e-2 |

  - Proposition G says ⟨ε̃⟩ is exactly conserved on the infinite lattice. The drift beyond θ ≈ 0.2 measures the finite-L spectral representation failing to resolve the packet once it enters the steep transition shell (max|j| = 22.3). The rows θ ≥ 0.25 are indicative only.
  - A first run with θ ≥ π/8 for the corner packet was in this unresolved regime throughout (`_firstrun_overlapfloor.log`). It is not used.
- **(B) d = 3, by characteristics of the lattice field u, for the z axis and the generic axis n = (1,2,2)/3** (`r96_rotation_leak.out:14-31`).
  - Method: RK4 with 160 steps. Leakage = the on-grid difference plus the lattice mass that left the comparison grid. G = Σ s(k_a)²/2 conservation on the packet is the integrator check.
  - Results (σ = 0.08):

    | packet | θ | leakage | bound 2‖1_E ψ‖ | max ΔG on packet |
    |---|---|---|---|---|
    | z, ball, \|k₀\| = 1.73 | π/4, π/2, π | 6.1e-10, 2.5e-9, 4.4e-8 | ≤ 6e-15 | ≤ 4e-10 |
    | z, corner (1.95, 1.95, 0.3) | 0.1, 0.2, 0.3, 0.4 | 2.3e-6, 1.1e-3, 4.5e-2, 0.32 | 1.1e-4, 1.8e-2, 0.31, 1.07 | ≤ 1.7e-7 |
    | (1,2,2)/3, ball, \|k₀\| = 1.65 | π/4, π/2, π | 5.7e-10, 2.2e-9, 4.1e-8 | ≤ 4e-17 | ≤ 4e-10 |
    | (1,2,2)/3, corner (2, 2, −1.9) | 0.1, 0.2, 0.3, 0.4 | 1.7e-5, 6.2e-3, 0.16, 0.74 | 9.0e-4, 7.2e-2, 0.75, 1.70 | ≤ 4.2e-4 |

  - The ball residual at θ = π (4e-8) is RK4 error. With 320 steps it falls to 5.0e-9 (z) and 4.1e-9 (generic) (`r96_rotation_charcheck.out`). The script's "VIOLATED (above 1e-8 floor)" flags at θ = π (`r96_rotation_leak.out:17,26`) are therefore integrator floor, not leakage.
  - Every corner row is below the bound, and the leakage switches on where the bound does.
  - Earlier runs are superseded: one used an overlap-based norm with a √ε floor of about 4e-7 (`_firstrun_overlapfloor.log`), and one was partial (`_secondrun_partial.log`).

### 4.4 Probe (c), boosts: Theorem L in d = 3 — proved; checked

**Theorem L³ (proved; R8-1's Theorem L with one added step).** Take a two-particle lattice state ψ, a rapidity η along n, an open set I of total momenta and a Borel set Σ of the spectrum of M. Suppose that for μ ∈ Σ, P ∈ I and s ∈ [0, η]:
- the mass-μ orbit P ↦ Φ^μ_s(P) stays in |P| < Π₁;
- every leg of (Φ^μ_s(P), q), for |q| in Q_Σ := {M₀(q) ∈ Σ} ∪ supp g, stays in the exact region (cube, or ball).

Then ‖e^{−iηK}ψ − ι U_BT(η)ψ‖ ≤ 2‖(1 − E)ψ‖, with E = 1_I(P)1_Σ(M).
- **Added step for d = 3.** U_BT moves q only by the Wigner rotation generated by S (the spin term). That rotation preserves |q|, and Q_Σ is a union of spheres. So the legs condition is the same with or without the Wigner rotation.
- Steps 1–4 and the density argument are R8-1's, as sharpened by its referee (`C5_R8-1_referee_verdict.md:25-30`).

**Check** (`r96_leak_d3_NP{640,960}.out`). A boost along x leaves P_⊥ fixed and differentiates only in P_x, so at fixed P_⊥ = (0.20, −0.10) the d = 3 chart law is a 1D transport on the l = 1 channel (3 m-states × 24 radial nodes). The spin term (P × S)_x = P_yS_z − P_zS_y is active: the m-weights evolve from (0.3620, 0.2514, 0.3865) to (0.3626, 0.2529, 0.3846) over η ∈ [0.1, 1].

| η | ‖U_lat − U_BT‖ψ, NP = 640 | NP = 960 | bound 2‖(1 − E)ψ‖ |
|---|---|---|---|
| 0.10–0.30 (< η* = 0.3166) | 1.3e-6 – 1.6e-6 | 5.8e-8 – 7.1e-8 | 0 |
| 0.35 | 1.9e-6 | 8.4e-8 | 5.4e-3 (NP 640) / 1.1e-2 (NP 960); the grid samples the bump's edge |
| 0.45 | 3.3e-5 | 3.3e-5 | 0.60–0.63 |
| 0.60 | 1.47e-2 | 1.47e-2 | 1.43 |
| 0.80 | 0.143 | 0.143 | 1.99 |
| 1.00 | 0.298 | 0.298 | 2.0 |

- Before η* the difference is discretisation: it falls 20× from NP = 640 to 960, as in R8-1 d = 1. The NP = 640 file flags "VIOLATED" against a 1e-6 tolerance at η ≤ 0.3; that is this floor, not a violation.
- (ii) The bound + continuum mix stays below the optimised bound at all eight η (`_NP960.out`, (ii)).
- Here every leg is ≤ 1.548 while c > 0, and ≤ 2.494 for |P| ≤ 2.4 (`_NP640.out:2`). So **the plateau Π₁ is the binding condition, and it is isotropic: cube and ball give the same interacting boost budget** for this law.

**Free boost budgets, cube vs ball (proved, elementary; `r96_geometry.out`, (iii)).**
- A particle at rest boosted along n has k(η) = m sinh η n.
- Cube: η* = asinh(B/(m max_a|n_a|)):
  - m = 0.5: 2.351 (axis), 2.693 (face diagonal), 2.894 (body diagonal);
  - m = 0.85: 1.837, 2.171, 2.369.
- Ball: asinh(B/m) in every direction.
- **Reading.** At Planck spacing with R7-1's b = 2.0/ℓ_P (`C5_R7-1_report.md`, §4.4), a proton at rest has 45.40 (axis) and 45.95 (body diagonal) with the cube (`r96_rotation_leak.out:37`), and 45.4 isotropically with the ball. The difference tends to ln√3 = 0.549. Both are far above the ~27 used by the highest-energy cosmic rays.
- The free leakage theorem is R7-1's (CONFIRMED, any d); its d = 3 orbit sets are as above. It was not separately re-run here for a free leg in d = 3.

### 4.5 Probe (d): cubic anisotropy of the bound state — proved (registered law); checked (stress test)

- **Registered law (B = 2.6, Π₂ = 1.2, κ = 0.8): zero anisotropy, exactly (proved).**
  - Wherever c ≠ 0 the bound state's legs satisfy |k| ≤ 1.548. That is inside the inscribed ball, so cube and ball are indistinguishable for it.
  - Its invariant mass is exactly M_b in every direction on the plateau.
  - Checked: §4.2 includes axis, face-diagonal and body-diagonal P with spread 4.0e-9 at L = 192.
  - The only cube effects in this law are the direction-dependent **free** boost budget (§4.4) and the finite rotation budget of corner states (§4.3), which the bound state never occupies.
- **Stress test (outside the registered law): shrink the exact cube to B = 1.6 and extend the plateau to Π₁ = 2.0, Π₂ = 2.4.**
  - B₂ = 2.4; pair-state mask 2.9 ⊃ supp W.
  - Geometry (`r96_geometry.out`, (ii)): some leg with |q| ≤ κ first touches a cube face at |P| = 1.272 along an axis, 1.798 along a face diagonal and 2.202 along a body diagonal. It first touches the inscribed ball at 1.271 in every direction.
  - Lattice (`_L128_Pi2.00_2.40_B1.60_B2_2.4_scan.out`; L = 96 agrees at the same |P| to the stated precision):

| |P| | axis: √(E² − P²) − 0.85 (lowest member) | face diagonal | body diagonal |
|---|---|---|---|
| 1.18–1.53 | ≤ 1.7e-7 | ≤ 2.0e-7 | ≤ 1.9e-7 |
| 1.62 | −9.2e-6 | ≤ 1.6e-7 (1.60) | −2.7e-7 (1.62) |
| 1.72 | −3.2e-4 (triplet split 3.1e-4) | ≤ 2.5e-7 (1.67) | ≤ 1.5e-7 (1.70) |
| 1.82 | −3.7e-3 (split 3.6e-3) | ≤ 2.6e-7 (1.80) | ≤ 1.8e-7 (1.79) |
| 1.91–2.01 | triplet not among the 12 lowest (12 band-bending pair states below) | ≤ 1.6e-7 (1.87, 2.01) | ≤ 2.4e-7 (1.87); +8.7e-5 at 2.04, inside the c < 1 shell |

  - **Reading.**
    - With only the cube exact, the bound triplet is exactly relativistic as long as its legs are in the cube. Along an axis, legs reach the faces first and the mass departs there.
    - The measured onset (|P| ≈ 1.6) lags the geometric touch (1.27). The band's deviation s(k) − k is super-flat just past B (non-analytic plateau), and the bound state's amplitude vanishes smoothly at |q| = κ.
    - The axis rows at |P| ≥ 1.8 are not L-converged (L = 96 gives −3.4e-2 at 1.83).
    - An isotropic plateau chosen inside the inscribed region removes the effect completely, as in the registered law.
  - A first stress-test version (B₂ = 2.0, Π₁ = 1.8) had the band bend so fast that lattice pair states with E < |P| (R8-2's edge sector) sat below the triplet along the axis (`_B2_2.00` files). It is superseded.
  - With B₂ = 3.0 (`_Pi1.80_2.20_B1.60_B2_3.0.out`) the axis shift at |P| = 1.767 is −4.1e-5, the same at L = 96 and 128.

---

## 5. Reading against the FIXED readings (`TESTS.md:3784-3787`)

- **PASS: worker reading, referee required.**
  - **(a) Closes to a stated tolerance.** All 45 commutators of {H, P_a, J_a, K_a} close in the canonical chart, with the spin term, to ≤ 1.5e-10 (NP = 40), converging with resolution. The algebra is proved (α = 1 forced by two conditions in d = 3). The lattice free generators equal the BT free generators in the chart to 2e-14.
  - **(b) Mass P-independent to converging precision.** The lattice triplet mass is P- and direction-independent: 4.2e-4 → 4.0e-9 from L = 48 to 192, with triplet split 2.5e-9.
  - **(c) Leakage bounds proved and checked for rotations and boosts.**
    - Rotations: Theorem R and Propositions G and B, proved. Checked with the direct lattice operator for z (ball at the integrator floor ≤ 5e-9; corner under the bound at every angle) and by characteristics for z and a generic axis (§4.3 (B)).
    - Boosts: Theorem L³, proved and checked in d = 3 with P_⊥ ≠ 0 and the spin term active.
- **The caveat that travels with it (as for R8-1, `TESTS.md:3800-3804`).**
  - There is no direct lattice-native run of the 45 commutators in d = 3. The R8-1 d = 2 attempt was resolution-limited at 7e-3 to 0.35 (`C5_R8-1_report.md:258-272`), and d = 3 would be worse.
  - The d = 3 lattice evidence is: the chart identity of the lattice free generators (2e-14); the rep-independent lattice spectrum (4e-9, converging); the direct lattice rotation operator (§4.3 (A)); and Theorem L³'s chart integration.
  - The registration expected INCONCLUSIVE overall for this reason (`TESTS.md:3788`). The FIXED PASS sentence asks for (a)–(c) as stated, and (a) is registered "in the canonical chart" (`TESTS.md:3780`). If the referee requires a direct lattice-native d = 3 commutator run, the strongest reading is INCONCLUSIVE, with P2‴, Theorem R, Propositions G and B and Theorem L³ as bounded positive results.
- **FAIL is not available.** P2‴ is an explicit d = 3 interacting counterexample to an obstruction on the box sector.

## 6. Strong-word check

- **"Exact":** an operator identity on 𝒟₂³ (algebra), or on ℋ_ball (rotations), in infinite volume. All numerics are finite-L or finite-grid, and converging.
- **"Globally" in Proposition G:** the infinite lattice. On a finite torus the spectral X breaks [J0_n, H₀] = 0 at the resolution scale; that is what the corner packet's ⟨ε̃⟩ drift shows.
- **"Unlimited rotation budget":** ℋ_ball only; all angles, all axes, every N. On the cube it is finite, and for supports that reach the corners it tends to 0.
- **"Every N":** applies only to Propositions G and B and Theorem R. Rotations are kinematic and W is pairwise. The **boost** algebra for N ≥ 3 is not claimed (BT cluster problem, R9-3).
- **Not re-derived here:** the free chart identity's analytic form (RECALLED BT/canonical-spin, checked to 2e-14), and the Q_max of 𝒟₂³ (sampled).
- **"Cubic anisotropy zero":** the bound state of the registered parameters. It is not a general statement about every κ, Π₂ and B.
- **Not addressed:** gravity, Ward identities or universal coupling (R9-2/R9-10, R8-2).

## 7. Price (named, not adopted)

Unchanged from R7-1/R8-1:
- non-quasi-analytic band and kernel functions;
- a frame-fixed box;
- an inert edge sector;
- form-factor interactions defined through the pair's invariant mass;
- a graded fermionic composition (`TESTS.md:3253`; R9-5 for the ⊗M₂ question).

Added in d = 3:
- **The shape of the exact region is a choice with a residual cost.**
  - The cube gives direction-dependent free boost budgets (ln√3 between axis and body diagonal) and a finite rotation budget for corner states.
  - The ball removes both, but at the cube's axis radius.
  - Neither shows up in any in-domain observable of the registered law.
- **Reading.** The continuous SO(3) here is a property of the chosen law on ℋ_ball. The Lattice axiom supplies only proper cubic rotations (`MINIMAL_AXIOMS_2026-06-29.md:37-38`).

No axiom text changes. Admissibility does not fix the dynamics (`MINIMAL_AXIOMS_2026-06-29.md:116-123`).

## 8. For the referee

Check, in order:
1. The α = 1 derivation with the d = 3 spin–spin term (§4.1, step 4), and the comparators (c2)/(c3), which fail only in [K_a, K_b].
2. The chart identity in d = 3 (`r96_d3_chart_algebra.py` (a)), and the lattice-native forms of §3 (X_NW and S in terms of X_E, J₀, H₀, P).
3. Proposition G: the support bound 1.548 < B, and [J0_n, W] = 0 by rotation invariance of the kernel. Also the non-closure [u_x, u_y] = j′_z u_z off the cube.
4. Proposition B and Theorem R (ODE uniqueness on the exact region; div u = 0).
5. Theorem L³'s added step (Wigner rotation preserves |q|, and Q_Σ is rotation invariant).
6. Whether §5's evidence meets the FIXED PASS sentence, given no direct lattice-native d = 3 commutator run.

Runtimes (OMP_NUM_THREADS=2):
- chart algebra, NP = 40: 110 s; NP = 28 with comparators: 4 min;
- lattice spectrum, L = 192: 2 min;
- rotations: about 4 min;
- d = 3 boost leakage: about 1 min per NP;
- geometry: 10 s.
