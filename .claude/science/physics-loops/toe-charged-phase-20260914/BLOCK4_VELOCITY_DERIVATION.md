# Working derivation: actual gauge/fermion speed logarithms

Author calculation, not yet a theorem proposal. Independent review pending.
Supplied continuous-time spatial lattice model; compact charged phase is NOT
assumed proved. No axiom or primitive modification. Literature comparators:
Anber-Donoghue 1102.0789v2 section 4 and Roy-Juricic-Herbut 1510.07650v2.
The calculation below uses its own physical A_0 convention.

## 1. Supplied free action and actual gauge inverse

Set lattice spacing one. The noncompact quadratic gauge action is
S_g = 1/2 integral [sum_i E_i^2 + c^2 sum_{i<j} F_ij^2],
E_i=partial_tau A_i - nabla_i A_0, F_ij=nabla_i A_j-nabla_j A_i.
Link-midpoint Fourier variables give qhat_i=2 sin(q_i/2),
Q=omega^2+c^2 qhat^2. In the gauge-fixing term
(partial_tau A_0+c^2 div A)^2/(2 c^2 xi), the true inverse is

D_mn(xi)=diag(c^2,1,1,1)_mn/Q
         +(xi-1)c^2 k_m k_n/Q^2, k=(omega,qhat).

At xi=1 it is diagonal. For positive xi and nonzero k it inverts the
positive gauge-fixed quadratic matrix; it is not a scalar denominator
inserted into an unrelated tensor ansatz. Verify this algebra directly.

A convenient two-component finite-range symbol is
h_0(k)=v[sin k_x sigma_1+sin k_y sigma_2
 +(2+zeta-cos k_x-cos k_y-cos k_z)/sqrt(1-zeta^2) sigma_3],
0<zeta<1, v>0. Define h_+(k)=h_0(k-b xhat),
h_-(k)=h_+(-k)^*, 0<b<pi; charges +e,-e, separately conserved
normal particle numbers, half filling. This is supplied model data.
All four nodes are (plus/minus b,0,plus/minus arccos zeta),
with local metric v^2 I, and each charge sector has two opposite chiralities.
Thus the parity-even long-wavelength polarization has four Weyl cones, or
N_D=2 four-component Dirac species, not four Dirac species. Opposite charge
signs square in the vacuum polarization. The anisotropic sigma_3 multiplier
is explicitly chosen to equalize the free cone speeds; it is not derived.

Peierls coupling every hopping gives the exact midpoint Ward identity:
qhat_j partial_j h(k) summed over j = h(k+q/2)-h(k-q/2),
with the temporal i omega identity added for D=i omega+h.
The action vertex is -e W, W_0=i I and W_j=partial_j h; thus
q.W=D(k+q/2)-D(k-q/2). This convention is used by the lattice checks.
The same expansion supplies the two-photon single-link vertex. Its omission
would invalidate the full lattice polarization Ward identity.

## 2. Independent continuum residue derivation

For one Dirac cone pair, use D_f(p)=i gamma_0 p_0+i v gamma_i p_i,
vertices gamma_0 and v gamma_i. The xi=1 gauge contractions weight the
temporal vertex by c^2 and the three spatial ones by one.
Feynman parameter x on the fermion denominator yields
V_x^2=x v^2+(1-x)c^2. The shifted numerator has temporal weight
(1-x)p_0 and spatial weight v c^2(1-x)p_i/V_x^2.
A four-dimensional radial logarithm is 1/(8 pi^2) log(Lambda/mu).

I_3 = integral_0^1 (1-x)/V_x^3 dx = 2/[c(c+v)^2],
I_5 = integral_0^1 (1-x)/V_x^5 dx
    = 2(2c+v)/[3 c^3 v(c+v)^2].

Clifford contraction gives temporal numerator c^2-3v^2 and spatial
numerator -(c^2+v^2). Expansion of the inverse averaged propagator fixes
the sign: delta D=e^2 integral Gamma S Gamma D_g, with S=-i slash p/p^2.
Consequently the coefficients in the inverse fermion propagator are

