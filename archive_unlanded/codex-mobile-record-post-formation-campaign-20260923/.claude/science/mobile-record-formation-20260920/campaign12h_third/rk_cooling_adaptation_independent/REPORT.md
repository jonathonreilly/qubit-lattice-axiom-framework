# Independent reconstruction: changing the target of a local RK cooler

Date: 2026-09-22. Conditional finite-model mathematics and one stipulated
Gaussian diagnostic. This report is sealed before any new author adaptation
note, code, result, context or seal is read. It is not a publication or audit
determination, and it supplies no axiom-native quantum implementation.

## Findings and indispensable premises

1. With the old jumps, the uniform state is stationary exactly when
   `delta=0` or the flippability count is constant on the component. Otherwise
   there is no pure stationary state; every stationary density has positive
   resolved jump intensity. A quantitative lower bound also rules out a
   vanishing long-time expected jump rate from any initial density. In this
   specified jump unraveling there are almost surely infinitely many jumps.
2. The stipulated weighted jumps do attract every density to psi_theta, for
   each finite real theta and finite connected physical component. A new
   weighted polynomial degree-lowering identity proves the required invariant-
   subspace exclusion. Splitting the jumps by m is essential to this proof and
   defines a different instrument; even at theta=0 it need not reproduce the
   original unresolved jumps.
3. The mismatched Gaussian bath has an explicitly mixed stationary state when
   U>0. Its Hamiltonian-quanta occupation diverges as s^(-1/2), reference-bath
   occupation as s^(-1), and stationary jump rate tends to gamma U/(8W).
   Retuning the oscillator ratio prepares the pure mode ground state, but
   requires the stipulated mode-dependent bath rather than following from the
   microscopic plaquette model.
4. In the specified periodic 24-link component, the numerical variational
   optimum is theta=0.0619383884167354. Its energy is -1.63415990848445,
   whereas the component ground energy is -1.64244259196795. The squared
   overlap is approximately 0.997439895836480. The variational state remains
   detectably different from an eigenstate. These are finite-component results.

All finite Lindblad rates below are strictly positive on the active jump
classes; theta is finite and real. The Gaussian calculation assumes gamma>0,
s>0, K,W>0 and U>=0. At gamma=0 there is no dissipative selection. At s=0 the
positive-frequency and damping assumptions fail. The finite-component
statements include frozen singleton components as trivial exceptions.

## 1. Old jumps under the detuned Hamiltonian

Let M=|C|, u=M^(-1/2) sum_c |c>, P0=|u><u|, and

    D = diag(d(c)) = sum_p P_p,
    P_p^- = L_p^dagger L_p = (P_p-X_p)/2,
    H_delta = 2J sum_p P_p^- - delta D,
    K_loss = sum_p gamma_p P_p^-.

The finite generator is `G=-i[H_delta,.]+sum gamma_p D[L_p]`, with real J and
delta and no additional terms. Connectivity and positive rates give

    ker K_loss = intersection ker L_p = span(u).

In particular `K_loss >= kappa (I-P0)` for some kappa>0 when M>1. The local
partial isometries satisfy L_p^2=0, including their coherent sum over spectator
pairs. The old dissipator annihilates P0, whereas

    H_delta u = -delta D u,
    G(P0) = i delta [D,P0].                                      (1)

Thus P0 is stationary iff delta=0 or d(c) is constant. These are genuine
exceptions: in either case the Hamiltonian differs from the previously
checked `2J sum P_p^-` by a scalar, so that finite attraction and finite
expected total cooling output follow from the earlier theorem. This holds
for real J; identifying that target with a ground state also uses the usual
J>=0 condition. A constant-flippability one-square component is an explicit
control, not a negligible corner case.

For any pure stationary density |v><v|, its purity derivative gives

    0 = -2 sum_p gamma_p (||L_p v||^2-|<v,L_p v>|^2).

Every summand vanishes, so v is an eigenvector of every L_p. Nilpotence forces
all those eigenvalues to be zero. Therefore v is proportional to u, and (1)
is the complete pure-stationarity test. When delta!=0 and d is not constant,
there is no pure stationary density. No uniqueness assertion for the mixed
stationary state is needed for the following bounds.

