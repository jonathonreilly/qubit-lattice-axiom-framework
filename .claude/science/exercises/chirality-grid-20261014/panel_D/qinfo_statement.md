# Panel D, quantum-information / condensed-matter lens: statement (2026-10-14, 20:47–21:05Z)

**Provenance.** Claude Opus 5.5, one panelist. I am the same model family as the supervisor and every exercise agent, so I am not independent of them, and nothing here is refereed. I read the following:
- the dossier;
- the axioms, in full;
- on `origin/claude/chirality-grid-exercise-20261014`: SUMMARY, ROUTES, WALL, ASSUMPTIONS, OUTSIDE_VIEW and TESTS in full, plus the X1, X2 and F2 reports in full and the X3, F4 and K3 sections cited below;
- `DEFERRED_DECISIONS.md:121-146`;
- gravity SUMMARY §26–27, TESTS (R19-28, R19-33, TW-1/2/3) and panel_F SYNTHESIS.

I ran one script: `scripts/site_budget.py`, which is pure arithmetic, with its output in `.out`. When I wrote this, none of the NT-1/2/3 reports existed. Only the PREREG files had been written.

**Path keys.**
- `CH:` = `origin/claude/chirality-grid-exercise-20261014:.claude/science/exercises/chirality-grid-20261014/`
- `GR:` = `.claude/science/exercises/gravity-current-state-20261009/`
- `AX:` = `docs/MINIMAL_AXIOMS_2026-06-29.md`

---

## Plain words first

1. **No experiment can see how many qubits sit at a grid point.** A "site" holding 32 qubits and a block of 32 one-qubit sites are the same mathematical object. What differs is bookkeeping:
   - which unit the translations move;
   - what counts as "nearest neighbour".

   So D1 and D2 are choices about how to write the law. Neither can be settled by observation.

2. **D1 is forced by the Standard Model's charges, not by handedness.**
   - Colour (three values) and weak isospin (two) cannot live on a site that holds one fermion mode. A one-mode site can carry only a phase-type charge.
   - With exact on-site gauge invariance and the lattice's translation symmetry, every site must hold at least 16 fermion modes (15 without ν_R). This holds whether or not the theory is handed.
   - Handedness only sets how much more than 16 is needed:
     - 32 for the corner package X2;
     - about 10³ for the slab;
     - about 10⁴ for a finite approximation of the overlap;
     - infinitely many for the exact overlap in real time.
   - So option (c), "refuse both", would give up colour and the weak force, not just handedness. And option (a), "one qubit per site, read as blocks", cannot keep the axiom's one-step translation symmetry. It moves the price onto the Lattice axiom instead of removing it.

3. **Range and site size trade against each other.**
   - Any rule that reaches a finite distance becomes a nearest-neighbour rule if you group sites into bigger blocks.
   - The one thing grouping cannot fix is a rule that needs infinitely many terms. That is Lemma R's class, the exact overlap.
   - So D2 really asks one thing: **will you ever accept an infinite register per point?**
     - If no, D2 is settled. Handedness then rests on symmetric mass generation (SMG) whichever way time is chosen.
     - If yes, it only helps with Euclidean time (set B), and only if the reflection-positivity tests (NT-1/NT-2) come back clean.

4. **My recommendations.**
   - **D1: a finite register per site,** stated once for the whole framework. It already covers the gravity root's ~90 modes.
   - **D2: no exact infinite-term kernel in the law.** Finite approximations are allowed, as a counted price.
   - **D3: do not choose time on handedness grounds.** Once D2 is "no", handedness does not favour B. Decide on gravity and on reflection positivity after NT-1/NT-2. My lean is continuous time (C) unless B's real-time reconstruction survives.
   - **D4: collaborators, and record the prices now.** Do not spend weeks of quantum Monte Carlo (QMC) on this machine. Add the condensed-matter QMC groups to the list.

---

## 1. Per decision

### D1. Matter per site

