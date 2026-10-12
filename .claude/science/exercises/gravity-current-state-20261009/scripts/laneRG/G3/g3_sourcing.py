"""G3 part 1: can a sawtooth (1/r-tailed) momentum source the VS shift constraint at linear order?

Linear-order first-class conditions (RN L1, 09-14 stencils, centred Fourier symbols qhat_j = 2 sin(q_j/2)):
 (E)  dT00/dt + div P = 0          P_j on edges (x + e_j/2)
 (M)  dP_j/dt + G[T]_j = 0         T_jj on sites, T_ij on ij faces, symmetric
Both with the SAME P.  (E) forces the shift source to be the energy current, whose one-body symbol is E grad E.

Separable free scalar, W(k) = m^2 + sum_i w(k_i), H = 1/2 sum pi^2 + 1/2 phi.K.phi.
Construction (any separable w):  T00 kernel  1/2 pi pi + 1/2 C(a,b) phi_a phi_b,  C = (W(a)+W(b))/2
   P_j  (pi_a phi_b):   i (w(a_j)-w(b_j)) / (2 qhat_j)
   T_ij (phi_a phi_b):  (w(a_i)-w(b_i))(w(a_j)-w(b_j)) / (4 qhat_i qhat_j)
NN-KG: w = 4 sin^2(k/2) (local).  SLAC: w = s(k)^2, s = sawtooth (energy current symbol = s(k), i.e. f = k).
Part (b) verifies (E),(M) on random classical fields in real space; part (c) measures real-space tails.
"""
import numpy as np, itertools, time
t0 = time.time()
def saw(k): return (k + np.pi) % (2*np.pi) - np.pi
def w_nn(k): return 4*np.sin(k/2)**2
def w_slac(k): return saw(k)**2

print("== (a) one-body symbol of the TOTAL energy current, E dE/dk, vs sawtooth k (NN-KG, m=1) ==")
for k in [0.1, 0.5, 1.0, 2.0, 3.0]:
    W = 1 + 4*np.sin(k/2)**2; EdE = 0.5*(2*np.sin(k))     # (1/2) d(E^2)/dk
    print(f"  k={k:4.1f}: E dE/dk = sin k = {EdE:+.5f}   sawtooth = {k:+.5f}   mismatch = {k-EdE:+.5f}")
print("  -> with NN-KG matter the shift source P must have symbol sin k (= energy current); a sawtooth P")
print("     leaves d/dt(scalar constraint) ~ div(J_E - P_saw) != 0 on the constraint surface.")

# ---------------- (b) real-space verification on a 2D odd torus ----------------
def kernels_2d(L, wfun):
    """Return real-space coefficient arrays for densities at the origin cell.
    Fields phi_y, pi_y on sites y (L x L).  Fourier phi_a = sum_y e^{-i a y} phi_y."""
    k = 2*np.pi*np.fft.fftfreq(L)
    A = np.array(np.meshgrid(k, k, indexing='ij'))            # (2, L, L)
    wa = [wfun(A[0]), wfun(A[1])]
    # pair arrays (a, b): shape (L,L,L,L)
    a0 = A[0][:, :, None, None]; a1 = A[1][:, :, None, None]
    b0 = A[0][None, None, :, :]; b1 = A[1][None, None, :, :]
    wa0 = wa[0][:, :, None, None]; wa1 = wa[1][:, :, None, None]
    wb0 = wa[0][None, None, :, :]; wb1 = wa[1][None, None, :, :]
    q0 = a0 + b0; q1 = a1 + b1                                # unreduced, centred phases use these
    qh0 = 2*np.sin(q0/2); qh1 = 2*np.sin(q1/2)
    Wa = 1.0 + wa0 + wa1; Wb = 1.0 + wb0 + wb1                # m = 1
    C = 0.5*(Wa + Wb)
    with np.errstate(divide='ignore', invalid='ignore'):
        dw0 = wa0 - wb0; dw1 = wa1 - wb1
        p0 = 1j*dw0/(2*qh0); p1 = 1j*dw1/(2*qh1)
        # limits on qhat = 0 sets: use l'Hopital numerically via tiny offset evaluation
    def fix(arr, num_fun, qh):
        bad = np.abs(qh) < 1e-12
        return arr, bad
    # handle q_j = 0 (b_j = -a_j) analytically: dw/(2 qhat) -> derivative; NN: sin(a); SLAC: saw(a)
    return A, (a0, a1, b0, b1, wa0, wa1, wb0, wb1, qh0, qh1, C)

