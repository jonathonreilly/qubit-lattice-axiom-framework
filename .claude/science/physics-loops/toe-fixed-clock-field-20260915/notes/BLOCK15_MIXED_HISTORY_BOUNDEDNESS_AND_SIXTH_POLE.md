# Separating the mixed histories from the sixth-order infrared singularity

Personal derivation, 2026-09-15. PROVISIONAL. Structural and normalization
checks passed; personal scope review is in the companion. No independent audit.

## 1. Target and dependencies

This note concerns the supplied zero-electric-penalty native pi-flux model,
its canonical pure Gaussian active reference and the actual electric
perturbation

 H(u)=H0+u V,  V=(1/2) sum_(v,e<f incident v) Z_e Z_f.

The first-order scalar has been subtracted. Active H0 is normal ordered
relative to its vacuum Omega. Its Majorana matrix is K, with hopping scale
h>0, and its eight-site-cell positive frequency is

 omega(k)=2h sqrt(sum_a sin^2(k_a/2)).

The finite approximants are the canonical antiperiodic cubic L=4M tori,
M>=32. The theorem is about a Taylor COEFFICIENT at u=0, followed by its
thermodynamic limit. It does not interchange that limit with fixed u.

The following current-main conditional sources are used at revision
083a58b4e7faca5839a7b31fab553f6fa1f2c254:

- The native dictionary supplies the common active/spectator frame, the
  electric pair insertions and cut closure product(-i gamma_v beta_v).
- NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS supplies a volume-independent
  kappa>0, relative to this SAME original vacuum energy, for every wrong
  local-flux sector. Its density certificate is inherited, not rerun here.
- The uniform and thermodynamic star sources supply rapidly quasi-local
  odd vacuum creators Y_v, their smooth coefficient matrix C(k), and the
  exact star vectors chi_v=Y_v Omega=O_v Omega.
- The positive Ward and spectral sources supply C(0)=alpha I in the smooth
  cell gauge and 7<h^2 alpha<330. The sign is already proved there; it is
  not a new sign certificate in this campaign.
- NATIVE_FULL_STAR_INFRARED_RESPONSE supplies the complete higher-odd
  singleton kernel's uniformly summable rows and their thermodynamic limit.

All these remain provisional/conditional dependencies here. Their supplied
Hamiltonian and reference are not selected from the framework axioms.

The new target is the complete mixed-history contribution to the sixth
spectator bilinear. We prove boundedness of its Bloch multiplier, rather
than evaluate each of its many signed coefficients. The conclusion is
that those terms cannot cancel the singleton channel's 1/omega singularity.
No sign of an individual mixed coefficient is assumed.

## 2. Which sixth histories can matter at separated centers

Each insertion toggles two distinct incident edges. A returning word has
total toggle delta S, and its gauge closure supplies one active and one
spectator Majorana at every vertex of S. A finite cut with at most twelve
edges encloses at most two vertices on the infinite cubic lattice: writing
P_a for the three coordinate projections, edge boundary counting gives
|delta S|>=2 sum_a |P_a S|>=6 |S|^(2/3), using the finite-set
Loomis-Whitney inequality. Thus |S|<=2 when |delta S|<=12. The same local
classification holds on the sufficiently large tori; a winding cut cannot
be made from twelve edges. The finite cut argument in the weak-electric
parent also proves this directly for cubic extents at least four.

Odd |S| is killed by active-vacuum parity. Empty S is spectator-scalar.
At orders at most five, a nonscalar even cut would have to be two adjacent
vertices, with ten boundary edges used once. Those edges form two
vertex-disjoint five-edge stars and cannot be partitioned into five pairs
of incident edges. Therefore every vacuum-returning coefficient through
five is scalar. The statement also holds with higher powers of resolvents:
the toggle support and parity argument is unchanged.

Consequently the nonscalar canonical sixth coefficient is the raw reduced
chain P V R V R V R V R V R V P. Folded terms factor through shorter
vacuum returns and are scalar or zero. This is the same canonical
normalization argument as the finite weak-electric source, now using the
size-independent local support fact. Scalar energy densities are outside
the present target.

For centers v,w at graph distance at least four, delta{v,w} is the disjoint
union of their six-edge stars. All twelve edges occur exactly once. Every
insertion is centered at v or w: the two edge sets have no common endpoint,
and two edges of one star can meet only at its center. There are fifteen
pair partitions at each center, and720 orders for each fixed pair of
partitions. Exactly72 orders have one star complete at the third step;
the other648 have mixed third prefixes. Thus the full separated-center
census is

 225*720=162000 histories,
 225*72=16200 singleton-middle histories,
 225*648=145800 mixed-middle histories.

