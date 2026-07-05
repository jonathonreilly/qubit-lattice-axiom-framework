# Native Gauge Transfer Weyl-Determinant Assembly Rung Ten Bounded Note

**Date:** 2026-06-12
**Claim type:** open_gate
**Type:** source-side sufficiency map

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

**Claim boundary:** this note tests the requested conditional assembly step. It
uses the scalar Bessel local-CLT input named below as `H_scalar`; it does not
re-prove that scalar input. The honest outcome is
partial-with-named-missing-link. `H_scalar` propagates to a finite, explicit,
entrywise determinant expansion on bounded determinant-mode windows. It does
not by itself supply the uniform Weyl-determinant cancellation/normalization
lemma, the determinant-mode/weight tail domination, or the reduced A2
spectral-domination lemma needed for both Route B and Route A.

`H_scalar` is supplied by the companion scalar note and treated as this
note's dependency; it is not re-proved here.

**Primary runner:** [scripts/native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_2026_06_12.py](../scripts/native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_2026_06_12.py)

**Runner cache:** [logs/runner-cache/native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_2026_06_12.txt)

No new axiom, literature value, external comparator, fitted constant, rounded anchor, parity proxy, or target-fed prefactor is used. The runner rows are witnesses only. They are not proof inputs for `K_W`.

## One-Hop Authorities And Context

- [`NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md`](NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md)
  supplies `H_scalar`, the scalar Bessel local-CLT atom and explicit
  remainder bound. This note uses it as a dependency and does not re-prove it.

- [`NATIVE_GAUGE_TRANSFER_HDET_GAUSSIAN_CORE_SUPPORT_NOTE_2026-06-18.md`](NATIVE_GAUGE_TRANSFER_HDET_GAUSSIAN_CORE_SUPPORT_NOTE_2026-06-18.md)
  supplies `H_det_core`, a bounded-support determinant-core check showing that
  the leading scalar Gaussian core, after 3x3 Weyl determinant mode summation
  and `(0,0)` normalization, aligns with the `SU(3)` saddle diagonal on the
  sampled active windows. This support does not derive `K_W(A)`, determinant
  tail constants, or `H_spec`.

- `NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md`
  is route-target context only, not a proof dependency, for the Route B
  value-side target and the already-derived geometric piece. Quote anchor:

```text
wilson_to_saddle_uniform(a):
| beta^(-3/2) r_(p,q)(beta)
  - beta^(-3/2) d_(p,q) exp[-3 C2(p,q)/beta] |
 <= K_W(a) beta^(-1/2)
```

  Quote anchor:

```text
K_diag(a) = K_W(a) + K_geom(a).
```

  Quote anchor:

```text
K_geom(a) = 6 a^4 + 3 a^2 + 3 a + 1.
```

- `NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md`
  is route-target context only, not a proof dependency, for the Route A
  derivative-side constants and the exact spectral inequality still needed.
  Quote anchor:

```text
The requested domination would require `c_D <= c_J` plus a uniform subleading
bound.
```

  Quote anchor:

```text
derive or bound c_D <= c_J for the reduced spectral pair, then transfer it to
the exact Wilson diagonal with explicit active-window and tail remainders.
```

- [NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md)
  supplies the reduced saddle profile and the already-separated
  operator-remainder surface. Quote anchor:

```text
beta^(-3/2) r_(p,q)(beta)
    -> H(x,y) exp[-Q(x,y)],
H(x,y) = x y (x+y) / 2,
Q(x,y) = x^2 + x y + y^2.
```

- [frontier_su3_wilson_closed_form_fanout_2026_05_04.py](../scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py) for the exact Bessel-determinant coefficient convention. Quote anchor:

```text
c_(p,q)(beta) = sum_(n in Z) det[I_(n + lambda_j + i - j)(beta/3)]_(i,j=1..3)
```

- [GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md) for the source-character recurrence used by the half-slice and derivative transfer. Quote anchor:

