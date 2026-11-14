# Repo search

Terms: `WALL.?_?40|gap-wall|KURT|jump fraction|fusion of two flux|partial centre flips|partial center flips`; then `ground.state transform|flux ground|hidden.bit|sector.trace.domination`; scoped follow-up `ground.state transform|flux ground|hidden.bit|kurtosis|sector.trace|trace.domination` on the soft-route and research/ym4d paths. Commands used bounded `git grep -n -i -E ... -- '*.md' '*.tex' | head` in `/Users/jonreilly/Projects/Physics`. The broad trace/sector query hit its cap with unrelated material; it supplies no absence claim.

| Ref | Revision searched |
|---|---|
| origin/main | 993f5e4f6d11a7e20a1cab9612c5749a53bae073 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Relevant hits and proximity:

- `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_CONSTRUCTION_ASTRA.md:163–200` defines the ground-state transform with stationary measure `psi_0^2 dU` and proves `lambda/lambda_0 <= 1-exp(-2 beta n_s)` at fixed finite volume. The same search hit occurs on pr/10133. This supplies the earlier construction and finite-volume spectral separation, not a kurtosis floor or a two-flux-level bound. Credit that earlier Codex derivation; do not count its construction again.
- `docs/CLOSURE_T2_M1_M2_DISTINGUISHER_NOTE_2026-05-10_t2m1m2.md:48,72` on all five refs concerns excess kurtoses `-6/7` and `-1` of Beta laws. It is a different object. `pr/10134:.../parts/witness.md:535` gives `E|psi|^4-(5/3)(E|psi|^2)^2=(5/3)delta^4` for a Gaussian colour vector plus a Gaussian cross product. It is not a transfer eigenfunction estimate. Neither is used.
- Inside this lane, `gap-kurt-max.md:193–244` already gives (S), the moment hierarchy and the discrete kurtosis-energy inequality. `gap-crux-core-max.md:384–402,475–477` supplies Lemma R, the two distinct WALL formulations and the consumer. Those are inputs checked where used below, not new discoveries.
- `gap-brainstorm2-max.md:489–496` already explains sector-trace domination; its source is `gap-loop-eq-opus.md:202–206`, FINISH row 754. `gap-es1-opus.md:30–44` supplies the class and normalized-sector notation; it is not row 754. The trace step is checked below with K′.

No hit of the target wall/fusion statements appeared in the completed first search. The scoped method search returned only the earlier ground-state construction. A broader method hit, `origin/main:docs/COMPACT_ROTOR_SPATIAL_GROUND_PATH_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md:24–40`, gives the reversible generator `L=(g^2/2)Delta+g^2 grad(log psi)·grad` for a supplied compact-rotor Hamiltonian; it is a continuous-time construction for a different dynamics and supplies no wall bound. This is a search result, not an absence theorem. `prior/gap-wall-check-astra.md` does not exist. The November 8 prior-work digest concerns different RG targets; it supplies no completed check of row 894. The registry has no wall/kurtosis/check-row owner match. Saved bounded search captures are in `/tmp/ym4d-gap-wall-check-astra-20261113/search-captures.json`; entries marked truncated remain discovery-only. This task checks the assigned row; it starts no attack on another row's open supplier.

The SA index README, matching chunk-02 rows 88–104 and neighbouring rows, and obligations searches were used first. Searches for kurtosis, flux sector, centre/center flip, jump fraction and partial flip found no matching obligation. The transfer match leads to outline lines 2195–2245 and 2313–2338: (GL3) gives positive Bessel convolution coefficients; (GL8) gives a positive trace-class gauge-averaged transfer operator and its partition-function trace. These are existing constructions, not the requested wall statements. Source revision `31a47c543775` is as supplied by the task; the source directory has no Git metadata. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. No Balaban estimate is used; Tadeusz Balaban's work is not re-derived here.

## Scope and checkpoint

Codex, gpt-6-astra, xhigh; 2026-11-13. Check of Claude Fable 5.2 max's row 894 at checkout `3ea473483ca0edd9ed47e941476291ca09748676`. Research text, not an audit; no standing is granted. The user-requested verdict vocabulary and output path govern this report. Only this file is changed. No numerical run, machine enumeration or computer-assisted proof is used. The GUIDE runs and physical phase identifications are not premises.

