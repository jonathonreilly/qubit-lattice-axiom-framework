"""Curvature-squared term lambda * sum_h delta_h^2 added to the Regge second variation (Kuhn, D4 cone)."""
import sys, pickle, numpy as np
sys.path.insert(0, '.'); sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import regge_generic as RG

def R2(C, k):
    k = np.asarray(k, complex); M = np.zeros((C.E, C.E), complex)
    for a, d in C.terms:
        rp = np.zeros(C.E, complex); np.add.at(rp, d[0], d[2] * np.exp(1j * (d[1] @ k)))
        rm = np.zeros(C.E, complex); np.add.at(rm, d[0], d[2] * np.exp(-1j * (d[1] @ k)))
        M += np.outer(rm, rp)
    return M

def soft_count(Qf, ngauge, kd, s=(0.02, 0.01)):
    ev = []
    for x in s:
        Q = Qf(x * kd); w = np.linalg.eigvalsh(0.5 * (Q + Q.conj().T)); ev.append(w[np.argsort(np.abs(w))])
    a, b = ev
    soft = [i for i in range(ngauge, len(b)) if abs(a[i] / b[i] - 4) < 0.1 and abs(b[i]) < 1e-2]
    return len(soft), b[ngauge:ngauge + 10]

if __name__ == '__main__':
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd)
    OFF, S = RG.kuhn(); K = RG.Complex(OFF, S); D = pickle.load(open('d4.pkl', 'rb'))
    for name, C, ng in (('Kuhn', K, 4), ('D4 cone', D, 32)):
        for lam in (0.0, 0.1, -0.1):
            Qf = lambda k, C=C, lam=lam: C.Q(k) + lam * R2(C, k)
            # nullity at a generic momentum
            q = np.array([0.3, -0.2, 0.25, 0.15]); s = np.sort(np.linalg.svd(Qf(q), compute_uv=False)); s /= s[-1]
            n_soft, ev = soft_count(Qf, ng, kd)
            print(f"{name} lambda={lam:+.1f}: nullity {int((s < 1e-9).sum())}; massless non-gauge {n_soft}; smallest non-gauge eigenvalues at |k|=0.01: {np.round(ev[:n_soft + 2], 6)}")
