# HCM-R: second round on the literal rim test

Codex, 2026-11-08. Checkout `16e489d52886236525a6a409c6e0ef691c796691`.
FINISH row 522. Research text. Not an audit. Grants no status.
No computer-assisted proof. Not checked by another model.

**Result: stop (c) at RIM-C (20), after three routes.**
HCM-R (4) remains open. The stated shift cost in finding 7 is false.

Check addressed: `../gates/hcm-false-check.md`, findings 6, 7, 8 and 11.

## 1. Ports and scope

There is no `prior/hcm-r2.md` at this checkout.
The registry's H-C-MARK row has no separate owner.
Searches of `open-core.md`, `l17c.md` and `port-map.md` found no supplier for this target.
The one-operation example, schedule count and majorant lemma are already done.
This note uses them without repeating their proofs.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the multiscale preparation and retained-region method.
**Y** means `YM4_1400.tex` at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
**SA** means `YM4_sketch_500.tex` at `31a47c543775`.
**I** means `theorem_0_complete_account_raw_I.tex` at that latter commit.
The line numbers below belong to those versions.
The outline index, its neighbouring rows and obligations preceded the source reads.
The CA index was used for the two CA entries below.

| Input | Source and scope |
|---|---|
| Literal rim equals a lifted top holonomy | Y 72324–72338; ported identity |
| Small-action affine field and its iterated average | Y 72340–72367; proved there on the commuting family |
| Earlier passes and one actual final-stage failure | Y 72375–72432; ported example, conditional on its named real estimates |
| Interior stage comparison excludes the outer joining collar | Y 72243–72322; ported comparison at the joined layer |
| Old guards and determining rows survive a prospective stop | Y 77526–77552; ported construction rule |
| The interrupted stage adds no gauge draw, elimination or normalizer | Y 77545–77549; ported rule, not cancellation of previous factors |
| Normalized moves represent the complete physical measure | SA 17499–17514; exact kernel identity, with agreement of formulas on supports |
| The component formula keeps its scalar normalizers | SA 18026–18042, 18060–18075; definition of the coordinate integrand |
| Gauge normalization has size comparable to theta to power minus three halves | SA 18734–18750; proved there on its stated cutoff range |
| Remaining rescalings have a logarithmic site price | SA 18751–18755; asserted estimate, not a lower comparison for this prefix |
| Actual pivot and its local coarea factors | SA 8167–8207, 8255–8306, 8308–8350; proved local chart, ported in §§7 and 9 |
| Stopped-space supply is an application condition | I 49495–49546; assumption, held at its existing scope |
| Preparatory boundary theorem assumes its stage theorem | I 54985–55004; conditional theorem, not a probability margin bound |
| The fixed-price contradiction | `hcm-false.md` (4)–(6), `hc-mark.md` §6.1; used as proved implications |

The source's affine calculation is not a theorem about translating an arbitrary noncommuting field.
Nor is a pointwise stage margin an estimate of conditional mass near a test boundary.
These distinctions matter in finding 7.

## 2. Fixed price and the extra logarithm

IN1 row 7 fixes $c=C_vc_r$ and $c_{\rm ent}$.
A refutation must prove a mass rate strictly smaller than their sum.
The refuter cannot enlarge $c$.
This repairs finding 6 in `hcm-false.md`.
Its table now restricts the mixture counterexample to the support-and-energy inference, as finding 11 requires.

Write
\[
 n_t=(MR_t)^4|C_t|,\qquad
 N=\sum_t n_t,\qquad
 v=\sum_t(1+\log x_t)n_t.                                      \tag{1}
\]
On the proposed plateau, $x_t\in[\Theta/2,\Theta]$.
Suppose a comparison with a normalized history law $Q$ gave
\[
 M(A)\ge e^{-C_N N}Q(A),                                     \tag{2}
\]
where $C_N$ is fixed independently of the plateau and absolute level.
Then $N\le v/[1+\log(\Theta/2)]$, directly from (1).
Thus its loss per unit $v$ tends to zero.
If also $-\log Q(A)=o(v)$, then $M(A)\ge e^{-o(v)}$.
For any fixed $c+c_{\rm ent}>0$, the corrected majorant contradiction would follow.
This is the useful effect of IN1's extra logarithm.

