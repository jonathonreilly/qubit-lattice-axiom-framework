"""M1 (1): exact two-body bound states on Z^d (d=1,2,3), contact attraction U<0.
Constituents: lattice KG band eps(k)=sqrt(m^2+sum_e 2(1-cos k_e)), m=1, so beta=1 in the IR.
Bound state at total lattice momentum Q: 1/U = G_Q(E) = <1/(E - eps(q) - eps(Q-q))>_q, E < E_th(Q).
Reports along lines in the zone: existence (isolated?), u=E_b^2/2, A(Q)=u''/beta-1, the composite IR beta_b,
the line average of u'' (sum rule), face concentration, rms size.
"""
import numpy as np
from scipy.optimize import brentq
np.set_printoptions(precision=5, suppress=True)
m = 1.0
MS = {}
def eps(k):  # k: (..., d)
    return np.sqrt(m*m + np.sum(2*(1-np.cos(k)), axis=-1))

def qgrid(d, n):
    g = (np.arange(n)+0.5)*2*np.pi/n - np.pi
    mesh = np.meshgrid(*([g]*d), indexing='ij')
    return np.stack([x.ravel() for x in mesh], axis=-1)

def bound(Q, U, qs):
    S = eps(qs) + eps(Q[None,:]-qs)
    Eth = S.min()
    f = lambda E: np.mean(1.0/(E - S)) - 1.0/U
    # f(E) -> 1/|U| >0 as E-> -inf ; near threshold f -> G(Eth^-) - 1/U ; bound exists iff G(Eth^-) < 1/U (both negative)
    lo = Eth - 50*abs(U) - 50
    hi = Eth - 1e-9
    if f(hi) > 0:   # no root below threshold (within grid resolution)
        return None, Eth, None
    E = brentq(f, lo, hi, xtol=1e-14, rtol=1e-15, maxiter=500)
    # relative wavefunction in q-space: psi(q) ~ 1/(E - S) ; rms size via momentum-space gradient is messy; use real-space FT in 1D only
    return E, Eth, S

def line_scan(d, U, nq, nQ, direction):
    qs = qgrid(d, nq)
    Qs = np.arange(nQ)*2*np.pi/nQ - np.pi
    dirv = np.array(direction, float)
    E = np.full(nQ, np.nan); Eth = np.zeros(nQ)
    for i, s in enumerate(Qs):
        Q = s*dirv
        e, th, _ = bound(Q, U, qs)
        Eth[i] = th
        if e is not None: E[i] = e
    return Qs, E, Eth

def analyse(tag, Qs, E, Eth, dn=1.0):
    n = len(Qs); h = Qs[1]-Qs[0]
    exists = ~np.isnan(E)
    out = []
    if exists.all():
        u = 0.5*E**2
        # spectral 2nd derivative (band is periodic & analytic when isolated)
        kk = np.fft.fftfreq(n, d=h)*2*np.pi
        upp = np.real(np.fft.ifft(-(kk**2)*np.fft.fft(u)))/dn
        upp_fd = (np.roll(u,-1)-2*u+np.roll(u,1))/h**2/dn
        i0 = np.argmin(abs(Qs)); iface = 0
        beta_b = upp[i0]
        A1 = upp/1.0 - 1          # anomaly against universal beta=1
        Ab = upp/beta_b - 1       # against composite's own IR beta
        # face concentration: width of region where Ab < -0.5
        width = h*np.sum(Ab < -0.5)
        out.append(f"{tag}: band isolated on whole line; E_b(0)={E[i0]:.6f} B(0)=Eth-E={Eth[i0]-E[i0]:.3e} "
                   f"E_b(face)={E[iface]:.5f} Eth(face)={Eth[iface]:.5f}")
        out.append(f"   beta_b=u''(0)={beta_b:.6f}  (universal beta=1: IR anomaly A(0)={A1[i0]:+.4e})")
        out.append(f"   line avg u'' (spectral)={upp.mean():+.2e}  (FD)={upp_fd.mean():+.2e}  => <A_b> = {Ab.mean():+.6f}, <A_1> = {A1.mean():+.6f}")
        out.append(f"   min A_b = {Ab.min():+.3f} at Q={Qs[np.argmin(Ab)]:+.3f};  width(A_b<-0.5) = {width:.3f};  A_b(Q=pi/2) = {Ab[np.argmin(abs(Qs-np.pi/2))]:+.4f}")
        # fraction of the total negative weight within |Q|>pi-0.5
        neg = np.where(Ab<0, Ab, 0)
        out.append(f"   share of sum(A_b<0) within 0.5 of face: {neg[abs(Qs)>np.pi-0.5].sum()/neg.sum():.3f}")
    else:
        frac = exists.mean()
        out.append(f"{tag}: bound band exists on {frac*100:.1f}% of the line (merges into continuum): Q-range with bound state:"
                   f" {Qs[exists].min() if exists.any() else None} .. {Qs[exists].max() if exists.any() else None}")
        if exists.any():
            i0 = np.argmin(abs(Qs)) 
            out.append(f"   E_b(0) exists? {exists[i0]}; Eth(0)={Eth[i0]:.4f}")
    return out

