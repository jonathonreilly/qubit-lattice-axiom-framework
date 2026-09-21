# Cubic entropy symbol classification and conditional selection review

2026-09-21. No actionable mathematical or code/prose defect was found in the
reviewed base classification or dependent reversal/divergence addendum.
The full48 symmetric-symbol space has dimension five, while the proper24
space has dimension eleven. All five displayed couplings have the supplied
positive-rate local realizations. Full raw-vector closure, raw-Gauss
preservation and derivative-curl closure are distinct additional premises;
the generalized internal A-sign reversal does not remove any of the five
couplings. These conclusions remain finite classification and local-generator
statements, not a new hydrodynamic theorem or Maxwell identification.

The complete base note was read, independently reconstructed and checked
before the author checker/results. Its pre-comparison seal is
`5c3ad0cd053ea4822b1137953e6610300b25ed5f699867d410d7d943aa12a0a9`.
The complete dependent addendum was then independently reconstructed and
separately sealed before author comparison, at
`24eeaed4f6c837cef2c6b2cd4dd2fdae3a43165530305bc4e23632fa94a80c96`.
Both initial records and their controls remain unchanged. This is an
independent reconstruction from supplied arguments, not blind-to-note work.

## 1. Representation, five maps and completeness

The alphabet is vacancy, six polar axis labels and eight axial cube labels.
A signed permutation Q acts by e->Qe and b->det(Q)Qb. The background is exactly
the full-support p*=1/15 law. On its Euclidean probability tangent V=1-perp,
the entropy Hessian is 15I, so entropy compatibility makes the real principal
matrices symmetric. The classification is at this background, not all
occupancy densities or arbitrary anisotropic products.

An orthonormal tangent basis is

    E_i=e_i/sqrt(2),        B_i=b_i/sqrt(8),
    s1=(4 1_A-3 1_B)/sqrt(168),
    s2=(14 1_vac-1_occupied)/sqrt(210),
    d_alpha=e^T D_alpha e/sqrt(2),
    t_ij=b_i b_j/sqrt(8),   w=b1 b2 b3/sqrt(8),

where D1=diag(1,-1,0)/sqrt(2), D2=diag(1,1,-2)/sqrt(6), and
Q_ij=(unit_ij+unit_ji)/sqrt(2). The order is
(E; s1,s2,B,d1,d2,t12,t13,t23,w).
The independent checker establishes exact orthonormality and zero sum.
Direct projector characters from the 48 label permutations give

    V = 2 A1g + Eg + T1u + A2g + T1g + T2g.

The six distinct character vectors have exact character Gram matrix I,
and their multiplicity-weighted sum reproduces the entire tangent character.
This independently reconstructs the decomposition without an imported
character table.

Inversion changes only E. An odd-in-polar-q symmetric symbol therefore has
only E/even blocks, and the displayed family is

    A(q)=[0 K(q); K(q)^T 0],
    K(q)=[a1 q, a2 q, m[q]_cross,
          u D1 q,u D2 q,v Q12 q,v Q13 q,v Q23 q,0].

Each of the five channels was embedded in species coordinates and verified
exactly under all 48 label permutations and all three coordinate directions.
Scalar, axial cross-product, diagonal tensor and off-diagonal tensor maps
have the required covariance. Their even input blocks are disjoint, so the
five parameters are independent. There is no w coupling in this full48
family.

Writing chi(g)=fixed species minus one, the symmetric-square character is
(chi(g)^2+chi(g^2))/2. Its exact inner product with the polar-vector character
tr(Q_g) is five over all 48 elements, and eleven over the proper24 subgroup.
Thus the five maps exhaust the required full48 space. Reflection symmetry
is an added premise: the repository's proper group does not justify replacing
the larger dimension by five. No explicit classification of all eleven
proper-only channels is supplied or inferred here.

## 2. Gram matrix, modes, isotropy and closure

The tensor completeness identities are

    sum_alpha (D_alpha q)(D_alpha q)^T=diag(q_i^2)-qq^T/3,
    sum_ij (Q_ij q)(Q_ij q)^T=|q|^2I/2+qq^T/2-diag(q_i^2).

Together with [q]_cross[q]_cross^T=|q|^2I-qq^T, they give

    KK^T=(m^2+v^2/2)|q|^2I
       +(a1^2+a2^2-m^2-u^2/3+v^2/2)qq^T
       +(u^2-v^2)diag(q_i^2).

The independent symbolic calculation is exact. Rank r of K gives 2r nonzero
signed speeds and 14-2r zeros. Generic rank three yields six nonzero and
eight zero speeds; already a nonzero scalar channel plus m!=0 spans all three
E directions at q!=0. Degeneracies are retained. Pure diagonal coupling has
rank one on an axis and rank two at q=(1,2,3), so rank two alone does not
identify isotropic transverse propagation.

