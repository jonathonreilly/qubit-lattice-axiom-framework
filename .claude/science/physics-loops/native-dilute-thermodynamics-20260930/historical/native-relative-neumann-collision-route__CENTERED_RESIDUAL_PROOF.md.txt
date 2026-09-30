# Compatible residual duality and the actual fixed-n open-cell interaction

New author analytic candidate. No numerical computation or formal grade.
The target was frozen in CENTERED_RESIDUAL_CONTRACT.md after disclosure of
the mechanism, before this complete written proof. This argument uses the
now focused-checked physical boundary theorem eb823182, receipt92624c8e.
It does not use the periodic interaction coefficient as the coefficient of
an open cell. Its new step is a compatible centered-source dual estimate
on actual removal amplitudes.

## 1. Exact statement and order of limits

Keep mu,tau>0, a=min(tau,mu/12), fixed guard R0>=14 and the physical vertex
cube Lambda of side ell. For0<eta<=1/2 and0<gamma<=1 use exactly

 H_plus=H_base+gamma ell^-2 N_partial,
 H_base=(1-eta)(S_Lambda+W_Lambda)+eta a Egrad15,Lambda+mu D_safe.

All boundary rows, the safe diagonal and the orientation-dependent soft
Gram G_ell are as in the checked boundary proof. V=ell^3. In the physical
N=2n sector let V_n be its polar guarded isometry from Sym^n C5, Q_n the
orthogonal complement of its range, C_n,ell=Q_n H_plus Q_n, and

 S_n,ell=V_n^*H_plus V_n
       -V_n^*H_plus Q_n C_n,ell^-1 Q_n H_plus V_n.                (1)

For each fixed n, eta and gamma these exist for all sufficiently large ell.
The checked gap is C_n,ell>=c(eta,gamma)ell^-2, with

 c(eta,gamma)^-1 <= C[eta^-1+gamma^-1],                           (2)

where C depends on fixed R0,mu,tau, not n or ell.

Define the infinite-volume comparison law

 H_eta=(1-eta)(S+W)+eta a Egrad15+mu D,
               (1-eta)H0 <= H_eta <= H0.                        (3)

Let T_eta be its ACTUAL physical N4, total-momentum-zero threshold form,
with the same incoming normalization Phi_A=(1/sqrt2)sum A_ab C_a C_b Omega
and ||A||_HS. Its free kernel is still the five constant modes U. Equivalent
energy norms and the common affine incoming class give

             (1-eta)T0 <= T_eta <= T0.                           (4)

Write mathcalT_eta,n=sum_(i<j) T_eta^(ij) on Sym^n C5, zero at n=0,1.
The candidate result is

 limsup_(ell->infinity)
 || V S_n,ell - mathcalT_eta,n ||
                <= C_(n,eta)[gamma+gamma^2/eta].                 (5)

Constants in this displayed convenient form need not be sharp. In particular

 lim_(eta->0) lim_(gamma->0) limsup_(ell->infinity)
 ||V S_n,ell-mathcalT_0,n||=0.                                   (6)

This is a fixed-n theorem with ordered limits. No uniform-in-n rate, useful
finite-density threshold, many-cell lower law, EOS or phase conclusion is
contained in(5)-(6). The proof below also applies to all the finite internal
matrix entries, not only a coherent direction or an eigenvalue minimum.

## 2. A polynomial version of the physical spectator bound

The previously checked local pin argument can be quantified without a
large matrix spectrum. On the clipped box B_y at radius r=R+6 choose a
common anchor x0 at least two sites from its faces. Each component anchor
domain is a connected rectangle. Coordinate paths of length at most C r
connect any anchor, including an incident-to-y pin anchor when available,
to x0. Cauchy along the path gives

 |f_d(x)-f_d(x0)|^2 <= C r Egrad_d.

The three axial values at x0 are bounded by C r Egrad, since all three
axial types have an incident-to-y pin. In each plane one type has such a
pin. One complete plane difference at an interior center bounds the other
constant value through their sum; its finitely shifted anchor values differ
from those at x0 by gradient terms. Thus, with v_d=f_d(x0),

 sum_d |v_d|^2 <= C[S_(B_y)/mu+r Egrad9].

Summing the first path estimate over at most C r^3 anchors proves

 C_pin(R)<=C(1+R)^4,
 E_R^near <= C(1+R)^7 J_Lambda.                                 (7)

The second factor R^3 is exactly the spectator/row incidence from the
checked proof. The constants are absolute for the fixed nine row types;
no eigenvalue computation is being asserted. All boxes satisfy ell>=2R+13.