Complete: all requested statements have verdicts below, appended as each check finished. The 4D SH-box kurtosis supplier is outside this check and remains open. Source SHA-256: `2a681ea78437f8044338f7c74e022d20dd99167ac419d486af3e516dbd17f2e7`; source bytes match pinned HEAD. The next decision is source-side correction by the row owner, not another proof attack here.

Throughout, the symmetry character is real of order two, the measure is invariant, and P commutes with the symmetry. P is a reversible Markov contraction with nonnegative spectrum. The inherited (S) has bounded g; finite fourth moments suffice for the displayed moment identities. A general strictly positive measurable kernel has a simple stationary vector but need not have a spectral gap. Where rho<1 or ordered eigenvalues are used, retain finite-volume compactness (or state these hypotheses explicitly). The Wilson finite-volume construction supplies them; simplicity alone, asserted at source Step 8.1, does not.

## Proposition D — HOLDS

Source §3.2. Interpret WALL as the displayed minimum form. Set v=kappa-1 and d=1-theta^2>0. Conditional variance gives `P(g^2)>=theta^2 g^2`; hence

    (1-rho)v <= <h,(I-P)h> <= kappa d.

If v>=1 the minimum inequality holds. If 0<v<1, it would require `v >= (a/M)kappa d >= [a(1-rho)/M]v>v`. If v=0 it requires `0 >= (a/M)d>0`. This proves both directions, including kappa=1 and kappa=2.

The older conditional formulation “if kappa<=2, then ...” excludes kappa=2 under these hypotheses. It is equivalent to kappa>2, whereas the minimum form is equivalent to kappa>=2. Do not transfer the strict conclusion of row 892's Proposition W to the minimum form.

## Corollary D1 — HOLDS

Source lines 107–109. The decimals in the source are approximations, not equalities. Here is a hand bound with enough slack for all downstream constants. Put `c=16 log 160`. From `rho^a<=160^(-16)` and monotonicity of `a(1-exp(-c/a))`,

    A=a(1-rho) >= 82(1-exp(-c/82)).

Use `log x=2 sum_{j>=0} t^(2j+1)/(2j+1)`, `t=(x-1)/(x+1)`. Four positive terms at t=1/3 give `log 2>6931/10000`; two at t=1/9 give `log(5/4)>223/1000`. Thus `log160=7 log2+log(5/4)>50747/10000`, and `c/82>99/100`. Also

    exp(99/100) > (1-1/100) sum_{j=0}^6 1/j!
                 = 193743/72000 > 1025/381,

where the last cross multiplication is `73816083>73800000`. Therefore

    A > 82(1-381/1025)=1288/25=51.52>51.5.

The derivative used for monotonicity is `1-(1+x)exp(-x)>=0`, since `exp(x)>=1+x`. No numerical evaluation is needed. Proposition D now applies with M=40. The claim for every fixed M<81.2 at sufficiently large a also follows, since the limit is `16 log160>81.2`: the same four- and two-term sums give `log2>0.69313`, `log(5/4)>0.22313`, hence `log160>5.07504`.

## Corollary D2 — HOLDS AFTER CORRECTION

Source lines 111–112. Specify `0<t_0<1`. The displayed general inequality holds:

    (kappa-1)/kappa <= (1-theta^2)/(1-rho)
                    <= 2 log(1/t_0)/A.

It gives a finite upper bound on kappa only when its right side is below 1. The printed `1.205` does not follow by rounding the bound with denominator 51.5: `1/(1-2 log80/51.5)>1.205`. Repair the proof using the stronger hand bound `A>51.52` just established; the claimed numerical conclusion then holds.

For explicit logarithm upper bounds, truncate the same positive series after m terms and bound its tail by `2 t^(2m+1)/((2m+1)(1-t^2))`. With m=4 at t=1/3 and m=2 at t=1/9 this gives `log2<0.69315`, `log(5/4)<0.22315`. Consequently `log20<2.99575` and `log80<4.38205`. Direct rational comparisons give

    5.9915/51.52 < 33/283,    8.7641/51.52 < 41/241.

Thus `kappa<283/250=1.132` and `kappa<241/200=1.205`, respectively. Keep 1.132 in the later prose: replacing it by `kappa<=1.13` is not a valid rounding.

## Theorem A1 — HOLDS

