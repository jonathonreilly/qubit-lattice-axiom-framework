# Repo search

Research check of `library/gap-sep-opus.md`, FINISH row 869. Mathematical verdicts are recorded below; the original Ginibre source-reading obligation remains open.
Repository pin requested: `6a773245a`; source-account pin: `31a47c543775`.
No scientific or audit status is granted. Computational runs may guide or refute but do not discharge proof obligations.

The search record below was established before derivation. Verdicts were appended statement by statement.

## Search record and provenance

Checker: OpenAI / gpt-6-astra / xhigh, as dispatched. Author checked: Claude Opus 5.5 / max. Research text only; not an audit or a status grant. The requested lane HEAD is exactly `6a773245a6216a42e7df0c88006ad7d6c19a1c1b`. Only this report is edited. No proof computation or simulation is used.

`prior/gap-sep-check-astra.md` was absent. `prior/repo-search-2026-11-08.md` was read; its targets are earlier RG suppliers, not this check. FINISH row 869 contains no separate “Repo prior work” line. The `open-registry.md` search for `gap-sep|Ginibre|Borgs|one.slice|parity|Lemma QS|Theorem HS|Lemma DS` returned no match. E17 itself remains row 866's work; this report does not attack it.

The explicit full-repository location in the request was used for read-only Git searches. Refs searched, in order:

| Ref | Commit |
|---|---|
| origin/main | faeafffaf6f4335b889df68428e017795630fda3 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Search 1 used `quadruple suppression|Lemma QS|Proposition SEP|Borgs.Seiler|Ginibre|environment coefficient|parity.{0,35}(edge|Hooft)|one.slice law`, capped at 90 lines. It hit the cap within main, so supplies no absence claim. Search 2 narrowed this to `quadruple suppression|Lemma QS|Proposition SEP|Borgs.Seiler|one.slice law|Ginibre.{0,40}(cosine|inequal)|marked plaquette weight|Hooft.{0,25}(loop|twist)`, capped at 100 lines. It completed across all five refs. No QS, SEP, or Borgs–Seiler theorem/check was found under those terms.

Relevant hits, read at their actual source:

| Source | Exact statement and closeness |
|---|---|
| main, `docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md`, 90–143; the same discovery pointer occurs on all refs | Equations (3.3), (4.1) identify the environment coefficient with `E_full[conj(chi)/w]/(d E_full[1/w]) = E_deleted[conj(chi)]/d`. This is the existing deletion/importance-weight identity, in a finite SU(3) spatial model. Credit and reuse its method; it does not prove four-link suppression or identify a transfer compression. |
| main, `docs/POSITIVE_WILSON_VILLAIN_MIXTURE_AND_WEAK_REGION_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md`, 200–214 | For Haar angles and nonnegative cosine couplings, increasing any coupling increases every cosine-character mean. Its two-copy, covering-torus expansion makes the covariance a sum of squares. This supplies the exact monotonicity method needed by SEP(b), already in the repository. The application is checked below; original-source access is reported separately. |
| all refs, `docs/FINITE_CLOCK_GINIBRE_FREE_STATE_AND_STATIC_CHARGE_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md`, 4,17 | Character Ginibre inequalities give a free-boundary exhaustion limit for the supplied finite-clock Villain law. Related method, different measure and boundary conditions; it is not SEP(b). |
| pr/10114 and pr/10133, `.claude/science/toe-ruleset-20261021/agents/ym4d-existence/EXISTENCE.md`, 3622–3652 | For a primitive SU(N) twist, `W1 W2 = z W2 W1`; the other two holonomies lie in the centre, giving N² isolated flat gauge orbits. Marked ARGUED there. This is C4's existing construction after relabeling coordinates; it is credited, not a new construction here. |
| pr/10114 and pr/10133, `ym4d-proof/REVIEW_MASSGAP_2606_PRIMARY_ASTRA.md`, 41 | “Equal one-slice laws can belong to distinct positive transfer semigroups.” A distinct abstract warning, not the particular finite-temperature Wilson assertion T3. No theorem is imported from this search excerpt. |

