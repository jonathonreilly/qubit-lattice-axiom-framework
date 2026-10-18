I read all the required files and then tried both routes from the overlap tradition. My answer to the question is **no**. On Z³, overlaps of profiles moved by O(1) displacements fixed by symmetry or sector structure cannot produce the mass ratios. Every version I tested either repeats a result already on main, gets the CKM ordering backwards, or needs positions put in by hand.

Disclosure: I am the same model family as the other route agents and the referee, so none of this is independent.

**What I read before concluding.**
- Required: `MINIMAL_AXIOMS_2026-06-29.md` in full, `PRIMITIVE_REGISTRY_CHECK.md` and `SCALE_REFERENCE_PRIMITIVE_NOTE.md`. `derivation_obligations.json` has three entries, about the charged-lepton readout and theta; none is on the hierarchy.
- Also: WALL.md, `hierwall/K/REPORT.md`, and the HIER-2 REPORT on its branch.
- On main: the Wilson Hamming-weight staircase note, `YT_GENERATION_HIERARCHY_PRIMITIVE_ANALYSIS` §0 (the circulant), the GST rank-1 note, `CKM_FROM_MASS_HIERARCHY`, `HIERARCHY_VALUE_FRONTIER_PROBE`, and the Bougerol–Lacroix Lyapunov no-go.

**Prior art.** A grep of main's docs finds nothing on split fermions, Arkani-Hamed–Schmaltz, Wyckoff positions, Wannier centres or random-product flavour. Several of my results land on things main already has; I mark those as mapped.

## Plain answer

- **Overlaps only move the problem.** An overlap turns a displacement into an exponent. The base of that exponent (displacement divided by profile width) is always a supplied number. At most, symmetry fixes ratios of exponents.
- **Symmetry-fixed positions on Z³ fail.** They are the half-cube points. They reproduce main's Hamming-weight staircase, leave two generations exactly degenerate, and give every sector the same spectrum.
- **Clustering fixes the pattern but inverts the CKM.** If the three generations sit close together inside one wide profile, the masses come out as 1 : ε : ε², three orders from one ratio. HIER-2's single spurion could not do that. But the same structure forces |V_cb| ≥ √2·|V_us|, against an observed ratio of 0.18.
- **The other tools are no better.** Exponential tails, the kind a lattice actually produces, are worse. The random-chain (Anderson) version gives a broad distribution rather than numbers, and it also inverts the CKM.

## Route 1: profiles placed by symmetry

**Object.** Profile centres at the fixed points of Z³ under translations and proper cubic rotations. Positions are linear in conserved charges. The overlap kernel is any real function.

- **L1a (proved; checked).** There are exactly 8 isolated fixed points, the half-integer cube points. Only (0,0,0) and (½,½,½) are singlets; the other six come in triplets related by the threefold rotation. Squared separations equal (Hamming weight)/4, so Gaussian and exponential overlaps both give exponents proportional to Hamming weight. That is main's Wilson staircase, and it allows at most two non-degenerate singlet levels.
- **L1b (proved; checked).** Any real overlap between two threefold orbits that respects the rotation is a real circulant matrix. Its two non-trivial eigenvalues are complex conjugates, so two singular values are exactly equal for every choice of positions and kernel (2,000 random kernels, gap ≤ 5e-15).
  - Splitting them needs either a time-reversal-odd phase (a flux through the triangle) or breaking of the threefold symmetry.
  - The phase is main's Koide/Brannen circulant (the δ = 2/9 lane); the symmetry breaking is GEN-2's E_g order.
  - This extends GEN-2's a·1 + b·J result to any real kernel under the proper rotations alone.
- **L1c (proved; checked).** Take positions linear in the U(1) charges, plus a generation step shared by all fields, with a flat Higgs. Yukawa invariance then forces the same left–right offsets in every sector (x_L − x_R = ±λ·Q_H + μ(g_i − g_j)). An even kernel gives M_d = M_uᵀ and M_e = M_d, so the spectra are identical (spread 4e-15). This is the overlap form of HIER-2's sector blindness.
  - Placing the Higgs at a hypercharge-linear point breaks the blindness. But it orders the third generation b > t > τ (pair sums, in λ² units: down 1.06, up 2.06, lepton 3.5), which is wrong.

**Number it would fix.** The width-free exponent ratios R_s = ln(m₁/m₃)/ln(m₂/m₃) and the pattern across sectors, from group and charge data alone. What it actually delivers is wrong: a degenerate pair and sector-blind spectra.

**Strongest objection.** Profiles need not sit at fixed points. A centre at (x,x,x) is allowed, but then x is a supplied number. Positions that depend on non-abelian Casimirs escape L1c, but only by supplying weights.

**Kill condition: met.** The route's only escapes are the phase or the symmetry-breaking direction, and both are already mapped.

**Test.** Done (`l1.out`, seconds).

## Route 2: clustered overlaps

