---
claim_id: one_plaquette_free_energy_is_not_four_d_ln_z_l_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Remainder-controlled three-point values of the single-plaquette Haar integral J(b) at b in {5,6,7} are not certified enclosures of four-dimensional Wilson ln Z_L, because J is one SU(3) matrix while Z_L uses N_p=6 L^4 plaquettes and the L2 wrapping count 6 L^2(2L-1), so substituting ln J into the June 10 bracket does not inherit L1–L3."
upstream_dependencies:
  - minimal_axioms
  - plaquette_value_derivation_program_specification_and_bracket_reduction_narrow_theorem_note_2026-06-10
runner: scripts/one_plaquette_free_energy_is_not_four_d_ln_z_l_2026_08_13.py
---

# One-Plaquette Free Energy Is Not Four-Dimensional ln Z_L

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** type split between the single-plaquette Haar generating function
`J(b)` and the 4D Wilson partition function `Z_L`, with a
remainder-controlled three-point table for `J` and `p_1` at
`b in {5, 6, 7}`.
**Status authority:** independent audit lane only. This source note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/one_plaquette_free_energy_is_not_four_d_ln_z_l_2026_08_13.py`](../scripts/one_plaquette_free_energy_is_not_four_d_ln_z_l_2026_08_13.py)

## Result Up Front

The June 10 program note
[`PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`](PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md)
names the remaining import-retirement interface for admission B1 as
"a certified enclosure of `ln Z_L` at three couplings". That note does
not derive `0.5934`.

This note answers a narrower typing question. The single-plaquette Haar
integral `J(b)` admits remainder-controlled rational enclosures at the
three couplings `{5, 6, 7}` (`δ = 1` around `6`). Those enclosures are
**not** certified enclosures of `ln Z_L`. `J` is an integral over one
`SU(3)` matrix. `Z_L` is an integral over `4 L^4` link variables with
`6 L^4` plaquette factors. At `L = 2` one has `N_p = 96` and
`N_ℓ = 64`. The L2 wrapping count `6 L^2 (2L-1)` equals `72` at `L = 2`
and is undefined for a single matrix.

Substituting `ln J(β)`, or `ln J(β)/(6 L^4)`, for `f_L(β)` in the June 10
bracket does not inherit lemmas L1–L3, because those lemmas count 4D
plaquettes. A mass-gap exponential finite-volume rate remains open.

This note does not derive 0.5934. It does not claim ln J is ln Z_L. It
does not retire B1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "J versus Z_L is a type split, and J, J', p_1 are remainder-controlled at three couplings; certified ln Z_L and a mass-gap rate remain open."
trace_class: negative_route_pruning
target_claim_id: certified_three_point_ln_z_l
target_blocker_text: "produce certified ln Z_L enclosures at three couplings, or a mass-gap rate"
source_of_blocker_text: handoff
reachability_to_target: prunes
next_trace_action: "One-plaquette ln J is a proxy, not Z_L. The June 10 three-point interface and a mass-gap rate remain open. Do not import 0.5934. Do not adopt axiom text."
hypothetical_axiom_status: "no edit"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises (one hop)

- **P1 (June 10 interface).** June 10 specifies the exact 4D objects
  `Z_L(β)`, `f_L(β) = (1/(6 L^4)) ln Z_L(β)`, and
  `<P>_L(β) = 1 + f_L'(β)` on the periodic torus, proves
  `|f_L(β) - f(β)| <= 6 β / L` from lemmas L1–L3, and names
  "a certified enclosure of `ln Z_L` at three couplings" as the
  bracket interface. June 10 does not derive `0.5934`.
- **P2 (single-link engine; June 10).** Gauge group `SU(3)`, so
  `N_c = 3`. The single-link generating function is the normalized Haar
  integral
  `J(b) = int_{SU(3)} exp((b/3) Re Tr U) dHaar U = sum_{n >= 0} a_n b^n`,
  with the order-3 recurrence
  `6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}`
  and seeds `a_0 = 1`, `a_1 = 0`, `a_2 = 1/36`. Authority for the engine
  and for `Re Tr U in [-3/2, 3]` is the June 10 note. Coefficients below
  are recomputed from the recurrence, not imported as decimals.
