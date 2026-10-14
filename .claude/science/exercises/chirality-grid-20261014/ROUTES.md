# Routes (steps 4, 6, 7)

## Round 1: independent families (13:19–14:10Z)

Six Opus 5.5 agents ran at xhigh, all from the same family. Each had a neutral, route-local brief. Reports are in `routes/F*/ROUTE_REPORT.md`, scripts in `scripts/F*/`. Nothing here is refereed, except that a codex referee is running on F2-R.

| Route | Family | Key result | Label | Strength vs target | Status |
|---|---|---|---|---|---|
| **F1-R1/R2** | Interaction-gapped mirror on the native carrier (momentum-selected) or slab-as-payload | Mod-16 gate: every candidate mirror passes at d = 16 and fails at 15. ν_R is forced by translations plus fermion parity on the staggered carrier. The Golterman–Shamir reduced-model signatures (a) far-corner composites and (b) a k = 0 mirror composite are located. Exact translations forbid light·mirror³ but allow AABB. | checked (C1, C2); proved (selection rule) | stronger (L ⇒ T), so blocked-equivalent | blocked-equivalent; the obligation is sharpened to "GS condition (3) fails" |
| **F1-R3** | Bulk path / automorphic equivalence: a symmetric gapped path from the slab bulk to a product state gives a quasi-local disentangler that gaps the mirror exactly | Proof skeleton. GS's conjecture ⇒ P false ⇒ a lattice invertible phase beyond cobordism | suggested | stronger | blocked-equivalent; **reopen: P or an explicit disentangler for 16 with Spin-Z4/Spin(10) in 4+1D** |
| **F2-R** | Price lemma: a rational exact Ginsparg–Wilson operator gives Chern 0 and hence doublers | Lemma R: any rational regular idempotent on T^d has all Chern classes 0. Exact GW therefore needs (a) a non-finitely-generated quasi-local kernel, (b) infinitely many auxiliaries per site, or (c) an auxiliary vacuum. The obstruction is independent of the fibre, so M₄(C) does not help. Tests T1, T3b/c, T4b, T5b pass. | proved (skeleton); checked | weaker (a price) | candidate-complete as a price, **pending the codex referee** |
| **F2-H** | Overlap-projected 16 plus a strongly coupled mirror (Kikukawa) on Euclidean Z³×Z_τ | Terminal: locality of the non-abelian measure (L2, open) and reflection positivity of the gauged measure (L3, open). Free overlap is link-RP (Kikukawa–Usui), which corrects R2-4 :204. | suggested | comparable | active; first test is a 2D vacuum-polarization MC |
| **F2-T** | Continuous time with a compact non-on-site chiral charge | Lemma H: balanced in each charge sector. Gioia–Thorngren's single-Weyl symmetry is non-compact; Fidkowski–Xu applies. | proved (free) | — | blocked-equivalent to SMG |
| **F3-A** | One-handed tick: a price theorem | E = (i/2)(U−U†) = sin H_F is conserved and local. The mirror sits at quasi-energy π, inverted, with identical charges. Either the vacuum lases with no threshold, or E′ exists and the mirror is light. The repo's U_g has E = g·(4R+4L walker), and Re U is the K2a selector. Corrects T22 kill :19. | proved (2-band); checked (R1-F1, R1-F2) | weaker (a price) | provisional no-go; positive continuation F3-C is blocked-equivalent to F1 |
| **F3-B** | Flux index κ for gauged QCAs | κ = 0 for continuously gaugeable QCAs. The SM's gauged charges have Σχq = 0, so index theory adds nothing for the SM. | proved (free); checked (R2); interacting open (O-κ) | weaker | provisional |
| **F4-A** | Inflow slab with far-wall SMG (an internal ladder of ~10³ qubits/site) | L1: a k-independent far self-energy moves the mirror, never removes it. **L2: a successful far wall forces a protected (non-removable) zero, so the slab works iff GS's "zeros are kinematical" conjecture fails for that model.** Real-space separation means no Eichten–Preskill leakage. | proved (L1); proof skeleton (L2); checked (T-F4-1) | target-equivalent | blocked-equivalent; the decisive test is a 2+1D-surface DQMC (weeks) |
| **F4-B** | No-go for every no-interaction inflow variant | Gauge-side dichotomy (fibre collapse is vector-like, or Planck-strength 1/L penalty). L ≳ 10⁴⁶ needed. | proof skeleton; checked (T-F4-2, T-F4-4b) | weaker (a price) | provisional no-go |
| **F4-C** | Folded single-boundary slab | Free fermions: exactly one Weyl per flavour, no mirror, 2L layers per site (T-F4-3 PASS). Gauging needs world-range gluing plus nonlocal photon terms. | checked | price | price recorded |
| **F5-A/B/C** | Dissipative / record-driven | Non-Hermitian damping escapes T2 (W3 = −1, checked), but Lemma B puts the Berry flux in the state. Every sink fails: jumps forever, an empty sea plus exhausted one-record capacity, or an Ohmic vacuum ~57 orders out. | proved (B, C, P, D); checked (T1, T2, T3a, T3′) | F5-A retired; F5-B wounded; F5-C blocked-equivalent to SMG | — |
| **F6** | Misframing | (1) M₂(C) per site already has an exact handedness operator T_d. What is missing is the net count, which is fibre-independent, so #4 and #2 are not prices for this wall. (2) Index lemma: no gauge-respecting mass changes the net count, so the 11-item failure list was guaranteed. (3) Electroweak-mass mirrors are excluded by S (4–6σ) and gg→h (≥ 9×). (4) "8 vs 48" is a category error. The anomaly gate (cheaper question Q\*) passes with ν^c. | proved / checked (tA–tD) | weaker (pruning) | survives; the wall is reframed as the field's shared SMG conjecture plus two framework prices (matter per site; how gauge fields enter) |

