# ENS Ramsey parity observable: source review

Bounded source/observable review, 2026-09-27. The Ramsey observable uses the full ground-to-sixth-level energy frequency, not that frequency divided by six. However, the separation of two positive Fourier peaks equals the full parity splitting only when their signed detunings have the same sign. Without this sign information, the visible separation is a lower bound on the full splitting. This distinction must accompany any envelope comparison. No model fitting or numerical spectrum calculation was performed here.

## Primary source and observable derivation

Lescanne et al., “Escape of a Driven Quantum Josephson Circuit into Unconfined States,” Phys. Rev. Applied11,014030(2019), published16January2019, DOI10.1103/PhysRevApplied.11.014030. The local PDF is the published article, obtained previously from the authors' ENS site. Read AppendixC/D and Fig.6/7 in full and visually inspected the preserved page9 rendering. Local text references below count newline lines.

AppendixC, printed014030-8, text543–563, defines omega_0k=(E_k−E_0)/hbar and a k-photon drive at omega_0k/k. The Ramsey sequence consists of two pi/2 rotations separated by variable delay, followed by sigma_z measurement. Fig.6 caption, text506–514, describes fitting Fourier transforms of exponentially decaying cosines and two components for k=6. AppendixC continuation, printed014030-9, text573–581, explicitly checks that changing the single-photon drive detuning by delta changes the Ramsey frequency by k*delta/(2pi). This source check establishes the full energy-frequency convention.

Write F_a=f06(ng)=(E6(ng)−E0(ng))/h and F_b=f06(ng+.5), in ordinary frequency units. At a common six-photon drive frequency f_d, signed Ramsey detunings are d_a=F_a−6f_d and d_b=F_b−6f_d. Their difference is F_a−F_b: the drive cancels and there is no division by6. The ground-energy contribution must be retained; this is a transition dispersion, not just E6 dispersion. For a cavity-coupled model, use the consistently assigned zero-cavity dressed transition on both parity branches rather than silently mixing bare and dressed observables.

The FT of a real Ramsey cosine displays positive frequencies r_a=|d_a| and r_b=|d_b|. Therefore:

- If d_a and d_b have the same sign, |F_a−F_b|=|r_a−r_b|.
- If signs differ, |F_a−F_b|=r_a+r_b.
- In either case, |r_a−r_b|<=|F_a−F_b|.

The absolute detuning signs or exact Fig.7 drive reference are not established numerically in the inspected caption/text. Symmetric motion around a nonzero FT center is consistent with a same-sign interpretation but is not an independent sign measurement. Do not promote visible difference to unconditional exact splitting. Conversely, dividing the Ramsey difference by6 would convert to a drive-frequency splitting and is incorrect for comparison against the energy-frequency difference requested here.

## Charge offsets, figure scope and uncertainty

AppendixD, printed014030-9, text583–600, attributes the doublet to quasiparticle-induced switching between Ng and Ng±1/2 and states that16-second Ramsey measurements average those configurations; Fig.7 caption, text567–572, says measurements repeat every32seconds over about2hours and drift over minutes. The millisecond switching timescale is discussed with reference38, not supplied as a new independently fitted switching-rate curve for this record.

Thus parity branches coexist in each averaged record, while an unknown background offset drifts. This does not establish ng=0, a uniform offset distribution, equal parity probabilities, an arithmetic average of extreme endpoint transitions, or that the observed time record reaches the maximum possible parity splitting. It also does not identify a charge trajectory from the frequency record without an assumed model.

Corrected on subsequent extraction review: Fig.7 has labeled FT ticks2.5–20MHz and an actual plot bottom near.664MHz, with a roughly two-hour time axis. The PDF contains mixed paint, including vector heatmap rectangles; the viewed PNG is a raster rendering, not the sole underlying source representation. It is not a table of fitted separations with uncertainties. Fig.6 provides fitted Fourier traces but no Fig.7 per-time covariance/error table. No quantitative experimental uncertainty for a digitized maximum or branch separation is supplied in these appendices. Pixel localization, linewidth, finite Ramsey-delay sampling, finite acquisition duration, overlapping components and drift are distinct limits; none becomes a Gaussian error bar just because a feature can be digitized. No precise splitting estimate was extracted by this review.

The16seconds is acquisition duration for each Ramsey measurement, not free-evolution delay or parity residence time. It cannot be inserted as a coherent evolution time. Likewise, averaging switching configurations produces multiple Fourier components; it is not the same as replacing the Hamiltonian by an average of two endpoint energies.

