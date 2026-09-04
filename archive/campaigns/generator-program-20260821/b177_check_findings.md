# Block 177 adversarial check — scalar-sector theorem

Scope: B2 sketch and B2 SOLVE COMPLETE were read in full. Arithmetic below is
symbolic/integer/rational; no float controls a decision. The worktree was not modified.

## C1 — complex Wick scope: CONDITIONAL, with a fatal object mismatch

Let `z_i` be holomorphic generators and let `Theta` be antilinear. With
`G_ij = omega((Theta z_i) z_j)`, left coefficients are conjugated by `Theta`.
For Wick-ordered quadratics, proper/quasi-free Wick contraction gives exactly
`G2_(ij),(kl) = G_ik G_jl + G_il G_jk`.
No extra entrywise conjugate occurs: it is already in the left sesquilinearity.
Indeed Hermiticity follows from `conj(G_ik)=G_ki`. If the opposite storage
convention is used, the displayed matrix is transposed/conjugated as a whole;
that has the same inertia and does not rescue positivity.

Thus the real example was inadequate evidence, but the abstract complex
permanent formula is correct. What is not established is its use with this
`G1`: imported H1-170b defines the Gaussian covariance as `Q^-1`, whereas
`Bench.form = herm([r Q]_{S,S})` is built from the action `Q`. Under H1-170b's
index order, Wick instead sees `[r(Q^-1)^T]_{S,S}`. Its raw matrix is not even
Hermitian on these fixtures; Hermitianizing it still does not give the action form.
Exact check: at `(8x4,st=0)` the Hermitianized covariance/action `(0,0)`
difference is `-35233/38760`, and the difference persists at both extents/dials.
If Hermitianization is imposed anyway, its exact `st=1/4` inertias are
`(6,2,0)` and `(4,4,0)`, so symmetric-power indefiniteness survives; but its
`st=0` inertias are the same, not the solve's PSD region result.
So the committed `oplus Sym^n(Bench.form)` identification is an added premise,
not a consequence of the stated Gaussian measure. **C1 verdict: REFUTED as an
unconditional committed-sector theorem; valid only for a separately declared
quasi-free functional whose reflected two-point kernel is `Bench.form`.**

## C2 — symmetric-power lemma: CORRECTED, sign survives

Put `p=<u,u>`, `q=<v,v>`, `r=<u,v>` for a Hermitian form. Direct permutation
counting on `{u^n,u^(n-1)v}` gives
`A=n! p^n`, `B=n! p^(n-1) r`, and
`D=(n-1)![p^(n-1)q+(n-1)p^(n-2)|r|^2]`.
Hence `det = n!(n-1)! p^(2n-2)(pq-|r|^2)`.
The solve's `r^2` is only the real-symmetric specialization; complex scope
requires `|r|^2 = r conj(r)`. For `p>0>q`, the determinant is strictly negative.
Changing from raw monomials to divided/orthonormal symmetric tensors is an
invertible positive diagonal congruence, multiplying this determinant by a
positive factor; its sign and the inherited mixed inertia are unchanged.
**C2 verdict: CONFIRMED-WITH-CORRECTION, and it proves conditional
indefiniteness for every `n>=2` once the correct one-particle kernel is named.**

## C3 — four inertias and Jacobi: CONFIRMED

I eliminated each exact Hermitian matrix by rational congruence/Schur complements,
independently of the imported Descartes helper. In `(n+,n-,n0)` order:
`8x4,st=1/4 -> (5,3,0)`; `12x4,st=1/4 -> (4,4,0)`;
`8x4,st=0 -> (4,0,4)`; `12x4,st=0 -> (4,0,4)`.
At `st=0` the first four pivots are positive and the exact remaining Schur
complement is `0_4`, establishing the four null directions rather than inferring them.