**Object.** M_ij = K(x_i, y_j), with K smooth on a width σ and the three generations within δ ≪ σ of each other along a line. Up and down quarks share the doublet cluster, which SU(2)_L forces.

- **L2a (proved by Taylor/Vandermonde expansion; checked, fitted slopes 0, 2.000, 4.000).** Collinear clusters give singular values ∝ δ⁰, δ², δ⁴, so R = 2 at leading order. A triangle cluster gives δ⁰, δ², δ², i.e. orders {0, 1, 1}.
- **L2b (coefficient argument; checked to 0.2%).** For every Gaussian overlap (any widths, offsets or Gaussian Higgs), κ = m₂²/(m₁m₃) = 2·G(ξ)·G(η). Here G = |ξ⊥|³/|Vandermonde|, with minimum √2 at equal spacing (checked on a grid), so κ ≥ 4.
  - Observed κ is 1.76 (up), 0.36 (down) and 12.4 (leptons), much the same at M_Z and 2e16 GeV.
  - With the ×3 tolerance on each mass this still passes, because κ then has ×81 of slack.
- **L2c (checked numerically; the leading-order argument through the doublet cluster's Jacobi matrix is suggested, not proved).** For Gaussians, |V_cb|/|V_us| = G(ξ_Q) ≥ √2, whatever the up and down shapes, offsets and widths. 300 random configurations agree to within 8%.
  - Observed: 0.18.
  - For kink (sech^p) zero modes the identity fails, but the median ratio is 1.0–1.4, and only 0.4% of 250 configurations reach ≤ 0.3.
  - |V_ub|/(|V_us||V_cb|) comes out 0.35–1.2, against 0.40 observed.

**Numbers it fixes from structure.** R = 2, κ_s, |V_cb|/|V_us| and |V_ub|/(|V_us||V_cb|). Still supplied: one width ratio per sector and the overall scale.

**Strongest objection: there is no coordinate to host the cluster.**
- A Gaussian profile needs a Wilson mass that varies linearly along a lattice direction. That is a wall, and walls leave 2+1D physics (K report).
- The internal taste cube has only two points per axis, so it cannot hold a wide profile.

**Kill condition: met.** The Gaussian class inverts the CKM ordering (0.18 observed against a bound of at least 1.41). Kinks need about 1% tuning. The route is dead as a source of the CKM hierarchy. On the mass side only a weak R ≈ 2 pattern remains.

**Test.** Done (`l2`, `l3`, `l5`, `l5b`, seconds each).

## Side checks on the other toolkit items

- **Exponential tails** (sharp walls, lattice Green functions) are separable. If the left and right clusters are separated, the overlap matrix has rank 1 for a single profile or rank 2 for two zero modes. One or two generations are then exactly massless (proved; checked to 1e-17). Interlaced clusters give orders {0, 1, 1} (checked).
- **Anderson-like localisation, as a random chain of 3×3 steps** (checked):
  - The exponent ratio depends on the ensemble: R = 2.96 for complex Ginibre (the digamma value is 3), 2.03 for a non-Gaussian isotropic ensemble, and it tends to 2 for weak steps.
  - At the depth needed (11–16 steps), R spans 1.6–6.7 at the 5–95% level. All three sectors look typical, so nothing is predicted, and the realized values are registered data.
  - When the doublet chain is shared, the median |V_cb|/|V_us| is 2.4–49, again inverted.
- **Wilson mass varying in space.** A linear profile is Route 2 and needs a wall. A random profile should average out to the staircase plus shifts of the order of the variance (suggested, not computed).

## Which extra numbers look unavoidable (suggested)

Within the overlap class, three supplied inputs appear unavoidable:
- one width ratio per sector;
- a time-reversal-odd phase or a symmetry-breaking direction to split the degenerate pair;
- doublet positions that are not a cluster but graded, like Froggatt–Nielsen doublet charges (3, 2, 0). That is at least two more supplied ratios, needed to get |V_us| ≫ |V_cb|.

The only rigid structure left that needs nothing supplied is main's Koide circulant, where the open question is still where its phase comes from.

**Literature used only as templates:** Arkani-Hamed–Schmaltz and Mirabelli–Schmaltz (split fermions), Kaplan (domain walls), Craig–Sutherland (Anderson localisation in theory space), Newman (Lyapunov spectra) and Froggatt–Nielsen. I recalled the running masses from memory rather than fetching them.

## Files

Everything is in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/masswall/R2/`:
- `scripts/l1_symmetric_overlaps.py` and `l1.out`
- `scripts/l2_cluster_overlaps.py` and `l2.out`
- `scripts/l3_ckm_lyapunov.py` and `l3.out`
- `scripts/l4_lyapunov_ckm.py` and `l4.out`
- `scripts/l5_kink_profiles.py`, `scripts/l5b_kink_scan.py`, `l5.out` and `l5b.out`

Each run went through `capped.sh`, one process at a time, with peak memory at most 45 MB. No processes are left running.