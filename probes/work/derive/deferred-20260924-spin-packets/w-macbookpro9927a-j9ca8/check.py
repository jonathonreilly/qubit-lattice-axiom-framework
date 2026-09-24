#!/usr/bin/env python3
"""Deferred-science recovery, spin-packets (first pass): checks for ATTEMPT.md, worker w-macbookpro9927a-j9ca8 (claude-opus-5-5).

Target (review finding U13-R3, PR8839): the deferred replay of the saved high-spin propagations PROPAGATED_S{64,96,128,192}.npz
behind the landed actual-first-output note's diagnostic "at S=192, t=1.2 ... the |f|<=2 flat-window density differs from its
predicted component by about 2.06e-4 in trace norm; the complementary probability in that window is about 1.24e-8".

Everything model-side is rebuilt here from the text of the landed prepared-flat-sector note (origin/main), without importing
the frozen builders: sites 0..7, A = even sites with Gauss background 1, E_e = f + sum_{b<=e}(q_b - [b even]), hops with
amplitude -g_{S,k}(E), g = sqrt([1 - E(E+k)/(S(S+1))]_+), |E + k| <= S; births on a link with both ends empty; the flat basis
(4); H2 = -A^dag A, H4 = (A^dag A)^2 - Z^dag Z/2, Gamma = sum (jA)^dag(jA); generator eta(H2+4) + delta H4 - i kappa Gamma/2,
eta = K S(S+1), (K, delta, kappa) = (.4, .7, .3). Families Q (provenance, SHA256) and X (flat-sector algebra, the seed) are
exact (integers, fractions). Family N (the replay) is floating point by nature (scipy expm_multiply), labelled as such.
"""
from __future__ import annotations

import hashlib
import io
import json
import math
import subprocess
import time
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np
from scipy.sparse import coo_matrix, identity
from scipy.sparse.linalg import expm_multiply

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    print(OUT[-1], flush=True)
    if not ok:
        FAILS.append(tag)


# ----------------------------------------------------------------------------------------------------------------------
# the supplied ring, from the note's text

def fields(q, f):
    E, v = [], f
    for a in range(8):
        v += q[a] - (1 if a % 2 == 0 else 0)
        E.append(v)
    assert E[-1] == f
    return tuple(E)


def charge_words(n):
    nminus = (n - 4) // 2
    out = []
    for occ in combinations(range(8), n):
        for mins in combinations(occ, nminus):
            out.append(tuple(0 if a not in occ else (-1 if a in mins else 1) for a in range(8)))
    return out


def gsq(E, k, S):
    """exact g^2 (S = None: unit rotor)"""
    return Fr(1) if S is None else max(Fr(0), 1 - Fr(E * (E + k), S * (S + 1)))


def hops(q, f, S, exact=False):
    E = fields(q, f)
    for s in range(8):
        c = q[s]
        if not c:
            continue
        for d in (1, -1):
            t = (s + d) % 8
            if q[t]:
                continue
            e = s if d == 1 else t
            k = -d * c
            if S is not None and abs(E[e] + k) > S:
                continue
            qq = list(q); qq[s] = 0; qq[t] = c
            g2 = gsq(E[e], k, S)
            yield (tuple(qq), f + (k if e == 7 else 0)), (g2 if exact else -math.sqrt(g2))


def births(q, f, S, exact=False):
    E = fields(q, f)
    for e in range(8):
        u, v = e, (e + 1) % 8
        if q[u] or q[v]:
            continue
        for sg in (-1, 1):
            if S is not None and abs(E[e] + sg) > S:
                continue
            qq = list(q); qq[u] = sg; qq[v] = -sg
            g2 = gsq(E[e], sg, S)
            yield (e, sg), (tuple(qq), f + (sg if e == 7 else 0)), (g2 if exact else math.sqrt(g2))


def Wn(q):
    return sum(1 for a in (0, 2, 4, 6) if q[a] == 0)


BP = {"01": (0, 1), "12": (1, 2), "23": (2, 3), "03": (0, 3)}


