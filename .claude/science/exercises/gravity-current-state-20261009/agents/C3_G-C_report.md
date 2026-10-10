# C3 lane G-C: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. **Codex sol referee: INCONCLUSIVE. The narrow no-go is confirmed only for frozen picture-I, fixed-point, point-marked order functionals with uniform per-realization invariance and an EH ensemble mean. It does not cover independent link fields, picture II, other couplings or a background-free quantum sum. The law-level Ward identity is exact but does not establish the physical quantum-sum branch** (C3_G-C_referee.md).

**Verdict (worker):** FAIL (no-go proved under stated hypotheses H1-H5) for per-realization protection. Quantum-sum branch: the exact Ward identity holds for the law and for every covariant sum over orders (proved), but it is INCONCLUSIVE as protection of the realized physics, because its premises are not established: an unrecorded micro-order, a 4D manifold-like phase, and locality of the sum-level effective action. Per PREREG the two halves are not merged into a PASS. Needs the codex sol referee.

**Plain summary:** We asked whether a spacetime made of scattered events, whose only structure is which event can influence which, can stop the graviton from getting a mass in every single realization, the way Einstein's symmetry does in the continuum. We proved that it cannot, for any such rule that also yields Einstein's equations on average. In one frozen set of events, a shape-changing stretch always changes the action by random jumps. The only rules immune to those stretches cannot sense the size of things at all, and they give a different theory of gravity with no Newtonian 1/r pull. The protection does hold exactly for averages over all possible event sets, or for a quantum superposition of them. So it protects our world only if the fine pattern of events is never fixed as a record, which conflicts with reading records as events. Also, unlike the fluctuations behind the "everpresent cosmological constant", these random jumps did not shrink relative to size over larger regions in our tests, and a counting argument says why.

# Lane G-C (protection): report

