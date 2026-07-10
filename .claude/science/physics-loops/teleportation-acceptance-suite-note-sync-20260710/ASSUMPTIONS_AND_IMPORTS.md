# Assumptions And Imports

No physical theorem, observed value, fitted selector, normalization, or
literature input is used. The claim is only about repository harness behavior.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Default `--list-probes` rows | Defines the documented default required and optional surface | computed lattice input | live acceptance-suite runner | yes | yes | exact table comparison in sync guard | retired by exact equality check |
| Strict `--strict-lane --list-probes` rows | Defines the documented strict-lane surface | computed lattice input | live acceptance-suite runner | yes | yes | exact table comparison in sync guard | retired by exact equality check |
| Profile composition | Establishes strict-lane as the default-required prefix plus present-gated additions, excluding default optional hooks | computed lattice input | runner selection functions and live list surfaces | yes | yes | executable count/prefix/category/disjointness checks | retired by guard |
| Meaning of PASS | Means zero child exit code with no parsed acceptance gate reporting FAIL; gate lines may be absent | computed lattice input | runner exit/report policy and source note | yes | yes | preserve explicit claim boundary and exit policy | closed for the meta scope |

Open imports: none.

## Counterfactual Pass

| Current choice | If wrong or changed | Route opened | Guard |
|---|---|---|---|
| The live runner is the source of profile identity | A prose snapshot is treated as authority | runner and note can drift again | exact live-output/table equality |
| Default ordering is eight required then four optional rows | Counts or order change | the note's numeric profile algebra becomes stale | explicit 8/4 partition check |
| Strict ordering is the default-required prefix then sixteen present-gated rows | Strict hooks move, disappear, or become optional | strict semantics no longer match the note | prefix, disjointness, category, and count checks |
| Cache freshness follows the guard source SHA | The note or documented runner changes alone | a cache-first consumer can see stale stdout | stdout fingerprints both mutable inputs; live rerun remains authoritative |
| PASS requires zero return and no parsed FAIL; a parsed gate set is not required | Readers infer every child exposes gate evidence | a gate-free zero-return PASS is overread | note states the return-code boundary explicitly |

Geometry, boundary conditions, normalizations, observables, representation
truncations, and sector choices are not inputs to this meta claim.
