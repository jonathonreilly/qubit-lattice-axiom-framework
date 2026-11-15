# Bottom second curvature for the normalized stationary tree

**Author argument; fresh independent review pending.** The new result below
is a source-specific proof of CJ18, conditional on the precise named
linear/current inputs CJ11–CJ17 of the frozen
[charged stationary-jet unit](CHARGED_STATIONARY_JET_ASTRA.md). It supplies
the missing bottom curvature estimate and therefore that unit's conditional
full-colour fourth-jet bound. It does not estimate a general all-depth
hidden inverse. It does not prove jet convergence, a complete finite-part
increment, a nonlinear complex neighborhood, four-dimensional continuum
existence, or a positive physical continuum Hamiltonian gap. Both final
physical targets remain OPEN.

The new [independent upstream review](REVIEW_CHARGED_STATIONARY_JET_ASTRA.md),
read after the first completed new controls, confirms CJ11–CJ17 and the
CJ18-to-quartic implication within their stated normalized-tree and named
linear contracts. It does **not** review the new CJ18 proof here. The
source hash remains `85b91738993f09f7e40a49f4c957c164a684bf499185629a82775229f6437254`;
the upstream review hash is
`f7e02d766c8885dceeeac8d2264784cdc65b85a771ae556efa5935d45236836d`.

Claim certificate: `actual_current_surface_status: bounded-support`;
`target_claim_type: bounded_theorem`; `trace_class: upstream_support`;
`reachability_to_target: partially_closes`; `bare_retained_allowed: false`;
`audit_required_before_effective_retained: true`. This is a source-side
certificate, not an audit assignment. No prior frozen artifact is edited.

## 1. Exact input contract and target

Use CJ1's **u-stripped normalized tree phase**, d=4, SU(N), odd fixed L>=3,
ell=L^n, top torus side T>=3, and kappas in a fixed compact positive
interval. Each level uses its own integrated unit links and counting
inner products. The root in a block is `LX+(L-1)/2`; the paired S4′ average
uses the same coordinate permutation at both endpoints and the exact
factor `(24 L^4)^-1`. The finite-u spread Hessian is a separate object.

The first-order chain is the **one** admissible localized representative
of CJ9–CJ11, not independent gauges for different external legs. Write
`a=a_0`, `f=d_2 a`, `r_j=a_(j+1)-Q_j a_j`, and write `B_p(a)` and `B_j(a_j)`
for the actual homogeneous degree-two ordered BCH coefficients CJ3.
The stationary second coefficient has top zero and satisfies CJ7–CJ8 on
the rooted hidden gauge complement. Its log-coordinate soft current is

    q_j=kappa_j(w2_(j+1)-Q_j w2_j-B_j(a_j)).                    (BC1)

The exact bottom source identity CJ19 is

    Psi=d_2 w2_0+B_p(a),
    d_2* Psi = S := Q_root,0* q_0-DB_p[a]* f
                                      +kappa_0 DB_0[a]* r_0,
    d_3 Psi = R := d_3 B_p(a),
    harmonic(Psi)=harmonic(B_p(a)).                            (BC2)

In particular the endpoint funnel is inside `Q_root,0* q_0`. It is not
replaced by a straight adjoint in BC2. CJ14–CJ17 already transport the
current with the covariant-conservation and funnel sources retained.

The following are the exact upstream estimates used here. Their constants
and one positive exponential rate eta0 are independent of n,T and the
allowed kappa sequence; rates may be shrunk by fixed amounts. All are
coefficientwise absolute bounds, including colours and link directions.

| Input | Pointwise amplitude in top-distance units | Provenance/status |
|---|---:|---|
| `a_j` | `C L^-(n-j)` | CJ11; source-only upstream review confirms its stated contract |
| `d_2 a_0` | `C ell^-2` | US8–US11, with their repaired unprimed strip |
| `r_j` | `C L^-3(n-j-1)` | US8–US11, FC19, exact own-unit convention |
| `q_j` | `C L^-3(n-j-1)` | CJ13–CJ17; source-only upstream review confirms its stated contract |
| Rooted stationary germ at each fixed n | analytic, with no uniform-radius claim | CJ7–CJ8 plus finite-dimensional positivity on the rooted complement |

