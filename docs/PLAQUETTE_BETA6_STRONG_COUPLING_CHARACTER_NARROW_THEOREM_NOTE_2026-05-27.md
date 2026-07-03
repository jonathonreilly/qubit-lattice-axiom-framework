# SU(3) Wilson Plaquette Strong-Coupling Padé[3/3] Narrow Theorem (Bounded)

**Date:** 2026-05-27
**Date of scope repair:** 2026-05-30
**Claim type:** bounded_theorem
**Claim scope:** the standalone conditional Padé-algebra facts that follow
after the coefficient packet and evaluation point are supplied:

1. given the published cluster-expansion coefficient table
   (Münster 1981; Drouffe-Zuber 1983, cited as external coefficient
   providers, not load-bearing axioms) gives the truncated series
   `<P>(u) = u + 4 u^4 + 24 u^6 - 24 u^7 + 100 u^8 + O(u^9)`;
2. given the evaluation point `u = 1/3`, the [3/3] Padé approximant of
   that series equals exactly the rational number `3/5`;
3. the same `3/5` value is reproduced in both the plain `u`-expansion
   and under the conformal change of variable
   `u -> z = u/(1 + alpha u)` for `alpha in {2, 4}`;
4. the Padé[3/3] value depends only on the coefficient set
   `{c_1, c_4, c_6}` and is rigid in `c_6 = 24`; perturbing `c_6` to
   `12` or `0` changes the Padé[3/3] value to the distinct rationals
   `3/7` or `9/23` respectively;
5. the ordinary Padé[3/3] Borel-Laplace route is obstructed at
   `u = 1/3`: the Padé[3/3] denominator of the Borel transform has a
   positive real pole on the Laplace contour, so this route does not
   supply the direct Padé[3/3] value `0.6`.

The MC value `<P>(beta=6) = 0.5934` enters this note **only as a
comparison number**: the residual gap between the rigid algebraic
value `3/5 = 0.6` and that comparison number is `+0.0066` (about
`+1.1%`). The note does **not** claim a derivation of `<P>(beta=6)`,
does not promote the MC value to retained-grade status, and does not
close the plaquette-self-consistency lane.

**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome; effective status is
pipeline-derived after independent review.
**Type:** bounded_theorem
**Primary runner:** [`scripts/frontier_plaquette_beta6_strong_coupling_character_narrow.py`](./../scripts/frontier_plaquette_beta6_strong_coupling_character_narrow.py)
**Cached log:** [`logs/runner-cache/frontier_plaquette_beta6_strong_coupling_character_narrow.txt`](./../logs/runner-cache/frontier_plaquette_beta6_strong_coupling_character_narrow.txt) (PASS=26 FAIL=0)

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The Padé algebra closes exactly inside the supplied coefficient packet and runner. The retained audit chain does not close because the Münster-Drouffe-Zuber coefficient table, the leading-order character coefficient setup, and the MC compar"*

with repair: *"missing_bridge_theorem: Add retained/effective bounded input rows for the SU(3) strong-coupling coefficient table and leading character-coefficient setup, or narrow this row to a pure algebra lemma explicitly conditional on those supplied c"*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **pure algebra split path**:

- **Load-bearing (in scope):** The exact Padé[3/3] algebra: given the supplied Münster-Drouffe-Zuber coefficient table `{c_1=1, c_4=4, c_6=24, c_7=-24, c_8=100}` as an external input, the runner verifies in exact sympy rational arithmetic that `Pade[3/3](1/3) = 3/5`, the conformal cross-check at `alpha in {2,4}` also yields `3/5`, the rigidity audit holds, and the Borel-Laplace route is obstructed.
- **NON-load-bearing (split off / admitted):** The Münster-Drouffe-Zuber SU(3) strong-coupling coefficient table itself, the leading-order character-coefficient setup `u(beta) = beta/(2 N^2)`, the choice to evaluate the algebraic series at `u = 1/3`, and the MC comparison value `0.5934` are all external inputs, not results retained in the framework; without a retained bridge deriving these from the axioms, the note is explicitly conditional on those cited external provisions.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## 2026-06-07 Source-Boundary Manifest

