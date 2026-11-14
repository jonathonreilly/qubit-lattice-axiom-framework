# Repo search

The lead's November 8 digest concerns earlier large-field and history
targets. Its local Wilson witness is already used by
`gap-fusion-astra.md`. It does not bound a twisted partition-function
ratio. I read the digest and checked PR 10114's
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:89–166` and
`checks/review_massgap_block_literature.md:105–130`. These paths are
relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
The second passage records Ito and Seiler's common-endpoint warning.
Neither passage supplies (TR-F).

Row 789 also names `NONLINEAR_CHART_ACTIVITY_ASTRA.md:82–108`
in that directory, and the sibling
`ym4d-existence/EXISTENCE_session6_snapshot.md:2268–2295`.
I checked both. Their small commutators concern covariance patching
and block-average noise. Neither is a centre-twist transport.
No numerical evidence from the snapshot is used.

The target-specific `prior/gap-trf-astra.md` is absent at this pin.
The registry, `open-core.md` and `l17c.md` have no match for
(TR-F), this row, or the displacement class below. Row 793 owns
this continuation. This does not reopen the broader fusion or
literature assignments.

The close prior results are reused: Codex's (LC) and (E21)–(E23)
in `gap-ext-astra.md`, checked by Claude Opus 5.5 in row 791;
the fixed-exterior obstruction in `gap-cf-astra.md`, checked by
Claude Opus 5.5 in row 788; and Lemma J/Way 3 of
`gap-crux-restate.md:143–160`. The last concerns fixed link
multiplications and their first-order action cost. This note's
proposed class allows arbitrary field dependence and mixtures.
Its bound concerns the complete cost, including the information term.

A targeted search on main and the four requested PR heads found
four outside-lane hits on PRs 10114 and 10133. I read the PR 10114
passages: `BFT4B55.md:188–200` is gauge averaging;
`SPHERE55.md:277–291` is reflection factorization;
`REVIEW_LOCOP.md:31–42` concerns source Taylor remainders;
`CODEX_REVIEW_LARGE.md:78–96` uses an even-coordinate plaquette
packing. That geometry is credited in Section 2. None of these
passages states the transport bound proved below. No assertion
of absence beyond this search is made.

## Contract and checkpoint

Author: **Codex gpt-6-astra max**, FINISH row 793, 2026-11-12.
Source pin: `3c444d5b9865305ddb3433f97e026ad022a65b24`.
Research text, not an audit; this grants no status.
**PROVED** means a hand proof by the author, not an independent check.
**ARGUED** marks an unverified argument or source classification.
**GUIDE** decides nothing. **OPEN** names an unproved obligation.

Read: GOAL, the requested FINISH sections, `gap-ext-astra.md`
and its check, `gap-cf-astra.md` and its check, and Section 5 of
`gap-fusion-astra.md`. The workflow was read from main at
`bb4ec020d5ada57c630dd89acc98a68397ade423`; its research procedure
and physics-loop skill are used within this assigned output's scope.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text**, for the outline/account material.
Both prescribed files were fetched once at `31a47c543775` into
the new directory `/tmp/ym4d-gap-trf-20261112.c8yI8V/`.
The index was searched first. Chunk 24 and its neighbouring rows
lead to ET5–ET6, outline 26765–26805, 26848–26867,
26925–26945 and 27060–27086. The quoted requirement is
one energy “serving both measures”. Their later conditional
construction compares a finite reference with periodic states;
it does not state the present twisted comparison.
The other index hits, outline 7913 and 10514–10527, concern
contour Haar coordinates and operator commutators. They do not
supply the group transports at issue here. No theorem from those
passages is needed in the proof below.

**PROVED — current checkpoint.** Theorem 3 excludes arbitrary
correlated transports with small mean squared endpoint displacement
on the twist sheet, even after field-dependent periodic gauge
alignment. Corollary 4 excludes bounded uses of the (LC) generators
per link as their size tends to zero. Section 5 constructs an
actual triangular Haar map that flips all direction-1 Polyakov
loops coherently, and proves its whole cost grows at least as
the sheet area. General (TR-F), (26) and (FQ) remain **OPEN**.

## 1. Consumer and exact cost

**PROVED inputs, reused.** Use row 789's notation
`mu=mu_m`, `mu'=mu_(m+v)` and `X=S_(m+v)-S_m`.
Put `F=-log(Z_(m+v)/Z_m)`.
Here `S_k=beta sum_p(1-eta_(k,p) s_p)`,
`Z_k=int exp(-S_k) dU` and `dmu_k=exp(-S_k)dU/Z_k`.
The signs represent the indicated closed centre cocycle.
For a finite family of Haar-preserving measurable bijections
with measurable inverses, let

