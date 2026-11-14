# Repo search

FINISH row 893, gap-crux-core-check-astra. Repository pinned at commit 2f21d83a9. The required target-prior lookup returned absent before this file was created on the first step. Verdicts were appended as each check was completed. Research text only; grants no status. No computation discharges a mathematical obligation.

Provenance: OpenAI/Codex, gpt-6-astra xhigh (row 893 assignment), 2026-11-13. Checked source `gap-crux-core-max.md`, 479 lines, at `2f21d83a9e7a7f78b04c2feb387e4054de25c12d`. Research check, not an audit; grants no status. The author's argument and its quoted earlier verdicts were visible. Independence here consists of the hand derivations below, not merely a different provider. No numerical proof, simulation, or formal verifier is used. Only this output file is changed.

The target-specific prior file is absent. The general `prior/repo-search-2026-11-08.md` is a retrieval aid about earlier RG targets, not a check of these flux statements. The registry search found no competing owner for row 893 or its named statements; unrelated geometric CORE rows are different objects. This is the requested check, not a new attack on (WALL), (HB), or (CORE).

Search refs in `/Users/jonreilly/Projects/Physics`: `origin/main=993f5e4f6d11a7e20a1cab9612c5749a53bae073`, `pr/10114=f76f6c649cff7dffbab664d8976e680e8f287fe9`, `pr/10133=89faef229ff6e6bde42baad15ed8270c2f4087d8`, `pr/10134=1e70c7211a2cdbc39001e619f1dd89db45e25851`, `pr/10141=c73ad7b177d94f89ff37b77386936e3d52b48b05`. Each search used bounded `git grep -n -i -E ... -- '*.md' '*.tex' | head`, including files outside this lane. Broad searches for `E17`, `Lemma SPLIT`, `spectral core`, `odd flux`, `kurtosis` hit their caps and prove no absence. Their visible hits are different objects: `pr/10114:.../ym4d-proof/BFT_B.md:4031` splits source slots, not thermal sectors; `origin/main:docs/ENERGY_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:267` identifies an energy subspace isometrically, not electric flux; `pr/10134:.../parts/witness.md:535` computes the fourth cumulant of a Gaussian plaquette composite, not a flux eigenfunction. No such hit is used as this target's proof. The completed narrowed all-ref search is recorded in section 14.

Relevant local prior work, read at source: `gap-es1-opus.md:30-76` already proves the crossed-sector identities, Theorem V and its upper/lower deficit bounds. Its exact inputs are positive twisted transfer operators, crossing, permutation symmetry, and `0 <= p_z <= 1`, `sum p_z = 4`. ABS is an application of that result, not a new deficit theorem. `gap-seed-shape.md` supplies the conditional shape-to-gap theorem; it does not supply the seed. These inputs are credited to their named lane authors.

Outline lookup used `sa-index/README.md`, neighbouring rows `chunk-02.md:99-102`, `chunk-03.md:128-130`, and `obligations.md:102-104`. Searches included transfer operator, thermal sum, centre flip, twist, vortex, kurtosis and spectral gap. Source SA 2315-2335 supplies `L=P C_E^{1/2} exp(-V) C_E^{1/2} P`, positivity, trace class and `Z_s(0)=Tr L^s`. SA 3712-3720 explicitly says no spectral gap above the invariant subspace has been proved. Reuse the transfer construction; neither passage checks this note's flux reductions. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. No Balaban estimate is consumed here; Tadeusz Balaban's original papers were not read or newly imported.

## 1. Proposition ABS — HOLDS AFTER CORRECTION

Source 154-158; input `gap-es1-opus.md:51-76`. The statement and final constants survive. Correct the proof's use of Corollary V1 and its incomplete large-h split.

For any selected four sectors, Theorem V(b) directly gives `Delta <= H_L + sigma_L + S'` when `(H_L+sigma_L)/2 <= 1/2`; selection of the four largest weights is unnecessary. Thus `delta <= 7(1.4e-8)=9.8e-8 < 1e-7`. The separate hypothesis on `eps_aa` completes (ES).

