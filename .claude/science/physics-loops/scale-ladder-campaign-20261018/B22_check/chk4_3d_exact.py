"""B22 check 4: 3D steps W_iso = e^{-ik_x s_x} e^{-ik_y s_y} e^{-ik_z s_z} and the uniaxial toy (z angle 2k_z),
generator lapse (Definition B), via EXACT momentum-space bracket elements (chk1 M6/M7) instead of 64^3 FFTs.

h(k) = i log W(k) in closed form: W = cos(om) 1 - i sin(om) n.s (det W = 1) -> h = om n.s (no eigensolver).
 X1 dispersion: om = arccos(c_x c_y c_z - s_x s_y s_z) for W_iso (and with 2k_z for W_ani).
 X2 uniform-w bracket (N = cos q.x, M = sin q.x): exact diagonal element K(k) vs first-order symbol
    -i q.(1/2)grad(h^2); residual ~ q^2 at fixed k, and ~ q^2/|k| at fixed q (breakdown for |k| <~ q^2/a).
 X3 node metric: K(k) vs -i q.g.k with g = diag(1,1,1) / diag(1,1,4); best-fit kappa for q || x, q || z.
 X4 spin term (not tested by B22: its lapses have grad N || grad M): N = e^{ia.x}, M = e^{ib.x} with a not || b;
    exact element E(k;a,b) vs  S1 + S2,  S1 = (b-a).(1/2)grad(h^2)(m),  S2 = (1/4) a_i b_j [d_i h, d_j h](m);
    and S2 vs the node-triad Kosmann form (i/2) s.(cof(e)(a x b)), cof(e) = diag(1,1,1) / diag(2,2,1).
"""
import time
import numpy as np

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"\n        {detail}" if detail else ""))
t0 = time.time(); rng = np.random.default_rng(44)
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
def U(theta, j):
    return np.cos(theta) * np.eye(2) - 1j * np.sin(theta) * s[j]
def Wstep(k, zf):
    return U(k[0], 0) @ U(k[1], 1) @ U(zf * k[2], 2)
def hgen(k, zf):
    W = Wstep(k, zf)
    c = np.real(np.trace(W)) / 2
    om = np.arccos(np.clip(c, -1, 1))
    # W - c 1 = -i sin(om) n.s  -> n_j = i tr(s_j (W - c))/(2 sin om)
    nv = np.array([np.real(1j * np.trace(s[j] @ (W - c * np.eye(2)))) / (2 * np.sin(om)) for j in range(3)])
    return om * sum(nv[j] * s[j] for j in range(3)), om
def dh(k, zf, j, d=1e-5):
    e = np.zeros(3); e[j] = d
    return (hgen(k + e, zf)[0] - hgen(k - e, zf)[0]) / (2 * d)
def half_grad_hsq(k, zf, d=1e-5):
    out = []
    for j in range(3):
        e = np.zeros(3); e[j] = d
        out.append(0.25 * (hgen(k + e, zf)[1] ** 2 - hgen(k - e, zf)[1] ** 2) / d)
    return np.array(out)

# ---------------------------------------------------------------- X1
K = rng.uniform(-np.pi, np.pi, (3000, 3)); dev = 0
for k in K:
    c, sn = np.cos(k), np.sin(k)
    dev = max(dev, abs(hgen(k, 1)[1] - np.arccos(np.clip(c[0] * c[1] * c[2] - sn[0] * sn[1] * sn[2], -1, 1))))
    dev = max(dev, np.abs(Wstep(k, 1) @ Wstep(k, 1).conj().T - np.eye(2)).max())
check("X1 [numerical identity] W_iso eigenphase om = arccos(c_x c_y c_z - s_x s_y s_z); W unitary, det 1",
      dev < 1e-10, f"max deviation {dev:.1e} over 3000 k")

# ---------------------------------------------------------------- X2/X3 uniform-w exact element
def Kexact(k, qv, zf):
    hk = hgen(k, zf)[0]; hp = hgen(k + qv, zf)[0]; hm = hgen(k - qv, zf)[0]
    return -1j / 8 * ((hk + hp) @ (hk + hp) - (hk + hm) @ (hk + hm))
def shell(kc, nk=60):
    v = rng.normal(size=(nk, 3)); return kc * v / np.linalg.norm(v, axis=1)[:, None]
