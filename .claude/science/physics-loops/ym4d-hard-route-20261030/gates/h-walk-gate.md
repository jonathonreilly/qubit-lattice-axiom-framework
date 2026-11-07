# Gate of h-walk (queue row 120)
Provenance: OpenAI Codex (GPT-6; xhigh requested for row 120, exact backend/effort not independently exposed), checkout `44dbf84faf41a67a7ec0081cdc9adb241c1209c6`; Sussman–Alpoge outline commit `31a47c543775`; hand mathematical review, research text, not an audit, grants no status.

Credit: the outline's operators, walk conventions, auxiliary-system and tree mechanisms, and decoupling argument are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. SA line numbers below refer to their pinned `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`. Tadeusz Balaban supplies the cut-down-sequence and generalized-random-walk method, particularly CMP **99** (1985), 389–434, pp. 408–410. His OCR was read in place outside the repository. The reviewed `library/h-walk.md` is Claude's text.

Scope: all sections, including the independent checks after a failed step. (I1)–(I3) remain premises; their proofs are not being gated here. ADVANCE means a valid research implication in the stated scope, not a status award. No computation discharges any step. Only this report is edited. The sparse checkout's workflow and applicable claim-review guidance were read from this same commit with `git show`; the user's one-file, no-delegation instructions govern.

## 0. Disposition — WRONG

**First unsupported claim:** “Proved as an implication” for the full Theorem H, including its region-trace and isometry clauses; §§3 and 8 below exhibit the failures. Independently, “Theorem VI reads this form verbatim” is false: row 114's D4 already replaces its monomial and its collar estimate. In particular, the carrier can extend `C_L M_1` beyond the tree, so a collar with an unexplained `O(1)` subtraction is insufficient. The algebraic construction and the conditional consumer must be judged separately. The repair is the collared implication in §9 below, with the actual parameter monomial. Whether the walk premise itself survives is addressed in §§3–8; this disposition cannot certify it in advance.

## 1. Statement and consumer — WRONG

**First failing step:** “Nothing else of statement 5 is read there.” The use of mechanism (i) also reads root support, a bounded number of roots at a left endpoint, and a carrier within `O(M_1)` of the cells; the naked norm/count premise does not contain these. D4's length-zero counterexample applies to that stripped premise. The definitions and distinction between the `M_1^{-1}` target and the proposed `M_1^{-1/3}` replacement are otherwise correct. This is a modified walk theorem, not the exact displayed SA exponent. **Repair:** explicitly include the support/carrier conditions later written in (H2)–(H3), and use §9's repaired consumer. Balaban's cited local-model method does not itself supply the independent-current or tree extension.

## 2. Counterexample tests — WRONG literally; the two principal conclusions survive

**First failing step: 2.1's mixed-term sign.** In its conventions,

`1 - (1/2) Re tr(exp(i gamma) exp(-i epsilon T))`

has mixed term `-(epsilon/2) Re tr(gamma T)`, not plus. A direct repaired test takes `T=diag(1,-1)` and `gamma=tT`: the summand is `1-cos(t-epsilon)`, whose linear coefficient is `-sin(epsilon)` and whose second derivative is `cos(epsilon)`, instead of `0` and `1` at epsilon zero. This confirms failure of full gauge covariance of the ambient soft-gauge Hessian. Under block-constant gauges the two endpoints of each axial transporter transform by the same group element, so its trace and Hessian are covariant. This proves covariance under that subgroup; it does not classify every accidental stabilizer of a particular datum.

**2.2:** no failing step in the locality warning: retaining a genuinely global `R`, `lambda_A` or `H^T J` as a coefficient does not produce local summands by merely restricting the other factors. This is a failure of the specified parametrix route, not a theorem excluding every possible regrouping.

**2.3:** no failing step in the power count, conditional on the proposed expansion. One vertex with a one-step branch has three cell edges but only one `M_1^{-1}` factor. More generally, with `v` vertices and branch lengths `m_i>=1`, `p=n-v+sum m_i`, `|omega|=n+sum(m_i+1)`, and `3p-|omega|=2(n-v)+2 sum(m_i-1)>=0`. Thus the available estimate is `M_1^{-|omega|/3}`. As the note correctly says, absence of a stronger estimate is not a lower bound or a counterexample to a different expansion.

**2.4:** its displayed inequality points the wrong way. To deduce decay from a per-term bound `q^n`, where `q=C/M_1` and distances can be `n M_1`, one needs `q^n<=C' exp(-delta n M_1)`, hence `delta<=log(1/q)/M_1`. A bound only on the sum does not even imply a bound on each signed term. With those corrections, the warning against deriving an `M_1`-independent rate from norm smallness alone is correct.

