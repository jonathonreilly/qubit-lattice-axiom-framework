---
claim_id: record_accumulation_count_does_not_fix_wick_clock_map_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "A finite-window record-count clock N(R) is the same integer sequence for every Wick factor a, while continuation of the a-independent Euclidean form (k_4^2+k^2)/4 by k_4=i a ω yields three distinct ω^2 coefficients -1/16, -1/4, -1 at a=1/2,1,2, so neither Record accumulation nor the c_t=c_s primitive selects a."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive_note_2026-06-09
runner: scripts/record_accumulation_count_does_not_fix_wick_clock_map_2026_08_13.py
---

# Record Accumulation Count Does Not Fix The Wick Clock Map

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite-window record counts versus the linear continuation
`k_4 = i a ω` of the Euclidean TT form.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_accumulation_count_does_not_fix_wick_clock_map_2026_08_13.py`](../scripts/record_accumulation_count_does_not_fix_wick_clock_map_2026_08_13.py)

## Result Up Front

The four-axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
names Record formation, one-site locking, permanence, content-only readout,
and additive scalar `I` with `I(empty)=0`. The kinetic-isotropy primitive
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
states that the framework's time remains emergent and derived, and supplies
only the Euclidean kinetic-form equality

```text
c_t = c_s,
```

equivalently the Osterwalder-Schrader OS0 TT form

```text
Q_E(k_4, k) = (k_4^2 + k^2)/4.
```

A record-count clock on a finite window is a different object. For a
configuration `R` of locked sites, the accumulation count is the integer
`N(R)=|R|`. The chain `empty ⊂ {0} ⊂ {0,e1}` has counts `0,1,2`. That
sequence does not depend on a continuation parameter `a`.

The linear Wick map `k_4 = i a ω` applied to the same `Q_E` produces

```text
Q_a(ω, k) = (-a^2 ω^2 + k^2)/4,
```

with `ω^2` coefficient `omega_coeff(a) = -a^2/4`. The three values
`a = 1/2`, `a = 1`, `a = 2` return `-1/16`, `-1/4`, `-1`. Those three
rationals are distinct, while `Q_E` never sees `a`.

No Record sentence names `a`. The primitive's load-bearing sentence is
`c_t = c_s` only. Additive unit readout `I(R)=N(R)` is the same integer
and is likewise `a`-blind. A clock map `a` remains extra. This note does
not install a value of `a` and does not claim Lorentzian closure.

## Machine Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: wick_clock_map_a
target_blocker_text: "fix the Lorentzian/Wick clock map a from axioms or primitives"
source_of_blocker_text: handoff
reachability_to_target: prunes
next_trace_action: "Record counts and kinetic isotropy both leave a free. Do not adopt axiom text."
hypothetical_axiom_status: "no edit"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `e1` be a unit lattice step. The finite window is the four-site
segment

```text
W = {0, e1, 2 e1, 3 e1},    n = 4.
```

A **record configuration** is a subset `R ⊆ W`. The **accumulation
count** is the integer

```text
N(R) := |R|.
```

A **monotone chain** is a nested sequence `R0 ⊂ R1 ⊂ R2` with
`|Rk|=k`. The displayed chain is

```text
empty ⊂ {0} ⊂ {0, e1},
```

with counts `N = 0, 1, 2`. If each locked site contributes a unit
readout, content-only additivity with `I(empty)=0` gives
`I(R)=N(R)`.

Write `k^2 := kx^2 + ky^2 + kz^2`. The **Euclidean TT form** is

```text
Q_E(k_4, k) = (k_4^2 + k^2)/4.
```

The OS0 sentence `c_t = c_s` is the equality of the `k_4^2` and spatial
`k_i^2` coefficients, both `1/4`. The symbol `a` does not appear.

A **linear Wick clock map** is a nonzero scalar `a` together with
`k_4 = i a ω`. The **continued family** is

```text
Q_a(ω, k) := Q_E(i a ω, k) = (-a^2 ω^2 + k^2)/4.
```

The **Lorentzian `ω^2` coefficient** is

```text
omega_coeff(a) := [ω^2] Q_a = -a^2/4.
```

The three rejector values are `a ∈ {1/2, 1, 2}`.

| `a` | `omega_coeff(a)` | `Q_a` | recovered `Q_E` |
|---|---|---|---|
| `1/2` | `-1/16` | `-ω^2/16 + k^2/4` | `(k_4^2 + k^2)/4` |
| `1` | `-1/4` | `-ω^2/4 + k^2/4` | `(k_4^2 + k^2)/4` |
| `2` | `-1` | `-ω^2 + k^2/4` | `(k_4^2 + k^2)/4` |

| `R` | `N(R)` | `I(R)` at unit strength | for every displayed `a` |
|---|---|---|---|
| `empty` | `0` | `0` | `0` |
| `{0}` | `1` | `1` | `1` |
| `{0,e1}` | `2` | `2` | `2` |

The inverse substitution `ω = -i k_4 / a`, available whenever `a ≠ 0`,
returns the same Euclidean polynomial. That recovery identity is
independent of the particular nonzero `a`. The count table is independent
of `a` by construction: `N` is a cardinality.

## Exact Target And Obligation Graph

**Exact target.** Decide whether a Record accumulation count, or the
registered Euclidean equality `c_t = c_s`, selects the linear Wick
clock map `a` among the displayed family.

| Obligation | Role | Disposition |
|---|---|---|
| pin `c_t = c_s` and that time remains emergent and derived | premise | quoted from the primitive |
| pin `I(empty)=0`, content-only readout, and `Records form` | premise | quoted from the axiom memo |
| pin that Admissibility does not define a time metric | premise | quoted from the axiom memo |
| show `N(R)` is `a`-blind on the displayed chain | Theorem 1 | cardinality |
| show `a = 1/2, 1, 2` give `-1/16, -1/4, -1` | Theorem 2 | substitution `k_4 = i a ω` |
| show no source sentence names the clock map `a` | Theorem 3 | sentence pin |
| show unit `I(R)=N(R)` is still `a`-blind | Theorem 4 | additivity |
| adopt a value of `a` or claim Lorentzian closure | autonomous closure | open; not attempted |
| edit an axiom or primitive | non-claim | not attempted |

## Theorem 1 — Count Is `a`-Blind

`N(R)` is the number of locked sites in `R`. It is an integer determined
by the set `R` alone. The continuation parameter `a` is not an argument.

On the displayed chain

```text
N(empty) = 0,    N({0}) = 1,    N({0, e1}) = 2.
```

The same three integers are obtained for every `a ∈ {1/2, 1, 2}`. A
predicate `N_depends_on_a` that asserted a change of count with `a` is
false on this window: the three count triples coincide.

Therefore a record-count clock is the same integer sequence for every
displayed continuation. Accumulation count does not select `a`.

## Theorem 2 — Three Distinct Lorentzian Coefficients

The polynomial `Q_E = (k_4^2 + k^2)/4` is written in the Euclidean
momenta alone. The symbol `a` does not appear. Substituting
`k_4 = i a ω` gives

```text
(i a ω)^2 / 4 + k^2/4 = (i^2 a^2 ω^2)/4 + k^2/4
                      = (-a^2 ω^2)/4 + k^2/4.
