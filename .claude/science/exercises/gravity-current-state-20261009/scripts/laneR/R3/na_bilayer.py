# N-a: bilayer (height<=2) orders under interval-count actions
import numpy as np, math
rng = np.random.default_rng(1)

def interval_counts(Rm):
    # Rm: boolean strict-order matrix (i<j means Rm[i,j]); returns N0..N3 (intervals with k interior elements)
    A = Rm.astype(np.int64)
    inner = A @ A   # number of z with i<z<j
    k = inner[Rm]
    return [int((k == m).sum()) for m in range(4)]

ok = True
for trial in range(200):
    a = rng.integers(1, 8); b = rng.integers(1, 8); n = a + b
    Rm = np.zeros((n, n), bool)
    Rm[:a, a:] = rng.random((a, b)) < rng.random()
    N = interval_counts(Rm)
    if not (N[0] == Rm.sum() and N[1] == N[2] == N[3] == 0):
        ok = False
print("N-a(1) random bilayers: N0 = R and N1=N2=N3=0 in all 200 trials:", ok)

# closed form: labelled bilayer sum with layers (a, n-a): sum_R C(a(n-a),R) e^{i phi R} = (1+e^{i phi})^{a(n-a)}
def logabs_Z(n, phi):
    # log |sum_a C(n,a) (1+e^{i phi})^{a(n-a)}| ; dominant a=n/2; use log-sum-exp of magnitudes as an upper bound
    # and the a=n/2 term as the leading magnitude
    m = abs(1 + np.exp(1j * phi))
    return (n * n / 4) * math.log(m) if m > 0 else -np.inf

print("\nN-a(2) per-link phase window: |1+e^{i phi}| < 1  <=>  phi mod 2pi in (2pi/3, 4pi/3)")
for phi in [0.065, 0.5, 1.0, 2.0, 2.0944, 2.2, math.pi, 4.0, 4.1888, 4.3, 2*math.pi - 0.065]:
    m = abs(1 + np.exp(1j * phi))
    print(f"  phi_l={phi:7.4f}  |1+e^(i phi)|={m:.4f}  log|Z_bil|/(n^2/4)={math.log(m) if m>0 else -np.inf:+.4f}  suppressed={m<1}")

# brute-force check of the closed form at small n (a=3,b=3: all 512 bipartite graphs)
a = b = 3; phi = 2.5
tot = 0j
for mask in range(1 << (a * b)):
    R = bin(mask).count("1")
    tot += np.exp(1j * phi * R)
print(f"\n  brute force a=b=3, phi=2.5: |Z|={abs(tot):.6f}, closed form |1+e^(i phi)|^9={abs(1+np.exp(1j*phi))**9:.6f}")

# Euclidean weights e^{-(a n + b R)}: sum = e^{-a n}(1+e^{-b})^{n^2/4}; log-growth per n^2/4 = ln(1+e^{-b}) > 0
print("\nN-a(3) real weights e^{-bR}: growth exponent ln(1+e^{-b}) per n^2/4 (always > 0):")
for bb in [-5, -1, 0, 1, 5, 20]:
    print(f"  b={bb:4}: ln(1+e^-b) = {math.log1p(math.exp(-bb)):.3e}")
print("  (b>0 also lets the antichain (R=0, weight e^{-an}) beat manifold-like orders, whose link count grows ~ n^{3/2})")

# BD normalisation: phi_l = (4/sqrt6)(l/l_p)^2 eps^{3/2}, l_p^2 = 8 pi G (G-A convention)
c = 4 / math.sqrt(6)
print("\nN-a(4) local BD (eps=1): window lower edge l/l_p =", round(math.sqrt((2*math.pi/3)/c), 4),
      "; at l = sqrt(G): (l/l_p)^2 = 1/(8pi) -> phi_l =", round(c/(8*math.pi), 4))