### A uniform positive long-time output bound

Set sigma_d^2=Var_u(d), and choose any

    C_G >= 2||H_delta-h I|| + 2 sum_p gamma_p ||L_p||^2             (2)

with real h. This bounds the generator's induced trace norm on Hermitian
operators. Also `||G(P0)||_1=2|delta| sigma_d`. For any stationary density rho,
write j(rho)=Tr(K_loss rho). Then

    2|delta| sigma_d <= C_G ||rho-P0||_1
                     <= 2 C_G sqrt(j(rho)/kappa),

and hence

    j(rho) >= kappa delta^2 sigma_d^2 / C_G^2.                    (3)

The same argument works without assuming convergence to a stationary state.
For the time-averaged density rho_bar_T, use
`G(rho_bar_T)=(rho_T-rho_0)/T` and `||rho_T-rho_0||_1<=2`. It yields

    E[N_jump(T)]/T >= kappa/C_G^2
                         * (|delta| sigma_d - 1/T)_+^2.          (4)

Thus the long-time expected mean output cannot vanish in the nonconstant,
nonzero-detuning case, for any initial density. This is a fixed-model bound;
neither kappa nor the resulting output lower bound is uniform in volume.

An entirely elementary choice is
`kappa >= gamma_min/(M-1)^2`: join every unordered pair of configurations
by a path of length at most M-1 and apply Cauchy-Schwarz to its differences.
The identity `sum_{a<b}|v_a-v_b|^2=M||v||^2` for centered v then bounds the
weighted graph Dirichlet form. One convenient choice in (2) is

    C_G = 4|J| P_count + |delta|(d_max-d_min) + 2 sum_p gamma_p,

where P_count counts the nonempty plaquette jump families. This follows by
centering the diagonal detuning at `(d_max+d_min)/2`. Tighter norm or gap
estimates may improve (3), but are not required for its strictly positive sign.

There is a stronger counting statement for the specified resolved jumps.
Let A=H_delta-i K_loss/2 be the no-jump effective Hamiltonian. If Av=lambda v,
then `Im lambda=-<v,K_loss v>/(2||v||^2)`. A real eigenvalue would force
v proportional to u, which would require H_delta u proportional to u. In the
case presently considered this is impossible. Every eigenvalue therefore
has strictly negative imaginary part, and finite dimensionality gives
uniform exponential no-jump survival decay. From every post-jump state the
probability of never jumping again is zero. Bounded total intensity prevents
explosion, so the total jump number is almost surely infinite as time tends
to infinity. This does not assert a particular almost-sure asymptotic rate or
make jump counts independent of the chosen unraveling.

### Exact finite control

The independently assembled three-square component has five configurations
and d=(1,3,2,2,2). At J=1, delta=1/5 and all three rates one, its full
25-dimensional complex Liouvillian has exact rank 24. The exact trace-one
stationary solution is Hermitian and strictly positive, certified by its
five exact positive leading principal minors. Its intensity is

    3470529320688444 / 529232036844402523
        = 0.0065576705094835385.

Its purity is strictly below one. Formula (3), with the conservative choices
above, gives the exact lower bound 1/338560. The uniform state's squared
Hilbert-Schmidt stationarity defect is exactly 4/125. The complete rational
stationary density, minors, purity and all controls are retained in
`FINITE_COOLER_RESULTS.json`. The delta=0 and constant-flippability controls
both retain the pure stationary target.

## 2. The weighted local construction

Write w_c=exp(theta d(c)/2)>0 and normalize psi from these amplitudes. For
one oriented class alpha=(p,m), r=exp(theta m/2) is constant, and w_b=r w_a
on each of its disjoint a->b pairs. The specified vectors are orthonormal:

    s_r=(a+r b)/sqrt(1+r^2),    d_r=(r a-b)/sqrt(1+r^2).

Therefore L_alpha^2=0, L_alpha^dagger L_alpha=P_alpha^- is a projection,
L_alpha psi=0, and connectivity gives

    intersection ker L_alpha = span(psi).                         (5)

