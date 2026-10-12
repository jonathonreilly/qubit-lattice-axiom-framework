"""C5 R4-2 (2): the escape outside class F -- the restricted-continuum shell representation.

Dual (quasi-momentum) coordinates k = D q / 2pi, D = diag(sqrt7,1,1,1), so that
e^{i q.x} = e^{2 pi i k.n} for sites x = D n of L7.  Mass shell (signature -+++):
    Q*(k) := k0^2 - 7 (k1^2+k2^2+k3^2) = M := 7 m^2 / (4 pi^2),  k0 > 0.
Gamma acts on k by B = g^{-T} (integral).  The torus point is p = k mod Z^4.

Checks:
 (A) a.e. injectivity of pi: H_m -> T^4: for random (irrational) shell points, the lift
     of p = frac(k) inside a box |n_i| <= NB is unique and equals k (60-digit check).
 (B) exact equivariance of the lift iota: iota(B p mod 1) = B iota(p), for several
     group elements B (60 digits).
 (C) nowhere-continuity / density: for a Haar-random p (not on the shell) the distance
     of p to the image shell, among lifts with |n| <= NB, falls with NB (power law),
     so every open set of T^4 meets the shell with arbitrarily large lifts.  A 1e-12
     perturbation of a shell point has no lift in the box.
 (D) rational (finite-orbit) shell points carry infinitely many lifts: the 'tower'
     sits exactly on the atoms; count lifts of p = (1/2,1/2,1/2,1/2) with M = 1.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 60
rng = np.random.default_rng(42)


def emb(a, b, c, d, i, j):
    M = np.eye(4, dtype=np.int64)
    M[i, i], M[i, j], M[j, i], M[j, j] = a, b, c, d
    return M


g1 = emb(8, 3, 21, 8, 0, 1)
g2 = emb(8, 3, 21, 8, 0, 2)
g3 = emb(8, 3, 21, 8, 0, 3)
Rz = np.array([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=np.int64)
G7 = np.diag([-7, 1, 1, 1])
for M in (g1, g2, g3, Rz):
    assert (M.T @ G7 @ M == G7).all()


def dual(M):
    Mi = np.round(np.linalg.inv(M)).astype(np.int64)
    assert (Mi @ M == np.eye(4, dtype=np.int64)).all()
    return Mi.T


m = mp.mpf("0.5")
Mshell = 7 * m**2 / (4 * mp.pi**2)


def Qstar(k):
    return k[0]**2 - 7 * (k[1]**2 + k[2]**2 + k[3]**2)


def random_shell_point(maxrap=0.6):
    # random direction and rapidity, physical q, then k
    v = rng.normal(size=3)
    v /= np.linalg.norm(v)
    eta = mp.mpf(float(rng.uniform(0, maxrap)))
    qs = [m * mp.sinh(eta) * mp.mpf(float(c)) for c in v]
    q0 = mp.sqrt(m**2 + sum(c**2 for c in qs))
    k = [q0 * mp.sqrt(7) / (2 * mp.pi)] + [c / (2 * mp.pi) for c in qs]
    assert abs(Qstar(k) - Mshell) < mp.mpf("1e-50")
    return k


def frac(k):
    return [x - mp.floor(x) for x in k]


def lifts(p, NB, tol_float=1e-7, tol_mp=mp.mpf("1e-40"), Mval=None):
    """All n in Z^4 with |n_i|<=NB (spatial) and Q*(p+n)=M, k0>0."""
    if Mval is None:
        Mval = Mshell
    pf = np.array([float(x) for x in p])
    r = np.arange(-NB, NB + 1)
    n1, n2, n3 = np.meshgrid(r, r, r, indexing="ij")
    s = 7 * ((pf[1] + n1)**2 + (pf[2] + n2)**2 + (pf[3] + n3)**2)
    k0 = np.sqrt(float(Mval) + s)
    t = k0 - pf[0]
    fr = np.abs(t - np.round(t))
    idx = np.argwhere(fr < tol_float)
    out = []
    for (a, b, c) in idx:
        nv = [int(np.round(t[a, b, c])), int(r[a]), int(r[b]), int(r[c])]
        k = [p[i] + nv[i] for i in range(4)]
        if k[0] > 0 and abs(Qstar(k) - Mval) < tol_mp:
            out.append(k)
    return out, fr


print(f"m = {m} lattice units, M = 7 m^2/(4 pi^2) = {mp.nstr(Mshell, 12)}")
print("(A) uniqueness of the lift (a.e. injectivity), box |n_i| <= 25:")
pts = [random_shell_point() for _ in range(6)]
for k in pts:
    p = frac(k)
    L, _ = lifts(p, 25)
    ok = len(L) == 1 and max(abs(L[0][i] - k[i]) for i in range(4)) < mp.mpf("1e-45")
    print(f"   k = {[mp.nstr(x, 6) for x in k]}  #lifts = {len(L)}  equals k: {ok}")

print("(B) equivariance iota(B p) = B iota(p) (60 digits):")
words = {"g1": g1, "g1^-1": np.round(np.linalg.inv(g1)).astype(np.int64), "g2": g2,
         "g3 Rz": g3 @ Rz, "Rz g1 g2^-1": Rz @ g1 @ np.round(np.linalg.inv(g2)).astype(np.int64)}
for name, g in words.items():
    B = dual(g)
    for k in pts[:3]:
        kB = [sum(int(B[i, j]) * k[j] for j in range(4)) for i in range(4)]
        assert abs(Qstar(kB) - Mshell) < mp.mpf("1e-45")
        if kB[0] <= 0:
            print(f"   {name}: image on past sheet (orthochronous check) -- skipped")
            continue
        pB = frac(kB)
        NB = int(max(abs(float(x)) for x in kB[1:])) + 3
        L, _ = lifts(pB, NB)
        err = min(max(abs(l[i] - kB[i]) for i in range(4)) for l in L) if L else None
        print(f"   {name:12s} |k'|_E={float(mp.sqrt(sum(x**2 for x in kB))):8.3f}  "
              f"#lifts in box {NB} = {len(L)}  |iota(Bp)-B iota(p)| = {mp.nstr(err, 3) if err is not None else 'NONE'}")

print("(C) density of the image shell / nowhere-continuity of iota:")
for trial in range(3):
    p = [mp.mpf(float(x)) for x in rng.uniform(0, 1, 4)]
    row = []
    for NB in (4, 8, 16, 32):
        _, fr = lifts(p, NB)
        row.append((NB, float(fr.min())))
    print("   Haar-random p: min distance (in k0) to shell lifts with |n|<=NB:",
          ", ".join(f"NB={a}: {b:.2e}" for a, b in row))
k = pts[0]
p = frac(k)
pp = [p[0] + mp.mpf("1e-12")] + p[1:]
L, fr = lifts(pp, 25, tol_float=1e-14)
print(f"   shell point p perturbed by 1e-12 in k0: #exact lifts in box 25 = {len(L)}; "
      f"nearest shell lift distance = {fr.min():.2e}")

print("(D) rational point p=(1/2,1/2,1/2,1/2) on M=1 (k=(5,1,1,1)/2): lifts in boxes")
Mone = mp.mpf(1)
p = [mp.mpf(1) / 2] * 4
for NB in (5, 10, 20, 40):
    L, _ = lifts(p, NB, Mval=Mone, tol_float=1e-9)
    print(f"   box {NB:3d}: #lifts on H_m over this single torus point = {len(L)}")
print("   (finite-orbit atoms carry the unbounded multiplicity; generic points carry 1)")
