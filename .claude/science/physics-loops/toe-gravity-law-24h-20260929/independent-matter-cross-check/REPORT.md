# Independent reconstruction of the walker CC repair and mixed-GC obstruction

The finite CC repair and the stated mixed-GC obstruction both check within the declared canonical, regular, scalar-smearing completion class. I independently reconstructed the actual averaged energy and symmetric bond current, then contracted every one of the 82,332 supplied coupling coefficients in real space. The contraction equals the full independently constructed defect. The coefficient `−i/4` in the next GC equation survives all allowed gravity cross terms at the tested field and lapse order. No mathematical error was found in these scoped claims.

The sign distinction is essential: the successful CC construction uses `J=−P^B` with the positive spatial-Lie orientation of the gravity seed. The literal real canonical branch `J=+P^B`, obtained if the source's displayed shift coupling is read that way, fails even the first CC jet for positive `K/alpha`. They must remain separate branches. Neither branch supplies a full matter-plus-gravity gauge action merely from the source's prescribed-current conservation identities.

This is a focused independent calculation, not a formal review/audit PASS. The frozen author report is `independent-matter-cross-route/REPORT.md`, SHA256 `e0535076030c83f451c25a2bbab81076763b798a5d782d7676912a61e0c9f8e1`; the checked `coupling_KA.json` has SHA256 `9bc29d9f43e5d83993922ec83402b9f6237c956689ce00e56bf14d9dd28a900e`. Later changes need new coverage. No author implementation was imported or executed.

## Source and canonical reconstruction

The source definitions are those of block136 at main `e75578f7136401d4bd750131671aed9212c06291`, with the fixed gravity convention in the campaign contract. The relevant source text, previous seed convention, block139 mass definition, block106 periodic-momentum result, and exact-boost T1–T2 were read at their actual stated scope. Source identities and read limits are recorded in `SOURCE_BINDINGS.json`. The actual minimal axioms/registry and registered primitives had already been read in this campaign; they do not supply these amplitudes, dynamics, canonical pairing, or generator identification. No unmerged PR result or prior negative theorem is used as a load-bearing shortcut.

Use `(T_j psi)(x)=psi(x+e_j)`, `S_j=(T_j−T_j⁻¹)/(2i)`, `C_j=(T_j+T_j⁻¹)/2`, and the literal two-component walk `H=Σ sigma_j S_j`. Its energy density is `Re psi_x†(H psi)_x`, subsequently averaged over the eight body-diagonal neighbors. Smearing and self-adjointness of that average give exactly

\[
E_N=\tfrac12\{f_N,H\},\qquad f_N=C_1C_2C_3N.
\]

The actual current is `P^B=(P''+Q)/2`, with

`P''_j=((1+T_j)/2) prod_(l!=j) C_l Re(psi† P_j psi)`, `P_j=S_j C_j`,

and `Q=C1 C2 C3 Q^b`, where the two literal terms of `Q^b_j` are the real parts of `psi_(x+e_j)† sigma_j(H psi)_x` and `(H psi)_(x+e_j)† sigma_j psi_x`, with the source's common factor `1/2`. I retained both terms and their adjoints. The independent code builds actual `2×2` matrix entries on integer position pairs, rather than a Pauli-symbol composition formula.

Summing each density gives `E_1=H` and `P^B_j[1]=P_j I` exactly. Analytically the latter follows from `sum Q_j=(1/2){sigma_j C_j,H}=S_j C_j`, while the averaging of `P''` preserves its total. The position implementation verifies the same identities from its entries. It produces 192 energy matrix entries for `N=delta_0`.

Writing `psi=(q+ip)/sqrt(2)` with `{q,p}=1` gives `{psi,psi*}=−i`. Therefore

\[
\{\psi^*A\psi,\psi^*B\psi\}=-i\psi^*[A,B]\psi,
\qquad \delta\psi=-iJ\psi.
\]

Since `P_j~−i partial_j` at long wavelength, the positive spatial-Lie smooth action `delta psi=+xi_j partial_j psi` requires `J[constant xi]=−xi_jP_j`, hence the chosen finite-lattice extension `J=−P^B`. Its exact action is `delta psi=+i B[xi]psi`; it is not an exact continuum Lie derivative at arbitrary lattice momentum. The source's displayed `−N.P^B` action term, if interpreted literally with this real canonical shift convention, instead produces a Hamiltonian constraint containing `+N.P^B`. The report correctly does not silently equate that branch with the positive-Lie branch.