The new Hamiltonian H_theta=sum h_alpha P_alpha^- annihilates psi. This
Hamiltonian is part of the supplied construction; it is not automatically
the detuned H_delta. Adding H_delta or any other arbitrary Hamiltonian to the
weighted generator is not covered. A pure target under such an addition
would still have to be an eigenvector of that Hamiltonian.

### Locality

A flip changes only the four links of p. Consequently

    m = sum_{q: q shares a link with p} [f_q(b)-f_q(a)],

where f_q is the flippability indicator. The contribution from p itself is
zero. Thus m is computable from the union of a bounded collar of plaquettes,
without measuring the extensive d(c). On the usual bounded-degree cubic
geometry there are at most 12 other incident plaquettes; more generally the
bound is the actual number sharing a link. It is this bounded local incidence
assumption, not an arbitrary abstract flip graph, that supplies physical
locality. The partition into oriented m classes is implemented by local
electric-basis projectors. It preserves the existing Gauss sector.

For example, on its class projector the local matrix can be written using
the distinguished raised-link Z and forward plaquette operator W as

    L_r = (-r Z - W^dagger + r^2 W)/(1+r^2).

The class projector recognizes both endpoints of each oriented pair; merely
using the signed increment evaluated at an un-oriented endpoint would not
implement that same pair projector.

### Attraction: a weighted polynomial proof

Uniqueness in (5) alone is not a proof of attraction. The fixed physical
displacement z_p remains necessary for the following new argument.

For any polynomial f on the ambient configuration coordinates, put
`v_f(c)=w_c f(c)`. Let T_p f(x)=f(x+z_p), Delta_p=T_p-I. Within a class of
constant r define

    g = r(I+r^2 T_p)^(-1)(I-T_p)f
      = -r/(1+r^2) sum_{k=0}^{n-1}
             [-r^2 Delta_p/(1+r^2)]^k Delta_p f,                 (6)

when f has degree at most n. The finite series is valid because Delta_p
lowers polynomial degree. Therefore g has degree at most n-1. On each pair,

    g(a)+r^2 g(b) = r[f(a)-f(b)],
    P_alpha^- v_f = L_alpha^dagger v_g.                           (7)

Both sides vanish off that class's pairs. These are weighted identities;
the unweighted coefficient and inverse operator would be incorrect for
r!=1. Constancy of r within the class is what makes g an ambient polynomial
of the asserted degree.

Let B=sum gamma_alpha P_alpha^-, H=H_theta and Q=H+iB/2. Suppose a nonzero
subspace S contained in psi-perp were invariant under every L_alpha and the
no-jump effective Hamiltonian H-iB/2. Then R=S-perp contains psi and is
invariant under every L_alpha^dagger and Q. Since B is strictly positive on
psi-perp, Q is invertible there. Its inverse preserves R intersect psi-perp:
this is a finite-dimensional invariant subspace on which Q is injective.

Induct on polynomial degree. Constants give v_f proportional to psi, hence
in R. Equations (6)-(7) and the induction hypothesis imply

    Q v_f = sum_alpha (h_alpha+i gamma_alpha/2)
                             L_alpha^dagger v_g  belongs to R.

This vector is perpendicular to psi. Subtract the psi component of v_f and
apply the inverse of Q on psi-perp to conclude v_f belongs to R. Polynomials
restricted to a finite set of distinct configurations span all functions on
that set; multiplication by the strictly positive w_c is invertible. Thus
R is the whole Hilbert space, contradicting nonzero S.

The finite target-orthogonal corner argument now applies: any surviving
corner trace would yield, by Cesaro averaging, a positive stationary corner
whose support is invariant under these jumps and the no-jump operator.
Zero leakage gives full support invariance, contradicted above. All densities
therefore converge to |psi><psi|. Finite dimension gives exponential decay
with model-dependent constants, and the integral of Tr(B rho_t) is finite.
This proves attraction for every finite real theta under the exact stated
generator. It is not an inference from a unique dark vector or a small-system
diagonalization. No bound uniform in volume or theta, and no theta=infinity
limit with vanishing amplitudes, is established here.

