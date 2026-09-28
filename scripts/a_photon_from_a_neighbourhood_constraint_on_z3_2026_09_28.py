#!/usr/bin/env python3
"""A photon from a neighbourhood constraint on Z^3: qubits that obey an ice rule carry a massless light-like pattern.

Question (the owner, 2026-09-28): can the qubits and a neighbourhood rule for
records themselves be the force carriers? Test: an in-framework qubit model
on Z^3 whose only rule is a nearest-neighbour constraint plus nearest-neighbour
moves that keep it; does a massless light-like pattern appear? Reference only
(re-derived here, not imported): quantum spin ice and U(1) quantum link
models (Hermele, Fisher and Balents 2004; Banerjee et al. 2008; Shannon et al.
2012); the single-mode (Feynman-Bijl) bound.

Embedding in Z^3 (a torus of size 2L): a site is typed by how many of its
coordinates are odd.
  vertex (V): none odd;  link (E): one odd (the odd axis is the link's
  direction);  plaquette centre (P): two odd;  cube centre (C): three odd.
The E sites carry the qubits: up/down = the field E = +1/-1 along the link's
positive axis. The V, P and C sites are spectators (no record content here).
  Constraint (ice rule, a Gauss law): at every V site, its six nearest
  neighbours (all E sites) satisfy div E = sum_a (E(v+e_a) - E(v-e_a)) = 0.
  Moves (ring exchange): at every P site, its four in-plane nearest
  neighbours (E sites), when they circulate, flip together (all four
  reversed), which keeps every constraint. Hamiltonian in the constrained
  space: H = -K sum_p F_p + V sum_p F_p^2 (F_p flips plaquette p if
  flippable; V = K is the Rokhsar-Kivelson (RK) point, whose ground state is
  the equal superposition of all constrained configurations of a sector).

PRE-REGISTERED (written before running):
  P1 embedding: every constraint and every move involves only nearest
     neighbours of one V or P site of Z^3.
  P2 the moves preserve the constraint exactly.
  P3 the constrained ensemble (the RK ground state's weights) has transverse
     field fluctuations S_T(q) that stay finite as q -> 0 (S_T at the smallest
     q >= 0.1 of its value at q = pi), with the longitudinal part zero.
     [Correction after the run, from the independent check: this criterion
     was mis-specified. Flat S_T (= 3/2 by a sum rule) is the RK point's
     property, where the photon's speed is zero; in a linear-photon phase
     S_T falls like |q|. P3 is kept as a check that the RK ensemble is a
     Coulomb (divergence-free, unfrozen) state, not as evidence of a linear
     photon.]
  P4 the single-mode bound at the RK point, E_min(q) <= omega_SMA(q) =
     f(q)/S_T(q), goes to zero as q -> 0 with a fitted exponent in [1.7, 2.3]
     (gapless; quadratic at the RK point).
  P5 on the smallest cluster (2x2x2 coarse cells, 24 qubits) exact
     diagonalisation reproduces the single-mode expression and the lowest
     level reached from A|psi0> lies at or below it.
  P6 harmonic (weak-coupling) regime of the same lattice gauge theory: exactly
     two massless polarisations with linear dispersion; random local
     gauge-invariant perturbations keep them massless; a gauge-breaking A^2
     term gaps them. [The harmonic rotor model H = (U/2) E.Z(k).E +
     (1/2) (curl A).W(k).(curl A) with continuous A, E is a separate
     weak-coupling model, not derived from the spin-1/2 Hamiltonian (for
     E = +-1, sum E^2 is constant). Parameters: U = K = 1; W(k) = I + 0.3
     sum_i B_i B_i^T cos^2 k_{i mod 3}, Z(k) = I + 0.3 sum_i C_i C_i^T
     cos^2 k_{(i+1) mod 3}, B_i, C_i Gaussian random 3x3 (seed 11, four
     each); gauge-breaking term m^2 A.A with m^2 = 0.05; momenta along a
     fixed generic direction.]
  FAIL if omega_SMA(q -> 0) stays finite (the S_T clause of the original
  FAIL line was mis-specified; see P3).
  G (added after the independent check): beyond the RK point on a 2x2x3
     cluster (34,080 states), the bound holds and S_T at the smallest q falls
     as V decreases (the mode stiffens); linear vs quadratic dispersion is not
     decidable at these momenta.
  Covariance (named, not tested): the embedding types sites by coordinate
  parity, so the model is covariant only under translations by two sites and
  rotations about vertex or cube sites, while the axioms ask for full Z^3
  covariance and a qubit at every site.

Checks A-F test P1-P6. Prints one line per check, the N5 resolution lines and
TOTAL: PASS=N FAIL=M.
"""
import itertools
import time
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 900

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


