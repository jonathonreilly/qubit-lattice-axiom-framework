# Native Gauge Transfer Weyl-Determinant Tail Domination Rung Eleven Bounded Note

**Date:** 2026-06-12
**Claim type:** open_gate
**Type:** source-side obstruction map

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

**Claim boundary:** this note attempts the requested `H_det(A)` step after the
scalar Bessel local-CLT derivation. The finite determinant multilinear expansion
is reproducible, and the runner witnesses the determinant-mode tail size. The
honest outcome is obstruction-at-exact-step: the supplied authorities do not
derive the uniform `c_(0,0)` lower normalization or the true Wilson
determinant-mode/weight tail domination needed to write a proof-side `K_W(A)`.

**Primary runner:** [scripts/native_gauge_transfer_weyl_determinant_tail_domination_rung_eleven_bounded_2026_06_12.py](../scripts/native_gauge_transfer_weyl_determinant_tail_domination_rung_eleven_bounded_2026_06_12.py)

**Runner cache:** [logs/runner-cache/native_gauge_transfer_weyl_determinant_tail_domination_rung_eleven_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_weyl_determinant_tail_domination_rung_eleven_bounded_2026_06_12.txt)

No new axiom, literature estimate, external value, comparator number, fitted constant, rounded anchor, value-from-target step, parity proxy, or fitted prefactor is used. The runner witnesses finite rows only; it does not infer `K_W(A)` from those rows.

## One-Hop Authorities

- [NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_ASSEMBLY_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_ASSEMBLY_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md)
  for the determinant propagation target and the exact missing `H_det(A)`
  statement. Quote anchor:

```text
det B_n
 = det G_n
   + t^(-1) sum_(j=1)^3 det G_n[j:P_1]
   + E_n.
```

  Quote anchor:

```text
H_det(A):
  a uniform Weyl-determinant cancellation/normalization lemma for the
  3x3 Bessel determinant mode sum, including c_(0,0) lower normalization
  and determinant-mode tail domination, converting H_scalar into
  wilson_to_saddle_uniform(A) with an explicit K_W[A; P_1, C].
```

  Quote anchor:

```text
r_(p,q)(beta) = c_(p,q)(beta) / c_(0,0)(beta)
```

  Quote anchor:

```text
For the true Wilson diagonal, `H_scalar` on compact windows can bound a finite annulus after the determinant propagation above. It does not control the infinite determinant-mode sum or the full outside-weight region unless it is supplemented by the tail clause inside `H_det(A)` or by a separate true-tail lemma.
```

- [NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md)
  for the scalar entry input. Quote anchor:

```text
P_1(a) = (a^4 - 6 a^2 + 3) / 24.
```

  Quote anchor:

```text
|B_k(t)
 - (2 pi t)^(-1/2) exp(-a^2/2) * (1 + P_1(a)/t)|
 <= C_0 / (sqrt(2 pi t) t^2).
```

  Quote anchor:

```text
This note does not assemble the `SU(3)` determinant, the determinant mode tail, the half-slice operator tail, or the half-line gap theorem.
```

- [NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md)
  for the leading saddle profile, already-derived geometric piece, and
  saddle-tail proxy. Quote anchor:

```text
beta^(-3/2) r_(p,q)(beta)
    -> H(x,y) exp[-Q(x,y)],
H(x,y) = x y (x+y) / 2,
Q(x,y) = x^2 + x y + y^2.
```

- [GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md) for the source-character recurrence. Quote anchor:

```text
X = (chi_(1,0) + chi_(0,1)) / 6
```

  Quote anchor:

```text
X chi_(p,q)
 = (1/6) [ chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)
         + chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q) ]
```

- [frontier_su3_wilson_closed_form_fanout_2026_05_04.py](../scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py) for the exact Bessel determinant coefficient convention. Quote anchor:

```text
c_(p,q)(beta) = sum_(n in Z) det[I_(n + lambda_j + i - j)(beta/3)]_(i,j=1..3)
```

- The same operator-remainder note supplies the already-derived geometric
  piece and saddle-tail proxy. Quote anchor:

```text
K_geom(a) = 6 a^4 + 3 a^2 + 3 a + 1.
```

  Quote anchor:

```text
K_tail_sad(a) = ((a + 2)^3 / 8) exp[-3 a^2 / 4].
```

## Citation Boundary On The 25-34 Percent Prompt

The prompt requests a quote-anchor for a `25-34%` out-of-window mode-mass
measurement. The supplied determinant assembly note has no exact sentence
containing `25-34%`, `out-of-window`, or `mode-sum mass`. This note therefore
does not present that measurement as a quote-anchor. The runner independently
recomputes the exact determinant-mode witness at the `|n| <= floor(1.25 sqrt(t))`
window and prints:

