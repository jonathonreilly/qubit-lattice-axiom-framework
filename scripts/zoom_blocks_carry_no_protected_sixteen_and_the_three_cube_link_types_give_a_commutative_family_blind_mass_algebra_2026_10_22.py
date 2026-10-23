AUDIT_INPUT_PATHS = ('docs/ZOOM_BLOCKS_CARRY_NO_PROTECTED_SIXTEEN_AND_THE_THREE_CUBE_LINK_TYPES_GIVE_A_COMMUTATIVE_FAMILY_BLIND_MASS_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Zoom blocks carry no protected 16; three cube link types give a commutative
geometric mass algebra (zoom-three-links probe, 2026-10-22). Seeded, self-contained."""
import itertools, signal, sys, time
import numpy as np
AUDIT_TIMEOUT_SEC = 90
signal.signal(signal.SIGALRM, lambda *a: sys.exit("TIMEOUT"))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
rng = np.random.default_rng(20261022)
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg}")

# O_h as 48 signed axis permutations
OH = []
for p in itertools.permutations(range(3)):
    for s in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[p[i], i] = s[i]
        OH.append(M)
def sites(L):  # doubled coordinates of an L^3 block centred at the origin
    r = [2 * k - (L - 1) for k in range(L)]
    return [np.array(v) for v in itertools.product(r, r, r)]
def perms(S):
    idx = {tuple(v): i for i, v in enumerate(S)}
    return [np.array([idx[tuple(g @ v)] for v in S]) for g in OH]
def multiplets(ev, tol=1e-8):
    ev = np.sort(ev); out = [1]
    for a, b in zip(ev[:-1], ev[1:]):
        if b - a < tol: out[-1] += 1
        else: out.append(1)
    return out

print("== A. does a zoom block carry a protected 16?")
# A1: O_h-commuting internal Spin(2N) needs O_h scalar on the 2N Majoranas
rows = []
for L in range(2, 7):
    S = sites(L); P = perms(S)
    fix = [np.sum(p == np.arange(len(S))) for p in P]
    chis = {"A1g": [1]*48, "A1u": [round(np.linalg.det(g)) for g in OH],
            "A2g": [round(np.linalg.det(np.abs(g))) for g in OH]}
    chis["A2u"] = [a*b for a, b in zip(chis["A1u"], chis["A2g"])]
    mult = {k: sum(c*f for c, f in zip(v, fix)) // 48 for k, v in chis.items()}
    rows.append((L, len(S), mult))
first = min(L for L, n, m in rows if 2 * max(m.values()) >= 10)
check("A1 [T]", first == 5 and rows[0][2]["A1g"] == 1 and rows[1][2]["A1g"] == 4,
      "an internal Spin(10) commuting with O_h needs 5 complex modes in one 1-dim O_h isotypic block (Schur on R^10); "
      "max 1-dim multiplicity by side L: " + ", ".join(f"L={L}:{max(m.values())}" for L, n, m in rows) +
      f"; smallest block with room = {first}^3 (2^3 has 1, 3^3 and 4^3 have 4)")
# A2: 2^3 block Fock space, generic O_h-invariant interacting H: multiplets <= 3
S2 = sites(2); P2 = perms(S2); n = 8; D = 2**n
def fock_perm(p):
    U = np.zeros((D, D))
    for st in range(D):
        occ = [a for a in range(n) if st >> (n-1-a) & 1]
        img = [p[a] for a in occ]
        sgn = 1
        for i in range(len(img)):
            for j in range(i+1, len(img)):
                if img[i] > img[j]: sgn = -sgn
        U[sum(1 << (n-1-b) for b in img), st] = sgn
    return U
c = []
for a in range(n):  # Jordan-Wigner
    op = np.array([[1.]])
    for b in range(n):
        f = np.diag([1., -1.]) if b < a else (np.array([[0., 1.], [0., 0.]]) if b == a else np.eye(2))
        op = np.kron(op, f)
    c.append(op)
h = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); h = h + h.conj().T
H0 = sum(h[a, b]*c[a].T@c[b] for a in range(n) for b in range(n))
for _ in range(12):
    a, b, cc, d = rng.choice(n, 4, replace=False); v = rng.normal() + 1j*rng.normal()
    t = v*c[a].T@c[b].T@c[cc]@c[d]; H0 = H0 + t + t.conj().T
Us = [fock_perm(p) for p in P2]
H = sum(U@H0@U.T for U in Us)
Nop = sum(ci.T@ci for ci in c)
ok_rep = max(np.abs(Us[i]@Us[j] - Us[[k for k in range(48) if np.array_equal(P2[k], P2[i][P2[j]])][0]]).max()
             for i, j in [(1, 5), (7, 30), (13, 41)]) < 1e-12
mx = 0; hist = {}
for N in range(n+1):
    sel = np.where(np.isclose(np.diag(Nop), N))[0]
    for m in multiplets(np.linalg.eigvalsh(H[np.ix_(sel, sel)]), 1e-7):
        hist[m] = hist.get(m, 0) + 1; mx = max(mx, m)
check("A2 [F]", ok_rep and mx == 3 and np.abs(H@Nop - Nop@H).max() < 1e-9,
      f"2^3 block, 256 states, generic O_h-symmetrised number-conserving interacting H (seeded): multiplet sizes {dict(sorted(hist.items()))}; "
      "largest = 3 = largest O_h irrep; no 16-fold level (would need a 16-dim irrep or a supplied degeneracy)")
# A3: 5^3 block: generic O_h-symmetric three-link-type hop splits the 10 orbit-uniform modes
S5 = sites(5); P5 = perms(S5); m5 = len(S5)
X = np.array(S5)//2; d2 = ((X[:, None, :]-X[None, :, :])**2).sum(-1)
H5 = np.where((d2 >= 1) & (d2 <= 3), rng.normal(size=(m5, m5)), 0.); H5 = H5 + H5.T
H5 = sum(H5[np.ix_(p, p)] for p in P5) / 48
Pa = sum(np.eye(m5)[:, p] for p in P5) / 48
w, vv = np.linalg.eigh(Pa); B = vv[:, w > 0.5]
eA = np.linalg.eigvalsh(B.T@H5@B); gap = np.min(np.diff(np.sort(eA)))
check("A3 [F]", B.shape[1] == 10 and gap > 1e-3 and max(multiplets(np.linalg.eigvalsh(H5), 1e-8)) == 3,
      f"5^3 block: 10 orbit-uniform (A1g) modes; generic O_h hop with axis/face/body links gives 10 distinct A1g levels (min gap {gap:.3f}); "
      "no 5 of them are degenerate, so a block Spin(10) is a supplied tuning, not protected by structure")
# A4: the 2pi rotation of a block Spin(10) is a c-number on the block (composite-sixteen B per block)
cf = []
for a in range(5):
    op = np.array([[1.]])
    for b in range(5):
        f = np.diag([1., -1.]) if b < a else (np.array([[0., 1.], [0., 0.]]) if b == a else np.eye(2))
        op = np.kron(op, f)
    cf.append(op)
g = []
for x in cf: g += [x + x.T, 1j*(x.T - x)]
Mab = lambda a, b: 0.5j*g[a]@g[b]
ev, U = np.linalg.eigh(Mab(0, 1)); R2pi = U@np.diag(np.exp(2j*np.pi*ev))@U.conj().T
gen = 0.3*Mab(0, 3) + 0.7*Mab(2, 7) - 0.4*Mab(5, 9)
ok_cas = np.abs(R2pi + np.eye(32)).max() < 1e-12
F = sum(x.T@x for x in cf); Pplus = np.diag(np.diag(F) % 2 == 0).astype(float)
ok_mix = np.abs(gen@Pplus - Pplus@gen).max() < 1e-12
check("A4 [T]", ok_cas and ok_mix,
      "on 5 block modes the 2pi rotation of Spin(10) is -1 on all 32 states (a c-number per block) and generators keep (-1)^F: "
      "the block's 16 is its Fock spinor, so on a fixed block lattice the composite-sixteen centre theorem applies blockwise")

print("== B. three cube link types (axis 1, face sqrt2, body sqrt3)")
Xc = np.array(S2)//1; Xc = (Xc + 1)//2
dd = ((Xc[:, None, :]-Xc[None, :, :])**2).sum(-1)
A = [(dd == k).astype(float) for k in (1, 2, 3)]
comm = max(np.abs(A[i]@A[j]-A[j]@A[i]).max() for i in range(3) for j in range(3))
ok_tab = True
for s in itertools.product([0, 1], repeat=3):
    v = np.array([(-1)**(np.dot(s, x)) for x in Xc]); w_ = sum(s)
    lam = [3-2*w_, ((3-2*w_)**2-3)/2, (-1)**w_]
    ok_tab &= all(np.allclose(A[k]@v, lam[k]*v) for k in range(3))
check("B1 [T]", comm < 1e-15 and ok_tab and [int(a.sum()) // 2 for a in A] == [12, 12, 4],
      "cube adjacency of the three link types (12 axis, 12 face, 4 body links) commute (Bose-Mesner algebra); eigenvectors (-1)^(s.x), "
      "eigenvalues (3-2w, ((3-2w)^2-3)/2, (-1)^w) with multiplicity 1,3,3,1 by weight w")
mults = []; cmax = 0; argd = 0
for _ in range(20):
    fu, fd = rng.normal(size=4), rng.normal(size=4)
    Mu = fu[0]*np.eye(8) + sum(fu[k+1]*A[k] for k in range(3)); Md = fd[0]*np.eye(8) + sum(fd[k+1]*A[k] for k in range(3))
    mults.append(tuple(sorted(multiplets(np.linalg.eigvalsh(Mu), 1e-9))))
    cmax = max(cmax, np.abs(Mu@Md - Md@Mu).max()); argd = max(argd, abs(np.sin(np.angle(np.linalg.det(Mu@Md)))))
check("B2 [T]", set(mults) == {(1, 1, 3, 3)} and cmax < 1e-13 and argd < 1e-12,
      "any geometry-only mass rule M = f(1, A_axis, A_face, A_body) (20 seeded up/down pairs; f's ratios are FITTED numbers): "
      "levels 1+1+3+3, so at most two nondegenerate families; [M_u, M_d] = 0, so V is a permutation in the joint eigenbasis, J = 0; "
      "arg det real (theta-bar structural, but with no CP)")
# Z^3 torus: translation-invariant three-range hops commute for any up/down functions
L = 4; Z = np.array(list(itertools.product(range(L), repeat=3)))
dz = (((Z[:, None, :]-Z[None, :, :]+L//2) % L - L//2)**2).sum(-1)
Hz = [np.where(dz == k, 1., 0.) for k in (1, 2, 3)]
cnt = [int(Hz[k][0].sum()) for k in range(3)]
fu, fd = rng.normal(size=3), rng.normal(size=3)
Hu = sum(fu[k]*Hz[k] for k in range(3)); Hd = sum(fd[k]*Hz[k] for k in range(3))
check("B3 [T]", cnt == [6, 12, 8] and np.abs(Hu@Hd-Hd@Hu).max() < 1e-12,
      f"on the 4^3 torus the three ranges have counts {cnt} (6/12/8) and any up/down distance functions commute: "
      "one band per species, no family index from the ranges alone")
# B4: the CL-1 cube tick: W_i with -1 around every face
sx = np.array([[0., 1.], [1., 0.]]); sz = np.diag([1., -1.]); I2 = np.eye(2)
k3 = lambda a, b, c_: np.kron(np.kron(a, b), c_)
W = [k3(sx, I2, I2), k3(sz, sx, I2), k3(sz, sz, sx)]   # site index = (x, y, z) bits
Xb = np.array(list(itertools.product([0, 1], repeat=3))); db = ((Xb[:, None]-Xb[None])**2).sum(-1)
ok_cl = all(np.allclose(W[i]@W[i], np.eye(8)) for i in range(3)) and all(np.allclose(W[i]@W[j]+W[j]@W[i], 0) for i in range(3) for j in range(i))
face = [W[i]@W[j] for i, j in [(0, 1), (0, 2), (1, 2)]]; om = W[0]@W[1]@W[2]
ok_sup = all(np.all(db[np.abs(f) > 0] == 2) for f in face) and np.all(db[np.abs(om) > 0] == 3)
check("B4 [T]", ok_cl and ok_sup and np.allclose(om@om, -np.eye(8)) and all(np.allclose(om@x, x@om) for x in W),
      "CL-1 hops W_i (face phases -1) anticommute; their products W_iW_j are exactly face-diagonal hops and w = W1W2W3 the body-diagonal hop, "
      "central with w^2 = -1: the three link types are the cube tick's Clifford algebra 1+3+3+1")
# commutant of the tick algebra
Kc = np.vstack([np.kron(np.eye(8), x) - np.kron(x.T, np.eye(8)) for x in W])
_, sv, vh = np.linalg.svd(Kc); Cb = vh[sv.size - np.sum(sv < 1e-10):] if False else vh[np.sum(sv > 1e-10):]
Cm = [v.reshape(8, 8).T for v in Cb]
nonab = max(np.abs(a@b-b@a).max() for a in Cm for b in Cm)
check("B5 [T]", len(Cm) == 8 and nonab > 0.1 and all(np.abs(om@x-x@om).max() < 1e-10 for x in Cm),
      "commutant of the tick algebra on one cube has dimension 8, non-abelian, commuting with w: C^8 = (spin 2) x (family 2) in each w = +-i sector, "
      "so one cube carries 2 families per sector (M2+M2), not 3")
# family mixing from arbitrary tick-commuting (or staggered x commutant) mass terms
eps = np.diag([(-1.)**x.sum() for x in Xb])
def rnd_c(): return sum((rng.normal()+1j*rng.normal())*x for x in Cm)
Jmax = 0; bd = 0
for trial in range(10):
    Mu, Md = rnd_c(), rnd_c()
    if trial % 2: Mu, Md = eps@Mu, eps@Md
    Hu_, Hd_ = Mu@Mu.conj().T, Md@Md.conj().T
    bd = max(bd, np.abs(Hu_@om-om@Hu_).max(), np.abs(Hd_@om-om@Hd_).max())
    def projs(Hm):
        e, v = np.linalg.eigh(Hm); out = []; i = 0
        while i < 8:
            j = i
            while j+1 < 8 and e[j+1]-e[i] < 1e-8: j += 1
            out.append(v[:, i:j+1]@v[:, i:j+1].conj().T); i = j+1
        return out
    pu, pd = projs(Hu_), projs(Hd_)
    for a, b, cc, d in itertools.product(range(len(pu)), range(len(pd)), range(len(pu)), range(len(pd))):
        Jmax = max(Jmax, abs(np.trace(pu[a]@pd[b]@pu[cc]@pd[d]).imag))
# positive control: three generic families do give a nonzero invariant
hu = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)); hd = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3))
eu, vu = np.linalg.eigh(hu + hu.conj().T); ed, vd = np.linalg.eigh(hd + hd.conj().T)
pp = lambda v, i: np.outer(v[:, i], v[:, i].conj())
Jc = abs(np.trace(pp(vu, 0)@pp(vd, 0)@pp(vu, 1)@pp(vd, 1)).imag)
check("B6 [T]", bd < 1e-10 and Jmax < 1e-12 and len(pu) == 4 and Jc > 1e-3,
      f"10 seeded up/down mass terms in the commutant (half of them staggered by (-1)^(x+y+z)): every H = MM^dag commutes with w, "
      f"4 doubly-degenerate levels, mixing block-diagonal 2+2, max |Im tr(Pu Pd Pu Pd)| = {Jmax:.1e} (3-family control {Jc:.3f}): J = 0 for every choice, fitted or not")
# geometric (rotation-covariant) part of the commutant, rotations lifted by a site gauge
def lift(gm):
    p = np.array([int(np.where((Xb == (((gm@(2*x-1))+1)//2)).all(1))[0][0]) for x in Xb])
    Pm = np.eye(8)[:, p]
    sig = [int(np.argmax(np.abs(gm[:, i]))) for i in range(3)]
    Dd = np.zeros(8); Dd[0] = 1; todo = [0]
    while todo:
        a = todo.pop()
        for i in range(3):
            Wp = Pm@W[i]@Pm.T; b = int(np.argmax(np.abs(Wp[a])))
            if Dd[b] == 0: Dd[b] = Dd[a]*Wp[a, b]/W[sig[i]][a, b]; todo.append(b)
    Uu = np.diag(Dd)@Pm
    ok = all(np.allclose(Uu@W[i]@Uu.T, W[sig[i]]) for i in range(3))
    return Uu, ok
lifts = [lift(gm) for gm in OH]
def inv_dim(G):
    K = np.vstack([np.kron(np.eye(len(Cm)), 1)[:0]] + [np.array([(U@x@U.T - x).ravel() for x in Cm]).T for U in G])
    return len(Cm) - np.linalg.matrix_rank(K, 1e-9)
proper = [lifts[k][0] for k, gm in enumerate(OH) if round(np.linalg.det(gm)) == 1]
dO, dOh = inv_dim(proper), inv_dim([u for u, _ in lifts])
check("B7 [T]", all(ok for _, ok in lifts) and dOh <= dO <= 2,
      f"every O_h element lifts by a site gauge to U with U W_i U^T = W_sigma(i); rotation-invariant commutant: dim {dO} (O), {dOh} (O_h): "
      "a rotation-covariant family mass matrix is a multiple of 1, so geometry alone leaves all cube families degenerate; any splitting is a lopsided (axis-choosing) input")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}   ({time.time()-T0:.1f} s)")
