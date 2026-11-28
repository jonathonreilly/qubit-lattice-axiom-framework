# The dense step beside a heavy frozen wall
Provenance: OpenAI Codex, configured model `gpt-6-astra`, effort `max` (read from the local Codex configuration; backend identity is not independently exposed). Commit `169e1d5f3d71daa336bfd8e8056516eb08a14a5d`. Different provider from the example's author, Anthropic/claude-opus-5-5/max. Author research, not an audit; no status is granted.

**Unchecked (scope and dependencies).** ES means `energy-by-stages.md`, LN means `lift-nonlinear.md`, PE means `paid-inputs-frozen-energy.md`, RD means `relative-density-bound.md`, and LU means `lattice-uhlenbeck.md`, all at the pinned commit. Statements imported from these notes remain inputs, not discharged by their labels. No numerical experiment, enumeration, or computer-assisted mathematical step is used. Elementary arguments below are supplied explicitly; no theorem recalled from memory is used as a proved input.

## 1. Check of LN Section 6: the example needs repairs, but its shell obstruction survives

**Discharged (the pair, including normalization).** For odd `L >= 5`, put `exp(i a sigma_3)` and its inverse on the two direction-1 links starting at `z+(0,1,0,0)` and `z+(0,-1,0,0)` inside a level-1 block. All other links are identity. Each link belongs to six plaquettes. Their supports are disjoint because their initial vertices differ by two transverse lattice units. Thus there are twelve nonzero plaquette angles, each of magnitude `a`. Distinguish squared-angle energy `e_theta=12 a^2` from normalized Wilson action `e_A=12(1-cos a)`; they are not equal. At `a=T/8`, the angles are **equal to**, not strictly below, `T/8`, and are strictly below `T`. For `0<T<=1`,

    (11/24) a^2 <= 1-cos a <= a^2/2,
    T^2/12 < (11/128)T^2 <= e_A <= (3/32)T^2,
    e_theta=(3/16)T^2.

For the first inequality, integrate `cos t<=1` to get `sin t<=t`, integrate again to get `cos t>=1-t^2/2`, and integrate twice more to obtain `1-cos a>=a^2/2-a^4/24`; use `a<=1`. Thus LN's lower bound on `e_A` is valid in the small-threshold regime. Either energy convention supports the example, but one must use the same convention in all its shell sums.

**Implication (identity parents, with the precise map input).** Use the all-lines abelian formula (E3) of PE, namely `QH=Q_path H+Phi(y)-Phi(y')`, and its reflection-invariant contour family. The straight direction-1 lines at transverse coordinates `+1` and `-1` have identical longitudinal weight and opposite link angle, hence cancel. The other straight components vanish. Reflection in `x_2=z_2` pairs the contours within the block and changes the sign of their direction-1 contribution, so `Phi(z)=0`. Other blocks contain no modified link. This proves identity parents exactly, provided the stated contour formula is the actual kernel. Disjoint copies in separated level-1 blocks give the same cancellation block by block. A path reads at most the two endpoint blocks; `4a<pi` prevents branch reduction. All later levels are identity. There is no rough cell and no nonzero label in this small-field chain. The nonlinear kernel outside this small-field regime is not an input to this cancellation.

**Implication (placement, given ES (CL) and its flat-wall geometry).** Take a finite rectangular patch along a flat frozen level-j wall, with the other wall and the torus seams farther away than the shells used. Work inside the lower-layer-free collar, so the nonidentity fine links are variables although their level-j parents are frozen to identity. All frozen data remain identity. One box of side `L` in level-j units contains `L^(4j)` level-1 blocks. Keeping alternate blocks in each coordinate still leaves a fixed positive fraction of these. For any fixed finite shell profile the required copies therefore fit for sufficiently large `j`. Copies contributing to the initial free cell's enlargement can instead be placed in its first frozen-side level-j cell; that cell has `L^(4(j-1))` level-1 blocks, again unbounded with `j`. This verifies the depth quantifier rather than treating a box's capacity as infinite at fixed `j`.

**Discharged (exact shell arithmetic, replacing the `o(1)`).** Let `B=(K+1)T^2`, `K>=1`, and use Wilson action for this paragraph. In each box-column of the patch put `n_k=ceil(2^k B/e_A)` pairs in its kth frozen-side box, with their plaquette supports strictly inside that box. Write `b_k=n_k e_A`. Then

    2^k B <= b_k < 2^k B+e_A.

