# PRE-STATED — independent hostile review of session-25 decade figures

UTC: 2026-10-28 22:02:14.

Scope: every decade figure and listed multiplicative comparison in SESSION25_RESULTS.md, with only the producing regions of owning files read. The two discretionary reads are SCIENCE_WORKFLOW.md and the project review-loop SKILL.md. No git, snapshots, audit ledgers, external publications, or whole large lane files. Only this deliverable will be written.

Prior exposure: the assignment supplied the required figures; before this registration I read ledger lines 1–170 and the methodology. I have not calculated any target or accepted any worker verdict. This review cannot attest to the author's model family or independence beyond using an independently implemented derivation.

Refutation criteria, fixed before calculations:

1. A reported rounded value is REFUTED if a rational enclosing interval excludes its stated rounding bin; approximations explicitly marked coarse are judged at their stated precision, not by invented extra digits.
2. A correct logarithm is nevertheless REFUTED as a live comparison if it uses a different threshold, ceiling, power, species N, packing constant, or constant version from the claimed baseline. Historical/conditional arithmetic will be distinguished from the live claim.
3. A claim of gain over an established route is REFUTED if the cited route lacks a load-bearing hypothesis or its proof does not imply the stated rate. An unchecked dependency remains NOT-VERIFIED, never CONFIRMED by a label.
4. A ceiling with output-dependent constants cannot certify a universal clearance unless those dependencies are controlled. A gate is non-discriminating if it is tautological, vacuous, internally impossible, or reconstructs its expected result from the same inputs without an independent implication.
5. Source locations will be found by strings, then actual current line numbers. Stale references are recorded. No finding receives CONFIRMED from a banked status alone.

Arithmetic protocol: plain Python integers and fractions.Fraction only. Logarithms will use range reduction and the atanh series with an explicit positive-tail upper bound; roots, if needed, will use integer rational brackets. No floats, Decimal, numpy, quadrature, or jobs writing auxiliary files. Report closed rational decimal enclosures.

Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. Review findings: CONFIRMED / NOT-VERIFIED / REFUTED. CONFIRMED arithmetic does not certify the underlying Yang–Mills claim.

## Findings (appended during review)

### F1 — REFUTED: both advertised programme-gain baselines

Targets: SESSION25_RESULTS.md:153–159, 187–195, 589–600; ARS_FIX.md:277–289; REVIEW_ARS_EPS_S1.md:501–517. Claim status: CONDITIONAL for the historical comparison; GAP for a proved programme gain.

RLARGE.md:64 defines eta_RS = min{epsilon/(2L^2), epsilon^2/(512 N A_d)}, while HIST.md:170 defines eta_q = min{epsilon/(2L^2), epsilon/(256 N A_d), delta_0/A_d}. KN_ADOPT.md:545 proposes eta_KN = epsilon/117. These are THREE thresholds. At d=4, L=3 and the tiny quoted epsilon values, eta_q/eta_RS = 2/epsilon, whereas eta_KN/eta_q = 2304N/117. Swapping these ratios produces the apparent contradiction between 79.84 and 2.303 decades.

The local RS-lin lemma can be reconstructed: HIST.md:137–149 uses stationarity P(W_0^{-1}M)=0 and the principal logarithm Y to obtain ||Y|| <= 1.134||Y||^2+2delta, with ||Y|| <= 1/8, hence ||Y|| <= 3delta. HIST.md:155–166 expands the kernel energy about its maximiser; the linear error is bounded by x||M-W_0||. HIST.md:177–179 then gives x >= epsilon/16 and ||M-W_0|| <= epsilon/(64N) <= x/(4N), so phi >= epsilon^2/(1024N). This verifies the local kernel mechanism, conditional on the stated geometric and Haar-ball hypotheses; it does NOT produce a joint bad-plaquette probability.

For that probability, HIST.md:505–521 explicitly ASSUMES (PLD-q)_k. Its proof selects at least |A_2|/81 nonadjacent cubes, then applies precisely that hypothesis. Without it the step bounding the nonquiet indicator product is absent. RLARGE.md:1020–1026 likewise imports a_eta from (PLD)_k and identifies eta_RS^2/(2N) only as a bare-level value. RLARGE.md:433–439 and 513–514 exclude both joint prices from the live HW route. Thus “already-proven route” in the ledger is false in the sense required for the +2.303 programme headline. The arithmetic ratio remains a conditional comparison of bare plaquette coefficients with two packing conventions, 625 versus 81.

### F2 — REFUTED: +63.619 as an established live clearance

Targets: SESSION25_RESULTS.md:578–580; ARS_BIND.md:336. Claim status: CONDITIONAL benchmark; GAP for the asserted quantitative conclusion.

RLARGE.md:88–94 says a = min{theta*a_bad,a_A}, a_bad = c_pr*min{epsilon^2,t_pr^2}, c_pr = 1/(640*53^2), and 24*theta*(1+2R*g_K^2) < 1. It does not say theta=1/24, a_A >= theta*a_bad, or epsilon=6.7e-40. Indeed RLARGE.md:71–72 makes 6.7e-40 just one entry of a minimum with unevaluated outputs C_Delta, C_flat and r_flat. RLARGE.md:612 prints a LESS-THAN upper estimate. Evaluating the supremum theta=1/24 and dropping a_A gives an UPPER bound for clearance, not a lower bound.

Let epsilon_0=6.7e-40, a_0=epsilon_0^2/(24*640*53^2), D=2.456e-152. At epsilon<t_pr the exact benchmark formula is

    log10[(a/100)/(D/C_Omega)]
      = log10[a_0/(100D)] + log10(C_Omega)
        + log10(min{24*theta*(epsilon/epsilon_0)^2, a_A/a_0}).

For example theta=1/10^70 satisfies the displayed upper constraint for sufficiently small coupling. With C_Omega=1 and epsilon=epsilon_0 it reduces the benchmark by log10(10^70/24), reversing the clearance sign even if a_A is harmless. Alternatively a_A=10^-160 makes the clearance negative directly. The supplied text does not exclude either witness. This refutes the unconditional inference; it does not prove the HW route cannot choose better constants. The coupling divisor 100 is itself a hand estimate at RLARGE.md:615–618, so an interval certificate for the displayed benchmark is not a theorem for all entropy prefactors.

### F3 — REFUTED as live currency: QFIX's 24.089-decade programme lever

Targets: SESSION25_RESULTS.md:1059–1089; QFIX.md:254–265, 507–508. Claim status: CONDITIONAL sensitivity, GAP as programme clearance.

QFIX calls the old a_RS ceiling binding, although RLARGE.md:433–439 excludes that price. Its factor eight follows correctly ONLY from the historical model a_RS proportional to epsilon^4 with epsilon_cut proportional to C_D^-2. With the live epsilon-limited HW branch a proportional to epsilon^2, the same q-induced change of C_D gives factor FOUR instead of eight, provided theta, a_A, C_Omega and all other ceilings stay fixed. The resulting half-size conditional lever will be computed below. This is another stale baseline, not a numerical repair of the discarded branch. The source's C_D(q), C_T(q), q-dependent theta_G and epsilon_* must stay attached to the comparison. A finite-q curve with these frozen inputs is not a uniform theorem as q tends to infinity.

### F4 — REFUTED: the q→infinity optimum drops a load-bearing minimum

Targets: QFIX.md:302–325, 358–375; SESSION25_RESULTS.md:1064, 1088. Claim status: GAP for the programme optimum; PROVEN obstruction to the displayed limiting argument.

SQ.md:318–319 gives tau_flat <= tau_R, while SQ.md:1633 gives tau_R <= theta_0^SQ4/Cprime. SQ.md:1622 defines theta_0^SQ4 = min{theta_G,theta_epsilon}. Therefore

    t_pr = Cprime*tau_flat
         <= min{1/(3.31e7*C_D(q)^2), theta_G(q), theta_epsilon(q), other entries}.

QFIX.md:369–374 instead takes ONLY the first entry as equality. The same file's lines 125, 314–318 state theta_G = 1.46e-13*8/q. Consequently t_pr <= 1.168e-12/q tends to zero: epsilon_cut tends to zero and the historical a_RS objective tends to MINUS INFINITY, not -28.575. This conclusion holds even if epsilon_* is adjusted to avoid theta_epsilon. The comparison theta_G/theta_epsilon used by QFIX is not the necessary test theta_G >= theta_SUP. With the asymptotic scalar C_D, that latter crossing is q in [2.128874338,2.128874339]e25. The actual optimum and all other minima are NOT-VERIFIED. This does not invalidate use of a finite q=1000 with compatible thresholds.

There is an earlier, finite-q incompatibility in the checker: checks/qf1b_q.py:60 fixes epsilon_*=1.12e-37, inherited from EPSSTAR.md:482's old-q floor. That floor was evaluated at the old C_D=4.76e15. At q=1000, theta_epsilon in the same checker is [2.088557437,2.088557438]e-39, so epsilon_cut <= [1.469503884,1.469503885]e-44, not [3.823458095,3.823458096]e-43. Under those simultaneous fixed inputs:

- the q=1000 historical margin is at most [-34.252690332,-34.252690331], not -28.592;
- the epsilon gain over 9.38495112638e-45 is at most [0.194738723,0.194738724], not 1.610;
- the forced lowering is at least [4.658904064,4.658904065], not 3.244.

