# Priced dual Green diagnostic

The exact lift works but the scalar-Green/l1 estimate is uninformative:
coarse costs126464(E1),280249(T12) exceed compact trial energies. Preserve it.
Compute only a diagnostic for the exact9-channel K2 inverse quadratic cost,
on32³ and48³ Fourier grids with soft q=0 contribution omitted. Each result
is a quadrature approximation, never a certified infinite Green bound.
The compact input has support well within each grid but this does not remove
Green-kernel quadrature error. Negative results do not invalidate the dual
lemma or all residual lifts. Price<=20CPU seconds/60wall/200MB, one BLAS thread,
streamed residual-pair channels. Absolute deadline and STOP checked.

Initial32/64 run exceeded its200MB envelope at the final RSS assertion; exact resources were not emitted and no result file was written. Original code/contract and failure record are preserved. Re-price to32/48 to reduce FFT live storage; all output remains diagnostic only.