```text
X = (chi_(1,0) + chi_(0,1)) / 6
```

  Quote anchor:

```text
X chi_(p,q)
 = (1/6) [ chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)
         + chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q) ]
```

## H_scalar

The scalar hypothesis tested here is the W85 local-CLT shape:

```text
exp(-t) I_k(t)
 = (2 pi t)^(-1/2) exp[-k^2/(2t)]
   (1 + P_1(k/sqrt(t))/t + R_2(k,t)),
|R_2(k,t)| <= C(A) t^(-2)
```

uniformly for `|k| <= A sqrt(t)`. In the Wilson coefficient, `t = beta/3`, `lambda = (p+q, q, 0)`, and

```text
k_ij(n) = n + lambda_j + i - j.
```

Both readings of the ambiguity:

1. **Literal compact-window reading.** `H_scalar` controls entries only after a finite determinant-mode cutoff and a finite active-weight cutoff have been selected. It does not give the infinite determinant-mode tail or the representation-weight tail by itself.
2. **Strengthened reading.** If `H_scalar` is paired with a scalar tail domination strong enough to sum all determinant modes and all outside-window representation weights, then the remaining value-side obstruction is the Weyl-determinant cancellation/normalization step below. Route A still needs the reduced spectral comparison `c_D <= c_J`.

## Determinant Propagation Available From H_scalar

Fix a bounded determinant-mode and active-weight window where all `|k_ij(n)| <= R sqrt(t)`. Define

```text
G_ij(n) = (2 pi t)^(-1/2) exp[-k_ij(n)^2/(2t)],
P_R = sup_(|z|<=R) |P_1(z)|,
C_R = C(R).
```

For each mode `n`, write the scaled entry matrix as

```text
B_ij(n,t) = exp(-t) I_(k_ij(n))(t)
          = G_ij(n) [1 + P_1(k_ij(n)/sqrt(t))/t + rho_ij(n,t)],
|rho_ij(n,t)| <= C_R/t^2.
```

Let `G_n` be the `3x3` matrix with entries `G_ij(n)`. Let `G_n[j:P_1]` mean `G_n` with column `j` replaced by the column whose entries are `G_ij(n) P_1(k_ij(n)/sqrt(t))`. Determinant multilinearity gives the finite algebraic expansion

```text
det B_n
 = det G_n
   + t^(-1) sum_(j=1)^3 det G_n[j:P_1]
   + E_n.
```

The derived finite remainder bound is

```text
|E_n|
 <= Had_n Theta_R(t),
Had_n = prod_(j=1)^3 || column_j(G_n) ||_2,
Theta_R(t) = (1 + P_R/t + C_R/t^2)^3 - 1 - 3 P_R/t.
```

This is an exact finite determinant propagation of the scalar pieces. Summing over a truncated mode set `|n| <= M sqrt(t)` gives

```text
E_lambda^trunc(M,R,t)
 <= Theta_R(t) sum_(|n|<=M sqrt(t)) Had_n.
```

This is not yet K_W(a). The 2026-06-18 `H_det_core` support note checks that
the leading Gaussian determinant mode sum has the correct normalized saddle
shape on sampled active windows. The missing step is now narrower than
entrywise scalar control: it is the determinant-level passage from the exact
Bessel mode sums

```text
S_0(lambda,t) = sum_n det G_n,
S_1(lambda,t) = sum_n sum_j det G_n[j:P_1]
```

to the normalized Wilson ratio

```text
r_(p,q)(beta) = c_(p,q)(beta) / c_(0,0)(beta)
```

with the exact `SU(3)` saddle normalization

```text
d_(p,q) exp[-3 C2(p,q)/beta].
```

The needed additional value-side ingredient is:

```text
H_det(A):
  a uniform Weyl-determinant cancellation/normalization lemma for the
  3x3 Bessel determinant mode sum, including c_(0,0) lower normalization
  and determinant-mode tail domination, converting H_scalar into
  wilson_to_saddle_uniform(A) with an explicit K_W[A; P_1, C].
```

