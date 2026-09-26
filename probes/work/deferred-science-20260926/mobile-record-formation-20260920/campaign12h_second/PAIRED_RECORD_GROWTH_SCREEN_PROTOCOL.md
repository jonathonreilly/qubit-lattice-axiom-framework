# Declared growth screen, before production

2026-09-21. Target the actual local birth and immutable permutation process,
not a reference equilibrium dimer sampler. The question is whether the new
parallel-swap channels repair typical formation/accessibility enough to
justify a larger correlation or dynamical study. A simulation is not a
proof of full packing, ergodicity, a Coulomb phase or a wave limit.

Models: retain beta births, kappa rigid translations and nu original full-cube
exchanges exactly as in the frozen first note. Add the 45 parallel-subset
swap channels per cube from the separate jam/escape note, each at rate mu.
The baseline has mu=0. The first extended setting uses beta=kappa=nu=1,
mu=1/15, so additional attempted swaps total 3 per site per unit time.
These rates are supplied and do not define a physical clock.

Implement a continuous-time uniformization with null events. Attempt rate
per volume is 3 beta + 3 kappa + 3 nu + 45 mu. Translation attempts select a
site and direction uniformly; both endpoints propose the same whole-dimer
move, yielding total kappa for each dimer/displacement channel. The content
projection omits accepted permutations that do not change site contents;
record identities are unnecessary for those projected statistics, and that
omission does not remove any formation transition. Separate exact histories
already track actual immutable identities.

Before production, compare all accepted channel outputs and their
multiplicities, including periodic wraparound, against a separate Python
implementation on small specified/random valid configurations. Check the
empty-state birth derivative, the periodic jam with zero baseline exits,
the explicit new escape, validity and conserved direction counts under each
conservative channel, and the symmetric reverse support. Save the initial
implementation and any failures; do not redefine the target after observing
outcomes.

Initial screen: even sides 4,6,8,12, empty and periodic-jam starts; at least
four fixed seeds per initial condition for each of baseline and extension;
horizon 1000 in the supplied time units. Stage a smaller side/horizon pilot
first to measure runtime and inspect diagnostics, then apply this grid if
appropriate. Compare vacancy density/time curves, full-packing hitting times,
accepted motions and site-renewal counts. Preserve every seed, failed run,
nonfilled state and trapped example. Extending time/size depends on the
specific uncertainty left by this screen and must be recorded separately.

At logarithmic snapshots, record the instantaneous squared Fourier amplitudes
of the standard staggered dimer field in the first two axis momentum shells,
separating longitudinal and transverse components. These are diagnostics of
the actual formation states, not equilibrium averages. Three axis modes and
four seeds give limited statistical information. A flat transverse signal or
small longitudinal signal alone establishes neither a Coulomb phase nor
quantum-vacuum correlations. Do not fit continuum exponents to this pilot.

Decision rules: exact accessible counterexamples can refute a universal
support claim. Finite successful fill histories show possibility only.
Persistent vacancies with no enabled event produce a verifiable blocked
configuration; persistent vacancies with enabled events remain finite-time
kinetic evidence. If formation routinely reaches full packing, inspect
conservative activity and dependence on initial state/count sector before
calling the state equilibrated. If the additional moves are ineffective,
return to a constructive support analysis before spending on larger runs.