It does not apply to a loss $C_{\log}\sum_t n_t\log x_t$.
The ratio of that sum to $v$ tends to one on the plateau.
Such a loss retains the coefficient $C_{\log}$.
SA 18015–18018 sets $\mathsf l_t=\log\theta_t$.
SA 18751–18755 explicitly allows a cost $C\mathsf l_t$ per site.
Consequently the source's quoted normalizer bound does not make $C_*$ negligible.
One must first identify cancellations or prove a sharper comparison for the actual prefix.
No such cancellation is inferred from the interrupted stage contributing no new factor.

## 3. The packing scale in finding 7

Set $\eta=L^{-m}$ and $t_s=3(1-\beta_s/2)>0$.
Work at zero source with $x_j=\theta_j$, an admissible subcase for a refutation.
The rim threshold is $\tau_m=t_s\varepsilon_m\eta^2$.
Write $k$ for the number of grid spacings in each color direction.
This avoids confusing it with the terminal level $K$.
A three-dimensional grid of spacing comparable to $\tau_m$ and radius $a_{\max}$ has
\[
 k\asymp a_{\max}/\tau_m,\qquad \#\mathcal G\asymp k^3.       \tag{3}
\]
All comparison constants in this section are fixed geometric constants.

For $k^{-3}=O(L^{-6m})$ with a level-independent constant, (3) requires

\[
 a_{\max}\ge d\varepsilon_m                                \tag{4}
\]
for some fixed $d>0$.
Taking $a_{\max}=\varepsilon_m/4$ has exactly this size.
But the proposed paired action price then has size
\[
 \theta_0 k^2\tau_m^2\asymp\theta_0\varepsilon_m^2
       ={\theta_0\over\theta_m}P_m^2.                       \tag{5}
\]
There is no remaining factor $L^{-4m}$.
The frame gives $\theta_0\ge\theta_m+\underline\lambda m-c_5$.
At fixed top coupling, (5) grows with the absolute level.
Finding 7's displayed limit dropped the growing factor $k^2$.

This is not merely failure of an upper estimate to vanish.
On the source's affine region, each interior 12-plaquette has angle $a\eta^2$.
A fixed smaller box contains at least $d_0\eta^{-4}$ such plaquettes.
For $|a\eta^2|\le1$, $1-\cos(a\eta^2)\ge a^2\eta^4/4$.
The action there is therefore at least $d_0a^2/4$.
At the identity field the two signs have the same action.
Pairing them cannot remove this positive quadratic price.
This lower bound supplements the upper bound ported from Y 72340–72351.

A weaker rate could still suffice for HCM-R.
If the proposed price $C\theta_0a_{\max}^2$ were valid, choose
\[
 a_{\max}=d\theta_0^{-1/2}.
\]
It is below $\varepsilon_m/4$ at a sufficiently high floor.
Its price is bounded, and packing would give
\[
 C\theta_0^{3/2}\tau_m^3
   =C t_s^3P_m^3(\theta_0/\theta_m)^{3/2}L^{-6m}.             \tag{6}
\]
At fixed top coupling this is at most a polynomial in $m$ times $L^{-6m}$.
It tends to zero and is summable over $m$.
Indeed, the ratio of successive terms $m^bL^{-6m}$ tends to $L^{-6}<1$.
An arbitrarily long finite plateau can be translated to larger absolute levels.
Thus the error in (5) alone does not rule out a refutation.
The next issue is proving a transport estimate for the conditioned law.

## 4. What a conditional packing proof must supply

Use the full measure-layer experiment, including all earlier auxiliary draws.
Let $\lambda$ be its reference measure in a finite coordinate chart and $\rho$ its density.
Let $\mu=\rho\lambda$.
Fix a positive-mass earlier outcome record $E$ which reaches the prospective final test.
Let $A\subset E$ be passage of the selected rim plaquette.
Passage of the whole final test implies $A$.
Fixed exterior rows that determine this plaquette are not being conditioned on in this experiment.
With those rows fixed its outcome is deterministic, as `hcm-false.md` (2) states.

