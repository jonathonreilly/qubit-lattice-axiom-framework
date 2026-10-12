Focused independent all-heralded-trial detection/readout review, 2026-10-12 UTC.

Disposition: both loss-map formulas, the sign of the constant term, both threshold inequalities, and all 28 frozen diagnostic rows check correctly. The sequential constant-assignment guarantee requires conditional fair marginals. The complete V3 now makes that requirement explicit and supplies the correct general marginal correction; V2's herald-before-fresh-choice clarification is retained. I find no remaining material mathematical correction in the scoped V3 statement. The original frozen numerical outputs remain unchanged. This is a focused source and mathematics check, not a formal audit, empirical detector assessment, or validation of the original full-sphere classification.

The reviewed original note is SHA256 `906b648dd5756a7d63998f1f965cf99e907f93e4d912e6dca5f794b0ee429af3`, checker `b1219211b54cc67e212805ab7ed48c8eefe049dad398b16fde06d083b029700b`, V2 `545443eea4933c013ad9a2a6f1f465acef4e0dc9d149833754e88117d490f36f`, and final V3 `e3589c09bc5ad06940c793bf3239a425b72bc0b89aa457575e67247399e539dc`. I also read the complete V2-to-V3 diff, `04bd2108d18da3aec6a67235492a554026a691fd84b08de80f81475d459b0b68`. The freeze is `648dc9d938fc95ba71b9112f6683f15e970c3b8ec398feb7da02d6d90858994c`, execution receipt `5b9c81eab55dfd91046c6fca7b431cbedd710e69f3abed02b4b88b5546f5b5ac`, and result `b2962638e5699da67393682f96cfd53b60fb2ff102a80782a1658d97621c76b4`. Every original and snapshot matched before and after the checks.

The freeze declares exactly seven efficiencies and two assignment models, pins the original derivation, the reflection result `a911495b6d1f60b48334d03346c45393911031bead3288c2e0c1aad2e7b25ea9`, and angular result `5f3913d3508ff38b5a8bda32ec3689df272bddc01a6838bee230145fa778dba9`. The checker itself is pinned by the execution receipt and repeated in the output, not by the earlier freeze. The source writes that receipt before reading and calculating its input values; it does not add a final source-identity assertion. This review therefore does not describe the entire checker as pre-frozen. The preserved execution identity, current matching bytes, and independent reconstruction of every result are the source-provenance evidence used here. V2 and V3 are explicit later premise clarifications rather than hashes retroactively attributed to the original execution.

Let D_A,D_B be detection indicators, X,Y the ideal signs, and R_A,R_B the no-click assignments. The retained signs are X'=D_A X+(1-D_A)R_A and Y'=D_B Y+(1-D_B)R_B. Under the stipulated conditional independence of loss and the source/outcomes/settings, E[D_A D_B|past]=ηAηB. For independent fair fill-in signs, every term containing an R has zero mean. Thus C_random=ηAηB C_actual, without a fairness requirement on X or Y. Independence of the fill-ins from the losses, ideal outcomes, source variables, and one another is essential to this particular formula.

For deterministic +1 fill-in the general pointwise formula is instead

    C_plus(a,b)=ηAηB C(a,b)+ηA(1-ηB)mA(a)
               +(1-ηA)ηB mB(b)+(1-ηA)(1-ηB).

Here the marginal functions are one-setting local marginals. In the reflection functional, B(1)=-1 and B(mA)=-M_A, B(mB)=-M_B, where M is the uniform local-setting average. The product term vanishes because ∫P3(a·b)dμ(b)=0 for each a; the diagonal supplies the negative average. This gives precisely V3's general B_plus expression. Conditional fair marginals set M_A=M_B=0 and yield B_plus=ηAηB B_actual-(1-ηA)(1-ηB). Pointwise conditional fairness is a sufficient premise; zero uniform conditional marginal means would suffice for this functional. A bound on correlation error alone supplies neither one.

The conditional qualification is substantive. For either history h=±, choose mA=mB=±1/100 and retain exactly the same correlation C(a,b), with |C|≤19/20. The probabilities

    P(x,y|a,b,h)=[1+m_h x+m_h y+C(a,b)xy]/4

are nonnegative for all x,y. Averaging equally over histories gives fair unconditional marginals and leaves C unchanged, even with zero correlation error. At η=99/100, however, the conditional B_plus has an extra ∓99/500000. The unbiased formula therefore is not a conditional lower bound in both histories. V3 explicitly resolves this point; its randomized branch remains independent of marginal fairness.

The quantum-null argument has weaker detector assumptions than the candidate factorization. For any local three-outcome POVM E_+, E_-, E_0 with sum I, randomized assignment produces binary effects F_±=E_±+E_0/2 and observable A=E_+-E_-. Constant +1 assignment gives F_+=E_++E_0, F_-=E_-, hence A=I-2E_-. Both are Hermitian contractions. The common-map reflection proof therefore still gives |B|≤1, including setting-dependent or outcome-dependent efficiencies, when every heralded trial is retained and the same local map is used in both branches. It does not justify arbitrary remote-setting dependence, branch disclosure, or conditioning on detector outcomes. V3 explicitly requires the herald and inclusion decision before the fresh branch and joint settings, so setting-based inclusion cannot silently alter the measure.