The convention "within L" can include the next box at distance exactly L. Accordingly let `q` be the last eligible box index, and let D contain **all** eligible boxes of the patch, not just the depth-zero boxes. This is a fixed number of wall-normal boxes, independent of depth. Its ith box-neighbourhood includes the profile through `m=q+i`. There is no energy on its lateral or free-side enlargement. For `n` columns,

    E_i=n sum_{k=0}^{m} b_k
        <= n[B(2^(m+1)-1)+(m+1)e_A],
    a_i=E_(i+1)-E_i=n b_(m+1) >= n 2^(m+1) B,
    a_i/E_i >= 1/[1+e_A/(2B)] >= 64/67 > 1/2.

Here `(m+1)/2^(m+1)<=1/2`: equality holds for `m=0,1`, and the ratio decreases thereafter because `(m+2)/(2m+2)<=1`. For squared-angle energy replace `e_A` consistently by `e_theta`; the resulting lower bound is `32/35>1/2`. Enlargements which include a bounded extra box collar are accommodated by increasing q and the final profile length by that fixed number.

**Implication (what this actually defeats).** Take enough populated boxes to cover all `J` candidate layers and their patch collars, inside the lower-layer clearance; increasing `t_0` and then `j` achieves this without changing `K,J,L,T`. Every eligible box is dense, while the equally heavy deeper boxes are ineligible under ES:192. A free cell touching the wall belongs to the original energy-defined Z and lies by this dense cluster. The sparse rule is unavailable there. At every permitted dense layer,

    C_f a_i > E_i/2                 for every C_f>=1.

Thus the **specified first-layer selection** at ES:88 has no output in this example (given the geometric and kernel inputs just isolated). Rounding, the strict inequality at `T/8`, and the endpoint convention for distance L do not rescue that selection.

**Discharged (two overstatements removed).** Failure of a sufficient fill estimate does not prove that an actual fill gains no action. Here deleting every pair gives the identity field, preserves every datum and parent, and removes all their action. In particular the expression `E_i+a_i-C_f a_i` being nonpositive would only mean that this lower bound is uninformative. It is not an upper bound on the actual gain. Also the example has no rough cell; its full constrained minimum is zero. It is not a counterexample to (AE-R), class-minimum, or an existential replacement for (4.2). It defeats the algorithm specified in ES Section 3, and hence that algorithm's proof of those conclusions.

## 2. Repair 2: start with the genuinely rough cell at the wall

**Discharged (the literal trigger change is insufficient).** Changing Z alone leaves ES's instruction "until no cell of Z and no dense box remains" unchanged. The identity-parent example still has eligible dense boxes. The useful version of repair 2 must also stop processing energy-dense boxes that have no level-j defect to remove, or define density from level-j quantities. The analysis below gives this strengthened version its best chance.

### 2.1 The hard local term, before any shell counting

**Discharged (small coarse curvature does not supply the fine gauge).** In a fixed level-j patch P adjoining the wall, insert M separated pairs from Section 1 in its frozen-side portion, avoiding every lower layer. Their contribution to squared-angle energy is `12 M a^2`, although their contribution to every level at least 1 is zero. For any fixed `epsilon_0,T,L`, choose

    M > epsilon_0^2/(12 a^2)

and then choose j large enough to fit them. The required hypothesis of LU Lemma U, `||theta(U)||_P<=epsilon_0`, fails. Energy is gauge invariant, so changing gauges cannot repair this hypothesis. No choice of T after L repairs this **uniformly in j**.

**Implication (a genuinely rough free seed; inputs explicitly restricted).** Give repair 2 the compact lift at the **identity** supplied by LN LIFT-NL, together with the dropped-block/Haar convention of mapped Text 5.2. These are named inputs, not invocations of a lift at a heavy field. In a free level-(j+1) block touching the wall, place separated level-j opposite pairs of amplitude `3T`, one next to its frozen face. All modified bonds are free; all frozen level-j bonds remain identity. Each pair has plaquettes of angle `3T>2T` and therefore forced rough labels. Take enough pairs to reach the kernel's dropped-box threshold (`m_*=c_1 L` in the stated convention); they fit in a block for large L. If there are q pairs, their bond logarithm has l4 norm `3T(2q)^(1/4)`. With T small after L this meets LIFT-NL's displacement hypothesis at the identity. Its support-truncated construction gives a fine seed whose level-j data are exactly these, whose lower frozen data remain identity, and which is identity outside the block plus its stated collar. Use this compact construction: an untruncated Whitney inverse would have tails and would not by itself keep lower data exact.