A noncubic rotation taking e1 to (3/5,4/5,0) gives off-diagonal covariance
residual -12(u^2-v^2)/25. Gram rotational covariance for every q therefore
requires u^2=v^2; substitution proves sufficiency. Then

    c_T^2=m^2+u^2/2,     c_L^2=a1^2+a2^2+2u^2/3.

This is the stated Gram/isotropic-speed property, not continuous rotational
symmetry of the microscopic alphabet. Scalars and tensors remain possible
propagating fields even in this isotropic case.

For the entire six-dimensional (E,B) marginal to close for arbitrary other
moments and every q, its source columns require a1=a2=u=v=0. The remaining
characteristic polynomial is
lambda^10(lambda^2-m^2|q|^2)^2. Four propagating speeds require m!=0 and q!=0;
otherwise degeneracies increase. This is a Maxwell-shaped classical symbol,
with ten zero speeds, not physical electromagnetism.

The exact nonnegative longitudinal form is

    q^T KK^T q=(a1^2+a2^2)|q|^4
       +u^2 sum_alpha(q^T D_alpha q)^2
       +v^2 sum_ij(q^T Q_ij q)^2.

Its vanishing for all q forces a1=a2=u=0 already at q=e1, then v=0 at
q=(1,1,0). Scalar gradients can nevertheless coexist with an invariant
transverse E/B subsector and additional longitudinal sound. Subsector
existence is weaker than full raw-vector marginal closure.

## 3. Positive local realization and exact current normalization

For the orthonormal species matrix U, take S_i=(15/2)UA_iU^T. It is symmetric,
S_i1=0, and transforms as a polar pair tensor under the full label action.
On a conventional four-site context define

    h_i=S_i(l,a)+S_i(a,r)-S_i(l,b)-S_i(b,r),
    c_i=kappa+max(h_i,0), kappa>0.

Swap the entire central labels. Central interchange negates h_i. The sum of
h_i on a periodic line cancels separately its nearest and distance-two pair
terms. Product weights are invariant under exchanges, and
c_i(eta)-c_i(eta^edge)=h_i(eta), so the product stationary balance defect is
zero. This holds at every homogeneous product law, not merely p*.
Fixed coefficients and a finite menu give
kappa<=c_i<=kappa+4 max_ab|S_i(a,b)|.

If a signed spatial permutation reverses a bond, its ordered context becomes
(Gr,Gb,Ga,Gl). The orientation sign of the polar tensor and the reversal of
the symmetric-argument expression both negate h, so the transformed rate is
the original rate. Thus actual positive-part rates, including reflections,
are covariant. The implementation is not justified solely by checking a
covariant mean symbol. All occupied/occupied exchanges preserve immutable
labels and capacity just as vacancy exchanges do.

For distinct context/endpoint sites, e.g. Z^3 or tori with every period at
least four, exact product averaging and central-swap symmetrization give

    J_a,i=(1/2) E[h_i(1_left=a-1_right=a)]
         =2p_a[(S_i p)_a-p^T S_i p].

The exterior slots each contribute S_i p. This is a homogeneous-product
current identity, not a claim that an arbitrary evolving law factorizes.
Aliased tiny periodic footprints require separate interpretation/evaluation;
they are not used in this reconstruction or its generic local realization.
At p*=1/15, S_i p*=0 and the exact tangent derivative is
DJ_i=2S_i/15=UA_iU^T. Hence the scale 15/2 is correct.

A separate exact finite control sums the actual kappa+positive-part(h) rate
over all 15^4 contexts in each of three directions at nonuniform rational
p_a=(a+1)/120. Coefficients (sqrt(21),sqrt(105),2,3,sqrt(2)) make all five
channels nonzero and their embedded tensors rational. All fifteen currents
match the formula exactly. This checks the nonlinear rate averaging directly;
it is stronger than merely differentiating the asserted current formula.

For interior p in entropy variables theta, D_theta p=diag(p)-pp^T. Therefore
J_i=grad_theta(p^T S_i p), proving the nonlinear entropy compatibility. These
supplied generators inherit no new limit theorem from this finite computation;
any macroscopic use still requires the previously stated limit hypotheses.

## 4. Dependent reversal and divergence selection implications

Internal Theta flips A signs and leaves B/vacancy unchanged. In these
coordinates T=diag(-I3,I11), so TAT=-A for all five couplings. At the generator
level S_i(Theta a,Theta b)=-S_i(a,b), hence transformed rates equal reversed-edge
rates. In the uniform product the exchange weight ratio is one. The adjoint
diagonal agrees because sum_e[c(eta)-c(eta^edge)]=sum_e h_i=0 pointwise.
Thus Theta L Theta=L*, including diagonals. A fixed fine-count sector need
not be Theta-invariant unless opposite A counts agree. This is conditional
classical generalized reversibility, not quantum time reversal.

