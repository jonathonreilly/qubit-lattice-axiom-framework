---
claim_id: y_like_spectrum_does_not_identify_u1y_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the taste cube C^8 the three residual-swap operators Y_a=(2 tau_a-I)/3 are pairwise distinct and isospectral with spec {+1/3 x6, -1 x2} and trace 0, so spectrum plus tracelessness do not select a unique generator or identify anomaly-complete U(1)_Y; the coefficient 1/3 is a scale choice and the (2,3)/(2,1) block names are extra representation-class data."
upstream_dependencies:
  - minimal_axioms
  - native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23
runner: scripts/y_like_spectrum_does_not_identify_u1y_2026_08_13.py
---

# Y-Like Spectrum Does Not Identify U(1)_Y

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact 8×8 residual-swap algebra on the taste cube `{0,1}^3`;
spectrum plus tracelessness of the native `Y_like` operators do not select
a unique generator or identify anomaly-complete `U(1)_Y`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_like_spectrum_does_not_identify_u1y_2026_08_13.py`](../scripts/y_like_spectrum_does_not_identify_u1y_2026_08_13.py)

## Result Up Front

The landed native abelian-surface note
[`NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md`](NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md)
constructs, for each selected axis of the taste cube `{0,1}^3`, a residual
complementary-axis swap `tau` and the traceless combination

```text
Pi_+ = (I + tau)/2,
Pi_- = (I - tau)/2,
Y_like = (1/3) Pi_+ - Pi_-.
```

It proves `spec(Y_like) = {+1/3 with multiplicity 6, -1 with multiplicity 2}`
and `Tr(Y_like)=0`. In the same opening claim-scope sentence it states that
this is only a hypercharge-like left-handed eigenvalue surface:

> It does not claim anomaly-complete `U(1)_Y`, electroweak matching,
> matter-completion labels, electric charge, or downstream phenomenology.

Anomaly notes later declare the identification of that surface with
anomaly-relevant Standard Model hypercharge as an extra premise P-HY. The
four-axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is an unedited
parent: its Lattice, Qubit, Admissibility, and Record sentences do not name
`Y_like` or `U(1)_Y`.

This note does not re-prove the native spectrum as a novelty. It recomputes
the closed form and the spectrum only as objects for a uniqueness
obstruction. Closed form:

```text
Y = (2 tau - I)/3
```

There are three residual swaps, one per selected axis. The three operators
`Y_0`, `Y_1`, `Y_2` are pairwise unequal as matrices on the supplied cube
basis and are isospectral. For rational `k`,

`spec(k Y_0) = {k/3 x6, -k x2}`,

and this equals the SM-like target `Σ_* = {+1/3 x6, -1 x2}` if and only if
`k=1`. In particular `k=1/3` has spectrum `{1/9 x6, -1/3 x2} ≠ Σ_*`.
Spectrum plus tracelessness therefore do not pick a unique generator, and
they do not force P-HY.

This is a scoped uniqueness gap. It does not claim that `U(1)_Y` is
impossible, and it does not adopt P-HY.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The three residual-swap generators are pairwise distinct and isospectral, and k=1 is the unique rational scale with spectrum Sigma_*. Spectrum plus trace therefore do not identify a unique operator as anomaly-complete U(1)_Y."
trace_class: negative_route_pruning
target_claim_id: y_like_u1y_identification
target_blocker_text: "Y_like ↔ U(1)_Y and hw=1 ↔ three families as explicit identification theorems"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "P-HY remains a declared identification; a commutation-with-SU(2)×SU(3) bridge or another selector is still open; do not adopt axiom text."
conditional_surface_status: "exact for three-axis distinctness and the k=1 scale rejector; physical U(1)_Y remains open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work on `C^8` with the orthonormal basis labeled by bits
`(x,y,z) ∈ {0,1}^3` in lexicographic order

```text
e0 = (0,0,0), e1 = (0,0,1), e2 = (0,1,0), e3 = (0,1,1),
e4 = (1,0,0), e5 = (1,0,1), e6 = (1,1,0), e7 = (1,1,1).
```

For a selected axis `a ∈ {0,1,2}`, write `tau_a` for the permutation matrix
of the coordinate swap of the other two axes:

```text
tau_0 : (x,y,z) |-> (x,z,y),
tau_1 : (x,y,z) |-> (z,y,x),
tau_2 : (x,y,z) |-> (y,x,z).
```

The permutation matrix is defined by `tau_a e_b = e_{swap_a(b)}`. It is a
real symmetric involution, hence Hermitian, and `tau_a^2 = I`.

The native projectors and generator are

```text
Pi_+^a = (I + tau_a)/2,
Pi_-^a = (I - tau_a)/2,
Y_a    = (1/3) Pi_+^a - Pi_-^a.
```

The SM-like target spectrum is the multiset

`Σ_* = {+1/3 (mult 6), -1 (mult 2)}`.

Eigenvalue multiplicities below are geometric: the multiplicity of a
rational `λ` for an 8×8 matrix `M` is `8 - rank(M - λ I)`, computed by
exact Gaussian elimination over `Q`. Because each `tau_a` satisfies
`tau_a^2 = I`, its minimal polynomial divides `x^2-1` and has distinct
roots, so `tau_a` and every rational polynomial in `tau_a` (including
`Y_a`) is diagonalizable. Geometric and algebraic multiplicities therefore
agree.

The four-axiom memo is quoted only as an unedited parent. No axiom sentence
is used as a selector among the three `Y_a`.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the native `Y_like` spectrum together with
tracelessness identifies a unique operator as anomaly-complete `U(1)_Y`.

| Obligation | Role | Disposition |
|---|---|---|
| pin native non-claim of anomaly-complete `U(1)_Y` | premise | quoted from the native abelian-surface note |
| pin unedited four-axiom memo | parent | no axiom sentence names `Y_like` |
| closed form `Y = (2 tau - I)/3` and spectrum `Σ_*` | Theorem 1 | recomputed on `±1` eigenspaces of `tau` |
| pairwise distinct isospectral `Y_0,Y_1,Y_2` | Theorem 2 | one disagreeing matrix entry per pair |
| scale rejector `k ≠ 1` | Theorem 3 | `k=1/3` gives `{1/9 x6, -1/3 x2}` |
| spectrum+trace do not force P-HY | Theorem 4 | scoped negative |
| `(2,3)`/`(2,1)` naming is extra | Theorem 5 | spectrum is basis-invariant |
| derive a unique physical `U(1)_Y` | autonomous closure | open |
| claim `U(1)_Y` is impossible | non-claim | not attempted |
| claim `hw=1` is not three families | non-claim | different object; not attempted |

## Theorem 1 — Closed Form And Spectrum

Fix an axis `a`. The residual swap `tau := tau_a` is a Hermitian involution:
each column of the permutation matrix has a single `1`, the map is an
involution of the eight basis labels, and the matrix is symmetric. Hence
`tau^2 = I` and `tau^† = tau`.

The combinations `Pi_+ = (I+tau)/2` and `Pi_- = (I-tau)/2` are complementary
orthogonal projectors. The number of fixed basis vectors of `tau` is four:
the selected bit is free and the two complementary bits are equal. Therefore

`Tr(tau) = 4`, `Tr(Pi_+) = (8+4)/2 = 6`, `Tr(Pi_-) = (8-4)/2 = 2`.

A projector’s rank equals its trace, so `rank(Pi_+)=6` and `rank(Pi_-)=2`.
Equivalently, `tau` has eigenvalue `+1` with multiplicity `6` and
eigenvalue `-1` with multiplicity `2`.

The native linear combination expands as

```text
Y_like = (1/3) Pi_+ - Pi_-
       = (I+tau)/6 - (I-tau)/2
       = (I+tau)/6 - 3(I-tau)/6
       = (I + tau - 3I + 3 tau)/6
       = (4 tau - 2 I)/6
       = (2 tau - I)/3.