**Implication (coarse top and heavy addition).** Under the dropped-block convention, parents reading the dropped block are Haar and may take value 1; outside that block all surviving paths see identity, so choose the level-(j+1) top to be identity. This is a support statement about an admissible chain, not a claim of positive probability for an individual Haar value. A four-box patch used by the dense fill, crossing the wall, contains a frozen-side subpatch beyond the seed's compact collar but still clear of all lower layers. The seed is identity there. Pack M fine pairs there, separated from the seed's support and from its one-step read neighbourhood. Their first parents are exactly identity as before, so the whole chain from level 1 upward, including the genuine level-j rough cell and its labels, is unchanged. Their plaquette supports are disjoint from the seed's nonzero plaquettes. Hence

    ||theta(U)||_P^2 >= 12 M (T/8)^2,

with no cancellation or limiting argument. Choose j to fit M. Thus even granting the existing compact lift where it is entitled to apply, the rough-cell repair asks for Lemma U on a patch outside its hypotheses. This conditional construction is not advertised as a counterexample to AE-R or as an independent proof of LIFT-NL. It exhibits the obstruction on the rough branch, not only at a harmless zero-trigger field.

**Discharged (the actual interpolation terms).** On a patch where gauges and logarithms have legitimately been obtained, write the target as `exp(i b)` and the relative bond field as h. Interpolation uses `b+chi h`. The discrete product rule is exact with a shift in the coefficient: on an oriented plaquette the curl is a sum of `chi dh`, terms `(d chi) h`, and `db`; choosing one plaquette value of chi merely adds another `(d chi)h` term. For a cutoff varying over `r s_j` fine spacings, these terms obey

    ||(d chi) h||_2 <= C/(r s_j) ||h||_2,
    ||nonlinear remainder||_2
       <= C (||b||_4+||h||_4)||h||_4.                 (2.1)

For completeness, the second estimate has an elementary local constant. Use matrix operator norm and suppose the sum of the four bond-log norms, throughout the interpolation, is at most 1/4. For `P=prod exp(A_i)`, its exponential series bounds `||P-I||<=1/3`, `||DP[H]||<=(4/3)sum|H_i|`, and `||D^2P[H,K]||<=(4/3)(sum|H_i|)(sum|K_i|)`; here `exp(1/4)<=4/3` follows by comparing its series with the geometric series. The logarithm series on `||P-I||<=1/3` bounds its first and second derivatives by `3/2` and `9/4`, respectively. The chain rule therefore bounds the second derivative of `log P` by 6 in the summed bond norm. Its linear term is the oriented curl. Integrating the derivative of its remainder from b to `b+chi h` gives the pointwise bound `6(sum|b_i|+sum|h_i|)sum|h_i|`. Each plaquette has four links and each link belongs to six plaquettes. Hölder and these finite incidences give (2.1), for example with nonlinear coefficient 1024, also allowing the fixed shifts of chi. This argument requires the small bond-log ball; it does not construct that ball. The finite Wilson-action variation also has the term

    N D,   N=||theta(U)||_(changed plaquettes),

where D is the l2 norm of the plaquette holonomy displacement, as in LN (FD). A proposed level-j gain of order T^2 does not bound this term when the changed plaquettes read the heavy side. It is necessary either to cancel common heavy terms **before** estimating, to avoid their supports, or to pay their removal from a genuine excess.

**Discharged (the variation bound itself).** If the original and changed plaquette angles have magnitudes x,y and their group distance is d, the group triangle inequality gives `y<=x+d`. Since `sin t<=t` on `[0,pi]`, the action increase is at most `xd+d^2/2`. Summation and Cauchy--Schwarz give `N D+D^2/2`. Thus N is the actual fine curvature norm in this argument; replacing it by the level-j curvature norm is not an algebraic cancellation.

**Implication (why the high-frequency suggestion is not yet the proof).** Even grant a relative gauge and a local zero-block-mean estimate `||h||_2<=C s_j||d_b h||_2`. The cutoff term in (2.1) is then at most `(C/r)||d_b h||_2`; this explains a coefficient tending to one on a quadratic high-frequency energy. Squaring `X+Y`, however, gives `X^2+2XY+Y^2`, so a bound with coefficient `1+C/r` leaves an error `(C/r)E_heavy`. For fixed r this is unbounded relative to T^2 in the pair family. Merely replacing C_f by a constant close to 1 does not give the missing payment. A weighted estimate that pays this error from energy actually removed could work; it is not the displayed estimate. Moreover, obtaining the relative gauge and controlling the nonlinear remainder without a large `||h||_4` is precisely what Lemma U's failed hypothesis prevents. An assertion of zero coarse mean is not an estimate on either of these quantities.