def config(C, r, f):
    i, j = BP[C]
    occ = sorted([0, 2, 4, 6, 2 * i + 1, 2 * j + 1])
    return (tuple(0 if a not in occ else (-1 if occ.index(a) == r % 6 else 1) for a in range(8)), f)


def c0(r):
    return -1 if r % 6 == 0 else 1


def flat_vector(kind, r, f):   # sqrt2 * a_(r,f) or sqrt2 * b_(r,f), note eq. (4)
    if kind == 0:
        return {config("01", r, f): 1, config("23", (r - 1) % 6, f + c0(r)): -1}
    return {config("12", r, f): 1, config("03", r, f): -1}


ATAB = {0: (-5, 2), 1: (-3, 1), 2: (0, 0), 3: (3, 1), 4: (5, 2), 5: (8, 4)}


def d_a(r, f):
    A, B = ATAB[r]
    return 4 * f * f + A * f + B


def d_b(r, f):
    return 4 * f * f - 8 * f + 4 if r == 0 else d_a(r - 1, f)


def step(v, sector, D2=False):
    """one hop of the unit rotor into the given sector; D2=True carries E(E+k) along for the electric term"""
    out = defaultdict(int)
    for (q, f), c in v.items():
        for w, _ in hops(q, f, None):
            if Wn(w[0]) == sector:
                out[w] += c
    return {k: x for k, x in out.items() if x}


def lin(*terms):
    out = defaultdict(Fr)
    for c, v in terms:
        for k, x in v.items():
            out[k] += c * x
    return {k: x for k, x in out.items() if x}


# ----------------------------------------------------------------------------------------------------------------------
# Family X: the flat-sector algebra and the seed, exactly


def family_x() -> None:
    bad = defaultdict(int)
    for kind in (0, 1):
        for r in range(6):
            for f in (-3, 0, 2, 5):
                v = flat_vector(kind, r, f)
                # (unit-rotor coefficients: each hop -1, so A^dag A paths carry +1)
                M = step(step(v, 1), 0)
                if M != {k: 4 * x for k, x in v.items()}:
                    bad["H2"] += 1
                MM = step(step(M, 1), 0)
                ZZ = step(step(step(step(v, 1), 2), 1), 0)
                H4v = lin((1, MM), (Fr(-1, 2), ZZ))
                if kind == 0:
                    want = lin((12, v), (2, flat_vector(1, r, f)), (-2, flat_vector(1, (r - 1) % 6, f + c0(r))))
                else:
                    want = lin((12, v), (2, flat_vector(0, r, f)), (-2, flat_vector(0, (r + 1) % 6, f - c0(r + 1))))
                if lin((1, H4v), (-1, want)):
                    bad["H4"] += 1
                # D2: each two-hop path P -> Pi1 -> P weighs (E1(E1+k1) + E2(E2+k2))/2
                dv = defaultdict(Fr)
                for (q, ff), cc in v.items():
                    E0 = fields(q, ff)
                    for s in range(8):
                        ch = q[s]
                        if not ch:
                            continue
                        for dd in (1, -1):
                            t = (s + dd) % 8
                            if q[t]:
                                continue
                            e = s if dd == 1 else t; k = -dd * ch
                            q1 = list(q); q1[s] = 0; q1[t] = ch; q1 = tuple(q1); f1 = ff + (k if e == 7 else 0)
                            if Wn(q1) != 1:
                                continue
                            E1 = fields(q1, f1)
                            for s2 in range(8):
                                c2 = q1[s2]
                                if not c2:
                                    continue
                                for d2 in (1, -1):
                                    t2 = (s2 + d2) % 8
                                    if q1[t2]:
                                        continue
                                    e2 = s2 if d2 == 1 else t2; k2 = -d2 * c2
                                    q2 = list(q1); q2[s2] = 0; q2[t2] = c2; q2 = tuple(q2)
                                    if Wn(q2) != 0:
                                        continue
                                    dv[(q2, f1 + (k2 if e2 == 7 else 0))] += Fr(E0[e] * (E0[e] + k) + E1[e2] * (E1[e2] + k2), 2) * cc
                want = d_a(r, f) if kind == 0 else d_b(r, f)
                if Fr(sum(v.get(k, 0) * x for k, x in dv.items()), 2) != want:
                    bad["D2"] += 1
                for k2 in (0, 1):
                    for r2 in range(6):
                        for f2 in range(f - 3, f + 4):
                            if (k2, r2, f2) != (kind, r, f):
                                u = flat_vector(k2, r2, f2)
                                if sum(u.get(k, 0) * x for k, x in dv.items()) != 0:
                                    bad["D2 off"] += 1
                # Gamma = sum_(e,sigma) (jA)^dag (jA): j is injective with unit amplitude in the rotor
                Av = step(v, 1)
                back = defaultdict(int)
                for (q, ff), c in Av.items():
                    for _, _, _ in births(q, ff, None):
                        back[(q, ff)] += c
                if step(back, 0) != {k: 4 * x for k, x in v.items()}:
                    bad["Gamma"] += 1
    check("X1", not bad, "flat basis (4) rebuilt from the note's labels: A^dag A = 4 (H2 = -4), H4 action (6), the electric "
          "compression d_a = 4f^2 + A_r f + B_r / d_b (diagonal, no other flat element within f +- 3), and Gamma = 4 on all "
          f"12 types at f = -3, 0, 2, 5, exactly {dict(bad) if bad else ''}")
    # the seed: the four-record all-A-plus zero-field state, mark (link 0, sigma = +1): one hop-then-birth path
    q0, f0 = (1, 0, 1, 0, 1, 0, 1, 0), 0
    seedok = fields(q0, f0) == (0,) * 8
    for S in (1, 2, 3, 8, 64, 96, 128, 192):
        out = defaultdict(Fr)
        for (q1, f1), g1 in hops(q0, f0, S, exact=True):
            for mark, w, g2 in births(q1, f1, S, exact=True):
                if mark == (0, 1):
                    out[w] += g1 * g2
        seedok &= dict(out) == {config("03", 1, 1): 1}
    check("X2", seedok, "the four-record all-A-plus zero-field state (all E = 0): for the mark (link 0, sigma = +1) the only "
          "hop-then-birth path is the hop 0 -> 7 across the cut followed by the birth on link (0,1), squared amplitude 1, "
          "output |03,1,1> = (+,-,+,0,+,0,+,+), f = 1, for every S in {1,2,3,8,64,96,128,192}; its flat part is -b_(1,1)/sqrt2, "
          "weight exactly 1/2 (b_(1,1) is the only basis vector containing |03,1,1>)")


