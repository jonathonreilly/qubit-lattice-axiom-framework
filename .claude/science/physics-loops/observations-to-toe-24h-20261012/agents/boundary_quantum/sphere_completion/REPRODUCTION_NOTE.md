# Post-freeze reproduction clarification

The independent review of the earlier finite composition packet found no
material mathematical error and identified a nonblocking reproduction issue:
its original `composition_check.py` writes results beside the script. A
direct rerun in the frozen source directory would change timestamped output
hashes even though the freeze JSON itself remained untouched. This clarifies
the earlier report's instruction; no V1 file has been edited or restamped.

The same original script and its two frozen inputs can be run unchanged in
a new directory. The new `reproduce.py` makes that procedure explicit with
`--packet composition --output-dir /absolute/new/runtime/directory`.
For the new full-sphere packet use `--packet sphere` instead. The output
directory must be new and outside both source packets. The wrapper copies
the exact code and inputs, runs it in the foreground, compares results after
removing execution timestamps, and records a receipt with byte hashes.

For example, during the active campaign:

```sh
python3 reproduce.py --packet sphere --output-dir /Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/boundary_quantum/sphere_completion/reproduction_v1
```

The original campaign deadline and stop guards remain active. The wrapper
does not modify or bypass those controls. Future reproductions should select
a new output directory rather than overwrite an earlier reproduction.

The original finite-packet V1 freeze SHA-256 remains
`35586385663854a0ab1b23ce9007512b3f50cc729310307b31a1f176b026f413`.
The independent mathematical review belongs to
`agents/boundary_quantum/independent_composition_review/`; it did not review
the subsequent full-sphere classification theorem.
