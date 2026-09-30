# Independent check of the physical threshold variational upper bridge

September 30, 2026. Focused mathematical check, not a formal review or audit.
No blocking error was found in the frozen author's stated upper-variational
claim. The pair normalization, volume-uniform remainder, compact-correction
limit, and concrete improvement survive the independent reconstruction below.
This does not supply a matching lower equation of state, a fixed-number
theorem, a condensate, or an on-shell scattering amplitude.

The checked author report has SHA256
`0c4ef9acc1332700e3210b85b8c190eaf7cc115abd8c850a2101ef10eb75aee3`.
This conclusion is bound to those bytes and the dependencies in
`SOURCE_BINDINGS.json`. No author file was edited. No author code was read,
imported, or executed. No formal PASS or claim-status change is issued.

## Independence and dependency boundary

Before opening the new report, code, or output, I read the contract, the
complete current-main native density note, the native stability definition,
the checked four-particle threshold proof and independent check, and the
checked strict-positivity extension. I also revisited the earlier independent
quartic and coercivity checks. The complete landed density note supplies the
coercivity details; this check does not repeat its box-partition computation.

`PRECOMPARISON.md` was frozen at 04:28:06 UTC with SHA256
`265155c264651ffd89e57fd541f9f3cef209118557d672363e7b681a56316810`.
It independently derives the construction, mixed Taylor estimates, identical
pair factors, compact approximation, limit order, coherent coercivity bound,
and the proposed one-word correction. The contract had already exposed the
target formulas, selected word, and source amplitude. This is independence
of derivation and implementation, not a blind discovery of the word or a
claim of historical novelty. The author's report and output were read only
after this freeze. The new literal action routine was written separately.

