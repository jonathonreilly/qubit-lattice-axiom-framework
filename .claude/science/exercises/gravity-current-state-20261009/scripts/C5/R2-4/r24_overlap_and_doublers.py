"""R2-4 checks A1 and A3.

A1: naive NN W(B4) Dirac operator on Z^4: zeros of d(p) = (sin p_mu) at the 16 corners,
    local chirality index = sign det(dd/dp) = prod_mu cos p_mu; the indices sum to zero
    (Nielsen-Ninomiya, comparator).  Staggered = 4 tastes (16 / 4 spin components), vector-like.
A3: free overlap operator (Neuberger), M0 = 1, Wilson kernel r = 1, on Z^4 with L = 32:
    D_ov(p) = 1 + A(p)/sqrt(A^dag A),  A = D_W - M0 = (aW - M0) + i g.sinp
    sqrt(A^dag A) = omega(p) = sqrt((aW - M0)^2 + sum sin^2)   (scalar in the free case)
    so  D_ov = [1 + (aW - M0)/omega] + i g . (sin p / omega).
    Fourier transform to position space; print the scalar and vector kernels along an axis
    and along the body diagonal: nonzero at every distance (not ultralocal), exponential decay.
    GW check: (1 - a)^2 + |b|^2 = 1 pointwise (canonical R = 1/2) to machine precision.
"""
import itertools, numpy as np

print("A1: naive nearest-neighbour Dirac symbol d_mu = sin p_mu on the 16 corners")
tot = 0
for corner in itertools.product([0, np.pi], repeat=4):
    idx = int(np.sign(np.prod(np.cos(corner))))
    tot += idx
print("   number of zeros = 16, signed index sum =", tot,
      " (+1 count:", sum(1 for c in itertools.product([0, 1], repeat=4) if sum(c) % 2 == 0), ")")

L = 32
k = 2 * np.pi * np.arange(L) / L
P = np.meshgrid(k, k, k, k, indexing='ij')
M0 = 1.0
aW = sum(1 - np.cos(p) for p in P)
s = [np.sin(p) for p in P]
s2 = sum(x * x for x in s)
om = np.sqrt((aW - M0) ** 2 + s2)
a_ov = 1 + (aW - M0) / om
b_ov = [x / om for x in s]
gw = np.max(np.abs((1 - a_ov) ** 2 + sum(x * x for x in b_ov) - 1))
print(f"\nA3: free overlap, L={L}, M0={M0}: max |(1-a)^2+|b|^2-1| = {gw:.2e} (canonical GW)")
print("   zeros of D_ov: a=0,b=0 only at p=0 ->", int(np.sum((np.abs(a_ov) < 1e-12) & (s2 < 1e-12))), "point(s)")
print("   a_ov at doubler corners:",
      sorted(set(np.round([a_ov[tuple(int(c * L // 2) for c in cc)] for cc in itertools.product([0, 1], repeat=4) if sum(cc) > 0], 6))))
A = np.fft.ifftn(a_ov).real
B0 = np.fft.ifftn(1j * b_ov[0]).real   # i*b_0 kernel (real in x space up to i)
print("\n   distance x along axis e0:  |a(x)|   |b_0(x)|")
rows = []
for x in range(0, L // 2 + 1):
    rows.append((x, abs(A[x, 0, 0, 0]), abs(B0[x, 0, 0, 0])))
    if x <= 12 or x % 4 == 0:
        print(f"   {x:3d}  {abs(A[x,0,0,0]):.3e}  {abs(B0[x,0,0,0]):.3e}")
xs = np.array([r[0] for r in rows[3:12]])
ya = np.log(np.array([r[1] for r in rows[3:12]]))
yb = np.log(np.array([r[2] for r in rows[3:12]]))
print("   fitted decay rate (x=3..11): scalar %.3f, vector %.3f per lattice spacing" %
      (-np.polyfit(xs, ya, 1)[0], -np.polyfit(xs, yb, 1)[0]))
print("\n   body diagonal (x,x,x,x):  |a|")
for x in range(0, 9):
    print(f"   {x:3d}  {abs(A[x,x,x,x]):.3e}")
nz = np.sum(np.abs(A) > 1e-14)
print(f"\n   entries of a(x) above 1e-14 on the 32^4 torus: {nz} of {L**4}  (ultralocal would be <= 81)")
