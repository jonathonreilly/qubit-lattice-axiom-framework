# Fine removal beside retained field
Provenance: OpenAI Codex; configured model `gpt-6-astra`, effort `max` (local configuration, not an independent identification of the backend); commit `8ac5aaae4bde97d7e5457714cf233dcdc0468139`; author research, not an audit, and no status is granted.

## 1. Scope and the meaning of payment

**Unchecked — source boundary.** This note concerns the proposed common fine-removal lemma, (HW) in `heavy-wall.md` Section 5, and the coordinated (PATCH) in `seam-nlpay.md` Section 3. Source labels are not imported as proofs. All mathematical assertions below carry their own label. No numerical calculation, enumeration, or computer-assisted proof is used. No remembered theorem is used as a discharged premise; elementary identities used below are derived in the text.

**Discharged — the signed quantity to estimate.** Write

    a_p(F) = 1 - (1/2) Re tr hol_p(F),   A(F) = sum_p a_p(F).

For a replacement X in a core D with target T, put

    G_D = sum_(p in D) [a_p(U)-a_p(T)],
    R_D = sum_(p in D) [a_p(X)-a_p(T)]
            + sum_(p outside D) [a_p(X)-a_p(U)].

Then `G_D-R_D=A(U)-A(X)`, by cancelling the two occurrences of the target action. An individual plaquette summand cancels exactly when its **holonomy trace** remains the same; retaining some of its bonds or its contribution to a coarse average does not imply this. The identity does not estimate the plaquettes with both changed and retained edges.

**Discharged — what genuine removable excess means.** Fix the actual parent constraints and the actual retained fine links, and let `F_d` be their admissible fibre. On a finite lattice set

    m_d = inf_(F in F_d) A(F),   E_d(U)=A(U)-m_d.

For admissible U this is nonnegative. If U attains the infimum, it is zero even when U has nonzero action. On a local region the same definition includes every incident plaquette and fixes the exterior. Replacing this excess by the action of an isolated piece, or by common locked action, changes the proposed lemma.

**Gap — quantifiers needing correction before a theorem is possible.** “Same parents at every level” literally includes the first parents; their further deterministic iterates then already agree. Equality of just the terminal parents is weaker. A zero parent must mean an exact fibre-preserving operation at the current background, not the assertion that a flat linear average of a bond logarithm vanishes. Also, an action-payment lemma must specify which spatial partial replacements it supplies. Declaring the entire relative field one atom and allowing only its complete replacement supplies no local lemma for HW or a seam. The tests below distinguish a prescribed local replacement from an unrestricted choice of decomposition and gauge.

## 2. The first mixed plaquette, before any norm estimate

**Discharged — exact failure of plaquette-by-plaquette deletion.** In a level-one block of odd side L at least 7, use `Z=diag(i,-i)` and a positive a small enough that all path angles below stay in `(-pi,pi)`. Put a direction-one link `exp(aZ)` at transverse position `(x_2,x_3,x_4)=(1,0,0)` and its inverse at `(-1,0,0)`. This is pair P. Pair Q has the same two values at `(1,1,0)` and `(-1,1,0)`, with the same longitudinal coordinate. All other links are identity. Reflection in `x_2=0` makes the abelian all-lines parent of each pair and of their sum identity: reflected straight-line contributions have opposite signs and equal weights, and reflected rooted contours have opposite integrals. The logarithms introduce no reduction modulo `2pi` when `8a<pi`. All higher parents are identity.

There are exactly two plaquettes shared by the supports of P and Q, both of orientation `(1,3)`, one at each sign of `x_2`. Their holonomies are initially `exp(aZ) exp(-aZ)=1` and its inverse. Deleting P whole while retaining Q changes each shared plaquette's action from zero to `1-cos a>0`. Both parents remain identity. No subtraction of common raw heavy energy removes these terms: the formerly flat plaquettes have actually changed.

**Discharged — this test alone is not a refutation of excess payment.** Each isolated pair has twelve nonidentity plaquettes. The pairs share two plaquettes; the four isolated incidences on these two plaquettes cancel in the combined field. Thus

    A(P+Q)=20(1-cos a),   A(Q)=12(1-cos a).

