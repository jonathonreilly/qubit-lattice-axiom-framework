"""R19-10 check: the instantaneous-excitation integral int eps_inst dt = int (<H(g(t))> - E0(H(g(t)))) dt,
evaluated with K at the exact end-of-step g (not the midpoint), for two time steps.  m = 0 and m = 1.
Adiabatic perturbation theory (RECALLED) predicts eps_inst ~ gdot^2 chi(g) so int eps_inst dt ~ c/T."""
import numpy as np, time
exec(open('r1910_adiabatic.py').read().split('# static delta(g)')[0])
T0 = time.time()
def run_inst(N, m, s, T, dt):
    KA, KB = build(N, m, s)
    wA, OA = np.linalg.eigh(KA); omA = np.sqrt(wA)
    U = OA/np.sqrt(2*omA); Ud = -1j*OA*np.sqrt(omA/2)
    nst = max(1, int(round(T/dt))); h = T/nst
    I = 0.0; prev = 0.0
    for j in range(nst):
        g = sstep((j + 0.5)/nst); K = (1-g)*KA + g*KB
        w, V = np.linalg.eigh(K); om = np.sqrt(w)
        a = V.T @ U; b = V.T @ Ud
        c = np.cos(om*h)[:, None]; sn = np.sin(om*h)[:, None]
        U = V @ (c*a + (sn/om[:, None])*b); Ud = V @ (-(om[:, None]*sn)*a + c*b)
        ge = sstep((j + 1.0)/nst); Ke = (1-ge)*KA + ge*KB
        Phi = np.real(U @ U.conj().T); Pi = np.real(Ud @ Ud.conj().T)
        e = 0.5*np.trace(Pi) + 0.5*np.trace(Ke @ Phi) - 0.5*np.sqrt(np.linalg.eigvalsh(Ke)).sum()
        I += 0.5*h*(e + prev); prev = e
    return I
for m in (0.0, 1.0):
    for T in (4, 8, 16, 32):
        res = []
        for dt in (0.05, 0.025):
            if T == 32 and dt == 0.025: continue
            N = int(2*T + 48); N += N % 2
            res.append(sum(w*run_inst(N, m, s, T, dt) for s, w in zip(S_nodes, S_w)))
        pr('m=%.1f T=%2d: int eps_inst dt = %s ; T * int = %s [%.0fs]' % (m, T, ', '.join('%.4e' % r for r in res),
           ', '.join('%.4f' % (T*r) for r in res), time.time()-T0))
