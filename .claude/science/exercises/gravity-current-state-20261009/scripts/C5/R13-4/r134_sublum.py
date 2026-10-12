"""R13-4 (iii) addendum: an explicitly subluminal box symbol (b < pi/2) and its leakage.
s' = sigma: 1 on [0,b], symmetric Gevrey-2 step to -1 over [b, pi-b], -1 on [pi-b, pi]; sigma even, 2pi-periodic.
Then s = int_0^k sigma is C^inf, odd, periodic, s = k on |k| <= b, |s'| <= 1, s(pi) = 0.
Same subtraction as r134_cone.py: D_cont = 0 outside the cone, so the leakage is D itself."""
import numpy as np

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def make_s(b, n=2**16):
    k = np.linspace(0, np.pi, n+1)
    sig = 1 - 2*sstep((k - b)/(np.pi - 2*b))
    s = np.concatenate([[0], np.cumsum(0.5*(sig[1:] + sig[:-1])*np.diff(k))])
    def S(q):
        q = -(((-q) + np.pi) % (2*np.pi) - np.pi)
        return np.sign(q)*np.interp(np.abs(q), k, s)
    def dS(q):
        q = -(((-q) + np.pi) % (2*np.pi) - np.pi)
        return np.interp(np.abs(q), k, sig)
    return S, dS, s[-1], np.max(np.abs(s[k <= b] - k[k <= b]))

out = []
def pr(*a):
    s_ = " ".join(str(x) for x in a); print(s_, flush=True); out.append(s_)

NQ = 2**21
kq = (np.arange(NQ) + 0.5)*2*np.pi/NQ - np.pi
def Dfun(E, r, t):
    w = np.sin(E*t)/np.where(E > 0, E, 1.0); w = np.where(E > 0, w, t)
    return np.array([np.sum(np.cos(kq*ri)*w)/NQ for ri in r])

for b in [1.2, 1.4, 1.5]:
    S, dS, s_pi, err = make_s(b)
    for m in [0.3, 0.01]:
        k = np.linspace(-np.pi, np.pi, 240, endpoint=False) + np.pi/240
        sv, dv = S(k), dS(k)
        best = 0
        for a in range(len(k)):
            E = np.sqrt(m*m + sv[a]**2 + sv[:, None]**2 + sv[None, :]**2)
            g = np.sqrt((sv[a]*dv[a])**2 + (sv*dv)[:, None]**2 + (sv*dv)[None, :]**2)/E
            best = max(best, g.max())
        k1 = np.linspace(-np.pi, np.pi, 200001)
        v1 = np.max(np.abs(S(k1)*dS(k1))/np.sqrt(m*m + S(k1)**2))
        pr(f"b={b}, m={m}: s(pi)={s_pi:.1e}, max|s-k| on box={err:.1e}, max|s'|={np.max(np.abs(dS(k1))):.4f}; "
           f"v_max d=1 {v1:.4f}, d=3 {best:.4f}")
pr("\nLeakage outside the c=1 cone, d=1, b=1.4, m=0.3 (x = r - t; max |D| over 4 sites)")
S, dS, _, _ = make_s(1.4)
E = np.sqrt(0.09 + S(kq)**2)
xs = [1, 2, 5, 10, 20, 40, 80, 160, 320]
for t in [100, 400, 1600]:
    vals = [np.max(np.abs(Dfun(E, t + x + np.arange(4), t))) for x in xs]
    pr(f"  t={t:5d}: " + " ".join(f"{v:.1e}" for v in vals))
pr("  same, massless m=0 (photon-like single band with b=1.4):")
E0 = np.abs(S(kq))
for t in [100, 400, 1600]:
    vals = [np.max(np.abs(Dfun(E0, t + x + np.arange(4), t))) for x in xs]
    pr(f"  t={t:5d}: " + " ".join(f"{v:.1e}" for v in vals))
with open(__file__.replace('.py', '.out'), 'w') as f:
    f.write("\n".join(out) + "\n")