**Discharged (stress test against overclaiming).** The pair family itself admits a better operation. Each pair is contained in a level-1 block and has identity data on its block boundary; deleting selected complete pairs introduces no new plaquette at that boundary, keeps every parent identity, and decreases action by exactly their total `e_A`. In its displayed gauge the links are uniformly small regardless of M. Thus the family disproves the invocation of Lemma U, not the existence of every possible nonlinear replacement. In particular using `||a||_4` to estimate many disjoint pairs loses locality which a successful proof may recover.

### 2.2 A free-side operation and the unchanged collar

**Gap (attempt to avoid crossing the wall).** Keeping all fine links on the heavy side is a legitimate alternative, but the mixed fine plaquettes are still part of the action. A direct correction of a free level-j bond must have an exact fine lift with zero change to every frozen level-j bond and every lower datum. LN's lift is an inverse on a full patch and assumes its small-energy gauge; its statement is not a half-space inverse at an arbitrary boundary field. Leaving a fine collar unchanged might isolate the correction from the heavy plaquettes, but one must then prove this restricted inverse is onto the required free coarse bonds, with curl cost independent of j, in the actual contour frames. No such assertion is proved by counting a positive fraction of free lines. Without it, the `(d chi)h` and nonlinear terms at the inner edge of the retained collar return. This route is open, not refuted.

**Discharged (which conclusion must change with the trigger).** The original end-of-stage assertion was a fine-energy bound, `A_c(U^-)<=kappa T^2`, including the c enlargement. A level-j-only trigger proves at most a statement about level-j labels and curvature. The heavy pair example has no coarse trigger but can have arbitrarily large `A_c`; it is an explicit counterexample to retaining the fine-energy end-of-stage assertion under that new stopping rule. Consequently the original use of that assertion in LOC-V and the count of all lower rough cells cannot be copied into repair 2. Lower rough cells must remain in the next-stage excess or be paid during an actual lower-scale replacement; erasing their coarse ancestor's trigger does not pay them.

## 3. Repair 1: minimize below the frozen coarse data first

**Discharged (the legal variational operation and its limit).** Choose a collar H in the frozen side, within the clearance from lower frozen layers. Fix the original fine field outside H, every lower datum, and **all** level-j bonds of the original field. Let

    m_H(U)=inf A(X)

over actual admissible chains satisfying those conditions, without requiring their lower levels to be regular. The original U is an admissible competitor. Therefore `0<=m_H(U)<=A(U)`. For every epsilon>0 a competitor `X_epsilon` has `A(X_epsilon)<=m_H(U)+epsilon`. No compactness or continuity assertion about a change of kernel labels is needed. The amount `G_H=A(U)-m_H(U)>=0` is a genuine removable excess with exactly the same data and boundary, and it must not be replaced by raw energy in H. On the isolated-pair example, if H contains the pairs with an identity boundary collar, deleting them attains the infimum and removes them exactly. Repair 1 succeeds on that example.

**Gap (where paying first asks for the unproved boundary assertion).** The restricted infimum just defined does not prove that a minimizing sequence has no rough lower cells, nor that it satisfies the box cap used in LN's minimizer paragraph. Defining the infimum only over regular lifts would assume this conclusion and could make the comparison with A(U) false or leave the fibre empty. The existing lower-stage Corollary is a theorem for its stated top and frozen data. Applying it here requires a version with the arbitrary fine outer boundary of H held fixed, including cells whose enlarged supports meet that boundary. This is not supplied by (QD), which controls coarse frozen plaquettes, nor by the lower-layer clearance, which only says which links may move. In particular a potentially rough free part of `V_j(U)` is not a class top to which that Corollary can simply be applied globally.

**Gap (attempt through the already paid rough-top comparison).** Replacing `V_j(U)` by its paid reference P before minimizing invokes the lower theorem with error `C_W T^2 |N_ref(V_j(U))|`. That is not a bound by G_H, and P also changes the parent mismatch which the current stage must restore. Near one rough free cell this error has the same order as the credit being sought, with no favorable coefficient supplied. Enlarging the raw heavy band does not prove that its action is available to pay this error. This shortcut therefore still needs the wall replacement estimate, including its actual excess and parent-restoration cost; it does not follow just from having a rough-top version of AE-R below.

