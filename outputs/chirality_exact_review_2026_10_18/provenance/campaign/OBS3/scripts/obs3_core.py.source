"""OBS-3 core: corner-basis Yukawa realisation -> one-loop corner/axis velocity tables -> counterterm-subtracted
residual -> mass-eigenstate SME rows.  Own assembly code (does not import OBS-2's sizes2.py); loop tables are
OBS-2's archived yuk_kin_* / yuk_flav_* JSON files (copied to tables/) plus OBS-3's range-2 tables (yuk3_kin_*).

Conventions (PREREG.md):
  T_f[c][a]  = velocity shift dv of field f at hw1 corner c (x,y,z = 0,1,2) along axis a.
  Higgs part : sum_{s,s'} Re(eta_s conj eta_s') I^var[c][(s,s')]   (I = B + S1 from yuk_lv.py, ordered double sum)
  Flavon part (M2): L field at c: sum_{c'!=c} |Y_cc'|^2 K(c,c');  R field at c: sum_{c'!=c} |Y_c'c|^2 K(c,c')
               K(c,c')[a] = own (a=c), partner (a=c'), third (other), from yuk_flav 'Qxy_sigma_c' dv.
  Residual   : r_c = T_c - iso - tet (e_c - 1/3),  iso = 9-entry mean, tet = corner-mean of (own - mean transverse).
  Eigenstate : left  dv_i(a) = sum_c |W_ci|^2 r_c(a);  right with |X_ci|^2.
               isotropic part computed in the exact delta form sum_c (|W_ci|^2 - 1/3) rho_c (sum_c rho_c = 0).
  SME        : vector = (L+R)/2, axial = (L-R)/2;  c_TT = -(3/4) dv_iso;  c-ring = (4/3) c_TT = -dv_iso.
"""
import json, os, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TAB = os.path.join(HERE, 'tables')
AX = 'xyz'

# ---------------------------------------------------------------- loop tables
def _order(syms):
    return {s: i for i, s in enumerate(syms)}

def key(a, b, syms):
    o = _order(syms)
    return a + b if o[a] <= o[b] else b + a

C3S = {'0': '0', 'x': 'y', 'y': 'z', 'z': 'x', 'X': 'Y', 'Y': 'Z', 'Z': 'X'}   # C3[111]: x->y->z->x
C3C = {'x': 'y', 'y': 'z', 'z': 'x'}

def load_kin(N, m, D, var, prefix='yuk_kin', symmetrise=True):
    """returns (I, syms): I[c][pairkey] -> np.array(3) of dv per axis (B + S1)."""
    fn = os.path.join(TAB, f"{prefix}_N{N}_m{m}_D{D}_mH{m}.json")
    r = json.load(open(fn))
    pairs = list(r['x'][var].keys())
    syms = []
    for p in pairs:
        for ch in p:
            if ch not in syms:
                syms.append(ch)
    order = [s for s in ['0', 'x', 'y', 'z', 'X', 'Y', 'Z'] if s in syms]
    I = {c: {k: np.array(r[c][var][k]['B']) + r[c][var][k]['S1'] for k in r[c][var]} for c in AX}
    if not symmetrise:
        return I, order
    out = {c: {} for c in AX}
    perm_axis = [1, 2, 0]   # under C3, axis a -> perm_axis[a]
    for c in AX:
        for k in I[c]:
            acc = np.zeros(3); cc, aa, bb = c, k[0], k[1]
            idx = np.arange(3)
            for g in range(3):
                acc += I[cc][key(aa, bb, order)][idx]
                cc, aa, bb = C3C[cc], C3S[aa], C3S[bb]
                idx = np.array([perm_axis[i] for i in idx])
            out[c][k] = acc / 3
    return out, order

def c3_violation(N, m, D, var, prefix='yuk_kin'):
    I, order = load_kin(N, m, D, var, prefix, symmetrise=False)
    perm_axis = [1, 2, 0]; mx = 0.0
    for c in AX:
        for k in I[c]:
            c2 = C3C[c]; k2 = key(C3S[k[0]], C3S[k[1]], order)
            v1 = I[c][k]; v2 = I[c2][k2]
            # value along axis a at (c,k) must equal value along perm_axis[a] at (C3 c, C3 k)
            mx = max(mx, max(abs(v1[a] - v2[perm_axis[a]]) for a in range(3)))
    return mx