The fractional-instanton and meron twist hits concern other supplied constructions. They do not state the QS bound, SEP comparison, or this finite-temperature test. Historical copies and review echoes are not independent results.

The SA-index README and chunk-02 rows 78–106 were read. Searches of all chunk files and `obligations.md` for `Bessel`, `GL3`, `GL8`, `Ginibre`, `Borgs`, `Hooft`, deleted plaquettes, half-integer spins, finite temperature, and thermal sums locate the existing convolution calculation, but not QS, SEP, or T3. Outline lines 2195–2243 prove GL3/GL4: `c_j = 2 exp(-beta) I_(2j+1)(beta)/beta`, hence `r_j = I_(2j+1)/I_1`, and the Bessel recurrence. Those are credited inputs from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The account search for the target names/method phrases found only unrelated plaquette-removal geometry in CA-II, not a supplier. This is a bounded search result, not an absence theorem. No Balaban theorem is needed for the statements checked here.

## 1. Lemma QS(i)–(iii), source lines 451–480 — HOLDS

The domain is a four-dimensional nearest-neighbour periodic cubical lattice, all periods at least three, beta nonnegative. The absolute environment estimate permits arbitrary signs eta_q in {+1,-1} on the remaining plaquette couplings.

Two perpendicular boundary links specify their square uniquely. Two parallel boundary links specify their intervening unit strip uniquely unless the transverse period is two. Thus every retained plaquette contains at most one of the four marked links. Conditional on the exterior links, the Wilson density factors into four separate Haar densities. This is conditional independence only; it asserts no unconditional independence.

Each link has six incident plaquettes. Removing the marked one leaves five unit-quaternion staples. Their signed sum has norm at most five. With `A_i = rho_i W_i`, the conditional representation mean is `r_j(beta rho_i) D^j(W_i^-1)`. An inverse-oriented link has its adjoint. Multiplying these four independent matrix means and taking the trace gives

`|E[chi_j(U_p) | exterior]| <= d_j product_i r_j(beta rho_i)`.

The cited row-843 Lemma 3.1 is valid: differentiating the tilted density gives `R_n'(s)=Var_s(t)>0`, and integration by parts gives `(2n+1) E(t)/s = E(1-t²)`. Thus the product of successive ratios, `r_j`, increases with s. Averaging proves the two QS inequalities. At rho_i=0 use Haar measure and the continuous values r_0(0)=1, r_j(0)=0 for j>0. The argument covers j=0 too.

This checks the new factor-four step. It reuses the existing Schur/Bessel calculation, rather than replacing it. No implication to E17 has been established by this lemma.

## 2. Continued fractions and fundamental constants, lines 495–511 — HOLDS

All terminating decimals below denote rationals. There is no numerical evaluation of a special function in this check. Put `R_n(x)=I_(n+1)(x)/I_n(x)`. GL4 gives

`R_n(x)=1/[2(n+1)/x+R_(n+1)(x)]`.

Row-843 Lemma 3.1(d) bounds R_n by the positive root U_n of `x u²+(2n+1)u-x=0`. To certify an upper seed q it suffices to check `x q²+(2n+1)q-x>=0`. To propagate, use the decreasing reciprocal map, keeping the sign of each bound.

The entire printed x=11.5 chain has the correct direction and outward rounding. The following table also supplies the two chains omitted from the author's text:

| x | upper R7 | lower R6 | upper R5 | lower R4 | upper R3 | lower R2 | upper R1 |
|---|---|---|---|---|---|---|---|
| 11.5 | .5418 | .5684 | .6204 | .6711 | .7317 | .7978 | .8729 |
| 12.5 | .5662 | .59304 | .64391 | .69256 | .75044 | .81271 | .8829 |
| 13 | .5776 | .6044 | .6547 | .70228 | .75893 | .81935 | .8873 |