**Worker:** Claude Opus 5.5 at max effort. Same model family as the supervisor; nothing here is refereed.
**Time:** 00:49Z to about 02:05Z, 2026-10-10. **Repository:** not edited.
**Scratch:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-C/`
**Pre-registration:** PREREG.md, stamped `Sat Oct 10 01:04:56 UTC 2026`, before any computation. N1 and N2 were pre-registered. Added afterwards, and none of them carries the verdict:
- N3 (zero-mode size scaling);
- N4 (Lemma B transition graph);
- the WTDiff row of N2.

**Labels:**
- **EXACT:** proved here.
- **CHECKED:** computed here.
- **ARGUED:** an argument, not a proof.
- **COMPARATOR:** literature. (M) means quoted from memory; no paper was downloaded.

---

## 1. Verdict against the fixed reading

| Half of the G-C question | Verdict | Basis |
|---|---|---|
| Does any order-only or link-only dynamics carry an exact **per-realization** identity (diffeomorphism-type, coboundary or conservation) that forbids a TT mass in each realization? | **FAIL: a no-go proved under hypotheses H1–H5 (§3).** It goes to the referee. | Lemma B and Theorem C (EXACT), with the algebra checked in N2 and the combinatorial core in N4 |
| Does a **quantum sum over orders** supply the protection? | **The identity is EXACT at the level of the law and of every covariant sum (Theorem A). As protection of the realized world it is INCONCLUSIVE.** | It applies to the realized physics only if the micro-order stays unrecorded (coherent). The records-as-events test setting denies that. The 4D premises (a manifold-like phase; locality and analyticity of the sum-level effective action) are open |

Per PREREG I did not merge the two halves into a PASS. needs_referee = true.

**Consequence for the campaign (reading).** The referee-corrected B1 statement was that the per-realization gauge identity is "a naturalness requirement, not a theorem". In the order-only class it is stronger than that: with an Einstein–Hilbert mean, the identity is **unattainable**. So for a recorded event substrate the only protection is in law. The whole burden falls on per-realization noise being quantitatively harmless:
- G-A: action-level crackle against the mean quadratic action;
- G-B and E1′: propagation noise.

B1's line "for the graviton, N requires G per realization" must be weakened accordingly for this class.

---

## 2. Plain summary

- **The question.** We asked whether a spacetime made of scattered events, whose only structure is which event can influence which, can stop the graviton from getting a mass in every single realization, the way Einstein's symmetry does in the continuum.
- **The no-go.** It cannot, for any such rule that also gives Einstein's equations on average.
  - In one frozen set of events, a shape-changing stretch always changes the action by random jumps.
  - The only rules immune to those stretches cannot sense the size of things at all. They give a different theory of gravity, with no Newtonian 1/r pull.
- **Where protection does hold.** It holds exactly for averages over all possible event sets, and for a quantum superposition of them. So it protects our world only if the fine pattern of events is never fixed as a record. That conflicts with reading records as events.
- **No averaging out.** The "everpresent cosmological constant" comes from fluctuations that shrink, relative to size, over larger regions. These random jumps did not shrink that way in our tests, and a counting argument says why.

---

## 3. Setting, definitions and hypotheses

This is a test setting only. The E1/E1′ axiom conflicts apply:
- Lattice is replaced by an event set.
- The causal order is supplied (A36: records carry no time).
- Records-as-events conflicts with "one record per site; permanent".

Supplied, not derived: the Poisson law, the action functionals, and the background metric fields. The realized-state primitive is why per-realization statements matter in the records reading: "a value that would change under a different law-admissible realized state is registered data".

**The two pictures.**
- **Picture I (embedded, frozen labels).**
  - A finite point set P in an open connected region U of M^{1,3} (or M^{1,1}), with a metric g, has order ord(P, g).
  - An **order-only functional** S is any function of the isomorphism class of the finite order. Optionally the points carry marks, for example a source.
  - This class includes link-only functionals, interval-count actions (Benincasa–Dowker, "BD"), link propagators with marked sources, and log-determinants of order-built operators.
  - The **per-realization response** is F_P(g) := S(ord(P, g)).
- **Picture II (intrinsic).** Only the isomorphism class is physical. The law μ_g is the law of the isomorphism class of ord(P, g) when P ~ Poisson(ρ·dvol_g) on a region D.

**The TT zero mode.**
- It is the constant volume-preserving strain g_s = B_sᵀηB_s, with B_s = diag(1, 1, e^s, e^{−s}) acting on (t, x¹, x², x³). This is the plus polarization for waves along x¹.
- A constant strain is pure gauge (ξ = (B_s − 1)x).
- The TT "mass" is the k → 0 limit of the TT response, i.e. the response to this mode.

**Hypotheses.**
- **H1. Substrate.** A finite configuration of n points in an open connected U. "a.e." refers to Lebesgue measure on Uⁿ, equivalently Poisson conditioned on n.
- **H2. Functional.** S is order-only (marks allowed).
- **H3. The identity sought: uniform per-realization zero-mode invariance.** There is an s₀ > 0 such that, for a.e. P in Uⁿ and all |s| < s₀ with B_sP ⊂ U, S(ord(B_sP)) = S(ord(P)).
- **H4. For the mean.**
  - Proper-volume Poisson sprinkling of a region D, with h supported inside D.
  - Γ_S[g] := E S is twice differentiable.
  - Its quadratic kernel at small k is Lorentz-covariant and polynomial in k (bulk locality, i.e. an EFT).
  - η is stationary: no tadpole.
- **H5. Einstein–Hilbert.** Γ_S has a nonzero two-derivative (EH) part. For the BD action this is the Benincasa–Dowker result (COMPARATOR, M: arXiv:1001.2725; E[S_BD] → ∫R√−g plus boundary terms).

---

## 4. Results

### R0. The Stückelberg identity (EXACT; CHECKED in N1(a))

F_P(φ*g) = S(ord(φP, g)) for every diffeomorphism φ, because x ≺_{φ*g} y if and only if φ(x) ≺_g φ(y).
- **What this means.** The points act as Stückelberg fields. A pure-gauge change of the metric at fixed points equals a motion of the points at fixed metric.
- **Check (N1(a)).** Co-moved points A⁻¹P under the metric AᵀηA reproduce the original order exactly, for d = 2 and 4 and s = 1e-3, 0.1 and 0.5.

### R1. The crackle structure: the per-realization Hessian (EXACT + CHECKED)

- **Piecewise constant (EXACT).** For finite P and any smooth metric family g_ε, F_P is piecewise constant in ε, with finitely many jumps; each jump is one pair crossing nullness. For a.e. P, ε = 0 is not a jump. So every ε-derivative of F_P at 0 vanishes.
  - Hence **the per-realization Hessian exists and is zero in every direction, gauge and physical alike.** It carries no information.
  - Hence a non-uniform ("infinitesimal") per-realization Ward identity, with s₀ allowed to depend on P, holds for **every** S and is vacuous.
- **Expected number of flipped relations**, at leading order in s, for Poisson density ρ in a causal diamond of height T: E F(s) = c_d·ρ²·s·T^{2d}.
  - **d = 2,** for the shear (t, x) → (t, x + st): **c₂ = 1/24, EXACT** (Appendix). CHECKED: ⟨F⟩/(sT⁴) = 0.039–0.043 at T = 40 and 60, for s from 1e-6 to 1e-3.
  - **d = 4,** for the TT strain: **c₄ = (7.258 ± 0.009)×10⁻⁴.** This is a numerical integral of the exact leading-order null-shell formula, by Monte Carlo over 4e6 points. CHECKED: ⟨F⟩/(sT⁸) = 6.2e-4 to 7.75e-4 at T = 6, 8 and 10, for s = 1e-4 and 1e-3.
  - **The smallest flipping strain s_min(P)** satisfies ⟨s_min⟩·c_d·T^{2d} ≈ 0.9–1.7, with sd/mean ≈ 1, as Poisson flips predict.
- **Physical translation** (the exact leading-order formula evaluated; no fit). At Planck density:

  | Diamond height | Flipped relations at h = 1e-21 | s_min |
  |---|---|---|
  | One LIGO wavelength, 3e6 m | ~10^306 | ~10^−327 |
  | 1 Gpc | ~10^458 | — |

  **Physical amplitudes sit about 300 decades inside the crackle regime.** No per-realization Hessian exists there.

### R2. Lemma B: per-realization zero-mode invariance holds if and only if S is flat-blind (EXACT)

**Statement.** Assume H1 and H2. Then H3 holds if and only if S takes a single value c_n on the orders of all generic n-point configurations in U. For marked S, the value depends only on the multiset of marks. I call such an S **flat-blind**.

**Proof.**
1. **The walls.** Let W_ij = {τ²(x_i − x_j) = 0} be the null walls. The order type is locally constant off the walls. Let Z be the union of:
   - the pairwise intersections W_ij ∩ W_kl;
   - the sets W_ij ∩ {(Δx²)² = (Δx³)²};
   - the collisions.

   Z has codimension ≥ 2 in Uⁿ.
2. **The path.** Join any generic P to a generic antichain configuration A (points spread on a spacelike hyperplane inside U). Use a smooth path in Uⁿ \ Z, transverse to the walls; such a path exists by standard transversality, since a codimension-2 set does not disconnect.
3. **Single crossings.** Along the path, the order changes only at finitely many crossings of single walls W_ij. At each crossing point P*, ∂_sτ²_ij = −2((Δx²)² − (Δx³)²) ≠ 0.
4. **Each crossing is a small strain.** Take P₋ on the "before" side, within distance δ of P*. Then a strain |s*| ≤ Cδ carries P₋ across W_ij. For δ small, no other pair changes its relation for |s| ≤ |s*| + δ. Choose Cδ < s₀. The admissible P₋ form a nonempty open set, so H3 holds for some P₋ in it.
5. **Conclusion.** So S is equal on the two sides of every crossing, and S(ord(P)) = S(ord(A)) = S(antichain_n). ∎

Marks ride along with their points, so the marked version follows in the same way.

**Note.** B_s leaves Δt unchanged, so a flip only toggles "related" against "unrelated".

**Check (N4; CHECKED; added after PREREG).** Random 4D configurations with random box aspect ratios, and small TT strains with |s| < 0.05:

| n | Order types realized | All n-posets | Strain-transition components |
|---|---|---|---|
| 3 | 5 | 5 | one |
| 4 | 16 | 16 | one |
| 5 | 63 | 63 | one |

Each single component includes the antichain. So any S invariant under these small strains is constant on all posets with n ≤ 5. For n ≤ 5 every poset is realizable, so flat-blind is trivial there. For large n, flat-blind functionals can still distinguish orders that do not embed in Minkowski space.

**Corollary B′ (EXACT).** Exact per-realization zero-mode invariance does not care how it would be implemented: a symmetry, an exact coboundary in a fixed region, or a conservation law. Any mechanism that achieves it forces flat-blindness.

### R3. Theorem C: flat-blind implies conformally blind, which implies no TT mass and no EH term (EXACT under H4; algebra CHECKED in N2)

**Statement.** If S is flat-blind (for every n), then under H4 the mean quadratic kernel at k ≠ 0 is K_k = a(k²)·P^(2). With locality, a = k⁴·g(k²): the leading term is linearized Weyl², with no mass and no EH term. The same holds for **every cumulant** of S, and therefore for the sum-level Γ = −i log E e^{iS}.

**Proof.**
1. **Diff.** Γ_S[φ*g] = Γ_S[g] for diffeomorphisms of D that are the identity near ∂D (Theorem A). At a stationary η this gives K(L_ξη, ·) = 0.
2. **Conformally flat metrics.** Take g = Ω²φ*η with Ω − 1 and φ − id supported inside D.
   - Causal relations are conformally invariant, so ord(P, g) = ord(φP, η).
   - φP ⊂ D is a flat configuration with an absolutely continuous law, so it is generic almost surely.
   - So S = c_{|P|}, and Γ_S[g] = G(ρ·Vol_g(D)), a function of the total volume alone.
3. **Weyl directions.** Take g = (1 + 2ω)η. Then Vol = V₀ + 4∫ω + 4∫ω².
   - Stationarity forces G′ = 0.
   - The second variation is then 16ρ²G″(∫ω)², which is a pure k = 0 term.
   - So at k ≠ 0, K_k(η, η) = 0.
4. **Barnes–Rivers.** A Lorentz-covariant kernel that annihilates the gauge directions is aP² + cP^{0s}. Since K_k(η, η) = 3c, we get c = 0.
5. **Locality.** k²P² is not polynomial; k⁴P² is.
   - N2 CHECKED: least-squares residual 0.68–5.8 for k²P², against 3e-15 for k⁴P².
   - N2 CHECKED: the polynomial kernels that annihilate both gauge and Weyl directions number **0 at degree 0, 0 at degree 2, and 1 at degree 4** (k⁴P²). ∎

A function of the count N can be added to S; c_n is arbitrary. It contributes only the volume (Λ-type) dependence G.

**Without locality (EXACT algebra; ARGUED physics; COMPARATOR data).** K = a(k²)P² still holds. A k² behaviour (a = k²) gives the pure spin-2 exchange T·T′ − ⅓TT′ instead of GR's T·T′ − ½TT′. That is the vDVZ structure: light bending is 3/4 of GR, i.e. γ = ½. Cassini gives γ − 1 = (2.1 ± 2.3)e-5, so this is excluded, assuming the trace sector is otherwise inert. A non-analytic a(0) ≠ 0 (a transverse "mass") is not excluded without locality.

### R4. The no-go (EXACT under H1, H2, H4 and H5)

**Statement.** H3 is incompatible with H5. Any order-only or link-only functional whose mean carries an EH term violates per-realization zero-mode invariance. This includes the BD action, by COMPARATOR (M).

**How the violation shows.** On a positive-probability set of configurations, a small TT strain changes S. Per realization, the zero-mode response is:
- piecewise constant (R1);
- non-analytic, with sd ∝ s^{1/2} (E1; N1(c));
- superextensive in the tested range (R7).

**Illustration (CHECKED, N1(c)).** E1 convention, with a fixed η-diamond, so the law is exactly independent of s.
- The means of ΔR, ΔL and ΔS_BD are consistent with 0 (within about 2σ).
- For the 4D BD action, sd(ΔS)/√s ≈ 3.2e3–5.9e3 for s from 1e-5 to 1e-1, flat to within about a factor 2.
- The fraction of realizations left unchanged falls from 0.62 at s = 1e-5 to 0 for s ≥ 1e-3.

### R5. The intrinsic picture; per-realization response depends on the coupling (EXACT)

**No Ward content per realization.**
- Diffeomorphisms act trivially on isomorphism classes.
- The configuration space, the isomorphism classes of finite orders, is discrete. It has no gauge orbits and no gauge directions.
- The only symmetries of a realization are Aut(C), a finite group.

So the intrinsic per-realization identity (label invariance, Rideout–Sorkin's "discrete general covariance" acting on one history) is exact but has no Ward content.

**A per-realization TT response needs a coupling between μ_η and μ_g.** For the zero mode there are two couplings that preserve the law:

| Coupling | Per-realization response | Evidence |
|---|---|---|
| Fixed points | crackle | N1(c) |
| Co-moving points, P ↦ B_s⁻¹P | ΔS ≡ 0 for **every** S | N1(a) |

So a "per-realization TT mass" is **not an intrinsic observable**. A k ≠ 0 TT wave has no isometry, so it has no canonical co-moving coupling (ARGUED).

**What is operational.** The physically meaningful per-realization quantity is field propagation on the realized order (E1′, G-B). For the source-driven link scalar, E1′-b (refereed) bounds the deviation from the massless mean by √(3/N̄). That bounds any per-realization effective "mass" of that proxy far below observation. It is a concentration bound, not an identity. It says nothing about masses induced radiatively by coupling to the matter vacuum on the order; that coupling brings back R4's action-level situation.

### R6. Theorem A: the identity at the level of the law and the sum (EXACT)

**Statement.**
- Let φ be a diffeomorphism of D (the identity near ∂D). If P ~ Poisson(ρ·dvol_{φ*g}), then φP ~ Poisson(ρ·dvol_g), by the mapping theorem, since φ is an isometry (D, φ*g) → (D, g). Also ord(P, φ*g) ≅ ord(φP, g), with marks transported.
- Hence μ_{φ*g} = μ_g, and **every functional of the law is exactly Diff-invariant.** That covers:
  - the mean;
  - all cumulants;
  - E e^{iλS};
  - Σ_C μ_g(C)·e^{iS(C)} for any order-only S;
  - constrained sums Σ_{C∈𝒞(g)} w(C), for any set of orders 𝒞(g) defined from the isometry class of (D, g), for example "orders faithfully embeddable at density ρ".

**Picture I.** With coordinate-Lebesgue sprinkling, the law is invariant under SDiff (volume-preserving diffeomorphisms). Every per-realization functional is **exactly Weyl-invariant**, F_P(Ω²g) = F_P(g), because causal relations are conformally invariant. So every law functional is **WTDiff-invariant** (Weyl plus transverse diffeomorphisms).

**Kernel counts (N2, CHECKED): Lorentz-covariant polynomial kernels annihilating the stated directions.**

| Invariance | Degree 0 (mass) | Degree 2 | Degree 4 |
|---|---|---|---|
| Diff | **0** | 1 (linearized EH) | 2 |
| Diff + Weyl | 0 | **0** | 1 (k⁴P², Weyl²) |
| TDiff (k·ξ = 0) | **1, (tr h)² only** | 3 | 4 |
| WTDiff (picture I) | **0** | **1** (the linearized WTDiff / unimodular kinetic term; COMPARATOR, M: Álvarez–Blas–Garriga–Verdaguer hep-th/0606019) | 2 |

**Consequence.** At a stationary background with a local kernel:
- every law-level or sum-level effective action has **no TT mass**;
- picture II allows the EH term;
- picture I allows the unique WTDiff two-derivative term.

**Scope.** This is protection **in law, or in the sum**. It extends E1(a) (constant strains only) and B1 §2.11 (the point process alone) to every gauge direction and every sum-level functional. It is not per-realization protection, which agrees with B referee item 15.

### R7. The zero-mode crackle does not average out; the TT analogue of everpresent Λ

**Sum level (EXACT + COMPARATOR).**
- The only local Diff-invariant non-derivative term is Λ√−g; under TDiff, f(det g) is also allowed.
- A fluctuating Λ (everpresent Λ: COMPARATOR, Ahmed–Dodelson–Greene–Sorkin astro-ph/0209274, a stochastic ansatz per the B referee) only changes the background to de Sitter, where the graviton is massless (COMPARATOR, M).
- So the law-level or sum-level theory has **no TT analogue of everpresent Λ that generates a graviton mass.**

**Per realization (CHECKED in range; flip count EXACT; ARGUED beyond).**
- Λ's everpresent fluctuation is counting noise: √N, i.e. relative size N^{−1/2}.
- The TT zero mode responds instead to relation flips. Their number, c_d·ρ²·s·T^{2d}, scales like s·N²: superextensive.
- **N3** (same points, no boundary crossings, s = 1e-3; added after PREREG): sd(ΔS)/N stays flat as N grows.

| d | N range | Links: sd/N | BD: sd/N | BD: sd/(N√s) |
|---|---|---|---|---|
| 2 | 202–1798 | 0.013–0.019 | 0.09–0.14 | 2.7–4.3 |
| 4 | 538–2718 | 0.011–0.014 | 0.18–0.21 | 5.7–6.7 |

- So the per-realization zero-mode response **does not average down like counting noise** (over a 13× range in N).
- **Why (ARGUED).** Var ≈ σ_f²·E F, with an O(1) cost per flip of about 1 (links), about 9 (2D BD) and about 28 (4D BD).

**Conclusions.**
- An everpresent-type averaging gives no bound on a random per-realization TT response.
- Because the response is non-analytic (R1), it is not a mass at all.
- The supervisor's analytic-model estimate m_g ~ H ~ 1e-33 eV assumed √N-suppressed, mass-type white noise over the Hubble volume. For these functionals the √N suppression is contradicted in the tested range.

**A pointer for G-A (ARGUED; order of magnitude; extrapolated; not verdict-bearing).** At h = 1e-21 the per-element zero-mode crackle of the BD action is about 6·h^{1/2} ≈ 2e-10. The mean EH action per element for a LIGO wave is about h²(2πℓ_P/λ)² ≈ 1e-123. The ratio is more than 100 decades.

### R8. Known causal-set dynamics (COMPARATOR, M)

- **Classical sequential growth** (Rideout–Sorkin gr-qc/9904062). Discrete general covariance means the probability of reaching a finite order does not depend on its labelling. That is a constraint on the law. Per history it is R5's trivial label invariance. Transitive percolation does not produce 4D manifold-like orders.
- **Sums over 2D orders with the BD action.**
  - Surya arXiv:1110.6244 finds a continuum phase and a layered phase.
  - Glaser–O'Connor–Surya arXiv:1706.06432: finite-size scaling, a first-order transition.
  - Brightwell–Henson–Surya arXiv:0706.0375: uniform 2D orders look like flat diamonds.
  - **2D has no local TT degree of freedom** (3 metric components, minus 2 diffeomorphisms, minus 1 Weyl = 0; EXACT counting). So no 2D toy can test a TT mass, which is why none was run.
- **4D.** The entropy of orders is dominated by Kleitman–Rothschild 3-layer orders. The BD action suppresses some of them partially (Loomis–Carlip arXiv:1709.00064). No 4D sum is known to have a manifold-like phase with a massless spin-2 mode.
- **In every case the protection lives in the law or the measure, never per history,** in line with R2–R6.

### R9. When does a quantum sum protect the realized world? (ARGUED)

- **Coherence.** The sum-level identity governs observed graviton propagation only if the micro-order is not decohered into one realization during the propagation. B referee item 7: "records quench" only if a record fixes the microconfiguration for longer than the probe transit.
- **Recorded events.** In the records-as-events reading, events and their relations are permanent facts (Record, realized-state). The order is then quenched, R2–R4 apply, and Theorem A reduces to E1's protection in law.
- **The price.** A sum-level rescue needs B2's candidate C, "which events neighbour which is itself a possibility, not a record". That is a price on the Record reading, named here only as a price.
- **Even then,** the 4D phase (R8) and the locality and analyticity of the sum-level Γ are open. The E1 referee notes complex zeros of the 4D mean operator.

### R10. Contrast: why Regge lengths escape (COMPARATOR (M) + ARGUED)

- **Regge calculus escapes.** With edge lengths on fixed combinatorics it is flat-blind per realization: zero bulk action on every flat configuration, wherever the vertices sit. It also gives EH in the continuum (Roček–Williams 1981; packet W2: exact vacuum gauge modes).
- **Why.** Lengths carry the conformal factor in each realization. An order carries only the conformal class. Volume enters only through counts, and per realization those counts cannot be told apart from Poisson density noise on a flat background (R3 step 2). That is the structural reason "order plus number" cannot give per-realization protection together with EH.
- **The price this implies.** Per-realization gauge protection with EH needs metric data beyond order and count. Fixed combinatorics loses it once matter is added (W1).

---

## 5. Numerical tables

**N1(b) flip counts, n fixed, ρ = 1, ⟨F⟩/(s·T^{2d}).** Prediction: c₂ = 1/24 = 0.0417; c₄ = 7.26e-4.

| d | T | ⟨N⟩ | Reps | s = 1e-5 | s = 1e-4 | s = 1e-3 | ⟨s_min⟩·T^{2d} (prediction 1/c_d) |
|---|---|---|---|---|---|---|---|
| 2 | 20 | 200 | 20 | 0 flips | 0.025 (0.4 flips) | 0.040 | 29 (24) |
| 2 | 40 | 800 | 20 | 0.041 | 0.042 | 0.043 | 21 (24) |
| 2 | 60 | 1800 | 20 | 0.035 | 0.041 | 0.041 | 41 (24) |
| 4 | 6 | 170 | 20 | 0 | 6.0e-4 (0.1 flips) | 6.3e-4 | 1763 (1378) |
| 4 | 8 | 536 | 20 | 1.2e-3 (0.2 flips) | 6.9e-4 | 7.7e-4 | 1791 (1378) |
| 4 | 10 | 1309 | 12 | 5.0e-4 (0.5 flips) | 7.75e-4 | 6.8e-4 | 1184 (1378) |

The sd/mean of s_min is 0.7–1.1, so the s_min column matches only within a factor of about 1.5.

**N1(c) region-fixed: BD action, per realization.**

| d | s | 1e-5 | 1e-4 | 1e-3 | 1e-2 | 1e-1 |
|---|---|---|---|---|---|---|
| 2 (T = 40, 40 reps) | sd/√s | 2781 | 3273 | 2959 | 2024 | 1172 |
| 2 | fraction unchanged | 0.45 | 0.03 | 0 | 0 | 0 |
| 4 (T = 8, 24 reps) | sd/√s | 5885 | 3463 | 4924 | 3153 | 3568 |
| 4 | fraction unchanged | 0.62 | 0.25 | 0 | 0 | 0 |

The means are consistent with 0 throughout. ΔR is dominated by points crossing the boundary.

**N2:** the kernel-count table is in R6. **N3:** the size-scaling table is in R7. **N4:** in R2.

All of these are per-realization statistics from small samples, not laws. The verdict rests on Lemma B and Theorem C, not on any fit.

---

## 6. Strongest correct statement

Take order-only (and link-only, marks allowed) functionals of a frozen, sprinkled realization.

1. **Lemma B.** An exact per-realization identity that kills the TT zero-mode response, holding at a uniform amplitude for almost every realization, exists if and only if the functional is flat-blind. A non-uniform, infinitesimal identity holds for every functional and says nothing.
2. **Theorem C.** Flat-blind order functionals are conformally blind. Under locality, Lorentz invariance in law, a smooth mean and stationarity, their mean (and every cumulant) quadratic action is k⁴g(k²)P^(2): no TT mass and no Einstein–Hilbert term. Without locality, the best k² behaviour has the vDVZ tensor structure, which light bending excludes.
3. **The no-go.** So every order-only action with an EH mean, including BD, has no per-realization protection. Per realization, its zero-mode response is piecewise constant and non-analytic, and in the tested range it is superextensive.
4. **Theorem A.** The exact Ward identity holds for the law and for every covariant sum over orders: Diff with proper-volume sprinkling, WTDiff with coordinate sprinkling. There it forbids local analytic TT masses. It protects the realized physics only if the micro-order is unrecorded, and its 4D premises are open.
5. **The intrinsic picture.** Diffeomorphisms act trivially and there are no gauge directions. A per-realization TT mass is not an observable, because it depends on the coupling used to compare realizations.

---

## 7. Strong-word check

| Strong claim | Holds only under |
|---|---|
| "no … functional with an EH mean can …" | H1, H2, H4 and H5. H4's locality is the soft spot: it is used for "no EH", but not for K = aP² |
| "if and only if flat-blind" | H1–H3: uniform s₀, a.e. P, one TT polarization |
| "every functional of the law" | proper-volume Poisson sprinkling and diffeomorphisms of D that are the identity near ∂D (SDiff for picture I) |
| "only (tr h)²" | degree-0 Lorentz-covariant kernels under TDiff |
| "superextensive" | CHECKED over 13× in N, in 2D and 4D, for two functionals, at s = 1e-3 only |
| "about 300 decades into the crackle regime" | the exact leading-order flip count, evaluated (no fit) |

---

## 8. What a referee should re-check

1. **Lemma B's transversality argument.** Check:
   - that Z has codimension ≥ 2;
   - single-wall crossings with ∂_sτ² ≠ 0;
   - the open set of P₋ that meets the a.e. hypothesis;
   - Cδ < s₀;
   - the marked version.

   N4 tests the conclusion for n = 3, 4 and 5.
2. **Theorem C.** Check:
   - that the identity Γ_S[Ω²φ*η] = G(ρ·Vol) holds;
   - that stationarity forces G′ = 0;
   - that the G″ term is pure k = 0;
   - that the Barnes–Rivers step gives c = 0;
   - the N2 counts.

   **Key question:** is H4's polynomial-kernel locality reasonable for causal-set functionals, which are non-local along the light cone? For BD the mean converges to local EH (COMPARATOR), so H5 and H4 are jointly met at leading order (M).
3. **H3's uniformity.** Is a uniform-amplitude identity the right notion? Given R1's vacuity result, I think so, but the referee should rule.
4. **R5's coupling-dependence claim,** and whether any other notion of per-realization mass escapes it.
5. **The numbers.** The derivation c₂ = 1/24, the Monte Carlo for c₄, the N1/N3/N4 code, and the per-flip-independence heuristic behind N3.
6. **The split verdict.** Should Theorem A count as a PASS for the "or" clause? I recorded it as INCONCLUSIVE because its physical premises are open.
7. **COMPARATOR items (M), none re-fetched:** Benincasa–Dowker 2010, Rideout–Sorkin 1999, Surya 2012, Glaser–O'Connor–Surya 2018, Brightwell–Henson–Surya 2008, Loomis–Carlip 2018, Álvarez–Blas–Garriga–Verdaguer 2006, Roček–Williams 1981, the masslessness of the dS graviton, and Kleitman–Rothschild.

---

## 9. What I read

**In full:**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`.
- Packet: TESTS.md (the rules and all of Campaign C3), SUMMARY.md §§7–9, `agents/B1_report.md`, `B2_report.md`, `B_referee.md` (including corrected Lemma Q), `E1_referee.md`, `supervisor_thread.md` (Lemma P and its corrections).