dirs = {"x": [1, 0, 0], "z": [0, 0, 1], "xz": [1, 0, 1], "xyz": [1, 1, 1]}
print("\n  X2: relative error of the first-order symbol -i q.(1/2)grad(h^2) vs the exact element, shell |k| = kc")
print("  step  dir   |q|      kc=0.05     kc=0.1      kc=0.2      kc=0.4")
X2 = {}
for nm, zf in (("iso", 1), ("ani", 2)):
    for dn, dvec in dirs.items():
        u = np.array(dvec, float); u /= np.linalg.norm(u)
        for qm in (0.02, 0.04):
            row = []
            for kc in (0.05, 0.1, 0.2, 0.4):
                ks = shell(kc); num = den = 0
                for k in ks:
                    Ke = Kexact(k, qm * u, zf); P1 = -1j * (qm * u) @ half_grad_hsq(k, zf) * np.eye(2)
                    num += np.linalg.norm(Ke - P1) ** 2; den += np.linalg.norm(P1) ** 2
                row.append(np.sqrt(num / den))
            X2[(nm, dn, qm)] = row
            print(f"  {nm}   {dn:4s} {qm:.2f}    " + "   ".join(f"{x:.2e}" for x in row))
sq = all(3.0 < X2[(nm, dn, 0.04)][i] / X2[(nm, dn, 0.02)][i] < 5.0 for nm in ("iso", "ani") for dn in dirs for i in range(4)
         if X2[(nm, dn, 0.02)][i] > 1e-9)
ik = all(X2[(nm, dn, 0.02)][0] > X2[(nm, dn, 0.02)][3] for nm in ("iso", "ani") for dn in ("xz", "xyz"))
check("X2 [numerical, exact elements] both steps: first-order symbol residual scales ~ q^2 (ratio 3-5 on doubling q)"
      " and grows toward the node at fixed q for off-axis lapse gradients (the expansion parameter is q^2/(|k| a))",
      sq and ik, f"e.g. iso xyz |q|=0.02: {np.round(X2[('iso','xyz',0.02)], 5)}")

print("\n  X3: kappa fit K = kappa * (-i q.k) on the shell kc = 0.1, and residual vs -i q.g.k")
kap = {}; resg = {}
for nm, zf, g in (("iso", 1, np.eye(3)), ("ani", 2, np.diag([1.0, 1.0, 4.0]))):
    for dn in ("x", "z", "xz", "xyz"):
        u = np.array(dirs[dn], float); u /= np.linalg.norm(u); qv = 0.01 * u
        ks = shell(0.1); num = den = ng = dg = 0
        for k in ks:
            Ke = Kexact(k, qv, zf); T = -1j * (qv @ k) * np.eye(2); Tg = -1j * (qv @ g @ k) * np.eye(2)
            num += np.real(np.vdot(T, Ke)); den += np.real(np.vdot(T, T))
            ng += np.linalg.norm(Ke - Tg) ** 2; dg += np.linalg.norm(Tg) ** 2
        kap[(nm, dn)] = num / den; resg[(nm, dn)] = np.sqrt(ng / dg)
        print(f"  {nm}  q || {dn:4s}: kappa = {kap[(nm, dn)]:.4f}   rel. residual vs -i q.g.k = {resg[(nm, dn)]:.3f}")
check("X3 [numerical, exact elements] node-metric form: residual vs -i q.g.k < 15% at kc = 0.1 for both steps"
      " (the remainder is the steps' linear-in-k anisotropy); uniaxial kappa ~ 1 (q || x) and ~ 4 (q || z)",
      max(resg.values()) < 0.15 and abs(kap[("ani", "x")] - 1) < 0.05 and abs(kap[("ani", "z")] - 4) < 0.2 and
      abs(kap[("iso", "z")] - 1) < 0.05, f"kappa_ani: x {kap[('ani','x')]:.4f}, z {kap[('ani','z')]:.4f}")

# ---------------------------------------------------------------- X4 spin term
def Eexact(k, a, b, zf):
    h = lambda kk: hgen(kk, zf)[0]
    return 0.25 * ((h(k + a + b) + h(k + b)) @ (h(k + b) + h(k)) - (h(k + a + b) + h(k + a)) @ (h(k + a) + h(k)))
