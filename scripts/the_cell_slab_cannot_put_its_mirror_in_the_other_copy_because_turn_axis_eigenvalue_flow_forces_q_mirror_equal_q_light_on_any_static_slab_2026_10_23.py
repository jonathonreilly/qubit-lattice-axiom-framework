AUDIT_INPUT_PATHS = ('docs/THE_CELL_SLAB_CANNOT_PUT_ITS_MIRROR_IN_THE_OTHER_COPY_BECAUSE_TURN_AXIS_EIGENVALUE_FLOW_FORCES_Q_MIRROR_EQUAL_Q_LIGHT_ON_ANY_STATIC_SLAB_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""copy-flip-slab: is there a slab on CL-1's 2x2x2 cell (adopted layer hop (B/2 + i eps)/2, copy mass (1 - s) R_e) whose near
wall holds the s = +1 copy (q = 2, hand +1) and whose far wall holds the s = -1 copy (q = 1) as the mirror (hand -1)?
 A  cell facts: the copy sign s is exact at K = 0 (commutes with every cell-built term), not at generic K; turn spectra per copy.
 B  candidate (a): layer-dependent mass crossing from the (0, Mc) window to the (2, 2 + Mc) window (step and tanh profiles).
 C  candidate (b): layer hop carrying the copy sign (s A), and a copy-FLIPPING hop (turn covariance).
 D  general theorem: turn-sector eigenvalue flow along the turn axis forces q_mirror = q_light on any static slab whose only
    axis crossings are the wall Weyls.
 E  family-count bookkeeping on the realised slabs.
Labels: [T] exact, [F] finite diagnostic, [S] reading. Supplied: the cell-slab kernel, (m, Mc, Ls), profiles, free fields,
Hamiltonian (not circuit) form. Every line reports a RESULT; the synthesis verdict (criteria_pre_run.txt) is printed."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg, det=""):
    NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""))
OM = np.exp(2j * np.pi / 3); th = 2 * np.pi / 3
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
SIG = [sx, sy, sz]
def q3(z): return int(round(np.angle(z) / th)) % 3

# ---------------------------------------------------------------- CL-1 cell (wall-families C, inlined)
E3 = np.eye(3, dtype=int); SITES = list(itertools.product((0, 1), repeat=3))
def eta(x, i): return [1, (-1) ** int(x[0]), (-1) ** int(x[0] + x[1])][i]
def pairs(par):
    out = []
    for o in itertools.product((0, 1), repeat=3):
        A = np.array(o) + par
        for i in range(3):
            if not o[i]: out.append((A, A + E3[i], eta(A, i), i))
    return out