```

Thus `Y_a = (2 tau_a - I)/3`. Applying this closed form to the eigenspaces
of `tau` gives the spectrum without a floating-point diagonalization:

- if `tau v = +v`, then `Y v = (2v - v)/3 = (1/3) v`;
- if `tau v = -v`, then `Y v = (-2v - v)/3 = -v`.

So `spec(Y_a) = {+1/3 x6, -1 x2} = Σ_*`. The trace is
`Tr Y_a = 0`:

`6*(1/3) + 2*(-1) = 0`.

The same ranks are recovered as

`rank(Y_a - (1/3) I) = rank(tau - I) = 2`,
`rank(Y_a + I) = rank(tau + I) = 6`,

hence the geometric multiplicities are `8-2=6` and `8-6=2`. This is a
recomputation of the native spectrum, not a novelty claim.

## Theorem 2 — Three Pairwise Distinct Operators

The three residual swaps are pairwise unequal as 8×8 matrices. A single
basis vector already separates them. On `e_{(0,0,1)}`:

```text
tau_0 e_{(0,0,1)} = e_{(0,1,0)},
tau_1 e_{(0,0,1)} = e_{(1,0,0)},
tau_2 e_{(0,0,1)} = e_{(0,0,1)}.
```

The corresponding matrix entries (row labeled by the image, column labeled
by `(0,0,1)`) disagree:

```text
(tau_0)_{(0,1,0),(0,0,1)} = 1,   (tau_1)_{(0,1,0),(0,0,1)} = 0,
(tau_0)_{(0,1,0),(0,0,1)} = 1,   (tau_2)_{(0,1,0),(0,0,1)} = 0,
(tau_1)_{(1,0,0),(0,0,1)} = 1,   (tau_2)_{(1,0,0),(0,0,1)} = 0.
```

In the lexicographic index these are the pairs of entries `(2,1)` and
`(4,1)`. Because `Y_a = (2 tau_a - I)/3`, the same entries of the generators
are `2/3` versus `0`. Therefore

`Y_0 != Y_1 != Y_2 != Y_0`.

By Theorem 1 every `Y_a` has spectrum `Σ_*` and trace `0`. The three
operators are isospectral and traceless, yet pairwise distinct. Spectrum
plus trace do not pick a unique generator on the supplied cube basis.

## Theorem 3 — Scale Rejector

Let `k` be rational. Then `k Y_0` is a rational polynomial in `tau_0`, so
it is diagonalizable on the same eigenspaces:

`spec(k Y_0) = {k/3 x6, -k x2}`.

This multiset equals `Σ_* = {1/3 x6, -1 x2}` if and only if `k=1`. Indeed
the two eigenvalues and their multiplicities must match:

- the assignment `k/3 = 1/3` and `-k = -1` forces `k=1`;
- the crossed assignment `k/3 = -1` and `-k = 1/3` requires `k=-3` and
  `k=-1/3` at once, which is impossible.

In particular the two scales that most often appear as alternative
normalizations fail:

```text
k=1/3: spec {1/9 x6, -1/3 x2} ≠ Σ_*,
k=-1:  spec {-1/3 x6, +1 x2} ≠ Σ_*.
```

The coefficient `1/3` in the native formula is a scale choice. It is not
forced by the demand that some traceless operator built from `tau` have a
two-point spectrum; it is forced only once the target multiset `Σ_*` is
already named.

## Theorem 4 — Spectrum Plus Trace Do Not Identify U(1)_Y

There is no theorem from the native `Y_like` spectrum and trace alone that
identifies a unique operator as anomaly-complete `U(1)_Y`. Three pairwise
distinct isospectral generators exist (Theorem 2). The native coefficient
`1/3` is a scale choice (Theorem 3). P-HY remains an extra identification,
declared in anomaly notes and explicitly refused as a claim by the native
surface note.

This note does not claim that `U(1)_Y` is impossible. It does not adopt
P-HY. It does not claim that `hw=1` fails to be three families: that is a
different object and is not addressed.

The N-gate below is the route audit for this scoped negative.

## Theorem 5 — Naming Residual

The spectrum `Σ_*` is a conjugation-invariant, basis-invariant fact about
each `Y_a`. The sentence that the six-dimensional `+1/3` block is the
representation class `(2,3)` and the two-dimensional `-1` block is the
representation class `(2,1)` is not a spectral fact. It names which factor
of a stipulated `C^2 ⊗ (C^2 ⊗ C^2)` splitting is the weak doublet and which
residual swap is the color swap.

The native construction does not supply those names. It supplies three
different residual swaps on one fixed cube basis. Assigning SM left-handed
content `(2,3)_{+1/3} + (2,1)_{-1}` is a representation-class naming, not a
consequence of `spec(Y_a)=Σ_*`. The name-free two-block algebra in
[`HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md)
likewise takes the `(2,3)+(2,1)` splitting as an input; it is a different
object and is not used as a premise here.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom-text change is required;
- claim that `U(1)_Y` is impossible, or that no later selector can pick a
  generator;
