"""Lemma C escape hatch: a divergence-free 'harmonic' improvement with a transverse-projector symbol.
w_j(q) = Pi_jl(q) c_l,  Pi_jl = delta_jl - conj(u_j) u_l/|u|^2,  u_j = 1 - e^{-i q_j}.  sum_j u_j Pi_jl = 0 for q != 0,
Pi(q->0) is direction dependent (no limit), so the q=0 total can be set freely. Real-space kernel ~ R^-d (not l^1).
"""
import numpy as np
out=[]
for L in [128, 256, 512]:
    q = 2*np.pi*np.fft.fftfreq(L)
    qx, qy = np.meshgrid(q, q, indexing='ij')
    ux, uy = 1-np.exp(-1j*qx), 1-np.exp(-1j*qy)
    n2 = np.abs(ux)**2 + np.abs(uy)**2; n2[0,0] = 1
    Pxy = -np.conj(ux)*uy/n2; Pxy[0,0] = 0
    Pxx = 1 - np.conj(ux)*ux/n2; Pxx[0,0] = 1
    div = np.abs(ux*Pxx + uy*(-np.conj(uy)*ux/n2)); div[0,0]=0
    K = np.fft.ifft2(Pxy)
    R = [4, 8, 16, 32]
    vals = [abs(K[r, r]) for r in R]
    sl = np.polyfit(np.log(R), np.log(vals), 1)[0]
    l1 = [np.abs(K[:r, :r]).sum() + np.abs(K[-r:, :r]).sum() + np.abs(K[:r, -r:]).sum() + np.abs(K[-r:, -r:]).sum() for r in [L//8, L//4, L//2]]
    s = f"L={L}: max|div|={div.max():.1e}; |K_xy(R,R)| slope vs R = {sl:.3f}; l1 partial sums over boxes L/8,L/4,L/2: " + ', '.join(f"{v:.3f}" for v in l1)
    print(s); out.append(s)
open('c1_harmonic.out','w').write('\n'.join(out)+'\n')
