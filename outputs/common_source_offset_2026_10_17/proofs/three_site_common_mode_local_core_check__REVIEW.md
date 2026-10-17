# Distinct check: common-mode local/source and background bounds

Verdict: conditional support; no necessary correction found. The shifted scalar all-three-site estimate and the actual represented-source/background interfaces follow on the inherited physical domain with Theta<1. No traveling-output or complete performance conclusion follows from this review.

Reviewed target: `three_site_common_mode_local_core/PROPOSAL.md`, SHA-256 `e817e63d7b6e7d1ba7d87db2322b8b5b7dd88b028fdbdd59962d4c3898713dcf`. The complete target was read. I refreshed the complete perturbed local/core source and reused the recently checked common-mode scalar/actual interfaces and unchanged prepared-core premises at the exact identities below. All eleven listed source/check hashes were verified.

## Shifted scalar density and three-site vector

For the nominal source centered at 2j+Delta, the three displayed Jacobi polynomials are correct. The second application to the seed uses only the first two source bonds: its squared norm is a1^4+a1^2 a2^2=lambda^4, while the second moment is a1^2=lambda^2/3. The common offset is therefore absent from these centered moments. The port is reached only on the third application; no physical lead shift has been assumed.

The cubic measure has these same moments and gives each polynomial squared norm one, hence integral ||p||^2 rho_M=3. With q_M=(y+i lambda)^3, the determinant error implies

    ||q_Delta|^2/R^6-1| <= 2beta+beta^2,
    |q_Delta|^2/R^6 >= (1-beta)^2.

Combining these with 1-s<=delta^2/(4j^2) proves (1). This comparison remains valid at the physical thresholds; it does not require a pointwise small relative density error there.

The weighted estimate in (2) is justified by Cauchy–Schwarz, not by an unavailable sixth moment: integral ||p|| delta^2 rho_M is at most the product of sqrt(3) and sqrt(integral delta^4 rho_M). Since odd centered cubic moments vanish, that latter moment equals Delta^4+2Delta^2 lambda^2+lambda^4. Its square root is Delta^2+lambda^2. The cubic outside mass is bounded by V_Delta^2; Cauchy–Schwarz with the global polynomial squared norm gives vector-tail cost sqrt(3)V_Delta. This is a vector-amplitude tail rather than merely the scalar mass tail. The exact scalar measure has no uncharged atoms by the distinct common-mode premise. Thus the complete integrated vector error Evec_Delta follows.

The cubic characteristic function is exp(-s)(1+s+s^2/3) for s=lambda t>=0. Differentiating it for p1 and p2 yields squared component contributions exp(-2s)(s+s^2)^2/3 and exp(-2s)2s^4/9, respectively. These reconstruct (3). The common factor exp[-it(2j+Delta)] is retained in the vector; taking its norm does not imply a global equivalence of the actual Hamiltonian to a shifted nominal apparatus.

## Residual comparison at fixed Delta

The residual complex ratio compares sources at the same supplied Delta. Its density bound D_rho=2L+L^2 is valid on the physical band. The polynomial estimates B1 and B2 need only the nominal scalar centered second and fourth moments just established. The unchanged Jacobi normalization also gives integral ||p||^2 rho_Delta=3. Splitting p_e rho_e-p rho_Delta as in the proposal therefore gives Bpol+D_rho(sqrt(3)+Bpol), including all three components and all phases. It does not compare the Delta packet to the zero-offset packet.

The minimum one in (5) is justified by projection of normalized scalar unitary evolution onto its three source sites. It is a scalar reference assertion, not an actual installed escape estimate.

## Joint columns and ordered actual subtraction

The reference cofactor column (a1a2,-a2 A0,P_r)^T Qref^-1 is exact. With y replacing the unshifted scalar variable, the nominal joint numerator has squared norm R^4, and the residual numerator perturbation gives exactly C_eps R^2. This reuses a polynomial identity, not unchanged resonance locations.

The complementary joint-column bound needs an argument beyond P_r/qref<6. Here |z|>.1849 and lambda/|z|<6e-8; the leading |P_r| term is <1.000001|z|^2, the a2 A0 term is less than 1.7(6e-8)(1+.005*6e-8)|z|^2 and the a1a2 term is of order (6e-8)^2|z|^2. Their sum is <1.000002|z|^2. Division by .99|z|^3 gives a joint norm <6. Both signs and every complementary channel are included.

The resolvent identity (6) is in the valid order Rref E2, background difference, a1a2 Q^-1. No actual G crosses a reference source polynomial. The selected full inverse and the complementary-input bound from the actual interface preserve all output rows and wrong-window input columns. The scalar load remains m_j(D), not m_j(D-Delta).

## Original physical windows and Stone factors

The processor envelope is a0+b0|delta|. Since delta=y+Delta, a_bar=a0+b0|Delta| is required; it is present. The original physical window becomes [-d-Delta,d-Delta] in y, which is contained in [-Dmax,Dmax] with Dmax=d+|Delta|. No physical window has been moved.