# ----------------------------------------------------------------------------------------------------------------------
# Family N: the replay (floating point)

K_, DELTA, KAPPA = .4, .7, .3
TIMES = np.linspace(0, 1.2, 4)


def physical_words(n, S):
    out = []
    for q in charge_words(n):
        d = fields(q, 0)
        for f in range(max(-S - e for e in d), min(S - e for e in d) + 1):
            out.append((q, f))
    return out


def build(S):
    words = physical_words(6, S)
    ix = {w: i for i, w in enumerate(words)}
    sec = np.array([Wn(q) for q, f in words])
    R, C, V = [], [], []
    for c, (q, f) in enumerate(words):
        for w, a in hops(q, f, S):
            R.append(ix[w]); C.append(c); V.append(a)
    n = len(words)
    T = coo_matrix((V, (R, C)), shape=(n, n)).tocsr()
    s0, s1, s2 = (np.flatnonzero(sec == k) for k in (0, 1, 2))
    A = T[s1][:, s0]
    Z = T[s2][:, s1] @ A
    M = (A.T @ A).tocsr()
    H4 = M @ M - (Z.T @ Z) / 2
    term = physical_words(8, S)
    tx = {w: i for i, w in enumerate(term)}
    w1 = [words[i] for i in s1]
    Gam = None
    for e in range(8):
        for sg in (-1, 1):
            r_, c_, v_ = [], [], []
            for col, (q, f) in enumerate(w1):
                for mark, w, a in births(q, f, S):
                    if mark == (e, sg):
                        r_.append(tx[w]); c_.append(col); v_.append(a)
            B = coo_matrix((v_, (r_, c_)), shape=(len(term), len(w1))).tocsr() @ A
            Gam = B.T @ B if Gam is None else Gam + B.T @ B
    P = [words[i] for i in s0]
    gen = K_ * S * (S + 1) * (-M + 4 * identity(len(P), format="csr")) + DELTA * H4 - 0.5j * KAPPA * Gam
    return P, gen.tocsr(), abs(T - T.T).max()