PE, PO = pairs(0), pairs(1)
def Wb(pp, k, i):
    M = np.zeros((8, 8), complex)
    for x, y, a, j in pp:
        if j != i: continue
        ia = np.ravel_multi_index(tuple(x % 2), (2,) * 3); ib = np.ravel_multi_index(tuple(y % 2), (2,) * 3)
        ph = a * np.exp(-1j * k @ (x // 2 - y // 2)); M[ia, ib] += ph; M[ib, ia] += np.conj(ph)
    return M
def cell(k):
    We = [Wb(PE, k, i) for i in range(3)]; Wo = [Wb(PO, k, i) for i in range(3)]
    Re = sum(We) / np.sqrt(3); Ro = sum(Wo) / np.sqrt(3); s = 1j * We[0] @ We[1] @ We[2] @ Re
    return We, Wo, Re, Ro, s
EPS8 = np.diag([(-1.) ** sum(x) for x in SITES]).astype(complex); I8 = np.eye(8)
def HP(k, prof, Mc, hop='A', extra=None):
    """open layer chain; on-layer (Re - Ro) + (m_l - 1) B/2 - (Mc/2)(1 - s) Re; hop (B/2 + i eps)/2 (or s x that)"""
    _, _, Re, Ro, s = cell(k); L = len(prof); H = np.zeros((8 * L, 8 * L), complex)
    A = ((Re + Ro) / 2 + 1j * EPS8) / 2
    if hop == 'sA': A = s @ A
    if extra is not None: A = A + extra
    for l, m in enumerate(prof):
        H[8 * l:8 * l + 8, 8 * l:8 * l + 8] = (Re - Ro) + (m - 1) * (Re + Ro) / 2 - (Mc / 2) * (I8 - s) @ Re
        if l + 1 < L: H[8 * l + 8:8 * l + 16, 8 * l:8 * l + 8] = A; H[8 * l:8 * l + 8, 8 * l + 8:8 * l + 16] = A.conj().T
    return H
def hand(Hf, P, h=1e-5):
    v = np.zeros((3, 3))
    for j in range(3):
        q = np.zeros(3); q[j] = h; hj = P.conj().T @ (Hf(q) - Hf(-q)) @ P / (2 * h)
        for i in range(3): v[i, j] = np.real(np.trace(SIG[i] @ hj)) / 2
    return int(np.sign(np.linalg.det(v)))
# the turn about (111): site-phase lift of the cyclic permutation (keeps both tilings, s and eps)
perm = np.zeros(8, int)
for a in SITES: perm[np.ravel_multi_index(a, (2,) * 3)] = np.ravel_multi_index((a[2], a[0], a[1]), (2,) * 3)
Pm = np.zeros((8, 8)); Pm[perm, np.arange(8)] = 1
We0, Wo0, Re0, Ro0, s0 = cell(np.zeros(3))
src = [Pm @ W @ Pm.T for W in We0 + Wo0]; tgt = [We0[1], We0[2], We0[0], Wo0[1], Wo0[2], Wo0[0]]
Dg = np.zeros(8, complex); Dg[0] = 1; todo = [0]
while todo:
    x = todo.pop()
    for A_, B_ in zip(src, tgt):
        for y in np.nonzero(np.abs(A_[x]) > 1e-12)[0]:
            if Dg[y] == 0: Dg[y] = np.conj(B_[x, y] / A_[x, y] / Dg[x]); todo.append(y)
UT = np.diag(Dg) @ Pm
def walls(prof, Mc, hop='A', extra=None, tol=1e-3):
    """K = 0 zero modes clustered by layer position and split by s; per 2-dim block: (pos, s, hand, q, turn eigen exps)"""
    L = len(prof); Hf = lambda k: HP(k, prof, Mc, hop, extra); ev, V = np.linalg.eigh(Hf(np.zeros(3)))
    Z = V[:, np.abs(ev) < tol]; UTL = np.kron(np.eye(L), UT); sL = np.kron(np.eye(L), s0)
    xe, U = np.linalg.eigh(Z.conj().T @ np.kron(np.diag(np.arange(L) * 1.), I8) @ Z); Z = Z @ U; out = []; i = 0
    while i < len(xe):
        j = i
        while j + 1 < len(xe) and abs(xe[j + 1] - xe[i]) < 2.0: j += 1
        P = Z[:, i:j + 1]; se, Us = np.linalg.eigh(P.conj().T @ sL @ P)
        for sg in (1, -1):
            Q = P @ Us[:, np.abs(se - sg) < 0.5]
            if Q.shape[1] == 0: continue
            tev = np.linalg.eigvals(Q.conj().T @ UTL @ Q)
            out.append(dict(pos=int(round(np.mean(xe[i:j + 1]))), s=sg, dim=Q.shape[1], P=Q,
                            h=hand(Hf, Q) if Q.shape[1] == 2 else 0, q=(2 * q3(np.prod(tev))) % 3 if Q.shape[1] == 2 else -1,
                            t=sorted(q3(z) for z in tev)))
        i = j + 1
    return ev, out
def fmt(out): return "; ".join(f"l{o['pos']} s{o['s']:+d} h{o['h']:+d} q{o['q']}" for o in out)
def bulk_gap(m, Mc, n=5):
    g = 9.
    Ks = [np.zeros(3)] if n == 0 else itertools.product(np.linspace(-np.pi, np.pi, n, endpoint=False), repeat=3)
    for K in Ks:
        for kl in np.linspace(-np.pi, np.pi, 8, endpoint=False):
            _, _, Re, Ro, s = cell(np.array(K)); A = ((Re + Ro) / 2 + 1j * EPS8) / 2
            Hb = (Re - Ro) + (m - 1) * (Re + Ro) / 2 - (Mc / 2) * (I8 - s) @ Re + np.exp(1j * kl) * A + np.exp(-1j * kl) * A.conj().T
            g = min(g, np.abs(np.linalg.eigvalsh(Hb)).min())
    return g

# ================================================================ A. cell facts
print("== A. the copy sign on CL-1's cell")
Kg = np.array([0.3, -0.7, 1.1]); _, _, ReG, RoG, sG = cell(Kg)
cm = lambda X, Y: np.abs(X @ Y - Y @ X).max()
d0 = max(cm(s0, X) for X in (Re0, Ro0, EPS8, UT)); dG = cm(sG, RoG)
check("A1 [T]", d0 < 1e-12 and dG > 0.1, "at K = 0 the copy sign s commutes with R_e, R_o, eps and the turn, so every cell-built "
      "layer term (any m(l), Mc(l), hop built from R_e, R_o, eps, s) keeps s exactly at K = 0; at generic K s fails to commute "
      "with R_o: the copy is a K = 0 label", f"K=0 defect {d0:.0e}; generic K |[s,R_o]| {dG:.2f}")
es, Vs = np.linalg.eigh(s0); spec = {sg: sorted(q3(z) for z in np.linalg.eigvals(Vs[:, np.isclose(es, sg)].conj().T @ UT @ Vs[:, np.isclose(es, sg)])) for sg in (1, -1)}
check("A2 [T]", spec == {1: [0, 0, 1, 1], -1: [0, 0, 2, 2]}, "turn spectra on the copies at K = 0: s = +1 {1,1,w,w}, s = -1 "
      "{1,1,w^2,w^2}; the w sector is s+ only, the w^2 sector s- only", f"exponents {spec}")

# ================================================================ B. candidate (a): layer-dependent mass
print("== B. candidate (a): m(layer) from the (0, Mc) window to the (2, 2 + Mc) window, Mc = 1, Ls = 32")
Ls, Mc = 32, 1.0
_, u1 = walls([0.5] * Ls, Mc); _, u2 = walls([2.5] * Ls, Mc)
ok = ([(o['pos'] < 3, o['s'], o['h'], o['q']) for o in u1] == [(True, 1, 1, 2), (False, 1, -1, 2)] and
      [(o['pos'] < 3, o['s'], o['h'], o['q']) for o in u2] == [(True, -1, -1, 1), (False, -1, 1, 1)])
check("B1 [T]/[F]", ok, "uniform windows: (0, Mc) holds s+ (q 2) on BOTH walls (near +1, far -1); (2, 2 + Mc) holds s- (q 1) on BOTH "
      "walls (near -1, far +1)", f"m=0.5: {fmt(u1)} | m=2.5: {fmt(u2)}")
gb = (bulk_gap(0.5, Mc), bulk_gap(2.5, Mc)); gc = [bulk_gap(m, Mc, n=0) for m in (1.0, 2.0)]
check("B2 [F]", min(gb) > 0.2 and max(gc) < 1e-9, "both end phases are gapped bulks, but every interpolation between them "
      "passes the bulk gap closings m = Mc (s- ratio 1 + Mc - m hits 1) and m = 2 (s+ ratio 1 - m hits -1)",
      f"gaps {gb[0]:.2f}, {gb[1]:.2f} (5^3 x 8 grid); K = 0 gap at m = 1, 2: {gc[0]:.0e}, {gc[1]:.0e}")
step = [0.5] * (Ls // 2) + [2.5] * (Ls // 2); evs, st = walls(step, Mc)
tanh = list(1.5 + np.tanh((np.arange(40) - 19.5) / 3.0)); evt, tt = walls(tanh, Mc)
sig = lambda out: sorted((min(2, int(3 * o['pos'] / out[-1]['pos'] + 0.5)) if out[-1]['pos'] else 0, o['s'], o['h'], o['q']) for o in out)
want = [(0, 1, 1, 2), (2, -1, 1, 1)]
ok = (len(st) == 4 and sorted((o['s'], o['h'], o['q']) for o in st if 10 < o['pos'] < 22) == [(-1, -1, 1), (1, -1, 2)] and
      [(o['s'], o['h'], o['q']) for o in st if o['pos'] < 3] == [(1, 1, 2)] and [(o['s'], o['h'], o['q']) for o in st if o['pos'] > 28] == [(-1, 1, 1)])
check("B3 [T]/[F]", ok, "sharp step 0.5 -> 2.5: near wall s+ (+1, q 2); far wall s- (q 1) but hand +1, the SAME hand as the light, "
      "so it is a second light Weyl, not the mirror; the interior interface carries BOTH mirrors s+ (-1, q 2) and s- (-1, q 1)",
      fmt(st))
okt = (len(tt) == 4 and [(o['s'], o['h'], o['q']) for o in tt if o['pos'] < 3] == [(1, 1, 2)] and
       [(o['s'], o['h'], o['q']) for o in tt if o['pos'] > 36] == [(-1, 1, 1)] and
       sorted((o['s'], o['h']) for o in tt if 5 < o['pos'] < 35) == [(-1, -1), (1, -1)])
check("B4 [F]", okt, "smooth profile m = 1.5 + tanh((l - 19.5)/3), Ls = 40: the same four Weyls; the interface modes cannot be "
      "removed by smoothing", fmt(tt))
# exact reason: per copy cumulative log|r|
def F(prof, sg): return np.cumsum([np.log(abs(1 - m + (Mc if sg < 0 else 0))) for m in prof])
Fp, Fm = F(step, 1), F(step, -1)
ok = (int(np.argmin(Fp)) in range(14, 17) and int(np.argmin(Fm)) == Ls - 1 and int(np.argmax(np.r_[0, Fm])) in range(15, 18) and Fp[-1] < -3 and Fm[-1] < -3)
check("B5 [T]", ok, "exact reason: at K = 0 each copy is its own Shamir chain (ratios r_+ = 1 - m, r_- = 1 + Mc - m); its hand-h_s "
      "mode sits at the max and its hand -h_s mode at the min of F_s = cum log|r_s| (h_+ = +1, h_- = -1), and a pair exists only "
      "if F_s(end) << 0. So the far boundary can hold copy s only with hand -h_s: s+ with -1 or s- with +1, never s- with -1",
      f"argmin F+ l={int(np.argmin(Fp))}, argmax F- l={int(np.argmax(np.r_[0, Fm])) - 1}, argmin F- l={int(np.argmin(Fm))}; F+(end) {Fp[-1]:.1f}, F-(end) {Fm[-1]:.1f}")

# ================================================================ C. candidate (b): the layer hop and the copy
print("== C. candidate (b): the layer hop carrying or flipping the copy")
_, b1 = walls([0.5] * Ls, Mc, hop='sA'); _, b2 = walls([1.5] * Ls, Mc, hop='sA'); _, b2r = walls([1.5] * Ls, Mc)
key = lambda out: sorted((o['pos'] < 3, o['s'], o['h'], o['q']) for o in out)
check("C1 [T]/[F]", key(b1) == key(u1) and key(b2) == key(b2r), "hop s A (the hop carries the copy sign): at K = 0 this is the gauge "
      "(-1)^l on the s- copy, |r| unchanged, so every window keeps the same copy on both walls", f"m=0.5: {fmt(b1)}")
def tavg(M): return sum(np.linalg.matrix_power(UT, j) @ M @ np.linalg.matrix_power(UT, j).conj().T for j in range(3)) / 3
Pp, Pn = (I8 + s0) / 2, (I8 - s0) / 2; rk = 0
for _ in range(20):
    M = tavg(rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))); X = Pp @ M @ Pn + Pn @ M @ Pp
    rk = max(rk, np.linalg.matrix_rank(X, 1e-9)); Xs = X
check("C2 [T]", rk == 4, "a hop that flips the copy (anticommutes with s) and commutes with the turn exists only on the eigenvalue-1 "
      "sectors (rank <= 4 < 8, from A2): no turn-covariant copy flip exists; the turn charges of the copies differ by w^2",
      f"max rank of turn-commuting s-odd operators {rk}")
_, bx = walls([0.5] * Ls, Mc, extra=0.3 * Xs / np.abs(Xs).max())
ok = all(o['dim'] == 1 and o['t'] == [1] for o in bx) and len(bx) == 2
check("C3 [F]", ok, "adding such a turn-commuting copy-mixing hop (g = 0.3) splits the K = 0 pairs; the surviving K = 0 zero modes "
      "on BOTH walls sit in the w sector, which is s+ only (A2), so neither wall becomes a q = 1 pair {1, w^2}",
      f"{[(o['pos'], o['t']) for o in bx]}")

# ================================================================ D. the axis eigenvalue flow theorem
print("== D. eigenvalue flow along the turn axis K = kappa (1,1,1) (any static turn-symmetric slab)")
UTL = np.kron(np.eye(Ls), UT); evU, VU = np.linalg.eig(UTL); SEC = [VU[:, [q3(z) == a for z in evU]] for a in range(3)]
SEC = [np.linalg.qr(S)[0] for S in SEC]
def nneg(prof, kap):
    H = HP(kap * np.ones(3), prof, Mc); return [int(np.sum(np.linalg.eigvalsh(S.conj().T @ H @ S) < 0)) for S in SEC], np.abs(np.linalg.eigvalsh(H)).min(), np.abs(UTL @ H - H @ UTL).max()
okD = True; dets = []
for name, prof in (("m=0.5", [0.5] * Ls), ("step", step)):
    rows = [nneg(prof, k) for k in [0.05] + list(np.linspace(0.4, 2 * np.pi - 0.4, 9)) + [-0.05]]
    okD &= all(r[0] == rows[0][0] for r in rows) and min(r[1] for r in rows) > 1e-3 and max(r[2] for r in rows) < 1e-12
    dets.append(f"{name}: {rows[0][0]}")
check("D1 [F]", okD, "on the axis the turn is a symmetry and the negative-state count per turn sector (1, w, w^2) is the same on "
      "both sides of K = 0 and all around the loop: the K = 0 crossings have zero net flow", "; ".join(dets))
def node_flow(o, prof):
    P = o['P']; Tp = P.conj().T @ UTL @ P; f = np.zeros(3, int)
    for sgn in (1, -1):
        h2 = P.conj().T @ HP(sgn * 1e-3 * np.ones(3), prof, Mc) @ P; e, v = np.linalg.eigh(h2)
        f[q3(v[:, 0].conj() @ Tp @ v[:, 0] / (v[:, 0].conj() @ v[:, 0]))] += sgn
    return f
form = lambda q, h: h * (np.eye(3, dtype=int)[(q + 2) % 3] - np.eye(3, dtype=int)[(q + 1) % 3])
nodes = [(o, [0.5] * Ls) for o in u1] + [(o, [2.5] * Ls) for o in u2] + [(o, step) for o in st]
fl = [(node_flow(o, p), form(o['q'], o['h'])) for o, p in nodes]
sg = 1 if np.array_equal(fl[0][0], fl[0][1]) else -1
check("D2 [T]/[F]", all(np.array_equal(a, sg * b) for a, b in fl), "each wall Weyl pair of copy charge q and hand h moves one state "
      "between turn sectors: flow = h (w^(q+2) - w^(q+1)) (one global sign), checked on all 8 wall pairs of B1 and B3",
      f"global sign {sg:+d}; e.g. near light {fl[0][0].tolist()}")
okA = all((not np.any(N * (form(ql, 1) + form(qm, -1)))) == (ql == qm) for N in range(1, 10) for ql in range(3) for qm in range(3))
okR = not np.any(form(0, 1) + form(1, 1) + form(2, 1))
check("D3 [T]", okA and okR, "theorem: with no other axis crossing the K = 0 flow of N_f (q_l, +1) + N_f (q_m, -1) must vanish, "
      "which holds iff q_m = q_l, for EVERY N_f (Z[Z3] torsion-free). The three flows sum to 0, so a copy-flipped mirror needs "
      "extra axis Weyls; a Floquet walk evades it through its second (pi) gap, as FREEZE does")

# ================================================================ E. bookkeeping
print("== E. family-count bookkeeping (families-mod-3 index; Omega twist selection)")
Ns = range(1, 10)
def allowed(light, mirror):
    out = []
    for N in Ns:
        for k in range(3):
            t = [(q + k) % 3 for q in mirror]
            omega_kept = sum(t) % 3 == 0          # Omega (single copy: t = 0; cross-copy B(s+)B(s-): t1 + t2 = 0)
            if not omega_kept: continue
            if (N * sum(t)) % 3 or (16 * N * sum(t)) % 3 or (16 * N * sum(x ** 3 for x in t)) % 9: continue
            if (N * 4 * sum((q + k) % 3 for q in light)) % 3 == 0: out.append(N); break
    return out
aU, aS, aH = allowed([2], [2]), allowed([2, 1], [2, 1]), allowed([2], [1])
check("E1 [T]", aU == list(Ns) and aS == list(Ns) and aH == [3, 6, 9], "uniform slab (light 2, mirror 2): every N_f; step slab "
      "(lights {2,1}, mirrors {2,1}, cross-copy Omega kept at k = 0): every N_f; only the unrealised copy-flip pair (2 | 1) gives "
      "3, 6, 9", f"uniform {aU}; step {aS}; copy-flip {aH}")
print("   E2 [S] the step slab also doubles the light content (two light copies, q 2 and q 1, per family), against CL-1's one light copy")
P1, P2, P3, P4 = False, False, False, False
print(f"   synthesis (criteria_pre_run): P1 walls in different copies with opposite hands {P1}, P2 interior gapped {P2}, "
      f"P3 forced {P3}, P4 mod 3 {P4} -> FAIL: no static copy-flip slab exists (D3); (a) gives far s- with the light's hand plus "
      f"interface mirrors, chosen; (b) keeps or cannot flip the copy")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
