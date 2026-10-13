"""R19-25 s4: Gupta-Bleuler with LOCAL dynamics on truncated Krein slots (ring of L=3 sites, mass m).
Pre-registered (07:00Z, before running):
 Two fields per site: phi_L (metric +1) and phi_T (Krein metric (-1)^n), truncated-boson slots of dimension d.
 phi = (a + a^K)/sqrt2, pi = (a - a^K)/(i sqrt2); [phi_L,pi_L] = i, [phi_T,pi_T] = -i below the top level.
 H = 1/2 sum[pi_L^2 + phi_L M phi_L] - 1/2 sum[pi_T^2 + phi_T M phi_T],  M = -Lap + m^2 (local, nearest neighbour).
 Normal-mode annihilators (CCR formula) b_X(k) = L^-1/2 sum_x e^{-ikx}[sqrt(w/2) phi_x + i pi_x/sqrt(2w)].
 GB constraint D_k = b_L(k) - b_T(k) (null in CCR: [b_L,b_L^K] = 1, [b_T,b_T^K] = -1). CCR: V = ker{D_k} has
 Krein-PSD Gram, quotient = Fock vacuum only (the pair is a pure quartet half).
 Questions at finite d: (1) does an exact joint kernel of the Bogoliubov annihilators {b_L(k)} exist (CCR: the
 squeezed vacuum)? (2) dim V and the Krein inertia of V; (3) is V H-invariant (leak ||(1-P_V) H P_V||, using the
 Krein-orthogonal... we use the plain projector onto V and measure distance of H V from V); (4) the residual of the
 best approximate vacuum (smallest singular value of the stacked b_L, b_T) vs d.
"""
import numpy as np, itertools
np.set_printoptions(precision=4, suppress=True, linewidth=150)
L = 3; m = 1.0
ks = [2*np.pi*j/L for j in range(L)]
w = [np.sqrt(m**2 + (2*np.sin(k/2))**2) for k in ks]

def run(d):
    a = np.zeros((d, d))
    for n in range(1, d): a[n-1, n] = np.sqrt(n)
    I = np.eye(d); etaT1 = np.diag([(-1.)**n for n in range(d)])
    nsl = 2*L                                     # slots: L-field sites 0..L-1, T-field sites L..2L-1
    def emb(X, s):
        M = np.array([[1.]])
        for t in range(nsl): M = np.kron(M, X if t == s else I)
        return M
    eta = np.array([[1.]])
    for t in range(nsl): eta = np.kron(eta, I if t < L else etaT1)
    Kad = lambda X: eta@X.conj().T@eta
    A = [emb(a, s) for s in range(nsl)]
    phi = [(A[s] + Kad(A[s]))/np.sqrt(2) for s in range(nsl)]
    pi = [(A[s] - Kad(A[s]))/(1j*np.sqrt(2)) for s in range(nsl)]
    def H_field(off, sign):
        Hf = 0
        for x in range(L):
            Hf = Hf + 0.5*pi[off+x]@pi[off+x] + 0.5*(m**2)*phi[off+x]@phi[off+x]
            y = (x + 1) % L
            dphi = phi[off+y] - phi[off+x]
            Hf = Hf + 0.5*dphi@dphi
        return sign*Hf
    H = H_field(0, 1.) + H_field(L, -1.)
    def b(off, j):
        k = ks[j]; ww = w[j]
        return sum(np.exp(-1j*k*x)*(np.sqrt(ww/2)*phi[off+x] + 1j*pi[off+x]/np.sqrt(2*ww)) for x in range(L))/np.sqrt(L)
    bL = [b(0, j) for j in range(L)]; bT = [b(L, j) for j in range(L)]
    # Krein self-adjointness of H and frequency check below the top
    sa = np.abs(Kad(H) - H).max()
    freq = max(np.abs(H@bL[j] - bL[j]@H + w[j]*bL[j]).max() for j in range(L))
    # (1) exact Fock vacuum of the L field?  joint kernel of {bL(k)}
    stackL = np.vstack(bL)
    sL = np.linalg.svd(stackL, compute_uv=False)
    # (2) V = joint kernel of D_k
    D = np.vstack([bL[j] - bT[j] for j in range(L)])
    u, s, vh = np.linalg.svd(D)
    tol = 1e-9*max(1, s.max())
    r = int((s > tol).sum()); V = vh[r:].conj().T
    out = dict(sa=sa, freq=freq, dim=d**nsl, minsvL=sL.min(), dimV=V.shape[1], smallest_D=s[-5:] if len(s) >= 5 else s)
    if V.shape[1]:
        Gram = V.conj().T@eta@V; Gram = (Gram + Gram.conj().T)/2
        ev = np.linalg.eigvalsh(Gram)
        out['inertia'] = (int((ev > 1e-9).sum()), int((ev < -1e-9).sum()), int((np.abs(ev) <= 1e-9).sum()))
        out['nonnull_ev'] = np.sort(ev[np.abs(ev) > 1e-9])
        HV = H@V; P = V@V.conj().T
        out['leak'] = np.linalg.norm(HV - P@HV, 2)/max(1e-300, np.linalg.norm(HV, 2))
    # (4) approximate joint vacuum: smallest singular value of stacked [bL; bT]
    sAll = np.linalg.svd(np.vstack(bL + bT), compute_uv=False)
    out['approx_vac_resid'] = sAll.min()
    return out

print(f"ring L={L}, m={m}, omega_k = {np.round(w, 4)}")
for d in [2, 3, 4]:
    o = run(d)
    print(f"d={d}: Hilbert dim {o['dim']}; H Krein-self-adjoint residual {o['sa']:.1e}; |[H,bL]+w bL| (full space) = {o['freq']:.3f}")
    print(f"      exact Fock vacuum of the positive field? min sing.val of stacked bL(k) = {o['minsvL']:.3e}  (0 => exists)")
    print(f"      best approximate joint vacuum residual (stacked bL,bT) = {o['approx_vac_resid']:.3e}")
    print(f"      V = ker{{D_k}}: dim {o['dimV']}; 5 smallest sing. vals of stacked D = {np.round(o['smallest_D'], 6)}")
    if o['dimV']:
        print(f"      Krein inertia of V (+,-,0) = {o['inertia']}; non-null Gram eigenvalues = {np.round(o['nonnull_ev'], 4)}; relative leak ||(1-P_V)HV||/||HV|| = {o['leak']:.3e}")