To retain QFIX's scalar q=1000 curve one must instead choose epsilon_* >= [2.914094417,2.914094418]e-36 and verify its OTHER upper bounds; its old “no-change floor” is not enough. EPSSTAR.md:687 offers much larger candidate thresholds, so this is a repairable condition, not an impossibility claim. That choice is absent from QFIX's combined margin/other-consumer check.

### F5 — CONFIRMED conditional arithmetic, REFUTED mixed precision and endpoint claims

The independent calculation uses the exact STAR_CONST.md:338–345 optimiser: if A=7/8 then minimising 8(9/T+2)/(A-T) gives 2T^2+18T-9A=0, T=(sqrt(387)-18)/4. With K=A-T, c_s=8(9/T+2)/K and c_g=2480/K+272 (STAR_CONST.md:328,399–400), their intervals are [411.922970884,411.922970885] and [5699.632830341,5699.632830342]. The Stage-1 formula is EPSSTAR.md:251–254; the q-dependent Lambda comes from SQ.md:1513,1570,1611,1624–1627; the curve's m=19615, F=175.8, N=2, kappa_+=1, c_N=2 and C_3=C_Omega=1 are QFIX.md:270–273,365–374. C_s and c_g are outputs of this particular allocation, not arbitrary same-glyph constants.

The scalar q curve, computed with these fixed inputs and t_pr=theta_SUP, is reproduced below. Its 24.089 figure is [24.089105770,24.089105771]; the corresponding epsilon-limited HW sensitivity is [12.044552885,12.044552886]. Neither is a proved live clearance (F2–F4).

Two arithmetic corrections:
- QFIX.md:344 / SESSION25_RESULTS.md:1068 “13.15” is REFUTED: 8 log10(B(8)/B(4)) lies in [13.143561886,13.143561887], rounding to 13.14. Moreover the stated objective caps epsilon_eff at 6.7e-40, so the plateau margin can actually rise only [12.957830686,12.957830687] before that cap. The uncapped 13.14356 is a raw sensitivity.
- QFIX.md:216 / SESSION25_RESULTS.md:1086 “1.038 at the plateau” is REFUTED at its printed precision: the exact q→infinity limit of 2 log10(C_T(486)/C_T(3)) is [1.037481305,1.037481306], rounding to 1.037. The 6.365 at q=12 is [6.365045455,6.365045456]. This is the effect of changing |N_S| alone with the three-coefficient reading already imposed; it is NOT a calculation of removing BOTH clauses called (H2). STAR_CONST.md:443–444 explains why restoring one common C_V changes the source constant too. The full conditionality does not “dissolve” from this one-parameter comparison.

QFIX.md:438 says 1.690 becomes 2.037 on restoring Lambda. That comparison also changes the endpoint: EPS1_EXEC.md:443–455 uses q=11 through q=100, giving [1.690373832,1.690373833] with its printed C_T inputs. The same finite endpoints with Lambda restored give [1.993868544,1.993868545], i.e. 1.994; [2.037035078,2.037035079] is q=11 through the true scalar limit. “2.037” is CONFIRMED only with the changed endpoint explicitly stated, REFUTED as solely the Lambda correction over the old table.

QFIX.md:379–385's +1.610 and 3.244 are CONFIRMED for its unrounded q=1000 cutoff. For the actually proposed two-significant-digit bound 3.8e-43, the lowering is [3.246291206,3.246291207], i.e. 3.246. At q=100, the proposed 3.5e-43 is ABOVE its own computed ceiling [3.495027493,3.495027494]e-43; a safe two-significant-digit value is 3.4e-43. A rigorous sufficient cutoff must round downward.


The independent q arithmetic output (enclosing rational decimals, not source-script output):

```text
cs [411.922970884, 411.922970885]
cg [5699.632830341, 5699.632830342]
B4 [43.948619310, 43.948619311]
B8 [1931.481139315, 1931.481139316]
q 8 CT [8.245142, 8.245143]e14 CD [7.613385, 7.613386]e17 cut [3.667251444, 3.667251445]e-49 margin [-52.664010533, -52.664010532]
q 11 CT [9.773761, 9.773762]e12 CD [7.743853, 7.743854]e15 cut [3.544720951, 3.544720952]e-45 margin [-36.723045077, -36.723045076]
q 12 CT [5.288348, 5.288349]e12 CD [4.051788, 4.051789]e15 cut [1.294800080, 1.294800081]e-44 margin [-34.472562415, -34.472562414]
q 32 CT [1.454322, 1.454323]e12 CD [8.888766, 8.888767]e14 cut [2.690377944, 2.690377945]e-43 margin [-29.202120111, -29.202120110]
q 100 CT [1.396001, 1.396002]e12 CD [7.798711, 7.798712]e14 cut [3.495027493, 3.495027494]e-43 margin [-28.747570901, -28.747570900]
q 1000 CT [1.385947, 1.385948]e12 CD [7.456241, 7.456242]e14 cut [3.823458095, 3.823458096]e-43 margin [-28.591547947, -28.591547946]
q None CT [1.385090, 1.385091]e12 CD [7.420609, 7.420610]e14 cut [3.860265105, 3.860265106]e-43 margin [-28.574904762, -28.574904761]
qlever8 [24.089105770, 24.089105771]
qlever11 [8.148140315, 8.148140316]
qlever12 [5.897657652, 5.897657653]
live HW qlever [12.044552885, 12.044552886]
q32cost [0.627215348, 0.627215349]
q100cost [0.172666138, 0.172666139]
q1000cost [0.016643184, 0.016643185]
Pmax/Pct plateau raw gain [13.143561886, 13.143561887]
Pmax/Pct gain after epsilon cap [12.957830686, 12.957830687]
QFIX gain vs EPS1_EXEC 9.38 [1.610253496, 1.610253497]
QFIX gain vs precise9.384951 [1.610024319, 1.610024320]
forced lowering at q1000 [3.243618467, 3.243618468]
forced lowering at rounded3.8 [3.246291206, 3.246291207]
q12energyshortfall [9.427744169, 9.427744170]
qinfenergyshortfall [6.478915343, 6.478915344]
spread q11to100 new [1.993868544, 1.993868545]
spread q11toinf new [2.037035078, 2.037035079]
spread q12toinf new [1.474414413, 1.474414414]
H2 epsilon-cut loss q=12 [6.365045455, 6.365045456]
H2 epsilon-cut loss q=100 [1.454093279, 1.454093280]
H2 epsilon-cut loss q=None [1.037481305, 1.037481306]
CD/ceiling q=11 [1.155799046, 1.155799047]
CD/ceiling q=12 [0.604744600, 0.604744601]
tpr need [9.522489170, 9.522489171]e-35
CD ceiling [1.781192096, 1.781192097]e13
CD ceiling ratio printed [1.779706976, 1.779706977]
CD ceiling ratio derived old [1.778656140, 1.778656141]
0.080 CT room [0.079838769, 0.079838770]
0.578 CT room [0.578406028, 0.578406029]
1.690 old spread finite100 [1.690373832, 1.690373833]
old lower-bound q8 loss [-2.761024549, -2.761024548]
actual old q8 loss [-4.385756275, -4.385756274]
old noH2 q12 loss [6.365008867, 6.365008868]
q theta_G versus tSUP inf crossover [2.128874338, 2.128874339]e25
fixed epsstar q=12 thetaeps [1.570082266, 1.570082267]e-39 cut UPPER [1.104706027, 1.104706028]e-44 margin UPPER [-34.748386392, -34.748386391]
fixed epsstar q=1000 thetaeps [2.088557437, 2.088557438]e-39 cut UPPER [1.469503884, 1.469503885]e-44 margin UPPER [-34.252690332, -34.252690331]
fixed epsstar q=None thetaeps [2.095808383, 2.095808384]e-39 cut UPPER [1.474605632, 1.474605633]e-44 margin UPPER [-34.246669733, -34.246669732]
fixed epsstar q1000 gain over EPS1cut [0.194738723, 0.194738724]
fixed epsstar q1000 lowering [4.658904064, 4.658904065]
q1000 epsstar needed exact [2.914094417, 2.914094418]e-36
```

### F6 — REFUTED: “1.696 decades” is not the spread of the four a_eta values

Targets: SESSION25_RESULTS.md:378; SYMBOLS.md:719–734,876–878; ARS_FIX.md:497–509. Claim status: PROVEN counterexample to a finite four-form spread.

At N=2 and the Gaussian illustrative kappa=1, the comparison of 1/(2N) with 49/(256*sigma_*^2), sigma_*^2=38, is indeed

    log10[(1/4)/(49/9728)] = log10(2432/49)
       in [1.695767490,1.695767491].

But the four-form table includes a_k/16. PLD.md:42 fixes its c_1=1/117 and PLD.md:196 gives a_k=c_1^(2k)/(2N) for kappa>=0.01. Thus the ratio of the bare coefficient to this listed coefficient is 16*117^(2k), with spread

    S(k) = log10(16) + 2k*log10(117).

At k=1, S lies in [5.340491706,5.340491707]; each additional level adds [4.136371723,4.136371724]. The spread is unbounded over k, not 1.696. Moreover PLD.md:276's (PLD-i) implication raises the probability base to |A|/16, so the claimed a_d*eta^2 form omits that /16 when interpreted in the same per-plaquette currency. These are bounds under different hypotheses and measures, not four interchangeable values of one universal coefficient. PLD.md:341–343 explicitly says sigma_*^2=N(1+18/kappa) is a Gaussian instance, not an established SU(N) variance.

### F7 — REFUTED: ARS_BIND's “exact” correction changes DXprime

Targets: SESSION25_RESULTS.md:578,599–601; ARS_BIND.md:333–359; checks/ab1_margins.py:25–26,123–138.

