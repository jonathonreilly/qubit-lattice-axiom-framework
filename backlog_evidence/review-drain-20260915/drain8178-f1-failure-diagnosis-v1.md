# PR8178 F1 failure diagnosis

**Verdict: narrow exact-comparison repair required. No retry authorized by this report.**

The actual baseline remains failed (15 PASS, 1 FAIL; F1 only). Its raw output, sidecar and failure receipt remain preserved. No production rerun, mutation run, source edit or staging was performed during diagnosis.

## Exact cause and mathematical result

Runner line 292 compares `U*P*U.H == D` using SymPy structural equality. Twelve entries retain unexpanded expressions despite being algebraically equal. For example, the (1,1) product entry is `1/3 - I/6 + I*(-1/12 - I/6) - I*(1/12 + I/6)`; expansion equals the expected `2/3 - I/3` exactly.

For the negative-character transform and shift sampling x-e_j, substitution y=x-e_j gives multiplier `(1+exp(-ik1)+exp(-ik2))/3`. The accepted proof is correct. An isolated control independently reconstructed the L=4 identity without importing the production runner. All 256 residual entries expand to exact zero. Separate Gaussian-rational arithmetic using pairs of Fractions independently verifies all 256 entries. The wrong positive-sign target produces ten nonzero entries, including residual (1,1)=-2I/3. This is an exact discriminating check, not a tolerance adjustment.

The one bounded control completed with exit 0 in 0.306 seconds, sampled peak RSS 80,379,904 bytes, within the predeclared 30-second/192-MiB process-tree limits. Full script, plan, raw output, stderr and receipt are retained under `check8178/f1-diagnosis*` and hash-bound in the JSON report. No scientific baseline was executed by the control.

## Narrow repair and follow-through

Replace only the F1 predicate with `(U*P*U.H-D).applyfunc(sp.expand) == sp.zeros(L*L)`. Keep D, U, P, the wrong-sign mutation, and strict exact arithmetic unchanged. The earlier review missed this symbolic-representation defect; the failed execution exposed it and must not be erased.

After author repair, rebind source hashes and staged tree, review the narrow diff in this same session, and refresh cold/adapter evidence. A separately authorized attempt needs new immutable output names and once-only identities under unchanged resource bounds. The actual 16-check baseline and all four pending new mutation controls still need successful execution, including rejection of the wrong Fourier sign. This report neither authorizes a rerun nor claims those pending results. Original control reuse remains limited to its previously accepted scope.

All source identities, raw failed-capture evidence, full independent control output and required reconfirmations appear in the companion JSON.
