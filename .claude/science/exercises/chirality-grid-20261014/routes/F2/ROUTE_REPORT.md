# Route agent F2: exact but modified (Ginsparg–Wilson / not-on-site) lattice chiral symmetry

**Agent:** Claude Opus 5.5. Same model family as the supervisor and the other route agents, so this is not an independent referee. Run 2026-10-14, 13:19–14:00Z. No repository file was edited.
**Folder:** `scratchpad/chirality_ex/routes/F2/`. It holds `PREREG.md` (pre-registrations, written before each run, with amendments) and `scripts/` (five scripts and their outputs).
**Refresher read:**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- Skimmed: `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` and `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`.
- Read where cited: `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` and `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`.
- The skill (steps 4 and 6) and `proof-search-governance.md`.
- The packet's `WALL.md`, `ASSUMPTIONS.md` and `step0/PRIOR_ART.md`.
- HEAD: `C5_R2-4_report.md` and `C5_R2-4_referee.md`, K2a (`TEST_LOG.md:58-96`, `KILL_SHEET.md:75-83`), and the T22 kill.
- The opus overlap results R45/R46/R54/R59.
- `DEFERRED_DECISIONS.md` #4.

Paths below are relative to the chirality-grid worktree unless marked HEAD (the `toe-leverage-analysis` worktree).
**Labels:** proved / checked / suggested / reading / comparator (literature, not re-proved).

---

## 0. Plain summary

The usual escape from the mirror problem on a grid is a modified mirror symmetry (Ginsparg–Wilson, "overlap"). It works in 4D Euclidean lattice theory, and in 2D I reproduced it in a version that uses only one fermion mode per site. Its catch is range, and this report makes that catch exact.

**proved here, independent check owed:** the exact symmetry can never come from any finite nearest-neighbour rule. This holds even if every site carries finitely many extra hidden variables that are then averaged out. The obstruction is topological (a Chern class) and does not depend on how big each site's algebra is. So enlarging M₂(C) to M₄(C) does not touch it.

**checked numerically:** an exponentially good approximation from a finite rule is cheap. About 30 hidden variables per fermion field and site give a 10⁻³⁵ defect, in the free theory and in weak gauge fields.

In continuous ("flowing") time the free version of this family is closed outright: it collapses onto the interacting (symmetric mass generation) problem.

The constructive route left is a Euclidean one, Kikukawa's SO(10) 16 measure with strongly coupled mirrors. Its open lemma is locality, and it has a named numerical test.

---

## 1. Routes

| Route | Family (object, mechanism, terminal obligation) | Premise it drops or changes | What you would have to believe | First artifact | Cost | What it would change if it worked |
|---|---|---|---|---|---|---|
| **F2-R: rational obstruction (exact price)** | Free lattice Dirac operator D on Z⁴ = Z³×Z_τ with an exact GW relation. **Mechanism:** the chiral projector P̂ = (1−γ̂5)/2, with γ̂5 = γ5(1−2RD), is a Chern-class carrier. **Terminal:** Lemma R plus the index/degree identity. | A4 (finite range) and A2 (finite site algebra), read jointly. | That an exact chiral symmetry is required, as the Lüscher route needs. If it is, the law must contain a **non-rational** kernel. | `Lemma R` (§2, proved here) and runs T1 and T4b (checked) | Done in this run; an independent referee is owed (≈1 h) | It converts the owner's range question into an exact trichotomy (§5). It extends Horváth / R2-4-A2 from "ultralocal" to "any finite rule with finitely many gapped auxiliary fields per site". It shows M₄(C) is the wrong price for chirality in this family. |
| **F2-H: GW projection plus strongly coupled mirror (Kikukawa SO(10) 16)** | Overlap Weyl fields for one generation as the 16 of SO(10) ⊃ SM with ν_R. The mirror (R-projected) part is saturated by SO(10)-invariant 't Hooft vertices. **Mechanism:** the exact GW projection removes doublers, so there is no Golterman–Shamir 8-doubler endpoint, and the strong multi-fermion vertices give the mirror sector a symmetric gap. **Terminal:** locality and smoothness of the gauge-field dependence of the measure term (open, as the author states). | A5 (free) and A4 (range), on the hypercubic Euclidean regulator that the approved `kinetic_isotropy_primitive` already names. | (i) A non-rational kernel is acceptable (F2-R). (ii) Kikukawa's measure is local. (iii) A positive transfer matrix exists for the chirally gauged measure (open). | 2D analogue of the locality test (the Kikukawa 1⁴(−1)⁴ and 2 1 (−1)³ models), then the 4D 16 at weak gauge coupling | Days: 2D in about a day, 4D in about a week of compute | It would give the first framework-hosted, exactly gauge-invariant, mirror-free SM generation, Euclidean. The remaining obligations would be RP and the non-rational-kernel price. |
| **F2-T: continuous-time collapse** | A Hamiltonian on Z³ with a free single-particle symbol h(k) and a compact gauge charge Q, possibly not on-site. **Mechanism:** a Stokes / spectral-flow balance inside each charge sector. **Terminal:** in continuous time, F2 reduces to SMG, i.e. an interacting disentangler of an anomaly-free, not-on-site G. | A3 (Hamiltonian, continuous time), where the K2a selector lives | That the framework's time is continuous. Then the GW mechanism (separate projectors for ψ and ψ̄) has no Fock-space counterpart. | Dependency reduction (§4, proved for free carriers, plus comparators) | Done | Negative and decisive for planning: the GW family cannot be the continuous-time chirality source. Continuous time sends this family to the SMG agent; hypercubic Euclidean time is where F2 lives. |