The pointwise bounds carry a factor `E_eta0,T(output-x)` for each external
input x, where `E_eta,T(z)=sum_(m in Z^4) exp(-eta |z+Tm|_1)`. For q and
the other quadratic fields there are two such factors. Thus, after one
fixed rate loss, their Bloch coefficient functions are bounded and
holomorphic in **both** independent input momenta. This is stronger than
a bound on real factorized test vectors. The old all-Cartan quartic and
the fixed-depth volume-first determinant cancellation are not used as
substitutes for any row in this table.

The target is `g=d_2 w2_0`, with a fixed eta>0 independent of depth:

    |K_g(b;x,y)| <= C ell^-2
              E_eta,T(b/ell-x) E_eta,T(b/ell-y).                (BC3)

Here b is a fine plaquette base point; finite orientation offsets are
absorbed into C. A polarized convention or the st coefficient changes
only a fixed factor two. The theorem below uses the polarized convention;
the numerical program labels its st convention explicitly.

## 2. The actual sources have amplitude ell^-3

The three terms of S must all be kept. CJ17 gives
`q_0=O(L^3 ell^-3)`. The finite-range counting adjoint of the fixed-L
paired root map has norm depending on L alone, so
`Q_root,0* q_0=O(ell^-3)`. The plaquette derivative is a local bilinear
commutator: `DB_p[a]*f=O(ell^-1 ell^-2)=O(ell^-3)`.
The soft derivative is also the derivative of a fixed finite path average,
so `kappa_0 DB_0[a]*r_0=O(ell^-1 L^3 ell^-3)=O(ell^-4)`.
These are coefficient bounds on the common input-momentum tube, not just
estimates after summing signed contributions.

For R, a naive derivative estimate on B would lose a power. The needed
improvement is an actual second-order lattice Bianchi identity. Here is
a local proof that specifies its algebra without presuming componentwise
regularity of a.

On a unit three-cube choose the root vertex and the coordinate-ordered
spanning tree. Let lambda at a vertex be the sum of a on its tree path,
and set `c=a-d_1 lambda` on cube edges. Each remaining edge circulation
is filled by a fixed finite collection of the six cube faces. Consequently

    |lambda| <= 3 max_cube |a|,
    |c| <= C max_cube |f|.                                    (BC4)

This is the elementary cochain identity on the contractible cube; its
constant involves at most the finite cube's edge/face count, not ell.
For a pure gradient consider the actual pure-gauge links
`U_xy=exp(-epsilon lambda_x)exp(epsilon lambda_y)`. Their link logarithms
are `epsilon d lambda-epsilon²[lambda_x,lambda_y]/2+O(epsilon³)`.
Every face product is exactly identity. Taking its second coefficient
gives

    B_p(d lambda)=d_2 C(lambda),
    C_xy(lambda)=[lambda_x,lambda_y]/2,
    d_3 B_p(d lambda)=0.                                      (BC5)

Apply the quadratic polarization of the actual B_p to `a=d lambda+c`.
The pure-gradient part cancels in d_3, leaving only terms with at least
one c. BC4 therefore proves the local polynomial factorization bound

    |d_3 B_p(a)| <= C(max_cube |a| max_cube |f|
                                        +(max_cube |f|)^2).    (BC6)

It holds for the complexified Lie algebra as a bilinear coefficient
identity, and also after polarization in two separate external momenta.
All maps used in its proof have fixed cube support. Thus the given
potential and curvature kernels imply `R=O(ell^-3)` on the same joint
complex tube. No estimate on arbitrary derivatives of a was inserted.
In summary, with counting norms on the fine ell-cell,

    ||S(k,theta)||_infinity+||R(k,theta)||_infinity
                                      <= C ell^-3.            (BC7)

Here k is total input momentum and theta is the first input momentum;
the second is k-theta. All input colour/direction components obey BC7.
The physical differential is complexified analytically: the adjoint
symbol is evaluated at **negative momentum and transposed**, not
complex-conjugated at the same momentum.

## 3. High aliases: a counting-norm Green estimate