Source lines 159–162. Work with the symmetric stationary two-point law `nu(dx)P^n(x,dy)`. Set `u=g(x)`, `v=g(y)`, and `C=E[u^2 v^2]`. Stationarity gives `E[u^4]=E[v^4]=kappa`; conditioning and reversibility give `E[u^3v]=E[uv^3]=theta^n kappa`. Thus

    E[(v-u)^4]=2kappa-8theta^n kappa+6C,
    <h,(I-P^n)h>=kappa-C.

Eliminating C gives exactly A1. This also independently checks the sign and the factors 4/3 and 1/6. For an exact sign bit, the mismatch probability is `(1-theta^n)/2`; its fourth increment moment is `8(1-theta^n)`, so both sides of A1 vanish. This is a hand test, not a run.

## Corollary A2 — HOLDS AFTER CORRECTION

Source lines 164–175. Parts (a)–(c) have the stated constants. Require `kappa>1` for the formulas containing `lambda_bar_n`, as in the preceding notation; treat `kappa=1` separately. Also retain `rho<1` for the displayed division by `1-rho^n`. In the compact finite-volume setting these conditions cause no ambiguity.

A1 gives `1-J_n=3 D_n/[4kappa(1-theta^n)]`, where `D_n=<h,(I-P^n)h>`. The bounds `(1-rho^n)(kappa-1)<=D_n<=kappa-1` prove (a), (b) and the bounds on W in (c). At kappa=1, A1 gives J_n=1 and W=0; conversely J_n=1 forces h=0. The latter also follows directly from strict positivity and the vanishing Dirichlet form, without asserting that simplicity implies rho<1.

The geometric sum gives

    c_n=(1+theta+...+theta^(n-1))/(1+theta),
    n theta^(n-1)/2 <= c_n <= n/(1+theta).

**Correction to the three-face equivalence:** W1, W2 and W3 are equivalent only on `kappa>1`. At kappa=1 the undivided W2 reads `0<=0`, while W1 is false. On kappa>1, division of W2 by `||h||^2` gives precisely `lambda_bar_1 <= 4(1-J_1)M/[3(1+theta)a]`; substitution into (c) proves both implications. W3 follows by the same substitution for every positive integer n. The phrases “duration of a flip” and “share of flips still in progress” are interpretations, not identities of event probabilities proved by A2.

## Corollary A3 — HOLDS AFTER CORRECTION

Source lines 177–178. Its general statement holds: `1-J_n>=eps>0` excludes kappa=1, and A2 gives `W >= (4/3)c_n eps >= (2/3)eps n theta^(n-1)`. The displayed M therefore suffices, including when the minimum has saturated at 1.

The numerical specialization needs `8 divides a`, since n is an integer number of lattice steps. Merely assuming a even and a>=82 does not define n=a/8. Correct text: “If 8 divides a, take n=a/8, eps=1/2 and theta^(n-1)>=3/5; then W>=a/40.” For other a, choose an integer n and retain the general bound on M; no unchanged constant 40 follows just by rounding n down.

## Lemma B4 — HOLDS

Source lines 242–245. Let `m=E[g^2 f^2]`, `e=gf` and `D=<f^2,Pg^2>`. The product e is invariant and mean zero. Directly symmetrizing the stationary edge law gives

    <e,Pe> = theta_2 m - (1/2)E[(g_1-g_0)^2 f_0 f_1]
           >= (theta+theta_2-1/2)m - D/2.

The inequality uses `f_0 f_1 <= (f_0^2+f_1^2)/2` and exchange of times; it does not require f to have a fixed sign. Combining with `<e,Pe><=rho m` gives (a).

Write `E_P(u,v)=<u,(I-P)v>`. Since `D=m-E_P(h_f,h_g)`, part (a) becomes

    (theta+theta_2-rho-1)m <= -E_P(h_f,h_g)/2.

The nonnegative Dirichlet form satisfies Cauchy–Schwarz. Conditional variance gives `E_P(h_f,h_f)<=kappa_f(1-theta_2^2)` and the analogous bound for g. These prove the first inequality in (b). Finally `m=1+<h_f,h_g> >= 1-sqrt((kappa_f-1)(kappa_g-1))`. All products are integrable under the stated fourth-moment hypotheses. No top-level property of f is used.

## Corollary B4′ — HOLDS

Source lines 247–249, in the finite-volume spectral setting. Multiplication `M_g` is an isometric involution because g^2=1. It interchanges the invariant and chi sectors. For the positive kernel `F(x,dy)=P(x,dy)1_{g(x)!=g(y)}`,

    M_g P M_g=P-2F,    F1=(1-theta)/2.