- adopt P-HY, or treat P-HY as a derived theorem;
- claim that `hw=1` is not three families;
- derive a commutation-with-`SU(2)×SU(3)` uniqueness lemma;
- identify any `Y_a` with electric charge, electroweak matching, or
  phenomenology;
- exhaust every traceless 8×8 matrix with spectrum `Σ_*`.

The scope is the exact gap: spectrum plus tracelessness of the native
`Y_like` family do not identify a unique anomaly-complete `U(1)_Y`.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| four-axiom memo | unedited parent | no axiom sentence names `Y_like` |
| native residual-swap construction and spectrum | common objects | recomputed; not claimed as novelty |
| native sentence “does not claim anomaly-complete `U(1)_Y`” | scope pin | quoted; not reversed |
| pairwise matrix disagreement and `k=1/3` rejector | declared algebra | computed here |
| P-HY identification | extra premise | not derived; not adopted |
| commutation with a supplied `SU(2)×SU(3)` action | escape route | live, not derived |

The exact advance is a finite uniqueness obstruction. Independent audit
remains required. This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The native note states that it does not claim anomaly-complete `U(1)_Y`. This note supplies the uniqueness obstruction: three isospectral distinct generators plus a scale rejector. It does not call the upstream surface unratified. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for `Y_like`, P-HY, and anomaly-complete. Hits: the native abelian-surface note constructs all three axes and refuses the identification; `HYPERCHARGE_IDENTIFICATION_NOTE` is name-free two-block algebra on a stipulated `(2,3)+(2,1)` splitting; ABJ and anomaly-forces-time notes declare P-HY as a premise. No landed pairwise-distinct plus scale rejector whose claim is that spectrum cannot identify `U(1)_Y` appears on that commit. |
| V3 | Textbook already? | No: textbook isospectrality does not mention the taste-cube residual swap or P-HY. |
| V4 | Discriminating exact witness? | Yes: exact pairwise matrix disagreement of `Y_0`, `Y_1`, `Y_2`, and the `k=1/3` spectrum `{1/9, -1/3}`. |
| V5 | One-step relabel? | No: not a restatement of the native non-claim sentence. Closest is that non-claim; this note adds the three-axis and scale rejectors. |

