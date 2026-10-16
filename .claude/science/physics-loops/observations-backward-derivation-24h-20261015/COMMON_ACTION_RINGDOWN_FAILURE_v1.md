# Preserved first-run failure

The v1 run completed61 passing controls and one failing representation check.
`visible_load_polynomial_absent` inspected SymPy free_symbols before simplifying
the substituted residue; terms with zero coefficients still retained P symbols.
The preceding two exact simplified residue identities already passed.
The v2 runner simplifies the exact expression before inspecting free_symbols.
No physical statement, candidate, tolerance, synthetic input or reserved result
was changed. The full v1 source/stdout/stderr/control file remains preserved.
The six synthetic trajectories are exposed development of the implementation;
reserved_synthetic denotes their predeclared role in the frozen extractor, not
a fresh empirical or statistically independent validation after this rerun.
