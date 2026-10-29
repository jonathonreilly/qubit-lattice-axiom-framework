# Independent review of the uniform one-loop coupling

**Scoped verdict: LAND after the one narrow correction below.** The final target is
[UNIFORM_ONE_LOOP_COUPLING_ASTRA.md](UNIFORM_ONE_LOOP_COUPLING_ASTRA.md),
SHA256 `b7baa6a711969c8fc96538009bb8f9f9acdde3f14f6d2f570a6ca5b9391516ce`.
This is a source review of its volume-first Gaussian coefficient and
all-increments bracket, conditional on its named mathematical inputs.
It is not whole-PR approval, an audit assignment, a finite-u estimate,
or a proof of continuum existence or a physical Hamiltonian mass gap.
Both physical targets remain open.

## 1. Independence and exact scope

The coordinator requested Astra/max. Runtime backend identity is not
independently observable. This is Codex reviewing Codex, with a different
author of the target. I authored separate conditional-covariance,
curved-background and selected-source-sector units; none supplies the
missing one-loop conclusion here. I did not author this target or its
CJ/BC predecessors. No mutable target draft was read. The numerical plan
was written before receipt of the final target, but the corrected UIR
review had already exposed its expected continuum coefficients. Additional
source-exposed controls were declared after the full target read and before
implementation. No blind or cross-family independence is claimed.

All 688 original target lines were read, and the sole changed region in
the 723-line corrected source was read in full. The original source hash
is `977d901f2c886a533c9eb1b487414e1a081df681463003eb231a3ef2b1b26670`,
preserved at c5841c8145 and 88130072aa. Before the correction, the author
receipt and manifest matched all six artifact and 25 input bindings.
The separate [correction receipt](checks/uniform_one_loop_fixed_complement_correction.json)
binds the new source; its exact affected review is recorded in the
[correction verification](checks/review_uniform_one_loop_correction_verification.json).
A hash check is not a whole-file read: the separate [read manifest](checks/review_uniform_one_loop_read_manifest.json) distinguishes complete reads, selected
proof ranges and reused earlier reads. The corrected CODEX_REVIEW_UIR
controls the old UIR55 bubble formula; its printed quarter-bubble is not
accepted. PROCESS_LIGHT governs this review. The coordinator retains
Git, publication, the resource lock, shared status and audit authority.

The theorem is about d=4, fixed N>=2, fixed odd L>=3, one fixed kappa>0,
the paired S4-prime mean with divisor 24 L^4, and the normalized tree phase
UL1. Integrated links, counting pairings and FLOW's normalized Lie algebra
are retained. Every coefficient is first defined by the thermodynamic
limit at fixed depth and nonzero external momentum, then by the
infrared limit. The subsequent depth-uniform bound does not exchange
these limits or estimate their finite-volume rate uniformly in depth.

## 2. The actual common jet class

UL5's norm includes absolute colour and orientation sums and an
exponential of top-lattice diameter. The top residual envelope
H_n v=kappa r_(n-1) supplies its quadratic row bound. CJ12 supplies its
full-colour cubic bound. BC26 supplies its full quartic bound through the
completed stationary expression, including cubic exchange. The bottom
vertex has count ell^4 and four inverse powers of ell; soft square and
mixed contributions leave summable L^-2s and L^-s respectively. The
anchored-column counts in BC23 are necessary to turn these statements
into the stated tensor norm. Taking one smaller positive rate and one
larger constant gives one common pair (m,C_J), including n=0.

The BC input is a source-specific second-curvature theorem, not a uniform
hidden inverse. Its complex division, both low-zero sheets, harmonic
value and reciprocal gluing were checked against its proof and scoped
review. The earlier CJ18-open header is historical: BC supplies precisely
that interface. No all-Cartan replacement for the full-colour quartic is
made. Nor is a depth-uniform nonlinear field neighborhood inferred from
uniform jets through order four.

There is a useful independent coercivity reconstruction. Put
r_i=a_(i+1)-Q_i a_i. Curl telescoping and the actual root/straight identity
give

    ||d v|| <= ||d a_0|| + 4 sum_(m=0)^(n-1) L^-m ||r_(n-1-m)||.

