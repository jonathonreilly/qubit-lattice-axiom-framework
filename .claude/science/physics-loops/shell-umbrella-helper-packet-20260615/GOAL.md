# Goal

Unblock the audit packet for
`one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13`.

The row exists to expose five helper modules used by
`scripts/frontier_one_parameter_reduced_shell_law.py`. That runner loads them
through `_frontier_loader.load_frontier(...)`, so ordinary AST import discovery
does not attach those helper sources to the audit packet. This loop adds a
parser-visible primary runner/cache link and an explicit helper-path entry in
the citation graph builder.