---

## 2. Lemma R and Theorem F2-R (proved here, skeleton with every step named; independent check owed)

**Setting.** Translation-invariant free operators on ℓ²(Z^d)⊗Cⁿ. Their symbols are matrix functions of z = (e^{ik₁},…,e^{ik_d}) on the torus T^d.

**Lemma 0 (equivalence; elementary, proved).** Two descriptions of an effective operator are the same thing:
- (i) it is obtained from a finite-range operator with finitely many auxiliary components per site by Gaussian elimination of a sector whose block E(z) is invertible on T^d. This is a Schur complement A − B E⁻¹ C, i.e. "eliminate a gapped auxiliary sector".
- (ii) its symbol is a rational function of z, regular on T^d.

*Proof.* (i)⇒(ii): the entries of E⁻¹ are adj(E)/det E, and det E ≠ 0 on T^d. (ii)⇒(i): take N/g = 0 − N·(−g)⁻¹·1, with g a Laurent polynomial nonzero on T^d. ∎

**Lemma R (proved here).** Let P(z) be an idempotent matrix (Hermitian or not) whose entries are rational in z and regular on T^d. Then every Chern class of the complex vector bundle Im P → T^d vanishes. In particular every Chern number vanishes, in every d.

*Proof skeleton.*
1. Write P = N/g with N, g Laurent polynomials and g ≠ 0 on T^d. Then T^d ⊂ U := (C*)^d ∖ V(g).
2. T^d is Zariski-dense in (C*)^d, so P² = P holds in M_n(O(U)).
3. Im P is therefore a finitely generated projective O(U)-module, i.e. an algebraic vector bundle E on the smooth affine variety U. U is connected, so E has constant rank. E's fibre over z ∈ T^d is Im P(z).
4. The topological Chern classes are the cycle-class images of the algebraic ones: c_k(E^an) = cl(c_k(E)), with c_k(E) ∈ CH^k(U) (Fulton, *Intersection Theory*, ch. 19).
5. U is open in A^d, so CH^k(A^d) → CH^k(U) is surjective (localization). CH^k(A^d) = 0 for k ≥ 1 (homotopy invariance). Hence CH^k(U) = 0 and c_k(E^an) = 0 in H^{2k}(U;Z).
6. Restrict to T^d ⊂ U. ∎

