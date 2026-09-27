# ENS final publication-source review

**Disposition:** no consequential numerical, data-isolation, adaptation or claim-scope defect found in the reviewed revision. No source correction is requested by this check. This is a selective independent review of the four named publication sources, not an audit or a fresh independent experiment.

## Scope and unchanged evidence

Read the complete open-gate note, primary orchestration and two imported model files. The primary model is byte-identical to the previously independently checked model.py. The direct helper's potential and solve function ASTs match the independent checked implementation, with the sole function change replacing the frozen global default parameter vector by None; the primary supplies the fitted vector explicitly. The adaptation removes file reads and exploratory execution without changing the operator, Fourier construction, labels or residual calculation. Its 140-term binomial construction is used at the checked selected tau≈.155; this review does not turn it into a uniformly certified approximation throughout the full optimizer bounds.

Prior direct-basis derivation, charge/photon convergence and sampled continuation evidence remain applicable to the unchanged selected point. Both implementations still share SciPy, as the note discloses. The note identifies larger independent cutoff and continuation checks as original development evidence; the fresh primary's direct call itself checks the nominal endpoints only.

## Calibration and numerical claims

The primary passes only the five declared calibration values into construct(). All initializations, nominal fit selection, fifth-line perturbations and rounding refits use those values and predetermined perturbations. The cosine baseline uses four inputs. Higher qubit and cavity values are converted to numbers only after construction and all refits finish. The final nominal-improvement assertion evaluates the already frozen predictions; it does not tune parameters or select among them using holdouts. The CSV hash is enforced. There are no reads of historical fitted parameter files in either helper or the primary.

The completed publication_runner.log was inspected rather than repeating its complete optimizer workload. It reports exactly the previously checked successful tau=.2-start parameters, retains the two iteration-limit failures, and matches the note's nominal residual table and cavity values. The selected calibration residuals are below1e−12GHz, and the scaled Jacobian condition number is about202630. The quadratic stability margin 4EC−G²/Omega is about0.7322006GHz, positive as claimed.

A fresh fine-primary forward calculation at the logged selected point was compared with the new direct helper outputs in the publication log: maximum disagreement is about0.000297Hz. The note's .001Hz statement is therefore supported. The coarse/fine maximum extended-model frequency difference is37.21Hz after converting MHz to Hz. The reported second/third potential ratios match the checked Fourier normalization.

## Sensitivity and interpretive scope

The runner log contains all32 extended and16 baseline printed-decimal rounding corners, with successful calibration checks. Their qubit-drive extrema reproduce every rounded range in the note. For each of the four transitions, even the largest sampled extended absolute error is smaller than the smallest sampled baseline absolute error; the stated improvement within these finite controls is supported. This does not compare equal numbers of calibration inputs, and the note explicitly says so.

Fifth-line ±1kHz perturbations move f06/6 by approximately±.123MHz. The ±10kHz residuals are approximately−3.561604 and−1.094048MHz, matching the prose. The additional ±50kHz cases are retained in the output and are not silently used to select a fit. Paired-offset samples move the f06/6 center by at most0.003106MHz and fres7 by about0.928679MHz. These match the stated limits and the acknowledged charge-convention concern.

The sensitivity ranges are clearly labeled sampled rounding controls, not outward-certified intervals, continuous-box enclosures, covariance propagation or confidence regions. The note correctly avoids turning the initial1MHz practical scale into an ENS uncertainty. It distinguishes nominal improvement from agreement within measurement errors, preserves the highest-transition residual, and does not infer unique transparency, mechanism or global parameter identifiability.

The open_gate/conditional-support language is consistent with the actual deliverable: a conditional numerical comparison using an imported physical family and a separate calibration observable, with physical identification and uncertainty still unresolved. No native square-regulator mapping, unbounded coupled-device theorem, statistical acceptance or retained status is asserted. The final PASS categories retain their computational meaning.

## Verification limits and identities

This review checks orchestration and source/prose alignment, reusing valid prior independent forward-model evidence. It does not independently rerun all sensitivity optimizations or re-audit Lescanne's experimental precision/readout analysis. The original source/protocol disclosures and withheld-observable scope remain premises. No author files were edited, committed, merged or audited.

Exact SHA-256 identities of the reviewed revision and inspected completed output:

- `docs/ENS_CAVITY_CALIBRATED_HOLDOUT_OPEN_GATE_NOTE_2026-09-27.md`: `2bc76041d8d753f5214518497c562b58426319dd8ae336dce09fb940af76f585`
- `scripts/ens_cavity_holdout_2026_09_27.py`: `731c052053d5b9c728c5525149991c136dcfe6ca32df6c40a400a2ea91befec7`
- `scripts/ens_andreev_resonator_model_2026_09_27.py`: `6129a23fe0d9cb6cf1b0862702650e13c6a607d0cb6f0208042247a9e53c6090`
- `scripts/ens_direct_charge_check_2026_09_27.py`: `d0a1c247b4d44633d90fc0d91168256e64edee42c57ad41716cc95e4cff91dbe`
- `.claude/science/physics-loops/ens-cavity-holdout-20260927/publication_runner.log`: `473f9daae4b17c79f19949408f5729f589f21ab9bff71a61083b894f62e34f10`
