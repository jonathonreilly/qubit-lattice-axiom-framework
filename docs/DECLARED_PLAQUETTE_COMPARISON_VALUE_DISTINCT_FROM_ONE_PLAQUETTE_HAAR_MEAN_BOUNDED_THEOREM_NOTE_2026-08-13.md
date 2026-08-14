---
claim_id: plaquette_b1_convention_independent_of_one_plaquette_mean_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the declared Wilson matching beta = 2 N_c / g_bare^2 with N_c = 3, the point g_bare = 1 selects beta = 6 exactly. The exact one-plaquette Haar mean p_1(6) = J'(6)/J(6) is remainder-controlled from the June 10 single-link recurrence and satisfies p_1(6) < 1/2 < 5934/10000. The rational 5934/10000 is compared only after the bound on p_1 is closed. The matching convention therefore does not select admission B1. The note does not derive 0.5934 and does not retire B1."
upstream_dependencies:
  - minimal_axioms
  - plaquette_value_derivation_program_specification_and_bracket_reduction_narrow_theorem_note_2026-06-10
runner: scripts/plaquette_b1_convention_independent_of_one_plaquette_mean_2026_08_13.py
---

# Plaquette B1 Convention Independent of the One-Plaquette Haar Mean

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact Wilson matching arithmetic at `g_bare = 1`, and a
remainder-controlled bound on the single-plaquette Haar mean at `beta = 6`.
**Status authority:** independent audit lane only. This source note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/plaquette_b1_convention_independent_of_one_plaquette_mean_2026_08_13.py`](../scripts/plaquette_b1_convention_independent_of_one_plaquette_mean_2026_08_13.py)

## Result Up Front

Admission B1 of
[`ALPHA_S_DERIVED_NOTE.md`](ALPHA_S_DERIVED_NOTE.md) is the numeral
`<P>* = 0.5934`, licensed only as an admitted comparison/reuse number by
[`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md).
The June 10 program note
[`PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`](PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md)
specified the retirement interface for that admission and did not derive the
numeral.

This stretch answers a narrower question. The Wilson matching convention
`beta = 2 N_c / g_bare^2` at `N_c = 3` and `g_bare = 1` selects
`beta = 6` exactly. That coupling does **not** select the admitted B1
numeral, because the exact one-plaquette Haar mean at `beta = 6` lies
strictly below `1/2`, and `1/2` lies strictly below `5934/10000`.

This note does not derive 0.5934. It does not retire B1. The named remaining
path is the June 10 three-point `ln Z_L` / mass-gap interface.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact matching arithmetic and a remainder-controlled one-plaquette bound are proved; 4D thermodynamic-limit <P>* and B1 retirement remain open."
trace_class: convention_independence
artifact_role: theorem
hypothetical_axiom_status: no edit
admitted_observation_status: "0.5934 is compared only as an admitted numeral after p_1 is bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises (one hop)

- **M1 (declared matching).** Gauge group `SU(3)`, so `N_c = 3`. The Wilson
  matching used on this surface is
  `beta = 2 N_c / g_bare^2`. At `g_bare = 1` this is an exact rational
  identity, not a fit. The matching is a declared convention, not an axiom
  consequence.
- **M2 (single-link engine; June 10).** The single-link generating function
  is the normalized Haar integral
  `J(b) = int_{SU(3)} exp((b/3) Re Tr U) dHaar U = sum_{n >= 0} a_n b^n`,
  with the order-3 recurrence
  `6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}`
  and seeds `a_0 = 1`, `a_1 = 0`, `a_2 = 1/36`. Authority for the engine and
  for the range `Re Tr U in [-3/2, 3]` is the June 10 note; the coefficients
  used below are recomputed from the recurrence, not imported as decimals.