**In part:** `agents/E1_report.md` (the verdict, operators, (a)–(d) and the referee list); `scripts/E1/E1_6b_strain.py` and its `.out`.

**Own prior-art check.** I grepped `docs/` for "causal set", "Stückelberg" and "discrete general covariance".
- I found only background citations (the Lorentz-boost notes and a historic intake note) and an unrelated U(1) Ward note (`docs/EXACT_GAUGE_WARD_RESPONSE_IDENTITIES_BOUNDED_THEOREM_NOTE_2026-09-15.md`).
- Packet prior art: E1(a), B1 §2.11, and B referee item 15.

No papers were downloaded.

---

## 10. Files

All paths are under `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-C/`:

- `PREREG.md`
- `scripts/N1_crackle_gauge.py`, with `scripts/N1_d2.out`, `scripts/N1_d4_id.out`, `scripts/N1_d4_flips.out`, `scripts/N1_d4_resp.out`
- `scripts/N1b_flip_constant_4d.py`, with `scripts/N1b_flip_constant_4d.out` and `scripts/N1b_translation.out`
- `scripts/N2_kernel_classification.py`, with `scripts/N2_kernel_classification.out`
- `scripts/N3_zero_mode_size_scaling.py`, with `scripts/N3_d2.out` and `scripts/N3_d4.out`
- `scripts/N4_lemmaB_transition_graph.py`, with `scripts/N4_lemmaB_transition_graph.out`