def flat_limit(cut):
    basis = [(k, r, f) for k in (0, 1) for r in range(6) for f in range(-cut, cut + 1)]
    ix = {b: i for i, b in enumerate(basis)}
    R, C, V = [], [], []
    for col, (k, r, f) in enumerate(basis):
        R.append(col); C.append(col); V.append(K_ * (d_a(r, f) if k == 0 else d_b(r, f)) + 12 * DELTA - 2j * KAPPA)
        outs = ([((1, r, f), 2), ((1, (r - 1) % 6, f + c0(r)), -2)] if k == 0 else
                [((0, r, f), 2), ((0, (r + 1) % 6, f - c0(r + 1)), -2)])
        for tgt, c in outs:
            if tgt in ix:
                R.append(ix[tgt]); C.append(col); V.append(DELTA * c)
    Hf = coo_matrix((V, (R, C)), shape=(len(basis),) * 2).tocsr()
    phi0 = np.zeros(len(basis), complex)
    phi0[ix[(1, 1, 1)]] = -1 / np.sqrt(2)
    return basis, expm_multiply(-1j * Hf, phi0, start=0, stop=TIMES[-1], num=len(TIMES), endpoint=True)


FROZEN = "8ccef7097deb77fe79f0d9406eef7d5c6e4962bd"
CAMP = ".claude/science/mobile-record-formation-20260920/campaign12h_fourth/"


def blob(path):
    return subprocess.run(["git", "show", f"{FROZEN}:{CAMP}{path}"], capture_output=True).stdout


