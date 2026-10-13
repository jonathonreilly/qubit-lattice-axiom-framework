# C5 R19-3 report: (S) as a quantum statement (J2). Is the graviton's own zero-point stress absorbed by (S) and (d-i) in every gauge?

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Unrefereed.** Run 2026-10-13, 03:50Z to about 04:40Z. No repository file was edited. Nothing was downloaded.

**Scratch folder.** `S/` = `.../scratchpad/C5/R19-3/`. Every script ran in under 40 s at `OMP_NUM_THREADS=2`.
- `S/scripts/r193_onepoint.py` / `.out`: per-mode one-point stress, on shell, TT vs harmonic Feynman–de Donder (FdD); k along z and along x.
  - `r193_onepoint_v0_unhalved.out` is the first run. It set the phase average ⟨f′²⟩ to 1 instead of ½, so every number in it is 2×. It is kept only as a record. The fixed run is `r193_onepoint.out`.
- `S/scripts/r193_gauge_family.py` / `.out`: off-shell symbolic k; kinetic matrices; the harmonic family over ξ by residues; the gauge-fixing Hilbert stress; the background-field total.
- `S/scripts/r193_beta_family.py` / `.out`: the gauge condition varied, F_ν = ∂^μh_μν − β∂_νh, with β ∈ {1/3, 1/2, 3/4, 2} and ξ ∈ {1, 3}.
- `S/scripts/r193_lemmaD.py` / `.out`: the pure-gauge cross term for arbitrary X and off-shell k, at density weights 0, 1 and 2.
- `S/scripts/r193_LLcheck.py` / `.out`: the explicit Landau–Lifshitz formula (MTW 20.22, RECALLED) against the LL identity, exactly.
- `S/scripts/r193_relaxed.py` / `.out`: literal N's harmonic source term t_H.
- `S/scripts/r193_C_zeropoint.py` / `.out`: Gupta–Bleuler zero-point bookkeeping.
- `S/scripts/r193_lattice.py` / `.out`: the box-regulator sums, v_max, cubic covariance, and sizes.
- `S/recheck/`: the archived R18-6 (2), R17-11 (4) and R17-7 (5) runners, copied together with R11-3 (an import dependency) and R9-9 (profiles), then rerun. **All 11 reproduce their stored `.out` byte for byte** (`S/recheck/run_all.log:1-11`).
- SHA-256 of every `.out`: `S/scripts/SHA256SUMS` (recompute with `shasum -a 256 -c`).

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`
- `TESTS` = `P/TESTS.md`
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`
- `rX` = `P/agents/C5_X_report.md`; `vX` = `P/agents/C5_X_referee_verdict.md`; `refX` = `P/agents/C5_X_referee.md`
- `S26` = `P/agents/C5_S26_synthesis.md`

**Read.**
- In full: `AX`; the C5 method (`TESTS:2302-2320`); the Round 19 head and the R19-3 item (`TESTS:7114-7253`); the Round 17 and 18 heads (`TESTS:5685-5720`, `6392-6420`); the R18-6 item (`TESTS:6682-6711`); vR18-6, refR18-6 and rR18-6; vR17-11, vR17-7 and vR9-9.
- In part: rR17-7 §4(b) (`170-215`); vR11-3 (`30-60`); rR9-9 (`1-140`); `S26` (J2 lines `77`, `161`, `186`, `278`, `413`, `501`, `773-806`); rR16-14 (`68`, `143`); rR18-11 (`1-180`; worker, referee running); refR18-7 (`3-39`).

**Labels.** Each claim carries one of:
- proved: derived here under stated hypotheses;
- checked: an exact or numerical result in a `.out` of this run;
- suggested: argued, not proved;
- reading: interpretation;
- comparator: literature, RECALLED, or via an earlier referee.

**Subtraction rule.** Every remainder is measured against e_g, the TT zero-point energy density. That is what (S) subtracts when the graviton sector is inside the H that defines e₀ (P136(ii), `vR18-6:7`). Nothing else is subtracted.

---

## 0. Reading against the FIXED readings (`TESTS:7242-7245`)

**Worker reading: J2-GAUGE-BRIDGE (needs the referee).** On the literal reading, J2-ABSORBED fails: two of the three registered stress definitions, (A) and (B), leave a non-absorbable remainder in harmonic gauge. NEITHER is not met: the gauge-independent objects have no remainder.

