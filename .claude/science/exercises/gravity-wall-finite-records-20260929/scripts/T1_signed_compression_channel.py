"""Exercise test T1 (route F3, agent 2): a signed (population-inverted) compression channel.

Pre-registered reading (written before running):
  PASS (route alive) if, in probe 18's isotropic metric-stored model with the helicity-0 kinetic weight made negative
  (alpha < 0) and tuned so the helicity +-1 kinetic weight vanishes at O(q^2) (v1 = 0), the spectrum is exactly two
  linear pure-TT modes, every other mode is frozen or has omega^2 = 0 to the orders checked, and no mode has omega^2 < 0.
  FAIL if the +-1 modes stay gapless at a higher order (soft), or any mode has omega^2 < 0 (instability).
Model: probe 18's kappa_iso(alpha, beta) (alpha: gauge-pattern moves, which carry helicity 0 and +-1; beta: curl moves,
TT and +-1), the landed E-H symbol plus an on-site stiffness m2 (Fierz-Pauli form optional), scalar rule exact (reduced to ker s).
"""
import io, contextlib, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(open(os.path.join(HERE, "_p18_defs.py")).read())


def raw_modes(q, alpha, beta, m2, fp):
    s_ = S_sym(q); B = np.linalg.svd(s_[None, :])[2][1:].conj().T
    trq = np.array([1, 1, 1, 0, 0, 0.])
    V = Xr(q) + m2 * (Nmet - (np.outer(trq, trq) if fp else 0))
    Gi = np.linalg.inv(B.conj().T @ B); kred = Gi @ B.conj().T @ kappa_iso(q, alpha, beta) @ B @ Gi; Vred = B.conj().T @ V @ B
    w2, vec = np.linalg.eig(Vred @ kred); o = np.argsort(w2.real); K = 2 * np.sin(q / 2)
    out = []
    for j_ in o:
        hv = B @ (kred @ vec[:, j_])
        lab = helicity(hv, K) if np.linalg.norm(hv) > 1e-12 else (None, 1.0)
        out.append((w2[j_].real, w2[j_].imag, lab))
    return out


n = np.array([0.3, -0.5, 0.81]); n /= np.linalg.norm(n)
beta = 1.0
print("probe 18 control (alpha = 1, fp):", [(round(w / (1e-3) ** 2, 4), l) for w, _, l in raw_modes(1e-3 * n, 1.0, beta, 1.0, True)])
for fp in (True, False):
    # scan alpha to find where the +-1 omega^2/q^2 coefficient crosses zero
    def pm1_coef(alpha, qq=1e-3):
        ms = raw_modes(qq * n, alpha, beta, 1.0, fp)
        vals = [w / qq ** 2 for w, _, (h, p) in ms if h == 1]
        return min(vals, key=abs) if vals else np.nan
    alphas = np.linspace(-1.0, 1.0, 81)
    coefs = [pm1_coef(a) for a in alphas]
    k = np.nanargmin(np.abs(coefs)); a_star = alphas[k]
    # refine by bisection on the sign change if any
    sgn = np.sign(coefs)
    for i in range(len(alphas) - 1):
        if sgn[i] * sgn[i + 1] < 0:
            lo, hi = alphas[i], alphas[i + 1]
            for _ in range(50):
                mid = (lo + hi) / 2
                if np.sign(pm1_coef(mid)) == np.sign(pm1_coef(lo)): lo = mid
                else: hi = mid
            a_star = (lo + hi) / 2
            break
    print(f"\nfp = {fp}: alpha* = {a_star:.6f} (helicity +-1 omega^2/q^2 coefficient there: {pm1_coef(a_star):.2e})")
    for qq in (1e-2, 2e-2, 4e-2):
        ms = raw_modes(qq * n, a_star, beta, 1.0, fp)
        print(f"  q = {qq}: " + "; ".join(f"h={l[0]} pur={l[1]:.3f} w2/q^2={w / qq ** 2:+.4e} w2/q^4={w / qq ** 4:+.3e}" for w, wi, l in ms))

print("\nAt the exact cancellation alpha = -1/2 (from the identity c1^2 = alpha c2^2/2 + c2^2/4 with c0^2 = alpha c2^2):")
for fp in (True, False):
    for direction in (n, np.array([1., 0, 0]), np.array([1., 1, 1]) / np.sqrt(3)):
        rows = []
        for qq in (2e-2, 4e-2, 8e-2):
            ms = raw_modes(qq * direction, -0.5, beta, 1.0, fp)
            pm1 = [w for w, _, (h, p) in ms if h == 1]
            h0 = [w for w, _, (h, p) in ms if h == 0]
            rows.append((qq, [x / qq ** 4 for x in pm1], [x / qq ** 2 for x in h0]))
        print(f"  fp={fp} dir={np.round(direction, 2)}: " + "; ".join(f"q={qq}: +-1 w2/q^4={np.round(a, 3).tolist()} h0 w2/q^2={np.round(b, 4).tolist()}" for qq, a, b in rows))

print("\nFull reduced spectra omega^2 (all 5 physical modes), sorted, at several q, fp = True:")
for a in (-0.51, -0.5, -0.49):
    for direction in (n, np.array([1., 0, 0])):
        line = []
        for qq in (0.05, 0.2, 0.6, 1.5):
            ms = raw_modes(qq * direction, a, beta, 1.0, True)
            line.append(f"q={qq}: " + ",".join(f"{w:+.2e}" for w, _, _ in ms))
        print(f"  alpha={a} dir={np.round(direction, 2)}: " + " | ".join(line))