The seed polynomial values, respectively, are `.00279326`, `.0002805`, `.00108288`, all positive. Each lower entry l satisfies `l[2(n+1)/x+u]<=1` using the preceding upper entry u. Each upper entry u satisfies `u[2(n+1)/x+l]>=1`. These are finite rational products with their factors displayed, so the table is a hand certificate. For example the final 11.5 test is `.8729(4/11.5+.7978)>1`; the final 12.5 and 13 tests are `.8829(.32+.81271)>1` and `.8873(4/13+.81935)>1`.

Squaring twice gives `.8729^4<.5806`, `.8829^4<.6077`, `.8873^4<.6199`. At x=2.3 the printed `.2992` upper seed for R3 has polynomial remainder `.000297472`; `.3438` is a valid lower R2, and `.4801` a valid upper R1. Thus the fundamental density ratio is at most `4(.4801)(.5806)=1.11498424<1.115`.

The parenthetic termwise proof of the recurrence is also correct: after shifting the second series, the coefficient is `(k+nu)-k=nu`, and its power is `(x/2)^(2k+nu-1)`.

## 3. QS-1 and QS-2, lines 481–493 — HOLDS AFTER CORRECTION

Both displayed probability bounds hold for the row-860 law, with spatial twists and positive timelike kinetic factors. Use periodic spatial distance in QS-2. The stated endpoint separation ensures that no retained plaquette couples links from two marked plaquettes. Together with QS(i), this makes all 4|S| marked links conditionally independent. Applying the conditional character bound to their product proves QS-2; QS-1 is its single-edge version.

There is a normalization error in the auxiliary partition identity inherited from row 860. If `Z_raw = integral product_q exp(beta eta_q x_q)` and `Z_raw,without S` literally deletes those exponential factors, then

`P(0_S) = z(beta)^|S| Z_raw,without S / Z_raw`,

not `Z_raw,without S/Z_raw`. Indeed Lemma OS replaces a marked `k_beta=exp(beta x)/z` by 1. Equivalently, define both partition functions using normalized plaquette factors k and then their ratio is exactly P(0_S). The normalized deleted law nu_S is unchanged by this constant convention. Consequently

`P(j_S)/P(0_S) = product_e[d_j r_j(beta)] E_nuS[product_e chi_j(U_p(e))]`

is correct, and the final inequalities need no numerical change. This corrects row 860's raw deleted-partition identities and the target's auxiliary deleted-partition wording in QS-2.

The phrase “every twist” must retain the law's domain: QS's absolute character estimate tolerates arbitrary signed plaquette weights, but the nonnegative one-slice probability in row 860 uses a spatial twist m and positive temporal weights. A general negative marked temporal weight would require the corresponding sign in its insertion formula and need not define that positive spectral law.

## 4. QS-4 and the all-half-integer density, lines 512–515, 566–570 — HOLDS AFTER CORRECTION

The final constants `.0160`, `6.6e-4`, and `1.177` are valid. Some intermediate bounds inherited from row 860 are rounded in the wrong direction. For x=12.5, the assertions `U_2<=.8198`, `U_4<=.7028`, and `U_5<=.6525` are false. Substitution into `x q²+(2n+1)q-x` gives negative values. Even the displayed rounded product `.8872*.8198*.7585*.7028` equals `.387718733180128`, not a number below `.3877`. This breaks that arithmetic certificate, not the final density bounds.

A short hand repair uses section 2 and valid root bounds `U_2(12.5)<.8199`, `U_4(12.5)<.7029`. Then

`r_2(12.5) <= .8829*.8199*.75044*.7029 < .382`,

`r_(5/2)(12.5) <= .382*.64391 < .246`.

For completeness, the two quoted sums admit a rational tail check. Put `b_n=(n+1)^2(5/4)^n/(n+1)!`, n=2j. The first five terms n=4,...,8 are bounded above by

`.508627, .152588, .037088, .007569, .001331`.

