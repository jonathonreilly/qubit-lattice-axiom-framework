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
