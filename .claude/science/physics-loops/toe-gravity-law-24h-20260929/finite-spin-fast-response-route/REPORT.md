# Finite-spin transfer of the actual absorbing first-mark response

Root research,2026-09-30. Candidate for focused independent checking; not formal
review, audit or retained status. The supplied one-hole compensated fast law
has a volume-uniform, all-fast-time comparison with its rotor response on
polynomial-field-bounded inputs. The complete finite-spin diagonal compensation
and the original event labels are retained. This is not the microscopic
bare-Omega local-limit theorem.

## 1. Exact domain, law and target

Use the physical charge/field carrier and supplied cubic law at main
30a9461ee19a49b99fa6628fe942f08e504e8903, with selected procedures
7146fe17a76de41badcaca3c3c7cac6d11eb2a00. The actual compensation source is
LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT, SHA256
c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b.
All prior imports are source-bound in SOURCE_IDENTITIES.json. Main/open
searches and the exact matched-prior distinctions are in CONTRACT and the
PRIOR_SEARCH files. No proposed foundation or new primitive is adopted.

Work on Z3 in the finite-change physical Hilbert representation over Omega,
or on even cubic tori with L>=max(28,4k). Fix W=1 and global N_B=k, where
k is finite, odd and positive. This safe torus restriction includes the
previous small-k regime and the checked periodic height theorem. All charge
and electric superpositions in that sector are permitted. For integer S>=1,
let C=S(S+1) and embed the physical spin box in the common rotor space.
The input density is spin-supported and obeys Tr(Q^4 rho)<infinity, where

 Q=1+sum_links |E_link|.

On Z3 this diagonal operator is closed from its finite-change word core.
The total-field moment is a global finite-excitation condition, not a local
energy-density hypothesis. The rate constants depend on k,delta,kappa but
not on S, volume or the positions/diameters of the finite excitation.

With unsigned actual normalized-spin hops F_a,S, define

 C_S=sum_a [F_a,S* F_a,S+D_a,infinity-D_a,S] Q_a,
 H_S=C_S+[F_S,F_S*],
 Delta_S=sum_a(D_a,infinity-D_a,S)Q_a,
 Hbar_S=H_S-Delta_S.

Q_a is the actual eighteen-neighbor occupancy gate, not the electric Q.
D_a,S is exactly the diagonal part of F_a,S*F_a,S. Global divergent F on
Z3 is never used as an operator: Hbar_S is defined by the checked one-hole
cancellation below. The rotor H_infinity has Delta_infinity=0.

Let J_S=(j_m,S)_m be the original stacked marks, either all resolved signs
per edge or each original unnormalized coherent edge sum. These are two
separate instruments. G_S=J_S*J_S has the same diagonal loss in either
case, but their output maps are not identified. Put

 A_S=-i delta H_S-kappa G_S/2, K_S=sqrt(kappa)J_S,
 Z_S(t)=exp(t A_S).

The fast time here is the leading grade-preserving time u=t_physical/epsilon².
No higher normal-form terms, dressed jumps or recurrent microscopic source
are included by this definition. Removing the W=1 scalar penalty phase
changes no first-event output density.

For a horizon T, define the actual first-event amplitude map

 V_S,T psi = Z_S(T)psi direct_sum [K_S Z_S(t)psi]_(0<=t<=T).

Its second summand lies in L2 time with the direct sum of the ORIGINAL marked
output Hilbert spaces. The actual quantum-classical instrument is the Bochner-L1 density
K_S Z_S(t)rho Z_S(t)*K_S* with its discrete mark corners, together with
the terminal no-event state. It is obtained directly from these amplitudes.
The proof device does not make the unobserved quantum amplitudes an extra
record. Arbitrary finite timestamp bins are later contractions of this map.

## 2. Weighted differences on the actual carrier

Extend a normalized spin link shift by zero outside its physical box:
U_S|m>=sqrt(1-m(m+1)/C)|m+1> for -S<=m<S, zero otherwise.
Its adjoint has the corresponding lowering amplitude. This extension leaves
the spin box invariant and agrees there exactly with the physical model.
For every integer m and sign sigma, including exterior values,

 |u_S,sigma(m)-1|<=m(m+sigma)/C.

