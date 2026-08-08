# /exercise — Lorentz naturalness beyond lattice/QG (SUMMARY)

**Date:** 2026-06-06 · **Slug:** lorentz-naturalness-beyond-lattice-qg · **Subagents:** 5 · **Literature:** yes

## Wall (neutral)
The prior analysis (#3123 quantified obstruction, #3126 Record-can't, #3129 no-carrier-symmetry,
#3131 closure-iii-new-physics) concluded the Lorentz-naturalness gap needs a new axiom or new physics,
leaning on the FIELD-WIDE Collins (PRL 93 (2004) 191301) verdict. The owner's correction: the framework
is NOT ONLY a lattice/QG theory — it is a qubit-ontology + Record + unification theory with a FIXED
fundamental description (β=6 lattice) that DERIVES the SM parameters, not an EFT with free couplings.
Does that non-EFT structure change the verdict?

## The correction (the exercise's headline — owner was right)
"Naturalness" (a small ratio needs a symmetry, else it's tuned) is a property of EFTs with (i) a SLIDING
cutoff and (ii) FREE couplings. The framework has NEITHER: `a⁻¹=M_Pl` is fixed; `g²=2N/β=1` is DERIVED
from β=6. So **"is c_t=c_s natural?" is partly a CATEGORY ERROR** — there's no free knob to tune. The
well-posed question is **"what does the framework COMPUTE for the species speed difference δv?"** — a
falsifiable prediction. And the `α_s/4π` in the obstruction note is a generic Collins ESTIMATE
substituted in (a prior), NOT the framework's own computation (the note flags it as an "open input").

## Corrected status: UNCOMPUTED (not passing, not falsified)
- **Tree level PASSES**: the only LV is the dim-6 (irrelevant) operator, Planck-suppressed
  `|δE²/E²| ~ (1/12)(E/M_Pl)²` — `~10⁻³⁴` at LHC, `~10⁻⁴⁰` at nucleon scale, safe by 12–13 orders.
  **Bonus falsifiable prediction**: at UHECR (`E~10¹¹` GeV) it is `~5.6×10⁻¹⁸`, only **0.3 orders** below
  the bound — near-term testable.
- **Radiative marginal δv is UNCOMPUTED**: the `α_s/4π` is a prior; three framework-specific structures
  (shared kernel; the `(μ/M_Pl)^γ` attractor flow #3121; the continuous-time `c_t≡1` fixing #3020) could
  move it and none is quantified.

## What the reframe does NOT rescue (the agents held the line)
- **Shared kernel does NOT cancel the species difference** (agent 2): `δc_s^(R) = C₂(R)·g²·J` with `J`
  species-independent; the common part is universal (reabsorbable), but the OBSERVABLE difference
  `∝ (C₂(A)−C₂(B))·g²·J` is **O(1)·α_s/4π** (Casimir differences are O(1): quark−lepton 4/3, gluon−quark
  5/3). So the best CURRENT estimate of the surviving difference is `~10⁻³`.
- **Collins applies to weakly-coupled fixed theories** (agent 3): being fixed/finite is necessary, not
  sufficient; graphene succeeds only because it's single-species (no difference observable). δv IS a
  genuine record (species time-of-flight; agent 4).

## Net verdict
The prior "obstruction needing new physics" framing **imported an EFT category** (free coupling + sliding
cutoff). For a FIXED fundamental theory, "tuning" → "prediction" ('t Hooft/Wetterich). The corrected
status: **tree passes; the radiative marginal δv is an UNCOMPUTED, high-stakes PREDICTION** (if the
estimate `~10⁻³` holds it is a FALSIFICATION, not an unnatural tuning). **The real next artifact is a
COMPUTATION** — the species-differential marginal δv on the native continuous-time surface at β=6,
including the shared-kernel difference + the `(μ/M_Pl)^γ` flow + the `c_t`-fixing — NOT a custodial-
symmetry hunt (#3126/#3129/#3131 were the EFT-framing's fallback).

## Ranked routes
| Rank | Route | Status if done | First artifact | Stop condition |
|---|---|---|---|---|
| 1 | **Compute the species-differential marginal δv** (the number) | a definite pass/falsify | lattice-PT self-energy on shared sin(pa) kernel, two reps, native surface, × (μ/M_Pl)^γ | δv < bound → pass; > bound → falsify |
| 2 | UHECR dim-6 prediction (near-edge) | a near-term test | the 5.6e-18 vs 1e-17 tree result | sharpen the UHECR coefficient + bound |
| 3 | quantify the (μ/M_Pl)^γ IR suppression on the difference | tightens route 1 | integrate the coupled velocity-RG (#3121) for the rep difference | γ_eff over the hierarchy |
| 4 | (fallback) custodial symmetry / new strong UV | only if route 1 lands above bound | #3126/#3129/#3131 (done: excluded/new-physics) | — |

## Do NOT
- Don't say "Lorentz naturalness is an obstruction needing new physics" without the caveat: that's the
  EFT framing; for the fixed theory it's an uncomputed prediction.
- Don't claim the reframe SOLVES it — the shared kernel does not cancel the species difference (agent 2).
- Don't pursue the custodial-symmetry hunt as primary — it's the fallback; the number is primary.
