#!/usr/bin/env python3
"""monopole-families: is the family count the Dirac index of the spin-S coherent-overlap (Berry) monopole on a block
boundary (families-brainstorm R1), with S = 3/2 from CL-1's cube-covariant hop, so that 2S = 3 light copies appear?
 A  Berry flux of spin-S coherent overlaps on the refined cube surface: plaquette flux = S x geodesic area (exact),
    face flux 2 pi S/3, Chern number 2S for N >= 2; N = 1 (S = 3/2) has pi per face: cube-symmetric lifts C in 3 + 6Z.
 B  surface staggered Dirac operator H1 = CL-1's '-1 around every unit face' (Z^3 staggered phases restricted to the
    boundary of [0,N]^3) x the overlap phases: near-zero count, exact sublattice kernel, gap x N.
 C  controls: S = 0 (CL-1's own surface field, no monopole) and H0 (monopole phases without the -1 faces).
 D  10% random real hop disorder.
 E  the 24 rotations (permutation x site gauge solved on a spanning tree) on the near-zero space: |chi| by class,
    irreducibility, half-turn commutation (ordinary vs double cover), three-fold turn eigenvalues.
Labels: [T] exact, [F] finite diagnostic. Supplied: the smooth spin-S field on the block boundary (not CL-1's own
fine-rung field), the radial coherent-state map, the choice of the minimal lift S = 3/2 (C = 3 rather than 3 + 6m)."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

def Smat(S):
    m = np.arange(S, -S - 1, -1); d = len(m); Sp = np.zeros((d, d))
    for i in range(1, d): Sp[i - 1, i] = np.sqrt(S * (S + 1) - m[i] * (m[i] + 1))
    return [(Sp + Sp.T) / 2 + 0j, (Sp - Sp.T) / 2j, np.diag(m) + 0j]
def coh(Sm, n):
    _, v = np.linalg.eigh(n[0] * Sm[0] + n[1] * Sm[1] + n[2] * Sm[2]); return v[:, -1]

SURF = {}
def surface(N):
    if N in SURF: return SURF[N]
    pts = [p for p in itertools.product(range(N + 1), repeat=3) if any(c in (0, N) for c in p)]
    idx = {p: i for i, p in enumerate(pts)}; E = []
    for p in pts:
        for a in range(3):
            q = list(p); q[a] += 1; q = tuple(q)
            if q in idx and any(p[b] == q[b] and p[b] in (0, N) for b in range(3) if b != a): E.append((idx[p], idx[q], a))
    P = []; face = []
    for ax in range(3):
        for sg, v in ((1, N), (-1, 0)):
            u = [b for b in range(3) if b != ax]
            if (u[0], u[1]) not in [(1, 2), (2, 0), (0, 1)]: u = u[::-1]
            if sg < 0: u = u[::-1]                                    # outward orientation
            for i in range(N):
                for j in range(N):
                    loop = []
                    for di, dj in ((0, 0), (1, 0), (1, 1), (0, 1)):
                        q = [0, 0, 0]; q[ax] = v; q[u[0]] = i + di; q[u[1]] = j + dj; loop.append(idx[tuple(q)])
                    P.append(loop); face.append(2 * ax + (sg < 0))
    par = np.array([sum(p) % 2 for p in pts])
    SURF[N] = (pts, idx, E, P, np.array(face), par); return SURF[N]

def build(N, S, eta=True, dis=0.0):
    pts, idx, E, P, face, par = surface(N); n = len(pts); c = np.full(3, N / 2)
    st = None
    if S > 0:
        Sm = Smat(S); st = [coh(Sm, (np.array(p) - c) / np.linalg.norm(np.array(p) - c)) for p in pts]
    H = np.zeros((n, n), complex)
    for i, j, a in E:
        u = 1.0
        if S > 0: u = np.vdot(st[i], st[j]); u /= abs(u)
        p = pts[i]; e = [1, (-1) ** p[0], (-1) ** (p[0] + p[1])][a] if eta else 1
        w = 1 + dis * rng.uniform(-1, 1) if dis else 1
        H[i, j] = e * u * w; H[j, i] = np.conj(H[i, j])
    return H
def fluxes(H, P):
    return np.array([np.angle(H[l[0], l[1]] * H[l[1], l[2]] * H[l[2], l[3]] * H[l[3], l[0]]) for l in P])

NS = range(1, 9); SS = (0.5, 1, 1.5, 2)
# ------------------------------------------------------------------ A
print("== A. Berry flux of the spin-S coherent-overlap field on the refined cube surface (6N^2+2 sites)")
sp = Smat(0.5); dev = 0
for S in SS:
    Sm = Smat(S)
    for _ in range(20):
        a, b = rng.normal(size=(2, 3)); a /= np.linalg.norm(a); b /= np.linalg.norm(b)
        x = np.vdot(coh(Sm, a), coh(Sm, b)); y = np.vdot(coh(sp, a), coh(sp, b)) ** int(2 * S)
        dev = max(dev, abs(abs(x) - abs(y)))
check("A1 [T] |<a|b>_S| = |<a|b>_1/2|^(2S) (spin-S coherent state = symmetric 2S-fold product), so every overlap loop "
      "phase is 2S x the spin-1/2 Pancharatnam phase = S x geodesic area; grid lines on a face project to great circles",
      dev < 1e-12, f"max dev {dev:.1e}")
Ctab = {}; fdev = 0; pmax = 0
for S in SS:
    for N in NS:
        pts, idx, E, P, face, par = surface(N); F = fluxes(build(N, S, eta=False), P)
        Ctab[S, N] = F.sum() / (2 * np.pi)
        if N >= 2:
            fdev = max(fdev, max(abs(F[face == f].sum() - 2 * np.pi * S / 3) for f in range(6))); pmax = max(pmax, abs(F).max())
okC = all(abs(Ctab[S, N] - 2 * S) < 1e-9 for S in SS for N in NS if N >= 2)
check("A2 [T] for every N = 2..8 and S = 1/2, 1, 3/2, 2: each face carries exactly 2 pi S/3, no plaquette exceeds pi, "
      "and the Chern number C = 2S", okC and fdev < 1e-9 and pmax < np.pi - 0.1,
      f"face dev {fdev:.1e}; max |plaquette| {pmax:.2f} rad; C(S=3/2) = " + ",".join(f"{Ctab[1.5, N]:+.0f}" for N in NS))
pts, idx, E, P, face, par = surface(1); F1 = fluxes(build(1, 1.5, eta=False), P)
check("A3 [T] N = 1 (CL-1's bare cell), S = 3/2: every face flux is exactly pi (= CL-1's -1 face phase); the principal "
      "branch sums to C = -1 (a non-symmetric lift); rotation-symmetric lifts give one m for all six faces, C = 3(1+2m): "
      "|C| = 3 is the minimal symmetric lift, the sign and m are not fixed by the cell",
      np.allclose(abs(F1), np.pi) and round(Ctab[1.5, 1]) == -1, f"face |flux|/pi = {np.round(abs(F1) / np.pi, 12)}; C = {Ctab[1.5, 1]:+.3f}")

# ------------------------------------------------------------------ B, C
print("== B. surface staggered Dirac H1 = (-1 faces) x (overlap phases); N_0 = levels below half the S=0 first level")
def spec(H): return np.sort(abs(np.linalg.eigvalsh(H)))
thr = {}
for N in NS:
    e0 = spec(build(N, 0)); thr[N] = 0.5 * e0[e0 > 1e-8][0]
def n0(e, N): return int((e < thr[N]).sum())
def kern(H, par):
    T = H[np.ix_(par == 0, par == 1)]; s = np.linalg.svd(T, compute_uv=False); r = int((s > 1e-9).sum())
    return (T.shape[0] - r, T.shape[1] - r)
R = {}
for S in (0,) + SS:
    for N in NS:
        pts, idx, E, P, face, par = surface(N); H = build(N, S); e = spec(H); k = n0(e, N)
        R[S, N] = (k, e[k], e[k - 1] if k else 0.0, kern(H, par), int((par == 0).sum() - (par == 1).sum()))
for S in (0,) + SS:
    print(f"  S={S}: N_0 by N=1..8: " + " ".join(f"{R[S, N][0]}" for N in NS) + " | kernel (even,odd) " +
          " ".join(f"{R[S, N][3][0]},{R[S, N][3][1]}" for N in NS))
okN = all(R[S, N][0] == 4 * S for S in SS for N in NS if N >= 2)
check("B1 [F] near-zero count N_0 = 2|C| = 4S for every S >= 1/2 and N = 2..8 (two staggered tastes, each seeing the "
      "monopole): S = 3/2 gives SIX, not three", okN, "S=3/2: " + ",".join(str(R[1.5, N][0]) for N in NS))
okK = all(R[S, N][3] == ((2 * S + 1, 2 * S - 1) if N % 2 == 0 else R[S, N][3]) for S in SS for N in NS if N >= 2)
imb = [R[0, N][4] for N in NS]
check("B2 [T] exact sublattice kernel: n_even - n_odd = 2 (N even: all 8 corners even) or 0 (N odd), flux-independent; "
      "for even N the kernel is (C+1, C-1): the eps-index is 2, the taste-summed count 2C; one sublattice never holds 2S",
      okK and imb == [0 if N % 2 else 2 for N in NS], "imbalance " + ",".join(map(str, imb)) + "; S=3/2 even N: " +
      " ".join(str(R[1.5, N][3]) for N in (2, 4, 6, 8)))
gN = [R[1.5, N][1] * N for N in NS if N >= 2]; ratio = [R[1.5, N][1] / max(R[1.5, N][2], 1e-3) for N in (3, 5, 7)]
check("B3 [F] S = 3/2 gap to the next level ~ 1/N (gap x N -> const, monotone for N >= 4); odd-N zero-band width falls "
      "faster than the gap (gap/width grows)", all(np.diff(gN[2:]) > -0.02) and abs(gN[-1] - gN[-2]) < 0.1 and
      ratio[0] < ratio[1] < ratio[2], "gap x N (N=2..8): " + ",".join(f"{g:.2f}" for g in gN) +
      "; odd gap/width " + ",".join(f"{r:.0f}" for r in ratio))
check("C1 [F] control S = 0 (CL-1's own surface field, pi per unit face, no extra monopole): N_0 = 0 (odd N) or 2 = the "
      "graph imbalance (even N): CL-1's own block boundary carries no 3", all(R[0, N][0] == (0 if N % 2 else 2) for N in NS),
      "N_0 = " + ",".join(str(R[0, N][0]) for N in NS))
gH0 = []
for N in (4, 6, 8):
    e = spec(build(N, 1.5, eta=False)); gH0.append(e[6] * N)
check("C2 [F] control H0 (overlap phases without the -1 faces): no Dirac structure; the level after the six lowest "
      "closes faster than 1/N (square-lattice Fermi line at E = 0), so no isolated index band", gH0[0] > gH0[1] > gH0[2],
      "level-7 x N at N=4,6,8: " + ",".join(f"{g:.3f}" for g in gH0))

# ------------------------------------------------------------------ D
print("== D. 10% random real hop disorder (|hop| x (1 + 0.1 u)), 3 seeds per N")
okD = True; wmax = 0; gmin = 9
for N in range(2, 9):
    pts, idx, E, P, face, par = surface(N)
    for _ in range(3):
        H = build(N, 1.5, dis=0.1); e = spec(H); k = n0(e, N); kz = int((e < 1e-9).sum())
        okD &= (k == 6) and (kz >= abs(R[0, N][4])); wmax = max(wmax, e[5] * N); gmin = min(gmin, e[6] * N)
check("D1 [F] S = 3/2: N_0 = 6 for every N = 2..8 and seed; exact zeros >= graph imbalance (protected), the rest split "
      "but stay far below the gap", okD and wmax < 0.3 * gmin, f"max width x N {wmax:.2f}, min gap x N {gmin:.2f}")

# ------------------------------------------------------------------ E
print("== E. the 24 cube rotations on the near-zero space (gauge-compensated, projective)")
ROT = [np.array(M) for M in (np.diag(s) @ np.eye(3)[list(p)] for p in itertools.permutations(range(3))
                             for s in itertools.product((1, -1), repeat=3)) if np.linalg.det(M) > 0]
def cls(M):
    t = round(np.trace(M))
    return {3: 'E', 0: 'C3', 1: 'C4'}.get(t, 'C2' if np.allclose(M, np.diag(np.diag(M))) else "C2'")
def rot_ops(N, H):
    pts, idx, E, P, face, par = surface(N); n = len(pts); c = np.full(3, N / 2); ops = []
    adj = [[] for _ in range(n)]
    for i, j, a in E: adj[i].append(j); adj[j].append(i)
    for M in ROT:
        pi = np.array([idx[tuple(int(round(x)) for x in M @ (np.array(p) - c) + c)] for p in pts])
        Pm = np.zeros((n, n)); Pm[pi, np.arange(n)] = 1; Hp = Pm @ H @ Pm.T
        g = np.zeros(n, complex); g[0] = 1; stack = [0]
        while stack:
            a = stack.pop()
            for b in adj[a]:
                if g[b] == 0: g[b] = np.conj(H[a, b] / Hp[a, b] / g[a]); stack.append(b)
        O = np.diag(g) @ Pm; ops.append((cls(M), M, O, np.abs(O @ H @ O.conj().T - H).max()))
    return ops
def rep(N, S):
    H = build(N, S); w, v = np.linalg.eigh(H); k = int(4 * S); V = v[:, np.argsort(abs(w))[:k]]
    ops = rot_ops(N, H); out = {}; cdev = 0; leak = 0
    for name, M, O, d in ops:
        Mr = V.conj().T @ O @ V; cdev = max(cdev, d); leak = max(leak, abs(np.abs(np.linalg.eigvals(Mr)) - 1).max())
        out.setdefault(name, []).append((M, Mr))
    chi = {c: round(abs(np.trace(out[c][0][1])), 6) for c in ('E', 'C3', 'C4', 'C2', "C2'")}
    irr = sum(abs(np.trace(Mr)) ** 2 for c in out for _, Mr in out[c]) / 24
    hx = [Mr for M, Mr in out['C2'] if M[0, 0] > 0][0]; hy = [Mr for M, Mr in out['C2'] if M[1, 1] > 0][0]
    comm = np.linalg.norm(hx @ hy - hy @ hx) / np.linalg.norm(hx @ hy); anti = np.linalg.norm(hx @ hy + hy @ hx) / np.linalg.norm(hx @ hy)
    t3 = out['C3'][0][1]; ev = np.linalg.eigvals(t3); ph = np.sort(np.round((np.angle(ev / ev[0]) / (2 * np.pi / 3) + 0.5) % 3 - 0.5, 3)) % 3
    return chi, irr, comm, anti, ph, cdev, leak
ctl = {}
for N, S in ((3, 0.5), (4, 0.5), (3, 1), (4, 1)):
    chi, irr, comm, anti, ph, cdev, leak = ctl[N, S] = rep(N, S)
    print(f"  S={S} N={N}: |chi| " + ",".join(f"{c}:{chi[c]:.3g}" for c in chi) + f"  sum|chi|^2/24={irr:.2f}  "
          f"half-turns {'commute' if comm < 1e-8 else ('anticommute' if anti < 1e-8 else 'neither')}")
res = {N: rep(N, 1.5) for N in (3, 5, 4, 6)}
okR = all(r[5] < 1e-10 and r[6] < 1e-8 for r in res.values())
check("E1 [T] every rotation is a site permutation times a site gauge commuting with H1 (sphere: fluxes fix the gauge "
      "class) and leaves the near-zero space invariant", okR, f"max |[O,H]| {max(r[5] for r in res.values()):.1e}")
for N in (3, 5, 4, 6):
    chi, irr, comm, anti, ph, cdev, leak = res[N]
    print(f"  S=3/2 N={N}: |chi| " + ",".join(f"{c}:{chi[c]:.3g}" for c in chi) + f"  sum|chi|^2/24={irr:.2f}  half-turns "
          f"{'commute' if comm < 1e-8 else ('anticommute' if anti < 1e-8 else 'neither')}  C3 eigen-ratios (units w): {ph}")
odd = [res[N] for N in (3, 5)]; even = [res[N] for N in (4, 6)]
c1, c2 = ctl[3, 0.5], ctl[3, 1]
check("E2 [F] odd-N controls: the two tastes form the doublet E of O (90-degree turns swap the sublattices): S = 1/2 "
      "gives E (irreducible, ordinary), S = 1 gives E x E1/2' = G' (irreducible, half-turns anticommute)",
      abs(c1[1] - 1) < 1e-6 and c1[2] < 1e-8 and abs(c1[0]['C3'] - 1) < 1e-6 and abs(c2[1] - 1) < 1e-6 and c2[3] < 1e-8)
check("E3 [F] odd N, S = 3/2: the six modes are T1 + T2 = E x T1 (|chi| = 6,0,0,2,0 on E,C3,C4,C2,C2'; sum|chi|^2/24 = 2; "
      "ordinary): two triplets (continuum j = 1 per taste, the tastes differing by A2); in each the three-fold turn has "
      "eigenvalues {1, w, w^2}: the copies do NOT share one turn eigenvalue",
      all(r[0] == {'E': 6, 'C3': 0, 'C4': 0, 'C2': 2, "C2'": 0} and abs(r[1] - 2) < 1e-6 and r[2] < 1e-8
          and list(r[4]) == [0, 0, 1, 1, 2, 2] for r in odd))
check("E4 [F] even N, S = 3/2: spinorial (half-turns anticommute), sum|chi|^2/24 = 2, |chi(C4)| = sqrt2: G' + E1/2' "
      "(dims 4 + 2) = continuum j = 3/2 + j = 1/2 (tastes see C +- 1): no triplet",
      all(abs(r[1] - 2) < 1e-6 and r[3] < 1e-8 and abs(r[0]['C4'] - 2 ** 0.5) < 1e-5 and r[0]['E'] == 6 for r in even))
print("   verdict: C = 2S = 3 is exact for the smoothly refined cell field, but the surface Dirac count is 2C = 6 (tastes);")
print("   odd N gives T1 + T2 (each triplet has distinct turn charges -> turn-invariant masses degenerate, J = 0); even N")
print("   gives 4 + 2 spinor modes. CL-1's own boundary field (S = 0) carries no 3. The 3 needs a supplied boundary field: UNTESTED")
print(f"TOTAL: PASS={NP} FAIL={NF}   ({time.time() - T0:.1f} s)")
