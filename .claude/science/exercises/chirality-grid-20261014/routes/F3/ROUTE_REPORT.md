# Route F3: discrete-time unitary dynamics and index theory (chirality-grid exercise)

- **Route agent:** Claude Opus 5.5. This is the same model family as the supervisor and the other route agents, so it is not independent.
- **Subagents:** none. The kill pass in §6 is my own, in a separate pass. It is not a referee.
- **Time:** 2026-10-14, 13:19–13:58Z.
- **Repositories:** none edited. Everything is in this folder.

**Refresher read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, lines 1–80, which cover the generated primitive baseline: scale-reference and kinetic-isotropy.
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`, in full.
- The exercise SKILL steps 4 and 6, and `physics-loop/references/proof-search-governance.md`, both from `origin/main`.
- The packet files `WALL.md`, `ASSUMPTIONS.md` and `step0/PRIOR_ART.md`, plus the step-0 clusters, by grep.
- LATTICE_HANDEDNESS from branch `origin/claude/toe-viability-probes-20260927`, lines 1–400. I cite it below as **LH**.
- The T22 kill sheet at `4bd42747e5:.claude/science/walls/toe-walls-20260929/kills/T22.md`.

**Memory note.** One script, R1-F1, peaked at 323 MB resident set size, above the 0.25 GB guideline. It ran for under a minute. Every other script stayed at or below 180 MB, and nothing is left running.

---

## 0. Plain summary

A "tick" is a grid rule that updates the world in discrete steps instead of flowing continuously. It can look one-handed at low energy. The mirror partners then sit at "half a tick's worth" of phase, which is formally the Planck energy. I checked whether that hides the mirrors or only renames them.

It only renames them. The hidden copy:
- carries exactly the same charges;
- is gapless;
- is filled upside-down.

That leaves two cases:
- **No extra conserved energy.** The vacuum radiates photons at zero threshold, like a laser medium.
- **An extra conserved local energy exists.** Measured by that energy, the copy is an ordinary light mirror of the opposite hand. For the repo's own one-handed tick, that energy operator is literally the campaign's doubled walker, with 4 right-handed and 4 left-handed nodes.

The index theory of ticks (their topological invariants) can only "realize" anomalous charges. The Standard Model's gauge charges are anomaly-free, so ticks offer the SM nothing beyond what continuous-time Hamiltonians already do. The only way forward in this family is symmetric mass generation of the hidden copy (SMG: interactions that make the mirror copy heavy without breaking a symmetry). That is the existing K2b problem.

**What this changes for the owner:** the tails-tick exit can be closed without deciding the range question.

---

## 1. Route table

| Route | Family (object, mechanism, terminal obligation) | Premise it drops or changes | What you would have to believe | First artifact | Cost | What it would change if it worked |
|---|---|---|---|---|---|---|
| **F3-A Time-doubler duality (price theorem)** | **Object:** a free quasi-local tick U on Z³ with W3 ≠ 0. **Mechanism:** the conserved E = (i/2)(U−U†) = sin H_F, degree theory and Fock-vacuum structure. **Terminal:** "a one-handed tick keeps a gapless, identically charged, population-inverted π copy. A stable vacuum needs a conserved local E, under which the copy is a light opposite-hand mirror." | A3 and A4 (ticks with tails), granted rather than challenged | Nothing new. It is a no-go/price. | **Done:** `scripts/r1_duality_check.py`, R1-F1 and R1-F2 (checked) | Note plus runner, about 1 day | It closes the tails-tick exit independently of the range question. It also corrects the T22 kill sheet's reading that the π nodes are "at the tick cutoff". |
| **F3-B Flux index κ for interacting, non-translation-invariant QCAs** | **Object:** a U(1)-symmetric fermionic QCA (interacting, any locality with a GNVW index) coupled to link fields. **Mechanism:** the GNVW index of the z-reduced QCA along a seam path of gauge fields. **Terminal:** κ = 0 for any continuously gaugeable QCA. κ is the anomaly coefficient Σχq, so for the SM's gauged charges κ = 0 and indices buy nothing. | A5 (free), translation invariance, and the one-body assumption (all dropped) | That κ equals Σχq for interacting QCAs. This is the open IR bridge (§3). | **Done:** `scripts/r2_seam_gauging.py` (checked) | Note, about 2 days. The interacting formalization is open-ended. | It moves T2 to interacting, gauge-coupled and disordered ticks for the purpose that matters. Index theory is shown to be an anomaly-realizing tool only. |
| **F3-C Floquet mirror-SMG (the only constructive continuation)** | **Object:** a free tick with κ_F = 15 or 16 per generation; the light 16 sits at ε≈0 and the copy at ε≈π. **Mechanism:** the tick's own local mirror selector a(k) = Re U, plus body-diagonal translation T₁₁₁ forbidding light–copy masses, plus U(1)_F → Z4 quartic interactions. **Terminal:** the π copy gaps symmetrically while ε≈0 stays gapless. | A5 (interactions); the A2/T6 matter count | The SMG conjecture for a momentum- and quasi-energy-separated mirror (Eichten–Preskill type) | Pre-registered 1+1D test (§4, not run) | 1–2 days DMRG for 1+1D; weeks for 3D (K2b) | Target-equivalent to F1/K2b. If it worked, it would give a chiral Floquet Hamiltonian. |

---

## 2. Route F3-A: the tick's mirror is relabelled, not removed

### Lemma A1 [proved]

**Setting.** Two bands, free, translation-invariant, U ∈ C¹(T³, SU(2)); strict or quasi-local. Write U = a − i b·σ with nondegenerate nodes {b = 0}. Put E := (i/2)(U − U†) = b·σ.

**Claims.**
- (i) [E, U] = 0, and E has the same hopping range and tail decay as U. So E is a local conserved Hermitian one-body operator. In second quantization, dΓ(E) commutes with the free many-body tick.
- (ii) The Weyl points of E are exactly U's nodes. Write χ for the tick chirality in the LH:91-94 convention, sign det(±J), and χ_E = sign det J with J = ∂b/∂k. Then χ_E = +χ at ε=0 nodes (a = +1) and χ_E = −χ at ε=π nodes (a = −1).
- (iii) Σ_{ε=0} χ = Σ_{ε=π} χ = W3, and Σ χ_E = 0.
- (iv) If a symmetry group G (U(1)_Y, SU(2), SU(3), Spin(10)) commutes with U, then (iii) holds in each isotypic block. So the ε=π sector carries exactly the same gauge representation content as the ε=0 sector.

**Proof.**
- (i) is immediate.
- (ii): at b = 0 we have a² = 1. In three dimensions det(−J) = −det J.
- (iii): Σ_{ε=0} χ and Σ_{ε=π} χ are the degrees counted at +1 and at −1 (LH:145-150), so both equal W3. Σ χ_E = 0 is T1 (LH:100-109) applied to the smooth two-band Hamiltonian E. Together, (ii) and T1 give an independent proof of (iii)'s π-part: the two-band case of Bessho–Sato.
- (iv): Schur's lemma; U = ⊕_ρ U_ρ ⊗ 1_ρ.

∎

### The identity for the repo's own tick [proved; checked]

For U_g (LH:205-215):
- E = g(k)·Σ_j σ_j sin k_j, with g > 0. That is the campaign walker (8 nodes, 4R+4L; PRIOR_ART:61) rescaled by a positive function.
- The scalar part a(k) = cos k_x cos k_y cos k_z is the symmetrized body-diagonal hop. At corners it equals the walker chirality (−1)^{#π}.

So the one-handed tick is the doubled walker with its own mirror selector, the K2a body-diagonal object (PRIOR_ART:84), rotated into the time component. The left-handed doublers are moved to quasi-energy π, not removed.

Script output (`scripts/r1_output.txt`):
- `b - g*sin k max = 0.0`;
- a = ±1 exactly on even and odd corners;
- the body-diagonal decomposition holds to 8e-16.

### Lemma A2 [proved, two-band free]

**Inversion.** Take any stationary Slater state that fills one quasi-energy arc (the natural vacuum fills ε ∈ (−π, 0]). Particle–hole pairs at ε=0 nodes carry quasi-energy +(δ₁+δ₂). Pairs at ε=π nodes carry ≡ −(δ₁+δ₂) mod 2π. So the π copy is gapless and population-inverted relative to the dynamics. (If W3 ≠ 0, both arc boundaries are gapless by (iii). Non-arc fillings add Fermi surfaces.)

**Stabilizer.** Suppose a conserved quadratic local E′ = a′ + h·σ has this state as its Fermi sea. Then, away from nodes, h = c·b̂ with c ≥ 0, and a′(node) = E_F at every node. For c > 0 off-nodes, every node of both sets is then an E′-Weyl point at the Fermi level, with E′-chirality +χ at 0-nodes and −χ at π-nodes, summing to 0. E itself is one such E′.

**Proof sketch.** [h·σ, b·σ] = 0 forces h ∥ b. The Fermi-sea condition forces c ≥ 0 and the common level. The indices follow as in A1(ii).

### Suggestion A3 [suggested; not proved for interacting dynamics]

There are two cases.
- **(a) No local conserved E′.** Interactions conserve only quasi-energy mod 2π. Pair creation is neutral under every additive charge, so no internal symmetry forbids "vacuum → photon (+ω) + π-pair (−ω)". The vacuum then emits at first order with zero threshold. The inverted π copy is a gain medium. I did not compute the rate; I estimate it as roughly α·Λ⁴ per volume.
- **(b) A local conserved E′ exists.** By A2 the π copy is gapless at E′'s Fermi level and identically charged. Under E∥B it is also anomaly-cancelling: spectral flow carries charge from the π sector into the ε≈0 sector around the quasi-energy circle. So it is a light mirror for every slow observable (Z width, soft gauge couplings).

Either case fails the target or observation.

### Checks run (pre-registered in `PREREG.md` before running)

- **R1 [checked; recorded FAIL on a pre-registered tolerance].** Five ticks:
  - U_g;
  - its range-2 truncation;
  - normalized Wilson–Weyl maps with M = 2, −2 and 0.5.

  Every node identity passed in all five:
  - Σχ(0) = Σχ(π) = W3;
  - χ_E = ±χ;
  - Σχ_E = 0;
  - |a| = 1 at the nodes.

  The verdict is FAIL only because the N=40 finite-difference W3 missed its integer by more than 0.05 (3.937, 3.943, 1.944). That verdict stands as recorded.
- **R1-F1 [checked, PASS].** This is a dated follow-up added after R1's result. Richardson extrapolation from N = 32, 48, 64 gives W3 = 3.9996, 3.9997, −0.9998, −0.9998 and 1.9989. All match Σχ(0).
- **Notable example [checked]:** the M = −2 map has exactly one Weyl node at ε=0 (k = (π,π,π), χ = −1), a literal single light Weyl fermion. It has 7 nodes at ε=π, with net −1. Its E is the 4R+4L walker.
- **R1-F2 [checked, PASS].** This tests for a selection rule on the q→0 photon vertex of U_g. The interband element Σ_j |⟨u₊|∂_jU|u₋⟩|² → 2.000 at both the ε=0 node and the ε=π node (shells r = 1e-2, 1e-3, 1e-4). Analytically it is 2i sin ε·⟨u₊|∂u₋⟩, which is finite. So no selection rule protects the inverted sector at linear order.

### What it corrects in the record [reading, backed by A1–A2 and R1-F2]

- T22 kill error 1 (`kills/T22.md:19`) discounts the π-sector nodes as "at the tick cutoff". That is not the physically relevant statement. Their pair excitations are gapless (quasi-energy ≡ −small) and couple to soft photons with the same strength as the light sector.
- LH:251-260 lists "time doubler, heating" as costs. The sharper statement is: identical charges, inverted, lasing vacuum or light mirror.

### Theorem-strength gap test

- **L_A:** "a free tick that is one-handed at ε≈0 has a gapless, identically charged, inverted π copy (proved). A stable Fock vacuum under a conserved local quadratic E′ makes it an E′-light opposite-hand partner (proved, two bands)."
- L_A does not imply T and T does not imply L_A. It is a scoped no-go/price: **weaker** than a full no-go, and not target-equivalent.
- The positive continuation of this family is F3-C, which is **target-equivalent** to F1. Status: `blocked-equivalent` for the positive direction; the no-go part is `provisional`.
- **Reopen condition:** an interacting tick whose vacuum is stable without any local conserved E′. That would contradict generic Floquet heating and would need a new mechanism.

### Price in framework terms

Admissibility supplies no dynamics (AX:114-123). A one-handed tick needs two supplied things:
1. an update law with tails (the range question; PRIOR_ART:232; T2 per LH:118-125);
2. a supplied extra conserved local energy, or else the vacuum is unstable.

Paying (2) brings back the light mirror. So the real price is the mirror itself: 15 identically charged Weyl fermions at the copy per generation, or 16 if ν_R stays Weyl rather than taking a Majorana mass. Gapping them is SMG plus the matter count (A2/A5).

**The range question does not need to be decided for this exit** [reading].

### Cheapest decisive test

Already run: R1, R1-F1 and R1-F2.

Next test for A3(a), not run:
- **Computation:** the first-order Floquet golden-rule photon emission rate per volume from the U_g ⊕ U_g Fock vacuum, with charges ±1 so the anomaly cancels, and a weakly Peierls-coupled lattice photon.
- **PASS (price stands):** Γ/V > 0 with no threshold.
- **FAIL:** Γ/V = 0 by a selection rule beyond R1-F2.
- **Cost:** about 3 hours.

---

## 3. Route F3-B: the only index a tick can add is an anomaly

### Lemma B1 [free case proved; interacting case is a skeleton with named open steps]

**Setting.** α_A is a family of fermionic QCAs on Z³ with:
- uniformly bounded range, or quasi-local with Lieb–Robinson-type tails so that the GNVW index exists;
- dependence on U(1) link variables that is gauge-covariant, local and norm-continuous.

Place it on T²_L × Z. Use the Landau seam path A_t = (A_y = t·(2π/L)·x), t ∈ [0,1]. It joins zero flux (t=0) to a uniform field of N_φ = L quanta (t=1) through continuous link configurations. The seam plaquettes carry large flux at intermediate t.

**Claim.** The z-reduced QCA, which is 1D with a finite cross-section, has a GNVW index that is constant in t. Define κ(α) := [log₂ ind(N_φ) − log₂ ind(0)]/N_φ. Then κ = 0.

**Free case.** log₂ ind is the det-winding in k_z, and the det of a continuous unitary family has constant winding. ∎

**Interacting case: open steps.**
- (B1-a) A definition of continuous local gauging for QCAs that are not symmetric circuits times shifts.
- (B1-b) Homotopy invariance of the fermionic GNVW index for norm-continuous families (cited: GNVW; Ranard–Walter–Witteveen; Fidkowski–Po–Potter–Vishwanath — from memory, not re-verified here).
- (B1-c) **The IR bridge:** for an interacting QCA whose ε≈0 sector is described by Weyl fermions (χ_i, q_i), the N_φ-linear part of log₂ ind is N_φΣχ_iq_i. It holds for free ticks (lowest Landau levels). For interacting ticks it needs an anomaly non-renormalization statement for QCAs. Giuliani–Mastropietro–Porta prove the Hamiltonian analogue; there is none for QCAs.

### Corollary B2 [proved, arithmetic + A1(iv)]

- On the SM 16, every gauged U(1) has Σχq = 0 (Y; B−L with ν_R). The same holds for B and L separately (Σχ B = 2−2 = 0; Σχ L = 2−1−1 = 0).
- So **no gauged charge needs or can carry a QCA index.** κ gives the SM nothing.
- The only nonzero index of a free one-handed SM tick is that of ungauged fermion number: κ_F = 16 per generation, or 15 if ν^c takes a Majorana mass. ν^cν^c is the only SM-invariant ψψ bilinear on the 16, and 16⊗16 has no Spin(10) singlet. So free symmetric dynamics conserve U(1)_F on the charged 15 automatically.
- Hence free one-handedness ⇔ κ_F ≠ 0 ⇔ the A1/A2 time copy.
- Removing the copy needs interactions that break U(1)_F to Z4, where the anomaly is 16 ≡ 0 mod 16. That is SMG, which says exactly why "every exit needs the full anomaly-free 16" (T22, `WALLS.md:41`).

### Suggestion B3 [suggested; cited theorem, one open step]: non-translation-invariant free ticks

- Strictly local means finite propagation, with no translation invariance: disorder, defects, quasi-periodic coins. Such free invertibles on Z³ are automorphisms in the Pedersen–Weibel bounded category over Z³.
- Its K₁ ≅ K₋₂(C) = 0 (nonconnective delooping; regular ring). The setup is confirmed by search; the exact index formula is from memory, to be checked against Pedersen–Weibel 1985 or Carlsson–Goldfarb.
- **Open step:** the coarse corner-cocycle W3 pairing, Tr(a₀[χ₁,a₁][χ₂,a₂][χ₃,a₃]), is a homomorphism on that K₁.
- If both hold, T2 extends to all strictly local free ticks, and **tails are exactly the failure of Bott periodicity in algebraic K-theory**: K₋₂^top(C) = Z carries W3, while algebraic K₋₂(C) = 0. [reading]

### Open obligation O-κ [open]

Does any **strictly local, interacting**, U(1)-symmetric fermionic QCA on Z³ have κ ≠ 0?
- Free: no (T2; B3).
- Nontrivial interacting 3D QCAs exist (Haah–Fidkowski–Hastings; Haah's Clifford QCAs; cited in archive `THREE_DIMENSIONAL_ANOMALOUS_BULK_CATEGORY_INDEX_STEELMAN_NOTE_2026-07-14.md:171-174`). Their classes are Witt/gravitational-type, not U(1)-flux-type [reading].
- By B2, O-κ is irrelevant for SM gauge chirality. It matters only for realizing an anomalous U(1).

### Check R2 [checked, PASS on every pre-registered criterion]

**Control.** The ordered strictly local tick S_xS_yS_z, gauged factor by factor:
- unitary to 2e-16 for every t;
- winding 0 for every t.

**Test.** The T4 range-2 tick, Peierls-substituted and then unitarized:
- winding 0 at t=0;
- **32 at L=8 and 48 at L=12, i.e. 4N_φ** at t=1. This reproduces the T22 "48" (`kills/T22.md:13`).
- Every jump (8 at L=8, 9 at L=12, located by bisection) occurs where σ_min(Q) ≤ 3.1e-7.
- On this path, every located singularity has a seam plaquette angle |F_p| ≥ 1.81 rad (> π/2), while bulk plaquettes stay ≤ 0.64 rad. No crossing occurs at any t where all plaquettes are ≤ 1.6 rad.

**Reading.** An anomalous U(1) can be coupled to the chiral tick only on a restricted, "admissible" set of gauge fields with disconnected flux sectors. That is Lüscher's mechanism (cross-link to F2), not a continuous gauging.

### Theorem-strength gap test

- **L_B:** "continuously gaugeable ⇒ κ = 0". It is a necessary condition; **weaker** than T and not equivalent.
- With B2 it is vacuous for SM gauge charges, so it can neither close nor block T on its own.
- Status: `provisional` (free case proved); interacting `active` with open steps B1-a/b/c.
- **Reopen for positive use:** only if nature needs an anomalous symmetry realized without light matter. An example would be a Z4-protected SM without ν_R, whose Z16 anomaly is ν = 15. Even then F3-A's vacuum price applies [suggested].

### Price

For the SM nothing is bought, so nothing is paid. For an anomalous U(1), the price is an admissibility restriction on link fields plus F3-A's vacuum price.

### Next cheapest test (not run)

- **Computation:** the same seam path for U_g ⊕ U_g with charges ±1 (anomaly-free).
- **PASS:** some gauge-covariant unitary coupling that mixes the two species stays regular across the seam, so the summed winding stays 0. This is the Floquet analogue of Lüscher's existence theorem.
- **FAIL:** every natural mixing is singular.
- **Cost:** about 2 hours.
- **Value:** low for the wall, because F3-A applies anyway.

---

## 4. Route F3-C: the constructive continuation, Floquet mirror-SMG

### Dictionary [proved for the identities; reading for the equivalence]

| Floquet object | Hamiltonian / K2a counterpart |
|---|---|
| The light 16 at ε≈0 (even corners) | The light 16 |
| The copy at ε≈π (odd corners) | Mirror 16 |
| Selector a(k) = Re U = cos k_x cos k_y cos k_z | K2a body-diagonal selector |
| Body-diagonal translation T₁₁₁, eigenvalue ±1 at even/odd corners | Forbids every light–copy bilinear mass in any translation-invariant theory, exactly as in the Hamiltonian |
| RWA "π-parity" | Adds nothing beyond T₁₁₁ |
| Conserved E | Puts the problem in Hamiltonian form |

So the terminal obligation, "a symmetric quartic gaps the copy while ε≈0 stays gapless, U(1)_F → Z4", **is** F1/K2b (`KILL_SHEET.md:83`). Status: `blocked-equivalent`. The tick offers no extra protection [reading, from the dictionary].

### What would have to be true

Mirror SMG with the mirror separated in momentum (and quasi-energy) rather than in space. That is the Eichten–Preskill setting:
- prior lattice evidence in 1+1D is negative (Golterman–Petcher–Rivas 1993 — from memory, unverified);
- Golterman–Shamir raise 3+1D concerns (PRIOR_ART:83; `kills/T22.md:12`).

### Cheapest decisive test (pre-registered here, not run)

**Model.** 1+1D, strictly local, where the chiral tick is just a shift. Take eight left-moving Majorana shifts. Their time-copies at k≈π form the E-mirror. The corresponding E-Hamiltonian is the naive sin k lattice with a matching interaction V.
- V is an SO(7)-symmetric quartic (the TW-3 content, `TESTS.md:9647-9658`) weighted by the local selector (1 − cos k)/2 on each leg.
- Run DMRG on H = E + V for L ≤ 64 and scan g.

**Readings.**
- **PASS:** for some g, the k≈π sector has a finite-size-extrapolated gap Δ_π > 0, while the k≈0 sector stays gapless (c_L = 4: Δ₀ ∝ 1/L and entanglement slope consistent with c = 4), with no symmetry-breaking order parameter.
- **FAIL:** for every g in [0, g_max], both sectors gap or neither does (the Golterman–Shamir pattern).

**Cost:** 1–2 days. **Risk:** high; the 1+1D literature is negative for this geometry.

### Price

Interactions (A5), plus the matter count (16–32 bits per vertex; PRIOR_ART T6), plus tails if built from U_g. The K2a continuous-time staggered version avoids tails.

---

## 5. Registry row for F3 (proposed update)

- **Family:** F3 discrete-time / QCA / index.
- **Object:** free and interacting QCAs on Z³.
- **Mechanism:** W3, the flux index κ, and E = sin H_F duality.
- **Terminal obligation:** single-Weyl QCA without a light or inverted copy; or SMG of the copy.
- **Strength vs target:** the A/B no-go parts are weaker scoped no-gos; the positive continuation (C) is target-equivalent to F1.
- **Status:** **blocked-equivalent** (positive); A/B `provisional`.
- **Evidence:** R1, R1-F1, R1-F2 and R2 (this folder).
- **Reopen condition:** a stable interacting Floquet vacuum without a local conserved energy, or O-κ positive and an anomalous symmetry demanded by observation.

---

## 6. Kill pass (same family, my own separate pass; not independent)

- **"E is conserved only in the free theory."** True. That is why A3 is a dichotomy. The exhaustiveness of "stable vacuum ⇒ some local conserved E′" is suggested, not proved.
- **"The π copy could sit at momenta photons can't reach."** No. q→0 photons create pairs at the same node, and R1-F2 shows the vertex is equal at both nodes.
- **"Pick another vacuum."** Arc fillings are always inverted at one gapless boundary. Non-arc fillings add Fermi surfaces. Interacting vacua are not covered. Wounded only there.
- **"A1 is just Bessho–Sato / T2 step 5."** Part (iii) is. New are:
  - the E = sin H_F identification;
  - the exact identity with the walker and the selector;
  - the inversion;
  - the representation content;
  - the correction to T22's error-1 reading.
- **"B1 free case is trivial."** Yes. Its content is the seam-path setup, the anomaly identification, and the checked location of the singularities.
- **"Does it assume the target?"** No.
- **"Does it contradict a landed or recorded result?"** It refines the reading of LH:251-260 and contradicts the T22 kill's reading at `:19`. The T22 kill's numbers are reproduced.

---

## 7. Literature (outside view; reference only, never imported as proof)

| Source | What it shows | Use here | Verified this session? |
|---|---|---|---|
| Bessho & Sato, PRL 127, 196404 (2021), [arXiv:2006.04204](https://arxiv.org/abs/2006.04204v2) | Floquet/non-Hermitian Nielsen–Ninomiya: bulk topology permits chiral bulk nodes | A1(iii) reproves the two-band case | Abstract only |
| Bakircioglu, Arnault & Arrighi, [arXiv:2505.07900](https://arxiv.org/abs/2505.07900) | Doubling occurs in QCAs, including time shifts (E ± π/ε); a "flavouring" fix keeps the doublers as flavours | Consistent with F3-A: renaming, not removal | Partial HTML |
| Topa, [arXiv:2609.14749](https://arxiv.org/abs/2609.14749) (preprint) | 3D probabilistic-CA Weyl excitation; "no protected 2-component node survives" | Not net-chiral; not engaged further | Abstract only |
| Pedersen–Weibel (1985); Carlsson–Goldfarb, [bounded K-theory](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/carlgold.pdf) | Bounded categories over Rⁿ deloop K-theory | B3 | Setup only; the index formula is from memory |
| GNVW (CMP 2012); Ranard–Walter–Witteveen (2022); Fidkowski–Po–Potter–Vishwanath (PRB 2019); Lüscher (NPB 549, 1999); Golterman–Petcher–Rivas (1993) | Index, its homotopy invariance, the fermionic version, admissible chiral U(1), Eichten–Preskill failure in 2D | B1-b, R2 reading, F3-C risk | From memory, unverified |

Literature search: [Bessho–Sato](https://arxiv.org/pdf/2006.04204), [APS](https://link.aps.org/accepted/10.1103/PhysRevLett.127.196404), [2505.07900 HTML](https://arxiv.org/html/2505.07900v2), [Pedersen–Weibel context, 1101.0573](https://arxiv.org/pdf/1101.0573).

## 8. Files (all in this folder)

- `PREREG.md`: R1, R2, the R1-F1 follow-up and R1-F2, each written before its run.
- `scripts/r1_duality_check.py`, output in `scripts/r1_output.txt`: R1. **FAIL** recorded, on W3 tolerance only.
- `scripts/r1f1_w3_richardson.py`, output in `scripts/r1f1_output.txt`: R1-F1. **PASS**.
- `scripts/r1f2_vertex.py`, output in `scripts/r1f2_output.txt`: R1-F2. **PASS**.
- `scripts/r2_seam_gauging.py`, output in `scripts/r2_output.txt`: R2. **PASS**.