The script sets theta=1/24 and DXp=2.5e-152. ARS_FIX.md:275, REVIEW_SF_S7.md:203 and QFIX.md:257 instead use 2.456e-152. Consequently:

- +63.619266641… is correct at the script's 2.5 benchmark, but at the common 2.456 benchmark the same optimistic a_0 gives [63.626978288,63.626978289].
- RS-lin's [61.424351291,61.424351292] becomes 61.416639644… at 2.5; both round to +61.42. Equal two-digit headlines conceal different denominators.
- The bare breach is [-15.617074076,-15.617074075] at 2.456, not the claimed “exact” -15.6248 correction; -15.6248 uses 2.5.
- The zero-margin C_Omega is [4.140702944,4.140702945]e15 at 2.456, versus approximately 4.2149e15 at 2.5. ARS_BIND.md:359–361's attribution to carrying a rounded -15.617 is false. The discrepancy is log10(2.5/2.456), not rounding error in that margin.

All four source-script arithmetic checks can pass their loose tolerances while this currency switch survives. F2 still prevents interpreting either positive a_0 benchmark as a certified lower clearance.

### F8 — CONFIRMED arithmetic; scope corrections for gains, minima and conversion losses

The exact bare models at d=4, L=3 are

    a_Q(e,N) = e^4 / [2N*(4608N)^2],
    a_K(e,N) = e^2 / (2N*117^2),
    a_J(e,N) = e^2 / [2N*(2304N)^2*81].

The KN gain a_K/a_Q is 2log10(4608N/(117e)), with the four requested intervals in the final table. The old integer “92” is reproducible by rounding at TWO mismatched baselines, (proposed e,N=2) and (proposed e,N=3); it is not reproducible at the headline e=6.7e-40. KN_ADOPT.md:277 says “three” while displaying only two; the ledger's “two” is the supported count in this parameter set.

The net per-cube KN/joint ratio is 81*(2304N)^2/(625*117^2): exactly 21233664/105625 at N=2, 47775744/105625 at N=3. These give [201.028771597,201.028771598] and [452.314736094,452.314736095], and logs [2.303258218,2.303258219], [2.655440736,2.655440737]. Bare 1551.148 is a different comparison, missing 81/625. The 79.837305384… old-joint improvement splits exactly as log10(4/e^2)+log10(625/81), i.e. [78.949910385,78.949910386]+[0.887394998,0.887394999]. There is no conflict once all THREE eta symbols are kept.

In particular, SESSION25_RESULTS.md:41–43's present-tense “RLARGE l.65 is FALSE” is REFUTED as written: the current eta_RS/eta_q is e/2, so its inequality is true at these inputs. The factor 512/13 belongs to the PROPOSED eta_KN, not the current eta_RS. KN_ADOPT.md:309 itself gives the correct current ratio. A new threshold requires changing that consumer; it does not falsify the old statement at its own definition.

Kernel minimum: from RLARGE.md:1020 and KN_ADOPT.md:545, after the proposed substitution

    a_RS_new = (e^2/N)*min{1/27378, kappa/256}.

Thus the branch boundary is kappa=128/13689, independent of e and N. All four full gain figures require kappa at least that value. At N=2 below it, provided the OLD branch remains plaquette-limited, the gain becomes [84.169725357,84.169725358]+log10(kappa). If kappa is so tiny that the old branch also becomes kernel-limited, even this expression stops applying; the old threshold is kappa=e^2/663552. The advertised “84.170+log kappa below it” is not an all-kappa formula. No value of kappa was independently established by these arithmetic checks.

F-mono: log10(2) is [0.301029995,0.301029996], and the displayed -15.918/+66.222 (also -18.714/+63.427 per cube) are correct for the conservative replacement a/100 -> a/200. They are NOT an exact mandatory loss. KN_ADOPT.md:377–380 itself proves a SUFFICIENT inequality using 1/g^2-R >= 1/(2g^2). For fixed R the exact displayed model is g^2 <= a/(100+aR), also subject to g^2 <= 1/(2R). At R=0 the loss is zero; the common worst-case safety loss is at most log10(2) when the old comparison includes the same standing cap. The actual exact gain need not cancel this R-dependent loss. RLARGE.md:114–116 also says the live HW defect price does not perform this conversion.

### F9 — REFUTED as a factor on C_1: ×287; CONFIRMED scoped ×9, ×1.78, ×1.16

Targets: SESSION25_RESULTS.md:392–397,1055–1079; SYMBOLS.md:514–532,664–666; EPSSTAR.md:216–218.

- C_1=20 -> c_g=5699.632830341… has factor [284.981641517,284.981641518], i.e. approximately 285, not 287. The underlying 236.9*C_1 product is [1350243.017507994,1350243.017507995], not 1.348e6. A factor approximately 287 DOES result on comparing that new product with the prematurely rounded old product 4700: [287.285748405,287.285748406]. The ledger compresses these different comparisons into a factor on C_1 itself. Correct same-precision old product: 236.9*20=4738.
- HW.md:604's approximate coefficient uses theta_SUP=1e-8/C_D^2 although SQ.md:216 corrects it to 3e-8/C_D^2. The unrounded change is exactly times 9, from [5.562477750,5.562477751]e-23 to [5.006229975,5.006229976]e-22, divided by C_D^4. Relative to the PRINTED 5e-23 it is [10.012459950,10.012459951], not exactly 9. This is the threshold-limited upper coefficient; HW.md:603–604 explicitly requires epsilon_1 >= Cprime*tau_flat, whereas the headline tiny-epsilon branch is epsilon-limited. There is no ninefold improvement of the latter.
- EPSSTAR.md:521,525,527 gives t_need=2e*sqrt(5.05e9*C_3); at e=6.7e-40, C_3=1 this is [9.522489170,9.522489171]e-35, giving C_D<= [1.781192096,1.781192097]e13. The earlier printed 3.17e13 is too high by [1.779706976,1.779706977], so ×1.78 is CONFIRMED. “Exactly sqrt(10)” describes the lost factor inside the ideal radical, not the ratio of the rounded 9.522489… and 3.01 numbers.
- QFIX.md:190's C_D(11)/6.7e15 lies in [1.155799046,1.155799047], confirming ×1.16 for c_N=2 and the restored Lambda(q). This excludes q=11 for this consumer at the unlowered epsilon, not structurally for every c_N or threshold.

### F10 — CONFIRMED conditional FACEB prices; REFUTED 81.7

Targets: SESSION25_RESULTS.md:452–461,980–984; FACEB.md:475–537. Claim status: PROVEN arithmetic; CONDITIONAL currency conversion; GAP for a programme break-even.

Write D=-log10(2.456e-152) and ell=log10(3). Then P(k)=(2k-3)ell, k_D=(D/ell+3)/2, k_e=(-log10(6.7e-40)/ell+3)/2. Independently enclosing ell and D yields:

| expression | rational decimal enclosure |
|---|---|
| ell | [0.477121254,0.477121255] |
| D | [151.609771637,151.609771638] |
| P(10) | [8.111061330,8.111061331] |
| P(42) | [38.646821632,38.646821633] |
| P(183.4) | [173.576712467,173.576712468] |
| P(355.6) | [337.897272592,337.897272593] |
| k_D | [160.379708394,160.379708395] |
| k_e | [42.552379043,42.552379044] |
| doubled-currency k | [80.939854197,80.939854198] |
| P(183.4)-D | [21.966940829,21.966940830] |

For the doubled convention solve 2(2k-3)ell=D, giving k_double=(k_D+3/2)/2, not 81.7. The ledger's corrected 80.940 is CONFIRMED.

Currency is decisive: FACEB.md:475–478 itself has a homogeneous inequality c(k)*eta^2 <= C_SR*eta^2. Cancelling eta^2 shows that shrinking eta cannot repair its k-dependence. The conversion to a cutoff instead uses the DISTINCT self-map inequality C_SR*3^(2k-3)*eta^2<=eta. That requires assumption X1, and comparing eta with g^2 requires X2; neither follows from arithmetic. Including the suppressed outputs changes the first break-even to

    k_D(C_Omega,C_SR)=3/2+
        [D+log10(C_Omega)-log10(C_SR)]/[2log10(3)].

For eta proportional to g, replace the denominator by 4log10(3) and the numerator's log10(C_SR) by 2log10(C_SR). The numbers 160.380 and 80.940 are not fixed programme thresholds. The input k=183.4 is a courtesy real value taken from a discarded n_sharp convention (ARS_FIX.md:488–494), not a derived admissible integer RG depth.

“<=0.90 decades left” (ledger:452, FACEB.md:677) uses log10(8) in [0.903089986,0.903089987]. 0.90 is an acceptable approximate display but not a safe upper bound; 0.904 is a safe three-decimal upper display for the factor-eight model. Whether eight bounds every relevant response is NOT-VERIFIED here. No such constant repairs an exponential-in-k deficit.

### F11 — Remaining decade figures, precision, and units

Targets: SESSION25_RESULTS.md:212–226,245–263,397,544–546,923; EPS1_EXEC.md:389–481; TAUFLAT.md:192–213. Claim status: CONDITIONAL for model prices; PROVEN for the explicit logarithmic identities.