**2.5–2.6:** no failing step in the route warnings. Arbitrary gauge-dependent periodization does not ensure single-term covariance. The artificial Dirichlet boundary of a cut-down is its outer bare boundary; coarse internal interfaces are not new Dirichlet faces. Lemma C must still prove admissibility.

**2.7:** no failing step in the distinction between the scalar graph norm and full second-difference regularity, or in the warning about merely Lipschitz multipliers on that graph norm. This warning must also be respected in §5; replacing a whole-system conjugation by a block formula does not justify using the same invalid multiplier estimate in an auxiliary lemma.

**2.8:** CORRECT-NO-ADVANCE as a conditional observation: genuinely canonical, covering-compatible local terms need no subsequent averaging to manufacture those properties. The construction must establish the properties; in particular, coordinate reflections of oriented bond cutoffs need a separate check (§8).

## 3. Cut-down geometry, Lemma C — WRONG at (C5); (C1)–(C4) advance

**First failing step:** (C5) includes `theta_kappa` among the objects determined by the region traces on `kappa^(4)`. Its denominator includes cutoffs of larger neighbouring cubes that need not meet that set.

A hand counterexample uses two adjacent scales `s=M_1 xi_j` and `Ls`. Take `Omega_j` to be the whole, sufficiently large torus, with earlier nonempty members also the torus. In the first sequence put the next region on the positive side of an aligned face `x_1=0`; in the second omit that region there. Take a level-j cube kappa with first-coordinate interval `[-7s,-6s]`. Its fourth enlargement ends at `-2s`; both sequences have precisely the same traces there. A next-level cube lambda with interval `[0,Ls]` has

`phi_lambda(c_kappa) = p(-1/2-6.5/L) * (tangential factors)`.

Choose tangential coordinates where those factors are positive. Since p is continuous and equals one at `-1/2`, this is positive for sufficiently large odd L. This coarse cutoff contributes to the first denominator. The level-j cubes replacing lambda in the second sequence have no cutoff reaching `c_kappa`; hence the denominator and `theta_kappa` differ. Both sequences can satisfy every separation inequality; the flat pair with zero current suffices. This is a failure of the asserted geometric dependence, not of inverse existence.

**What passes, line by line.** The original M_1 grids refine at adjacent levels; the smaller M' grids divide them. The complement identity for the intersection proves separation: the old boundary is farther than `rho xi_i`, and the new box boundary farther than `(rho'+M')xi_i`. The rounding loss is at most one M' cell per face and step; summing the geometric series gives the printed `2L(rho'+4M')xi_kappa` upper bound. Thus the boxes fit within `kappa^(4)` with the stated room. Nesting gives exact region agreement on `kappa^(7/2)`; the finite carrier radius then gives agreement of all local matrix entries used near the cutoffs. No global inverse is being identified there.

Lowering a retained index increases the metric density; extend the cut-down density by the bare one outside its domain. Every path therefore has at least its original length, so taking infima proves (C3), including possible exterior shortcuts. For (C4), all pointwise bounds weaken when `xi_{i'}>=xi_i`. The derivative bound weakens by the square of that ratio. An artificial low-index gauge cube still lies in the original two-layer union; its side is at most `c_g M' xi_i<=c_g M_1 xi_{i_0}`. The original gauge on it is stronger than the new low-index bound. At the upper index the cube lies in the original upper layer. No gauges chosen for different cubes are required to coincide. These checks use exactly the regular-pair premise, including its original gauge-cube range.

The cutoff supports, derivative bounds and overlap estimates (c1)–(c4) survive: contributing scales differ only by a bounded adjacent-level factor, which their constants are allowed to absorb. The normalization denominator is at least one. The artificial outer Dirichlet face is in the new bare collar. Balaban p. 408 likewise fixes smaller separation scales before the large walk scale and rebuilds local operators on cut-down sequences; his displayed domains are not literally the intersections used here. The direct checks above, not his citation, justify this variant.

**Visible repair to (C5), not a proved replacement here:** enlarge the *geometric* read set to include the region-membership tests determining every cube whose `phi` contributes on `supp phi_kappa`. The coarse-neighbour reach is `O_L(M_1)` in the relevant local units, so an enlarged hull is plausible and compatible with D4. To complete this repair one must prove trace-local determination also for a candidate cube absent in one sequence, and keep the enlarged carrier within `C_L M_1` in the original metric near lower-layer boundaries. Merely taking the union of the presently contributing cubes does not check absent candidates. Alternatively construct a partition whose prescribed read neighbourhood already has that property. Neither repair is in the note. The local matrices themselves, as opposed to the normalization denominator, do depend only on `kappa^(4)`.

