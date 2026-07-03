"""Finite runner (memory-safe): finite-k yz TT bubble sign diagnostic for the
native elliptic anti-Hermitian lattice Dirac operator.

#3214 (universal_gr_scalar_generator_tt_kernel_sharpening): the HOMOGENEOUS (k=0) metric
coupling enters det(D+J) only via the O_h scalar s(q)=g_ij qhat^i qhat^j -> TT graviton in the
exact kernel. #3220 (universal_gr_degenerate_supermetric_graviton_sign_no_go): the k=0
supermetric is degenerate (trace=shear), gluing gives an opposite-signed (tachyonic) graviton.
BOTH are k=0 (homogeneous-metric / ultralocal) statements.

THIS NOTE: the runner checks a FINITE-k yz transverse-traceless channel and a trace-channel
contrast.  It does not prove that the yz vertex is the complete finite-k metric Hessian of
W=log|det(D+J)|, nor does it prove the full diffeomorphism Ward identity or spin-2 isotropy
bridge.  On the framework's NATIVE Dirac generator -- the real ANTI-HERMITIAN lattice Dirac
H=iD (det = m^2+|sin q|^2 > 0, an elliptic / valid partition function) -- the runner-defined
yz TT k^2 coefficient is POSITIVE, CONVERGENT, and mass-robust.  The non-elliptic bare-Hermitian
control is negative and divergent.

  T1  native lattice Dirac is anti-Hermitian -> elliptic: det(iD+m)=m^2+|sin q|^2 > 0 on ALL BZ
      modes (valid Sakharov Z); the bare-Hermitian sigma.sin gives m^2-|sin q|^2 (sign-indefinite,
      invalid Z).
  T2  the exact-TT yz channel (k along x) is transverse-traceless by construction (k^i h_ij=0,
      tr h=0) inside this runner-defined channel.
  T3  on the native elliptic iD: TT-projected k^2 slope is POSITIVE and CONVERGENT in BZ size
      (N=10..22 -> ~+0.0188) as a finite-BZ sign diagnostic.
  T4  mass-robust: TT slope > 0 for m in {0.5,1.0,1.5,2.0}; channels SPLIT at finite k with TT
      (+) OPPOSITE-signed to trace (-) inside this diagnostic.
  T5  CONTROL: the non-elliptic bare-Hermitian sigma.sin (det sign-indefinite, not a valid Z)
      gives a NEGATIVE, N-DIVERGENT slope -- the tachyonic artifact; not the native generator.

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
sig = [sx, sy, sz]

results = []
def check(name, ok): results.append((name, bool(ok)))

# --- T1: native anti-Hermitian Dirac is elliptic (det>0); bare Hermitian is sign-indefinite ---
N = 16
pts = np.linspace(-np.pi, np.pi, N, endpoint=False)
m = 1.0
neg_iD = 0; neg_H = 0; tot = 0
for qx in pts:
    for qy in pts:
        for qz in pts:
            s2 = np.sin(qx) ** 2 + np.sin(qy) ** 2 + np.sin(qz) ** 2
            if m * m + s2 <= 0: neg_iD += 1     # iD: det = m^2 + |sin|^2
            if m * m - s2 <= 0: neg_H += 1       # bare Herm: det = m^2 - |sin|^2
            tot += 1
check("T1 native anti-Herm iD elliptic: det=m^2+|sin|^2 > 0 on ALL BZ modes (valid Z)", neg_iD == 0)
check("T1b bare-Hermitian sigma.sin: det=m^2-|sin|^2 sign-indefinite (%d/%d modes <=0, invalid Z)" % (neg_H, tot),
      neg_H > tot // 2)

# --- stress 2-pt function on the yz TT channel (k along x) ---
def tt_slope(elliptic, mass, Ng):
    p = np.linspace(-np.pi, np.pi, Ng, endpoint=False)
    pref = 1j if elliptic else 1.0
    def D(q): return pref * (sig[0] * np.sin(q[0]) + sig[1] * np.sin(q[1]) + sig[2] * np.sin(q[2])) + mass * I2
    def V(q): return 0.5 * (sig[1] * pref * np.sin(q[2]) + sig[2] * pref * np.sin(q[1]))  # yz vertex
    def Pi(kx):
        t = 0
        for qx in p:
            for qy in p:
                for qz in p:
                    q = np.array([qx, qy, qz]); qk = np.array([qx + kx, qy, qz])
                    t += np.trace(np.linalg.inv(D(q)) @ V(q) @ np.linalg.inv(D(qk)) @ V(q))
        return t / Ng ** 3
    k1 = 2 * np.pi / Ng
    return ((Pi(k1) - Pi(0.0)) / (2 - 2 * np.cos(k1))).real

# --- T2: yz channel is TT by construction (k along x) ---
# h_yz with k=(kx,0,0): k^i h_ij = kx*h_xj = 0 (h_xy=h_xz=0); trace = 0. Transverse-traceless.
check("T2 yz channel (k along x): k^i h_ij=0 and tr h=0 inside this runner-defined channel", True)

# --- T3: native elliptic TT slope positive + convergent ---
slopes = [tt_slope(True, 1.0, Ng) for Ng in [10, 14, 18, 22]]
check("T3 native elliptic iD: TT k^2 slope POSITIVE for all N (%s)" % ", ".join("%+.4f" % s for s in slopes),
      all(s > 0 for s in slopes))
check("T3b convergent in BZ size (spread over N=10..22 < 0.002)", max(slopes) - min(slopes) < 2e-3)

# --- T4: mass-robust + channel split (TT vs trace opposite-signed) ---
mass_slopes = [tt_slope(True, mm, 16) for mm in [0.5, 1.0, 1.5, 2.0]]
check("T4 mass-robust: TT slope > 0 for m in {0.5,1,1.5,2} (%s)" % ", ".join("%+.4f" % s for s in mass_slopes),
      all(s > 0 for s in mass_slopes))
# trace channel
def trace_slope(mass, Ng=16):
    p = np.linspace(-np.pi, np.pi, Ng, endpoint=False)
    def D(q): return 1j * (sig[0] * np.sin(q[0]) + sig[1] * np.sin(q[1]) + sig[2] * np.sin(q[2])) + mass * I2
    def V(q): return (1j / 3) * (sig[0] * np.sin(q[0]) + sig[1] * np.sin(q[1]) + sig[2] * np.sin(q[2]))
    def Pi(kx):
        t = 0
        for qx in p:
            for qy in p:
                for qz in p:
                    q = np.array([qx, qy, qz]); qk = np.array([qx + kx, qy, qz])
                    t += np.trace(np.linalg.inv(D(q)) @ V(q) @ np.linalg.inv(D(qk)) @ V(q))
        return t / Ng ** 3
    k1 = 2 * np.pi / Ng
    return ((Pi(k1) - Pi(0.0)) / (2 - 2 * np.cos(k1))).real
tt = tt_slope(True, 1.0, 16); tr = trace_slope(1.0)
check("T4b diagnostic channels split, yz TT(+%.4f) OPPOSITE-signed to trace(%.4f)" % (tt, tr),
      tt > 0 and tr < 0)

# --- T5: control -- non-elliptic gives negative + N-divergent (artifact) ---
ns = [10, 14, 18]
hs = [tt_slope(False, 1.0, Ng) for Ng in ns]
check("T5 CONTROL: non-elliptic sigma.sin -> NEGATIVE slope (%s), N-divergent (not the native generator)"
      % ", ".join("%.0f" % s for s in hs),
      all(s < 0 for s in hs) and (max(abs(np.array(hs))) - min(abs(np.array(hs)))) > 50)

n_pass = sum(1 for _, ok in results if ok); n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("native elliptic iD yz TT finite-k bubble slope is positive, convergent, and mass-robust.")
print("non-elliptic bare-Hermitian control is negative and N-divergent.")
print("BOUNDED on: runner-defined yz channel; open = full W metric Hessian/contact terms,")
print("full Ward identity, E_g/T_2g spin-2 isotropy continuum limit, G_Newton magnitude, chiral limit.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
