"""R7-1, script 1 (d = 2, free matter, one-body generators, real-space lattice check).

Law (one complex fermion mode per site of Z^2; free part only here):
  s(k)   = rho(k) k + (1 - rho(k)) sin k        C^inf, odd, 2pi-periodic, s = k on |k| <= B
  eps(k) = sqrt(m^2 + s(kx)^2 + s(ky)^2)        = sqrt(m^2 + |k|^2) on the box [-B, B]^2
  P_j    = s(k_j)  (smooth momentum; equals R6-1's sawtooth Q on the box)
  K_j    = (1/2){H, X_j}   (first moment of the Hamiltonian density; B1 Theorem S form)
  J      = (1/2)({X, j_y} - {Y, j_x}),  j = grad(eps^2/2) = (s s')(k_j)
Checks:
  (A) eps = sqrt(m^2+k^2) on the box; anomaly Hess(eps^2/2) - I zero on box, zone mean -I.
  (B) real-space kernel decay of eps and s (quasi-locality; super-polynomial, sub-exponential).
  (C) Poincare relations on an L x L torus, real-space operators applied by FFT, on
      wavepackets with compact momentum support inside / straddling / outside the box.
      Comparator: NN Klein-Gordon band eps_c^2 = m^2 + sum 4 sin^2(k/2), P = sin k.
  (D) leakage of a finite boost: lattice flow vs continuum flow; bound 2||1_E psi||.
"""
import numpy as np
np.set_printoptions(linewidth=150)

def sstep(x):                      # C^inf (Gevrey-2) step: 0 for x<=0, 1 for x>=1
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

B, B2, M = 2.0, 3.1, 0.3          # exact box |k_i| <= B; transition (B, B2); mass (lattice units)

def rho(k):
    return sstep((B2 - np.abs(wrap(k)))/(B2 - B))

def s(k):
    k = wrap(k); r = rho(k)
    return r*k + (1-r)*np.sin(k)

def dsstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
        d1 = np.where(x > 0, e1/np.where(x > 0, x, 1)**2, 0.0)
        d2 = np.where(x < 1, e2/np.where(x < 1, 1-x, 1)**2, 0.0)
    return (d1*e2 + e1*d2)/(e1+e2)**2

def ds(k):                         # exact derivative s'(k)
    k = wrap(k); r = rho(k)
    dr = -np.sign(k)*dsstep((B2 - np.abs(k))/(B2 - B))/(B2 - B)
    return dr*(k - np.sin(k)) + r + (1-r)*np.cos(k)

def d2s(k, h=1e-4):
    return (s(k+h) - 2*s(k) + s(k-h))/h**2

def eps(kx, ky, m=M):
    return np.sqrt(m*m + s(kx)**2 + s(ky)**2)

out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line); out.append(line)

# ---------------- (A) box exactness and the anomaly ----------------
kk = np.linspace(-np.pi, np.pi, 4001)[:-1]
inbox = np.abs(kk) <= B
pr('(A) max |s(k)-k| on |k|<=B :', np.max(np.abs(s(kk[inbox]) - kk[inbox])))
KX, KY = np.meshgrid(kk[::8], kk[::8], indexing='ij')
inb2 = (np.abs(KX) <= B) & (np.abs(KY) <= B)
pr('(A) max |eps - sqrt(m^2+k^2)| on box :', np.max(np.abs(eps(KX, KY)[inb2] - np.sqrt(M*M+KX[inb2]**2+KY[inb2]**2))))
anom = ds(kk)**2 + s(kk)*d2s(kk) - 1.0          # (Hess eps^2/2)_xx - 1 = (s s')' - 1
pr('(A) anomaly (s s\')\' - 1: max|.| on box = %.2e ; zone mean = %.6f (theory -1) ; min/max outside = %.3f / %.3f'
   % (np.max(np.abs(anom[inbox & (np.abs(kk) < B - 1e-3)])), anom.mean(), anom[~inbox].min(), anom[~inbox].max()))
pr('(A) s\'(k) (the "cos k factor") on box: max|s\'-1| = %.2e; at zone edge s\'(pi) = %.4f' %
   (np.max(np.abs(ds(kk[inbox & (np.abs(kk) < B-1e-3)]) - 1)), ds(np.array([np.pi-1e-6]))[0]))