A_t=e^2(3v^2-c^2) I_3/(8 pi^2),
A_s=e^2(c^2+v^2)c^2 I_5/(8 pi^2).

The speed is the spatial/temporal coefficient ratio, so for
ell=log(Lambda/mu),

 dv/dell = v(A_s-A_t)
 = e^2(c-v)(4v^2+3vc+c^2)/[6 pi^2 c(v+c)^2].

The individual wavefunction factors are gauge dependent. For the longitudinal
part use q.Gamma=D_f(p)-D_f(p-q). The linear logarithm from
[D_p-D_{p-q}] S_{p-q} [D_p-D_{p-q}]
is proportional to D_p itself, since its linear part is -D_p after angular
integration; the quadratic external-D term gives no linear UV logarithm.
Thus it cancels from A_s-A_t. This needs a precise regulator and sign check.

For the photon, rescale spatial loop momentum by v and spatial gauge fields
by v. The standard Dirac trace/Feynman-parameter integral must be rederived
below rather than assumed. It gives the parity-even transverse logarithm
N_D e^2/(6 pi^2 v^3) times (P^2 delta_ab-P_a P_b), P=(p_0,v p).
Thus the electric coefficient changes by
 B_E=N_D e^2/(6 pi^2 v),
and the absolute magnetic coefficient c^2 changes by
 B_B=N_D e^2 v/(6 pi^2).
After electric normalization,

 dc/dell=N_D e^2(v^2-c^2)/(12 pi^2 v c),
 de/dell=-N_D e^3/(12 pi^2 v).

The last relation requires the charge Ward identity; the spatial lattice
vertex and wavefunction normalization must be matched, not presumed from a
scalar propagator. These are one-loop residues, not an all-orders phase proof.

## 3. Coupled truncated one-loop flow

Let r=v/c and g=e^2/c. Algebra gives

 dr/dell = -g(r-1) H_N(r)/(12 pi^2),
 dg/dell = -N g^2(r+1/r)/(12 pi^2),
 d log c/dell = N g(r^2-1)/(12 pi^2 r),
 H_N(r)=2(4r^2+3r+1)/(r+1)^2+N(r+1), N=N_D.

H_N>0 for r>0. The speed ratio stays between its initial value and one.
Since r and 1/r stay bounded, g is comparable to 1/(1+ell), its integral
diverges and r tends to one. The individual speeds remain between the
initial two speeds because dv points toward c and dc toward v. They converge
to a positive common value. This is a theorem of the displayed truncated ODE,
not yet a theorem of the full quantum field theory.

Near equality, g~6 pi^2/(N ell) and
r-1 scales as ell^[-(N+2)/N]; for the four-Weyl carrier N=2, the exponent is 2.
The exact local linearized solution about fixed common c uses
r(ell)-1=[r(0)-1][1+N g(0)ell/(6 pi^2)]^[-(N+2)/N].
Higher-loop control and threshold matching are still to be supplied.

## 4. Hard next steps

Prove the lattice-to-cone logarithmic matching with a bounded infrared
remainder, accounting for Peierls vertices, seagulls, other cones, continuous
frequency and the gauge zero. Derive the photon normalization independently.
Establish which physical dispersion coefficient is defined; massless charged
infraparticle structure forbids casually claiming an exact isolated pole.
Check finite mass thresholds and finite renormalization/marginal anisotropy:
leading-log attraction does not fix UV matching constants or finite-scale
agreement. Do not declare the original staggered-carrier target closed.


## 5. Actual lattice logarithm: power-counting proof to complete

Near a simple cone write D=D_0+R with R=O(|k|^2), uniformly in the
continuous frequency. For rho=sqrt(omega^2+|k|^2), small enough spatial k
gives ||S||+||S_0|| <= C/rho, ||S-S_0||<=C,
||partial S-partial S_0||<=C/rho, and
||partial^2 S-partial^2 S_0||<=C/rho^2 by the resolvent identity.
Peierls vertices differ from their cone values by O(rho), vertex derivatives
are bounded, and the true lattice gauge covariance differs from its cone
covariance by O(1). Derivatives with respect to external fermion momentum
therefore have remainder O(rho^-3) relative to the homogeneous degree -4
self-energy logarithm. Second external derivatives of the photon bubble have
the same integrable O(rho^-3) remainder. Four-dimensional radial measure
is rho^3 d rho, so each remainder integrates to a finite O(kappa) value.

