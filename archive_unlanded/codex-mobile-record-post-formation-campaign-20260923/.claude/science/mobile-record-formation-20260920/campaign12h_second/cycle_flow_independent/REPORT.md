# Independent bounded-cycle flow review

2026-09-21. The finite-chain inequalities, constants, stationary scaling and
stated Gibbs/loop applications are correct under the displayed hypotheses.
No mathematical counterexample to those claims was found. One narrow runner
assertion needs correction: the advertised four-state history test does not
assert that its configurations are distinct. The current actual history is
correct; this is a verification-coverage finding, not a theorem failure.
This report assigns no formal audit or landing status.

## Finding F1: the four-state assertion admits an identity reversal

In `bounded_cycle_flow_check.py`, lines 163–168, the test condition checks
return to the initial state, eight immutable records, and zero charges. It
only *reports* `distinct_states`; it does not require that value to be four.
A targeted in-memory replacement

    reverse = lambda records, center, species: records.copy()

passes all three checks in `immutable_gauss_cycle()`, while reporting
`distinct_states=1` and `cycle_length=4`. All Fourier increments then vanish,
which also passes the one-sided increment bound. This is reproducible with
`check_runner_assertion.py`; baseline and mutation outputs, receipts and
source hash are preserved. No primary bytes were changed.

The narrow correction is to compute the number of distinct states and include
`distinct_states == 4` in the first check's Boolean condition. Requiring each
prescribed reversal to change its state is also reasonable but unnecessary
once the four distinct states and final return are checked. Re-run only this
baseline and identity mutation after that change. No mathematical note
correction or broader rerun is required by this finding.

## Mathematical reconstruction

The detailed pre-comparison proof is preserved in
`PRE_COMPARISON_DERIVATION.md`. For one directed m-cycle, the forward difference
G=T-I and positive dissipative form S=I-(T+T*)/2 diagonalize in the same Fourier
basis. Their nonconstant eigenvalues give exactly

    ||S^(-1/2) G S^(-1/2)|| = csc(pi/m),
    ||S^(-1/2) (G-G*) S^(-1/2)/2|| = cot(pi/m).

A constant stationary edge flow supplies only a common nonnegative weight.
Pulling ambient functions back to each cycle and applying Cauchy–Schwarz over
cycle weights proves the claimed strong sector bound. Repeated vertices do
not invalidate the pullback argument; splitting into simple cycles is another
valid route. Positive support is closed for a finite stationary chain.
Reducibility therefore needs no repair: functions constant on different
closed components can remain globally centered, nonzero, and frozen. No gap
or irreducibility is used. The eigenvalue sector bound follows by testing the
skew form on a complex eigenfunction; zero dissipation forces eigenvalue zero.

For the stationary semigroup,

    integral_0^t D(P_s f) ds = (S-||P_t f||_pi^2)/2,
    E_pi |f(eta_t)-f(eta_0)|^2 = 2 Re <f,(I-P_t)f>_pi.

The cycle bound followed by time Cauchy–Schwarz yields exactly

    E_pi |f(eta_t)-f(eta_0)|^2 <= C_M sqrt(2t D(f) S).

The absolute value of the intermediate complex scalar is sufficient; no real
observable restriction is missing. Nonnormality does not obstruct this proof,
and the bound does not classify arbitrary projected-memory dynamics.

For a bounded conserved site content, subtracting the event-center Fourier
phase gives |Delta F_N|<=2AsR|k|/sqrt(V). The uniform exit-rate assumption then
gives D(F_N)<=2 Lambda A^2 s^2 R^2 |k|^2, including its factor two. The phases
must correspond to K in 2pi Z^3 and a valid local periodic unwrapping. With
fixed M, bounded stationary S_N, and fixed K,T, the displayed Euler-time
mean-square bound is O(N^(-1/2)). It also vanishes for microscopic
`t_N=o(N^2)`. The zero mode is exactly conserved. Finite sets of fields/modes
are covered; existence, tightness, growing mode sets and a diffusive limit
are not established. The supremum remains outside expectation.

## Application and challenged boundaries

A plaquette permutation has R^4=id. Its Gibbs stationary flow is constant
on each orbit after canceling the exterior Hamiltonian; removing self events
leaves cycles of length two or four. Reverse rotations add reverse cycles.
A Metropolis bond contributes the two-cycle weight
`kappa min(pi(eta),pi(eta^xy))`. Their sum and restriction to a closed count
sector give the required configuration-flow decomposition with M=4. Uniformly
bounded local interactions and multipliers, finitely many event types per
site, and conserved content supply the remaining rate/support assumptions.
A bounded stationary structure factor is still a separate hypothesis. The
proof establishes none for an arbitrary Gibbs interaction.