Their sum is `.707203`. Since `b_9<.000206` and `b_(n+1)/b_n=(5/4)(n+2)/(n+1)^2<=.1375<.14` for n>=9, the remaining sum is below `.00025`. Hence `sum_(n>=4)b_n<.70746`. For odd n>=5, use the first and second odd terms `.152588`, `.007569`; for odd n>=9 the two-step ratio is below `.018`. The rest is below `.000206/(1-.018)<.000210`. Thus the odd sum is below `.16037`.

With rho_0<=1, QS-1 now gives the stronger sufficient estimates

`P(j>=2) < .70746*.382^4 < .0160`,

`P(j half-integer, j>=5/2) < .16037*.246^4 < .00066`.

For the beta=2.3 all-half-integer ratio, the source's final number also survives. Valid bounds are

`r_(3/2)(2.3)<.0561`, `r_(3/2)(11.5)^4<.0688`.

For the latter use `R1<=.8729`, `R2<=.8018`, `R3<=.7317`. The subsidiary lower bound `R3>=.7256` claimed from U4 is rounded too far; replace it by `.7255`, using `U4(11.5)<.6826`. This still gives the stated upper R2=.8018.

Next, `r_(5/2)(11.5)<.5122*.6826*.6204<.217` and `36 r_(5/2)(2.3)<.101`, so this contribution is below `.000224`. For higher half-integers, `R6(11.5)<.5835`, `R7(11.5)<.5418` give `r_(7/2)(11.5)<.069`. The G3 sum over odd n>=7 at beta=2.3 is below `.005`: its first term is below `.004223` and its two-step ratio below `.023`. Its QS contribution is therefore below `.005*.069^4<.000001`. Consequently

`P(odd)/rho_0 < 1.11498424 + 16*.0561*.0688 + .000224 + .000001`

`=1.17696412 < 1.177`.

These proofs use small displayed rational inequalities and geometric tails only. The quoted simulation values and unprinted numerical checks supply no step.

## 5. Proposition TL, lines 536–548 — HOLDS AFTER CORRECTION

The partition-function identity holds. On each marked positive timelike plaquette, the absolutely convergent character series gives

`sum_j (-1)^(2j) d_j r_j chi_j(g)=k_beta(-g)`.

The ratio to k_beta(g) is exp(-2 beta x(g)). Insert this in Lemma OS on the finite set R and integrate. Thus the parity expectation is exactly `Z_m(flip R)/Z_m`. There is no deleted-weight normalization issue in this ratio. The same argument uses charge parity for U(1), and the eigenvalue of the central element -1 on an irrep for Q_8 and 2T.

The geometric description needs qualification. Let `Sigma_R` be the union, modulo two, of the *dual* plaquettes to p(e), e in R. The insertion is the disorder surface with boundary `partial Sigma_R`. That boundary may be several loops or a more general even lattice contour. A wrapping closed component has no loop boundary and records a global twist. Thus an arbitrary R is not necessarily one ordinary 't Hooft loop. For a contractible dual square surface, the usual boundary-loop identification is correct; for a full cocycle cut, the global twist identity is exactly row-860 P1. This is the precise correction to the title and to lines 546–548, 631–632.

The later perimeter/area-law assertions in lines 550–564 are not consequences of TL. They are addressed with T3 below.

## 6. The six candidates, lines 121–167 and 614–619

### C1, local environment coefficient — HOLDS AFTER CORRECTION

The candidate is well-defined, and QS supplies the stated uniform upper bound. A threshold below *proved* lower bounds in all specified comparison regimes would separate those regimes. The Monte Carlo points do not supply those lower bounds, an infimum over the Coulomb phase, or an implication to E17.

The assertion that e_F tends to one as beta tends to infinity is not a group discriminator by itself. On any fixed untwisted finite torus it holds for all four groups, including SU(2): the deleted action is maximized when every retained plaquette is one; the other five faces of an elementary cube then force the deleted face to be one. Compactness gives concentration on these maxima. This fixed-volume observation is not a uniform-volume phase theorem. The stated spin-wave asymptotic remains a heuristic in this report.

