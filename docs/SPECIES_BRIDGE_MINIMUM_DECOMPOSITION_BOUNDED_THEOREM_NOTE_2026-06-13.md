# The Species Bridge Decomposes into Derived Support + Two Vacuities + One C₃-Grade Contentless Identification: AC_φλ(iii) in Minimum Form (Bounded Theorem)

**Date:** 2026-06-13
**Claim type:** bounded_theorem
**Boundary:** This source note does not set or predict an audit outcome, does
not retire or re-grade any Tier-A admission, and does not edit any audit data
file.
**Primary runner:**
[`scripts/frontier_species_bridge_minimum_decomposition_2026_06_13.py`](../scripts/frontier_species_bridge_minimum_decomposition_2026_06_13.py)
**Runner cache:**
[`logs/runner-cache/frontier_species_bridge_minimum_decomposition_2026_06_13.txt`](../logs/runner-cache/frontier_species_bridge_minimum_decomposition_2026_06_13.txt)
(SCORECARD: PASS=10, FAIL=0)

> **Not claimed:** a derivation of the abstract→physical identification
> (it is not derived away), a claim about across-fermion-type alignment
> (CKM/PMNS), or any audit status. **Claimed (bounded):** the
> `AC_φλ` sub-admission (iii) — the abstract-sector → physical-species
> bridge — decomposes into **derived support** (the hw=1 carrier is
> `M₃(ℂ)`, irreducible, no proper quotient), **two provably-vacuous
> convention choices** (within-triplet naming; carrier-triplet choice),
> and **one irreducible residual** that is **contentless at the tested
> C₃-structural grade**: it supplies no number, selector, ordering, or
> weight. The minimum form
> of AC_φλ(iii) is a single interpretive identification of the same class
> as the universal abstract→physical bridge (abstract su(3) → physical
> color) present in every gauge theory.

## Role — the θ̄ treatment, applied to the species bridge

The Tier-A minimum statements carry AC_φλ(iii) as "the abstract-sector →
physical-species bridge." This note does for it what the structured
admission did for θ: separate what is derived from what is convention from
the irreducible residual, and pin the residual's tested C₃-structural
content to zero. The result sharpens AC_φλ(iii) to its weakest possible
form — an interpretive identification carrying no tested structural or
numerical content at that grade — which is
arguably the kind of "admission" every physical theory has and which some
would argue is not a genuine input at all.

## The decomposition (runner, 10/10)

**Derived support (B).** On the staggered surface (D, `dim ker D = 8`,
Hamming grading 1+3+3+1, the C₃[111] rotation `U_R`), the hw=1 triplet is
three orthogonal C₃-connected states whose generated algebra
`⟨T₁,T₂,T₃,C₃⟩|_{hw=1}` is `M₃(ℂ)` (dim 9, scalar commutant ⟹ irreducible,
no proper exact quotient). The carrier **structure** is derived, not
admitted (check 3) — reproducing the gate note's algebraic species clause.
(`U_R` is a symmetry of **ker D**, not of D globally — `[D, U_R] ≠ 0` on
the full lattice — which is exactly what the carrier-structure claim
needs.)

**Vacuity 1 — within-triplet naming (C).** The three hw=1 states form a
**single C₃ orbit** (C₃ acts as a 3-cycle), and a generic C₃-equivariant
Hermitian equipartitions (`diag(H) = Tr(H)/3`), so no structure-derived
functional separates the corners. Which corner is e/μ/τ is a vacuous
convention — the landed labeling no-go, reproduced (check 4).

**Vacuity 2 — carrier-triplet choice (D, new).** The corner structure has
*two* triplets (hw=1 and hw=2). The staggered chirality
`ε(x) = (−1)^{x₁+x₂+x₃}` satisfies `εDε = −D` (so it preserves ker D),
**commutes with the C₃ rotation** (`[ε, U_R] = 0`), and maps the hw=1
triplet bijectively onto the hw=2 triplet (the (π,π,π) corner shift
`hw_k ↔ hw_{3−k}`) (checks 5–6). Hence ε restricts to a **unitary C₃-
intertwiner** between the two candidate carriers: hw=2 is also `M₃(ℂ)`
(dim 9, scalar commutant), and `EH·C₃|_{hw1} = C₃|_{hw2}·EH` with EH
unitary (check 7). The two carriers are unitarily equivalent as
C₃-representations — same algebra, same 3-cycle orientation — so **which
Hamming triplet is "the generations" supplies no structural or numerical
content** (as C₃-representations). It is naming-class, not input-class.

