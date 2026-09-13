# Load-bearing correction: the native two-node carrier has a Hall term

Author discovery at approximately 20:26UTC, after the initial Maxwell-only
coefficient checkpoint. Earlier coefficient calculations remain valid for the
specified Hall-subtracted quadratic gauge model, or its applicable intermediate
window. They are NOT the full asymptotic native gauge dynamics. Do not publish
the early wording without this correction.

The selected h0(k)=(sin k1,sin k2,2+zeta-cos k1-cos k2-cos k3).sigma,
zeta in (1/2,1), is a stack of two-dimensional Wilson Chern insulators with
M(k3)=2+zeta-cos k3. At k3=+-kappa, kappa=acos(zeta), the slices close.
For |k3|<kappa, 0<M<2; elsewhere M>2. The occupied-band Chern index is
one in the former interval and zero outside, with the explicit convention
C=(1/(2pi i)) int tr(P[partial1 P,partial2 P]). The sign reverses under
orientation convention, but the nonzero magnitude does not.

The lower-band map has masses M-2,M,M,M+2 at the four sine zeros, with
orientation signs +,-,-,+. Hence C=-1/2 sum orientation*sign(mass), giving
C=1 inside and C=0 outside. A second proof counts preimages of a regular
pole of d/|d|; a numerical link-variable Chern calculation will challenge it.

For filled negative bands, zero chemical potential and temperature, adiabatic
linear response, the Hall coefficient has magnitude
sigmaH=e^2 int(dq3/2pi) C(q3)/(2pi)
      =e^2 kappa v/(2pi^2 a), v=sqrt(1-zeta^2),
in the normalized cell coordinates y3=a n3/v. The speed multiplier r does
not change eigenvectors or this leading free-band Hall coefficient.
The Hall/Chern-Simons-like quadratic response has one derivative, unlike
the two-derivative Maxwell kernel. It is allowed by the actual lattice
symmetries; a parity-even electric/magnetic constitutive ansatz alone does
not remove it. The carrier preserves inversion but breaks time reversal.

With canonical isotropic Maxwell coefficients and constant H=sigmaH,
the physical photon polynomial is
(omega^2-|k|^2)^2-H^2(omega^2-k_perp^2)=0.
Thus omega_+-^2=|k|^2+H^2/2 +-sqrt(H^4/4+H^2 k3^2).
Along the node-separation axis, the positive frequencies are
(sqrt(H^2+4k3^2)+-abs(H))/2. One mode is gapped and the other obeys
omega_-=k3^2/abs(H)+O(k3^4), rather than two common linear cones.
This is the leading weak-coupling quadratic-response consequence, not a
claim about the full interacting phase or lifetime. Positive anisotropic
Maxwell corrections do not remove the leading one-derivative term.

A constant integer-Chern fully gapped band stack shifts the Hall vector by
an integer reciprocal-lattice unit. In this fixed two-node family the
fractional slice average kappa/pi lies strictly between zero and 1/3, so
such additions alone cannot cancel it while preserving node positions.
Additional gapless charged sectors, opposite Hall copies, translation
breaking, node merger, or a supplied bare noncompact counterterm are live
escapes. These are model changes or further derivations, not an axiom update.

The one-loop Maxwell charge flow would give H(L)=H0/z while momentum
falls as mu0 exp(-L); hence H/mu=(H0/mu0) exp(L)/z grows. If H0/mu0 is
of order e0^2 at fixed geometry, crossover occurs after O(log(1/e0^2))
logarithmic running, before z differs from one by more than
O(e0^2 log(1/e0^2)). This is a formal small-coupling crossover statement:
it prevents using the Hall-free z^-3 law to assert the asymptotic native
common cone. It does not establish the subsequent full Hall-regime RG.

Primary literature consulted AFTER noticing the omission:
Ying/Burkov/Wang, Phys.Rev.B107,035131 (2023), accepted manuscript
https://link.aps.org/accepted/10.1103/PhysRevB.107.035131 . Introduction and
sectionII read in full (through their line370); sectionIII beginning through
line441 read, remainder not yet read. Their Hall-modified photon and IR
regime are comparators, not a substitute for our actual h0 Chern derivation.
Vazifeh/Franz1303.5784 and Goswami/Tewari1210.6352 opened but not yet read.
No existing docs matched the initial combined Weyl/Hall query; broader
Hall/Chern-Simons search returned119 files requiring targeted scope review.
