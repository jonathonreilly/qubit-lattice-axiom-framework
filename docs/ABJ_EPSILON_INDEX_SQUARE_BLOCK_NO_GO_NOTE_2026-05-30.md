# ABJ Epsilon-Index Square-Block No-Go

**Date:** 2026-05-30
**Status:** exact route-pruning no-go on the standard staggered
`epsilon`-index residual; not a retained 3+1 closure theorem.
**Primary runner:**
[`scripts/frontier_abj_epsilon_index_square_block_no_go.py`](../scripts/frontier_abj_epsilon_index_square_block_no_go.py)
**Generated output:**
[`outputs/abj_epsilon_index_square_block_no_go_2026-05-30.json`](../outputs/abj_epsilon_index_square_block_no_go_2026-05-30.json)

## Target

The late-May ABJ bridge work narrowed the old bare admission in the parent
`docs/ANOMALY_FORCES_TIME_THEOREM.md` route to a smaller residual:

```text
(P1') Exhibit a framework-internal background of nontrivial topology
      (chi != 0) or nonzero gauge topological charge Q != 0 on which the
      staggered chiral index

          A_t[U] = Tr(epsilon exp(-t D[U]^dag D[U]))

      is non-zero.
```

This note checks whether that residual can be closed on the same finite
even periodic `Z^4` staggered surface used by the current Fujikawa/Jacobian
support notes, using the site-parity grading `epsilon(x)`.

## Theorem

On any finite even periodic hypercubic `Z^4` torus with equal
`epsilon = +1` and `epsilon = -1` sublattices, the standard massless
nearest-neighbor staggered Dirac operator coupled to arbitrary unitary link
phases has block form

```text
D[U] = [[0, B], [-B^dag, 0]]
```

after ordering sites by `epsilon` parity.  The block `B` is square.  Therefore

```text
D[U]^dag D[U] = diag(B B^dag, B^dag B),
```

and `B B^dag` and `B^dag B` have the same spectrum including zero
multiplicity. Hence, for every `t > 0`,

```text
A_t[U]
  = Tr(exp(-t B B^dag)) - Tr(exp(-t B^dag B))
  = 0.
```

So the same-surface residual `(P1')`, if interpreted as the standard
staggered `epsilon` index on finite even periodic `Z^4` tori, cannot be
witnessed by any U(1) background on that surface.

## Proof

The massless staggered operator only hops between opposite site parity.  The
site-parity grading satisfies

```text
epsilon D[U] epsilon = -D[U].
```

Gauge links change phases on nearest-neighbor hops but do not change the
bipartite support pattern.  Anti-Hermiticity of the staggered difference
operator gives the lower block as `-B^dag`.

Because the torus has equal even and odd site counts, `B` is square.  The two
positive operators `B B^dag` and `B^dag B` have identical non-zero singular
value spectra.  Since `B` is square, their zero multiplicities also agree.
Thus the heat-kernel traces in the `epsilon=+1` and `epsilon=-1` sectors are
identical, and their signed difference is zero for all `t`.

The argument is algebraic.  It does not depend on whether the U(1) phases are
free, random, constant-flux-style, or otherwise chosen, provided the operator
remains the standard nearest-neighbor staggered operator on an equal-sublattice
finite even periodic torus.

## Runner Evidence

The paired runner checks:

- `Z_4 x Z_2^3` with random U(1) phases;
- `Z_4 x Z_2^3` with a constant-flux-style U(1) background;
- `Z_4^4` with random U(1) phases;
- `Z_4^4` with a constant-flux-style U(1) background.

For each background it verifies:

- equal `epsilon` sublattice sizes;
- anti-Hermiticity of `D`;
- `epsilon D epsilon = -D`;
- vanishing diagonal parity blocks;
- lower block equals `-B^dag`;
- matching spectra of `B B^dag` and `B^dag B`, including zero modes;
- `A_t[U] = 0` at `t in {0.1, 0.5, 1.0, 2.0}`.

It also includes a rectangular synthetic control showing that a non-zero
signed heat trace appears once sublattice balance is removed.  That control is
not a framework background; it only demonstrates the exact algebraic escape
hatch.

Runner result:

```text
TOTAL: PASS=45 FAIL=0
```

## What This Prunes

This no-go prunes the following route:

```text
standard finite even-torus staggered epsilon index
  + arbitrary U(1) link phases
  -> non-zero A_t[U]
  -> retire the ABJ residual (P1')
```

The route fails because the square bipartite block form forces
`A_t[U] = 0`.

## What This Does Not Prune

This note does **not** rule out:

- the continuum ABJ theorem;
- accepting ABJ anomaly-to-inconsistency as a named physics premise;
- a taste-singlet staggered `gamma_5` or Adams-style staggered index;
- an overlap/Ginsparg-Wilson index operator;
- a genuinely imbalanced or curved cell complex with `chi != 0`;
- a non-abelian cohomology derivation of the anomaly;
- the already-derived algebraic statement that anomaly cancellation plus
  chirality parity forces `d_t` odd;
- the single-clock codimension-1 theorem excluding `d_t > 1` once the anomaly
  premise is available.

## Consequence For The 3+1 Lane

The 3+1 spacetime lane is not closed by this note.  Instead, the lane's
positive route is now sharper:

1. derive ABJ anomaly-to-inconsistency directly as a framework theorem by a
   route that does not rely on the standard `epsilon` index on equal finite
   tori;
2. use a framework-native taste-singlet/Adams/overlap index operator and prove
   it is an allowed physical chiral measure;
3. move to a non-flat or imbalanced lattice complex where the signed heat trace
   can be non-zero; or
4. keep ABJ as an explicit accepted physics premise and leave the 3+1 theorem
   bounded on that premise.

The first three are positive-retention routes.  The fourth is a bounded
claim-boundary route.
