"""C5 R16-5: W2_pf translation/strain moment checks (Lemma T_pf), pair channel, sawtooth escape.
Run: OMP_NUM_THREADS=2 python3 r165_tpf.py
Bands: R9-9 profiles G, L, NN (eps^2 = m^2 + u(k), per axis). No subtraction anywhere (raw values).
"""
import numpy as np
from r99_profiles_copy import profile, wrap
np.set_printoptions(precision=4)
N = 2**16
k = -np.pi + 2*np.pi*(np.arange(N)+0.5)/N
dk = 2*np.pi/N

def symbols(band, m):
    u, up, upp = profile(band, k)
    eps = np.sqrt(m*m + u)
    v = up/(2*eps)
    syms = {
        'p=eps*v=u\'/2 (R8-2 fwd value)': up/2,
        'sin k': np.sin(k),
    }
    return eps, v, syms

def saw_smooth(kk, delta):
    # Pi = k on |k|<=pi-delta, smooth odd periodic return across the face (C-infinity blend)
    from r99_profiles_copy import sstep
    kw = wrap(kk); a = np.abs(kw)
    r = sstep((np.pi - a)/delta)          # 1 inside, ->0 at the face
    return r*kw + (1-r)*np.sin(kw)*0.0 + (1-r)*0.0 + r*0  # = r*k : odd, periodic, smooth (r->0 at face)

print("=== (1) Lemma T_pf: zone mean of dPi/dk and finite-q averaging identity ===")
for band in ['G', 'L', 'NN']:
    for m in [1.0, 0.3]:
        eps, v, syms = symbols(band, m)
        syms = dict(syms)
        for d in [0.5, 0.1]:
            syms['smoothed sawtooth delta=%.1f' % d] = saw_smooth(k, d)
        for name, Pi in syms.items():
            dPi = (np.roll(Pi,-1)-np.roll(Pi,1)); dPi = np.where(np.abs(dPi)>np.pi, dPi-2*np.pi*np.sign(dPi), dPi)/(2*dk)  # periodic central diff; a 2pi jump is a -2pi*delta at the face
            mean_dPi = dPi.mean()
            # set where Pi' differs from 1 (true translation) by > 1e-6
            frac_bad = np.mean(np.abs(dPi - 1) > 1e-6)
            # finite q: Pi(k+q)-Pi(k) averaged over the zone (must equal theta(q) if identity held)
            out = []
            for q in [0.01, 0.1, 1.0]:
                s = int(round(q/dk))
                diff = np.roll(Pi, -s) - Pi
                out.append((q, diff.mean(), diff.max()-diff.min()))
            # weighted best theta'(0) from the T00 identity Pi' eps = c eps: c = <Pi' eps>/<eps>
            print(f"{band} m={m} {name:34s} <Pi'>={mean_dPi:+.2e} frac|Pi'-1|>1e-6={frac_bad:.3f} " +
                  " ".join(f"[q={q}: <dPi>={a:+.1e}, spread={b:.2e}]" for q, a, b in out))
        u_, up_, _ = profile(band, k)
        vb = np.sqrt(np.max(up_**2/(4*np.maximum(u_,1e-300))))
        print(f"{band} m={m} whole-zone v_max: per axis at this m = {np.abs(v).max():.4f}; any-d, any-m bound sup|u'|/(2 sqrt u) = {vb:.4f} (|v|^2 = sum u_i'^2/4(m^2+sum u_i) <= max_i u_i'^2/4u_i)")
print()

print("=== (2) forward-limit identity F^{ij}(k,k) = v_i pi_j from W1_pf (nu=j), 1D check ===")
# W1_pf: omega F0(k,k+q) = D(q) Fxx(k,k+q); omega = eps(k+q)-eps(k), D = 2 sin(q/2) e^{iq/2} -> forward ratio
for band in ['G', 'L']:
    m = 0.3
    u, up, upp = profile(band, k); eps = np.sqrt(m*m+u); v = up/(2*eps); pi = up/2
    Fxx_fwd = v*pi    # candidate forward spatial stress
    for q in [1e-3, 1e-4]:
        s = q
        u2, up2, _ = profile(band, k+s); eps2 = np.sqrt(m*m+u2)
        om = eps2 - eps
        D = 2*np.sin(s/2)
        F0 = D*Fxx_fwd/om   # what W1_pf returns for F^{0x}(k,k+q) if F^{xx}(k,k+q) ~ v pi
        mask = np.abs(v) > 1e-3
        print(f"{band} q={q:g}: max|F0x - pi| / max|pi| on |v|>1e-3 = {np.max(np.abs(F0-pi)[mask])/np.max(np.abs(pi)):.2e}")
print()

