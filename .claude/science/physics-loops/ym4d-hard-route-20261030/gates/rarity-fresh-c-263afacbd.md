# Hand check of rarity-fresh-c, queue 58
Provenance: OpenAI Codex / GPT-6 (exact serving variant and runtime effort are not exposed; the item requests xhigh); source commit `263afacbdc5f0b2247f5bd706be9343fbb31c19b`; research text, not an audit, grants no status. The source identifies its author as Anthropic Claude Opus 5.5/max. This is a separate-model reading, not independent certification.

All source paths below are relative to this loop directory. File retrieval and writing are the only computer operations used for the mathematics: no computation, search experiment, numerical evidence, or computer-assisted discharge. No remembered theorem is used as an established premise. Elementary calculations are displayed; proposed repairs remain unproved for the hierarchy.

| Statement checked | Verdict | Reason / scope |
|---|---|---|
| EX (2.1) | ADVANCE | Exact integral comparison when its bounds and a nonzero normalizer are supplied. |
| EX product application to hard fibres | CORRECT-NO-ADVANCE | Product denominator, compatible replacements and additive gains are not supplied. |
| FC (2.2), level-zero force estimate (2.3) | ADVANCE | Integration by parts, Gaussian averaging and plaquette incidence; Section 9 below. |
| FC's payment for every named pack | CORRECT-NO-ADVANCE | Needs a force lower bound for that pack; not a rough-field bound. |
| RANK: privacy | ADVANCE | Fixed-pattern face-bond geometry is sound. |
| RANK (2.4), hence (JW) | CORRECT-NO-ADVANCE | Global branch/chart and inverse arguments are missing; no counterexample to (JW) claimed. |
| RANK's literal distance of `Dlog` from identity at most `1/4` for angles `<=1/2` | WRONG | The transverse norm is at least the angle; take angle `1/2`. |
| PER | ADVANCE | Its telescoping proof uses exactly its strong exterior-independent increment hypothesis. |
| S1: conditional gain, denominator, entropy, label change | CORRECT-NO-ADVANCE | First unsupported route step; Defects 1–3, before the admitted multiplier gap. |
| S2 | CORRECT-NO-ADVANCE | Enlarged-domain branch formula and constrained comparison are not supplied. |
| S3: bounded descent | CORRECT-NO-ADVANCE | The cited age bound includes diameter and an extra hypothesis. |
| S3(a): `(1+p)^N<=2`, with N the size of G | WRONG | Choose `N>1/p`; binomial expansion gives a value greater than 2. |
| S3(b) | CORRECT-NO-ADVANCE | Dense payment needs joint lower-level prices and bounded multiplicity. |
| S3(c), `(SEC_m)`, availability of `(ADD_m)` | CORRECT-NO-ADVANCE | VAL/PER's extension and locality hypotheses do not follow from the cited statements. |
| S4: zero parent influence of a sparse hole across patterns | WRONG | A removed face column changes the normalized average; explicit commuting bond variation in Defect 5. |
| S4: probabilistic recursion (4.1) | CORRECT-NO-ADVANCE | The `m_*`-child alternative and joint bound are missing. |
| S4: solving the scalar recursion once supplied | ADVANCE | The displayed induction absorbs its error at a fixed large `x_*`. |
| S5, S6 | CORRECT-NO-ADVANCE | Rough-parent accounting and the terminal comparison are absent. |
| S1–S3 imply (SEP) | CORRECT-NO-ADVANCE | No positive rate established; full-law rarity is weaker than same-pattern deletion. |

**First failure:** in the requested S1–S6 route it is S1's unprovided conditional chart/minimum and integral comparison, before the multiplier bound. In the note's earlier auxiliary-lemma order, RANK is the first proof not carried through; its literal logarithm derivative estimate is explicitly false. No counterexample to the final Wilson rarity clauses or to (SEP) is claimed.

## 1. S1: start with the denominator, not the multiplier

**Verdict: CORRECT-NO-ADVANCE.** The earliest unsupported step in the S1–S6 route is S1's passage from the named regular estimates to a uniform comparison for the *site-conditioned, parent-constrained* law, including its admissible minimizer and denominator neighbourhood (`rarity-fresh-c:76–80`). It occurs before the admitted multiplier gap. Being class on the free bonds does not itself construct a convex fibre chart with arbitrary retained holes/data. The displayed difference is written for `F_k`, although the immediately preceding definition replaces it by `F(.|omega)=-log Inner(omega;.)`.

### Defect 1: the conditional law and its upper comparison are not supplied