- **P3 (axiom memo; no edit).**
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is an
  upstream dependency. No axiom sentence is used to identify `J` with
  `Z_L`, and this note performs no axiom edit.

No Monte Carlo sample, no 4D transfer matrix, and no fitted selector
enters. The numeral `0.5934` is not an input to `J` or to `p_1`.

## Exact objects

The one-plaquette Haar mean at coupling `b` is

```text
p_1(b) := (d/db) ln J(b) = J'(b) / J(b).
```

On the periodic 4D torus `Λ_L = (Z/L)^4`,

```text
N_p(L) = 6 L^4 ,     N_ℓ(L) = 4 L^4 ,
Z_L(β) = ∫ ∏_p exp(-(β/3)(3 - Re Tr U_p)) ∏_ℓ dU_ℓ ,
f_L(β) = (1/(6 L^4)) ln Z_L(β) .
```

`J` is not `Z_L`. The three couplings used here are `b ∈ {5, 6, 7}`,
i.e. `δ = 1` around `6`. The L2 wrapping count of June 10 is

```text
W(L) := 6 L^2 (2L - 1) .
```

At `L = 2` the exact integers are `N_p = 96`, `N_ℓ = 64`, `W = 72`.
For every integer `L ≥ 2`, `N_p(L) ≠ 1`.

## Coefficient lemmas

**Lemma C1 (recurrence seeds).** `a_0 = 1`, `a_1 = 0`, `a_2 = 1/36` by P2.

**Lemma C2 (recomputed `a_3`).** The recurrence at `N = 2` reads

```text
6 * 3 * 6 * 7 * a_3 = 2*3*a_2 + 2*(7)*a_1 + a_0
                    = 6*(1/36) + 0 + 1
                    = 7/6 .
```

The left coefficient is `756`, so `a_3 = (7/6)/756 = 7/4536 = 1/648`.

**Lemma C3 (recomputed `a_4`).** The recurrence at `N = 3` reads

```text
6 * 4 * 7 * 8 * a_4 = 3*4*a_3 + 2*(9)*a_2 + a_1
                    = 12/648 + 18/36
                    = 1/54 + 1/2
                    = 14/27 .
```

The left coefficient is `1344`, so
`a_4 = (14/27)/1344 = 1/(27*96) = 1/2592`.

**Lemma C4 (nonnegativity).** The seeds are nonnegative. For every
`N ≥ 2` the recurrence denominator `6(N+1)(N+4)(N+5)` is positive and
the right-hand side is a nonnegative combination of `a_N`, `a_{N-1}`,
and `a_{N-2}`. By induction, `a_n ≥ 0` for every `n`.

**Lemma C5 (Haar majorant).** June 10 records `Re Tr U in [-3/2, 3]`, so
`|(1/3) Re Tr U| ≤ 1`. Expanding the exponential in the Haar integral
gives `a_n = (1/n!) E[((1/3) Re Tr U)^n]`, hence `0 ≤ a_n ≤ 1/n!`.

## Remainder calculus

Fix an integer truncation `N` and a coupling `b ∈ {5, 6, 7}` with
`N > b`. Lemmas C4 and C5 give

```text
0 ≤ J(b)  - sum_{n=0}^{N} a_n b^n
  ≤ sum_{n=N+1}^{∞} b^n / n! ,

0 ≤ J'(b) - sum_{n=1}^{N} n a_n b^{n-1}
  ≤ sum_{k=N}^{∞} b^k / k! .
```

The exponential tail with start `M > b` is at most the first term times
the geometric majorant `M / (M - b)`:

```text
sum_{k=M}^{∞} b^k / k!  ≤  (b^M / M!) * M / (M - b) .
```

Therefore the explicit remainder bounds

