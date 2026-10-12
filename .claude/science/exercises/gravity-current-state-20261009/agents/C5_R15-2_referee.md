# VERDICT: CONFIRMED WITH CORRECTIONS

The worker runner reruns byte-for-byte (`r152_rerun.out`, SHA-256
`002294d895ba5fd601293217b842420cff837231429a28f34092eb89b91b023b`).
An independent symbolic derivation and separately coded convolution check are
in `scripts/r152_referee_checks.py` and `r152_referee_checks.out`.

## Findings

1. **Lemma A — confirmed for nonzero spatial momentum, with a scope
   correction to the start-time sentence.** Substituting the conserved-source
   relations into the Lorenz exchange gives exactly the displayed TT, vector,
   and scalar decomposition: the independent symbolic residual is zero
   (`R15-2_report.md:94-109`; `r152_referee_checks.out:1-3`). Only TT retains a
   `1/(k^2-w^2)` pole; the vector and scalar coefficients are time-local
   constraint kernels. Since Theorem U explicitly assumes an undamped `1/s`
   pole, its cone obstruction and R11-5 Lemma C apply only to TT
   (`TESTS.md:4518-4524`; `C5_R11-5_report.md:103-123`). “The start time is
   needed by TT alone” is correct only for that light-cone/stationarity
   obstruction. If the whole matter filter is actually switched on at a
   finite `t0`, the scalar/vector mean source also has the boundary defect of
   Lemma B and needs initial constraint data. The `k=0` homogeneous mode is
   outside the displayed SVT division by powers of `k` and is not proved here.

2. **Lemma CU — not confirmed as a universal theorem; a restricted version is
   correct.** For channel-diagonal gains whose differences are temporal
   filters multiplying the same spatial profile, a nonzero difference leaves
   an uncancelled inverse-Laplacian constraint term and hence an instantaneous
   long-range tail. Equal gains remove that extra tail
   (`R15-2_report.md:128-132`; `r152_referee_checks.out:37-39`). But the claimed
   necessity fails without that restriction: for example,
   `F_V-F_TT=k^2 Q` cancels the vector `1/k^2`, and an analogous sufficiently
   high power of `k` can make scalar remainders spatially local
   (`r152_referee_checks.out:40`). Equality is also not by itself a proof of
   strict microcausality because the common Gaussian spatial factor has
   noncompact support. The report itself calls the couplings Riesz-nonlocal and
   admits that no-signalling was not computed beyond the mean-field argument
   (`R15-2_report.md:136-139`). The warranted result is therefore: one common
   gain is the condition that reconstructs `F E_Lorenz` and cancels the
   constraint tails within the report's restricted ansatz.

3. **Conserved noise — confirmed after correcting what the “iff” qualifies.**
   For `X=f*xi`, finite-start differentiation gives
   `D X=f(0)xi+f'*xi` and
   `D^2 X=f(0)xi'+f'(0)xi+f''*xi`
   (`r152_referee_checks.out:5-9`). Thus `f(0)=f'(0)=0` is necessary and
   sufficient for the report's ordinary finite-variance construction in which
   the derived S/V components are only `f'*xi` and `f''*xi`, start at zero, and
   contain neither white nor differentiated-white boundary terms
   (`R15-2_report.md:143-152`). It is not necessary for conservation in the
   broader distributional sense if those singular boundary terms are retained.
   The repaired gain independently has unit zeroth moment, zero first moment,
   and `f(0)=f'(0)=0` (`r152_referee_checks.out:10`).

4. **Lemma B and the proposed `B` term — confirmed, with the quantifier on
   decay narrowed.** Direct integration by parts gives
   `d_mu(f*_[t0,t]T)^{mu nu}=f(t-t0)T^{0nu}(t0)`. With `psi'=-f` and
   `Psi1'=psi`, the displayed `B` has the opposite divergence, so `J+B` is
   exactly conserved and supplies the nonzero initial constraint source
   (`R15-2_report.md:154-165`; `r152_referee_checks.out:12-15`). At late times,
   `B^{00}->-m1 div T^{0i}(t0)` and `B^{0i}->0`. Therefore zero first moment is
   necessary and sufficient for `B` to decay for **arbitrary** conserved
   initial data; a particular datum with `div T^{0i}(t0)=0` also decays when
   `m1` is nonzero (`r152_referee_checks.out:15-16`). The proposed `B` is an
   exact repair, not a uniqueness theorem, and the report's one-shot
   measurement imprecision/backaction remains a named but unbuilt initial
   instrument (`R15-2_report.md:168`).

5. **TT factor `1/4` and finite-age regularity of `hdot` — leading result
   confirmed; finite constants and derived budget endpoints require
   correction.** With two polarizations, `e_lambda:e_lambda=2`, the stated
   per-polarization spectrum, and Isaacson's normalization, the coefficient is
   `hbar*c/(2*pi^3)`, exactly one quarter of the earlier
   `2*hbar*c/pi^3` leading-log normalization
   (`R15-2_report.md:191-199`; `r152_referee_checks.out:18-21`). Including the
   repaired gain also removes the white boundary term because
   `K=(f*J0)` has `K(0)=0`, so `hdot=K'*xi` has finite variance at every finite
   age, though it still grows logarithmically. However the worker checker uses
   `K'=f*J0'` (`scripts/r152_checks.py:133-151`); the correct identity is
   `K'=f(t)J0(0)+f*J0'`. The omitted `f(t)` changes the finite part while not
   changing the leading slope: independently, at `Omega*tau=1` the corrected
   slope is `0.338759` versus `|F(Omega)|^2/pi=0.338204`, but the effective
   constant approaches about `1.36`, not the asserted universal unfiltered
   `c1=0.657` (`r152_referee_checks.out:22-26`). Hence the exact `0.2524`, the
   universal `c1` in `R15-2_report.md:193-198`, and TT budget endpoints that
   use that finite constant are not confirmed as written; the leading `1/4`
   result is.