**Runtime.** Every script runs in under 3 minutes with OMP_NUM_THREADS=2, and memory stays under 1 GB. N3 runs `N1_crackle_gauge.py` in-process, via `exec` of its function section.

---

## Appendix: c₂ = 1/24 (EXACT, leading order in s)

**Setup.** 2D diamond of height T, ρ = 1, shear (t, x) → (t, x + st).
- The interval is τ²(s) = Δt² − (Δx + sΔt)², so ∂_sτ² = −2ΔtΔx at s = 0. On the cone Δx = ±Δt, |∂_sτ²| = 2Δt².
- ∫dΔx δ(τ²) contributes 1/(2Δt) on each branch.
- So E F/s = ∫_D dx Σ_± ∫_0^{Δt_max} Δt dΔt.

**Light-cone coordinates.** Let u = (t + x)/√2 and v = (t − x)/√2, each in (0, a), with a = T/√2.
- The +x null displacement changes only u, by √2·Δt, so Δt_max = u/√2 and the inner integral is u²/4.
- The other branch gives v²/4.

**Result.** E F/s = ∫∫ (u² + v²)/4 du dv = a⁴/6 = T⁴/24.

**4D.** The same null-shell formula gives E F/s = ∫_D dx ∫ dΩ |(n²)² − (n³)²| · Δt_max⁴/4, where Δt_max = (t² − r²)/(2(t − x·n)). Its Monte Carlo value is c₄ = 7.258e-4·T⁸.


