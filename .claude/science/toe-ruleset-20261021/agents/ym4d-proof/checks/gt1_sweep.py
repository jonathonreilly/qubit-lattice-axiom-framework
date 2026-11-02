#!/usr/bin/env python3
# gt1_sweep.py -- float sweep at larger torus side.  Criteria: checks/gt1_criteria.md, clauses gt2-E, gt2-F;
# plus a RE-RUN of the moment-cancellation separation (clause gt1-D) at larger R, recorded under the new id
# gt1b-D with the gt1 criteria untouched.
# Precision: IEEE double.  Separable nested 1-D DFT of 1/phi(k); no numpy, no BLAS, single thread.
# NUMERIC LOCK is taken by the caller.
import math, cmath, sys

def green(d, R):
    """G(x) = R^-d sum_{k != 0} exp(2 pi i k.x / R) / phi(k), by d nested 1-D DFTs.  Returns a flat list."""
    N = R ** d
    phi = [0.0] * N
    # phi(k) = sum_mu (2 - 2 cos(2 pi k_mu / R))
    c = [2.0 - 2.0 * math.cos(2.0 * math.pi * m / R) for m in range(R)]
    for i in range(N):
        t = i; s = 0.0
        for _ in range(d):
            s += c[t % R]; t //= R
        phi[i] = s
    A = [0.0 + 0j] * N
    for i in range(N):
        A[i] = (1.0 / phi[i]) if phi[i] > 1e-12 else 0.0
    W = [[cmath.exp(2j * math.pi * (a * b % R) / R) for b in range(R)] for a in range(R)]
    stride = 1
    for mu in range(d):
        blk = stride * R
        for base in range(0, N, blk):
            for off in range(stride):
                idx = [base + off + j * stride for j in range(R)]
                vals = [A[t] for t in idx]
                for a in range(R):
                    Wa = W[a]
                    tot = 0j
                    for b in range(R):
                        tot += vals[b] * Wa[b]
                    A[idx[a]] = tot
        stride = blk
    f = 1.0 / N
    return [v.real * f for v in A]

def mk(d, R):
    G = green(d, R)
    Rp = [R ** (d - 1 - mu) for mu in range(d)]
    def ix(x):
        return sum((x[mu] % R) * Rp[mu] for mu in range(d))
    return G, ix

def rep(m, R):
    m %= R
    return m - R if 2 * m > R else m

