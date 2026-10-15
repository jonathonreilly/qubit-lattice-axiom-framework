# Focused canonical mathematical and source correspondence

## Scope and result

This is a post-exposure source comparison by `/root/force_energy_bridge_check`; `/root` remains author. It is not a formal claim audit, a publication approval, an integrated-main check, or a new observational result. I read the complete initial canonical note and both Python sources, then inspected every byte delta to the final snapshots below. I also read the complete fixed synthetic protocol used by the primary runner. All source snapshots and successive diffs were frozen before their corresponding semantic comparisons.

The final formulas and implementation agree with the independently frozen reconstruction in `INDEPENDENT_MATH_v1.md`, within the stated action, regularity, nondegeneracy and physical-input premises. One new scope finding about matter-theory solution membership was sent to the author and repaired. Both earlier working-note findings—background versus geometric coupling and the normalization of the canonical field—are explicitly repaired. I found no remaining mathematical/source discrepancy in the checked final snapshots. This conclusion does not certify unexamined numerical receipts, literature/data accuracy, a measured action, or a matter/gravity calibration.

## Exact source and exposure identities

| Final source | SHA-256 | Complete coverage |
|---|---|---|
| `docs/SCALAR_COSMOLOGICAL_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md` | `c8e52d53d2e2a4c02bc784668665e7d0c635c208492d32ebe968dd0e73bc8078` | 375 lines, 20,906 bytes; initial 373-line note read fully, followed by complete exact delta |
| `scripts/scalar_cosmological_inverse.py` | `1bf2d30207b99cea8508a612a739ed8b82dc7d6860920e101fb4e1374eccd9be` | 434 lines, 20,416 bytes; all functions and assertions read, including both later fixture additions |
| `scripts/scalar_cosmological_inverse_check.py` | `df487184eb73a347b1c5c6aacc641d49ea482cac75e2494dac15dcd6d07923ca` | 60 lines, 3,087 bytes; read completely; unchanged |
| Campaign `action_selection/SYNTHETIC_PROTOCOL_v1.json` | `7f504a86f3e82cbcc7129ba7c2233b044430e70b7ede1ad82564c298f9ea3ab1` | Entire JSON, all twelve cases, calibration/residual indices and tolerances |

The note's first exposed canonical hash was `e4025969133e49394328cf628dc2797d041cd643ba7785953f5bc495fbdef53a`. Its final delta adds the matter-solution qualification, changes the matching import-ledger phrase to “metric/scalar solution membership,” and restricts the quoted cancellation maximum to case9. No equation changed.

The helper's first exposed hash was `d3b96bb4d5530aee99805cfc1515b694da58e713441c5e19c08068dc3668eb66`. The intermediate hash `435d7b03a8038a8bf2eddef1122e7123953d046071df2136f23f359412f27bd7` adds only the implemented curved-history fixture. The final helper adds only the nonzero-pressure fixture. The exact diffs and all original copies remain alongside this report. The helper's computational formulas did not change during this final comparison.

Earlier independent source, proof, controls and their freezes remain unchanged. The independent report hash is `aa6f275dd043529fc824a00b0ebdbb190abf610a6ddfb9fc1e4ecad81edaa21a`; its identity is `50a88fbcc91f8ca007e1ba7d7f2d96c4aa3c5dbf1dc0c439722d7a06be612efa`. The prior working-note comparison is `8b785b2a52d6d42dd8f4fe5e17d5af41bc8acbc41a9899b027de04eeb393f05f`, identity `de25bdc2bc55d680be3c970aafd0b7336891b5d5f894adc7207d72e19f29ac9e`.

## Independent oracle and what was executed

The pre-exposure derivation began with the complete supplied action note (SHA `39a0dd9e107edba23adbfe8cf070f8f279190c40c651dc905af9d59911cad000`). It derived the Jordan metric equations, reconstruction, Bianchi implication, candidate inverse, transverse inequality and plateau counterexamples without opening the author's new derivation or code. The preserved independent run passed 42 controls: 39 exact algebra/rational controls and three ordinary floating chart round trips. Its program hash is `c043596f9cf7c76c7b67eaf2745ee246c2c1950a3b247c52a6fafb1fabb63979`, result hash `c860bf5331c7f03f5d317a9b7ec41d54c4a57c5bed01ffbb8125efb12b48f0bf`. No failed independent attempt was discarded or repaired.

The earlier report discloses the coordination messages received after the independent proof and control code were frozen, including the author's case9 failure. The source comparison here is explicitly post-exposure. I did not run either canonical source, its aggregate, the source-bound cache, mutation variants, or the author's numerical history/precision-diagnosis programs. The executed commands for this comparison only copied, hashed, displayed and recorded source. Exact fixture values below were checked by direct algebra, not claimed as a new numerical execution. The author's synthetic executions remain author evidence; they are not part of the 42 independent controls.

## Metric reconstruction and scalar sufficiency

With the action convention `F R/2 - Z(F)(partial F)^2/2 - V`, the note's `Z=omega/F` is consistent with the independent notation. For physical Jordan time and `chi=kappa/a^2`, the independent combinations are