---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** False

**Corrected verdict:** Under the fixed reading, G-C is INCONCLUSIVE, not FAIL. The reading gives one verdict for a question with two branches ("does a per-realization identity exist ... or does a quantum sum supply it?"). A FAIL needs a no-go that closes both branches, and the sum branch is open.

What the lane does deliver is a correct but conditional partial no-go for the per-realization branch. It still owes the codex sol referee.

**Supported core (I could not refute it).** Take picture I: a frozen embedded sprinkling whose metric perturbation acts only through the causal order of fixed points. Under H1–H5:
- Uniform invariance under a constant TT strain, holding in every realization (H3), is equivalent to the functional being "flat-blind" (Lemma B).
- A flat-blind functional's mean quadratic kernel is a(k²)P^(2), with no spin-0 part. So an Einstein–Hilbert (EH) mean is impossible.
- Therefore no order-only or link-count functional with an EH mean, BD included, has the identity.

Locality is not needed for the EH exclusion. Linearized EH has a non-zero P^(0s) (Weyl-direction) part, and N2 itself prints "linearized EH kernel annihilates eta (Weyl): False". So the no-go holds under H4 without locality, which is stronger than the worker states. Locality is needed only for "no TT mass in a flat-blind mean".

**The headline is broader than the proof.** The no-go must be scoped to:
- picture I (frozen labels, fixed-point coupling);
- one polarization, a constant strain, and uniform s0;
- functionals of the order with marks on points.

