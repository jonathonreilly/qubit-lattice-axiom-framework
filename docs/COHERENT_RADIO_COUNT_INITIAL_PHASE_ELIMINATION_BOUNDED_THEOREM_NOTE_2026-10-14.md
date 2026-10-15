# Initial receiver phase elimination from coherent radio counts

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [coherent_radio_count_initial_phase_check.py](../scripts/coherent_radio_count_initial_phase_check.py)

**Exact target:** for supplied invertible endpoint phase operators in fixed
units, construct observable contrasts that eliminate arbitrary initial receiver
phases, propagate finite errors, and derive the at-most-two-dimensional initial
phase response for three coherent links driven by two uplink chirps.

This is a conditional observation-operator theorem. The standard three-link
plasma combination and null-space projection are reconstructed tools, not new
laws or novelty claims. The contribution to this campaign is an explicit
finite-count construction, its chirped physical operator and a checked way to
avoid selecting an initial receiver phase. It does not select a scalar action,
initial field history, absolute scale or environmental solution.

## Observations before reconstruction

The exposed Cassini June 18 development ODF supplies only X/X coherent band
pairs; distinct ground-station links are not frequency diversity. The archival
count reconstruction is documented in
`CASSINI_DOPPLER_COUNT_STATION_TIME_BOUNDED_THEOREM_NOTE_2026-10-14.md` and is
provenance context, not a mathematical premise here. Reserved calibration and
validation products remain unopened. No archive measurement enters this note's
mathematical runner; its carrier values and phase histories are synthetic.

