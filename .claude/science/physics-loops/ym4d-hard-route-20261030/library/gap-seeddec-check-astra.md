# Repo search

Check item: FINISH row 891, gap-seeddec-check-astra. Requested base: `0fc143e90`.

Prior coverage file `library/prior/gap-seeddec-check-astra.md` is absent. This is research text and grants no status. No computation will discharge a claim.

Searches before derivation used `git grep -n -i -E`, all five refs below, `*.md` and `*.tex`, bounded by head 80/100. Terms: `SEED-DEC|gap-seeddec|same.class.{0,35}(pair|box)|period.8 snake|1,120,616`, then `half.integer.{0,50}(cycle|edge)|minimal relative filling|filling.Peierls|SEED-DEC|chessboard.{0,35}(decoder|norm)|commuting triples`. Neither completed search reached its cap. No target statement or prior check was found outside this lane. This is a search result, not an absence theorem.

- `origin/main`: `993f5e4f6d11a7e20a1cab9612c5749a53bae073`
- `pr/10114`: `f76f6c649cff7dffbab664d8976e680e8f287fe9`
- `pr/10133`: `89faef229ff6e6bde42baad15ed8270c2f4087d8`
- `pr/10134`: `1e70c7211a2cdbc39001e619f1dd89db45e25851`
- `pr/10141`: `c73ad7b177d94f89ff37b77386936e3d52b48b05`

Relevant method hit: `pr/10141:research/ym4d/library/ag1.md:1024-1075`, Theorem 10, already expands a sum of cell-local witnesses, applies a chessboard product estimate in distinct tiles and sums the products of their norms. Its exact conclusions are survival probability at most `alpha_k Q^{-(k-h)}` and joint survival/other-tile probability at most `alpha_k Q^{-(k-h)} alpha_k^m`, under Lemma 9, K, MI, COV, CB and the two-run interface. This supplies the union/subadditivity method, not TOP or the new child-pair estimate. `gates/ag1-gate.md:61` explicitly identifies this subadditivity step. Credit Claude's AG1/P-an drafts and Codex's AG1 distillation (its provenance line at the pinned ref); no new general subadditivity lemma is claimed here.

Other hit files: `ym4d-existence/EXISTENCE.md` and its session snapshots on pr/10114 and pr/10133 concern simultaneously diagonalizable SU(N) commuting holonomies and a positive trace-character sum, not counting finite-group flat-connection orbits; `ym4d-proof/CODEX_REVIEW_SPHERE.md:81` concerns half-integer coordinate positions, not representation parity. `research/ym4d/library/sr1.md:520` lists chessboard infrastructure. The frame-coded motif, anomalous bulk-category and four-cube cutting-kernel hits are different objects. These locator matches supply no target result.

Read `prior/repo-search-2026-11-08.md` whole; its thirteen targets concern the earlier analytic hard-route interfaces, not this decoder. Searched `open-registry.md` for seed/decoder, parity, half-integer, filling, and gap-seeddec/gap-brainstorm: no competing owner of this check; TOP-W is an unrelated classical excess-energy estimate. The actual assigned check is FINISH row 891.

Outline lookup: `sa-index/README.md` usage instructions; searches across chunk files and `obligations.md` for decoder, relative filling, parity cycle, half-integer, electric flux, chessboard. No decoder locator found. Read neighbouring `chunk-03.md:23-38`, obligations 74 and 85, then SA `2885-2939`: (AM6) is the finite one-direction chessboard bound for positive bounded slab functions with positive infimum, proved by maximizing normalized fillings. Reuse that existing method; it is not itself a theorem about signed Wilson insertions or this label law. Sussman and Alpoge, with Claude and Codex, receive credit for that source. `lit-balaban.md` has no gap/flux/chessboard/Peierls/decoder match; no unavailable Balaban paper is imported.

The local predecessor `gap-brainstorm-check-astra.md:166-328` already supplies the overlap/idempotence failure, the conditional 351 count, the colour power-loss warning, and the rate/background mismatches. This check tests whether the changed construction answers them; it does not repeat that predecessor's counterexample.

# Statement checks