In a sequential experiment the efficiencies, loss independence, candidate lower statistic, and (for constant assignment) fairness must be the required conditional quantities for each included trial. A mean efficiency is insufficient: histories with η=1 with probability 2/3 and η=.97 with probability 1/3 have average per-arm efficiency .99, but the low-efficiency history has ideal readout gap -0.01089328, whereas inserting .99 into the formula gives +0.03031512. This is a failure of that conditional substitution, not a proof against every possible aggregate-statistics analysis. Likewise a shared loss bit with ηA=ηB=1/2 and ideal XY=1 gives random-assignment C_readout=1/2, not ηAηB C=1/4. The note correctly stipulates independence for the candidate formula while not requiring it for an arbitrary local quantum POVM null.

Writing the pre-loss conditional lower value as 1+Δ>1, independent fair assignment gives Δ_random=q(1+Δ)-1. Therefore q>1/(1+Δ), or equal η>1/√(1+Δ), is exactly the positive-gap condition for this bound. Constant assignment with fair conditional marginals gives Δ_plus=Δη²+2η-2 and root η>2/[1+√(1+2Δ)]. The constant threshold is strictly larger for positive Δ, since its gap subtracts (1-η)². These statements are sufficient certificates using the lower pre-loss statistic; they are not necessary detector efficiencies for any optimized measurement or Bell inequality. For efficiencies known only to be at least the stated equal value, both bounded formulas are increasing in each efficiency when the lower B exceeds one.

I bracketed both efficiency roots by exact rational bisection of their gap polynomials, independently of the author's integer-square-root construction. All four published rational brackets contain the independently enclosed root:

| Pre-loss budget | Random-assignment threshold | Constant +1 threshold |
| --- | ---: | ---: |
| Ideal V=.95 | 0.9753268017988440 | 0.9756166967849663 |
| δ=ε=1/1000 | 0.9834123234650103 | 0.9835454450674528 |

Thresholds are strict. The perturbed row means δ=1/1000 radians per arm and extra candidate-side correlation error ε=1/1000; its pre-loss lower gap is 0.0340194487964251. The constant-assignment column additionally retains conditional fairness. I reconstructed the ideal lower statistic from the pinned a3 upper endpoint and the perturbed allowance from L_upper, then computed all 28 gaps and counts with exact fractions, without author-helper imports.

| Per-arm η | Ideal random N | Ideal +1 N | Perturbed random N | Perturbed +1 N |
| --- | ---: | ---: | ---: | ---: |
| 1 | 469373 | 469373 | 1064613 | 1064613 |
| 199/200 | 742028 | 742940 | 2192615 | 2197247 |
| 99/100 | 1340688 | 1349577 | 6818493 | 6921083 |
| 197/200 | 3100627 | 3171825 | 117986506 | 136306903 |
| 49/50 | 13353020 | 14538632 | No count | No count |
| 39/40 | No count | No count | No count | No count |
| 97/100 | No count | No count | No count | No count |

Every “No count” is a preserved nonpositive certified gap; none was made artificially positive by squaring. For positive gaps each ceiling satisfies N-1<40J²/Δ_readout²≤N exactly. Since retained binary outcomes keep Z∈[-J,J], J=111/20, fixed-horizon conditional Hoeffding gives each one-sided error ≤exp[-NΔ_readout²/(8J²)]≤e^-5<.01 at the midpoint threshold. This is not an optional-stopping guarantee. Extra systematic error that also shifts the quantum null still needs its own allowance as in the angular note.

The independent controls exhaust all ideal outcomes, detection flags, and fill-in bits for both fair and biased rational joint laws. With ηA=3/5, ηB=4/5 and biased mA=2/5, mB=1/5, C=2/5, random readout is 24/125 as predicted, while constant readout is 48/125 rather than the fairness-only value 34/125. A fair law matches both formulas. Small common-qubit POVMs with setting- and outcome-dependent efficiencies remain positive and produce contraction observables; the tested random and constant statistics were -0.0085 and -0.154, within the null bound. These numerical controls supplement the explicit analytic POVM proof.

The check script ran in 0.012 seconds with maximum RSS 33.9 MB and one numerical-library thread. Exact evidence and source identities are preserved in runtime `quantum/detection_readout/independent_detection_review/detection_independent_checks_v1.json` and the accompanying receipt. Only the designated review directories were written. No author source, original calculation, real targets, fit, active field process, Git state, or audit state was changed. The conclusions remain prospective and conditional: no measured calibration, detector model validation, empirical rejection, or full apparatus protocol is established.
