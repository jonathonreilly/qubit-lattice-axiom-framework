# A53 report: the 16-site gap, local-singlet rivals, and a 24-site exact test

Everything is in `SP/c8/A53/`, where SP = `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad`. The running log is `NOTES.md`, and `chain.log` holds the queued runs. I made no repo edits, git writes or PRs, and ran no audit or review lanes. Every rule is a supplied exploration under decision 22; nothing is adopted.

## 1. Verdict

- **The 16-site gap comes from that cluster, not from the rule (EXACT).**
  - Its ground state is exactly a product of singlets on the 8 site pairs that the cluster's wrapping makes (002)-partners six times over.
  - Every other correlation is exactly zero. Cube and plaquette singlet weights equal a random state's.
- **The gap persists at 24 sites, in every symmetry sector checked (EXACT bounds; interpretation ARGUED).**
  - The parton's exact energy is −1.7488 per site.
  - The lowest state found is at −2.0168.
  - In the parton's own main sector (k = 0, A1) the lowest state is at or below −2.0073, with overlap ≤ 5×10⁻⁶.
  - The low state takes its advantage from couplings the wrapping enhances again: ⟨σ·σ⟩ = −0.97 on 36 doubled face diagonals, with nearest-neighbour bonds uncorrelated.
- **On 6³, 8³ and 10³, none of the rivals I computed beats the parton (rivals EXACT; parton CHECKED).**
  - Products of block singlets with 2–18 sites lose by 0.041–0.061 per site.
  - Block-modulated partons (cube or plaquette blocks) rise monotonically away from the parton.
  - A rough dressed-cube estimate (ARGUED) lands within 0.005 per site. So the parton's lead over a correlated cube crystal is not established.

## 2. Question

Take A51's best finite-reach rules: J_NN = 1, dual-frame two-place class sums, plus A49's star four-spin terms.

- Is the 16-site gap a quirk of 16 sites?
- Does it persist on a 24-site exact cluster?
- Does any local-singlet rival beat the parton on large grids?

## 3. Answers

### 3.1 The 16-site ground state (EXACT; t1_16)

Pair types are labelled class × multiplicity of the wrapped operator. Values are for the L6 rule; the L8 rule has the same structure.

| Pair type | Pairs | GS ⟨σ·σ⟩ | Parton ⟨σ·σ⟩ |
|---|---|---|---|
| (001)×1 | 48 | 0.000 | −1.089 |
| (011)×2 | 48 | 0.000 | +0.603 |
| (111)×4 | 16 | 0.000 | −0.419 |
| (002)×6 | 8 | **−3.000** | +0.752 |

- **Mechanism.** All six (002)-type displacements of a site land on the same partner. So the (002) pairs form a perfect matching, each pair carrying 6J(002) ≈ 2.2, and the ground state puts a singlet on each pair.
  - Energy check: 0.373(−9) + 0.119(5.196) + 0.190(2.121) = −2.335. The only four-spin terms that survive are the Dm sets made of two such pairs.
- **Singlet weights.** Cubes 0.055 and plaquettes 0.125, exactly the random values 14/256 and 2/16. The parton gives 0.347 and 0.438. The ground state is built from wrapped distance-2 pairs, not from local clusters.
- **Controls.**
  - Two independent kernels and the flip-reduced sector agree.
  - They reproduce A51's E₀/N (−2.33458, −2.30279), parton energies (−1.77524, −1.76626) and overlap (1.98×10⁻⁴).
- **Why I keep the wrapped convention.** Counting each pair once does not help on 16 sites: it leaves 3 face-diagonal and 0.5 (002) bonds per site, and moves the parton to −3.87 per site. The wrapped convention keeps the per-site term count: the parton sits at −1.775 (16 sites) and −1.749 (24 sites), against −1.715 to −1.728 on 6³–10³.

### 3.2 Exact block-singlet products against the parton

**Factorization (EXACT).** For SU(2)-singlet blocks:
- two-place terms between blocks vanish;
- four-spin terms split 2+2 give ⟨σσ⟩_A⟨σσ⟩_B, or one third of that when the pairing crosses the split;
- all other splits vanish.

Brute force on an 18-site region confirms this to 4×10⁻¹⁵. The S = 1 negative control fails by 0.017, as it should. For the tilings below, enumeration finds no star four-set split 2+2. So each product's energy is exactly its block's restricted-rule singlet ground-state energy.