**Discharged (why a raw boundary tail is insufficient).** Suppose the attempted boundary argument yields only

    E_inner <= C_target T^2 + theta^m E_outer,   0<theta<1.

For a prescribed collar of m layers, pack the outer frozen-side band with pairs. It can have `E_outer >= 12 M a^2` for arbitrarily large M by increasing j. The last term is then not bounded by any fixed multiple of T^2, even if m depends on L and T. This disproves the sufficiency of that estimate for a depth-uniform cap. It does not prove that the actual minimizing field has this large tail: the separated pairs can be removed or left untouched without transmitting it. A successful estimate must exploit that fact, for example by cancelling the common boundary field in a relative excess or by separating its fine scales. Increasing a fixed collar until its exponential beats an unbounded raw energy is not a uniform argument.

**Implication (payment without multiplication over depth).** If a boundary replacement theorem gives `G_H >= c T^2 n_H`, with n_H counting original lower rough cells removed for the first time, such relaxations can be put before stage j. Their action differences telescope exactly in the order actually performed. If the sum of all subsequent restoration costs is at most `eta sum_H G_H`, with one fixed `eta<1`, the remaining credit is `(1-eta)sum_H G_H`; there is no `(1-eta)^j`. This is the correct possible repair of the bookkeeping. Neither the nonnegativity of G_H nor an energy bound on its minimizer proves the displayed rough-cell payment. Obtaining it with the arbitrary retained boundary is the same local issue encountered in Section 2, not a second independent obstruction.

## 4. The minimizer paragraph: J depending on L does not by itself break K before L

### 4.1 A hand bound for the number of layers

**Implication (explicit assumption for this section).** Grant the cap proposed in LN: throughout the relevant lower-layer-free collar a candidate minimizing field has energy at most `K T^2` in each level-j cell. A box of `L^4` such cells consequently has energy at most `L^4 K T^2`. This is an assumption here; Section 3 explains why it has not been obtained for the required boundary problem. Also grant the existing dense-target and exact-restoration estimates when their small-energy hypotheses hold. The following argument resolves the constants issue under those hypotheses.

**Discharged (geometry).** For any finite union D of unit boxes in four dimensions,

    |D^(+h)| <= (2h+1)^4 |D|.

Each original box has at most `(2h+1)^4` boxes at sup-norm box distance at most h; taking the union can only reduce the count. This bound needs no bound on D's diameter, boundary area or number of components.

**Implication (the cluster convention needed for this improvement).** Here D is the union of the actual dense boxes, grouped by the distance graph if desired; it is not their rectangular hull with unpaid gaps filled in. Then `E(D)>=K T^2 |D|`. Its neighbourhoods are unions of boxes, to which the stated any-shape RF input applies. If a construction instead fills a large rectangular hull first, it must pay those additional boxes separately and cannot use this proof of (4.3).

**Discharged (growth versus the cap).** Group b successive box layers into a macro-layer, where b is an absolute integer large enough for all RF and restoration collars (increase b once to include their fixed widths). Set `E_t=E(D^(+bt))`, `a_t=E_(t+1)-E_t`, and use the first t with

    a_t <= delta E_t,        delta>0 absolute.            (4.1)

The value of delta is chosen small against the fill and restoration constants below. If all earlier tests fail, with `lambda=1+delta` and `gamma=log lambda`,

    E_t >= lambda^t E_0 >= lambda^t K T^2 |D|.

The assumed cap, allowing a fixed extra collar c, also gives

    E_t <= (2bt+c)^4 L^4 K T^2 |D|,

where c is absolute; choose `c>=4b+9` large enough to cover all the fixed target and patch collars below. Put `C_0=(2b+c)^4` and

    B_0=8 C_0 [1+24(2/gamma)^4].

For every integer t>=0, `(2bt+c)^4<=C_0(1+t)^4<=8 C_0(1+t^4)`. The elementary exponential series gives `exp(gamma t/2)>=(gamma t/2)^4/24`, so

    (2bt+c)^4 <= B_0 exp(gamma t/2).

Consequently failure through N tests is impossible for

    N=1+ceil[(2/gamma) log(B_0 L^4)],
    J(L)=b(N+1)+c.                                      (4.2)

Indeed it would imply `exp(gamma N/2)<=B_0 L^4`, contrary to this choice. Thus `J(L)=O(log L)`, with a fully specified depth-independent bound. No computation is involved.

### 4.2 Charge the enlarged target to the energy at the selected layer

