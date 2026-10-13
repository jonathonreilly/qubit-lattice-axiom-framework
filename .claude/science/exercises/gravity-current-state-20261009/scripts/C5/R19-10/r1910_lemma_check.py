"""R19-10: check Lemma S-ins on the ramp family. Per inserted site (sector-integrated), track
eps_fix(t) = <H_B>_psi(t) - E0(K_B); Gamma_hat = max_t |d eps_fix/dt| (finite differences on the step grid);
verify A_fix >= eps_fix(0)^2/(2 Gamma_hat) and eps_fix(t) >= eps_fix(0) - Gamma_hat t."""
import numpy as np
exec(open('r1910_adiabatic.py').read().split('# static delta(g)')[0])
def traj(N, m, s, T, dt=0.05):
    KA, KB = build(N, m, s)
    wA, OA = np.linalg.eigh(KA); omA = np.sqrt(wA)
    U = OA/np.sqrt(2*omA); Ud = -1j*OA*np.sqrt(omA/2)
    E0B = 0.5*np.sqrt(np.linalg.eigvalsh(KB)).sum()
    def efix(U, Ud):
        Phi = np.real(U @ U.conj().T); Pi = np.real(Ud @ Ud.conj().T)
        return 0.5*np.trace(Pi) + 0.5*np.trace(KB @ Phi) - E0B
    nst = max(1, int(round(T/dt))); h = T/nst
    es = [efix(U, Ud)]
    for j in range(nst):
        g = sstep((j + 0.5)/nst); K = (1-g)*KA + g*KB
        w, V = np.linalg.eigh(K); om = np.sqrt(w)
        a = V.T @ U; b = V.T @ Ud
        c = np.cos(om*h)[:, None]; sn = np.sin(om*h)[:, None]
        U = V @ (c*a + (sn/om[:, None])*b); Ud = V @ (-(om[:, None]*sn)*a + c*b)
        es.append(efix(U, Ud))
    return np.array(es), h
for m in (0.0, 1.0):
    for T in (1, 2, 4, 8):
        N = int(2*T + 48); N += N % 2
        tot = None
        for s, w in zip(S_nodes, S_w):
            e, h = traj(N, m, s, T)
            tot = w*e if tot is None else tot + w*e
        t = np.arange(len(tot))*h
        G = np.max(np.abs(np.diff(tot))/h)
        A = np.trapezoid(tot, t)
        lin_ok = np.all(tot >= tot[0] - G*t - 1e-12)
        pr('m=%.1f T=%d: eps_fix(0) = %.5f ; Gamma_hat = %.5f ; A_fix = %.5f >= eps0^2/(2 Gamma_hat) = %.5f : %s ; eps(t) >= eps0 - Gamma t everywhere: %s'
           % (m, T, tot[0], G, A, tot[0]**2/(2*G), A >= tot[0]**2/(2*G), lin_ok))