This repair leaves the row in the honest bounded-support lane and makes the
source boundary executable rather than implicit. The direct theorem is a finite
rational-algebra statement over the explicit input packet

```text
I_SC = (
  c_1 = 1,
  c_4 = 4,
  c_6 = 24,
  c_7 = -24,
  c_8 = 100,
  u_eval = 1/3,
  P_MC = 0.5934
).
```

The runner now checks this packet as a supplied tuple before doing any Padé
work. It then verifies the actual Padé[3/3] matching equations
`series * Q - P = O(u^7)`, the nonzero denominator at `u = 1/3`, the exact
value `3/5`, the two conformal cross-checks, the `c_6` rigidity audit, and the
positive-contour Borel-Padé obstruction. The MC number is checked only as a
comparison value and is explicitly not consumed as a theorem equality.

Accordingly, this note can support a re-audit of the fully internal statement:

> Given `I_SC`, the displayed Padé and Borel-Padé finite algebra follows.

It cannot support a re-audit that treats the coefficient table, the beta-to-`u`
map, or the MC comparator as framework-native facts. Those remain outside the
row until separately derived or accepted by their own retained/effective-bounded
authority rows.

## Statement

Let `<P>(u)` denote the strong-coupling character expansion of the
single-plaquette expectation for SU(3) Wilson gauge action on a
4-dimensional hypercubic lattice, written as a formal power series in
the single-link fundamental character coefficient `u`. With the
published Münster-Drouffe-Zuber coefficient table

```text
c_1 = 1,   c_4 = 4,   c_6 = 24,   c_7 = -24,   c_8 = 100,                 (1)
```

the truncated series is

```text
<P>(u) = u + 4 u^4 + 24 u^6 - 24 u^7 + 100 u^8 + O(u^9).                 (2)
```

**Supplied context (C1) (not retained by this row).** The coefficient of `u`
in the supplied expansion is `1`. The standard leading-order single-link
variable convention satisfies `u(beta) = beta / (2 N^2)` with `N = 3`, so

```text
u(beta) = beta / 18,    u(beta = 6) = 1/3.                                (3)
```

This row does not derive the character-coefficient setup or the beta-to-`u`
identification. It uses `u = 1/3` only as the supplied evaluation point for the
Padé algebra below.

**Conclusion (T2) (Padé[3/3] is a definite rational at `u = 1/3`).**
The Padé[3/3] approximant of `(2)` exists and equals

```text
Pade[3/3](u) = (u - 6 u^3) / (1 - 6 u^2 - 4 u^3),                         (4)
```

with numerator and denominator both being explicit integer-coefficient
polynomials. Evaluating at `u = 1/3` gives

```text
Pade[3/3](1/3) = ( 1/3 - 6 * 1/27 ) / ( 1 - 6/9 - 4/27 )
              = ( 1/3 - 2/9 ) / ( 1 - 2/3 - 4/27 )
              = ( 1/9 ) / ( 5/27 )
              = 3/5.                                                      (5)
```

**Conclusion (T3) (conformal-mapping cross-check).** Under the
two-parameter conformal change of variable
`u = z / (1 - alpha z)`, for either `alpha = 2` or `alpha = 4`,
the Padé[3/3] approximant of the re-expansion of `(2)` in `z`,
evaluated at the corresponding `z(u = 1/3) = 1/(3 + alpha)`, equals
exactly `3/5` in both cases.

**Conclusion (T4) (sensitivity / rigidity audit).** The Padé[3/3]
approximant of `(2)` uses only the coefficients `c_1`, `c_4`, `c_6`
(and the implicit zeros `c_2 = c_3 = c_5 = 0`). In particular, the
value `3/5` is invariant under arbitrary perturbations of `c_7` and
`c_8`. Conversely it is rigid in `c_6 = 24`: replacing `c_6` by `12`
yields `Pade[3/3](1/3) = 3/7`, and replacing `c_6` by `0` yields
`Pade[3/3](1/3) = 9/23`.