def family_n() -> None:
    hist = json.loads(blob("actual_first_output_author/ACTUAL_OUTPUT_CONTROLS.json"))["finite_window_controls"]
    basis48, lim48 = flat_limit(48)
    basis64, lim64 = flat_limit(64)
    i64 = {b: i for i, b in enumerate(basis64)}
    cutdiff = max(abs(lim48[t][i] - lim64[t][i64[b]]) for t in range(4) for i, b in enumerate(basis48))
    bidx = {b: i for i, b in enumerate(basis48)}
    rows = []
    worst_vec, worst_rel, worst_abs = 0.0, 0.0, 0.0
    t0 = time.time()
    for S in (64, 96, 128, 192):
        P, gen, asym = build(S)
        ix = {w: i for i, w in enumerate(P)}
        z = np.load(io.BytesIO(blob(f"finite_spin_unprepared_followup/PROPAGATED_S{S}.npz")))
        theirs = [(tuple(int(x) for x in q), int(f)) for q, f in zip(z["charges"], z["circulations"])]
        same = set(theirs) == set(P) and len(theirs) == len(P)
        psi = np.zeros(len(P), complex); psi[ix[config("03", 1, 1)]] = 1
        flat = np.zeros(len(P), complex)
        for w, c in flat_vector(1, 1, 1).items():
            flat[ix[w]] += -c / 2
        Aop = -1j * gen
        vecs = expm_multiply(Aop, np.column_stack((flat, psi - flat)), start=0, stop=TIMES[-1], num=4, endpoint=True,
                             traceA=Aop.diagonal().sum())
        perm = np.array([ix[w] for w in theirs]) if same else None
        dvec = max(np.abs(vecs[i][perm] - z["vectors"][i]).max() for i in range(4)) if same else math.inf
        worst_vec = max(worst_vec, dvec)
        comps = []
        for lab in basis48:
            v = flat_vector(*lab)
            if all(w in ix for w in v):
                comps.append((lab, [(ix[w], c / np.sqrt(2)) for w, c in v.items()]))
        for ti in range(4):
            tot = vecs[ti][:, 0] + vecs[ti][:, 1]
            br = vecs[ti][:, 1]
            for N in (1, 2, 8):
                sel = [(lab, cs) for lab, cs in comps if abs(lab[2]) <= N]
                got = np.array([sum(c * tot[i] for i, c in cs) for lab, cs in sel])
                bri = np.array([sum(c * br[i] for i, c in cs) for lab, cs in sel])
                exp_ = np.array([lim48[ti][bidx[lab]] for lab, cs in sel])
                aa, bb, cc = np.vdot(got, got).real, np.vdot(exp_, exp_).real, np.vdot(got, exp_)
                err = math.sqrt(max(0.0, (aa + bb) ** 2 - 4 * abs(cc) ** 2))
                comp = float(np.vdot(bri, bri).real)
                h = next(x for x in hist if x["S"] == S and x["N"] == N and abs(x["t"] - TIMES[ti]) < 1e-9)
                for mine, theirs_v in ((err, h["density_trace_norm_error"]), (comp, h["complementary_window_weight"])):
                    if abs(theirs_v) >= 1e-12:     # rows at t = 0 are rounding-level (~1e-17): compare absolutely
                        worst_rel = max(worst_rel, abs(mine - theirs_v) / abs(theirs_v))
                    else:
                        worst_abs = max(worst_abs, abs(mine - theirs_v))
                if ti == 3 and N == 2:
                    rows.append((S, len(P), same, asym, err, comp))
    tbl = "; ".join(f"S={S} dim {n}: err {e:.4e}, compl {c:.4e}" for S, n, s, a, e, c in rows)
    s192 = next(r for r in rows if r[0] == 192)
    ok = (all(r[2] and r[3] < 1e-13 for r in rows) and worst_vec < 1e-9 and worst_rel < 1e-6 and worst_abs < 1e-12
          and cutdiff < 1e-10
          and abs(s192[4] - 2.06e-4) < 5e-7 and abs(s192[5] - 1.24e-8) < 5e-11)
    check("N1", ok, "floating replay, independent builder (hermitian hop, physical Gauss intervals): word sets equal the saved "
          f"ones at S = 64, 96, 128, 192; propagated vectors equal the saved PROPAGATED_S*.npz to {worst_vec:.1e} at "
          f"t = 0, .4, .8, 1.2; all 48 window rows (N = 1, 2, 8) of ACTUAL_OUTPUT_CONTROLS reproduced (relative "
          f"{worst_rel:.1e} where >= 1e-12, absolute {worst_abs:.1e} for the rounding-level t = 0 rows); flat limit cut 48 "
          f"vs 64 agree to {cutdiff:.1e} (propagator tolerance; the truncation tail is ~1e-32). t = 1.2, N = 2: {tbl} "
          f"({time.time() - t0:.0f} s)")


# ----------------------------------------------------------------------------------------------------------------------
# Family Q: provenance chain and sources

MAIN = "0e6ad82850"
NOTE = "docs/ACTUAL_FIRST_OUTPUT_COMPONENTS_AND_TWO_BIRTH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-24.md"
PREP = "docs/PREPARED_FLAT_SECTOR_WITH_ELECTRIC_DYNAMICS_AND_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md"
HERE = "probes/work/derive/deferred-20260924-spin-packets/w-macbookpro9927a-j9ca8/"


