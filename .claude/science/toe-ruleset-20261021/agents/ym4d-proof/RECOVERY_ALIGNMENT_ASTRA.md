Model/effort provenance: coordinator's tool dispatch explicitly selected `gpt-6-astra`, reasoning effort `max`, fork_turns `none`; this worker's system identifies the GPT-6 family but does not itself expose a more precise runtime ID.

# Recovery of the periodic/log-chart background-transfer worker

Status: open research continuation; mathematical support only, no audit verdict.
Source snapshot: coordinator supplied baseline HEAD `46dc04b05c5842a03ae3af64caa77628f099128f` plus preserved uncommitted `ALIGN3_55.md` (249 lines). I do not independently attest the git identity: this worker is prohibited from git operations. Procedure source: this worktree's methodology/physics-loop references, freshness unverified against remote under that scope restriction. Writes are restricted to this note and `checks/recovery_align_*`; no original source edits, shared-summary edits, audit changes, commits, publication, or unattended execution.

## Pre-stated targets and checks

1. Test the proposed PER-1..4 periodic completion from the infinite-lattice cochain algebra. Explicitly distinguish merged single-path weights from separate image paths; include harmonic constants, winding, root restriction and a wrapping torus. Independent check: build one-dimensional subdivision from exact interpolation weights, use a tensor chain contraction rather than importing the saved checker, and compare the completion equations.
2. Test the claimed periodic P2-tw(log) bound in the stated `0 < alpha < theta <= sigma <= 1`, `alpha + theta <= 1` window. Recompute every own/coarse-unit exponent and the input-level sums, including unweighted `G_0`, and inspect the actual Campanato definition and charge decomposition. A slot outside the claimed uniform envelope or an unsupported identity defeats the claimed proof; a finite numerical check cannot establish an infimum inequality.
3. Work toward AC(log), source-infimum restriction and covariant output conversion. Seek a completed lemma under exact stated premises or an explicit matching-domain counterexample. A conditional reduction is not a closed background-transfer theorem. Failed routes remain recorded.
4. For any exact computation, freeze its expected identities and controls before running. Do not tune thresholds to observations. Use a second derivation wherever useful and state what it does not establish.

Claim metadata: actual_current_surface_status=open; target_claim_type=bounded_theorem; trace_class=upstream_support; reachability_to_target=partially_closes; conditional_surface_status=null; hypothetical_axiom_status=null; admitted_observation_status=null; audit_required_before_effective_retained=true; bare_retained_allowed=false.

No physical axioms or primitives are being added. This is a conditional finite-lattice Yang–Mills analysis with its supplied geometry, action, source and norm definitions; it does not derive those physical identifications from the repository's foundation axioms.

## 1. Periodic completion: what survives the independent reconstruction

**Exact support, with the image definition essential.** Write `D` for the scalar-to-link difference and `d1` for link-to-plaquette curl. On the infinite cubical lattice, assume the supplied interpolation/contour maps satisfy `MD=I-S0 R`, `B D=D R`, and `D S0=S1 D`. Then `E=DM-I+S1 B` obeys `E D=0`. Every row `z_b` of `E` is therefore a 1-cycle. This follows directly by evaluating `E D` on point-supported scalar functions; it does not assume the torus has trivial cohomology.

An explicit bounded homotopy is available on the universal cover. Fix the tail `p` of the output link. For each oriented input edge `e`, fill `gamma(p,tail e)+e-gamma(p,head e)` by the axial ladder of plaquettes. Its number of plaquettes is at most `|tail e-p|_1`, and it stays in the coordinate box spanned by `p` and `e`. The signed sum of these ladders with coefficients `z_b(e)` has boundary `z_b`: all radial paths cancel because `boundary z_b=0`. Thus `E=F d1`. Finite first moments of the rows make the sum absolutely convergent. Finite range is preserved; exponential decay is preserved with a possibly smaller exponent (polynomial factors are absorbed into that reduction).

Translation covariance modulo `L Z^d` converts the row-first-moment bound into a column bound: group output links into their `d L^d` residue classes, translate the fixed input plaquette through each class, and bound the resulting sum by each row's total filling mass. In particular

