# Physical weighted source bound on the microscopic initial layer

Author analytic discovery proof. Not independently checked. This is a strictly weaker time-scale result than CONTRACT(W1). The time interval shrinks with epsilon; no common positive physical horizon is obtained. The supplied actual microscopic law, bare Omega, all later births, physical Gauss sector, finite integer spin and original resolved/coherent marks are unchanged.

## Statement and notation

Let n=|A|, c=2756 and

    Phi_a=c+sum_e 2^(-d(a,a(e)))E_e²,
    X=sum_a w_a Phi_a,
    Z=cn+sum_e E_e².

The periodic distance and complete finite spin law are those in CONTRACT. There are finite C,c_* and epsilon0>0, independent of spin and torus volume, such that for the ACTUAL microscopic ensemble from bare Omega, with t=epsilon²u and u>=0,

    <X>_micro(t)/n <= C epsilon² exp(c_*u),           (I1)
    (kappa/epsilon²)n^-1 integral_0^t
       sum_(a,mu at a)<j_mu*Phi_a j_mu>_micro(s) ds
                   <= C epsilon² exp(c_*u).          (I2)

Constants depend on the fixed local law, delta,kappa and the fixed order-six normal-form circuit, and are not practical resource estimates. Increasing c_* absorbs a factor1+u. The estimates become trivial at large u; in particular they do NOT solve(W1) for fixed physical t>0. The scaling epsilon² S(S+1)=delta/K is permitted without changing constants. For fixed local radius r, w_a Q_a²<=C_r w_a Phi_a; physical translation invariance then turns(I1) into a local bound for t<=u0 epsilon². Equation(I2) is the actual mean weighted original post-mark activity, not a new observed weight or grade.

A useful consequence is a vanishing weighted initial layer. For example, for u_epsilon=(4c_*)^-1 log(1/epsilon), the bounds on physical X/n and weighted activity/n are O(epsilon^(7/4)). This is NOT a uniform bound on epsilon^-2<X>/n over that logarithmic window. Finite fixed monitored regions inherit the activity statement by physical translation invariance. No assertion on a signed surrogate source is substituted for(I2).

## 1. Uniform quadratic-weight algebra

Here is the load-bearing weighted refinement of the checked unweighted finite-circuit proof. It is included rather than assumed.

Use the physical basis of charges and integer link fields. A local operator A_Z has field-displacement Schur seminorm

    s_p(A)=max{ sup_alpha sum_beta |A_(alpha,beta)|
                       (1+d_E(alpha,beta))^p,
                sup_beta sum_alpha |A_(alpha,beta)|
                       (1+d_E(alpha,beta))^p },

where d_E is the sum of absolute field changes on its support. All local charge labels are included in the row/column indices. A blocked boundary transition has coefficient zero. Since 1+d_E(alpha,gamma)<= (1+d_E(alpha,beta))(1+d_E(beta,gamma)), these are submultiplicative norms. We use fixed p>=4 below. Original normalized spin hops have bounded row/column sums and unit field bandwidth, uniformly in S. The electric compensation coefficient is diagonal and bounded uniformly in S after division by S(S+1); its Schur norm is its uniform supremum. Finite sums, products and commutators therefore have uniform s_p bounds.

P_W deletes selected matrix entries, and I_W divides a nonzero-grade entry by a nonzero integer. Both are contractions in s_p and do not change field displacement or support. Every finite-order normal-form coefficient consequently has bounded s_p. A local gate exp(z A_Z) obeys s_p(exp(z A_Z))<=exp(|z|s_p(A_Z)). The fixed finite-color circuit has a bounded cone for any one input term. Its exact transformed local terms, their Taylor coefficients and their remainders are therefore analytic in this Banach algebra on a common epsilon disk. Cauchy estimates give the SAME epsilon orders as the unweighted construction, uniformly in S and volume, with finite s_p constants. This argument also bounds [E_e,Y E-local terms] and their shifted analogues: an E commutator multiplies a matrix entry by one component of its field displacement, costing one power of s_p rather than S.

To justify quadratic forms, insert diagonal fields into these row estimates. A finite-support weighted term of the shape E_e A E_f, E_e A or A has its absolute quadratic form bounded by a constant times the sum of 1+E_g² over its support; use 2|E_e E_f|<=E_e²+E_f² and the row/column bounds after shifting fields across A. The shift errors cost at most two powers of d_E. Local generator action on a SUM of such terms involves only intersecting supports: complete gain and loss cancel for disjoint supports. Each fixed finite composition enlarges support/incidence by a finite constant.

X is bilocal rather than finite-range: c sum w_a plus sum_(a,e)f(a,e)w_a E_e². The same argument applies to this explicitly summed family. Each operation enlarges the two endpoint neighborhoods by a fixed radius; bounded shifts of either endpoint change f by at most a fixed factor2^r. Its required sums are finite uniformly in volume:

    sup_e sum_a f(a,e)<=27,
    sup_a sum_e f(a,e)<=162.                         (I3)

