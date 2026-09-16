# Numerical history

Attempt1 of the calibrated-transfer program completed all assertions. Personal output review then found that the J=0.1 crossover gap, about1.3e-41, was reported as2.9e-10 by subtractive roundoff in log(lambda) with lambda near1. The absolute assertion tolerance did not detect this relative-resolution failure. The original source and raw stdout/stderr are preserved.

The corrected calculation evaluates the exact positive deficit1-lambda=2 E sin²(pi rK/N), then uses-log1p(-deficit)/delta. It does not loosen a tolerance or change the mathematical target. A follow-up relative crossover assertion is required so the same loss cannot pass unnoticed. Matrix semigroup products still use the positive Poisson eigenvalues; their comparison remains an absolute finite-dimensional diagnostic.
