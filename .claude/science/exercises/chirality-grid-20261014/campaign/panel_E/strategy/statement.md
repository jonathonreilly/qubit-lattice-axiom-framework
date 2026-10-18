# Panel E: program-strategy statement (2026-10-17)

**Provenance.** Written by Claude Opus 5.5, the same model family as the supervisor, every worker and the other lenses, so it is **not independent**. Nothing here has been refereed. I read DOSSIER, SUMMARY, TESTS from wave 1 to the end, every campaign REPORT and REFEREE_VERDICT, the CKM synthesis, X2, X1, F4 and panel D, and the full axioms file. My one script, `panel_E/strategy/scripts/strategy_numbers.py` with its `.out`, does back-of-envelope arithmetic only. No repository was edited and nothing was sent.

**Path prefixes.**
- CH = `origin/claude/chirality-grid-exercise-20261014:.claude/science/exercises/chirality-grid-20261014/`
- AX = `docs/MINIMAL_AXIOMS_2026-06-29.md`
- GR = `.claude/science/exercises/gravity-current-state-20261009/SUMMARY.md`

## 0. Plain words

1. **Putting one generation at each cube corner is what breaks X2's flavour sector. Its chirality mechanism is not what fails.** With exact grid translations, corner generations cannot mix the way quarks do. Every way to supply the mixing either fails flavour-changing bounds or needs tuning of about 1e-27. **Keep the mechanism; stop putting generations on corners.** The re-scoped package (call it X2′) puts all three generations at the one fully symmetric corner (k = 0) as an internal label. That removes four of the campaign's flavour prices by construction (suggested). The cost: the number 3 is supplied rather than explained, matter per site goes up ×3, and one Lorentz-violation price returns at one loop.
2. **The Lorentz-violation part of every flavour price is the same wall as gravity's "matter light cones".** Its cost is set by gravity's open owner question on counting (GR:792), not by chirality. Jon should decide it once.
3. **Route 1 is not closed.** The negativity sits in the part of the weight that does not depend on the measure. But no legitimate chiral measure has been tested on a geometry that can host one. Finish TOR-1, then stop route 1 in-house.
4. **Route 3 should get referee time and the outside ask, not worker time.** Its decisive test is too large for this machine in 18 hours. Its question is exactly the one the outside SMG groups can answer from data they already hold.
5. **QMC-1's validated code makes the collaborator ask timely now.** The compute is cheap (about $0.2k–$1k in the cloud for a 2+1D scan). What is missing is a specialist and a gap estimator the referee accepts.

## 1. Verdicts

### Q1. Route 2 (X2)

**Is X2 viable?** It is not killed: every registered reading came back PRICE (CH/TESTS.md:362, :412, :468, :573). As registered, X2 is *flavour-priced out* unless Jon decides counting in its favour. Its remaining price list:

| Item | Status | Source |
|---|---|---|
| 32 complex modes per site; fermion statistics; supplied walker + W·Q; range ≤ 2; on-site Spin(10), G_SM links, covariant F[U]; ν_R forced; U(1)_F → Z₄ (Dirac ν, zero 0νββ) | named prices | CH/combos/X2/COMBO_REPORT.md:212-219; panel_D synthesis:18 |
| L_X2: symmetric mirror gap, no 10-vector condensate, no gapless composite, zeros not ghosts once gauged | open; QMC-1 suggests a GPR-like crossover | X2:171-177; TESTS.md:639 |
| Mixed Z₂³ anomaly of the 5-corner mirror | unchecked ("cheapest open kill") | X2:252 |
| F1. Exact translations ⇒ CKM is a permutation | proved (definite-momentum content) | TESTS.md:471, :512 |
| F2a. Electroweak-doublet carriers | D3 benchmark: M* ≈ 1.3–7.9e3 TeV needed; no decoupling limit; shortfall ≥ 180 even tuned; not universal | TESTS.md:472-473, :514; OBS4 REPORT:134-136 |
| F2b. Class S (lattice-scale singlet) | Θ + about 1e-27 kinetic tuning (one-loop toy regenerates a 2.9e-2 spread) + κ ≲ 0.55 + no gapless composite | TESTS.md:583, :596-601 |
| F2c. Intermediate scale | no window (reading, CKM synthesis:65-69). My addition (suggested): the light–light kinetic coefficient and the off-diagonal Yukawa carry the same spurion S_K·a, so the tuning needed (bound / y_off) does not depend on the breaking scale. | — |
| F3. One-loop Lorentz violation | B-gen escape exists, but only with F2's carriers; two-loop L-words about 1e13 over the bound | TESTS.md:414-422 |
| F4. Strain/clock | CKM forces a first-order traceless-strain channel; clock row ×0.09–2.5 (FLAV2-NEAR) | X2:126-136; TESTS.md:371 |