For the thirteen-label loop example, reversal order A,B,A,B on disjoint
loops forms four distinct configurations. Each move preserves capacity,
immutable identities and both microscopic Gauss fields. A common orbit flow
divided by positive orbit weights is stationary. Local Gibbs weights permit
local bounded rates because their exterior factor cancels; taking the minimum
orbit weight divided by the current weight is one explicit bounded choice.
This does not establish Gibbs invariance for arbitrary additional translations
or classify every possible E/B coupling.

The scope challenges give concrete countercontrols, rather than objections to
hypotheses the note already states:

- A clockwise particle makes spatially local jumps but has a configuration
  cycle of length N. Its Euler-time correlation tends to exp(2pi i t), and
  its sector constant diverges. The note's countercontrol is correct.
- Independent reversible nearest-neighbor dimers have M=2 and structure
  factor S_N=(1/2)sin^2(pi/N). Their Fourier fluctuation satisfies Lf=-2f,
  so its relative mean-square change is 2(1-exp(-2t)). At Euler time this
  tends to two although the absolute fluctuation vanishes. A small structure
  factor cannot be silently renormalized using the absolute freezing result.
- Symmetric exchanges started from the full-support inhomogeneous product
  p_x=1/2+delta cos(2pi x1/N) have expected Fourier change asymptotic to
  -2 delta pi^2 T sqrt(N) at time NT. Its squared mean grows linearly in N,
  while the homogeneous stationary law has bounded S_N=1/4 and M=2.
  Stationarity cannot be discarded. The displayed stationary proof supplies
  no automatic formation-state or initial-layer estimate.

The note preserves these distinctions. It makes no universal exclusion,
quantum-vacuum, all-record-model, or pathwise maximal claim requiring repair.

## Verification coverage and reproducibility

Before reading the author runner or numerical constants, the reconstruction
and independent checker were sealed under `PRE_COMPARISON_SEAL.json`, SHA-256
`d1e80df6fb761c83ed16bfac9b59cf9eaf46f7e10dce09eefc24c7d19f50c32b`.
The independent code supplies exact rational matrix certificates for optimal
cycle constants and a nonuniform seven-state chain with overlapping cycles
and two closed components; complex semigroup/energy checks; a complete
sixteen-state Gibbs plaquette flow decomposition with period-one/two/four
orbits and Metropolis channels; a side-seven immutable two-loop history; and
the three scope countercontrols above. The energy integrals and exponentials
are numerical controls, not substitutes for the preceding uniform proof.
The exact matrix and Gibbs flow identities are rational symbolic checks.

All independent assertions passed on the first run. Full stdout and empty
stderr are retained. The deliberate identity-reversal mutant passed the
original author's assertion; that unexpected acceptance is preserved as F1,
not discarded. After the pre-comparison seal, the complete author runner,
result JSON and run log were read. All ten recorded rows and the final total
match, and both note/runner hashes match the result's source bindings. Only
three author loop controls were executed selectively, as baseline and mutation;
the full author suite was not repeated. Authentication of its rows is not
counted as new independent mathematics.

Run `python3 independent_check.py` for the independent checks. The targeted
runner test is `python3 check_runner_assertion.py`; source authentication is
`python3 compare_sources.py`. They write only in this review directory. Runtime
identities are recorded in `SOURCE_COMPARISON.json` (Python 3.13.5, NumPy 2.4.4,
SciPy 1.17.1, SymPy 1.14.0). No external theorem was imported; bibliographic
novelty and the original papers' broader hypotheses were not reviewed.

The exact primary identities are:

| Source | SHA-256 |
|---|---|
| BOUNDED_CYCLE_FLOW_AND_EULER_DYNAMICS.md | c100b9f20e091b944a78499c0112aae4803fdfb6b54f4e28330714a58b580b56 |
| bounded_cycle_flow_check.py | 4f7b078d8e0afc908e5315efb5c785f892295380e7753030f0edc73a2feeffbc |
| LOCAL_GIBBS_RECORD_CIRCULATIONS.md | 70a9abf1588e90e8a7065a5e1d6155f8f56997672b0303c0ea6cbca71fc1bf12 |
| MICROSCOPIC_GAUSS_IMPULSE_AND_RECORD_LOOPS.md | 684f10acda3ebf659ed4b1b47e3fbe35a29c92dfbe1fee77e9cd9469b27f0c30 |
| BOUNDED_CYCLE_FLOW_RESULTS.json | 1f2a545d2f885e48a1bab9843f6cc8d4c22bc01287b0cb900754b3bcd61aa9cb |
| BOUNDED_CYCLE_FLOW_RUN.log | 1e18f566b488b34a34ca8fb8adf27ee9619263595e997f383d467bc88bcd7e6d |

`FINAL_SEAL.json` binds all six sources, unchanged instruction/skill identities,
and every review artifact. Commit/branch provenance was supplied in the brief;
this check authenticated working-file bytes and performed no Git operation.
F1 is the sole open correction at this frozen source revision.
