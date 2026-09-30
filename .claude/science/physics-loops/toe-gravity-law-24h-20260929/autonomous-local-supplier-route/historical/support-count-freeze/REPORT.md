# An autonomous local clock that supplies the original marked rotor process

Author construction, 2026-09-30; conditional supplied-model mathematics.
This is not primitive adoption, a formal review gate, or a source landing.

**Result at the stated scope.** On a fixed finite cubic torus and a finite
horizon, the ORIGINAL compensated rotor process from Omega, with either its
resolved labels or its coherent labels, has an explicitly finite, positive,
time-independent Hamiltonian approximation. The source factors and original
record maps are kept. There is a separately supplied finite clock and a bank
of original-label records at each A center. Every interaction acts on one
original star and its center apparatus, or on an original magnetic pair.
The clocks supply both timing and energy. No global energy projectors, clock
resets, phase corrections during the run, or externally timed collisions are
part of the implemented Hamiltonian.

This proves locality on an enlarged tensor lattice with finite apparatus at
each center. An explicit M2 block encoding below gives finite geometric range,
but that range and the interaction order grow with the requested accuracy and
resources. It does NOT prove a bounded-strength, fixed-range, bounded-arity
implementation on the unchanged one-M2-per-site graph. Nor does it derive
this carrier, Hamiltonian, preparation or readout from the minimal axioms.
The numerical resource certificate is intentionally extravagant: existence
with a complete ledger, not a practical machine or an optimal bound.

The main new step in this route is the simultaneous original-process,
finite-positive-clock, local-support and endpoint-energy argument. Momentum
clocks and their finite approximations have substantial prior literature;
SOURCES.md identifies actual constructions inspected and the narrower claim.

## 1. Frozen source and finite target

Source authority at freeze is main 9d15f404c63ff5b9d877e2bdc06ea8713493ffb4.
The original-law argument was read at PR9345
fe51bf1728b625dc0133256f43e7783afb11f7d8; its landed argument is unchanged.
Only status, runner pointer and a reproduction appendix differ. The other
matched clock/supply mathematics is unchanged from the initially searched
e75578f7136401d4bd750131671aed9212c06291. On an even cubic torus
of side L>=24, let N=L^3/2. There are N A sites and N B sites. The supplied law
and its original jump operators are

    h = K_s D + A,          A = delta H4 = sum_p A_p,
    A_(a,c) = -2 delta S_ac* S_ac,       S_ac = F_c F_a P,
    D = sum_(a->b) (1-n_b) E_ab(E_ab-q_a),
    B_(a,b,sigma) = P j_(a,b,sigma) F_a P.

Use fixed source units with hbar_planck=1 and the actual nonnegative source
couplings. Clock position below has units of time, not lattice distance.

The hard-core record algebra, integer links, all A charges +/-1, B charges
0,+/-1, Gauss constraint div E=q-1_A, charge N, compensator, K_s,delta,kappa,
Omega, and readout are supplied imports. A link is stored at its B endpoint.
An original B is supported on the radius-one star of its A center. It moves
the old A charge q to an empty B_d and creates charges sigma,-sigma at A,B_b,
where d differs from b; E_ab increases by sigma and E_ad decreases by q.
The resolved instrument has 12N labels. The coherent instrument has 6N labels
and jump B_(a,b,+)+B_(a,b,-), with no normalization and no sign resolution in
an environment. Fix ONE of these choices throughout.

Actual source bounds, valid in every later birth sector, are

    ||A_p|| <= 288 delta,        v := ||A||_upper = 2592 delta N,
    ||B_res||^2 <= 9,            ||B_coh||^2 <= 18,
    ||Gamma_a|| <= 80 kappa,     Gamma_a=kappa sum_(m at a) B_m* B_m.

The last bound is the PR9345 center-incidence estimate; it is not inferred
from the sum of the individual B norms. Hence g:=sum_a||Gamma_a||<=80kappa N.
The earlier weighted rotor proof deliberately uses g_w=300kappa N; these
are different bounds for different estimates, not a silent constant change.

Take a product cutoff |E_e|<=R. Compress each original A_p and B_m onto this
box and use Gamma_(a,R)=kappa sum B_(m,R)* B_(m,R). In particular,

    A_(p,R) = P_R A_p P_R,

