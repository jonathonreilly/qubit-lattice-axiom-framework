# Block 221 Entry Counterexample

Date: 2026-08-28

Status: exact executable handoff witness; not a retained theorem or broad
finality no-go.

## Result

The Block 220 single-event condition is load bearing. Running the unchanged
frozen table from two same-bit roots on the period-four parity component can
write a false permanent Record on a mixed input.

Use the four parity-component vertices in the runner's order and the mixed
word

```text
initial bits: [1,0,0,0]
roots: vertices 1 and 2
root directions: ordinal 0 at both roots
base-frame physical direction: +y (D6 column 3)
```

The initial state is

```text
(U_1, R_(0,+y), R_(0,+y), U_0).
```

One enabled five-step trace is

```text
0 root_launch_match             center 1 port 0 target 3
1 head_skip_root_cross_edge     center 3 port 3 target 2
2 head_skip_root_cross_edge     center 3 port 0 target 1
3 head_skip_root_cross_edge     center 3 port 1 target 2
4 head_return_root_commit       center 3 port 2 target 1
```

It reaches

```text
(U_1, LOCK_0, R_(0,+y), L_0).
```

Thus a permanent `LOCK_0` appears while the opposite transient `U_1` remains
untouched. The trace is a false coverage certificate, not merely a liveness
failure.

An exhaustive breadth-first census of every mixed L4 word, unordered pair of
root sites and four directions per root gives:

```text
same-bit two-root starts:             576
same-bit starts with a reachable Record: 96
opposite-bit two-root starts:         768
opposite-bit starts with a reachable Record: 0
largest explored reachable set:       51 states
maximum shortest false-Record trace:   5 actions
```

Because every starting word in this census is mixed, each of the 96 reachable
Records is false. The immediate wall is therefore same-bit coverage ownership,
not opposite-bit safety on this smallest component.

## Cause

In the one-root theorem, a noninverse H-to-R encounter is safely interpreted
as another edge into the unique known root and skipped. With two roots, the
same local pattern may instead be an edge into an unresolved foreign tree.
Skipping it counts that obstacle as if its entire region had already closed.
The surviving head can then return to its own root and commit without covering
the component.

The local pair does not reveal whether the encountered same-bit `R` belongs
to the actor's ancestry. Root bit and direction alone therefore do not close
multi-root ownership.

## Exact carrier opportunity and boundary

The unused global residual per complement parity is
`E+5T_other`. It contains neither another ordinary
`D6=A1+E+T_axis` nor another twisted
`D6 tensor A2=A2+E+T_other`. A one-site repair therefore cannot simply add a
new independent directional zipper orbit.

There is one narrower live seam. Block 220 activates only the four tangent
directions of each already embedded P/H/R orbit for a supplied normal. The
two physical directions `+n,-n` in each of P, H and R already exist in the
40-ray carrier but lie inside Block 220's context complement. Reclaiming them
gives 12 phase-marker modes per normal and changes the named/projector
partition from `34+94` to `46+82`. Direct reconstruction gives maximum Gram,
projector and cubic-transport residuals below `4.2e-14`.

Those modes do not by themselves prove a zipper. They are viable only if a
frozen microgrammar time-multiplexes existing roles, freezes every affected
root before commit, preserves the collision dart, and restores or erases all
borrowed states before reuse. The first state-alias, ABA reuse, missing-dart
or fair-MEC counterexample is the gate to a higher-block/oriented-edge memory
route.

## Block 221 gate

Any autonomous repair must replace skip-as-coverage at unresolved same-bit
tree contacts with one of two physically represented outcomes:

1. a proof-carrying ancestry zipper that establishes common ancestry or
   safely merges distinct trees before either root can commit; or
2. ownership-aware rollback that erases the colliding trees before reuse.

The repair may not import a root identifier, coordinate, torus size, global
visited set, fresh epoch or hidden scheduler memory. It must reject this exact
trace, all proper-cubic/complement transports, the period-four parallel-dart
variants, and any rotated action order. It must also exclude a branch-closed
fair nonterminal maximal end component.

This witness narrows the next campaign; it does not exclude higher-block,
oriented-edge, stochastic, coherent or continuous-time arbitration routes and
does not justify an axiom amendment.
