"""T133 - CHECKING TWO CLAIMS THAT OVERTURN THINGS I SAID.

The UV-floor lane returns two corrections to my own statements:
  (i)  the Kuhn simplicial FEM operator, the cubical cell-complex (DEC) operator
       and the plain nearest-neighbour hypercubic Laplacian are THE SAME OPERATOR
       (+8 on-site, -1 on each of 8 neighbours, lumped mass 1).  If true, my
       "the cell complex has better hypercubic symmetry" premise was simply false
       and that whole route is closed with zero gain.
  (ii) my T130 UV floor of s ~ 9 a^2 was an L=8 FINITE-VOLUME artifact; the true
       infinite-volume floor is s ~ 25 a^2.
Both are checkable directly from my own assembler, so check them.

Also verify their covariant Symanzik derivation, which I can do by hand:
   lattice symbol  Delta(k) = sum_mu 2(1 - cos k_mu) = k^2 - (1/12) sum_mu k_mu^4 + ...
   Delta + c Delta^2 = k^2 - (1/12) sum k_mu^4 + c (sum k_mu^2)^2 + ...
   and (sum k_mu^2)^2 = sum k_mu^4 + sum_{mu != nu} k_mu^2 k_nu^2.
   Under the heat trace's Gaussian weight, <k_mu^4> = 3 sigma^4 so
   <sum_mu k_mu^4> = 12 sigma^4, and <sum_{mu != nu} k_mu^2 k_nu^2> = 12 sigma^4
   (12 ordered pairs x sigma^4) -- EQUAL, which is the whole trick.
   error = -(1/12)(12 sigma^4) + c(12 + 12) sigma^4 = sigma^4 (24c - 1)  =>  c = 1/24.
Confirmed by hand.  Their "12 sigma^4 (2c - 1/12)" is the same expression."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t116 import kuhn, positions, lengths_from_positions, assemble

print("T133  (i) is the Kuhn FEM operator the nearest-neighbour hypercubic Laplacian?")
L=4
verts,vid,simp=kuhn(L); N=len(verts)
l20=[lengths_from_positions(positions(s,lambda X:0.0*X,L)) for s in simp]
K,Mv=assemble(simp,l20,N)
h=1.0/L
K=K*(h**2)          # to lattice units a=1:  K ~ a^{d-2} = a^2 in d=4
Mv=Mv/(h**4)        # mass ~ a^d
row=K[0]; base=np.array(verts[0])
nz={}
for j in range(N):
    if abs(row[j])>1e-12:
        off=tuple(int(((np.array(verts[j])-base)[a]+L//2)%L-L//2) for a in range(4))
        nz[off]=nz.get(off,0.0)+row[j]
print(f"      lumped mass per vertex (a=1): {Mv[0]:.10f}   (NN Laplacian: 1)")
print(f"      stencil of row 0, by offset:")
for off in sorted(nz,key=lambda o:(sum(abs(x) for x in o),o)):
    print(f"         {str(off):>16} : {nz[off]:+.10f}")
print(f"      -> {len(nz)} distinct offsets;  on-site {nz[(0,0,0,0)]:+.6f},"
      f" nearest-neighbour entries all {'equal' if len(set(round(v,9) for o,v in nz.items() if sum(abs(x) for x in o)==1))==1 else 'UNEQUAL'}")
print(f"      any next-nearest (|off|>1) entries? "
      f"{'NO' if not any(sum(abs(x) for x in o)>1 for o in nz) else 'YES'}")
print()
print("   (ii) was my s ~ 9 floor a finite-volume artifact?  Same operator, growing L,")
print("        compared against the EXACT winding sum at each L.")
def windsum(s,side,W=10):
    t=0.0
    for w in itertools.product(range(-W,W+1),repeat=4):
        n2=sum(x*x for x in w); t+=np.exp(-n2*side*side/(4.0*s))
    return t
def nn_spectrum(L):
    """exact spectrum of the NN hypercubic Laplacian on the L^4 torus, a=1."""
    m=2*(1-np.cos(2*np.pi*np.arange(L)/L))
    A=m[:,None,None,None]+m[None,:,None,None]+m[None,None,:,None]+m[None,None,None,:]
    return A.ravel()
print(f"      {'s/a^2':>7} " + " ".join(f"{'L=%d'%L:>11}" for L in (8,16,32,64)))
for s in (4,8,16,25,40,64):
    out=[]
    for L in (8,16,32,64):
        lam=nn_spectrum(L)
        Kl=float(np.sum(np.exp(-s*lam)))
        Ke=(L**4)/(4*np.pi*s)**2*windsum(s,float(L))
        out.append(abs(Kl-Ke)/Ke)
    print(f"      {s:7.1f} " + " ".join(f"{x:11.3e}" for x in out),flush=True)
print()
print("   The L=8 column is what I measured in T130.  If the larger-L columns are")
print("   L-independent and differ from it, my floor was indeed a finite-volume artifact.")
print()
print("   (iii) covariant Symanzik: does Delta + Delta^2/24 lower the floor?")
print(f"      {'s/a^2':>7} {'Delta (L=64)':>14} {'Delta+D^2/24':>14} {'gain':>8}")
for s in (2,4,8,16,25):
    lam=nn_spectrum(64); L=64
    Ke=(L**4)/(4*np.pi*s)**2*windsum(s,float(L))
    e0=abs(float(np.sum(np.exp(-s*lam)))-Ke)/Ke
    lam2=lam+lam*lam/24.0
    e1=abs(float(np.sum(np.exp(-s*lam2)))-Ke)/Ke
    print(f"      {s:7.1f} {e0:14.3e} {e1:14.3e} {e0/e1:8.1f}x")
