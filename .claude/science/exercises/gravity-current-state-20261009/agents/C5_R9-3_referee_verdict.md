# VERDICT: CONFIRMED WITH CORRECTIONS

The component numerics, the operator-valued support reduction, the qualitative Fourier-tail tracking, and the diagnosis of a defective tail observable are confirmed. The largest correction is the registered reading: the worker's scientifically sensible **INCONCLUSIVE** interpretation is not the literal FIXED result. `TESTS.md` says FAIL if a refereed proof shows that *either* the connected term *or the packing unitary* has power-law-or-slower tails (`TESTS.md:3699-3702`). At nonzero total momentum for this nontrivial pair law, a cluster-separable Sokolov packing has `B → B_a ≠ I`, while `H_S-H_BT → H_a-B_a H_a B_a† ≠ 0`, in the `a=(12)(3)` spectator limit. Nondecay is “power-law or slower.” Thus this report supplies the missing referee confirmation and the literal reading is **FAIL**, albeit for a non-discriminating registration defect. The physically intended question—whether the deviations from the correct channel limits and the actual `H_S,K_S` cluster residuals decay faster than every power—remains **INCONCLUSIVE** because `H_S,K_S` were not assembled (`R9-3_report.md:142-144,185-193,283-294`).

## 1. Operator-valued reduction

**Confirmed, with hypotheses made explicit.** Let (Q=Q_G\otimes I_{\rm sp}). The rank-one interaction is supported in (G), so (G) and (G^\perp) reduce both (M) and (M_0), and (M=M_0) on (G^\perp). If the half-density reparametrizations (R_\mu) act unitarily on one common spectator Hilbert space and (\mu\mapsto R_\mu) is strongly Borel (it is smooth on the compact mass/momentum region used here), the bounded operator-valued functional calculus

\[
F(M)=\int E_M(d\mu)\otimes R_\mu
\]

is well defined. Equality of the restricted spectral measures on (G^\perp) then gives

\[
F(M)-F(M_0)=Q[F(M)-F(M_0)]Q.
\]

Since (R_M=F(M)), (R_0=F(M_0)), and (R_0) is unitary,

\[
B_b-I=R_0^\dagger R_M-R_0^\dagger R_0
     =R_0^\dagger[F(M)-F(M_0)].
\]

Moreover (R_0) commutes with (Q), so the report's right-support conclusion is valid and can be strengthened to (B_b-I=Q(B_b-I)Q). This is the operator-valued extension of the scalar statement in `C5_R8-1_referee_verdict.md:25-30`, and it matches the runner's stated reduction (`scripts/r93_packing_cluster.py:3-8,120-153`). An independent finite-dimensional test using a genuinely matrix-valued, noncommuting (R_\mu) gives zero support error and (8.8\times10^{-17}) reduction error (`referee_r93_independent_checks.py:13-44`; `referee_r93_independent_checks.out:1`).

The correction is numerical, not algebraic: the runner truncates the spectator grid and uses cubic interpolation (`scripts/r93_packing_cluster.py:112-145`), so its implementation realizes the exact identity only to its interpolation floor, not exactly.

## 2. Requested reruns

**Confirmed.** I ran both cases with `OMP_NUM_THREADS=2` (and two threads for the BLAS backends), adding only a filename tag so that the supplied outputs were not overwritten.

- $P=0.4$, $\sigma_k=0.1$, $hfac=0.03$: the residuals are $5.6519\times10^{-4}$, $9.6366\times10^{-5}$, and $2.1219\times10^{-6}$ at $D=80,160,320$, exactly reproducing the worker (`scripts/r93_packing_cluster_b_2+1_P0.40_referee.out:1-4`; original at `scripts/r93_packing_cluster_b_2+1_P0.40_sk0.1.out:8-12`).
- $P=0$ control with the same packet and grid settings: $\|(B_b-I)\psi_D\|/\|\psi\|=2.2633\times10^{-11},3.3088\times10^{-11},4.3373\times10^{-11}$, and the commutator residuals are $4.4$–$8.7\times10^{-13}$ (`scripts/r93_packing_cluster_b_2+1_P0.00_referee.out:1-7`). Analytically $q_1(0,k;\mu)=k$ for every $\mu$, so every $R_\mu=I$ and $B_b=I$; the independent formula check is $1.1\times10^{-16}$ (`scripts/r93_packing_cluster.py:58-68`; `referee_r93_independent_checks.out:2`). The nonzero run values are therefore numerical floor, not physics.

