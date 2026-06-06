# The Staggered Realization is Forced by One Qubit per Site + Locality (Counterfactual Pass on the Gate)

**Date:** 2026-06-06
**Claim type:** bounded_theorem (counterfactual-pass result)
**Status:** review-loop source proposal. Adds no axiom, no fitted input, no audit
verdict.
**Primary runner:**
[`scripts/frontier_staggered_scheme_forced_by_one_qubit_locality_2026_06_06.py`](../scripts/frontier_staggered_scheme_forced_by_one_qubit_locality_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_staggered_scheme_forced_by_one_qubit_locality_2026_06_06.txt`](../logs/runner-cache/frontier_staggered_scheme_forced_by_one_qubit_locality_2026_06_06.txt)

---

## Role

The **counterfactual pass** (the assumption-by-assumption "what if this is wrong,
and what direction does the closure go?" exercise) applied to the
**staggered-Dirac realization gate**
([STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md),
audited_renaming).

**What the pass reveals:** the gate is *not* a monolithic wall. Per
[STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md)
it is a **4-substep chain**: substep-1 (Grassmann forcing), substep-2
(Kähler-Dirac equivalence), substep-3 (BZ-corner / species, retained), substep-4
(species-label = `AC_φλ`). Substep-1
([…SUBSTEP1_GRASSMANN_FORCING…](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md))
already forces the matter to be **fermionic, not bosonic**, by per-site
Hilbert-dimension matching: the qubit `M₂(ℂ)` has per-site dim 2, a Grassmann pair
`(χ, χ̄)` has Fock dim 2 (`χ̄²=0`), while a per-site boson has Fock dim ∞ — bosonic
excluded.

## The counterfactual fill (this note, runner SCORECARD 20/20 PASS)

Substep-1 settles *fermionic vs bosonic*. The remaining counterfactual is **"what
if the fermionic realization is Wilson / naive / overlap rather than
staggered?"** The same per-site dim-2 argument **+ the Locality axiom** answers it:

| scheme | per-site Grassmann content | per-site Fock dim | verdict |
|---|---|---|---|
| **staggered (KS)** | 1 component | `2¹ = 2` | **matches qubit (dim 2), local** |
| Wilson | 4-component Dirac spinor | `2⁴ = 16` | dim ≠ 2 ⟹ needs 4 qubits/site |
| naive | 4-component (+ doublers) | `2⁴ = 16` | dim ≠ 2 |
| overlap / domain-wall | (nonlocal / 5th dim) | — | violates **Locality** |

Only the **staggered (Kogut–Susskind)** realization places exactly **one Grassmann
field per site** (Fock dim 2 = the qubit dim) **and** is local. Wilson/naive would
require per-site dim 16 — i.e. **four qubits per site** — contradicting the Quantum
axiom's one qubit per site; overlap/domain-wall is nonlocal (or needs an auxiliary
dimension), contradicting Locality.

> **`{Quantum (one qubit M₂(ℂ) per site, dim 2), Locality}` force the staggered
> carrier (one Grassmann per site).** This completes substep-1 from "fermionic vs
> bosonic" to "**staggered vs all other lattice-fermion schemes**."

## The broader counterfactual output

The pass re-characterizes the whole gate: it is a **mostly-closed 4-substep
chain**, not a deep wall.

- **substep-1** (Grassmann + staggered-scheme forcing) — `{Quantum, Locality}`,
  this note completing it;
- **substep-2** (Kähler-Dirac equivalence) — the staggered ≅ Kähler-Dirac
  identity, a standard math fact (Becher–Joos), currently unaudited;
- **substep-3** (BZ-corner / species reduction) — retained / retained_bounded;
- **substep-4** (species-label) — `= AC_φλ`, still outside this carrier note.

So the gate's one named irreducible residual (substep-4 `AC_φλ`) is
not closed here. The remaining open pieces are substep-2, substep-4, and the
continuum Dirac limit; this note only narrows the wall around the carrier.

## Scope and honest residual

- Forces the staggered **carrier** (one Grassmann per site). The Dirac **operator**
  built on it — the single-link hopping, the Kogut–Susskind phases, and the
  Kähler-Dirac equivalence (substep-2) — and the **continuum** Dirac limit are
  separate substeps, **not** claimed here.
- The dimension counting is representation theory; the exclusion of overlap is the
  **Locality** axiom. No new axiom.

## Reprove-and-cite ledger

- **Reproven here** (runner): the per-site Fock-dimension counting for staggered
  (2), Wilson/naive (16), and the locality verdicts; the uniqueness of staggered
  under `{dim 2, local}`.
- **Cited**: substep-1 Grassmann forcing (fermionic-vs-bosonic dim matching); the
  gate closure synthesis (the 4-substep structure); the Quantum and Locality
  axioms (`MINIMAL_AXIOMS_2026-06-05`); the staggered ≅ Kähler-Dirac equivalence
  (Becher–Joos, comparator); the `AC_φλ` species-label residual remains outside
  this carrier note.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. It does not promote any note or change any
audited claim scope.

- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- [STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
- [STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
