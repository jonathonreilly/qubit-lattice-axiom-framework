# Repo search

Written by OpenAI Codex, gpt-6-astra, xhigh, 2026-11-17. Check of
row 1103 at `0bdd62338c0b16241714e7de6001172ef6c99153`. Research text,
not an audit; grants no status. Only this output file is edited.

The task-specific prior note does not exist at this revision. The lead's
`prior/repo-search-2026-11-08.md` predates this exercise. Its general
soft-route and hard-route snapshot hits are retrieval leads, not proofs of
C6, C7, C14, C15 or the mixed-only corner. The targeted comparisons below
are complete. The other check of row 1103 was not read.

No run discharges a statement. The two requested sources were fetched once
each into the new scratch directory
`/tmp/sa-gap-face-exercise-check-astra.o8DSTr/`.
The outline and CA-I are pinned at Sussman--Alpoge commit `31a47c543775`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, for the source constructions and arguments used below.

## Repository comparison

The six fetched heads were: main `8b11ae2bb95e`, PR10114 `f76f6c649cff`,
PR10133 `89faef229ff6`, PR10134 `1e70c7211a2c`, PR10141 `a2f6a430e251`,
and PR10144 `1f20846b8057`. Text snapshots were searched outside this
hard-route folder; no history search was used. Identical blobs were read
once. The requested other check was excluded before content extraction.

| Hit checked in its current source | Closeness and use |
|---|---|
| Lead digest's `S/MASS_GAP_LOCAL_BLOCK_ASTRA.md`, PR10114/10133, L106-149 | Already gives `r_f=I_2/I_1` and a simple b-edge loop eigenvalue `r_f^b`. This is a C4 ingredient, credited to that earlier Codex construction. Its positive one-step witness is not C4's whole-sector upper bound or a classification of faces. |
| main `docs/FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md`, L82-92 | Already gives the four-torus real curl rank `3V-3` by Fourier modes. Reuse that prior count; C7 needs its characteristic-two cellular version, checked below. This is not a prior proof of the full independent-plaquette obstruction. |
| main `docs/GL_F_MULTILOOP_GRADED_NET_COCYCLE_NARROW_NO_GO_NOTE_2026-06-10.md`, L177-191 | Plaquette generation in a three-dimensional free block; the passage uses finite rank certificates. Different dimension and no C15 product-space basis theorem. No certificate is used here. |
| main `docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md`, L2553-2567 | “Mixed-only” refers to electric/magnetic sign averaging in a clock model, not the corner `(0,beta,0)`. |