## 3. Fourier-tail tracking

**Confirmed as finite-window component evidence; not confirmed as an operator asymptotic theorem.** The three modified form factors are (C_c^\infty): the endpoint factors (e^{-1/x^s}) are flat for every (s>0), and multiplication by the smooth packet preserves compact smoothness. Their exact Fourier transforms therefore decay faster than every inverse power. The proxy actually computed is a discretized sine transform followed by a 41-point sampled envelope (`scripts/r93_ff_proxy.py:1-5,15-30`), whose values are recorded at `scripts/r93_ff_proxy.out:3-13`.

My independent parsing of the raw component data reproduces the claimed local-slope agreement. From `D=226`, the maximum data/proxy slope mismatch is `0.362, 0.448, 0.687` for `s=0.5, 1, 2`; from `D=320`, it is `0.362, 0.266, 0.331` (`referee_r93_independent_checks.py:89-123`; `referee_r93_independent_checks.out:4-9`). The ordering reversal and the analytic-form-factor floor are also present in the supplied outputs (`R9-3_report.md:240-262`; `scripts/r93_packing_cluster_b_2+1_P0.40_gauss.out:7-11`). One numerical wording needs correction: only `B_b-I` was extended to `D=640`, reaching `2.96e-8` (`scripts/r93_packing_cluster_b_2+1_P0.40_sk0.1.out:8-14`); `B_c-I` stops at `D=320`, where it is `2.12e-6` (`scripts/r93_packing_cluster_c_2+1_P0.40_sk0.1.out:6-10`).

That establishes a persuasive correlation for the tested Gaussian state and three form-factor families. It does **not** prove that (B_b-I), in operator norm or uniformly over cluster states, inherits the Fourier bound. The proxy is not the full packing kernel, the agreement uses only two or three late intervals per family (only one interval beyond (D=320) for (s=2)), and the required nonstationary-phase estimate remains absent, as the worker itself acknowledges (`R9-3_report.md:264-268,289-292,316-321`). The strongest justified phrase is “the tested component tails track the form-factor proxy over the sampled window,” not “the operator tail is proved super-polynomial.”

## 4. Spectator-direction tails and FIXED (c)/(d)

**The narrow incompatibility is confirmed; the worker's universal wording needs scope corrections.** In the (a=(12)(3)) cluster limit, a Sokolov packing that restores generator clustering must satisfy

\[
B\,T_a(D)\psi-B_aT_a(D)\psi\longrightarrow0,
\qquad
H_{BT}T_a(D)\psi-B_aH_aB_a^\dagger T_a(D)\psi\longrightarrow0.
\]

The second limit follows because the crossed (b,c) pair terms vanish strongly when their pairs are separated; for these smooth compact rank-one kernels, this is the ordinary translated-kernel/Riemann–Lebesgue limit. If (H_S=B^\dagger H_{BT}B) clusters, then (H_ST_a(D)\psi\to H_aT_a(D)\psi). Therefore

\[
B-I\to B_a-I,
\qquad
H_S-H_{BT}\to H_a-B_aH_aB_a^\dagger
\]

in that channel. For the submitted nontrivial pair interaction at $P\ne0$, $B_a$ is a mass-dependent momentum reparametrization, is not $I$, and does not commute with $H_a$. Hence suitable translated packets have a nonzero asymptotic packing effect and a nonzero BT-cancelling correction. The submitted data directly show the effect on the chosen packets: $\|(B_a-I)\psi_D\|=0.059$–$0.426$, and $\|[B_a,H_a]\psi_D\|=2.38\times10^{-3}$–$2.97\times10^{-2}$, over $D=10$–$320$ (`scripts/r93_packing_cluster_a_2+1_P0.40_comm.out:2-13`).

Three corrections are required.

1. This statement is for nonzero (P), a nontrivial pair packing (B_a\ne I), and suitable state families. At (P=0), (B_a=I) (`scripts/r93_packing_cluster_b_2+1_P0.00_referee.out:1-7`). It is not true without those qualifiers for “every” cluster-separable Sokolov law or every state.
2. The data show growth over the sampled interval, not indefinite growth. On the compact box sector (H_a-B_aH_aB_a^\dagger) is bounded, so “does not decay” is the valid conclusion; “grows” is not an asymptotic theorem.
3. The proof concerns the literal un-subtracted observables in (d). The physically connected channel remainders are instead (B-B_a) and ((H_S-H_{BT})-(H_a-B_aH_aB_a^\dagger)), which may decay rapidly and were not computed.