def load_flav(N, m, D, kind='sigma_c'):
    f = json.load(open(os.path.join(TAB, f"yuk_flav_N{N}_m{m}_D{D}_mH{m}.json")))
    own, partner, third = f[f'Qxy_{kind}']['dv']
    chk = f[f'Qxz_{kind}']['dv']   # [own, third, partner]
    cov = max(abs(chk[0] - own), abs(chk[1] - third), abs(chk[2] - partner))
    return (own, partner, third), cov

def Kvec(c, c2, opt):
    own, partner, third = opt
    v = np.full(3, third); v[c] = own; v[c2] = partner
    return v

# ---------------------------------------------------------------- velocity tables for one sector
def higgs_T(I, syms, eta):
    """eta: dict symbol -> complex. returns 3x3 array T[c, a]."""
    T = np.zeros((3, 3))
    for ci, c in enumerate(AX):
        acc = np.zeros(3)
        for s in syms:
            for t in syms:
                w = (eta.get(s, 0) * np.conj(eta.get(t, 0))).real
                if w != 0.0:
                    acc += w * I[c][key(s, t, syms)]
        T[ci] = acc
    return T

def flavon_T(Y, opt, side):
    """side 'L': rows of Y; 'R': columns."""
    T = np.zeros((3, 3))
    for c in range(3):
        for c2 in range(3):
            if c2 == c:
                continue
            w = abs(Y[c, c2])**2 if side == 'L' else abs(Y[c2, c])**2
            T[c] += w * Kvec(c, c2, opt)
    return T

def eta_from_diag(dg, y0mode='trace', theta=0.0, y0=None, range2=False):
    """dg: complex corner-diagonal Yukawas Y_cc. Symbols: '0' on-site, x,y,z = g_c, X,Y,Z = g_c^2 (range 2)."""
    if y0 is None:
        y0 = np.mean(dg) if y0mode == 'trace' else 0.0
    eta = {'0': y0}
    for i, c in enumerate(AX):
        d = dg[i] - y0
        if range2:
            eta[c] = (1 - theta) * d; eta[c.upper()] = theta * d
        else:
            eta[c] = d
    return eta

SWAP = {'sym': 'sym', 'int': 'ext', 'ext': 'int'}

def sector_tables(Y, Itab, syms, opt, carrier, y0mode='trace', theta=0.0, y0=None):
    """Y: 3x3 corner-basis Yukawa. Itab: dict var -> I for the L field and the swapped var for R.
    returns (T_L, T_R) for one Yukawa sector (multiplicity applied by caller)."""
    eta = eta_from_diag(np.diag(Y), y0mode, theta, y0, range2=('X' in syms))
    TL = higgs_T(Itab['L'], syms, eta); TR = higgs_T(Itab['R'], syms, eta)
    if carrier == 'M2':
        TL = TL + flavon_T(Y, opt, 'L'); TR = TR + flavon_T(Y, opt, 'R')
    return TL, TR

# ---------------------------------------------------------------- counterterm split and eigenstates
def split(T):
    iso = T.mean()
    tet = np.mean([T[c, c] - np.mean([T[c, a] for a in range(3) if a != c]) for c in range(3)])
    r = T - iso - tet * (np.eye(3) - 1 / 3)
    return iso, tet, r

def eig_rows(Wcol2, r):
    """Wcol2: |W_ci|^2 for one eigenstate (3,), r: residual 3x3. returns (iso, aniso traceless vec)."""
    rho = r.mean(axis=1)                    # per-corner isotropic part, sum = 0 analytically
    iso = np.dot(Wcol2 - 1 / 3, rho - rho.mean())
    full = (Wcol2[:, None] * (r - rho[:, None])).sum(axis=0)
    return iso, full - full.mean()

