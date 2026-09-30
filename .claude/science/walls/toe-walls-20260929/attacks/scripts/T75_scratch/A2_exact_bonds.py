"""High-precision entanglement Hamiltonian bonds near the cut (mpmath) to calibrate Test A.
Wedge = sites 1..Mw of the infinite half-filled chain.  h = ln((1-C)/C).
Compare bond h[j,j+1] with pi*(j+1/2)*s and report s(j)."""
import mpmath as mp
mp.mp.dps = 120
Mw = 60
C = mp.matrix(Mw, Mw)
for i in range(Mw):
    for j in range(Mw):
        d = i - j
        C[i, j] = mp.mpf(1)/2 if d == 0 else mp.sin(mp.pi*d/2)/(mp.pi*d)
E, Q = mp.eigsy(C)
h = mp.matrix(Mw, Mw)
D = mp.matrix(Mw, Mw)
for k in range(Mw):
    nu = E[k]
    D[k, k] = mp.log((1-nu)/nu)
h = Q*D*Q.T
print("bond j: h[j,j+1] (sign -> hopping -t), and h/(pi*(j+1/2))")
for j in range(1, 16):
    v = h[j-1, j]
    print(j, mp.nstr(v, 8), mp.nstr(-v/(mp.pi*(j+mp.mpf(1)/2)), 8), mp.nstr(-v/(mp.pi*mp.sqrt(j*(j+1))), 8))
print("onsite h[j,j] (should be ~0):", [mp.nstr(h[j,j], 4) for j in range(0,6)])