Here is a sufficient margin lemma, with the needed relative denominator.
Suppose there are $n$ pairs of injective, measure-preserving Borel maps $T_{q,+},T_{q,-}$.
For each pair choose $G_q\subset A$ such that both images lie in $E$.
All $2n$ images of these sets must be pairwise disjoint.
Assume, on $G_q$,
\[
 \rho(T_{q,+}z)+\rho(T_{q,-}z)\ge2e^{-D}\rho(z),              \tag{7}
\]
and assume the averaged margin bound
\[
 \sum_{q=1}^n\mu(A\setminus G_q)\le\delta n\mu(A),
       \qquad \delta<1.                                    \tag{8}
\]
Only a fixed $\delta<1$ is required.
No common intersection of all the $G_q$ is required.

**Packing lemma.** Under these hypotheses,
\[
 {\mu(A)\over\mu(E)}\le {e^D\over2n(1-\delta)}.              \tag{9}
\]
To prove it, integrate (7) on $G_q$ and use preservation of $\lambda$.
The result is
\[
 \mu(T_{q,+}G_q)+\mu(T_{q,-}G_q)\ge2e^{-D}\mu(G_q).
\]
Sum over the disjoint images in $E$.
Equation (8) gives $\sum_q\mu(G_q)\ge n(1-\delta)\mu(A)$.
These two inequalities prove (9).

For the bare Wilson density, a paired bound
\[
 S(T_{q,+}z)+S(T_{q,-}z)\le2S(z)+2D
\]
implies (7) by the arithmetic-geometric mean inequality.
In the actual experiment, (7) must include the auxiliary draw densities too.
If a map is not measure-preserving, its Jacobian belongs in (7).
Haar invariance of deterministic link translations proves only the assertion about $\lambda$.
It proves neither (7), separation of the images, nor (8).

In particular an absolute boundary estimate $\mu(A\setminus G_q)\le o(1)\mu(E)$ is insufficient.
The denominator in (8) is $\mu(A)$, which may be much smaller.
Likewise pointwise strict passage gives no uniform lower bound on its distance from a boundary.
Y 77529–77552 retains the full old guards.
Y 69535–69550 keeps hard cutoffs in their original slots after completing a square.
Neither passage supplies (8).

## 5. Route one: deterministic affine shifts of bare links

The source proves its affine formula when the field itself is commuting.
Left multiplication of an arbitrary field by that family is a different operation.
Here is an exact obstruction to the claimed uniform action price.

Let $T_1,T_3$ be Pauli matrices, with $T_i^2=1$ and $T_1T_3=-T_3T_1$.
Inside a fixed box put
\[
 G(x)=\exp\{\tfrac i2 b(-1)^{x_2/\eta}T_1\},\qquad
 U(x,y)=G(x)G(y)^{-1}.                                      \tag{10}
\]
Use lattice coordinates with $x_2/\eta$ integral.
Extend $G$ to the identity outside a larger box.
The entire field is pure gauge, so its Wilson action is zero.
In the interior, $U_1=1$ and $U_2(x)=\exp\{ib(-1)^{x_2/\eta}T_1\}$.
Every contour value and link is within $C|b|$ of the identity.
Thus $b$ can be arbitrarily small; this is not a large-curvature example.

Apply the proposed fixed shift
\[
 S_{a,1}(x)=e^{i\eta ax_2T_3},\qquad S_{a,\nu}=1\ (\nu\ne1),
       \qquad U^a_b=S_{a,b}U_b.                             \tag{11}
\]
Use the source's smooth cutoff outside the affine region.
Select a smaller box with $1\le x_2\le2$.
For an interior 12-plaquette write

