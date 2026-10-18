# Route F5: dissipative and record-driven dynamics as a way past doubling

**Agent:** route agent F5, Claude Opus 5.5. This is the same model family as the supervisor, so it is not an independent referee. Worked 2026-10-14, 13:19–13:55Z.
**Framework Refresher Read:**
- read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md`;
- read: `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (the generated baseline of the three approved primitives);
- read: the head of `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`;
- packet: `WALL.md`, `ASSUMPTIONS.md` and `step0/PRIOR_ART.md` (with `cluster_A_record_side.md`);
- read: the branch note LATTICE_HANDEDNESS, sections T1–T5;
- read: exercise SKILL steps 4 and 6, and the proof-search governance file.

None of the approved primitives touches this route. Scale-reference is used only to convert lattice units to GeV in the bounds below.
**Labels:**
- **proved**: a proof or proof skeleton given here, with its open steps named;
- **checked**: a finite or numerical run in this folder;
- **suggested**: an argument that has not been checked;
- **reading**: an interpretation;
- **comparator**: a supplied model.

Every Lindblad model below is a supplied comparator. The axioms supply no dynamics (`docs/MINIMAL_AXIOMS_2026-06-29.md:114-123`). Decoherence mechanisms, update laws and record-production dynamics are listed as outside the axioms (`:182-186`).

## Plain summary

1. **Losses can remove the mirrors from the spectrum.** A grid can be given losses so that the seven mirror partners decay at once and the one wanted handed particle does not. The losses need only nearest-neighbour or next-nearest-neighbour reach. The proof that rules out handed ticks needs the update to be reversible, so it does not apply here.
2. **The mirror's twist moves into the vacuum instead.** In any state built from independent fermion modes, the topological twist the mirror carried has to sit somewhere in the vacuum. It sits in one of three places: a mirror node, a sharp filled/empty edge in momentum, or a blurred (mixed) region.
3. **Local losses cannot keep the vacuum right near the wanted particle.** Near that particle, the losses leave upper and lower states equally occupied on average.
4. **Read literally, the Record axiom allows one record per site.** The loss channel uses that up within a few ticks, and afterwards the grid is reversible again and the mirrors return.
5. **One mechanism checked out, but only in a lower-dimensional toy.** An absorbing far wall on a two-sided slab removes the far-side mirror without the mirror just moving one row inward.
6. **The same toy shows a new cost.** The absorbing wall also drains the slab's interior.
7. **Absorbing only above zero energy is no better.** A sink can be built that takes only particles above zero energy and holes below it. That keeps the vacuum filled, but the smeared-out mirrors then conduct electricity at about the Planck rate (checked: σ ≈ 5·10⁻³ e²/ħa). The vacuum would absorb light within about 10⁻⁴⁰ s.
8. **Verdict on the lens.** Both kinds of sink fail, for opposite reasons. The lens does not open a door of its own. It turns the spectrum problem into a vacuum-state problem. Removing the mirror's twist from the vacuum needs a vacuum that is not built from independent modes, which means interactions: the symmetric-gapping route.

## Routes

