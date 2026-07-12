# DM Leptogenesis Exact-Kernel Source-Package Identifiability Boundary

**Date:** 2026-04-15 (source-package boundary sharpened 2026-07-12)
**Claim type:** no_go
**Actual current-surface status:** no-go source proposal; independent audit
lane owns any effective status.
**Script:**
[`scripts/frontier_dm_leptogenesis_exact_kernel_closure.py`](../scripts/frontier_dm_leptogenesis_exact_kernel_closure.py)

## Claim

The current minimal framework axiom surface does **not** determine a unique
nonzero tuple

```text
(gamma, E1, E2, K00)
  = (1/2, sqrt(8/3), sqrt(8)/3, 2),
```

and, when the note's downstream benchmark data are independently held fixed,
does not determine the formal value
`epsilon_1 / epsilon_DI = 0.9276209209...`.

This is a narrow identifiability result about derivation from the current
axiom surface alone.  It is not a no-go against the exact finite-dimensional
matrix identities, the coherent leptogenesis kernel, or a future theorem that
supplies a normalized source/action and physical-observable bridge.

The formerly quoted numbers remain a consistent **conditional completion**.
On that completion, the corrected benchmark arithmetic remains

```text
epsilon_1 / epsilon_DI = 0.9276209209...,
eta / eta_obs          = 0.5578749661...,
```

and the earlier percent-level eta closure remains withdrawn.

## Minimal premise set

The only load-bearing authority is the current
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) surface:

1. Lattice;
2. Qubit;
3. Admissibility; and
4. Record, including content-determined finite scalar readout additivity.

The same authority explicitly leaves readout-context selection,
log-determinant readout, source/action, and physical-observable identification
outside the axiom content.  No observed target, fitted selector, literature value,
benchmark constant, or unregistered primitive is used in the no-go proof.

## Exact restricted-packet algebra

Write the Hermitian source carrier as

```text
H = [[A,       b+rho,        b-rho-i gamma],
     [b+rho,   c+delta,      d            ],
     [b-rho+i gamma, d,      c-delta      ]].
```

The packet extracts

```text
E1  = delta + rho,
E2  = A + b - c - d,
K00 = <u,H u>,                 u=(1,1,1)/sqrt(3),
cp1 = -2 gamma E1 / 3,
cp2 =  2 gamma E2 / 3.
```

These are exact algebraic definitions once `H` is supplied.  They do not
select `H` from the four axioms.

## Two-completion theorem

Let

```text
e1 = sqrt(8/3),              e2 = sqrt(8)/3,
A  = 2 + 4 sqrt(2)/9,        b = 0,
c  = 2 - sqrt(2)/9,          d = -sqrt(2)/9,
delta = 1/2,                 rho = e1 - 1/2,
gamma = 1/2.
```

The resulting exact Hermitian matrix `H_ref` satisfies

```text
(gamma,E1,E2,K00) = (1/2,e1,e2,2).
```

It also lies in the positive-polar carrier domain `H=Y Y^dag`.  Its exact
leading principal minors are

```text
D1 = 2 + 4 sqrt(2)/9,
D2 = 643/324 + 2 sqrt(6)/3 + 8 sqrt(2)/9,
D3 = -3361/648 - 16 sqrt(3)/27 + 227 sqrt(2)/108 + 8 sqrt(6)/3.
```

The first two are manifestly positive.  The elementary rational bounds
`sqrt(2)>7/5`, `sqrt(6)>12/5`, and `sqrt(3)<7/4` give
`D3 > 2021/648 > 0`.  Sylvester's criterion therefore proves `H_ref>0`,
so a full-rank `Y` with `H_ref=Y Y^dag` exists.

Now take any positive `lambda != 1` and define

```text
H_lambda = lambda H_ref.
```

For every existing model of the current minimal axioms, because `H`, a
source/action map, and a physical-observable bridge do not occur in the axiom
language, that model has downstream expansions by either `H_ref` or `H_lambda` without
changing the common minimal-axiom reduct.  Both added carriers lie in the
positive-polar domain, both obey every extraction formula above, and positive
scaling preserves the source-oriented sign.  But linearity gives

