#!/usr/bin/env python3
"""superposition-of-two-sources, independent run 2 of 2 (worker w-jonathonsmac4f50-j213d, claude-opus-5).

Built on probes/lib/formation_response.py (copied beside this file as formation_response_copy.py; its step function is restated
here, vectorised over copies).  Light-cone past (dim 3s, n = 7) on a 32^3 periodic plane, aligned start e0 = (0,0,1), a field
h along t1 = (1,0,0) added to V = beta S at the source sites at every level.  Copies with the SAME random numbers:
  0  no field;  A  field +h at the origin;  B(d, sign)  field sign*h at d e1;  AB(d, sign)  both fields.
Displacement field of copy X: delta_X(x) = mean over levels T0 < t <= T of (s_X - s_0).t1, spatial mean removed (as in the
library).  Nonlinearity N = delta_AB - delta_A - delta_B against the sum S = delta_A + delta_B:
  printed along the line through the sources (x1 from -4 to d + 4, x2 = x3 = 0) and along the perpendicular line through the
  midpoint (x1 = d/2, x3 = 0, x2 from 0 to 8), plus the global ratios max|N|/max|S| and ||N||_2/||S||_2.
Statistical control: the same ratios computed from the two halves of the averaging window (their spread is the error)."""
import sys
import time
import numpy as np

L, T, T0, SEED = 32, 2000, 800, 1
n = 7
t1 = np.array([1.0, 0.0, 0.0])
e0 = np.array([0.0, 0.0, 1.0])