Inside the box this is1-sqrt(1-x)<=x; outside the allowed transition the
right side is at least1. Integer m(m+sigma) is nonnegative. Hence for each
actual charge-controlled elementary hop or birth,

 ||(f_S-f_infinity)Q^-2||<=2/C.

Each elementary word changes Q by at most1, so
||Q² f_S Q^-2||,||Q² f_infinity Q^-2||<=4. Telescoping a two-hop product
therefore gives the bound10/C against Q^-2. Charge/vacancy/gate projections
commute with Q and have norm at most1.

The exact one-hole block identity is

 P_h Hbar_S P_h=P_h[F_h,S F_h,S*-
                         sum_(a:dist(a,h)=2) F_a,S*F_a,S]P_h,
 P_a Hbar_S P_h=P_a[F_a,S,F_h,S*]P_h, a!=h.

The diagonal block has at most684 two-hop terms. Distinct-bond paths in
the offdiagonal commutator cancel, leaving row and column word budgets60.
These formulas remain true at spin boundaries. Since Q commutes with the
hole-position projectors, block Schur applied after right multiplication by
Q^-2 proves

 ||(Hbar_S-H_infinity)Q^-2||<=7440/C.

The actual diagonal difference is positive. Each oriented A-B link appears
only once; every gate is at most1. Its coefficient is m(m+sigma)/C inside
the spin box, and1 outside where the extended hop vanishes. Thus globally

 0<=Delta_S<=2Q²/C.

This does NOT bound the extensive operator norm of Delta_S. It implies only
its specified relative bound. Combining gives the convenient larger bound

 ||(H_S-H_infinity)Q^-2||<=10000/C.                    (1)

The stacked mark difference has at most twelve resolved contributions per
one-hole input. Each mark is a weighted partial isometry; different signs
of a coherent edge have orthogonal output charge ranges. Therefore the
same estimate, without changing the observed labels, gives

 ||(J_S-J_infinity)Q^-2||<=2sqrt(12)/C<=8/C.

The losses are diagonal. Summing the twelve nonnegative squared-weight
differences gives, conservatively,

 ||(G_S-G_infinity)Q^-2||<=24/C.                       (2)

Both actual losses satisfy0<=G_S,G_infinity<=12. Equations(1)-(2) yield

 ||(A_S-A_infinity)Q^-2||<=a0/C,
 ||(K_S-K_infinity)Q^-2||<=b0/C,
 a0=10000delta+12kappa, b0=8sqrt(kappa).                (3)

These estimates do not assume the spin evolution stays away from its field
boundary. They include the exact boundary zeros and all diagonal compensation.

## 3. Domains and the checked rotor input

On the common Z3 space, Delta_S is a nonnegative self-adjoint multiplication
operator and D(Q²) is contained in its domain by the relative estimate.
Hbar_S is bounded self-adjoint with norm at most744. Thus H_S is self-adjoint
on D(Delta_S). Adding the bounded nonnegative loss defines a contraction
semigroup. The spin-supported subspace is invariant. On finite tori the
same construction is bounded at each fixed volume, with the same estimates.
The auxiliary exterior extension has no effect on the original finite-spin
output.

The already focused-checked finite-global-k rotor theorem supplies

 ||Z_infinity(t)||<=C_k exp(-gamma_k t),
 ||Q² Z_infinity(t)psi||
    <=C_k exp(-gamma_k t)R2(t)||Q²psi||,                (4)
 R2(t)=1+8bt+4b²t², b=5C_k delta M, M=1092.

The periodic version gives this under the declared safe L restriction; Z3
uses the finite-change representation. The full polynomial graph-domain
proof was independently checked, including the preservation and continuity
of D(Q²). Its constants may be very large, but are finite at each fixed k.

Define explicit finite numbers

 L1=C_k[gamma_k^-1+8b gamma_k^-2+8b² gamma_k^-3],
 L2=C_k[integral_0^infinity exp(-2gamma_k t)R2(t)^2 dt]^(1/2),
 B_k=a0 L1+b0 L2.                                    (5)

For example R2² has coefficients1,16b,72b²,64b³,16b4; the integral is the
finite sum of its jth coefficient times j!/(2gamma_k)^(j+1).

## 4. A passive output estimate controls every horizon

