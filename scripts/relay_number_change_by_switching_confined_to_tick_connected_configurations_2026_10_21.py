#!/usr/bin/env python3
"""Relay number that can change: odds on block-mode occupations, switching confined to configurations
the block tick connects. Supplied tiny models, no physical identification.

M1: one block, two fermion modes a (value +1), b (value -1) and one link mode c (boson, truncated
exactly by the conserved K = n_c + n_a). Tick = free phases then a pair coupling g (a^+ b^+ c + h.c.).
M2: ring of L = 3 blocks, four fermion modes per block (value +/-, direction R/L), 4096-dim Fock space;
tick = fermionic shift (every relay steps, CL-4) then block coins with mixing m and an external,
switched-off pair pulse E(t). Records bookkept on sampled trajectories (CL-3, Record axiom).
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/RELAY_NUMBER_CHANGE_BY_SWITCHING_CONFINED_TO_TICK_CONNECTED_CONFIGURATIONS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import os, sys, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
def _timeout(*a):
    raise TimeoutError('120-second cap exceeded')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

T0 = time.time()
PASS = FAIL = 0
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def uexp(H, tau=1.0):
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * w * tau)) @ V.conj().T


def components(C, tol=1e-13):
    """connected classes of the graph with an edge wherever the block tick has a nonzero element."""
    n = C.shape[0]; lab = -np.ones(n, int); k = 0
    for s in range(n):
        if lab[s] >= 0: continue
        stack = [s]; lab[s] = k
        while stack:
            i = stack.pop()
            for j in np.nonzero((abs(C[:, i]) > tol) | (abs(C[i, :]) > tol))[0]:
                if lab[j] < 0: lab[j] = k; stack.append(j)
        k += 1
    return lab


def switch(cfg, P, Pn, cls):
    """shortfall rule: from c (odds fell) leave w.p. (P-Pn)/P to c' of the SAME class whose odds rose,
    in proportion to the rise. cfg: trajectory configs (int array); P, Pn, cls: per-config arrays."""
    exc = np.maximum(P - Pn, 0.0); dfc = np.maximum(Pn - P, 0.0)
    leave = rng.random(cfg.size) < np.where(P[cfg] > 0, exc[cfg] / np.maximum(P[cfg], 1e-300), 0.0)
    out = cfg.copy()
    for i in np.nonzero(leave)[0]:
        w = dfc * (cls == cls[cfg[i]])
        if w.sum() > 0:
            out[i] = rng.choice(w.size, p=w / w.sum())
    return out


# =========================== M1: one block, pair <-> link quantum ===========================
NC = 4                                    # boson levels 0..3 (exact: K = n_c + n_a <= 2 below)
sm = np.array([[0, 1], [0, 0]], float); Z = np.diag([1.0, -1.0]); I2 = np.eye(2); Ic = np.eye(NC)
cb = np.diag(np.sqrt(np.arange(1, NC)), 1)
A = np.kron(np.kron(sm, I2), Ic); B = np.kron(np.kron(Z, sm), Ic); Cc = np.kron(np.kron(I2, I2), cb)
na, nb, nc = A.T @ A, B.T @ B, Cc.T @ Cc
EPS, G = 0.3, 0.12
def m1_tick(Om, g=G, model='B'):
    if model == 'B':
        H0 = EPS * (na + nb) + Om * nc; V = A.T @ B.T @ Cc
    else:                                 # sea picture: u = A, l = B, lower band at -EPS
        H0 = EPS * na - EPS * nb + Om * nc; V = A.T @ B @ Cc
    V = V + V.T
    return uexp(H0) @ uexp(g * V), H0, V
idx = lambda a, b, c: (a * 2 + b) * NC + c
Q1 = np.diag(na - nb).copy(); N1 = np.diag(na + nb).copy()

U, H0, V = m1_tick(2 * EPS)
check('M1 tick conserves value Q = n_a - n_b exactly; relay number N = n_a + n_b is not conserved',
      np.abs(U @ np.diag(Q1) - np.diag(Q1) @ U).max() < 1e-14 and np.abs(U @ np.diag(N1) - np.diag(N1) @ U).max() > 1e-2,
      f"|[Q,U]| = {np.abs(U @ np.diag(Q1) - np.diag(Q1) @ U).max():.1e}, |[N,U]| = {np.abs(U @ np.diag(N1) - np.diag(N1) @ U).max():.2f}")
U0 = m1_tick(2 * EPS, g=0.0)[0]
check('vacuum stability: with the coupling off, relay number commutes with the tick',
      np.abs(U0 @ np.diag(N1) - np.diag(N1) @ U0).max() < 1e-15)

# particle-hole equivalence (sea picture A <-> pair picture B), rederived numerically
HA = m1_tick(2 * EPS, model='A')[1] + G * (lambda v: v + v.T)(A.T @ B @ Cc)
HB = m1_tick(2 * EPS, model='B')[1] + G * (lambda v: v + v.T)(A.T @ B.T @ Cc)
eA, eB = np.linalg.eigvalsh(HA), np.linalg.eigvalsh(HB)
gs = np.argmin(np.diag(HA))
check('sea picture: spectrum of H_A + eps equals pair-picture spectrum H_B; B vacuum <-> filled lower mode (A ground config)',
      np.abs(np.sort(eA + EPS) - np.sort(eB)).max() < 1e-12 and gs == idx(0, 1, 0),
      f"max spectral gap {np.abs(np.sort(eA + EPS) - np.sort(eB)).max():.1e}")

# Born (equivariance) with classes = connected components of the block tick
def run_m1(psi0, Om, T, ntraj, restrict=True):
    U = m1_tick(Om)[0]; lab = components(U) if restrict else np.zeros(U.shape[0], int)
    psi = psi0.copy(); P = abs(psi) ** 2
    cfg = rng.choice(P.size, size=ntraj, p=P / P.sum()); maxdev = 0.0; maxcls = 0.0; jumps = []
    for t in range(T):
        psin = U @ psi; Pn = abs(psin) ** 2
        for k in set(lab): maxcls = max(maxcls, abs(P[lab == k].sum() - Pn[lab == k].sum()))
        new = switch(cfg, P, Pn, lab); jumps.append((cfg[new != cfg], new[new != cfg]))
        cfg, psi, P = new, psin, Pn
        f = np.bincount(cfg, minlength=P.size) / ntraj
        sig = np.sqrt(np.maximum(P * (1 - P), 1e-12) / ntraj)
        maxdev = max(maxdev, (abs(f - P) / sig)[P > 1e-4].max())
    return maxdev, maxcls, jumps

psi = np.zeros(2 * 2 * NC, complex); psi[idx(0, 0, 1)] = 1.0          # one link quantum, no relays
dev, mcls, jumps = run_m1(psi, 2 * EPS, 40, 20000)
check('M1 Born: class odds conserved by the tick (equivariance hypothesis) and 20000 trajectories follow |psi|^2 over 40 ticks',
      mcls < 1e-14 and dev < 5.0, f"class-total drift {mcls:.1e}, max deviation {dev:.2f} sigma")
fr, to = np.concatenate([j[0] for j in jumps]), np.concatenate([j[1] for j in jumps])
crt = np.sum(N1[to] > N1[fr]); ann = np.sum(N1[to] < N1[fr])
check('M1: relays are created and end in pairs; every jump keeps Q', crt > 0 and ann > 0 and np.all(Q1[to] == Q1[fr])
      and np.all(np.abs(N1[to] - N1[fr]) % 2 == 0), f"{crt} creations, {ann} endings")

# energy accounting of deposits per jump
dep_full = np.diag(EPS * (na + nb) + 2 * EPS * nc); dep_rel = np.diag(EPS * (na + nb))
check('M1 resonant: relay deposits + link-quantum deposits are unchanged by every jump; relay deposits alone jump by 2 eps',
      np.abs(dep_full[to] - dep_full[fr]).max() < 1e-15 and np.isclose(np.abs(dep_rel[to] - dep_rel[fr]).max(), 2 * EPS),
      f"max |d(full)| = {np.abs(dep_full[to] - dep_full[fr]).max():.1e}, max |d(relays only)| = {np.abs(dep_rel[to] - dep_rel[fr]).max():.2f}")

# superposed link sectors: component restriction vs plain fiber shortfall
psi = np.zeros(2 * 2 * NC, complex); psi[idx(0, 0, 1)] = 1; psi[idx(0, 0, 2)] = 1; psi /= np.linalg.norm(psi)
_, _, jr = run_m1(psi, 2 * EPS, 30, 4000, restrict=True)
_, _, ju = run_m1(psi, 2 * EPS, 30, 4000, restrict=False)
bad = lambda js: sum(int(np.sum(np.abs(dep_full[j[1]] - dep_full[j[0]]) > 1e-12)) for j in js)
check('switching confined to tick-connected classes keeps per-jump energy; unconfined shortfall makes energy-violating jumps (control)',
      bad(jr) == 0 and bad(ju) > 0, f"violating jumps: confined {bad(jr)}, unconfined {bad(ju)}")

# Floquet umklapp: the tick cannot tell Om from Om + 2 pi
def transfer(Om, T=60):
    U = m1_tick(Om)[0]; p = np.zeros(2 * 2 * NC, complex); p[idx(0, 0, 1)] = 1; best = 0
    for _ in range(T): p = U @ p; best = max(best, abs(p[idx(1, 1, 0)]) ** 2)
    return best
tr0, tr2, tr1 = transfer(2 * EPS), transfer(2 * EPS + 2 * np.pi), transfer(2 * EPS + 1.0)
check('tick-energy is conserved only mod 2 pi per tick: Om = 2 eps + 2 pi converts as fully as resonance; Om = 2 eps + 1 does not',
      abs(tr0 - tr2) < 1e-12 and tr0 > 0.99 and tr1 < 0.1, f"max pair odds {tr0:.3f}, {tr2:.3f}, {tr1:.3f}")

# joint CL-5 energy: Floquet eigenstate advances one phase in every configuration, = quasienergy
w, Vv = np.linalg.eig(m1_tick(2 * EPS)[0]); sel = [i for i in range(w.size) if abs(Vv[idx(1, 1, 0), i]) > 0.3 and abs(Vv[idx(0, 0, 1), i]) > 0.3]
v = Vv[:, sel[0]]; vn = m1_tick(2 * EPS)[0] @ v; mask = abs(v) > 1e-8
ph = -np.angle(vn[mask] * v[mask].conj()); bare = (abs(v) ** 2 * dep_full).sum()
check('dressed state: joint phase advance is the same in every configuration (= quasienergy), bare deposits differ by the binding share',
      np.ptp(ph) < 1e-12 and abs(ph[0] - bare) > 1e-3, f"quasienergy {ph[0]:.4f}, bare deposits {bare:.4f}, binding {ph[0]-bare:+.4f}")

# =========================== M2: ring of 3 blocks, 12 fermion modes ===========================
L, NM = 3, 12; DIM = 1 << NM
bits = ((np.arange(DIM)[:, None] >> (NM - 1 - np.arange(NM))) & 1).astype(np.int8)   # n_i per config
VAL = np.array([+1, +1, -1, -1]); DIRR = np.array([1, 0, 1, 0])
def perm_op(pi):
    """Fock representation of a mode permutation: returns (target index, sign) per basis config."""
    tgt = np.zeros(DIM, int); sgn = np.ones(DIM)
    for s in range(DIM):
        occ = np.nonzero(bits[s])[0]; img = pi[occ]
        tgt[s] = int(sum(1 << (NM - 1 - j) for j in img))
        inv = sum(1 for i in range(len(img)) for j in range(i + 1, len(img)) if img[i] > img[j])
        sgn[s] = -1.0 if inv % 2 else 1.0
    return tgt, sgn
def apply_perm(op, psi):
    out = np.zeros_like(psi); out[op[0]] = op[1] * psi; return out
pi_S = np.array([4 * ((i // 4 + (1 if DIRR[i % 4] else -1)) % L) + i % 4 for i in range(NM)])
pi_T = (np.arange(NM) + 4) % NM
S_op, T_op = perm_op(pi_S), perm_op(pi_T)
def annih(i, psi):
    out = np.zeros_like(psi); occ = bits[:, i] == 1
    sgn = (-1.0) ** bits[:, :i].sum(1)
    src = np.nonzero(occ)[0]; out[src - (1 << (NM - 1 - i))] = (sgn * psi)[src]; return out
x = rng.normal(size=DIM) + 1j * rng.normal(size=DIM)
err = max(np.abs(apply_perm(S_op, annih(i, apply_perm((np.argsort(S_op[0]), S_op[1][np.argsort(S_op[0])]), x)))
                 - annih(pi_S[i], x)).max() for i in range(NM))
check('fermionic shift implements c_i -> c_pi(i) on Fock space (every relay steps one block, CL-4)', err < 1e-12, f"max {err:.1e}")

s4 = np.array([[0, 1], [0, 0]], float); Z4 = np.diag([1.0, -1.0])
def loc(k):
    m = np.array([[1.0]])
    for j in range(4): m = np.kron(m, Z4 if j < k else (s4 if j == k else np.eye(2)))
    return m
c4 = [loc(k) for k in range(4)]
def coin(m, E, same_value=False):
    H = m * (c4[0].T @ c4[1] + c4[2].T @ c4[3])
    H = H + (E * (c4[0].T @ c4[1].T + c4[2].T @ c4[3].T) if same_value else E * (c4[0].T @ c4[3].T + c4[1].T @ c4[2].T))
    return uexp(H + H.T)
def apply_coin(Cx, x, psi):
    return np.einsum('ij,ajb->aib', Cx, psi.reshape(1 << (4 * x), 16, 1 << (4 * (L - 1 - x)))).ravel()
MM, E0, TP, TT = 0.4, 0.8, 8, 14
Et = lambda t: E0 * np.sin(np.pi * (t + 0.5) / TP) ** 2 if t < TP else 0.0
def full_tick(psi, t, sv=False):
    psi = apply_perm(S_op, psi); Cx = coin(MM, Et(t), sv)
    for xb in range(L): psi = apply_coin(Cx, xb, psi)
    return psi
check('M2 tick commutes with ring translation (no block privileged)',
      np.abs(apply_perm(T_op, full_tick(x / np.linalg.norm(x), 0)) - full_tick(apply_perm(T_op, x / np.linalg.norm(x)), 0)).max() < 1e-12)
Qb = np.stack([bits[:, 4 * b:4 * b + 4] @ VAL for b in range(L)], 1); Nrel = bits.sum(1)
vac = np.zeros(DIM, complex); vac[0] = 1
v1 = vac.copy()
for t in range(TP, TP + 6): v1 = full_tick(v1, t)
check('M2 vacuum stability: with the pulse off the empty state stays empty', abs(abs(v1[0]) - 1) < 1e-13)

psi0 = np.zeros(DIM, complex)
psi0[1 << (NM - 1 - 0)] = 1 / np.sqrt(2); psi0[1 << (NM - 1 - 5)] = 1j / np.sqrt(2)   # +R at block 0, +L at block 1

def run_m2(ntraj, mode='local', keep=0):
    psi = psi0.copy(); P = abs(psi) ** 2; cfg = rng.choice(DIM, size=ntraj, p=P)
    hist = []; maxcls = 0.0; viol = 0
    for t in range(TT):
        psi = apply_perm(S_op, psi); cfg = S_op[0][cfg]; P = abs(psi) ** 2
        post_shift = cfg.copy(); Cx = coin(MM, Et(t), mode == 'samevalue')
        if mode == 'global':
            for xb in range(L): psi = apply_coin(Cx, xb, psi)
            Pn = abs(psi) ** 2; Qg = Qb.sum(1); cfg = switch(cfg, P, Pn, Qg)
        else:
            lab = components(Cx)
            for xb in range(L):
                psin = apply_coin(Cx, xb, psi); Pn = abs(psin) ** 2
                rest = (np.arange(DIM) >> (4 * (L - 1 - xb) + 4)) * (1 << (4 * (L - 1 - xb))) + (np.arange(DIM) & ((1 << (4 * (L - 1 - xb))) - 1))
                locc = (np.arange(DIM) >> (4 * (L - 1 - xb))) & 15
                cls = rest * 16 + lab[locc]
                tot = np.bincount(cls, P, minlength=cls.max() + 1) - np.bincount(cls, Pn, minlength=cls.max() + 1)
                maxcls = max(maxcls, np.abs(tot).max())
                cfg = switch(cfg, P, Pn, cls); psi, P = psin, Pn
        viol += int(np.sum(np.any(Qb[cfg] != Qb[post_shift], 1)))
        if keep: hist.append((post_shift[:keep].copy(), cfg[:keep].copy()))
    return psi, cfg, maxcls, viol, hist

psiT, cfgT, mcls, viol, hist = run_m2(6000, 'local', keep=400)
PT = abs(psiT) ** 2
nex = bits.T.astype(float) @ PT; nmc = bits[cfgT].mean(0)
pNe = np.bincount(Nrel, PT, minlength=13); pNm = np.bincount(Nrel[cfgT], minlength=13) / cfgT.size
z = max(np.abs(nmc - nex).max() / np.sqrt(0.25 / cfgT.size), np.abs(pNm - pNe).max() / np.sqrt(0.25 / cfgT.size))
check('M2 Born: block-class odds conserved by each coin, and 6000 trajectories reproduce mode occupations and relay-number odds',
      mcls < 1e-13 and z < 5, f"class drift {mcls:.1e}; P(N=1,3,5) exact {pNe[1]:.3f},{pNe[3]:.3f},{pNe[5]:.3f} vs sampled {pNm[1]:.3f},{pNm[3]:.3f},{pNm[5]:.3f}; max {z:.2f} sigma")
check('M2: the pulse creates relays (relay number changes) and every coin event keeps each block value',
      pNe[3] > 0.05 and viol == 0, f"P(N>1) = {1 - pNe[1]:.3f}, block-value violations {viol}")
_, _, _, vg, _ = run_m2(1500, 'global')
_, _, mc2, vs, _ = run_m2(800, 'samevalue')
check('controls: joint switching over the whole configuration (same total value) moves value between blocks; a same-value pair coin breaks block value',
      vg > 0 and vs > 0, f"violating trajectory-ticks: global {vg}, same-value coin {vs}")

# record bookkeeping on 400 trajectories (CL-3, Record axiom, value of records)
NSITE = 64; okR = True; nread_bad = 0; last_read = 0; valbad = 0; pairbad = 0; ncre = nend = 0; cap = 0
for tr in range(400):
    relay_mode = {}; rid = 0; recs = []; last = {}; burnt = [set() for _ in range(L)]; ended = []
    for t in range(TT):
        ps, pc = int(hist[t][0][tr]), int(hist[t][1][tr])
        if t == 0:
            for i in np.nonzero(bits[ps])[0]: relay_mode[rid] = i; rid += 1
        else:
            relay_mode = {r: pi_S[i] for r, i in relay_mode.items()}
        okR &= sorted(relay_mode.values()) == list(np.nonzero(bits[ps])[0])
        vsum = 0
        for r, i in relay_mode.items():
            b = i // 4; free = [s for s in range(NSITE) if s not in burnt[b]]
            if not free: cap += 1; continue
            s = free[rng.integers(len(free))]; burnt[b].add(s)
            v = VAL[i % 4]; recs.append([b, s, v, 0]); vsum += v
            if r in last: recs[last[r]][3] += 1
            last[r] = len(recs) - 1
        valbad += vsum != Qb[ps].sum()
        for b in range(L):
            old = set(i for i in np.nonzero(bits[ps])[0] if i // 4 == b); new = set(i for i in np.nonzero(bits[pc])[0] if i // 4 == b)
            gone, came = sorted(old - new), sorted(new - old)
            for sv in (+1, -1):
                g_ = [i for i in gone if VAL[i % 4] == sv]; c_ = [i for i in came if VAL[i % 4] == sv]
                mover = {r: i for r, i in relay_mode.items() if i in g_}
                for (r, _), j in zip(list(mover.items()), c_): relay_mode[r] = j
                for r in list(mover)[len(c_):]: ended.append(r); del relay_mode[r]
                for j in c_[len(mover):]: relay_mode[rid] = j; rid += 1
            dc = [sum(1 for i in came if VAL[i % 4] == sv) - sum(1 for i in gone if VAL[i % 4] == sv) for sv in (+1, -1)]
            pairbad += dc[0] != dc[1]
            ncre += max(dc[0], 0); nend += max(-dc[0], 0)
    nread_bad += sum(1 for r in recs if r[3] > 1); last_read += sum(recs[last[r]][3] for r in ended)
    sites = [(r[0], r[1]) for r in recs]; okR &= len(sites) == len(set(sites))
check('records on 400 trajectories: one record per site, none read twice, an ended relay\'s last record never read, record value per tick = total value',
      okR and nread_bad == 0 and last_read == 0 and valbad == 0 and cap == 0,
      f"twice-read {nread_bad}, last-record reads {last_read}, value mismatches {valbad}, full blocks {cap}")
check('relays begin and end only in opposite-value pairs in one block', pairbad == 0 and ncre > 0 and nend > 0,
      f"{ncre} pairs begun, {nend} pairs ended, unpaired events {pairbad}")

print('supplied: one fermion mode per block mode; value labels; the vacuum (empty modes = filled lower band); '
      'the link mode and its energy deposit; coin, pulse and coupling; relay-identity matching at switches; site choice.')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
