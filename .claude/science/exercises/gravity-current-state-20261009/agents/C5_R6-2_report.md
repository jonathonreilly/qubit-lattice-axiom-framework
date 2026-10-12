# C5 R6-2: can any set produce the graviton? A Weinberg–Witten sorting with the B′ specifics

**Worker.** Claude Opus 5.5 (same family as every C5 worker and the supervisor). 2026-10-12, 14:19Z–14:55Z. **Unrefereed.** No repository file was edited. Scripts and outputs: `scratchpad/C5/R6-2/scripts/` (`r62_little_group.py`, `r62_hww_dispersion.py`, `r62_hww_box5.py`, `r62_tensor_lv_counts.py`, `r62_averaging_lemma.py`, each with a `.out`). Every run took under 1 s on 2 threads.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS`, `SUMMARY`, `OUTSIDE_VIEW` are in `P/`. Bare `B_referee.md`, `R0_report.md`, `R2_report.md`, `C5_*` are in `P/agents/`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.

**Labels.** proved / checked (script) / suggested / reading / comparator (V = fetched or search-verified this session; M = from memory, unverified).

---

## 0. In plain words

- **The theorem.** Weinberg–Witten (WW) says that in a theory with exact Lorentz symmetry, a massless spin-2 particle cannot get its energy from an ordinary (Lorentz-covariant, conserved) energy-momentum tensor. So a graviton cannot be an ordinary composite of matter in a Lorentz-invariant world. It has to be a gauge field, whose own energy is not localizable (GR's pseudotensor), or one of WW's premises has to fail.
- **Set A (continuum + records).** Its matter is an ordinary Lorentz-invariant field theory, so WW applies. The graviton must be put in by hand. Every way out changes what A is. Reading: **SUPPLIED-FORCED** (referee required).
- **Set B (Euclidean Z⁴).** The grid protects matter's light cone. It does **not** protect the graviton's: for a two-index field, the 4D cube symmetry allows 3 mass and 9 kinetic forms, against Lorentz's 2 and 4. So a hand-tuned non-gauge graviton escapes WW. The price is the 11 tunings already counted. A gauge-protected graviton falls under WW. Reading: **OPEN**. It becomes SUPPLIED-FORCED if the graviton's speed is to equal light's without tuning.
- **Set B′ (Lorentz-random lattice).** One copy has only a discrete symmetry. Its little groups are rotations of order 1, 2, 3, 4 or 6, and none of them can see helicity 2 (checked). The density lemma (Lemma Z) does not carry over to pairs of momenta (proved). So WW fails copy by copy. But Zariski density makes any polynomial effective law on a copy Lorentz-invariant, and then WW applies to it, even with tuning. Reading: **OPEN**, leaning SUPPLIED-FORCED, conditional on such a law existing. Nobody has built one.
- **Set C (axioms' Z³, tuned).** WW proper is evaded, because there are no boosts. But its lattice (Hamiltonian) cousin is not evaded by Lorentz violation.
  - Suppose an emergent graviton's gauge rule is the full linearized coordinate change, and its energy is a sum of local gauge-invariant terms. Then it disperses as ω ∝ k² (checked numerically; prior art in N0914 and Xu–Hořava). Light-like gravitons need "weak" invariance.
  - On finite-dimensional sites, weak invariance adds nothing: averaging over the compact gauge group turns any gauge-invariant local Hamiltonian into a sum of individually invariant local terms (proved; checked on a Z₂ chain).
  - So the live N-type graviton cannot come from the microscopic Hamiltonian of a finite site. It needs one of four things:
    - a non-regular strong-coupling phase;
    - unbounded local variables (a Qubit price);
    - a smaller gauge group, which brings gapless partners;
    - kinematic non-locality (Marolf).

  If the graviton is there, universality comes free once matter has an exactly conserved local momentum. That momentum is the barrier (R6-1). Reading: **OPEN**.
- **The one-line answer.** No set produces a universally coupled graviton under the refereed walls. The nearest candidate is C with unbounded per-slot variables (named "C-N*" in §6). It is blocked at exactly the exact-momentum wall, and it pays at least one speed tuning.

---

## 1. Prior art, counted once

**In the repository and packet.**
- `B_referee.md:47` (WW premises and exits), `:48` (Marolf), `:154`, `:175` (holography as a WW/Marolf loophole).
- `OUTSIDE_VIEW.md:39` (WW and the soft theorem; with IR Lorentz invariance, the graviton is a gauge mode).
- `B1_report.md:138-150` (WW → Property G).
- `C5_O2_report.md:55-70` (Weinberg restated; WW corollary); the O2 referee says WW is a separate theorem (`C5_O2_referee.md:5`).
- `R0_report.md:128-145` (literature table: Gu–Wen, Xu, Xu–Hořava, Pretko, BCM, HHJM, Marolf, WW loopholes); `R0_report.md:99` (probe 13: "weak invariance adds nothing in lifted clock encodings"); `R0_report.md:168` ("the only linear ±2-only case is weak invariance on noncompact variables").
- `R2_report.md:151-162` (universality is forced by the vector Gauss law given conserved momentum; WW does not apply on the lattice); `R2_referee.md:38` (confirms that WW is correctly not used).
- Lane R and RN results, `TESTS:725-776`, `TESTS:836-895`.
- **N0914 (landed 09-14 note).** H_L (strong) gives ω² = Jg k⁶ and H_N (weak) gives ω² = Jg k² (`N0914:69-75`). The regular compact-character lemma: every local h-character is O(k²), so all frequencies are O(k³) (`N0914:186-216`). Its own scope note: "not a no-go for qubits, emergent nonlinear gauge symmetry or strongly interacting constraint phases" (`N0914:215-216`, `:396-397`).
- O2 Lemma W (`TESTS:2386-2389`); R2-6 (`TESTS:2741-2744`).
- No other repo hit for "Weinberg–Witten" outside this packet (git grep, docs/ included). `docs/SOFT_SPIN2_COLLISION_INVARIANTS_…_2026-09-14.md` is soft-theorem prior art, not WW.

**What is new here** (worker claim, to be refereed):
- (i) the discrete little-group lemma for Γ_L, with its crystallographic orders;
- (ii) the failure of Lemma Z for momentum pairs;
- (iii) the tensor-sector form count, which shows B's dimension-4 protection does not cover the graviton (the numbers coincide with K1's 11 = 3 + 8, `SUMMARY:418`; the WW reading is new);
- (iv) Lemma A, that weak invariance is empty on finite-dimensional sites. This answers the open "compact realization" item of `TESTS:759` and N0914 at the microscopic level only;
- (v) the finite-volume frame state for the B′ ensemble.

The HWW dispersion statement itself is **prior art** (N0914; Xu–Hořava; Gu–Wen). My numerics re-check it in a different (staggered) placement, with π–h cross terms included.

**Literature.**
- WW, PLB 96 (1980) 59 (V via `B_referee.md:47`).
- Jenkins, "Constraints on emergent gravity", IJMPD 18 (2009) 2249, arXiv:0904.0453 (**V**, abstract fetched): a theory without fundamental spin-2 gauge invariance "must either lack a stress-energy operator or have a non-relativistic graviton"; the latter conflicts with the equivalence principle.
- Jenkins hep-th/0409189 and hep-th/0607239 (V, search): the graviton as a Goldstone of spontaneous Lorentz violation evades WW.
- Kostelecký–Potting, PRD 79 065018, arXiv:0901.0662 (V, search): NG modes of a symmetric two-tensor obey linearized Einstein in a fixed gauge. The two-tensor carries a supplied massless-spin-2 kinetic operator.
- Marolf, PRL 114 031104, arXiv:1409.2509 (V, search): universal coupling to energy makes the Hamiltonian a boundary term on shell; with local kinematics the bulk freezes; this holds on lattices and needs neither Lorentz nor translation invariance.
- Carlip arXiv:1207.2504 (V via `OUTSIDE_VIEW:40`).
- Benedetti–Casini–Magán arXiv:2205.03412 (V, search; WW rederived in local QFT).
- Porrati arXiv:1209.4876 (V, search).
- Loebbert's WW essay (Annalen Phys. 2008): **M**; the search did not find it.
- Kraus–Tomboulis hep-th/0203221: **M**.

---

## 2. Hypotheses, stated before the per-set titles

**WW (comparator, as in `B_referee.md:47`, `B1_report.md:140-145`).**
- **(W1)** A unitary Poincaré representation with an invariant vacuum.
- **(W2)** Massless one-particle states |p, h⟩ with |h| = 2.
- **(W3)** A local, conserved, Lorentz-covariant T^{μν} with ∫T^{0ν} = P^ν on those states, i.e. a nonzero forward matrix element.
- **(W4)** Continuity of ⟨p′|T|p⟩ as p′ → p.

The proof uses the rotation R_θ that fixes both null momenta p ≠ p′ in their CM frame. On ⟨p′|T^{μν}(0)|p⟩ it acts by e^{2ihθ}, while on rank-2 tensors it has weights e^{imθ}, |m| ≤ 2. A boost to that frame has rapidity of order log(1/angle) and lowers the energies to √(−q²)/2 → 0, so the argument is an IR statement that uses large boosts.

**Universality (O2 Lemma W, refereed CWC, `TESTS:2386-2389`).** Decoupling of pure-gauge polarizations needs an additive collision invariant Q^ν on every channel.

**Setting (`TESTS:3066-3068`).** The four sets of `TESTS:2424-2426` and `:2647-2651`, with the minimal matter content of each set's refereed results. Graviton: any emergent massless helicity-±2 mode.

**Outside realizations this report excludes:**
- curved backgrounds;
- gravitons without an S-matrix (cosmological settings);
- massive gravity read as "a graviton" (a P0-type mass is a tuning, not production);
- higher-dimensional bulks except where named in §5(e);
- non-particle classical metrics, except to name them as an exit (that is R6-4's territory).

---

## 3. Checks and lemmas

### 3.1 Discrete little groups never see helicity 2 (proved; checked `r62_little_group.out`)

**Little-group table.** With a stabilizer C_n in place of SO(2), the matrix element is forced to vanish only if 2h ≢ m (mod n) for every |m| ≤ 2. For h = 2 that first happens at n = 7. The table:
- h = 3/2 is constrained at n ≥ 6;
- h = 2 at n ≥ 7;
- h = 5/2 at n ≥ 8;
- h = 3 at n ≥ 9.

**Γ_L = SO⁺(Q, ℤ), Q = 7n₀² − n₁² − n₂² − n₃².**
- Q has no integer null vector (brute force with n₀ ≤ 24; analytically, 7n₀² has the form 4^a(8b+7)).
- Take γ ∈ Γ_L that fixes two distinct real null vectors. Then its eigenvalue-1 space contains their span P. That eigenspace is rational, so P can be taken rational, and γ acts on the rational definite plane P^⊥ ∩ ℤ⁴. So γ has order 1, 2, 3, 4 or 6 (2D crystallographic restriction). Loxodromic elements rescale null vectors, and parabolic ones fix one null direction only.
- Explicit elements:
  - C₄ (rotation in n₂–n₃) fixes the pair (1, ±√7, 0, 0);
  - C₃ (cyclic n₁→n₂→n₃) fixes the pair (1, ±√(7/3)(1,1,1)).
- Integral automorphs of definite binary forms have orders {1, 2, 3, 4, 6} (enumerated).

**Conclusion (proved).** No element of Γ_L, and no element of the cubic real-time group of B or C (its pair stabilizers are C₂, C₃, C₄ about cubic axes), gives a WW constraint on h = 2. The per-realization phase argument is empty.

### 3.2 Lemma Z does not extend to momentum pairs (proved; standard)

- The stabilizer in G = SO⁺(1,3) of two non-collinear null vectors is compact (≅ SO(2)).
- A discrete Γ ⊂ G acts properly discontinuously on G/K for compact K. So Γ_L-orbits of non-collinear null pairs are discrete.
- Hence a Γ_L-covariant two-particle form factor F(p, p′) is constrained only on discrete orbits. Continuity cannot spread a constraint to Lorentz covariance.
- Lemma Z's density (`TESTS:2925`) uses the non-compact stabilizer MN of a single null vector. It controls dispersion, ⟨p|·|p⟩-type single-momentum functions, not WW's off-forward elements.

### 3.3 B's protection does not cover a rank-2 field (checked `r62_tensor_lv_counts.out`)

Quadratic forms of a symmetric tensor:

| Group | Mass forms | Kinetic symbol forms (k k h h) |
|---|---|---|
| W(B4), and also B4⁺ | 3 | 9 |
| SO(4) (Monte Carlo 1.99, 3.97; exact) | 2 | 4 |

- Both groups have Sym²V invariants = 1, i.e. V₂^tl = 0, which is the matter protection (`TESTS:2379`).
- So for h_μν the hypercubic law allows 1 extra mass form and 5 extra kinetic forms at dimension ≤ 4. This matches K1's gauge-restoration codimension 11 = 3 + (9 − 1) (`SUMMARY:418`; `TESTS:1663`).
- R3-2's Γ_L count (2 mass, 4 kinetic; `TESTS:2758`) equals the Lorentz count, as Zariski density requires.

### 3.4 Lemma A: weak gauge invariance is empty on finite-dimensional sites (proved; checked `r62_averaging_lemma.out`)

**Statement.** Let H = Σ_x h_x be uniformly local and commute with every local Gauss operator G_y. The G_y have bounded support and finite-dimensional site algebras. Then the closure K of the group they generate is compact. Define h̃_x = ∫_K U(g) h_x U(g)† dg. Only the finitely many factors of g that touch supp h_x matter, so h̃_x is local. It is individually invariant, and Σ_x h̃_x = ∫ U H U† = H.

**Consequences:**
- The non-invariant parts of a weakly invariant density sum to zero identically.
- For non-abelian G_y the same holds with the Haar measure of the compact closure.
- Noncompact (unbounded) local variables have no normalizable average. That is exactly where H_N lives (`N0914:72-82`).

**Check.** Z₂ gauge chain, L = 4 (8 qubits), translation-invariant densities on 4 consecutive qubits:
- weak solutions: dim 43; strong: dim 31; zero-sum densities: dim 15;
- dim(strong + zero-sum) = 43;
- every weak solution satisfies Σh_x = Σavg(h_x) to 0.0e+00.

### 3.5 HWW: strongly invariant local energy ⇒ ω = O(k²) (prior art; re-checked `r62_hww_dispersion.out`, `r62_hww_box5.out`)

**The model.** Staggered placement on Z³: h_ii on sites, h_ij on faces, ξ on links. The gauge is the full spatial linearized diffeomorphism δh_ij = ½(D_iξ_j + D_jξ_i), and π is gauge-invariant (vector Gauss law only).

**Results:**
- Every gauge-invariant local linear functional supported in boxes R = 3, 4, 5 (dims 15, 171, 171) has symbol O(ε^{1.999}) in all directions tested, with gauge residual ≤ 4e-16.
- Random strongly invariant positive Hamiltonians have π free, h entering only through those invariants, and a random π–invariant cross term. Their maximum physical frequency scales as ω ~ k^{2.000 ± 0.002} (3 trials × 2 directions).
- **Control.** The weakly invariant spatial linearized-Einstein form (residual |VG| ≤ 4e-23) gives ω ~ k^{1.000} on TT. Its symbol is O(k²), while every strongly invariant quadratic symbol is O(k⁴), so it is not strongly invariant.
- With the scalar (Hamiltonian) constraint also exact, the order is O(k³) (N0914 proved in its regular compact class; Gu–Wen L-type).

**Proof sketch for the linear statement.** N0914's Taylor argument (`N0914:203-208`). The analytic general version is the polynomial exactness of the elasticity (Kröner/Calabi) complex: invariants factor through the linearized curvature.

**Combined statement (A + HWW).** Assume:
- (a) a microscopic lattice with finite-dimensional sites;
- (b) an exact local Gauss law, or an emergent one in which microscopic local terms map to local gauge-invariant IR terms ("regular IR map");
- (c) the full spatial linearized-diffeo redundancy acting on the emergent h.

Then the emergent graviton disperses as ω ∝ k² (vector law) or k³ (both laws). The scope is SUGGESTED for (b) beyond N0914's regular class, and checked or proved in the Gaussian class.

**What this does not cover:**
- strongly coupled, non-regular IR maps (Gu–Wen N-type at strong coupling);
- smaller gauge groups;
- non-local Hamiltonians or kinematics.

**Observational status (comparator, M).** ω ∝ k² is excluded by GW170817 (c_g/c − 1 in [−3e-15, 7e-16]; `C5_O2_report.md:48`).

**This is WW's Hamiltonian face** (reading, consistent with Jenkins V and Marolf V). Local, observable, gauge-invariant gravitational energy is incompatible with a relativistic graviton, and the argument uses locality instead of Lorentz invariance. Lorentz violation alone therefore does not open the door.

---

## 4. Probe (a): WW hypotheses against each set's refereed low-energy content

| Hyp. | A (continuum + records) | B (Euclidean Z⁴, W(B4)) | B′ (LRL realization; ensemble) | C (Z³ × ℝ, proper cubic) |
|---|---|---|---|---|
| W1 Poincaré | Holds: A1 exact Poincaré (`C5_O5_synthesis.md:322-329`, set construction unrefereed). Flashes are covariant in law (rGRWf) | Fails exactly: the OS transfer matrix has Z³ × Z_τ ⋊ cubic only. Holds at dim ≤ 4 for matter (`TESTS:2379`), **not for h_μν** (§3.3) | Fails per realization: Γ_L ⋉ L₇ only; pair stabilizers ≤ C₆ (§3.1). Ensemble: G/Γ_L has finite Haar volume (cocompact, `TESTS:2713`), so the constant frame state is a normalizable Poincaré-invariant state (suggested; contrast Lemma H on H³, `C5_R5-1_referee_verdict.md:20`) | Fails exactly and in the IR (preferred frame, `SUMMARY:394`) |
| W2 massless h = 2 states | The would-be graviton | Would-be | Per realization there is no continuous covariant momentum in the conservative class (`TESTS:2915-2916`), so no Poincaré particle label | Would-be; lattice helicity defined only up to C₄ |
| W3 covariant conserved T, ∫T^{0ν} = P^ν | Holds for a Lagrangian A3 QFT (Belinfante; comparator). Not proved for every microcausal A3 law. Flashes give ∂_μT^{μν} = J^ν ≠ 0, stochastic and rate-bounded (`TESTS:2722-2726`) | Matter T covariant at dim 4. Momentum conserved only mod G (lattice); exact additive charge forces an infinite fibre (`TESTS:2748-2751`, bounded) | Per realization: quasi-momentum mod reciprocal; multiparticle umklapp (`TESTS:2791`); no covariant finite-fibre charge (`TESTS:2915`). Polynomial EFT, if it exists: covariant by Zariski (`TESTS:2788`) | Fails: no conserved lattice momentum density for interacting single-band d ≥ 2 matter (`TESTS:2386-2394`; RN-L2 `TESTS:857-858`) |
| W4 forward continuity | Standard | Standard in the EFT | 1→1 silence below the gap (`TESTS:2718`); q → 0 is in-gap | n/a |
| Soft universality (Lemma W) | Holds (Weinberg) given A5 | Needs an exact additive charge → infinite fibre (bounded) | Umklapp channels violate additivity; only Example E carries a charge (`TESTS:2917`) | Needs an exact momentum density (§5(d)) |

---

## 5. Probes (b)–(e)

### (b) B′ specifics

1. **Does WW go through with Γ_L alone, using Zariski density and Lemma Z?**
   - **Pointwise: no** (proved, §3.1–3.2). Pair little groups are C_{1,2,3,4,6}, and none constrains h = 2. Γ_L acts properly on momentum pairs, so Lemma Z's density does not reach the off-forward element.
   - **Via Zariski: yes, conditionally** (suggested; the counts are refereed). Suppose a per-realization effective law exists with a polynomial (q²) expansion. Then every polynomial invariant is Lorentz-invariant (`TESTS:2788`). Its quadratic graviton sector has the Lorentz counts 2 + 4 (`TESTS:2758`), and its Noether T is covariant at every polynomial order. So WW applies to that effective law.
   - **That is stronger than in B.** In B′ even a tuned non-gauge massless spin-2 composite is forbidden; in B a tuned one escapes through the hypercubic tensor forms (§3.3).
   - **Correction to the expectation's mechanism.** Zariski density, not Lemma Z, does the work.
2. **Does multiparticle umklapp spoil the covariance of the forward matrix element? No** (reading, from refereed facts).
   - WW uses only one-particle matrix elements with transfer q → 0, inside the gap, where 1→1 processes are silent (`TESTS:2718`).
   - Umklapp breaks exact covariant conservation only in multiparticle sectors whose total transfer is reciprocal (`TESTS:2791`).
   - It does hit Lemma W. Soft decoupling needs additivity on every channel, so umklapp attacks **universality**, not WW.
3. **The ensemble route closes the door rather than opening it** (suggested). If the frame is a quantum variable (R5-5, pending), the invariant frame state is normalizable (finite-volume G/Γ_L), so W1 holds exactly for the whole system. WW then binds the frame-averaged theory, provided a covariant T exists.

**B′ reading: OPEN, leaning SUPPLIED-FORCED.**
- What is missing is the per-realization law: R4-1 is a bounded FAIL for finite orbits (`TESTS:2906`), and R5-2 is pending.
- Per realization, neither WW's premise nor the universal-coupling premise holds in the conservative class. The only charge carrier is the continuum hyperboloid, which is set A.

### (c) B specifics: is dimension-4 protection with dimension-6 breaking enough for WW?

**For matter's T: yes.** The matter T is Lorentz-covariant at dimension 4 (`TESTS:2379`).

**For the graviton sector: no** (checked, §3.3). W(B4) and B4⁺ allow 3 mass and 9 kinetic tensor forms, against Lorentz's 2 and 4. Two branches follow:
- **(B-g) Gauge-protected h.** The only gauge-invariant W(B4) kinetic form is the EH one (K1), so the graviton sector is Lorentz-invariant at dimension 4 and c_g = c needs no tuning. WW then holds in the IR effective law, so the graviton is a gauge field there, not a composite carrying energy through the covariant matter T. Can that gauge field emerge from B's finite sites?
  - Not with a regular IR map (§3.4–3.5).
  - The exact-charge route collapses to A (R2-1, bounded, `TESTS:2748-2751`).
  - Any positive local linear source bridge gives γ ≤ ½ (`TESTS:2729-2731`).
- **(B-t) Not gauge-protected.** WW is evaded by the 1 extra mass form and the 5 extra kinetic dimension-4 forms. This is Jenkins' "non-relativistic graviton" branch. The prices:
  - K1's 11 tunings (`SUMMARY:418`), a cosmological-tadpole tuning separately;
  - no universal coupling without an infinite fibre (R2-1).

**B reading: OPEN.**
- It is SUPPLIED-FORCED conditionally, if c_g = c and masslessness are to be untuned (B-g).
- WW's hypotheses are not shown to hold unconditionally, because branch B-t evades them.

### (d) C specifics

**WW proper is evaded.** There are no boosts, exactly or in the IR tensor sector.

**Its Hamiltonian face is not evaded** (§3.4–3.5). An emergent graviton with the full linearized-diffeo redundancy, built from finite-dimensional sites with a regular IR map, has ω ∝ k² or k³, which observation excludes. The routes to a linear, ±2-only graviton:
1. **Gu–Wen N-type at strong coupling** (non-regular IR map). Open; the authors call it "not reliable" (`R0_report.md:131`).
2. **Unbounded local variables carrying H_N exactly** (N0914; `TESTS:759`). This is a Qubit price (`AX:47`).
3. **A smaller gauge group** (scalar charge, or S/S-tl). TT is linear, but ±1 and 0 partners are gapless with independent speeds. The charges are fractonic, and energy cannot be the charge. Refereed FAIL on (iii) in the linear-coupling class (`TESTS:752-753`; `R2_report.md` table).
4. **Kinematic non-locality** (Marolf, V; it bites beyond linear order).

**Universality is not the barrier.** Given an exactly conserved local momentum density, the vector Gauss law ∂_iE_ij = Σκ_s P_s,j is preserved only if κ_s = κ, whenever species exchange momentum (`R2_report.md:152`, proved, elementary). The barrier is the exact momentum density itself:
- regular single-band interacting d ≥ 2 matter has none (RN-L2, `TESTS:857-858`);
- C3 boost closure (`SUMMARY:397-412`);
- C4's six appearances.

The class-wide version is R6-1's question.

**Newtonian half.** It needs the scalar constraint with a gauge lapse. Lapse-only coupling FAILs on γ and Shapiro (`TESTS:865`).

**Minimal speed tunings (the graviton–matter Collins split, `TESTS:719`).**
- At least 1 relative graviton–matter speed. GW170817 gives −3e-15 ≤ Δc/c ≤ 7e-16 (`C5_O2_report.md:48`). An emergent speed is set by lattice couplings, so its natural size is O(1): comparator M (the spin-ice c = √(UK)·a₀, `R0_report.md:141`). That is about 15 decades.
- The local codimension is 3, or 4 without P/T (`TESTS:757`, a refereed count; the lane itself is INCONCLUSIVE).
- On top of that, matter's N − 1 speeds: one instance at 3e-17 (`TESTS:2380`).
- P0's two TT masses return only if the matter coupling breaks the redundancy (`TESTS:756`).

**C reading: OPEN.** The expectation said "WW is evaded by Lorentz violation, and universal coupling is the barrier". Corrected:
- Lorentz violation evades WW but not its Hamiltonian face.
- The barriers are (1) linear dispersion from finite sites, which needs strong coupling or a Qubit price, and (2) the exact momentum density, not universality as such.

### (e) Exits: which set could host each, and at what price

| Exit | Hosts | Price (named, not adopted) | Status |
|---|---|---|---|
| Graviton as a gauge field with non-covariant (pseudotensor) energy | Any set, as a supplied field (A5). Emergent only in C via routes 1–2 of (d) | A: primitive A5. C: Qubit `AX:47` (unbounded slots) or a strong-coupling phase. In C/B also an exact matter momentum density (R6-1) | The standard exit. Emergence is OPEN only via the non-regular route |
| Holography (the graviton lives in a bulk) | None as defined. The substrates are 3+1-dimensional, so a bulk would be 4+1 | Lattice `AX:37` (Z³ → a 2D boundary substrate) and an AdS bulk (Λ < 0, against the observed Λ > 0); dS holography is unestablished (comparator M) | Not available without a Lattice dimension change |
| Non-particle gravity (classical metric, no graviton pole) | A (CQ / records-as-metric) | Record and A5-type changes; decoherence–diffusion bounds | Not a graviton; R6-4's question |
| Spontaneous Lorentz violation: graviton as a Goldstone (Kraus–Tomboulis M; Jenkins V; Kostelecký–Potting V) | A only by breaking A1's invariant vacuum. B′/C have explicit, not spontaneous, breaking | A supplied symmetric tensor with a massless-spin-2 kinetic operator (KP), so this is supplied. Jenkins: LV in the graviton's energy-momentum, in tension with the equivalence principle | Supplied in disguise |
| Non-covariant T from explicit LV (Jenkins' non-relativistic graviton) | B (tensor forms, §3.3), C | B: K1's 11 tunings. C: ω ∝ k² unless strong coupling; speed tunings | Tuned |
| Induced (Sakharov) gravity | All | Metric supplied; only its action is induced | Production of the dynamics, not of the field (reading) |
| Kinematic non-locality (Marolf) | B′ (non-summable invariant couplings, `TESTS:2785`) or a non-local C | Admissibility `AX:57` ("nearest-neighbor") | OPEN; no construction |

---

## 6. The best producing mechanism found, and why it is not PRODUCIBLE

**Candidate C-N\*** (set C plus prices):
1. unbounded rotor variables per tensor slot (Qubit price, `AX:47`);
2. exact vector and scalar Gauss laws, read as Admissibility's nearest-neighbour **support** rule. Reading: `AX:63-73` makes "admissible" the support of the per-site distribution, so a hard local constraint sits in that text, as the ice rule does at `R0_report.md:96`;
3. the weakly invariant H_N.

**What it gives, all prior art.** Two linear TT modes, no partners, and an attractive 1/r response to a supplied energy source (N0914; `TESTS:759`). Exact gauge invariance removes TT masses (`TESTS:755`). Universality comes free once a conserved momentum density exists.

**What it lacks:**
- (i) an exactly conserved local momentum density for interacting matter on Z³ (blocked in every bounded class tried; R6-1 class-wide);
- (ii) at least 1 graviton–matter speed tuning;
- (iii) a reason the observable energy density is not local. Record's "only records are readable" (`AX:82-83`) is compatible with that (reading).

Under the fixed reading it is not PRODUCIBLE, because universal coupling to matter's energy-momentum is not established.

**Lemma A sharpens the Qubit price.** On finite-dimensional sites this mechanism can arise only through a non-regular strong-coupling phase, never from the microscopic Hamiltonian's form.

---

## 7. Readings against the FIXED readings, `TESTS:3086-3089`

| Set | Reading | Basis | Expectation (`TESTS:3090-3094`) |
|---|---|---|---|
| **A** | **SUPPLIED-FORCED** (referee required) | W1–W4 hold for A's Lagrangian Poincaré QFT; flashes are inert and classical (`TESTS:2722-2726`); every exit changes A's defining premises (§5(e)) | Met |
| **B** | **OPEN**. Conditional SUPPLIED-FORCED if c_g = c and masslessness are untuned | §3.3: W(B4) does not protect h_μν, so branch B-t evades WW at the K1 price; universality is blocked by R2-1 (bounded) | "SUPPLIED-FORCED at the IR level, or OPEN": OPEN, with the correction that dimension-4 protection does not extend to the tensor sector |
| **B′** | **OPEN**, leaning SUPPLIED-FORCED, conditional on a per-realization polynomial law | §3.1–3.2: the pointwise WW argument is empty. Zariski density makes WW bite on any polynomial law, even tuned. No law exists yet | Met. Mechanism corrected: Zariski density, not Lemma Z |
| **C** | **OPEN** | WW is evaded, but its Hamiltonian face (§3.4–3.5) forces strong coupling or a Qubit price. Exact momentum is the barrier (R6-1). At least 1 speed tuning | Met. Barrier corrected: momentum and dispersion, not universality |

**No set is PRODUCIBLE.**

**Referee required:**
- A's SUPPLIED-FORCED;
- the no-go-type Lemma A and the §3.1 orders lemma, which are used to narrow B, B′ and C. Neither is used as a FAIL reading.

---

## 8. Scope and strong-word check

- **"Never constrains h = 2"** holds for stabilizer orders in {1, 2, 3, 4, 6}. Those are all the orders possible for Γ_L pair stabilizers and the cubic real-time groups (proved). It says nothing about continuous emergent symmetries.
- **"Weak invariance adds nothing"** is proved only for finite-dimensional sites with bounded-support Gauss operators and uniformly local terms. It does **not** cover:
  - unbounded variables;
  - energetically (not exactly) imposed Gauss laws, where it holds only after projecting to the low-energy space with a regular IR map (suggested);
  - non-regular strong-coupling phases.
- **HWW** is checked for Gaussian strongly invariant Hamiltonians in one staggered placement, for box supports up to R = 5. The general analytic statement is N0914's (regular compact class) and the Calabi-complex factorization (comparator M).
- **The finite-volume frame state** is standard for a lattice Γ_L (cocompact). That it rescues W1 for the ensemble presumes a frame Hilbert space (R5-5's construction), so it is suggested.
- **A's W3** (a covariant T) is assumed for Lagrangian A3 laws. A microcausal law without a stress tensor is an A6-type exit, not shown impossible.
- **Not shown:**
  - that strongly coupled qubit phases cannot realize N-type;
  - a class-wide momentum no-go (R6-1);
  - any observable numbers for the C-N\* speed tuning beyond the GW170817 band.