**Comparators.**
- Read 2017 (arXiv:1608.04696) proves the polynomial (compactly supported) case through K₀ of the Laurent ring. Lemma R is the localized (rational) extension.
- Dubail–Read 2015 (arXiv:1307.7726): chiral Gaussian fermionic PEPS, whose Bloch data are rational, have gapless strictly local parent Hamiltonians.
- Wahl–Tu–Schuch–Cirac 2013: chiral GfPEPS exist but have power-law correlations, i.e. a rational projector singular on the torus.
- Mangolte (arXiv:math/0310325) lists torus → sphere as the exceptional case for density of regular maps. That is consistent with the d = 2 case of Lemma R: rational regular maps T² → S² have degree 0.

**Theorem F2-R (proved, modulo the index link in part (b)).** Let D be a free lattice Dirac operator on Z^d (d even), with symbol rational and regular on T^d. Suppose D satisfies an exact GW relation γ5D + Dγ5 = 2Dγ5RD, where R is rational and commutes with γ5. Then γ̂5 = γ5(1−2RD) satisfies γ̂5² = 1. (Checked algebraically: γ5 has to commute with R, R does not have to commute with D.) P̂ is rational and idempotent, so all its Chern classes vanish (Lemma R). Consequences:

- **(a) Exact, hypercubic scalar+vector class, canonical R (proved).** GW forces 2a = a² + b² for D = a + iγ·b. So ε := γ5(D−1) = n·Γ, with n = (a−1, b) ∈ S⁴ and five anticommuting Hermitian Γ's (γ5, iγ5γ_μ). The zeros of D are exactly n⁻¹(south pole), and each zero's local degree is its Nielsen–Ninomiya chirality. Hence **net chirality of the massless modes = ±deg n = ±C₂(P̂) = 0**. A rational exact-GW operator therefore always carries a doubler of opposite chirality. This is Horváth's 1998 no-go extended from ultralocal to rational.
- **(b) General rational R, any taste/flavour structure.** The GW index in a smooth background of charge Q is (sign)·C(P̂_free)·Q. That makes it 0 for rational D, so there is no anomaly and no single Weyl or Dirac species.
  - The link is a comparator (Lüscher 1998; Kikukawa–Yamada 1998; Adams 2002).
  - **checked in 2D (T1):** for overlap kernels, index = −c₁(free ε band)·n in 96/96 cases. This includes r = 0.6, where the Chern windows differ from the mass windows.

**Corollaries.**
1. **(proved, given Theorem F2-R)** Every exact lattice chirality of GW type needs a kernel that is **not** the Schur complement of any finite-range structure with finitely many gapped auxiliary fields per site. Examples: sign(H_W), equivalently the Fermi-sea projector of a gapped nearest-neighbour Hamiltonian, or a domain wall at L_s = ∞.
2. **(proved, given Theorem F2-R)** The obstruction does not depend on the fibre dimension n, so it is independent of the site algebra. **Enlarging M₂(C) to M₄(C) (DEFERRED_DECISIONS.md:121-146) does not remove it.**
   - **checked, T4b:** one fermion component per site (staggered, Adams kernel, the qubit-compatible carrier) already gives an exact-GW index of −n, 24/24 cases in 2D.
   - **reading:** this settles PRIOR_ART tension T2 (`step0/PRIOR_ART.md:275-281`) for this family. What a single qubit per site lacks is a non-rational kernel, not a chirality operator.
   - **comparator:** in 4D, Adams' kernel gives 2 tastes and Hoelbling's gives 1 but breaks hypercubic symmetry. Neither was checked here.
3. **(reading)** This sharpens R2-4's Π-QL (HEAD `C5_R2-4_report.md:296`, "nearest-neighbour → quasi-local, SUGGESTED"). For the GW family the true price is "nearest-neighbour → **non-finitely-generated** quasi-local". Exponential tails produced by finite hidden structure are not enough.

**Gap test.** L_R is the statement "exact GW with nonzero net chirality ⇒ non-rational kernel".
- **L_R ⇒ T?** No. It is a price lemma for one family.
- **T ⇒ L_R?** No; T could be met by SMG.
- **Strength vs target:** weaker (a family price).
- **Status:** candidate-complete as a price. The pending items are a referee pass on Lemma R and on step (b)'s link in 4D.

---

## 3. F2-H: the constructive Euclidean route