\[
 s=\eta ax_2,\quad t=\eta a(x_2+\eta),\quad Q=U_2(x).
\]
Its holonomy is $e^{isT_3}Qe^{-itT_3}Q^{-1}$.
Multiplying the two Pauli expansions gives
\[
 \tfrac12\operatorname{tr}(e^{isT_3}Qe^{-itT_3}Q^{-1})
       =\cos s\cos t+\cos(2b)\sin s\sin t.
\]
Hence its Wilson action is exactly
\[
 1-\cos(a\eta^2)+2\sin^2 b\,\sin s\sin t.                   \tag{12}
\]
Here $s,t$ have the same sign.
Both terms are nonnegative for $|s|,|t|\le1$.
Using $|\sin u|\ge|u|/2$ on that interval gives
\[
 a_p(U^a)\ge b^2a^2\eta^2/8\quad (|b|\le1).
\]
There are at least $d_1\eta^{-4}$ such plaquettes.
Therefore
\[
 \theta_0 A(U^a)\ge d_2\theta_0b^2a^2\eta^{-2}.              \tag{13}
\]
Formula (12) is even in $a$.
The same lower bound holds for the paired average of the actions at $+a$ and $-a$.
Their linear terms cancel, but their commutator cost does not.
For any fixed nonzero $b$, (13) excludes a uniform bound $C\theta_0a^2$.
Even $b=\theta_0^{-1}$ leaves a divergent ratio $b^2\eta^{-2}$ at fixed top coupling.
The frame makes $\theta_0$ grow at most linearly in $m$.

This is a counterexample to a proposed shift estimate, not to HCM-R.
No complete repeated history is assigned to (10).
It shows why Haar invariance and small curvature cannot prove the claimed cost.
One must use a field-adapted transport, or a weaker estimate with a larger price.

There is an unconditional weaker estimate.
On a fixed support, each shifted link has generator of norm at most $C|a|\eta$.
Twice differentiating a plaquette trace gives a fixed finite number of products with two such generators.
Every other factor is unitary.
Thus its second derivative has absolute value at most $C a^2\eta^2$.
The support meets at most $C\eta^{-4}$ plaquettes.
The identity
\[
 f(1)+f(-1)-2f(0)=\int_{-1}^1(1-|s|)f''(s)\,ds
\]
now proves
\[
 S(U^a)+S(U^{-a})-2S(U)\le C\theta_0a^2\eta^{-2}.             \tag{14}
\]
This proof works for every bare field and for a three-color generator.
It uses no fluctuation estimate.

Choosing $a_{\max}=d\eta\theta_0^{-1/2}$ makes (14) bounded.
If image separation and (8) held, (9) would give
\[
 C P_m^3(\theta_0/\theta_m)^{3/2}L^{-3m}.                    \tag{15}
\]
This weaker rate still tends to zero after an absolute-level translation.
But Y 72352–72367 gives separation only on the commuting affine family.
It does not identify the shifted coarse holonomy on all of $A$.
The complete earlier outcomes need not be preserved either.
Thus (14) repairs the action estimate without proving a conditional pass rate.

## 6. Route two: transport the shift in a tree gauge

This route removes the pure-gauge obstruction in (13).
It can also preserve Haar measure exactly.
Choose a fixed rooted spanning tree of the bare patch.
Order its vertices away from the root.
Replace each tree link by the transport $g_x$ from the root to its endpoint.
Each replacement is a fixed group translation after earlier variables are fixed.
Repeated Haar invariance gives product Haar measure in the $g_x$.
For each non-tree link replace $U_b$ by
\[
 W_b=g_{b_-}U_bg_{b_+}^{-1}.
\]
Conditional on the tree variables this is again a fixed left-right translation.
The full change therefore preserves product Haar measure.
All tree links in $W$ equal one.

Hold the tree variables fixed and translate the non-tree $W_b$ by deterministic factors.
This is an invertible Haar-preserving map, even though its expression in $U$ depends on $U$.
Choose an axial tree with its direction-1 trunk in $x_2=0$.
All its other links run in directions where the affine potential vanishes.
Then the affine factors in (11) equal one on the tree.
For a pure-gauge input, $W=1$, and the source's affine computation applies.
Gauge covariance returns the coarse holonomy in the original frame.
This repairs (13) on that class.

For a nonflat field the tree links no longer determine the whole connection.
Its non-tree variables are Wilson loops around the fundamental tree cycles.
A plaquette bound $\epsilon$ bounds a loop with an $s$-plaquette filling only by $s\epsilon$.
Indeed, express the loop as the ordered product of transported plaquettes.
For unitary matrices, telescoping gives $\|\prod_iP_i-1\|\le\sum_i\|P_i-1\|$.
Tree cycles in a fixed physical patch can have $s$ of order $\eta^{-2}$.
This estimate gives no uniform closeness of the non-tree variables to one.
The available higher-scale tests cannot be replaced by such closeness without a proof.

