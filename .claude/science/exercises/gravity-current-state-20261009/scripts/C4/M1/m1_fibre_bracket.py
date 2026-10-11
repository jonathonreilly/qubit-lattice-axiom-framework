"""M1 (2): the two-particle sector, fibre by fibre, exactly (truncated relative box |r|<=R, hard wall).
1D, two distinguishable particles, eps(k) = m + 2t(1-cos k) (m=1, t=0.5 -> beta=1), contact U at r=0.
Gauge psi(x1,x2) = e^{iQ x2} phi(x1-x2):  X2 -> i d/dQ, X1 = X2 + r.
First moment of the energy density (kinetic density of each particle at that particle, contact energy at its site):
  K = 1/2{i d_Q, H(Q)} + K',  K' = 1/2{r, E1}.
  P(Q) = 1/2{H', H} + i[H, K']         (P = i[H,K], the total energy current)
  C(Q) = [H, P]                         (C1: must vanish)
  D(Q) = -1/2{P', H} + i[K', P] + beta H  (C3 defect: i[K,P] + beta H, must vanish)
Reports: Hellmann-Feynman <b|P|b> = d u_b/dQ; leakage |(P - p_b) b| (P not conserved on the composite);
<b|D|b>/(beta E_b) against the band anomaly A_b = u_b''/beta - 1; sup_Q ||H(Q)||, ||P(Q)|| as R grows
(bounded fibre), against the tower requirement.
"""
import numpy as np
m, t = 1.0, 0.5; beta = 2*t*m
def ops(R, Q, U):
    rs = np.arange(-R, R+1); n = len(rs)
    E1 = np.diag(np.full(n, m+2*t)).astype(complex); E2 = E1.copy(); dE2 = np.zeros((n, n), complex); d2E2 = dE2.copy()
    for i in range(n-1):
        # E1: phi(r) -> sum_n eps_n phi(r-n): -t phi(r-1) - t phi(r+1)
        E1[i+1, i] += -t; E1[i, i+1] += -t
        # E2: phi(r) -> sum_n eps_n e^{-iQn} phi(r+n): -t e^{-iQ} phi(r+1) - t e^{iQ} phi(r-1)
        E2[i, i+1] += -t*np.exp(-1j*Q); E2[i+1, i] += -t*np.exp(1j*Q)
        dE2[i, i+1] += -t*(-1j)*np.exp(-1j*Q); dE2[i+1, i] += -t*(1j)*np.exp(1j*Q)
        d2E2[i, i+1] += -t*(-1)*np.exp(-1j*Q); d2E2[i+1, i] += -t*(-1)*np.exp(1j*Q)
    V = np.diag(np.where(rs == 0, U, 0.0)).astype(complex)
    H = E1 + E2 + V
    rr = np.diag(rs.astype(float)).astype(complex)
    Kp = 0.5*(rr@E1 + E1@rr)
    acomm = lambda A, B: A@B + B@A
    comm = lambda A, B: A@B - B@A
    P = 0.5*acomm(dE2, H) + 1j*comm(H, Kp)
    dP = 0.5*acomm(d2E2, H) + dE2@dE2 + 1j*comm(dE2, Kp)
    C = comm(H, P)
    D = -0.5*acomm(dP, H) + 1j*comm(Kp, P) + beta*H
    return rs, H, P, C, D
if __name__ == "__main__":
    print(__doc__)
    R = 60
    for U in [-0.5, -1.0]:
        Qs = np.linspace(-np.pi, np.pi, 129)[:-1]; h = Qs[1]-Qs[0]
        Eb = np.array([np.linalg.eigvalsh(ops(R, Q, U)[1])[0] for Q in Qs])
        ub = 0.5*Eb**2
        kk = np.fft.fftfreq(len(Qs), d=h)*2*np.pi
        dub = np.real(np.fft.ifft(1j*kk*np.fft.fft(ub))); d2ub = np.real(np.fft.ifft(-(kk**2)*np.fft.fft(ub)))
        print(f"U={U}: R={R}")
        print("     Q      E_b      <P>_b    du_b/dQ   |(P-p)b|   |C b|    <D>_b/(beta E_b)   A_b=u''/beta-1   |rest|")
        for Q in [0.0, np.pi/4, np.pi/2, 3*np.pi/4, -np.pi+1e-9]:
            i = np.argmin(abs(Qs - Q)); Q = Qs[i]
            rs, H, P, C, D = ops(R, Q, U)
            w, v = np.linalg.eigh(H); b = v[:, 0]
            pb = np.vdot(b, P@b).real
            leak = np.linalg.norm(P@b - pb*b); cb = np.linalg.norm(C@b)
            Db = np.vdot(b, D@b).real/(beta*w[0])
            print(f"  {Q:+.3f}  {w[0]:.5f}  {pb:+.5f}  {dub[i]:+.5f}  {leak:.3e}  {cb:.3e}   {Db:+.5f}           {d2ub[i]/beta-1:+.5f}")
    print()
    print("Free case U=0: P conserved on the two-particle sector? |C| restricted to states with |r|<=R/2:")
    for R in [20, 40]:
        rs, H, P, C, D = ops(R, 0.7, 0.0)
        inner = np.abs(rs) <= R//2
        print(f"   R={R}: |C[inner,inner]|_op = {np.linalg.norm(C[np.ix_(inner, inner)], 2):.2e}   (interacting U=-1: "
              f"{np.linalg.norm(ops(R, 0.7, -1.0)[3][np.ix_(inner, inner)], 2):.2e})")
    print()
    print("Bounded fibre: sup_Q ||H(Q)|| and sup_Q ||P(Q)|| on states with |r|<=R/2 (wall-free part), U=-1")
    for R in [10, 20, 40, 80]:
        sH = sP = 0.0
        for Q in np.linspace(-np.pi, np.pi, 17):
            rs, H, P, C, D = ops(R, Q, -1.0)
            inner = np.abs(rs) <= R//2
            sH = max(sH, np.linalg.norm(H[np.ix_(inner, inner)], 2)); sP = max(sP, np.linalg.norm(P[np.ix_(inner, inner)], 2))
        print(f"   R={R:3d}: sup||H||={sH:.4f}  sup||P||={sP:.4f}   (bounds: ||H|| <= 2(m+4t)+|U| = {2*(m+4*t)+1:.1f})")
    print("   A complete tower over one Q needs E_n = sqrt(M^2 + beta (Q+2 pi n)^2) for all n: unbounded. The fibre is bounded.")
