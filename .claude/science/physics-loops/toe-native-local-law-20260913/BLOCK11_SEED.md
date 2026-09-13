# Constructive next mechanism: stable Hall-free charged quartet with mixing

Provisional derivation seed, not yet checked. Preserve while completing block10.
Target is stronger than simply duplicating and declaring independent species:
allow a native onsite flavor-mixing term, keep four separated simple Weyl nodes,
and make Hall cancellation a time-reversal consequence. Then derive their
actual cone metrics and test whether the gauge flow closes their differences.

Take 0<b<pi/2 and the same 1/2<zeta<1. Define a four-orbital symbol
H(k)=diag(h0(k-b xhat), h0^*(-k-b xhat))+m tau_x sigma1.
The blocks are related by T=tau_x K, T^2=1; the onsite mixing is T-even.
The symbol is even in k3, so a z-reflection pairs opposite chirality nodes
at equal energy. No flavor-number conservation is assumed when m!=0.
The negative-energy two bands require background charge -2 per cell.
Both T and z-reflection are model symmetries, not new framework axioms.

Write H=sin(ky) sigma2 + A sigma1+B sigma3, with real flavor matrices
A=a I+b1 tau_z+m tau_x, B=c I+d tau_z,
a=-cos(kx) sin(b), b1=sin(kx) cos(b),
c=2+zeta-cos(kx) cos(b)-cos(ky)-cos(kz), d=-sin(kx) sin(b).
At fixed k an antiunitary sigma2 K anticommutes with H, giving +/- energies
for this family. At ky=0 or pi, det H=|det(B+i A)|^2.
At ky=0 put t=cos(kx), s=sin(kx), R=sqrt(1-m^2).
The imaginary part of det(B+iA)=0 gives c t=s^2 cos(b).
The real part then gives t^2=cos(b)^2/(1-m^2).
For the positive-c branch relevant to the nodes,

 cos(kx*)=cos(b)/R,
 cos(kz*)=1+zeta-R,
 ky*=0.

Thus there should be exactly four nodes (+-kx*,0,+-kz*) whenever
m^2<min(sin(b)^2,1-zeta^2). At ky=pi the analogous c+cos(b)t is at least
2+zeta and cannot equal R<=1, excluding extra zeros. The negative t branch
would require negative c, incompatible with its definition. kx=pi/2 is
excluded by the imaginary equation when sin(b)cos(b)>0.
Need fully check all roots, gap multiplicity and node derivative ranks.

For H^2, the three remaining flavor matrices anticommute:
H^2=S I+2(a b1+c d) tau_z+2 a m tau_x-2 d m sigma2 tau_y,
S=sin(ky)^2+a^2+b1^2+m^2+c^2+d^2.
So E_+-^2=S+-2sqrt((a b1+c d)^2+m^2(a^2+d^2)).
This needs matrix and spectral verification.

At a node, let q=det(B+i A). Its derivatives at ky=0 are
q_x=2 sin(kx*) R exp(i b),
q_z=2(c-i cos(kx*) sin(b)) sin(kz*).
Thus Re(q_x^* q_z)=-4 sin(kx*) cos(b) m^2 sin(kz*).
The low-energy metric from E_-^2 is Re(q_i^*q_j)/E_+^2 in the x-z plane,
with the y coefficient one. Cross xz is generally nonzero and changes sign
between opposite-reflection nodes. Hence Hall cancellation may not make all
four matter cone metrics equal at nonzero mixing. This is a useful concrete
second discriminator, not a reason to assume equality.

Time reversal sends Berry curvature to its negative at -k and preserves the
occupation, so the integrated Hall vector cancels in the full four-band model,
including mixing. Need projector/Kubo checks and continuity/topological proof
for the four Weyl charges. Small generic T and z-reflection preserving
perturbations should preserve separated topological nodes and common node
energy (the four nodes form a symmetry orbit); need examine forbidden tilt,
extra Fermi pockets and charge neutrality carefully, not assert full stability
from node count alone.