NOT a product built from individually truncated F's. Intermediate excursions
in the original pair word must remain. These compressed maps have the same
local supports and preserve Gauss constraints. Write h_R=K_s D_R+A_R and
shift h_+=h_R+v I>=0. A scalar shift does not change records or transfers.
Useful bounds are

    Qmax = 1+6NR,
    hbar = 2 K_s Qmax^2 + 2v >= ||h_+||, ||h_R||,
    Pbar = g_w (316 K_s Qmax^2+2v) >= ||P_R^current||,
    P_R^current = kappa sum_m [B_m* h_R B_m - {B_m*B_m,h_R}/2].

The accepted rotor-process bridge and its independently checked product-box
transfer give errors eta_rot in full binned history/state, E_rot in source
mean energy, and errors in source energy/current second moments. They apply
to this actual initial Omega and all subsequent original marks, not only to
the first birth. For a reproducible sufficient cutoff: M_birth=N/2,
b=1+2M_birth, x=(v+g_w/2)T, y=g_w T, and

    bM = sqrt(sum_(j=0)^M_birth y^j/j!),
    X_p = bM sum_(l>=0) (b+4l)^p x^l/l!,
    Y_p = bM sum_(l>=ell+1) (b+4l)^p x^l/l!,
    R = 2M_birth+4ell+8,
    eta_rot <= 4Y_0,       E_rot <= 4(2K_s X_2+v)Y_0.

The proof uses [N_B,h]=[N_B,Gamma]=0 and [N_B,B]=2B, so at most N/2 births
can occur; it does not assume a rate independent of history or forbid the
reversible magnetic paths. Every word with total field variation <=R is
unchanged by the product box, so the same discarded-word tail controls it.
The full weighted domain/current statements remain those of the frozen
bridge; this route adds bounded-target apparatus errors to them.

## 2. Original collision maps and actual records

Choose n bins, tau=T/n, with 80 kappa tau<=1/2. At center a let

    K_(a,0)=sqrt(I-tau Gamma_(a,R)),
    K_(a,m)=sqrt(tau kappa) B_(m,R).

Introduce a blank flag F_(a,k) with d_F=13 levels in the resolved case or
d_F=7 in the coherent case. A second zero-free-energy register E_(a,k) has
the same dimension. A finite local unitary U_(a,k) has ready column

    psi |0>_F |0>_E -> sum_(m including 0) K_(a,m) psi |m>_F |m>_E.    (2.1)

This is an isometry since sum K* K=I. First complete the single-flag column
sum_m K_m psi |m>_F to U_flag separately in its finite local Gauss blocks,
leaving spectator link coordinates fixed. Let C_copy be the local modular
copy permutation |f,e> -> |f,e+f mod d_F>. Choose the FULL unitary

    U_(a,k)=C_copy (U_flag tensor I_E) C_copy*,
    C_record=span{|m>_F |m>_E : m=0,...,d_F-1}.              (2.1a)

It has ready column (2.1) and preserves C_record. Completion and the copy
permutation are supplied local controls. Tracing E gives precisely the
original classical mark instrument; in the coherent case E copies only the
original edge label, never sigma. There is no hidden measurement resolving
the coherent sum.
Different (a,k) use fresh initially blank registers; all registers are retained
physically. A positive spectral logarithm on this local finite space gives

    exp(-i G_(a,k))=U_(a,k),               0<=G_(a,k)<=2pi I.        (2.2)

Its spectral calculation is local to one star and its records, not global
source-energy diagonalization. G need not commute with h_R; its failure to
commute is exactly what the clock supplies energy for.
Choose its logarithm by the same copy conjugation of a positive logarithm
of U_flag. Then G preserves C_record exactly. All terms of the implemented
Hamiltonian preserve the product of these matched-record subspaces.
Consequently tracing all E makes the F bank EXACTLY diagonal in the original
label basis at every time, including partial pulses and finite-clock errors.
This exact classical output statement does not assert exact record permanence.
For an effective logarithm with a separated branch cut, one may first choose
a computable common phase of U whose finite spectrum avoids 1, and then use
the logarithm with values in (0,2pi). This changes (2.1) only by one common
phase and leaves its instrument exactly unchanged. Such a phase is found by
testing a dense list for a certified positive spectral distance from 1.

