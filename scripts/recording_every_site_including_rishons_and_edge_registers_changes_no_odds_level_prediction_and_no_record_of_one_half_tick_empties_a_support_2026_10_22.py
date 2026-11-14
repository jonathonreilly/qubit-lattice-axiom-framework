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
  C  mediated entanglement in a calibrated toy: the oscillator coupling gm is
     set from the target phase, gm = sqrt(dphi/(16 pi)), so the toy reproduces
     |sin(dphi/2)| by construction (an imposed-phase check, not an independent
     gravity prediction); recording the mediator every half-tick keeps that
     entanglement, the conditioning alternative makes the mediator definite and
     loses it
Contrast throughout: the alternative where records condition the odds.
Supplied: toy Hamiltonians, sizes, couplings, dt, seeds, tolerance 1e-12; the
BMV inputs (1e-14 kg, 200 um, 250 um, 2.5 s) and the target-calibrated gm (C);
the 1.60 ns hydrogen 2p lifetime, a0 and t_P, and a flat coupling spectrum cut
off at c/a0, as inputs of a printed conditional estimate that is not a check (B1).
"""
import sys
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
# T3 is structural: walk() takes only the odds, the half-ticks and the cost, never a record set, so the three rules see
# the same histories by construction. A comparison of those histories with themselves cannot fail, so it is not counted.
print("STRUCTURAL (not counted) A10 [T]: record-set independence holds by construction: the transport (walk) takes "
      "the odds, the half-ticks and the cost and no record set, so candidates (i), (ii) and (iii) record the same actual "
      f"histories and differ only in the readable set; records per half-tick: (i) {len(recs['i'])}, (ii) {len(recs['ii'])}, "
      f"(iii) {len(recs['iii'])}")
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
check(abs(r05 / Gam - 1) < 0.1 and abs(r02 / r05 - 1) < 1e-2 and rz05 < Gam / 10 and rz02 < rz05, "B1 [T+D]",
      "emitter decay with every link site recorded each half-tick: the Wigner-Weisskopf rate, independent of the "
      "half-tick; conditioning records would Zeno-freeze it",
      f"Gamma=2g^2/J {Gam:.3f}; fitted {r05:.3f} (dt 0.05), {r02:.3f} (dt 0.02); conditioned {rz05:.4f}, {rz02:.4f}")
# the conditioned (Zeno) rate is set by the short-time energy variance, not by the decay rate: for an emitter that starts
# on site 0, |U00(dt)|^2 = 1 - Var(H) dt^2 + O(dt^4) with Var(H) = g^2, so -ln|U00|^2/dt -> g^2 dt. Two chains with the
# same Golden-rule rate 2g^2/J = 0.18, (g, J) = (0.3, 1) and (0.3 sqrt 2, 2), have conditioned rates in the ratio 2.
zr = {}
for g_, J_ in ((0.3, 1.0), (0.3 * np.sqrt(2), 2.0)):
    H_ = np.zeros((NL + 1, NL + 1))
    H_[0, 1] = H_[1, 0] = g_
    for i in range(1, NL):
        H_[i, i + 1] = H_[i + 1, i] = J_
    zr[(g_, J_)] = (2 * g_ ** 2 / J_, -np.log(abs(expm(-1j * 0.05 * H_)[0, 0]) ** 2) / 0.05, g_ ** 2 * 0.05)
(G1_, z1_, v1_), (G2_, z2_, v2_) = zr.values()
check(abs(G1_ - G2_) < 1e-12 and abs(z1_ / v1_ - 1) < 0.02 and abs(z2_ / v2_ - 1) < 0.02 and abs(z2_ / z1_ - 2) < 0.05,
      "B1b [T+D]",
      "short-time input of the Zeno contrast: the conditioned rate is dt Var(H) = g^2 dt, so two chains with the same "
      "decay rate 2g^2/J give conditioned rates in the ratio 2; a decay rate alone does not fix the Zeno suppression",
      f"Gamma {G1_:.3f} = {G2_:.3f}; conditioned {z1_:.5f} vs g^2 dt {v1_:.5f}; {z2_:.5f} vs {v2_:.5f}; ratio {z2_ / z1_:.3f}")
print(f"      CONDITIONAL ESTIMATE (not a check; supplied short-time model): with records conditioning the odds every "
      f"tau = t_P, the rate becomes tau Var(H)/hbar^2; with a supplied flat coupling spectrum cut off at w_c = c/a0, "
      f"Var(H)/hbar^2 = Gamma w_c/(2 pi), so the hydrogen 2p lifetime 1.60 ns (supplied) would become "
      f"~{1.6e-9 * 2 * np.pi / (tP * wc):.0e} s; the number scales as 1/w_c and is not derived from the chain or the lifetime")
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
      "coincide (g2(0) = 0 by construction of the one-photon configuration space; the computed part is P(arm u) = 1/2; "
      "measured single-photon g2 well below 1); comparator, not checked here: in a classical model where the detected "
      "intensity is a nonnegative random variable I, g2(0) = <I^2>/<I>^2 >= 1 by Cauchy-Schwarz",
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
      "a mediator register (edge for gravity, link for a Coulomb gate) recorded every half-tick in a CALIBRATED toy "
      "(coupling gm = sqrt(dphi/(16 pi)) set from the target phase, so toy C = |sin(dphi/2)| by construction; not an "
      "independent gravity prediction): it stays indefinite mid-run, returns, and the qubits end with the imposed-phase "
      "entanglement; conditioning pins it and loses it",
      f"inner phase {pin:.3f} rad, dphi {dphi:.3f}, target C {Ct:.4f}; gm {gm:.5f} calibrated; toy C {Cf:.4f} (return "
      f"{back:.6f}, mid-run P(n>0) {pmid:.4f}); conditioned C {Cc:.4f}")
# calibration disclosure: completing the square in H = a^+a + gm (zA + zB)(a + a^+) gives the branch phase
# 2 pi gm^2 (zA + zB)^2 per period and concurrence |sin(8 pi gm^2)|; the toy follows whatever gm is put in
gm2 = 1.25 * gm
Hm2 = w0 * np.kron(np.kron(I2, I2), am.T @ am) + gm2 * np.kron(np.kron(Z, I2) + np.kron(I2, Z), am + am.T)
v2 = expm(-1j * 2 * np.pi / w0 * Hm2) @ v0
back2 = np.sum(abs(v2.reshape(4, dm)[:, 0]) ** 2)
Cf2 = conc(v2.reshape(4, dm)[:, 0] / np.sqrt(back2))
check(abs(16 * np.pi * gm ** 2 - dphi) < 1e-12 and abs(Cf2 - abs(np.sin(8 * np.pi * gm2 ** 2))) < 2e-3
      and abs(Cf2 - Ct) > 0.05, "C1b [T+D]",
      "calibration control: the toy concurrence is |sin(8 pi gm^2)| for the gm put in; with gm' = 1.25 gm (not "
      "calibrated) it follows gm' and misses the BMV target, so the C1 agreement is imposed by the calibration",
      f"16 pi gm^2 - dphi = {16 * np.pi * gm ** 2 - dphi:.1e}; gm' {gm2:.5f}: toy C {Cf2:.4f} vs |sin(8 pi gm'^2)| "
      f"{abs(np.sin(8 * np.pi * gm2 ** 2)):.4f} vs target {Ct:.4f}")
print("supplied: link ring w=1, m=0.5, dt 0.35 (A); chain g=0.3, J=1 (and g=0.3 sqrt 2, J=2 in B1b); MZ layout; "
      "probe phase pi/2 (B); "
      "oscillator mediator, 200 half-ticks per period, d=14, coupling gm = sqrt(dphi/(16 pi)) CALIBRATED from the "
      "target phase (C); comparison inputs: BMV 1e-14 kg, 200 um, 250 um, 2.5 s; for the conditional estimate only: "
      "hydrogen 2p 1.60 ns, a0, t_P, flat coupling spectrum cut off at c/a0; "
      "seed 20261022")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
sys.exit(1 if NF else 0)