For four equal-charge Weyl fields (N=2 Dirac count) with possibly different
metrics, each fermion's self-energy metric coefficient should remain e^2/(3pi^2).
Photon coframe moves at N e^2/(6pi^2)(mean Cf-Cg); charge runs with N.
Then z=1+N e0^2 L/(6pi^2), mean-relative metric decays as z^(-(N+2)/N),
individual contrasts as z^(-2/N), and W as z^-1. For N=2 these are powers
2,1,1. This is only a proposed extension until re-derived with Weyl traces
and the actual quartet vertices. Native dynamical gauge phase, finite
matching, all-orders bounds and the physical multiplet remain open.

## Further analytic simplification and first challenge

At the nodes S=2 sin(b)^2, so the nonzero spectator energies are exactly
+-2 sin(b), independent of m and zeta within the stated node domain.
The low-energy metric has Gyy=1 and
Gxx=1-m^2/sin(b)^2,
Gzz=sin(kz*)^2 [sin(b)^2(1-2m^2)+m^4]/[(1-m^2)sin(b)^2],
Gxz=-sin(kx*) cos(b) m^2 sin(kz*)/sin(b)^2.
Its x-z determinant is
(1-m^2/sin(b)^2)(1-m^2) sin(kz*)^2>0.
Thus all four nodes are simple in the interior, with chirality
sign(kx* kz*), by continuation from m=0 and nonzero determinant.
The factor r/a and any chosen cell-coordinate D transform this metric
explicitly; do not identify the raw k metric with a unit physical cone.

The first independent projector calculation at b=.4,zeta=.7,m=.2 agrees
with this determinant-derived metric to1.5e-15. The metric cross term is
+-0.0574795630084294 and does not vanish. The direct spectra agree with the
H^2 formula to3.6e-15, while full occupied/empty four-band Kubo curvature
cancels at opposite momenta to4e-16. These are preliminary numerical
challenges, not the proof of the whole open parameter range.

A possible minimum-content argument must be scoped to spinless T^2=+1,
only simple isolated Weyl nodes at a common Fermi level, and a regular
occupied bundle elsewhere. Time reversal pairs non-TRIM nodes of the same
chirality; the total Weyl charge on the Brillouin torus vanishes by Stokes.
A simple twofold Weyl node at a TRIM is excluded when T^2=+1: choose T=K in
its two-dimensional subspace, and the linear Hamiltonian must be purely
imaginary Hermitian, leaving only sigma2 and rank at most one. Hence there
must be at least two time-reversal pairs, i.e. four simple nodes in this
restricted domain. Do NOT extend this to T^2=-1 Kramers-Weyl nodes, higher
multiplicities, extra Fermi surfaces, interacting topological order or
non-band settings. The explicit family attains the scoped minimum.

## Local stability target beyond the displayed family

For fixed parameters strictly inside the node domain, permit finite-range
translation-invariant number-preserving Hermitian four-band perturbations
small in C2 norm, preserving T=tau_x K and Mz:kz->-kz. The four isolated
nodes are a single orbit of these symmetries. Their common energy can shift;
tune the chemical potential to that common energy, rather than assuming
particle-hole symmetry of every perturbation.

A two-band spectral subspace is smoothly separated from the spectator pair
near each original node (gap2sin b). Write its exact reduced Hamiltonian as
d0(k)I+d(k).sigma. Since the unperturbed d derivative is invertible, the
implicit-function theorem and small C1 bounds give one surviving simple
node per disjoint neighborhood. Symmetry maps these four nodes into each
other and forces their energies equal. The tilt is small relative to the
nonzero minimum cone speed, so the nodes remain type I and no local Fermi
pockets arise at the common chemical potential. A compact gap away from the
four neighborhoods excludes other Fermi surfaces for small C0 perturbations.
This needs explicit estimates/lemma structure, not a blanket claim that
any time-reversal-symmetric perturbation preserves the phase.

Time reversal makes the occupied-projector curvature odd at opposite
momenta, so the full free-band Hall vector vanishes. T and Mz together also
make every gapped constant-kz slice have zero total occupied Chern number:
T makes C(kz)=-C(-kz), while Mz makes C(kz)=C(-kz). Local individual Weyl
charges can still be nonzero, because opposite charges lie at distinct kx
on the same node plane. This cancellation does not gap the nodes.

An unbroken time-reversal-invariant coupled state and regulator forbid a
local zero-field Hall term in its effective action. This symmetry statement
does not prove that the interacting native gauge phase exists or preserves T;
spontaneous breaking and higher-derivative optical activity remain possible.