# ---------------------------------------------------------------- A embedding in Z^3
def z3_embedding(L):
    n = 2 * L; ok = True
    kinds = {}
    for s in itertools.product(range(n), repeat=3):
        kinds[s] = sum(c % 2 for c in s)
    E = lambda s: kinds[tuple(c % n for c in s)] == 1
    nv = npl = 0
    for s, k in kinds.items():
        if k == 0:   # vertex: all six nearest neighbours are link sites
            nv += 1
            ok &= all(E(tuple(np.add(s, d))) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
        if k == 2:   # plaquette centre: the four in-plane nearest neighbours are link sites
            npl += 1
            even_axis = [a for a in range(3) if s[a] % 2 == 0][0]
            inplane = [a for a in range(3) if a != even_axis]
            ok &= all(E(tuple(np.add(s, sg * np.eye(3, dtype=int)[a]))) for a in inplane for sg in (1, -1))
            # the out-of-plane neighbours are cube centres or vertices? they are not link sites
            ok &= not any(E(tuple(np.add(s, sg * np.eye(3, dtype=int)[even_axis]))) for sg in (1, -1))
    nE = sum(1 for k in kinds.values() if k == 1)
    return ok, nv, npl, nE


ok, nv, npl, nE = z3_embedding(3)
check("A: embedding: the ice rule involves exactly the six nearest neighbours of each all-even site, and each move exactly the four in-plane nearest neighbours of a two-odd site",
      ok and nE == 3 * nv and npl == 3 * nv,
      f"Z^3 torus 6^3: {nv} vertex sites, {nE} link sites (qubits), {npl} plaquette sites; all neighbourhoods as required")


# ---------------------------------------------------------------- coarse-lattice tools
def initial_ice(L):
    r = np.indices((L, L, L))
    return [((-1) ** (r[(a + 1) % 3] + r[(a + 2) % 3])).astype(int) for a in range(3)]


def divergence(E):
    return sum(E[a] - np.roll(E[a], 1, axis=a) for a in range(3))


def plaquette_state(E, a, b, r):   # plaquette in the (a, b) plane with lower corner r
    L = E[0].shape[0]; ea = np.eye(3, dtype=int)[a]; eb = np.eye(3, dtype=int)[b]
    t = lambda v: tuple(np.mod(v, L))
    return (E[a][t(r)], E[b][t(np.add(r, ea))], E[a][t(np.add(r, eb))], E[b][t(r)])


def flip(E, a, b, r):
    L = E[0].shape[0]; ea = np.eye(3, dtype=int)[a]; eb = np.eye(3, dtype=int)[b]
    t = lambda v: tuple(np.mod(v, L))
    for arr, pos in ((E[a], t(r)), (E[b], t(np.add(r, ea))), (E[a], t(np.add(r, eb))), (E[b], t(r))):
        arr[pos] *= -1


def flippable(st):
    return st in ((1, 1, -1, -1), (-1, -1, 1, 1))


def loop_update(E, rng):
    """Long-loop update (uniform over divergence-free configurations): walk along outgoing arrows until a vertex repeats; reverse the loop."""
    L = E[0].shape[0]
    v = tuple(rng.integers(L, size=3)); path = [v]; seen = {v: 0}; links = []
    while True:
        outs = []
        for a in range(3):
            if E[a][v] == 1:                       # link v -> v + e_a points out of v
                outs.append((a, v, tuple(np.mod(np.add(v, np.eye(3, dtype=int)[a]), L))))
            w = tuple(np.mod(np.subtract(v, np.eye(3, dtype=int)[a]), L))
            if E[a][w] == -1:                      # link w -> v stored at w, pointing from v to w
                outs.append((a, w, w))
        a, pos, nxt = outs[rng.integers(len(outs))]
        links.append((a, pos)); v = nxt
        if v in seen:
            for (aa, pp) in links[seen[v]:]:
                E[aa][pp] *= -1
            return
        seen[v] = len(links); path.append(v)


# ---------------------------------------------------------------- B moves preserve the constraint
rng = np.random.default_rng(7)
Lb = 4; Eb = initial_ice(Lb)
for _ in range(2000):
    loop_update(Eb, rng)
viol = 0; nflip = 0
for _ in range(5000):
    a, b = rng.choice(3, 2, replace=False); r = rng.integers(Lb, size=3)
    if flippable(plaquette_state(Eb, a, b, r)):
        flip(Eb, a, b, r); nflip += 1
    viol = max(viol, int(np.abs(divergence(Eb)).max()))
check("B: the ring-exchange moves keep the ice rule exactly (and the loop updates sample only rule-respecting configurations)",
      viol == 0 and nflip > 100, f"{nflip} flips on a 4^3 coarse torus; largest divergence afterwards {viol}")


# ---------------------------------------------------------------- C/D constrained ensemble, S_T(q), single-mode bound
def ensemble(L, nsamp, loops_between, seed):
    rng = np.random.default_rng(seed); E = initial_ice(L)
    for _ in range(L ** 3):
        loop_update(E, rng)
    qs = [2 * np.pi * m / L for m in range(1, L // 2 + 1)]
    ST = np.zeros(len(qs)); SL = np.zeros(len(qs)); rho = 0.0; ST2 = np.zeros(len(qs))
    pos = np.arange(L)
    for s in range(nsamp):
        for _ in range(loops_between):
            loop_update(E, rng)
        STs = np.zeros(len(qs))
        for d in range(3):                       # q along axis d
            other = [a for a in range(3) if a != d]
            for pol in other:                    # transverse polarisations
                Ed = E[pol].sum(axis=tuple(a for a in range(3) if a != d))
                for i, q in enumerate(qs):
                    STs[i] += abs(np.sum(Ed * np.exp(1j * q * pos))) ** 2 / L ** 3 / 6
            El = E[d].sum(axis=tuple(a for a in range(3) if a != d))
            for i, q in enumerate(qs):
                SL[i] += abs(np.sum(El * np.exp(1j * q * (pos + 0.5)))) ** 2 / L ** 3 / 3
        ST += STs; ST2 += STs ** 2
        fl_all = []
        for (a, b) in ((0, 1), (1, 2), (2, 0)):
            st0 = E[a]; st1 = np.roll(E[b], -1, axis=a); st2 = np.roll(E[a], -1, axis=b); st3 = E[b]
            fl = ((st0 == 1) & (st1 == 1) & (st2 == -1) & (st3 == -1)) | ((st0 == -1) & (st1 == -1) & (st2 == 1) & (st3 == 1))
            fl_all.append(fl.mean())
        rho += np.mean(fl_all)
    err = np.sqrt(np.maximum(ST2 / nsamp - (ST / nsamp) ** 2, 0) / nsamp)   # samples separated by L^3/8 loop updates; autocorrelation not estimated
    return np.array(qs), ST / nsamp, SL / nsamp, rho / nsamp, err

ens = {L: ensemble(L, 400, L ** 3 // 8, seed=L) for L in (8, 12)}
qs8, ST8, SL8, rho8, er8 = ens[8]; qs12, ST12, SL12, rho12, er12 = ens[12]
check("C: the RK ensemble is divergence-free with flat, unfrozen transverse two-point correlations (~3/2 by a sum rule; zero stiffness at this point), consistent with a Coulomb phase (P3, reframed)",
      SL8.max() < 1e-20 and SL12.max() < 1e-20 and ST8[0] >= 0.1 * ST8[-1] and ST12[0] >= 0.1 * ST12[-1],
      f"L=8: S_T at q = {np.round(qs8, 3).tolist()}: {np.round(ST8, 3).tolist()} (+- {np.round(er8, 3).tolist()}), max S_L {SL8.max():.1e}; "
      f"L=12: S_T at q = {np.round(qs12, 3).tolist()}: {np.round(ST12, 3).tolist()} (+- {np.round(er12, 3).tolist()}); flippable fraction {rho8:.3f}, {rho12:.3f}")

K = 1.0
qall = np.concatenate([qs8, qs12]); Sall = np.concatenate([ST8, ST12]); rall = np.concatenate([[rho8] * len(qs8), [rho12] * len(qs12)])
omega = 8 * K * rall * np.sin(qall / 2) ** 2 / Sall       # f(q)/S_T(q), f per cell = (K/2) rho * 16 sin^2(q/2)
small = qall < 1.6
slope = np.polyfit(np.log(qall[small]), np.log(omega[small]), 1)[0]
check("D: at each finite size the single-mode bound at the RK point falls toward zero at long wavelength, quadratically (quadratic here, not yet light-like; the infinite-size limit needs S_T to stay finite) (P4)",
      1.7 <= slope <= 2.3 and omega[np.argmin(qall)] < 0.2 * omega[np.argmax(qall)],
      f"omega_SMA(q)/K: " + ", ".join(f"q={q:.3f}: {w:.4f}" for q, w in sorted(zip(qall, omega))) + f"; fitted exponent {slope:.2f}")


# ---------------------------------------------------------------- E exact diagonalisation on 2x2x2 (momentum-projected)
def enumerate_ice_fast(L, chunk=1 << 20):
    nl = 3 * L ** 3; goods = []
    for start in range(0, 2 ** nl, chunk):
        b = np.arange(start, min(start + chunk, 2 ** nl), dtype=np.int64)
        bitsarr = (((b[:, None] >> np.arange(nl)) & 1) * 2 - 1).astype(np.int8)
        Es = [bitsarr[:, a * L ** 3:(a + 1) * L ** 3].reshape(-1, L, L, L) for a in range(3)]
        div = sum(Es[a].astype(np.int16) - np.roll(Es[a], 1, axis=a + 1) for a in range(3))
        goods.append(b[~np.any(div.reshape(len(b), -1), axis=1)])
    b = np.concatenate(goods)
    bitsarr = (((b[:, None] >> np.arange(nl)) & 1) * 2 - 1).astype(int)
    return b, [bitsarr[:, a * L ** 3:(a + 1) * L ** 3].reshape(-1, L, L, L) for a in range(3)]


def ref_ice(Ls):
    Lx,Ly,Lz=Ls; x,y,z=np.indices(Ls)
    return [((-1)**y).astype(int), ((-1)**x).astype(int), ((-1)**(x+y)).astype(int)]
def encode(E):
    bits=np.concatenate([(e.reshape(-1)==1).astype(np.uint8) for e in E])
    return int(''.join(map(str,bits[::-1])),2)
def decode(code,Ls):
    n=np.prod(Ls); nb=3*n; bits=np.array([(code>>i)&1 for i in range(nb)])*2-1
    return [bits[a*n:(a+1)*n].reshape(Ls) for a in range(3)]
def plaquettes(Ls):
    return [(a,b,r) for (a,b) in ((0,1),(1,2),(2,0)) for r in itertools.product(*[range(l) for l in Ls])]
def pstate(E,a,b,r,Ls):
    ea=np.eye(3,dtype=int)[a]; eb=np.eye(3,dtype=int)[b]; t=lambda v: tuple(np.mod(v,Ls))
    return (E[a][t(r)],E[b][t(np.add(r,ea))],E[a][t(np.add(r,eb))],E[b][t(r)]), [(a,t(r)),(b,t(np.add(r,ea))),(a,t(np.add(r,eb))),(b,t(r))]
def sector(Ls):
    ref=ref_ice(Ls); start=encode(ref); P=plaquettes(Ls)
    index={start:0}; confs=[start]; rows=[];cols=[]; nflip=[]
    i=0
    while i<len(confs):
        E=decode(confs[i],Ls); cnt=0
        for (a,b,r) in P:
            st,links=pstate(E,a,b,r,Ls)
            if st in ((1,1,-1,-1),(-1,-1,1,1)):
                cnt+=1
                for (aa,pos) in links: E[aa][pos]*=-1
                c=encode(E)
                if c not in index: index[c]=len(confs); confs.append(c)
                rows.append(index[c]); cols.append(i)
                for (aa,pos) in links: E[aa][pos]*=-1
        nflip.append(cnt); i+=1
    N=len(confs); F=sps.csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(N,N))
    return confs,index,F,np.array(nflip)
def translation_perm(confs,index,Ls,axis):
    perm=np.zeros(len(confs),dtype=np.int64)
    for i,c in enumerate(confs):
        E=decode(c,Ls); E2=[np.roll(e,1,axis=axis) for e in E]; perm[i]=index[encode(E2)]
    return perm
def study(Ls, Vs, axis_q=2, pol=0):
    t0=time.time(); confs,index,F,nflip=sector(Ls); N=len(confs); t1=time.time()
    perm=translation_perm(confs,index,Ls,axis_q); Lq=Ls[axis_q]; q=2*np.pi/Lq
    Epol=np.array([decode(c,Ls)[pol] for c in confs])            # (N, Lx, Ly, Lz)
    coord=np.arange(Lq); shape=[1,1,1]; shape[axis_q]=Lq
    A=(Epol*np.exp(1j*q*coord).reshape(shape)[None]).sum(axis=(1,2,3))
    def project(v):   # onto momentum q along axis_q: (1/L) sum_n e^{-iqn} T^n v ; T acts by the permutation
        out=np.zeros_like(v); w=v.copy()
        for nn in range(Lq):
            out+=np.exp(-1j*q*nn)*w; w=w[np.argsort(perm)] if False else w[perm]
        return out/Lq
    res=[]
    for V in Vs:
        H=(-F+V*sps.diags(nflip.astype(float))).tocsr()
        w0,v0=eigsh(H,k=1,which='SA'); psi0=v0[:,0]; e0=w0[0]
        phi=A*psi0; phi=phi-np.vdot(psi0,phi)*psi0; nrm=np.vdot(phi,phi).real
        sma=np.vdot(phi,H@phi).real/nrm-e0; ST=nrm/np.prod(Ls)
        # Lanczos in the momentum-q subspace starting from projected phi
        v=project(phi); v/=np.linalg.norm(v); vs=[v]; T=np.zeros((60,60)); vprev=np.zeros_like(v); beta=0.0
        for m in range(60):
            wv=H@v-beta*vprev; alpha=np.vdot(v,wv).real; wv=wv-alpha*v; wv=project(wv)
            for u in vs: wv-=np.vdot(u,wv)*u
            T[m,m]=alpha; beta=np.linalg.norm(wv)
            if beta<1e-10 or m==59: break
            T[m,m+1]=T[m+1,m]=beta; vprev,v=v,wv/beta; vs.append(v)
        low=np.linalg.eigvalsh(T[:m+1,:m+1])[0]-e0
        res.append((V,round(e0,4),round(low,4),round(sma,4),round(ST,4)))
    return N,round(t1-t0,1),res

codes_all, _ = enumerate_ice_fast(2)
confs2, index2, F2, nflip2 = sector((2, 2, 2))
H2 = (-F2 + sps.diags(nflip2.astype(float))).tocsr()
sector_levels = np.sort(np.linalg.eigvalsh(H2.toarray()))
N2, _, res2 = study((2, 2, 2), (1.0,))
V_, e0_, low_, sma_, ST_ = res2[0]
check("E: exact diagonalisation on 2x2x2 coarse cells (24 qubits): the RK ground state has energy zero; the lowest level at q = pi (momentum-projected) lies below the single-mode bound 1.6; "
      "the sector's lowest excitation (0.970) sits at zero momentum",
      abs(e0_) < 1e-9 and abs(sma_ - 1.6) < 1e-9 and low_ <= sma_ + 1e-9 and abs(sector_levels[1] - 0.9696) < 1e-3 and low_ > sector_levels[1] + 0.1,
      f"{len(codes_all)} constrained configurations, {N2} in the reference sector; E0 = {e0_}; at q = pi: lowest level {low_}, bound {sma_}, S_T {ST_}; "
      f"sector's lowest excitation {sector_levels[1]:.4f} (zero momentum)")

# ---------------------------------------------------------------- G beyond the RK point (2x2x3)
N3, t3, res3 = study((2, 2, 3), (1.0, 0.5, 0.0))
ST3 = [r[4] for r in res3]
check("G: beyond the RK point on a 2x2x3 cluster: the single-mode bound holds at V/K = 1, 0.5, 0, and S_T at the smallest q falls as V decreases (the mode stiffens); "
      "linear vs quadratic dispersion is not decidable at these momenta",
      all(r[2] <= r[3] + 1e-9 for r in res3) and ST3[0] > ST3[1] > ST3[2],
      f"{N3} states; (V/K, E0, lowest level at q = 2pi/3, bound, S_T): {res3}")

# ---------------------------------------------------------------- F harmonic regime: protected massless photons
def curl_matrix(k):
    ph = 2 * np.sin(k / 2)
    return np.array([[0, -ph[2], ph[1]], [ph[2], 0, -ph[0]], [-ph[1], ph[0], 0]], complex)


def spectrum(k, W, Z, m2=0.0):
    C = curl_matrix(k); Kmat = C.conj().T @ W(k) @ C + m2 * np.eye(3)
    ph = 2 * np.sin(k / 2); nrm_ = np.linalg.norm(ph)
    if nrm_ < 1e-12:
        P = np.eye(3)
    else:
        u = ph / nrm_; P = np.eye(3) - np.outer(u, u)       # transverse projector (the Gauss law removes the longitudinal E)
    Zk = Z(k); Zt = P @ Zk @ P
    ev, U = np.linalg.eigh(Zt); keep = ev > 1e-9
    Zh = U[:, keep] @ np.diag(np.sqrt(ev[keep])) @ U[:, keep].conj().T
    w2 = np.linalg.eigvalsh(Zh @ P @ Kmat @ P @ Zh)
    return np.sqrt(np.clip(np.sort(w2)[-2:], 0, None))     # two transverse modes


rngF = np.random.default_rng(11)
Bw = rngF.normal(size=(4, 3, 3)); Bz = rngF.normal(size=(4, 3, 3))
Wloc = lambda k: np.eye(3) + 0.3 * sum((B @ B.T) * np.cos(k[i % 3]) ** 2 for i, B in enumerate(Bw))
Zloc = lambda k: (np.eye(3) + 0.3 * sum((B @ B.T) * np.cos(k[(i + 1) % 3]) ** 2 for i, B in enumerate(Bz)))
I3 = lambda k: np.eye(3)
kdir = np.array([1.0, 0.37, 0.21]); kdir /= np.linalg.norm(kdir)
ks = [0.4, 0.2, 0.1, 0.05]
pure = [spectrum(t * kdir, I3, I3) for t in ks]
pert = [spectrum(t * kdir, Wloc, Zloc) for t in ks]
mass = [spectrum(t * kdir, Wloc, Zloc, m2=0.05) for t in ks]
lin = [p[0] / t for p, t in zip(pure, ks)]
check("F: harmonic regime: exactly two massless polarisations with linear dispersion; random local gauge-invariant perturbations keep them massless; a gauge-breaking A^2 term gaps them (P6)",
      all(abs(x - 1) < 0.01 for x in lin) and all(abs((p.max() / t) / (pert[-1].max() / ks[-1]) - 1) < 0.1 for p, t in zip(pert, ks)) and mass[-1].min() > 0.1,
      f"pure: omega/|k| at |k| = {ks}: {[round(x, 4) for x in lin]}; perturbed (gauge-invariant): omega/|k| = {[round(p.max() / t, 4) for p, t in zip(pert, ks)]}; "
      f"with A^2 mass: min omega {[round(p.min(), 4) for p in mass]}")

print("per_element: the constraint and each ring-exchange move are checked on explicit Z^3 neighbourhoods and on explicit configurations.")
print("per_site: every vertex site's six neighbours and every plaquette site's four in-plane neighbours are verified to be link (qubit) sites.")
print("per_mode: transverse and longitudinal structure factors at each lattice momentum; harmonic modes from explicit 3x3 symbols.")
print("per_block: exact diagonalisation of the 24-qubit and 36-qubit (34,080-state sector) clusters; loop Monte Carlo on 8^3 and 12^3 coarse tori.")
print("lattice_wide: checked and not executed - the linear photon away from the RK point in the full quantum model needs quantum Monte Carlo (not run).")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