Without `H_det(A)`, a source note that writes a numerical `K_W` from the finite residual rows would be fitting a constant to the target. That would violate the anti-fabrication rule.

## Mode And Weight Tail

The saddle tail already available from rung eight is, for `max(x,y) > A`, `A >= 1`,

```text
K_tail_sad(A) = ((A + 2)^3 / 8) exp[-3 A^2 / 4].
```

This follows from `s = x + y > A`, `Q >= 3 s^2/4`, and the saddle polynomial bound. It is a saddle multiplier tail, not a true Wilson tail.

For the true Wilson diagonal, `H_scalar` on compact windows can bound a finite annulus after the determinant propagation above, and `H_det_core` checks the leading Gaussian determinant normalization on sampled active windows. These do not control the exact-Bessel infinite determinant-mode sum or the full outside-weight region unless they are supplemented by the tail clause inside `H_det(A)` or by a separate true-tail lemma. The exact next path this opens is therefore a determinant-level tail domination statement, not a scalar fit.

## Route B Assembly

If a future source note supplies `H_det(A)` and hence

```text
| beta^(-3/2) r_(p,q)(beta)
  - beta^(-3/2) d_(p,q) exp[-3 C2(p,q)/beta] |
 <= K_W(A) beta^(-1/2)
```

on the active window, then W85's arithmetic applies:

```text
K_diag(A) = K_W(A) + K_geom(A),
K_geom(A) = 6 A^4 + 3 A^2 + 3 A + 1.
```

With a true-tail contribution `K_tail_true(A,beta)` and the existing half-slice contraction, a relative operator error of the form

```text
epsilon(beta) <= K_total(A) / sqrt(beta)
```

would give the W85 perturbation threshold

```text
beta > (2 K_total(A) / (1 - L))^2,
L = 0.1938058
```

where the `L` row is reused only in the fenced W85 perturbation arithmetic. This note does not derive `K_total(A)` or a beta threshold, because `K_W(A)` and the true-tail piece are not derived from `H_scalar` alone.

## Route A Assembly

The character recurrence gives the exact beta-derivative of the Wilson coefficient through neighboring coefficients:

```text
c'_(p,q)(beta) = (1/6) sum_{nu in N(p,q)} c_nu(beta).
```

Therefore, if `H_det(A)` transfers `H_scalar` to the Wilson diagonal uniformly for the active window and its one-step neighbor shell, the same value-side transfer controls the diagonal derivative term `Delta_D` up to explicit active-window and tail remainders. This addresses the exact-Wilson transfer part named in W86.

It does not prove the reduced spectral inequality. W86's reduced constants are

```text
c_J = A_0 - A_1,
A_i = <Phi_i, L Phi_i>,
```

and

```text
c_D = B_1/mu_1 - B_0/mu_0,
B_i = <Phi_i, S_(1/2) M_[Q H exp(-Q)] S_(1/2) Phi_i>.
```

The additional Route A ingredient is:

```text
H_spec:
  a reduced A2 spectral-domination lemma proving c_D <= c_J with an
  explicit subleading margin for the isolated reduced spectral pair.
```

`H_scalar` concerns scalar Bessel entries. It does not determine the reduced eigenfunctions `Phi_i` or compare the two reduced Rayleigh quotients above. That is why it cannot yield `c_D <= c_J` by itself.

## Sufficiency Verdict

H_scalar is necessary but not sufficient for the two-route half-line assembly.
H_scalar plus H_det_core is necessary but not sufficient for the two-route half-line assembly.

The precise outcome is:

```text
partial-with-named-missing-link:
  H_scalar + H_det(A) opens Route B value-side assembly;
  H_scalar + H_det(A) transfers the exact Wilson derivative side;
  Route A still needs H_spec, the reduced A2 spectral-domination lemma.
```

