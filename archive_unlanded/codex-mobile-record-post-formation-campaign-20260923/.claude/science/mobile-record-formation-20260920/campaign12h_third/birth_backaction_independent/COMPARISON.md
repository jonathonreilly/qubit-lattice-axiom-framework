# Post-seal comparison: coherent motion, pair birth and occupation monitoring

This is a bounded source comparison after the independent reconstruction in
`REPORT.md` was sealed. That report, its controls, and its 19-artifact
pre-comparison packet remain unchanged. This is scientific scrutiny of the
supplied finite models, not a formal audit or publication determination.

**Disposition:** one narrow scope correction, F1 below. The completion proof,
the exact means under their intended Hamiltonians, and the distinction between
dark-state existence and empty-start accessibility agree with the independent
reconstruction. No other unresolved mathematical finding was identified in
these frozen sources. F1 remains open in the bytes reviewed here; the author
has agreed to make the correction after this seal.

## F1: specify H0=0 for the square waiting-time formula

Section 1 of `OCCUPATION_MONITORING_AND_PAIR_BIRTH_COMPLETION.md` permits an
arbitrary Hermitian H0 commuting with every occupation projector. Section 5
specializes graph, hopping, birth and monitoring rates, but does not explicitly
remove H0 before stating its exact square mean. The calculation and runner
use H0=0. The formula does not hold for the full Hamiltonian class allowed
earlier in the note.

An exact countercontrol, still respecting the cycle symmetry and every
occupation projector, is

    H0 = |holes02><holes02| + |holes13><holes13|,
    kappa = beta = d = 1.

Starting in the same opposite-hole antisymmetric state, direct inversion of
the complete two-hole killed Liouvillian gives

    mean = 55/16 = 161/48 + 1/12.

The positive mean operator satisfies its exact adjoint equation and all its
leading principal minors are positive. The calculation uses the independently
assembled full 16-state generator, not an author function or reduced formula.

**Narrow correction:** add “H0=0” to Section 5's square model and to the
symbolic clock result's stated conditions in the checker/output. No change to
the formula, numerical calculation, or general completion theorem is needed.

## Completion proof and convergence

The author's proof is a valid alternative to the pre-comparison trajectory
proof. Its load-bearing steps were reconstructed directly:

1. The vacancy count decreases at rate
   `-2 sum_e beta_e Tr(q_x q_y rho)`. At a stationary positive density,
   positivity forces every active vacant-pair support to vanish, hence every
   birth dissipator vanishes separately.
2. The Hilbert-Schmidt pairing with the remaining generator gives
   `-(1/2) sum_x d_x ||[n_x,rho]||_HS^2`. Thus the state is block diagonal
   in occupation patterns, without requiring classical internal colors.
3. The off-pattern Hamiltonian block is a nonzero scalar times the unitary
   map carrying the whole internal content factor. Commutation with H
   transports the positive density blocks and their traces. H0 has no such
   off-pattern block and cannot cancel the specified hop.
4. The fixed-cardinality exclusion configuration graph is connected. The
   author's spanning-tree leaf induction is valid, as is the independent
   edge-transposition argument. For each even vacancy count at least two,
   a pattern contains an active birth edge and has zero stationary weight;
   connectivity then removes that entire count sector.
5. Every stationary density in the even sector is fully occupied. Finite
   Cesaro limit points are stationary, and the full-occupation probability
   is monotone, proving convergence for every initial state. Compressing to
   the nonfull block gives a CP trace-decreasing semigroup. Its survival
   effect tends to zero in operator norm in finite dimension, so one common
   time with contraction factor below one supplies an exponential tail and
   finite mean.

This proof does not infer convergence of the internal density from convergence
of occupation. On full occupation H0 may continue to act unitarily. The
phase-covariance argument for first measuring total vacancy number correctly
handles coherences between count sectors without changing the stated
occupation statistics. The note does not assign an unmeasured-superposition
trajectory interpretation to those coherences.

The stated finite-dimensional K, connected nonzero-hopping graph, local
occupation monitoring, even-vacancy initial sector and nonempty active birth
set match the independently checked sufficient hypotheses. A well-defined
finite Lindblad generator also requires finite total rates beta_e; this is
the ordinary finite-rate interpretation used in both calculations. Neither
packet treats divergent channel sums or unbounded infinite-dimensional H0.
No perfect matching, bipartiteness or diagonal internal-state assumption is
used. The independent star control with one birth edge checks the absence of
a hidden perfect-matching premise.

## Clocks, dark spaces and accessibility

The three-state clock agrees exactly with the independent formula
`2/beta + beta/(4 kappa^2)`. Its Lyapunov solution has the correct off-diagonal
sign; the minimizing beta and mean are `2 sqrt(2) kappa` and `sqrt(2)/kappa`.
The classical comparison is `1/k+2/beta`, with no asserted calibration between
classical rate k and coherent coupling kappa. As a separate numerical control,
the critical-damping case beta=4, kappa=1, t=1 has exact birth probability
`1-5 exp(-2)`. The author value differs by about 1.7e-16. The other 19 numeric
points were read and authenticated, not independently replayed; the mean is
already established symbolically.

For one vacancy, the largest H-invariant subspace in ker Gamma is exactly the
undetected subspace. Its orthogonal complement reduces both H and Gamma and
has no imaginary-axis eigenvalue of `-iH-Gamma/2`; finite-dimensional Jordan
blocks do not spoil decay. The observability-stack criterion follows from
Cayley-Hamilton. Independent Krylov calculations give rank three for the
one-source square and rank four for the one-source cube. They verify the
localized square dark overlap 1/2 and the cube uniform-state eventual birth
probability 1/2. These one-vacancy checks were newly performed after sealing;
they are not misrepresented as part of the earlier blind derivation.

