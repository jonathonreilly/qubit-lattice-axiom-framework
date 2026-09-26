# Gauge readout and local RK cooling: bounded author-source comparison

Date: 2026-09-22. This is a post-seal scientific comparison, not an audit,
publication, or native-implementation determination.

## Outcome and read boundary

No material mathematical correction or consequential prose/code discrepancy
was found in the authorized packet. Both arguments agree with the independent
reconstruction under their stated finite-system, supplied-apparatus premises.
The setting convention for the X readout differs from the independent one by
the harmless relabeling `s_author = -s_independent`; the Y convention agrees.

The original `REPORT.md`, both independent runners, their complete results,
the three preserved development attempts, and every original seal binding are
unchanged. In particular, the independent polynomial degree-lowering proof of
cooling attraction remains the proof recorded in that report. The author's
different exponential-vector proof is assessed below; it has not been substituted
for the independent argument.

The fixed pre-comparison seal is
`99c8c68ce7803368e633fdf7f3d7314eb1f47f7ba3150a3fa732888e1f1a43b3`.
All 43 bindings (four sources and 39 artifacts) were authenticated again.
Only after explicit authorization did this comparison open the author seal
`d9ea3fc91a09aff6e197925cd2a37907217f4583a8bf29a9a871a64423c2b8fc`
and its 13 named artifacts. All 13 hashes and byte counts match. Both complete
notes, both complete runner sources, every result field, both receipts, and the
source-context JSON were read. The complete stdout files equal the corresponding
result files byte for byte; both stderr files are empty. The two receipts record
successful execution and bind the correct script hashes.

No adaptation/weighted-cooling packet, later CQ/cutoff or Hamiltonian-change
source, campaign checkpoint, or registry was opened. The context JSON's link
to an additional cutoff-context file was not followed. Its historical provenance
statements are recorded author assertions, not an additional independently
reviewed source here. No author runner was imported or executed, and no author
file was modified.

## Readout argument and exact signs

The distinguished link is raised by W and has Z=2E. For the two fresh-charge
branches, `V_q^dagger V_q = P_v(I-qZ)/2`. Thus q is the negative of the incoming
edge-Z value in an electric-basis trial, and two branches each carrying rate beta
have total loss beta P_v, not 2 beta P_v. The supplied operators preserve the
full Gauss generators and increase matter record number by two.

For the author's pulse `S_s=exp(-i s pi Y/4)`, direct algebra gives

    S_s^dagger Z S_s = Z(I-P)-sX,
    m_s = -<Z(I-P)>+s<X>.

Consequently `(m_+-m_-)/2=<X>` and the fair, input-independent setting estimator
`s*q` is unbiased. Our sealed construction used the opposite sign of the Y
pulse, explaining its estimator `-s*q`. The two schemes are identical after
relabeling the setting. For the author's Y measurement, the pulse is
`exp(-i s pi X/4)`, and the correct estimator is `-s*q`. These are the signs
actually implemented by the runner. The imaginary cat `(a+i b)/sqrt(2)` with
`W a=b` has Y expectation -1 with this definition of Y; the reported output
does not make the common opposite-sign mistake.

The nonflippable term is retained before the setting contrast. A single setting
is not an unbiased arbitrary-state loop measurement. The author explicitly
requires matching input ensembles or randomized settings independent of the
input, and distinguishes that from sequential probes on the same disturbed
state. The operator identities hold with arbitrary spectator correlations.
Balanced output coarsening gives effects `(I +/- X)/2` or `(I +/- Y)/2`; retaining
both setting and charge records is a finer instrument. The source does not
equate these different retained-outcome instruments or claim a joint sharp
measurement of X and Y.

The diagonal phase synthesis `D X D^dagger=Y`, with `D=exp(-i pi Z/4)`, is correct.
The fresh-probe cubic identity, Gauss/resource conservation, and fuel/spent
Kraus extraction agree with the sealed independent full-space calculation.
The author's 16-field, 144-matter/field, and 432-dilated dimensions are correct.
Its bit convention is the reverse ordering of our initial bit-word enumeration;
the physical flippable words and pulse signs agree, rather than depending on
their numeric basis indices.

