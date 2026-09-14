# Corrections and checks

The first direct full-Fock implementation initialized H_m with a real dtype,
discarding its imaginary matrix elements. The exact Gauss commutator check
failed before a trace result was accepted. Original source/stdout/stderr are
preserved as attempt1 gzip files. The complex dtype repair preserves the
intended Hamiltonian; all N=3,4,5 and M=1,2,3,4 trace comparisons then ran.
The independent phase-history sums and full Fock operator traces agree to
1.1e-13 or better. Single-species and wrong-temporal-conjugation complex
weights remain explicitly recorded. Trotter errors are nonzero and decrease;
no finite-slice result was called the exact Gibbs trace.

The displayed history boundary sign and temporal matrix order survived the
full-Fock check. This is an author check using distinct constructions, not an
independent review or an audit verdict.
