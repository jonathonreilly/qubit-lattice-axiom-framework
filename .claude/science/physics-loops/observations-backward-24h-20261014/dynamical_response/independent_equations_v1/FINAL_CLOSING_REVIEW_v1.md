# M14 final note and saved mutation evidence: closing supplement

This is a narrow post-exposure source and evidence correspondence check. It supplements the unchanged independent equations, canonical source, affected-source and sharp-envelope reports in this directory. Root remains the scientific author. No science, aggregate, ODE or mutation harness was rerun, and no source, Git/index, cache, campaign state or formal audit record was changed.

The only note delta from the previously reviewed `2133ec1786855f768c261f243f77c1fcc114001c4b583d1115fdec4defb6dd30` to the final `952a82662a01ea1af31da281a45f14a1818c365d789f20784725a11013017b9f` is the thirteen-line test-history paragraph preserved in `FINAL_NOTE_DELTA_v3.diff`. I read that complete delta. It changes no equation or mathematical premise. Its claims agree with the saved records, with the distinctions below.

## Evidence actually checked

The read-only `closing_mutation_binding_v1.py` inspected and pinned 238 saved files. Its detailed receipt, `CLOSING_MUTATION_BINDING_v1.json`, lists every identity and every mutation outcome. I read the complete v3 harness and the two v2 completion/interruption records. The binding check parsed all three harnesses' mutation specifications, checked all 72 historical result rows, and compared all 70 materialized mutant sources with the exact single replacement on their own version's frozen baseline. The two nonmaterialized v1 cases are the disclosed selector failures. Recorded stdout summaries, named failed checks, exit codes, source hashes and stderr dispositions match the corresponding result rows. No row or survivor was dropped from this comparison.

| Run | Failed-check outcomes | Exceptions | Survivors | Selector failures | Evidentiary treatment |
| --- | ---: | ---: | ---: | ---: | --- |
| v1 | 18 | 2 | 2 | 2 | Preserved original result, including weaknesses |
| v2 | 21 | 3 | 0 | 0 | Entire run invalid because its unchanged baseline failed |
| v3 | 21 | 3 | 0 | 0 | Guarded clean-baseline run, within the stated mutation scope |

The v1 survivors are the `1+eta` and `abs(yhat)+eps` denominator substitutions. The ambiguous selectors each matched twice; the later selectors are unique. The sharp state and ratio witnesses independently checked in `SHARP_ENVELOPE_REVIEW_v1.md` remain 1/24 versus 1/26 and 1/16 versus 3/52. The production envelope functions were not changed by those added fixtures.

The v2 source contains the erroneous negative first ratio entry; the preserved unchanged domain baseline has 25 passing controls and one failing sharp-ratio control. Its correction record expressly supersedes the initial attempted-interruption description: the run had already completed and no process was killed. All v2 outcomes are excluded as rejection evidence. This history is consistent with the note and is not concealed by v3.

The v3 harness checks its unmutated primary before entering the mutation loop and refuses a failing baseline. The saved baseline has 85 passed, zero failed, matching saved stdout and summary, with empty stderr. All 24 v3 selectors match once, all 24 saved source replacements are exact, and every recorded outcome is accounted for. The three exceptions are two downstream potential-decoder `ValueError: math domain error` failures (`full_forward_force`, `numerical_inverse_ratio`) and one physical-monomial `ValueError` (`covariance_row_time_leg`). They are not assertion rejections or setup/import failures. The other 21 variants have named failed-check outcomes. Mutation coverage is finite and does not prove that arbitrary implementation errors would be caught.

## Final source and execution binding

The v3 mutation run used note `2133ec17...`; its primary and five scientific helper hashes equal the final reviewed code. The subsequent final source-bound execution uses note `952a8266...`, whose only added content is the history paragraph. The final primary is `cb233af6423d3dae7f35f2bc079df2b62c4720d599472326ff191026a645a8d0`; cache is `4cc15dc73aa8ab18e28e6117ab48eb34e97e1fd8bd48293245f8daa65bdce7c8`. `CANONICAL_SOURCE_FREEZE_v2.json`, current inputs, products and cache agree on 85 passed, zero failed, exit zero. The receipt records fresh status and 2.2028229236602783 seconds against a 180-second timeout; the cache header rounds elapsed time to 2.20 seconds. I verified these saved bindings rather than recomputing the runner's fingerprint algorithm or executing its science.

No unresolved discrepancy was found in this closing scope. Full equation and domain reasoning remains in the earlier reports; forward numerical independence remains a separate checker's responsibility. This supplement supplies neither new empirical validation nor formal audit or landing approval.