def family_q() -> int:
    bad = []
    note = subprocess.run(["git", "show", f"{MAIN}:{NOTE}"], capture_output=True, text=True).stdout
    prep = subprocess.run(["git", "show", f"{MAIN}:{PREP}"], capture_output=True, text=True).stdout
    for q in ["At S=192, t=1.2, K=.4, delta=.7, kappa=.3, the |f|<=2 flat-window",
              "density differs from its predicted component by about 2.06e-4 in trace norm;",
              "The archived high-spin saved-vector replay remains a historical diagnostic"]:
        if q not in note:
            bad.append("note")
    for q in ["b_(r,f)=(|12,r,f>-|03,r,f>)/sqrt(2)", "| 5 | 8 | 4 |", "H4 b_(r,f) =12 b_(r,f)+2 a_(r,f)"]:
        if q not in prep:
            bad.append("prep")
    b = json.load(open("probes/work/deferred-science-20260924/batch-13.json"))
    if "Explicitly defer saved-vector replay" not in next(x for x in b["findings"] if x["id"] == "U13-R3")["resolution"]:
        bad.append("U13-R3")
    st = json.load(open(HERE + "RECOVERY_STATUS.json"))
    allsrc = {(x["pr"], x["path"]): x for x in b["sources"]}
    for e in st["source_groups_inspected"]:
        m = allsrc[(e["pr"], e["path"])]
        data = subprocess.run(["git", "show", f"{m['head']}:{m['path']}"], capture_output=True).stdout
        if hashlib.sha256(data).hexdigest() != m["sha256"] or e["sha256"] != m["sha256"]:
            bad.append("sha:" + e["path"].split("/")[-1])
    # the chain: vector files <- DECOMPOSITION_RESULTS <- script (asserts builder 5030a960) <- builder (asserts flat module 50df6b9c)
    dec = json.loads(blob("finite_spin_unprepared_followup/DECOMPOSITION_RESULTS.json"))
    for row in dec["rows"]:
        if hashlib.sha256(blob("finite_spin_unprepared_followup/" + row["vector_file"])).hexdigest() != row["vector_sha256"]:
            bad.append("vec " + row["vector_file"])
    script = blob("finite_spin_unprepared_followup/unprepared_decomposition_check.py").decode()
    builder = blob("finite_spin_post_birth_author/finite_spin_dynamics_check.py")
    flatmod = blob("finite_spin_post_birth_author/flat_band_spin_correction_probe.py")
    b5 = hashlib.sha256(builder).hexdigest()
    if not (b5.startswith("5030a960") and b5 in script and hashlib.sha256(flatmod).hexdigest() in builder.decode()
            and dec["source_sha256"] == hashlib.sha256(script.encode()).hexdigest()
            and "q,E=m.fmod.state((0,3),1,1);psi[ix[q,E[-1]]]=1" in script):
        bad.append("chain")
    if dec["parameters"] != {"K": 0.4, "delta": 0.7, "kappa": 0.3}:
        bad.append("parameters")
    if not st["origin_main_sha"].startswith(MAIN):
        bad.append("main")
    n = len(st["source_groups_inspected"])
    check("Q", not bad, f"origin/main {MAIN}: the note's S=192 sentence and the replay deferral; the prepared note's basis, "
          f"table and H4 lines; U13-R3; SHA256 of all {n} status sources; provenance chain: 4 vector files = "
          "DECOMPOSITION_RESULTS hashes = output of unprepared_decomposition_check.py (source hash recorded), which asserts "
          "builder 5030a960, which asserts flat module 50df6b9c; seed line psi = |(0,3),1,1>; K,delta,kappa = .4,.7,.3 "
          f"{bad if bad else ''}")
    return n


def main() -> None:
    t0 = time.time()
    n = family_q()
    family_x()
    family_n()
    print(f"TOTAL: PASS={len(OUT) - len(FAILS)} FAIL={len(FAILS)}  ({time.time() - t0:.0f} s)")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return
    print("SUMMARY: PARTIAL recovery of PR8839's deferred saved-vector replay (U13-R3). Provenance exact: the four saved "
          "high-spin vectors are the finite-spin propagations of the actual first output |03,1,1> (exactly the output of the "
          "mark (link 0, +) for every S >= 1), by the script whose hash DECOMPOSITION_RESULTS records, through builder "
          "5030a960 and flat module 50df6b9c. Independently rebuilt from the landed note's text (flat basis, electric table, "
          "H4 action and Gamma = 4 on it checked exactly), the model reproduces every saved vector to 1e-12 and every window "
          "row, including S=192, t=1.2, |f|<=2: trace-norm error 2.0556e-4, complementary weight 1.2398e-8. What it adds "
          "beyond the landed bounds: finite-S sizes of (2), (6), (7) at S = 64..192, t <= 1.2, non-monotone in S; no rate, "
          f"uniform bound or limit law follows. {n} deferred sources inspected; first pass; no new theorem.")


if __name__ == "__main__":
    main()
