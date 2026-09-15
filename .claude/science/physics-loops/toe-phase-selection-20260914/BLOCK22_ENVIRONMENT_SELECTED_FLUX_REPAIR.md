# Block22: selecting the integer repair from the physical environment

Personal active proof candidate,2026-09-15. This is a continuation of
BLOCK22_FIXED_CLOCK_DEFECT_LOCALIZATION_DERIVATION.md, not an independently
reviewed theorem or a native formation law. It removes the fixed-axis choice
from a particular almost-sure physical flux representative. It does not
select a Villain law or supply a nearest-neighbor record-production rule.

## 1. Exact scope

Fix an ODD clock order N>=3 and a finite beta satisfying the principal-flux
cluster condition in the preceding note. Let mu be any subsequential local
limit of the original, ungauge-fixed free-box Z_N Villain link law in four
Euclidean dimensions. The preceding note gives finite principal magnetic
charge components, with

 Pr(M(C(c))>=m)<=C_q exp(-b_beta m),
 C_q=6/92², b_beta=-log[2*92² exp(-beta pi²/18)]/12>0.  (1)

The local Gibbs condition is on the ORIGINAL link registers, with all N
values allowed. A gauge-fixed conditional law is not substituted here.

For odd N, the principal integer residue b in
{-(N-1)/2,...,(N-1)/2} is odd under orientation reversal. Thus u=2pi b/N
and q=d2 b/N transform as genuine real/integer cochains under lattice
isometries and under global charge conjugation. At even N the pi tie spoils
this simple statement; that case is not included in this construction.

Let G be the full group of signed coordinate permutations in four dimensions,
|G|=384. It is a symmetry group of the supplied Euclidean Villain model; this
is not asserted to be additional content of the framework's Z3 Lattice axiom.
Translations, the physically relevant spatial cubic subgroup, and global
charge conjugation will be included in the covariance statement.

## 2. Finite energy breaks exact spatial coding ties

Write w_beta(v)=sum_k exp[-beta(v-2pi k)²/2], and

 m_beta=min_(v in circle) w_beta(v)>0,
 M_beta=max_(v in circle) w_beta(v)<infinity,
 epsilon=(m_beta/M_beta)^6/N>0.

A link belongs to at most six plaquettes in four dimensions. Its conditional
probability for EACH of its N values, given all other links, is at least
epsilon. This holds for every finite beta; no high-temperature mixing or
independence is assumed. The inequality follows by bounding each of the
six local factors below by m_beta and the N-term normalizer above by
N M_beta^6. The DLR identity passes this finite conditional statement to mu.

Consider two different framed origins (x,g,s) and (y,h,t), where x,y are
integer lattice vertices, g,h in G and s,t in {+1,-1}. Their codes are the
entire compact plaquette-residue configurations pulled back to those
origins/frames and multiplied by s,t modulo N. The cells are enumerated by
increasing l_infinity base radius, then by a fixed finite lexicographic order
of bases and orientations. This is just a comparison convention on the
pulled-back arrays. Under an external symmetry the collection of candidate
codes is permuted without changing any code value.

For a pair of compared plaquettes with different underlying supports, choose
a link belonging to one and not to the other. Conditional on all other
links, equality of the two residues fixes exactly one of its N values.
If the two framed origins are identical and only s=-t, equality fixes
2b_p=0 modN. Odd N again permits exactly one link value. Therefore each
such equality event has conditional probability at most

 rho=1-(N-1)epsilon<1.                                (2)

A collection of comparisons with disjoint link supports admits iteration of
this bound: condition on all links except a chosen distinguishing link,
apply(2), remove that equality factor and repeat. Correlations through the
Gibbs interaction do not invalidate this conditioning argument.

In particular no nonidentity affine signed-permutation/charge-conjugation
map fixes the complete plaquette configuration almost surely. There are
countably many such maps. For any fixed one, infinitely many disjoint
comparison pairs can be chosen, and their probability of all matching is
bounded by rho^k for every k. A map may have a fixed plane or line; choose
comparison plaquettes away from it. A pure nonzero translation also leaves
some edge of a plaquette outside its image, even when the two plaquettes
share another edge. This excludes exact global ties, not long correlation
lengths or spontaneous breaking between Gibbs states.

## 3. A unique frame for each finite charge component

For a nonzero finite component gamma, take as candidate origins all lattice
vertices on its primal3-cells. Their number is at most8M, where M is the
integer charge mass. For every origin take every g in G and both s signs.
The number of candidates is at most6144M. Compare their infinite codes from
section2 and take the lexicographically least one.

Two distinct candidates have different codes almost surely by section2.
Among finitely many candidates, every pair has a first differing cell, so
there is a finite code radius at which the winner is determined. This is an
almost-sure statement on the Gibbs domain, not a deterministic solution on
all configurations. Exactly symmetric configurations form a null set for the
stated measure; no rule on them is claimed to follow from covariance.

