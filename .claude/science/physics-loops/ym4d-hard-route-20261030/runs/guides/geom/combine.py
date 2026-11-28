# GUIDE only. Combine per-node lines of several partial logs into F_v by Gauss-Legendre.
import sys, math, re
L = int(sys.argv[1]); beta = float(sys.argv[2]); nq = int(sys.argv[3]); files = sys.argv[4:]
def leggauss(n):
    xs = []; ws = []
    for i in range(1, n+1):
        x = math.cos(math.pi*(i - 0.25)/(n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n+1): p0, p1 = p1, ((2*k-1)*x*p1 - (k-1)*p0)/k
            dp = n*(x*p1 - p0)/(x*x - 1); dx = p1/dp; x -= dx
            if abs(dx) < 1e-15: break
        xs.append(x); ws.append(2/((1 - x*x)*dp*dp))
    return xs, ws
nodes, weights = leggauss(nq)
data = {}
for f in files:
    for ln in open(f):
        m = re.match(r's=([+-][0-9.]+) u=([+-][0-9.]+) \+- ([0-9.]+)', ln)
        if m: data.setdefault(round(float(m.group(1)), 5), []).append((float(m.group(2)), float(m.group(3))))
I = 0.0; v = 0.0
for s, w in zip(nodes, weights):
    lst = data[round(s, 5)]
    u = sum(a for a, _ in lst)/len(lst); e = math.sqrt(sum(b*b for _, b in lst))/len(lst)
    I += w*u; v += (w*e)**2
nS = L*L; Fv = beta*nS*I; dFv = beta*nS*math.sqrt(v)
print("COMBINED L=%d beta=%.3f |S|=%d nq=%d  F_v=%.4f +- %.4f  r=%.4f (one-sigma range %.4f .. %.4f)" % (L, beta, nS, nq, Fv, dFv, math.exp(-Fv), math.exp(-Fv-dFv), math.exp(-Fv+dFv)))