| beta | `(p,q)` | outside mode mass |
|---:|---:|---:|
| 96 | `(6,5)` | `0.249199184790` |
| 192 | `(10,8)` | `0.344182812319` |

Those rows are witnesses. They are not a proof-side tail constant.

## What The Scalar Input Gives

For `t = beta/3`, `lambda = (p+q,q,0)`, and

```text
k_ij(n) = n + lambda_j + i - j,
```

The scalar local-CLT note supplies the entrywise replacement

```text
exp(-t) I_(k_ij(n))(t)
 = G_ij(n) * (1 + P_1(k_ij(n)/sqrt(t))/t) + absolute_error_ij,
```

with `G_ij(n) = (2 pi t)^(-1/2) exp[-k_ij(n)^2/(2t)]` and the scalar
absolute error bound. On a fixed compact determinant-mode window, the
determinant assembly note's multilinear identity gives the finite determinant
expansion and a Hadamard-style remainder envelope. The runner verifies this
finite algebra numerically on witness rows and prints the large `Hadamard
column product / |det G_n|` ratios that make generic cofactor control too loose
to normalize the determinant sum.

This is not a derived `K_W(A)`. A proof-side `K_W(A)` would require all of the following derived, non-fitted pieces:

```text
1. an analytic lower bound for c_(0,0)(beta) in the same Bessel-determinant normalization;
2. a uniform bound on the normalized first correction sum
   sum_n sum_j det G_n[j:P_1], including the c_(0,0) correction;
3. a true determinant-mode tail bound outside the active n-window;
4. a true representation-weight tail bound outside p,q <= A sqrt(beta).
```

The supplied authorities derive the scalar entry and the saddle proxy tail, but not these true determinant-normalization and true-tail pieces.

## Two Readings

Reading 1: strict no-import reading. The scalar local-CLT lemma may be inserted
into finite determinant windows. The attempt stops at the `c_(0,0)`
lower-normalization and true-tail step because the retained authorities do not
derive the needed determinant-mode and outside-weight domination constants. This
is the reading used for this note.

Reading 2: stronger analytic-estimate reading. If a future source note derives
a scalar-plus-mode theorem from the same exact Bessel atoms, proves a uniform
positive lower bound for `c_(0,0)`, and supplies true determinant-mode/weight
tails, then the determinant assembly note's formal expansion gives the next
algebraic surface for `K_W(A)`. This note does not take that estimate as an
input.

## Assembly Boundary

The Route B value-side arithmetic is conditional. If a later source note derives

```text
| beta^(-3/2) r_(p,q)(beta)
  - beta^(-3/2) d_(p,q) exp[-3 C2(p,q)/beta] |
 <= K_W(A) beta^(-1/2)
```

with the true-tail terms included, then the retained geometric arithmetic gives

```text
K_diag(A) = K_W(A) + K_geom(A).
```

This note does not derive `K_W(A)`, `K_diag(A)`, a half-line `beta_0`, or the half-line gap theorem. Writing any of those constants from the finite residual rows would be a fitted target-side step.

## Falsifiers

At `beta = 96`, `(p,q) = (6,5)`, displayed as `beta^(-3/2)` scaled values:

| substitution | value |
|---|---:|
| correct exact determinant ratio | `0.078225286971` |
| correct saddle `N_c = 3` | `0.079761275743` |
| wrong `N_c = 2` | `0.122681758828` |
| wrong `N_c = 4` | `0.051856618041` |
| wrong dimension omitted | `0.000292165845` |
| wrong determinant size `2x2` | `0.005101635871` |
| wrong highest-weight index `lambda = (p,q,0)` | `0.030362625798` |

Wrong cutoff scaling also changes the mode-tail witness at `beta = 192`, `(p,q) = (10,8)`, `A = 1.25`:

| cutoff | window | outside mode mass |
|---|---:|---:|
| `floor(A sqrt(t))` | `10` | `0.344182812319` |
| `floor(A beta^(1/3))` | `7` | `0.600571111925` |
| `floor(A sqrt(beta))` | `17` | `0.026879797238` |

These substitutions visibly change the object or the tail surface. They do not supply the missing domination estimate.

## What Is New Here

- The exact obstruction is moved from scalar-entry expansion to determinant
  normalization plus true tails.
- The runner reproduces the 24.9% and 34.4% mode-window witnesses from the exact Bessel determinant, while keeping them non-load-bearing.
- The note records that the requested quote-anchor for the 25-34% sentence is
  absent from the supplied determinant assembly note.
- The c00-normalization requirement is kept separate from the determinant-mode and outside-weight tail requirements.

## What Is Restated

- The scalar local-CLT note's `P_1` and absolute error bound.
- The determinant assembly note's finite determinant multilinear expansion and
  `H_det(A)` target.