Detailed balance and `2|u(x)u(y)|<=|u(x)|^2+|u(y)|^2` show `|<u,Fu>| <= [(1-theta)/2]||u||^2`. Thus the restrictions of P and M_g P M_g to the invariant sector differ in norm by at most 1-theta. The min-max principle gives the ordered-eigenvalue bound, including `theta_2<=rho+1-theta`. Count multiplicities, and pad finite-rank spectra with zeros if needed. Without compactness, formulate the norm comparison rather than an unstated discrete enumeration.

This says “within 1-theta”, not exact equality of spectra. It applies to an **exact** bit only. B4 does not extend this unitary spectral correspondence to a merely small fourth-moment defect.

## Proposition B5 — HOLDS

Source lines 251–252. Take `rho<1` and `0<=theta_2<=theta<1`. Set `x=(1-theta^2)/(1-rho)` and define x_2 likewise. Conditional variance, applied to each eigenfunction, gives `kappa_j<=1/(1-x_j)` when x_j<1. Therefore the two quantities in B4(b) obey

    E[g^2f^2]>=1-c,
    sqrt(kappa_g kappa_f(1-theta^2)(1-theta_2^2))<=(1-rho)c.

Crucially, `c<1` is equivalent to `x+x_2<1`. The coefficient being multiplied is positive. Using `1-theta_j<=1-theta_j^2`, B4(b) gives exactly `(1-x-x_2)(1-c)<=c/2`.

If both x_j<=t<1/2, monotonicity in each variable implies `(1-2t)^2<=t/2`. Its smaller root is `(9-sqrt(17))/16`. At the rational `t=381/1250=0.3048`, the left side minus the right side is `19/1562500>0`. Thus two levels cannot both have x_j<=0.3048, a little stronger than the stated 0.30 claim. No decimal root evaluation or enumeration is used.

## Corollary B6 — HOLDS AFTER CORRECTION

Source lines 254–259, including the author's correction at 259. The rigorous conclusion is the first sentence, counting eigenvalues with multiplicity. Remove the false equality `exp(-7.85)=1/2560`. Both thresholds work, but they differ.

For the stronger threshold `theta_k^a>exp(-157/20)`, use the sharpened D1 bound A>51.52:

    x_k < (157/10)/(1288/25)=785/2576 < 381/1250,

where `981250<981456`. B5 proves that there is at most one such eigenvalue per sector. In particular this holds above 1/2560: the preceding logarithm bounds give `log2560=11log2+log(5/4)<7.8478<7.85`. The original proof's `15.7/51.5<0.3048` is false; the corrected denominator fixes it. Alternatively the weaker rational threshold follows directly from the upper bound on log2560 with denominator 51.5.

The second sentence has no quantified bound as written (“about”, followed by an ellipsis). Delete it as the author does at line 259, retaining B4(b)/B5 as the actual pairwise estimates. The corrected trial-vector test at line 259 follows from min-max on `span{g,phi}` and B5; its use requires the top level itself to satisfy x<0.3048.

### Claimed identification of the B6 scenario — FAILS

Source lines 256, 333–343 and the final RESULT go beyond B6. “At most one light level per sector” does not assert that all seven nonzero sectors have a light level. B4′ requires g^2=1; D2 gives only a small nonzero variance. B4 supplies one overlap inequality, not a unitary correspondence of the whole near-bit spectrum. Therefore “eight vacua”, “the rest of the sector a copy of the even sector”, and equivalence with a Z_2 topological phase do not follow. Correct consequence: **any sector with theta^a>=1/20 has kappa<1.132 and has no second level above the B6 threshold.** No thermodynamic phase, degeneracy across sectors, or converse is established. Also exclusion of kappa<1.132 is not equivalent to the stronger demanded floor kappa>=1.66 or kappa>=2.

## Corollary K′ and its trace input — HOLDS AFTER CORRECTION

Source lines 298–306. Correct the attribution: row 754 is `gap-loop-eq-opus.md`, Corollary 6.3, lines 202–206. `gap-es1-opus.md:30–44` defines the class and p_z; it is a distinct note. The sharpening `Theta_chi<=1+S_ev(a/2)` is written explicitly in `gap-brainstorm2-max.md:489–496`.