Let Delta=log10(6.7e-40/9.38495112638e-45). Its enclosure is [4.853642787,4.853642788]. Hence 2Delta, 3Delta, 4Delta are [9.707285574,9.707285575], [14.560928362,14.560928363], [19.414571149,19.414571150]. The quoted 9.707/14.561/19.415 are CONFIRMED algebraic powers at those inputs. The epsilon^-3 consumer itself remains ARGUED in EPS1_EXEC.md:545–554; multiplying Delta by three does not prove that consumer's analytic estimate. PLD.md:995's 2m_*g/epsilon RISES by Delta at fixed g, while epsilon/g loses Delta; the signed correction is CONFIRMED.

At DXprime=2.456e-152 and C_Omega=1, log10(epsilon/g) is [36.630960621,36.630960622] before and [31.777317834,31.777317835] after. The source's separate use of rounded g=1.57e-76 accounts for its extra decimal differences; both reproduce 36.63/31.78. These are decades of epsilon/g, not g^2 ceiling clearance.

EPS1_SWEEP.md:455's 9.38495112638e-45 exceeds sqrt(3.52309230578e-88/4), whose enclosure is [9.384951126377803,9.384951126377804]e-45. A downward 12-decimal-significand display is 9.38495112637e-45. It does not change any three-decimal decade figure. But TAUFLAT's own script uses C_D=900*5.288e12=4.7592e15 (checks/tf1_tau.py:63,67,109), giving eta_flat in [3.523098101594866,3.523098101594867]e-88, not the later twelve-digit imported value. With that rational chain the energy shortfall is [9.707284860,9.707284861]. If one literally instead fixes C_D=4.76e15 as TAUFLAT.md:196 displays, eta_flat is [3.520730229309,3.520730229310]e-88 and the shortfall is [9.707576847,9.707576848], which rounds to 9.708. Thus sub-millidecade “exactness” cannot be attached to the rounded C_D label. QFIX's restored Lambda and unrounded C_T give [9.427744169,9.427744170], explaining 9.428 under its explicitly different chain.

The old +1.157 is 2log10(5.288e12/1.396e12)=[1.156812056,1.156812057], using q=100 as the endpoint, not infinity. The -2.761 at q=8 substitutes the LOWER BOUND C_T>=1.27e14 as equality. It is an upper bound on the relative epsilon cutoff, not the actual q=8 value. Using the computed C_T(q) with the same frozen-Lambda convention gives [-4.385756275,-4.385756274] relative to q=12. The refreshed QFIX chain changes Lambda as well.

The 0.080 and 0.578 figures are log10(5.288e12/4.4e12) in [0.079838769,0.079838770] and log10(5.288e12/1.396e12) in [0.578406028,0.578406029], respectively: different endpoints. Their doubled cutoff sensitivities are approximately 0.160 and 1.157 (1.156 is a downward coarse truncation, not the nearest three-decimal rounding). Neither is the remaining optimisation at fixed large q: the latter comparison already spends the q lever.

The “52-decade tau_flat error” is an ENERGY-threshold error. With the script's C_D=4.7592e15, tau_R=2.75e-15, Cprime=53 and c_flat=1/640, log10(eta_A/eta_B) lies in [52.077008938,52.077008939]. The tau ratio has HALF that log: [26.038504469,26.038504470]. SESSION25_RESULTS.md:397 and SYMBOLS.md:457 misname that currency even though SYMBOLS.md:887–889 calls it eta_flat elsewhere.

The four-value gain spread 0.555 is [0.555457836,0.555457837], for extrema 6.7e-40 and 1.27e-39; including the proposed epsilon gives [10.262743411,10.262743412], explaining the discarded 10.263. The ledger says the reviewer “averaged” five rows (line 226); checks/ra1b_margins.py:103–105 computes a range, not an average.

The “30.4 decades inside (C7)” (ledger:218; REVIEW_ARS_EPS_S1.md:408) is NOT a justified window. The old, incorrect product condition c_plus*C_Omega<=1.5e46 would give [30.559017183,30.559017184]-log10(c_plus) between its upper endpoint and the bare reversal. The corrected ratio condition c_plus/C_Omega<=1.5e46 gives a LOWER bound on C_Omega, no upper endpoint. Thus no constant 30.4 window follows from (C7).

Finally, the pole sweep labels are REFUTED. The original epsilon list 10^-1,...,10^-4 spans THREE decades, not four (ledger:923). Six points 10^-1,...,10^-6 span FIVE decades, not six (ledger:546; TUNIF.md:549; checks/tu1b_pole.py:12–14,22). A pure A/epsilon pole grows exactly 1000 over the first interval and satisfies a >=1000 test. A positive regular part B makes (10000A+B)/(10A+B)<1000. The original “unsatisfiable by the truth” diagnosis is false; numerical outcomes for the actual seeded field were not independently rerun here.

### F12 — Check power: what the audited gates can and cannot decide

Review verdicts below attach to test capability, not to unexecuted source-run outcomes. Source scripts using float or Decimal were inspected, never executed.

| gate/source | verdict and discriminating limit |
|---|---|
| ar1_margins.py:24,243–245 | REFUTED as independent recovery of c_1: c_1 is defined as the reciprocal making the tested product 1/2. An altered geometric input changes both sides together. |
| ar1_margins.py:269–271; ar1c_knrebuild_posthoc.py:52–59,77–90,95–99 | REFUTED as executable checks: SAME-CONSTANT, identity, REPRODUCES and CHART-AVAILABLE labels are printed without the claimed predicate. The mathematical identities can be checked by hand; printed labels add no evidence. |
| kn1_gain.py:25–37,81–109 | CONFIRMED capable of catching a wrong epsilon or c_1; NOT-VERIFIED as a live-branch certificate because kappa=1 is hard-coded and the delta_0 cap is omitted. At the two tiny inputs the latter omission is harmless; varying arbitrary N or kappa is a different test. |
| ra1b_margins.py:103–116,121–145 | CONFIRMED as arithmetic input/packing comparisons: replacing 625 by 81 changes the answer by log10(625/81). NOT-VERIFIED as proof that either probability exponent is available. |
| ab1_margins.py:25–26,123–138 | REFUTED as a certificate of actual live clearance: a_live omits a_A, theta is its forbidden upper endpoint, and DX is changed. The sign test can fail, but it tests the wrong completion of the hypotheses. |
| ab1_margins.py:140–153 | CONFIRMED log-factorisation identity, not independent evidence for the route: both total and parts use the same two thresholds and packing constants. |
| qf1_q.py:144–156,262; qf1_criteria.md:65,69 | REFUTED as proof of a global supremum or all-q monotonicity. A finite grid and one positive value at q=10^6 do not test q→infinity, omitted minima, or output-dependent constraints. |
| qf1_q.py:233–276 / QF1-6 | CONFIRMED as a wiring control only. Freezing both q-dependent inputs forces a zero curve by construction; it cannot discover a missing q-dependent constraint such as theta_G or the theta_epsilon minimum. |
| qf1_criteria.md:71 / QF1-7; fb1_bianchi.py:212–243; ar1_margins.py:410–419 | REFUTED as exact or independent certification: repeated evaluation at two Decimal precisions shares formulas and constants, gives no rigorous transcendental remainder, and cannot detect a currency error. FACEB A7 omits the doubled-currency 81.7 row completely. |
| qf1_criteria.md:72–73 / QF1-8,9 | CONFIRMED capable of detecting the displayed square-root error and distinguishing integer powers on the chosen rows. NOT-VERIFIED as validation of a_RS's live use; all fitted rows descend from that same historical model. |
| ee1_exec.py:233–244 | CONFIRMED that different exponents can fail the arithmetic check; power agreement cannot prove that the Cauchy consumer has that power or settle the free q baseline. |
| sy1_symbols.py:112–146 | CONFIRMED nontrivial window/coefficient comparison at specified constants; REFUTED “exact rational only” if applied to its decision code, which uses sqrt(float(...)) and float comparisons. It does not test the four-form a_eta spread. |
| tu1b_pole.py:19–23 | REFUTED as a simple-pole discriminator: a double pole gives every successive ratio 100, satisfies ratios>=9 and last>=9.9, and can have a constant corrected sequence. The stated approach-to-10 condition is absent. |

The quoted agreement residuals “8e-48 decades”, “0.000000 decades” and “10^-4 decade” are not interchangeable with proof. The first two source-run residuals are NOT-VERIFIED here; exact algebra predicts zero for their shared definitions. The 625 reconciliation is independently CONFIRMED: the exact margin difference is log10(625) in [2.795880017,2.795880018]. It does not establish an applicable probability bound.

There is also a subtle formal-limit defect even before restoring the omitted minima. Let h=4/q, B=27c_s>0. The curvature expression used by QFIX contains

    f(h)=(1-h)(4h)^(h/(1-h))*B^(1/(1-h)).

Its exact logarithmic derivative is log(4hB)/(1-h)^2. As h decreases to zero,

    f(h)=B+B*h*log(h)+O(h).

Its coefficient in C_T is strictly positive; every other term and Lambda has an ordinary O(h) expansion. Thus C_D(h)=C_D(0)+A*h*log(h)+O(h), A>0, so for sufficiently small positive h, C_D(h)<C_D(0). The scalar objective approaches the printed limiting value from ABOVE eventually. The finite grid cannot justify its exact supremum claim even for its own uncapped t_pr model. This changes no shown rounded finite-q figure; the size/location of the formal overshoot is NOT-VERIFIED. The physical-minimum obstruction in F4 is much more material.

### F13 — Citation drift and source boundary

