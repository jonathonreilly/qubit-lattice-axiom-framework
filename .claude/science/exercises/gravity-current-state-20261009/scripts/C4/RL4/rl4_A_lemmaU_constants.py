"""RL4 A: explicit constants for Lemma U' (multiplicative per-insertion comparison on the window/rapidity set)
and the resulting rigorous rate constant c_low = (1-2 delta) sqrt(pi I_W (1-err)).

Conventions (RL1/RL2/RL3): units l_k = 1, rho*eps = 1, f(m) = e^{-m} sum_n C_n m^n/n!, m = pi tau^4/24.
Everything below uses h only on [0, tau2] (window diamonds), where h is bounded RIGOROUSLY by the Neumann/chain-volume
estimate |h(tau) - f(tau)| <= F (e^{F V(tau)} - 1), F = sup_{[0,tau]}|f|, V = pi tau^4/24.  No Volterra numerics are used
in any bound (they are printed only as a sanity comparison).
"""
import numpy as np, os, sys
from math import factorial, log, exp, sqrt, pi
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rl2_core as rc

RL3 = os.path.join(os.path.dirname(HERE), "RL3")
SQ = sqrt(pi/24)

def fder(C, g, m):
    """g-th m-derivative of f(m) = e^{-m} sum C_n m^n/n!  ->  e^{-m} sum (Delta^g C)_n m^n/n!, Delta C_n = C_{n+1}-C_n."""
    c = np.concatenate([np.asarray(C, float), np.zeros(g+2)])
    for _ in range(g):
        c = c[1:] - c[:-1]    # (Delta c)_n = c_{n+1} - c_n  (sign convention: d/dm e^{-m} m^n/n! terms)
    m = np.asarray(m, float)
    return np.exp(-m)*sum(c[n]*m**n/factorial(n) for n in range(len(c)))

def check_fder(C):
    m = np.linspace(0.01, 5, 7); e = 1e-5
    num = (fder(C, 0, m+e) - fder(C, 0, m-e))/(2*e)
    num2 = (fder(C, 0, m+e) - 2*fder(C, 0, m) + fder(C, 0, m-e))/e**2
    return np.max(np.abs(num - fder(C, 1, m))), np.max(np.abs(num2 - fder(C, 2, m)))

def tail_sup(vals):
    """running sup from the right: Phi(m_i) = max_{j>=i} vals_j"""
    return np.maximum.accumulate(vals[::-1])[::-1]

def analyse(k, C, tau1, tau2, verbose=True):
    out = {}
    # ---- f on [0, tau2]: monotone? sup|f|, rigorous h band
    tg = np.linspace(0, tau2, 20001); mg = pi*tg**4/24
    fg = fder(C, 0, mg)
    F = np.max(np.abs(fg))                     # sup_{[0,tau2]}|f| (grid; f is a smooth polynomial*exp, grid 3e-5)
    mono = np.all(np.diff(fg) <= 1e-15)
    Dh = F*(np.exp(F*pi*tg**4/24) - 1)          # |h - f| <= Dh(tau)   (rigorous, chain-volume bound)
    h_inf = F + Dh[-1]                          # sup_{[0,tau2]} |h|
    inW = tg >= tau1
    hlow = fg - Dh                               # h >= f - Dh
    h0 = np.min(hlow[inW])                       # inf_W h  (needs > 0)
    # rigorous lower bound on I_W = int_W tau h^2
    IW_low = np.trapezoid((tg*np.clip(hlow, 0, None)**2)[inW], tg[inW])
    # Volterra comparison (sanity only)
    d = np.load(os.path.join(RL3, "rl3_H_op%d.npz" % k)); tV, HV = d["taus"], d["H"]
    sel = tV <= tau2 + 1e-12
    hf = np.interp(tV[sel], tg, fg)
    vol_dev = np.max(np.abs(HV[sel] - hf)); vol_band = np.interp(tV[sel], tg, Dh)
    viol = np.any(np.abs(HV[sel] - hf) > vol_band + 1e-3)
    IW_vol = np.trapezoid((tV*HV**2)[(tV >= tau1) & sel], tV[(tV >= tau1) & sel])
    # ---- hop envelopes
    mm = np.concatenate([np.linspace(0, 50, 200001), np.linspace(50.0005, 2000, 40000)])
    Phi1 = tail_sup(np.abs(fder(C, 1, mm)))     # Phi_1(m) = sup_{m'>=m} |f'(m')|
    Phi2 = tail_sup(np.abs(fder(C, 2, mm)))
    psi0 = Phi1[0]
    x = np.linspace(0, np.sqrt(2000), 400001)
    psi = np.interp(x**2, mm, Phi1)              # psi(x) = Phi_1(x^2)
    Psi1 = np.trapezoid(psi, x)
    # g=2 block: psi2(x) = Phi_2(pi x^2/24); S2 = int sqrt(psi2)
    psi2 = np.interp(pi*x**2/24, mm, Phi2)
    xs2 = x[pi*x**2/24 <= 2000]
    S2 = np.trapezoid(np.sqrt(np.interp(pi*xs2**2/24, mm, Phi2)), xs2)
    # grid-sup safety: Phi from a grid of spacing 2.5e-4 in m; |f''| bounded -> sup error <= 2.5e-4*sup|f''|
    gridpad1 = 2.5e-4*np.max(np.abs(fder(C, 2, mm[:200001])))
    Psi1 += gridpad1*np.sqrt(50)   # pad Phi_1 by gridpad1 on m<=50 (x<=sqrt 50)
    psi0 += gridpad1
    # weights
    e_w = h_inf*(pi/2)*tau2**2                   # end leg, integrated end
    om = pi/2 + h_inf*(pi**2/4)*tau2**4          # inner leg (delta + h)
    omx = max(1.0, om)
    maxC = np.max(np.abs(C))
    def per_vertex(theta):
        c_min_inv = 4*tau2**2*np.exp(-theta)/SQ                     # 1/c maximal at T=T'=tau2
        arg = SQ*np.exp(theta)*tau2**2*psi0/(4*Psi1)
        QLL = c_min_inv*Psi1*(1 + log(max(1.0, arg)))
        QPL = 4*(tau2/tau1)*np.exp(-theta)*Psi1/SQ
        xpp = SQ*np.exp(theta)*tau1**2/4
        QPP = float(np.interp(xpp**2, mm, Phi1)) if xpp**2 < 2000 else 0.0
        q1 = max(QLL, QPL, QPP)
        a = np.exp(theta)*tau1/(2*tau2)
        pt = float(np.sqrt(np.interp(pi*(a*tau1**2)**2/24, mm, Phi2))) if pi*(a*tau1**2)**2/24 < 2000 else 0.0
        E2 = max(S2/a, pt)
        # g>=3: m >= pi/24 ((g-2) tau1^2 e^theta)^2 ; |f^(g)| <= 2^g maxC e^{-m}(1+m)^5 ; ends: (1+(pi/2)tau2^4)^2
        qg = 0.0
        for g in range(3, 60):
            mgg = pi*((g-2)*tau1**2*np.exp(theta))**2/24
            lb = g*log(2) + log(6*maxC) - mgg + 5*log1p(mgg) + 2*log(1 + (pi/2)*tau2**4)
            qg = max(qg, exp(lb/g) if lb/g > -700 else 0.0)
        q = max(q1, E2, qg)
        K = max(1.0, (1+e_w)**2/(2*omx*h0))
        delta = K*2*omx*q/h0
        return dict(QLL=QLL, QPL=QPL, QPP=QPP, E2=E2, qg=qg, q=q, delta=delta)
    out.update(F=F, mono=mono, h_inf=h_inf, h0=h0, IW_low=IW_low, IW_vol=IW_vol, vol_dev=vol_dev, viol=viol,
               psi0=psi0, Psi1=Psi1, S2=S2, e_w=e_w, om=om)
    # smallest theta (0.25 grid) with delta <= 0.05
    th = None
    for t in np.arange(2, 60, 0.25):
        r = per_vertex(t)
        if r["delta"] <= 0.05:
            th = t; break
    out["theta_star"] = th; out["pv"] = per_vertex(th)
    out["per_vertex"] = per_vertex
    return out