Here is the complete trace argument with its hypotheses. Write `Z_chi(t)=Tr(T^t P_chi)`, `Z_0(t)=lambda_0^t(1+S_ev(t))`, and `p_chi=Z_chi/Z_0`. For the periodic Wilson transfer, the electric-twisted traces `Z^e(t)` are nonnegative partition integrals. Fourier projection on the finite centre group gives

    0<=Z_chi(t)=|Gamma|^(-1) sum_e chi(e) Z^e(t)
       <=|Gamma|^(-1) sum_e Z^e(t)=Z_0(t).

This extra trace input is not a consequence of an arbitrary abstract (S+) alone. For a even and a/2>=3, nonnegative sector eigenvalue ratios r_j<=theta give

    p_chi(a) <= sum_j r_j^a
               <= theta^(a/2) sum_j r_j^(a/2)
               <= theta^(a/2)(1+S_ev(a/2)).

Lemma R and `1-theta >= (1-theta^2)/2` now prove the displayed K′ bound with exponent `-A(kappa-1)/(4kappa)`. This includes kappa=1, though then it supplies no suppression. No trial-function assumption from the rest of Corollary 6.3 is imported.

Under the stated GLUE, kappa>=83/50=1.66 gives `(kappa-1)/kappa>=33/83`. Using just A>=51.5, the exponent is at least `3399/664>51/10`. The logarithm bounds above give `log160=7log2+log(5/4)<5.0752<5.1`. Thus `2 exp[-A(kappa-1)/(4kappa)]<1/80` by hand. Summing the four relevant normalized sector terms, as in `gap-crux-core-max.md:389`, gives Q_0<=1/20. This checks that conditional consumer bound, not the subsequent SH theorem or its physical applicability.

Correct the general threshold sentence to require `A>4log160` (and the same prefactor bound `S_ev(a/2)<=1`):

    Var(g^2) >= 4log160/(A-4log160).

Without the restriction on A, a negative right side would incorrectly make the criterion vacuous. Both printed sufficient decimals are safe: `log160<5.076` gives

    4log160/(200-4log160) < 20.304/179.696 < 0.113,
    4log160/(1000-4log160) < 20.304/979.696 < 0.021.

These are rational comparisons. The central sufficient value 1.66 is unchanged.

## B1: partial-flip splitting — HOLDS AFTER CORRECTION

Source lines 189–197; half-flip claim also at 257 and 338. Choose a direction i for which `chi(C_i)=-1`. This is required by (4); a nonzero sector need not be odd in every direction.

1. Haar invariance makes every V_Sigma a unitary involution. Centrality of -1 gives commutation with gauge averaging and the kinetic convolutions. The subset symmetric-difference law is exact.
2. A spatial plaquette changes sign exactly when its two cut-crossing links lie on opposite sides of Sigma. Thus `V_Sigma B V_Sigma=B exp(-2beta sum_{p in dSigma}x_p)`. Commutation with K^(1/2), and `-1<=x_p<=1`, prove the two operator inequalities as quadratic-form inequalities. The geometric boundary/perimeter statement applies to an actual region Sigma; an arbitrary scattered subset has its own, possibly much larger, boundary.
3. The finite Fourier projectors Pi_A are mutually orthogonal: summing the subset characters gives `Pi_A Pi_B=delta_AB Pi_A` and `sum_A Pi_A=I`. Their squared norms sum to one. The full cut acts by `(-1)^|A|`, proving the parity-support assertion. This is Haar-Hilbert-space algebra, not independence under the vacuum law.
4. With the direction chosen above, `C^R=C_i C^L`. Substitution into `(g-g o C^L)/2` and `(g+g o C^L)/2` gives all four claimed parities and their exact sum g. No measure invariance under partial flips is required for this algebraic decomposition.

**Half-flip correction.** Exact orthogonality of `V_L Psi` and Psi requires choosing Psi to be an eigenvector of the half-box translation tau that interchanges L and R. Then

    <Psi,V_L Psi>=<tau Psi,V_R tau Psi>
                 =<Psi,C_i V_L Psi>=-<Psi,V_L Psi>.

Such a choice can be made within a sector eigenspace because tau commutes with T, but it is not a property of every vector in a degenerate eigenspace. State the choice. The perimeter Rayleigh bound then follows from (2).

### Two extra inferences after B1 — FAILS

The pointwise multiplier D describes the **magnetic factor's** change, not the exact change of the vacuum law. For `nu=Omega^2 dU`, its partial-flip density ratio is `Omega(C^Sigma U)^2/Omega(U)^2`. No identity equating this ratio with D is proved or follows from (2).