Thus W87 finishing the scalar Bessel lemma and the 2026-06-18 Gaussian-core
support are not, by themselves, the whole theorem. The next path is now a
focused exact-Bessel `H_det_remainder(A)` determinant-normalization/tail note
and a separate `H_spec` reduced-spectral comparison note.

## Witness Rows

The runner recomputes the true `SU(3)` Bessel determinant using scaled Bessel entries `exp(-t) I_k(t)`, so the common exponential cancels in the ratio.

Finite exact-to-saddle rows, witnesses only:

| beta | `(p,q)` | exact `r_(p,q)` | saddle `d exp[-3 C2/beta]` | relative difference |
|---:|---:|---:|---:|---:|
| 48 | `(4,3)` | `25.894978539180` | `26.882522035981` | `-3.673552e-02` |
| 96 | `(6,5)` | `73.579022615880` | `75.023779892741` | `-1.925732e-02` |
| 192 | `(10,8)` | `207.380571748836` | `209.688188327461` | `-1.100499e-02` |

Active-grid witness rows for `A = 1.25`, displayed as `sqrt(beta)` times the maximum beta-scaled exact-to-saddle diagonal difference:

| beta | cap `floor(1.25 sqrt(beta))` | max row | value |
|---:|---:|---|---:|
| 48 | 8 | `(5,5)` | `2.710005629592e-02` |
| 96 | 12 | `(7,7)` | `1.907301888919e-02` |
| 192 | 17 | `(10,11)` | `1.337437050442e-02` |

The determinant-cancellation witness in the runner prints, for several modes, `Hadamard column product / |det G_n|` around `3e2` to `5e2`. That row explains why a generic cofactor bound is not a determinant normalization lemma. It is not used as a proof of impossibility.

## Falsifiers

At `beta = 96`, `(p,q) = (6,5)`, all rows are displayed as `beta^(-3/2)` scaled values:

| substitution | value |
|---|---:|
| correct exact determinant ratio | `0.078225286971` |
| correct saddle `N_c = 3` | `0.079761275743` |
| wrong `N_c = 2` | `0.122681758828` |
| wrong `N_c = 4` | `0.051856618041` |
| wrong dimension omitted | `0.000292165845` |
| wrong determinant size `2x2` | `0.005101635871` |
| wrong highest-weight index `lambda = (p,q,0)` | `0.030362625798` |

These wrong-structure substitutions visibly change the object. They do not supply `K_W`.

## What Is New Here

- The explicit finite determinant propagation of `H_scalar` through the `3x3` Weyl determinant, including the `Theta_R(t)` remainder functional.
- The distinction between an entrywise scalar expansion and a normalized Weyl-determinant coefficient expansion.
- The sufficiency verdict: `H_scalar` by itself is not enough for both routes; the named additional ingredients are `H_det(A)` and `H_spec`.

## What Is Restated

- W85's `wilson_to_saddle_uniform(a)` target and `K_diag = K_W + K_geom`.
- W86's `c_J/c_D` structure and the need for `c_D <= c_J`.
- Rung six's leading saddle profile `H exp[-Q]`.
- The exact Bessel-determinant coefficient convention and the six-neighbor character recurrence.

## No-Go Discipline Gate

This section records the N1-N8 no-go discipline pass for the narrow
negative boundary: `H_scalar` alone is not sufficient for the two-route
half-line assembly. It is not an audit verdict.

N1 - Alternative route enumeration:

1. Entrywise determinant propagation. ATTEMPTED. It succeeds at the finite multilinear expansion above, but stops before normalized `K_W` because determinant cancellation and `c_(0,0)` normalization are not supplied by entrywise bounds.
2. Direct determinant Gaussian core evaluation. ATTEMPTED and partially
   supported by the 2026-06-18 `H_det_core` note for sampled active windows.
   It still does not turn exact Bessel `S_0,S_1` into an explicit
   `K_W[A;P_1,C]`.