Order centers a=1,...,N within each bin. The ideal discrete process applies
these U's in that order and then exp(-i tau h_R). Interpret nonzero F flags
as the actual label sequence in that bin, in that order, dropping zeros.
This is an explicit classical interpretation of actual labels; no data
decoding or replacement observable is inferred. Histories with two or more
continuous-time events in one small bin are accounted for in the error.
On the history-append space the collision and splitting bounds give

    delta_sweep <= T tau c,     c=7g^2+4 hbar g,   g=80kappa N.    (2.3)

The center Taylor remainder is <=7tau^2||Gamma_a||^2, the cross-center
remainder <=4tau^2 sum_(a<b)||Gamma_a||||Gamma_b||, and the split with free h
costs <=4tau^2 hbar g. CPTP telescoping gives (2.3), including references and
retained original histories. The frozen local-supplier proof was independently
checked before this report was completed. It supplies this finite-target
collision estimate, not the new autonomous-clock conclusion.

## 3. A static local program and its ideal translation-clock proof

Assume T>0; T=0 requires no apparatus. Set circle length L_c=4T and
omega=2pi/L_c. Put one clock at each A center. The analysis clock is
L2(circle) with P=-i d/dx, Fourier modes exp(i m omega x), m in Z.
It is NOT the implemented apparatus: its unbounded-below spectrum will be
removed in section 4. The initial clock wavefunction is the product of

    beta(x) = [L_c(2k0+1)]^(-1/2) sum_(m=-k0)^k0 exp(i m omega x).

For 0<sigma<=L_c/2 its position probability outside |x|_circle<=sigma obeys

    theta <= 1/[(2k0+1) sin^2(pi sigma/L_c)]
          <= L_c^2/[4(2k0+1)sigma^2].                         (3.1)

This follows directly from the finite geometric sum. All clock phases are
prepared around zero once. The state is a product across centers and with
the source/blank records; no intercenter entanglement or stored trajectory
correlations are assumed. The phase reference/preparation is nevertheless
a supplied, consumed resource.

Let m_g=Nn. Choose s<=tau/(8N+4). In bin k=0,...,n-1 put the center-a pulse
at t_(a,k)=k tau+2as. Its nonnegative periodic triangle g_(a,k) has support
[t_(a,k)-s,t_(a,k)+s], height 1/s, area 1, Lipschitz constant 1/s^2 and total
variation 2/s. The pulses are ordered and disjoint except at zero endpoints.
At each grid boundary j tau every triangle vanishes throughout the circle
neighborhood of radius s. At each center the sum over its n triangles is
bounded by 1/s.

Replace the triangles by the positive Fejer convolution of degree M:

    f_(a,k)=F_M*g_(a,k),
    F_M(x)=[L_c(M+1)]^(-1)
            [sin((M+1)pi x/L_c)/sin(pi x/L_c)]^2.

Each f is nonnegative, of Fourier degree M, integral one and supremum <=1/s.
Also sum_k f_(a,k)<=1/s and TV(f)<=2/s. Its first circular moment obeys

    mu_M := integral |x|_circle F_M(x) dx
          <= L_c[1+ln(M+1)]/[2(M+1)].

For an elementary proof use F_M<=min((M+1)/L_c,
L_c/[4(M+1)x^2]) and split at L_c/[2(M+1)]. Consequently

    rho_1 := ||f-g||_1 <= L_c[1+ln(M+1)]/[(M+1)s],
    rho_inf := ||f-g||_infty <= L_c[1+ln(M+1)]/[2(M+1)s^2].   (3.2)

Using 1+ln u<=2sqrt(u), u>=1, gives the simpler upper bounds
2L_c/[s sqrt(M+1)] and L_c/[s^2 sqrt(M+1)], respectively.
The actual stored Fourier coefficients, rather than a black-box pulse, are

    fhat_j=(1-|j|/(M+1)) exp(-i j omega t_(a,k))
              sinc^2(j omega s/2)/L_c,       |j|<=M,

and zero otherwise, with sinc(0)=1. The compressed matrix entry indexed by
clock modes u,v is fhat_(u-v).

