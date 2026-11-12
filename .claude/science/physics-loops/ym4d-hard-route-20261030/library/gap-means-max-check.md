# Repo search

The target-specific `prior/gap-rigid-check-astra.md` is absent at the pinned
revision. The lead's `prior/repo-search-2026-11-08.md` concerns older RG
obligations. Its nearby hit, PR 10114's
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`,
was opened: it bounds a one-step plaquette correlation, not crossed sectors
or an even seed. Main's
`docs/THOOFT_1981_DUAL_SUPERCONDUCTOR_CENTER_VORTEX_CONFINEMENT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md:20–32`
expressly supplies vocabulary and bibliography only.
PR 10114's
`.claude/science/toe-ruleset-20261021/agents/ym4d-existence/EXISTENCE.md:3630–3684`
discusses twisted small-volume holonomies, electric flux and the distinction
between vacuum degeneracy and a gap. It supplies no quantitative crossed-sector
criterion or negative surface term.

I refreshed and searched main and PRs 10114, 10133, 10134, 10141 and 10144.
The searches cover tracked Markdown and TeX outside this hard-route folder;
the folder and its registry were searched separately. No earlier quantitative
Theorem R or 92-square construction was found. This is a bounded search,
not a novelty theorem. Full search outputs and revisions are in
`/tmp/gap-rigid-check-Xs5pNE/`. No registry row owns a duplicate of this check.
Rows 745–746 own the wider literature surveys; the search here is targeted.

The closest mathematical predecessors are already explicit inputs:
`gap-flux-exercise.md:477–491,527–539` gives CL1, the exact three-set
classification, X16 and EVL; `gap-crux-restate.md:174–219` gives the deficit
and seed propagation lemmas. They are reused, not claimed here.
Literature comparison and exact search revisions are recorded below.

Codex, task assignment gpt-6-astra / max, FINISH row 744; research check at
`18aeda83ac633fda416183044c2fa34d7205d2d5`; not an audit; grants no status.
Author checked: Claude Fable 5.2 / max, row 737.
Unqualified line numbers below refer to `gap-means-max.md` at that revision.

**Finding:** no checked step breaks Theorem R. Its constants and R4, R5,
R7 hold given the named inputs. Proposition NS needs its explicitly used
one-cycle-at-each-vertex hypothesis added to the opening statement.
The surface S_0 satisfies that hypothesis. Its count and sign have a hand
proof below, independent of the author's enumeration.

**Checkpoint:** the requested statement checks, hand geometry and targeted
prior-work comparison are complete at the source revisions recorded here.
The failed routes were access to the full 1979 paper and the Witten text;
neither is used as a proof source. The remaining source-side action is to
add the vertex-link hypothesis to NS and qualify the older positivity
sentence identified below; those source edits are outside this check.
No mathematical run or enumeration is used. No finite seed at order-one
coupling has been established.

## Verdicts in the requested order

| Statement | Verdict | Scope |
|---|---|---|
| R1(a), lines 168,172 | HOLDS | X16, with factor 1/4 |
| R1(b), lines 170–172 | HOLDS | All four slices; no admissibility assumption needed |
| R2(a),(b), lines 176–187 | HOLDS | Including the strict threshold and subgroup conclusion |
| R3(a),(b), lines 191–202 | HOLDS | Every inequality has the stated direction |
| Theorem R, Step 0 | HOLDS | Three nonnegative deficits telescope |
| Theorem R, Step 1 | HOLDS | The smallness constants hold |
| Theorem R, Step 2 | HOLDS | Spatial permutations act on all 64 sectors; dominance holds |
| Theorem R, Step 3 | HOLDS | Exactly one of the three pair subgroups is selected |
| Theorem R, Step 4 | HOLDS | Seven nonvacuum terms are bounded |
| Theorem R, Step 5 | HOLDS | Three doublings and the exponential bound hold |
| Theorem R, Step 6 | HOLDS | The remaining seed is greater than 2 |
| R4, lines 252–258 | HOLDS | Every sufficiently large integer cube and its periodic limits |
| R5, lines 262–268 | HOLDS | Each of the three seeds supplies ES at larger dyadic sizes |
| R7, lines 270–276 | HOLDS | Both free-energy bounds are upper bounds |
| NS for Euler characteristic 1, lines 74–82 | HOLDS AFTER CORRECTION | Require one cycle in every vertex link, as line 82 already does |
| S_0, lines 88–94 | HOLDS | Hand count: (V,E,F)=(93,184,92); a closed surface |
| NS0, lines 96–98 | HOLDS | The stated A(S_0) has coefficient −2^−183 at order β^92 |

## 1. R1, R2 and R3

**R1(a).** Exchange axes 1 and 2 in the eight-term electric average.
One electric bit remains electric; summing it gives twice its even
projection. The other two become magnetic bits. Thus the coefficient is
2/8=1/4, with four magnetic choices and four electric characters per choice.
These are exactly the sixteen sectors X. This reuses X16.

**R1(b).** CL1 is a Fourier identity for an arbitrary function w on the
six twist bits. The later hypothesis called admissibility in Proposition
CL is not a hypothesis of CL1. It need not hold for finite-time weights.
For w(k)=Z^k(a,a,c,d), the exchange 1↔2 preserves w. After transforming
the fixed bit e_2, it exchanges
(e_3,e_4,m_3,m_4) with (m_4,m_3,e_4,e_3).
Inversion in the two remaining electric bits gives

\[
 G(x)=\frac14\sum_y(-1)^{x_1y_4+x_2y_3+x_3y_2+x_4y_1}G(y).
\]

The common factor 8 in what=8Z cancels. Neither chi_2 nor m_2 changes;
there is no additional phase, even on the slice (1,1). Positivity of
sector traces gives G≥0. Setting x=0 gives sum G=4G(0), and replacing
each sign by + gives G(x)≤G(0), including a slice whose G(0) vanishes.

**R2.** The same calculation gives 0≤p≤1 and sum p=4. Rounding at 1/2
has total error eta≤2Q≤8theta<2/5. Therefore |L| differs from 4 by less
than 1 and equals 4. For x∈L, let n count the negative Fourier signs
on L. The Fourier identity and the rounding error give

\[
 4(1-\eta)\le4p(x)\le4-2n+\eta,
 \qquad 2n\le5\eta<2.
\]

Thus n=0: all signs on L are positive. For x,x'∈L those signs remain
positive at x+x', so 4p(x+x')≥4−eta>2. Hence x+x'∈L.
Also 0∈L. This proves the subgroup and isotropy claims without listing
subsets. Nondegeneracy of B and |L|=4 also give L=L-perp.

**R3.** Write lambda=lambda_0(A), lambda'=lambda_0(2a,c,d).
K(b) gives Delta≥0; R1(b) gives Hp=p. The entire chain is

\[
 4(\lambda')^a
 \ \le\ 4Z_0(a;2a,c,d)
 \ =\ \sum_x Z_x(2a;A)
 \ \le\ \sum_x Z_x(a;A)^2
 \ =\ \lambda^{2a}(1+\epsilon)^2\sum_xp(x)^2.
\]

The second inequality is sum r_i^2≤(sum r_i)^2 for the nonnegative
eigenvalues of (T_{A,m}P_chi)^a; it has no simplicity requirement.
Division by the positive factor on the right gives a **lower** bound
4 exp(−Delta)/(1+eps)^2 on sum p^2. Subtraction from sum p=4 gives
the claimed **upper** bound on Q. No inequality is reversed.

## 2. Theorem R, Steps 0–6

**Step 0.** Expanding 4Delta_1+2Delta_2+Delta_3 cancels both intermediate
energies and gives a(8e(a^3)−e((2a)^3)). Each Delta_i is nonnegative
by K(b) applied to the side being doubled. Spatial axis covariance also
gives symmetry of e, by taking the long-time root of Z.
Consequently Delta_1≤delta/4.

**Step 1.** For u,v≥0,
1−exp(−u)(1+v)^−2≤u+2v. For example split the left side as
(1−exp(−u))+exp(−u)(1−(1+v)^−2).
Therefore theta≤delta/4+2eps≤2.25×10^−7 and eta≤1.8×10^−6.
R2 applies with room to spare.

**Step 2.** Here the permutations are the spatial group S_3, not an
assertion that every spacetime permutation acts by a sector permutation.
Under S_3, e, chi and m all permute by their spatial index. The sign
of a permutation causes no change to Z_2-valued magnetic components.
Changing the summation variable e in F1 proves rho(pi sigma)=rho(sigma)
for every (chi,m), all 64 choices. In the slice with (chi_2,m_2) fixed,
R1(b) bounds its value at any four remaining bits by its value at zero.
This is rho(sigma)≤rho(sigma|2). Conjugating by 2↔3 or 2↔4 proves
the two other dominance inequalities. No slice is omitted.

**Step 3.** A_0 is the inverse image of L under the injective linear map
(c,n)↦(0,c,0,n); hence it is a subgroup. Dominance on the other axis,
then the exchange 3↔4, puts both coordinate pairs of each x∈L in A_0.
Thus 4=|L|≤|A_0|^2. If |A_0|=4, L would contain an entire coordinate
plane and therefore equal it. Spatial exchange would make it equal to
the other coordinate plane too, a contradiction. So |A_0|=2, with
A_0={0,alpha}. The inclusion L⊂A_0×A_0 is an equality by cardinality.
There are exactly three possible nonzero alpha in F_2^2.

**Step 4.** If alpha_w differs from alpha, a nonzero sector in Sigma_w
has at least one coordinate pair alpha_w. Dominance bounds its rho by
a single-coordinate value outside L, hence by eta. Sigma_w has seven
nonzero sectors, so

\[
 S_w(a;a^3)\le\epsilon+7\eta(1+\epsilon)
 \le 0.00001270000126 <0.0000128.
\]

These decimals are exact terminating rational arithmetic, not a run.

**Step 5.** At each doubling B→B', permute the doubled side into time.
The box left after that exchange is exactly B up to spatial order:
its replacement side is the old time a. Lemma W and the trace-square
inequality therefore give W_w(a;B')≤W_w(a;B)^2. Its normalization costs
exp(Delta_i), with the positive sign printed in the source. Iterating
gives the exponent 4Delta_1+2Delta_2+Delta_3=delta and the power 8.
For u=0.0001025,

\[
 S_w(a;(2a)^3)\le e^u-1\le\frac{u}{1-u}<0.000103<\frac1{5041}.
\]

The exponential estimate follows by termwise comparison of its power
series with the geometric series. For the first strict comparison,
0.000103(1−0.0001025)−0.0001025=0.0000004894425>0.
For the last, 5041×0.000103=0.519223<1.

**Step 6.** For alpha_w=alpha the three nonzero elements of L belong
to Sigma_w, and their rho sum is at least 3−eta. Keeping them and the
vacuum gives S_w≥eps+(1+eps)(3−eta)>2. The other two sums are less
than 0.0000128, so the exceptional w, and therefore alpha, is unique.

## 3. R4, R5 and R7

**R4.** Theorem R supplies Corollary EV's seed at N=a. Theorem S-w
and its all-integer enlargement give the printed bound for every L≥2a;
the dyadic recursion alone is not being used to cover odd L.
With q≤0.519223<0.52, the rate exceeds 0.65/a by a hand bound:
log(1/0.52)=log 2−log(26/25)≥56/81−1/25>13/20.
Here log 2=2 sum_{j≥0}(1/3)^(2j+1)/(2j+1) and log(1+x)≤x.
EV-L(d) applies to bounded local functions satisfying its condition (i).
Their fixed supports eventually satisfy its spatial width condition.
The conclusion concerns these periodic limit points, not a new continuum
identification or a proved seed at order-one coupling.

**R5.** Put a=2^(k+1)N and t=a/2, an integer at least 3.
The dyadic part of S-w gives s_k=S_w(t;a^3)≤q^(2^k)/5041.
Inclusion of the even block and time monotonicity give eps≤s_k.
For a spatial side a and its two fixed transverse sides, K and X give

\[
 a(2e(a)-e(2a))
 =a(2\kappa(a)-\kappa(2a))
 \le2a\kappa(a)\le4g_w(t;a).
\]

For each pair of transverse sides this is its own kappa and ell;
there is no identification of ell between different boxes.
Enlarging the first and then the second spatial side using E' with
(t,b,h)=(a/2,a,2a) multiplies g_w by at most 4 each time.
Hence (Delta_1,Delta_2,Delta_3)≤(4,16,64)log(1+s_k), and
delta≤(16+32+64)log(1+s_k)≤112s_k.
The threshold is safe since

\[
 112(4.5\times10^{-6})=0.000504
 <5041\times10^{-7}=0.0005041.
\]

The same proof works for per, full and kappa: each has the positive
direct-sum trace, periodic top eigenvalue and permutation symmetry of W.
It does not assume that magnetic summands have simple joint top a priori;
a sum below 1 excludes extra top copies. Since 0<q<1, such k exist.
The zero-seed limiting case is immediate with all later sums zero.
Thus the asserted existential equivalence with ES holds.

**R7.** For the even operator S and A_t=Tr S^t,
A_2t≤lambda_0^t A_t and lambda_0^t≤A_t. These give
A_t/lambda_0^t−1≤A_t^2/A_2t−1. For the two cube sizes they also give
a e(a^3)≤log Z_ev(a;a^3) and
a e((2a)^3)≥log Z_ev(2a;(2a)^3)−log Z_ev(a;(2a)^3).
Multiply the first by 8 and subtract the second: the displayed upper
bound on delta follows. All four partition functions are positive.

## 4. NS: the needed correction and the hand integral

The opening statement at lines 74–76 permits point contacts between
sheets. Edge incidence two does not imply a single cycle in a vertex
link. Line 82 explicitly adds that condition, and its proof uses it
twice. **Add that condition to Proposition NS for the claimed chi=1
case.** This corrects its stated domain; it does not change S_0 or NS0.

The distinction matters to the value, not just to a proof convention.
Splitting a vertex with r disjoint link cycles into r vertices changes
V by r−1 without changing any plaquette word or Haar integral. Thus the
Euler characteristic relevant to the integral is that of the normalized
surface, not necessarily V−E+F of a complex with point contacts. Merely
allowing such contacts in line 74 does not justify line 76.
No assertion for all singular complexes or other Euler characteristics
is certified by this check.

Here is a tree-gauge check for the corrected chi=1 statement. Choose a
primal spanning tree and gauge its V−1 links to the identity. Successive
Haar substitutions do this with unit normalization. There is a dual
spanning tree disjoint from these links. Indeed a disconnected dual
complement would have a nonempty cut consisting of primal tree edges;
the boundary of the corresponding union of faces has even degree at
each vertex, whereas a forest has no nonempty even-degree subgraph.
Orient each successive child face so the shared link occurs inversely;
this is allowed since tr(U^−1)=tr(U) in SU(2), and a dual tree has no
orientation consistency cycle. Integrate the F−1 dual tree links using

\[
 \int\operatorname{tr}(AU)\operatorname{tr}(U^{-1}B)\,dU
 =\tfrac12\operatorname{tr}(AB).
\]

The number of remaining links is E−(V−1)−(F−1)=2−chi=1.
The resulting one-vertex, one-edge, one-face surface has boundary word
g^2, up to inversion. The alternative gg^−1 identifies a two-sided edge
and gives two vertices in its polygon quotient; forcing one vertex
would violate the one-cycle link condition. Collapsing a tree and
merging faces preserve the closed-surface topology.

For Haar SU(2), write U=x_0 I+i sum_{j=1}^3 x_j sigma_j on the unit
3-sphere. Haar invariance gives integral x_0^2=1/4. Hence
integral tr(U^2)=integral(4x_0^2−2)=−1. This checks the minus sign
without a sampled integral. The result is

\[
 \int\prod_{p\in S}\operatorname{tr}U_p=-2^{-(F-1)},
 \qquad
 \int\prod_{p\in S}x_p=-2^{1-2F}.
\]

The source's identity (3) has the right order and sign too: setting
V=UB turns tr(AUBU) into tr(B^−1 A V^2); integral V^2=−I/2.
Its identity (2) follows from averaging UBU^−1=(tr B)I/2.
All three character integrals in line 80 therefore hold.

## 5. S_0: a count from pieces, without enumeration

Use the source coordinates, and suppress t until the final gluing.
Put P=boundary R minus the open edge b. It is a simple path of nine
edges and ten vertices from (1,0) to (2,0).
Write L_+=(1,0,1), L_-=(1,0,−1), R_+=(2,0,1), R_-=(2,0,−1).

**The band M.** The wall D=P×[−1,1] is a rectangular disc with a 9×2
grid. Thus (V,E,F)=(30,47,18), and its boundary length is 22.
The other six squares form a disc B: start with the 1×2 floor rectangle
(V,E,F)=(6,7,2) and attach its four wings along distinct boundary
edges. Each adds (2,3,1); wings meeting at a floor vertex create no
additional identification. Thus B has (14,19,6) and boundary length 14.

D and B meet exactly in the two vertical paths at (x,y)=(1,0),(2,0),
each of length two. Their six vertices and four edges are distinct.
There are no other intersections: P uses the rectangle perimeter,
whereas the added squares have x=1 or 2, or lie above the missing b.
Consequently M has

\[
 (V_M,E_M,F_M)=(30+14-6,\ 47+19-4,\ 18+6)=(38,62,24).
\]

The unglued boundary of B consists of these two five-edge paths:

\[
\begin{split}
 L_+&\to(1,-1,1)\to(1,-1,0)\to(2,-1,0)
       \to(2,-1,-1)\to R_-,\\
 L_-&\to(1,1,-1)\to(1,1,0)\to(2,1,0)
       \to(2,1,1)\to R_+.
\end{split}
\]

The wall contributes P at z=+1 and P at z=−1, each of length nine.
The displayed paths exchange the two ends, so their union with those
two copies of P is one simple 28-edge cycle c. Gluing the two discs
along the two disjoint arcs makes a band with this single boundary,
hence a Möbius band. Interior vertex links are circles and boundary
vertex links are intervals: along each attaching arc two half-discs
join, and at its endpoints the remaining boundary is an interval.
This also checks the local condition at the four quarter turns.

**The cap C.** Each outer cap, at z≥1 or z≤−1, is a disc. Its ten wall
squares and six roof squares give F=16. Its vertices are the ten at
the open rim and the twelve of the 3×2 roof, so V=22. It has ten edges
on each rim, ten vertical edges and seven internal roof edges: E=37.
Its boundary is boundary R at z=+1 or −1, of length ten.

Call the eight-square central piece Q. Its face x=2 is a 2×2 grid
with (V,E,F)=(9,12,4). The other four squares form two pairs of flaps
at opposite corners. In each pair the squares share one x-edge and
attach to the grid along two adjacent boundary edges. The pair adds
three vertices, five edges and two faces, preserving the disc topology.
Thus Q has (15,22,8), with boundary length 12. Its boundary is exactly
the two five-edge paths displayed above, together with b at z=±1.

Q meets the upper cap only in b at z=1, and the lower cap only in b
at z=−1. Those edges are disjoint. The other parts of Q are inside or
outside R in the slab −1≤z≤1; the outer caps run away from that slab.
There are no additional point contacts. Gluing the three discs along
these edges therefore gives a disc C with boundary c and

\[
 (V_C,E_C,F_C)=(22+15+22-4,\ 37+22+37-2,\ 16+8+16)
             =(55,94,40).
\]

**Close the surface.** Put M at t=0 and C at t=1. The collar c×[0,1]
has 28 squares and 28 vertical edges. Its vertices are already exactly
the boundary vertices of M and C, at their respective t coordinates.
It has no additional intersections since c is simple. Hence

\[
 F=24+28+40=92,\qquad
 E=62+28+94=184,\qquad
 V=38+55=93.
\]

Every old boundary edge now has its second incident square. Every
boundary vertex interval joins the collar interval into a single circle.
The other vertex links were already circles. This verifies every link
and vertex condition by gluing, not by a list checked by software.
The surface is connected, and 93−184+92=1. Capping a Möbius band gives
a projective plane; the collar changes neither topology nor Euler
characteristic. The coordinate spans are 3,3,4,1 cells. Sides at least
4,4,5,3 avoid vertex identifications after insertion into the torus.

## 6. NS0 and the precise positivity obstruction

Proposition SC defines A(S) without the common factor exp(−beta|P|).
At a fixed finite torus, each selected sinh contributes beta x_p with
relative corrections of order beta^2; each unselected cosh starts at 1
with corrections of order beta^2. The Taylor expansion and the integral
above therefore give

\[
 A(S_0)=-2^{-183}\beta^{92}+O(\beta^{94})
       =-2^{-183}\beta^{92}(1+O(\beta^2))<0
\]

for sufficiently small positive beta. The sign has no numerical input.
The fine character assignment, spin 1/2 on S_0 and spin 0 elsewhere,
has the same negative sign: its character integral is −2^−91 and all
its character coefficients are positive. The sinh/cosh surface term
is therefore negative too, as asserted. If the common Wilson factor
is put back, its leading coefficient is unchanged, but its relative
remainder is generally O(beta), not O(beta^2).

This defeats termwise nonnegativity in these two stated expansions.
It does not rule out regrouping terms, another positive representation,
or a switching argument using cancellations. It does not refute (KP)
or positivity of a whole homology-class weight. The surface lies inside
a contractible box, so its class is zero.
The sentence in `gap-kappa-order.md:60` that calls every closed manifold
sheet term positive must consequently be restricted to orientable
sheets (or representations with the appropriate positive indicator).
The exact identity of Proposition SC itself is unaffected.

## 7. Earlier work and the scope of the comparison

**Flux duality and light sectors.** Gerard ’t Hooft's 1979
[A Property of Electric and Magnetic Flux in Non-Abelian Gauge Theories](https://doi.org/10.1016/0550-3213(79)90595-9)
is the historical source for electric/magnetic duality and its confinement
constraints. Only its publisher abstract and bibliographic record were
accessible here, so this note does not claim a full-text comparison with it.

Mendel Nguyen, Yuya Tanizaki and Mithat Ünsal,
[Study of gapped phases of 4d gauge theories using temporal gauging of the Z_N 1-form symmetry](https://doi.org/10.1007/JHEP08(2023)013)
(2023), Appendix A, equations (A.4)–(A.11), give an accessible derivation
of the duality and of the isotropy and cardinality of light-flux slices,
crediting ’t Hooft. Their binary limit uses a gapped-vacuum hypothesis
plus an explicitly identified assumption that normalized sector ratios
approach 0 or 1. At N=2 the nonempty slice has four mutually isotropic
elements. This is a close predecessor of the exact classification behind
CL and R2. The checked appendix does not derive a finite even seed from
small even-sector remainder and doubling deficit. Theorem R's finite
rounding estimate, quantitative hypotheses and seed conclusion must be
distinguished from that asymptotic classification.

Okuto Morikawa and Hiroshi Suzuki,
[Direct Monte Carlo computation of the ’t Hooft partition function](https://arxiv.org/html/2501.07042v2)
(2025), equations (1.1), (1.2) and (2.1)–(2.3), state the Fourier
normalization, the fixed-slice duality and the twisted Wilson action.
At N=2 their cubic-box duality is R1(b), up to relabeling the axes and
magnetic components. R1(b)'s rectangular version only needs the two
exchanged lengths equal. Their numerical study supplies no proof of
Theorem R's smallness hypotheses and is not used here. These papers
prevent treating the duality or the basic light-flux classification as new.

**The negative surface sign is already in the literature.** Sky Cao,
Minjae Park and Scott Sheffield,
[Random surfaces and lattice Yang-Mills](https://arxiv.org/pdf/2307.06790v4)
(2023; version 4, 2025), Section 6.1.2, Proposition 6.27, pp. 80–82,
give a signed symplectic Haar-word formula; Theorem 6.29 gives the related
lattice surface expansion. Here is its specialization, not a claim of
a new sign formula. Set N=2, so Sp(1)=SU(2). For a normal sheet with
two occurrences per edge, each edge has one pairing, with orthogonal
Weingarten weight at −2 equal to −1/2. The vertex cycles number V and
there are F trace words. Their formula gives

\[
 I_\chi=(-1)^F(-1/2)^E(-2)^V
       =(-1)^\chi 2^{V-E}.
\]

Dividing by 2^F recovers the normalized integral used above, including
the negative chi=1 sign. Thus the sign mechanism predates this repository
construction. The checked passage does not exhibit S_0's 92-square cubical
embedding or its sinh/cosh coefficient. Section 4 supplies a separate
tree-gauge derivation for the case requested here.

The bounded search found no earlier statement of the full quantitative
Theorem R, nor this specific 92-square construction. It did find the
earlier identities and sign just credited. No priority claim beyond that
search result is made. Witten's 1991 two-dimensional gauge-theory paper
was found bibliographically, but its crosscap formula was not checked
in accessible full text; it is not an imported proof here.

## 8. Source record and limits

The remote content searched was pinned to these fetched revisions:

| Ref | Revision |
|---|---|
| main | `a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc` |
| PR 10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| PR 10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| PR 10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| PR 10141 | `fb99b4dddc7254e6124ac124887d58eeb3a77802` |
| PR 10144 | `1f20846b8057f6346ebab6c0dbebdabbd9e472a4` |

The search families were duality/rigidity, light electric and magnetic
flux, nonorientability, projective planes, Frobenius–Schur signs and
negative surface terms. Most broad repository hits concerned unrelated
reality classifications or other gauge/fermion models. The close YM4D
hits opened are identified at the start of this note. The lead's digest,
`open-registry.md` and `open-core.md` were checked for duplicate ownership.
Search outputs remain under `/tmp/gap-rigid-check-Xs5pNE/`; the revisions
and substantive findings above do not depend on retaining that scratch.

The local inputs, all at the pinned checkout revision, were:

| Source | Read ranges and use |
|---|---|
| `gap-means-max.md` | Section 2.4 and Section 4, including their definitions; target statements |
| `gap-flux-exercise.md` | 109–146, 420–560; sector traces, crossing, CL1, CL, W, S-w, EV, X16 and EVL |
| `gap-flux-exercise-check.md` | Full note; earlier corrections and twisted transfer-matrix justification |
| `gap-crux-restate.md` | 29–46, 170–223; notation, A, K, X, E/E', S and all-integer enlargement |
| `gap-kappa-order.md` | 35–61; exact SC formula and the overbroad positivity sentence |

The Sussman–Alpoge index was used before opening bounded excerpts:
`sa-index/README.md`, neighboring gap/GL3/GL8 rows in chunks 01 and 02,
`obligations.md`, and the CA 4.12–4.19 index. Searches for the target
flux, nonorientable-surface and rigidity objects yielded no matching
target theorem. The downloaded sources are fixed at upstream revision
`31a47c543775` and were each fetched once:

| Source | Lines inspected | Relevance |
|---|---|---|
| [Outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex) | 588–599; 2195–2231; 2313–2335 | Decay scope; one-plaquette character coefficients; transfer-trace framework |
| [Complete account I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex) | 2702–2712 | Theorem 0's stated scope does not assert a mass gap |

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their outline/account text, for that inherited framework. Neither
source supplies a checked instance of ES here. The specified local
Balaban-paper directory was absent; no Balaban result or garbled OCR
formula is imported. No whole outline or complete account was read.

Verification here means the algebraic arguments, inequalities and
topological gluing written above. There was no numerical sector test,
surface enumeration, symbolic proof run or computer-assisted discharge.
Only this research check note is changed; no source theorem, registry,
audit record or scientific status is changed.

RESULT: R1–R3, Theorem R Steps 0–6, R4, R5 and R7 HOLDS; NS at chi=1 HOLDS AFTER CORRECTION by adding the one-cycle vertex-link hypothesis; S_0 and NS0 HOLDS, with 92 plaquettes and leading term −2^−183 beta^92; no order-one ES instance or scientific status is granted.
