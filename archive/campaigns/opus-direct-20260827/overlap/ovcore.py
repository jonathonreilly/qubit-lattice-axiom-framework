"""Generic 2d overlap machinery: any hermitian Clifford fibre {Gam_mu}, chirality CH.
D_W = 2r/a + sum_mu[ -(1/2a)(r-Gam_mu)U_mu S_mu^+ - (1/2a)(r+Gam_mu)U_mu^* S_mu^- ]
D_ov = (1/a)(1 + A(A^dag A)^{-1/2}),  A = D_W - m/a.
"""
import numpy as np

def gauge(L, n):
    U1 = lambda x, y: np.exp(-1j*2*np.pi*n*y/(L*L))
    U2 = lambda x, y: (np.exp(1j*2*np.pi*n*x/L) if y == L-1 else 1.0+0j)
    return U1, U2

def build_DW(L, n, Gam, r=1.0, a=1.0):
    f = Gam[0].shape[0]; N = L*L; If = np.eye(f, dtype=complex)
    D = np.zeros((f*N, f*N), dtype=complex); U1, U2 = gauge(L, n)
    ix = lambda x, y: x*L + y
    for x in range(L):
        for y in range(L):
            i = ix(x, y); D[f*i:f*i+f, f*i:f*i+f] += (2*r/a)*If
            for mu, (dx, dy) in enumerate([(1,0),(0,1)]):
                j = ix((x+dx) % L, (y+dy) % L); U = U1(x,y) if mu == 0 else U2(x,y)
                D[f*i:f*i+f, f*j:f*j+f] += -(1/(2*a))*(r*If - Gam[mu])*U
                D[f*j:f*j+f, f*i:f*i+f] += -(1/(2*a))*(r*If + Gam[mu])*np.conj(U)
    return D

def full_chir(L, CH):
    return np.kron(np.eye(L*L), CH)

def overlap_report(L, n, Gam, CH, mrho=1.0, r=1.0, a=1.0, extra_proj=None):
    DW = build_DW(L, n, Gam, r=r, a=a); C = full_chir(L, CH)
    if extra_proj is not None:
        P = extra_proj; DW = P.conj().T @ DW @ P; C = P.conj().T @ C @ P
    ch = np.max(np.abs(C @ DW @ C - DW.conj().T))                     # chiral-hermiticity
    A = DW - (mrho/a)*np.eye(DW.shape[0])
    U, S, Vh = np.linalg.svd(A); V = U @ Vh
    Dov = (1.0/a)*(np.eye(DW.shape[0]) + V)
    gw = np.max(np.abs(C @ Dov + Dov @ C - a*(Dov @ C @ Dov)))
    ind = 0.5*np.real(np.trace(C @ (2*np.eye(Dov.shape[0]) - a*Dov)))
    w, vecs = np.linalg.eig(V); k = np.where(np.abs(w+1) < 1e-8)[0]
    npl = nmi = 0
    if len(k):
        Q, _ = np.linalg.qr(vecs[:, k]); ev = np.linalg.eigvalsh(Q.conj().T @ C @ Q)
        npl = int(np.sum(ev > 0.5)); nmi = int(np.sum(ev < -0.5))
    return dict(chir_herm=ch, gw=gw, minSV=S.min(), index=ind,
                nzero=len(k), nplus=npl, nminus=nmi, trC=np.real(np.trace(C)), dim=DW.shape[0])

def table(name, L, Gam, CH, ns=(0,1,2,3), mrho=1.0, r=1.0, a=1.0, extra_proj=None):
    print(f"--- {name}  (L={L}, m_rho={mrho}, r={r}) ---")
    hdr = f"{'n':>3} {'chirherm':>10} {'GWviol':>11} {'minSV':>10} {'index':>11} {'nzero':>6} {'n+':>3} {'n-':>3}"
    print(hdr)
    res = []
    for n in ns:
        d = overlap_report(L, n, Gam, CH, mrho=mrho, r=r, a=a, extra_proj=extra_proj)
        print(f"{n:>3} {d['chir_herm']:10.2e} {d['gw']:11.3e} {d['minSV']:10.3e} "
              f"{d['index']:11.6f} {d['nzero']:>6} {d['nplus']:>3} {d['nminus']:>3}")
        res.append(d)
    print(f"    dim={res[0]['dim']}  Tr(chirality)={res[0]['trC']:.3e}")
    return res