print("=== (3) pair channel: first moment of F^{0x}_pair is nonzero, but [B,P]=0 since pi(k)+pi(-k)=0 ===")
for band in ['G', 'L']:
    for m in [1.0, 0.3]:
        u, up, upp = profile(band, k); eps = np.sqrt(m*m+u); pi = up/2
        # continuum-minimal-like smooth spatial pair kernel F^{xx}_pair(k,-k) ~ -k1 k2/(2 sqrt(e1 e2)) -> s(k)^2/(2 eps) with s = pi/eps*... use generic smooth: w(k)=pi(k)
        Fxx_pair = pi*pi/(2*eps)        # smooth, even
        b = Fxx_pair/(2*eps)           # i d/dq [D(q) Fxx/omega] at q=0, omega=2 eps, dD/dq(0)=1
        odd_res = np.max(np.abs(pi + pi[::-1]))
        print(f"{band} m={m}: max|b(k)| (pair part of M_xx) = {np.abs(b).max():.3e}; max|pi(k)+pi(-k)| = {odd_res:.1e} -> [B,P_x] = 0")
print()

print("=== (4) sawtooth escape: raw Fourier coefficients of the momentum symbol (nothing subtracted) ===")
Nf = 2**14
kf = -np.pi + 2*np.pi*(np.arange(Nf)+0.5)/Nf
def coeffs(Pi):
    c = np.fft.fft(Pi)/len(Pi)
    return np.abs(c)
saw = wrap(kf)
for name, Pi in [('sawtooth (exact crystal momentum)', saw),
                 ('smoothed sawtooth delta=0.5', saw_smooth(kf, 0.5)),
                 ('smoothed sawtooth delta=0.1', saw_smooth(kf, 0.1)),
                 ('G: u\'/2 at m=0.3', profile('G', kf)[1]/2)]:
    c = coeffs(Pi)
    print(f"{name:36s} |c_n| at n=10,50,200,1000: " + ", ".join(f"{c[n]:.2e}" for n in [10, 50, 200, 1000]))
    h = 2*np.pi/Nf
    dPi = (np.roll(Pi,-1)-Pi)/h   # forward periodic difference: a jump of -2pi shows up as one cell of size -2pi/h
    strip = np.abs(dPi-1) > 1e-6
    print(f"{'':36s} integral of (Pi'-1) over the zone (periodic difference, jump included) = {np.sum(dPi-1)*h:+.4f} (expect -2pi = {-2*np.pi:+.4f}); anomaly set measure = {strip.mean()*2*np.pi:.4f}")
print("sawtooth n*|c_n| at n=10,100,1000:", [round(n*coeffs(saw)[n], 4) for n in [10, 100, 1000]], "(=1 -> |c_n| = 1/n, 1/r tail along each axis)")
print()

print("=== (5) cubic-covariant component mixing (separable, 1D): Pi' eps = c eps + e v Pi  ->  c * oint eps^{-e} = 0 ===")
for band in ['G', 'L', 'NN']:
    m = 0.3
    u, up, upp = profile(band, k); eps = np.sqrt(m*m+u)
    for e in [-2, -1, 0, 1, 2, 5]:
        I = np.sum(eps**(-e))*dk
        print(f"{band} m={m} e={e:+d}: oint eps^(-e) dk = {I:.4e} (>0, so c = 0 forced)")

print()
print("=== (6) nested chi-cut attempt: generator symbol g = k*c(k) (edge decoupled smoothly); identity g(k+q)-g(k) = theta(q) on {F^{0j}(k,k+q) != 0} ===")
from r99_profiles_copy import sstep
for (a, b) in [(2.0, 2.6), (2.5, 3.0), (2.9, 3.1)]:
    kw = wrap(k); r = sstep((b - np.abs(kw))/(b - a))   # c = 1 for |k|<=a, 0 for |k|>=b
    g = kw*r
    for q in [0.01, 0.001]:
        s = int(round(q/dk)); qq = s*dk
        diff = np.roll(g, -s) - g
        supp = (np.abs(g) > 1e-12) & (np.abs(np.roll(g, -s)) > 1e-12)   # F^{0j}(k,k+q) ~ g continuity: nonzero here
        res = diff[supp] - qq
        print(f"c=1 on |k|<={a}, 0 beyond {b}: q={qq:.4g}: max_k |g(k+q)-g(k)-q| on support = {np.abs(res).max():.3e} "
              f"(= {np.abs(res).max()/qq:.2f} q); best constant theta: spread of g(k+q)-g(k) on support = {diff[supp].max()-diff[supp].min():.3e}")
print("A continuous g that equals k on the box must return to 0 somewhere on the coupled set: the identity fails there at O(q).")

print()
print("=== (7) mixing in the T^{0x} identity (1D separable): g' = c + e*v (T^{xx} mixing; T^{00} mixing killed by C2 parity) -> oint: 2pi c + e*oint v = 0 ===")
for band in ['G', 'L', 'NN']:
    for m in [1.0, 0.3]:
        u, up, upp = profile(band, k); eps = np.sqrt(m*m+u); v = up/(2*eps)
        print(f"{band} m={m}: oint v dk = {np.sum(v)*dk:+.2e}  (=0: periodic eps) -> c = 0 for every e")