The readout source states the needed boundaries: initially vacant endpoints,
supplied qutrit/link/probe roles and controls, fresh fuel and output removal,
backaction, and separately supplied transport if probe sites are to be reused.
The finite closed dilation is reversible; boundary-time fresh-probe permanence
is not asserted for every instant of a reused finite apparatus. Conserving the
displayed resource/rest count is not conserving an arbitrary interacting field
Hamiltonian. The earlier single-carrier gate substitution is a conditional use
of its already checked assumptions, not a newly verified many-carrier model.

## Cooling proof, including its new analytic step

The model is precisely `H=sum h_p P_p^-` with real h_p, positive gamma_p and the
listed jumps L_p, within one finite connected flip component. No arbitrary
extra Hamiltonian or jumps are included. Fixed spectator-independent flip
displacement and disjoint pairs for each plaquette are load-bearing premises.

The loss operator K is strictly positive on the orthogonal complement of the
uniform target u, because its quadratic form is the positive weighted sum of
all pair differences. The source's separating diagonal observable
`F(c)=sum 3^l E_l(c)` has distinct values on distinct spin-half configurations:
the largest differing coefficient strictly dominates the sum of all smaller
coefficients. Its increments Delta_p are constant across the p pairs. On each
pair, the ratio of difference and sum amplitudes in `exp(tF)u` is
`-tanh(t Delta_p/2)`, so Eq. (1), including its sign and the nonflippable sector,
is exact.

For a putative nonzero invariant W contained in u-perp, invariance under R and
the jumps implies that W-perp is invariant under their adjoints. Hence both
compression equalities used in Eq. (2) are valid even when W does not reduce R
or any jump. At t=0 the compressed R-dagger has strictly positive Hermitian
part K/2 and is invertible. Continuity provides a nonempty interval of
invertibility; Eq. (2) forces `P_W exp(tF)u=0` throughout that interval.
Differentiation and the Vandermonde spanning argument then force W=0. No
commutation of the different P_p^- is needed, and signed, inhomogeneous h_p
are allowed. The very large F coefficients are only a separation device,
not a physical coupling or a quantitative gap estimate.

The remaining finite-semigroup step is also valid. The target-orthogonal corner
is an autonomous completely positive trace-decreasing evolution. Persistent
positive trace would give a nonzero positive stationary corner by Cesaro
averaging. Zero leakage and its diagonal/off-block stationary equations give
a support invariant under both R and all jumps, which has just been excluded.
Finite dimensionality then gives exponential corner decay with model-dependent
constants; positivity bounds the full trace distance by twice the square root
of the corner trace. A singleton component is the trivial already-target case.

This supplies the needed invariant-subspace verification rather than importing
it from uniqueness of the common dark vector or from Kraus et al. The source's
four-state counterexample is exactly the one independently reconstructed:
connected pair graph, unique uniform common dark vector, yet a rank-two
stationary density orthogonal to that vector. Its inconsistent displacement
equations would identify distinct configurations, violating the physical
embedding premise. The countercontrol therefore supports the theorem's scope
and does not refute the theorem with all its hypotheses.

## Collision and event-resource claims

The local nilpotent partial-isometry collision has the stated Kraus operators.
With `cos(theta)=exp(-gamma_p dt/2)`, its reduced channel is exactly the one-term
dissipative semigroup. Noncommuting plaquette channels plus the Hamiltonian
require the stated Trotter limit; their finite-step product is not the full
simultaneous semigroup. The independent report preserves a numerical finite-step
countercontrol to that stronger statement.

The jump-count claim follows from `K u=0` and exponential corner decay:
`E N_jump = integral Tr(K rho_t) dt < infinity`, so the resolved cooling-jump
count is finite almost surely. It does not yield a deterministic storage bound,
a finite exact stopping certificate, or a finite bound on all fresh no-click
probes needed for an ideal continuous limit. Two permanent outputs per jump are
a further explicitly supplied interface; the field-only L_p does not itself
create the qutrit charged pair of the readout construction.

The cooling runner's resource matrix on its two outcome-number sectors is
`2(P_spent+P_fuel)=2I`. Its commutator check is consistent but tautological on
that restricted encoding: it is not a separate microscopic record-transport or
full-energy test. The note makes the intended supplied-interface and energy
limits explicit, so this does not require a scientific correction. Keeping
the spectator-pair alternatives coherent in each L_p is also part of the
specified coarse jump. A measurement resolving those alternatives would need
its own channel assessment.