KN_ADOPT.md:122,139–144,531 and ledger:15 point to PROOF.md:1754 for the kernel average. That line currently belongs to a seam discussion; the string “Decision 4: the RG kernel” is at PROOF.md:1806–1810. The transporter definition formerly cited as line 712 is now at 764, and S4prime at 766. KN_ADOPT's / ledger's pointer to PROOF line 84 for the 1551 correction is stale: the corrected factor appears at line 94. The [S24-flag 6] paragraph is currently at line 73; its newly added +63.619 assertion inherits F2/F7, so it is not exempt because it is in PROOF.

No git operation was performed. No snapshot or audit ledger was read. The two discretionary files were the methodology and project review skill; all other reads were the ledger or narrowly selected owning-source/check regions for the figures above. The ledger grew from 1095 to 1211 lines during this review. The added T55-O section has no new decade quantity; the final provenance section marks the earlier work provisional. This report audits the numerical and logical content independently; model labels and banked statuses are not evidence. Later additions beyond that inventory are outside this review.

## Independent arithmetic certificate

All displayed intervals in this report have rational decimal endpoints rounded OUTWARD. They enclose the stated exact rational benchmark inputs; they do not claim that approximate physical/analytic source constants are known to that precision.

For 1<=r<=2, set z=(r-1)/(r+1), 0<=z<=1/3. With m=100,

    ln(r)=2*sum(j=0..99,z^(2j+1)/(2j+1))+R,
    0<=R<=2*z^201/[201*(1-z^2)].

For arbitrary positive rational x, write x=2^k*r and add k*ln(2). Divide by an independently enclosed ln(10). Roots use integer square-root brackets. Exponentials first reduce to 0<=u<=1/2; after Taylor degree 100 their positive tail is at most (u^101/101!)/(1-u/102), then square back. Every elementary operation is rounded outward to 55 significant decimal digits using integer floor/ceil, never a floating operation.

For B(m)=product(j>=1,(2^j-1)^(m/2^j)), 160 log terms suffice with explicit tail

    0 < remaining log tail < m*ln(2)*(162)/2^160.

This independently handles the nonrational q powers and the infinite product rather than trusting precision agreement.

One implementation correction is disclosed: the first attempt formed an enormous exact remainder rational and hit Python's integer-to-string safety limit before producing any result. The final implementation instead bounds that same remainder using the already enclosed positive power; the bound is still outward. No failed run's result was recorded as a verdict. The independent sanity assertions ln(10)/ln(10) enclosing 1, log10(2)+log10(5) enclosing 1, and the squared sqrt(2) brackets all succeeded.

The following self-contained Python uses only integers, Fraction and isqrt. It is embedded here because the authorised write scope excludes auxiliary check files.