The exact norm-loss identity gives

 ||Z_S(T)v||²+integral_0^T ||K_S Z_S(t)v||²dt=||v||².  (6)

First prove this on the self-adjoint generator domain and extend by density;
bounded K_S and contraction justify the integral. Thus V_S,T is an isometry,
including for the common-space extension. The same identity holds for rotors.

For psi in D(Q²), Duhamel gives

 Z_S(t)psi-Z_infinity(t)psi
 =integral_0^t Z_S(t-s)(A_S-A_infinity)Z_infinity(s)psi ds. (7)

This is legitimate even on Z3: (4) makes the forcing graph-continuous and
integrable, and the relative Delta bound puts the rotor path in D(A_S).
Integration of the differentiated product proves(7) on this domain; no
uniform operator bound for Delta_S is assumed.

For each s, propagate that forcing vector by the SPIN law from s to T,
including its terminal state and every first-event output after s. By(6)
the norm of this vector in the common terminal-plus-record output space is
exactly the forcing norm. Minkowski then bounds the propagated difference
by the L1 norm of the forcing. The direct output-map difference is the L2
function (K_S-K_infinity)Z_infinity(s)psi, with zero terminal component.
Consequently

 ||(V_S,T-V_infinity,T)psi||
 <=integral_0^T ||(A_S-A_infinity)Z_infinity(s)psi||ds
    +[integral_0^T||(K_S-K_infinity)Z_infinity(s)psi||²ds]^(1/2)
 <=(B_k/C)||Q²psi||, every T>=0.                       (8)

This is why no unproved spin survival-tail integral is needed. It is a
comparison of the entire absorbing output, not a compact-time generator
estimate with a growing time substituted into it.

All bounds tensor with an arbitrary spectator identity. For any physical
spin-supported density rho, including an arbitrary ancilla, purify rho and
use the rank-one trace-distance bound for two isometries. For the continuous-time output, apply the rank-one inequality pointwise
and Cauchy in time, together with the terminal component. The sum is at
most (||V_S,T psi||+||V_infinity,T psi||) times the amplitude difference.
This directly controls the Bochner-L1 cq norm; it does not invoke a normal
diagonal-dephasing map on trace class over a nonatomic L2 space. Partial
trace and discrete mark dephasing are contractions. Writing I_S,T for the
original first-event instrument therefore gives

 ||I_S,T(rho)-I_infinity,T(rho)||_1
 <=min(2,2B_k/C sqrt(Tr[(Q^4 tensor I)rho])), uniformly T. (9)

Finite timestamp bins or marginal fields/records obey the same bound. This
does not replace a coherent edge mark by resolved signs: the argument is
applied separately to either original J.

Since the rotor survival tends to zero, the terminal component of(8) also
implies

 lim_(T->infinity) Tr[Z_S(T)rho Z_S(T)*]
 <=min(1,B_k²/C² Tr(Q^4 rho)).                         (10)

The limit exists by norm loss. It bounds any missing first-event probability;
it does not identify an asymptotic surviving quantum state. The first-event
measure over all positive times has the corresponding bounded test-output
comparison by taking the monotone horizon limit. No waiting-time or output
field moment bound for spin is inferred from a small total missing mass.

## 5. Scientific gain and remaining obligations

For families with uniformly bounded Tr Q^4 rho, (9) gives an actual O(S^-2)
first-event response comparison uniform over all fast horizons and the allowed
volumes. More generally Tr Q^4 rho=o(C²) suffices for convergence. A fixed
rotor input can be approached by normalized physical spin-box compressions;
those commute with Gauss and particle-sector projections, and the ordinary
initial trace-distance error is added separately. No moving high-field family
outside this weighted condition is silently covered.

The new step prices finite-spin boundaries and the extensive diagonal
compensation using the checked rotor response. It does not prove a uniform
unweighted finite-spin gap or exact absorption for every finite S. The carrier,
law, preparation and physical clock remain supplied model assumptions. Global
fixed k is not an extensive dilute-density condition. Positive-time conditional
source clusters, the microscopic electric moment bound, multiple simultaneous
holes, dressed jumps, recurrent births and signed local comparison remain
separate obligations. In particular this lemma is strictly weaker than M4.

The proof is frozen for a focused check before extensive downstream reuse.
No formal milestone verdict, retained status or new PR is implied.
