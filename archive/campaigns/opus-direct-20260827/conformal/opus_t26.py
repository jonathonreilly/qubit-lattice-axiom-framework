"""T26 - DOES MATTER SOURCE THE METRIC?  The rule's own effective action.
The master identity (R16) says the rule's determinant is the metric's length
form.  The standard object that turns that into a FIELD EQUATION is the
effective action W[g] = log |det Q[g]| : stationarity of W in g is the induced
(Sakharov) gravitational equation.  R4 killed the naive guess (fibre-scalarity
of K^2); this is the principled route instead.

Probe: put a CONFORMAL BUMP in the metric,  g_s = (1 + h f_s) * delta,  localised
at a site z_g, and a MASS DEFECT  m_s = m0 + delta * [s = z_m]  (the matter).
Compute  dW/dh at h=0  =  tr( Q0^-1 dK/dh ).
  * uniform matter (delta = 0)  -> must vanish, by the lattice's own symmetry.
  * with a defect (delta != 0)  -> if it is NONZERO and tracks delta, then the
    stationarity condition of the rule's action ties the metric to the matter:
    matter sources geometry.  That is the seed of an Einstein equation.
Also scan the separation |z_g - z_m| to see whether the response falls off."""
import numpy as np, itertools
np.set_printoptions(precision=6, suppress=True)
D = 2
BAS = [(), (0,), (1,), (0,1)]; IDX = {b:i for i,b in enumerate(BAS)}; NF = 4
def epsm(a):
    M = np.zeros((NF,NF))
    for Sx in BAS:
        if a in Sx: continue
        T = tuple(sorted(Sx+(a,))); M[IDX[T], IDX[Sx]] = (-1)**sum(1 for i in Sx if i<a)
    return M
def iota(a, gi):
    M = np.zeros((NF,NF))
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T = tuple(x for x in Sx if x != i); M[IDX[T], IDX[Sx]] += (-1)**pos*gi[a,i]
    return M
EPS = [epsm(a) for a in range(D)]
IOT_FLAT = [iota(a, np.eye(D)) for a in range(D)]        # flat g^-1 = I
GAM_FLAT = [EPS[a] + IOT_FLAT[a] for a in range(D)]
# d(g^-1)/dh at h=0 for g = (1 + h f) I  is  -f I, so dGamma_a/dh = -f * iota_a(I)
def build(L, m_site, prof, h):
    """Q with conformal metric bump amplitude h and profile prof(site)."""
    sites = [(t,x) for t in range(L) for x in range(L)]
    sid = {s:i for i,s in enumerate(sites)}; N=len(sites)
    Q = np.zeros((NF*N, NF*N))
    for s in sites:
        Q[sid[s]*NF:(sid[s]+1)*NF, sid[s]*NF:(sid[s]+1)*NF] += m_site[s]*np.eye(NF)
    def gam(s, a):
        gi = np.eye(D)/(1.0 + h*prof[s])
        return EPS[a] + iota(a, gi)
    for s in sites:
        for a in range(D):
            for sgn, r in ((+1, ((s[0]+(a==0))%L, (s[1]+(a==1))%L)),
                           (-1, ((s[0]-(a==0))%L, (s[1]-(a==1))%L))):
                blk = 0.5*sgn*0.5*(gam(s,a)+gam(r,a))
                Q[sid[s]*NF:(sid[s]+1)*NF, sid[r]*NF:(sid[r]+1)*NF] += blk
    return Q, sid, sites
def dWdh(L, m0, delta, z_m, z_g, sigma=0.0):
    sites = [(t,x) for t in range(L) for x in range(L)]
    prof = {}
    for s in sites:
        if sigma == 0.0: prof[s] = 1.0 if s == z_g else 0.0
        else:
            dt = min((s[0]-z_g[0])%L, (z_g[0]-s[0])%L); dx = min((s[1]-z_g[1])%L, (z_g[1]-s[1])%L)
            prof[s] = float(np.exp(-(dt*dt+dx*dx)/(2*sigma*sigma)))
    m_site = {s: m0 + (delta if s == z_m else 0.0) for s in sites}
    Q0, sid, _ = build(L, m_site, prof, 0.0)
    # analytic dQ/dh : dGamma_a(s)/dh = -prof[s] * iota_a(I)
    dQ = np.zeros_like(Q0)
    for s in sites:
        for a in range(D):
            for sgn, r in ((+1, ((s[0]+(a==0))%L, (s[1]+(a==1))%L)),
                           (-1, ((s[0]-(a==0))%L, (s[1]-(a==1))%L))):
                blk = 0.5*sgn*0.5*(-(prof[s])*IOT_FLAT[a] - (prof[r])*IOT_FLAT[a])
                dQ[sid[s]*NF:(sid[s]+1)*NF, sid[r]*NF:(sid[r]+1)*NF] += blk
    Qi = np.linalg.inv(Q0)
    analytic = float(np.trace(Qi @ dQ))
    # independent route: central finite difference of log|det Q|
    def W(hh):
        Q,_,_ = build(L, m_site, prof, hh)
        return np.linalg.slogdet(Q)[1]
    e = 1e-5
    fd = (W(e)-W(-e))/(2*e)
    return analytic, fd
L, m0 = 6, 0.8
zc = (3,3)
print("T26  L=6  m0=0.8   dW/dh at h=0   [analytic tr(Q^-1 dQ/dh)  vs  finite-difference of log|det Q|]")
print()
print("A. UNIFORM matter (delta = 0) - the lattice symmetry should make this vanish")
a0, f0 = dWdh(L, m0, 0.0, zc, zc)
print(f"   delta=0.0 : analytic={a0:+.10e}   fd={f0:+.10e}   agree={abs(a0-f0)<1e-6}")
print()
print("B. MASS DEFECT at the SAME site as the metric bump")
for delta in (0.05, 0.1, 0.2, 0.4):
    a1, f1 = dWdh(L, m0, delta, zc, zc)
    print(f"   delta={delta:<5} : analytic={a1:+.10e}  fd={f1:+.10e}  "
          f"agree={abs(a1-f1)<1e-5}   (response-a0)={a1-a0:+.6e}  ratio/delta={(a1-a0)/delta:+.6f}")
print()
print("C. SEPARATION SCAN - does the response fall off with distance?  (delta=0.2)")
for dx in range(0, 4):
    zm = (3, (3+dx) % L)
    a1, _ = dWdh(L, m0, 0.2, zm, zc)
    print(f"   |z_m - z_g| = {dx} : dW/dh = {a1:+.10e}   response = {a1-a0:+.6e}")
print()
print("D. SMOOTH (Gaussian sigma=1.2) metric profile, defect at centre, delta scan")
a0s, _ = dWdh(L, m0, 0.0, zc, zc, sigma=1.2)
for delta in (0.0, 0.1, 0.3):
    a1, _ = dWdh(L, m0, delta, zc, zc, sigma=1.2)
    print(f"   delta={delta:<5} : dW/dh={a1:+.10e}   response={a1-a0s:+.6e}")