```python
from fractions import Fraction as F
from math import isqrt
from functools import lru_cache
P=55
def pow10(n):
    return F(10**n) if n>=0 else F(1,10**(-n))
def decade(x):
    x=abs(x)
    if not x:return 0
    k=len(str(x.numerator))-len(str(x.denominator))
    while x < pow10(k):k-=1
    while x >= pow10(k+1):k+=1
    return k
def roundout(x,up=False):
    if not x:return F(0)
    step=pow10(decade(x)-P+1)
    y=x/step
    n=-((-y.numerator)//y.denominator) if up else y.numerator//y.denominator
    return n*step
class I:
    def __init__(self,l,h=None):
        if isinstance(l,I):self.l,self.h=l.l,l.h;return
        self.l=roundout(F(l)); self.h=roundout(F(l if h is None else h),True)
        assert self.l<=self.h
    def __add__(a,b):
        b=I(b);return I(a.l+b.l,a.h+b.h)
    __radd__=__add__
    def __neg__(a):return I(-a.h,-a.l)
    def __sub__(a,b):return a+-I(b)
    def __rsub__(a,b):return I(b)+-a
    def __mul__(a,b):
        b=I(b);v=[a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h];return I(min(v),max(v))
    __rmul__=__mul__
    def inv(a):
        assert a.l*a.h>0
        return I(1/a.h,1/a.l)
    def __truediv__(a,b):return a*I(b).inv()
    def __rtruediv__(a,b):return I(b)*a.inv()
    def __pow__(a,n):
        assert isinstance(n,int)
        if n<0:return (a.inv())**(-n)
        y=I(1)
        for _ in range(n):y=y*a
        return y
    def out(a,n=9):
        s=10**n
        l=(a.l*s).numerator//(a.l*s).denominator
        h=-((-a.h*s).numerator//(-a.h*s).denominator)
        def fmt(k):
            sign='-' if k<0 else '';v=abs(k)
            return sign+str(v//s)+'.'+str(v%s).zfill(n)
        return '['+fmt(l)+', '+fmt(h)+']'
    def sci(a,n=9):
        k=decade(max(abs(a.l),abs(a.h)))
        return (a/pow10(k)).out(n)+'e'+str(k)
def atomlog(x):
    assert 1<=x<=2
    z=(x-1)/(x+1);zz=z*z
    # 100 terms, exact positive tail <= 2 z^(201)/(201(1-z^2)).
    t=I(z);s=I(0)
    for j in range(100):
        s=s+t/F(2*j+1)
        t=t*zz
    r=2*t.h/(201*(1-zz))
    return 2*s+I(0,r)
LN2=atomlog(F(2))
def _ln(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    r=x/(F(2)**k)
    while r<1:r*=2;k-=1
    while r>2:r/=2;k+=1
    return atomlog(r)+k*LN2
def ln(x):
    x=I(x)
    return I(_ln(x.l).l,_ln(x.h).h)
LN10=ln(10)
def lg(x):return ln(x)/LN10
def _exp(x):
    if x<0:return _exp(-x).inv()
    k=0
    while x>F(1,2):x/=2;k+=1
    s=I(1);t=I(1)
    for j in range(1,101):
        t=t*x/j;s=s+t
    # after degree 100, consecutive omitted-term ratios <= x/102.
    nextterm=t*x/101
    s=s+I(0,nextterm.h/(1-x/102))
    for _ in range(k):s=s*s
    return s
def ex(x):
    x=I(x);return I(_exp(x.l).l,_exp(x.h).h)
def power(x,r):return ex(ln(x)*F(r))
def _sqrt(x):
    if not x:return I(0)
    k=decade(x)//2
    scale=pow10(P-k)
    y=x*scale*scale
    n=isqrt(y.numerator//y.denominator)
    return I(F(n)/scale,F(n+1)/scale)
def sqrt(x):
    x=I(x);assert x.l>=0
    return I(_sqrt(x.l).l,_sqrt(x.h).h)
def show(label,v):print(label,I(v).out())
E=I('6.7e-40');EP=I('9.38495112638e-45');DX=I('2.456e-152')
def quad(e,N=2):return (e/(512*N*9)*e)**2/(2*N)
def linear(e,N=2):return (e/117)**2/(2*N)
def joint(e,N=2):return (e/(256*N*9))**2/(2*N*81)
A0=E**2/(24*640*53**2)

T=(sqrt(387)-18)/4
K=I(F(7,8))-T
CS=8*(9/T+2)/K
CG=8*310/K+272
def Bbase(J=160):
    s=I(0)
    for j in range(1,J+1):
        s=s+ln(2**j-1)/2**j
    return s+I(0,(LN2*(J+2)/2**J).h)
LB=Bbase()
@lru_cache(None)
def Bt(m):return ex(m*LB)
def qparams(q):
    if q is None:return F(0),F(1),I(1)
    h=F(4,q);a=1/(1-h)
    return h,a,(1-h)*power(4*h,h/(1-h))
@lru_cache(None)
def CT(q,ns=3,pmax=True,cs_override=None):
    m=19615;h,a,ct=qparams(q);cs=CS if cs_override is None else I(cs_override)
    ac2=(1+sqrt(6))**2*(ct*power(27*cs,a)+4096*CG)/(F(3,4)-F(1,4*m))/m**2
    s1=power(36*cs*ns,a)/2
    s2=ac2/2
    s3=288*(CG+18*(ns*cs*power(64,-2+2*h)+F(1,36*m)))
    return sqrt(6)*I('175.8')*Bt(F(8) if pmax else 4*a)*(s1+s2+s3)
@lru_cache(None)
def Lam(q):
    h=F(0) if q is None else F(1,q)
    return 4*power(2,2+4*h)*(I('4.94')+I('3.34')*power(32,h))
@lru_cache(None)
def chain(q,ns=3,pmax=True):
    ct=CT(q,ns,pmax)
    cd=2*(I('1.011')*2*Lam(q)*ct+I('46.8'))
    tpr=1/(I('3.31e7')*cd**2)
    cut=tpr/(2*sqrt(I('5.05e9')))
    return ct,cd,tpr,cut
def qm(q,ns=3,pmax=True):
    cut=chain(q,ns,pmax)[3]
    e=cut if cut.h<E.l else E
    return lg(quad(e)/(100*DX))
def theta_eps(q):
    r=F(0) if q is None else F(1,q)
    return I('1.12e-37')/(16*I('3.34')*power(32,r))
for N in [2,3]:
 for lab,e in [('today',E),('proposed',EP)]:
  show('gain '+lab+' N='+str(N),lg(linear(e,N)/quad(e,N)))
for lab,e in [('today',E),('proposed',EP)]:
 for mode,aa in [('quadratic',quad(e)),('KN',linear(e)),('RSlin-percube',joint(e))]:
  show(lab+' '+mode+' bare-margin',lg(aa/(100*DX)))
  if mode!='RSlin-percube':show(lab+' '+mode+' /625-margin',lg(aa/(62500*DX)))
show('log625',lg(625));show('log625over81',lg(F(625,81)))
show('RSlin-gain-over-old',lg(joint(E)/(quad(E)/625)))
show('threshold-ratio contribution',lg(4/E**2))
for N in [2,3]:
 show('KN-over-RSlin N='+str(N),lg((linear(E,N)/625)/joint(E,N)))
 print('ratio N='+str(N),((linear(E,N)/625)/joint(E,N)).out())
show('live-benchmark DX2.456',lg(A0/(100*DX)))
show('live-benchmark DX2.5',lg(A0/(I('2.5e-150'))))
show('live vs RSlin',lg(A0/joint(E)))
show('counterexample theta=1e-70',lg((E**2/(I(10)**70*640*53**2))/(100*DX)))
show('Delta eps',lg(E/EP))
for n in [2,3,4]:show(str(n)+'Delta',n*lg(E/EP))
show('floor36.63',lg(E/sqrt(DX)))
show('floor31.78',lg(EP/sqrt(DX)))
show('spread-gain-foureps',2*lg(I('1.27e-39')/E))
show('spread-fiveeps',2*lg(I('1.27e-39')/EP))
show('kappa-offset',lg((E**2/(256*2))/quad(E)))
show('log2',lg(2))
print('C_Omega reversal bare',(100*DX/quad(E)).sci())
print('C_Omega reversal percube',(62500*DX/quad(E)).sci())
show('30.4 bare window',lg(I('1.5e46')/(100*DX/quad(E))))
show('aeta-spread N2 sigma38',lg(F(1,4)/F(49,256*38)))
show('aeta-spread N2 sigma37.2',lg(F(1,4)/F(49,256)*F('37.2')))

print('cs',CS.out());print('cg',CG.out());print('B4',Bt(F(4)).out());print('B8',Bt(F(8)).out())
for q in [8,11,12,32,100,1000,None]:
 ct,cd,tp,cut=chain(q)
 print('q',q,'CT',ct.sci(6),'CD',cd.sci(6),'cut',cut.sci(9),'margin',qm(q).out())
show('qlever8',qm(None)-qm(8));show('qlever11',qm(None)-qm(11));show('qlever12',qm(None)-qm(12))
show('live HW qlever', (qm(None)-qm(8))/2)
show('q32cost',qm(None)-qm(32));show('q100cost',qm(None)-qm(100));show('q1000cost',qm(None)-qm(1000))
show('Pmax/Pct plateau raw gain',8*lg(Bt(F(8))/Bt(F(4))))
show('Pmax/Pct gain after epsilon cap',lg(quad(E)/(100*DX))-qm(None))
show('QFIX gain vs EPS1_EXEC 9.38',lg(chain(1000)[3]/I('9.38e-45')))
show('QFIX gain vs precise9.384951',lg(chain(1000)[3]/EP))
show('forced lowering at q1000',lg(E/chain(1000)[3]))
show('forced lowering at rounded3.8',lg(E/I('3.8e-43')))
show('q12energyshortfall',2*lg(E/chain(12)[3]))
show('qinfenergyshortfall',2*lg(E/chain(None)[3]))
show('spread q11to100 new',2*lg(chain(11)[1]/chain(100)[1]))
show('spread q11toinf new',2*lg(chain(11)[1]/chain(None)[1]))
show('spread q12toinf new',2*lg(chain(12)[1]/chain(None)[1]))
for q in [12,100,None]:
 show('H2 epsilon-cut loss q='+str(q),2*lg(CT(q,486)/CT(q,3)))
for q in [11,12]:
 print('CD/ceiling q='+str(q),(chain(q)[1]/I('6.7e15')).out())
tpneed=2*E*sqrt(I('5.05e9'));cdceil=sqrt(1/(I('3.31e7')*tpneed))
print('tpr need',tpneed.sci());print('CD ceiling',cdceil.sci())
print('CD ceiling ratio printed',(I('3.17e13')/cdceil).out())
print('CD ceiling ratio derived old',(sqrt(1/(I('3.31e7')*I('3.01e-35')))/cdceil).out())
show('0.080 CT room',lg(I('5.288e12')/I('4.4e12')))
show('0.578 CT room',lg(I('5.288e12')/I('1.396e12')))
show('1.690 old spread finite100',2*lg(I('9.774e12')/I('1.396e12')))
show('old lower-bound q8 loss',2*lg(I('5.288e12')/I('1.27e14')))
show('actual old q8 loss',2*lg(CT(12)/CT(8)))
show('old noH2 q12 loss',2*lg(I('8.05e15')/I('5.288e12')))
print('q theta_G versus tSUP inf crossover',(I('1.46e-13')*8/chain(None)[2]).sci())
for q in [12,1000,None]:
 epscap=theta_eps(q)/(2*sqrt(I('5.05e9')))
 print('fixed epsstar q='+str(q),'thetaeps',theta_eps(q).sci(),'cut UPPER',epscap.sci(),'margin UPPER',lg(quad(epscap)/(100*DX)).out())
show('fixed epsstar q1000 gain over EPS1cut',lg(theta_eps(1000)/(2*sqrt(I('5.05e9')))/EP))
show('fixed epsstar q1000 lowering',lg(E/(theta_eps(1000)/(2*sqrt(I('5.05e9'))))))
print('q1000 epsstar needed exact',(16*I('3.34')*power(32,F(1,1000))*chain(1000)[2]).sci())

D=-lg(DX);LE=-lg(E);L3=lg(3)
show('DXdec',D);show('epsilondec',LE);show('log3',L3)
for k in ['10','42','160','183','183.4','355.6','356']:
 show('P('+k+')',(2*F(k)-3)*L3)
kd=(D/L3+3)/2;ke=(LE/L3+3)/2
show('kstar DX',kd);show('kstar epsilon',ke);show('kstar double',(D/(2*L3)+3)/2)
show('173.58 beyond DX',(2*F('183.4')-3)*L3-D)
show('at42 vs eps',81*L3-LE)
show('log8',lg(8))
for c in [F(1,4),F(1,64*117**2),F(1,4*38),F(49,256*38)]:
 print('aeta coeff',str(c))
show('spread k1 coefficient',lg(16*117**2))
show('per-level growth of spread',2*lg(117))
old=I('1e-8')**2/(640*53**2);new=I('3e-8')**2/(640*53**2)
print('HW old coefficient',old.sci());print('HW new coefficient',new.sci())
print('HW ratio displayed',(new/I('5e-23')).out());print('HW ratio unrounded',(new/old).out())
show('HW correction decades',lg(9))
cg=I('5699.632830341894211')
print('cg/20',(cg/20).out())
print('236.9*cg',(I('236.9')*cg).out())
print('ratio to displayed4700',(I('236.9')*cg/4700).out())
print('rounded pair 1.348e6/4700',(I('1.348e6')/4700).out())
etaold=I(F(1,640))*I('2.75e-15')**2/53**2
tp=1/(I('3.31e7')*I('4.76e15')**2)
etanew=I(F(1,640))*tp**2/53**4
show('52 gap exact',lg(etaold/etanew))
print('eta new actual published',etanew.sci(12));print('sqrt eta given12digits',sqrt(I('3.52309230578e-88')/4).sci(15))
show('9.707 energy from exactTAUFLAT',lg(4*E**2/etanew))
show('4.854 eps from exactTAUFLAT',lg(E/sqrt(etanew/4)))
show('5.153 clause factor',lg(2*sqrt(640*53**4)))
show('candidate unsafe energy decades',lg(4*EP**2/I('3.52309230578e-88')))
show('TAUFLAT 9.38496 unsafe energy',lg(4*I('9.38496e-45')**2/I('3.52309230578e-88')))
for lab,aa in [('old',quad(E)),('new',linear(E))]:
 show(lab+' shifted by log2',lg(aa/(200*DX)))
 show(lab+' cube shifted by log2',lg(aa/(125000*DX)))
show('N2 vs N3',2*lg(F(3,2)))
show('c1 power control 1.6258',2*lg(F(117,18)))
show('margin PLD corrected -17.313',lg(quad(E)/(100*DX))-lg(F(1,4)/F(49,256*38)))
print('exact route ratio N2',F((512)**2*81,13**2*625))
print('exact route ratio N3',F((768)**2*81,13**2*625))

```

Completion receipt: 2026-10-28 22:25:13 UTC. The embedded Fraction/isqrt certificate executed successfully and reproduced the principal displayed enclosures; 80 final table rows were checked for structure. SESSION25_RESULTS.md remained 1211 lines at the last inventory. No source script using float/Decimal was executed, and no file other than this deliverable was written.

**Single most dangerous NOT-VERIFIED item:** a quantitative lower bound for the actual live minimum `a=min{theta*c_pr*min(epsilon^2,t_pr^2),a_A}` at one jointly admissible choice of thresholds and output constants. In particular no inspected source establishes that `a_A` stays above the claimed suppression rate. A positive clearance computed from the upper endpoint theta=1/24 cannot settle this.

## Final figure-by-figure table

This table reports the claim in its **stated currency**. “Conditional arithmetic” means the formula was independently enclosed, not that its hypotheses are available. All file names below are relative to this lane directory. Common inputs are E=6.7e-40 (RLARGE.md:71–72, an upper-ceiling benchmark), E_p=9.38495112638e-45 (EPS1_SWEEP.md:455, a proposed and slightly upward-rounded bound), D=2.456e-152 (REVIEW_SF_S7.md:203), and the historical model N=2, L=3, A_d=9, kernel kappa=1 unless explicitly varied. Every D-based row freezes C_Omega=1 unless its formula says otherwise. Source inputs quoted approximately are treated as exact benchmark rationals only for this arithmetic audit.