Lemma EX itself is **ADVANCE**, for a finite, nonzero normalizer: bounding the numerator by `m(Q) exp(-inf_Q F)` and the denominator below by `m(D) exp(-f_D)` proves (2.1). Its usefulness depends on the actual reference measure on the fibre, including label weights and constraint Jacobians. It is not an estimate of these quantities.

There is a useful qualification to the requested semi-concavity test. On a *supplied, uniformly controlled class chart* of fixed dimension `n`, the named first-order locality bound can suffice. Write `F=x A+R`, suppose `|D R[h]| <= b ||h||_1`, `b=C+C x exp(-mu d)`, and suppose the pulled-back classical Hessian is at most `C_A`. At an interior minimizer, `x DA(0)=-DR(0)`. Integration along the segment gives

```
F(h)-F(0) <= (C_A x/2)||h||_2^2 + 2b||h||_1.
sup_{||h||_2<=x^(-1/2)} [F(h)-F(0)]
    <= C_A/2 + 2C sqrt(n/x) + 2C sqrt(nx) exp(-mu d).
```

At fixed `n,d`, this is `o(x)` and can be absorbed in a positive fixed multiple of `x eps_q^2 T^2`. Thus **failure of all-depth semi-concavity alone does not refute the proposed denominator strategy**. It does prevent simply asserting an `O(1)` oscillation on that ball. For example, the one-dimensional function

```
F_x(t)=x t^2/2 + x e^(-mu d)(sqrt(t^2+x^(-1))-x^(-1/2))
```

has `F_x''>=x` and `|(F_x-x t^2/2)'|<=x e^(-mu d)`, but its rise at `t=x^(-1/2)` is `1/2+(sqrt(2)-1)sqrt(x)e^(-mu d)`. This is an explicit test of the asserted analytic inference, not a constructed Wilson marginal.

What S1 lacks is the application of the displayed repair to its actual `F(.|omega)`, on a ball contained in the same admissible conditional support, with a lower bound on its reference density. Mapped Text 5.3's local OS construction (`638–656`) fixes lower fields on a particular set `Omega`, requires clearance for the outer measure to be independent of the varied parent, and estimates `Inner` through a gas and its rarity input. It does not assert that arbitrary conditioning on the lower site data in S1 preserves `(I_k)` with the same constants on the proposed ball. Conditioning is legitimate; preservation of estimates is a separate assertion. The identity `P(E)=E[P(E|omega)]` only helps after a uniform conditional bound has been proved. In addition, the OS construction makes its frozen set a union of whole boxes; S1's removal of fixed-width collars has not verified that admission condition.

### Defect 2: EX has an unpaid entropy term on the chosen clusters

Even granting an admissible ball and the preceding upper bound, EX gives

```
log P(Q|data) <= -gain + [f_D-F(V°)] + log[m(Q)/m(D)].
```

On a fixed `n`-dimensional chart with controlled Haar/coarea density, a radius `x^(-1/2)` ball costs at least the bookkeeping term `(n/2)log x-log vol(B_1^n)` plus the density constants. A fixed patch can pay this at large enough `x`. The note switches to an arbitrarily large connected cluster at the end of line 80, while the displayed gain in line 78 pays one mark and includes a negative `C n`. No bound relating that `n` to an additive number of paid marks is proved. A fixed `x_*` cannot absorb `C n` for one fixed mark and arbitrary `n`.

There is also a defect even if an extensive gain were supplied but the single Euclidean ball were retained. For `n=2r`, iterated polar integration gives `vol(B_1^{2r})=pi^r/r!`; hence its inverse has logarithm at least `(r/2)log(r/2)-r log pi` (retain the largest `r/2` factors of `r!`). This produces `n log n`, not just a fixed cost per mark. The explicit quadratic chart `F(v)=x||v||^2/2` on `[-1,1]^n`, with `Q={v_1>=a}`, already makes the stated one-ball EX estimate useless at fixed `x` as `n` grows, although its actual one-coordinate tail is well behaved. This refutes the entropy absorption argument, not the desired Wilson probability bound.

The product extension after EX is valid **if** one constructs a common admissible product denominator, a product/disintegrated reference measure with the stated volume bounds, and a telescoping gain uniform under the other replacements. Disjoint patches alone do not establish any of these on a hard-parent fibre. RANK is an upper parent-window bound; it supplies no lower denominator volume on a different label fibre. Possible repair: fixed local boxes, relative integral comparisons, and an additive cluster gain/entropy estimate. These are obligations, not consequences of (2.1).

### Defect 3: F-D is not the missing multiplier/label comparison

F-D bounds an inverse linearized operator at an admitted stationary background. It does not bound the first derivative of the minimum as the constraint changes. The distinction is explicit in the constrained quadratic example

```
A(u,v)=u^2/2+M v,       constraint v=w.
u_min=0,   fibre Hessian=1,   minimum=M w,   lambda=M.
```

