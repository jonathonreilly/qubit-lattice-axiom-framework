"""R19-22 s1: how fast does a finite site space reproduce ONE canonical pair (and two coupled pairs)?

Pre-registered (written before running, 06:25Z):
 (1) Holstein-Primakoff spin-S: h = S^y/sqrt(S), E = S^z/sqrt(S); H = (E^2 + h^2)/2.
     Expect level spacing 1 - (2n+1)/(2S): error POLYNOMIAL ~ 1/S.
 (2) Z_N clock in CCR scaling: delta = sqrt(2 pi/N), h = delta*n (centered labels), E = delta*m in the
     DFT basis (centered labels); H = (E^2 + h^2)/2 with the diagonal (kinked) quadratics.
     Expect error EXPONENTIALLY small, ~ exp(-pi N/2) up to powers.
 (3) Two coupled pairs, H = (E1^2+E2^2)/2 + (h^T M h)/2, M = [[1+kap,-kap],[-kap,1+kap]]:
     normal modes 1 and sqrt(1+2 kap). Same scalings expected for the two lowest one-quantum gaps.
 (4) Commutator defect: D := 1 - [h,E]/i has trace = dim (finite-dim trace identity).
     HP: D = n/S (eigenvalues 0..2). Clock: D concentrated at the wrap.
Subtraction: none (errors are |gap - exact CCR gap|).
"""
import numpy as np
np.set_printoptions(precision=4, suppress=False, linewidth=140)

def spin_ops(S):
    d = int(round(2*S + 1)); m = S - np.arange(d)            # S^z eigenvalues S..-S
    Sp = np.zeros((d, d))
    for i in range(1, d):
        Sp[i-1, i] = np.sqrt(S*(S+1) - m[i]*(m[i]+1))
    Sx = (Sp + Sp.T)/2; Sy = (Sp - Sp.T)/(2j); Sz = np.diag(m)
    return Sx, Sy, Sz

def clock_ops(N):
    delta = np.sqrt(2*np.pi/N)
    n = np.arange(N); n = np.where(n < (N+1)//2, n, n - N)    # centered labels
    h = np.diag(delta*n.astype(float))
    F = np.exp(2j*np.pi*np.outer(np.arange(N), np.arange(N))/N)/np.sqrt(N)
    E = F @ np.diag(delta*n.astype(float)) @ F.conj().T       # Fourier-conjugate quadratic label
    return h, E

print("(1) HP spin-S single pair, H=(E^2+h^2)/2: gaps vs exact 1")
print(" S     gap01-1        gap12-1        pred -(1)/(2S)  pred -(3)/(2S)")
for S in [2, 4, 8, 16, 32, 64, 128, 256]:
    Sx, Sy, Sz = spin_ops(S)
    h = Sy/np.sqrt(S); E = Sz/np.sqrt(S)
    H = (E@E + h@h)/2
    w = np.linalg.eigvalsh(H)
    # (Sy^2+Sz^2) = S(S+1) - Sx^2: levels doubly degenerate (Sx=+-(S-n)); take distinct values
    u = np.unique(np.round(w, 10))
    print(f"{S:4d}  {u[1]-u[0]-1:+.3e}  {u[2]-u[1]-1:+.3e}   {-1/(2*S):+.3e}      {-3/(2*S):+.3e}")

print("\n(2) Z_N clock (CCR scaling) single pair, H=(E^2+h^2)/2: gaps vs exact 1")
print(" N     gap01-1        gap12-1        exp(-pi N/2)")
rows = []
for N in [8, 12, 16, 20, 24, 28, 32, 40, 48]:
    h, E = clock_ops(N)
    H = (E@E + h@h).real/2
    w = np.linalg.eigvalsh((H + H.T)/2)
    e01 = w[1]-w[0]-1; e12 = w[2]-w[1]-1
    rows.append((N, abs(e01)))
    print(f"{N:4d}  {e01:+.3e}  {e12:+.3e}   {np.exp(-np.pi*N/2):.3e}")
Ns = np.array([r[0] for r in rows if r[1] > 1e-13]); errs = np.array([r[1] for r in rows if r[1] > 1e-13])
if len(Ns) >= 3:
    sl = np.polyfit(Ns, np.log(errs), 1)[0]
    print(f" fitted log-error slope vs N (points with err>1e-13): {sl:.4f}   (pi/2 = {np.pi/2:.4f})")

print("\n(3) two coupled pairs, kap=0.7: exact modes 1 and sqrt(1+2kap)=%.6f" % np.sqrt(2.4))
kap = 0.7; M = np.array([[1+kap, -kap], [-kap, 1+kap]]); wexact = sorted([1.0, np.sqrt(1+2*kap)])
print(" HP:  S    err(lowest 1-quantum gap)  err(second)")
for S in [2, 4, 8, 16, 24, 32]:
    Sx, Sy, Sz = spin_ops(S); d = Sx.shape[0]; I = np.eye(d)
    h1 = np.kron(Sy, I)/np.sqrt(S); h2 = np.kron(I, Sy)/np.sqrt(S)
    E1 = np.kron(Sz, I)/np.sqrt(S); E2 = np.kron(I, Sz)/np.sqrt(S)
    H = (E1@E1 + E2@E2 + M[0,0]*h1@h1 + M[1,1]*h2@h2 + 2*M[0,1]*h1@h2)/2
    w = np.linalg.eigvalsh((H + H.conj().T)/2)
    # HP vacuum sector: lowest state; the lowest two distinct excitation gaps
    u = np.unique(np.round(w - w[0], 9))
    print(f"      {S:3d}   {u[1]-wexact[0]:+.3e}               {u[2]-wexact[1]:+.3e}")
print(" clock: N  err(lowest gap)  err(second)")
for N in [8, 12, 16, 20, 24, 32, 40]:
    h, E = clock_ops(N); I = np.eye(N)
    h1 = np.kron(h, I); h2 = np.kron(I, h); E1 = np.kron(E, I); E2 = np.kron(I, E)
    H = (E1@E1 + E2@E2 + M[0,0]*h1@h1 + M[1,1]*h2@h2 + 2*M[0,1]*h1@h2)/2
    H = (H + H.conj().T)/2
    w = np.linalg.eigvalsh(H)
    g = w[1:6] - w[0]
    print(f"      {N:3d}   {g[0]-wexact[0]:+.3e}        {g[1]-wexact[1]:+.3e}")

print("\n(4) commutator defect D = 1 - [h,E]/i: trace and spectrum")
for S in [4, 16]:
    Sx, Sy, Sz = spin_ops(S); h = Sy/np.sqrt(S); E = Sz/np.sqrt(S)
    C = (h@E - E@h)/1j; D = np.eye(C.shape[0]) - C
    ev = np.linalg.eigvalsh((D + D.conj().T)/2)
    print(f" HP S={S}: tr D = {np.trace(D).real:.6f} (dim {C.shape[0]}); eig(D) min/max = {ev.min():.4f}/{ev.max():.4f};"
          f" D == (S - Sx)/S: {np.allclose(D, (S*np.eye(C.shape[0]) - Sx)/S)}")
for N in [16, 32]:
    h, E = clock_ops(N); C = (h@E - E@h)/1j; D = np.eye(N) - C
    ev = np.linalg.eigvalsh((D + D.conj().T)/2)
    print(f" clock N={N}: tr D = {np.trace(D).real:.6f} (dim {N}); eig(D) sorted ends: {np.round(ev[:3],4)} ... {np.round(ev[-3:],4)}")
