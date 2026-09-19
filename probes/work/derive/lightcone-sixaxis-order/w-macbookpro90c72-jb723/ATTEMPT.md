# lightcone-sixaxis-order, attempt 1 (worker w-macbookpro90c72-jb723, model grok-4.6)

Own plan: write `π`’s interaction explicitly and decide whether it is the static six-axis pair Hamiltonian (so block 17’s chessboard would apply). a3/a4 treated reversibility and one-flip costs; this attempt is the many-body character of `log Z`.

## (1) The statement attempted

**Statement (PARTIAL).** For light-cone six-axis formation, `Z_x=∑_{u∈{±e_j}} ∏_{y∈N(x)} W(u,s_y)` with `W∈{p,q,r}`. Thus `π(s)∝∏_x Z_x` is a **7-body** (site included) or **6-body** (not) Gibbs weight, not a pair interaction. Pairwise-ness would force the 7-stencil cross-ratio

```
Z(s_A,s_B) Z(+,+) / [Z(s_A,+) Z(+,s_B)] ≡ 1
```

for the two opposite stencil sites `A,B` with the rest aligned. It is not identically 1: for `(s_A,s_B)=(-z,-z)` the ratio is
`(p^7+q^7+4r^7)(p^5 q^2+p^2 q^5+4r^7)/(p^6 q+p q^6+4r^7)^2`.
Therefore block 17’s pair-matrix chessboard / bond-plane RP for `W` does **not** transfer to `π`. A contour argument must be done on `log Z`, not on `W`. (a) Reversibility still only needs a symmetric stencil. (b) No Peierls threshold is proved here. (c) Comparison to `216m` is blocked until that contour is written. (d) Stationary laws of a reversible automaton are the Gibbs measures of this many-body `π`; “memory of the initial plane” is convergence to one of them, not a non-equilibrium droplet.

## (2) Steps

**Step 1 — explicit `Z` (PROVED; CHECKED I2).** Definition of the formation normalizer.

**Step 2 — cross-ratio (PROVED; CHECKED I1).** If `log Z=∑_{pairs} f`, the cross-ratio is 1. Direct expansion of the 7-fold product for the four configurations `(±z,±z)` and `(+z,+x)` gives the displayed rational functions, not 1.

**Step 3 — no-go for transferring T2–T4 (PROVED).** T2 of block 17 is RP of the pair matrix `W`. `π` is not `exp(∑_{⟨xy⟩} log W(s_x,s_y))`.

## (3) First failure of a pair-Gibbs route

Step 3. First missing step for (b): a Peierls estimate using the one-flip factor of a4 together with a surface expansion of `∏_{x∈∂Λ} Z_x / Z_x^{aligned}`.

## (4) What would finish it

That surface expansion, giving a threshold on `(p,1,2)`, compared with `216m` and the executed ordering.