## 4. Eight-unknown system, Lemma U — ADVANCE as finite-dimensional algebra

**First failing step: none.** Re-elimination against SA 10142–10206 gives the stated result, including the transpose conventions and both Schur signs. Write `u=Pi X^{-1}g'`. The three scalar equations give, in order,

`h=G'(s_lambda+Q'^T mu)`, `lambda=G'(s_h-h)`,

`(Q'G'^2Q'^T)mu=Q'G's_h+s_mu-Q'G'^2s_lambda`.

Consequently `Pi X^{-1}(s,0,0)=G'Rs`. The mixed term `<D^T A,A_s lambda>` in q has half its coefficient in each polarized off-diagonal block. Substituting `lambda=L A` adds the two halves and produces `D R D^T`, with no missing factor two. The three terms of `c_J(A,L A)` are exactly SA's bilinear current continuation with its two arguments equal; this does not use the physical-current identity. Finally `A-D L A=S A`, giving the claimed `-S^T Delta^(2)[j]S`.

Eliminating Y and Z in the full system gives

`T A+Q^T nu=f+B^T X^{-1}g-(q_A lambda+L^T q_lambda lambda)u`, `Q A=f_nu`.

Thus `nu=W^{-1}(Q T^{-1} f_tilde-f_nu)` and the multiplier-multiplier inverse block is **minus** `W^{-1}`. The A-multiplier block is **plus** `T^{-1}Q^T W^{-1}`; the AA block is `T^{-1}-T^{-1}Q^T W^{-1}Q T^{-1}`. All transposes are bilinear physical transposes, also at complex pairs. Existence is conditional on precisely the stated invertibilities from (I1), for an arbitrary scale-bounded coefficient j; no on-shell substitution is made.

## 5. Localization and Lemma L — WRONG as written; the graph-norm step has a direct repair

**First failing step:** Lemma D's product-rule argument for *any* of §4's spaces. For the Lambda graph norm a first-difference bound on the weight is insufficient, exactly as test 2.7 warns. In a flat scale-one patch, take lambda smooth and equal to one near `x_1=0`, and `theta=tau |x_1|` there. Across that plane `Delta_eta exp(theta)` is of order `tau/eta`. Its squared L2 contribution in a fixed tangential patch is of order `tau^2/eta`, whereas the graph norm of lambda stays bounded. Thus the asserted uniform multiplier bound on Lambda is false. This attacks the proof's auxiliary assertion, not the existence of scalar Green-function decay.

**Written repair sufficient for the graph-norm use.** Restrict Lemma D to weighted L2 and first-order energy spaces. Choose the pillar cutoffs used in (5.0) with *two* bounded differences: `|D chi|<=C_L/m`, `|D^2 chi|<=C_L/m^2`. Such cutoffs come from smooth profiles on enlarged pillar boxes and normalization by their bounded-overlap sum; neighbouring scales differ by a bounded L factor. Multiplication then preserves Lambda, since

`A_s(chi lambda)=chi A_s lambda+[A_s,chi]lambda`,

`||[A_s,chi]lambda|| <= C_L (||m^{-1}D lambda||+||m^{-2}lambda||)`

locally. The averaging mass contributes the oscillation over its finite carrier. Zero boundary values remain zero; no corner regularity theorem is needed. These local product estimates, bounded overlap and duality prove both inequalities (5.0), and supply the localized dual pairings in Lemmas P and S.

For `G':L2 -> Lambda`, apply (I1)(i) only to the weighted zeroth and first derivatives. The remaining graph component is **exactly** `A_s G'g=g`, supported where g is. Thus the local graph estimate follows without multiplying a graph-norm field by a nonsmooth exponential. For the transpose `G':Lambda* -> L2`, test against an L2 vector g supported near y and put a smooth cutoff zeta equal to one near the support z of F:

`|<g,G'F>|=|<F,zeta G'g>|<=||F||_(Lambda*) ||zeta G'g||_Lambda`

`<=C_L exp(-tau_0 d(y,z)) ||F||_(Lambda*) ||g||_2`.

The middle inequality uses the just-proved smooth-cutoff bound. This fills the missing localized-duality justification; it does not assume that arbitrary Lipschitz exponentials act boundedly on Lambda.

