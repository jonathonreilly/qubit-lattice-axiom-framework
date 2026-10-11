"""Design B (flow the free part AND the normal interaction, leave the umklapp part unflowed; T2, sawtooth flow, KG m=1):
E^(2)/V = -(lam^2/24)[ I_N (h-independent) + 2 eps_U I_X(h) + eps_U^2 I_U(h) ],
I_X(h) = weight of normal 4-tuples k' (flowed frame) whose image Phi_h k' is lab-umklapp (a leg crosses a zone face).
Monte Carlo over normal 4-tuples with the exact t-integrated weight 1/(sum w * prod 2w)."""
import numpy as np, time
t0 = time.time()
def saw(k): return (k + np.pi) % (2*np.pi) - np.pi
def w(k): return np.sqrt(1.0 + 4*np.sum(np.sin(k/2)**2, axis=-1))
rng = np.random.default_rng(11)
def flowT2(k, eps, nsteps=100):
    x, y = k[..., 0].copy(), k[..., 1].copy(); h = 1.0/nsteps
    for _ in range(nsteps):
        xm = saw(x + 0.5*h*eps*saw(y)); ym = saw(y + 0.5*h*eps*saw(x))
        x = saw(x + h*eps*saw(ym)); y = saw(y + h*eps*saw(xm))
    out = k.copy(); out[..., 0] = x; out[..., 1] = y
    return out
Ntot = 0; acc = {e: [] for e in [0.01, 0.02, 0.04, 0.08]}; IN = []
for batch in range(8):
    N = 400000
    k = rng.uniform(-np.pi, np.pi, size=(N, 3, 3))
    k4 = -k.sum(1)
    ok = np.all(np.abs(k4) < np.pi, axis=1)
    kk = np.concatenate([k, k4[:, None, :]], axis=1)          # (N,4,3), normal by construction where ok
    W = np.where(ok, 1.0/(w(kk).sum(1)*np.prod(2*w(kk), axis=1)), 0.0)
    IN.append(W.mean())
    for e in acc:
        f = flowT2(kk, e)
        n_lab = np.round(f.sum(1)/(2*np.pi))                      # unwrapped sum of wrapped flowed legs / 2pi
        cross = ok & np.any(n_lab != 0, axis=1)
        acc[e].append(np.where(cross, W, 0.0).mean())
    Ntot += N
IN = np.array(IN); print(f"MC I_N = {IN.mean():.4e} +- {IN.std()/np.sqrt(len(IN)):.1e}  (convolution value 6.18e-05; MC measure is (2pi)^-9 d^9k)")
for e in acc:
    a = np.array(acc[e])
    print(f"  eps={e:.2f}: I_X = {a.mean():.4e} +- {a.std()/np.sqrt(len(a)):.1e};  I_X/|eps| = {a.mean()/e:.4e};  I_X/eps^2 = {a.mean()/e**2:.4e}")
print(f"[{time.time()-t0:.0f}s]")
