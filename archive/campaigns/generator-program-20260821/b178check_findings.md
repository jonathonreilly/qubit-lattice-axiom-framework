# Block 178 adversarial check — B2b/B3

Scope: exact SymPy arithmetic using Block-170 `Bench`, imported `b166`, `fx.H_free`, `fx.quotient`, `fx.quotient_connection`, `dense`, and `r=Bench.r`; no worktree file was modified.  Hop class below means `(min(dt,-dt) mod T, min(dx,-dx) mod 4)` on quotient sites.

## C1 — zero shear, convention, and volume

For `H=dense(fx.quotient(fx.H_free))`, zero shear and unit volume give `H=I` and `rHr-H=0` entrywise at both `8x4` (`16x16`) and `12x4` (`24x24`).  Thus the corrected zero-shear control is reproduced.

For an antiunitary `Theta phi=r conjugate(phi)`, invariance of `bar(phi) Q phi` is `r Q r=Q^T`, not generally `r Q r=Q`.  On this transport-off zero-shear control `Q=mH` is real symmetric, so `Q^T=Q` and both tests vanish exactly.  The matrix `r` is the committed descended site involution (`r^2=1`); the error is omitting the transpose, not using the wrong descended permutation.

Non-flat symmetric-volume counterexample: set zero shear and `nu(t,x)=(1,2,3,4)_x` at every time.  Then `H` is diagonal, repeating `(25/16,3/2,17/8,17/6)` on every time level, and both `rHr-H` and `rHr-H^T` vanish at both extents.  Hence “mirror-symmetric sector = geometry-free sector” is false: reflection-symmetric volume geometry survives.

**C1 VERDICT: REFUTED AS A THEOREM.**  The zero-shear flat control is right; the stated covariance convention is incomplete, and non-flat reflection-symmetric geometry is an exact invariant counterexample.

## C2 — shear attribution

At unit volume and physical shear `sigma=3/5` everywhere (`a=25/16,b=-15/16`), `nnz(rHr-H)=(64,96)` at `8x4,12x4`; all nonzeros are `+-15/64`.  Pinning levels `t=0,1` to zero shear gives `(32,64)`, again only `+-15/64`, exactly the claimed free-level counts.

A single **b-modulus** level (`b_(0,x)=-15/16`, all other `b=0`, and `a=nu=mu=1`) contributes exactly 16 entries at either extent: four each in time blocks `(0,1),(1,0),(1,2),(2,1)`, values `+-15/64`.  This verifies localization of the shear-linear/off-diagonal piece.

But a physical single-level shear `sigma_(0,x)=3/5` also forces `a_(0,x)=25/16`.  Its exact defect has 24 entries, not 16: the same 16 off-diagonal `+-15/64` plus eight diagonal-block entries `+-9/64` in `(0,0)` and `(2,2)`.  Thus the ambient/pinned count is a symmetry/cancellation fact for those profiles, not a generic additive “each physical shear level contributes 16” law.

**C2 VERDICT: PARTLY CONFIRMED, BROAD ATTRIBUTION REFUTED.**

## C3 — transport

On the pinned constant-volume carrier (levels `0,1` zero; free levels at `3/5`), the `8x4` commutator test reproduces `nnz(rKr-K)=16` for `(sx,st)=(3/5,0)`, `64` for `(0,1/2)`, and `72` for `(3/5,1/2)`.  The `sx` defect is exactly hop classes `(1,0):8,(1,2):8`.

The complete `st` support is not those two classes: it is `(0,1):16,(1,0):32,(2,1):16`; the combined support adds `(1,2):8`, with eight overlapping `sx/st` slots.  Exact linearity holds matrixwise: `D_K(sx,st)=sx D_K(1,0)+st D_K(0,1)`.

At `12x4` the corresponding commutator counts are `32,96,112`, with `sx` classes `(1,0):16,(1,2):16`, `st` classes `(0,1):16,(1,0):48,(2,1):32`, and 16 overlapping slots.  So `16 -> 64/72` is an `8x4` support census, not an extent-independent scaling law.

Under the correct transpose test `rKr-K^T`, the pinned-carrier counts are `16,64,72` at `8x4` but `24,104,116` at `12x4`.  At flat zero shear, `K` is real antisymmetric: the `sx` commutator defect is zero although its transpose-condition defect has `16/24` entries.  Convention is load-bearing, even though every nonzero transport dial still fails the transpose test.

**C3 VERDICT: LINEARITY AND THE 8x4 COUNTS CONFIRMED; HOP-CLASS AND REPLICATION STORY REFUTED/INCOMPLETE.**

## C4 — the forced-fork inference and fork-independent observables

A bosonic quasi-free Hilbert grading needs more than a nonsymmetric quadratic matrix: a one-particle complex space `V`, an antilinear involution/conjugation, and a Hermitian positive-semidefinite reflected two-point form `G(u,v)`; Wick/permanent extension then defines the forms on `Sym^n V`, and particle number grades `direct_sum_n Sym^n V`.  For the fixed Gaussian, the raw candidate is the reflected covariance selection `G=[r(Q^-1)^T]`; theta invariance would make the covariance compatible with reflection, whereas its failure can leave this `G` non-Hermitian and therefore unusable as an OS Gram matrix.

