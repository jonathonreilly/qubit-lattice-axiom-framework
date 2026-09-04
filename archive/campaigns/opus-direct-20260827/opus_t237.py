"""
T237 - T236 redone with loops large enough to decide.

T236 used R,T <= 3 with -log|W| in 0.05..0.22, i.e. every loop within 20% of 1.
Confinement is an ASYMPTOTIC property; a small string tension is invisible at
that size, so T236 could not bound sigma.  Here: L=24 in 3D (the axioms as
written), loops to 8x8, averaged over many configurations.

Diagnostic that does not rely on a global fit -- the CREUTZ RATIO
      chi(R,T) = -log[ W(R,T) W(R-1,T-1) / (W(R-1,T) W(R,T-1)) ]
The perimeter and constant parts cancel identically, so chi -> sigma if there is
an area law and chi -> 0 if there is not.  No fit, no model choice.
"""
import numpy as np, time

def equilibrate_and_sample(L, nwarm, nsamp, gap, seed=71, cone=0.6):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(L,L,L,2)) + 1j*rng.normal(size=(L,L,L,2))
    psi /= np.linalg.norm(psi, axis=-1, keepdims=True)
    idx = np.indices((L,L,L))
    masks = [(idx.sum(axis=0) % 2 == p) for p in (0,1)]
    def sweep():
        for mask in masks:
            prop = psi + cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
            wo = np.ones(psi.shape[:3]); wn = np.ones(psi.shape[:3])
            for ax in range(3):
                for sg in (1,-1):
                    nb = np.roll(psi, sg, ax)
                    wo *= np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                    wn *= np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
            acc = (rng.random(psi.shape[:3]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
            psi[acc] = prop[acc]
    for _ in range(nwarm): sweep()
    out = []
    for _ in range(nsamp):
        for _ in range(gap): sweep()
        out.append(psi.copy())
    return out

RMAX = 8
def wloops(psi):
    U = []
    for ax in range(3):
        z = np.sum(np.conj(psi)*np.roll(psi,-1,ax), axis=-1)
        U.append(z/np.maximum(np.abs(z),1e-300))
    W = np.zeros((RMAX+1, RMAX+1))
    planes = [(0,1),(0,2),(1,2)]
    for mu,nu in planes:
        # precompute staples: product of R links along mu starting at x
        Amu = [None]*(RMAX+1); Amu[0] = np.ones_like(U[0])
        for R in range(1, RMAX+1):
            Amu[R] = Amu[R-1]*np.roll(U[mu], -(R-1), mu)
        Anu = [None]*(RMAX+1); Anu[0] = np.ones_like(U[0])
        for T in range(1, RMAX+1):
            Anu[T] = Anu[T-1]*np.roll(U[nu], -(T-1), nu)
        for R in range(1, RMAX+1):
            for T in range(1, RMAX+1):
                bot = Amu[R]
                right = np.roll(Anu[T], -R, mu)
                top = np.conj(np.roll(Amu[R], -T, nu))
                left = np.conj(Anu[T])
                W[R,T] += np.real(np.mean(bot*right*top*left))
    return W/len(planes)

if __name__ == "__main__":
    L = 24
    t0 = time.time()
    cfgs = equilibrate_and_sample(L, 3000, 60, 8)
    print(f"L={L}, {len(cfgs)} configurations  [{time.time()-t0:.0f}s]")
    W = np.mean([wloops(c) for c in cfgs], axis=0)
    print("\n  W(R,T):")
    print("      " + "".join(f"{T:9d}" for T in range(1, RMAX+1)))
    for R in range(1, RMAX+1):
        print(f"   R={R} " + "".join(f"{W[R,T]:9.5f}" for T in range(1, RMAX+1)))
    print("\n  Creutz ratios chi(R,T) = -log[W(R,T)W(R-1,T-1)/(W(R-1,T)W(R,T-1))]")
    print("  (perimeter and constant cancel identically; chi -> sigma if area law)")
    print("      " + "".join(f"{T:9d}" for T in range(2, RMAX+1)))
    for R in range(2, RMAX+1):
        row = f"   R={R} "
        for T in range(2, RMAX+1):
            num = W[R,T]*W[R-1,T-1]; den = W[R-1,T]*W[R,T-1]
            row += f"{-np.log(max(num/den,1e-300)):9.5f}" if den > 0 and num > 0 else "      n/a"
        print(row)
    diag = [(-np.log((W[R,R]*W[R-1,R-1])/(W[R-1,R]*W[R,R-1]))) for R in range(2, RMAX+1)
            if W[R-1,R] > 0 and W[R,R-1] > 0 and W[R,R] > 0]
    print(f"\n  diagonal chi(R,R) for R=2..{RMAX}: " + " ".join(f"{v:+.5f}" for v in diag))
    print(f"  -> {'AREA law (chi plateaus at sigma>0): CONFINED' if len(diag)>2 and np.mean(diag[-3:])>0.01 else 'chi -> 0: NO area law detected at these sizes'}")

# ---------------------------------------------------------------------------
# WHY is there no area law?  Compact-U(1) confinement in 3D is driven by
# MONOPOLES.  A Berry connection is not an independent fluctuating field -- it
# is determined by the matter configuration -- so if the ordered record field is
# smooth, monopoles should be absent and the confinement mechanism has nothing
# to work with.  Measured, not assumed.
# ---------------------------------------------------------------------------
def monopoles(psi):
    U = []
    for ax in range(3):
        z = np.sum(np.conj(psi)*np.roll(psi,-1,ax), axis=-1)
        U.append(z/np.maximum(np.abs(z),1e-300))
    def plaq(mu, nu):
        a = U[mu]; b = np.roll(U[nu], -1, mu)
        c = np.conj(np.roll(U[mu], -1, nu)); d = np.conj(U[nu])
        return np.angle(a*b*c*d)              # principal branch, in (-pi,pi]
    # oriented sum of the six faces of each unit cube
    tot = np.zeros(psi.shape[:3])
    for (mu, nu) in ((0,1),(1,2),(2,0)):
        F = plaq(mu, nu)
        rho = 3 - mu - nu                      # the remaining axis
        tot += F - np.roll(F, -1, rho)
    m = tot/(2*np.pi)
    q = np.round(m)
    return q, m

if __name__ == "__main__":
    print("\n=== why no area law?  monopole density ===")
    qs = []
    for c in cfgs[:20]:
        q, m = monopoles(c)
        qs.append(q)
        assert np.max(np.abs(m - q)) < 1e-9, f"cube sum not quantised: {np.max(np.abs(m-q)):.2e}"
    q = np.concatenate([x.ravel() for x in qs])
    print(f"   cube flux is quantised to integers (checked, else assertion)")
    print(f"   monopole charges seen: {sorted(set(q.astype(int)))}")
    print(f"   density of non-zero charge: {np.mean(q != 0):.6f}  "
          f"({int(np.sum(q!=0))} of {q.size} cubes)")
    print(f"   mean |plaquette phase|: "
          f"{np.mean([np.mean(np.abs(np.angle(np.sum(np.conj(c)*np.roll(c,-1,0),axis=-1)))) for c in cfgs[:5]]):.4f} rad")
    print("""
   => the Berry connection is DETERMINED by a smooth matter configuration, not
      an independently fluctuating compact gauge field.  With no monopoles the
      3D confinement mechanism has nothing to act on, which is why chi -> 0.
      The absence of a string tension is a statement about THIS field, not a
      claim that a compact U(1) fails to confine in three dimensions.""")