If a vector b is supported on physical configurations with an occupied
graph edge and a third particle within distance R, its support projector
is bounded by E_R^near. Combining(7) with H_base>=eta a J_Lambda gives

 |<b,psi>|^2 <= C(1+R)^7/(eta a) ||b||^2 <psi,H_base psi>.        (8)

This is a genuine energy-dual bound on the SAME physical Hilbert space.
It is useful for boundary collision sources. It neither constructs a
physical state by separately optimizing removal fibers nor controls a
global no-defect projection by a small defect fraction.

## 3. Actual threshold cutoffs for the comparison law

The checked adiabatic threshold construction applies to H_eta directly.
Here are the required properties and why they persist; no new threshold
matrix entry is supplied. Its finite-range nine-bond symbol is Hermitian,
has the same U kernel at zero, a four-dimensional high gap at least mu,
and is bounded below by(1-eta)a ell(k)I. The N4 nonmatching compression is
at least(1-eta)mu, by the original N4 diagonal argument. Thus its exact
Schur core, compact-source duality and incoming energy completion exist.

In its free81-channel exterior, eliminate the constant high block. That
block has an analytic exponentially local inverse. The soft Schur symbol
has zero zeroth and first spatial moments and quadratic positive behavior.
Fourier annuli give the zero-energy response soft part O(r^-1), its first
finite difference O(r^-2), and the high part O(r^-2). Cut the soft response
by a smooth cutoff at radii R,2R, then reconstruct the high field by its
full inverse. The soft commutator has two cancellations and is O(R^-3) on
an O(R^3) shell. Its high residual vanishes before the final exponential
truncation. Restore exact response values in the fixed physical source
core, impose its actual matching relations and truncate high/nonmatching
tails beyond C R. All these repairs have exponentially small residual.
This repeats the actual symbol/core derivation for(3), whose coercivity is
uniform for eta in a compact subinterval of[0,1/2]; it is not a bosonic
replacement of the core.

Consequently there are physical four-site creators D_R,A with translated
vacuum coefficients chi_R,A/sqrt2, linear in A, such that

 ||chi_R,A||_2^2 <= C_eta R ||A||^2,
 chi_R,A=chi_eta,A on the fixed support of every F_eta,B,
 E_eta(Phi_A+chi_R,A)=T_eta[A]+O_eta(R^-1)||A||^2.                 (9)

The actual residual H_eta,4(Phi_A+chi_R,A) has a decomposition into:

 (i) a two-graph-edge matching field on unique, separated matchings,
     with ordered kernel k_R,de(r), support |r|<=C R,
     |k_R,de(r)|<=C_eta R^-3 and sum_r |k_R,de(r)|<=C_eta;
 (ii) a physical residual of norm at most C_eta exp(-c_eta R),
      supported at diameter C R and having an occupied graph edge.

Changing the harmless constant C or including exponentially small shell
pieces in(ii) permits the pointwise bound in(i) globally. The exact factor
between the ordered creator kernel and the physical amplitude is fixed by
counting its two ordered matching representations; it is retained in the
creator identity below. All bounds are linear/operator bounds over the
full15 incoming space. There is no square-summable zero-energy minimizer
assumption.

The last assertion about(ii) follows also from the physical invariant
subspace: every offdiagonal term annihilates and creates a graph edge.
The all-no-graph-edge configurations are diagonal and decoupled from the
incoming state, so its response and residual have no such component.
The exponential estimate survives the finite physical core repair.

## 4. A compatible centered-source lemma on the true anchor rectangles

Let B_e=b_x b_(x+d), e=(x,d), x in Omega_d(Lambda). A two-pair creator with
kernel k has the form

 R_k^* = sum_(e,f) k(e,f) B_e^* B_f^*.                           (10)

Numerical factors such as1/2 belong to k. Overlaps vanish by the original
qubit algebra. For the unnormalized uniform soft creator
C_z=sum_(x,d) U_d z B_(x,d)^*, with ||z||=1, put

 r=V^(-n/2) R_k^* C_z^(n-2) Omega,       n>=2.                   (11)

Fixed factorial factors can be absorbed into constants for this lemma.
Suppose each column k((x,d),f) has support in an O(R^3) set, magnitude
at most C R^-3 and l1 norm at most C, uniformly in f,d. Restriction to the
actual cell is allowed. These hypotheses hold for part(i) of section3.

The exact creator identity r=sum_e B_e^* v_e uses

 v_e=V^(-n/2) sum_f k(e,f) B_f^* C_z^(n-2)Omega.                  (12)

