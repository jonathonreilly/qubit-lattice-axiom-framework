# Registrable Determinant-Character Readout Is Additive-Plus-Even Hence Phase-Free — Narrow Bounded Theorem

**Date:** 2026-06-10 (2026-06-12: two boundary-naming citations — the |delta|-magnitude chain note and the hw-complementation support note — are demoted from dependency links to context; both are cited only to name what this note does NOT close, and the sin(3 delta) / symmetric-function facts used by Conditional Implication B are verified directly in the primary runner. 2026-06-16: post-audit source firewall removes bridge-discharge language and scopes both downstream uses as conditional algebra inside the supplied readout context. 2026-06-18: algebraic-core split added in [`REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md`](REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md), isolating the determinant-character phase-erasure algebra from the physical strong-CP and AC_phi_lambda readout identifications.)
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** source-side claim-boundary declaration only — a narrow conditional
theorem on the Record-registrable determinant-character / log-character
homomorphism readout class. `proposed_retained` is **not** asserted; the
boundary below is a source-side declaration, not an audit verdict.
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome and does not edit the audit-lane-owned Tier-A
registry, ledger, queue, or publication-status surfaces.
**Primary runner:**
[`scripts/frontier_registrable_readout_additive_even_phase_free_2026_06_10.py`](../scripts/frontier_registrable_readout_additive_even_phase_free_2026_06_10.py)
(latest local run: SCORECARD: PASS=46, FAIL=0; paired cached log:
[`logs/runner-cache/frontier_registrable_readout_additive_even_phase_free_2026_06_10.txt`](../logs/runner-cache/frontier_registrable_readout_additive_even_phase_free_2026_06_10.txt))
**Scope guard runner:**
[`scripts/frontier_registrable_readout_phase_homomorphism_scope_guard_2026_06_12.py`](../scripts/frontier_registrable_readout_phase_homomorphism_scope_guard_2026_06_12.py)
(TOTAL: PASS=8, FAIL=0; cached:
[`logs/runner-cache/frontier_registrable_readout_phase_homomorphism_scope_guard_2026_06_12.txt`](../logs/runner-cache/frontier_registrable_readout_phase_homomorphism_scope_guard_2026_06_12.txt))

## Boundary

This note proves one narrow structural theorem about scalar readouts in a
supplied readout context satisfying the **Record** constraints plus an explicit
determinant-character / log-character homomorphism boundary for the
phase-bearing determinant component. It records the conditional algebra that
the two registrability bridges named open by
[`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`](TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md)
could use if a separate physical-readout theorem supplies the missing
identification.

It does **not** retire either Tier-A admission, edit
`docs/audit/data/tier_a_admissions.json`, remove bounded status from any
consumer, derive `|delta| = 2/9`, supply the global `Cl(3)/Z^3 -> PL S^3 x R`
identification, close strong-CP premise 1 ("no bare `theta` slot"), or change
the Record axiom boundary. It does **not** derive phase-group additivity from
Record finite additivity. It supplies a registrability structure theorem on the
explicit determinant-character / log-character homomorphism surface and two
conditional downstream implications, with the surviving residuals named
explicitly. It does **not** discharge, close, or exhaust the physical
strong-CP mass phase or AC_phi_lambda species readout bridges.

## The Record boundary and the extra homomorphism boundary

From [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md), the
**Record** axiom states that, in a *supplied* readout context with a finite
central-sector decomposition and a fixed `K`/CPT conjugation:

1. **(Additivity)** the scalar readout `I` is finitely additive over finite
   pairwise-disjoint record collections, with `I(empty) = 0`;
2. **(Orbit)** the realized outcome is the `K`/CPT orbit of the realized central
   sector.

It supplies **no** readout context, decomposition, `K`/CPT structure,
sector-generation rule, weighting, normalization, probability, modulus rule,
log-det, source/action, scale, or observable identification. The theorem below
uses (Additivity) and (Orbit) only for those two Record conclusions.

The theorem also assumes, as part of the supplied readout context and **not** as
a consequence of Record, that the determinant phase-bearing component lies in a
determinant-character / log-character homomorphism class: for sector-factored
multiplicative determinant data, the phase component is an `R`-valued group
homomorphism of the per-sector phase variables. This is a modeling/readout
surface restriction, not a new axiom and not a derived Record fact. Record
finite additivity alone still admits K-even phase-dependent functions such as
`sum_j cos(theta_j)` over disjoint records; those functions are excluded only by
the determinant-character / log-character homomorphism boundary.

## The theorem

