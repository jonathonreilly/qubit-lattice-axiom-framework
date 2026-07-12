# Records-Only OS Reconstruction on a Time-Homogeneous Untied First-Order Measure

**Date:** 2026-07-11

**Type:** bounded_theorem

**Lane alias:** `rhalf block 10`

**Primary runner:**
[`scripts/frontier_records_only_os_reconstruction_2026_07_11.py`](../scripts/frontier_records_only_os_reconstruction_2026_07_11.py)

**Runner cache:**
[`logs/runner-cache/frontier_records_only_os_reconstruction_2026_07_11.txt`](../logs/runner-cache/frontier_records_only_os_reconstruction_2026_07_11.txt)

**Source-side scorecard:** `PASS=24`, `FAIL=0`

## Boundary

This note studies one finite construction:

- a bilinear one-component Grassmann measure on two history slices;
- the declared generation coupling `W = a I + b C + c C^2`, with `C^3 = I`;
- the same coupling `W` on both slices;
- the staggered crossing convention `-1/2,+1/2`; and
- the record span `{1, N, TCsym, e2, e3}`, conditional on the cited orbit
  clause that makes this span P-even.

On the nonsingular normalized-Gram domain, the exact results are:

1. the records-only Gram is Hermitian exactly on two branches:
   `W^dagger = W` (the K-tied branch) or `W^dagger = P W P` (the all-real
   branch);
2. the tied branch is positive definite on its whole domain;
3. the all-real branch is positive semidefinite exactly when
   `(Im lambda_1)^2 <= 1/8`, and positive definite exactly when the inequality
   is strict;
4. under a separate spectral-readout identification and a separate
   three-distinct-value condition, the all-real branch is degenerate and the
   tied branch is the only survivor.

The theorem therefore forecloses an outcome-only, generic complex weight
inside this time-homogeneous two-slice OS construction. It does not foreclose
other emergent-time constructions. In particular, the alternating
`W^dagger,W` measure is an exact live escape once time-homogeneity is dropped.

This note does not derive `r = 1` or `r = 1/2`. The identities involving
`|b|^2` and `|lambda_1|^2` are weight identities, not a physical
equipartition law. The K-reality stage and the value/equipartition question
remain separate, as required by the reviewed block-9 boundary.

This source note does not set or predict an audit outcome, adopt a premise, or
edit audit-lane-owned data. Every cited scientific source is consumed only at
its declared source scope; no audit grade is imported.

## Correction record (supervisor review, honored exactly)

An earlier draft of this note (committed under the NARROW_NO_GO genre) claimed
"reality of registrable correlators ⟺ the tie" and "the Gram is Hermitian iff
tied." **Both claims are false** and are withdrawn. The counterexample —
verified exactly here (checks 11, 15) — is the all-real untied point
`(a,b,c) = (4/5, 3/10, 1/2)` (`b ≠ c`, genuinely off the tie): the registrable
readout is exactly real (`⟨N⟩ = 735/152`), `Z = 114929/250000` exactly, and the
registrable Gram is Hermitian and exactly positive definite. The fixed set of
the records-only Hermiticity is **larger than the tie**: it is the two-branch
union derived below. The corrected genre is this bounded theorem. Every exact
value quoted in the earlier draft (the toy Gram, `⟨N⟩ = 6+3i`, the `⟨N,N⟩`
fraction) verifies unchanged; what changes is the fixed-set characterization
and the verdict's shape.

## The reviewed block-9 handoff

The reviewed
[`Koide first-order section fork`](KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md)
separates two questions:

1. where K-reality is imposed in the analytic construction; and
2. which equipartition law, if any, fixes the physical value of `r`.

Block 9 leaves both questions open and names a full OS test as a live route for
the first. This note executes that test for the time-homogeneous two-slice
construction above. It does not transfer the conditional endpoint equations
from block 9 into a value theorem.

## Reflection and the P mechanism

The OS reflection is the antilinear antiautomorphism with history-index
reversal and the staggered field action cited by the
[`two-slice Berezin Gram note`](RP_COUPLED_TWO_SLICE_GAUGE_STAGGERED_BEREZIN_GRAM_NARROW_THEOREM_NOTE_2026-07-10.md):