With those changes, Lemma P's convolution uses the triangle inequality and spends half the rate, and Lemma S is the ordinary weighted Cauchy/Schur calculation. The annular bound converges because the growth exponent `8 log L/rho'` is at most half the smallest exponent being summed. The stated `tau_L rho'>=256 log L` gives the required room.

**Commutators.** Identity/multiplication terms cost only the base-point shift. A first-order difference commutator has one cutoff difference. For the apparently third-order block `D A_s`, the two terms are `[D,h]A_s lambda` and `D[A_s,h]lambda`: pairing the latter with A moves D onto the test field, using its energy norm; the former uses `A_s lambda` already in Lambda. This verifies the displayed estimate without full second derivatives of lambda. Curvature remainders have mass-form size. The current is only multiplied or shifted, so no derivative bound on J is used.

**Premise qualification.** The absolute row/column coefficient estimate for `Delta^(2)[j]` is used here and in (7.2), explicitly citing `a2-curved.md` (8.3)/(8.10). It controls the local form on `A-D lambda`, since `||m^{-1}(A-D lambda)||<=C||Psi||_X`. The displayed inverse bounds (I1)(i)–(iv) alone do not assert this coefficient estimate. It is a named ingredient of the cited full §7.4 package; it must remain included when (I1) is imported. If (I1) is interpreted as *only* its four displayed inverse/conjugation inequalities, the localized coefficient bound is an additional, unproved premise here. (I3), which concerns level-k local maps, does not replace the all-scale second-jet bound. No input proof is redone or promoted by this gate.

**Lemma L under that explicit reading and the written repair: ADVANCE.** Normalize the raw site Gram inverse as `N_raw=Xi^{-2} N_normalized^{-1} Xi^{-2}`; its source norm is `||m^{-2}s_mu||`, its target norm `||m^2 mu||`. This checks the scale factors rather than treating raw N as an unweighted bounded matrix. All other local factors in (4.1)–(4.2) have the displayed energy/graph source and target types. The successive maxima of inverse factors are 5 in `X^{-1}`, 10 in `f_tilde`, 13 in A or nu, 18 in Y and 23 in Z. Twenty-five rate halvings are therefore conservative. The local graph part is already supplied above, not an extra inverse. Holomorphy is finite-matrix inversion on the admitted domain; reality follows from the real coefficient convention. Constants depend on the fixed smaller cube/gap thresholds and L only. They do not depend on M_1, box size, depth, volume or region shape. This is conditional on (I1) being uniform on every cut-down, as expressly stipulated.

## 6. Theorem W — WRONG in its locality conclusion; the parametrix and chained estimate advance conditionally

**First failing step in the theorem:** (c)'s specified hull and (d)'s dependence argument invoke the false cutoff part of (C5). Their region-trace and canonical conclusions are not proved for `union kappa_i^(4)`. Repair requires the enlarged geometric read set discussed in §3. For fixed regions, the cutoffs are fixed scalar numbers: this failure does not introduce additional field reads or spoil holomorphy in the fields. The norm argument below is independent of that defect.

**Identity and support: no failing step after §5's norm repair.** The local and global K entries agree throughout a full stencil neighbourhood of `supp h_tilde`; source and output cutoffs stay away from the artificial boundary. Hence `K B=1-R` with the printed **minus** sign in `R_kappa=-[K,h_tilde_kappa]S_kappa theta_kappa`. A nonzero product only requires an intersection of supports (the proof's phrase “the set ... lies within” should mean “meets”); the r_0 margins put the intermediate pillar inside both enlarged cells. The output is in the root cell and the input is read on the final theta support.

**Chaining redone.** Each local inverse pays `exp(-tau_L d(x,z))`, because `d_B^kappa>=d_B`, while each commutator pays `C_L/M_1`. For fixed intermediate pillars the sum of leg lengths is at least the path distance visiting the required cells. Reserve half its exponent for that distance. Sum the other half successively over the last, next-to-last, and earlier pillars, dropping the final leg before summing; every sum is bounded by `K_(tau_L/2)`. Thus (6.2) follows with `C_W=C_1 K_(tau_L/2)`. No factor of `exp(+c M_1)` is introduced. This is why the rate is independent of M_1; norm smallness alone would not suffice.

For `R`, at a fixed output pillar only boundedly many cutoffs can have nonzero commutator. Schur summation therefore gives `||R||<=C_L/M_1`; choosing M_W makes it at most one half. The geometric walk count then proves convergence. There is a minor distinction in the last sentence of (a)'s proof: a volume-independent **Schur majorant** for all roots is not a bound on the sum of their separate operator norms. At fixed finite volume the latter has an extra finite factor equal to the number of roots, still giving absolute operator-norm convergence. The volume-free kernel/Schur estimate needed by the consumer survives.

