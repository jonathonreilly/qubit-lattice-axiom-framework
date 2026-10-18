# Fixed-size hierarchical native tunneling check

Disposition: PASS for a fixed finite even M>=4 and fixed even open longitudinal Lz>=6, conditional on the stated native fourth-order plaquette coefficient and independently established minimum pair-column tunneling coefficient. No counterexample from gauge, energy dependence, longer-range events or diagonal loops was found. The argument below explains why this can concern the actual finite Hamiltonian rather than just its leading truncated model. It is not uniform in either size.

## Required exact reduction

At fixed sizes, the full N=0 eigenspace of H0 is separated from the other H0 energies by a nonzero constant. Use its exact analytic symmetry-equivariant Kato/direct-rotation effective Hamiltonian K(lambda). It is finite dimensional and isospectral to the actual isolated low band. Its Taylor coefficients contain the stated number of native transverse insertions. Thus an entry changing k entire columns has order at least k Lz/2. Plane parity requires k even. In particular every offdiagonal entry starts at order Lz; equality for a two-column entry requires nearest-neighbor columns and exactly their connecting edge on every longitudinal layer. The known coefficient is -t, t=Jz lambda^Lz/2^(Lz-1), in both directions for even Lz. No extra pair-channel coefficient is chosen.

In the diagonal part, the leading nonconstant term is -K sum plaquettes P with K=(Lz+14)Jz lambda^4/128. Transverse winding length-four single-color loops at M=4 are spin-sign-independent; they do not add another plaquette term. Higher diagonal coefficients change defect energies only relatively by o(1) at fixed size. Symmetry makes the diagonal value exactly common on P+ configurations, not just common through a selected order. Subtract that scalar and divide the exact matrix by Jz lambda^4. Its diagonal has a fixed positive gap from P+ to its complement, while all offdiagonal entries are O(lambda^(Lz-4)). Analytic second-stage isolated-subspace perturbation is therefore valid. This is the appropriate rigorous framework; a low-order truncation alone would not suffice for arbitrarily large fixed M.

## Valuation of offdiagonal paths

For a second-stage path with b offdiagonal N=0 events, let k_i>=2 be the number of columns changed at event i. A target row or column flip changes M columns, so sum k_i>=M. Its native degree is at least (Lz/2) sum k_i; the b-1 intermediate excited-plaquette denominators cost at most 4(b-1) powers. Consequently:

- If b<=n=M/2, the exponent is at least n Lz-4(b-1), minimized at b=n.
- If b>=n, sum k_i>=2b, so the exponent is at least b(Lz-4)+4, minimized at b=n because Lz>4.

Equality requires b=n, k_i=2 for every event, and total native degree n Lz. Every target column is changed exactly once, with no spectator column changes. Therefore the events are disjoint nearest-neighbor dimers on that row/column. Long-range pair events, simultaneously changing more columns, repeated events and higher corrections to a minimal pair all have strictly larger valuation. This also proves that no offdiagonal P+ splitting occurs earlier: the smallest nontrivial row/column-gauge pattern has M changed columns. For M>=4, equality gives a single row or column.

This bound uses matrix-element support/degree, not a guessed norm comparison between a large event and several small events. Intermediate returns to P+ cannot occur on an equality path: a proper collection of dimers is not another gauge pattern.

## Folds, energy dependence and gauges

One can include the exact diagonal part in the unperturbed second-stage resolvents, whose leading denominators are the plaquette defect energies. Their relative corrections vanish as lambda->0. Energy-dependent Feshbach denominators differ from these by the low eigenvalue displacement. After subtracting the common diagonal P+ value, that displacement starts at least quadratically in the small offdiagonal norm, O(lambda^(2(Lz-4))) in rescaled units. Thus it cannot affect the leading offdiagonal coefficient. Equivalently, folded terms need a proper P+ return; any folded offdiagonal term contains an earlier offdiagonal P+ process or an additional diagonal return loop. The former is absent below the derived order and the latter adds positive valuation. Plane symmetry makes all purely diagonal return corrections common on P+, including their dependence on the spectral parameter.

Use a symmetry-equivariant near-identity reduction throughout. An arbitrary O(1) change of ground-band basis changes the displayed row-flip matrix representation, though not its spectrum. Higher analytic near-identity ground-block gauge rotations cannot change the first nonscalar coefficient, because all preceding ground-block terms are scalar. This is the precise gauge statement; equality of unrelated truncated matrix gauges is not needed.

## Coefficient and sign

A row ring of M=2n sites has exactly two perfect nearest-neighbor matchings. For one fixed matching, a proper subset of its dimers has k connected runs and creates 4k bad plaquettes, costing 8K k. Each pair event has amplitude -t. The product of n vertices and n-1 negative denominators is negative.

The sum over dimer orders of the product of inverse run counts is binom(2n-2,n-1). To see this, the proper-subset recurrence divides the sum of predecessor weights by its run count; its solution is the product of Catalan numbers of the run lengths. Closing the last missing edge of the n-cycle gives n Catalan(n-1)=binom(2n-2,n-1). The n=2 case is also direct: two orders, each with one run. Adding the two matchings gives offdiagonal matrix element -tau, where

    tau = 2 binom(2n-2,n-1) t^n/(8K)^(n-1),
    exponent = n Lz-4(n-1).

This is the leading row/column amplitude of the actual finite low-band Hamiltonian after its two analytic reductions. The effective leading operator is a sum of those commuting whole-row and whole-column flips (with their global redundancy); claiming a particular smallest spectral gap additionally requires diagonalizing that finite character operator rather than identifying the amplitude with the gap.

## Boundaries

The result is an asymptotic finite-size statement with constants depending on M,Lz. It assumes open longitudinal boundaries, even Lz, the supplied native Hamiltonian and the stated native K and t coefficients. It does not establish useful coupling thresholds, a growing-size expansion, an observable transition, a neutral readout coupling, or an empirical force. One state per symmetry character and neutral-observable selection may make these splittings invisible to the original neutral readout.

## Root attempt and explicit example

Read /private/tmp/neutral_hierarchical_root.md after completing the argument above. Its valuation inequality agrees with this derivation. The remaining word-count premise is supplied by the exact first Kato reduction: H0-diagonal resolvents/projectors and folded products preserve the count of transverse V insertions and cannot reduce the physical Hamming distance of an order-p matrix entry. This resolves the flagged simultaneous-event/gauge concern.

For M=4,Lz=6: n=2, K=5Jz lambda^4/32 and t=Jz lambda^6/32, hence tau=Jz lambda^8/320. The regular row/column-flip representation has the single product-character constraint +1. Its leading -tau sum of 2M flips has unique all-plus character ground; the next allowed character has two minus signs, so the leading gap is 4tau=Jz lambda^8/80. These are asymptotic consequences, not 96-qubit diagonalization results. A physical local Z on column (x,y) changes precisely its row and column characters and has leading matrix element one between the corresponding Fourier-character states. It therefore can reach the charged leading line; an invariant neutral C cannot. This extra response observation uses the same finite-size isolated-band analytic reductions and supplies no neutral/cosmological identification.