## Why the CC curvature-ideal construction is valid

At flat gravity and degree two in the walker amplitude, independent canonical differentiation gives

\[
\{C[N],C[M]\}^{(\psi^2)}
=-i[E_N,E_M]-K\sum_A(r_{N,A}A_{M,A}-r_{M,A}A_{N,A}).
\]

Thus the displayed target `G[F0]` requires its equation (5). A frame-response term `h psi†V psi` cannot contribute: the flat gravity kinetic gradient is zero. The only relevant term in `C` is the explicitly allowed `P psi†A psi`. This is a degree statement, not an assertion that all other couplings are unimportant at later orders.

The fixed lapse bracket is `F0_j=lambda(N_x M_(x+e_j)−M_x N_(x+e_j))`, with `lambda=K/(4alpha)`. At `lambda=1`, define lapse Laurent variables `x,y` and the walker ket variable `z`. The curvature derivatives are

\[
r_{ii}(x)=\sum_{j\ne i}(2-x_j-x_j^{-1}),\qquad
r_{ij}(x)=2(1-x_i)(1-x_j).
\]

Let `m_x=(x1−1,x2−1,x3−1)`. These six polynomials generate exactly `m_x²`: the three combinations `(r_jj+r_kk−r_ii)/2` are `d_i=2−x_i−x_i⁻¹`, with `(x_i−1)²=−x_i d_i`, while the mixed products are `r_ij/2`. Conversely every displayed curvature polynomial is in `m_x²`. The Laurent units and the invertible factor two make this an equality of ideals, not just a leading-order resemblance.

The pair ideal is `m_x²+m_y²`. Its quotient retains only the 16 Taylor slots `1`, `x_i−1`, `y_j−1`, `(x_i−1)(y_j−1)`, with full Laurent dependence on `z`. The independently rebuilt defect has zero coefficient in every one of these slots. This is an exact operator-coefficient test for all walker momenta; no low-momentum approximation in the walker is used.

There is also an analytic check of the potentially nontrivial mixed slots. Write `H_i=partial_i H`. The mixed physical lapse derivative of the energy commutator is `−i[H_i,H_j]/4`. For `i!=j` this equals `epsilon_(ij ell) cos k_i cos k_j sigma_ell/2`. Direct expansion of the actual current gives the vector part `partial_(Q_j) B_i(0;k)=−i epsilon_(ij ell) cos k_i cos k_j sigma_ell/4`. The two terms from differentiating `(x−y)B(xy;k)` give the same mixed coefficient. The diagonal mixed derivative vanishes by antisymmetry. The single-lapse first jets cancel because `{sigma_j C_j,H}/2=P_j` and `J=−P^B`.

Finite ideal membership gives a finite coupling, without a singular inverse: for every integer `n`, `(x^n−1)/(x−1)` is a finite signed Laurent sum. Repeated ordered telescoping removes the constant/first Taylor jet in `x`, then in `y`, leaving products in the two curvature ideals. If `D=Σ r_t(x)f_t+Σ r_t(y)g_t` and `D(y,x,z)=−D(x,y,z)`, then `KA_t=[f_t(x,y,z)−g_t(y,x,z)]/2` has precisely the required antisymmetrized contraction. This establishes existence independently of the provided coefficient list. It does not establish a minimal radius.

## Complete independent check of the polynomial witness

For `N=delta_0,M=delta_m`, I construct `−i[E_N,E_M]` by multiplying the literal position matrices and summing all possible intermediate spin/position indices. `F0` is nonzero only for `m=±e_j`: it equals a positive unit bond at zero for `m=e_j` and a negative unit bond at `−e_j` for `m=−e_j`. This supplies the current contribution directly from the real-space `P^B` densities.

The result has **15,168** matrix entries on **188** nonzero relative lapse displacements. The nonadjacent witness `m=2e1`, spin-up row `(-1,-1,-1)`, column `(1,-1,-1)`, is `i/1024`. No periodic torus or numerical Fourier sampling is involved.

