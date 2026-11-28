# Guide only. Importance sampling of the one-plane twisted integral J_eps(s) (sign -1 on the 12 commutator).
# Rotations fix u_1 along e_z and the azimuth of u_2. Coordinates: x1, x2 (scalar parts), y (cosine u1,u2), u3, u4.
# Gaussian prediction at the twisted minimum: s^(9/2) J_eps(s) -> 1/(2^(9/2) pi^(3/2)) = 0.0079368...
import math, random, sys
rng = random.Random(7)
def cr2(A, B):
    cx = A[1]*B[2]-A[2]*B[1]; cy = A[2]*B[0]-A[0]*B[2]; cz = A[0]*B[1]-A[1]*B[0]
    return cx*cx + cy*cy + cz*cz
def Jtw(s, N):
    sd = [1/math.sqrt(4*s)]*3 + [1/math.sqrt(4*s), 1/math.sqrt(8*s), 1/math.sqrt(4*s)]*2
    lognorm = sum(-math.log(math.sqrt(2*math.pi)*d) for d in sd)
    acc = 0.0; acc2 = 0.0; G = rng.gauss
    for _ in range(N):
        z = [G(0.0, d) for d in sd]
        x1, x2, y = z[0], z[1], z[2]; u3 = z[3:6]; u4 = z[6:9]
        n3 = u3[0]**2+u3[1]**2+u3[2]**2; n4 = u4[0]**2+u4[1]**2+u4[2]**2
        if abs(x1) >= 1 or abs(x2) >= 1 or abs(y) >= 1 or n3 >= 1 or n4 >= 1:
            continue
        a1 = math.sqrt(1-x1*x1); a2 = math.sqrt(1-x2*x2)
        u1 = (0.0, 0.0, a1); u2 = (a2*math.sqrt(1-y*y), 0.0, a2*y)
        E = 2*(1 - cr2(u1, u2)) + 2*(cr2(u1, u3) + cr2(u2, u3) + cr2(u1, u4) + cr2(u2, u4)) + 2*cr2(u3, u4)
        logdens = math.log((2/math.pi)*a1) + math.log((2/math.pi)*a2) + math.log(0.5) \
                  - 2*math.log(math.pi**2) - 0.5*math.log1p(-n3) - 0.5*math.log1p(-n4)
        logq = lognorm - 0.5*sum((zi/d)**2 for zi, d in zip(z, sd))
        val = math.exp(logdens - s*E - logq); acc += val; acc2 += val*val
    m = acc/N
    return m, math.sqrt(max(acc2/N - m*m, 0.0)/N)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
pred = 1/(2**4.5*math.pi**1.5)
print(f"prediction for s^(9/2) J_eps: {pred:.6f}")
for s in [1e2, 1e3, 1e4, 1e5]:
    m, se = Jtw(s, N)
    print(f"s={s:.0e}  s^(9/2) J_eps = {m*s**4.5:.6f} (se {se*s**4.5:.1e})", flush=True)
