# Exercise packet — staggered-Dirac realization gate (2026-06-06)

Repo "exercise" skill (`docs/ai_methodology/skills/exercise/SKILL.md`), 5-subagent
fan-out (max-reasoning, each with a framework-refresher read).

## Wall (Exercise Zero, neutral)
Derive the staggered Kogut–Susskind Dirac matter operator on Cl(3)⊗Z³ —
(a) one-Grassmann/site carrier, (b) KS phases η_μ(x), (c) Dirac/Kähler–Dirac
structure, (d) species/taste reduction, (e) chirality — from {Lattice, Quantum,
Record}. Progress = forcing or honestly admitting each; closure/demotion/no-go
artifacts count.

## Headline ("just to be sure" caught an over-claim)
The prior passes (#2956, #2967) concluded "gate essentially closed / forced ×6".
**The full exercise refutes that with the repo's own substeps.** Three genuine
**hidden admissions** beyond AC_φλ:
1. **FS (fermionic statistics)** — substep-1 is `retained_no_go` *statistics-agnostic*:
   a hard-core boson has on-site dim 2 = qubit dim = Grassmann dim, so dimension
   forces the carrier *size* (excludes Wilson dim-16) but **not** the
   fermion-parity grading.
2. **Signature/time** — the Kähler–Dirac d−δ needs a derivative direction + Hodge
   metric, absent from the axioms (no time axiom).
3. **Chirality ε(x)** — "out of scope" in substeps; gated on the *unaudited*
   `axiom_first_spin_statistics_theorem`.

## Verified positive leads (finite checks reproduced)
- **Lead 1 (η = cohomological 2-cocycle):** η_μ(x)=(−1)^{Σ_{ν<μ}x_ν} is a Z₂
  1-cochain whose plaquette curvature is uniformly −1 (the Clifford
  anticommutation 2-cocycle), unique mod coboundary (= global gauge). Upgrades
  η-forcing to cohomological uniqueness; sidesteps the JW/CAR-string no-go.
- **Lead 2 (Kähler–Dirac = Cl(3) action):** γ_μ=e_μ∧−ι_{e_μ} on Λ(ℂ³) (dim
  8 = dim Cl(3)_ℂ) satisfy {γ_μ,γ_ν}=−2δ; Hamming grading 1,3,3,1; volume element
  → chirality. The Dirac structure is the qubit's own geometric-algebra action
  (one qubit = one Cl(3) chiral block = spinor module).

## Open atom (Elon reduction)
Not the Kähler–Dirac equivalence (now retained_bounded) and not the η-phase
(deterministic downstream of spin-diagonalization). The honestly-open atom is the
**on-site chirality selector ε(x)**. Decisive artifact: a one-link
chirality-selector enumerator — ≥2 survivors ⇒ ε is a free selector (a second
staggered admission); exactly 1 ⇒ a forcing lemma exists (gated on a retained
spin-statistics theorem).

## Route portfolio
| Rank | Route | Outcome class | First artifact |
|---|---|---|---|
| 1 | chirality-selector ε(x) | forced-finding OR new admission | one-link enumerator |
| 2 | FS statistics | new Tier-A `FS` candidate (no-go) | promote substep-1 no-go |
| 3 | signature/time import | name the hidden import | audit what d−δ consumes |
| 4 | η cohomology forcing | derive-from-retained (verified) | shipped (this packet) |
| 5 | Kähler–Dirac = Cl(3) | derive-from-retained (verified) | shipped (this packet) |

No new axiom invented. Literature = inspiration only (Nielsen–Ninomiya no-go;
Becher–Joos; Catterall reduced-staggered; Jordan–Wigner; Karsten–Wilczek) — see
LITERATURE_SEARCH.md. Files: EXERCISE.md (full 5 sections), this SUMMARY.md.