I then read the coupling as data only. A monomial `x^a y^b z^c` has, relative to its gravity-momentum base, lapse position `l=b−a`, bra position `r=−a`, and ket position `s=c−a`. For a curvature coefficient `r_t(v)` at displacement `v`, the first contraction contributes at

`(M position,row,column)=(l−v,r−v,s−v)`,

and the antisymmetrized contraction contributes with the opposite sign at

`(v−l,r−l,s−l)`.

This literal delta-lapse contraction of all **82,332** `KA` coefficients equals the independently constructed defect entry by entry. Computation uses exact Gaussian integers after multiplying by the common denominator **49,152**. It does not reuse the author's Laurent multiplication, division, or symmetry code. A separate serialization comparison confirms that `defect.json` itself represents the same independently calculated position matrix.

The complete supplied coupling also satisfies:

- Hermiticity for real lapse, checked by exchanging actual bra/ket endpoints and conjugating coefficients;
- odd spin time reversal of `A`, so `P.A` is even with gravity momentum odd;
- all 24 proper cubic rotations, including the shift of the integer anchor when a staggered face is rotated to a negatively oriented face;
- physical Chebyshev radius four from both lapse and gravity-momentum anchors for each diagonal component, `7/2` for each shear component, and the same componentwise maximum coordinate diameters.

There is no anti-alias assumption to verify: the implementation uses unrestricted integer coordinates. Translation covariance and the finite support make this a complete infinite-lattice coefficient check. The listed coefficients are `KA`; the actual `A` is obtained by division by the fixed nonzero `K`.

The literal `J=+P^B` branch was reconstructed separately. Its first-jet remainder is nonzero: 72 entries in my unexpanded `2×2` Taylor-matrix representation, or exactly the author's **84** nonzero terms after conversion to its expanded Pauli/Laurent representation. The serialized opposite-sign remainder matches as well. More simply, its single first lapse moment requires `lambda=−1`; the positive-Lie branch requires `lambda=1`. Curvature terms start at second lapse order and cannot change that condition. With positive `K,alpha`, the literal plus branch therefore has no CC repair of this form.

## Mixed GC: independent affine-position proof and all cross terms

Allow every regular finite-range higher gravity coefficient in both constraints, with the fixed linear gravity seeds, fixed flat quadratic matter data, and matter beginning at `U(1)`-invariant degree two. In particular write the possible relevant terms as

`C=Cg+E+h.V+P.A+...`, `G=Gg+J+h.B+P.D+...`,

where the four displayed coefficients are arbitrary quadratic matter functionals with the appropriate smearing. Set gravity fields to zero, take constant shift `xi=e_j`, and retain matter degree two.

The whole contribution of the allowed gravity cross terms at this order can be listed:

1. The fixed `G1=P.Rxi` has zero differential because `Rxi=0`. Its bracket with `h.V` is zero; it also cannot pair with `P.A`.
2. `P.D` in `G` can pair with `C1=−K R1`, giving `+K r_N.D`. Every component of `r_N` is a second difference and has zero zeroth and first lapse moments.
3. `h.B` can pair with the quadratic gravity kinetic term only through a gradient proportional to gravity momentum, which is zero here. Higher pure-gravity terms have zero relevant first derivative at the flat point.
4. Pairing two gravity-linear matter terms gives matter degree four. Matter brackets involving gravity-dependent terms vanish at flat gravity, and higher pure-matter terms cannot contribute at degree two.

Thus no term was discarded merely because the particular constructed `A` happens not to help. The entire allowed class has zero contribution at the first lapse moment. The independent code checks the six curvature stencils' zeroth and all three first moments exactly.

The remaining affine calculation has a particularly direct position proof. Constant shift gives `J=−P_j`. The body-diagonal energy average preserves affine functions, so `E_(x_j)=(X_j H+H X_j)/2`. Since `[P_j,H]=0` and `[P_j,X_j]=−i C2_j`, with `C2_j=(T_j²+T_j⁻²)/2`,

\[
\{J[e_j],E_{x_j}\}=i[P_j,E_{x_j}]=C2_j H.
\]

