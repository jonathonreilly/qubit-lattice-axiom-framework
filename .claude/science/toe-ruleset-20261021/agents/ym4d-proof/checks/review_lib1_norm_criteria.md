# B1 affected-review numerical criteria

1. Exact integer/Fraction equality is required; no floating tolerance.
2. Independently saturate supports by set-based adjacent inactive-vertex
   growth. The corrected full-output routine must equal a direct sum at
   every allowed root followed by a maximum, with weight 2 per full support
   vertex, on every connected labelled graph of 1–4 vertices and every
   retained subset, using positive nonconstant rational input coefficients.
3. For every relabelling of a four-cycle and each coefficient q in
   {1/3,1,7/2}, the retained-singleton witness must give input 2q, full
   output 16q and active output 2q. For every relabelling of path 0-1-2,
   endpoint coefficients 1/3 and 2/5 must give full 44/15, active-root with
   full weight 8/5, and active 4/5; the full maximum is at the inactive root.
4. The unchanged corrected complete baseline must finish every original
   predicate and all seven added exact predicates. Runtime tracing must
   observe the same full-output function in all 2,184 inequality cases
   and both exact witnesses, with equality to the independent norm oracle.
5. The original source's active-for-full substitution must reproduce its
   successful exit and false rejection label. Corrected source substitutions
   in the shared routine must reject both-active and active-weight-only at
   exact_cycle_output_full_norm, and active-roots-only at
   exact_inactive_root_output_full_norm. Failure elsewhere is not detection.
6. Numeric execution requires niceness >=10, all five recorded thread
   settings equal to 1, RSS <2,000,000,000 bytes, every load average <20,
   macOS free memory >=50%, and each computation's elapsed time <=60 seconds.
   Resource refusal is neither successful validation nor a mathematical
   counterexample. Runs are sequential without worker pools.
