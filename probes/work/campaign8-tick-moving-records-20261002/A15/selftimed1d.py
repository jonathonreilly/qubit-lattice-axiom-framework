#!/usr/bin/env python3
"""A15 tasks 1/3 (1D): self-timed (handshake-wait) local beats for the A10 alternating-pairing cycle.

Supplied toy. Each site keeps its own counter c(x) (number of pair events it has taken part in) and a schedule
offset phi(x). Its next partner is fixed by j = c(x)+phi(x) mod 2 (as in seam1d.py). A pair fires when both sites
name each other; firing applies u(theta) and advances both counters. A site whose partner does not exist (chain
end) skips: it advances alone (lock rule). Firings of disjoint ready pairs commute, so the history (network of pair
events) does not depend on firing order; we use as-soon-as-possible rounds only to draw it.
Checks:
 (a) region B starts one sub-step out of phase: a wait front leaves the seam at one site per round; every B site
     waits exactly once; afterwards the phase is uniform;
 (b) transmission of packets through the old seam is the uniform one (= 1, no reflection);
 (c) rate lock: if B sites may fire at most every 2nd round (intrinsic rate 1/2), the long-run firing rate of every
     site tends to the slow rate (throttling front), and neighbouring counters never differ by >= 2*period."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
from seam1d import ublock, packet, branch

def partner(x, c, phi, N):
    j = (c + phi) % 2
    y = x + 1 if j == x % 2 else x - 1
    return y if 0 <= y < N else -1

def selftimed(N, phi, rounds, th=None, psi=None, avail=None, record_wait=False):
    c = np.zeros(N, int)
    u = ublock(th) if th is not None else None
    waits = np.zeros((rounds, N), bool)
    for r in range(rounds):
        sel = np.array([partner(x, c[x], phi[x], N) for x in range(N)])
        ok = np.ones(N, bool) if avail is None else avail(r, N)
        fired = np.zeros(N, bool)
        for x in range(N):
            y = sel[x]
            if not ok[x]:
                continue
            if y == -1:
                fired[x] = True          # skip a missing partner
            elif y == x + 1 and sel[y] == x and ok[y]:
                fired[x] = fired[y] = True
                if psi is not None:
                    a, b = psi[x], psi[y]
                    psi[x] = u[0, 0] * a + u[0, 1] * b
                    psi[y] = u[1, 0] * a + u[1, 1] * b
        c[fired] += 1
        waits[r] = ~fired
    return c, waits, psi

if __name__ == '__main__':
    N, s = 120, 60
    for label, phi in (("seam bond odd (s even)", np.array([0] * s + [1] * (N - s))),
                       ("seam bond even (s odd)", np.array([0] * (s + 1) + [1] * (N - s - 1)))):
        c, waits, _ = selftimed(N, phi, 80)
        # interior sites only (ends skip)
        inner = slice(2, N - 2)
        wait_counts = waits[:, inner].sum(axis=0)
        first_wait = [int(np.argmax(waits[:, x])) if waits[:, x].any() else -1 for x in range(N)]
        A_waits = wait_counts[:s - 2].sum(); B_waits = wait_counts[s - 2:].sum()
        front = [(x, first_wait[x]) for x in range(s - 6, s + 8)]
        uni = (c + phi) % 2
        # after the front: is (c+phi) uniform on sites the front has passed?
        print(label)
        print("  total waits in A-interior: %d, in B-interior: %d (sites %d)" % (A_waits, B_waits, N - s - 2))
        print("  (site, round of its single wait) near seam:", front)
        print("  final (c+phi) mod 2 over interior: values", sorted(set(uni[2:N - 2].tolist())),
              "| counters min/max", c[2:N - 2].min(), c[2:N - 2].max())
    # (b) transmission through the old seam in the self-timed model
    print("(b) packets through the self-timed seam (offset 1 at t=0)")
    N, s = 520, 260
    phi = np.array([0] * s + [1] * (N - s))
    for th, K0 in ((np.pi / 2, np.pi / 2), (np.pi / 4, 2.171), (0.3, 2.742)):
        u = ublock(th)
        vg, _, _ = branch(K0, u, +1)
        psi = packet(N, (s // 2) - 58, K0, 12.0, u, +1)
        psi[s:] = 0; psi /= np.linalg.norm(psi)
        T = int(2 * 116 / abs(vg)) + 20
        _, _, psi = selftimed(N, phi, T, th=th, psi=psi.astype(complex))
        p = np.abs(psi) ** 2
        print("  theta=%.3f K0=%.3f: transmitted %.12f reflected %.3e" % (th, K0, p[s:].sum(), p[:s].sum()))
    # (c) rate lock / throttling front: B sites (x >= s) available only on even rounds
    N, s = 200, 100
    phi = np.zeros(N, int)
    avail = lambda r, N: np.array([True] * s + [r % 2 == 0] * (N - s))
    R = 400
    c, waits, _ = selftimed(N, phi, R, avail=avail)
    rate_late = (~waits[R // 2:, :]).mean(axis=0)
    print("(c) A intrinsic rate 1, B intrinsic rate 1/2: late-time firing rate at x =",
          {x: round(float(rate_late[x]), 3) for x in (2, 20, 50, 80, 95, 99, 100, 150, 197)})
    # throttling front: first round at which site x falls behind the free-running count
    lag_front = []
    c_t = np.zeros(N, int)
    cnt = np.zeros(N, int)
    for r in range(R):
        cnt += ~waits[r]
        behind = np.where(cnt[:s] < r + 1)[0]
        lag_front.append(s - behind.min() if behind.size else 0)
    print("    depth of throttled zone in A after r rounds:", {r: lag_front[r] for r in (10, 40, 80, 160, 199)})
    dc = np.abs(np.diff(c[2:N - 2]))
    print("    max neighbour counter difference:", dc.max(), "(bound: < 2 * period = 4)")
