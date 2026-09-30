# A priced physical boundary penalty and an actual cell compression gap

Author analytic candidate, not independently checked. This is a second
result in the new route and does not use the frozen relative Neumann proof
as a premise. No numerical computation is used. The exact target and its
prior mechanism exposure are recorded in BOUNDARY_PENALTY_CONTRACT.md.
All earlier packets and root's boundary notes remain unchanged.

This argument repairs the free boundary-singleton obstruction to a physical
cell gap at a price of order gamma N/ell^3 after translation averaging. It
does not prove that the resulting cell Schur form has the full T0 interaction
coefficient. In particular it does not transfer the periodic Schur theorem
to a physical open cell.

## 1. Actual lower cells and the comparison penalty

Use the unchanged supplied qubit Hamiltonian and its simultaneous identity

 H=S+W+mu D,       S+W >= a Egrad15,       a=min(tau,mu/12)>0.

For a physical vertex cube Lambda={1,...,ell}^3 retain every complete
positive S/W row whose entire physical support lies in Lambda. Denote the
forms by S_Lambda,W_Lambda. Retain complete internal bare-pair difference
rows in Egrad15,Lambda. For x in Lambda let q_x be the number of actual
18-neighbors outside Lambda, m_int the occupied-neighbor count inside, and

 d_Lambda(x)=n_x min_(0<=j<=q_x) [(m_int+j-1)(m_int+j-2)/2].       (1)

This is the root ledger's safe nonnegative diagonal. The only difference
from the literal internal phi(m_int) is removal of its isolated-site penalty
when q_x>0. Define the width-two boundary set

 partial Lambda={x:q_x>0},       N_partial=sum_(x in partial Lambda)n_x.

For 0<eta<=1/2, gamma>0 set

 H_Lambda^base=(1-eta)(S_Lambda+W_Lambda)
                 +eta a Egrad15,Lambda+mu sum_x d_Lambda(x),
 H_Lambda^+=H_Lambda^base+gamma ell^-2 N_partial.                  (2)

All forms act on the actual physical cell tensor product. The added term
is a comparison penalty, not an altered model premise.

On a torus with L divisible by ell, average all translations of a disjoint
cube tiling. The simultaneous comparison and positive-row deletion give
H>=sum_cells H_Lambda^base for every tiling. A site is in the boundary of
its cell for at most the fraction

 p_ell=1-(ell-4)^3/ell^3 <=12/ell,       ell>=4.

Indeed the graph has axial displacements of length two. Hence the exact
operator comparison after translation averaging is

 H >= average_translations sum_cells H_Lambda^+
                                  -12 gamma N/ell^3.             (3)

There is no IMS localization of the state, boundary energy deletion or
assumption about the state on the boundary. Equation(3) holds for coherent
states and arbitrary particle-number distributions. Nondivisible torus
remainders are not included in this assertion; the thermodynamic sequence
can be chosen divisible by each fixed ell.

## 2. A boundary-aware physical spectator pin

Use unique forward edges d=2e_i,e_i+/-e_j and let

 Omega_d(Lambda)={x:x,x+d in Lambda}.

Each is a rectangular anchor domain. For a nine-component field f on these
domains let

 J_Lambda(f)=Egrad9,Lambda(f)+S_Lambda(f)/mu.                      (4)

All S rows are the literal centered singlet/plane rows rewritten in forward
coordinates; no omitted component is replaced by a constant. The internal
fifteen-gradient form dominates the nine-gradient form by the actual axial
translations and duplicate plane representations. Since eta a<=(1-eta)mu,

                 H_Lambda^base >= eta a J_Lambda.                (5)

Fix R>=4 and r=R+6. Assume ell>=2r+1. For y in Lambda set
B_y=Lambda intersect (y+[-r,r]^3), a rectangular vertex box whose side
lengths lie between r+1 and 2r+1. On its valid edge-anchor domains impose
f(e)=0 for every edge incident to y. There exists a finite C_pin(R),
independent of ell,y, such that

 sum_(e subset B_y)|f(e)|^2 <= C_pin(R) J_(B_y)(f).                (6)

Here J_(B_y) retains only complete rows inside that physical vertex box.
The estimate includes face, edge and corner positions of y.