> **Theorem (registrable determinant-character readout is additive-plus-even,
> hence phase-free).**
> Let a scalar readout be *Record-registrable*: a scalar assigned to records
> that is (i) finitely additive over pairwise-disjoint records [(Additivity)]
> and (ii) constant on `K`/CPT orbits of the realized central sector [(Orbit)].
> Suppose in addition that its determinant phase-bearing component is a
> determinant-character / log-character homomorphism on sector-factored
> multiplicative determinant data. Then on a finite central-sector decomposition
> that homomorphic per-sector **phase** contribution is identically zero.
> Equivalently, the phase index of a multiplicative determinant character
> `chi_k(z) = exp(i k arg z)` must be `k = 0`; phase-free modulus/log-modulus
> data is the determinant-class datum that can survive these constraints.

### Proof (each leg checked in the runner)

**T1 — the central sectors define disjoint record labels.** In the supplied
readout context, the finite central-sector decomposition is a set of orthogonal
central idempotents `e_j` with `e_j e_k = 0` (`j != k`) and `sum_j e_j = 1`.
Orthogonality is disjointness, so the associated record labels are
pairwise-disjoint.

**T2 — Record additivity forces a per-record sum with no interference.** Posit
the most general two-sector readout permitting a cross term,
`I(e_1 cup e_2) = I(e_1) + I(e_2) + c`. (Additivity) is exactly
`I(e_1 cup e_2) = I(e_1) + I(e_2)`, which forces `c = 0`. Iterating over the
finite family, a registrable readout equals `sum_j I(e_j)`; there is no
cross-record / interference content. This is finite additivity over records; by
itself it is **not** phase-group additivity of an arbitrary phase function.

**T3 — the homomorphism boundary puts determinant phase in the additive
class.** For a sector-factored configuration `det = prod_j z_j`, so
`arg det = sum_j arg(z_j)` (mod `2 pi`). The determinant-character /
log-character boundary says the phase-bearing readout component is an
`R`-valued group homomorphism of this per-sector phase data. This is the step
that supplies additivity on the phase group; it is not inferred from Record
finite additivity.

**T4 — an additive functional is odd (no regularity needed).** For any
`R`-valued additive `g` on an abelian group, `g(0) = g(0) + g(0)` gives
`g(0) = 0`, and `g(x) + g(-x) = g(0) = 0` gives `g(-x) = -g(x)`. This is pure
algebra; **no continuity, measurability, or linearity is assumed**, so the
Cauchy/Hamel pathology of additive functions is irrelevant here.

**T5 — even ∩ additive = zero.** (Orbit) makes the readout constant on `K`/CPT
orbits; `K`/CPT acts on the central characters as complex conjugation, sending
`arg z` to `-arg z`. So the homomorphic phase functional is also **even**:
`g(-t) = g(t)`. Even (`g(-t) = g(t)`) together with odd (T4:
`g(-t) = -g(t)`) gives `g(t) = -g(t)`, hence `g(t) = 0` for every `t`. The
homomorphic determinant-character phase contribution vanishes; equivalently the
determinant-character phase index is `k = 0`.

**T6 — the hostile guard is threaded.** `K`/CPT-evenness *alone* does **not**
erase phase: `cos(arg z)` is `K`-even (`cos(-theta) = cos(theta)`) yet
phase-dependent. Nor does Record finite additivity alone erase all K-even phase
functions: `sum_j cos(theta_j)` is finitely additive over disjoint sector
records and K-even while still phase-dependent. The theorem does not exclude
that counterexample by Record. It excludes it only because
`sum_j cos(theta_j)` is not a determinant-character / log-character group
homomorphism of the per-sector phase data. It is precisely the **intersection**
homomorphic additive ∩ even that is the phase-free class.

**T7 — the surviving datum is modulus-type.** `log|z|` is additive
(`log|z_1 z_2| = log|z_1| + log|z_2|`) and `K`-even (`|conj z| = |z|`), so it
survives registration on this homomorphism surface. The registrable
determinant-class phase index is therefore `k = 0`; modulus/log-modulus data is
the surviving phase-free class within the determinant-character /
log-character boundary.

## Conditional Implication A — strong-CP determinant-readout algebra (blocker (a))

