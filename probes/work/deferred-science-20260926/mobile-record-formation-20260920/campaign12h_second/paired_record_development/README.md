The first author run stopped on a symbolic comparison of an expanded
polynomial with an algebraically equal factored expression. The recorded
increment was (YZ+Y-Z-1, -XZ-X+Z+1, 0), with exact zero divergence; this equals
the written (1+Z)(Y-1,1-X,0). SymPy's structural matrix equality was replaced
by simplification of their difference. The original source and failure logs
are preserved here. No mathematical formula or failed scientific counterexample
was discarded. Subsequent source also adds full event rotation checks and
explicit exact absorbing-equation residual/positivity checks.
