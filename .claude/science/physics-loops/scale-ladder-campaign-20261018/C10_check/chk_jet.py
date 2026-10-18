#!/usr/bin/env python3
"""C10 check: jet certificates for flat Kuchar densities, own encoding (new code).
Infinite lattice Z (no ring), central Delta, chiral bracket {a_i,a_j} = 2 Delta_ij.
h_x = sum_{r<=s in [A0,A1]} c_rs(window variables at x) a_{x+r} a_{x+s}, c_rs polynomial of degree <= N.
Classes (window encodings differ from the C10 runner):
  g     : c in E_t = (Delta u)_{x+t}, t in [W0,W1], substituted as linear forms in u   (X+ only via g)
  shift : c in differences u_{x+t} - u_{x+W0}, t in (W0,W1]   (shift invariance built in, not imposed)
  u     : c in u_{x+t}, t in [W0,W1]   (no shift invariance; control)
Flatness F_0y = d_{u_y} h_0 - d_{u_0} h_y + {h_0,h_y}: all u-monomials of degree <= N-1 in the a-quadratic
coefficients must vanish (complete for C^N coefficient functions at the ruler u = 0).
{h_0,h_y} computed as quadratic form 8 a^T S0 Dl Sy a with S the symmetric coefficient matrices.
Normalisation: uniform value sum_{r<=s} c_rs(0) != 0  (t * value - 1)."""
import sympy as sp, itertools, sys, time
from sympy import QQ

def run(A0, A1, W0, W1, N, mode):
    t0 = time.time()
    pairs = [(r, s) for r in range(A0, A1 + 1) for s in range(r, A1 + 1)]
    if mode == "g":   vars_off = list(range(W0, W1 + 1))
    elif mode == "shift": vars_off = list(range(W0 + 1, W1 + 1))
    else: vars_off = list(range(W0, W1 + 1))
    mons = [c for k in range(N + 1) for c in itertools.combinations_with_replacement(range(len(vars_off)), k)]
    kap = {}
    for (r, s) in pairs:
        for c in mons:
            kap[(r, s, c)] = sp.Symbol(f"K{r+10}_{s+10}_" + "".join(map(str, c)) + f"_{len(c)}")
    # u-variables: indices over a generous range
    lo, hi = -40, 40
    U = {i: sp.Symbol(f"u{i - lo}") for i in range(lo, hi)}
    def winvar(x, j):
        t = vars_off[j]
        if mode == "g": return (U[x + t + 1] - U[x + t - 1]) / 2
        if mode == "shift": return U[x + t] - U[x + W0]
        return U[x + t]
    def coeffs(x):
        """symmetric coefficient dict S[(i,j)] (i<=j absolute a-indices) -> polynomial in u"""
        S = {}
        wv = [winvar(x, j) for j in range(len(vars_off))]
        for (r, s, c), k in kap.items():
            mon = sp.Mul(*[wv[j] for j in c])
            key = (x + r, x + s)
            S[key] = S.get(key, 0) + k * mon
        return {key: sp.expand(v) for key, v in S.items()}
    def symmat(S):
        M = {}
        for (i, j), v in S.items():
            if i == j: M[(i, i)] = M.get((i, i), 0) + v
            else:
                M[(i, j)] = M.get((i, j), 0) + v / 2; M[(j, i)] = M.get((j, i), 0) + v / 2
        return M
    Dl = lambda i, j: sp.Rational(1, 2) if j == i + 1 else (-sp.Rational(1, 2) if j == i - 1 else 0)
    S0 = coeffs(0); M0 = symmat(S0)
    usyms = list(U.values())
    eqs = set()
    span = 2 * (A1 - A0) + (W1 - W0) + 6
    for y in range(1, span + 1):
        Sy = coeffs(y); My = symmat(Sy)
        Q = {}
        # derivative terms (quadratic form coefficient dict keyed i<=j)
        for (i, j), v in S0.items():
            dv = sp.diff(v, U[y])
            if dv != 0: Q[(i, j)] = Q.get((i, j), 0) + dv
        for (i, j), v in Sy.items():
            dv = sp.diff(v, U[0])
            if dv != 0: Q[(i, j)] = Q.get((i, j), 0) - dv
        # bracket term 8 a^T M0 Dl My a
        rows0 = {}
        for (i, j), v in M0.items(): rows0.setdefault(i, []).append((j, v))
        colsy = {}
        for (i, j), v in My.items(): colsy.setdefault(i, []).append((j, v))
        P = {}
        for i, lst in rows0.items():
            for (j, v) in lst:
                for jj in (j - 1, j + 1):
                    dlt = Dl(j, jj)
                    if jj in colsy:
                        for (k, w) in colsy[jj]:
                            P[(i, k)] = P.get((i, k), 0) + 8 * v * dlt * w
        for (i, k), v in P.items():
            key = (min(i, k), max(i, k))
            Q[key] = Q.get(key, 0) + v
        for key, v in Q.items():
            v = sp.expand(v)
            if v == 0: continue
            gens = [s for s in usyms if v.has(s)]
            if not gens:
                eqs.add(v); continue
            pl = sp.Poly(v, *gens)
            for mon, cf in pl.terms():
                if sum(mon) <= N - 1: eqs.add(sp.expand(cf))
    eqs.discard(0)
    tt = sp.Symbol("tt")
    norm = tt * sum(k for (r, s, c), k in kap.items() if len(c) == 0) - 1
    unk = list(kap.values())
    tb = time.time() - t0
    G = sp.groebner(list(eqs) + [norm], *(unk + [tt]), order="grevlex", domain=QQ)
    empty = (list(G.exprs) == [1])
    return empty, len(unk), len(eqs), tb, time.time() - t0, G

if __name__ == "__main__":
    A0, A1, W0, W1, N = map(int, sys.argv[1:6]); mode = sys.argv[6]; expect = sys.argv[7]
    empty, nu, ne, tb, tt_, G = run(A0, A1, W0, W1, N, mode)
    res = "EMPTY (Groebner [1])" if empty else f"CONSISTENT (Groebner {len(G.exprs)} elements)"
    ok = (expect == "empty") == empty
    print(f"[{'PASS' if ok else 'FAIL'}] mode={mode} a[{A0},{A1}] w[{W0},{W1}] N={N}: {res}; expected {expect}; "
          f"{nu} unknowns, {ne} eqs, build {tb:.1f}s, total {tt_:.1f}s", flush=True)
    if not empty and "--show" in sys.argv:
        print(G.exprs[:20])