### Instrument and resource boundaries

Each L_alpha is a nilpotent partial isometry, so the previously checked fresh
two-state collision produces Kraus operators

    M0=I+(cos phi-1)P_alpha^-,    M1=-i sin phi L_alpha.

The single dissipative channel has the same exact semigroup parameterization;
overlapping classes plus H_theta require the stated small-step composition
limit. Class outcomes alpha may be retained. Revealing individual spectator
pairs is a further refinement and is not the same jump.

Importantly, even at theta=0, `sum_m D[L_(p,m)]` generally differs from
`D[sum_m L_(p,m)]`. The no-jump losses agree, but coherences between different
m alternatives differ. In the five-state control, a coherent superposition
of two difference vectors has an exact squared Hilbert-Schmidt difference
1/2 between these jump outputs. Thus this is a genuine apparatus change,
not an identity with the old cooler for all histories.

For the specified class-resolved process, expected total cooling clicks are
finite and their number is finite almost surely. Fresh no-click probes,
timing, export/storage, and any rule converting a click to permanent records
remain supplied resources. Finite expected clicks do not guarantee a finite
exact stopping certificate or a bounded deterministic storage capacity. The
local field cooler does not itself establish matter-pair formation, and the
rest-count dilation does not by itself conserve an arbitrary additional
interacting field energy.

At theta=2 log(2), the five-state target is proportional to (1,4,2,2,2).
The exact common dark dimension is one and the Liouvillian rank is 24 for
the independently chosen positive rates (1,2,3,4,5) and signed Hamiltonian
coefficients (2/3,-1,4/3,-5/3,2). All weighted identities through polynomial
degree four are checked exactly. On the larger component below, all 24
plaquettes have seven nonempty m classes, and the local computation of m
and amplitude ratios was checked over all 3456 oriented pairs.

## 3. Separate Gaussian diagnostic

This section is a supplied canonical mode with [q,p]=i, not a limit derived
from the finite spin-half model. Let g=gamma s, omega=sqrt(ab),

    Delta = a/r-b r,       D_g = g^2+4ab.

For V with entries Q=<q^2>, P=<p^2>, C=<{q,p}>/2, the exact dual equations are

    Qdot = -g Q+2a C+g r/2,
    Pdot = -g P-2b C+g/(2r),
    Cdot = a P-b Q-g C.                                           (8)

The first-moment drift is A=[[-g/2,a],[-b,-g/2]], with eigenvalues
`-g/2 +/- i omega`. Its stable Gaussian channel gives the unique stationary
Gaussian covariance

    Q = r/2 + a Delta/D_g,
    P = 1/(2r) - b Delta/D_g,
    C = g Delta/(2D_g).                                           (9)

One can derive the stationary Gaussian characteristic function directly from
the linear drift and noise integral. The stable drift sends the initial
characteristic-function argument to zero. In particular finite initial
second moments converge to (9); this calculation does not assume a Gaussian
initial state just to close the moment equations.

The determinant, stationary purity, energy, two different occupations and
resolved jump output are

    det V = (1+Delta^2/D_g)/4,
    purity = (1+Delta^2/D_g)^(-1/2),
    E = <H> = (a/r+b r)/4,
    n_H = E/omega - 1/2,
    n_0 = <b0^dagger b0> = Delta^2/(2D_g),
    j = g n_0.                                                    (10)

n_H counts excitations of the actual Hamiltonian oscillator. n_0 counts
reference-bath quanta and is the occupation entering the jump rate. They
are not interchangeable. The stationary covariance generally has a nonzero
C and is not the Gibbs covariance of H. Its purity formula uses the
stationary Gaussian state, not an arbitrary state with the same moments.

For the prescribed r=sqrt(K/W), set c=gamma^2+4KW. Then
`Delta=-U r`, `D_g=s(4KU+c s)` and

    E = sqrt(K/W)(U+2W s)/4,
    j = gamma K U^2 / [2W(4KU+c s)].                              (11)