Translations and gauge covariance of the algebraic construction survive when the translated data include *all* cutoff read sets. Gauge transformations act at the same base points as the scalar cutoffs and hence commute with them, using (I2) only for that covariance assertion. Reality is preserved. Coordinate reversal is a separate matter (§8).

## 7. Lemma J, Theorem T and the transposed multiplier — WRONG literally; the tree estimates have a written repair

**Lemma J: ADVANCE conditional on the repaired norm statement of W; first failing step: none in its normalization or exponent.** The dual of `sum xi_c^6 |nu_c|^2` under the physical row pairing has norm squared `sum xi_c^2 |f_c|^2`, so `||e_c||=xi_c`. The transpose contributes `xi_c^{-4}`. Consequently the weight in `xi_c^3 |j_beta(c)|` is exactly `xi_c^3 xi_c^{-4} xi_c=1`. On one pillar the squared mass-dual current bound is `eta^4 (xi/eta)^4 xi^2 gamma_0^2 xi^{-6}=gamma_0^2`, up to fixed incidence factors. For an enlarged cutoff neighbourhood the printed `2 gamma_0` should be `C_L gamma_0`; no M_1 or depth factor occurs. Splitting the path decay between its distance to c and its obligation to visit the cells leaves a summable endpoint exponential and proves (7.1). Reversing walks from their last cell proves absolute summability at each c. The row support is the last theta support, not the original root.

For `j^(0)`, at most a fixed number of theta supports meet c. Thus `sup xi^3 |j^(0)|<=C_0 gamma_0`, and the stipulated arbitrary-coefficient version of (I1) applies once that is below gamma_j. No equation of motion is used. The vertex form is local in its *argument*, while its coefficient carries a branch; these are different assertions. Its estimate (7.2) uses precisely the absolute second-jet input identified in §5, on the adjacent-scale row carriers.

**Theorem T's first new failing line:** in (b), after retaining `(C_W/M_1)^{m_i}` at each branch, the next display replaces all coefficient powers by `C_3^n`. For fixed n and unbounded `m_i`, that drops `C_W^{sum m_i}`. **Written repair:** retain `C_*^{n+sum m_i}` (with `C_*>=1`), then bound it by `C_*^{|omega|}`. This is absorbed by C_T in the claimed conclusion. It does not cost another M_1 power.

The remainder identity in (a) has the correct sign: `K_1 B^(0)=1-R^(0)+sum V_beta B^(0)`. Its vertex part is bounded by `C gamma_0 sum_(m>=1)(C/M_1)^m`; fixed source and target pillars leave only boundedly many terminal branch and local-model choices, followed by at most geometrically many backward continuations. This is `O_L(gamma_0/M_1)`, making the norm at most three quarters after the stated choices.

For (b), each nonzero vertex meets both its trunk cell and its terminal branch cell within the fixed stencil margin. Join the trunk legs and the near-minimizing branch paths at these points. Their union is connected; deleting cycles only reduces its length, and it meets every required cell. Spend `tau_L/4` of every trunk length and the entire branch exponent on this tree. The remaining `3tau_L/4` of the trunk lengths pays the successive intermediate-pillar sums. The fixed joining offsets cost `C^{|omega|}`, already allowed. Finally the exact identity `3p-|omega|=2(n-v)+2 sum(m_i-1)` proves the one-third power. This checks both the tree geometry and the rate; there is no hidden `M_1` in the exponent.

For (c), reverse branch continuations and a composition of the total cell count give an exponential number of decorated trees, as stated. For (d), field dependence and gauge covariance are preserved factorwise, but the geometric read set must still be repaired as in §3. That inherited locality failure is not repaired by the correct tree count.

**Corollary T: ADVANCE for the estimates, conditional on the preceding repairs.** The Schur blocks give H_1 and minus the row precision. Repeating the physical-pairing calculation gives (7.4) with exponent `tau_L/8`. The integration point belongs to the old root cell, so the tree in this *one-endpoint* bound meets that cell as well; it legitimately meets **all** cells. This is exactly what permits re-rooting the E term at its supported row later. No unexplained factor of xi, missing root, or stationarity premise remains in this step.

## 8. Theorem H — WRONG as a whole; (H2)'s support and decay survive conditionally

**Lemma 8.1: ADVANCE; first failing step: none.** Dropping the last region replaces scale L by scale one, weakening all pointwise bounds, including the derivative bound by L squared. The short sequence's top gauge cubes are already among the longer sequence's level-k gauge cubes. No extra admissibility of the current is assumed.