# ---------------------------------------------------------------- inputs
def rot(t12, t23, t13, d):
    s12, c12, s23, c23, s13, c13 = np.sin(t12), np.cos(t12), np.sin(t23), np.cos(t23), np.sin(t13), np.cos(t13); e = np.exp(1j * d)
    return np.array([[c12 * c13, s12 * c13, s13 / e], [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])

def ckm_wolfenstein(lam, A, rb, eb):
    s12 = lam; s23 = A * lam**2
    z = A * lam**3 * (rb + 1j * eb) * np.sqrt(1 - A**2 * lam**4) / (np.sqrt(1 - lam**2) * (1 - A**2 * lam**4 * (rb + 1j * eb)))
    s13 = abs(z); d = np.angle(z)
    return rot(np.arcsin(s12), np.arcsin(s23), np.arcsin(s13), d)

deg = np.pi / 180
w3 = np.exp(2j * np.pi / 3)
F = np.array([[w3**(c * j) for j in range(3)] for c in range(3)]) / np.sqrt(3)
V_OBS2 = rot(13.04 * deg, 2.38 * deg, 0.201 * deg, 1.20)
U_PMNS = rot(33.4 * deg, 49.0 * deg, 8.57 * deg, 197 * deg)
INPUTS = {
    'obs2': dict(mu=np.array([2.16e-3, 1.27, 172.69]), md=np.array([4.67e-3, 0.0934, 4.18]), V=V_OBS2),
    'circ': dict(mu=np.array([2.16e-3, 1.2730, 172.57]), md=np.array([4.70e-3, 0.0935, 4.183]), V=np.eye(3)),
    'pdg24': dict(mu=np.array([2.16e-3, 1.2730, 172.57]), md=np.array([4.70e-3, 0.0935, 4.183]),
                  V=ckm_wolfenstein(0.22501, 0.826, 0.1591, 0.3523)),
}
ME = np.array([0.511e-3, 0.10566, 1.77686]); MNU = np.array([0.0, 8.6e-12, 5.0e-11])
VEV = 174.1

# fixed rows (PREREG rule 1): (one-sided lower bound on c-ring, |d-ring| bound)
FIXED = {'u': (3e-23, 3e-23), 'd': (1e-22, 1e-22)}
E_BOUNDS = dict(iso_neg=5e-21, iso_pos=2e-15, aniso=2e-20)        # OBS-2 sizes2.py:37 (D6)
SIDE = {'u33': 6e-22, 'd33': 3e-21,                                # D44 p3 c^(4)_33 rows (Schreck 2017*)
        'u_dis': 1.4e-4, 'd_dis': 1.0e-3,                          # D44 p1 ZEUS 2022 (tightest anisotropic combos, approx)
        's': 1e-9, 'c': 1e-8, 'b': 1e-7, 't': 1.6e-7}             # OBS-2 heavy/meson rows (mapping SUGGESTED)

# ---------------------------------------------------------------- full evaluation
def evaluate(real, tabs, scale_q=1.0, scale_l=1.0, inputs='pdg24'):
    """real: dict with Wu, Xu, Xd (3x3 unitary; Wd = Wu V), carrier, var, y0mode, theta, y0u, y0d.
    tabs: dict with 'I' (var -> I), 'syms', 'opt' (flavon kernel).  Returns dict of rows."""
    inp = INPUTS[inputs]; V = inp['V']
    if 'Yu' in real:      # textures supplied directly (SVD gives the embeddings)
        Yu = real['Yu'] * scale_q; Yd = real['Yd'] * scale_q
        Wu, Xu, Wd, Xd = real['Wu'], real['Xu'], real['Wd'], real['Xd']
    else:
        Wu = real['Wu']; Wd = Wu @ V; Xu = real['Xu']; Xd = real['Xd']
        Yu = Wu @ np.diag(inp['mu']) @ Xu.conj().T / VEV * scale_q
        Yd = Wd @ np.diag(inp['md']) @ Xd.conj().T / VEV * scale_q
    We = F; Ye = F @ np.diag(ME) @ F.conj().T / VEV * scale_l
    Yn = (F @ U_PMNS) @ np.diag(MNU) @ (F @ U_PMNS).conj().T / VEV * scale_l
    var = real.get('var', 'sym')
    It = {'L': tabs['I'][var], 'R': tabs['I'][SWAP[var]]}
    kw = dict(y0mode=real.get('y0mode', 'trace'), theta=real.get('theta', 0.0))
    car = real.get('carrier', 'M1')
    uL, uR = sector_tables(Yu, It, tabs['syms'], tabs['opt'], car, y0=real.get('y0u'), **kw)
    dL, dR = sector_tables(Yd, It, tabs['syms'], tabs['opt'], car, y0=real.get('y0d'), **kw)
    eL, eR = sector_tables(Ye, It, tabs['syms'], tabs['opt'], car, **kw)
    nL, nR = sector_tables(Yn, It, tabs['syms'], tabs['opt'], car, **kw)
    # residual per sector contribution (linear), summed per field
    def res(T):
        return split(T)
    parts = {'Q': [res(uL), res(dL)], 'uc': [res(2 * uR)], 'dc': [res(2 * dR)], 'L': [res(eL), res(nL)], 'ec': [res(2 * eR)]}
    fields = {f: (sum(p[0] for p in ps), sum(p[1] for p in ps), sum(p[2] for p in ps)) for f, ps in parts.items()}
    out = {'fields': fields, 'Yu': Yu, 'Yd': Yd}
    for sec, (Lf, Rf, WL, WR, names) in {'u': ('Q', 'uc', Wu, Xu, ('u', 'c', 't')), 'd': ('Q', 'dc', Wd, Xd, ('d', 's', 'b')),
                                          'e': ('L', 'ec', We, F, ('e', 'mu', 'tau'))}.items():
        for i, nm in enumerate(names):
            isoL, anL = eig_rows(np.abs(WL[:, i])**2, fields[Lf][2])
            isoR, anR = eig_rows(np.abs(WR[:, i])**2, fields[Rf][2])
            cring = -(isoL + isoR) / 2; dring = -(isoL - isoR) / 2
            can = -(anL + anR) / 2; dan = -(anL - anR) / 2
            out[nm] = dict(cring=cring, dring=dring, cTT=0.75 * cring, dTT=0.75 * dring, can=can, dan=dan)
    return out

def fixed_ratio(o):
    """max ratio over the FIXED rows (u, d rings; electron rows)."""
    r = {}
    for q in ('u', 'd'):
        bc, bd = FIXED[q]
        r[q + '_c'] = max(0.0, -o[q]['cring']) / bc
        r[q + '_d'] = abs(o[q]['dring']) / bd
    e = o['e']
    def iso_r(x):
        return (-x / E_BOUNDS['iso_neg']) if x < 0 else (x / E_BOUNDS['iso_pos'])
    r['e_iso'] = max(iso_r(e['cTT']), iso_r(e['dTT']))
    r['e_an'] = max(np.abs(e['can']).max(), np.abs(e['dan']).max()) / E_BOUNDS['aniso']
    return max(r.values()), r

def side_ratio(o):
    r = {}
    r['u33'] = max(np.abs(o['u']['can']).max(), np.abs(o['u']['dan']).max()) / SIDE['u33']
    r['d33'] = max(np.abs(o['d']['can']).max(), np.abs(o['d']['dan']).max()) / SIDE['d33']
    r['u_dis'] = max(np.abs(o['u']['can']).max(), np.abs(o['u']['dan']).max()) / SIDE['u_dis']
    r['d_dis'] = max(np.abs(o['d']['can']).max(), np.abs(o['d']['dan']).max()) / SIDE['d_dis']
    for q in ('s', 'c', 'b', 't'):
        r[q] = max(abs(o[q]['cTT']), abs(o[q]['dTT']), np.abs(o[q]['can']).max(), np.abs(o[q]['dan']).max()) / SIDE[q]
    return r

def get_tabs(N, m, D, prefix='yuk_kin', kind='sigma_c', flavN=None):
    I = {}; syms = None
    for var in ('sym', 'int', 'ext'):
        I[var], syms = load_kin(N, m, D, var, prefix)
    fN = flavN or (N if N >= 32 else 32)
    opt, cov = load_flav(fN, m, D, kind)
    return dict(I=I, syms=syms, opt=opt, flavcov=cov)

BRACKET = [(m, D) for m in ('0.1', '0.05', '0.025') for D in ('0.0', '0.5')]