Deleting P saves `8(1-cos a)` overall, while creating `2(1-cos a)` on the mixed plaquettes. A payment theorem could charge that cost to this actual gain. The example refutes only the assertion that whole-pair deletion always avoids creating unpaid plaquette terms. It does not refute HW, PATCH, or an optimally chosen decomposition.

## 3. The nonabelian test is an interaction term, not a linear parent error

**Discharged — the commutator square, including its coefficient.** Put

    X = [[0,i],[i,0]],   Y = [[0,1],[-1,0]],
    A = cos(t) I + sin(t) X,   B = cos(t) I + sin(t) Y.

Direct multiplication gives `X^2=Y^2=-I`, `XY=-YX`, and zero trace for X, Y and XY. Thus

    A Y A^-1 = cos(2t) Y + sin(2t) XY,
    (1/2) tr(A B A^-1 B^-1)
        = cos(t)^2 + sin(t)^2 cos(2t) = 1-2 sin(t)^4.

The action is exactly `2 sin(t)^4`. The horizontal-edge field with the same A on both forward horizontal edges is flat by itself, as is the corresponding vertical B field. Their linkwise combination is not flat. Equivalently, the bond logarithms are the gradient of the vertex values `0,tX,t(X+Y),tY`, whose additive curl is zero. One cannot pay the combined field using only the two separate curls or their separate plaquette actions.

**Discharged — scope of this test.** Assigning the two factors to different scale labels does not alter this multiplication. A valid scale splitting must include their interaction or use background-dependent factors whose exact actions already contain it. This square alone does not construct two exact zero-parent factors for the actual multilevel map; it is not offered as a second full-fibre counterexample. The complete counterexample below is abelian, so it needs no commutator estimate at all.

## 4. The local consequence that the proposed lemma would have to supply

**Implication — a necessary consequence of payment only by removable excess.** Give the candidate favorable endpoint hypotheses: U and T have the same exact parents at every available level, the same retained fine data d, and T is a constrained minimum. A local partial replacement must allow T on a prescribed inner region and U on a prescribed exterior, with a transition region between them. Gauge matching is allowed only by gauges preserving d. It must account for every changed plaquette.

Any bound on its positive cost by a finite sum of constants times genuine removable excesses has the following necessary zero-excess consequence:

    If U and T are constrained minima, and a_p(U)=a_p(T),
    a prescribed local partial replacement can be made with
                        A(X)-A(U) <= 0.                 (ZP)

Indeed every local constrained excess of U is zero: a local decrease with the same parents and retained exterior would also decrease the global constrained action. Higher fields in the example below are identity and have zero excess too. Hence every proposed payment term vanishes, independently of its coefficient, scale summability, or depth. Equality of the endpoint plaquette actions makes the replacement cost R_D exactly `A(X)-A(U)`, for every choice of D.

**Discharged — why locality is part of this test.** An unrestricted operation `U -> T` is not challenged by (ZP). The requested application to a core or seam requires a partial replacement which retains the specified exterior. Equivalently, if the lemma chooses its own transition region of radius at most r in top units, the example may put an unchanged point farther than r from the core. A decomposition that joins every touching piece into one arbitrarily long atom can avoid this requirement, but then it is not the local, cube-indexed lemma proposed to supply HW or PATCH. The counterexample addresses (ZP), not the tautology that two equal-action endpoints can be exchanged globally.

## 5. Exact configuration: small plaquettes, identity parents, retained fine boundary

**Discharged — lattice and fields.** Fix an odd L divisible by 3, with `L>=9`. Set `m=L^N`, `alpha=pi/m`, and use a four-dimensional periodic lattice of side `2m`. Coordinates are `(x,y,z,w)`. Choose N large enough that `15L alpha<pi` and `3alpha<T_class`, where the positive fine class threshold is fixed before N. Any smaller fixed positive pointwise plaquette threshold can also be met this way.

Let f be the L-periodic integer function of x which is 1 at residue 1, -1 at residue -1, and 0 elsewhere. Put

    d_x=f(x+1)-f(x) in {-1,0,1}.

