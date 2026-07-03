# Staggered-Dirac Gate — Exercise Re-Assessment: Three Hidden Admissions + Two Verified Leads

**Date:** 2026-06-06
**Claim type:** bounded_theorem (exercise re-assessment; corrects a prior over-claim)
**Status:** review-loop source proposal. Adds no axiom, no fitted input, no audit
verdict. **Corrects** the "essentially closed / forced ×6" framing of the prior
staggered-Dirac passes (the staggered-scheme note and the formal audit note from
the same day).
**Primary runner:**
[`scripts/frontier_exercise_staggered_dirac_reassessment_2026_06_06.py`](../scripts/frontier_exercise_staggered_dirac_reassessment_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_exercise_staggered_dirac_reassessment_2026_06_06.txt`](../logs/runner-cache/frontier_exercise_staggered_dirac_reassessment_2026_06_06.txt)
**Exercise packet:** `.claude/science/exercises/staggered-dirac-gate/`

---

## Role

Output of the repo's **exercise** wall-breaking skill
([`docs/ai_methodology/skills/exercise/SKILL.md`](ai_methodology/skills/exercise/SKILL.md))
run on the staggered-Dirac realization gate as a full 5-subagent fan-out
(assumptions ledger / Elon reduction / literature / mathematics-sector /
reframing, each with a framework-refresher read). The run was commissioned as a
"just to be sure" check on the claim that the gate is essentially closed — and it
**caught an over-claim**.

## The correction (runner SCORECARD 18/18 PASS)

The earlier same-day passes concluded the gate was "essentially closed (6 forced
findings)". The full exercise refutes that **with the repo's own substeps**.
Three genuine **hidden admissions** beyond the named `AC_φλ`:

1. **Fermionic statistics (FS) is not dimension-forced.** A **hard-core boson**
   has on-site Fock dim 2 = the qubit dim = the Grassmann-pair dim. Dimension
   forces the carrier **size** (one mode/site — excluding Wilson's dim 16) but
   **not** the fermion-parity grading. Substep-1 is in fact a `retained_no_go`
   that is *statistics-agnostic*: the ungraded one-site algebra is the same
   `M₂(ℂ)` either way. So the earlier "bosonic excluded by dim ∞" was the wrong
   alternative; the relevant alternative (hard-core boson) is **not** excluded,
   and FS is an admission.
2. **A Euclidean-signature / time-direction import is hidden.** The Kähler–Dirac
   operator `d − δ` needs a derivative direction and a Hodge inner product —
   absent from `{Lattice, Quantum, Record}` (no time axiom).
3. **Chirality `ε(x)` is a hidden admission.** It is marked "out of scope / not
   load-bearing" in the substeps, and is gated on the *unaudited*
   `axiom_first_spin_statistics_theorem`.

So the staggered-Dirac gate is **not essentially closed**: its genuine hidden
admissions are `{FS statistics, signature/time, chirality ε}`, beyond `AC_φλ`.
(What *is* right in the prior pass: the dim-2 carrier excludes Wilson/naive
(dim 16) and overlap (nonlocal); the continuum demotion stands. The error was
conflating carrier-*size* forcing with statistics forcing, and over-counting
"forced".)

## Two verified positive leads

The exercise also produced two **finite-verified** routes (reproduced in the
runner):

- **Lead 1 — η is a cohomological 2-cocycle.** The KS phase
  `η_μ(x) = (−1)^{Σ_{ν<μ} x_ν}` is a `Z₂` 1-cochain whose plaquette curvature is
  **uniformly −1** (= the Clifford anticommutation 2-cocycle) — verified on all
  192 plaquettes of a 4³ block — and is **unique modulo coboundary (= global
  gauge)**. This upgrades η-forcing to a cohomological-uniqueness statement and
  **sidesteps the Jordan–Wigner/CAR-string no-go** (η is a c-number cochain, not
  the statistics string).
- **Lead 2 — Kähler–Dirac `D = d − δ` is the Cl(3) Clifford action.**
  `γ_μ = e_μ∧ − ι_{e_μ}` on `Λ(ℂ³)` (dim `8 = dim Cl(3)_ℂ`) satisfy
  `{γ_μ, γ_ν} = −2δ_{μν}` (verified); the Hamming-degree grading is `1,3,3,1`
  (= the substep-3 taste/doubler pattern); the volume element gives chirality. So
  the Dirac/γ structure is **the qubit's own geometric-algebra action** — one
  qubit = one Cl(3) chiral block (spinor module) — not an imported overlay.

## The open atom + route portfolio (synthesis)

The Elon reduction isolates the honestly-open atom: **not** the Kähler–Dirac
equivalence (now retained_bounded) and **not** the η-phase (deterministic
downstream of spin-diagonalization), but the **on-site chirality selector
`ε(x)`**. The decisive next artifact is a **one-link chirality-selector
enumerator**: over on-site sign assignments on a single Z³ bond, count those
consistent with `{Lattice, Quantum, Record}` + retained graded-locality — **≥2
survivors ⟹ ε is a free selector (a second staggered admission); exactly 1 ⟹ a
forcing lemma exists** (gated on a retained spin-statistics theorem).

| Rank | Route | Outcome class | First artifact |
|---|---|---|---|
| 1 | chirality selector `ε(x)` | forced-finding *or* new admission | one-link enumerator |
| 2 | FS statistics | new Tier-A `FS` candidate (no-go) | promote substep-1 no-go |
| 3 | signature/time import | name the hidden import | audit what `d−δ` consumes |
| 4 | η cohomology forcing | derive-from-retained (verified) | this note |
| 5 | Kähler–Dirac = Cl(3) | derive-from-retained (verified) | this note |

No route requires a new axiom (the protocol's forbidden outcome).

## Literature (inspiration only, cited)

Nielsen–Ninomiya (NPB 185/193, 1981 — the no-go that any "1 component ⇒ chiral"
proof must break); Kogut–Susskind (PRD11, 1975) / Kawamoto–Smit (1981);
Becher–Joos (Z.Phys.C 15:343, 1982, staggered ≅ Dirac–Kähler); Jordan–Wigner
(1928, one qubit = one fermion mode, nonlocal string); Catterall (arXiv:2010.02290,
2405.03037, reduced/chiral staggered, `ε` → `U(1)→Z₄`); Karsten–Wilczek
(arXiv:2502.16500). None imported as authority.

## Scope

This is a re-assessment + two verified leads + a route map — **not** a closure of
the gate (it shows the gate is *less* closed than claimed). The verified leads
(η-cohomology, Kähler–Dirac = Cl(3)) are exact finite facts; the open atom (`ε`
selector) and the FS/signature admissions are named, not discharged. No new axiom.

## Reprove-and-cite ledger

- **Reproven here** (runner): hard-core-boson dim 2 = qubit dim (statistics not
  dim-forced); η plaquette curvature ≡ −1 (192 plaquettes); the Cl(3) γ-matrices
  on `Λ(ℂ³)` (Clifford + `1,3,3,1` grading); the route classifications.
- **Cited**: the exercise skill + assumption-import protocol; the staggered-Dirac
  substeps and the prior same-day passes (corrected here); the Quantum/Locality/
  Record axioms (`MINIMAL_AXIOMS_2026-06-05`); the literature above (comparators).

## Audit dependency repair links

- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- [STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