**Conclusion (T5) (Borel-Padé mismatch witness).** Define the Borel
transform of `(2)` by `b_n := c_n / n!`. The Padé[3/3] of the Borel
transform exists. Its formal Borel-Laplace value at `u = 1/3`,

```text
int_0^infinity exp(-t) * BorelPade[3/3](t/3) dt,                          (6)
```

is obstructed because the Padé[3/3] Borel denominator has a positive
real root in the Borel plane, corresponding to a positive pole on the
Laplace contour at `u = 1/3`. The ordinary Padé[3/3] Borel-Laplace
route therefore does **not** supply the same analytic-continuation
method as the direct Padé[3/3] on the SC series. This row does not prove
or disprove Borel summability in all possible resummation schemes.

**Conclusion (T6) (Padé[4/4] is unstable).** The Padé[4/4] approximant
of `(2)` evaluated at `u = 1/3` equals `157/395 ≈ 0.3975`. The gap to
the MC reference value `0.5934` widens substantially from the
Padé[3/3] case. The alternating sign at `c_7` destabilizes the
diagonal Padé sequence beyond `[3/3]`.

**MC-comparison statement (NOT a closure).** Taking the MC value
`0.5934` as a comparison number only, the residual gap

```text
0.5934 - 3/5  =  -0.0066,    relative gap = -1.11%,                       (7)
```

is small in absolute terms but is **not** zero. The note does not
claim that the Padé[3/3] value `3/5` is the true continuum-or-finite
expectation `<P>(beta = 6)`. The 1.1% gap is the honest residual of
this analytic-continuation route.

## Proof

`(C1)` Standard strong-coupling context, not a retained conclusion of this
row. For SU(N) Wilson gauge action
`S_W = (beta / N) sum_P (N - Re Tr U_P)`, the single-link integral
over Haar measure, with the fundamental character expansion
`exp((beta/N) Re Tr U) = sum_R d_R c_R(beta/N) chi_R(U)/d_R`, gives at
leading order
`<chi_F>_{1-link} / d_F = (beta / (2 N^2)) + O(beta^4)` for the
fundamental rep. Specializing to `N = 3` gives `u(beta) = beta/18`.
Evaluating at `beta = 6` gives `u = 1/3`. This paragraph is an external
setup citation for the evaluation point, not a proof that the framework's
beta=6 plaquette row has retained authority for that setup.

`(T2)` The Padé[3/3] approximant is the unique pair of polynomials
`P(u)` of degree at most 3 and `Q(u)` of degree at most 3 with
`Q(0) = 1` such that
`<P>_{truncated}(u) Q(u) - P(u) = O(u^7)`. Using only the SC
coefficients `c_0 = 0`, `c_1 = 1`, `c_2 = c_3 = c_5 = 0`, `c_4 = 4`,
`c_6 = 24`, the linear system solves to the rational coefficient
`P(u) = u - 6 u^3`, `Q(u) = 1 - 6 u^2 - 4 u^3`. The arithmetic
verification of `Pade[3/3](1/3) = 3/5` is shown in line `(5)`.

`(T3)` The conformal substitution `u = z/(1 - alpha z)` re-expanded
through order `z^8` gives a definite integer-coefficient series in
`z`. Building the Padé[3/3] of that series and evaluating at
`z = 1/(3 + alpha)` is done in closed form by the runner for both
`alpha = 2` and `alpha = 4`. The exact rational coincidence
`Pade[3/3]_z(1/(3+alpha)) = 3/5` is a consequence of the conformal
re-summation preserving the Padé[3/3] of the underlying analytic
function within the radius of convergence.

