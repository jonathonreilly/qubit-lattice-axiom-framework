# Handoff

The block hardens the already-audited bounded finite-window logic with a
fail-closed runner certificate. It requires all four finite rows, finite
observables, Born residual `< 1e-10`, exact `k=0`, positive gravity on the two
finest successful rows, and an explicit raw-kernel `OverflowError` at the next
tested spacing `h = 0.125`.

The runner, independent property check, mutation checks, fresh SHA-pinned
cache, vocabulary lint, review loop, audit validation pipeline, strict audit
lint, and `git diff --check` pass. Pipeline-generated authority files were
stripped after validation.

The exact next action is to open the review PR. After landing, the independent
audit lane must decide the edited row's effective status and then recheck the
dependent `lattice_nn_distance_law_note`; this branch authors neither verdict.