We prove the elementary bound needed for BC7. Fix a small delta<pi/8 and
consider `|Re k_mu|<pi+delta`, `|Im k_mu|<eta`, with eta sufficiently small
and fixed. On the ell^4 fine cell use balanced aliases
`K_mu=-(ell-1)/2,...,(ell-1)/2` and set

    q_K=(k+2pi K)/ell,
    nu_mu(q)=exp(iq_mu)-1,
    phi(q)=sum_mu (2-exp(iq_mu)-exp(-iq_mu)),
    P_K(k;u,v)=ell^-4 exp(i q_K.(u-v)).                        (BC8)

These are biorthogonal projections for complex k. `P_high=sum_(K!=0)P_K`
is a branchwise projection, not a globally periodic projection. On
one-forms, two-forms and three-forms, the cochain Hodge Laplacian is the
same scalar phi on every orientation component.

**High-alias lemma.** Uniformly for odd ell>=3 on this tube,

    ||d Delta(k)^-1 P_high||_(infinity->infinity)
      +||d* Delta(k)^-1 P_high||_(infinity->infinity) <= C ell.  (BC9)

The norms use counting measure. Fixed exterior-form multiplicities are
part of C. This does not assign an inverse to the zero eigenvalue at k=0.

For completeness, let h_t(j) be the one-dimensional continuous-time
nearest-neighbor heat kernel, with generator
`f(j+1)+f(j-1)-2f(j)`. Its Fourier integral gives positivity, total mass
one, symmetry, and

    h_t(0)<=C(1+t)^-1/2,
    sum_j exp(alpha j) h_t(j)=exp(2t(cosh(alpha)-1)).            (BC10)

Positivity follows also by expanding the two independent Poisson jump
counts. To justify monotonicity rather than assume a Gaussian estimate,
put `g_j=h_t(j)-h_t(j+1)` for j>=0. Directly differentiating gives
`g_0'=g_1-3g_0` and `g_j'=g_(j-1)+g_(j+1)-2g_j` for j>=1, with initially
g_0=1 and the other g_j=0. This bounded half-line operator has nonnegative
off-diagonal entries; its exponential, obtained by adding a scalar
multiple of the identity and using its power series, preserves positivity.
Hence h_t is decreasing on nonnegative integers. Weighted telescoping of
the nonnegative differences, using BC10, gives for 0<=alpha<=1

    sum_j exp(alpha|j|)|h_t(j+1)-h_t(j)|
       <= C[(1+t)^-1/2+alpha] exp(C alpha²t).                  (BC11)

Indeed on each half-line the telescoping sum is bounded by a boundary
term C h_t(0) plus `(exp(alpha)-1) sum_j exp(alpha|j|)h_t(j)`;
the latter mass is at most twice BC10's exponential. Tensoring four
copies proves the same bound for one directional difference of the
four-dimensional heat kernel H_t, with another absolute constant.

The exact twisted heat kernel has the image representation

    exp(-t Delta(k))(u,v)
             =sum_(m in Z^4) exp(ik.m) H_t(u-v-ell m).         (BC12)

It follows by applying the boundary character, or by finite Fourier
summation. For complex k it follows by absolute normal convergence of
the jump-count series. Since `|m|_1 <= |u-v-ell m|_1/ell+4`, with one
additional harmless constant for a boundary-crossing difference, its
derivative row sum is bounded by BC11 with alpha=eta/ell. For
0<=t<=ell² this is `C(1+t)^-1/2`; the extra alpha term is absorbed because
`alpha sqrt(1+t)<=C eta`. The subtracted K=0 heat derivative has counting
row sum at most
`C |nu(k/ell)| exp(C eta²t/ell²)<=C/ell` on this time interval.
Thus

    ||d exp(-t Delta)P_high|| <= C(1+t)^-1/2+C/ell,
                                      0<=t<=ell².             (BC13)

