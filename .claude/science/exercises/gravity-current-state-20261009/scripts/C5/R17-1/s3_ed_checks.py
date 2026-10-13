"""R17-1 s3 (written before running). Exact diagonalization checks, label probe, f-sum via
m1 = <C^dag (H-E0) C> + <C (H-E0) C^dag>, chi = sum (|C_n0|^2+|C^dag_n0|^2)/omega_n (sparse solve).
 (i)  CONTROL: 3D Z2 toric code + electric field, H = -K sum_p B_p - h sum_l X_l, on the 2x2x2 torus,
      Gauss sector reachable from n=0 (B_p = flip of the 4 links of p). Transverse label probe.
      The method must not report a gapless photon: expect m1(k) = O(1) (k^0) and a gap.
 (ii) TENSOR: Z2 cube model H = -K sum_c Z^{cube c} - h sum_f X_f on face slots (cube = 6 faces, s1/s2).
      (a) duality check on 2x2x2: face-basis BFS spectrum vs 3D TFIM H = -K sum tau^x - h sum_{faces} tau^z tau^z.
      (b) 3x3x2 torus (largest feasible: 18 cubes, 2^18 TFIM states): gap, m1(k), chi_TT(k) at the allowed k,
          h/K in {0, 0.1, 0.2, 0.3}. Size limit: 3x3x2; no extrapolation.
 (iii) dipole hop (cube_x -> cube_{x+a}) on 2x2x3 torus, zero sector, BFS from one flipped cube:
      identity m1(k) = (-<H>/V)|chat.delta(k)|^2 summed over a, and E0 < 0.
"""
import numpy as np, itertools, scipy.sparse as sp, scipy.sparse.linalg as sla
rng = np.random.default_rng(0)
E3 = np.eye(3, dtype=int)
def ground(H):
    w, v = sla.eigsh(H, k=3, which='SA', tol=1e-12, ncv=40); o = np.argsort(w); return w[o], v[:, o]
def fsum_chi(H, E0, psi, Cdiag):
    Cp = Cdiag*psi; Cm = np.conj(Cdiag)*psi
    Hs = H - E0*sp.identity(H.shape[0])
    m1 = np.real(np.vdot(Cp, Hs @ Cp) + np.vdot(Cm, Hs @ Cm))
    chi = 0.0
    for b in (Cp, Cm):
        b = b - psi*np.vdot(psi, b)
        xr, info = sla.minres(Hs, np.real(b), rtol=1e-11, maxiter=20000)
        xi, info = sla.minres(Hs, np.imag(b), rtol=1e-11, maxiter=20000)
        x = xr + 1j*xi
        x = x - psi*np.vdot(psi, x); chi += np.real(np.vdot(b, x))
    return m1, chi
def bfs(n_slots, flips, start=0):
    idx = {start: 0}; order = [start]; i = 0
    while i < len(order):
        c = order[i]; i += 1
        for f in flips:
            d = c ^ f
            if d not in idx: idx[d] = len(order); order.append(d)
    return idx, order
def build_flip_H(idx, order, flips, K, diag):
    rows, cols, vals = [], [], []
    for a, c in enumerate(order):
        for f in flips: rows.append(idx[c ^ f]); cols.append(a); vals.append(-K)
    D = sp.diags([diag(c) for c in order])
    return sp.csr_matrix((vals, (rows, cols)), shape=(len(order),)*2) + D
# ---------------- (i) toric code control
L = 2
links = [(x, d) for x in itertools.product(range(L), repeat=3) for d in range(3)]
lidx = {l: n for n, l in enumerate(links)}
def lk(x, d): return lidx[(tuple(np.mod(x, L)), d)]
plaq = []
for x in itertools.product(range(L), repeat=3):
    for a, b in [(0,1),(1,2),(0,2)]:
        x = np.array(x); ls = [lk(x, a), lk(x + E3[a], b), lk(x + E3[b], a), lk(x, b)]
        m = 0
        for l in ls: m ^= (1 << l)
        plaq.append(m)
plaq = list(set(plaq))
idx, order = bfs(len(links), plaq)
print("(i) toric code 2x2x2: links %d, distinct plaquette flips %d, sector dim %d" % (len(links), len(plaq), len(order)))
lpos = [np.array(x, float) + 0.5*E3[d] for (x, d) in links]
nmat = np.array([[(c >> l) & 1 for l in range(len(links))] for c in order], float)
for h in [0.0, 0.2, 0.5]:
    H = build_flip_H(idx, order, plaq, 1.0, lambda c: -h*sum(1 - 2*((c >> l) & 1) for l in range(len(links))))
    w, v = ground(H); psi = v[:, 0]
    out = []
    for k, eps in [(np.zeros(3), (1,0,0)), (np.array([0, np.pi, 0]), (1,0,0)), (np.array([0, 0, np.pi]), (1,0,0)),
                   (np.array([np.pi, np.pi, 0]), (0,0,1))]:
        cvec = np.array([np.exp(1j*k @ lpos[l])*eps[links[l][1]] for l in range(len(links))])/np.sqrt(L**3)
        m1, chi = fsum_chi(H, w[0], psi, nmat @ cvec)
        out.append("k=%s e=%s: m1=%.5f chi=%.5f" % (np.round(k/np.pi, 2), eps, m1, chi))
    print("  h=%.1f E0=%.6f gap=%.5f | %s" % (h, w[0], w[1]-w[0], " | ".join(out)))
