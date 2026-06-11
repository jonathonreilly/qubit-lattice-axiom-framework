# Registrable Readout Is Additive-Plus-Even Hence Phase-Free — Narrow Bounded Theorem

**Date:** 2026-06-10
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** source-side claim-boundary declaration only — a narrow conditional
theorem on the Record-registrable readout class. `proposed_retained` is **not**
asserted; the boundary below is a source-side declaration, not an audit verdict.
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome and does not edit the audit-lane-owned Tier-A
registry, ledger, queue, or publication-status surfaces.
**Primary runner:**
[`scripts/frontier_registrable_readout_additive_even_phase_free_2026_06_10.py`](../scripts/frontier_registrable_readout_additive_even_phase_free_2026_06_10.py)
(SCORECARD: PASS=30, FAIL=0; cached:
[`logs/runner-cache/frontier_registrable_readout_additive_even_phase_free_2026_06_10.txt`](../logs/runner-cache/frontier_registrable_readout_additive_even_phase_free_2026_06_10.txt))

## Boundary

This note proves one narrow structural theorem about the readout class the
**Record** axiom supplies, and applies it to the two registrability bridges
named open by
[`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`](TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md).

It does **not** retire either Tier-A admission, edit
`docs/audit/data/tier_a_admissions.json`, remove bounded status from any
consumer, derive `|delta| = 2/9`, supply the global `Cl(3)/Z^3 -> PL S^3 x R`
identification, close strong-CP premise 1 ("no bare `theta` slot"), or change
the Record axiom boundary. It supplies a registrability structure theorem and
its two direct consequences, with the surviving residuals named explicitly.

## The Record boundary used (and only this)

From [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md), the
**Record** axiom supplies, in a *supplied* readout context with a finite
central-sector decomposition and a fixed `K`/CPT conjugation:

1. **(Additivity)** the scalar readout `I` is finitely additive over finite
   pairwise-disjoint record collections, with `I(empty) = 0`;
2. **(Orbit)** the realized outcome is the `K`/CPT orbit of the realized central
   sector.

It supplies **no** readout context, decomposition, `K`/CPT structure,
sector-generation rule, weighting, normalization, probability, modulus rule,
log-det, source/action, scale, or observable identification. The theorem below
uses only (Additivity) and (Orbit); it adds nothing.

## The theorem

> **Theorem (registrable readout is additive-plus-even, hence phase-free).**
> Let a scalar readout be *Record-registrable*: a scalar assigned to records
> that is (i) finitely additive over pairwise-disjoint records [(Additivity)]
> and (ii) constant on `K`/CPT orbits of the realized central sector [(Orbit)].
> Then on a finite central-sector decomposition its per-sector **phase**
> contribution is identically zero. The only registrable determinant-class datum
> is modulus-type: the multiplicative determinant character `chi_k(z) = exp(i k
> arg z)` is registrable only at `k = 0`.

### Proof (each leg checked in the runner)

**T1 — the central sectors are a disjoint record family.** The finite
central-sector decomposition is a set of orthogonal central idempotents `e_j`
with `e_j e_k = 0` (`j != k`) and `sum_j e_j = 1`. Orthogonality is disjointness,
so `{e_j}` is a pairwise-disjoint record family.

**T2 — additivity forces a per-sector sum with no interference.** Posit the most
general two-sector readout permitting a cross term, `I(e_1 cup e_2) = I(e_1) +
I(e_2) + c`. (Additivity) is exactly `I(e_1 cup e_2) = I(e_1) + I(e_2)`, which
forces `c = 0`. Iterating over the finite family, a registrable readout equals
`sum_j I(e_j)`; there is no cross-sector / interference content.

**T3 — the determinant phase is in the additive class.** For a sector-factored
configuration `det = prod_j z_j`, so `arg det = sum_j arg(z_j)` (mod `2 pi`):
the determinant phase is a per-sector sum, hence a registrable readout's phase
part is an additive `R`-valued functional `g` of the per-sector phase data.

**T4 — an additive functional is odd (no regularity needed).** For any
`R`-valued additive `g` on an abelian group, `g(0) = g(0) + g(0)` gives
`g(0) = 0`, and `g(x) + g(-x) = g(0) = 0` gives `g(-x) = -g(x)`. This is pure
algebra; **no continuity, measurability, or linearity is assumed**, so the
Cauchy/Hamel pathology of additive functions is irrelevant here.

