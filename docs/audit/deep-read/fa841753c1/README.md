# Docs-top external-reader log

Pin: `fa841753c1a6296e5ad45518375660b0f1004769`

Repo: `jonathonreilly/qubit-lattice-axiom-framework`

This directory is the external-reader record for the newest-first docs-top
read. It is the repair input. It is not an audit pass, not a ledger update,
and not a science landing.

## How to use a record

Note number `N` is line `N` of `docs_top_order.txt` (1-based). The Python
index is `N - 1`.

For a signed note, read both:

- `records/note_<N>.json`
- `records/WAVE_<letter>_INDEX.md`

The JSON `issues[0].detail` is the finding. `open` is what stayed unresolved.
`provenance_not_opened` says what the reader did not open and did not rerun.
`grade_clash` is true only when a bold Type line and the ledger `claim_type`
differ. A printed `PASS` or `FAIL` row is not an audit pass. Runners named in
`runner` were not executed.

A line that failed the card scan is recorded by line number and label, not by
its original text. A dirty dependency is counted and omitted. Do not
reconstruct those strings from memory.

## Coverage

The read started at note 1. The log lived only under `/tmp`. That directory
was wiped more than once. Notes 1–1550 have no card and no wave index in
this snapshot. They were not rebuilt from memory.

What survived on disk at the cut: wave indexes for notes 1551–1737, 169
files named `records/note_<N>.json` for 1552–1737, and 18 cards stored
under the claim id instead of `note_<N>.json`. The read lock was note 1738,
which has no card yet.

These note numbers have a wave index and no `note_<N>.json`:

1551, 1553, 1554, 1555, 1557, 1559, 1560, 1561, 1562, 1563, 1565, 1566,
1567, 1571, 1572, 1574, 1575, 1576.

From 1577 through 1737 the JSON card and the wave index are both present.
`coverage.json` lists the missing JSON numbers.

## Repair rule

One finding, one repair PR. Cite the note number and the pin. Do not treat
this log as permission to rewrite a note, rerun a campaign, or push `main`.
