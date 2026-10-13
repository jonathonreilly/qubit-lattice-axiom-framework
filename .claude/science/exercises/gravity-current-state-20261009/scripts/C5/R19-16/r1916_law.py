"""R19-16 (R0, R1) checks of the analytic law and the uniform divided difference against 40-digit mpmath references;
and the size of (analytic - archived tabulated) law at the archived evaluators' sample points."""
import sys, time, numpy as np, mpmath as mp
import lib1916 as R
L = R.L
mp.mp.dps = 40
t0 = time.time(); rng = np.random.default_rng(1916)
b = mp.mpf(R.BG); w = mp.pi - b
def sstep_mp(t):
    t = mp.mpf(t)
    if t <= 0: return mp.mpf(0)
    if t >= 1: return mp.mpf(1)
    e1, e2 = mp.e**(-1/t), mp.e**(-1/(1 - t)); return e1/(e1 + e2)
def d_mp(x):
    x = mp.mpf(x)
    if x <= b: return x
    return x - w*mp.quad(sstep_mp, [0, (x - b)/w])
def sig_mp(k):
    k = mp.mpf(k)
    # wrap to (-pi, pi]
    while k > mp.pi: k -= 2*mp.pi
    while k <= -mp.pi: k += 2*mp.pi
    return mp.sign(k)*d_mp(abs(k))
def c_mp(k):
    return 1 - sstep_mp((abs(mp.mpf(k)) - b)/w)

print(f'law {R.AnalyticPhotonLaw().name}; S(1) = {R.S_of_u(np.array([1.0]))[0]!r} (exact 1/2 by sstep(t)+sstep(1-t)=1)')
# (R0) sigma and c vs mpmath
ks = np.r_[rng.uniform(R.BG, np.pi, 60), rng.uniform(-np.pi, np.pi, 40), [R.BG, np.pi, -np.pi, 3.05, 3.1415, 0.0]]
es = max(abs(float(R.sig(np.array([k]))[0] - sig_mp(k))) for k in ks)
ec = max(abs(float(R.cfun(np.array([k]))[0] - c_mp(k))) for k in ks)
print(f'[R0] analytic sigma vs 40-digit reference, {len(ks)} points (60 in the transition): max abs err {es:.2e}; c: {ec:.2e}')
# sigma' = c (finite difference, 4th order) in the transition
h = 1e-3; kk = rng.uniform(R.BG + 0.01, np.pi - 0.01, 200)
fd = (-R.sig(kk + 2*h) + 8*R.sig(kk + h) - 8*R.sig(kk - h) + R.sig(kk - 2*h))/(12*h)
print(f'     sigma\' - c (4th-order FD, h=1e-3, 200 pts in transition): max {np.abs(fd - R.cfun(kk)).max():.1e} (FD truncation ~h^4)')

# (R1) uniform divided difference vs mpmath (sigma1^2 - sigma2^2)/dsym(q), all scales of q, incl. transition, faces, box edge
def dd_mp(k1, k2):
    q = float(L.wrap(np.array([k1 - k2]))[0]); dq = mp.mpf(float(L.dsym(np.array([q]))[0]))
    if q == 0: return None
    if abs(q) <= 1: dq = mp.mpf(k1) - mp.mpf(k2)      # dsym = q exactly; avoid rounding of k1-k2 in the reference
    while dq > mp.pi: dq -= 2*mp.pi
    while dq <= -mp.pi: dq += 2*mp.pi
    if abs(q) > 1: dq = mp.mpf(float(L.dsym(np.array([q]))[0]))
    return (sig_mp(k1)**2 - sig_mp(k2)**2)/dq
cases = []
for _ in range(60):   # transition interior, tiny to moderate q
    k2 = rng.uniform(R.BG, np.pi); cases.append((k2 + 10**rng.uniform(-12, -0.7)*rng.choice([-1, 1]), k2))
for _ in range(30):   # straddling the box edge b
    q = 10**rng.uniform(-10, -0.7); cases.append((R.BG + q*rng.uniform(), R.BG - q*rng.uniform()))