The inverse bound is independent of arbitrary `M`; the multiplier is not. This is a counterexample to the generic inference “by F-D,” not to a Wilson-specific multiplier theorem.

The actual source `c0-loc:999–1048,1245–1251` requires stationarity, smooth class constraints, a curvature bound and a mean-preserving test bump to obtain its multiplier estimate. Rough rerouted constraints and another logarithm branch are explicitly outside its domain. S1 must construct a path of admitted class minima with the same exterior, prove its multiplier bound along that path, and bound the change of parent constraints in the appropriate summed norms. None follows merely from the inverse estimate. The assertion that replacing a rough hull by a class fill *lowers* its action while preserving the needed comparison is another unsupplied energy comparison. The hypotheses of a fill are not minimality of that fill.

The proposed loss `C T |Delta|+C|Delta|^2` also needs a small coefficient relative to the *paid number* of marks. Counting changed lines is not that estimate until hull size, the normalization of the average, and multiplicity of changed parents are fixed. This is not repaired by removing the word “restoration”: different label fibres still have to be compared.

## 2. RANK, privacy, and (JW)

**Verdicts:** privacy of a face bond, **ADVANCE** on the specified block geometry; the asserted exact factorization, **CORRECT-NO-ADVANCE** (replace it by sectionwise bounds); the global estimate (2.4) and the claimed settlement of (JW), **CORRECT-NO-ADVANCE**. I do not have a counterexample to (JW) for the actual covariant kernel.

### Defect 4: the proof has not justified its logarithm chart or global inverse

The privacy argument itself survives the attack. A crossing bond is in neither block's internal contour. A straight segment of length `L` starting in the preceding block stops before that crossing bond, and one starting in the succeeding block starts after it. Only the intervening parent's row reads it. On a transverse column whose entire length read by these segments avoids the hull, the `L` longitudinal starting points give `s_c=L`; partial survival of a column alone would not imply this count. This is a geometric statement about a **fixed** pattern, not independence of labels. The indicator `1_K` still couples selected variables through plaquette conditions. Its integral need not factor. Uniform upper bounds on each section, followed by iterated integration, would give the desired product without exact factorization.

The crucial next sentence in line 44 is not valid for the uncentred logarithm formula printed there: closeness of the line holonomies to one another and smallness of `exp(avg log ell_x)` do not force the individual principal logarithms to be small. Here is the explicit SU(2) failure of that inference. Put `tau=diag(i,-i)` and take equal numbers of

```
ell_+=exp((pi-delta)tau),   ell_-=exp(-(pi-delta)tau),
                 0<2delta<theta_0.
```

Their group distance is `2delta`, their principal logarithms average to zero, and the displayed parent is identity. Each line has angle `pi-delta`, not at most `1/2`. Prefix rotations can be identical in this one-row calculation. Thus the quoted small-angle inference is **WRONG for the formula used to prove it**. This is an explicit branch-cut example for that analytic step; it is not being passed off as a proof that these row data lie on the entire lattice kernel's (JW) support.

The distinction matters here: the mapped class construction actually compares displaced-path **loops** with a reference path `Omega_0` and forms a link `exp(A)Omega_0` (`c0-loc:194–204`). It is not in general the uncentred formula above. A coherent relative-log definition can exclude the example, but then the proof must use that definition, include the reference-path derivative, and show its validity on the *whole* rough-pattern support. Importing only the flat chart is insufficient. Small plaquette flux controls differences of paths with an exhibited spanning surface; it does not alone fix an open-path logarithm branch.

There is a second check on the displayed differential. With the angle convention of the note, left-trivializing the derivative of `log` at `exp(theta tau_3)` gives on the transverse plane

```
Dlog = theta cot(theta) I +/- theta J,   J^2=-I.
```

To check it, differentiate `exp(v)=cos|v|+(sin|v|/|v|)v` in a direction perpendicular to `tau_3`, then multiply on the right by `exp(-theta tau_3)`. The differential of exp is `(sin theta/theta)` times a rotation by `theta`; invert it. Consequently

```
||Dlog-I|| = sqrt((theta cot theta-1)^2+theta^2) >= |theta|.
```

At `theta=1/2`, the asserted `1/4` bound is false. In exponential coordinates for the varying bond there is also a `dexp_xi` factor. These are locally repairable constants on a *specified* smaller chart; they are not a counterexample to a bound with another absolute `C` in (2.4).

