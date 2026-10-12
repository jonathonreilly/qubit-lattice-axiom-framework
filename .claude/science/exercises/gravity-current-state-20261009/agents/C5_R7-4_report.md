# C5 R7-4: the weak N-type stress bridge (worker report)

Worker: Claude Opus 5.5 (same family as the supervisor). Run 15:07Z to 15:30Z, 2026-10-12. No repository files were edited. Scratch folder: `.../scratchpad/C5/R7-4/` (`S/` below). Scripts and outputs are in `S/scripts/`. Nothing here is refereed.

Path abbreviations used below: `TESTS` = `.claude/science/exercises/gravity-current-state-20261009/TESTS.md`; `SUMMARY` likewise; `agents/` = that exercise's `agents/` folder; `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

## Headline against the FIXED readings (`TESTS:3360-3371`)

- **PASS is met only in the free (non-scattering) class.** There I give an explicit exact linear coupling of two species with different dispersions. It is checked, it gives 1/r, and it gives γ = 1. But the constraint does **not** force universality there: the per-species coupling is a free parameter. So universality and γ = 1 come only from named tunings (§2). This extends RN L1 (`TESTS:840-851`) from one species to two; it is not a new mechanism.
- **For matter that actually scatters, I find an obstruction (argued, not refereed): the lattice boost-flow obstruction (§4).**
  - An exact linear lapse/shift bridge makes matter's energy dipole D = Σ x·T00 an exact "linear-order boost charge": i[H, D] = J with [H, J] = 0.
  - Under the cluster property, the S-matrix must then commute with the free flow that D generates. On every outgoing particle that flow moves momentum as dk/ds = ω(k)·n.
  - On the compact Brillouin zone this flow winds momenta around the torus. Non-forward on-shell configurations are carried off the energy shell, so their T-matrix must vanish.
  - This holds for every continuous positive band, SLAC included, and for every interaction whose energy density is quasi-local. The R6-1 box form-factor witness falls in this class.
- **Recommended reading: INCONCLUSIVE.** The literal PASS holds only for free species with tuned universality. The obstruction is a **FAIL candidate** in a stated class. It needs the referee, and it has named gaps (§4.6).

## 0. Prior art read

- **Axioms (`AX`, read in full).** Admissibility fixes no Hamiltonian, stress or dynamics (`AX:114-130`). So every coupling below is supplied content.
- **N0914.**
  - H_N gives ω² = Jg·k² (`N0914:72-74`).
  - The source problem gives the inverse-Laplacian kernel (`N0914:290-295`).
  - "deriving a mobile conserved matter stress source and reciprocal backreaction is a separate obligation" (`N0914:294-295`).
- **Lane R.** The exact-constraint weak VS/N-type theory is the strongest counter-route (`TESTS:759`, `TESTS:767`; `agents/R2_referee.md`, §6).
- **RN L1 (CWC).** For the free scalar:
  - exact symmetric stress;
  - first class at linear order;
  - 1/r, with the same G for different masses;
  - γ = c_m²/c_g² (`TESTS:840-851`; `agents/RN_L1_referee.md`, items 1, 2, 5, 6).
- **RN L3, §2a (suggested).** First-class lapse and shift implies a conserved total energy current, i.e. ballistic energy (`agents/RN_L3_report.md:120-137`). Its cohomology step is proved for finite range by RC C1 Lemma C (`TESTS:1171`; `agents/RC_C1_referee.md:5`).
- **RG G3.** The shift source must be the energy current, which forces SLAC (`TESTS:1066`).
- **RC C1.**
  - Lemma R: C¹ invariants of normal collisions are λE + b·k + c (`TESTS:1172`).
  - Theorem A: closure forces E² = m₀² + β|k|², and mutually scattering species share β (`TESTS:1173`; `agents/RC_C1_referee.md:9`).
- **C4 boost wall (§17).**
  - It is an O(κ) closure obstruction, Hess(E²/2) = βI (`SUMMARY:397-412`).
  - M1 already uses the one-particle first-moment flow dQ/dη = −E(Q) (`agents/C4_M1_report.md:177`).
  - V3 gives the E_g vacuum shear, μ_E = +1.97e-3 for the m = 1 scalar (`SUMMARY:411`).