The three operator terms reconstruct A by the algebra of §4. On the active mask all nonzero partition terms are level k: separation puts it farther than the cutoff reach from lower layers. The row precision's minus sign is required. For the E term, re-root at the last trunk cell; its row support and the all-cells estimate of Corollary T justify this, independently of which cell was initially listed first.

**First literal failing clause of H:** (H1)'s count `C_h^m` at m=0 allows only one index, although there are three types, with multiplicity. Write `C_0 C_1^m` or `C_h^{m+1}`. Re-rooted E terms still have an exponential count: count the trunk backwards from its last cell and attach the same branches. There is no superexponential proliferation. This harmless count repair is separate from the material failure of (H3): it inherits (C5)'s false geometric locality and hence does not establish equality of the functions when only those region traces agree. Field holomorphy for fixed regions is a distinct, surviving assertion.

**D4 support check: the necessary clauses are present in the statement.** Read (H2) explicitly as `A_omega(b,b')=0` when `dist_B(b,X_root)>C_L`. The G term has that property from its left cutoff followed by C_V; the E term from its supported coefficient followed by the fixed E and C stencils; the local term from theta. Bounded overlap gives a bounded number of possible roots at b. The missing root in the definition of tree distance therefore causes no loss beyond the root cell's diameter. (H3) also expressly asks that the actual hull lie within `C_L M_1` local units of the cells. Together these are the kind of support/carrier clauses D4 requires. **Qualification:** this full H3 claim fails for the cutoff geometric dependencies identified in §3. The narrower *field carrier* required in the fixed-region decoupling argument can nevertheless be bounded directly, as follows.

For each actual local inverse, its field reads lie in `kappa^(4)`, whose original-metric diameter is `O_L(M_1)` by the two-layer geometry. A zero-length multiplier contributing at c reads a box `lambda^(4)` with `c in supp theta_lambda`, hence c is inside that same box. When it supplies `j^(0)` to the local model at kappa, c lies in `kappa^(7/2)`; this is within `O_L(M_1)` of its walk cell. Joining through c bounds the entire additional field read set by `O_L(M_1)` from that cell. The branches have the same property. Finally the C and E stencils add only `O_L(1)`. Take the union of these *actual* field read boxes and stencils as the carrier hull, with a fixed enlargement for the stencils. This proves its radius bound for each fixed region sequence and its local-class field holomorphy by (C4). It does **not** assert that the list of contributing boxes is determined by the traces on that hull; that is the failed canonicity issue. Fixed-region decoupling does not require the latter assertion.

For the quantitative kernel estimate, active row scales equal one. A unit row source has norm one and evaluation of the row* output costs one. Thus (7.3) directly bounds the G kernel. In the E term its coefficient row is within a fixed stencil distance of both arguments; adding these short legs to the all-cells tree proves its estimate. The local term has bounded range. Therefore, with the norm repairs and coefficient premise retained, the exponent `delta_h=tau_L/8` and the `M_1^{-m/3}` bound are valid. Replacing the depth-k metric by the longer-sequence metric only weakens them. Compression by any Y preserves the bounds and supports, so (H4)'s algebraic compression has no new failure.

**A separate failure in (H3): even product profiles do not establish reflection covariance of oriented-bond cutoffs.** For a positively stored bond `b=(x,x+eta e_1)` reflected by r, the positively stored image bond starts at `rx-eta e_1`. Conjugating multiplication by f through the reflection evaluates f at the image of the *old* base point, rx; the prescribed new multiplier evaluates it at `rx-eta e_1`. They differ wherever f varies. The gauge twist on the reversed bond does not remove this scalar difference. Rows have the same issue with their row length. Thus the proof's claim that every listed isometry carries these cutoffs to themselves is false. Gauge covariance, which keeps base points fixed, is unaffected.

**Visible symmetry repair, not completed here:** use orientation-invariant bond/row locations for the cutoffs and extend the partition to the needed fixed boundary neighbourhood, then recheck the support identities; or average the terms over the finite coordinate-isometry group, provided covariance of the total operator and compatibility of the admitted domain have separately been supplied. The latter total-operator property is not a consequence merely of (I3)'s finite analyticity. The consumer in §9 needs no single-term reflection covariance, so it can instead explicitly omit that clause. Likewise replace “A itself is covariant exactly under” by “the construction is covariant under” the block-constant subgroup; test 2.1 refutes the full group, not every possible larger datum-dependent stabilizer.