**Is the CKM–translation tension a no-go or a price?**
- It is a structural no-go for *natural* corner generations. F1 is proved, and F2c's tuning is scale-independent.
- It is a price only for *tuned* ones: at least 1e-24 to 1e-27, or a counting clause plus Θ.
- It is not a theorem-level no-go. The class-S coefficients are natural, not forced. The D3 benchmark is not universal. Of possible protecting symmetries, only flavour symmetries are closed off, by the YY† spurion argument (CKM synthesis:59-63).
- This is not new to the repo. Main already has the Z₃ version, single Higgs ⇒ monomial Yukawas (`origin/main:docs/LEPTON_SINGLE_HIGGS_PMNS_TRIVIALITY_NOTE.md:24`). The campaign adds the escape prices. Because main's hw=1 triplet programme reads generations off translation characters (`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md:23-33`), **this is a cross-lane finding for the flavour lane**, like X2-L8 was for gravity.

**Should X2 be re-scoped?** Yes (reading). X2′ keeps X2's carrier, filter class and quartic, puts 3×16 at Γ with a filter that vanishes only there, and uses one k = 0 Higgs. What changes (all suggested; GEN-1 below checks them):
- CKM is unconstrained by translations: Γ + Γ + 0 = 0, so F1, F2a and F2b do not arise.
- Only the Standard Model's own FCNC remains.
- The Γ label sector is single-handed, and f(Γ) = 0, so X2-L1 and X2-L2 survive.
- Γ has full cubic symmetry, so no first-order traceless-strain channel exists (F4 removed).
- The light content is translation-neutral, so X2's mixed-Z₂³ kill question should pass automatically.
- Light³·mirror couplings become translation-forbidden.

What it costs:
- the native "3" (now a supplied index);
- 96 complex modes per site instead of 32;
- **no texture escape for one-loop Lorentz violation.** The speed matrix on Q is ∝ H_u + H_d, and that cannot be flat in both the up and down bases. My estimate of the d–u spread is κ̄y_t²|V_td|² ≈ 1.5–7.5e-7, about 1e15 over the D44 rows (`strategy_numbers.out`). It uses OBS-3's hw1 kernel; the Γ kernel is not computed. Removing it needs about 7 linear flavour-covariant counterterms per order, tuned to about 1e-16. That is the same class as set C's standing cone price (GR:778), and it applies equally to route 3's near-wall modes. So **flavour-pattern Lorentz violation is generic to set C** whenever generations are an internal index.

Net: X2′ beats X2 under either counting regime. X2's corner branch should be recorded as "FLAVOUR-PRICED", with the table above, and parked rather than rescued.

### Q2. Route 1

**Is RP failure established for a legitimate chiral measure?** No.

Established, at referee scope:
- On open time, the chiral kernel is negative for a chart-local Lüscher-structured measure, and the negativity sits in the modulus (TESTS.md:463-464, :483).
- Open time cannot host a legitimate global measure: (b″) cannot be met (:566).

The modulus is fixed by D alone, and the measure's phase moved λ_min by at most 1.2% (:464). So, suggested: wherever the negativity exists, a cleverer measure will not remove it. The open question is geometric.

TOR-1's partial outputs (unrefereed, in progress; `campaign/TOR1/scripts/POST3.out:1-5`) show the chiral, modulus and vector-like references all PSD within error at the searched Lt = 4 pool. The binding issue may therefore be power, not legitimacy.

