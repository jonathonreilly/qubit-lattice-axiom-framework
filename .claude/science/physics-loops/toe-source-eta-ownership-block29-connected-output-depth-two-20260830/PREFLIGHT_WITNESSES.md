# Block29 preflight witnesses

## Connected geometry

For each first exit `g`, the Block28 output center is `Y+9g`.  The decoded
front of its Locked word is exactly `g`, so Block24 derives the next selected
Blank at `Y+18g` without an external site label.

The two-current/eight-first-Blank carrier and eight possible selected future
Blank blocks give `18` state-controlled blocks.  Including every identity-only
factor in each six-block Block24 candidate star gives the full literal carrier:

```text
18 state-controlled block centers
34 full-carrier block centers
34 pairwise-disjoint 32-site supports
1,088 represented qubit sites
8 selected future Blank candidates
16 additional future spectator-only centers
```

The eight selected future candidates are disjoint from all ten first-layer
blocks and from each other.

## Cylinder algebra

For a pair prefix `(g,h,c_L,c_R)` and future outcomes `(d_L,d_R)`, the exact
Gram coefficient is

```text
q_lambda(g,h)
* T(c_L | source_L) * T(c_R | source_R)
* T(d_L | c_L) * T(d_R | c_R).
```

Both future transition rows sum to one.  Marginalizing `(d_L,d_R)` therefore
recovers the exact Block28 prefix coefficient.  Marginalizing one complete arm
also recovers the matching uniform singleton cylinder because both `q` tables
have one-arm marginals `1/4`.

## Record and resource counts

One arm has `4 * 14^2 = 784` injective two-step Record histories.  Disjoint
left/right supports give `784^2 = 614,656` pair configurations without a
monolithic enumeration.

On the valid first-pair history, two first-layer targets become Locked and six
remain Blank.  The future debit is `0/1/1/2` in sectors
`D_00/D_10/D_01/D_11`.  In `D_11`, exactly four supplied Blanks have therefore
been debited in total; the two old current Records and two first-layer Records
remain QND, and twelve controlled candidate Blanks remain unused.

These are preregistered targets, not executed results.