**Per-mode one-point stress.** Each entry is t_μν = c · k̃_μk̃_ν/ω per spatial mode, with k̃ = (ω(q), d(q)) null. Here c = 1 is exactly the TT zero point, 2 × ω/2.

| Treatment | (A) ⟨(−g)t_LL⟩ | (B) −⟨G^(2)_μν⟩/8πG | (C) Hamiltonian zero point | (A′) −⟨[√−g G^{μν}]^(2)⟩/8πG |
|---|---|---|---|---|
| Reduced phase space (TT) | 1 | 1 | 1 | 1 |
| Coulomb/Poisson gauge (canonical) | 1 | 1 | 1 | 1 |
| Harmonic (de Donder, β = ½), any ξ, incl. ξ → 0; FP ghosts | **2** | **4** | 1 (10 − 8 count) | 1 |
| Other linear gauges, β = ⅓, ¾, 2 (ξ = 1, 3) | **7/4, 3, ½** | **17/4, 3, 11/2** | not computed | 1 |
| Harmonic: EH + gauge-fixing + ghost Hilbert stress (background field) | — | — | — | 1 + 4 − 4 = 1 |

Sources: `r193_onepoint.out:2-11,24-33`; `r193_gauge_family.out:9-22`; `r193_beta_family.out:9-16`; `r193_C_zeropoint.out:1-3`.

**What the remainder is.**
- After summation, every entry has the form ρ nn + p h with p = ρ/3 (`r193_lattice.out:4-6`).
- Under (S) + (d-i), the leftover is a Λ-type term, Λ̃ = κ(c − 1)e_g.
- In harmonic gauge it is 3e_g for (B) and e_g for (A), i.e. 6.4e123 and 2.1e123 ρ_Λ at a = ℓ_P (`r193_lattice.out:10-12`). It is zero in TT and Coulomb gauge. Its size and sign depend on the gauge condition β, but not on the gauge weight ξ.
- **Literal N's own harmonic-gauge source** is τ = (−g)(T + t_LL) + t_H (`rR16-14:68,143`). Its vacuum value is (2 + ξ)e_g: ξ-dependent, and 2e_g at exact harmonic gauge (`r193_relaxed.out:4-5`).

**Why this is the gauge-bridge reading.**
- The non-absorbable part depends on the gauge and on the pseudotensor (density-weight) choice. That is the J2-GAUGE-BRIDGE clause.
- The bridge it needs can be named, and it costs no number. Read the gravitating quantum one-point source as the **weight-1 density √−g G^{μν}**, i.e. the metric variation of the action: (A′), or equivalently the background-field total.
- Lemma D (§4.3, proved) shows that this one object ignores every pure-gauge part of the vacuum two-point function. It equals the TT value in every gauge whose Wightman function differs from TT only by pure-gauge-factor terms (checked in 8 + 2 gauges).
- Under that bridge, the graviton's zero point is absorbed:
  - e = e_g = ⟨ω⟩_BZ = 2.447/a⁴, which (S) removes;
  - W_g = 4e_g/3 = 3.263/a⁴, which (d-i) absorbs (`r193_lattice.out:4-6`);
  - no remainder, no number.
- "Refereed demonstration" is not met by a worker run; hence "needs the referee".

**Fork check (Exhaustive forks rule, `TESTS:7123`).**
- J2-ABSORBED (literal): no. (A) and (B) fail in harmonic gauge.
- J2-GAUGE-BRIDGE: yes (worker).
- NEITHER: no. The gauge-independent objects (A′), (C) and the background-field total have zero remainder.
- OPEN would apply only if the referee rejects Lemma D or the harmonic-gauge numbers.

---

## 1. In plain words

