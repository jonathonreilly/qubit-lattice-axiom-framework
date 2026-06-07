# Lorentz Naturalness for a Fixed Fundamental Theory is a Computation, Not a Tuning (Framing Correction)

**Date:** 2026-06-06
**Claim type:** bounded_theorem (framing correction + tree-level pass; radiative marginal scoped uncomputed)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary declaration.
**Primary runner:**
[`scripts/frontier_lorentz_naturalness_is_a_computation_not_a_tuning_2026_06_06.py`](../scripts/frontier_lorentz_naturalness_is_a_computation_not_a_tuning_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_lorentz_naturalness_is_a_computation_not_a_tuning_2026_06_06.txt`](../logs/runner-cache/frontier_lorentz_naturalness_is_a_computation_not_a_tuning_2026_06_06.txt)

---

## Role

A `/exercise` re-examination (durable packet at
`.claude/science/exercises/lorentz-naturalness-beyond-lattice-qg/`) **corrects the
framing** of the Lorentz-naturalness obstruction
[`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
(#3123). Those notes (and the closure analysis #3126/#3129/#3131) leaned on the
**field-wide Collins–Perez–Sudarsky–Urrutia–Vucetich** (*PRL* **93** (2004) 191301)
naturalness verdict and the EFT-framing fallback "find a custodial symmetry." This
note shows that framing **imports an EFT category** (a sliding cutoff + free
couplings) the framework does **not** instantiate, and re-poses the question
correctly. Runner **12 PASS / 0 FAIL**. No new axiom.

This is a **framing correction + a tree-level pass**, not a claim that the
obstruction is solved (the radiative marginal `δv` remains uncomputed — see scope).

## (A) "Naturalness" is an EFT category the framework does not instantiate

Naturalness — *a small dimensionless ratio needs a symmetry, else it is tuned* — is
a property of EFTs with **(i)** a *sliding* cutoff and **(ii)** *free* couplings to
tune. The framework has **neither**: `a⁻¹ = M_Pl` is **fixed** (no sliding `μ`), and
the gauge coupling `g² = 2N/β = 1` is **derived** from `β=6` (no free knob). It is a
**fixed fundamental theory** that *derives* the SM parameters. Therefore "is
`c_t=c_s` natural?" is **partly a category error**: there is no coupling to tune. The
well-posed question is **"what does the framework *compute* for the species-to-species
speed difference `δv`?"** — a *falsifiable prediction*, not a tuning. (Runner Part A;
't Hooft / Wetterich: for a fixed theory, "tuning" → "prediction.")

The assumption ledger (exercise packet) makes this precise: of the Collins
argument's premises — (a) a continuum EFT is being regulated; (b) an infinite tower
of *independent* operators; (c) sliding-cutoff running; (d) the marginal coefficient
is a *free* parameter; (e) naturalness-as-objection — **(a),(b),(d),(e) fail** for a
fixed finite fundamental theory.

## (B) The tree-level prediction passes (and a near-term UHECR test)

At tree level the only Lorentz violation is the **dimension-6** (irrelevant)
operator, Planck-suppressed (the retained emergent-Lorentz result, given the
approved Planck primitive): `|δE²/E²| ~ (1/12)(E/M_Pl)²`. Runner Part B:

| observable | `E` | `|δE²/E²|_tree` | bound | safe by |
|---|---|---|---|---|
| photon (GRB/Fermi-LAT) | `10³` GeV | `5.6×10⁻³⁴` | `10⁻²⁰` | 13 orders |
| nucleon (Hughes–Drever) | `1` GeV | `5.6×10⁻⁴⁰` | `10⁻²⁷` | 12 orders |
| **UHECR** | `10¹¹` GeV | `5.6×10⁻¹⁸` | `10⁻¹⁷` | **0.3 orders** |

The tree-level prediction **passes**, and at the highest energies (UHECR) it sits
only `~0.3` orders below the bound — a **genuinely near-term falsifiable** prediction.
The marginal (dim-2) operator is *absent* at tree level on the native continuous-time
surface (#3020).

## (C) The radiative marginal is the open piece — and the `α_s/4π` is a prior, not a posterior

The marginal `δv` is purely **radiative** (the Collins regeneration). The
obstruction note's `δv ~ α_s/4π ~ 6×10⁻³` is a **generic EFT estimate substituted
in** (the note explicitly flags the O(1) coefficient and `γ` as "open inputs") — it
is **not** the framework's computation. Three framework-specific structures could
move the actual number and **none is quantified**:

1. **The shared kernel** — all species hop with the *same* `sin(p_i a)` kernel, so
   the loop integral `J` is species-independent: `δc_s^(R) = C₂(R)·g²·J`. The
   *common* part is universal (reabsorbable into the one emergent `c`). **But the
   observable species *difference* `∝ (C₂(A)−C₂(B))·g²·J` is `O(1)·α_s/4π`** — the
   Casimir differences are O(1) (quark−lepton `4/3`, gluon−quark `5/3`), so the
   shared kernel does **not** cancel it (runner Part C). It universalizes the
   unobservable common part, not the observable difference.
2. **The attractive IR flow** `(μ/M_Pl)^γ` (#3121) — genuine suppression, but `γ` on
   the *difference* over the hierarchy is unquantified.
3. **The continuous-time `c_t≡1` kinematic fixing** (#3020) — collapses the
   two-parameter gate to one spatial scalar (Reisz spatial-only power-counting),
   unquantified at loop level.

## (D) Honest status: UNCOMPUTED (not passing, not falsified)

- **Not (a) passing**: the tree-level Planck-suppression covers only the dim-6
  operator; the marginal piece is a different operator, genuinely radiatively
  generated, *not* Planck-suppressed.
- **Not (b) falsified**: `α_s/4π` is a prior, not the framework's posterior; the
  three suppressions above are unquantified.
- **Therefore (c) UNCOMPUTED** — and *high-stakes*: a fixed theory that *computes*
  `δv ~ 10⁻³` against a bound `~10⁻²⁰` would be **falsified**, not "unnatural." The
  best *current* estimate of the surviving difference is `O(1)·α_s/4π` (the shared
  kernel does not cancel it), so the computation is decisive in both directions.

## Verdict and the real next artifact

The prior "naturalness obstruction needing a new axiom or new physics" framing
**imported an EFT category** the fixed theory does not instantiate. The corrected
status: **the tree-level prediction passes (Planck-suppressed, with a near-edge
UHECR test); the radiative marginal `δv` is an uncomputed, high-stakes prediction.**
**The real next artifact is a computation** — the species-differential marginal `δv`
on the native continuous-time surface at `β=6`, including the shared-kernel
difference, the `(μ/M_Pl)^γ` flow, and the `c_t`-fixing — yielding a definite number
to compare against the bounds. The custodial-symmetry hunt (#3126/#3129/#3131) was
the **EFT-framing's fallback**; the fixed theory's **primary** task is the number.

**The owner's correction is validated**: the framework's non-EFT structure changes
the *framing* (computation, not tuning) and yields a tree-level pass — though it does
not, by itself, reduce the radiative estimate (the shared kernel does not cancel the
species difference). The honest state is "uncomputed, high-stakes," not "obstructed,
needs new physics."

## What this note does NOT claim

- It does **not** claim the obstruction is solved or that `δv` is below bounds — the
  radiative marginal is uncomputed.
- It does **not** contradict #3123/#3126/#3129/#3131 — it re-frames them: those are
  correct *as EFT-naturalness/symmetry statements*, but the fixed theory's primary
  question is the computation.
- It does **not** reduce the `α_s/4π` estimate (the shared kernel does not cancel the
  species difference).
- **No** new axiom, primitive, repo vocabulary, or class tag; the LV bounds and
  literature are comparators. It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): `g²=2N/β=1` derived (no free coupling); the tree-level
  dim-6 Planck-suppressed pass table (incl. the UHECR near-edge); the shared-kernel
  factorization `δc_s^(R)=C₂(R)g²J` with the O(1) Casimir differences (no
  cancellation of the species difference); the UNCOMPUTED status.
- **Cited** (comparator/scope only): Collins et al *PRL* 93 (2004) 191301;
  Giuliani–Mastropietro–Porta (arXiv:1107.4741, fixed-lattice emergent Lorentz);
  Bednik–Pujolàs–Sibiryakov *JHEP* 1311 (2013) 064 and Anber–Donoghue *PRD* 83 (2011)
  105027 (log-slow vs power-law); 't Hooft (1980) / Wetterich / Williams
  (arXiv:1812.08975) (naturalness vs computability); the framework's own #3123 `γ`,
  #3121 flow, #3020 dissolution, and the retained emergent-Lorentz dim-6 result.

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It does
not promote this note or change any audited claim scope.

- [LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + the approved Planck scale primitive;
(2) the framework's `β=6` SU(3) coupling (`g²=1`, derived); (3) the retained
tree-level dim-6 emergent-Lorentz result; (4) the shared `sin(p_i a)` staggered
kernel and the SU(3) Casimirs; (5) the #3123 `α_s/4π` estimate as a *prior*. The
tree-level pass is computed; the radiative marginal is scoped uncomputed.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (naturalness, EFT, sliding cutoff, Casimir, shared kernel, fixed
fundamental theory). `β=6→g²=1` is the framework's own convention; the LV bounds and
literature are comparators, not derivation inputs.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of #3123, #3126, #3129, #3131, #3121, #3020, or any upstream row. The audit
lane is the only status authority.