To prove(6), first determine the exact finite-dimensional zero space. If
J_(B_y)=0, every component is constant on its connected rectangular anchor
domain. Complete interior S rows then put the nine constants in range U,
the actual five-dimensional constant soft space. There is at least one
edge incident to y of each axial type: in each coordinate at least one
side has length at least r, so a displacement of either +2 or -2 is valid.
These three pinned axial rows of U kill both E components. For each plane
ij choose signs sigma_i,sigma_j for which y+sigma_i e_i+sigma_j e_j lies
in B_y. Its edge is of one of the two forward plane types. The corresponding
row of U has magnitude1/sqrt2 in that plane's T column, and pins that
component. Thus all five soft constants vanish. There are only finitely
many possible box shapes and marked positions at fixed r, up to translation
and axis permutation. Take C_pin(R) to be the largest reciprocal smallest
eigenvalue of their pinned J matrices. Every one is strictly positive by
the preceding kernel proof. This is a finite, exact definition of a constant;
no numerical eigenvalue, favorable estimate or uniform-in-R bound is claimed.

For a physical vector psi and an output occupation eta_occ define the
literal removal amplitudes

 f_eta_occ(e)=<eta_occ|b_x b_(x+d)|psi>.

They vanish whenever e meets eta_occ. Every actual J row norm is the sum
of its amplitude-row norm over eta_occ. If an occupied removed edge has a
spectator y at distance <=R, it is contained in B_y and has the pins in(6).
Summing (6) over these spectators and output configurations gives

 <E_R^near> <= C_R J_Lambda(psi),
 C_R=C_pin(R)(2r+5)^3,                                          (7)

where E_R^near counts occupied graph edges having another occupied site
within Chebyshev distance R of either endpoint. To check incidence, a fixed
row can occur only for y within r+2 of one of its fixed anchors; there are
at most(2r+5)^3 such physical sites, irrespective of the particle number.
Each removal edge with at least one close spectator is included at least
once. No removal fiber is independently minimized, and all amplitudes in
this sum come from the same physical psi. Equation(7) is an operator-form
inequality by this literal amplitude decomposition.

Let B_R count particles outside R-isolated graph dimers, with isolation
measured only against other sites of Lambda. Every bad particle with a
graph neighbor belongs to an edge counted by E_R^near: a connected graph
component with at least three vertices has a third vertex within distance
two of an endpoint of each edge; a two-vertex component which is not isolated
has the close spectator by definition. Isolated singletons are charged to
d_Lambda unless they lie in partial Lambda. Thus pointwise

 B_R <= sum_x d_Lambda(x)+N_partial+2 E_R^near.                   (8)

This separates the free boundary singleton count from the nearby-edge
energy estimate. Charging all guard errors to B_R would lose this separation
and would unnecessarily introduce a factor ell^2 from the penalty.

## 3. Guarded rows, with no boundary-singleton loss

Fix an integer R0>=14 once and for all. For valid edges use the same actual
isolated-pair selection as on the torus, but only inside Lambda. The map
I sends a physical occupation to its set of selected isolated graph edges
in auxiliary bosonic Fock space and its complete remaining site occupation
in an environment register. Recovering the original occupation by union
proves that I is an isometry. Removing a selected edge does not change any
remaining selection or the environment, so guarded annihilation intertwines
exactly with auxiliary edge annihilation. Creation is not assumed to do so.

In an output occupation eta_occ the guard is
q(e)=1_{dist(e,eta_occ)>R0}. For every complete internal J row l, choose an
edge e0 in that row. The elementary row estimate is

 |sum_e l_e q_e f_e|^2
 <=2|sum_e l_e f_e|^2+2||l||^2 sum_e |q_e-q_e0| |f_e|^2.          (9)

The row diameter is at most four in edge Hausdorff distance. Unequal guards
therefore imply that the input edge has a spectator within R0+4. The
weighted row incidence is at most fifteen: twelve from gradients, at most
three from the actual S rows. Missing boundary rows only decrease it.
Combining(7),(9) yields, uniformly in particle number and ell,

 J_guard <= D_R0 J_Lambda,
 D_R0=2+30 C_(R0+4).                                            (10)

No boundary particle count appears in(10). The local pin proof is applied
to actual boundary-truncated boxes. In particular this estimate cannot be
obtained by extending every field by zero and silently restoring lost rows.

