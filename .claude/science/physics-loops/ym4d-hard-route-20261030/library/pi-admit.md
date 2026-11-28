# PI-ADMIT: complete reads at actual entries

Checked line by line by Claude (Opus 5.5), gates/pi-admit-check.md: ADVANCE; wording repairs applied.

Codex; checkout `75f92f69536ea90fdeea5cec2df1f110dec0ba76`.
FINISH row 482. Research text, not an audit. No scientific status is granted.
This file is the only repository output. No computation supplies a proof.

## 1. Target and sources

The target is the verdict in `prior/pi-admit.md`, section 6.
It concerns each actual operator entry on its prescribed complex domain.
It does not concern arbitrary pairs satisfying the older S1 and S2.
That larger assertion is already false by `out-pi.md`, Propositions 3.2–3.3.
Those counterexamples do not identify a history which the construction produces.

Admission requires the actual reference on every coefficient read.
It requires S1-loc on whole PI patches, including their exterior traces.
It also requires S2 and S2+, with the correct scales and common ceilings.
Changing the Hessian or the averaging rows requires a separate identification.

Write **I** for `theorem_0_complete_account_raw_I.tex` and **SA** for
`YM4_sketch_500.tex`, both at revision `31a47c543775`.
Write **N** for `YM4_1400.tex`, at revision
`2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
SA and I were fetched once. N was fetched once if absent.
Their SHA-256 values agree with the digest:

| Source | SHA-256 |
|---|---|
| SA | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| N | `222ef1bd4b668f88fab33f6edd131b4308fc897eefb112ac5898b8730549f178` |

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text, receive credit for all account statements used below.
Balaban supplies the geometric method: multiscale cubes, collars and local
gauges from CMP 99b, erosion from CMP 109, and localization from CMP 116.
The specified local paper folder is absent on this machine.
References to those papers below use the account's quotations and repository
ports. They do not claim a fresh reading of the original PDFs.

The outline index and its neighbouring rows were consulted before source
excerpts. The digest's consumer census fixes the scope.
`open-registry.md:442` assigns this admission problem to `pi-admit`.
`cp-triage.md:140–185,228–269` leaves the wider GEOH and DOM tasks separate.
In particular, this note does not take over the stage theorem or LOC-flat.

## 2. What is already supplied

The following are inputs, not new proofs here.

| Source | Content | Status in the source |
|---|---|---|
| I 12712–12728, 12935–12973 | General tower and S1–S3 input class. | Definitions. |
| I 52362–52419 | Data collar and the single-gauge condition `(reg)^sharp` on each enlarged box's data trace. | Hypotheses. |
| I 52620–52663, 52762–52801 | Weighted twist norm and its first-seam conversions. | Definition and proved conditional estimates. |
| I 52800–52925, 53220–53245 | Box fitting; the same fitting argument at all indices. | Proved conditional geometry. |
| I 53164–53218 | A later consumer ceiling can be imposed on `a^sharp`. | Proved conditional order of choice. |
| I 53260–53333 | Direct restriction of `(u1)` and the distinction from the stronger box route. | Proved conditional restriction; `(u1)` is an input. |
| I 49495–49546 | Actual real-background membership and the later drop-out spaces. | Application conditions; not supplied by the operator theorem. |
| I 50149–50319 | Step tests, hulls and the first-step P0 contribution. | Definitions and elementary set identities, with the stated first-step reading. |
| N 61973–61991 | One-cell label hull, explicit bare test, and five P0 layers. | Construction rules. |
| N 16102–16129 | General separated regions; distinct whole-action and inner-action Hessians. | Definitions. |
| N 16964–16977 | Boundary parametrix using incident inner plaquettes. | Outline argument under native regularity assumptions. |

Theorem PI, its counterexamples, and the PI-class GW/GW1 results are reused.
Neither their proofs nor the account's box-fitting proof are repeated.
The remaining work is to supply the hypotheses for actual entries.

Two newer results must also be retained. N 35847–35907 proves protected
stencils on the two-layer inset of either erosion tower. N 35634–35822
proves the regular proper background and its uniform physical continuation.
The regularity in that theorem tests **inner** plaquettes
(N 35276–35287). Its determining bonds satisfy `c subset Omega_0`
(N 10554–10566). These results supply their stated interior and native
boundary problems. They do not specify exterior links for the whole-action
PI problem. N 1990–2008 and 2062–2078 retain the separate history-domain
conditions. N 40688–40713 likewise retains complete gauge cubes and collars.

## 3. The complete-read box interface implies PI admission

This is a conditional match, not an actual-history assertion.
It states exactly what can be taken from I, sections 4.14–4.16.

Fix a PI setting, including its literal rows, pairings and compressed
whole-action Hessian. Identify its propagator block `M_b` with I's `M_1`.
The later localization block `M` remains different.
Use one matched fine lattice and region membership convention.
The proposition assumes the row and index identification; it does not prove it.
Assume I's nest condition (A1), I 45570–45585: the regions are nested;
each `Omega_j`, for `j>=1`, is a union of closed level-j `M`-cubes
from partitions compatible under L-adic refinement;
`dist_infty(Omega_j^c,Omega_{j+1}) >= M ell_j` for `1<=j<=k-1`;
and `Omega_0` is the Dirichlet hull of `Omega_1`.
These are the aligned shells; assume also the box cover used in I 52362–52419.
In particular, `X_0` is the whole complement of `Omega_1`, with closure.
Assume the data collar `(col)` and `(reg)^sharp` for the **actual** reference.
The twist norm must include every PI bond and every required difference pair,
including the extra bonds of `Omega_0^+`. Its transports use that reference.

Choose the fixed blocks so that

\[
 M_1\mid M_1^\sharp\mid M,\qquad
 M\ge13L^2M_1^\sharp,\qquad
 M_1^\sharp\ge3M_1,\qquad
 r_N+2\le4M_1^\sharp.                                      \tag{1}
\]

Retain the PI gaps (T) and torus floors as well. In particular, add the
level-0 hypothesis `dist(Omega_0^c,Omega_1) > R M_b eta` from (T),
with PI's Euclidean distance; (A1) does not impose this gap.
These are lower bounds on
fixed blocks. They impose no depth or volume dependence.

Let the real bound be `a^sharp`. Let the twist-current norm of I 52620–52647
be less than `r`, with twist radius `a_1^oplus`. Require

\[
 a^\sharp\le a_0^*/2,\qquad
 L^2r a_1^\oplus\le a_1^*/2.                              \tag{2}
\]

Here `r` bounds the whole prescribed parameter domain.
It cannot be obtained by discarding part of that domain.
The current component of this norm is irrelevant to this admission step.
GW1 and the layer consumers retain their separate current ceilings.

**Proposition 3.1.** These complete-read inputs imply S1-loc, S2 and S2+.
The constants are uniform in depth, volume and patch position.

**Proof.** Put `j=lambda(x)` and `s_j=M_1^sharp ell_j`.
Use the shell covering fact proved in I 52800–52814 and its all-index
version at I 53220–53245. Choose a box centre `y` in `X_j` with
`|x-y|_infty <= s_j`. This is the same choice used in the account's fitting
lemma, I 52881–52925. By (1),

\[
 N(x)^{+2\eta}\subset\{z:|z-y|_\infty\le5s_j\}
                         =\square^4.                    \tag{3}
\]

The extra two fine spacings include any first-difference stencil at the
patch edge. The collar places the background reads in the data region.
Restrict the single gauge supplied there by `(reg)^sharp`.
If a site of `N(x)` lies outside the data region, assign its gauge arbitrarily.
No bond on which a bound is required uses that assignment.

The account proves that this box meets at most two adjacent shells.
It proves this first at the two lowest levels, I 52816–52878, then at every
level, I 53220–53245. Its bound uses a bond midpoint or a pair position.
PI uses endpoint scales. The scale ratio is at most `L`: the endpoints and
the pair position lie in these same two shells. At the outer boundary,
both conventions extend the scale as `eta` outside the nest.
Thus the value loss is at most `L`, and the difference loss at most `L^2`.
The restricted potential satisfies

\[
 \ell_{\lambda(z)}|A|\le L a^\sharp,\qquad
 \ell_{\lambda(z)}^2|\nabla A|\le L^2a^\sharp.              \tag{4}
\]

These are S1-loc with `a_0=a^sharp`.
The derivative is the ordinary difference, as required by PI.
No gauges from different boxes have been glued.

For the twist, use the norm already proved to give the seam losses in
I 52762–52801. Equivalently, apply the same ratio bound to each full stencil.
It gives `N_(U_r)(a) < L^2 r a_1^oplus`. This proves S2.
An additional exterior bond has scale `eta`. Its difference pair has the
same bare scale near the outer boundary. These indices were included in
the assumed norm. They give S2+ with the same constant, and in fact without
the seam loss there. Equation (2) supplies the stated margins. This proves
the proposition. ∎

I 53164–53218 supplies the real constant's order of choice in (2).
That order is ported here. The twist inequality is a separate consumer
ceiling. Neither follows for an earlier prescribed domain merely by
declaring a smaller replacement domain. Its actual image must be bounded.

**Exact scope of the changed class.** Proposition 3.1 supplies the stronger
complete-read class in the digest. On that class Theorem PI applies directly.
Replacing an input class by this class does not prove that every actual
consumer enters it. The missing part is supply, not another inverse estimate.

## 4. One supplier lemma

Call the following statement **C0-SUP: actual boundary re-entry**.
It is a supplier within PI-ADMIT, not a new registry item.

Consider each actual entry in the digest's section 5 which requires PI.
Use its prescribed parameter domain, actual determining set and ambient
continuation. Include every parameter and switch value which the call uses.
Write `X` for its outer region, and `eta` for its fine spacing.
One explicit localized entry is I 131725–131746, where `X=Omega_0(B_Z)`.
Restrict this supplier to entries requiring the whole-action PI input.
If an entry instead requires the native inner-action operator, its
identification remains separate.

**C0-SUP.** At each such entry, the actual continuation has one consistent
real reference and actual twist
on `X^{+2 eta}`. On every PI patch crossing `partial X`, that reference has
one unitary gauge satisfying

\[
 \eta |A|,\ \eta^2|\nabla A|\le L^2a_0^*.                  \tag{5}
\]

The actual twist satisfies

\[
 \eta|a|,\ \eta^2|\nabla_{U_r}a|<a_1^*                   \tag{6}
\]

on all boundary bonds and exterior stencils read by PI. The same constants
work over histories, depths, volumes and the prescribed complex domains.
Those domains include the enlarged discs used by the consumer.
The supplier must follow from the construction's data and tests, before
using the PI-based layer theorem at this entry.

The scale in (5) is bare. The gap proof in
`out-pi.md:763–798,1630` makes outer boundary models entirely bare.
For a PI patch this follows from the same gap inequalities: a patch centred
at level `j>=1` cannot cross the preceding boundary; a level-zero patch
meeting `X^c` cannot also reach `Omega_1`. The gaps exceed twice its reach.
There is no hidden high-level elliptic estimate in (5).

I 119615–119650 requires one **global** pair and its own ambient
continuation. Separate local extensions cannot establish that membership
if they disagree on shared actual reads. I 131725–131746 names the localized determining
set and lists its ambient raw-stratum conditions. It does not print (5)–(6).
I 137566–137569 places the localized set outside the input spaces' geometry
and invokes the localized layer-function lemma with its proof incomplete.
These are the precise extra reads to be supplied, rather than a new proof
of the whole stage theorem.

The next three sections attack this one lemma by different routes.

## 5. Route 1: construct gauges directly from passed tests

### 5.1 What the original bare test does supply

Use the explicit first-step rule in N 61973–61991. This is stronger
information than merely saying that `Omega_1` is a union of coarse cells.
Work in a nonzero summand of its positive partition. Let `A=P_0'` be the
coarse hull of the failed bare tests. For coarse cells, let `d_cell` be the
graph distance with touching cells adjacent. The rule gives

