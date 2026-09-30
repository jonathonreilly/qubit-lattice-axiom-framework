# Focused independent check: physical weighted microscopic initial layer

I found no substantive mathematical error in the frozen
INITIAL_LAYER_WEIGHTED_LEMMA.md at229c1f18 and FAST_WEIGHT_FORM.md at16ad5397.
The stated inequalities follow at their explicit shrinking-time scope from
the actual compensated finite-spin law and the checked finite-circuit normal
form. This is a focused analytic reconstruction, not a formal review, audit,
retained result, numerical certificate or a common-positive-time theorem.
No author source or previous packet was changed.

The physical conclusion is, for fixed supplied couplings and sufficiently
small epsilon, uniformly in integer spin and all stated even torus volumes,

 <X>_micro(epsilon^2 u)/|A| <= C epsilon^2 exp(c_* u),
 (kappa/epsilon^2)|A|^-1 integral_0^(epsilon^2 u)
       <sum_(a,mu at a) j_mu* Phi_a j_mu>_micro(s) ds
                                      <= C epsilon^2 exp(c_* u).

It includes the bare physical Omega preparation, the actual physical
observable and all subsequent births for each original instrument separately.
It supplies a useful bounded-fast-time initial layer and the stated weaker
logarithmic-layer consequence. The exponential exp(c_* t/epsilon^2) prevents
deduction of the contract's fixed positive physical-time weighted target.

## Independence, source exposure and exact inputs

PRE.md was frozen at
d181d854f73c77d6b357383cc133a372d5ade610b0b6ba85dcb184832e3e2fc4
before opening either target proof, its intermediate arguments or code.
The parent brief disclosed the target names/hashes and requested checks,
without a verdict. The full contract and actual landed model/compensation
sources were read first. My precomparison proposed a local normal-form
initial-layer estimate using suprema of two-support moments rather than the
author's summably weighted global X. It independently anticipated the
shrinking-time restriction and identified weighted preparation, physical
return, local closure and coherent losses as necessary obligations.

After that freeze, I read both complete target proofs, WORKING_01,
OFFGRADE_LOCAL_LEMMA, the full DEFECT_LEMMA and its independent check, the
offgrade focused check and weighted-current addendum, and the complete
landed uniform-local-ring source. Only its explicitly proved finite-order
circuit construction is used; its different spin normalization, prepared
state and slow-birth dynamics theorem are not imported. I did not open or
execute the author's check_weighted_current.py or its numerical output.
No new computation was needed. The arithmetic and operator checks below
are actual independent analytic checks, not rerun author assertions.

Current main was actually fetched and remains
30a9461ee19a49b99fa6628fe942f08e504e8903. Selected procedure authority remains
7146fe17a76de41badcaca3c3c7cac6d11eb2a00. SOURCE_BINDINGS.json records exact
hashes and read scopes, including all transitive proof inputs used here.
The prior independent receipts are evidence of their own limited scopes;
the weighted extension is reconstructed below rather than inferred from
their verdicts. No root native result enters this argument.

The supplied law is the actual locally gated compensation,

 H=delta epsilon^-4(W+epsilon T+epsilon^2 C_S),
 L_mu=sqrt(kappa)epsilon^-1 j_mu,
 T=-sum_a(F_a+F_a*),
 C_S=sum_a(F_a*F_a+D_el,a/[S(S+1)])Q_gate,a.

Here D_el,a is the unscaled electric polynomial, not the landed notation
D_(a,S) for the diagonal of F_a*F_a. The source identity
D_(a,infinity)-D_(a,S)=D_el,a/[S(S+1)] verifies the equality of laws.
The compensation gate is the product of other nearby A occupancies; it is
distinct from either the diagnostic Phi or the contract's local Q_a.
Normalized spin shifts keep their exact boundary zeros. The Gauss sector,
qutrit matter, quantum dynamics, couplings and bare Omega are supplied,
not selected by native M2 or the approved primitives.

## Exact jump form and the leading fast coefficient

Let f(a,e)=2^(-d(a,a(e))) in periodic L1 distance and c=2756. The lattice sum
factorizes as (1+2 sum_(m>=1)2^-m)^3=27. Choosing shortest torus
representatives gives an injection into the infinite sum; restriction to A
can only reduce it. Thus sum_a f(a,e)<=27 and sum_e f(a,e)<=6*27=162,
uniformly in volume. The definitions

 Phi_a=c+sum_e f(a,e)E_e^2,
 X=sum_a w_a Phi_a,
 Z=c|A|+sum_e E_e^2