**Discharged (the improvement over the printed K condition).** Let `C_tar T^2` bound the dense target's fine energy per box, including its fixed `b_2^2` factor, and let `C_pay` bound the coefficient of its energy in fill plus restoration costs. At the first good macro-layer t, the total target and target-restoration cost is at most

    C_pay C_tar (2bt+c)^4 T^2 |D|.

Set

    B_1=8 C_0 [1+24/gamma^4],
    K >= 16 C_pay C_tar B_1.                            (4.3)

The same elementary exponential bound gives `(2bt+c)^4/lambda^t<=B_1`. Since every earlier test failed,

    target cost / E_t
       <= C_pay C_tar (2bt+c)^4/(K lambda^t) <= 1/16.

This K is independent of L and of the first good index t. Replacing t by the worst possible J and discarding the preceding energy growth would create the spurious condition `K>=C J(L)^4`. That is not necessary.

**Implication (term-by-term reserve, not a new gluing theorem).** Suppose the available fill plus exact-restoration bounds, in Wilson-action units, have total shell cost at most `C_sh a_t`, total target cost as above, and the remaining sparse parent correction at most `E_t/16`. Choose `delta<=1/(16 C_sh)`, before K and L. Subtracting all costs from the removed core action E_t leaves at least

    E_t - E_t/16 [shell] - E_t/16 [target]
        - E_t/16 [remaining parent correction] = (13/16)E_t.

This deliberately leaves more reserve than the `1/16` needed in (4.2) of ES. If the energy estimates are instead in squared-angle units, introduce the fixed conversion constants first: on `|theta|<=1`, `(11/24)|theta|^2<=1-cos|theta|<=|theta|^2/2`. Absorb their ratios into `C_sh,C_pay,C_tar` and the initial core coefficient; make delta smaller and K larger by these fixed factors. Neither operation introduces L or depth. The existence of this shell/restoration bound at a heavy wall is still the issue in Sections 2–3; this paragraph establishes what its constants would allow, not that it holds.

