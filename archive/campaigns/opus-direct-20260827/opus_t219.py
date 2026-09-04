"""
T219 - is the dynamics of R138 RELATIVISTIC?

R138: the record measure fixes the ground state of a positive Hamiltonian
H = -D^-1 L D; the rates fix the spectrum.  The eigenvalues of H ARE the
relaxation rates of the reversible Markov generator L, so the excitation
dispersion E(k) can be measured directly as the decay rate of the Fourier-mode
autocorrelation.

  E(k) ~ |k|   (z=1)  -> relativistic; compatible with R97 (the site algebra IS
                        the proper Lorentz algebra)
  E(k) ~ k^2   (z=2)  -> Schrodinger-like; the construction CANNOT supply the
                        framework's dynamics on its own

Measured at lam = 1.0 (the Born point) and lam = 0.5 (disordered control).
"""
import numpy as np, sys

def run(L, lam, nsweep, nwarm, kmax=5, seed=3):
    rng = np.random.default_rng(seed)
    v = rng.normal(size=(L,L,L,3)); v /= np.linalg.norm(v,axis=-1,keepdims=True)
    i,j,k = np.indices((L,L,L)); A = ((i+j+k)%2==0); B = ~A
    def half(mask):
        nb = (np.roll(v,1,0), np.roll(v,-1,0), np.roll(v,1,1),
              np.roll(v,-1,1), np.roll(v,1,2), np.roll(v,-1,2))
        prop = rng.normal(size=v.shape)                 # FIXED proposal:
        prop /= np.linalg.norm(prop,axis=-1,keepdims=True)  # uniform new direction
        wo = np.ones(v.shape[:3]); wn = np.ones(v.shape[:3])
        for n in nb:
            wo *= 1 + lam*np.sum(v*n,axis=-1)
            wn *= 1 + lam*np.sum(prop*n,axis=-1)
        acc = (rng.random(v.shape[:3]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
        v[acc] = prop[acc]
    for _ in range(nwarm):
        half(A); half(B)
    modes = np.zeros((nsweep, kmax, 3), dtype=complex)
    for t in range(nsweep):
        half(A); half(B)
        f = np.fft.fftn(v, axes=(0,1,2))
        for n in range(1, kmax+1):
            modes[t, n-1] = (f[n,0,0] + f[0,n,0] + f[0,0,n])/3
    return modes

def gamma_from(modes, kmax, tmax=400):
    out = []
    for n in range(kmax):
        x = modes[:, n, :] - modes[:, n, :].mean(axis=0)
        T = len(x)
        C = np.zeros(tmax)
        for comp in range(3):
            f = np.fft.fft(x[:, comp], 2*T)
            ac = np.fft.ifft(f*np.conj(f)).real[:tmax]
            C += ac
        C /= C[0]
        # integrated autocorrelation time with automatic windowing
        tau = 0.5
        for t in range(1, tmax):
            if C[t] <= 0: break
            tau += C[t]
            if t > 6*tau: break
        out.append(1.0/tau)
    return np.array(out)

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    ns = int(sys.argv[2]) if len(sys.argv) > 2 else 60000
    for lam in (1.0, 0.5):
        m = run(L, lam, ns, 4000)
        G = gamma_from(m, 5)
        ks = 2*np.pi*np.arange(1,6)/L
        print(f"\n=== L={L} lam={lam}  ({ns} sweeps) ===")
        print("  n     k       Gamma(k)      Gamma/k      Gamma/k^2")
        for n in range(5):
            print(f"  {n+1}  {ks[n]:6.4f}   {G[n]:10.6f}   {G[n]/ks[n]:10.5f}   {G[n]/ks[n]**2:10.5f}")
        p = np.polyfit(np.log(ks), np.log(G), 1)[0]
        print(f"  fitted exponent z in Gamma ~ k^z :  {p:.3f}"
              f"   ({'RELATIVISTIC z=1' if abs(p-1)<0.2 else 'DIFFUSIVE z=2' if abs(p-2)<0.3 else 'neither'})")
