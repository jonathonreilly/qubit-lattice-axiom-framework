# Lane R, probe R3 (events): a quantum sum over event orders, with relabelling as the redundancy

**Worker:** Claude Opus 5.5 (same family as the supervisor and the earlier C3 workers). Not refereed. The repository was not edited.
**Time:** 10:29Z to about 10:55Z, 2026-10-10.
**Scratch:** `.../scratchpad/laneR/R3/`. It holds `PREREG.md` (stamped 10:38:46Z, before any numerics), `scripts/`, and the `*.out` files.
**Labels:**
- **proved:** an exact argument given here.
- **checked:** a computation run here.
- **suggested:** an argument, or an assembly of results that are not all refereed.
- **reading:** an interpretation.
- **comparator:** literature. (M) means from memory; (S) means from a search snippet or abstract only. No paper was downloaded.

## 0. Verdict against the FIXED readings

**Worker verdict: INCONCLUSIVE, leaning FAIL.** It is not a PASS, because no model in this class exhibits criterion (i).

| Candidate class | (i) gapless helicity-2, linear | (ii) protected | (iii) universal | (iv) tunings ≤ P0 | Class reading |
|---|---|---|---|---|---|
| **A.** Background-free Lorentzian sum Σ_C e^{iS(C)} over orders, with S an interval-count action (local BD, smeared BD, link action) | No macroscopic propagating TT mode: the TT sector is dominated by the variance term (§3, the dilemma) | Only against *local analytic* masses. The sum generates a non-local, Diff-invariant TT term | Conditional only | The KR window is an O(1) range, not a tuning | **Suggested FAIL, bounded to class A.** Conditional on A1–A4 (§3). **It needs the codex sol referee before it can be recorded as FAIL.** |
| **B.** Background-free sums with positive weights e^{−S} or probabilities (the framework's own Admissibility type), interval-count S | No manifold-like phase: non-manifold orders win | — | — | — | **Proved for the bilayer and antichain classes (elementary).** Non-manifold orders are never suppressed (§2). The class cannot reach (i) |
| **C.** Other amplitudes: non-interval-count actions, sums restricted by hand to manifold-like orders, complex sequential growth | Not shown. No 4D manifold-like phase is known in the literature (comparator) | Law-level Diff identity only (§1) | Conditional | Unknown | **INCONCLUSIVE** |

**Expected lane reading** (registered: "INCONCLUSIVE, leaning FAIL on (iii)"). For R3 the lean comes earlier, at (i) and (ii), not at (iii).

## 1. What relabelling invariance gives, and what it does not

**R3-1 (proved; mostly already in G-C R5).** In a sum over orders, relabelling is the global, finite, discrete group S_n. The sum over unlabelled orders quotients it out exactly.
- A single order has only Aut(C), a finite group.
- The configuration space of unlabelled orders is discrete. It has no continuous gauge orbits and no local generators.
- So no Noether-II or Ward identity holds on any single history.
- The redundancy is exact, but it is "used up" by the quotient. It constrains nothing per history.

**R3-2 (proved; checked in N-d).** Relabelling does not act like diffeomorphisms on perturbations of a sprinkled background in any local way.
- A continuum diffeomorphism acts on a sprinkling in one of two ways:
  - **co-moving** (Stückelberg): the poset is identical (G-C R0);
  - **as a displacement of points at a fixed metric:** this is a *physical* change of the order, not gauge.
- So the pure-gauge directions of the continuum have zero extent in poset space. There is no split of nearby orders into "gauge ⊕ physical".
- **A local move is not local in the relation graph.** Moving one event by δ flips relations with partners spread over its whole light cone. The count grows like ρ·δ·T³.
  - **Checked (N-d, 4D, δ = 0.05, 40 realizations per T):** 0.57, 2.60, 7.92 and 23.1 flips at T = 6, 9, 13 and 19. The local exponents are 3.7, 3.0 and 2.8, against a prediction of 3.
  - The median time-separation of flipped partners grows with T (1.2 → 3.7).
- This is the quantitative face of BHS: there is no finite-valency, Lorentz-equivariant neighbourhood in which a "local gauge move" could act.

**R3-3 (reading, with a comparator).** In sequential-growth language, relabelling is a change of birth order (a linear extension), i.e. a discrete refoliation. Rideout–Sorkin's "discrete general covariance" constrains the growth *law*. It is the discrete analogue of refoliation invariance, the role of the Hamiltonian constraint (comparator, M). Orders have no spatial labels, so no analogue of the momentum constraints arises from it.

**R3-4 (proved in G-C as Theorem A; here conditional on A1).** The redundancy acts only through the coarse-graining fiber {C ~ g}. Suppose there is a covariant fiber map, i.e. which orders count as faithful to (D, g) is defined from the isometry class of g (A1, a Hauptvermutung-type premise). Then every fiber-level functional is exactly Diff-invariant:
- the mean, all cumulants, and Γ[g] = −i log Σ_{C~g} e^{iS(C)}.

That forbids every **local analytic** TT mass (the B referee's proved gauge-identity statement).

**R3-5 (proved; standard linearized algebra).** Diff invariance without locality does not forbid a TT mass.
- Take m²∫C_{μνρσ}□⁻²C^{μνρσ}. It is exactly Diff-invariant.
- Its quadratic kernel is m²·P^(2): the linearized Weyl² kernel k⁴P^(2) divided by k⁴.
- That is a gauge-invariant, non-local spin-2 mass. It is the explicit form of G-C R3's "a(0) ≠ 0 is not excluded without locality".
- **Conclusion:** relabelling invariance protects masslessness only together with a *locality theorem for Γ* at scales ≫ ℓ_k. The redundancy does not supply that theorem.

## 2. The non-manifold entropy problem

**R3-6 (proved, elementary; checked in N-a).** On a bilayer (height ≤ 2) order every relation is a link. So for **any** interval-count action S = c_n·n + Σ_k c_k N_k we get N₀ = R and N_{k≥1} = 0. Checked on 200 random bilayers.

The labelled bilayer sum with layers of size n/2 is exactly:

e^{iφ_n n}(1 + e^{iφ_l})^{n²/4}.

The brute force over all 512 graphs at a = b = 3 matches the closed form: |Z| = 0.015778 in both.

- **Lorentzian weights.** Bilayers are suppressed below the at most e^{O(n ln n)} manifold-like orders **if and only if** |1 + e^{iφ_l}| < 1, i.e. φ_l mod 2π ∈ (2π/3, 4π/3).
- **Positive weights e^{−S}.** The sum is e^{−an}(1 + e^{−b})^{n²/4}, which grows like e^{c n²} with c = ln(1 + e^{−b})/4 > 0 for every finite b.
  - For b > 0 the antichain (weight e^{−an}) also beats manifold-like orders, whose link count grows like n^{3/2}.
  - So **no positive weighting by an interval-count action selects manifold-like orders.**
  - This includes the probability-measure type that Admissibility supplies (proved for these two classes).

**The window for 4D BD.** φ_l = (4/√6)(ℓ/l_p)² ε^{3/2}, with l_p² = 8πG (G-A's convention).
- Local BD is in the first window iff ℓ/l_p ≥ 1.1325 (checked).
- **Comparator (S):** a Carlip talk reports Z_bilayer ~ 2^{−cn²} "for ℓ > 1.136 ℓ_p". That agrees to 0.3%; the exact convention was not read.
- At ℓ = √G the per-link phase is 0.065 (G-A's figure), outside the window, so bilayers dominate.
- Loomis–Carlip (arXiv:1709.00064, S) and Mathur–Singh–Surya (arXiv:2009.07623, S: the link action suppresses KR orders "for the same range") are the literature versions. Both are bounded to these classes.

## 3. The dilemma: entropy suppression against variance pinning (suggested)

**R3-7 (suggested; assembled).** For class A, the per-link phase that defeats the KR entropy is the same per-relation sensitivity that makes the action's per-history variance huge. The variance's TT response is wavelength-independent.

**Ingredients.**
- **(a)** The bilayer window φ_l ≥ 2π/3 (R3-6, proved).
- **(b)** Var_η S ≥ (16/6)·0.0191·(ℓ/l_p)⁴·ε^{5/2}·(L/ℓ)⁶ for a 4-box of side L. This is G-A's Last–Penrose second-chaos bound: the local form is referee-checked; the ε^{5/2} smeared scaling is the G-A normalization the G-A referee accepted through ℓ_k ≈ 3e-19 m.
- **(b′) The orbit-volume lemma** (proved for pair kernels; checked in N-b). In a 4D region of size T, **every** nonzero Lorentz-invariant pair kernel has ∫∫K² ∝ T⁶. The Lorentz orbit of a timelike pair is a hyperboloid whose volume inside the region grows like (T/τ)²; in 2D the growth is T² log T.
  - **N-b (checked):** the 4D invariant kernel has local slopes 7.1, 6.8, 6.45, 6.32 and 6.09 up to T = 30, approaching 6. A non-invariant (Euclidean-shell) kernel has slopes 4.3, 4.2 and 3.9, approaching 4. This is within the pre-registered 6 ± 0.4 and 4 ± 0.3 at the largest T.
  - **Sketch, not proved:** this extends to k-point chaos kernels, because Lorentz orbits of k-tuples are non-compact. With G-C Theorem C it would give: *every order-only action with an EH mean has Var ≥ c·L⁶*. So superextensive variance is not a BD quirk but the price of Lorentz invariance in law together with an EH mean.
- **(c)** N1 (same family, checked; strictly INCONCLUSIVE on its own coefficient wording at kU = 30). The long-baseline TT response of the second-chaos functional is (I₀(h)^{1/2} − 1)·V₂ ≈ (h²/8)·V₂. It is independent of ω.
- **(d)** G-A's generous comparator, S_kin = h²ω²V/(64πG).

**Result** (`dilemma.out`; the formula is cross-checked against direct numbers, both giving R = 2.08e157 at ℓ = 1.2 l_p, L = 1e6 m):

R := δ_TT Var / S_kin = 7.9e-4 · φ_l · (L/ℓ_k)⁴.

With φ_l ≥ 2π/3 this gives R ≥ 1.65e-3·(L/ℓ_k)⁴. So R ≤ 1 needs **L ≤ 5ℓ_k**.

But an EH mean needs L ≫ ℓ_k. There is therefore **no window** in which both of these hold:
- non-manifold orders are suppressed;
- a macroscopic TT mode is governed by the EH term rather than by the non-local variance term.

| Wavelength | ℓ_k needed for R ≤ 1 |
|---|---|
| LIGO cell, L = 1e6 m | ≥ 2e5 m |
| PTA, L = 1e16 m | ≥ 2e15 m |
| CMB tensors, L = 1e25 m | ≥ 2e24 m |

Requiring no damping over 1 Gpc of LIGO propagation (R ≲ λ/D ≈ 3e-20) needs ℓ_k ≥ 1.5e10 m.

Prefactor uncertainties (box against slab geometry; (b) is a lower bound; N1's coefficient) are O(10). They move the ℓ_k bound by at most a factor of about 2, because R ∝ ℓ_k⁻⁴.

**Assumptions the class-A FAIL rests on** (each is a referee item):
- **A1:** a covariant fiber map C ~ g exists (Hauptvermutung-type).
- **A2:** the fiber's counting measure has the sprinkling law's second-chaos structure. This is what reduces the background-free sum to G-C's induced Γ, the object the G-C checker said Theorem A actually covers.
- **A3:** |Σ_{C~g} e^{iS}| ≈ N_g·e^{−Var_g/2}. This is the Gaussian / local-CLT form; for local BD, S is μ × an integer, which needs μ ≠ 0 mod 2π, true in the window.
- **A4:** the TT response of the higher chaoses does not cancel the second-chaos response. Comparing Im Γ with Re Γ as "the mode is pinned or overdamped" is a **reading**.

**A stricter reading** (not used for the verdict). In Sorkin's quantum measure, a coarse-grained history with a TT wave carries relative weight about exp(−(h²/8)·Var). At the observed h = 1e-21 in a LIGO cell that is about e^{−1e196}.

**Relation to the packet.** This turns P8(ii) ("no e^{iS} weighting by interval-count actions") from a one-sided kill into a two-sided one:
- without e^{iS} weighting (or with positive weights), the KR and bilayer entropy wins (R3-6, proved);
- with it, the variance pins the TT sector (R3-7, suggested).

It is consistent with the Route-2 kill and N1 (same family). At ℓ = √G it reproduces the Route-2 figure ℓ_k ≈ 10^{−18.5} m to within the O(10) prefactor; that point is outside the KR window.

## 4. Prior art (comparators)

- **Causal-set sums.**
  - Surya's review (arXiv:1903.11544, S).
  - Benincasa–Dowker, arXiv:1001.2725 (M): the BD mean tends to EH.
  - Dowker–Glaser, arXiv:1305.2588 (M).
  - 2D sums restricted to 2-orders show continuum and layered phases (Surya 1110.6244; Glaser–O'Connor–Surya 1706.06432; M).
  - Loomis–Carlip and Mathur–Singh–Surya: bilayer and KR suppression in a coupling window (S).
  - **Nobody has shown a 4D manifold-like phase, and no causal-set graviton has been computed** (M; G-C R8). 2D has no TT degree of freedom.
- **CDT** (Ambjørn–Jurkiewicz–Loll; M). 4D de Sitter volume profiles and a minisuperspace effective action. A transverse-traceless graviton propagator is not established. The foliation is a supplied structure.
- **Regge calculus.**
  - Roček–Williams 1981 (M): linearized Regge on a hypercubic subdivision gives massless gravitons in the continuum limit. The vertex-translation gauge symmetry is exact only about flat backgrounds and broken on curved ones (Bahr–Dittrich; M).
  - Dittrich–Kamiński–Steinhaus (arXiv:1404.5288, abstract, S): no *local* path-integral measure makes 4D linearized Regge invariant under the 5–1 and 4–2 Pachner moves; non-locality is suggested as the way out.
  - **Same direction as R3-5 and R3-7:** exact discrete diffeomorphism or discretization invariance in 4D pulls toward non-locality.
- **Spin foams** (Rovelli 2006; Bianchi–Modesto–Rovelli–Speziale; Bianchi–Magliaro–Perini 2009; M). The leading-order large-spin graviton propagator on one or a few simplices matches linearized Regge or GR. The "flatness problem" (Bonzom; Hellmann–Kamiński; M) is open. These are supplied-background semiclassical results, not a protected mode of a background-free sum.

**Net comparator reading.** In every approach the massless graviton appears either on a supplied (near-)flat background or semiclassically. None derives it as a protected mode of a background-free sum. Where exact discrete gauge invariance is pursued in 4D, non-locality appears.

## 5. Prices on top of P1–P4 (named only; nothing adopted)

| # | Price | Touches | Why it is needed |
|---|---|---|---|
| R3-a | **Complex amplitudes on whole histories** (a quantum measure / decoherence functional), not a nonnegative probability distribution | Admissibility's distribution clause (a probability measure per site from nearest-neighbour conditions) | R3-6: positive weights cannot select manifold-like orders, for interval-count actions (proved for bilayers and antichains). M-C already showed matter needs signs or phases |
| R3-b | **An unrecorded micro-order** ("which events relate to which is a possibility, not a record") | Record, beyond P4 | The sum must stay coherent over a graviton transit (G-C R9; B2 candidate C). If the order is recorded, R3 collapses to G-C's frozen picture |
| R3-c | **A covariant coarse-graining map** from orders to geometries (Hauptvermutung / faithful embedding at density ρ) | a new readout primitive | Without it no spin-2 field is even defined; the redundancy acts only through this fiber (R3-4). No intrinsic test for 4D-embeddable orders is known |
| R3-d | **An amplitude that is not interval-count, or a supplied restriction of the sum to manifold-like orders** ("dimensional restriction") | a new primitive; non-local selector | Interval-count amplitudes cannot do both jobs (R3-7). The replacement must (1) beat the 2^{n²/4} entropy, which needs Θ(n²) log-amplitude variation on non-manifold orders, and (2) keep per-history fluctuations TT-blind at L ≫ ℓ_k. No such amplitude is known. R3-7 suggests (2) fails for any order-only action with an EH mean unless its variance's TT response is not ω-independent |
| (obligation) | **A locality theorem for the induced Γ** at scales ≫ ℓ_k | — | R3-5: Diff invariance alone allows m²C□⁻²C |

There is no new price for one cone: Lorentz invariance in law gives it in mean (E1, E1′). Λ is free; it is conjugate to n (everpresent Λ). That is the ordinary cosmological-constant problem, not counted here.

## 6. Strong-word check

| Claim | Holds only under |
|---|---|
| "every" Lorentz-invariant pair kernel gives T⁶ | pair kernels in the bulk of a 4D region; the k ≥ 3 extension is a sketch |
| bilayers suppressed "iff" φ_l ∈ (2π/3, 4π/3) | interval-count actions; labelled bilayers dominated by the balanced layer split |
| "no" positive weighting selects manifold-like orders | interval-count actions; bilayer and antichain competitors |
| "no window" | the BD family's variance coefficient (G-A) plus N1's coefficient plus A1–A4; prefactor O(10) |
| relabelling gives "no" per-history Ward identity | exact (a discrete quotient); G-C R5 |

## 7. What a referee should check

1. **R3-6.** The closed form, the window, and the claim that every interval-count action reduces to (n, R) on bilayers.
2. **R3-7's reduction.**
   - The background-free fiber against the sprinkling law (A1, A2).
   - The Gaussian magnitude (A3).
   - That the higher-chaos TT response does not cancel (A4).
   - The elimination algebra R = 7.9e-4·φ_l·(L/ℓ_k)⁴.
3. **The orbit-volume lemma** and its sketched k-point extension, combined with G-C Theorem C.
4. **R3-5:** the C□⁻²C kernel.

## Files

All under `.../scratchpad/laneR/R3/`:
- `PREREG.md`
- `scripts/na_bilayer.py` → `na_bilayer.out`
- `scripts/nb_orbit.py` → `nb_orbit.out`, and `scripts/nb_orbit_ext.py` → `nb_orbit_ext.out` (larger T, run after the first output and before interpreting it)
- `scripts/nd_pointmove.py` → `nd_pointmove.out`
- `scripts/dilemma.py` → `dilemma.out`

Every run took under 1 minute with OMP_NUM_THREADS=2.

**Read in full:**
- the axioms memo;
- SUMMARY.md;
- PRICE_NOTE.md;
- the Lane R section of TESTS.md;
- C3_G-C_report.md (with its adversarial check);
- the G-C and G-A referee headers;
- C3_exercise_G_graviton.md.

**Read in part:** C3_G-A_report.md (normalizations, I_BD, S_kin) and the Route-2 kill outputs in the C3 scratch folder.

**C3_G-L_referee.md:** only its verdict and findings 1–2 were read (link readouts; not load-bearing for R3). The PRICE_NOTE and SUMMARY entries on G-L were also used.

## Sources (search results only; no downloads)

- [Loomis–Carlip, arXiv:1709.00064](https://www.arxiv.org/pdf/1709.00064)
- [Mathur–Singh–Surya, arXiv:2009.07623](https://www.arxiv.org/pdf/2009.07623)
- [Surya review, arXiv:1903.11544](https://arxiv.org/pdf/1903.11544)
- [Carlip talk slides (ICRANet)](https://indico.icranet.org/event/8/contributions/1623/attachments/594/1163/MGb.pdf)
- [Dittrich–Kamiński–Steinhaus, arXiv:1404.5288](https://www.arxiv.org/abs/1404.5288)
- [Dittrich–Steinhaus, arXiv:1110.6866](https://ar5iv.arxiv.org/html/1110.6866)