\[
 \Omega_1\cap A^{\sim5}=\varnothing,\qquad
 \Omega_0=\Omega_1^{\sim1}.                               \tag{7}
\]

Equation (7) refers to cell index sets. Geometric closures come afterwards.
Let `q=r_N+3`, and let `W_1=M check R_1 ell_1` be the coarse-cell side
in the present physical units. Impose `q eta<W_1`, a fixed block floor.
Take `x` whose PI patch crosses the outer boundary. It has level zero.
Let `Q_x` be the fine-site box of half-width `q eta`.
It includes the PI patch and its first-difference padding.
The PI torus floor makes this box nonwrapping.
Every coarse cell meeting `Q_x` is at most one cell from a cell containing
`x`, hence at most two cells from `Omega_1`. Every cell of `Omega_1` has
distance at least six from `A`. Thus each cell meeting `Q_x` has distance
at least four from `A`.

Every bare density cube covering a plaquette base point in `Q_x` therefore
passed its test. Otherwise its hull would put that point in `A`.
The one-layer enlargement in the bare test includes the plaquette itself.
Consequently the **tested bare field** obeys

\[
             \sup_{p\subset Q_x}|\partial U_{\rm bare}(p)-1|
                           <\varepsilon_0.               \tag{8}
\]

This uses the P0 tests. The P1 and Q1 tests alone do not establish (8).
The cell argument is Balaban's nested-collar method, here applied to
Sussman and Alpoge's explicit first-step partition.