[Armstrong (2006), sections 4.3–4.6](https://pmc.ncbi.nlm.nih.gov/articles/PMC5256086/)
describes the three coherent X/X, X/Ka1, Ka/Ka2 links with ratios 880/749,
3344/749 and 14/15. The
[Cassini Radio Science User's Guide (2018), section 3.6.2.2, printed pp.64–67](https://pds.nasa.gov/data/pds4/misc/document_cassini/Cassini_Radio_Science_Users_Guide_30Sep2018.pdf)
describes media calibration and trajectory modeling. These supply instrument
context. Their published precision is not an error bound used here.

The inspected day169 RSR directory names X/X and X/Ka products; their raw
samples have not been opened in this block. The file naming convention is
specified in the [Cassini RSS archive SIS, section 3.3](https://atmos.nmsu.edu/pdsd/archive/data/co-ss-rss-1-sce1-v10/cors_0024/document/casrssis.txt).
The [DORS-002 format, sections 4.2.3–4.2.5](https://atmos.nmsu.edu/pdsd/archive/data/co-ss-rss-1-sce1-v10/cors_0024/document/dors_002_020501.txt)
identifies PD1/PD2 as retrieved wet/dry atmospheric path delays and quality
flags. They are potential nuisance-calibration suppliers, not extra coherent
radio phases. This metadata inspection establishes no physical error bound.
The three-link calculation below is an explicitly supplied model class; the
complete real measurement supplier remains application work.

## Derive the frequency law under explicit medium premises

Adopt linear Maxwell equations in a cold collisionless unmagnetized electron
fluid, a fixed neutralizing ion background, and geometric optics on a common
prescribed ray. These are external physical hypotheses, not consequences of
the revised scalar action or lattice axioms. Linearizing the electron equation
with exp(i(kz-omega t)) gives

    -i omega m_e v = -e E,
    J = -n_e e v = i n_e e^2 E/(m_e omega),
    n^2 = 1 - omega_p^2/omega^2,
    omega_p^2 = n_e e^2/(epsilon_0 m_e).

Define positive accumulated receiver cycles using exp(i(omega t-kz)). The
phase advance relative to vacuum on a ray is

    delta Phi = (f/c) integral (1 - sqrt(1-X)) dl,
    X = f_p^2/f^2,
    delta Phi = K N_e/f + higher order,
    K = e^2/(8 pi^2 epsilon_0 m_e c),
    N_e = integral n_e dl.

This is a carrier phase advance; the group delay has the opposite derivative
relation and is positive. Reversing the receiver-minus-reference convention
reverses the observed phase sign; it does not change the separation weights.
Do not put the raw ODF receiver/reference number into this equation without
the conversion and phase sign established in the measurement model.

For 0<=X<=eta<1, Taylor's theorem gives

    0 <= 1-sqrt(1-X)-X/2 <= X^2/[8(1-eta)^(3/2)].

Thus the first omitted phase term is bounded by f/c times the path integral
of the right side. This bound does not cover magnetic, collision, diffraction,
different-ray, or nonstationary eikonal corrections. Neither eta nor the
electron column is supplied by the metadata. Their physical bounds remain
open. The law is reconstructed conditionally, not fitted to a gravity target.

## 2. Coherent phase transfer and the common-path condition

For constant local uplink/downlink carrier frequencies F_u,F_d and a coherent
turnaround ratio k=F_d/F_u, the uplink phase advance is retransmitted with
factor k. Let delta Phi_l be the received phase residual in cycles after
known reference phase is removed, and set p_l=delta Phi_l/F_d,l (seconds).
At the stated leading order,

    p_l(t) = G(t) + U(t)/F_u,l^2 + D(t)/F_d,l^2 + e_l(t),
    U=K N_u, D=K N_d.

The retarded uplink and downlink columns are distinct functions. Equating
them is unnecessary. The same U and D across links requires common retarded
ray histories at each compared receive time; same ground date alone does
not establish it. The same G requires the appropriate common clock,
geometry, and nondispersive phase normalization. Coherent transfer cancels
the intermediate spacecraft clock only under the coherent-turnaround model;
it does not remove ground-clock or spacecraft-motion errors. All unmatched
path, clock, reference, electronics, slip and higher-order effects enter e_l.

The fixed carriers and shared phase functions are a model class, not an
assertion about the complete ramped Cassini instrument. In particular the
stored ODF reference/ramp frequency is not silently equated to F_u or F_d.

## 3. Exact aligned finite counts, without a smoothness premise

Write a=F_Xu^-2, b=F_Xd^-2, c=F_Ka1d^-2,
d=F_Kau^-2, e=F_Ka2d^-2. For X/X, X/Ka1 and Ka/Ka2,

    p = A z + epsilon,
    A = [[1,a,b],[1,a,c],[1,d,e]], z=(G,U,D)^T.

Here e is a matrix coefficient, epsilon a residual phase vector. If a!=d
and b!=c, define

    w1=(c*d-a*e)/[(a-d)(b-c)],
    w2=(a*e-b*d)/[(a-d)(b-c)],
    w3=a/(a-d).

Direct substitution gives w^T A=(1,0,0). For ANY unwrapped endpoint phase
histories obeying this relation, common endpoints s<r and T=r-s,

    d_l=[p_l(r)-p_l(s)]/T,
    w^T d = [G(r)-G(s)]/T + w^T[epsilon(r)-epsilon(s)]/T.

No approximation replaces a count by its midpoint derivative. U,D need not
be constant, linear, smooth, or statistically stationary inside the interval.
They may even have bounded jumps if the same unwrapped physical phases are
counted. The proof is subtraction of the endpoint equations. This eliminates
an intra-bin plasma interpolation premise within this supplied model class;
it does not establish that the real instrument satisfies that class.

For error limits |Delta epsilon_l/T|<=E_l, the deterministic bound is
sum |w_l| E_l. For a supplied covariance C of the measured counts, the
variance is w^T C w, including cross-channel covariance. Independence and
white-noise scaling are not derived. Nonzero weights of either sign can
amplify an error even while cancelling a plasma term.

The standard two-link difference instead has w1+w2=0: it cancels common
G together with the common uplink contribution and retains the downlink
plasma difference. It is a plasma diagnostic, not a unit-gain gravity signal.
For the first two rows the explicit vector (a,-1,0) has zero response.
This is a constructive ambiguity in this linear model, not a global
impossibility theorem for radio data with additional dynamics or information.

## 4. Count endpoints and station-clock alignment

Suppose a normalized instantaneous phase rate y_l is Lipschitz with constant
L_l on the union of the interval and its shift, including every translated
point pair (or derive this from a derivative bound on their connecting hull), and link l uses [s+delta_l,r+delta_l].
Then, with the same duration T,

    |average_shifted(y_l)-average_common(y_l)| <= L_l |delta_l|.

Integrate |y_l(t+delta)-y_l(t)|<=L_l|delta| to prove it. Consequently the
alignment contribution to the reconstructed common count is at most
sum |w_l| L_l|delta_l|. This is conditional on physical derivative and clock
offset bounds; neither is established by matching archive time tags.
Alternatively if only |y_l|<=B_l is known, endpoint interval differences
give 2 B_l |delta_l|/T for equal shifts. Use the tighter available bound;
do not infer L_l or B_l from finitely many samples without a justified
regularity model. Different durations require explicit rebinning or the
full endpoint formula, not this equal-duration statement.

## 5. Exact initial-state term in fixed count units

For varying carrier frequencies distinguish physical phase from its time-varying
normalization. Let Phi_l be the residual received phase in cycles and let
F_ref,l>0 be a FIXED conversion factor. Define q_l=Phi_l/F_ref,l. Corrected raw
counts divided by F_ref,l supply Delta q_l. They do not in general supply the
change in p_l=Phi_l/F_d,l(t), because

    Delta p_l = Delta Phi_l/F_d,l(r)
                + Phi_l(s)[1/F_d,l(r)-1/F_d,l(s)].

A constant nonzero phase Phi_l with changing F_d gives zero raw counts but
nonzero Delta p_l. This is a normalization counterexample, not a real Cassini
plasma history. The earlier working wording omitted this distinction; that source and the
independent finding are preserved in the campaign record.

Now suppose a specified invertible phase operator B(t) obeys q(t)=B(t)z(t),
z=(G,U,D)^T, and define v_t^T=(1,0,0)B(t)^-1. If a physical model was originally
written p=A(t)z, then B=diag(F_d,l(t)/F_ref,l) A(t). The two-chirp section below derives a restricted physical operator.
Its extension to the full calibrated retarded proper-clock transfer remains
a separate application obligation. In particular it need not retain first column 1.

With d=(q_r-q_s)/T, exact linear algebra gives

    (G_r-G_s)/T = v_r^T d + (v_r-v_s)^T q_s/T
                = v_r^T d + [v_r^T B_s-(1,0,0)]z_s/T.

Proof: substitute q_r=B_r z_r and q_s=B_s z_s. Counts give Delta q in these
fixed units; the correction also uses the allowed initial state. If B_r=B_s
the correction vanishes. More generally equal endpoint row weights suffice,
even when individual nuisance columns change.

In the special class where B(t) has common first column 1, the correction has
zero G_s coefficient. It is then [v_r^T a_s U_s+v_r^T b_s D_s]/T for its two
nuisance columns. Do not apply this simplification to a chirped physical B
without deriving that column. Given a verified box |z_s,j|<=B_j, the exact
correction bound is sum_j |[v_r^T B_s-(1,0,0)]_j| B_j/T. Neither initial phase
nor initial column bounds follow from count-derivative bounds alone. If the
measured q includes endpoint phase errors epsilon, their propagated term is
[v_r^T epsilon_r-v_s^T epsilon_s]/T; a bound on Delta epsilon alone need not
control it when the weights change.

Constructive witness in fixed units: B_s has rows
(1,1,1),(1,1,1/4),(1,1/4,1/4). B_r has the same rows except its final uplink
coefficient is 1/5. The history q_r=q_s=B_s(0,1,0)^T and z_r=B_r^-1 q_r has
zero counts but G_r=1/16, G_s=0. The zero history has the same zero counts and
zero common-phase change. The nonzero history has U_s=1,U_r=15/16,D_s=D_r=0.
This checks the missing-state term within the matrix model; it is not an
assertion that measured Cassini ramps realize this matrix evolution.


## Eliminate initial receiver phase across count intervals

Let aligned endpoints t_0<...<t_n be fixed. At each endpoint,

    q_i = B_i z_i,  z_i=(G_i,U_i,D_i)^T,
    v_i^T=(1,0,0) B_i^-1.

Each B_i is a known invertible matrix. Each q_i is in FIXED phase units:
q_l=Phi_l/F_ref,l with constant F_ref,l. The measured count increments are
Delta q_i, not a time-varying-frequency normalization. Put c_0=0 and
c_i=sum_{k=1}^i Delta q_k. Then q_i=q_0+c_i and

    G_i = v_i^T c_i + v_i^T q_0.

Let r_i=v_i^T c_i and let W have row i equal to v_i^T. The full endpoint
common phase is therefore G=r+W q_0. No dynamic model or bound on q_0 is
used in this identity. It holds for arbitrary latent histories satisfying
the specified B_i, including independently varying U_i,D_i.

### Exact state elimination and recoverable contrasts

For any contrast h with h^T W=0,

    h^T G = h^T r.

The linear space of these exact contrasts has dimension n+1-rank(W).

This is directly executable: compute W from the supplied endpoint operators,
solve W^T h=0, and apply h to r made from counts. The contrast may retain less
than the individual G_i. Reporting it as a full recovery of G would be false.
For constant B, all rows of W are equal, so any h with sum h_i=0 is allowed.
For varying B the contrast conditions generally differ from ordinary time
differences. No initial phase value is supplied, optimized toward a theory
target, or inferred from an unmeasured absolute phase.

### Add explicitly modeled clock/trajectory nuisance functions

Suppose a physical candidate supplies a common-phase signature s and a
specified finite set of nuisance histories H, so

    G = theta*s + H*beta + epsilon.

The amplitudes theta,beta are unknown; selecting the columns of H and deriving
the candidate signature s are additional premises, not a fit result or a
proof that real errors lie in H. Define K=[W H]. If h^T K=0 and h^T s!=0,

    theta_hat = h^T r/(h^T s),
    |theta_hat-theta| <= sum_i |h_i| E_i / |h^T s|

when |epsilon_i|<=E_i and counts are exact. With count errors also present,
add their propagated error as derived below. Thus one can eliminate an
arbitrary initial phase and arbitrary amplitudes of the declared nuisance
histories without pretending to have derived their numerical values.

For a positive-definite supplied endpoint covariance C, the minimum-variance
unit-response, nuisance-annihilating contrast is obtained by minimizing
h^T C h subject to K^T h=0 and s^T h=1. Calling the resulting estimator
unbiased additionally requires zero-mean remaining physical and count errors,
or subtraction of their known means. Covariance alone does not imply that
premise: epsilon=delta*s+xi with E[xi]=0 and Cov(xi)=I has unchanged
covariance but induces bias delta for every unit-response contrast. For the simple C=I case let P be the Euclidean projector onto
ker(K^T). If P s!=0, h=P s/(s^T P s) has the required constraints and minimum
norm, by Cauchy-Schwarz on that subspace. It preserves only the part of s
outside the nuisance span. If s=K a, every admissible contrast annihilates it;
that explicit algebraic overlap must be reported rather than remedied by
deleting a real nuisance. No claim of general physical indistinguishability
follows from an arbitrarily chosen finite H.

### Count-error propagation without false independence

If measured increments have vector errors eta_k, the error in h^T r is

    sum_{k=1}^n b_k^T eta_k,
    b_k = sum_{i=k}^n h_i v_i.

This follows by interchanging the finite sums in c_i. With componentwise
limits |eta_kl|<=E_kl, a deterministic bound is sum_kl |b_kl| E_kl.
With a supplied covariance Sigma for all stacked increments, the variance is
b^T Sigma b. Cumulative sums create endpoint correlations even when the
increments are independent; an independently assumed endpoint white-noise
model is not justified by the count construction.

For an amplitude contrast normalized to h^T s=1, add this count-error bound
to the propagated physical epsilon bound. The code checks saturation of the
componentwise count-error bound and uses correlated positive-semidefinite
increment covariances. It does not estimate either bound from archive
quantization or from the published final Cassini precision.

### Operator uncertainty and robust state elimination

The preceding cancellation is exact only for the supplied operator rows.
Using nominal W_0 when the true W differs gives a leakage h^T(W-W_0)q_0.
Thus exact nominal cancellation alone does not supply a uniform error bound
over arbitrary q_0 and uncertain W. The working calculation preserves this
failure rather than hiding it with q_0=0.

There is a stronger positive construction when the operator uncertainty has
a verified form. If h^T W(lambda)=0 for every allowed lambda, initial phase
elimination is uniform. For the special EXACT affine row family

    W(lambda)=W_0+sum_a lambda_a W_a,

solve [W_0 W_1 ...]^T h=0. This removes the unknown initial phase for every
lambda in that family, without bounding q_0. It is not enough to truncate an
unknown nonlinear family at first order and call the elimination exact.
Any discarded remainder times q_0 needs a justified bound.

The remaining coefficient error uses observed cumulative counts rather than
an assumed initial state:

    |h^T r(lambda)-h^T r(lambda_0)|
    <= sum_i |h_i| ||v_i(lambda)-v_i(lambda_0)||_* ||c_i||.

The norm pair may be Euclidean or another fixed dual pair. For joint operator and count errors, this last bound can use observed cumulative
counts c_obs only if the separate count-error term uses the TRUE operator
rows, bounded uniformly over the allowed family. More explicitly,

    h^T r_0(c_obs) - h^T r_lambda(c_true)
    = h^T [r_0(c_obs)-r_lambda(c_obs)]
      + sum_k b_k(lambda)^T eta_k,

where eta_k=Delta q_obs,k-Delta q_true,k. The first term has the displayed
data-based bound with c_obs; the second requires sup_lambda |b_kl(lambda)|.
For an exact affine row family with |lambda_a|<=Lambda_a and nominal 0,
b_k(lambda)=b_k(0)+sum_a lambda_a b_k,a, hence a valid bound is
sum_kl E_kl (|b_kl(0)|+sum_a Lambda_a |b_kl,a|). Physical endpoint-error
bounds also use true-family weights. Using nominal count coefficients alone
is not justified.

Preserved counterexample to that weaker joint rule: v_i(lambda)=(1+lambda,0,0)
at both endpoints, h=(-1,1), nominal0, true lambda1. True increment(1,0,0)
and error(-1,0,0) give observed count0. The observed-data operator term is0,
while the nominal count bound1 misses the true error2. The uniform true-
family bound2 covers it. This preserves the independent finding against the earlier joint-bound
wording; no empirical calibration follows.

When the exact affine coefficients, lambda range and count errors are
bounded, this gives a finite joint error limit without an initial-phase
amplitude premise. Constructing such an exact uncertainty family and its
physical bounds from real clocks, ramps and retarded rays remains open.


## Physical operator for two uplink chirps


Use the X/X, X/Ka1 and Ka/Ka2 architecture, with constant coherent ratios
k1,k2,k3. Two uplink phase functions have derivatives f_X(s),f_K(s)>0. The
first two links share f_X and the third uses f_K. Compare the same nominal
emission time s(t), bounce and receive events, after prescribed clock and
retarded maps. Let G(t) be a small common displacement of emission station
time. We do not assume it equals a gravitational delay; clock, geometry and
other nondispersive perturbations may contribute.

For the leading plasma phase, require separable local frequencies on the
nominal rays: f_u,local=f_u(s) Z_u(l,t),
f_d,local=k_l f_u(s) Z_d(l,t), with Z_u,Z_d common across the compared
frequency channels and positive. The common factors may include a specified
achromatic Doppler/redshift map. The same ray columns and their proper length
measure must be shared. This is a geometric-optics and weak-dispersion
condition; it is not justified by archive time-tag equality. Frequency-
dependent ray splitting, time-dependent media frequency conversion,
noncoherence, different ground clocks and missing electronics calibration
require explicit residuals and bounds.

From the carrier phase expansion, the two common weighted columns are
U=K integral n_e/Z_u dl and D=K integral n_e/Z_d dl. Conditional on the
specified eikonal phase convention and common rays, their contribution to
the received phase is k_l U/f_u + D/(k_l f_u). Common achromatic factors
may instead be absorbed into U,D; the cancellation below does not constrain
their histories. No column value or derivative is set to zero.

### Derive the fixed-unit matrix

Let fixed positive reference uplink frequencies be F_X,F_K. They are unit
normalizations, not fitted frequencies or extra empirical claims. Put
F_ref,l=k_l F_u,l and s_l=f_u,l/F_u,l. The reference-normalized phase
q_l=delta Phi_l/F_ref,l obeys to the declared order

    q_l = s_l G + a_l U/s_l + b_l D/s_l + epsilon_l,
    a_l=1/F_u,l^2,
    b_l=1/(k_l F_u,l)^2.

The geometric term follows from

    k_l[Phi_u(s+G)-Phi_u(s)]/F_ref,l = s_l G + R_l,
    |R_l| <= (sup |f'_u|)/(2 F_u,l) G^2

on the whole segment between s and s+G. This is the actual nonlinearity
discarded by the linear phase model, not a smooth-plasma assumption. Plasma
evaluated on perturbed rays and at shifted emission times also changes;
those cross terms and the cold-plasma expansion remainder belong to
epsilon_l. Their bounds have not been measured here.

Define constant A0=[1 a b], with rows
(1,a1,b1),(1,a1,b2),(1,a3,b3), and write

    B(t) = [ s(t), diag(1/s(t)) a, diag(1/s(t)) b ],
    s(t)=(s_X(t),s_X(t),s_K(t))^T.

This B acts on (G,U,D), with every measured q in fixed units. It is distinct
from dividing the measured carrier phase by its instantaneous frequency.
All frequency arguments are at the specified nominal emission event; the
shared mapping to that event remains an obligation for real data.

### Explicit inverse row and its singularity

Suppose A0 is invertible and w0^T A0=(1,0,0), with w0 given by the constant-
carrier formula. Put D_s=sum_l w0_l s_l^2. If D_s!=0, then

    v_l(t) = w0_l s_l(t)/D_s(t),
    v(t)^T B(t) = (1,0,0),
    det B(t) = det A0 * D_s(t)/(s_X(t)^2 s_K(t)).

Proof: v^T diag(1/s) a=(w0^T a)/D_s=0 and similarly for b;
v^T s=sum w0_l s_l^2/D_s=1. For the determinant, multiply B on the left
by diag(s), giving [s^2,a,b], and expand along the replacement first column
using the first row of A0^-1. Divide by product_l s_l.

Since w01+w02=-a3/(a1-a3) and w03=a1/(a1-a3),

    D_s=[a1 s_K^2-a3 s_X^2]/(a1-a3).

The vanishing condition is f_K^2=f_X^2. For positive frequencies it is the
loss of uplink frequency diversity. Downlink diversity also requires b1!=b2.
Thus the conditioning denominator has a physical origin; it is not a
regularizer chosen to make an inverse succeed. All numerical work excludes
these singularities by checking them, rather than clipping a small divisor.

### Initial-phase uncertainty has at most two observable shapes

At sample i, the inverse row decomposes exactly as

    v_i = alpha_i (w01,w02,0) + beta_i (0,0,w03),
    alpha_i=s_X,i/D_s,i, beta_i=s_K,i/D_s,i.

Therefore W (rows v_i) has rank at most two for arbitrary positive chirp
histories in this class. It does not require a constant relative chirp.
If s_K/s_X is constant across all sample endpoints, the rank is one.
With two distinct relative chirps, w03!=0 and at least one of w01,w02
nonzero, the rank is two, by independence of the two displayed channel
vectors. These nonzero conditions hold for finite distinct positive uplink
frequencies and the nondegenerate constant-carrier matrix.

For any h satisfying sum_i h_i alpha_i=sum_i h_i beta_i=0, the exact
fixed-unit count construction returns h^T G without choosing or bounding
the initial receiver phases. There are at least n+1-2 such contrasts for
n+1 endpoints before adding clock/trajectory nuisance columns. This is a
physical-architecture reduction of the generic three-initial-combination
model. It does not provide all G_i, the scalar initial state, or a full
plasma-free gravity inference.

With one common chirp s_X=s_K=s, v=w0/s and w0^T q=s G. Thus constant
channel weights recover Delta(s G) from counts directly; recovering G itself
still follows the stated contrast or initial-state relation. Confusing these
two targets would reintroduce the normalization error found in v1.

### Error and empirical obligations

After restoring epsilon, the contrast error is sum_i h_i v_i^T epsilon_i,
or its count/initial-phase form only when justified. The exact contrast
removes arbitrary initial phase for a known B, but an uncertain chirp or
common-path model can leak it back. Use the robust-family conditions in
the operator-uncertainty section above or supply justified bounds; do not silently
set the initial state or unmeasured residuals to zero.

The archived development product contains only X/X coherent bands. It has
not supplied simultaneous chirped X/Ka1 and Ka/Ka2 phases, the common-ray
mapping, or the error bound for this construction. Ratios and raw phase
conventions must be sourced and checked before physical reuse. This result eliminates a chosen initial receiver phase within its stated class;
it leaves action/potential selection, absolute scales, scalar initial history
and the real environmental solution open. Focused independent mathematics checks are recorded below; physical calibration is open.

## Proof obligations, imports and degenerate cases

| Component | Role and provenance | Exact result or open application obligation |
| --- | --- | --- |
| Linear Maxwell equations and cold collisionless unmagnetized electron fluid | Adopted physical premises, not derived from the scalar theory | Dispersion and Taylor remainder derived above |
| Coherent fixed ratios and a shared ray/clock mapping | Imported measurement model; instrument ratios sourced above | Common-column factorization derived conditionally; actual calibration still required |
| Calibrated unwrapped count increments, with slips and resets treated explicitly | Measurement inputs, not established by metadata equality | Constant initial phase is eliminated; time-dependent cycle slips require their own residuals or correction |
| Fixed phase units and supplied invertible endpoint matrices | Mathematical model hypotheses | Initial phase is eliminated for contrasts in the stated null space |
| Exact affine operator uncertainty family and count-error bounds | Optional supplied family/domain | Uniform cancellation and joint observed-data error bound proved; a real family/bounds remain to be supplied |
| Signature and nuisance-history basis | Candidate-specific supplied functions | Unit-response contrasts derived; physical completeness of that basis is not claimed |
| Covariance, error means, and pointwise limits | Optional statistical/deterministic inputs | Propagation derived; unbiasedness additionally requires zero means or removed known means |
| Two uplink chirps and separable local frequencies | Restricted physical architecture | Explicit inverse row, determinant and rank at most two proved; common paths and perturbation residuals remain conditions |
| Synthetic frequencies and histories | Illustrative fixtures, not fits or calibration data | Exact checks corroborate proofs; no independent empirical test |

The proof graph is: Maxwell/fluid equations to the conditional phase law;
constant-carrier factorization to finite-count endpoint subtraction;
fixed-unit accumulation to G=r+Wq0; a null-space contrast to elimination;
finite-sum interchange to count-error propagation; coherent chirped transfer
to B(t), its inverse row and the two-shape factorization. Each mathematical
step is proved in this note; no ancestor theorem output is needed. The last
physical application obligation is a candidate-consistent emission/ray/clock
operator and a controlled residual budget, followed by a specified signature
and an observation protocol. That obligation is not assumed to prove the
scalar theory. The strongest result here is the conditional contrast theorem.

The domain has ordered endpoints, fixed positive unit frequencies, invertible
operators and explicitly bounded errors wherever a bound is used. Coincident
actual uplink frequencies and equal relevant downlink coefficients give the
displayed zero determinant and are excluded from inversion. A constant
relative chirp has rank one rather than two. A signature in the chosen
nuisance span has zero projected response; the code supplies an explicit
example. Endpoint jumps require the stated global bound or a direct interval
treatment. Extra phase data, dynamical restrictions and alternative observation
models remain available routes; the finite witnesses here assert no general
impossibility or search exhaustion.

## Execution and review record

The primary runner directly imports all three mathematical helper modules and
declares them and this note as inputs. It reads no archive or ancestor output;
its package-local integrity reads hash the note and its own source closure.
Python, SymPy and mpmath are required. The declared cache timeout is 120 seconds.
It writes deterministic products under `outputs/coherent_radio_initial_phase`;
the source-bound cache is `logs/runner-cache/coherent_radio_count_initial_phase_check.txt`.
The author control families are 879 plasma/finite-count checks, 198 initial-phase
checks and 41 chirped-operator checks. Counts describe synthetic controls, not
independent observations or evidence of generality; the proof supplies that.

The focused independent implementation reconstructed the cold-fluid current,
exact inverses, interval integrals, null spaces, error propagation and chirped
families by separate calculations. It caught three substantive qualifications:
changing-frequency normalization needs an initial-phase term; a joint operator/
count bound must use true-family noise coefficients; covariance alone does not
imply unbiasedness. The repaired statements and explicit witnesses are above.
Working versions and findings are preserved in the campaign record. The final
source checks are in `physical_link/independent_v1` in the campaign pack. These
are focused author-stage checks, not a formal audit verdict or landing review.

The calibration/development/validation split is unchanged. No scalar fit or
physical precision is inferred. Full combined landing validation and independent
audit remain outstanding. This proposal introduces a bounded_theorem row for
that later independent assessment; no audit-owned status is written here.

## Claim-status record

```yaml
target_claim_id: coherent_radio_count_initial_phase_elimination
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact contrasts and finite error propagation for a supplied phase operator; a derived two-chirp subclass"
hypothetical_axiom_status: null
admitted_observation_status: "Exposed metadata motivates the model; no new empirical gravity test"
claim_type_reason: "Positive finite-count construction and explicit bounded error domains"
audit_required_before_effective_retained: true
bare_retained_allowed: false
trace_class: upstream_support
target_blocker_text: "Derive or eliminate measurement initial-state assumptions instead of choosing them"
source_of_blocker_text: user_goal
reachability_to_target: "Supplies observable contrasts eliminating initial receiver phase; scalar field state and real measurement calibration remain open"
artifact_role: "Conditional observation-operator theorem and synthetic controls"
next_trace_action: "Supply allowed simultaneous channels and their candidate-consistent retarded clocks/rays; test surviving signatures with justified error bounds"
```