`sup_P sum_b |F(b,P)| <= d L^d sup_b sum_e |z_b(e)| |tail e-tail b|_1`.

Periodizing the kernels, including the paths before images are merged, commutes with composition and with `D,d1`: this is an absolutely convergent rearrangement of lattice sums on periodic lifts. The same supremum row/column bounds hold, including for wrapping tori. This proves PER-1 and the factorization part of PER-3 in arbitrary finite dimension. PER-2 follows from the endpoint identity of each lifted path and interpolation of affine functions. Constant 1-forms are killed by `sum_Y a(y,Y)(y-Y)=0`. The torus's harmonic modes are handled by this last equation, not discarded.

Taking transposes gives the precise PER-4 slots for an input divergence `D^T w` at level `l`:

`-<w,x_l> + sum_{m=l}^{k-1}<w_{m+1}, Bx_m-x_{m+1}> - sum_{m=l}^{k-1}<F_m^T w_m,d1 x_m>`,

where `w_{m+1}=S1^T w_m` and `x_k=0`. The terminal term vanishes for that stated reason. Root restriction and the hierarchical left inverse then follow from `R M=0`, `R S0=I`, and the recursion. The first-moment Taylor argument plus the supplied spline nesting/derivative bounds gives P1'(img) with the **sum** of its three norm constants, as corrected at the end of ALIGN3 §1.4. This is support for the spline image construction; the compact four-point subdivision still needs its own regularity range.

**Computational check.** `checks/recovery_align_exact.py` independently solves cyclic spline interpolation at coarse counts 3,5,9. In one dimension, every periodic form is an exact form plus its constant mean. Since image M and merged M agree on exact forms, the uniquely determined correction is `M_img=M_merged(I-h)`. The code derives S1 independently from `D S0=S1 D` and its row sum `1/L`, then verifies `M D=I-S0R`, `M1=0`, and `D M=I-S1 B` entrywise. All pass. The uncorrected merged operator fails both harmonic cancellation and completion in all three cases, with its y=1 harmonic values `-8/9`, `40/99`, `8/153`. These agree with the older counterexamples without reusing their implementation. This is a finite one-dimensional check; the arbitrary-dimensional conclusion is the chain proof above.

## 2. P2-tw: sufficient window confirmed, with two bookkeeping repairs

Let `h_m=L^{-(k-m)}`. The spline scalar column mass after n refinements is at most `3^d L^{dn}`: its cardinal basis is the B-spline convolved with the inverse-collocation coefficients of absolute sum 3, and the nonnegative B-spline samples at spacing `L^{-n}` sum to `L^n`. For the differentiated direction, integrate the derivative of the cardinal step interpolant over the fine edges; its total variation is at most 3. Tensoring yields the claimed `3^d L^{(d-1)n}` bound for S1. This independently justifies the two column-growth rates needed by PER-4. Periodization cannot increase the absolute sums.

For a divergence input at level l of coarse current size `pi=h_l^{-3}|w|`, the explicit PER-4 representation has, at output level m>=l,

- one plain slot at l, cost `pi` for l=0 or `h_l^{-theta} pi` for l>0;
- residual cost at most `C L^theta h_{m+1}^{1-theta} pi`;
- positive-level curvature cost at most `C h_m^{1-alpha-theta} pi`, and level-zero curvature cost at most `C h_0^{1-alpha} pi`.

The last estimate uses exactly the source Campanato definition in BFT_A §7.2: box side is at least h_m, so `[G^c]_alpha <= h_m^{-alpha} sup|G^c|`. This is a valid bound even for an oscillatory filling. The extra separate G0 term in COFUN_CC's N is charged as well (at most one extra copy of its level-zero bound).

The G_l commutator divergence has `pi <= C eta sup|G_l^c|`. Thus positive input levels sum with `h_l^theta`, and at fixed m,

`sum_{1<=l<=m} h_l^theta <= h_m^theta/(1-L^{-theta})`.