Finally, a derivative bound only on `K` does not prove injectivity on its enclosing ball. The line segment used to compare two points must stay in a single logarithm chart where that bound holds. One can repair this locally by proving a derivative uniformly close to one fixed invertible map on the entire ball. Then integrating the derivative along the segment proves a lower Lipschitz bound and injectivity, and a Jacobian estimate yields the volume bound. Those hypotheses, including the treatment of all sheets, are not written for the full support here.

For the one-bond core, the suggested detour around a ball is a promising way to supply the common-frame estimates. The note only asserts the area estimate, and the required log-branch identification and global preimage argument are still missing even if that area estimate is granted. Thus `P(l_0|U)<=1_K` is correct, and a valid (2.4) **would** imply (JW), but the quoted proof does not settle (JW). The more general hull case remains an additional geometric obligation. None of this supplies the lower fibre volume used in S1.

## 3. S4 first: what exclusion actually does

**Verdicts:** the fixed-pattern, omitted-bond independence is **ADVANCE**; the statement that a sparse hole has *zero influence on the parent* across the configurations/patterns required by the recursion is **WRONG**; derivation of (4.1) is **CORRECT-NO-ADVANCE**. The scalar recursion, *if supplied with a base*, is **ADVANCE**.

### Defect 5: exclusion changes the average; it is not absorption

Here is the exact elementary failure, within the commuting subgroup of SU(2), away from every logarithm cut. Let a parent have `N` lines. A sparse hull deletes `r` of them, with `0<r<N/2`. Use signed logarithm coordinates `theta` along `tau`; if these coordinates have means `a_H` on the deleted set and `a_R` on the survivors, then

```
theta(M_0)=(1-r/N)a_R+(r/N)a_H,
theta(M_l)=a_R,
theta(M_l)-theta(M_0)=(r/N)(a_R-a_H).
```

This is nonzero when the two means differ, however small all angles are. It is realized by a lattice bond variation, not an independent-line fiction. Start with identity links except one bond `exp(a tau)`, where `T<a<2T` and `0<chi(a)<1`. Its incident cells form a fixed finite sparse core (take the stipulated large `m_*` above that number). Place it near a block face, so its hull collar contains a crossing bond e whose incident plaquettes do not meet the core bond. Keep the hull small compared with L, so the parent is retained. All straight lines through e are excluded, while e belongs to no internal block contour. Set `U(e)=exp(t tau)`, with `|t|<T`, and keep all other links fixed. Only the core cells can carry labels; both the all-zero pattern and the pattern labelling that core have positive weight throughout this interval. The all-lines parent reads e on `L` starting lines, so its signed angle changes by `t/L^3`; the retained-line parent reads none and does not change. Other parent rows do not read e, by privacy. Thus the difference of these two maps has derivative `-1/L^3`, and cannot be identically zero: two distinct choices of t cannot both have zero difference. This explicitly refutes zero influence across admissible sparse patterns; it does not by itself refute the probabilistic inequality (4.1).

A nonzero displacement can also cross a sharp threshold if the original parent is sufficiently close to it. To turn that observation into a *non-rare* probability counterexample would require its energy and conditional mass, which are not supplied here. Conversely, to prove (4.1), S1/S2 must pay the displaced near-threshold configurations uniformly in the retained holes. They have not done so. The issue is not repaired by declaring the holes exterior: the exterior determines the surviving subsets and the constraints of the conditional problem.

This distinction is already visible in the permitted mapped source `relative-density-bound:361–369`: exclusion produces a correction `M` bounded by `C_Delta rho' T/L`, rather than zero. I use the elementary face-bond calculation above, not that source's numerical checks or its unrebuilt deformation theorem, as the explicit failure. Mixed plaquettes also retain dependence on fixed hole data after a delta constraint ceases to read the omitted bonds.

The power `m_*` therefore needs a separate exhaustive alternative: every unpriced exit must require at least `m_*` *jointly priced* children. A bound on a one-cell supremum does not give this joint event. The definition of `p_k` must also exclude conditioning on the very hole being tested and specify compatible parent/data supports. If those issues were repaired and

```
p_k<=z_k+C_L p_(k-1)^m,   z_k=e^(-a x_k),
p_0<=2z_0,   x_(k-1)>=x_k-b,   m>=2,
```

were genuinely supplied, then `p_(k-1)<=2z_(k-1)` gives an error at most

```
C_L 2^m exp(a m b) z_k^m.
```

It is at most `z_k` for all `x_k>=x_*` once `C_L 2^m exp(a m b) exp(-a(m-1)x_*)<=1`. That calculation has no factor per level. The missing part is the probabilistic premise, not this arithmetic.