For fixed positive U, taking the stationary state first and then s down to
zero gives

    Q -> sqrt(K/W)/4,
    P ~ U/[4 sqrt(KW) s],
    C -> -gamma/[8 sqrt(KW)],
    purity ~ 2 sqrt(W s/U),
    E -> U sqrt(K/W)/4,
    n_H = sqrt(U)/(4 sqrt(W s)) - 1/2 + O(sqrt(s)),
    n_0 ~ U/(8W s),
    j -> gamma U/(8W) > 0.                                       (12)

Thus finite positive-mode damping does not imply ground-state cooling under
this mismatch, and stationary output continues. The drift relaxation rate
gamma s/2 tends to zero, so (12) cannot be substituted for a fixed-time
small-s limit. No integration over a lattice mode density or physical photon
identification is supplied.

For U=0, Delta=0: the stationary state is the pure reference/Hamiltonian
vacuum, V=diag(r/2,1/(2r)), E=omega/2, and both occupations and the stationary
jump rate vanish. For gamma=0 the evolution is unitary and the selection
statement must be discarded. Retuning to `r_*=sqrt(a/b)` gives Delta=0 for
each fixed s>0, pure Hamiltonian vacuum and zero stationary output. Its
s-dependent coefficients are a new bath choice; this algebra does not
provide a spatially local or native microscopic realization of that bath.

The independent runner checks (8) directly in the exact Weyl algebra,
including its constant noise terms, without a Fock-space truncation. It then
checks the Lyapunov equation and all limits. The exact example
K=4,W=1,U=3,gamma=2,s=1/5 has

    (Q,P,C)=(7/13,109/52,-3/26),
    purity=sqrt(754)/58, E=17/10,
    n_H=9/16, n_0=45/26, j=9/13.

This also tests the factors of two and the sign of C. The retuned and U=0
controls are exact.

## 4. Finite weighted variational calculation

The independent geometry uses all 24 distinct positive-axis links of the
periodic 2x2x2 cubical complex, including distinct wrap links. It is not a
simple eight-vertex graph with only 12 undirected link qubits. The prescribed
seed is integer bit word 15798951 in the recorded ordering. Breadth-first
closure gives 864 configurations, all with zero Gauss charges and zero
reported plane flux. Each of the 24 plaquettes has 144 oriented pairs.
This enumerates one component, not the entire Gauss sector.

The exact flippability histogram is

| d | 4 | 6 | 8 | 10 | 12 | 16 |
| --- | --- | --- | --- | --- | --- | --- |
| number of states | 120 | 64 | 492 | 96 | 80 | 12 |

For each plaquette the m values are (-6,-4,-2,0,2,4,6), with pair counts
(4,22,24,44,24,22,4). Each plaquette has 11 overlapping plaquettes including
itself on this two-cell geometry. Full d differences agree exactly with the
local overlapping-plaquette computation for every pair.

Let q=exp(theta/2)>0, n_d count states, and e_t count oriented pairs with
d(a)+d(b)=t. Here

    (t,e_t)=(12,384),(14,480),(16,960),(18,672),(20,576),
            (22,96),(24,96),(26,96),(28,96).

The variational energy is exactly the rational function

    E(q)=[(J-delta) sum_d d n_d q^(2d)
                      -2J sum_t e_t q^t] / sum_d n_d q^(2d).      (13)

The numerator uses each oriented forward pair once; X contributes both
matrix entries, giving the explicit factor two. The runner isolates all
positive roots of the exact derivative polynomial. There is one positive
critical point, and both endpoint limits, 16/5 and 64/5, exceed it. Hence it
is the global optimum of this one-parameter family. The exact polynomial,
its complete factorization and rational root interval are saved.

| Quantity | Value |
| --- | --- |
| uniform energy | -1.6 |
| optimal theta | 0.0619383884167354179308422851 |
| optimal energy | -1.63415990848445210940479846 |
| component ground energy | -1.6424425919679508 |
| variational excess energy | 0.008282683483499254 |
| squared ground-state overlap, numerical | 0.9974398958364804 |
| variational eigenvector residual norm | 0.21031644375741435 |
| mean d, variational / ground | 8.34030126409349 / 8.416876197406662 |