**Discharged (order of choices under Section 4.1's assumptions).** The consistent order is: fixed fill/restoration coefficients and b,c; delta and gamma; B_0,B_1 and K, also meeting the original lower bounds on K; the original sparse constants C_*, eta_0, R_1 and r_* in their stated order, then eps_q; L large enough that `r_*/L` meets the sparse budget; T small enough that every four-box gauge patch has energy below its threshold; finally enough geometric clearance for `t_0>=C L J(L)+C r_*`. None of those sparse constants is assigned a dependence on the dense J(L). Under the cap, such a patch has energy at most `C L^4 K T^2`, so `T<=epsilon_patch/(sqrt(CK)L^2)` suffices for Lemma U. Any additional L-dependent smallness from the nonlinear lift is imposed on T at this same final stage. If `T=a_*/L^2`, choose a_* accordingly. This respects K before L and `r_*<<L`. The dense collar has width `L J(L)`; it is not the sparse radius r_*. It is accommodated by clearance, not by requiring `J(L)L<<L`.

**Discharged (decision on LN's minimizer warning).** J depending logarithmically on L is **not** itself a constants obstruction. The loss in the printed crude comparison is removed by (4.3). What remains is proving the cap and the relative boundary replacement for the actual minimizing problem, rather than assuming them from the Corollary whose proof is in question.

## 5. One remaining inequality, and exactly which statements it would repair

**Gap (HW, the wall excess replacement inequality).** Here is a concrete sufficient local form of the missing step. It is deliberately stronger than a bare assertion that some global minimum exists. Work in the ES stage setting: class level-(j+1) top W, the same quiet frozen data at all lower levels, and a core D whose replacement collar may cross the level-j wall but misses every lower frozen layer. Let T_D be the specified small target with the correct parents and frozen level-j bonds (the target-existence input of ES:88). For a proposed replacement X_D define, with the plaquette partition used consistently,

    G_D = sum_(p in D) [a_U(p)-a_T_D(p)],
    R_D = sum_(p in D) [a_X_D(p)-a_T_D(p)]
             + sum_(p outside D) [a_X_D(p)-a_U(p)].

All changed plaquettes, including mixed plaquettes, corrections and tails, belong to these sums. Let n_D count original rough cells, at any level still present, which this operation removes for the first time. The sought construction must keep the actual top W and every frozen datum exact, remove the chosen core's level-j defect, and satisfy

    R_D <= (1-eta) G_D - c_R T^2 n_D,
    eta,c_R>0 absolute,   G_D>0.                        (HW)

The rough-cell term is included in the inequality so that a changed coarse trigger cannot silently discard lower rough cells. In the original argument a bound on n_D from TE and the core energy would supply it from a reserved fraction of the gain; at a heavy shell that bound must itself be justified. Positivity of the core excess is not the problem for a dense core with the stated target: `A_U(D)>=K T^2 |D|` and `A_T_D(D)<=C_tar T^2 |D|` give `G_D>=A_U(D)/2` once `K>=2 C_tar`. For a sparse core the analogous comparison is its kappa threshold against the small QD target. For the full old Corollary, the construction must cover every remaining original energy/density trigger, not just coarse rough cells. Sparse collars must remain bounded by r_*, dense collars may have the `J(L)L` size of Section 4, and all must remain inside the clearance. No upper bound on the *total* energy under the frozen level-j bonds is a hypothesis. An epsilon-competitor version with error epsilon and then epsilon tending to zero is sufficient.

**Discharged (why this is the exact cost, rather than a new energy definition).** Direct cancellation gives

    A(U)-A(X_D)=G_D-R_D.

Thus (HW) would give a genuine decrease at least `eta G_D+c_R T^2 n_D`, with no frozen action counted as credit. Common high-energy plaquettes cancel before any norm estimate. This identity includes an arbitrarily energetic unchanged outer field. If parents are restored only at the final minimal lift as in LN, the corresponding budget uses the fill's complete cost **plus** the signed increment `Phi_j(W^+)-Phi_j(W^-)`; this increment cannot be omitted or bounded by raw coarse curvature without the missing local estimate. A proof using this latter budget would also settle the present stopping point; a local fine replacement is a sufficient route, not asserted to be necessary for AE-R.

**Implication (the recursion that would then be justified).** Compose actual decreases, assigning an original rough cell when it first ceases to be rough. Write B_j for the sum of their core credits G_D and N_j for the sum of their n_D. Once the level-j output is class and the restored parents are W, the variational inequality `Phi_(j+1)(W)<=Phi_j(W^+)` gives

    Xi_(j+1)(U) >= eta B_j + c_R T^2 N_j + Xi_j(U^-).

It is essential that the same constrained references occur on both sides. If the stages eliminate every original rough cell, the first-removal assignment gives `sum_j N_j=sum_k |R_k|` exactly. Telescoping then gives the class-top AE-R with `a_R=c_R`; neither coefficient is iterated multiplicatively. The rough-top error needs the separate paid-top construction of ES. The original raw `sum E(s)` in ES (4.2) can be retained only if a replacement theorem actually pays those E(s). Otherwise it must be replaced by B_j. A separate nonnegative heavy-field potential is also possible, but its change must telescope exactly and vanish or have a controlled endpoint; an added error per depth does not suffice.

**Implication (the Corollary must state the conclusion actually proved).** Payment for all remaining fine-energy and dense-box triggers would force their absence in a minimizer and recover the original non-concentration conclusion. Repair 2, with only coarse triggers paid, can at most force absence of those coarse defects. It would need a separate proof of the fine-energy cap before LOC-V or any fine gauge argument could use that cap. This is a precise weakening of the Corollary, not evidence that the original non-concentration statement is false. Repair 1 could supply the stronger conclusion by a boundary-uniform relative replacement and the now harmless `J(L)` argument.

**Gap (why the attempted routes stop at HW).** For the original algorithm, the selected shell does not exist in Section 1. For repair 2, the available estimate for R_D requires the fine gauges which fail on the rough-seed/heavy-wall patch; even granting a gauge, a coefficient `1+epsilon` on raw heavy shell energy leaves an unpaid term. The free-side variant needs an exact restricted lift and its mixed-plaquette estimate. For repair 1, a constrained infimum supplies a nonnegative removable excess but no bound on this boundary replacement cost, while a raw exponential tail is not uniform in depth. The rough-top shortcut has an unpaid error of the same order as the intended credit. These are attempts at the same cost inequality, not proofs that every repair fails. Section 4 removes the constants objection once the required minimizing-field cap and local cost estimates are established.

**Gap (what would settle it).** A written construction of X_D, or of the final-lift version of its cost, must control the cutoff-relative-connection term, its nonlinear remainder, and the simultaneous frozen/parent restoration in R_D by removable excess, uniformly in depth and arbitrary retained fine boundary data. A decomposition into fine-scale relative fields with a summable cost, or an exact free-side inverse avoiding the heavy supports with a proved mixed-plaquette bound, could provide it. Conversely an admissible configuration for which every allowed replacement violates (HW) would refute that proposed local repair. It would refute AE-R itself only if its signed excess violated AE-R with the exact same data and class reference. The displayed pair configurations do not do that.

## 6. Consequence for FALL through (UP), (WAM) and (GLUE-E)

**Unchecked (the other consumer inputs).** This note does not reprove EX, the trial estimate, class-minimum identification, flux decay, or the weighted kernel moments. The following implication uses their stated formulations in `excess-shell-end.md`, Sections 1, 2 and 4.2, and the rate calculation in `excess-seam.md`, Section 2.

**Discharged (the distinctions that matter here).** (GLUE-E) asks for an admissible replacement's **complete** R_D, with all intermediate fields in its defining class, bounded by a localized shell sum of the two endpoint actions. It is not supplied by the failure or success of a raw dense-box trigger. (WAM) asks `A_U(w)<=[1+D_A(L) nu_l] A_T(w)` uniformly in depth, including `nu_l=0`. (UP) bounds `Y_l=E_0-E_l` by `C_TOP(L)a_l+D_TOP(L)[(f_l+nu_l)E_l+tau_l]` at every partial top. In the cited implication from WAM to UP, the trial estimate and a fine-flux bound on the specified minimizer are explicit additional inputs. A class top alone supplies neither its fine-energy gauge nor that identification.

**Implication (what survives, and what cannot be used).** The elementary implications `GLUE-E -> shell comparison -> WAM -> UP`, and the scalar deduction of FALL from UP plus its other inputs, are not refuted here. Their use beside a frozen wall is still conditional: the present stage cannot supply the required class-minimizer/non-concentration inputs, and the proposed use of Lemma U for the nonlinear seam can read arbitrarily large fine energy. The heavy fields in Section 1 are not the specified class minimizers of WAM, so they are not counterexamples to WAM, UP or FALL. There is no conclusion here against a version of FALL that has no such frozen data and proves its own hypotheses independently.

**Implication (a warning after a successful repair, with its exact condition).** Even proving HW and the non-concentration input would not by itself prove the weighted nonlinear GLUE-E estimate. If a shell proof has coefficient A_s(L), top-unit radius r(L), and kernel exponential moment M_*(L), its stated absorption at the required spatial rate nu_req still needs

    2 A_s(L) M_*(L) sinh(nu_req r(L)) < 1.

The factor arises by integrating superlevel shells: their weight integral is at most `2 sinh(nu_req r) w`, and transferring the kernel costs M_*. A logarithmically growing dense radius can therefore be harmless for K yet require fresh work for this weighted condition. FALL's depth contraction q(L)<1 and this spatial weight rate are different constants. Neither a loss per depth nor silently reducing a rate already fixed by a downstream consumer repairs the route.

## 7. Reading and decision boundary

**Unchecked (coverage).** Read GOAL and the three required FINISH sections first. Scientific reads were bounded portions of LN Sections 1, 3, 4's statement, 5.2–5.4 and 6–7; ES Sections 1–5 and the end of 7–8; PE Sections 1–4 through its layer construction; RD's numbers, Proposition 10 and nearby displayed statements; LU's setting, Lemma U and F/RF; the excess contract Section 1; mapped Text 3.1 and 5.2, plus bounded search excerpts; `sector-values.md`'s FALL statement and scalar proof; `excess-shell-end.md`'s UP, WAM, GLUE-E and WAM-to-UP calculations; `excess-seam.md`'s rate calculation; and short setting excerpts from `quiet-boundary-rarity.md`. Filename/content searches were restricted away from the forbidden paths. Search excerpts of `seam-nlpay.md` were used only to locate these consumer definitions; no conclusion relies on its proof. Repository methodology absent from the sparse working tree was read through `git show` at the pinned commit. No excluded file, external account, paper or independent-side proof was opened. No remembered theorem supplies a discharged step.

**Discharged (scope of the negative decision).** The corrected hand profile defeats ES's prescribed layer selection. It does not defeat all possible fills or the target inequalities. Both requested repairs were attacked at the boundary cost, including an actual rough-cell branch conditional only on the existing compact identity lift and kernel convention. Neither is completed or ruled out. The logarithmic-layer constants issue is resolved conditionally in Section 4. The single mathematical stopping point for this item is **(HW), the wall excess replacement inequality**, with the constraints, cost and possible settling arguments in Section 5. Other imported lemmas remain unchecked inputs, not extra conclusions of this report. No audit, status change, commit, push, PR, post, subagent or other file edit was performed.

STOPPED