Two clarifications keep this honest. First, the C₃-equivalence of hw=1 and
hw=2 is **automatic** — both are 3-dimensional regular (transitive)
C₃-representations with identical spectra `{1, ω, ω²}`, equivalent
regardless of ε; ε's role is only to supply a *canonical, orientation-
preserving* intertwiner rooted in the actual surface operator, not to
establish an equivalence otherwise in doubt. Second, ε is the staggered
chirality (a genuine flip, `εDε = −D`) and is **not diagonal in the
Hamming-triplet basis** — its kernel chirality-eigenstates are equal
hw=1/hw=2 mixtures — so the carrier-choice between two Hamming triplets is
*orthogonal* to the chirality content; ε enters here only as the
equivariant operator exhibiting the C₃-equivalence, and the full
taste/Dirac/chirality content of hw=1 vs hw=2 is bracketed (see NOT-claims).

**The irreducible residual is contentless at the C₃ grade (E).** After (B) derived and
(C), (D) vacuous, the species bridge is exactly one interpretive
identification: *the derived 3-state irreducible C₃-structure is what
physics calls fermion generations at the C₃-structural grade.* The
contentlessness is **carried by
checks 4 and 7** — the within-triplet single-orbit equipartition and the
unitary ε-intertwiner — and made probative in check 8: a corner-weight
diagonal that *separates* the corners for a generic operator (computed
spread ≈ 6) is forced **equal** once the operator is required to be
C₃-equivariant (orbit-averaged, spread = 0). So no C₃-equivariant
functional separates the corners — the constancy is from orbit-averaging,
not a trivial invariance. (The ε carrier-swap, pulled back via the
intertwiner, is the identity `EH†EH = I`; carrier-vacuity is therefore
carried by check 7, not by an automorphism-group count.) Check 9 then
discharges each input-type by a **computed witness**: **number** — the
carrier is the rigid regular C₃-rep (three fixed integer character triples
`(−1,1,1)/(1,−1,1)/(1,1,−1)`, no free modulus); **selector** — unitary
carrier-equivalence (7) + single orbit (4); **ordering/weight** —
equivariant equipartition (8). The bridge supplies none. What remains is a
pure abstract→physical identification of the **same class — at the
C₃-structural grade — as** abstract su(3) → physical color (with the
caveat below that, unlike color, two candidate carriers exist; their
selection is vacuous only at the C₃ grade, the full taste/Dirac content
being bracketed).

## What this changes — AC_φλ(iii) in minimum form

The minimum statement of AC_φλ(iii) is now: *a single interpretive
identification of an already-derived irreducible C₃-structure with the
physical fermion generations, carrying no tested C₃-grade number, selector,
ordering, or weight.* Within AC_φλ this is a weaker admission shape than (i) (a binary
selector) and (ii) (a value-fixing readout): (iii) carries no
number/selector/ordering/weight, while (i) and (ii) each do. *(This is a
within-AC_φλ comparison the runner backs; it is not a cross-registry
superlative — the runner does not examine θ/Y₀/g₀, and g₀ is itself
arguably already content-free.)* It is the same identification every gauge
theory makes
between its abstract representation-theoretic content and the named
physical species at the C₃-structural grade; if that universal identification is not counted as a
framework-specific admission elsewhere, AC_φλ(iii) need not be either —
but this note does not make that governance call; it only fixes the
tested C₃-grade content to zero.

## What this note does NOT claim

- **Not** a derivation of the abstract→physical identification: it is not
  derived away, only shown contentless at the tested C₃-structural grade.
  It remains an interpretive bridge.
