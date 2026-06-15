# Goal

Remove the source-side markdown dependency cycles currently surfaced by the audit queue, without changing any audit verdict, ledger row, or generated effective-status output.

The target is audit unblock, not claim promotion. The source notes keep the scientific statements and filenames, but non-load-bearing downstream/back-reference mentions stop being markdown links that the citation graph treats as dependencies.