For t>=ell², elementary sine/cosh estimates on BC8 give
`Re phi(q_K)>=c |K|²/ell²` for K!=0, and
`|nu(q_K)|<=C(1+|K|)/ell`. These remain true in the slightly enlarged
real cube by decreasing c; the balanced extreme aliases lie only
delta/ell beyond a fine Brillouin face. The complex phase in P_K has
absolute value at most exp(4eta). Summing a row **first** gives

    ell^4 * ell^-4 * C/ell
       sum_(K!=0)(1+|K|) exp(-c t|K|²/ell²)
           <= C/ell exp(-c' t/ell²).                          (BC14)

The counting factor ell^4 cancels the Fourier normalization ell^-4.
No sum of absolute Fourier inverse coefficients is substituted for this
calculation at small t. The remaining Gaussian series in BC14 is bounded
by a constant times exp(-c't/ell²) for t/ell²>=1, independently of its
finite cutoff. Integrating BC13 and BC14 over their respective time
intervals proves BC9. The inverse and its derivative are holomorphic
there by normal convergence of the high-alias heat integral.

## 4. Zero alias: uniform analytic division from a nonuniform germ

The low Fourier coefficient is the normalized biorthogonal average
`A_0=ell^-4 sum_u exp(-ik.u/ell) A(u)`. Its norm is bounded by the
cell sup norm times exp(4eta); no cell-volume factor is lost. Taking
the zero alias of the Hodge consequence of BC2 gives, where phi is nonzero,

    phi(k/ell) Psi_0 = N_0 := d(k/ell) S_0+d*(k/ell) R_0,
    ell² Psi_0 = N_ell/P_ell,
    N_ell=ell^4 N_0,
    P_ell=ell² phi(k/ell)=4ell² sum_mu sin²(k_mu/(2ell)).        (BC15)

BC7 and `d(k/ell)=O(ell^-1)` give `N_0=O(ell^-4)` and a uniform bound
on N_ell on the joint input tube. The desired quotient is therefore
bounded at scale one; the physical Psi_0 has scale ell^-2.

For each **fixed** n, the hidden rooted Hessian is positive on its
complement at real k, including k=0. The finite matrix analytic implicit
function theorem supplies a stationary germ there. At this order its
concrete formula is `w2(k,theta)=-H_hidden(k)^-1 S_CJ7(theta,k-theta)`;
S_CJ7 is the full hidden quadratic source, distinct from the bottom Euler
one-form S in BC2. Thus no nonlinear closure of a single Bloch mode is
assumed. If the localized
first lift differs from the orthogonal lift, the finite rooted gradient
Gram solves for the analytic gauge change in a possibly smaller germ;
equivalently use the affine section with the chosen first tangent.
This step makes no claim about a uniform inverse, spectral lower bound,
or analyticity radius. For each real theta it proves that the actual
N_ell in BC15 is divisible by P_ell on a possibly tiny complex neighborhood
of k=0, with theta also locally analytic. This is holomorphic divisibility,
not a statement based on real smoothness.

Here is the uniform extension argument. On a fixed small complex polydisc
set

    w_mu=2ell sin(k_mu/(2ell)),
    k_mu=2ell arcsin(w_mu/(2ell)),
    P_ell=sum_mu w_mu².                                      (BC16)

For ell>=3 these maps and their derivatives have uniform bounds on any
sufficiently small fixed polydisc. Choose rho>0 below a fixed fraction of
the input strip, and below 1/32; choose r=rho/16. The inverse map sends
`|w_mu|<2rho` into the source tube while theta remains in a fixed smaller
strip and k-theta stays in the original strip. Let
`F(w,theta)=N_ell(k(w),theta)`, with bound M independent of ell. Write
`w'=(w_2,w_3,w_4)`, `A(w')=sum_(mu>=2)w_mu²`. Define

    Q(w,theta)=(1/(2pi i)) integral_(|z|=rho)
             F(z,w',theta)/[(z²+A(w'))(z-w_1)] dz.             (BC17)

For `|w_mu|<r`, both denominator factors on the circle are bounded away
from zero: `|z²+A|>=rho²-3r²`, `|z-w_1|>=rho-r`. The expression is
holomorphic in w and every theta component, and

    |Q| <= 4 M/rho².                                        (BC18)

For a fixed real theta and w' sufficiently close to zero, both roots of
`z²+A(w')` lie in the fixed-n divisibility germ. All possible poles of
`F(z,w',theta)/(z²+A)` inside the circle are precisely those two roots,
including their coalescence at zero; the germ removes them. Cauchy's
formula then gives `F=(sum w_mu²)Q` for |w_1|<r and such w'. The identity
theorem in the three w' variables extends this equality over their whole
connected r-polydisc. Since this holds for every real theta, the identity
theorem, applied successively to the theta variables, extends it throughout
their fixed connected complex strip. The n-dependent germ radius has
disappeared from BC18.