- **R6-1 (SUGGESTED).**
  - Its witness W uses a C^∞ box form factor with a = 0.49π (`agents/C5_R6-1_report.md:87-104`).
  - The worker's own suggestion: "any boost moves momenta near ∂S out of S" (`agents/C5_R6-1_report.md:191`).
  - The referee: W gives no boost-compatible or SLAC energy current (`agents/C5_R6-1_referee_verdict.md:33`).
- **R6-2.**
  - Lemma A is false as stated (`agents/C5_R6-2_referee.md:51`).
  - The exact weak N-type bridge stays OPEN (`agents/C5_R6-2_referee.md:75,92`).
  - The GW170817 band is −3e-15 ≤ Δc/c ≤ 7e-16 (`agents/C5_R6-2_referee.md:79`).
- **Literature.** Gu–Wen (0907.1203), Xu–Hořava (1003.0009), Pretko (1604.05329) and Rasmussen–You–Xu are used as **comparators** only, as cited in `N0914:412-415` and in `agents/R2_referee.md`. I did not re-verify them on the web this run. The Cook / Haag–Ruelle intertwining used in §4.2 is a standard scattering-theory **comparator**.
- **Repo search.** It found no prior use of S-matrix invariance under the first-moment flow as a linear-order bridge test. The search covered `agents/` for Møller, Cook and Haag, and energy-dipole wording.

## 1. Setting (fixed by the item)

**Gravity.** H_N on Z³ with the 09-14 integer stencils: S, the scalar constraint, and G, the vector constraint (`N0914:95-101`).

**Coupling.** Lapse n and shift N_j multiply the constraints:

H = H_N + Σ_s H_s + n·(S/κ + Σ_s a_s T00^s) + N_j·(−(J/κ)G_j + Σ_s a_s J_E^s,j) + Σ_s c′_s h_ij T^s_ij.

The sign and normalization follow RN L1: −½h·T at the GR point (`agents/RN_L1_report.md`, "Normalization"). Linear order means O(√κ) in the constraint algebra.

## 2. Result A: two free species with different dispersions

### 2.1 Exact identities (CHECKED, `r74_two_species.out`, lines 1-3)

Take a nearest-neighbour scalar with hopping c_s² and mass m_s, with H_s = Σ ½π² + ½m_s²φ² + ½c_s²Σ_j(d_jφ)². RN L1's T00 and T_ij have their gradient parts scaled by c_s². Three random-field checks at (c, m) = (1, 0.3), (1.3, 1.1) and (0.7, 0):
- **(E)** dT00/dt = −div J_E with **J_E = c_s²·P**, where P_j = ½(π_x + π_{x+e_j})d_jφ. Relative residual ≤ 2.5e-10, which is float rounding of the polarization difference; the identity is exact for quadratic forms.
- **J_E = P fails** unless c_s = 1: residuals 0.41 and 1.04.
- **(M)** dP_j/dt = (G[T])_j with T **symmetric** in the 09-14 placement. Residual ≤ 5e-11.

**New precision.** The shift source is the energy current, which is c_s² times the pseudo-momentum. RN L1's "the same P is both" holds only at c = 1.

### 2.2 Closure fixes the couplings per species (PROVED, elementary)

- Preserving the shift constraint for a separately conserved species gives (J/κ)c′_s + a_s c_s² = 0, so **c′_s = −κa_s c_s²/J**.
- The lapse constraint closes for any a_s, by GSᵀ = 0 and S(q̇) = −J·div G (RN L1, CWC).
- So **the a_s are free parameters for free species. The constraint algebra does not force universality.**

### 2.3 Observables at linear order

Status: PROVED as formulas; evaluated in `r74_two_species.out`, lines 5-16.

- **Static field.** Take a dust source of species S. Then ψ = κa_S T00/(4q̂²) and n = −2gκψ, with 1/r at the GR point (RN L1, checked to 0.05%; not recomputed here).
- **Test quantum of species s.** Its frequency shift is

  δω_s/ω_s = a_s·n·[1 + (c_s²/c_g²)·(f·v_s)/ω_s], with f = sin k and c_g² = Jg.

  This gives:

| Quantity | Value | Needed for GR-like behaviour |
|---|---|---|
| Rest redshift | a_s·n | LPI: a_A = a_B |
| Slow free fall | ẍ = −a_s c_s²·∇n (inertia is m_s/c_s²) | WEP: a_A c_A² = a_B c_B² |
| Light bending, from (light)/(Newtonian at v = c_s) | **γ_s = c_s²/c_g²**, independent of a_s | γ = 1: c_s = c_g |

- **Numbers.**
  - c_g = 1: species (c = 1.3) has γ = 1.69 and a free-fall factor of 1.69. So equal a gives an Eötvös parameter η = 0.69 against the c = 1 species.
  - c_g² = 1.21: γ = 0.826 for c = 1.
  - The lattice anisotropy of the ray response is −k²/4, −k²/8 and −k²/12 on axis, face diagonal and body diagonal. This matches RN L1.

### 2.4 Tunings named (free class)

| # | Tuning | Bar | Size |
|---|---|---|---|
| T1 | c_g = c (one graviton–matter speed) | GW170817: −3e-15 ≤ Δc/c ≤ 7e-16. Cassini (\|γ−1\| < 2.3e-5) is weaker | about 15 decades against an O(1) bare mismatch. This is a naturalness estimate, per `agents/C5_R6-2_referee.md:79` |
| T2 | a_A = a_B (N−1 coupling ratios) | Redshift/LPI and Eötvös tests (comparator) | not forced in the free class |
| T3 | c_A = c_B (N−1 matter speeds) | WEP at η ≲ 1e-15 (MICROSCOPE, comparator) and matter Lorentz invariance at about 1e-20 (`TESTS:2331`) | not forced in the free class |
| T4 (beyond linear order) | the E_g counterterm (P0's μ_E) | — | the local free-matter vacuum gives μ_E ≠ 0 (V3, `SUMMARY:411`; RV4 FAIL bounded, `SUMMARY:508-517`) |

**Against the item's three tests (free class):**
- **Universality across two species:** holds only with T2 and T3.
- **Newtonian limit:** 1/r holds.
- **γ = 1:** needs T1.

## 3. Result B: what interactions would force, if a bridge existed (PROVED, elementary, plus cited)

Let species A and B exchange energy and momentum in collisions. Then:
- Σ_s a_s T00^s is conserved only if a_A = a_B, since energy flows between species.
- Σ_s a_s J_E^s is conserved only if its one-particle symbols a_s ω_s∇ω_s are one common collision invariant b·k. With a common a, this gives c_A² = c_B² = b/a, which is RC C1 Theorem A's shared β (`agents/RC_C1_referee.md:9`).

So **an interacting bridge would supply T2 and T3 for free, leaving only T1.** That is exactly why the interacting bridge is the question. Section 4 argues that it does not exist on a lattice.

## 4. Result C: the lattice boost-flow obstruction (main new item)

### 4.1 Lemma 1: the bridge is an exact linear-order boost charge

Status: prior art plus PROVED.
- Linear first-class closure with a quasi-local T00 (ΣT00 = H_m), shift source P and symmetric T gives div P = div j_E.
- Lemma C then gives P = j_E + curl + a constant. The constant is 0, by cubic covariance (`TESTS:1171`).
- dP/dt = G[T]. Hence J := Σ_x j_E(x) = Σ_x P(x) is conserved.
- With D := Σ_x x·T00(x), summation by parts gives **i[H, D] = J and [H, J] = 0**. RN L3 §2a reached the same point and called it "ballistic energy".
- The improvement freedom T00 → T00 + div v changes D to D − V, where V = Σv is a quasi-local total operator. It changes nothing below.
- Unlike the C4 boost wall, nothing here uses [K, P] closure, O(κ), or Hess(E²/2).

### 4.2 Lemma 2: S commutes with the free first-moment flow

Status: ARGUED. It is the standard Cook / Haag–Ruelle step (comparator). Hypotheses:
- (H1) asymptotic one-particle bands ω(k) that are continuous and positive on the torus;
- (H2) Møller operators exist;
- (H3) cluster property: interaction parts of T00 and j_E vanish on separating wave packets faster than 1/t. Super-polynomial tails suffice, so R6-1's form factors are included;
- (H4) the one-particle restriction of D is D⁽¹⁾ = ½{X, ω(K)} + Y(K).

The argument:
- e^{iHt}De^{−iHt} = D + tJ exactly.
- Ω_± D₀ = D Ω_±, because (D − D₀) and t(J − J₀) vanish on e^{−iH₀t}ψ.
- Hence **[S, U_s] = 0 for U_s = exp(is n·D₀)**, for every direction n.

The one-particle current is J⁽¹⁾ = ω∇ω. This is G3's "shift source = energy current", now derived from D.

### 4.3 Lemma 3: kinematics (PROVED)

- U_s acts on each leg by the flow dk/ds = ω(k)·n, up to a Jacobian and a phase. The phase comes from Y.
- S conserves H₀ energy.
- So **if T(in→out) ≠ 0, then E_in(Φ_s) = E_out(Φ_s) for all s**, and the support of T is invariant under the flow.
- A bounded support, such as a box form factor, is therefore impossible unless T = 0. In `r74_boost_flow.out` every leg leaves R6-1's box S at s_box = 0.28–1.8, even in the continuum control.

### 4.4 Lemma 4: on the compact zone, non-forward orbits leave the shell

**Continuum control, ω² = m² + |k|² on R² (CHECKED).** The flow is the exact Lorentz boost. It stays on shell for 12 of 12 configurations, and for every direction n; max|ΔE| is 4e-9 (integration error).

**SLAC band, ω² = m² + |k̄|² with k̄ reduced to the zone.**
- Status: PROVED up to genericity; CHECKED for 12/12 random configurations along x, 8/8 along random n, and 4 special directions.
- **Mechanism.** Between edge crossings the flow is an exact boost. When the first leg's component crosses π, its reduced momentum jumps by 2π. From then on d(E_in − E_out)/ds = ∓2π·n_i ≠ 0, unless an out-leg crosses at the same instant. Crossing instants are analytic in the configuration, so a coincidence is a proper analytic condition.
- **Numbers.** It leaves the shell at s_off = 0.92–2.47, with |ΔE| up to 3.3. Exact SLAC matter (RC C1 Theorem A's only survivor) is therefore excluded from the interacting bridge.
- **Exception, and its kill.** The CM reflection (a,−a) → (a₁,−a₂),(−a₁,a₂) stays on shell under the x and y flows. It leaves under the diagonal flow and under n = (cos 0.3, sin 0.3), at s_off = 1.43 and 1.19. Lemma 2 holds for every n.

**Smooth periodic bands: SMTH (C^∞, with ω² relativistic in the box) and nearest-neighbour KG.**
- Status: PROVED when the legs' x-periods τ(k_y) = ∮dk_x/ω are rationally independent. Then a sum of periodic functions with independent periods vanishes identically only if each term is constant, i.e. ω is flat along the leg. Otherwise ARGUED.
- CHECKED:
  - SMTH: 12/12 and 8/8, with s_off = 0.55–1.91.
  - KG: 10/10, leaving immediately, since d(E_in − E_out)/ds|₀ = Σ sin k_x is not conserved (Lemma R). The four periods are distinct in every sample, for example 3.69, 3.23, 4.03, 3.76 (`r74_kg_flow.out`).
- Forward and exchange controls stay on shell for every band.

### 4.5 Theorem (ARGUED; a FAIL candidate for the referee)

**Class:**
- translation- and cubic-covariant matter on Z^d, d ≥ 2;
- a quasi-local energy density;
- (H1)–(H4);
- coupled to the fixed 09-14 N-type constraint pair at linear order.

**Statement.** If the lapse/shift constraints are exactly preserved, the matter's on-shell n→m T-matrix vanishes on an open dense set of non-forward configurations. Only forward or exchange scattering survives.

**Corollaries:**
- The R6-1 witness and every box-supported construction (R7-3's candidates, conditionally) cannot feed the bridge. This upgrades `agents/C5_R6-1_report.md:191` from suggested to argued.
- RG's open non-analytic corner and RC C1's SLAC escape are closed for the **bridge**. They are not closed for momentum conservation alone.
- Universality is never forced inside this class. Forward scattering moves no energy-momentum between species, so §3's mechanism is unavailable, and T2 and T3 stay tunings.
- **Generalization.** The same holds if the lapse couples to any conserved density with a nowhere-vanishing one-particle weight ρ̃ > 0. Particle number, the Galilean case with flow dk/ds = n, is included.

### 4.6 Gaps and escapes (named, not dismissed)

**Gaps:**
- (G1) Lemma 2 is not proved with domains. Bound states, composite legs and dressed one-particle sectors need (H4) checked. Composite bands are continuous and positive (M1), so they should be covered.
- (G2) In the smooth case, resonant (rationally dependent) periods are covered only by the direction-n freedom (argued and checked), not proved.
- (G3) "Open dense non-forward" is shown for 2→2. n→m is argued by the same flow.

**Escapes outside the class:**
- (E1) Long-range, IR-singular interactions (Coulomb, gravity itself). The cluster property (H3) fails, so infraparticles are not covered. This is the live corner.
- (E2) A non-compact one-particle fibre, i.e. a continuum in every cell (RI's complete tower). It has no winding, as the CONT control shows.
- (E3) Forward-only (integrable-like) scattering. It is allowed, but it forces no universality.
- (E4) Changing the 09-14 constraint pair, or making it approximate (energetic penalties). Then μ_E and μ_T2 return (`agents/R2_report.md` §4(c)).
- (E5) Non-quasi-local energy density.

### 4.7 In plain words

An exact constraint of this kind makes the centre of matter's energy coast at a fixed velocity forever. On a grid, momentum lives on a circle. The rule that keeps the centre coasting turns, for incoming particles, into a "boost" that pushes every particle's momentum around that circle at its own rate. Real collisions mix particles with different rates, so the push breaks energy conservation for any collision that changes directions. The only way out is for collisions never to change directions, which is not matter.

## 5. The three requested tests

| Test | Free species (Result A) | Scattering matter (Result C) |
|---|---|---|
| Universality across two species with different dispersions | Only with tunings T2 (a_A = a_B) and T3 (c_A = c_B). Not forced (proved) | The bridge, if it existed, would force both (§3). But it is obstructed (§4, argued) |
| Newtonian limit, γ | 1/r (RN L1). γ_s = c_s²/c_g² (proved, evaluated) | n/a (no bridge) |
| Speed tuning against GW170817 | T1: c_g = c, about 15 decades, naturalness estimate | T1 would remain even if the bridge existed |

## 6. Strong-word check

- **"Exact"** is used only for the free-field identities (E) and (M), checked to float rounding.
- **"Proved"** is used only for:
  - §2.2, the free a_s;
  - §2.3, the formulas;
  - §3;
  - Lemma 1, given Lemma C;
  - Lemma 3;
  - Lemma 4 for SLAC (up to genericity) and for the smooth case (under rational independence).
- **Argued:** Lemma 2 and the theorem.
- **"Impossible" is not used for the bridge.** The theorem is a FAIL candidate in the stated class, pending a referee.
- **Not claimed:**
  - anything about long-range or IR-singular matter;
  - anything about modified constraints, non-compact fibres or O(κ);
  - a qubit realization of H_N (Lemma A remains false as stated);
  - literature priority.

## 7. Files (in `S/scripts/`)

- `r74_two_species.py` / `.out`: exact identities for two species; linear observables; γ_s, EP and LPI.
- `r74_boost_flow.py` / `.out`: boost-flow shell test for the CONT, SLAC and SMTH bands, plus the R6-1 box exit time, forward controls, the special CM reflection and random directions.
- `r74_kg_flow.py` / `.out`: the same test for nearest-neighbour KG, with leg periods.
