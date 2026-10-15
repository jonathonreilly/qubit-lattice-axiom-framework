# Actual execution failures

The initial parallel source-read call successfully printed the complete
`BLOCK01_READOUT_INTAKE_v1.md`, but its appended `shasum` argument mistakenly
included `New Axioms Lets Go/` inside the pack-relative path without quoting.
The shell consequently split that mistaken path. `shasum` reported `No such
file or directory` for the fragments and the command exited with status 1.

The next command used the correct pack-relative path. It returned the expected
SHA-256 `6d8dc4094320a13731ee1366cf5343076f82b7c106fded48496807fd6d933e33`
and confirmed the previously checked block-01 v5 hash
`5c2eb165f317192fbc6c8f3c548e442ce40d60d55915c363e57a4311d4d0f586`.
No source bytes were changed, and this was a path/hash-command failure, not a
mathematical check failure. All computational runs are recorded separately.

After the second successful run, I found a domain precision issue in my own
explicit bump implementation: `phi(t)/Z` has closed support `[-1/2,1/2]`,
whereas the source asks for compact support strictly inside the open interval
`(-1/2,1/2)`. Its area and divergence calculations were valid, but it did not
meet that literal support placement. The final checker uses
`psi(t)=2*phi(2t)/Z`, with support `[-1/4,1/4]`, and was rerun. The baseline
construction is unchanged. Both earlier checker versions, outputs, and
evidence files were preserved; no failing numerical result was hidden.

The first attempt to launch that final run repeated the mistaken extra
`New Axioms Lets Go/` path segment. Python exited with status 2 before running
the checker. Its actual error output is preserved in
`run03_failed_command.txt`. The next command used the correct pack-relative
path and launched the final computation. This was a command-path error, not
a failed mathematical check.