It does not cover dynamics of separate fields carried on links (the G-B class), which could have internal coboundary or conservation identities. Lemma B's marks ride on points, not on links that flip. It also does not cover picture II. There the worker's own R5 shows that a per-realization TT mass depends on the coupling: in the co-moving coupling ΔS ≡ 0 for every S. Choosing the fixed-point coupling as the physical one is only ARGUED.

**The sum branch is INCONCLUSIVE, but Theorem A must be re-scoped.** It is exact, but it is a statement about functionals of the background-dependent sprinkling law μ_g: the induced effective action of a fixed background. It is not about a background-free dynamical sum over orders, and it exhibits no mechanism for an emergent graviton. Its 4D premises are open.

**Corrected record.** "G-C: INCONCLUSIVE. Contains a conditional no-go for per-realization zero-mode protection of order-functional (G-A-class) gravitons with an EH mean (picture I, H1, H2, H4 without locality, H5), referee owed. Link-field (G-B-class) identities untested. The sum-level identity is exact in law, but its physical premises are open."

**Issues:** 1. **The verdict is mapped onto halves.** The TESTS.md reading has one PASS/FAIL/INCONCLUSIVE for the whole question. The split into halves comes from the worker's own PREREG, not from TESTS.md. Because the question is a disjunction and the sum branch stays INCONCLUSIVE, the lane verdict is INCONCLUSIVE. The worker's "FAIL" row could be recorded as a lane FAIL, which would be wrong.