def main():
    d = 4
    out = []; P = out.append
    P("gt1_sweep.py -- float sweep, d=4, separable nested 1-D DFT.  IEEE double.  Numeric lock held.")
    P("criteria: checks/gt1_criteria.md (clauses gt2-E, gt2-F; plus gt1b-D, a re-run of gt1-D at larger R).")
    M1 = {}; M2 = {}
    for R in (8, 12, 16, 24):
        G, ix = mk(d, R)
        # solver validation (float): Delta G == delta_0 - R^-d
        worst = 0.0
        for i in range(0, R ** d, max(1, R ** d // 4000)):
            x = [(i // (R ** (d - 1 - mu))) % R for mu in range(d)]
            s = 0.0
            for mu in range(d):
                e = [0] * d; e[mu] = 1
                s += 2 * G[ix(x)] - G[ix([x[k] + e[k] for k in range(d)])] - G[ix([x[k] - e[k] for k in range(d)])]
            want = (1.0 if all(v % R == 0 for v in x) else 0.0) - R ** (-d)
            worst = max(worst, abs(s - want))
        P("")
        P("=== R=%d ===  solver validation max|Delta G - (delta - R^-d)| = %.3e" % (R, worst))
        half = R // 2
        rows = []
        for s in range(1, half + 1):
            ax = [s] + [0] * (d - 1)
            dg = G[ix([ax[0] + 1] + [0] * (d - 1))] - G[ix(ax)]
            d2g = (G[ix([ax[0] + 2] + [0] * (d - 1))] - 2 * G[ix([ax[0] + 1] + [0] * (d - 1))] + G[ix(ax)])
            dg2 = [s] * d
            dgd = G[ix([dg2[0] + 1] + dg2[1:])] - G[ix(dg2)]
            rows.append((s, dg, d2g, dgd))
        P("  s | r^3|gradG| ax | r^4|gradG| ax | r^4|grad^2G| ax | r^5|grad^2G| ax | diag r^3|gradG|")
        for (s, dg, d2g, dgd) in rows:
            r = float(s); rd = math.sqrt(d) * s
            P("  %2d | %12.6f | %12.6f | %14.6f | %14.6f | %14.6f"
              % (s, r ** 3 * abs(dg), r ** 4 * abs(dg), r ** 4 * abs(d2g), r ** 5 * abs(d2g),
                 rd ** 3 * abs(dgd)))
        M1[R] = max(r ** 3 * abs(dg) for (r, dg, _, _) in [(float(a), b, c, e) for (a, b, c, e) in rows])
        M2[R] = max(float(a) ** 4 * abs(c) for (a, b, c, e) in rows if a >= 2)
        if R == 24:
            seq3 = [float(a) ** 3 * abs(b) for (a, b, c, e) in rows if a >= 2]
            seq4 = [float(a) ** 4 * abs(b) for (a, b, c, e) in rows if a >= 2]
            seq4b = [float(a) ** 4 * abs(c) for (a, b, c, e) in rows if a >= 2]
            seq5 = [float(a) ** 5 * abs(c) for (a, b, c, e) in rows if a >= 2]
            def bounded(q):
                return max(q) / min(q) < 2.0
            def mono(q):
                return all(q[i + 1] > q[i] for i in range(len(q) - 1))
            P("  gt2-F: s^3|gradG| bounded(<2x): %s ; s^4|gradG| monotone: %s ; "
              "s^4|grad^2G| bounded(<2x): %s ; s^5|grad^2G| monotone: %s  -> %s"
              % (bounded(seq3), mono(seq4), bounded(seq4b), mono(seq5),
                 "PASS" if (bounded(seq3) and mono(seq4) and bounded(seq4b) and mono(seq5)) else "FAIL"))
            # ---- gt1b-D : the moment-cancellation separation at R=24 (re-run of gt1-D, new id) ----
            # bare kernel column: potential = G on component (0,1); b_B = d* of it
            # cancelling: source dB for B a single-link 1-form; potential = G * (dB); b_A = d* of it
            # dB for B_0(0)=1 : (dB)_{0,nu}(x) = -[B_0(x+e_nu)-B_0(x)] = -(delta_{x+e_nu,0} - delta_{x,0})
            src = {}
            for nu in range(1, d):
                e = [0] * d; e[nu] = 1
                z0 = tuple(0 for _ in range(d))
                src[(z0, 0, nu)] = src.get((z0, 0, nu), 0.0) + 1.0
                key = tuple((-e[k]) % R for k in range(d))
                src[(key, 0, nu)] = src.get((key, 0, nu), 0.0) - 1.0
            def potA(x, m, n):
                s = 0.0
                for ((z, mm, nn), v) in src.items():
                    if (mm, nn) != (m, n):
                        continue
                    s += G[ix([x[k] - z[k] for k in range(d)])] * v
                return s
            def potB(x, m, n):
                return G[ix(x)] if (m, n) == (0, 1) else 0.0
            def dstar(pot, x):
                o = []
                for n in range(d):
                    s = 0.0
                    for m in range(d):
                        if m == n:
                            continue
                        a, b = (m, n) if m < n else (n, m)
                        sg = 1.0 if m < n else -1.0
                        em = [0] * d; em[m] = 1
                        s += sg * (pot([x[k] - em[k] for k in range(d)], a, b) - pot(x, a, b))
                    o.append(s)
                return o
            shA = {}; shB = {}
            step = 1
            for i in range(0, R ** d, step):
                x = [(i // (R ** (d - 1 - mu))) % R for mu in range(d)]
                r2 = sum(rep(v, R) ** 2 for v in x)
                if r2 == 0 or r2 > (R // 2) ** 2:
                    continue
                r = math.sqrt(r2); sh = int(math.floor(r))
                vA = max(abs(v) for v in dstar(potA, x))
                vB = max(abs(v) for v in dstar(potB, x))
                shA[sh] = max(shA.get(sh, 0.0), vA * r ** d)
                shB[sh] = max(shB.get(sh, 0.0), vB * r ** d)
            ks = sorted(set(shA) | set(shB))
            P("  gt1b-D (re-run of gt1-D at R=24, gt1 criteria untouched):")
            P("    shell s : rho_B (bare)        | rho_A (zero-mean source)")
            for s in ks:
                P("      s=%2d : %18.8f | %18.8f" % (s, shB.get(s, float('nan')), shA.get(s, float('nan'))))
            sB = [shB[s] for s in ks if s in shB]; sA = [shA[s] for s in ks if s in shA]
            incB = all(sB[i + 1] > sB[i] for i in range(len(sB) - 1))
            incA = all(sA[i + 1] > sA[i] for i in range(len(sA) - 1))
            P("    rho_B strictly increasing: %s ; rho_A strictly increasing: %s  -> %s"
              % (incB, incA, "PASS" if (incB and not incA) else "FAIL"))
            P("    ratio rho_B(max shell)/rho_B(s=2) = %.4f ; rho_A(max)/rho_A(2) = %.4f"
              % (sB[-1] / sB[1] if len(sB) > 1 else float('nan'),
                 sA[-1] / sA[1] if len(sA) > 1 else float('nan')))
    P("")
    P("gt2-E  R-uniformity:  M1(R) = max_s s^3|grad_1 G(s,0,0,0)| , M2(R) = max_{s>=2} s^4|grad_1^2 G|")
    for R in sorted(M1):
        P("   R=%2d : M1 = %.6f   M2 = %.6f" % (R, M1[R], M2[R]))
    g1 = M1[24] / M1[8]; g2 = M2[24] / M2[8]
    P("   growth 8 -> 24 :  M1 x%.4f , M2 x%.4f  -> %s"
      % (g1, g2, "PASS" if (g1 < 2.0 and g2 < 2.0) else "FAIL"))
    txt = "\n".join(out)
    print(txt)
    with open(sys.argv[1] if len(sys.argv) > 1 else "gt1_sweep_out.txt", "w") as f:
        f.write(txt + "\n")

if __name__ == "__main__":
    main()