- The operator-remainder note's leading saddle profile.
- The exact Bessel determinant convention and six-neighbor source recurrence.
- Rung eight's `K_geom(a)` and saddle-tail proxy.

## No-Go Discipline Gate

Skill freshness: the local no-go skill and the `origin/main` no-go skill text
were read; the `origin/main` N6 wording was followed for this note.

N1 - Alternative route enumeration:

1. Finite determinant multilinearity. ATTEMPTED. It succeeds on compact windows
   by the determinant assembly note's displayed formula, but it does not
   normalize the infinite mode sum.
2. Direct use of the scalar local-CLT absolute bound. ATTEMPTED. It bounds
   entry errors, but it does not provide the determinant-mode summation tail or
   `c_(0,0)` lower bound.
3. Operator-remainder saddle profile. ATTEMPTED. It supplies the leading
   `H exp[-Q]` target, but not the determinant-level remainder constant.
4. Operator-remainder saddle tail. ATTEMPTED. It bounds the saddle multiplier
   tail, and the determinant assembly note explicitly says the true Wilson tail
   still needs `H_det(A)` or a separate true-tail lemma.
5. Character recurrence route. ATTEMPTED. It supplies the six-neighbor graph and derivative-neighbor structure, but not an explicit Edgeworth/local-CLT theorem for the growing active window.
6. Numerical residual and mode-mass grid. ATTEMPTED as witness only. It is rejected as a proof route because fitting `K_W` or a tail constant from those rows would be value-from-target.

N2 - Wall-independence audit:

| wall | follows from another wall here? | note |
|---|---|---|
| `c_(0,0)` lower normalization | no | needed before any normalized `r_(p,q)` bound can be made uniform |
| determinant first-correction normalization | partially downstream of c00, but also needs cofactor/cancellation control | a c00 lower bound alone does not bound `S_1` |
| determinant-mode true tail | no | concerns the infinite `n` sum |
| outside-weight true tail | no | concerns `p,q > A sqrt(beta)` and the operator tail surface |

The collapsed wall set is: lower normalization plus true
determinant-mode/weight tail domination with determinant-correction control.
This note does not count a missing scalar lemma because the scalar local-CLT
note supplies it.

N3 - Hidden-wall scan:

The load-bearing phrases are `compact determinant-mode window`, `c_(0,0) lower normalization`, `true determinant-mode tail`, `outside-weight tail`, and `witness only`. They are explicit walls. No phrase like "standard" or "by construction" is used as a proof step.

N4 - Residual matching:

| cited source | residual there | residual here | match |
|---|---|---|---|
| scalar local-CLT note | scalar Bessel local-CLT entry remainder | entry input for determinant assembly | yes, as input only |
| determinant assembly note | `H_det(A)` determinant normalization and true tail | exact target here | yes |
| operator-remainder note | leading saddle profile | target profile, not a remainder proof | partial |
| operator-remainder note | `K_geom` and saddle tail | geometric piece and non-true-tail proxy | yes, scoped |
| character recurrence note | six-neighbor source graph | recurrence input, not tail proof | partial |

N5 - Rhetoric audit:

The negative statement is per-source-note and per-current-authority: `K_W(A)` is not derived here from the supplied authorities. It is not a statement about all possible determinant proofs. The note separates per-entry, per-mode, normalized determinant-sum, outside-weight, and operator-tail levels.

N6 - Partial-closure path scan:

No new axiom is named. The missing pieces are analytic source-side estimates: a determinant-normalization lemma and true-tail bounds. A convention reframe or approved primitive registry entry would not by itself provide those inequalities. The note avoids the phrase "no retained primitive supplies this", so the primitive-registry subcheck is not invoked.

N7 - Steelman:

A hostile reviewer could try to derive the missing package directly from the
exact Bessel determinant using the scalar note's integral proof as the entry
point, then add an internal Chernoff or Poisson-summation bound for
`exp(-t) I_k(t)`, a total-positivity lower bound for the singlet determinant,
and a summable Gaussian envelope for the determinant-mode tail. The strongest
support for that route is the scalar note's all-`a` absolute error and the
determinant assembly note's finite determinant expansion. This note does not
rule that route out; it records that those extra estimates are not derived in
the supplied authorities.

N8 - Cross-cycle echo:

The closest matching prior surfaces are the operator-remainder true-tail caveat
and the prior Wilson-to-saddle obstruction. Both isolate the same exact Wilson
determinant remainder rather than a scalar-entry failure. This note sharpens
that residual after the scalar local-CLT note by naming the determinant
normalization and true-tail pieces, not by broadening the negative claim.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_weyl_determinant_tail_domination_rung_eleven_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=16, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/native_gauge_transfer_weyl_determinant_tail_domination_rung_eleven_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