Equivalently choose an ordered partition at each center (90 each) and one
of the twenty interleavings of two ordered triples. Two interleavings are
singleton-middle and eighteen mixed. This is a classification of all
histories, not a sampling rule.

Every proper prefix of a mixed history has at least one partially flipped
star. A partial star has two or four flipped edges; complementation by its
full star is a vertex gauge, and leaves six or eight defective plaquettes.
For the separated centers the two plaquette supports do not overlap.
Therefore every mixed prefix has at least six defective plaquettes and

 D_F=H0+B_F >=delta I,  delta=6 kappa>0,                (1)

on the FULL active Fock space in both parities. A completed star at one
center is harmless to this bound while the other is partial. In contrast,
the singleton middle has no flux defect and retains a gapless odd active
resolvent. It must not be assigned the wrong-flux gap.

At bounded separation only finitely many additional local support patterns
are possible. A doubled extra edge in an adjacent two-vertex cut has to
meet its odd boundary stars; a disconnected extra pair would leave too
few occurrences to realize the cut. Their mixed prefixes have a nonzero
local flux and hence a positive uniform bound at least kappa. Their
individual coefficients and thermodynamic limits are bounded by the same
filtered-inverse construction below. A finite-distance change of a kernel
adds a bounded trigonometric polynomial to its multiplier.

## 3. A filtered five-inverse word admits two separated odd factors

Choose the same smooth inverse filter at every volume: f(x)=-1/x for
x>=delta, with a smooth cutoff near zero. Its Fourier kernel w obeys

 f(x)=int w(t) exp(-itx) dt,
 int (1+|t|)^p |w(t)| dt < infinity for every fixed p.   (2)

For example the odd cutoff construction in the quasi-local star source
has these properties. A possible integrable singularity of w at t=0 is
allowed. No exponential time moment is assumed. With the smaller gap
kappa one can use one common filter for both close and separated terms.
Functional calculus makes f(D_F) the EXACT negative inverse on every
mixed prefix. There is no truncation of its high active spectrum.

Write B_F=B_(v,F)+B_(w,F), each a bounded even quadratic perturbation
supported on its star. Define

 U_B(t)=exp[-it(H0+B)] exp(itH0),
 tau_t(A)=exp(-itH0) A exp(itH0).

The five inverse factors acting on Omega are an integral of five cocycles
at successively shifted times. Explicitly, for prefix denominators D1,...,D5,

 exp(-it5 D5)...exp(-it1 D1) Omega
 = U5(t5) tau_(t5)(U4(t4)) ...
   tau_(t5+...+t2)(U1(t1)) Omega.                       (3)

The total final free evolution kills Omega. Gauge closure then inserts
gamma_v gamma_w, with the actual native scalar phase and the electric
factor2^-6 retained. These phases have modulus one and depend on the
fixed history/order and cell types; they do not grow with separation.

Let S=sum_j |tj| and R=d(v,w). Finite-range CAR propagation and Duhamel
comparison give

 ||U_(Bv+Bw)(t)-U_Bv(t)U_Bw(t)||
   <=min(2, C(1+|t|)^q exp(c|t|-mu R)).                (4)

One direct proof uses the interaction-picture generators tau_s(Bv) and
tau_r(Bw). Their commutator is exponentially small before their light
cones meet. Variation of the unitary propagators integrates that
commutator twice; it costs time powers, not an exponential in volume.
No spectral gap for Bv or Bw separately is used in this step.

Use(4) at each of the five slots, and commute even factors centered at v
past factors centered at w. The same propagation estimate controls each
commutation. The finite number of factors is fixed. The result is

 mixed_history(v,w)
  =eta/64 int [product_j w(tj)]
       omega(A_v(t) B_w(t)) d^5t + e(v,w),             (5)

where A_v and B_w are ODD, norm-one products of the center Majorana and
unitary local cocycles/evolutions belonging to that center. For each fixed
history and t they are covariant translates with finitely many cell
types. Their definitions depend on the local progress of that history,
not on the location of the other center. No factorization of the vacuum
state has been made: the two-point expectation in(5) is retained.