The fermion tadpole from the two-photon hopping vertex has no infrared
logarithm: its derivative multiplies only D_g=O(rho^-2). The photon seagull
is independent of its external momentum for single-link Peierls coupling;
it cancels the zero-momentum bubble term but has no q^2 logarithm. At large
frequency all needed differentiated integrands are absolutely integrable.
Away from every cone the fermion line is regular. In the fermion self-energy,
other cone singularities have a nonsingular gauge line and are integrable.
In the photon bubble all four cones contribute and each weighs one half of
a Dirac species. These estimates concern fixed microscopic parameters with
separated simple nodes, not a limit in which nodes merge.

The exact full lattice polarization identity can be proved without a grid:
contract its bubble with (q_0,qhat), use q.W=D_+-D_-, and shift the periodic
BZ/continuous-frequency variables. For a spatial index nu the remaining
vertex difference is
W_nu(k+q/2)-W_nu(k-q/2)=qhat_nu partial_nu^2 h(k).
It cancels the seagull -delta_mn integral tr[S partial_nu^2 h]. For the
constant temporal vertex the difference is zero. This identity relies on
both diagrams, not just a transversality check at selected momenta.
A shell cutoff by itself need not preserve the exact finite remainder Ward
identity; its logarithmic residue is the covariant cone result.

Current actual-matrix checks: direct derivatives of the lattice fermion
self-energy (including momentum-dependent vertices) approach both analytic
wavefunction residues. Analytic second external derivatives of the actual
Peierls photon bubble approach the per-Weyl electric and magnetic residues;
longitudinal logarithmic residue vanishes. The finite shell remainders are
nonzero and are not discarded as numerical error.

## 6. General metric perturbations: candidate linearized tensor result

At the common Euclidean metric choose units c=v=1. Let f_a be each fermion's
symmetric traceless infinitesimal frame perturbation (nine components) and
h the photon metric frame perturbation. The metric is I+2f_a or I+2h.
Antisymmetric frame changes are spin-basis rotations; a trace is a field/unit
normalization. Common f_a=h is a change of coordinates, not a mismatch.

The parity-even quadratic Maxwell tensor has Riemann symmetries after the
constant axion term is set aside. Decompose it into scalar normalization,
traceless Ricci part delta odot h, and Weyl part C (ten components). Here
(delta odot h)_mnrs=delta_mr h_ns+delta_ns h_mr
                   -delta_ms h_nr-delta_nr h_ms.
Its Ricci contraction is 2h for traceless h. The tensor C has zero Ricci
contraction and represents the non-metric photon polarization part.

At linear order the leading continuum residue is O(4) covariant. The
symmetric traceless representation is irreducible, so its linear response
coefficient is fixed by the previously derived temporal/spatial deformation.
There is no equivariant linear map from the Weyl representation to a
symmetric traceless two-tensor. This representation argument needs an
explicit tensor/gamma contraction check before use as a claimed result.

For species charge q_a e and multiplicity n_a in Dirac units (one Weyl has
n_a=1/2), define kappa=e^2/(6 pi^2), W=sum_a n_a q_a^2. The candidate
linearized flow, after removing common isotropic normalization, is

 df_a/dell = 2 q_a^2 kappa (h-f_a),
 dh/dell = kappa sum_a n_a q_a^2(f_a-h),
 dC/dell = -W kappa C,
 dkappa/dell = -W kappa^2.

The photon formula follows independently because a fermion determinant in
its own frame adds a Maxwell quadratic form of that frame. Canonical field
normalization divides the existing photon tensor by 1+W kappa d ell;
its Weyl component therefore decays. It is not sourced at first order by a
fermion metric perturbation. The fermion response to a photon Weyl tensor
vanishes at this order by its Ricci contraction.