The analysis Hamiltonian is

    H_infty = h_+ + sum_a P_a + V,
    V = sum_(a,k) f_(a,k)(X_a) G_(a,k),
    0<=V,           ||V||<=v_c:=2pi N/s.                    (3.3)

It is selfadjoint on D(sum P_a), by bounded perturbation. Its exact
characteristic solution, for initial coordinate vector y, is

    Psi_t(y+t 1) = [product_a beta(y_a)] U_y(t) psi,
    i dU_y/dt = [h_+ + sum_(a,k) f_(a,k)(y_a+t)G_(a,k)] U_y.

This is a time-ordered solution: no commutation of h and G is presumed.
The unconditional joint clock-position density translates exactly even
after source/clock correlations form. This follows from unitarity on each
characteristic, or pointwise trace cancellation. A postselected trajectory
need not have that marginal.

On the event that every |y_a|<=sigma, translation in L1 and TV(f)<=2/s give
||U_y(t)-U_0(t)|| <=4pi m_g sigma/s, uniformly for 0<=t<=T. The bad-position
probability is at most Ntheta. Comparing purifications and then tracing clocks
gives the trace-norm bound

    delta_jitter <=8pi m_g sigma/s +4sqrt(Ntheta).             (3.4)

Comparison of f and g gives delta_smooth<=4pi m_g rho_1. Under the triangles,
neglect h only on the interval from the first pulse's start to the last
pulse's end within a bin (length 2Ns). The remaining initial guard has length
s. Moving this guard to the end and restoring the omitted free time costs
at most (4Ns+2s)hbar in vector norm per bin. Thus the conservative bound

    delta_pulse <=16 m_g s hbar                              (3.5)

controls the difference from the ordered collision sweep with total free
evolution tau. All pulse timing above describes fixed coefficients of (3.3),
not a sequence of external actions during operation.

## 4. Implemented finite clocks: positive compression and exact Dyson support

Choose K_c>k0 and let Pi_K project one clock onto -K_c<=m<=K_c. Implement

    H_(C,a)=omega sum_(m=-K_c)^K_c (m+K_c)|m><m| >=0,
    F_(a,k)^K=Pi_K f_(a,k)(X_a) Pi_K >=0,
    V_K=sum_(a,k) F_(a,k)^K G_(a,k) >=0,
    H_AUT=h_+ +sum_a H_(C,a)+V_K >=0.                         (4.1)

This is a finite, time-independent Hamiltonian. F is the ordinary positive
Toeplitz compression. It is NOT a cyclic replacement of the Fourier shifts.
Its norm obeys ||V_K||<=v_c. The original h_R remains present throughout.
Clock ground energy is zero; adding K_c omega is only a scalar in the
comparison with H_infty, but is included in the physical preparation budget.

In the interaction picture of h_++sum P, each insertion of V changes one
clock momentum by at most M. Source and reference dynamics change no clock
momentum. Starting in the product band |m_a|<=k0, every Dyson word and every
prefix with at most r insertions lies inside the finite clock space whenever

    K_c>=k0+Mr.

For these orders the finite and infinite coefficients agree EXACTLY.
With T_j(z)=sum_(l>=j) z^l/l!, the two remaining norm-convergent Dyson series
therefore give, uniformly for 0<=t<=T,

    vector error <=2T_(r+1)(v_c T),
    delta_cut <=4T_(r+1)(v_c T).                             (4.2)

This also establishes the required clock-domain comparison: the ideal
generator is selfadjoint by bounded perturbation, its interaction-picture
Dyson series converges in operator norm, and equality of the low-order words
is on the explicitly specified initial band. No differentiation of an
incorrect wrapped position/momentum pair or unproved rotor LR hypothesis is
used. The finite model needs no unbounded operator domain at all.

Clock-independent contractions/isometries at fixed grid times leave the
momentum-word argument intact. Expanding the intervals gives total ordered
simplex volume T^l/l!, so the same bound holds when comparing corresponding
passive grid tests. This mathematical process comparison does not add those
tests to the autonomous closed-system energy ledger for free.