```text
R_N(b)  := (b^{N+1} / (N+1)!) * (N+1) / (N+1 - b) ,
R'_N(b) := (b^{N} / N!) * N / (N - b)
```

satisfy `0 ≤ J(b) - J_N(b) ≤ R_N(b)` and
`0 ≤ J'(b) - J'_N(b) ≤ R'_N(b)`, where `J_N` and `J'_N` are the
displayed partial sums. Both partial sums are exact nonnegative
rationals. Since `J(b) > 0` and `J'(b) > 0`,

```text
J'_N / (J_N + R_N)  ≤  p_1(b)  ≤  (J'_N + R'_N) / J_N .
```

The geometric majorant is valid as soon as `N > b`. The table below uses
`N = 20`, which is larger than `7` and meets the `N ≥ 16` truncation
used for the independent `b = 6` ceiling. No claimed inequality uses a
floating-point evaluation of `J` or of `ln J`.

## Theorem 1 — type split

`J(b)` is a single Haar integral over one `SU(3)` matrix. `Z_L(β)` is an
integral over `4 L^4` link variables with `6 L^4` plaquette factors.
For `L = 2`,

```text
N_p(2) = 6 * 16 = 96 ,     N_ℓ(2) = 4 * 16 = 64 .
```

These objects are unequal as functions. The L2 wrapping count
`6 L^2 (2L - 1)` is undefined for a single matrix: there is no torus
side-length in the Haar integral, and no wrapping link to delete. At
`L = 2` that count equals `6 * 4 * 3 = 72`. For every integer `L ≥ 2`,
`N_p(L) ≠ 1`.

Therefore a certified interval for `ln J(b)` is not a certified interval
for `ln Z_L(β)`. The same holds for an interval for `J` itself, and for
an interval for `p_1 = J'/J`. Object inequality is the reason: an
enclosure of one integral is not an enclosure of a different integral.

The discriminating identity is `N_p(L = 2) = 96 ≠ 1`. Replacing `Z_L`
by `J` in a predicate that reads “this is `ln Z_L`” fails that identity.

## Theorem 2 — certified three-point table for `J` (proxy only)

Take the truncation `N = 20`. The recurrence produces exact rational
partial sums `J_20(b)` and `J'_20(b)` at `b ∈ {5, 6, 7}`, and the
remainder formulae produce exact rational majorants `R_20(b)` and
`R'_20(b)`. The paired runner exhibits those rationals. The comparisons
used here are exact inequalities of rationals:

```text
J_20(5) > 2 ,     5 (J'_20(5) + R'_20(5)) < 2 J_20(5) ,
J_20(6) > 3 ,     2 (J'_20(6) + R'_20(6)) <     J_20(6) ,
J_20(7) > 5 ,     2 (J'_20(7) + R'_20(7)) <     J_20(7) .
```

Hence

```text
2 < J(5) ,     p_1(5) < 2/5 ,
3 < J(6) ,     p_1(6) < 1/2 ,
5 < J(7) ,     p_1(7) < 1/2 .
```

An independent truncation `N = 16` at `b = 6` reproduces the exact
partial sums

```text
J_16(6)  = 251763633587 / 73156608000 ,
J'_16(6) = 443237359 / 304819200 ,
```

and the remainder identity

```text
J_16(6) - 2 (J'_16(6) + R'_16(6)) = 5323057146257 / 52306974720000 > 0 ,
```

so again `p_1(6) < 1/2`. None of those rationals is constructed from
`0.5934`.

A decimal value of `ln J` is not claimed. The elementary comparisons
`J > 1 ⇒ ln J > 0` and `1 - 1/J_N ≤ ln J ≤ J_N + R_N - 1` are available
as rational bounds, but they are not needed: even a perfect table of
`ln J(5)`, `ln J(6)`, `ln J(7)` would still fail Theorem 1.

If the one-plaquette mean at `b = 6` is replaced by `5934/10000`, the
ceiling `p_1(6) < 1/2` fails, because `5934/10000 > 1/2`. That
substitution is refused by the remainder bound. The rational
`5934/10000` is compared only after the ceiling is closed, and is never
an argument of `J` or of `p_1`.