The resulting curvature envelope is `C eta h_m^{1-alpha}/(1-L^{-theta})`; residuals are bounded likewise. The unweighted G0 divergence instead gives `C eta h_m^{1-alpha-theta}`. Consequently **alpha+theta<=1 is a sufficient window for this representation**, including equality. It does not require a logarithmic loss at equality: G0 is one input slot and the output norm is a maximum, not a sum over m. The point-charge costs are `C eta h_m^{1-theta}` times geometrically summable input strengths. Residual-slot divergences carry `h_{l+1}^theta`; their two incident levels obey the same geometric sum. This rederives the qualitative P2 estimate for every permitted input representation, so taking the full input infimum is legitimate here.

Two corrections to the saved prose are necessary. First, its Step 4 positive-level G bounds must include the geometric factor `(1-L^{-theta})^{-1}` when summed over input levels; its unspecified final constant can absorb it. Second, the Phi divergence from a G slot gains **one** power `h_l eta` relative to its principal divergence, not the two powers claimed in the bullet `Phi-divergences (j_l,G_l)`. Indeed `G_l=h_l^2 G_l^c`, `Phi=O(h_l^2 eta^2)`, so `pi(w_B)=O(h_l eta^2 G_l^c)`. The j-slot Phi correction does gain `h_l^2 eta`. The weaker correct gain is sufficient in the stated window; no claimed conclusion needs the erroneous extra power.

The paragraph asserting that EVERY alternative curvature representative must have a comparable oscillation is not established by the argument given: a prescribed divergence alone does not prove the asserted lower bound in the full source infimum, which can redistribute between slots. I retain only the sufficient upper-bound theorem. P2 outside this window remains open, not refuted. In particular the exact exponent control in the script is a failure of the extended *upper-bound argument*, not a counterexample to P2.

Conditions retained: the analytic local gauge-generator/soft-residual definitions and the background sizes in the global `M^(sigma)` class; `0<alpha<theta<=sigma<=1`, `alpha+theta<=1`; the spline image maps above. These do not supply a global critical background or the flat inverse theorem.

## 3. New direct AC(log) lemma: centered contour moments replace LA-pol

**Statement (author proof, independent review pending).** Fix odd L>=3, dimension d=4 (the proof works in any fixed d), `0<alpha<theta<=sigma<=1`, and a real log chain y with `||y||_(sigma)<=eta` in the fixed analytic log chart. No critical-point equation is assumed in this lemma. Let mu vanish at level-k roots and have ALIGN55 §4's exact norm

`M=||mu||_C=max_l(sup|mu_l|+sup|nabla^c mu_l|+[nabla^c mu_l]^infty_theta)`,

with `mu_l=ev^(l)mu`. Let B be LINEAR_PACKAGE §1.2's centered, order-paired S4' root map. With the exact log generator

`K'_y mu(b)=-[y(b),mu_bar(b)]-(1/2) Phi(ad_y(b)) D mu(b)`,

there is `C_AC(d,L,N,alpha,theta,sigma,eta_*)`, independent of k,T, such that

`|||K'_y mu|||_(1,sharp) <= C_AC eta M`, for `eta<=eta_*`.

Here sharp is precisely BGT55 §6.2, including the summed N_res; the field and residual norms use their stated coarse units. The proof uses only the flat residual control already in `||y||_(sigma)` and the contour's **linear** moments. It does not invoke TR-1, a nonlinear covariance identity, or the still-unwritten LA-pol estimate.

### 3.1 Exact midpoint moment identity

Place the initial root at 0, the final root at `L e_nu`, and let an offset z range over the centered box `{-o,...,o}^d`, `o=(L-1)/2`. For any fixed coordinate order, the contour is `P_z`, the straight L-step nu segment, then the reverse of `P_z` translated by `L e_nu`. For a signed positive edge b of direction i, let `m_b=tail(b)+e_i/2`. If beta_b is the averaged signed coefficient of b in B's row, then

`sum_{b:dir i} beta_b = L delta_(i,nu)`,

`sum_{b:dir i} beta_b (m_b)_j = (L^2/2) delta_(i,nu) delta_(j,nu)`.