| Route | Family (object, mechanism, terminal obligation) | Premise it drops or changes | What you would have to believe | First artifact | Cost | What it would change if it worked |
|---|---|---|---|---|---|---|
| **F5-A** Dissipative Wilson walker | Object: a quasi-free Lindbladian on the walker `h = Σ sin k_j σ_j`, with gauge-covariant loss/gain jumps `L = √κ Δ^m c` (range m). Mechanism: the point-gap winding `W3[h_eff − E_ref] = −1` of `h_eff = h − (i/2)Γ`, `Γ = κ f^{2m}`, `f = Σ(1−cos k_j)`. Terminal obligation: a vacuum that is the filled light sea, with jumps compatible with Record, for all time. | A3: the dynamics is Hermitian or unitary. Also LATTICE_HANDEDNESS T2's premise that `U^{-1}` is a Laurent polynomial (branch note `:128-130`). | That record formation is a Markov sink of unlimited capacity, and that a local sink can hold the light sea. | `f5_t1_dissipative_walker.py` (run) | done | It would give a one-handed light spectrum from NN or NNN dissipation. **Killed on both horns.** A Markov sink fails under the literal Record axiom (Lemmas B, C, P and D, test T1). An energy-selective sink gives a Planck-conductivity vacuum (T3′, checked). |
| **F5-B** Absorbing far wall: records as the far wall of an inflow slab | Object: a Hermitian Chern/inflow slab Z³×{1..L} whose last layer feeds a loss sink. Mechanism: inflow puts one hand on the near wall, and the far-wall mirror becomes damped rather than gapped by SMG. Terminal obligation: in 3+1D with SM content, the far mirror is damped with no Zeno relocation, the bulk sea is not drained, the vacuum has no Ohmic response, and the record register never fills. | A6 (an extra coordinate), plus A3 at the far wall only. It replaces far-wall SMG (Golterman–Shamir; `SPIN10…:195-221`) with absorption. | That the record register behind the far wall can absorb without draining the bulk, and without making the vacuum a lossy conductor for the shared gauge fields. | `f5_t2_lossy_far_wall.py`, `f5_t2b_generic_mass.py`, `f5_t3a_bulk_drain.py` (all run) | T4 (below), about 20 min; a 3+1D slab, about 1 day | It would give an alternative to far-wall SMG for the domain-wall route. **Wounded.** The mechanism passes in 1+1D (T2/T2b), but the Markov wall drains the bulk sea (T3a). An energy-selective wall should conduct at the Planck scale (T3′'s mechanism; slab test T4 not run). |
| **F5-C** Reduction: "the doubler moves into the state" | Object: a translation-invariant Gaussian state ρ(k) on T³. Mechanism: Berry-flux bookkeeping (Lemma B). Terminal obligation: a non-Gaussian vacuum that carries the compensating flux without a node, a filled/empty edge or a mixed region. | None new. It shows that the lens's obligation is the SMG obligation (A5) at the level of the state. | That any open-system escape ends at the same lemma as symmetric mass generation. | Lemma B proof (below) | done | Fold this lens into SMG plus inflow; do not run it as an independent family. Gives SMG one extra, cheap diagnostic: the vacuum's Berry-flux budget. |

---

## Route F5-A: construction, lemmas and test T1

**Construction (comparator, with its admissibility checks).**
- Hamiltonian: `H = Σ_x c_x† (Σ_j −(i/2)σ_j)(c_{x+e_j} − c_{x−e_j})`. In Bloch form this is `h(k) = Σ sin k_j σ_j` (block 68's walker, `PRIOR_ART.md:61`).
- Loss jumps: `L_{x,s} = √κ Σ_j (c_{x,s} − ½(c_{x+e_j,s} + c_{x−e_j,s}))` for each component s. This is range 1 and gives `Γ(k) = κ f(k)² · 1`. Iterating the Laplacian m times gives `κ f^{2m}`. Below, `p ≡ 2m` is the power of f in Γ = κ f^p, so Γ ∝ q^{2p} near the node.
- Optional gain jumps use the same symbol with `c → c†`.

Checks:
- **CPTP.** It is in Lindblad form. [proved]
- **Locality.** Range m. [proved]
- **Covariance.** It is covariant under translations and the 24 proper rotations (Γ is a scalar invariant). [proved]
- **Gauge covariance.** Insert links in the Laplacian. The jumps are charged, so charge leaves the system: the U(1) is only a weak symmetry. [proved]

**Lemma A1 (escape, proved; checked).**
- `W3[h_eff − E_ref] = −1` for `0 < Im(−E_ref) < min_{doublers} Γ/2`. The map `k ↦ (d(k), Γ/2 − |E_ref|)` reaches the "south" direction only at k = 0, with chirality +1 (degree count). Γ = 0 gives 0.
- T2's proof needs `U^{-1}` to have Laurent-polynomial entries (branch note `:128-130`). `h_eff − E_ref` is finite range, but its inverse is not. So T2 does not apply.
- Checked: W3 = −1.000000 for f^1, f^2 and f^4 (`f5_t1_output.txt`, section 1). Controls: Hermitian 0.000; normalisation map ±1/0.
- This is the Bessho–Sato mechanism: Weyl chirality in non-Hermitian systems is balanced by bulk point-gap winding (literature row L1).
- Light spectrum: one undamped Weyl node. The seven doublers decay at rates `κ(2·hw)^{2m}` (16, 256 and 1296 for f⁴).
- The light-mode damping `Γ(q) ≈ κ(qa)^{2p}/2^p` is irrelevant in the infrared.

**Observational bound (checked arithmetic).** With κ ~ 1 in Planck units, take `Γ ∝ q^{2p}`:
- p = 2 (range-1 jumps): a 10¹¹ GeV cosmic-ray constituent decays in about 10⁻¹¹ s. Excluded.
- p = 4 (range-2 jumps, Δ²): the lifetime is about 4·10²² s. Allowed.
- So the route needs jumps of range at least 2 (Δ²).

**Lemma B: Gaussian-state doubling (proved).**
- Let ρ(k) be a continuous rank-1 projector field on T³∖Z, with Z finite.
- Then the Berry fluxes through small spheres around the points of Z sum to 0.
- Proof: Stokes on the compact manifold T³ minus balls, applied to the curvature of the line bundle Im ρ.
- Corollary: a Gaussian vacuum that equals one Weyl node's filled sea near the node (flux ±1) must carry flux ∓1 elsewhere. That can be:
  - a mirror node;
  - a rank change (a filled/empty discontinuity, i.e. a Fermi surface, which carries Chern number à la Haldane);
  - a set where ρ is not a projector (a mixed state).
- Scope: Gaussian (quasi-free) states only. Correlated states are not covered.

**Lemma C: analytic sinks give analytic steady states (proved, skeleton).**
- Suppose the jump symbols are real-analytic (finite range or exponentially local), and the damping matrix `X = ih + Γ/2` has spectrum in Re > 0 for k ≠ 0.
- Then the unique steady state `ρ_ss`, the solution of `h_eff ρ − ρ h_eff† = −iN`, is real-analytic on T³∖{0}.
- By the identity theorem: if `ρ_ss` is pure on an open set, it is pure everywhere on that connected set, with constant rank.
- With Lemma B: either `ρ_ss` is mixed on an open dense set, so jumps fire at rate r > 0 forever, or it is a constant-rank pure state with zero flux around the node, so the node's sea is not filled.
- Open step: uniqueness of `ρ_ss` per k, which is standard when X is stable.

**Lemma P: parity lemma (proved, skeleton; checked).** Near an undamped node, take the leading homogeneous terms of the gain matrix N and the loss matrix M:
- **They are even.** A PSD matrix function's leading homogeneous term has even degree (an odd term would be both ≥ 0 and ≤ 0).
- **Occupations follow from the secular limit.** Since `|q| ≫ Γ`, the steady-state band occupations are `n_± = ⟨±|N|±⟩/⟨±|M+N|±⟩`.
- **Parity links the two bands.** `|+(q̂)⟩ = |−(−q̂)⟩`, so with equal leading degrees `n_+(q̂) = n_−(−q̂)`, and the sphere averages are equal. If gain dominates, `n_± → 1`. If loss dominates, `n_± → 0`.
- **Conclusion.** In every case the direction-averaged deviation from the Dirac sea, `e_sea(q) → 1` as q → 0.
- **Handedness does not help.** Mirror-handed (P-odd) dissipators cannot evade this, because evenness comes from positivity, not from mirror symmetry.
- Open step: control of the band-coherence terms, which are `O(Γ/|q|)`.

**Lemma D: record capacity (proved, under a reading).**
- Reading: every jump writes one permanent record at a Z³ site, a site never carries more than one record (`MINIMAL_AXIOMS:79-80`), and a jump with no free record slot cannot occur.
- Then `∫₀^∞ r_x(t) dt ≤ 1` for every site x.
- Gain-containing sinks have r > 0 forever (Lemma C), so they violate the bound after a finite time.
- A loss-only sink drains the light sea. Starting from the filled sea, it writes 0.98–1.00 records per site within 10–10⁶ ticks (checked, T1 §5). That exhausts the capacity.
- After that no jump can fire, the dynamics is Hermitian, and T1 (balance) applies again.

**Relaxed shell.** Suppose the infrared sea is simply inherited from the initial state. Modes with `Γ(q)·t_age > 1` have relaxed anyway:
- for p = 4, every mode above q* = 4.2·10¹¹ GeV has relaxed (checked arithmetic, T1 §5);
- by Lemma P that shell is at O(1) deviation from the sea;
- its energy density is about q*⁴ ≈ 3·10⁴⁶ GeV⁴, against a critical density of about 4·10⁻⁴⁷ GeV⁴ (suggested, by about 90 orders);
- pushing q* to near the cutoff (qa ≈ 0.15) needs p ≈ 31, that is jumps of range about 15. Even then a relaxed propagating window remains for any analytic symbol.

**Test F5-T1** (pre-registered 13:33Z in `PREREG_T1.md`; output `f5_t1_output.txt`).

Members searched:
- the scalar family with p = 1, 2 and 4;
- 12 random local families (3 loss + 2 gain, range-1 symbols × f^m, m = 1, 2).

Results [checked]:
- **Point-gap winding.** W3 = −1 exactly for the scalar family. For the random families it is not converged: min singular value 3·10⁻³–3·10⁻², and the point gap can close where Re λ = 0 crosses intermediate damping, so the value there is not interpretable.
- **Jump rate.** r > 0 for every gain-containing member: 1.1–10.5 for the scalar family, 30–600 for the random ones. Loss-only members have r = 0, with an empty steady state.
- **Sea error.** `e_sea` → 1 for every member: exactly 1.0 for the scalar family, 0.993–1.005 at q = 0.03 for random m = 1.
- **Parity relation.** The deviation `max|n_+(q̂) − n_−(−q̂)|` shrinks linearly in q: 0.23 → 0.078 → 0.023 for q = 0.3 → 0.1 → 0.03 (Lemma P).
- **Controls.** The dark-state insulator gives r = 0 and mixedness 0. The Hermitian limit gives W3 = 0.

**Verdict against the pre-registered readings:**
- PASS is not met by any member.
- FAIL as worded ("r bounded away from 0 and e_sea → 1") is met by every gain-containing member. Loss-only members have r = 0 but `e_sea = 1`, so they fail PASS on the sea clause. The FAIL wording did not anticipate the empty dark state; the capacity follow-up (§5) covers it.
- Resource note: T1's peak resident memory was 309 MB for 5 s, above the 0.25 GB guideline. T2, T2b and T3a peaked at about 32 MB.

---

## Route F5-B: absorbing far wall, tests T2, T2b and T3a

**Idea.** Keep inflow (A6) for the near wall's single hand. Replace the problematic far-wall step with absorption: the last layer feeds the record sink. Prior attempts failed at exactly this step:
- the partner Weyl lives at the end of a record-time interval (`THE_RECORD_TIME_DOMAIN_WALL…:69-71`);
- the frozen Spin(10) boundary pushes eight doublers inward (`SPIN10…:195-221`).

**F5-T2/T2b** (QWZ strip, the 1+1D analogue, which is not closure per `WALL.md:47`; `f5_t2_output.txt`, `f5_t2b_output.txt`) [checked]:
- **Readings.** PASS is met for Γ ∈ [0.1, 30] at m = −1, −1.5 and −0.5.
- **Light content.** Exactly one light in-gap branch, near the edge. Its decay is ~10⁻¹⁶ at m = −1 (the edge is one row thick) and scales as `e^{−2Ly/ξ}`, ξ ≈ 1.45, at m = −1.5: 2.5e−4, 1e−6 and 4e−9 for Ly = 8, 12 and 16.
- **Far-wall mirror.** It decays at rate ≈ Γ for Γ ≲ 3. For Γ ≥ 10 the decay falls as ~4/Γ (Zeno), down to 0.04 at Γ = 100. It is never light: no far-localised state has decay below 10⁻².
- **Answer to the question.** Absorption does not just push the mirror inward, unlike the frozen boundary.

**F5-T3a** (pre-registered 13:42Z; `f5_t3a_output.txt`) [checked]:
- **Readings.** PASS is not met.
- **Bulk drain.** The Markov wall drains the whole bulk valence sea. At Ly = 20, 99.5% of valence states decay faster than 10⁻⁴, with median ≈ 1.4–2.9·10⁻² scaling as 1/Ly (0.054, 0.029, 0.018 at Γ = 1).
- **What survives.** Only 0.2% have decay below 10⁻⁶: the light branch's own near-edge sea.
- **Wording.** "Every valence state", in the FAIL clause, was a poor choice of words: the near-edge part of the light sea is protected, as it should be.
- **Meaning.**
  - After the bulk drains, the light sea ends where the surface branch merges into an emptied bulk. That is a zero-cost filled/empty interface carrying Lemma B's compensating flux.
  - An energy-selective (zero-temperature, non-Markov) bath would protect the bulk sea. But it is itself a charged gapless metal attached to every far-wall site.

**Test F5-T3′: the energy-selective horn** (pre-registered 13:47Z; `f5_t3p_dirty_mirror_conductivity.py` → `f5_t3p_output.txt`) [checked].
- **Why T3 was replaced.** The earlier T3 was withdrawn before it ran: with a drained bulk it could not separate the Ohmic branch (see `PREREG_T1.md`).
- **Setup.** A zero-temperature, energy-selective sink (self-energy `−iΓ(k)/2`, μ = 0) keeps the seas filled. The test computes the Kubo–Bastin DC conductivity of the dissipative Wilson walker.
- **Result.** σ_xx = 5.49·10⁻², 1.98·10⁻² and 4.80·10⁻³ e²/(ħa) for p = 1, 2 and 4. These are grid-converged at N = 32, 48 and 64 to five digits. The light-node region (|k| < 0.5) contributes less than 10⁻⁴ of it; the damped doublers carry the rest.
- **Control.** The Hermitian walker with η → 0 gives σ → 0: 7.2·10⁻³, 9.0·10⁻⁵ and 9.1·10⁻⁷ for η = 0.1, 10⁻² and 10⁻³. The pre-registered linear fall-off in η could not be seen. These grids do not resolve the η-wide node regions, so the decrease looks like η²; the continuum single-node value is linear, 2π²γ.
- **Reading.** FAIL is met (σ ≥ 10⁻⁶ for every p).
- **In physical units.** σ ≈ 5·10⁻³ × 4πα × M_Pl ≈ 6·10¹⁵ GeV. The photon damping time is about 10⁻⁴⁰ s, against a bound of σ < 1/t_age ≈ 1.5·10⁻⁴² GeV, so it is excluded by about 57 orders [checked arithmetic].
- **Scope.** This is the minimum conductivity of a broadened Weyl node at μ = 0, with spectral weight that broadening cannot remove (f-sum rule). By the same mechanism F5-B's energy-selective far wall should behave alike [suggested; not computed on a slab].

**The dilemma (checked on F5-A's two horns).**
- A band-blind (Markov) sink drains or heats the seas: Lemma P, T1 and T3a.
- An energy-selective sink keeps the seas but turns the damped mirrors into a Planck-scale conductor: T3′.

**Lemma V: Ohmic vacuum (suggested in general; the energy-selective case is checked in T3′).** Wherever Lemma B puts the flux, a uniform gauge field E sees a dissipative channel:
- **On a filled/empty interface.** E pushes sea states across it, and they are absorbed. The rate per volume is ~ `Σ_i Q_i² e² E · A_S/(2π)³`, where `A_S` is the k-space area of the interface (~Λ²).
- **On a mixed region.** It carries white current noise, `Σ_k Tr[v ρ v (1−ρ)]/Γ_k > 0` by Wick.
- **No cancellation.** `Σ Q_i²` never cancels over species, so anomaly freedom does not help. The result is a vacuum conductivity or heating rate of order e²Λ (Planckian).
- The quantized anomaly inflow (∝ E·B per species, which cancels for anomaly-free gauge charges) is separate, and harmless for SM gauge charges.

---

## Route F5-C: the reduction

**Lemma B plus Lemma C.**
- Open, non-Hermitian or record-driven dynamics removes the mirror from the single-particle spectrum (A1) but not from a Gaussian vacuum.
- The only states that can carry a single Weyl sea with no mirror node, no lattice-scale filled/empty interface and no mixed region are non-Gaussian: correlated, interacting.
- That is the SMG obligation (W-a in `ASSUMPTIONS.md:38`).

**What the lens does add.**
- **A diagnostic:** compute the vacuum's Berry-flux budget. It is cheap for any SMG candidate's mean-field or Gaussian approximant: where does the ∓1 sit?
- **A far-wall tool:** absorption (T2), for the inflow family.

**Prior art engaged:**
- **"Records consume chirality"** (`CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05.md:56`). Lemma B gives a mechanism-level reason within Gaussian states. Records can damp or absorb the mirror, but the mirror's flux then sits in the state. [suggested]
- **"Handed rules register only texture or direction"** (`PRIOR_ART.md:156-159`). Lemma P shows that even a handed dissipator cannot cool a single node: positivity forces even leading order. [proved]
- **The pseudoscalar census's unrun fermion test** (`ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR…_2026-09-13.md:97`). The parity lemma answers its dissipative half: a soldered handed (DM-curl) term entering a jump symbol changes only odd subleading orders. That leaves `e_sea → 1`. [proved for quasi-free sinks; the census's own question about the 09-03/09-05 parity notes is not run here]
- **LATTICE_HANDEDNESS** listed "non-unitary record dynamics" as outside its class (branch note `:348`). This route covers that class at the quasi-free level.
- **Measurement-driven (monitored) dynamics.** Gaussian quantum trajectories stay Gaussian, so Lemma B applies trajectory by trajectory. The trajectory average is the Lindbladian treated above [proved for Gaussian trajectories]. Post-selected no-click evolution is excluded by the contract: its readout probabilities are not normalised (`WALL.md:44`).

**Liouville-space reading.** A density matrix evolves ket ⊗ bra. The bra side is driven by `h*`, whose Weyl nodes have the opposite chirality (`det` of `σ*` flips). So readouts, which are bilinear in ket and bra, see every Weyl paired with its conjugate. The doubled space M₂(C)⊗M₂(C)^op ≅ M₄(C) is where open dynamics acts. The anti-Hermitian part `−iΓ` plays the role of the fourth Clifford direction (a "mass") that M₂(C) lacks (`NO_PER_SITE_CHIRALITY…:55-65`). This connects to the parked M₄(C) decision (#4), but it does not decide it. [reading]

---

## Theorem-strength gap tests

| Route | Terminal lemma L | L ⇒ T? | T ⇒ L? | Strength | Status |
|---|---|---|---|---|---|
| F5-A | "No quasi-free analytic Markov sink whose jumps write records under the literal Record axiom keeps one undamped Weyl node, damped doublers and the filled node sea for all time" (Lemmas C, D, P) | no (it is a scoped no-go) | no | weaker (a bounded no-go for one lens) | retired. The energy-selective horn is also closed (T3′: Planck conductivity). Reopen needs unbounded record capacity, non-analytic jump symbols, and doublers that carry no current. |
| F5-B | "A 3+1D inflow slab with an absorbing far wall: far mirror damped, bulk sea intact, no Ohmic vacuum response, register never full" | it gives W-a for the spectrum, not W-b (gauge) | no | unknown/comparable (a far-wall analogue of the Golterman–Shamir problem) | wounded: the Markov horn drains the bulk (T3a, checked); the energy-selective horn is expected to conduct (T4, not run) |
| F5-C | Lemma B (Gaussian-state doubling) | no | no | it maps the lens's obligation onto SMG's | blocked-equivalent to the SMG family at the state level |

## Prices in framework terms

1. **Dynamics.** A supplied Lindblad dissipator: a decoherence mechanism or record-production dynamics, outside the axioms (`MINIMAL_AXIOMS:182-186`).
2. **Range.** Jumps of range at least 2 for the cosmic-ray bound. Non-analytic, stretched-exponential jump symbols to escape Lemmas C and P. This is beyond the overlap operator's exponential locality, so it bears on the owner's range question (A4).
3. **Record reading.** Literal "one record per site of Z³" kills F5-A (Lemma D). Reviving it needs an unbounded record register per site. Either "site" is read as an event (records along record-time), or a register coordinate is added. That is an A6-type extra coordinate. It is an owner-level reading of `MINIMAL_AXIOMS:79-80`, and is consistent with the owner's recorded thought that a sealed region fills until frozen [reading].
4. **F5-B extra coordinate.** About 80–120 layers: the near-wall leak `Γ e^{−2L/ξ} < 1/t_age` gives L/ξ ≳ 70 with ξ ~ 1. Plus 4D gauge fields shared across layers.
5. **Charge bookkeeping.**
   - Charged jumps mean the records must carry gauge charge for Gauss's law.
   - Draining a filled sea at random sites leaves a frozen random charge background of order e per Planck site.
   - That background gives a field ~ e(ℓ/a)^{3/2}/ℓ² at scale ℓ, roughly 10⁴³ V/m at 1 m [suggested; this kills any version that drains a charged sea into site records].

## Next decisive tests (one per route)

**F5-A: none left inside the lens.** Both horns have run (T1 and T3′).
- Reopen only if a sink keeps the seas filled without broadening charged doublers.
- With one lattice field the doublers carry the same charges and nonzero velocity, so broadening keeps their f-sum spectral weight at low frequency [suggested]. A reopen therefore needs doublers with no current coupling, which a single field cannot supply.

**F5-B: F5-T4** (pre-registered here 13:49Z, not run). This is the energy-selective far wall on the inflow strip.
- **Setup.** T2's QWZ strip, m = −1.5, Ly = 20. Each far-row site is attached to a zero-temperature wide-band lead: self-energy −iΓ/2 on the last row, μ = 0, Γ ∈ {0.1, 1, 10}. Compute the Kubo–Bastin DC conductivity along x with the near-edge Drude part removed. That is, add a uniform η and subtract the η-scaling part, η ∈ {10⁻², 10⁻³}.
- **PASS:** the remaining (far-wall) part is below 10⁻⁶ e²/h for some Γ.
- **FAIL:** it is at least 10⁻³ e²/h for every Γ.
- **Expected:** FAIL. A dissolved chiral channel has mean free path ℓ ≈ v/Γ and 1D conductivity ≈ (e²/h)ℓ, the 1D form of T3′ [suggested].
- **Cost:** about 20 min.
- **What a FAIL means.** In 3+1D, the far wall would be a sheet of Planck conductivity seen by the shared 4D gauge fields, and F5-B dies on the energy-selective horn too, as F5-A did.

**F5-C: no new test.**
- The escape it leaves, a non-Gaussian vacuum, belongs to the SMG family.
- A tempting variant is "dissipative SMG": drive the mirror sector into an on-site Spin(10) singlet as the unique dark state of local jumps. That dark state is a product state. The light sector would then see the atomic projection that already restored eight doublers (`SPIN10…:195-221`) [suggested].
- Only an entangled (finite-coupling) dark state could differ, and that is the open SMG question itself.

## Literature (reference only; nothing imported as proof)

| Source | What it shows | Maps to the repo? | Import risk |
|---|---|---|---|
| L1. Bessho & Sato, PRL 127, 196404 (2021), arXiv:2006.04204 | Nielsen–Ninomiya is extended by a bulk winding that exists only in Floquet or non-Hermitian systems. Predicts a non-Hermitian chiral magnetic skin effect. | Yes: A1 is its mechanism on the repo walker (checked W3 = −1). It also covers LATTICE_HANDEDNESS T4 (the Floquet side). | Low. Translated and checked here. |
| L2. Kawabata, Shiozaki & Ryu, PRL 126, 216405 (2021), arXiv:2011.11449 | Field theory of point-gap phases. The skin effect is the anomaly's signature, and 3D gives a chiral magnetic skin effect. | It names F5-A's anomaly: in a B field the single Weyl's return flow becomes boundary-skin accumulation. | Not translated here. |
| L3. Budich, Zoller & Diehl, PRA 91, 042117 (2015), arXiv:1409.6341 | Topology competes with locality in dissipative preparation of Chern states. | It is the 2D parent of Lemma C. | Abstract only. |
| L4. Goldstein, SciPost Phys. 7, 067 (2019), arXiv:1810.12050 | A finite-range Lindbladian cannot drive at a finite rate to a unique topological pure state above 1D. Exponentially local dynamics or mixed approximants can. | It parallels Lemmas C and P (finite range ⇒ mixed or slow). Lemma P is stronger at a gapless node: no analytic sink cools it. | Abstract only. |
| L5. Lessa, Cheng & Wang, arXiv:2401.17357 (2024); Wang & Li, arXiv:2403.14533 | Strong-symmetry anomalies force long-range non-separability of mixed states. Mixed strong–weak anomalies do not preclude separable states. | Charged jumps make U(1) weak, so a mixed vacuum can evade anomaly constraints, but at the cost of Gauss's law (price 5). | Abstract only. |
| L6. Hayashi, Hashimoto, Horibe & Yamamoto, hep-lat/9604005 (1996) | A non-Hermitian Minkowski-lattice action gives a single free species. The evolution is non-unitary once gauge fields are on. | It is the same trade as F5-A, at the action level. | Abstract summary via search; unverified. |

**Mathematical lenses used.**
- K-theory of GL over the Laurent ring versus unitary units: why T2 fails for non-unitary operators.
- Line-bundle Chern numbers and Stokes (Lemma B).
- The identity theorem for real-analytic symbols (Lemma C).
- Parity of PSD homogeneous forms (Lemma P).

Considered and found empty: spectral graph theory, number theory.

## Files (all in this folder)
- `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/routes/F5/ROUTE_REPORT.md` (this file)
- `PREREG_T1.md`: pre-registrations for T1, T2, T2b, T3a (with timestamps) and the readings
- `f5_t1_dissipative_walker.py` → `f5_t1_output.txt`
- `f5_t2_lossy_far_wall.py` → `f5_t2_output.txt`
- `f5_t2b_generic_mass.py` → `f5_t2b_output.txt`
- `f5_t3a_bulk_drain.py` → `f5_t3a_output.txt`
- `f5_t3p_dirty_mirror_conductivity.py` → `f5_t3p_output.txt` (peak memory 114 MB)
