"""R17-1 s4 (written before running).
 (1) Rotation covariance at N = 2. A proper cubic rotation sends E_ij -> R_ii'R_jj' E_i'j'. On a Z_2 clock the
     label map n -> -n mod 2 is the identity, so the natural action is a pure qubit permutation and on-site
     face labels carry the unsigned (permutation) representation. Compute its cubic characters on the face
     3-plet and decompose; compare with the signed tensor (T2). Then test the alternative 'shift'
     implementation (n -> 1-n on sign-flipped slots, i.e. half-odd spin reading): does it preserve the
     zero-syndrome mod-2 Gauss sector? (count of sign-flipped slots per Gauss row, mod 2, for C4_z and C3).
 (2) 3x3x2 h=0 cube-model check: exact formula including the L_z=2 coincidence (top/bottom faces of a cube
     share the same cube pair, so <X_top X_bot> = 1) vs the ED values of s3.
 (3) General-N CSS clock model with uniform labels on supp(m): delta_s = m_s - N*[n_s+m_s >= N];
     E[delta_s] = 0, Var = m_s (N - m_s) -> label-probe m1 = 2K sum |c_s|^2 m_s(N-m_s) (flat, k^0), checked by
     enumeration; clock probe C_I = (N/2pi) sin(2 pi n/N): m1(k=0) for the integer-invariant N=3 lift (G delta=0
     for the n=0 lift) is still nonzero (k^0) when labels are uniform.
"""
import numpy as np, itertools
TYPES = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
E3 = np.eye(3, dtype=int)
def rot_mats():
    Rs = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product([1,-1], repeat=3):
            R = np.zeros((3,3), int)
            for a in range(3): R[a, perm[a]] = sg[a]
            if round(np.linalg.det(R)) == 1: Rs.append(R)
    return Rs
Rs = rot_mats()
def cls(R):
    tr = int(np.trace(R))
    return {3: 'E', -1: 'C2', 1: 'C4', 0: 'C3'}[tr] if tr != -1 else 'C2'
# classify C2 (axis) vs C2' (face diagonal): both trace -1; distinguish by R^2 and axis
def cls2(R):
    tr = int(np.trace(R))
    if tr == 3: return 'E'
    if tr == 0: return 'C3'
    if tr == 1: return 'C4'
    w, v = np.linalg.eig(R); ax = np.real(v[:, np.argmin(abs(w - 1))]); ax = np.abs(ax)/np.abs(ax).max()
    return 'C2' if np.sum(ax > 0.5) == 1 else "C2'"
offs = [(0,1),(1,2),(0,2)]
chars_unsigned = {}; chars_signed = {}
for R in Rs:
    c = cls2(R); u = 0; s = 0
    for (i, j) in offs:
        ii = int(np.argmax(np.abs(R[:, i]))); jj = int(np.argmax(np.abs(R[:, j])))
        if tuple(sorted((ii, jj))) == (i, j):
            u += 1; s += int(R[ii, i]*R[jj, j])
    chars_unsigned.setdefault(c, set()).add(u); chars_signed.setdefault(c, set()).add(s)
print("(1) face 3-plet characters by class (unsigned = Z2 permutation action; signed = tensor):")
for c in ['E', 'C3', 'C2', 'C4', "C2'"]:
    print("   %-4s unsigned %s   signed %s" % (c, chars_unsigned[c], chars_signed[c]))
print("   O-group irreps (E,8C3,3C2,6C4,6C2'): A1 (1,1,1,1,1) E (2,-1,2,0,0) T2 (3,0,-1,-1,1) -> unsigned = A1+E, signed = T2")
# shift implementation: per Gauss row, count sign-flipped slots
def G_entries(x, t):
    i, j = TYPES[t]; x = np.array(x); out = []
    if i == j: out += [((tuple(x - E3[j]), j), 1), ((tuple(x), j), -1)]
    else: out += [((tuple(x), j), 1), ((tuple(x + E3[i]), j), -1), ((tuple(x), i), 1), ((tuple(x + E3[j]), i), -1)]
    return out