## 4. The actual five open-cell soft modes

Let F_ell be the five-dimensional subspace of fields
f_d(x)=U_d z on all x in Omega_d. Its Gram matrix is

 G_ell=sum_d |Omega_d| U_d^* U_d,
             (ell-2)^3 I5 <= G_ell <= ell^3 I5.                  (11)

The normalized embedding is W1:z -> (U_d G_ell^-1/2 z)_d,x.
This uses the true orientation-dependent anchor counts. It is not the
periodic normalization ell^-3/2 U.

The internal one-body form J_Lambda satisfies

 dist(f,F_ell)^2 <= C_s ell^2 J_Lambda(f),                        (12)

with a numerical constant C_s, for all sufficiently large ell. Here is an
elementary derivation. Subtract the separate mean m_d on each rectangular
Omega_d. Scalar Neumann Poincare bounds the remainder q by
||q||^2<=ell^2 Egrad9/4. On a common interior cube, all constant-component
S rows are present and their constant form is2||P_high m||^2 per center.
The number of such centers is at least(ell-4)^3. The complete infinite S
symbol is bounded by2mu, so zero-extending q for this estimate gives
S_inner(q)<=2mu||q||^2. The square triangle inequality bounds
(ell-4)^3||P_high m||^2 by S_Lambda(f)/mu+2||q||^2. Approximating f by the
constant field U U^*m then proves(12), for example with C_s=64 when ell>=8.
The zero extension here is only an upper bound on the error's retained S
rows; it adds no row to the physical lower Hamiltonian.

Let Exc be the auxiliary number outside F_ell. Literal guarded removal and
(10),(12) imply on physical states

 I^* Exc I <=64 ell^2 D_R0 J_Lambda.                             (13)

## 5. An actual physical compression gap, including all environments

Work in the physical sector N=2n. Let W_n embed Sym^n C5 into the auxiliary
Fock space with all n pairs in F_ell and empty environment. Put

 T_n=I^* W_n,       G_n=T_n^*T_n.

The image of I with empty environment consists exactly of edge occupations
whose n edges are distinct and pairwise R0-isolated. A forbidden pair of
edges has at most C_b(R0) choices of its second edge given its first. By(11),
the compression to F_ell of the indicator of any such collection has norm
at most C_b/(ell-2)^3. Condition on the first edge, then sum its exact
one-body evaluation resolution of identity. The pair union bound on an
arbitrary symmetric n-mode vector gives

 G_n >=(1-delta_n) I,
 delta_n=binom(n,2) C_b(R0)/(ell-2)^3.                            (14)

This includes repeated auxiliary edge occupation and shared-site conflicts;
it is not a classical product-state estimate. A safe explicit choice is
C_b(R0)=18(2R0+9)^3, since either endpoint of the second edge must lie in a
bounded neighborhood of an endpoint of the first. No sharp constant is used.

Assume delta_n<1. Define the physical isometry
V_n=T_n G_n^-1/2 and P_n=V_n V_n^*. Its rank is binom(n+4,4).
On the auxiliary fixed physical-number space the complement of the
all-soft/empty-environment subspace is bounded by N_environment+Exc.
Using(8),(13) and the positive terms in(2) yields

 I-T_n T_n^* <= C_gap ell^2 H_Lambda^+,
 C_gap=1/mu+[2 C_R0+64 D_R0]/(eta a)+1/gamma.                    (15)

The right side follows term by term; constants are deliberately not sharp.
Since T_n T_n^*<=P_n,

 H_Lambda^+ >= Delta_ell (1-P_n),
                    Delta_ell=(C_gap ell^2)^-1.                 (16)

This is an operator inequality on the full physical N=2n sector, with all
bad environments retained. For odd N the all-soft/empty-environment space
is absent, so the same argument gives H_Lambda^+>=Delta_ell. The constants
are independent of N, ell and the state. Equation(16) is not an assertion
that P_n is an invariant eigenspace or that H_Lambda^+ annihilates it.

## 6. Compatible trial bound and a genuinely physical finite Schur operator

Every occupation contributing to T_n consists of isolated actual graph
edges, so its diagonal d_Lambda energy is zero. For a remaining selected
(n-1)-edge occupation eta_occ the removed-edge amplitude before guarding is

             U_d G_ell^-1/2 v_eta_occ,
             sum_eta_occ ||v_eta_occ||^2 <= n.