`(T4)` Pad[3/3] uses series data only through order `u^(3+3) = u^6`.
Therefore the Padé[3/3] value cannot depend on `c_7`, `c_8`, or any
higher coefficient. The runner verifies this directly over 16
perturbations of `(c_7, c_8)`. The rigidity in `c_6` is read off by
re-solving the Padé linear system at `c_6 = 12` and `c_6 = 0`; the
resulting values `3/7` and `9/23` are distinct rationals, so `3/5` is
a genuinely `c_6 = 24`-dependent algebraic value, not a coincidence
floating across the coefficient table.

`(T5)` The Borel transform `B(t) = sum b_n t^n` has coefficients
`b_n = c_n / n!`; for the published table these are
`b_1 = 1, b_4 = 1/6, b_6 = 1/30, b_7 = -1/210, b_8 = 5/2016`. The
Padé[3/3] of `B(t)` is a well-defined rational function, but its
denominator has a positive real root. At `u = 1/3`, this gives a
positive pole on the ordinary Borel-Laplace contour
`int_0^infinity exp(-t) BorelPade[3/3](t/3) dt`. Thus the ordinary
Padé[3/3] Borel-Laplace route is obstructed and does not supply the
direct-Padé continuation `3/5`. This is only a Padé[3/3] Borel-route
obstruction witness; no claim is made that other Borel-resummation
strategies (e.g. conformal-Borel, optimal Borel mapping) fail. ∎

## What this claims

- `(C1)`: the supplied leading-order coefficient setup and
  `u(beta) = beta/(2 N^2)` substitution at `N = 3` are named context,
  not retained conclusions of this row.
- `(T2)`: given the supplied coefficient table and supplied `u = 1/3`,
  the exact closed-form Padé[3/3] approximant
  `(u - 6 u^3) / (1 - 6 u^2 - 4 u^3)` and the exact rational value
  `3/5` at `u = 1/3`.
- `(T3)`: conformal-mapping invariance of the Padé[3/3] value at the
  two tested `alpha`.
- `(T4)`: the sensitivity audit identifying `c_6 = 24` as the
  determining coefficient.
- `(T5)`: the Borel-Padé[3/3] obstruction witness via the positive
  contour pole of the Padé[3/3] Borel transform at `u = 1/3`.
- `(T6)`: the Padé[4/4] is unstable for this series.

The MC residual `0.5934 - 3/5 = -0.0066` is **stated as a comparison
number**, not as a closure of `<P>(beta = 6)`.

## What this does NOT claim

- Does **not** derive the Münster-Drouffe-Zuber coefficient table
  `{c_1 = 1, c_4 = 4, c_6 = 24, c_7 = -24, c_8 = 100}` from the
  framework axioms. The table is cited as an external coefficient
  provider only; the theorem-grade content is the algebraic
  consequence under Padé[3/3] and the conformal cross-check, not the
  derivation of the coefficients themselves.
- Does **not** claim that `<P>(beta = 6) = 3/5` is the true
  finite-volume or infinite-volume Wilson plaquette expectation. The
  residual gap to the MC reference value is explicitly `-0.0066`
  (`-1.1%`); the note does not promote `3/5` to a retained-grade
  closure of the plaquette lane.
- Does **not** identify `u(beta) = beta/18` with the all-orders single-link
  character coefficient. It is the leading-order substitution; the
  higher-order corrections in `u(beta) - beta/18` are not consumed
  here and would shift the substitution point away from `u = 1/3`.
- Does **not** provide retained one-hop authority for using `u = 1/3` as the
  framework beta=6 evaluation point; `u = 1/3` is an explicit supplied input to
  the Padé algebra.
- Does **not** consume or close the upstream plaquette rows
  `PLAQUETTE_SELF_CONSISTENCY_NOTE.md`,
  `GAUGE_VACUUM_PLAQUETTE_BRIDGE_SUPPORT_NOTE.md`,
  `BRIDGE_GAP_HK_PLAQUETTE_CLOSED_FORM_NOTE_2026-05-06.md`,
  `GAUGE_VACUUM_PLAQUETTE_BETA6_EVALUATION_SEAM_REDUCTION_SCIENCE_ONLY_NOTE_2026-04-17.md`,
  or `GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md`.