print("  (U(1) contrast, identity) circulation delta = +x(x) +y(x+ex) -x(x+ey) -y(x): M0 = 0 exactly, so its k=0 f-sum is 0.")
# ---------------- (ii) cube model
def faces_cubes(Ls):
    faces = [(x, t) for x in itertools.product(*[range(l) for l in Ls]) for t in range(3)]  # t: 0=xy,1=yz,2=xz
    fidx = {f: n for n, f in enumerate(faces)}
    TT = [(0,1),(1,2),(0,2)]
    def fk(x, t): return fidx[(tuple(np.mod(x, Ls)), t)]
    cubes = []
    for x in itertools.product(*[range(l) for l in Ls]):
        x = np.array(x)
        fs = [fk(x, 0), fk(x + E3[2], 0), fk(x, 1), fk(x + E3[0], 1), fk(x, 2), fk(x + E3[1], 2)]
        cubes.append(fs)
    fpos = [np.array(x, float) + 0.5*(E3[TT[t][0]] + E3[TT[t][1]]) for (x, t) in faces]
    return faces, cubes, fpos, TT
for Ls in [(2,2,2)]:
    faces, cubes, fpos, TT = faces_cubes(Ls)
    flips = []
    for fs in cubes:
        m = 0
        for f in fs: m ^= (1 << f)
        flips.append(m)
    idx, order = bfs(len(faces), flips)
    h = 0.3
    H = build_flip_H(idx, order, flips, 1.0, lambda c: -h*sum(1 - 2*((c >> f) & 1) for f in range(len(faces))))
    wf = np.sort(np.linalg.eigvalsh(H.toarray()))[:6]
    # TFIM on cubes: bonds = faces (each face in exactly two cubes)
    nc = len(cubes); fc = {}
    for c, fs in enumerate(cubes):
        for f in fs: fc.setdefault(f, []).append(c)
    dim = 2**nc; states = np.arange(dim)
    bits = ((states[:, None] >> np.arange(nc)) & 1)
    zz = sum(1 - 2*(bits[:, fc[f][0]] ^ bits[:, fc[f][1]]) for f in range(len(faces)))
    rows = np.concatenate([states ^ (1 << c) for c in range(nc)]); cols = np.tile(states, nc)
    HT = sp.csr_matrix((-np.ones(len(rows)), (rows, cols)), shape=(dim, dim)) + sp.diags(-h*zz.astype(float))
    Hd = HT.toarray(); reps = [s_ for s_ in range(dim) if s_ < (s_ ^ (dim - 1))]
    B = np.zeros((dim, len(reps)))
    for n_, s_ in enumerate(reps): B[s_, n_] = B[s_ ^ (dim - 1), n_] = 1/np.sqrt(2)
    we = np.sort(np.linalg.eigvalsh(B.T @ Hd @ B))[:6]
    print("\n(ii-a) 2x2x2 duality (h/K=0.3): face-basis sector dim %d ; lowest: %s" % (len(order), np.round(wf, 8)))
    print("       TFIM Z2-even sector dim %d ; lowest:   %s" % (len(reps), np.round(we, 8)))
# (ii-b) 3x3x2 via TFIM (Z2-even ground state is the unique ground state at finite size)
Ls = (3,3,2)
faces, cubes, fpos, TT = faces_cubes(Ls)
nc = len(cubes); fc = {}
for c, fs in enumerate(cubes):
    for f in fs: fc.setdefault(f, []).append(c)
dim = 2**nc; states = np.arange(dim, dtype=np.int64)
nf = np.zeros((dim, len(faces)), np.int8)
for f in range(len(faces)):
    nf[:, f] = ((states >> fc[f][0]) & 1) ^ ((states >> fc[f][1]) & 1)
rows = np.concatenate([states ^ (1 << c) for c in range(nc)]); cols = np.tile(states, nc)
Hx = sp.csr_matrix((-np.ones(len(rows)), (rows, cols)), shape=(dim, dim))
def tt_pols(kh):
    kh = kh/np.linalg.norm(kh); a = np.array([1.0, 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1.0, 0])
    u = np.cross(kh, a); u /= np.linalg.norm(u); v = np.cross(kh, u)
    return [(np.outer(u,u) - np.outer(v,v))/np.sqrt(2), (np.outer(u,v) + np.outer(v,u))/np.sqrt(2)]