Even partial-flip invariance and singleton Fourier support do not imply the quoted kurtosis lower bound. Hand counterexample: let I be uniform on {1,2}, and s_1,s_2 independent symmetric signs, independent of I. Let the two flips change the respective signs, and set `g=1_{I=1}s_1+1_{I=2}s_2`. The law is invariant, g has only singleton Fourier components, both component L2 masses are 1/2, and `g^2=1`. Hence kappa=1, whereas `3-2 max-share=2`. Additional independence of amplitudes or a lower bound on mixed fourth moments is needed. This does not invalidate the exact splitting; it invalidates the claimed kurtosis consequence even in its hypothetical invariant case.

## Two-dimensional setup and SU(2) value — HOLDS AFTER CORRECTION

Source lines 122–135. Use normalized plaquette kernel k and beta>0. On the **gauge-invariant** space of the spatial ring, gauge fixing a spanning tree leaves class functions of its holonomy H. Product Haar makes H Haar. Central convolution on every edge is b-fold convolution on H, so an irreducible character has eigenvalue c_r^b, with `c_r=(dim r)^(-1) integral k overline(chi_r)`. Complex conjugation is needed for a general irreducible character; inverse symmetry of this weight makes these coefficients real. The physical operator includes gauge projection, which acts as the identity on this space. The full unprojected edge space has additional degeneracies and is not the space asserted here.

For SU(2), the already-derived outline (GL3), lines 2210–2231, gives `c_j=I_(2j+1)(beta)/I_1(beta)`. The needed monotonicity is proved in `gap-q8test-opus.md:157–167`, Lemma 3.1(a): the adjacent ratio is the expectation of t under the positive density proportional to `exp(beta t)(1-t^2)^(n-1/2)` on (-1,1). Its mean is strictly between 0 and 1, by pairing t and -t. Thus the unique top odd character is spin 1/2, and the top nonconstant even one is spin 1. This reuses the repository's Bessel argument.

For the normalized real top odd function g=chi_(1/2), `chi_(1/2)^2=1+chi_1`; character orthogonality gives `E g^2=1` and `E g^4=2`. Consequently theta and rho are exactly the ratios printed in line 127, raised to b. **The value kappa=2 HOLDS.** WALL holds for every positive a,M. Correct “with equality” to “attains the threshold kappa=2”: equality in the minimum inequality occurs only when `(a/M)2(1-theta^2)>=1`.

The blanket “every coupling” must mean finite beta>0. At beta=0 all odd eigenvalues are zero and the odd ground eigenspace is degenerate; arbitrary choices of g then need not have the listed kurtosis.

## Two-dimensional Q_8 value — HOLDS

Source lines 130–131; beta>0 and the gauge-invariant ring convention above. Reuse `gap-assume-opus.md:359–363`, Lemma F1's class data. The defining character has values 2,-2 on the two central elements and zero on the remaining six. Hence `E chi^2=8/8=1` and `E chi^4=32/8=4`. Its character norm is one, so it is irreducible. Its squared dimension is four, exhausting the centre-odd part of the regular representation, whose dimension is |Q_8|/2=4. It is therefore the only odd irreducible. Its coefficient is `2 sinh(beta)/Z_Q>0`, with `Z_Q=sum_U exp(beta chi(U)/2)`. Thus the **flux ground** function, not just a trial character, has kappa=4 for every b.

## Two-dimensional 2T value — HOLDS

Source lines 130–131 and 312; beta>0. Reuse the same F1 class data: traces 2,-2,0,1,-1 have multiplicities 1,1,6,8,8. Thus `E chi^2=24/24=1` and `E chi^4=48/24=2`.

Check that chi is the top odd character. The quotient 2T/Q_8 has order three; let eta be a nontrivial quotient character. The three characters chi, chi eta, chi eta^2 have norm one and are mutually orthogonal. Indeed, each nontrivial quotient coset contributes eight to the sum of chi^2, as does Q_8; `1+omega+omega^2=0`. Their squared dimensions total 12=|2T|/2, so they exhaust the odd irreducibles. With `Z_T=sum_U exp(beta chi(U)/2)`, their coefficients are

    c_chi = [2sinh(beta)+8sinh(beta/2)]/Z_T,
    c_chi_eta=c_chi_eta²=[2sinh(beta)-4sinh(beta/2)]/Z_T.