Port the comb-gauge construction of N 5104–5125, with its interval length
`2L` replaced by `2q` fine steps. In four dimensions, sliding an added bond
through the later coordinate segments uses at most `6q` plaquettes.
Use `K=8q`. On the whole box this gives

\[
                   |U_{\rm bare}^u(b)-1|\le K\varepsilon_0.
                                                               \tag{9}
\]

The construction is one unitary gauge, not separate bond gauges.
Its estimate follows by telescoping the product of the conjugated
plaquettes; each conjugation has norm one. This is the account's proof.

For SU(2), choose `K epsilon_0<1/4` and take the principal Hermitian logarithm
`eta A=-i log U_bare^u`. Its eigenvalue bound gives
`eta|A|<=2K epsilon_0`. For any two parallel neighbouring bonds in the box,

\[
 \eta^2|\nabla A(b,b')|
       =\eta|A(b')-A(b)|\le4K\varepsilon_0.                \tag{10}
\]

Thus `4K epsilon_0<=L^2 a_0^*/2` proves (5) for this bare reference.
The twist is zero, also on exterior reads, so (6) holds.
All constants are fixed before the bare smallness threshold.
No estimate depends on the number of fine sites in the torus.

This establishes a boundary certificate for the tested original field.
It establishes the same certificate for any reference agreeing with that
field on `Q_x`. Agreement only of averages is insufficient.

### 5.2 Why this does not yet propagate to the localized entry

Try to repeat (8) for the reference `V_r` of a newly reached setting.
If this is an unchanged restriction on complete reads, section 6 applies.
Otherwise its relation to the previously tested reference must be established.
The old indicator tests `U_bare`, or the field stored at its creation.
It does not test `V_r` merely because a later call uses the same position.
SA 17440 explicitly distinguishes determining and action sequences.
Stored terms retain the space in which they were created.

Here is the exact estimate this attempted propagation needs.
If `V_r=e^{i eta h}U_r` on every bond of a plaquette and `h` is real, then
unitarity and a four-factor telescoping identity give

\[
 |\partial V_r(p)-1|
       \le |\partial U_r(p)-1|
                   +4\eta\sup_{b\in\partial p}|h(b)|.     \tag{11}
\]

If the right side is small on the whole box, (9)–(10) regenerate the gauge.
Thus this route needs a bound for the **actual** `h` on every link of the
box, or a small-curvature extension agreeing on all required boundary reads.
An interior estimate cannot be inserted into the supremum in (11).

The new proper-background theorem does not give these missing plaquettes.
Its regularity supremum is over inner plaquettes, N 35276–35287.
Its physical continuation has complete stencils for that native problem,
N 35771–35822. The protected-stencil theorem, N 35847–35907, puts the
two-layer inset safely inside free pillars. It does not turn a patch at
the untrimmed outer boundary into that inset.
SA 17396's small current at such a bond also uses inner plaquettes only.

Using the PI-based layer bound to estimate `h` at this same call would
assume the admission being sought. No such use is made here.
The direct-test route therefore stops at (11) on the protruding reads
of the newly reached reference. This is a failure to close C0-SUP,
not a counterexample to that lemma.

## 6. Route 2: carry the box certificates through restriction and extension

The account has a stronger supplier than an interior curvature argument.
Port I 49120–49189. Given the printed gauge clause on the appropriate
nest, it supplies a single gauge on the hull with constant

\[
        \mathfrak a(\square)
             =L^2\mathsf c_1 B M R_{m(\square)}
                              \alpha_{0,m(\square)}.      \tag{12}
\]

Its proof restricts the supplied gauge and converts the layer weights.
In the localized case its conclusion is expressly on
`square^4 intersect Y_loc intersect X_n`. This domain is part of the result.
If these sets contain the full PI reads, and (12) meets (2), Proposition 3.1
settles admission there. Neither its constant nor its fitting argument is
missing.

There is also a valid restriction step. Suppose an admitted pair is used
unchanged on a smaller tower, at the same fine mesh, with
`Omega'_j subset Omega_j`. Assume every new background read remains in the
old complete background domain. Require the smaller tower to satisfy (T)
and the PI floors. Then

\[
       m'(z)\le m(z),\qquad N'(x)\subset N(x).             \tag{13}
\]

Restrict the old patch gauge. Its old weighted value and difference bounds
imply the new ones. Restrict the same twist and its full stencils.
The smaller weights give S2. Any newly exterior coefficient has bare
weight, which is no larger than its old weight; this gives S2+.
No radius is lost. This is the complete-read version of the finer-scale
restriction used at N 37360–37386. It covers genuine restrictions.
It does not identify a different localized background with that restriction.

Try next to manufacture the missing collar by a cutoff. This procedure
already exists. I 46800–46829 and 46890–46930 extend local twists with
the bound `(1+2L/M)r/2<r`, starting with a globally given real reference.
I 47789–47812 cuts off a real potential in a single supplied gauge cube.
`b109.md:1953–2017`, P14, records both results and their exact limitation.
They are ported, not reconstructed here.

The cutoff agrees with the old field only where it equals one.
To use reading independence, that region must contain every coefficient
read, including the protruding Wilson plaquettes. One cannot first cut
off those links and then invoke reading independence for them.
Furthermore, the gauge assumed in I 45439–45507 lives on the nest trace.
The stronger version in I 52362–52419 lives on the **data-region** trace.
Passing from the former to the latter is not the box-fitting theorem.
I 49495–49515 explicitly retains actual global membership as an
application condition.

A small exact example isolates the exterior-norm problem. It is an example
about the attempted inference, not about a realized RG history.
For definiteness, take a finite torus with coordinates
`i_n in Z/(2J Z)` and spacing `eta`. Choose `J` large.
Let `X={-J+1,...,0} times (Z/(2J Z))^3` in lattice coordinates.
Near its face through zero, the region is `x_1<=0`. Take `U_r=1`.
Let `H=sigma_3`, `K>0`, and put, on a complex parameter disc,

\[
 a(z)(b_2)=\eta^{-1}KzH,\qquad
 b_2=(2\eta e_1,\,2\eta e_1+\eta e_2),\qquad
 a(z)(b)=0\quad(b\ne b_2).                               \tag{14}
\]

These formulas specify positive bonds; reversed links are their inverses.
The face is chosen far from other faces and torus identifications.
The bond `b_2` belongs to the two-spacing background collar.
It is tested only by the S1-loc and S2+ hypotheses; no PI coefficient reads it.
It is neither a field bond nor the parallel one-step neighbour of a
field bond. Hence a norm testing only field bonds and their first
difference stencils is zero. The family `exp(i eta a(z))` is entire
and equals the flat field at `z=0`. But

\[
                    \eta|a(z)(b_2)|=K|z|.                \tag{15}
\]

No fixed exterior bound follows from that interior norm or from
holomorphy at the real centre. This tests a hypothesis index, not a coefficient PI reads.
If the supplied norm includes `b_2` and
its pairs, this example is excluded. Proposition 3.1 then uses those bounds.

With a supplied real reference, one may choose a bounded filler on otherwise
unused exterior indices.
At a bare boundary, zero filling costs only a fixed first-difference loss:
for a retained value `eta|a|<=c` next to zero, the new scaled difference
is at most `c`, since the reference transport is unitary. Thus extension
existence alone is not the obstruction. The required facts are that the
filler changes no actual coefficient and agrees with the prescribed
ambient continuation wherever that continuation is read.

I 119615–119650 requires the continuation of one global pair. Local
extensions may evaluate a term only after their complete-read equality
and domain hypotheses have been established.
The real collar condition `(col)` alone also says nothing about the
twist norm's missing indices.

This route proves the restriction implication (13) and the conditional
admission of section 3. It does not supply their complete-read antecedents
for every actual localized continuation. The attempted extension step has
not proved C0-SUP. Example (14) rules out inferring it solely from the
smaller norm and a holomorphic germ.

## 7. Route 3: use the native boundary inverse instead

The newer outline gives a substantial alternative. Its proper background,
physical continuation and boundary inverse retain the true inner action.
N 16964–16977 sketches the boundary construction; N 31940–32015 gives the
commutator and parametrix argument without filling missing plaquettes.
These results must be used on their own domains. Their method follows
Balaban's finite-range localization and parametrix construction.

Try to replace the whole-action PI entry by this native entry.
The necessary equality already fails at a flat boundary.
Use the finite slab of section 6 for `Omega_0`, with `J>=4`.
The calculation is local to its face through zero. Take `U=1` and real
`alpha!=0`. Let

\[
 b=(0,\eta e_2),\qquad A(b)=\alpha\sigma_3,qquad
                         A(c)=0\quad(c\ne b).             \tag{16}
\]

The bond belongs to both variable sets. Exactly one of its six plaquettes
leaves the region: the plaquette in the positive `e_1` direction.
The other five lie inside. Let `Delta_W` be the compressed whole-action
Hessian, and `Delta_in` the inner-plaquette Hessian on common variables.
With PI's Hessian normalization, the missing plaquette contributes
`1-cos(eta t alpha)` to the Wilson action along `tA`. Its second derivative
at zero is `eta^2 alpha^2`. Since `||A||_2^2=eta^4 alpha^2`,

\[
 \langle A,(\Delta_W-\Delta_{\rm in})A\rangle
                          =\eta^{-2}\|A\|_2^2>0.         \tag{17}
\]

This difference remains at zero curvature and zero twist.
It is not an error of order `a_0+a_1` about the flat reference.
Moreover, PI includes touching field bonds; N's determining bonds obey
`c subset Omega_0` (N 10554–10566). Equality of names does not identify
these variable spaces either.

Nor does the native theorem select a good exterior reference. With all
inner links fixed to one, arbitrary changes on a crossing bond leave the
native inner data and action unchanged. Proposition 3.3 of `out-pi.md`
already supplies two such exterior choices: the flat extension is admitted,
whereas a member of its one-bond path makes the PI operator singular.
This is a ported obstruction to inferring a whole-action certificate from
the native inner field alone. It is **not** a claim that the RG selects
the singular choice.

Trimming the region also fails to identify the original entry. When the
outer block is invertible, eliminating its variables gives

\[
       D_{II}-D_{IO}D_{OO}^{-1}D_{OI},                    \tag{18}
\]

not simply `D_II`. This follows by solving the outer equation for its
variables and substituting into the inner equation. Using (18) requires
an outer inverse and its bounds. A proof on an inset does not supply them
for the original untrimmed entry.

Thus the native route supplies a different, useful boundary problem.
Equations (17)–(18) prevent the proposed direct substitution into PI.
A new boundary comparison and consumer identification could still work.
They have not supplied C0-SUP by this route.

## 8. Outcome and effect on consumers

This is stop **(c)**. One supplier, C0-SUP, remains unproved after the
three routes above. Route 1 constructs the original bare certificate but
cannot propagate its plaquette bound to all new reads. Route 2 carries
complete certificates but cannot create their missing actual membership.
Route 3 constructs the native inner boundary problem but does not identify
the whole-action entry. None of these failures proves C0-SUP false.

The interior supply of Proposition 3.1's inputs at actual entries also remains open.
I 49503–49510 requires real-background membership and gauges on `Q intersect Omega_0`.
I 137566–137569 places the localized set outside the input spaces' geometry
and invokes a localized layer-function result whose proof is incomplete.
The lemma itself is marked "Stated; proof incomplete" at I 131633.
Thus C0-SUP is the first open input, not the only one.

The digest does not exhibit a positive-weight history producing the old
singular crossing-bond field. Neither does this note. Therefore it does not
claim the task's counterexample alternative, or stop at that counterexample
alone. The unrestricted input-class obstruction is already ported in
`out-pi.md`; it is not a newly realized history here.

Section 3 proves a sufficient box criterion for the digest's field refinement.
The box criterion is not asserted to be the weakest such criterion.
The account's construction on that refinement is not proved here.
In particular, a new admission indicator would require a
corresponding large-field assignment. The identity
`1=chi_admit+(1-chi_admit)` gives partition coverage, but gives no small
factor for the new complement. N 62010–62019 expressly distinguishes these
two requirements for totalized tests. No such modified expansion is claimed.

Consequently the digest's consumer census remains conditional.
I 13142–13173 is the general (S1)–(S2) entry, not the first bare inverse.
The localized setting used to formulate
C0-SUP is I 131725–131746. Its complete ambient continuation is described
at I 119615–119650. The same admission issue remains for the other fresh
settings in the digest's section 5, including completion and paired frames.
This note neither admits those entries by renaming their operators nor
asserts that their prescribed complex domains can be shrunk.

The displayed estimates and matrix identities are hand arguments.
No numerical run or finite enumeration was used.

## 9. Status table

| Claim | Status | Scope or first missing input |
|---|---|---|
| PI on its admitted class | Ported from `out-pi.md:273–321`; existing result | Actual-entry hypotheses remain. |
| Enlarged boxes, all-index fitting and constant order | Ported from I 52362–52419, 52800–52925, 53164–53245 | Conditional on the stated shells, data collar and box gauges. |
| Weighted perturbation norm and seam losses | Ported from I 52620–52663, 52762–52801 | Only indices included in the norm. |
| Complete box interface implies S1-loc, S2, S2+ | Proved here, Proposition 3.1, using those ports | Interior supply of these inputs at actual entries is also open: I 49503–49510, 137566–137569, 131633; the localized set is outside the input spaces' geometry, and its layer-function lemma has proof incomplete. |
| Original P0 partition supplies the bare boundary certificate | Proved here, (7)–(10), using N 61973–61991 and the gauge proof at N 5104–5125 | Tested bare field; fixed block and smallness floors. |
| Same-field, complete-read restriction preserves admission | Proved here, (13); matches N 37360–37386 | Nested smaller tower satisfying (T) and the PI floors, unchanged field and contained reads. |
| Hull gauge constants and cutoff completions | Ported from I 49120–49189, 46800–46829, 46890–46930, 47789–47812 | Supplied gauges or global real reference; full-read equality retained. |
| Protected inset and native proper background | Ported from N 35847–35907, 35634–35822 | Native inner action and its stated geometry and datum hypotheses. |
| Interior norm plus holomorphic germ does not bound an unspecified exterior | Proved here, (14)–(15) | Test of a hypothesis index, not a coefficient PI reads or an actual-history counterexample. |
| Native inner Hessian is not the whole-action Hessian | Proved here, (16)–(17); definitions at N 10540–10566, 16129 | Already different on a common variable at the flat reference. |
| Arbitrary S1–S2 input class admits singular crossing-bond fields | Ported from `out-pi.md:339–347,1210–1225` | No realized RG history asserted. |
| Construction and every consumer survive the refined field class | Input; not proved | Partition coverage alone does not give large-field bounds or actual continuation membership. |
| **First open input: C0-SUP, section 4** | **Input; three routes fail to close it, sections 5–7** | **Uniform boundary gauges and exterior twist control for actual reached entries on their prescribed domains.** |