The fixed-support derivative argument still gives (14) in this tree gauge.
It does not give the missing response estimate
\[
 a\longmapsto -i\log\partial V_m(T_aU)(p_m)                 \tag{16}
\]
with a uniformly nondegenerate three-dimensional derivative on the conditioned passing set.
Nor does it bound the mass lost when the actual guards are reevaluated.
Those guards include stored contour tests, not just gauge-invariant plaquettes.
The tree gauge is an integration coordinate; it does not delete those tests.
Auxiliary draw factors must also be transported in (7).

Thus this route supplies a legitimate field-adapted, Haar-preserving candidate.
It proves the source's response on pure gauges, where it was already known up to covariance.
It does not extend that response or the margin estimate to the conditioned law.
Assuming a uniform derivative bound in (16) would insert an unproved part of the supplier.

## 7. Route three: use the source's actual pivot chart

The account does supply a local inverse, so it must be checked before inventing another one.
SA 8167–8207 computes the one-step physical pivot coefficient as $L^{-3}I_3$ at the identity.
It also gives the conjugated coefficient at a pure gauge.
SA's index classifies QC22–QC24, 8257–8299, as the actual small-fibre chart.
SA 8308–8342 retains its real coarea determinant.
These are source results, credited to Sussman and Alpoge with Claude and Codex.
They are not new inverse constructions here.

Try to alter one selected top link by recursively changing its single native pivot.
At each earlier level choose the corresponding pivot again.
On the common abelian arc the contour logarithms average arithmetically.
Only the target row reads that pivot, by SA 8167–8176.
Exactly $L$ of its $L^4$ straight paths contain it, by SA 8181–8197.
Thus a leaf angle $b$ changes the top link angle by exactly
\[
 bL^{-3m}.                                                   \tag{17}
\]
The calculation iterates since all the other coarse links remain the identity.
A plaquette containing that top link has the same angle.
For a fixed small chart radius $b_0$, its largest displacement is at most $b_0L^{-3m}$.
But
\[
 {b_0L^{-3m}\over\tau_m}
      ={b_0\over t_s\varepsilon_m}L^{-m}\longrightarrow0       \tag{18}
\]
at fixed top coupling.
This local route cannot move even the flat datum outside the rim-passing ball for large $m$.
Equivalently, its inverse derivative has size $L^{3m}$.
Moving the top row by $\tau_m$ would demand a leaf displacement of order $\varepsilon_mL^m$.
That leaves the local chart.

The source's chart solves a one-step constraint.
It does not claim a uniformly cheap all-depth transverse variation.
Spreading the change over many fine links could avoid (18).
That returns to the coordinated transport and guard problem of §§5–6.
The coarea determinant cannot by itself restore the missing directions or margins.

## 8. The margin obstruction and the precise supplier

There is no measure bound in the word “strict”.
Here is a direct test of using large thresholds and a smooth density to prove (8).
On $(-3,3)^3$ use the density proportional to $e^{-|z|^2}$.
For $0<u<1$, impose these six earlier guards:
\[
 |z_i-(1-u)|<1,\qquad |z_i+(1-u)|<1,
       \qquad i=1,2,3.                                    \tag{19}
\]
Their conjunction is exactly $E_u=(-u,u)^3$.
Every threshold is one. Every guard is affine before taking its absolute value.
The density is positive and has a fixed quadratic logarithm.
Take $u=\tau/(4\sqrt3)$.
Every point of $E_u$ then passes $|z|<\tau$.
Its conditional pass probability is one.
Any translation of length greater than $2\sqrt3u$ moves this cube disjointly from itself.
Thus a grid translation of size $2\tau$ preserves none of this conditional event.
For those translations the left side of (8) is $n\mu(A)$, so no $\delta<1$ works.

This is not an actual Yang–Mills history.
It disproves an inference from smooth densities, bounded Hessians and large earlier thresholds to a relative margin bound.
The earlier mixture countermodel did not address that inference.
To exclude (19) for the actual problem, one must use its particular guard geometry and conditional law.

The deterministic margins in Y 72243–72322 concern specified background comparisons on an inset.
They are not stable-set estimates for the arbitrary translations of §§5–6.
Y 77529–77552 keeps the old tests on their full footprints after failure.
Holding auxiliary random choices fixed does not hold their outcomes fixed after the bare field changes.
Existence tests must be preserved too.

