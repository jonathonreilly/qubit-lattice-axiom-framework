# Independent compressed-observation kernel review

Reviewer: `/root/force_energy_bridge_check`. This is a focused mathematical
check, not a formal audit, physical-data validation or publication approval.
Root is the sole scientific author. Files were written only in
`residual_energy/independent_count_kernel_v1`.

The precheck was frozen before any new author implementation was opened:
`PRECHECK_v1.md`, SHA-256
`fd11f68d69ed5542728e7060582a861759360ed17c9e83e19e66f6bb4f28ca4a`.
The independent implementation imports no author code. No raw observation,
reserved product or actual force residual was accessed.

## Findings

The proposed adjacent unequal-window hat and scalar fixed-point massless Gram
are correct. With real gaps the normalization must use the separation of the
window centroids, producing a trapezoid. Nonlinear clocks and varying known
calibration determine more general kernels; the kernel must be reconstructed
from those weights rather than freely replaced by a uniform average.

The initially important qualification is that canceling a constant scalar
readout does not cancel an arbitrary initial velocity vector when observation
direction changes. The corrected vector-moment condition resolves this and
derives a vector acceleration kernel without dropping the geometric term.
The vector Gram coefficient is exactly 1/(6pi) in the supplied massless,
fixed-spatial-point gradient model. The resulting weighted-regression energy
infimum has coefficient 3pi for uniform physical-time velocity means.

These statements concern the reduced observation model. There is still no
actual Cassini force residual, calibrated velocity readout, selected field
energy or independent observational test in this work.

## Unequal windows and gaps

For nonoverlapping ordered intervals I_i=[a_i,b_i], write T_i=b_i-a_i>0,
g_i=a_{i+1}-b_i>=0 and H_i=g_i+(T_i+T_{i+1})/2. Define

    r_i(s)=-1_Ii/(H_i T_i)+1_I{i+1}/(H_i T_{i+1}),
    w_i(s)=-integral_{-infinity}^s r_i(t)dt.

For absolutely continuous v, integration by parts gives

    (mean_{i+1} v-mean_i v)/H_i=integral w_i(s) v'(s)ds.

The weight rises with slope 1/(H_i T_i), is constant 1/H_i on the gap,
and falls with slope -1/(H_i T_{i+1}). Its total area is one. For zero
gap it is the unequal normalized hat. When the gap is nonzero, using the
adjacent-window H falsely gives area 1+2g_i/(T_i+T_{i+1}). Missing data or
record ordering alone therefore cannot establish temporal adjacency.

For raw unnormalized velocity integrals, D has row entries
-1/(H_i T_i), +1/(H_i T_{i+1}); the scalar massless fixed-point Gram is

    G=(1/(6pi)) D diag(T) D^T.

For velocity means, the corresponding contrast matrix has entries
-1/H_i,+1/H_i and the middle diagonal is diag(1/T). These are identical
representations. The diagonal entries are
(1/T_i+1/T_{i+1})/(6pi H_i²), adjacent off-diagonals are
-1/(6pi H_i H_{i+1} T_{i+1}), and other entries vanish. These off-diagonal
terms express the shared velocity window. This matrix is not an instrumental
noise covariance; that covariance has separate measurement provenance.

## Clock and calibration pushforward

Suppose, as an explicit physical-model premise, an instrument clock average
contains y(tau)=kappa(tau) z(S(tau))+b(tau)+e(tau), where s=S(tau) is known,
increasing, and z(s) is the intended physical-time velocity projection.
After subtracting a known integrated b, the kernel of one normalized clock
average is

    k_i(s)=kappa(tau(s))*tau'(s)/Delta_tau_i

on its mapped physical interval. For raw clock integrals remove the
Delta_tau denominator. Known reference-frequency or calibration factors
belong in kappa. They cannot be pulled out of an integral merely because
there is only one compressed output number.

