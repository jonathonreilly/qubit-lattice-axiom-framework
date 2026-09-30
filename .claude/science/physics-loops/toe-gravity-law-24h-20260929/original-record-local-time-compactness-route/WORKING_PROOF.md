# Uniform local-output time compactness for the actual microscopic law

Root author proof candidate. This has not received an independent check.
It keeps the supplied law and all original marks unchanged and uses the
checked defect and first-field-moment results. No numerical calculation is
needed for the proposed analytic statement. Main source and procedure
authority are as frozen in CONTRACT.md.

## 1. Statement and the exact output carrier

Fix a finite quantum region X of matter sites and links, a finite set F of
monitored A centers, a finite horizon T, finitely many fixed time-bin
boundaries, and a fixed total count cap M. The classical register keeps the
specified original mark labels and orders in those bins until overflow;
after overflow it keeps an absorbing flag. The physical system continues
to evolve with its actual generator. This is a coarse-graining of the
output, not a stopped or altered system law. Either original resolved or
original coherent instrument is used separately.

Write Gamma_(epsilon,L)(t) for the resulting joint classical-register and
local-quantum output from bare Omega. All integer-spin field bases are
embedded by their integer E labels in the same rotor link spaces. The
matter and register spaces do not depend on spin or volume. Impose the
declared coupled scaling

 epsilon^2 S(S+1)=delta/K, with delta,K,kappa>0 fixed.

For small epsilon, all safe volumes containing the fixed enlarged geometry,
R>=1 and s,t in [0,T], the proposed bound is

 ||Gamma_(epsilon,L)(t)-Gamma_(epsilon,L)(s)||_1
       <= C_1 epsilon+C_2/sqrt(R)+C_3(R)|t-s|.       (T1)

The constants may depend on X,F,M,T, the fixed bin structure and supplied
couplings, but not on S,L,epsilon. C_3(R) can grow with R. It suffices to
take S>=R; along the coupled limit this holds for every fixed R. Enlarging
C_2 makes the cutoff convention R versus floor R immaterial.

Consequently, for every sequence epsilon_j decreasing to zero and arbitrary
safe growing volumes, these exact outputs have a subsequence converging
uniformly on [0,T] in trace norm. Its limit is continuous, positive,
trace one, and diagonal in the classical register. The local A sites are
occupied in the limit. There is no assertion of a unique limit, a particular
quantum generator, spatial boundary independence or a uniform global
trace-norm speed. A countable family of fixed output specifications admits
a common diagonal subsequence; no continuous-timestamp total variation
statement is inferred.

## 2. Joint registers and the actual normal form

Attach the classical register by the actual original jump update at each
monitored center. On a block-diagonal classical-quantum observable A, the
gain for mark mu reads j_mu* A_(updated history) j_mu and the loss is the
actual anticommutator in its current history block. Updates are contractions
in the supremum norm over history blocks. The absorbing overflow update
has the same property. Equivalently the classical update has a Kraus column
with sum V_z*V_z=I, all sharing the same physical j_mu. Its completely
bounded cross estimates are independent of the register dimension.

Extend the exact order-six physical circuit Y by identity on this register.
It leaves the observed labels and history updates unchanged, and the jumps
become J_mu=Y j_mu Y*. Use sigma=Y rho_joint Y*. The physical marginal of
rho_joint is exactly the unmonitored microscopic ensemble. Thus the checked
physical per-site hole and first-field-moment bounds apply to it unchanged.
No conditional or postselected bound is being assumed.

For every A site a, the finite circuit estimate gives

 Tr[sigma(t) w_a] <=2 Tr[rho_joint(t) w_a]+C epsilon^2
                  <=C epsilon^2(1+T), 0<=t<=T.       (T2)

Indeed, for a vector w_a Y psi=Y w_a psi+[w_a,Y]psi and
||[w_a,Y]||<=C epsilon. This norm estimate comes from the bounded cone of
Y* w_a Y-w_a; it does not say [w_a,Y] is locally supported. Convexity gives
the mixed-state inequality. It remains valid with the attached register.
Summing finitely many sites bounds any local hole union, with its explicit
support-size constant. Translation symmetry was used only in the already
proved physical bound, not in sigma or the circuit coloring.

On joint observables the exact transformed generator has the same structure
as in the defect proof:

 L'^* =i delta epsilon^-4[W,.]+epsilon^-2 B2
                                  +epsilon^-1 C1+R_epsilon,
 B2=i delta[D2,.]+kappa sum_mu D[j_mu]^*,             (T3)