The named-open bridge in the Tier-A K/CPT note asks that the physical
`arg det(M_u M_d)` contribution used by
[`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) be represented
by the determinant-class registrable readout, with no phase-sensitive
non-multiplicative or action-level datum remaining relevant to that premise.
This note does not prove that physical identification.

`arg det(M_u M_d) = arg det M_u + arg det M_d` is the additive sector-phase sum
(T3, T8 in the runner). By T5 its determinant-character / log-character
homomorphic registrable content is zero: on that Record-compatible
homomorphism surface the determinant **phase** vanishes by the `k = 0`
(modulus) character. Broader K-even record-additive phase functions, including
per-sector `sum cos(theta_j)`, are not ruled out by Record; they are outside
this homomorphism theorem. The
multiplicative determinant-character class is therefore phase-free for the
supplied determinant-character **phase** readout only under the explicit
determinant-character / log-character boundary.

This is a conditional algebraic implication, not a bridge discharge. To use it
as a strong-CP source-side bridge input, a separate retained theorem still has to
identify the physical mass-orientation readout with this supplied
Record-registrable determinant-character / log-character surface and rule out
additional action-level orientation-sensitive data.

The 2026-06-18 algebraic-core split note isolates the exact determinant-character
phase-erasure theorem as its own source-side exact-support artifact. That split
does not discharge this paragraph's physical mass-readout identification; it
only makes the algebraic core separately reviewable.

Registry tracking guard (context only): the Tier-A registry names the shared
K-real mass-side structure between theta(b) and AC_phi_lambda(i), but it also
states that the two move only after the determinant-readout / exhaustion bridge
is closed, not by registry wording alone. This note therefore does not replace
the missing bridge theorem with a Tier-A dependency edge.

**What Conditional Implication A does NOT close** (carried, not erased):

- **Strong-CP premise 1**, "no bare `theta` slot is admissible", is a *separate*
  action-surface premise. It was shown not derivable from retained reflection
  positivity by
  [`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md).
  This note addresses only the mass-orientation **phase**, not premise 1.
- **The standing modeling identification** — that the physical mass-surface
  readout context satisfies the Record registrability constraints and the
  determinant-character / log-character homomorphism boundary for its
  phase-bearing determinant component — is unchanged. The theorem removes the
  phase freedom *within* that constrained class; it does not prove the physical
  readout must be registrable or homomorphic in this sense. That
  identification remains the strong-CP / AC_phi_lambda modeling premise.

## Conditional Implication B — AC_phi_lambda unordered-multiset algebra (blocker (b-i))

The same Tier-A note's registry consequence asks for the **unordered-multiset
registrability bridge** before the orientation lemma can reduce AC_phi_lambda to
a magnitude-only atom.
This note does not prove that the physical species readout is exactly that
unordered-multiset surface.

For the AC_phi_lambda Hermitian circulant
`H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T`, the runner verifies
`conj(H(delta)) = H(-delta)`: the `delta -> -delta` sign flip **is** the `K`/CPT
conjugation. The elementary symmetric polynomials are all **even** in `delta`
(`e_1 = 3a`; `e_2 = 3a^2 - 3B^2`;
`e_3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta)`), so the unordered eigenvalue
multiset is `K`-even and Record-registrable as orbit data. The sign of `delta`
lives only in the orientation-odd `sin(3 delta)` line, which is `K`-**odd** and
therefore not a scalar on the realized `K`/CPT orbit unless it is collapsed to
zero or to the unordered orbit. This conditional implication uses the Orbit
clause directly; it does not require pretending that every K-even phase
function is determinant-character additive.

Hence, inside the supplied Record-registrable unordered-multiset context, the
surviving scalar species data is the unordered mass multiset (the symmetric
functions), and the sign / orientation of `delta` is not extra scalar orbit
content. This conditionally isolates the sign-erasure algebra that a later
physical-readout bridge would need; it does not by itself reduce the physical
AC_phi_lambda admission to the magnitude-only atom `|delta|`.

**What Conditional Implication B does NOT close** (carried, not erased):

- The `|delta|` **magnitude** value (`2/9`) and its single-summand readout still
  depend on the named readout identification **R-eta** of
  `KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  (context, not load-bearing: cited only to name the open magnitude chain)
  and on the global geometry **R2** below. This note removes only the **sign**
  as extra content.
- **R2, the PL/ABSS equivariant global bridge** — the global geometric
  identification `Cl(3)/Z^3 -> PL S^3 x R` named open in
  [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  (Part D) — is **off this layer**. It is a manifold-topology statement
  provably requiring the PL Poincaré conjecture (Perelman), TOP = PL in
  dimension 3 (Moise), and van Kampen `pi_1 = 0`. These are standard external
  mathematics, named LIVE there, **not** on the framework surface, and **not** a
  question of what Record registers. The unordered-multiset algebra here is
  independent of R2: it asks only whether the already-computed symmetric data is
  invariant on the supplied orbit surface. R2 therefore remains a separate
  import-required wall (see the no-go discipline section), not addressed by this
  note.

## Why these two bridges share one Record layer

Both bridges are the *same* Record-registrability question — what scalar a
registrable readout carries on a finite central-sector decomposition modulo
`K`/CPT. Blocker (a) additionally needs the determinant **phase** readout to be
on the determinant-character / log-character homomorphism surface, where
additive ∩ even kills the phase index. Blocker (b-i) needs the eigenvalue
**sign/orientation** to fail scalar orbit invariance, while the unordered
symmetric functions survive. The consumers share the Record orbit/additivity
layer, but the determinant phase-erasure claim no longer asserts that Record
alone supplies phase-group additivity.

## Net

```text
Record boundary (Additivity + K/CPT orbit)
  + determinant-character / log-character homomorphism boundary for phase readout
  => homomorphic determinant phase contribution = 0   (homomorphism forces odd; even forces zero)
  => (a) det-class phase character k=0 on the supplied homomorphism surface;
     physical arg det(M_u M_d) identification still open
  => (b-i) delta-sign is not scalar orbit content on the supplied unordered
     multiset surface; physical AC_phi_lambda readout identification still open