- **The question.** If gravity is quantum, empty space holds graviton zero-point jitter. The rule (S) says the lowest state weighs nothing. The rule (d-i) hands the grid vacuum's leftover pressure to the site-making sector. Do these two rules also remove the gravitons' own jitter, whatever coordinates are used to describe it?
- **The energy that (S) removes is unambiguous.** Counted as the energy of the lowest state, the jitter is two polarizations × ½ħω per mode in every treatment. In harmonic gauge the 8 ghost modes cancel 8 of the 10 field components exactly.
- **The stress that "gravitates" is not unambiguous.** Its value depends on which formula for gravity's own stress is used, and on the gauge:
  - In the TT and Coulomb descriptions, the Landau–Lifshitz pseudotensor, the Isaacson average and the energy all agree.
  - In harmonic gauge, the Isaacson average counts the jitter 4 times and the Landau–Lifshitz pseudotensor twice. Other gauges give other multiples, up to 5½ and down to ½.
  - The surplus would act like a Planck-sized cosmological constant, about 1e123 times the observed one.
- **One formula is gauge-blind.** The stress as it appears in Einstein's equation written with the volume factor √−g (the derivative of the action with respect to the metric) gives exactly 1× in every gauge tested. There is a short proof of why: it is the only density weight for which unphysical, pure-coordinate jitter cancels. With that reading, (S) removes the jitter's energy and (d-i) its pressure, with no number to tune.
- **So J2 is not automatic, but it is cheap.** The bridge must say which stress gravitates for quantum states. The natural choice is the action's metric derivative. The Landau–Lifshitz pseudotensor in harmonic gauge would not do: as literal N uses it, it double-counts the graviton zero point.

---

## 2. Hypotheses and setting (stated before titles)