For the converse, positivity of the three deficits gives `Delta <= 1e-7`. Theorem V(a), without any condition on `sigma_L`, gives

`Q <= 4[1-exp(-Delta-2 eps)] <= 4(Delta+2 eps) <= 1.2e-6`.

Set `d=1.3e-6`. Since `d(1-d)>1.2e-6`, every `p_z` lies in `[0,d)` or `(1-d,1]`. If k entries are near one, `|k-4| <= 16d < 1`; hence k=4. This works for ALL h, including h>=1 omitted by the printed parenthesis. For the four largest entries, `h <= 12d < 1/2`. Theorem V(a),(c) now gives `h(1-h)<=6e-7`, so `h<=6e-7/(1-12d)<6.1e-7`. No sector thermal bound is needed for this direction.

Use the author's later Q-ABS correction at 418: `Q_F<=5e-11`, four light sums each `<=1e-9`, and `S'<=4e-9` give `96 Q_F+4e-9+4e-9<=1.28e-8`. The earlier `1.4e-10` budget is superseded. This proves an absolute one-size sufficient input, conditional on the accompanying thermal bounds, not a seed at any actual SU(2) coupling.

## 2. Lemma SPLIT — HOLDS

Source 267-270, with the positive transfer and centre-sector setting from `gap-es1-opus.md:30-44`. Put `w_chi=Z_chi/Tr(T^t)` and `u=sum_{chi!=0} w_chi`. These are nonnegative sector probabilities. The indicator that at least one of three bits is nonzero lies between each bit indicator and their sum. Therefore `Q_0<=u<=3Q_0`. The identity `1-u=(1+S_ev)/(1+S)` immediately gives both displayed bounds when `3Q_0<1`. Also `S_ev<=S` and `u<=S/(1+S)` since the even sector contains the vacuum. Hence `Q_0<=S/(1+S)`. No dynamical or rate assumption is hidden in this step.

## 3. Corollary O1 — HOLDS

Source 272-280. In (a), subtract `1+s/2` from `(1+s)(1-3s/7)`: the result is `s(1-6s)/14>=0` for `0<=s<=1/6`. In (b), SPLIT gives `S<=(11/10)/(17/20)-1=5/17<3/10`. In (c), SPLIT gives the stronger `Q_0<=s/(1+s)` along with `S_ev<=s`.

The source of the shape thresholds was read at `gap-seed-shape.md:45-152`. The `r>=24` use is legitimate: its `(j,p,q)=(6,6,12)` recurrence and threshold `3/10` apply to the FULL thermal sum, which O1 bounds. For a simple independent slack check, on `x<=3/10`, `u<=216 x^6(1+(7/2)x^6)<0.16`, so `exp(u)<=1/(1-u)<25/21`. Thus `phi(x)/x^6<216(1.003)(25/21)<258< (31/10)^5`; the larger hand constant `K=31/10` still has `K(3/10)=93/100<1`. This confirms the consumed threshold without relying on decimal evaluation of 3.03.

Scope: SH gives a volume-uniform positive lattice gap at each fixed seed datum, and an explicit rate `log(1/(K s))/(2a)` for cubes beyond its finite scale `L_0`. A uniform physical application requires a seed for EVERY first-passage datum at fixed physical time and shape. The full continuum identification still uses the account's named inputs. O1 supplies none of these seeds. Also `Q_0<=1/20` is sufficient with glue, not necessary at that SAME constant: `S<=3/10` only gives `Q_0<=3/13` by the universal converse.

## 4. Face F2 — HOLDS

Source 335-338. Write `y=theta_P^b`, `A=1+s_+`, `B=1+s_-`. Crossing gives the exact fraction `q=yB/(A+yB)`, with `0<y<=1`, `A,B>=1`. Increasing the fraction in B gives `q>=y/(A+y)>=y/(A+1)`. Its denominator is at least A, so `q<=yB/A<=yB`. These are the stated bounds. The sufficient energy threshold can be written exactly as `E_P >= [log 20+log(1+s_-)]/b`; replacing `log 20` by 3 is safely stronger since the first nine positive terms of the series for `exp(3)` already exceed 20. The ratio `3/24=1/8` explains the rounded 0.13; it is no estimate for the actual SU(2) energy.

## 5. Face F3 — HOLDS

Source 340-344. Inputs are exactly the twisted transfer, crossing and axis symmetry in `gap-es1-opus.md:30-44`; the citation to its line 38 should point to line 30 for top-eigenvalue domination. Let `e=b eps_v`, `A=1+s_+`, `B=theta_P^b(1+s_-)`. Then `Z^0/lambda_0^b=A+B`, `Z^v/lambda_0^b=A-B=exp(-e)(1+S_v)`, and `q=B/(A+B)`. This independently verifies the displayed identity.

Since `A+B=A/(1-q)`, `1-2q>=exp(-e)(1-q)/A`. Put `x=exp(-e)/A` in `(0,1]`; then `q<=(1-x)/(2-x)<=1-x<=e+s_+`. In the other direction `A+B>=1`, so `1-2q<=exp(-e)(1+S_v)`. Taking logs gives `e<=-log(1-2q)+log(1+S_v)<=2q/(1-2q)+S_v`. Finite positive Wilson partition functions ensure `q<1/2`, so the denominators are valid.

## 6. Variational face (VF) — HOLDS AFTER CORRECTION

Source 345-349 and edge 36 at 377. The SUFFICIENT statement holds: `b eps_v<=1/25` and `s_+<=1/100` give `q<=1/20`. Equivalently its eigenvalue hypothesis is `tau_v>=tau_0 exp(-1/(25b))`. Rayleigh trial vectors bound the required side.

Correct edge 36 and every use of “face” as an equivalence: this is a sufficient face with a different thermal input, not `(CORE) <=> (VF)` with the printed constants. F3 returns only `b eps_v<=1/9+S_v` from `q<=1/20`. Even with zero thermal corrections, the scalar identities allow `A=1`, `B=1/19`, `S_v=0`, giving `q=1/20` and `b eps_v=log(19/18)>1/25` (use `log(1+x)>=x/(1+x)=1/19`). This is a counterexample to the asserted inference from those identities, not an asserted Wilson realization. Moreover `s_+` in the crossed `(a,b,b)` box is not `S_ev(a;b^3)`; the two glue hypotheses must remain distinct.

## 7. Lemma VAR1 — HOLDS

Source 357-362; transfer factorization read in `gap-filter-ls-opus.md:128-151`. Write `c=z^|E|`, `A=K^(1/2)`, `B=B_0`. The proposed measure has mass `c <A Omega_0,B A Omega_0>/tau_0=1`, irrespective of pointwise signs of `A Omega_0`. Its density is nonnegative. Rayleigh's inequality gives `tau_v/tau_0>=E_nu D_ell`; convexity of exp gives `E_nu D_ell>=exp(-2 beta sum E_nu x_p)>=exp(-2 beta b)`. Thus `eps_v<=2 beta b u`, with u the mean on the specified line. This is only an upper bound supplied by this trial vector; comparing its size with (VF) does not disprove (VF) or rule out better trials.

## 8. Lemma VAR2 — HOLDS AFTER CORRECTION

Source 364-372. Parts (i),(ii) hold verbatim. The spectral measure of the unit vector Omega_0 for `T_v>=0` is a probability measure on `[0,tau_v]`. Its nth moment is at most `tau_v^n`; Cauchy-Schwarz gives its 2nth moment at least the square of its nth moment. These prove the upper energy bound and its improvement on doubling.

Make (iii)'s stationary process precise. Positivity as an operator of `L_0=c K^(1/2) B_0 K^(1/2)` alone does not identify its coordinate kernel as a Markov kernel. Use the physical positive-kernel representation already proved in `gap-transfer.md:108-181`:

`M_0=c B_0^(1/2) K B_0^(1/2)`,
`psi_0=sqrt(c/tau_0) B_0^(1/2) K^(1/2) Omega_0`.

It has the same nonzero spectrum; `||psi_0||=1` and `M_0 psi_0=tau_0 psi_0`. Choose psi_0 positive. Its Doob kernel is `M_0(U,V) psi_0(V)/(tau_0 psi_0(U))`, stationary law `psi_0^2 dU`, which equals nu of VAR1. Expanding the n factors between their magnetic slices now gives exactly

`W_n=E_nu[D_ell(X_0) ... D_ell(X_(n-1))]`.

There are n insertions on consecutive magnetic slices, and n-1 full transitions of this chain. This specifies the half-step convention instead of silently treating multiplication at the kinetic slice as the same observable.

The further spectral limit is also available for each fixed finite Wilson box. Write `M_v=c B_v^(1/2) K B_v^(1/2)` with its positive unit vacuum psi_v. Then `Omega_v=sqrt(c/tau_v) K^(1/2) B_v^(1/2) psi_v`. The overlap is a positive multiple of `<B_0^(1/2)psi_0,K B_v^(1/2)psi_v>`, strictly positive since the Wilson gauge-averaged K kernel is strictly positive. If `c_v=|<Omega_0,Omega_v>|^2>0`, spectral decomposition gives

`c_v exp(-n eps_v) <= W_n <= exp(-n eps_v)`.

Thus the energy part of (VF) is equivalent to `W_n>=c exp[-n/(25b)]` for all n, for SOME c>0 at this fixed box. No cutoff-uniform overlap is established. Keep `s_+<=1/100` separately. This is a bound on an open sheet in this vacuum process; identifying it with the equal-time spatial-loop hypothesis (S1), or with E17's wrapping partition-function ratio, needs an additional bridge. The algebra above supplies no such identification.

## 9. Proposition K — HOLDS

Source 385-389. The consumed SQ-F statement and proof were read in `gap-brainstorm2-max.md:486-494`, alongside check 883, `gap-brainstorm2-check-astra.md:138-170`. Keep the physical positive-kernel ground functions of that source, not an arbitrary isospectral representation's fourth moments.

For each nonzero character, `gamma_chi>=gamma=eta/[8(1+eta)]`. Since the assumed even sum is below one, both `S_ev(a)^gamma_chi` and `exp(-gamma_chi a)` are at most `1/160`. SQ-F gives `p_chi<=2/160=1/80`. Exactly four characters have any prescribed nonzero bit; dividing their weights by the full trace only decreases them. Hence `q_i<=4/80=1/20` for all i. Also `1/gamma>8`, so `S_ev(a)<=160^(-1/gamma)<1/10`. O1(b) gives `S<=5/17<3/10`, and SH applies at `b>=24a`.

This is a valid absolute-seed implication. It explicitly pays for both the half-time prefactor and the exponential remainder that defeated the earlier pure F-h claim. It does NOT use the invalid discrete implication KURT => FUSE-E (check 889). All seven electric sectors are required. Uniform physical conclusions retain the all-datum seed quantifier and SH scale qualification in section 3.

## 10. Lemma R — HOLDS

Source 391-393. Let P be the physical reversible Markov ground-state transform, `Pg=theta g`, `E g^2=1`, `E g^4=kappa>1`. Pointwise Jensen gives `P(g^2)>=(Pg)^2=theta^2 g^2`. Multiplying by g^2 and integrating yields `<g^2,Pg^2>>=theta^2 kappa`. For `h=g^2-1`, centre parity makes h even, its mean is zero, and `||h||^2=kappa-1`. Thus `theta^2 kappa-1<=<h,Ph><=rho(kappa-1)`. Rearrangement gives exactly `rho>=1-kappa(1-theta^2)/(kappa-1)`. This controls the discrete deficit `1-rho`; it is not directly a bound on `-log rho`.

## 11. Proposition W — HOLDS

Source 397-405, using the CONDITIONAL (WALL)_40 stated at 397: whenever `kappa<=2`, require `kappa-1 >= (a/40) kappa(1-theta^2)`. At finite positive Wilson coupling, `kappa=1` is excluded: a continuous real normalized odd g cannot have `g^2=1` on the connected link configuration space with full-support vacuum measure. Hence Lemma R can be used if `kappa<=2`.

It gives `rho>=1-40/a>1/2`. For `0<=x<=1/2`, integration of `1/(1-x)<=1+2x` proves `log(1-x)>=-x-x^2`. Thus, at `a>=82`,

`rho^a >= exp(-40-1600/a) > exp(-60) > 160^(-16)`.

The last comparison follows from `log 160>5`: the exponential series bounds `e<11/4`, and `(11/4)^5<160`. This contradicts `rho^a<=S_ev(a)<=160^(-16)`. Therefore all seven kappas exceed 2.

For K with eta=1, `gamma=1/16`. Its time condition follows exactly from `16 log 160<82`: the series gives `e>27/10` and `exp(1/8)>9/8`, while `9*27^5=129140163>128000000`, so `exp(41/8)>160`. K and O1 yield `Q_0<=1/20` and `S<=5/17<3/10`; SH supplies the stated fixed-datum gap. No rounded equality such as `160^(-16)=exp(-81.2)` is needed.

**Correction to the advertised final “same” next statement (475), not to this proposition:** `Var(g^2)>=min{1,(a/40)kappa(1-theta^2)}` is weaker at `kappa=2`. It is then automatic, whereas the conditional WALL above need not be. With this final min-form, the same proof excludes only `kappa<2`; it gives `kappa>=2`, which still suffices for K, CORE and the seed. State that corrected conclusion, or require the wall inequality also at equality. Likewise the sentence at 412 identifying WALL with an even excitation of logarithmic rate `<=M/a` needs `-log rho<=-log(1-M/a)`. For W it is enough that `-a log rho<60`. WALL is a sufficient route to HB with constants; no converse from HB is proved.

## 12. “CORE is genuinely weaker than E17” — FAILS as an established logical comparison

Source 306-310, 450-452 and RESULT. E17's actual consumer was read at `gap-vortex-astra.md:173-211`. It controls specified twists on tori `(a,a,c,d)`, `c,d in {a,2a}`, for large a at fixed coupling and at a specified exponential rate. CORE controls an untwisted spatial cube on `(a,b,b,b)`, `b>=24a`, at a selected size; its continuum version quantifies over first-passage data. These are different domains, not a restriction of one quantified statement to fewer cases.

The note itself admits no E17 => CORE edge without extra glue. Adding glue changes the premise being compared. It also supplies no converse/non-converse theorem within the actual Wilson family. A large-box spectral gap does not by itself bound a thermal TRACE at time proportional to box side: multiplicities can grow, and twisted-background traces require further comparison. Therefore “both say electric flux is heavy at all sizes” cannot fill the missing rate, trace and background bridges. This verdict rejects a proved ordering, not CORE as an open sufficient target and not E17 as an actual Wilson assertion.

Correct replacement: **CORE plus `S_ev(a;b^3)<=1/10` is a one-size sufficient condition for the SH seed. No input decay rate is needed for this conditional implication. Its logical ordering relative to E17 is not established.** It is also not shown to be the weakest sufficient condition. At fixed box and coupling, existential NGD can even be vacuous by choosing `0<s_0<S_ev`; only a separately supplied glue bound `S_ev<=s_0`, with the matching all-datum quantifier, makes it useful. SPLIT gives comparisons of sufficient thresholds, not exact equivalence at each printed constant.

## 13. Ten graph edges checked against their sources

These are source checks of numbered edges in 3.2, not a check of every claim in the 38-edge graph. Existing proofs and counterexamples are reused, with their scope; no closure is inferred from a prior verdict alone.

### Edge 3: HA => (P), with area gain — HOLDS

Read row 866, `gap-z2parity-astra.md:303-331`, and row 870, `gap-z2parity-check-opus.md:35-45`. Conditional on the earlier area-order zero `ord_0 F>=A_i`, divide F by `lambda^A_i` and use the maximum principle on radius s<r, then let s increase to r. At one this gives `F(1)<=BN r^(-A_i)`. The real branch is fixed by positive interpolating partition functions. Therefore `q<=(BN/2)r^(-A_i)<=12 B a^4 exp[-(log r)a^2]`. Completing the square in `-(log r)a^2+g a` preserves the prescribed E17 rate, with factor `exp[g^2/(4 log r)]`. HA remains an unproved hypothesis.

### Edge 7: EXC relative identity and its E17 consequence — HOLDS

Read row 872, `gap-filter-ls-opus.md:128-151,170-185`, and row 873, `gap-filter-ls-check-astra.md:143-175`. Integrating EXP gives `p(1)=p(s_*) exp[-a integral Delta(s) ds/s]`. EXC(c_0) is exactly the printed relative inequality. Since `p(s_*)<=1`, it implies the named E17 rate if `c_0>=g=-(1/2)log eta_*`. The graph already includes this repair; arbitrary positive c_0 cannot be substituted for the witness rate.

### Edge 10: (DRESS) <=> EXC-W, with a carrier condition — FAILS

Read row 888, `gap-excmag-max.md:227-237`, row 872 at 170-185, and the later check 890, `gap-excmag-check-astra.md:68-119,512-547`. DRESS is the INTEGRATED bound `integral_1^S Delta_beta(s) ds/s>=kappa L_i`. Literal EXC-W in row 872 is the POINTWISE bound `Delta(s)>=delta L_i` for every s. The latter implies the former with `kappa=delta log S`; the reverse direction is not an identity. For example, on log s in [0,1], a function equal to `-L_i` on the first quarter and `2L_i` afterwards has positive area integral and no positive pointwise lower bound. This refutes the proposed rearrangement, not DRESS for Wilson SU(2).

Remove the carrier-switch condition from the exact identity: EXP defines the integrated response without selecting a unique fundamental sheet. A carrier interpretation is an additional open assertion, not an identification of these two inequalities. Check 890 also rejects deriving carrier crossing or erasure of the electric gain from second-order data. Thus the graph must not retain those arguments as established obstructions. Neither integrated DRESS nor pointwise EXC-W is proved at isotropic coupling.

### Edge 12: SEED-DEC-U => FQ — HOLDS AFTER CORRECTION

Read row 887, `gap-seeddec-max.md:163-178,194-206`, and check 891, `gap-seeddec-check-astra.md:90-101`. OUT(U) gives `q_(m,i)<=Pr_m([gamma]!=0)<=N_box p_0`, with `N_box=acd/g^3`. At `g=a/4`, this is 64 only for the spatial cube; it is 128 or 256 for the other consumer shapes. Require `a>=8`, `4|a`, compatible side divisibility, and both bounds `N_box p_0<=K sqrt(S)/8` and `N_box p_0<1/192` for EACH required twist and shape. These yield FQ directly. No magnetic-background reflection positivity is needed, and no estimate of p_0 is proved by the union bound. The note's blanket 64 must not be used on the rectangular boxes.

### Edge 14: SEED-DEC-H => stretched-exponential odd weight — HOLDS AFTER CORRECTION

Read row 887, `gap-seeddec-max.md:146-178,197-200`, and check 891, `gap-seeddec-check-astra.md:59-88`. Keep CE and covariance as premises. The same-class pair recursion is `z_(j+1)<=C_3 z_j^2`; its count is `[(70+61)^3-(10+9)^3]/2=1,120,616`. Induction gives `z_J<=C_3^(-1)(C_3 z_0)^(2^J)`. At `L=4g10^J`, OUT(H) gives `Pr([gamma]!=0)<=64 C_3^(-1)theta^(2^J)` if `C_3 z_0<=theta<1` uniformly in J. The exact exponent is `log 2/log 10`, not the rounded 0.301 used as an equality.

Use `z_0<1/1,120,616`, with a UNIFORM strict margin, not merely “below 8.93e-7”: multiplying the latter by C_3 gives `1.000710088>1`. The check's CE premise remains unsupplied for the actual one-slice law. No nonzero magnetic-background CE is proved.

The note's proposed use for an absolute seed is valid conditionally: impose this bound at the same untwisted time/shape family as SH, and supply glue at one of those sizes. Then sufficiently small odd weight supplies CORE through SPLIT. Decay on a different time schedule does not provide that seed. Mere pointwise strict inequalities with margins tending to zero as L grows are also insufficient. Check 891 corrects the claim that the separate Peierls output must be verified at level zero; the graph must not preserve that exclusion.

### Edge 15: FQ => F-h — HOLDS

Read `gap-vortex-astra.md:173-211` and check 780, `gap-vortex-check-opus.md:45-62`. A nonzero crossed character has an odd bit in direction 3 or 4, so its trace is bounded by that odd-bit trace. `Z^m<=Z^0` and `Z_(0,0)>=Z^0/8` yield `p_(chi,m)<=8Q_F`. Under `Q_F<1/192`, the twelve such weights total less than 1/2; since the sixteen weights sum to four and each is at most one, the four purely magnetic weights are the light group. Thus FQ gives precisely F-h. It supplies neither F-l nor the even sums.

### Edge 16: F-h + F-l + six even sums => ES — HOLDS

Read `gap-es1-opus.md:204-217` and check 753, `gap-es1-opus-check.md:370-402`. Twelve heavy and four light sectors give `eta_L<=6K sqrt(S)+2KS`; Theorem V then gives `Delta<=12K sqrt(S)+4KS+S'`. Sum the three deficits with weights 4,2,1. With `K_*=max(1,K)` as the target note already specifies, and every indicated sum at most `d=10^(-16)/(144K_*^2)`,