6. **Exact-limit CP — not yet confirmed.** Each explicitly realized finite
   Gaussian network is CP by unitary evolution, homodyne instrumentation,
   causal feedback, and partial trace, and the positive-real approximants have
   a sound record-side covariance convergence test
   (`R15-2_report.md:172-179`; `scripts/r152_checks.out:37-44`). But the check
   proves trace-norm convergence only for the displayed classical covariance
   `A_N A_N*`. It does not construct convergence of the full quantum
   instruments/maps, including the backaction and internal-vacuum initial-state
   contributions; “bounded” total arcsine mass is not such a convergence proof
   (`R15-2_report.md:180`). This is the same distinction the earlier referee
   made between finite rational CP and the exact irrational limit
   (`C5_R13-6_referee.md:224-233`). In addition, saturation of the correlated
   scalar two-port trade-off is explicitly only suggested
   (`R15-2_report.md:174`). The strongest result is finite-approximant CP plus a
   convergent record covariance; exact full-model CP remains conditional on a
   quantum realization/domain and pointwise channel-convergence proof.

7. **Constraint-channel `|u1|` — formula and arithmetic confirmed as a
   conditional per-channel benchmark; premise (iii) is not established.** From
   the assumed `S_phi=hbar*g|F|^2/(2k^2)` and static quadratic magnitude
   `(2g)^-1<|grad phi|^2>`, the factor `g` cancels, the Gaussian spatial integral
   is `1/(8*pi^(3/2) ell^3)`, and the independent temporal integral gives
   `I_F=21/32`. This reproduces
   `|u1|=hbar I_F/(32*pi^(3/2) ell^3 tau)` and all four quoted ratios to
   `rho_Lambda` (`R15-2_report.md:226-240`;
   `r152_referee_checks.out:28-33`). What is not derived is that constrained,
   gauge-dependent scalar/vector metric noise possesses this separately local,
   non-cancelling stress and gravitates as a homogeneous cosmological source.
   The scalar exchange is itself indefinite, signs/cancellations are admitted
   to be suggested, and a nonlinear covariantly conserved completion is absent
   (`R15-2_report.md:242-245,273,279`). The analogous prior H-cosmo inference
   was already judged conditional on an unproved gauge-fixed energy
   identification (`C5_R6-4_referee.md:210-217`), while the axioms require a
   separate source/action and physical-observable bridge
   (`MINIMAL_AXIOMS_2026-06-29.md:85-90,173-190`). Thus the overshoot is valid
   only if premise (iii), the least-decoherence split, and no compensating
   cross-channel or subtraction term are all imposed.

8. **Reading — `OPEN` confirmed.** The fixed rule requires an explicit model
   passing every stated test, checked, for `VIABLE`, and a refereed
   inconsistency for `EXCLUDED` (`TESTS.md:4939-4951`). The linear
   conserved-noise and Bianchi constructions rule out the named example of an
   immediate exclusion. But exact-limit CP is still conditional; Lemma CU is
   narrower than stated; the second-order PPN coefficient is only power
   counting (`R15-2_report.md:202-210`); and the constraint-energy conclusion
   depends on premise (iii). These leave search regions, not a checked viable
   model, exactly as the worker ultimately says (`R15-2_report.md:247-250`).

## Strongest correct statement

For nonzero spatial momentum in linearized GR, a conserved source decomposes exactly into a two-polarization TT exchange carrying the sole massless light-cone pole and time-local scalar/vector constraint exchanges, so the R11/R12 cone no-go forces finite age only in TT. The repaired gain has `f(0)=f'(0)=0` and zero first moment: it supports an ordinary finite-variance conserved S/V noise process from `t0`, while truncating the filtered matter source at `t0` creates the exact boundary divergence `f(t-t0)T^{0nu}(t0)`, cancelled by the displayed initial-memory `B`, which decays for arbitrary initial data when the first moment vanishes. Under the report's TT spectral normalization the Isaacson leading-log coefficient is exactly one quarter of the earlier O(1) estimate, and `hdot` is finite at every finite age, but the worker omitted the `f(t)J0(0)` derivative term, so its finite constant and dependent budget endpoints are not exact. Equal channel gains cancel instantaneous constraint tails only within the restricted channel-diagonal gain ansatz; full no-signalling is not proved. Finite rational instruments are CP and their record covariances converge, but exact irrational full-instrument CP remains conditional. Finally, `|u1|=hbar(21/32)/(32*pi^(3/2)ell^3 tau)` and its quoted numerical overshoot are correct per-channel algebra if constrained metric noise is assigned the assumed static gravitating energy, but that gauge-invariant nonlinear premise is open. The strongest fixed reading is therefore **OPEN**, neither VIABLE nor EXCLUDED.