give sum_a Phi_a<=27 Z and X<=27 Z on the whole carrier. These are sums
of physical diagonal observables, not localized versions of an extensive
exponential moment.

For a birth at b, exactly one hole is removed and exactly one link field
m changes by a unit. The remaining-hole coefficient on that link is at
most26. Completing the square gives exactly

 m^2/2+1378-26(2|m|+1)=(|m|-52)^2/2 >=0.

Since Phi_b>=2756+m^2, the exact change of X is at most -Phi_b/2. Also
Phi_b after the shift is at most2 Phi_b before it. Hence the whole original
dissipator satisfies

 sum_mu D[j_mu]* X <= -(1/4) A_Phi,
 A_Phi=sum_(a,mu at a)j_mu*Phi_a j_mu.

For coherent j=j_++j_-, both loss cross terms and the gain cross term with
this diagonal X vanish because the final matter charges are orthogonal.
This is an identity for this observable, not a replacement of the coherent
recycling map. It holds on coherent inputs and at spin boundaries.

The first circuit generator is -F+F*, since [W,F]=F and T=-(F+F*).
At second order the diagonal coefficient is
D2=C_S+[F,F*]. Product ordering of first-order gates can contribute an
additional commutator with W, but its W-average is zero; it therefore
does not change this D2. Expanding it gives precisely the three offdiagonal
families in FAST_WEIGHT_FORM. The electric polynomial and its occupation
gate are diagonal and commute with X exactly. They are not bounded by a
loss or by a growing bare S^2 constant.

I independently count the paths as follows. At an input hole h,
F_h F_h* has at most6*6=36 paths. A gated negative F_a*F_a term can be
assigned to an input hole at distance two; the possible centers a are the
six axial and twelve diagonal A neighbors, giving18*36=648 paths. A cross
commutator transfers a hole from c to a through a shared B. There are18
possible a, at most two shared B sites and two product orders, giving72
paths. A fixed occupied source has a unique charge, so there is no extra
charge-sign multiplicity. Each path has coefficient at most one in absolute
value. The bound756 is consequently safe, including all blocked paths.

For every such path, each changed link's A endpoint is within distance two
of its assigned input hole h. Thus f(h,e)>=1/4. Hole relocation costs at
most3 Phi_h; each of at most two distinct shifted links costs at most
27(E_e^2+2)<=135 Phi_h. If the same link is used twice in a same-center
term, the hop and return cancel its net field change. Therefore the change
is bounded by273 Phi_h in all cases. Multiplication gives206388, below the
stated210000. D2 is Hermitian, so the absolute entries of i[D2,X] are
symmetric. The row estimate and 2|u_alpha u_beta|<=|u_alpha|^2+|u_beta|^2
prove the two-sided form bound. No inference from a sparse compression or
from the old zero-loss witness is needed for this all-state estimate.

The resulting leading-fast inequality and its integrated activity follow
by an integrating factor. This is a relative X bound, not absorption by
original loss and not an epsilon-independent physical-time growth rate.

## Weighted finite-circuit closure

The displacement Schur norm is submultiplicative because the total field
displacement obeys the triangle inequality and
1+d(alpha,gamma)<=(1+d(alpha,beta))(1+d(beta,gamma)). Row and column sums
are both necessary. A literal hop has finite field bandwidth and bounded
row/column sums uniformly in S; its normalized coefficients are at most
one. The normalized electric polynomial is diagonal with uniform bounded
supremum. Finite words, commutators and Taylor coefficients therefore have
uniform bounds at every fixed displacement exponent.

W-averaging deletes entries and the homological inverse divides a nonzero
grade entry by an integer of absolute value at least one. They contract
these Schur norms and preserve support. Exponentiating one local gate gives
the convergent Banach-algebra estimate exp(|z|s_p(A)). Each input term meets
only a bounded circuit cone. Thus exact conjugated local terms and their
Taylor remainders retain the required epsilon orders in weighted norms,
uniformly in volume and spin. No norm of the complete global circuit in
this Schur algebra is required or bounded here.

A useful explicit form check is, for any two field configurations linked
by a matrix entry with displacement d,

 Phi_a(alpha)<=2 Phi_a(beta)+2d^2
                    <=(2+2d^2/c)Phi_a(beta).