The by-product about other inverse blocks is valid at the same conditional energy-norm level: removing the multiplier row leaves inverse block T^{-1}, and the h response to an h source in X^{-1} is `1-R`. It supplies none of the unclaimed pointwise derivative or Hölder upgrades. The order of constants for the norm theorem is noncircular; a repaired geometric/symmetry construction would have to add its fixed L-dependent constants before choosing M_1.

## 9. Consumer against D4's collared repair — WRONG as written; the corrected implication ADVANCES

**First failing step:** item 2 omits the cell-size room needed for the parameter partition, and item 3 asserts `d_B(omega;b,b')>=w-C` with C independent of M_1. The valid subtraction is `R_h=C_L M_1`. The concluding “verbatim” claim also imports Theorem VI's erroneous exemption of the first sixteen parameter cubes. Merely changing the one-half power to one-sixth cannot repair these steps.

**Written replacement.** Work on a fixed region sequence with the corrected kernel/count estimates and the actual field-carrier construction of §8; no single-term reflection covariance or comparison between different region sequences is required. Include every varied cube meeting that carrier:

`s^omega = product_(Delta in P(omega) intersect S) s_Delta`.

Unvaried parameters equal one. There is no exemption for the first sixteen cubes and no exemption for a zero-length term. At fixed left argument, bounded overlap leaves only `C_L` roots. If the monomial is nonconstant, a carrier point meets a parameter cube outside the collar. Any admitted tree is within `R_h` of that point: use the cell's meeting point for a nonroot cell, and the supported left endpoint for the root. Therefore its length t obeys `t>=w-R_h`, as well as `t>=d_B(b,b')`.

Choose `ell_P>=8 C_geom R_h`, where C_geom accounts for the fixed top-unit conversion. Traverse a finite admitted tree twice and divide the traversal into pieces of length at most `ell_P/(4 C_geom)`. Each piece, thickened by R_h, has coordinate diameter less than ell_P and meets at most sixteen partition cubes. Counting pieces gives

`#P(omega)<=16+C_L t/ell_P`.

Approximate an infimizing tree to obtain the same bound with `t=d_B(omega;b,b')`. This proof also covers t=0: the leftover sixteen-cube factor is precisely why the monomial must not be artificially exempted. At depth k all local scales are at most one, so weighted lengths dominate physical lengths in the active top units.

Let `delta=delta_h`. Also choose `ell_P>=2 C_L kappa_bar/delta`. Then

`|s^omega| exp(-delta t/2)<=exp(16 kappa_bar)`.

For an s-dependent term, `|s^omega-1|<=|s^omega|+1` costs at most a factor two. Split the remaining exponent into quarters to obtain

`|(s^omega-1)A_omega(b,b')|`

`<=2 C_h exp(16 kappa_bar) exp[-delta(w-R_h)/4]`

`   * (C_h M_1^{-1/3})^m exp[-delta d_B(b,b')/4]`.

Keep the proposed reserve consistently: split `M_1^{-m/3}=M_1^{-m/6} M_1^{-m/6}`. The first factor pays the exponential index count when `C_h^2 M_1^{-1/6}<=1/2` after adjusting fixed prefactors; the second absorbs `m+1` when `M_1>=e^6`, since `(m+1)e^{-m}<=1`. Thus one sufficient floor is `M_1>=max(e^6,(2C_h^2)^6)`. Alternatively sum `(m+1)r^m` directly. The note's smaller floor based on using the entire one-third power cannot simultaneously claim that the unused one-sixth reserve has already paid for the same sum.

Sum over the boundedly many roots, tree lengths and the unit-scale endpoint bonds. The last endpoint exponential has a uniform Schur sum. Consequently

`||chi(A(s)-A)chi|| <= C exp(16 kappa_bar) exp[-delta(w-R_h)/4]`.

In particular this is at most `c_L/20` if

`w>=2R_h`,

`w >= (8/delta) [16 kappa_bar + log(20C/c_L)]`.

This is D4's repaired estimate with the available one-third walk power. It is a hand implication from the repaired norm construction and the explicitly retained input package, not an application of the unrepaired Theorem VI. M_1 is fixed before ell_P and w; no earlier field ceiling depends on it. The rate delta depends only on L.

The resulting Hermitian-part loss is at most `c_L/20` after any compression. Thus an already established assembled precision with gap `c_L/2+c_L/20` retains `c_L/2`; the decoupling argument does not supply its starting gap or the other a2-full repairs. A local gauge-gradient correction may be left undecoupled by definition, or its finite carrier must be excluded by the collar. At `s=1` the expansion recovers A. Normal convergence on the closed parameter polydisc gives holomorphy in its interior, and with strict margin in the choices above on a neighbourhood of that polydisc. It also preserves field holomorphy on the admitted local classes. None of this constructs the separate inverse-root series r(s).