if __name__ == "__main__":
    print(__doc__)
    print("Only bands with E_b>0 everywhere are analysed for C3 (u=E^2/2 needs positive energy above the vacuum).")
    print("Diagonal lines Q=s(1,..,1): u'' is d^2u/ds^2 divided by d (= the Hessian component along the unit diagonal).")

    for mm, Us in [(1.0, [-0.2, -0.5, -1.0, -1.5]), (3.0, [-2.0, -4.0])]:
        m = mm
        for U in Us:
            Qs, E, Eth = line_scan(1, U, 4096, 256, [1.0])
            for l in analyse(f"d=1 m={m} U={U:+.1f}", Qs, E, Eth): print(l)
            qs = qgrid(1, 4096); S = eps(qs) + eps(-qs)
            E0 = E[np.argmin(abs(Qs))]
            psi = 1.0/(E0 - S); phi = np.fft.fftshift(np.abs(np.fft.ifft(np.fft.ifftshift(psi)))**2)
            r = np.arange(len(phi)) - len(phi)//2
            print(f"   rms relative size xi = {np.sqrt((phi*r**2).sum()/phi.sum()):.3f} sites")
    print()
    for d, nq, cases in [(2, 160, [(1.0, -1.0), (1.0, -1.5), (3.0, -4.0)]), (3, 64, [(1.0, -4.0), (3.0, -7.0), (1.0, -2.0)])]:
        for mm, U in cases:
            m = mm
            for dirn, name, dn in [([1.0]+[0.0]*(d-1), "x-line", 1.0), ([1.0]*d, "diag", float(d))]:
                Qs, E, Eth = line_scan(d, U, nq, 64, dirn)
                if np.nanmin(E) <= 0: print(f"d={d} m={m} U={U}: E_b<=0 somewhere, skipped"); continue
                if np.isnan(E).any():
                    ex = ~np.isnan(E)
                    print(f"d={d} m={m} U={U:+.1f} {name}: PARTIAL band: bound only for |s| >= {abs(Qs[ex]).min():.3f} (merges into the continuum near s=0;"
                          f" caveat: grid-threshold artefacts make the edge approximate)")
                    continue
                for l in analyse(f"d={d} m={m} U={U:+.1f} {name}", Qs, E, Eth, dn): print(l)
    # d=3 near-threshold check: does a weak attraction bind at Q=0 when the q-grid is refined? (grid always binds)
    m = 1.0
    print()
    print("d=3 critical-coupling check at Q=0 and Q=(pi,pi,pi): binding energy vs q-grid n (true bound state iff B converges >0)")
    for U in [-2.0, -4.0, -6.0]:
        for Q in [np.zeros(3), np.pi*np.ones(3)]:
            row = []
            for n in [24, 40, 64]:
                e, th, _ = bound(Q, U, qgrid(3, n))
                row.append(th - e if e is not None else float('nan'))
            print(f"   U={U:+.1f} Q={Q[0]:.2f}(1,1,1): B(n=24,40,64) = " + ", ".join(f"{b:.3e}" for b in row))