This is the literal auxiliary annihilation identity, not independent
optimization of the removal amplitudes. Every complete S/W/gradient row
annihilates these constant soft amplitudes before the guard is applied.
A nonzero guarded row lies within a fixed shell of one of the2(n-1)
remaining occupied sites. The number of such rows is at most C(R0)(n-1),
with bounded row coefficients, while(11) supplies an ell^-3 squared-amplitude
factor. Thus for a fixed finite C_t=C_t(mu,tau,R0), independent of eta<=1/2,

                T_n^* H_Lambda^base T_n
                   <= C_t n(n-1)/ell^3 I.                        (17)

The boundary penalty has a separate direct price. Its compression to the
five soft modes is bounded by C_partial/ell per pair, because at most
C ell^2 valid edges have an endpoint within the width-two boundary and
G_ell>=c ell^3 I. Restricting to the diagonal isolated-edge image decreases
this positive diagonal observable. Consequently

 T_n^* H_Lambda^+ T_n
       <=[C_t n(n-1)+C_partial gamma n]/ell^3 I,
 V_n^* H_Lambda^+ V_n <= theta_n I,
 theta_n=[C_t n(n-1)+C_partial gamma n]/[ell^3(1-delta_n)].         (18)

For theta_n<Delta_ell, min-max and(16) put exactly binom(n+4,4) physical
levels below Delta_ell. Writing Q_n=1-P_n, the actual complement compression
C_n=Q_n H_Lambda^+ Q_n satisfies C_n>=Delta_ell Q_n. The finite physical
Schur matrix is therefore well defined:

 S_n,ell=V_n^*H_Lambda^+V_n
       -V_n^*H_Lambda^+Q_n C_n^-1 Q_nH_Lambda^+V_n.               (19)

The same elementary block resolvent argument as for any positive finite
matrix gives, for ordered low eigenvalues lambda_j and Schur eigenvalues s_j,

 lambda_j<=s_j<= [1+theta_n/(Delta_ell-theta_n)]lambda_j.          (20)

This is applied to the physical open-cell operator(2), not imported from a
periodic spectrum. One may verify(20) by eliminating Q at spectral parameter
lambda, comparing C_n^-1 with(C_n-lambda)^-1, and using positivity of the
zero-parameter block Schur complement and V_n^*H V_n<=theta_n.

## 7. What this changes, and what remains unproved

The formerly free boundary singletons are now priced by a comparison term
whose original-Hamiltonian cost is(3). The cluster/guard estimate(10) avoids
multiplying their penalty by an additional ell^2. The true physical cell has
a low-rank band and Schur operator at the controlled scale(16)-(20).
For fixed eta,gamma,R0 and n^2/ell->0, the displayed band condition holds.
This is a nontrivial boundary statement on the original carrier; it neither
assumes a global dimer isometry nor deletes occupied neighbors from D.

At density rho, the cost in(3) per volume is at most12 gamma rho/ell^3.
The tentative scale ell approximately rho^-1/3 h, h->infinity slowly, makes
that price O(gamma rho^2/h^3) while typical pair count is O(h^3). This removes
the earlier incompatible scale requirement from the crude N/ell^2 IMS
estimate. It does not prove a lower EOS. In particular, the following steps
remain genuinely open:

* Compare the actual S_n,ell of(19), with its real boundary and retained
  penalty, to sum_(i<j) T0^(ij)/ell^3 with an error usable for growing n.
  The periodic collision correctors do not establish this: truncating a
  corrector near a face changes both high components and its residual.
* Remove the eta-gradient deformation at the correct leading coefficient
  and price gamma if it is sent to zero. Its dependence is explicit in(15).
* Control arbitrary physical particle-number tails when summing cell lower
  forms, rather than assuming every cell has its typical number. The local
  gap alone is not such a tail bound or a leading interaction estimate.

No full-T0 boundary Schur estimate, canonical EOS, condensate, phase result,
formal audit, or numerical constant for the pinned local matrix is claimed.
The finite family kernel argument proves existence of C_pin at fixed R; it
does not conceal an unperformed matrix computation. The complete new proof
requires independent focused checking before downstream use.