This proves divisibility on **all** of the quadratic zero variety in the
smaller polydisc, including its singular vertex and both roots in every
one-variable slice. It is an explicit continuation of the germ, rather
than an assumption that its zero-set branch extends. No irreducibility
or unspecified real-to-complex continuation theorem is required.

There are no additional zero components in a sufficiently thin top tube.
For `k=x+iy` in the enlarged real cube, direct cosine/cosh estimates give

    Re P_ell(x+iy) >= (4/pi²)|x|_2²-2|y|_2².                 (BC19)

Shrink the final imaginary width below a fixed small multiple of r.
Every zero then lies in the BC17 polydisc. More explicitly the regions
`|Re k|_infinity<r/2` and `|Re k|_infinity>r/4` cover the tube. The first
is inside the division patch after the harmless uniform change BC16;
on the second, BC19 gives a fixed positive lower bound c r² when the
width is small enough. Direct division there and BC17 on the first region
agree on their overlap. Therefore

    ||Psi_0(k,theta)|| <= C ell^-2                            (BC20)

on a fixed smaller joint tube, independently of n. The proof permits
arbitrarily small fixed-n stationary analyticity radii.

At k=0, BC17 agrees with the actual fixed-n stationary germ, so its value
is exactly `harmonic(B_p(a))`. For every theta, including nonzero opposite
input momenta, the mean of `d_2 w2_0` is zero on the periodic fine cell.
Thus subtracting B_p leaves zero harmonic mean for g. There is no manually
inserted constant harmonic correction and no long-range mean-subtraction
tail. The constant noncommuting control below checks the nonzero retained
Psi harmonic directly.

## 5. Reconstruction, reciprocal folding, and both density bounds

On each alias branch reconstruct

    Psi_high=d_2 Delta^-1 P_high S+d_3* Delta^-1 P_high R,
    Psi=Psi_high+exp(ik.u/ell) Psi_0.                          (BC21)

BC7 and BC9 bound the first part by `C ell * ell^-3=C ell^-2`;
BC20 bounds the second by the same amount. For real nonzero total
momentum, Hodge inversion is unique and BC21 agrees with the actual
stationary curvature. At zero it agrees by the germ and its harmonic
condition. The same identity shows that subtracting B_p gives a closed
two-form family g on the whole complex tube, by analytic continuation.

Periodicity requires a check because the selected low alias is not
itself periodic. A fixed finite cover can be chosen as follows. For each
real input coordinate use the central interval
`(-pi+delta/2,pi-delta/2)` and the two face lifts
`(pi-delta,pi+delta)`, `(-pi-delta,-pi+delta)`. Take their eight-fold
products for the two input momenta. For the total momentum use the folds
`k=p+q-2pi m`, `m in {-1,0,1}^4`, retaining the open pieces with
`|Re k_mu|<pi+delta`. These finitely many pieces cover the real input
torus and a fixed thin complex tube. Their number and the constants do
not depend on n. Convex connected overlap components may be used.

On changing a fold, `K -> K+m` modulo ell permutes the complete alias
sum in BC8. Adding ell to an alias leaves both its derivative symbols and
its cell exponential unchanged. The high part and the selected low part
change separately; their reconstructed sum has the actual fine-cell
boundary character exp(ik_mu), which is unchanged. On a real overlap
away from total zero, both expressions equal the same actual finite-depth
stationary solution. The holomorphic identity theorem in both external
momenta identifies them on the complex overlap. The removable extension
then preserves that identity at the complex zero variety. The actual
S4′ coefficients are periodic in each independent top input momentum,
so the same argument glues their input faces. This establishes a periodic
holomorphic family, not merely matching estimates on opposite faces.

The localized linear lift bounds `B_p(a)=O(ell^-2)` as a bilinear symbol.
Consequently BC21 gives a periodic holomorphic bound `C ell^-2` for g
on the joint input tube. Shift the two independent Fourier contours
componentwise by a smaller fixed eta. For output `b=ell X+u`, coefficient
extraction gives

    |K_g(u;x-X,y-X)| <= C ell^-2
                       exp[-eta(|x-X|_1+|y-X|_1)].             (BC22)

