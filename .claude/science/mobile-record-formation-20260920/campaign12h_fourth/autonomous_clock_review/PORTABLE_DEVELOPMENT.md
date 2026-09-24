# Portable wrapper correction

The first portable run passed the first three controls and executed the fourth
scientific control successfully. Its result comparison then failed solely at
the top-level wall_seconds metadata:0.4012354169972241 versus the frozen
0.35009949980303645. A complete recursive difference identified no other change.
The exact initial wrapper is preserved alongside this note; all logs and the
copy remain at /var/folders/4x/st_z21996n39j7bxfgns7gtw0000gn/T/autonomous-clock-portable-jbikz5ef.
The corrected wrapper compares every other field exactly and validates the
new nonnegative runtime separately. No mathematical source, result, tolerance
or scientific assertion was changed. The original scientific run exited0;
the initial publication wrapper exited1 at its overly strict metadata check.
