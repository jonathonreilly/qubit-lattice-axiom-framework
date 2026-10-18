"""B25 library: spectral vs unitary taste lattices.
Model chain: b25lib24.py = copy of B24's b24lib.py (import of b24base redirected to b25base.py = verbatim copy of b24base.py
= B23's b23lib.py -> B20_check/chklib.py -> B18_check/chk_model.py).  Nothing upstream is modified.
Adds:
  * taste detection on (pi/8)Z^3 (units pi/16 mod 32, all 4096 t) at random k:
      rotation-type   spec W(k+t) = w spec W(k)          (w = 1 part: Lambda_sp)
      reflection-type spec W(k+t) = w conj spec W(k)     (preserves the level E iff w = e^{2iE}; Lambda_sp(E) adds these)
  * k-independent intertwiner tests (null space of the linear map, two random k):
      'U'  W(k+t) V = V W(k)        (unitary taste, Lambda_u)
      'T'  W(k+t) V = V W(k)^T      (transpose taste)
      'I'  W(k+t) V = w V W(k)^dag  (reflection, unitary type)   'K'  W(k+t) V = w V W(k)^*  (reflection, antiunitary type)
  * lattice naming at scales 2pi .. pi/8 and point typing relative to two lattices (Lambda_u, Lambda_sp(E))."""
import os, sys, itertools, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from b25lib24 import *          # noqa
import numpy as np

_rng25 = np.random.default_rng(2525)
KT2 = _rng25.uniform(-np.pi, np.pi, (2, 3))
TV16 = np.array(list(itertools.product(range(0, 32, 2), repeat=3)))      # (pi/8)Z^3 in pi/16 units, 4096 points

def eig_sets(w, ks):
    return np.angle(np.linalg.eigvals(Wb(w, ks)))
def match_rot(e1, E2, tol=1e-6):
    """e1: (12,) phases at k; E2: (N,12) at k+t.  Returns (N,12) bool: candidate w_j = E2[:,0]-e1[j] works."""
    z1 = np.exp(1j * e1); Z2 = np.exp(1j * E2)
    om = Z2[:, :1] / z1[None, :]                       # (N,12) candidate omegas
    cand = om[:, :, None] * z1[None, None, :]          # (N,12,12) rotated spectra
    D = np.abs(cand[:, :, :, None] - Z2[:, None, None, :])   # (N,12,12,12)
    ok = (D.min(3).max(2) < tol) & (D.min(2).max(2) < tol)
    return ok, om
def tastes25(w):
    """dict with rotation and reflection tastes on (pi/8)Z^3: {t16: set of omegas (as angle rounded)}"""
    rot = None; ref = None
    for k in KT2:
        e1 = eig_sets(w, k[None])[0]
        E2 = eig_sets(w, k[None] + np.pi / 16 * TV16)
        okr, omr = match_rot(e1, E2); okf, omf = match_rot(-e1, E2)
        R = [set(np.round(np.angle(omr[i][okr[i]]), 5)) for i in range(len(TV16))]
        F = [set(np.round(np.angle(omf[i][okf[i]]), 5)) for i in range(len(TV16))]
        if rot is None: rot, ref = R, F
        else:
            rot = [{a for a in x if any(abs(wrap(a - b)) < 1e-4 for b in y)} for x, y in zip(rot, R)]
            ref = [{a for a in x if any(abs(wrap(a - b)) < 1e-4 for b in y)} for x, y in zip(ref, F)]
    return ({tuple(int(c) for c in t): s for t, s in zip(TV16, rot) if s}, {tuple(int(c) for c in t): s for t, s in zip(TV16, ref) if s})
def lam_sp(rot, ref=None, E=None):
    """Lambda_sp (w = 1 rotation tastes), optionally with the reflection tastes preserving level E (w = e^{2iE})."""
    L = {t for t, s in rot.items() if any(abs(wrap(a)) < 1e-4 for a in s)}
    if ref is not None and E is not None:
        L |= {t for t, s in ref.items() if any(abs(wrap(a - 2 * E)) < 1e-4 for a in s)}
    return L
def lname(L):
    """B24_check chk4 naming (units pi/16, mod 32): sc(a) = aZ^3; fcc(b) = {b x : x in Z^3, sum x even} (NN vector b(1,1,0));
    bcc(a) = aZ^3 + (a/2)(1,1,1).  '?n' if L is none of these."""
    for nm, S in LATS.items():
        if S == L: return nm
    return f"?{len(L)}"
