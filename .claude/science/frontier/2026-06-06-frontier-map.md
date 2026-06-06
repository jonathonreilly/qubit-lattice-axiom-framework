# Frontier Map: 2026-06-06

*Adapted from the /frontier template to this framework's structure — physics lanes, Tier-A admissions, audit
status — rather than simulation mechanism families.*

## Coverage Summary
- Total docs notes: **2857**
- Genuine Tier-A admitted inputs: **2** (`AC_φλ` flavor, lev 41; `θ` strong-CP, lev 20)
- Audit ledger: **198** retained · **704** retained_bounded · **214** retained_no_go (dead ends) ·
  **37** open_gate · **75** audited_conditional · **17** audited_failed · **1260 unaudited (44%)**
- Foundations pillar this session: **mass = recordedness** added to the existing **gauge = unrecorded** (#2667),
  composition/local-tomography (#2573), d=3-as-Z³-primitive.

## Lane Census (docs notes by lane)

| Lane | Notes | Status |
|---|---|---|
| Koide / charged-lepton flavor | 264 | **PARTIAL** — `Q=2/3` structure derived; `r=1/2` reduces to `det_C` vs `det_R` (open, AC_φλ); `δ=2/9` forced number + radian admission |
| Dark matter / DM sector | ~290 | PARTIAL — heavy Majorana candidate, mass window; Ω ratio bounded |
| Neutrino / PMNS | 164 / 109 | PARTIAL — Dirac, trimaximal column 1/3, θ23 upper octant; positive PMNS lane open |
| CKM | 56 | **STRONG** — atlas/axiom package, δ=arctan√5, full magnitudes (publishable surface) |
| Record / axiom / mass | 138 / 80 / 70 | **STRONG (foundations)** — gauge + mass + composition from Record |
| Higgs / EW | 54 | STRONG — v, couplings, sin²θ_W, m_H (bounded, M_Pl/exp-16 imported) |
| Strong-CP / θ | 9 | **NARROWED** — continuous naturalness dissolved both sides (this session); discrete selection + gauge slot walled |
| Cosmology / graviton | 14 / 5 | PARTIAL — Λ=spectral gap, w=−1, graviton m_g²=2Λ (record-selected scale, this session) |

## Confirmed vs unvalidated vs refuted
- **Retained/bounded (902):** the publishable quantitative surface (CKM, EW, confinement, neutrino bounds) +
  the foundations pillar.
- **Unaudited (1260, 44%):** the largest single liability — a *credibility* gap, not a science gap.
- **Refuted/dead (214 no_go + 17 failed):** the foreclosure ledger (see Dead Ends).

## Top 5 Highest-Value Gaps (ranked by info-gain × feasibility ÷ effort)

**1. Foundations consolidation → the publishable unit.** *Highest value for the actual goal.* The 40-seat panel's
verdict was that the framework's real, defensible contribution is **axiom→structure**: gauge invariance,
composition/local-tomography, and now **mass**, all corollaries of the Record axiom. This is a coherent
foundations paper (PRX Quantum / PRA tier), and it is **tractable** (synthesis of *existing, audited* results into
the manuscript surface). **Risk:** the reviewer rejects meta-framings — so it must land in `docs/publication/` as
manuscript narrative using repo-canonical vocabulary, not as a new "theorem." **Effort:** medium (writing +
positioning, no new derivation).

**2. Koide `r=1/2` via `det_C` / Kähler-Dirac index (AC_φλ, lev 41).** *The one genuine open derivation lever.*
This session's min-info detour ended by pinning it precisely: does the staggered-Dirac generation determinant come
out **first-order** (index / `det_C` → r=1/2, Q=2/3) or **second-order** (modulus / `det_R` → r=1, Q=1)? The
native readout `log|det|` gives `det_R` (κ=1 — the live partial-falsification); `det_C` needs the chirality
grading promoted from static structure. **Info gain: maximal** — closes a flavor value from first principles, or
confirms the partial-falsification. **Effort: high** (the Kähler-Dirac index of the generation operator; 45-yr
problem territory). **Feasibility: the hardest thing on the board, but the only real one.**

**3. Audit the unaudited backlog (1260 claims).** *The publication blocker.* 44% of the ledger is unaudited; no
foundations paper ships on that. Triage by leverage (the rows the publishable surface + foundations pillar depend
on first). **Info gain: moderate** (mostly confirms/demotes existing claims), **but gates publication.** **Effort:
high, batchable** (audit-lane work, not new science). Pairs with #1.

**4. The mass scale `v` / hierarchy via mass=recordedness.** *Speculative, high-ceiling.* The new pillar left "why
is `v ≠ 0`" as its deepest residual, reframed as "why a durable symmetry-breaking record." This connects to the
open hierarchy lane (imported `M_Pl` + un-derived exponent-16). A genuinely new angle on a big open thing — but
unproven it goes anywhere. **Effort: medium-high, exploratory.**

**5. θ gauge "no bare slot" / discrete selection (θ, lev 20).** *Low expected payoff now.* The continuous-
naturalness half is dissolved (this session); the residual discrete selection needs a weighting (min-info refuted)
and the gauge slot is well-walled (RP foreclosed, action-form blocked, antiunitary-parity leaves iθQ invariant,
Vafa-Witten bounds-not-selects). **Recommend: do not invest further** until a new structural primitive appears.

## Dead Ends (do not revisit unless new theory motivates)
- **min-info as a *counting* principle** for Koide/θ — refuted 2026-06-06: orbit-count ≠ the native `log|det|`
  (dimension-count, κ=1); max-entropy → wrong (ρ=I/3 → r=1); the fitting version *is* the existing block-democracy
  admission. CKM uses dimension-count too. Reduces to the `det_C`/chirality lever (#2 above), not information.
- **RP for the θ-slot** — `strong_cp_rp_half` no-go (topological density Θ-anti-invariant, phase cancels).
- **Action-form uniqueness** — Wilson/HK/Manton jointly compatible with retained primitives.
- **β=6 reformulation** — no known approach (QLM/D-theory/string-net) derives the coupling; always input.
- **d=3 from the qubit alone** — closed; d=3 is a Z³ lattice primitive (Cl(3)⊗Z³), not derived from the algebra.
- **"chiral → r=1/2" magnitude** — refuted (#2624): chirality moves the determinant *phase* (η/δ), not the
  magnitude `r`. Holomorphy needs a SUSY superpotential the framework lacks.
- **η→δ topological selector** — failed (#2688): δ is *also* an admission (modulus even in δ, degenerate spectra).
- **Continuous-naturalness framing of strong-CP** — dissolved both sides this session (#2932/#2939/#2947); θ̄ is
  record-discrete, so the "tiny continuous angle" puzzle is gone — only a discrete selection remains.

## Recommendation
**Run #1 and #3 together** (consolidate the foundations pillar into the manuscript surface *while* triaging the
unaudited rows it depends on) as the publication track, and keep **#2 (Koide `det_C`)** as the one science lane
worth a deep dive when appetite for a hard derivation returns. **#5 is a wall — leave it.** The session's net is
that the framework's *frontier has shifted from "derive the SM numbers" (largely walled) to "consolidate the
axiom→structure foundations" (open and publishable)* — the panel was right, and mass=recordedness is the newest
brick in exactly that wall.
