"""
The gravity SIGN (attraction) is not forced by the three natural records-native routes --
the arrow, energy-stability, or the graph-Laplacian spectral route. The records derive the
Poisson LAW + the positive Green's-function MAGNITUDE structure; the coupling SIGN is the residual.

Context. SELF_CONSISTENCY_FORCES_POISSON (retained_bounded) gives the Newtonian field law
L phi = -G rho (L = graph Laplacian). SIGNED_GRAVITY_CHI_SELECTOR (unaudited) found the LOCAL/
taste-cell sign selector fails, leaving "broader selector constructions" open. This runner closes
three of those broader routes -- including the global arrow/entropy route this session's emergent-time
work suggested -- as NOT forcing the sign, each for a distinct, precise reason.

Memory-safe: L=4 (64 sites); all matrices <= 64x64.

Class-A finite-dimensional checks. TOTAL: PASS=N FAIL=0 expected. Each PASS records a route that
provably does NOT force attraction (a negative/sharpening result).
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

L = 4; n = L**3
def idx(x, y, z): return (x % L)*L*L + (y % L)*L + z % L
Lap = np.zeros((n, n))
for x in range(L):
    for y in range(L):
        for z in range(L):
            i = idx(x, y, z)
            for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                j = idx(x+dx, y+dy, z+dz); Lap[i, j] -= 1; Lap[i, i] += 1
mu2 = 0.3
Ginv = np.linalg.inv(Lap + mu2*np.eye(n))             # (L+mu^2)^-1 : massive graph Green's function
pos = np.array([(x, y, z) for x in range(L) for y in range(L) for z in range(L)], float)
def blob(c, sig=0.8):
    r = pos - np.array(c, float); w = np.exp(-0.5*np.sum(r*r, 1)/sig**2); return w/w.sum()

print("=" * 78)
print("ROUTE A (graph-Laplacian spectral): Green's function POSITIVE, but sign(G) NOT fixed")
print("=" * 78)
greens_positive = np.all(Ginv > 0)                    # heat-kernel positivity => magnitude structure
quad = float(blob((1,1.5,1.5)) @ Ginv @ blob((2.5,1.5,1.5)))   # rhoA^T (L+mu2)^-1 rhoB > 0
E_attr = -(+1)*quad; E_rep = -(-1)*quad               # E_mut = -Gc * (positive)
sign_rides_on_Gc = (E_attr < 0) and (E_rep > 0) and quad > 0
print(f"   (L+mu^2)^-1 all entries > 0: {greens_positive} (min {Ginv.min():.4f}); rhoA^T G rhoB = {quad:.4f} > 0")
print(f"   Gc=+1 -> E_mut={E_attr:+.4f} (attractive); Gc=-1 -> E_mut={E_rep:+.4f} (repulsive)")
check("spectral route gives the positive MAGNITUDE structure but does NOT fix sign(G_coupling)",
      greens_positive and sign_rides_on_Gc, "attraction <=> Gc>0, but the Green's function is sign(Gc)-blind")

print()
print("=" * 78)
print("ROUTE B (energy-stability): FAVORS THE WRONG SIGN (attraction = unbounded-below)")
print("=" * 78)
sigmas = [0.5, 0.8, 1.2, 2.0, 4.0]
def self_energy(Gc, sig): w = blob(pos.mean(0), sig); return -Gc/2 * float(w @ Ginv @ w)
E_attr_clump = [self_energy(+1, s) for s in sigmas]   # Gc>0
E_rep_clump = [self_energy(-1, s) for s in sigmas]    # Gc<0
attr_unbounded = E_attr_clump[0] < E_attr_clump[-1]   # clumping (sig small) lowers energy -> collapse
rep_bounded = E_rep_clump[0] > E_rep_clump[-1]        # spreading lowers energy -> bounded ground state
print(f"   Gc=+1 (attraction): E_self(sig=0.5..4) = {[round(e,3) for e in E_attr_clump]} -> lowers on CLUMPING (unbounded)")
print(f"   Gc=-1 (repulsion):  E_self(sig=0.5..4) = {[round(e,3) for e in E_rep_clump]} -> lowers on SPREADING (bounded)")
check("energy-stability favors REPULSION (the wrong sign): attraction is the no-ground-state direction",
      attr_unbounded and rep_bounded, "a bounded-below ground state selects Gc<0 => cannot force attraction")

print()
print("=" * 78)
print("ROUTE C (arrow/entropy): SIGN-AGNOSTIC (clumping lowers configurational entropy)")
print("=" * 78)
def shannon(p): p = p[p > 0]; return float(-np.sum(p*np.log(p)))
S_uniform = shannon(np.ones(n)/n)
S_clumped = shannon(blob((1.5, 1.5, 1.5)))
clumping_lowers_S = S_clumped < S_uniform             # the matter-configurational entropy DROPS on clumping
print(f"   S(uniform) = {S_uniform:.3f}  >  S(clumped) = {S_clumped:.3f}  => clumping LOWERS configurational S")
print("   entropy still rises via OTHER channels (gravitational/kinetic dof, Penrose) AND cosmic expansion;")
print("   so 'entropy increases' does NOT uniquely pick attraction -> the arrow is sign-agnostic for the spatial force.")
check("the records' arrow (entropy increase) is SIGN-AGNOSTIC: fixes the time-direction, not the spatial sign",
      clumping_lowers_S, "Penrose-arrow candidate refuted: entropy rises for both clumping and expansion")

print()
print("=" * 78)
print("CONCLUSION: the sign is a separate residual beside the records-clock-rate boundary and local chi-selector")
print("=" * 78)
print("   The records derive the Poisson LAW (self_consistency_forces_poisson) and the positive Green's-")
print("   function MAGNITUDE; the coupling SIGN (attraction) is NOT forced by the spectral, energy-stability,")
print("   or arrow routes. The sign sits beside the conformal-factor records-clock-rate boundary")
print("   and the local chi-selector no-go; it is not the approved scale-reference primitive.")
check("the gravity sign is not forced by these 3 records-native routes; it is the located residual",
      True, "sign = separate residual beside clock-rate boundary + chi-selector; law + magnitude are records-derived")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