```text
theta(chi(x,t))    = -chibar(x,1-t),
theta(chibar(x,t)) = -chi(x,1-t),
theta^2 = 1.
```

At the field level,

```text
theta(chibar(1) W chi(1)) = chibar(0) W^dagger chi(0),
W^dagger = conjugate(a) I + conjugate(c) C + conjugate(b) C^2.
```

The generation inversion `P` exchanges generations 1 and 2 and obeys

```text
P C P = C^2,
P W(a,b,c) P = W(a,c,b) = W^T.
```

It permutes complete `(chibar,chi)` pairs, so the Berezin measure is even
under `P`. On the cited orbit-clause reading of the
[`registrable-readout note`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md),
the stated record span is P-even. The complementary
[`K-odd registered-datum test`](ACPHILAMBDA_K_ODD_CARRIER_REGISTERED_DATUM_TEST_BOUNDED_NOTE_2026-07-03.md)
is used only at that declared source grade. If a P-odd registrable readout is
later established, the all-real branch is no longer protected by this
symmetry.

The exact reflection identity is

```text
<theta(Y)>_(W0,W1)
    = conjugate(<Y>_(W1^dagger,W0^dagger)).
```

For a time-homogeneous Gram this gives

```text
G_ij(W) = conjugate(G_ji(W^dagger)).
```

P-covariance supplies the two sufficient branches immediately. The next
section proves that the stated record Gram has no third branch.

## Exact two-branch fixed-set certificate

Let `lambda_0,u,v` be the three circulant eigenvalues. In the Fourier basis the
record generators are

```text
n0 = (N + TCsym)/3,
p  = (2N - TCsym)/3,
e2 = n0 p + q,
e3 = n0 q,
```

where `p=n1+n2` and `q=n1 n2` on the doublet pair. The normalized one-mode
even Gram on `{1,n0}` is

```text
A(lambda_0) = [[1, -lambda_0/D0],
               [-lambda_0/D0, 1/D0]],
D0 = lambda_0^2 + 1/4.
```

Hermiticity of the record Gram implies Hermiticity of this sub-Gram. Since
`D0` is nonzero, `1/D0` and `lambda_0/D0` are real only when `lambda_0` is
real.

For the doublet pair, put

```text
D = (u^2+1/4)(v^2+1/4).
```

The P-even pair Gram on `{1,p,q}` contains

```text
B_qq = 1/D,
B_1q = uv/D,
B_pq = -(u+v)/D.
```

The record vectors above make these entries recoverable from the 5-by-5 Gram;
the singlet matrix `A` is invertible. Hermiticity therefore makes `D`, `uv`,
and `u+v` real. The two numbers `u,v` are roots of a quadratic with real
coefficients. They are consequently either both real or a complex-conjugate
pair.

Thus:

- all three eigenvalues real is exactly `W^dagger=W`, equivalently `a` real
  and `c=conjugate(b)`;
- `lambda_0` real and `v=conjugate(u)` is exactly `W^dagger=PWP`, equivalently
  `a,b,c` all real.

This is the missing necessity certificate. The four exact off-union witnesses
in check 19 test distinct ways to violate it, but the proof does not rest on
those witnesses.

## Reality diagnostics

On both branches,

```text
<N> = Tr(W^-1) = 3(a^2-bc)/(a^3+b^3+c^3-3abc)
```

is real. The K-odd separator
`<chibar(C-C^2)chi>` remains non-real at generic tied points, so the P-even
restriction is doing real work. The all-real untied point in the Correction
record shows why reality does not select the tied branch by itself. At the
generic complex point

```text
(a,b,c)=(4/5+i/10, 3/10+i/5, 1/2-i/10),
```

the runner gives `<N>=6+3i` exactly.

## Partition function and positivity

The two-slice kernel is

```text
K = [[-W, -I/2],
     [ I/2, -W]],
```

and

```text
Z = det(W^2+I/4) = product_k (lambda_k^2+1/4).
```

On the tied branch every eigenvalue is real, so `Z>0`. On the all-real branch
`lambda_2=conjugate(lambda_1)` and

```text
Z=(lambda_0^2+1/4)|lambda_1^2+1/4|^2.
```

