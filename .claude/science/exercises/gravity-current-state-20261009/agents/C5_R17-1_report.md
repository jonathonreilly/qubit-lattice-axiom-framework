# C5 R17-1: literal qubits. Does the k⁴ obstruction survive on Z₂, Z₃ and Z₄ clocks?

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. Ran 2026-10-13, 00:08Z to 00:45Z.
- **Unrefereed.** The reading below is WINDOW. It also refutes the EXTENDS clause inside the stated class, so it should go to the referee.
- I edited no repository file and downloaded nothing.
- The method was fixed at 00:19Z, before any run (`S/METHOD_preregistered.md`).
- Scripts s1–s9 and their `.out` files are in `S/scripts/`. Each runs in under 20 s with OMP_NUM_THREADS=2.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`, and `TESTS` = `P/TESTS.md`. R17-1 is registered at `TESTS:5723-5745`, with its FIXED readings at `:5742-5744`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.
- Earlier reports and their verdicts:
  - `R16-7` = `P/agents/C5_R16-7_report.md`; `vR16-7` = its verdict.
  - `R16-11` = `P/agents/C5_R16-11_report.md`.
  - `vR16-11` = R16-11's referee verdict. It is in scratch only (`scratchpad/C5/ref_R16-11/REFEREE_VERDICT.md`) and not yet archived. It reads TRANSFERS, confirmed with corrections.
  - `vR15-5` = `P/agents/C5_R15-5_referee_verdict.md`.
- `S` = `scratchpad/C5/R17-1/`.

**Labels.**
- **proved:** a derivation made here, unrefereed.
- **checked:** numerics run here.
- **suggested:** an argument, not a proof.
- **reading:** an interpretation.
- **comparator:** literature, RECALLED and not fetched.

---

## 0. Plain words

- **The question.** R16-7 and R16-11 proved the k⁴ bound when the "vector" Gauss law is an integer law. Does it still hold when each metric slot is a literal qubit read as a Z₂ clock, so that the law holds only mod 2?
- **The answer: no.** The qubit case lies outside the obstruction: it is the window, at the level of the f-sum. Two explicit, local qubit models with an exact mod-2 law show this.
  - **The "cube" model.** Its basic move flips all six face slots of one lattice cube; this is the smallest mod-2-invariant move. Its TT electric f-sum is exactly flat in k, i.e. k⁰ (proved; checked by ED).
  - **The "moving cube" model.** Here the same pattern hops to a neighbouring cube. Its TT f-sum is exactly k², the Einstein–Hilbert power (proved; checked).
  - For comparison, the integer-law case gives k⁴ (R16-7).
- **The mechanism (proved).**
  - Every realized jump of the E-labels changes the integer vector charge by a multiple of N.
  - Its zeroth "strain" moment equals −N times the dipole moment of that charge change.
  - So the integer law is exactly what forces k⁴. The mod-N law allows k² (charge changes with zero dipole) and k⁰ (charge changes with a dipole).
  - In plain terms, the integer law forces the uniform strain and its first moment to be conserved (k⁴). Conserving only the uniform strain gives k². Conserving neither gives k⁰.
- **What the window buys.** No exclusion and no production.
  - The k⁰ cube model plus an electric-field term is exactly the 3D transverse-field Ising model on the dual lattice (proved; checked by ED). It is a scalar Ising model in disguise, gapped except at an Ising transition.
  - The k² model's TT signal comes from the density of one conserved scalar species (the cube is cubic-symmetric). A "TT" probe sees a scalar density wave, not two helicity-2 modes (reading).
- **Two structural facts about qubits.**
  - **Signs (proved).** On a Z₂ clock, E and −E are the same state. Under the natural action of lattice rotations (a pure permutation of qubits), the off-diagonal on-site electric labels therefore carry the unsigned representation A₁ + E, not T₂. The T₂g half of the graviton's two polarizations has no on-site covariant label. It returns only if rotations also flip the qubit (a "shift" implementation) — a named bridge choice.
  - **Vertex (proved).** At N = 2 every invariant move is Hermitian, so R16-11's sine-curvature probe is identically zero. Its cosine version has zero linear vertex in every real ground state, which includes every stoquastic one. B-inv therefore has nothing to bound at N = 2.
- **Control.** The 3D toric code, with and without an electric field (ED on 2×2×2). The same probe gives a k⁰ f-sum and a gap of 8 → 5.9, and the method reports no photon (PASS as a negative control).
- **Reading: WINDOW** (worker). It is not a production claim. The obstruction moves.
  - The question is no longer "does the f-sum allow EH?" (it does at N = 2).
  - Nor is it "does a gapless Z₂ phase exist?" (hopping strain quanta plausibly give one; suggested).
  - It is now: "does any mod-2 model have exactly two helicity-±2 gapless branches, with gapped vector and scalar channels, and a metric readout?" No method here decides that.

---

## 1. Setting, probe and hypotheses

**Slots.** These follow N0914's layout (`N0914:87-97`).
- The diagonal slots E_jj sit at the site x. The face slot E_ij sits at x + (e_i+e_j)/2. Each slot is a Z_N clock with X|n⟩ = ωⁿ|n⟩ and Z|n⟩ = |n+1 mod N⟩.
- The mod-N vector law: H commutes with every X^{G_row}, and G is N0914's integer stencil (`N0914:95-97`).
- H is any local Hamiltonian, bounded and of finite range.
- Excluded, as registered (`TESTS:5733`): rotors, integer-law QLMs, non-local hops.

**The probe at N = 2 (fixed before running).**
- The integer-label probe is E_TT(k) = V^{−1/2} Σ_s e^{ik·pos_s} c_s n_s. The weights are c_s = ε_jj on diagonal slots and 2ε_ij on face slots, with ε a unit TT polarization.
- At N = 2, X_s = 1 − 2n_s is Hermitian. So this probe is −½·V^{−1/2}Σ e^{ikx} c_s X_s plus a c-number: the "Hermitian part of the clock" and the label probe coincide.
- At N = 3 and 4, I report both the label probe and the clock probe C_I ∝ (X − X†)/2i (§4).

**What changes from the governing no-go.** Integer lifting is removed (`N0914:109-114,218-223`; `vR15-5:33`). Kept: finite slots, an exact law (mod N) and quasi-locality.

---

## 2. Prior art (each counted once)

1. **R16-7 and vR16-7.**
   - Theorem B: exact integer law ⇒ m₁ = O(k⁴), V^{−1/2}-normalized (`vR16-7:5,17`).
   - R16-7's suggested §8 on mod-N clocks (`R16-7:224-230`).
   - N = 2 in the Weyl presentation is outside B (`R16-7:84,266`).
2. **R16-11 and vR16-11.**
   - Lemma S and Theorem B′ (`R16-11:94-135,156-166`).
   - Mod-N clocks were left open (`R16-11:288`).
   - vR16-11 confirms the min-weight-20 integer qubit hop only in finite boxes (`vR16-11:31`). It also says B-inv does not close gap 1 (`vR16-11:21-23`).
3. **N0914.**
   - The moment lemma (`:225-250`) and lifting (`:109-114,218-223`).
   - The finite-clock Hamiltonian (`:151-161`).
   - "This is not a no-go for qubits" (`:215-216`).
4. **R15-5 Lemma W's N > 36nM** (`vR15-5:33`).
5. **Repository grep** for Z₂ / mod-2 tensor clocks and X-cube: no note in `docs/` treats them. The one hit, `docs/U1_GAUSS_SUPPORT_FORCING_EXTENDED_PAYLOAD_CLASS_BOUNDED_NOTE_2026-09-05.md`, is a U(1) note and not relevant. Of the three `docs/` notes that mention fracton or Pretko, none handles a mod-N tensor law (grep only; not read in full).
6. **Comparators (RECALLED):**
   - Z_N rank-2 / X-cube fracton codes are gapped at large penalty;
   - Higgsing U(1) higher-rank theories to Z_N (Bulmash–Barkeshli 2018);
   - the f-sum of a conserved hopping density is O(k²) (Pitaevskii–Stringari);
   - the 3D quantum TFIM has its transition at field/coupling ≈ 5.16 and lies in the 4D Ising (mean-field, log-corrected) class;
   - the 3D toric code is gapped.

---

## 3. The decomposition theorem (proved; checked)

**Theorem M (proved).**
- Take any H on Z_N clock slots and the label probe C above. Then
  [C†,[H,C]]_{n′n} = −H_{n′n}|c(n′) − c(n)|², with c(n′) − c(n) = V^{−1/2} ĉ·δ(k) and δ = n′ − n (the realized integer jump).
- Hence **m₁(k) = V⁻¹ Σ_δ w_δ |ĉ·δ(k)|²**, with ĉ·δ(k) = Σ_s e^{ik·pos_s} c_s δ_s and w_δ = −Σ_n ψ*(n+δ) H_{n+δ,n} ψ(n) (paired with −δ).
- If H commutes with the mod-N law, every active jump has Gδ = Nγ_δ with γ_δ an integer vector field. If H is stoquastic and ψ is its Perron state, then w_δ ≥ 0.
- Also m₁(0) = 2V⁻¹⟨0|C₀(H − E₀)C₀|0⟩. It vanishes iff C₀|0⟩ lies in the ground space, i.e. iff the uniform TT label is conserved on the ground state.

**Moment identity (proved; checked to 0 on 200 random patterns, s1(c)).** Put Gauss row j at x + e_j/2. Then D(Gδ) = −M₀(δ), where D_{lj} = Σ pos_l (Gδ)_j and M₀ is the slot-type-summed zeroth moment. So **M₀(δ) = −N·D(γ_δ)**.

**Consequences (proved for finite sums of lifts).** Since ĉ·δ(k) = ε:M₀(δ) + O(k):
- (i) γ_δ = 0, the integer-invariant case: O(k⁴), which is R16-7's Theorem B (`N0914:239-242`).
- (ii) D(γ_δ) = 0 but γ_δ ≠ 0: the zeroth moment vanishes, so the term is O(k²). It is exactly k² when the TT-projected first moment is nonzero. I suggest, by N0914's cycling argument (`:203-206`), that the first moment is fixed by γ's second moment.
- (iii) D(γ_δ)^{TT} ≠ 0: a k⁰ term.

**This trichotomy is not exhaustive.** It is excluded only by the class:
- non-summable or power-law hops give fractional powers (`R16-11:243-259`);
- non-quasi-local readouts.

**Lemma Wr (wraps; proved).** For a nonzero pattern m mod N and a slot s in its support, the two realizable lifts that differ only by the wrap at s differ in M₀ by N·ê_type(s) ≠ 0. So at least half of the realizable lifts of every nonzero clock character Z^m have M₀ ≠ 0.
- A pure clock character, Z^m times any f(X) with no projector, activates them on every label configuration that occurs.
- With uniform labels on supp m: E[δ_s] = 0 and Var δ_s = m_s(N − m_s), checked for N = 2, 3, 4, 8 (s4(3)). So a pure-character term −K(Z^m + h.c.) contributes the flat **2KΣ_s|c_s|² m_s(N − m_s)**.

---

## 4. (a) Minimal invariant hops at N = 2, 3, 4 (checked: s1, MILP in a 4³ box; all Gauss rows the box touches are imposed)

**Search scope.** These are the minimum weights containing one fixed diagonal slot or one fixed face slot. By cubic symmetry, they are the minimum weights containing any slot of that kind. The full list of all minimal patterns was not enumerated.

| N | Fixed slot | Min weight | Pattern | Realizable lifts | Integer-invariant (Gδ = 0) | M₀ = 0 | M₀ = M₁ = 0 |
|---|---|---|---|---|---|---|---|
| 2 | face | **6** | the six face slots of one cube ("cube") | 64 | **0** | 8 | **0** |
| 2 | diagonal | **8** | μ8 (2 xx, 2 zz, 4 xz; 3 orientations) | 256 | **0** | 24 | **0** |
| 3 | face or diagonal | **10** | entries 1, 2 | 1024 | **1** | 54 | 2 |
| 4 | face | 6 | 2 × cube | 64 | 0 | 8 | 0 |
| 4 | diagonal | 8 | 2 × μ8 | 256 | 0 | 24 | 0 |

**Minimal lifts.**
- The as-is lift of the cube has M₀ = 2(J − I) in units of slot counts (J is the all-ones matrix), a traceless off-diagonal tensor. Its integer charges ±2 sit at the cube's corners: Gδ = 2γ, with γ a set of vector-charge dipoles.
- The as-is lift of μ8 has M₀ = [[2,0,4],[0,0,0],[4,0,2]]. Both are nonzero.

**Hops with no lift of vanishing moments (the registered ask).**
- At N = 2: the cube and μ8 (all orientations), and every F₂-invariant hop of weight below 20.
  - The last statement rests on the integer {−1, 0, 1} minimum of 20. I rechecked that in a 4³ box (s5 reproduces R16-11 s4). vR16-11 confirms it in 4³, 6³ and 8³ boxes only (`vR16-11:31`), so it is box-limited.
- At N = 4: 2 × cube and 2 × μ8.
- At N = 3: the minimal weight-10 hops do have an integer-invariant lift, with entries in {−2, −1, 1}: a spin-1 QLM hop. Their clock character Z^m still activates the 1023 other lifts (Lemma Wr). With uniform labels, the k = 0 weight is 3.45 for the label probe (formula: 3.45) and 0.59 for the clock probe (s4(3)).

**N0914's own model at N = 2 (checked, s9).**
- Its R2 rows, built from `N0914:133-142`, satisfy G R2 = 0 over the integers. The diagonal rows have max coefficient 4 and row-ℓ₁ 24, as `N0914:148` states.
- Mod 2, the diagonal rows vanish, and **each off-diagonal row equals the product of the two cubes sharing that face** (weight 10). Its as-is M₀ counts are [2, 4, 4].
- So N0914's g-term at N = 2 is a pure clock character of cube pairs, and Lemma Wr applies to it.
- A k⁰ f-sum for that model follows exactly in its J → 0 CSS limit (suggested: the separation check was not run for cube pairs). For J ≠ 0 it is generic (suggested).

---

## 5. (b) Exact symbols (proved; checked: s2, s6; k = 1e-3 to 0.3; five directions; both TT polarizations; subtraction: none)

**(A) The cube CSS model.** H_S = −U Σ X^{G_row} − K Σ_{cubes} Z^{cube}, optionally with μ8 terms.
- All terms commute and the model is frustration-free. Its gap is ≥ 2 min(U, K) (proved).
- Every pair s ≠ t inside one pattern is separated by some other Z-stabilizer: 99 of 99 pairs, cube + 3 μ8 orientations (s7). So ⟨Z^p X_s X_t⟩ = 0 in every ground state, and
  **m₁(k) = K Σ_p Σ_{s∈p} |c_s|²** for every k, every V with all L ≥ 3, and every ground state.
  - For cubes alone this is 8K Σ_{i<j} ε_ij².
- Slopes are 0.000 in every direction and polarization. In the E_g polarization (k ∥ x, ε = (yy − zz)/√2), μ8 gives m₁ = 4.000K, slope 0 (s6).

**(B) The moving-cube model.** H_D = −K Σ_{x,a}(T_{x,a} + h.c.), where T_{x,a} is the label ladder operator moving one flipped cube from x + a to x, with δ = 1_{cube x} − 1_{cube x+a}.
- **Identity (proved; checked to all digits on 2×2×3, s3(iii)).**
  m₁(k) = Σ_a W_a |ĉ·cube(k)|² 4 sin²(k·a/2), with W_a ≥ 0 and Σ_a W_a = −E₀/V.
- **Bound (proved).** In the zero-syndrome sector, −E₀/V ≥ K/12. The trial state has one cube per disjoint 3×2×2 block, in an equal superposition of two adjacent positions. The reference configuration is a sum of cubes, so it lies in the sector. Other hops contribute ≤ 0 by stoquasticity.
- Hence **m₁(k) ≥ (K/12)·min_a 4 sin²(k_a/2)·|ε:M₀(cube) + O(k)|² = c k²** for generic k̂ and ε with ε:J ≠ 0.
- Slopes are 2.000 (s2(B)). In the E_g polarization with μ8, the slope is 2.000 (s6).
- **Whole-zone v_max** (single quantum on the infinite lattice): ε(k) = −2K Σ_a cos k_a, so max |∇ε| = 2√3·K·a/ħ (proved). The ED gives E₀ = −6K (k = 0), as this predicts. No light cone or c is defined in these models.

**(C) A single-pattern M₀ = 0 lift of the cube** (charge-2 quadrupole hop; 24 rotations). Slope 2.000 in generic directions (s2(C)).

**(D) An integer-invariant lift** (N = 3, weight 10, 24 rotations). Slope 4.000, which reproduces R16-7 (s2(D)).

---

## 6. (c) What the failure buys: no exclusion and no production

- **Exclusion: none.** A k⁰ or k² f-sum makes the Bogoliubov bound χ ≥ 1/m₁ at least as weak as Einstein–Hilbert's 1/k². It excludes nothing.
- **Production: none established.**

**The k⁰ model is exactly an Ising model (proved; checked).**
- Start from n = 0 and flip cubes. The face labels are then n_f = τ_c ⊕ τ_{c′}, where c and c′ are the two cubes sharing face f. Also Z^{cube c} = τˣ_c and X_f = τᶻ_c τᶻ_{c′}.
- So **−K Σ Z^{cube} − h Σ_f X_f is the 3D transverse-field Ising model on the dual cubic lattice**, in its Z₂-even sector.
- **The structural reason (proved).** Restricted to face slots, the mod-2 Gauss row (Gn)_j(x) is the parity of the four faces around the j-edge. That is ordinary Z₂ flatness on the dual lattice.
- **Duality check (2×2×2).** The face sector (dim 128) and the even TFIM sector (dim 128) have the same lowest six levels to 1e-8 (s3(ii-a)).
- **ED, 3×3×2 torus.** This is the largest feasible size: 18 cubes, 54 face slots, 2¹⁸ states. Results (s3(ii-b), s8):
  - At h = 0, m₁ equals the exact formula in all 8 (k, polarization) entries, once the L_z = 2 coincidence (top and bottom faces share a cube pair) is included (s4(2)).
  - At h/K = 0.1–0.3, m₁ stays O(1) at every allowed k: for example 4.00, 3.85, 3.34, 1.65 at k = (2π/3, 0, 0), polarization 1.
  - χ_TT = 0.02–0.25.
  - Even-sector gaps (the face model is the even sector only; s3's "gap" column also includes the odd sector): ≥ 2, ≥ 2.14, 1.43, 1.91 at h/K = 0, 0.1, 0.2, 0.3.
  - Size limit: only the k on that grid; no extrapolation.
- **Reading.** The TT label probe is the anisotropic Ising bond energy. The phases are gapped on both sides, with a scalar 4D-Ising transition near h/K ≈ 0.19 (comparator). The static response there is at most log-singular, with no 1/k² (comparator). So this k⁰ window carries no graviton.

**The k² model: the signal is a conserved scalar density (reading; partly proved).**
- The cube is invariant under all 24 rotations (s2: one copy mod translation), and the moving-cube model conserves the number of cubes.
- E_TT(k) is (ε:M₀(cube))·ρ_cube(k) up to overlap corrections, so every TT polarization sees the same single species' density. For k along a body diagonal both TT couplings vanish (ε:J = 0; s2(B)).
- At low density this is a gas of hopping hard-core cubes, gapless and plausibly superfluid with z = 1 sound (suggested; comparator). That sound is helicity 0. With μ8's three orientations, there are three species in A₁ + E (suggested). That is still not two helicity-±2 branches.

**So the obstruction moves to:** does any model in the class have exactly two helicity-2 gapless TT branches, with gapped vector and scalar channels and a metric readout? That is not decided here. §7's sign fact bears on it.

---

## 7. (d) The readout bridge at N = 2

**Signs (proved; checked, s4(1)).**
- On a Z₂ clock the label map n → −n mod 2 is the identity. So the natural action of proper cubic rotations (`AX:37-38`) is a pure permutation of qubits.
- The face 3-plet then has characters (E, C₃, C₂, C₄, C₂′) = (3, 0, 3, 1, 1) = **A₁ + E**, against the tensor's signed (3, 0, −1, −1, 1) = T₂.
- So at N = 2 the off-diagonal on-site electric labels carry no T₂. For k along an axis, a helicity-±2 pair needs one E_g polarization (xx − yy) and one T₂g polarization (xy). The T₂g one has no on-site covariant label.
- Therefore the window is shown above also in the covariant E_g polarization (s6). The face-slot (off-diagonal ε) numbers are unsigned densities.
- **The alternative "shift" implementation** (n → 1 − n on sign-flipped slots, i.e. reading the qubit as S^z = n − ½):
  - it restores T₂ signs;
  - it preserves the zero-syndrome mod-2 sector: the flipped-slot parity is 0 on every Gauss row for C₄z, C₂z and C₃ (s4(1));
  - but it forbids the single-slot face tension −hΣX_f.
  - This is a bridge choice, not axiom content (P-r17-1c).

**Vertex (proved).**
- At N = 2, Z^m is Hermitian, so R16-11's sine probe i(T − T†) ≡ 0.
- For the cosine/flux probe, ⟨[E_TT, Z^m]⟩ = Σ_s a_s ⟨Z^m X_s⟩. Each Z^m X_s with s ∈ supp m is anti-Hermitian, so this is 0 in every state real in the label basis. That includes every stoquastic ground state: the cube, moving-cube and N0914-at-N = 2 models (`R16-7:127-130`, `vR16-7:11`).
- So B-inv's vertex vanishes. This is the zero-vertex case R16-11 left open (`R16-11:209,290`), and vR16-11 already calls it phase-dependent (`vR16-11:23`).

**Which record-readable quantity is "the metric"? (reading)**
- **In an X-basis readout context:** the per-slot labels n_s are gauge invariant (the X's commute with X^{G}). E_TT(k) is then a sum of locked bits.
- **In a Z-basis context:** the only gauge-invariant quantities are Z₂ fluxes Z^m over F₂-invariant patterns, for example the product of a cube's six face bits ∈ {±1}.
- "The metric" at N = 2 is therefore at best a coarse-grained flux density: a nonlinear object with zero linear vertex to E_TT in real states.
- Three obligations stand outside the axioms:
  - neither readout context is axiom content (`AX:82-83,181-183`);
  - the six-slot cell needs a block encoding into site qubits, since the axioms give one M₂(C) per site and N0914 puts slots on faces (`N0914:180-184`);
  - permanence (`AX:80`) makes any flux record a one-time readout.
- No metric susceptibility at N = 2 is supplied. Every f-sum above is a statement about the electric-label probe only.

---

## 8. (e) Physical control: the 3D Z₂ toric code (checked, s3(i))

**Setup.** H = −K Σ_p B_p − h Σ_l X_l on the 2×2×2 torus. The Gauss sector reachable from n = 0 has dimension 16384. The probe is the same transverse label probe.

**Results.**
- At h = 0: gap 8K, and **m₁ = 4.000 at k = 0, (0,π,0), (0,0,π) and (π,π,0)**, i.e. k⁰, with χ = 0.0625.
- At h = 0.2 and 0.5: m₁ = 3.73–4.00; gaps 7.38 and 5.93.
- At h = 0 this is exact by the same separation argument as §5(A).

**What it shows.**
- The method reports a k⁰ f-sum. By M4 and Feynman, that forces no soft mode, so it does not report a photon.
- Same observable, in a model known to be gapped and deconfined (exactly so at h = 0). **PASS as the registered negative control.**
- It is not a positive control: no gapless phase was measured.

**The contrast (proved).** On the same qubit Hilbert space, U(1) ring exchange (an integer-invariant circulation lift) has M₀ = 0 exactly. Its k⁰ term vanishes and m₁ = O(k²). The qubit's Z₂ reading against its integer reading moves the power, exactly as in the tensor case.

---

## 9. (f) Prices (named, never adopted)

| Price | Axiom touched | Buys |
|---|---|---|
| **P-r17-1a**: read the metric slot as a Z₂ clock with a mod-2 law, not a spin-½ link with an integer law | None directly: both present M₂(C) (`AX:47`). It is a choice of the admissibility rule's conserved structure (`AX:57-61`) and of the readout | Escapes Theorems B and B′: k⁰ or k² TT-label f-sums (§5). Costs only a Z₂ redundancy (no continuous removal of longitudinal modes), and no on-site T₂ under the permutation action |
| **P-r17-1b**: dynamics that conserves the uniform strain, i.e. hopping of invariant patterns (a global conservation law not in `AX:57-61`) | Admissibility (a dynamical hypothesis) | EH-power k² instead of k⁰. Comes with conserved-species densities: a scalar for the cube (suggested) |
| **P-r17-1c**: the "shift" implementation of rotations at N = 2 (half-odd S^z reading) | Lattice: how rotations act on the possibility domain (`AX:37-38`; not fixed by the axioms) | On-site T₂ electric labels. Forbids the face tension −hΣX_f |
| **P-r17-1d**: a metric readout at N = 2 as a coarse-grained Z₂-flux density | Record readout bridge (`AX:82-90,181-183`) | Some definition of "metric" at N = 2. Unbuilt; nonlinear, with zero linear vertex in real states |
| Carried: P-r16-7b (scalar attraction); P-N1 (CCR graviton) | as before | Untouched. P-N1 remains the only known source of a light-like TT branch |

---

## 10. Readings against the FIXED clauses (`TESTS:5742-5744`)

- **EXTENDS: no.** The k⁴ bound is false at N = 2 (and at N = 3, 4) in the stated class. The explicit counterexamples of §5 are proved and checked. It holds only where every active lift is integer-invariant, i.e. in R16-7's QLM subclass.
- **WINDOW: yes** (worker reading, unrefereed). It is shown in the covariant E_g polarization as well as the face polarizations.
  - **k⁰:** the cube CSS model, with m₁ = K Σ_p Σ_{s∈p}|c_s|² exact for every ground state.
    - Checked by ED: 2×2×2 duality and the 3×3×2 torus.
    - It is gapped, and dual to the 3D TFIM.
  - **k²:** the moving-cube model, with m₁ ≥ (K/12) min_a 4 sin²(k_a/2)|ĉ·cube|² ≥ c k² (proved).
    - Its identity is checked by ED, and the slope 2.000 is checked on symbols.
  - Neither is a production claim. §6 says what each buys: nothing graviton-like in either explicit model.
- **OPEN:** not as the reading. It does remain for the moved question in §6.
- **Expectation check** (`TESTS:5745`).
  - It matches "WINDOW at the f-sum level", with three differences:
    1. a k² (Einstein–Hilbert-power) window exists, not only k⁰;
    2. gapless phases in the class are plausible (hopping strain quanta; suggested), so the obstruction is not "whether any gapless Z₂ tensor phase exists";
    3. two new structural facts sharpen the moved question: no on-site T₂ under the natural action, and the minimal k⁰ model is exactly Ising.
  - **Changed hypothesis:** integer lifting, as registered.

---

## 11. Round-17 rule checklist (`TESTS:5689-5706`)

- **v_max.**
  - The cube model at h = 0 has immobile excitations (v = 0).
  - The moving-cube single quantum has whole-zone v_max = 2√3·K·a/ħ.
  - No gauge-boson branch was established, so the gauge-field v_max rule has nothing to apply to.
- **Self-force, Ward identities, counting conventions, Λ (enforced or stipulated):** none apply. No kernels, Ward identities, tunings or Λ mechanism are used.
- **Physical control:** §8, the same observable in the toric code. It is a negative control only.
- **Readout bridge:** §7, named (P-r17-1d).
- **Forks:** the trichotomy of §3 lists its excluded alternatives (power-law hops; non-quasi-local readouts).
- **Generic GR comparison:** not applicable; there is no initial-state or memory claim.
- **Changed hypothesis:** §1.

---

## 12. Strong words and scope

**Proved** (all unrefereed):
- Theorem M and the moment identity;
- Lemma Wr;
- the CSS flat formula (given the s7 separation);
- the moving-cube identity and its variational bound;
- the face-sector TFIM duality and the face-flatness structure;
- the A₁ + E sign fact;
- the N = 2 vertex-zero statement.

**Checked:** s1–s9.
- These are MILP searches in a 4³ box (the minimum weights are box-limited, like vR16-11's 20) and exact symbol slopes.
- The ED clusters were 2×2×2 (toric code, cube duality), 3×3×2 (cube/TFIM) and 2×2×3 (moving cube, one quantum).
- No phase is established by any cluster.

**Suggested:**
- the first moment is fixed by γ's second moment;
- N0914's own model has k⁰ for J ≠ 0;
- the CSS uniformity at N = 3, 4;
- a superfluid of strain quanta, with its species count and helicity.

**"Exactly"** is used only for operator identities and integer arithmetic.

**Not covered:** the scalar channel (R16-7's Theorem D is untouched), fermions, matter, nonlinear gravity, Λ, the U ~ J phases of N0914's model, and N ≥ 5.

## Files (`S/`)

- `METHOD_preregistered.md`: the method, written 00:19Z, before the runs.
- `scripts/`:
  - `s1_modN_minimal_hops` (MILP and lift enumeration);
  - `s2_exact_symbols`;
  - `s3_ed_checks` (toric code control, cube/TFIM, moving cube);
  - `s4_signs_wraps_N3`;
  - `s5_recheck_R16-11_s4_box4`;
  - `s6_mu8_Eg_channel`;
  - `s7_css_pair_check`;
  - `s8_even_sector_gap`;
  - `s9_N0914_R2_mod2`.
- Each script has a matching `.out` file.
