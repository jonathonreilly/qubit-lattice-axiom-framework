> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# A real two-qubit clock return and a conditional finite-window literal gate

Status: new author construction, pending distinct check. ROOT proposed the inverse rank-one spectrum. The proof below reconstructs the interlacing, weights, complete gate phase and positive hardware costs. Its physical composition depends on EXACT_ALL_TIME.md SHA `37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34`; no distinct-check acceptance of that dependency has been supplied to this author at freeze, so the composition remains explicitly conditional on that interface. No two-time same-gate or halt claim is made.

## Literal gate and clock subspace

Let theta=atan(4/3), so cos(theta)=3/5, sin(theta)=4/5 and

    W=exp(i theta)exp(i theta X1X2).

Its old-X1X2 sector eigenvalues are w_+=exp(2i theta), w_-=1. K=2I+Z1Z2 commutes with X1X2. On the two clock qubits write T=Y_aY_b. Its +1 eigenspace is spanned by

    e=(|00>−|11>)/sqrt(2),
    d=(|01>+|10>)/sqrt(2).

Let S=d-perp, a real three-dimensional subspace containing the real product seed |00>. On S,

    T3=2|e><e|−I_S.

No e or d state is prepared; they only define a real clock Hamiltonian. In particular |00> is the actual proposed clock input.

## Explicit inverse spectral construction

Define

    tau=2pi−3theta, omega=2pi/tau,
    delta=2+2theta/tau=(4+2omega)/3,
    alpha=(0,omega,2omega),
    beta=(delta−omega,delta,delta+2omega).           (1)

Because 1<4/3<sqrt(3), monotonicity of tangent on (0,pi/2) gives pi/4<theta<pi/3. Hence pi<tau<5pi/4 and 8/5<omega<2. In particular omega<delta<2omega: these inequalities reduce respectively to omega<4 and omega>1. Thus

    alpha1<beta1<alpha2<beta2<alpha3<beta3.

Also sum(beta)−sum(alpha)=3delta−2omega=4.

Define three explicit real numbers

    q_j=−prod_k(alpha_j−beta_k)
              /[4 prod_{l!=j}(alpha_j−alpha_l)].   (2)

Interlacing makes each q_j positive: the numerator/denominator signs for j=1,2,3 are respectively (−,+),(+,−),(−,+), before the leading minus. The rational identity

    prod_k(z−beta_k)/prod_j(z−alpha_j)
        =1−4 sum_j q_j/(z−alpha_j)                 (3)

follows by matching the three residues and the value 1 at infinity. Comparing the coefficient of 1/z, using the trace difference 4, proves sum_j q_j=1. Thus f=(sqrt(q1),sqrt(q2),sqrt(q3)) is a real unit vector.

For a fully explicit orthogonal map, choose the ordered real orthonormal basis of S

    [ e, (|00>+|11>)/sqrt(2), (|01>−|10>)/sqrt(2) ].

In these coordinates e=(1,0,0). Let h=f−e and O=I−2hh^T/||h||². Since q2,q3>0, h is nonzero. This real symmetric orthogonal Householder matrix obeys O f=e and O^T e=f. Define

    G=O diag(alpha) O^T on S.

The matrix determinant lemma and (3) show that G+4|e><e| has precisely the eigenvalues beta. No eigenvector or sign branch is left unspecified. All matrices here are finite real symmetric matrices.

Define the full four-by-four clock matrix C by

    C|_S=G+T3,   C d=0,                            (4)

with no off-diagonal S/d block. Both C and T preserve S. On S the two old-sector generators are

    C−T=G,
    C+T=G+4|e><e|−2I_S.

The first spectrum is alpha. Since tau omega=2pi, its time-tau exponential is I_S. The second spectrum is beta−2, whose entries differ from delta−2 by integer multiples of omega; since tau(delta−2)=2theta, its exponential is exp(−2i theta)I_S. Therefore exactly

    exp[−i tau(C−X1X2 T)]|_{old tensor S}
       =exp(−2i theta) W tensor I_S.               (5)

This is valid on the whole old space and arbitrary passive extensions, not just old-X eigenstates. It returns every S clock vector, including |00>, without leaving any logical information in the clock. Arbitrary old-clock correlations supported in S also obey this identity.

## Positive real clock block and norm bounds

G is positive with ||G||=2omega<4. Equation (4) gives ||C||<=2omega+1<5. More usefully,

    (C+I)|_S=G+2|e><e|>=0,
    (C+I)d=d,
    ||C+I||<=2omega+2<6.                           (6)

Thus the fixed positive shift +I suffices; no numerical minimum-eigenvalue estimate is needed. C+I is a real symmetric positive two-qubit block on the neighboring clock sites. Supplying this general real two-qubit matrix is an explicit actuator premise; it is not derived from a narrower displayed exchange-only primitive class or a native Hamiltonian. Its particular real coefficients depend on the specified literal theta through (1)-(4).

## Conditional composition with the exact mediator device

