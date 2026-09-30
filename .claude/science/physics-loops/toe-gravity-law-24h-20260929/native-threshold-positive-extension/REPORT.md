# Root extension candidate: strict positivity of the threshold form

Author extension, pending focused check. This is a short dependent consequence
for the SAME coherent native scattering route, not a separate PR or an
independent discovery family. It uses the full frozen threshold proof and its
independent check, both read completely by root, plus the actual spectator-pin
kernel argument in the native density source (reread at unchanged source hash).

The checked threshold construction proves existence of the compact-source
inverse G_H(0), finite row energy of each constant incoming profile Phi_z,
and T(z)=E(Phi_z)-<F_z,G_H(0)F_z> >=0, F_z=H Phi_z. It only states
semidefiniteness. The following argument appears to strengthen it to strict
positivity for every nonzero constant incoming vector z in Sym^2 C^5.

Assume T(z)=0. Let u_epsilon=-(H+epsilon)^-1 F_z and
psi_epsilon=Phi_z+u_epsilon. Its full SOS energy is

 E(psi_epsilon)=E(Phi_z)-<F_z,(H+epsilon)^-1 F_z>
                           -epsilon||(H+epsilon)^-1 F_z||^2.

The finite inverse form makes the last term tend to zero by dominated spectral
integration. Thus this nonnegative sum of the literal local row norms tends
to zero. The checked compact-source Green construction gives a pointwise
limit psi0=Phi_z-G_H(0)F_z, harmonic under H and with a decaying correction
in the separated-pair exterior. Every fixed finite row therefore annihilates
psi0. No l2 limiting correction is assumed.

For any fixed residual occupation pair eta, W rows make every Q_A(x) amplitude
on eta constant in x. The axial singlet row makes d1+d2+d3 zero, so every
bare axial amplitude is constant. Plane-complement rows equate the four signed
plane amplitudes and their collective sum is constant, so each bare plane
amplitude is constant too. These are exactly the actual local transformations
used in the finite-torus kernel proof and remain pointwise identities on Z^3.

Pick an occupied y in eta. For a given bare annihilator with offsets u,v,
choose center x=y-u. Its output amplitude on eta is zero: the annihilator
cannot leave occupation at its own endpoint. Constancy then makes that
amplitude zero at every x, for every eta and every bare pair. Thus every
Q_A(x) kills psi0. The original H expression and H psi0=0 give
(4mu+V3(S))psi0(S)=0 pointwise. Positive mu forces psi0=0.

But a nonzero constant incoming z has a nonzero separated-bond amplitude:
the normalized five internal vectors are linearly independent and their
symmetric tensor products form the actual15-dimensional constant channel
space. Deleting the finite collision hole cannot remove such a constant
profile. Along a separation sequence that amplitude stays nonzero, while
the Green correction tends to zero. Hence psi0 cannot vanish identically.
This contradiction would prove T(z)>0 for every z!=0. The finite Hermitian
15-by-15 form would consequently have a positive smallest eigenvalue at each
fixed mu,tau>0, without a numerical lower bound or a uniform coupling limit.

This does not evaluate T, give a phase, identify a flux-normalized scattering
matrix or prove a dilute-gas asymptotic. It uses3D threshold inverse existence;
the pin argument alone would not establish positivity of an infimum when
finite-energy Green response failed. Preserve this as a candidate until the
pointwise row-energy limit, incoming normalization and exact spectator pin
extension have received a focused check.
