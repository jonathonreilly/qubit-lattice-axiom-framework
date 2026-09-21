# Local-dilute quantum curl: bounded independent check

**Disposition:** no actionable mathematical defect or consequential source/code
drift found. The supplied local Hamiltonian has the stated active-cell
positivity bound, and the uniform fixed-mode collision estimate proves its
carrier-subtracted fixed-particle Euler limit. This does not close the
original immutable-record, formation, positive-gapless-vacuum or constraint
selection questions. It is a scientific check, not formal retained status.

The complete note was read first. `INDEPENDENT_DERIVATION.md`, an independently
assembled finite checker, outputs and logs were sealed before author access:
`PRE_COMPARISON_SEAL.json` SHA-256
`4868b4ac03254f3e04994e942f6bcae17161646c9ec564005651ef225578af09`.
Afterward the complete author code/results, successful logs and two preserved
failed runs were read and authenticated. No author code was executed or edited.

## Reconstructed proof

The actual two-qubit singlet/triplet space has at most one excitation per
cell, including across different triplet components. In the normalized
bosonic occupation embedding, an allowed hop has unit amplitude, while a
hop into any occupied cell is removed. Hence the physical n-sector is exactly
`mu n + P dGamma(c C_N) P` on its hard-core subspace. This is a compression
of the generator; the note does not mistake it for compression of the free
unitary group.

The real symmetric centered curl has Fourier eigenvalues
`0,+|sin k|,-|sin k|` and norm at most sqrt(3). Therefore

    H_N >= (mu-c sqrt(3)) N_exc.

For the stipulated strict inequality on mu, the specified active-cell system
has its unique singlet product ground state and a uniform gap lower bound.
The microscopic coefficients and adjacent-cell supports are uniform in N.
The given fine packing has maximum support diameter three Manhattan steps;
it selects a pair direction and does not establish the original fine-lattice
law or its rotational covariance. Ground-state uniqueness refers to the
specified active two-qubit-cell Hilbert space. Retaining the illustrative
packing's unused qubits as unconstrained decoupled degrees of freedom would
add degeneracy; they must be fixed or pinned for an enlarged-system uniqueness
claim. The source uses that packing to assert support locality only.

For s distinct Fourier wavevectors, each compressed position projector has
operator norm s/V, independent of polarization. The first-quantized union
bound for a coincident particle pair gives, for every entangled vector in
the fixed n-particle Fourier space,

    ||Q_N psi||^2 <= binomial(n,2) s^2/V = delta_N^2.

Free curl evolution preserves this exact finite-mode space. Thus the bound
is uniform over all free times. Variation of constants on the hard-core
space and `||dGamma(c C_N)||<=n c sqrt(3)` give

    ||U_hc(t)phi_N-U_0(t)psi_N||
      <= delta_N [1+n c sqrt(3)|t|]+delta_N^2,
    phi_N=P_N psi_N/||P_N psi_N||.

There is no omitted normalization denominator: comparing the two physical
initial vectors costs `1-||P_N psi_N||<=delta_N^2`. For t=N tau, fixed n,s
and bounded tau, the error is O(N^-1/2). The proof requires delta_N<1 to
normalize the physical vector. The hard-core/free comparison is exact for
n=0,1; the subsequent finite-lattice-to-continuum sine replacement generally
is not exact for n=1.

The one-particle symbol error is bounded by
`c |2pi q|^3/(6N^2)`. Second quantization costs at most n and Duhamel over
scaled time costs T, proving the additional error in equation (9).

Exact local matrix algebra gives the mode-commutator error at most 2m/V on
the sector of at most m excitations. Each phased correction is supported on
occupied cells and preserves their set, so the norm estimate needs no
independence. It yields the canonical core algebra. The real-space canonical
equations for the rotating-frame generator are
`Q_dot=c curl P`, `P_dot=-c curl Q`, with an onsite bracket. They are distinct
from the derivative bracket of the previously checked positive-block model.