With the FIXED text unchanged, (c) and (d) are indeed incompatible at nonzero (P): (c) makes (H_S\to H_a), while the BT representation tends to the unclustered (B_aH_aB_a^\dagger); their difference must cancel that nonzero defect. Because FAIL is expressly disjunctive and includes the packing unitary (`TESTS.md:3695-3702`), the literal registered result is **FAIL**, not INCONCLUSIVE. This FAIL diagnoses the registration, not a physical failure of the Sokolov cure.

## 5. Ring non-representability

**Confirmed narrowly; the title-level claim is too broad.** In the continuum free-rest chart, the pair-(12) term changes (q_{12}) at fixed rest spectator momentum (p_3). At fixed nonzero total (P), the inverse boost gives

\[
k_3=m\sinh\!\left[\operatorname{asinh}(p_3/m)+
\operatorname{asinh}(P/M_0(q_{12},p_3))\right],
\]

so changing $q_{12}$ changes $k_3$ continuously and generically by a noninteger multiple of $2\pi/L$ (`R9-3_report.md:159-167`). An independent $L=300$ example changes $q_{12}$ by one grid unit but moves $k_3$ by $-0.074785$ grid units (`referee_r93_independent_checks.py:58-75`; `referee_r93_independent_checks.out:3`). Thus the continuum chart-change operator does not preserve the finite-ring momentum grid at generic $P\ne0$; a projection, quadrature, or interpolation prescription is required before the registered ring residuals are defined.

This does **not** prove that no ring-native discretization or alternative finite-dimensional approximation exists. It proves only that the submitted continuum BT/Sokolov chart construction has no exact restriction to the naive ring grid at generic nonzero (P). (P=0), accidental grid coincidences, and separately specified ring discretizations are exceptions. Since (H_S) was never assembled, its claimed off-grid kernel is a formal consequence of the chart composition, not a checked lattice operator.

## 6. Reading, exactness, and the two registration issues

**Algebra and trimer mass.** Conditional on a well-defined unitary (B) commuting with (P), a common invariant domain, and the BT algebra, unitary conjugation does give the displayed commutators and preserves the spectrum; (H_{BT}(P)=\sqrt{M_{BT}^2+P^2}) then makes every invariant-mass eigenvalue (P)-independent (`R9-3_report.md:126-144,173-183`). These are correct formal identities. They are not a completed construction here: the logarithmic choice needs a spectral branch, the polar choice needs invertibility and stable cluster limits, domain invariance is only suggested, and no (B,H_S,K_S) matrix was assembled (`R9-3_report.md:131-144,316-320`). Thus “exact by conjugation, conditional on existence/domain hypotheses” is correct; “the explicit lattice law was proved and checked” is not.

**Registration issue 1—wrong channel subtraction.** Confirmed and stronger than the worker's wording. The literal observables (B-I) and (H_S-H_{BT}) are required to approach nonzero channel operators when Sokolov packing fixes BT clustering at (P\ne0). A future test should measure (B-B_a) and ((H_S-H_{BT})-(H_a-B_aH_aB_a^\dagger)) in the (a) channel, plus (B-I) only in the all-separated channel. Under the immutable present wording, however, this defect cannot be used to change FAIL into INCONCLUSIVE.

**Registration issue 2—finite-window information criterion.** Confirmed with terminology corrected. The chosen AICc calculation selects a power law for the known $C_c^\infty$, $s=0.5$ component window: $\Delta\mathrm{AICc}=-8.70$ over $D=80$–$640$ (`scripts/r93_fit.py:16-29`; `scripts/r93_fit.out:28-30`). Applying the same formulas to its rigorously super-polynomial Fourier proxy also selects power, with $\Delta\mathrm{AICc}=-8.91$, while the super-polynomial fit hits the imposed $\beta=0.1$ search boundary (`referee_r93_fit_sensitivity.out:6`). That is not an error in AICc; it is a demonstration that the finite window is underpowered for asymptotic classification. The result is also sensitive to the start point: for the main $s=1$ series the super-polynomial preference drops from $+8.37$ at $D_{\min}=80$ to $+0.15$ at $D_{\min}=113$, while the $s=0.5$ power preference changes from $-8.70$ to $-5.01$ (`referee_r93_fit_sensitivity.out:1-5`). The registered full range mixes packet-overlap decay with the operator-dominated regime (`R9-3_report.md:212-230`). Moreover, the registration names only an information criterion, not the worker's beta grid, floor rule, or post-hoc $D_{\min}$ (`TESTS.md:3695-3696`; `scripts/r93_fit.py:21,31-38`). The test can report which finite-window model compresses the samples better; it cannot certify the true tail class.