In each nontrivial quotient coset, multiplication by the central element -1 pairs traces +1 and -1, giving the displayed sums. Their difference is `12sinh(beta/2)/Z_T>0`. Both coefficients are nonnegative, and the second is positive since `sinh(beta)=2sinh(beta/2)cosh(beta/2)`. Raising to b preserves the strict ordering. The unique real flux ground character has kappa=2.

## Two-dimensional 2O value — HOLDS AFTER CORRECTION

Source lines 130, 135, 312. The source explicitly leaves the ground-character identification unchecked. The Haar moment is already in F1; the following short character comparison supplies the missing identification for beta>0.

The quaternion description is 2T together with the 24 elements having exactly two nonzero coordinates, each equal to plus or minus 1/sqrt(2). Thus the trace multiplicities are

| trace chi | 2 | -2 | 1 | -1 | sqrt(2) | -sqrt(2) | 0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| count | 1 | 1 | 8 | 8 | 6 | 6 | 18 |

These are F1's class data, with signs separated by U↦-U. They give `E chi^2=1`, `E chi^4=2`, `E chi^6=5`. Let epsilon be the quotient character of 2O/2T, and let `q=chi^3-2chi`, the character of the symmetric cube of the defining representation. Then chi, epsilon chi and q are actual odd characters of dimensions 2,2,4. They are orthonormal: q has norm squared `5-4·2+4·1=1`; `<chi,q>=2-2=0`; `<chi,epsilon chi>=0` because the sums of chi^2 on 2T and its coset are both 24; `<epsilon chi,q>=0` because on each part separately the sum of `chi^4-2chi^2` is zero. Norm one proves irreducibility. Their squared dimensions sum to 24=|2O|/2, so there is no omitted odd irreducible.

With `Z_O=sum_U exp(beta chi(U)/2)`, put `s=sinh(beta/2)` and `u=sinh(beta/sqrt(2))`. Directly summing the seven columns gives

    c_chi         = [2sinh(beta)+8s+6sqrt(2)u]/Z_O,
    c_epsilon_chi = [2sinh(beta)+8s-6sqrt(2)u]/Z_O,
    c_q           = [2sinh(beta)-4s]/Z_O.

The first exceeds the second by `12sqrt(2)u/Z_O` and the third by `(12s+6sqrt(2)u)/Z_O`. All are nonnegative: expanding `exp(beta chi/2)` in tensor characters gives nonnegative character coefficients. Alternatively the middle numerator has beta^(2m+1) coefficient `[2+4/4^m-6/2^m]/(2m+1)!`, zero at m=0,1 and positive thereafter. Thus chi is the unique top odd character for every finite beta>0. Its normalized fourth moment is exactly 2, independently of b. This completes the proof omitted at source line 312; it is a hand character calculation, not an enumeration run.

## Two-dimensional U(1) value and WALL failure — HOLDS

Source lines 130, 134; beta>0 and real normalized functions. Characters are `exp(i n phi)`, with coefficients `I_|n|(beta)/I_0(beta)`. The already cited positive-density Bessel argument orders them strictly with |n|. Odd means odd n. Every real unit top odd vector is `sqrt(2)cos(phi-alpha)` for a phase alpha; Haar integration gives `E g^2=1`, `E g^4=4·(3/8)=3/2`. The degeneracy between sine and cosine does not change this value. A complex unit character has a different absolute fourth moment and is outside the real-g convention.

Here `theta=(I_1/I_0)^b`. The minimum inequality holds exactly when `1-theta^2<=40/(3a)`; hence the claimed failure condition is correct. For fixed finite beta>0, b→infinity makes theta→0; taking also a large makes the flux thermal weight small. The even sum is `2 sum_{k>=1}(I_(2k)/I_0)^(ab)`, which tends to zero: for any fixed positive integer s, bound it by `2(I_2/I_0)^(ab-s) sum_{k>=1}(I_(2k)/I_0)^s`; the sum is finite by the positive Bessel series and factorial decay. The same holds at a/2. Thus the 2D analogue has heavy flux and small even sums while WALL fails. This shows WALL is stronger than needed for such suppression; it is not a counterexample to a four-dimensional SH-box theorem.

## Two-dimensional Z_2 value — HOLDS