## No-Go Discipline Gate (Theorem 4)

The negative claim is restricted to: spectrum plus tracelessness of the
native `Y_like` family do not identify a unique operator as anomaly-complete
`U(1)_Y`. The gate does not ship a global non-existence theorem against
`U(1)_Y`.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| pick one axis by fiat | declare `Y_0` (or `Y_1`, or `Y_2`) to be the generator | typing: the three operators are already isospectral; the choice is extra data | **ATTEMPTED** |
| average the three `Y_a` | form `Y_bar = (Y_0+Y_1+Y_2)/3` | a different operator: `spec(Y_bar) = {+1/3 x4, -1/3 x4} ≠ Σ_*` | **ATTEMPTED** |
| scale `k ≠ 1` | replace `Y_0` by `k Y_0` | Theorem 3: `spec(k Y_0)=Σ_*` iff `k=1`; `k=1/3` gives `{1/9 x6, -1/3 x2}` | **ATTEMPTED** |
| P-HY declaration | identify some `Y_a` with anomaly-complete `U(1)_Y` by premise | extra premise, not a consequence of spectrum plus trace | **ATTEMPTED** |
| commute with a supplied `SU(2)×SU(3)` action | demand that the generator lie in a stipulated commutant | live escape; no such action is derived here | **ATTEMPTED** (escape) |
| edit the axiom memo | add a sentence that names a unique abelian generator | forbidden; no axiom sentence is edited | **ATTEMPTED** (forbidden) |