### Round-1 synthesis (supervisor)

1. **Convergence.** F1, F3, F4, F5 and F2-T reduce to one obligation: in 3+1D, can a symmetric interaction gap an anomaly-free mirror 16 while leaving a protected, non-kinematical zero (Golterman–Shamir condition (3)/(4) failing)?
   - F4-L2 makes this a single observable: a protected zero, or a massless composite.
   - F1-C2 locates the two composite signatures.
2. **Independent of that obligation:**
   - F2-H (Euclidean overlap plus a strongly coupled mirror) ends at a different lemma: non-abelian measure locality plus reflection positivity.
   - F2-R and F3-A turn the range and tick questions into exact prices.
3. **Corrections to earlier supervisor statements:**
   - The parked decisions #4 (M₄(C)) and #2 (orientation bit) are not prices for this wall (F6, F2-R).
   - T22 kill :19 understated the π copy (F3-A).
   - R2-4 :204 is out of date on free overlap RP (F2-H).
4. **Framework-native fact.** The walker's hw1 triplet is single-handed under T_d. With iεF the zero modes are exactly 3L at hw1 and 3R at hw2 (F6 tD, checked). The mod-16 gate passes only at 16 per generation (F1 C1).

## Round 2: combinations (14:07–14:58Z)

Three Opus 5.5 agents at xhigh, same family. Each crossed cores from different families. Reports are in `combos/X*/COMBO_REPORT.md`; nothing is refereed.

