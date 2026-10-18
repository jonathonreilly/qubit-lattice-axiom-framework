"""Independent D2-D4: O-invariant sublattices of Z^3 up to index 32 (HNF), FCC 2*D3 vs O-equivariant placements."""
import itertools, numpy as np
def inlat(H, v):  # H upper-triangular rows a,b,c / 0,d,e / 0,0,f ; is v in row lattice?
    (a, b, c), (_, d, e), (_, _, f) = H
    x = list(v)
    if x[0] % a: return False
    k = x[0] // a; x = [x[0]-k*a, x[1]-k*b, x[2]-k*c]
    if x[1] % d: return False
    k = x[1] // d; x = [0, 0, x[2]-k*e]
    return x[2] % f == 0
gens = [np.array([[0,-1,0],[1,0,0],[0,0,1]]), np.array([[0,0,1],[1,0,0],[0,1,0]])]  # C4z, C3 generate O
tot = 0; inv = []
for n in range(1, 33):
    for a in range(1, n+1):
        if n % a: continue
        for d in range(1, n//a + 1):
            if (n//a) % d: continue
            f = n // (a*d)
            for b in range(d):
                for c in range(f):
                    for e in range(f):
                        tot += 1
                        H = ((a,b,c),(0,d,e),(0,0,f))
                        if all(inlat(H, R @ np.array(row)) for R in gens for row in H):
                            inv.append((n, H))
print("sublattices of index <= 32:", tot)
print("O-invariant:", [(n, H) for n, H in inv])
# 2*D3 (FCC scaled by 2): index 16; is it M Z^3 with M commuting with O? commutant of O on R^3:
Os = set()
frontier = [np.eye(3, dtype=int)]
while frontier:
    M = frontier.pop()
    key = tuple(M.flatten())
    if key in Os: continue
    Os.add(key); frontier += [g @ M for g in gens]
Os = [np.array(k).reshape(3,3) for k in Os]; print("|O| =", len(Os))
A = np.vstack([np.kron(R, np.eye(3)) - np.kron(np.eye(3), R.T) for R in Os])  # vec(RM - MR) row-major
print("dim commutant of O on R^3:", 9 - np.linalg.matrix_rank(A))
M = 2*np.array([[1,1,0],[1,0,1],[0,1,1]]).T  # columns = FCC basis vectors (x2)
print("det M =", round(abs(np.linalg.det(M))), "; M commutes with all of O:", all((R@M == M@R).all() for R in Os))
Mi = np.linalg.inv(M)
tw = [np.rint(Mi @ R @ M).astype(int) for R in Os]
print("M^-1 R M integral for all R (O acts on FCC labels by another integral rep):", all(np.allclose(Mi@R@M, t) for R, t in zip(Os, tw)),
      "; equals R for all R:", all((t == R).all() for t, R in zip(tw, Os)))
