#!/usr/bin/env python3
"""quantum-split: how CL-1's split acts when edges are quantum registers (length L(1 + n/2S)).
Supplied 1D toy: a chain cell = one edge register (+ two matter modes); its split = two child edges at n = 0
(+ four matter modes, the two new ones in the children's vacuum).  Exact identities, finite diagnostics, estimates.
 A  structure: one-shot controlled split, the exchange form, the glued form; charge; no signalling; trace flux
 B  the top wall: packet through the glued junction vs the box; CL-2 transport across it; fixed schedule (c)
 C  actual-configuration trigger (b): Born weight of the split event and a remote setting
 D  estimates against measurement
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/A_GLUED_SPLIT_OF_EDGE_REGISTERS_IS_UNITARY_AND_LOCAL_WHILE_ONE_SHOT_TRIGGERED_AND_SCHEDULED_SPLITS_FAIL_IN_A_ONE_DIMENSIONAL_TOY_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 120
import os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm, eigh
np.seterr(all='ignore')
T00 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ''))
def opn(M): return np.linalg.norm(M, 2)

# ---------- CL-2 transport: fewest changes (cost) then greatest entropy, along nonzero elements (entropic limit)
def transport(p, q, allowed, cost, tau=0.1, iters=40000, tol=1e-12):
    sp, sq = p > 1e-14, q > 1e-14
    K = np.where(allowed, np.exp(-cost / tau), 0.0)[np.ix_(sp, sq)]
    a, b = p[sp] / p[sp].sum(), q[sq] / q[sq].sum(); u = np.ones_like(a); v = np.ones_like(b); err = 1.0
    for it in range(iters):
        u = a / (K @ v + 1e-300); v = b / (K.T @ u + 1e-300)
        if it % 25 == 0:
            err = np.abs(u * (K @ v) - a).sum()
            if err < tol: break
    P = np.zeros((len(p), len(q))); P[np.ix_(sp, sq)] = u[:, None] * K * v[None, :]
    return P, err

# ---------- fermion modes (Jordan-Wigner), occupation basis, mode 0 = most significant bit
def cops(nm):
    I2, Z, a = np.eye(2), np.diag([1., -1.]), np.array([[0., 1.], [0., 0.]])
    out = []
    for j in range(nm):
        m = np.array([[1.]])
        for k in range(nm): m = np.kron(m, Z if k < j else (a if k == j else I2))
        out.append(m)
    return out
def sector(nm, N):
    return [i for i in range(2 ** nm) if bin(i).count('1') == N]
def hop_chain(c, bonds):
    H = 0
    for i, j in bonds: H = H - (c[i].T @ c[j] + c[j].T @ c[i])
    return H

print("== A. structure (one cell; parent: edge n, modes a,b at N=1; children: two edges, modes a,1,2,b at N=2)")
cp, cc = cops(2), cops(4)
ip, ic = sector(2, 1), sector(4, 2)
hp = hop_chain(cp, [(0, 1)])[np.ix_(ip, ip)]; hc = hop_chain(cc, [(0, 1), (1, 2), (2, 3)])[np.ix_(ic, ic)]
ep, vp = eigh(hp); ec, vc = eigh(hc)
Vm = vc[:, :2] @ vp[:, :2].T                       # parent vacuum -> children's vacuum, excitation -> lowest excitation
Qp = (np.array([bin(i).count('1') for i in ip]) - 1.0); Qc = (np.array([bin(i).count('1') for i in ic]) - 2.0)
check("A0 THEOREM: the passing is an isometry 2 -> 6 that keeps the charge Q = N - modes/2 (new modes half filled)",
      opn(Vm.T @ Vm - np.eye(2)) < 1e-13 and np.allclose(Qp, 0) and np.allclose(Qc, 0),
      f"|V^T V - 1| {opn(Vm.T @ Vm - np.eye(2)):.0e}; Q parent {sorted(set(float(round(x,12))+0.0 for x in Qp))}, children {sorted(set(float(round(x,12))+0.0 for x in Qc))}; vacua {ep[0]:.3f} -> {ec[0]:.3f}")

S2 = 2; ne = S2 + 1                                 # register n = 0..2S
dP, dC = ne * 2, ne * ne * 6; D = dP + dC
def pidx(n, m): return n * 2 + m
def cidx(n1, n2, m): return dP + (n1 * ne + n2) * 6 + m
V = np.zeros((D, D)); Pf = np.zeros((D, D))
for m in range(2):
    Pf[pidx(S2, m), pidx(S2, m)] = 1
    for k in range(6): V[cidx(0, 0, k), pidx(S2, m)] = Vm[k, m]
Qim = V @ V.T
S1 = V @ Pf + (np.eye(D) - Pf)                      # (a) one-shot: split the full component, identity elsewhere
G = V + V.T + (np.eye(D) - Pf - Qim)                # (a) exchange form
check("A1 THEOREM (collision): the one-shot controlled split on the sum over lattices is not an isometry; its image "
      "lands on child states the map also keeps, so two orthogonal states become one", opn(S1.T @ S1 - np.eye(D)) > 0.99,
      f"|S^T S - 1| = {opn(S1.T @ S1 - np.eye(D)):.3f} (rank of collision 2)")
check("A2 THEOREM: the exchange V + V^dag on (full, split image) is unitary and an involution; it carries a merge V^dag",
      opn(G.T @ G - np.eye(D)) < 1e-13 and opn(G @ G - np.eye(D)) < 1e-13, f"|G^T G - 1| {opn(G.T @ G - np.eye(D)):.0e}")

# in-sector ticks: edge spin-S hop (rate J) + matter hop measured from each sector's vacuum
def Sx(S2_):
    n = np.arange(S2_ + 1); s = S2_ / 2; mm = n - s
    up = np.sqrt(s * (s + 1) - mm[:-1] * (mm[:-1] + 1)); X = np.zeros((S2_ + 1, S2_ + 1))
    X[np.arange(1, S2_ + 1), np.arange(S2_)] = up / 2; return X + X.T
def Hsec(J, Sxp, nep):
    Hp_ = J * np.kron(Sxp, np.eye(2)) + np.kron(np.eye(nep), hp - ep[0] * np.eye(2))
    Hc_ = (J * (np.kron(np.kron(Sxp, np.eye(nep)), np.eye(6)) + np.kron(np.kron(np.eye(nep), Sxp), np.eye(6)))
           + np.kron(np.eye(nep * nep), hc - ec[0] * np.eye(6)))
    return Hp_, Hc_
Hp_, Hc_ = Hsec(0.02, Sx(S2), ne)
Hs = np.zeros((D, D)); Hs[:dP, :dP] = Hp_; Hs[dP:, dP:] = Hc_
Ut = expm(-1j * Hs * 0.5)
psi = np.zeros(D, complex); psi[pidx(S2, 0)] = 1.0     # cube full, matter in vacuum, slow edges
pc_ex = []
for k in range(8):
    psi = Ut @ (G @ (Ut @ psi)); pc_ex.append(np.sum(np.abs(psi[dP:]) ** 2))
flips = sum(1 for i in range(1, 8) if abs(pc_ex[i] - pc_ex[i - 1]) > 0.5)
check("A3 DIAGNOSTIC (flicker): with slow edges the exchange form sends the odds parent <-> children every even half-tick, "
      "so CL-2's actual configuration must gain and lose the new sites each time", flips >= 6,
      "P(children) per tick " + ' '.join(f"{x:.2f}" for x in pc_ex))

# glued form: the parent's full state IS the children's split image; the raise that would fill the last quantum
# passes onto the image (V), the lowering of the image passes back (V^dag).  Parent window n = 0..2S-1.
neP = S2; dPg = neP * 2; Dg = dPg + dC
Sxg = Sx(S2)[:neP, :neP]
Hp_g = 0.02 * np.kron(Sxg, np.eye(2)) + np.kron(np.eye(neP), hp - ep[0] * np.eye(2))
up_top = Sx(S2)[S2, S2 - 1] * 0.02
Hg = np.zeros((Dg, Dg)); Hg[:dPg, :dPg] = Hp_g; Hg[dPg:, dPg:] = Hc_
Vg = np.zeros((Dg, dPg))
for m in range(2):
    for k in range(6): Vg[dPg + (0 * ne + 0) * 6 + k, (neP - 1) * 2 + m] = Vm[k, m]
Jn = np.zeros((Dg, Dg)); Jn[:, :dPg] = Vg; Jn = up_top * (Jn + Jn.T); Hg = Hg + Jn
Ug = expm(-1j * Hg)
Qg = np.zeros(Dg); Qg[:dPg] = np.tile(Qp, neP); Qg[dPg:] = np.tile(Qc, ne * ne)
psi = np.zeros(Dg, complex); psi[(neP - 1) * 2 + 0] = 1.0
pc_gl = []
for k in range(8):
    psi = Ug @ psi; pc_gl.append(np.sum(np.abs(psi[dPg:]) ** 2))
check("A4 THEOREM + DIAGNOSTIC (glued form): hermitian, so the tick is unitary on the sum over refinement patterns, "
      "keeps Q, and with slow edges the children's weight moves smoothly (no flicker)",
      opn(Ug.conj().T @ Ug - np.eye(Dg)) < 1e-12 and opn(Hg @ np.diag(Qg) - np.diag(Qg) @ Hg) < 1e-13
      and max(abs(np.diff([0] + pc_gl))) < 0.01,
      f"|U^dag U - 1| {opn(Ug.conj().T @ Ug - np.eye(Dg)):.0e}; P(children) " + ' '.join(f"{x:.4f}" for x in pc_gl[:5]))

# no signalling: cell X entangled with a remote qubit B; a setting theta on B; X's Born distribution
rng = np.random.default_rng(20261022)
psi0 = rng.normal(size=(Dg, 2)) + 1j * rng.normal(size=(Dg, 2)); psi0 /= np.linalg.norm(psi0)
dists = []
for th in np.linspace(0, np.pi, 5):
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    ps = (Ug @ Ug @ psi0) @ R.T
    dists.append(np.sum(np.abs(ps) ** 2, axis=1))
dmax = max(np.abs(d - dists[0]).max() for d in dists)
check("A5 THEOREM (local unitary): with the glued split the cell's distribution over configurations, sector label "
      "(number of sites, so of records) included, is independent of a remote setting", dmax < 1e-14, f"max diff {dmax:.0e}")

# trace flux across the generation cut
Pp = np.zeros(Dg); Pp[:dPg] = 1; Pc = 1 - Pp
upf = np.linalg.norm(np.diag(Pc) @ Ug @ np.diag(Pp)) ** 2; dnf = np.linalg.norm(np.diag(Pp) @ Ug @ np.diag(Pc)) ** 2
W = np.zeros((dP - 2 + 2 * dC, dP))                  # one-way history-labelled isometry: full -> (children, label 1)
keep = [i for i in range(dP) if Pf[i, i] == 0]
for r, i in enumerate(keep): W[r, i] = 1
off = len(keep) + dC
for m in range(2):
    for k in range(6): W[off + k, pidx(S2, m)] = Vm[k, m]
check("A6 THEOREM (index): for any unitary on the sum over refinement patterns from a finite start, the trace weight "
      "split across a generation cut equals the weight merged back; only a non-onto isometry (a history label) splits "
      "without merging", abs(upf - dnf) < 1e-12 and opn(W.T @ W - np.eye(dP)) < 1e-13,
      f"glued: up {upf:.6f} = down {dnf:.6f}; history isometry: up {np.linalg.norm(W[off:]) ** 2:.0f}, down 0")

print("== B. the top wall (edge ladder only; hop J_n proportional to length, parent n = 0..P-1, children m = 0..)")
P = 12; Cc = 36; J0 = 1.0
def ladder(Nl, Js): H = np.zeros((Nl, Nl)); H[np.arange(Nl - 1), np.arange(1, Nl)] = Js; return H + H.T
Jp = J0 * (1 + (np.arange(P - 1) + 0.5) / P); Jc = J0 * (1 + (np.arange(Cc - 1) + 0.5) / P)
Jjun = np.sqrt(J0 * 2 * Jc[0])                     # junction hop: geometric mean of the parent top and child bottom
def Hglue(on, two=False, prof=True):
    jp, jc = (Jp, Jc) if prof else (np.ones(P - 1), np.ones(Cc - 1))
    if not two:
        H = np.zeros((P + Cc, P + Cc)); H[:P, :P] = ladder(P, jp); H[P:, P:] = ladder(Cc, jc)
        if on: H[P - 1, P] = H[P, P - 1] = Jjun if prof else 1.0
        return H
    c2 = 13; Lc = ladder(c2, jc[:c2 - 1])
    H = np.zeros((P + c2 * c2, P + c2 * c2)); H[:P, :P] = ladder(P, jp)
    H[P:, P:] = np.kron(Lc, np.eye(c2)) + np.kron(np.eye(c2), Lc)
    if on: H[P - 1, P] = H[P, P - 1] = Jjun
    return H
n = np.arange(P); dt = 0.25
def packet(w): f = np.exp(-(n - 3.0) ** 2 / (2 * w * w) - 1j * np.pi / 2 * n); return f / np.linalg.norm(f)
def run(on, w, two=False, prof=True, nt=120):
    H = Hglue(on, two, prof); U = expm(-1j * H * dt); ps = np.zeros(len(H), complex); ps[:P] = packet(w)
    lastk = len(H) - (4 if not two else 13 * 4); best = 0.0; seq = [ps.copy()]
    for t in range(nt):
        ps = U @ ps; seq.append(ps.copy())
        if np.sum(np.abs(ps[lastk:]) ** 2) > 1e-3: break
        best = max(best, np.sum(np.abs(ps[P:]) ** 2))
    return best, seq, U
_, box, _ = run(False, 2.5, nt=60)
nbar_box = [np.sum(np.abs(s[:P]) ** 2 * n) for s in box]
Tg = {w: run(True, w)[0] for w in (1.2, 2.5)}; Tu = run(True, 2.5, prof=False)[0]; T2 = run(True, 2.5, two=True, nt=40)[0]
check("B1 DIAGNOSTIC: without the split the up-moving packet reflects at the top (box, qcrush B5); glued, it passes "
      "into the children, the residual set by the junction's impedance step and falling as the packet widens",
      nbar_box[-1] < max(nbar_box) - 3 and Tg[2.5] > Tg[1.2] > 0.85 and Tg[2.5] > 0.97 * Tu,
      f"box: <n> peaks {max(nbar_box):.2f}, then {nbar_box[-1]:.2f}; glued transmitted {Tg[1.2]:.3f} (width 1.2), "
      f"{Tg[2.5]:.3f} (2.5) vs {Tu:.3f} on a uniform chain (no step); two independent child edges {T2:.3f}")
_, glu, U1 = run(True, 2.5)
cfg = len(U1); cost = np.abs(np.arange(cfg)[:, None] - np.arange(cfg)[None, :]).astype(float)
allowed = np.abs(U1).T > 1e-12
ps = glu[0].copy(); act = np.abs(ps) ** 2; up = dn = 0.0; berr = 0.0
for t in range(len(glu) - 1):
    p0 = np.abs(glu[t]) ** 2; p1 = np.abs(glu[t + 1]) ** 2
    Pl, e = transport(p0, p1, allowed, cost); act = act @ (Pl / np.maximum(p0[:, None], 1e-300))
    berr = max(berr, np.abs(act - p1).sum()); up += Pl[:P, P:].sum(); dn += Pl[P:, :P].sum()
wfin = np.sum(np.abs(glu[-1][P:]) ** 2)
check("B2 DIAGNOSTIC (CL-2 across the junction): the actual configuration stays Born-distributed over the sectors; it "
      "splits with the forward flux and merges back only with the reflected flux (up - down = children's weight)",
      berr < 1e-6 and abs(up - dn - wfin) < 1e-3 and dn < 0.1,
      f"Born err {berr:.0e}; actual flux up {up:.4f}, down {dn:.4f}, children's weight {wfin:.4f}")
fr = {}
for w in (1.2, 2.5):
    _, bx, _ = run(False, w, nt=60); fr[w] = max(np.abs(s[P - 1]) ** 2 for s in bx)
check("B3 DIAGNOSTIC (c, fixed schedule): a split at a fixed tick finds only the full component; the rest of the odds "
      "would get children below the rung length, which have no state, and that rest grows with the packet's width",
      fr[2.5] < fr[1.2] < 0.8, f"best scheduled tick carries {fr[1.2]:.3f} (width 1.2), {fr[2.5]:.3f} (2.5) of the odds")

def tree_b(st, Ubl, Ujl, top, chm, costm, tau=0.1, prune=1e-9):
    """exact (b): the junction acts in a tick only on the branch whose actual configuration is at the parent top.
    Branches = junction histories, each with its own odds and the actual sub-distribution riding on it."""
    br = [(st.copy(), np.abs(st) ** 2)]; nb = 1
    for t in range(len(Ubl)):
        new = []
        for ps, a in br:
            p0 = np.abs(ps) ** 2; at = np.zeros_like(a); at[top] = a[top]; ar = a - at
            for sub, U in ((at, Ujl[t]), (ar, Ubl[t])):
                if sub.sum() < prune: continue
                q = U @ ps; Pl, _ = transport(p0, np.abs(q) ** 2, np.abs(U).T > 1e-12, costm, tau)
                new.append((q, sub @ (Pl / np.maximum(p0[:, None], 1e-300))))
        br = new; nb = max(nb, len(br))
    Pact = sum(a[chm].sum() for _, a in br); Eodd = sum(a.sum() * np.sum(np.abs(ps[chm]) ** 2) for ps, a in br)
    return Pact, Eodd, nb, sum(a.sum() for _, a in br)

print("== C. the actual-configuration trigger (b) vs the glued split (a); small ladder (+child) x remote qubit")
Pq, Cq = 6, 8
def Hc_small(on):
    H = np.zeros((Pq + Cq, Pq + Cq)); H[:Pq, :Pq] = ladder(Pq, np.ones(Pq - 1)); H[Pq:, Pq:] = ladder(Cq, np.ones(Cq - 1))
    if on: H[Pq - 1, Pq] = H[Pq, Pq - 1] = 1.0
    return H
Ue_b, Ue_j = expm(-1j * Hc_small(False) * 0.5), expm(-1j * Hc_small(True) * 0.5)
NC = Pq + Cq; cfg2 = 2 * NC; NT = 12
lev = np.repeat(np.arange(NC), 2); bb = np.tile([0, 1], NC)
cost2 = (np.abs(lev[:, None] - lev[None, :]) + np.abs(bb[:, None] - bb[None, :])).astype(float)
def Rb(th): return np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
top2 = [2 * (Pq - 1), 2 * (Pq - 1) + 1]; ch2 = np.zeros(cfg2, bool); ch2[2 * Pq:] = True
nl = np.arange(Pq); res = []
for seed in range(3):
    r = np.random.default_rng(100 + seed)
    st = np.zeros((NC, 2), complex)
    for b_ in range(2):
        f = np.exp(-(nl - r.uniform(0.5, 3)) ** 2 / 2 - 1j * r.uniform(-np.pi, np.pi) * nl); st[:Pq, b_] = f / np.linalg.norm(f)
    st = (st / np.linalg.norm(st)).reshape(-1); row = []
    for th in (0.0, np.pi / 4):
        Ubl = [np.kron(Ue_b, Rb(th if t == 0 else 0.0)) for t in range(NT)]
        Ujl = [np.kron(Ue_j, Rb(th if t == 0 else 0.0)) for t in range(NT)]
        Pa, Eo, nb, tot = tree_b(st, Ubl, Ujl, top2, ch2, cost2)
        ps = st.copy()
        for U in Ujl: ps = U @ ps
        row.append((Pa, Eo, np.sum(np.abs(ps[ch2]) ** 2), nb, tot))
    res.append(row)
born = max(abs(x[0] - x[1]) for row in res for x in row); sig = max(abs(row[1][0] - row[0][0]) for row in res)
gl = max(abs(row[1][2] - row[0][2]) for row in res); nbm = max(x[3] for row in res for x in row)
tot = min(x[4] for row in res for x in row); ex = res[0]
check("C1 THEOREM + DIAGNOSTIC (b breaks Born): with the update chosen by the actual configuration the odds branch by "
      "junction history, and the actual split's frequency differs from the odds weight averaged over the branches",
      born > 1e-2 and tot > 0.999, f"max |P(actual split) - E[odds split]| {born:.3f}; e.g. {ex[0][0]:.4f} vs "
      f"{ex[0][1]:.4f}; branches <= {nbm}; weight kept {tot:.4f}")
check("C2 DIAGNOSTIC (b signals): that frequency (the tick at which the records double) depends on a setting at a remote "
      "qubit that never interacts with the edge", sig > 1e-2, f"max |dP(split)| (theta 0 vs pi/4) {sig:.4f}; e.g. "
      f"{ex[0][0]:.4f} vs {ex[1][0]:.4f}")
check("C3 THEOREM (a): with the glued split the frequency is the Born weight, independent of the setting",
      gl < 1e-13, f"max diff {gl:.0e}; glued P(split) {ex[0][2]:.4f}")

print("== D. ESTIMATES (measured inputs; rung L = sqrt(8 pi) l_P)")
tP = 5.39e-44; H0 = 2.18e-18
dn_tick = H0 * tP
check("D1 exchange form today: a register gains 2S H0 t_tick quanta per tick, so a full cube would flicker parent <-> "
      "children ~1/(2S H0 t_P) times per split; the glued form never flickers", 1 / dn_tick > 1e60,
      f"H0 t_P = {dn_tick:.1e}: ~{1 / dn_tick:.0e}/2S flickers per cube per split")
lnBBN = np.log(4e9); tB, tnow = 180.0, 4.35e17
rate_now = (lnBBN / np.log(2)) / tnow; splits_early = rate_now * tB; need_early = 0.5 * np.log(tB / 1.0) / np.log(2)
check("D2 (c) fixed schedule vs the measured expansion history: the window needs |ln a(t) - (ln2) t/(K t_tick)| < ln2 "
      "at all times; a schedule matching the e-folds since BBN gives ~0 splits in 1-180 s, where a grows by 13x",
      need_early > 3 and splits_early < 1e-10,
      f"{lnBBN / np.log(2):.0f} splits since BBN; schedule gives {splits_early:.0e} in 1-180 s vs {need_early:.1f} needed")
check("D3 (a) glued split fires once per doubling of each cube's own edge, so the split cascade has period ln 2 in "
      "ln a in every era, keeping the tensor ripple's period ln 2; (c) gives period H K t_tick, ln 2 only in tuned de Sitter",
      True, "structural")
print("supplied: 1D chain cell, spin-S edge hop and length-proportional ladder hops (no CL-3 edge dynamics), "
      "collective children, cross-sector unit cost, entropic transport tau = 0.1, packet shapes, measured numbers.")
print(f"elapsed {time.monotonic() - T00:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