for name, R in [("C4_z", np.array([[0,-1,0],[1,0,0],[0,0,1]])), ("C3_111", np.array([[0,0,1],[1,0,0],[0,1,0]])),
                ("C2_z", np.array([[-1,0,0],[0,-1,0],[0,0,1]]))]:
    flipped_types = []
    for t, (i, j) in enumerate(TYPES):
        ii = int(np.argmax(np.abs(R[:, i]))); jj = int(np.argmax(np.abs(R[:, j])))
        if R[ii, i]*R[jj, j] < 0: flipped_types.append(t)
    # Gauss row j at x: slots and their types; parity of flipped slots in each row type
    par = {}
    for j in range(3):
        cnt = 0
        for t in range(6):
            for dx in itertools.product([-1,0,1], repeat=3):
                for g, v in G_entries(dx, t):
                    if g == ((0,0,0), j) and t in flipped_types: cnt += 1
        par[j] = cnt % 2
    print("(1) shift implementation of %s: sign-flipped slot types %s ; flipped-slot parity per Gauss row (x,y,z) = %s"
          % (name, [TYPES[t] for t in flipped_types], [par[j] for j in range(3)]))
# (2) 3x3x2 corrected h=0 formula
def tt_pols(kh):
    kh = kh/np.linalg.norm(kh); a = np.array([1.0, 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1.0, 0])
    u = np.cross(kh, a); u /= np.linalg.norm(u); v = np.cross(kh, u)
    return [(np.outer(u,u) - np.outer(v,v))/np.sqrt(2), (np.outer(u,v) + np.outer(v,u))/np.sqrt(2)]
Ls = (3,3,2); offs3 = [(0,1),(1,2),(0,2)]
ed = {((0.67,0,0),0):0.0, ((0.67,0,0),1):4.0, ((0.67,0.67,0),0):2.0, ((0.67,0.67,0),1):4.0, ((0,0,1),0):0.0,
      ((0,0,1),1):0.0, ((0.67,0,1),0):0.8521, ((0.67,0,1),1):1.2308}
print("(2) 3x3x2, h=0: exact formula with the Lz=2 top/bottom coincidence vs s3 ED")
for kk in [np.array([2*np.pi/3,0,0]), np.array([2*np.pi/3,2*np.pi/3,0]), np.array([0,0,np.pi]), np.array([2*np.pi/3,0,np.pi])]:
    for p, eps in enumerate(tt_pols(kk)):
        # per cube: faces xy at z and z+1 (positions differ by e_z) coincide in cube pair when Lz=2
        cxy = 2*eps[0,1]; cyz = 2*eps[1,2]; cxz = 2*eps[0,2]
        val = abs(cxy)**2*abs(1 + np.exp(1j*kk[2]))**2 + 2*abs(cyz)**2 + 2*abs(cxz)**2
        key = (tuple(np.round(kk/np.pi, 2)), p)
        print("   k/pi=%s p%d exact(Lz=2) = %.4f ; ED = %s" % (np.round(kk/np.pi, 2), p, val, ed.get(key)))
# (3) general-N uniform-label variance and clock probe
print("(3) uniform labels: E[delta], Var[delta] for each N, m")
for N in [2, 3, 4, 8]:
    for m in range(1, N):
        ds = [m - N*((n + m) >= N) for n in range(N)]
        print("   N=%d m=%d: E=%.3f Var=%.3f (m(N-m)=%d)" % (N, m, np.mean(ds), np.var(ds), m*(N-m)))
p3 = [((0,1,0),5,2),((0,1,1),2,1),((0,1,1),5,1),((1,1,0),0,1),((1,1,0),5,1),((1,1,1),0,1),((1,1,1),2,1),((1,1,1),5,2),((1,1,2),0,1),((2,1,1),2,1)]
N = 3
rng = np.random.default_rng(3)
eps = tt_pols(np.array([1.0, 0.3, 0.2]))[0]
cs = np.array([eps[TYPES[t][0], TYPES[t][1]] if TYPES[t][0] == TYPES[t][1] else 2*eps[TYPES[t][0], TYPES[t][1]] for x, t, v in p3])
ms = np.array([v for x, t, v in p3])
lab = []; clk = []
for n in itertools.product(range(N), repeat=len(p3)):
    n = np.array(n); n2 = (n + ms) % N
    lab.append(abs(np.sum(cs*(n2 - n)))**2)
    clk.append(abs(np.sum(cs*(N/(2*np.pi))*(np.sin(2*np.pi*n2/N) - np.sin(2*np.pi*n/N))))**2)
mins = min(lab)
print("   N=3 minimal pattern (w=10; one of its lifts is integer-invariant, s1), k=0, uniform labels:"
      " <|chat.delta|^2> label probe = %.4f (formula sum c^2 m(N-m) = %.4f) ; clock probe = %.4f ; min over lifts = %.2e"
      % (np.mean(lab), np.sum(cs**2*ms*(N-ms)), np.mean(clk), mins))