- **H-grav (R9-9's box graviton).**
  - N0914's H_N with the derivative symbol d(q) = ρ(q)q + (1 − ρ(q))·2 sin(q/2) per axis, with ρ = 1 on |q| ≤ 1 and 0 on |q| ≥ 2.5 (`rR9-9:35-41`; archived `scripts/C5/R9-9/r99_graviton.py:19-21`). Jg = 1.
  - Every N-type identity is algebraic in commuting real symbols (`vR9-9:5`). So each lattice mode q is a continuum linearized-gravity mode at spatial wave vector d(q), with continuous time: ω(q) = |d(q)|, two TT modes.
- **Whole-zone v_max (gauge field rule, `TESTS:7120`).**
  - v_max = max|∂_qω| = max d′ = **1** (checked to 2.5e-10, `r193_lattice.out:1,14`). It is attained on the box. The edge is slower, with d′ → 0 at the zone face.
  - In harmonic gauge all 10 components and the ghosts share this symbol, so v_max = 1 for every field here.
- **H-V3 (forward vertex; the only lattice input beyond H_N).**
  - The quadratic stress operators G^(2), t_LL, t_H and the gauge-fixing term are evaluated at zero total momentum with each spatial derivative replaced by i d_a(q). This is "symbol substitution".
  - The lattice graviton's own cubic vertex is W7's open degree-3 item (`S26:405`, `rR18-6:102`). H-V3 is a stipulation (P-r193b).
  - Locality: it inherits R9-9's non-analytic symbol, with super-polynomial tails, so it is quasi-local, not Lemma-M local (`rR9-9:93-95`). Lemma M was not tested.
- **Vacua.** Each is quasi-free (Gaussian), with symmetric (Weyl) ordering, and is evaluated as an operator (Wightman) expectation.
  - Contact terms polynomial in k₀, i.e. instantaneous propagator parts, have no on-shell support and are dropped by the residue rule (§4.1).
  - The q = 0 sector is excluded: the six torus moduli h_ij(q = 0) have no normalizable ground state and are measure zero in the infinite-volume limit. The global Hamiltonian constraint is replaced by R14-5's λ (H-imp, `rR18-6:60`).
- **Three treatments.**
  - **(T) Reduced phase space.** TT only.
  - **(H) Harmonic gauge.** F_ν = ∂^μh_μν − β∂_νh with β = ½ and Gaussian weight 1/(2ξ). ξ = 1 is Feynman–de Donder (FdD); ξ → 0 is exact harmonic. Gupta–Bleuler vacuum, FP ghosts. Also the off-harmonic members β = ⅓, ¾, 2, as a gauge-condition scan.
  - **(K) Coulomb/Poisson gauge**, canonical: the constrained components are solved as operators.
- **Stress definitions.**
  - (A) ⟨(−g)t_LL^{μν}⟩, a weight-2 density.
  - (B) Isaacson-type −⟨G^(2)_μν⟩/8πG, weight 0.
  - (C) the Hamiltonian zero point.
  - Added, and reported as a new object (Literal first, `TESTS:7124`): (A′) −⟨[√−g G^{μν}]^(2)⟩/8πG, weight 1, the EH part of the background-field (Hilbert) stress.
- **Signs of law data (`TESTS:7125`).** No law-data weights enter. β and ξ are gauge choices, not law data.
- **Excluded** (as registered, `TESTS:7232`): graviton self-interaction beyond one loop; matter; backreaction. Also excluded here: axial or nonlinear gauges; the Lagrangian (path-integral) Coulomb gauge's δ(0) contact terms; ghost stress for β ≠ ½ (non-minimal ghost operator).

## 3. Prior art (each counted once)

- **R18-6, vR18-6, refR18-6.**
  - J2 as stated: isotropy needs cubic invariance; the virial covers only free gauge-fixed TT modes (`vR18-6:7`; `refR18-6:30`).
  - C1 (isotropy check) and C2 (the per-mode virial), rerun identical (`recheck/R18-6/r186_vacuum_parts.rerun`).
  - This run replaces C2's virial argument by the explicit second-order tensors, in all three treatments.
- **R17-11 and vR17-11.**
  - The exchange current Q = ∇(W h). Any smooth isotropic grid enthalpy W h is absorbed in class 𝒟 (`vR17-11:5-20,44-45`).
  - Used as is: W_g here is one more such W.
- **R17-7 and vR17-7.**
  - E₀ includes every band's zero point by definition (`vR17-7:16-21`).
  - The grid vacuum's residual is (0, ρ₀ + p₀).
  - The same structure holds here, with ρ₀ + p₀ → W_g.
- **R11-3 and vR11-3.**
  - Lattice zero-point stresses have w ≥ 0, with two invariants (ρ, p) under the cubic group × time (`vR11-3:30-45`).
  - Here the graviton gives w = 1/3 exactly under H-V3, because ω = |d| (`r193_lattice.out:4-6`).
- **R9-9 and vR9-9.** The box graviton and its symbol (`vR9-9:5`).
- **R18-11** (worker; referee running; `rR18-11:134-146`).
  - Theorem G: a record insertion is readout-gauge independent iff it is a weight-1 contravariant density (a = 2, √−g T^{μν}).
  - This is the **same mechanism** as Lemma D here, in a different object: matter-record noise in set A versus the gravitational self-stress here. It is counted once. Nothing here relies on R18-11's unrefereed claims.
- **R16-14 and R18-7 (refR18-7).** Literal N's source is τ = (−g)(T + t_LL) + t_H in harmonic gauge (`rR16-14:68,143`; `refR18-7:39`).
- **Comparators (RECALLED).**
  - Isaacson effective stress (MTW §35.15);
  - the Landau–Lifshitz pseudotensor and identity (LL §96; MTW 20.20-20.22; the explicit formula is verified here, `r193_LLcheck.out:2`);
  - the Poisson–Will relaxed equations with t_H;
  - FP counting for the graviton (10 − 2·4);
  - BRST quartets (Kugo–Ojima);
  - on-shell gauge independence of the one-loop effective action (DeWitt; Kallosh–Tarasov–Tyutin);
  - the background-field de Donder action ('t Hooft–Veltman).
- **Repository grep.**
  - `P/` was grepped for isaacson, pseudotensor, t_LL, Landau–Lifshitz, graviton zero-point, Gupta, Faddeev, ghost, background-field.
  - No prior computation of the graviton's own one-point stress across gauges was found. The hits are classical LL uses (R16-14, R18-7), R18-11's Theorem G, and the J2 statements above.

---

## 4. Results

### 4.1 Method (probe (a)). Exact symbolic; checked

- **Expansion.** Write g = η + s h, with h_μν = e_μν f(k·x) for one Fourier mode and a real polarization e. Derivatives act by the chain rule on f, f′, f″. Expand to O(s²): G_μν; the densities (−g)G^{μν} and √−g G^{μν}; √−g R; the gauge-fixing Lagrangian.
- **Phase average.** Average over the phase with f = cos: ⟨f′²⟩ = ½ and ⟨f f″⟩ = −½. This kills every total derivative exactly.
- **Wick contraction.** Each quadratic form in e is contracted with the gauge's polarization covariance.
- **Covariances.**
  - TT for the reduced and Coulomb treatments.
  - For gauge (β, ξ): Cov = c·K(k)⁻¹, where K is the EH + GF kinetic matrix. Normalization: c K⁻¹(k₀² − k²) = P_FdD at β = ½, ξ = 1 (checked entrywise, `r193_gauge_family.out:6`).
- **Expectation rule.** The symmetric Wightman expectation per spatial mode is Res_{k₀=ω}[Q(k₀)·Cov(k₀)]. Double poles are the m²-derivative of the massive Wightman function.
  - At ξ = 1 this reproduces the on-shell evaluation: the same 4, 2 (`r193_onepoint.out:8,10` vs `r193_gauge_family.out:9`).
  - Instantaneous (k₀-polynomial) parts have no residue.
- **Calibration.**
  - TT gives t_00 = 1 per mode in units of ω/V, i.e. 2 × ω/2, the Hamiltonian zero point (`r193_onepoint.out:3`).
  - This is checked directly from G^(2), not assumed from the virial.
- **(A) is the LL pseudotensor.**
  - The identity (−g)t_LL = (1/16πG)∂∂H − (−g)G/8πG has ⟨∂∂H⟩ = 0 in any translation-invariant state.
  - The identity agrees exactly with the explicit MTW (20.22) formula (difference 0, exact rationals, off-shell k, random polarization; `r193_LLcheck.out:1-2`).
  - Scope: single-wave (rank-1 derivative) configurations, which are exactly what a forward vacuum expectation uses.
- **Sanity checks.**
  - Pure gauge alone gives zero for every definition (`r193_gauge_family.out:3-5`; off shell, `r193_lemmaD.out:3-5`).
  - Pure gauge × TT gives zero on shell (`r193_gauge_family.out:3-5`).

### 4.2 The per-mode tensors and their sums (probes (a), (b))

- **Per mode, every treatment and definition gives t_μν = c·k̃_μk̃_ν/ω exactly.** k̃ is null. This is checked for k along z and along x, all 16 components (`r193_onepoint.out:3-11,25-33`; "pure kk: True" in every row of `r193_gauge_family.out` and `r193_beta_family.out`).
  - So k̃^μ t_μν = 0 per mode: each per-mode one-point tensor is forward-conserved (the Vertex conservation rule, `TESTS:7131`, read for one-point tensors).
- **Cubic invariance of each vacuum (proved; checked).**
  - Each vacuum is the Gaussian state fixed by a covariance built from η, k̃(q) and, for TT, the transverse-traceless projector on d̂(q).
  - d(Rq) = R d(q) for all 48 signed permutations (checked to 6.7e-16, `r193_lattice.out:3`). So every covariance is invariant under the 24 proper rotations, and the state is invariant, not merely covariant.
  - This holds for TT (unique Fock vacuum of a cubic-invariant positive H), for Coulomb (TT only at linear order), and for the indefinite FdD and (β, ξ) Gaussian states.
  - Consequences:
    - T^{0i} = Σ d_i = 0, since O has no invariant vector and d is odd;
    - T_ij ∝ δ_ij, with anisotropy 1.4e-16 (`r193_lattice.out:4-6`).
- **Box sums (checked, N = 96, 160, 256; stable to 1e-8).**
  - e_g = ⟨ω⟩_BZ = **2.44707/a⁴**.
  - p = ⟨|d|²/3ω⟩ = e_g/3 exactly, because ω = |d|.
  - **W_g = 4e_g/3 = 3.26276/a⁴** (`r193_lattice.out:4-6`).
  - 98.7% of e_g is carried by the edge (|q_a| > 1 on some axis) (`r193_lattice.out:7`).
  - At a = ℓ_P: e_g = 2.1e123 ρ_Λ and W_g = 2.9e123 ρ_Λ (ρ_Λ RECALLED; `r193_lattice.out:10`).
- **Pressure is a convention; energy is not (reading).**
  - If the uniform strain acts on the lattice spacing rather than through the symbol, p = ⟨q·∇ω⟩/3 = 0.391/a⁴ instead of 0.816/a⁴ (`r193_lattice.out:8`).
  - Only W changes, and (d-i) absorbs any W.
  - The energy component, which (S) must match, is the same under both.

### 4.3 Decomposition and remainder (probes (b), (c))

**Decomposition.**
- Each summed stress is ρ nn + p h = −ρ g + (ρ + p)h in the lattice frame.
- In the bridge's terms (R18-6 §2.1, `rR18-6:63-72`): (d-i) receives W = ρ + p; (S) subtracts e₀ ⊃ e_g.
- What is left is −(ρ − e_g)g, i.e. **Λ̃ = κ(c − 1)e_g**.

| Gauge | c_A | c_B | c_A′ | c_C | Remainder for (A) | Remainder for (B) |
|---|---|---|---|---|---|---|
| TT, Coulomb | 1 | 1 | 1 | 1 | 0 | 0 |
| Harmonic β = ½, any ξ | 2 | 4 | 1 | 1 | e_g (2.1e123 ρ_Λ at ℓ_P) | 3e_g (6.4e123 ρ_Λ) |
| β = ⅓ | 7/4 | 17/4 | 1 | — | ¾e_g | 13/4 e_g |
| β = ¾ | 3 | 3 | 1 | — | 2e_g | 2e_g |
| β = 2 | ½ | 11/2 | 1 | — | −½e_g | 9/2 e_g |

Sources: `r193_beta_family.out:9-16`; `r193_gauge_family.out:9-15`.
- The remainder is **not gauge independent**. Within the linear covariant family it depends on the gauge *condition* β but not on the weight ξ (`r193_gauge_family.out:13-15`). Its sign depends on the gauge (β = 2 gives a negative Λ̃ for (A)).
- **Literal N's relaxed source, with t_H.** ⟨t_H⟩ = ξ·kk, so τ_vac = (2 + ξ)e_g (`r193_relaxed.out:4-5`). This is ξ-dependent. At exact harmonic gauge (ξ → 0), where the relaxed equations are equivalent to Einstein's, it is 2e_g.

**Lemma D (proved; checked). Density weight 1 is gauge-blind.**
- *Statement.* Let Y^{μν}[h] be the O(h²) part of a weight-w contravariant density built from G^{μν} (w = 0: G_μν; w = 1: √−g G^{μν}; w = 2: (−g)G^{μν}). Let ξ^μ = v^μ e^{ik·x} be a pure gauge, and X an arbitrary polarization at −k, off shell. Then the forward (zero-total-momentum) bilinear 2Y(L_ξη, X) vanishes identically iff w = 1.
- *Proof.*
  1. Diffeomorphism covariance at bilinear order gives 2Y^(2)(L_ξη, X) = L_ξ(Y^(1)[X]) − Y^(1)[L_ξX].
  2. The second term is a linear differential operator acting on a zero-momentum bilinear, so it is a constant with zero forward value.
  3. For a weight-w density, the forward Lie derivative is i[(w − 1)(k·v)Y^{μν} − v^μ k_αY^{αν} − v^ν k_αY^{μα}].
  4. The last two terms vanish by the linearized Bianchi identity k_αG^(1)αν[X] = 0, which holds for every X and every k.
  5. The first term vanishes for all X iff w = 1. ∎
  - (For lower indices, w = 0, the transport terms are k_μ(vG)_ν-type and do not vanish.)
- *Checked symbolically, for arbitrary X and off-shell k.* The cross term vanishes in 10 of 10 components for w = 1, and in 0 of 10 for w = 0 and for w = 2 (`r193_lemmaD.out:3-5`). Pure gauge × pure gauge vanishes for all three.
- *Corollary.* In any gauge whose Wightman polarization function differs from the TT one only by terms with a pure-gauge factor on at least one side, ⟨[√−g G^{μν}]^(2)⟩ equals its TT value.
  - That condition holds for the de Donder family: the e–e block of P_FdD is exactly P_TT, and the rest pairs a gauge leg (proved by the decomposition η = −(k k̄ + k̄ k) + δ_⊥).
  - It holds for the off-harmonic family (checked: c_A′ = 1 in all 8 (β, ξ) members).
  - It holds trivially for Coulomb gauge.
  - Axial and nonlinear gauges were not checked.
- *Relation to the background field (checked at β = ½, ξ = 1).* The full background-field Hilbert stress is EH (= A′) 1 + gauge-fixing 4 + ghosts −4 = 1 (`r193_gauge_family.out:18-22`). The EH + GF value 5 = 10 × ½ is computed. The ghost value −4 is the FP count (comparator).
  - So the gauge-fixing and ghost stresses cancel, as BRST exactness predicts, and (A′) is the background-field (effective-action) source.
- *Same mechanism as* R18-11's Theorem G (worker; `rR18-11:138-142`): there flat conservation of the record, here the linearized Bianchi identity. Counted once.

**(C), the Hamiltonian zero point, in harmonic gauge (proved; arithmetic checked).**
- In the Gupta–Bleuler vacuum, a component with negative kinetic sign and [a, a†] = −1 has ⟨0|H|0⟩ = +ω/2 (hand derivation, encoded in `r193_C_zeropoint.out:1`). So all 10 components give 10 × ω/2.
- The ghosts give −8 × ω/2 (FP: 4 complex Grassmann components).
- Net 2 × ω/2 = e_g per mode (`r193_C_zeropoint.out:3`).
- The background-field stress above is the same count as a stress.
- For ξ ≠ 1 and β ≠ ½: the BRST-quartet argument (comparator, Kugo–Ojima), not computed.

**Coulomb/Poisson = TT (proved, canonical).**
- With no matter, the linear Hamiltonian and momentum constraints set Φ = Ψ = B_i = 0 as operators at linear order. The one-loop vacuum two-point function is TT only.
- In propagator language, the instantaneous parts have no residue at k₀ = ω.
- The Lagrangian path-integral Coulomb gauge, with its δ(0) contact terms, is not evaluated.

### 4.4 Probe (d): (S) with the gravity sector inside H, plus (d-i)

- **Under the weight-1 reading (A′), or (C), or any of (A), (B) in TT or Coulomb gauge.** The graviton vacuum stress is exactly −e_g g + W_g h[n] with no remainder.
  - (S) removes e_g, provided the graviton is in H (P136(ii); a stipulation, `vR17-7:16-17`).
  - (d-i) absorbs W_g = 4e_g/3 in class 𝒟 (`vR17-11:44-45`).
  - **No number** is needed (proved at one loop under H-grav, H-V3 and the vacua above).
  - As `vR17-11:28` says for the grid vacuum, the Planckian W_g is hidden in the stipulated E/creation compensator. It is not physically absent.
- **Under (A) or (B) in harmonic gauge, and under literal N's τ.** A Planckian Λ̃ = κ(c − 1)e_g remains: 1e123 to 6e123 ρ_Λ at a = ℓ_P, sign gauge-dependent. Removing it would take a fitted counterterm or a gauge restriction.
  - Making it smaller than ρ_Λ by spacing alone needs a ≳ 1e-4 m (`r193_lattice.out:13`), excluded by every lab bound (reading).

### 4.5 Prices (probe (e); named, none adopted)

| # | Price | Axiom text touched | Status |
|---|---|---|---|
| **P-r193a** (J2's observable bridge) | The quantum one-point gravitational source is the **weight-1 density** ⟨√−g G^{μν}⟩, i.e. the metric variation of the gauge-fixed one-loop effective action (equivalently the reduced-phase-space value). ⟨t_LL⟩ (weight 2) and ⟨G^(2)_μν⟩ (weight 0) gravitate only in TT or Coulomb gauge. One clause, zero numbers. It refines P136(ii) and N_red's readout clause (P135). It also forces a correction to literal N (R16-14/R18-7's (−g)(T + t_LL) + t_H): in harmonic gauge that source double-counts the graviton zero point (2e_g at ξ → 0), unless its quantum one-point is read through P-r193a | `AX:187-190` (source/action, physical-observable identification); `AX:82-83` | proved consistent at one loop (Lemma D + checks); needed |
| **P-r193b** (lattice forward vertex) | The lattice graviton's cubic vertex at zero total momentum is the symbol substitution: each derivative → i d_a(q), and per mode it inherits the linearized gauge covariance. Without it, neither the TT virial calibration (c = 1) nor Lemma D is guaranteed on the lattice. It rides on P-N1 / W7's degree 3 | `AX:47` (supplied sector) | stipulated; open (W7) |
| Carried | P92 (S); P-vac′ (d-i); P135 (N_red); P136 (J2: (i) GR's self-coupled graviton; (ii) gravity inside H); P-N1; P52/P53 (P-r1711a); P93 | — | carried |

**Suggested (not checked).** P-r193a and R18-11's P-r1811a (a = 2, √−g T^{μν}) are the same clause, "the metric is sourced by weight-1 densities, i.e. by variations with respect to the metric". If both are confirmed, they would be counted as one price.

---

## 5. Strong words checked

- **"Gauge-blind" / "gauge-independent" for (A′).** Proved (Lemma D) for gauges whose Wightman function differs from TT by pure-gauge-factor terms. Checked in the de Donder family (all ξ, including the ξ → 0 limit, closed form) and in 6 off-harmonic (β, ξ) members, plus TT and Coulomb. Not shown for axial or nonlinear gauges, beyond one loop, or with interactions.
- **"No remainder."** At one loop, under H-grav and H-V3, with the q = 0 moduli excluded and operator (Wightman) expectations. Not a lattice derivation of the graviton's cubic vertex (W7).
- **"(S) removes e_g."** Only if the graviton sector is inside the H that defines e₀ (P136(ii)). That is a definition, not derived.
- **"Depends on the gauge."** For (A) and (B): exact rationals across 4 gauge conditions. For literal N's τ: across ξ.
- **"Planckian Λ̃."** Arithmetic at a = ℓ_P, with ρ_Λ RECALLED.
- **"Isotropic."** From the invariance of each state under the 24 proper rotations, not covariance (`TESTS:7130`).
- **"Exact."** The per-mode coefficients are exact rationals (sympy). The BZ sums are numerical, stable to 1e-8.

## 6. Against the expectation (`TESTS:7246-7250`)

- **"J2-ABSORBED for (B) and (C); (A) may differ."**
  - (C): **confirmed** in all treatments.
  - (B): **not confirmed.** In harmonic gauge it is the worst of the registered definitions (c = 4, versus c = 2 for (A)).
  - The gauge-independent object is a third definition, the weight-1 density.
- **"The likeliest failure is ⟨t_LL⟩'s off-shell gauge dependence … J2-GAUGE-BRIDGE for the pseudotensor reading only."** Half right. (A) fails as predicted, but so does (B), so the bridge is needed for both registered stress readings, not for the pseudotensor alone.
- **Removed hypothesis: free TT-only gauge-fixed modes.** Removed. The run includes the harmonic gauge's unphysical modes, the ghosts (counted, and verified as a stress at ξ = 1), the Coulomb constraints, and a gauge-condition scan. Kept: one loop, the box regulator, no matter.
- **Generic GR or model-specific (round-17 rule).** Lemma D and the per-mode numbers are generic linearized GR, holding mode by mode in the continuum. The lattice enters only through ω = |d| and H-V3.

## 7. Notes for a referee

1. Is the literal reading right? I read "(A) ⟨t_LL⟩, (B) ⟨G^(2)⟩ in harmonic gauge with FP ghosts" as h-operator expectations in the gauge-fixed vacuum, with ghosts entering only (C). (A′) and the background-field total are reported as new objects (Literal first).
2. Is the Wightman residue rule at double poles right for ξ ≠ 1, β ≠ ½? At ξ = 1 it reproduces the on-shell evaluation, and the β = ½ results are ξ-independent in closed form.
3. Lemma D's step 3: the forward Lie derivative of a weight-w contravariant density, and the use of the off-shell linearized Bianchi identity. Symbolic check: `r193_lemmaD.out:3-5`.
4. The ghost stress (−4) is FP counting, not computed. EH + GF = 5 is computed (`r193_gauge_family.out:19-20`).
5. Whether P-r193a should be merged with R18-11's a = 2 clause once vR18-11 is in.

## 8. Files

- Report: `S/R19-3_report.md`.
- Scripts and outputs: `S/scripts/r193_{onepoint,gauge_family,beta_family,lemmaD,LLcheck,relaxed,C_zeropoint,lattice}.{py,out}`; `S/scripts/r193_onepoint_v0_unhalved.out` (superseded, 2× slip).
- Reruns: `S/recheck/{R18-6,R17-11,R17-7}/*.rerun` (+ `.rerun.err`); `S/recheck/run_all.log` (11 IDENTICAL).
