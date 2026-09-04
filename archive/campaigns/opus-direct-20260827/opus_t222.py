"""
T222 - does SUPPLYING the fourth direction fix the defect R140 measured?

R140: the record field on Z^3 has eta = 0 (S ~ 1/khat^2) where a relativistic
slice needs eta = 1 (S ~ 1/khat).  R112/R133/R140 all converge on "a fourth
direction must be supplied".  This tests whether doing so removes exactly that
defect.

PRE-REGISTERED PREDICTION (written before running):
  the same consistent rule on Z^4,  mu ∝ prod_{4D edges} (1 + lam v_x.v_y),
  in its ordered phase has massless modes, so S_4D ~ 1/khat^2_4D.  A 3D SLICE
  sums out the fourth momentum:
      S_slice(k3) = sum_{k4} S_4D(k3,k4) ~ 1/|khat_3|   =>  eta = 1
  i.e. the fourth direction should convert eta = 0 into eta = 1.

CONTROLS
  (i) synthetic 4D Gaussian field with S_4D = 1/khat^2 exactly -> its 3D slice
      must give eta = 1.  Validates that slicing does what is claimed,
      independent of the interacting model.
  (ii) the full 4D structure factor of the interacting model must itself be
      1/khat^2_4D (massless), or the premise of the test fails.
"""
import numpy as np, sys, time

def slice_and_full(v, L):
    """S over a 3D slice (averaged over all x4) and the full 4D S, along one axis."""
    Ssl = np.zeros((L, L, L))
    for t in range(L):
        f = np.fft.fftn(v[:, :, :, t, :], axes=(0, 1, 2))
        Ssl += np.sum(np.abs(f)**2, axis=-1)
    Ssl /= L
    f4 = np.fft.fftn(v, axes=(0, 1, 2, 3))
    S4 = np.sum(np.abs(f4)**2, axis=-1)
    return Ssl, S4

def run(L, lam, nwarm=3000, nmeas=4000, seed=9):
    rng = np.random.default_rng(seed)
    v = rng.normal(size=(L,L,L,L,3)); v /= np.linalg.norm(v,axis=-1,keepdims=True)
    idx = np.indices((L,L,L,L)); A = (idx.sum(axis=0) % 2 == 0); B = ~A
    def half(mask, cone):
        nb = []
        for ax in range(4):
            nb.append(np.roll(v, 1, ax)); nb.append(np.roll(v, -1, ax))
        prop = v + cone*rng.normal(size=v.shape)
        prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
        wo = np.ones(v.shape[:4]); wn = np.ones(v.shape[:4])
        for n in nb:
            wo *= 1 + lam*np.sum(v*n, axis=-1)
            wn *= 1 + lam*np.sum(prop*n, axis=-1)
        acc = (rng.random(v.shape[:4]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
        v[acc] = prop[acc]
        return acc[mask].mean()
    cone = 1.0
    for t in range(nwarm):
        a = 0.5*(half(A,cone)+half(B,cone))
        if t % 100 == 99:
            cone *= 1.15 if a > 0.55 else (0.87 if a < 0.35 else 1.0)
            cone = min(max(cone, 0.05), 4.0)
    Ssl = np.zeros((L,L,L)); S4 = np.zeros((L,L,L,L)); n = 0
    for t in range(nmeas):
        half(A,cone); half(B,cone)
        if t % 4 == 0:
            a, b = slice_and_full(v, L); Ssl += a; S4 += b; n += 1
    return Ssl/n, S4/n

def report(name, S, L, ndim):
    kn = 2*np.pi*np.arange(1,6)/L
    kh2 = 4*np.sin(kn/2)**2
    s = []
    for m in range(1,6):
        if ndim == 3:
            s.append((S[m,0,0]+S[0,m,0]+S[0,0,m])/3)
        else:
            s.append((S[m,0,0,0]+S[0,m,0,0]+S[0,0,m,0]+S[0,0,0,m])/4)
    s = np.array(s)
    a = s*kh2; b = s*np.sqrt(kh2)
    print(f"  {name}")
    print(f"     S*khat^2 spread = {a.max()/a.min():5.2f}x   (flat => eta=0, classical)")
    print(f"     S*khat   spread = {b.max()/b.min():5.2f}x   (flat => eta=1, relativistic)")
    return a.max()/a.min(), b.max()/b.min()

if __name__ == "__main__":
    print("=== CONTROL (i): synthetic 4D Gaussian with S_4D = 1/khat^2 exactly ===")
    L = 12; rng = np.random.default_rng(2)
    kk = 2*np.pi*np.fft.fftfreq(L)
    G = np.meshgrid(kk, kk, kk, kk, indexing='ij')
    KH2 = sum(4*np.sin(g/2)**2 for g in G); KH2[0,0,0,0] = np.inf
    Ssl = np.zeros((L,L,L)); NS = 300
    for _ in range(NS):
        amp = np.sqrt(1.0/KH2/2)
        f = amp*(rng.normal(size=(L,)*4) + 1j*rng.normal(size=(L,)*4))
        x = np.fft.ifftn(f).real
        for t in range(L):
            Ssl += np.abs(np.fft.fftn(x[:,:,:,t]))**2
    report("synthetic 4D field, 3D slice", Ssl/(NS*L), L, 3)

    for L, lam in ((10, 1.0), (12, 1.0)):
        t0 = time.time()
        Ssl, S4 = run(L, lam)
        print(f"\n=== interacting record field on Z^4, L={L}, lam={lam} "
              f"[{time.time()-t0:.0f}s] ===")
        report("CONTROL (ii): full 4D structure factor", S4, L, 4)
        report("THE TEST: 3D slice", Ssl, L, 3)
