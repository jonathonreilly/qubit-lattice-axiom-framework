---
claim_id: speed_preserving_linear_wick_map_is_unit_clock_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Among linear Wick maps k4=i a ω of the Euclidean OS0 form (k4^2+k^2)/4, the declared extra matching that the Lorentzian null a^2 ω^2=k^2 coincide with Euclidean equal coefficients holds if and only if a^2=1, hence a∈{+1,-1} uniquely up to time-orientation; neither the four axioms nor c_t=c_s names that matching, and this note does not install a=1 or claim Lorentzian closure."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
runner: scripts/speed_preserving_linear_wick_map_is_unit_clock_2026_08_13.py
---

# Speed-Preserving Linear Wick Map Is The Unit Clock

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact algebra of the linear Wick family of the Euclidean OS0
TT form, under a declared extra speed-preservation matching.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/speed_preserving_linear_wick_map_is_unit_clock_2026_08_13.py`](../scripts/speed_preserving_linear_wick_map_is_unit_clock_2026_08_13.py)

## Result Up Front

The approved kinetic-isotropy primitive
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies one Euclidean kinetic-form equality,

```text
c_t = c_s,
```

equivalently the Osterwalder-Schrader OS0 kinetic normalization of the
Euclidean regulator block `Z^3 x Z_tau`. In momentum space that is the
declared Euclidean TT form

```text
Q_E(k4, k) = (k4^2 + k^2)/4,
```

where `k^2 = kx^2 + ky^2 + kz^2`. Both quadratic coefficients are `1/4`.
That is the primitive's content. The four-axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
does not define a time metric and does not name a continuation parameter.

A linear Wick clock map is a different object: the continuation

```text
k4 = i a ω,    a ∈ Q \ {0},
```

from Euclidean temporal momentum to a Lorentzian frequency. Substituting
into the same `Q_E` produces the family

```text
Q_a(ω, k) = ((i a ω)^2 + k^2)/4 = (-a^2 ω^2 + k^2)/4.
```

The Euclidean polynomial never sees `a`. The coefficient of `ω^2` is
`omega_coeff(a) = -a^2/4`. The spatial coefficient stays `1/4`.

**Speed-preservation** is a declared extra matching, not an axiom and
not a primitive sentence: the Lorentzian null `a^2 ω^2 = k^2` should
be the same as the Euclidean equal-coefficient null written in `ω`,
namely `ω^2 = k^2`. Equivalently `|omega_coeff(a)|` should equal the
spatial coefficient. That matching is `|a|^2 = 1`. For `a ∈ Q \ {0}`
one has `|a|^2 = a^2`, so

```text
speed_preserved(a)  ⇔  a^2 = 1  ⇔  a ∈ {+1, −1}.
```

The two solutions differ only by the sign of `k4 = i a ω`: they are
the two time-orientations of one unit clock. The values `a = 1/2` and
`a = 2` fail: they give `a^2 = 1/4` and `a^2 = 4`, with `ω^2`
coefficients `-1/16` and `-1` against spatial `1/4`.

Neither the four axioms nor `c_t = c_s` names speed-preservation across
Wick continuation. The uniqueness is therefore conditional on that extra
matching. This note does not install `a = 1` and does not claim Lorentzian closure.

## Machine Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The Euclidean TT polynomial is independent of a. Speed-preservation of that form across the linear Wick family is equivalent to a^2=1, hence a∈{+1,-1}. The matching is a declared extra condition: neither the four axioms nor c_t=c_s names it."
trace_class: negative_route_pruning
target_claim_id: speed_preserving_linear_wick_map_is_unit_clock
target_blocker_text: "select the linear Wick clock map a that preserves the OS0 speed from axioms or the kinetic-isotropy primitive"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact for the displayed Q_a family and the rational unit-clock solutions; the matching remains extra and Lorentzian closure remains open"
hypothetical_axiom_status: no edit
admitted_observation_status: null
next_trace_action: "Speed-preservation selects a=±1 uniquely among linear Wick maps. The matching is extra. Do not install a=1. Do not claim Lorentzian closure."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `k^2 := kx^2 + ky^2 + kz^2` for spatial Euclidean momentum. The
**Euclidean TT form** is the quadratic polynomial

```text
Q_E(k4, kx, ky, kz) = (k4^2 + k^2)/4.
```

Its temporal and spatial coefficients are

```text
[k4^2] Q_E = 1/4,    [kx^2] Q_E = [ky^2] Q_E = [kz^2] Q_E = 1/4.
```

The OS0 sentence `c_t = c_s` is exactly that equality of coefficients.
The overall `1/4` is the declared TT normalization; the primitive fixes
the ratio, and the displayed polynomial is the isotropic representative
with that normalization. The symbol `a` does not appear.

A **linear Wick clock map** is a nonzero rational `a` together with the
substitution `k4 = i a ω`. The **continued family** is

```text
Q_a(ω, k) := Q_E(i a ω, k) = (-a^2 ω^2 + k^2)/4.
```

The **Lorentzian `ω^2` coefficient** is

```text
omega_coeff(a) := [ω^2] Q_a = -a^2/4.
```

The **spatial coefficient** remains `1/4` on every row. The inverse
substitution `ω = -i k4 / a`, available whenever `a ≠ 0`, returns the
same Euclidean polynomial:

```text
Q_a(-i k4 / a, k) = (k4^2 + k^2)/4 = Q_E.
```

That recovery identity is independent of the particular nonzero `a`.

The Euclidean equal-coefficient null of `Q_E` is `k4^2 = k^2`. After
the linear substitution the Lorentzian null of `Q_a` is

```text
a^2 ω^2 = k^2.
```

**Speed-preservation** is the declared extra demand that this Lorentzian
null be the same as the Euclidean equal-coefficient null written in `ω`,

```text
ω^2 = k^2.
```

Those two quadratic cones coincide if and only if `a^2 = 1`.
Equivalently,

```text
speed_preserved(a) := (a * a == 1)
                  ⇔  |omega_coeff(a)| = 1/4
                  ⇔  a^2 / 4 = 1/4.
