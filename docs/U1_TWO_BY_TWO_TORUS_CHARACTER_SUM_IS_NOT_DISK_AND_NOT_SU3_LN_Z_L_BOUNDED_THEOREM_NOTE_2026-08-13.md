---
claim_id: u1_two_by_two_torus_character_sum_is_not_disk_and_not_su3_ln_z_l_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the 2D U(1) Wilson 2x2 torus the unnormalized character-sum Z_T(beta)=sum_n I_n(beta)^4 is strictly larger than the tree-gauge-fixed 2D disk Z_D(beta)=I_0(beta)^4 at the three couplings beta in {1,2,3}, with an exact remainder-controlled gap. The same object is not the June 10 4D SU(3) ln Z_L enclosure target: N_p=4 is not N_p(L=2)=96 and U(1) is not SU(3). No four-dimensional plaquette value is claimed."
upstream_dependencies:
  - plaquette_value_derivation_program_specification_and_bracket_reduction_narrow_theorem_note_2026-06-10
  - minimal_axioms
runner: scripts/u1_two_by_two_torus_character_sum_is_not_disk_and_not_su3_ln_z_l_2026_08_13.py
---

# 2x2 U(1) Torus Character-Sum Z Is Not the Disk and Not 4D SU(3) ln Z_L

**Date:** 2026-08-13
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** homology constraint for the unnormalized 2D U(1) Wilson
character sum on the 2x2 torus, and a negative identification against the
June 10 four-dimensional SU(3) `ln Z_L` object.
**Status authority:** independent audit lane only. This source note writes no
audit verdict, retags no ledger row, and does not set or predict an audit
outcome.
**Primary runner:**
[`scripts/u1_two_by_two_torus_character_sum_is_not_disk_and_not_su3_ln_z_l_2026_08_13.py`](../scripts/u1_two_by_two_torus_character_sum_is_not_disk_and_not_su3_ln_z_l_2026_08_13.py)

Parents on `origin/main`:

- [`PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`](PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md)
  for the four-dimensional SU(3) Wilson `ln Z_L` target, quoted below.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  as the current axiom memo, read as a premise surface only.

## Result Up Front

Two statements, both remainder-controlled and both negative.

1. Homology is not empty on the 2x2 torus. The character-sum object
   `Z_T(beta)` is strictly larger than the tree-gauge-fixed disk
   `Z_D(beta)` at every coupling used here. At `beta = 2` the gap is at
   least `2`. At `beta = 1` the gap is at least `1/8`.
2. `Z_T` is not the June 10 `ln Z_L` object. Even a perfect numerical table
   of `Z_T` is the partition function of this 2D U(1) 2x2 torus model only.
   Plaquette count `N_p = 4` is not `N_p(L = 2) = 96` of four-dimensional
   SU(3), and the group is U(1), not SU(3).

Nothing here imports a four-dimensional plaquette comparison numeral, claims
a four-dimensional `<P>*`, rewrites axiom text, or substitutes `Z_T` for
`f_L`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Remainder-controlled Z_T > Z_D at beta in {1,2,3}; N_p=4 is not N_p(L=2)=96, so Z_T is not June 10 ln Z_L."
trace_class: upstream_support
target_claim_id: certified_three_point_ln_z_l
target_blocker_text: "produce certified ln Z_L enclosures at three couplings, or a mass-gap rate"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "2x2 U(1) torus Z_T is a homology-aware certified table for that model only. The June 10 4D SU(3) interface remains open. Do not adopt axiom text."
hypothetical_axiom_status: "no edit"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. Declared objects

Work throughout with the 2D U(1) Wilson weight `exp(beta cos theta)` on a
single plaquette angle. The integer-order modified Bessel functions of the
first kind are

```text
I_n(beta) = I_{-n}(beta),
I_n(beta) = sum_{k >= 0} (1 / (k! (k+n)!)) (beta/2)^{2k+n}   (n >= 0).
```

The character expansion is the Fourier identity

```text
exp(beta cos theta) = sum_{n in Z} I_n(beta) e^{i n theta}.
```