Indeed the composite straight map has counting row sum L^m and column
sum L^-3m, hence l2 norm at most L^-m. Its curl agrees with that of the
root map. The fine-to-top curvature average contracts the d4 l2 norm,
and the unit-lattice exterior derivative has norm at most four.
Weighted Cauchy-Schwarz therefore gives

    H_n >= c_alt d*d,
    c_alt = [1+16/(kappa(1-L^-2))]^-1 > 0.

This is an analytic cross-check of UL7, not a replacement fitted to its
samples. UL7 itself correctly converts an energy bound into twice that
bound for the Hessian. On the full gauge-completed free space the
longitudinal eigenvalue is exactly lambda. Thus the only free zero is
the acoustic fibre p=0; no doubler is hidden in the class.

UL8 has the required counting factor L^-4 and constant-link response
Q_0(0)=L I. Its low-alias contribution to lambda(p)G_(k+1)(p) is
L^-4 L^2 L^2 P_perp=P_perp. The fixed-k nonzero aliases and the finite
kappa^-1 term vanish in this limit. This proves beta[T_k]=1, without
assuming convergence of T_k. The extra leg-direction Dirichlet factor
is retained in the straight symbol.

The symmetry and torus statements also match the actual model. Reflecting
a negative coarse direction reverses the whole path and exchanges its
endpoints; after translating the root, its centered offset and coordinate
order give another paired S4-prime path. Axis permutations relabel the
same 24 orders. Gauge covariance and charge conjugation survive the
SU(N) maximum and the unique local stationary orbit. At fixed depth a
local rooted slice gives a finite Bloch matrix with positive hidden
Hessian on its complement. Its analytic inverse and the finite tree
contractions for the jets periodize exactly. The internal image labels
are eliminated along that tree. The US/CJ/BC bounds are for these same
kernels, not for independently selected finite-volume actions.

## 3. Normalizer, colour and determinant domains

The HS-to-FLOW dictionary is T_FLOW(b)=T_HS(sqrt(N)b)/N. Thus q=2,3,4
jets acquire factors 1,sqrt(N),N. The fixed kappa in UL1 is not replaced
by kappa times a running-coupling ratio. The constrained SU(N) maximizer
and polar bookkeeping agree at the required orders: the determinant
phase starts at degree three, its maximizing-trace defect at degree six.
Their relevant tree jets and Gaussian background two-jets agree; no
identity at a general background follows.