### C2, Haar moments — identities HOLDS; structural dismissal FAILS

The four moment formulas are correct. Weyl's formula gives the Catalan and central-binomial expressions. In Q_8 the real parts are +1,-1 and six zeros. In 2T they are +1,-1, six zeros and sixteen values of magnitude 1/2. These give the two finite-group expressions directly. The first discrepancies from SU(2) are at degree 4 for Q_8 and degree 6 for 2T. Thus source line 118's “up to degree 4, 6 agree” must mean *strictly below* those degrees.

The displayed moments already distinguish SU(2) from all three comparison groups. For example M1=1/4 distinguishes U(1); M2=1/8 distinguishes Q_8; M3=5/64 distinguishes 2T, whose M3=3/32. Matching one kinetic eigenvalue does not alter Haar moments. The asymptotic property `n^(3/2) M_n -> 1/sqrt(pi)` likewise distinguishes all three. Therefore “C2 fails as a structural separation because matching absorbs it” is not a valid deduction. The last-section concession about finite coupling does not repair that general dismissal. What remains absent is a theorem connecting this distinction to E17.

### C3, topology — HOLDS AFTER CORRECTION

`pi_1(SU(2))=0` and `pi_1(U(1))=Z` are the correct group-space facts. A finite discrete group also has trivial based fundamental group, so this invariant alone does not distinguish SU(2) from Q_8 or 2T. A nontrivial finite group is disconnected, however; it is not a simply connected *space* in the usual connected definition. Compactness plus connectedness plus simple connectivity does distinguish the listed groups. Neither version supplies a probability estimate.

Delete the unrestricted claim that finite-group “thin vortices” are Z_2-valued. General finite-gauge-group magnetic holonomy is labelled by conjugacy classes, not only by the centre: Q_8 already has the noncentral class {i,-i}. The Z_2 statement is correct only for centre flux. Likewise pi_1(SU(2))=0 excludes the indicated intrinsic group-winding charge; it does not exclude every integer monopole variable defined after a projection or extra field choice.

### C4, flat connections with one primitive twist — HOLDS

For the *sole* nonzero twist in the (0,3) plane, the existing T26 construction applies. An anticommuting SU(2) pair has zero scalar parts and orthogonal imaginary axes; up to conjugation take i and j. Its common centralizer is {+1,-1}, so the two other holonomies have four discrete choices. Without the twist, commuting SU(2) holonomies instead give the continuous `(S^1)^4/Z_2` family. The outline's flat-holonomy discussion at 8733–8761, located through chunk-08 rows 43–46, already retains these commuting holonomies.

U(1) cannot have an anticommuting pair, whereas Q_8 and 2T contain i,j. The comparison thus does not exclude those finite groups. The quoted beta*pi²/2 is the large-side classical action of uniformly spread U(1) flux on a hypercube, not an established finite-coupling partition-function asymptotic. With side L its classical uniform-flux cost is `beta L^4[1-cos(pi/L²)]`, tending to that value. No quantum free-energy conclusion is imported.

### C5, conserved central flux — HOLDS

For SU(2), the central character is (-1)^(2j). For U(1), the signed sum of integer edge charges through a closed cut is conserved: plaquette multiplication adds boundaries with zero intersection against the cut. Q_8 and 2T both have centre {+1,-1}. These facts support the stated comparison of *central* flux. They provide no suppression estimate for the nontrivial sector.

### C6, surface weight — HOLDS AFTER CORRECTION

For a closed **orientable, nonsingular** plaquette surface of constant representation, Schur integration gives `r_j^F d_j^(V-E+F)`. Thus the torus, sphere, and handle comparisons in C6 are correct in that domain, after factoring out the common r^F and summing the two U(1) orientations where appropriate. The same Schur argument applies to the two-dimensional irreducible representation of Q_8 and 2T.

