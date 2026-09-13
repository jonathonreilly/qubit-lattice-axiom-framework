# Original mutation diagnostic failure

The first primary passed31 checks. Eleven altered sources failed assertions;
the altered comb spine instead raised KeyError when the Record-only decoder
indexed a missing terminal register. The packaging gate rejected that result
because it required a discriminating assertion, not an incidental lookup error.

The exact first primary and all first mutation sources/stdout/stderr/RESULTS
are preserved here. Paths in that original RESULTS.json name their original
locations; resolve its mutations/ prefix within this first_mutation_attempt/
directory for recovery. The final primary explicitly asserts the fixed
terminal site is present before reading it; all mutants are then rerun from
that new source. No mathematical probability or geometry tolerance changed.

The cache-writing helper also compared its result status with the wrong enum: it expected pass but runner_cache returns ok. The runner exited0, passed31 checks and wrote a fresh cache before that wrapper assertion. The exact wrapper is preserved here; cache freshness was checked directly afterward. No rerun or cache editing was needed.