# ---------------- (B) real-space kernels ----------------
N = 4096
k1 = 2*np.pi*np.fft.fftfreq(N)
s_r = np.abs(np.fft.ifft(s(k1)))   # s is odd: its kernel is imaginary
pr('(B) |s kernel|(r) for r = 1, 8, 32, 64, 128, 256, 512:', ['%.2e' % abs(s_r[r]) for r in [1, 8, 32, 64, 128, 256, 512]])
N2 = 1024
kq = 2*np.pi*np.fft.fftfreq(N2)
EX, EY = np.meshgrid(kq, kq, indexing='ij')
e_r = np.fft.ifft2(eps(EX, EY)).real
pr('(B) eps kernel, B = %.1f, transition to %.1f' % (B, B2))
pr('(B) |eps kernel|(r,0) for r = 1, 8, 32, 64, 128, 256, 512:', ['%.2e' % abs(e_r[r, 0]) for r in [1, 8, 32, 64, 128, 256, 512]])
pr('(B) |eps kernel|(r,r) for r = 1, 8, 32, 64, 128, 256:', ['%.2e' % abs(e_r[r, r]) for r in [1, 8, 32, 64, 128, 256]])
# stretched-exponential fit log|h| = c - a r^beta on the s kernel (axis), r in [16, 512]
rr = np.arange(16, 513); yy = np.log(np.abs(s_r[rr]) + 1e-300)
best = None
for beta in np.linspace(0.2, 1.0, 81):
    A_ = np.vstack([np.ones_like(rr, dtype=float), -rr**beta]).T
    coef, res, *_ = np.linalg.lstsq(A_, yy, rcond=None)
    r2 = np.sum((A_@coef - yy)**2)
    if best is None or r2 < best[0]:
        best = (r2, beta, coef)
pr('(B) stretched-exp fit to |s kernel| (rough; envelope oscillates): beta = %.2f, a = %.3f' % (best[1], best[2][1]))

# ---------------- (C) Poincare relations on an L x L torus ----------------
L = 512
kg = 2*np.pi*np.fft.fftfreq(L)
GX, GY = np.meshgrid(kg, kg, indexing='ij')
xg = np.fft.fftfreq(L)*L                     # centred coordinates in [-L/2, L/2)
XX, YY = np.meshgrid(xg, xg, indexing='ij')

def ops(model):
    if model == 'box':
        E = eps(GX, GY); PX = s(GX); PY = s(GY)
        jx = s(GX)*ds(GX); jy = s(GY)*ds(GY)
    else:                                     # NN Klein-Gordon comparator
        E = np.sqrt(M*M + 4*np.sin(GX/2)**2 + 4*np.sin(GY/2)**2)
        PX = np.sin(GX); PY = np.sin(GY); jx = np.sin(GX); jy = np.sin(GY)
    mult = lambda f: (lambda v: np.fft.ifft2(f*np.fft.fft2(v)))
    H = mult(E); Px = mult(PX); Py = mult(PY); Jx_ = mult(jx); Jy_ = mult(jy)
    X = lambda v: XX*v; Y = lambda v: YY*v
    Kx = lambda v: 0.5*(H(X(v)) + X(H(v)))
    Ky = lambda v: 0.5*(H(Y(v)) + Y(H(v)))
    J = lambda v: 0.5*(X(Jy_(v)) + Jy_(X(v))) - 0.5*(Y(Jx_(v)) + Jx_(Y(v)))
    return dict(H=H, Px=Px, Py=Py, Kx=Kx, Ky=Ky, J=J)

def comm(A, Bop, v):
    return A(Bop(v)) - Bop(A(v))

def packet(k0, w):
    d2 = wrap(GX-k0[0])**2 + wrap(GY-k0[1])**2
    ph = np.exp(-d2/(2*w*w))                  # Gaussian in k (weight beyond the box is reported)
    v = np.fft.ifft2(ph)
    return v/np.linalg.norm(v)

# relations, with conventions fixed by the continuum: [K_i,P_j]=i d_ij H, [K_i,H]=i P_i,
# [K_x,K_y] = c1 * i J, [J,K_x] = c2 * i K_y, [J,P_x] = c2 * i P_y, [J,H]=0 (c1, c2 = signs, measured)
def residuals(model, v):
    O = ops(model)
    n = np.linalg.norm
    r = {}
    r['[Kx,Px]-iH'] = n(comm(O['Kx'], O['Px'], v) - 1j*O['H'](v))
    r['[Kx,Py]'] = n(comm(O['Kx'], O['Py'], v))
    r['[Kx,H]-iPx'] = n(comm(O['Kx'], O['H'], v) - 1j*O['Px'](v))
    r['[Ky,H]-iPy'] = n(comm(O['Ky'], O['H'], v) - 1j*O['Py'](v))
    c = comm(O['Kx'], O['Ky'], v); Jv = O['J'](v)
    r['[Kx,Ky]+iJ'] = n(c + 1j*Jv); r['[Kx,Ky]-iJ'] = n(c - 1j*Jv)
    c = comm(O['J'], O['Kx'], v); Kyv = O['Ky'](v)
    r['[J,Kx]-iKy'] = n(c - 1j*Kyv); r['[J,Kx]+iKy'] = n(c + 1j*Kyv)
    c = comm(O['J'], O['Px'], v); Pyv = O['Py'](v)
    r['[J,Px]-iPy'] = n(c - 1j*Pyv); r['[J,Px]+iPy'] = n(c + 1j*Pyv)
    r['[J,H]'] = n(comm(O['J'], O['H'], v))
    r['[Px,H]'] = n(comm(O['Px'], O['H'], v))
    r['scale ||Kx v||'] = n(O['Kx'](v))
    return r

cases = [('inside box, k0=(0.4,-0.3), sig_k=0.12', (0.4, -0.3), 0.12),
         ('inside box, fast k0=(1.4,0.3), sig_k=0.08', (1.4, 0.3), 0.08),
         ('straddles box edge, k0=(2.0,0), sig_k=0.1', (2.0, 0.0), 0.1),
         ('outside box (zone edge), k0=(2.9,2.9), sig_k=0.08', (2.9, 2.9), 0.08)]