Proposition HOLES (`explicit-region-two-step:73–85`) concerns the existence of fine defects under a top cell and the failure of carrying every fine hole as a persistent ancestor hole. It does **not** assert that every such top field is rough. It therefore neither disproves (4.1) nor gets “defeated” by excluding some lines. Its proof conditions on nonincident links, multiplies the absence probabilities, and inserts the flow upper bound. Once a lower probability `q` is granted, `(1-q)^n<=exp(-nq)` gives the stated growth. A replacement for persistent regions still needs a bound on the residual field-dependent influence after absorption; `explicit-region-two-step:154–159` explicitly leaves that task in (GAS2). Rarity-c has not supplied it by a zero-influence assertion.

## 4. S3(c): PER is sound; its application is not supplied

**Verdicts:** Lemma PER, **ADVANCE** as a conditional elementary lemma; `(SEC_m)` from the named inputs, **CORRECT-NO-ADVANCE**; availability of `(ADD_m)` in the form used here, **CORRECT-NO-ADVANCE**. No counterexample to the actual sector-value inequality is claimed.

The PER proof can be checked term by term. Put `D=Phi(a',omega)-Phi(a,omega)`. Translate the changed box in each telescoping increment back to the reference box. Its exterior may differ arbitrarily, which is precisely allowed by (2.5). Each of the `N` increments differs from `D` by at most `eps`. Thus `|ND|<=|Phi(Psi_N)-Phi(Psi_0)|+N eps<=2Bn+N eps`. No path between sectors is used. This is an implication from a *value* comparison uniform over exteriors; a derivative-locality estimate cannot replace (2.5).

### Defect 6: global class values and the cited shell statement do not give this regional jump

Theorem VAL is explicitly an implication from SRC and Prop GS (`sector-values:234–238`). It bounds `R_m` on a **globally class** field by its whole-torus gradient energy, cubic-energy bound and toron term. For two globally class fields one may already apply its triangle inequality. The new content of `(SEC_m)` is a localized difference uniform over a possibly rough exterior, with holes and a change of sector. VAL does not say this.

To apply PER as proposed, one must construct the copies `Psi_j` inside its domain. Agreement of `W,W'` on their common collar does not say that collar is flat, or give a class extension of it to the proposed flat exterior. A construction must bound the added collar energy and seam energy and preserve the required flux margin. If those copies exist with a controlled local energy bracket, VAL and genuine exterior-independent increments would indeed give a local difference bound. A crude bound `Bn/N` with `n/N` of order the volume of a collar of thickness `C log(x|Q|)` does not by itself give the printed, `x`-independent `B'` and energy bracket. The added energy and the toron term must be estimated in that same bound.

The particular citation for `(ADD_m)` has materially narrower quantifiers. Mapped Prop MD (`666–680`) has separated holes, a positive regular crossing distance, a shell-size/rate restriction, and a small-error regime. Its Step 3 first freezes the interior polymers and **discards** patterns with insufficient regular crossing length using (A1). Equation (680) applies to the remaining configurations. It is not a pointwise decomposition for every `p,m,q` and arbitrary holes. For example, a chain of holes crossing the shell has `D_r=0`; the stated MD bound then supplies no small error at any collar thickness. S3(c)'s “a hole inside J is kept” provides neither the separation nor a regular shell around it. Rarity of an excluded pattern cannot justify a uniform estimate after conditioning on that pattern. The MD recursion also uses lower-level rarity; replacing its producer requires a level-by-level dependency check, not declaring ADD an unconditional regular input.

There are independent competitor obligations. Theorem S and F2-mult (`fill-cubical-extension:296–359`) extend prescribed links with a bounded flux, potentially enlarged by `C_a`, and localize the change. Their conclusions do not prescribe removal of a chosen topological lump, a particular change of sector, the same multilevel parents, or a signed decrease in action. They therefore do not justify “each intermediate field exists by (F2)” with all the properties S3(c) uses. Nor is the stated `2 pi^2(1-small)` *difference* proved by merely naming the energy of a lump: the two admissible competitors and their common data must first be constructed and compared. I import no continuum instanton or topological-energy theorem from memory to fill this gap.

Thus the region clause cannot be bypassed by the printed argument. A new localized value-difference theorem might bypass its particular formulation, but PER does not manufacture that theorem's filling and near-additivity hypotheses.

## 5. S2 and S3(a,b): coverage of the full law

**Verdicts:** S2, **CORRECT-NO-ADVANCE**; S3's bounded descent, **CORRECT-NO-ADVANCE**; S3(a)'s asserted uniform pattern-sum bound, **WRONG**; S3(b)'s payment by a joint lower-level event, **CORRECT-NO-ADVANCE**. These are independent of the sector issue above.

### Defect 7: the case split does not supply its missing branches or uniform costs

