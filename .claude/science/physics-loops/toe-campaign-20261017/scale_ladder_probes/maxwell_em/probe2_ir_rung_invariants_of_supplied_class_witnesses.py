"""Scale-ladder probe 2 (conditional Maxwell dynamics lane).

For the existence witnesses of docs/U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md
and docs/U1_GAUSS_SUPPORT_FORCING_EXTENDED_PAYLOAD_CLASS_BOUNDED_NOTE_2026-09-05.md, compute
IR-rung invariants of each translation-invariant real-linear first-order law in Fourier space:
  * number of branches with Re/Im eigenvalue -> 0 as q -> 0 (gapless count), their speeds,
  * damping class (undamped / damped / diffusive), gapless loci away from q=0,
  * O(a^2 q^2) cubic anisotropy of the speed (irrelevant-operator suppression).
Question: which supplied clauses are detected (and which excluded) by matching to the IR target
'exactly one undamped massless transverse doublet with one isotropic light cone at q -> 0'?
Exploratory probe; no claim.
"""
import numpy as np
np.set_printoptions(precision=5, suppress=True)

def ops(q):
    D = np.exp(1j * np.asarray(q)) - 1.0                     # forward differences
    d0 = D.reshape(3, 1)                                     # vertex -> edge
    C = np.array([[0, -D[2], D[1]], [D[2], 0, -D[0]], [-D[1], D[0], 0]])  # edge -> face (dual)
    d2 = D.reshape(1, 3)                                     # face -> cube
    return d0, C, d2

def maxwell(q, eps=0.0):
    d0, C, d2 = ops(q)
    Ce = C @ (np.eye(3) + eps * C.conj().T @ C)              # improved curl L = C(1+eps C^T C)
    Z = np.zeros((3, 3))
    return np.block([[Z, -Ce.conj().T], [Ce, Z]])

def three_speed(q, a=-2, a2=2, qq=1, r=-1, b=-3, b2=3):
    d0, C, d2 = ops(q)
    M = np.zeros((8, 8), complex)
    # order: E(3) B(3) phi psi
    M[0:3, 3:6] = r * C.conj().T; M[0:3, 6:7] = a2 * d0
    M[3:6, 0:3] = qq * C;          M[3:6, 7:8] = b2 * d2.conj().T
    M[6:7, 0:3] = a * d0.conj().T; M[7:8, 3:6] = b * d2
    return M

def onsite_phase(q, th=3/7):
    G = maxwell(q)
    # complex payload z=(E,B) in C^6 written as real R^12: z' = (G + i th) z
    A = np.real(G); Bm = np.imag(G)
    # complex-linear map on Fourier amplitudes of two real fields x+iy is simply G + i th
    return G + 1j * th * np.eye(6)

def coin_KC(q, K=np.array([[1., 1.], [0., 1.]])):
    d0, C, d2 = ops(q)
    Z = np.zeros((6, 6), complex)
    KC = np.kron(K, C)
    return np.block([[Z, -KC.conj().T], [KC, Z]])

def damped(q, u=-0.3, v=-0.3):
    M = maxwell(q).astype(complex); M[0:3, 0:3] += u * np.eye(3); M[3:6, 3:6] += v * np.eye(3); return M

def overdamped(q, v=-0.3):
    return damped(q, u=0.0, v=v)

laws = {
    "Maxwell NN curl": maxwell,
    "improved curl eps=0.1": lambda q: maxwell(q, 0.1),
    "three-speed vertex+cube payload": three_speed,
    "onsite-phase coin theta=3/7": onsite_phase,
    "K(x)C coin K=[[1,1],[0,1]]": coin_KC,
    "damped u=v=-0.3": damped,
    "overdamped u=0,v=-0.3": overdamped,
}
dirs = {"100": np.array([1, 0, 0.]), "110": np.array([1, 1, 0.]) / np.sqrt(2), "111": np.ones(3) / np.sqrt(3)}

print("Eigenvalues lambda of dX/dt = M(q) X ; omega = Im lambda, gamma = -Re lambda\n")
for name, f in laws.items():
    print(f"== {name}")
    for s in [0.2, 0.05, 0.0125]:
        lam = np.linalg.eigvals(f(s * dirs["100"]))
        lam = lam[np.argsort(np.abs(lam))]
        nz = np.sum(np.abs(lam) < 1e-12)
        small = lam[(np.abs(lam) > 1e-12)]
        print(f"  |q|={s:<7} exact-zero modes={nz:2d}  lowest nonzero |lambda|/|q| = {np.round(np.abs(small[:6])/s,4)}"
              f"  min|lambda|={np.abs(small).min():.4g}")
    # anisotropy of slowest propagating speed at fixed |q|
    for s in [0.4, 0.2, 0.1]:
        sp = {}
        for dn, dv in dirs.items():
            lam = np.linalg.eigvals(f(s * dv)); lam = lam[np.abs(lam) > 1e-12]
            sp[dn] = np.sort(np.abs(lam.imag))[np.abs(np.sort(np.abs(lam.imag))) > 1e-9][:1] / s if np.any(np.abs(lam.imag) > 1e-9) else [np.nan]
        v = np.array([sp[k][0] for k in dirs])
        print(f"   |q|={s}: slowest |Im lambda|/|q| along 100,110,111 = {np.round(v,6)}  spread={np.nanmax(v)-np.nanmin(v):.3e}  spread/q^2={(np.nanmax(v)-np.nanmin(v))/s**2:.4f}")
    print()

# onsite-phase gapless locus
th = 3 / 7
qs = np.linspace(0.0, 1.0, 2001)
mins = [np.abs(np.linalg.eigvals(onsite_phase(x * dirs['100']))).min() for x in qs]
i = int(np.argmin(mins))
print(f"onsite-phase law: min |lambda| over q along 100 = {mins[i]:.2e} at |q|={qs[i]:.4f}; "
      f"|lambda| at q=0 = {mins[0]:.4f} (gap = theta = {th:.4f}); |k|=2sin(q/2)=theta at q={2*np.arcsin(th/2):.4f}")
