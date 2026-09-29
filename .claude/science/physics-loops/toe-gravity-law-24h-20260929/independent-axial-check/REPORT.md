# Independent axial calculation, radius one

Checked 2026-09-29 against science revision `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. This is a focused mathematical check, not a formal audit, landing review, source-review PASS, premise adoption, or physical gravity result.

**Result:** the original axial CC degree-two plus GC/GG degree-one system is correctly assembled and consistent: rank 306, nullity 195, with 501 unknown coefficients. Adding the GC degree-two, momentum-quadratic equations gives a verified contradiction for the explicitly **momentum-linear spatial-generator** class. A compact proof is below. It does not exclude a cubic-momentum term in G3, additional constraint mixing, larger support, another canonical realization, or matter branches.

## Frozen inputs and coverage

The initially dispatched `nonlinear-evidence/axial_cc.py` has SHA256
`427e83efa1d55c836465c61c672e0cf4c0814420a59fc64430e2b80e6aae9528`.
Its exact starting bytes are preserved as `axial_cc_start.py`. I read the complete script, `NONLINEAR_CONTRACT.md`, and `INDEPENDENT_SEED_CHECK.md`; runner output was not used as proof. I then independently derived and implemented the equations. The frozen author's assembly was imported only at the final comparison step. This is derivation/implementation independence, not blind source review.

The coordinator subsequently requested the separate GC kinetic extension. Its frozen inputs are:

| File in `nonlinear-evidence/` | SHA256 |
| --- | --- |
| `axial_mixed_kinetic.py` | `8d7d288bc5aa66a381c6d9aecd734f2612ca4be4723cf27e1749bac98a24692f` |
| `axial_r1_mixed_kinetic_system.json` | `0e71538830876e21615224ece17a0003b874e111012860b2187531fb291ed8b1` |
| `axial_r1_mixed_kinetic_rational.json` | `6f089488f2b9519d74f62a7b60b98bdc622311911adc5e67758831ba217111e6` |

All three have corresponding `*_start` copies here. Every matrix coefficient and right-hand side in the radius-one kinetic payload was independently reconstructed before the supplied dual witness was read. The extension's optional symmetry mode was read but not executed or independently certified. Radius-two and later extensions are outside this report.

Read complete pinned science sources: blocks112,62,101; current `MINIMAL_AXIOMS_2026-06-29.md`; complete `docs/audit/data/axiom_premise_nodes.json`; and the kinetic-isotropy, scale-reference, and realized-state primitive source notes. Their hashes and the independent artifacts are recorded in `MANIFEST.json`. The four axioms and registered primitives do not supply this phase space, Hamiltonian, spatial generator, pure hypersurface target, or continuum comparison. In particular, the named kinetic-form isotropy does not establish this carrier's K=4alpha. These remain supplied mathematical conditions.

Changed bytes or added equation families require changed-scope coverage before this check is reused broadly. The later author's claimed results are not incorporated by reference.

## Direct derivations

Let A=h_xx, B=h_yy, C=h_zz and P,Q,R their independent canonical momenta. Use `{h_i(x),P_j(y)}=delta_ij delta_xy`, alpha=1, K=4, and Delta f_x=f_(x+1)-2f_x+f_(x-1).

Block101's positive spatial action term gives the negative Hamiltonian potential. Consequently

`C1[N]=4 sum_x N_x Delta(B+C)_x`,

`T2[N]=sum_x N_x [(P²+Q²+R²)/8-(PQ+PR+QR)/4]`,

`G1[X]=2 sum_x X_x(P_x-P_(x+1))`.

Here X_x is located at x+1/2. The six-coordinate pairing has diagonal matrix momenta P_jj and off-diagonal matrix momenta P_ij/2. No off-diagonal factor enters this diagonal restriction.

At first field order, `dC1[N]/dB=dC1[N]/dC=4 Delta N`, and `dT2/dQ+dT2/dR=-P/2`. Therefore

`{C1[N],T2[M]}+{T2[N],C1[M]}=2 sum P(N Delta M-M Delta N)=G1[F0]`,

`F0_x=N_x M_(x+1)-M_x N_(x+1)`.

This confirms the nonlinear contract's corrected sign. The displayed bond field in pinned block112 has the opposite orientation when paired with this standard Hamiltonian convention. Negating both constraints cannot repair a bilinear bracket sign.

For p=(p,0,0), the exact block62 quadratic curvature reduces to `R2=(p²/2)BC`; hence `V2[1]=-2 sum(D+B)(D+C)`. This uses the specified staggered symbol, not a guessed continuum density.

For the cubic kinetic normalization, differentiate at e=0 the actual diagonal expression

`[sum_i (1+e h_i)² P_i² - (sum_i(1+e h_i)P_i)²/2] / [4 sqrt(prod_i(1+e h_i))]`.

The coefficient is

`T3_cont = [2 sum h_i P_i² - (sum P_i)(sum h_i P_i) - (sum h_i)/2 * (sum P_i²-(sum P_i)²/2)]/4`.

The independently differentiated full 18-term polynomial is printed in `results.txt`; it matches every prescribed coefficient. Its construction did not use the author's `continuum_t3()`.

The positive Lie action gives

`G[X]=integral [P(X A'+2(1+A)X')+Q X B'+R X C']`.

Integrating by parts puts its quadratic density at the shift anchor:

`G2_cont=-P A'-2A P'+Q B'+R C'`.

For a lattice coefficient c^(ij)_(ab) multiplying `X_x h_i(x+a)P_j(x+b)`, a,b in {0,1}, the zeroth moment is zero. The h and P first moments are weighted by a-1/2 and b-1/2. Their targets are respectively diag(-1,1,1) and diag(-2,0,0). This independently confirms all G2 moment equations. The inverse metric is `g^xx=1-A+O(h²)`, so the F1 coefficient sums are -1 for A and 0 for B,C.

The continuum signs of the other kernels are `U0(X,N)=X N'` and `V0(X,Y)=X Y'-Y X'`. Accordingly U0's zeroth moment is 0, N first moment 1, X first moment 0; V0's antisymmetric first moment is 1. The shift offsets relative to a vertex anchor are xp+1/2, explaining the half-integer weights.

