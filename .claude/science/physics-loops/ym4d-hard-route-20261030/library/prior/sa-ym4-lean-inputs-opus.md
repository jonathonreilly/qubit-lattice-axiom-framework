lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-24T09:52Z

# Row 1449: does the kernel-checked Wilson continuum construction supply the gap chain's continuum inputs?

Started 2026-11-23T21:52Z (date -u), Mac mini worker 2, at commit 9f6c0bca2. Port reading, not a proof lane. No claim about the Lean release beyond its authors' recorded checks.

Credit: the source is Ethan Sussman and Levent Alpoge's public `YM4 Lean` release (written with OpenAI Codex assistance; reduced from the OpenAI Lean archives read in row 692), commit 3932084a9b82 of 2026-11-20. Quotes below are short and attributed.

## Plan

1. Locate the source. The row names a read-only checkout on an external volume. This session's scope rule allows reading only the repository, ~/ym4d-papers and own /tmp scratch, so the source is fetched by public URL into a /tmp scratch folder, pinned at 3932084a9b82.
2. Q1: read Challenge.lean, README.md, doc/Theorem.tex, doc/verification.md, Formulation/*.lean. State exactly what `YangMills.wilson_subsequence` and `YangMills.su2_fixed_observable_continuum_limit` assert.
3. Q2: read the gap chain's inputs (P1)-(P4), class C, (H2), (TOT) in library/gap-seed-audit-fable.md L104-130, gap-os-equiv.md Statement (5), gap-mini-branch-fable.md 5.3, rows 1342, 1349, 1356, 1359. Table: supplied / components only / not supplied, with the Lean declaration.
4. Q3: compare the Lean coupling sequence with the (M-neutral) trajectory of row 1367.
5. Q4: map onto library/t0-tree.md.
6. Next two rows with decisive outcomes; RESULT line.

## Repo search

(pending)

## Step 0. Source

Fetched by public URL into /tmp/ym4lean-w2-1449 (raw.githubusercontent.com, repository ethanwsussman/Yang--Mills-LLM-experiment, folder `YM4 Lean`, commit 3932084a9b82fc79466b4a2faad9ec032b637445, authored 2026-11-21T01:22Z, message "Update README.md"). The folder holds 12,651 files (135 MB). The external-volume checkout named in the row was not opened (scope rule of this session). Nothing was built or run. Read: Challenge.lean (264 lines), README.md, doc/Theorem.tex, doc/verification.md, then the Formulation files named below.

Their verification record (doc/verification.md, quoted in short): source fingerprint `3dcd0129...`; "Lean reported exactly `Classical.choice`, `Quot.sound`, `propext` for each theorem"; Con Leche accepted 333,678 grouped declarations; Nanoda accepted 342,294 expanded declarations; native and stock Comparator matched the public theorem; "The Windows Lake invocation exited with status 2" for the sandboxed stock rebuild. We have not replayed any of this.

Repo search: `grep -rn 3932084a` and `wilson_subsequence` over this target folder find only row 1449 and this file. Row 692 (`library/prior/oai-release-2026-11-11.md`) read the OpenAI release `YangMills.jointExistence`, which is a different theorem (beta/log(1/a) slope family, OPE, unique-vacuum Wightman for one phase). Their README says this construction "was carried out independently of OAI's".
