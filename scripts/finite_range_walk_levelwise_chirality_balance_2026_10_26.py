#!/usr/bin/env python3
"""Level-wise chirality balance for finite-range walks on Z^3.

Source note:
  docs/FINITE_RANGE_WALK_LEVELWISE_CHIRALITY_BALANCE_BOUNDED_THEOREM_NOTE_2026-10-26.md

Checks, with expected values never fed in (W3 always comes from the bulk integral, the
right-hand side from certified level decompositions and box-surface Chern numbers):

  0. sign and normalisation lemmas: the lattice Chern routine against a direct
     finite-difference integral; Ch(lower band) = sign det v at a Weyl node; the
     t-winding identity for exp(-2 pi i t P);
  1. the localization identity W3 = -sum_boxes Ch(P_<) on analytic infinite-range maps
     with W3 = -1 and +2 (n = 2) and on a coupled n = 3 map whose level sets are pockets;
  2. finite-range walks (n = 2 and n = 4): exact-grid W3 = 0, box sums zero at levels 0
     and pi, nodal chirality sums zero at clean levels;
  3. a finite-range witness whose level-0 Weyl nodes have net chirality -4: its level 0
     must also carry Fermi sheets, and sheet points are exhibited.

Certification: the level set is excluded from coarse cells by a Lipschitz bound
(rigorous up to floating-point rounding); Chern numbers use the Fukui-Hatsugai-Suzuki
lattice sum on box surfaces, whose mesh adequacy is evidenced by agreement at two
meshes, not proved.
"""
from __future__ import annotations

import os
import sys

for _var in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_var, "1")

import numpy as np
from scipy.linalg import expm

import finite_range_walk_levelwise_chirality_balance_2026_10_26_helpers as L

AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = (
    "docs/FINITE_RANGE_WALK_LEVELWISE_CHIRALITY_BALANCE_BOUNDED_THEOREM_NOTE_2026-10-26.md",
    "scripts/finite_range_walk_levelwise_chirality_balance_2026_10_26_helpers.py",
)

C = L.Checker()


# ----------------------------------------------------------------- 0. sign lemmas
def P_lower(v):
    def P(K):
        d = K @ v
        n = d / np.linalg.norm(d, axis=-1, keepdims=True)
        H = sum(n[..., j, None, None] * L.PAULI[j] for j in range(3))
        return 0.5 * (np.eye(2) - H)
    return P


def direct_chern(P, lo, hi, M=120):
    tot = 0.0
    for G in L.box_surface_points(lo, hi, M):
        Pg = P(G)
        du = (Pg[2:, 1:-1] - Pg[:-2, 1:-1]) / 2
        dv = (Pg[1:-1, 2:] - Pg[1:-1, :-2]) / 2
        Pc = Pg[1:-1, 1:-1]
        t = np.trace(Pc @ (du @ dv - dv @ du), axis1=-2, axis2=-1)
        tot += (1j / (2 * np.pi) * t.sum()).real
    return tot


def fhs_raw(P, lo, hi, M=30):
    tot = 0.0
    for G in L.box_surface_points(lo, hi, M):
        Pg = P(G)
        _, V = np.linalg.eigh(Pg)
        Q = V[..., :, -1]

        def lk(a, b):
            return np.sum(a.conj() * b, axis=-1)
        p = lk(Q[:-1, :-1], Q[1:, :-1]) * lk(Q[1:, :-1], Q[1:, 1:]) * lk(Q[1:, 1:], Q[:-1, 1:]) * lk(Q[:-1, 1:], Q[:-1, :-1])
        tot += np.angle(p).sum()
    return tot / (2 * np.pi)