In a physical output occupation xi of2n-2 sites, set
beta_xi,f=<xi|B_f^* C_z^(n-2)Omega>. It is zero unless f is an occupied
graph edge of xi, of which there are at most9(2n-2). These coefficients
are independent of e. This is why the following centering is compatible
with actual hard-core amplitudes.

Center EACH column on its complete valid-anchor rectangle:

 k_c((x,d),f)=k((x,d),f)
       -|Omega_d|^-1 sum_(x' in Omega_d) k((x',d),f).             (13)

For fixed xi,d, the resulting v_c(x,d;xi) has zero spatial mean. This
includes positions where e meets xi. At those positions the physical
removal amplitude <xi|B_e psi> is zero, but v_c is still defined. One must
not delete those positions before centering. The creator identity and its
pairing with removal amplitudes remain exact because creation into an
already occupied site vanishes.

For a scalar field u on any of these rectangular domains, Neumann
Poincare followed by reflected discrete Sobolev gives

 ||u-mean u||_6 <= C ||gradient u||_2.                            (14)

All side lengths are ell,ell-1 or ell-2, so C is uniform for ell>=8.
This is the same elementary mean-zero Neumann inequality proved in the
relative-Neumann argument: reflect across faces, cut off at the box scale,
apply the infinite discrete |u|^4/BV Sobolev estimate, and use Poincare on
the cutoff error. It does not use positivity of a matrix heat kernel.

Hölder and(14) imply for every mean-zero source s

 |sum_x conjugate(s_x)u_x|^2
                      <= C ||s||_(6/5)^2 Egrad(u).

An uncentered column in(13) has l^(6/5) norm at most C R^-1/2.
Its removed constant has norm at most C ell^-1/2. Therefore

 ||k_c(.,d;f)||_(6/5)^2 <= C(R^-1+ell^-1).                       (15)

Use the triangle inequality over the at most9(2n-2) occupied f in xi,
Cauchy over that finite set, and then sum over xi. The physical identity
and hard-core creator norm give

 sum_(xi,f)|beta_xi,f|^2
   =sum_f ||B_f^* C_z^(n-2)Omega||^2
   <=9V ||C_z^(n-2)Omega||^2 <=C_n V^(n-1).                     (16)

The last inequality follows by embedding physical occupations into canonical
SITE-boson Fock space, multiplying symmetric tensors and projecting back
to at most one boson per site. For a k-site creator A_g on an m-site sector,
||A_g||<=sqrt(binom(m+k,k))||g||. Since all factors create, forbidden repeated
sites cannot later reenter the allowed space. No pair CCR is assumed.

Combining(12)-(16), summing actual removal gradients and using(5) of the
boundary proof gives

 |<r_c,psi>|^2
 <= C_n/(eta a V) (R^-1+ell^-1) <psi,H_base psi>.                (17)

This holds for every physical psi, with its true spectator compatibility.
A finite coherent polarization/resolution of Sym^n C5 extends the estimate
from z^n to the full internal input space with a finite n-dependent constant.
For example coherent powers span that finite-dimensional space; a fixed
finite spanning frame has a finite inverse Gram bound. Uniformity as
n increases is not asserted here.

The removed column-mean source r_m=r-r_c has a different useful estimate:

                         ||r_m|| <= C_n/V.                      (18)

To prove it, for each d factor its creator as

 [sum_(x in Omega_d) B_(x,d)^*]
 [sum_f b_d(f) B_f^*]/|Omega_d|,
             b_d(f)=sum_(x in Omega_d) k((x,d),f).

The first vacuum norm is O(sqrt V); the second is O(sqrt V) since
|b_d(f)|<=C. The site-creator inequality used in(16), together with
|Omega_d| comparable to V and the n-2 spectators, proves(18).
Neither b_d(f) nor the actual rectangle counts need be translation invariant.
Using the physical Q_n gap only on this small mean part yields

 V <Q_n r_m,C_n,ell^-1 Q_n r_m>
                   <= C_n[eta^-1+gamma^-1]/ell.                  (19)

Thus no exact conditional identification of that mean with a scalar hazard,
a boson operator or the target threshold matrix is needed. The P_n part of
the mean carries the order V^-1 interaction and is not bounded using(19).

## 5. One physical many-pair trial and its actual cell residual

Use the same coherent polynomial construction, now restricted to the true
physical cell. All creation words must have every site inside Lambda:

 B_n z^n=C_z^n Omega/(sqrt(n!) V^(n/2)),
 Psi_n,R z^n=sqrt(n!) V^(-n/2)
       [C_z^n/n!+D_R,z^2 C_z^(n-2)/(n-2)!]Omega.                 (20)

