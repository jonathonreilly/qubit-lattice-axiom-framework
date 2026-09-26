# Certified band gaps of the relaxed compass carvings N20 and N16 in every translation-invariant gauge sector

Task `J:derive:deferred-20260925-band-gauge:a1` · worker `w-jonathonsmac4f50-j7516` · model `claude-opus-5-5` ·
origin/main `e37967e326` · checker `check.py` (exact; about 5 s).

**Provenance.** The source PRs (9048, 9054, 9088, 9097, 9112) come from `claude/dynamics-clause-*` branches. That is
the same model family as this attempt, though not this machine's induced-law blocks. No independence is claimed, and
cross-model confirmation is needed.

## Obligation chosen

The landed PR 9054 note keeps the momentum scans only as diagnostics:
- N20: "two near-zero bands and smallest sampled nonzero absolute energy about 0.61787 on 16³ points";
- N16: "four near-zero bands and sampled separation about 1.437".

It adds: "calling it a gap requires further control between samples". This attempt supplies that control.

For every translation-invariant gauge sector and every momentum on the three-torus, it proves exactly how many zero
bands there are and a uniform lower bound on every other energy. The enclosures are tight to about 1.6 % (N20) and
0.25 % (N16). The corrected witness (the 28-edge simple cycle in the N16 lift) is preserved and re-verified.

## Setting (supplied; conditional exactly as landed)

- The model: the landed runner's carvings N20 and N16 on the 4×4×4 torus, with compass bonds K = 1.
- The record contents: (1, √2, √3) with the constrained axes zeroed, then normalised. Each dangling field is the sum
  of its two record contributions.
- The auxiliary Majorana matrix A(k): bond entries −2u e^{ik·off} and field entries ±2h, as in the runner's
  `majorana_matrix`. Single-particle energies are the eigenvalues of iA(k).
- A **translation-invariant gauge sector** means u = 1 on the runner's spanning tree and u = ±1 on the non-tree bonds:
  2⁴ sectors for N20 and 2³ for N16.
- Physical projection onto D_j = 1 is not addressed. These are statements about the auxiliary quadratic operator, as
  the landed note requires.

## Steps

1. **CHECKED A (bipartite).** Every nonzero entry of A(k) joins the two sides:
   - one side holds the even sites plus the b-Majoranas of the odd sites;
   - the other holds the reverse.

   So iA(k) = [[0, iM(k)], [(iM(k))*, 0]] and the energies are ± the singular values of M(k). |A| = |B| = 17 for N20
   and 14 for N16.
2. **PROVED + CHECKED B (flat bands at every k).** The support of M(k) does not depend on k. Its maximum bipartite
   matching is 16 (N20) and 12 (N16). Every term of det M, and of each largest minor, needs a matching of that size,
   so rank M(k) ≤ 16 (resp. 12) at every k. That gives at least 1 (resp. 2) zero singular values, and at least 2
   (resp. 4) zero energies, at every k.
3. **PROVED (gauge).**
   - Choose a spanning tree of the quotient graph and let x_j be the unwrapped lift positions along it. The unitary
     diagonal similarity D = diag(e^{ik·x_j}) maps the entry of bond (a,c) to −2u e^{ik·(off + x_a − x_c)}. Each b-Majorana
     takes its site's x.
   - Along the tree the exponent vanishes, so after the gauge only the non-tree bonds with nonzero winding depend on
     k. There are 3 such bonds in both nets.
   - check.py verifies, for the tree it uses, that every k-dependent bond lies in the deleted row or column.
4. **PROVED (interlacing).** Let M′ be M with row r deleted. Then M*M − M′*M′ = r*r ⪰ 0, so by Weyl monotonicity
   σ_i(M) ≥ σ_i(M′) for each i in descending order. Columns follow likewise via Mᵀ.

   Deleting one row and one column removes every k-dependent entry. Hence σ_i(M(k)) ≥ σ_i(M′) for all k, where M′ is
   a fixed k-independent matrix.
5. **CHECKED D (exact certificates).**
   - M′ uses exact rational brackets of its algebraic entries: square roots come from integer isqrt, and the error is
     bounded by ‖E‖ ≤ mn·max|E_ij| < 10⁻³⁷.
   - The exact inertia of M′ᵀM′ − c²I, computed by congruence with 1×1 and 2×2 pivots, gives:
     - N20, 16×16: inertia (16, 0, 0) at c = 0.6079 in 8 sectors and at c = 0.7858 in the other 8.
     - N16, 13×13: inertia (12, 1, 0) at c = 1.4333 in all 8 sectors, so only the kernel lies below c.
6. **CHECKED E (upper bounds).** At the minimising momenta the matrix M(k*) is real. An exact test space spanned by the
   kernel vector(s) and one more rational vector, with Courant–Fischer, bounds the band:
   - N20 sector (−1,1,−1,1): ≤ 0.6179 at π(1,0,1);
   - N20 sector (1,1,1,1): ≤ 0.7959 at π(0,1,1);
   - N16: ≤ 1.4368 at π(1,1,1).
7. **CHECKED F.** The 28-edge simple cycle in the N16 lift is re-verified, so the lift is not a tree. The quotient
   cycle ranks are 4 and 3.

## Theorem (bounded instance)

In every translation-invariant gauge sector, and for every k ∈ T³, the auxiliary Bloch Hamiltonian has:

| Net | Zero bands | Every other energy | Sectors | True minimum lies in |
|---|---:|---|---:|---|
| N20 | exactly 2 | \|E\| ≥ 0.6079 | 8 | [0.6079, 0.6179] |
| N20 | exactly 2 | \|E\| ≥ 0.7858 | other 8 | [0.7858, 0.7959] |
| N16 | exactly 4 | \|E\| ≥ 1.4333 | all 8 | [1.4333, 1.4368] |

"Exactly" follows because step 2 gives at least that many zero bands, and step 5 gives rank ≥ 16 (resp. 12). The
sampled values 0.61787, 0.79585 and 1.43679 lie in these enclosures. The lower-energy N20 class is the runner's lowest
sampled sector.

**Mechanism.** The gap band is nearly flat: for N20, σ₂ ranges over [0.6179, 0.6189] across the zone. So the mode
barely feels the three winding bonds, and removing them costs under 2 %.

## First unresolved step and remaining obligations

1. **Non-periodic gauge fields and the global flux minimiser.** Translation-invariant sectors are a finite family. An
   arbitrary Z₂ field on the infinite lift is not covered. The same interlacing idea applies to supercells: delete
   the lines of the winding bonds of the supercell.
2. **Physical projection** onto D_j = 1 and the spin-sector degeneracy: open, as landed.
3. **Tighter constants.** The certified bound sits 1.6 % below the true minimum. Better trees, or deleting fewer or
   other lines, could close it. A certified minimum is not claimed.
4. **The other PRs in the bundle.** The time-reversal-odd star terms and the Chern number claims (9088, 9097, 9112)
   are not addressed.

## ASSUMED

- The supplied carvings, record contents, compass bonds, the Majorana representation, and the runner's gauge-sector
  convention.
