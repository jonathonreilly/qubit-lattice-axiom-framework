"""ba7 (BFT lane A, session 7): checks of BFT_A §31 (Lemma TD, Lemma IP, depth signal of U_H / D_N).

Matrix-free abelian chain of checks/ba5_y.py and helpers of checks/ba6_w0.py (read-only imports).
Criteria: checks/ba7_criteria.md (written before this file).  Usage: python3 ba7_s7.py PART   (PART in A K)
"""
import sys
import time
import traceback

import numpy as np

sys.path.insert(0, "/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/.claude/science/"
                   "toe-ruleset-20261021/agents/ym4d-proof/checks")
import ba5_y as b5  # noqa: E402
import ba6_w0 as b6  # noqa: E402

L = b5.L
T0 = time.time()
Chain, dT, dform, dot, axpy, mx, l1 = b5.Chain, b5.dT, b5.dform, b5.dot, b5.axpy, b5.mx, b5.l1
div1, qstr, cube_rand = b6.div1, b6.qstr, b6.cube_rand


def stamp():
    return f"({time.time() - T0:.0f} s, RSS {b5.rss():.0f} MB)"


def qstrT(u, s):
    """transpose of qstr: level-m 1-form -> level-l 1-form."""
    out = []
    for nu in range(4):
        up = u[nu]
        for ax in range(4):
            up = np.repeat(up, s, axis=ax)
        out.append(sum(np.roll(up, t, axis=nu) for t in range(s)) / s ** 4)
    return out


def bmean(Y, s):
    Sm = Y[0].shape[0] // s
    return [a.reshape(Sm, s, Sm, s, Sm, s, Sm, s).mean(axis=(1, 3, 5, 7)) for a in Y]


def gradl1(Y):
    return sum(float(np.sum(np.abs(b5.fwd(a, m)))) for a in Y for m in range(4))


