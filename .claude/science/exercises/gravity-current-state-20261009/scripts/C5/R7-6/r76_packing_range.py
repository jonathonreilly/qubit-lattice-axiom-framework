"""R7-6 script 4 (d = 1, continuum fibre at fixed total P; by Lemma L3 identical to the lattice box sector):
range of the BT packing operator B_a for the partition a = (12)(3), with the standard (spectator rest-frame momentum q3)
identification, so that B_a = 1 on the P = 0 fibre.

  B_a = sum_n |chi_n><chi_n| (pair internal, eigenvectors of M_12 = M0(q) + lam |g><g|)  (x)  R_{M0(q)}^{-1} R_{mu_n}
  R_mu : k3 -> q3(P, k3; mu) = spectator momentum in the rest frame of (cluster of mass mu) + (particle 3)
  (R_{M0}^{-1} R_mu f)(k3) = f(k3') sqrt(dk3'/dk3),  q3(P, k3'; mu) = q3(P, k3; M0(q)).

Test states psi = a(q) e^{-i q r} (x) b(k3) e^{-i k3 x}: r = separation of particles 1 and 2, x = position of 3
relative to the 12 pair (conjugate to k3 at fixed P).
(A) pair separated (r grows), spectator at x = 0: B_a - 1 must vanish for cluster separability; rate measured.
(B) pair together (r = 0), spectator far (x grows): B_a - 1 does NOT vanish (BT's long-range packing).
(C) P = 0: B_a = 1 exactly (check).
"""
import numpy as np, time
m, LAM, KAP = 0.3, -3.0, 0.25
def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def g(q): return q*sstep(1.0 - (q/KAP)**2)/KAP
def M0f(q): return 2*np.sqrt(m*m + q*q)

def q3(P, k, mu):
    E = np.sqrt(mu*mu + (P-k)**2) + np.sqrt(m*m + k*k)
    Th = np.arctanh(P/E); return m*np.sinh(np.arcsinh(k/m) - Th)

def solve_k(P, target, mu, k0):
    k = k0.copy()
    for _ in range(40):
        h = 1e-6
        f = q3(P, k, mu) - target; d = (q3(P, k+h, mu) - q3(P, k-h, mu))/(2*h)
        dk = f/d; k -= dk
        if np.max(np.abs(dk)) < 1e-14: break
    return k

out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

Nq, Qmax = 601, 1.2
q = np.linspace(-Qmax, Qmax, Nq); dq = q[1]-q[0]
M = np.diag(M0f(q)) + LAM*dq*np.outer(g(q), g(q))
mu, chi = np.linalg.eigh(M)
pr('pair: Nq = %d, dq = %.4f; bound state M_b = %.10f (2m = %.2f); next level %.6f' % (Nq, dq, mu[0], 2*m, mu[1]))
Nk = 601
def run(P, a_fun, b_fun, kc):
    k = np.linspace(kc-0.45, kc+0.45, Nk); dk = k[1]-k[0]
    at = a_fun(q)*np.sqrt(dq); bt_norm = np.sqrt(np.sum(np.abs(b_fun(k))**2)*dk)
    c = chi.T @ at                       # <chi_n|a>
    res = np.zeros((Nq, Nk), complex)
    M0q = M0f(q)
    for n in range(Nq):
        if abs(c[n]) < 1e-13: continue
        J = np.where(np.abs(chi[:, n]) > 1e-12)[0]
        # for every output pair-momentum q_j (free mass M0q[j]) and output k: k' with q3(P,k';mu_n) = q3(P,k;M0q[j])
        tgt = q3(P, k[None, :], M0q[J][:, None])
        kp = solve_k(P, tgt, mu[n], np.broadcast_to(k[None, :], tgt.shape).copy())
        h = 1e-6
        dtgt = (q3(P, k[None, :]+h, M0q[J][:, None]) - q3(P, k[None, :]-h, M0q[J][:, None]))/(2*h)
        dkp = dtgt/((q3(P, kp+h, mu[n]) - q3(P, kp-h, mu[n]))/(2*h))
        res[J] += chi[J, n][:, None]*c[n]*b_fun(kp)*np.sqrt(dkp)
    res *= np.sqrt(dk)/bt_norm
    psi = at[:, None]*b_fun(k)[None, :]*np.sqrt(dk)/bt_norm
    return np.sqrt(np.sum(np.abs(res - psi)**2))/np.sqrt(np.sum(np.abs(psi)**2))

t0 = time.time()
sig_q, q0 = 0.06, 0.08
sig_k, k30 = 0.06, 0.15
for P in [0.0, 0.4]:
    pr('--- total P = %.2f ---' % P)
    for r in [0, 10, 20, 40, 80, 160, 320]:
        a = (lambda r: (lambda qq: np.exp(-(qq-q0)**2/(2*sig_q**2))*np.exp(-1j*qq*r)))(r)
        b = lambda kk: np.exp(-(kk-k30)**2/(2*sig_k**2))
        pr('(A) P = %.2f  pair separation r = %4d, spectator x = 0  : ||(B_a - 1)psi|| = %.3e   [%.0f s]' % (P, r, run(P, a, b, k30), time.time()-t0))
    for x in [0, 20, 80, 320]:
        a = lambda qq: np.exp(-(qq-q0)**2/(2*sig_q**2))
        b = (lambda x: (lambda kk: np.exp(-(kk-k30)**2/(2*sig_k**2))*np.exp(-1j*kk*x)))(x)
        pr('(B) P = %.2f  pair together r = 0, spectator at x = %4d : ||(B_a - 1)psi|| = %.3e   [%.0f s]' % (P, x, run(P, a, b, k30), time.time()-t0))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