Provenance: OpenAI Codex, dispatched as gpt-6-astra xhigh, checking Claude Fable 5.2 max; source checkout `0fc143e90f28b803c8942bdafa522fab203df7b6`. Research check only, not an audit or status grant. Checked source SHA-256: `196098a074522ec6da99d8fa7869486775f6150b25920d67e7f9611c8aa730e9`. Source abbreviations: S = `gap-seeddec-max.md`; CK = `gap-brainstorm-check-astra.md`. No numerical evidence is used as proof. This report is the sole working checkpoint. All requested checks are complete; the remaining mathematical obligations are the two seeds, RIG, and the quantitative S1/S2 inputs.

## 1. Lemma A, Lemma B and Corollary C — HOLDS

S Step 3a. Check the construction cell by cell. If a plaquette P is interior to both N_a and N_b, its two incident cubes q_- and q_+ belong to both boxes. The cocycle at each q gives `V_a(q)+V_b(q)=W_ab(q)`. Summing these two equalities gives
`(boundary V_a)(P)+(boundary V_b)(P)=(boundary W_ab)(P)=D_a(P)+D_b(P)`.
Thus the corrected fillings agree on every shared interior plaquette. An edge interior to N_a has all four incident plaquettes interior to N_a, including when an endpoint lies on an end face normal to the edge. The patched D therefore has boundary gamma on that edge. Setting unread plaquettes to zero causes no boundary error there.

Lemma A uses the relative groups H_2(B, boundary B)=0 and H_3(B, boundary B)=Z_2 correctly. Corollary C uses the ordinary group H_1(B)=0 correctly. A connected component of the residual cycle remains a cycle. No torus is replaced by a ball. For the general wording of B, an intersection of arbitrary cyclic boxes need not be one box; interpret its relative boundary componentwise (or simply impose the stated boundary equation on common interior plaquettes). The cell proof above needs no connectedness of that intersection. All overlaps actually used in T0 are core-boxes, so this convention causes no application gap.

## 2. The 1/4 rule, Lemma T0 and Lemma T1 — HOLDS

S Step 3b. On a triple overlap O_3, each of the four small chains used to compare W_ab with the O_3 reference has fewer than |O_3|/4 cubes. The difference of the two proposed transition chains is a relative 3-cycle. Its support has fewer than |O_3| cubes; it therefore cannot be the nonzero relative 3-cycle [O_3]. The transitions agree on O_3. Summing the three transitions cancels each reference term twice. Strict inequality and smallness on every contained core-box, not merely on O, are essential. No transitivity of a diameter condition is assumed.

For T1, the cover does contain every edge as an interior edge, including core seams: in a perpendicular coordinate choose the box starting one core earlier when the coordinate is a multiple of g; otherwise choose the box starting in that core. In the edge direction choose the core containing its initial vertex. These choices put the four incident plaquettes inside the chosen box. Lemma B thus leaves a homologous residual cycle supported only on edges whose containing boxes are all unclean. If its total class is nonzero, at least one connected component has nonzero class. Boxes chosen along that component form a site-connected family and contain the component. Their union cannot fit a proper box. This proves T1 for every local nonempty filling rule; symmetry is not needed here.

The single-plaquette check for g>=3 is also consistent: an interior plaquette has two noncollinear interior boundary edges, which fix its unique area-one filling; if it is not interior, its loop has no interior edge. The illustrated decimal-position straight-line example is unnecessary to the proof and is not used as a lattice construction.

## 3. Lemmas G and H; TOP and TOP+ — HOLDS

S Steps 3c and 4. For G(b), lift the boxes along a spanning tree. In each coordinate the range of their initial indices is at most n-1: the sum of the absolute increments on the tree bounds the range. Adding the box width gives (n+1)g_j sites. The stated size restriction makes the resulting cyclic interval proper. G(c) is the integer inequality `p mod G + w - 1 <= 2G-1` for `w<=G+1`. Nine connected boxes therefore fit a parent at ratio 10, and eight parity classes force two with the same class; their tree distance and coordinate offsets are at most eight.

In H, choose a connected nine-member subset containing the specified member, not an arbitrary subset. In the induction, each old box N is contained in Q(N); adjacency of old boxes therefore gives adjacency or equality of their new boxes. The union of the new family contains the old union. If it had at most eight members, G(b) would put it in a 9g_j box, contradicting the hypothesis. This is exactly the invariant the induction needs. No fillings are transported up the hierarchy.

