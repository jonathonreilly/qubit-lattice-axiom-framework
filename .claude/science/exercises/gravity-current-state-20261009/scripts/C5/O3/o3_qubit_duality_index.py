# O3 part 2b: (a) Jordan-Wigner duality is one spectrum, not a pair; (b) no CCR boson on a finite site;
# (c) Witten index sdim of the hard-core (M1) space on 2D/3D tori by transfer matrix; (d) naive-strain cusp.
import numpy as np, itertools, sys
sys.path.insert(0, '.')

# (a) 1D XX chain of qubits (hard-core bosons) vs JW free fermions
L = 10
sp_ = np.array([[0,1],[0,0]]); sm = sp_.T; I2 = np.eye(2); Z = np.diag([1,-1])
def op(o, i):
    out = np.array([[1.0]])
    for j in range(L): out = np.kron(out, o if j==i else I2)
    return out
H = np.zeros((2**L,2**L))
for i in range(L):
    j = (i+1)%L
    H -= op(sp_,i)@op(sm,j) + op(sm,i)@op(sp_,j)
ev_q = np.sort(np.linalg.eigvalsh(H))
# JW: sector with N particles has fermion BC periodic if N odd, antiperiodic if N even (for this sign convention)
ev_f = []
for N in range(L+1):
    for bc in ([0.0] if N%2==1 else [0.5]):
        k = 2*np.pi*(np.arange(L)+bc)/L; e = -2*np.cos(k)
        for occ in itertools.combinations(range(L), N):
            ev_f.append(sum(e[list(occ)]))
ev_f = np.sort(ev_f)
print("(a) XX chain L=%d: qubit ED vs JW free-fermion spectrum: max |diff| = %.2e; E0 = %.6f (both); dim %d = %d"
      % (L, np.max(np.abs(ev_q-ev_f)), ev_q[0], len(ev_q), len(ev_f)))
print("    two decoupled copies ('boson chain' + 'fermion chain'): E0 = %.6f = 2*E0, no cancellation" % (2*ev_q[0]))
print("    free CCR boson with omega_k=|e_k| paired with the fermion sea would give E0 = %.6f + %.6f = 0 (needs CCR)"
      % (0.5*np.sum(np.abs(-2*np.cos(2*np.pi*(np.arange(L)+0.5)/L))), -0.5*np.sum(np.abs(-2*np.cos(2*np.pi*(np.arange(L)+0.5)/L)))))
# (b) trace obstruction
for d in [2, 4, 16]:
    a = np.diag(np.sqrt(np.arange(1,d)), 1)
    c = a@a.T - a.T@a
    print("(b) truncated oscillator d=%2d: Tr[a,a^dag] = %.1f (CCR would need %d); zero-point of omega*a^dag a: 0, of omega(a^dag a+1/2): needs CCR" % (d, np.trace(c), d))

# (c) Witten index of hard-core (M1) configurations on tori: W = sum_{indep sets} (-1)^{|S|}
def ring_layer_states(nx, ny):
    # independent sets of an nx x ny torus layer (as bitmasks)
    N = nx*ny; nb = []
    for y in range(ny):
        for x in range(nx):
            m = 0
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                xx,yy = (x+dx)%nx,(y+dy)%ny
                j = xx+nx*yy
                if j != x+nx*y and ((nx>1 and dx) or (ny>1 and dy)): m |= 1<<j
            nb.append(m)
    out = []
    def rec(i,s,forb):
        if i==N: out.append(s); return
        rec(i+1,s,forb)
        if not (forb>>i)&1: rec(i+1, s|(1<<i), forb|nb[i])
    rec(0,0,0); return out
def witten_stack(nx, ny, Lz):
    st = ring_layer_states(nx, ny)
    sgn = np.array([(-1)**bin(s).count('1') for s in st], dtype=float)
    A = np.array([[1.0 if (a & b)==0 else 0.0 for b in st] for a in st])
    T = A*sgn[None,:]
    return int(round(np.trace(np.linalg.matrix_power(T, Lz)))), len(st), np.sort(np.abs(np.linalg.eigvals(T)))[::-1][:4]
print("(c) 2D square tori (ring of n, length Lz): W")
for n in [3,4,5,6,7,8]:
    row = []
    for Lz in range(3, 13):
        W,_,_ = witten_stack(n,1,Lz); row.append(W)
    print("   n=%d: Lz=3..12: %s" % (n, row))
print("(c) 3D cubic tori n x n x Lz: W (and |eigenvalues| of the signed transfer matrix)")
for n in [3,4]:
    row = []
    for Lz in range(2, 11):
        W, D, lam = witten_stack(n,n,Lz); row.append(W)
    print("   n=%d (layer states %d): Lz=2..10: %s ; top |lambda| = %s" % (n, D, row, np.array2string(lam, precision=4)))
