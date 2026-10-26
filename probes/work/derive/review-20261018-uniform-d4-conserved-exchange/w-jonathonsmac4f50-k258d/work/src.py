#!/usr/bin/env python3
"""Exact local Laurent Ward algebra and finite D4-cone FD diagnostics.
The symbolic identity is distinct from sampled exchange fits and two-scale
partner suppression. No uniform EH, decoupling or Noether-action theorem.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ('archive/d4cone_ward_review_2026_10_18/MANIFEST.json', 'archive/d4cone_ward_review_2026_10_18/original-recovery.tar.gz', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/SCALE_LADDER_GRAVITY_D4CONE_EXACT_WARD_SITE_SCALAR_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/SCALE_LADDER_GRAVITY_D4CONE_STRAIN_READING_EXCHANGE_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/SCALE_LADDER_GRAVITY_D4_CONE_COMMON_CONE_SPINS_ZERO_ONE_TWO_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'outputs/d4cone_ward_review_2026_10_18/INPUT_CLOSURE.json')
import os, signal, json
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
if not __debug__:raise RuntimeError('Assertions must remain enabled')
def expired(signum,frame):raise TimeoutError('Enforced aggregate600-second cap reached')
signal.signal(signal.SIGALRM,expired);signal.alarm(AUDIT_TIMEOUT_SEC)

import itertools, sys
import numpy as np

PASS = FAIL = 0
HC = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
PAIRS = list(itertools.combinations(range(4), 2))


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''),flush=True)
    if not ok:raise AssertionError(name)


# ------------------------------------------------------------------ generic Bloch Regge builder (as in the orthoscheme runner)
def _key_pair(v1, v2):
    (b1, t1), (b2, t2) = v1, v2
    if (t1, b1) > (t2, b2): (b1, t1), (b2, t2) = (b2, t2), (b1, t1)
    rel = tuple(np.subtract(b2, b1))
    return (t1, t2, rel), tuple(b1)

def _key_tri(vs):
    vs = sorted(vs, key=lambda v: (v[1], v[0]))
    b0 = vs[0][0]
    return tuple((t, tuple(np.subtract(b, b0))) for b, t in vs), tuple(b0)

def coords_from_lengths(L2):
    """L2: 5x5 squared lengths -> 5x4 coordinates (vertex 0 at origin)."""
    G = np.array([[0.5 * (L2[0, a] + L2[0, b] - L2[a, b]) for b in range(1, 5)] for a in range(1, 5)])
    C = np.linalg.cholesky(G)
    return np.vstack([np.zeros(4), C])

def dihedral(P, h, m, n):
    """interior dihedral angle at triangle h (3 indices) between facets opposite m and opposite n."""
    def outward(opp):
        face = [i for i in range(5) if i != opp]
        A = np.array([P[i] - P[face[0]] for i in face[1:]])
        _, _, vt = np.linalg.svd(A); nv = vt[-1]
        if (P[opp] - P[face[0]]) @ nv > 0: nv = -nv
        return nv
    c = np.clip(outward(m) @ outward(n), -1, 1)
    return np.pi - np.arccos(c)

def tri_area(L2):
    a, b, c = L2
    G = np.array([[a, 0.5 * (a + b - c)], [0.5 * (a + b - c), b]])
    return 0.5 * np.sqrt(np.linalg.det(G))

class Complex:
    def __init__(self, OFF, base_simplices, g0=None, fd=1e-6):
        self.OFF = [np.array(o, float) for o in OFF]
        self.g0 = np.eye(4) if g0 is None else np.asarray(g0, float)
        self.simp = [list(s) for s in base_simplices]
        # edge classes
        self.ekey = {}
        for s in self.simp:
            for i, j in itertools.combinations(range(5), 2):
                k, _ = _key_pair(s[i], s[j])
                if k not in self.ekey: self.ekey[k] = len(self.ekey)
        self.E = len(self.ekey)
        self.evec = [None] * self.E
        for (t1, t2, rel), c in self.ekey.items():
            self.evec[c] = np.array(rel, float) + self.OFF[t2] - self.OFF[t1]
        self.types = sorted({t for s in self.simp for _, t in s})
        self.fd=fd
        self._build(fd)

    def pos(self, v): return np.array(v[0], float) + self.OFF[v[1]]
    def L(self, v1, v2):
        d = self.pos(v2) - self.pos(v1); return np.sqrt(d @ self.g0 @ d)

    def _build(self, fd):
        # hinge classes and their stars (simplex, translation) with hinge at anchor 0
        stars, hverts = {}, {}
        for si, s in enumerate(self.simp):
            for tri in itertools.combinations(range(5), 3):
                key, anc = _key_tri([s[i] for i in tri])
                T = -np.array(anc)
                stars.setdefault(key, []).append((si, T, tri))
                hverts.setdefault(key, [(tuple(np.add(s[i][0], T)), s[i][1]) for i in tri])
        self.terms = []
        for key, st in stars.items():
            hv = hverts[key]
            # area gradient
            a_terms = []
            pairs = [(0, 1), (0, 2), (1, 2)]
            L2 = [self.L(hv[i], hv[j]) ** 2 for i, j in pairs]
            for n, (i, j) in enumerate(pairs):
                l = np.sqrt(L2[n]); up = list(L2); dn = list(L2)
                up[n] = (l + fd) ** 2; dn[n] = (l - fd) ** 2
                dA = (tri_area(up) - tri_area(dn)) / (2 * fd)
                c, anc = _key_pair(hv[i], hv[j]); a_terms.append((self.ekey[c], np.array(anc, float), dA))
            d_terms = []
            for si, T, tri in st:
                vs = [(tuple(np.add(v[0], T)), v[1]) for v in self.simp[si]]
                L2m = np.array([[self.L(vs[i], vs[j]) ** 2 for j in range(5)] for i in range(5)])
                m, n = [i for i in range(5) if i not in tri]
                for i, j in itertools.combinations(range(5), 2):
                    l = np.sqrt(L2m[i, j]); th = []
                    for sgn in (1, -1):
                        M = L2m.copy(); M[i, j] = M[j, i] = (l + sgn * fd) ** 2
                        th.append(dihedral(coords_from_lengths(M), tri, m, n))
                    dth = (th[0] - th[1]) / (2 * fd)
                    c, anc = _key_pair(vs[i], vs[j])
                    d_terms.append((self.ekey[c], np.array(anc, float), -dth))
            pack = lambda tl: (np.array([t[0] for t in tl]), np.array([t[1] for t in tl]), np.array([t[2] for t in tl]))
            self.terms.append((pack(a_terms), pack(d_terms)))

    def Q(self, k):
        k = np.asarray(k, complex); Q = np.zeros((self.E, self.E), complex)
        def row(t, kk):
            r = np.zeros(self.E, complex); np.add.at(r, t[0], t[2] * np.exp(1j * (t[1] @ kk))); return r
        for a, d in self.terms:
            Q += 0.5 * (np.outer(row(a, -k), row(d, k)) + np.outer(row(d, -k), row(a, k)))
        return Q

    def gauge(self, k):
        """vertex displacements xi_t e^{ik.b}: delta l = (xi_2 e^{ik.b2} - xi_1 e^{ik.b1}) . v/|v| per Bloch edge variable."""
        k = np.asarray(k, complex); nt = len(self.types); tix = {t: i for i, t in enumerate(self.types)}
        G = np.zeros((self.E, 4 * nt), complex)
        for (t1, t2, rel), c in self.ekey.items():
            v = self.evec[c]; u = self.g0 @ v / np.sqrt(v @ self.g0 @ v)
            G[c, 4 * tix[t2]:4 * tix[t2] + 4] += u * np.exp(1j * k @ np.array(rel, float))
            G[c, 4 * tix[t1]:4 * tix[t1] + 4] -= u
        return G

    def line_map(self, k):
        k = np.asarray(k, complex); HC = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        M = np.zeros((self.E, 10), complex)
        for (t1, t2, rel), c in self.ekey.items():
            v = self.evec[c]; l = np.sqrt(v @ self.g0 @ v); z = k @ v
            ph = np.exp(1j * k @ self.OFF[t1]) * (1.0 if abs(z) < 1e-14 else (np.exp(1j * z) - 1) / (1j * z))
            for j, (a, b) in enumerate(HC):
                M[c, j] = ph * v[a] * v[b] * (2 if a != b else 1) / (2 * l)
        return M

def d4cone():
    """D4 = Z^4 u (Z^4 + u/2) with each Delaunay 16-cell (centred at the deep holes (e_mu+e_nu)/2) coned from its centre."""
    pairs = list(itertools.combinations(range(4), 2))
    OFF = [np.zeros(4), 0.5 * np.ones(4)] + [0.5 * (np.eye(4)[m] + np.eye(4)[n]) for m, n in pairs]
    def as_vertex(p):
        p = np.asarray(p, float)
        if np.allclose(p, np.round(p)): return (tuple(int(x) for x in np.round(p)), 0)
        q = p - 0.5
        assert np.allclose(q, np.round(q)); return (tuple(int(x) for x in np.round(q)), 1)
    sims = []
    for h, (m, n) in enumerate(pairs):
        r, s = [i for i in range(4) if i not in (m, n)]
        c = OFF[2 + h]; E = np.eye(4)
        axes = [0.5 * (E[m] + E[n]), 0.5 * (E[m] - E[n]), 0.5 * (E[r] + E[s]), 0.5 * (E[r] - E[s])]
        for signs in itertools.product([1, -1], repeat=4):
            vs = [((0, 0, 0, 0), 2 + h)] + [as_vertex(c + sg * ax) for sg, ax in zip(signs, axes)]
            sims.append(vs)
    return OFF, sims



# ------------------------------------------------------------------ segments, stress, coupling
def segment_readings(C, k):
    """delta(l^2) of the 24 site-site segments through one cell (4 axes, 12 face diagonals through the deep holes,
    8 body diagonals through the centre) over edge variables, the design matrix in the 10 metric components, lengths."""
    E = np.eye(4, dtype=int); Z = (0, 0, 0, 0); k = np.asarray(k, complex); R, D, ls = [], [], []
    def seg(parts, l):
        r = np.zeros(C.E, complex)
        for (p, q) in parts:
            key, anc = _key_pair(p, q); r[C.ekey[key]] += 2 * l * np.exp(1j * k @ np.array(anc, float))
        return r
    def drow(v): return [v[a] * v[b] * (2 if a != b else 1) for a, b in HC]
    for mu in range(4):
        R.append(seg([((Z, 0), (tuple(E[mu]), 0))], 1.0)); D.append(drow(E[mu].astype(float))); ls.append(1.0)
    for h, (m, n) in enumerate(PAIRS):
        hv = (Z, 2 + h)
        R.append(seg([((Z, 0), hv), (hv, (tuple(E[m] + E[n]), 0))], np.sqrt(2))); D.append(drow((E[m] + E[n]).astype(float))); ls.append(np.sqrt(2))
        R.append(seg([((tuple(E[n]), 0), hv), (hv, (tuple(E[m]), 0))], np.sqrt(2))); D.append(drow((E[m] - E[n]).astype(float))); ls.append(np.sqrt(2))
    for sg in itertools.product([1, -1], repeat=3):
        s_ = np.array([1, *sg]); v0 = tuple(int(x) for x in (1 - s_) // 2); v1 = tuple(int(x) for x in (1 - s_) // 2 + s_)
        R.append(seg([((v0, 0), (Z, 1)), ((Z, 1), (v1, 0))], 2.0)); D.append(drow(s_.astype(float))); ls.append(2.0)
    return np.array(R), np.array(D, float), np.array(ls)


def K0(k): return np.sum(2 - 2 * np.cos(k))


def stress(k1, k2, c=-0.25, g=0.25):
    """corner stress for phi1 ~ e^{-i k1.x}, phi2 ~ e^{i k2.x}; returns S (4x4) and w = e^{-iq}, q = k2 - k1."""
    x, y = np.exp(-1j * k1), np.exp(1j * k2); w = 1 / (x * y); d = y - x; ww = w - 1
    return c * np.outer(d, d) + g * (np.outer(ww, ww) - np.eye(4) * (ww @ ww)), w, d, x, y


def min_stress(k1, k2):
    u = np.exp(-1j * k1) - 1; v = np.exp(1j * k2) - 1
    return 0.5 * (np.outer(u, v) + np.outer(v, u)) - 0.5 * np.eye(4) * (u @ v)


def strain_rows(w):
    """symbolic vertex-displacement relative strains of the 4 axis and 12 face segments (rows) per displacement component."""
    W = np.zeros((16, 4), complex); E = np.eye(4)
    for mu in range(4): W[mu] = 2 * (w[mu] - 1) * E[mu]
    for h, (m, n) in enumerate(PAIRS):
        W[4 + 2 * h] = (w[m] * w[n] - 1) * (E[m] + E[n]); W[5 + 2 * h] = (w[m] - w[n]) * (E[m] - E[n])
    return W


def couple(S, w, kappa=1 / 24):
    """local map of a corner stress to relative-strain couplings of the axis and face segments (body: 0), plus the
    gauge-blind face combination N_f = eps_+ + eps_- - (1/2)(four axis strains of the plaquette), weight kappa tr S."""
    b = np.zeros(24, complex)
    for nu in range(4): b[nu] += S[nu, nu] / 2
    for h, (m, n) in enumerate(PAIRS):
        b[4 + 2 * h] += S[m, n] / 2; b[5 + 2 * h] -= S[m, n] / 2
        b[m] -= (w[n] - 1) * S[m, n] / 4; b[n] -= (w[m] - 1) * S[m, n] / 4
    kap = kappa * np.trace(S)
    for h, (m, n) in enumerate(PAIRS):
        b[4 + 2 * h] += kap; b[5 + 2 * h] += kap; b[m] -= 0.5 * (1 + w[n]) * kap; b[n] -= 0.5 * (1 + w[m]) * kap
    return b


def scalar_coupling(k1, k2, ls, kappa=1 / 24):
    """symmetrised (real-action) coupling of the scalar bilinear phi1 phi2 to the segment rows delta(l^2)."""
    S1, w, *_ = stress(k1, k2); S2, w2, *_ = stress(-k2, -k1)
    assert np.allclose(w, w2)
    return (couple(S1, w, kappa) + couple(S2, w, kappa)) / ls ** 2


def onshell(rng, sc):
    ks = sc * (rng.standard_normal(3) + 1j * rng.standard_normal(3)); c = 1 + np.sum(2 - 2 * np.cos(ks)) / 2
    return np.array([*ks, np.arccos(c + 0j)])


def shell_from(ks):
    c = 1 + np.sum(2 - 2 * np.cos(ks)) / 2; return np.array([*ks, np.arccos(c + 0j)])


def pair_at(q, s, d, e):
    """Named finite complex Newton search, with shell residual and termination evidence."""
    best=float('inf')
    for attempt,t0 in enumerate((0.1,0.5,-0.5,1.0,-1.0,0.3j,-0.3j),1):
        t=t0*s;converged=False
        for iteration in range(60):
            f=lambda t:K0(shell_from(s*d+t*e)-q);h=1e-7
            value=f(t);derivative=(f(t+h)-f(t-h))/(2*h)
            if not np.isfinite(derivative) or abs(derivative)<1e-18:break
            step=value/derivative;t-=step
            if not np.isfinite(t):break
            if abs(step)<1e-15:converged=True;break
        if not np.isfinite(t):continue
        k3=shell_from(s*d+t*e);res=max(abs(K0(k3)),abs(K0(k3-q)));best=min(best,res)
        if res<1e-12:
            print(f'Newton shell scale={s} attempt={attempt} iterations={iteration+1} small_step={converged} residual={res:.6e}',flush=True)
            return k3,k3-q
    raise RuntimeError(f'No on-shell pair: best residual={best}')


def rank_svd(A,tol=1e-9):
    U,sv,Vh=np.linalg.svd(A,full_matrices=True)
    return int(np.count_nonzero(sv>tol)),U,sv

def Qinv(C,k):
    # Used only at real k. Hermitian complement is appropriate here; the
    # complex on-shell exchange below instead retains G(k)G(-k)^T.
    assert np.max(abs(np.imag(k)))==0
    Q=C.Q(k);G=C.gauge(k);r,U,sv=rank_svd(G);B=U[:,r:]
    reduced=B.conj().T@Q@B;inverse=np.linalg.inv(reduced)
    gauge_res=np.linalg.norm(Q@G)/(np.linalg.norm(Q)*np.linalg.norm(G))
    check(f'real-momentum gauge rank and reduced inverse fixture{PASS+FAIL+1} fd={C.fd} k={tuple(k)}',r==32 and gauge_res<1e-8 and np.linalg.norm(reduced@inverse-np.eye(len(reduced)))<1e-8,
          f'rank={r}; gauge_residual={gauge_res:.3e}; min_gauge_singular={sv[r-1]:.3e}')
    return B@inverse@B.conj().T,gauge_res

def partners(C,k):
    Q=C.Q(k);G=C.gauge(k);rg,Ug,sg=rank_svd(G)
    values,V=np.linalg.eigh((Q+Q.conj().T)/2);order=np.argsort(abs(values));values=values[order];V=V[:,order]
    A=np.hstack([C.line_map(k),G]);ra,Ua,sa=rank_svd(A,1e-10);projector=np.eye(C.E)-Ua[:,:ra]@Ua[:,:ra].conj().T
    # Test the assumed finite8-mode low non-gauge cluster, rather than
    # silently treating fixed eigenvector indices as established rank.
    low=V[:,rg:rg+8];projected=projector@low;U,sv,Vh=np.linalg.svd(projected,full_matrices=False)
    numerical_rank=int(np.count_nonzero(sv>1e-3));P=U[:,:2];PP=P@P.conj().T
    boundary_gap=abs(values[rg+8])/max(abs(values[rg+7]),1e-30)
    null_gap=abs(values[rg])/max(abs(values[rg-1]),1e-30)
    selected_gap=sv[1]/max(sv[2],1e-30)
    gauge_res=np.linalg.norm(Q@G)/(np.linalg.norm(Q)*np.linalg.norm(G))
    orth=np.linalg.norm(A.conj().T@P)/np.linalg.norm(A)
    check(f'finite partner cluster ranks and projector at k={tuple(k)}',rg==32 and ra==38 and numerical_rank==2 and boundary_gap>10 and null_gap>10 and selected_gap>20 and gauge_res<1e-8 and orth<1e-10 and np.linalg.norm(PP@PP-PP)<1e-12,
          json.dumps(dict(gauge_rank=rg,metric_gauge_rank=ra,projected_rank_at_1e_minus3=numerical_rank,singular_values=sv.tolist(),cluster_gap=boundary_gap,null_gap=null_gap,selected_gap=selected_gap,gauge_residual=gauge_res,orthogonality=orth)))
    return P


def T_of(S): return S / 2      # the coupling equals (1/2) c(S) . h on constant metrics (checked in E2)


def exact_ward_certificate():
    import sympy as sp
    x=sp.symbols('x0:4',nonzero=True);y=sp.symbols('y0:4',nonzero=True);w=[1/(a*b) for a,b in zip(x,y)];d=[b-a for a,b in zip(x,y)];u=[z-1 for z in w]
    delta=sum(a+1/a-b-1/b for a,b in zip(x,y));square=sum(z*z for z in u)
    S=sp.Matrix(4,4,lambda m,n:-d[m]*d[n]/4+(u[m]*u[n]-(square if m==n else 0))/4)
    for n in range(4):check(f'exact Laurent Ward component{n}',sp.cancel(sum(u[m]*S[m,n] for m in range(4))+d[n]*delta/4)==0)
    # Exact generic symmetric-stress map, and all six separate face null rows.
    entries=sp.symbols('t0:10');T=sp.zeros(4)
    for value,(m,n) in zip(entries,HC):T[m,n]=T[n,m]=value
    W=sp.zeros(16,4)
    for m in range(4):W[m,m]=2*u[m]
    b=sp.zeros(1,16)
    for m in range(4):b[m]=T[m,m]/2
    for h,(m,n) in enumerate(PAIRS):
        W[4+2*h,m]=W[4+2*h,n]=w[m]*w[n]-1;W[5+2*h,m]=w[m]-w[n];W[5+2*h,n]=-(w[m]-w[n])
        b[4+2*h]=T[m,n]/2;b[5+2*h]=-T[m,n]/2;b[m]-=u[n]*T[m,n]/4;b[n]-=u[m]*T[m,n]/4
        row=sp.zeros(1,16);row[4+2*h]=row[5+2*h]=1;row[m]=-(1+w[n])/2;row[n]=-(1+w[m])/2
        check(f'exact separate face-null row{m}{n}',all(sp.cancel(v)==0 for v in row*W))
    check('exact arbitrary symmetric stress-to-segment divergence',all(sp.cancel((b*W)[n]-sum(u[m]*T[m,n] for m in range(4)))==0 for n in range(4)))

def main():
    exact_ward_certificate()
    OFF, Sm = d4cone(); Dc = Complex(OFF, Sm); rng = np.random.default_rng(3)
    R0, D0, ls = segment_readings(Dc, np.zeros(4))
    print(f"D4 cone: {len(Sm)} simplices, {Dc.E} edge classes; NN site scalar K0 = sum_mu (2 - 2 cos k_mu)")

    # ---------------- E1 exact conservation identity, minimal at leading order
    worst = 0.0
    for _ in range(6):
        k1 = 0.6 * (rng.standard_normal(4) + 1j * rng.standard_normal(4)); k2 = 0.6 * (rng.standard_normal(4) + 1j * rng.standard_normal(4))
        S, w, d, x, y = stress(k1, k2); lhs = (w - 1) @ S; rhs = -0.25 * d * (K0(k2) - K0(k1))
        worst = max(worst, np.abs(lhs - rhs).max() / np.abs(lhs).max())
    mins = []; a1, a2 = rng.standard_normal(3) + 0.5j * rng.standard_normal(3), rng.standard_normal(3) + 0.5j * rng.standard_normal(3)
    for sc in (0.02, 0.01, 0.005):
        k1, k2 = shell_from(sc * a1), shell_from(sc * a2); S = stress(k1, k2)[0]; mins.append(np.linalg.norm(S - min_stress(k1, k2)) / np.linalg.norm(S))
    check("finite complex Ward residuals and three-scale on-shell leading-stress diagnostic",
          worst < 1e-13 and all(1.7 < mins[i] / mins[i + 1] < 2.3 for i in range(2)), f"identity residual {worst:.0e}; |S - S_min|/|S| " + ", ".join(f"{m:.1e}" for m in mins))

    # ---------------- E2 symbolic strain rows = carrier's code; the local map reproduces the divergence; normalisation
    q = np.array([0.31, -0.22, 0.17, 0.4]) + 0.1j * np.array([0.2, 0.1, -0.3, 0.05])
    Wc = (segment_readings(Dc, -q)[0] / ls[:, None] ** 2) @ Dc.gauge(-q); w = np.exp(-1j * q)
    expected_rows=np.zeros((16,32),complex);expected_rows[:,:4]=strain_rows(w)
    dev_rows = np.abs(Wc[:16] - expected_rows).max()
    S_ = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4)); S_ = S_ + S_.T
    dev_map = np.abs(couple(S_, w, 0.0)[:16] @ strain_rows(w) - (w - 1) @ S_).max()
    k1, k2 = 1e-3 * rng.standard_normal(4), 1e-3 * rng.standard_normal(4); h = rng.standard_normal(10); S0 = stress(k1, k2)[0]
    from_h = (couple(S0, np.exp(-1j * (k2 - k1)), 0.0) @ (D0 @ h / ls ** 2)) / (np.array([S0[a, b] * (1 if a == b else 2) for a, b in HC]) @ h)
    check("all32 carrier displacement columns, local stress map and constant-metric normalization",
          dev_rows < 1e-14 and dev_map < 1e-13 and abs(from_h - 0.5) < 3e-3, f"row dev {dev_rows:.0e}; map dev {dev_map:.0e}; normalisation {from_h.real:.4f}{from_h.imag:+.3e}j")

    # ---------------- E3 exact on-shell Ward identity of the symmetrised scalar coupling
    rows = []
    for sc in (0.5, 0.1, 0.02):
        k1, k2 = onshell(rng, sc), onshell(rng, sc); qq = k2 - k1
        WG = segment_readings(Dc, -qq)[0] @ Dc.gauge(-qq)
        r_on = []; r_off = []
        for kap in (0.0, 1 / 24):
            b = scalar_coupling(k1, k2, ls, kap); r_on.append(np.linalg.norm(b @ WG) / (np.linalg.norm(b) * np.linalg.norm(WG)))
        k1o = k1 * np.array([1, 1, 1, 1.1]); b = scalar_coupling(k1o, k2, ls); WGo = segment_readings(Dc, -(k2 - k1o))[0] @ Dc.gauge(-(k2 - k1o))
        rows.append((sc, max(r_on), np.linalg.norm(b @ WGo) / (np.linalg.norm(b) * np.linalg.norm(WGo))))
    check("all32-column on-shell scalar Ward fixtures and specified off-shell mutant",
          all(r[1] < 1e-12 and r[2] > 1e6 * r[1] for r in rows), "; ".join(f"scale {r[0]}: on {r[1]:.0e}, off {r[2]:.0e}" for r in rows))

    # ---------------- E4 the face combination is gauge-blind exactly and metric-blind at leading order
    out4 = []
    for s in (0.02, 0.01):
        qq = s * np.array([0.3, -0.5, 0.6, 0.55]); w = np.exp(-1j * qq)
        Nb = (couple(np.eye(4), w, 1.0) - couple(np.eye(4), w, 0.0)) / 4 / ls ** 2
        Rm = segment_readings(Dc, -qq)[0]
        out4.append((np.abs(Nb @ Rm @ Dc.gauge(-qq)).max() / np.abs(Nb).max(), np.abs(Nb @ Rm @ Dc.line_map(-qq)).max() / np.abs(Nb).max()))
    check("all32-column face-sum nullity and two-scale metric-reading diagnostic",
          all(o[0] < 1e-14 for o in out4) and out4[0][1] / out4[1][1] > 1.8, "; ".join(f"gauge {o[0]:.0e}, metric {o[1]:.1e}" for o in out4))

    # ---------------- E5 exchange between exactly conserved corner sources
    SYM = [(a, b) for a in range(4) for b in range(a, 4)]
    def cons_S(qq):
        w = np.exp(-1j * qq); A = np.zeros((4, 10), complex)
        for j, (a, b) in enumerate(SYM):
            E_ = np.zeros((4, 4)); E_[a, b] = E_[b, a] = 1; A[:, j] = (w - 1) @ E_
        U,sv,Vh=np.linalg.svd(A);rank=int(np.count_nonzero(sv>1e-10));assert rank==4
        N = Vh[rank:].conj(); out = []
        for v in N:
            T = np.zeros((4, 4), complex)
            for j, (a, b) in enumerate(SYM): T[a, b] = T[b, a] = v[j]
            out.append(T)
        return out, w
    res5={};directions={'axis':[0,1,0,0],'tick':[0,0,0,1],'generic':[.3,-.5,.6,.55],'body':[1,1,1,1]}
    for fd,C in [(1e-6,Dc),(2e-6,Complex(OFF,Sm,fd=2e-6))]:
        for scale in (.02,.01):
            for kap in (0.,1/24):
                for nm,d in directions.items():
                    d=np.array(d,float)/np.linalg.norm(d);qq=scale*d;Ss,w=cons_S(qq);Bs=np.array([couple(T,w,kap)/ls**2 for T in Ss]);inv,gauge_res=Qinv(C,qq)
                    K=np.conj(Bs)@segment_readings(C,qq)[0]@inv@segment_readings(C,-qq)[0].T@Bs.T*(qq@qq)
                    Ts=[T_of(T) for T in Ss];X=np.array([[np.sum(Ti.conj()*Tj),np.conj(np.trace(Ti))*np.trace(Tj)] for Ti in Ts for Tj in Ts])
                    co=np.linalg.lstsq(X,K.ravel(),rcond=None)[0];fit=np.linalg.norm(X@co-K.ravel())/np.linalg.norm(K.ravel());ward=np.linalg.norm(Bs@segment_readings(C,-qq)[0]@C.gauge(-qq))/(np.linalg.norm(Bs)*np.linalg.norm(segment_readings(C,-qq)[0]@C.gauge(-qq)))
                    res5[(fd,scale,kap,nm)]=(co,fit)
                    target=np.array([-4,4/3 if kap==0 else 2]);tol=3e-4*(scale/.01)**2
                    check(f'finite complex exchange fit fd={fd} scale={scale} weight={kap} direction={nm}',np.max(abs(co-target))<tol and np.isfinite(fit) and (fit<3e-3 if scale==.01 or nm!='generic' else True) and ward<1e-12,
                          json.dumps(dict(coefficients=[[z.real,z.imag] for z in co],fit_residual=fit,ward_residual=ward,carrier_gauge_residual=gauge_res,tolerance=tol)))
    # The generic corner-source finite-q tensor is not exactly in the two
    # continuum-invariant span. Test its measured first-order approach using
    # the existing two scales; retain the original .003 finest-scale bound.
    # Axis/tick/body are already below that bound and can reach the FD floor,
    # so no false monotone/asymptotic assertion is imposed on those fixtures.
    for fd,kap in itertools.product((1e-6,2e-6),(0.,1/24)):
        coarse=res5[(fd,.02,kap,'generic')][1];fine=res5[(fd,.01,kap,'generic')][1]
        ratio=coarse/fine
        check(f'finite generic tensor-fit approach fd={fd} weight={kap}',fine<3e-3 and 1.8<ratio<2.2,
              json.dumps(dict(coarse_residual=coarse,fine_residual=fine,halving_ratio=ratio,scope='Two supplied real momentum norms only; not a uniform continuum theorem')))
    for scale,kap,nm in itertools.product((.02,.01),(0.,1/24),directions):
        c1=res5[(1e-6,scale,kap,nm)][0];c2=res5[(2e-6,scale,kap,nm)][0];delta=np.linalg.norm(c1-c2)/np.linalg.norm(c1)
        check(f'finite-difference sensitivity scale={scale} weight={kap} direction={nm}',delta<1e-3,f'complex coefficient relative difference={delta:.6e}')

    # ---------------- E6 partner coupling of the scalar; gauge independence of the on-shell scalar exchange
    pr = []
    e1, e2 = rng.standard_normal(4), rng.standard_normal(4)
    for s in (0.02, 0.01):
        k1 = s * e1; k2 = s * e2; qq = k2 - k1; Rq = segment_readings(Dc, -qq)[0]; Pq = partners(Dc, -qq); Mq = Dc.line_map(-qq)
        pr.append(tuple(np.linalg.norm(scalar_coupling(k1, k2, ls, kap) @ Rq @ Pq) / np.linalg.norm(scalar_coupling(k1, k2, ls, kap) @ Rq @ Mq) for kap in (0.0, 1 / 24)))
    r6 = np.random.default_rng(11); ds = [r6.standard_normal(3) for _ in range(4)]; ds = [v / np.linalg.norm(v) for v in ds]; gd = []
    for s in (0.1, 0.05, 0.025):
        k1 = shell_from(s * ds[0]); k2 = shell_from(0.8 * s * ds[1]); qq = k2 - k1; k3, k4 = pair_at(qq, 0.9 * s, ds[2], ds[3])
        b1 = scalar_coupling(k1, k2, ls); b2 = scalar_coupling(k3, k4, ls); G, Gm = Dc.gauge(qq), Dc.gauge(-qq)
        right=segment_readings(Dc,-qq)[0].T@b1;left=b2@segment_readings(Dc,qq)[0];Q=Dc.Q(qq)
        ward=max(np.linalg.norm(left@G),np.linalg.norm(Gm.T@right))/max(np.linalg.norm(left),np.linalg.norm(right),1e-30)
        gauge_res=np.linalg.norm(Q@G)/(np.linalg.norm(Q)*np.linalg.norm(G));A=[];solve_res=[]
        for lam in (1.,10.):
            matrix=Q+lam*G@Gm.T;solution=np.linalg.solve(matrix,right);A.append(left@solution);solve_res.append(np.linalg.norm(matrix@solution-right)/np.linalg.norm(right))
        check(f'complex bilinear exchange residuals scale={s}',ward<1e-10 and gauge_res<1e-8 and max(solve_res)<1e-8,
              f'full32 source Ward={ward:.3e}; carrier gauge={gauge_res:.3e}; solves={solve_res}')
        gd.append(abs(A[1] - A[0]) / abs(A[0]))
    check("two-scale selected-partner suppression and three finite on-shell gauge-weight comparisons",
          all(p[0] > 0.3 and p[1] < 2e-2 for p in pr) and pr[0][1] / pr[1][1] > 1.8 and max(gd) < 1e-10,
          "partner " + "; ".join(f"{p[0]:.2f} -> {p[1]:.1e}" for p in pr) + "; gauge dependence " + ", ".join(f"{x:.0e}" for x in gd))

    print('per_element: Exact Laurent stress, arbitrary symmetric-source mapping and six separate face-null rows are symbolically certified.')
    print('per_site: All32 displacement columns including both site species and six centers are checked on the supplied96-simplex carrier.')
    print('per_mode: Gauge ranks, separated finite low cluster, selected projector, complex on-shell residuals and source conservation are reported.')
    print('per_block: Complex exchange fits retain imaginary parts, residuals and two finite-difference steps at two named momentum scales.')
    print('lattice_wide: Exact local Ward algebra only; uniform Einstein-Hilbert continuum exchange, partner decoupling, interacting action symmetry and physical identification remain unproved.')
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}",flush=True)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
