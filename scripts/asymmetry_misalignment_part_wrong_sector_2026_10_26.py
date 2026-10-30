#!/usr/bin/env python3
"""sol_E v3: couplings the charge principle still allows. Criteria: sol_E_v3_criteria_pre_run.txt (frozen before
the first run). Uses the v2 model definitions (sol_E_charged_orders_v2.py). Deterministic, numpy only."""
import io, contextlib, itertools, time, numpy as np
T00 = time.time()
src = __import__('pathlib').Path(__file__).with_name('asymmetry_misalignment_part_charged_orders_2026_10_26.py').read_text().split("PRINC = ['uu_onsite'")[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
NP[0] = NP[1] = 0
# W1
check("W1", q(('phi_u*', 'Q', 'D')) == 0 and q(('phi_d*', 'Q', 'U')) == 0,
      "wrong-sector Yukawas phi_u^* Q D and phi_d^* Q U are U(1)_H-neutral (allowed by the principle, like hypercharge)")
# W2 / W3
sl = Slab(48); rng = np.random.default_rng(2026102601); rng2 = np.random.default_rng(2026102602); rng3 = np.random.default_rng(2026102603)
DR = [add_vertex(draw(rng), rng2) for _ in range(10)]
def add_wrong(dr, r):
    dr['Wu'] = {'0': law_g(r), **{k: law_g(r) for k in VB}}; dr['Wd'] = {'0': law_g(r), **{k: law_g(r) for k in VB}}; return dr
DR = [add_wrong(dr, rng3) for dr in DR]
def yuk(sl, ph, w, V):
    return np.array([[np.sum(ph[xor(XN[a], XN[b])] * w * pair_scalar(sl.Z[a], sl.Z[b], Gv(V, XN[a], XN[b]))) for b in FAM] for a in FAM])
def parts(sl, dr, lu, ld):
    wu, wd = layer_w(lu, sl.Ls), layer_w(ld, sl.Ls); phu, phd = cell_ft(dr['pu']), cell_ft(dr['pd'])
    cj = lambda ph: {K: np.conj(v) for K, v in ph.items()}
    return yuk(sl, phu, wu, dr['Vu']), yuk(sl, phd, wd, dr['Vd']), yuk(sl, cj(phd), wd, dr['Wu']), yuk(sl, cj(phu), wu, dr['Wd'])
cw = {}
for D in (0, 4):
    for order in ('a', 'b'):
        lu, ld = (1, 1 + D) if order == 'a' else (1 + D, 1); v = []
        for dr in DR:
            Yu, Yd, Yuw, Ydw = parts(sl, dr, lu, ld)
            v.append((abs(-np.imag(np.trace(np.linalg.solve(Yu, Yuw))) - np.imag(np.trace(np.linalg.solve(Yd, Ydw)))),
                      abs(np.imag(np.trace(np.linalg.solve(Yd, Ydw)))), abs(np.imag(np.trace(np.linalg.solve(Yu, Yuw))))))
        cw[order, D] = np.median(np.array(v), axis=0)
print("  c_w = |d theta_bar_tree/d kappa_w| (median; total, phi_u^* in down vertex, phi_d^* in up vertex):")
for k, v in cw.items(): print(f"    ordering {k[0]} Delta {k[1]}: {v[0]:.2e}  {v[1]:.2e}  {v[2]:.2e}")
check("W2", min(v[0] for v in cw.values()) > 1e-2, f"wrong-sector Yukawas leak at dimension 4: min median c_w = {min(v[0] for v in cw.values()):.2e} "
      f"-> theta_bar < 1e-10 needs kappa_w < {1e-10 / min(v[0] for v in cw.values()):.0e}")
rA, rA2 = np.random.default_rng(5), np.random.default_rng(6); mx = 0
for _ in range(6):
    dr = add_wrong(add_vertex(draw(rA, aligned=True), rA2), rA2)
    for D in (0, 3, 9):
        Yu, Yd, Yuw, Ydw = parts(sl, dr, 1, 1 + D); k = 1e-3
        mx = max(mx, abs(np.sin(wrap(-np.angle(np.linalg.det(Yu + k * Yuw)) - np.angle(np.linalg.det(Yd + k * Ydw))))))
check("W3", mx < 1e-12, f"aligned orders, wrong-sector terms at kappa_w = 1e-3: max |sin theta_bar_tree| = {mx:.1e}")
# S1 / S2 / S3: which symmetries can forbid the wrong-sector Yukawas?
ok1 = True
for qQ, qU, qD in itertools.product(range(-6, 7), repeat=3):
    qu, qd = -(qQ + qU), -(qQ + qD)
    forb = (qQ + qD - qu != 0) and (qQ + qU - qd != 0); anom = 3 * (2 * qQ + qU + qD) != 0
    ok1 &= (forb == anom)
check("S1", ok1, "U(1): both wrong-sector Yukawas forbidden <=> QCD anomaly 3(2qQ+qU+qD) != 0 (all 13^3 charge choices); "
      "a separating U(1) is a PQ symmetry")
ok2 = True; ok3 = True; info = []
for N in range(2, 13):
    sep_free = []
    for qQ, qU, qD in itertools.product(range(N), repeat=3):
        x = (2 * qQ + qU + qD) % N
        if x != 0 and (3 * x) % N == 0: sep_free.append((qQ, qU, qD))
    ok2 &= (len(sep_free) > 0) == (N % 3 == 0)
    for qQ, qU, qD in sep_free:
        qu, qd = -(qQ + qU), -(qQ + qD)
        for a, b, c, d in itertools.product(range(5), repeat=4):
            if a + b + c + d > 4 or a - b - c + d != 0 or (qu * (a - b) + qd * (c - d)) % N != 0: continue
            if (a - b) + (c - d) != 0: ok3 = False
    if N == 2:                           # computed: type-II Z_2 (D odd -> phi_d odd), the textbook natural-flavour-conservation choice
        qQ, qU, qD = 0, 0, 1; x = (2 * qQ + qU + qD) % 2; qu, qd = -(qQ + qU) % 2, -(qQ + qD) % 2
        l5 = (2 * qu + 2 * qd) % 2 == 0; an = (3 * x) % 2 != 0
        info.append(f"Z_2 type II (D, phi_d odd): wrong-sector forbidden {x != 0}, (phi_u phi_d)^2 allowed {l5} (no accidental PQ), "
                    f"QCD-anomalous {an} (3 odd colour triplets)")
check("S2", ok2, "Z_N, N = 2..12: a QCD-anomaly-free Z_N forbidding both wrong-sector Yukawas exists <=> 3 | N")
check("S3", ok3, "every such Z_N leaves only PQ-invariant renormalisable order potentials (m12^2 phi_u phi_d, lambda5 (phi_u phi_d)^2, "
      "lambda6,7 forbidden) -> accidental PQ, an electroweak-scale (Weinberg-Wilczek-type) axion; " + info[0])
# P1: order-potential cross-talk, first-order source on the real down order
def src_B1(pu, pd):     # V = sum_{c,e} [phi_u^*(c) phi_u(c+e) phi_d^*(c+e) phi_d(c) + c.c.];  s(s) = dV/d phi_d^*(s)
    s = {}
    for x in BITS:
        s[x] = sum(np.conj(pu[xor(x, e)]) * pu[x] * pd[xor(x, e)] + pu[x] * np.conj(pu[xor(x, e)]) * pd[xor(x, e)] for e in [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    return np.array([s[x] for x in BITS])
def src_B3(pu, pd):     # V = sum [phi_u^*(c) phi_u(c+e) phi_d^*(c) phi_d(c+e) + c.c.]
    s = {}
    for x in BITS:
        s[x] = sum(np.conj(pu[x]) * pu[xor(x, e)] * pd[xor(x, e)] + pu[xor(x, e)] * np.conj(pu[x]) * pd[xor(x, e)] for e in [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    return np.array([s[x] for x in BITS])
def src_on(pu, pd): return np.array([abs(pu[x]) ** 2 * pd[x] for x in BITS])
def todd(s, pd):
    g = np.array([pd[x] for x in BITS]).real; im = s.imag - (g @ s.imag) / (g @ g) * g
    return np.linalg.norm(im) / np.linalg.norm(s)
r1 = np.median([todd(src_B1(dr['pu'], dr['pd']), dr['pd']) for dr in DR]); r3 = np.median([todd(src_B3(dr['pu'], dr['pd']), dr['pd']) for dr in DR])
r0 = max(np.linalg.norm(src_on(dr['pu'], dr['pd']).imag) / np.linalg.norm(src_on(dr['pu'], dr['pd'])) for dr in DR)
check("P1", r1 > 1e-2 and r0 < 1e-14, f"order potential: PQ- and U(1)_H-invariant bond quartic sources a T-odd down-order component, "
      f"median |Im s_perp|/|s| = {r1:.2f} (variant B3: {r3:.2f}); on-site |phi_u|^2|phi_d|^2: {r0:.1e} (vacuum response not computed)")
print(f"time {time.time() - T00:.1f} s")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
