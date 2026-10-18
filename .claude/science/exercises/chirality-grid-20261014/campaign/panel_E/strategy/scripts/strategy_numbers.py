# Panel E strategy lens: back-of-envelope numbers (suggested-level estimates, not physics results).
import numpy as np
# (1) X2' (three generations internal at one k=0 corner): one-loop flavour-pattern speed matrix on Q ~ kbar*(Hu+Hd).
# kbar ~ 0.011 is OBS-3's hw1-corner isotropic kernel (kbar^2 ~ 1.3e-4, OBS3 REPORT:169); the Gamma-point kernel is NOT computed.
kbar = np.sqrt(1.3e-4)
# PDG-like CKM (standard parametrisation), magnitudes only matter here
s12,s23,s13,d = 0.2250, 0.0418, 0.00369, 1.144
c12,c23,c13 = np.sqrt(1-s12**2), np.sqrt(1-s23**2), np.sqrt(1-s13**2)
e = np.exp(1j*d)
V = np.array([[c12*c13, s12*c13, s13/e],
              [-s12*c23-c12*s23*s13*e, c12*c23-s12*s23*s13*e, s23*c13],
              [s12*s23-c12*c23*s13*e, -c12*s23-s12*c23*s13*e, c23*c13]])
for label, (yu,yc,yt,yd,ys,yb) in {"low-scale": (1.2e-5,3.6e-3,0.94,2.7e-5,5.5e-4,2.4e-2),
                                   "~Planck (x0.45)": tuple(0.45*np.array([1.2e-5,3.6e-3,0.94,2.7e-5,5.5e-4,2.4e-2]))}.items():
    Hu = np.diag([yu**2,yc**2,yt**2])           # up-mass basis for Q
    Hd = V @ np.diag([yd**2,ys**2,yb**2]) @ V.conj().T
    H = Hu + Hd
    up_rows = np.real(np.diag(H))               # u_L, c_L, t_L
    dn_rows = np.real(np.diag(V.conj().T @ H @ V))  # d_L, s_L, b_L
    spread_ud = kbar*(dn_rows[0]-up_rows[0])
    print(f"[{label}] kbar*(H_dd - H_uu) = {spread_ud:.2e}  -> vs c^d,u rows ~1e-22: x{abs(spread_ud)/1e-22:.1e}"
          f"  (one universal Q counterterm can zero only one of u_L, d_L)")
    print(f"   rows kbar*diag: u {kbar*up_rows[0]:.1e} c {kbar*up_rows[1]:.1e} t {kbar*up_rows[2]:.1e} | d {kbar*dn_rows[0]:.1e} s {kbar*dn_rows[1]:.1e} b {kbar*dn_rows[2]:.1e}")
    # a single flavour-covariant counterterm kappa*Hu on Q cancels the Hu part exactly; residual from Hd part:
    resid = kbar*(np.real(np.diag(V.conj().T@Hd@V))[0]-np.real(np.diag(Hd))[0])
    print(f"   after one covariant counterterm ~Hu on Q (tuned to kbar): residual from Hd {resid:.1e}; tuning needed ~ {1e-22/abs(spread_ud):.0e} of kbar")
# (2) Cloud cost for a 2+1D finite-size scan, from QMC-1 cost model (REPORT:199-211), beta=4, per 1000 sweeps per W
ch = {8:93, 12:1056}
ch[10] = 93*(10/8)**6      # N^3 scaling with N ~ L^2
sweeps, nW = 2000, 6
tot = sum(ch[L]*sweeps/1000*nW for L in (8,10,12))
for fac,lab in ((1,"as-is Python engine"),(8,"with singlet-sector factorisation (~8x)")):
    t = tot/fac
    print(f"2+1D scan L=8,10,12 x {nW} W x {sweeps} sweeps, beta=4, {lab}: {t:,.0f} core-h  ~ ${0.01*t:,.0f}-${0.05*t:,.0f}")
print(f"  beta=L variant ~x3 on L=12 (REPORT:206): add ~{ch[12]*2*sweeps/1000*nW:,.0f} core-h before factorisation")
# (3) QMC-1b in-house wall time (2 threads), from measured L6 sweep 29.7 s at beta=4, dtau=0.1 (REPORT:199)
t6 = 29.7; t4 = t6*(16/36)**3
for dt_fac,lab in ((1,"dtau 0.1"),(2,"dtau 0.05")):
    print(f"QMC-1b per 200 sweeps ({lab}): L4 {200*t4*dt_fac/3600:.2f} h, L6 {200*t6*dt_fac/3600:.2f} h")
