# GUIDE only: exact numerics of the level crossing in the abelian analogue (Z_6, 2D spatial torus Lx x Ly).
# Per winding sector (mx,my) the electric basis is heights h in Z_6^V with h[0]=0 fixed (dimension 6^(V-1)).
# L = K^{1/2} e^{bM} K^{1/2}, K = prod_e w[q_e], e^{bM} = prod_p (convolution in h_p by the Z_6 Fourier coefficients of e^{b cos}).
# p_{s,b} = sum_{mx odd} Tr L^a / sum_all Tr L^a;  J_b/Lx = (1/(a Lx)) log(p_S/p_1).
import numpy as np, itertools, sys
N = 6
def sector_matrix(Lx, Ly, w, b, mx, my):
    V = Lx*Ly; dim = N**(V-1)
    hs = np.array(list(itertools.product(range(N), repeat=V-1)), dtype=np.int64)   # h for plaquettes 1..V-1
    h = np.concatenate([np.zeros((dim,1),dtype=np.int64), hs], axis=1).reshape(dim, Lx, Ly)
    logw = np.zeros(dim); lw = np.log(w)
    for x in range(Lx):
        for y in range(Ly):
            qh = (h[:,x,y] - h[:,x,(y-1)%Ly] + (mx if y==0 else 0)) % N
            qv = (h[:,(x-1)%Lx,y] - h[:,x,y] + (my if x==0 else 0)) % N
            logw += lw[qh] + lw[qv]
    Kh = np.exp(0.5*logw)
    # index map
    mult = N**np.arange(V-2, -1, -1)
    def index(hfull):   # hfull shape (dim, V) with arbitrary h0; subtract h0
        hh = (hfull[:,1:] - hfull[:,[0]]) % N
        return hh @ mult
    hflat = h.reshape(dim, V)
    c = np.array([np.mean([np.exp(b*np.cos(2*np.pi*m/N))*np.cos(2*np.pi*m*k/N) for m in range(N)]) for k in range(N)])
    B = np.eye(dim)
    for p in range(V):
        Cp = np.zeros((dim,dim))
        for k in range(N):
            h2 = hflat.copy(); h2[:,p] = (h2[:,p] + k) % N
            Cp[index(h2), np.arange(dim)] += c[k]
        B = Cp @ B
    A = (Kh[:,None]*B)*Kh[None,:]
    return 0.5*(A+A.T)
def pfrac(Lx, Ly, w, b, a):
    lo = []; le = []
    for mx in range(N):
        for my in range(N):
            ev = np.linalg.eigvalsh(sector_matrix(Lx, Ly, w, b, mx, my))
            ev = np.clip(ev, 1e-300, None)
            (lo if mx % 2 else le).append(a*np.log(ev))
    lo = np.concatenate(lo); le = np.concatenate(le)
    def lse(v):
        m = v.max(); return m + np.log(np.exp(v-m).sum())
    return lse(lo) - lse(np.concatenate([lo,le]))     # log p
Lx, Ly, a = 2, 2, 600
w1 = np.array([1.0, 0.48, 0.17, 0.0018, 0.17, 0.48]); wS = w1.copy(); wS[3] = 0.485
gam = np.log(0.485/0.48)
print(f"Z6 {Lx}x{Ly}, a={a}: gamma' = {gam:.5f} per unit area at b=0")
print("  b      -log p_1/(a Lx)   -log p_S/(a Lx)    J_b/Lx      (J_b/Lx)/gamma'")
prev = None
for b in (0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5, 0.7, 1.0, 1.5, 2.3):
    l1 = pfrac(Lx, Ly, w1, b, a); lS = pfrac(Lx, Ly, wS, b, a)
    J = (lS - l1)/(a*Lx)
    print(f"  {b:4.2f}   {-l1/(a*Lx):.5f}          {-lS/(a*Lx):.5f}          {J:+.6f}   {J/gam:+.4f}")
