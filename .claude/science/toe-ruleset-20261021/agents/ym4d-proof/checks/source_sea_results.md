# Author checks for the one-level sea estimate

Final run: [source_sea_run_02.json](source_sea_run_02.json), all six groups
PASS. Command: `python3 checks/source_sea_check.py` from the lane, with JSON
stdout saved. Runtime: Python3.12.8, NumPy2.4.1, mpmath1.3.0 on arm64 macOS.

| Diagnostic | Result and meaningful control |
|---|---|
| Actual 4D geometry | All1,296 cells on a6^4 torus have32 links and24 plaquettes; each of7,776 plaquettes has four cell witnesses. No reflection-plane crossing. Twelve endpoint-region reflection checks pass for (L,T)=(3,2),(3,4),(5,2). A single bad plaquette witnesses four bad cells, rejecting the multiplicity-one count. Cell-contained source support misses96 actually touched plaquettes. |
| Noncommuting SU(2) reflection | On5,184 random Haar links, total action changes by1.19e-11 or less under the correct reflection, and maximum cell-energy error is2.23e-16. Omitting the inversion of normal links changes the action by7.1077. |
| Exact finite gauge interpolation | All65,536 Z2 link configurations on a4x2 torus were enumerated, retaining the global even-plaquette constraint. All256 exact histories and256 holes satisfy the sharp reference-relative bound. Every nonempty product event is checked at four penalties. Removing the penalty or attempting a reference ratio from a single-defect probability law is detected. This is a2D Z2 diagnostic, not an SU(N) proof. |
| Correlated hard-source identity | All64 rational-complex refinements agree exactly between direct integration and joint replacement;16 are nonzero. Six controls fail: uniform coarse reference, missing kernel normalizer, missing source compensation, discarded failure returns, unchanged-sea insertion and discarded exterior source. The reference is9 in the fixture's explicit Haar convention. |
| Actual SU(2) kernel | Nine radial Haar integrals at t=20,80,400 and M=rI check the Bessel normalizer to better than1e-40. At t=400, the clean mean's mismatch tail is approximately1.92e-86. The rough mean M=-I has tail near1, while falsely applying the clean bound would give3.36e-12. No global contour realization of this diagnostic mean is inferred. |
| Sources and cutoff arithmetic | The explicit smaller fixed source radius leaves at least half each exponential rate. Under the separately proposed Wilson-u flow, the largest a_delta beta_1 for delta<=1 is0.02322 at N=2 and0.03483 at N=3; both miss the volume exponent4. The final theorem does not use the failed union-bound window. |

[Run01](source_sea_run_01.json) also passed. Run02 followed a checker
strengthening: the cell-incidence control now reports its explicit one-to-four
witness, and the K_c geometry now checks reflection covariance. Run01 is
preserved. No scientific failed run was overwritten. Two edit attempts were
rejected because a patch included unmatched context; they changed no files,
and the corrected patches then applied. Literature access failures are
separately recorded.

These tests substantiate conventions, exact finite identities and mutation
sensitivity. The proof of the arbitrary-volume and arbitrary-SU(N) result is
the penalty-family argument in the source note. Independent review is still
required. The final source domain is localized original coefficients on an
explicit fixed polydisc, with a real fully integrated coarse field. Neither
a fixed-V connected-source estimate nor a continuum theorem was tested or
proved by these computations.