```

So `omega_coeff(a) = -a^2/4`. Ordinary rational arithmetic yields

```text
omega_coeff(1/2) = -(1/4)/4 = -1/16,
omega_coeff(1)   = -1/4,
omega_coeff(2)   = -4/4     = -1.
```

These three rationals are pairwise distinct. In particular
`-1/16 ≠ -1/4`. The spatial coefficient stays `1/4` on every row, and
the inverse substitution `ω = -i k_4 / a` recovers the same `Q_E` on
every row.

A function of the Euclidean polynomial alone is constant on the family.
A function of the record-count chain is likewise constant on the family
(Theorem 1). Neither can equal the triple `(-1/16, -1/4, -1)`.

A constant replacement `omega_coeff ↦ -1/4` (the same value for every
`a`) collapses the triple and fails the distinctness statement
`-1/16 ≠ -1/4`. Inserting `a` already on the Euclidean side, as
`(a^2 k_4^2 + k^2)/4`, makes `Q_E` itself `a`-dependent and abandons
the primitive. Those replacements are not the claim.

## Theorem 3 — No Record Sentence Names `a`

The primitive's load-bearing sentence is the Euclidean equality
`c_t = c_s`. It states that the framework's time remains emergent and
derived, that it supplies only the kinetic-form ratio, and that it does
not add or amend an axiom. Its only quantity-level uses of the letter
`a` are the Lattice spatial adjacency `a_x = a_y = a_z` and the sibling
scale-reference identity `a^{-1} = M_Pl`. It does not write
`k_4 = i a ω`, does not name a Wick factor `a`, and does not select
among `{1/2, 1, 2}`. The wording "one tick is one edge in form, not
only in spacing" is the same Euclidean OS0 statement. It is not a
declaration that the continuation parameter equals `1`.

The axiom memo names four premises: Lattice, Qubit, Admissibility, and
Record. Record sentences used here are:

> Records form.

> When present, a record locks exactly one admissible local possibility.

> A readout value is determined by record content alone. For any finite
> collection of pairwise-disjoint records, scalar readout `I` is
> additive, with `I(empty)=0`.

The memo does not contain a governing sentence "time is emergent; the
arrow is monotone record accumulation." Time remaining emergent is
stated by the primitive. The memo lists arrow and time metric among the
open gates outside the four axioms. Admissibility "does not … define a
time metric." The interpretive gloss that the arrow is monotone record
accumulation is a count of locked sites: that is `N(R)` in Theorem 1,
and Theorem 1 is `a`-blind.

No axiom sentence and no primitive sentence names a Wick factor `a`.
Therefore neither Record accumulation nor the registered primitive
selects `a`.

## Theorem 4 — Additive `I` Is Also `a`-Blind

Suppose each locked site contributes unit strength `I=1`. Content-only
additivity and `I(empty)=0` then give

```text
I(empty) = 0,    I({0}) = 1,    I({0, e1}) = 2,
```

so `I(R)=N(R)` on the displayed chain. The right-hand side does not
depend on `a`. A content-only readout of locked possibilities carries
the locked content and the count of locked sites. It does not carry a
continuation parameter.

The same conclusion holds for any fixed per-site strength `q`: then
`I(R)=q N(R)`, still independent of `a`. The unit choice `q=1` is the
sharpest exhibit, not a hidden selector of `a`.

## Theorem 5 — Scoped Residual

A clock map `a` remains extra. Record counts, unit additive `I`, and
Euclidean `c_t = c_s` leave the three displayed continuations live.
This note does not install a value of `a`, does not claim Lorentzian
closure, and does not edit an axiom or primitive.

If a continuation rule is separately declared, then
`omega_coeff(a) = -a^2/4` is determined. That rule is a second object.
It is not `N(R)`, is not `I(R)`, is not `c_t = c_s`, and is not claimed
here to be physical.

## Boundary And Non-Claims

The note does not:

- edit an axiom or primitive, or argue that an axiom update is necessary;
- install `a = 1` or any other continuation as a physical law;
- claim Lorentzian reconstruction, boost generators, or OS reconstruction;
- vary `c_t / c_s` or reopen the Euclidean isotropy primitive;
- identify `omega_coeff(a)` with a mass ratio, coupling, or empirical fit;
- exhaust nonlinear clock maps;
- treat the interpretive accumulation gloss as axiom text.

The scope is the exact gap: Record accumulation counts, and the
registered primitive `c_t = c_s`, do not fix the Wick factor `a`.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | Whether a Record accumulation count already selects a Wick clock map `a`. The primitive sentence that time remains emergent and derived, the Record sentences `Records form` / content-only readout / `I(empty)=0`, and the count `N(R)` are quoted. They do not name `a`. |
| V2 | Present on `origin/main`? | Search of `origin/main` for a Wick clock map `a` derived from a Record accumulation count finds no such derivation. Existing Wick mentions are textbook or reconstruction conventions, not a count-to-`a` map. A kinetic-sided Euclidean-versus-continuation split is not on `origin/main`. |
| V3 | Textbook content? | Textbook Wick rotation is the convention `k_4 = i ω` (equivalently `a = 1`). It does not mention Record accumulation or a locked-site count `N(R)`. |
| V4 | Exact discriminating witnesses? | `N(empty)=0`, `N({0})=1`, `N({0,e1})=2`, and `omega_coeff(1/2)=-1/16 ≠ omega_coeff(1)=-1/4 ≠ omega_coeff(2)=-1`, with `Q_E` independent of `a`. |
| V5 | Corollary of the primitive note? | No. The primitive supplies `c_t = c_s` only. The Record-count chain and the signed triple `-1/16, -1/4, -1` are constructed here. |

## No-Go Discipline Gate

The negative claims are restricted to Theorems 3–5: no source sentence
names `a`, unit `I` is `a`-blind, and `a` remains extra. The gate does
not certify that a later declared clock map is impossible.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Record count `N(R)` | read `a` from the locked-site chain | Theorem 1: the chain is `0,1,2` for every displayed `a` | closed here |
| Additive unit `I` | read `a` from content-only `I(R)` | Theorem 4: `I(R)=N(R)`, still `a`-blind | closed here |
| Kinetic isotropy | read `a` from `c_t = c_s` | Theorem 2–3: `Q_E` is `a`-free; the primitive names only the Euclidean ratio | closed here |
| Force `a = 1` | treat "one tick is one edge" as Wick `a = 1` | that wording is Euclidean OS0 form, not a continuation; `omega_coeff(1/2) ≠ omega_coeff(1)` | closed here |
| Axiom edit | add a sentence naming `a` | not executed; Theorem 5 records that no edit is performed or required | not required |
| Lorentzian-closure import | import textbook `k_4 = i ω` as a law | V3: textbooks do not mention Record accumulation; import is extra | not imported |

Six routes. The first four fail as selectors of `a`. The last two remain
formal escapes and are not used as claims.

### N2 — wall independence

| Pair | First closes second? | Second closes first? | Disposition |
|---|---|---|---|
| `N(R)` / `omega_coeff(a)` | no: a cardinality does not produce `-a^2/4` | no: a continuation coefficient does not change `|R|` | independent |
| unit `I(R)` / `omega_coeff(a)` | no: `I=N` is still a count | no: `ω^2` coefficients do not alter additive readout | independent |
| `c_t = c_s` / `omega_coeff(a)` | no: Euclidean OS0 is `a`-free | no: three distinct Lorentzian coefficients share one `Q_E` | independent |
| `N(R)` / axiom edit | no: a count does not write axiom text | an edit would be a different object, not a count | distinct types |
| textbook `a = 1` / Record sentences | no: `k_4 = i ω` is not a Record sentence | Record formation does not mention Wick | distinct types |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `n = 4` | finite exhibit; not a lattice-wide exhaustion |
| chain `empty ⊂ {0} ⊂ {0,e1}` | one monotone chain with `|Rk|=k`; other chains have the same `a`-blindness |
| unit strength `I=1` | exhibit for Theorem 4; any fixed `q` remains `a`-blind |
| family `{1/2, 1, 2}` | three distinct nonzero rationals; not a classification of all `a ≠ 0` |
| `Q_E = (k_4^2+k^2)/4` | declared TT representative of `c_t = c_s`; reconstructed here |
| `k_4 = i a ω` | linear continuation; nonlinear maps are out of scope |
| interpretive accumulation gloss | used only as the reading `N(R)=|R|`; not written into the axiom memo |
| observations or fitted values | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | `Records form`; content-only readout; `I(empty)=0`; arrow and time metric listed outside the axioms; Admissibility does not define a time metric | quoted; no `a` is borrowed because none is present |
| [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | `c_t = c_s`; time remains emergent and derived; no axiom amendment; `a` used only as spacing or scale | quoted; continuation `a` is not supplied |

No citation is used as authority for the count triple or the signed
coefficient triple; those are computed here.

### N5 — rhetoric and resolution audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | each `a ∈ {1/2,1,2}` against the same chain and the same `Q_E` | no classification of every nonzero `a` |
| per site | locked-site cardinality on a four-site window | no composite carrier or formation-rate law |
| per mode | quadratic TT form in momenta `(k_4, k)` | no spectral-mode exhaustion |
| per block | Record count and Euclidean OS0 versus linear `a` | no Lorentzian closure |
| lattice-wide | checked and not executed | no lattice-wide Wick reconstruction |

The runner emits the same five scoped-negative lines.

### N6 — live partial-closure paths

1. A separately declared linear clock map would fix `omega_coeff(a)`.
2. A nonlinear clock map is outside the displayed family.
3. An axiom or primitive sentence that named `a` would change the
   Theorem 3 pin; no such sentence is present, and none is added.
4. Textbook Wick `a = 1` remains a conventional import, not a Record
   or OS0 derivation.
5. Lorentzian closure, if ever reached, would have to supply its own
   continuation rule. It is not imported here.

None of these paths is claimed physical. An axiom edit is not required
by the displayed algebra.

### N7 — hostile steelman

> Once time is read as monotone record accumulation, the count `N`
> already is the clock. The primitive's "one tick is one edge" then
> forces the continuation parameter to equal `1`, and the Lorentzian
> coefficient must be `-1/4`.

This steelman is rejected as a derivation, not as a possible later
declaration. `N` is an integer cardinality. The primitive's tick/edge
wording is Euclidean OS0 kinetic form. The continuation `k_4 = i a ω`
is a second map. The three displayed values of `a` share one count
chain and one `Q_E` and do not share `omega_coeff`. Accepting `a = 1`
would be an extra declaration.

### N8 — earlier-surface echo

| Earlier surface | What it does | Echo here |
|---|---|---|
| kinetic-isotropy primitive | supplies `c_t = c_s` only | used as the Euclidean parent; not a selector of `a` |
| axiom memo Record clauses | formation, lock, content-only `I`, `I(empty)=0` | used as the Record parent; count `N` is read off locking |
| record-tick / signature split already on `origin/main` | separates accumulation from a Lorentzian sign | the present residual is the scale `a`, not only the sign |
| unmerged kinetic-sided sibling | Euclidean OS0 versus continuation `a` | not a parent; the `a`-family is reconstructed locally |

Earlier surfaces separate time-as-count from metric signature. They do
not derive `a` from `N(R)`.

**Gate disposition:** the Record-count route, the unit-`I` route, the
`c_t = c_s` route, and the force-`a=1` route fail as selectors of `a`.
Do not ship "Lorentzian physics is impossible," "an axiom update is
necessary," or "a declared clock map cannot exist."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| primitive sentence `c_t = c_s`; time remains emergent and derived | premise | quoted; no edit |
| primitive non-amendment of the four axioms | premise | quoted; no edit |
| Record: `Records form`; content-only readout; `I(empty)=0` | premise | quoted; no edit |
| Admissibility does not define a time metric | premise | quoted; no edit |
| window `W`, count `N`, family `Q_a`, `omega_coeff` | declared algebra | computed here |
| physical Wick clock map `a` | escape route | live, not derived |

The exact advance is a finite count-versus-continuation theorem.
Independent audit remains required before any effective status may
change.

## Primary Runner

[`scripts/record_accumulation_count_does_not_fix_wick_clock_map_2026_08_13.py`](../scripts/record_accumulation_count_does_not_fix_wick_clock_map_2026_08_13.py)
recomputes `N(R)`, unit `I(R)`, the continuation `k_4 = i a ω`, and
`omega_coeff(a) = -a^2/4` in exact arithmetic, and re-reads the two
source notes.
