# lightcone-formation, attempt 1 (worker w-macbookpro90c72-j5bbf, model grok-4.6)

Independent of grok a2 (FSS/LRO), a5 (sphere Dobrushin `β<3/7`), a6 (`{E,14-E}`).

## (1) The statement attempted

**(a)** The 7-stencil PCA is reversible w.r.t. `π∝∏_x Z(S_x)` by pairing (CHECKED). `π` is Gibbs for a 7-site star potential `∑_x log Z(β|S_x|)`, not the static nearest-neighbour `β s·s'`. Reflection positivity of this star potential is not proved (ASSUMED open; block 19's RP for the comparator does not transfer).

**(c)** Linear kernel `C=7σ²/(2E(1-E/14))` satisfies `7σ²/(2E) ≤ C ≤ 49σ²/(2E)` because `0<E≤12` implies `1-E/14∈[1/7,1)`. CHECKED on every L=4 mode.

**(d)** Six-axis 7-pred Dobrushin at `(p,q,r)=(3,1,2)`: one-slot TV `c=270/989`, `7c=1890/989>1`. This bound does **not** prove uniqueness at campaign weights. (Sphere linearised threshold `3/7` is a different menu.)

**(e)** Block 19's IR `1/(βE)` is for the static bond law. Here the linear formation kernel is `1/E` times `7/(2(1-E/14))`; the nonlinear `π` has a different potential, so Gaussian domination / RP must be re-done.

## (2) Steps

**Step 1 — linear identity and envelope (PROVED; CHECKED as E1).**

**Step 2 — pairing (PROVED; CHECKED as E2).**

**Step 3 — six-axis Dobrushin (CHECKED as E3).** Exhaustive one-slot flips of a 7-tuple.

**Step 4 — potentials differ (PROVED).**

## (3) First failing step

Naive `7c<1` uniqueness at `(3,1,2)` fails (`7c>1`). RP/LRO for `π` not obtained.

## (4) What would finish it

RP through a bond plane for `log Z(β|S|)`; IR bound as in a2; a Dobrushin constant using averaged environments (as uniqueness-region-up).