## 10. Disposition — WRONG as the note's full claim; a narrower consumer implication advances

**First failing step:** declaring the entire corrected statement 5 proved from the note's unmodified construction and saying Theorem VI reads it verbatim. The full theorem still has an incorrect region-trace locality claim and an unproved reflection-covariance clause. The normalization, graph-norm and consumer repairs above must not be silently attributed to Claude's original text.

| Section | Verdict on the written section | First failure / surviving result |
|---|---|---|
| 0 | WRONG | Full implication is not proved; the consumer also does not read it verbatim. |
| 1 | WRONG | Consumer premise omits support/carrier requirements. |
| 2 | WRONG | Mixed-term sign in 2.1; covariance restriction and one-third count survive. |
| 3 | WRONG | C5's cutoff denominator reads unseen coarse cubes; C1–C4 advance. |
| 4 | ADVANCE | None: all eight-variable Schur identities check. |
| 5 | WRONG | Graph-norm use of the Lipschitz multiplier argument; repaired local inverse decay advances under the stated package qualification. |
| 6 | WRONG | Region-locality claim inherits C5; parametrix, support and chained rate advance conditionally. |
| 7 | WRONG | Dropped branch constants; repaired multiplier/tree estimates advance, while geometric locality remains defective. |
| 8 | WRONG | Length-zero count needs a prefactor; H3 also fails. Kernel decay, left support and fixed-region field-carrier bounds advance conditionally. |
| 9 | WRONG | Wrong collar subtraction and inherited monomial; the written collared replacement advances. |
| 10 | WRONG | Full closure and “verbatim” disposition overstate what was established. |

Defects ranked by what they break (seven groups):

1. **Region-trace locality:** C5 is false for the supplied normalized cutoffs. This breaks W(c)–(d), T(d), and H3's canonical comparison of different region sequences. An enlarged geometric read set or a different partition is a visible but unfinished repair. It does not invalidate fixed-region field holomorphy or the field-carrier argument used in §9.
2. **Consumer geometry and monomial:** §9 uses the unrepaired VI. The complete replacement above includes every varied carrier cube, `ell_P` room of order M_1, and `w-R_h`.
3. **Graph-norm localization:** the proof of D applies an invalid multiplier estimate. The restricted lemma plus smooth-cutoff/transpose repair above supplies the uses needed for L without computer assistance or corner regularity.
4. **Single-term coordinate symmetry:** base-point cutoffs are not carried by orientation reversal as asserted. The visible repairs need their own boundary/domain check; the fixed-region decoupling bound does not read this clause.
5. **Premise scope:** preserve the all-scale absolute second-jet coefficient bound actually read from (I1)'s cited §7.4 package. Four inverse norm statements alone, and (I3)'s one-step maps, are not that input. (I2) is used only for gauge covariance. No input is independently discharged here.
6. **Tree and count bookkeeping:** retain `C_W^{sum m_i}`, allow a fixed multiplicity at length zero, and distinguish a Schur majorant from a sum of separate root operator norms. These have written repairs without loss of the one-third exponent or the M_1-independent decay rate.
7. **Test wording:** repair the sign in 2.1 and the inequality/deduction in 2.4; do not interpret 2.3 as a lower-bound counterexample or the subgroup test as a classification of all stabilizers.

**Current checkpoint — complete.** All of Claude's §§0–10 have been read and checked in bounded ranges at the pinned revision. The algebra, the repaired local inverse/parametrix/tree estimates, and the corrected fixed-region collared implication are the useful advances. The full canonical and single-term-isometry version of Theorem H is not established. The remaining concrete work is the geometric-read-set repair and the orientation-covariant cutoff construction (or an explicit narrowing of those clauses), with the coefficient-premise wording kept exact. No claim about independent verification of (I1)–(I3), full A2, the inverse-root expansion, or Yang–Mills closure follows. This report grants no status and changes no queue row.

Source verification: HEAD remained `44dbf84faf41a67a7ec0081cdc9adb241c1209c6`. Reviewed source blobs: `h-walk.md` = `c4477d14685f67c1786b5ed0ff326a4de738caaf`; `a2-full-gate.md` = `e78297a2e5e4ff02fc0aee4a1ba76e970b3ddf24`. Both and FINISH.md remained unchanged against HEAD. The downloaded outline SHA-256 is `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. These are source-identity checks only, not mathematical evidence. Repository status showed only this new report.