For n<2 the correction is absent. This is a single actual physical vector
for each input polynomial. Alternative matchings add their literal phases,
overlapping words vanish, and every coefficient is shared by all removals.
At n=2 the construction is exactly(Phi+chi_R)/V in the interior, which fixes
the pair factor. The normalized open-cell soft frame instead uses
U G_ell^-1/2; since G_ell/V=I+O(ell^-1), this only changes its overlap with
(20) by O_n(ell^-1). The creator bound and isolated-edge Gram bound imply

 A_n,R,ell=V_n^* Psi_n,R -> I,
 ||Psi_n,R-B_n||<=C_n sqrt(R/V),
 ||B_n-V_n||<=O_n(ell^-1)+O_n(V^-1/2).                           (21)

Every limit in this section has FIXED n,R,eta,gamma before ell grows.

Expand H_base Psi using actual local words. The following classification
can be verified directly by commuting pure creators through each finite
local number-preserving monomial; it does not invoke an unspecified cluster
theorem.

(a) Bulk four-particle terms are exactly the N4 residual of section3,
    multiplied by C_z^(n-2), with its n2 factorial normalization.
(b) Terms with at least three interacting pairs have norm squared
    O_(n,R,eta)(V^-2).
(c) Boundary four-particle differences have norm squared
    O_(n,R,eta)(ell^2/V^2), and their configurations contain a nearby
    spectator and an occupied graph edge within distance C R.

Here is a detailed count and the boundary-law check. A connected local
source involving r pairs has O(V) translated placements in the bulk and
finite support at FIXED R. Multiplication by n-r distant pair creators and
normalization V^-n/2 gives squared norm at most C_(n,R) V^(1-r), using the
site-creator inequality. For r>=3 this is O(V^-2). A disconnected product
of the one four-particle correction and an original interaction source
has at most two free cluster placements and involves at least four pairs;
its squared norm is at most C_(n,R) V^(2-r)<=C_(n,R)V^-2. Finite commutator
expansion exhausts the possibilities; all additional attachments meet one
of the original local noncreation sites, so there is no extra free center.
At fixed n the number of terms is finite and the constants may grow with n.

The safe boundary diagonal is not merely the old degree-three polynomial:
its additional term is a fixed-neighborhood occupancy polynomial, of degree
at most nineteen. This is explicitly allowed in this count. It has bounded
support and coefficients and only finitely many creator commutators. Its
one-pair action, like every complete S/W/gradient row, annihilates C_z Omega:
a graph pair has safe diagonal zero and the constant U amplitudes cancel
each retained row. Thus there is NO one-pair source in H_base e^(tC)Omega.
The higher-degree boundary polynomial contributes only local sources of
at least two pairs, or commutators with the four-particle correction.
Boundary placements number O_R(ell^2), giving(c) at r=2 and smaller orders
at r>=3. This addresses the literal nonmonotone safe diagonal rather than
silently treating the open cell as periodic.

All four-particle boundary sources have an occupied graph edge. Every
output of a pair move has one; diagonal actions preserve it; correction
words have one by section3. Their diameter is C R. Multiplying by spectator
creators leaves that close cluster present unless the word vanishes by
hard-core exclusion. Hence(8) applies to their complete physical source.
Their Q-compressed inverse energy, multiplied by V, is O_(n,R,eta)(1/ell),
without the ell^2 gap loss. This is the essential boundary price.

For(b), the ordinary gap suffices: V ell^2 O(V^-2)=O(ell^-1), with the fixed
parameter factor in(2). The exponentially small nonmatching/repaired part
of(a) is supported at diameter C R with an occupied edge, so(7)-(8) bound
its volume-scaled inverse energy by C_(n,eta) R^7 exp(-c_eta R).
The main matching part of(a) is exactly the creator kernel(10)-(11).
Equations(17)-(19) control it by C_(n,eta)/R plus errors tending to zero.
Nothing in this application asks whether independently optimized fibers
could be assembled into a state; the single state is already(20).

## 6. The separately priced penalty residual

Let P_boundary=gamma ell^-2 N_partial. On the uncorrected finite soft input,
its boundary-number second moment is at most C_n/ell: N_partial<=2n and
its first moment is O_n(1/ell), by the actual anchor counts. This remains
true for B_n, including nonisolated matching amplitudes. To see it without
a false creation intertwiner, expand its finitely many pairings and apply
Cauchy over at most(2n-1)!! matchings; the unrestricted normalized site-pair
count with one boundary endpoint is O(1/ell).

Consequently

 ||P_boundary B_n||^2 <= C_n gamma^2 ell^-5.

