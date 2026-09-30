# Local integrated identity for the original same-mark off-grade pole

Author discovery lemma, September 30, 2026. Not independently checked, not an M4 convergence theorem and not the weighted-source target (W1). This is a uniform LOCAL refinement of the landed fixed-graph coherence correction, not a claim to invent penalty averaging. The complete actual cross dissipator is retained. No measured grade splitting, positive embedding, gap assumption or local replacement of a global exponential is used.

## 1. Exact imported normal form and scope

Use the supplied microscopic compensated finite-spin law and the finite-depth, finite-range unitary Y constructed through order six in the checked DEFECT_LEMMA, equations(D4)-(D6). Its local coefficient bounds hold uniformly in spin S and torus volume. Work in the exact rotated ensemble sigma(t)=Y rho_micro(t) Y*, including its actual preparation Y Omega; no change of state is made in this argument. For every epsilon in a sufficiently small fixed interval, the exact adjoint generator has the decomposition

    L_epsilon* = epsilon^-4 A0 + epsilon^-2 B2
                   + epsilon^-1 C + R_epsilon,
    A0 O = i delta[W,O],
    B2 O = i delta[D2,O]+kappa sum_mu D[j_mu]* O.       (O1)

The remainder R_epsilon is an exact sum of bounded local maps with common finite support range and bounded local completely bounded strength. This follows by writing the exact finite-circuit jumps as J_mu=j_mu+epsilon j1_mu+epsilon² j2_mu(epsilon), with uniform local analytic bounds, and expanding their dissipator EXACTLY. The order-zero Hamiltonian delta D4, order-two delta D6 and order-three remainder are included in R_epsilon. The maps need not separately be positive. Each whole local cross or dissipator difference map annihilates operators on a disjoint support; splitting its loss from gain before using locality would be invalid.

The first derivative has j1_mu=[-F+F*,j_mu] and W grades0,-2. The original j_mu has grade-1. Thus

    C(O)=kappa sum_mu (j_mu* O j1_mu+j1_mu* O j_mu
           -(1/2){j_mu* j1_mu+j1_mu* j_mu,O}).         (O2)

This is the full original same-mark map, including recycling and both losses. Its two terms inside an unnormalized coherent edge mark remain coherent. If [W,O]=0, C(O) has only grades+1,-1. B2 preserves every W grade. These statements hold on the full tensor carrier, and then on the invariant physical Gauss space; coherences and a reference ancilla are allowed.

For definiteness, local-strength constants mean a decomposition into maps Q_Z acting on a bounded support Z, with

    nu(Q)=sup_x sum_(Z containing x) ||Q_Z||_cb.

Let lambda2,lambda1,lambda0 bound nu(B2),nu(C),sup_epsilon nu(R_epsilon), and let r bound all their support diameters. They are finite constants from the specified finite circuit, fixed delta,kappa and degree-six graph; they do not depend on S,L or ancillary dimension. This is not a numerical resource claim. A reproducible upper bound follows by the finite-color support-cone recursion and the analytic gate bounds in the cited defect construction. For a fixed support X,

    ||Q(O_X)|| <= nu(Q)|X| ||O_X||,
    supp Q(O_X) subset X^(r).                         (O3)

Define m0=|X|, m1=|X^(r)|, m2=|X^(2r)|. Onsite averaging and the homological inverse I_W preserve support, have completely bounded norms1 and at most iota=pi/2, and obey [W,I_W A]=A-P_W A. All operators below are finite matrices at fixed S,L. Uniform bounds, not an unproved unbounded rotor generator, are the substantive conclusion.

## 2. Two explicit corrections and the exact residual

Let O=O* be supported on X, [W,O]=0, ||O||<=1. Put

    K0=(i/delta) I_W C(O),
    K20=(i/delta) I_W B2 K0,
    K_epsilon=epsilon³ K0+epsilon^5 K20.              (O4)

Both corrections are Hermitian and preserve Gauss. Since C(O) is off-grade and B2 preserves grades,

    A0 K0=-C(O),  A0 K20=-B2 K0.

Consequently the exact algebra, with no discarded cross terms, is

    L_epsilon* K_epsilon = -epsilon^-1 C(O) + E_epsilon(O),
    E_epsilon(O) = epsilon² C K0
      +epsilon³(R_epsilon K0+B2 K20)
      +epsilon^4 C K20+epsilon^5 R_epsilon K20.       (O5)

There is no epsilon term: the second correction cancels it. No inverse of a dark-sector Hamiltonian or loss operator occurs. The small denominator is only the integer nonzero W-grade spacing delta.

For explicit constants write

    a=(iota/delta)lambda1 m0,
    b=(iota/delta)lambda2 m1 a,
    d=lambda1 m1 a+lambda0 m1 a
           +lambda2 m2 b+lambda1 m2 b+lambda0 m2 b.

Then for epsilon<=1,

    ||K_epsilon|| <= a epsilon³+b epsilon^5,
    ||E_epsilon(O)|| <= d epsilon².                 (O6)

For an arbitrary normalization multiply the right sides by ||O||. The common finite support radius gives m1,m2<=c_r |X|, so d is bounded by an explicit constant times |X|³; no volume factor occurs.

