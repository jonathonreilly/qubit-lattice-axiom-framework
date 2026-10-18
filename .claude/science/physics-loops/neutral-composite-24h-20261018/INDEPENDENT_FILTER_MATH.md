# Independent Gaussian-filtered neutral operator check

This is a direct mathematical check of the supplied construction. No repository files changed and no numerical spatial-localization claim is made.

## Definitions and normalization

Use the normalized time kernel

O_tau=(1/(sqrt(2pi)tau)) integral_dt exp[-t²/(2tau²)] exp[-i omega0 t] O(t).

With O(t)_ab=exp[i(Ea−Eb)t]O_ab, the matrix element filter is exactly
F_tau(Delta)=exp[-tau²(Delta−omega0)²/2], Delta=Ea−Eb.

Without the displayed prefactor the filter acquires sqrt(2pi)tau; normalized overlaps/linewidths stay unchanged but the quoted absolute norm z changes. The structure-factor frequency convention must use the same Delta sign.

Let the original nonzero operator have normalized positive spectral measure p, total mass1, in the specified stationary-state inner product. Set

m_tau=integral F_tau dp,
z_tau=integral F_tau² dp,
p_tau(domega)=F_tau² dp/z_tau.

Then z_tau is the filtered squared norm relative to the original squared norm, and the normalized squared overlap is m_tau²/z_tau (F real nonnegative). These statements rely on positivity and a common inner product; they are not valid with a signed response function substituted for p. Any disconnected zero-frequency expectation should be explicitly retained or removed before defining p.

## Smooth continuum asymptotics

Assume p has a density s in a neighborhood of omega0, s(omega0)=s0>0, with enough local regularity for the indicated asymptotics and no atom at omega0. Contributions from outside a fixed neighborhood are exponentially small. Let x=tau(omega−omega0). Dominated localization yields

m_tau ~ sqrt(2pi) s0/tau,
z_tau ~ sqrt(pi) s0/tau,
m_tau²/z_tau ~ 2sqrt(pi) s0/tau.

For a locally C2 density the odd Gaussian moment cancels the linear term in m,z; their next correction is order tau^-3. Under p_tau,

E[omega]−omega0 = s'(omega0)/(2s0 tau²)+o(tau^-2),
Var(omega)=1/(2tau²)+o(tau^-2),
std(omega) ~1/(sqrt2 tau).

Thus the root's three leading formulas are correct. The narrow normalized wavepacket loses both its unnormalized spectral weight and its squared overlap with the original operator as tau^-1. After unit normalization its norm is1 by construction; it is the required rescaling1/sqrt(z_tau) and disappearing original overlap that diagnose the small selected weight. Do not describe the unit-normalized packet itself as having vanishing norm.

## Order of limits and exceptions

The continuum limit must resolve the filter: at finite volume the relevant level spacing must satisfy tau*delta_omega <<1, or the thermodynamic spectral measure must be taken before tau→infinity. At fixed finite volume, eventual Gaussian filtering is a spectral selection among finitely many transitions, not evidence for a new isolated mode.

An atom of weight a at omega0 gives m_tau→a,z_tau→a, squared overlap→a, and width→0. This is a pre-existing spectral line with nonvanishing selected weight. Finite systems also have atoms; persistence with volume, support, temperature and perturbations is needed to distinguish a thermodynamic mode. If the target lies off every finite-system line, z_tau→0 exponentially. After normalization the nearest line(s) win: a unique nearest line gives zero width around its own frequency, while equal-distance lines on opposite sides can retain a nonzero limiting width. The normalized mean need not approach the requested omega0.

At a one-sided threshold s(omega0+x)~C x^alpha for x≥0, alpha>−1,

z_tau ~(C/2)Gamma((alpha+1)/2) tau^−(alpha+1),
m_tau²/z_tau ~C 2^alpha Gamma((alpha+1)/2) tau^−(alpha+1).

The mean offset is Gamma((alpha+2)/2)/Gamma((alpha+1)/2)/tau, and the standard deviation is

[Gamma((alpha+3)/2)/Gamma((alpha+1)/2)−(Gamma((alpha+2)/2)/Gamma((alpha+1)/2))²]^(1/2)/tau.

Thus even the1/sqrt2 linewidth coefficient is not universal at a threshold. Vanishing/divergent densities, gaps, singular-continuous measures and unresolved lines need their own asymptotics. A nonzero target atom overrides the smooth background's tau^-1 leading behavior.

## Spatial support and operational meaning

If the supplied microscopic Hamiltonian obeys a finite-velocity locality estimate, evolution of an initially local O for times of order tau spreads its approximating support to a radius of order v*tau, with tails controlled by that estimate and the Gaussian time tail. This is an upper-bound construction, not a proof that the actual packet radius grows linearly or a universal lower bound on spatial size. Cancellations, nondispersive modes or strictly local conserved operators may behave differently. For the actual lattice, reconstruct the spatial kernel by finite-momentum FFT and measure a declared norm-weighted radius/tail fraction, checking mesh size and periodic wraparound. A frequency-width calculation alone does not verify spatial locality.

The two-sided time filter is an operator definition using positive and negative times. It is not automatically a causal laboratory preparation protocol; any physical implementation or success probability requires an additional construction. Unit normalization can magnify small tails/errors as z_tau decreases.

## Is this a scalar?

Neutrality only means zero conserved charge/syndrome; it does not establish a scalar rotational representation. If O is already a rotation singlet and the dynamics commute with rotations, this time filter preserves that singlet transformation law. For omega0≠0 the filtered operator is generally non-Hermitian even when O is Hermitian; a real field would require a properly paired positive/negative-frequency construction. Neither fact gives a relativistic scalar action or universal conformal matter coupling.

In a smooth continuum this construction produces a selected narrow continuum wavepacket. It does not move poles, change the Hamiltonian, create an isolated excitation, establish an autonomous local degree of freedom, derive a kinetic coefficient/potential, or solve source/detector matching. To claim a new scalar mode one must demonstrate additional structure, such as a robust isolated response pole/resonance and dispersion, nonvanishing controlled operator residue, spatial behavior and effective dynamics. For a resonance rather than a real-axis atom, an arbitrarily narrow external filter still does not remove the underlying finite lifetime.

Conclusion: the proposed asymptotics are correct with the normalization and continuum assumptions stated. The constructive object is useful as a controlled counterexample to inferring a new mode from small spectral linewidth alone; it is not itself the missing cosmological scalar.
