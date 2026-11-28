# Repo search

The lead's November 8 digest was read in full. It concerns earlier
large-field/history targets. Its common-reference warnings are related,
but do not prove (CF). Row 778's search locates the closer warning in
PR 10114's `checks/review_massgap_block_literature.md:112–121`:
separate interpolation does not supply a common twisted endpoint.
The local Wilson witness is already consumed by `gap-fusion-astra.md`.
Neither is an order-one vortex estimate. These are prior results, not
new work here. I checked the review at lines 105–130 and PR 10114's
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:89–166`, rather than treating the
lead's digest as evidence.
Those two PR paths are relative to
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.

This checkout is pinned at `cbfbf26f0149108a6025960ded48b627e3acddd4`.
Main was fetched at `a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc`.
PRs 10114, 10133, 10134 and 10141 were fetched for bounded reading.
Their read revisions respectively were `f76f6c649cff`,
`89faef229ff6`, `1e70c7211a2c` and `fb99b4dddc72`.
The target-specific `prior/gap-cf-astra.md` does not exist at the pin.
Searches of `open-registry.md`, `open-core.md` and `l17c.md` found no
other owner of (CF). Rows 778 and 780 supply the contraction and its
check; rows 781 and 782 own the broader literature searches. This
note does not repeat their tasks. No absence theorem follows from
these searches.

A closer finite-group hit is **Claude Fable 5.2 medium's
`gap-kappa-order.md:113–120`**: the Q₈ flat-holonomy counts and the
absence of a flat connection in a rank-four twist are already there.
They are reused below. That note attacks (KP), not (CF). Main's
`docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md:1–55`
concerns nearest-neighbour conditional-law examples, not Q₈ Wilson
theory. The quaternion hit in `CHARGED_STATIONARY_JET_ASTRA.md`
is likewise not a twisted gauge partition-function comparison.

The Sussman–Alpoge index was searched before its cited source lines.
The nearest common-normalizer material is outline ET5–ET6,
`/tmp/sa_ym4.tex:26765–26805,26848–26867`, indexed in chunk 24
and `obligations.md`: a scalar covariance comparison conditional
on its companion normalizer, not a construction for the present
twisted pairs. Outline lines 565–600 and CA-I lines 2490–2515,
2698–2714 delimit their clustering claims; they do not assert this
vortex bound. No such supplier was found in the index searches
for vortex, electric flux, the commutator law or quaternion groups.

## Contract and checkpoint

Author: **Codex gpt-6-astra max**, FINISH row 783, 2026-11-12.
Research text, not an audit; this grants no status. `PROVED` denotes
an author hand proof, not an independent check. `ARGUED` denotes an
unverified argument or literature import; `GUIDE` decides nothing;
`OPEN` denotes an obligation not established here.

The GOAL and specified FINISH sections, row 778 Sections 4–8,
row 780, fusion Sections 5–6, and Grok literature Part D were read.
Credit Codex for row 778 and fusion; Claude Opus 5.5 for row 780;
and the named authors of the literature record. The Sussman–Alpoge
outline and CA-I were fetched once at `31a47c543775`. Credit **Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors of their
text**, for their material. No numerical proof is used.

**OPEN, current checkpoint.** The fixed-fiber implementation fails
by the hand argument below. Unrestricted (CF) is still open. The
primary-source results checked so far do not certify the claimed
fixed-beta Q₈ perimeter lower bound or torus failure of (V).

The target is row 778 (CF), with its uniform density bounds (12) and
`N >= c a^2`, for the actual Wilson pair `(m,m+v_ri)`. The consumer
is (V), and hence the weaker (FQ) and (F-h). The definitions and
checked conditional implications of rows 778–780 are reused.

## 1. First decision: what the Q₈ test currently establishes

**OPEN, not a certified counterexample at fixed beta.** The source
statements below do not prove a fixed finite-beta perimeter lower
bound for arbitrarily large Q₈ Wilson loops, or failure of (V) on
the specified periodic tori. This is a conclusion about the checked
statements, not a claim that no such theorem exists in the literature.
The finite-subgroup test remains binding as an unresolved test; it
cannot yet be used here as a proved contradiction to (CF).

### 1.1 The first-order theorem and its quantifiers

**ARGUED literature import; PROVED specialization and limitation.**
The finite-group lead in `prior/gap-lit-flux.md:40–41` was followed
to [Sky Cao, Theorem 1.2.1](https://arxiv.org/html/2001.05627v2#S1.SS2).
It concerns subsequential infinite-volume limits from free boxes.
Its first-order loop formula has an additive error independent of
the loop length. Its hypotheses apply to the defining Q₈
representation. This is not a relative-error perimeter theorem.

Here is the specialization, computed by hand. Write the Wilson
weight in this note as `exp(beta tr(U_p)/2)` and Cao's inverse
coupling as `b = beta/2`. His character gap is `Delta = 2`.
The six elements `±i, ±j, ±k` have character zero; `-1` has
character `-2`. Consequently

\[
 r_b=6e^{-6\beta}+e^{-12\beta},\qquad
 A_b=-\frac{e^{-12\beta}}{6e^{-6\beta}+e^{-12\beta}}I_2,
 \qquad \|A_b\|<1.
 \tag{17}
\]

The sum of the six noncentral representation matrices vanishes by
pairing `g` with `-g`. This proves (17), without enumeration.
With

\[
 c_b=\min\{0.15,\ 2^{-19}\log\|A_b\|^{-1},\ 1-\|A_b\|\},
 \quad
 E_\beta=(2e+2)e^{-\beta c_b/(3+2c_b)},
\]

the normalized character `w_gamma = tr(U_gamma)/2` obeys the
imported estimate

\[
 \left|\langle w_\gamma\rangle_
       {\beta}
 -e^{-|\gamma|(6e^{-6\beta}+2e^{-12\beta})}\right|
 \le E_\beta,
 \qquad \beta\ge1000+14\log8.
 \tag{18}
\]

At fixed finite beta, the proposed leading term tends to zero
as `|gamma|` increases, while `E_beta` stays positive. Its lower
bound therefore becomes negative. Even an expectation identically
zero for all sufficiently large loops would satisfy that part of
(18). Thus (18) does **not** exclude an eventual area law at fixed
beta. The perimeter upper bound in Cao's Corollary 4.2.14 does not
exclude one either. No assertion about interchanging the beta and
size limits is imported.

**ARGUED literature import; insufficient consumer.**
[Adhikari and Cao, Theorem 1.1](https://arxiv.org/html/2202.10375v2#S1)
proves exponential decay of correlations of local observables at
weak coupling for finite groups in free boxes. Neither a Wilson
perimeter lower bound nor comparison of periodic twist normalizers
is its conclusion. A mass gap for local observables is compatible
with a deconfined finite-group gauge theory; it does not decide the
center-flux observable here.

**ARGUED older source; no missing conclusion silently imported.**
[P. Vecsernyés, *Lattice gauge theories in terms of knots*,
printed pp. 271–273](https://www.kfki.hu/elftterm/dgt.pdf), reports
a convergent weak-coupling knot expansion for arbitrary finite
groups with positive character action and positive character gap.
The displayed conclusions are analyticity and exponential
clustering. The subsequent discussion of free-charge phases does
not state the needed all-size Wilson lower bound or twisted-torus
estimate. I read those printed pages in the scan, not its garbled
or absent text layer. The related Szlachányi–Vecsernyés 1989 paper,
DOI `10.1063/1.528218`, was identified but its full text was not
obtained; its proof is not claimed as read.

The [Borgs 1988 abstract](https://link.springer.com/article/10.1007/BF01225259)
announces a perimeter-law freezing region for a continuous-time
theory. Its full theorem was not obtained; the Euclid archive
returned an additional-security-check page. It is not imported
as a theorem about this isotropic four-dimensional Wilson measure.

### 1.2 Reused zero-temperature result

**PROVED in prior work; credited, not repeated.**
`gap-kappa-order.md` gives the counts of Q₈ holonomy quadruples
with prescribed central commutators:

\[
 N_0=736,\qquad N_k=96\ (\operatorname{rank}k=2),\qquad
 N_k=0\ (\operatorname{rank}k=4).
 \tag{19}
\]

Its proof uses `Q₈/{±1} = F₂²`: the commutator matrix is a
symplectic Gram matrix of rank at most two. In particular the
twist `k_* = v_12 + v_34` has no flat connection. At every fixed
finite lattice size, the normalized finite sums therefore give

\[
 \lim_{\beta\to\infty}\frac{Z^{v_{34}}}{Z^0}=\frac3{23},
 \qquad
 \lim_{\beta\to\infty}\frac{Z^{k_*}}{Z^{v_{34}}}=0.
 \tag{20}
\]

These limits do not take size to infinity at fixed beta.

### 1.3 An area-sized classical obstruction, and why it stops short

**PROVED, new quantitative consequence of the prior obstruction.**
Let `G = Q₈`, let `n = (a,a,c,d)` with `c,d in {a,2a}`, and
use a closed center cocycle `eta` of class `k_*`. Call a plaquette
bad when `eta_p U_p != 1`. Every configuration has at least `a²`
bad plaquettes.

For each lattice vertex `y`, form the union `S_y` of the six
coordinate two-tori through `y`. If none of their plaquettes is
bad, the four coordinate-circle holonomies based at `y` have
central pairwise commutators with matrix `k_*`. To see this, cut
each coordinate torus to its rectangle; cancel interior edges in
the plaquette product. Each curvature is central, so its transport
does not affect the product. The remaining boundary word is the
commutator of the two circle holonomies, and the product of `eta`
on that torus is `(-1)^{k_{mu nu}}`. This contradicts (19).

Hence every `y` is incident in this sense to at least one bad
plaquette. A fixed plaquette of orientation `mu nu` belongs to
exactly `n_mu n_nu` of the sets `S_y`, at most `cd`. Counting
these incidences gives

\[
 a^2cd\le\sum_{p\,\mathrm{bad}}n_{\mu(p)}n_{\nu(p)}
       \le cd\,\#\{p:\ p\mathrm{\ bad}\}.
 \tag{21}
\]

For Q₈, each bad plaquette costs at least one in
`sum_p(1 - tr(eta_p U_p)/2)`. Thus the minimum action deficit
in the rank-four sector is at least `a²`.

**PROVED limitation of the elementary partition-sum bound.**
Put `V_lat = a²cd`, with `4 V_lat` unoriented links and
`6 V_lat` unoriented plaquettes. Gauge fixing a spanning tree
shows that a flat sector has `8^(V_lat-1) N_k` link assignments:
the tree gauge transformation is fixed to be one at the root,
and the remaining flat connection is determined by its four
holonomies. All link assignments have counting-Haar mass
`8^(-4 V_lat)`. Using (21) in the numerator and just the flat
assignments in the denominator proves

\[
 \frac{Z^{k_*}}{Z^{v_{34}}}
 \le \frac{8^{3V_{\rm lat}+1}}{96}\,e^{-\beta a^2}.
 \tag{22}
\]

The right-hand side grows rather than decays as `a -> infinity`
at fixed beta. The uncancelled entropy is of order the volume,
not the area. Obtaining a bound `C a^p exp(-tau a²)` with
`tau > 0` for this ratio at one fixed finite beta would require
a normalized defect estimate, not (21) alone. In frame 1 the
pair is precisely `(m,m+v_12)` with spatial `m=v_34`, so that
such an estimate would directly refute (V). That finite-temperature
step is **OPEN** here.

**PROVED group distinction, not a proof of a phase.** The same
counting proof of (21) works for any finite subgroup of SU(2)
containing `-1`. Indeed, two SU(2) matrices with commutator `-1`
anticommute. In quaternion coordinates they are pure imaginary
unit quaternions on orthogonal axes. Their common centralizer is
`{±1}`. Two further holonomies commuting with both cannot
anticommute with each other. Thus the required rank-four
commutator matrix is impossible. For finite `G`, the action gap

\[
 \Delta_G=\min_{g\ne1}\left(1-\tfrac12\operatorname{tr}g\right)>0
\]

turns (21) into energy at least `Delta_G a²`. For SU(2) this
infimum is zero. The discrete energy argument consequently
does not transfer to SU(2). Conversely, mere continuity does
not supply the missing free-energy comparison for SU(2).

## 2. A fixed-exterior implementation of (CF) is false in SU(2)

**PROVED, quantitative obstruction for an actual twisted pair.**
This strengthens the exact identity (15) of row 778; it does not
claim that its general warning was new. Keep exactly the selected
link pairs of that row's Section 5: all selected links have
direction 1 or 2. Write `xi` for every unselected link. Consider
the pair `(0,v_34)`, with time direction 3 and spatial direction 4.
Choose the usual representative of `v_34` supported on

\[
 \Sigma=\{p_{34}(x):x_3=x_4=0\},\qquad |\Sigma|=a^2.
\]

No plaquette in `Sigma` meets a selected link. Set

\[
 H(\xi)=\sum_{p\in\Sigma}\tfrac12\operatorname{tr}U_p(\xi),
 \quad B_k(\xi)=C_k(\xi)\prod_x z_{k,x}(\xi),
\]

using row 778's exact unnormalized conditional masses. The only
changed Wilson factors depend on `xi`. Hence, for every exterior,

\[
 f_{v_{34},x}=f_{0,x},\quad z_{v_{34},x}=z_{0,x},\quad
 \frac{B_{v_{34}}(\xi)}{B_0(\xi)}=e^{-2\beta H(\xi)}.
 \tag{23}
\]

In particular all conditional commutator laws, including their
product density, are identical in the two measures. At the
identity exterior `H=a²`. Continuity gives an open set of
positive product-Haar measure on which `H>a²/2`. All Wilson
weights are strictly positive on this set. There,

\[
 \frac{B_{v_{34}}(\xi)}{B_0(\xi)}<e^{-\beta a^2}.
 \tag{24}
\]

Suppose a fiberwise version of (CF) retained this same `xi`,
matched the two masses `B_k(xi)` before integrating over `xi`,
and used a common nonnegative factor and a density satisfying
row 778's (12), with `N >= c a²`. Then (13), on every fiber
where the mass is nonzero, would require

\[
 \left|B_{v_{34}}(\xi)/B_0(\xi)-1\right|\le\varepsilon_N.
 \tag{25}
\]

Fix any compact `I=[beta_-,beta_+]` inside `(0,infinity)`.
Uniformly on `I`, `epsilon_N -> 0`, whereas (24) makes the
left side of (25) at least `1-exp(-beta_- a²)` on that open
set. For sufficiently large `a` this is a contradiction. It
cannot be removed by discarding a Haar-null set.

**PROVED scope; OPEN global comparison.** It rules out the common-normalizer
construction that preserves these fibers and matches their
conditional masses. It applies at fixed beta, in the actual SU(2)
measure, and in one of the required frames. Therefore this one
fixed selection cannot supply an all-frame proof by a pointwise
exterior comparison. A different selection for each frame,
a transformation mixing exterior fibers, or a genuinely global
comparison is not excluded. The small measure of the displayed
open set is irrelevant to a pointwise assertion, but is crucial
to any attempt to infer a global partition-function obstruction.
No such inference is made.

**OPEN after the failed route.** For this choice of selection,
integrating (23) gives the exact remaining comparison

\[
 \frac{Z^{v_{34}}}{Z^0}
 =\mathbb E_{B_0d\xi/Z^0}\!\left[e^{-2\beta H(\xi)}\right].
 \tag{26}
\]

The commutator product integrates to one and does not estimate
this exterior expectation. Showing it is `1-O(a^p e^{-sigma a²})`
requires cancellation after weighting by the actual `B_0`.
Replacing that weight by Haar, or deleting its normalizers,
would change the question.

## 3. How much weaker than (V) is unrestricted (CF)?

**PROVED, existence equivalence for the density-only formulation.**
Read (CF) literally as requiring common nonnegative factors and
a density with (12), without requiring that those factors arise
from a specified Wilson change of variables. As row 780 notes,
this formulation only imposes the displayed density bounds.
On the requested shapes and beta interval, it is equivalent,
up to constants in the area exponent, to (V).

The implication from (CF) to (V) is already proved in row 778.
For the converse assume

\[
 D(a,\beta)\le C a^p e^{-\sigma a^2},\qquad \beta\in I.
 \tag{27}
\]

Fix any actual pair `(m,m+v_ri)` and put

\[
 R=Z^{m+v_{ri}}/Z^m,\quad q=(1-R)/2,\quad
 d=(1-R)/(1+R)=q/(1-q).
\]

By row 778's (1)–(2), `0<R<=1`, `q<=D/2`, and `d<=D` once
`D<=1`. Let `mu` be its Haar-commutator law on SU(2), and let
`w_N` be the Haar density of `mu^{*N}`, with `N>=2`. Its bounds
are a special case of (12), for the same `delta=exp(-24 beta_+)`.
For `h(g)=tr(g)/2`, the already proved dimension-two coefficient
of the commutator law gives

\[
 |h|\le1,\quad h(-g)=-h(g),\quad
 \int h(g)w_N(g)\,dg=4^{-N}=:u_N.
 \tag{28}
\]

Choose

\[
 N=\left\lfloor\frac{\sigma a^2}{2\log4}\right\rfloor.
\]

For sufficiently large `a`, this is at least two and at least
`sigma a²/(4 log 4)`. Also
`u_N >= exp(-sigma a²/2) >= C a^p exp(-sigma a²) >= d`.
Thus `t=d/u_N` belongs to `[0,1]`. On a one-point exterior
space define

\[
 F(g)=1+t h(g)\ge0,\qquad
 \lambda=\frac{Z^m}{1+d}.
\]

Then, exactly,

\[
 \lambda\int F(g)w_N(g)\,dg=Z^m,\qquad
 \lambda\int F(-g)w_N(g)\,dg
 =Z^m\frac{1-d}{1+d}=Z^{m+v_{ri}}.
 \tag{29}
\]

The same choice of `N` works in every frame and for every pair.
This proves the converse. No numerical integration is used.

**OPEN, and the reason this is not a supplier.** The construction
uses the unknown ratio `R` in `F` and the unknown normalizer
`Z^m` in `lambda`. It is circular as a method of proving (V).
It says that disproving the unrestricted existence statement
would also disprove (V); the fixed-fiber counterexample in
Section 2 does neither. If (CF) is strengthened to require
the actual conditional laws of a prescribed Wilson construction,
only its forward implication is asserted here.

## 4. The full density mechanism also survives in a finite subgroup

**PROVED, a stronger limitation on the proposed discrimination.**
Full-Haar minorization, as well as the odd contraction, is available
after a bounded number of commutators in a finite perfect group.
Here perfect means that its commutators generate the whole group.
Let `G` be such a group of order `M`, and let `mu_G` be its
Haar-commutator law. The same two applications of Schur averaging
used in row 778 give, for every irreducible representation `rho`,

\[
 \widehat\mu_G(\rho)=d_\rho^{-2}I.
\]

A nontrivial one-dimensional representation would factor through
the trivial abelianization, so all nontrivial `d_rho` are at least
two. Finite-group Fourier inversion and `|chi_rho|<=d_rho` give
the following bound for the Haar density `w_L` of `mu_G^{*L}`:

\[
 |w_L(g)-1|
 \le\sum_{\rho\ne1}d_\rho^{2-2L}
 \le(M-1)4^{-L}.
 \tag{30}
\]

The last inequality uses `sum_rho d_rho²=M`. Choose a fixed
integer `L` making the right side at most `1/2`. Now suppose
the independent, possibly noncentral conditional commutator laws
satisfy `delta mu_G <= nu_j <= delta^{-1} mu_G`, exactly the
finite-energy hypothesis used in row 778. Each block of `L`
convolutions has density between `delta^L/2` and
`3 delta^{-L}/2`. In particular each block has a Haar component
of mass `eta=delta^L/2`.

For a central involution `z`, the odd part of a density remains
odd under convolution. Convolution by a block contracts its
supremum norm by at most `1-eta`, since its Haar part kills that
odd function. After the first block the odd difference is at
most `3 delta^{-L}`. Subsequent convolution preserves the
lower density bound. Thus, for `N>=L`, the product density `v_N`
satisfies the entirely pointwise inequalities

\[
 v_N(g)\ge\delta^L/2,\qquad
 \left|\frac{v_N(zg)}{v_N(g)}-1\right|
 \le6\delta^{-2L}
       (1-\delta^L/2)^{\lfloor N/L\rfloor-1}.
 \tag{31}
\]

Any remaining fewer-than-`L` convolutions are norm contractions.
This proves (31) for all `N`, not just multiples of `L`. A
change of variable `g -> zg` gives the same arbitrary
nonnegative-endpoint comparison as row 778's (13).

**PROVED application, with a named group identification.**
The binary icosahedral subgroup is `SL(2,F_5)`; for this standard
identification see [Darrin D. Frey and Tom Rudelius,
equation (1.1)](https://arxiv.org/html/1811.04921v2#S1).
Its order is `24*5=120`: there are 24 possible nonzero first
columns, and five second columns of determinant one for each.
Its perfectness can be checked without a character table.
Write `u(t)` and `l(t)` for the upper and lower elementary
unipotent matrices and set `a=diag(2,3)` over `F_5`. Direct
matrix multiplication gives

\[
 [a,u(t)]=u(3t),\qquad [a,l(t)]=l(3t).
\]

Since three is invertible, every elementary unipotent is a
commutator. These matrices generate `SL(2,F_5)`: row elimination
reduces any determinant-one matrix to a diagonal one, row swaps
are products of unipotents, and explicitly

\[
 u(r)l(-r^{-1})u(r)=
 \begin{pmatrix}0&r\\-r^{-1}&0\end{pmatrix}=:b(r),\qquad
 b(r)b(-1)=\operatorname{diag}(r,r^{-1}).
\]

Thus the group is perfect. In (30), `L=4` suffices because
`119/256<1/2`. For its defining SU(2) Wilson action the same
selected-pair finite-energy argument has
`delta=exp(-24 beta_+)`. Hence (31) yields exponential
center flattening in `N` at every fixed finite beta interval,
including weak coupling. All factors and normalization bounds
in this argument are hand inequalities.

**PROVED shared input; OPEN phase implication.** Q₈'s lack of full-Haar support is not
an adequate escape from the finite-subgroup test: a binary
polyhedral subgroup has the stronger full-density mechanism too.
This proves no weak-coupling phase theorem for that group.
To meet the requested finite-subgroup test, a proof must distinguish
the common-normalizer step, beyond even the strengthened local
flattening input (31). Calling this a proved finite-group
counterexample would additionally require its missing phase theorem.

## 5. Binding tests and remaining decision

**PROVED U(1) discrimination of the available positive mechanism.**
The valid test in `gap-crux-fp.md` Section 3b.3 concerns a purported
all-coupling conclusion when the same proof hypotheses hold in
U(1). Here `[A,B]=1` in U(1), even under non-Haar conditioning.
Commutator convolution is the identity on a nonzero center-odd
function, such as `g -> g`. It has no strict odd contraction,
no Haar density after convolution, and no version of (28) with
`u_N=4^{-N}`. Thus the positive commutator input really does fail
there. This does not establish (CF) for SU(2), and the elementary
fixed-fiber refutation is not itself a nonabelian confinement
mechanism.

**PROVED limits of the finite-group discrimination.** A strict
odd commutator contraction alone does not distinguish SU(2)
from the subgroups in row 780. Nor can a conclusion about fixed
finite beta be rejected merely using (20). For Q₈ specifically,
the commutator law is supported on `{±1}`, so the SU(2) proof's
full-Haar lower density bound cannot literally be transferred to
Q₈. This support observation does not settle center-odd mixing
on its support; Section 4 proves that it does not distinguish
the binary icosahedral case. Neither observation certifies a
finite-beta failure of (V).

**OPEN after three distinct routes.**

1. The finite-group defect route gives an area-sized *energy*
   obstruction, (21), but its elementary normalized estimate
   (22) loses volume entropy. Missing: a fixed-beta, periodic,
   twist-sensitive contour estimate. The checked literature
   formulas do not supply it.
2. The direct Wilson conditional route fails in the fixed-fiber
   form by (23)–(25). Missing: an estimate of the actual exterior
   average (26), or a justified transformation of its weighted
   fibers for every magnetic background and frame.
3. The unrestricted-factorization route is equivalent to the
   target by (27)–(29). It does not weaken the quantitative task.
   Missing: construction of the common factors from the Wilson
   action without inserting the already unknown twist ratios.

**GUIDE for the next decision.** Control the weighted exterior
comparison, with a quantitative use of SU(2) beyond the shared
contraction and density flattening. Rephrasing it as another
existence statement, or replacing the finite-temperature subgroup test by a
zero-temperature count, would not be progress.

No computer-assisted step discharges any claim above. No numeric
run or machine enumeration was made. Only this research note was
written; queues, audit records and status files were not changed.
The new hand arguments have not had an independent check.
Work is local and uncommitted on `research/gap-cf-astra-cbfbf26f0`.

RESULT: OPEN — unrestricted (CF), (V), (FQ) and order-one (F-h) remain unproved; the fixed-exterior implementation is refuted by an actual SU(2) twisted pair, density-only (CF) is equivalent to (V), and a fixed-beta Q₈ perimeter/torus obstruction is not certified by the primary statements checked here.