Combining the preceding bounds, the entire reduced history/source output
under corresponding passive original-record tests at fixed grid times is within

    eta_total <= eta_rot + delta_app,
    delta_app := T tau c +16m_g s hbar +4pi m_g rho_1
                 +8pi m_g sigma/s+4sqrt(Ntheta)+delta_cut.    (4.3)

Use the accepted rotor moment errors plus hbar delta_app for source mean
energy, hbar^2 delta_app for its second moment, and Pbar delta_app and
Pbar^2 delta_app for source current mean and quadratic second moment.
These are bounded-observable additions after the rotor truncation, not a
claim that trace distance alone controls an unbounded observable. Arbitrary
energy-injecting source interventions are not covered by the rotor bridge.
Here current moments mean those of the original source-current expression
evaluated on the approximating source state at grid times. They are not
moments of the generally pulsed derivative i[H_AUT,h_R], and no new
selfadjoint extension or measurement law for an unbounded current is asserted.

## 5. Full energy ledger, including controller and residual interactions

The apparatus free energy is H_C=sum_a H_(C,a). Its initial mean is
N K_c omega, its maximum is 2N K_c omega, and its initial variance is
N omega^2 k0(k0+1)/3. Flags and their copy registers have zero free spectra.
All coupling energy is in V_K, not silently assigned to zero-cost switching.
The initial total mean is <h_R>_Omega+v+N K_c omega+<V_K>_0,
bounded above by hbar+N K_c omega+b0 below; it includes controller interaction
energy as well as the clock reserve and supplied source preparation.
The total positive Hamiltonian is conserved exactly, and

    -Delta <H_C> = Delta <h_R> + Delta <V_K>.                 (5.1)

Total conservation alone would be insufficient. Here the last term is small
at the actual observation boundaries. For sigma<s, at any jtau in [0,T],
the analysis translating density and the endpoint zeros of every triangle
give

    0<=<V>_(jtau) <= b0:=2pi m_g rho_inf +v_c Ntheta.

Using the joint finite-clock trace bound for the bounded V gives

    0<=<V_K>_(jtau) <= b0+v_c delta_cut,
    |Delta <V_K>| <=2b0+v_c delta_cut                       (5.2)

between time zero and any grid endpoint. Initially the finite state is
exactly in the projected band, so only the final endpoint needs the cutoff
term. The bounds are deliberately conservative despite V_K>=0.

Combining with the original rotor energy bridge proves the source-supplier
ledger

    |-Delta <H_C> - Delta <h>_original|
       <= E_rot +hbar delta_app +2b0+v_c delta_cut.          (5.3)

The original source mean increment also equals its integrated original
current on this finite horizon by the accepted weighted-domain theorem.
This does not prove convergence of an instantaneous clock-current operator
or equality of work distributions, and it does not identify a positive source
gain on every branch. Clocks can gain energy on branches; they are finite
energy/coherence resources, not catalysts or stationary reservoirs.

The closed run retains F and E quantum registers. Discarding E yields an
exactly classical F register by (2.1a), with original-process error (4.3).
There is no extra dephasing operation needed to obtain that output channel.
There is also no need to perform active intermediate projection in the run.
If an observer actually dephases or reads F at a grid boundary, free h_R and
H_C commute with that operation, but V_K need not. Its additional energy
change must be charged to that measurement apparatus. Positivity and the
same pointwise pulse bound limit each such change by
2(b0+v_c delta_cut); it is NOT declared zero. Grid-test trace accuracy and
the no-intervention closed ledger (5.3) are distinct claims.

The finite apparatus need not have exactly monotone N_B or exactly permanent
old flags: small Fejer tails can recouple completed gates, and their unitary
completions include reverse actions off the ready subspace. The complete
history bound controls these effects over [0,T]. The monotone birth grading
used for rotor truncation belongs to the original target process, not to a
new exact irreversible law for this closed finite apparatus.

## 6. Explicit finite resource choices