Schur's test then bounds Phi_a^(1/2) A Phi_a^(-1/2) uniformly by a fixed
displacement norm of A, for every a, including a far from the support of A.
Commuting an E through A costs one displacement factor. Products needed in
the quadratic family have at most two exposed E factors; finite compositions
can be estimated by the total displacement along each product path. The
available fixed Schur exponents, or a larger fixed exponent if desired,
bound those factors uniformly. Normalized electric coefficients remain
bounded coefficients inside these products; they do not add an uncontrolled
electric degree or spin factor.

I checked the refinement from CZ to CX explicitly. For a local grade-zero
transition, match input and output holes inside its bounded support. Relocated
hole weights have bounded ratios by the triangle inequality for d. This
part of the row bound is a constant times the sum of input local-hole Phi
weights. For the unchanged holes, retain

 H_e(alpha)=sum_(input holes h) f(h,e)

in the field-change term. Its bound is a weighted row coefficient times
H_e(alpha)(E_e^2+1), plus the already accounted local-hole weights.
After summing the bounded-incidence interaction centers, the electric part
is bounded by sum_e H_e E_e^2<=X, and the constant part by
sum_e H_e<=162 sum_h w_h<=162X/c. Each local hole is counted only boundedly
many times. This proves CX rather than |A|X. Unbounded displacement values
inside an exact local gate are paid by their Schur weights.

For a fixed nonpositive-grade jump, its output holes inject into the input
holes in that local support. The exact matrix formula for D[V]*X involves
two paths through an intermediate output and the full average of the two
input X values. Apply the preceding change estimate to both paths. The
weighted row/column sums cost a product of the two jump Schur norms. Summed
incidence again gives CX. Polarizing two jumps of the same grade is valid
by the same two-path calculation; it does not discard their interference.
Positive-grade jumps can add local holes; summing their new Phi weights
costs at most C sum_a Phi_a<=C Z instead.

For off-grade or otherwise unrefined quadratic terms, use the bilocal
family sum_(a,e)f(a,e)w_a E_e^2. Each complete local action touches only
one of its two endpoint neighborhoods, or both if they are close. A finite
composition enlarges those neighborhoods by a fixed radius. Shifting a
kernel endpoint changes f by at most a fixed factor. Summing the resulting
finite convolutions leaves bounded coefficients for every E_e^2 and only
C|A| constant terms. This gives the claimed CZ form majorant. Complete
gain and loss cancel on disjoint supports; taking their extensive norms
separately would not justify this statement. The author's argument retains
that cancellation. These estimates also justify the corresponding Z drift.

## Exact grades, epsilon powers and corrected observable

The first jump derivative [-F+F*,j] has grades0,-2, while j has grade-1.
Consequently J_-1=j+O(epsilon^2), J_0,J_-2=O(epsilon), and every positive
grade begins at O(epsilon^2). For grade-zero X, averaging the complete
adjoint dissipator retains precisely equal jump grades. The resulting
negative/zero-grade corrections cost O(X) after multiplication by
epsilon^-2; positive-grade squares cost O(epsilon^2 Z). The bare jump form
above remains as the explicit negative activity. The diagonal Hamiltonian
coefficients cost at most C epsilon^-2 X. This gives(I5).

Write A0=i delta epsilon^-4[W,.] and L'* =A0+B_epsilon. If
R_X=(1-P_W)L'*X, the two definitions in the author proof give exactly

 A0 K1=-R_X,
 A0 K2=-(1-P_W)B_epsilon K1,
 L'*(X+K1+K2)=P_W L'*X+P_W B_epsilon K1+B_epsilon K2.

I_W takes a Hermitian off-grade input to an anti-Hermitian operator, so
the displayed factors of i make K1,K2 Hermitian. Weighted orders are
K1=O(epsilon^3 Z), K2=O(epsilon^5 Z) in the two-sided form sense.
B2 preserves grades, hence P_W epsilon^-2 B2 K1=0 exactly. The remaining
two compositions have orders epsilon^2 Z and epsilon^3 Z. The off-grade
Hamiltonian remainder is only epsilon^3 before correction and is included.
This independently verifies(I6)-(I7), including the sign and the absence
of an order-epsilon term. No dissipative gap or inverse on grade zero is used.

Likewise Z commutes with W, and the remaining local maps have strength
O(epsilon^-2) in the same quadratic family. Thus |L'*Z|<=C epsilon^-2 Z
as a two-sided form. Fixed spin and finite volume permit differentiation
without domain issues; uniform constants supply the claimed joint bounds.

## Bare preparation and physical-coordinate return

The global circuit is not locally supported and [w_a,Y] itself is not a
local operator. The precise useful factorization is

 [w_a,Y]=Y(Y* w_a Y-w_a).