In S2 the elementary size estimate on a radius-`CL` patch is harmless *if* every read plaquette has flux at most `LT_2`: there are `C(L)` plaquettes and `1-cos t<=t^2/2`, so taking `a_*` small bounds that patch energy. The subsequent expansion would be useful on an admitted chart about a stationary minimizer with the claimed small flux. But S2 has not supplied that minimizer for its holes/exterior, the relative chart or the uniform branch density formula on all parents with flux up to `LT_2`. `(I_k)` for the full density on class parents does not imply the same formula for the partial density `rho_k^cl` at nonclass parents. The lift estimate `(R3)` is an estimate for an admitted constructed lift, not an identity for the full restricted integral. The assertion that class parents make every indicated rough oscillation nonstationary also needs the actual constrained boundary problem. S1's unresolved comparison is being reused, not proved here.

S3's bounded descent cites the wrong bound. The actual row (f) is in Section **4**, `explicit-region-two-step:154`, and gives age at most

```
log_L(diam gamma)+h_max,
```

conditional on `(PF)` and unless a new exit occurs. It does not give `h<=h_max` for arbitrary clusters. Moreover, an averaging relation does not upper-bound each child flux by the parent flux divided by `L^2`: in the commuting case opposite fine contributions can cancel in the parent while remaining nonzero in the children. A lift estimate is not a property of every field in its fibre. A bounded descent, or an alternative accounting for each new exit and the diameter, is still needed.

The explicit arithmetic failure in S3(a), line 86, is

```
(1+p)^|G| <= 2.
```

For any fixed `p>0`, choose an integer `|G|>1/p`. The binomial expansion gives `(1+p)^|G|>=1+|G|p>2`. Such large clusters are not excluded by S1's choice of P. The product-odds sum is attained in the elementary model of independent holes with odds `p`, so a product bound alone cannot improve this conclusion. A normalized integration over unchanged holes might cancel their sum, or `exp(p|G|)` might be absorbed in an extensive gain; neither is written. This is a counterexample to the printed uniform bound, not to Wilson rarity.

Dense children can pay a Haar branch **if** their joint probability is bounded with the correct conditional law and each paid child is counted with bounded multiplicity. Applying EX to their union is not a substitute for these properties (Defect 2). The separate kernel rule that a parent becomes Haar if fewer than half its lines survive must also be covered by the dense-charge geometry; “dense boxes are Haar” alone is not its converse. The finite Haar-plateau observation is a useful warning: a full marginal cannot be assigned an arbitrary `x f^2` price merely from its displayed parent flux.

## 6. S5: an exact identity is not the multilevel induction

**Verdict: CORRECT-NO-ADVANCE.** The identity used on the class part is **ADVANCE**, conditional only on the densities/disintegrations being defined on the same fibre.

### Defect 8: the rough part still needs joint accounting, and no energy can be spent twice

The equality `exp(-F_i^M+F_i)=Q_(i-1)` is just the definition of the marked integral divided by the unmarked integral. Where the induction hypothesis applies, its factor can be pulled through the remaining positive integral with coefficient one. This is the valid point of DM Step 3(a) (`quiet-boundary-rarity:119–121`). It does not estimate the complementary rough-parent contribution.

The cited charging paragraph QB:143 states why a *type-I* mark with a hull or nonregular parent has no patch gain, bounds the number of such charges using disjoint patches, and spends an explicitly reserved energy term in its stronger producer. S5 does not inherit that reserved term after discarding the producer. It also claims arbitrary multilevel marks, including type-II marks. It must give an injective or bounded-multiplicity assignment of unpaid marks to genuinely priced events, maintain compatible conditional supports under each exposure, and reserve enough of each rate for all assigned marks. The assertions about `x f^2`, `m_*` and `L^4` do not give such an assignment. In particular a flux-squared price for the **full** rough marginal is not among the inputs and is explicitly limited by S3(b)'s Haar plateau; using a restricted non-Haar branch would require a separate bound and subsequent branch sum.

The logical obstruction is explicit. Let a single event B of probability `q` force one marked event at each of `s` levels. Every one-level marginal is `q`; a regular-parent branch can have zero marked probability; but the intersection is still `q`, not `q^(s/C_R)` when `s>C_R`. This finite probability example is not asserted to be a Wilson history. It shows precisely what the class-part identity and one-level prices fail to control. A proof for this kernel must rule out that reuse of one price by a quantitative multilevel argument. S3's unsupplied bounded descent and S4's unsupported recursion do not do so. No product (4.2) or depth-uniform `C_R` is established.

## 7. S6: the terminal level remains a separate base case

**Verdict: CORRECT-NO-ADVANCE.** Avoiding chessboard is a permissible strategy. The failed centre-plane reflection argument does not refute this strategy.

### Defect 9: EX at K has no supplied gain or denominator

