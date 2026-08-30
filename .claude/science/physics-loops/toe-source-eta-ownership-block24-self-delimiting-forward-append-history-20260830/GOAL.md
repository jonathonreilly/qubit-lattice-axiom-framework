# Block24 goal: one self-delimiting append rule and finite Record histories

## Exact target

Starting from the Block22 fourteen-effect six-qubit POVM/radial writer and the
Block23 Record-controlled state family, construct one finite fixed-anchor
instrument whose nontrivial input condition is only

```text
current block = Locked(f,b),
forward block at x+9f = exact radial Blank.
```

The instrument must preserve the complete current Record, prepare the forward
live state `rho_b` with `Ready_f`, apply the Block22 writer, and return one of
fourteen new complete Records `Locked(f,b')`. It must give the exact conditional
probability

```text
T(b'|b) = Tr(E_b' rho_b)
```

from its physical Kraus factors, not by assigning a target table.

The same translated rule must self-disable at the old block after success,
because its forward block is then Locked rather than Blank. On an isolated
straight Blank ray it must leave exactly one eligible tip and support an
inductive family of all finite Record cylinders

```text
Pr_f(b1,...,bn | rho)
  = Tr(rho E_b1) product_{j=1}^{n-1} T(b_{j+1}|b_j).
```

Every earlier Record must remain permanent and classically QND. Summing the
last outcome must return the preceding cylinder, and the statement must remain
valid after tensoring the initial live state with an arbitrary reference.

## Physical append factors

Let `C^x_(f,b)` be the complete 26-pointer Locked projector at the current
32-site block and let `B_(x+9f)` be the full 32-factor radial Blank projector.
For each next label `c`, the forward-block factor is the literal composition

```text
Blank -> rho_b tensor Ready_f -> post-writer live tensor Locked(f,c).
```

It must be represented by the explicit Block22 square root of `E_c`, the six
prepared live factors, and all 26 pointer maps. Its adjoint product must be

```text
T(c|b) B_(x+9f).
```

Define separate branches `L_(f,b,c)` with identity on the current live factor
and on the other five possible forward blocks. The valid-domain effect and
STOP branch are

```text
P_valid = sum_(f,b) C^x_(f,b) tensor B_(x+9f),
K_STOP = I - P_valid.
```

Orthogonal Record controls must prove `P_valid^2=P_valid` and exact CPTP
completion. No coherent sum across front or outcome branches is allowed.

## Geometry and recurrence obligations

- `S` is the exact 32-site Block22 support.
- At a fixed anchor, `S+x` and the six `S+x+9f` blocks are pairwise disjoint:
  the common covariant carrier has 224 sites and radius 13.
- A realized append touches only the current and selected forward blocks: 64
  sites. A three-event realized chain has three blocks and 96 sites.
- For fixed `f`, centers `x+9jf` are all distinct, and translated supports are
  pairwise disjoint because the maximum within-block axial coordinate span is
  eight while adjacent centers are separated by nine.
- In a finite chain, every non-tip Record sees a non-Blank forward block and
  STOPs; only the newest Record sees the supplied next Blank block.
- The arbitrary-length claim is a projectively consistent family of every
  finite cylinder. It is not an assertion that an infinite tensor-product
  state, formation time, or physical completion event has been supplied.

## Required exact checks

1. imported effects sum coefficientwise to identity;
2. all explicit square roots reconstruct their effects;
3. all 196 `T` entries are branch-derived, positive, and stochastic;
4. all 1,176 append branches have factor-derived effects;
5. `P_valid` is an orthogonal projector and STOP completes a global channel;
6. every complete old classical Record projector is QND;
7. separate branch maps transform covariantly under all 24 proper cubic
   rotations and translations;
8. successful reapplication at the same anchor has zero append eligibility;
9. the exact three-event composition contains 16,464 branches and yields
   `E_b1 T(b2|b1) T(b3|b2)`;
10. symbolic arbitrary-reference normalization holds;
11. the finite-history induction and prefix consistency are proved from the
    physical one-step certificate plus stochasticity, not from a copied
    transition table; and
12. hostile altered models actually fail their named invariant.

## Success terminal

The strongest permitted positive terminal is:

```text
EXACT-COVARIANT-SELF-DELIMITING-ONE-BLANK-RECORD-APPEND-INSTRUMENT-
WITH-PROJECTIVELY-CONSISTENT-ARBITRARY-FINITE-STRAIGHT-RAY-CYLINDERS
```

It remains a bounded candidate law because `rho_b`, the range-nine compound
block instrument, the selected seed, and each finite prefix's next Blank block
are construction data rather than content uniquely forced by the four axioms.

## Explicit exclusions

This block does not claim fresh-substrate generation, a vacuum-selection law,
multiple-tip collision arbitration, arbitrary turns, a global scheduler,
formation rate, physical time, an action/current/source join, gravity, a
nearest-neighbor compiler for the compound writer, Born-rule uniqueness, an
axiom amendment, an audit verdict, obligation retirement, or TOE-score
movement.

If the route fails, the failure is restricted to the displayed append
instrument and quantified domain. The predecessor-aware five-Blank guarded
channel and other collision/resource laws remain live unless separately
tested.
