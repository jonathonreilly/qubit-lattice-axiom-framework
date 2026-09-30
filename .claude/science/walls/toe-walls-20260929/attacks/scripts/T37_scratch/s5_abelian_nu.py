"""S5: abelian / electroweak-charge laws for the sector dial, tested on the neutrino band."""
from common import *
g = load_runner(); PARS, _RG = g["PARS"], g["_RG"]
r_e, r_d, r_u = 0.5, 0.62109, 0.83097
# neutrino band (Dirac-type sqrt(m) dictionary, band only)
d21, d31_no, d32_io = 7.42e-5, 2.515e-3, 2.498e-3
m0 = np.concatenate([[0.0], np.logspace(-6, np.log10(0.3), 4000)])
def rnu_NO(m1):
    m = np.sqrt(np.array([m1**2, m1**2+d21, m1**2+d31_no])); return rf(m)
def rnu_IO(m3):
    m = np.sqrt(np.array([m3**2, m3**2+d32_io, m3**2+d32_io+d21])); return rf(m)   # masses (m3, m1, m2)
NO = np.array([rnu_NO(x) for x in m0]); IO = np.array([rnu_IO(x) for x in m0])
print("neutrino r band (lightest mass 0..0.3 eV): NO in [%.4f, %.4f], IO in [%.4f, %.4f]" % (NO.min(), NO.max(), IO.min(), IO.max()))
print("   cosmological sum < 0.12 eV corner: NO r at m1 for sum=0.12:", end=" ")
from scipy.optimize import brentq
f = lambda m1: np.sqrt(m1**2)+np.sqrt(m1**2+d21)+np.sqrt(m1**2+d31_no)-0.12
m1c = brentq(f, 0.0, 0.1); print("m1=%.4f eV, r=%.4f" % (m1c, rnu_NO(m1c)))
rmax = max(NO.max(), IO.max())
# (a) linear law in (T3, Y) of the left-handed field, fitted to e, d, u
fields = {"nu": (0.5, -0.5, 0.0), "e": (-0.5, -0.5, -1.0), "u": (0.5, 1/6, 2/3), "d": (-0.5, 1/6, -1/3)}
A = np.array([[1, fields[s][0], fields[s][1]] for s in ("e","d","u")]); y = np.array([r_e, r_d, r_u])
coef = np.linalg.solve(A, y)
pred_nu = coef @ np.array([1, fields["nu"][0], fields["nu"][1]])
print("(T3,Y)-linear law fitted exactly to (e,d,u): r0=%.4f alpha=%.4f beta=%.4f -> predicted r_nu = %.4f ; achievable band max %.4f -> miss by %.3f" % (coef[0], coef[1], coef[2], pred_nu, rmax, pred_nu - rmax))
# (b) linear law in Q: 2 parameters from (e, d), predict u and nu
kappa = (r_d - r_e)/((-1/3) - (-1.0)); r0 = r_e - kappa*(-1.0)
print("Q-linear law from (e,d): kappa=%.4f r0=%.4f -> r_u pred %.4f (data %.4f, miss %+.3f) ; r_nu pred %.4f (band max %.4f)" % (kappa, r0, r0+kappa*2/3, r_u, r0+kappa*2/3-r_u, r0, rmax))
# least-squares over (e,d,u) for Q-linear
Aq = np.array([[1, q] for q in (-1.0, -1/3, 2/3)]); cq = np.linalg.lstsq(Aq, y, rcond=None)[0]
print("   least squares Q-linear over (e,d,u): r = %.4f + %.4f Q ; residuals %s ; nu pred %.4f" % (cq[0], cq[1], np.round(Aq@cq-y, 4), cq[0]))
# (c) C-even rules f(Q^2): ordering by |Q|
order = sorted([("d", 1/3, r_d), ("u", 2/3, r_u), ("e", 1.0, r_e), ("nu", 0.0, None)], key=lambda t: t[1])
print("(c) ordering by |Q|: ", [(n, round(q,3), None if r is None else round(r,3)) for n, q, r in order])
print("    r along increasing |Q| (d,u,e) = (%.3f, %.3f, %.3f) -> not monotone (rises then falls); a cubic in Q^2 passes any 4 points => no test" % (r_d, r_u, r_e))
# (d) Debye-Waller-type abelian suppression r = r0 exp(-Q^2 s2) (the abelian analogue of the character cap, |<e^{iQphi}>|^2, Gaussian phase)
s2 = np.log(r_e/r_d)/(-(1.0) + (1/9))   # solve r_e = r0 e^{-s2}, r_d = r0 e^{-s2/9}
r0 = r_d*np.exp(s2/9)
print("(d) Gaussian holonomy suppression r0 exp(-Q^2 s): from (e,d): s=%.4f r0=%.4f -> r_u pred %.4f (data %.4f) r_nu pred %.4f (=r0, the LARGEST)" % (s2, r0, r0*np.exp(-s2*4/9), r_u, r0))
