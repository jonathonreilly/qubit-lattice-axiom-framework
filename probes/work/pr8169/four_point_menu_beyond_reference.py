#!/usr/bin/env python3
"""J:falsifier:PR8169 - the frame-attached four-point menu note (PR #8169), its Falsifiers section: "Falsified if the bisector
180-degree map fails to swap the reference pair, if pair-Gibbs at e^{2 beta} = 2, t = 0 is not 1/3 and 1/6, if the Born four-tuple does not
sum to 2, or if the chain and ends-first supports of the executed path have equal cardinality."  The runner executes each item at the
orthogonal reference pair q = e_z, q' = e_x and on one three-site path.  Here, exactly and beyond those sizes:
  (1) every non-collinear pair of rational unit vectors (q, q') from Pythagorean quadruples with denominator <= D_MAX: the bisector
      map R = 2 b b^T - I (b = (q + q')/|q + q'|, R rational) is a proper rotation that swaps q and q' and preserves S = {q, q', -q, -q'};
      a rotation fixing q and q' is the identity and a rotation swapping them is R (checked through its action on q, q', q x q'), so the
      stabilizer of the unordered neighbourhood is {I, R} and the covariant laws are the copy/flip family (the orbits {q, q'}, {-q, -q'});
  (2) pair-Gibbs on S at every such t: copy/flip ratio exp(2 beta (1 + t)) exactly (symbolic beta), and alpha = 1/3, gamma = 1/6 at t = 0,
      e^{2 beta} = 2; the linear family (1 + lambda s.(q + q'))/4 gives alpha = (1 + lambda (1 + t))/4;
  (3) the two-outcome Born overlap (1 + s.q)/2 on S at every such pair: the four values and their sum;
  (4) supports under sequential formation on paths of n = 3..7 sites, every formation order (n! orders): a site formed with 0 recorded
      neighbours draws from the whole sphere (Haar), with one recorded neighbour q from {q, -q}, with two non-collinear ones from
      S(q, q') (four points; two if collinear); the support-size signature of each order, the chain versus ends-first comparison, and the
      number of distinct signatures.
HIT if any item fails.  Exact rationals (fractions) and sympy for the symbolic identities; deterministic.
"""
import itertools
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

D_MAX = 30


def rational_unit_vectors(dmax):
    out = set()
    for d in range(1, dmax + 1):
        for a in range(-d, d + 1):
            for b in range(-d, d + 1):
                c2 = d * d - a * a - b * b
                if c2 < 0:
                    continue
                c = int(round(c2 ** 0.5))
                if c * c == c2:
                    for cc in {c, -c}:
                        out.add((Fr(a, d), Fr(b, d), Fr(cc, d)))
    return sorted(out)


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def matvec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def neg(v):
    return tuple(-x for x in v)


