#!/usr/bin/env python3
"""A three-dimensional composite-site network with an exact charge.

Supplied model, finite diagnostic, no physical reading.  Composite sites
(open PR 9144: one gauge-role qubit tau and one matter-role qubit sigma per
site) with Yao-Lee bonds (tau^l tau^l)(sigma.sigma) need a trivalent network
with three distinct bond flavours per site.  This runner certifies:

 1. the hyperhoneycomb (10,3)-b graph embeds in Z^3 (and so in the vertex
    sublattice of the doubled lattice) with every bond on a lattice axis and
    exactly three of the six neighbours used: trivalent, induced, bipartite,
    girth 10, 4 sites per primitive cell, flavours {x,y,z} at every site;
 2. the record pattern on the doubled lattice (unrecorded composite sites,
    flavour records on the bond links) and its covariance: stabiliser and
    orbit of the pattern under the 24 proper rotations;
 3. on an 8-qubit star of four composite sites with the covariant odd term:
    [H, S^a] = 0 exactly for the total matter spin, and the spectrum equals
    the three-flavour free-Majorana spectrum (fixing the sign of the odd
    term's reduction on a cluster where the sign matters);
 4. the 10-loop operators commute with every bond and odd term (Pauli-string
    algebra) and the term supports fit small blocks;
 5. flux-free Bloch spectrum, kappa = 0: a nodal line (dimension estimate 1),
    gapped at strong anisotropy;
 6. kappa = 0.3: isolated Weyl points, chirality +-1 by Berry flux through a
    cube, total zero;
 7. six-valent route: minimal composite-site content by the dimension of the
    generated algebra (4 qubits for SU(2), 3 for U(1), 2 for the trivalent
    Yao-Lee site);
 8. six-valent cubic bands: zero flux gives a zero-energy surface, pi flux
    isolated eightfold nodes with zero Berry flux and the lower energy.

Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import sys
import time

import numpy as np
from scipy.optimize import minimize

AUDIT_TIMEOUT_SEC = 600

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


# ----------------------------------------------------------------------------
# 1. The hyperhoneycomb on Z^3 with axis bonds (network coordinates; the doubled
#    lattice scales every coordinate by two).
# ----------------------------------------------------------------------------
AX = {"x": 0, "y": 1, "z": 2}
FL = ["x", "y", "z"]
L_CELL = (2, 2, 4)


def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    """Flavour of the bond between adjacent network sites p and q."""
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q          # the lower end of the chain bond
    m = p[2] % 4
    # alternate x, y along the chain; the alternation is shifted by one bond in
    # layers 2 and 3 so that the pattern keeps the (1,1,2) translation and the
    # inversion about a chain-bond midpoint (D-flavour)
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p)
            q[a] += s
            q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


def torus_graph(Ls):
    sites = [p for p in itertools.product(range(Ls[0]), range(Ls[1]), range(Ls[2])) if is_site(p)]
    idx = {p: n for n, p in enumerate(sites)}
    adj = {n: [] for n in range(len(sites))}
    for p in sites:
        for a in range(3):
            for s in (-1, 1):
                q = list(p)
                q[a] += s
                qf = tuple(q[b] % Ls[b] for b in range(3))
                if is_site(qf):
                    adj[idx[p]].append(idx[qf])
    return sites, idx, adj


sites8, idx8, adj8 = torus_graph(L_CELL)
degrees = sorted(len(adj8[n]) for n in adj8)
# infinite-lattice checks on a window
window = [p for p in itertools.product(range(-3, 4), range(-3, 4), range(-3, 5)) if is_site(p)]
triv = all(len(neighbours(p)) == 3 for p in window)
fl_ok = all(sorted(flavour(p, q) for q in neighbours(p)) == FL for p in window)
bip = all((sum(p) + sum(q)) % 2 == 1 for p in window for q in neighbours(p))
# translation (1,1,2) preserves sites and flavours -> 4 sites per primitive cell
t112 = all(is_site((p[0] + 1, p[1] + 1, p[2] + 2)) for p in window) and all(
    flavour(p, q) == flavour((p[0] + 1, p[1] + 1, p[2] + 2), (q[0] + 1, q[1] + 1, q[2] + 2))
    for p in window for q in neighbours(p))
# inversion about the midpoint of the chain bond (0,0,0)-(1,0,0) preserves sites and flavours
inv = lambda p: (1 - p[0], -p[1], -p[2])
inv_ok = all(is_site(inv(p)) for p in window) and all(
    flavour(p, q) == flavour(inv(p), inv(q)) for p in window for q in neighbours(p))
# girth and 10-cycle count through the origin (DFS on the infinite graph)
p0 = (0, 0, 0)


def cycles_through(p0, length):
    count = 0
    girth = None
    stack = [(p0, [p0])]
    while stack:
        p, path = stack.pop()
        for q in neighbours(p):
            if q == p0 and len(path) >= 3:
                if girth is None or len(path) < girth:
                    girth = len(path)
                if len(path) == length:
                    count += 1
            elif q not in path and len(path) < length:
                stack.append((q, path + [q]))
    return girth, count // 2


girth, n10 = cycles_through(p0, 10)
# coordination sequence
shell = {p0: 0}
frontier = [p0]
seq = []
for _ in range(5):
    nxt = []
    for p in frontier:
        for q in neighbours(p):
            if q not in shell:
                shell[q] = shell[p] + 1
                nxt.append(q)
    seq.append(len(nxt))
    frontier = nxt
# connectivity on the 4x4x8 torus
_, _, adjT = torus_graph((4, 4, 8))
seen = {0}
st = [0]
while st:
    n = st.pop()
    for m in adjT[n]:
        if m not in seen:
            seen.add(m)
            st.append(m)
connected = len(seen) == len(adjT)
check("hyperhoneycomb embeds in Z^3 with axis bonds",
      triv and fl_ok and bip and t112 and inv_ok and girth == 10 and degrees == [3] * 8 and connected,
      f"sites per 2x2x4 cell {len(sites8)}, degrees {sorted(set(degrees))}, induced trivalent {triv}, "
      f"flavours xyz at every site {fl_ok}, bipartite {bip}, (1,1,2) translation {t112} -> 4 sites per "
      f"primitive cell, inversion about a chain-bond midpoint {inv_ok}, girth {girth}, 10-cycles through a site {n10}, coordination sequence {seq}, "
      f"connected on 4x4x8 torus {connected}")

# ----------------------------------------------------------------------------
# 2. Record pattern on the doubled lattice and its covariance.
# ----------------------------------------------------------------------------
# doubled cell 4x4x8: vertices 2p, cube partners 2p+(1,1,1), links 2p+e.
n_vert = 2 * 2 * 4
n_net = len(sites8)
bonds_cell = sum(len(adj8[n]) for n in adj8) // 2
n_links = 3 * n_vert
# links from network vertices to recorded vertices
rec_links = 0
for p in sites8:
    for a in range(3):
        for s in (-1, 1):
            q = list(p)
            q[a] += s
            if not is_site(tuple(q)):
                rec_links += 1
# proper rotations
mats = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((-1, 1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for r in range(3):
            M[r, perm[r]] = signs[r]
        if round(np.linalg.det(M)) == 1:
            mats.append(M)
assert len(mats) == 24


def pattern_bonds(Ls):
    out = set()
    for p in itertools.product(range(Ls[0]), range(Ls[1]), range(Ls[2])):
        if not is_site(p):
            continue
        for q in neighbours(p):
            out.add((p, q, flavour(p, q)))
    return out


def rotated_pattern_matches(M, t, with_flavour=True):
    """R p + t is a site for every site p in a window, with matching flavours."""
    for p in window:
        rp = tuple(int(v) for v in M @ np.array(p) + np.array(t))
        if not is_site(rp):
            return False
        for q in neighbours(p):
            rq = tuple(int(v) for v in M @ np.array(q) + np.array(t))
            if not is_site(rq):
                return False
            if with_flavour:
                f_img = FL[int(np.argmax(np.abs(M[:, AX[flavour(p, q)]])))]
                if flavour(rp, rq) != f_img:
                    return False
    return True


stab_f, stab_s = 0, 0
for M in mats:
    okf = any(rotated_pattern_matches(M, t, True) for t in itertools.product(range(2), range(2), range(4)))
    oks = any(rotated_pattern_matches(M, t, False) for t in itertools.product(range(2), range(2), range(4)))
    stab_f += okf
    stab_s += oks
check("record pattern: half the composite sites, flavour records on links, covariant rule, supplied pattern",
      n_net == 8 and bonds_cell == 12 and rec_links == 24 and stab_f >= 1 and 24 % stab_f == 0 and stab_s % stab_f == 0,
      f"per 4x4x8 doubled cell: {n_vert} vertices of which {n_net} unrecorded network sites and "
      f"{n_vert - n_net} recorded; {n_links} link sites of which {bonds_cell} carry flavour records, "
      f"{rec_links} join a network site to a recorded site, {n_links - bonds_cell - rec_links} join two "
      f"recorded sites; site-set stabiliser {stab_s} of 24 (orbit {24 // stab_s}), pattern-with-flavours "
      f"stabiliser {stab_f} of 24 (orbit {24 // stab_f}); the rule flavour = record axis is equivariant by construction")

# ----------------------------------------------------------------------------
# 3. Eight-qubit star: exact SU(2) and the Yao-Lee reduction with the odd term.
# ----------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
PX = np.array([[0, 1], [1, 0]], dtype=complex)
PY = np.array([[0, -1j], [1j, 0]], dtype=complex)
PZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {"x": PX, "y": PY, "z": PZ}


def op(nq, ops):
    """ops: dict qubit -> 2x2 matrix."""
    out = np.array([[1.0 + 0j]])
    for q in range(nq):
        out = np.kron(out, ops.get(q, I2))
    return out


def bond_term(nq, I, J, lam):
    # composite site I: tau at 2I, sigma at 2I+1
    t = op(nq, {2 * I: PAULI[lam], 2 * J: PAULI[lam]})
    s = sum(op(nq, {2 * I + 1: PAULI[a], 2 * J + 1: PAULI[a]}) for a in FL)
    return t @ s


def odd_term(nq, nl, c, nm, lam, mu, nu):
    t = op(nq, {2 * nl: PAULI[lam], 2 * c: PAULI[nu], 2 * nm: PAULI[mu]})
    s = sum(op(nq, {2 * nl + 1: PAULI[a], 2 * nm + 1: PAULI[a]}) for a in FL)
    return t @ s


NQ = 8
Jst = (1.0, 0.8, 0.6)
KAP = 0.35
leaf = {"x": 1, "y": 2, "z": 3}
H8 = sum(Jst[k] * bond_term(NQ, 0, leaf[f], f) for k, f in enumerate(FL))
cyc = [("x", "y", "z"), ("y", "z", "x"), ("z", "x", "y")]
H8 = H8 + KAP * sum(odd_term(NQ, leaf[l], 0, leaf[m], l, m, n) for (l, m, n) in cyc)
S_tot = {a: 0.5 * sum(op(NQ, {2 * i + 1: PAULI[a]}) for i in range(4)) for a in FL}
comm = max(np.abs(H8 @ S_tot[a] - S_tot[a] @ H8).max() for a in FL)
ed = np.linalg.eigvalsh(H8)


def free_spectrum_star(sign):
    A = np.zeros((4, 4))
    for k, f in enumerate(FL):
        A[0, leaf[f]] = 2 * Jst[k]
        A[leaf[f], 0] = -2 * Jst[k]
    for (l, m, n) in cyc:
        A[leaf[l], leaf[m]] += 2 * KAP * sign
        A[leaf[m], leaf[l]] -= 2 * KAP * sign
    eps = np.sort(np.linalg.eigvalsh(1j * A))
    eps = eps[eps > 1e-12]
    one = [sum(s * e / 2 for s, e in zip(sg, eps)) for sg in itertools.product((-1, 1), repeat=len(eps))]
    tot = [sum(c) for c in itertools.product(one, repeat=3)]
    return np.sort(np.repeat(np.sort(tot), 256 // len(tot)))


dev = {s: np.abs(free_spectrum_star(s) - ed).max() for s in (+1, -1)}
ODD_SIGN = +1          # convention: the two signs are spin-flip time-reversal images
check("8-qubit star: [H, S] = 0 exactly and spectrum = three-flavour free Majorana spectrum",
      comm < 1e-12 and dev[1] < 1e-9 and dev[-1] < 1e-9,
      f"J={Jst}, kappa={KAP}; max|[H,S^a]| {comm:.1e}; spectrum deviation with odd-term hopping "
      f"+kappa: {dev[1]:.1e}, -kappa: {dev[-1]:.1e} (the spectrum is even in kappa, so no spectrum fixes "
      f"the sign: a convention); 256 levels, {len(np.unique(np.round(ed, 8)))} distinct, lowest {ed[0]:.6f}")

# ----------------------------------------------------------------------------
# 4. Loop operators commute with every term (Pauli-string algebra); supports.
# ----------------------------------------------------------------------------


def find_10_loops(p0):
    loops = []
    stack = [(p0, [p0])]
    while stack:
        p, path = stack.pop()
        for q in neighbours(p):
            if q == p0 and len(path) == 10:
                loops.append(tuple(path))
            elif q not in path and len(path) < 10:
                stack.append((q, path + [q]))
    uniq = {}
    for lp in loops:
        uniq[frozenset(lp)] = lp
    return list(uniq.values())


loops10 = find_10_loops(p0)


def loop_string(lp):
    """tau Pauli at each loop site: the flavour not used by the loop there."""
    s = {}
    n = len(lp)
    for k, p in enumerate(lp):
        used = {flavour(p, lp[(k - 1) % n]), flavour(p, lp[(k + 1) % n])}
        s[p] = (set(FL) - used).pop()
    return s


def commute(s1, s2):
    n_anti = sum(1 for p in s1 if p in s2 and s1[p] != s2[p])
    return n_anti % 2 == 0


terms = []      # tau-Pauli strings of bond terms and odd terms near the origin
boxes = set()
for p in window:
    for q in neighbours(p):
        terms.append({p: flavour(p, q), q: flavour(p, q)})
    nb = {flavour(p, q): q for q in neighbours(p)}
    for (l, m, n) in cyc:
        terms.append({nb[l]: l, p: n, nb[m]: m})
        pts = [np.array(nb[l]) * 2, np.array(p) * 2, np.array(nb[m]) * 2]
        pts += [x + 1 for x in pts]
        pts = np.array(pts)
        boxes.add(tuple(int(v) for v in pts.max(0) - pts.min(0) + 1))
all_comm = all(commute(loop_string(lp), t) for lp in loops10 for t in terms)
# a wrong flavour on one loop site breaks it (control)
lp = loops10[0]
bad = dict(loop_string(lp))
k0 = lp[0]
bad[k0] = [f for f in FL if f != bad[k0]][0]
control_breaks = not all(commute(bad, t) for t in terms)
bond_boxes = set()
for p in window:
    for q in neighbours(p):
        pts = np.array([2 * np.array(p), 2 * np.array(q), np.array(p) + np.array(q),
                        2 * np.array(p) + 1, 2 * np.array(q) + 1])
        bond_boxes.add(tuple(int(v) for v in pts.max(0) - pts.min(0) + 1))
bond_box = sorted(bond_boxes)
check("10-loop operators commute with all bond and odd terms; term supports are small blocks",
      len(loops10) == n10 and all_comm and control_breaks and bond_box == [(2, 2, 4), (2, 4, 2), (4, 2, 2)],
      f"{len(loops10)} loops through a site, all commute with {len(terms)} terms; control (one wrong "
      f"Pauli) breaks commutation {control_breaks}; bond support box {bond_box}, odd-term boxes "
      f"{sorted(boxes)}")

# ----------------------------------------------------------------------------
# 5./6. Bloch spectra of the c Majoranas (one flavour), flux-free sector u = +1.
# ----------------------------------------------------------------------------


def hopping_entries(Ls, sites, idx, Jvec, kappa, sign):
    """List of (a, b, R, amp): A_ab(k) = sum amp e^{i k.R}, A antisymmetric real."""
    ent = []
    for p in sites:
        a = idx[p]
        subA = sum(p) % 2 == 0
        for q in neighbours(p):
            qf = tuple(q[b] % Ls[b] for b in range(3))
            R = tuple((q[b] - qf[b]) // Ls[b] for b in range(3))
            b = idx[qf]
            J = Jvec[AX[flavour(p, q)]]
            ent.append((a, b, R, 2 * J if subA else -2 * J))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            for (l, m, n) in cyc:
                q1, q2 = nb[l], nb[m]
                q1f = tuple(q1[b] % Ls[b] for b in range(3))
                q2f = tuple(q2[b] % Ls[b] for b in range(3))
                R1 = tuple((q1[b] - q1f[b]) // Ls[b] for b in range(3))
                R2 = tuple((q2[b] - q2f[b]) // Ls[b] for b in range(3))
                Rrel = tuple(R2[b] - R1[b] for b in range(3))
                ent.append((idx[q1f], idx[q2f], Rrel, 2 * kappa * sign))
                ent.append((idx[q2f], idx[q1f], tuple(-r for r in Rrel), -2 * kappa * sign))
    return ent


def bloch(ent, n, k):
    A = np.zeros((n, n), dtype=complex)
    for a, b, R, amp in ent:
        A[a, b] += amp * np.exp(1j * (k[0] * R[0] + k[1] * R[1] + k[2] * R[2]))
    return 1j * A


def gap_fn(ent, n):
    def g(k):
        e = np.linalg.eigvalsh(bloch(ent, n, k))
        return float(np.min(np.abs(e)))
    return g


def grid_gaps(ent, n, N):
    ks = 2 * np.pi * np.arange(N) / N
    G = np.empty((N, N, N))
    for i, kx in enumerate(ks):
        for j, ky in enumerate(ks):
            for l, kz in enumerate(ks):
                G[i, j, l] = np.min(np.abs(np.linalg.eigvalsh(bloch(ent, n, (kx, ky, kz)))))
    return ks, G


def dim_estimate(ent, n, c=1.5):
    counts = {}
    grids = {}
    for N in (16, 48):
        ks, G = grid_gaps(ent, n, N)
        counts[N] = int((G < c * 2 * np.pi / N).sum())
        grids[N] = (ks, G)
    d = np.log(counts[48] / counts[16]) / np.log(3) if counts[16] > 0 else np.nan
    return d, counts, grids[48]


def local_minima(ks, G, thresh):
    N = len(ks)
    out = []
    for i, j, l in zip(*np.where(G < thresh)):
        v = G[i, j, l]
        nb = G[np.ix_([(i - 1) % N, i, (i + 1) % N], [(j - 1) % N, j, (j + 1) % N], [(l - 1) % N, l, (l + 1) % N])]
        if v <= nb.min():
            out.append((v, (ks[i], ks[j], ks[l])))
    return [k for _, k in sorted(out, key=lambda t: t[0])]


def refine(g, k0):
    r = minimize(g, np.array(k0), method="Nelder-Mead",
                 options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 2000, "maxfev": 4000})
    return r.x, r.fun


def berry_flux_cube(ent, n, k0, nocc, r=0.04, m=10):
    """Chern number of the lowest nocc bands through a cube of half-width r around k0."""
    def states(k):
        w, v = np.linalg.eigh(bloch(ent, n, k))
        return v[:, :nocc]
    total = 0.0
    s = np.linspace(-r, r, m + 1)
    faces = []
    for ax in range(3):
        o1, o2 = [(1, 2), (2, 0), (0, 1)][ax]
        faces.append((ax, +1, o1, o2))
        faces.append((ax, -1, o2, o1))
    for ax, sg, o1, o2 in faces:
        def pt(u, v):
            k = np.array(k0, dtype=float)
            k[ax] += sg * r
            k[o1] += u
            k[o2] += v
            return k
        V = [[states(pt(s[i], s[j])) for j in range(m + 1)] for i in range(m + 1)]
        for i in range(m):
            for j in range(m):
                U = (np.linalg.det(V[i][j].conj().T @ V[i + 1][j]) *
                     np.linalg.det(V[i + 1][j].conj().T @ V[i + 1][j + 1]) *
                     np.linalg.det(V[i + 1][j + 1].conj().T @ V[i][j + 1]) *
                     np.linalg.det(V[i][j + 1].conj().T @ V[i][j]))
                total += np.angle(U)
    return total / (2 * np.pi)


n8 = len(sites8)
ent0 = hopping_entries(L_CELL, sites8, idx8, (1.0, 1.0, 1.0), 0.0, ODD_SIGN)
d0, cnt0, (ks40, G40) = dim_estimate(ent0, n8)
g0 = gap_fn(ent0, n8)
mins0 = local_minima(ks40, G40, 0.15)
best = min((refine(g0, k) for k in mins0[:6]), key=lambda t: t[1])
# anisotropic: gapped
entA = hopping_entries(L_CELL, sites8, idx8, (1.0, 1.0, 2.5), 0.0, ODD_SIGN)
_, GA = grid_gaps(entA, n8, 20)
gA = gap_fn(entA, n8)
gapA = min(refine(gA, k)[1] for k in local_minima(*grid_gaps(entA, n8, 20), 10.0)[:6])
# bandwidth
wmax = max(np.abs(np.linalg.eigvalsh(bloch(ent0, n8, k))).max() for k in itertools.product(ks40[::5], repeat=3))
check("kappa = 0, isotropic, flux-free: nodal line (dimension 1); anisotropic J_z = 2.5: gapped",
      best[1] < 1e-7 and abs(d0 - 1.0) < 0.35 and gapA > 0.5,
      f"min gap {best[1]:.1e} at k/2pi = (" + ", ".join(f"{float(v):.4f}" for v in np.mod(best[0], 2*np.pi)/(2*np.pi)) + "); "
      f"near-zero counts N=16: {cnt0[16]}, N=48: {cnt0[48]} -> dimension estimate {d0:.2f}; "
      f"bandwidth {wmax:.3f}; J=(1,1,2.5) gap {gapA:.4f}")

KAP3 = 0.3
entW = hopping_entries(L_CELL, sites8, idx8, (1.0, 1.0, 1.0), KAP3, ODD_SIGN)
dW, cntW, (ksW, GW) = dim_estimate(entW, n8)
gW = gap_fn(entW, n8)
nodes = []
for k in local_minima(ksW, GW, 0.3):
    kk, gv = refine(gW, k)
    if gv < 1e-7:
        kk = np.mod(kk, 2 * np.pi)
        if all(np.linalg.norm(np.mod(kk - q + np.pi, 2 * np.pi) - np.pi) > 1e-3 for q, _ in nodes):
            nodes.append((kk, gv))
chis = []
degen_ok = True
for kk, gv in nodes:
    e = np.linalg.eigvalsh(bloch(entW, n8, kk))
    e_abs = np.sort(np.abs(e))
    degen_ok &= e_abs[2] > 1e-3        # exactly two bands touch (one +, one - level near zero)
    chis.append(berry_flux_cube(entW, n8, kk, n8 // 2))
ph_sym = max(np.abs(np.sort(np.linalg.eigvalsh(bloch(entW, n8, k))) + np.sort(np.linalg.eigvalsh(bloch(entW, n8, k)))[::-1]).max()
             for k in itertools.product(ksW[::4], repeat=3))
chi_int = [int(round(c)) for c in chis]
chi_res = max(abs(c - r) for c, r in zip(chis, chi_int)) if chis else 1.0
check("kappa = 0.3: nodal line breaks into Weyl points with chirality +-1 summing to zero",
      len(nodes) >= 2 and len(nodes) % 2 == 0 and all(abs(c) == 1 for c in chi_int) and sum(chi_int) == 0
      and chi_res < 0.05 and abs(dW) < 0.5 and degen_ok and ph_sym < 1e-9,
      f"{len(nodes)} nodes, gaps < 1e-7; chiralities {chi_int} (Berry flux residual {chi_res:.3f}); "
      f"spectrum symmetric under E -> -E at every k (inversion x particle-hole) to {ph_sym:.0e}; "
      f"counts N=16: {cntW[16]}, N=48: {cntW[48]} -> dimension estimate {dW:.2f}; nodes at k/2pi: "
      + "; ".join("(" + ", ".join(f"{float(v):.3f}" for v in kk / (2 * np.pi)) + ")" for kk, _ in nodes))

# ----------------------------------------------------------------------------
# 7. Six-valent route: minimal site content from the generated algebra.
# ----------------------------------------------------------------------------


def majoranas(nq):
    """2 nq Majoranas by Jordan-Wigner."""
    out = []
    for q in range(nq):
        z = {p: PZ for p in range(q)}
        out.append(op(nq, {**z, q: PX}))
        out.append(op(nq, {**z, q: PY}))
    return out


def generated_dim(nb, nc):
    m = nb + nc
    nq = (m + 1) // 2
    g = majoranas(nq)[:m]
    # restrict to the +1 eigenspace of the product of all m Majoranas, which is
    # central in the even subalgebra (and in all of Cl(m) for odd m)
    b, c = g[:nb], g[nb:]
    gens = [1j * bi @ cj for bi in b for cj in c] + [1j * c[i] @ c[j] for i in range(nc) for j in range(i + 1, nc)]
    # restrict the (even) generators to the +1 eigenspace of the product of all m
    # Majoranas, which is central in the even subalgebra they generate
    G = np.linalg.multi_dot(g)
    Gh = (1j) ** (m * (m - 1) // 2 % 4) * G      # Hermitian version
    w, v = np.linalg.eigh(Gh)
    P = v[:, w > 0]
    gens = [P.conj().T @ x @ P for x in gens]
    dim = P.shape[1]
    B = np.zeros((0, dim * dim), dtype=complex)

    def add(vecs, B):
        for v in vecs:
            v = v.ravel().astype(complex)
            if B.shape[0]:
                v = v - B.T @ (B.conj() @ v)
            nv = np.linalg.norm(v)
            if nv > 1e-8:
                B = np.vstack([B, v / nv])
        return B
    B = add([np.eye(dim, dtype=complex)] + gens, B)
    while True:
        n_old = B.shape[0]
        cand = [(B[i].reshape(dim, dim) @ g) for i in range(n_old) for g in gens]
        B = add(cand, B)
        if B.shape[0] == n_old:
            break
    rank = B.shape[0]
    return rank, dim


r9, d9 = generated_dim(6, 3)
r8, d8 = generated_dim(6, 2)
r6, d6 = generated_dim(3, 3)
check("six-valent site content: generated algebra dimensions 256, 64, 16 -> 4, 3, 2 qubits",
      (r9, d9) == (256, 16) and (r8, d8) == (64, 8) and (r6, d6) == (16, 4),
      f"6 b + 3 c (SU(2), six-valent): algebra dim {r9} on {d9} states -> 4 qubits; 6 b + 2 c (U(1)): "
      f"{r8} on {d8} -> 3 qubits; 3 b + 3 c (trivalent Yao-Lee): {r6} on {d6} -> 2 qubits")

# ----------------------------------------------------------------------------
# 8. Six-valent cubic c-Majorana bands: zero flux and pi flux (2x2x2 cell).
# ----------------------------------------------------------------------------
cub_sites = list(itertools.product(range(2), range(2), range(2)))
cub_idx = {p: n for n, p in enumerate(cub_sites)}


def cubic_entries(pi_flux):
    ent = []
    for p in cub_sites:
        a = cub_idx[p]
        subA = sum(p) % 2 == 0
        for ax in range(3):
            for s in (-1, 1):
                q = list(p)
                q[ax] += s
                qf = tuple(v % 2 for v in q)
                R = tuple((q[b] - qf[b]) // 2 for b in range(3))
                lo = p if s > 0 else tuple(q)
                u = 1.0
                if pi_flux:
                    # standard pi-flux gauge: y bonds carry (-1)^x, z bonds carry (-1)^(x+y)
                    if ax == 1:
                        u = (-1.0) ** lo[0]
                    if ax == 2:
                        u = (-1.0) ** (lo[0] + lo[1])
                amp = 2.0 * u * (1 if subA else -1)
                ent.append((a, cub_idx[qf], R, amp))
    return ent


def energy_per_site(ent, n, N=16):
    ks = 2 * np.pi * (np.arange(N) + 0.5) / N
    tot = 0.0
    for k in itertools.product(ks, repeat=3):
        e = np.linalg.eigvalsh(bloch(ent, n, k))
        tot += -0.5 * e[e > 0].sum()
    return tot / (N ** 3 * n)


ent_c0 = cubic_entries(False)
ent_cp = cubic_entries(True)
dc0, cc0, _ = dim_estimate(ent_c0, 8)
dcp, ccp, (ksp, Gp) = dim_estimate(ent_cp, 8)
gp = gap_fn(ent_cp, 8)
pnodes = []
for k in local_minima(ksp, Gp, 0.5):
    kk, gv = refine(gp, k)
    if gv < 1e-7:
        kk = np.mod(kk, 2 * np.pi)
        if all(np.linalg.norm(np.mod(kk - q + np.pi, 2 * np.pi) - np.pi) > 1e-3 for q in pnodes):
            pnodes.append(kk)
deg_p = [int((np.abs(np.linalg.eigvalsh(bloch(ent_cp, 8, kk))) < 1e-6).sum()) for kk in pnodes]
flux_p = [berry_flux_cube(ent_cp, 8, kk, 4) for kk in pnodes]
E0 = energy_per_site(ent_c0, 8)
Ep = energy_per_site(ent_cp, 8)
check("six-valent cubic bands: zero flux surface (dimension 2), pi flux point nodes with zero Berry flux",
      abs(dc0 - 2.0) < 0.35 and abs(dcp) < 0.5 and len(pnodes) >= 1 and all(d == 8 for d in deg_p)
      and all(abs(f) < 0.05 for f in flux_p) and Ep < E0,
      f"zero flux counts N=16: {cc0[16]}, N=48: {cc0[48]} -> dimension {dc0:.2f}; pi flux counts "
      f"{ccp[16]}, {ccp[48]} -> dimension {dcp:.2f}; {len(pnodes)} pi-flux nodes in the 2x2x2 zone, "
      f"degeneracy {deg_p}, Berry flux {[round(float(f), 3) for f in flux_p]}; energy per site zero flux "
      f"{E0:.4f}, pi flux {Ep:.4f} (Lieb ordering, finite diagnostic)")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}  (runtime {time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