def part0_sign_lemmas():
    print("== 0. sign and normalisation lemmas", flush=True)
    rng = np.random.default_rng(1)
    lo, hi = np.array([-1.0, -0.8, -1.2]), np.array([0.9, 1.1, 1.0])
    signs = []
    for trial in range(6):
        v = rng.normal(size=(3, 3))
        P = P_lower(v)
        dc = direct_chern(P, lo, hi)
        raw = fhs_raw(P, lo, hi)
        sd = np.sign(np.linalg.det(v))
        print(f"   v det sign {sd:+.0f}: direct Ch = {dc:+.4f}, raw lattice sum = {raw:+.6f}", flush=True)
        C.check(f"Weyl-node lemma: Ch(lower band) = sign det v by the direct integral (trial {trial})", abs(dc - sd) < 0.05)
        C.check(f"raw lattice Chern sum is an integer (trial {trial})", abs(raw - round(raw)) < 1e-9)
        signs.append(np.sign(raw) * np.sign(dc))
    C.check("lattice-to-analytic sign is the same in all trials", len(set(signs)) == 1)
    C.check(f"helper CH_SIGN ({L.CH_SIGN}) equals the calibrated sign ({signs[0]})", L.CH_SIGN == signs[0])
    for trial in range(3):
        v = rng.normal(size=(3, 3))
        P = P_lower(v)
        M, Nt = 60, 40
        tot = 0.0
        for G in L.box_surface_points(lo, hi, M):
            Pg = P(G)
            du = (Pg[2:, 1:-1] - Pg[:-2, 1:-1]) / 2
            dv = (Pg[1:-1, 2:] - Pg[1:-1, :-2]) / 2
            Pc = Pg[1:-1, 1:-1]
            for t in (np.arange(Nt) + 0.5) / Nt:
                z = np.exp(-2j * np.pi * t)
                gi = np.eye(2) + (1 / z - 1) * Pc
                Au = gi @ ((z - 1) * du)
                Av = gi @ ((z - 1) * dv)
                At = gi @ (-2j * np.pi * z * Pc)
                tr = 3 * np.trace(Au @ Av @ At - Au @ At @ Av, axis1=-2, axis2=-1)
                tot += tr.sum() / Nt
        val = tot / (24 * np.pi ** 2)
        ch = direct_chern(P, lo, hi, M=M)
        print(f"   t-winding trial {trial}: (1/24pi^2) int tr theta^3 = {val.real:+.4f}, Ch = {ch:+.4f}", flush=True)
        C.check(f"t-winding identity: winding of exp(-2 pi i t P) over surface x [0,1] equals Ch(P) (trial {trial})",
                abs(val - ch) < 0.05)


# ----------------------------------------------------------------- 1. analytic controls
def xvec(K, M):
    c, s = np.cos(K), np.sin(K)
    return np.concatenate([(M - c.sum(-1))[..., None], s], -1)


def VM_fun(M):
    def f(K):
        x = xvec(K, M)
        x = x / np.linalg.norm(x, axis=-1, keepdims=True)
        return x[..., 0, None, None] * np.eye(2) + 1j * sum(x[..., j + 1, None, None] * L.PAULI[j] for j in range(3))
    return f


def VM(M):
    N = 64
    k = 2 * np.pi * np.arange(N) / N
    K = np.stack(np.meshgrid(k, k, k, indexing="ij"), -1)
    m = np.linalg.norm(xvec(K, M), axis=-1).min() - 3 * np.pi / N   # |x| is 3-Lipschitz in sup norm
    assert m > 0
    # ||x/|x| - y/|y||| <= 2|x - y|/|x| and |x(k) - x(k')| <= 3 ||k - k'||_inf  =>  Lipschitz 6/m
    return L.Func(VM_fun(M), 2, 6.0 / m, f"V_{M}")


def coupled_func(blocks, eta, seed, name):
    rng = np.random.default_rng(seed)
    n = sum(b.n for b in blocks)
    Kh = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Kh = (Kh + Kh.conj().T) / 2
    Cc = expm(1j * eta * Kh)

    def f(K):
        out = np.zeros(K.shape[:-1] + (n, n), complex)
        o = 0
        for b in blocks:
            out[..., o:o + b.n, o:o + b.n] = b(K)
            o += b.n
        return Cc @ out
    return L.Func(f, n, max(b.L for b in blocks), name)


def const_block(E):
    return L.Func(lambda K: np.exp(-1j * E) * np.ones(K.shape[:-1] + (1, 1)), 1, 0.0, f"e^(-i{E})")