2. **The headline is broader than the proof.** The headline reads "any order-only or link-only dynamics", and the lane question explicitly includes coboundary and conservation identities. The proof covers:
   - functionals S(ord(P, g)) of a frozen embedded point set, with marks on points;
   - the metric entering only through the order.

   It does not cover a separate tensor field on links (the G-B setting) with an internal per-realization gauge, coboundary or conservation identity. Link marks do not ride along when links flip. Corollary B' covers such mechanisms only when they act on the embedding-metric zero mode. R5 handles G-B only with a concentration bound, which is neither an identity nor a no-go.

3. **The no-go depends on the picture.** The worker's own R0/R5 show that with co-moving points, ΔS ≡ 0 for every S. So "per-realization TT mass" is coupling-dependent, and the FAIL holds only in picture I with the fixed-point coupling. The claim that this coupling is canonical, via the k→0 limit of k≠0 waves, is ARGUED. The verdict text should name picture I explicitly.

4. **The soft-spot statement is wrong, in the conservative direction.** §7 says locality is "used for 'no EH'". It is not. Step 4 (c = 0) already excludes EH, because linearized EH has a non-zero P^(0s) part. Locality is used only for a(0) = 0. The no-go therefore holds under H4 without locality.

5. **Theorem A is mis-labelled as a sum over orders.** "EXACT at every covariant sum" refers to Σ_C μ_g(C)e^{iS(C)} and similar quantities. These are functionals of the sprinkling law of a fixed background g, and their invariance follows directly from the mapping theorem. That is not a background-free dynamical sum over orders. It should be worded as "law-level / induced effective action of a background".

6. **"Superextensive" is a misnomer.** The flip count is superextensive (∝ sN²). But sd(ΔS) ∝ √s·N is extensive: sd/N is flat, as N3 and my V2 both show. The correct contrast is extensive versus counting noise ∝ √N. The word appears in R4, §6.3 and §7.