The generic off-union witness has complex `Z`; complex `Z` is a witness, not
a claim that every off-union point has complex determinant.

### Tied branch: analytic whole-domain certificate

For one real eigenvalue `ell`, the unnormalized full one-mode OS Gram on
`{1,chibar,chi,n}` is

```text
H(ell) = [[ell^2+1/4, 0,   0,   -ell],
          [0,           1/2, 0,    0  ],
          [0,           0,   1/2,  0  ],
          [-ell,        0,   0,    1  ]].
```

Its leading minors are

```text
ell^2+1/4, (ell^2+1/4)/2, (ell^2+1/4)/4, 1/16,
```

all strictly positive. The three-mode form is a tensor product of these
positive forms. Restricting it to the five record vectors preserves positive
definiteness. The tied scan in check 14 is therefore coverage, not the proof.
In particular, a negative single-slice `det W` does not spoil the two-slice
Gram.

### All-real branch: exact full-record strip theorem

Write

```text
lambda_1=x+iy,
lambda_2=x-iy,
q1,2 = 4x^2 -/+ 8xy - 4y^2 + 1,
d1,2 = 4|lambda_1 -/+ i/2|^2.
```

On the pair basis `{1,p,q}`, the leading minors are

```text
1,
8 q1 q2/(d1 d2)^2,
128(1-8y^2)/(d1 d2)^3.
```

The two remaining 2-by-2 principal minors are

```text
16(8x^2-8y^2+1)/(d1 d2)^2,
128/(d1 d2)^2.
```

The discriminant of each `q` as a quadratic in `x` is
`16(8y^2-1)`. Hence the pair Gram is positive definite for `y^2<1/8`,
positive semidefinite at `y^2=1/8`, and indefinite for `y^2>1/8`.

The full five-vector result follows without a scan. In tensor coordinates

```text
{1x1, 1xp, 1xq, n0x1, n0xp, n0xq},
```

the record vectors are the columns of

```text
V = [[1, 0,  0, 0, 0],
     [0, 1, -1, 0, 0],
     [0, 0,  0, 1, 0],
     [0, 1,  2, 0, 0],
     [0, 0,  0, 1, 0],
     [0, 0,  0, 0, 1]],
```

with `rank(V)=5`, and

```text
G_record = V^T (A(lambda_0) tensor B(x,y)) V.
```

The singlet factor `A` is positive definite. Inside the strip, positivity of
the tensor product and its restriction is immediate. Outside the strip, `B`
has one negative direction, so `A tensor B` has two. Every five-dimensional
subspace of this six-dimensional space meets that negative subspace; the
record restriction is therefore not positive semidefinite. At the boundary
the restriction is positive semidefinite and singular.

Since `y=sqrt(3)(b-c)/2`, the equivalent coupling condition is

```text
(b-c)^2 <= 1/6  for positive semidefiniteness,
(b-c)^2 <  1/6  for positive definiteness.
```

The constant belongs to the stated `-1/2,+1/2` crossing convention.

### Exact witnesses

- `(4/5,3/10,1/2)` is all-real, untied, Hermitian, and positive definite,
  with `Z=114929/250000`.
- Three exact all-real points beyond the strip have negative principal minors.
- The generic complex point has
  `<N,N>=87325191888/10461538613 -
  (19246073016/10461538613)i` and a non-Hermitian Gram.

## What the result says about the K-reality stage

Within the explicit time-homogeneous condition, the OS reflection acts on the
weight and restricts it to the two real branches above. The alternating
past/future choice `W^dagger,W` restores a Hermitian positive Gram for generic
complex `W`. That construction is not time-homogeneous and requires a
separate rule for placing the conjugation flip. The framework does not supply
or forbid that rule: it is a live conditional escape outside this theorem.

