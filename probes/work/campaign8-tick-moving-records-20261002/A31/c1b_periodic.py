"""A31 c1b: correction to c1 (c1 used an OPEN cube, where boundary sites spoil cancellations).
On a periodic 3x3 torus in the xy-plane (9 qubits; x-bonds and y-bonds), is the calm aligned state
|n>^9 stationary under each covariant pair term?
  Heisenberg  s.s on every bond
  compass     s^x s^x on x-bonds, s^y s^y on y-bonds
  DM          (s_i x s_j)_x on x-bonds (i -> j = i+e_x), (s_i x s_j)_y on y-bonds
Then: does the DM term keep the one-flip sector over |n> closed (a single analytic band), and does
it create a second flip next to an existing one?"""
import signal, numpy as np
signal.alarm(55)
I2 = np.eye(2); X = np.array([[0,1],[1,0]],complex); Y = np.array([[0,-1j],[1j,0]]); Z = np.diag([1.,-1.]).astype(complex)
L = 3; N = L*L
sites = [(x,y) for x in range(L) for y in range(L)]; idx = {s:i for i,s in enumerate(sites)}
def op1(O, i):
    out = np.array([[1.]], complex)
    for j in range(N): out = np.kron(out, O if j == i else I2)
    return out
S = [[op1(p, i) for p in (X,Y,Z)] for i in range(N)]
bonds = [(idx[(x,y)], idx[((x+1)%L, y)], 0) for (x,y) in sites] + [(idx[(x,y)], idx[(x,(y+1)%L)], 1) for (x,y) in sites]
Hh = sum(sum(S[i][c] @ S[j][c] for c in range(3)) for i,j,a in bonds)
Hk = sum(S[i][a] @ S[j][a] for i,j,a in bonds)
Hd = 0
for i,j,a in bonds:
    b, c = (a+1)%3, (a+2)%3
    Hd = Hd + S[i][b] @ S[j][c] - S[i][c] @ S[j][b]
def aligned(n):
    th, ph = np.arccos(np.clip(n[2],-1,1)), np.arctan2(n[1], n[0])
    v = np.array([np.cos(th/2), np.exp(1j*ph)*np.sin(th/2)]); out = np.array([1.], complex)
    for _ in range(N): out = np.kron(out, v)
    return out, v
def resid(H, psi): e = np.vdot(psi, H @ psi).real; return np.linalg.norm(H @ psi - e*psi)
rng = np.random.default_rng(5)
for name, n in [('z', [0,0,1]), ('x', [1,0,0]), ('random', rng.normal(size=3)), ('random2', rng.normal(size=3))]:
    n = np.array(n, float); n /= np.linalg.norm(n); psi, v = aligned(n)
    print(f"n={name:8s}: residual Heisenberg {resid(Hh,psi):.1e}  compass {resid(Hk,psi):.3f}  DM {resid(Hd,psi):.1e}")
# one-flip sector over |n> for n = random: build the flip states and test closure under DM and Heisenberg
n = rng.normal(size=3); n /= np.linalg.norm(n); psi, v = aligned(n)
vbar = np.array([-np.conj(v[1]), np.conj(v[0])])     # orthogonal single-site state
def state(flips):
    out = np.array([1.], complex)
    for j in range(N): out = np.kron(out, vbar if j in flips else v)
    return out
one = np.array([state({i}) for i in range(N)]).T       # 512 x 9
two = np.array([state({i,j}) for i in range(N) for j in range(i+1, N)]).T
for name, H in [('Heisenberg', Hh), ('DM', Hd)]:
    img = H @ one
    in1 = one @ (one.conj().T @ img); in2 = two @ (two.conj().T @ img)
    lv = np.linalg.norm(psi.conj() @ img)
    print(f"{name:10s} on one-flip states: weight leaving the one-flip sector {np.linalg.norm(img - in1):.2e} "
          f"(into two flips {np.linalg.norm(in2):.2e}; back to the calm state {lv:.1e})")
H1 = one.conj().T @ (Hh + 0.4*Hd) @ one                 # one-flip block for J=1, D=0.4
w = np.sort(np.linalg.eigvalsh((H1 + H1.conj().T)/2))
k = 2*np.pi*np.arange(L)/L
print("one-flip block of J s.s + 0.4 DM: 9 levels", np.round(w, 4).tolist(), "(single band, uniform Peierls phase, no flux)")
# (2) a record with content +n or -n at site 0 (compressed change H_R = Q H Q, Q = |r><r| on site 0):
#     is the calm state on the other 8 sites still stationary?
for name, n in [('z', [0,0,1]), ('random', rng.normal(size=3))]:
    n = np.array(n, float); n /= np.linalg.norm(n); _, v = aligned(n)
    vbar = np.array([-np.conj(v[1]), np.conj(v[0])])
    for cname, r in [('+n', v), ('-n', vbar)]:
        Q = op1(np.outer(r, r.conj()), 0)
        st = np.array([1.], complex)
        for j in range(N): st = np.kron(st, r if j == 0 else v)
        print(f"record content {cname}, n={name:6s}: residual of compressed Heisenberg {resid(Q@Hh@Q, st):.1e}; "
              f"compressed DM {resid(Q@Hd@Q, st):.2e}")