```

The identity gates of the companion runner are exactly
`omega_coeff(a) = -a^2/4` and `speed_preserved(a) := (a*a==1)`.

| `a` | `a^2` | `omega_coeff(a)` | spatial | `speed_preserved(a)` |
|---|---|---|---|---|
| `+1` | `1` | `-1/4` | `1/4` | true |
| `-1` | `1` | `-1/4` | `1/4` | true |
| `1/2` | `1/4` | `-1/16` | `1/4` | false |
| `2` | `4` | `-1` | `1/4` | false |

The two unit-clock rows share one quadratic form `Q_a`. They differ
only by the sign of the linear map `k4 = i a ω`.

## Exact Target And Obligation Graph

**Exact target.** Among linear Wick maps of the displayed OS0 TT form,
decide which nonzero rationals preserve the Euclidean equal-coefficient
speed, and decide whether that matching is already named by the four
axioms or by `c_t = c_s`.

| Obligation | Role | Disposition |
|---|---|---|
| pin `c_t = c_s` and the OS0 Euclidean wording | premise | quoted from the primitive |
| pin that the primitive does not add or amend an axiom | premise | quoted from the primitive |
| pin that Admissibility does not define a time metric | premise | quoted from the axiom memo |
| show `Q_E` has no `a` and is OS0 | Theorem 1 | coefficient comparison |
| show speed-preservation ⇔ `a^2 = 1` ⇔ `a ∈ {+1, −1}` | Theorem 2 | rational square |
| show `a = 1/2` and `a = 2` fail | Theorem 3 | `omega_coeff` versus spatial `1/4` |
| show no source sentence names the extra matching | Theorem 4 | sentence pin |
| install `a = 1` as an axiom or primitive | non-claim | not attempted |
| claim Lorentzian closure | non-claim | not attempted |

## Theorem 1 — The Euclidean Form Is Independent Of `a`

The polynomial `Q_E = (k4^2 + k^2)/4` is written in the Euclidean
momenta `(k4, kx, ky, kz)` alone. The symbol `a` does not appear. The
four quadratic coefficients are

```text
[k4^2] Q_E = 1/4 = [kx^2] Q_E,
```

which is `c_t = c_s` at the declared TT normalization. That is the OS0
statement.

For each nonzero `a`, the Euclidean member of the family is the same
polynomial: one obtains `Q_a` by substituting `k4 = i a ω`, and the
inverse substitution displayed above returns `Q_E` with no residual `a`.
Evaluating `Q_E` at any Euclidean point, for example
`(k4, k^2) = (2, 9)`, returns the single rational `13/4`, independent of
which continuation will later be used.

Therefore every member of the linear family shares one Euclidean OS0
form. The primitive, which speaks only about that Euclidean form,
cannot distinguish the members.

## Theorem 2 — Speed-Preservation Selects The Unit Clock

Substitute `k4 = i a ω` into `Q_E`:

```text
(i a ω)^2 / 4 + k^2/4 = (i^2 a^2 ω^2)/4 + k^2/4
                      = (-a^2 ω^2)/4 + k^2/4.