## Calibration independence and 2024 linkage

Read the existing ENS protocol/results and complete calibration/model/evaluation scripts without importing them. The extended model's optimizer indexes exactly f01,f02,fres1,fres2,fres3; the five inputs calibrate EC,EJ1,Omega,G,tau. The cosine baseline uses only the first four. The saved calibration JSON confirms these keys and matches the pinned CSV hash. The parity split and Fig.7 data do not enter that optimizer, its starts, stopping or cost-only solution selection. Evaluation divides full f0j by j only for its separate drive-frequency residual reporting; that division must not be carried over into this Ramsey observable. The existing endpoint-halfspread drive field is neither the full Ramsey parity difference nor its full range over background offset.

The pinned Experiment.csv ENS row contains full f06=29.1888GHz and f01/f02/cavity frequencies but no Ramsey parity-doublet column. Thus the parity observable is algebraically unused calibration information. This is still retrospective testing: the prior protocol discloses source/full-CSV exposure and source discussion of parity was already read. Independence from the optimizer is narrower than experimental independence, blindness, or freedom from shared systematic/model assumptions.

The locally preserved Willsch2024 primary article explicitly calls ENS the “same device as in ref.40” (text2054–2061); reference40 is Lescanne2019 (text3381–3385). This supports device identity, not identical cooldown, charge offset, calibration epoch, power shift or exact reuse of the Fig.7 acquisition in the later numerical CSV. Those stronger relations were not established here. Preserve the2019 parity-data versus2024 tabulated-calibration provenance rather than treating them as simultaneous observations by default.

## Meaning of envelope compatibility

For a fixed calibrated model define D(ng)=|f06(ng)−f06(ng+.5)| and independently evaluate its charge-offset envelope with appropriate convergence/assignment checks. An observed FT separation above a rigorously supported model maximum would contradict that model/observable mapping even without known detuning signs, subject to measurement and source-identity uncertainty. An observed separation below the maximum only passes a necessary capacity check; it does not fix ng, certify the Hamiltonian, select Andreev versus another harmonic mechanism, or establish precise frequency agreement.

If same-sign detunings are assumed, an observed splitting lying inside the model envelope establishes existence of a compatible offset, not a prediction of that offset or a statistical fit. With unknown signs the admissible full splitting must also consider the sum of observed FT frequencies. Do not match an arbitrary background offset to data and then call it independently predicted. A plotted supremum need not have been sampled experimentally, and a finite ng mesh is not automatically a rigorous envelope. Parameter-rounding corners and cutoff controls are model/numerical sensitivities, not source confidence intervals.

## SHA256

Paths are relative to `../ens-independent-cavity/` unless stated otherwise.

- `Lescanne2019.pdf`: `49fd0df0facd4579af9c29d2ac0b91cf52badadb930134053d5d63c89c084382`.
- `Lescanne2019.txt`: `0b980d81d5a8293b361256ede22c0ff093d9ed7c77cac8982006a5e36e6b8b5c`.
- `PROTOCOL.md`: `26b6e2f99375e9df5d17caa338a1fade2ed15470cb1c9aa59caf9333bedfae88`.
- `RESULTS.md`: `f3fa6382566d91a948bb34b3b44c549c010b5b007b4e144e20c7a423d86f8392`.
- `calibrate.py`: `2b70f60ab9f4a6a675041b927171c703b25dc351381d165497e6910fa0b62e76`.
- `calibration.json`: `a29d0a620d69f34aea0df124e94a7438206ccc6efe0970f815aca2549d99a284`.
- `model.py`: `6129a23fe0d9cb6cf1b0862702650e13c6a607d0cb6f0208042247a9e53c6090`.
- `../stronger-test/Experiment.csv`: `0b6abf45a5b574f2ecc492b19560d44ff1638894a0579504dc850c1cb628a01b`; pinned upstream commit d97280c61c54ca8d54ccf0a8706713130778eb63 per existing dataset provenance.
- `../willsch2024.txt`: `8cd4c52f2fe5f52ccda97d8a657c571266387f79cdb5226c53694daa53fce187`.

Extraction-review correction: the earlier “0–20MHz” and raster-only wording above was misleading and has been corrected explicitly. No Ramsey-observable or detuning-sign conclusion changed. See `PARITY_EXTRACTION_REVIEW.md`.
