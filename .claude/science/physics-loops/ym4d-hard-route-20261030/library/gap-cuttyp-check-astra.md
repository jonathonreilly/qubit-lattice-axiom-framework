# Repo search

Codex / gpt-6-astra / xhigh; check of row 936 at `134d5fb6fedc7aaa13c2e7a03105678a166bfe4a`, 2026-11-14. Research text, not an audit; grants no status.

Searched `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141` in `/Users/jonreilly/Projects/Physics`, using bounded `git grep -n -i -E` over Markdown and TeX. Initial terms: `CUT.TYP|gap-cuttyp|conditional cut gap|frozen Q_8|binary tetrahedral`. No CUT-TYP statement appeared. The binary-tetrahedral hits concern finite spinor representations (`docs/BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28.md:35,242`), a corner-fermion model, and `briefs_hrp/AUTHOR_BRIEF_HRP.md:63`, which proposes Q8 or 2T as a test group. None states a conditional-cut Poincare estimate. Broader method searches and primary-source comparisons are recorded below as completed.

The requested `library/prior/gap-cuttyp-check-astra.md` is absent. The registry search for `gap-cuttyp|CUT.TYP|oddgap|odd Poincar|LSI.weak|EVEN.PI|LOC.CAP` returned no rows. This check owns only row 937, not a new attack on row 936's open inequalities. The November 8 repo-search digest is a locator for older work, not evidence for this target.

## Scope and working checkpoint

Completed source matching:

Ref identities at the search checkpoint, in the order above: `4d88da5504d356762deb6b1a1c2695336af9fb81`, `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `89faef229ff6e6bde42baad15ed8270c2f4087d8`, `1e70c7211a2cdbc39001e619f1dd89db45e25851`, `c73ad7b177d94f89ff37b77386936e3d52b48b05`.

- A narrower five-ref query `odd Poincar|CUT.TYP|conditional cut gap|quenched.{0,30}(chiral|O\(4\))|RARE-P([^a-z]|$)|CUT-3D|LOC-CAP|Proposition ORBIT` returned only the unrelated archived `126_BRIDGE_GAP_NEW_PHYSICS_OPENING_NOTE_2026-05-06.md:316` (a proposed determinant/quenched-coupling modification). No same-target result was located. A broader query was capped and is not used as absence evidence.
- The method query `Bauerschmidt|Bodineau|replica overlap|Nishimori|conditional.{0,25}Poincar` located `origin/main:.claude/science/physics-loops/su2-gauge-aligned-response-20261108/sources/connected-response-literature-scan-20261109.md:146–162`. Its Menz entry requires uniform conditional site gaps and a positive comparison matrix for a covariance bound. Its Bach–Møller entry requires weak pair coupling around scalar onsite wells. Neither supplies the quenched compact-spin gap here.
- `origin/main:research/mass-gap/library/prior/gap-fullread-2.md:47–66` states the Bauerschmidt–Bodineau–Dagallier integrated-Hessian criterion: a lower bound on the renormalized Hessian at every scale, plus an integrable exponential of that bound, yields an LSI. It explicitly leaves the Wilson application unmatched. This is related prior method work, not a CUT-TYP proof or another owner of this check.
- SA-index README and `chunk-02.md:99–109,169–174` locate GL8/GL10; neighbouring rows identify their hypotheses. The targeted obligations/index search found no CUT-TYP/odd-cut statement. The cited outline lines 2313–2394 were read: GL8 is `Z_s(0)=Tr L^s`; GL10 is the trace bound by `Tr L^s` for contraction insertions. These supply the credited transfer frame, not a conditional odd gap. The wall-potential representative used here is fixed explicitly in `gap-fr-opus.md:29–36`, rather than silently identifying its kernel with SA's half-convolution representative.
- A bounded CA-I/II/III search for `odd Poincar|CUT.TYP|quenched|Nishimori|transfer contraction|gauge.averaged transfer` found only CA-II's healed-island use of “quenched” (104864,104950). No account theorem is imported from those unrelated hits. This is a targeted search, not a claim to have reread the account. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

The older November 8 digest concerns UV/history suppliers and contains no checked cut-gap result. The new work below checks row 936's own statements; it does not repeat those earlier proofs.

Source: `library/gap-cuttyp-max.md`, 550 lines, SHA-256 `9805c5fe4c9a69c7507707d3fbefe7977ff58c875bebf5937fb6fb26957e4c72`. Its bytes were checked against the pinned commit after the mathematical check. Verdict vocabulary: HOLDS, HOLDS AFTER CORRECTION, FAILS. A failed inference is distinguished from a counterexample to its desired conclusion. No numerical run can discharge a statement.

Plan: (1) finish prior/source matching; (2) check M and W; (3) check CAP, RARE-P, LOC and ORBIT; (4) check Q and CUT-3D; (5) check U(1), frozen groups and GUIDE arithmetic; (6) write the verdict table and one RESULT line.

Final checkpoint: all source statements covered below. Five substantive defect groups are recorded. Missing GUIDE source/log verification is explicit; no further experiment was substituted. The report is the only changed file. No source, registry, FINISH row or audit file edited. The next scientific decision belongs to the lead: retain the valid conditional inequalities, correct the failed overlap/Gaussian interpretations, and keep the actual cut-gap inputs open.

## Checked implications

**CAP, lines 253–266: HOLDS.** Write `m=E F^2`, `D=E|grad F|^2`. CUT bounds the good-set contribution by `D/g_0`. Apply CAP to `|F|`; its weak gradient has norm at most that of F. Thus `(1-delta')m <= D(1/g_0+1/kappa)`. This requires `g_0,kappa>0`, as used in the proof. The entropy specialization is the existing row-930 RARE argument: `E[h^2 1_Bad] <= [2D/alpha+(log 2)E h^2]/log(1/delta)`. Credit row 930 and its row-933 check; this is not a new entropy lemma.

**RARE-P, lines 268–282: HOLDS.** Weighted Cauchy gives `h^2 <= (1+1/eta)(h-Eh)^2+(1+eta)(Eh)^2`. Integrate on Bad and use the even Poincare inequality on h. This yields the printed constants and, at `eta=1`, `(1-2delta)/(1/g_0+2/lambda_e)`. The sentence at line 284 calling this a *cap on lambda_s* needs correction: it caps this lower bound, not the actual odd gap. The Markov step at lines 315–318 also holds: `E[#bad]<=delta L_1` gives probability at most `1/3` for more than `3delta L_1` bad cuts. The resulting RARE-P bound in section 6.1 is correct. LOC still needs its separate local-capacity premise.

**LOC, lines 294–310: HOLDS.** For each k, conditional odd Poincare gives `D_k >= gamma_*[(1-delta_1)m-D_N(k)/kappa_1]`. Sum: the disjoint cut energies sum to at most D and `sum_k D_N(k)<=n_0 D`. Solving gives exactly the stated bound. The suggested conditional-PI supplier works if that conditional PI applies to the restrictions of h (a full conditional PI suffices) and the conditional bad probability is uniformly bounded. These are additional inputs, not consequences of TYP-1.

**ORBIT, lines 320–330: HOLDS.** `f(phi_pi xi)-f(xi)=-2f(xi)`. The orbit velocity has squared norm N. Cauchy on an interval of length pi and Haar change of variables give `4 E f^2 <= pi^2 N exp(Delta_X) E|grad f|^2`. This proves the displayed lower bound, including its constant. It supplies neither an upper bound nor a uniform bound on `Delta_X`.

**Q1–Q3, lines 344–361: HOLDS.** Let K denote the block covariance matrix called G in Q1, to distinguish it from `sum_k gamma_k`. Independent replicas give `N^2 Q=tr K^2`. K is positive, `tr K=N`. A top-eigenvector linear test has energy at most its coefficient norm squared, so `gamma<=1/||K||<=1/(NQ)`. A one-spin coordinate with variance at least `1/4` gives `gamma<=3`. With `c=c_0(1-delta)`, exchangeability of cuts gives `E min(3,1/(NQ))>=c`. A variable in `[0,3]` with mean at least c exceeds `c/2` on a set of probability at least `c/6`. This is Q3, which requires only a positive fraction of environments with bounded NQ.

## Defect 1: the advertised necessary overlap test does not follow

**Lines 369–371, 428, 450–452 and their result echoes: FAILS.** TYP-1 permits a fixed bad probability delta. Q2 gives only

`E Q_k <= 1/(N gamma_*) + delta`, hence `N E Q_k <= 1/gamma_* + delta N`.

The source prints this last bound and then calls it bounded in N. It is not. Nor does Q3 imply `(OD): E Q_k<=C/N`. Q3 controls a positive fraction of environments, not the average. Thus order-one averaged overlap alone does not refute TYP-1 or the whole CUT route.

The failure is mathematical, not just a missing estimate. Consider an even conditional spin law selected by an environment flag. With probability `1-delta`, use product Haar spins: `gamma=3`, `Q=1/(4N)`. With probability delta, use a smooth even density concentrated near the two configurations `(q,...,q)` and `(-q,...,-q)`. Its Q can be arbitrarily close to 1. For any fixed `gamma_*<3` and `delta<1/3`, TYP-1 holds, while `E Q` stays of order delta. This example diagnoses the proposed implication; it is not a counterexample to SU(2) Wilson CUT-TYP.

A valid necessary test for TYP-1 is the tail statement `P(NQ_k>1/gamma_*)<=delta`. A valid necessary test for CUT-TYP is exactly Q3. An averaged `C/N` statement would need an additional tail or uniform-integrability input.

## Cut-law identities and their scope

**M1, lines 88–91,120–125: HOLDS.** Use the symmetric wall-potential kernel from row 922. Expanding both even projections produces four slab weights, each with coefficient `1/4`. Flipping the v endpoint in just one slab changes exactly its adjacent temporal cut plaquettes; each spatial plaquette contains zero or two flipped links. The two spatial half-weights combine to one full spatial weight. A different transfer representative with the same trace need not have the same two-slice density; the check uses the representative actually specified upstream. Any common action-normalization constant must be used in both W and Z_e.

**M2, lines 93–100,126–130: HOLDS.** The spatial trace is `Re(xi_x h_xy xi_y^* g_xy^*)=<xi_x,g_xy xi_y h_xy^*>`. A temporal trace is `<xi_x,t_x xi_x^+ (t'_x)^*>`. The two independently chosen slab signs therefore yield exactly the product of the two coshes. All remaining plaquette weights belong to the positive xi-independent bulk measure. No independence of the two staple fields is needed or obtained.

**M3, lines 102–106: HOLDS**, with the stated spin convention. `1-s_x.s_y=|s_x-s_y|^2/2`, so the local action has coefficient `beta/2` in front of the squared differences. With continuum action `(2g_sigma^2)^(-1) integral |partial s|^2`, `g_sigma^2=1/beta`: `10/23` and `5/13` at the endpoints. The spin target is SU(2), with left/right SU(2) symmetry; it is not a product target SU(2) x SU(2). This identifies the bare local factor, not an effective coupling after integrating Phi_env.

**M4, lines 108–112,131–137: HOLDS AFTER CORRECTION.** On the simple transverse graph (sides at least 3), invariance of each bilinear bond requires `a_x^-1 g_xy a_y=z_xy g_xy` and `b_x^-1 h_xy b_y=z_xy h_xy` with the same central sign. For generic holonomies the sign cocycle has trivial cycle products, hence is a coboundary. Absorb its vertex signs into **both** a and b. Parallel transport then identifies the symmetry group with the product of the two holonomy centralizers modulo their common centre. Noncommuting SU(2) holonomies have centralizer `{+-1}`. The trace-zero exception is indeed null for the finite-beta Wilson marginal, which has a positive smooth density. The assertion “Flat layers: SO(4)” must account for **winding holonomies**: plaquette-flat torus layers can have noncentral commuting winding holonomies and only U(1) centralizer. Central full holonomy groups in both layers give SO(4); the gauge-trivial case is an example. In a pure-gauge chart the rotations may be uniform; in the original chart they are transported site rotations. This is a symmetry statement about the local factor only.

**M5, lines 114–116: HOLDS.** It is disintegration of the specified joint law. Calling this “planted” or “Nishimori-type” adds no estimate. Conditional replicas are exchangeable with the original cut given the environment; no further correlation inequality is derived here.

**M6, lines 118–119: HOLDS AFTER CORRECTION.** Conditional on the non-cut bulk links, the cut links at all times have nearest-neighbour spatial couplings and temporal couplings. For w_e the temporal bonds also have the sign mixture of M1/CUT-3D. The non-cut bulk links are then integrated with their joint weight. A single ordinary, quenched, untwisted 3D O(4) model does not equal nu_k.

**Section 2.2(1): HOLDS.** The ambient extension of each sign component is a Laplace transform of a positive measure. In fact their positive sum is also a Laplace transform and is log-convex. This ambient log-convexity supplies no spherical Poincare estimate.

## Defect 2: a sign mixture is not by itself a proved slow gap

**Section 2.2(2), lines 145–149; CUT-3D's “r=0 is fatal”: FAILS as a proved conclusion.** The displayed external-field mixture is exact. Concentration near opposite configurations and a tunnelling-small gap require quantitative concentration/barrier estimates; none is given. A symmetric mixture alone proves neither. At beta=0 the same representation has Haar cut gap 3, not a small gap. At the requested beta range the text supplies no estimate making its “fatal” conclusion a theorem. The GUIDE control is one model observation, not that estimate.

## Defect 3: the flat-gap comparison overstates what the identities show

**Section 3.2 and its result echoes: HOLDS AFTER CORRECTION of the placement; FAILS as a proof of logical independence or a universal method exclusion.**

The flat 2D chiral mass gap is spatial correlation decay. Here gamma is an odd Poincare constant for spin-coordinate dynamics, under a quenched law with Phi_env. These are distinct statements. The note supplies no comparison theorem in either direction. A typical-environment estimate omits the flat null environment, but that observation alone does not prove logical independence. A flat-model theorem might enter a comparison argument; none is supplied or ruled out here.

Even with Phi=1, a magnetization test gives an **upper bound** of susceptibility type on a dynamical gap. It does not identify that gap with `1/chi`. Nor is an inverse correlation length the same gap. Moreover, a small positive constant depending on fixed beta is still “order one” in N. The quoted values below `1/100` do not contradict TYP-1 without a specified numerical gamma_*.

The corrected placement is: the bare local factor has beta_sigma=beta, but neither the flat model nor its mass gap controls the full conditional law by a theorem given here. CUT-TYP remains open. The statement “the flat model is the worst case” is also unproved: maximal symmetry alone orders neither Poincare constants nor the effect of Phi_env.

**Section 4.1: HOLDS only as the explicitly conditional patch test; its claimed bad-event rate remains unproved.** If a patch really has `E<xi_x,xi_y>>=m^2`, averaging the four coordinate tests gives a direction with variance at least `m^2 A^2/4` and energy at most A. Thus `gamma<=4/(m^2 A)`. Exact flatness is a null event. A positive-probability approximate-flat event, its probability, stability of the correlations, and compatibility with Phi_env are all missing. No `exp(-C' L_1/c_0)` lower probability bound or consequent failure of RARE has been established.

**ORBIT's interpretation, lines 332–342: FAILS where it asserts a proved rotor scale or a forced local-move mechanism.** For a gauge-trivial local connection, the bound is `4 exp(-osc_orbit log Phi)/(pi^2 N)`. Section 4.1 supplies an upper bound only under its unproved patch-order assumption. These do not establish a two-sided `1/N` scale. Losing an exact rotational symmetry does not prove an extensive barrier on every path, or that every useful path consists of local moves. The literal uniform rotation path always exists. The estimates on its defect and on other paths remain open.

## Spectral width, coupling and arithmetic

**W, lines 169–177: HOLDS.** For sides at least 3, there are four distinct neighbours. Thus `tr A_R=0`, `tr A_R^2=16N`, and the mean squared eigenvalue is 4. If the extreme eigenvalues are l and u, averaging `(lambda-l)(u-lambda)>=0` gives `-lu>=4`. Therefore `(u-l)^2=(u+l)^2-4lu>=16`. This is a connection-independent statement about the specified block adjacency matrix.

**W's application, lines 179–186: HOLDS AFTER CORRECTION.** In the sign convention of [Bauerschmidt–Bodineau, Theorem 1 and equation (1)](https://arxiv.org/html/1712.03676), the density is `exp(-sigma.M.sigma/2)`. The matrix matching the local factor is `M=beta[(u+epsilon)I-A_R]`, not `beta[A_R-l I]`. Its limiting norm is `beta(u-l)`. The paper states the theorem for scalar site couplings; the vector-block version uses the same Gaussian splitting and one-site covariance bound. In either case, this particular width test requires `beta(u-l)<4`, hence beta<1 is necessary. It is not sufficient for all connections. This says nothing about all spectral or all single-site methods. The manuscript's broader title and RESULT claim must be narrowed to the named tests.

The cited primary theorem and proof were checked on its arXiv HTML page; no Balaban paper was fetched. The degree-four chord-influence test uses `4 beta/4=beta`, hence also stops at 1, **if using that specified test**. Its upstream source is row 933 section 5 and the checked six-neighbour chord estimate it names; it is not a universal Dobrushin/Poincare impossibility theorem. Phi_env remains outside both applications.

**Section 2.3 arithmetic: HOLDS as evaluation of the displayed approximations, with the following restrictions.**

| Entry | Hand check and scope |
|---|---|
| `g_sigma^2` | `1/2.3=10/23`, `1/2.6=5/13`; the rounded 0.43 and 0.38 are correct in the specified convention. |
| Correlation lengths | Substituting the displayed exponential values gives `0.0416*1374/sqrt(7.226)`, about 21.3, and `0.0416*3526/sqrt(8.168)`, about 51.3. These reproduce 21 and 51. The recalled two-loop formula is an asymptotic input, not an error-controlled lattice correlation length at these beta values. No order or rotor estimate follows for the cut with Phi_env. |
| Bessel ratio | With `t=(23/20)^2`, `I_1=(23/20) sum_{m>=0} t^m/[m!(m+1)!]` and `I_2=t sum_{m>=0} t^m/[m!(m+2)!]`. Successive terms have ratios `t/[(m+1)(m+2)]` and `t/[(m+1)(m+3)]`; geometric tail bounds after m=7 give `2.0978000<I_1<2.0978002` and `1.0054314<I_2<1.0054318`. Thus u rounds to 0.479. No run is used for these bounds. |
| Walk products | From the rounded inputs, `2.64*.479=1.26456` and `2.64*.479^2=0.60572424`. Thus 1.26 and 0.61 are correct rounded arithmetic. The connective constant is a numerical input, not an exact 2.64, and these products alone are not a convergence/divergence theorem for the normalized quenched expansion. |
| Section 3.2's polarization | The same positive Bessel series, now with `t=(23/10)^2`, gives `.69<I_2(4.6)/I_1(4.6)<.71` (retain m=0 through 8 and bound the tails by their next-term ratios). Thus 0.7 is reasonable rounded arithmetic. This does not establish that a typical local field has magnitude `2 beta`, or control Phi_env. |

The claims “every plaquette ... near 0.60/0.67” and “holonomy half-angle near 53 degrees each” **FAIL as deductions from M5**. A mean plaquette value gives no concentration, and `arccos(E cos theta)` is not a typical theta. Even arccos(0.67) is about 48 degrees. Furthermore, the untwisted Wilson mean is not automatically the mean under the projected law w_e. The quoted Monte Carlo inputs remain unverified recalled values.

The section-3 literature discussion supports only a search report: no matching theorem was supplied by the sources read. Failure of these sufficient tests neither proves that no convergent expansion exists nor proves that no method controls any quenched model above beta=1. The other recalled literature entries are not used as mathematical premises here.

## CUT-3D

**Lines 373–393: HOLDS**, for the displayed identities and conditional inequality, with integer `r>=0` and the stated separation from time 0. There are `a` binary temporal signs on a time cycle. A centre flip at any integrated layer toggles its two incident signs. For each of the two arcs between the fixed layers, these toggles span exactly the even-parity sign changes. Their total rank is `a-2`. Thus each of the four parity classes has `2^(a-2)` sign assignments, proving (a) after normalization. Summing each incident sign gives the cosh factor in (b); the omitted factors are independent of B_r. An F depending on B_r only through time s has the same energy as its restriction to that layer. The conditional law is invariant under the whole-layer centre flip, so its odd marginal inequality gives (c), followed by integration.

**The “finite-range” reading at lines 395–398: HOLDS AFTER CORRECTION.** At fixed signs the spin Hamiltonian has nearest-neighbour bonds and external boundary fields. After summing signs, `log cosh(beta sum_x ...)` couples the whole transverse layer. The cosh-mixture pi_r itself is not a finite-range Gibbs law in the ordinary spin-only sense. Keeping the global layer signs, or conditioning on them, must be explicit. The fixed-sign components are not separately centre-even; a gap estimate for them would need a mixture argument. The full environment env_r is finer than the two-slice env_k; enlarging r makes it less fine, so “fixes more” is only relative to env_k.

## Defect 4: the proposed Gaussian comparison uses the wrong Hessian

**Lines 400–416: FAILS for the asserted spin-wave identification and the universal U(1) zero mode.** The form `4-A_R` is the unconstrained covariant Gaussian form. For unit spins expanded along tangent vectors eta around a configuration zeta, the second variation of the local energy is

`beta sum_<xy> [(|eta_x|^2+|eta_y|^2)<zeta_x,R_xy zeta_y>-2<eta_x,R_xy eta_y>]`.

Its diagonal is `sum_y <zeta_x,R_xy zeta_y>`, not 4 in a frustrated configuration. Its domain is the tangent bundle, not all of `(R^4)^Lambda`; the full cut also has Phi_env's contribution. No quadratic argument here proves an odd gap.

For the unconstrained Gaussian form, the exact identity is

`<c,(4-A_R)c> = sum_<xy> |c_x-R_xy c_y|^2`.

Its kernel consists of covariantly constant **vectors**, not rotations commuting with holonomies. An abelian U(1) connection can have a plaquette holonomy `e^(i phi)!=1`. A nonzero parallel complex vector would satisfy `c=e^(i phi)c`, impossible. Choose one transverse link of g with that phase and h trivial: this is an allowed U(1) environment. Thus `lambda_0=0 for every environment` is false. Nevertheless the XY angular energy is invariant under adding a constant angle to every spin; its angular Hessian has that zero direction. This explicitly separates the two operators. Conversely, in SU(2), g=h can have nonabelian holonomy while R acts by conjugation and fixes the real quaternion 1. Nonabelian holonomy alone also does not prove positivity of this vector Laplacian. A uniform order-one bottom for typical connections is a further estimate, not an identity.

## U(1), frozen Q_8/2T, and the LSI statement

**The U(1) rotation fact test, section 2.2(3): HOLDS for the local action.** The phases `xi_x -> e^(it)xi_x` cancel on every XY bond, even with frustrated abelian connection. They need not preserve Phi_env. This does not assert a parallel vector for that connection.

**The cut-toron tests at lines 288–290, 333–334 and 413: HOLDS AFTER CORRECTION of their model and scale.** Their exact input is the monopole-free Gaussian/Villain Model G of row 930, not arbitrary compact U(1) Wilson theory. Row 933's checked factorization gives, at `s=a/2`, `gamma_k=mu_0(tau)/(2N)` for every environment. The mean cut angle has metric cost `1/N`; the relative-toron form defining mu_0 has cost 2. Thus the factor `1/(2N)` is consistent. For any `g_0>L_1 mu_0/(2N)`, every environment is bad and RARE-P's hypothesis fails. The ORBIT estimate preserves a barrier-weight factor, but by itself does not reproduce the small-tau prefactor in mu_0. Calling it the exact order uniformly in tau is unwarranted.

**The Model G overlap claim at lines 364–367 and 414: FAILS as an all-size fact test.** The asserted uniform bound on the variance v of the conditional differences is not proved. Finite variance in each finite box is insufficient to keep `exp(-2v)` of order one as the box changes. Row 933 already identified this uniformity issue for the earlier winding-line argument; the present note supplies no new conditional covariance estimate resolving it. Nor does `N exp(-2v)>2/c_0` by itself contradict Q3: Q3's threshold is `2/[c_0(1-delta)]`, and its requirement is a positive probability, not a full averaged bound. Keep the exact soft-toron test instead. No assertion about monopoles is checked here.

**Frozen-group test, lines 289–291: HOLDS at beta=infinity for the single-link heat-bath form, with side lengths at least 3.** Every conditioned link is fixed by a spatial flatness plaquette and its other three links. Hence every single-link conditional variance is zero, including those summed within a cut. The even law still supports a cut and its centre flip, so a nonconstant odd function has zero Dirichlet energy. This is not a continuous-gradient statement, nor a heat bath refreshing the whole cut at once. At finite beta on a finite lattice the conditional weights are strictly positive; the zero-gap conclusion cannot be extended literally there.

For the requested frozen Q_8 and 2T arithmetic, the already checked parent fact test is `gap-oddgap-max.md:253–322`, with its source check at `gap-oddgap-check-astra.md:147–185`. A commuting noncentral tuple lies in one maximal cyclic subgroup. Thus the respective flat counts are `16+3(4^4-16)=736` and `736+4(6^4-16)=5856`. An anticommuting pair uses two orthogonal imaginary quaternion axes: six choices followed by four, and four choices for the remaining central holonomies, giving 96 in both groups. Thus `r=3/23,1/61` and `p=(1-r)/2=10/23,30/61`. These small counts agree. They are the prior row-930/933 result, not a new derivation or a finite-beta estimate. Row 936 contains no new finite-group computation.

**Section 6.2's LSI implication and numerical seed exclusion: HOLDS.** For mean-zero gauge-invariant f, linearize at `F=1+t f`: `Ent(F^2)=2t^2 E f^2+o(t^2)`. Hence LSI with constant alpha implies PI with the same constant, including the odd sector. At the Model G seed, the checked G4 bound is `lambda_odd<8.2*10^-9`, while `L_1/N=1/20`. Therefore `alpha>=C L_1/N` is excluded for `C>1.64*10^-7`, and certainly for the printed `C>1.7*10^-7`.

**The broader “not group-blind / only at large tau” conclusion: HOLDS AFTER CORRECTION.** The stated seed bound excludes the displayed range of constants, not every positive C. A uniform family can fail more strongly: with fixed a,L_1,beta and N increasing, G4 gives `lambda_odd/(L_1/N)<=10.3 tau^(-3/2) exp(-pi^2/(8tau)) ->0`, where `tau=a L_1/(4 beta N)`. Thus no fixed positive C works over that family. Other geometric families must be stated separately. Large-tau convergence of an odd gap is not by itself a proof of an LSI on the full law. EVEN-PI is weaker than an LSI with the same constant; nothing here proves that obtaining it is easier, or that (TYP-1,EVEN-PI) is logically a weaker pair than every proposed original pair.

**Section 6.3's small-N item: HOLDS AFTER CORRECTION to a proposed test.** A single coordinate yields a Rayleigh **upper bound** `(1-q)/q`; it is not generally the odd eigenvalue of a nonuniform even one-spin law. At fixed finite beta compactness gives positivity, not a beta-uniform order-one constant. The character solution for a four-link ring is explicitly not done. It contributes no checked fact test.

## Defect 5: the GUIDE run does not sample the law in Q

**Section 6.4: HOLDS only as reported untwisted-model arithmetic; FAILS as a test establishing or refuting Q3/TYP-1 for w_e.** The named script and logs are outside the permitted on-disk source set. A filename inventory of this checkout found no copy. They were not read or rerun, and the code, thermalization, error bars and execution/resource claims remain unverified. No Monte Carlo or eigenvalue job was launched for this check.

Even taking the run description literally, its law is the untwisted Wilson component. The desired law is the four-component projection in M1. In row-930 notation, for an even observable the symmetrized untwisted two-slice density is proportional to `E_s E_(a-s)+O_s O_(a-s)`, whereas w_e is proportional to `E_s E_(a-s)`. They are not equal in general. A conditional replica updated within the untwisted component is likewise not a replica from nu_k. M5 does not remove this distinction. At finite sweep separation, it also does not make the starting cut and the later cut conditionally independent.

The printed table's multiplications can nevertheless be checked without the missing logs:

| N and printed E[q^2] | Product from printed values | Printed N E[q^2] |
|---|---:|---:|
| 16, .171 | 2.736 | 2.7 |
| 36, .070 | 2.520 | 2.5 |
| 64, .108 | 6.912 | 6.9 |
| 144, .089 | 12.816 | 12.8 |
| 36, .114 | 4.104 | 4.1 |
| 64, .088 | 5.632 | 5.6 |
| 144, .035 | 5.040 | 5.1 |
| 64, .072 | 4.608 | 4.6 |
| 144, .049 | 7.056 | 7.1 |

The seventh row rounds to 5.0 from the displayed mean. It is compatible with 5.1 if the unrounded mean was at least `5.05/144` (about .03507). Without the raw value this is a rounding ambiguity, not evidence of a bad run. The control's products and error estimates cannot be reconstructed from the ranges alone.

The data do not prove an asymptotic growth law or a deconfinement transition; “TYP-1 fails there as it must” must be removed. In addition to the law and mixing problems, Defect 1 invalidates that proposed averaged-overlap refutation. For a genuinely sampled environment with `NQ=5`, Q2 does give `gamma<=1/5`; the table does not establish that value typically under w_e. The arithmetic `4/78.4` about .051 is correct, but it supplies no seed flux bound. The explicitly unrun twisted sectors, seed box, beta=2.6 and Gaussian test remain unrun.

## Verdict map

Line numbers refer to the pinned `gap-cuttyp-max.md`. Rows cover the labelled statements and the separate conclusions made from them. A FAILS verdict on an inference does not refute the desired Wilson inequality.

| Source statement | Verdict | Exact disposition |
|---|---|---|
| M1, 88–91 | HOLDS | Four slab-sign terms, with the specified wall-potential transfer kernel. |
| M2, 93–100 | HOLDS | Exact local factor times the positive bulk integral of two coshes. |
| M3, 102–106 | HOLDS | Bare local beta_sigma=beta in the displayed convention. |
| M4, 108–112 | HOLDS AFTER CORRECTION | Generic centralizer statement; absorb signs into both representatives; account for winding holonomies. |
| M5, 114–116 | HOLDS | Disintegration and conditional-replica exchangeability, without a disorder estimate. |
| M6, 118–119 | HOLDS AFTER CORRECTION | Conditional sign-mixture representation, with remaining bulk links integrated. |
| 2.2(1), 141–144 | HOLDS | Ambient Laplace-transform/log-convexity identity. |
| 2.2(2), 145–149 | FAILS | Exact mixture does not prove a tunnelling-small gap. |
| 2.2(3), 150–152 | HOLDS | U(1) local rotation symmetry, not full-law or vector-Laplacian invariance. |
| 2.3, 154–165 | HOLDS AFTER CORRECTION | Displayed arithmetic holds; recalled inputs and typical-angle/order claims are not estimates. |
| W matrix theorem, 169–177 | HOLDS | Width at least 4 by the exact trace calculation. |
| W criterion use, 179–186 | HOLDS AFTER CORRECTION | Correct matrix sign and restrict to the named width/chord criteria. |
| 3.2, 190–216 | FAILS | No proof of logical independence, worst-environment order, or universal method exclusion. Correct placement given above. |
| 3.3 literature conclusions, 218–233 | HOLDS AFTER CORRECTION | Search/recall record only; no matching supplier established. |
| 4.1 patch test, 239–251 | HOLDS AFTER CORRECTION | Conditional Rayleigh bound holds; patch probability/order and the proposed rate remain unproved. |
| CAP, 253–266 | HOLDS | Exact conditional implication and entropy specialization. |
| RARE-P, 268–282 | HOLDS | Exact conditional implication; its lower bound does not cap the actual gap. |
| RARE-P U(1)/frozen fact tests, 288–292 | HOLDS AFTER CORRECTION | Model G at half-time; finite groups only at infinite beta with single-link heat bath. |
| LOC, 294–310 | HOLDS | Conditional local-capacity implication with the stated overlap count. |
| TYP-1 aggregation, 315–318; 6.1 item 2 | HOLDS | Markov bound plus RARE-P; LOC still needs LOC-CAP. |
| ORBIT inequality, 320–330 | HOLDS | Exact path/Cauchy/density-ratio estimate. |
| ORBIT physical/flat interpretation, 332–342 | FAILS | No two-sided rotor bound or necessity of local flip paths proved. |
| Q1–Q3, 346–361 | HOLDS | Replica identity, Rayleigh upper bounds and positive-fraction necessary condition. |
| Q's Model G overlap claim, 364–367 | FAILS | Missing uniform variance bound; stated Q3 refutation also drops `1-delta`. |
| OD as necessary, 369–371,428,450–452,529–531 | FAILS | Fixed bad fraction allows `delta N` in averaged NQ. |
| CUT-3D (a)–(c), 373–393 | HOLDS | Sign-class count, conditional density, and odd conditional inequality. |
| CUT-3D finite-range/fatal reading, 395–398 | HOLDS AFTER CORRECTION | Finite range at fixed signs only; remove proved “fatal” assertion. |
| Gaussian/abelian comparison, 400–416 | FAILS | Wrong constrained Hessian; explicit abelian nontrivial-flux counterexample to the claimed parallel vector. |
| LSI linearization and seed bound, 434–440 | HOLDS | Same PI constant; printed `C>1.7e-7` exclusion is safe. |
| LSI interpretation, 440–444 | HOLDS AFTER CORRECTION | Retain constants and geometry; no proof of relative difficulty or large-tau LSI. |
| Small-N proposed test, 456–458 | HOLDS AFTER CORRECTION | Coordinate Rayleigh bound only; no solved ring test supplied. |
| GUIDE table, 468–478 | HOLDS AFTER CORRECTION | Printed products check, with one double-rounding ambiguity; raw observations/errors unverified. |
| GUIDE implementation/observations, 462–466,480–481 | FAILS verification | Script/logs absent from permitted source set; no assertion that the reported observations are false. |
| GUIDE extrapolations, 484–496 | FAILS | Untwisted finite-lag data neither establish nor refute the projected-law hypotheses. Fixed-environment `NQ=5 => gamma<=.2` remains conditional. |
| Open-input declarations and result, 419–444,500–550 | HOLDS AFTER CORRECTION | Keep the inequalities open; remove OD's necessity and the failed interpretations from the summary. |

The line-by-line check tests the overlap implication against its allowed exceptional set and tests the Gaussian claim against the constrained second variation and a holonomy counterexample. The valid identities and inequalities are verified through their plaquette/sign, Dirichlet and moment arguments; repeating those arguments is not claimed as a separate independent derivation. Prior row-930/933 results are credited and used at their stated scopes. No computer-assisted proof, mass-gap conclusion, flux-half conclusion, audit, status change, source repair, commit or push was performed.

RESULT: FAILS as written: the claimed necessary averaged-overlap test and the Gaussian/U(1) comparison fail, and several interpretations exceed the proved statements. M1–M3, M5, W's width bound, CAP, RARE-P, LOC, ORBIT's inequality, Q1–Q3 and CUT-3D's identities/inequality hold at the scopes above; M4/M6 and the placement require corrections. The Model G soft-toron and infinite-beta Q_8/2T single-link tests survive. GUIDE products were checked, but the original run is unverified and does not test w_e. CUT-TYP and the actual typical-gap, capacity/even-gap and force-covariance inputs remain open; no status is granted.