T1 now implies TOP at every admitted level. The families Q(N) in H also prove TOP+: if a connected family had at most L/g_j-2 members, G(b) would contain it in a proper box of at most L-g_j sites per side. Thus the family has at least L/g_j-1 members. The torus divisibility makes the eight class tilings well-defined. These conclusions remain purely deterministic.

## 4. The period-eight snake at ratio four — HOLDS AFTER CORRECTION of scope

S N3 and Step 3c. Repeat the eight printed indices by translation (8,2,2). Their parity classes, in order, are 000,100,010,110,011,111,001,101. Consecutive indices differ by at most one in each coordinate, including across the period. A repeated class is at least eight apart in coordinate one. At ratio r<=4 a parent contains child indices in an interval of length 2r-2<=6, so it contains no same-class pair from the snake. This is a hand counterexample to the proposed *general connected-set hierarchy lemma* at those ratios.

It does not construct a cycle gamma and a filling rule whose actual unclean set is exactly that snake. Hence it does not by itself refute TOP for the specific minimal-filling decoder at ratio four, or prove that ratio ten is necessary for that decoder. Replace the unrestricted wording “ratio four fails” by “the connected-set implication used in Lemma H fails at ratio four.” The ratio-ten proof above is unaffected; five through nine remain undecided here.

## 5. Lemma CH, C_3 and the answer to check 882 — HOLDS given CE

S Step 4; CK section 3. Write a parent reflection plane correctly as `x_i=k g_{j+1}-1/2`. It sends a child index x_i to `20k-x_i-2`, which preserves parity. A fixed witness pair, reflected throughout a parent tiling, therefore gives 2N distinct child boxes in one child tiling. Containment in disjoint parent site-blocks ensures distinctness. Symmetry of M and the label law gives the same child norm z_j to every factor. Child CE bounds the disseminated pair probability by `z_j^(2N)`, hence its parent norm by `z_j^2`.

Next expand the union over witness pairs separately in each parent. Parent CE bounds each heterogeneous product by the product of the corresponding parent norms. Summing factorizes. This is the already used AG1 subadditivity method, now with the new same-class witness construction. Colours are summed *after* the child estimate; no witness product is thinned to one eighth of its factors. CK's overlap/idempotence counterexample does not apply: each event reads its own box, and every product identification uses disjoint edge sets. This establishes the claimed escape from check 882, under CE and covariance.

Independent hand count: in one coordinate the ordered even-offset count is `10+2(9+8+7+6)=70`; the odd-offset count is `9+2(8+7+6+5)=61`. Multiply across coordinates, subtract identical boxes, and divide by two:

```math
 |\Pi|=\frac{(70+61)^3-(10+9)^3}{2}
       =\frac{2,248,091-6,859}{2}=1,120,616.
```

Thus `z_{j+1}<=C_3 z_j^2` and induction gives `z_j<=C_3^{-1}(C_3 z_0)^{2^j}`. No enumeration or run discharges the count. The exact seed is `z_0<1/1,120,616`; “below 8.93e-7” is only a rounded description, not a sufficient replacement threshold.

CE is an explicit premise of this verdict. The source itself does not rebuild CE for the one-slice law. CK explains why disjoint one-cell label insertions inherit the untwisted reflection form; the outline's positive-profile AM6 is credited prior methodology, not an automatic substitution of signed gauge functions into its hypotheses. No magnetic-background CE is asserted here.

## 6. OUT(U), OUT(H), OUT(P) and the consumer rate — HOLDS AFTER CORRECTION

The three displayed OUT bounds hold on their stated geometries (and H/P under CE). U is the union bound from T1. H adds one-cell CE and CH. For P, fix a deterministic spanning tree and traversal for each rooted animal; its length 2(n-1) gives at most `26^{2(n-1)}` animals. At least ceil(n/8) boxes have one class. Retaining those boxes and applying CE gives at most `z_j^{n/8}`. Thus A=676 is a hand-proved constant; no recalled improvement is needed.