| Rule | 2×2×1 | 2×2×2 | 2×2×4 | 2×3×3 | Parton (CHECKED) | Best − parton |
|---|---|---|---|---|---|---|
| 6³ inner | −1.61239 | −1.65459 | −1.66582 | −1.66593 | −1.72681(10) | +0.061 |
| 8³ inner | −1.59654 | −1.63287 | −1.64354 | −1.64408 | −1.69469(11) | +0.051 |
| 10³ inner | −1.58052 | −1.61240 | −1.62103 | −1.62121 | −1.66262(14) | +0.041 |
| 6³ r4 | | −1.65867 | −1.66942 | −1.66908 | −1.72841(11) | +0.059 |
| 8³ r4 | | −1.64623 | −1.65725 | −1.65773 | −1.71461(13) | +0.057 |
| 10³ r4 | | −1.64938 | −1.66069 | −1.66101 | −1.72022(16) | +0.059 |

- **Control.** Columnar dimers come out at −1.50000, matching A51's VMC VBS value of −1.502(1).
- **Margin trends.**
  - It shrinks slowly with block size.
  - It shrinks with L under the size-dependent inner rules (0.061 → 0.041).
  - It is flat at 0.058 under the fixed short rule.
- **Dressed-cube estimate (ARGUED, not a bound).**
  - Two coupled cubes (2×2×4) gain 0.17–0.18 over two separate cubes.
  - Crediting three such interfaces per cube gives −1.722, −1.697, −1.664 (inner rules) and −1.723, −1.712, −1.717 (r4 rules).
  - Estimate minus parton is +0.005, −0.002, −0.002 (inner) and +0.005, +0.002, +0.003 (r4).
  - The estimate ignores non-additivity and channels that involve three cubes.

### 3.3 Block-modulated partons (CHECKED by VMC; δ = 0 values EXACT)

Hops between blocks are scaled by δ. δ = 1 is the parton; δ = 0 is the projected product of block partons.

| | δ = 0 | 0.3 | 0.6 | 0.85 | 1 |
|---|---|---|---|---|---|
| Cubes, 6³ | −1.65137 | −1.66359(45) | −1.69543(39) | −1.72130(19) | −1.72681(10) |
| Cubes, 8³ | −1.63001 | | −1.66823(36) | | −1.69469(11) |
| Plaquettes, 6³ | −1.61239 | | −1.69058(35) | | −1.72681(10) |

All three rows use the inner rules.

- **Shape of the family.** It is monotonic. Shifting the tiling maps δ → 1/δ, so δ = 1 is stationary, and it is the minimum: E(0.85) − E(1) = +0.0055(2), which is 27σ.
- **δ = 0 states.** The projected cube parton has overlap 0.994 with the exact cube ground state. The dimer and plaquette partons coincide with their blocks' ground states.

### 3.4 The 24-site cluster (EXACT bounds; lz24, an24, lzpg)

- **Cluster.** Lattice vectors 2(1,−1,0), 2(0,1,−1), 2(1,1,1).
  - Every index-24 sublattice of 2Z³ contains a vector with length² ≤ 8. Up to symmetry, this one is the only choice without nearest-neighbour doubling.
  - The parton has a closed shell (gap 4.00, APBC).
  - Wrapped pair types: (001)×1 72, (011)×1 72, (011)×2 36, (002)×3 24 (forming 8 triangles), (111)×2 12, (111)×3 24.
- **Sector.** 1,352,078 flip-even states. Singlets are flip-even when N ≡ 0 mod 4.

| State | ⟨H⟩/N or Ritz/N | Overlap² with parton |
|---|---|---|
| Lowest found (random start; residual 0.020) | **−2.01678** | 4.4×10⁻¹¹ (⟨T_a⟩ −0.9994 vs +1) |
| Lowest k = 0 found (translation-symmetrized, converged) | −2.01450 | 1.6×10⁻¹⁰ (a different point-group irrep) |
| k = 0 A1 sector (79% of the parton), after 110 steps | ≤ **−2.00727** | ≤ 4.9×10⁻⁶, still falling |
| Cube-singlet product on this cluster | −1.63276 | 0.16 |
| Parton (exact amplitudes) | −1.74883 | 1 |

- **Anatomy of the lowest state** (state / parton):
  - ⟨σ·σ⟩ on (011)×2: −0.971 / +0.636; on nearest neighbours: +0.032 / −1.055; on (002)×3: −0.203 / +0.500.
  - Face-diagonal class energy: −2.105 / +2.39 per site. Four-spin terms: about +0.21 / −1.53.
  - Singlet weight on cubes: 0.107 / 0.352; on plaquettes: 0.142 / 0.436.
- **Symmetry.**
  - The rule is invariant under the cluster's six proper rotations (defect 4×10⁻¹⁵) but not under its mirrors (term defect 0.0027).
  - The parton is not a rotation eigenstate here: it splits A1 0.791, E 0.209, A2 0.