Only B_a=Y* w_a Y-w_a has a bounded support cone and weighted size
O(epsilon). This factorization, together with the field comparison below,
makes the author's preparation argument precise; it is not a substantive
gap or a needed change of law. The author explicitly excludes a global
Schur bound for Y and supplies the required per-link bound.

Each Y* E_e Y-E_e is a bounded local O(epsilon) operator: commuting E_e
through each local gate costs its field displacement, not S. Therefore
Y*Phi_a Y<=C Phi_a, and the same holds with Y and Y* interchanged. The
constant shift errors sum by the kernel bounds27 and162. Since E_e Omega=0,
this also gives <Z>_(Y Omega)<=C|A|.

For the hole moment, pull the global Y out of the weighted norm. Since
w_a Omega=0,

 <Y Omega,w_a Phi_a w_a Y Omega>
       <= C ||Phi_a^(1/2) B_a Omega||^2
       <= C epsilon^2 Phi_a(Omega)=C epsilon^2 c.

The second inequality is the local weighted Schur estimate, not an
unweighted norm multiplied by S. Summation proves(I9). This correctly uses
Y Omega, including its O(epsilon) hole amplitude, rather than Omega in the
rotated dynamics. It does not assume a bounded microscopic energy of Omega.

For return, write Yw_aY*=w_a+B'_a with the same weighted O(epsilon) bound.
Using YPhi_aY*<=C Phi_a and the square inequality gives

 Y(w_a Phi_a w_a)Y*<=C w_a Phi_a+C epsilon^2 Phi_a.

Summing proves the first(I12). For each original mark put J=j+R with
R=O(epsilon) in its bounded cone. In the positive transformed Phi weight,
(j+R)*Phi(j+R)<=2j*Phi j+2R*Phi R. The weighted Schur bound on R and the
finite marks per center give the second(I12) with C epsilon^2 Z. This
inequality bounds cross terms; it does not delete them from the generator.
The original coherent mark remains a single operator throughout.

## Integration, quantifiers and remaining frontier

Let M=Xc+A epsilon^3 Z with A large enough that
X<=M<=X+C epsilon^3 Z. Combining the two corrected drift estimates yields

 d<M>/dt<=C epsilon^-2<M>+C epsilon<Z>.

With z(t)=<Z>/|A|<=C exp(Ct/epsilon^2), the source term integrates on
t=epsilon^2 u to O(epsilon^3 u exp(Cu)), while M(0)/|A|=O(epsilon^2).
This proves the displayed initial-layer X estimate after enlarging c_*.
Integrating(I7) and retaining activity gives an O(epsilon^2 exp(c_*u))
bound as well. The possibly negative Xc endpoint is controlled by
|Xc-X|<=C epsilon^3 Z; it is not silently dropped. Physical activity return
adds C integral_0^(epsilon^2 u) z(s)ds, of the same permitted order.

The scaling epsilon^2 S(S+1)=delta/K is allowed because all constants
were uniform in S before substitution. No fixed-volume-first limiting
argument occurs. Positivity/form inequalities also persist on the Gauss
sector and after tensoring an ancilla. The evolution conclusion, however,
is specifically for the actual Omega preparation, not for arbitrary states
that merely satisfy a global unweighted bound.

Translation symmetry is invoked only for the original physical generator,
Omega and Phi. Those translations act transitively on A. No symmetry of
the chosen circuit coloring is needed. For a fixed local ball, Cauchy and
the minimum f on its finitely many links give w_a Q_a^2<=C_r w_a Phi_a.
The same positive weight comparison applies inside the actual post-mark
intensity. Thus finite monitored regions inherit the asserted unconditional
mean weighted activity. This is not a new electric-weight observation, a
conditional hazard bound or convergence of the complete marked instrument.

For u=(4c_*)^-1 log(1/epsilon), the exponent contributes epsilon^-1/4,
so the two physical bounds are O(epsilon^(7/4)), exactly as stated.
Their epsilon^-2 rescaling is not uniformly bounded on this logarithmic
window. At fixed positive physical t the estimate grows exponentially in
epsilon^-2. The original(W1), positive-time microscopic source-cluster
weights, marked M4/process convergence, infinite-volume unbounded-rotor
dynamics and a uniform physical energy/current limit remain open.

No correction to either frozen proof is requested. The preparation
factorization and weighted closure above record the details I independently
used to verify the terse steps. No extra theorem, favorable simulation or
unread external result supplies those steps. Permitted reuse is only the
source-bound initial-layer and leading-fast form statement checked here.
