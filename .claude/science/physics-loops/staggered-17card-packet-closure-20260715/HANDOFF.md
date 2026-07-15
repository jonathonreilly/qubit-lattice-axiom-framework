# Handoff

The canonical runner is a checked-in, self-contained numerical implementation,
but the packet resolver previously missed it because the wrapper launches it
through `subprocess.run` rather than importing it. The source repair detects
that static command target in both resolver implementations and includes a
matching regression test.

The repository-wide lock helper is unavailable on this machine because its
default path targets `/Users/jonreilly`; work remained isolated in the clean
dedicated science-fix worktree.

The paired wrapper now also verifies that the supplied canonical source exposes
the load-bearing Hamiltonian, evolution, card, and fixed-size entrypoints. Its
source-hash drift returns the terminal conditional row to the ordinary audit
queue without authoring a verdict.

Verification completed: the wrapper reports `TOTAL: PASS=20 FAIL=0`; both
resolver implementations pass their regression tests; the full pipeline
renders the canonical source as the row's helper, invalidates the prior runner
hash, and places the row in the ready ordinary queue; strict lint reports no
errors. All generated audit/status outputs were stripped after validation.

Review-loop disposition: PASS WITH BOUNDED CLAIMS. No audit verdict was
authored or applied.

Next exact action: run the independent fresh-context audit on
`staggered_fermion_card_2026-04-11` after this source repair lands.

Delivery: commit `109e9883ac`; draft PR
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/5383.