for label, k0, w in cases:
    v = packet(k0, w)
    seam = np.sqrt(np.sum(np.abs(v[np.abs(XX) > L/2 - 32])**2) + np.sum(np.abs(v[np.abs(YY) > L/2 - 32])**2))
    vk = np.abs(np.fft.fft2(v))**2; vk /= vk.sum()
    outw = np.sqrt(vk[(np.abs(GX) > B) | (np.abs(GY) > B)].sum())
    for model in ['box', 'cosKG']:
        r = residuals(model, v)
        pr('(C) %-48s %-6s ' % (label, model) + '  '.join('%s=%.1e' % (kq_, vq) for kq_, vq in r.items()))
    pr('(C)    packet weight within 32 sites of the seam: %.1e ; momentum weight outside the box: %.1e' % (seam, outw))

# ---------------- (D) finite-boost leakage ----------------
# boost along x: lattice flow dk_x/deta = eps(k) on the torus; continuum flow k_x -> m_perp sinh(theta+eta)
def lattice_flow(kx, ky, eta, nstep=300):
    h = eta/nstep; k = kx.copy()
    for _ in range(nstep):                    # RK4
        a1 = eps(k, ky); a2 = eps(k+0.5*h*a1, ky); a3 = eps(k+0.5*h*a2, ky); a4 = eps(k+h*a3, ky)
        k = k + h*(a1+2*a2+2*a3+a4)/6
    return k

nk = 301
kgrid = np.linspace(-np.pi, np.pi, nk, endpoint=False); dk = kgrid[1]-kgrid[0]
GX2, GY2 = np.meshgrid(kgrid, kgrid, indexing='ij')
sig = 0.25
psi = np.exp(-(GX2**2 + GY2**2)/(4*sig**2)); psi /= np.sqrt(np.sum(np.abs(psi)**2)*dk*dk)
pr('(D) Gaussian packet at rest, sigma_k = %.2f, m = %.2f, box B = %.2f' % (sig, M, B))
for eta in [0.5, 1.0, 1.5, 2.0]:
    # pull back: U_eta psi (k) = psi(Phi_{-eta} k) sqrt(eps(Phi_{-eta}k)/eps(k))
    kl = lattice_flow(GX2, GY2, -eta)
    # exact 2D evaluation of the Gaussian at the pulled-back point
    ul = np.exp(-(wrap(kl)**2 + GY2**2)/(4*sig**2))/np.sqrt(np.sum(np.exp(-(GX2**2+GY2**2)/(2*sig**2)))*dk*dk)
    ul = ul*np.sqrt(eps(kl, GY2)/eps(GX2, GY2))
    mp = np.sqrt(M*M + GY2**2)
    th = np.arcsinh(GX2/mp) - eta
    kc = mp*np.sinh(th)
    uc = np.exp(-(kc**2 + GY2**2)/(4*sig**2))/np.sqrt(np.sum(np.exp(-(GX2**2+GY2**2)/(2*sig**2)))*dk*dk)
    uc = uc*np.sqrt(np.sqrt(M*M+kc**2+GY2**2)/np.sqrt(M*M+GX2**2+GY2**2))
    # continuum image restricted to the zone (mass leaving the zone counts as leakage too)
    leak = np.sqrt(np.sum(np.abs(ul - uc)**2)*dk*dk + max(0.0, 1.0 - np.sum(np.abs(uc)**2)*dk*dk))
    # E_eta = points whose continuum orbit over [0, eta] leaves the exact box
    th0 = np.arcsinh(GX2/mp); kxe = mp*np.sinh(th0 + eta)
    E = (np.abs(GY2) > B) | (np.abs(kxe) > B) | (np.abs(GX2) > B)
    bound = 2*np.sqrt(np.sum(np.abs(psi[E])**2)*dk*dk)
    pr('(D) eta = %.1f : ||U_lat psi - U_cont psi|| = %.2e   bound 2||1_E psi|| = %.2e' % (eta, leak, bound))
pr('(D) compact-support statement: a packet with momenta in |k_x| <= k_max, |k_y| <= k_max has zero leakage for')
pr('    |eta| <= asinh(B/m_perp) - asinh(k_max/m_perp), m_perp = sqrt(m^2 + k_max^2)  (exact; no numerics needed)')
# physical rapidity budgets for a Planck-spacing lattice, B taken as 2.6 / l_P  (reading)
EP = 1.22e19  # GeV
for name, mGeV in [('electron', 5.11e-4), ('proton', 0.938), ('top', 173.0)]:
    pr('(D) rapidity reach at rest for %-8s : asinh(B E_P / m) = %.1f' % (name, np.arcsinh(B*EP/mGeV)))
pr('(D) a 3e20 eV proton in the lattice frame has rapidity %.1f; remaining budget %.1f'
   % (np.arcsinh(3e11/0.938), np.arcsinh(B*EP/0.938) - np.arcsinh(3e11/0.938)))

with open(__file__.replace('.py', '.out'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