**Object.**
- Overlap D[U] on Z³×Z_τ. Lüscher's locality holds under the plaquette bound ‖1−U_p‖ < ε (comparator: Hernández–Jansen–Lüscher 1999).
- The chirally projected Weyl measure for one generation in the 16 of SO(10).
- The mirror R-projected field is saturated by SO(10)-invariant 't Hooft vertices (Kikukawa, PTEP 2019, arXiv:1710.11618).
- **comparator, from the abstract:** the measure is manifestly gauge-invariant in all topological sectors and the effective action is CP-invariant. **Locality of the measure's gauge-field dependence is open.** The author proposes a weak-coupling Monte Carlo test that has no sign problem.

**State of the non-abelian measure (comparators).**
- U(1): fully nonperturbative (Lüscher 1999).
- General non-abelian anomaly-free: proved to all orders of perturbation theory (Lüscher 2000).
- SU(2)×U(1) GWS: nonperturbative in every SU(2) topological sector, but only with vanishing U(1) magnetic flux (Kadoh–Kikukawa, arXiv:0709.3658).
- SU(3) is vector-like on SM content, so it is standard.
- 2D precedent: in the 345 model with Yukawa couplings, mirror decoupling failed (singular, non-local vertex). In the 1⁴(−1)⁴ model, strong quartic mirror vertices gave numerical evidence of locality. The construction extends to 2 1 (−1)³ (Kikukawa, arXiv:1710.11101).

**Dependency graph** (leaf : status):
- L1, exponential locality of D[U] : comparator, proved under the plaquette bound.
- L2, locality of the SO(10)/SM measure term in all sectors : **OPEN**, the terminal lemma.
- L3, real-time reconstruction of the chirally gauged complex-phase measure : **OPEN**. **Correction to the repo:** free overlap fermions ARE link-reflection-positive (comparator: Kikukawa–Usui, arXiv:1005.3751). HEAD `C5_R2-4_report.md:204`, "RP of overlap … not established", is out of date for the free case; the gauged chiral case is still open.
- L4, the non-rational-kernel price : proved necessary (F2-R).
- L5, the regulator : Z³×Z_τ hypercubic is the geometry the approved kinetic-isotropy primitive already names (`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:23-24`). Reading: no extra price for the time grain.
- L6, the plaquette bound as a hard nearest-neighbour support constraint : reading. It fits Admissibility's "support" reading (`MINIMAL_AXIOMS…:57-61`, reading note 3), but it needs the finite-range-cliques reading Π-FR, which R2-4 A6 already showed any lattice gauge action needs.

**Gap test.**
- L2 + L3 + the L4 price ⇒ T in its Euclidean-with-RP form. L2 alone does not imply T.
- **Strength:** comparable. L2 is a property of a fully specified object, testable by a finite computation, so it is not the wall restated.
- **Status:** active.
- **Kill check against prior art:** it is not the repo's SPIN10 slab (`docs/SPIN10_…:195-221`). That one projected ultralocally and got the 8-doubler Golterman–Shamir endpoint; here the projection is exact GW, so there are no doublers to restore. Golterman–Shamir's later propagator-zero objections (T22 kill) are not answered here.

---

## 4. F2-T: continuous time (dependency reduction)

**Lemma H (proved for free carriers; this is the content of Nielsen–Ninomiya 1981, Hamiltonian form, comparator).** Hypotheses:
- h(k) is a continuous Hermitian symbol on T³ (any range short of discontinuous);
- Q has a continuous single-particle symbol q(k) with integer spectrum, [q, h] = 0, number-conserving or Bogoliubov–de Gennes.

Then every charge sector is chirality-balanced. *Proof:* the occupied sub-bundle of the q = c eigenbundle is defined on T³ minus small balls around the nodes; the boundary of a compact 3-manifold is null-homologous, so the Berry monopole charges sum to zero (Stokes). The 1+1D version is zero spectral flow around S¹. ∎

So no free continuous-time construction, of GW type or otherwise, puts a compact chiral gauge charge on a single hand. The GW trick uses different projectors for ψ and ψ̄, and that has no Fock-space counterpart.