At level K there is indeed no parent constraint, and EX remains an elementary probability inequality. But S1–S3 use regular parents, a constrained lift, fibre coercivity and branch comparisons. Removing the parent does not supply their unconditioned replacements. The top density is `F_K`, whose rough part the note explicitly leaves unbounded (`rarity-fresh-c:60`); it is not the bare Wilson action merely because no next blocking is performed. One still needs a top-level marked integral comparison, with its admissible denominator, uniform in the exterior, and then the joint accounting for marks below it. No outgoing level-K label should be invented in doing this.

There is no inference from “EX holds” to “(4.2) holds.” For example, EX is equally valid for a uniform law and an event of probability one half, at any externally named parameter x; it produces no exponential decay without a growing action difference. This is a direct test of that logical inference, not an example of the actual `F_K`. A proved uniform top comparison could replace chessboard; none is supplied here.

## 8. Do S1–S3 supply (SEP), and at what rate?

**Verdict: CORRECT-NO-ADVANCE; no positive (SEP) rate has been established.** The nominal rates in rarity-c are `c_I x_l eps_q^2 T^2` and `c_II x_l T^2`, followed by an unproved bounded-multiplicity loss `1/C_R`. At a *fixed finite geometry*, a valid comparison with those gains and only subexponential prefactors would retain action rates `c_I eps_q^2 T^2/C_R` and `c_II T^2/C_R` as the bare coupling tends to infinity, provided `x_l/t->1`. These are conditional candidate rates, not outputs of S1–S3.

The precise distinction can be checked without a saddle theorem. For a positive finite base measure on a sector D, let `m(D)=ess inf_D A`. For every `eta>0`, the set `A<m(D)+eta` has some positive measure `b_eta`; hence

```
b_eta e^(-t(m(D)+eta)) <= W_t(D) <= nu(D)e^(-t m(D)).
```

Taking logarithms, dividing by `-t`, and then sending `t` to infinity and `eta` to zero gives the limit in rarity-x (3.1). A full-law marked probability estimate therefore implies only

```
m(all requested marks)-m(all histories) >= the limiting mark rate.
```

(SEP) instead compares `m(D)` with `m(D\gamma)` for **every residual active pattern**, using the same top/data and positive essential supports. S1's minimizer is not proved to have that residual pattern. Changing a label, its parent map, a lump's sector, or a tower can change other predicates. Neither a lower denominator ball somewhere in the full fibre nor a sum over unchanged holes proves compatible deletion.

An explicit finite positive example separates the two logical claims. Take two disconnected test vertices a,b, one unit of base mass in each of the four sectors, and actions

```
A(empty)=0,  A({a})=1,  A({b})=100,  A({a,b})=2.
```

For `t>=2 log 2`, the probability of each single marked event is at most `e^(-t/2)`, and the joint event has probability at most `e^(-2t)<=e^(-t)`. Thus a full-law product bound with rate `1/2` per mark holds. But deleting the component `{a}` from `{a,b}` gives

```
m({a,b})-m({b})=2-100=-98,
W_t({a,b})/W_t({b})=e^(98t).
```

(SEP) fails. This is a counterexample to the implication from full-law product rarity to same-pattern deletion, not a Wilson configuration. It explains why even repairing S1–S6 would not automatically settle the stronger requirement selected by rarity-x.

The two routes share an objective—integrate finer fields before pricing own-level defects—and neither needs the rejected centre-plane chessboard as a logical prerequisite. They differ at the comparison they must prove. Rarity-c seeks conditional patch/branch comparisons with holes held as exterior, then a recursion and charging scheme. Rarity-x keeps an exact positive partition by the entire active set and explicitly asks for a relative mass bound between a sector and that same sector with one connected component deleted. The latter exposes both the constrained action separation and the relative fluctuation factor. Rarity-c has not supplied either at that scope. Its appeal to resolved wells is a proposed way to control a conditional law; rarity-x's two-branch calculation (3.3) correctly warns that this cannot be transferred to the full mixture without comparing branch masses. Neither route, as supplied here, closes its full-mass producer, its mu clause, or the boundary-data consumer (MD*).

## 9. The remaining auxiliary calculation: FC

For completeness, every line of the FC proof (`rarity-fresh-c:24–36`) can be checked under its stated differential hypotheses, with `B I` understood as an operator upper bound and divergence defined relative to m. Compact support inside O makes integration by parts legitimate even if F is not smooth elsewhere:

```
E[Xg]=E[g(XF-div_m X)].
```

