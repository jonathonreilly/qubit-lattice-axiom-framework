"""C5 R18-8 (B): the anomaly identity for genuine lattice operators (not the Vlasov form).

One axis of a separable band on a ring of N sites (transverse axes contribute a constant u_perp to eps^2):
  eps(p) = sqrt(m^2 + u_perp + u(p)),  P(p) = u'(p)/2 (current-aligned),  X = diag(site - N/2),
  K = (X eps + eps X)/2   (lattice boost = energy moment).
Exact operator identities on the infinite lattice: [K,H] = i P,  [K,P] = i eps P' = i (H + Q_D),
  Q_D := eps (P' - 1)  (the defect charge of the axis).
On the ring they hold on states localised away from the seam, up to the band operators' tails at distance N/2.
Wave packets: Gaussian, width sigma sites, carrier k0 in the box (Q_D = 0 there) or in the edge.
"""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sublum_copy import SymS, SymG

M, N, SIG = 0.3, 2048, 24.0
S14, G14 = SymS(1.4), SymG(1.4)
LAWS = {  # u, u', u''
    "S(1.4)": (lambda k: S14.s(k)**2, lambda k: 2*S14.s(k)*S14.ds(k), lambda k: 2*(S14.ds(k)**2 + S14.s(k)*S14.d2s(k))),
    "G(1.4)": (G14.g, G14.dg, G14.d2g),
}
kn = 2*np.pi*np.fft.fftfreq(N)            # in [-pi, pi)
xs = np.arange(N) - N/2
def op(fk, psi):
    return np.fft.ifft(fk*np.fft.fft(psi))
lines = []
def pr(*a):
    s = " ".join(str(t) for t in a); print(s); lines.append(s)

pr("(B) ring N=%d, packet width %.0f sites, m=%.1f; <.> = expectation; residual = ||lhs psi - rhs psi||/||lhs psi||" % (N, SIG, M))
pr("law     u_perp  k0    <[K,P]>/i      <H>           <H+Q_D>        <Q_D>          res[K,P]=i(H+Q_D)  res[K,P]=iH   res[K,H]=iP")
for law, (u, up, upp) in LAWS.items():
    for uperp in (0.0, 0.5):
        for k0 in (0.5, 1.2, 1.6, 2.6, np.pi):
            eps = np.sqrt(M*M + uperp + u(kn)); P = 0.5*up(kn); dP = 0.5*upp(kn)
            psi = np.exp(-xs**2/(4*SIG**2) + 1j*k0*xs); psi /= np.linalg.norm(psi)
            Kpsi = lambda ph: 0.5*(xs*op(eps, ph) + op(eps, xs*ph))
            KP = Kpsi(op(P, psi)) - op(P, Kpsi(psi))
            KH = Kpsi(op(eps, psi)) - op(eps, Kpsi(psi))
            rhs = 1j*op(eps*dP, psi); rhs0 = 1j*op(eps, psi)
            ev = lambda v: np.vdot(psi, v)
            QD = ev(op(eps*(dP - 1), psi)).real
            r1 = np.linalg.norm(KP - rhs)/np.linalg.norm(KP)
            r0 = np.linalg.norm(KP - rhs0)/np.linalg.norm(KP)
            r2 = np.linalg.norm(KH - 1j*op(P, psi))/max(np.linalg.norm(KH), 1e-300)
            pr("%-7s %4.1f  %5.3f  %+.6e  %+.6e  %+.6e  %+.6e  %.1e            %.1e      %.1e" % (
                law, uperp, k0, (ev(KP)/1j).real, ev(op(eps, psi)).real, ev(rhs).imag, QD, r1, r0, r2))
open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w").write("\n".join(lines) + "\n")
