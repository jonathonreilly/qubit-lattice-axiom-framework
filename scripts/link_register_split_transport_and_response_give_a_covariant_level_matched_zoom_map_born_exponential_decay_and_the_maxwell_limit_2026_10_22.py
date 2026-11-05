AUDIT_INPUT_PATHS = ('docs/LINK_REGISTER_SPLIT_TRANSPORT_AND_RESPONSE_GIVE_A_COVARIANT_LEVEL_MATCHED_ZOOM_MAP_BORN_EXPONENTIAL_DECAY_AND_THE_MAXWELL_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""register-consistency: three gaps of the link-register law (CL-1 links, CL-2 cost, CL-3 continuum).

A. SPLIT: block Gauss identity; Z_3 toy (parent 2x1 torus -> children 4x2 torus) with the
   conditional-vacuum passing, the nearest vacuum-carrying unitary and the level-matched unitary.
B. CL-2 COST: emitter + truncated link-mode chain under block half-ticks; actual-configuration
   waiting times vs Born and Wigner-Weisskopf; occupation-only vs occupation+electric cost.
C. CONTINUUM: register photon band from the plaquette phase, Coulomb law from Gauss, departure
   energy (vacuum-standard) of register states and its edge response.
Labels: [T] exact theorem check, [D] finite diagnostic, [E] estimate against measurement.
"""
import time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = [0, 0]


def check(ok, label, detail=""):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" | {detail}" if detail else ""))


# ---------------------------------------------------------------- A. split
print("== A. split: children's link registers")


def cubic_links(L, d=3):
    """links (v, axis) of the L^d torus; returns divergence matrix D (V x Lk)."""
    V = L ** d
    coords = np.array(np.unravel_index(np.arange(V), (L,) * d)).T
    rows, cols, vals = [], [], []
    for v in range(V):
        for a in range(d):
            l = v * d + a
            w = coords[v].copy(); w[a] = (w[a] + 1) % L
            u = np.ravel_multi_index(tuple(w), (L,) * d)
            rows += [v, u]; cols += [l, l]; vals += [1, -1]   # outflow at v, inflow at u
    return sp.csr_matrix((vals, (rows, cols)), shape=(V, V * d)), coords


Lp = 3
Dp, cp = cubic_links(Lp)
Dc, cc = cubic_links(2 * Lp)
Vc = (2 * Lp) ** 3
# R: children's block sum; S: parent face total = sum of the 4 child bonds crossing that face
R = sp.csr_matrix((np.ones(Vc), (np.ravel_multi_index(tuple((cc // 2).T), (Lp,) * 3), np.arange(Vc))),
                  shape=(Lp ** 3, Vc))
Srows, Scols = [], []
for v in range(Vc):
    for a in range(3):
        if cc[v][a] % 2 == 1:   # child bond leaving the +a children of a block across the block face
            I = np.ravel_multi_index(tuple(cc[v] // 2), (Lp,) * 3)
            Srows.append(I * 3 + a); Scols.append(v * 3 + a)
S = sp.csr_matrix((np.ones(len(Srows)), (Srows, Scols)), shape=(3 * Lp ** 3, 3 * Vc))
res = abs(R @ Dc - Dp @ S).max()
nper = np.diff(S.indptr)
check(res == 0 and set(nper) == {4},
      "[T] A1 a block's eight child Gauss laws sum to the parent's exactly when each parent bond's electric"
      " value is the total of the 4 child bonds crossing its face and the block charge is the children's total"
      " (R D_c = D_p S, integer identity; 12 internal bonds per block are unconstrained by it)",
      f"3^3 -> 6^3 torus, max |R D_c - D_p S| = {res}, child bonds per face {sorted(set(nper))}")

# Z_N toy on 2D tori
N = 3
cosN = lambda e: (1 - np.cos(2 * np.pi * e / N)) / (2 * (1 - np.cos(2 * np.pi / N)))   # h(+-1)=1/2


def torus2(Lx, Ly):
    nl = 2 * Lx * Ly
    xl = lambda i, j: 2 * ((i % Lx) * Ly + (j % Ly))
    yl = lambda i, j: 2 * ((i % Lx) * Ly + (j % Ly)) + 1
    plaq = []
    for i in range(Lx):
        for j in range(Ly):
            v = np.zeros(nl, int)
            v[xl(i, j)] += 1; v[yl(i + 1, j)] += 1; v[xl(i, j + 1)] -= 1; v[yl(i, j)] -= 1
            plaq.append(v % N)
    wx = np.zeros(nl, int); wy = np.zeros(nl, int)
    for i in range(Lx): wx[xl(i, 0)] = 1
    for j in range(Ly): wy[yl(0, j)] = 1
    gens = plaq[:-1] + [wx, wy]
    dim = len(gens)
    params = np.array(np.unravel_index(np.arange(N ** dim), (N,) * dim)).T
    confs = (params @ np.array(gens)) % N
    keys = confs @ (N ** np.arange(nl))
    order = np.argsort(keys)
    return dict(nl=nl, xl=xl, yl=yl, plaq=plaq, confs=confs, keys=keys, order=order,
                wind=params[:, -2:], Lx=Lx, Ly=Ly)


def index_of(T, confs):
    k = (confs % N) @ (N ** np.arange(T["nl"]))
    pos = np.searchsorted(T["keys"][T["order"]], k)
    pos = np.minimum(pos, len(k) - 1) if np.ndim(pos) else pos
    idx = T["order"][pos]
    assert np.all(T["keys"][idx] == k)
    return idx


def ham(T, g2):
    n = len(T["confs"])
    diag = g2 * cosN(T["confs"]).sum(1)
    rows, cols = [], []
    for p in T["plaq"]:
        j = index_of(T, T["confs"] + p)
        rows.append(np.arange(n)); cols.append(j)
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    Up = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    return sp.diags(diag) - (Up + Up.T) / (2 * g2)


P_ = torus2(2, 1); C_ = torus2(4, 2)
g2p = 1.5; g2c = g2p / 2            # 2+1D: g^2 = e^2 a
Hp = ham(P_, g2p).toarray() / 1.0  # physical energy = H_lat / a, a_p = 1
Hc = ham(C_, g2c) / 0.5            # a_c = 1/2
check(len(set(P_["keys"])) == len(P_["keys"]) and len(set(C_["keys"])) == len(C_["keys"])
      and abs(Hc - Hc.T).max() < 1e-12,
      "[T] A2 Z_3 registers: plaquette loops + 2 windings parametrise every Gauss-law configuration once;"
      " the Kogut-Susskind plaquette/electric Hamiltonian is Hermitian on it",
      f"parent 2x1 dim {len(P_['keys'])}, children 4x2 dim {len(C_['keys'])}")

# face totals of the children's configurations
def face_totals(T):
    c = T["confs"]; out = np.zeros((len(c), P_["nl"]), int)
    for i in range(P_["Lx"]):
        for j in range(P_["Ly"]):
            out[:, P_["xl"](i, j)] = c[:, C_["xl"](2 * i + 1, 2 * j)] + c[:, C_["xl"](2 * i + 1, 2 * j + 1)]
            out[:, P_["yl"](i, j)] = c[:, C_["yl"](2 * i, 2 * j + 1)] + c[:, C_["yl"](2 * i + 1, 2 * j + 1)]
    return out % N


ft = face_totals(C_)
pidx = index_of(P_, ft)                   # every child configuration's face totals form a parent configuration
wp = P_["wind"][:, 0] * N + P_["wind"][:, 1]
wc = C_["wind"][:, 0] * N + C_["wind"][:, 1]
nP = len(P_["keys"]); nC = len(C_["keys"])


def shift_perm(T, s):
    """translation by s sites along x as a permutation of the Gauss-law basis (parent 1 <-> children 2)"""
    c = T["confs"]; new = np.zeros_like(c)
    for i in range(T["Lx"]):
        for j in range(T["Ly"]):
            new[:, T["xl"](i + s, j)] = c[:, T["xl"](i, j)]; new[:, T["yl"](i + s, j)] = c[:, T["yl"](i, j)]
    return index_of(T, new)


tp, tc = shift_perm(P_, 1), shift_perm(C_, 2)
assert np.all(tp[tp] == np.arange(nP)) and np.all(tc[tc] == np.arange(nC)) and np.all(wp[tp] == wp) and np.all(wc[tc] == wc)


def parity_basis(idx, perm, sgn):
    """orthonormal basis (columns, global indices) of the T = sgn subspace of the span of idx"""
    rows, cols, vals, k = [], [], [], 0
    seen = set()
    for i in idx:
        if i in seen: continue
        j = perm[i]; seen.update([i, j])
        if j == i:
            if sgn > 0: rows.append(i); cols.append(k); vals.append(1.0); k += 1
        else:
            rows += [i, j]; cols += [k, k]; vals += [2 ** -0.5, sgn * 2 ** -0.5]; k += 1
    return sp.csr_matrix((vals, (rows, cols)), shape=(len(perm), k))


vp_l, ep_l, sp_l, vc_l, ec_l, sc_l = [], [], [], [], [], []
Hp_s = sp.csr_matrix(Hp)
for w_ in range(N * N):
    for par in (1, -1):
        lab = 2 * w_ + (par < 0)
        Bp = parity_basis(np.where(wp == w_)[0], tp, par)
        if Bp.shape[1]:
            e_, v_ = np.linalg.eigh((Bp.T @ Hp_s @ Bp).toarray())
            for k in range(len(e_)):
                vp_l.append(Bp @ v_[:, k]); ep_l.append(e_[k]); sp_l.append(lab)
        Bc = parity_basis(np.where(wc == w_)[0], tc, par)
        Mc_ = (Bc.T @ Hc @ Bc).tocsr()
        e_, v_ = spla.eigsh(Mc_, k=6, which="SA", v0=np.ones(Mc_.shape[0]))
        for k in np.argsort(e_):
            vc_l.append(Bc @ v_[:, k]); ec_l.append(e_[k]); sc_l.append(lab)
vp = np.array(vp_l).T; ep = np.array(ep_l); sp_lab = np.array(sp_l)
vc = np.array(vc_l).T; ec = np.array(ec_l); sc_lab = np.array(sc_l)
o = np.argsort(ep, kind="stable"); vp, ep, sp_lab = vp[:, o], ep[o], sp_lab[o]
o = np.argsort(ec, kind="stable"); vc, ec, sc_lab = vc[:, o], ec[o], sc_lab[o]
assert vp.shape == (nP, nP) and ep[1] - ep[0] > 1e-6 and ec[1] - ec[0] > 1e-6
Om_c = vc[:, 0]; Om_p = vp[:, 0]
# conditional-vacuum passing: parent configuration n -> children's vacuum on configurations with face totals n
Pm = np.zeros((nC, nP))
# 'as in the children's vacuum' read in each electric-flux (winding) sector: that sector's lowest state
sec_vac = {s_: vc[:, [k for k in range(len(ec)) if sc_lab[k] // 2 == s_][0]] for s_ in range(N * N)}
amp = np.zeros(nC)
for s_ in range(N * N):
    amp[wc == s_] = sec_vac[s_][wc == s_]
Pm[np.arange(nC), pidx] = amp
wmatch = np.all(wp[pidx] == wc)
norms = np.linalg.norm(Pm, axis=0)
Pm /= norms
check(wmatch and norms.min() > 1e-6 and abs(Pm.T @ Pm - np.eye(nP)).max() < 1e-12,
      "[T] A3 the passing 'face totals = parent values, everything else as in the children's vacuum of the"
      " same flux sector' is an isometry into the children's Gauss-law space (disjoint face totals; face"
      " totals carry the winding; the global vacuum alone has no weight off the zero-flux sector)",
      f"min weight {norms.min()**2:.3e}, ||P^T P - 1|| {abs(Pm.T @ Pm - np.eye(nP)).max():.1e}")


def polar(A):
    U, s, Wt = np.linalg.svd(A, full_matrices=False)
    return U @ Wt


Qc = lambda X: X - np.outer(Om_c, Om_c @ X)
Pin = Pm @ (np.eye(nP) - np.outer(Om_p, Om_p))
Vstar = np.outer(Om_c, Om_p) + polar(Qc(Pin) @ vp[:, 1:]) @ vp[:, 1:].T
E0c, E0p = ec[0], ep[0]


def excess(V, n):
    psi = V @ vp[:, n]
    return psi @ (Hc @ psi) - E0c - (ep[n] - E0p)


heatP0 = excess(Pm, 0); heatV0 = excess(Vstar, 0)
dist = lambda V: np.linalg.norm(V - Pm)
# nearest check: random isometries with V Om_p = Om_c
rng = np.random.default_rng(1)
worse = 0
for _ in range(20):
    X = Qc(rng.normal(size=(nC, nP - 1))) * 1e-2
    Vr = np.outer(Om_c, Om_p) + polar(Qc(Pin) @ vp[:, 1:] + X) @ vp[:, 1:].T
    worse += dist(Vr) > dist(Vstar) - 1e-12
check(abs(Vstar.T @ Vstar - np.eye(nP)).max() < 1e-10 and abs(Vstar @ Om_p - Om_c).max() < 1e-12
      and worse == 20 and heatP0 > 1e-3 and abs(heatV0) < 1e-10,
      "[T] A4 the nearest isometry carrying the vacuum onto the children's vacuum is"
      " V* = |Om_c><Om_p| + polar(Q_c P Q_p); it heats the vacuum by 0, the bare passing does not",
      f"vacuum heat: passing {heatP0:.4f}, V* {heatV0:.1e}; 20/20 perturbed constrained isometries farther: {worse}")

# gauge/winding/translation covariance
leakW = max(abs(Vstar[np.ix_(wc == a, wp == b)]).max() for a in range(N * N) for b in range(N * N) if a != b)
Tp = np.eye(nP)[tp].T; Tc = sp.csr_matrix((np.ones(nC), (tc, np.arange(nC))), shape=(nC, nC))
covT = abs(Tc @ Vstar - Vstar @ Tp).max()
check(leakW < 1e-12 and covT < 1e-8,
      "[T] A5 V* is gauge covariant by construction (all states Gauss-law), conserves the electric winding"
      " sectors and commutes with translations (parent shift 1 <-> children shift 2): the polar part of a"
      " covariant map is covariant",
      f"cross-sector weight {leakW:.1e}, ||T_c V* - V* T_p|| {covT:.1e}")

# level-matched unitary: per winding sector, vacuum->vacuum then polar onto the children's next levels
Vm = np.outer(Om_c, Om_p)
for s_ in range(2 * N * N):
    ps = [k for k in range(1, nP) if sp_lab[k] == s_]
    cs = [k for k in range(1, vc.shape[1]) if sc_lab[k] == s_][:len(ps)]
    if ps:
        A = vc[:, cs].T @ Pm @ vp[:, ps]
        Vm += vc[:, cs] @ polar(A) @ vp[:, ps].T
Vm_ok = abs(Vm.T @ Vm - np.eye(nP)).max()
exP = np.array([excess(Pm, n) for n in range(nP)])
exS = np.array([excess(Vstar, n) for n in range(nP)])
low = vc  # 6 lowest per winding sector
leakS = 1 - np.mean([np.linalg.norm(low.T @ (Vstar @ vp[:, n])) ** 2 for n in range(1, nP)])
leakM = 1 - np.mean([np.linalg.norm(low.T @ (Vm @ vp[:, n])) ** 2 for n in range(1, nP)])
covTm = abs(Tc @ Vm - Vm @ Tp).max()
check(Vm_ok < 1e-10 and abs(Vm @ Om_p - Om_c).max() < 1e-8 and leakM < 1e-12 and leakS > 0.05 and covTm < 1e-8,
      "[D] A6 vacuum-only carrying is not enough: V* sends the parent's excited levels mostly outside the"
      " children's 6 lowest levels per (flux, momentum) sector, i.e. it heats; the level-matched polar map (vacuum"
      " to vacuum, each sector's levels onto the children's lowest levels of that sector) exists, is covariant and"
      " leaves nothing above the matched window",
      f"weight outside low window: V* {leakS:.2f}, matched {leakM:.0e}; mean |excess| passing {abs(exP[1:]).mean():.2f},"
      f" V* {abs(exS[1:]).mean():.2f}; matched-map translation residual {covTm:.1e}")
print(f"   parent gap {ep[1]-ep[0]:.3f}, children gap {ec[1]-ec[0]:.3f} (physical units, g_p^2={g2p})")

# ---------------------------------------------------------------- B. CL-2 cost
print("== B. CL-2 cost: emitter + link-register chain")
g, J, dt, Lch = 0.15, 1.0, 0.05, 420
GammaWW = 2 * g * g / J
n = Lch + 1                              # 0 = excited emitter, j = one quantum on chain link j
bonds = [(0, 1, g)] + [(j, j + 1, J) for j in range(1, Lch)]
even = [b for k, b in enumerate(bonds) if k % 2 == 0]; odd = [b for k, b in enumerate(bonds) if k % 2 == 1]


def blocks(bl):
    a = np.array([b[0] for b in bl]); c = np.array([b[1] for b in bl]); h = np.array([b[2] for b in bl])
    return a, c, np.cos(h * dt), -1j * np.sin(h * dt)


def apply(psi, B):
    a, c, co, si = B
    pa, pc = psi[a].copy(), psi[c].copy()
    psi[a] = co * pa + si * pc; psi[c] = si * pa + co * pc
    return psi


BE, BO = blocks(even), blocks(odd)
psi = np.zeros(n, complex); psi[0] = 1
steps = int(7 / GammaWW / dt)
Pe = np.empty(steps + 1); Surv = np.empty(steps + 1); Pe[0] = Surv[0] = 1
jumps_min = jumps_ent = 0.0
monotone = True
partner = {}
rng = np.random.default_rng(7)
M = 20000
cur = np.zeros(M, int); tleave = np.full(M, np.inf)


def half(psi, B, t):
    """advance odds by a block half-tick; return per-state move probability under the minimal plan
    and the entropic (product) plan on cost-free pairs."""
    global jumps_min, jumps_ent
    a, c, _, _ = B
    p0a, p0c = abs(psi[a]) ** 2, abs(psi[c]) ** 2
    psi = apply(psi, B)
    p1a, p1c = abs(psi[a]) ** 2, abs(psi[c]) ** 2
    move = np.zeros(n); dest = np.arange(n)
    d = p1c - p0c                         # mass a -> c if d > 0
    with np.errstate(divide="ignore", invalid="ignore"):
        move[a] = np.where(d > 0, np.where(p0a > 0, d / p0a, 0), 0)
        move[c] = np.where(d < 0, np.where(p0c > 0, -d / p0c, 0), 0)
    dest[a] = c; dest[c] = a
    m = p0a + p0c
    chain = a > 0
    jumps_min += abs(d[chain]).sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        jumps_ent += np.where(m[chain] > 0, (p0a * p1c + p0c * p1a)[chain] / m[chain], 0).sum()
    return psi, np.clip(move, 0, 1), dest


for s in range(steps):
    psi, mv, de = half(psi, BE, s)
    flip = rng.random(M) < mv[cur]
    leaving = flip & (cur == 0) & np.isinf(tleave)
    tleave[leaving] = (s + 0.5) * dt
    cur = np.where(flip, de[cur], cur)
    Surv[s + 1] = Surv[s] * (1 - mv[0])
    psi, mv, de = half(psi, BO, s)
    flip = rng.random(M) < mv[cur]
    cur = np.where(flip, de[cur], cur)
    Pe[s + 1] = abs(psi[0]) ** 2
    monotone &= Pe[s + 1] <= Pe[s] + 1e-15
t = np.arange(steps + 1) * dt
check(monotone and abs(Surv - Pe).max() < 1e-12,
      "[T] B1 block half-ticks: in every two-configuration block a cost that charges any change makes the plan"
      " unique (move exactly the shortfall); with P_e falling at every half-tick the actual configuration's"
      " survival in the excited level equals the Born P_e(t) exactly",
      f"max |S - P_e| {abs(Surv - Pe).max():.1e} over {steps} ticks, t_max = {t[-1]*GammaWW:.1f}/Gamma")
win = (t > 1 / GammaWW) & (t < 6 / GammaWW)
rate = -np.polyfit(t[win], np.log(Surv[win]), 1)[0]
emp = np.array([np.mean(tleave > tt) for tt in t[win][::200]])
ks = np.abs(emp - np.exp(-GammaWW * t[win][::200])).max()
bins = np.minimum(np.arange(n) // 20, n // 20)
born_end = np.abs(np.bincount(bins[cur], minlength=bins.max() + 1) / M
                  - np.bincount(bins, weights=abs(psi) ** 2, minlength=bins.max() + 1)).sum() / 2
check(abs(rate / GammaWW - 1) < 0.02 and ks < 0.02 and born_end < 0.03,
      "[E] B2 the actual configuration's waiting times are exponential at the Wigner-Weisskopf rate"
      " Gamma = 2 g^2/J (end-coupled link chain at band centre); sampled trajectories keep Born odds",
      f"fitted rate/Gamma_WW {rate/GammaWW:.4f}; 20000 sampled leave times: max |S_emp - e^-Gt| {ks:.3f};"
      f" end-time TV(actual, |psi|^2) on 20-link bins {born_end:.3f}. Measured: hydrogen 2p exponential, tau 1.60 ns")
print(f"   photon jumps per tick on the chain: fewest changes incl. electric values {jumps_min/steps:.4f},"
      f" occupation-only cost + greatest entropy {jumps_ent/steps:.3f}")
# stationary register state on a free chain link pair: occupation-only cost lets the quantum flip
# Floquet eigenstate of a closed chain of link registers (no emitter)
Lr = 24
Hch = np.zeros((Lr, Lr))
for j in range(Lr - 1): Hch[j, j + 1] = Hch[j + 1, j] = J
from scipy.linalg import expm
UE = np.eye(Lr, dtype=complex); UO = np.eye(Lr, dtype=complex)
for j in range(Lr - 1):
    h = np.zeros((Lr, Lr)); h[j, j + 1] = h[j + 1, j] = J
    (UE if j % 2 == 0 else UO)[:] = expm(-1j * dt * 8 * h) @ (UE if j % 2 == 0 else UO)
w, Fv = np.linalg.eig(UO @ UE)
f = Fv[:, 3] / np.linalg.norm(Fv[:, 3])
jm = je = 0.0
for B in (UE, UO):
    p0 = abs(f) ** 2; f = B @ f; p1 = abs(f) ** 2
    for j in range((0 if B is UE else 1), Lr - 1, 2):
        m = p0[j] + p0[j + 1]
        jm += abs(p1[j + 1] - p0[j + 1]); je += (p0[j] * p1[j + 1] + p0[j + 1] * p1[j]) / m
check(je > 10 * jm,
      "[D] B3 with occupation-only cost every move of a link quantum along the chain is free, so greatest"
      " entropy flips the actual electric values at O(1) per tick even in a stationary register state;"
      " counting electric-value changes restores the forced (current-sized) motion",
      f"Floquet eigenstate of a 24-link chain: actual jumps/tick minimal {jm:.3f}, entropic {je:.3f}")

# ---------------------------------------------------------------- C. continuum
print("== C. continuum: Maxwell limit for registers")
L = 4
D3, c3 = cubic_links(L)
nl = D3.shape[1]
# curl: plaquettes (v, a<b): A(v,a) + A(v+a,b) - A(v+b,a) - A(v,b)
rows, cols, vals = [], [], []
V3 = L ** 3; pi_ = 0
for v in range(V3):
    for a in range(3):
        for b in range(a + 1, 3):
            va = c3[v].copy(); va[a] = (va[a] + 1) % L
            vb = c3[v].copy(); vb[b] = (vb[b] + 1) % L
            ua = np.ravel_multi_index(tuple(va), (L,) * 3); ub = np.ravel_multi_index(tuple(vb), (L,) * 3)
            for (u, ax, s) in ((v, a, 1), (ua, b, 1), (ub, a, -1), (v, b, -1)):
                rows.append(pi_); cols.append(u * 3 + ax); vals.append(s)
            pi_ += 1
Cu = sp.csr_matrix((vals, (rows, cols)), shape=(pi_, nl)).toarray()
K = Cu.T @ Cu
lam = np.sort(np.linalg.eigvalsh(K))
ks = 2 * np.pi * np.array(np.unravel_index(np.arange(V3), (L,) * 3)).T / L
lk = (4 * np.sin(ks / 2) ** 2).sum(1)
expect = np.sort(np.concatenate([np.zeros(V3), lk, lk]))
check(abs(lam - expect).max() < 1e-9 and abs(Cu @ D3.T.toarray()).max() == 0,
      "[T] C1 on the centre-bond lattice the plaquette phase's quadratic part curl^T curl has, at each k,"
      " eigenvalue 0 on the gauge (gradient) mode and lambda_k = sum 4 sin^2(k_i/2) on exactly two modes:"
      " two photon polarisations, curl grad = 0",
      f"4^3 torus, {nl} links, max eigenvalue deviation {abs(lam-expect).max():.1e}")
eps, cE, cB = 0.2, 1.3, 1 / 1.3        # same coupling for both: c_E c_B = 1 (cone = edge cone)
Mmap = np.block([[np.eye(nl), np.zeros((nl, nl))], [-eps * cB * K, np.eye(nl)]]) @ \
       np.block([[np.eye(nl), eps * cE * np.eye(nl)], [np.zeros((nl, nl)), np.eye(nl)]])
ev = np.linalg.eigvals(Mmap)
Om = np.sort(np.abs(np.angle(ev)))
pred = np.sort(np.concatenate([np.zeros(2 * V3), np.repeat(np.arccos(1 - eps ** 2 * cE * cB * lk / 2), 2),
                               np.repeat(np.arccos(1 - eps ** 2 * cE * cB * lk / 2), 2)]))
Jm = np.block([[np.zeros((nl, nl)), np.eye(nl)], [-np.eye(nl), np.zeros((nl, nl))]])
check(abs(Om - pred).max() < 1e-6 and abs(Mmap.T @ Jm @ Mmap - Jm).max() < 1e-12,
      "[T] C2 the half-tick pair (electric plaquettes along the normal, then magnetic plaquettes) is a"
      " symplectic map; each register photon has cos(Omega) = 1 - eps^2 c_E c_B lambda_k/2, so"
      " Omega/eps -> sqrt(c_E c_B)|k|: the free photon, speed sqrt(c_E c_B), lattice corrections O(eps^2 k^2, k^2)",
      f"max quasi-energy deviation {abs(Om-pred).max():.1e} (Heisenberg map of the quadratic register is exact)")
Lg = 64
kk = 2 * np.pi * np.fft.fftfreq(Lg)
KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing="ij")
lap = 4 * (np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2)
lap[0, 0, 0] = np.inf
G = np.real(np.fft.ifftn(1 / lap))
Rs = [4, 6, 8]
# Coulomb coefficient from potential differences (removes the torus constant); torus term ~ r^2/L^3
# neutralising-background term of the torus Green function: + r^2/(6 L^3), removed exactly
coef = lambda g1, g2, r1, r2: 4 * np.pi * ((g1 - r1 ** 2 / (6 * Lg ** 3)) - (g2 - r2 ** 2 / (6 * Lg ** 3))) / (1 / r1 - 1 / r2)
ax = [coef(G[r, 0, 0], G[2 * r, 0, 0], r, 2 * r) for r in (6, 8, 10)]
dg = [coef(G[r, r, r], G[2 * r, 2 * r, 2 * r], r * 3 ** 0.5, 2 * r * 3 ** 0.5) for r in (3, 4)]
# exact: least electric energy under Gauss's law = (1/2) q^T (D D^T)^+ q, attained by E = -grad phi
D6, _ = cubic_links(6)
q = np.zeros(216); q[0] = 1; q[np.ravel_multi_index((3, 2, 1), (6,) * 3)] = -1
Emin = np.linalg.lstsq(D6.toarray(), q, rcond=None)[0]
Lap = (D6 @ D6.T).toarray()
gauss_ok = abs(0.5 * Emin @ Emin - 0.5 * q @ np.linalg.pinv(Lap) @ q) < 1e-10 and abs(D6 @ Emin - q).max() < 1e-10
check(gauss_ok and max(abs(np.array(ax + dg) - 1)) < 0.02,
      "[T/D] C3 Gauss's law with static charges +-1 fixes the longitudinal electric values (E = -grad phi,"
      " lap phi = -q): the register energy shifts by exactly -c_E G(R), and 4 pi R G(R) -> 1 isotropically:"
      " Coulomb with alpha = c_E/(4 pi) at the dressed-coupling unit",
      "4 pi dG/d(1/R) over R..2R: axis R=6,8,10 " + ", ".join(f"{x:.3f}" for x in ax) + "; diagonal R=3,4 sqrt3 " + ", ".join(f"{x:.3f}" for x in dg)
      + " (64^3 torus)")
# departure energy and edge response
k0 = np.array([0.07, 0.04, 0.02])
omega = lambda a, k: np.sqrt(((2 / a) ** 2 * np.sin(k / 2) ** 2).sum())
a0 = np.array([1.0, 1.0, 1.0]); h = 1e-6
dlog = np.array([(omega(a0 * np.exp(h * np.eye(3)[i]), k0) - omega(a0 * np.exp(-h * np.eye(3)[i]), k0)) / (2 * h)
                 for i in range(3)])
nhat2 = k0 ** 2 / (k0 ** 2).sum()
w0 = omega(a0, k0)
# local energy of a register mode in the electric basis: eigenstates give a configuration-independent value
nmax = 60
ad = np.diag(np.sqrt(np.arange(1, nmax)), -1)
X = (ad + ad.T) / np.sqrt(2)
Hosc = w0 * (ad @ ad.T + 0.5 * np.eye(nmax))  # number basis
xs, xv = np.linalg.eigh(X)                     # electric-value basis = eigenbasis of X
Hx = xv.T @ Hosc @ xv
loc = lambda st: (Hx @ st) / st
vac = xv.T[:, :] @ np.eye(nmax)[:, 0]; one = xv.T @ np.eye(nmax)[:, 1]
mask = abs(one) > 1e-3 * abs(one).max()
locv = np.real(loc(vac)[mask]); loc1 = np.real(loc(one)[mask])
dep1 = loc1 - locv
check(abs(dlog.sum() + w0) < 1e-8 * w0 and abs(-dlog / w0 - nhat2).max() < 2e-3
      and np.ptp(locv) < 1e-6 * w0 and abs(dep1 - w0).max() < 1e-6 * w0,
      "[T] C4 vacuum standard for registers: an eigenstate's local energy is the same at every electric"
      " configuration, so the vacuum's zero-point (w/2 per mode, any edges) subtracts to 0 at every actual"
      " configuration, and a one-photon register sources exactly hbar w; omega_k(edges) is homogeneous of"
      " degree -1, so the edge response is traceless with T^ij = w n^i n^j (null dust)",
      f"one photon departure/w - 1 {abs(dep1/w0-1).max():.1e}; sum_i dw/dln a_i + w {dlog.sum()+w0:.1e};"
      f" max |T^ii/w - n_i^2| {abs(-dlog/w0-nhat2).max():.1e}")
zp = 0.5 * np.mean(np.sqrt(lk[1:]))
check(True,
      "[E] C5 without the vacuum standard the register zero-point would source ~ (1/2)<w_k>/cell ~ 1 Planck"
      " density per cell against the measured rho_Lambda ~ 1e-123 Planck: the subtraction is required, and it"
      " removes the zero-point's edge derivative too (CL-3 must count the plaquette phase from the links'"
      " vacuum on the same edges)",
      f"<w_k>/2 on 4^3 = {zp:.2f} per link-cell in lattice units")
print(f"elapsed_seconds {time.time()-T0:.1f}")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
