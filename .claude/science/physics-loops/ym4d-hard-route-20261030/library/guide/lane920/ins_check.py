# GUIDE check of (INS), Lemma E, Lemma BR, Remark R1 on 2D Z_N lattice gauge theory,
# spatial circle of b links, exact enumeration. Decides nothing; checks algebra only.
import itertools, sys
import numpy as np

def run(N, b, beta, a, nq=40):
    S = N**b
    st = np.array(list(itertools.product(range(N), repeat=b)))      # slices and gauge configs
    ct = np.cos(2*np.pi*np.arange(N)/N)
    # e1[A,g,B] = sum_x cos(2 pi (A_x + g_{x+1} - B_x - g_x)/N)
    gsh = np.roll(st, -1, axis=1)                                     # g_{x+1}
    ph = (st[:, None, None, :] + gsh[None, :, None, :] - st[None, None, :, :] - st[None, :, None, :]) % N
    e1 = ct[ph].sum(axis=3)                                           # shape (S_A, S_g, S_B)
    M = np.exp(beta*e1).mean(axis=1)                                  # M[A,B], Haar average over g
    Mp = (e1*np.exp(beta*e1)).mean(axis=1)                            # dM/dbeta
    # centre flip: link 0 shifted by N/2
    flip = st.copy(); flip[:, 0] = (flip[:, 0] + N//2) % N
    idx = {tuple(s): i for i, s in enumerate(st)}
    Cperm = np.array([idx[tuple(s)] for s in flip])
    C = np.zeros((S, S)); C[np.arange(S), Cperm] = 1.0
    P0 = 0.5*(np.eye(S) + C)
    w, v = np.linalg.eigh(M)
    lam0 = w[-1]; Om = v[:, -1]; Om = Om*np.sign(Om.sum())
    assert np.all(Om > 0)
    Z0a = np.trace(np.linalg.matrix_power(M, a) @ P0)
    Sev = Z0a/lam0**a - 1.0
    R = np.linalg.matrix_power(M, a-1) @ P0                           # ring kernel R[U',U]
    Rinf = lam0**(a-1)*np.outer(Om, Om)
    u_aev = np.trace(Mp @ np.linalg.matrix_power(M, a-1) @ P0)/(b*Z0a)
    u_inf = Om @ Mp @ Om/(b*lam0)
    def G(th):
        # G[A,B,Cc] = mean_g exp(beta[(1-th) e1(A,g,B) + th e1(A,g,Cc)]), and its theta-derivative
        E = beta*((1-th)*e1[:, :, :, None] + th*e1[:, :, None, :])   # (A,g,B,Cc)
        X = np.exp(E)
        D = beta*(e1[:, :, None, :] - e1[:, :, :, None])
        return X.mean(axis=1), (D*X).mean(axis=1)
    def Zs(th, RR):
        g0, g1 = G(th)
        # Z = sum_{U,U',W,W'} RR[U',U] G[U,U',W'] G[W,W',U'] Om[W] Om[W'] / lam0
        H = np.einsum('wbc,w->bc', g0, Om)                           # H[W',U'] = sum_W Om[W] G[W,W',U']
        H1 = np.einsum('wbc,w->bc', g1, Om)
        z = np.einsum('pu,upq,qp,q->', RR, g0, H, Om)/lam0           # p=U', u=U, q=W'
        dz = (np.einsum('pu,upq,qp,q->', RR, g1, H, Om) + np.einsum('pu,upq,qp,q->', RR, g0, H1, Om))/lam0
        return z, dz
    x, wq = np.polynomial.legendre.leggauss(nq); th = 0.5*(x + 1); wq = 0.5*wq
    I_a = 0.0; I_inf = 0.0; deltas = []
    for t, ww in zip(th, wq):
        za, dza = Zs(t, R); zi, dzi = Zs(t, Rinf)
        I_a += ww*(-dza/za); I_inf += ww*(-dzi/zi)
        deltas.append((-dza/za + dzi/zi)/(b*beta))                    # Delta_theta per link
    z0, dz0 = Zs(0.0, R); z1, dz1 = Zs(1.0, R)
    p0, dp0 = Zs(0.0, Rinf); p1, dp1 = Zs(1.0, Rinf)
    zq, _ = Zs(0.3, Rinf); zq2, _ = Zs(0.7, Rinf)
    D0 = (-dz0/z0 + dp0/p0)/(b*beta); D1 = (-dz1/z1 + dp1/p1)/(b*beta)
    Erho0 = z0/p0; Erho1 = z1/p1
    print(f"N={N} b={b} beta={beta} a={a}: log(1+S_ev)={np.log1p(Sev):.12e}  INS integral={I_a - I_inf:.12e}  ref integral={I_inf:.3e}")
    print(f"   Z_theta(0)/Z_0(a)={z0/Z0a:.12f}  Z_theta(1)/lam0^a={z1/lam0**a:.12f}  Phi0/lam0^(a+1)={p0/lam0**a:.12f} Phi1/lam0^(a+1)={p1/lam0**a:.12f}  R1: Phi(.3)/Phi(.7)={zq/zq2:.12f}")
    print(f"   Lemma E: Delta_0={D0:.10e} vs u_aev-u_inf={u_aev-u_inf:.10e}; Delta_1={D1:.3e}")
    print(f"   BR: E0(rho)={Erho0:.12f} vs 1+S_ev={1+Sev:.12f}; E1(rho)={Erho1:.12f}; max_theta|Delta|/Delta_0={max(abs(d) for d in deltas)/abs(D0):.4f}; Delta at theta=0.04,0.5,0.96: {deltas[1]:.4e} {deltas[len(deltas)//2]:.4e} {deltas[-2]:.4e}")

if __name__ == "__main__":
    for (N, b, beta, a) in [(4, 2, 0.7, 2), (4, 2, 1.5, 3), (4, 2, 3.0, 4), (6, 2, 2.0, 3), (2, 2, 1.0, 3)]:
        run(N, b, beta, a)