new axioms: 0     new primitives: 0     new admissions: 0     new imports: 0
residuals named: strong-CP premise 1 (separate); standing readout-context /
                 homomorphism premise; |delta| magnitude (R-eta);
                 R2 PL/ABSS global bridge (external-math LIVE)
```

## No-Go / Bounded-Wall Discipline Gate (N1–N8)

This note is a conditional positive theorem with a named external-math residual
(R2). The discipline gate is applied to the residual claim "R2 remains an
import-required wall, off the Record layer."

### N1 — Alternative route enumeration (≥5) for the R2 residual

| route | what it would attempt | result | marker |
|---|---|---|---|
| Record-registrability supplies R2 | derive the global PL `S^3` identification from what Record registers | FAILS: R2 is manifold topology, not a readout-class question; Record supplies no geometry | RULED OUT (category mismatch) |
| Finite-R cone-cap → global PL | identify the compactification with `PL S^3` from finite caps | FAILS: Euler characteristic blind among closed orientable 3-manifolds | RULED OUT BY PRIOR (`KOIDE_APS_C3_FIXED_LOCUS_...` D2) |
| Local ABSS prerequisites ⇒ global | upgrade the local Morse-Bott/spin/lift checks to the global identification | FAILS: local checks are conditional on the ambient already being `PL S^3 x R` | RULED OUT BY PRIOR (same note, Part C) |
| Replace R2 with a new geometric primitive | adopt the `PL S^3` ambient as a framework primitive | INFEASIBLE: no-new-primitive rule; this would be an unapproved primitive | RULED OUT (policy) |
| Import Perelman/Moise/van Kampen as derivation steps | use the external theorems to close R2 inside the framework | NOT a closure: these are external math; they may be a named open / disclosed comparator, never a derivation step on the framework surface | ATTEMPTED → bounded (import-required) |
| Unordered-multiset algebra avoids R2 | show the supplied-orbit sign-erasure calculation does not route through R2 | SUCCEEDS only as conditional algebra: R2 is not used in the symmetric-function parity check; physical readout identification remains open | ATTEMPTED -> conditional algebra isolated, R2 still open |

Six routes named; the residual is correctly bounded, not a premature no-go.

### N2 — Wall-independence audit

The surviving walls are independent: (W1) strong-CP premise 1 (action-surface
admissibility of a bare `theta` slot); (W2) the standing readout-context
identification (physical readout satisfies the Record registrability
constraints and the determinant-character / unordered-multiset surfaces);
(W3) the `|delta|`
magnitude via R-eta; (W4) R2 the global PL/ABSS identification. None follows from
another: W1 is about the gauge action, W2 about modeling the readout, W3 about a
dimensionless readout identification, W4 about manifold topology. The theorem
collapses none of them into another; it removes phase/sign freedom only inside
the supplied readout class.

### N3 — Hidden-wall scan

Load-bearing premises are explicit: (Additivity) and (Orbit) from Record; the
determinant-character / log-character homomorphism boundary for the phase
component; the sector-factoring of `det`; the AC_phi_lambda circulant form
(consumed from the Tier-A note's L2). No "we assume", "by construction",
"naturally", or "registered" smuggles a hidden admission: each use of
"registrable" is the explicit Record (Additivity)+(Orbit) data, the
homomorphism restriction is separately named, and each external-math name
(Perelman/Moise/van Kampen) is flagged as the open R2 route, not assumed.

### N4 — Residual matching

The cited witnesses match exactly: the RP no-go attacks strong-CP **premise 1**
(matched, and explicitly NOT this note's target); the `KOIDE_APS_C3_FIXED_LOCUS`
Part D attacks the **global PL identification** (matched as R2); the
`KOIDE_DELTA_ETA_DENSITY` chain attacks the **magnitude via R-eta** (matched).
No witness is repurposed.

### N5 — Rhetoric audit

"The homomorphic determinant phase is zero on the supplied readout surface" is verified only at the
determinant-character / log-character homomorphism resolution (T3–T5) and the
product-determinant resolution (T8); it is **not** claimed for arbitrary
Record-additive K-even phase functions (T6 keeps `sum cos(theta_j)` as the
guard). "Reduces to the magnitude-only atom" is the sign/orientation removal
only inside the supplied unordered-multiset context; the physical readout
identification and magnitude are explicitly left open. "Off this layer" for R2
is the category claim (topology vs. readout class), checked as a boundary
witness (T10).

### N6 — Partial-closure path scan

No new axiom or primitive is proposed. The legitimate closure path for the
physical-readout wall is a separate retained theorem identifying the strong-CP
mass phase and AC_phi_lambda species data with the supplied Record-registrable
surfaces used here. The legitimate closure path for R2 is to
**derive or audit** the global identification on the framework surface (the
external-math content), exactly as `KOIDE_APS_C3_FIXED_LOCUS_...` records it
LIVE. The AC_phi_lambda convention-class reclassification (the Y0 precedent) is
a possible *downstream* registry move, but it is audit-lane owned and is **not**
enacted or predicted here.

### N7 — Steelman

Strongest objection: "`sum_j cos(theta_j)` is finitely additive over disjoint
records and K-even, yet remains phase-dependent. Therefore Record alone cannot
prove phase erasure." Response: correct. This note no longer claims that Record
finite additivity implies phase-group additivity. The phase-erasure theorem is
conditional on the explicit determinant-character / log-character homomorphism
surface, where additivity is group-homomorphic in the phase variables. If the
physical readout allows broader K-even record-additive functions, the phase is
not erased by this theorem; that broader surface is outside the claimed
closure. The theorem is correctly conditional on the Record-registrable
homomorphism class.

### N8 — Cross-cycle echo

The Record reclassification (Record moved from Tier-A to an approved axiom node)
retired a wall by an owner governance decision plus the minimality policy, not by
a new axiom. That is the template the AC_phi_lambda convention-class move would
follow — but only **after** this theory chain lands and the audit lane acts. This
note records conditional algebra for that path without enacting it. No structurally
similar wall was retired by a mechanism overlooked here.

## What this note does NOT claim

- It does **not** retire AC_phi_lambda or `theta`, edit the Tier-A registry, or
  remove bounded status from any consumer.
- It does **not** derive `|delta| = 2/9`, supply R-eta, or supply the global
  `Cl(3)/Z^3 -> PL S^3 x R` (R2) identification.
- It does **not** close strong-CP premise 1 ("no bare `theta` slot").
- It does **not** prove the physical readout context *must* satisfy the Record
  registrability constraints or the determinant-character / log-character
  homomorphism boundary; it removes phase freedom *within* that class.
- It does **not** derive phase-group additivity from Record finite additivity.
- It introduces **no** new axiom, primitive, admission, normalization,
  probability rule, comparator, or audit verdict, and consumes no PDG / fitted /
  measured / lattice-MC value.
- It does **not** promote, demote, or set the audit status of any dependency.
  The independent audit lane is the only status authority.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the Record
  axiom boundary (finite record additivity and `K`/CPT orbit invariance).
- [`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`](TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md)
  — the two named-open registrability bridges that motivate the conditional
  algebra here, and the AC_phi_lambda circulant form (L2) consumed in
  Conditional Implication B.
- [`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) — the
  selected-surface strong-CP premise whose mass-orientation phase content
  Conditional Implication A bounds only after a separate physical-readout
  identification is supplied.
- [`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
  — the distinct premise-1 no-go, cited to scope what Conditional Implication A
  does NOT close.
- [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — where R2 (the global PL/ABSS bridge) is named open; cited to bound
  Conditional Implication B.

Context (not load-bearing: cited only to name boundaries; no content is consumed):

- `KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md` — names
  the still-open `|delta|` magnitude chain (R-eta) that Conditional Implication B explicitly does
  NOT close; the theorem and both conditional implications consume no content
  from it.
- `ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md` —
  corroborating context for the orientation-odd `sin(3 delta)` line; the
  symmetric-function evenness and `sin(3 delta)` K-oddness used by Conditional
  Implication B are verified directly in this note's primary runner, so no
  content is consumed from the support note.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status
authority.
