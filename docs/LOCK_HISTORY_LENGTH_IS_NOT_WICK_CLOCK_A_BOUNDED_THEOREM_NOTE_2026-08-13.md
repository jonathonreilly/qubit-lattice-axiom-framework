---
claim_id: lock_history_length_is_not_wick_clock_a_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Live Record plus a finite lock-history length n does not name the Wick clock parameter a_w. Two lawful histories with n=2 and n=4 share no readout of blank sites. The OS0 form Q_E=(k4^2+k^2)/4 continued by k4=i a_w omega has omega_coeff(a_w)=-a_w^2/4; omega_coeff(1)=-1/4 and omega_coeff(2)=-1 are distinct and equal neither n nor 1/n. Kinetic isotropy is c_t=c_s, not a function of |H|. Independent of the Q_E/Q_lopsided |a| split and of a_sr versus a_w. The note does not install a_w=1 and does not adopt L_phys."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive_note_2026-06-09
runner: scripts/lock_history_length_is_not_wick_clock_a_2026_08_13.py
---

# A Lock-History Length Is Not The Wick Clock Parameter `a`

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite lock-history lengths versus the linear Wick
continuation `k4 = i a_w omega` of the Euclidean OS0 form.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/lock_history_length_is_not_wick_clock_a_2026_08_13.py`](../scripts/lock_history_length_is_not_wick_clock_a_2026_08_13.py)
**Parents on origin/main:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md).

## Result Up Front

Live Record, with no named `I` and with blank sites unread, plus a history
of `n` locks, does not name the Wick clock parameter `a_w`.

1. Two lawful lock words have lengths `n=2` and `n=4`. Blank unread
   forbids assigning a readout to empty sites in order to manufacture a
   clock.
2. After `k4 = i a_w omega` in the OS0 form `Q_E = (k4^2 + k^2)/4`, one
   has `omega_coeff(a_w) = -a_w^2/4`. Then `omega_coeff(1) = -1/4` and
   `omega_coeff(2) = -1` are different, and neither equals `n` or `1/n`
   for those two lengths.
3. Kinetic isotropy names `c_t = c_s`, not a function of `|H|`. Record
   names no Wick parameter. The clock map `a_w` remains extra.

This note does not install `a_w = 1` and does not adopt `L_phys`. It is
independent of the Euclidean-versus-lopsided cut that can select different
`|a|`, and independent of the type split `a_sr ≠ a_w`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Fraction algebra on declared lock words and the OS0 quadratic; live Record quoted; a_w=1 and L_phys not adopted."
trace_class: negative_route_pruning
target_claim_id: wick_clock_map_a
target_blocker_text: "live Record plus a history of n locks does not name Wick a"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact for the displayed words and omega_coeff identities; a declared clock map remains extra"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

This is current Record, not a retype. No axiom or primitive is edited.

## Exact Objects

A **history** `H` is a finite word of locks. Write `|H| = n` for its
length. The lengths used here are

```text
n ∈ {0, 1, 2, 3, 4}.
```

The empty word has `n = 0`. The two displayed nonempty words are

```text
H2 = AB,     |H2| = 2,
H4 = ABCD,   |H4| = 4.
```

Each letter is one admissible local possibility locked by a forming
record. Both words are lawful lock histories. Length is a cardinality of
already-formed locks. It is not a site readout of a blank.

The **linear Wick map** is a nonzero rational `a_w ∈ Q \ {0}` together
with

```text
k4 = i a_w omega.
```

The **Euclidean OS0 form** is the `a_w`-free quadratic

```text
Q_E(k4, k) = (k4^2 + k^2)/4.
```

Because `i^2 = -1`, the continuation is

```text
Q_E(i a_w omega, k) = (-a_w^2 omega^2 + k^2)/4,
```

and the **Lorentzian `omega^2` coefficient** is the exact rational

```text
omega_coeff(a_w) = -a_w^2 / 4.
```

The map `n ↦ a_w` is not named by Record and is not named by
`c_t = c_s`.

## Live Record

The current Record axiom is the `Record / Fixed Reality` section of
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). Quoted
verbatim:

Records form.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.

The same memo states that finite additivity, a named scalar collection
functional `I`, and an assigned value `I(empty)=0` are not Record axiom
content. Named `I` is not axiom content. A site with no record cannot be
read; the axiom does not assign a scalar to absence.

The live Record section, from `### Record / Fixed Reality` through
`## Qualification`, does not contain `I(empty)=0`.

## Kinetic Isotropy

