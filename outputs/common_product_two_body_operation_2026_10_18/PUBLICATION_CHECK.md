# Bounded publication drift check: unpenalized two-body operation

2026-10-18. **No required correction identified in the integrated note at the exact hash below.** Its changes from the preserved exponent-21 author draft match the checked penalty-removal source and its distinct review. This is a source-to-manuscript drift check, not a new proof audit, retained-status verdict or publication authorization.

## Exact scope and exposure

All paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

| Input | Bytes | SHA-256 |
| --- | ---: | --- |
| `common_product_two_body_operation_publication/NOTE.md` | 21905 | `299339801b7f6714df652ab874a1a65ad504ceaf8ba934c08249dde458986899` |
| `common_product_two_body_operation_publication/AUTHOR_NOTE_21.md` | 20029 | `7db80cf49a53d6958278d9a15134f424cc05a60b630427ea6b756138a50ee749` |
| `common_product_two_body_operation_publication/AUTHOR_EXPOSURE.json` | 18597 | `aca31b764a17a54918e06bc67e96034168abda41d03bb02a658f75e7e485511d` |
| `common_product_two_body_runtime_penalty_removal/PROPOSAL.md` | 15779 | `b74d8f05658f6718dfcb4d9a050c6ddca90a357eabeb9dfed9c042567b36d9bb` |
| `common_product_two_body_runtime_penalty_removal_check/REVIEW.md` | 11085 | `64174ac689b6894ebfdf69369bdeb6816501ce15388cce6db5dd232d651b4337` |

The complete new 146-line source and complete 68-line review were read without truncation. The complete unified diff between the two 233-line manuscript versions was read. Unchanged manuscript content reuses its preceding complete authoring/readback coverage. The preserved author note and exposure record match their delivered bytes exactly; the exposure record was identity-checked, not represented as a new evidence-producing run.

I authored the earlier manuscript and previously read the component arguments/checks. ROOT supplied the new source/review and integrated the changes. This is therefore source-exposed same-model checking by the earlier drafter, not blind replication or independent proof lineage. The new review explicitly supports the unpenalized real-gauge combination; its support is not inferred merely from the author's pending-status prose.

Necessary unchanged interfaces retain their prior complete reads. Their exact byte identities were refreshed in this pass:

- Quadratic-background source: `388ebae502c0687fbbf267294d36ad7c32ddfa3dc32c1cd5d8ffbf7cb7af15fa`; distinct review: `39e5671ca6c4799ed011819a950af6743cb10eceb76c0e0465336bd8a1ba7f1e`.
- Real-gauge source: `1cc8b14dabd52a73f90bedf0186d7c3c92d02a9608aa72ce01ff0303fa3fe1f3`; distinct review: `603671b279be1867d9aabca527ac0142bee3e9d915eccf4ed050a2d9ae29db4a`.

The earlier finite-router, entrance, boundary, joint gadget and inventory interfaces are reused at the scope recorded in `AUTHOR_EXPOSURE.json`. They were not recursively re-audited. No newer continuation is included.

## Checked integration points

1. **Actual operator and reference:** NOTE line 90 removes the optional uniform head penalty from both installed and reference Hamiltonians. The definition is static, with no timed quench. The new ancillary Ising penalties remain in `H0`, and the single record bias remains in the background. “Unpenalized” refers to the removed uniform original-head term, not deletion of the gadget penalties or record bias.

2. **Full-space background bound:** NOTE lines 122–129 retain all 161 fixed core/writer/cable/bias blocks and every scalar vacancy. The radial table has `4ell-2` norm-`2jbar` bonds, two norm-`3jbar` combined sources, two norm-`jbar` caps, two norm-`jbar` residual bonds and four norm-`jbar/2` residual on-sites. Its sum is `8jbar(ell+1)`. The displayed `Bmax=161Lambda+8jbar(ell+1)` is the checked full-occupation ceiling. The source's double-occupation eigenvalue `3jbar` sets the source-block norm; no one-head bandwidth or scalar subtraction replaces this estimate. The old `Lambda(293+8ell)` appears only as historical comparison.