At `L=4g10^J`, H has exponent `(L/(4g))^{log(2)/log(10)}`. It cannot supply the fixed positive rate in E17. P at a fixed level can supply an exponential rate. From `z_j<=C_3^{-1}(C_3 z_0)^{2^j}`, a strict uniform `C_3 z_0<1` eventually makes `A z_j^{1/8}<1`, but does not guarantee the rate demanded by eta_*.

Correct the stronger sentence “so this is a level-0 demand.” The displayed sufficient level-j inequality is

```math
 A z_j^{1/8}\le\eta_*^{g_j/2}.
```

It need not be verified at level zero: the actual z_j may be far smaller than its CH upper bound. Even that upper bound does not make the assertion algebraically necessary. Put `b=log C_3`, `d=8 log A`, `u=-log(C_3 z_0)` and `v=4g log(1/eta_*)`. Its level-j sufficiency condition is `2^j u >= d-b+10^j v`; the minimum over j need not occur at zero. For small positive v, level one already lowers the required u relative to zero. Retain the displayed level-zero condition as a simple sufficient condition, not a necessary demand or an exclusion of improving at another level. The recalled A=26e count and its decimals are not needed or re-established here.

## 7. SEED-DEC-U and its derivation — HOLDS AFTER CORRECTION of domain

S Step 6; `gap-expose-astra.md:575-599`; `gap-hs-max.md:168-172` and its existing check `gap-hs-check-astra.md:137-148`. The prior P1 identification gives, for each required m and i,

```math
 p_{m,i}(a)\le \nu_m([\gamma]\ne0)
       \le64\max_N\nu_m(N\text{ unclean}).
```

Thus a bound uniform over those m of `64 p_0(a/4)<=K(a) sqrt(S_ev(a))/8`, together with `64 p_0(a/4)<1/192`, gives exactly both FQ inequalities. This uses no spatial RP and no untwisted-to-twisted comparison. The magnetic twists change the law, not the vertex gauge constraint that makes gamma a cycle. The all-component event is stronger than the single pairing needed by FQ; it is a sufficient condition, not an equivalent reformulation of the consumer.

Require `a>=8`, as well as a divisible by four: g=a/4 must satisfy the defined g>=2. For rectangular sides (a,c,d), also require each side to be a multiple of g and at least 4g before replacing 64 by acd/g^3. These are the domain corrections. The local bound itself remains OPEN. No decay estimate is derived from topology. The separate existing implication FQ -> F-h is cited, not rechecked or counted as new work. The fixed-coupling rate and cutoff-uniform first-passage seed remain distinct, as already specified in `gap-finishline-opus.md` section 2.4.

## 8. SEL; frozen Z_2, Q_8 and 2T — HOLDS in the frozen untwisted model

SEL's general inequality is just OUT(U) reversed, and its uniform-in-J consequence is OUT(H). Its finite-group premise must mean the normalized zero-temperature limit at fixed finite volume and time: after removal of a scalar, the transfer operator tends to the projection onto gauge-invariant flat configurations. Indeed the kinetic convolution tends to the identity, while the normalized spatial weight tends to the flat-configuration indicator; these commute with gauge projection. The scalar cancels from the trace ratios. This is not an assertion at any finite beta.

That projected space has one orthonormal orbit vector for each simultaneous conjugacy class of commuting triples. A central cut flip permutes those vectors. Its trace is the number F of fixed orbits, and
`p_i=(N_G-F)/(2N_G)`. The two distinct central triples (1,1,1) and (-1,1,1), with the minus sign in coordinate i, are exchanged. Hence `N_G-F>=2`, proving `p_i>=1/N_G` and `p_0(g)>=1/(64N_G)` for Q_8 and 2T (and the other stated finite subgroups).

The printed Q_8 count 92 can be checked without enumeration: eight central triples; each remaining commuting triple belongs to exactly one of the three cyclic order-four subgroups. Each contributes `(4^3-2^3)/2=28` conjugacy orbits, since simultaneous inversion pairs noncentral triples. Thus `N_Q8=8+3*28=92`, and the stated lower bound is `1/5888`. No value of N_2T is required for the printed symbolic bound; finiteness already makes it positive.