`delta<=7e-8+(35/144)e-16<1e-7`, and `eps<=d<1e-7`.

This is a conditional implication with all listed input sums at the SAME size. No flux hypothesis alone supplies them.

### Edge 22: KURT => FUSE-E in discrete time — FAILS

Read row 886, `gap-kurt-max.md:497-505`, check 889, `gap-kurt-check-astra.md:421-477`, and the original counterexample `gap-loop-eq-check.md:466-512`. Credit that prior counterexample; it is not new here. On Haar SU(2), `f=tr U`, `h=f^2-1` have zero mean, unit L2 norms, and are orthogonal, with `Ef^4=2`. The positive Markov kernel

`K_tau(U,V)=1+(1/8)f(U)f(V)+tau h(U)h(V)`, `0<tau<1/36`,

has eigenvalues `1,1/8,tau`, positive lower bound `1-1/2-9tau>1/4`, odd kappa=2, and even ratio rho=tau. Thus KURT holds uniformly but `E/m=log 8/log(1/tau)` tends to zero. No uniform positive FUSE-E exponent follows from these discrete kernel premises. This is not a Wilson-action counterexample or a supplied model of the full crossing class; it disproves the edge attributed specifically to SQ. The corrected SQ estimate controls `1-rho`, not the logarithmic energy ratio. Proposition K above avoids this edge and survives.