For ANY actual initial density, including arbitrary mixtures, correlations and reference ancillas, integrate (O5) against the exact normalized sigma(t):

    |integral_0^T epsilon^-1 Tr[sigma(t) C(O)] dt|
       <=2a epsilon³+2b epsilon^5+d T epsilon².       (O7)

This controls the signed/complex integrated cross functional; it is NOT a bound on the integral of its absolute value, a positive activity, or the norm of an independently evolved cross map. For a non-Hermitian O the same operator identity holds; using the dual norm directly gives (O7) with the same constants. Hermiticity was used only to display real expectations.

## 3. Time-dependent tests and summable local families

For a piecewise C1 family O(t), with grade0, support X, sup norm M and total operator-norm variation V (including finitely many jumps), linearity of K gives

    |integral epsilon^-1 Tr[sigma(t) C(O(t))] dt|
      <= (a epsilon³+b epsilon^5)(2M+V)+d T epsilon² M. (O8)

At a change of the specified registered generator, use its appropriate K on each side and pay both endpoint norms; do not claim a cancellation across changed maps. In particular finitely many bin switches cost epsilon³ times their number. No uniform-in-the-number-of-bins claim follows unless that product is priced.

The same result holds for a decomposition O(t)=sum_X O_X(t), each term grade0, provided

    sum_X |X|³ (sup_t||O_X(t)||+Var O_X)<infinity       (O9)

with a bound uniform in S,L. Absolute convergence justifies exchanging sums and state expectations. This gives a precise quasilocal consumer norm; an arbitrary effective backward observable has not been shown to satisfy it uniformly. If its variation is O(epsilon^-2), (O8) only gives O(epsilon), with its explicit support constants. Rapid propagation cannot be hidden in a claimed bounded variation or in m1,m2.

## 4. Actual original finite-history registers

The identity includes exact finite classical record registers, with a specified finite monitored center set F, bin partition and count cap M. Record the original mark mu, not its W grade, and keep coherent signs inside their original edge mark. For every input register word z, append the bin and mark or enter the overflow symbol using V_(mu,z)=|append(mu,z)><z|. Replace a monitored original jump by the Kraus family j_mu tensor V_(mu,z), leaving all unmonitored jumps unchanged. Since sum_z V*V=I, its system marginal is exactly the original generator. Starting with a classical blank register, its quantum blocks are exactly the original sequential CP maps for the declared binned/capped history; overflow retains the tail as one output. This is a mathematical copy of classical original outcomes, not a new physical event or a proxy source law. Different original jumps retain different observed labels.

Y acts only on the system. Hence every copied jump still has the same j,j1 grades, and the first-order cross map contains its matching V on gain and the full original loss. The apparent number of register words does not multiply lambda1 or lambda0: for a fixed original mark use the column operator with components j tensor V_z, whose norm squared is ||j*j||, and likewise j1. The complete cross map has cb norm at most4||j||||j1||, independently of register dimension. The same column estimate applies to the remainder. When a test touches the regional record register, anchor it to ALL monitored centers F as well as its system support X. Only those copied maps can act through the register; unmonitored distant maps cancel by (O3). Thus the constants depend on X,F and the bin switches, not on total torus volume or the cap's Hilbert dimension. Arbitrary reference ancillas are untouched by this construction and by all homological maps.

This establishes (O7)-(O8) for the actual joint recorded ensemble and bounded grade-zero register/system tests. It does not estimate the entire finite-history instrument against the effective instrument: a Duhamel comparison needs the full backward test family and all other generator residuals. Neither continuous timestamp convergence nor a permanent autonomous apparatus is claimed here.

## 5. Preparation, physical coordinates and the remaining target

The lemma holds for arbitrary sigma(0), so it automatically includes Y|Omega><Omega|Y*. It never assumes bare Omega in rotated coordinates. For a physical test O_phys, the exact transformed test is Y O_phys Y*. It need not have grade0 even when O_phys does. A fixed local bounded grade-zero test changes by O(epsilon) under the finite circuit, but multiplying such a change by epsilon^-1 in the disputed integral is not automatically small. Therefore (O7) is expressly a generator-component lemma in the exact normal-form coordinates, not a replacement of the physical test.

The actual physical weighted source w_a Q_a² has norm O(S²)=O(epsilon^-2) at fixed radius. Applying the generic bound(O7) to a similarly large grade-zero test yields only O(1) over a fixed time, even before pricing the physical-coordinate return. Its absolute positive activity is also not the signed cross functional. The surviving grade-zero fast field current in WORKING_01 cannot be canceled by I_W. To prove(W1), a separate state-dependent weighted current/corrector estimate and weighted preparation/return bound are still needed. No fast gap, local cluster distribution or weighted microscopic preparation is inferred.

## 6. Prior-art comparison and evidence

The actual landed BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET note section on equations(8)-(9) already retains the order epsilon^-1 QP loss, constructs a size epsilon³ off-diagonal correction, and gets a fixed-graph O(epsilon) trace comparison using the full CPTP semigroups. Its exact argument was reread before this derivation. The checked DEFECT_LEMMA(D7)-(D9) already uses two local observable corrections and grade preservation to obtain epsilon² defect drift. The present statement extracts that mechanism for the COMPLETE shared-mark cross map and gives a uniform local/ancillary/finite-history consumer norm. It is a narrow useful extension, not a new full microscopic limit. No numerical calculation is required by the proof; any forthcoming sparse control is corroboration only and will be separately priced.