- **M3 (B1 license, not a derivation).** The numeral `0.5934` enters only as
  the admitted B1 comparison numeral
  `5934/10000`.
  [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  licenses that numeral as comparison/reuse and does not derive it.
- **M4 (axiom memo; no edit).**
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is an
  upstream dependency. No axiom sentence is used as a hypothesis that
  selects `0.5934`, and this note performs no axiom edit.

No Monte Carlo sample, no 4D transfer matrix, and no fitted selector enters.

## Exact objects

The one-plaquette Haar mean at coupling `b` is

```text
p_1(b) := (d/db) ln J(b) = J'(b) / J(b).
```

This is the mean of `(1/3) Re Tr U` for a single Haar-weighted Wilson
plaquette. It is not the 4D thermodynamic-limit object `<P>* := 1 + f'(6)`
named by the June 10 specification.

Write `a_n` for the recurrence coefficients. Then

```text
J(b)  = sum_{n >= 0} a_n b^n ,
J'(b) = sum_{n >= 1} n a_n b^{n-1}.
```

## Coefficient lemmas

**Lemma C1 (recurrence seeds).** `a_0 = 1`, `a_1 = 0`, `a_2 = 1/36` by M2.

**Lemma C2 (recomputed `a_3`).** The recurrence at `N = 2` reads

```text
6 * 3 * 6 * 7 * a_3 = 2*3*a_2 + 2*(7)*a_1 + a_0
                    = 6*(1/36) + 0 + 1
                    = 7/6.
```

The left coefficient is `756`, so `a_3 = (7/6)/756 = 7/4536 = 1/648`.

**Lemma C3 (recomputed `a_4`).** The recurrence at `N = 3` reads

```text
6 * 4 * 7 * 8 * a_4 = 3*4*a_3 + 2*(9)*a_2 + a_1
                    = 12/648 + 18/36
                    = 1/54 + 1/2
                    = 14/27.
```

The left coefficient is `1344`, so `a_4 = (14/27)/1344 = 1/(27*96) = 1/2592`.

**Lemma C4 (nonnegativity).** The seeds are nonnegative. For every `N >= 2`
the recurrence denominator `6(N+1)(N+4)(N+5)` is positive and the right-hand
side is a nonnegative combination of `a_N`, `a_{N-1}`, and `a_{N-2}`. By
induction, `a_n >= 0` for every `n`.

**Lemma C5 (Haar majorant).** June 10 records `Re Tr U in [-3/2, 3]`, so
`|(1/3) Re Tr U| <= 1`. Expanding the exponential in the Haar integral gives
`a_n = (1/n!) E[((1/3) Re Tr U)^n]`, hence `0 <= a_n <= 1/n!`.

## Remainder calculus

Fix an integer truncation `N >= 12` and set `b = 6`. Lemmas C4 and C5 give

```text
0 <= J(6)  - sum_{n=0}^{N} a_n 6^n
   <= sum_{n=N+1}^{infty} 6^n / n! ,

0 <= J'(6) - sum_{n=1}^{N} n a_n 6^{n-1}
   <= sum_{n=N+1}^{infty} 6^{n-1} / (n-1)!
    = sum_{k=N}^{infty} 6^k / k! .
```

The exponential tail `sum_{k=M}^{infty} 6^k / k!` with `M > 6` is at most
the first term times the geometric majorant `M / (M-6)`:

```text
sum_{k=M}^{infty} 6^k / k!  <=  (6^M / M!) * M / (M-6).
```

Therefore the explicit remainder bounds

```text
R_N   := (6^{N+1} / (N+1)!) * (N+2) / (N-4) ,
R'_N  := (6^{N} / N!) * N / (N-6)
```

satisfy `0 <= J(6) - J_N <= R_N` and `0 <= J'(6) - J'_N <= R'_N`, where
`J_N` and `J'_N` are the displayed partial sums. Both `J_N` and `J'_N` are
exact nonnegative rationals. Since `J(6) > 0` and `J'(6) > 0`,

```text
J'_N / (J_N + R_N)  <=  p_1(6)  <=  (J'_N + R'_N) / J_N .
```

In particular, the exact rational comparison

```text
2 (J'_N + R'_N) < J_N
```

implies the coupling-independent ceiling `p_1(6) < 1/2`.

## Theorem 1 — matching selects `beta = 6`

On the declared matching `beta = 2 N_c / g_bare^2` with `N_c = 3` and
`g_bare = 1`,

```text
beta = 2 * 3 / 1^2 = 6
```

exactly. This is rational arithmetic on a declared convention. It is not an
axiom necessity claim, and it does not mention the B1 numeral.

## Theorem 2 — one-plaquette mean at `beta = 6` is not the B1 numeral

Take the truncation `N = 16`. The recurrence produces the exact partial sums

```text
J_16  = 251763633587 / 73156608000 ,
J'_16 = 443237359 / 304819200 ,
```

and the explicit remainder majorant

```text
R'_16 = 6^{16} / 16! * 16 / 10 = 944784 / 4379375 .
```

Adding gives the exact rational upper envelope

```text
J'_16 + R'_16 = 259952292959 / 155675520000 .
```

The separation identity is then the exact positive rational

```text
J_16 - 2 (J'_16 + R'_16) = 5323057146257 / 52306974720000 > 0 ,
```

so `p_1(6) < 1/2`. The paired runner recomputes every displayed rational
from the recurrence and the remainder formula; none of those rationals is
constructed from `0.5934`.

Only after that ceiling is closed, compare the admitted B1 numeral as the
rational `5934/10000`:

```text
1/2 = 5000/10000 < 5934/10000 .
```

Hence `p_1(6) < 1/2 < 5934/10000`, and the one-plaquette Haar mean at the
matching point `beta = 6` is not the admitted B1 numeral.

A second, independent truncation `N = 20` is checked in-runner by the same
remainder calculus and yields the same strict ceiling `p_1(6) < 1/2`. The
`N = 16` identity above is already sufficient.

If the one-plaquette mean is replaced by `5934/10000`, the ceiling
`p_1 < 1/2` fails, because `5934/10000 > 1/2`. If the matching is replaced
by a different rational function of `(N_c, g_bare)`, the identity
`g_bare = 1 => beta = 6` fails at some positive test point (the runner uses
`(N_c, g_bare) in {(3,1), (3,2), (2,1)}`). Those two substitutions are the
discriminating gates for Theorems 1 and 2.

## Theorem 3 — B1 is not retired

The object named by admission B1 is the 4D thermodynamic-limit plaquette
mean `<P>*`, not the one-plaquette integral `p_1(6)`. Theorem 2 separates
those two numbers. It does not enclose `<P>*`, does not produce a certified
three-point `ln Z_L` bracket, and does not supply a mass-gap rate.

Therefore this note does not retire B1. The June 10 three-point `ln Z_L` /
mass-gap interface remains the named path.

## Boundaries and explicit non-claims

- This note does not derive 0.5934 and does not treat `0.5934` as a target
  to be reconstructed from `p_1`.
- No 4D `<P>*` evaluation, no Monte Carlo, no cluster expansion at
  `beta = 6`, and no radius claim.
- No axiom edit, no axiom necessity, and no new primitive.
- The matching `beta = 2 N_c / g_bare^2` is declared, not derived from the
  axiom memo.
- The one-plaquette mean is not a substitute for the June 10 finite-volume
  rate `|f_L - f| <= 6 beta / L`.

## Verification

Run:

```bash
python3 scripts/plaquette_b1_convention_independent_of_one_plaquette_mean_2026_08_13.py
```

The runner uses exact `Fraction` arithmetic for the recurrence, the
remainder majorants, the matching identities, and the comparison
`1/2 < 5934/10000`. It does not write a cache. Expected summary:

```text
TOTAL: PASS>=10 FAIL=0
```
