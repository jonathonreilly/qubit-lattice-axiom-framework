# Conditional Static-Recurrence Positivity + Finite Relabeling Invariance

**Date:** 2026-05-28; scope repair 2026-07-19
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome; a source or runner edit requires independent
re-audit.
**Primary runner:**
[`scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py`](../scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py)
**Cached runner output:**
[`logs/runner-cache/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.txt`](../logs/runner-cache/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.txt)

## Scope repair

This note proves a conditional finite-matrix theorem. Its starting data are a
finite anti-Hermitian matrix and the explicitly stated alternating two-step
recurrence. It does **not** claim that the framework axioms select that
recurrence, a staggered kinetic branch, a Hamiltonian, a temporal-gauge
carrier, a Grassmann transfer kernel, or a Fock-space second quantization.

The labels “staggered”, “static links”, and “temporal gauge” below describe the
finite construction that motivated the matrices. They are not conclusions
derived from `MINIMAL_AXIOMS_2026-06-29.md`. In particular, this note starts
*after* the recurrence has been supplied.

The source claim has exactly two parts:

1. the supplied static classical recurrence has a positive-definite two-step
   matrix; and
2. determinant, spectrum, and exponential trace are invariant under supplied
   finite permutation-unitary conjugations.

No quantum-transfer, reflection-positivity, dynamical-gauge, P2, or
`AC_phi_lambda` consequence is part of the theorem.

## The bounded theorem

### Part A — conditional positivity of the classical two-step matrix

Let `K` be a finite-dimensional complex Hilbert space, let `h: K -> K`
satisfy

```text
h^dag = -h,
```

and let `m > 0`. Supply the alternating recurrence

```text
A_even = m I + h,                 A_odd = m I - h,

A_t psi_t + (1/2) psi_{t+1} - (1/2) psi_{t-1} = 0.
```

For `V_t = (psi_t, psi_{t-1})`, define the one-step companion matrices and
their two-step product by

```text
T_even = [[-2 A_even, I],         T_odd = [[-2 A_odd, I],
          [ I,        0]],                 [ I,       0]],

C(h,m) = T_odd T_even.
```

Then `C(h,m)` is Hermitian positive definite. If the eigenvalues of `h` are
`i lambda_j`, with `lambda_j` real, then

```text
spec(C(h,m)) = union_j {
    exp(+2 asinh(sqrt(m^2 + lambda_j^2))),
    exp(-2 asinh(sqrt(m^2 + lambda_j^2)))
}.
```

Thus every eigenvalue is real and strictly positive. The smaller member of
each reciprocal pair lies in `(0,1)`, because `m > 0`.

This is a theorem about `C(h,m)`. The notation does not identify `C(h,m)` with
a physical one-particle transfer kernel, and the smaller reciprocal roots are
not declared to be a quantum kernel.

### Proof

Because `m` is real and `h^dag=-h`, one has

```text
A_odd = A_even^dag,              T_odd = T_even^dag,
C(h,m) = T_even^dag T_even.
```

The matrix `T_even` is invertible: if `T_even(x,y)=(0,0)`, its lower
component gives `x=0` and its upper component then gives `y=0`. Consequently
`C(h,m)` is Hermitian positive definite directly.

It remains to compute its exact spectrum. Anti-Hermiticity makes `h` normal,
so a unitary `U` exists with

```text
U^dag h U = diag(i lambda_1, ..., i lambda_n),    lambda_j in R.
```

Conjugating both components of `K direct-sum K` by `U` decomposes `C(h,m)`
into `2 x 2` blocks

```text
C(lambda) =
  [[4(m^2 + lambda^2) + 1,  -2(m - i lambda)],
   [              -2(m + i lambda),             1]].
```

Each block is Hermitian and has

```text
det C(lambda) = 1,
tr  C(lambda) = 2 + 4(m^2 + lambda^2).
```

Put `q = sqrt(m^2 + lambda^2)`. The two eigenvalues are

```text
1 + 2q^2 +/- 2q sqrt(1+q^2)
  = (sqrt(1+q^2) +/- q)^2
  = exp(+/- 2 asinh(q)).
```

They are strictly positive, in agreement with the factorization above. QED.

### A supplied static-link realization of the hypothesis

The runner uses a finite periodic spatial carrier with a supplied list of
unitary link matrices `U_x`. It defines

```text
h[U]_{x,y} = (1/2)(U_x delta_{y,x+1}
                         - U_{x-1}^dag delta_{y,x-1}).
```

For every such list, the forward block and backward block are
minus-conjugate-transposes, so `h[U]^dag = -h[U]`. The theorem therefore
applies to the supplied matrix `C(h[U],m)`, including the runner's finite
`SU(3)` and `U(1)` examples.

This realization proves no axiom-to-carrier bridge. In particular, the
following remain input choices rather than conclusions of this row:

- the unitary-link carrier and its interpretation as a gauge background;
- time independence of the same spatial matrix over the two slices;
- the alternating matrices `A_even` and `A_odd`;
- the recurrence coefficient `1/2` and companion-matrix convention; and
- any identification of the recurrence roots with a Grassmann, Hilbert-space,
  or Fock-space transfer operator.

### Part B — finite conjugation invariance

Let `P` be a finite permutation unitary. Let `M` be any square matrix on the
same finite carrier, let `H` be any finite Hermitian matrix, and let `beta` be
real. Under the supplied relabeling rule