**Comparators that close the escapes.**
- Gioia–Thorngren (arXiv:2503.07708) realize a single Weyl fermion's chiral symmetry on a 3+1D cubic Hamiltonian lattice. The symmetry is not on-site and is **non-compact**, so it cannot be the compact U(1)_Y.
- Fidkowski–Xu (arXiv:2306.10105): the compact chiral U(1) of a single Weyl fermion cannot be implemented by a locality-preserving unitary on finite-dimensional sites.
- What remains for an anomaly-free compact G is to disentangle the not-on-site action into an on-site one, using ancillas, by an interacting map. That is SMG.

**Gap test.** The continuous-time terminal obligation equals the SMG family's terminal obligation. It is **blocked-equivalent** and is handed to that family.

**Open lemma, registered not attempted (L-tick).** Does every *rational* unitary tick on T³ have W3 = 0?
- It would extend LATTICE_HANDEDNESS T2 (polynomial, SK₁ = 0) to "finite tick with finitely many internal feedback channels".
- The K₀ argument of Lemma R does not transfer directly: W3 is a K₁ invariant, and higher Chow groups of U need not vanish.

---

## 5. Price in framework terms (F2-R makes this exact)

Exact GW chirality needs exactly one of three mathematically equivalent non-rational objects. Each costs a different premise:

| Option | Object | Premise it costs | Text |
|---|---|---|---|
| (a) | A non-finitely-generated quasi-local kernel (sign function) | Admissibility's "one fixed nearest-neighbor rule" | `MINIMAL_AXIOMS…:57` |
| (b) | Infinitely many auxiliary fields per site (domain wall at L_s = ∞, an unbounded fifth coordinate) | Lattice (Z³ only) or Qubit (finite one-site algebra) | `:37-41`, `:47` |
| (c) | The vacuum (ground-state projector) of an auxiliary gapped nearest-neighbour Hamiltonian (the Narayanan–Neuberger overlap of Fock vacua) | "A law privileges no states" (`:94`), and the realized-state primitive's "no state-selection rule" (`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md:37-38, :60`) | — |

**Approximate alternative (finite rule).**
- Use n poles, i.e. about 2n auxiliary Dirac fields per physical field and site (continued-fraction form). This gives a GW defect δ ≈ 4e^{−2πnK(k)/K(k′)}.
- **Exact chirality is lost.** Lüscher's projector does not exist at finite n, so gauge invariance holds only to order δ. In practice this is the domain-wall/extra-coordinate family with a finite fifth coordinate.
- **Requirement (suggested, order of magnitude).** Gauge-variant terms induce gauge-boson masses of order (g²/16π²)δΛ², with Λ = M_Pl (scale-reference primitive). With U(1)_em kept exact, ρ-parameter precision needs δ ≲ 1e-35. Otherwise the photon-mass bound (m_γ < 1e-18 eV) needs δ ≲ 1e-88.

---

## 6. Tests run (all pre-registered in `PREREG.md` before running)

