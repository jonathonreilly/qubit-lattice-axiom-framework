#!/usr/bin/env python3
"""Stress test of the deterministic Lemma 22.1 of parts/upper-chain.md: exploration of layers as a stopping set.

The lemma is proved by hand; this checks the bookkeeping on planted configurations. d = 2, three levels (0, 1, 2), L = 17 (the
lemma asks L >= 17), w_0 = 3, plain blocks, so w = 3 L. A block at level l is one level-(l+1) cell, and E_l is stored on the grid of
level-(l+1) cells. Non-quiet cells are given as sparse sets: random dust, plus planted snakes at hop at most w, which push a
layer outward and force the rule (B). The algorithm reads a cell only when it lies in a current layer.

Criteria, written before the run.
X1: on success, on every instance: (N) and (B) hold; no non-quiet cell lies on a final layer; the parent of each cell of Sigma_l is in
    Sigma_(l+1) for l < 2; each cell of Sigma_l is at least w / 2 level-l cells inside the shadow of Sigma_(l+1), from both sides.
X2: every brick added by (B) has a witness that is bad, by direct evaluation of the definition of bad, and the parent added is within
    2 w / 3 + w_0 + 2 level-(l+1) cells of the E of that time.
X3: on failure at the top, the witnesses of the top level contain a chain at range 2 w from the start to the brick that failed.
X4: not vacuous: over all instances (B) fires at least 20 times at each of the two lower levels, and at least 3 instances fail.
X5: the stopping property: rerunning with the non-quiet cells strictly outside the final family (on or inside it kept) changed
    arbitrarily gives the same final family, on 5 successful instances.

First run, as registered: X1 PASS but vacuous, X2 PASS, X3 PASS, X4 FAIL, X5 FAIL (0 instances). All 24 instances failed at the top, since the dust at level 2 had up to 400
cells on a grid of 83521, about one per block, which percolates: an error of my generator, not of the lemma. (B) fired 16 and 8 times.
Second registration, written before the second run: dust at level 2 at most 5 cells; snakes at level 2 with probability 1/10, and of 20 to 45 hops with probability 3/4.
X1 now also asks at least 5 successful instances, so that it is not vacuous. X2 to X5 as before.
Second run, as registered: X1 FAIL (2 successes, depth 34 >= 25, final checks ok), X2 PASS (37 <= 39), X3 PASS, X4 FAIL ((B) fired 32, 17), X5 FAIL (ok on 2 instances, below the 3 asked). Again the harness:
my stop fired at 3 blocks from the centre, which is inside the first layer, so one non-quiet cell at the top ended a run.
Third registration, written before the third run: the stop at a brick within 2 blocks of the edge of the grid, which leaves room for a layer; dust at level 2 at most 2 cells; snakes at level 2 with probability 1/20; 36 instances. Criteria as in the second.
Third run: X1 to X5 all PASS. 36 instances, 17 successes, (B) fired 79 and 60 times, depth 34 >= 25, largest distance 37 <= 39.
"""
import resource
import sys

import numpy as np
from scipy import ndimage
from scipy.ndimage import maximum_filter1d

RSS_LIMIT_GB = 2.0
L = 17
W0 = 3
W = W0 * L
S3 = 17  # top grid, level-3 cells
LEVELS = 3


def dil(A, r):
    B = maximum_filter1d(A.astype(np.uint8), 2 * r + 1, axis=0, mode="constant")
    return maximum_filter1d(B, 2 * r + 1, axis=1, mode="constant").astype(bool)


def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