def part1_localization():
    print("== 1. localization identity on analytic maps with W3 != 0", flush=True)
    cases = [VM(2.0), VM(0.0), coupled_func([VM(2.0), const_block(2.0)], 0.15, 5, "n3: C(V_2 + e^{-2i})")]
    for W in cases:
        print(f"=== {W.name} (n={W.n}, Lipschitz L={W.L:.3f})", flush=True)
        wa = L.w3_grid(W, 40, 0.3)
        wb = L.w3_grid(W, 56, 0.17)
        w3 = int(round(wb.real))
        print(f"   bulk W3 integral: N=40 {wa.real:+.8f}, N=56 {wb.real:+.8f}", flush=True)
        C.check(f"{W.name}: bulk W3 integral converged to the integer {w3:+d}",
                abs(wb.real - w3) < 1e-3 and abs(wa.real - wb.real) < 1e-3 and w3 != 0)
        for eps in (0.0, np.pi):
            r = L.analyze_level(W, eps, N0=32, depth=4, M=24)
            print(f"   level {eps:.4f}: uncertified cells {r['nbad']}, components {r['ncomp']},"
                  f" decomposed={r['clean']} {r['reason']}", flush=True)
            if not r["clean"]:
                C.check(f"{W.name} eps={eps:.3f}: level decomposed into isolated boxes", False)
                continue
            C.check(f"{W.name} eps={eps:.3f}: box Chern numbers integer and mesh-stable",
                    all(abs(b["ch"] - round(b["ch"])) < 1e-9 and abs(b["ch"] - b["ch2"]) < 1e-9 for b in r["boxes"]))
            s = int(round(sum(b["ch"] for b in r["boxes"])))
            C.check(f"{W.name} eps={eps:.3f}: W3 = -sum_boxes Ch(P_<) ({w3:+d} = {-s:+d})", -s == w3)
            nod = [q for b in r["boxes"] for q in b["nodes"]]
            npock = sum(b["pocket"] for b in r["boxes"])
            print(f"   boxes {len(r['boxes'])}, pocket boxes {npock}, nodes at the level {len(nod)}", flush=True)
            if npock == 0 and nod and all(q["gap_others"] > 1e-3 for q in nod) and all(b["nodes"] for b in r["boxes"]):
                C.check(f"{W.name} eps={eps:.3f}: per box Ch(P_<) = sum of nodal chiralities",
                        all(round(b["ch"]) == sum(q["chi"] for q in b["nodes"]) for b in r["boxes"]))