| Test | What | Result | Label |
|---|---|---|---|
| T1 | 2D overlap index in uniform U(1) flux n = 1,2,3; L = 8, 10; r = 1 and 0.6; 8 masses. Compared with FHS c₁ of the free ε band. | **PASS**: index = −c₁·n in 96/96 cases, integer exactly, one global sign. At r = 0.6, m = 1.5 gives c₁ = −1, and m ≥ 2.5 gives c₁ = 0 with index 0, so the index tracks the Chern number, not the mass window. | checked (`t1_index_vs_chern_2d.out`) |
| T3 / T3b / T3c | Free 4D kernel, M ∈ {0.5, 1, 1.5}: Shamir closed form, and Zolotarev computed directly at 130 digits | **PASS** (pre-registered ≤ 100 at δ = 1e-35). Zolotarev: rate 2.4–3.0 per pole. At M = 1, n = 28 gives 1e-36.1 and n = 70 gives 1e-90.2, both computed directly, with no extrapolation. Shamir (exact formula): N = 118 for 1e-35 and 294 for 1e-88, at M = 1. | checked (`t3b…out`, `t3c…out`). **Correction:** `t3…out`'s Zolotarev column is wrong (K and K′ swapped); its Shamir column is right. The first t3b run used the wrong x-scale and is kept as `…_WRONGSCALE.out`. |
| T4 | 2D staggered Adams overlap, first operator | **FAIL** as registered. The candidate list lacked a factor i, so the accepted Γ55 did not commute with D_st (norm 4) and the kernel was ungapped. | checked; verdict stands |
| T4b | Corrected operator: phase i, η5 = (−1)^{x₁}, [Γ55, D_st] = 0 exactly in the free theory | **PASS**: index = −n, 24/24 cases (m ∈ {0.3, 0.6, 1.0, 1.4}, L ∈ {8, 12}, n ∈ {1, 2, 3}), gaps ≥ 0.15 | checked (`t4b…out`) |
| T5 | U(1) background on 6⁴ | **ABORTED**: 564 MB resident, over the machine limit; killed with no result | — |
| T5b | Gaussian weak-coupling U(1) backgrounds, 4⁴, g ∈ {0.5, 0.65}, 12 configurations each | **PASS** (registered ≥ 0.3). min\|H_W\| = 0.80 at g = 0.5 and 0.74 at g = 0.65, so κ ≥ 0.107. Direct Zolotarev at κ = 0.1067: n = 30 gives 1e-35.5 and n = 76 gives 1e-90. The proxy is tiny: abelian only, not an equilibrium ensemble. | checked |

**Effect on the wall.**
- **Moved, toward an exact price.** F2's exact form is now equivalent to a named premise choice, (a), (b) or (c). Its approximate form is a counted matter-per-site price of about 60 auxiliary Dirac fields per physical field and site, free or weak coupling, at δ = 1e-35.
- **Not moved:** the non-abelian measure's locality (L2) and real-time reconstruction (L3).
- **Owed:** no other-vendor referee has checked Lemma R, T1–T5b, or the readings drawn from them.

---

## 7. Cheapest decisive test per route (pre-registrable readings)

**F2-R.** An other-vendor referee (codex sol) checks Lemma R steps 1–6 and part (a) of the theorem.
- **PASS:** no gap. The exact-GW price is fixed at {(a), (b), (c)} and becomes an owner decision.
- **FAIL:** a gap in step 4/5 (for example, Chern classes not cycle classes on U) or in density. The rational class then reopens, and the next test is a search for a degree-1 rational regular map T² → S², which by the Mangolte comparator should find none.
- **Cost:** about 1 hour.

**F2-H.** 2D test first, using the anomaly-free 2 1 (−1)³ model with GW-projected Weyl fields and strong quartic mirror vertices:
- weak-coupling Monte Carlo of the mirror sector's gauge vacuum polarization Π_μν(p);
- L ∈ {8, 12, 16};
- **PASS:** Π_μν is analytic at p → 0 within errors, with no 1/p or log p singular non-local term, and is L-independent.
- **FAIL:** a singular non-local term like the one in the 345 model.

The 4D 16 run follows only after a 2D PASS. Cost: about a day for 2D, about a week for 4D. Waiting on the owner (budget) and the probe queue.

**F2-T.** No test. It is blocked-equivalent to SMG and handed to the SMG agent.

---

## 8. What not to do next

- **Do not adopt M₄(C) "for chirality".** In this family it buys a chirality operator, which staggered blocks already provide (T4b), not net chirality (Lemma R).
- **Do not search for ultralocal or "short-tail" GW operators** with finite hidden structure. Lemma R excludes all of them.
- **Do not plan a continuous-time GW construction.** Lemma H and the comparators close it; the work belongs to SMG.

---

## 9. Limits and flags

- Lemma R is a family price, not a no-go on the wall: interactions (SMG) are untouched.
- Part (b)'s link from the index to the Chern number in 4D for general R is a comparator. It is checked only in 2D.
- T5b is a tiny abelian proxy.
- The δ targets are suggested orders of magnitude.
- All literature items are from abstracts or recall: comparators, not re-proved. I did not verify Poppitz–Shang's 2D mirror-decoupling failure; it is recalled only.
- Every run is same-family, and no other-vendor referee has seen these results.