`S/` means `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
Targeted searches found no outside-lane C6/C14 classification, C15 theorem,
or mixed-only SU(2) corner supplier. Search terms included forest faces,
leaf lemma, 2-core, stiff faces, frozen orientations, closed mixed surfaces,
principal chiral, product of graphs, four-cycle corner/face, and the lane's
coupling notation. The latter was also searched separately on YM4D and
mass-gap paths. The local registry, open-core and l17c searches found no
competing owner of this check. These are bounded search findings, not an
absence theorem. Full inventories, queries' hit files and the ref map are
in the scratch directory above.

The SA index locates relevant prior machinery, not these classifications:
outline chunk 01 L116-143, chunk 02 L84-96, obligations L37-51;
CA-full rows for `4.6:lem-rooted-tree-majorant` and
`4.6:prop-logarithm-convergence`; CA-4.12-4.19 chunk 01's axial-gauge rows.
Source reads: outline L238-294, L1150-1374, L2195-2231; CA-I
L22172-22243, L22645-22730, L43765-43880. The account's small-curvature
axial-gauge lemma is related but not a full-support theorem for partially
frozen Wilson laws. The abstract KP convergence theorem is already proved
there; it is not an open lemma for this lane to rebuild.

## Verdicts

| Statement | Verdict | Exact scope or first failure |
|---|---|---|
| C1 | HOLDS | Haar chain substitution |
| C2 | HOLDS | Including periodic mu and free nu |
| C2' | HOLDS AFTER CORRECTION | Exact factor holds; total-volume bound fails at L325-326 |
| C3 | HOLDS | Free-boundary independent plaquette law |
| C4 | HOLDS AFTER CORRECTION | General f and short periodic cycles invalidate L345; use q and the girth |
| C5(a) | HOLDS AFTER CORRECTION | Specify the nontrivial star endpoint, with other couplings zero |
| C6 | HOLDS AFTER CORRECTION | Leaf/core list holds; product-only claim fails at L401; gap conclusions are overbroad |
| C7 | HOLDS | The stated mod-2-acyclic rank bound, not a classification of all solvable laws |
| C14 | FAILS | Unsupported variance step at L1036-1037; false unconditional exclusion at L1029-1031 |
| C15 | HOLDS | Finite-support F_2 chains on Z^2 x Z^2 |
| Coupling conversion | HOLDS | Both cited papers' conventions give beta_here=4 beta_theirs |
| N1a ranges | HOLDS | Published ranges and their stated observable/boundary scope; proofs not discharged |
| F4-KP reduction | FAILS | Missing SU(2) terms and hypotheses at L1248-1259; first wrong identification L1060 |

All source line references below refer to the pinned fable note unless
another file is named. “HOLDS” records this mathematical check only.

## C1, C2, C3: HOLDS

Source: `gap-face-exercise-fable.md` L281-313, L329-339. Assume the
normalizing integral of Psi is positive, as required to define the law.
C1 is triangular Haar substitution. In its order,
`h_0 ... h_(t-1) = V_0 V_t^{-1}`. Schur's lemma then gives its matrix
expectation, including the stated order of multiplication.

For C2, label a ladder by a positively oriented mu-link in the transverse
slice. Even when mu is periodic, these labels partition the mu-links.
The variables `a_k,b_k` belong to U', so they may be shared between ladders
without compromising a conditional change of variables. The inverse map is

\[
M_{k+1}=b_k^{-1}P_k^{-1}M_ka_k.
\]

There is no last-to-first equation because nu is free. Thus each ladder
has one Haar variable M_0 and one independently variable P_k per square.
This remains true if the mu direction has only one periodic link: then
`a_k=b_k`, but the inverse formula is still valid. The resulting product
measure proves both C2 conclusions. The unused top-level a,b in the source's
index range are harmless; they are needed only for k<L_nu.

C3 follows by successively deleting direction leaves. This proves
independence of the specified plaquette transports, not of every link or
every arbitrary Wilson loop. It is a free-boundary statement.

## C2': HOLDS AFTER CORRECTION

The exact ladder factor at L315-322 holds for Wilson weights, including
unequal plaquette couplings. Its second character is initially
`chi_j(B^{-1})`; SU(2) makes this `chi_j(B)`. No factor of `2j+1` remains.
One may also prove it by taking the trace of the product of the central
convolution operators and the two holonomy translations. This checks the
normalization independently of the written character contractions.

The first incorrect bound is L325-326: a lower bound on all side lengths
does not give an upper bound L^3 on the number of ladders. Correct text:

> For homogeneous Wilson weight at fixed finite beta, put
> `delta_L=sum_(j>0) (2j+1)^2 c_j(beta)^L`. For N ladders their product
> differs pointwise from 1 by at most `(1+delta_L)^N-1`. Moreover
> `delta_L=4 c_(1/2)^L(1+o(1))`; hence `delta_L<=5 c_(1/2)^L` for
> sufficiently large L, depending on beta. The total correction tends to
> zero when `N c_(1/2)^L -> 0`, in particular for cubes. Arbitrarily large
> transverse sides are not covered by that total-error argument.

To see the missing quantifier directly, set all exterior holonomies to 1.
Every ladder factor is `1+delta_L>1`; choose N growing faster than
`c_(1/2)^(-L)`. All four sides can still be at least L. The factorial
coefficient decay makes the displayed asymptotic summable. For generic
continuous class weights, the series also needs a convergence convention;
two or more factors give absolute convergence by Peter--Weyl Parseval and
Cauchy--Schwarz. Wilson weights have absolute convergence for every L.

## C4: HOLDS AFTER CORRECTION

The degree-one argument at L356-361 is correct, interpreted as a statement
about Peter--Weyl sectors. Projection onto a fixed assignment of edge
representations commutes with vertex gauge averaging. At a vertex with
exactly one nontrivial incident representation the average is zero.
Orthogonality to constants removes the all-trivial assignment. Every
surviving support therefore contains a cycle.

Two hypotheses are missing from the stated bound at L345:

1. A general positive continuous class weight need not satisfy
   `|c_j|<=c_(1/2)`. Let `f=1+epsilon chi_1`, with `0<epsilon<1`.
   It is strictly positive since `chi_1` ranges from -1 to 3. But
   `c_(1/2)=0`, `c_1=epsilon/3`. The adjoint character of one spatial
   plaquette has Haar mean zero and norm one, and covariance
   `(epsilon/3)^(4T)>0`. This contradicts the stated zero upper bound.
2. A spatial torus can have cycles shorter than four. On a side of length
   three, the fundamental character of the winding three-link loop has
   covariance `c_(1/2)^(3T)`, violating the claimed `c_(1/2)^(4T)` for a
   Wilson weight with beta>0. Multiedges and self-loops similarly matter
   at lengths two and one.

Correct text:

> With free time boundary and a spatial graph of girth g, the displayed
> estimate holds with `q^(gT)`, where `q=sup_(j>0)|c_j(f)|<1`.
> For a Wilson weight and free spatial boundary, or periodic spatial
> sides at least four, `q=c_(1/2)` and g=4 when a square is present.
> Disjoint spatial projections use independent chains and have zero
> covariance. These conclusions concern the free-time law; they alone do
> not establish T's uniform periodic-box assertion.

Here `q<1` follows without a sign hypothesis: if `m=min f>0`, write the
Markov kernel as m times Haar averaging plus `(1-m)` times another Markov
kernel. On mean-zero functions its norm is at most `1-m`.

For Wilson weights the coefficient formula is already proved by Sussman
and Alpoge, with Claude and Codex, outline L2195-2231 (GL3). After division
by the trivial coefficient it is exactly D2. The remaining ordering has
this short hand check. For integer n>=0 use

\[
I_n(b)=\frac{(b/2)^n}{\sqrt\pi\,\Gamma(n+1/2)}
\int_{-1}^1 e^{bt}(1-t^2)^{n-1/2}\,dt.
\]

Expanding the exponential, discarding odd powers, and integrating the
even powers by the beta integral recovers the Bessel series in GL3.
Integration of the derivative of `e^(bt)(1-t^2)^(n+1/2)` gives
`I_(n+1)/I_n=E_n[t]`, where E_n uses the positive integrand above.
Symmetry and b>0 give `0<E_n[t]<1`. Thus `I_1>I_2>I_3>...>0`.
Conditional expectation onto the two boundary time slices is an L2
contraction. Applying the sector bound to their covariance proves the
corrected estimate. No decimal approximation enters this check.

## C5(a): HOLDS AFTER CORRECTION specifying the star endpoint

Source L367-370. Set the other three plane couplings to zero, as on that
star face. In temporal gauge, the limiting increments are identically 1.
The spatial links on the initial slice remain independent Haar, and every
slice is the same. For a spatial plaquette take `A=chi_(1/2)(U_p)/2`.
Its mean is zero and its variance is 1/4 by Haar orthogonality. Therefore
the covariance is exactly 1/4 at every allowed time separation, on
arbitrarily long free-time boxes. This is a nonconstant witness, not a
statement that every A has positive variance. It does not say that the
fully flat six-plane theory has a nontrivial zero mode: that theory's local
gauge-invariant observables are constant on a free box.

## C6: HOLDS AFTER CORRECTION

The leaf integrations and five possible residual cores at L392-408 hold
with free boundary: empty, triangle, four-cycle, diamond (`K_4-e`), and
`K_4`. Stars number four and labelled paths number `4!/2=12`.

The four-cycle row's statement that its closed surfaces *are products* is
false at L401. Choose adjacent squares P_1,P_2 in A and adjacent squares
Q_1,Q_2 in B. The two shells
`partial P_1 x partial Q_1` and `partial P_2 x partial Q_2` share exactly
one mixed plaquette. Their mod-2 sum is a connected 30-plaquette closed
surface. A product of two finite square-lattice loops has area divisible
by four. Thus this surface is not one product. C15 supplies the correct
description as **finite sums** of products.

Replace the conclusions following the table by:

> Forests are exactly the orientation graphs completely eliminated by
> C2. Their free-boundary plaquette law is a product. C4 proves the stated
> star estimate on its corrected domain. C3 alone is not a proof of the
> uniform periodic-box T-analog for every forest. The other four cores are
> the residual cases of this elimination method; the table proves no
> no-go statement for their gaps. In particular, a triangle sub-face of
> `K_4-e` gives no implication from a gap at positive added couplings to a
> gap after those couplings are removed.

“The proved corners are exactly the forests” is not a mathematical
classification of gapped models. At small positive couplings even the
cyclic cases lie in the stated strong-coupling regime. At window couplings
it can only describe this exercise's available proofs. No such periodic
gap is newly supplied by this check.

## C7: HOLDS, with its explicit mod-2 premise retained

Source L410-420. The number `3V-3` is correct for the standard cellular
four-torus. This reuses the prior real rank count identified above and
checks the field change rather than importing a Fourier proof over F_2.
The connected 1-skeleton has `rank partial_1=V-1`, hence
`dim Z_1=4V-(V-1)=3V+1`. Modulo plaquette boundaries a closed edge path can
be reordered by swapping neighbouring coordinate steps. Opposite steps
cancel; the remaining class is its four winding parities. The four
coordinate loops realize those parities independently. Thus
`dim H_1(T^4;F_2)=4`, and `rank partial_2=3V-3`.

A set K with no nonempty closed mod-2 subset has independent boundary
columns, proving the bound. A literal periodic spanning-tree face has 3V
plaquettes and therefore does **not** satisfy this premise. Removing seam
plaquettes gives free forest boxes with `3V-O(V/L_min)` plaquettes, which
explains the asymptotic half-density statement. This bound is for the
declared mod-2-acyclic class; it is not a classification of every exactly
solvable SU(2) law. The source's generic character-expansion explanation
must not be used to identify all nonabelian polymers with mod-2 surfaces.

## C15: HOLDS on the stated infinite lattice with finite support

Source L1069-1095. Work over F_2 throughout. Let X and Y be the finite
edge coordinate spaces containing the support of M. Put
`V=ker partial_A intersect X`, `W=ker partial_B intersect Y`. The row
condition gives `M in X tensor W`; the column condition gives
`M in V tensor Y`. Choose finite-dimensional complements of V and W.
The resulting four summands of `X tensor Y` show that their intersection
is exactly `V tensor W`. No completion, infinite matrix product, or
topological tensor product is involved.

Here is a direct check of the claimed planar basis. For a finite cycle z,
let h(i,j) mark its horizontal edge from (i,j) to (i+1,j). Assign the
square with lower left corner (i,j) the coefficient
`t(i,j)=sum_(k<=j) h(i,k)` mod 2. A finite cycle crosses each vertical cut
an even number of times, so t has finite support. Its differences across
horizontal edges equal h. The cycle equation at each vertex then gives
the required differences across vertical edges, starting from zero
outside the support. Thus `partial t=z`. If `partial t=0`, all adjacent
square coefficients agree; finite support makes all of them zero. This
proves both spanning and independence. Tensoring these two bases gives
the asserted unique finite set T of square pairs.

For the area formula, include every unordered adjacent pair P,P' once,
with phi empty outside its finite support. The row on their common edge
is `partial_B(phi(P) triangle phi(P'))`, so summing its edge count gives
exactly the displayed formula. A nonzero column needs at least four rows;
every nonzero row needs at least four entries. Hence `|S|>=16`. At
equality, the four row positions must be one unit-square boundary, and
every nonzero column occupies all four positions. The common row is then
another unit-square boundary. The surface is `partial P x partial Q`,
homeomorphic to `S^1 x S^1`. This product argument, rather than Euler
characteristic alone, establishes that it is a torus.

The domain restriction matters downstream. On periodic A and B, each
cycle space also has its two winding generators, and the sum of all unit
square boundaries is zero. If A and B have v_A and v_B vertices, the
mixed cycle space has dimension `(v_A+1)(v_B+1)`, whereas the span of
hypercube shells has dimension `(v_A-1)(v_B-1)`. C15's uniqueness and
exhaustion by shells therefore cannot be applied to periodic boxes.

## Coupling conversion and N1a: HOLDS as a source-range check

Source L198-201, L222. Both papers use `N beta_theirs Re Tr U_p`, with
unnormalized Tr and one orientation per square. For SU(2) this is
`4 beta_theirs w(U_p)`, so `beta_here=4 beta_theirs`.

Hao Shen, Rongchan Zhu and Xiangchan Zhu, *A stochastic analysis approach to
lattice Yang--Mills at strong coupling*, arXiv:2204.12737v1, p. 4,
Assumption 1.1 and (1.3), give the SU(N) bound
`|beta_theirs|<1/[16(d-1)]`, without an extra N in the denominator.
Thus at d=4 it becomes `beta_here<1/12`. Corollary 1.6, p. 7, concerns
exponential covariance decay for smooth cylinder functions in the
infinite-volume law; Corollary 4.4, p. 19, gives the finite-volume
log-Sobolev inequality. The extra N in the earlier reader's prose is a
transcription error. [Primary paper](https://arxiv.org/pdf/2204.12737v1).

Cao, Nissim and Sheffield, *Dynamical approach to area law for lattice
Yang--Mills*, arXiv:2509.04688v2, p. 2, (1.2), Definition 1.4 and
Theorem 1.6, give `beta_theirs<1/[8(d-1)]` for SU(N). This converts to
`beta_here<1/6`. Their area-law statement is for rectangular loops with
side lengths at most half the torus side. It is not a full local-observable
gap theorem at that larger threshold.
[Primary paper](https://arxiv.org/pdf/2509.04688v2).

The relevant formula pages were visually inspected as well as extracted.
This verifies conventions, ranges and stated scope; it does not check or
discharge either paper's proof. Neither result reaches the window.

## C14: FAILS as an unconditional classification

### (a) The gauge identity holds; the variance argument needs more

Source L1019-1037. On each free mu-line set `g(x,0)=1` and recursively
`g(x,k+1)=g(x,k) U_mu(x,k)`. This sets every mu-link to 1. There is no
periodic holonomy obstruction. Frozen mu-nu and mu-rho plaquettes then
make U_nu and U_rho constant along mu. For the scalar observable
`A=w(U_(nu rho))`, `tau_(t e_mu) A=A` pointwise, whenever both supports
lie in the box. Consequently the covariance is its variance.

The first unsupported proof step is L1036-1037: “Its coupling is finite, so its
law has a density and it is not constant.” Finite remaining couplings
give a strictly positive tilt of the **constrained reference measure**.
They do not establish its density or support. The source never defines
that reference measure for intersecting infinite-coupling constraints,
nor proves that its missing-plane trace is nonconstant. Merely writing
infinity in a Wilson weight is not such a proof. For a reference measure
of full support on the flat locus, nonconstancy can be checked: set all
links to 1 except nu-links chosen in a fixed U(1) subgroup, depending
only on x_rho. Every frozen orientation stays flat, while the unfrozen
nu-rho plaquette trace varies. Positive finite tilting then preserves
positive variance. This is a valid **conditional** repair.

There is a second quantifier problem in “rate 0.” Positive variance in
each finite box need not have a volume-independent positive lower bound.
The finite couplings are summed over all replicated slices. For example,
freeze 12 and 13, keep beta_23=b>0, and set all couplings involving 4 to
zero for this illustration. A free box with n copies in direction 1 and
one 23 square reduces to the single-plaquette density `exp(n b w)`.
Its variance is positive at each n and tends to zero as n grows. This
example is a quantifier warning, not a counterexample to a no-gap theorem
on the all-positive domain. To exclude a **uniform finite-volume**
exponential bound one must estimate how the variance depends on size;
to exclude clustering in a specified infinite-volume state one must show
that the variance survives that limit. Neither follows from positivity
alone. C5(a)'s Haar witness does survive on its star domain.

### (b) The eleven-graph check holds

An induced two-edge path `nu--mu--rho` is exactly the pattern needed for
the pointwise identity in (a). A graph without such a path is a disjoint
union of cliques. The complete list on four direction vertices is:

| Frozen graph F | Edges | Pattern from (a), or exception |
|---|---:|---|
| Four isolated vertices | 0 | no frozen plane |
| One edge and two isolated vertices | 1 | no two-edge path |
| Two disjoint edges | 2 | no two-edge path |
| Two adjacent edges and an isolated vertex | 2 | the displayed path |
| Star `K_(1,3)` | 3 | any two spokes |
| Path `P_4` | 3 | its first two edges |
| Triangle and an isolated vertex | 3 | clique exception |
| Four-cycle | 4 | any two consecutive edges |
| Triangle with a pendant edge | 4 | pendant edge and one incident triangle edge |
| Diamond `K_4-e` | 5 | the missing edge's endpoints and either common neighbour |
| `K_4` | 6 | fully flat exception |

For a frozen triangle, free spatial gauge fixing really does leave
independent three-dimensional SU(2) principal chiral/O(4) layers, with
the remaining three couplings as their three bond strengths. Ordering
alone does not establish power-law decay of invariant observables. The
source correctly marks that step BELIEF at L1026-1028. The decimal
threshold 1.0109 is not established by this check and is not a hand bound
provided in the source; replace it by the precise hypothesis of whichever
ordering theorem is actually imported. With unequal remaining couplings,
one isotropic threshold would not state the required hypothesis anyway.

### (c) The unconditional exclusion is false

The BELIEF from (b) is lost at L1029-1031 and again at L1236-1238. More
decisively, C14 allows *every* positive finite remaining coupling. Freeze
the triangle 12,13,23 and choose the other three couplings to be
`b=1/100`. The resulting independent O(4) layers have a uniform positive
clustering rate. Here is a hand small-coupling check, independent of any
claimed large-coupling O(4) result.

Changing one neighbour changes a one-site conditional log weight by a
function of oscillation at most 4b. Its conditional total-variation
influence is therefore at most `c=exp(4b)-1`. There are at most six
neighbours and

\[
6c \le 6\left(\frac1{1-1/25}-1\right)=\frac14<1.
\]

For completeness, couple the single-site conditional updates maximally
in two copies. At stationarity their disagreement probabilities obey
`d_x <= sum_y c_(xy) d_y + b_x`, with b supported on the changed boundary
or conditioned set. Iteration gives `d <= sum_(k>=0) C^k b` because the
row sum is at most 1/4. An influence reaching distance r needs at least
r nearest-neighbour steps. Its total is bounded by
`sum_(k>=r)(1/4)^k`. Conditioning on the support of a second bounded
observable and using this coupling bounds the covariance by that tail
times the two sup norms and a constant depending only on the supports.
Finite-volume heat-bath laws are strictly positive, so this stationary
coupling exists; the contraction also removes dependence on initial
conditions. Thus the bound is uniform in the free boxes. Independent
layers give zero covariance once the layer supports separate. Restricting
to gauge-invariant functions preserves the bound.

This is a frozen **triangle** with no zero coupling and a positive rate
in all directions, contrary to (c). Also, with all six planes frozen on
a free simply connected box every local gauge-invariant observable is
constant, so the covariance bound is trivially true; this is not a
nontrivial gapped endpoint. Correct replacement for (c):

> The graph list identifies which frozen sets force a missing-plane
> observable to be replicated pointwise. A no-gap conclusion additionally
> needs a nondegenerate specified law and the appropriate variance bound.
> The frozen triangle and fully flat theory remain explicit exceptions.
> No unconditional classification of positive-rate stiff faces follows.

## “F4-KP gives the T-analog at the corner”: FAILS as written

Source L1248-1261. This is a failure of the claimed reduction, not a
counterexample to clustering at the corner. There are three missing
bridges, grouped here because each precedes application of KP.

**The stated mod-2 surfaces do not enumerate the SU(2) expansion.** The
first false identification is already at L1060-1062, before C15. At a
link, the actual condition is that the tensor product of its incident
representations has an invariant vector. Three nontrivial incident
representations are possible: `1/2 tensor 1/2 tensor 1` contains a singlet.
Only the set of **half-integer** labels is necessarily closed mod 2;
the support of all nontrivial labels need not be.

Here is a nonzero term on the mixed-only lattice. Use the two neighbouring
hypercube shells from the C6 counterexample. Their intersection is one
plaquette p. Label p by spin 1 and each of the other 30 faces by spin 1/2.
At each of the four boundary links of p there are three occupied faces,
so this 31-face support is not closed mod 2. Nevertheless its character
integral is nonzero. To check this without enumeration, remove p from
each torus. Each punctured torus has a single boundary holonomy H.
Schur contraction of its two-face internal links leaves
`C chi_(1/2)(H)`, with C a positive power of 1/2. Equivalently, cutting
the punctured torus to a polygon leaves one commutator, and
`integral chi_j(XYX^{-1}Y^{-1}H) dX dY = chi_j(H)/(2j+1)^2`;
successive face contractions supply the other positive dimension factors.
The two punctured surfaces have disjoint internal links. The remaining
four boundary-edge integrations are therefore

\[
C^2\int_{SU(2)}\chi_1(H)\chi_{1/2}(H)^2\,dH
=C^2\int\chi_1(H)(1+\chi_1(H))\,dH=C^2>0.
\]

Wilson coefficients of these labels are positive for beta>0. Thus the
omitted support contributes to the actual partition function. Calling
“closed” a general invariant-labelled, possibly branched support repairs
the object, but then C15 no longer describes all its polymers or their
entropy.

The minimum-size observation can be salvaged separately. No link can
have exactly one incident nontrivial representation. Each nonempty row
and column of the support is consequently a finite square-lattice graph
with no degree-one vertices and hence contains a cycle of at least four
edges. There are at least four nonzero rows, each of size at least four.
So an unmarked nonzero vacuum term still has at least 16 faces in the
infinite lattice. Equality forces the product of two unit-square
boundaries, and the two-face link integrals force one common spin.
This does not restore the proposed enumeration of larger supports.

**The displayed sum uses the wrong footprint for direct KP application.**
In the natural gas obtained by taking link-connected components of the
occupied support, distinct polymers have disjoint link sets. They are
incompatible if they share a link, even without a shared plaquette.
Such pairs occur among product tori: choose two B
square boundaries sharing a vertex but no edge, and two A square
boundaries sharing an edge. The product tori share a link and no face.
F4-KP only bounds polymers containing a given plaquette p. It supplies no
alternative exact gas with incompatibility defined by shared plaquettes.
In the mixed lattice each link lies in at most four mixed plaquettes.
Charging a link-overlap to a face of each polymer gives the estimate

\[
\sum_{\eta\not\sim\gamma}|w(\eta)|e^{a|\eta|}
\le 16a|\gamma|,
\]

from its displayed hypothesis, whereas the KP criterion with
`a_gamma=a|gamma|` needs `a|gamma|`. Neither a matching footprint nor
the stronger inequality is supplied. The existence of the letter a in
F4-KP does not absorb the factor: changing a also changes the exponential
inside its hypothesis.

**The unmarked partition sum does not supply the stated observables and
volumes.** Observable insertions allow open representation supports
ending on their links. Their absolute weights are not estimated by the
given vacuum sum. The statement provides neither these marked bounds
nor the periodic winding terms excluded by C15. Its conclusions concern
all bounded local gauge-invariant observables and arbitrary sufficiently
large periodic boxes; an infinite-lattice unmarked surface count alone
does not give those quantifiers. Nor does it give the numerical rate
near `4(-log c_(1/2))` claimed later in step 8.

A sufficient corrected **conditional** statement is the following. It is
a stronger open input, not a proof that the original F4-KP suffices:

> Construct an exact source-dependent polymer gas for
> `Z_Lambda(s,t)=integral exp(action+sA+tB)`, including every admissible
> labelled support and winding support in each periodic box. Define
> incompatibility by overlap of the full link footprint, and mark source
> dependencies locally. Supply, uniformly on fixed complex source discs
> and over those boxes, a majorant with constants alpha,m>0 satisfying
> `sum_(eta incompatible gamma) sup|w_eta(s,t)|
> exp(alpha |eta| + m length(eta)) <= alpha |gamma|`.
> The rate m=m(beta)>0 is independent of A and B; their source disc radii
> and the covariance prefactor may depend on their supports and sup norms.
> Include in length the bounded joining cost of overlapping footprints,
> so the sum of lengths of a connected source cluster bounds the distance
> between the two observable supports. Require consistent local activities
> under volume exhaustion and the same estimates for the marked roots.
> Then the connected logarithm converges, its mixed source derivative is
> bounded by `C_(A,B) exp(-m dist(supp A,supp B))`, uniformly in volume,
> and its local periodic limits agree.

The implication uses the already available Sussman--Alpoge abstract
polymer theorem (outline L1150-1374; CA-I
`4.6:lem-rooted-tree-majorant`, L22172 ff.). Only connected clusters
depending on both sources survive the mixed derivative of log Z. Their
length pays the distance, and Cauchy's formula on the fixed discs bounds
the two derivatives. This is the appropriate conditional route to T.
Uniqueness among all infinite-volume DLR states would require the
corresponding boundary-condition control; it is not silently inferred
from periodic limits. The exact gas construction and the majorant remain
unproved here.

## Recorded runs and limits of this check

Both scripts and both saved outputs in `runs/gap-face-exercise-fable/`
were read in full. No script was rerun and no new numerical job was run.

* Run 1 enumerates S_3 configurations, but uses `math.exp` and floating
  accumulation. Its recorded deviations agree with the prose. It is a
  numerical diagnostic of the two-rung free and periodic identities,
  not an exact arithmetic proof and not a direct test of periodic mu.
* Run 2's bit operations and rank algorithm concern the F_2 chain complex
  of two free 3-by-3 site grids. Its printed kernel dimension and area
  histogram agree with the prose. Its last three partition sums use
  floating input u, and describe the mod-2 model, not SU(2) intertwiner
  weights. It cannot detect the 31-face term above or periodic windings.

No source, registry, FINISH row, audit record, or other check was edited.
No Balaban theorem was imported. The other row-1103 check was not read.
No mass-gap claim or scientific status is granted. All repairs above are
text in this check only; the source file still needs its author's edits.

## Final checkpoint

All thirteen requested statement checks are recorded above. The original
fable file still matches `0bdd62338` byte for byte. Only this output is
untracked/changed; it is local and uncommitted. The final whitespace check
reported no defect. No proof-validation test suite or numerical run was
executed. Two attempted arXiv HTML URLs returned 404; the cited PDF copies
were fetched and the needed pages inspected instead. The initial per-blob
metadata fetch was stopped and replaced by a successful batched snapshot
fetch; its log is in scratch. These retrieval steps supply no proof.

The next source action is to apply the stated corrections and remove the
unconditional C14 classification and F4-KP implication. The corner gap,
its full labelled-support estimate, periodic winding control and marked
observable estimates remain open. No new attack on those inputs is made.

RESULT: C1, C2, C3, C7, C15, the factor-four conversion and N1a's source ranges HOLD; C2', C4, C5(a) and C6 HOLD AFTER CORRECTION; C14's unconditional classification and the stated F4-KP-to-T reduction FAIL. No mass gap or status is granted.
