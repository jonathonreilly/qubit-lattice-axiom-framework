# Attack on T41: Cross-sector quark determinant readout (theta mass side) is an open obligation

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor, Opus 5.5; same-family checks only).

Read: `docs/MINIMAL_AXIOMS_2026-06-29.md` in full; `PRIMITIVE_REGISTRY_CHECK.md` (no primitive gives a mass matrix, K/CPT or an index). Also the theta and quark-CP notes cited, lane files L08/L09/L11. No open PR (36 checked) or archive note solves it.

## Verdict in plain words
Closing this wall would show only that a record readout cannot see the quark mass phase, not that the phase is zero. On the repo's even-lattice surface the phase couples to nothing and a positive determinant needs no lepton input. Where a phase can couple (nonzero index), the readouts stay blind while the weight carries the phase, and a discrete sign bit returns that the flavor fits neither fix nor see. So the wall is misframed; the live items are an index supplier and the joint theta-bar assembly (T42/T43). Strong CP stays open.

## The wall (checked)
- Plain: Strong CP needs the overall phase of the quark mass matrix to be zero. The repo can show this only if the quarks' determinant readout is the same channel as the charged leptons' counting rule. That quark object is unbuilt; the quark fits set the phase by hand.
- Precise: Target: construct the quark mass/determinant carrier and physical readout, and prove correspondence with the charged-lepton K/CPT occupancy carrier, so arg det(M_q)=0 follows unimported. Similarity and shared notation do not count (`docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md:21-26`). The four members belong together.
- Real? Yes as an open gate, unsolved in docs/, archive/, open PRs; misframed as a route to the value.

## Load-bearing premises
| Premise | Kind | Path:line | If wrong | Tested? | Cheapest test |
|---|---|---|---|---|---|
| No mass matrix, K/CPT, index in axioms | axiom (absence) | docs/MINIMAL_AXIOMS_2026-06-29.md:141-146,179-180 | wall not open | no-go 07-04 | none |
| Quark readout constant on K-orbits | supplied model | docs/KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md:60-62,89-116 | readout sees phase | witnesses only | S5 (done) |
| Block-multiplicative character | supplied model | docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md:44-57; MINIMAL_AXIOMS:220-224 (additivity removed) | k not forced 0 | no | rederive from Record text |
| Exhaustion: all phase effects pass the readout | hidden, now explicit | docs/THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md:62-70 | blindness irrelevant | no | S3 |
| Balanced grading, tr ε=0 | method | docs/THETA_ASSEMBLY_PAIRED_SHIFT_FIXED_GRADING_MCKEAN_SINGER_REDUCTION_NARROW_THEOREM_NOTE_2026-07-02.md:41,84-88 | pairing fails, phase live | proved | S2 |
| Hermitian flavor block, K-real surface | supplied model | docs/THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md:72-105 | arg det leaves {0,π} | runner | S1 |
| Quark carrier shares lepton orbit indexing | reading | obligation note:9-26 | K-transport fails | never | S5 |

## Routes
| Route | Approach | Premise dropped | Must believe | First artifact | Cost | Changes | Verdict |
|---|---|---|---|---|---|---|---|
| R1 index first (misframe) | graded operator, tr ε≠0; paired-shift law | cross-sector identity | strong-CP content lives in index sectors | Lemma: class readouts phi-independent (S3) plus exhaustion ⇒ no supported index sector. Missing: exhaustion. | lemma low; supplier high | folds T41 into T42/T43 | survives as reframing; the supplier is T42-hard |
| R2 parity plus positivity (outside) | left-right parity gives Hermitian M (Beg-Tsao PRL 41, 278; Mohapatra-Senjanovic PLB 79, 283; 1978); positive det(D+M) (Vafa-Witten PRL 53, 535, 1984) | readout identity | an improper symmetry exists | Missing: parity from Admissibility; Lattice gives proper rotations only (MINIMAL_AXIOMS:38,58) | high | T43; orientation bit L11-W2 | wounded: equivalent to the orientation bit |
| R3 build the quark carrier (lane's own step) | Hermitian NNI atlas vs circulant | none | atlas carriers hold the sign datum | S4, S5 | done | none | dead: carriers lack the datum |

## Test run
- Pre-registered (`T41_scratch/PREREG.md`, before running). Pass: phase erased on the balanced surface with no lepton input; phase = ν·arg det m on the graded surface; class readouts phi-independent; atlas observables blind to eigenvalue signs. Fail: phase visible on the balanced surface, or readouts vary.
- Script: `T41_scratch/t41_test.py` (`results.txt`, `results.json`).
- Result: S1: Hermitian flavor block, 8 sign patterns, arg det 2e-15. S2: 32 graded cases, arg det O = ν·arg det m to 1e-15; ν=0 gives 0 for any complex m; a Hermitian m with one negative eigenvalue gives π at ν=±1. S3: |det| spread 1e-14 over phi; toy Z(0.3)/Z(0)=0.947, Im⟨ν⟩=0.36. S4: note reproduced (6e-7); M_u and M_d each have one negative eigenvalue, even at ξ=0 (c12_u=1.48>1), so arg det(M_u M_d)=0 is π+π; all 64 sign patterns leave masses, |V|, J unchanged (6e-12) while arg det takes 0 and π, 32 each. S5: K is a gauge relabeling for the lepton circulant but for neither quark carrier; J flips sign.
- Deviation: run 1 failed S4 only because I compared with atlas constants, not the note's numbers as pre-registered; fixed and rerun (`results_run1_S4_comparator_bug.txt`).
- Reading: supports MISFRAMED. S2 is the repo's paired-shift algebra with a flavor matrix; p_ν is a toy. It does not show whether the axioms supply an index.

## Outcome
MISFRAMED. Cheaper question: does the four-axiom lattice supply a grading with tr(ε|ker)≠0 (operator-dependent, taste-singlet, unbalanced)? If not, arg det M_q is inert and nothing needs erasing; if so, the target is the joint θ̄ = θ_gauge + arg det(M_u M_d), sign bit fixed by that supplier. Siblings: T42, T43 absorb it; T38 is not needed for the mass side on the balanced surface (reading).

## Claims and labels
- proved (landed, unaudited): forcing pairs make the readout phase-free, not the phase zero (KCPT note:89-116; 07-17 note:96-101); pairing gives det≥0 on the balanced Hermitian surface (07-01 T2, T3); tr ε=0 makes the transfer zero (07-02 C1).
- checked: S1-S5.
- suggested: T41 closure plus exhaustion implies no index sector (n≡0).
- reading: K is complex conjugation of mass data (CP/T-like); CPT holds for any arg det, so "K/CPT constancy" can only mean CP-blindness of one channel.