```

So `omega_coeff(a) = -a^2/4` and the spatial coefficient is `1/4`. The
Lorentzian null is `a^2 ω^2 = k^2`. The Euclidean equal-coefficient
null written in `ω` is `ω^2 = k^2`. These coincide if and only if
`a^2 = 1`.

Now `a ∈ Q \ {0}`. Write `a = p/q` in lowest terms with `q > 0`. Then
`a^2 = 1` means `p^2 = q^2`, hence `|p| = q`, hence `a ∈ {+1, −1}`.
Conversely both unit values satisfy `a^2 = 1`. Therefore

```text
speed_preserved(a)  ⇔  a * a == 1  ⇔  a ∈ {+1, −1}.
```

The two solutions give the same quadratic `Q_a = (-ω^2 + k^2)/4`. They
are unique up to time-orientation: `a ↦ -a` reverses the sign of the
linear clock map and leaves the quadratic form unchanged.

A predicate that replaced `speed_preserved` by true-for-all-`a` would
accept every nonzero rational, including `a = 1/2`. That replacement
is not the identity gate.

## Theorem 3 — The Maps `a = 1/2` And `a = 2` Fail

Ordinary rational arithmetic on the identity gate yields

```text
omega_coeff(1/2) = -(1/4)/4 = -1/16,
omega_coeff(2)   = -4/4     = -1.
```

Against spatial coefficient `1/4`:

```text
a = 1/2  ⇒  a^2 = 1/4 ≠ 1,   |-1/16| ≠ 1/4,
a = 2    ⇒  a^2 = 4   ≠ 1,   |-1|   ≠ 1/4.
```

So `speed_preserved(1/2)` is false and `speed_preserved(2)` is false.
The Lorentzian null at `a = 1/2` is `ω^2 = 4 k^2`. The Lorentzian
null at `a = 2` is `4 ω^2 = k^2`. Neither is the Euclidean
equal-coefficient cone `ω^2 = k^2`.

These two rejectors are the same rationals that already distinguish
members of the linear family by their `ω^2` coefficients. Speed-
preservation retains only the unit-clock rows.

## Theorem 4 — The Matching Is Extra; No Axiom Edit

The primitive's load-bearing sentence is the Euclidean equality
`c_t = c_s`, identified with OS0 hypercubic symmetry of `Z^3 x Z_tau`.
It states that it supplies only that kinetic-form ratio, that it does
not add or amend an axiom, and that it does not re-axiomatize time. Its
only quantity-level uses of the letter `a` are the Lattice spatial
adjacency `a_x = a_y = a_z` and the sibling scale-reference identity
`a^{-1} = M_Pl`. It does not write `k4 = i a ω`, does not name
speed-preservation across Wick continuation, and does not select
`a ∈ {+1, −1}`. The wording "one tick is one edge in form, not only
in spacing" is the same Euclidean OS0 statement. It is not a
declaration that the continuation parameter equals `1`.

The axiom memo names four premises: Lattice, Qubit, Admissibility, and
Record. Lattice is the cubic lattice `Z^3`. Record locks content and
supplies additive scalar readout `I` with `I(empty)=0`. Admissibility
determines a nearest-neighbor distribution and, in the memo's own
dynamics paragraph, does not define a time metric. No axiom sentence
introduces a continuation parameter `a`, a Lorentzian `ω^2`
coefficient, or a speed-preservation matching across Wick
continuation.

Therefore `|a| = 1` is conditional on the extra matching declared
above. This note does not install `a = 1`. This note does not claim Lorentzian closure. If a later construction wants a definite clock
map, it must declare the matching, or some other continuation rule,
as a second object. That declaration is a live formal escape. It is
not `c_t = c_s`, and it is not claimed here to be physical.

## Boundary And Non-Claims

The note does not:

- edit an axiom or primitive, or argue that an axiom update is necessary;
- install `a = 1` or any other continuation as a physical law;
- claim Lorentzian reconstruction, boost generators, or OS reconstruction;
- vary `c_t / c_s` or reopen the Euclidean isotropy primitive;
- identify `omega_coeff(a)` with a mass ratio, coupling, or empirical fit;
- exhaust nonlinear clock maps;
- treat speed-preservation as already named by the four axioms.

The scope is the exact gap: among linear Wick maps of the displayed
OS0 form, speed-preservation selects the unit clock, and that matching
is extra.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | Whether a speed-preserving linear Wick map of the OS0 form is unique, and whether the axioms or `c_t = c_s` already name that matching. |
| V2 | Present on `origin/main`? | Search of `origin/main` for a uniqueness theorem that `|a|=1` is the unique linear Wick map preserving OS0 speed finds no such derivation. Existing Wick mentions are textbook or reconstruction conventions, not this matching. |
| V3 | Textbook content? | Textbook Wick rotation is the convention `k4 = i ω` (equivalently `a = 1`). It does not isolate speed-preservation as an extra matching, and it does not prove uniqueness among nonzero rationals from `a^2 = 1`. |
| V4 | Exact discriminating witnesses? | `omega_coeff(1/2)=-1/16` versus spatial `1/4`; `omega_coeff(2)=-1` versus spatial `1/4`; `a=±1` give `-1/4` versus `1/4`. |
| V5 | Corollary of the primitive note? | No. The primitive supplies `c_t = c_s` only. Speed-preservation across Wick continuation is declared here and is not a primitive sentence. |

## No-Go Discipline Gate

The negative claims are restricted to Theorem 4: neither the four
axioms nor `c_t = c_s` names the extra matching, `|a|=1` remains
conditional, `a = 1` is not installed, and Lorentzian closure is not
claimed. Theorems 1–3 are positive algebra on the displayed family.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Euclidean OS0 as selector of `a` | read `a` from `Q_E` alone | Theorem 1: `Q_E` is `a`-free | closed here |
| Speed-preservation matching | impose `a^2 ω^2 = k^2` equal to `ω^2 = k^2` | Theorem 2: unique unit clock `a = ±1` | closed here, extra |
| Half-clock and double-clock | test `a = 1/2` and `a = 2` | Theorem 3: both fail | closed here |
| Force `a = 1` from the primitive | treat "one tick is one edge" as Wick `a = 1` | that wording is Euclidean OS0 form, not a continuation | Theorem 4 |
| Axiom edit | add a sentence naming `a = 1` | not executed; Theorem 4 records that no edit is performed or required | not required |
| Lorentzian-closure import | import textbook `k4 = i ω` as a law | V3: textbooks do not isolate the extra matching; import is extra | not imported |

Six routes. The first three are the algebra of this note. The last
three remain formal escapes and are not used as claims.

### N2 — wall independence

| Pair | First closes second? | Second closes first? | Disposition |
|---|---|---|---|
| `Q_E` / `speed_preserved(a)` | no: an `a`-free Euclidean form does not impose `a^2 = 1` | no: a matching on `Q_a` does not change `Q_E` | independent |
| `c_t = c_s` / `a = ±1` | no: Euclidean OS0 is `a`-free | no: the unit clock is a continuation statement | independent |
| `a = 1/2` rejector / axiom edit | no: a failed matching does not write axiom text | an edit would be a different object | distinct types |
| textbook `a = 1` / primitive sentence | no: `k4 = i ω` is not `c_t = c_s` | the primitive does not mention Wick | distinct types |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| linear family `k4 = i a ω` | declared class; nonlinear maps are out of scope |
| `a ∈ Q \ {0}` | rational clock maps; the square equation `a^2 = 1` is solved in `Q` |
| `Q_E = (k4^2+k^2)/4` | declared TT representative of `c_t = c_s`; reconstructed here |
| speed-preservation | declared extra matching, not a source sentence |
| family `{1/2, 1, 2, -1}` | unit-clock solutions plus two rejectors; not a classification of nonlinear maps |
| observations or fitted values | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice is `Z^3`; Admissibility does not define a time metric; Record supplies `I(empty)=0` | quoted; no Wick factor `a` is borrowed because none is present |
| [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | `c_t = c_s`; OS0 wording; no axiom amendment; `a` used only as spacing or scale | quoted; speed-preservation across Wick continuation is not supplied |

No citation is used as authority for `omega_coeff` or for the
equivalence `a^2 = 1 ⇔ a ∈ {+1, −1}`; those are computed here.

### N5 — rhetoric and resolution audit (Theorem 4)

Theorem 4 is the only negative claim. Its executed content is a
sentence pin plus two non-installations.

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | each displayed `a` is tested by `speed_preserved(a) := (a*a==1)` | no classification of every real or complex `a` |
| per site | statements are momentum-space quadratic forms | no composite carrier or formation-rate law |
| per mode | quadratic TT form in momenta `(k4, k)` | no spectral-mode exhaustion |
| per block | linear Wick family versus the extra speed matching | no Lorentzian closure |
| lattice-wide | checked and not executed | no lattice-wide Wick reconstruction |

Rhetoric that Theorem 4 does **not** license:

- "the four axioms force `a = 1`";
- "`c_t = c_s` already is Wick `a = 1`";
- "speed-preservation is a primitive sentence";
- "this note installs `a = 1`";
- "Lorentzian physics is closed" or "Lorentzian physics is impossible";
- "an axiom update is necessary."

The runner emits the same five scoped-negative lines. Replacing
`speed_preserved` by true-for-all-`a` must fail at `a = 1/2`; that
mutation is a check that Theorem 4's extra matching is load-bearing,
not a claim that every continuation is physical.

### N6 — live partial-closure paths

1. A separately declared speed-preservation matching would select
   `a = ±1` among linear maps, by Theorem 2.
2. A nonlinear clock map is outside the displayed family.
3. An axiom or primitive sentence that named `a` would change the
   Theorem 4 pin; no such sentence is present, and none is added.
4. Textbook Wick `a = 1` remains a conventional import, not an OS0
   derivation.
5. Lorentzian closure, if ever reached, would have to supply its own
   continuation rule. It is not imported here.

None of these paths is claimed physical. An axiom edit is not required
by the displayed algebra.

### N7 — hostile steelman

> Once `c_t = c_s` is granted, equal Euclidean coefficients already
> mean unit speed, so the only possible Wick map is `a = 1`. Installing
> that value is just spelling the primitive in Lorentzian language.

This steelman is rejected as a derivation, not as a possible later
declaration. The primitive's tick/edge wording is Euclidean OS0
kinetic form. The continuation `k4 = i a ω` is a second map. The
Euclidean polynomial is independent of `a` (Theorem 1). The values
`a = 1/2` and `a = 2` share that polynomial and fail speed-preservation
(Theorem 3). Accepting `a = 1` would be an extra declaration of the
matching in Theorem 2. Theorem 4 records that the extra declaration
is not a source sentence.

### N8 — earlier-surface echo

| Earlier surface | What it does | Echo here |
|---|---|---|
| kinetic-isotropy primitive | supplies `c_t = c_s` only | used as the Euclidean parent; not a selector of `a` |
| axiom memo | four named axioms; Admissibility does not define a time metric | used as the axiom parent; no Wick factor is present |
| textbook Wick convention | writes `k4 = i ω` | conventional `a = 1`, not a uniqueness proof from speed-preservation |

Earlier surfaces supply Euclidean OS0 form. They do not name
speed-preservation across Wick continuation, and they do not install
`a = 1`.

**Gate disposition:** the Euclidean-OS0-as-selector route fails. The
speed-preservation route selects the unit clock and remains extra.
Do not ship "Lorentzian physics is impossible," "an axiom update is
necessary," or "this note installs `a = 1`."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| primitive sentence `c_t = c_s` and OS0 wording | premise | quoted; no edit |
| primitive non-amendment of the four axioms | premise | quoted; no edit |
| axiom memo: `Z^3` Lattice; Admissibility does not define a time metric | premise | quoted; no edit |
| Euclidean TT form `(k4^2+k^2)/4` and family `Q_a` | declared algebra | computed here |
| speed-preservation matching | declared extra condition | not a source sentence |
| physical Wick clock map `a` | escape route | live, not installed |

The exact advance is a finite continuation-versus-matching theorem.
Independent audit remains required before any effective status may
change.

## Primary Runner

[`scripts/speed_preserving_linear_wick_map_is_unit_clock_2026_08_13.py`](../scripts/speed_preserving_linear_wick_map_is_unit_clock_2026_08_13.py)
recomputes the Euclidean TT polynomial, the continuation `k4 = i a ω`,
`omega_coeff(a) = -a^2/4`, and `speed_preserved(a) := (a*a==1)` in
exact arithmetic, and re-reads the two source notes.