Before time integration the error is bounded by
min(C,C(1+S)^q exp(cS-mu R)). Split at S=mu R/(2c), and use arbitrary
moments in(2) on the second part. For each p,

 |e(v,w)|<=C_p (1+R)^(-p).                              (6)

This is uniform in volume and summable over the three-dimensional lattice
when p>3. It gives a bounded convolution error. Keeping the minimum with
the unitary norm bound is essential: polynomial filter moments cannot
integrate an uncut exponential in S.

The locality estimates used here are standard fermionic propagation
machinery. [Nachtergaele, Sims and Young](https://arxiv.org/pdf/1705.08553),
Theorem3.1, states both the commutator and anticommutator versions for even
interactions. The present nearest-neighbor bounded quadratic interaction
satisfies its hypotheses. No ground-state spectral-gap stability theorem
from that paper is imported into this gapless reference.

## 4. Graded locality bounds the remaining two-point multiplier

For fixed times the odd families in(5) have effective localization radius
O(1+S). Truncating their unitary generators on balls preserves parity and
gives the same exponential propagation error. In particular

 J_A(t)=sup_v sum_w ||{A_v(t)^*,A_w(t)}||
       <=C (1+S)^q,
 J_B(t)<=C (1+S)^q,                                    (7)

for some fixed q. To see the polynomial rather than exponential bound,
use the trivial norm bound inside a ball of radius c1 S+c2 log(2+S)+c3.
Its volume is polynomial in S. Outside that ball the exponential spatial
tail is summable. Disjoint odd ball approximants anticommute exactly.

For any finite coefficient sequence a, the CAR/C*-algebra inequality is

 ||sum_v a_v A_v||^2
  <=||{sum_v a_v A_v, (sum_v a_v A_v)^*}||
  <=J_A sum_v |a_v|^2.                                 (8)

The second step is the row/column Schur bound for the nonnegative matrix
of anticommutator norms. Both row and column sums have the same bound by
adjunction. This inequality applies to non-Hermitian odd A_v. It requires
neither Gaussianity nor exponential clustering of the state.

Apply(8) also to the adjoint A family and the B family. The cross-correlation
kernel omega(A_v B_w) defines a bounded bilinear form on site l2, with
norm at most sqrt(J_A J_B). Translation covariance in a fixed magnetic
cell therefore gives a bounded matrix-valued Bloch multiplier. Integrating
this operator bound with |product w(tj)| is finite by(2),(7). Add the
summable error(6), then the finitely many histories and close separations:

 ||K6_mixed||_(l2->l2) <=C_mix h^-5 < infinity.          (9)

K6 denotes the real antisymmetric spectator matrix in the convention
H6=(i/4) beta^T K6 beta. Passing to its antisymmetric real part changes
only a fixed norm factor. C_mix is an existence constant depending on
the fixed ratio kappa/h and the filter/locality bounds. No useful numerical
value is claimed. In Bloch space(9) is an essential supremum bound.

The same estimates hold on the finite tori. Fixed-entry limits follow
from local cocycle convergence and the integrable filter product, exactly
as in the star thermodynamic source. A uniformly bounded convolution
operator is thereby obtained in infinite volume. Entrywise bounds alone
would not have proved(9); the odd-family bound(8) is the decisive step.

## 5. The singleton normalization and its surviving singularity

The complete singleton-middle family is precisely second-order elimination
of the actual third-order vertices -i O_v beta_v through odd active states.
Put

 T_vw=<chi_v,H0^-1 chi_w>.

Keeping spectator CAR signs gives

 H6_singleton=-sum_vw T_vw beta_v beta_w,
 (K6_singleton)_vw=-4 Im T_vw.                         (10)

The diagonal is spectator-scalar and is omitted from K6. Equivalently the
coefficient of i beta_v beta_w for v<w is -2 Im T_vw. There is no extra
factor of two from summing the two ordered centers after this conversion.

For a literal linear source chi_v=alpha gamma_v Omega, Gaussian covariance
I+iK/omega and one-particle energy omega give

 T=alpha^2[omega^-1+iK omega^-2],
 K6_singleton=-4 alpha^2 K omega^-2.                    (11)

For the actual source the one-particle coefficient matrix is C(k), smooth
with C(0)=alpha I. Thus C(k)-alpha I=O(|k|). Its one-particle inverse kernel
differs from that of the literal linear source by O(|k|/omega(k)), bounded
near the conical node. This conclusion is unchanged by choosing a smooth
cell gauge equal to the identity at zero; it assigns no value to an
individual band eigenvector there. Away from the node all inverse
frequencies are bounded.

The actual higher-odd singleton return is bounded as a convolution
operator by the parent's summable-row theorem. It is retained, not set to
zero. Combining that fact with(9) yields for the COMPLETE nonscalar sixth
coefficient, almost everywhere away from the node,

 i K6(k)=-4 alpha^2 iK(k)/omega(k)^2+B(k),
 ess_sup_k ||B(k)|| <=C h^-5.                           (12)

Here all mixed histories and all higher odd singleton sectors are present.
Finite-distance coefficients are included in B. This is a multiplier
statement. A bounded remainder is not automatically a pointwise
real-space decay asymptotic.

The active Hermitian matrix iK(k) has four eigenvalues +omega and four
-omega. Weyl's eigenvalue inequality applied to(12) gives four positive
and four negative sixth-order eigenvalues with respective leading
magnitudes4 alpha^2/omega and bounded additive errors. Since alpha>0,
no bounded mixed remainder can cancel this singularity.

## 6. Finite-volume consequence and the actual remaining problem

The parent coefficient matrices C_L converge with every fixed derivative
to C, while the mixed bounds and higher-odd summable bounds are uniform.
The smallest AP frequency is2 sqrt3 h sin(pi/L). Uniform convergence near
zero, a small fixed nodal neighborhood, and the bounded complement give

 lim_(L->infinity) ||i K6_L||/L
       =2 alpha^2/(pi sqrt3 h).                        (13)

For the upper bound, use C_L=alpha I+o(1)+O(|k|) near the node and the
minimum frequency; outside a fixed nodal neighborhood the norm divided
by L vanishes. Then shrink that neighborhood. For the lower bound evaluate
the multiplier at a minimum-frequency AP momentum and use the same
uniform coefficient convergence. The uniform bounded remainders vanish
after division by L. No convergence rate for C_L is required.

The O(|k|) coefficient remainder is uniform in L by the parent's derivative
bounds. The separate calibration C_L(0)-alpha I=o(1) contributes o(L),
not necessarily O(1), before division by L. Only the mixed and higher-odd
remainders have been asserted uniformly bounded without that calibration.

This is a statement about the canonical coefficient's one-particle
spectator matrix. It is not a many-body excitation gap and not a prediction
that the exact Hamiltonian has an energy diverging at small momentum.
Its site rows remain square summable, consistently with the previous
singleton response bounds. A uniform row norm is compatible with an
unbounded Bloch multiplier in three dimensions. Both 1/|k| and its square
are locally integrable there. In particular the singularity does not imply
a divergent local susceptibility or a divergent sixth-order ground-energy
density. Nor does it exclude analyticity in every other possible norm.

The physical lesson is limited and useful: a vacuum-only fixed-order
elimination of the gapless active sector is not uniform in momentum or
volume. The complete mixed sixth histories do not repair that specific
singularity. Keeping active and spectator fields together, retaining
energy dependence, or an infrared resummation remains available. The
previously known quadratic two-channel diagnostic illustrates such a
reorganization but is not promoted to the full nonlinear native model.

No axiom update is forced. No fixed-coupling phase, selected vacuum,
Hamiltonian-selection theorem or all-order expansion has been proved.

## 7. Verification and limits

The companion exhausts the complete162000 separated-star histories in each
of four actual cubic relative geometries, retaining all five prefixes.
The minimum mixed-prefix count is six defective plaquettes in every case.
This checks the geometric classification; the uniform stiffness itself is
an inherited analytical/certified dependency, not an enumerated spectrum.

Literal CAR matrices test the exact five-cocycle product and its separated
cluster factorization, with errors below1.2e-15. The coupled fixture has a
nonzero6.5e-8 factorization error, so exact separation has not been assumed
in the interacting propagation step. Its coarse Duhamel bounds are loose.
A non-Hermitian odd cross-family kernel has norm2.1624 against its derived
bound2.2992. Direct elimination in one common active/spectator CAR frame
checks the singleton skew-matrix factor-4 to4.5e-16 and rejects the wrong
sign and a missing ordered-center factor. The finite Bloch matrices contain
a supplied bounded remainder; they are explicitly diagnostic, not computed
native mixed coefficients or evidence for a phase. No initial checker
failure occurred. All these checks are by the same author.