For the monitored square with H0=0, the author's six scalar equations agree
with the independent equations after the changes of variables p=2o and
a_total=4a. The full symbolic density residual in the author checker has the
correct dephasing rate: d for patterns differing at two sites, and 2d for
patterns differing at four. Its integrated trace is the same mean, with the
same small-d, large-d and large-beta limits. The general dark-state bound
`Pr(tau>t)>=exp(-2dt)` is also valid: using the equivalent jumps sqrt(d)q_x,
the first monitoring event has rate 2d in the two-hole sector. Before it, the
dark eigenstate acquires only a phase and a scalar no-jump factor. This is an
unraveling argument about the same Lindblad evolution.

For the unmonitored N4 torus, both calculations obtain 2,016 unordered pairs,
192 contacts, squared norm 512 and energy 4 kappa. The amplitude is symmetric
in the two holes and vanishes on coincidence and contact. The author uses an
x-oriented 31-edge matching, while the blind reconstruction independently
used a z-oriented one. Both leave 000 and 111. The comparison checker validates
all of the author's edges, distinct endpoints and the two remaining holes.

The author's positive-waiting-time continuity argument correctly promotes the
zero-waiting product to a positive-probability set of trajectories. It only
claims positive dark *component* from empty, with no useful macroscopic lower
bound. This agrees with the independently derived explicit but very small
lower bound. On the unmonitored square, by contrast, the opposite-hole dark
projector is conserved and orthogonal to every first-birth outcome from empty.
The only two-hole dark direction is that opposite-pair difference: a vector
in the zero-loss two-dimensional opposite-pair subspace is annihilated by
the hopping matrix only when its two coefficients sum to zero. Thus the
author's empty-square completion statement has the necessary accessibility
qualification and does not conflict with torus trapping.

## Executable coverage, identities and failed attempts

Both complete author notes were read (204 and 233 lines), as were both complete
checkers (124 and 121 lines), the complete result JSON files and receipts.
The two stdout files are byte-identical to their result files; both stderr
files are empty. All 12 bindings in the author pre-comparison seal authenticate.
The author scripts were not imported or rerun, which also avoids changing
their outputs. Authentication is distinct from independent mathematical
verification.

The new `comparison_check.py` imports only the earlier independent finite
generator. It reconstructs all five author stationary-operator nullities from
the full 256-dimensional generator restricted to the even sector, obtaining
`1,4,1,3,3`; checks the one-hole ranks; checks the alternative matching; compares
the exact mean expressions; and supplies the new H0 countercontrol. These
checks supplement, rather than replace, the analytic arguments.

One comparison-only helper assertion failed initially: the earlier helper used
structural SymPy matrix equality for the mean-operator residual. Nonzero H0
introduced unsimplified complex products. The archived diagnosis demonstrates
that every entry is exactly zero after simplification. The sealed helper was
left unchanged; the comparison-only code now expands the exact residual.
The original source, full log, stderr and receipt, and the complete diagnosis
are preserved under `failed_attempts/detuning_structural_equality/`. The final
comparison passed. This was not a failure of the mean equation or a discarded
counterexample.

A subsequent seal-helper attempt used `Path('.').parent` without first
resolving the path and therefore looked for the author manifest in the wrong
directory. It stopped before creating a seal. Its input/error and diagnosis
are preserved under `failed_attempts/seal_relative_parent/`; resolving the
independent directory before taking its parent fixes this bookkeeping issue.

The author also declares a preserved generic-rank performance interruption.
Its archive was not replayed or used as proof evidence here. The final exact
rank source and results are authenticated and independently corroborated.
The contextual literature abstracts were not re-read; neither author note
imports a theorem from them, and no external theorem is needed for this review.

Frozen principal identities:

| Source | SHA-256 |
| --- | --- |
| Independent REPORT.md | 6a01fe727d842624277c332f966c282a6e10035b6d7374934a1d80f16c103d04 |
| Independent PRE_COMPARISON_SEAL.json | f18244dc934652e8e6570923d5582476e605c10fb99615c6c7218037b05f5f09 |
| COHERENT_RECORD_MOTION_AND_BIRTH_BACKACTION.md | be2eef3b7257a95a58fe4ceba13b0b67f33f155101dc0ed89d400afb54bdc074 |
| OCCUPATION_MONITORING_AND_PAIR_BIRTH_COMPLETION.md | ae2f80e8b3b72cf601d458d2e13a4e6c9e5a591e7aa9f35ae1e9dbf3fdc85bda |
| quantum_birth_backaction_check.py | ea8041a3f5150cfd110ae4046bc2f51e068ce909e5dae5ee6826554dc464788f |
| pair_birth_dephasing_check.py | dbb3cc7cea1fbf5ecb575df47c428cbe039935925ae57a6dfaacfd873d779b62 |
| BIRTH_BACKACTION_AUTHOR_PRECOMPARISON_SEAL.json | 437ce4aa2f75bcde51eab5e7e31a27d4387d58d19dde0e54b4d155227dec859b |

`FINAL_COMPARISON_SEAL.json` binds the complete author packet and all preserved
independent evidence. Other third-campaign topics and the current campaign
checkpoint were not opened. No primary source was edited. This packet does not
establish volume-uniform completion, a quantum field phase, a native-site
implementation, or any general impossibility claim.
