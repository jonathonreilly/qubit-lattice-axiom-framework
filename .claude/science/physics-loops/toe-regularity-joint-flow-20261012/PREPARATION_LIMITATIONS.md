# Mechanical preparation limits

Preparation reads and maps the complete notes, primary code and source reports.
It does not independently recertify their proofs or rerun their computations.
Current workflow/delivery/conformance and the prior centre/current packaging
pattern were inspected. The mechanical task explicitly forbids Git/ref actions;
no planning-branch fetch or publication action is performed by the preparer.
The executing root owns current planning/source freshness and final delivery.

The SOURCE_IDENTITIES manifest initially covers the prepared files only and
excludes itself. Root must regenerate or supplement it after adding fresh
verification evidence/caches or changing any prepared file. Exact publication
reconstruction must continue to pass; any later note/primary change needs an
explicit transformation and new hash. No source evidence is deleted.