### Edge 24: FUSE-E => the displayed periodic-sector trace bound — HOLDS

Read row 886 at 497-505, row 876 at 486-494, and check 889 at 421-435. For the matching periodic operator and even `a>=6`, spectral calculus gives `p_chi(a)<=Theta_chi theta^(a/2)`, with `Theta_chi<=1+S_ev(a/2)`. FUSE-E says `theta<=rho^g`; since `rho^a<=S_ev(a)`,

`p_chi(a)<=[1+S_ev(a/2)] S_ev(a)^(g/2)`.

This edge has no kurtosis premise. If it holds for all seven sectors, with `S_ev(a/2)<=1` and `S_ev(a)<=160^(-2/g)`, its four-bit sum gives CORE. The graph's use with those additional hypotheses is sound. Check 889's rejection of unqualified full-consumer sufficiency does not refute this displayed estimate; it prevents silently dropping the half-time, other-sector, and glue inputs.

### Edge 27: TS-theta + a “four per cent seed” => geometric growth — HOLDS AFTER CORRECTION

Read row 878, `gap-crux-exercise2-max.md:485-515`, and check 884, `gap-crux-exercise2-check-astra.md:100-127`. The corrected recurrence is valid with `0<theta<4`, the two actual one-flip-even thermal sums bounded by s_*, and TS applicable at the intermediate shape. Put `r=4/theta`, `D=(6/theta)log(1+s_*)+C`, `Phi_*=D/(r-1)`. Then `Phi(2n)-Phi_*>=r(Phi(n)-Phi_*)`; a seed must satisfy `Phi(n_1)>Phi_*`.

