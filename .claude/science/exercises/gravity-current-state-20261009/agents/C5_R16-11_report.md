# C5 R16-11: does R16-7's Theorem B survive an emergent Gauss law? The dressing transfer.

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker). 2026-10-12, 23:23Z to 23:52Z. **Unrefereed.** No repository file was edited. Nothing was downloaded. Scripts s1–s5 and their `.out` files are in `S/scripts/`; each runs in under 1 minute on 2 threads.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`. The R16-11 registration is `TESTS:5492-5513`, with the FIXED readings at `:5509-5512`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.
- `R16-7` = `P/agents/C5_R16-7_report.md`. `vR16-7` = its referee verdict, `P/agents/C5_R16-7_referee_verdict.md`. A copy is at `scratchpad/C5/ref_R16-7/REFEREE_VERDICT.md`, and the full report is `.../ref_R16-7/R16-7_referee_verdict.md`.
  - The verdict's reading is **INCONCLUSIVE** (`vR16-7:3`). Its corrected Theorem B is at `:5`, and its strongest correct statement at `:17`.
  - **I build on that corrected statement** (V^{−1/2} normalization, §1), not on R16-7's NOT-PRODUCED-EVIDENCE.
- `R15-5` = `P/agents/C5_R15-5_report.md`; `vR15-5` = `P/agents/C5_R15-5_referee_verdict.md`.
- `S` = `scratchpad/C5/R16-11/`.

**Labels.**
- proved: a derivation made here (unrefereed);
- checked: numerics run here;
- suggested: an argument, not a proof;
- reading: an interpretation;
- comparator: literature, RECALLED and not fetched.

**Convention.** The registration writes Ẽ = W†EW. I write H′ = W†HW and Ẽ = W E W†. These are the same thing with W ↔ W†.

---

## 0. Plain words

- **The question.** R16-7 showed the following. When the microscopic rules keep the gravity-type ("vector") Gauss law exactly, on finite slots, the metric cannot have Einstein–Hilbert stiffness. Spin ice is different: there the law is not microscopic, and it appears only at low energy. Does R16-7's bound survive when the law emerges in that way?
- **Answer, if the emergence is by a local change of variables: yes (proved, unrefereed).**
  - Suppose some quasi-local unitary W carries the true ground state into the exact-law subspace.
  - Then the dressed TT electric f-sum is ≤ 2S²K₂k⁴. Here K₂ is a second-moment sum over the dressed Hamiltonian's local terms.
  - This holds for any penalty size and any law-violating V, provided such a W exists.
  - The condition on the dressing's tails is mild. Tails Φ(r) with Σ r¹³Φ(r) < ∞ suffice, and stretched-exponential tails are far inside this.
  - Only the dressed ground state has to obey the law. The Hamiltonian need not be block-diagonalized.
- **Why the dressing cannot help.**
  - The f-sum sees the dressed Hamiltonian only between states that obey the law.
  - Inside that subspace, every local term can be replaced by a term that commutes with every Gauss operator.
  - For such terms, a uniform or linearly varying TT electric field is pure gauge. All 24 of these fields are sums of Gauss operators (checked, residual 5e-14).
  - That fixes the k⁴, independent of how the law came about.
- **Spin ice (reconciled).**
  - The same transfer holds for the U(1) law, with power k² instead of k⁴. For U(1), the three "rotation" fields are not pure gauge (checked).
  - Stated with gauge-invariant probes, both bounds say one thing: the static susceptibility of the minimal local invariant stays above a positive constant.
  - Maxwell's B field has a constant susceptibility, which is allowed. Pretko-type curvature-squared gravity also has a constant curvature susceptibility, which is allowed. Einstein–Hilbert's curvature susceptibility vanishes like k², which is forbidden.
  - Spin ice therefore gets its photon not by escaping the bound but because the photon never violated it.
- **What remains:**
  - phases with no such quasi-local dressing (critical or power-law dressings, first-order transitions, U ~ J where no W is constructed);
  - mod-N clocks;
  - a curvature readout whose vertex vanishes;
  - the scalar channel (Theorem D need not transfer, because dressing generally destroys stoquasticity; suggested).
- **The tail condition is necessary in kind (checked).** An explicit exact-law, qubit-compatible model with power-law-ranged hops (weight L⁻ᵖ) has f-sum ~ k^{p−1}, which is k² at p = 3. This is not a quasi-local dressing, so it is not a FAILS-TO-TRANSFER.
- **Reading: TRANSFERS (worker; a no-go, so it needs the referee),** scoped to finite slots with an integer vector law and the stated hypotheses (W1, W2).
  - What transfers is the referee-corrected Theorem B (`vR16-7:5,17`).
  - It does not upgrade R16-7's INCONCLUSIVE.
- **The two gaps vR16-7 left (§4a).**
  - **Gap 1 (observable): narrowed, not closed.** Corollary B-inv bounds a local gauge-invariant curvature probe directly. Einstein–Hilbert is then excluded for any local curvature readout with a nonzero vertex. A readout bridge is still needed.
  - **Gap 2 (U(1) control): not closed.** The dressing transfer is again an operator identity, and no 3D photon was measured.

---

## 1. Setting and hypotheses

**Slots** (as in R16-7's 𝒬_E, finite-slot part, `R16-7:61-67`).
- Quantum-link (QLM) spin-S slots with integer E_s, ‖E_s‖ ≤ S. S = ½ is the qubit case.
- The six tensor slot types sit at N0914's positions: E_jj(x) at x, and the face slot E_ij(x) at x + (e_i + e_j)/2 (`N0914:87-97,136-142`).
- Gauss operators G_j(x) = (G E)_j(x), with N0914's integer stencil (`N0914:95-97`).
- 𝓗₀ = ∩ ker(G_j − g_j⁰) is a fixed Gauss sector; the background g⁰ = 0 is allowed.
- Π_X̄ = the projector onto G_j = g_j⁰ for every j whose stencil meets X.

**Microscopic H.**
- Any self-adjoint, bounded-below H on these slots, for example U·Σ(vector-law penalty) + V with V law-violating (`TESTS:5497-5501`).
- |0⟩ is a ground state, on a finite volume V.

**Dressing hypotheses.**
- **(W1) The dressed ground state obeys the law:** |0′⟩ := W†|0⟩ ∈ 𝓗₀.
  - Floor version: q := sup_X ⟨0′|1 − Π_X̄|0′⟩, the local vector-charge probability in the dressed frame.
- **(W2) The dressed Hamiltonian has a local decomposition** H′ = W†HW = Σ_X h′_X with
  - K₂ := sup_y Σ_{X∋y} ‖h′_X‖ μ₂(X̄)² < ∞, where μ₂(X̄) = Σ_{s∈X̄} |pos_s − x_X|²;
  - for the floor version, also K₀ := sup_y Σ_{X∋y} ‖h′_X‖ |X̄|².

**Probe normalization.** Following vR16-7's correction (`vR16-7:5`; full report §1.1), C := V^{−1/2} Ẽ_TT(k), with Ẽ_TT(k) = W E_TT(k) W†.
- E_TT(k) = Σ_s e^{ik·pos_s} c_s E_s, where c_s = ε_jj on diagonal slots and 2ε_ij on face slots.
- ε is a unit (Frobenius) TT polarization, so |c_s| ≤ √2.
- m₁(C) := ⟨0|[C†,[H,C]]|0⟩ is a per-site quantity.

**Tails** (suggested; standard Lieb–Robinson decomposition, comparator).
- Suppose H is a sum of range-r₀ terms of norm ≤ J, and W has quasi-locality tail Φ(r). That is, W†OW = Σ_r Δ_r(O) with Δ_r supported on supp(O) + B_r and ‖Δ_r‖ ≤ ‖O‖Φ(r).
- Then K₂ ≲ J Σ_r (r + r₀ + 1)³ · (r + r₀ + 1)¹⁰ · Φ(r).
- So **Σ_r r¹³ Φ(r) < ∞ suffices.**
  - Quasi-adiabatic continuation (Hastings–Wen 2005; Bachmann–Michalakis–Nachtergaele–Sims 2012, comparator) has tails faster than any power.
  - Finite-order or optimally truncated Schrieffer–Wolff dressings have exponential tails.

---

## 2. Lemma S: the support-moment form of N0914's lemma (proved; checked)

**Statement.** Let h be an operator supported on X that commutes with every G_j, or let h = Π_X̄ h₀ Π_X̄ for any h₀ on X. Then
‖[E_TT†,[h,E_TT]]‖ ≤ 2S² k⁴ ‖h‖ μ₂(X̄)².

**Proof.**
- **(i) Pure-gauge strains.** Take any constant or linear symmetric strain field ℓ(pos). Each is G^Tα on a neighbourhood of X̄, for a polynomial α of degree ≤ 2, cut off far away (`N0914:227-237`). So Σ_{s∈X̄} ℓ(s)E_s = Σ_j α_j G_j − Σ_{s far} (…)E_s.
  - h commutes with every G_j. For h = Π h₀ Π this holds because G_j Π = g_j⁰ Π. h also commutes with far slots.
  - Hence [h, Σ_{s∈X̄} ℓ(s)E_s] = 0, and the same holds for the complex conjugate field.
- **(ii) The remainder.** Write E_TT = ℓ-part + B_X. The ℓ-part is the Taylor polynomial of e^{ik·pos}c_s of degree ≤ 1 around x_X. The remainder is B_X = Σ_{s∈X̄} r_k(s)E_s, with |r_k(s)| ≤ √2 k²|pos_s − x_X|²/2.
- **(iii) Reduce the double commutator.**
  - [h, E_TT] = [h, B_X].
  - The ℓ-part of E_TT† commutes with [h, B_X], by the Jacobi identity and the fact that E's commute among themselves.
  - So [E_TT†,[h,E_TT]] = [B_X†,[h,B_X]], with norm ≤ 4‖h‖‖B_X‖² ≤ 4‖h‖(S√2 k² μ₂/2)². ∎
- **What is new relative to R16-7's (B2):**
  - the bound needs only the support of h and ‖h‖, not a sum over its shift patterns (there are exponentially many for a generic dressed term);
  - any bounded diagonal factor, local or not, is allowed;
  - it holds as an operator norm, so in every state.

**Checked (s1 (A)).**
- With the exact N0914 stencil on a 7³ box, all 24 constant and linear symmetric strain fields are of the form G^Tα on the interior. The maximum residual is 4.8e-14, and the rank is 24 of 24.
- U(1) control (links, div):
  - the 3 constants and the 6 symmetric linear fields are pure gauge (residual ≤ 6e-14);
  - the 3 rotations ω × pos are not (residual 2.33).
- Counting reason (proved):
  - for the tensor, sym∇ maps quadratic α (3 × 6 = 18 parameters) injectively onto the 18 linear symmetric strains, because no Killing field is quadratic;
  - for U(1), ∇ maps quadratic scalars (6) into the 9 linear vector fields and misses the 3 rotations.

**Checked (s2 (M); a 2D U(1) qubit cluster, 12 links, dim 4096; an algebra check, not a phase).**
- A random dense h, twirled onto the law:
  - ‖[C†,[h,C]]‖ has slope 1.996 in k (three directions), within the U(1) support bound (ratio ≤ 0.21);
  - untwirled, the slope is −0.008 (O(1)).

**Checked (s1 (B)).** Planar "Airy" rectangles are exactly invariant qubit hops (`s1 .out`).
- Construction: m_aa = Δ_bb φ, m_bb = Δ_aa φ, m_ab = −∇⁺_a∇⁺_b φ, with φ the indicator of an L₁ × L₂ rectangle.
- For L ≥ 2 the entries lie in {−1, 0, 1}. Gm = 0 exactly, and the 0th and 1st moments are 0.
- The TT symbol has slope 3.96–4.00 in every direction where it is nonzero.
- The ratio to the support-moment bound is ≤ 0.55.
- L = 1 needs entries −2 (spin ≥ 1).

---

## 3. Lemmas P and F: only the law-obeying block of the dressed H enters the f-sum (proved; checked)

**Lemma P (proved).** Under (W1):
m₁(C) = V⁻¹ ⟨0′|[E_TT†,[H″,E_TT]]|0′⟩, where H″ := Σ_X Π_X̄ h′_X Π_X̄.
- E_TT is diagonal in the E basis, so it maps 𝓗₀ into itself. Each of the four terms of the double commutator is therefore a matrix element ⟨u|H′|v⟩ with u, v ∈ 𝓗₀.
- For u, v ∈ 𝓗₀, ⟨u|H′|v⟩ = ⟨u|H″|v⟩, because Π_X̄ = 1 on 𝓗₀.
- H″ commutes with every G_j, and ‖Π h′ Π‖ ≤ ‖h′‖. ∎
- **No block-diagonalization of H′ is needed.**
  - H′ may still create and destroy vector charges.
  - Only the dressed ground state must lie in the law sector.
  - This is weaker than the Schrieffer–Wolff "effective Hamiltonian" hypothesis in the registration (`TESTS:5495`).

**Lemma F (floor; proved).** Without (W1), write h′ = Πh′Π + (rest), and let D_X = [E†,[h′_X,E]]. Since E commutes with Π, Cauchy–Schwarz gives |⟨rest-part⟩| ≤ ‖D_X‖(2√q_X + q_X).

**Checked (s2 (P), (F)).**
- For ψ ∈ 𝓗₀ and a law-violating H′ (max |[G,H′]| = 7.0), m₁(H′) = m₁(H″) = 0.030706358576, with difference 0.
- With leakage η = 1e-3 to 0.3, |Δm₁| = 1.4e-4 to 4.9e-2, always inside the Lemma F bound (a loose bound).

---

## 4. Theorem B′: the dressing transfer (proved)

**Statement.** Assume finite slots, (W1) and (W2). For every TT polarization and every probe A:

m₁(C) ≤ 2S² K₂ k⁴ + F,  with F = 0 under exact (W1), and F ≤ 8S² K₀ (2√q + q) in general;

χ_AA ≥ |⟨[C, A]⟩|² / m₁(C)   (Bogoliubov, `R16-7:41`, V^{−1/2}-normalized as `vR16-7:5` requires).

**Proof.** Lemma P (or F), then Lemma S term by term, then V⁻¹Σ_X ≤ sup_y Σ_{X∋y}, then Bogoliubov. ∎

**Corollary B2′ (proved; this is R16-7's B2, `R16-7:168`, transported).** If the dressed TT electric susceptibility χ_{CC} ≥ c_E > 0, then H has an excitation connected to |0⟩ by Ẽ_TT with ω² ≤ (2S²K₂k⁴ + F)/c_E. The spectrum is frame-independent, so this is a statement about the microscopic H.

**Corollary B-inv (proved): the bound in gauge-invariant form, answering vR16-7's observable objection (`vR16-7:5`; full report §1.3).**
- **The probe.** Take any exactly invariant hop pattern m (for example an Airy rectangle, or an R-row for rotors), and the local, gauge-invariant "sine-curvature" probe A_m(k) = V^{−1/2} Σ_x e^{−ikx} i(T_{m,x} − T_{m,x}†), dressed as Ã_m = W A_m W†. For rotors, i(T − T†) = −2 sin(m·h).
- **The vertex.** [E_s, T_m] = m_s T_m gives ⟨[C, Ã_m]⟩ = i (c·m̂(k)) ⟨0′|T_m + T_m†|0′⟩. Its size is |c·m̂(k)| = k² a_m(k̂)^{1/2} + O(k³).
- **The bound.** Hence χ_{ÃÃ}(k) ≥ a_m(k̂) ⟨T_m + T_m†⟩′² k⁴ / (2S²K₂k⁴ + F).
  - With F = 0, this is a **k-independent positive lower bound** whenever the dressed curvature hop has a nonzero expectation.
  - No conjugate coordinate and no division by a vanishing vertex are used.
- **The Gaussian comparators** (from the repo's TT forms, `N0914:69-74`; `vR15-5:18-21`). The local invariant curvature probe has the static susceptibility χ_RR = k⁴ χ_hh^TT:
  - Einstein–Hilbert (h:R(h)): χ_RR ∝ k²/g → 0;
  - curvature-squared (|R|², Pretko vector-charge type): χ_RR ∝ 1/g, constant.
- **So, in every phase obeying (W1) and (W2) with ⟨T_m + T_m†⟩′ ≠ 0 for some invariant m with a_m ≠ 0, the Einstein–Hilbert curvature susceptibility is excluded** for k² ≲ g⟨T + T†⟩′²/(2S²K₂Z). Z is the comparator's normalization.
  - With a floor, the exclusion holds on the window √(ZF/(g⟨T + T†⟩′²)) ≪ k ≪ √(g⟨T + T†⟩′²/(2ZS²K₂)) (reading of the comparator).
- **Checked, U(1) form (s5; the 12-link cluster, exactly invariant ring-exchange H with a random diagonal term; algebra check, not a photon).** For k = 1e-3 to 0.3 along two directions:
  - the vertex scales as k (2.421e-3 at k = 1e-3) and m₁ as k² (2.421e-6);
  - the lower bound |vertex|²/m₁ = 2.42105 is k-independent;
  - χ_AA = 2.42105 equals it. It is saturated because, on this cluster, the sine-ring probe is proportional to the transverse current.
- **What is still a bridge (reading).** The statement covers every local gauge-invariant curvature readout with a nonzero vertex. It does not cover:
  - a readout whose vertex vanishes (all dressed curvature hops "disordered", ⟨T + T†⟩′ = 0);
  - a non-local readout.

  AX:85-90 leaves the physical readout to a separate bridge.

---

## 4a. Which of vR16-7's two gaps the dressing transfer closes

**What is transferred.** The referee-corrected Theorem B (`vR16-7:5,17`):
- the V^{−1/2}-normalized TT-electric f-sum is O(k⁴);
- normalized conjugate probes obey the Bogoliubov lower bound;
- χ_EE^TT ≥ c_E > 0 forces an excitation with ω ≤ Ck².

Theorem B′ and B2′ (§4) are exactly these three statements for the dressed operators. **R16-7's INCONCLUSIVE is not upgraded.**

**Gap 1: the optimized probe ratio is not identified with a physical metric susceptibility** (`vR16-7:5`; full report §1.3: "a local curvature character has a commutator vertex that itself vanishes as k²"). **Narrowed, not closed.**
- **What B-inv does (proved).**
  - It keeps the local curvature character as the probe and does not divide out its vanishing vertex.
  - The squared vertex (∝ k⁴) and the f-sum (≤ 2S²K₂k⁴) cancel. This leaves a k-independent lower bound on the static susceptibility of a local, Hermitian, gauge-invariant observable: χ_{A_mA_m} ≥ a_m(k̂)⟨T_m + T_m†⟩′²/(2S²K₂) + O(k).
  - No conjugate coordinate is used. The same holds with W = 1, so B-inv is a repair of Theorem B itself, which the dressing then transports.
  - For a general local invariant probe a_y, the same argument gives χ_AA ≥ |v(k̂)|²/(2S²K₂) + o(1). Here v is the k²-coefficient of ⟨[C, A]⟩, and only its quadratic Taylor part survives by Lemma S (proved).
- **What it excludes.** Einstein–Hilbert, in the Gaussian comparator, gives this probe χ_RR ∝ k²/g → 0 (`N0914:72-74`). So Einstein–Hilbert is excluded for every physical curvature readout that is (i) local, or quasi-local with summable moments, and gauge-invariant, and (ii) has a nonzero k²-vertex.
- **What it does not do.**
  - It does not prove that the physical metric or curvature readout is such an operator. That is the `AX:85-90` bridge (P-r16-11c).
  - It does not cover zero-vertex readouts (⟨T + T†⟩′ = 0, the curvature hops "disordered") or non-local readouts.
  - The Einstein–Hilbert side is a Gaussian comparator, not a finite-slot computation.
- **Net effect.** The gap shrinks from "an unspecified finite-slot metric susceptibility" to "local invariant readouts with vanishing vertex, or non-local readouts".

**Gap 2: the U(1) control did not pass in the registered sense** (`vR16-7:13`). **Not closed.**
- My U(1) statements (§5; s2 (M)) are again operator identities on a 12-qubit 2D cluster. For U(1), B-inv gives χ_BB ≥ const whether or not a photon exists. That is consistent with Maxwell but is not a measurement of a 3D emergent photon.
- R16-11's registration has no control clause (`TESTS:5509-5512`), so its reading is not gated on gap 2. Any use of R16-7's PRODUCED / NOT-PRODUCED rubric still needs a real 3D control, which was not attempted here.
- **Reading.** The tensor exclusion is a lower-bound no-go. It needs the bound to be true, not the method to detect a gapless phase. So gap 2 limits what the method can certify as present, not the exclusion.

---

## 5. (b) Reconciling with spin ice

- **The U(1) case transfers identically (proved, the same proof).**
  - In the U(1) version of Lemma S only the constant field is pure gauge, so ‖[E_T†,[h,E_T]]‖ ≤ 4‖h‖(S Σ|c_s| k |pos − x|)², which is O(k²) (s2 (M): slope 1.996).
  - Quantum spin ice at large J_zz is the textbook case of (W1) and (W2): perturbative ring exchange from a law-violating J_± (comparator: Hermele–Fisher–Balents 2004).
  - Its dressed f-sum is O(k²), and B-inv gives χ_BB ≥ const.
  - Maxwell has χ_BB = k²χ_AA = const. **No conflict:** the photon emerges because Maxwell's minimal invariant has a k-independent susceptibility, not because dressing evades a bound (reading of a proved statement).
- **Is the tensor obstruction specifically the k⁴ moment structure, and does dressing preserve it?** Yes, both (proved).
  - The structure belongs to every local operator commuting with the integer vector law: 24 of 24 constant and linear strains are pure gauge (§2).
  - Lemma P shows that dressing lands, block-restricted, in exactly that class.
  - The difference from U(1) is one count: 18 = 18 for the tensor against 6 < 9 for U(1).
  - In invariant language, both bounds say "minimal-invariant susceptibility ≥ const". The tensor case differs because the target theory, Einstein–Hilbert, needs that susceptibility to vanish like k². Its Hamiltonian h:R(h) is not a sum of squares of local invariants: it is indefinite, and it contains the non-invariant h itself (`N0914:72-83`, `vR15-5:6`).
- **The tensor analogue of spin ice (checked; suggested consequence).**
  - Take H = UΣ_j(G_jE)² − J_⊥ΣS^x on qubits.
  - The minimal exactly invariant qubit hop has weight w = 20. This is the optimum of an integer program in 4³ and 6³ boxes, with diagonal or face slot fixed; it is non-planar or planar Airy, extent 3 × 3 × 2 (s4).
  - No invariant pattern has ≤ 2 slots (s1 (C), 26,406 patterns tested). So:
    - the first off-diagonal invariant term arises at Schrieffer–Wolff order 20, with amplitude ~ J_⊥²⁰/U¹⁹;
    - the first-order projection of R13-2's two-slot 𝒟₀ term (sin h·B_N·sin h) has no hopping part: only its diagonal piece (from sin²h_s) survives. Proved: every non-diagonal hop in it is a ≤ 2-slot pattern, and such a pattern has a nonzero 0th or 1st moment, so it cannot be invariant.
  - Compare spin ice, whose ring term appears at order 3 (comparator).
  - Diagonal terms at order 2 should dominate the tensor-ice manifold long before order 20 (suggested). The transferred bound says that even if a liquid forms, its TT stiffness is curvature-squared (z = 2 at best, `vR15-5:20`), not Einstein–Hilbert.

---

## 6. Is a tail condition needed? A power-law boundary example (checked; scope)

- **The model (s3).** Exactly invariant, qubit-compatible planar Airy L × L hops in all three planes, with weight L⁻ᵖ per site per plane, L = 2…2·10⁴, unit ⟨cos⟩.
- **The symbol.** c·m̂ = −φ̂_L(k_a,k_b)(tᵀεt). The analytic formula matches the explicit patterns to 2.7e-15.
- **Results** (slopes for k = 3e-3 to 3e-2):

| p | 2.5 | 3 | 4 | 5 | 6 | 8 | 12 |
|---|---|---|---|---|---|---|---|
| m₁_TT slope (body / generic directions) | 1.50 | 2.00 | 2.99 | 3.81 (log) | 3.99 | 4.00 | 4.00 |

- **So m₁ ~ k^{min(4, p−1)}.**
  - At p = 3 the f-sum is k² on generic directions. On directions with a vanishing in-plane momentum component it carries a log(L_max) divergence (face direction slope 2.12). p = 3 is therefore marginal.
  - The transverse-trace (scalar) channel gets a positive stiffness of the same power. There is no conformal-sign attraction, so Newtonian attraction would still need P-r16-7b.
- **Reading.**
  - An exact-law, compact, qubit-compatible Hamiltonian with r⁻³ hop range has an "Einstein–Hilbert-power" TT f-sum and, harmonically, z = 1 TT modes.
  - Some tail condition is therefore needed in the theorem. My sufficient condition (Σ r¹³Φ < ∞; for this family the support form needs p > 11, the pattern form B2 needs p > 7) is not sharp, since k⁴ already holds for p > 5.
  - This is not a quasi-local dressing. It is a B2-violating bare H, so it does **not** meet FAILS-TO-TRANSFER as registered.

---

## 7. Finite U: what the rigorous dressings give (suggested; comparator)

- At U ≫ J, prethermalization theory (comparator: Abanin–De Roeck–Ho–Huveneers 2017) supplies a quasi-local W with exponential tails such that W†HW = U·N + D + V′, with [D, N] = 0 and ‖V′‖_loc ≤ e^{−cU/J}. Here N = Σ_j(G_jE)² has integer spectrum, as required. This is RECALLED and its hypotheses were not re-checked here.
- **Suggested consequences:**
  - a dressed-frame charge probability q ≲ (e^{−cU/J}/U)² by a variational argument, assuming charges cost ≥ U − O(J) in D;
  - so Theorem B′ holds with an exponentially small floor F, and Einstein–Hilbert is excluded on k_− ~ F^{1/4}-scale to O(1).
- **Relation to Lemma W.** This is R15-5 Lemma W's regime (`R15-5:178-192`), but:
  - resummed to optimal order;
  - in f-sum rather than dispersion form;
  - for the integer QLM law, where the N > 36nM lifting issue of `vR15-5:33` does not arise.
- **What is not known.** Whether the floor is a real infrared effect or an artefact of the asymptotic construction. In a deconfined phase with gapped charges I expect an exact dressing to exist and F = 0 (suggested, not proved).
- **At U ~ J no W is constructed.** There (W1) and (W2) are the hypotheses the registration poses, not results.

---

## 8. (c) What remains open

1. **Phases with no dressing satisfying (W1) and (W2) with Σ r¹³Φ < ∞.** This sharpens P-r16-7a into the precise negation of (W1) and (W2). It includes:
   - critical points and gapless dressings with power-law tails, which §6 shows can change the power;
   - first-order transitions out of the constrained limit;
   - U ~ J regions where no W is known to exist.
2. **Gapless intermediate phases.**
   - Hastings-type quasi-adiabatic continuation needs a spectral gap along the path, so it does not apply to the gapless emergent phase itself (comparator).
   - Theorem B′ needs no gap: (W1) and (W2) are its only inputs.
   - The constructive route (§7) needs only the penalty gap U ≫ J. Gaplessness of D is harmless there.
3. **Mod-N clocks with a modular law** (`N0914:218-223`; `R16-7:224-230`). Lemma S needs the integer law. Dressing does not supply lifting.
4. **Rotors (unbounded E).** Lemma S uses ‖E_s‖ ≤ S. For rotors, the dressed H″ needs R16-7's pattern-moment hypothesis (B2) directly, and that is not implied by Lieb–Robinson tails.
5. **The readout bridge.** This covers zero-vertex curvature readouts (⟨T_m + T_m†⟩′ = 0 for every invariant m with a_m ≠ 0) and non-local readouts (§4).
6. **The scalar channel.** Theorem D is basis-dependent (E-basis stoquasticity). A dressed H′ need not be stoquastic even if H is, so D does **not** transfer automatically (suggested). P-r16-7b is untouched.
7. **Not addressed:** fermionic slots, matter, nonlinear gravity, Λ.

---

## 9. (d) Prices (named, never adopted)

| Price | Axiom touched | Buys |
|---|---|---|
| **P-r16-11a**: the vector law emerges with **no** quasi-local dressing of the ground state into the law sector: (W1) or (W2) fails, for example a critical or power-law dressing. This sharpens P-r16-7a. Unbuilt | none; a dynamical hypothesis | the only finite-slot integer-law route left to an Einstein–Hilbert TT f-sum (Theorem B′) |
| **P-r16-11b**: power-law-ranged exactly invariant hops, weight ≲ r⁻³ to r⁻⁵ | Admissibility (nearest-neighbour rule, `AX:57`) if fundamental; if emergent, a gapless mediator, which is then P-r16-11a | m₁ ~ k^{p−1}, k² at p = 3 (§6). Comes with a positive scalar stiffness, so P-r16-7b is still needed |
| **P-r16-11c**: the physical curvature or metric readout is non-local, or its curvature vertex vanishes (⟨T + T†⟩′ = 0) | Record readout bridge (`AX:82`; `AX:85-90` says it must be supplied) | escapes Corollary B-inv |
| Carried over: P-r16-7b (sign problem or scalar-law violation) | none | scalar attraction (Theorem D); not affected by dressing |

---

## 10. Readings against the FIXED clauses (`TESTS:5509-5512`)

- **TRANSFERS: yes (worker reading, proved, unrefereed). It is a no-go, so it goes to the referee.**
  - **The bound.** Theorem B's bound holds for dressed operators, m₁(Ẽ_TT) ≤ 2S²K₂k⁴ with χ_AA ≥ |⟨[C,A]⟩|²/m₁, in every phase connected to the constrained limit by a quasi-local dressing.
  - **"Connected" means:** (W1) the dressed ground state lies in the law sector, and (W2) the dressed Hamiltonian has a finite second-moment sum K₂.
  - **Stated tails:** Σ_r r¹³Φ(r) < ∞ (polynomial, faster than r⁻¹⁴), which includes stretched-exponential and quasi-adiabatic tails.
  - **Scope:** finite slots (QLM, qubits included) with the integer vector law.
  - **Additions:**
    - the gauge-invariant form B-inv, which also answers vR16-7's conjugate-probe objection for local readouts with a nonzero vertex;
    - the floor version for approximate dressings.
  - **What is transferred** is the referee-corrected Theorem B (`vR16-7:5,17`), not a NOT-PRODUCED-EVIDENCE; R16-7 stays INCONCLUSIVE.
  - **vR16-7's gaps** (§4a): gap 1 (the observable) is narrowed to zero-vertex or non-local readouts; gap 2 (the U(1) control) is not closed.
- **FAILS-TO-TRANSFER: no.**
  - No quasi-local dressing class gives a dressed m₁ of O(k²).
  - The boundary example in §6 (exact law, r⁻³ hop range, m₁ ~ k², checked) is outside the registered dressing class (`TESTS:5501`). It is recorded as a scope marker, not as this reading.
- **OPEN: not as a reading of the registered conditional question.** OPEN does remain for the existence of a dressing at U ~ J and for the items in §8.
- **Expectation check** (`TESTS:5513`).
  - The registered expectation matches, with two differences:
    - the needed tails are much weaker than stretched-exponential (polynomial suffices);
    - only the ground state must be dressed into the law sector, not the Hamiltonian.
  - "Only phases not connected to the constrained limit" remain. That is now a precise condition, the negation of (W1) and (W2), and §6 shows it is not empty in principle.

---

## 11. Strong-word check and scope

- **"Proved"** (all unrefereed) is used for: Lemma S, Lemma P, Lemma F, Theorem B′, Corollaries B2′ and B-inv, the counting 18 = 18 against 6 < 9, and the absence of hopping terms in the first-order projection of 𝒟₀.
  - These rest on N0914's pure-gauge-strain fact. vR16-7 independently confirmed it (`vR16-7:7`), and s1 (A) checks it here.
- **"Checked"** is used for s1–s5. These are algebra and symbol checks, plus one 12-qubit algebra check. **No phase was computed.** No 3D emergent-photon or graviton susceptibility was measured.
- **"Exactly"** is used for: Gm = 0 (integer arithmetic), the equality m₁(H′) = m₁(H″) on 𝓗₀, and pure gauge for 24 of 24 strains (to 5e-14).
- **"Suggested"** is used for:
  - the tail-to-K₂ translation (standard Lieb–Robinson bookkeeping);
  - the §7 finite-U floor estimates;
  - "an exact dressing exists in a deconfined phase";
  - "diagonal terms dominate tensor ice";
  - "D does not transfer".
- **Comparators (RECALLED, not fetched):** Hermele–Fisher–Balents 2004; Hastings–Wen 2005; Bachmann–Michalakis–Nachtergaele–Sims 2012; Bravyi–Hastings–Michalakis 2010; Abanin–De Roeck–Ho–Huveneers 2017; Pretko 2017 (vector-charge theory, z = 2); Xu 2006 (soft graviton).
- **Not covered:** mod-N clocks, rotors (unbounded E), fermions, matter, the scalar channel, nonlinear gravity, Λ, and the existence of W at U ~ J.

## Files (`S/scripts/`)

- `s1_gauge_strains_and_patterns.py` / `.out`: pure-gauge strains, tensor against U(1); Airy qubit hops (exact Gm = 0, moments, slope 4, support bound); no ≤ 2-slot invariant patterns; single flips O(1).
- `s2_block_identity_and_floor.py` / `.out`: Lemma P equality, Lemma F bound and the U(1) Lemma S slope on a 12-qubit cluster.
- `s3_tail_threshold_powerlaw_airy.py` / `.out`: the power-law Airy family, m₁ ~ k^{min(4, p−1)}.
- `s4_min_qubit_invariant_hop.py` / `.out`: integer program, minimal qubit invariant hop weight 20.
- `s5_invariant_probe_bound.py` / `.out`: B-inv in U(1) form. The vertex goes as k and m₁ as k², so the bound on a local invariant probe is k-independent (saturated on the cluster).