### N2 — wall independence

Theorem 4 closes only uniqueness from the native spectrum and trace. It
does not close a later commutation selector, a declared P-HY premise, or
the existence of some physical `U(1)_Y`. Those walls remain independent.
The `hw=1` versus three-families identification is a different object and
is not a wall of this note.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| taste cube `{0,1}^3` and the lex `C^8` basis | declared native object |
| selected axis `a` and residual swap `tau_a` | declared construction |
| coefficient `1/3` | scale choice; Theorem 3 |
| target multiset `Σ_*` | named comparison spectrum |
| P-HY identification | extra premise; not derived |
| `(2,3)+(2,1)` block names | representation-class input; Theorem 5 |
| conjugation / gauge orbit | extra data; not a uniqueness proof |
| `SU(2)×SU(3)` commutant selector | live escape; not executed here |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | four named axiom sentences; none names `Y_like` or `U(1)_Y` | quoted as an unedited parent only |
| [`docs/NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md`](NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md) | residual-swap construction, spectrum `Σ_*`, and the sentence that the note does not claim anomaly-complete `U(1)_Y` | objects recomputed; identification still refused |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | the three generators `Y_0`, `Y_1`, `Y_2` and the scales `k Y_0` | no classification of every traceless 8×8 matrix |
| per site | one `C^8` taste cube, not a lattice of spacetime sites | no composite multi-site theorem |
| per mode | eigenvalue multiplicities of `Y_a` via `rank(Y-λI)` | no harmonic-mode exhaustion |
| per block | three-axis distinctness and the `k=1` scale rejector only | no anomaly cancellation or electroweak matching |
| lattice-wide | checked and not executed | no lattice-wide identification of `U(1)_Y` |

The obstruction is per-cube / three-axis / declared residual swaps; it is
not lattice-wide.

### N6 — live partial-closure paths

1. A later selector that commutes a candidate generator with a supplied
   `SU(2)×SU(3)` action on the same `C^8`.
2. Any other selector that is not spectrum-plus-trace, including extra
   typing that names one axis.
3. A declared P-HY premise, kept as an extra identification and not
   derived from the native spectrum.

No axiom sentence is edited. The obstruction does not demand an axiom-text
change.

### N7 — hostile steelman

> The three operators `Y_a` are gauge-equivalent residual swaps, so they
> are the same `U(1)`.

**Answer.** Even if the three matrices are conjugate in some larger
automorphism group of the cube, conjugation is extra data. As operators on
the supplied cube basis they are unequal (Theorem 2). P-HY names one
physical hypercharge, not an orbit of conjugate generators. Passing to an
orbit, or supplying the conjugating map, is a different claim.

### N8 — cross-cycle echo

The native abelian-surface note already refuses anomaly-complete `U(1)_Y`
as a claim. Anomaly-forces-time notes declare P-HY as a premise. The
present negative is a different residual: spectrum plus trace do not
uniquely select a generator. The rejectors do not cancel the native
non-claim; they supply the uniqueness obstruction that non-claim left
implicit.

**Gate disposition.** PASS for the scoped obstruction that spectrum plus
trace do not identify a unique `U(1)_Y`. FAIL / DO NOT SHIP for
"`U(1)_Y` cannot exist" or "`hw=1` is not three families" (different
object; do not claim it).

## Primary Runner

[`scripts/y_like_spectrum_does_not_identify_u1y_2026_08_13.py`](../scripts/y_like_spectrum_does_not_identify_u1y_2026_08_13.py)
rebuilds each residual swap as an exact `Fraction` permutation matrix,
forms `y_like(axis)` from `tau(axis)` by the closed form
`Y = (2 tau - I)/3`, and recomputes projector ranks, the native linear
combination, traces, eigenvalue multiplicities by `rank(Y-λI)`, pairwise
matrix disagreement, and the scale rejector. Identity gates call
`y_like(axis)`. Replacing `y_like` by `k=1/3` times itself must fail the
spectrum-equals-`Σ_*` check. Replacing all three axes by axis `0` must
fail pairwise distinctness. Replacing `y_like` by `Pi_+` (spectrum
`{1 x6, 0 x2}`) must fail `Σ_*`.