kl = [np.array([2*np.pi/3, 0, 0]), np.array([2*np.pi/3, 2*np.pi/3, 0]), np.array([0, 0, np.pi]), np.array([2*np.pi/3, 0, np.pi])]
V = np.prod(Ls)
print("\n(ii-b) cube model on 3x3x2 torus (18 cubes, 54 face slots; TFIM dim %d)" % dim)
for h in [0.0, 0.1, 0.2, 0.3]:
    zz = (1 - 2*nf.astype(float)).sum(1)
    H = Hx + sp.diags(-h*zz)
    w, v = ground(H); psi = v[:, 0]
    res = []
    for k in kl:
        for pi, eps in enumerate(tt_pols(k)):
            c = np.array([np.exp(1j*k @ fpos[f])*2*eps[TT[faces[f][1]]] for f in range(len(faces))])/np.sqrt(V)
            m1, chi = fsum_chi(H, w[0], psi, nf.astype(float) @ c)
            exact0 = 8*sum(eps[i, j]**2 for i, j in TT)
            res.append("k/pi=%s p%d m1=%.4f (h=0 exact %.4f) chi=%.4f" % (np.round(k/np.pi, 2), pi, m1, exact0, chi))
    print("  h/K=%.1f E0/V=%.6f gap=%.5f" % (h, w[0]/V, w[1]-w[0]))
    for r in res: print("     " + r)
# ---------------- (iii) dipole hop on 2x2x3, zero sector
Ls = (2,2,3)
faces, cubes, fpos, TT = faces_cubes(Ls)
V = np.prod(Ls)
def cidx(x): return int(np.ravel_multi_index(tuple(np.mod(x, Ls)), Ls))
xs = list(itertools.product(*[range(l) for l in Ls]))
terms = []  # (plus_mask, minus_mask, a)
for x in xs:
    for a in range(3):
        c1 = set(cubes[cidx(np.array(x))]); c2 = set(cubes[cidx(np.array(x) + E3[a])])
        if c1 == c2: continue
        plus = 0; minus = 0
        for f in c1 - c2: plus |= (1 << f)
        for f in c2 - c1: minus |= (1 << f)
        terms.append((plus, minus, a, x))
start = 0
for f in cubes[0]: start ^= (1 << f)
idx = {start: 0}; order = [start]; i = 0
while i < len(order):
    c = order[i]; i += 1
    for plus, minus, a, x in terms:
        for p, m in [(plus, minus), (minus, plus)]:
            if (c & p) == 0 and (c & m) == m:
                d = c ^ p ^ m
                if d not in idx: idx[d] = len(order); order.append(d)
rows, cols = [], []
for j, c in enumerate(order):
    for plus, minus, a, x in terms:
        for p, m in [(plus, minus), (minus, plus)]:
            if (c & p) == 0 and (c & m) == m: rows.append(idx[c ^ p ^ m]); cols.append(j)
H = sp.csr_matrix((-np.ones(len(rows)), (rows, cols)), shape=(len(order),)*2)
w, v = ground(H) if len(order) > 4 else (np.linalg.eigvalsh(H.toarray()), None)
psi = v[:, 0]
print("\n(iii) dipole hop on 2x2x3 torus, one flipped cube: reachable dim %d ; E0 = %.6f ; -E0/V = %.6f" % (len(order), w[0], -w[0]/V))
nmat = np.array([[(c >> f) & 1 for f in range(len(faces))] for c in order], float)
for k in [np.array([np.pi, 0, 0]), np.array([0, 0, 2*np.pi/3]), np.array([np.pi, np.pi, 2*np.pi/3])]:
    for pi, eps in enumerate(tt_pols(k)):
        cf = np.array([np.exp(1j*k @ fpos[f])*2*eps[TT[faces[f][1]]] for f in range(len(faces))])/np.sqrt(V)
        m1, chi = fsum_chi(H, w[0], psi, nmat @ cf)
        # identity: sum over terms of w_term |chat.delta|^2 with w_term = <T + T^dag>
        pred = 0.0
        for plus, minus, a, x in terms:
            Tm = np.zeros(len(order))
            ex = 0.0
            for p, m in [(plus, minus), (minus, plus)]:
                for j, c in enumerate(order):
                    if (c & p) == 0 and (c & m) == m: ex += psi[idx[c ^ p ^ m]]*psi[j]
            dl = np.zeros(len(faces))
            for f in range(len(faces)):
                if (plus >> f) & 1: dl[f] = 1
                if (minus >> f) & 1: dl[f] = -1
            pred += ex*abs(np.sum(dl*cf*np.sqrt(V)))**2/V
        print("  k/pi=%s p%d: m1(ED)=%.6e  identity sum_delta w|chat.delta|^2 = %.6e  chi=%.4e" % (np.round(k/np.pi, 2), pi, m1, pred, chi))
