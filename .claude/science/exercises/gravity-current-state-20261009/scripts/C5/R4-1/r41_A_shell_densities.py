"""R4-1 (A): exact ensemble shell densities C_m of L7-LRL (Siegel product of local densities),
checked against direct lattice-frame counts.

Q(n) = -7 n0^2 + n1^2 + n2^2 + n3^2, physical x = (sqrt7 n0, n1, n2, n3), rho = 1/sqrt7.
Ensemble mean of sum_{v in gL7, future, x^2=-m} h(v) = C_m * int theta(x0) delta(x^2+m) h(x) d^4x   (R3-3 Sec 2.1 unfolding).
Siegel (indefinite, rank 4, one class per genus assumed -> checked numerically below):
   C_m = rho * prod_p alpha_p(Q, -m),   alpha_p = lim p^{-3r} #{n mod p^r : Q(n) = -m mod p^r}.
For p not dividing 14 m: alpha_p = 1 - chi(p)/p^2 with chi = (-7/.) = (./7).
"""
import numpy as np, sys
M = int(sys.argv[1]) if len(sys.argv) > 1 else 128
rho = 1/np.sqrt(7)

def chi(p):
    r = p % 7
    if r == 0: return 0
    return 1 if r in (1, 2, 4) else -1

def primes_upto(n):
    s = np.ones(n+1, bool); s[:2] = False
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def alpha_p(p, t, r):
    q = p**r
    x = np.arange(q, dtype=np.int64)
    sq = np.bincount((x*x) % q, minlength=q).astype(float)          # distribution of x^2 mod q
    s0 = np.bincount((-7*x*x) % q, minlength=q).astype(float)       # distribution of -7 x^2 mod q
    def cconv(a, b):
        return np.rint(np.real(np.fft.ifft(np.fft.fft(a)*np.fft.fft(b)))).astype(float)
    d = cconv(cconv(cconv(s0, sq), sq), sq)
    return d[t % q] / float(q)**3

def vp(p, n):
    v = 0
    while n % p == 0: n //= p; v += 1
    return v

# L(2, chi) by direct summation (character sum bounded -> tail O(1/N^2))
Nsum = 4_000_000
n = np.arange(1, Nsum+1); ch = np.array([0, 1, 1, -1, 1, -1, -1])[n % 7]
L2 = float(np.sum(ch/n.astype(float)**2))
P = primes_upto(4*M)
C = np.zeros(M+1)
for m in range(1, M+1):
    t = -m
    val = rho/L2                       # prod over ALL p of generic factor (1-chi/p^2) = 1/L(2,chi)
    for p in [int(p) for p in P if (14*m) % p == 0]:
        gen = 1 - chi(p)/p**2
        v = vp(p, m)
        if p in (2, 3, 5, 7):
            rr = v + (5 if p == 2 else 3)
            a1 = alpha_p(p, t, rr); a2 = alpha_p(p, t, rr+1)
            assert abs(a1-a2) < 1e-12, (m, p, a1, a2)
            if p in (3, 5):   # check the textbook formula where brute force is cheap
                af = gen*sum((chi(p)/p)**i for i in range(v+1))
                assert abs(a1-af) < 1e-12, (m, p, a1, af)
        else:
            a1 = gen*sum((chi(p)/p)**i for i in range(v+1))
        val *= a1/gen
    C[m] = val
np.save('C_siegel.npy', C)
print(f"L(2,chi_-7) = {L2:.12f}")
print("m  C_m(Siegel)")
for m in range(1, M+1):
    print(f"{m:4d} {C[m]:.10f}", end=('\n' if m % 4 == 0 else '   '))
print(f"\nmean C_m over m=1..{M}: {C[1:].mean():.5f}   (rho = {rho:.5f})")

# --- check: lattice-frame counts N_m(T) = sum_{n0<=T} r3(7 n0^2 - m) vs C_m * hyperboloid measure
T = int(sys.argv[2]) if len(sys.argv) > 2 else 600
Nmax = 7*T*T
r1 = np.zeros(Nmax+1); k = np.arange(0, int(np.sqrt(Nmax))+1); r1[k*k] += 1; r1[k[1:]**2] += 1
def lin_conv(a, b, nmax):
    L = 1
    while L < 2*(nmax+1): L *= 2
    out = np.fft.irfft(np.fft.rfft(a, L)*np.fft.rfft(b, L), L)[:nmax+1]
    return np.rint(out)
r2 = lin_conv(r1, r1, Nmax); r3 = lin_conv(r2, r1, Nmax)
assert r3[1] == 6 and r3[2] == 12 and r3[3] == 8 and r3[7] == 0
def hyp_measure(Tph, m):
    R = np.sqrt(Tph**2 - m)
    return np.pi*(R*Tph - m*np.log((R+Tph)/np.sqrt(m)))
print(f"\ncheck vs lattice-frame counts, n0 <= T (T = {T//2}, {T}):  ratio = N_m(T)/(C_m * hyperboloid measure)")
n0 = np.arange(1, T+1)
for m in [1, 2, 3, 4, 5, 6, 7, 8, 11, 14, 15, 16, 21, 28, 31, 49, 63, 64, 96, 112, 127]:
    if m > M: continue
    out = []
    for TT in (T//2, T):
        idx = 7*n0[:TT]**2 - m
        cnt = r3[idx].sum()
        out.append(cnt/(C[m]*hyp_measure(np.sqrt(7)*TT, m)))
    print(f"m={m:4d}  C_m={C[m]:.6f}  ratio(T/2)={out[0]:.5f}  ratio(T)={out[1]:.5f}")