**T5 — even ∩ additive = zero.** (Orbit) makes the readout constant on `K`/CPT
orbits; `K`/CPT acts on the central characters as complex conjugation, sending
`arg z` to `-arg z`. So the phase functional is also **even**: `g(-t) = g(t)`.
Even (`g(-t) = g(t)`) together with odd (T4: `g(-t) = -g(t)`) gives
`g(t) = -g(t)`, hence `g(t) = 0` for every `t`. The per-sector phase
contribution of any registrable readout vanishes; equivalently the
determinant-character phase index is `k = 0`.

**T6 — the hostile guard is threaded.** `K`/CPT-evenness *alone* does **not**
erase phase: `cos(arg z)` is `K`-even (`cos(-theta) = cos(theta)`) yet
phase-dependent. The theorem does not use evenness alone. `cos(arg z)` is
excluded because it is **not sector-additive** —
`cos(arg(z_1 z_2)) != cos(arg z_1) + cos(arg z_2)` — so (Additivity) removes it
before evenness is even invoked. It is precisely the **intersection**
additive ∩ even that is the modulus class; additivity alone admits the odd
phase-sum, evenness alone admits `cos(arg z)`, and their intersection is
phase-free.

**T7 — the surviving datum is modulus-type.** `log|z|` is additive
(`log|z_1 z_2| = log|z_1| + log|z_2|`) and `K`-even (`|conj z| = |z|`), so it
survives registration. The registrable determinant-class readout is exactly the
phase-free `|det|` character (`k = 0`).

## Consequence A — strong-CP determinant-readout bridge (blocker (a))

The named-open bridge in the Tier-A K/CPT note asks that the physical
`arg det(M_u M_d)` contribution used by
[`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) be **exhausted by
the determinant-class registrable readout**, with no phase-sensitive
non-multiplicative or action-level datum remaining relevant to that premise.

`arg det(M_u M_d) = arg det M_u + arg det M_d` is the additive sector-phase sum
(T3, T8 in the runner). By T5 its registrable content is zero: on the
Record-registrable surface the determinant **phase** is exhausted by the
`k = 0` (modulus) character, and no separately-registrable non-multiplicative
phase datum survives (T2 removes interference content; T6 removes `K`-even
non-additive functions like `cos(arg)` as non-registrable). The
multiplicative determinant-character class is therefore exhaustive for the
registrable mass-surface **phase** readout.

This **discharges the determinant-phase content of the positive-real
mass-orientation premise on the registrable surface**. It does so from the
Record boundary and retained surfaces only, threading the hostile guard.

**What Consequence A does NOT close** (carried, not erased):

- **Strong-CP premise 1**, "no bare `theta` slot is admissible", is a *separate*
  action-surface premise. It was shown not derivable from retained reflection
  positivity by
  [`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md).
  This note addresses only the mass-orientation **phase**, not premise 1.
- **The standing modeling identification** — that the physical mass-surface
  readout context *is* the Record-supplied registrable one — is unchanged. The
  theorem removes the phase freedom *within* the registrable class; it does not
  prove the physical readout must be registrable. That identification remains
  the strong-CP / AC_phi_lambda modeling premise.

## Consequence B — AC_phi_lambda unordered-multiset registrability (blocker (b-i))

The same Tier-A note's Registry Consequence asks for the **unordered-multiset
registrability bridge** before the orientation lemma can reduce AC_phi_lambda to
a magnitude-only atom.

For the AC_phi_lambda Hermitian circulant
`H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T`, the runner verifies
`conj(H(delta)) = H(-delta)`: the `delta -> -delta` sign flip **is** the `K`/CPT
conjugation. The elementary symmetric polynomials are all **even** in `delta`
(`e_1 = 3a`; `e_2 = 3a^2 - 3B^2`;
`e_3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta)`), so the unordered eigenvalue
multiset is `K`-even and registrable; the sign of `delta` lives only in the
orientation-odd `sin(3 delta)` line, which is `K`-**odd** and therefore
unregistrable by T4/T5 (an odd additive datum with zero even part).

Hence the registrable species surface is exactly the unordered mass multiset
(the symmetric functions), and the sign / orientation of `delta` is not extra
registrable content. This **closes the unordered-multiset registrability
bridge** and reduces AC_phi_lambda to the magnitude-only atom `|delta|`, exactly
the reduction the orientation lemma was waiting on.

**What Consequence B does NOT close** (carried, not erased):

