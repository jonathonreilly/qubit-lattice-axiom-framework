#!/usr/bin/env python3
"""Independent bounded checks for SIGN-1.

Modes:
  algebra  Reconstruct theta=230 from the saved feasible point on an
           independent sample, exhaust all C(64,4) components in batches,
           check the exact theta=270 Fierz identity, symmetries, and the
           filtered lower-grade remainder.
  weights  Generate a few weak/strong 4-site auxiliary-field weights in the
           128-dimensional number-conserving d frame, using the corrected
           filtered remainder and a QR-stabilised determinant.

No Fock-space matrix is constructed.  The largest one-particle matrix is
256x256 (the 4-site Majorana matrix); exponentials are only 128x128.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import itertools
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")
os.environ.setdefault("MKL_NUM_THREADS", "2")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "2")

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(HERE, "scripts")
sys.path.insert(0, SCRIPTS)

# Suppress the worker module's import-time report.  We reuse only its explicit
# Clifford/channel definitions; all constraints, component enumeration,
# lower-grade algebra, and weight evaluation below are independent.
with contextlib.redirect_stdout(io.StringIO()):
    import kramers_fams as kf


def rss_mib() -> float:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes; Linux reports KiB.
    return raw / (2**20) if sys.platform == "darwin" else raw / 1024


def alt(x: np.ndarray, y: np.ndarray, q: np.ndarray) -> np.ndarray:
    i, j, k, l = q.T
    return (
        x[i, j] * y[k, l]
        - x[i, k] * y[j, l]
        + x[i, l] * y[j, k]
        + y[i, j] * x[k, l]
        - y[i, k] * x[j, l]
        + y[i, l] * x[j, k]
    )


SINGLES = list(kf.singles)
DOUBLED = list(kf.doubled)


def sol_vector(sol: dict) -> np.ndarray:
    out = [sol[n] for n in SINGLES]
    for d in DOUBLED:
        out.extend((sol[d][0, 0], sol[d][1, 1], sol[d][0, 1]))
    return np.asarray(out, dtype=float)


def vector_sol(v: np.ndarray) -> dict:
    out = {n: float(v[i]) for i, n in enumerate(SINGLES)}
    p = len(SINGLES)
    for d in DOUBLED:
        a, c, b = v[p : p + 3]
        out[d] = np.array([[a, b], [b, c]])
        p += 3
    return out


def design(q: np.ndarray) -> np.ndarray:
    """Columns whose coefficients give the physical quartic, in worker units."""
    cols = []
    for n in SINGLES:
        cols.append(sum((alt(a, a, q) for a in kf.famo[n]), np.zeros(len(q))))
    for d in DOUBLED:
        ss = kf.famo[d + ":s"]
        cc = kf.famo[d + ":c"]
        cols.append(sum((alt(a, a, q) for a in ss), np.zeros(len(q))))
        cols.append(sum((alt(a, a, q) for a in cc), np.zeros(len(q))))
        cols.append(2 * sum((alt(a, b, q) for a, b in zip(ss, cc)), np.zeros(len(q))))
    return -0.25 * np.asarray(cols).T


KB = kf.vertex_B()


def target(q: np.ndarray, theta: float) -> np.ndarray:
    q1 = sum((alt(-x.conj(), x, q) for x in KB), np.zeros(len(q), complex)).real
    q2 = sum((2 * alt(x, x, q).real for x in KB), np.zeros(len(q)))
    r = np.deg2rad(theta)
    return np.cos(r) * q1 + np.sin(r) * q2


def independent_theta230() -> tuple[np.ndarray, dict]:
    rng = np.random.default_rng(314159)
    q = np.array(
        sorted({tuple(sorted(rng.choice(64, 4, replace=False))) for _ in range(7000)})[:5000],
        dtype=np.int16,
    )
    m = design(q)
    c = target(q, 230.0)
    saved = np.load(os.path.join(SCRIPTS, "kramers_solutions.npy"), allow_pickle=True).item()["th230"]
    g0 = sol_vector(saved)
    dg, *_ = np.linalg.lstsq(m, c - m @ g0, rcond=1e-12)
    g = g0 + dg
    sol = vector_sol(g)
    sv = np.linalg.svd(m, compute_uv=False)
    return g, {
        "sol": sol,
        "sample_max_rel": float(np.max(np.abs(m @ g - c)) / np.max(np.abs(c))),
        "rank": int(np.sum(sv > 1e-10 * sv[0])),
        "margin": sign_margin(sol),
        "correction_inf": float(np.max(np.abs(dg))),
    }


def sign_margin(sol: dict) -> float:
    vals = []
    for n in SINGLES:
        vals.append(-sol[n] if kf.parity(n) == "even" else sol[n])
    for d in DOUBLED:
        ev = np.linalg.eigvalsh(sol[d])
        vals.extend((-ev if kf.parity(d) == "even" else ev).tolist())
    return float(min(vals))


def batches_of_quads(batch: int = 8192):
    it = itertools.combinations(range(64), 4)
    while True:
        vals = list(itertools.islice(it, batch))
        if not vals:
            break
        yield np.asarray(vals, dtype=np.int16)


def exhaustive_residual(g230: np.ndarray) -> tuple[float, float, int]:
    # theta=270 exact Fierz: Re coefficients and the opposite Im coefficients.
    names270 = [
        ("sing", "8v", -34.0),
        ("trip", "8v", +2.0),
        ("sing", "56v", -2.0),
        ("trip", "56v", +2.0),
    ]
    worst230 = 0.0
    worst270 = 0.0
    scale230 = 0.0
    scale270 = 0.0
    count = 0
    for q in batches_of_quads():
        c230 = target(q, 230.0)
        r230 = design(q) @ g230 - c230
        q2 = target(q, 270.0)  # cos(270) is numerical zero; harmless below.
        rhs270 = np.zeros(len(q))
        for spin, rep, coeff in names270:
            re = kf.famo[f"pair:{spin}:{rep}:Re"]
            im = kf.famo[f"pair:{spin}:{rep}:Im"]
            are = sum((alt(a, a, q) for a in re), np.zeros(len(q)))
            aim = sum((alt(a, a, q) for a in im), np.zeros(len(q)))
            rhs270 += -0.25 * coeff * (are - aim)
        worst230 = max(worst230, float(np.max(np.abs(r230))))
        worst270 = max(worst270, float(np.max(np.abs(rhs270 - q2))))
        scale230 = max(scale230, float(np.max(np.abs(c230))))
        scale270 = max(scale270, float(np.max(np.abs(q2))))
        count += len(q)
    return worst230 / scale230, worst270 / scale270, count


def channel_list(sol: dict) -> list[tuple[float, np.ndarray]]:
    return kf.channels(sol)


def original_lower_grades(theta: float) -> tuple[np.ndarray, float]:
    """K_R and scalar C in Q = Q_4 + gamma^T K_R gamma + C."""
    r = np.deg2rad(theta)
    l1, l2 = np.cos(r), np.sin(r)
    kr = np.zeros((64, 64), complex)
    c = 0.0 + 0.0j
    for b in KB:
        bd = -b.conj()
        kr += 2 * l1 * (bd @ b - b @ bd)
        c += 2 * l1 * np.trace(bd @ b)
        c += 2 * l2 * (np.trace(b @ b) + np.trace(bd @ bd))
    return kr, float(np.real_if_close(c))


def decomposed_scalar(sol: dict) -> float:
    # For O(a)=(i/2) gamma^T a gamma, scalar(O^2)=-tr(a^2)/2.
    return float(sum(c * (-0.5 * np.trace(a @ a)) for c, a in channel_list(sol)))


def symmetry_and_filter(sol230: dict) -> dict:
    eye = np.eye(64)
    pair = {
        "T1_square": float(np.max(np.abs(kf.O1 @ kf.O1 + eye))),
        "T2_square": float(np.max(np.abs(kf.O2 @ kf.O2 + eye))),
        "anticomm": float(np.max(np.abs(kf.O1 @ kf.O2 + kf.O2 @ kf.O1))),
    }
    ch = channel_list(sol230)
    bad_u = bad_t2 = bad_t1 = 0.0
    for c, a in ch:
        bad_u = max(bad_u, float(np.max(np.abs(kf.OU.T @ a @ kf.OU - a))))
        want = -a if c < 0 else a
        bad_t2 = max(bad_t2, float(np.max(np.abs(kf.O2.T @ a @ kf.O2 - want))))
        bad_t1 = max(bad_t1, float(np.max(np.abs(kf.O1.T @ a @ kf.O1 - want))))
    pair.update(channel_U=bad_u, channel_T2=bad_t2, channel_T1=bad_t1)

    kr, cq = original_lower_grades(230.0)
    ar = (-2j * kr).real
    pair.update(
        R_imag=float(np.max(np.abs((-2j * kr).imag))),
        R_T2=float(np.max(np.abs(kf.O2.T @ ar @ kf.O2 + ar))),
        R_U=float(np.max(np.abs(kf.OU.T @ ar @ kf.OU - ar))),
        scalar_remainder=float(cq - decomposed_scalar(sol230)),
    )

    # Four-site f_NN row: F_x F_x^T = rho I.  Compare the exact contraction
    # 2[F^T B^dag F,F^T B F] with rho F^T 2[B^dag,B] F, and with the
    # worker's unscaled F^T 2[B^dag,B] F.
    lx, nv, nm, nmaj = 4, 32, 128, 256
    fx = np.zeros((lx, lx))
    for x in range(lx):
        fx[x, x] = -0.5
        fx[x, (x + 1) % lx] += -0.25
        fx[x, (x - 1) % lx] += -0.25
    fs = np.zeros((64, nmaj))
    for t in range(2):
        for y in range(lx):
            fs[t * nv : (t + 1) * nv, t * nm + y * nv : t * nm + (y + 1) * nv] = fx[0, y] * np.eye(nv)
    rho = float(np.sum(fx[0] ** 2))
    exact = np.zeros((nmaj, nmaj), complex)
    pulled = np.zeros_like(exact)
    for b in KB:
        bd = -b.conj()
        bg = fs.T @ b @ fs
        bdg = fs.T @ bd @ fs
        exact += 2 * (bdg @ bg - bg @ bdg)
        pulled += fs.T @ (2 * (bd @ b - b @ bd)) @ fs
    denom = float(np.max(np.abs(exact)))
    pair.update(
        rho=rho,
        filtered_correct_rel=float(np.max(np.abs(exact - rho * pulled)) / denom),
        filtered_worker_rel=float(np.max(np.abs(exact - pulled)) / denom),
    )

    # Verify all three walker directions separately on a 3-site ring.  Each
    # test is 192 Majoranas, below the 256 matrix bound.
    l = 3
    shift = np.roll(np.eye(l), 1, axis=0)
    o2g = kf.antireal(np.kron(np.eye(l), np.kron(kf.E, np.eye(16))).astype(complex))
    oug = kf.realify(np.kron(np.eye(l), np.kron(np.eye(2), 1j * kf.G9[8])))
    for label, sigma in zip("xyz", (kf.X.astype(complex), kf.SY, kf.Z.astype(complex))):
        h = np.kron((shift - shift.T) / (2j), np.kron(sigma, np.eye(16)))
        aw = (-2j * kf.density_K(h)).real
        pair[f"walker_{label}_T2"] = float(np.max(np.abs(o2g.T @ aw @ o2g + aw)))
        pair[f"walker_{label}_U"] = float(np.max(np.abs(oug.T @ aw @ oug - aw)))
    return pair


def run_algebra() -> None:
    g230, info = independent_theta230()
    r230, r270, count = exhaustive_residual(g230)
    checks = symmetry_and_filter(info["sol"])
    print("theta230 independent correction")
    print(f"  sampled rank={info['rank']} correction_inf={info['correction_inf']:.3e}")
    print(f"  sampled max relative residual={info['sample_max_rel']:.3e}")
    print(f"  sign-cone margin={info['margin']:.9f}")
    print(f"exhaustive components={count}")
    print(f"  theta230 max relative residual={r230:.3e}")
    print(f"  theta270 Fierz max relative residual={r270:.3e}")
    print("symmetry/filter checks (max absolute defects unless labelled rel)")
    for key in sorted(checks):
        print(f"  {key}={checks[key]:.12g}")
    print("theta230 omitted density blocks")
    for d in DOUBLED:
        print(f"  {d}={np.array2string(info['sol'][d], precision=8)} eig={np.linalg.eigvalsh(info['sol'][d])}")
    print(f"peak_rss_mib={rss_mib():.1f}")


def stable_logdet_1pm(bs: list[np.ndarray]) -> complex:
    from scipy.linalg import qr

    n = bs[0].shape[0]
    u = np.eye(n, dtype=complex)
    d = np.ones(n, complex)
    v = np.eye(n, dtype=complex)
    for b in bs:
        x = (b @ u) * d[None, :]
        q, r, piv = qr(x, pivoting=True, overwrite_a=True, check_finite=False)
        dn = np.diag(r).copy()
        rn = r / dn[:, None]
        pm = np.zeros((n, n))
        pm[piv, np.arange(n)] = 1.0
        v = rn @ pm.T @ v
        u, d = q, dn
    big = np.abs(d) > 1
    db = np.where(big, d, 1.0)
    ds = np.where(big, 1.0, d)
    inner = (1.0 / db)[:, None] * (u.conj().T @ np.linalg.inv(v)) + np.diag(ds)
    ans = 0.0 + 0.0j
    for z in (u, inner, v):
        s, l = np.linalg.slogdet(z)
        ans += np.log(s) + l
    ans += np.sum(np.log(db.astype(complex)))
    return ans


def build_weight_objects(sol230: dict):
    from scipy.linalg import expm

    lx, nv, nm, nmaj = 4, 32, 128, 256
    shift = np.roll(np.eye(lx), 1, axis=0)
    h = np.kron((shift - shift.T) / (2j), np.kron(kf.X.astype(complex), np.eye(16)))
    kw = kf.density_K(h)
    fx = np.zeros((lx, lx))
    for x in range(lx):
        fx[x, x] = -0.5
        fx[x, (x + 1) % lx] += -0.25
        fx[x, (x - 1) % lx] += -0.25
    fs = []
    for x in range(lx):
        f = np.zeros((64, nmaj))
        for t in range(2):
            for y in range(lx):
                f[t * nv : (t + 1) * nv, t * nm + y * nv : t * nm + (y + 1) * nv] = fx[x, y] * np.eye(nv)
        fs.append(f)
    rho = float(np.sum(fx[0] ** 2))
    kr, _ = original_lower_grades(230.0)
    # kr already includes lambda1.  Filtering a product of two local bilinears
    # inserts F F^T=rho I between them.
    rr = sum(rho * f.T @ kr @ f for f in fs)
    oug = kf.realify(np.kron(np.eye(lx), np.kron(np.eye(2), 1j * kf.G9[8])))
    w, vv = np.linalg.eig(oug)
    pp, _ = np.linalg.qr(vv[:, np.abs(w - 1j) < 1e-8])
    kwd = pp.conj().T @ kw @ pp
    rd = pp.conj().T @ rr @ pp
    fd = [f @ pp for f in fs]
    # Keep the orthonormal families in their original storage.  Building both
    # a 1,024-element channel list and a second dense (1024,64,64) array adds
    # no information and needlessly raises peak RSS.
    return kwd, rd, fd, sol230


def sample_local_av(sol: dict, dt: float, w_coupling: float, rng: np.random.Generator) -> np.ndarray:
    """Sample sum_j sqrt(2 dt W |c_j|) eta_j a_j without duplicating families."""
    av = np.zeros((64, 64), complex)
    for n in SINGLES:
        c = sol[n]
        if abs(c) < 1e-14:
            continue
        kap = np.sqrt(2 * dt * w_coupling * abs(c)) * (1.0 if c < 0 else 1j)
        ms = kf.famo[n]
        av += kap * np.tensordot(rng.normal(size=len(ms)), np.asarray(ms), axes=1)
    for d in DOUBLED:
        ev, vv = np.linalg.eigh(sol[d])
        aa = np.asarray(kf.famo[d + ":s"])
        bb = np.asarray(kf.famo[d + ":c"])
        for i in range(2):
            c = ev[i]
            if abs(c) < 1e-14:
                continue
            kap = np.sqrt(2 * dt * w_coupling * abs(c)) * (1.0 if c < 0 else 1j)
            phi = rng.normal(size=len(aa))
            av += kap * (
                vv[0, i] * np.tensordot(phi, aa, axes=1)
                + vv[1, i] * np.tensordot(phi, bb, axes=1)
            )
    return av


def run_weights() -> None:
    from scipy.linalg import expm

    _, info = independent_theta230()
    kwd, rd, fd, sol230 = build_weight_objects(info["sol"])
    rng = np.random.default_rng(8675309)
    for w_coupling, dt, lt, ncfg in ((0.5, 0.05, 4, 3), (8.0, 0.05, 10, 3)):
        k0d = kwd + w_coupling * rd
        e0 = expm(-4 * dt * k0d)
        logs = []
        det1_phases = []
        detm_phases = []
        for _ in range(ncfg):
            bs = []
            ldm = 0.0 + 0.0j
            for _slice in range(lt):
                av = sample_local_av(sol230, dt, w_coupling, rng)
                kvd = np.zeros_like(k0d)
                for f in fd:
                    kvd += f.conj().T @ ((0.5j) * av) @ f
                bs.append(e0 @ expm(4 * kvd))
                # det(exp A exp B)=exp(tr A+tr B).  This avoids taking a
                # determinant of an ill-conditioned exponential at W=8.
                ldm += np.trace(-4 * dt * k0d) + np.trace(4 * kvd)
            l1 = stable_logdet_1pm(bs)
            logw = l1 - 0.5 * ldm
            logs.append(logw)
            det1_phases.append(float(np.angle(np.exp(1j * l1.imag))))
            detm_phases.append(float(np.angle(np.exp(1j * ldm.imag))))
        print(f"W={w_coupling:g} dt={dt:g} Lt={lt} ncfg={ncfg}")
        print("  weight_phases=" + np.array2string(np.angle(np.exp(1j * np.imag(logs))), precision=6))
        print("  det1_phases=" + np.array2string(np.asarray(det1_phases), precision=6))
        print("  detM_phases=" + np.array2string(np.asarray(detm_phases), precision=6))
        print("  log_abs_weights=" + np.array2string(np.real(logs), precision=6))
    print(f"peak_rss_mib={rss_mib():.1f}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=("algebra", "weights"))
    args = p.parse_args()
    if args.mode == "algebra":
        run_algebra()
    else:
        run_weights()


if __name__ == "__main__":
    main()