class Run:
    def __init__(self, nq):
        self.nq = nq  # list by level of sets of (x, y) level-l cells
        self.size = [S3 * L ** (2 - l) for l in range(LEVELS)]  # E[l] lives on the grid of level-(l+1) cells
        self.E = [np.zeros((self.size[l], self.size[l]), dtype=bool) for l in range(LEVELS)]
        self.added = {0: [], 1: [], 2: []}  # (brick, witness cell, kind, distance at addition)
        self.n_b = [0, 0, 0]
        self.failed = None
        self.read = [set() for _ in range(LEVELS)]
        c = S3 // 2
        self.start = (c, c)
        self.E[2][c, c] = True
        self._fill_below(2, c, c, c, c)

    def _fill_below(self, l, x0, x1, y0, y1):
        """Rule (N) below a rectangle of bricks of E[l]: a shadow with a margin of 2 blocks."""
        while l > 0:
            x0, x1 = x0 * L - 2, (x1 + 1) * L + 1
            y0, y1 = y0 * L - 2, (y1 + 1) * L + 1
            l -= 1
            n = self.size[l]
            x0, y0 = max(x0, 0), max(y0, 0)
            x1, y1 = min(x1, n - 1), min(y1, n - 1)
            self.E[l][x0:x1 + 1, y0:y1 + 1] = True

    def _near(self, l, b, t):
        n = self.size[l]
        return self.E[l][max(b[0] - t, 0):min(b[0] + t + 1, n), max(b[1] - t, 0):min(b[1] + t + 1, n)].any()

    def _dist_to_E(self, l, cell):
        """Sup distance in level-l cells from a level-l cell to the set E[l], searched in a window."""
        n = self.size[l]
        b = (cell[0] // L, cell[1] // L)
        best = None
        for t in range(0, 8):
            x0, x1, y0, y1 = max(b[0] - t, 0), min(b[0] + t + 1, n), max(b[1] - t, 0), min(b[1] + t + 1, n)
            xs, ys = np.nonzero(self.E[l][x0:x1, y0:y1])
            if len(xs):
                xs, ys = xs + x0, ys + y0
                dx = np.maximum.reduce([xs * L - cell[0], cell[0] - (xs * L + L - 1), np.zeros_like(xs)])
                dy = np.maximum.reduce([ys * L - cell[1], cell[1] - (ys * L + L - 1), np.zeros_like(ys)])
                best = int(np.maximum(dx, dy).min())
                break
        return best

    def _shadow_block_dist(self, l, b):
        """Largest cell distance from the block b of E[l] to shadow E[l+1], in blocks: smallest t with the shadow within t blocks."""
        up = self.E[l + 1]
        n = self.size[l + 1]
        B = (b[0] // L, b[1] // L)
        x0, x1, y0, y1 = max(B[0] - 4, 0), min(B[0] + 5, n), max(B[1] - 4, 0), min(B[1] + 5, n)
        xs, ys = np.nonzero(up[x0:x1, y0:y1])
        if not len(xs):
            return 10**9
        xs, ys = xs + x0, ys + y0
        dx = np.maximum.reduce([xs * L - b[0], b[0] - (xs * L + L - 1), np.zeros_like(xs)])
        dy = np.maximum.reduce([ys * L - b[1], b[1] - (ys * L + L - 1), np.zeros_like(ys)])
        return int(np.maximum(dx, dy).min())

    def _add(self, l, b, witness, kind, dist):
        if self.E[l][b]:
            return
        self.E[l][b] = True
        self.added[l].append((b, witness, kind, dist))
        self._fill_below(l, b[0], b[0], b[1], b[1])
        if l == 2:
            n = self.size[2]
            if min(b[0], b[1], n - 1 - b[0], n - 1 - b[1]) <= 2:
                self.failed = b
            return
        # rule (B): a cell of this block farther than 2 L^2 from the shadow means t > 2 L blocks
        if self._shadow_block_dist(l, b) > 2 * L:
            self.n_b[l] += 1
            p = b  # the parent cell of any cell of the block, on the level-(l+1) grid
            d = self._dist_to_E(l + 1, p)
            self._add(l + 1, (p[0] // L, p[1] // L), p, "B", d)

    def run(self):
        changed = True
        while changed and self.failed is None:
            changed = False
            for l in range(LEVELS):
                for y in sorted(self.nq[l]):
                    b = (y[0] // L, y[1] // L)
                    if self.E[l][b] or not self._near(l, b, 3):
                        continue
                    self.read[l].add(y)
                    self._add(l, b, y, "read", None)
                    changed = True
                    if self.failed is not None:
                        return

    def key(self):
        return tuple(hash(self.E[l].tobytes()) for l in range(LEVELS))


def dust_and_snakes(rng, n_snakes):
    nq = [set() for _ in range(LEVELS)]
    sizes = [S3 * L ** (3 - l) for l in range(LEVELS)]  # in level-l cells
    c = S3 // 2
    for l in range(LEVELS):
        count = int(rng.integers(0, 3)) if l == 2 else int(rng.integers(50, 400))
        for _ in range(count):
            nq[l].add((int(rng.integers(0, sizes[l])), int(rng.integers(0, sizes[l]))))
    # half-widths of the initial E_l in level-l cells
    h2 = 0.5 * L
    h1 = (h2 + 2) * L
    h0 = (h1 + 2) * L
    halves = [h0, h1, h2]
    for _ in range(n_snakes):
        l = int(rng.choice([0, 1, 2], p=[0.475, 0.475, 0.05]))
        ctr = (c + 0.5) * L ** (3 - l)
        ang = rng.uniform(0, 2 * np.pi)
        ux, uy = np.cos(ang), np.sin(ang)
        s = max(abs(ux), abs(uy))
        ux, uy = ux / s, uy / s
        x, y = ctr + (halves[l] + L) * ux, ctr + (halves[l] + L) * uy
        for _k in range(int(rng.integers(20, 46)) if rng.uniform() < 0.75 else int(rng.integers(46, 90))):
            nq[l].add((int(x), int(y)))
            hop = rng.uniform(1.0, 2.5) * L
            x += hop * ux
            y += hop * uy
            if not (0 <= x < sizes[l] and 0 <= y < sizes[l]):
                break
    return nq


def cluster_ok(points, center, radius, rng_hop, diam):
    """Is there a chain of the given points at range rng_hop inside the sup ball, of diameter at least diam?"""
    pts = [p for p in points if max(abs(p[0] - center[0]), abs(p[1] - center[1])) <= radius]
    if len(pts) < 2:
        return False
    pts = np.array(pts)
    seen = np.zeros(len(pts), dtype=bool)
    for i in range(len(pts)):
        if seen[i]:
            continue
        stack, comp = [i], [i]
        seen[i] = True
        while stack:
            j = stack.pop()
            d = np.maximum(np.abs(pts[:, 0] - pts[j, 0]), np.abs(pts[:, 1] - pts[j, 1]))
            for k in np.nonzero((d <= rng_hop) & ~seen)[0]:
                seen[k] = True
                stack.append(int(k))
                comp.append(int(k))
        q = pts[comp]
        span = max(q[:, 0].max() - q[:, 0].min(), q[:, 1].max() - q[:, 1].min())
        if span >= diam:
            return True
    return False


def is_bad(l, cell, nq, memo):
    key = (l, cell)
    if key in memo:
        return memo[key]
    if cell in nq[l]:
        memo[key] = True
        return True
    if l == 0:
        memo[key] = False
        return False
    # chain of bad_(l-1) cells in the ball of radius w level-l cells about the cell, read in level-(l-1) cells
    ctr = ((cell[0] + 0.5) * L, (cell[1] + 0.5) * L)
    radius = W * L
    if l == 1:
        pts = nq[0]
    else:
        # bad_1 cells: non-quiet level-1 cells, plus those with a chain of bad_0 cells in their ball
        pts = set(nq[1])
        near0 = [p for p in nq[0] if max(abs(p[0] / L - ctr[0]), abs(p[1] / L - ctr[1])) <= radius + W]
        coarse = {(p[0] // L, p[1] // L) for p in near0}
        for q in coarse:
            if q not in pts and is_bad(1, q, nq, memo):
                pts.add(q)
    res = cluster_ok(pts, ctr, radius, 2 * W, W * L / 3)
    memo[key] = res
    return res


def verify_final(run):
    ok = True
    margin = 10**9
    for l in range(LEVELS):
        E = run.E[l]
        # layers on the block grid: blocks within 3 of E, not in E
        lay = dil(E, 3) & ~E
        for y in run.nq[l]:
            if lay[y[0] // L, y[1] // L]:
                ok = False
        if l < 2:
            up = run.E[l + 1]
            sh = np.kron(up, np.ones((L, L), dtype=bool))
            # (N)
            need = dil(sh, 2)
            if (need & ~E).any():
                ok = False
            # (B) in blocks: t <= 2 L for every block of E
            if sh.any():
                t = ndimage.distance_transform_cdt(~sh, metric="chessboard")
                if t[E].max() > 2 * L:
                    ok = False
            lay_up = dil(up, 3) & ~up
            lay_up_cells = np.kron(lay_up, np.ones((L, L), dtype=bool))
            if (lay & ~lay_up_cells).any():
                ok = False
            # depth inside the shadow of Sigma_(l+1), from both sides, in level-l cells at block resolution
            shadow_lay = np.kron(lay_up, np.ones((L, L), dtype=bool))
            if lay.any():
                inner = ndimage.distance_transform_cdt(shadow_lay, metric="chessboard")
                margin = min(margin, int(inner[lay].min()) * L - L)
    return ok, margin


def main():
    rng = np.random.default_rng(20261031)
    n_runs = 36
    ok1, ok2, ok3 = True, True, True
    tot_b = [0, 0]
    fails = 0
    succ_instances = []
    smallest_margin = 10**9
    worst_range = 0
    for inst in range(n_runs):
        nq = dust_and_snakes(rng, int(rng.integers(1, 7)))
        r = Run(nq)
        r.run()
        tot_b[0] += r.n_b[0]
        tot_b[1] += r.n_b[1]
        memo = {}
        for l in (1, 2):
            for b, wit, kind, dist in r.added[l]:
                if kind == "B":
                    if dist is not None:
                        worst_range = max(worst_range, dist)
                        if dist > 2 * W // 3 + W0 + 2:
                            ok2 = False
                    if not is_bad(l, wit, nq, memo):
                        ok2 = False
                        print(f"  instance {inst}: level {l} witness {wit} not bad")
        if r.failed is not None:
            fails += 1
            wits = [w for (_b, w, _k, _d) in r.added[2]]
            pts = np.array(wits)
            c = S3 // 2
            start_cells = [(c * L + i, c * L + j) for i in (0, L - 1) for j in (0, L - 1)]
            reach = np.zeros(len(pts), dtype=bool)
            for s in start_cells:
                reach |= np.maximum(np.abs(pts[:, 0] - s[0]), np.abs(pts[:, 1] - s[1])) <= 2 * W
            stack = list(np.nonzero(reach)[0])
            while stack:
                j = stack.pop()
                d = np.maximum(np.abs(pts[:, 0] - pts[j, 0]), np.abs(pts[:, 1] - pts[j, 1]))
                for k in np.nonzero((d <= 2 * W) & ~reach)[0]:
                    reach[k] = True
                    stack.append(int(k))
            if not reach[-1]:
                ok3 = False
                print(f"  instance {inst}: failure with no chain at range 2 w")
        else:
            good, margin = verify_final(r)
            smallest_margin = min(smallest_margin, margin)
            ok1 = ok1 and good and margin >= W // 2
            if len(succ_instances) < 5:
                succ_instances.append((nq, r))
        rss_guard()
    print(f"instances {n_runs}, failures {fails}, (B) fired {tot_b[0]} at level 0, {tot_b[1]} at level 1")
    print(f"X1 smallest depth inside the shadow = {smallest_margin} (claim >= {W // 2}); all final checks {'ok' if ok1 else 'NOT ok'}")
    print(f"X2 witnesses bad: {'ok' if ok2 else 'NOT ok'}; largest distance at a (B) addition {worst_range} (claim <= {2 * W // 3 + W0 + 2})")
    print(f"X3 chains at failure: {'ok' if ok3 else 'NOT ok'}")
    ok4 = tot_b[0] >= 20 and tot_b[1] >= 20 and fails >= 3
    # X5
    ok5 = True
    for nq, r in succ_instances:
        nq2 = [set(s) for s in nq]
        for l in range(LEVELS):
            E = r.E[l]
            lay = dil(E, 3)
            keep = {y for y in nq2[l] if lay[y[0] // L, y[1] // L]}
            n = S3 * L ** (3 - l)
            extra = set()
            for _ in range(300):
                y = (int(rng.integers(0, n)), int(rng.integers(0, n)))
                if not lay[y[0] // L, y[1] // L]:
                    extra.add(y)
            nq2[l] = keep | extra
        r2 = Run(nq2)
        r2.run()
        same = all((r.E[l] == r2.E[l]).all() for l in range(LEVELS))
        ok5 = ok5 and same
    print(f"X5 stopping property on {len(succ_instances)} instances: {'ok' if ok5 else 'NOT ok'}")
    n_succ = n_runs - fails
    print(f"successful instances: {n_succ}")
    print("X1", "PASS" if ok1 and n_succ >= 5 else "FAIL")
    print("X2", "PASS" if ok2 else "FAIL")
    print("X3", "PASS" if ok3 else "FAIL")
    print("X4", "PASS" if ok4 else "FAIL")
    print("X5", "PASS" if ok5 and len(succ_instances) >= 3 else "FAIL")


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    main()
