# C5 round 3, probe R3-4: set A's gravity escape. Which of E1–E4 is cheapest and still viable? (worker report)

**Worker.** Claude Opus 5.5, the same family as the supervisor and the earlier probes. **Not refereed.** Run 2026-10-12, 12:28Z to about 12:50Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R3-4/`:
- `r34_checks.py` and `r34_checks.out`: all arithmetic and the small numerical checks, sections [1]–[7].

**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `TESTS.md`, Campaign C5, lines 2302–2704, including R3-4 at 2696–2704.
- `agents/C5_O5_synthesis.md`: §0, F7–F8, §2.0–2.6.
- `SUMMARY.md` §§15–21.
- `PRICE_NOTE.md` §1, §5, and the v6 delta with its wrap-up additions.
- `agents/C5_O4_referee.md` and `agents/C5_O2_referee.md`.
- The R2-3 worker report, `scratchpad/C5/R2-3/R2-3_report.md`.
- Its codex verdict, `scratchpad/C5/ref_R2-3/REFEREE_VERDICT.md`.

**R2-3 referee status has changed since registration.** `TESTS.md:2696` says the R2-3 referee "is still running". It has returned: **NOT CONFIRMED, so R2-3 is INCONCLUSIVE** (`REFEREE_VERDICT.md:1-3,21`). Three parts of that verdict matter here:
- Lemma Q is not proved (`:9`). Nothing below relies on it.
- E4 (non-local gravitational dressing) and covariant collective or coloured collapse laws are "genuine unclosed routes" (`:21`).
- E1 violates the global-Einstein reading of (b), E2 abandons the supplied graviton, and E3 is not a collapse law (`:21`).

**Prior art (each counted once).**
- R2-3 §7, the E1–E4 list (`R2-3_report.md:241-262`), and the referee's open list (`REFEREE_VERDICT.md:7,21`).
- O4's category IV: gravity sourced only through recorded matter. The O4 report says a BMV-type experiment would refute it, and that the Oppenheim trade-off binds it (`agents/C5_O4_report.md:194-197`).
- The O4 referee: gravity-mediated entanglement (GIE) has **not** been observed, and a 2026 assessment calls direct experiments beyond present capability (`agents/C5_O4_referee.md:19`).
- The block-56 formation note. A records-only source changes the static boundary flux; a ledger-preserving replacement keeps the monopole and moves the dipole (`docs/ADMISSIBILITY_RULE_WHAT_A_FORMATION_EVENT_DOES_TO_THE_LEDGER_AND_TO_THE_FAR_FIELD_THE_MONOPOLE_NEVER_JUMPS_THE_DIPOLE_DOES_BOUNDED_THEOREM_NOTE_2026-09-21.md:24`). This is the lattice analogue of E4's acausal update of the monopole and dipole.
- The lattice Page–Geilker discriminator T4 (`docs/ADMISSIBILITY_RULE_FORMING_ONE_RECORD_KEEPS_THE_LEDGER_ONLY_AT_A_PRICE_ONE_PRICE_SERVES_EVERY_SITE_ONLY_WITH_THE_AMBIENT_AT_INFINITY_AND_A_SOURCE_IN_TWO_PLACES_SEPARATES_THE_READINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md:250`).
- `docs/GRAV_DECOHERENCE_DERIVED_NOTE.md`: a conditional Diósi–Penrose/BMV arithmetic companion, not a premise.
- A grep at 12:31Z found no repository hits for Juárez-Aubry, Tilloy, Bohm–Dirac or Donnelly–Giddings. Oppenheim appears only in O4.

**Labels.**
- **proved:** a proof is given here, under the stated hypotheses.
- **checked:** arithmetic or a numerical check in `r34_checks.out`.
- **suggested:** argued, not proved.
- **reading:** an interpretation or a price comparison.
- **comparator:** literature. *RECALLED* means from memory. *Web-checked* means confirmed at abstract or summary level during this run.

---

## 0. Verdict in plain words

**Why set A needs an escape at all.**
- Set A's records are rare collapse "flashes" on a continuum (A4), plus a supplied quantum graviton (A5) (`C5_O5_synthesis.md:327-328`).
- A flash changes matter's energy and momentum at one place. Einstein's equations need a conserved source.
- So something has to give. R2-3 listed four ways out; its referee left E4 and collective collapse laws unclosed.

**What this probe adds: one theorem that sorts the escapes.**
- **Lemma P (proved, §2).** Suppose:
  - Einstein's equations, ordinary or unimodular, hold globally (no resets);
  - whatever pays for a flash starts out in its ground state.

  Then a flash can never raise matter's energy. It can change matter's momentum only by *losing* at least |Δp|c of energy, which is carried off by other fields.
- **Every localization does the opposite.** Localizing a ground state raises its energy in every branch (checked), and the R2-3 flash class raises the mean energy on every state (Lemma H, refereed in its narrow form).
- **So a collapse-type record law has exactly three options:**
  1. re-solve gravity's initial data on a spacelike slice at each flash, which is acausal (E1, E4);
  2. draw the energy from a pre-existing reservoir (E5, below);
  3. drop the quantum gauge graviton (E2).

  The fourth way out is E3: records that never act back on the quantum state, so the flash's energy change is identically zero.
- **Lemma F (proved, §2).** A reservoir in a Lorentz-invariant state behaves like Λ, and Λ can absorb only gradients. So any reservoir that pays for localized flashes picks out a rest frame in its state.

**Each escape against the FIXED readings** (`TESTS.md:2699-2702`):

| Escape | Reading | Main prices | What would decide it |
|---|---|---|---|
| **E1.** Metric jumps on collapse surfaces (Juárez-Aubry–Kay–Miramontes–Sudarsky) | **VIABLE**, conditional on JKMS's conjectured well-posedness | The metric is classical (A5's quantum graviton is lost). Einstein's equations hold only between collapses. The collapse foliation has no published covariant selection rule (abstract-level check). **Superluminal signalling in principle, of O(1) size** (proved toy, §3). Schrödinger–Newton self-gravity | GIE (E1 predicts none). Primordial B-modes (strongly suppressed; comparator) |
| **E2.** Classical or classical–quantum gravity (Oppenheim et al.; Tilloy–Diósi; Tilloy's massive flashes) | **OPEN for set A.** Inside it: ultra-local continuous Newtonian CQ is **EXCLUDED** (32 decades); non-local and discrete CQ, Tilloy–Diósi and massive flashes are **VIABLE** in Newtonian windows (comparator) | A5 is dropped: the metric is classical and diffuses. The relativistic GR version has been proposed but not tested against GW170817 or lensing | GIE. The squeeze between torsion balances and interferometry. B-modes |
| **E3.** Bell-type beables with a guidance foliation | **VIABLE** | A beable layer and a guidance law (a formation rule the axioms leave open). A foliation, which can be determined by Ψ to keep covariance in law. The records are a dense history, not rare flashes. No metric beable at the nonlinear level | Nothing, in quantum equilibrium. It predicts GIE, as quantum gravity does |
| **E4.** Kraus operators dressed to spatial infinity | **VIABLE** (observationally) | **One spacelike slice per flash**, forced by Lemma P. Kraus operators non-microcausal at O(G) (comparator). Einstein's evolution equations fail at each flash, though the constraints hold. Possible in-principle signalling through state-dependent heating (suggested). All of A4's collapse bounds | Nothing at current sensitivity: the acausal updates are ≤ 1e-33 m s⁻² at 1 m (checked) |
| **E5.** A positive-energy reservoir (the referee's "compensating source") | **OPEN** | A new gravitating classical medium with a frame in its state (Lemma F). No construction is known. A radiation-like medium is marginal at GRW rates (factor 0.8–1.6 against the ΔN_eff budget) and excluded at the Earth-heat maximum. A cold, clustered medium is ample | A construction, then cosmological and local bounds |

**Cheapest and still viable: E3** (reading; the price count is in §5).
- It adds no observable effect beyond unitary quantum field theory plus linearized quantum gravity.
- It keeps A5, exact constraints and Einstein's equations everywhere.
- It removes F7's record budget entirely: O4's "records copy, never measure" becomes exact.
- Its price is a guidance law plus a foliation that can be state-determined and is invisible in equilibrium.

**If set A keeps collapse flashes (A4 as written), the cheapest VIABLE escape is E4.** E5 would be cheaper if it could be constructed.

**What this means for set A** (reading). Every surviving option puts a frame somewhere:
- slices chosen by the state (E1, E4);
- a frame in a reservoir's state (E5);
- a guidance foliation (E3).

Lorentz invariance in law survives only with state-determined frames. Only in E3 is that frame operationally invisible. The mandatory reading of R2-3 stands: the records do no gravitational work in E3 and E4, and in E1 and E2 they do work only by replacing the quantum graviton.

---

## 1. Hypotheses and scope (stated before the title)

**Set A, as in O5 §2.1.** The prices A1–A6 are listed at `C5_O5_synthesis.md:322-329`:
- Minkowski base;
- matter as a local relativistic QFT;
- A4: records are flash-like, covariant in law, rare and coarse;
- A5: a supplied linearized graviton.

**What gravity has to obey.**
- **(H-grav.)** The linearized Einstein equation, or its trace-free (unimodular) form, as in R2-3 §1.
- Two coupling forms: **(S)** classical per realization, through a stress expectation; **(Q)** quantum, through constraints.

**The bounds used** (the registered budget, `TESTS.md:2536-2541`, plus the gravity-specific ones):
- Collapse window. R2-3's refereed heating and definiteness numbers (`REFEREE_VERDICT.md:11,17`): Earth-heat allowance 2.64e-11 s⁻¹ in R2-3's convention, or 5.3e-11 s⁻¹ in O4's half-energy convention; GRW rates pass every heating bound.
- Page–Geilker (1981): semiclassical gravity without collapse is excluded (comparator, RECALLED; lattice analogue at the T4 note cited above).
- GW170817: c_T is within 1e-15 of c.
- Interferometry and torsion-balance squeezes of classical–quantum gravity (Oppenheim et al. 2023, web-checked).
- GIE: not yet observed (`C5_O4_referee.md:19`).
- Primordial tensor modes: r < 0.036 (BICEP/Keck 2021; RECALLED).

**Outside realizations this scope excludes.**
- Nonlinear GR beyond the O(G⁰) energy balance of Lemma P.
- Retrocausal or two-boundary record laws.
- Pearle-type tachyonic or non-local noise. The referee flagged it for Lemma V (`REFEREE_VERDICT.md:19`). Lemma P's corollary (C2) covers only local Kraus operators.
- Non-equilibrium Bohmian dynamics.

---

## 2. Two lemmas that sort the escapes

### Lemma P: no causal compensation from the vacuum (proved)

**Hypotheses.**
- **(P1) A global solution exists.** In each realization, a linearized metric solves the linearized Einstein equation globally as a distribution, or its unimodular form, which allows an extra source ∂^νΛ.
  - The source is T_m + T_o: matter (an expectation in the conditional state, or a stress built from flashes) plus any other non-gravitational fields o.
- **(P2) Localized change.** The flash's change to the stresses has compact spacetime support, or decays fast enough in every direction. This covers rGRWf flashes on localized bodies. Surface jumps on a whole slice are R2-3's Lemma B, which the referee confirmed in its core (`REFEREE_VERDICT.md:5`).
- **(P3) No reservoir.** The fields o are in their ground state before the flash, and they obey the spectrum condition: the 4-momentum of any state, measured from the ground state, lies in the closed forward cone V̄₊.
- **(P4) Order counting.** The gravitational field's own energy-momentum is O(G). It cannot balance an O(G⁰) change in matter's momentum, which is the case for flashes (Δp ~ ħ/r_C).

**Statement.** Let ΔP_m be the change in matter's total 4-momentum across one flash, in one realization. Then **ΔP_m ∈ −V̄₊**:
- the flash cannot raise matter's energy;
- it can change matter's momentum by Δp only if matter loses at least |Δp|c of energy, which is radiated into o.

**Proof.**
- The linearized Bianchi identity, ∂_μG^{μν}_lin ≡ 0, forces ∂_μ(T_m + T_o)^{μν} = 0. In the unimodular case it forces ∂^νΛ/8πG instead.
- In the unimodular case, the current is supported in a compact region K (P2). So ∂Λ = 0 on the connected exterior of K in ℝ⁴, Λ takes one value before and after the flash, and the gradient term integrates to zero.
- Integrate the conservation law over the slab between a Cauchy slice before the flash and one after it. Decay removes the side terms. So ΔP_m + ΔP_o = 0.
- By (P3), P_o is zero before the flash and lies in V̄₊ after it. So ΔP_o ∈ V̄₊, and ΔP_m = −ΔP_o ∈ −V̄₊.
- By (P4), the gravitational field's own stress cannot take up the difference at O(G⁰). ∎

**Corollaries.**
- **(C1) The R2-3 flash class fails (proved).** Every Π_pos flash law of R2-3 violates (P1)–(P4).
  - Lemma H gives E[ΔE_m] = λ(ħ²/2m)∫|∇f|² > 0 on every state, within its refereed nonrelativistic scope (`REFEREE_VERDICT.md:9`).
  - So some realization of positive probability has ΔE_m > 0.
  - The check reproduces Lemma H's mean: 0.125000 against 0.125 at r_C = 1, and 1.388856 against 1.388889 at r_C = 0.3 (`r34_checks.out` [1]).
  - In a "hot" two-packet state, individual branches can lose energy (minimum −4.40), but the mean still rises by the c-number.
- **(C2) Relativistic matter on the vacuum fails too (proved under standard hypotheses).**
  - Assume a local QFT with a unique vacuum Ω and the spectrum condition.
  - Ω is separating for local algebras (the Reeh–Schlieder context, `agents/C5_O2_referee.md:19`). So KΩ ∝ Ω forces K ∝ 1.
  - Any other vector has energy strictly above the vacuum's, because the only zero-energy vectors are multiples of Ω.
  - So every non-trivial local Kraus operator raises the energy in its branch when it acts on the vacuum.
  - The same holds on the ground state of a nonrelativistic system: every branch of a Gaussian localization of the oscillator's ground state raises its energy. The minimum gain is +0.0417 at r_C = 1 and positive for all three r_C tested (`r34_checks.out` [1]).
  - This replaces Lemma H's quadratic-dispersion restriction, which the referee noted (`REFEREE_VERDICT.md:9`), for the vacuum and ground-state sector.
- **(C3) The classification (proved, under P1–P4).** A localizing record law that keeps A5 must do one of the following:
  - break (P1) by re-solving Cauchy data on a slice (E1, E4);
  - break (P3) with a pre-existing reservoir (E5);
  - drop the gauge graviton (E2);
  - have ΔP_m ≡ 0, i.e. no back-action at all (E3).

**Relation to the R2-3 referee.**
- The referee left open "metric resets, an additional collapse-field stress, or another compensating source" (`REFEREE_VERDICT.md:7`).
- Lemma P narrows that list:
  - a compensating source **born from the vacuum** cannot work;
  - only a **pre-existing positive-energy reservoir** can;
  - metric resets must be **acausal re-solutions on a slice**.
- Lemma P is a per-realization statement about expectation values (S-type). It does not use Lemma Q's operator identity. Its operator version (Q) is suggested only.

### Lemma F: a reservoir carries a frame in its state (proved, elementary)

**Statement.** If the reservoir's state is Lorentz-invariant, it cannot pay for localized flashes. A reservoir that does pay for them therefore has a rest frame in its state.

**Proof.**
- The only symmetric 2-tensors invariant under SO⁺(1,3) are multiples of η. So an invariant state has ⟨T_o⟩ = ρη: it is Λ-like.
- Its exchange current with matter is then ∂(ρη) = ∂ρ, a gradient. For a localized exchange this integrates to zero, as in the proof of Lemma P. So it can pay for no ΔP_m ≠ 0. ∎
- **Hence:** a reservoir that pays for localized flashes has a non-invariant stress in each realization. For a type-I stress that means a timelike eigenvector, a rest frame, in the state. Lorentz invariance in law is untouched.

**Consistency with R2-3.** Josset–Perez–Sudarsky's homogeneous Λ(t) is exactly the invariant-state reservoir. It absorbs only the homogeneous mean, in agreement with R2-3's Lemma B′ (`REFEREE_VERDICT.md:5`).

---

## 3. E1: metric jumps on state-chosen Cauchy surfaces

**What it is** (comparator, web-checked at abstract level: Juárez-Aubry, Kay, Miramontes and Sudarsky, JCAP 01 (2023) 040, arXiv:2205.11671).
- Between collapses, the semiclassical Einstein–Klein–Gordon equations hold.
- Collapses happen on random, non-intersecting Cauchy surfaces.
- Well-posedness of the initial-value problem, with and without collapses, is **conjectured**, not proved.
- The abstract gives no covariant rule for choosing the surfaces. Whether the full text supplies one was not checked.

**Superluminal signalling of O(1) size. Proved (elementary toy).** Comparator: Bahrami, Großardt, Donadi and Bassi, NJP 16, 115007 (2014), web-checked summary: semiclassical gravity "together with the standard collapse postulate … gives rise to superluminal signalling".
- **Setup.** Alice's mass m is in |L⟩ + |R⟩, entangled with Bob's qubit. Charlie, near Alice, reads the classical metric.
- **Under conditional-⟨T⟩ sourcing:**
  - if Bob measures Z, Charlie's field is g_L or g_R, each with probability ½;
  - if Bob measures X, Alice's mass stays in a superposition, and the field is g_mean with certainty.
- **These are distinguishable in a single shot**, with total-variation distance 1 for a reading that resolves the two fields.
- **Under linear sourcing (E3, E4),** Charlie's reduced state is the same 50/50 mixture for both of Bob's choices. No signal.
- **Numbers** (checked, `r34_checks.out` [2]):
  - m = 1e-14 kg, d = 1 µm, r = 10 µm gives |g_L − g_mean| = 6.7e-16 m s⁻².
  - Alice's own GRW collapse time is 1.7e3 s at λ = 1e-16 s⁻¹, and 1.7e-2 s at λ = 1e-11 s⁻¹.
  - So a signalling window exists in principle everywhere in the collapse window.
- **Reading.** The signal runs along the collapse surfaces, so the collapse foliation is detectable in principle. Operationally, that undoes set A's motive: an unobservable frame.

**Bounds.**
- Page–Geilker: passed, because macroscopic pointers collapse fast (comparator).
- Collapse heating and interferometry: R2-3's window (`REFEREE_VERDICT.md:11,17`).
- Schrödinger–Newton self-gravity of mesoscopic packets: not yet tested experimentally (RECALLED).
- GIE: E1 predicts none.
- Primordial B-modes: León, Majhi, Okon and Sudarsky (arXiv:1607.03523, PRD 96; web-checked) find the B-mode spectrum "strongly suppressed" under semiclassical gravity with collapse. That is consistent with r < 0.036 today, and a future detection would weigh against E1.
- **No stated bound is violated.**

**Reading: VIABLE, conditional on JKMS's conjectures.**

**Prices.**
- A5 is replaced by a classical metric.
- Einstein's equations hold only between collapses (R2-3 referee, `:21`).
- A collapse foliation, without a known covariant rule.
- O(1) in-principle signalling.
- Schrödinger–Newton nonlinearity.

---

## 4. E2, E3, E4 and E5

### E2: classical, or classical–quantum, gravity

**Comparator, web-checked.**
- **Oppenheim, Sparaciari, Šoda and Weller-Davies, Nat. Commun. 14, 7910 (2023).**
  - The decoherence–diffusion trade-off, applied to Newtonian classical–quantum gravity.
  - The page text was fetched and is partly garbled. Its Table 1, as read (window widths: `r34_checks.out` [5], checked):

    | Model | Upper bound | Lower bound | Window |
    |---|---|---|---|
    | Ultra-local continuous | 1e-41 kg² s m⁻³ | 1e-9 kg² s m⁻³ | **empty by 32 decades** (EXCLUDED) |
    | Non-local, Diósi–Penrose-type kernel | l_P²D₂ ≤ 1e-9 kg² s m⁻¹ | l_P²D₂ ≥ 1e-35 kg² s m⁻¹ | 26 decades open |
    | Discrete-jump models | — | — | 24 decades open |

  - The paper's own words: "classical–quantum theories of Newtonian gravity with ultra-local continuous noise are ruled out by experiment", and "discrete theories of classical gravity are not ruled out".
- **Tilloy–Diósi feedback.** Gaona-Reyes, Carlesso and Bassi (PRD 2021, arXiv:2007.11980) find that the simplest generalizations of KTM are inconsistent or excluded, and that TD is "the only viable" full-Newtonian feedback implementation under the simplest conditions.
- **Tilloy's GRW with massive flashes** (PRD 97, 021502, arXiv:1709.03809). The abstract says it is "in agreement with known experimental data" and falsifiable for all values of its parameters. It cuts off 1/r below about 1e-7 m, and its gravitational decoherence goes as 1/λ_GRW.
- **GPSL** (arXiv:2602.19377, 2026) sets lower bounds on the parameters; the abstract implies a window remains (suggested).

**Relativistic status.**
- Oppenheim and Weller-Davies propose a manifestly covariant classical–quantum path integral for GR (arXiv:2302.07283). Complete positivity is proved for the general framework; the GR theory is "a candidate" (web-checked abstract).
- A Nordström version exists (arXiv:2401.05514).
- Grudka et al. (arXiv:2402.17844) relate the theory to quadratic gravity. Complete positivity favours a scale-invariant version (web-checked summary).
- **Correction to R2-3.** R2-3 says a covariant version is "known only for Nordström" (`R2-3_report.md:249`, RECALLED). That is out of date: a covariant GR proposal exists, but it is untested.
- Not established anywhere I found: that this proposal reproduces Newtonian 1/r and GW170817's c_T to 1e-15 with two TT polarizations, inside the trade-off windows.

**Reading: OPEN for set A** (set A needs a covariant law). Inside it:
- the ultra-local continuous Newtonian sub-model is EXCLUDED (comparator);
- the non-local and discrete classical–quantum sub-models, Tilloy–Diósi and massive flashes are VIABLE in the Newtonian regime (comparator).

**Prices.**
- A5 is dropped: the graviton is a classical stochastic field.
- An irreducible pair of metric diffusion and gravitational decoherence.

**Reading.** E2 is the one escape in which records and gravity are the same thing. The classical metric, or the flashes of the massive-flash model, is the record channel: O4's category IV, with "only records are readable" applied to the source of gravity.

**What would decide it.**
- GIE. A local classical theory cannot entangle (Oppenheim–Weller-Davies abstract). The caveat is Trillo and Navascués (PRD 2025; arXiv:2411.02287), who claim the Diósi–Penrose model does entangle. That claim is disputed (arXiv:2503.19774).
- B-modes.
- Tightening the squeeze.

### E3: Bell-type beables with a guidance foliation

**Hypotheses.**
- Ψ evolves unitarily: QFT plus quantized linearized gravity, so A5 is kept.
- The beables (a configuration, with the jump events of Bell-type QFT) are guided by Ψ along a foliation.
- Quantum equilibrium holds.

**Bounds.**
- Predictions equal those of unitary QFT plus linearized quantum gravity for every outcome recorded in the configuration (comparator, RECALLED: Dürr–Goldstein–Münch-Berndl–Zanghì 1999 hypersurface Bohm–Dirac; Dürr–Goldstein–Tumulka–Zanghì Bell-type QFT).
- So there is:
  - no heating;
  - no extra decoherence;
  - no flash noise;
  - nothing new in lensing (F6).
- F7's record budget is empty. F8's non-locality sits in the guidance law, with no signalling in equilibrium.
- Records exert no back-action on Ψ, so ΔP_m ≡ 0 at the level of Ψ. The constraints and the Bianchi identity hold exactly, as operator identities.

**Reading: VIABLE.**

**Prices.**
- **Record.** The records become a beable history that never acts on Ψ. This is O4's P4′ ("records copy, never measure") made exact, where O4 had it only as a sufficient policy (`C5_O4_referee.md:38`). "Records form … permanent" is read as jump events plus a configuration history (reading).
- **Formation rule.** A guidance law, or jump rates, is supplied. This fills the open gate "the remaining formation rules" (`MINIMAL_AXIOMS_2026-06-29.md:184-186`). It is not a change to axiom text (reading).
- **Foliation.**
  - Either a preferred one: absolute structure, invisible in equilibrium.
  - Or one determined by Ψ: Dürr, Goldstein, Norsen, Struyve and Zanghì, Proc. R. Soc. A 470, 20130699 (2014), web-checked abstract. Existence for general interacting QFT is not established (RECALLED).
  - It touches the time-metric open gate (`:185`).
- **Dense, not rare (suggested).**
  - Independent flashes sampled from a unitary Ψ show every branch. That is the many-worlds flash and mass-density theory of Allori, Goldstein, Tumulka and Zanghì 2011 (RECALLED).
  - So definite outcomes need a beable that tracks one branch over time: a dense history.
  - A4's "rare and coarse" wording then changes to "non-disturbing". Discreteness survives only in the jump events.
- **No metric beable beyond linear order (suggested).** Bohmian metric trajectories depend on the foliation (Shtanov 1996; Pinto-Neto and Struyve; RECALLED). So the metric stays in Ψ. That is fine for linearized gravity on set A's Minkowski base. The nonlinear and cosmological E3 is OPEN.

**What would decide it.** Nothing in equilibrium. E3 predicts GIE and the standard tensor modes.

### E4: Kraus operators dressed to spatial infinity

**Comparator.** Donnelly and Giddings, PRD 93, 024030 (2016), arXiv:1507.07921 (web-checked summary):
- dressed operators are gauge-invariant;
- their commutators fail at spacelike separation at O(G).

The R2-3 referee lists the narrower dressing theorem (`REFEREE_VERDICT.md:9`).

**What Lemma P forces.**
- Heating flashes (C1, C2) cannot be dressed causally.
- So the dressing must reach spatial infinity on a chosen Cauchy slice, and the ADM charges change at once on that slice.
- **One slice per flash is therefore necessary, not optional (proved via C3).**
- The constraints hold; the evolution equations fail at each flash (a jump in the Cauchy data).

**Sizes** (checked, `r34_checks.out` [3]):
- A flash on one nucleon changes the ADM mass by 5.5e-45 kg.
- The Earth's flash heating raises its ADM mass at 2.0e-9 kg s⁻¹ at the GRW rate, and at 5.2e-4 kg s⁻¹ at the Earth-heat maximum.
- Localizing a pointer of 1e10 nucleons over 1 µm moves the far field by 1.1e-33 m s⁻² at 1 m in each outcome. The average change is zero, because collapse is a martingale, so it carries no signal.

**Signalling (suggested).**
- If a flash's energy change depends on the local state, a choice by Bob changes the monopole at spacelike-separated points on the slice. Examples: relativistic dispersion (Lemma H's c-number needs quadratic dispersion), or converting flashing matter into massless quanta, which do not flash.
- Size for 1e27 particles over 1 s: 3.7e-44 m s⁻² at 1 m.
- It is unmeasurable, but it makes the slices operationally real in principle. It vanishes for laws in which every species heats at a state-independent rate.

**Bounds.** Nothing beyond A4's collapse window. A5's quantum graviton is kept, so E4 predicts GIE and the standard tensor modes.

**Reading: VIABLE (observationally).**

**Prices.**
- One slice per flash: a state-chosen foliation at best, touching the time-metric gate.
- A formation rule that is non-microcausal at O(G). This conflicts with A3's "microcausal local rule" (`C5_O5_synthesis.md:326`).
- Einstein's evolution equations fail at each flash.
- A4's heating window and collapse bounds.
- The suggested signalling caveat.

### E5: a pre-existing reservoir (referee-flagged; not in R2-3's list)

**Structure.**
- By Lemma F, any reservoir that pays causally has a frame in its state.
- It must also be classical and stochastic (a hybrid): a unitary quantum reservoir gives decoherence, not collapse.

**Numbers** (checked arithmetic; the ΔN_eff and dark-matter inputs are RECALLED; `r34_checks.out` [4], [7]):
- **A static store inside the Earth** would need 2.3e4 J m⁻³ at the GRW rate. Its own gravity is negligible against the Earth's.
- **Spread uniformly through the universe,** that store would be 13 decades above ρ_crit c². So a universe-wide static store is excluded (suggested).
- **A dark-radiation medium,** capped by ΔN_eff ≤ 0.3, can deliver at most 2.1e-7 W m⁻². The Earth needs 3.5e-7 W m⁻² in R2-3's convention, or 1.7e-7 W m⁻² in O4's. That is marginal at the GRW rate, and short by a factor of 4e5 at the Earth-heat maximum.
- **A cold medium clustered at the local dark-matter density** carries 3.7 W m⁻² of rest energy, which is ample.
- **Emission-type flashes funded by rest mass** (E5′). These must emit at least |Δp|c ≈ 2.4 eV per flash at r_C = 1e-7 m. That is 1.4e17 W for the Earth at the GRW rate, 3,000 times its heat flow, unless the emitted quanta are invisible. And since an emitted quantum decoheres rather than collapses, E5′ falls back to E3 or to a regress (suggested).

**Reading: OPEN** (no construction exists).

---

## 5. Ranking (reading)

Prices are counted against set A's A1–A6 and the axiom text. Observational exposure means effects beyond unitary QFT plus quantum gravity.

| Rank | Escape | Keeps A5 and global Einstein? | New structure | Frame | Observational exposure |
|---|---|---|---|---|---|
| 1 | **E3** | yes, both | Beable layer; guidance law (fills an open gate) | Foliation; can be determined by Ψ; invisible in equilibrium | none |
| 2 | **E4** | A5 yes; Einstein only between flashes | Dressed Kraus operators (O(G) non-microcausal) | One slice per flash (forced); visible in principle only through the energy channel (suggested) | A4's collapse window |
| — | **E5** (OPEN) | yes, both | A gravitating classical medium | In the reservoir's state (Lemma F) | Medium bounds, uncomputed |
| 3 | **E1** | no, and no | Classical metric; well-posedness conjectured | Collapse surfaces; visible in principle at O(1) | Collapse window; B-modes; GIE |
| — | **E2** (OPEN for set A) | no | Classical stochastic metric | Newtonian or ADM forms; the covariant GR form is untested | The trade-off squeeze; GIE |

---

## 6. Against the registered expectation (`TESTS.md:2704`)

- **"CQ gravity is constrained but viable in a window."**
  - Confirmed for Newtonian non-local and discrete classical–quantum gravity, Tilloy–Diósi and massive flashes.
  - Ultra-local continuous classical–quantum gravity is already excluded.
  - For set A, which needs a covariant law, E2 is **OPEN**: the covariant GR proposal is untested.
- **"Metric jumps are viable but need a foliation."**
  - Confirmed, conditional on JKMS's conjectures.
  - Two prices were not registered: an O(1) in-principle signalling (§3), and the loss of A5's quantum graviton.
- **"Beables are viable with a foliation (a preferred frame in the guidance law only)."**
  - Confirmed, and E3 is the cheapest.
  - The foliation can be determined by Ψ.
  - Not registered: E3's records must be a dense history, not rare flashes, and the metric cannot be a beable beyond linear order.
- **E4 was not in the expectation.** It is VIABLE observationally, and its slice per flash is now proved necessary (Lemma P, C3).

---

## 7. For the referee

- **Lemma P.**
  - The slab integration, and the compact-support step for the unimodular gradient.
  - The spectrum-condition step for o.
  - The O(G) order counting that excludes gravitational self-energy from the balance.
  - Whether (P2) holds for rGRWf hyperboloid flashes on localized bodies.
- **(C2).** Whether the separating property of the vacuum, together with its uniqueness, gives a strict energy increase for every non-scalar local Kraus operator.
- **Lemma F.** The step from invariant tensors to a frame needs a type-I stress.
- **E1 toy.** Whether JKMS's sourcing is by the conditional-state ⟨T⟩. The abstract says semiclassical evolution between collapses; I did not read the full text.
- **E4 signalling.** The suggestion is that a relativistic flash law heats at a rate that depends on the state.
- **Oppenheim Table 1.** The fetched text is partly garbled, and their convention names D₀ the decoherence coupling and D₂ the diffusion coupling.
- **Correction to R2-3.** R2-3's "covariant CQ only for Nordström" is corrected in §4.
- **Ψ-determined foliations.** Their existence for interacting QFT.
- **Heating convention.** R2-3's 3ħ²/(4mr_C²) is twice O4's figure (`REFEREE_VERDICT.md:11`). Both conventions are given in E5's numbers.

**Sources (web-checked this run, at abstract or summary level).**
- [Oppenheim et al., Nat. Commun. 14, 7910 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10696068/); [arXiv:2203.01982](https://arxiv.org/abs/2203.01982)
- [Juárez-Aubry, Kay, Miramontes, Sudarsky, arXiv:2205.11671](https://arxiv.org/abs/2205.11671)
- [Bahrami et al., arXiv:1407.4370](https://arxiv.org/pdf/1407.4370)
- [Gaona-Reyes, Carlesso, Bassi, arXiv:2007.11980](https://arxiv.org/pdf/2007.11980)
- [Tilloy, arXiv:1709.03809](https://arxiv.org/abs/1709.03809)
- [GPSL, arXiv:2602.19377](https://arxiv.org/abs/2602.19377)
- [Oppenheim and Weller-Davies, arXiv:2302.07283](https://arxiv.org/abs/2302.07283)
- [Grudka et al., arXiv:2402.17844](https://ar5iv.labs.arxiv.org/html/2402.17844)
- [Dürr et al., arXiv:1307.1714](https://arxiv.org/pdf/1307.1714)
- [Donnelly and Giddings, arXiv:1507.07921](https://alphaxiv.org/abs/1507.07921)
- [Trillo and Navascués, arXiv:2411.02287](https://arxiv.org/pdf/2411.02287); [reply, arXiv:2503.19774](https://arxiv.org/pdf/2503.19774)
- [León et al., arXiv:1607.03523](https://arxiv.org/pdf/1607.03523)
- [Majorana Demonstrator, arXiv:2202.01343](https://arxiv.org/abs/2202.01343). The abstract gives no numeric λ; not used.