The finite matrix is `H=(4/5)diag(d)-adjacency`. Numerical diagonalization
has ground-vector residual 8.51e-15. More strongly, treating the computed
strictly positive vector as an exact rational vector and applying the
Collatz inequalities gives the rigorous finite ground-energy enclosure

    -4781053331520493/2910940908924955
          <= E0 <= -234590294577373/142830133439430,               (14)

of width 1.74e-13. This uses connectedness and the nonpositive off-diagonal
entries of the exact Hamiltonian; it is not a heuristic residual bound.
The vector, squared overlap and variational residual remain numerical
quantities. The recorded root interval establishes global optimization
within the stated family, not exact ground-state representability.

In particular, the nonzero variational residual is an explicit warning
against replacing H_theta by H_delta in the attraction theorem. No
thermodynamic fidelity, preparation gap, phase identification, or relation
to the separately stipulated Gaussian mode follows from this calculation.

## 5. Reproduction, evidence and unresolved scope

The three standalone runners are `finite_cooler_check.py`, `gaussian_check.py`
and `variational_geometry_check.py`. Each completed on its first execution.
Full stdout, stderr and command/source receipts are retained; stdout matches
the corresponding result JSON byte for byte. The first two stderr files are
empty. The variational run retains one SciPy FutureWarning about the future
default output dtype of `sparse.diags` with integer input; the present output
is float64, as used for the numerical Hamiltonian. All complete result fields
and that warning were read. `VARIATIONAL_COMPONENT.npz` preserves the exact state list,
degrees and numerical vectors; the large Liouvillian on 864^2 matrix entries
was neither constructed nor claimed to have been solved.

The first sealing helper incorrectly assumed every stderr file was empty
and failed that bookkeeping assertion. Its submitted source, full traceback,
partial metadata, prior report draft and diagnosis are preserved under
`failed_attempts/seal_stderr_assumption/`. The repair records and authenticates
the warning rather than suppressing it. No scientific script, result,
parameter, tolerance or run changed. There was no failed scientific assertion.
Rejected logical shortcuts are preserved explicitly: uniqueness of
a dark vector is insufficient; the old polynomial identity cannot be used
with the wrong weights; m-resolved and unresolved instruments differ even
at theta=0; a high finite overlap does not make a variational state an
eigenstate; and stationary infrared formulas do not describe a fixed-time
limit with vanishing damping.

No external literature lookup was needed for the new deductions. The
unweighted local operator, its established-literature context and the
earlier invariant-subspace proof are reused only from the exact previously
reviewed packet. Principal source bindings are:

| Source | SHA-256 |
| --- | --- |
| previously reviewed unweighted note | 7fa8e6b7a84b3467b784283f596ef192ceab6fbc18172f18fd93e1d139a2791f |
| prior independent report | d72068c4dae9a210224f5c7217dc9b6ded91ea0422f7f14ec9ff1b659302747f |
| prior independent cooler runner | cce65c2ad05e2956bf1d9b5786435b07b1e99bb9705505a57b3b375172cffcc9 |
| prior independent cooler result | 0707122f13d02f7c283df20dd8f50543872f97266311b9c598ac93573fbba0e4 |
| prior completed comparison seal | 24abda952a7f728c5408dc5846dc4fdf7cc913c5552d12fe50b4a773c550eb81 |

The new source/evidence seal records all complete file identities. No author
adaptation artifact or seal contents were accessed before this seal; the
given author-seal hash was treated solely as an unopened identity. No primary
source, prior packet, Git, workflow, publication or audit state was changed.

The remaining obligations are outside this bounded reconstruction: general
Hamiltonian-compatible cooling beyond the specified parent H_theta,
volume-uniform gaps and resource efficiency, autonomous fresh-stream or
native-site implementation, and any microscopic derivation or thermodynamic
interpretation of the Gaussian diagnostic. They are not needed for the
finite conditional statements proved here.