| Combination | Cores | Key result | Label | Strength vs target | Status |
|---|---|---|---|---|---|
| **X1 disentangled inflow** | F1-R3 + F4 slab + TPF disentangler + F3-B κ | The terminal is S\*: the slab bulk ground state can be symmetrically disentangled to a product. S\* = cobordism triviality (known: 16 ≡ 0) + **lattice completeness (open conjecture)**. In the slab, every obstruction on how the symmetry acts on the lattice is automatically zero (Fidkowski–Xu, the Shirley–Zhang–Ji–Levin index, κ, Tu–Long–Else), so qubit-sized sites are not the obstacle. S\* and the GS conjecture cannot both hold. **Corrects F1-R3's grading from "stronger" to target-equivalent** (modulo the lattice bulk–boundary correspondence E3). | proved skeletons; checked (DI-Z8 1D instrument; SM-16 arithmetic) | target-equivalent | blocked-equivalent. **Reopen:** an explicit disentangler for ψ₀; lattice completeness in ≥ 3+1D; an invariant beyond cobordism |
| **X2 native three-generation package** | F6 (T_d, walker) + F1 (mod-16, filter) + generation lane + TW-2/TW-3 + F4-L2 | Explicit cubic-invariant filtered Spin(10) quartic on the walker: 3 generations at hw1, mirrors at hw0/hw2/hw3. **Light corners exactly decoupled:** [H, ψ(hw1)] = 0 at every coupling (checked). **Corrections:** F1's selection rule is false for 3-light splits; F6's 3L+3R shortcut is tuned. Eichten–Preskill leakage is present, cannot be forbidden, and is irrelevant (dim-6). **Flavour theorem (proved, checked over 1120 subgroups):** nontrivial CKM forces a residual that leaves a strain direction invariant, so a first-order flavour-strain channel is unavoidable (size open; goes to C5). | proved; checked (T1–T5) | stronger, so blocked-equivalent (= GS cond. 3 fails + no SSB) | blocked-equivalent; **it is the Eichten–Preskill design; the Golterman–Petcher–Rivas intermediate SSB is the open kill**; the mixed Z₂³ anomaly classes are the cheapest open kill |
| **X3 Euclidean set-B package** | F2-H/F2-R overlap + F3-A + gravity set B (R19-28/33) + strain | **Free test PASS:** the OS-reconstructed overlap transfer matrix has one light Weyl per chirality; its doublers are a positive-norm continuum at E ≥ ln 2 (Planckian), with nothing inverted, so **F3-A does not apply to the Euclidean route** (its scope is restricted to finite-band unitary ticks). **F2-R prices (a) non-rational kernel ≡ (b) infinite-dimensional site, as one price** after reconstruction. Overlap's exact GW symmetry removes NF-1's taste price and R19-34's strain-mass hazard. **Gauged RP:** gauge-fixed positivity (Osterwalder–Seiler route) fails for the overlap; gauge-averaged tests are inconclusive. New leaf L3grav (the overlap stress is non-local in time). | proved (free); checked (T-X3 PASS; T-X3b–f) | stronger | active through finite tests of L2α and L3g; the terminal L2α (non-abelian measure locality) is not advanced |

### Round-2 synthesis (supervisor)

1. **No combination supplies a new mechanism toward the target.**
   - Every chirality route in the round ends at one of two frontier statements, and both are open across the field:
     - **(I) the symmetric-gapping / lattice-completeness question:** GS condition (3), equivalently S\* (F1, F3, F4, F5, X1, X2);
     - **(II) the locality of Lüscher's non-abelian measure plus gauged RP** (F2-H, X3).
   - Neither is specific to this framework.
2. **Genuine gains of the round:**
   - **F3-A** is now scoped to real-time finite-band ticks. The Euclidean route escapes it (X3, checked).
   - **F2-R's two prices are one price.**
   - **Qubit-site obstructions do not bind slab or Euclidean constructions** (X1, X3).
   - **The framework's own walker gives a clean, cubic-invariant three-generation chiral package** (X2), whose failure mode is precisely known: GPR intermediate SSB, or a GS composite.
   - **New cross-lane theorem:** nontrivial CKM forces a first-order flavour-strain channel (X2-L8).
3. **Gravity × chirality.** Set B (Euclidean Z⁴) now carries the best gravity bill (R19-28, refereed) **and** the only chirality route whose free real-time spectrum is clean (X3). Its shared obligations are gauged RP plus the RP of matter + spatial-TT gravity with a time-non-local overlap stress (L3grav).