“Closed non-branching” alone does not state this domain. Nonorientable surfaces require Frobenius–Schur factors; pinched vertices require counting their separate index loops. This is already addressed by `gap-means-max.md:74–96`, Proposition NS and its explicit projective-plane construction, credited to its author. Its elementary identity `integral D_(1/2)(g)^2 dg = -I/2` follows from `chi_(1/2)(g²)=4x(g)²-2` and M1=1/4. Thus the omitted sign is not licensed by the Schur formula used in C6. The earlier construction is not re-enumerated or newly certified here; the orientable restriction is enough for C6's actual torus/sphere comparison.

### “No single candidate passes both tests” — FAILS as a classification theorem

C2's exact moment sequence is a direct counterexample to the claimed algebraic classification. C3 also mixes trivial fundamental group with connected simple connectivity. The valid, weaker conclusion is that none of the arguments supplied here turns its distinguishing property into E17. A group discriminator and a sufficient confinement estimate are different statements. This check excludes no future use of C1–C6, singly or together.

## 7. Proposition SEP, lines 594–612 — HOLDS AFTER CORRECTION

Part (a) follows from QS and section 2. Part (b)'s mathematical argument is valid for untwisted finite U(1) Wilson tori, all periods at least three, beta>=6. Its quoted separation is at least **.0359**, not a rigorous lower margin .036.

The required monotonicity already has a complete repository proof, cited in the search record. Here is its exact application check. For integer characters a,b,m and Haar theta on the link torus, put `H(theta)=sum_m J_m cos(m.theta)`, J_m>=0. In the doubled covariance integral make the surjective torus change `(theta,theta')=(v-u,v+u)`. Haar measure pushes forward to Haar measure. Expanding `exp[2 sum_m J_m cos(m.u)cos(m.v)]` yields

`2 Z² Cov(cos(a.theta),cos(b.theta))`

`=4 sum_(n_m>=0) [product_m (2J_m)^n_m/n_m!] [integral sin(a.u) sin(b.u) product_m cos(m.u)^n_m du]^2 >=0`.

All expansions are absolutely convergent in finite volume. Differentiating a cosine mean in J_b therefore gives a nonnegative derivative. Plaquette boundaries are integer characters of the link torus, so multi-link plaquette interactions satisfy exactly these hypotheses. Nonnegative signs, rather than pairwise spin interactions, are what matters. This checks the existing Ginibre-method proof against SEP's use; it is not an assertion that a non-Abelian analogue holds.

Set to zero all couplings except the five faces of one elementary cube other than p. The cube is embedded when periods>=3. Its six oriented face angles have one relation, their sum zero. The other five are independent Haar coordinates before weighting: gauge-fix a cube spanning tree, or peel the five-face disk, eliminating one new boundary edge per face. Each eliminated edge sets one face angle with coefficient +1 or -1, so this map is surjective with Haar pushforward. The five remaining factors are independent `exp(beta cos theta)` densities. The missing face is their signed sum, giving exactly `(I_1(beta)/I_0(beta))^5`. Monotonicity transfers this lower bound to nu_p in the full torus.

The source's x=6 chain is valid: upper R3=.5744, lower R2=.6351, upper R1=.7682, lower R0=.9078. Its seed polynomial has positive remainder .00041216. Each reciprocal step has outward rounding. Squaring twice and multiplying once gives `.9078^5>.6165`. Monotonicity of R0 follows from the tilted-circle variance identity. Thus SEP(b) is proved without a computational step and without a recalled, unverified inequality as a premise.