For requested apparatus trace accuracy alpha>0 and endpoint interaction
allowance epsilon_E>0, taking smaller alpha if necessary so alpha<=1, choose

    n >= max(1, 2Tg, 5T^2 c/alpha),    tau=T/n,  m_g=Nn,
    s <= min(tau/(8N+4), alpha/[80m_g(hbar+1)]),
    sigma <= min(s/2, alpha s/(80pi m_g)),
    vbar=8N/s >= v_c,
    theta_* <= min(alpha^2/(1600N), epsilon_E/(8vbar N)),
    k0 = ceil(L_c^2/[8sigma^2 theta_*]),
    D0 = ceil(max(160m_g L_c/(alpha s),
                  64m_g L_c/(epsilon_E s^2))),
    M=D0^2-1,
    dcut=min(alpha/5, epsilon_E/(4vbar)),
    k >= max(ceil(6vbar T), ceil(log_2(8/dcut)), 1),
    r=k-1,                  K_c=k0+Mr.                     (6.1)

For entirely rational arithmetic take sigma= min(s/2,alpha s/(320m_g));
this uses pi<4. Since k>=6vbar T and e<3,
T_k(v_cT)<=2(e v_cT/k)^k<=2^(1-k). Thus delta_cut<=2^(3-k)<=dcut.
The five process contributions in (4.3), grouping both jitter terms, are
each <=alpha/5. Equations (3.1)-(3.2) give
2b0+v_c delta_cut<=3epsilon_E/4. All parameters are explicit and finite.

The actual-source example takes L=24, N=6912, K_s=delta=kappa=T=1 and the
independently certified rotor cutoff R=1346132804, whose five retained
rotor errors are <2^-100. Choose

    alpha=1/[1000(1+hbar^2+Pbar^2)],  epsilon_E=1/1000.

The exact rational script check_resources.py verifies the new resource
inequalities.
It uses the sharper g=552960 for sweeps and the earlier g_w=2073600 for
weighted/moment bounds. It yields n with 111 decimal digits, m_g with 115,
M with 1118, and K_c with 1344. One clock uses 4463 qubits under binary
encoding; the dominant cost is the 111-digit bank of fresh records per site,
not the clock's binary register. Each added source moment error is <1/1000,
the endpoint interaction allowance is <=3/4000, and the combined mean ledger
error is <2^-100+1/1000+3/4000. These are existence bounds with enormous
costs, not an efficiency claim. Clock energy and coupling bounds are

    <H_C>_0=N K_c omega,
    ||H_AUT||<=hbar+2N K_c omega+vbar.

The static program contains m_g positive logarithms (the same center map can
be repeated on different records) and at most m_g(2M+1) real Fourier
coefficients. All original matrix entries, square roots, logarithms and
Fejer coefficients are finite computable data for computable source inputs.
A loose star dimension is d_star=2[3(2R+1)^6]^6. Dense storage of all local
G matrices would need at most 2m_g(d_star d_F^2)^2 real entries, in addition
to those Fourier data; formula sharing can reduce this bound. These matrix
constructions are specified finite resource imports, not computations that
were performed by the small verification jobs.
No claim of economical compilation/preparation is made. A generic finite
state-preparation circuit for each clock is an explicit possible import;
the packet has only 2k0+1 equal Fourier amplitudes, needs no intercenter
entanglement, and its mean/variance are given above. Preparation and static
Hamiltonian fabrication are paid resources, not autonomous derivations.

Finite coefficient precision is allowed: a total operator-norm error zeta
in the implemented finite Hamiltonian costs at most 2Tzeta in trace norm;
initial trace error epsilon_p adds epsilon_p. Endpoint ledger errors must
also include the actual perturbation's interaction energy (at most 2zeta
for a bounded perturbation) and any initial energy error, bounded by the
finite total norm times epsilon_p. Positivity can be retained by positive
matrix-factor approximations or a further scalar shift. This is not a
claim that a large norm permits an accuracy-independent preparation cost.

## 7. Geometry, explicit M2 encoding, and its limitation

On the supplied logical tensor graph each D term touches an original edge;
each A_p touches the union of two A stars whose centers have distance two;
and each clock pulse term touches one star, that center's clock, and its
one flag/copy pair. None uses the whole torus or a clock shared globally.
Its coupling norm is <=2pi/s per center after summing the local pulses.