where the original register updates are included in the dissipators. C1 is
the complete first jump cross map, including its gain and loss; its physical
grades on a grade-zero input are +/-1. R_epsilon has bounded local action
strength on norm-bounded observables. The higher Hamiltonian diagonal terms
are delta D4+delta epsilon^2 D6, with no odd diagonal coefficient; the
remaining Hamiltonian is O_local(epsilon^3). The exact jump remainder after
j+epsilon j1 is O_local(epsilon^2). These facts give (T3), including all
same-mark interference, uniformly in spin and volume.

An unmonitored term disjoint from the physical support of A cancels between
gain and loss. A monitored term can act on the register even if it is far
from X, but there are only the fixed finite centers F. Their bounded circuit
cones are included in the local support count. Each register update uses its
current fixed bin; the generator may change at the finitely many bin times,
with the same bounds on every interval and almost everywhere on [0,T].

## 3. Cutoff tests and the true electric coefficient

Let O be any norm-at-most-one classical-quantum observable on the output
carrier. It need not conserve W. Let P_A fill every A site in X. Let Y_E be
the finite link set consisting of all links in X and every link incident on
any matter site in X. This contains every electric polynomial that can fail
to commute with a test on X; adding a harmless fixed neighbourhood is also
allowed. Put P_R equal to the product of |E_e|<=R projections on Y_E and

 A=P_A P_R (O tensor I_(Y_E outside X)) P_R P_A.       (T4)

All these projections commute. Then ||A||<=1, [W,A]=0, and A commutes with
each individual A-occupancy projection w_a. It may change the charge sign
at an occupied A site. Outside X its extra field action is diagonal only.
The register action is unrestricted within its given finite space.

The actual second coefficient has the exact decomposition

 D2=D_vac+Cspin^-1 D_el,  Cspin=S(S+1),
 D_vac=sum_a F_a F_a*
       +sum_a F_a*F_a(Q_a-1)
       +sum_(a!=c)[F_a,F_c*],
 D_el=sum_(a,b~a) n_a(1-n_b) E_e(E_e+k_(a,b,q)) Q_a.  (T5)

Here k is the actual orientation-dependent +/-q_a and Q_a is the original
radius-two A-occupancy gate. This is the full spin coefficient, not its
rotor replacement. Each local summand of D_vac has uniformly bounded norm,
finite support and bounded incidence, and vanishes on the subspace with
all A sites in that support occupied. The cross terms are grouped with
their adjoints where necessary. The electric part is the actual diagonal
occupation-dependent polynomial from the supplied compensation source.

For any D_vac summand h_z whose commutator with A is nonzero, choose U_z
to contain all of its A sites and those of A. The no-hole projector P_(U_z)
commutes with A and is annihilated by h_z on both sides. Consequently

 [h_z,A]=Q_(U_z)[h_z,A]Q_(U_z), Q_(U_z)=I-P_(U_z),
 |Tr sigma i[h_z,A]|<=2||h_z|| Tr sigma Q_(U_z).      (T6)

Only boundedly many h_z occur. By (T2), their full epsilon^-2 contribution
is bounded by C_(X,F,T), independently of epsilon and volume. Using only
P[h_z,A]P=0 and a square-root bound here would be insufficient; the two-sided
hole support in (T6) is essential.

The gates Q_a and n_a commute with A. An electric term can fail to commute
only through a field in X, a charge at an A site in X, or occupancy of a B
site in X. Its link is therefore in Y_E. For such an edge, both A's input
and output on that link lie in |E_e|<=R. Thus

 ||[n_a(1-n_b)E_e(E_e+k)Q_a,A]||<=2(R^2+R).

All other electric terms commute with A exactly, including the terms whose
only overlap is a diagonal auxiliary cutoff. There are finitely many
possibly noncommuting edges. Since delta/(epsilon^2 Cspin)=K exactly,

 |Tr sigma i delta epsilon^-2[Cspin^-1 D_el,A]|
                                             <=C_X K(R^2+R). (T7)

This is why a cutoff only on the original output links could fail: changing
a B occupation also changes electric coefficients on its other incident
links. No second-moment estimate is used in (T7).

## 4. Original jumps and their coherent cross terms

Every bare original j_mu acts on an input hole at its center a. Since A
commutes with w_a, both its gain and its anticommutator loss, with the
actual register update, are supported on w_a on both input sides. Therefore

 |Tr sigma D[j_mu]^*A|<=2||j_mu||^2 Tr sigma w_a.     (T8)