## Theorem 3 — illegal substitution is not the June 10 bracket

The June 10 bracket uses `f_L` at three couplings and the `6 β / L`
finite-volume error. The left error term is
`(72 - 6 δ) / (L δ)`, assembled from
`|f_L(b) - f(b)| ≤ 6 b / L` at `b ∈ {6 - δ, 6}`. That rate is the sum
of the L2 torus-to-free-box leg and the L3 block-factorization leg.
Lemma L2 counts the torus plaquettes that use at least one wrapping
link: `6 L^2 (2L - 1) ≤ 12 L^3`, enumerated at `L = 2, 3, 4`. At
`L = 2` the wrapping count is `6 * 4 * 3 = 72`.

Replacing `f_L(β)` by `ln J(β)`, or by `ln J(β) / (6 L^4)`, does not
inherit L1–L3. Those lemmas count 4D plaquettes. The one-plaquette
integral has no torus, no wrapping link, and no block decomposition.
The integer `72` is never an argument of `J(b)`.

The runner checks `W(2) = 72` by the closed formula and by an explicit
`L = 2` enumeration of torus plaquettes, and checks that
`one_plaquette_J` depends only on the coupling and the truncation.
A predicate that treats a `J`-enclosure as a `Z_L`-enclosure fails
Theorem 1.

## Theorem 4 — mass-gap rate still open

June 10 records that a proven mass gap with explicit cluster constants
would replace the surface rate `6 β / L` by an exponential finite-volume
bound. This note does not produce a spectral gap `Δ` and does not
produce those constants.

The named residual remains: certified `ln Z_L` at three couplings, or a
mass-gap rate. The three-point `J` table of Theorem 2 does not fill
that residual.

## Theorem 5 — scoped negatives

This note does not retire B1. It does not derive `0.5934`. It does not
claim a 4D thermodynamic-limit plaquette mean `<P>*`. It does not
perform Monte Carlo. It does not use `0.5934` as an input to `J` or to
`p_1`. It does not claim ln J is ln Z_L.

The object named by admission B1 is the 4D limit `<P>* := 1 + f'(6)`,
not the one-plaquette mean `p_1(6)` and not `ln J(6)`. Theorem 2
encloses the one-plaquette objects. Theorem 1 separates them from
`Z_L`. The June 10 three-point `ln Z_L` / mass-gap interface remains
the named path.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named interface quoted? | June 10 names "a certified enclosure of `ln Z_L` at three couplings" and does not derive `0.5934`. Both sentences are quoted above. |
| V2 | Already on `origin/main`? | Search of `origin/main` finds no landed type-split theorem that a remainder-controlled interval for `ln J` is not an interval for `ln Z_L`. June 10 uses `(ln J)''` as a declared curvature scale for budget arithmetic, and uses `-β + ln J` as an exactly solvable proxy surface; neither identification is a 4D `Z_L` enclosure. An unmerged one-plaquette-mean comparison is not a parent. |
| V3 | Textbook Haar integral? | The single-link Haar series `J(b)` is standard. Textbook evaluations of that integral do not name the B1 three-point `ln Z_L` interface, do not count `N_p = 6 L^4`, and do not supply L2/L3. |
| V4 | Exact witness? | `N_p(L=2) = 96 ≠ 1`, `N_ℓ(L=2) = 64`, `W(2) = 72`, `a_3 = 1/648`, `a_4 = 1/2592`, and `N_p(L) ≠ 1` for every integer `L ≥ 2`. |
| V5 | Corollary of June 10? | No. June 10 specifies the interface and uses `ln J` as a proxy. An interface specification is not a proxy/target theorem. The type split and the illegal-substitution refusal are proved here. |

## No-Go Discipline (N1–N8)

The negatives that survive are Theorem 1 (type split) and Theorem 5
(scoped non-claims). At least five routes are recorded.