from math import log1p

if __name__ == "__main__":
    lP = 1.616255e-35; pc = 3.0856776e16; D = 1e9*pc
    for (tau1, tau2) in [(0.1, 0.6), (0.15, 0.5)]:
        print("=== window W = [%.2f, %.2f] ===" % (tau1, tau2))
        for k, C in enumerate(rc.OPS):
            e1, e2 = check_fder(C)
            o = analyse(k, C, tau1, tau2)
            pv = o["pv"]; th = o["theta_star"]; d = pv["delta"]
            eta = (th + log(8))/2
            print("op%d: fder check %.1e %.1e | f decreasing on [0,tau2]: %s ; sup|f| = %.6f ; h_inf <= %.6f ; h0 = inf_W h >= %.6f"
                  % (k, e1, e2, o["mono"], o["F"], o["h_inf"], o["h0"]))
            print("     Volterra sanity: max|H_vol - f| on [0,tau2] = %.4f (rigorous band at tau2 = %.4f; violation: %s)"
                  % (o["vol_dev"], o["h_inf"]-o["F"], o["viol"]))
            print("     psi(0)=sup|f'| = %.4f ; Psi1 = int Phi1(x^2) dx = %.4f ; S2 = %.4f ; weights e = %.4f, omega = %.4f"
                  % (o["psi0"], o["Psi1"], o["S2"], o["e_w"], o["om"]))
            print("     theta* = %.2f (eta* = %.3f): QLL=%.3e QPL=%.3e QPP=%.3e E2=%.3e q_g>=3=%.3e -> delta = %.4f"
                  % (th, eta, pv["QLL"], pv["QPL"], pv["QPP"], pv["E2"], pv["qg"], d))
            for t in [th+2, th+5]:
                print("        theta = %.2f -> delta = %.3e" % (t, o["per_vertex"](t)["delta"]))
            for s in [1.0e4, 1.2e4]:
                lk = 1e-19; eps = (lP/lk)**4; tau = np.sqrt(2*D*s + s*s)/lk
                z = 1.0*np.sqrt(eps)    # z = c sqrt(eps), c = O(1)
                err = 2*np.exp(-2*eta) + z*tau2*np.exp(-eta)/2 + (z*tau2*np.exp(eta))**2/8
                clow = (1-2*d)*np.sqrt(pi*o["IW_low"]*(1-err))
                cfail = 2/(np.sqrt(eps)*tau)
                print("     s = %.1e m: eps = %.4e, sqrt(eps) tau = %.3f ; c_fail = %.5f ; I_W >= %.5f (Volterra %.5f) ; err = %.1e ;"
                      " c_low = %.4f ; c_low/c_fail = %.1f ; sd e-folds >= %.1f"
                      % (s, eps, np.sqrt(eps)*tau, cfail, o["IW_low"], o["IW_vol"], err, clow, clow/cfail, clow*np.sqrt(eps)*tau/2))