Let T(z)=x+g z for the winning framed origin, with winning sign s. Pull gamma
back to gamma'=s T^*gamma. Use the explicit coordinate contraction from the
preceding note to construct its integer2-form filling F(gamma'), and return

 n_gamma^cov=s (T^-1)^* F(gamma').                      (3)

Pullback conventions here treat a cochain as a function on oriented cells;
(T^-1)^* is the inverse map carrying the coordinate filling back to the
physical lattice. Since d commutes with cellular isometry pullback and
s²=1, d2 n_gamma^cov=gamma. All mass, amplitude and support bounds of the
preceding note survive signed permutations and translations.

Under an external lattice isometry or charge conjugation, candidate origins,
frames and signs permute, and each pulled-back code remains identical.
The winner therefore transforms with the input, making(3) covariant. The
fixed ordering used to compare CODES does not fix a physical coordinate
frame: every candidate is compared in its own coordinates. No independent
random mark or additional microscopic state is introduced.

## 4. A quantitative finite-window coding estimate

The almost-sure argument can be made uniform for small components. Fix a
component gamma of mass M, and suppose a code radius L>=4096 satisfies
M<=L/4096. Its event of being exactly the root component is determined by
its charges and the absence of neighboring charges, hence by a finite link
neighborhood within distance two of its cell support.

For any two distinct candidates use the reference plaquettes with axes(0,1)
and bases n v, where

 v=(1,4,16,64),
 ceil(L/256)<=n<=floor(L/128).

Both candidate images lie within code radius L, and outside the protected
component neighborhood. There are at least L/512 such n for L>=4096.
If the two signed coordinate frames differ, g v!=h v because v has distinct
nonzero coordinate magnitudes. Their plaquette bases separate by at least
n-|x-y|_infinity minus two orientation offsets. Since origins lie on the
component, |x-y|_infinity<=M+2. The lower n bound and M<=L/4096 keep the
plaquettes more than one cell apart. If frames agree and origins differ,
the two plaquettes are distinct translates; a distinguishing edge still
exists. If both agree and only the conjugation sign differs, use the
odd-N argument in section2.

Within either candidate image, successive plaquettes have disjoint link
supports because the step has l_infinity size64. Each comparison involves
at most eight links; each link can occur in at most two comparisons, one
from each candidate family. The conflict graph of comparisons therefore
has degree at most8. A greedy independent set retains at least a ninth of
them. The deliberately weaker bound L/9216 comparisons is sufficient.
Their distinguishing edges lie outside the links specifying gamma, so the
conditional finite-energy iteration also preserves the event C(root)=gamma.
For any fixed candidate pair,

 Pr(pair codes agree through L | C(root)=gamma)
 <=rho^(L/9216),                                      (4)

whenever the conditioning event has nonzero probability. This is a finite
cylinder conditioning, not an assumed independent exterior environment.
Union over candidate pairs gives the conservative estimate

 Pr(winner not certified by radius L | C(root)=gamma)
 <=min(1,(6144M)² rho^(L/9216)).                       (5)

For the assertion about code equality, using all pairwise distinct prefixes
is stronger than necessary for certifying the minimum, and so is a valid
sufficient stopping rule. The rate may be extremely small at large beta;
this is a mathematical existence/locality bound, not an efficient algorithm.

## 5. Covariant real holonomy and locality in probability

Define n^cov=sum_gamma n_gamma^cov and u^cov=u-2pi n^cov. The same mass and
support bounds as before imply local finiteness and every finite local
moment. Then

 d2 u^cov=0,
 exp(iu^cov_p)=exp(iu_p),
 exp(iN u^cov_p)=1                                    (6)

almost surely. Every finite integer Wilson cycle is represented exactly by
the exponential of the real surface integral of u^cov, independent of the
chosen finite spanning surface. The representative now transforms covariantly
under translations, signed coordinate permutations and charge conjugation
on their common full-measure domain. One explicit invariant choice of domain
requires finite charge components, absence of every nonidentity affine/code
tie, and, for every lattice vertex x,

 sum_gamma M_gamma² 1{dist_infinity(x, geometric_support(gamma))<=8M_gamma}
 <infinity.

The mass tail(1), a polynomial bound on possible nearby roots, and summation
over masses give finite expectation for each such sum. Countably many
vertices preserve full measure. Geometric cell supports make this domain
invariant under all the stated transformations, including orientation/base
offsets. The support bounds guarantee that every contributing filling lies
in this summable class. If the original Gibbs state has these
symmetries, so does its pushforward; otherwise this is equivariance between
transformed states, not a symmetry claim for an individual state.

For a finite-window approximation at a target plaquette p, discard components
not fully verified within the window and discard any whose winner has not
been certified from the available code prefixes. To quantify the error, split
contributing components into mass larger than R/C and the remainder, with
one fixed sufficiently large geometric C, e.g.C=2^18. Equation(1) and the
support bound6M give an exponential tail in R for the first class, even
after summing possible roots and masses. For the small components, take
L=floor(R/4). Their candidate origins and all observed codes lie within the
radius-R window, and M<=L/4096 once R is sufficiently large. Equation(5),
summed over O(R^4) possible roots and O(R^2) candidate pairs, gives a bound
by a fixed polynomial in R times rho^(floor(R/4)/9216). Both parts are
bounded by A exp(-cR) for constants A,c>0 depending on beta,N.

This proves exponential approximation in PROBABILITY. The absolute sum of
component contributions has uniform moments, also for the truncated rules.
Hölder therefore upgrades the approximation to every fixed finite L^r norm,
with possibly smaller positive exponential rate. It is not deterministic
finite-range dependence, operator-norm locality, nor a claimed finitary
coding radius stable against every possible exterior modification. A remote
large closed defect can change a chosen filling inside an otherwise empty
window; the earlier long-cycle control preserves that distinction.

## 6. What has and has not been removed

The supplied fixed-clock Gibbs configuration can supply the frame for this
particular flux representative almost surely. Its source is the actual
finite-energy distribution and the proved finite-component geometry. This
retires an external-frame choice inside this probability construction.

The original Villain law, beta,N, four-dimensional carrier and state-selection
problem remain supplied. A nearest-neighbor Admissibility rule, full-domain
law, actual N=3 penalty-Hamiltonian phase, Gaussian scaling limit, matter
coupling and native TOE are not established here. Nor does the almost-sure
frame selection choose a unique Gibbs phase. This is a proposed constructive
bridge to a covariant closed real flux, with the clock quantization retained.