def build_real(L, wfun, dsym):
    """dsym(a) = limit of (w(a)-w(b))/(2 qhat) at b=-a (one-body symbol: sin a or saw(a))."""
    k = 2*np.pi*np.fft.fftfreq(L)
    K = np.array(np.meshgrid(k, k, indexing='ij')).reshape(2, -1)   # (2, N)
    N = K.shape[1]
    a = K[:, :, None]; b = K[:, None, :]
    wa = wfun(a); wb = wfun(b)
    q = a + b; qh = 2*np.sin(q/2)
    ratio = np.empty((2, N, N))
    for j in range(2):
        num = wa[j] - wb[j]
        bad = np.abs(qh[j]) < 1e-12
        with np.errstate(divide='ignore', invalid='ignore'):
            r = num/(2*qh[j])
        # on qhat_j = 0 with b_j = -a_j (mod 2pi): limit is dsym(a_j) (num vanishes linearly)
        r[bad] = np.broadcast_to(dsym(a[j]), r.shape)[bad]
        ratio[j] = r
    Wa = 1.0 + wa.sum(0); Wb = 1.0 + wb.sum(0)
    C = 0.5*(Wa + Wb)
    # positions: sites y (index n), Fourier phi_a = sum_y e^{-i a.y} phi_y  => phi_y = (1/N) sum_a e^{i a y} phi_a
    Y = np.array(np.meshgrid(np.arange(L), np.arange(L), indexing='ij')).reshape(2, -1)
    E = np.exp(-1j*(K.T @ Y))            # E[a, y] = e^{-i a.y}  -> phi_a = E @ phi
    return K, Y, E, ratio, C, Wa, Wb, qh

def check_identities(L, wfun, dsym, label, rng):
    K, Y, E, ratio, C, Wa, Wb, qh = build_real(L, wfun, dsym)
    N = K.shape[1]
    Wk = 1.0 + wfun(K).sum(0)
    for trial in range(2):
        phi = rng.normal(size=N); pi = rng.normal(size=N)
        # dynamics: phidot = pi, pidot = -K phi (K has symbol W)
        phik = E @ phi; pik = E @ pi
        pidk = -Wk*phik; phidk = pik
        # density Fourier components at total q = a+b ; we evaluate the density at real-space cell x via
        # rho(x) = (1/N^2) sum_{a,b} kern(a,b) e^{i (a+b).(x+offset)} X_a Y_b   (centred phases)
        def dens(kern, Xa, Yb, off, x):
            ph = np.exp(1j*((K[:, :, None] + K[:, None, :]) * (x + off)[:, None, None]).sum(0))
            return np.sum(kern*ph*Xa[:, None]*Yb[None, :])/N**2
        res_E = []; res_M = []
        for x in [np.array([0, 0]), np.array([3, 5])]:
            zero = np.zeros(2)
            # dT00/dt
            Tdot = dens(np.ones((N, N))*0.5, pidk, pik, zero, x) + dens(np.ones((N, N))*0.5, pik, pidk, zero, x) \
                 + dens(0.5*C, phidk, phik, zero, x) + dens(0.5*C, phik, phidk, zero, x)
            divP = 0
            for j in range(2):
                e = np.eye(2)[j]
                Pp = dens(1j*ratio[j], pik, phik, e/2, x)        # P_j at x + e_j/2
                Pm = dens(1j*ratio[j], pik, phik, -e/2, x)       # P_j at x - e_j/2
                divP += Pp - Pm
            res_E.append(abs(Tdot + divP)/max(abs(Tdot), 1e-30))
            # (M): dP_j/dt + G[T]_j at edge x + e_j/2
            for j in range(2):
                e = np.eye(2)[j]
                Pdot = dens(1j*ratio[j], pidk, phik, e/2, x) + dens(1j*ratio[j], pik, phidk, e/2, x)
                GT = 0
                for i in range(2):
                    ei = np.eye(2)[i]
                    Tij = ratio[i]*ratio[j]           # phi_a phi_b kernel (dw_i dw_j / 4 qh_i qh_j)
                    off_p = (e/2) + (ei/2); off_m = (e/2) - (ei/2)   # T_ij located at x+e_j/2 +- e_i/2
                    GT += dens(Tij, phik, phik, off_p, x) - dens(Tij, phik, phik, off_m, x)
                res_M.append(abs(Pdot + GT)/max(abs(Pdot), 1e-30))
        print(f"  {label:6s} L={L} trial {trial}: max rel residual (E) = {max(res_E):.2e}, (M) = {max(res_M):.2e}")

