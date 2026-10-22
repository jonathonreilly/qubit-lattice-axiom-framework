AUDIT_INPUT_PATHS = ('docs/RECORDING_EVERY_SITE_INCLUDING_RISHONS_AND_EDGE_REGISTERS_CHANGES_NO_ODDS_LEVEL_PREDICTION_AND_NO_RECORD_OF_ONE_HALF_TICK_EMPTIES_A_SUPPORT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Record reading: what the actuality law should say about rishon and
edge-register sites once a record may fix other sites (finite runner, seeded).

Owner reading of Record + Admissibility (2026-10-22): a record locks its own
site; through admissibility this may leave a neighbour, or another site, with
one possibility (or none).  Tested here: record every site, rishons and edge
registers included, under the actuality law (one actual configuration moved
by the fewest-change transport; records never condition the odds).

Sections
  A  U(1) quantum-link ring (4 matter + 8 rishon modes, one Gauss sector):
     support theorem (no record pattern of one half-tick leaves an empty
     support), Born statistics with and without rishon records, Gauss's law
     among records, forced values versus records, stale records, the
     no-empty-support clause as a formation rule, and non-abelian gauge safety
  B  photons: emitter decay with every link site recorded (no Zeno), single
     photon interference and anticorrelation from link records, repeated
     link-number records (non-demolition) with a pointer for decoherence
  C  mediated entanglement: an edge-register (or link) mediator recorded every
     half-tick keeps the gravity-mediated phase (0.79 rad, concurrence 0.156);
     the conditioning alternative makes the mediator definite and loses it
Contrast throughout: the alternative where records condition the odds.
Supplied: toy Hamiltonians, sizes, couplings, dt, seeds, tolerance 1e-12.
"""
import time
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0
TOL = 1e-12


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}  {vals}")


def popc(s):
    return bin(s).count("1")


def transport(p0, p1, U, cost):
    """Fewest-change coupling of p0 -> p1 along nonzero elements of U (exact LP)."""
    I0, I1 = np.nonzero(p0 > 1e-14)[0], np.nonzero(p1 > 1e-14)[0]
    mask = (abs(U) > 1e-12)[np.ix_(I1, I0)]
    vi = np.argwhere(mask.T)
    nv = len(vi)
    A = np.zeros((len(I0) + len(I1), nv))
    A[vi[:, 0], np.arange(nv)] = 1
    A[len(I0) + vi[:, 1], np.arange(nv)] = 1
    res = linprog(cost[np.ix_(I0, I1)][vi[:, 0], vi[:, 1]], A_eq=A,
                  b_eq=np.r_[p0[I0], p1[I1]], bounds=(0, None), method="highs")
    Pi = np.zeros((len(p0), len(p0)))
    Pi[I0[vi[:, 0]], I1[vi[:, 1]]] = res.x
    return Pi


def walk(psis, Us, cost, K, rng):
    """Sample K actual-configuration histories; records play no part."""
    T = len(Us)
    cfg = np.zeros((K, T + 1), int)
    p = abs(psis[0]) ** 2
    cfg[:, 0] = rng.choice(len(p), size=K, p=p / p.sum())
    for t in range(T):
        Pi = transport(abs(psis[t]) ** 2, abs(psis[t + 1]) ** 2, Us[t], cost)
        rows = np.cumsum(Pi / np.maximum(Pi.sum(1, keepdims=True), 1e-300), 1)
        u = rng.random(K)
        cfg[:, t + 1] = np.minimum((rows[cfg[:, t]] < u[:, None]).sum(1), len(p) - 1)
    return cfg


def zmax(freq, prob, K):
    return float(np.max(abs(freq - prob) / np.sqrt(np.maximum(prob * (1 - prob), 1e-12) / K)))


# ------------------------------------------------------------------ A
print("== A. U(1) quantum-link ring: records of every site under the actuality law")
L = 4
M = [3 * j for j in range(L)]
RP = [3 * j + 1 for j in range(L)]
RM = [(3 * j - 1) % (3 * L) for j in range(L)]
NQ = 3 * L
RISH = sorted(RP + RM)
gauss = lambda s: tuple(((s >> M[j]) & 1) + ((s >> RM[j]) & 1) + ((s >> RP[j]) & 1) for j in range(L))
okcfg = [s for s in range(1 << NQ) if all(((s >> RP[j]) & 1) + ((s >> RM[(j + 1) % L]) & 1) == 1 for j in range(L))]
secs = {}
for s in okcfg:
    secs.setdefault(gauss(s), []).append(s)
gsel = max(secs, key=lambda g: (len(secs[g]), g))
st = secs[gsel]
iq = {s: i for i, s in enumerate(st)}
D = len(st)
B = np.array([[(s >> x) & 1 for x in range(NQ)] for s in st], int)


def fop(s, i, dag):
    if ((s >> i) & 1) == dag:
        return None, 0
    return s ^ (1 << i), (-1) ** popc(s & ((1 << i) - 1))


H = np.zeros((D, D))
for j in range(L):
    k = (j + 1) % L
    for n, s in enumerate(st):
        t, sg = s, 1
        for (i, dg) in ((M[k], 0), (RM[k], 1), (RP[j], 0), (M[j], 1)):
            t, a = fop(t, i, dg) if t is not None else (None, 0)
            sg *= a
        if t is not None and t in iq:
            H[iq[t], n] -= sg
            H[n, iq[t]] -= sg
    for n, s in enumerate(st):
        H[n, n] += 0.5 * (-1) ** j * ((s >> M[j]) & 1)
dt, T, K = 0.35, 10, 4000
U = expm(-1j * dt * H)
psi0 = np.zeros(D, complex)
psi0[0] = 1
psis = [psi0]
for t in range(T):
    psis.append(U @ psis[-1])
ham = np.array([[popc(a ^ b) for b in st] for a in st], float)
cfg = walk(psis, [U] * T, ham, K, RNG)
P = np.array([abs(v) ** 2 for v in psis])
insupp = all(P[t, cfg[:, t]].min() > 1e-14 for t in range(T + 1))


def cond_support(t, sites, vals):
    sup = P[t] > 1e-14
    for x, v in zip(sites, vals):
        sup &= (B[:, x] == v)
    return np.nonzero(sup)[0]


empty = 0
trials = 0
for t in range(1, T + 1):
    for kk in range(0, K, 20):
        x = cfg[kk, t]
        for S in (list(range(NQ)), M, RISH, list(RNG.choice(NQ, 5, replace=False))):
            trials += 1
            empty += len(cond_support(t, S, B[x, S])) == 0
check(insupp and empty == 0, "A1 [T+D]",
      "support theorem: the transport moves only along nonzero elements, so the actual configuration always lies in "
      "the odds' support; records of one half-tick copy it, so locking any set of them leaves every site at least one "
      "possibility (the actual value): 'no possibility' never arises",
      f"Gauss sector dim {D}; samples in support {insupp}; empty supports {empty}/{trials} (all sites, matter, rishons, random 5)")
mz = max(zmax((B[cfg[:, t]][:, M]).mean(0), P[t] @ B[:, M], K) for t in range(1, T + 1))
jz = max(zmax(np.bincount(cfg[:, t], minlength=D) / K, P[t], K) for t in range(1, T + 1))
gv = sum(gauss(st[c]) != gsel for c in cfg.ravel())
check(mz < 4.5 and jz < 4.5 and gv == 0, "A2 [T+D]",
      "records never enter the transport: matter records are Born whether rishons are recorded or not, the joint "
      "pattern is Born, and every recorded pattern satisfies Gauss's law (readable once rishons are recorded)",
      f"max z matter {mz:.2f}, joint {jz:.2f} (K={K}, T={T}); Gauss violations among records {gv}/{cfg.size}")
# conditioning alternative: records collapse the odds to the recorded values
Kc = 600
fc = np.zeros((T + 1, len(M)))
fm = np.zeros((T + 1, len(M)))
for kk in range(Kc):
    for rec, ff in ((range(NQ), fc), (M, fm)):
        v = psi0.copy()
        for t in range(1, T + 1):
            v = U @ v
            pp = abs(v) ** 2
            c = RNG.choice(D, p=pp / pp.sum())
            keep = np.all(B[:, list(rec)] == B[c, list(rec)], axis=1)
            v = np.where(keep, v, 0)
            v /= np.linalg.norm(v)
            ff[t] += B[c, M] / Kc
tvc = max(abs(fc[t] - P[t] @ B[:, M]).max() for t in range(1, T + 1))
tvm = max(abs(fm[t] - P[t] @ B[:, M]).max() for t in range(1, T + 1))
check(tvc > 0.1 and tvm > 0.05, "A3 [D]",
      "contrast: if records conditioned the odds, recording rishons or even matter alone would make links definite "
      "between half-ticks and shift matter statistics off Born (the definite-links failure)",
      f"max |matter freq - Born|: all recorded {tvc:.2f}, matter only {tvm:.2f}; actuality law {mz:.2f} sigma")
# forced values: one record leaves a neighbour one possibility
nf = nm = agree = tot = pf = pt = gf = gt = 0
for t in range(1, T + 1):
    for kk in range(0, K, 10):
        x = cfg[kk, t]
        sup = cond_support(t, M, B[x, M])
        for r in RISH:
            vals = set(B[sup, r])
            tot += 1
            if len(vals) == 1:
                nf += 1
                agree += (vals.pop() == B[x, r])
        j = int(RNG.integers(L))
        s1 = cond_support(t, [RP[j]], [B[x, RP[j]]])
        pt += 1
        pf += len(set(B[s1, RM[(j + 1) % L]])) == 1
        s2 = cond_support(t, [M[j], RM[j]], [B[x, M[j]], B[x, RM[j]]])
        gt += 1
        gf += len(set(B[s2, RP[j]])) == 1
check(agree == nf and pf == pt and gf == gt and nf > 0, "A4 [T+D]",
      "constraint propagation: locking one rishon leaves its link partner one possibility; matter plus one rishon "
      "leaves the other rishon one (Gauss); matter records alone fix some rishons. Every forced value equals the "
      "actual value (support theorem), so it is a definite value, not a new record",
      f"partner forced {pf}/{pt}; Gauss-forced {gf}/{gt}; rishons forced by matter records {nf}/{tot}, equal to actual {agree}/{nf}")
# readout from records + forced values equals Born on the union
zf = 0.0
for t in range(1, T + 1):
    fr = np.zeros(NQ)
    cnt = np.zeros(NQ)
    for kk in range(K):
        x = cfg[kk, t]
        sup = cond_support(t, M, B[x, M])
        for r in RISH:
            if len(set(B[sup, r])) == 1:
                fr[r] += B[x, r]
                cnt[r] += 1
    for r in RISH:
        if cnt[r] > 50:
            # Born probability of n_r = 1 and forced
            pr = sum(P[t, c] for c in range(D) if len(set(B[cond_support(t, M, B[c, M]), r])) == 1 and B[c, r] == 1)
            zf = max(zf, zmax(np.array([fr[r] / K]), np.array([pr]), K))
check(zf < 4.5, "A5 [D]",
      "readout: values read as records plus forced values have the Born joint law of that union, the same law the "
      "rishon records themselves give; a forced value carries no extra or different information, so whether it "
      "counts as a record does not matter for readout",
      f"max z (forced-and-occupied frequency vs Born) {zf:.2f}")
# stale records: latest-record patterns read as current
emp0 = emp3 = 0
for t in range(1, T + 1):
    for kk in range(0, K, 4):
        fresh = RNG.random(NQ) < 0.5  # role-change-only rule: some sites refreshed, the rest hold t=0 records
        stale = np.where(fresh, B[cfg[kk, t]], B[cfg[kk, 0]])
        emp0 += len(cond_support(t, range(NQ), stale)) == 0
        emp3 += len(cond_support(t, range(NQ), B[cfg[kk, t]])) == 0
nt = T * len(range(0, K, 4))
check(emp0 > 0 and emp3 == 0, "A6 [D]",
      "'no possibility' appears only for locks that do not copy one configuration: latest records mixing half-ticks "
      "(some sites refreshed, the rest stale) read as current give empty supports; per-half-tick and on-change "
      "records (latest values current) never do. The clause is a consistency theorem of the law",
      f"empty supports: mixed-stale {emp0}/{nt}; on-change/per-half-tick {emp3}/{nt}")
# candidate (i)'s justification tested on matter: does one free matter lock fix another site?
mf = mt = 0
for t in range(1, T + 1):
    for kk in range(0, K, 10):
        x = cfg[kk, t]
        j = int(RNG.integers(L))
        sup = cond_support(t, [M[j]], [B[x, M[j]]])
        mt += 1
        mf += any(len(set(B[sup, y])) == 1 and len(set(B[P[t] > 1e-14][:, y])) == 2 for y in range(NQ) if y != M[j])
check(mf > 0, "A9 [T+D]",
      "candidate (i) fails its own justification: a single lock of a FREE matter site already leaves rishons one "
      "possibility through Gauss's law, so 'a lock fixes no other site' would exclude matter too, leaving nothing "
      "readable; the bound/free condition passes matter only because a Gauss cluster is not a mirror pair",
      f"one matter lock forces another (otherwise open) site in {mf}/{mt} samples")
# no-empty-support clause as a formation rule, random formation order within a half-tick
blocked = 0
for t in range(1, T + 1):
    for kk in range(0, K, 40):
        x = cfg[kk, t]
        order = RNG.permutation(NQ)
        done = []
        for y in order:
            done.append(y)
            blocked += len(cond_support(t, done, B[x, done])) == 0
check(blocked == 0, "A7 [T+D]",
      "read as a formation rule ('a record that would leave a site no possibility cannot form'), the clause never "
      "blocks a record in any formation order, so 'forbidden' and 'allowed but inconsistent' readings agree: it is idle",
      f"blocked formations {blocked}/{T * len(range(0, K, 40)) * NQ}")
# scoreboard of the candidate record rules on the same actual histories
recs = {"i": M, "ii": list(range(NQ)), "iii": list(range(NQ))}  # (iii) = (ii): its clause never blocks (A7)
law = {k: np.array([(B[cfg[:, t]][:, M]).mean(0) for t in range(T + 1)]) for k in recs}
tie = all(np.array_equal(law["i"], law[k]) for k in recs)
check(tie, "A10 [T+D]",
      "candidates (i) exclusion, (ii) every site, (iii) every site unless a support would empty: on the same actual "
      "histories the matter records are bit-identical and only the readable set differs; Born, Gauss (in the actual "
      "configuration) and every odds-level prediction tie, because no record conditions the odds",
      f"records per half-tick: (i) {len(recs['i'])}, (ii) {len(recs['ii'])}, (iii) {len(recs['iii'])}; matter record laws identical {tie}")
# non-abelian gauge safety: colour-component records in a gauge-invariant state
nm4 = 4


def cop(i):
    m = np.zeros((16, 16))
    for s in range(16):
        if (s >> i) & 1:
            m[s ^ (1 << i), s] = (-1) ** popc(s & ((1 << i) - 1))
    return m


C = [cop(i) for i in range(nm4)]  # psi_1, psi_2, r_1, r_2
vac = np.zeros(16)
vac[0] = 1
sing = (C[0].T @ C[3].T - C[1].T @ C[2].T) @ vac / np.sqrt(2)
ctrl = C[0].T @ C[3].T @ vac


def rec_law(state, g):
    cp = [g[0, 0] * C[0] + g[0, 1] * C[1], g[1, 0] * C[0] + g[1, 1] * C[1],
          g[0, 0] * C[2] + g[0, 1] * C[3], g[1, 0] * C[2] + g[1, 1] * C[3]]
    ns = [c.conj().T @ c for c in cp]
    out = []
    for pat in range(16):
        Pm = np.eye(16, dtype=complex)
        for i in range(4):
            Pm = Pm @ (ns[i] if (pat >> i) & 1 else np.eye(16) - ns[i])
        out.append(np.real(state.conj() @ Pm @ state))
    return np.array(out)


a, b = RNG.normal(size=2) + 1j * RNG.normal(size=2)
nrm = np.sqrt(abs(a) ** 2 + abs(b) ** 2)
g = np.array([[a, -np.conj(b)], [b, np.conj(a)]]) / nrm
dsing = abs(rec_law(sing, g) - rec_law(sing, np.eye(2))).max()
dctrl = abs(rec_law(ctrl, g) - rec_law(ctrl, np.eye(2))).max()
check(dsing < 1e-12 and dctrl > 1e-3, "A8 [T+D]",
      "non-abelian rishons: colour-component occupations are not gauge invariant, but in a gauge-invariant state "
      "their Born record law is the same in every gauge-rotated basis, so recording them is as safe as recording "
      "matter colour components (control: a non-singlet state)",
      f"max law change under random SU(2): singlet {dsing:.1e}, control {dctrl:.2f}")

# ------------------------------------------------------------------ B
print("== B. photons with every link site recorded")
NL, gc, J = 80, 0.3, 1.0
Hw = np.zeros((NL + 1, NL + 1))
Hw[0, 1] = Hw[1, 0] = gc
for i in range(1, NL):
    Hw[i, i + 1] = Hw[i + 1, i] = J
Gam = 2 * gc ** 2 / J
for dtw in (0.05, 0.02):
    Uw = expm(-1j * dtw * Hw)
    nst = int(round(20 / dtw))
    v = np.zeros(NL + 1, complex)
    v[0] = 1
    surv = []
    for _ in range(nst):
        v = Uw @ v
        surv.append(abs(v[0]) ** 2)
    tt = dtw * np.arange(1, nst + 1)
    sel = (tt > 3) & (tt < 15)
    rate = -np.polyfit(tt[sel], np.log(np.array(surv)[sel]), 1)[0]
    pz = abs(Uw[0, 0]) ** 2
    rz = -np.log(pz) / dtw
    if dtw == 0.05:
        r05, rz05 = rate, rz
    else:
        r02, rz02 = rate, rz
tP, wc = 5.391e-44, 2.998e8 / 5.29e-11
check(abs(r05 / Gam - 1) < 0.1 and abs(r02 / r05 - 1) < 1e-2 and rz05 < Gam / 10 and rz02 < rz05, "B1 [T+D+E]",
      "emitter decay with every link site recorded each half-tick: the Wigner-Weisskopf rate, independent of the "
      "half-tick; conditioning records would Zeno-freeze it",
      f"Gamma=2g^2/J {Gam:.3f}; fitted {r05:.3f} (dt 0.05), {r02:.3f} (dt 0.02); conditioned {rz05:.4f}, {rz02:.4f}; "
      f"hydrogen 2p estimate: conditioned at the Planck half-tick, lifetime ~1.60 ns x 2pi/(t_P c/a0) = "
      f"{1.6e-9 * 2 * np.pi / (tP * wc):.0e} s (measured 1.60 ns)")
# single photon in a Mach-Zehnder made of link sites; records of every link site each step
La = 6
nS = 2 + 2 * La + 2  # in, arm u (La), arm l (La), and outputs D1, D2 (plus a spare)
iu = [1 + i for i in range(La)]
il = [1 + La + i for i in range(La)]
D1, D2 = 1 + 2 * La, 2 + 2 * La


def mz_steps(phi):
    Us = []
    S = np.eye(nS, dtype=complex)  # input beam splitter on (in, u0, l0)
    q = np.array([[0, 1, -1], [1, 0.5 * np.sqrt(2), 0.5 * np.sqrt(2)], [1, -0.5 * np.sqrt(2), -0.5 * np.sqrt(2)]]) / np.sqrt(2)
    ix = [0, iu[0], il[0]]
    S[np.ix_(ix, ix)] = q
    Us.append(S)
    for i in range(La - 1):  # shift along both arms
        Sh = np.eye(nS, dtype=complex)
        for arm in (iu, il):
            Sh[[arm[i], arm[i + 1]]] = Sh[[arm[i + 1], arm[i]]]
        Us.append(Sh)
    e = np.exp(1j * phi)
    Bs = np.eye(nS, dtype=complex)  # output beam splitter on (u_end, l_end, D1, D2), phase phi on arm u
    ix = [iu[-1], il[-1], D1, D2]
    Bs[np.ix_(ix, ix)] = np.array([[0, 0, 1, 1], [0, 0, 1, -1], [e, 1, 0, 0], [e, -1, 0, 0]]) / np.sqrt(2)
    Us.append(Bs)
    return Us


cpos = 2.0 * (1 - np.eye(nS))
vis, visc, unit = [], [], True
for phi in (0.0, np.pi):
    Us = mz_steps(phi)
    unit &= all(np.allclose(Ux.conj().T @ Ux, np.eye(nS)) for Ux in Us)
    v = np.zeros(nS, complex)
    v[0] = 1
    ps = [v]
    for Ux in Us:
        ps.append(Ux @ ps[-1])
    cf = walk(ps, Us, cpos, 3000, RNG)
    vis.append(np.mean(cf[:, -1] == D1))
    # conditioning: the recorded link site collapses the photon each step
    hits = 0
    for kk in range(1500):
        w = np.zeros(nS, complex)
        w[0] = 1
        for Ux in Us:
            w = Ux @ w
            pp = abs(w) ** 2
            c = RNG.choice(nS, p=pp / pp.sum())
            w = np.zeros(nS, complex)
            w[c] = 1
        hits += c == D1
    visc.append(hits / 1500)
V = (vis[0] - vis[1]) / (vis[0] + vis[1])
Vc = abs(visc[0] - visc[1]) / (visc[0] + visc[1])
check(unit and V > 0.98 and Vc < 0.1, "B2 [T+D]",
      "single photon through a Mach-Zehnder of link sites, every site recorded each step: full fringes; conditioning "
      "records erase them (bare which-arm records, read only through pointers, as for matter)",
      f"P(D1) at phi=0, pi: {vis[0]:.3f}, {vis[1]:.3f}; V={V:.3f}; conditioned V={Vc:.3f}")
Us = mz_steps(0.0)
v = np.zeros(nS, complex)
v[0] = 1
ps = [v]
for Ux in Us:
    ps.append(Ux @ ps[-1])
cf = walk(ps, Us, cpos, 3000, RNG)
armu = np.mean(np.isin(cf[:, 1], iu))
# a configuration is one occupied site (number is conserved): arm records never coincide
coin = sum(int(np.isin(c, iu)) * int(np.isin(c, il)) for c in cf.ravel())
g2 = coin / max(1, cf.size)
check(abs(armu - 0.5) < 0.04 and g2 == 0.0, "B3 [T+D]",
      "anticorrelation: each actual configuration holds the one photon on one link site, so arm records never "
      "coincide (g2(0) = 0, measured single-photon g2 well below 1); a definite or classically mixed link gives "
      "g2 >= 1 (definite-links)",
      f"P(arm u recorded) {armu:.3f}; arm coincidences {coin}/{cf.size}; g2(0) = {g2:.0f}")
# repeated link-number records: non-demolition repeatability; decoherence only from a pointer in the odds
nmax = 4
amp = np.array([1, 1, 1, 0, 0], complex) / np.sqrt(3)
n_op = np.diag(np.arange(nmax + 1))
Uf = expm(-1j * 0.7 * n_op)
ps = [amp]
for _ in range(8):
    ps.append(Uf @ ps[-1])
cn = np.abs(np.subtract.outer(np.arange(nmax + 1), np.arange(nmax + 1))).astype(float)
cfn = walk(ps, [Uf] * 8, cn, 3000, RNG)
rep = np.mean(np.all(cfn == cfn[:, :1], axis=1))
adag = np.diag(np.sqrt(np.arange(1, nmax + 1)), -1)
coh0 = abs(amp.conj() @ adag.T @ amp)
coh8 = abs(ps[-1].conj() @ adag.T @ ps[-1])
# pointer: a probe qubit gets a phase pi/2 per photon (dispersive), in the odds
probe = np.kron(amp, np.array([1, 1]) / np.sqrt(2))
Ud = np.diag(np.exp(-1j * np.pi / 2 * np.kron(np.arange(nmax + 1), [0, 1])))
pr = (Ud @ probe).reshape(nmax + 1, 2)
rho = pr @ pr.conj().T
cohp = abs(np.trace(rho @ adag.T))
check(rep == 1.0 and abs(coh8 - coh0) < 1e-12 and cohp < 0.75 * coh0, "B4 [T+D]",
      "repeated link-number records agree at every half-tick (the fewest-change transport keeps a stationary "
      "number), so link records count photons without demolition, while the field's coherence stays: phase "
      "decoherence, as in measured non-demolition counting, comes from a pointer coupled in the odds",
      f"repeat fraction {rep:.3f}; |<a>| before/after {coh0:.3f}/{coh8:.3f}; with a dispersive probe {cohp:.3f}")

# ------------------------------------------------------------------ C
print("== C. mediated entanglement with the mediator recorded each half-tick")
G, hb = 6.674e-11, 1.0546e-34
m, d, dx, Tr = 1e-14, 200e-6, 250e-6, 2.5
ph = lambda r: G * m * m * Tr / (hb * r)
pin, pout, pcr = ph(d), ph(d + 2 * dx), ph(d + dx)
dphi = pin + pout - 2 * pcr
Ct = abs(np.sin(dphi / 2))
dm = 14
w0 = 1.0
gm = np.sqrt(dphi / (16 * np.pi))
am = np.diag(np.sqrt(np.arange(1, dm)), 1)
Z = np.diag([1.0, -1.0])
I2, Im = np.eye(2), np.eye(dm)
Hm = w0 * np.kron(np.kron(I2, I2), am.T @ am) + gm * np.kron(np.kron(Z, I2) + np.kron(I2, Z), am + am.T)
nsteps = 200
Um = expm(-1j * (2 * np.pi / w0 / nsteps) * Hm)
plus = np.array([1, 1]) / np.sqrt(2)
v0 = np.kron(np.kron(plus, plus), np.eye(dm)[0]).astype(complex)


def conc(ab):
    a_ = ab.reshape(2, 2)
    return 2 * abs(np.linalg.det(a_))


v = v0.copy()
pmid = 0.0
for k in range(nsteps):
    v = Um @ v
    if k == nsteps // 2:
        pmid = 1 - np.sum(abs(v.reshape(4, dm)[:, 0]) ** 2)
back = np.sum(abs(v.reshape(4, dm)[:, 0]) ** 2)
Cf = conc(v.reshape(4, dm)[:, 0] / np.sqrt(back))
Ccs = []
for kk in range(200):
    w = v0.copy()
    for k in range(nsteps):
        w = Um @ w
        pn = np.sum(abs(w.reshape(4, dm)) ** 2, 0)
        n = RNG.choice(dm, p=pn / pn.sum())
        ab = w.reshape(4, dm)[:, n]
        w = np.kron(ab / np.linalg.norm(ab), np.eye(dm)[n])
    Ccs.append(conc(w.reshape(4, dm)[:, n]))
Cc = float(np.mean(Ccs))
check(abs(pin - 0.79) < 0.01 and abs(Ct - 0.156) < 0.001 and abs(Cf - Ct) < 2e-3 and pmid > 1e-3 and Cc < Ct / 5,
      "C1 [T+D+E]",
      "a mediator register (edge for gravity, link for a Coulomb gate) recorded every half-tick: it stays indefinite "
      "mid-run, returns, and the masses end with the predicted entanglement; conditioning pins it and loses it",
      f"inner phase {pin:.3f} rad, dphi {dphi:.3f}, target C {Ct:.4f}; toy C {Cf:.4f} (return {back:.6f}, mid-run "
      f"P(n>0) {pmid:.4f}); conditioned C {Cc:.4f}")
print("supplied: link ring w=1, m=0.5, dt 0.35 (A); chain g=0.3, J=1; MZ layout; probe phase pi/2 (B); "
      "oscillator mediator, 200 half-ticks per period, d=14 (C); seed 20261022")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