For every tensor component the metric equations form a weighted star graph.
The detailed-balance weights are n_a/2 on f_a and one on h. For E=(1/2) sum_i w_i (y_i-y_bar)^2, their weighted
quadratic energy has derivative
 E'= -kappa sum_a n_a q_a^2 (f_a-h)^2.
The conserved mean is (sum_a n_a f_a+2h)/(sum_a n_a+2).
If all charges are nonzero, the unique zero direction is a common metric.
All other eigenvalues lambda_j of the constant positive graph matrix give
powers [1+W kappa_0 ell]^(-lambda_j/W).

For four unit-charge Weyl cones, n_a=1/2 and W=2. The common matter average
versus photon mode has lambda=4 and exponent 2. The three independent
inter-cone metric differences have lambda=2 and exponent 1. The ten photon
Weyl-tensor components also have exponent 1. Thus an isotropic shared-fermion
ansatz misses slower linearized modes. This does not mean that every such
perturbation is independently realizable in the particular nearest-neighbor
symbol; that microscopic matching remains a condition to be stated.

## 7. Finite lattice matching is not a constant infrared drive

If the exact local shell remainder produces a forcing bounded by
C kappa(ell) exp(-p ell), p>0, a mismatch mode solves
 y'=-lambda kappa y+f(ell).
Its integrating-factor expression is
 y(ell)=[1+W kappa_0 ell]^(-lambda/W)
        [y(0)+integral_0^ell [1+W kappa_0 s]^(lambda/W) f(s) ds].
The integral converges absolutely. The lattice correction changes the finite
matching constant but does not shift the massless truncated flow's asymptotic
fixed metric by a constant. This statement requires the decaying forcing;
a permanent marginal source or a new mass threshold is a different problem.
The full-BZ finite constant and physical finite-scale mismatch remain open.

## 8. Observable caution

The speed parameters here are the characteristic coefficients of the
renormalized local one-loop two-point action. Analytic continuation gives
its characteristic cone. They are not a proof of an isolated massless charged
pole, a microscopic front velocity, or a fully controlled interacting spectral
threshold. A charged infraparticle and possible decay cuts require separate
analysis. The calculation can supply logarithmic RG coefficients without
claiming those stronger observable statements or the original blocked-taste
framework carrier bridge.


## 9. Direct angular derivation of the full tensor coefficient

The representation argument in section 6 can be replaced by an explicit
contraction. Write a small gauge kinetic deformation K_mnrs with Riemann
symmetries in the action (1/4) K_mnrs F_mn F_rs. Its gauge-invariant inverse
quadratic perturbation is M_ns(q)=2 K_mnrs q_m q_r, with M q=0.
At the reference Feynman gauge, delta D_g=-M/q^4. The coefficient of
i gamma_b p_a in the linear fermion correction is e^2/(8 pi^2) times

 T_ba = average_S3 [2 M_ba - delta_ba tr M + 2 q_b q_a tr M].

This follows from tr(gamma_b gamma_n gamma_a gamma_s)/4
=delta_bn delta_as-delta_ba delta_ns+delta_bs delta_na; the extra term
with M q vanishes by transversality. Unit-sphere moments are
<q_i q_j>=delta_ij/4 and
<q_i q_j q_k q_l>=(delta_ij delta_kl+delta_ik delta_jl
                  +delta_il delta_jk)/24.
With R_ns=sum_m K_mnms, substitution gives exactly

 T = (4/3) R -(1/3) tr(R) I.

For a metric deformation K=delta odot h with tr h=0, R=2h, so
delta f=e^2 h/(3 pi^2). For a photon Weyl deformation R=0, delta f=0.
This derives the response for every traceless symmetric component without
assuming that a numerical scalar-speed test covers it. A simultaneous
f=h is a linear coordinate change; covariance of the leading cone residue
and the charge Ward identity then give the own-fermion term -e^2 f/(3 pi^2).

A finite exact check of the angular contraction can use the 24 unit vectors
consisting of the eight signed coordinate vectors and the sixteen vectors
(plus/minus 1/2,plus/minus 1/2,plus/minus 1/2,plus/minus 1/2), all with
weight 1/24. Their second and fourth moments agree exactly with the displayed
sphere moments; every polynomial entering T has degree at most four.
This is an exact cubature identity, not a sampled-sphere proof.