```text
(gamma,E1,E2,K00)_lambda
  = lambda (gamma,E1,E2,K00)_ref,

(cp1,cp2)_lambda
  = lambda^2 (cp1,cp2)_ref.
```

At a fixed downstream benchmark, the coherent source term is

```text
epsilon_1
  = |C (cp1 f23 + cp2 f3) / K00|,
```

so

```text
epsilon_1(H_lambda) = lambda epsilon_1(H_ref),
```

for positive `lambda`.  Holding the Davidson--Ibarra comparator fixed gives
the same scaling for `epsilon_1 / epsilon_DI`.  For example, `lambda=2`
doubles the conditional ratio at the same independently held benchmark while
leaving the minimal-axiom reduct unchanged.  This is a fixed-benchmark formal
non-invariance result; it is not a claim that all other quantities in a fully
coupled phenomenological completion remain fixed.

Therefore neither the four absolute package values nor the quoted kernel
ratio is a semantic consequence of the current minimal axioms.

## Why Record additivity does not select the reference completion

For any content-determined finitely additive scalar record readout `I`, the
map

```text
I_lambda(R) = lambda I(R)
```

is also content-determined, obeys `I_lambda(empty)=0`, and is finitely
additive on pairwise-disjoint record collections.  Thus Record additivity
does not fix an absolute readout normalization.  More importantly, the
minimal axiom memo supplies no map at all from the downstream carrier `H` to
record content.  A log-determinant or isospectral-response construction can
be used only after that source/readout context and its normalization have
been supplied or derived.

## What survives exactly

The decisive Parts 1--4 of the runner verify symbolically, without importing
`dm_leptogenesis_exact_common.exact_package()`, that:

1. `H_ref` reproduces the conditional reference tuple;
2. `H_lambda` remains positive definite for every positive `lambda` and obeys
   the same extraction identities;
3. all four package coordinates vary linearly with `lambda`;
4. the CP channels vary quadratically and the coherent kernel varies
   linearly; and
5. finite Record additivity is invariant under readout rescaling.

Part 5 imports the existing conditional package solely to check its tuple
against the independently extracted witness (class B) and replay the old
`epsilon_1/epsilon_DI` and `eta/eta_obs` arithmetic (class D).  No Part-5
value is used in the no-go proof.

Consequently the durable exact content is the family of extraction and
kernel identities **given a supplied normalized carrier**, not the selection
of one numerical member from the current axioms.

## Claim boundary and import-retirement path

This theorem rules out only the following route:

> derive the nonzero numerical package and kernel ratio from the current
> minimal axioms plus the restricted packet's carrier identities, without a
> normalized carrier/tuple-selection theorem or a scale-invariant kernel
> bypass.

It leaves several distinct retirement routes open:

1. **Tuple selection:** a normalized source/carrier construction can select
   `H_ref` (or the same extracted tuple) directly, without first deriving a
   record-readout map.
2. **Physical kernel interpretation:** a source/action plus physical-observable
   bridge can attach the selected carrier to the coherent kernel.
3. **Bypass:** a scale-invariant kernel theorem could remove the carrier
   normalization from the physical ratio without selecting every absolute
   package coordinate separately.

The no-go does not assert that all three routes must be completed together.
Only tuple selection, with a scale-invariant theorem as a bypass, belongs to
the narrow wall.  Physical-observable interpretation belongs solely to a later
physical-kernel claim.

The conditional benchmark arithmetic is not promoted by this note.  The
independent audit lane must decide the claim type and effective status after
landing.

## Verification

```bash
python3 scripts/frontier_dm_leptogenesis_exact_kernel_closure.py
```

Expected result:

```text
SUMMARY: PASS=20 FAIL=0
CLASS BREAKDOWN: class A: 15, class B: 3, class D: 2
```