3. **Six-entry prescription and exponent:** NOTE lines 143–165 use the new `Bmax` in both its mixed-error square-root entry and background-smallness fourth-root entry. The other four entries, `K=48`, `Cmix=16384K^2`, `lambda=10Delta alpha^4/jbar`, and `T=U/(10Delta alpha^4)` match the checked interface. The prescription enforces `beta<=Delta/32`, `lambda<=1`, and the three `epsilon_g/3` allocations. The stated orders `Bmax=Theta(Lambda epsilon^-1 log)`, `alpha=Theta(epsilon^(7/2)/log)`, `lambda=Theta(epsilon^12/log^4)`, and `T=Theta(Lambda^-1 epsilon^-17 log^5)` match the new source. They remain orders of a sufficient selected family, not necessary or practical costs.

4. **Scalar and phase:** NOTE line 181 has exactly `exp{-it[48nu+s_joint+lambda*cbar]}`. The absent `lambda*mubar` phase is explicitly identified as absent from both runtime Hamiltonians. The mixed fourth-order scalar remains `-24nu^2/Delta+27nu^4/Delta^3`, not twelve isolated scalars. Higher mixed scalar corrections remain charged to the simulation error. The inelastic `q`, `-i`, incoming `(ell+57)k`, reference time `lambda*t`, positive finite normalization and single record bias are preserved.

5. **Real gauge and supplied state:** The unchanged sign table at NOTE line 71 is `+,-,+,-,+,-` for each entrance: six plus and six minus four-qubit cats on 48 qubits. The exact ancilla-only unitary commutes with the new ancilla-free background; deleting a real diagonal original-head penalty preserves background reality. The new distinct review expressly checks this composition. `J_real=UJ` has no additional phase with the stated `S=diag(1,i)` convention. This is not a physical cat-preparation procedure or a free conversion of a different supplied state. Joint preparation, input/rest independence, physical dual-rail input and passive references are unchanged.

6. **Outputs, probability and information:** The complete comparator retains logical program on P, old P/environment information relocated intact to Q/E, original-head vacancy, record1 and the signed cats. The same unnormalized branch target is used throughout the horizon. Final channel, absolute branch and joint-success bounds are unchanged, including `11epsilon/16`, `3epsilon/4`, and `1-49epsilon^2/1024-epsilon/8` at the stated allocation. No rare-branch normalization, discarded output or permanent halt is introduced.

7. **Counts and loads:** NOTE line 223 gives the actual `175+4ell` qubits and `265+4ell` blocks, comprising `169+4ell` background blocks plus 96 gadget blocks. The `124+4ell` uniform head-penalty blocks are explicitly absent. The qubits, range-35 placement, added loads `12nu` and `24nu`, ancillary load `2Delta+2nu`, and single record-bias accounting are unchanged. Deleting the positive on-site terms only improves the original incident-load margins.

8. **History and physical limits:** The exponent-21 and exponent-27 prescriptions are clearly attributed to earlier penalized devices. They are not substituted for the present operator or phase. The note preserves exact coefficient and interaction supply, signed-cat and boundary preparation, all output/reference conditions, finite-window limits and prior-art attribution. It explicitly rejects transfer of the old head-gap, energy-to-blank or Gibbs preparation certificates. No stronger preparation premise is introduced to obtain exponent 17, and no native realization or practical-cost claim appears.

## Verification and disposition limits

Commands actually run were Python 3 read-only file/line/hash bookkeeping, complete file reads, and `diff -u AUTHOR_NOTE_21.md NOTE.md`. The diff returned exit 1 because differences exist; that is the expected comparison result, not a failed scientific test. All nine specified byte-pin checks passed. No scientific executable, checker replay, numerical experiment, Git action, canonical installation or publication action was performed.

Only `PUBLICATION_CHECK.md` was authored for this task. NOTE, SOURCES, archived author files and ROOT's integration files were not edited. The disposition binds only to the exact note hash above; any later scientific change needs its affected drift check refreshed. Repository installation, packaging/runner checks, actual publication evidence and independent retained audit remain ROOT's separate responsibilities. No manuscript correction is requested by this bounded check.