Taking `g=1` gives `E Y=0`. For `X_t=sum t_i X_i`, the antisymmetric part of `(X_iY_j)` drops out of `X_tY_t`; thus `X_tY_t<=B|t|^2`. With `phi(s)=log E exp(sY_t)`, integration by parts gives `phi'(s)<=sB|t|^2` for `s>=0`. Integrate from zero to one. Completing the square in a normalized Gaussian integral gives `exp(a|Y|^2)=E_g exp(sqrt(2a)<g,Y>)`. Positivity permits interchange of integrals, and rescaling each Gaussian coordinate gives `(1-2aB)^(-N/2)`. A subfamily has the same operator bound. Applying the exponential Markov inequality at `a=1/(4B)` proves the printed product tail. No convexity is used.

At level zero, a left-invariant field on one link has zero Haar divergence. On a plaquette, a directional second derivative is bounded above in absolute value by `(sum_{b in p}|t_b|)^2<=4 sum_{b in p}|t_b|^2`; a link belongs to six plaquettes in four dimensions. Summation gives `B=24x`. There are three Lie algebra coordinates per selected link, and `Y=x grad A`, so (2.2) gives exactly the coefficient `x/96` and factor `2^(3|S|/2)` in (2.3). Fixing the other links changes none of those counts.

The claim that this prices “every pack” additionally needs `sum f_b^2` bounded below by the stated number and amplitude of its pairs. It is not a consequence of FC without that deterministic inequality; stationarity makes every force zero regardless of whether the action is minimal. I have not imported an unproved identification of that pack with its force. The note correctly does not use FC in S1–S6. The sign of `-Cov` in a differentiated marginal is also correct; it supplies no missing uniform upper bound on the remaining mean Hessian or on moving-domain terms.

## 10. Reading boundary and completed disposition

The source of every mathematical assertion assessed here is the requested commit. Read first: `GOAL.md:1–79` and `FINISH.md:145–174`. The queue and standing rows around item 58 were then located. `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent from this checkout; no branch was fetched or substituted for the pinned source. The local physics-claim-reviewer skill was inspected for applicable proof-checking questions; no audit, landing workflow, delegation, or model switch was invoked.

The complete target argument `library/rarity-fresh-c.md:1–179` was read in bounded ranges. Necessary bounded supporting reads were:

- `parts/hard-core--mapped.md`: Text 3.1; the density/one-step definitions at 562–579; Texts 5.1–5.3, especially the kernel at 604–614, local OS at 636–662 and MD at 664–688; short source-identification/order searches. These were checked as statements with their conditions, not accepted by their labels.
- `library/one-window.md`: Sections 4–5, including the full (JW) statement, the fixed-torus chart and its limitations; bounded searches for the multilevel/conditional distinction.
- `library/explicit-region-two-step.md`: TYP/RARE/HOLES, chart hypotheses and concentration comparison, and the two-step rows through the bounded-age/absorption discussion. No numerical results were used as proof.
- `library/sector-values.md`: Theorem VAL, `(Loc^c)` and the region clause at 232–270; heading/dependency searches. SRC, GS and FALL were not re-proved or granted closed status.
- `library/c0-loc.md`: common-frame/path definitions at 120–208 and 215–258; stationary hypotheses at 910–934, multiplier and admission boundary at 995–1071, and F-D/identification limits at 1185–1266. The full fan and local-lift proofs were not re-reviewed.
- `library/quiet-boundary-rarity.md`: the quiet/ST/geometry/reference definitions at 15–75, and DM's statement, proof and charging clause at 97–149. Existing gate verdicts quoted there were not used as mathematical evidence.
- `library/fill-supply.md:118–174`; `library/fill-cubical-extension.md:296–359`; `library/relative-density-bound.md:325–371`, plus bounded searches for the kernel's geometry. The unrebuilt deformation step in the latter was not used.
- `library/rarity-fresh-x.md:1–159`: probability contract, exact partition, (CD), (SEP), and the two-branch calculation. This was read after rarity-c's own proofs. Its later counting argument was not needed and was not reviewed.

Some initial multi-file searches returned truncated output; those were only location searches. Every decisive passage used above was subsequently retrieved in a bounded, untruncated range. No forbidden independent-side file, gate on that attempt, history-budget/compute-inventory/strategy gate, or excluded library file was opened. Incidental references to them in allowed source text were not followed. No outside literature or Sussman–Alpoge source was imported. No theorem from memory supplies a missing step.

Only this report was written. The usable new conclusions of this reading are the checked elementary comparisons (EX, PER, FC), the fixed-pattern privacy calculation, and the diagnosis of the named gaps and explicit false intermediate assertions. The first failed route step remains S1's conditional comparison, not merely its later multiplier sentence. Final rarity, (SEP), (JW), and the proposed bypass of the region/chessboard producers receive no proved status from this report.