\[
 \nu_j=(T_j)_*\mu,\qquad \nu=\sum_j\pi_j\nu_j,
 \qquad I_\pi=\sum_j\pi_jD(\nu_j\Vert\nu).
\]

The weights are independent of the field. Their number and values
may depend on the lattice and on beta. The full cost is

\[
 \mathcal C(T,\pi)=\sum_j\pi_j\mathbb E_\mu
       [S_{m+v}(T_jU)-S_m(U)]-I_\pi.
\]

Equations (E21)–(E23) give

\[
 \mathcal C(T,\pi)
 =\mathbb E_\nu X+D(\nu\Vert\mu)
 =F+D(\nu\Vert\mu').                         \tag{T1}
\]

All action terms and the exact information term are included here.
In particular `C >= E_nu X`. This inequality can exclude a family
without separately estimating its action loss on every other plaquette.

**OPEN sufficient statement, unchanged.** The weakest consumer
remains (FQ), from row 778. On `n=(a,a,c,d)`, with
`c,d in {a,2a}`, it asks for

\[
 Q_F=\max_{m_2=0,\ i=3,4}
       \frac{1-Z_{m+v_{1i}}/Z_m}{2},\qquad
 8Q_F\le K(a)\sqrt{S_{\rm ev}(a;(a,c,d))},
 \quad Q_F<1/192,\quad K(a)\le C_1a^{p_1}.    \tag{FQ}
\]

Here `m` is spatial in frame 1, and `S_ev` is the same even-sector
thermal sum as in that row. Its checked witness is
`S_ev>=eta_*^a`, with `0<eta_*<1/16` on `I`.
A sufficient transport estimate is

\[
 \mathcal C(T,\pi)\le\varepsilon_a,
 \qquad
 \varepsilon_a=
 \min\{1/96,\ K(a)\eta_*^{a/2}/4\},
 \qquad K(a)\le C_1a^{p_1}.                  \tag{T2}
\]

It is required for every crossed pair and shape, uniformly on
`I=[beta_-,beta_+]` contained in `(0,infinity)`.
To exclude a proposed family as a supplier it suffices to fail
on the required cube `(a,a,a,a)`, with `m=0` and `v=v_13`.
This pair belongs to frame 1's crossed list (`i=3`, `m_2=0`).

## 2. A uniform positive plaquette mean

**PROVED.** On the untwisted periodic cube, let

\[
 s_p(U)=\tfrac12\operatorname{tr}U_p,
 \quad c_0(\beta)=\int_{SU(2)}e^{\beta\operatorname{tr}(g)/2}\,dg,
 \quad \kappa_I=\min_{\beta\in I}\frac{\log c_0(\beta)}\beta,
 \quad r_I=\kappa_I/54>0.                   \tag{T3}
\]

Then `E_(mu_0) s_p >= r_I` for every plaquette and every `a>=3`.
The positivity of `kappa_I` is the strict-Jensen argument already
used in (E25). The even-coordinate packing also occurs in PR 10114's
`CODEX_REVIEW_LARGE.md:78–90`, for a different probability bound.
The added step here applies conditional Jensen to its edge union,
then uses convexity to obtain a volume-independent mean.

Put `b=floor(a/2)`. Select the 13-plaquettes with bases

\[
 (x_1,x_2,x_3,x_4)=(2j,x_2,2k,x_4),
 \qquad 0\le j,k<b,
 \quad x_2,x_4\in\mathbb Z/a\mathbb Z.
\]

There are `M=b^2 a^2` selected plaquettes. Their edge sets are
disjoint, also across the periodic boundary. Only directions 1
and 3 occur. Any 13-plaquette wholly within their edge union must
have both its base coordinates in `{0,2,...,2b-2}`; hence it is
selected. Every other plaquette therefore has an edge outside
that union.

Fix the selected edges and Haar-integrate the rest. Every
unselected plaquette has conditional Haar mean zero: integrate
one of its outside edges, which occurs once. Conditional Jensen
gives

\[
 Z^0(\beta)=\int e^{\beta\sum_p s_p}\,dU
 \ge\int e^{\beta\sum_{p\ {m selected}}s_p}\,dU
 =c_0(\beta)^M.                             \tag{T4}
\]

The last equality uses the disjoint edge sets. Each selected
plaquette holonomy is Haar under the product Haar measure.
Write `f=log Z^0`. Differentiation under the finite compact
integral gives `f''=Var(sum_p s_p)>=0` and `f(0)=0`.
Convexity gives `f'(beta)>=f(beta)/beta`.
Translations and axis permutations make every plaquette mean
the same on the untwisted cube. Since there are `6a^4` plaquettes,

\[
 \mathbb E_{\mu_0}s_p
 =\frac{f'(\beta)}{6a^4}
 \ge\frac{b^2}{6a^2}\frac{\log c_0(\beta)}\beta
 \ge\frac{\kappa_I}{54}=r_I.                \tag{T5}
\]

Here `b>=a/3` for integers `a>=3`. This proves the claim.
No clustering or strong-coupling expansion was used.

## 3. The complete cost excludes small endpoint displacement

Use the standard representative
`Sigma={p_13(x): x_1=x_3=0}` of `v_13`. It has `a^2`
plaquettes. Their `4a^2` unoriented edges are distinct; denote
their union by `E_Sigma`. In this section `mu=mu_0` and
`X=2 beta sum_(p in Sigma) s_p`.

**Definition.** For each map choose any measurable periodic
vertex gauge `g_j(U)`. It need not preserve either measure.
It is used only to compare configurations. For `e=(x,y)` put

\[
 \widetilde U_{j,e}
   =g_j(U)_x^{-1}(T_jU)_e g_j(U)_y,
 \qquad d_{j,e}(U)=\|\widetilde U_{j,e}-U_e\|_{\rm op},
\]
\[
 L_\Sigma(T,\pi;g)
 =\sum_j\pi_j\mathbb E_{\mu_0}
       \sum_{e\in E_\Sigma}d_{j,e}^2.        \tag{T6}
\]

There is one gauge on the entire torus for each output.
Separate alignments for the four corners of each plaquette
are not allowed. A gauge on a cover with twisted boundary
conditions is not a periodic gauge in this definition.

**Theorem 3 — PROVED.** Every family in Section 1, for every
such choice of gauges, obeys

\[
 \boxed{\quad
 \mathcal C(T,\pi)
 \ge 2\beta\{r_I a^2-2a\sqrt{L_\Sigma(T,\pi;g)}\}.
 \quad}                                    \tag{T7}
\]

There is no restriction on the number of maps, their dependence
on the Wilson variables, their correlations, or their changes
on edges outside `E_Sigma`.

*Proof.* Gauge invariance of the plaquette trace holds for each
configuration, also when the gauge depends on that configuration.
For four unitary factors, telescoping their products gives

\[
 |s_p(T_jU)-s_p(U)|
 \le\sum_{e\in\partial p}d_{j,e}(U).       \tag{T8}
\]

Indeed the norm of each telescoping term is the norm of its
changed factor, and `|tr M|/2<=||M||_op`. Reversing an edge
does not change the difference norm, since inversion on unitaries
is an isometry. Summing (T8) uses each sheet edge once.
Cauchy–Schwarz on the product of the probability law
`pi_j mu_0(dU)` and counting measure on `E_Sigma` gives

\[
 \sum_j\pi_j\mathbb E_{\mu_0}
     \sum_{e\in E_\Sigma}d_{j,e}
 \le 2a\sqrt{L_\Sigma(T,\pi;g)}.
\]

By (T5), therefore,

\[
 \mathbb E_\nu X
 \ge2\beta\{r_I a^2-2a\sqrt{L_\Sigma(T,\pi;g)}\}.
\]

Apply (T1), retaining `D(nu||mu_0)>=0`. This proves (T7).
The full mean change in `S_0`, on and off the sheet, less the
exact `I_pi`, equals that nonnegative relative entropy. Thus
negative contributions on some other plaquettes cannot defeat
(T7). No plaquette cost or information term was omitted. QED.

**PROVED exclusion.** The natural class

\[
 L_\Sigma(T,\pi;g)\le r_I^2a^2/16
 \quad\hbox{for some measurable periodic alignments}
                                                        \tag{SD}
\]

has `C >= beta_- r_I a^2`. It fails (TR-F) for all sufficiently
large `a`, uniformly on `I`. In fact it eventually fails even
the constant ceiling `1/96`. In particular every family with
`L_Sigma=o(a^2)` fails, with uniformity on `I` when the little-o
bound is uniform there.

**PROVED necessary condition, not a sufficient estimate.** If a
family does meet (T2), then for every such choice of alignments

\[
 L_\Sigma(T,\pi;g)
 \ge\frac1{4a^2}
       \left(r_I a^2-\frac{\varepsilon_a}{2\beta}\right)_+^2.
                                                        \tag{T9}
\]

Thus the coupling between input and output supplied by the maps
must have squared displacement of order the sheet area, even
after periodic gauge alignment. This is an obstruction to that
coupling class, not a lower bound on the actual twist free energy.

## 4. Arbitrarily correlated uses of the small generators

**Definition: the class being excluded.** For each lattice choose
an integer `N>=2` and the generators `A_N,B_N` of (LC).
After one periodic alignment as in (T6), require each sheet link
to have the form

\[
 \widetilde U_{j,e}=L_{j,e}(U)\,U_e\,R_{j,e}(U).       \tag{T10}
\]

Together `L_(j,e)` and `R_(j,e)` contain at most `q` factors.
Each factor is an arbitrary conjugate of `A_N`, `B_N`, or an
inverse of either. The factors, their order, their conjugating
matrices and the choice to omit them may depend on the entire
field and on `j`. All correlations are allowed. Each complete
map must still satisfy the Haar-bijection hypotheses of (E22).
We do not assume that an arbitrary field-dependent multiplication
automatically preserves Haar measure.

This class includes parallel insertion of (LC) commutators when
each link receives a bounded number of insertions, followed by
any periodic gauge transformation. Each commutator counts as
four generator factors. It also includes compositions whose total
number of such factors per sheet link has the bound `q`.

**Corollary 4 — PROVED.** For this class,

\[
 \mathcal C(T,\pi)
 \ge2\beta a^2\{r_I-4q\sqrt{\pi/N}\}.         \tag{T11}
\]

In particular, if `q/sqrt(N)` tends to zero, uniformly on `I`,
the entire family fails (TR-F) for large `a`. This allows any
finite number of maps, including one growing arbitrarily fast
with `a`.

*Proof.* For `G=A_N` or `B_N`, the SU(2) norm identity and (LC)
give `||G-I||_op^2=2(1-tr G/2)<=pi/N`. Inversion and conjugation
preserve this norm. Telescoping (T10), including factors on both
sides, gives `d_(j,e)<=q sqrt(pi/N)`. Hence
`L_Sigma<=4a^2 q^2 pi/N`. Insert this into (T7).
Once `q sqrt(pi/N)<=r_I/8`, the lower bound is
`beta_- r_I a^2`. QED.

**PROVED averaged version.** A deterministic maximum `q` is
unnecessary. If `q_(j,e)(U)` counts the factors in (T10), then

\[
 L_\Sigma\le\frac\pi N
       \sum_j\pi_j\mathbb E_{\mu_0}
         \sum_{e\in E_\Sigma}q_{j,e}^2.       \tag{T12}
\]

Thus a mean square factor count `o(N)` per sheet edge also fails.
Rare fields with many updates are allowed in this statement;
their actual probability remains inside (T12).

The conclusion concerns final link changes. It places no lower
bound on the sum of squared increments along a long path of maps.
Coherent accumulation can make a large final change from many
small increments. Such accumulation can leave this class.

## 5. A concrete coherent Haar transport and its whole cost

**PROVED construction; failed supplier.** The following map
realizes an exact coherent centre flip using the Wilson variables.
It does not rely on independent conjugation of the increments.

Take `N=a` in (LC), write `C=C_a`, and fix a direction-1 circle.
In its coordinate order let its link matrices be `U_0,...,U_(a-1)`.
Put

\[
 P_0=I,\qquad P_r=U_0\cdots U_{r-1},\qquad
 V_r=P_r^{-1}CP_r U_r\quad(0\le r<a).         \tag{T13}
\]

Apply this rule to every direction-1 circle, leaving all other
links fixed. The circles have disjoint link sets. The controls
`P_r` in (T13) are the original prefixes.

The map `T_C` is a measurable bijection. Recover `U_r` in increasing
order by

\[
 U_r=P_r^{-1}C^{-1}P_r V_r,
\]

where the preceding recovered links determine `P_r`. Each forward
coordinate is left multiplication of `U_r` by a function of
earlier coordinates. Conditional Haar invariance, successively
in `r`, proves that it preserves product Haar. Equivalently,
perform the updates in decreasing `r`; each is a Haar-preserving
shear whose controlling prefix is unchanged during that update.
This also proves Haar preservation on all circles together.

Each shear has the exact four-factor realization

\[
 P_r^{-1}CP_r
  =[P_r^{-1}A_aP_r,\ P_r^{-1}B_aP_r].       \tag{T14}
\]

The controlling prefix uses no copy of the updated link. Thus
each of those four left multiplications, with the order in the
commutator, is itself an admissible shear.

Induction, without commuting any Wilson link through `C`, gives

\[
 V_0\cdots V_{r-1}=C^rP_r,
 \qquad V_0\cdots V_{a-1}=-P_a.             \tag{T15}
\]

So every direction-1 Polyakov trace changes sign. Moreover

\[
 \|(T_CU)_e-U_e\|_{\rm op}
 \le\|C-I\|_{\rm op}=2\sin(\pi/(2a))\le\pi/a
                                                        \tag{T16}
\]

on changed links. This is coherent transport in the actual
configuration space. It does not identify the output law with
the law twisted by `v_13`.

**PROVED action accounting.** Only plaquettes in planes 12, 13
and 14 can change: `3a^4` plaquettes. Each contains two changed
links. For all other plaquettes the trace is unchanged. Therefore

\[
 |S_0(T_CU)-S_0(U)|\le6\pi\beta a^3.        \tag{T17}
\]

The exact target action difference is

\[
 S_v(T_CU)-S_0(U)
 =\beta\sum_{p\notin\Sigma}\{s_p(U)-s_p(T_CU)\}
  +\beta\sum_{p\in\Sigma}\{s_p(U)+s_p(T_CU)\}.       \tag{T18}
\]

Terms outside the three affected orientations in the first sum
vanish. This displays every changed plaquette, including those
outside the twist sheet. The pointwise estimate (T17) alone
does not give the desired comparison.

**PROVED density and information accounting.** For any mixture
supported on `T_C`, its inverse and the identity, with
field-independent weights, the densities are

\[
 \rho_j(V)=\frac{e^{-S_0(T_j^{-1}V)}}{Z_0},\qquad
 \rho(V)=\sum_j\pi_j\rho_j(V),
\]
\[
 I_\pi=\sum_j\pi_j\int\rho_j(V)
 \log\frac{e^{-S_0(T_j^{-1}V)}}
               {\sum_k\pi_k e^{-S_0(T_k^{-1}V)}}\,dV.   \tag{T19}
\]

The inverse just given makes these actual output densities.
No unknown twisted normalizer appears in (T19). Applying the
exact identity (T1) to (T18)–(T19) gives, for the whole cost,

\[
 \boxed{\quad
 \mathcal C(T,\pi)
 \ge2\beta\{r_Ia^2-2\pi a\}.
 \quad}                                    \tag{T20}
\]

Indeed, each sheet plaquette has only two changed links. By
(T8) and (T16), its trace decreases by at most `2pi/a`.
The inverse map has the same displacement bound: apply (T16)
at its preimage. The identity has zero displacement. Average
these bounds and use (T5) and (T1). Once `a>=4pi/r_I`,
the right side is at least `beta_- r_Ia^2`. Neither a fair coin
between the two coherent directions nor any other weights
repair this failure. This proves a bound on (E22), including
its exact information subtraction, without guessing that subtraction.

**PROVED binding-test scope.** The small four-factor realization
(T14) uses (LC). That realization fails in U(1), whose commutators
are identity, and in the binary icosahedral group for unbounded
`a`, by its positive gap from identity. These are the prior checked
tests, not new phase theorems. The formula (T13) by itself could
use an Abelian root `C`; that observation shows why a loop flip
alone does not distinguish the required groups. No successful
confinement construction is inferred from it. The exclusion
theorem can hold in comparison groups; a negative theorem need
not furnish a group-specific positive mechanism.

## 6. What the exclusion changes, and what remains open

**PROVED, stated scope.** This is the requested third alternative:
an obstruction for a specified natural class. Arbitrarily correlated,
field-dependent Haar transports satisfying (SD) cannot meet (TR-F).
This includes the factor class (T10) with `q/sqrt(N)->0`, and
the actual coherent construction (T13). It is stronger in this
direction than the earlier independent-increment test: the choices
here need not be independent, isotropic, or fixed multiplications.
It is also an integrated cost obstruction, not a pointwise claim
about a rare exterior configuration.

**GUIDE.** A continuation that inserts each vanishing (LC)
generator only a bounded number of times per link is excluded.
It must leave that class to have any chance of meeting (TR-F).
For example, a large accumulated endpoint change, or a centre
change on a seam, can leave it. Neither is shown to suffice.
Changing the cocycle representative also requires checking the
displacement relative to the representative actually used in the cost.

**OPEN — one remaining comparison.** For the unrestricted problem,
one still needs, on every crossed pair and the prescribed shapes,
a law obtained from admissible Wilson transports for which

\[
 \mathbb E_\nu(S_{m+v}-S_m)+D(\nu\Vert\mu_m)
 \le\min\{1/96,\ K(a)\eta_*^{a/2}/4\},       \tag{T21}
\]

uniformly on `I`, with polynomial `K`. This is the original
(TR-F) comparison, not a new reduction or a claimed weakening.
Theorem 3 supplies a necessary displacement bound for one of its
pairs. It supplies no small upper bound after that restriction is
removed. Direct control of the weighted exterior mean (26) is
likewise not supplied. The weakest sufficient consumer stays (FQ).
No conclusion about a finite-beta phase of either comparison
group is used or proved.

## 7. Scope check and source record

**ARGUED self-check of scope; no independent check.** Applying the
repository's no-go discipline within this research-only task:

- **N1, family:** all finite Haar-bijection mixtures on the cube,
  for `(0,v_13)`, with field-independent weights and (SD). The
  uniform inequality (T7) covers the entire family, not a list
  of unsuccessful constructions.
- **N2, dependencies:** there is one displacement restriction.
  No claim of several independent barriers is made.
- **N3, premises:** product Haar, finite lattice with `a>=3`,
  positive compact beta interval, untwisted Wilson input, the
  displayed representative, and one periodic gauge per output
  are explicit. No mixing, saddle approximation or phase input
  occurs in (T3)–(T20).
- **N4, prior results:** (E21)–(E23) supply the exact same cost
  identity. Lemma J and the fixed-exterior counterexample have
  different classes; they supply context, not proof of (T7).
- **N5, resolution:** the conclusion bounds the complete finite
  lattice cost. It does not exclude all transports, all source
  sectors, or all resolutions of a spreading argument.
- **N6, premises versus definitions:** no new axiom, physical
  identification, or change of the target is needed or proposed.
- **N7, strongest escape:** many coherent updates on the same
  sheet links could produce order-one endpoints while each
  increment is small. The prior common-coin example after (E20)
  already shows why independent-increment bounds miss coherent
  accumulation. Such transports may violate (SD); they still
  owe (T21). This escape is outside the excluded class.
- **N8, earlier restrictions:** (E18)–(E20) concern independent
  increments; (E25) concerns uniform link-sign mixing; Lemma J
  concerns fixed factors. Their open escapes are preserved.
  The present theorem closes the small-endpoint correlated class
  only. No audit packet, computational certificate or status is
  claimed for this hand argument.

Read remote revisions:

| Ref | Commit |
|---|---|
| main | `bb4ec020d5ada57c630dd89acc98a68397ade423` |
| PR 10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| PR 10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| PR 10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| PR 10141 | `fb99b4dddc7254e6124ac124887d58eeb3a77802` |

The outside-lane search expression and its complete results are
in `search-record.json` and the five `*.search.txt` files under
`/tmp/ym4d-gap-trf-20261112.c8yI8V/`. A preceding broad query
matched unrelated endpoint displacements and was truncated; it
supports no conclusion. The completed narrower search is the
one reported above. The local gap-note search found no existing
displacement theorem under the searched terms. These are search
limits, not an absence theorem.

The outline index README, matching chunk rows and neighbours,
and `obligations.md` preceded the source reads listed above.
The CA-I index for 4.12–4.19 was included in the object search;
no statement from those items is an input. Outline 565–600 was
also read after its index entry; its spectral example supplies
no twist estimate and is not used here. The two downloads are
at the prescribed revision. No additional literature download,
numerical run, machine enumeration or computer-assisted proof
was used. Only this output file is written in the checkout.

**PROVED by the author, not independently checked:** the positive
plaquette mean (T5); the full-cost bound (T7), (SD) and (T9);
the generator corollary (T11)–(T12); and the triangular map,
its inverse, density and cost bound (T13)–(T20).
The next useful check is those statements with their constants,
especially the edge-union property in (T4) and the exact
information cancellation in (T1). No checked or retained standing
is requested by this text.

Work is local and uncommitted on `research/gap-trf-astra-3c444d5b9`.
The two downloads have 32,992 and 166,711 lines; their hashes are
in the scratch directory's `source-manifest.json`. These checks
are bookkeeping only. No prior proof,
queue, registry, audit record or status file was edited. Nothing
was posted or pushed.

RESULT: PROVED for the stated small-endpoint class — arbitrary correlated, field-dependent Haar transports in (SD), including (T10) with q/sqrt(N) tending to zero and the explicit coherent Polyakov-flip map, have whole cost at least beta_- r_I a^2 and cannot meet (TR-F) for large a; unrestricted (TR-F), (26) and order-one (FQ) remain OPEN, and the new hand proofs are not independently checked.