- **Not** a claim about across-fermion-type alignment (the CKM/PMNS
  mixing structure) — a separate residual, not addressed here.
- **Not** a claim that hw=1 and hw=2 are physically interchangeable in
  the full Dirac/taste content — only that they are unitarily equivalent
  *as C₃-carriers of the generation structure*, so the carrier-choice
  supplies no C₃-structural or numerical content.
- **Not** a retirement or re-grade of AC_φλ; the registry is untouched.
- **No** PDG value, fitted selector, or empirical comparator anywhere.

## Honesty gate (negative-flavored sub-claim discipline)

The negative sub-claims — "naming vacuous," "carrier-choice vacuous,"
"residual contentless" — are each scoped to a computed witness: the single
C₃ orbit + equipartition (naming, check 4); the explicit unitary
ε-intertwiner (carrier, check 7); and, for contentlessness, the
orbit-averaging test (check 8: a corner-separating functional is forced
constant only after C₃-equivariance is imposed) plus the per-input-type
computed witnesses (check 9). Honest about the proof's reach: the
tested C₃-grade contentlessness conclusion is *carried by checks 4 and 7*; a fully
rigorous "zero structural-selection bits" statement would require
computing the C₃- (and ε-) invariant functional ring of the carrier and
showing it has no orbit-separating generator — check 8 establishes the
representative case (the diagonal corner-weight) rather than the full ring,
so the conclusion is argued/strongly-supported, not exhaustively proven.
The claim is about *structural-selection bits at the C₃ grade on this
surface*, not a philosophical claim that interpretive identifications are
never admissions — the residual is explicitly retained as a bridge of the
universal abstract→physical class, and the carrier "vacuity" holds only at
the C₃-structural grade (the full Dirac/taste/chirality content of hw=1 vs
hw=2 is bracketed).

**Scorecard reading.** The strongly-witnessed facts are the `M₃(ℂ)`
carrier (checks 1–3), the single-orbit equipartition (check 4), and the
unitary ε-intertwiner carrier-equivalence (checks 5–7). The
contentlessness conclusion (checks 8–9) is argued from those, with check 8
made probative by the orbit-averaging contrast and check 9 reduced to
computed per-input-type witnesses; read 10/10 as "decomposition + two
vacuities fully witnessed; contentlessness argued from them," not as an
independent 10-fact proof of contentlessness.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  (the hw=1 `M₃(ℂ)` algebraic species clause — derived support)
- [`STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md)
  (the within-triplet naming vacuity — orbit-equivariance no-go,
  reproduced)
- Context, not load-bearing (plain text, in-flight): the 06-11
  equivariant channel-space note (`KOIDE_GENERATION_CHANNEL_SPACE_...`),
  which independently computes the ε corner-complement map and the
  same-orientation triplet blocks, and the Tier-A minimum-statement
  refinement carrying AC_φλ(iii).

## Reprove-and-cite ledger

- **Reproven here (runner):** the staggered surface and grading; the
  hw=1 `M₃(ℂ)` algebra and scalar commutant; the single-C₃-orbit and
  equipartition naming witness; `εDε = −D`, `[ε,U_R]=0`, the hw=1↔hw=2
  bijection; the unitary C₃-intertwiner and the hw=2 `M₃(ℂ)`; the
  orbit-averaging contrast (generic corner-weight separates, spread ≈ 6;
  C₃-equivariant forced equal, spread = 0) and `EH†EH = I`; the
  per-input-type computed witnesses (rigid character triples; carrier
  equivalence; equipartition); the interface pins on the labeling no-go
  and gate note.
- **Cited at declared grade:** the gate-note species clause; the
  labeling no-go.

## Verification

```bash
python3 scripts/frontier_species_bridge_minimum_decomposition_2026_06_13.py
```

Expected: 10 `[PASS]` lines, three `RESIDUAL (declared-open)` lines, then
`TOTAL: PASS=10 FAIL=0` and the verdict paragraph. Exit code 0 iff
FAIL=0.

**Independent audit required.** This note asserts no effective-status
change.
