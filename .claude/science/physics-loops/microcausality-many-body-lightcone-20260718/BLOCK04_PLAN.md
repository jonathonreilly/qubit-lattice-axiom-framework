# Block04 plan — fermionic even-CAR walk-expansion LR bound (bridge, CAR half)

Date: 2026-07-18. Family: microcausality-many-body-lightcone. Fourth
block: takes the CAR half of the named "fermionic transfer bridge"
(block03 Non-Claims). The transfer-operator identification (Berezin /
log-transfer) is NOT attempted and remains open.

## Why the qubit theorem does not directly apply

Jordan-Wigner maps even fermionic bond terms to qubit bond terms only
when the two sites are adjacent in the JW ORDER. For a general pair
(generic in Z^3 embeddings), the JW image carries a Z-string through the
intermediate sites: pre-battery gate F8a shows the image of the hop
between JW-nonadjacent sites fails to commute with an intermediate qubit
X, i.e. it is NOT supported on the two qubit factors. CAR locality
nevertheless holds (F8b: it commutes with the intermediate CAR
generators of both parities). So the fermionic statement needs an
intrinsic graded-locality lemma, not a representation transfer.

## The one new load-bearing lemma (L-F, rebuilt from CAR relations)

Disjoint-support EVEN elements commute with arbitrary disjoint
elements; odd-odd disjoint pairs anticommute. Proof: cross-site
generators anticommute ({c_x, c_y} = {c_x, c_y^dag} = 0 for x != y), so
moving one generator across an even monomial (2m generators) gives
(-1)^{2m} = +1; iterate over the second monomial's generators;
bilinearity. With L-F replacing tensor-factor disjointness, every step
of block03's chain (reduction, self-drop, Jacobi, norm transport,
iteration, walk counts, assembly) applies verbatim to even bond
Hamiltonians on the CAR algebra.

## Pre-battery (all OK after one probe-indexing fix, session record)

- F1 CAR relations hold in the 4-site JW representation (all pairs).
- F2 graded table: even-disjoint commutes (vs even, density, odd);
  odd-odd disjoint anticommutes with nonzero commutator.
- F3 hopping term Hermitian with exact norm 1.
- F4 fermionic boundary reduction [H, n_0] = [hop_01, n_0].
- F5 odd-term necessity: odd "bond term" anticommutes with disjoint
  odd observables — the reduction step fails without evenness.
- F6 cone: k = 0,1,2 below-cone vanishing at d = 3 against BOTH even
  and odd probes; arrival at k = 3 on both. (First run used a
  mis-indexed probe — site 2 instead of site 3 — and correctly showed
  arrival at k = 2 = that probe's distance; fixed.)
- F8 JW-string exhibit pair as above. F9 [h,h] = 0, sums Hermitian.

## Theorem to land

For finite Lambda in Z^3, supplied EVEN Hermitian bond terms h_b on the
CAR algebra, ||h_b|| <= J, A in CAR(X), B in CAR(Y) of arbitrary
parity, X cap Y = empty (d >= 1):

  ||[tau_t(A), B]|| <= 2||A|| ||B|| (n_X/10) sum_{k>=d} (20 J |t|)^k/k!

all t, volume-uniform; mu-reweighted exponential form and 20eJ readout
inherited from block03. Neither scale claimed sharp.

## Cluster discipline

PR #4 in the family: cluster-cap evaluator MUST be re-run and recorded
before the PR (block03's evaluation said "no fourth same-surface PR" —
this is a DIFFERENT surface: new algebra, new lemma; the evaluator must
say so explicitly or the block does not ship).
