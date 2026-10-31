"""bb1: level-1 derivative decay at the trivial background, d = 4, L = 3 (BFT_B.md §1.5).
Criteria: checks/bb1_criteria.md (written first). Usage: python3 bb1_decay.py A|B."""
import os
import sys

import numpy as np
import scipy.fft as sfft

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c37_kcurv as K37  # noqa: E402  (Fib, d1c, grid, tdist_inf, say)

say = K37.say


def build():
    F = K37.Fib({"a": (0.0, 1.0), "b": (1.0, 1.0)})
    F.As["b"] = F.As["b"] - F.As["a"]
    del F.op
    return F


def hats(F, T, kap=1.0, check=False, cdt=np.complex64):
    """a_S, a_B (T^4, 324, 4), H_1 (T^4, 4, 4); optional fibre-level gauge-equivalence residuals."""
    shp = (T,) * 4
    aS = np.zeros(shp + (F.nloc, 4), cdt); aB = np.zeros(shp + (F.nloc, 4), cdt); H1 = np.zeros(shp + (4, 4), np.complex128)
    done = np.zeros(shp, bool)
    rd = rq = amax = 0.0
    for idx in K37.grid(T):
        if done[idx]:
            continue
        Kv = 2 * np.pi * np.array(idx) / T
        Ok = F.Ot(Kv, kap); Dk = F.d(Kv); Qk = F.Q(Kv)
        rhs = np.hstack([Dk.conj().T @ F.iota, Qk.conj().T])
        X = np.linalg.solve(Ok, rhs)
        Cg = X - F.onemPi @ rhs
        x = -Cg[:, :6]
        d1 = K37.d1c(Kv)
        vS = kap * Cg[:, 6:]
        vB = F.J + x @ d1
        vH = -kap * (Qk @ x) @ d1
        if check:
            amax = max(amax, float(np.abs(vB).max()))
            rd = max(rd, float(np.abs(Dk @ (vS - vB)).max())); rq = max(rq, float(np.abs(Qk @ (vS - vB)).max()))
        mi = tuple((-np.array(idx)) % T)
        for arr, v in ((aS, vS), (aB, vB), (H1, vH)):
            arr[idx] = v; arr[mi] = v.conj()
        done[idx] = True; done[mi] = True
    return aS, aB, H1, (rd, rq, amax)


def stats(hat, mus=()):
    """max |entry| by coarse l^inf shell, row/col l1 sums, weighted row sums (coarse l^1 distance), max |imag|."""
    T = hat.shape[0]
    dinf = K37.tdist_inf(T)
    r = np.arange(T); r = np.minimum(r, T - r)
    d1 = sum(np.meshgrid(r, r, r, r, indexing="ij"))
    prof = np.zeros(T // 2 + 1); rs = np.zeros(hat.shape[-2]); cs = np.zeros(hat.shape[-1]); im = 0.0
    wr = {mu: np.zeros(hat.shape[-2]) for mu in mus}
    for c in range(hat.shape[-1]):
        kc = sfft.fftn(np.ascontiguousarray(hat[..., c]).astype(np.complex128), axes=(0, 1, 2, 3), workers=1) / T ** 4
        im = max(im, float(np.abs(kc.imag).max()))
        a = np.abs(kc.real); del kc
        for s in range(T // 2 + 1):
            prof[s] = max(prof[s], float(a[dinf == s].max()))
        rs += a.sum(axis=(0, 1, 2, 3)); cs[c] = a.sum()
        for mu in mus:
            wr[mu] += (a * np.exp(mu * d1)[..., None]).sum(axis=(0, 1, 2, 3))
        del a
    return prof, rs.max(), cs.max(), {mu: v.max() for mu, v in wr.items()}, im


def rates(prof):
    return [float(np.log(prof[s] / prof[s + 1])) for s in range(len(prof) - 1)]


def part_A():
    F = build(); say("A: fibres built")
    ok = {}
    P = {}
    for T in (8, 10):
        aS, aB, H1, (rd, rq, amax) = hats(F, T, check=(T == 8), cdt=np.complex128 if T == 8 else np.complex64)
        say(f"A T={T}: fibres solved")
        if T == 8:
            ok["A1"] = rd <= 1e-6 * amax and rq <= 1e-6 * amax
            say(f"A1: max|d(a_S - a_B)| = {rd:.2e}, max|Q(a_S - a_B)| = {rq:.2e}, max|a_B| = {amax:.4f}")
        out = {}
        for lab, h in (("a_S", aS), ("a_B", aB), ("H_1", H1)):
            out[lab] = stats(h, mus=(0.5, 1.0) if T == 10 and lab == "a_S" else ())
        del aS, aB, H1
        for lab, (prof, rmax, cmax, wr, im) in out.items():
            say(f"A T={T} {lab}: P(s) = " + ", ".join(f"{v:.3e}" for v in prof) + "; r_s = "
                + ", ".join(f"{v:.3f}" for v in rates(prof)) + f"; max row l1 {rmax:.6f}, max col l1 {cmax:.6f}"
                + "".join(f"; N_{mu} = {v:.4f}" for mu, v in wr.items()) + f"; max imag {im:.1e}")
        if T == 8:
            zr, zc = out["a_S"][1], out["a_S"][2]
            ok["A2"] = abs(zr - 2.848907) <= 1e-4 * 2.848907 and abs(zc - 156.078934) <= 1e-4 * 156.078934
            say(f"A2: Z_row = {zr:.6f} (c37: 2.848907), Z_col = {zc:.6f} (c37: 156.078934)")
        P[T] = {lab: v[0] for lab, v in out.items()}
    a3 = True
    for lab in ("a_S", "a_B", "H_1"):
        rt = rates(P[10][lab])
        stab = max(abs(P[8][lab][s] - P[10][lab][s]) / P[10][lab][s] for s in range(4))
        a3 &= rt[2] >= 0.5 and rt[3] >= 0.5 and stab <= 0.1
        say(f"A3 {lab}: r_2 = {rt[2]:.3f}, r_3 = {rt[3]:.3f}; max rel. T=8/10 difference at s <= 3: {stab:.2e}")
    ok["A3"] = a3
    print(f"A: {'PASS' if all(ok.values()) else 'FAIL'} {ok}", flush=True)


def part_B():
    F = build(); say("B: fibres built")
    for kap in (0.25, 4.0):
        aS, aB, H1, _ = hats(F, 8, kap=kap)
        for lab, h in (("a_B", aB), ("H_1", H1)):
            prof = stats(h)[0]
            say(f"B kappa={kap} {lab}: P(s) = " + ", ".join(f"{v:.3e}" for v in prof) + "; r_s = "
                + ", ".join(f"{v:.3f}" for v in rates(prof)))
        del aS, aB, H1
    print("B: informational", flush=True)


if __name__ == "__main__":
    {"A": part_A, "B": part_B}[sys.argv[1]]()