I also calculate this commutator from its literal row-zero position kernels, independently of a differentiated Fourier expression. It has 24 nonzero matrix entries for each axis, and agrees exactly with `C2_j H`.

For a scalar translation-covariant lapse structure, `U0(e_j,1)=mu0` and `U0(e_j,x_j)=mu0 x_j+c_j`. The uniform-lapse equation forces `mu0=0`, because `[P_j,H]=0` and `H` is nonzero. The affine equation would consequently require

\[
C2_j H=c_j H.
\]

The coefficient of `sigma_j z_j³` on the left is `1/2 · 1/(2i)=−i/4`. It is zero on the right for every scalar `c_j`. The literal position calculation extracts **`−i/4` for all three axes**. No continuum normalization of `c_j` was needed.

The affine/constant probes are legitimate on finitely supported walker profiles. For any fixed finite-support candidate, they can instead be compact plateaux containing the entire differentiated support; the seed derivatives then vanish before any boundary is reached. The proof does not assume an affine coordinate on a periodic torus or a normalized plane wave. Because the closure claim is strong and off shell, arbitrary compact profiles are admissible; restricting to constraint-satisfying matter states would change the target.

Regular field-dependent scalar structure corrections cannot alter this degree: at flat gravity they multiply a vanishing linear gravity constraint or first enter matter degree four. Unrestricted operator/tensor-valued smearings, extra constraint species, or different flat generator data are not covered. A gradient-only shift target also differs from the declared arbitrary-shift target.

## Mass, prior art and limits

The analytic staggered-mass extension is consistent with the actual block139 definition. Let `epsilon_x=(−1)^(x1+x2+x3)`, `A_f={f,H}/2`, and `E_f(m)=A_f+m epsilon f`. Then

`[A_f,epsilon g]+[epsilon f,A_g]=epsilon({f,A_g}−{A_f,g})=0`

for commuting real multiplication operators `f,g`; the `m²` commutator also vanishes. Directly in the current density, its two additional mass terms cancel because `epsilon_(x+e_j)=−epsilon_x`. Thus the CC defect and current are unchanged for every real mass. For GC the two-step momentum commutes with the staggered mass and still has derivative `C2_j`, so the coefficient above remains in `C2_j H_m`. This argument retains the fixed staggered background; it does not assert one-site translation symmetry for a fixed nonzero mass. I reconstructed this algebra, but did not independently rerun the author's mass-product enumeration or the source's eight-site-term classification.

The `cos(2k_j)` multiplier is already in the actual landed block106 and exact-boost T2. The additional scoped result checked here is that every allowed flat gravity cross term vanishes at its first lapse moment, so the multiplier obstructs this specified scalar-smearing canonical lift. It is not a new periodic-band theorem or an application of the older walker-only CC obstruction. Indeed, the full CC witness demonstrates a repair of that older restricted defect.

The common canonical action containing the checked `P.A` term is a well-defined finite-range supplied action. Its existence does not make its constraints first class, identify its stress physically, or prove a gauge symmetry. The successful CC construction and failed GC identity should both be retained. GG and higher-order closure were not solved. Other current/generator identifications, mixed symplectic structures, additional carriers, nonlocal singular couplings, operator-valued smearings, weak closure and infrared-only sectors remain outside this check.

## Execution and evidence

The full independent pass was priced below one minute and 300 MB: sparse position contractions and coefficient lookups, with no quotient reconstruction or dense solve. Actual runtime was **30.649 seconds**, peak RSS **143,065,088 bytes**, with threads capped at one. The additional exact serialization/Taylor-basis comparison took **0.938 seconds**. Deadline and stop-sentinel checks were active. No heavy source runner, unmanaged worker, Git/GitHub mutation or other agent's file edit occurred.

Reproduce from this directory with `python3 check_matter.py` and `python3 check_normal_remainder.py`, retaining the declared thread caps. `results.json`, `results.txt`, `normal_results.json`, `normal_results.txt`, `SOURCE_BINDINGS.json`, and `MANIFEST.json` bind the actual calculations and coverage. Finite samples are not being promoted to a universal result: the CC computation exhausts finite coefficients, while the GC statement follows from the explicit degree, moment and three-step proofs above.
