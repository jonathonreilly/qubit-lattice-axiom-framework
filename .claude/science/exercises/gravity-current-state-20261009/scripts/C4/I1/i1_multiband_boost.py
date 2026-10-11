# I1 check 1: multi-band generalization of the C3 boost condition.
# One-particle fibres on Z (d=1) with N orbitals per cell at intra-cell positions r_a.
# X = i d/dk + S (S = diag r_a).  For decomposable A: i[X,A] = -(dA - i[S,A]) =: -D A.
# K = 1/2{X,h} + a ;  P := i[h,K] = 1/2{Dh,h} + i[h,a]  (total energy current).
# Closure targets: [h,P]=0 (P conserved) and Q := 1/2{DP,h} - i[a,P] = beta*h  (i[K,P] = -beta H).
# Prediction (proved in report): choosing a to make P band-diagonal fixes a uniquely off-diagonal,
# then Q is band-diagonal identically with Q_aa = E_a * u_a'' , u_a = E_a^2/2.
import numpy as np
rng = np.random.default_rng(7)
N, R = 3, 2
hR = {r: rng.normal(size=(N,N)) + 1j*rng.normal(size=(N,N)) for r in range(-R, R+1)}
hR[0] = hR[0] + hR[0].conj().T + np.diag([-4.0, 0.0, 4.0])   # separate bands
for r in range(1, R+1):
    hR[-r] = hR[r].conj().T
S = np.diag(rng.uniform(0, 1, N))
def h(k):  return sum(M*np.exp(1j*k*r) for r, M in hR.items())
def dh(k): return sum(1j*r*M*np.exp(1j*k*r) for r, M in hR.items())
def D(A, dA): return dA - 1j*(S@A - A@S)
def anti(A, B): return A@B + B@A
def parts(k, improve=True):
    H = h(k); E, V = np.linalg.eigh(H)
    Dh = D(H, dh(k))
    Dh_b = V.conj().T @ Dh @ V
    a_b = np.zeros((N,N), complex)
    if improve:
        for i in range(N):
            for j in range(N):
                if i != j:
                    a_b[i,j] = 1j*(E[i]+E[j])*Dh_b[i,j]/(2*(E[i]-E[j]))
    a = V @ a_b @ V.conj().T
    P = 0.5*anti(Dh, H) + 1j*(H@a - a@H)
    return H, E, V, a, P
eps = 1e-5
ks = np.linspace(-np.pi, np.pi, 41)[:-1]
maxcomm_naive = maxcomm = maxoff = maxdiag = 0.0
hermit = 0.0
for k in ks:
    H, E, V, a0, P0 = parts(k, improve=False)
    maxcomm_naive = max(maxcomm_naive, np.abs(H@P0 - P0@H).max())
    H, E, V, a, P = parts(k)
    hermit = max(hermit, np.abs(a - a.conj().T).max())
    maxcomm = max(maxcomm, np.abs(H@P - P@H).max())
    Pp = parts(k+eps)[4]; Pm = parts(k-eps)[4]
    DP = D(P, (Pp - Pm)/(2*eps))
    Q = 0.5*anti(DP, H) - 1j*(a@P - P@a)
    Qb = V.conj().T @ Q @ V
    # predicted diagonal: E_a * u_a''  with u_a = E_a^2/2, via finite differences of sorted eigenvalues
    Ep = np.linalg.eigvalsh(h(k+1e-4)); Em = np.linalg.eigvalsh(h(k-1e-4))
    upp = ((Ep**2/2) - 2*(E**2/2) + (Em**2/2))/1e-8
    maxoff = max(maxoff, np.abs(Qb - np.diag(np.diag(Qb))).max())
    maxdiag = max(maxdiag, np.abs(np.real(np.diag(Qb)) - E*upp).max()/np.abs(E*upp).max())
print("N=%d bands, range %d, random analytic h(k), intra-cell positions %s" % (N, R, np.round(np.diag(S).real,3)))
print("naive boost (a=0): max |[h,P]| =", "%.3e" % maxcomm_naive, " (total energy current NOT conserved)")
print("improved boost a = band-projected: a hermitian err %.1e ; max |[h,P]| = %.2e" % (hermit, maxcomm))
print("Q = i[P,K]-type closure operator: max off-diagonal (band basis) = %.2e" % maxoff)
print("rel. error of diag(Q) vs E_a * u_a'' :", "%.2e" % maxdiag)
# zone averages of u_a'' per band (closure needs u''=beta everywhere; periodic => average 0)
kk = np.linspace(-np.pi, np.pi, 4097)[:-1]; dk = kk[1]-kk[0]
U = np.array([np.linalg.eigvalsh(h(k))**2/2 for k in kk])
upp = (np.roll(U,-1,0) - 2*U + np.roll(U,1,0))/dk**2
print("zone-average of u_a'' per (energy-sorted) band:", np.round(upp.mean(0), 12), " -> anomaly (u''-beta) averages -beta in every band")
print("max |u_a''| per band (closure would need const beta):", np.round(np.abs(upp).max(0), 3))