For Z_2 the eight flat holonomy states form the regular representation of the three cut flips. Each joint electric-parity eigenspace is one-dimensional, so the normalized projector assigns each homology class probability 1/8. Consequently `P([gamma]!=0)=7/8` and `p_0(g)>=7/512`. Equivalently, its electric-basis diagonal is uniform over all cycles. These lower bounds are valid for each g>=2 on the cube of side 4g. They neither prove rarity for SU(2) nor transfer the frozen bound to 2T at beta=2.3. The U(1) Coulomb paragraph remains an unproved comparison, as the source labels it.

## 9. PAR and the vertex identity — HOLDS; the claimed conditioning obstruction — FAILS

S Step 7.1. Summing the already checked OS identity by central parity replaces each normalized temporal kernel by its even or odd part. Dividing by k_beta gives respectively `(1+exp(-2 beta x))/2` and `(1-exp(-2 beta x))/2`. Multiplying back by the raw Wilson weights gives cosh or sinh. Thus both displayed PAR formulas have the correct normalization; the deleted-weight normalization error in the earlier OS note does not recur here.

A temporal-link centre flip at v reverses the six x_e incident to v and leaves the remaining action fixed. Its partition-function ratio is one, giving exactly

```math
 \mathbb E_\mu\exp\left(-2\beta\sum_{e\ni v}x_e\right)=1.
```

For beta>0, if all six x_e were nonnegative almost surely, the integrand would be at most one. Equality of its expectation forces every one of those x_e to vanish almost surely. PAR then gives no odd edge at v. This verifies consequence (b)'s stated implication.

There are three corrections to the subsequent reading. First, the pointwise independent-edge signed measure is supported on cycles exactly in the degenerate case where every q_e=0 (for beta>0, all x_e=0); otherwise the singleton of any edge with q_e!=0 has nonzero weight. Replace “never supported on cycles” by this qualified statement. Second, not every event has a sign-changing PAR integrand: `gamma=empty` has integrand `product_e(1-q_e)>0` for every gauge field. Third, the mean-one identity gives no estimate that the mean is carried by configurations of probability about exp(-16.6). Substituting the mean plaquette trace into an exponential is neither its typical value nor a tail estimate.

The signed kernel in PAR is not a conditional probability of gamma given U. Consequently it cannot be used *as if* it were such a probability. But this does not prove “no bound conditioning on a typical gauge field exists,” or exclude estimates that control both typical and atypical contributions to the signed expectation. The claimed universal obstruction fails at that inference. The exact identity survives and the seed remains open.

The centre-orbit Ising formula has an exact corrected reading: insert `1_{boundary h=0}` in its numerator and sum h' over cycles only. Centre averaging annihilates noncycles; on cycles it gives `w_h/sum_{h' cycle}w_h'`, whose denominator is a positive Ising partition function divided by the cosh factors. For frustrated couplings the numerator can remain negative. The anti/per partition-ratio identity follows in the same way. Neither identity supplies the stated typical-field or percolation conclusions.

## 10. HC and PB — HOLDS; filling-Peierls barrier — HOLDS AFTER CORRECTION

S Step 7.3. An edge-connected component Sigma of D+D_0 is a relative 2-cycle: all selected plaquettes incident to any one interior edge belong to the same component, and their number is even. Flipping Sigma preserves the filling constraint. Minimality gives `|Sigma intersect D|<=|Sigma|/2`, so `|Sigma intersect D_0|>=|Sigma|/2`. This proves HC for every minimal D, including ties.

For PB, a fixed n-plaquette Sigma must contain at least ceil(n/2) plaquettes of D_0. Union over those subsets costs at most `2^n eps^{n/2}`. Each plaquette has at most twelve edge-neighbours in three dimensions; the canonical traversal of a spanning tree has 2(n-1) steps. Thus `a_n<=12^{2(n-1)}=144^{n-1}` and the displayed PB bound holds for the existential choice of a minimizer as well. No independent-disorder assumption is used: FN supplies the joint subset bound.

Here is the precise density restriction. On a cube of n=2g sites per side, there are `3(n-1)(n-2)^2` interior edges and `3(n-2)(n-1)^2` interior plaquettes. Put rho_N equal to the average occupation of those interior edges. Every filling has at least `|gamma_N|/4` plaquettes. Taking expectations under FN gives

