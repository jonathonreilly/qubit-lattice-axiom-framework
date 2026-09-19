# lightcone-sixaxis-order, attempt 4 (worker w-macbookpro90c72-j7b47, model grok-4.6)

Own plan: one-site Peierls factor of `π∝∏_x Z_x` for six-axis light-cone formation, after locking reversibility of a symmetric stencil. a3 (same family, unrefeered) treated reversibility and two-site DB; this attempt is the single-spin cost of `π` and the local-max condition `p>q`.

Light-cone: record at `(t+1,x)` from `(t,x)` and/or `(t,x±e_j)`. Stationary `π(s)∝∏_x Z_x(s)`, `Z_x=∑_{u∈axes} ∏_{y∈N(x)} W(u,s_y)`, `W=p` same, `q` opposite, `r` orthogonal. `n=7` if the site is included, `n=6` if not.

## (1) The statement attempted

**Statement (PARTIAL).** For either stencil, flipping one spin of the fully `+z` configuration multiplies `π` by

```
ρ_n = [(p^{n-1} q + p q^{n-1} + 4 r^n) / (p^n + q^n + 4 r^n)]^n,    n=6 or 7.
```

The numerator–denominator gap is `(p-q)(p^{n-1}-q^{n-1})`, independent of `r`. Hence `ρ_n<1` iff `p>q` (`ρ_n=1` if `p=q`). The aligned configuration is a **strict local maximum** of `π` precisely when `p>q`. On the line `(p,1,2)` this holds for every `p>1`; at `(3,1,2)`, `ρ_7=281399112371155271/63844929217529296875<1`.

(a) Reversibility of a symmetric stencil is the bond-swap identity `∑_x s'_x·S_x(s)=∑_x s_x·S_x(s')` (CHECKED on a bond). Whether the site must be included: both `n=6` and `n=7` give a local max under the same `p>q`. (b) Not a full contour threshold. (c) Block 17’s `216m` is far above this local condition `p>q`. (d) Memory of an aligned start, for a reversible automaton, is at least that the aligned configuration is a local trap of `π`; convergence from a finite perturbation is not proved.

## (2) Steps

**Step 1 — swap identity (PROVED; CHECKED L1).** Undirected stencil: `∑_x s'_x ∑_{y∼x} s_y = ∑_{⟨xy⟩}(s'_x·s_y+s'_y·s_x)` equals the same with primes swapped.

**Step 2 — one-flip `Z` (PROVED; CHECKED L2, L3).** Aligned, every stencil is seven (six) copies of `+z`, so `Z=p^n+q^n+4r^n`. After flipping the origin to `-z`, each of the `n` sites whose stencil contains the origin sees a multiset of one `-z` and `n-1` copies of `+z`, hence `Z=p^{n-1}q + p q^{n-1}+4r^n`. Product of `n` such factors. Gap `(p-q)(p^{n-1}-q^{n-1})`.

**Step 3 — local max (PROVED).** `p^{n-1}-q^{n-1}` has the sign of `p-q`.

## (3) Where the route stops

A one-site cost is not a Peierls contour bound: a large droplet’s surface-to-volume for this many-body `log Z` is not computed. First missing step for (b): the ratio `π(cube of side L flipped)/π(aligned)` as `L→∞`, or a chessboard estimate for `π`.

## (4) What would finish it

An explicit surface tension `τ(p,1,2)>0` for `p≥p_0`, giving at least six Gibbs measures (the six axes) by Pirogov–Sinai / contour expansion, compared with block 17’s `216m` and the executed threshold.