Replacing X by b/ell costs a fixed factor, since |u/ell|_1<4. Sampling
the infinite-volume Bloch symbol at the T-torus momenta is exact
periodization; uniqueness on the real fibres and the retained harmonic
value identify it with the actual finite-T response. Thus BC22 yields
BC3. For 0<m<eta/2, the positive exponential envelopes give separately

    sup_b sum_(x,y)|K_g(b;x,y)| exp(m diam(b/ell,x,y))
                                                  <= C_m ell^-2,
    sup_x sum_(b,y)|K_g(b;x,y)| exp(m diam(b/ell,x,y))
                                                  <= C_m ell². (BC23)

The second line sums all ell^4 fine bases per top cell. Its factor is
`ell^4 ell^-2=ell²`. Orientations and colours multiply fixed constants.
No row-to-column norm identification, or supremum over factorized signs,
is used. This proves CJ18 on the exact BC1–BC2 source, conditional on the
explicit upstream table in Section 1.

## 6. Conditional full-quartic consequence and precise limits

The remaining bridge is the one stated after CJ19, now with BC3 available.
Use the repaired **periodic** TU-3 primitive on g, with total momentum
as its twisted variable and theta as an extra parameter. Closure and
the harmonic condition were proved above. It yields a bottom second
potential of amplitude `C ell^-1` on a fixed smaller joint strip.
The actual second residuals from BC1 are

    r2_j=B_j(a_j)+q_j/kappa_j.                                (BC24)

At s=n-j-1 their amplitude is at most `C L^-2s`. Propagating a primitive
forward with the actual Q maps, the NQ-1 bound gives, with
`m=j-1-i` and `s=n-j`, a residual contribution
`L^m L^-2(s+m)=L^-2s L^-m`. Its sum is geometric. The primitive's
contribution is `C L^j ell^-1=C L^-(n-j)`.
The top defect is a holomorphic closed one-form in total momentum.
CJ11's analytic one-form lemma, with theta retained, makes its value at
total zero vanish. The same local root interpolation corrects the top
to zero, without a harmonic tail. This produces one admissible second
coefficient with amplitudes `C L^-(n-j)` and the corresponding absolute
weighted row and anchored-column kernels.

It is essential to apply these estimates to the completed stationary
quartic, not separately to the bare quartic and its exchange. With the
definitions preceding CJ18, its exact value is

    T4=R4 + (1/2)||D_h w2+Z||² + U_a(w2),
    U_a(w)=<Da,DZ[a]w>.                                      (BC25)

Its bottom square has amplitude ell^-4 and one ell^4 output count, hence
O(1). Its soft square is `q_j²/kappa_j`, with vertex count L^4s and
amplitude L^-6s, hence a summable L^-2s. Every soft R4 monomial contains
a linear residual and has at least the same summable power. The bottom
terms of R4 occur once. The bottom U term has amplitudes
`ell^-2,ell^-1,ell^-1` and count ell^4. Each soft U term has amplitudes
`L^-3s,L^-s,L^-s` and count L^4s, hence a summable L^-s.

Polarize each local polynomial before taking absolute coefficient sums.
Each external leg has its exponential envelope to the vertex; this
controls the diameter weight and the anchored output sum exactly as in
BC23. Only finite path lengths, orientations, colours and polarization
factors enter C. Therefore, under the stated named linear/current contracts,

    sup_(n,T) |||D^4 T_n(1)|||_m <= C_4 < infinity             (BC26)

for the full noncommuting-colour jet, including cubic exchange. Together
with the existing quadratic and cubic inputs this is the jet-bound
interface CJ2 used by UIR55's class J at the trivial background. It does
not by itself prove the finite-part increment or its convergence, a
uniform neighborhood of the identity, a finite-u analogue, or a continuum
existence or spectral theorem. The separate determinant root and harmonic
Gram factors described in CJ8's domain discussion remain separate; none
is inserted into the classical value BC25 or deleted from a determinant
consumer. The upstream packet has received the scoped review recorded
above. The immediate next obligation is fresh independent review of this
new source/analytic-division bridge and its use of those contracts.

## 7. Evidence, literature reuse, and provenance

The [prospective criteria](checks/bottom_second_curvature_criteria.md)
precede both programs. [Program 01](checks/bottom_second_curvature_01.py)
uses the actual d4 twisted-cell Fourier kernels at ell=3,9,27 and
independently builds the ell=3 incidence matrices. Its 76 predicates pass.
The sampled counting norms `||d_mu Delta^-1 P_high||/ell` range from
.222222 to .340397, including complex face twists; these samples support
the proof and are not a depth-uniform argument. It also checks the complex
image formula and rejects omitted cell normalization, complex conjugation,
an individually periodic high branch, and origin-only divisibility.