The independent addendum checker builds a complete exact 81-state four-site
ring generator with three labels and a symmetric Theta-odd pair tensor
[[0,2,-2],[2,3,0],[-2,0,-3]]. It verifies uniform stationarity and the full
matrix identity RLR=L^T. This reduced-label test targets the diagonal/adjoint
reasoning; the all15 statement follows from the pointwise argument, not from
extrapolation of the toy.

For u_dot=-iA(q)u, q.B is automatically preserved. Requiring the subspace
q.E=q.B=0 to remain invariant while the other moments are arbitrary forces
q^T K_other(q)=0. The independent scalar/tensor columns force
 a1=a2=u=v=0; conversely that member preserves both constraints. This is not
a microscopic Gauss invariance of the unconstrained exchange process.

For derivative observables F=i[q]_cross B and G=-i[q]_cross E,

    F_dot=-im[q]_cross G,
    G_dot=+im[q]_cross F-[q]_cross K_other(q)z.

The signs and all source columns were reconstructed exactly. Scalar columns
vanish because [q]_cross q=0. The D1 tensor source is nonzero at q=(1,1,0),
and the Q12 source at q=e1. Closure for arbitrary other moments and every
nonzero q therefore requires only u=v=0, allowing a1,a2 and longitudinal
sound. At q=0 the derivative fields vanish and impose no selection.

A bounded raw spectral covariance still gives O(|q|^2) derivative covariance.
Closure selects no stationary state. All species counts, including the
higher scalar/tensor combinations, are conserved at q=0. No positive
relaxation gap eliminating those moments has been proved; any decoupling
requires an additional justified scaling or process.

## 5. Author comparison, exact/numerical boundaries and evidence

After both independent seals, the complete 187-line base author checker and
42-line selection checker, their results and logs were read. The base checker
uses exact character arithmetic and a symbolic Gram expansion, but numerical
orthonormality/covariance, spectra, current finite differences and sampled
periodic strings. That distinction is correctly disclosed. Its recorded
current derivative discrepancy is 7.71046004821585e-10 against tolerance1e-7;
its covariance residual is 3.3306690738754696e-16. Those are controls, not
proofs of completeness, stationarity or a limit theorem.

The base result does not embed its source hash. To bind current source and
output, both small author checkers were copied byte unchanged into this
review directory and executed there. Both completed with empty stderr and
produced JSON equal to the recorded original outputs. The selection result's
embedded source hash also matches. These two reproductions are source
comparison, not extra independent mathematical checks. The original
`independent check pending` statuses are preserved historical author output;
this report records the subsequent review without rewriting them.

The independently authored base and addendum controls have fourteen and eight
exact groups, respectively. All passed on first execution; no failed route
or discarded counterexample is concealed. Both complete stdout/stderr pairs,
private-copy author outputs and comparison receipts are retained. No source,
Git state, publication or audit status was changed. No unrelated phase-screen
or winding diagnostic was read. No external literature was needed.

Principal source identities:

| Source | SHA-256 |
| --- | --- |
| Base note | `58bb81005b17fe6a699a23e1a3b77acaa00b3f2d65aefb46f9053729639e6f26` |
| Selection addendum | `b53cefa242a5b8111f79cef560e04492a517719263de372a65c1812a7b18388f` |
| `cubic_entropy_symbol_check.py` | `7103bd3d00d204186952c6d4e7b29d1286a619413b0ce0b01f9cfca179477927` |
| `CUBIC_ENTROPY_SYMBOL_RESULTS.json` and its identical log | `109dce93265e83b464cf3cd24d446faa773acae01b71f982e6e1cc045b1965f8` |
| `cubic_symbol_selection_check.py` | `9cf32449497f5ab1fa7c89a98bfba3d347d0393b4d1cb97fdf5c067464d74ab5` |
| `CUBIC_SYMBOL_SELECTION_RESULTS.json` and its identical log | `8b5071026889b7aadfdae9a6c62f2f5faec3d23fbee040b3d7593f03c7cffbe6` |

Run `independent_check.py`, `selection_independent_check.py` and
`compare_author.py` in this directory with SymPy/NumPy available. The first
two use only their own finite constructions. The third executes private
copies and writes only below this review directory. `FINAL_SEAL.json` binds
all reviewed sources and artifacts and rechecks the unchanged initial seals.
The open physical/limit obligations above remain explicit; this review does
not confer retained or audited status.