- Does **not** retire the open `g_bare = 1` derivation gate, the
  open `alpha_bare = 1/(4 pi)` source, the bounded
  `alpha_LM`/`alpha_s(v)` tadpole improvement chain, or the
  low-energy running bridge to `M_Z`. The narrow theorem does not
  promote `ALPHA_S_DERIVED_NOTE.md`.
- Does **not** assert or deny Borel summability of the SC series. The
  `(T5)` witness records that the Padé[3/3] Borel denominator has a
  positive-contour pole at `u = 1/3`; this is a Padé[3/3]
  Borel-route obstruction witness, not a proof of Borel non-summability
  in all senses.
- Does **not** identify `Pade[3/3]` as the asymptotic limit of the SC
  expansion. The Padé[4/4] is unstable in this series, so the diagonal
  Padé sequence does not visibly converge; the close numerical match
  between `Pade[3/3] = 3/5` and the MC comparison value is not the
  same statement as a convergent extrapolation.

## Cited dependencies (coefficient providers, not load-bearing)

- Münster (1981), *Nucl. Phys. B190 [FS3], 439*: SU(N) Wilson
  strong-coupling cluster-expansion graph counting; coefficient table
  through O(u^8) for D=4 fundamental-rep plaquette.
- Drouffe-Zuber (1983), *Phys. Rep. 102, 1*: review of lattice
  strong-coupling expansions; D=4 SU(3) plaquette coefficients in
  Table 13.
- Itzykson-Drouffe Vol. 2 ch. 6: textbook account of single-link
  character integrals on SU(N) Haar measure.
- Creutz, *Quarks, Gluons, Lattices* ch. 14: single-link expansion
  conventions.

These are external coefficient providers, NOT load-bearing on the
theorem statement. The theorem-grade content is the algebraic
consequence under Padé[3/3] and the conformal cross-check.

No internal framework notes are consumed as load-bearing dependencies.
The plain-text pointers to upstream plaquette notes in *What this does
NOT claim* are reader-orientation pointers only, not load-bearing
deps.

## Forbidden imports check

- No external numerical targets consumed as load-bearing. The MC value
  `0.5934` enters only as a comparison number for the residual-gap
  measurement, not as a fitted input or load-bearing target.
- No fitted selectors consumed.
- No same-surface family arguments load-bearing on retention.
- No unit-convention imports load-bearing on the algebraic value.
- No specific framework numerical inputs (`<P>`, `1/(4 pi)`,
  `alpha_s(M_Z)` etc.) load-bearing on the Padé[3/3] value.

## Validation

Primary runner:
[`scripts/frontier_plaquette_beta6_strong_coupling_character_narrow.py`](./../scripts/frontier_plaquette_beta6_strong_coupling_character_narrow.py)

Verifies all six conclusions exactly via sympy rational arithmetic
(Padé linear-system solve in `Rational`), with the Borel-Laplace
integral evaluated by `scipy.integrate.quad`. Expected result:

```text
TOTAL: PASS=20 FAIL=0
```

The runner additionally records the full comparison table:

```text
Truncated SC series O(u^8) at u=1/3   : 0.419906   gap = +0.1735 (+29.24%)
Pade[3/3] in u                        : 0.600000   gap = -0.0066 ( -1.11%)
Pade[3/3] in conformal z (alpha=4)    : 0.600000   gap = -0.0066
Pade[3/3] in conformal z (alpha=2)    : 0.600000   gap = -0.0066
Pade[4/4] in u                        : 0.397468   gap = +0.1959
Borel-Pade[3/3]+Borel-Laplace         : obstructed by positive-contour pole
MC reference value                    : 0.593400
```

The truncated-series, Padé[3/3], conformal-z Padé[3/3], Padé[4/4]
and Borel-Padé[3/3] values are all rational and computed in exact
sympy `Rational` arithmetic; the Borel-Laplace integral is the only
numerical step (with adaptive `scipy.integrate.quad`).