For a selected input the subtraction majorant is proportional to

    (a_bar+b0|y|)[C_eps/(m^2 R^4)+6/(m R^3)].

Extending this positive majorant to the full line gives the four integrals pi/(2lambda^3), 1/lambda^2, 2/lambda^2 and 2/lambda. The Stone factor 1/(2pi) times two lips supplies 1/pi, matching Dsel. For a complementary input the factor is proportional to (a_bar+b0|y|)[C_eps/(mR)+6]. Integrating over the symmetric enclosing interval gives exactly the asinh, square-root, 12a_bar Dmax and 6b0 Dmax^2 terms in Dwrong. Extending a majorant does not assert actual analytic control outside the original windows.

The two selected input projections combine with at most sqrt(2)Dsel; paying 2Dwrong for the two wrong-window terms is conservative. Actual error images need not be orthogonal. Record-X/parity sector orthogonality introduces no extra multiplier, and passive reference tensoring preserves the operator bounds. Each lip retains its physical ordering; Q_lower need not be Q_upper's adjoint. Stone synthesis requires the inherited actual matching and local regularity hypotheses, which remain explicit through the actual-interface dependency.

Reference truncation uses the shifted sixth prefix moment but the distance d-|Delta| to the ORIGINAL window boundary. Its sqrt(2mu6)/(d-|Delta|)^3 allowance is valid and conservative for the two prepared old energies. The source sum (8) therefore compares the represented actual source with the full perturbed scalar source plus this distinct reference truncation. It has not added the actual global omitted state. A later complete synthesis must charge that actual state only once, not once per spatial range.

## Complete represented background and limits

Source compression remains exactly unchanged, so the previously checked full-fiber recovery L0=14000 applies to all non-source finite heads and closed tails. The forcing column -kappa L a1a2 Q^-1 retains its order and perturbed numerator. Each window contributes the two-lip factor (1/pi) integral R^-3<=2/(pi lambda^2); paying both windows gives the displayed 4/pi. Bounding a1a2 by (2sqrt(2)/3)(1+epsilon)lambda^2 yields (9), with c=(1-Theta)m. No missing common-offset term remains outside that shifted inverse margin. The propagating stationary ray is excluded and must be handled separately.

These are absolute represented-piece bounds, not a numerical decay rate for the actual full state or a chosen useful performance point. Actual outside spectrum, physical traveling phases and waveform choice, incoming concentration, output normalization and finite complete performance remain separate obligations. Nothing here transfers the zero-offset complete tolerance ceiling.

## Exposure and verification limits

Root authored this source. I authored the perturbed attachment ancestor, checked both common-mode sources and have shared traveling/reference/core ancestry. This review is distinct from the new author derivation but is not blind or an independent recertification of those antecedents. Their recorded distinct checks are reused within scope. The changed weighted scalar estimate, shifted-window integrals, joint complementary bound and aggregation were reconstructed here rather than accepted from status labels.

No dynamics, numerical integration, parameter sweep, scientific runner, solver, Git/publication/checkpoint action, prompt/model modification or delegation occurred. Only this review was written; deterministic hashing was used. No retained-status or physical implementation certification is claimed.

## Exact source identities

- `three_site_common_mode_source/PROPOSAL.md`: `5076c3e9eb2683cdb8c9ad99bb002bc52ff242fdb9a6419d20e6acc22520b7fb`.
- `three_site_common_mode_source_check/REVIEW.md`: `af2e768b78e337f1f11d982ea83fdb1d6270f6b646ccb0895b79fd6613d44ffb`.
- `three_site_common_mode_actual_interface/PROPOSAL.md`: `9225b6ea6533dea56db4f8b7157deac5c6f52e5927b554052c59299622a13957`.
- `three_site_common_mode_actual_interface_check/REVIEW.md`: `e9b32196906e1d4b5010ac9b30d348e438d6e88fcdac82d51ae107f3f7ba1cea`.
- `three_site_perturbed_local_reference/PROPOSAL.md`: `b36ef9001996fd031bfabd8541776be27831050cac6b67fee1016cf10f04b504`.
- `three_site_perturbed_local_reference_check/REVIEW.md`: `3db966162b1c49a28041a8c0a04eaa9c5bebb7613718894d43227b3e65cd18c7`.
- `three_site_perturbed_local_core/PROPOSAL.md`: `7c5fcdae5cb9682e6d4f1babe1390ddbb58446416df0f4309fb056f14c1688a7`.
- `three_site_perturbed_local_core_check/REVIEW.md`: `e23d90ee489dcded97cb2397e95e378b7cba3c58747110a0ac1849036a7bc990`.
- `prepared_core_recovery/PROPOSAL.md`: `cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9`.
- `prepared_core_dwell_check/REVIEW.md`: `88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819`.
- `prepared_core_composition_check/REVIEW.md`: `52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c`.
