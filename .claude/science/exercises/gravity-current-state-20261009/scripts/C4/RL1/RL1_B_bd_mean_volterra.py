"""RL1 (B): exact finite-density MEAN of the realization inverse of the 4D Benincasa-Dowker (BD) operator, flat M^4, rho=1.
B = beta(-I + N), beta = 4 sqrt(rho)/sqrt6, N(x,y) = c[n(y,x)] for y<x, n = #elements strictly between, c = (1,-9,16,-8) for n=0..3.
B^{-1} = -beta^{-1}(I + H), H = sum_{k>=1} N^k.
EXACT (multivariate Mecke + disjointness of consecutive chain intervals + Poisson independence):
   E H(x,y) = Hbar(tau),  Hbar = f + rho f*Hbar,  f(tau) = E c[n] = e^{-m}(1 - 9m + 8m^2 - (4/3)m^3), m = rho pi tau^4/24.
Continuum target (Box = -dt^2 + lap):  rho B^{-1}(x,y) -> G_Box = -theta delta(tau^2)/(2 pi), i.e. -(sqrt6/4) Hbar -> -delta(tau^2)/(2pi)
   => W(T) = int_0^{T^2} Hbar dsigma -> (4/sqrt6)/(2pi) = 0.25990, and Hbar(tau) -> 0 for tau >> 1 (no tail, massless 4D).
Also the diagonal (shared-path) ladder of the second moment:  Lbar = f2 + rho f2*Lbar, f2 = E c[n]^2 = e^{-m}(1 + 81m + 128 m^2 + (32/3) m^3).
Also Johnston one-hop control: f = e^{-m} alone (then Hbar = f only if no recursion; here we solve the same Volterra with f=link to
show a link-only 'operator' would not be local).
"""
import numpy as np, sys, time
xg, wg = np.polynomial.legendre.leggauss(140)
SMAX = 16.0
S2 = 0.5*SMAX*(xg+1); WS2 = 0.5*SMAX*wg
xa, wa = np.polynomial.legendre.leggauss(48)
xb, wb = np.polynomial.legendre.leggauss(120)

def fc(s):
    m = np.pi*s**2/24; return np.exp(-m)*(1 - 9*m + 8*m**2 - (4/3)*m**3)
def fc2(s):
    m = np.pi*s**2/24; return np.exp(-m)*(1 + 81*m + 128*m**2 + (32/3)*m**3)

def conv_nodes(tau, F2):
    T1 = []; W = []
    for s2, ws, p in zip(S2, WS2, F2):
        top = tau - np.sqrt(s2)
        if top <= 0: continue
        c = min(4.0, top)
        pieces = [(0.5*c*(xa+1), 0.5*c*wa)]
        if top > c:
            v = 0.5*(xb+1); wv = 0.5*wb
            pieces.append((top-(top-c)*v**2, 2*(top-c)*v*wv))
        for t1, w1 in pieces:
            tt = (tau**2 + t1**2 - s2)/(2*tau)
            r = np.sqrt(np.maximum(tt*tt - t1*t1, 0))
            T1.append(t1); W.append(w1*(np.pi*r/tau)*2*t1*ws*p)
    if not T1: return np.zeros(0), np.zeros(0)
    return np.concatenate(T1), np.concatenate(W)

def solve(fun, taumax, h_fine, h):
    F2 = fun(S2)
    taus = np.unique(np.concatenate([np.arange(0, 6, h_fine), np.arange(6, taumax+h, h)]))
    K = np.zeros_like(taus)
    for i, tau in enumerate(taus):
        if tau == 0: K[i] = fun(np.array(0.0)); continue
        t1, w = conv_nodes(tau, F2)
        Kint = np.interp(t1, taus[:i], K[:i]) if i > 0 else 0*t1
        # implicit treatment of the newest point is not needed: t1 < tau strictly
        K[i] = fun(np.array(tau**2)) + np.sum(w*Kint)
    return taus, K

if __name__ == "__main__":
    t0 = time.time()
    for (hf, h) in [(0.04, 0.08), (0.02, 0.04)]:
        taus, H = solve(fc, 24.0, hf, h)
        sig = taus**2
        W = np.concatenate([[0], np.cumsum(0.5*(H[1:]+H[:-1])*np.diff(sig))])
        print(f"\n[BD mean inverse] grid h_fine={hf}, h={h}   (target W -> {4/np.sqrt(6)/(2*np.pi):.5f}, Hbar -> 0)")
        print("  tau   Hbar(tau)      W(tau)=int Hbar dsigma")
        for T in [0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24]:
            i = np.argmin(abs(taus-T)); print(f"  {taus[i]:5.2f} {H[i]: .5e}  {W[i]: .5f}")
        np.savez(f"RL1_B_Hbar_h{hf}.npz", taus=taus, H=H)
        sys.stdout.flush()
    taus, L = solve(fc2, 6.0, 0.02, 0.04)
    print("\n[diagonal ladder of E H^2: Lbar = f2 + f2*Lbar]  tau | Lbar | local e-fold rate d ln Lbar/dtau")
    lnL = np.log(np.abs(L)+1e-300); rate = np.gradient(lnL, taus)
    for T in [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]:
        i = np.argmin(abs(taus-T)); print(f"  {taus[i]:5.2f} {L[i]: .4e}  {rate[i]: .3f}")
    np.savez("RL1_B_Lbar.npz", taus=taus, L=L)
    print("elapsed %.1fs" % (time.time()-t0))