**What would close set B's real-time branch:**
- (i) a torus reading *with power*: CHI-RP-FAIL, with the vector-like reference also negative;
- (ii) an owner ruling that exact RP is required (CH/WALL.md:44; AX:60-61) even though UV-1 places the failure in a lattice-scale tail;
- (iii) the 4D non-abelian case, which only a collaborator (Kikukawa) can supply.

I would call it "closed at 2D-proxy scope once (i) lands, parked pending an outside 4D answer", and do no more 2D proxies either way.

### Q3. The ~18 hours

- **Worker time** goes to the re-scope (GEN-1, QMC-1b; §4).
- **TOR-1** finishes and gets its referee.
- **Route 3 gets codex time, not Claude time.** Have the codex referee check F4-L1/L2/L3 and X1's Lemmas E and Z now. These lemmas are unrefereed (CH/routes/F4/ROUTE_REPORT.md:241), and the outside ask cites L2.
- **No in-house route-3 QMC.** A 4×4×4 slab with the Spin(10) 16 is about 45× QMC-1's L6 cost per sweep. An 8-flavour version needs a new sign-free channel.
- **Usage-limit risk.** Use at most 3 Claude agents, put referee load on codex, and checkpoint each landing to the branch.
- **Timeline.**
  - Now: GEN-1, QMC-1b and the F4 referee start.
  - 16Z: TOR-1, then its referee.
  - ~18Z: GEN-1's referee.
  - ~23Z: QMC-1b's readout and referee.
  - 00–05Z: synthesis, owner sheet and cross-lane notes (the flavour lane gets NFC plus the escape prices; the gravity lane gets the flavour multiplier on the light cones).

### Q4. D1–D4

- **D1** keeps its direction: finite, counted, decided once. Do not anchor N at 32. The candidates are now 32 (X2 corners, priced out), 96 (X2′, the same order as the ~90-qubit gravity root cited at panel_D/strategy_statement.md:63) and about 1e3 (route 3).
- **D2** is unchanged: decline. Route 1 is weaker.
- **D3**: set C stays the default, but its bill grows. The flavour-pattern Lorentz violation is part of the matter-cone wall, and set B removes it by symmetry (GR:774). Decide D3 together with gravity Q2 (counting) and Q6 (set B). If the counting clause counts as zero numbers, it must be stated *per propagating mode*. Stated per gauge multiplet, it does not cover flavour.
- **D4** moves a little. Collaborators still come first. But the trigger for funding compute is half met (a sign-free engine is validated, TESTS.md:626). Pre-authorise a bounded cloud budget of about $1k for the 2+1D L = 8–12 scan (18k core-hours, or about 2.3k with the singlet factorisation; `strategy_numbers.out`). It should be gated on a referee-accepted gap estimator and a specialist reading the PREREG. 3+1D L = 8 (47k core-hours, 128–208 GB) stays collaborator-only.

## 2. Strongest argument, and the steelman

**Argument.** Four flavour tests in a row each turned a hazard into a bigger price: OBS-2 gave ×1e14, OBS-3 found an escape, OBS-4 showed the escape needs carriers above 1e3 TeV, and CLS-1 priced the remaining route at 1e-27. The NFC lemma names the root cause. One test that removes the root cause (GEN-1) is worth more than a fifth pricing (D6, general potentials, a search for a Θ-like symmetry). Spend in-house hours where we hold a unique asset: the validated engine and the flavour kernels. Spend outside asks where the field holds one: existing SMG configurations and 4D RP expertise.

**Steelman against.**
1. Corner generations are the repo's flagship (main's hw=1 programme). Supplying 3 by hand explains less.
2. Under Jon's standard, tuning fails no observation. If the counting clause counts as zero, class S costs only Θ plus dynamical conditions, and keeps native 3 at a third of X2′'s matter.
3. X2′ is forced at one loop where corners had B-gen.
4. Re-scoping after failed readings is moving the goalposts.

**Replies.**
1. Whether generations are corners is a decision for the flavour lane and Jon. Chirality should not be held hostage to it.
2. Agreed. That is why I tie the decision to Q2. A yes there would bring corners back as co-primary.
3. True, and stated above. But that cost is the cone class, whereas corner FCNC cannot be removed by any clause.
4. Agreed. X2 is recorded as FLAVOUR-PRICED, and X2′ is a new pre-registered object, not a rescue of X2's readings.

