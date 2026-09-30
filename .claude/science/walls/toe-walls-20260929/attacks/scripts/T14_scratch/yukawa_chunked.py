"""Chunked (low-memory) version of yukawa_euclid_gap.run; identical formulas."""
import numpy as np
def run_chunked(Nt, Ns, eps, m, mu, c_psi=1.0, lam=1.0, chunk=16):
    tt = 2*np.pi*np.arange(Nt)/Nt
    ts = 2*np.pi*np.arange(Ns)/Ns
    sp = np.sin(ts); cp = np.cos(ts); hs = 4*np.sin(ts/2)**2
    S1 = sp[None,:,None,None]; S2 = sp[None,None,:,None]; S3 = sp[None,None,None,:]
    C1 = cp[None,:,None,None]
    Hs = hs[None,:,None,None]+hs[None,None,:,None]+hs[None,None,None,:]
    ssp = S1**2+S2**2+S3**2
    meas = 1.0/(eps*Nt*Ns**3)
    acc = dict(ft=0.0, fx=0.0, tt=0.0, ts=0.0)
    for a in range(0, Nt, chunk):
        th = tt[a:a+chunk]
        s0 = (c_psi*np.sin(th)/eps)[:,None,None,None]
        s01 = (c_psi*np.cos(th))[:,None,None,None]
        s02 = (-c_psi*eps*np.sin(th))[:,None,None,None]
        h0 = (lam*4*np.sin(th/2)**2/eps**2)[:,None,None,None]
        den = m**2 + s0**2 + ssp
        D = 1.0/(mu**2 + h0 + Hs)
        acc['ft'] += np.sum(D*s01*(1/den - 2*s0**2/den**2))
        acc['fx'] += np.sum(D*C1*(1/den - 2*S1**2/den**2))
        Nk = m**2 - (s0**2 + ssp)
        def tcoef(s, s1, s2):
            Np = -s*s1; Npp = -s*s2; dp = 2*s*s1; dpp = 2*s1**2+2*s*s2
            second = Npp/den - 2*Np*dp/den**2 - Nk*dpp/den**2 + 2*Nk*dp**2/den**3
            return np.sum(second/den)
        acc['tt'] += tcoef(s0, s01, s02)
        acc['ts'] += tcoef(S1, C1, -S1)
    ft = meas*acc['ft']; fx = meas*acc['fx']
    tt_ = 0.5*4*meas*acc['tt']; ts_ = 0.5*4*meas*acc['ts']
    a_psi = fx - ft/c_psi
    a_phi = 0.5*(ts_ - tt_/lam)
    return dict(ft=ft, fx=fx, tt=tt_, ts=ts_, a_psi=a_psi, a_phi=a_phi, gap=a_psi-a_phi)
if __name__=="__main__":
    from yukawa_euclid_gap import run
    print(run(40,24,0.6,0.5,0.4,1.1,0.9)); print(run_chunked(40,24,0.6,0.5,0.4,1.1,0.9))
