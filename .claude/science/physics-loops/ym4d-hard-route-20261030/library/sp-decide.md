# The two-step sparse-crossing action gap
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured reasoning effort are not exposed; queue requests max); commit `56dbbda919d1eb9890cab641685a720009dfd466`; research text, not an audit, grants no status.

## 1. Scope and first obstruction to a counterexample

**Discharged — source identity and method.** This checkout has the requested HEAD. GOAL and FINISH's independence, efficiency and rules sections were read first. The repository entry point's `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent from this checkout; no other revision substitutes for it. Only this file is written. Source reads and file checks are bookkeeping, not proof. No numerical calculation, search over configurations, external literature, audit or subagent is used. No theorem recalled from memory is admitted as a premise.

**Gap — the question being decided.** Use exactly the two-step coupling-free history measure `nu`, event `E_h`, windows `B_w`, fixed geometry and positive-support indexing in `rarity-repair.md`, Section 7. In particular, the denominator includes every supported label branch. Define `a_all(w)` and `a_exit(w)` by essential infima under restrictions of that same measure. The question is whether their difference has a strictly positive infimum over the nonempty numerator windows. Literal singleton-hull admission and the actual non-quiet predicate are part of the question.

**Discharged — a supported exit cannot lie below the full essential minimum.** If `a = ess inf_{B_w} A`, then `nu(B_w intersect {A<a})=0`: write this set as the countable union of `{A<a-1/n}`. Intersecting a null set with `E_h` still gives a null set. Hence `a_exit(w)>=a_all(w)`. A refutation must approach equality on positive-measure sets (possibly with varying `w`); a low-action isolated configuration is insufficient. This rules out the suggested “below” alternative at the level of essential infima, without deciding strict positivity.

## 2. Relaxing the face construction: an actual interval is settled

**Implication — exact face action, conditional only on the geometric admission in (2.1a).** Write the crossing-face angles as `a(z)`, where `z` ranges over its transverse cube `S` of side `L`, and extend `a` by zero outside `S`. Keep all other fine bonds equal to identity, as in that construction. Commutativity gives, with each unoriented plaquette counted once,

    A_face(a) = sum_{z in the transverse torus, j=2,3,4}
                         [1-cos(a(z+e_j)-a(z))].            (2.1)

Indeed a `(1,j)` plaquette on the crossing plane reads the two crossing bonds with opposite signs; all other plaquettes are identity. If `D` is the set of the `k` deleted columns, the two parent angles are exactly

    a_0 = L^(-3) sum_S a(z),
    a_h = (L^3-k)^(-1) sum_{S\D} a(z).                       (2.2)

All internal contours are identity even when rerouted inside their blocks. In particular the deleted values are free variables of the retained-line constraint, not prescribed data. The source's choice `a_h=v=T+qD_0/2`, `q=k/L^3`, `D_0=d-(d+beta)/k` has a large artificial face cost: at least `6L^2-6k` boundary plaquettes have angle `v`, so

    A_face >= (6L^2-6k)(1-cos v),                            (2.3)

when `k<L^2`. The count subtracts at most six boundary faces for each deleted column; the full transverse cube has `6L^2` boundary faces. This is a lower bound for that prescribed face, not for all relaxed histories.

**Discharged — the unavoidable absolute cost after arbitrary relaxation.** Positive weight of the label at `h` requires `flux_h>T`, since `chi=0` on `[0,T]`. Thus some fine plaquette has angle greater than `T`. For `0<T<=1`, integration of `cos s>=1-s^2/2` gives `sin s>=s-s^3/6`, and a second integration gives

    1-cos T >= T^2/2-T^4/24 >= 11T^2/24.                    (2.4)

The preliminary cosine inequality follows by integrating `sin s<=s`, itself obtained from `cos s<=1`. Monotonicity of `1-cos` on `[0,pi]` and nonnegativity of all other terms imply `a_exit(w)>=11T^2/24`. Releasing every face field and every other fine bond cannot remove this absolute bound. It does not subtract the denominator's minimum.

**Discharged — a zero-action denominator in the small windows, with the scale condition displayed.** Let `v` be the retained parent angle in the admitted construction defining `W_*`; thus `v<9T/8`. Its level-1 field has one nonidentity bond. At the next, all-zero-label step, in this commuting chart the exact angle field is

    theta(W_*) = b + d psi,       |b(e)|<=v/L^3.             (2.5)

Here `b=Q_path theta(V_1)`. The gradient is the contour term in mapped Text 3.1: averaging the contour in a block gives one number at that block's centre, so the two endpoint terms subtract. Each input bond occurs on at most `L` of the `L^4` starting lines, proving the bound on `b`. Relative logarithms have no correction in the stipulated commuting small branch.

Let `G` be the pure-gauge top with angle field `d psi`. Extend its vertex gauges to the fine vertices arbitrarily. The resulting fine pure-gauge field has action zero, every label is zero with weight one, and its two-step top is `G`: path products telescope, and gauge covariance restricts the gauge to successive centres. Consequently

    dist(G(e), W(w)(e)) <= v/L^3 + w                        (2.6)

on the changed bond, and at most `v/L^3` on every other bond. Assume `L^3>=450`, a concrete sufficient large-scale condition (in particular `L>=9` suffices). Then `v/L^3<T/400=epsilon/4`. For every `0<=w<=epsilon/2`, `G` lies strictly inside `B_w`. No parameter is changed: without that sufficient condition the exact criterion is `w+v/L^3<epsilon`.

This is also an essential-support argument. In a sufficiently small open neighbourhood of this fine pure-gauge field, all fine and level-1 fluxes stay below `T`, both kernels use their all-zero branch, and the top remains inside the open window. Fine product Haar assigns positive measure to every such neighbourhood. To check this without a density theorem, translates of a nonempty open set cover a compact group by finitely many translates; invariance and total mass one rule out zero measure. The same applies to the finite product of link groups. Continuity of the action supplies neighbourhoods with action arbitrarily close to zero. Therefore

    a_all(w)=0,
    a_exit(w)-a_all(w)>=11T^2/24
        for 0<=w<=epsilon/2 with nonempty numerator.         (2.7)

This proves a genuine part of (SP) for the original measure, without conditioning on the face fields. In particular arbitrary relaxation of (2.1a) inside these windows cannot supply a counterexample. No statement about nonempty support is inferred when the singleton hull or non-quiet admission fails.

## 3. The lift margin at these windows, with its admission boundary

**Discharged — the top-flux arithmetic.** Put `rho=T_2/T>=2`. Taking the curl in (2.5) gives `flux(W_*)<=4v/L^3`. Multiplying the changed top bond by `exp(w tau)` changes each incident plaquette angle by at most `w`. Changing four links by less than `epsilon` changes a plaquette angle by less than `4epsilon`, by repeated use of the bi-invariant triangle inequality. Thus, throughout every actual window in Section 7,

    flux(V_2) < 4v/L^3 + T_2/4 + 4epsilon
              <= T_2/4 + T/20 <= (11/40)T_2,                (3.1)

using `L^3>=450`. The endpoint `w=T_2/4` is included. The windows have substantially more margin than merely `flux<T_2`.

**Implication — the advertised regular lift would have margin `149T/160`.** The source threshold choice is `C_s L^(-kappa) T_2<=T/4` (`hard-core--threshold.md:145–155`). If the stated lift estimate `flux(Lift V)<=C_s L^(-kappa) flux(V)` is available for the particular stationary lift on all of (3.1), then

    flux(Lift V_2) <= (11/40)(T/4)=11T/160 < T.             (3.2)

The version using mapped (R3) has the same arithmetic when `C_r T_2/L<=T/4`. This check uses the full window radius, not only its centre. It leaves no threshold-arithmetic mechanism by which an admitted regular lift already reaches `T`.

**Gap — this does not identify either essential minimum.** Mapped (R2), lines 740–742, constructs a critical point and uniqueness in a stated ball, conditionally on its inverse and trial inputs. (R3), lines 744–752, concerns that constructed reference. `c0-loc.md:1043–1049,1245–1251` explicitly leaves minimum/chart existence and identification as inputs, and excludes rough rerouted contours. Neither argument proves that the unrestricted denominator minimum is that lift, or that the minimum with the actual `h`-excluded constraints has (3.2). The latter minimum can move even when the all-lines reference has ample margin. The arithmetic in (3.2) is an implication, not a discharged regularity theorem for the actual minimizers.

## 4. The excluded-line minimum: what a signed repair must pay

**Discharged — additional denominator branches help a lower-gap proof.** One need not identify the full denominator minimum with the regular lift. If an all-zero-label reference `U_0` has a top strictly in `B_w`, and its fine and intermediate fluxes are strictly below `T`, continuity and the Haar argument in Section 2 give `a_all(w)<=A(U_0)`. Other supported branches can only lower `a_all`. Thus a signed comparison against an admitted regular reference would suffice. Conversely, undercutting that reference alone would not refute (SP): a still lower denominator branch could remain.

**Discharged — the missing sign cannot be omitted.** For a fixed exact top `V`, extend the fixed-pattern map with the literal hull `h` to its coherent logarithm domain before imposing its label probabilities. Let `m_h(V)` be its action infimum on that domain, and let `m_0(V)` be the value of an admitted all-lines reference. Then the exact identity is

    A(U)-m_0(V) = [A(U)-m_h(V)] + [m_h(V)-m_0(V)].           (4.1)

The first infimum can include fields with zero weight for the label `h`; using it as a lower bound is legitimate. Using such a field as a supported denominator history is not. Both the positive excess above this infimum and the signed change of minimum need bounds. Decreasing a hole plaquette while holding its neighbours fixed does not control either term: every plaquette incident to a changed bond contributes to the action change.

**Discharged — small deleted fraction alone gives no reserve.** This can be checked in a finite quadratic diagnostic, without identifying its variables with lattice plaquettes. On `R^N` put `E(a)=sum_i a_i^2/2`. An all-line mean `v` has minimum `Nv^2/2`, since `sum_i(a_i-v)^2>=0`. With `r` coordinates omitted from the mean, the unrestricted minimum is `(N-r)v^2/2`: the retained coordinates equal `v` and the omitted coordinates equal zero. The minimum loss is `rv^2/2`, although the deleted fraction `r/N` tends to zero. This is not a Wilson counterexample and does not satisfy the crossing predicate; it excludes an argument based solely on `q<<1` with no bound on the reference and its response.

### 4.1 An exact quadratic calculation with the actual fixed-pattern rows

**Implication — which linear maps are being tested.** Grant the literal singleton-hull admission of Section 7, without substituting a cube or another routing rule. Differentiate the corresponding fixed-pattern relative-log maps at the flat field. Write `Q_h` for the first-step map with precisely those excluded lines and routed contours, `Q_0` for the all-lines first-step map, and `Q_0^(1)` for the all-lines second step. These are finite real matrices on scalar commuting link angles. Although the label `h` has zero probability at the flat field, its fixed-pattern map and derivative are well defined there; this is a relaxed variational calculation, not differentiation of a positive-probability label event.

**Discharged — quotient and constraints for this finite calculation.** Let `d_f,d_t` be the fine and top oriented plaquette incidence matrices. Put

    X = (real fine 1-cochains)/ker d_f,
    <x,z>_X = sum_p (d_f x)_p(d_f z)_p,
    Y = image d_t,
    C_s x = d_t Q_0^(1) Q_s x,        s=0,h.                 (4.2)

The energy inner product on `X` is positive definite by its definition. The maps `C_s` descend to this quotient. Indeed a curl-free cochain is a gradient plus constant coordinate cochains: subtract the constant cochain whose value in direction `j` is the period in that direction divided by the torus side. Integrate the remainder along paths and interchange adjacent coordinate steps by plaquette relations; backtracking then cancels, and the remaining coordinate cycles have zero integral. A gradient telescopes to its values at block centres; a constant bond value integrates to `L` times that value on every path in its direction. Excluding some paths or rerouting their internal contours changes neither fact. Thus a zero fine curl gives zero top curl.

For the admitted non-Haar pattern each coarse bond has a surviving straight line and hence a private crossing-face bond. Its linear coefficient is the positive number of surviving lines reading it divided by the total number of surviving lines. Internal contours read no crossing-face bond; no other parent row reads this bond. Assigning one such variable per row proves that `Q_h`, and likewise `Q_0`, are surjective. The same argument at the second step proves that both `C_s` map onto `Y`. This argument uses the actual retained subsets, not their replacement by complete-column subsets. Adding a curl-free fine field can match any remaining curl-free top difference at zero quadratic energy: prescribe the top vertex potential on fine vertices and use constant fine periods divided by `L^2`.

**Discharged — the two unconstrained minimum values.** Define adjoints using the displayed energy inner product on `X` and the ordinary plaquette inner product on `Y`. The finite matrices

    G_s=C_s C_s^*,       H_s=C_s^* G_s^(-1)                 (4.3)

are well defined: `<y,G_s y>=||C_s^*y||_X^2`, which can vanish only when `y` is orthogonal to the range `Y`, hence when `y=0`. For `y in Y`, the minimum of `E(x)=||x||_X^2/2` under `C_s x=y` is

    x_s=H_s y,
    m_s^quad(y)=<y,G_s^(-1)y>/2.                            (4.4)

To prove it, write any competitor as `x_s+z`, `z in ker C_s`. Then `<x_s,z>_X=<G_s^(-1)y,C_s z>=0`, so

    E(x_s+z)=m_s^quad(y)+||z||_X^2/2.                       (4.5)

No spectral estimate or matrix computation is hidden in this identity.

**Discharged — the cost of forcing one hole plaquette.** Fix the actual fine plaquette `p` used at `h` in the face construction, and set `ell_p x=(d_f x)_p`. Let `b_p` be its energy-inner-product representer, determined by the finite positive definite linear system `<b_p,x>_X=ell_p x`. Since `|ell_p x|<=||x||_X`, `||b_p||_X<=1`. The orthogonal projection onto `ker C_h` is `P_h=I-H_h C_h`. Set

    alpha_p(y)=|ell_p H_h y|,
    r_p=||P_h b_p||_X^2,             0<=r_p<=1.             (4.6)

For a threshold `t>0`, minimizing (4.5) additionally over `|ell_p x|>=t` gives exactly

    m_h^quad(y) + (t-alpha_p(y))_+^2/(2r_p),                (4.7)

when `r_p>0`. Cauchy–Schwarz gives the lower bound; equality is obtained by taking `z` proportional to `P_h b_p`, with the nearer of the two signs. If `r_p=0`, the extra cost is zero when `alpha_p>=t` and the constraint is impossible otherwise. Thus the convention in (4.7) is explicit. The same infimum holds for a strict threshold by approaching its boundary whenever the strict set is nonempty.

Subtracting the all-lines minimum, with `t=1`, exhibits every term that the hole-cost heuristic needs:

    inf_{C_h x=y, |ell_p x|>=1} E(x) - m_0^quad(y)
      = (1/2)<y,(G_h^(-1)-G_0^(-1))y>
          + (1-alpha_p(y))_+^2/(2r_p).                     (4.8)

In particular the excluded-line minimum contributes a signed term of either sign. The estimate `r_p<=1` controls the fluctuation cost, not this signed term. The prescribed face is no longer frozen in (4.4)–(4.8): every fine cochain is minimized over, including every deleted-line coordinate.

**Gap — this calculation has not been promoted to Wilson action.** Equations (4.2)–(4.8) are exact for the quadratic tangent problem with the actual fixed-pattern rows. They supply neither a uniform nonlinear chart for all low-action histories nor bounds on the constrained Wilson remainder and its minimum. They also omit the second crossing inequality, the non-quiet test and positive label support. These omissions make (4.7) useful as a relaxed lower-bound calculation if its signed comparison is positive; they do not make it an admissible counterexample if the comparison fails.

## 5. One smaller inequality at which the calculation stops

**Gap — the finite quadratic reserve (QR).** Fix just the endpoint centre `W(T_2/4)` and just the face's plaquette `p`. Let `e_f` denote the unit cochain of the face's unique nonidentity level-1 parent bond, and `e_*` the top bond cochain of `b_*`. In dimensionless angles define the single, specified top curl

    y_* = d_t[ Q_0^(1)((v/T)e_f) + (rho/4)e_* ].             (5.1)

The contour gradient drops out, so this is the exact commuting curl of that centre divided by `T`. The single inequality still unproved is

    |ell_p H_h y_*|
      + sqrt( max{0, <y_*,(G_0^(-1)-G_h^(-1))y_*>} )
                                                    <= 1/2. (QR)

The matrices refer to the actual torus, actual excluded-line set and actual routing, as in (4.2). Neither summand may be discarded. In particular this test includes the minimum over the entire excluded-line fibre, not the face ansatz alone.

**Discharged — the explicit reserve that (QR) would give in its stated problem.** Write its first summand as `alpha` and its second as `beta`. Then `alpha<=1/2`, `beta<=1/2-alpha`. The negative part of the first term of (4.8) is at most `beta^2/2`. Using `r_p<=1`, its right side is at least

    [(1-alpha)^2-beta^2]/2
      >= [(1-alpha)^2-(1/2-alpha)^2]/2
       = 3/8-alpha/2 >= 1/8.                              (5.2)

For angles scaled by `T`, this is `T^2/8`. The coefficients are: `1/2` from the bare quadratic energy; `1/r_p>=1` from the one-plaquette functional; at most `beta^2/2` lost to changing the fibre minimum; and the remaining `1/8` from the displayed subtraction. The impossible case `r_p=0` with `alpha<1` is harmless. This is a proved implication from (QR), not a proof of (QR) or (SP).

**Discharged — why this is strictly less work, and its logical role.** (QR) is one inequality between finite matrix entries at one specified vector. All its constrained minimizations have been eliminated by (4.4) and (4.7). It contains one colour, one fixed top centre and one fine plaquette; it has no window infimum, no nonlinear SU(2) products, no disintegration, no fluctuation factor, and no optimization over label branches. A proof would still leave the other window points, other possible hole plaquettes and the nonlinear/support passage unpaid. It is a smaller sufficient analytic input in the attempted proof, **not** a claimed necessary consequence of fixed-`T` (SP); failure of the convenient constant `1/2` would not refute (SP). This distinction prevents quietly replacing the requested problem by its tangent model.

**Unchecked — expectation, with its reason and limit.** I expect (QR) to hold after the intended admitted large-`L` choices. The endpoint has top amplitude of order `rho`, while two averaging steps should spread its minimum over fine plaquettes; a bounded sparse exclusion should perturb that smooth minimum and its value weakly. That predicts a small first summand and a small signed-loss summand. This is a heuristic, not a recalled Green-function theorem. The diagnostic preceding (4.2) explains why the deleted fraction alone does not prove it. What is missing is a hand bound on this particular inverse-matrix row and on the signed inverse-matrix difference for the literal excluded-line geometry. No unspecified constant `C` has been absorbed into `1/2`.

**Gap — disposition of the requested (SP).** There is no hand-checkable supported history attaining the complete denominator's infimum, and there is no signed comparison for the remaining windows. I therefore cannot label (SP) PROVED or REFUTED. Equation (2.7) is discharged; (3.2), (4.8) and (5.2) have precisely the scopes stated. No repaired S1–S4 statement, and no wider rarity statement, is killed by this calculation.

## 6. Source boundary and recovery checkpoint

**Discharged — bounded reads at the pinned source.** Paths are relative to this loop directory. The complete requested note and its listed full/ranged sources were read; truncated retrievals were repeated before their content was used. The substantive ranges were:

- `GOAL.md:1–75`; `FINISH.md:148–177`, with the queue around row 62; the checkout's `AGENTS.md`.
- `library/rarity-repair.md:1–320`; `library/rarity-fresh-c.md:1–179`; `gates/rarity-fresh-c-263afacbd.md:1–291`; `library/rarity-fresh-x.md:1–161`.
- `parts/hard-core--mapped.md:376–402,562–624,636–688`; additionally `734–758` to inspect the actual lift statement and its proof boundary.
- `library/quiet-boundary-rarity.md:15–31`; `parts/upper-chain.md:176–190`; `library/one-window.md:41–103`.
- `library/relative-density-bound.md:325–371`; additionally `145–175` for the cube, collar and minimum-comparison conventions cited there.
- `library/c0-loc.md:186–210,910–934,995–1071,1185–1266`; `parts/hard-core--threshold.md:118–160` for the adopted threshold order.

**Discharged — evidence limits and edits.** Bounded location searches were not mathematical evidence. Numerical claims encountered inside these allowed sources were not used. No forbidden independent-side source or gate, excluded library file, strategy/history-budget/compute-inventory gate, external proof account or literature was opened. References to such material in allowed sources were not followed. No result from memory supplies an input. Only `library/sp-decide.md` is written; no editable prompt file or other source file is modified. No commit, push, PR, post, audit, numerical job or subagent was made.

**Gap — current recovery point.** For the admitted face-defined family, the low-window conclusion is (2.7), with its displayed scale condition. Releasing the fine face prescription cannot beat its absolute hole cost there. At the remaining windows, the regular-lift margin has the conditional numerical value (3.2); it is not a statement about the excluded-line minimum. The unresolved next inequality is exactly (QR), including its signed inverse-matrix difference. Its expected truth is explained above, without using an unproved estimate as evidence. Even a proof of (QR) would still require a uniform window/plaquette extension and a nonlinear, positively supported Wilson comparison before deciding (SP). Literal singleton-hull and non-quiet admission remain explicit; an empty family must be reported as vacuous, never as an energetic proof.

STOPPED