Source line 130; beta>0. The ring holonomy is a uniform sign, its sole odd character is itself, and its normalized convolution coefficient is tanh(beta). Thus `g^2=1`, kappa=1 and `theta=tanh(beta)^b` lies strictly between zero and one. WALL fails for every positive a,M. The value uses the normalized sign character, not the unnormalized trace of the reducible two-dimensional embedding.

## Connected in-class counterexample, §4.3 — HOLDS

Source lines 142–143. An explicit choice removes the unspecified smallness condition. On Haar SU(2), let `s=sign chi` (its value on the trace-zero null set is irrelevant), `phi=chi^2-1`. Character orthogonality gives `E phi=0`, `E phi^2=1`; also `|phi|<=3`, and phi is even. Choose `p=1/10000`, `theta=1-2p`, `r=1/100000`. The displayed kernel is bounded below by

    1-theta-r||phi||_infinity^2 >= 2/10000-9/100000=11/100000>0.

The three functions 1,s,phi are orthonormal. Thus the operator is the sum of their rank-one projections with coefficients 1,theta,r, respectively. It is Markov, reversible, nonnegative and compact; g=s is the top odd eigenfunction, rho=r, and kappa=1. For example at a=100, `S_ev(a)=r^100<160^(-16)`, `S_ev(a/2)=r^50<=1`, and Bernoulli's inequality gives `theta^100>=1-100(2p)=49/50`. WALL still fails since its right side is strictly positive. Every comparison here is exact integer arithmetic.

The continuous-kernel variant also holds, with a normalization precaution. Replace s by the continuous odd clipped function `u_delta=clip(chi/delta,-1,1)` and normalize `g_delta=u_delta/(E u_delta^2)^(1/2)`. As delta decreases to zero, dominated convergence gives `m_2=E u_delta^2→1` and `E g_delta^4→1`. Choose delta so small that `theta/m_2+9r<1` and `E g_delta^4<2`. Then

    P_delta(U,V)=1+theta g_delta(U)g_delta(V)+r phi(U)phi(V)

is continuous and strictly positive, with the same three nonzero eigenvalues. It meets GLUE above and violates WALL by D. Connectedness, even with a continuous positive kernel, therefore does not supply WALL. This is a counterexample in (S+), not a Wilson plaquette-action counterexample and not a 4D SH box.

## Independent-tube identity, §4.2 — HOLDS

Source lines 137–140. For independent identical normalized odd variables w_i, oddness gives zero mean and zero third moment. In the fourth power of their sum only the all-equal index and the three pairings survive. Dividing by n^2 gives `kappa=3-(3-kappa_1)/n`. Tensor-product dynamics gives the stated eigenvalue. Thus n>=2 implies kappa>=2. This is a sufficient construction. Its converse, suggested by “KURT is the statement g splits into at least two independent parts”, is not proved and is not used. B1 alone supplies no such independence.

## Completed scope and disposition

Every requested mathematical statement has a verdict above. D, D1, A1, B4, B4′ and B5 hold on their stated finite-volume domains. D2, A2, A3, B6, K′ and the extended B1 claims require the explicit repairs above. All six exact 2D kurtosis values hold for beta>0 on the real gauge-invariant ground space; the 2O identification omitted by the source is supplied here. The connected counterexample holds, including a continuous version. The independent-tube identity also holds. The three claimed physical/spectral identifications and the extra B1 inferences marked FAILS must not be used.

The source's GUIDE computations, B2's action estimate, 4D rival-phase assertions, SH gluing theorem and existence of the required 4D kurtosis floor were not proved or computationally tested here. No claim is made that the scalar ratio W is a measured vortex duration, or that a finite-box moment bound diagnoses a topological phase. The checked consumer implication leaves its actual Wilson-SU(2) input open. Different provider provenance is recorded; it is not itself evidence of an independent mathematical check. The proofs above give the hand reasoning used.

RESULT: Row 897 checked by Codex gpt-6-astra xhigh: D, D1, A1, B4, B4′ and B5 HOLD; D2, A2, A3, B6, K′ and B1 HOLD AFTER the stated numerical, domain and scope CORRECTIONS; all six 2D kurtosis values HOLD for beta>0, with the missing 2O ground-character proof supplied; the connected counterexample HOLDS; the eight-vacua/topological-order identification and B1's extra kurtosis/vacuum-density inferences FAIL. Under GLUE the minimum-form WALL_40 remains exactly kappa>=2, and K′ retains the sufficient floor kappa>=1.66. No 4D SH-box kurtosis floor or mass gap is proved or refuted here; no status is granted.