Degree counting with a canonical bracket lowering total field degree by two gives the exact required linear equations

`CC2: {C1,T3}+{T3,C1}+{V2,T2}+{T2,V2}=G2[F0]+G1[F1]`,

`GC1: {G1,V2}+{G2,C1}=C1[U0]`,

`GG1: {G1[X],G2[Y]}+{G2[X],G1[Y]}=G1[V0(X,Y)]`.

`{G1,T2}=0`, since both are independent of h. If G3 is restricted to hhP, the P² part at the next mixed order is

`GC2_P2: {G1,T3}+{G2,T2}=T2[U0]`.

Neither `{G3(hhP),C1}` nor `C1[U1(h)]` has a P² part. In contrast, `{G3(P³),C1}` does have one. Time reversal by itself allows P³ in G3. Thus the original phrase describing all time-reversal polynomial terms was insufficient without an explicit momentum-linearity condition; the coordinator identified and is separately exploring this escape. The contradiction here does not cover it.

## Why the discarded 3D components do not repair these equations

Take fields and smearings independent of y,z, diagonal h and P, and a shift only in x. Form brackets first, then restrict. The derivatives of C1 with respect to shear fields vanish: its mixed difference contains a transverse difference of the lapse. Its A derivative also vanishes; only B,C derivatives remain. G1[X_x] has derivative only with respect to P_A, since every transverse difference of X_x vanishes. T2's shear-momentum derivatives are proportional to the discarded shear momenta and vanish at the restriction.

Every bracket checked here has one of these three fixed generators as a factor. Thus an unknown term's omitted-coordinate derivative cannot multiply a surviving fixed-generator derivative. Unknown terms with an undifferentiated omitted field vanish as well. On the right, F0 has only an x component and G1 is evaluated with diagonal momenta. Transverse differences of field-dependent kernels also vanish on x-dependent data. Transverse displacements of surviving diagonal fields merely combine coefficients already freely represented in the axial basis.

This establishes necessity of these projected equations for the declared 3D class; it does not establish a 3D lift or cover brackets between two nonlinear unknown generators at higher orders. It remains true for GC2_P2 under the stated momentum-linear G hypothesis.

## Independent local-identity check and rank

`check.py` builds complete functionals on an 11-site periodic chain. It differentiates those sums at each explicit canonical site and multiplies the resulting derivatives to form the Poisson bracket. It does not align conjugate factors by relative translation as the author's infinite-lattice routine does. After the bracket, monomials are anchored at their unique N variable (or X for GG) and only then compared to the author's local coefficient table.

