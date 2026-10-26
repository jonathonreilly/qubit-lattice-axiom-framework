# T36 pre-registration (written before running any script)

Model used (supplied, not derived; the repo's own): Kawamoto-Smit staggered hopping on the
Z^3 torus of side 4 (`scripts/corner_kernel_cubic_carriers_..._2026_09_02.py`, note
`docs/CORNER_KERNEL_CUBIC_CARRIERS_...2026-09-02.md`). Corner kernel = 8-dim, Hamming grading hw.
hw=1 block = the "generation triplet" of L09-W2. Nothing is fitted to data.

## P1 (law level; the wall's own "cheapest step", part 1)
Question: does ANY operator that respects the lattice symmetry (24 proper rotation lifts; and,
separately, the KS one-site shift lifts) split the hw=1 triplet?
Computation: commutant dimension of the symmetry lifts on hw=1; number of generic levels.
- PASS reading (wall closed negatively at law level, and stronger than L09-W2(b)):
  commutant on hw=1 under O has dimension 1 (all three generations exactly degenerate).
- FAIL reading (a law-level splitting exists in the supplied model): dimension >= 2.
Side question: do the KS shift lifts preserve the hw grading? If they do not, the hw=1 triplet is
not a translation-covariant subspace (an extra supplied structure).

## P2 (state level; no-protection lemma)
For every subgroup H of the 24 rotations (all subgroups enumerated by closure), compute
  s_H = number of generic distinct levels of an H-invariant Hermitian operator on hw=1,
  n_H = dim of H-invariant traceless symmetric rank-2 spatial tensors + H-invariant axial vectors
        (vector rep = the 3x3 rotation matrices).
- PASS (claim holds): s_H >= 2  <=>  n_H >= 1 for every H, i.e. no residual symmetry splits the
  triplet while forbidding a spatial quadrupole or axial vector.
- FAIL: some H with s_H >= 2 and n_H = 0 (a protected splitting exists).

## P3 (locking in the corner model)
Add hw-graded masses mu_hw (staircase) and a source S on the hw=1 block. Diagonalise
H(pi+p) + M exactly for small p and read the quadratic coefficient tensor of the hw=0 branch.
- PASS (locking): that tensor is unitarily equivalent (up to fixed corner phases) to (M_1)^{-1},
  so its relative anisotropy equals that of the triplet's inverse mass matrix.
- FAIL: the tensor is insensitive to the splitting.
This is a statement about the supplied model; the physical reading is labelled separately.

## P4 (running, L16-W6 member)
One-loop SM Yukawa RGEs, M_Pl -> m_t, perturbative random 3x3 UV Yukawas (all singular values
<= 3). Measure the change of ln(sv_i/sv_j) between UV and IR.
- PASS (running can make ratios): the IR/UV ratio of a singular-value ratio exceeds 10 for a
  non-negligible (>1%) share of samples.
- FAIL: the amplification of any singular-value ratio stays below a factor 10 (in fact expected
  a small factor).
Also: price of the "registered data" reading under an O(1) anarchic ensemble = fraction of UV
samples whose up-type ratios fall in the observed window (reading, not a derivation).

## Outcome rule
If P1 PASS and P2 PASS: outcome PRICED (splitting is realized-state data; price = a state that
breaks O to a non-cubic subgroup, three numbers per sector, isotropy-tension with T14).
If P1 FAIL: STANDS with the law-level route named. If P2 FAIL: the protected-splitting route
becomes the best route and must be built.