for _ in range(30):   # straddling the BZ face (wrapped)
    q = 10**rng.uniform(-10, -0.7); cases.append((np.pi - q*rng.uniform(), -np.pi + q*rng.uniform()))
for _ in range(30):   # box, and large q
    cases.append((rng.uniform(-np.pi, np.pi), rng.uniform(-np.pi, np.pi)))
cases += [(3.05 + 0.5e-7, 3.05 - 0.5e-7), (3.05 + 0.4995e-7, 3.05 - 0.4995e-7), (3.05 + 0.5005e-7, 3.05 - 0.5005e-7)]
cases += [(2.8 + R.QREF, 2.8), (3.0 + R.QREF - 2*np.pi, 3.0), (2.0, 1.0 - 1e-12), (2.0, 1.0 + 1e-12), (-3.0, 3.0), (3.1, -3.1), (0.0, np.pi), (0.0, -np.pi), (np.pi, 0.0), (1e-300, np.pi), (2.0, 2.0 - np.pi), (R.BG, R.BG - np.pi)]   # incl. the tie |q| = pi
err = 0.0; worst = None
for k1, k2 in cases:
    ref = dd_mp(k1, k2)
    if ref is None: continue
    v = R.dd1(k1, k2); e = abs(float(v - ref))
    if e > err: err, worst = e, (k1, k2, v, float(ref))
print(f'[R1] uniform Delta vs 40-digit reference, {len(cases)} segments (q from 1e-12 to pi; transition, box edge, BZ face,'
      f' |q| = 1 plateau edge, |q| = pi tie, referee seam): max abs err {err:.2e} at {worst}')
# uniform formula vs direct quotient; continuity across the old 1e-7 switch, and the q = 0 limit
def both_forms(k1, k2):        # the two representations evaluated at the SAME point
    qs = R.QS; R.QS = 10.0; a = R.dd1(k1, k2); R.QS = -1.0; b = R.dd1(k1, k2); R.QS = qs; return abs(a - b)
jq = 0.0
for _ in range(400):
    k2 = rng.uniform(-np.pi, np.pi); q = rng.choice([-1, 1])*rng.uniform(0.1, np.pi)
    jq = max(jq, both_forms(float(L.wrap(np.array([k2 + q]))[0]), k2))
j7 = abs(R.dd1(3.05 + 0.5*0.999e-7, 3.05 - 0.5*0.999e-7) - R.dd1(3.05 + 0.5*1.001e-7, 3.05 - 0.5*1.001e-7))
lim = max(abs(R.dd1(k + 1e-12, k - 1e-12) - R.dd1(k, k)) for k in rng.uniform(-np.pi, np.pi, 200))
print(f'     integral form - direct form at the same point, 400 pairs with |q| in [0.1, pi] (incl. transition/faces): max {jq:.1e}; across the old 1e-7 switch: {j7:.1e} '
      f'(old lib199: 1.49e-5 kernel jump); |Delta(q=2e-12) - Delta(q=0)| max over 200 k: {lim:.1e}')

# size of (analytic - archived tabulated) law at the archived evaluators' sample points
tab = L.LAW
for name, kk in (('kgrid(224)', (np.arange(224) + 0.5)*2*np.pi/224 - np.pi), ('kgrid(96)', (np.arange(96) + 0.5)*2*np.pi/96 - np.pi),
                 ('samples(2^14)', (np.arange(1 << 14) + 0.5)*2*np.pi/(1 << 14) - np.pi), ('dense 2e5', np.linspace(-np.pi, np.pi, 200001))):
    ds = np.abs(R.sig(kk) - tab.sig(kk)).max(); dc = np.abs(R.cfun(kk) - tab.c(kk)).max()
    print(f'[R0] analytic - archived table at {name:14s}: max|d sigma| {ds:.2e}, max|d c| {dc:.2e}')
print(f'time {time.time() - t0:.0f}s')