def part_A():
    rng = np.random.default_rng(7)
    print("E1 (Lemma TD), k = 2, T = 2", flush=True)
    ch = Chain(2, 2); M0, M1 = ch.S[0], ch.S[1]
    S0p = cube_rand(rng, M0, 5, 2, 4); S1 = cube_rand(rng, M1, 3, 1, 4)
    Tp = axpy(1.0, b5.QTop(S1, M1), S0p)
    cc = b5.coulomb(Tp)
    S0 = axpy(-1.0, axpy(-1.0, cc, Tp), S0p)
    T0v = axpy(1.0, b5.QTop(S1, M1), S0)
    ea = float(np.max(np.abs(div1(T0v)))) / max(mx(S0), mx(S1))
    z1 = b5.coulomb(cube_rand(rng, M1, 3, 1, 4))
    b1 = axpy(1.0, z1, S1)
    c1 = axpy(-1.0, b1, S1)
    c0 = axpy(1.0, b5.QTop(b1, M1), S0)
    eb0 = float(np.max(np.abs(div1(c0)))) / mx(c0)
    eb1 = float(np.max(np.abs(div1(c1)))) / mx(c1)
    X, rX, iX = ch.solve(ch.rhs(cur={0: S0, 1: S1}))
    Z, rZ, iZ = ch.solve(ch.rhs(cur={0: c0, 1: c1}, resid={0: [-a for a in b1]}))
    fX, rrX = ch.outs(X); fZ, rrZ = ch.outs(Z)
    ec = mx(axpy(-1.0, fZ, fX)) / mx(fX)
    er = [mx(axpy(-1.0, rrZ[j], rrX[j])) / mx(rrX[j]) for j in range(2)]
    u1 = div1(b1); dS0 = div1(S0)
    ed = {}
    for o in (0, 1):
        samp = dS0[o::L, o::L, o::L, o::L]
        ed[o] = float(np.max(np.abs(u1 + samp))) / float(np.max(np.abs(dS0)))
    mask = np.ones_like(dS0, dtype=bool)
    oo = min(ed, key=ed.get)
    mask[oo::L, oo::L, oo::L, oo::L] = False
    off_root = float(np.max(np.abs(dS0[mask]))) / float(np.max(np.abs(dS0)))
    okd = min(ed.values()) <= 1e-10
    ok1 = ea <= 1e-10 and eb0 <= 1e-10 and eb1 <= 1e-10 and ec <= 1e-8 and max(er) <= 1e-8 and okd
    print(f"  (a) composite-co-closed: {ea:.1e}; (b) max|d*c_0|/max|c_0| = {eb0:.1e}, max|d*c_1|/max|c_1| = {eb1:.1e}",
          flush=True)
    print(f"  (c) outputs: f_0 {ec:.1e}, r_0 {er[0]:.1e}, r_1 {er[1]:.1e}; CG res {rX:.0e} ({iX} it) / {rZ:.0e} ({iZ} it)",
          flush=True)
    print(f"  (d) u_1 + ev(d*S_0): offset 0: {ed[0]:.1e}, offset 1: {ed[1]:.1e}; d*S_0 off the roots (offset {oo}): "
          f"{off_root:.1e} (informational)", flush=True)
    print(f"E1 {'PASS' if ok1 else 'FAIL'} {stamp()}", flush=True)
    del X, Z

    print("E2 (Lemma IP), level 0 of the (2, 2) torus, side 18", flush=True)
    M = 18; ok2 = True
    for s in (3, 9):
        v = [rng.standard_normal((M,) * 4) for _ in range(4)]
        u = [rng.standard_normal((M // s,) * 4) for _ in range(4)]
        lhs = dot(qstr(v, s), u); rhs_ = dot(v, qstrT(u, s))
        ea2 = abs(lhs - rhs_) / (abs(lhs) + 1)
        one = [np.ones((M // s,) * 4) for _ in range(4)]
        Is1 = [s ** 3 * a for a in qstrT(one, s)]
        eb2 = max(float(np.max(np.abs(a - 1.0))) for a in Is1)
        ok2 &= ea2 <= 1e-12 and eb2 <= 1e-12
        x = np.arange(M)
        g = np.meshgrid(x, x, x, x, indexing="ij")
        fields = {
            "random": [rng.standard_normal((M,) * 4) for _ in range(4)],
            "smooth": [np.cos(2 * np.pi * g[(i + 1) % 4] / M) + 0.5 * np.sin(2 * np.pi * (g[i] + 2 * g[(i + 2) % 4]) / M)
                       for i in range(4)],
            "step": [(g[0] < M // 2).astype(float) for _ in range(4)],
            "step-diag": [((g[0] + g[1]) % M < M // 2).astype(float) for _ in range(4)],
        }
        line = f"  s={s}: transpose {ea2:.1e}, |I_s 1 - 1| {eb2:.1e}; Poincare ratios Σ|Y - I_sM_sY|/(sΣ|∇Y|):"
        for name, Y in fields.items():
            IY = [s ** 3 * a for a in qstrT(bmean(Y, s), s)]
            num = l1(axpy(-1.0, IY, Y)); den = s * gradl1(Y)
            ratio = num / den
            ok2 &= ratio <= 12
            line += f" {name} {ratio:.3f}"
        print(line, flush=True)
    print(f"E2 {'PASS' if ok2 else 'FAIL'} {stamp()}", flush=True)


def part_K():
    print("E3 (depth signal)", flush=True)
    R = {}
    for (k, T) in [(1, 1), (2, 1), (2, 3), (3, 1)]:
        try:
            R[(k, T)] = b6.run_k(k, T, True)
        except Exception:
            print(f"  k={k} T={T}: ERROR", flush=True)
            traceback.print_exc(limit=3)
        print(f"  done k={k} T={T} {stamp()}", flush=True)

    def get(kt, key):
        return R[kt][key] if kt in R and key in R[kt] else None
    U = {kt: get(kt, "UH") for kt in [(1, 1), (2, 1), (2, 3), (3, 1)]}
    D = {kt: get(kt, "DN") for kt in [(1, 1), (2, 1), (2, 3), (3, 1)]}
    res = {}
    res["H3a"] = None if None in (U[(3, 1)], U[(2, 3)]) else U[(3, 1)] <= 2 * U[(2, 3)]
    res["H3b"] = (None if None in (U[(1, 1)], U[(2, 1)], U[(3, 1)])
                  else (U[(3, 1)] - U[(2, 1)]) <= (U[(2, 1)] - U[(1, 1)]) + 0.02 * U[(2, 1)])
    res["N3"] = (None if None in (D[(3, 1)], D[(2, 1)], D[(2, 3)])
                 else D[(3, 1)] <= 2 * max(D[(2, 1)], D[(2, 3)]))
    for name, v in res.items():
        print(f"{name} {'N/A' if v is None else ('PASS' if v else 'FAIL')}", flush=True)


if __name__ == "__main__":
    {"A": part_A, "K": part_K}[sys.argv[1]]()
