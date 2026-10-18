# Focused neutral-domain resonance review

Disposition: DEMOTE the general-momentum original-observable claim; PASS in principle for finite native coefficients and the conditional expanded dark-half-line energy/width, subject to the narrow fixes below and the parent aggregate replay. This is source review, not an audit verdict or a landing gate.

Reviewed worktree `/private/tmp/scalar-environment-20261017`, HEAD a519e1a80698a0f12d2b05939200838bfdcc2f97; observed origin/main fa841753c1a6296e5ad45518375660b0f1004769. No source edits, verdict applications, or full numerical reruns by this reviewer.

## Required narrow fix

The note defines the original observable as the uniform sum O=Σ_j,a Z_j,a Z_j+2,a and uses a translation-invariant symmetric vacuum, but then assigns it a general-q source 2λ|0>−tλ²|1>/2 and residue 2Z(q)λ⁴/c². Translation invariance makes that uniform observable access only q=0. The source_dressing probe computes only the uniform source and uniform observable differences; it does not derive a Fourier-density observable at nonzero q. A Fourier density has phase-weighted configuration differences, so simply transplanting the uniform ΔO=-8,-16 is unjustified. Narrow the native original-observable statement to q=0, retaining residue coefficient 113594/57121, and label generic-q source/residue output as a prescribed effective-model probe. Alternatively define O_q and derive its actual canonical dressing before making the general-q native claim.

## Runner strengthening

The dark-rational probe computes exact kernels but does not assert their quoted values, and the aggregate only loads that result. Assert the complete L14/L16 kernels: 2_4 and 4_6 have -3/64 at offsets 0,2 and zero elsewhere; 4_4 has -13/96 at offset0 and zero elsewhere. Likewise assert H1norm≈0, H2mean≈−2 and H2res≈0 for checked even ell>=4; currently aggregate checks only H3norm. These are narrow acceptance checks for the actual claim, not an independent proof replacement.

State the q-certificate coverage explicitly: modes 0..floor(3L/8), L12,16, i.e. q<=3π/4 (L12's last allowed point is 2π/3). It is not a near-π closure certificate. The note already excludes a uniform π limit, but explicit finite sample coverage prevents confusion.

## Mathematical and premise assessment

Reused INDEPENDENT_KINK_SECOND_CHECK, INDEPENDENT_KINK_THIRD_CHECK, INDEPENDENT_KINK_FOURTH_CHECK, INDEPENDENT_KINK_MOMENTUM_CHECK, INDEPENDENT_KINK_RESONANCE_CHECK, INDEPENDENT_DARK_FOURTH_CHECK and INDEPENDENT_DARK_BOUND_CHECK. Their independent enumeration, canonical/Bloch contraction, Fraction kernels and manual half-line reductions establish the appropriate finite or conditional boundaries. Inspected the core, rational, source-dressing, q-certificate, dark-third, conditional-pole and dark-bound runners. The half-line ansatz gives r=T/v, E=b+v+T²/v and Z=1−r²; the q0 width is Z×9/32=511173/1827872. The old 9/32 is only the single boundary-channel loss coefficient, not the expanded native candidate's width. No consequential discrepancy in that expanded algebra was found.

The complete energy8 band argument is valid for the stated ordinary periodic rings (L>=3). Actual microscopic rung h and signed resolvents feed the finite calculations. The specified Hamiltonian, anisotropy, thin tube, positive parity and chosen symmetric ground representative remain explicit conditional inputs, not consequences of the minimal axioms. No new degree of freedom, interaction, fitted observational number, scale conversion or cosmological identification is imported by the displayed finite calculation.

Degenerate-channel scope is appropriately corrected: K4 d2 couples to d4, so an isolated d2 pole cannot be the native leading pole. The even-domain chain is conditional on all-length closure and completeness; finite projected kernels do not prove absence of other channels. Frozen full-column auxiliary results are visibly identified as frozen, with scripts and input hashes included. The leading rank-one loss premise remains essential. Add that width/residue asymptotics require fixed q away from dark binding thresholds |v|=|T| as well as away from π; the strict inequality alone does not supply uniform threshold control. The π/3 cancellation is correctly not called a protected stable state.

The proposed next hard residual—connected-support/all-length closure followed by native finite-H response in the full degenerate basis—is correctly named. Current evidence does not establish an infinite native pole, physical scalar, gravitational/environmental coupling, or empirical prediction. Those are explicitly open. No additional scientific computation is required to publish the honestly narrowed conditional support result, beyond the parent's existing replay/packaging checks.

## Source snapshot
- `docs/NATIVE_NEUTRAL_DOMAIN_RESONANCE_NOTE_2026-10-18.md`: `add61590f38df822e95f2fceb76abb26bb43ccb922e81f9ba0f6078fa51433c7`
- `scripts/native_neutral_domain_resonance.py`: `7e34effc4088af24aa412fd191b771643e84e41a56f81eff9edd3cef30074d9f`

## Same-session affected-fix confirmation

Final focused disposition: PASS for finite native coefficients and conditional expanded effective-model resonance/source, pending parent aggregate replay and repository mechanical gates. The source-scope finding is resolved.

The note now defines centered O_q explicitly and distinguishes uniform O at q0. The new physical_q_source probe constructs actual diagonal Fourier differences in computational configurations and compares them with independently phased native V_q and H1V_q. I inspected its complete code; its packaged output is not yet present and the parent replay remains required. Independently, a single two-bit flip changes the two centered NNN bonds by -4 each, giving -8cos(q)e^(iqj); the adjacent length-two support gives the consistent extra cos(q) factor at second order. Canonical cross terms still vanish because O_q is diagonal and preserves unperturbed energy subspaces, and all aligned vacua have the same O_q eigenvalue. Thus the displayed first/second source and leading residue 2Zcos²(q)λ⁴/c² are consistent. The effective pole and bound-math scripts now multiply their source/residue by cos(q)/cos²(q), respectively. The qπ/2 leading readout zero is explicitly stated without claiming all-order invisibility.

The aggregate now asserts exact dark kernels and stated H1/H2/H3 even-domain identities. Note coverage and dark-threshold caveats are explicit. No remaining actionable scientific blocker in this focused unit. Prior independent finite/algebraic checks remain valid; all-L completeness and native resonance control remain open.

Final affected source SHA256:
- `docs/NATIVE_NEUTRAL_DOMAIN_RESONANCE_NOTE_2026-10-18.md`: `9196443ebcee90efe5282f062d2a68ff0d07b408aeea3b7ac8f2b071f8f4723d`
- `scripts/native_neutral_domain_resonance.py`: `fe3dd66dab4df611129d460aeae8b137599a9a0a1292fa7d7849583c9399d8bd`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_physical_q_source.py`: `1e34c264518527172fe81070b4bd9f0c622f8aae3756fbf581b80c70abe4a6f1`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_kink_dark_resonance.py`: `cd14169b2b9d5a0ff5f93d3c88cbaa1a29bd96876b03ad5ce2d3e4ce0b411193`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_dark_bound_math.py`: `cd821809563dbf58bc94cf19b6c304eaf06685f06460e7b53e92b16aef5cb6b2`