The current-main source read is
`docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md`
at `30a9461ee19a49b99fa6628fe942f08e504e8903`, SHA256
`7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0`.
Selected procedure revision remains
`7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. The mathematical inputs remain
supplied model assumptions; no axiom or primitive-selection inference occurs.

The reused threshold input concerns the physical infinite-lattice N=4,
total-momentum-zero translation-orbit space. It establishes a bounded
nonnegative H4, a finite collision source F, a finite zero-energy inverse
quadratic form on that source, and the relaxed 15-channel threshold form.
It does not assert a bounded inverse on all l2 or an l2 zero-energy minimizer.
Its separately checked extension establishes strict positivity for fixed
positive mu,tau. The previous independent quartic calculation supplies the
bare E-pulse coefficient; it is not recomputed here for all polarizations.

## Actual operator and physical normalization

Each site is a qubit with b=|0><1| and n=b* b. Distinct sites commute and
b squared is zero. Let d_i(x)=b_(x+e_i)b_(x-e_i),

    QE1=(d1-d2)/sqrt(2),
    QE2=(d1+d2-2d3)/sqrt(6),
    QTij=(b_(x+e_i)-b_(x-e_i))(b_(x+e_j)-b_(x-e_j))/2.

The actual supplied Hamiltonian is

    H0=mu N-2mu sum PE-mu sum PT+V3+Wtau,
    V3=mu sum_x n_x binom(m_x,2),
    m_x=sum_(d in G) n_(x+d),
    G={+/-2e_i, +/-e_i+/-e_j},
    Wtau=tau sum_(x,j,A) (QA(x+e_j)-QA(x))* (QA(x+e_j)-QA(x)).

Both mu and tau are strictly positive. The checked full-carrier SOS is
H0=A+mu D+Wtau, where D=(1/2)sum n_x(m_x-1)(m_x-2). The local grouping
has at most 25 sites and norm at most h=182mu+240tau. This follows from the
onsite/attraction bounds 1+16+12, the 153 unordered neighbor-pair terms in
V3, and fifteen gradient squares bounded by 16tau each. It is a local bound.

Put R=(QE1,QE2,QT12/sqrt(2),QT13/sqrt(2),QT23/sqrt(2)) and
C*=sum_(x,A) z_A R_A(x)* for ||z||=1. The exact q=0 Gram gives
||C* Omega|| squared=V, while H0 Omega=H0 C* Omega=0. These are physical
hard-core identities; there is no assumed bosonic pair algebra.

For a compact orbit vector chi, let chi_lift=sum_(sigma,t) chi_sigma
|S_sigma+t>. Define J=(1/sqrt(2))sum_(sigma,t) chi_sigma W_(S_sigma+t)*,
X=J-J*, and Y=C*-C. On each finite torus the state

    psi(u)=exp(u squared X) exp(uY) Omega

is exactly normalized. Its fixed-volume expansion through degree two is

    Omega + u C*Omega
      + u squared [ (C*) squared Omega/2 - V Omega/2
                    + chi_lift/sqrt(2) ] + O_L(u cubed).

H0 kills the first two vectors and the vacuum component. Therefore the
quartic energy coefficient is the energy of the bracketed four-particle
vector divided by V. With Phi=(C*) squared Omega/sqrt(2), this is exactly
one half of E(Phi+chi), whenever the compact terms embed without aliases.
In particular, the bare E-channel threshold form 104mu+240tau corresponds
to the pulse coefficient 52mu+120tau. No factor of two is missing.

## Uniform remainder reconstructed without a cluster theorem

The PRE used a conservative decomposition into six-site Y terms and four-site
X terms. After release I also checked the sharper primitive-term constants
in the author report. For Y, the sums of absolute primitive coefficients of
the five R fields are (sqrt(2),4/sqrt(6),sqrt(2),sqrt(2),sqrt(2)). Thus their
combined sum ell obeys ell<=sqrt(32/3). A primitive two-site anti-Hermitian
term d B*-conj(d)B has norm |d|, not 2|d|. There are at most two translates
through each site. A commutator therefore costs alpha=4ell per support site.

For X put m=(1/sqrt(2))sum |chi_sigma|. A four-site term has norm
|chi_sigma|/sqrt(2) and four translates through a fixed site. Its commutator
cost is beta=8m. A Y commutator adds at most one support site and an X
commutator at most three. Defining F_k(q)=product_(j=0,...,k-1)(q+3j), any
prescribed sequence with r Y and s X commutators has bound

    alpha^r beta^s F_(r+s)(q) ||O||.

The proof expands the local terms and discards disjoint commutators at each
step. It bounds each connected sequence separately, then sums its norm.
It never assigns a small support to the sum of all sequences. Summation of
the initial local densities produces V times this bound. Consequently it is
uniform in volume for fixed chi and all sufficiently large embedding tori.

For clarity, the remainder follows from two one-variable Taylor formulas.
For an observable O first expand exp(-vX)O exp(vX) to order two, then expand
its three Y-conjugated vacuum expectations, and set v=u squared. Every
Taylor remainder is bounded by the next commutator norm divided by its
factorial, since conjugation by either exponential preserves operator norm.
The phase exp(i pi N/2) fixes X, O=H0 or N, and Omega, and sends Y to -Y.
All the relevant vacuum expectations are therefore even in u, for complex
z and complex chi as well as real coefficients.

For H0 the three retained Y degrees are respectively 4, 2, and 0. The
respective discarded degrees are 6, 4, and 2, and the X remainder is degree
three in v. H0 Omega=H0 Y Omega=0 removes the lower energy coefficients.
The resulting bound is

    |<H0>/V - E(Phi+chi) u^4/2| <= D_chi |u|^6,
    D_chi=h[alpha^6 F6(25)/720 + alpha^4 beta F5(25)/24
             + alpha^2 beta^2 F4(25)/4 + beta^3 F3(25)/6].

For N, expand X only to first order. The pure Y expectation starts with
2V u squared. The vacuum and first-Y expectations of [N,X] vanish: its
charges are +/-4, and after one Y commutator they are +/-2 or +/-6. This gives

    |<N>/V-2u squared| <= B_chi u^4,
    B_chi=alpha^4 F4(1)/24 + alpha^2 beta F3(1)/2
                              + beta^2 F2(1)/2.

These reproduce the report's constants, including all factorials and mixed
orders. The bounds hold for all real u with their loose right-hand sides.
There is no V u squared smallness condition and no infinite-volume unitary
construction being assumed. The fixed-volume vector expansion identifies
only the coefficient; the commutator bounds justify the uniform error.

## Torus embedding and compact infimum

A compact collection of finite occupation shapes and their required local
operator images embeds faithfully for sufficiently large L. As a conservative
sufficient choice, take L>4D, where D bounds their coordinate spans and the
finite connected supports contributing to the coefficient. Distinct orbit
shapes then cannot alias. A nonzero translation stabilizer of a four-site
set would have order at most four and include a displacement incompatible
with confinement to such a small coordinate box. Each compact orbit lift
has squared norm V. The author's existence-of-large-L statement is enough;
an optimal cutoff is unnecessary.

This argument must not be applied to the entire torus N=4 space. My literal
control constructs a counterexample to that stronger normalization claim:
at L=16 the set {0,2e1,8e1,10e1} has stabilizer order two, only V/2 distinct
translates, and the unnormalized sum of all V translates has norm squared
2V. Its E1 incoming matching amplitude is one, but the actual periodic
H0 applied to that incoming profile is zero there. The released proof
explicitly excludes a global isometry and is not contradicted by this test.

Only the compact collision source F=H4 Phi, the chi cross term, the chi
quadratic term, and the finite connected bare-energy coefficient are needed.
The separated-pair zero equations cancel the incoming profile outside the
collision region. These local terms embed for fixed chi and large L, proving
the half-form coefficient without summing a fictitious l2 incoming state.
The already checked bare quartic support argument supplies its local part.

The relaxed functional is

    E(Phi+eta)=E_bare+2 Re<eta,F>+<eta,H4 eta>.

Because H4 is bounded and F is finitely supported, this functional is l2
continuous. In particular, the difference at eta and eta' is bounded by
[2||F||+||H4||(||eta||+||eta'||)] ||eta-eta'||. Finite-support vectors are
dense. An l2 approximate minimizer can therefore first be chosen and then
truncated to produce compact chi within any prescribed positive accuracy of
T(z). Equivalently, the checked negative-energy resolvent approximants may
be used before truncation. No l2 limiting minimizer is required. The support
and D_chi,B_chi may diverge as the accuracy improves; no uniformity in that
last limit is claimed or needed.

## Ordered variational consequences

For fixed chi write t=E(Phi+chi)>0. The trial estimate is

    g_L(nu) <= (t/2)u^4-2nu u squared+D_chi |u|^6+nu B_chi u^4.

Choosing u squared=2nu/t gives

    g_L(nu) <= -2nu squared/t
                  +(8D_chi/t cubed+4B_chi/t squared)nu cubed.

First take the large-L limsup for this fixed chi, then nu down to zero,
then improve chi's threshold accuracy. This proves the stated upper bound
with -2/T(z). The threshold form is a finite Hermitian form on Sym^2 C^5,
so its value on unit coherent inputs z tensor z is continuous. Minimization
over z is legitimate. It must remain the coherent minimum, not the lowest
eigenvalue on all 15 incoming channels.

The additional conclusion T(z)>=8c, with
c=min(tau,mu/12)/99090432, follows from the landed full-carrier coercivity.
It does not need existence of a thermodynamic expectation limit: for fixed
chi and sufficiently small fixed u, the uniform density bound gives
rho>=2u squared-B_chi u^4, while 0<=rho<=1. Combine this with
e>=c(rho squared-2rho/V), send L to infinity, and then divide by u^4 and
send u to zero. The result is t/2>=4c. Finally take the compact infimum.
Reversing the volume and small-u limits would leave the adverse finite-V
term and would not justify this argument. The conclusion is restricted to
coherent incoming vectors. It supplies no bound T0>=8c I on the full matrix.

## Independent literal occupation control

The new `check_literal.py` uses exact rational coefficients, actual unordered
four-site occupation sets, and direct hard-core annihilation and creation.
It expands the E projector as delta_ij-1/3, the plane coefficients as signed
products divided by four, and the center-gradient operator as six local
terms minus the six neighbor-center terms. It counts V3 from actual graph
degrees. No projected independent-pair carrier or author assembly is used.

For S={0,(3,-1,1),(3,1,1),(6,0,0)}, the independent H0 column has 21 nonzero
entries and gives

    H_SS=8mu/3+4tau=d,
    [H0(C_E*) squared Omega](S)=tau/3.

All 21 reverse columns satisfy exact Hermiticity. All 12 oriented nonzero
differences among the four sites are distinct. Therefore a nonzero translate
of S intersects S in at most one site; the two-body off-diagonal terms in H0
preserve at least two occupied sites, so no such translate contributes to
the orbit diagonal. Direct orbit grouping also finds only the diagonal entry.

Only the middle axial pair is a graph edge, giving V3=0 and the displayed
diagonal. In the source contraction the shifted middle pair that becomes the
x-axis pair at center (3,0,0) produces the straight two-pair configuration
with incoming amplitude one and coefficient tau/3. The other returned
configurations have zero matching amplitude. This also verifies the source
by a short occupation-level argument, separate from the complete array check.

The optimal one-word physical creation coefficient is g=-tau/(6d), or
chi_S=sqrt(2)g. Its pulse quartic is

    52mu+120tau + g(tau/3)+g squared d
       =52mu+120tau-tau squared/(96mu+144tau).

Three exact rational parameter controls agree. At mu=tau=1, g=-1/40,
the coefficient is 41279/240, and the improvement is 1/240. The compact word
has trivial torus stabilizer at L=7,8,13. Direct periodic operator action at
L=31 equals the periodized infinite 21-entry column exactly. The separate
L=16 distant stabilizer test is described above. Finally, after independently
forming the full array, all 21 entries were compared with the frozen author
output and agree exactly.

The single run was priced at 30 CPU seconds/150 MB with one BLAS thread;
CPU and wall guards plus deadline/STOP checks were active. Actual measured
resources were 0.309406 seconds wall, 0.308546 seconds CPU, and 22,495,232
bytes peak RSS. No large N=4 torus matrix or full many-particle exponential
was enumerated. `literal_results.json` records the complete rational column
and actual controls. This finite computation checks local coefficients and
specific normalization cases; it does not replace the all-volume proof.

## Remaining limits

The bridge reaches the already checked relaxed zero-threshold form only as
an upper variational coefficient. It does not establish a matching lower
many-body asymptotic, a canonical fixed-N thermodynamic limit, a preparation
efficiency bound, fragmentation or polarization selection, spontaneous order,
an excitation spectrum, or a positive-energy scattering theorem. It evaluates
neither the general 15-channel Green matrix nor its smallest eigenvalue.
The fixed positive couplings, compact correction chosen before the volume
and small-density limits, and supplied physical Hamiltonian remain essential.
All provisional threshold dependencies retain their original scope. No
record-process, gravitational-source, axiom-consistency, or native-law
selection conclusion follows from this successful bounded construction.