For a positive covariance C decompose coarse links into transverse
vectors and the range of D, using the orthonormal longitudinal frame
D(Delta')^-1/2. A block determinant and its inverse Schur block give

    det C = det_perp C_perp * det' Delta / det'(D* C^-1 D).

This reconstructs UL11 with its signs. The normalized kernel's Laplace
prefactor contributes +1/2 log det C to the effective action, while the
hidden Gaussian integration contributes +1/2 log det Hess_h Psi. The
coarse gauge block cancels as stated. The remaining transverse group
has half a ghost; the extra fine/coarse ghost difference is another half.
Counting either twice changes the coefficient.

Scalar constants and vector harmonics are not deleted indiscriminately.
The root scalar shear contributes ell^4 to the pseudodeterminant; its
completed projection is P_int+J P_c0 J*. Neutral harmonic graphs have
Grams 1+ell^-2 and 1+ell^2, each with multiplicity h=4(N-1). Their ratio
leaves -h log ell before differentiation. It has zero background
coefficient, but is present in the determinant identity. The residual
weights remain +1/2,-1,+1/2,-1/2 for L_per,Delta_c,G_c,H_h.
At the free full-colour point the vector harmonic dimension is
4(N^2-1), and the scalar constant dimension is N^2-1. At a charged
background a fixed-free-complement Taylor regulator is not a nonlinear
pseudodeterminant with a changing stabilizer.

Right-translated Haar density at zero quantum field is background
independent. Its quadratic quantum correction is of higher order in 1/u;
the field-dependent leading soft normalizer is already included above.
This statement does not identify the tree Hessian with the exact finite-u
normalized-density Hessian or bound its remainder.

## 4. Reflection, off-shell charts and the fixed-complement correction

Differentiating the actual infinitesimal gauge variation gives UL13,
including its factors 3/2 and 1/2. In link-centered coordinates inversion
makes the two- and four-jets even and the three-jet odd in all momenta.
B4 covariance and the Ward identity fix the quadratic degree-two tensor
to |k|^2 I-k k*. Equal beta therefore makes delta H fourth order.
For a possible cubic degree-one difference A p+B q, contraction with p
first forces B=0; contraction with q then forces A=0. The lower-jet Ward
terms cannot supply a degree-two term. Odd parity leaves degree three.
For the quartic, the constant difference contracts to zero against an
arbitrary external momentum, hence vanishes; even parity leaves degree
two. These are full-colour polynomial statements.

The target's symmetric split is a legitimate way to preserve this parity:

    e^(B/2) e^X e^(B/2) = e^B e^Y,
    Y=Ad_(e^-B/2) X.

At fixed B this is exactly linear in the quantum coordinate. Its adjoint
matrix M is orthogonal with determinant one. Therefore
H_s=M* H_r M and D_s=M* D_r, including off shell. No force term arises
from this particular change. One must still differentiate the nonlinear
map from action-log coordinates to this split. Its symmetric BCH series
is B+X-[B,[B,X]]/24+[X,[X,B]]/12+..., so the off-shell term
T'(B) times its second quantum derivative is retained. It has at least
two additional momentum powers. Dropping that term is not justified by
stationarity of an arbitrary external background. The same observation
shows why the change cannot spoil the differences in UL15.

There is a finite-regulator qualification to determinant invariance which
is made explicit here. A fixed free complement must either be transported
with M or its correction retained. Let P be the free kernel projection,
Q=1-P, O0=0 direct-sum D with D>0, O=O0+e O1+e^2 O2, M=exp(e A),
A*=-A, U=P A Q and F=P O1 Q. Direct block expansion, including the
within-Q conjugation, gives

    [e^2]{log det_Q(M* O M)-log det_Q O}
        =2 Re tr(D^-1 F* U)-tr(U*U).                 (R-CHART)

This is generally nonzero. The second term is the induced Gram
correction; the first cannot be omitted at a nonstationary background.
Transporting Q's subspace gives exact isometric invariance instead.
Thus det M=1 alone does not prove equality of the two fixed-complement
finite-volume coefficients.

For the actual change M in UL15, U and F connect the free zero modes
only to +/-P. Their ranks are bounded independently of volume. At fixed
P!=0, the inverse there is bounded by C/lambda(P); the local vertices
are bounded by the common jet constants. Dividing R-CHART by T^4 gives
O(T^-4 C(P)), also for admissible P_T tending to P. It vanishes before
P is sent to zero, exactly in the exceptional-fibre convention used by
FC14–FC16. The ghost scalar Gram D_s*D_s is unchanged. Thus the target's
volume-first determinant and symmetric-split comparison are valid.

**F1, resolved:** the original paragraph inferred unchanged determinants
from det M=1 without qualifying the prescribed fixed complement. I
requested a narrow source correction rather than silently supplying that
qualification only in this review. The author independently verified the
block expansion and inserted UL13a, exact transported-space invariance,
the retained off-shell force term and the fixed-P volume-density estimate.
The affected review verifies the signs, coefficient-versus-derivative
factor, outside half-vector weight and unchanged theorem. No finite-volume
uniformity is recovered, and no remaining source correction is requested.

## 5. Rebuilt infrared and finite-part estimate

For O=O0+e O1+e^2 O2 the coefficient is
tr(G O2)-1/2 tr(G O1 G O1). Phase averaging leaves two ordered transfers.
The outside half-vector weight is separate. The old quarter-bubble
changes the relative seagull/bubble normalization and is rejected.

The common class and Ward/reflection orders give G=O(|k|^-2),
delta G=O(delta), V=O(r), delta V=O(delta r^3), S=O(1), and
delta S=O(delta r^2), with differentiated versions through order two.
Every telescoped integrand difference is consequently bounded by UL17.
Near k=0,+P e2,-P e2 each pole has exponent at most two. In the inner
ball k=Pz this gives an integral O(delta P^4), including both moving
centres. On |k|>=2|P| the second P derivative is bounded by
C delta |k|^-2. At P=0 the flat Cartan background shifts the loop
momentum. Its coefficient is a periodic second derivative of log det O0;
the small-sphere flux is O(r^2), so its integral is zero. Reflection
removes the linear integral. The removed inner Taylor terms cost
O(delta P^4). Dominated convergence on the outer region proves UL20,
and division by lambda(P)/4 proves the uniform finite-part Lipschitz
bound. No P-independent majorant across an untracked moving pole is used.

For Wilson subtract a radial cutoff times its leading continuum
integrand. The remainder has the same improved estimates and a finite
Taylor-subtracted P^-2 limit. After k=Pz the continuum term has
J_c(z)=|z|^-4 h(z/|z|)+O(|z|^-5). Its separate singularities at
0,+e2,-e2 and the subtracted derivative at zero are integrable in d4.
Removing the displayed homogeneous tail leaves an absolutely integrable
function. The tail integrates to its spherical coefficient times
log(1/P), plus a finite cutoff constant. This proves existence of the
reference finite part, rather than merely identifying its logarithm.

For one root charge the transfer matrices are -q k1 I +/- qP J12.
The two-transfer trace yields h_S=n1^2-4 n1^2 n2^2 and
h_V=4 h_S-2, since tr J12^2=-2. Rotation and the unit-sphere identity give
<n1^2>=1/4 and <n1^2 n2^2>=1/24. With radial measure 1/(8 pi^2),
C_S=q^2/(96 pi^2) and C_V=-20 C_S. The two real colours of each
positive-root pair cancel the outside half. Since sum_(i<j)q_ij^2=N^2
for the FLOW unit Cartan direction and the Wilson wave density tends to
P^2/4, the transverse coefficient is -7N^2/(8 pi^2). The extra half-ghost
is -N^2/(24 pi^2); their sum is -11N^2/(12 pi^2).

The neutral finite term remains. The exact-two-form projector has rank
3(V_f-1) and six V_f diagonal plaquette entries; each diagonal is
(1-1/V_f)/2. The neutral Wilson cosine Hessian and Cartan completeness
then give -(N-1)(1-1/V_f)/4, tending to -(N-1)/4. Its absence of a
charge logarithm does not remove it from a_0. All analogous neutral
T_n tadpoles remain inside the same finite-part bound.

## 6. Residual, scale transfer and every increment

FC16 is consumed only at each fixed depth. Its neutral part keeps the
full quartic tadpole, root mean and harmonic factors. The neutral mixed
vertex has a Ward zero O_n(P), while the residual is O_n(P^2). Charged
mixed poles have orders (1,2),(2,1),(2,0); the repeated-residual (2,2)
term carries P^4. After Wilson normalization these tend to zero. The
periodic projector defects have density bounded by
C_n T^-4(1+P^-2)^m_n. Dyadic counting of the remaining pole orders below
four identifies their a.e. Bloch integral. This proves the fixed-n zero;
it does not bound the depth dependence of C_n or interchange limits.

The fine stationary map has smooth amplitude ell^-1 at P/ell and
nonzero transverse aliases O_n(P^3), with the full Dirichlet symbol.
Fine translation invariance pairs opposite aliases. Their nonzero
contribution is O_n(P^6); the smooth density has factors
ell^4 ell^-2 ell^-2=1. Thus the fine finite part is a_0 and the
logarithm acquires n log L. The extra ghost uses the same scalar
Laplacian in fine and coarse units, so its reference finite part cancels.
The normalized prefactors and the fixed-root Gaussian Schur determinants
factor consistently with the sequential definition of B_n. Therefore

    B_n=beta0 n log L+a_n-a_0,
    beta0=11N^2/(12 pi^2)=2N(2 b0),  b0=11N/(48 pi^2).

The common class gives |a_n-a_0|<=C_FP. Subtracting the last identity
at any two fixed integers j<=n gives an error at most 2 C_FP, with
no new limit interchange. Hence HINT2_55 R2.3 B-BR receives
beta'=beta''=beta0 and R'=2 C_FP for every 0<=j<=n. At j=0 the bound
is C_FP, and at j=n it is zero. Bounded finite parts do not imply
convergence of a_n or b_n; an alternating bounded sequence is a direct
counterexample to that inference. The source makes no such claim.

## 7. Evidence and resource record

The [prospective plan](checks/review_uniform_one_loop_numeric_plan.json)
and [source-exposed supplement](checks/review_uniform_one_loop_after_target_plan.json)
precede the independent implementation. The first attempt stopped before
importing mathematical libraries: free memory was 49%, below the unchanged
50% gate. Its [empty stdout](checks/review_uniform_one_loop_01.stdout.json)
and [exact stderr](checks/review_uniform_one_loop_01.stderr.txt) are preserved.
No mathematical predicate ran. After the resource state recovered, the
**unchanged** program completed [38/38 predicates](checks/review_uniform_one_loop_02.stdout.json),
comprising 24 ordinary checks and 14 mutation/control detections, with no
mathematical failure and empty stderr.

The separate implementations include:

- Exact noncommuting determinant polynomials versus the full two-transfer
  trace expansion; the quarter-bubble and missing-transfer changes fail.
- Sphere moments derived algebraically, charged vector/spin coefficients,
  the SU(N) root identity and HS/FLOW density conversion. Wrong spin,
  colour multiplicity and ghost weights are detected.
- An actual noncommuting SU(2) plaquette with four independent background
  links and all twelve quantum directions. Its force is 0.3139888, so it
  is off shell. Right/symmetric gradients, Hessians, gauge completion and
  scalar Gram agree below 3.2e-61. Leaving D untransformed produces a
  0.2035806 discrepancy. A nonlinear additive-chart control separately
  requires its force term and nontrivial Haar Jacobian.
- The exact fixed-complement correction -354/2695, with mixed term
  -24/2695 and Gram term 6/49. Removing either term or using only the
  full determinant-one assertion fails. Its fixed-rank density scales
  as T^-4. This control predates the author's narrow correction.
- All 7,776 L=3 paired S4-prime paths satisfy generating reflection and
  permutation identities and Q(0)=3I. The complex root-gradient identity
  has error 2.37e-14; dropping the second axial leg gives defect 0.0329382.
  A bounded oscillatory sequence also rejects an inference from the
  all-increments bracket to convergence of adjacent increments.

These are finite checks, not 38 independent proofs or an arbitrary-depth
numerical certification. Exact arithmetic is used for the rational and
symbolic tests; the plaquette uses 60-digit arithmetic and the final
complex path check ordinary complex floating point. None uses author
helper code or fits a universal constant from a sample maximum.

Only after that completed independent run was the full author checker
read and reproduced from an identical temporary copy, so its own output
write could not alter a frozen author artifact. The [replay](checks/review_uniform_one_loop_author_replay.json)
returns 24/24 and matches every structured result field exactly. Its
ordinary finite-block computations and wrong-formula controls are
reproducibility evidence, not new uniform mathematics. The independent
script used 68.9 MB peak RSS and 0.667 seconds; the author child used
109.6 MB and 2.295 seconds. Successful runs had at least 53% free memory
and all load averages below 2.88. Both used nice 10, five thread caps at
one and the read-only coordinator lock. No threshold was relaxed, failed
output erased, author file rewritten, or shared/Git/audit file changed.
The [attempt record](checks/review_uniform_one_loop_attempts.json) and
[freeze receipt](checks/review_uniform_one_loop_receipt.json) bind the
complete evidence and the preserved resource halt.

## 8. Literature and disposition boundary

Kim–Adams–Lee, [0710.1930v1, Sections 1–5](https://arxiv.org/pdf/0710.1930v1),
was checked at the setup, scale derivative, rate-dependent finite-part
step and massless/no-doublers qualifications. Its rate proof invokes an
extended power-counting theorem. That result is not imported into this
review: the three-centre subtraction and integrable tail above establish
the needed bounded-class statement directly.

Lüscher–Weisz, [hep-lat/9504006v1, Sections 2.1 and 5.1–5.2](https://arxiv.org/pdf/hep-lat/9504006v1),
was checked for the background split, gauge and ghost conventions and
Haar measure vertices. It allows off-shell backgrounds, but supplies no
reason to omit a quantum-coordinate force or restricted-space Gram.
No all-order theorem from that paper is used. The downloaded versioned
PDFs and their hashes are recorded under /tmp, outside the repository.
Balaban and Dimock are credited for the constructive block-field and
localization methods underlying the internal source lemmas; no d3
hard-constraint theorem is transferred to this d4 soft model by name.

**VERDICT: LAND** for UL4 and its exact every-increment B-BR consequence,
within the supplied normalized fixed-kappa model and the named reviewed
linear/jet/residual contracts. F1 is resolved in the final source above;
no other material finding remains. Finite-u nonlinear flow, connected
source return, large fields, continuum existence/nontriviality and a
positive physical Hamiltonian gap remain separate open obligations. This
review confers no audit or retained-grade status.