Proof: the two axial pieces cancel in the zeroth moment. Their first-moment difference is `-L delta_(j,nu) z_i`; the straight piece contributes `delta_(i,nu)(L z_j+(L^2/2)delta_(j,nu))`. Averaging z gives the formula. It holds for every coordinate order before that order average. In particular

`sum_{b:dir i} beta_b (m_b-m_c)=0`, `m_c=(L/2)e_nu`.

This exact formula is the missing cancellation. An uncentered offset box leaves the displayed z terms. The proof occurs on a lifted local contour and therefore also applies when the torus contour wraps.

### 3.2 Principal commutator residual

At level l put `h=rho_l`, `H=rho_(l+1)=Lh`, `a_l=y_l/h`, and `A_l(b)=-[y_l(b),mu_bar_l(b)]`. Since the coarse endpoints are the restrictions of the fine gauge function,

`r_l(A)=-[r_l(y),mu_bar_(l+1)]-sum_b beta_b [y_l(b),mu_bar_l(b)-mu_bar_(l+1)]`.  (AC1)

This is an exact expansion of `B A_l-A_(l+1)`; it explicitly includes the independent next-level background y_(l+1). When l=k-1 the next-level gauge function is zero, so A_k=0 and the same identity applies.

Choose, for each orientation i, the constant fine reference `a_i(0)` and the fine gradient `g=nabla^c mu_l(0)`. Discrete Taylor summation along the finitely long lifted paths gives

`mu_bar_l(b)-mu_bar_(l+1) = h g dot (m_b-m_c) + E_b`,

`|E_b| <= C_(d,L,theta) H^(1+theta) M`,

and `|a_i(tail b)-a_i(0)| <= C_(d,L) H eta`. Taylor summation is valid on the periodic lift. For distances greater than one coarse unit, use `2 sup|nabla mu|` in place of the local seminorm; the fixed support diameter only changes C. The coefficient of the constant reference `h a_i(0)` against the affine part vanishes by §3.1. The remaining terms have sizes

`C eta M (h H^(1+theta)+h H^2) <= C eta M H^(2+theta)`,

because `H<=1`, `theta<=1`, and L is fixed. The first term in (AC1) is at most `2 eta M H^(2+sigma) <= 2 eta M H^(2+theta)` by the **flat** residual component of the assumed background norm. Therefore

`sup_own |r_l(A)| <= C eta M H^(2+theta)`.  (AC2)

This calculation supplies a different derivation of the required small factor; it does not inherit an unproved polarized contour estimate.

### 3.3 Even analytic remainder and the field norm

Let `R_l=-(1/2)Phi(ad_y_l)D mu_l`. On a fixed small analytic ball, `||Phi(ad_y)||<=C|y|^2`, hence

`sup_own |R_l| <= C h^3 eta^2 M`.

The finite row mass of B and the identical next-level bound give `sup|r_l(R)|<=C H^3 eta^2 M` (R_k=0). This is bounded by `C eta^2 M H^(2+theta)` for theta<=1.

For the potential/gradient/Campanato components of A^c, use the discrete product rule on `-[a_l,mu_bar_l]`. The assumed C^(1,alpha) control of a_l and C^(1,theta) control of mu_l yield `||A_l||_(C^(1,alpha))<=C eta M`, uniformly. Campanato products use the elementary bounded-factor oscillation inequality; pointwise control of a_l follows from its gradient supremum, and pointwise control of its gradient from the lattice Campanato embedding already identified in BFT_A BL-C.

The remainder needs no extra derivative of mu. For a level-l array F^c, the direct discrete inverse bound is

`||F||_(C^(1,alpha)) <= C h^(-1-alpha) sup|F^c|`, for h<=1.  (INV)

Indeed a difference quotient is at most `2 h^-1 sup|F^c|`, and the Campanato box side is at least h. Applying (INV) to `R_l^c=O(h^2 eta^2 M)` gives `C h^(1-alpha) eta^2 M`, uniformly bounded since alpha<1. Thus no C^2 regularity of mu is silently assumed.

### 3.4 Sharp residual and the full N_res sum

