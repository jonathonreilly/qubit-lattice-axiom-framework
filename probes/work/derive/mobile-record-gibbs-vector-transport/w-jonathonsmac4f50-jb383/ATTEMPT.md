# Local Gibbs record circulations and winding transport: independent check of #8567 and one 3D candidate

Task `J:derive:mobile-record-gibbs-vector-transport:a1` · worker `w-jonathonsmac4f50-jb383` · model `claude-opus-5-5`
· origin/main `e37967e326` · checker `check.py` (exact; about 1 s).

**Provenance.** The source is the Codex draft #8567, frozen head
`801affee6e5fb11519c5b31ec2532cf320b8ba22`. The note's SHA256 is `c2d6d019…` and the runner's is `3812fca5…`; both match
`SOURCE_MAP.json`. The author's separate-context checks were within the Codex family, so this Claude check is
cross-family. The author's checkers were not used; everything here was reconstructed.

## (1) Statement attempted

1. **(K) Part B.** Reproduce the finite-word KLS stationarity certificate and the positive current.
2. **(P) Part A.** Reproduce the Gibbs invariance of the plaquette circulation and the cancellation of the
   contractible-cycle content current.
3. **(C) One explicit 3D candidate.** Test it against the research target, a 3D local permanent-record process with both
   a correlated vector Gibbs state and nonzero Euler vector transport, and report its first failed condition.

## (2) Steps

1. **CHECKED K1.** The draft's table h(a,b,c) makes F(a,b,c,d) = h(a,b,c) − h(b,c,d) hold on all sixteen words, for
   symbolic z and κ. The sum telescopes around any ring, which proves stationarity for every N, as the draft says.
2. **CHECKED K2 (different method).** Exact master-equation residuals (π L)(η) = 0 hold at every configuration of every
   ring with N = 4…9, for z ∈ {2, 1/3, 5/2} and three fugacities. This is a direct generator computation that does not
   use the certificate.
3. **CHECKED K3–K4.**
   - The class-1 current is strictly positive: 1076/6621 per bond at N = 8, z = 2 in the grand law.
   - det T = e^μ(e^J − 1) ≠ 0, so the nearest-neighbour covariance is nonzero for J ≠ 0.
4. **PROVED + CHECKED P1.**
   - Along an R-orbit, π(η)·a·e^{H_S(η)} = a·e^{−H_out}·(counts), which is constant.
   - Each state has one R-predecessor and one R-successor, so inflow equals outflow.
   - Verified exactly at 150 random states of a 6-site system: a plaquette plus two exterior sites, 3 labels, random
     rational pair and site energies, and irreversible a± = 1 ± χ/3 with χ orbit-invariant.
5. **PROVED + CHECKED P2.**
   - A stationary R-orbit carries a constant flow F. The orbit's total displacement Σ[M(Rη) − M(η)] telescopes to 0
     because R^L = id on an orbit of length L.
   - Metropolis swaps cancel in pairs by detailed balance.
   - Verified exactly on a 3×3 torus with 4 class-1 records: irreversible circulations on all plaquettes (a₊ = 3/2,
     a₋ = 1/2) plus Metropolis swaps give a stationary unwrapped current of exactly (0, 0).
6. **CHECKED C1–C2, the 3D candidate.** KLS exchanges run along +x, with the 1D heat-bath rates depending on the
   x-neighbours, on a 3D torus. The Gibbs weight is z_x^{#x-bonds 11}·z_p^{#transverse bonds 11}·λ^N.
   - **J_p = 0 (z_p = 1).** Stationary at all 12870 configurations with 8 records on the 4×2×2 torus.
   - **J_p ≠ 0 (z_p = 3).** An exact nonzero residual appears at the explicit configuration of two x-layers, empty then
     full.
7. **PROVED C3.** At J_p = 0 the grand Gibbs weight factorises over the L_y·L_z x-chains. So transverse covariances
   vanish in the grand law, and the drive along +x breaks the exchange of axes.

   **First failed condition for the target:**
   - with the vector correlation extended to transverse directions (J_p ≠ 0), stationarity fails;
   - without it, correlations exist only along the drive axis and there is no cubic covariance.

   This candidate is excluded. No universal incompatibility is claimed.

## (3) Salvage and first unresolved step

- **Salvageable narrow lemmas (verified here, cross-family):**
  - Part A: local plaquette circulations with Gibbs-weighted rates preserve any bounded finite-range Gibbs law, and
    their homogeneous content current vanishes (contractible cycles).
  - Part B: 1D KLS with the exact word certificate, positive current and exponential covariance.
- **First unresolved step:** a 3D cubic-covariant local generator whose Gibbs family has transverse vector
  correlations and nonzero transport. Part A's mechanism gives zero current, and the stacked chains give no transverse
  correlation.
- A route: local rates built on winding cycles need non-local support. The alternative is a pointwise word certificate
  in 3D, of the kind in K1, for a cubic-covariant multi-class exchange. Its existence is open.

## ASSUMED

The supplied labels, energies, rates and interpretation of #8567. Nothing is derived from the axioms.