- **N1 alternative routes.** (i) Substitute `J` for `Z_L` in a
  three-point enclosure: pruned by Theorem 1, because `N_p(2) = 96 ≠ 1`.
  (ii) Treat the one-plaquette mean `p_1(6)` as the B1 object: a
  reconstructed residual; Theorem 2 gives `p_1(6) < 1/2`, and the B1
  object is 4D `<P>*`, not `p_1`. (iii) Monte Carlo evaluation of
  `ln Z_L` or `<P>_L`: not licensed here. (iv) A proven mass-gap
  exponential finite-volume rate: open (Theorem 4). (v) An axiom edit
  identifying `J` with `Z_L`: not performed. (vi) Import of `0.5934` as
  an input to `J` or `p_1`: forbidden; a forced `p_1(6) = 5934/10000`
  is rejected by `p_1(6) < 1/2`.
- **N2 wall independence.** The type-split wall is the mismatch of
  integral domains (`1` matrix versus `N_p(L)` plaquettes). The open
  mass-gap rate and the licensed three-point `ln Z_L` computation are
  not counted as walls, because this note leaves them open.
- **N3 hidden-wall scan.** “Certified,” “four-dimensional,” and
  “one-plaquette” are load-bearing only for the declared Wilson/Haar
  objects. None is used to close B1 or to produce `0.5934`.
- **N4 residual matching.** The named remaining path is exactly the
  June 10 residual: certified `ln Z_L` at three couplings, or a
  mass-gap rate. The one-plaquette table is a proxy, not that residual.
- **N5 rhetoric audit.** The five N5 lines below are the scoped
  meanings of the negatives.
- **N6 partial-closure paths.** The legitimate positive path remains
  the June 10 interface. No axiom sentence is requested. A mass-gap
  rate would upgrade the finite-volume error, not identify `J` with
  `Z_L`.
- **N7 steelman.** A hostile reading is that June 10 already treated
  `ln J` as a proxy, so a type-split note is only a restatement. The
  reply is V5: a proxy used for budget arithmetic is not a theorem that
  a `J`-interval is not a `Z_L`-interval, and is not a refusal of the
  illegal substitution into the bracket.
- **N8 cross-cycle echo.** Prior notes sometimes feed a one-plaquette
  number into a 4D claim. This note records the type mismatch instead
  of repeating that substitution.

**N5 lines (scoped negatives).**

N5-1. "Not a certified ln Z_L enclosure" means a remainder-controlled interval for `J` or `ln J` is not an interval for the 4D Wilson partition function. It does not mean the single-plaquette series is undefined.

N5-2. "Illegal substitution" means replacing `f_L` by `ln J`, or by `ln J/(6 L^4)`, does not inherit lemmas L1–L3. It does not mean no three-point computation of `ln Z_L` can exist.

N5-3. "Does not retire B1" means the 4D thermodynamic-limit plaquette mean is not enclosed. It does not assert that the admitted numeral is false.

N5-4. "Does not derive 0.5934" means that numeral is not reconstructed from `J` or `p_1` and is not an input to those objects.

N5-5. "Mass-gap rate still open" means this note produces neither a spectral gap `Δ` nor cluster constants. It does not assert that a gap is absent.

## Boundaries and explicit non-claims

- This note does not derive 0.5934 and does not treat `0.5934` as a
  target to be reconstructed from `J` or `p_1`.
- This note does not claim ln J is ln Z_L.
- No 4D `<P>*` evaluation, no Monte Carlo, no cluster expansion at
  `β = 6`, and no radius claim.
- No axiom edit, no axiom necessity, and no new primitive.
- The one-plaquette table is not a substitute for the June 10
  finite-volume rate `|f_L - f| ≤ 6 β / L`.

## Verification

Run:

```bash
python3 scripts/one_plaquette_free_energy_is_not_four_d_ln_z_l_2026_08_13.py
```

The runner uses exact `Fraction` arithmetic for the recurrence, the
factorial tail majorants, the three-point `J` and `p_1` enclosures, the
counting identities, and the comparison `1/2 < 5934/10000`. It does not
write a cache. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