Combining (AC2) with the remainder, `sup|r_l(K'mu)^c|<=C eta M H^(1+theta)`. The sharp residual multiplier is `H^(-1-theta)`, so its maximum is bounded. Applying (INV) at the **residual's level l+1** yields

`||r_l(K'mu)||_(C^(1,alpha)) <= C eta M H^(theta-alpha)`.

For N_res, l=0,...,k-2, so `H=L^-q`, q>=1. Consequently

`N_res(K'mu) <= C eta M sum_(q>=1)L^(-(theta-alpha)q)`

`= C eta M /(L^(theta-alpha)-1)`.

This completes AC(log) including its previously missing summed leg. The k=1 sum is empty. The strict condition alpha<theta is load-bearing; no statement at equality is inferred.

**Discriminating checks actually run.** The exact script enumerates all centered order-paired contours in dimension four at L=3,5 and verifies both moments in every direction. Lower-corner and single-transverse-offset controls fail the cancellation. For explicit noncommuting affine data at L=3, the principal residual is `(2,-4,-5)/27` at h=1/3 and shrinks by exactly 1/27 each refinement; constant-background/affine-gauge residual is zero. The uncentered control retains quadratic scaling 1/9. These are local polynomial identities, not full periodic gauge examples and not certificates of analytic constants. The analytic bounds are the proof above.

## 4. Restricted source cost: a precise consumer interface

For a fixed finite lattice, let `R0(f)` be the flat representations of f with G_l=0 for l>=1; all plain-current and residual slots remain available. Define

`N0_1(f)=min_(R in R0(f)) [ ||G0^c||+[G0^c]_alpha + ||G||_Y + ||j0^c||+||j||_Pc+||s||_R ]`.

The G0 term appears both separately and inside Y because that is the actual COFUN_CC convention. Define `N0_Z` by the identical restriction in the covariant representations. These are finite, attained norms for every fixed k,T: the all-plain-current representation supplies surjectivity; the representation cost is a norm on a finite-dimensional slot space; a bounded minimizing sequence has a convergent subsequence in the closed affine synthesis fiber. This existence statement supplies no uniform comparison to the unrestricted norm.

For every R in R0(f), the exact inequalities

`sum_(l>=1) pi_l(j_l) <= ||j||_Pc/(L^theta-1)`,

`||s||_(R(theta))=L^(-theta)||s||_R`

give the quotient representation cost in KFACTOR_OFF55's sigma=theta pair at most

`C_N N0_1(f)`, `C_N=max(1,(L^theta-1)^(-1))`.

This is the corrected consumer interface identified by CODEX_REVIEW_ALIGN2 F3, now stated with existence/attainment and the exact cost domain. In particular an L2/CONV-P response estimate implies

`||u_Gamma||_(theta) <= 2 G (1+C_projection eta) C_N N0_1(f)`

under L2's stated smallness and critical-slice hypotheses. A consumer supplying one explicit R in R0 may replace N0 by that explicit cost. It may **not** replace N0 by the smaller unrestricted N1 merely because such a representation exists. Every finite source possesses one, so that existence condition would impose no useful restriction.

### 4.1 A source-chart conversion that preserves the restricted class

This lemma is conditional on the covariant-source dictionary used by BGT55 §2.2: curvature slots pair with the local transported `d_Z`, residual slots pair with the derivative of the same analytic root residual, and plain slots pair with left-trivialized links. It does not identify a different consumer's unnamed norm with this dictionary.

Use `J:left-trivialized -> log`, `w=J^-1 v`, `f=J^-T S`. For a covariant representation `(G,j,s)` set

`E_G=d_Z J^-1-d`, `delta_l=D rho_l(y)-r_l`,

`G_flat=G`, `s_flat=s`,

`j_flat=J^-T j + E_G^T G + sum_l delta_l^T s_l`.

These are exact identities of linear functionals. In the fixed local analytic ball, finite incidence and nearest-link transport imply `E_G=O(h_l eta)` coefficientwise; the unenhanced local residual derivative obeys `delta_l=O(H eta)`, `H=h_(l+1)`. No smoothness of the test vector is needed for these coefficient bounds.