For `12x4,st=1/4`, the eight leading minors are, in order:
`57/40, 3249/1600, 185193/64000, 10556001/2560000,`
`-601692057/6553600000, 34296447249/16777216000000,`
`-1954897493193/42949672960000000,`
`111429157112001/109951162777600000000`.
All are nonzero; their signs are `+ + + + - + - +`. Including `Delta_0=1`,
there are exactly four changes, so the solve's Jacobi application is valid.
The `8x4` exact leading-minor signs are `+ + + + - - + -`, giving three changes.
**C3 verdict: CONFIRMED exactly; the extent asymmetry is real on these fixtures.**

## C4 — witnesses: CONFIRMED-WITH-PROVENANCE-CORRECTION

At `12x4,st=1/4`, the matrix is exactly
`[[57/40 I4, (57/320)diag(1,-1,1,-1)],[same,0_4]]`.
Thus `u=e0` gives `u^dag G u=57/40`. The solve record supplies no components
for its “rationalized eigendirection”, so its quoted value is not reproducible
as a claim about that unnamed vector. It is algebraically attainable: taking
`v*=e0-(85628045/21082587)e4` gives exactly
`v*^dag G v*=-24656243/1124404640` by direct rational multiplication.
A much cleaner independent witness is `v=e0-5e4`, for which
`v^dag G v=-57/160<0`. (At `8x4`, the recorded `e4-e5` gives `-65/512`.)
**C4 verdict: the positive/negative witness claim is CONFIRMED; the particular
large fraction lacks a specified-vector certificate in the solve record.**

## C5 — theorem wording and vacuum dial: REFUTED AS WORDED

The all-`n` permanent formula is a proof for a *stipulated* proper quasi-free
functional with one-particle kernel `G1`: `Gn=perm(G1)` and C2 applies for every
`n`. It is not a proof that the committed Gaussian has `G1=Bench.form`.
Accordingly the honest result is: “conditional all-`n` symmetric-power theorem;
the committed Wick-sector identification remains an explicit premise.” The
solve's real `n=2` example does not verify even `n=2` for the committed kernel.

The vacuum sensitivity itself is exact. Symbolically `det Q=c P(st)^4`; at
8x4, `P(0)=66447280221259` and `P'(0)=-13079847592350`, while at 12x4,
`P(0)=1993466346364384822133` and `P'(0)=-744781636638830596050`.
Thus `|det Q|^2` has nonzero derivative at zero at both extents. In the imported
machinery `H=herm(Q)` and the region pin are `st`-free, `Q` is affine in `st`,
and only `st` changes between the two carriers: this is a fair *temporal*
transport dial, not a full connection-off dial because `sx=3/5` remains.
The clean full-phase dial is `Q_tau=H+tau A`, `A=Q-H`, with geometry/pin fixed.

“Born readout is the unique positive-with-transport window” is only true inside
the additionally stipulated direct sum `oplus Sym^n(Bench.form)`. It is not a
uniqueness theorem over readouts: `Z conj(Z)` is proportional to
`1/|det Q|^2` (not `|det Q|^2`), and positivity plus sensitivity alone does not
select it over other positive functions. **C5 verdict: restrict to conditional
sector uniqueness; withdraw the unconditional Born-selection claim.**

## Ten-line summary
1. C1: complex antilinear Wick contraction does give the permanent; conjugations do not spoil it.
2. C1: the solve nevertheless uses action form `rQ`, while its Gaussian supplies covariance `Q^-1`.
3. The committed Wick/Fock identification is therefore a premise, not a derived theorem.
4. C2: replace `r^2` by `|r|^2`; the determinant remains strictly negative for `p>0>q`.
5. Tensor normalization is a positive congruence and cannot change that sign.
6. C3: exact inertias are `(5,3,0)/(4,4,0)` on and `(4,0,4)/(4,0,4)` at `st=0`.
7. All 12x4 on-dial leading minors are nonzero; Jacobi's four-change count is valid.
8. C4: `57/40` reproduces; a clean negative witness gives `-57/160`; the named vector was omitted.
9. C5: `st` cleanly dials temporal anti-Hermitian transport, but `Q_tau=H+tau A` is cleaner globally.
10. Final verdict: conditional symmetric-power theorem survives; unconditional Born uniqueness does not.