This holds for the complete coherent mark as well as each resolved mark;
no sign cross term is discarded. The finite relevant mark set consists of
the monitored marks and those whose physical support meets A. Equation(T2)
makes the epsilon^-2 bare dissipator contribution uniformly bounded.

For the first cross map, j1=[-F+F*,j] has grades zero and minus two. On the
grade-zero A in (T4), the full gain/loss cross operator consequently has
grades +/-1. For the finite union U of its physical A support, its
compression to the all-occupied subspace is zero. The complete cross-map
norm is bounded by a constant times ||j||||j1||||A||, including the
classical update. Cauchy on the occupied/hole blocks gives

 |Tr sigma C1 A|<=C sqrt(Tr sigma Q_U)
                                      <=C epsilon sqrt(1+T). (T9)

Multiplication by epsilon^-1 gives a uniform bound. All higher jump terms
are in the bounded local remainder of (T3); neither their gain nor loss is
removed. The Hamiltonian remainder has the same uniform local property.
The W commutator vanishes exactly on A. Combining (T6)-(T9) proves

 |d/dt Tr sigma(t) A|<=C_(X,F,M,R,T)                  (T10)

almost everywhere. This is an expectation bound in the actual joint state,
not a claim that the generator's operator norm is uniform or that the
global state has bounded trace-norm derivative.

## 5. Removing auxiliary tests and proving the trace-norm modulus

The physical hole and first-moment bounds give uniformly on [0,T]

 p_A<=C_X epsilon^2(1+T),
 p_E=Tr rho_joint(I-P_R)<=C_T |Y_E|/R.               (T11)

The gentle projection inequality, valid also on the classical-quantum
joint state, then implies

 |Tr rho_joint(t) O-Tr rho_joint(t) A|
                                      <=C epsilon+C'/sqrt(R). (T12)

Here O is extended by identity on the auxiliary links. No history-conditioned
field tail is required; the marginal supplies the joint projection tail.
The finite circuit also gives

 |Tr rho_joint(t) A-Tr sigma(t) A|<=C_(X,Y_E) epsilon. (T13)

This is an ordinary bounded-local-observable estimate with ||A||<=1.
Its constant need not depend on R, on the register matrix dimension or
on ||E||. The physical support of the test is fixed as R changes. The
register is untouched by Y.

Apply (T12)-(T13) at both endpoints and integrate (T10). The constants are
uniform over every norm-at-most-one O. Trace duality on the output carrier
therefore proves (T1). For small finite spin the restriction S>=R is
irrelevant to a limiting sequence; for each fixed R it holds on its tail.
This proof does not differentiate a cumulative mean-mark error.

## 6. Uniform-in-time subsequences and limits of the result

For any desired tolerance, first choose R so the second term of (T1) is
small, then take the tail of a sequence epsilon_j->0 so its first term is
small, and finally choose a time increment using the finite C_3(R).
Finitely many discarded paths are individually continuous. This proves
equicontinuity of the sequence in the common trace-norm carrier.

At each time, the checked first moment uniformly approximates all states
by their block on finitely many electric levels. Matter and the fixed
capped/binned register are finite dimensional. Adding a refusal state if
desired normalizes the approximation with an error tending to zero.
Thus the possible output states are totally bounded in trace norm,
uniformly in time. Diagonal extraction on a countable dense time mesh,
followed by the equicontinuity estimate, gives a uniformly Cauchy subsequence
on [0,T]. Completeness of trace class gives the asserted continuous limit.
Positivity, unit trace and classical block diagonality are closed properties.
The vanishing local hole probability gives support on occupied A sites.

The same diagonal argument works for a countable collection of fixed
regions, horizons and binned/capped output specifications. Algebraic
consistency under the corresponding fixed partial traces/coarse-grainings
is preserved. This alone is not a theorem identifying a continuum-time
instrument, and no timestamp topology has been changed silently.

The limit's quantum evolution remains unspecified. A finite first moment
does not provide second-moment uniform integrability or control the
epsilon^-2 source-weighted tails. Uniform first count moments likewise
do not by themselves give uniform integrability of unbounded count
observables; a mean identity cannot be passed to an uncapped limiting count
law without a separate argument. Spatial boundary independence, uniqueness,
weighted W1 and changing-source fast feedback remain open. The result is
a local trajectory compactness prerequisite for those identification
problems, not their solution or a new physical-law selection.
