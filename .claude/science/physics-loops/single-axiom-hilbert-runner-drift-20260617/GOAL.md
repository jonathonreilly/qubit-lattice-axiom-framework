# Goal

Repair the high-load `single_axiom_hilbert_note` audit backlog item by aligning
the source note, runner, and cached output with the already-narrowed
definitional-compression scope.

The concrete audit blocker was source/runner drift: the runner output reported
`Locality gradient (near > far): False`, while the note and runner synthesis
still carried old distance-decay and "single axiom reduction" language.

This PR does not audit, land, retag, or update generated audit/status files.