The correction in(21) contributes O_(n,R)(gamma^2 ell^-4/V), since the
number operator is bounded by2n in this sector. By(2),

 limsup_(ell->infinity)
 V <Q_n P_boundary Psi,C_n,ell^-1 Q_n P_boundary Psi>
                    <= C_n[gamma+gamma^2/eta].                   (22)

Its contribution to V Psi^* H_plus Psi is at most C_n gamma+o_ell(1).
For the correction cross term, use the boundary probability of B_n and
the correction norm O_(n,R)(V^-1/2); after volume scaling its bound is
O_(n,R)(gamma/ell). Thus no endpoint or propagated interaction price is
being hidden in energy conservation or in a norm-only trial estimate.

## 7. Full internal energy normalization and the Schur identity

At fixed R all corrected creators have finite support. Expand the actual
physical occupation contractions in Psi^* H_base Psi. A leading connected
four-particle component has one free center and n-2 distant spectator edges.
The former has V+O_R(ell^2) allowed translations; the latter have
V^(n-2)+O_(n,R)(V^(n-3)+ell^2 V^(n-3)). Configurations in which another
spectator meets that component lose an independent center and are lower
order. Cauchy over their finite matching multiplicities bounds every such
remainder. No indefinite offdiagonal row is discarded.

On coherent inputs w^n,z^n the leading term is

 binom(n,2) E_eta,R(w^2,z^2) <w,z>^(n-2),
 E_eta,R(A,B)=E_eta(Phi_A+chi_R,A, Phi_B+chi_R,B).                 (23)

The factor is exact: D=chi/sqrt2, Phi=C^2/sqrt2, and n!/(n-2)! spectator
selection followed by the two-pair normalization gives n(n-1)/2. The same
coefficient is present on the complete Sym^n space by polynomial
polarization. Equations(9),(22)-(23) yield

 limsup_(ell->infinity)
 ||V Psi^* H_plus Psi-mathcalT_eta,n||
                           <= C_(n,eta)/R+C_n gamma.             (24)

For clarity, fixed-R finite support makes this elementary center count
sufficient; no long-range cluster expansion or convergence in n is used.
The polynomial degree of the boundary diagonal changes finite constants,
not the number of free centers. No separately computed threshold entries
or expected bosonic interaction coefficient are inserted.

For ANY trial map Psi, physical completion of the Q_n square gives exactly

 Psi^* H_plus Psi-A^* S_n,ell A
       =(Q_n H_plus Psi)^* C_n,ell^-1(Q_n H_plus Psi),
                         A=V_n^*Psi.                            (25)

Use a finite sum Cauchy bound on the residual classes above. From(17)-(22),

 limsup_(ell->infinity) V ||right side of(25)||
 <= C_(n,eta)[R^-1+R^7 exp(-c_eta R)
                                  +gamma+gamma^2/eta].          (26)

The norm is on the full finite internal input space. Constants may absorb
fixed numbers of residual classes. Since A->I and the right side is
positive, (24)-(25) bound ||V S_n,ell|| and permit replacing A by I with
an error tending to zero. Combining(24),(26), then sending R->infinity
AFTER ell->infinity at fixed n,eta,gamma, proves(5). Sending gamma->0,
then eta->0 and using(4), proves(6).

The point of this order is substantive. R is not required to exceed
ell^(2/3): the spread residual uses actual centered removal duality, and
only its O(V^-1) column-mean part uses the cell gap. Boundary sources use
the physical spectator estimate. An ordinary l2-residual-only argument
would not prove the stated ordered limit.

## 8. Limits of this candidate and required checking

This is a new, source-bound mathematical candidate, not the already checked
periodic theorem. It establishes only a fixed-n physical-cell interaction
limit if every step survives focused checking. In particular the following
are load-bearing and should be checked adversarially:

* Centering on all valid anchors before imposing spectator holes, and the
  exact hard-core creator adjoint pairing in(12)-(17).
* The O(V^-1) factorization of removed means and its use only on Q_n.
* The high-degree safe diagonal, absence of a boundary one-pair source,
  boundary-cluster support and its actual energy-dual price.
* The n2 pair factor and the physical matching center count in(23).
* The ordered limits with no asserted uniform n-dependent rate.

The method does not by itself control arbitrary cell occupation tails or
prove a thermodynamic lower EOS. A future application would have to combine
this fixed-n family with an actual tail-discard/particle-count argument,
finite-mode variance or de Finetti control, and the exact averaged boundary
penalty debit. Those steps are not imported by writing(6). No global dimer
isometry, independent removal minimization, condensate or phase is claimed.
