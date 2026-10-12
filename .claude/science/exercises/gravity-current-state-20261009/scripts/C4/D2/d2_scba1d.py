"""D2: self-consistent Born (non-crossing) approximation on the real axis, 1D.
Sigma(k,w) = (1/N) sum_q |M_q|^2 G(k-q, w - w_q),  G = 1/(w + i eta - eps(k) - Sigma(k,w)).
Phonon energies rounded to the w-grid.  Band = lowest root of w - eps - Re Sigma(k,w) below which
A is ~0; Z = 1/(1 - dReSigma/dw) there.  Resolution: delta >= 2 pi/N, broadening eta."""
import numpy as np, sys, time
TWO_PI = 2*np.pi
def run(kind, N, c, g2, a, eta=0.01, dw=0.002, wmin=-1.5, wmax=4.5, nit=60):
    eps_f = {'TB': lambda k: 1 - np.cos(k), 'Q4': lambda k: (1 - np.cos(k))**2}[kind]
    k = TWO_PI*np.arange(N)/N; eps = eps_f(k)
    w = np.arange(wmin, wmax, dw); Nw = len(w)
    q = k.copy(); wq = 2*c*np.abs(np.sin(q/2)); M2 = g2*(2*np.abs(np.sin(q/2)))**(2*a); M2[0] = 0
    sh = np.rint(wq/dw).astype(int)
    Sig = np.zeros((N, Nw), complex)
    for it in range(nit):
        G = 1/(w[None, :] + 1j*eta - eps[:, None] - Sig)
        new = np.zeros_like(Sig)
        for iq in range(1, N):
            s = sh[iq]
            Gs = np.roll(G, iq, axis=0)       # Gs[j] = G[j - iq]  -> G(k - q)
            if s > 0:
                new[:, s:] += M2[iq]*Gs[:, :Nw - s]
                # below the grid: G(w - wq) ~ 1/(w - wq - eps) (free tail, real part only)
                new[:, :s] += M2[iq]/(w[None, :s] - wq[iq] + 1j*eta - eps[(np.arange(N) - iq) % N][:, None])
            else:
                new[:] += M2[iq]*Gs
        new /= N
        diff = np.abs(new - Sig).max()
        Sig = 0.5*Sig + 0.5*new
        if diff < 1e-7: break
    # lowest root of f(w) = w - eps - Re Sigma
    E = np.empty(N); Z = np.empty(N)
    for j in range(N):
        f = w - eps[j] - Sig[j].real
        i = np.where(np.diff(np.sign(f)) > 0)[0][0]
        t = f[i]/(f[i] - f[i+1]); E[j] = w[i] + t*dw
        dS = (Sig[j, i+1].real - Sig[j, i].real)/dw
        Z[j] = 1/(1 - dS)
    return k, E, Z, it, diff
if __name__ == '__main__':
    print("# SCBA 1D: eta=0.01, dw=0.002.  E(pi)-E(pi-j dk) local exponents p for j=1,2,4,8,16; chord slope s(1 dk); Z(0), Z(pi)")
    for kind, c, g2, a, N in [('TB', 1.5, 0.3, 0.5, 64), ('TB', 1.5, 0.3, 0.5, 128), ('TB', 1.5, 1.0, 0.5, 128), ('TB', 1.5, 0.3, 1.0, 128), ('Q4', 1.0, 0.1, 0.5, 128)]:
        t = time.time()
        k, E, Z, it, diff = run(kind, N, c, g2, a)
        h = N//2; dk = k[1]
        D = [E[h] - E[h - j] for j in (1, 2, 4, 8, 16, 32)]
        p = [np.log(abs(D[i+1]/D[i]))/np.log(2) for i in range(5)]
        print(f"{kind} c={c} g2={g2} a={a} N={N} | E0={E[0]:.5f} Epi={E[h]:.5f} Z0={Z[0]:.4f} Zpi={Z[h]:.4f} | p=" + " ".join(f"{x:.3f}" for x in p)
              + f" | s(dk)={D[0]/dk:.4f} | it={it} diff={diff:.1e} t={time.time()-t:.0f}s", flush=True)