Here is one precise, weaker supplier to which all three routes were directed.
Call it **RIM-C, conditional rim escape**.
Fix the constants of IN1 and a finite plateau $[\Theta/2,\Theta]$.
Use the actual normalized bare Wilson experiment and its prescribed auxiliary draws.
Consider positive-probability earlier outcome records $E$ of the isolated one-lineage continuation.
They have no intervening funded exit and reach the prospective final stage at level $m$.
The top couplings in the continuation lie in the plateau.
Integrate the tested top rows in this experiment; do not fix them as exterior data.
For the selected lifted rim plaquette, require
\[
 \Pr\{\|\partial V_m(p_m)-1\|<\tau_m\mid E\}
    \le C_\Theta(1+m)^{3/2}L^{-3m}.                         \tag{20}
\]
Here $C_\Theta<\infty$ may depend on the plateau and the fixed constants.
It must not depend on the absolute level, cutoff, torus, placement or earlier outcome record.
Other admission and kernel inputs stay at the scopes in HCM-R.

The requested $O(L^{-6m})$ rate is stronger than (20).
Even (20) remains open here.
It would suffice for summably small passing probabilities after a common absolute-level translation.
It would not estimate the probability of reaching each stage, or the formula-layer mass.
Those further costs cannot be discarded.

The three routes fail at different steps.
The fixed affine route has the explicit action obstruction (13), and its weaker repair lacks image separation.
The tree route removes that gauge obstruction but lacks transverse response and preserved-guard mass on the actual conditional set.
The native pivot route has the explicit loss (18), already at the flat field.
None proves (20). None refutes it.

## 9. RIM-N: what the source normalizations do and do not give

Finding 8 correctly removes one possible factor.
Y 77545–77549 says the interrupted stage adds no draw, pivot elimination or normalizer.
The same passage says the prefix's one-step factors remain in their birth coordinates.
There can also be completed preparatory stages before that stop.
Their factors are not removed by a statement about the interrupted stage.
SA 18040–18042 keeps all such scalar factors in the component integrand.

There is an exact cancellation when a complete normalized scalar law is identified.
For example, with the gauge integral $z(\theta,\epsilon)$ of SA 18734–18750,
\[
 \int z(\theta,\epsilon)^{-1}
 1_{\{|u-1|<\epsilon\}}e^{-\theta(1-\operatorname{tr}u/2)}\,du=1.
                                                                    \tag{21}
\]
This follows from its definition; no second estimate of that source integral is needed.
The factor $z^{-1}$ and its own integral cancel together.
If additional guards restrict this integral, the result is their probability under this gauge law.
It need not equal one.
The same distinction holds for normalized Gaussian factors and their retained cutoffs.

The source also displays an actual logarithmic coordinate factor.
SA 8343–8350 gives, after $u=g_jy$,
\[
 (\sigma_0g_j^3)^{|\mathcal F_j|},\qquad
 \log g_j^{3|\mathcal F_j|}
       =-\tfrac32|\mathcal F_j|\log\theta_j.                 \tag{22}
\]
Here $\mathcal F_j$ is the actual set of free bonds in that chart.
This is not a claim that (22) survives uncancelled in the prefix.
It shows why a complete factor comparison is necessary.
If this factor survives at a number of coordinates proportional to $n_j$, its rate need not vanish.
Division by $1+\log x_j$ removes the logarithmic growth, but leaves a constant.
An upper bound of $C\log\theta_j$ per site cannot decide the required lower comparison.

SA 17499–17514 proves equality for the full measures represented by the moves.
It allows a normalized bare law as input.
It does not identify an arbitrarily stripped coordinate prefix with a conditional probability law.
In HCM-R, the paid birth factor is excluded and old factors occur only once.
Some determining data are fixed; others are integrated after their deltas are resolved.
A comparison must use precisely this division of factors and these coordinates.
Full-measure equality must be disintegrated through that division before it can supply RIM-N.

If the resulting positive density is $J_p$, set $Z_p=\int J_p\,d\mu_p$.
The normalized law $J_p\,d\mu_p/Z_p$ still needs identification with the intended conditional bare experiment.
Then hcm-false.md (12) applies with this very $Z_p$.
The source passages above do not give a lower bound for that restricted $Z_p$ after the prescribed factor extraction.
The common-envelope upper bound cannot supply it.
This is the remaining normalization issue; it has not been refuted here.