There is no universal four-percent seed. At `theta=1,s_*=4`, the required ODDS are `q<e^(-C/3)/25`, or probability `p<e^(-C/3)/(25+e^(-C/3))`. Moreover `S_ev<=1` gives only `s_+<=3+4S_ev<=7`, since the one-flip-even space contains four charge sectors; with `C=0` this instead gives `q<1/64`, `p<1/65`. The target marks this edge “after correction” but repeats the discarded four-percent shorthand at 169 and 244. Restore the actual threshold and intermediate thermal inputs. No new proof of TS, its seed, or the claim that TS is unnecessary for every proposed route follows.

## 14. Disposition and coverage

The conditional one-size reductions survive: ABS after its proof repair; SPLIT and O1; F2 and F3; VAR1; VAR2 with the specified magnetic-slice process; K; and W. VF is a sufficient condition with its additional thermal bound. None supplies the open flux or glue estimate at any coupling in the requested band.

The conclusions to change are specific: no established strict ordering CORE versus E17; no CORE/VF equivalence at the stated constants; no DRESS/pointwise-EXC-W equivalence; no discrete KURT => FUSE-E. The final min-form WALL still suffices for the seed, with kappa>=2 rather than the conditional form's strict conclusion. Preserve the exact decoder margin/domain and Theorem E's actual seed. The updates from checks 889-891 are incorporated above; their own proofs are not claimed as newly independent results.

