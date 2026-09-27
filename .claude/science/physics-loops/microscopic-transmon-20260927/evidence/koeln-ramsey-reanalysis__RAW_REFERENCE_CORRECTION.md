# Readout-reference source correction

2026-09-27. This notice supersedes the earlier interpretation in CODE_REVIEW.md that all267 stored raw01 x0 samples are Ramsey free-evolution delays. Original review bytes and fit evidence remain unchanged.

The exact July29 074423 GateScan processed HDF5 identifies its final two samples, zero-based indices265 and266, as readout-reference populations0 and1 for every one of31gates, to floating-point rounding. The appropriate Ramsey-only array contains265 delay samples per gate, ending19.84µs, and16,430 I/Q residual coordinates. Preserve the two reference raw I/Q values separately; excluding them is based on source semantics, not fit residuals.

The earlier residual reconstruction, units, sign and sparse-Jacobian checks remain valid for the supplied267-sample array. They do not validate interpreting that entire array as Ramsey dynamics. Its fitted calibration preference and downstream transferred predictions must remain labeled historical mixed-observation results pending source-corrected fitting and separate review. No corrected result is supplied by this notice.

The related July29 161812 qutrit Ramsey12 acquisition contains three final readout references and147 genuine delay samples. Exact indices, axes, per-gate population deviations and raw/processed hashes for both acquisitions are recorded in ../koeln-microscopic-transfer/READOUT_REFERENCE_CERTIFICATE.json. Source reasoning is in ../koeln-microscopic-transfer/RAW12_SOURCE_REVIEW.md. Neither raw data nor the original reviews were modified; no fitting occurred.
