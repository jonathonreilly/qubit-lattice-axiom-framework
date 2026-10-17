# Ordinary source generation and actual validation evidence

Before the bounded validation runs, the ordinary file-authoring command wrote create_sources.py and invoked:

    python3 -B /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/interacting_control_qualified_publication_draft/create_sources.py

The tool reported exit0 and the complete output:

    {"created": "source plan and four metadata programs", "sources": 27, "body_count": 9, "science_executions": 0}

That authoring script SHA256 is31f14a5a1994476bfe486217e16b72b3f40ae0af9423be4b038910d02fdabd8e. It is retained unchanged. This was source generation, not a validation receipt or science process. It did not have a separate prelaunch recorder/capture; no such evidence is reconstructed here. The tool's combined output was the short JSON above; no standalone authoring stdout/stderr files are claimed.

Actual bounded build and inspection validation processes are separately recorded under metadata_runs/build and metadata_runs/inspection, with source-at-launch, recorder-at-launch, input identities, exact child argv, full streams, launch/result receipts and60-second wall limits. Both exited0, with empty stderr and inputs unchanged during each run. They establish source integrity only. The final seal has its own source/launcher capture and validation receipt under metadata_runs/seal.

No new scientific process or historical replay ran. No metadata validation launch failed in this draft. The historical failed metadata attempt remains in the source archive and is not rewritten as a new failure. The primary's seven expected virtual refusal cases are successful metadata checks, not failed launches or scientific counterexamples.
