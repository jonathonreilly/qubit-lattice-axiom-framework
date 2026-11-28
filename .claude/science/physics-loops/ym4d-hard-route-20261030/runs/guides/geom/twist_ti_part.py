# GUIDE only. Pure-Python SU(2) Wilson twist ratio r = Z_tw/Z on L^4 by thermodynamic integration in the sheet coupling s (Lemma T4).
# -log r = beta*|S| * int_{-1}^{1} u(s) ds,  u(s) = mean of (1/2) tr U_p over the sheet at sheet coupling s*beta.
import sys, time, math, random
L = int(sys.argv[1]); beta = float(sys.argv[2]); nq = int(sys.argv[3]); ntherm = int(sys.argv[4]); nmeas = int(sys.argv[5]); seed = int(sys.argv[6])
n_lo = int(sys.argv[7]) if len(sys.argv) > 7 else 0
n_hi = int(sys.argv[8]) if len(sys.argv) > 8 else nq
walk_up = len(sys.argv) > 9 and sys.argv[9] == 'up'
rnd = random.Random(seed).random
V = L**4
def site(c): return ((c[0]%L)*L + (c[1]%L))*L*L + (c[2]%L)*L + (c[3]%L)
coords = [(a,b,c,d) for a in range(L) for b in range(L) for c in range(L) for d in range(L)]
def shift(c, m, k):
    c = list(c); c[m] += k; return site(c)
fwd = [[shift(c, m, 1) for c in coords] for m in range(4)]
bwd = [[shift(c, m, -1) for c in coords] for m in range(4)]
sheet = [c[0] == 0 and c[1] == 0 for c in coords]
sheet_sites = [x for x in range(V) if sheet[x]]
nS = len(sheet_sites)
def qmul(a, b):
    a0,a1,a2,a3 = a; b0,b1,b2,b3 = b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def qmulc(a, b):   # a * conj(b)
    a0,a1,a2,a3 = a; b0,b1,b2,b3 = b; b1=-b1; b2=-b2; b3=-b3
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def qcmul(a, b):   # conj(a) * b
    a0,a1,a2,a3 = a; a1=-a1; a2=-a2; a3=-a3; b0,b1,b2,b3 = b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
U = [[(1.0,0.0,0.0,0.0)]*V for _ in range(4)]
def sweep(sb):
    log = math.log; exp = math.exp; sqrt = math.sqrt; cos = math.cos; sin = math.sin; twopi = 2*math.pi
    for m in range(4):
        Um = U[m]; fm = fwd[m]
        for x in range(V):
            xm = fm[x]
            w0 = w1 = w2 = w3 = 0.0
            for n in range(4):
                if n == m: continue
                Un = U[n]; fn = fwd[n]; bn = bwd[n]
                inplane = (m + n == 1)
                c = sb if (inplane and sheet[x]) else beta
                a = qmulc(qmulc(Un[xm], Um[fn[x]]), Un[x])
                w0 += c*a[0]; w1 += c*a[1]; w2 += c*a[2]; w3 += c*a[3]
                xd = bn[x]
                c = sb if (inplane and sheet[xd]) else beta
                a = qmul(qcmul(Un[bn[xm]], (Um[xd][0], -Um[xd][1], -Um[xd][2], -Um[xd][3])), Un[xd])
                w0 += c*a[0]; w1 += c*a[1]; w2 += c*a[2]; w3 += c*a[3]
            k = sqrt(w0*w0 + w1*w1 + w2*w2 + w3*w3)
            if k < 1e-12:
                k = 1e-12; w0 = k; w1 = w2 = w3 = 0.0
            e2 = exp(-2*k)
            while True:
                t = 1.0 + log(e2 + rnd()*(1.0 - e2))/k
                v = rnd()
                if v*v <= 1.0 - t*t: break
            r = sqrt(max(0.0, 1.0 - t*t)); ct = 2*rnd() - 1; st = sqrt(1 - ct*ct); ph = twopi*rnd()
            X = (t, r*st*cos(ph), r*st*sin(ph), r*ct)
            Um[x] = qmulc(X, (w0/k, w1/k, w2/k, w3/k))
def plaq(m, n, x):
    return qmul(qmul(U[m][x], U[n][fwd[m][x]]), qcmul(U[m][fwd[n][x]], (U[n][x][0], -U[n][x][1], -U[n][x][2], -U[n][x][3])))[0]
def sheet_plaq(): return sum(plaq(0, 1, x) for x in sheet_sites)/nS
def bulk_plaq():  return sum(plaq(2, 3, x) for x in range(V))/V
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
nodes, weights = leggauss(nq)     # nodes in decreasing order, from near +1 to near -1
t0 = time.time(); us = []; es = []
sel = list(range(n_lo, n_hi))
if walk_up: sel = sel[::-1]
for s in [nodes[i] for i in sel]:
    sb = s*beta
    for _ in range(ntherm): sweep(sb)
    vals = []; pl = 0.0; npl = 0
    for i in range(nmeas):
        sweep(sb); vals.append(sheet_plaq())
        if i % 25 == 0: pl += bulk_plaq(); npl += 1
    nb = 10; bs = len(vals)//nb; b = [sum(vals[j*bs:(j+1)*bs])/bs for j in range(nb)]
    mean = sum(vals)/len(vals); bm = sum(b)/nb
    err = math.sqrt(sum((y - bm)**2 for y in b)/(nb - 1)/nb)
    us.append(mean); es.append(err)
    print("s=%+.5f u=%+.5f +- %.5f  bulk34=%.4f  t=%.0fs" % (s, mean, err, pl/npl, time.time() - t0), flush=True)
if len(sel) != nq or walk_up: sys.exit(0)
I = sum(w*u for w, u in zip(weights, us)); dI = math.sqrt(sum((w*e)**2 for w, e in zip(weights, es)))
Fv = beta*nS*I; dFv = beta*nS*dI
print("RESULT L=%d beta=%.3f |S|=%d nq=%d nmeas=%d  F_v=%.4f +- %.4f   r=%.4f  (one-sigma range %.4f .. %.4f)" % (L, beta, nS, nq, nmeas, Fv, dFv, math.exp(-Fv), math.exp(-Fv - dFv), math.exp(-Fv + dFv)), flush=True)