[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies the Euclidean kinetic-form equality

```text
c_t = c_s,
```

the Osterwalder-Schrader OS0 kinetic normalization. It states that the
framework's time remains emergent and derived, and that the primitive
does not add or amend an axiom. It does not write `k4 = i a_w omega`,
does not name `omega_coeff`, and does not name a function of `|H|`.

## Theorem 1 — Two Lawful Histories; Blank Unread

`H2 = AB` and `H4 = ABCD` are finite words of locks. Both are lawful:
each letter is one locked admissible possibility, and Record licenses
reading formed lock content.

Their lengths are different:

```text
|H2| = 2,    |H4| = 4.
```

Quote blank-unread: a site with no record cannot be read. Do not assign
a readout to empty sites to manufacture a clock. The empty history has
no lock content, so it has no readout. Padding either word with unread
sites, or assigning a scalar to absence, is not a Record clock. In particular one must not write `I(empty)=0` and then convert
that assigned absence into a tick count or a Wick parameter.

Length `|H|` is therefore only the number of letters already present.
It is not a manufactured window clock that reads blanks.

## Theorem 2 — Distinct `omega_coeff`; Neither Is `n` Or `1/n`

The polynomial `Q_E = (k4^2 + k^2)/4` is written in the Euclidean
momenta alone. Substituting `k4 = i a_w omega` gives

```text
(i a_w omega)^2 / 4 + k^2/4 = (i^2 a_w^2 omega^2)/4 + k^2/4
                            = (-a_w^2 omega^2)/4 + k^2/4.
```

So `omega_coeff(a_w) = -a_w^2/4`. Exact rationals:

```text
omega_coeff(1) = -1/4,
omega_coeff(2) = -1.
```

These two values are different: `-1/4 ≠ -1`. For the displayed lengths,

```text
n ∈ {2, 4},    1/n ∈ {1/2, 1/4}.
```

Neither coefficient equals either length or either reciprocal:

```text
-1/4 ∉ {2, 4, 1/2, 1/4},
-1   ∉ {2, 4, 1/2, 1/4}.
```

The same `omega_coeff` pair is obtained for every history: the
continuation does not see `|H|`. The same pair of lengths is obtained
for every `a_w`: the word length does not see the Wick parameter.

The sample `a_w = 1` is one nonzero rational among others. It is
displayed so that `-1/4` can be compared with `-1`. It is not installed
as a law.

## Theorem 3 — OS0 Is `c_t = c_s`; `a_w` Remains Extra

OS0 names `c_t = c_s`, the equality of the Euclidean `k4^2` and spatial
`k^2` coefficients, both `1/4` in `Q_E`. That equality is not a function
of `|H|`. Changing a lock-word length leaves `Q_E` unchanged.

Record names formation, one-site locking, permanence, content-only
readout, and unreadability of a blank site. It names no Wick parameter
and no map `n ↦ a_w`.

Therefore a live lock history plus OS0 leaves the clock map `a_w` extra.
This note does not install `a_w = 1` and does not adopt `L_phys` as a
stand-in for `a_w` or as a clock built from unread sites.

## Mutation Predicates

The following hostile predicates fail on the objects above.

1. “`omega_coeff(a_w)` equals `|H|` for all `a_w`, `H`.” Counterexample:
   `omega_coeff(1) = -1/4` and `|H2| = 2` are unequal, and
   `omega_coeff(2) = -1` is unequal to both `2` and `4`.
2. “The live memo contains `I(empty)=0`.” False of the live Record
   section (`### Record / Fixed Reality` through `## Qualification`).
   Named `I` and `I(empty)=0` are not Record axiom content.

## Independence

This note does not rerun two neighboring cuts.

- Euclidean `Q_E` versus a lopsided kinetic form can select different
  `|a|`. That is a different residual. The algebra here keeps `Q_E`
  fixed and varies only the lock-word length against `a_w`.
- Scale-reference `a_sr` is not the Wick parameter `a_w`. That is a
  different type split. The algebra here never uses `a_sr`.

## Claim Boundary

| Item | Status |
|---|---|
| live Record readout sentences | quoted; not edited |
| named `I` and `I(empty)=0` | not axiom content |
| `|H2|=2`, `|H4|=4` | exact word lengths |
| blank unread | quoted; no clock from empty sites |
| `omega_coeff(1)=-1/4`, `omega_coeff(2)=-1` | derived from `Q_E` |
| `n ↦ a_w` | not named |
| `a_w = 1` | displayed sample; not installed |
| `L_phys` | not adopted |
| `Q_E` versus lopsided `|a|` | independent; not claimed |
| `a_sr ≠ a_w` | independent; not claimed |
| axiom or primitive edit | none |

## What This Does Not Claim

- No axiom or primitive is edited.
- `a_w = 1` is not installed.
- `L_phys` is not adopted as a clock or as `a_w`.
- Lorentzian closure, boost generators, and OS reconstruction are not
  claimed.
- Nonlinear clock maps are out of scope.
- A later declared continuation rule remains a live formal escape. It is
  not derived here.

## Imports And Open

**Imported.** The current four-axiom memo, used for the live Record
sentences and the statement that named `I` and `I(empty)=0` are not
Record content. The kinetic-isotropy primitive, used for `c_t = c_s`
and the Euclidean OS0 form.

**Derived here.** Lawful lengths `2` and `4`; blank unread as a bar on
manufacturing a clock from empty sites; `omega_coeff(a_w) = -a_w^2/4`
with the displayed pair `-1/4 ≠ -1`; failure of both mutation
predicates.

**Open.** Any separately declared linear or nonlinear clock map; any
identification of `|H|` with a physical length `L_phys`; Lorentzian
closure.

## Primary Runner

[`scripts/lock_history_length_is_not_wick_clock_a_2026_08_13.py`](../scripts/lock_history_length_is_not_wick_clock_a_2026_08_13.py)
recomputes `|H|` and `omega_coeff(a_w)` in exact `Fraction` arithmetic,
re-reads the two source notes, and checks the two mutation predicates.
No runner cache is written.