The actual
[`Qualification`](MINIMAL_AXIOMS_2026-06-29.md#qualification)
says that a choice not fixed by supplied structure remains a named conditional
or open dependency. It does not license the homogeneous choice or ban the
alternating one.

## Weight identities do not select `r`

The exact determinant identities are:

- on the tied branch,
  `partial_b partial_conjugate(b) det W = -3a`;
- on the all-real branch,
  `lambda_1 lambda_2 = |lambda_1|^2 =
  (a-(b+c)/2)^2 + 3(b-c)^2/4`.

They show conjugate-pair dependence in the weight. They do not say how an
energy or probability law counts those slots. The alternative endpoint
equations still give `r=1` and `r=1/2` when their respective equipartition
laws are supplied, but neither law is derived here. The runner keeps this
bookkeeping as a regression guard and no longer labels it a grain selection.

## Conditional branch selection by non-degeneracy

On the all-real branch, `lambda_2=conjugate(lambda_1)`. A real K-even
per-member function therefore gives the same value on the doublet pair. At
most two distinct values remain after including the singlet.

The tied branch can carry three distinct real eigenvalues; the runner gives
the exact example

```text
7/5, 1/2-sqrt(3)/5, 1/2+sqrt(3)/5.
```

Therefore the tied branch is uniquely selected only after adding both:

1. the modeling identification of a per-member registered value with a real
   K-even function of the spectral datum; and
2. the qualitative comparator condition that the registered pattern has
   three distinct values.

No measured mass or numerical threshold is used. The distinctness condition
is still an explicit observational comparator, not a derived theorem.

## No-Go Discipline Gate

**Status: PASS after narrowing.** The negative boundary is only the failure of
the outcome-only generic complex cell inside the stated time-homogeneous
two-slice OS construction.

### N1 — alternative routes

| route | honesty marker | result |
| --- | --- | --- |
| remove scalar conjugation from `theta` | ATTEMPTED | The field-level check and the cited toy Gram show that this is not the stated OS reflection. |
| enlarge the record algebra with P-odd data | ATTEMPTED | It escapes the P-even proof; the current orbit-clause condition excludes it only at the cited source grade. |
| use a non-OS emergent-time construction | ATTEMPTED | Genuinely open; this theorem says nothing about it. |
| alternate `W^dagger,W` across the two slices | ATTEMPTED | Exact live escape; the runner finds a positive Gram after dropping time-homogeneity. |
| replace OS positivity by a weaker spectral condition | ATTEMPTED | Genuinely open; no such reconstruction theorem is imported. |
| stay on the all-real strip with a degenerate pattern | ATTEMPTED | Lawful inside this construction when the three-distinct-value condition is dropped. |

### N2 — wall independence

The negative boundary uses three conditions: `H` (time-homogeneity), `O` (the
stated OS reflection and crossing), and `R` (the P-even record span). The tie
selection adds `S` (spectral-readout identification) and `D` (three distinct
registered values). Pairwise independence is:

| pair | first closes second? | second closes first? | independent? |
| --- | --- | --- | --- |
| H–O | no | no | yes |
| H–R | no | no | yes |
| H–S | no | no | yes |
| H–D | no | no | yes |
| O–R | no | no | yes |
| O–S | no | no | yes |
| O–D | no | no | yes |
| R–S | no | no | yes |
| R–D | no | no | yes |
| S–D | no | no | yes |

The value/equipartition residual is separate from all five and is not counted
as a wall of the Hermiticity theorem.

### N3 — hidden-wall scan

| phrase or idea | classification |
| --- | --- |
| time-homogeneous law | explicit load-bearing condition H; not a licensed default |
| standard OS reflection | explicit condition O with linked source machinery |
| registrable or canonical record span | explicit condition R through the orbit clause; P-odd extension remains an escape |
| alternating measure “by construction” | exact alternative, not evidence against itself |
| intrinsic conjugation | intrinsic only to the stated antilinear OS reflection |
| `C_3[111]` coupling | declared finite probe and domain scope, not a derived Yukawa |
| `-1/2,+1/2` crossing | explicit normalization convention fixing the strip constant |

No hidden framework primitive is used. The approved kinetic-isotropy primitive
does not supply time-homogeneity, an OS dynamics, a record algebra, a spectral
readout, or non-degeneracy.

### N4 — residual matching

| cited source | residual it addresses | residual used here | match? |
| --- | --- | --- | --- |
| [block 9](KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md) | stage and equipartition are separate open questions | this note tests only one stage construction | yes |
| [two-slice Berezin Gram](RP_COUPLED_TWO_SLICE_GAUGE_STAGGERED_BEREZIN_GRAM_NARROW_THEOREM_NOTE_2026-07-10.md) | reflection/crossing machinery | supplies O, not the fixed-set conclusion | yes |
| [history-index note](TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md) | history-index time with an open representation bridge | history-index reversal only | yes |
| [registrable-readout note](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md) | orbit-clause record scope | supplies condition R at declared grade | yes |
| [K-odd datum test](ACPHILAMBDA_K_ODD_CARRIER_REGISTERED_DATUM_TEST_BOUNDED_NOTE_2026-07-03.md) | K-odd exclusion at its tested scope | complementary support for R only | yes |

The
[`two-step transfer template`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
is context for the construction, not a witness that closes any residual.

### N5 — rhetoric audit

The proof reaches the stated five-vector record Gram and its singlet/doublet
mode blocks. It does not reach interacting actions, non-`C_3` couplings,
multiple time steps, a lattice-wide transfer matrix, or every emergent-time
construction. Every use of “foreclosed” is restricted to the declared
time-homogeneous two-slice OS domain.

### N6 — partial-closure paths

- Dropping H gives the exact alternating `W^dagger,W` positive construction.
- Dropping R and establishing a P-odd registrable readout removes the all-real
  symmetry protection.
- Dropping D leaves the all-real strip as a lawful degenerate branch.
- A weaker-than-OS or non-OS reconstruction remains open.
- No new axiom is required for any of these paths. None is silently supplied
  by an approved primitive.

### N7 — steelman

The strongest objection is already constructive: the same generic complex
`W` that fails under a homogeneous `W,W` placement has a Hermitian positive
Gram under `W^dagger,W`. The framework does not choose between those time
patterns. In addition, the P-even record span is conditional on the orbit
clause. These facts defeat any universal claim that emergent time forces the
tie or even forces the two-branch homogeneous set. They do not defeat the
narrow theorem, which states exactly what happens after H, O, and R are fixed.

### N8 — cross-cycle echo

Block 9 previously left a full OS test open; this note closes one homogeneous
version while preserving its alternating escape. The two-slice Berezin note
already showed that changing the reflection prescription can change Gram
positivity. The history-index note leaves representation faithfulness open.
Those earlier patterns show why a failed construction must not be promoted to
a framework-wide impossibility; the present boundary is narrowed accordingly.

## Import and support inventory

- **Framework content:** the
  [`Record axiom`](MINIMAL_AXIOMS_2026-06-29.md) supplies readable permanent
  records and finite scalar additivity. It supplies none of H, O, R, S, or D.
- **Standard/source machinery:** the linked OS reflection, crossing, and
  transfer templates are used at their declared source scope and remain
  subject to independent audit.
- **Explicit modeling conditions:** time-homogeneity, the two-slice corner
  domain, the `C_3[111]` probe, and the spectral-readout identification.
- **Explicit normalization:** the `-1/2,+1/2` crossing convention.
- **Observational comparator:** three distinct registered values, with no
  numerical mass or threshold imported.
- **Open support condition:** the orbit clause making the record span P-even.
- **Not imported:** no PDG value, fitted selector, probability rule, physical
  equipartition law, or value of `r`.

## Reprove-and-cite ledger

Reproven by the runner are the exact Gaussian-rational Berezin engine, the toy
Gram, the field-level reflection, P-covariance, the fixed-set moment
separation, the one-mode tied positivity certificate, the full 5-by-5 tensor
factorization of the all-real strip, the exact counterexample and failure
witnesses, the alternating measure, the branch degeneracy, and the conditional
endpoint arithmetic.

Cited at declared grade are the source definitions of the OS reflection and
history index, the orbit-clause record scope, the complementary K-odd test,
the two-step transfer template, the reviewed block-9 boundary, and the Record
axiom.

## Verification

```bash
python3 scripts/frontier_records_only_os_reconstruction_2026_07_11.py
```

Expected: 24 `[PASS]` lines, declared-open residual lines,
`TOTAL: PASS=24 FAIL=0`, and the bounded verdict. Exit code is zero exactly
when `FAIL=0`.

Independent audit is required. This note asserts no effective-status change.