There are exactly four nonzero d_x in each period. All links in directions 2, 3 and 4 are identity. For direction 1 define

    U_1(x,y,z,w)=exp(d_x s_U(y) Z),
    T_1(x,y,z,w)=exp(d_x s_T(y) Z),   Z=diag(i,-i),

    s_U(y)=alpha y              (0<=y<=m),
           alpha(2m-y)         (m<=y<=2m),
    s_T(y)=-alpha y            (0<=y<=2m).

Both fields are periodic as group-valued fields. On `m<=y<=2m` they agree because `s_U-s_T=2pi` and d_x is an integer. They also agree at y=0 and y=m. All nonidentity plaquettes have orientation `(1,2)` and angle alpha. In particular

                        a_p(U)=a_p(T)                 (5.1)

on every plaquette, including the retained part.

**Discharged — the retained data are genuine fine boundary data.** Retain every transverse link, every direction-one link with `d_x=0`, and every direction-one link with `y=0` or `m<=y<2m`. The only variables are direction-one links with `d_x!=0` and `0<y<m`. Call these data d. Geometrically the variable domain is the union of open unit-thickness slabs

    (x,x+1) x (0,m) x (periodic z,w),   d_x!=0.

All transverse links lie on their retained faces. The faces separating adjacent slabs are retained too. Thus no assertion about an arbitrary interior freezing is concealed: this is a specified region with retained fine boundary. The slabs are thin and long; a universal assertion for arbitrary retained boundary and regions includes them. These are **not** asserted to be the cleared, thick collars or the particular frozen-layer geometry of HW. That distinction limits the downstream conclusion in Section 8.

**Discharged — the exact parents, with no logarithm-branch shortcut.** For either endpoint introduce the site field

    g(x,y,z,w)=exp(f(x) s(y) Z).

It is periodic, including for s_T, since f is integer. Gauge multiplication gives

    F_1^g=1,
    F_2^g(x,y,z,w)=exp(f(x)[s(y)-s(y+1)]Z),
    F_3^g=F_4^g=1.

The principal angle on each displayed direction-two bond has magnitude at most alpha. At every first block centre x is a multiple of L, so `g=1`. Products along a parent path transform only at its two centres; therefore the parent path matrices before and after this gauge transformation are identical.