print("\n== (b) exact identities (E),(M) with the 09-14 placement, random classical fields, 2D odd torus ==")
rng = np.random.default_rng(7)
check_identities(9, w_nn, np.sin, "NN-KG", rng)
check_identities(9, w_slac, saw, "SLAC", rng)
check_identities(11, w_slac, saw, "SLAC", rng)
# sign/consistency control: a WRONG current (sawtooth density -i saw(b) pi_a phi_b) with NN-KG energy density
print(f"  [{time.time()-t0:.1f}s]")

# ---------------- (c) real-space tails, 1D (axis structure is exactly 1D for separable laws) ----------------
print("\n== (c) real-space tails of P (pi_y phi_z coefficient) and T_jj (phi_y phi_z), 1D, density at origin ==")
def tails_1d(L, wfun, dsym):
    k = 2*np.pi*np.fft.fftfreq(L)
    a = k[:, None]; b = k[None, :]
    q = a + b; qh = 2*np.sin(q/2)
    with np.errstate(divide='ignore', invalid='ignore'):
        r = (wfun(a) - wfun(b))/(2*qh)
    bad = np.abs(qh) < 1e-12
    r[bad] = np.broadcast_to(dsym(a), r.shape)[bad]
    # coefficient of pi_y phi_z in P at edge 1/2: (1/L^2) sum_{a,b} i r(a,b) e^{i(a+b)/2} e^{-i a y} e^{-i b z}
    Pk = 1j*r*np.exp(1j*q/2)
    Tk = (r*r)*np.exp(1j*q*0)           # T_jj at site 0 : phases from qhat^2 shift integer -> centred at 0
    Pyz = np.fft.fft2(Pk)/L**2           # fft2 gives sum e^{-i a y - i b z}
    Tyz = np.fft.fft2(Tk)/L**2
    y = np.fft.fftfreq(L)*L
    Yd = np.abs(y[:, None] - 0.5); Zd = np.abs(y[None, :] - 0.5)
    D = np.maximum(Yd, Zd)
    Yd2 = np.abs(y[:, None]); Zd2 = np.abs(y[None, :]); D2 = np.maximum(Yd2, Zd2)
    out = []
    for R in [4, 8, 16, 32, 64, 128]:
        mP = np.max(np.abs(Pyz)[(D >= R-0.5) & (D < R+0.5)])
        mT = np.max(np.abs(Tyz)[(D2 >= R-0.5) & (D2 < R+0.5)])
        sP = np.sum(np.abs(Pyz)[D >= R]); sT = np.sum(np.abs(Tyz)[D2 >= R])
        out.append((R, mP, mT, sP, sT))
    return out
for lab, wf, ds in [("NN-KG", w_nn, np.sin), ("SLAC", w_slac, saw)]:
    out = tails_1d(1025, wf, ds)
    print(f"  {lab}:   R    max|P coef| at dist R   max|T coef|   sum|P| beyond R   sum|T| beyond R")
    for R, mP, mT, sP, sT in out:
        print(f"         {R:4d}   {mP:.3e}            {mT:.3e}      {sP:.3e}        {sT:.3e}")
    if lab == "SLAC":
        Rs = np.array([o[0] for o in out]); mP = np.array([o[1] for o in out]); mT = np.array([o[2] for o in out])
        sP = np.array([o[3] for o in out])
        print(f"  SLAC tail exponents (fit R=16..128): max|P| ~ R^{np.polyfit(np.log(Rs[2:]), np.log(mP[2:]), 1)[0]:.2f}, "
              f"max|T| ~ R^{np.polyfit(np.log(Rs[2:]), np.log(mT[2:]), 1)[0]:.2f}, sum|P| beyond R ~ R^{np.polyfit(np.log(Rs[2:]), np.log(sP[2:]), 1)[0]:.2f}")
# the momentum density proper -pi (D phi): kernel D(r) = Fourier of i saw(k)
L = 1025; k = 2*np.pi*np.fft.fftfreq(L); Dr = np.fft.fft(1j*saw(k))/L; r = np.fft.fftfreq(L)*L
print("  sawtooth derivative kernel |D(r)| * r (-> 1 means 1/r tail):", [f"{abs(Dr[int(R)])*R:.4f}" for R in [4, 16, 64, 256]])
print(f"[{time.time()-t0:.1f}s]")