```text
M -> P M P^dag,                  H -> P H P^dag,
```

the following are unchanged:

```text
det(M),                          spec(H),
Z_beta(H) = Tr(exp(-beta H)).
```

Indeed,

```text
det(P M P^dag) = det(P) det(M) det(P^dag) = det(M),
spec(P H P^dag) = spec(H),
exp(-beta P H P^dag) = P exp(-beta H) P^dag,
Tr(P exp(-beta H) P^dag) = Tr(exp(-beta H)).
```

This applies when a relabeling of three selected modes is represented by a
permutation unitary extended by the identity. The representation of the
physical relabeling as conjugation is the stated hypothesis; the theorem does
not derive a physical species map or a selected `hw = 1` carrier.

## Runner exhibits

The paired runner checks seven consequences of the two theorem statements:

| Check | Exact theorem surface | Runner exhibit |
|---|---|---|
| modal formula | scalar mode `h = i lambda` | displayed eigenvalues agree with `exp(+/-2 asinh(sqrt(m^2+lambda^2)))` |
| identity-link specialization | supplied periodic `U_x = I` matrices | finite position-space spectrum agrees with the Fourier evaluation of the same supplied recurrence |
| sampled `SU(3)` matrices | 200 lists of supplied unitary `3 x 3` links | `h^dag=-h`, `C^dag=C`, `C=T_even^dag T_even`, and `min eig(C)>0` for every list; modal spectrum agrees |
| sampled `U(1)` matrices | 200 lists of supplied phases | same matrix checks |
| determinant invariance | finite `M -> P M P^dag` | invariant for all tested relabelings |
| spectrum invariance | finite Hermitian `H -> P H P^dag` | invariant for all six permutations of a three-mode carrier |
| exponential-trace invariance | `Tr(exp(-beta H))` | invariant for the same six permutations |

The random scans are regression exhibits, not the proof of positivity. The
proof is the all-`h` modal factorization above.

## Input and import audit

| Item | Role | Classification in this note | Claim treatment |
|---|---|---|---|
| finite complex Hilbert space `K` | carrier for the matrices | theorem setup | explicit hypothesis |
| `h^dag=-h`, `m>0` | load-bearing modal input | theorem hypothesis | explicit, not attributed to the framework axioms |
| alternating recurrence and `T_odd T_even` convention | defines `C(h,m)` | conditional construction input | explicit, not derived |
| supplied unitary link list | finite realization of `h^dag=-h` | runner/example input | no physical carrier inference |
| permutation action by conjugation | defines relabeling for Part B | theorem hypothesis | explicit |
| physical KS action, temporal gauge, Grassmann/Fock map | would be needed for a quantum-transfer reading | outside theorem | not consumed |
| determinant weight and gauge-half norm square | would be needed for a dynamical-gauge RP route | outside theorem | not consumed |

No fitted values, observations, empirical comparators, unit identifications,
or literature values are used. The minimal framework axioms are not a
load-bearing premise of this conditional matrix theorem.

## Scope firewall

The theorem does not establish any of the following:

- a Hamiltonian or transfer operator selected by the framework axioms;
- a staggered KS action derived from Lattice, Qubit, Admissibility, and Record;
- a physical temporal-gauge or time-dependent gauge carrier;
- positivity of a Grassmann transfer kernel or its inner product;
- a second-quantized or many-body operator `Gamma(t1)`;
- an Osterwalder-Schrader or reflection-positivity inequality;
- a `U`-integrated Wilson-plaquette gauge theorem;
- P2 phase blindness, scalar additivity beyond the Record axiom, or any
  `AC_phi_lambda` conclusion; or
- a continuum or OS-reconstruction statement.

These are exclusions from this row, not negative theorems about whether a
separate construction could establish them.

## Honest status

This source proposes only a bounded conditional finite-matrix theorem. Once
the anti-Hermitian matrix and alternating recurrence are supplied, the exact
positive-definite spectrum of `C(h,m)` closes by finite-dimensional linear
algebra. Once a finite relabeling is supplied as permutation conjugation,
`det`, `spec`, and `Tr(exp(-beta H))` are exactly invariant.

The earlier physical-transfer reading is removed. Independent re-audit is
required before the audit pipeline assigns any effective status.

## Dependencies and contextual filenames

There are no load-bearing source-note dependencies. The result is proved from
the hypotheses stated here.

The following plain-text filenames are context or excluded downstream routes,
not upstream dependencies of this theorem:

- `MINIMAL_AXIOMS_2026-06-29.md` — explains why a dynamics or kinetic branch
  must not be silently attributed to the minimal framework surface.
- `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md` — historical
  motivation for studying a two-step recurrence; not consumed.
- `STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md` — separate
  determinant theorem; not consumed by Part A or Part B.
- `REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`
  — separate abstract norm-square theorem; not applied here.
- `P2_PHASE_BLINDNESS_FROM_RP_TRANSFER_TRACE_BRIDGE_NOTE_2026-05-28.md` and
  `STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md` — downstream
  P2/realization context; no conclusion from either is claimed.

## Validation

Run:

```bash
python3 scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py
```

Expected scorecard line:

```text
SCORECARD: PASS=7 FAIL=0
```

The runner is a falsifier for the formulas and finite implementations. Audit
status remains owned by the independent audit lane.