def inter_dim(w, t16, kind, om=1.0, ks=None):
    ks = KT2 if ks is None else ks; rows = []
    for k in ks:
        A = Wb(w, (k + np.pi / 16 * np.asarray(t16))[None])[0]; B = Wb(w, k[None])[0]
        B = {'U': B, 'T': B.T, 'I': B.conj().T, 'K': B.conj()}[kind]
        rows.append(np.kron(A, np.eye(12)) - om * np.kron(np.eye(12), B.T))   # vec(A V - om V B) row-major
    u, s, vh = np.linalg.svd(np.vstack(rows)); null = vh[np.sum(s > 1e-8 * max(1, s[0])):].conj()
    if len(null) == 0: return 0
    # an intertwiner must be INVERTIBLE: test a generic element of the solution space (singular solutions only intertwine
    # sub-blocks and do not make t a taste).  Returns the solution-space dimension if a generic element is invertible, else 0.
    rg = np.random.default_rng(len(null))
    V = (rg.normal(size=len(null)) + 1j * rg.normal(size=len(null))) @ null
    sv = np.linalg.svd(V.reshape(12, 12), compute_uv=False)
    return len(null) if sv[-1] > 1e-6 * sv[0] else 0
def has_inter(w, t16, kinds=('U',), om=1.0): return {k: inter_dim(w, t16, k, om) for k in kinds}
def _lat(kind, a):
    S = set()
    for v in itertools.product(range(32), repeat=3):
        if kind == 'sc': ok = all(c % a == 0 for c in v)
        elif kind == 'fcc': ok = all(c % a == 0 for c in v) and sum(c // a for c in v) % 2 == 0
        else: ok = all(c % a == 0 for c in v) or all((c - a // 2) % a == 0 for c in v)
        if ok: S.add(tuple(v))
    return frozenset(S)
LATS = {f"sc({a})": _lat('sc', a) for a in (32, 16, 8, 4, 2)}
LATS.update({f"fcc({b})": _lat('fcc', b) for b in (16, 8, 4, 2)})
LATS.update({f"bcc({a})": _lat('bcc', a) for a in (32, 16, 8, 4)})
def lat_gens(nm):
    kind, a = nm.split('(')[0], int(nm.split('(')[1][:-1])
    if kind == 'sc': return [(a % 32, 0, 0)]
    if kind == 'fcc': return [(a % 32, a % 32, 0)]
    return [(a % 32, 0, 0), (a // 2, a // 2, a // 2)]
def lam_kind(w, Lsp, kind='U', om=1.0):
    """largest lattice of LATS inside Lsp all of whose generators have a k-independent intertwiner of this kind
    (kind 'U' with om = 1 gives Lambda_u; it is a group and O-invariant, hence one of LATS)."""
    cache = {}
    def ok(v):
        if v == (0, 0, 0): return True
        if v not in cache: cache[v] = inter_dim(w, v, kind, om) > 0
        return cache[v]
    for nm, L in sorted(LATS.items(), key=lambda x: -len(x[1])):
        if L <= Lsp and all(ok(g) for g in lat_gens(nm)): return nm
    return None
def lam_u(w, Lsp): return lam_kind(w, Lsp, 'U')
# good pairs (B24_check chk4_pairs, units pi/16) -- recomputed in b25 letter runner from scratch on (pi/32)Z^3

def prefilter(w, k, sign=1):
    """|tr W^p|, p=1..4, at k and at k + t (or -k + t if sign=-1) for all t: necessary for any rotation/reflection taste."""
    def inv(ks):
        Ws = Wb(w, ks); out = []; M = Ws.copy()
        for p in range(4):
            out.append(np.abs(np.trace(M, axis1=1, axis2=2))); M = M @ Ws
        return np.array(out).T
    a = inv(k[None])[0]; b = inv(sign * k[None] + np.pi / 16 * TV16)
    return np.abs(b - a[None]).max(1) < 1e-6
def tastes25(w, sign=1):
    """rotation and reflection tastes on (pi/8)Z^3: returns (rot, ref) dicts t16 -> set of omega angles.
    sign = -1: tastes with linear part -1 (k -> t - k) instead."""
    rot = ref = None
    for k in KT2:
        cand = prefilter(w, k, sign)
        idx = np.where(cand)[0]
        e1 = eig_sets(w, k[None])[0]
        E2 = eig_sets(w, sign * k[None] + np.pi / 16 * TV16[idx]) if len(idx) else np.zeros((0, 12))
        okr, omr = match_rot(e1, E2); okf, omf = match_rot(-e1, E2)
        R = {tuple(int(c) for c in TV16[i]): set(np.round(np.angle(omr[j][okr[j]]), 5)) for j, i in enumerate(idx)}
        F = {tuple(int(c) for c in TV16[i]): set(np.round(np.angle(omf[j][okf[j]]), 5)) for j, i in enumerate(idx)}
        if rot is None: rot, ref = R, F
        else:
            rot = {t: {a for a in x if any(abs(wrap(a - b)) < 1e-4 for b in R.get(t, ()))} for t, x in rot.items()}
            ref = {t: {a for a in x if any(abs(wrap(a - b)) < 1e-4 for b in F.get(t, ()))} for t, x in ref.items()}
    return {t: s for t, s in rot.items() if s}, {t: s for t, s in ref.items() if s}

# ---- good-pair table (same definition as B24_check chk4: C2pair(mod Lambda_u) within Tfix(mod Lambda_sp), linear action
#      around k*, (pi/32) grid); recomputed here, cached
_GOOD = None
ROT3 = []
for _p in itertools.permutations(range(3)):
    for _s in itertools.product((1, -1), repeat=3):
        _M = np.zeros((3, 3), int)
        for _i in range(3): _M[_i, _p[_i]] = _s[_i]
        if round(np.linalg.det(_M)) == 1: ROT3.append(_M)
_tr3 = [int(np.trace(R)) for R in ROT3]
ISTR = np.array([t in (3, 0) or (t == -1 and np.all(np.abs(np.diag(R)) == 1)) for R, t in zip(ROT3, _tr3)])
_C2 = [i for i, t in enumerate(_tr3) if t == -1]
C2PR = [(i, j) for i in _C2 for j in _C2 if i < j and np.array_equal(ROT3[i] @ ROT3[j], ROT3[j] @ ROT3[i])]
def good_table():
    global _GOOD
    if _GOOD is None:
        N = 64; grid = np.array(list(itertools.product(range(N), repeat=3))); FX = {}
        for nm, L in LATS.items():
            memb = np.zeros((N,) * 3, bool)
            for v in L: memb[tuple(2 * c for c in v)] = True
            FX[nm] = np.array([memb[tuple(((grid @ R.T - grid) % N).T)] for R in ROT3])
        _GOOD = {}
        for nu in LATS:
            p = np.zeros(len(grid), bool)
            for i, j in C2PR: p |= FX[nu][i] & FX[nu][j]
            for ns in LATS:
                if LATS[nu] <= LATS[ns]: _GOOD[(nu, ns)] = int((p & ~np.all(FX[ns][ISTR], axis=0)).sum()) == 0
    return _GOOD
def coset_reps(Ls, Lu, cap=256):
    reps = []; Lu = list(Lu)
    for t in sorted(Ls, key=lambda v: sum(min(c, 32 - c) for c in v)):
        if any(tuple((a - b) % 32 for a, b in zip(t, r)) in set_ for r in reps for set_ in [LATS_SET_CACHE(Lu)]): continue
        reps.append(t)
        if len(reps) >= cap: break
    return reps
_lsc = {}
def LATS_SET_CACHE(Lu):
    key = tuple(sorted(Lu))
    if key not in _lsc: _lsc[key] = set(Lu)
    return _lsc[key]
def analyse_word(w):
    """full taste census of one word: Lambda_sp, Lambda_u, coset kinds, reflection tastes (I/K), k-dependent tastes."""
    rot, ref = tastes25(w); Ls = lam_sp(rot); ns = lname(Ls)
    out = dict(Lsp=ns, nrot=len(rot), nref=len(ref))
    if ns.startswith('?'): out['Lu'] = None; return out
    nu = lam_u(w, Ls); out['Lu'] = nu; Lu = LATS[nu]
    reps = coset_reps(Ls, Lu); kinds = {}
    for t in reps[1:]:
        kinds[t] = ''.join(k for k in 'UT' if inter_dim(w, t, k) > 0)
    out['index'] = len(Ls) // len(Lu); out['kinds'] = collections.Counter(kinds.values())
    out['kdep'] = sum(1 for v in kinds.values() if v == '')
    out['good'] = good_table()[(nu, ns)]
    # reflection tastes: per omega, Lambda_sp(E) for E = omega/2 and omega/2 + pi
    oms = sorted({round(float(wrap(a + 1e-9)), 4) for s in ref.values() for a in s})
    out['refl'] = []
    for om in oms:
        LE = Ls | {t for t, s in ref.items() if any(abs(wrap(a - om)) < 1e-4 for a in s)}
        nE = lname(LE); g = good_table().get((nu, nE)) if not nE.startswith('?') else None
        tE = [t for t, s in ref.items() if any(abs(wrap(a - om)) < 1e-4 for a in s)][:1]
        kd = ''.join(k for k in 'IK' if tE and inter_dim(w, tE[0], k, np.exp(1j * om)) > 0)
        out['refl'].append((om, nE, g, kd))
    return out