Completed narrowed repo search: `gap-crux-core|FUSE-suff|SEED-FP|SEED-DEC|WALL\)_|kurtosis.{0,40}(flux|eigen)|vortex.free.energy|twist.deficit|centre.flips|center.flips`, all five recorded refs, cap 60. It returned five copies of one unrelated archived sentence at `archive/notes/docs/work_history/repo/review_feedback/FRAME_CAGED_LOCAL_MOTIF_CYCLE50_NOTE_2026-07-14.md:247`: a finite frame-coded record orbit carries a seed-decoded frame. That is a different record model, not a flux/thermal-seed theorem. No matching target or method statement was found in that completed search. This is a search result, not a theorem that the repository contains no alternative proof. A targeted index search for `SEED-FP|FUSE-E|kurtosis|electric.flux|centre.flip|center.flip|thermal.sum|vortex.free.energy|squared.eigenfunction` returned no entries in README, chunks, obligations or `sa-index/ca-full/`. The positive transfer construction was read through the separate indexed locator already recorded above.

Not covered: the remaining graph edges as complete proofs; claimed phase tests for U(1), finite groups or weakly coupled SU(2); the recalled numerical sizes; the failed-attack exclusions in Steps 6-7; the account's continuum construction; or proof of any seed, WALL, HB, NGD, CORE, DRESS or CE for the actual order-one model. No external literature was fetched. No simulation, numerical certificate, Lean check, test suite, audit, ledger update, source edit, commit or push was performed. The requested output is left locally in the pinned checkout.

Checkpoint: requested statement checks and ten edge checks complete. Source commit `2f21d83a9e7a7f78b04c2feb387e4054de25c12d`; output only. Final bookkeeping confirmed the target source and checks 889-891 remain byte-identical to the pinned commit. Target SHA-256: `d397352b6c30b5ac360dd6c544eac25cf5e5df22813a8e88f73055379d8a7c09`. This byte comparison is provenance only. Open obligations remain the actual all-datum flux bound and matching glue bound. The next decision for the lead is to repair these graph identifications before using the note to select a proof target; this check starts no new proof lane.

RESULT: SPLIT, O1, F2, F3, VAR1, K, R and W HOLD; ABS, VF and VAR2 HOLD AFTER CORRECTION; the claimed established weakening CORE < E17 FAILS. Of ten graph edges, 3, 7, 15, 16 and 24 HOLD; 12, 14 and 27 HOLD AFTER CORRECTION; 10 (DRESS <=> pointwise EXC-W) and 22 (discrete KURT => FUSE-E) FAIL. No order-one seed or mass gap is proved, and no status is granted.