The local jump's relation to Weimer Eq. (12), and the stated limited use of
Kraus Theorem 2, agree with the independently pinned v2/v3 source readings in
the original packet. Neither source is treated as a new general principle or
as a replacement for the present hypotheses and proof.

## Verification coverage and limits

The new standalone `comparison_check.py` does not import either author script.
It completed on its first execution; stdout equals `COMPARISON_RESULTS.json`
and stderr is empty. Its additional controls are:

- Direct bit-transition reconstruction of all 24 reported phase-state outcome
  probabilities, all 14 nonflippable bias rows, both pulse identities, and
  the diagonal phase synthesis, with exact SymPy arithmetic.
- The author's exponential-vector identity on the independently selected
  five-state, three-square component, using a different separating linear
  functional and exact rational powers at t=log(2). Its three increments are
  57, 114 and 228. The full R-dagger combination is exact for the independently
  chosen inhomogeneous gamma and signed h; the Vandermonde determinant is
  21895775886512782739520. This is a control of the identity, not the all-size
  proof, and leaves the independent polynomial proof unchanged.
- An independently assembled open-cube component and its 81-dimensional
  Liouvillian, constructed through action on matrix units with row-major
  vectorization. This differs from the author's Kronecker implementation.
  A separate modulus 257 with i mapped to 16 certifies rank 80. Together with
  the exact target nullvector, this proves complex nullity one for that fixture.
  Its numerical gap is 0.8676724142632016. Expected total jump counts for the
  selected basis state and mixed state are 3.2205813001704713 and
  3.199535228041951. They match the author values; late-row observable
  differences are at most 5.42e-16.

All author numerical result fields and their implementing code were inspected.
The author periodic 864-state traversal was authenticated and reviewed in code,
not independently rerun. It concerns the 24-link periodic two-cell cubical
geometry implemented by the runner, with distinct wrap links; it is neither
a simple undirected eight-vertex graph with only 12 edges nor a census of the
entire Gauss sector. Its stated traversal-only scope is correct. The smaller
author nullity certificates, reward outputs, and time samples remain finite
controls; neither their exact ranks nor the floating gaps establish a
volume-uniform rate. The independently selected three-square component was
already checked before author access and remains separately sealed.

No complete author-suite replay, efficient thermodynamic preparation, state
communication between disconnected flip components, formation-plus-cooling
joint theorem, native one-M2 compiler, autonomous fresh-stream theorem, or
Maxwell/Coulomb-phase result is claimed. All three original helper failures
and their repairs remain preserved; this comparison added no failed attempt.

## Exact source and evidence identities

The complete source/artifact rows are in `FINAL_SEAL.json`. Principal identities:

| Item | SHA-256 |
| --- | --- |
| Author readout note | 8cdf426a9e96a01602a0e77874bc05b939a8c0bf372a11cda2acc0f647be84d0 |
| Author readout runner | 84666c00f11256630fb1f2a7f5ad6de7a98c81c7a93e1b0953b3e3dd1f2ed7a3 |
| Author readout result/stdout | 159fad39fb3a12327859a2c035f9519ee48d89e44d4288a9b8aa0d0d8c921078 |
| Author cooling note | 7fa8e6b7a84b3467b784283f596ef192ceab6fbc18172f18fd93e1d139a2791f |
| Author cooling runner | 9faf0f87d0574368feb0f656308308c269d3df922bfff7576a8d6d10182b5552 |
| Author cooling result/stdout | 5c1771868cd2086b074e8e81629046a5fb7d1aa4b51c0decd4fd548c34133e7d |
| Original independent report | d72068c4dae9a210224f5c7217dc9b6ded91ea0422f7f14ec9ff1b659302747f |
| New comparison runner | f31cf946ecac63e96bad5b8737675f277b9528051fc1d80642f0ffd83a024480 |
| New comparison result/stdout | 84285d52346c119e2902422766cd9039f9321195ccc26b5161c0ccb9954c8a08 |

Reproduce only the new checks with
`/opt/homebrew/opt/python@3.13/bin/python3.13 comparison_check.py` from this
directory. The runner reads the frozen prior evidence and authorized sources;
it writes only its comparison result beside itself. Preserve the recorded
logs/receipt/seal before intentionally rerunning a time-stamped result.