For a literal tensor product of M2 sites, use the fixed computational-basis
encoding of each finite factor: A uses one qubit, B uses two (one unused
code), each of the six integer links at B uses
q_E=ceil(log2(2R+1)) qubits, one clock uses
q_C=ceil(log2(2K_c+1)), and each record uses q_F=4 resolved or 3 coherent.
At each coarse A cell allocate

    b_A=1+q_C+2n q_F,             b_B=2+6q_E

qubits. Place them lexicographically in a disjoint cubic block of side
a_block=ceil_cuberoot(max(b_A,b_B)). The fine torus has side L a_block.
Original physical source observables are the explicit factorwise encoded
operators; each mark is the basis value of its own record register. The
map back to original charge/link/record factors is this stated local basis
isometry, not a global or dynamical decoding lemma.

Extend each local encoded matrix by zero outside its local legal codes;
extend free clock energies nonnegatively and preserve all legal-code
subspaces. The resulting original-product code is invariant. Magnetic
terms remain bounded below by -v in total, so the same scalar shift makes
the full extension positive. Positivity of compressed clock potentials
and G is preserved. Thus (4.1) is an exact engineered finite-qubit
Hamiltonian realization of the enlarged tensor model on its prepared code.
On the fine graph its interaction diameter is at most 7a_block: a magnetic
pair has coarse diameter four, with at most three additional block widths
for internal coordinates. A pulse uses at most five block widths. The
number of qubits touched by a pulse is at most
13+36q_E+q_C+2q_F; a magnetic pair touches at most 24+66q_E.

This encoding explicitly changes the microscopic geometry and uses many-body
terms. In the certified example a_block and the range have 38 decimal
digits. It does not establish unchanged microscopic range, bounded arity,
uniform local dimension/coupling, or the native M2 carrier selection.
If those are additional target requirements, a further locality compiler
with identity-on-source preparation/readout and its own energy/controller
ledger remains a substantive missing theorem. This report does not invoke
universal simulation as a replacement for that theorem.
Assuming such a compiler without proving its original-factor channel,
preparation and full-energy bounds would be a target-strength import for
that stronger microscopic version, not a consequence of this construction.

## 8. Exact and numerical discriminators; claim boundary

check_clock.py enumerates 9720 legal actual cubic-star birth words and
checks their Gauss and count action. It also checks 27 exact Gaussian-integer
interaction-picture Dyson words for finite-band coefficient agreement.
A cyclic-shift negative control produces the wrong clock commutator boundary
entry -9 at K_c=4; the ordinary unwrapped compressed shift has the right
commutator. An additional exact 9-by-9 integer-matrix control verifies the
matched-record code commutator and a nonzero transition between its labels.
These are actual-source/clock controls, not a full-Hilbert brute
force enumeration or a replacement law.

A separate explicitly labeled clock-module fixture has h=diag(0,2),
G=I-X, f=(1-cos x)/2, k0=2 and time 0.6. Its K_c=6,8,10 errors against a
K_c=32 reference are respectively 7.91e-6, 1.67e-8, 2.04e-11, below the
proved Dyson tail bounds. At K_c=10 the energy changes are

    source       +0.03277574467294,
    clock        -0.06870793908688,
    interaction  +0.03593219441394,
    total         1.8e-15.

This is a decisive control against replacing (5.1) by free-energy conservation
at arbitrary times. It is not numerical evidence that this two-level fixture
is the original rotor law. The largest matrix dimension is 130. The job used
1.455 wall seconds, 0.142 CPU seconds and 30.3 MB; the exact resource job used
0.0038 wall seconds, 0.0019 CPU seconds and 17.9 MB. Both had threads capped
at one and ran within their declared prices: 10 CPU seconds/200 MB and
5 CPU seconds/100 MB respectively, each with a 120-second wall ceiling.
No full-torus matrix is built.

The proved finite approximation has actual original marks, later births,
waiting-time information only at the chosen bin resolution, a positive
finite apparatus, autonomous operation over [0,T], local enlarged-cell
interactions, and a complete mean-energy ledger. It does not give exact
continuous timestamps, an infinite-time irreversible Markov reservoir,
permanent records under indefinite recurrence, a stationary/catalytic
clock, microscopic fixed-range native implementation, branchwise work
statistics, or a foundational source selection. Its target-dependent
imports and these residuals are explicit; the construction is submitted
for independent mathematical/source checking before substantive reuse.