That failure blocks a **canonical reflection-positive Hilbert reconstruction from these data**.  It does not force Hermitianization for *any* quasi-free grading: algebraic polynomial-degree grading still exists; a non-positive quasi-free functional can use the raw covariance; and a Hilbert construction could restrict/quotient, double fields, change complex structure/reflection, or add a separate positive two-point form.  Even if one insists on the fixed `r` and ordinary OS Hilbert form, what is forced is an extra prescription, not specifically `herm(.)`, and the prescription need not succeed.  Moreover C1 already refutes the antecedent “no theta-invariant measure with geometry” at volume-geometry scope.

Fork-independence lemma, exact scope: if the fork changes only a post-`Q` one-particle kernel while leaving `Q` fixed, then `Z(Q)=pi^N/det(Q)` and every function of `Q` alone are fork-independent.  Thus `|Z|^2=pi^(2N)/|det Q|^2` is indeed independent of the action/covariance Hermitianization fork and algebraically positive where `det Q` is nonzero; interpreting `Z` as the Gaussian integral additionally requires its convergence domain (here `herm(Q)>0`).

It is not unique.  Already `|Z|^p` for every `p>0` (or `(|Z|^2)^alpha`, `alpha>0`) is positive, fork-independent, and remains transport-sensitive whenever the power is strictly monotone and `|Z|` moves.  Positive functions of `Q^dagger Q`, normalized ratios of such weights, and the previously checked `1/det(herm Q)` on its PD domain provide a larger family.  Uniqueness would require an additional composition/Born/readout axiom absent here; it cannot follow from positivity plus sensitivity.

**C4 VERDICT: REFUTED.**  Non-invariance is an obstruction to canonical OS reconstruction, not a theorem forcing Hermitianization or uniquely selecting `|Z|^2`.

## C5 — independent B3 composition and the limit

The independent route in `b178check_probe.py` substitutes each record into raw cover `fx.H_free` first, then separately forms `dense(fx.quotient(H))` and `dense(fx.quotient_connection(d_holo,H))`, and takes exact `DomainMatrix.det`.  At records `{(2,0):1/5,(3,0):2/5}` and `(g_re,g_im)=(0,1/4)` it equals the landed `Site.Q_holo_t` route entry-for-entry.

For menu entry `a=0`, the independently recomputed `J_0(0,1/4)` is **exactly equal as a reduced Rational** to the 2,299-digit numerator over 2,302-digit denominator printed in `b178arm_findings.md` under “imaginary-quarter”: the equality test compares the integers, not a decimal.  It is positive and lies exactly in `(123118943/125000000000,196990309/200000000000)`.  The whole independent vector has signs `(+,+,-,-)` and `L1(J)` lies in `(1424446619/500000000000,2848893239/1000000000000)`.  Hence `J!=0` is reverified.

Along `(g_re,g_im)=lambda(1/3,1/4)`, the independent exact `L1` brackets are: `lambda=1/2`, `(181601231/125000000000,1452809849/1000000000000)`; `lambda=1/4`, `(739880333/1000000000000,369940167/500000000000)`; and the added `lambda=1/8`, `(366622121/1000000000000,183311061/500000000000)`.  These disjoint rational brackets prove the strict three-point chain `L1_1/8<L1_1/4<L1_1/2`.

The finite chain does not prove global monotonic contraction.  The limit is nevertheless rigorous: every determinant and normalized weight is rational in `lambda`; all finitely many determinant/normalization denominators are nonzero at `lambda=0`; therefore they remain nonzero in a neighborhood, `J(0)=0`, and continuity gives `lim_(lambda->0) J(lambda)=0` componentwise.  The three points are corroboration, not that proof.

**C5 VERDICT: CONFIRMED AT ITS SCOPED READOUT.**  `J!=0` proves that the chosen `|det Q|^-2` consistency defect responds to the holonomy dial; calling this “record-record interference” is an interpretation and does not establish C4 or uniqueness of the readout.

## Ten-line summary
1. C1: flat, zero-shear `rHr=H` is exact at `8x4` and `12x4`.
2. Antiunitary covariance is `rQr=Q^T`; it coincides with `rQr=Q` only on the real-symmetric control.
3. Non-flat volumes `(1,2,3,4)_x` give an exact reflection-invariant geometric counterexample.
4. C2: ambient/pinned shear counts `64/96` and `32/64` are reproduced.
5. A single `b` level localizes to 16 entries, but a physical shear level has 24 because `a` changes too.
6. C3: `8x4` transport counts `16/64/72` and exact dial linearity reproduce.
7. The full hop support and the `12x4` counts (`32/96/112`) refute the advertised generalization.
8. C4: non-invariance forces no particular Hermitianization, and `|Z|^2` belongs to a family of fork-independent positives.
9. C5: an independent raw-Hodge-before-quotient route exactly reproduces nonzero `J_0(0,1/4)`.
10. The added `lambda=1/8` contracts exactly; rational continuity, not three samples, proves `J->0`.
