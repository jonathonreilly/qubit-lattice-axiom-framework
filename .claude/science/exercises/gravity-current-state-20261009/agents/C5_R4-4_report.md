# C5 round 4, probe R4-4: set A's E3 completion. An equilibrium beable theory sourcing gravity (worker report)

**Worker.** Claude Opus 5.5, the same family as the supervisor and the earlier probes. **Not refereed.** Run 2026-10-12, 13:09Z to about 13:30Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R4-4/`:
- `scripts/r44_checks.py` and `scripts/r44_checks.out`: every number below, in sections [1]–[7].
- `scripts/pdf2txt.py`: text extraction only.
- `downloads_untrusted/`: two primary texts, read as data and never executed. They are Struyve, arXiv:1902.02188, and the referee's copy of Dürr–Goldstein–Norsen–Struyve–Zanghì, arXiv:1307.1714.

**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `TESTS.md`, Campaign C5, lines 2302–2851. R4-4 is at 2827–2838.
- `agents/C5_O5_synthesis.md`.
- `SUMMARY.md` §§15–22.
- `PRICE_NOTE.md`, v5 plus the v6 delta and its wrap-up additions.
- `agents/C5_R3-4_report.md`, `C5_R3-4_referee.md` and `C5_R3-4_referee_verdict.md`.
- `agents/C5_R2-3_report.md` and `C5_R2-3_referee.md`.

**Prior art, each counted once** (grep run at 13:10Z for "stadium", "beable" and "Bell-type" over `docs`, `.claude/science` and `archive`, plus the preserved branches).
- **R3-4 E3.** Rated VIABLE only in the explicit preferred-foliation equilibrium scope. The wave-function-determined completion is OPEN, and "dense history" and "no nonlinear metric beable" are not necessities (`C5_R3-4_referee.md:33,45`). R3-4's E1 signalling toy is correct only for an ideal projective conditional-state source (`:25`). R3-4's Lemma P has a sound conditional core (`:7`).
- **R2-3 E3.** "Records that do not act back on Ψ … the only route found that keeps exact (b)" (`C5_R2-3_report.md:252-255`). The R2-3 referee notes that "E3 is not a collapse law" (`C5_R2-3_referee.md:21`).
- **The 09-27 beables note,** branch `claude/toe-viability-probes-20260927`, `docs/RECORDS_AS_BEABLES_UNDER_THE_MOVING_RECORDS_READING_…_2026-09-27.md`. Codex confirmed it as revised.
  - Bell's minimal jump law on the walker is equivariant and cubic-covariant, gives CHSH 2.81 read from records, and has nonlocal odds.
  - **T6:** in a unique time-reversal-invariant ground state every configuration current vanishes, so the vacuum's occupations are at rest (lines 191–224 of that file).
  - It declares the wave a second ingredient beside the records, which is a departure from the memo (lines 242–247).
- **The 09-28 identity note,** on the same branch. Which record carries a disturbance is a choice of identity rule.
- **`agents/B2_report.md:254`** (suggested). Beable-sourced gravity would see the frozen vacuum beables, and "gravity has to couple to the wave, at least in the vacuum."
- **Candidate pack.** Records fork B is Bell-type beables (`.claude/science/candidates/candidate-law-20261008/DECISION_MATRIX.md:23`; `CANDIDATE_1.md:9,83,93`). Kill-sheet K4 is beables in 3D (`KILL_SHEET.md:20,87-97`).
- **The stadium picture** (owner thoughts, 09-30 to 10-04, in session memory only).
  - Its beach-ball records were mapped to Bell-type beables.
  - Owner's question: "records are mass though?"
  - The memory states a wall: "inertia from the wave, weight from records must track to 1e-15."
  - It is treated here as a hypothesis, not a rule.
- **J-queue tasks** on `ai/probes` (`probes/tasks/review-science-20260929.json`): `beable-identities-and-pointer-degeneracy`, `wall-gravity-source-and-equivalence` and `canonical-gravity-changed-carriers`. None is a beable-sourced-metric computation.
- **Wall T72,** branch `claude/toe-walls-20260929`, `WALLS.md:91`: composites fall by O(binding). This is related (composite equivalence), not the same question.

**Labels.**
- **proved:** a proof is given here, under the stated hypotheses.
- **checked:** a number in `r44_checks.out`.
- **suggested:** argued, not proved.
- **reading:** interpretation or price.
- **comparator:** literature. *web-checked* means primary text or abstract seen this run; *RECALLED* means from memory.

---

## 0. Verdict in plain words

**The idea tested.** Set A's E3 keeps a unitary wave plus "beables": an actual configuration that the wave guides (Bell-type quantum field theory). R4-4 asks whether the actual configuration can be what gravity feels: a classical metric sourced by the beables' actual stress rather than by the quantum average ⟨T⟩. If it can, records would do gravitational work.

**What came out.**

1. **Page–Geilker passes.** The field follows the actual masses (proved, elementary; Struyve states the same, web-checked).
2. **Energy-momentum conservation fails** for every natural version of the beable stress (proved).
   - The wave pushes beables around through the "quantum potential". The total beable momentum of an isolated free system changes in single runs: in the toy, a beable reverses its momentum, +4.000 → −4.005, with nothing local to recoil against (checked [5]).
   - The beable energy changes too, even after the quantum-potential energy is added. For a free Gaussian packet the exact change is ΔE = ħ²(x₀² − σ₀²)/(4mσ₀⁴) (proved; checked [1]).
   - A point source with that kind of non-conservation is never a gradient. So neither Einstein gravity nor its unimodular form has a solution (Lemma K, proved).
   - Struyve, who proposed exactly this source, says the same in his own text (web-checked).
3. **The minimal version is also excluded observationally** (estimate). The beable stress leaves out the "osmotic" part of every bound system's kinetic energy. In atoms the beables of a real ground state are at rest. So the gravitational pull a body exerts (active mass) would differ from its inertia by a composition-dependent amount.
   - From the electron shells alone, Fe and Al differ by ≈ 4.7e-7.
   - Lunar laser ranging bounds that difference at 3.9e-14 (comparator, web-checked). The margin is about 7 decades (checked [7]).
4. **Conservation can be restored only by adding a new field.**
   - It must be a retarded compensator field of **indefinite energy**, a ghost-like classical medium (proved: one-line construction).
   - It must also include a quantum-potential stress, to keep active mass equal to inertial mass for stationary bodies (proved).
5. **Even then, the beable-sourced metric lets Bob signal faster than light, in principle** (toy proved and checked). The gravitational field reads the beable's trajectory without disturbing the wave. Bohmian trajectories respond to distant settings, and the field passes that response on to a third party.
   - In the toy, the single-time distributions are identical for both of Bob's settings, at the noise floor.
   - The distribution of the time-integrated field differs: TV distance 0.785, against a noise floor of 0.041 (checked [2]).
   - So the foliation that E3 was supposed to hide becomes observable.
6. **No gravity-mediated entanglement.** A classical metric sourced by beables cannot entangle two masses: concurrence is 0 exactly, against 0.156 for quantum Newtonian coupling at recalled BMV parameters (proved; checked [4]). Gravity-mediated entanglement has not been observed (`C5_O4_referee.md:19`), so this is not excluded today. A successful BMV run would exclude it.
7. **What survives cleanly is E3 as refereed** (model R, §1).
   - The graviton stays quantum, in the wave (A5).
   - The beables source only an epiphenomenal readout metric that acts on nothing.
   - Model R passes all four checks.
   - Its foliation **can** be selected by the wave function on set A's flat base: the hyperplanes orthogonal to the state's total 4-momentum (DGNSZ eq. 24, web-checked primary text). That covariance holds only up to the regulator, which Bell-type QFT needs.
   - In model R the records still do no gravitational work.

**Against the FIXED readings** (`TESTS.md:2835-2838`).

| Model | Page–Geilker | BMV / classical analogues | Energy-momentum conservation | Foliation selected by Ψ? | Reading |
|---|---|---|---|---|---|
| **C0:** classical h sourced by the beable stress alone (Struyve's eq. 3) | pass | no GIE predicted, so open, untested | **excluded** (Lemma K) | not needed for the failure | **FAIL** for this subclass (proved); also active-mass composition excluded by about 7 decades (estimate) |
| **CQ:** C0 plus a local quantum-potential stress | pass | as C0 | **excluded** per realization in non-stationary states (Lemma E) | — | **FAIL** for this subclass (proved) |
| **CG:** CQ plus a retarded indefinite-energy compensator | pass | no GIE (open). It predicts gravitational which-path readout at intact interference (suggested) | **holds by construction** | fixed frame, or one set by the total state's P^μ (suggested); observable through signalling | consistent with the four listed checks, but only through a definitional ghost. In-principle superluminal signalling (proved toy). Born-equilibrium bias under back-reaction (Salcedo, comparator) |
| **R:** E3 with quantum A5; beable metric as a readout | pass | predicts GIE, as quantum gravity does | exact at operator level | **yes on a flat base,** hyperplanes ⊥ P^μ[Ψ] (comparator) | consistent with all four; but the beable metric does no work |

**Overall reading: INCONCLUSIVE.**
- **Why not FAIL.** No test excludes the whole registered class: CG survives the four listed checks.
- **Why not PASS, as I read it.** In CG, conservation is bought with a compensator invented for the purpose, of indefinite energy. CG also signals faster than light in principle, against the campaign's no-signalling requirement for record laws (`TESTS.md:2552`). In R the "classical metric sourced by the actual beable stress" is only a readout.
- **What would change the reading.** If the referee counts the readout metric as "sourced", R is a PASS with the prices of §4. If the referee counts CG's compensator as satisfying conservation, CG is a PASS with heavier prices.
- **The subclasses C0 and CQ are FAIL** (proved).

**Mandatory reading carried forward (reading).** The registered sentence "records do no gravitational work" (R2-3, R3-4) survives in sharpened form. Records that do gravitational work as a classical source cost one of:
- inconsistency (C0, CQ);
- a ghost compensator, with signalling in principle and no GIE (CG).

The clean completion is the one where they do none (R).

---

## 1. Hypotheses and scope (stated before the title); the models

**Base: set A** (`C5_O5_synthesis.md:322-329`).
- Minkowski space; local relativistic QFT; a supplied linearized graviton (A5).
- Records read as beables. This replaces A4's collapse flashes, as in R3-4 E3.

**Matter: a Bell-type QFT** (DGTZ, J. Phys. A 38 R1 (2005), arXiv:quant-ph/0407116; web-checked abstract). The abstract says the construction works "for more or less any *regularized* quantum field theory".
- **Wave.** Ψ is in Fock space and evolves unitarily by a regularized H = H₀ + H_I.
- **Beables.** The beable configuration q(t) lies in the space of finite particle configurations. It moves by Bohmian velocities under H₀.
- **Jumps.** It jumps at rates σ(q′←q) = [(2/ħ) Im⟨Ψ|P(q′)H_I P(q)|Ψ⟩]⁺/⟨Ψ|P(q)|Ψ⟩ (comparator, RECALLED form; DGTZ CMP 2005 per the search summary).
- **Equivariance.** The |Ψ|² distribution is equivariant (comparator). The 09-27 note proves this for Bell's minimal law on the walker (T1).
- **Regulator.** The regulator is part of the model. A lattice regulator gives Bell's own 1984 Z³ model.
- **Map to the axioms (reading).**
  - "Records form" means creation jumps.
  - "Permanent" means the configuration history, under the owner's moving-records reading.
  - "One record per site" against Pauli occupation is open (09-27 note, T6 bridge).

**Gravity: four models.** The prices are named in §4; none is adopted.
- **C0** (R4-4 literally; Struyve's "novel semi-classical gravity").
  - A classical linearized metric h solves the linearized Einstein equation, or its trace-free unimodular form, globally. Its source is the stress of the actual configuration, T_B.
  - h acts back on Ψ as an external field: H → H − ½∫h_{μν}T̂^{μν}.
  - For point beables, T_B^{μν} = Σ_k p_k^μ p_k^ν/p_k^0 · δ³(x − X_k(t)), plus the stress of the fields evaluated at the configuration (the Coulomb part, in Coulomb gauge). For field beables φ_B it is T^{μν}(φ_B), as in Struyve.
- **CQ.** C0 plus a quantum-potential stress whose total energy is Q at the actual configuration. This is the gravity analogue of Struyve's j_Q in Coulomb-gauge scalar QED (his eq. 6; web-checked).
- **CG.** CQ plus the compensator of Lemma C.
- **R** (E3 as refereed).
  - A5 is quantum and lives in Ψ, gauge-fixed with the constraints solved.
  - Beables are guided as usual.
  - The "actual metric" is a readout: its constrained part is computed from the beables' mass configuration, and its transverse-traceless part is a field beable guided by Ψ.
  - Nothing responds to this readout. The dynamics is unitary QFT plus quantized linearized gravity.

**Out of scope.**
- Nonlinear and cosmological GR. Struyve's minisuperspace consistency is noted, not used.
- Non-equilibrium beables.
- Retrocausal or two-boundary laws.
- Collapse back-action (A4 as written; that is R3-4 E1/E2/E4).
- A proof that the regularized interacting process exists globally. That is assumed, as in DGTZ and Georgii–Tumulka (comparator, RECALLED).

---

## 2. Lemmas

### Lemma K: a localized non-conservation is never a gradient (proved)

**Statement.** Let J^ν(t,x) = f^ν(t)·δ³(x − X(t)), with X ∈ C¹, in d = 3 space. Then dJ = 0 forces f ≡ 0.

**Proof.**
- The spatial components give ∂_iJ_j − ∂_jJ_i = f_j∂_iδ − f_i∂_jδ.
- The distributions ∂_1δ, ∂_2δ, ∂_3δ at the same point are linearly independent. So for i ≠ j the coefficients vanish, which gives f_i = 0 for all i.
- Then ∂_0J_i − ∂_iJ_0 = −f_0∂_iδ = 0, which gives f_0 = 0. ∎

**Same argument.** It covers creation and annihilation jumps (J = Σp δ⁴(x − e)), and finite sums of distinct sources.

**Global form, for smooth sources.**
- If J^ν = ∂^νΛ/8πG and Λ tends to one constant at spatial infinity, then ∫J^i d³x = 0.
- So **any realization whose total beable 3-momentum changes has no unimodular solution.**
- In ordinary GR, ∂_μT^{μν} = 0 forces both energy and momentum to be conserved.

### Bohmian non-conservation is generic (proved, with checks)

**Particles, non-relativistic.**
- dp_k/dt = −∇_k(V + Q)(q, t), so the total beable momentum changes as dP_B/dt = −Σ_k∇_kQ for translation-invariant V.
- That sum is the derivative of Q under a rigid translation of the configuration. It is non-zero unless Q is translation-invariant along the realized configuration.
- **Check [5].** In the toy's reflection branch, left-starting beables go from p = +4.000 to −4.005 with no local partner. The per-trajectory mean |Δp| is 8.0, while the ensemble mean stays at about 0 (−0.096 → +0.100).

**Field beables.**
- Struyve's equation of motion gives ∂_μT^{μν}(φ_B) = −(δQ/δφ(x))·∂^νφ_B(x), up to sign convention.
- Its spatial integral is again the translation derivative of Q.
- Struyve's own text: "equation (3) is not consistent … the equation of motion for the scalar field does not guarantee this" (arXiv:1902.02188, p. 2; web-checked primary text). He attributes the problem to spatial-diffeomorphism gauge invariance. He makes it consistent only for scalar QED in Coulomb gauge (an extra current j_Q) and for minisuperspace.

### Lemma E: adding the quantum-potential energy does not conserve energy (proved; checked [1])

**Why.** Along a trajectory, E_tot = ½mv² + V + Q = −∂_tS gives dE_tot/dt = ∂_tQ(q, t), the explicit time dependence of Q. That is non-zero for every non-stationary Ψ.

**Closed form.** For a free 1D Gaussian of initial width σ₀:
- the trajectory is x(t) = x₀σ_t/σ₀;
- Q = ħ²/(4mσ_t²) − ħ²x²/(8mσ_t⁴);
- **E_tot(∞) − E_tot(0) = ħ²(x₀² − σ₀²)/(4mσ₀⁴).**

**Checks.**
- The formula matches the numerics: −0.25000 at x₀ = 0, −0.18750 at 0.5, 0 at 1, +0.75 at 2 (units ħ = m = σ₀ = 1).
- Finite-difference Q agrees to 6 digits.
- The ensemble mean stays at ⟨H⟩ = 0.125 (0.12519 and 0.12481 by Monte Carlo).
- **Scale.** For a nucleon at σ₀ = 0.1 µm the change is about 1.7e-28 J per packet.
- Single runs can **gain** energy. So a compensator starting in its ground state with a spectrum condition is excluded under R3-4's refereed Lemma P premises (`C5_R3-4_referee.md:7`). This is conditional: Lemma P's compact-support premise holds here only as a decaying, not a compact, source.

**Stationary states.** In a stationary state, ∂_tQ = 0 and E_B + Q = E₀ in every run (proved). CQ is therefore consistent for exact eigenstates only.

### Lemma M: active mass under C0 (proved for hydrogen; estimate for composition)

**The deficit is general.**
- A real (time-reversal-invariant, spin-singlet) bound ground state has ∇S = 0, so its beables are at rest.
- The beable source per bound system is then Σm + V(q_actual), whereas its inertia is Σm + E₀.
- In general, E[½mv_B²] = ⟨KE⟩ − (ħ²/8m)∫|∇ρ|²/ρ. The beable kinetic energy misses the Fisher ("osmotic") term, which is strictly positive unless ρ is uniform (proved; standard identity).

**Hydrogen.** E[V(r_actual)] = −27.193 eV, against 2E₀ = −27.211. So active minus inertial energy is −13.59 eV per atom, 1.45e-8 of m_H. It also fluctuates by 26.6 eV per atom from run to run (checked [7]).

**Composition** (estimate). From the electron shells alone, with Thomas–Fermi binding 20.8 Z^{7/3} eV (RECALLED) and the virial theorem, the missing fraction is:

| Body | Missing fraction |
|---|---|
| Al | 3.3e-7 |
| Fe | 8.0e-7 |
| Fe − Al difference | **4.7e-7** |

**Against the bound.** The lunar-laser-ranging active/passive bound for Fe against Al is 4e-12 (Bartlett–Van Buren 1986) and 3.9e-14 (Singh et al. 2023, arXiv:2212.09407). Both are web-checked, at summary level. The margin is **7.1 decades** (checked [7]).
- The nuclear kinetic energy, of order 20 MeV per nucleon, is mostly osmotic too. It would raise the difference toward about 1e-3 (suggested; not computed).
- Passive mass and inertia come from Ψ's coupling to h, so MICROSCOPE-type tests of universal free fall are not the binding test here. Active-mass composition tests are.
- **Owner's thought "records are mass", as a hypothesis.** "Weight from records, inertia from the wave" fails in this minimal form at 7+ decades. It survives only with the quantum-potential stress (CQ), which restores Σm + E₀ for stationary bodies.

### Lemma C: a compensator always exists, and it is a ghost (proved)

**Construction.** Let □A^ν = J^ν, with the retarded solution, and set T_comp^{μν} = −(∂^μA^ν + ∂^νA^μ − η^{μν}∂·A).
- Then ∂_μT_comp^{μν} = −J^ν − ∂^ν(∂·A) + ∂^ν(∂·A) = −J^ν.
- So T_B (+ T_Q) + T_comp is conserved, and linearized Einstein has a solution.

**Why it is a ghost.**
- T_comp^{00} is linear in A, so its sign is indefinite.
- For a static J it integrates to a surface term, which is 0. So it does not repair Lemma M.

**Reading.** Any non-conservation can be absorbed this way. The conservation check has teeth only if the compensator must satisfy positivity, which is R3-4's Lemma P setting.

### Lemma S: a beable-sourced field signals (proved for the toy; checked [2])

**Setup.** This is the "surrealistic trajectory" geometry of Englert–Scully–Süssmann–Walther (comparator, RECALLED).
- Alice's particle is in two packets at ∓8, moving at ±4 so that they cross at t = 2 (ħ = m = 1, width 1). It is entangled with Bob's spin: (φ_L↑ + φ_R↓)/√2.
- Bob, far away, runs a Stern–Gerlach in the Z or the X basis before the packets overlap. His pointer packets are disjoint.
- Alice's beable is then guided by her conditional wave function:
  - **Z:** φ_L or φ_R. The trajectory crosses (fraction that changes side: 1.000).
  - **X:** (φ_L ± φ_R)/√2. The trajectory never crosses (0.000).
- A classical field sourced by X_A(t) kicks Charlie's test packet by κ∫X_A dt.

**Results.**
- **The single-time marginals of X_A are the same for both settings.** Histogram TV is 0.023, 0.042 and 0.036 at t = 0, 2, 4, against a sampling floor of 0.044.
- **The readout distributions differ.** The means agree (−0.075 and −0.070), but the standard deviations are 6.0 and 17.2. The TV distance is 0.785, against a floor of 0.041.
- **Charlie's outcome statistics depend on Bob's setting.** TV is 0.13 at κ = 0.05, 0.60 at κ = 0.2 and 0.78 at κ = 1.

**Why it works.**
- The mean of a linear readout depends only on single-time marginals, so it cannot signal.
- Any readout sensitive to two-time correlations can.

**Scope.**
- The result is proved and checked in the non-relativistic, instantaneous-coupling toy.
- The relativistic Bohm–Dirac version, with retarded coupling from Alice to a nearby Charlie and Bob at spacelike separation, is **suggested**. It has the same structure: Bob's influence acts along the foliation leaf.
- If the source is ⟨T⟩ in the **conditional wave function** instead (Prezhdo–Brooksby / Gindensperger type), the Bohmian conditional wave function realises R3-4's ideal projective toy exactly. TV = 1 in a single shot ([3]; the referee confirmed that toy as correct, `C5_R3-4_referee.md:25`).
- A quenched pair background (Lemma V′ below) makes a gravity-scale realisation worse, not better (suggested).

### Lemma N: no gravity-mediated entanglement (proved; checked [4])

**Proof.** Under C0, CQ and CG, each mass's wave function evolves under a c-number potential set by the other's actual beable position. A product state therefore stays a product. Concurrence is 0 (≤ 8e-17 numerically) in every branch.

**Comparison.** With quantum Newtonian coupling, the recalled BMV parameters (1e-14 kg, Δx = 250 µm, d = 450 µm, 2.5 s; RECALLED) give a concurrence of 0.156.

### Lemma V′: frozen vacuum beables (suggested)

**Why the vacuum beables are frozen.**
- The interacting vacuum Ω has multi-particle components.
- If Ω is unique and time-reversal invariant, every Bell current and velocity vanishes. That is the 09-27 note's T6 argument, which only needs time reversal to preserve the configuration projectors.
- So the vacuum beables form a frozen random pattern drawn from |Ω|². This is B2's suggestion, now sharpened.

**What C0, CQ and CG would see.**
- A positive vacuum beable mass density, which needs the same c-number subtraction as Λ.
- Quenched mass noise.

**Size, for white noise.** δΦ/c² ≈ (Gm/c²)√(n_v L). Under the illustrative assumption n_v ~ αΛ³ (not derived):
- about 5e6 at 1 Gpc for a Planck cutoff, which is absurd;
- about 4e-18 for a 1 TeV cutoff (checked [6], arithmetic only).

**Caveat.** Free Fermi-sea occupations are determinantal, and therefore hyperuniform, so white noise is not automatic. Cutoff- and model-dependent; uncomputed. Model R is unaffected.

---

## 3. The four registered checks

**Page–Geilker** (comparator: PRL 47, 979 (1981), web-checked summary).
- **C0, CQ and CG pass.** The source follows the actual positions of the masses, and Struyve says this "immediately solves the problem with the macroscopic superposition" (p. 2).
- **R passes.** Branch-wise fields after decoherence; standard QM with quantum gravity.

**BMV and classical analogues.**
- **C-models: no GIE** (Lemma N). Not excluded today: gravity-mediated entanglement "has not experimentally refuted IV" (`C5_O4_referee.md:19`). A positive BMV result would exclude every C-model.
- **Classical analogue: a source mass in coherent superposition, read by a test mass** (suggested).
  - The C-models predict a definite deflection toward the actual beable position, while the source's wave stays coherent.
  - After recombination, the deflection correlates with the source's fringe outcome at full visibility (the no-crossing rule of the toy).
  - That is a which-path record without loss of visibility, which QM forbids. It is an in-principle test; there are no data.
  - The self-gravity of the beable acting on its own wave lies in an untested Schrödinger–Newton-like regime (RECALLED: no SN test done).
- **R predicts GIE and standard results,** like quantum gravity.

**Energy-momentum conservation.**
- **C0: FAIL** (Lemma K plus non-conservation; Struyve agrees). Also an active-mass exclusion (Lemma M, estimate).
- **CQ: FAIL** for non-stationary Ψ (Lemma E).
- **CG:** holds only through a ghost (Lemma C).
- **R:** exact. The operator constraints hold and Ψ is unitary. The readout metric is not required to solve Einstein's equations run by run, because nothing responds to it.
- **Back-reaction.** For the C-models, Salcedo shows that the classical-on-Bohmian back-reaction biases the particle distribution away from |ψ|², and that energy is not conserved (PRL 90, 118901 (2003), arXiv:quant-ph/0302127; web-checked abstract and summary). Quantum equilibrium is therefore not preserved in general (comparator).

**Can the foliation be selected by Ψ rather than fixed?**
- **R: yes, on set A's flat base, for non-vacuum states.**
  - DGNSZ (Proc. R. Soc. A 470, 20130699; arXiv:1307.1714, p. 10, eq. 24; web-checked primary text) give P^μ = ∫dσ_ν⟨Ψ|t^{μν}|Ψ⟩. It is conserved, so it does not depend on the slice, and it is "generically future-causal".
  - The hyperplanes orthogonal to P^μ form a foliation, and "for a covariant choice of foliation … the guidance law is covariant".
  - In R, Ψ is unitary and P^μ (matter plus graviton) is constant, so the foliation is a fixed functional of Ψ. Equivariance along its leaves holds as for any fixed foliation (comparator). It is the rest frame of the total state.
  - **Limits.** P = 0 for the vacuum, which DGNSZ set aside. Nonlinear or cosmological gravity has no global P (OPEN). And Bell-type QFT needs a regulator (DGTZ abstract), so covariance in law holds only if the regulator is covariant. That is A6's open item (`C5_O5_synthesis.md:329`).
  - DGNSZ also warn that their alternative, the integrable part of a current vector field, need not be timelike (p. 9). The P^μ choice avoids that.
  - **This partly answers the R3-4 referee's open item** (`C5_R3-4_referee.md:33`). An explicit Ψ-selected foliation exists for flat-space E3. A completed regularized interacting QFT-plus-gravity Bell process on it is the DGTZ recipe applied, not constructed here.
- **C-models: no Ψ-only foliation** (suggested).
  - Ψ is driven by the beable-sourced h, so P[Ψ] is not conserved. Hyperplanes orthogonal to a varying P are not a foliation.
  - Using the total P (Ψ plus h plus compensator), which CG conserves by construction, works formally.
  - Either way the foliation is observable through Lemma S.

---

## 4. Prices (named, not adopted)

| # | Price | Axiom text touched | Model |
|---|---|---|---|
| E3-1 | A wave Ψ beside the records; the state becomes (records, Ψ) | Qualification: "A state is a configuration of records" (`MINIMAL_AXIOMS_2026-06-29.md:92`); a law gives one answer per state (`:94-95`) | all |
| E3-2 | Bell-type guidance and jump rates, nonlocal in their odds | Fills the open "remaining formation rules" and "physical persistence dynamics" gates (`:184-186`). The 09-27 note shows the odds are nonlocal | all |
| E3-3 | A regulator, which Bell-type rates require. A lattice regulator brings back a frame; a covariant one is not supplied | A6 (`C5_O5_synthesis.md:329`) | all |
| E3-4 | A foliation. Fixed, or Ψ-selected via P^μ[Ψ] (flat base, non-vacuum) | Time-metric gate (`:185`) | R: invisible in equilibrium. C: observable (Lemma S) |
| E3-5 | Gravity stays the quantum A5; records do no gravitational work; the beable metric is a readout | none new (A5) | R |
| C-1 | Records do gravitational work only with a quantum-potential stress (for active mass) **and** an indefinite-energy retarded compensator (for conservation) | new classical field; no axiom carries it | CG |
| C-2 | In-principle superluminal signalling along the foliation; loss of quantum equilibrium under back-reaction (Salcedo); no GIE | conflicts with no-signalling for record laws (`TESTS.md:2552`) | CG |

---

## 5. Against the expectation, and for the referee

**Against the expectation.** R4-4 registered no expectation. The R3-4 expectation, "Beables are viable with a foliation (a preferred frame in the guidance law only)" (`TESTS.md:2704`), holds for R only. Sourcing a classical metric with the beables moves the frame out of the guidance law and into observable gravity.

**Points for the referee.**
- **Lemma K.** The distributional independence of ∂_iδ, and the integrated unimodular step. That step needs Λ to tend to one constant at spatial infinity.
- **Lemma E.** The Gaussian closed form, and whether the CQ choice "total Q at the configuration" is the right analogue of Struyve's j_Q.
- **Lemma M.** The virial and real-ground-state argument. Open-shell and spin currents (the Bohm–Pauli curl term) reduce the electron deficit but do not remove the Fisher term. Thomas–Fermi is a rough formula.
- **Which bound applies.** LLR is an active/passive test. MICROSCOPE does not apply, because passive mass comes from Ψ.
- **Lemma C.** The sign of the compensator, and whether a definitional compensator should count under "energy-momentum conservation".
- **Lemma S.** The no-crossing and crossing claims follow from 1D conditional wave functions with disjoint pointer packets. The relativistic extension is only suggested.
- **DGNSZ eq. 24.** Its use for R, conditional on regulator covariance.
- **Overall reading.** INCONCLUSIVE, against PASS for R or CG. This turns on two readings: whether the readout metric counts as "sourced", and whether the ghost counts as conservation.

**Sources.**
- Web-checked, primary text: [Struyve, arXiv:1902.02188](https://arxiv.org/abs/1902.02188) (pp. 2–3 and 7); [Dürr–Goldstein–Norsen–Struyve–Zanghì, arXiv:1307.1714](https://arxiv.org/abs/1307.1714) (pp. 9–12).
- Web-checked, abstract or summary level: [DGTZ, Bell-type QFTs, arXiv:quant-ph/0407116](https://arxiv.org/abs/quant-ph/0407116); [Salcedo, arXiv:quant-ph/0302127](https://arxiv.org/abs/quant-ph/0302127); [Page–Geilker 1981](https://inspirehep.net/literature/10482); [Bartlett–Van Buren 1986](https://inspirehep.net/literature/244361); [Singh et al., arXiv:2212.09407](https://ar5iv.labs.arxiv.org/html/2212.09407).
- RECALLED: Bose et al. 2017 parameters; the Thomas–Fermi coefficient; ESSW 1992; Georgii–Tumulka.
