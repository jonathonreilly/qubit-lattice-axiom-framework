"""GUIDE check for row 1085: tests the pillow-graph coefficient formula by the exact Gram identity
<L, L'> = sum_P [P in JI x JI'][P in JII x JII'][P in a x a'][P in b x b'] / d_P^2.
L(JI, JII, a, b) = chi_JI(side I) chi_JII(side II) chi_a(bottom) chi_b(top) on the pillow graph.
All spins doubled. sixj copied from runs/gap-descent-sign/su2box.py (row 1081)."""
import math, itertools, random, sys

def lf(n): return math.lgamma(n + 1)
def tri(a, b, c): return 0.5 * (lf((a+b-c)//2) + lf((a-b+c)//2) + lf((-a+b+c)//2) - lf((a+b+c)//2 + 1))
def ok(a, b, c): return (a+b+c) % 2 == 0 and abs(a-b) <= c <= a+b
def sixj(a, b, c, d, e, f):
    if not (ok(a,b,c) and ok(a,e,f) and ok(d,b,f) and ok(d,e,c)): return 0.0
    pre = tri(a,b,c) + tri(a,e,f) + tri(d,b,f) + tri(d,e,c)
    t1, t2, t3, t4 = (a+b+c)//2, (a+e+f)//2, (d+b+f)//2, (d+e+c)//2
    s1, s2, s3 = (a+b+d+e)//2, (b+c+e+f)//2, (a+c+d+f)//2
    tot = 0.0
    for z in range(max(t1,t2,t3,t4), min(s1,s2,s3)+1):
        tot += (-1)**z * math.exp(pre + lf(z+1) - lf(z-t1) - lf(z-t2) - lf(z-t3) - lf(z-t4) - lf(s1-z) - lf(s2-z) - lf(s3-z))
    return tot

def coefs(JI, JII, a, b):
    """dict state -> coefficient; state = (j, j', k, k', sx, sy), doubled."""
    out = {}
    ss = [s for s in range(abs(JI-JII), JI+JII+1, 2)]
    js = [j for j in range(abs(JI-b), JI+b+1, 2)]
    jps = [j for j in range(abs(JII-b), JII+b+1, 2)]
    ks = [j for j in range(abs(JI-a), JI+a+1, 2)]
    kps = [j for j in range(abs(JII-a), JII+a+1, 2)]
    for j, jp, k, kp, sx, sy in itertools.product(js, jps, ks, kps, ss, ss):
        v = (sixj(j, jp, sx, JII, JI, b) * sixj(j, jp, sy, JII, JI, b) *
             sixj(k, kp, sx, JII, JI, a) * sixj(k, kp, sy, JII, JI, a))
        if v != 0.0:
            out[(j, jp, k, kp, sx, sy)] = math.sqrt((j+1)*(jp+1)*(k+1)*(kp+1)*(sx+1)*(sy+1)) * v
    return out

def gram_exact(L, Lp):
    tot = 0.0
    for P in range(0, 200):
        if all(ok(x, y, P) for x, y in zip(L, Lp)): tot += 1.0 / (P+1)**2
    return tot

if __name__ == '__main__':
    random.seed(1)
    mx = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    worst = 0.0; cnt = 0; nonsq = 0
    labels = list(itertools.product(range(mx+1), repeat=4))
    pairs = [(L, L) for L in labels] + [(random.choice(labels), random.choice(labels)) for _ in range(3000)]
    for L, Lp in pairs:
        c1 = coefs(*L); c2 = coefs(*Lp)
        g = sum(v * c2.get(s, 0.0) for s, v in c1.items())
        nonsq += sum(1 for s, v in c1.items() if v < 0)
        e = abs(g - gram_exact(L, Lp)); worst = max(worst, e); cnt += 1
        if e > 1e-9: print("MISMATCH", L, Lp, g, gram_exact(L, Lp))
    print(f"max doubled spin {mx}: {cnt} Gram pairs, worst error {worst:.2e}, negative coefficients seen {nonsq}")
