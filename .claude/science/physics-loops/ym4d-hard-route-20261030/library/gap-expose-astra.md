# Repo search

**READ.** The science checkout is pinned at
`1bad6dfa3d3962673d61a692d5895cee2c1b0b9f`.
`prior/gap-expose-astra.md` does not exist at this pin. The lead's
`prior/repo-search-2026-11-08.md` records searches of main and PRs
10114, 10133, 10134 and 10141. It concerns earlier tasks. Its closest
hit is PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md`. I fetched that PR
at `f76f6c649cff7dffbab664d8976e680e8f287fe9` and read lines 1–166.
Credit its Codex author for the exact Wilson transfer and retained
exterior normalization. Its local witness is not the requested
wrapping-surface estimate.

**READ.** Main was fetched at
`bb4ec020d5ada57c630dd89acc98a68397ade423`. Its
`docs/BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md`
was read in full. It concerns SU(3) coefficient samples and an unresolved
recoupled network. No numeric result from it is used. Its distinction
between face coefficients and the sewn network is relevant prior work.
Two further main matches were inspected at their relevant passages:
`docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md:90–110`
concerns local normality of a supplied Hamiltonian model;
`docs/GAUGE_WILSON_PW_COMPRESSION_SHELL_AND_ENERGY_PATH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md:80–106`
concerns energy-controlled projection losses. Neither is the
relative-sector comparison studied below.

**READ.** The assigned `gap-block-astra.md` was read in full;
`gap-tree-astra.md` sections 3–6 and `gap-tree-check-opus.md` were read.
Their local filters, degree-twelve distinction, flat-plane term and
absolute high-spin remainder are reused, not rediscovered. Credit
Codex gpt-6-astra and checker Claude Opus 5.5. The check's restriction
of (G16)'s final simplified constants to beta at most one is retained.
`gap-kappa-order.md:31–74`, by Claude Fable 5.2, already gives the
closed mod-two surface sum, the area bound and the plane integral.

**READ.** Conserved centre sectors and the twisted transfer trace are
also prior work: `gap-kanazawa-astra.md:213–248`, (K9), and
`gap-means-max.md:146–162`, citing the checked (TM-tw) construction.
The task is therefore the interface resolution and its norm budget,
not a new derivation of that trace identity. `gap-ext-astra.md:78–128`
supplies the original ratios and the weaker consumer (FQ).

**READ.** Targeted searches of `open-registry.md`, `open-core.md` and
`l17c.md` for gap-expose, gap-block, gap-tree, conserved centre flux,
icosahedral and G22 found no other owner of this supplier. The registry's
row named B28 belongs to Wightman reconstruction, a different statement.
Local searches also found the existing centre-sector discussion in
`gap-channel-astra.md`; it is not a relative-interface norm estimate.
These are bounded retrieval results, not a repository-wide absence theorem.

# Conserved flux and the cost of resolving an exact transfer

Author: **Codex gpt-6-astra max**, FINISH row 809, 2026-11-12.
Research text, not an audit; this grants no scientific status.
**READ** reports a source. **PROVED** labels a hand argument in this
note, not an independent check. **ARGUED**, **GUIDE** and **OPEN** have
their literal meanings. Definitions inherit the label of their paragraph.

**READ.** Credit **Ethan Sussman and Levent Alpoge, with Claude and
Codex as the authors of their text**, for the Wilson convolution,
half-kernel transfer and Schatten insertion inequality. Both requested
files at `31a47c543775` were downloaded once into the new empty folder
`/tmp/sa-gap-expose-astra.KO5d17/`. Index lookup preceded source reading:
`sa-index/README.md`, chunk 02's neighbouring rows and obligations
63–76; outline 2195–2393. The outline proves (GL3), (GL4), (GL8)
and (GL10). It explicitly does not assert bounded L2 inverse-convolution
conjugation. Its (GL10) assumes the insertion norm; it does not supply it.
The 4.12–4.19 index search found no matching conserved-flux insertion
lemma. Outline 31860–31884, located through chunk 29, and CA-I
2700–2716 were also read: the authors keep the mass-gap question
separate. No Balaban formula or computer-assisted result is an input.

## Checkpoint

**PROVED / OPEN — final checkpoint.** (E4) is an exact conserved-flux
interface sum with the full Wilson transfer. (E6) and (E13) show that
its relative sector selectors have norm one, including the high-spin
tail. Section 3 excludes the specified layerwise absolute norm
estimates from (B30). Lemma 2 excludes bounded direct conjugation of
arbitrary plaquette multipliers, even in the odd flux space. Flat
planes retain their known area weights; the branched majorant (E14)
is insufficient. The unresolved decision is a joint resummation with
the actual exterior trace, beyond section 3's class. (FQ) and (V)
remain open. All science sources retain the revisions recorded above.

## 1. The actual conserved charge and an exact interface sum

**READ / conventions.** Choose time direction r, period t, and a
three-dimensional spatial torus Q. Its edge and plaquette sets are E
and P. Every period is at least three. A time-independent spatial
sign cocycle represents m. Use the unshifted weights of (B1), so the
omitted constant `exp(-beta)` per plaquette cancels in every ratio.
On the full gauge-invariant Hilbert space put

\[
 \mathcal H=L^2(SU(2)^E,dU)^{SU(2)^{V(Q)}},\qquad
 K=\bigotimes_{e\in E}C_\beta,\quad
 C_\beta=\sum_j r_j\Pi_j,\quad z=\int e^{\beta\operatorname{tr}g/2},
\]
\[
 B_m(U)=\exp\!\left(\beta\sum_{p\in P}\eta_{m,p}x(U_p)\right),
 \qquad L_m=z^{|E|}K^{1/2}B_mK^{1/2},\quad x(g)=\operatorname{tr}g/2.
 \tag{E1}
\]

**READ.** Gauge projection is implicit in the restriction to H.
The published transfer identity gives `Z^m=Tr L_m^t`.
The bounded multiplier B_m has a bounded positive inverse on each
finite torus. Every r_j is strictly positive. Consequently L_m is
positive, injective and trace class on H. This is the full transfer,
with all spatial representations and all scalar factors retained.

**PROVED — the distinction from (B4).** Let J_e change the sign of
one spatial edge. These are commuting self-adjoint unitaries on H.
They commute with K and with gauge averaging. At a vertex v, the
product of J_e over its incident edges is the gauge transformation
whose value is `-I` at v and I elsewhere. It is the identity on H.
Thus the centre-odd boundary space of (B4), if projected to the full
gauge-invariant space without another charged endpoint, is killed:
`P_gauge P_-^v=0`. It does not become a flux sector by itself.

**PROVED — precise replacement after sewing.** For an edge set
`b in F_2^E`, define

\[
 E_b=\prod_{e\in E}\frac{1+(-1)^{b_e}J_e}{2}.
 \tag{E2}
\]

These mutually orthogonal projections sum to I. The vertex identity
shows `E_b=0` unless `partial b=0`. They select the parity of 2j on
each edge, retaining every spin, magnetic index and intertwiner.
For a closed spatial one-cochain omega, set
`Theta_omega=product_e J_e^{omega_e}`. Since `d omega=0`, each
spatial plaquette has unchanged sign. Therefore Theta commutes with
B_m, K and L_m, and acts on E_b as `(-1)^{<omega,b>}`.
If omega is exact, Theta is a product of vertex gauge transformations
and is trivial on H. A nonzero flux needs its nontrivial cohomology
class, or equivalently the closed dual interface through the torus.
This supplies the conserved charge; local endpoints have been sewn.

**READ, applied with these conventions.** Put omega on the links
crossing a spatial coordinate cut. Changing the sign of the matching
temporal plaquettes at one time seam represents v. The existing
(TM-tw)/(K9) identity, now in the half-kernel cut, reads

\[
 Z^{m+v}=\operatorname{Tr}(\Theta_\omega L_m^t),\qquad
 Z^m-Z^{m+v}=2\operatorname{Tr}(P_-L_m^t),\quad
 P_-=(1-\Theta_\omega)/2.
 \tag{E3}
\]

**PROVED — interface resolution with the same full transfer.** Insert
the finite resolution (E2) at each temporal half-kernel cut in (E3).
The commutation with Theta removes words that change its eigenvalue.
With `b_{t+1}=b_1`, the result is exactly

\[
 Z^m-Z^{m+v}
 =2\!\sum_{\substack{\partial b_s=0\ (1\le s\le t)\\
                     \langle\omega,b_s\rangle=1\ (1\le s\le t)}}
       \operatorname{Tr}(E_{b_1}L_mE_{b_2}L_m\cdots E_{b_t}L_m).
 \tag{E4}
\]

All sums here are finite. A term need not be nonnegative. The
representations inside K and the entire spatial exponential remain
resummed. Thus (E4) has the common-transfer form of (B28). Its
insertions are exact interface configurations, with norm one whenever
nonzero. No interface multiplier has been discarded.

**PROVED — relation to closed plaquette surfaces, reusing SC.** To
see the spacetime support, expand the spatial multiplier only:

\[
 B_m=\sum_{s\subset P}B_{m,s},\qquad
 B_{m,s}=\prod_{p\in s}\sinh(\beta\eta_{m,p}x_p)
          \prod_{p\notin s}\cosh(\beta\eta_{m,p}x_p).
 \tag{E5}
\]

Under J_e this multiplication operator has parity `(partial s)_e`.
Hence `E_b B_{m,s} E_c=0` unless `b+c=partial s`.
In the fully expanded word the temporal faces are b_s and the
spatial faces at the intervening layer are s_s. The equations
`partial b_s=0` and `b_s+b_{s+1}=partial s_s` say exactly that their
union is a closed mod-two two-chain. Its twist pairing is
`<omega,b_s>`, independent of the layer. This is Proposition SC's
closed surface in the transfer picture, including branching.
The area bound of Lemma M gives at least `a^2` plaquettes in
the aspect ratios of the task. Refining (E4) by (E5) replaces L_m
by `z^{|E|}K^{1/2}B_{m,s}K^{1/2}`. Those refined factors are not the
same L_m. Their restoration to (B28) needs a further argument.

## 2. Exact normalization against the full transfer removes the gain

**PROVED, Lemma 1 — a relative-sector norm.** Let K be bounded, positive,
injective, with dense range on a Hilbert space. Let A be a bounded
positive operator with bounded inverse. If F is a nonzero orthogonal
projection commuting with K, set

\[
 R=A K^{1/2},\quad T=RR^*,\quad T_F=RFR^*.
\]

Then the smallest c such that `T_F <= c T` as quadratic forms is
exactly one. Moreover there is a unitary U such that

\[
 R=T^{1/2}U,\qquad
 T_F=T^{1/2}(UFU^*)T^{1/2},\qquad \|UFU^*\|=1.
 \tag{E6}
\]

**PROVED — argument without an unbounded inverse.** R and R* are
injective with dense ranges: use injectivity of K and invertibility
of A, and the identity `(ran R)^perp=ker R*`. On the dense range of
R*, send `R*f` to `T^{1/2}f`. Their squared norms both equal
`<f,Tf>`. This isometry extends to a unitary U. The identity
`UR*=T^{1/2}` gives (E6) after taking adjoints. Since F is an
orthogonal projection, `0<=T_F<=T`. If `T_F<=cT`, then
`<R*f,F R*f><=c||R*f||^2`. Density extends this inequality to all
vectors. A unit vector in ran F gives `c>=1`. This also proves the
uniqueness of a bounded insertion between the two T half-powers.

**PROVED — application to the original Wilson integral.** Take
`A=z^{|E|/2}B_m^{1/2}` and the K of (E1). Then T is the full Wilson
transfer in the spatial half-action cut. Selecting temporal parities
b replaces K by `K^{1/2}E_bK^{1/2}` and gives T_b=T_F exactly.
Thus its insertion in the compatible full-transfer reference is the
projection `U E_b U*`. Both cuts give the same norm one, and the
unitary U includes the entire spatial action. The reference is common
to all sectors. Choosing a common positive scalar does not alter
`T_b<=cT` or its optimal c. The scalar therefore cannot restore a gain.

**PROVED — why (B16) cannot bound this relative remainder.** The
lemma applies also to a link-spin cutoff projection and to its
complement, restricted to any nonempty conserved flux sector. Their
relative insertion norms are both one whenever the subspaces are
nonzero. This remains true for arbitrarily large cutoffs. For example,
put a half-integer spin j on a simple winding loop and zero elsewhere;
its Wilson character is a nonzero gauge-invariant vector in the odd
flux space. It supplies high-spin vectors at every cutoff. The
fundamental loop supplies a low-spin vector once `J>=1/2`.

**READ / PROVED — application limit.** (B15)–(B19) estimate an *absolute*
block operator divided by a specified scalar. Their proved bound
`||T_high||<=constant eta_J`, with `eta_J -> 0`, is retained. It does
not imply `T_high<=epsilon_J T` with `epsilon_J -> 0`. Lemma 1
refutes that latter implication for the actual Wilson transfer.
The discarded absolute coefficient occurs in the reference as well.
No use of the finite low-spin matrix alone pays this comparison.
More precisely, `T_F=RFR*` has the same nonzero eigenvalues as
`F R*R F=F L_m F`. Thus (B15)'s compression and (B16)'s absolute
tail bound apply in the other cut by `XX*`/`X*X`. Comparing either
one with the full T is the additional, failed step.

**PROVED — all exterior vectors are too strong, at any block length.**
Since P_- commutes with L_m and L_m is injective,

\[
 2P_-L_m^n\le\epsilon L_m^n\quad\Longleftrightarrow\quad
 \epsilon\ge2\qquad(n\ge1),
 \tag{E7}
\]

provided the odd flux space is nonzero. Test an odd vector for
necessity; `0<=P_-<=I` gives sufficiency. Equivalently, the supremum
of the defect ratio over positive rank-one exterior operators is two.
This is an obstruction to an all-exterior operator comparison, not
to its trace against the actual Wilson exterior. A rank-one odd
exterior need not have a pointwise positive Wilson kernel. No such
identification is used in (E7).

## 3. A natural class cannot satisfy (B30)

**PROVED — class and theorem.** Fix any compact positive beta
interval I, for example `[1/2,1]`. Consider the following class of
estimates of (E4), for all boxes `n=(a,a,c,d)`, `c,d in {a,2a}`:

1. Keep the same L_m in every layer. Resolve the temporal convolution
   by its orthogonal representation or parity sectors. Spatial Wilson
   factors may already be fully resummed, as in (E4).
2. At each layer, one may refine a selector F into an absolutely
   operator-norm-convergent sum `F=sum_alpha c_alpha Y_alpha`.
   Products of bounded maps are allowed inside Y, with their full
   norm product charged. All scalar factors and errors are charged.
3. Expand these local identities independently at the different
   layers. Apply the triangle inequality separately at each layer,
   charging the full Cartesian product of the local sums before
   any interlayer or trace-dependent simplification. Keep different
   temporal histories separate when taking absolute coefficients.
   Use (B29)'s product of insertion norms.
   Assign each resulting defect term to one connected wrapping
   plaquette set. No cancellation or joint resummation between
   different layer words is used to reduce that norm cost.

In particular, evaluating a completed word to zero and then deleting
its charged norm cost is outside this class of estimates; a zero local
summand already has zero norm and costs nothing. The theorem does not
rule out exploiting exact identities between successive layers.

No estimate in this class has the uniform coefficient and operator
budgets (B30), with fixed `h>0`, `D>=1`, `0<q<1` and
`400 h q^(1/D)<1`. This is a theorem about layerwise absolute
resolution, not about every resummed Wilson-block expansion.

**PROVED — proof.** For any nonzero orthogonal selector F,
the triangle inequality gives

\[
 1=\|F\|\le\sum_\alpha |c_\alpha|\,\|Y_\alpha\|.
 \tag{E8}
\]

If Y is factored, its charged product of norms is no smaller than
its norm. The same holds when an error term is kept in the sum.
Thus each independent layer contributes absolute norm cost at
least one. Scalar redistribution cannot change this conclusion.

Take a straight winding spatial loop C in direction i, paired
oddly with omega, and select `b_s=C` at every layer. Its underlying
temporal plaquette set is the connected flat wrapping `(r,i)` plane.
The projection E_C is nonzero: the fundamental Wilson character
around C lies in its range. The word itself is nonzero. Indeed,
`E_C L_m E_C` is a nonzero positive trace-class operator, and its
t-th power has strictly positive trace. Its contribution to (E4)
is twice that trace. After all the local refinements allowed above,
the sum of absolute coefficients times charged norm products for
this one history is at least

\[
 2\prod_{s=1}^t
       \left(\sum_{\alpha_s}|c_{s,\alpha_s}|
                               \|Y_{s,\alpha_s}\|\right)\ge2.
 \tag{E9}
\]

For the unsplit history the product is exactly one. Nonnegativity
of the cost means other histories cannot reduce (E9).
If the proposed assignment to connected sets obeyed (B30), summing
its cost bounds over all such sets would instead give

\[
 \sum_{\text{all defect terms}}|c_\gamma|
                              \prod_s\|X_{\gamma,s}\|
 \le\frac{N_p}{400q}\frac{\rho^{a^2}}{1-\rho},\qquad
 \rho=400h q^{1/D}<1.
 \tag{E10}
\]

This is exactly row 807's connected-set count, now applied to the
norm cost before taking a trace. `N_p<=24a^4`, so (E10) tends to
zero as a tends to infinity, contradicting (E9). If a proposed
assignment cannot be made because decorations are not localized,
it already fails the class's third clause, before its budget test.
This proves the theorem, at every beta in I and hence uniformly.
Moving the factor two into a fixed overall prefactor changes the
lower bound two to one; the same contradiction remains.

**PROVED — nonempty coarse selectors do not help.** Replacing a
collection of orthogonal selectors at one layer by their sum gives
another orthogonal projection of norm one. If the winding-loop
history survives that grouping, the same argument applies. Arbitrary
joint block resummations that change the layer words are excluded
from the theorem. They are a substantive possible escape.
For the still narrower choice of retaining only global flux sectors,
(E7) excludes an all-exterior comparison at every block thickness.

**ARGUED — relation to row 804.** This is not another free insertion
of an artificial filter into a Haar tensor. The projections here are
the exact restrictions of the full Wilson temporal convolution.
Lemma 1 includes the resummed spatial action and the common exterior
reference. What fails is attempting to retain its coefficient decay
again as a relative insertion gain.

## 4. Attempt to expose spatial faces without changing the transfer

**PROVED, Lemma 2 — a direct conjugation is unbounded.** A spatial
plaquette multiplier cannot in general be moved across the Wilson
half-convolution as a bounded insertion. Take a simple spatial
plaquette p, let `f=x(U_p)`, and let `phi_j=chi_j(U_p)`.
These are orthonormal gauge-invariant functions: the plaquette
holonomy is Haar, and characters are orthonormal. One-link Schur
orthogonality gives `K phi_j=r_j^4 phi_j`. The sine addition identity
`2 cos(theta) sin((2j+1)theta)=sin((2j+2)theta)+sin(2j theta)`
gives `2f phi_j=phi_(j+1/2)+phi_(j-1/2)` for `j>=1/2`.
Thus on this finite-spin domain

\[
 K^{1/2}M_fK^{-1/2}\phi_j
 =\frac12\left(\frac{r_{j+1/2}}{r_j}\right)^2\phi_{j+1/2}
  +\frac12\left(\frac{r_{j-1/2}}{r_j}\right)^2\phi_{j-1/2}.
 \tag{E11}
\]

The positive Bessel recurrence in (GL4) gives

\[
 \frac{r_{j-1/2}}{r_j}
 =\frac{I_{2j}}{I_{2j+1}}
 \ge\frac{2(2j+1)}{\beta}.
 \tag{E12}
\]

Consequently the norm of (E11) is at least
`2(2j+1)^2/beta^2`, which diverges. The reverse conjugation is
unbounded by the raising coefficient instead. All inverses used
in this argument act only on finite-spin vectors, where they are
defined. No asserted inverse on an entire smooth domain is needed.

**PROVED — the same failure in an odd flux sector.** On sufficiently
large spatial tori choose a simple winding loop C disjoint from
the four edges of p. Multiply each phi_j by `chi_(1/2)(U_C)`.
The functions remain orthonormal, since their edge sets are disjoint.
They are gauge invariant and have odd flux through the cut of C.
Their K eigenvalue acquires the same factor `r_(1/2)^|C|`, which
cancels in (E11). Thus the divergence holds on the actual odd flux
space too. It is uniform on I when beta is replaced by beta_+ in
the lower bound.

**ARGUED — exact failed step, and its limit.** To move
`z^|E| K^(1/2) M_f B_m K^(1/2)` into `X L_m`, the formal choice is
`X=K^(1/2) M_f K^(-1/2)`. Lemma 2 rules out this bounded-operator
procedure even for one ordinary plaquette polynomial. The outline
already warned that (GL5) is only a smooth-domain construction;
(E11) supplies an explicit failure on the charged Wilson space.
It does not prove unboundedness for every particular nonlinear
function `B_(m,s)/B_m` of (E5), or forbid a different placement of
two half-kernels. Such a replacement must be proved separately.

## 5. Where the degree-twelve distinction enters, and where it does not

**READ.** Keep the checked (G12)–(G17a). Let Gamma be the binary
icosahedral group, V its defining representation, and h its extra
invariant in `Sym^12 V`. For every k, `h^k` is a nonzero invariant
in `Sym^(12k) V`. SU(2) convolution on the charged parent space
`V tensor Sym^(12k) V` tends uniformly to zero on I as k grows,
by the factorial bounds. Gamma retains the copy `V tensor h^k`
with eigenvalue at least `beta_-/(4 exp(beta_+))`. U(1) retains a
weight-one copy with eigenvalue at least
`beta_-/(2 exp(beta_+))`. These are the existing, precise control
failures for transplanting (B16)'s parent-spin bound.

**PROVED — low and high spins in the compatible reference.** The
distinction does not turn (E6) into a strict contraction for SU(2).
For any finite-spin unit vector psi selected by F, set
`f=A^(-1)K^(-1/2)psi`. This inverse is defined on that finite-spin
psi, f belongs to H, and `R*f=psi`. Hence

\[
 \frac{\langle f,T_Ff\rangle}{\langle f,Tf\rangle}=1.
 \tag{E13}
\]

This uses a single explicit vector. A low-spin winding loop already
supplies psi; increasing J cannot fix it. A high-spin loop supplies
the identical test beyond every J. The exterior vector f need not
lie in the low-spin cutoff, since A inverse contains the full spatial
weight. Thus (E13) is a generalized all-exterior comparison for the
selected low-spin sector; it does not assert that the scalar-normalized
matrix A_J of (B15) has a unit eigenvalue. The relative high-spin
remainder has norm one for the same reason. The absolute matrix
and absolute tail bounds remain valid; passing from them to this
relative comparison is what fails.

**READ / PROVED — binding control tests.**

| Step | SU(2) | U(1) | Binary icosahedral Gamma |
|---|---|---|---|
| Centre parity and (E4) | Exact | Exact for the subgroup `{1,-1}` | Exact |
| Absolute SU(2) parent-spin tail (B16) | Valid, read from row 807 | Cannot transplant: zero-weight parents and their weight-one charged extensions | Cannot transplant: first extra invariant at degree twelve and the copies `V tensor h^k` |
| Relative-sector contraction required by this construction | Fails at (E6), (E8) | Fails at the same norm-one selector | Fails at the same norm-one selector |

**PROVED — controls for the last row.** U(1) has positive Fourier
coefficients at every integer weight, from the exponential series.
Gamma's normalized Wilson convolution is strictly positive on each
actual irreducible. Indeed, matrix entries of its faithful V separate
points of the finite group; their polynomial algebra, including
conjugates, is every function on Gamma by finite interpolation.
SU(2)'s invariant alternating form identifies the conjugates with V.
Thus every irreducible occurs in some tensor power of V, and its
character coefficient in `exp(beta chi_V/2)` is positive. The
injectivity used in Lemma 1 holds for both controls. Their winding
fundamental characters give nonzero odd parity selectors. No
confinement conclusion for either group passes the construction.

**ARGUED — scope of the tests.** This is a failed construction for
SU(2) as well, not a new group-selective estimate. The degree-twelve
distinction survives at the absolute-tail step; it cannot repair
the relative normalization step. Nor does agreement of Haar tensors
through degree eleven identify Wilson-tilted low-spin matrices at
positive beta: their full exponential still reads higher degrees.

## 6. Flat planes and branched low-spin surfaces keep their own weights

**READ, reused without another proof.** For a single flat wrapping
fundamental plane of area A, (G21)/(B32) gives exactly
`2 r_(1/2)^A` in the one-plaquette-normalized twist difference.
It has no high-spin exposure. On I, `r_* = max_I r_(1/2)<1`.
Row 807 bounds the sum over these planes, including all orientations,
by `48 a^2 r_*^(a^2)` at the task's aspect ratios. This is their
proper area payment. It is not divided by the full Z^m.

**PROVED — why (E9) does not contradict that payment.** Selecting
E_C in (E4) keeps every allowed spin on C and all spatial interactions.
The small weight of the undecorated fundamental plane lives inside
the trace, in powers of K. Bounding the word by (B29) discards that
information. E_C having norm one does not say that the trace has
order-one weight. Nor may one extract `r_(1/2)^A` from E_C while
keeping the full transfer: an exact scalar redistribution replaces
E_C by `r_(1/2)^(-ell) E_C` at a layer of ell selected links. Its
norm costs exactly the extracted scalar back. The character term
and its full-reference insertion are different estimates.

**PROVED — a valid, but insufficient, area majorant for branching.**
Let gamma be the full nonzero plaquette support of a character term,
and label its faces by `0<j_p<=J`. In the one-plaquette-normalized
partition function its weight is

\[
 a(\mathbf j)=\left(\prod_{p\in\gamma}d_{j_p}r_{j_p}\right)
               \int\prod_{p\in\gamma}\chi_{j_p}(U_p)\,dU
\]

up to a twist sign. The integral need not be assigned a sign.
The elementary character bound `|chi_j|<=d_j` gives

\[
 \sum_{\substack{\operatorname{supp}\mathbf j=\gamma\\0<j_p\le J}}
           |a(\mathbf j)|
 \le W_J(\beta)^{|\gamma|},\qquad
 W_J(\beta)=\sum_{0<j\le J}d_j^2 r_j(\beta).
 \tag{E14}
\]

This includes every branching pattern and all its link integrals.
It charges face area, without pretending that branching forces high
spin. It is deliberately crude and gives no cancellation of vacuum
decorations against Z^m.

**PROVED — this particular majorant fails at order one.** On
`I_0=[1/2,1]`, the normalized fundamental eigenvalue is
`r_(1/2)=integral x exp(beta x)/integral exp(beta x)`.
Centre symmetry removes odd moments, and `integral x^2=1/4`.
Every surviving coefficient in its numerator is nonnegative, so

\[
 r_{1/2}(\beta)\ge\frac{\beta}{4e^\beta}>\frac1{24},
 \qquad W_J(\beta)\ge4r_{1/2}(\beta)>\frac16
       \quad(J\ge1/2,\ \beta\in I_0).
 \tag{E15}
\]

Here `beta>=1/2` and `e^beta<=e<3` give the strict rational bound.
The displayed majorant, combined only with the count 400, has
`400 W_J>1`; it cannot establish a convergent area sum. Splitting
W_J into a scalar and a nominal q changes neither its product nor
this failure. This is a failure of (E14)'s upper bound, not a lower
bound on the actual summed branched weight. Flat planes are counted
by their polynomial multiplicity instead, as above. A useful bound
for the other low-spin surfaces remains open.

**ARGUED — what a successful resummation must retain.** The
interface formula (E5) already enforces conservation for branched
surfaces. What it does not supply is a small normalized activity
after summing their spin labels, signs and decorations. Summing
those before using absolute values is outside the theorem of
section 3. It is also a possible way to avoid its obstruction.
Any such step must still compare with the same Z^m.

## 7. Weakest sufficient statement and the remaining work

**READ / exact reformulation of the consumer, not a new closure.**
For a crossed pair of `gap-ext-astra.md` define

\[
 p_{m,i}(a)=\frac{\operatorname{Tr}(P_{-,i}L_m^a)}
                         {\operatorname{Tr}L_m^a}
           =\frac{1-R_m(v_{1i})}{2},\qquad
 Q_F=\max_{m_2=0,\ i=3,4}p_{m,i}(a).
 \tag{E16}
\]

The weakest sufficient statement used here is the existing (FQ):
`8 Q_F <= K(a) sqrt(S_ev(a))`, `Q_F<1/192`, with polynomial K.
For example the already available lower bound `S_ev>=eta_*^a`
makes the following uniform large-a estimate sufficient:

\[
 Q_F\le C a^p\eta_*^{a/2},\qquad 0<\eta_*<1.
 \tag{E17}
\]

Then choose `K(a)=8 C a^p`; the strict smallness holds for all
sufficiently large a. One may reduce the existing eta_* below one
without weakening its lower bound. No area exponent is needed for
this sufficient version. Neither (E17) nor (FQ) is proved here.

**PROVED — a trace-level attempt retains an extensive cost.** In
(E1), `e^(-beta|P|) I <= B_m <= e^(beta|P|) I`. The variational
characterization of each eigenvalue, on H or its odd sector, gives

\[
 p_{m,i}(t)\le e^{2\beta|P|t}
       \frac{\operatorname{Tr}(P_{-,i}K^t)}{\operatorname{Tr}K^t}.
 \tag{E18}
\]

Indeed the corresponding eigenvalues of L_m lie between
`z^|E| e^(-beta|P|)` and `z^|E| e^(beta|P|)` times those of K;
raise the nonnegative eigenvalues to t and sum. This uses
eigenvalue monotonicity, not the false general inference that
`A<=B` implies `A^t<=B^t`. With the task's aspect ratios the
exponent `|P|t` is of order a to the fourth power. Therefore an
area estimate for the electric trace alone would not make this
comparison useful. Cancelling that spatial vacuum cost is still
an analytic obligation; it is not supplied by finite-volume
strict positivity.

**OPEN — exact missing supplier.** To obtain (B28)–(B31), one must
resum complete spatial and temporal histories into bounded
insertions whose *total* norm cost passes (B30), or prove a weaker
trace estimate such as (E17) directly with the actual exterior.
The resummation must go beyond the layerwise absolute class of
section 3. An all-exterior domination of the whole odd sector is
impossible by (E7). A direct move of arbitrary plaquette
polynomials through the Wilson half-kernel is impossible by
Lemma 2. The missing constructive step is a trace-compatible
resummation of low-spin wrapping surfaces and their decorations
that pays the common normalization. The absolute high-spin tail
and the degree-twelve distinction do not supply it.

**ARGUED — scope and next decision.** The negative theorem has one
explicit family: layerwise sector resolution with separate triangle
inequalities at each layer, before interlayer simplification.
Its proof covers scalar reallocations, exact local
refinements, charged error terms and nonempty orthogonal groupings.
It does not exclude joint blocks across layers, sign cancellations
before the absolute sum, a norm tied only to actual exteriors, or
a direct trace estimate. Those are changes of the stated family,
not defects in its counterexample. No universal fixed-block
impossibility, order-one area law, (V), or mass gap follows.
The next useful attempt must give one of those joint resummations
and its actual reference; repeating the local filter or increasing
the spin cutoff cannot change (E13).

**READ — verification boundary.** All new arguments are by hand.
No numerical run, enumeration, interval calculation or Lean check
was used. No independent check of this note has occurred. Only this
assigned file was changed in the checkout. The registry, FINISH,
audit records and ledgers were left as read. The file remains local
on `research/gap-expose-astra-20261112`, based on the requested pin;
no commit, push or external post was made.

RESULT: SCOPED OBSTRUCTION PROVED BY HAND, NOT INDEPENDENTLY CHECKED — (E4) keeps the full Wilson transfer, but sector resolutions estimated by separate layerwise triangle inequalities cannot meet (B30): their total insertion norm cost is at least two, and their relative low- and high-spin selectors have norm one. The degree-twelve absolute-tail distinction is retained; the attempted contraction fails for both controls at named steps. A trace-compatible joint resummation paying low-spin surfaces and the original normalization remains OPEN; neither (FQ) nor (V) is proved.

