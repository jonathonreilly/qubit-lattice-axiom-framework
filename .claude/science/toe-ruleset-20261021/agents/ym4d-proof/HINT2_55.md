Reviewer model: claude-opus-5-5

# HINT2_55 — the non-freeness witness, repaired: the comparator side for the observable actually used, the Yang–Mills side as named bounds, and the soft-branch inputs

Worker file (Opus 5.5, worker role; the binding rules of REVIEW_BRIEF_55 apply). This worker writes only this file and
`checks/h2_55_*` (the pre-existing `checks/h2_{constfield.py,criteria.md,out.txt,time.txt}` belong to an older, unrelated
HIST.md check and are not touched). No git. Append-only after this PRE-STATED block. Labels: **PROVEN-HERE** (complete
argument written here), **CONDITIONAL** (implication proven here; every input named with owner file and owner's status),
**ARGUED** (reason given, hole named), **OPEN**, **IMPORTED-standard** (textbook fact, named, not re-derived), **[m]**
(literature from memory, not re-read). Statuses quoted from other files are those files' labels unless this file says it
re-derived them. Line numbers drift; citations carry a locating string.

## PRE-STATED (written 2026-10-29T01:51:41Z UTC, before any criteria file, script or written derivation of this file)

*Provenance.* Before this block I read: REVIEW_BRIEF_55 (all); HINT55.md (all 603 lines); CODEX_REVIEW_HINT.md (all 293
lines, including "Exactly what may be banked"; its last line is complete); UIR55.md (all; it is still at its PRE-STATED
block); FLOW55.md §0-§1 and §7-§12; CODEX_REVIEW_FLOW55.md (its verdict lines and "Exactly what may be banked", by grep).
Exploratory reasoning, not written down, preceded this block. It covered: the pairing formula for the one-point function of
the comparator's quadratic energy density; a matrix-valued (colour) spectral class; a scalar generalised-free-field example
of a non-canonical identification; and a preliminary hand evaluation of the order-e⁴ ultraviolet logarithm of ⟨E(t)⟩ for a
centred Gaussian su(N) connection pushed through the NONABELIAN flow (preliminary value: −Nξe²/(16π²)·log(t/s₀) times the
tree value, ξ the Gaussian's gauge parameter). That value is a hypothesis to be tested here, not a result.

*Symbol pins (systemic defect 1), fixed now.* t = continuum flow time; f_ω(t) := t²ω(E(t,0)); 𝓔 := t²E. e_a, e² =
comparator couplings (not the lane's E_k, E_2, not Euler's e — written exp where needed). ξ = gauge parameter of a Gaussian
connection's covariance (δ − (1−ξ)p̂p̂)/p²; α₀ = gauge-fixing parameter of the flow (Lüscher's). M = a positive semidefinite
COLOUR matrix (not FLOW's M-cubes, not Balaban's M). (F-tune), β_±, R_F, U_±(m), u_k, m := K − k, t^{(m)} := c_tL^{−2m} as in
HINT55 §"Symbol table". (UIR^♮), (UNIV-1L), (SF-g), (RLF-δ), (SF-cont), (SF-∞) as in FLOW55 §0/§8.

**Targets.**
- **T1 (comparator side covers the observable as realised).** (a) The exact one-point formula for the comparator's flowed
  energy density, for ANY law (Gaussian or not) with finite second moments and any positive semidefinite colour metric — the
  correct argument for a one-point function of a composite, not a composite Källén–Lehmann statement. (b) Repair the
  unequal-colour normalisation: a colour class defined by matrix-valued (or every-positive-contraction) spectral data, closed
  under every linear colour map; show Codex's counterexample is excluded; transfer KLM, UV-D, SEP. (c) Exact f(t) and its
  t-dependence for canonical Maxwell fields with any colour coupling matrix, Proca fields with colour-dependent masses,
  generalised free fields, contact representatives, and mixtures. (d) Coverage of every Euclidean representative whose
  linear-field two-point function agrees with a class member at non-coincident points. (e) "Free nonabelian-colour fields":
  decide whether the nonabelian flowed density is an observable of a free abelian theory; compute (or fail to compute) the
  order-e⁴ logarithm for the Gaussian-connection realisation and its α₀-independence. (f) State what no one-point witness
  can do (identification; bounded observables), with explicit examples.
- **T2 (Yang–Mills side).** Name the bounds on t²⟨E(t)⟩ at short flow time that the RG must deliver; prove
  H_int ⇐ (F-tune) + (named bounds) with every link stated (including Codex's semicontinuity correction and an inter-scale
  step for continuous t); connect (F-tune) to FLOW55's reduction ((UIR^♮) + layer-1 inputs); say which named bounds no
  existing layer-1 statement supplies.
- **T3 (soft-branch inputs).** Verdicts on (NOISE-ADD), (ANTI-♭) and its route (β)/(W-AF2_r), and whether the bare-observable
  witness or the deterministic S4c branch needs them.

**What would count as a refutation (fixed now).**
- Of the one-point formula: a law in the class, finite second moments, with ω(𝓔(t,0)) ≠ the pairing formula.
- Of the colour repair: a member of the repaired class and a linear colour map (or positive colour metric) leaving the class,
  or a member with finite ultraviolet liminf and f(t₀) > liminf.
- Of an exact value: an exact-arithmetic mismatch, or a designed-FAIL control that does not fire.
- Of the Gaussian-connection coefficient: dependence on α₀ of the logarithm of ⟨E⟩ (E is α₀-independent configuration by
  configuration, so a correct computation must give an α₀-independent coefficient), or disagreement with an independent
  re-evaluation; if I cannot make the α₀ test, the coefficient stays ARGUED.
- Of an obstruction example: failure of its positivity/reflection positivity, of its claimed monotonicity, or of its claimed
  rate.
- Of the reduction: an input used but not listed; a constant depending on the cutoff K or the torus; an input that is H_int
  restated (a lower bound on a quantity that already separates Yang–Mills from the comparator class).
- Of a T3 verdict: an explicit model in which the claimed implication fails (or holds, for a claimed failure).

**Checks planned.** Ids `h2_55_<x>`; `checks/h2_55_<x>_criteria.md` written before each script; exact rational arithmetic
(`fractions`) and exact symbolic algebra (`sympy`, pure Python) only, no floats in any verdict; nice 10; each with a
designed-FAIL control. Planned: h2_55_a (comparator one-point values, colour repair, Codex's counterexample, Proca/GFF
monotonicity at rational points), h2_55_b (Gaussian-connection order-e⁴ logarithm: tensor contractions and the
α₀-independence test), h2_55_c (obstruction examples: scalar GFF identification, wrapped-normal monotonicity),
h2_55_d (reduction arithmetic with the inter-scale step). Ids may be added; none removed.

---