**Registered reading.** PASS is unavailable for independent reasons: the setting required explicit, not formal, (H_S,K_S); the ring algebra, actual (H_S,K_S) cluster residuals, both registered tail observables in the intended sense, and moving trimer checks were not performed (`TESTS.md:3683-3700`; `R9-3_report.md:283-302`). Scientifically, those omissions leave the intended Sokolov-lattice construction INCONCLUSIVE. Formally, the literal packing-unitary/connected-term FAIL disjunction is now refereed and satisfied, so the immutable reading is **FAIL**.

## No-go discipline check

- **N1—alternative routes.** Six materially different attacks were checked: (i) subtract the correct channel limits, which removes the contradiction but changes (d)'s literal observable; (ii) take (P=0), where (B_a=I), which is a genuine scoped exception; (iii) take a trivial or commuting pair interaction, also outside the submitted nontrivial law; (iv) choose a different symmetric global packing, which cannot help if it still obeys (B\to B_a); (v) deny decay of the crossed pair terms, which would defeat cluster separability itself, while their strong decay follows here from the translated smooth finite-rank kernels; and (vi) use a ring-native discretization, which can cure the ring implementation issue but not the continuum channel-limit identity.
- **N2–N3—walls and hidden hypotheses.** No independent wall count is claimed. The necessary hypotheses are explicit: nonzero (P), nontrivial (B_a), the Sokolov channel limit, strong disappearance of crossed pair terms, and a common operator domain.
- **N4—residual matching.** The nondecay evidence is the present (B_a-I) and ([B_a,H_a]) residual, not the earlier R7-6 pair-separation residual. No mismatched prior residual is used.
- **N5—resolution.** The conclusion is only about the spectator cluster direction and suitable translated packets. The (b,c) packing differences when their own pairs separate do decay in the tested states; no all-direction, all-state, operator-norm nondecay is claimed.
- **N6—partial closure.** Correct channel subtraction is a definition/registration repair, not a new axiom or new physics.
- **N7—steelman.** The strongest objection is that “tails” was intended to mean deviations from the appropriate cluster limits. Under that physically natural reading there is no incompatibility, and the actual tail question remains open because (H_S,K_S) were not built. It does not defeat the literal FIXED wording.
- **N8—echo.** R7-6 already identified long-range (B_a) together with the possibility that the packed law clusters (`C5_R7-6_referee_verdict.md:109-137`). The present correction applies that known mechanism rather than mistaking it for a universal failure of packing.

The broad statement “all cluster-separable Sokolov laws have nondecaying packing tails” fails N5 without the qualifiers above. The narrow statement used for the literal registered result—this nontrivial (P\ne0) construction, the un-subtracted observables, and the spectator channel—survives the stress test.

## Strongest correct statement

For the submitted nontrivial `d=1` rank-one box interaction, the exact support reduction `B_b-I = R_0†[F(M)-F(M_0)]` is valid for the bounded operator-valued functional calculus, and the requested two-thread rerun reproduces `5.6519e-4`, `9.6366e-5`, and `2.1219e-6` at `P=0.4`, while `P=0` is identity to the `1e-11` interpolation floor. On the tested Gaussian states, the `B_b-I` and `B_c-I` component tails track discretized Fourier proxies for three smooth compact form-factor classes, but this is finite-window evidence, not a uniform super-polynomial operator bound, and the AICc power preference for `s=0.5` demonstrates finite-window underdetermination rather than an AICc error. Conditional on existence and domain control of a Sokolov unitary `B`, conjugation gives the Poincaré algebra and momentum-independent trimer mass formally; neither `B` nor `H_S,K_S` was assembled or checked. At generic nonzero `P`, the continuum chart also fails to preserve the naive ring grid without an interpolation/discretization prescription. Finally, in the spectator `a=(12)(3)` channel, cluster separability forces `B → B_a ≠ I` and `H_S-H_BT → H_a-B_a H_a B_a† ≠ 0` for this law, so the literal FIXED (c)/(d) requirements are incompatible and the registered reading is **FAIL**; that FAIL is a registration artefact, while the physically meaningful subtracted-tail and assembled-operator question remains **INCONCLUSIVE**.
