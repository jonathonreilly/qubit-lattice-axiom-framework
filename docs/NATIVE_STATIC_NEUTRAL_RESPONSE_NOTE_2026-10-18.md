# Static neutral response of the microscopic ground band

**Status:** bounded-support.
**Primary runner:** [scripts/native_static_response.py](../scripts/native_static_response.py)

A large internal composite does not by itself give a long-range mediator.
For the same supplied XX/YY/ZZ Hamiltonian and joint weak-coupling even-cube
regime as the [ground-window theorem](NATIVE_MICROSCOPIC_GROUND_WINDOW_NOTE_2026-10-18.md),
the static retarded response between separated local plane-invariant probes
has an exponentially decaying upper bound. This is a result about that
neutral ground-state response, not a no-go for every force or every state.

## Why small ground-band splittings do not supply a neutral mediator

The coefficient ground patterns are s_xy=a_x b_y. On an all-even periodic
cube, the X and Y plane flips act on these patterns as the regular
representation of Z2^(2L-1). The physical product of all those generators is
Z_all, not the identity on the full Hilbert space; its value is +1 on this
band. Each allowed character therefore occurs exactly once.

The symmetry-preserving normal-form dressing and the gapped interpolation
to the actual Hamiltonian preserve those integer character ranks. The exact
lowest band also has one state per allowed character, even if its energies
split. A plane-invariant observable cannot connect different characters,
and there is only one band state in each character. Consequently all its
inelastic transitions from an actual ground character cross the gap to the
complement, Delta >= c Jz. No lower bound on internal splittings is assumed.

This includes local Z_r Z_(r+2ez), native energy bonds, and their neutral
commutators. Every actual ground density has the same response bound:
character coherences drop out of the retarded commutator. Elastic mixture
covariance and isothermal changes of character populations are different
quantities and are not bounded by this argument.

## A direct static-response estimate

For Hermitian neutral local A and B, the response to a diagnostic perturbation
-hB is chi_AB = 2 Re sum_n A_gn B_ng/(E_n-E_g). This defines a response
coefficient; it does not add a proposed physical interaction to H.

Use f_sigma(E)=(1-exp(-E^2/(2 sigma^2)))/E. Its Fourier kernel under
f(E)=integral k(t) exp(iEt) dt is

    k_sigma(t) = -i sign(t) erfc(sigma |t|/sqrt(2))/2.

The filtered susceptibility is integral k(t)<[A,tau_t B]>dt. The spectral
error is at most 2||A||||B|| exp(-Delta^2/(2sigma^2))/Delta.
A finite-range Lieb–Robinson bound controls times |t|<=r/(2v); the Gaussian
kernel controls the remaining times. Choosing sigma^2=2 Delta v/r gives

    |chi_AB| <= C_XY ||A||||B||
      [Delta^-1 + sqrt(r/(Delta v))] exp(-kappa r),
    kappa = min(mu/2, Delta/(4v)).

Here r is torus support distance, and C_XY depends on the fixed local
supports. The small-r bound 2||A||||B||/Delta is also available. The native
velocity bound v=O(Jz a) and gap Delta>=c Jz bound the response range by a
constant times lattice spacing a, independent of lambda in this family.
This is an upper bound, not a measured correlation length.

Extended sources are bounded by summing local pair estimates with absolute
weights. Their size may amplify the prefactor but does not create a 1/r tail
at separations beyond their supports with fixed weights. The feature's
internal length lambda^(-2/3) a is therefore not a derived mediator range.

## Evidence and limits

The [root proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/STATIC_NEUTRAL_RESPONSE_PROOF.md)
and independent [character](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_STATIC_CHARACTER.md)
and [filter](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_STATIC_FILTER.md)
checks give the derivation. The runner checks finite character multiplicities,
Y-plane phases, Fourier normalization and signed cross-spectral filter bounds.
It does not numerically certify the microscopic gap.

The premise remains the specified ground-state and weak-coupling growing-box
family. Charged probes, excited features, critical/isotropic regimes, thermal
states and unrestricted thermodynamic limits remain outside this result.
In particular, factors in a feature–environment interaction can carry plane
charge; this result cannot be applied to them merely because the total
Hamiltonian is neutral. It does not rule out every possible native force.
No observation is fitted or independently tested, and no cosmological scalar
or physical detector identification is established.