`D = -2F(Hdot-chi) - (rho+p) - Fddot + H Fdot`,

`V = F(3H^2+Hdot+2chi) - (rho-p)/2 + Fddot/2 + (5/2)H Fdot`.

The implementation `metric_readout` uses these signs and coefficients exactly. It rejects nonpositive F and divides by Fdot only when nonzero. A zero denominator in the optional q readout returns None; this is not treated as a healthy reconstruction. The candidate inverse separately imposes positive D, changing F and the candidate domain.

The scalar implication is local on a connected interval where Fdot is nowhere zero, with conserved matter and actual FLRW curvature evolution. Differentiating the Friedmann equation and combining Raychaudhuri gives the scalar equation multiplied by Fdot. The helper's symbolic total derivative includes `chi_dot=-2H chi` and matter conservation. Its eliminated-trace scalar expression has the correct `(rho-3p)`, potential and omega-derivative signs. It does not silently divide on a plateau.

The repaired note correctly distinguishes Einstein positivity `2omega+3>0` from the stronger candidate D positivity. The field `chi` in the distance paragraph is explicitly dimensionless K-metric distance, with Einstein kinetic convention `-Q(partial chi)^2`. The conventional dimensionful canonical field is `varphi=sqrt(2Q)chi`. This resolves the earlier normalization finding.

## Candidate-specific inverse and full-field restriction

The supplied action has kinetic normalization `-Q K_AB partial phi^A partial phi^B`, not one half of it. The complete diagonal transverse metric, conformal coupling and full potential are stated. The conformal identity is

`D = c Fdot^2/(F-Fc) + 2F Tperp`,

where `Tperp=Kxx xdot^2+Kyy ydot^2>=0`, `c=(1-3a_c)/(2a_c)`, and `Fc=Qs/(1+s)`.

The inverse `Y=Fdot^2/D`, `Y=(F-Fc)/c` on the exact radial truncation gives the stated two-point formulas. The chosen root `k=(1-2sqrt(2c/(2c+3)))/3` is the unique one in `0<k<1/3`; the other algebraic root is outside that domain. The tests `0<c<1/2`, Fc positive, F>Fc, distinct F and Y, and positive D/nonzero Fdot are necessary. Code enforces these two-point gates and checks the chart again for later residual rows. It cannot turn finitely many synthetic samples into an interval proof, and the note does not claim that.

The recovered normalization `Q0=4a_c Fc/(1+k)^2` and `Q=Q0(1+k)` agree with the independent derivation. In the potential inverse, the note uses `V/F^2=L B0+T B1` with `L=2Hv^2/Q`, `T=L nu`; this is algebraically equivalent to the independent basis expressed directly in F. The code solves the two-by-two system with the correct determinant/signs, rejects rank loss and nonpositive L/T, and reconstructs Hv and nu correctly. At u=0, B1=0: nu is not determined by a vacuum point. Numerical determinant tests and reported ordinary-float condition numbers are diagnostics, not verified lower bounds on rank under uncertain observations.

The q distinction is now exact:

`1/q_rec = 1/q_geom + 4F^2 Tperp/Fdot^2`, `q_rec<=q_geom`.

Here `q_geom=a_c/J` is fixed by the field-space coupling; `q_rec` is formed from the total background stress. The code's result key `q` implements q_rec. Its comparison with the source geometric q occurs only on generated x=y=0 histories, as the note explicitly states. That name does not conceal a general identification in the checked scope. The symbolic control also checks the full relation with Tperp.

For a full solution, equality in the kinetic inequality at one instant only sets transverse velocities to zero at that instant. Equality throughout an open interval sets both velocities to zero throughout, hence makes both coordinates constant. Diagonality, transverse independence of Kuu and the conformal coupling remove radial connection and transverse matter terms. The remaining equations require `Ux=k x exp(-(1-k)u/alpha)=0` and `Uy=(2k/3)y exp(-(1+k)u/alpha)=0`. Positive k,Hv and finite fields then force x=y=0. This is the correct open-interval argument. The note does not replace it by two fitted epochs, approximate equality or constancy of only one transverse coordinate.

## Converse membership finding and repair

The forward identities are necessary conditions. The converse additionally assumes the identities hold throughout the smooth monotone interval with a single set of admissible parameters and the specified curvature/conserved source. Reconstructing u(F), setting x=y=0 and imposing the exact potential identity then satisfies both metric equations. The nonzero-Fdot Bianchi implication supplies the coupled scalar equation, while Ux=Uy=0 supplies the other two. Two nondegenerate calibration pairs determine the parameters uniquely inside this specified chart, not among all actions or unsampled field-space extensions.

The initial canonical note called this a solution of the candidate without expressly separating the matter field equations. I raised finding C1: a supplied conserved stress tensor does not by itself construct psi solving an arbitrary fixed matter action S_m. Root accepted it. The final note now says “candidate FLRW metric/scalar system with the stated conserved physical fluid” and expressly requires a supplied matter solution for complete S_m membership. The import ledger was narrowed consistently. `CANONICAL_FINDING_C1_v1.json` preserves the original finding and exact repaired identity. No mathematical correction to the metric/scalar reconstruction was needed.

