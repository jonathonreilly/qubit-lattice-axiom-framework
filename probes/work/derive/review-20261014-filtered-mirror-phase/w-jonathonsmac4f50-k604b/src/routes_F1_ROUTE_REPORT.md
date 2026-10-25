# F1 route report: interaction-driven gapping of the mirror sector

- **Agent:** Claude Opus 5.5 route agent. This is the same model family as the supervisor and the other route agents, so it is not an independent referee.
- **Window:** 2026-10-14, 13:19Z to about 13:55Z.
- **Hygiene:** no repository was edited. The only files are in this folder. Each script ran under OMP_NUM_THREADS=2, one at a time, with peak resident memory of 39 MB or less. Nothing is still running.

**Refresher surfaces read:**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (233 lines).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, including its generated baseline for the scale-reference and kinetic-isotropy primitives.
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`, lines 1-45.
- Exercise SKILL steps 4 and 6, and `proof-search-governance.md`.
- The packet's `WALL.md`, `ASSUMPTIONS.md` and `step0/PRIOR_ART.md`, plus cluster C.

**Primary surfaces re-read at the cited lines:**
- `docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md`, in full.
- On the HEAD branch: `candidate-law-20261008/TEST_LOG.md:58-96`, `KILL_SHEET.md:75-83`, and `checks/k2a_selector_momentum_space.py`.
- `gravity-current-state-20261009/TESTS.md:9611-9700`, covering the TW-1/2/3 pre-registrations and the worker readings.
- `agents/C5_TW3_report.md`, at the cited lines.

**Labels used below:**
- **proved:** an argument complete here.
- **checked:** a finite computation in this folder.
- **suggested:** an argument that has not been checked.
- **reading:** an interpretation.
- **comparator:** literature.

---

## 0. The family in one paragraph, and what the prior art already fixes

**The family.** The mirror partners are not removed. Interactions gap them without any fermion bilinear, while the wanted handed modes stay gapless.

**The prior-art endpoint.** The repo's Spin(10) slab note covers the strong-coupling limit. There, freezing the mirror slots restores 8 corner Weyl nodes, 4+4 (`SPIN10…:195-221`), a fixed-volume Feshbach statement (`:225-243`). The note itself says an intermediate phase can evade this (`:241-242`, N7 `:454-461`).

**K2a.** In continuous time, the body-diagonal shift T₁T₂T₃ equals Weyl chirality on the zero modes. K2a calls the coupling "PASS-weak" with no gap shown. Hypercubic time has no selector (`TEST_LOG.md:58-96`).

**TW-3, today, on the HEAD branch.**
- Onsite symmetric gapping needs 4 staggered fields, i.e. 16 Weyl.
- An onsite translation-invariant interaction cannot select the twins, so any selective law must be spread over the 2³ cube (P-TW3a; `C5_TW3_report.md:31,34,204,269`).

**Literature.** Golterman–Shamir's generalized no-go (arXiv:2505.20436, §III; proceedings arXiv:2603.15985) has three conditions:
- (1) a finite-range Hamiltonian;
- (2) a free massless continuum limit;
- (3) a complete set of interpolating fields with no zeros.

If all three hold, the massless spectrum is vector-like. GS argue that (2) holds automatically in 4D, because four-fermion terms are irrelevant there, and they conjecture that bound states make (3) hold in any local SMG phase. So in 4D the whole family lives or dies on (3).

**What F1 adds:**
- a mod-16 table on the framework's own carriers (C1);
- a locator for where the Golterman–Shamir (GS) picture puts the extra light states on the repo's slab (C2);
- three routes that reduce the terminal obligation to one sharp, testable question.

---

## 1. Checks run

### C1. Emanant Z16 indices of lattice translations on the native carriers (checked)

Pre-registration: `PREREG_C1.md`, 13:39Z. Script and output: `scripts/c1_emanant_z16.py` and `.out`.

**Method.** On the IR zero modes, take each lattice translation g. If g² = (−1)^F, it is directly a Spin-Z4 generator. If g² = +1, it becomes one after multiplying by i^F, which needs fermion number to be conserved mod 4. For each such generator I computed the Dai–Freed index ν_g = Σ q over the left-handed Weyl fermions, mod 16 (comparator: García-Etxebarria–Montero, arXiv:1808.00009, where Ω₅^{Spin×_{Z₂}Z₄} = Z₁₆).

**Results:**

| Carrier / sector | Nonzero ν_g per internal component | Symmetric gapping allowed for internal multiplicity d = |
|---|---|---|
| Staggered field, whole (control) | ν = −4 for g = T₁T₂T₃, which squares to −1 and **needs only (−1)^F** | 4, 8, 16 (not 1, 2 or 15) |
| Staggered K2a mirror (one chirality at K = 0) | ν = −2 (from T₁T₂T₃, needs only (−1)^F); ν = ∓2 (from i^F) | 8, 16 (not 1, 2, 4 or 15) |
| Walker H = Σσ_a sin p_a, whole | ν = −8 for T₍₁₁₁₎·i^F (needs Z4^F) | 2, 4, 8, 16 |
| Walker, "three generations" split (light = hw1, mirror = {hw0, hw2, hw3}) | (−3, −1, −1, +1, −1, +1, +1, −5) over the 8 elements of Z₂³·i^F | **16 only** (not 8 or 15) |
| Walker chirality split, mirror {hw0, hw2} | ν = −4 (for i^F and for T₍₁₁₁₎·i^F) | 4, 8, 16 |

**Other exact facts (checked):**
- T_μ² = +1 on the zero modes.
- The T_μ pairwise anticommute, and each commutes with the chirality and with H(k).
- T₁T₂T₃ squares to −1. It is a Spin-Z4 generator by itself.

**Pre-registered reading: COUNT-16 (checked, with the control passing).**
- **The control passes.** The whole staggered carrier gives |ν| = 4 per field, which reproduces the "multiples of four staggered fields" count of Catterall–Pradhan(–Samlodia), arXiv:2501.10862, and TW-3 (`C5_TW3_report.md:31,203-205`).
- **d = 16 passes and d = 15 fails.** Every candidate mirror sector has all ν_g ≡ 0 at d = 16, and at least one is nonzero at d = 15.

**Readings:**
- **The anomaly gate is passable, and it forces ν_R.** On the staggered carrier this follows from lattice translations plus fermion parity alone, because the body-diagonal shift squares to (−1)^F. No B−L-type Z₄ has to be imposed (proved for the stated symmetry, given the comparator classification). On the walker, the same conclusion needs fermion number conserved mod 4. That matches K2a's "record count conserved only mod 4" (`TEST_LOG.md:80`).
- **The "16 vs 8" tension.** A whole walker field is half a Z16 unit (ν = 8), and a whole staggered field is a quarter (ν = 4). What a mirror route must pass is the split count. With the 16 placed on-site, every split I tested passes.
- **Scope.** These are necessary conditions only: one cyclic subgroup at a time, with no mixed time-reversal or Spin(10) anomalies. A pass does not show that a gapped phase exists.

### C2. Where the Golterman–Shamir bound-state picture puts the extra light states on the repo's slab (checked)

Pre-registration: `PREREG_C2.md`, 13:43Z. Script and output: `scripts/c2_gs_reduced_locator.py` and `.out`.

**Model.** The slab h_L(k) of `SPIN10…:168-186`, with L = 2 and 3 and b(0) = 0. A local composite χ on the mirror layer pairs with B_L, with Δ = 0.3, 1 and 3, in two classes:
- (a) χ is a bare lattice Weyl;
- (b) χ has its own Wilson partner χ′.

Zero points were found on a 16³ grid plus all corners, and their chirality was taken from the Chern number on a small sphere.

**Results (pre-registered readings GS-a and GS-b both CONFIRMED; no anomaly).**
- **Class (a).** The k = 0 mirror is gapped. The light mode A₁ (chirality +1) survives. New zero modes appear at all 7 nonzero corners (−1, −1, −1, +1, +1, +1, −1), net −1, so the spectrum is vector-like.
  - At Δ = 0.3 they are about 97% χ: composites.
  - At Δ = 3 their weight moves to the far A layers (A₂ 0.59 at the hw1 corners).
  - So the SPIN10 strong-coupling doublers are the large-Δ end of the same branch (checked within the class).
- **Class (b).** The corners stay gapped. At k = 0 there is one zero mode of each chirality: A₁ and χ′ in equal weight. χ′ is a massless composite with the mirror's chirality, which is exactly the Eichten–Preskill failure.

**Reading.** Within any free reduced model this is forced by Nielsen–Ninomiya, so C2 is evidence neither for nor against GS. Its use is that it gives the decisive many-body test two concrete signatures to look for:
- **(a)** gapless far-boundary or composite modes at the nonzero corners;
- **(b)** a gapless mirror-chirality mode at k = 0 in the composite channel χ′ ~ A^c B B.

**Selection rule on the native carrier (proved, by momentum conservation).** On the native carrier the mirror is selected by momentum (route R1 below). Exact translations then forbid every low-energy light·mirror³ and light³·mirror coupling, because their total momentum is Q ≠ 0. They do **not** forbid the 2+2 operator A A B B, and that operator is precisely the channel for composite (b). So translations block only half of the classic failure. The other half is a dynamical question.

---

## 2. Routes

| Route | Family (object, mechanism, terminal obligation) | Premise dropped or changed | What you would have to believe | First artifact | Cost | What it would change if it worked |
|---|---|---|---|---|---|---|
| **R1: native-carrier, momentum-selected mirror SMG** | **Object:** the 3D Hamiltonian staggered field (K2a), or the walker, × an on-site Spin(10) 16, in **continuous time**. **Mechanism:** the mirror is the translation-emanant sector (staggered: the χ = +1 eigenspace of the T₁T₂T₃ selector; walker: the nodes {hw0, hw2, hw3}, with hw1 as three light generations). It is gapped by a translation- and rotation-covariant **filtered** Spin(10)-singlet quartic built on ψ_S = Fψ, with F a finite stencil that vanishes at the light nodes. The quartic is non-onsite, as TW-3 requires. **Terminal:** a finite-coupling phase with the mirror gapped, the light 16_L gapless, and neither signature (a) nor (b). | A5 (free carrier) → interacting. A2/T6 → 16 (staggered) or 32 (walker) complex modes per site. A9: continuous time is required, since there is no selector in Z⁴. | GS condition (3) fails here: the propagator zeros of the complete interpolating set cannot be removed. Equivalently, the SMG bound state does not form a light Dirac partner (signature (b)), and no composite branch reaches the corners (signature (a)). | C1, C2 and the selection rule (done). Next: write F explicitly (for the walker, f(p) = 1 − Σ_μ sin²(p_μ/2)Π_{ν≠μ}cos²(p_ν/2) is a trigonometric polynomial, so F has finite range), and pre-register the many-body test below. | Construction: hours. Decisive test: cluster-weeks. | One generation per light node: chiral 16s with exact on-site Spin(10), so the SM subgroup is gauged by ordinary links, with no doublers. On the walker, the hw1 triplet would be three handed generations. That would turn the hw1 "generation" reading (T4) into a selector-backed one. |
| **R2: the payload slab (Wang–Wen slab compiled into on-site matter)** | **Object:** a Wilson/DW slab of width L, with the layer index and the A/B orbital as **on-site** payload. Per site: M₂(C)_spin ⊗ M₂(C)_orbital ⊗ C^L ⊗ 16 = 64L complex modes. Time is continuous (Hamiltonian), or hypercubic Euclidean via DW fermions. **Mechanism:** a Spin(10) quartic on the far-layer B_L modes at **finite** coupling, not freezing. The mirror projector is on-site and exact, which TW-3's no-go does not cover. **Terminal:** as R1, on the far boundary. | "No extra dimension" is **not** load-bearing: a finite slab is a Z³ lattice with payload (proved: the layer hopping is on-site in 3D). A2 → at least M₄(C) per site, the parked DEFERRED #4 shape, plus layers and the 16. The Wilson mass needs the orbital doubling, because the native scalar hop of block 77 only shifts levels. | Wang–Wen's boundary SMG holds for a 16 at finite coupling, in a window where the SMG gap Δ is below the far-layer Wilson pairing at the corners but nonzero at k = 0. C2 shows that once that ordering is violated (Δ ≫ Wilson), you are on the SPIN10 doubler branch. | Done here: the slab locator C2 (signatures). Next: the minimal toy content of 16 Weyl with Spin-Z4, so that the d = 16 gate passes at the smallest payload. | Decisive test: cluster-weeks, the same class as R1. Araki–Fukaya–Onogi–Yamaguchi (arXiv:2608.29963) report HMC with phase reweighting working for 2D DW mirror SMG. | Same as R1, plus a hypercubic-time version (which the kinetic-isotropy primitive favours). The price moves from "extra dimension" to "matter per site". |
| **R3: the bulk-path reduction (disentangler)** | **Object:** the slab **bulk** ground state, as a 4+1D invertible fermionic phase with Spin(10) or Spin-Z4 symmetry. **Mechanism:** if the free bulk can be joined to a product state by a symmetric gapped path (P), automorphic equivalence (Hastings–Wen; Bachmann–Michalakis–Nachtergaele–Sims) gives a symmetric quasi-local unitary U. Then H_far = U†(Σ onsite singlet projectors)U, applied in a strip at the far boundary, gaps the mirror **exactly**, with no strong-coupling dynamics. **Terminal: P.** | A4 (finite range) → quasi-local tails. A5 → interacting, but only through U. | Lattice invertible phases are classified by cobordism, as a statement about paths: 16 Weyl ≡ 0 in Z₁₆, so the class is trivial. | Proof skeleton (below). Literature check: does an explicit symmetric circuit or commuting-projector model exist for this 4+1D class? | Days (literature and proof). A numerical check of P in 4+1D would cost more than R1/R2. | An explicit, exactly gapped mirror. Corollary (suggested): if GS's conjecture holds in 4D, P fails, so there would be a lattice invertible phase beyond cobordism. That puts GS in direct conflict with the classification, and makes the dispute decidable mathematically, not only numerically. |

### R3 proof skeleton (suggested; open steps named)

1. **[open: P]** The free slab bulk, as a gapped Spin(10)-symmetric local fermion Hamiltonian, is joined to an on-site product state by a continuous symmetric gapped path.
2. **[standard; needs the symmetric, fermionic, quasi-local version cited exactly]** Automorphic equivalence then gives a symmetric quasi-local unitary U with U|bulk⟩ = |product⟩.
3. **[open: the strip lemma]** Restricting U to a strip of width w near the far boundary gives a quasi-local symmetric unitary that disentangles the far region up to e^{−w/ξ} errors, and leaves the near boundary's 16_L intact.
4. H_far is then gapped and symmetric, with no bilinear mass, since Spin(10) has none for a 16. The near 16_L stays gapless, because it has no symmetric relevant deformation. Hence there is a chiral spectrum. **[open: control of the gapless near boundary under the strip errors]**
5. **Corollary.** Truncating the tails gives a finite-range model in the same phase. GS condition (3) must fail for it, so the GS conjecture implies ¬P.

---

## 3. Theorem-strength gap tests

- **R1 and R2 terminal lemma L.** Statement: "There is a finite-coupling symmetric phase with a gapped mirror, a gapless 16_L at the light nodes, and no other gapless states."
  - L ⇒ T for the chirality clause of one generation, with SM ⊂ Spin(10) on-site and exactly gauge-invariant. Three generations come from three copies, or from the walker's hw1. The hierarchy (K6) is not addressed.
  - T ⇏ L, because other families could pass T.
  - So **L is stronger than the target's chirality clause: blocked-equivalent under the governance rule.** The new mechanism offered is the momentum selection rule plus the two signatures. That narrows the open step from "SMG works" to the single statement "GS condition (3) fails here". That is a sharpening, not a reopening.
- **R3 terminal P.** P ⇒ L (via steps 2–4), and T ⇏ P. **P is stronger than T: blocked-equivalent.**
  - **Reopen condition:** P proved for the 16-Weyl Spin-Z4 or Spin(10) class in 4+1D, or an explicit symmetric disentangler found.
  - **What it changes:** it moves the obligation from a boundary many-body spectrum to a bulk classification statement. That is a different obligation map.
- **Family equivalence (suggested; corollary of GS §III plus C2).** For models that pass the C1 gate, the whole F1 family is equivalent to the failure of GS condition (3) in a 4D symmetric phase. **The exact price of F1 is therefore that one statement.** If GS's bound-state conjecture is true, F1 is closed on every lattice with finite range (and, by smoothness, very likely with quasi-local range too), and the wall moves to the non-onsite-symmetry families (GW/overlap; Gioia–Thorngren, arXiv:2503.07708).

## 4. Prices in framework terms

| Price | R1 | R2 | R3 |
|---|---|---|---|
| Interactions | yes | yes | yes |
| Fermion statistics (A7) | yes | yes | yes |
| On-site internal Spin(10), or Spin-Z4 for the toy | yes | yes | yes |
| ν_R in every generation | forced (checked, C1) | forced | forced |
| Time | continuous (Hamiltonian) only | Hamiltonian or Euclidean DW | Hamiltonian or Euclidean DW |
| Payload per site | 16 (staggered) or 32 (walker) complex modes. This strains "one record per site" (T6) and fires the payload/M₄(C) owner question (DEFERRED #4 at `docs/repo/DEFERRED_DECISIONS.md:121-146`) | 64L complex modes | as R2 |
| Fermion number | must be conserved mod 4 (walker); the staggered carrier needs only (−1)^F | — | — |
| Range | — | — | quasi-local tails (the owner's range question, A3/A4) |

The mirror gap sits at the lattice scale, M_Pl-ish under the scale-reference primitive (reading). The TeV bound on mirror masses therefore needs no tuning (reading).

## 5. The single cheapest decisive test (pre-registrable; not runnable in this budget)

**MIRROR-SMG-4D.**
- **Setup.** 4D Euclidean domain-wall fermions with L_s = 2–4, or the R2 Hamiltonian slab at L = 2. The content is 16 Weyl with Spin-Z4, so the C1 gate passes at minimal payload. A Spin-Z4-symmetric quartic (or its auxiliary-field form) sits on the mirror wall only, with Wilson r = 1.
- **Method.** HMC with Pfaffian-phase reweighting, the method of Araki–Fukaya–Onogi–Yamaguchi, arXiv:2608.29963, carried from 2D to 4D. Volumes 8⁴ to 12⁴. A scan of the coupling G.
- **Measured:**
  - (i) the mirror-wall gap;
  - (ii) the physical-wall Weyl pole at k = 0;
  - (iii) signature (a): low modes at the nonzero corners in the far-wall elementary channel and the composite B³ channel;
  - (iv) signature (b): a low mode with mirror chirality at k = 0 in the composite χ′ ~ A^c B B channel.
- **PASS:** over a coupling window, (i) is open and (ii) is massless, with (iii) and (iv) gapped. All of this must hold with no symmetry-breaking order parameter and survive the finite-size trend across three volumes.
- **FAIL:** wherever (i) is open, (iii) or (iv) closes. Or (i) opens only together with symmetry breaking.
- **OPEN:** otherwise.
- **Cost:** cluster-weeks. The cheaper versions are not decisive, for these reasons:
  - 2D tests fail GS condition (2) (GS §V), so they do not decide the 4D question;
  - free reduced models obey Nielsen–Ninomiya by construction (C2);
  - the strong-coupling series reaches only the SPIN10 branch.
- **Waiting on:** owner approval of compute, or a collaborator group (Fukaya/Onogi, Catterall, Hasenfratz).

## 6. What not to do

- **Do not try "freeze the mirror, then SMG the 7 corner doublers".** (proved by counting, via C2) The corner set is itself net-chiral, with chiralities −1, −1, −1, +1, +1, +1, −1, net −1. This just moves the mirror to the corners, and the same GS question returns.
- **Do not take a 1+1D or 0+1D SMG success as evidence for 4D.** (comparator: GS §V; Araki et al. is 2D)
- **Do not gap the twins with onsite interactions.** (TW-3, proved there) In R1 the K2a chirality split commutes with every single shift (checked, C1), so a chirality-selective law can keep all translations. It must still be non-onsite.
- **Do not run R1 in hypercubic time.** The spatial body-diagonal translation does not see the time doubler's chirality flip (reading, consistent with K2a's Z⁴ check).

## 7. Files

All paths are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/routes/F1/`:
- `PREREG_C1.md` and `PREREG_C2.md`, each written before its run;
- `scripts/c1_emanant_z16.py` and `scripts/c1_emanant_z16.out`;
- `scripts/c2_gs_reduced_locator.py` and `scripts/c2_gs_reduced_locator.out`;
- this file.

## Sources

- Golterman & Shamir, "Constraints on the symmetric mass generation paradigm for lattice chiral gauge theories", arXiv:2505.20436v3 (§II, §III, §V); proceedings arXiv:2603.15985; earlier, arXiv:2311.12790. https://arxiv.org/html/2505.20436v3
- Catterall, Pradhan (and Samlodia), "Symmetries and Anomalies of Hamiltonian Staggered Fermions", arXiv:2501.10862 (PRD 2026, doi:10.1103/fk62-x1k3). https://arxiv.org/abs/2501.10862v2
- Gioia & Thorngren, "Exact Chiral Symmetries of 3+1D Hamiltonian Lattice Fermions", arXiv:2503.07708. https://arxiv.org/html/2503.07708v3
- Araki, Fukaya, Onogi & Yamaguchi, "Symmetric Mass Generation for Domain-Wall Fermions", arXiv:2608.29963. https://arxiv.org/abs/2608.29963
- García-Etxebarria & Montero, arXiv:1808.00009 (the Z₁₆ classification; recalled, not re-fetched).
- Wang & Wen, arXiv:1809.11171 (as cited in `SPIN10…:474-479`).