The metric/Weyl analysis concerns the parity-even marginal kinetic sector.
The supplied normal carrier's Hall cancellation and node separation must be
kept distinct from a theorem excluding every relevant perturbation or pairing
instability. Arbitrary independent cone frames are an effective-sector probe;
which ones a chosen microscopic hopping family realizes must be stated.


## 10. Massive threshold: derivation and precise limit

This section is a separately supplied massive Dirac comparator at a common
reference metric, not a claim that the normal Weyl carrier dynamically gaps.
A gauge-invariant mass or pairing channel would require its own microscopic
matching. Below the masses the charged fields leave the active massless EFT.

The Dirac trace and Feynman parameter shift give the scalar photon quadratic
coefficient (up to a momentum-independent UV subtraction)

 Pi(Q^2)=N e^2/(2 pi^2) integral_0^1 x(1-x)
          log[Lambda^2/(m^2+x(1-x)Q^2)] dx.

One way to check the factor is the transverse form before radial integration:
8 N e^2 integral_0^1 x(1-x) dx integral d^4 l/(2 pi)^4
 (l^2+m^2+x(1-x)Q^2)^(-2) times (Q^2 delta_mn-Q_m Q_n).
The momentum-subtracted screening loss is positive and bounded by

 0 <= Pi(0)-Pi(Q^2) <= N e^2 Q^2/(60 pi^2 m^2),

using log(1+t)<=t and integral x^2(1-x)^2 dx=1/30.
Its logarithmic derivative relative to the massless charge coefficient is

 F(z)=6 integral_0^1 [x^2(1-x)^2 z/(1+x(1-x)z)] dx,
 z=Q^2/m^2.

Thus 0<F(z)<1, F(z)<=z/5, F is increasing, and F tends to one as z tends
to infinity by dominated convergence. The small-z derivative is 1/5.
In a momentum-subtraction charge convention the one-loop common-metric
charge equation is kappa'=-N F(exp(-2s)) kappa^2 below Q=m,
s=log(m/Q). Its total remaining polarization flow is finite:

 integral_0^infinity F(exp(-2s)) ds
 =3 integral_0^1 x(1-x) log[1+x(1-x)] dx <=1/10.

Consequently 1/kappa(infinity)-1/kappa(Q=m)<=N/10 in this comparator.
A mass-independent subtraction scheme can keep a formal running parameter,
but physical low-momentum polarization has the displayed decoupling. There
is no continuing charged massless logarithm below all charged thresholds.
This does not assign a massless speed to an integrated-out massive fermion.

For a mode with massless exponent p, the available interval L above a
threshold gives attenuation [1+W kappa_0 L]^(-p) within the displayed
linearized flow. To reduce a nonzero mismatch by a factor R<1 requires
L >= [R^(-1/p)-1]/(W kappa_0). This is a conditional scale requirement,
not a numerical empirical prediction. Neither the initial mismatch, matching
constant nor the charged thresholds are derived from the framework axioms.

The main lesson is two separate facts: bounded irrelevant lattice remainders
do not create a constant shift of the massless asymptotic fixed metric; a
finite charged interval does not force exact metric equality at its endpoint.
All-orders stability, finite matching and physical-observable identification
remain open. None of these conditions is a proven axiom contradiction.


## 11. Exact longitudinal kernel at the lattice cone

Use lattice D=i omega+h, with internal momentum (omega,K-q), external
frequency zero and bare cone h(K)=0. The exchanged photon has frequency
-omega. Its contracted vertex is
 X=-i omega I+sum_j qhat_j partial_j h(K-q/2)
  =D_external-D_internal=-D_internal.

For external derivative a, let d0=partial_a D_external and
di=partial_a D_internal. Then X'=d0-di, S'=-S di S. Direct multiplication
therefore gives

 -partial_a(X S X)=2 d0-di.