def part1_3():
    vecs = rational_unit_vectors(D_MAX)
    pairs = [(q, p) for q, p in itertools.combinations(vecs, 2) if abs(dot(q, p)) < 1]
    ts = set()
    bad = {"rotation": 0, "swap": 0, "set": 0, "stabilizer": 0, "born": 0, "distinct": 0}
    for q, p in pairs:
        t = dot(q, p)
        ts.add(t)
        S = {q, p, neg(q), neg(p)}
        if len(S) != 4:
            bad["distinct"] += 1
        s = tuple(x + y for x, y in zip(q, p))
        n2 = dot(s, s)                                     # > 0 since t > -1
        R = [[2 * s[i] * s[j] / n2 - (1 if i == j else 0) for j in range(3)] for i in range(3)]
        RtR = [[sum(R[k][i] * R[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        if not (all(RtR[i][j] == (1 if i == j else 0) for i in range(3) for j in range(3)) and det3(R) == 1):
            bad["rotation"] += 1
        if not (matvec(R, q) == p and matvec(R, p) == q):
            bad["swap"] += 1
        if {matvec(R, v) for v in S} != S:
            bad["set"] += 1
        # stabilizer: a rotation g is fixed by g q, g q' and g(q x q') = g q x g q'; fixing (q, q') forces g(n) = n (identity); swapping
        # forces g(n) = q' x q = -n, which is R's action
        nvec = cross(q, p)
        if matvec(R, nvec) != neg(nvec):
            bad["stabilizer"] += 1
        born = [(1 + dot(v, q)) / 2 for v in (q, p, neg(q), neg(p))]
        if sum(born) != 2 or born[0] != 1 or born[2] != 0 or born[1] != (1 + t) / 2 or born[3] != (1 - t) / 2:
            bad["born"] += 1
    print(f"[1] {len(vecs)} rational unit vectors (denominators <= {D_MAX}); {len(pairs)} non-collinear pairs over {len(ts)} values of t in "
          f"[{float(min(ts)):.4f}, {float(max(ts)):.4f}]: failures {bad}")
    print(f"[3] Born overlap (1 + s.q)/2 on S: values 1, (1 + t)/2, 0, (1 - t)/2 summing to 2 at every pair: {bad['born'] == 0}")
    # (2) Gibbs and linear families, symbolically in t and beta
    t, b, lam = sp.symbols("t beta lambda", real=True)
    wq = sp.exp(b * (1 + t))                               # s = q or q': s.(q + q') = 1 + t
    wf = sp.exp(-b * (1 + t))                              # s = -q or -q'
    alpha, gamma = wq / (2 * wq + 2 * wf), wf / (2 * wq + 2 * wf)
    ok_ratio = sp.simplify(alpha / gamma - sp.exp(2 * b * (1 + t))) == 0
    B = sp.log(2) / 2
    ok_13 = sp.simplify(alpha.subs({t: 0, b: B}) - sp.Rational(1, 3)) == 0 and sp.simplify(gamma.subs({t: 0, b: B}) - sp.Rational(1, 6)) == 0
    ok_b0 = sp.simplify(alpha.subs(b, 0) - sp.Rational(1, 4)) == 0
    lin_q, lin_f = (1 + lam * (1 + t)) / 4, (1 - lam * (1 + t)) / 4
    ok_lin = sp.simplify(2 * lin_q + 2 * lin_f - 1) == 0 and [lin_q.subs({t: 0, lam: v}) for v in (0, 1, -1)] == [sp.Rational(1, 4), sp.Rational(1, 2), 0]
    exact_ts = sorted(ts)[:: max(1, len(ts) // 12)]
    pts = [(float(tt), float(alpha.subs({t: sp.Rational(tt.numerator, tt.denominator), b: B}))) for tt in exact_ts]
    print(f"[2] pair-Gibbs: alpha/gamma = exp(2 beta (1 + t)) symbolically: {ok_ratio}; alpha = 1/3, gamma = 1/6 at t = 0, e^(2 beta) = 2: {ok_13}; "
          f"uniform at beta = 0: {ok_b0}; linear family sums to 1 and gives 1/4, 1/2, 0 at lambda = 0, 1, -1 (t = 0): {ok_lin}")
    print("[2] copy mass alpha(t) at e^(2 beta) = 2 on sample rational t: " + ", ".join(f"t={a:+.3f}: {v:.4f}" for a, v in pts))
    ok = all(v == 0 for v in bad.values()) and ok_ratio and ok_13 and ok_b0 and ok_lin
    return ok, len(pairs), len(ts)


def part4():
    """support sizes under every formation order on a path of n sites (generic, non-collinear Haar draws)."""
    res = {}
    for n in range(3, 8):
        sigs = set()
        chain = tuple(range(n))
        ends_first = (0, n - 1) + tuple(range(1, n - 1))
        sig_of = {}
        for order in itertools.permutations(range(n)):
            formed = set()
            sig = [None] * n
            for x in order:
                rec = [y for y in (x - 1, x + 1) if 0 <= y < n and y in formed]
                # 0 recorded: the sphere (continuum, 'inf'); 1: the antipodal pair of that neighbour (2); 2: generic non-collinear draws (4)
                sig[x] = "inf" if not rec else (2 if len(rec) == 1 else 4)
                formed.add(x)
            sig = tuple(sig)
            sigs.add(sig)
            sig_of[order] = sig
        c, e = sig_of[chain], sig_of[ends_first]
        mids_chain = [c[i] for i in range(1, n - 1)]
        mids_ends = [e[i] for i in range(1, n - 1)]
        res[n] = (len(sigs), c, e, c != e)
        print(f"[4] path of {n} sites: {len(sigs)} distinct support signatures over {len(sig_of)} orders; chain {c}, ends-first {e}; "
              f"interior supports chain {mids_chain} vs ends-first {mids_ends}: {'differ' if c != e else 'EQUAL'}")
    return all(v[3] for v in res.values()) and res[3][1][1] == 2 and res[3][2][1] == 4, res


def main():
    t0 = time.time()
    ok13, npairs, nts = part1_3()
    ok4, res = part4()
    print(f"[time] {time.time() - t0:.1f}s")
    if not ok13:
        print("HIT: an exact check of Theorems 1-4 fails at some rational non-collinear pair (see [1]-[3])")
    if not ok4:
        print("HIT: the chain and ends-first supports agree on some path (see [4])")
    print(f"SUMMARY: bisector swap, S preserved, stabilizer {{I, R}}, Born sum 2 exact at all {npairs} rational non-collinear pairs ({nts} values of t, "
          f"denominators <= {D_MAX}); Gibbs 1/3, 1/6 and the linear family symbolic; supports on paths n = 3..7 over all orders: chain != ends-first "
          f"for every n, distinct signatures {', '.join(f'n={n}: {v[0]}' for n, v in res.items())}; falsifier "
          f"{'does not fire' if (ok13 and ok4) else 'FIRES'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
