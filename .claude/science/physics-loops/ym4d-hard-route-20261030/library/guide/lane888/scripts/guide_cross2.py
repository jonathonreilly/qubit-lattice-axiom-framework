# GUIDE only: flux tensions of the two carriers in the abelian analogue, to all orders in b (top eigenvalues).
# Z_6 on an Lx x Ly spatial torus. Winding sector mx carries the flux; charge-1 carrier lives in mx=1, charge-3 in mx=3.
# sigma_c(b) = -(1/Lx) log( lambda_max(mx=c, my=0) / lambda_max(0,0) ) for L = K^{1/2} e^{bM} K^{1/2}  (time -> infinity limit).
import numpy as np, itertools, sys
N = 6
class Sector:
    def __init__(self, Lx, Ly):
        self.Lx, self.Ly = Lx, Ly; V = Lx*Ly; self.V = V; dim = N**(V-1); self.dim = dim
        hs = np.array(list(itertools.product(range(N), repeat=V-1)), dtype=np.int64)
        self.h = np.concatenate([np.zeros((dim,1),dtype=np.int64), hs], axis=1)
        mult = N**np.arange(V-2, -1, -1)
        self.perm = []
        for p in range(V):
            row = []
            for k in range(N):
                h2 = self.h.copy(); h2[:,p] = (h2[:,p] + k) % N
                row.append(((h2[:,1:] - h2[:,[0]]) % N) @ mult)
            self.perm.append(row)
    def Khalf(self, w, mx, my):
        Lx, Ly = self.Lx, self.Ly; h = self.h.reshape(self.dim, Lx, Ly); lw = np.log(w); logw = np.zeros(self.dim)
        for x in range(Lx):
            for y in range(Ly):
                qh = (h[:,x,y] - h[:,x,(y-1)%Ly] + (mx if y==0 else 0)) % N
                qv = (h[:,(x-1)%Lx,y] - h[:,x,y] + (my if x==0 else 0)) % N
                logw += lw[qh] + lw[qv]
        return np.exp(0.5*logw)
    def top(self, w, b, mx, my, steps=140):
        Kh = self.Khalf(w, mx, my)
        c = np.array([np.mean([np.exp(b*np.cos(2*np.pi*m/N))*np.cos(2*np.pi*m*k/N) for m in range(N)]) for k in range(N)])
        def A(v):
            u = Kh*v
            for p in range(self.V):
                u = sum(c[k]*u[self.perm[p][k]] for k in range(N))
            return Kh*u
        # Lanczos with full reorthogonalization, start from K-weighted vector
        rng = np.random.default_rng(1); q = Kh**4 + 1e-3*rng.random(self.dim); q /= np.linalg.norm(q)
        Q = [q]; al = []; be = []
        for j in range(steps):
            z = A(Q[-1]); a_ = Q[-1] @ z; al.append(a_)
            z = z - a_*Q[-1] - (be[-1]*Q[-2] if be else 0)
            for qq in Q: z -= (qq @ z)*qq
            nb = np.linalg.norm(z)
            if nb < 1e-13: break
            be.append(nb); Q.append(z/nb)
        T = np.diag(al) + np.diag(be[:len(al)-1],1) + np.diag(be[:len(al)-1],-1)
        return np.linalg.eigvalsh(T)[-1]
Lx, Ly = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (3, 2)
S_ = Sector(Lx, Ly)
w1 = np.array([1.0, 0.48, 0.17, 0.0018, 0.17, 0.48]); wS = w1.copy(); wS[3] = 0.485
gam = np.log(0.485/0.48); v = lambda x: (1+x)/(1-x)
D1 = 0.25*v(0.48**2) + 0.25*v(0.17*0.48**2) - 0.5*v(0.48**4)
D3 = 0.5*v(0.17*0.48**3/0.485) - 0.5*v(0.48**4)
print(f"Z6 {Lx}x{Ly}: gamma' = {gam:.5f}; second-order prediction sigma_1 = {-np.log(0.48):.5f} - {D1:.4f} b^2, sigma_3 = {-np.log(0.485):.5f} - ({D3:.4f}) b^2, crossing b* = {np.sqrt(gam/(D1-D3)):.3f}")
print("   b     sig_1 (s=1)  sig_1 (s=S)  sig_3 (s=S)   pred sig_1  pred sig_3   J/Lx = sig_1(1) - min(sig_1,sig_3)(S)   over gamma'")
for b in (0.0, 0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5, 0.7, 1.0, 1.5, 2.3):
    l0_1 = S_.top(w1, b, 0, 0); l0_S = S_.top(wS, b, 0, 0)
    s1_1 = -np.log(S_.top(w1, b, 1, 0)/l0_1)/Lx
    s1_S = -np.log(S_.top(wS, b, 1, 0)/l0_S)/Lx
    s3_S = -np.log(S_.top(wS, b, 3, 0)/l0_S)/Lx
    J = s1_1 - min(s1_S, s3_S)
    print(f"  {b:4.2f}   {s1_1:.5f}      {s1_S:.5f}      {s3_S:.5f}       {-np.log(0.48)-D1*b*b:.5f}     {-np.log(0.485)-D3*b*b:.5f}      {J:+.6f}                         {J/gam:+.4f}")