print("\n  X4: N = e^{ia.x}, M = e^{ib.x}, a = eps*(1,0,0), b = eps*(0,1,0.5) (a x b != 0); midpoint m on shell |m| = 0.15")
print("  step  eps     |E - S1|/|E|   |E - S1 - S2|/|E|   |S2 - S2_triad|/|S2_triad|")
X4 = {}
for nm, zf, cof in (("iso", 1, np.eye(3)), ("ani", 2, np.diag([2.0, 2.0, 1.0]))):
    for ep in (0.01, 0.02):
        a = ep * np.array([1.0, 0, 0]); b = ep * np.array([0, 1.0, 0.5])
        r1 = r2 = r3 = 0; nE = nT = 0
        for m in shell(0.15, 40):
            k = m - (a + b) / 2
            E = Eexact(k, a, b, zf)
            S1 = ((b - a) @ half_grad_hsq(m, zf)) * np.eye(2)
            D = [dh(m, zf, j) for j in range(3)]
            S2 = 0.25 * sum(a[i] * b[j] * (D[i] @ D[j] - D[j] @ D[i]) for i in range(3) for j in range(3))
            sv = cof @ np.cross(a, b); S2t = 0.5j * sum(sv[j] * s[j] for j in range(3))
            r1 += np.linalg.norm(E - S1) ** 2; r2 += np.linalg.norm(E - S1 - S2) ** 2; r3 += np.linalg.norm(S2 - S2t) ** 2
            nE += np.linalg.norm(E) ** 2; nT += np.linalg.norm(S2t) ** 2
        X4[(nm, ep)] = (np.sqrt(r1 / nE), np.sqrt(r2 / nE), np.sqrt(r3 / nT))
        print(f"  {nm}   {ep:.2f}     {X4[(nm, ep)][0]:.3e}        {X4[(nm, ep)][1]:.3e}            {X4[(nm, ep)][2]:.3f}")
ok4 = all(X4[(nm, 0.01)][0] > 5 * X4[(nm, 0.01)][1] for nm in ("iso", "ani")) and \
      all(X4[(nm, 0.01)][2] < 0.35 for nm in ("iso", "ani"))
check("X4 [numerical, exact elements] with grad N x grad M != 0 both steps' brackets carry the second-order spin term"
      " (1/4)a_i b_j[d_i h, d_j h]: including it cuts the residual > 5x; at |m| = 0.15 it is the node-triad Kosmann"
      " form (i/2)s.(cof(e)(a x b)) up to the steps' O(|k|) anisotropy (uniaxial: cof(e) = diag(2,2,1), not g = diag(1,1,4))",
      ok4)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}  ({time.time() - t0:.1f} s)")

# ---------------------------------------------------------------- X4b triad limit of the spin term
print("\n  X4b: |S2 - S2_triad|/|S2_triad| vs |m| (eps = 0.005)")
tri = {}
for nm, zf, cof in (("iso", 1, np.eye(3)), ("ani", 2, np.diag([2.0, 2.0, 1.0]))):
    row = []
    for mm in (0.15, 0.075, 0.0375):
        a = 0.005 * np.array([1.0, 0, 0]); b = 0.005 * np.array([0, 1.0, 0.5]); r3 = nT = 0
        for m in shell(mm, 40):
            D = [dh(m, zf, j) for j in range(3)]
            S2 = 0.25 * sum(a[i] * b[j] * (D[i] @ D[j] - D[j] @ D[i]) for i in range(3) for j in range(3))
            sv = cof @ np.cross(a, b); S2t = 0.5j * sum(sv[j] * s[j] for j in range(3))
            r3 += np.linalg.norm(S2 - S2t) ** 2; nT += np.linalg.norm(S2t) ** 2
        row.append(np.sqrt(r3 / nT))
    tri[nm] = row
    print(f"  {nm}: " + "  ".join(f"{x:.4f}" for x in row))
check("X4b [numerical] the step spin term tends to the node-triad Kosmann form linearly in |m| (ratio ~2 per halving)",
      all(1.6 < tri[nm][i] / tri[nm][i + 1] < 2.5 for nm in tri for i in range(2)))
print(f"\nTOTAL (incl. X4b): PASS={PASS} FAIL={FAIL}  ({time.time() - t0:.1f} s)")
