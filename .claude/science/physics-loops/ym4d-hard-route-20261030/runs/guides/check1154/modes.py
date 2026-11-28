# GUIDE only (pure Python). (a) G_r on the free-boundary square; (b) the box mode
# sum of (6) against pi^2/8; (c) multiplicity r(q)-1 of the transverse spectrum.
import math, itertools

def f(x):
    return math.log((1 + math.exp(-x)) / (1 - math.exp(-x)))

# (a) G_r = <d0,(I+Lap_r/4)^{-1} d0> on [-r,r]^2, free boundary, by CG
def G_r(r):
    n = 2 * r + 1
    def A(x):
        y = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                s = x[i][j]
                lap = 0.0
                for (a, b) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= a < n and 0 <= b < n:
                        lap += x[i][j] - x[a][b]
                y[i][j] = s + lap / 4
        return y
    b = [[0.0] * n for _ in range(n)]; b[r][r] = 1.0
    x = [[0.0] * n for _ in range(n)]
    res = [row[:] for row in b]; p = [row[:] for row in res]
    rr = sum(v * v for row in res for v in row)
    for _ in range(2000):
        Ap = A(p)
        alpha = rr / sum(p[i][j] * Ap[i][j] for i in range(n) for j in range(n))
        for i in range(n):
            for j in range(n):
                x[i][j] += alpha * p[i][j]; res[i][j] -= alpha * Ap[i][j]
        rr2 = sum(v * v for row in res for v in row)
        if rr2 < 1e-28:
            break
        beta = rr2 / rr; rr = rr2
        for i in range(n):
            for j in range(n):
                p[i][j] = res[i][j] + beta * p[i][j]
    return x[r][r]

for r in (1, 2, 3, 5, 8, 12):
    g = G_r(r)
    print("r=%2d G_r=%.10f eta_r=%.6f (>= 24/29=%.6f for r>=2)" % (r, g, 1 / g - 1, 24 / 29))

# (b) per-box normalized mode sum m^3/(b1 b2 b3) * 3 * sum (r(q)-1) f(m w_q)
def box_sum(bs, m):
    tot = 0.0
    s = [[4 * math.sin(math.pi * q / (2 * b))**2 for q in range(b)] for b in bs]
    for q1 in range(bs[0]):
        for q2 in range(bs[1]):
            l12 = s[0][q1] + s[1][q2]
            for q3 in range(bs[2]):
                rq = (q1 > 0) + (q2 > 0) + (q3 > 0)
                if rq < 2:
                    continue
                lam = l12 + s[2][q3]
                w = 2 * math.asinh(math.sqrt(lam) / 2)
                x = m * w
                if x > 40:
                    continue
                tot += (rq - 1) * f(x)
    return m**3 / (bs[0] * bs[1] * bs[2]) * 3 * tot

print("pi^2/8 =", math.pi**2 / 8)
for (bs, m) in (((60, 61, 60), 2), ((60, 61, 60), 4), ((60, 61, 60), 6), ((120, 121, 120), 4), ((120, 121, 120), 8)):
    print("box", bs, "m", m, "normalized sum", box_sum(bs, m))