A fixed finite number of local actions or homological inverses on X thus has a quadratic-form majorant C Z, with the coefficient's stated epsilon order. No product of two extensive norms is used. For clarity, after taking absolute row sums, terms containing a given E_e² have coefficients bounded by a fixed convolution of these summable kernels and bounded-incidence support indicators; constant terms sum to Cn. This proves the claimed CZ majorant on the whole finite carrier, and hence on Gauss and with ancillas. It is not an unbounded-rotor domain assertion.

Two more refined bounds retain X instead of Z. For a grade-zero local Hamiltonian interaction, input and output have the same number of holes in its support. Match the input and output holes arbitrarily within that bounded support. Their Phi weights have bounded ratios; hole relocation is paid by the sum of input local-hole Phi weights. A field change s on link e changes X by

    sum_(remaining holes h) f(h,e)(2s E_e+s²).

Keep this coefficient until summing over interaction centers. The E_e² part has bounded incidence and the constant part is bounded by(I3). Summing therefore costs C X, NOT nX. The field-displacement Schur norm prices s² and the absolute matrix elements. Thus every bounded-incidence, finite-range grade-zero Hamiltonian family with uniform s_p has

    -C X <= i[H_diag,X] <= C X.                      (I4)

For D2 the exact source-word proof FAST_WEIGHT_FORM gives the concrete210000, but(I4) also handles the fixed higher diagonal coefficients.

Likewise, if a local jump V has one fixed NONPOSITIVE W grade, its output has no more holes in its support than its input. In the matrix formula

    (D[V]*X)_(alpha,beta)=sum_gamma V*_(alpha,gamma)
      V_(gamma,beta)[X_gamma-(X_alpha+X_beta)/2],

match each output hole to a distinct input hole. Removed-hole weights are paid by the input local-hole sum. Apply the preceding field-change estimate to the two paths and use their Schur product bounds. After summing bounded-incidence jump centers this gives the two-sided form bound C X. It also applies to the polarized cross map between two jumps of the SAME nonpositive grade, with constant proportional to the product of their s_p norms. For a positive-grade jump, newly created holes instead cost its local Phi weights. Their center sum is <=27Z, giving a CZ bound. These estimates retain interference between all paths within the specified jump; replacing them by path probabilities is unnecessary.

## 2. Exact transformed generator and a weighted correction

Let sigma=Y rho_micro Y*, with Y the exact checked order-six finite local circuit. It obeys

    L'* = i delta epsilon^-4[W,.]+B_epsilon,
    B_epsilon=epsilon^-2 B2+O_local(epsilon^-1),
    B2=i delta[D2,.]+kappa sum_mu D[j_mu]*,

with the same orders in the weighted algebra above. The exact jumps J_mu=Y j_mu Y* have finitely many W grades in their bounded circuit cone. Their positive grades are O(epsilon²); J_(mu,-1)=j_mu+O(epsilon²), J_(mu,0) and J_(mu,-2) are O(epsilon), and all other nonpositive grades are at least O(epsilon²). These orders follow from J'(0)=[-F+F*,j] of grades0,-2. They are coefficient statements, not measured grade channels.

Since X has grade0, onsite averaging gives the EXACT diagnostic identity

    P_W sum_mu D[J_mu]* X
                     =sum_(mu,r)D[J_(mu,r)]*X.

The bare grade minus-one term obeys the checked original form(J3). Its same-grade correction is O(1)X after the microscopic epsilon^-2 factor; grades0,-2 also cost O(1)X, while positive-grade squares cost O(epsilon²)Z. By(I4) all diagonal Hamiltonian coefficients contribute at most C epsilon^-2 X. Thus

    P_W L'*X+(kappa/(4epsilon²))A_Phi
                  <=C epsilon^-2 X+C epsilon² Z,
    A_Phi=sum_(a,mu at a)j_mu*Phi_a j_mu.             (I5)

The averaging is inside a proof of an operator inequality. The ensemble and observed labels are never grade-dephased or altered.

Put R_X=(1-P_W)L'*X. Its leading order in the quadratic-weight family is epsilon^-1; the Hamiltonian off-grade remainder is only O(epsilon³). Define

    K1=(i epsilon^4/delta) I_W R_X,
    K2=(i epsilon^4/delta) I_W(1-P_W) B_epsilon K1,
    Xc=X+K1+K2.

They are Hermitian, and the weighted algebra proves

    -C epsilon³Z <=K1+K2<=C epsilon³Z.              (I6)

The exact cancellation is the same algebra as the checked defect correction:

    L'*Xc=P_W L'*X+P_W B_epsilon K1+B_epsilon K2.