3. Compact-window tail by H_scalar. ATTEMPTED. The literal scalar hypothesis
   controls finite annuli, and `H_det_core` verifies the leading Gaussian
   determinant-core normalization on sampled active windows, but the
   exact-Bessel infinite determinant-mode and outside-weight tails need an
   added domination clause.
4. Exact derivative transfer by recurrence. ATTEMPTED. The recurrence transfers value-side coefficient bounds to one-step derivative neighbors, but it does not compare the reduced spectral constants.
5. Reduced spectral comparison. ATTEMPTED through W86. The formal `c_J/c_D` quantities are identified, but `c_D <= c_J` is not derived by the scalar Bessel hypothesis.
6. Numerical residual grid. ATTEMPTED as a witness only. It is rejected as a proof route because fitting a `K_W` from those rows would be value-from-target.

N2 - Wall-independence audit:

| wall | closes if H_scalar is proved? | independent reason |
|---|---|---|
| `H_det_remainder(A)` exact-Bessel determinant cancellation/normalization and true tail | no | `H_det_core` covers the leading Gaussian core; the remaining wall concerns scalar correction propagation, exact-Bessel tails, and `c_(0,0)` lower constants |
| `H_spec` reduced A2 spectral domination | no | it concerns reduced eigenfunctions and Rayleigh quotients, not Bessel coefficient asymptotics |

Closing `H_det_remainder(A)` would not prove `H_spec`. Closing `H_spec` would
not provide `K_W(A)` or true tails. The collapsed wall set therefore has two
independent additions beyond `H_scalar + H_det_core`.

N3 - Hidden-wall scan:

The phrases "bounded determinant-mode window", "c_(0,0) lower normalization", "true-tail", "reduced spectral pair", and "subleading margin" are load-bearing and promoted to named ingredients. "H_scalar" is explicitly conditional. "Witness" rows are marked as non-proof numerical checks.

N4 - Residual matching:

| cited source | residual there | residual here | match |
|---|---|---|---|
| W85 | `wilson_to_saddle_uniform(a)` | value-side `K_W(A)` from determinant assembly | yes |
| W86 | `c_D <= c_J` plus exact-Wilson transfer | Route A reduced spectral domination plus transfer | yes |
| Rung six | leading `H exp[-Q]` profile | leading object for determinant assembly | partial, not a remainder proof |
| Character recurrence note | exact six-neighbor `J` | derivative transfer through neighboring coefficients | yes |

N5 - Rhetoric audit:

The negative statement is at source-note sufficiency scope: `H_scalar` alone is not enough for the two-route assembly. It is not a statement that a determinant-level proof or reduced spectral proof cannot be supplied. Per-entry, per-mode, determinant-summed, and operator-tail levels are separated explicitly.

N6 - Partial-closure path scan:

No new axiom is named. The next paths are analytic source-side ingredients: `H_det(A)` for determinant cancellation/normalization and true tails, and `H_spec` for the reduced spectral comparison. A convention or label change would not supply either analytic inequality.

N7 - Steelman:

A hostile reviewer could try to fold `H_det(A)` into W87 by proving a stronger scalar theorem: not just entrywise `H_scalar`, but a scalar-plus-mode theorem with Gaussian tail domination and a ready-made determinant Gaussian core evaluation. If W87 actually delivers that stronger package, then the value-side wall named here would shrink to checking the finite algebra and denominator normalization constants. That still would not prove `H_spec`, because W86's `c_D <= c_J` is a reduced spectral statement about `T_infty` eigenfunctions.

N8 - Cross-cycle echo:

Repo search found a similar local-CLT tail issue in the lattice Green note. There, a different retained stronger theorem carried the asymptotic while the direct local-CLT route was left non-load-bearing. No analogous stronger retained theorem was found here for the Weyl-determinant `K_W(A)` or for `c_D <= c_J`. The echo supports keeping the current outcome partial and named rather than promoting a scalar-entry lemma into a determinant/operator theorem.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=26, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