In the transformed field the exact abelian all-lines formula is

    QH=Q_path H+Phi(c)-Phi(c').

Each rooted axial contour and straight parent path has length at most `5L`. Its total angle has magnitude at most `5L alpha<pi`, so its group logarithm is its actual additive angle. The direction-two straight contribution is f(x) times a quantity independent of x; its average over an L-block vanishes since `sum f=0`. All other straight contributions vanish. Reflection of x about the block centre sends f to -f, preserves the axial contour order, and leaves the y-profile unchanged. Hence the rooted contour integrals cancel in pairs and `Phi(c)=0` at every centre. Every first parent is exactly identity. All subsequent parents are consequently identity. The endpoint plaquette angles are below the class threshold, so the mapped kernel has no rough labels or excluded lines here and uses this all-lines map. This argument proves equality at **every** level, not merely equality of terminal parents or a linearized constraint.

**Discharged — the fine total can nevertheless be large.** Assign positive plaquettes to cubes by their base vertex, consistently with the sums defining the action. In any aligned top cube containing m consecutive sites in each direction, there are `4m/L` active longitudinal positions and `m^2` transverse chains at each position. Both endpoints have angle alpha on every active `(1,2)` plaquette, at every y. The cube's action is

    (4m^4/L)(1-cos(pi/m)) >= 8m^2/L.                 (5.2)

For the inequality, `1-cos t=2sin(t/2)^2` and concavity of sine on `[0,pi/2]` give `sin(t/2)>=t/pi`. Thus (5.2) diverges while each plaquette angle tends to zero. The counterexample is not dependent on one large-angle plaquette or on a Haar-parent choice.

## 6. Exact constrained minimality and the unavoidable mixed cost

**Discharged — a finite identity for an arbitrary SU(2) chain.** Identify SU(2) with the unit vectors of `R^4` by

    q=(q_0,q_1,q_2,q_3) -> q_0 I+i sum_(a=1)^3 q_a sigma_a.

Here `sigma_1=[[0,1],[1,0]]`, `sigma_2=[[0,-i],[i,0]]`, and `sigma_3=diag(1,-1)`. A unitary determinant-one matrix has the form `[[z,w],[-conj(w),conj(z)]]` with `|z|^2+|w|^2=1`: orthogonality fixes the second row up to a phase, and determinant one fixes that phase. Its four real coordinates give this parametrization. Direct multiplication of the three displayed matrices gives `tr(sigma_a sigma_b)=2 delta_ab`, and therefore

                  (1/2) Re tr(r q^-1) = r dot q.

Let `r_0=e_0`, `r_m=-e_0` and `|r_y|=1`. For either sign sigma define

    q_y=cos(y alpha)e_0+sigma sin(y alpha)e_3,
    delta_y=r_y-q_y,   phi_y=sin(y alpha),
    E(r)=sum_(y=0)^(m-1) [1-r_y dot r_(y+1)].

Then the following identity holds for every chain r, with no smallness assumption:

    E(r)-m(1-cos alpha)
      = (1/2) sum_(y=1)^(m-2) phi_y phi_(y+1)
             |delta_(y+1)/phi_(y+1)-delta_y/phi_y|^2.   (CHAIN)

Here all denominators are positive. To verify it, first use `delta_0=delta_m=0`, `q_(y-1)+q_(y+1)=2 cos(alpha)q_y`, and

    2 q_y dot delta_y = -|delta_y|^2

from the two unit norms. Expansion of E(r)-E(q) gives

    cos(alpha) sum_(y=1)^(m-1) |delta_y|^2
                  -sum_(y=1)^(m-2) delta_y dot delta_(y+1).

Expanding the right side of (CHAIN) gives exactly this expression because `phi_(y-1)+phi_(y+1)=2 cos(alpha)phi_y` and `phi_0=phi_m=0`. Finally consecutive q's have dot product cos(alpha), so `E(q)=m(1-cos alpha)`. This proves (CHAIN) by displayed finite algebra; no spectral theorem or numerical eigenvalue is being invoked.

**Discharged — U and T attain the constrained minimum over all fields.** For each active x and each (z,w), the free links form a chain r_y with endpoints I and -I. Its `(1,2)` plaquettes contribute E(r). All outside `(1,2)` plaquettes are fixed and contribute `m(1-cos alpha)` per active chain. The `(1,3)` and `(1,4)` plaquettes have nonnegative action. All remaining plaquettes have zero action. By (CHAIN), if

    C = (4(2m)/L)(2m)^2 = 32m^3/L

is the number of active chains, every field with d has action at least

                      2 C m(1-cos alpha).             (6.1)

U and T attain this bound: their chains are the displayed q with opposite signs, and their transverse mixed actions vanish. They have the required identity parents. Consequently (6.1) is also the infimum over the exact parent-constrained fibre, and

                       E_d(U)=E_d(T)=0.               (6.2)

This is minimality against arbitrary nonabelian competitors, not just against the abelian ansatz. Restricting any local operation further cannot provide positive removable excess at either endpoint.

**Discharged — partial replacement forces a positive cost on one chain.** Put `i=m/3`, `j=2m/3`, and choose a chain with `d_x=1`. Require a replacement to take the target value at i and retain the original value at j. These requirements can be imposed on neighborhoods, not just on individual links. Relative to q=U, they give

    delta_i/phi_i=-2e_3,     delta_j/phi_j=0.

Set `v_y=delta_y/phi_y`. Weighted Cauchy--Schwarz, applied to `v_j-v_i=sum_(y=i)^(j-1)(v_(y+1)-v_y)`, gives

    4 <= [sum_(y=i)^(j-1) phi_y phi_(y+1)|v_(y+1)-v_y|^2]
                      [sum_(y=i)^(j-1) 1/(phi_y phi_(y+1))].

On this interval every phi is at least `sqrt(3)/2`. There are `m/3` terms in the second sum, so it is at most `4m/9`. Equation (CHAIN) therefore gives, for **every** such replacement,

                       A(X)-A(U) >= 9/(2m) > 0.       (6.3)

All other chains contribute nonnegative differences after their fixed outside actions are subtracted. If the inner/exterior requirements apply to the whole cross-section, summing the same argument gives `9C/(2m)`. The sign `d_x=-1` changes the vector -2e_3 to 2e_3 and leaves this bound unchanged. This is the mixed cost after exact cancellation of the entire common outside action. It is incompatible with (ZP).

**Discharged — the partial fibre is nonempty and can stay class.** For the cross-sectional core `y<=i` and exterior `y>=j`, an explicit interpolation is

    s_X(y)=-alpha y                     (0<=y<=i),
           -pi/3+3alpha(y-i)           (i<=y<=j),
           alpha y                    (j<=y<=m),
           s_U(y)                     (m<=y<=2m).

Put `X_1=exp(d_x s_X Z)` and keep transverse links identity. It agrees with T in the core and U in the exterior. Its plaquette angles are at most `3alpha<T_class`; the same parent calculation applies, now with path angles bounded by `5L(3alpha)<pi`. Thus it has identity parents and a class chain throughout. No emptiness or inaccessible target is responsible for (6.3). Its actual action increase per chain is

                  (m/3)[cos(alpha)-cos(3alpha)]>0.

For positivity, `0<alpha<3alpha<pi` and cosine is strictly decreasing there. Smoothing the interpolation or allowing nonabelian values cannot remove the positive lower bound (6.3).

**Discharged — a coherent admissible gauge cannot identify the endpoints.** A site gauge preserving d must be constant in (y,z,w) on each x-plane, since all transverse links are the retained identity. Write its value h_x. Every direction-one link at y=0 is retained and equal to identity, so `h_x=h_(x+1)`; the gauge is one global h. A retained active link at y=m+1 has value `exp((pi-alpha)Z)` or its inverse. Its eigenvalues are distinct, so preservation forces h to commute with Z: in its diagonal basis the off-diagonal entries of h must vanish. Such a gauge fixes every link of U and T separately. There is no global relative-gauge normalization, preserving the same fine data, that turns this into an exchange of equivalent endpoints.

Locally conjugating the target on the inner slab alone can interchange the two signs. That is not a coherent gauge of the admissible target preserving d on the whole region. Allowing such independent core identifications drops a hypothesis of (ZP) and does not supply the coherent alignment requested by PATCH. No claim against that weaker, locally gauge-identified replacement is made here.

## 7. Why changing scale or allowing a small positive excess does not repair this lemma

**Discharged — touching chains cannot be peeled by a zero-excess local move.** Equality in (CHAIN) forces `delta_y/phi_y` to be constant for `1<=y<=m-1`, since every coefficient of a squared difference is positive. If one interior link is retained, that constant is zero; every interior link on its chain must then remain unchanged. A nontrivial zero-cost change therefore changes the entire chain between its retained ends. There is no finest-first ordering that removes one bounded portion while retaining another. This proves the obstruction for every construction of the partial replacement, not just for the displayed interpolation.

For an interpretation with a radius r(L) in top units, fix the available depth n and top spacing `B=L^n`, and choose `m=L^N` with `N>n` so large that `m/3>r(L)B` (increase the margin for any fixed number of collar layers). Stop the parent chain at n; all its fields are still identity. A core near i then has a retained point j beyond every allowed collar. The same proof applies. Joining the entire chain into one atom would require an unbounded top-unit support. With `N=n` the construction already gives a chain spanning a top cube and an explicit obstructed partial replacement inside it. This distinguishes the prescribed-partial-replacement claim from the bounded-radius version; both fail in the asserted arbitrary-boundary domain.

The same argument addresses an **existential choice of cube-supported factors**, not only a prescribed splice. Suppose each factor at level l is supported in a cube of diameter at most `c(L)L^l`, for `l<=n`, and every partial product has its action increase paid by removable excess. Choose `m>4c(L)B+6`. Its first nontrivial factor leaves at least one interior link of every chain unchanged. Since all credits are zero, the resulting field must still attain (6.1). Equality in (CHAIN) then forces every chain to remain unchanged, a contradiction. The argument repeats if initial factors act trivially. Thus no such finite local splitting reaches T. Allowing a factor supported on the whole long chain is a precise escape, with precisely the loss of locality just identified.

**Discharged — a strictly positive excess can be arbitrarily small.** At fixed L,m, change the U profile only at y=1 by adding epsilon, where `0<epsilon<alpha/4`. Apply this to all active columns, leaving all retained data unchanged, and call the field `U_epsilon`. The same gauge and reflection proof gives identity parents; all fine angles remain below the chosen threshold. Its excess is exactly

    E_d(U_epsilon)
        =2 C cos(alpha)(1-cos epsilon) <= C epsilon^2. (7.1)

Indeed only the two adjacent `(1,2)` increments change, from alpha,alpha to `alpha+epsilon,alpha-epsilon`, and
`cos(alpha+epsilon)+cos(alpha-epsilon)=2 cos(alpha)cos(epsilon)`.
The estimate uses `1-cos epsilon<=epsilon^2/2`, obtained by integrating `sin t<=t`.

The values at i,j have not changed. For the same partial replacement of the whole cross-section, (6.3) gives

    A(X)-A(U_epsilon) >= 9C/(2m)-E_d(U_epsilon).       (7.2)

As epsilon tends to zero the right side stays positive, whereas every local constrained removable excess is at most `E_d(U_epsilon)`: its local infimum is at least the global infimum. At this fixed finite volume and depth any finite sum of such credits with fixed coefficients tends to zero. Thus an extra hypothesis `G>0`, or a finite but large summable constant, cannot repair this particular assertion. Charging the nonzero **minimum** in (6.1), instead of (7.1), would repair the bookkeeping only by abandoning payment solely from removable excess.

**Discharged — a reference cannot release retained data for free.** A purported level credit could be positive if its reference minimization discards some of d. That amount is not removable while d is retained. The counterexample concerns exactly the same retained data on both sides, as the candidate requires. It does not rule out a different theorem which explicitly pays changes of data or carries a separate boundary/interface energy.

## 8. Decision on the candidate and on its proposed consumers

**Discharged — refutation of the universal local lemma.** Sections 5–7 give fields in the actual all-lines class chain, with identical parents at every level and identical retained fine boundary data. The target is even an exact constrained minimum. Every genuine local removable excess is zero, but every indicated partial replacement costs at least `9/(2m)`; the fully specified class partial replacement exists. The strictly positive-excess variant has a cost bounded away from zero at fixed m while all proposed excess payments tend to zero. Consequently the proposed arbitrary-boundary local lemma is false. The obstruction occurs after exact cancellation and already in an abelian subgroup. No summable-in-level coefficient can repair a zero right-hand side at a fixed finite lattice.

**Discharged — exactly what this does not refute.** This kills the **universal candidate only**, not (HW) or coordinated (PATCH) in their stated domains.

- **HW.** Its domain has a particular quiet frozen-layer pattern, clearance from lower layers, a triggered core, and a specified small target. The counterexample has retained faces running through long thin slabs. For the unperturbed endpoints `G_D=0` for every D, whereas HW requires `G_D>0`; there is no triggered rough core. The perturbed example supplies positive excess but does not supply HW's trigger and small-target hypotheses. Hence no admissible HW instance violating its inequality has been constructed. Deletion still works for heavy-wall's isolated pairs because their common identity reference is attainable with no retained-face frustration.
- **PATCH.** Its right-hand side is the endpoint **curvature energy**, not their removable excess. That energy is nonzero here. Moreover, the literal terminal-parent seam has a specified unfrozen minimizer and trial: without d, identity is an admissible zero-action field, so neither endpoint here is that minimizer. The all-top-cubes U-local premise is also not supplied by class membership; (5.2) shows why. This is not a counterexample to coordinated PATCH after all of its own hypotheses have been met.

**Gap — a substantive restriction would be needed for a repaired common lemma.** Parent equality alone does not distinguish different constrained minima whose mixture costs energy. A repair could restrict the retained geometry and prove a relative coercivity/uniqueness estimate there, or allow an interface cost which is not paid by removable excess, or give up local partial replacements and remove whole connected components. These are changes of mathematical content. No such positive estimate for the actual cleared HW collars or the actual seam endpoints is established here. In particular, the two stops cannot be identified merely by writing the proposed excess-only decomposition.

**Implication — GLUE-E, WAM and UP remain conditional on their actual inputs.** If GLUE-E were separately proved for its specified class minimizer U and trial T, its complete replacement cost and `A(X_D)>=A(U)` would give

    A_U(D)-A_T(D)
       <= A_s(L) sum_p (K*1_(S_r(D)))(p)[a_U(p)+a_T(p)].

That is the shell comparison. WAM asks `A_U(w)<=[1+D_A(L)nu_l]A_T(w)` uniformly down to `nu_l=0`. The WAM-to-UP step additionally reads the specified trial estimate, class-minimum identification and fine-flux bound; none is proved by a fine-field decomposition or by this counterexample. UP remains the estimate

    E_0-E_l <= C_TOP(L)a_l
                    +D_TOP(L)[(f_l+nu_l)E_l+tau_l].

Those additional inputs are unchecked here. In the unperturbed example (5.1) actually gives `A_U(w)=A_T(w)` for every weight, so it supplies no violation of WAM even if one temporarily enlarges its endpoint family. The example does not refute GLUE-E, UP or FALL on their stated endpoint families.

**Implication — the spatial absorption condition survives unchanged.** Suppose the preceding shell comparison holds with a symmetric probability kernel K whose exponential moment at the required rate is at most `M_*(L)`. Write `P=A_U(w)`, `Q=A_T(w)`, with `|log w(p)-log w(q)|<=s d(p,q)` and `0<=s<=nu_req`. Integrate the shell inequality over the superlevel sets `{w>t}`. At a plaquette the shell indicator integrates to at most

    max_(distance<=r) w-min_(distance<=r) w
                           <= 2 sinh(sr) w.

Transferring the symmetric kernel to the weight costs at most M_*, by the termwise inequality `w(p+z)<=w(p)exp(nu_req d(z,0))`. Thus

    P-Q <= beta(s)(P+Q),
    beta(s)=2 A_s(L) M_*(L) sinh(s r(L)).

At the prescribed rate the required absorption is still

    beta_* = 2 A_s(L) M_*(L) sinh(nu_req r(L)) < 1.    (RATE)

If it holds, put `b=2 A_s M_* r cosh(nu_req r)`. Integrating cosh gives `beta(s)<=b s`, and rearrangement yields

    P <= [1+2 b s/(1-beta_*)] Q.

If `beta_*>=1`, this rearrangement supplies no upper bound at the required rate. Summability in depth, a finite radius, and a finite coefficient separately do not prove (RATE). This note supplies none of the missing quantitative values, changes no required rate, and makes no deduction of HW, PATCH, GLUE-E, WAM, UP or FALL from the refuted lemma.

## 9. Verification boundary

**Unchecked — coverage and provenance of inputs.** GOAL and the three specified FINISH sections were read first. Scientific reading used bounded ranges or locating searches in `heavy-wall.md` (the pair, mixed term, HW and consumers), `seam-nlpay.md` Sections 1–4, `lift-nonlinear.md` Sections 1–4, mapped Text 1, 3.1 and 5.2–5.3 and locating excerpts, `paid-inputs-frozen-energy.md` Section 2, `excess-shell-end.md` Sections 1–2 and 4.2, `excess-seam.md` Section 2, and the displayed map/gauge statements in `block-poincare-energy-package.md`, `analytic-lift.md` and `lattice-uhlenbeck.md`. The mapped source is credited for the specified reflection-symmetric all-lines contour convention; its proofs, external account and other claims are not inputs to (CHAIN). Missing sparse methodology was inspected by `git show` at the pin. Local procedure/configuration reads establish provenance and scope only. No prohibited independent-side file or gate was opened; no literature or remembered result supplies a mathematical step.

**Discharged — limits of the negative claim.** The written counterexample quantifies over every allowed SU(2) replacement by (CHAIN); it is not an inference from failed searches. The attempted escapes have distinct dispositions: exact cancellation is already performed; nonabelian interpolation is included in the lower bound; coherent boundary-preserving gauges cannot align the endpoints; whole-component removal succeeds but loses the required locality; positive excess tending to zero still fails to pay. These tests do not claim exhaustion of routes to HW or PATCH. The thin-region restriction, local-versus-global gauge distinction, endpoint choice and definition of removable excess are explicit. No audit or procedural PASS is asserted. Only this file was written; no computation, audit, subagent, commit, push, PR or post was used.

REFUTED