**Recommendation: (b) in substance, phrased in qubits.** The wording would be: "each site holds a fixed register of N fermion modes (qubits with fermionic grading), with N ≥ 16 set by the matter content." This keeps Z³, unit translations and nearest-neighbour adjacency as written. The parked M₄(C) "for γ5" motivation stays dead (Lemma R; `CH:ROUTES.md:74`).

**Reasons.**

1. **The floor (proved, elementary representation theory; this re-derives T25's MATTER-COUNT price, `CH:kills/K3/KILL_REPORT.md:184`).**
   - *Premises:*
     - each site's fermion modes span a space V_x (CAR algebra, graded tensor product);
     - gauge transformations act on site x through a unitary representation ρ_x of G on V_x (link-variable gauge theory);
     - the law is covariant under unit translations (AX:57-58), so ρ_{x+e} ≅ ρ_x∘φ for some automorphism φ of G;
     - one SM generation is present.
   - *Argument:*
     - The images of each multiplet under automorphisms of G_SM keep their dimension.
     - A multiplet present at any site has an image at every site.
     - So dim V_x ≥ 6 + 3 + 3 + 2 + 1 (+1) = 15 (16).
     - In particular, a one-mode site (CAR(1) ≅ M₂(C), AX:47) carries only abelian charge, because SU(3) and SU(2) have no nontrivial 1-dim representations.
     - The spinor and generation labels can be spread over neighbouring sites, as staggered fermions do. Gauge labels cannot.
   - This is why the KS/staggered count is 16 (`CH:routes/F6:147` via K3:152). The floor is the same 16 as the Z₁₆ gate (`CH:ROUTES.md:34`). That is not a coincidence: both count the Weyl components of one generation.
   - **Robust core (proved, and true even if the SM fields are composites):** a site whose whole Hilbert space is 2-dimensional (AX:47) admits no nontrivial SU(3) action, because SU(3) has no nontrivial representation of dimension ≤ 2. So exact on-site colour is impossible on a one-qubit site in any encoding.
   - The 16 floor assumes the SM fields are *elementary* site modes. With site-local composites it drops. For example, 5 modes, whose 32-dim Fock space contains the 16 (Wilczek–Zee; comparator, recalled). That is still far above one qubit.

2. **(a) is not free.**
   - If the axiom's sites are the fine qubits, the floor contradicts unit-translation covariance (AX:57-58) together with "no site is privileged" (AX:40). The law must then be covariant only under block translations: a crystal with a basis.
   - If instead the blocks are the axiom's sites, the site domain is M_{2^N}, and that is (b).
   - Operationally ⊗_x M_{2^N}(C) ≅ ⊗_{x,i} M₂(C), so the physics is identical (reading). Only the axiom line that carries the price differs.
   - I prefer (b) for three reasons:
     - it keeps the Lattice axiom literal;
     - the gravity root already presupposes a ~90-mode site (`GR:agents/panel_F/SYNTHESIS.md:52`);
     - X2 is written as a 32-mode site (`CH:combos/X2/COMBO_REPORT.md:55,212`).

3. **(c) is unavailable under the observation standard.** It would also fail vector-like QCD by item 1, so it concedes more than handedness.

4. **Count corrections.**
   - The dossier's "16 for X2" is the KS count. **X2 as written is 32 modes per site** (2 walker components × 16; X2:212), all three generations included.
   - With a *local* fermion-to-qubit encoding in 3D, multiply by about 2–3 qubits per mode (comparator, recalled: Verstraete–Cirac, Bravyi–Kitaev superfast). The exception is when fermion parity is itself a gauge element, i.e. the Spin(10) centre or Z₄^X. Then a purely bosonic qubit register suffices (Wang–Wen, `CH:OUTSIDE_VIEW.md:39,173`, a proposal).
   - Tally (checked, `scripts/site_budget.out`):

     | Carrier | Fermion modes per site | Qubits with a local encoding |
     |---|---|---|
     | X2 | 32 | ~64–96 |
     | Gravity root | ~90 | ~180–270 |
     | Slab | 768–1152 | ~1.5–3.5×10³ |
     | Finite-n approximate overlap, 3 generations, δ ≈ 1e-35 | ~1.2×10⁴ | — |
     | Same, δ ≈ 1e-88 | ~2.9×10⁴ | — |

     The finite-n rows use F2's direct pole counts, n = 30 and n = 76 (`CH:routes/F2/ROUTE_REPORT.md:169,173`).

5. **Fermion number conserved only mod 4 (X2's price P-X2-6, `X2:80`) is not an observational problem at the grid scale (checked, arithmetic; hadronic inputs are comparators, recalled).**
   - It reaches the light sector only as dimension-6 qqql operators (C/Λ²).
   - p → e⁺π⁰ > 2.4e34 yr needs Λ/√|C| ≳ 5.1e15 GeV.
   - At 1/a = M_Pl with C = 1, the lifetime margin is 3×10¹³. With X2's leakage suppression, 1/a ≳ 10¹²–10¹⁵ GeV suffices.
   - It is consistent with SM sphalerons (ΔF = 12 ≡ 0 mod 4).
   - It becomes a constraint only if a ≫ ℓ_P (`GR:agents/panel_F/SYNTHESIS.md:44`).

6. **Reject an infinite register as law content** (reading). It is not needed observationally (item 4's finite rows). It makes "one record per site" (AX:79-80) lock infinitely many modes at once, and it gives up finite entropy per site.
   - Caveat: compact-group gauge links (L²(G) per link) and the supplied graviton (P-N1, `GR:SUMMARY.md:777`; R19-22 `GR:TESTS.md:8309`) already lean on infinite local spaces.
   - **Decide "are local domains finite?" once, for matter, links and graviton together.** Unbounded *bosonic* local spaces are the riskier kind. Lieb–Robinson light cones can fail for unbounded bosonic interactions (comparator, recalled: Eisert–Gross 2009). Infinite *fermionic* fibres keep them.

7. **Landed notes that D1 re-scopes.**
   - `docs/STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md:41-54` and `docs/STAGGERED_DIRAC_KINETIC_CLASS_TWO_COMPONENT_EXCLUSION_NARROW_THEOREM_NOTE_2026-06-11.md:13-20` exclude Wilson, naive, two-component and walker carriers on the strict one-mode reading.
   - X2's walker is exactly the excluded D_2c = Σσ_μ⊗∇_μ.
   - Under D1 = (b) those notes stay true as conditionals on N = 1 and stop binding.

### D2. Range

**Recommendation: do not admit a non-finitely-generated kernel as law content.** Allow two things:
- finite-range laws, which are nearest-neighbour after blocking;
- "nearest-neighbour-generated" quasi-local objects for derived quantities and proofs, such as spectral projectors and quasi-adiabatic disentanglers.

**Reasons.**

1. **Observation cannot tell quasi-local from local** (comparator, recalled: Lieb–Robinson; Hastings–Koma). Exponential tails with ξ ~ a leak e^{−10²⁰} across a fermi. "Quasi-local" is not an observational price.

2. **Blocking trades range for register size (proved, elementary).**
   - A range-r law on N-mode sites is a nearest-neighbour law on N·r³-mode blocks.
   - So once D1 allows a finite register, AX:57's "nearest-neighbour" adds nothing beyond "finite range".
   - The class that survives blocking is "finitely generated" (rational symbol), which is exactly Lemma R's class (`CH:routes/F2/ROUTE_REPORT.md:48-62`; codex-confirmed, `CH:ROUTES.md:146-156`).
   - So D2's real content is one thing: accept a kernel that no finite block makes nearest-neighbour.

3. **D2 = yes buys handedness only in set B.**
   - In continuous time, any range fails on two counts:
     - Lemma H puts every free charge sector into balance (`F2:126-132`);
     - Fidkowski–Xu forbid a shallow-circuit chiral U(1) on finite sites (`OUTSIDE_VIEW:56`).
   - The codex referee's caveat (`ROUTES:156`) concerns other escapes, not range.
   - In set B, the exact overlap makes the real-time site infinite (`CH:combos/X3/COMBO_REPORT.md:131-143`; K2 referee: the two costs co-occur, `ROUTES:164`). So **D2 = yes implies D1 = ∞**.

4. **The finite approximation costs D1, not D2.**
   - It needs ~60–150 auxiliary Dirac fields per field (`F2:157-160`, `:169-176`), with gauge violation of order δ. The contract allows emergent symmetry with bounded violation (`CH:WALL.md:41`).
   - In set B, though, the Pauli–Villars-subtracted finite version also fails reflection positivity (K2c, `ROUTES:184,197`). Without Pauli–Villars it becomes a 5D slab whose far wall needs SMG, i.e. route 3.

5. **AX:57 does not itself decide D2** (reading).
   - Admissibility constrains the record rule, not dynamics (AX:114-123; `CH:WALL.md:57`).
   - Read literally, it is a Markov-field condition. Even nearest-neighbour Hamiltonians do not give exactly nearest-neighbour-Markov statistics unless their terms commute (comparator, recalled: Hammersley–Clifford; Brown–Poulin).
   - Commuting-projector models with finite sites carry no Hall response (Kapustin–Fidkowski, `OUTSIDE_VIEW:60`).
   - So D2 is a choice about supplied dynamics. It is not compliance with the axiom text.

6. **On F2's option (c), sign(H_W) = 1 − 2P₋(H_W).** It is an operator function, not a choice of state. I agree with the codex referee (`ROUTES:154`).

### D3. Time

**Recommendation: hold the decision until NT-1, NT-2 and the UV test in §5 report. Default to set C if set B's chiral real-time branch needs a "Π-W for matter" that has not been constructed.**

**Reasons.**
- **Set C is native to the Qubit and Record axioms.**
  - M₂(C) on a site and readable records are Hilbert-space statements (AX:47, :77-83).
  - Set B gets its Hilbert space only through reflection positivity.
  - RP now fails, or is in doubt, in three independent places:
    - the conserved GR bridge (R19-33 B-RP-FAILS, `GR:TESTS.md:8909-8913`);
    - the hard-measure overlap (K2c, codex-confirmed for the 2D U(1) proxy including tori, `CH:ROUTES.md:190-204`);
    - the hard plaquette bound in 3D (NT-2 pending; pure gauge at Lx = 3 is already negative, `ROUTES:198-201`).
- **Set B's real asset is gravity's.** The 90° time–space rotation is the only symmetry that fixes the matter light cones without tuning (`GR:SUMMARY.md:774,778`).
  - The condensed-matter comparator agrees. Without a symmetry, grid-scale Lorentz violation leaks into dimension-4 operators at O(1) per loop (comparator, recalled: Collins–Pérez–Sudarsky–Urrutia–Vucetich 2004).
  - That argument is about gravity and light cones, not handedness.
- **Handedness does not favour B once D2 = no.**
  - B with finite rules returns to SMG: Catterall-type reduced-staggered SMG on Z⁴ (comparator, `OUTSIDE_VIEW:73-74,96`), or the 5D slab.
  - That is the same frontier (I) as in set C.
- **A non-RP lattice is not automatically fatal.**
  - Lattice QCD runs improved actions whose transfer matrix is not positive. The unphysical states sit at the cutoff (comparator, recalled: Lüscher–Weisz 1984).
  - In a TOE, though, cutoff states are real. Negative norm at the grid scale means negative probabilities for grid-scale records.
  - If K2c's violation turns out to be cutoff-confined, that should be a **new named price** ("ghosts only at grid energy"), not a silent pass.

### D4. Compute and collaborators

**Recommendation: (b) plus (c) now; (a) only after two gates.**

**Gates for (a):**
1. NT-3 reads TG1-SYMMETRIC.
2. A *proved* sign-free design exists for X2-MB (Majorana/Kramers positivity).
   - X2 itself says "establish sign-freeness first" (`X2:286`).
   - If X2-MB is not sign-free, it is not "weeks"; it is out of reach.
   - F4 test A already uses a Slagle–You–Xu-type design that is known to be sign-free (`CH:routes/F4/ROUTE_REPORT.md:185-195`).

Weeks of QMC on a shared 16 GB Mac is the wrong tool.

**Collaborators to add** (the dossier's list lacks the people who own these exact 2+1D tests):
- **Condensed-matter QMC:** Yi-Zhuang You, Cenke Xu, Zi Yang Meng, Kevin Slagle, and Fakher Assaad (the ALF open DQMC code). They ran the 2+1D SMG transitions (`OUTSIDE_VIEW:94`).
- **4D GPR / intermediate-phase question:** Catterall and Hasenfratz (Butt–Catterall–Hartshaw–Hasenfratz 2026 is that question; `OUTSIDE_VIEW:96`).
- **Adversarial referee on zeros and composites:** Golterman–Shamir.
- **S\* and finite-dimensional disentanglers:** Thorngren, Preskill and Fidkowski. The open item there is that their rotors are infinite-dimensional (`OUTSIDE_VIEW:98`).

**Record the prices now regardless.**

Be clear with collaborators that a 2+1D PASS informs but does not decide 3+1D (`F4:123-128`).

---

## 2. How the decisions interact

| If… | Then… | Basis |
|---|---|---|
| D2 = yes | D1 must allow ∞ (real time), and only set B benefits | X3-C (`X3:131-143`); Lemma H (`F2:126-139`) |
| D1 = finite | D2's "nearest-neighbour" clause is moot (blocking); only "finitely generated?" remains | §1 D2 item 2 (proved) |
| D2 = no | Handedness rests on SMG / lattice completeness (frontier I) in **both** set B and set C | `CH:ROUTES.md:49-51`; F2-T; X1 S\* |
| D3 = C | D2 is irrelevant to handedness | Lemma H + Fidkowski–Xu |
| D3 = B | D2 is **not** forced. B with D2 = no means Catterall-type SMG on Z⁴ or the 5D slab. D2 = yes is worth something only if NT-1 passes and L2α and L3grav hold | `X3:272-288` |
| D1 = (a), literal | D1 = (b) plus a Lattice-axiom change (block translations) | §1 D1 item 2 |
| Any D1 | Must be decided together with the fermion edge, because strain safety depends on it: the overlap removes the strain mass (`X3:147-151`); staggered gives twins (TW-1/2/3, `GR:TESTS.md:9720-9735`); Wilson D1 edges carry the PSI hazard | — |
| D4 | Depends on D2 and NT-1. If D2 = yes and NT-1 passes, the decisive test is L2α (Kikukawa's measure MC; Kikukawa, Fukaya/Onogi), not SMG QMC | `F2:189-195` |

**Net.** If the owner never accepts an infinite local register, D2 is settled, D3 is a gravity decision, and handedness is a bet on SMG that only D4 can advance.

---

## 3. Strongest argument from my tradition, and the steelman against

**For.**
- The quantum-matter programme says an anomaly-free symmetry should be realizable with finite-dimensional sites and on-site action. This is Wen's conjecture, proved for 1+1D finite groups (Seifnashri–Shirley, `OUTSIDE_VIEW:99`).
- With 16 per generation, every obstruction on *how the symmetry acts* vanishes in the slab (Lemma O, `X1:95-103`).
- So the expected home of a chiral SM is a finite register per site, and the obstruction is dynamical (SMG), not kinematic.
- Add the operational facts:
  - register size is unobservable;
  - range and register trade;
  - "finitely generated" is the only invariant.
- So D1 and D2 are bookkeeping choices, and the economical choice is "finite, finitely generated".

**Against (steelman).**
1. **Golterman–Shamir may be right that SMG zeros are kinematical.** Then every finite-register route fails, and the only door left is the exact overlap (D2 yes, infinite fibre). My D2 = no would close it.
   - My mitigation: D2 = no is reversible. A GS-type theorem should reopen it.
2. **Lattice completeness may fail** (Shirley–Zhang–Ji–Levin show anomaly-free ≠ on-siteable in 2D, `OUTSIDE_VIEW:100`). Then no finite register suffices whatever its size.
3. **N = 32 to 10⁴ makes "qubit" decorative.** The framework then reads as generic lattice field theory on Z³, plus records. That is a real loss of distinctiveness, and I have no answer to it beyond honesty.
4. **The floor theorem assumes exact on-site link gauge invariance.**
   - Emergent non-abelian gauge fields with colour spread over one-mode sites would keep the strict reading. Jon's thought that records are the grain and particles are patterns (owner's thought, being tested) points this way.
   - No 3+1D example exists. The emergent-photon-from-qubits case (quantum spin ice; comparator, recalled) is U(1) only.
   - This is the only road that keeps one qubit per site, and it is harder than handedness.
5. **On D3, preferring C gives up the only symmetry mechanism for one light cone.** C5 found set C costs 4 tuned numbers per charge class per order, or a counting clause (`GR:SUMMARY.md:778`).

---

## 4. What would change my mind

**NT-1 (chiral-measure RP).**
- **CHI-RP-PASS-at-power:** set B stays alive for handedness. D2 becomes a live owner question, worth deciding only alongside D1 = ∞. I would lean D3 toward B.
- **CHI-RP-FAIL:** the exact-overlap door needs an unconstructed Π-W for matter. D2 = yes then buys nothing, and my D3 default moves firmly to C.

**NT-2 (3D plaquette-bound RP).**
- **PG3-NEG:** set B has a gauge-side RP problem before any fermion enters. That strengthens C.
- **PG3-PSD:** removes one of set B's three RP problems.

**NT-3 (T-G1).**
- **TG1-BROKEN** (the filter overlap frustrates the symmetric phase): X2's 32-mode route is wounded. The cheapest finite register rises to the slab's ~10³, and D4's first ask shifts to F4 test A (condensed-matter QMC).
- **TG1-SYMMETRIC:** X2 remains the cheapest finite route. The D4 ask goes to Catterall/Hasenfratz with a sign-free 2+1D design.
- **Scope caveat:** 1D rings at strong coupling test only overlap frustration, not 3+1D SMG.

**Other evidence.**
- **A UV-confinement result** (§5): if the RP violation vanishes at fixed physical distance from the plane as the gauge coupling weakens, I would accept set B with a named "grid-energy ghost" price.
- **An explicit emergent SU(N) gauge theory with spread colour on a one-mode lattice:** reopens the strict Qubit reading and weakens D1 = (b).
- **A proof of the GS conjecture:** I would reverse D2.

---

## 5. One concrete next action

**A decision: settle D1 once, across all lanes.** The proposed wording is: "a site holds a fixed register of N fermion modes (graded qubits); N ≥ 16 is set by matter content; local domains are finite (or not), the same rule applying to matter, links and graviton."

Why this first:
- It costs no compute.
- It is a precondition for any SM matter on this grid, handed or not (§1 D1 item 1).
- It legalizes the gravity root's ~90-mode site and all three chirality routes.
- It forces the explicit re-scoping of the two strict-reading staggered notes.
- Its "finite domains" clause settles D2 by implication.

**Runner-up (a test, hours, ≤ 0.4 GB): RP UV-confinement.**
- On K2c's W-matched machinery, raise β_g so that the Schwinger mass falls well below the cutoff. Restrict the witnesses to functions supported at depth t₀ ≥ 1, 2, 3 from the reflection plane.
- **Reading:**
  - **UV-CONFINED:** the negative eigenvalue, relative to the physical channel, falls with t₀·m_S and with β_g.
  - **IR-PERSISTENT:** it does not.
- This decides whether set B's non-positivity is a grid-scale price or a real-time failure. Note that K2c's β_g = 0 runs have no scale separation, so they cannot answer this.

---

**Files:** `statement.md` (this file); `scripts/site_budget.py` and `scripts/site_budget.out` (arithmetic only; the appended correction uses F2's direct pole counts).