```math
 \epsilon\ge\frac{\rho_N}{4}\frac{n-2}{n-1}.
```

For the specific geometric majorant using `a_n<=c^{n-1}`, its sufficient smallness test `2c sqrt(epsilon)<1` can therefore hold only if

```math
 \rho_N<\frac{n-1}{c^2(n-2)}.
```

At large g this becomes the source's rho<1/c^2, giving 1/20736 for the proved c=144 count. If a suitable c=3 count were separately supplied, it would give 1/9. The note only recalls that count; it neither states nor proves it for these edge-connected relative walls. Consequently 1/9 is a hypothetical threshold of that chosen majorant, not a proved best possible Peierls threshold.

The broader claim “no Peierls argument on minimal-filling walls proves the seed” **FAILS** as an inference. Failure of one upper-bound summation test neither proves divergence of the actual wall sum nor rules out sharper probabilities, restricted contours, or correlations. No theorem supplies a lower bound on all possible contour entropies or forbids such refinements. The quoted rho=0.33 is a finite-volume GUIDE measurement, not a proved lower bound for the required family of laws. Retain the explicit arithmetic obstruction to satisfying this particular FN-plus-geometric-majorant test, conditional on the relevant density, and remove the universal exclusion.

## Remaining exact statements and open claims

Step 2 F1 and F3 — **HOLDS**: coordinate-cut pairing detects H_1(T^3;Z_2); relative fillings exist; their difference is a cube-chain boundary unique up to complement. Identifying plaquettes with dual bonds gives the finite Ising ground-state interpretation, with cube flips as spin flips and free boundary. It supplies no low-temperature estimate for the induced disorder law.

Step 7.2, the Fourier/'t Hooft identities — **HOLDS**, with the actual temporal-layer convention of OS. Summing PAR against a character gives T(R). Vertex centre flips give invariance under coboundaries. The characters of the finite relative-cycle group then determine its law. For independent plaquette noise D, the character of its boundary is exactly `(1-2p)^{|dR|}`; the converse requires that identity for every character, including periods if working globally on a torus. The claimed ultraviolet self-energy estimate, typical Ising order, and cutoff-limit failure of this decoder are unproved inputs/heuristics, not consequences of Fourier inversion.

RIG — **FAILS as a completed proof**, not refuted as a theorem. The source explicitly stops before proving its alternative between one macroscopic wall and many small walls with the required joint probability. HC/PB alone do not prove that alternative or the asserted uniform tail `C g^3 2^{-c g^2}`. S1 and S2 are named open proposals; to imply SEED-DEC-U they must supply that quantitative tail, or another tail meeting its actual time, geometry and background quantifiers. Their present descriptions grant no seed. The low-spin/high-spin strategy claims likewise inherit the limitation already recorded in `gap-hs-check-astra.md:216-220`: a small marginal density does not exclude a cumulative or winding-conditioned mechanism. Order-one local caps alone do not rule out a much smaller block probability. The statements that every decoder's proved threshold lies in the Peierls range, or that no coarse electric construction can help, are unsupported general exclusions and are not used.

No finite-coupling selectivity theorem is supplied for U(1), Q_8 or 2T; no SU(2) seed is proved; no cutoff-uniform mass-gap or existence conclusion follows from this check. Numerical guides, the author's three refutation scripts, and recalled literature constants were not rerun or treated as proof. No status, registry, source note, FINISH row or remote ref is changed.

RESULT: HOLDS for the deterministic patching, hereditary 1/4 rule, T1, ratio-ten hierarchy, TOP and TOP+; HOLDS under CE for the same-class quadratic recursion with C_3=1,120,616, which escapes check 882's overlap/power-loss failure; HOLDS AFTER CORRECTION for the snake's scope, the level-zero rate claim, SEED-DEC-U's domain and the filling-Peierls barrier; HOLDS for frozen finite-group selectivity and PAR; FAILS for the universal typical-field-conditioning and all-Peierls exclusions, while RIG remains an unfinished proof and both seeds remain open. Research check only; no status granted.