The longitudinal inverse-propagator correction is this matrix times
(xi-1)e^2 c^2/Q^2. At the cone its leading part is d0, giving the same
wavefunction logarithm (xi-1)e^2/(8 pi^2 c) in time and every spatial
coefficient. Thus the characteristic-speed logarithm cancels for arbitrary
fixed xi. Finite lattice off-shell coefficient ratios can still depend on
xi; they are not promoted to physical velocities. This exact reduction is
checked against the unreduced matrix derivative in the private runner.

## 12. Source formula consistency, not imported authority

Kostelecky-Lane-Pickering equation (28), in both the preprint and retrieved
published text, agrees with the derived metric/Weyl differential coefficients
after normalization. Its printed integrated k_F expression (34) is not used:
on a nonzero Ricci-free k_F with c=0, (28) gives k_F proportional to Q^-1,
whereas the displayed (34) leaves that component constant. This narrow
substitution is recorded as a source-formula discrepancy, not as a claim to
have audited the paper or found a new physical effect. The present photon
normalization and direct ODE solution supply their own evidence.


## 13. From Taylor residues to actual one-loop two-point asymptotics

The perturbative object is the infinite-spatial-volume Brillouin-zone
integral and continuous-frequency integral of the displayed supplied action.
Take that volume limit at the perturbative-integral level first. No limiting
interacting Gibbs state is inferred. For a small Euclidean external momentum
p at a fixed separated cone, write the integral as |q|>A|p| plus its complement,
with fixed A>2 and a fixed small outer cone radius kappa.

For the fermion self-energy the homogeneous integrand has degree -3.
Its linear external Taylor term has degree -4 and integrates to the derived
matrix coefficient times p log(kappa/|p|). The next Taylor remainder is
bounded by C |p|^2 |q|^-5; its outer integral is O(|p|).
In the inner region, rescaling q=|p|u bounds both the unexpanded integrand
and its zero-momentum subtraction by O(|p|): the singularities |u|^-2 and
|u-p_hat|^-1 are locally integrable in four dimensions, uniformly for unit
Euclidean p_hat. Other cones and the lattice remainder supply finite O(p)
matching terms. Therefore

 Sigma(p)-Sigma(0)=linear_log_matrix(p) log(kappa/|p|)+O(|p|).

The sign of Sigma here must be fixed by defining it as the correction to the
inverse propagator, consistent with sections 2 and 11. A finite Sigma(0)
can shift the bare cone and is a matching/counterterm datum; changing that
location at order e^2 does not change the order-e^2 logarithmic residue.

For the photon bubble the homogeneous integrand has degree -2. Subtract its
constant and linear external Taylor terms. The quadratic term has degree -4
and gives the transverse tensor log. The cubic remainder is bounded by
C |p|^3 |q|^-5 and its outer integral is O(|p|^2). The inner region scales as
O(|p|^2); both translated simple fermion singularities are integrable. Hence

 Pi(p)-Pi(0)-p_a partial_a Pi(0)
   =quadratic_transverse_log_tensor(p) log(kappa/|p|)+O(|p|^2).

The seagull cancels the constant term under the full Ward identity and has
no quadratic logarithm. Possible finite parity-odd linear response is a
separate lower-dimensional term; the supplied conjugate pair cancels its
free Hall response. No arbitrary parity-odd perturbation is silently excluded
from the general microscopic law by the parity-even tensor calculation.

These estimates provide a continuum logarithm from the actual lattice
vertices and propagators, with an integrable remainder. They do not evaluate
the finite O(p) or O(p^2) matching constants. They also do not continue the
error estimate uniformly onto Minkowski decay thresholds or prove an exact
massless charged pole. The proposed speed flow is the leading-log local
characteristic flow, with that precise observable boundary.

## 14. Payload and phase boundary

The gauge action used for this one-loop calculation is a supplied noncompact
quadratic action with Peierls-coupled fermions. Its continuous link variables
are not an already-derived finite-payload gauge phase. A formal weak-field
expansion of a compact model may share these perturbative coefficients only
after its action and normalization are matched; perturbative equality alone
cannot establish its infrared phase. None of the preceding campaign's
unmerged compact or finite-time approximation theorems is needed as a premise
for this block's one-loop integral calculation.