The G correction has own current size `C h_l eta h_l^2 |G_l^c|=C eta h_l^3 |G_l^c|`. Thus its P0/Pc cost is at most `C eta` times the original G cost at every level. For the s correction, the actual R norm gives

`|s_l| <= L^(-theta) H^(2+theta)||s||_R`.

Multiplying by `C H eta` and converting to the lower-level Pc currency `h_l^(-3-theta)` costs at most `C L^3 eta ||s||_R`; the upper-level currency costs at most `C L^(-theta) eta ||s||_R`. Only two neighboring residual levels contribute to any output level. The level-zero P0 cost is smaller than this Pc envelope. The transformed plain current changes its cost by a factor `1+C eta`.

For the remaining G seminorm, transporting a field to a box corner along a path of coarse length O(r) changes it by at most `C eta r sup|G^c|`. Therefore the ordinary Campanato seminorm is at most its covariant counterpart plus `C eta sup|G^c|`, since `r^(1-alpha)<=1`. This bound also holds on wrapping boxes by lifting the stipulated axial paths. It uses connection smallness in the supplied global chart, not merely small curvature.

Combining these estimates representation by representation and then taking the infimum proves

`N1(J^-T S) <= (1+C_SC eta) N_Z(S)`,

and, because the construction creates no new G slots,

`N0_1(J^-T S) <= (1+C_SC eta) N0_Z(S)`.

Constants depend on the fixed finite stencils, analytic radius, L,N,alpha,theta, not on k,T. For complex backgrounds, replace orthogonal-transport estimates by their `exp(C eta)` bounds on paths of coarse length <=1 and cap them on the fixed ball. A source dictionary with long or unspecified transport paths is outside this statement. This is an author-level proof of a local source-chart estimate for the pinned dictionary, not an audit of every downstream consumer.

## 5. Boundary of this continuation and exact remaining work

The completed new mathematical result is **AC(log) with the full summed N_res**, derived from the exact centered midpoint moments. The image-path completion and P2 sufficient window have been independently reconstructed; the source-infimum interface and the local covariant-source pullback have explicit quantifiers. They remain provisional author support pending independent checking.

**The full covariant field conversion NC(log) is not closed in this note.** It must establish

`|||J^-1 v|||_(Z,sharp) <= (1+C_NC eta)|||v|||_(1,sharp)`

for the same actual root-residual linearization, including transported derivatives and covariant N_res. The direct AC lemma is not that statement: its input is a gauge function and its output is K' mu. Substituting a generic field v into the AC proof would change its domain.

A concrete next route is available, but is recorded as an obligation rather than counted as proved. Let `H_l(a)=log Mbar_l(exp a)`, `F_l(a)=H_l(a)-B a`. For constant direction-wise a, paired contours have the form `P_z exp(L a_nu) P_z^-1`; centered offsets cancel their quadratic term. One should write the complete polarized estimate

`|D F_l(y_l)v_l| <= C [ |y_l| osc(v_l) + osc(y_l)|v_l| + |y_l|^2 |v_l| ]`

for the actual W0-projected mean on a fixed analytic ball. Then keep the independent next-level log using the exact two-variable function `log(exp(-b) exp(b+t))`, with `t=r_l(y)+F_l(y_l)` and direction `r_l(v)+D F_l(y_l)v_l`. A bound `|(D rho_l-r_l)v|<=C eta H^3 |||v|||sharp`, plus the inverse estimate (INV), would sum its C^(1,alpha) residual error as `sum H^(1-alpha)`. The remaining transported-gradient and residual norm comparison must be written for the exact convention in BFT_B §12.0. The finite moment/BCH2 checks above support the quadratic premise only; they do not establish this all-order output theorem.

Other retained obligations and limits:

- Existence of the global critical background, the lane-A linear inverse/nonlinear contraction hypotheses, flat RW-sharp and the specified reference projection bound remain supplied inputs. This note has not reconstructed those upstream proofs.
- The full background-transfer assembly also needs the matched HD/FW estimates, smallness fixed after valid operator constants are frozen, and the covariant field conversion just identified. The already-known GA/RED'' algebra is only an implication from those inputs.
- The P2 window is `alpha+theta<=1`, with `0<alpha<theta<=sigma<=1`. The usual `(alpha,theta)=(1/4,1/2)` is included. No necessity theorem or unrestricted P2 claim above that window is supplied.
- Exponential-weighted versions, local-to-global extension outside the gauge saturation of C_glob, arbitrary curvature-small backgrounds, and full Yang–Mills existence/OS/nontriviality are not conclusions of this continuation.
- No new audit verdict, branch status, master tally, or theorem closure is declared. The older Codex refutations of merged one-path periodic M and of the unrestricted-infimum inference remain valid; the image construction and restricted cost address their precise escape routes.

## 6. Check record and handoff

Read mathematical sources: all 249 lines of ALIGN3_55.md; CODEX_REVIEW_ALIGN2.md (its complete arguments and final banking boundary); relevant exact definitions/proofs in ALIGN2_55 §1.4-1.6 and §2.2-2.8, COFUN_CC §1, BGT55 §2 and §6, ALIGN55 §4, KFACTOR_OFF55 §1.1-1.2, BFT_A §7.2, BFT_B §12.0/§15.0 and DICT55 O10/O11. Historical brief and REVIEW_BRIEF_55 read as recovery context; their old model/write restrictions are superseded by the present coordinator scope. The procedure files were read locally without git or remote refresh. No literature-based novelty claim is made.

One newly written exact checker was run, with criteria saved first. All stated finite identities and deliberate controls passed; stderr is empty. Reproduction:

`python3 -I -B .claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks/recovery_align_exact.py`

Artifacts: `checks/recovery_align_exact_criteria.md`, `checks/recovery_align_exact.py`, `checks/recovery_align_exact_out.txt`, `checks/recovery_align_exact_err.txt`. The recorded output is from the actual run; no old script was imported, rerun, or altered. There was no failed checker run to suppress. The failed extensions retained in the science are the merged periodic construction, uncentered moment control, outside-window upper-bound control, and the unsupported necessity argument; their scopes are distinguished above.

Suggested focused review: first challenge (AC1), its exact midpoint cancellation, and the coarse-unit inverse bound that closes N_res; then inspect the source-chart dictionary and slot prices. The next research action is the all-order **generic-field** NC(log) proof in §5, not another conditional restatement of R2.

Final author-support table (not audit verdicts):

| Item | Supported scope | Remaining condition |
|---|---|---|
| PER-1..4 | Exact periodic image/cochain construction, arbitrary fixed dimension | Kernel decay and the displayed commuting-pair hypotheses; satisfied by the specified image spline construction |
| P1'(img) | Spline image gauge regularity with the corrected sum constant | Supplied spline interpolation/derivative bounds; compact s3 regularity is separate |
| P2-tw(log) | Representation-wise full-N estimate for alpha+theta<=1 | Global background sizes/local analyticity; geometric-factor and Phi-G corrections above |
| AC(log), new | Direct proof including summed N_res, alpha<theta<=sigma<=1 | Small real log chain in M^(sigma); centered order-paired B; independent review pending |
| Restricted infimum | Finite attained N0 and exact L2 source-cost interface | Cannot be replaced by the smaller unrestricted N without another theorem |
| Source chart | Full and restricted infimum estimates by explicit slot conversion | Precisely the local covariant-source dictionary stated in §4.1 |
| Covariant field NC(log) | Open; concrete next proof mechanism recorded | All-order generic-field residual estimate and complete transported-norm comparison |
| Full R2 | Remains a conditional assembly | Upstream inverse/background inputs, HD/FW, reference bounds, NC(log), and frozen smallness constants |

Source hashes and check hashes are recorded in `checks/recovery_align_source_receipt.json`; they identify the files read, not scientific approval or complete-file reading where only bounded sections were used. The primitive registry was inspected: no registered physical primitive is used as a missing premise or as a new physical identification in this finite-lattice result. The only write-set of this worker is this report and the five `recovery_align_*` check/receipt artifacts.