Removing the carrier is an exact number-conserving rotating-frame operation.
It does not remove the laboratory gap or make the curl energy positive.
Longitudinal and extra sine-zero branches remain. The source explicitly
retains these boundaries and does not infer unbounded-field convergence
from the bounded-observable norm estimate.

## Independent controls and author comparison

Before comparison, the independent checker constructed actual side-3 and
side-4 cubic matrices and verified all 24 proper cubic transformations. It
assembled physical two-particle hops directly and separately assembled the
free boson generator, including occupation square roots. Their compressed
matrices agree exactly. Physical/free dimensions are 3159/3321 and
18144/18528. The local commutator relations are checked exactly, including
the sharp diagonal 2m/V example at m=2.

An entangled two-mode superposition with c=.4 was evolved at three scaled
times on each actual torus. The complete finite physical sectors were kept.
The collision, forcing and Duhamel bounds all hold. Free evolution separately
constructed from 3-by-3 polarization matrices agrees with the full free
two-particle exponential to below 2.01e-16. The side-3 two-particle laboratory
bottom is approximately .81350713, above the proved .61435935 bound. These
floating-point values corroborate the proof; they do not prove its scaling
rate or positive-density behavior.

After the seal, `compare_author.py` independently checked all nine author
symbol rows and all nine dynamic rows' collision and bound arithmetic.
Using the sealed independent occupation construction, it reproduced the
three N=3 author free/continuum errors to at most 1.56e-15. N=4 and N=6
author trajectories were authenticated, not replayed; the blind controls
already used different states and rates on N=3,4. The author's full three-cell
tensor calculation is correctly distinguished from the three-dimensional
two-particle tests. The results contain numerical evaluations of exact
symbol formulas, not certified exact floating-point values.

The author's first preserved run used a Python without SciPy and failed
before executing its controls. The second failed an N=6 normalization
assertion. Our independent reconstruction reproduces the standard norm's
squared value `.9942129629627128`, whereas compensated summation gives
`.9942129629629627`, agreeing with the analytic `.9942129629629629`.
The complete source delta is exactly the addition/use of compensated norm
accumulation. All original tolerances and the theorem are unchanged. Both
failed receipts bind the preserved prior checker. The final author run and
both independent runs exited zero with empty stderr. No independent failed
attempt occurred in this packet.

## Limits and identities

The result fixes particle number, Fourier mode list and scaled time horizon
before taking N to infinity. It neither covers a fixed positive density nor
growing mode lists or arbitrarily long scaled times. The assumed projected
Fourier initial state is not prepared by the earlier birth law. The newly
supplied Hamiltonian changes local singlet/triplet contents, and its cell
architecture is additional structure. No unchanged-projector, original-rate,
electric-Gauss, interacting matter or photon-vacuum theorem follows.

All exact source and evidence identities are bound in `FINAL_SEAL.json`.

| Source | SHA-256 |
|---|---|
| DIMER_LOCAL_DILUTE_QUANTUM_CURL_LIMIT.md | 34ab30936006b553c778d9b050b226e8270a653d278875eab966b445d776043c |
| dimer_local_dilute_curl_check.py | 429536b7ba4ffa5d97ae94b929c6215b2f56309a862db6d4f785391d10eb4e11 |
| Author RESULTS.json | bdb9f286ba919d4cea3fcda4c1371b237da64689db5f18581186277c6ba9179a |
| Preserved pre-repair checker | 7bc27e9f5247416ba03c16185f4d56bd31735086e38871ff1b1be57c3e47dae8 |
| Independent checker | 435d32300bedc9de810d9f7d61ad21f244a084746de1db1faba6e3118d9e7921 |
| Independent comparison | d80631f418abf5a9b0626771773b746e2035e4a46bc7cd6b0f4acac01cac7e3f |

Reproduce using `python3 independent_check.py` and `python3 compare_author.py`
in this directory with NumPy, SymPy and SciPy. They write only their own
result files. Original raw logs and command/hash receipts are preserved;
reproduction may update result timestamps. No new external theorem import
was required, and the previously checked finite-block sources remain unchanged.