**Original-source access remains incomplete at this checkpoint.** Ginibre's bibliographic primary source is [General formulation of Griffiths' inequalities, CMP 16 (1970), 310–328](https://doi.org/10.1007/BF01646537). Its publisher abstract was read, but the article is paywalled. The [Project Euclid record](https://projecteuclid.org/euclid.cmp/1103842172) presents a bot barrier; that path was stopped. Other public-archive searches did not return the original full text. The 1969 APS predecessor's full-text endpoint returned 401. No original Ginibre theorem/page is claimed as read. The direct proof above settles the mathematical use, but does not satisfy the separate requested reading of the original paper. An accessible primary link has been requested while the rest of the check continues.

## 8. Finding FT, T3, and their claimed bearing, lines 344–449, 550–591 — FAILS

### What Borgs–Seiler actually supplies

Primary text read: Christian Borgs and Erhard Seiler, [CMP 91 (1983), 329–380](https://doi.org/10.1007/BF01208780), using the openly readable [full-paper transcription](https://www.academia.edu/61871779/Lattice_Yang_Mills_theory_at_nonzero_temperature_and_the_confinement_problem). Relevant passages: section II.3, pp. 337–342, especially (II.46)–(II.50); section III.2, pp. 348–354, Lemma III.6 and Theorem III.7; section IV, pp. 357–359. The transcription loses some displayed formula glyphs; no missing numerical threshold is reconstructed from memory.

Their result gives Polyakov long-range order at sufficiently weak coupling for fixed positive temperature in at least three spatial dimensions. Their string-tension comparison is `sigma_'tH <= sigma_P`, where sigma_'tH is an **electric-flux** free-energy-per-length limit. It implies vanishing of that string tension in their deconfined regime. It is not the asserted positive **magnetic-twist interface tension**, nor a proof of `Z_twist/Z -> 0` on the shapes used here. The paper does not establish the claimed Wilson beta=2.3, N_t=3 threshold or equality of local slice laws. The finite-temperature existence theorem is legitimate background; T3 as stated does not follow from it.

### The N_t=3 GUIDE sampler has an invalid update partition

GUIDE867b uses `idx=sum(coordinates)%2` and updates every link of a chosen direction and colour simultaneously, with staples computed before that update. This partition is independent only when every relevant transverse periodic cycle is even. At L_t=3, the spatial links `(t=0,x; i)` and `(t=2,x; i)` have the same colour but occur together in the timelike plaquette across the periodic seam. They are coupled and are not a conditional-independent update block.

This is a mathematical defect, detectable without running the code. Take i=1, so temporal links are updated first and the offending spatial links next. After the simultaneous update, each link's conditional fundamental matrix mean has norm at most `r_(1/2)(6 beta)=O(beta)`. The two new random draws are independent given the old configuration, hence the seam-plaquette mean is O(beta²). Later direction updates do not touch this plaquette. In the true finite-volume Wilson law, expansion at beta=0 gives instead

`E_beta[x_p] = beta integral x_p² dHaar + O(beta²) = beta/4 + O(beta²)`.

Other distinct plaquettes have zero cross integral with x_p, since each has an unpaired Haar link. Therefore this full-sweep kernel does not preserve the Wilson law in general. This proves an algorithm defect; it does not compute the bias at beta=2.3. The N_t=3 rows cannot support Finding FT. The even-period rows do not have this particular seam defect, but none of these runs discharges a theorem.

### The logical inference fails independently of the sampler

1. Two close scalar means, e_F and P(odd), are not equality or a distance bound for the law of every bounded edge set. No metric on laws, joint-event comparison, or uniform error estimate is supplied. Approximate agreement does not ensure that an arbitrary proposed inequality has the same truth value.

2. The fixed-temperature limit and the E17 limit differ. The actual E17 text was read at `gap-expose-astra.md:575–599`: time t=a, spatial sides (a,c,d), with a growing in `C a^p eta_*^(a/2)`. Even a proof that p tends to 1/2 as c,d grow at a=3 would not refute it. For every finite a0, a finite prefactor C can make the right side at least 1/2 for all `3<=a<=a0`. Since p<=1/2 in this positive twist-ratio setting, those sizes then impose no obstruction. A step valid at every t can still feed a proof that uses sufficiently large a or iteration over growing supports. It need not itself fail at t=3.

3. The cited many-layer theorem takes a spatial thermodynamic limit in d>=3. The proposed `(3,3,c,d)` family fixes one spatial period as well as time. Its asserted ordered phase does not follow by substituting that shape into the stated theorem. A separate shape-specific argument would be needed.

4. Even a deconfinement assertion or zero electric string tension is weaker than a quantified area cost for the magnetic twist. TL identifies which partition ratio needs control; it does not supply that control or its limit 0. The area/perimeter laws at lines 550–555 remain physical expectations here.

5. “SU(2) confines at every beta” in line 580 is an unproved premise in this setting. It cannot establish that the candidate threshold is unnecessary. Nor has the report ruled out local estimates as ingredients of a multiscale proof.

**Correct replacement:** short-period thermal states are a useful proposed comparison. QS is uniform in t>=3 and alone supplies no proved large-surface parity estimate. A shape-sensitive continuation may use such local bounds, but no necessity theorem about its form has been obtained. The existing SEED-FP contract is indeed shape-specific; this is read from `gap-finishline-opus.md:113–121`, not inferred as the only possible route.

## 9. Coverage, limits, and disposition

The entire 683-line author file was read, including both embedded scripts. The requested statements were checked line by line by Codex. The four-link argument and the printed 11.5 continued fraction have no failing step. Corrections and failures are recorded at the individual statements above. No source text, registry, audit record, FINISH row, branch, or remote was changed.

| Statement | Verdict |
|---|---|
| QS(i)–(iii), conditional independence and fourth-power character bound | HOLDS |
| Continued-fraction chain, .8729 and the fundamental upper bounds | HOLDS |
| QS-1/QS-2 probability bounds | HOLDS AFTER CORRECTION of the auxiliary raw partition normalization |
| QS-4 and the 1.177 odd-density bound | HOLDS AFTER CORRECTION of intermediate rounding; final constants survive |
| TL partition identity and geometric interpretation | HOLDS AFTER CORRECTION: a dual disorder surface, possibly multiple boundaries or a closed global twist |
| C1 candidate comparison | HOLDS AFTER CORRECTION: specified finite-volume/empirical claims only |
| C2 exact moments | HOLDS |
| C2 dismissal and exhaustive six-candidate classification | FAILS |
| C3 topology/vortex claims | HOLDS AFTER CORRECTION to the stated group-winding or centre-flux invariant |
| C4 sole primitive twist, C5 central flux | HOLDS |
| C6 surface weights | HOLDS AFTER CORRECTION to orientable nonsingular surfaces |
| SEP(a),(b) | HOLDS AFTER CORRECTION of the certified margin to .0359; direct monotonicity proof supplied |
| N_t=3 sampling evidence and equality of one-slice laws | FAILS |
| T3 as stated, including the Borgs–Seiler attribution and necessity claim | FAILS |

GUIDE867's even-period data were not rerun or statistically validated. They remain unverified exploratory numbers. GUIDE867b's odd-period runs have the explicit sampler defect above. The quoted critical couplings and general confinement/area-law claims have not been promoted to theorems. No computer-assisted proof, simulation, enumeration, or special-function evaluation was run. Shell commands served reading, search, file writing, and bookkeeping only.

One requested source-reading obligation remains open: the original full Ginibre paper was not accessible through the attempted public sources. This is an access limitation, not a mathematical failure of SEP(b). The primary Borgs–Seiler text was read, with the stated transcription limitation. No reply supplying another Ginibre link has been received at this checkpoint.

The output is local and uncommitted at the requested lane path. The managed sandbox makes .git read-only; no commit or push was attempted. E17, the improved typical-value bound, and shape-sensitive continuation keep their existing owners and remain open. No status is granted.

RESULT: PARTIAL CHECK — QS and its final probability constants hold after the recorded normalization/arithmetic repairs; TL holds with the dual-surface qualification; SEP(b) holds by the checked direct monotonicity argument with certified separation .0359. The six-candidate exclusion and T3 as stated FAIL, including an invalid N_t=3 sampler and a limit/observable mismatch in the Borgs–Seiler use. E17 is untouched. The requested reading of Ginibre's original full text remains incomplete because access failed; no scientific or audit status is granted.