| Figure / assertion | Verdict | Correct value or interval | Currency and claim status | Input / symbol provenance |
|---|---|---|---|---|
| +82.1406 | CONFIRMED | [82.140563603,82.140563604] | log10(a_K/a_Q), CONDITIONAL | E: RLARGE.md:72; eta_RS:64; eta_KN: KN_ADOPT.md:545; N=2 |
| +82.4927 | CONFIRMED | [82.492746121,82.492746122] | same conditional ratio, N=3 | same epsilon and c_1 sources; KN_ADOPT.md:269 |
| +91.8478 | CONFIRMED | [91.847849178,91.847849179] | same ratio at proposed E_p, CONDITIONAL | EPS1_SWEEP.md:455; KN_ADOPT.md:270,545; N=2 |
| +92.2000 | CONFIRMED | [92.200031696,92.200031697] | same ratio at E_p, CONDITIONAL | same sources; KN_ADOPT.md:271; N=3 |
| old “92”, two wrong pairings | CONFIRMED | both 91.847849… and 92.200031… round to 92; neither is today's value | coarse integer rounding only | KN_ADOPT.md:268–277; E vs E_p and N must both be named |
| 82/92 as a proved programme gain | REFUTED | no established programme gain; GAP | discarded joint-price currency | RLARGE.md:433–439,513–514,1020–1026 |
| +2.303 over an “already-proven route” | REFUTED | arithmetic [2.303258218,2.303258219]; route pricing remains CONDITIONAL | per-cube KN versus joint RS; GAP as established programme improvement | HIST.md:170,185–186,505–521; KN_ADOPT.md:545; N=2; 625 versus 81 |
| +2.655, N=3 partner | CONFIRMED | [2.655440736,2.655440737] | CONDITIONAL comparison only | same eta and packing definitions, N=3 |
| 1551× -> 201.029× / 452.315× | CONFIRMED | 21233664/105625 / 47775744/105625 | correction from bare threshold square to per-cube price; CONDITIONAL | HIST.md:185–186; RLARGE.md:1021; KN_ADOPT.md:545 |
| -15.617 | CONFIRMED | [-15.617074076,-15.617074075] | log10[(a_Q/100)/D], historical benchmark | RLARGE.md:64,1026; E:72; D: REVIEW_SF_S7.md:203 |
| -18.413 | CONFIRMED | [-18.412954093,-18.412954092] | preceding benchmark with /625 | c_RS=625: RLARGE.md:1021; same E,D |
| +66.523 | CONFIRMED | [66.523489528,66.523489529] | log10[(a_K/100)/D], CONDITIONAL | eta_KN: KN_ADOPT.md:545; E,D as above |
| +56.816 | CONFIRMED | [56.816203953,56.816203954] | preceding formula at E_p, CONDITIONAL | EPS1_SWEEP.md:455; KN_ADOPT.md:545 |
| log10(625) reconciliation | CONFIRMED | [2.795880017,2.795880018] | exact difference of the two historical conventions | RLARGE.md:1021; ARS_FIX.md:267–275 |
| -35.032 / -37.828 proposed old-route margins | CONFIRMED | [-35.031645225,-35.031645224] / [-37.827525243,-37.827525242] | bare / per-cube historical ceiling ratios | E_p: EPS1_SWEEP.md:455; RLARGE.md:64,1021 |
| +63.728 / +54.020 proposed-linear per-cube margins | CONFIRMED | [63.727609510,63.727609511] / [54.020323935,54.020323936] | today's / proposed KN model, CONDITIONAL | KN_ADOPT.md:545; E and E_p; c_RS=625 |
| -15.918 / +66.222 | CONFIRMED | [-15.918104071,-15.918104070] / [66.222459532,66.222459533] | conservative /200 safety convention, CONDITIONAL | KN_ADOPT.md:377–384; same E,D |
| -18.714 / +63.427 | CONFIRMED | [-18.713984089,-18.713984088] / [63.426579515,63.426579516] | same safety convention plus /625 | KN_ADOPT.md:384–385; RLARGE.md:1021 |
| mandatory exact 0.30103 F-mono loss | REFUTED | log10(2)=[0.301029995,0.301029996] is a worst-case safety allowance; loss can be zero | exact ceiling depends on R; CONDITIONAL | KN_ADOPT.md:377–380; RLARGE.md:113–116 |
| +63.619 “live exponent clears DXprime” | REFUTED | [63.626978288,63.626978289] at common D is only an optimistic UPPER benchmark, plus log C_Omega and missing minima | GAP as actual clearance | theta bound, a_A min: RLARGE.md:88–94; script substitutes theta=1/24 and D=2.5e-152: ab1_margins.py:25–26 |
| +61.42 | CONFIRMED | [61.424351291,61.424351292] at D; approximately 61.41664 at 2.5e-152 | conditional joint per-cube ceiling; not proved availability | eta_q: HIST.md:170; joint /81:505–510; D: REVIEW_SF_S7.md:203 |
| +2.203 live-over-joint | REFUTED | [2.202626996,2.202626997] for a_0, not a guaranteed live advantage | CONDITIONAL upper benchmark | RLARGE.md:88–94 versus HIST.md:505–510 |
| 79.84 | CONFIRMED | [79.837305384,79.837305385] | old eta_q joint price over old eta_RS/625 | HIST.md:170,181,185–186; RLARGE.md:64,1021 |
| 78.950 + 0.887 | CONFIRMED | [78.949910385,78.949910386]+[0.887394998,0.887394999] | threshold-square effect plus packing effect | same eta_RS, eta_q, 625 and 81 definitions |
| 4.2149e15 as correction of 4.14e15 | REFUTED | [4.140702944,4.140702945]e15 at D; 4.2149e15 belongs to 2.5e-152 | C_Omega zero-margin value, CONDITIONAL | ARS_BIND.md:337,359–361; ab1_margins.py:26,132–138 |
| 2.59e18 per-cube reversal | CONFIRMED | [2.587939340,2.587939341]e18 | C_Omega zero-margin value, CONDITIONAL | E,D,c_RS as ARS_FIX.md:267–275 |
| 30.4 decades inside C7 | REFUTED | no upper C_Omega endpoint follows from corrected C7; old product at c_plus=1 would give [30.559017183,30.559017184] | wrong operator and frozen output; GAP | EPS1_SWEEP.md:494; REVIEW_ARS_EPS_S1.md:195–198,404–408 |
| 84.170+log10(kappa) | REFUTED | offset [84.169725357,84.169725358], only between kappa=E^2/663552 and 128/13689; gain 0 below the former | piecewise conditional gain, not all small kappa | RLARGE.md:64,1020; KN_ADOPT.md:545; E:72; N=2 |
| 24.089 / “24 decades” programme q lever | REFUTED | historical scalar lever [24.089105770,24.089105771]; epsilon-limited HW lever [12.044552885,12.044552886] before other minima | wrong live exponent; CONDITIONAL sensitivities | QFIX.md:270–273,365–374; live exponent RLARGE.md:88 |
| q=8: -52.66 | CONFIRMED | [-52.664010533,-52.664010532] | CONDITIONAL scalar historical model, t_pr=theta_SUP | QFIX.md:270–276; c_s,c_g: STAR_CONST.md:338–345,399–400 |
| q=11: -36.72 | CONFIRMED | [-36.723045077,-36.723045076] | same scalar model; not admissible at unlowered E,c_N=2 | QFIX.md:190,270–279 |
| q=12: -34.47 | CONFIRMED | [-34.472562415,-34.472562414] | same scalar model | QFIX.md:270–280; m=19615,c_N=2,C_3=C_Omega=1 |
| q=32: -29.20 | CONFIRMED | [-29.202120111,-29.202120110] | same scalar model | QFIX.md:270–286,365–374 |
| q=100: -28.75 | CONFIRMED | [-28.747570901,-28.747570900] | same scalar model | QFIX.md:270–287,365–374 |
| q=1000: -28.59 | CONFIRMED | [-28.591547947,-28.591547946] | scalar model only; with fixed epsilon_* floor it is at most -34.252690331 | QFIX.md:270–290; omitted min: SQ.md:318–319,1622,1633 |
| supremum -28.575 at infinity | REFUTED | scalar LIMIT [-28.574904762,-28.574904761]; live-minimum objective tends to -infinity; actual supremum NOT-VERIFIED | limit is not a certified optimum, F4/F12 | q-dependent theta_G: QFIX.md:125,314–318; minima SQ.md:318–319,1633 |
| 8.148 above q>=11 | CONFIRMED | [8.148140315,8.148140316] | conditional scalar limit-minus-q11 | QFIX.md:279,292; same frozen chain |
| 5.898 above q=12 | CONFIRMED | [5.897657652,5.897657653] | conditional scalar limit-minus-q12 | QFIX.md:280,292 |
| 0.63 / 0.17 / 0.017 remaining | CONFIRMED | [0.627215348,0.627215349] / [0.172666138,0.172666139] / [0.016643184,0.016643185] | scalar limit-minus-q32/100/1000, not all-constraint optimisation | QFIX.md:286–302 |
| 13.15 P-max/P-ct | REFUTED | raw [13.143561886,13.143561887] -> 13.14; capped margin gain [12.957830686,12.957830687] | 8log10(B(8)/B(4)); CONDITIONAL on unavailable P-ct | STAR_CONST.md:382–388; QFIX.md:342–350,374; E cap RLARGE.md:72 |
| 4.854 original forced lowering | CONFIRMED | [4.853642787,4.853642788] at E_p | epsilon, CONDITIONAL | RLARGE.md:72; EPS1_SWEEP.md:455 |
| 3.244 new forced lowering | CONFIRMED | [3.243618467,3.243618468] at unrounded scalar cutoff | epsilon, CONDITIONAL; not at every epsilon_* | QFIX.md:270–273,290,383–385 |
| +1.610 cutoff gain | CONFIRMED | [1.610253496,1.610253497] versus 9.38e-45; [1.610024319,1.610024320] versus E_p | epsilon, CONDITIONAL scalar comparison | EPS1_EXEC.md:764; QFIX.md:383; E_p: EPS1_SWEEP.md:455 |
| 3.244 / +1.610 attached to the chosen rounded 3.8e-43 | REFUTED | lowering [3.246291206,3.246291207]; gain versus 9.38e-45 [1.607580758,1.607580759] | epsilon; unrounded/rounded baseline mismatch | QFIX.md:379–385 |
| q=100 safe cutoff 3.5e-43 | REFUTED | actual scalar upper [3.495027493,3.495027494]e-43; safe two-digit choice 3.4e-43 | cutoff must round DOWN | QFIX.md:287,379–381 |
| fixed-floor q=1000 gain/forcing | REFUTED | gain <=[0.194738723,0.194738724]; lowering >=[4.658904064,4.658904065] | epsilon_*=1.12e-37 activates theta_epsilon; other minima may worsen it | qf1b_q.py:60,181–182; SQ.md:318–319,1622,1633 |
| 19.415 / 9.707 / 14.561 | CONFIRMED | [19.414571149,19.414571150] / [9.707285574,9.707285575] / [14.560928362,14.560928363] | 4Delta/2Delta/3Delta, conditional exponents | EPS1_EXEC.md:513–554; E and E_p above |
| 36.63 -> 31.78 | CONFIRMED | [36.630960621,36.630960622] -> [31.777317834,31.777317835] | epsilon/g at g=sqrt(D), CONDITIONAL | EPS1_SWEEP.md:242; D: REVIEW_SF_S7.md:203 |
| PLD absorption ratio loses 4.854 | REFUTED | it GAINS Delta at fixed g | 2m_*g/epsilon, not epsilon/g | PLD.md:995; EPS1_EXEC.md:324–346 |
| +1.157 old q leverage | CONFIRMED | [1.156812056,1.156812057] | epsilon gain q12->q100 with frozen Lambda | EPS1_EXEC.md:443–451; printed C_T=5.288e12,1.396e12 |
| -2.761 actual q8 shift | REFUTED | only a bound from C_T>=1.27e14; computed frozen-Lambda q12->q8 shift [-4.385756275,-4.385756274] | epsilon; a lower C_T bound was used as equality | EPS1_EXEC.md:452; actual C_T chain QFIX.md:365–370 |
| 6.365 H2 effect at q12 | CONFIRMED | [6.365045455,6.365045456] | epsilon loss when ONLY source neighbourhood changes 3->486, CONDITIONAL | QFIX.md:203–216; qf1c_posthoc.py:31–34 |
| 1.038 H2 effect at infinity | REFUTED | [1.037481305,1.037481306] -> 1.037; finite q=10^6 gives [1.037518069,1.037518070] -> 1.038 | epsilon loss; finite endpoint mislabeled limit | qf1c_posthoc.py:31; QFIX.md:216 |
| “H2 conditionality collapses” | REFUTED | only one H2 clause was varied; second coefficient-restatement clause remains unpriced | GAP as full removal of H2 | QFIX.md:203–209; STAR_CONST.md:443–444 |
| 9.707 -> 9.428 energy shortfall | CONFIRMED | [9.707284860,9.707284861] -> [9.427744169,9.427744170] | eta_flat / energy, CONDITIONAL chains | old C_D=900*5.288e12: tf1_tau.py:63,67,109; new QFIX.md:270–273 |
| “9.707 at exactly C_D=4.76e15” | REFUTED | [9.707576847,9.707576848] -> 9.708 | printed rounded C_D differs from script's 4.7592e15 | TAUFLAT.md:196; tf1_tau.py:109 |
| 1.690 old q spread | CONFIRMED | [1.690373832,1.690373833] | epsilon spread on the FINITE q11..100 printed table | EPS1_EXEC.md:443–455 |
| 1.690 -> 2.037 from Lambda alone | REFUTED | same finite endpoints give [1.993868544,1.993868545] -> 1.994; [2.037035078,2.037035079] changes endpoint to infinity | endpoint and symbol both changed | EPS1_EXEC.md:443–455 versus QFIX.md:438 |
| 0.080 -> 0.578 room | CONFIRMED | [0.079838769,0.079838770] -> [0.578406028,0.578406029] | C_T, fixed-q floor versus q100 endpoint | TAUFLAT.md:375–378; EPS1_EXEC.md:474–480 |
| 10.263 -> 0.555 gain spread | CONFIRMED | [10.262743411,10.262743412] -> [0.555457836,0.555457837] | five values including proposal versus four historical values | ra1b_margins.py:94–105; E extrema: ARS_FIX.md:269–273 |
| 1.696 spread of four constants | REFUTED | pairwise [1.695767490,1.695767491]; four-form spread >=5.340491706 at k=1 and unbounded over k | different depths, hypotheses and measures | PLD.md:42,196–197,276,283,341,1044–1048; RLARGE.md:1026 |
| ×287 on C_1 | REFUTED | [284.981641517,284.981641518] -> approximately 285; product is 1.3502430175e6 | same-precision C_1 change, not ratio of rounded products | STAR_CONST.md:399–400,470; CONST_T.md:292 |
| ×287 on rounded A_c*gamma_c | CONFIRMED | new product /4700=[287.285748405,287.285748406] | different rounding convention; CONDITIONAL comparison only | EPSSTAR.md:216–218; old exact product 4738 |
| ×1.78 DESC ceiling correction | CONFIRMED | printed-ceiling ratio [1.779706976,1.779706977]; new C_D ceiling [1.781192096,1.781192097]e13 | C_D, not t_pr (whose correction is about sqrt(10)) | EPSSTAR.md:521,525,527; QFIX.md:397–407 |
| ×1.16 q11 failure | CONFIRMED | [1.155799046,1.155799047] | C_D(11)/(6.7e15), c_N=2 | QFIX.md:190,270–279 |
| ×9 theta_SUP correction | CONFIRMED | exact 9 on unrounded model; [10.012459950,10.012459951] against printed 5e-23 | theta_SUP^2 coefficient; threshold-limited branch only | SQ.md:212,216; HW.md:603–604; Cprime=53,c_flat=1/640 |
| 52 decades described as tau_flat | REFUTED | eta_flat log-ratio [52.077008938,52.077008939]; tau_flat log-ratio [26.038504469,26.038504470] | energy threshold versus its square root | TAUFLAT.md:192–204; tf1_tau.py:63,67,109; ledger:397 |
| 0.90 upper limit | REFUTED | log10(8)=[0.903089986,0.903089987]; safe upper display 0.904 | arithmetic factor-eight model; analytic universal bound NOT-VERIFIED | FACEB.md:677; ledger:452 |
| 8.11 / 38.65 | CONFIRMED | [8.111061330,8.111061331] / [38.646821632,38.646821633] | P(k) at k10 / k42, conditional eta self-map | FACEB.md:489–511; L=3 |
| 173.58 | CONFIRMED | [173.576712467,173.576712468] | P(183.4), not a certified coupling loss | FACEB.md:491,513; k=183.4 from ARS_FIX.md:490 |
| 337.90 | CONFIRMED | [337.897272592,337.897272593] | P(355.6), same conditional currency | FACEB.md:514; ARS_FIX.md:489 |
| 151.610 | CONFIRMED | [151.609771637,151.609771638] | -log10(D), C_Omega=1 | REVIEW_SF_S7.md:203; FACEB.md:518 |
| k*=160.380 | CONFIRMED | [160.379708394,160.379708395] | conditional P(k)=Ddec, C_SR=C_Omega=1 | FACEB.md:489–523 |
| +21.97 beyond DXprime | CONFIRMED | [21.966940829,21.966940830] | P(183.4)-Ddec; requires X1/X2 for physical interpretation | FACEB.md:527–529 |
| k*=42.552 | CONFIRMED | [42.552379043,42.552379044] | conditional epsilon-sized budget, C_SR=1 | FACEB.md:519,523; E: RLARGE.md:72 |
| 81.7 -> 80.940 doubled currency | CONFIRMED | [80.939854197,80.939854198] | correction solving 2P(k)=Ddec | FACEB.md:536–537; D and L as above |
| “four decades” pole grid | REFUTED | three decades, four points; pure-pole growth 1000 | log10(10^-1/10^-4) | TUNIF.md:542–543; ledger:923 |
| “six decades” repair grid | REFUTED | five decades, six points | log10(10^-1/10^-6) | tu1b_pole.py:12–14,22; ledger:546 |
| 8e-48 / 0.000000-decade source agreement residuals | NOT-VERIFIED | source-run residuals not replayed; underlying shared-formula log identities are exact | implementation convergence, not scientific evidence | EPS1_EXEC.md:534; ARS_BIND.md:330; ledger:245,599 |
| reconciliation to 10^-4 decade | CONFIRMED | exact difference is enclosed log10(625); relevant rounded values are consistent | arithmetic only | ARS_FIX.md:272–275; ra1b_margins.py:109–116 |
