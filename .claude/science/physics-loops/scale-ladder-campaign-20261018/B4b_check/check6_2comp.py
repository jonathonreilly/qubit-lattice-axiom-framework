"""Own vectorised re-computation of the repo's 2-comp Cl(3) 'conserved vertex + k-independent seagull' scheme
(frontier_universal_gr_stress_ward_transverse_seagull.py). A k-independent seagull tadpole can only remove Pi(0);
test the O(k^3) residual RELATIVE to the O(k^2) TT signal (symbol-level Ward ratio)."""
import numpy as np
s = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]],complex), np.array([[1,0],[0,-1]],complex)]
S = np.array(s)
def Dm(q, m): return 1j*np.einsum('ni,iab->nab', np.sin(q), S) + m*np.eye(2)
def Gm(q, m): return np.linalg.inv(Dm(q, m))
def Vc(q, k):  # V_cd = (i/2)(sig_c cos(q_c+k_c/2) sbar_d + c<->d), sbar_d = (sin q_d + sin(q_d+k_d))/2
    u = 1j*np.einsum('ni,iab->inab', np.cos(q + k/2), S)
    sb = 0.5*(np.sin(q) + np.sin(q + k))
    V = 0.5*(np.einsum('cnab,nd->cdnab', u, sb) + np.einsum('dnab,nc->cdnab', u, sb))
    return V
def Pi(k, N, m):
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    q = np.stack(np.meshgrid(p, p, p, indexing='ij'), -1).reshape(-1, 3)
    G0, G1 = Gm(q, m), Gm(q + k, m)
    V1 = Vc(q, k); V2 = Vc(q + k, -k)
    A = np.einsum('nab,ijnbc->ijnac', G0, V1); B = np.einsum('nab,klnbc->klnac', G1, V2)
    return np.einsum('ijnab,klnba->ijkl', A, B) / len(q)
m, N = 1.0, 24
P0 = Pi(np.zeros(3), N, m)
for k0 in (0.4, 0.2, 0.1):
    k = np.array([k0, 0, 0]); Pk = Pi(k, N, m) - P0
    res = np.abs(np.einsum('i,ijkl->jkl', 2*np.sin(k/2), Pk)).max()
    tt = (Pk[1,2,1,2]).real / (2 - 2*np.cos(k0))
    print("k0 %.2f  max|khat.(Pi-Pi0)|/k0^3 = %.5f   TT(yz) k^2-slope = %.5f   ratio = %.3f" % (k0, res/k0**3, tt, res/k0**3/abs(tt)))
