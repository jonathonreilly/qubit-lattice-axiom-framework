"""R6-3 (a)-(c),(e): exact Haar-average count variance of the LRL ensemble in sharp diamonds D_T and
truncated past cones P_T, from Var N(W_T) = rho^2 T^6 sum_{t != 0} C*_t J_W(c t T^2)  (report section 2).
Inputs: r63_Jtable.npz (J), r63_Cstar.npy (C*_t, |t| <= 4000). Compared with the R4-5 Monte Carlo."""
import numpy as np
d = np.load('r63_Jtable.npz'); absM = d['absM']
Cs = np.load('r63_Cstar.npy'); tt = Cs[:, 0].astype(int); CC = Cs[:, 1]
rho = 1/np.sqrt(7); c = (2*np.pi)**2/7; A = 16*np.pi**3
lnM = np.log(absM)

def fitB(Jx, lo=1e6, hi=3.2e8):
    sel = (absM >= lo) & (absM <= hi)
    return np.mean(absM[sel]**2*Jx[sel] - A*lnM[sel])
B_Dt, B_Ds = fitB(d['DJt']), fitB(d['DJs'])
selP = (absM >= 1e5) & (absM <= 3.2e8)
aPt, bPt = np.polyfit(lnM[selP], absM[selP]**2*(d['PJt'][selP] - 1039.0300*absM[selP]**-1.5), 1)
aPs, bPs = np.polyfit(lnM[selP], absM[selP]**2*d['PJs'][selP], 1)
print("asymptotic forms used beyond |M| = 1e8:")
print("  diamond  J = (16 pi^3 ln|M| + B)/M^2 , B_tl = %.1f, B_sl = %.1f" % (B_Dt, B_Ds))
print("  pastcone J_tl = (2pi)^3 (4pi/3) |M|^-1.5 + (%.1f ln|M| + %.1f)/M^2 ; J_sl = (%.1f ln|M| + %.1f)/M^2" % (aPt, bPt, aPs, bPs))

def Jfun(W, M):
    M = np.asarray(M, float); m = np.abs(M); out = np.empty_like(m)
    tl = M < 0
    for sgn, mask in ((-1, tl), (1, ~tl)):
        key = W + ('Jt' if sgn < 0 else 'Js')
        tab = d[key]
        mm = m[mask]; inside = mm <= 1e8
        val = np.empty_like(mm)
        val[inside] = np.exp(np.interp(np.log(mm[inside]), lnM, np.log(tab)))
        x = mm[~inside]; lx = np.log(x)
        if W == 'D':
            val[~inside] = (A*lx + (B_Dt if sgn < 0 else B_Ds))/x**2
        else:
            val[~inside] = (1039.0300*x**-1.5 + (aPt*lx + bPt)/x**2) if sgn < 0 else (aPs*lx + bPs)/x**2
        out[mask] = val
    return out

def Var(W, T):
    s = np.sum(CC*Jfun(W, c*tt*T**2))
    # tail |t| > 4000: mean density c rho*, J ~ asymptotic forms
    tmax = 4000.0
    if W == 'D':
        tail = 2*c*np.sqrt(7)/(2*np.pi)**4*(A*(np.log(c*tmax*T**2) + 1) + 0.5*(B_Dt + B_Ds))/(c*T**2)**2/tmax
    else:
        tail = c*np.sqrt(7)/(2*np.pi)**4*(1039.03*2/(c*T**2)**1.5/np.sqrt(tmax))
    return rho**2*T**3*((s + tail)*T**3)

vol = {'D': np.pi/24, 'P': np.pi/3}
print("\n== diamonds: exact Haar average (Siegel shell sum) vs R4-5 Monte Carlo (ball-averaged frames) ==")
mc = {13: (0.5183, 0.5923), 27: (0.6457, 0.6314), 54: (0.7194, 0.7782), 108: (0.8796, 0.8247)}
print("   T     Var        Var/(rho V)     Var/T^2   [R4-5 MC Var/T^2: eta_max 1.5, 3.0 (+-4..9%)]")
for T in (6, 9, 13, 19, 27, 38, 54, 76, 108):
    v = Var('D', T); rv = rho*vol['D']*T**4
    extra = "   MC: %.3f, %.3f" % mc[T] if T in mc else ""
    print("  %4d  %10.4e  %10.4e  %8.4f%s" % (T, v, v/rv, v/T**2, extra))
print("\n== asymptotics (diamonds): Var / (T^2 ln T) and Var/T^2 ==")
G = rho**2*np.sum(CC/(c*tt)**2)
print("   predicted leading law Var ~ 2*16pi^3 rho^2 [sum_t C*_t/(c t)^2] T^2 ln T = %.5f T^2 ln T" % (2*A*G))
for T in (1e2, 1e3, 1e4, 1e5, 1e6, 1e8, 1e12, 1e30, 5e60):
    v = Var('D', T)
    print("   T=%8.1e  Var/T^2=%10.4f  Var/(T^2 lnT)=%8.5f  Var/(rho V)=%.3e" % (T, v/T**2, v/(T**2*np.log(T)), v/(rho*vol['D']*T**4)))
print("\n== truncated past cones (flat spacelike base) ==")
H = rho**2*np.sum(np.where(tt < 0, CC*1039.03/(c*np.abs(tt))**1.5, 0.0))
print("   predicted leading law Var ~ (2pi)^3|B_1| rho^2 sum_{t<0} C*_t/(c|t|)^1.5 T^3 = %.5f T^3" % H)
for T in (13, 27, 54, 108, 1e3, 1e4, 1e6, 1e8, 1e12, 5e60):
    v = Var('P', T)
    print("   T=%8.1e  Var=%10.4e  Var/T^3=%8.5f  Var/(rho V)=%.3e" % (T, v, v/T**3, v/(rho*vol['P']*T**4)))
np.savez('r63_variance_consts.npz', G=G, H=H, B_Dt=B_Dt, B_Ds=B_Ds)