7. **The "13× range in N" combines two dimensions.** Within each dimension the range is 8.9× (2D) or 5.05× (4D). The 4D T=6 row (N=170, links sd/N = 0.0245) is dropped from the quoted range without a note. N3 runs only s = 1e-3. The 2D rows use a shear, which is not TT; the worker itself says 2D has no TT mode.

8. **The extrapolation crosses a regime change.** The tested 4D regime has s²T⁴ ≤ 0.02, where flipped pairs are links. At a LIGO cell, s²T⁴ ~ 1e123, so flipped pairs have huge intervals and flips cascade. In my V2, at s²T⁴ ≈ 200 the fraction of flips with non-empty intervals has already risen to 11%. The pointer of 6h^{1/2} per element for G-A, and the §2 lines "No averaging out" and "gives no bound", are uncontrolled beyond the tested range. The worker labels the G-A pointer as not verdict-bearing, which is correct, but §2 should also say "in the tested range".

9. **The N1(c) outputs cannot be reproduced from the shipped script.** The invocation and seed were not recorded. For d=2 and d=4 with seed 7 the outputs differ. At s = 1e-5 the worker reports a BD fraction unchanged of 0.62. Across 14 seeds I get 0.75–0.92, and the bulk prediction exp(−c4·s·T⁸) is 0.89. At s = 1e-5, sd/√s ranges from 575 to 7770 across seeds, so "flat within factor ~2 from 1e-5 to 1e-1" is not robust at small s, where only a few pairs flip. This is illustrative only and not verdict-bearing.

10. **Strong word in the plain summary.** "A shape-changing stretch always changes the action" overstates the result. The theorem gives a positive-probability set. The relation-flip count makes a change near-certain at physical scales, but that is shown for the relation count, not proved for each action.

11. **The math held up.** Nothing in Lemma B, Theorem C step 3, the Barnes–Rivers step (K(η,η) = 3c), the N2 counts, c2 = 1/24, c4, the physical flip-count translation, or the vDVZ/γ = 1/2 remark was found wrong.

**Re-runs:** All runs are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-C/verify/`, with OMP_NUM_THREADS=2. Each took under 1 minute.

**V1_pair_flip_constants.py (V1.out).** An independent check of the flip constants by direct pair sampling, without the null-shell formula:

| d | s | E F/(s·T^{2d}) | Target |
|---|---|---|---|
| 2 | 1e-2 | 0.041649 ± 1.1e-4 | 1/24 = 0.041667 |
| 2 | 1e-3 | 0.04162 ± 3.6e-4 | 1/24 |
| 4 | 3e-2 | 7.249e-4 ± 1.6e-6 | worker 7.258e-4 |
| 4 | 1e-2 | 7.262e-4 ± 2.8e-6 | worker 7.258e-4 |
| 4 | 3e-3 | 7.224e-4 ± 5.1e-6 | worker 7.258e-4 |

Both constants are CONFIRMED. The log10 E F ≈ 306 at a LIGO cell follows from them.

**V2_bulk_crackle_regimes.py (V2.out).** My own re-implementation of the BD and link response with fixed n and no boundary, in 4D, for T = 8, 10, 12 and s = 1e-3 to 1e-1:
- ⟨F⟩ matches c4·s·T⁸ to within 1–2%.
- BD sd/(N√s) is 3.7–8.2, roughly flat in both s and N.
- Links sd/sqrt(F) is 1.2–2.4, and BD sd/sqrt(F) is 18–39.
- The fraction of flips with a non-empty interval is 0.000 at s²T⁴ ≤ 0.2, 0.006–0.014 at s²T⁴ ≈ 9–19, and 0.029–0.114 at s²T⁴ ≈ 41–207.

This supports sd ∝ √s·N (extensive) in the tested range. It also shows the regime change toward physical s²T⁴ ~ 1e123.

**V3_boundary_vs_bulk.py (V3.out).** At T = 8, 4D, 60 realizations, the boundary-crossing count is 0.02 at s = 1e-5 and 0.05 at s = 1e-4:

| s | Fixed-n fraction unchanged (R / BD) | Fixed-region fraction unchanged (R / BD) | Bulk prediction |
|---|---|---|---|
| 1e-5 | 0.87 / 0.83 | 0.83 / 0.83 | 0.89 |
| 1e-4 | 0.43 / 0.35 | 0.47 / 0.40 | 0.30 |

**Re-runs of the worker's N1_crackle_gauge.py.**
- d=2 with seed 7, mode all: the (a) lines are identical, but (b) and (c) differ from N1_d2.out.
- d=4 with mode resp, 14 seeds: BD fraction unchanged at s = 1e-5 is 0.75–0.92, against the worker's 0.62. sd/√s is 575–7770.
- d=4 with mode flips, seed 7: differs from N1_d4_flips.out.

The outputs cannot be reproduced without the original invocation, though they are statistically consistent.

**V4_lemmaB_graph.py and V4b_lemmaB_exact_crossings.py (V4.out, V4b.out).** These test Lemma B's combinatorial core. V4b solves each pair's wall crossing exactly:

| n | s0 | Samples | Result |
|---|---|---|---|
| 5 | 0.002 | 100k | 63/63 posets, 1 component |
| 6 | 0.01 | 800k | 318/318 posets realized, 1 component containing the antichain |

The worker's N4 result is extended to n = 6 and a 25× smaller s0. In V4, which uses random strains, the graph fragments only because too few crossings are sampled.

**N2.** I read the code and the output. The counts (Diff 0/1/2, Diff+Weyl 0/0/1, TDiff 1/3/4, WTDiff 0/1/2) agree with the standard results, including WTDiff via EH of ĝ, and "EH annihilates η: False". I did not re-run it.