- The `|delta|` **magnitude** value (`2/9`) and its single-summand readout still
  depend on the named readout identification **R-eta** of
  [`KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md`](KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  and on the global geometry **R2** below. This note removes only the **sign**
  as extra content.
- **R2, the PL/ABSS equivariant global bridge** — the global geometric
  identification `Cl(3)/Z^3 -> PL S^3 x R` named open in
  [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  (Part D) — is **off this layer**. It is a manifold-topology statement
  provably requiring the PL Poincaré conjecture (Perelman), TOP = PL in
  dimension 3 (Moise), and van Kampen `pi_1 = 0`. These are standard external
  mathematics, named LIVE there, **not** on the framework surface, and **not** a
  question of what Record registers. The unordered-multiset registrability
  reduction here is independent of R2: it asks only whether the
  already-computed symmetric data is the registrable surface, which is a Record
  question. R2 therefore remains a separate import-required wall (see the no-go
  discipline section), not addressed by this note.

## Why this is one theorem for two bridges

Both bridges are the *same* Record-registrability question — what scalar a
registrable readout carries on a finite central-sector decomposition modulo
`K`/CPT. Blocker (a) needs the determinant **phase** to be unregistrable;
blocker (b-i) needs the eigenvalue **sign/orientation** to be unregistrable.
Both are the odd part of an additive datum under the `K`/CPT conjugation, killed
by the single additive-plus-even theorem. The two consumers differ only in which
odd datum they care about.

## Net

```text
Record boundary (Additivity + K/CPT orbit)
  => registrable readout = additive over sectors AND K/CPT-even
  => per-sector phase contribution = 0   (additivity forces odd; even forces zero)
  => (a) det-class phase character k=0 EXHAUSTS the registrable arg det(M_u M_d)
  => (b-i) delta-sign unregistrable; species surface = unordered multiset; |delta| atom

new axioms: 0     new primitives: 0     new admissions: 0     new imports: 0
residuals named: strong-CP premise 1 (separate); standing readout-context premise;
                 |delta| magnitude (R-eta); R2 PL/ABSS global bridge (external-math LIVE)
```

## No-Go / Bounded-Wall Discipline Gate (N1–N8)

This note is a conditional positive theorem with a named external-math residual
(R2). The discipline gate is applied to the residual claim "R2 remains an
import-required wall, off the Record layer."

### N1 — Alternative route enumeration (≥5) for the R2 residual

| route | what it would attempt | result | marker |
|---|---|---|---|
| Record-registrability closes R2 | derive the global PL `S^3` identification from what Record registers | FAILS: R2 is manifold topology, not a readout-class question; Record supplies no geometry | RULED OUT (category mismatch) |
| Finite-R cone-cap → global PL | identify the compactification with `PL S^3` from finite caps | FAILS: Euler characteristic blind among closed orientable 3-manifolds | RULED OUT BY PRIOR (`KOIDE_APS_C3_FIXED_LOCUS_...` D2) |
| Local ABSS prerequisites ⇒ global | upgrade the local Morse-Bott/spin/lift checks to the global identification | FAILS: local checks are conditional on the ambient already being `PL S^3 x R` | RULED OUT BY PRIOR (same note, Part C) |
| Replace R2 with a new geometric primitive | adopt the `PL S^3` ambient as a framework primitive | INFEASIBLE: no-new-primitive rule; this would be an unapproved primitive | RULED OUT (policy) |
| Import Perelman/Moise/van Kampen as derivation steps | use the external theorems to close R2 inside the framework | NOT a closure: these are external math; they may be a named open / disclosed comparator, never a derivation step on the framework surface | ATTEMPTED → bounded (import-required) |
| Unordered-multiset bridge avoids R2 | show (b-i) does not route through R2 at all | SUCCEEDS: (b-i) is closed here independently of R2; R2 is load-bearing only for the magnitude / single-summand readout | ATTEMPTED → (b-i) closed, R2 isolated |

Six routes named; the residual is correctly bounded, not a premature no-go.

### N2 — Wall-independence audit

The surviving walls are independent: (W1) strong-CP premise 1 (action-surface
admissibility of a bare `theta` slot); (W2) the standing readout-context
identification (physical readout = Record-supplied); (W3) the `|delta|`
magnitude via R-eta; (W4) R2 the global PL/ABSS identification. None follows from
another: W1 is about the gauge action, W2 about modeling the readout, W3 about a
dimensionless readout identification, W4 about manifold topology. The theorem
collapses none of them into another; it removes a *fifth* item (phase/sign
freedom) that previously rode along with W2.

### N3 — Hidden-wall scan

Load-bearing premises are explicit: (Additivity) and (Orbit) from Record; the
sector-factoring of `det`; the AC_phi_lambda circulant form (consumed from the
Tier-A note's L2). No "we assume", "by construction", "naturally", or
"registered" smuggles a hidden admission: each use of "registrable" is the
explicit Record (Additivity)+(Orbit) data, and each external-math name
(Perelman/Moise/van Kampen) is flagged as the open R2 route, not assumed.

### N4 — Residual matching

The cited witnesses match exactly: the RP no-go attacks strong-CP **premise 1**
(matched, and explicitly NOT this note's target); the `KOIDE_APS_C3_FIXED_LOCUS`
Part D attacks the **global PL identification** (matched as R2); the
`KOIDE_DELTA_ETA_DENSITY` chain attacks the **magnitude via R-eta** (matched).
No witness is repurposed.

### N5 — Rhetoric audit

"The determinant phase is unregistrable" is verified at the per-sector
resolution (T3–T5) and the product-determinant resolution (T8); it is **not**
claimed at any non-additive functional resolution (T6 shows such functions are
excluded by additivity, not registered-as-zero). "Reduces to the magnitude-only
atom" is the sign/orientation removal only; the magnitude is explicitly left
open. "Off this layer" for R2 is the category claim (topology vs. readout
class), checked as a boundary witness (T10).

### N6 — Partial-closure path scan

No new axiom or primitive is proposed. The legitimate closure path for R2 is to
**derive or audit** the global identification on the framework surface (the
external-math content), exactly as `KOIDE_APS_C3_FIXED_LOCUS_...` records it
LIVE. The AC_phi_lambda convention-class reclassification (the Y0 precedent) is
a possible *downstream* registry move, but it is audit-lane owned and is **not**
enacted or predicted here.

### N7 — Steelman

Strongest objection: "additivity over sectors is itself an extra modeling
assumption; a physical readout might be non-additive (like `cos(arg)`), in which
case the phase is not erased." Response: additivity is **not** added here — it is
the Record axiom's (Additivity) clause, applied to the orthogonal central
idempotents that the axiom itself names as the decomposition. A non-additive
readout is simply not Record-registrable; admitting one would be adopting a new
readout primitive, which the no-new-primitive rule forbids. So the steelman
reduces to "drop the Record additivity clause", which is out of scope. The
theorem is correctly conditional on the Record-registrable class.

### N8 — Cross-cycle echo

The Record reclassification (Record moved from Tier-A to an approved axiom node)
retired a wall by an owner governance decision plus the minimality policy, not by
a new axiom. That is the template the AC_phi_lambda convention-class move would
follow — but only **after** this theory chain lands and the audit lane acts. This
note prepares that path (Consequence B) without enacting it. No structurally
similar wall was retired by a mechanism overlooked here.

## What this note does NOT claim

- It does **not** retire AC_phi_lambda or `theta`, edit the Tier-A registry, or
  remove bounded status from any consumer.
- It does **not** derive `|delta| = 2/9`, supply R-eta, or supply the global
  `Cl(3)/Z^3 -> PL S^3 x R` (R2) identification.
- It does **not** close strong-CP premise 1 ("no bare `theta` slot").
- It does **not** prove the physical readout context *must* be Record-supplied;
  it removes phase freedom *within* the registrable class.
- It introduces **no** new axiom, primitive, admission, normalization,
  probability rule, comparator, or audit verdict, and consumes no PDG / fitted /
  measured / lattice-MC value.
- It does **not** promote, demote, or set the audit status of any dependency.
  The independent audit lane is the only status authority.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the Record
  axiom boundary (the only premise of the theorem).
- [`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`](TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md)
  — the two named-open registrability bridges this note addresses, and the
  AC_phi_lambda circulant form (L2) consumed in Consequence B.
- [`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) — the
  selected-surface strong-CP premise whose mass-orientation phase content
  Consequence A discharges on the registrable surface.
- [`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
  — the distinct premise-1 no-go, cited to scope what Consequence A does NOT
  close.
- [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — where R2 (the global PL/ABSS bridge) is named open; cited to bound
  Consequence B.
- [`KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md`](KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — the `|delta|` magnitude chain conditional on R-eta; cited to bound what
  Consequence B leaves open.
- [`ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md`](ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md)
  — the finite complementation support; the orientation-odd `sin(3 delta)` line
  context for Consequence B.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status
authority.