For radius one, every residual monomial in the checked CC, GC, GG and mixed-kinetic equations has integer slot-position diameter at most 3. For example a C1 derivative shifts its lapse at most one site from a T3 momentum slot; the other T3 slots are within one site of their density anchor. The largest separation is therefore 3. G1 differentiation shifts X at most one site from an h slot, giving the same bound. The other substitutions have diameter at most 2.

The explicit labels N,M or X,N or X,Y identify a unique translation anchor. Relative separations lie in [-3,3]; L=11>2*3 makes their reduction modulo L injective. Each monomial's translation orbit has exactly 11 elements because its anchor variable occurs once. Dividing the summed orbit coefficient by 11 is therefore exact, including wrapped stencils. This gives a local coefficient lift, not a sampled finite-torus test. Uniform potential normalization is independently compared as an exact finite-support translation quotient; smooth moments are exact rational equations.

All 501 original columns and all right-hand sides agree exactly, including zero entries. Independent Fraction elimination gives rank 306 / nullity 195. A particular solution and all 195 independent kernel vectors are substituted into all 702 nonzero equations; every residual is zero. Free coordinates form the identity submatrix, so the kernel vectors are independent. `independent_solution.json` preserves this affine certificate. Runtime was 7.43 seconds. The primary author's elimination routine was not called.

`check_kinetic.py` independently adds all GC2_P2 columns with the same explicit torus gradients. Every entry and right-hand side agrees with the frozen kinetic payload. The supplied 14-row dual witness, when applied to these independently obtained equations, cancels all 501 unknown coefficients and gives right-hand side -1. Runtime was 2.97 seconds. The full rows and combined contributions are printed in `kinetic_results.txt`.

## Compact radius-one contradiction

Let `t^I_(a,b,c)` denote the T3 coefficient of `A_(x+a) P_(x+b) P_I(x+c)`, I=B,C, and write `t=t^B+t^C`. Let `c_ab` denote the G2 coefficient of `A_(x+a)P_(x+b)` for a,b in {0,1}.

Four CC2 coefficients give, for a=0,1,

`-4 t_(a,1,-1)=0`,

`8 t_(a,1,-1)-4 t_(a,1,0)=0`.

Four further CC2 coefficients give, for a=-1,0,

`4 t_(a,-1,1)=0`,

`4 t_(a,-1,0)-8 t_(a,-1,1)=0`.

Consequently all eight displayed t values vanish. These coefficients are identifiable by the N,M,h,P monomial labels in `kinetic_results.txt`; no other unknown family contributes to them at this support.

Adding the two GC2_P2 coefficients of `N_0 X_0 P_1 Q_0` and `N_0 X_0 P_1 R_0` gives

`-2 t_(0,1,0)+2 t_(1,1,0)-c_01/2=0`, hence `c_01=0`.

Likewise the sum for `N_0 X_(-1) P_(-1) Q_0` and `N_0 X_(-1) P_(-1) R_0` gives

`-2 t_(-1,-1,0)+2 t_(0,-1,0)-c_10/2=0`, hence `c_10=0`.

But the two longitudinal continuum moment equations are

`(-c00-c01+c10+c11)/2=-1`,

`(-c00+c01-c10+c11)/2=-2`.

Subtracting them demands `c01-c10=-1`, contradicting `c01=c10=0`. This independently explains the 14-row certificate. It uses no V2 normalization, cubic kinetic continuum normalization, F1, U0, GC1, GG1, or cubic-symmetry reduction. The extra momentum-linear G hypothesis and the fixed T2/C1/G1, support, and pure target form remain essential boundaries.

## Remaining limits

The radius means physical lattice units: distance<=R, equivalently doubled-coordinate distance<=2R. The initial phrase combining doubled coordinates and physical distance was potentially ambiguous; the coordinator clarified this interpretation. At R=1 the density supports x-1,x,x+1 and the edge supports x,x+1 used here follow that meaning.

No radius-two matrix, P³-expanded generator, constraint-mixed extension, h² GC/GG equation, substituted structure-function Jacobi relation, nonlinear 3D lift, source coupling, or record formation has been independently checked in this report. No universal finite-range impossibility, continuum impossibility, or framework-axiom consequence follows. The singular trace branch is outside the nonsingular DeWitt inversion. No source, root runner/state, Git index, commit, push, or GitHub object was mutated by this check.

Executed commands from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/check.py > .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/results.txt 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/check_kinetic.py > .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/kinetic_results.txt 2>&1
```

Both exited 0. Campaign deadline and stop sentinel were checked before work and during assembly/elimination. All computations were local, single-threaded, short-lived processes; no external compute, unmanaged worker, or heavy job was launched.