The 2x2 torus has 4 sites, 8 links, and `N_p = 4` plaquettes. Adjacent
plaquettes share a link. Haar integration of that shared link forces a
single common integer character index on all four plaquettes. The
unnormalized character-sum object used here is therefore

```text
Z_T(beta) := sum_{n in Z} I_n(beta)^4
           = I_0(beta)^4 + 2 sum_{n >= 1} I_n(beta)^4.
```

The tree-gauge-fixed 2D disk with the same four plaquettes has vanishing
homology, so only the `n = 0` term survives:

```text
Z_D(beta) := I_0(beta)^4.
```

Gauge-volume conventions cancel in the comparison `Z_T` versus `Z_D`.

Partial sums and the geometric remainder bound are

```text
S_{n,N}(beta) = sum_{k=0}^N (1 / (k! (k+n)!)) (beta/2)^{2k+n},
t_k           = (1 / (k! (k+n)!)) (beta/2)^{2k+n},
t_{k+1}/t_k   = (beta/2)^2 / ((k+1)(k+1+n)),
q_n(N)        := (beta/2)^2 / ((N+1)(N+1+n)).
```

If `q_n(N) < 1` then the tail is a positive geometric series and

```text
0 <= I_n(beta) - S_{n,N}(beta) <= t_{N+1} / (1 - q_n(N)).
```

Every claimed inequality in this note uses exact rational arithmetic:
factorials, powers of `beta/2` written as `Fraction`, and factorial
majorants. No floating-point comparison is load-bearing.

Three couplings: `beta in {1, 2, 3}`. Truncate the character sum at
`|n| <= N_*` with `N_* >= 2` and the Bessel series at `N >= 6`. Then every
`q_n(N)` used below is strictly less than `1`.

## 2. Theorem 1 — homology is not empty at `beta = 2`

**Theorem 1.** `I_1(2) >= S_{1,0}(2) = 1`, hence
`2 I_1(2)^4 >= 2` and `Z_T(2) >= Z_D(2) + 2 > Z_D(2)`.

**Proof.** The `k = 0` term of the `n = 1` series is

```text
S_{1,0}(2) = (2/2)^1 / (0! 1!) = 1.
```

Every remaining term is nonnegative, so `I_1(2) >= 1`. Therefore
`2 I_1(2)^4 >= 2`. But

```text
Z_T(2) - Z_D(2) = 2 sum_{n >= 1} I_n(2)^4 >= 2 I_1(2)^4 >= 2,
```

so `Z_T(2) >= Z_D(2) + 2 > Z_D(2)`. The `n != 0` sector is occupied: the
homology constraint is not empty.

## 3. Theorem 2 — explicit gap at `beta = 1`

**Theorem 2.** `Z_T(1) - Z_D(1) >= 1/8`.

**Proof.** The same first term is now

```text
S_{1,0}(1) = (1/2)^1 / (0! 1!) = 1/2.
```

Hence `I_1(1) >= 1/2` and `2 I_1(1)^4 >= 2 * (1/2)^4 = 1/8`. The remainder
of the `n >= 1` sum is nonnegative, so
`Z_T(1) - Z_D(1) >= 1/8`.

## 4. Theorem 3 — rational enclosures, and the model they enclose

**Theorem 3.** At each `beta in {1, 2, 3}` the remainder bound with
`N = 6` supplies a closed rational interval containing `I_0(beta)` and a
closed rational interval containing `I_1(beta)`. Even a perfect table of
`Z_T` is `ln Z` of this 2D U(1) 2x2 torus model only.

**Proof.** For `N = 6` and `n in {0, 1}` every `q_n(6)` at these three
couplings is strictly less than `1`:

| `beta` | `n` | `q_n(6)` |
| ---: | ---: | ---: |
| 1 | 0 | `1/196` |
| 1 | 1 | `1/224` |
| 2 | 0 | `1/49` |
| 2 | 1 | `1/56` |
| 3 | 0 | `9/196` |
| 3 | 1 | `9/224` |

The enclosure is the exact rational pair

```text
[S_{n,6}(beta), S_{n,6}(beta) + t_7 / (1 - q_n(6))].
```