Use precisely the new calibrated device in EXACT_ALL_TIME.md. To distinguish notation, let l=lambda²,

    x=3l(2−l)/(1−l), g=sqrt(x), A0=4+2l+x,
    a_eff=[sqrt(A0+4l)+sqrt(A0−4l)]/2,
    b_eff=[sqrt(A0+4l)−sqrt(A0−4l)]/2,
    c_eff=2lambda+g+2−a_eff.

Add the single actual positive clock block b_eff(C+I). The exact-interface dressing estimate gives, for all joint inputs and all real t, comparison error at most

    164lambda[1+|t| b_eff ||C+I||]                 (7)

against the complete unitary

    exp[−it(c_eff+b_eff)]
       exp(−itK) exp[−it b_eff(C−X1X2T)]
                          tensor exp(−it2a_eff n_m).

K commutes with the clock generator here, so this factorization is justified. The scalar b_eff is the installed +I shift and is retained once. At the physical time T_gate=tau/b_eff, (5) makes this target exactly

    exp[−iT_gate(c_eff+b_eff)−2i theta]
       [ exp(−iT_gate K) W ] tensor I_S
                          tensor exp(−iT_gate2a_eff n_m).  (8)

The mediator need not be initialized: arbitrary correlations between mediator, old system and passive references are allowed under this tensor-product-unitary comparison. To obtain an input-independent common clock output |00>, supply that clock product state independently of these systems. The complete target retains any pre-existing mediator correlations. It does not replace them with a fresh product environment.

## Explicit finite window, cap and resources

Take 0<epsilon<=1 and define the scaled half-width h=epsilon/24. Choose

    0<lambda<=min{
       1/1000,
       epsilon/[656(1+6(tau+1))],
       (Lambda−4)/(8+2sqrt(7)) },  Lambda>4.        (9)

Observe at any t in [T_gate−h/b_eff,T_gate+h/b_eff]. This interval is positive since tau>pi and h<=1/24. Put s=b_eff t; then |s−tau|<=h and |s|<=tau+1. The background comparison (7) costs at most epsilon/4. For every clock vector in S, selfadjoint-generator continuity and ||C−X1X2T||<=||C||+1<6 give

    ||exp[−is(C−X1X2T)]−exp[−i tau(C−X1X2T)]||
       <=6|s−tau|<=epsilon/4.

Therefore throughout the entire stated window, the actual output is within epsilon/2 in complete vector/isometry norm of

    exp[−it(c_eff+b_eff)−2i theta]
       [exp(−itK)W] tensor |00>_clock
                          tensor exp(−it2a_eff n_m),     (10)

interpreted as a map on arbitrary old/mediator/passive input with the independent clock |00> inserted. The unhalved complete channel distance is <=epsilon. In (10), the scalar, old aging and mediator aging all use the actual observation time t; the gate phase −2theta is constant. No normalized rare-branch argument or hidden phase correction is used.

There are five qubits and six positive blocks: the previous five plus b_eff(C+I). The latter adds less than 6b_eff to each clock-site incident load. The exact-interface estimates give g<=sqrt(7)lambda and 0<b_eff<=lambda². Hence every incident load is bounded above by 4+(8+2sqrt(7))lambda for lambda<=1; (9) is a conservative sufficient cap. Clock-pair support is the existing neighboring a,b edge. No higher-body physical block or additional prepared entangled ancilla is installed.

For fixed Lambda>4, choosing lambda equal to the minimum in (9) gives lambda=Theta(epsilon) as epsilon approaches zero. Since b_eff/lambda²->1, the sufficient gate time is Theta(epsilon^{-2}) in the fixed old-gap units; the absolute half-width is Theta(epsilon^{-1}) and its relative size h/tau is Theta(epsilon). This is a supplied, calibrated constant-qubit family, not a native preparation or equal-supplier speed comparison.

## Sampled return is not halt

At twice the scaled time, the same exact clock calculation gives exp(−4i theta)W² tensor I_S, not the same W. Thus this construction does not meet the earlier two-sample same-W contract and is not a counterexample to its algebraic constraints. It is a single gate-time return with a controlled shrinking-relative-width window. The uniform all-time mediator simulation does not make the gate output constant at later times.

The clock coefficients, exact mediator calibration, literal K, positive real general two-clock block, clock product seed and chosen observation window remain suppliers. The mediator target uses effective frequency 2a_eff rather than bare gap 4. There is no capture, reset, permanent halt, implementation of the old two-port apparatus, or microscopic-native selection claim.

The new exact clock proof is (1)-(6); the physical theorem is conditional on the explicit exact-mediator interface and its distinct-check disposition. ROOT supplied the spectral construction; this author reconstructed the proof and resource/error bookkeeping. No scientific executable, external search, Git, canonical/checkpoint/editable-prompt/model change, publication or delegation was used. A transient placeholder from a mistaken patch path was removed immediately; the only surviving new artifact is this source. All frozen sources remain unchanged. Distinct review is required before promotion.
