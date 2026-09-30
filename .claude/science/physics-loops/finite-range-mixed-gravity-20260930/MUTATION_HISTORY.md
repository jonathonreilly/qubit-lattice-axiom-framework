# Actual fault-injection evidence

`mutations/` preserves the eight final scratch mutations, each detected at a
load-bearing assertion. `extra-mutations/` contains endpoint transformation,
central-stencil coefficient and Laurent constant controls requested by review.
`clock-mutations/` additionally exercises integral coefficients, Jacobi cyclic
sign, synchronous reduction, endpoint range, harmonic split, quotient point
and frame-metric invariance. Exact replacements, baseline/mutated hashes,
exit codes and full failure logs are retained, not rewritten as successful runs.
Apply each replacement once to a scratch copy of the two scripts and run the
primary with python3,120-second timeout and BLAS threads1. Production source
is never mutated by these controls. The check is failure under a corrupted
formula/input; no runner banners are substituted for actual assertions.

Historical `initial-nondetecting/` preserves the cochain sign mutation whose
second product was zero in the original fixture. The harness correctly halted.
The fixture was strengthened to J=E11+E44; both products now contribute and the
same mutation fails. An earlier expanded-versus-factored equality assertion
was fixed by comparing its expanded difference; original logs are preserved.
These initial failures are not claimed as successful evidence.

The original non-detecting cochain log ends in an extra blank line. It is
preserved losslessly as initial-nondetecting/cochain_commutator.log.gz to keep
the new source diff whitespace-clean without changing historical bytes.
Decompression SHA256: e6f75b92098423399339c8b3ef29cd4c1fca191d49870c4a3fb935537808ae0f.
The uncompressed original also remains in the runtime evidence directory.
