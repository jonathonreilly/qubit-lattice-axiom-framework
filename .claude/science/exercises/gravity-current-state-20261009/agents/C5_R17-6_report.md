# C5 R17-6: is there a qubit (Z₂-clock) model with exactly two gapless helicity-±2 branches?

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. Ran 2026-10-13, 00:44Z to about 01:12Z.
- **Unrefereed.** The worker reading is **OPEN**. Two no-go theorems for stated subclasses (Theorems G and Z, §4) are offered to the referee. If the referee confirms them, they are OBSTRUCTED results for those subclasses only.
- I edited no repository file and downloaded nothing.
- The method, including how helicity is identified, was fixed at 00:52Z, before any run (`S/METHOD_preregistered.md`).
- Scripts s1–s5 and their `.out` files are in `S/scripts/`. Each runs in under 5 s with OMP_NUM_THREADS=2.
- The R17-1 referee verdict arrived during this run (`scratchpad/C5/ref_R17-1/REFEREE_VERDICT.md`, "vR17-1"). It reads CONFIRMED WITH CORRECTIONS, WINDOW. I use it where it matters.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`, and `TESTS` = `P/TESTS.md`. R17-6 is registered at `TESTS:5956-5986`, with its FIXED readings at `:5982-5985`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.
- Earlier reports: `R17-1` = `P/agents/C5_R17-1_report.md`; `R15-3`, `R15-5`, `R16-7`, `R16-11` likewise. Their verdicts are `vR15-3`, `vR16-7` and `vR16-11` (`P/agents/C5_*_referee_verdict.md`).
- `S` = `scratchpad/C5/R17-6/`.

**Labels.**
- **proved:** a derivation made here, unrefereed.
- **checked:** numerics run here.
- **suggested:** an argument, not a proof.
- **reading:** an interpretation.
- **comparator:** literature, RECALLED or quoted from repo files, not fetched.

---

## 0. Plain words

- **(a) Is "no T₂ under the natural action" a general obstruction? No** (proved; checked). R17-1's A₁+E result is true, but it holds only for one combination: *linear* labels, at *zero momentum*, on slots that sit at highly symmetric points (sites, face centres, edge centres). Relax any one of the three and T₂ appears:
  - **At the zone corner** R = (π,π,π), N0914's own slots carry exactly the full tensor A₁+E+T₂ under the natural action. The "shift" action of P-r17-1c is the same thing seen through an on-site flip of half the qubits (an exact identity, checked on 9216 of 9216 cases).
  - **Two-slot composite labels** n_s·n_t carry T₂ at zero momentum, even with N0914's slots.
  - **Slots at low-symmetry points** (body-diagonal, edge-midpoint-type and general positions) carry T₂ at zero momentum.
  - So no representation-theory no-go exists for the natural action. The registered example of an OBSTRUCTED class cannot be proved this way.
- **(c) Is there a Z₂ version of R15-3's partner theorem? Yes, two of them, each with the same escape.**
  - **Goldstone route (Theorem G).** Suppose the gapless TT modes are Goldstone modes of a broken continuous symmetry. Then at least 4 gapless branches are forced, for any symmetry content and any mix of type-A and type-B modes.
  - **f-sum route (Theorem Z).** Suppose the TT f-sum vanishes as k → 0. This holds for Einstein–Hilbert (k²) and for the L-type (k⁴), and the TT static response must stay finite. Then the vector and scalar channels of the same readout have vanishing f-sums too. So if their static response at long wavelength is direction-independent, they carry spectral weight at vanishing energy. "Exactly two" therefore needs a **pinch point**: a static response that jumps with the direction of k. This is the many-body form of R15-3's "discontinuous symbol" edge.
  - **The divergent-response variant (Z′).** If the TT response diverges, which is what a readout conjugate to a visible graviton does, the same conclusion holds with no condition on the f-sum.
  - **The one gap:** a k⁰-class f-sum together with a finite TT response.
  - **What the pinch point means for qubits** (Identity V, exact). With N0914's stencil, the vector channel along an axis *is* the integer Gauss divergence divided by a lattice factor. So the pinch point needs the even "γ-charges" allowed by the mod-2 law (Gn = 2γ) to be suppressed at long wavelength faster than k². The scalar channel separately needs a second suppression, of the transverse trace.
  - **A mod-2 law alone does not give this** (Lemma R; proved for face slots, checked for all slot pairs on 4³). In every equal-weight (CSS / RK-type) Z₂ state the labels are pairwise independent, so the response is white noise.
- **(b) Best candidate, and why it was not run.** A phase with pinch points needs gapped or bound γ-charges, i.e. an emergent integer law.
  - **Where the emergence is perturbative**, the phase is (suggested) dressing-connected to an exact integer law. R16-11 then caps the dressed TT f-sum at k⁴: at best an L-type soft-graviton pair (Gu–Wen / Xu comparators).
  - **Where it is not perturbative**, this is the U ~ J window again (P-r16-7a, `TESTS:5408`).
  - **No exact diagonalization was feasible.** The smallest torus that carries both axial TT polarizations is 2³. Its zero-syndrome sector already has dimension 2³¹ (checked), and a 2³ torus has no small k.
- **Reading: OPEN** (worker).
  - No model meets CANDIDATE.
  - OBSTRUCTED is offered for two stated subclasses, the Goldstone class and the regular-response soft-TT class, pending the referee.
  - The question now lives in Z₂ phases with emergent long-wavelength constraints that are not dressing-connected to an integer law. That is the old U ~ J window, now with a precise signature (pinch points in the readout).

---

## 1. Setting, hypotheses, readout, helicity method

**Class (as registered, `TESTS:5967-5970`).**
- Local, translation-invariant, cubic-covariant qubit Hamiltonians on Z³ with a mod-2 vector law (H commutes with every X^{G_row}; G is the stencil at `N0914:95-97`).
- Slots: N0914's placement (diagonal slots at sites, face slots at face centres). Other placements are discussed in §3.
- Rotation action stated each time: natural (a pure permutation of qubits) or shift (P-r17-1c).
- Excluded: integer-law lifts, rotors, power-law hops.

**Removed hypotheses** (`TESTS:5976`): integer lifting and R15-3's Gaussian/PSD class. Theorems G and Z use neither.

**Helicity identification (fixed in advance, `S/METHOD_preregistered.md`).**
- A pair of branches is "helicity ±2" iff two things hold:
  - (i) little-group eigenvalues (−1, −1) about a C4 axis, (+1, +1) about a C2′ face diagonal, and (ω, ω̄) about a C3 diagonal;
  - (ii) a nonzero residue in the TT components of the stated readout.
- Vector channel: C4 = ±i (C2′ = −1). Scalar channel: C4 = +1.
- These eigenvalues were checked for Sym² in s1(4): TT (−1, −1), (+1, +1), (ω, ω̄); V (±i), (−1, −1), (ω, ω̄). C3 alone cannot tell helicity 2 from helicity 1.

**Readout bridge** (the round-17 rule, `TESTS:5703`).
- The "metric readout" is a quasi-local covariant label whose five traceless components carry E⊕T₂, each once:
  - the X-basis electric labels n_s (record-readable in an X-basis context; R17-1 §7, `AX:82-83`);
  - or their staggered or composite versions (§3).
- Nothing here identifies this label with physical geometry. P-r17-1d is carried.

---

## 2. Prior art (each counted once)

1. **R17-1 and vR17-1.**
   - The A₁+E fact under the natural action (`R17-1:205-209`). vR17-1 calls it conditional on that action and says "the axioms do not select it" (`vR17-1:22`).
   - The k⁰ cube model is a scalar TFIM. The k² moving cube has a rank-one, scalar-density TT signal (`vR17-1:16,28`).
   - The moved question (`R17-1:199`).
2. **R16-7 / vR16-7.** The integer-law k⁴ f-sum, the Bogoliubov form and the readout-bridge requirement (`vR16-7:5,17`).
3. **R16-11 / vR16-11.** The dressing transfer (`vR16-11:37`). It "says nothing automatically about an undressed microscopic readout" (`vR16-11:10`).
4. **R15-3 / vR15-3.**
   - The per-irrep inequality and Theorem C (`R15-3:117-135`; `vR15-3:5,15`).
   - Discontinuity is the sharp edge (`R15-3:190`; `vR15-3:9`).
   - Exact constraints are excluded (`R15-3:62-63`).
5. **R15-5.** The N-type projector jumps at k = 0 (`TESTS:5154`). Lemma L: qubit/qubit gives z = 3 (`TESTS:5156`). Comparators: Gu–Wen L-type, helicity ±2 only, ε ∝ k³ (`R15-5:107-108`); Xu soft graviton ω ∝ k² and Xu–Hořava z = 3/2 (`R15-5:113-114,139`).
6. **R13-2 / R12-5.** The six-pair PSD exclusion (X-G) (`TESTS:4758-4764`). Gu–Wen's freeze argument is uncontrolled (`TESTS:4548`).
7. **N0914.**
   - The stencil (`:95-97`) and H_N (`:72-73`).
   - "Not a no-go for qubits" (`:215-216`) and modular aliasing (`:218-223`).
   - The block-encoding obligation (`:180-184`).
8. **Comparators (RECALLED):**
   - Watanabe–Murayama Goldstone counting, n_A + 2n_B = n_BG with n_B = rank⟨[Q_a,Q_b]⟩/2, for internal symmetries;
   - pinch points as the signature of Coulomb (emergent-gauge) phases, including rank-2 tensor versions;
   - Z₂ gauge phases are gapped.

---

## 3. (a) Representation theory

**Proposition F (Frobenius; proved, checked s1(3)).**
- Under the natural action, the zero-momentum content of linear labels on one slot orbit is Ind_{H_p}^{O}(1), where H_p is the stabilizer of the slot position mod Z³.
- So the T₂ multiplicity is dim T₂^{H_p} = |H_p|⁻¹ Σ_{h∈H_p} χ_{T₂}(h).
- For the Wyckoff positions of P432 (s1(3)):

| Position | Stabilizer | mult T₂ at Γ |
|---|---|---|
| 1a site, 1b cube centre | O | 0 |
| 3c face centre, 3d edge centre | D4 | 0 |
| 6e (x,0,0), 6f (x,½,½) | C4 | 0 |
| 8g (x,x,x) | C3 | 1 |
| 12h (x,½,0) | C2 | 1 |
| 12i (0,y,y), 12j (½,y,y) | C2′ | 2 |
| 24k general | C1 | 3 |

- R17-1's A₁+E is exactly the statement that both of N0914's slot types sit at stabilizers containing C4 or all three C2 axes. It is not general.

**Zone-corner content (checked s1(1-2)).**
- N0914's face slots under the natural action carry A₁+E at Γ but **T₂ at R = (π,π,π)**. The diagonal slots carry A₁+E at both points.
- So **the staggered labels (−1)^{x+y+z}·(n − ½) of N0914's slots carry exactly Sym² = A₁+E+T₂ under the natural action.**

**Proposition S (proved; checked s2(i), 9216/9216 slot–rotation pairs).**
- Let U_stag flip every slot whose staggered sign is −1. Then for all 24 rotations about a site, (shift action of g) = U_stag·(natural action of g)·U_stag†. The shift sign σ_iσ_j of a face slot equals the change in its staggered sign.
- A unit translation becomes T·F_all, where F_all flips every slot.
- F_all preserves the mod-2 sector, because every Gauss row has even weight 6 (`N0914:95-97`).
- **Consequence.** Shift-covariant models that commute with F_all are unitarily the same as natural-covariant models that commute with F_all. "Natural versus shift" chooses which momentum, Γ or R, carries the long-wavelength tensor readout. It is not a physical obstruction.
- This matches R17-1's finding that the shift action forbids the uniform single-slot tension (`R17-1:213`): in the natural frame that term is staggered.

**Composite labels (checked s5).**
- Under the natural action with N0914's slots, two-slot products n_s n_t on nearest pairs (|d| ≤ 1) fall into 10 orbits. Seven of them contain T₂ at Γ. Examples:
  - n_xx(x−e_y)·n_zz(x), orbit size 6, content A₁+E+T₂;
  - diagonal–face pairs at distance 1/√2, orbit size 24, three copies of T₂.
- So a covariant, quasi-local, record-readable (in X-basis) T₂ label exists at k = 0 if the readout may be quadratic in the labels (P-r17-6b).

**Literal one-qubit-per-site** (`AX:37-47`; checked s1(1), row 1a).
- Site qubits (1a) carry A₁ at Γ and R and A₁+E on the X and M stars, for rotations about a site.
- Viewed from a cube centre (1b, also a full-O point of the space group) the M star carries T₂.
- So for literal site qubits, T₂ exists only as a zone-boundary ("taste") multiplet, and its O-label depends on which point-group copy is called "the rotations". Any slot model on non-site positions still needs the block encoding of `N0914:180-184` (vR17-1:25). That is P-r17-6c.

**Answer to (a).** No slot placement or action is representation-obstructed once you allow:
- staggered (R-point) readouts (P-r17-6a, equivalent to P-r17-1c);
- composite readouts (P-r17-6b);
- low-symmetry slot positions (P-r17-6c).

The A₁+E obstruction is exact only for linear, Γ-point labels on C4- or D2-symmetric slots (proved).

---

## 4. (c) Z₂ partner theorems

### Theorem G: the Goldstone route (proved, given the Watanabe–Murayama counting as comparator; enumeration checked s2(ii))

**Hypotheses.**
- An exact continuous internal symmetry is spontaneously broken in an O- and translation-invariant ground state. Its broken generators W carry a real O-representation.
- Each Goldstone branch along a symmetric k̂ carries the little-group character of the generator, or generator pair, that creates it.
- Counting: n_A + 2n_B = dim W.
- The TT characters of two branches hold on a C4 axis and on a C2′ diagonal.

**Proof.**
- W = W_A ⊕ W_B, where W_B carries the nondegenerate invariant form ρ.
- Since O's irreps are real, W_B has even multiplicity in each irrep, and ρ pairs C4-eigenvalue λ only with λ⁻¹. So the −1 eigenspace of W_B is even and gives a(W_B)/2 type-B modes. Likewise for C2′.
- Let a = mult(C4 = −1) and b = mult(C2′ = +1). The per-irrep inequality a_ρ + b_ρ ≤ dim ρ (`R15-3:117-121`; `vR15-3:5`) gives
  N = dim W_A + dim W_B/2 ≥ (a_A + a_B/2) + (b_A + b_B/2) ≥ 2 + 2 = 4. ∎
- s2(ii) enumerates every W of dimension ≤ 12 and confirms that the minimum is 4, attained for example by 2E (type A) and 4E (type B).

**So** Goldstone helicity-2 modes always come with at least 2 more gapless branches. This applies to the conserved-strain (k²) class whenever its U(1)s condense: the moving-cube gas (R17-1 §6) and multi-species analogues.

### Theorem Z: the f-sum route (proved)

**Hypotheses.**
- (H1) H is quasi-local and translation- and O-covariant under the stated action, with Σ_{X∋0} ‖h_X‖·|X|·diam(X)² < ∞.
- (H2) Unique ground state, invariant under translations and O, on a family of tori.
- (H3) Readout O_a(k) = V^{−1/2} Σ_x e^{−ik·x} τ_x(o_a), with o_a finitely supported, a = 1…5, carrying E⊕T₂ once each.
- Write m₁,a(k) = ⟨[O_a†,[H,O_a]]⟩ = Σ_m ω_m(|⟨m|O_a|0⟩|² + |⟨m|O_a†|0⟩|²), and χ_a(k) = 2Σ_m(…)/ω_m.

**Soft-TT signature along ẑ.**
- (S1) m₁,a(kẑ) → 0 for a ∈ {xx−yy, xy}.
- (S2) liminf χ_a(kẑ) ≥ c > 0 for both.
- EH's H_N with readout E has m₁ = g q̂² and χ = 1/J (`N0914:72-76`). H_L has m₁ = O(k⁴) and χ ~ 1/k². Both satisfy (S1)–(S2).

**Statements.**
- **(Z1) Continuity.** m₁,a(k) is an absolutely convergent Fourier series in k, uniformly in V, by (H1). Hence it is continuous at k = 0.
- **(Z2) Schur.** M_ab(0) = ⟨[O_a(0)†,[H,O_b(0)]]⟩ is O-invariant. O's irreps are of real type, so M(0) = μ_E 1_E ⊕ μ_T 1_T.
- **(Z3)** (S1) forces μ_E = μ_T = 0, because along ẑ the TT pair is one E component and one T₂ component (s1(4)). Hence **m₁,a(k) → 0 for all five components and all directions**, including the vector components xz, yz and the scalar component 2zz−xx−yy along ẑ.
- **(Z4) Concentration.** The part of χ_a(k) from excitations above Ω is at most 2m₁,a(k)/Ω², which tends to 0.
- **(Z5) The dichotomy.**
  - (A) If χ_ab(k) has a direction-independent limit L at k → 0, then L is O-invariant, so L = λ_E 1_E ⊕ λ_T 1_T with λ_E, λ_T ≥ c by (S2). The V and S channels along ẑ then keep static weight ≥ c at energies → 0, by (Z4).
  - (B) Equivalently: if the V and S channels of the readout have **no spectral weight below a fixed Δ**, then χ_V(kẑ), χ_S(kẑ) ≤ 2m₁/Δ² → 0. Meanwhile χ_xz(kŷ) ≥ c, because xz is TT along ŷ. So **χ_ab(k) is discontinuous at k = 0: a pinch point.** ∎

**(Z′) The divergent-response variant (proved). It needs no condition on μ.**
- Suppose χ_TT(kẑ) → ∞. This happens whenever the readout sees a gapless TT branch with residue Z(k) such that Z/ω → ∞, for example an h-type, conjugate readout.
- Suppose also that the leading divergence is direction-independent: f(|k|)⁻¹χ_ab(k) → L ≠ 0 for some scalar f → ∞.
- Then L is O-invariant, so by Schur χ_V(kẑ) and χ_S(kẑ) diverge too.
- The part of χ from energies above Ω is at most 2m₁/Ω², which is bounded. So the divergence must come from energies → 0: V and S spectral weight at vanishing energy. ∎
- The escape is again a direction-dependent leading singularity. EH in the h readout, χ_hh ∝ P_TT(k̂)/k², is of that kind.
- **Gap that remains:** μ > 0 together with a *finite* χ_TT. There the gapless branch's contribution can be hidden beside an O(1) high-energy part, and neither Z nor Z′ applies.

**Scope.**
- (B) uses "gapped V/S" in the strict spectral sense: no weight below Δ, including multi-particle weight.
- In the weaker branch sense (no single-particle V/S branch), a two-TT continuum could in principle carry the low-energy V weight. For z = 1 TT branches whose two-TT vertex vanishes like k (as m₁,V → 0 suggests), its contribution to χ_V is O(k² log k) and cannot rescue (A) (suggested; power counting).
- **Excluded alternatives** (the forks rule):
  - the k⁰ class (μ > 0) with finite χ_TT, where neither Z nor Z′ says anything;
  - degenerate or symmetry-broken ground states;
  - readouts not carrying E⊕T₂ once each;
  - non-summable hops.

### Identity V and what a pinch point costs a qubit model (proved; checked s4(i), 1.4e-13 on 20 random configurations, L = 6)

**Identity V.** For N0914's stencil along k = kẑ, exactly:
- (Gn)_x = (1 − e^{−ik}) n_xz;
- (Gn)_y = (1 − e^{−ik}) n_yz;
- (Gn)_z = (e^{ik} − 1) n_zz.

**What it costs.**
- Under the mod-2 law, Gn = 2γ. By Cauchy–Schwarz, S_a² ≤ m₁,a χ_a/2 with m₁ bounded. So gapped V forces S_V(kẑ) → 0, which is equivalent to **S_γ(kẑ) = o(k²)**: the even charges must be dipole-hyperuniform.
- The S channel additionally needs **S_{n_xx+n_yy}(kẑ) → 0**: the transverse trace, which no vector law constrains.
- An exact mod-2 scalar stabilizer Z^{S_row} does the opposite. It makes the X-basis ground-state amplitude invariant under label shifts by S-rows, which randomizes the transverse trace (suggested).

### Lemma R: equal-weight Z₂ states have no pinch points (proved for face slots; checked for all slots on 4³, s3(i))

**Statement.** In a state uniform over a coset n₀ + ker_{F₂}G, two labels are correlated iff e_s + e_t lies in the F₂ row space of G.
- Face slots: two cubes share only one face, so some cube contains s but not t (proved).
- All 73 536 slot pairs on the 4³ torus: none lies in the row space (rank 185 of 192), and no single slot is frozen (checked).

**Consequence.**
- The labels are pairwise independent Bernoulli(½), so S_a(k) is constant and nonzero in every channel, and χ_a ≥ 2S_a²/m₁,a ≥ c.
- So every CSS or RK-type equal-weight Z₂ ground state, including R17-1's cube and μ8 CSS model, is in branch (A).

### Controls (checked s3(ii); same observable χ_ab(k) of the E readout)

- **EH comparator** (exact constraints, physical E = TT(q̂)). The model is known to have exactly two helicity-±2 linear branches (`TESTS:5155`).
  - χ_xz,xz/(1/J) = 0.000 for k ∥ ẑ, 1.000 for k ∥ ŷ, 0.500 for k ∥ (110). The rank is 2.
  - The method reports branch (B), a pinch point, with TT characters (s1(4)). **PASS (positive control).**
- **Elastic Gaussian** (J|E|²/2 + g q̂²|h|²/2). χ = I/J is regular, and six linear branches exist. The method reports (A), partners. **PASS (negative control).**
- Both controls are Gaussian. **No positive Z₂ control exists:** no Z₂ model with a known two-helicity-2 phase is available.

### Answer to (c)

- **Yes, in two stated subclasses:** Goldstone modes (G), and soft-TT readouts with regular response (Z, with Lemma R covering every equal-weight Z₂ state).
- **The common escape** is R15-3's discontinuity edge in many-body form: a pinch point. For qubits, Identity V turns it into two hyperuniformity conditions (γ-charges, and the transverse trace).
- R16-11's own counting (18/18 symmetric gradients; `vR16-11:27`) gives no extra branch bound beyond this. I did not find a Z₂ version of it.

---

## 5. (b) The best candidate, and why no exact diagonalization was possible

**Candidate family 𝒦★ (constructed on paper; not run).**
- N0914's N = 2 slots under the shift action (equivalently the natural action with the R-point readout, Prop S).
- H = U Σ_edges (G S^z)² (diagonal, so it commutes with every X^{G_row}: the mod-2 law stays exact)
  − K Σ (k²-class dipole-free hops: R17-1's M₀ = 0 cube lift, `R17-1:170`)
  + N0914's N = 2 curl and cube-pair terms (`N0914:151-161`; their mod-2 form is in `R17-1:145-148`).
- By Theorem Z and Identity V, its only route to the target is a phase in which the γ-charges are bound (S_γ = o(k²)) and the transverse trace is suppressed.
  - **U ≫ K.** The γ-charges are virtual. The phase is (suggested) quasi-locally dressing-connected to the exact integer law, so R16-11 applies to the dressed probe (`vR16-11:37`): TT f-sum O(k⁴), i.e. at best an L-type or Xu-type soft pair (z = 3 or 2; `R15-5:107-114`, comparators). This is not the Z₂ window: the mod-2 terms are irrelevant there.
  - **U ≲ K.** The γ-charges proliferate. Lemma R's white noise suggests branch (A).
  - **U ~ K.** Undecided. This is exactly P-r16-7a (`TESTS:5408`).

**Exact diagonalization: infeasible (checked s4(ii)).**
- Both axial TT polarizations need diagonal and face slots.
- On the 2³ torus (48 slots, F₂ rank 17) the zero-syndrome sector has dimension 2³¹ ≈ 2.1e9. On 3³ it is 2⁸⁴.
- The 2³ torus also has only k ∈ {0, π}, so it has no small-k data.
- R17-1's tractable sectors (the face-only TFIM dual and the single moving cube) carry only the T₂ half of a TT pair along an axis (§3), and their helicity content is already known to be scalar (`vR17-1:19,28`).
- I therefore report no exact-diagonalization spectrum and claim no candidate.

---

## 6. (d) Prices (named, never adopted)

| Price | Axiom touched | Buys |
|---|---|---|
| **P-r17-6a**: the metric read as the staggered (R-point) label under the natural action. This is equivalent to P-r17-1c (Prop S). Translations act on it as T·F_all | Lattice (`AX:37-41`): how translations and rotations act on the readout; Record readout (`AX:82-83`) | Full A₁+E+T₂ readout with no on-site sign choice. Needs F_all·T to be a symmetry |
| **P-r17-6b**: composite (two-slot product) T₂ labels at Γ | Record readout bridge (`AX:82-90`) | A T₂ label at k = 0 under the natural action. The readout is nonlinear in records |
| **P-r17-6c**: slots at low-symmetry positions (8g, 12h, 12i/12j, 24k) plus a block encoding into site qubits | Lattice and Qubit (`AX:37-47`; `N0914:180-184`) | Linear T₂ at Γ. Costs a superlattice for the readout |
| **P-r17-6d**: emergent long-wavelength constraints (γ dipole-hyperuniformity and transverse-trace suppression) that are not dressing-connected to an exact integer law | Admissibility (`AX:57-61`; a dynamical hypothesis) | The only route left by Theorem Z. Unbuilt; equal to P-r16-7a in substance |
| Carried: P-r17-1a to P-r17-1d; P-N1 (CCR graviton, still the only known light-like TT pair) | as before | untouched |

---

## 7. Readings against the FIXED clauses (`TESTS:5982-5985`)

- **CANDIDATE: no.** No explicit qubit model with checked evidence of exactly two helicity-±2 gapless branches was found or run (§5).
- **OBSTRUCTED: not as the reading for the registered question.**
  - Offered for two stated Z₂ subclasses, needing the referee:
    - Theorem G (Goldstone helicity-2 branches: at least 4 branches);
    - Theorem Z (soft-TT signature with direction-independent long-wavelength response: V/S spectral weight at vanishing energy), with Lemma R placing every equal-weight Z₂ state in the regular-response branch;
    - Z′ (a divergent TT response whose leading singularity is direction-independent: the same conclusion).
  - The registered example class, "no natural-action Z₂ model has a T₂ gapless branch", **cannot be obtained from representation theory**, which §3 refutes as a general obstruction (proved; checked).
- **OPEN: yes** (worker reading). It stays open for:
  - pinch-point phases with emergent constraints not dressing-connected to an integer law (P-r17-6d = P-r16-7a);
  - the k⁰ class (μ > 0) with finite TT response, about which neither Z nor Z′ says anything.
- **Expectation check** (`TESTS:5986`).
  - It expected "a representation obstruction for the natural action, plus an unresolved shift-action class". The first part fails: there is no general representation obstruction, and the shift class is unitarily the natural class read at R.
  - The obstruction that does exist is dynamical (Theorems G and Z). The surviving window has a sharp signature: pinch points, i.e. S_γ = o(k²) plus transverse-trace suppression.
- **Changed hypotheses:** integer lifting and Gaussian/PSD, as registered. Theorems G and Z use neither.

---

## 8. Round-17 rule checklist (`TESTS:5689-5706`)

- **v_max:** no branch is established, so there is nothing to bound. The controls are Gaussian comparators, not models in the class.
- **Self-force, Ward identities, counting conventions, Λ:** not applicable.
- **Physical control:** §4, the same observable, χ_ab(k) of the E readout plus helicity characters.
  - The positive control is the EH comparator, which is known to have the target phase.
  - The negative control is the elastic Gaussian.
  - There is no Z₂ positive control.
- **Readout bridge:** §1, carried as P-r17-1d, with P-r17-6a and P-r17-6b as named options.
- **Forks:** Theorem Z's dichotomy lists what it excludes (§4).
- **Generic GR comparison:** not applicable.
- **Changed hypotheses:** §1 and §7.

---

## 9. Strong words and scope

**Proved (unrefereed):**
- Proposition F and the Wyckoff table;
- Proposition S;
- Theorem G (given the Watanabe–Murayama counting, which is a comparator);
- Theorem Z (Z1)–(Z5) and Z′;
- Identity V;
- Lemma R for face slots.

**Checked:**
- s1: representation content at Γ, R and the X and M stars;
- s2: 9216 of 9216 sign identities, and the Goldstone enumeration up to dim W ≤ 12;
- s3: Lemma R on 4³, and the controls;
- s4: Identity V, and the sector sizes;
- s5: composite labels.

**Suggested:**
- the multi-TT continuum power counting;
- dressing-connectedness at U ≫ K;
- proliferation (branch A) at U ≲ K;
- the scalar stabilizer randomizing the transverse trace.

**"Exactly"** is used only for operator identities and representation counts.

**Not covered:**
- the k⁰ class;
- models with degenerate or symmetry-broken ground states;
- N ≥ 3;
- matter, sources, nonlinear gravity, Λ;
- any physical identification of the readout with geometry.

## Files (`S/`)

- `METHOD_preregistered.md`: fixed at 00:52Z, before any run.
- `scripts/`:
  - `s1_reps` (Wyckoff and staggered content; helicity characters);
  - `s2_stag_and_goldstone`;
  - `s3_lemmaR_and_controls`;
  - `s4_identityV_and_sizes`;
  - `s5_pair_labels`.
- Each script has a matching `.out` file.