## Plateaus, scale freedom and observation mapping

A constant-F history does not determine a kinetic coefficient by the quotient above. Even when its metric equations hold, the scalar equation is separate. The dust-plus-Lambda example uses D=0 and the positive full-field kinetic metric to force all scalar velocities to vanish; then a fixed potential gradient cannot balance a changing nonzero dust trace. This is a conditional exact-domain counterexample, not an exclusion of fitted cosmology. A vacuum plateau can instead be a solution and leave shape parameters undetermined; the final note does not claim all plateaus are impossible.

The simultaneous scaling of F, rho, p and Q0 preserves the relative reconstruction while leaving absolute gravitational normalization unknown. Hv can be calibrated in supplied physical time units, but Hv^2/Q0 cannot be fixed without absolute normalization. The tensor coefficient F is explicitly not identified with a force-measured Newton constant.

The tensor transport discussion is consistent with the post-exposure derivation recorded in the working-note comparison: geometric optics gives conserved `F A_h^2 k`, hence the endpoint amplitude factor and inverse distance factor. Equal local endpoint coefficients can telescope despite an intervening changing background. The sharp-jump reflection/transmission example correctly demonstrates a failure of the adiabatic domain, not a dynamical screening result. These statements require the declared source/detector, beam, mode-conversion and smoothness premises. No environmental solution or measured F history is provided.

I have not independently read the external papers, accessed GW summaries, or validated literature equation numbers in this canonical pass. The literature and empirical-input portions were read completely for consistency with the mathematical claims, not treated as verified external measurements. The note's refusal to infer an action from one exposed distance pair and its zero-independent-empirical-test scope are appropriate.

## Implementation and precision scope

I checked all functions in the helper and the complete primary. The source-model construction differentiates the supplied radial action. The synthetic ODE uses Einstein dust conservation `rhoE_dot=(-3HE+b udot)rhoE`, the action-normalized matter source `-b rhoE/(2QK)` in the scalar acceleration, and `HEdot=-K udot^2-rhoE/(2Q)`. These signs agree with the action. The physical conversions use `dt_J=A dt_E`, `a_J=A a_E`, `F=Q/A^2`, `rho_J=rhoE/A^4`, and the correct Hdot/Fddot chain rules. The five-point derivative check divides the Einstein-time derivative by A. These are independent checks of source correspondence; they are not an independent ODE run.

The protocol fixes twelve synthetic cases, samples 0 through16, calibration indices0 and6 and later residual indices7 through16. The implementation uses those same fixed choices, with the protocol's unchanged parameter and residual tolerances. It hard-codes the current sample/index values rather than treating them as a general configurable API; that matches this frozen protocol. The later rows are synthetic residual controls and not empirical holdouts.

The canonical source uses ordinary double-precision DOP853 trajectories. `readout_from_state` then reassembles model-generated physical readouts at 50-digit arithmetic from saved rounded states and the supplied source-model parameters; the general inverse receives the resulting readouts. Recovered rhoE and aE are computed from the saved rounded Jordan row. This does not recover information from an actual rounded measurement, and it is not a 50-digit trajectory. The separate path lifts already rounded readouts before inversion and expressly tests that the original case9 failure remains. The note/primary preserve that distinction and do not claim improved observational precision. I did not independently reproduce the quoted case9 error, cancellation maximum, condition number, 50/80-digit diagnostic or original 90/91 result; those numerical values remain author/reviewer evidence outside this source-only pass.

The two final helper additions correctly exercise implemented non-flat and nonzero-pressure paths. Direct substitution at F=t, H=1/t, curvature=2/t^2 and t=2 gives D=7/2, V=17/4, q_rec=1/17. Changing rho to3/10 and p to1/10 subtracts2/5 from D and1/10 from V, giving31/10 and83/20. No root aggregate execution was needed to confirm those values or the limited diffs.

The primary binds itself, note, helper and fixed protocol by SHA-256 in its output, labels the surface conditional-support, reports no observed action/state/gravity selection, and preserves the numerical limitation in its result metadata. It exits nonzero if a control fails. I inspected this behavior as source and did not verify a current cache or execute its outputs.

## Remaining limits

This comparison supports the stated conditional inverse and its implementation correspondence. It does not supply physical H,F,rho,p and their derivatives, uncertainty propagation through the ill-conditioned inverse, absolute units/gravity calibration, source/environment matching, a complete matter realization, an initial-state principle, action selection among alternatives, or a TOE. It also does not certify finite precision, all candidate histories, arbitrary transverse motion reconstruction, literature/data accuracy, author result receipts, mutation strength, or publication/integrated-main compatibility.

The 42 independent controls, working-note findings, initial canonical finding, intermediate snapshots and final source identities remain distinct and immutable. No canonical/shared source, Git state, process, lock, graph, cache, PR or campaign ownership file was changed by this check.