- **Interpretation (ARGUED).**
  - On Z³ each face diagonal carries J₂ once, and the face diagonals form two frustrated FCC lattices.
  - On this cluster, the wrap doubles 36 face diagonals into a 3-regular network with couplings of 1.54, which can be almost fully singlet-paired. This is the 16-site mechanism in another form.
  - This cluster's shortest wrap vector has length² 8, the same as the 16-site cluster's.

## 4. Methods

- **Rules.** `rules51_L.npz`, keys B4_r4 and B4_inner. The infinite-lattice operator is wrapped onto each cluster, as in A49/A51's fwd16.
- **Exact kernel (`a53lib.py`, numba).**
  - σ·σ = zz + 2X; the products (σσ)(σσ) are expanded the same way.
  - Star four-spin terms are regrouped by star centre into 7-bit pattern tables.
  - The S^z = 0 sector uses spin-flip reduction and Lin two-table ranking.
- **Lanczos.**
  - Two passes with checkpoints; pass 2 recomputes every α and checks it against pass 1.
  - Sector runs use Hermitian symmetrizers Π_a(2 + T_a + T_a⁻¹)/4 and the D3 A1 projector.
  - The overlap is read off as the first component of the Ritz vector.
- **Blocks.** Open-cluster exact diagonalization, combined with the factorization above.
- **VMC.** A51's sampler and estimators, with block-modulated π-flux hops.
- **Parton energies.** From A51's saved samples.

## 5. Checks

| Run | Runtime | Peak memory |
|---|---|---|
| t1_16 | 91 s | 179 MiB |
| bench24 (matvec 1.9 s; parton amplitudes 5.9 s) | 13 s | 219 MiB |
| lz24, random start (6 runs) | 246 s × 5, 10 s | 166–183 MiB |
| lz24, parton start | 247 / 223 s | 183 MiB |
| lzpg A1 (plus 1 redundant rerun) | 242 / 18 / 241 s | 182–195 MiB |
| an24 | 40 s | 433 MiB |
| t2_check / ref51 / t3_once16 | 1.1 / 0.2 / 4.6 s | 137 / 114 / 184 MiB |
| t2_prod ×4, t2_cubeparton ×2, t2_blocks ×2 | 0.6–108 s | 122–205 MiB |
| vmc53 ×5 | 266–267 s | 100–190 MiB |

- **Run conditions.** 38 run.sh invocations, one at a time, at load 2.3–5.2 with 30–41% memory free.
  - Two were SKIPPED: desktop apps pushed the 1-minute load to 10.1 and 7.7, and the chain retried.
  - Longest run 267 s; highest peak 433 MiB.
- **Controls passed.**
  - The 16-site numbers reproduce A51's.
  - The factorization holds and its negative control fails.
  - The dimer product equals A51's VBS.
  - VMC: Casimir estimator deviation ≤ 4×10⁻¹¹; drift ≤ 1×10⁻¹².
  - Lanczos: every α reproduced in pass 2, and |P_A1 D p|² equals the parton's A1 weight.
- **Flagged and fixed.**
  - The first factorization check double-counted, and its region had no 2+2 sets.
  - an24 failed twice: once because pass 2 ended 4 steps short, once on an import.
  - The first form of lzpg assumed the parton had ±1 characters; it does not, so I replaced it with the A1 projection.
- **Caveat.** The random-start vector is not fully converged (residual 0.020). Its energy is an exact upper bound, but its anatomy describes a mixture of near-degenerate low states.

## 6. Open edges

1. A variational dressed-cube state, for example a cube product with exact perturbative dressing or a cluster-correlator VMC, to settle the near-tie in §3.2.
2. A larger, less-wrapped cluster. The 32-site 2·BCC cluster has shortest wrap length² 12, but it has 6×10⁸ states, beyond this machine. COMPARATOR (from memory): small 3D clusters are known to show strong shape effects.
3. The parton's E-sector weight (21%) on the 24-site cluster, and the low spectrum sector by sector.
4. Long-range four-spin terms, and full-reach rules in the block contest.

## 7. Plain-language summary

We asked why a small grid that can be solved exactly has a much calmer state than the two-part background. On the 16-place grid it is a quirk of that grid. Wrapping it around makes each place meet one partner six times over, and the calmest state just locks those partners together in pairs. A 24-place grid shows the same kind of quirk through a different set of doubled links. On large grids we built rivals from locked groups of 2 to 18 places and computed them exactly. We also blended the background toward them. None beat it; the best came within about 0.04–0.06 per place. A rough estimate for loosely linked cubes comes very close, so that contest is still open.