B2 preserves W grade, so P_W epsilon^-2 B2 K1=0. The difference B_epsilon-epsilon^-2B2 has strength O(epsilon^-1), and K1 has order epsilon³. K2 has order epsilon^5. The weighted majorant then gives, on the actual whole finite Hilbert space,

    L'*Xc+(kappa/(4epsilon²))A_Phi
                   <=C epsilon^-2 X+C epsilon²Z.   (I7)

No positivity of Xc is assumed. The two corrections are essential; bounding the order epsilon^-1 cross loss separately would not give(I7).

The simpler weight Z commutes with W. The same finite-range quadratic algebra, with no hole refinement needed, gives

    -C epsilon^-2Z <=L'*Z<=C epsilon^-2Z.           (I8)

This does not assert that the microscopic energy is Z. Z is an explicit diagnostic field moment only.

## 3. Actual preparation, integration and original activity

The physical preparation is Omega, with zero fields and no A holes. In rotated coordinates it is Y Omega, not Omega. Every transformed E_e differs from E_e by a bounded O(epsilon) local operator, by the field-displacement estimate in section1 and the finite circuit cone. Each transformed w_a differs from w_a by O(epsilon) in the Phi_a-weighted norm; its cone is bounded. These imply

    <Z>_(sigma0)<=C n,
    <X>_(sigma0)<=C epsilon² n.                     (I9)

For the second bound write w_a Y Omega=[w_a,Y]Omega, and keep the Phi_a weight inside the squared norm. The commutator has a bounded local cone, O(epsilon) weighted norm, and Omega has Phi_a=c. This squares to O(epsilon²), uniformly in S. The global circuit norm ||Y-I|| is not used.

Let z=<Z>/n and x=<X>/n. By(I8), z(t)<=C exp(Ct/epsilon²). Add a sufficiently large C epsilon³ Z to Xc to make a positive majorant M with X<=M and M<=X+C'epsilon³Z. Equations(I7)-(I8), discarding the nonnegative activity, give

    d<M>/dt <=C epsilon^-2<M>+C epsilon <Z>.

Together with(I9) this yields

    x(epsilon²u)<=C epsilon² exp(c_*u).              (I10)

Integrating(I7), retaining the nonnegative activity and using(I6),(I8)-(I10), also gives

    (kappa/epsilon²)n^-1 integral_0^(epsilon²u)
              <A_Phi>_sigma(s)ds
                  <=C epsilon² exp(c_*u).          (I11)

Endpoint signs are handled with |<Xc-X>|<=Cepsilon³<Z>; in particular no negative endpoint is dropped as though Xc were positive.

To return to PHYSICAL weights, the local circuit estimates give form inequalities

    Y X Y* <= C X+C epsilon² Z,
    sum_(a,mu at a) J_mu* (Y Phi_a Y*) J_mu
                       <=C A_Phi+C epsilon² Z.     (I12)

For the first, use the squared-norm decomposition of w_aY* into Y*w_a plus its O(epsilon) local commutator, in the Phi_a-weighted norm. Uniformly Y Phi_a Y*<=C Phi_a follows by summing the local bound on Y E_e Y* with f(a,e), using(I3). For the second write J_mu=j_mu+(J_mu-j_mu), use (A+B)*(A+B)<=2A*A+2B*B in the positive transformed Phi weight, and use the O(epsilon) weighted local norm of J_mu-j_mu. Summing its squared errors costs epsilon² sum_a Phi_a<=27epsilon² Z. Cross terms are bounded by a positive form, not erased from the dynamics.

The first inequality in(I12) proves(I1) from(I8),(I10). The exact physical post-mark moment equals the left side of the second inequality in the rotated state. Its error integrates to C integral z(s)ds <=C epsilon²(1+u)exp(Cu); combine this with(I11) and enlarge c_* to prove(I2). Both original instruments obey the same column/Schur estimates with their actual coherent signs retained. Every later birth is included in the exact ensemble used in these integrations.

Finally the PHYSICAL microscopic generator, bare Omega and diagnostic Phi are translation covariant on each torus. Hence the average per n equals the moment at each A center. No translation covariance of the chosen normal-form coloring is required. This gives the declared local and finite-region conclusions.

## What remains open

The exponential exp(c_*t/epsilon²) is explicit and fatal to a common positive-time deduction. The all-state current form(I4) prices motion by X rather than by original loss; the actual zero-loss field-current example explains why that distinction cannot be erased. A successful(W1) proof still needs a state/source-sensitive long-fast-time estimate, or an alternative weighted corrector with a physically uniform growth rate. Neither the connected effective-source theorem nor the global count tilt supplies that step. This lemma does not prove the microscopic local marked limit, microscopic positive-time cluster weights or an infinite-volume unbounded field process. It has no numerical evidence or formal review attached; its weighted closure and physical return require an independent proof check before reuse.
