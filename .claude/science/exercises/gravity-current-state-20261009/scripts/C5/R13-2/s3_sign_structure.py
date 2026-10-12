# R13-2 s3: where the Euclidean (Trotter/Villain) weights of the energetic N-type lose positivity.
#  q-basis (h diagonal): kinetic factor <q'|exp(-eps H_E)|q> = Fourier transform of exp(-eps H_E(E)) -> positive iff
#     exp(-eps H_E) is a positive-definite function (Bochner).  E-basis (E diagonal): same with the h-potential.
import numpy as np, itertools
from common import *
rng=np.random.default_rng(5)
print("(1) U(1) (integer E, compact h), quadratic N-type kinetic K = J[E:E-(trE)^2/2] + U_v |G E|^2, J=1:")
# real-space on an L^3 torus, canonical slots p=E (orthonormal comps), G from symbols via FFT -> build dense K for L=3
L=3; ks=[2*np.pi*np.array(n)/L for n in itertools.product(range(L),repeat=3)]
for Uv in (1.0,100.0,1e4):
    mins=[]
    for k in ks:
        q=2*np.sin(k/2); Gm=Vmap(q).T; K=KN(0.5)+Uv*Gm.T@Gm; mins.append(np.linalg.eigvalsh(K).min())
    print(f"   U_v={Uv:g}: min over torus momenta of eig K = {min(mins):.4f}  (negative => integer E with K(E)<0 exist;"
          f" K(nE)=n^2 K(E) -> H unbounded below, Z = Tr e^(-beta H) diverges)")
print("   uniform (k=0) trace configuration E = n*I: K = J n^2 (3 - 9/2) = -1.5 n^2 J: unbounded below for every U_v (G(nI)=0).")
print("(2) DeWitt family K_lam = E:E - lam (trE)^2 (+ any PSD penalty): on-site eigenvalues")
for lam in (0.5,0.4,1/3,0.25,0.0):
    print(f"   lam={lam:.4f}: eig = {np.round(np.linalg.eigvalsh(KN(lam)),4)}  -> PSD iff lam <= 1/3")
print("   scalar-gauge invariance of the kinetic term on G=0 (E -> E + (k^2 I - k k)beta) holds only at lam = 1/2:")
for lam in (0.5,1/3,0.0):
    vals=[]
    for t in range(50):
        k=rng.normal(size=3); q=k; Gm=Vmap(q).T
        # restrict to ker G
        u,s,vt=np.linalg.svd(Gm); kerG=vt[np.sum(s>1e-10):].T
        dvec=Svec(q)   # scalar-gauge direction (k^2 I - kk) in orthonormal basis
        Kr=KN(lam)
        vals.append(np.linalg.norm(kerG.T@Kr@dvec)/np.linalg.norm(dvec))
    print(f"   lam={lam:.4f}: max |P_kerG K_lam (scalar-gauge direction)| = {max(vals):.3e}")
print("(3) Z_N single-site clock version, q-basis kinetic weight: H_E(E) = J[sum_ab w_ab (1-cos 2pi E_ab/N) - lam*c*(1-cos 2pi trE/N)]")
print("    (single-clock cosines + trace cosine as in Gu-Wen's H_J; c chosen so the small-field form is E:E - lam(trE)^2)")
N=4; eps_t=0.3
grids=np.array(list(itertools.product(range(N),repeat=6)))
Ec=np.where(grids> N//2, grids-N, grids)  # centred integers
w=np.array([1,1,1,2,2,2.])   # canonical off-diagonal slots: E_ab appears twice in E:E
for lam in (0.5,1/3,0.25,0.0):
    phi=2*np.pi*Ec/N
    H=np.sum(w*(1-np.cos(phi)),axis=1)*(N/(2*np.pi))**2 - lam*(1-np.cos(2*np.pi*Ec[:,:3].sum(1)/N))*(N/(2*np.pi))**2*2
    f=np.exp(-eps_t*H).reshape((N,)*6); F=np.fft.fftn(f).real
    print(f"   N={N}, eps={eps_t}, lam={lam:.4f}: min eig of H_E/J (on Z_N^6) = {H.min():.3f}; min Fourier coeff of exp(-eps H_E) = {F.min():+.4e} (max {F.max():.3e}); negative coefficients: {int(np.sum(F< -1e-12))}")
print("   reading: ANY negative-sign trace cosine (lam>0 in this single-clock form) is an antiferro character -> negative q-basis weights,")
print("   even at lam<=1/3 where the small-field form is PSD.  PSD small-field form is necessary, not sufficient.")
print("   ferro rewrite for lam<=1/3: E:E - lam (trE)^2 = sum_{a<b}(E_aa-E_bb)^2/3 + 2 sum_offdiag E_ab^2 + (1/3-lam)(trE)^2, each square -> ferro cosine:")
for lam in (1/3,0.25,0.0):
    phi=2*np.pi*Ec/N; s2=(N/(2*np.pi))**2
    H=(sum((1-np.cos(2*np.pi*(Ec[:,a]-Ec[:,b])/N)) for a,b in [(0,1),(1,2),(0,2)])/3 + 2*np.sum(1-np.cos(phi[:,3:]),axis=1)
       + (1/3-lam)*(1-np.cos(2*np.pi*Ec[:,:3].sum(1)/N)))*s2*2
    f=np.exp(-eps_t*H).reshape((N,)*6); F=np.fft.fftn(f).real
    print(f"   lam={lam:.4f}: min Fourier coeff = {F.min():+.4e}; negative coefficients: {int(np.sum(F< -1e-9*F.max()))}")
print("(4) E-basis: the h-potential must be 'ferromagnetic' after a shift (Lemma S). N-type h:R(h) symbol eigenvalues / k^2 at random k:")
for t in range(3):
    k=rng.normal(size=3); q=2*np.sin(k/2); print("   ",np.round(np.linalg.eigvalsh(-Rmap(q))/(q@q),4))
print("   one negative eigenvalue (transverse trace h, the S-conjugate direction) at every k != 0: B_N is not PSD, so it cannot be the")
print("   Hessian of a ferromagnetic cosine sum at its minimum (Lemma S).")