[Program 02](checks/bottom_second_curvature_02.py) independently constructs
the L=3 paired S4′ SU(2) Bloch cell: 81 sites, 324 hidden links, 486
plaquettes, 7,776 paired contours, and 80 rooted scalar gauge directions,
with kappa=.7 and the exact `1/(24*3^4)` mean. This is the fundamental
cell of the Bloch operator, not a restriction of the analytic theorem to
a one-site physical top torus. Both external momenta and noncommuting
colours are retained. The top cubic current is assembled from three
**linear** stationary lifts before independently solving for w2.
All 61 predicates pass. At an actual complex null point of the normalized
phi, the low numerator is `1.8302e-17` while total curvature is `.0820789`.
Deleting the soft DB source changes that numerator by `3.60695e-5`;
deleting the Wilson DB or Bianchi source is also detected.

A 48-node Cauchy circle of radius .06, using the actual source, recovers
the direct low curvature at a complex null point to `3.17e-15`. At zero
total momentum it recovers the nonzero constant noncommuting harmonic
`max|B|=.1422222222` to `8.44e-15`, while g has zero mean. Additional
controls check exact cochain identities, rooted stationarity, the local
quadratic Bianchi cancellation, reciprocal faces, and the factor 24.
Neither program imports predecessor helper code. Complete outputs and
stderr are frozen, including any failures if they occur. No predicate
failed in the first completed runs of these two new programs. Predicate
counts are not counts of independent proofs.

The heat-kernel mechanism is compared with
[Abadias–De Leon-Contreras, J. Evolution Equations 22 (2022), article 91,
Lemma 2.6](https://link.springer.com/article/10.1007/s00028-022-00851-1):
that primary result gives unweighted l1 difference estimates on Z. The
complex-character weighted version needed here is proved directly in
BC10–BC14. The paper explicitly cautions against a global Gaussian
pointwise estimate for the discrete heat kernel; no such estimate is
assumed here. [Dowker, arXiv1207.2096v2, equations (13)–(15)](https://arxiv.org/pdf/1207.2096v2)
gives the phase-twisted circle image/Fourier formula for real phase.
BC12 uses its exact mechanism and proves the required complex extension
by the jump-count exponential moment; the d4 kernel is its product.

[Dybalski–Stottmeister–Tanimoto, arXiv2303.10754](https://arxiv.org/abs/2303.10754)
was screened at its abstract for the Combes–Thomas/analytic Fourier/image
strategy; no theorem from it is imported. An attempted v2 HTML retrieval
failed and is recorded. The prior unit's exact selected Dimock/Balaban
read coverage and dimension/constraint mismatches remain as recorded in
its immutable manifest. None is silently promoted to a nonlinear
four-dimensional soft-chain theorem. The selected current LINEAR_PACKAGE,
legacy PROOF, and S13–S15 review repairs supply the alias-removal and
periodic-gluing precedent; BC17–BC23 explicitly discharge those tasks
for this new bilinear source.

[Michta–Slade, ALEA 19 (2022), Lemma 2.1](https://alea.impa.br/articles/v19/19-38.pdf)
was also read at its definitions and Bessel-resolvent representation
(2.3)–(2.5). Its scalar infinite-lattice Laplacian has symbol
`1-d^-1 sum cos k_mu`; the present phi is `2d` times that symbol. Its
heat time must therefore be rescaled by 2d. That representation is a
useful normalization comparison, not a theorem about the complex twisted
cell, the bilinear stationary source, or its removable complex zeros.
The paper's asymptotic proof and Appendix B were not read or imported.

The physics-loop/review-loop authority remains the fetched revision
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`; stale local main is not used.
The [source/read manifest](checks/bottom_second_curvature_source_manifest.json)
records actual coverage and hashes, separating inherited reads, fresh
selected reads, primary literature screening, and unsuccessful retrieval.
The [freeze receipt](checks/bottom_second_curvature_receipt.json) binds the
owned argument and all evidence. New work is provisional pending fresh
review; root owns integration/publication and all shared status changes.