## 3. What would change my mind

- **GEN-1 = NO-GAIN** (X2-L1/L2 or a gate fails at Γ): drop the re-scope, and route 3 carries frontier I.
- **Jon answers Q2 "clause = zero numbers":** X2 corners becomes co-primary.
- **QMC-1b = FILTER-SENSITIVE:** keep momentum-filtered packages as the main vehicle for frontier I. **FILTER-ROBUST:** the 10-vector channel itself is the hazard, and weight shifts to route 3's freely chosen far-wall channel.
- **TOR-1 = CHI-RP-PASS-at-power:** D3 becomes "both open".
- **An outside group finds gapless composites in a 2+1D SMG phase:** routes 2 and 3 both drop, and D2/D3 reopen.

## 4. Tests, with readings fixed now

**GEN-1: generation placement (hours; reuses the OBS-2/3 kernels).**
- **Object.** X2′ as in Q1, with law-level G_SM Yukawas fitting PDG masses and CKM. Comparator: the X2-corner numbers.
- **Items.**
  - (a1) CKM is realisable with exact translations and one k = 0 Higgs.
  - (a2) X2-L1 and X2-L2 hold at Γ.
  - (a3) The Z₁₆/ν_R gate and the mixed Z₂³ anomaly of the 7-corner mirror.
  - (a4) Whether a CKM-forced first-order strain channel exists.
  - (a5) Whether any tree-level ΔF = 2 arises beyond the Standard Model's.
  - (b) The one-loop residual on the clean D44 rows after the per-field counterterm, and the number n of linear flavour-covariant counterterms needed to remove it, with their tuning.
- **Readings.**
  - **GEN-CONE(n):** a1–a5 hold and n ≤ 8.
  - **GEN-PRICE(n):** a1–a5 hold, but n > 8 or a non-covariant structure is needed.
  - **GEN-NO-GAIN:** any of a1–a3 fails.
  - **OPEN:** otherwise.
- **My prediction** (not independent): GEN-CONE with n ≈ 7.

**QMC-1b: is the GPR-like signal set by the corner filter? (about 6 h wall, two 1 GB processes).**
- **Setup.** QMC-1's engine and scope, with f_Γ = (2 − cos p_x − cos p_y)/4 against a rerun of f2. L = 4 and 6, β = 4, Δτ = 0.05, W ∈ {2, 4}, at least 200 sweeps. Gates (i)–(iv) are re-passed first.
- **Suppressed window:** E3w ≤ 0.1 at both L. This is a precondition only, not a gap claim.
- **Readings.**
  - **FILTER-SENSITIVE:** for f_Γ, some window W has S10/L² ratio (L6/L4) ≤ 0.75, at least 2σ below 1, while f2 gives ≥ 0.85.
  - **FILTER-ROBUST:** both filters give ≥ 0.85 at every window W.
  - **OPEN:** otherwise.
- **Fixed scope sentence:** neither reading establishes a gap, SMG or GPR.

**TOR-1:** the readings stay as registered (TESTS.md:557-560).

## 5. Collaborator ask: draft only, not sent (needs Jon's approval)

> Dear Prof. You and Prof. Xu: We are a small independent project. Our computations are by AI agents of one model family, each checked by an AI referee from another vendor; no human specialist has reviewed them. (1) We have a lemma that a slab whose far surface is gapped symmetrically must leave a far-surface propagator zero carrying the near cone's index, or else show a gapless composite. Would you measure the zero's index in G(ω=0,k) and the three-fermion composite weight in your existing SMG phase (arXiv:2603.18278)? We would pre-register the readings with you, and invite Golterman and Shamir to fix them in advance. (2) We have a validated sign-free AFQMC of a Spin(10) Eichten–Preskill-type model whose four-fermion legs are momentum-filtered so the light corners decouple exactly. At 4×4 and 6×6 (β = 4) the 10-vector correlations span the box once the mirrors are suppressed. That is a GPR-like pattern, not an established result. Is this the intermediate phase you would expect for this channel, and which gap estimator would you accept? Code, validation and data are available.

The Kikukawa ask goes second, updated with whatever TOR-1 reads. Catterall–Hasenfratz goes third, with QMC-1 and QMC-1b.