# ----------------------------------------------------------------- 2. finite-range walks
def part2_finite_range():
    print("== 2. finite-range walks: box sums and clean-level chirality sums", flush=True)
    I2 = np.eye(2)
    SZs = np.kron(I2, L.SZ)                         # 1 (x) sigma_3, commutes with the C4z coin 1 (x) D(R_z)
    gold = L.two_qubit_walk(L.B_GOLD, "g")
    cases = [
        (L.Q_product((1, 1, 1)), False),
        (L.dariano_perinotti_weyl(), False),
        (L.conj_coin(gold, SZs, 0.3, "two-qubit gold walk with axial coin exp(0.15i 1(x)sigma_3)"), True),
    ]
    Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    Dz = np.kron(I2, expm(-0.25j * np.pi * L.SZ))
    Kt = np.random.default_rng(3).uniform(0, 2 * np.pi, (200, 3))
    for W, c4z in cases:
        print(f"=== {W.name} (n={W.n}, range {W.range}, #hops {len(W.c)}, L={W.L:.3f})", flush=True)
        Ut = W(Kt)
        un = np.abs(Ut @ np.conj(np.swapaxes(Ut, -1, -2)) - np.eye(W.n)).max()
        C.check(f"{W.name}: unitary at 200 random k", un < 1e-12, "numerical")
        if c4z:
            cov = np.abs(W(Kt @ Rz.T) - Dz @ Ut @ Dz.conj().T).max()
            C.check(f"{W.name}: C4z covariance U(R k) = D U(k) D^dag", cov < 1e-12, "numerical")
        r = W.range
        w1 = L.w3_grid(W, 6 * r + 2)
        w2 = L.w3_grid(W, 6 * r + 5, 0.37)
        C.check(f"{W.name}: exact-grid W3 = 0 ({w1.real:+.1e}, {w2.real:+.1e})",
                abs(w1) < 1e-8 and abs(w2) < 1e-8, "exact-grid certificate")
        det = np.linalg.det(Ut)
        print(f"   det U spread over samples {np.abs(det - det[0]).max():.1e}", flush=True)
        for eps in (0.0, np.pi):
            res = L.analyze_level(W, eps, N0=32, depth=4, M=24)
            boxes = res["boxes"]
            print(f"   level {eps:.4f}: uncertified cells {res['nbad']}, components {res['ncomp']},"
                  f" decomposed={res['clean']} {res['reason']}", flush=True)
            if not res["clean"]:
                C.check(f"{W.name} eps={eps:.3f}: level decomposed into isolated boxes", False)
                continue
            s = sum(int(round(b["ch"])) for b in boxes)
            C.check(f"{W.name} eps={eps:.3f}: box Chern numbers integer and mesh-stable",
                    all(abs(b["ch"] - round(b["ch"])) < 1e-9 and abs(b["ch"] - b["ch2"]) < 1e-9 for b in boxes))
            C.check(f"{W.name} eps={eps:.3f}: sum_boxes Ch(P_<) = -W3 = 0 (got {s:+d})", s == 0)
            npock = sum(b["pocket"] for b in boxes)
            nod = [q for b in boxes for q in b["nodes"]]
            weyl = [q for q in nod if q["gap_others"] > 1e-3]
            multi = [q for q in nod if q["gap_others"] <= 1e-3]
            for q in weyl:
                print(f"     Weyl node k={np.round(q['k'], 5)} chi={q['chi']:+d}"
                      f" |v| sing. vals={np.round(np.linalg.svd(q['v'], compute_uv=False), 4)}", flush=True)
            if npock == 0 and not multi:
                chis = [q["chi"] for q in weyl]
                C.check(f"{W.name} eps={eps:.3f}: clean level with only Weyl nodes, sum chi = 0"
                        f" ({len(chis)} nodes, sum {sum(chis):+d})", sum(chis) == 0 and len(chis) > 0)
                C.check(f"{W.name} eps={eps:.3f}: per box Ch = sum chi in box",
                        all(round(b["ch"]) == sum(q["chi"] for q in b["nodes"]) for b in boxes))


# ----------------------------------------------------------------- 3. sharpness witness
def small_box_certificate(W, p, d, n_face=60, n_vol=10):
    """(a) no eigenvalue 1 on the surface of [p-d, p+d]^3 (Lipschitz cells); (b) a quasienergy
    phi absent on the whole cube."""
    h = 2 * d / n_face
    cs = (np.arange(n_face) + 0.5) * h - d
    pts = []
    for a in range(3):
        b_, c_ = (a + 1) % 3, (a + 2) % 3
        for side in (-d, d):
            G = np.zeros((n_face, n_face, 3))
            G[..., a] = side
            G[..., b_] = cs[:, None]
            G[..., c_] = cs[None, :]
            pts.append(G.reshape(-1, 3))
    pts = np.concatenate(pts) + p
    if not np.all(L.gapfun(W(pts), 0.0) > W.L * h / 2 * (1 + 1e-9)):
        return False, None
    hv = 2 * d / n_vol
    cv = (np.arange(n_vol) + 0.5) * hv - d
    V = np.stack(np.meshgrid(cv, cv, cv, indexing="ij"), -1).reshape(-1, 3) + p
    for phi in np.linspace(-np.pi, np.pi, 73)[:-1]:
        if abs(np.angle(np.exp(1j * phi))) < 0.3:
            continue
        if np.all(L.gapfun(W(V), phi) > W.L * hv / 2 * (1 + 1e-9)):
            return True, np.mod(phi, 2 * np.pi)
    return False, None


