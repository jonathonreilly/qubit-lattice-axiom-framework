# Central Bragg crossing: author check

**Date:** 2026-09-24
**Status:** author-run derivation and diagnostics; no independent review claimed.

The central resonance is not the generic simple-root case. For
\(\lambda_m=2(1-\cos(m\pi/5))\), the principal phase satisfies
\(5k(u,\lambda_m)-m\pi=O(u^2)\). The first-order site matrices vanish at
\(u=0\), since every \(\alpha_a(u)=u^2-u(2a+1)\) vanishes there; the
principal frame also has \(R_0'(0)=0\). Thus the moving-frame perturbation
obeys \(A_1(u)=O(u)\), while the eigenvalue gap is \(\asymp u^2\).

For inner width \(\rho=S^{-1/2}\), the direct product error is bounded by
\(\rho^3 S+\rho^2+\rho/S=O(S^{-1/2})\). Outside the layer, the homological
correction scales as \(A_{1,12}/\sin(5k)=O(1/u)\); its derivative is
\(O(1/u^2)\). The accumulated normal-form error and endpoint correction
are therefore \(O(1/(S\rho))=O(S^{-1/2})\). This balance supplies the
analytic estimate; the finite samples are only corroboration.

The paired runner returns exact zero for the central moving-frame matrix and
for all four quadratic-contact coefficient residuals. It rejects a fixed
off-diagonal mutation. Across all four energies and eight sizes, the exact
principal-frame product errors range from about \(4.1\times10^{-5}\) to
\(3.1\times10^{-2}\); the largest tested \(\sqrt S\)-scaled error is below
0.68. Local determinants and moving-frame SU(1,1) identities agree within
\(2.6\times10^{-15}\). No local cell was hyperbolic in this sample; the
theorem does not require a particular finite-spin ellipticity pattern.

The initial standalone route probe failed to import its paired transfer
module because its repository-root path selected `outputs/` rather than the
repository. Correcting the path to the repository root fixed the probe; no
calculation ran in the failed attempt. The corrected full probe and output are
preserved as `central_bragg_route_probe.py/.json/.stdout`.

The central estimate is at four fixed energies only. It is not uniform in
energy and does not control ordinary turning points, endpoint layers,
eigenfunction overlaps, or the actual two-index readout.