A scalar contrast c annihilates arbitrary constant z exactly when
sum c_i M_i=0, M_i=integral k_i. If M_i!=0, divide the datum by M_i to
obtain p_i=k_i/M_i of unit integral. With mu_i=integral s p_i(s)ds,
H=mu_j-mu_i!=0, the normalized contrast produces

    w(s)=[integral_{-infinity}^s p_i - integral_{-infinity}^s p_j]/H.

This weight has area one and its derivative is (p_i-p_j)/H. Fixed-sign
calibration with ordered disjoint supports gives nonnegative p_i and w.
Arbitrary signed calibration does not guarantee positivity or good numerical
conditioning. Even known varying calibration does not normally allow a
compressed weighted mean to be replaced by the uniform physical-time mean.

The L2 metric also changes. For disjoint windows it contains
integral k_i(s)^2 ds; under the clock map this is

    integral kappa(tau)^2/[Delta_tau_i² S'(tau)] dtau.

S'>=epsilon>0 and bounded calibration suffice for finiteness. More generally
the displayed integral must be finite. Overlapping windows require their
actual cross integrals. A known affine clock and constant calibration reduce
to the uniform physical-time window after normalization.

The definition of the measured velocity matters. If it were dx/dtau rather
than dx/ds, the effective calibration includes S'. A uniform tau average
of dx/dtau equals Delta x/Delta_tau and can be normalized by
M_i=Delta s/Delta_tau into the uniform physical-time velocity average,
even for nonlinear S. Conversely naive differentiation in tau gives
x''(tau)=S'^2 a_s+S'' v_s. The clock-acceleration term is real and cannot
be omitted. The clock map does not itself select which measurement model
matches a radio count.

## Geometry and the exact corrected target

For z=n.v, scalar integration by parts yields
z'=n.a+n'.v. Thus the scalar hat contains both terms. A constant initial
vector v0 can still contribute integral w n'.v0, despite integral r=0.
For general compressed vector projections define

    F_c(s)=sum_i c_i k_i(s)n_i(s),
    N_i=integral k_i(s)n_i(s)ds.

The necessary and sufficient condition for canceling every constant v0 is
sum c_i N_i=0 as a three-vector. With two rows and nonzero vector moments,
this requires proportional moments. It is not implied by scalar weights
summing to zero. More observations allow a nullspace contrast; the actual
rank and any additional nuisance constraints determine whether one exists.

Under that condition,

    W_c(s)=-integral_{-infinity}^s F_c(t)dt

is compactly supported, W_c'=-F_c, and
sum c_i y_i=integral W_c.a exactly after any known additive corrections.
The varying direction is inside W_c. No separate n'.v term was discarded.
For this vector formulation it is enough that the known finite-window F_c
is integrable and L2, while v is absolutely continuous. Direction derivatives
are not needed merely to reconstruct this fixed-point measurement kernel.
No assertion is made that W_c has a constant direction or is a scalar
positive normalized hat.

## Vector Gram and energy infimum

For the supplied real free massless scalar on R³ and one common fixed
spatial point, let L_c(h)=integral W_c(s).grad h(s,x0)ds. Unitary spatial
Fourier transform and angular isotropy yield the exact dual inner product

    G_cd=(1/(6pi²)) integral_0^infinity
                       omega² Re[W_hat_c.conj(W_hat_d)] domega
        =(1/(6pi)) integral W_c'.W_d' ds
        =(1/(6pi)) integral F_c.F_d ds.

The unitary spatial angular factor is 4pi/3; real time weights supply the
half-line Parseval factor pi. The real-data constraint is compatible with
the Riesz representatives, as in the published finite-window proof.

For disjoint uniform physical-time means with |n_i(s)|=1 almost everywhere,
write B_ii=1/(6pi T_i). If C has rows annihilating all nuisance columns N,
then G=C B C^T. B is a convenient contrast-metric representation, not a
claim that every individual raw velocity average is a bounded energy
functional. Before cancellation, a raw velocity integral referenced to a
finite starting time can leave an endpoint jump in its acceleration weight;
that jump need not have finite energy-dual norm.

For a full row basis C of ker(N^T), B positive definite, and residual
contrasts z=C y, Hilbert-space minimization gives

    E_inf=(1/2) z^T (C B C^T)^-1 z
         =(1/2) min_beta (y-N beta)^T B^-1 (y-N beta).

The second identity follows by minimizing u^T B^-1 u subject to C u=C y:
the minimizer is u=B C^T(C B C^T)^-1 C y. Since ker C=col N, its feasible
set is exactly y-col N. Therefore for the uniform means

    E_inf=3pi min_beta sum_i T_i [y_i-(N beta)_i]^2.

For unnormalized velocity integrals instead, B_ii=T_i/(6pi) and the
residual weight is 1/T_i. Rank-deficient nuisance columns require their
column space or a pseudoinverse; if that space spans all data, the bound is
zero. More general overlapping/calibrated kernels require the true Gram
and, if singular, its range/feasibility conditions.

The Riesz solution is attained in the energy completion for these bounded
contrasts. Among smooth rapidly decreasing initial data this statement is
an infimum unless smooth attainment is separately established. It does not
assign individual unbounded readouts to every rough field. Smooth density
and finite-dimensional Gram approximation justify the same infimum.

For mu>0, the exact Fourier weight becomes
(omega²-mu²)^(3/2)/omega on omega>=mu. Its upper bound omega² proves the
Loewner enclosure G_mu<=G_0 for every vector contrast combination.
This is a necessary lower-energy bound, not mass-independent equality or
attainment. For independent modes with couplings alpha_j and shared energy,
the total Gram is sum alpha_j² G_mu_j<=q G_0, q=sum alpha_j². Replacing the
actual Gram by q G_0 therefore yields only a necessary lower bound unless
massless equality applies. Coupling and Q normalization are separate from
the unit-gradient mathematical energy used above.

## Additional nuisances and physical imports

Unknown constant additive baseline contributes its own nuisance column:
ones for normalized instrument means, clock durations for raw clock integrals.
With varying calibration, canceling the velocity moment need not cancel this
baseline. Two compressed means generally cannot cancel two independent
nuisance columns nontrivially. Known integrated baselines can instead be
subtracted; known-shape nuisance functions add corresponding response columns.
Errors in clocks, calibration or direction leave an initial-velocity moment
whose effect needs a velocity bound or a nuisance treatment.

The exact diagonal energy metric assumes one fixed spatial sampling point,
a massless gradient acceleration with stated normalization, and the reduced
linear velocity readout. A moving spacecraft, conformal time-derivative force,
multiple retarded endpoints, station proper clocks, changing calibration,
media, source forcing and tensor response cannot be absorbed into that metric
without their own derivation and error budget. Positive residual energy from
a conditional mathematical model is not a detected scalar energy: ordinary
measurement errors and unmodeled contributions also affect the residual.

## Independent execution

`independent_count_kernel_check_v1.py`, SHA-256
`1becb7f812e659c3cad271abd192765147fba16fcd5f2f174162bfe670431e2e`,
completed 109 controls with zero failures in 0.0833 seconds. Full results and
stdout/stderr are retained. There were no failed attempts suppressed.
The largest numerical equality error was 1.52e-13.

Controls cover unequal durations; actual gaps; polynomial, oscillatory and
nonsmooth absolutely continuous velocities; direct and matrix Grams; nonlinear
clock/calibration pushforward; known and unknown baseline effects; affine clock
reduction; the distinct dx/dtau definition; omitted clock/geometry witnesses;
vector cancellation and direct primitive identities; nuisance-rank cases;
weighted regression versus the contrast minimum; and independent Fourier
half-line Gram quadrature with analytic tail enclosures. The Fourier check
used constant unit directions varying between synthetic windows and a genuine
vector nuisance nullspace. These are independent mathematical controls,
not empirical tests, author-code mutation tests or proofs by finite sampling.