def part3_witness():
    print("== 3. sharpness witness: unbalanced level-0 nodes force Fermi sheets", flush=True)
    Q = L.Q_product((2, 1, 1))
    T2 = L.lmul(L.Laurent({(1, 0, 0): np.eye(2)}), Q)
    T2.name = "T2 = e^{i k_x} Q(2,1,1)"
    qnodes = []
    for lev in (0.0, np.pi):
        rq = L.analyze_level(Q, lev, N0=32, depth=4, M=16, verbose=False)
        ok = rq["clean"] and not any(b["pocket"] for b in rq["boxes"])
        for b in rq["boxes"]:
            ok = ok and len(b["nodes"]) == 1 and round(b["ch"]) == b["nodes"][0]["chi"]
            if b["nodes"]:
                qnodes.append((b["nodes"][0]["k"], b["nodes"][0]["chi"], lev))
        C.check(f"Q(2,1,1) level {lev:.3f}: clean, each node alone in a certified box with Ch = chi", ok)
    C.check("Q(2,1,1) inventory: 16 Weyl nodes at level 0 and 16 at level pi", len(qnodes) == 32)
    W = T2
    r = W.range
    w1 = L.w3_grid(W, 6 * r + 2)
    w2 = L.w3_grid(W, 6 * r + 5, 0.37)
    C.check(f"{W.name}: exact-grid W3 = 0 ({w1.real:+.1e}, {w2.real:+.1e})",
            abs(w1) < 1e-8 and abs(w2) < 1e-8, "exact-grid certificate")
    Kt = np.random.default_rng(4).uniform(0, 2 * np.pi, (300, 3))
    det = np.linalg.det(W(Kt))
    C.check(f"{W.name}: det U = exp(2 i k_x) is not constant", np.abs(det - det[0]).max() > 0.5)
    nod = []
    for p, chiQ, lev in qnodes:
        # degeneracies of T2 are those of Q; keep the ones where e^{i p_x} Q(p) has eigenvalue 1
        if abs(np.angle(np.exp(1j * p[0]) * (1 if lev == 0 else -1))) > 1e-9:
            continue
        chi, v, tilt, _ = L.weyl_chirality(W, 0.0, p)
        okb, phi = small_box_certificate(W, p, 0.1)
        ch = L.chern_box(W, p - 0.1, p + 0.1, 0.0, phi, 24)[0] if okb else np.nan
        tv = np.linalg.norm(np.linalg.solve(v, tilt))
        nod.append(dict(k=p, chi=chi, ch=ch, ok=okb, tv=tv))
        print(f"   level-0 Weyl node k={np.round(p, 6)} chi={chi:+d} |v^-1 tilt|={tv:.3f} box certified={okb}"
              f" Ch={ch:+.6f}", flush=True)
    C.check(f"{W.name}: every level-0 node box is certified level-free on its surface and cut-free inside",
            len(nod) > 0 and all(q["ok"] for q in nod))
    C.check(f"{W.name}: all level-0 nodes are type I (|v^-1 tilt| < 1)", all(q["tv"] < 1 for q in nod))
    C.check(f"{W.name}: per node box Ch(P_<) = chi", all(abs(q["ch"] - q["chi"]) < 1e-9 for q in nod))
    s = sum(q["chi"] for q in nod)
    print(f"   net chirality of the {len(nod)} isolated level-0 Weyl nodes: {s:+d}; with W3 = 0 the level-0"
          f" Fermi sheets must carry the compensating flux", flush=True)
    C.check(f"{W.name}: net level-0 nodal chirality is nonzero ({s:+d})", s != 0)
    pts = 0
    rng = np.random.default_rng(9)
    for _ in range(40):
        kk, sv = L.find_min(W, 0.0, rng.uniform(0, 2 * np.pi, 3))
        if sv < 1e-9:
            lam = np.linalg.eigvals(W(kk[None])[0])
            if np.sort(np.abs(lam - 1))[1] > 1e-2:
                pts += 1
    C.check(f"{W.name}: non-degenerate eigenvalue-1 points (sheet points) exist at level 0 ({pts}/40 starts)", pts > 0)


def main():
    print("Imported: the three-winding vanishing theorem (W3 = 0 for finite-range walks).")
    part0_sign_lemmas()
    part1_localization()
    part2_finite_range()
    part3_witness()
    C.total()
    return 0 if C.f == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