The logarithm in (1) would settle its rate if (2) were proved.
It does not prove (2).
The source's scalar cancellation (21) is a local input, not an identification of the whole prefix.

There is also a probability distinction before applying the majorant lemma.
Write $E_j$ for survival to the preceding rim stop.
Let $R_{j+1}$ mean reaching the next final test without another exit.
Then
\[
 Q(E_{j+1}\mid E_j)
 =Q(R_{j+1}\mid E_j)
   Q(\hbox{next rim fails}\mid E_j\cap R_{j+1}),              \tag{23}
\]
when $E_{j+1}$ is exactly that continuation event.
A conditional pass estimate bounds only the second factor.
The first factor includes all intervening ordinary and stage outcomes.
It also has to be kept in the mass lower bound.
Neither a normalized-move identity nor a small rim-passing probability bounds it from below.

Suppose eventually that these actual factors give $M_\Theta\ge e^{-o(v_\Theta)}$
for the repeated history family in hcm-false.md §4.
Keep $c=C_vc_r$ and $c_{\rm ent}$ fixed.
Its majorant lemma would imply
\[
 B_h\ge(c+c_{\rm ent}-o(1))v_\Theta.
\]
The ported schedule has $v_\Theta/P_h^2\to\infty$, whereas $B_h\le C_0P_h^2$.
This would refute HCM-R (4) when $c+c_{\rm ent}>0$.
The needed mass estimate has not been proved.
In particular, this conditional conclusion is not a refutation of HCM-R.

## 10. Result

**Stop (c), at RIM-C (20).** Three routes to this weaker conditional escape estimate fail as specified above.
HCM-R (4) is neither proved nor refuted.
The first open input cannot yet be narrowed to RIM-N.
Finding 7 omits both the growing grid factor in its cost and the noncommuting translation problem.
Its relative margin estimate is also unproved for the actual earlier outcomes.

The new by-hand results are the cost correction (5), the shift counterexample (10)–(13),
the uniform weaker cost (14), the conditional packing lemma (9), and the pivot limitation (17)–(18).
The tree change of coordinates supplies a Haar-preserving candidate, but no conditional mass bound.
The normalizer analysis identifies exactly when the extra logarithm would help.
No source test, research status or ownership row is changed.

| Claim | Status | Scope |
|---|---|---|
| Fixed-price and countermodel-scope repairs | Applied to hcm-false.md | Findings 6 and 11; check named under its header |
| Affine field, rim identity and one-operation failure | Ported | Y 72324–72432; already theirs |
| Grid price tends to zero while $k^3\asymp L^{6m}$ | False as stated | Equations (4)–(5), already on the commuting family |
| Fixed affine left translations have cost $C\theta_0a^2$ on arbitrary small-curvature fields | False | Explicit pure-gauge example (10)–(13); not a history refutation |
| Universal paired action cost $C\theta_0a^2L^{2m}$ | Proved here | Equation (14), deterministic bare shifts |
| Packing with the correct relative margin | Proved implication | (7)–(9); actual image separation and margin are not supplied |
| Tree-adapted shift preserves bare Haar measure | Proved here | §6; does not preserve earlier outcomes by itself |
| Recursive single-pivot route reaches the rim threshold within its fixed local chart | False | Equations (17)–(18), on the flat commuting field |
| Large thresholds and a smooth positive density imply the needed margin | False as an inference | Countermodel (19), not a Yang–Mills history |
| A loss $O(N)$ becomes negligible per unit IN1 volume | Proved here | (1)–(2); a loss $O(N\log\Theta)$ does not |
| Failed stage has no new normalizer | Ported | Y 77545–77549; previous factors remain |
| RIM-N and the full repeated-history mass lower bound | Unproved downstream | §§2 and 9; no normalizer cancellation or reaching probability is assumed |
| HCM-R (4) | Open | No actual-history counterexample or weighted renewal bound |
| **First open input: RIM-C (20), the actual conditional rim escape estimate** | **Open after three distinct routes** | **Fixed affine, tree-adapted affine, and native recursive pivot** |