def step(s, U, ph, beta, fields):
    """s: (C, L, L, L, 3); fields: list per copy of [(site, vector)]"""
    S = s + sum(np.roll(s, 1, axis=j + 1) + np.roll(s, -1, axis=j + 1) for j in range(3))
    V = beta * S
    for c, fl in enumerate(fields):
        for site, vec in fl:
            V[(c,) + site] = V[(c,) + site] + vec
    kappa = np.linalg.norm(V, axis=-1)
    kappa = np.where(kappa < 1e-12, 1e-12, kappa)
    uu = V / kappa[..., None]
    w = np.clip(1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa, -1.0, 1.0)
    a = np.where((np.abs(uu[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    b1 = a - (a * uu).sum(-1)[..., None] * uu
    b1 /= np.linalg.norm(b1, axis=-1)[..., None]
    b2 = np.cross(uu, b1)
    r = np.sqrt(np.clip(1 - w * w, 0, 1))
    return w[..., None] * uu + r[..., None] * (np.cos(ph)[..., None] * b1 + np.sin(ph)[..., None] * b2)


def run(beta, h):
    origin = (0, 0, 0)
    copies = [("0", []), ("A", [(origin, h * t1)])]
    for d in (4, 8):
        for sg in (1, -1):
            copies.append((f"B{d}{'+' if sg > 0 else '-'}", [((d, 0, 0), sg * h * t1)]))
            copies.append((f"AB{d}{'+' if sg > 0 else '-'}", [(origin, h * t1), ((d, 0, 0), sg * h * t1)]))
    C = len(copies)
    rng = np.random.default_rng(SEED)
    s = np.broadcast_to(e0, (C, L, L, L, 3)).copy()
    acc = [np.zeros((C, L, L, L)), np.zeros((C, L, L, L))]
    cnt = [0, 0]
    half = T0 + (T - T0) // 2
    for t in range(1, T + 1):
        U = rng.random((L, L, L))
        ph = rng.random((L, L, L)) * 2 * np.pi
        s = step(s, U[None], ph[None], beta, [f for _, f in copies])
        if t > T0:
            j = 0 if t <= half else 1
            acc[j] += (s - s[0:1]) @ t1
            cnt[j] += 1
    fields = {}
    for part in ("all", "h1", "h2"):
        if part == "all":
            a = (acc[0] + acc[1]) / (cnt[0] + cnt[1])
        else:
            a = acc[0 if part == "h1" else 1] / cnt[0 if part == "h1" else 1]
        a = a - a.mean(axis=(1, 2, 3), keepdims=True)
        fields[part] = {name: a[c] for c, (name, _) in enumerate(copies)}
    m = float(np.linalg.norm(s[0].reshape(-1, 3).mean(axis=0)))
    return fields, m


def main():
    t_start = time.time()
    summary = []
    for beta in (3.0, 6.0):
        for h in (0.5, 2.0):
            fields, m = run(beta, h)
            F = fields["all"]
            print(f"beta={beta:g} h={h:g} L={L} T={T} T0={T0} seed={SEED}: |m| of the unperturbed copy = {m:.4f}; "
                  f"delta_A at the source = {F['A'][0, 0, 0]:+.6f}, at r = 1, 4 along e1: {F['A'][1, 0, 0]:+.6f}, {F['A'][4, 0, 0]:+.6f}")
            for d in (4, 8):
                for sg in ("+", "-"):
                    Sf = F["A"] + F[f"B{d}{sg}"]
                    Nf = F[f"AB{d}{sg}"] - F["A"] - F[f"B{d}{sg}"]
                    rmax = float(np.max(np.abs(Nf)) / np.max(np.abs(Sf)))
                    rl2 = float(np.linalg.norm(Nf) / np.linalg.norm(Sf))
                    halves = []
                    for part in ("h1", "h2"):
                        G = fields[part]
                        S2 = G["A"] + G[f"B{d}{sg}"]
                        N2 = G[f"AB{d}{sg}"] - G["A"] - G[f"B{d}{sg}"]
                        halves.append(float(np.max(np.abs(N2)) / np.max(np.abs(S2))))
                    line = " ".join(f"{x}:{Sf[x % L, 0, 0]:+.5f}/{Nf[x % L, 0, 0]:+.6f}" for x in range(-4, d + 5, 2))
                    perp = " ".join(f"{y}:{Sf[d // 2, y, 0]:+.5f}/{Nf[d // 2, y, 0]:+.6f}" for y in (0, 1, 2, 4, 8))
                    print(f"  d={d} sign {sg}: max|N|/max|S| = {rmax:.4f} (halves {halves[0]:.4f}, {halves[1]:.4f}), ||N||/||S|| = {rl2:.4f}; "
                          f"along e1 (x: S/N) {line}; perpendicular through the midpoint (x2: S/N) {perp}")
                    summary.append((beta, h, d, sg, rmax, rl2, halves))
    print("table: beta h d sign | max|N|/max|S| | ||N||/||S|| | half-window values")
    for beta, h, d, sg, rmax, rl2, halves in summary:
        print(f"  {beta:g} {h:g} {d} {sg} | {rmax:.4f} | {rl2:.4f} | {halves[0]:.4f} {halves[1]:.4f}")
    small = [x for x in summary if x[1] == 0.5]
    big = [x for x in summary if x[1] == 2.0]
    worst_small = max(x[4] for x in small)
    worst_small_l2 = max(x[5] for x in small)
    big_range = (min(x[4] for x in big), max(x[4] for x in big))
    print(f"seconds={time.time() - t_start:.0f}")
    print("=" * 90)
    msg = (f"at h = 0.5 the two-source field equals the sum of the one-source fields to within max|N|/max|S| <= {worst_small:.4f} "
           f"(||N||/||S|| <= {worst_small_l2:.4f}) over beta = 3, 6, d = 4, 8 and both signs; at h = 2 the ratio is "
           f"{big_range[0]:.4f} to {big_range[1]:.4f}")
    print("SUMMARY: " + msg)
    if worst_small > 0.02:
        print(f"HIT: additivity at h = 0.5 fails the task's 2 % expectation: {msg}")
    elif big_range[1] <= 0.02:
        print(f"HIT: no visible saturation at h = 2 (every ratio at or below 2 %): {msg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