The paired runner evaluates both endpoints as `Fraction` objects. The
intervals are:

| `beta` | `I_0` lower | `I_0` upper | `I_1` lower | `I_1` upper |
| ---: | ---: | ---: | ---: | ---: |
| 1 | `537664349/424673280` | `131055685069/103514112000` | `16800557929/29727129600` | `66902221753/118377676800` |
| 2 | `1181737/518400` | `56723377/24883200` | `5772103/3628800` | `22676119/14256000` |
| 3 | `127946737/26214400` | `5981524717/1225523200` | `1450892379/367001600` | `5570393547/1409024000` |

These intervals enclose modified Bessel values of the 2D U(1) weight. They
do not enclose a four-dimensional SU(3) Haar integral. A perfect evaluation
of `Z_T(beta)`, or of `ln Z_T(beta)`, would still be the partition function
(or its logarithm) of this 2D U(1) 2x2 torus model only.

## 5. Theorem 4 — `Z_T` is not the June 10 `ln Z_L` object

**Theorem 4.** `N_p = 4` is not `96 = N_p(L = 2)` of four-dimensional
SU(3). The group U(1) is not SU(3). Therefore `Z_T` is not the June 10
`ln Z_L` object.

**Proof.** The 2x2 torus used above has four plaquettes. The June 10 parent
defines the four-dimensional periodic lattice `Lambda_L = (Z/L)^4` with
`N_P = 6 L^4` plaquettes, so at `L = 2`

```text
N_P(L = 2) = 6 * 2^4 = 96.
```

Four is not ninety-six. Independently, the structure group of `Z_T` is
U(1) and the structure group of the June 10 object is SU(3). The June 10
target is quoted here as the parent states it:

> a certified enclosure of `ln Z_L` at three couplings.

That sentence names `ln Z_L` of four-dimensional SU(3) Wilson theory. It
does not name `Z_T`. The two objects are distinct as counting problems and
as group integrals.

## 6. Theorem 5 — refusals

**Theorem 5.** This note does not import the June 10 admitted comparison
numeral `0.5934`. It does not claim a four-dimensional `<P>*`. It does not
rewrite axiom text. It does not substitute `Z_T` for `f_L`.

The June 10 parent remains the authority for the four-dimensional
specification

```text
Z_L(beta),   f_L(beta) = (1/(6 L^4)) ln Z_L(beta),   <P>* := 1 + f'(6).
```

Those symbols are not evaluated here. The axiom memo is read only to record
that Lattice, Qubit, Admissibility, and Record are the standing premises;
no axiom sentence is edited.

## 7. Mutation predicates

A predicate asserting `Z_T = Z_D` fails at `beta = 2`, because Theorem 1
supplies the gap lower bound `2`. A predicate asserting that `Z_T` is the
four-dimensional SU(3) `ln Z_L` object fails, because `4 != 96`. The paired
runner implements both predicates and requires them to fail. Its identity
gates call `i_n_partial(n, beta, N)` and `plaquette_count_4d(L)`.

## 8. Non-claims

- No continuum limit, no four-dimensional Wilson expectation, and no
  thermodynamic `f(beta)` are derived.
- No character-sum table is offered as a substitute for a certified
  enclosure of four-dimensional `ln Z_L`.
- No axiom sentence is proposed, and no standing premise is rewritten.
- Unmerged work is not cited.

## 9. Machine-check surface

The paired runner recomputes every displayed rational from the series
definition, checks the geometric majorant hypothesis `q_n(N) < 1` at the
declared truncation, verifies Theorems 1--4 by exact `Fraction`
comparisons, and checks the two mutation predicates. It prints
`TOTAL: PASS=N FAIL=0` with `N >= 12` and exits nonzero on any failure.

`AUDIT_INPUT_PATHS`:

- `docs/U1_TWO_BY_TWO_TORUS_CHARACTER_SUM_IS_NOT_DISK_AND_NOT_SU3_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md`
- `docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`
- `docs/MINIMAL_AXIOMS_2026-06-29.md`
