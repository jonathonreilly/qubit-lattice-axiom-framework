#!/usr/bin/env python3
"""
Gauge-sector velocity drag from the seagull-completed transverse vacuum
polarization. Self-contained, memory-safe (single process, chunked BZ loop,
only (chunk,4,4) matrices -- never an N^4 grid of matrices).

Cross-sector front-speed alignment v_F = v_gauge is the last open residual of
emergent Lorentz invariance (B4 does not cover it; the relative speed is a free
B4 invariant). The handle is the velocity-RG mutual-drag flow; the gauge half
needs the one-loop vacuum polarization Pi_munu(q) from the gauged staggered/
Kahler-Dirac fermion loop. A bubble-only assembly is NOT transverse (lattice
gluon-mass artifact); the two-gluon SEAGULL tadpole restores transversality.

Feynman rules (framework free propagators; gauged via k_mu -> k_mu + A_mu in the
hopping sin(k_mu)):
  fermion line   Sf(k) = (-i sum_mu v_mu sin(k_mu) gamma_mu) / (sum_mu v_mu^2 sin^2 k_mu)
  one-gluon vtx  D_mu(k->k+q)  = i gamma_mu cos(k_mu + q_mu/2)
  two-gluon sea  D_munu        = -i delta_munu gamma_mu sin(k_mu)
  Pi_munu(q) = Tr[Sf(k) D_mu Sf(k+q) D_nu] - Tr[Sf(k) D_munu]   (color factor T_F)

The vacuum polarization carries no internal gauge line, so Pi is gauge (xi)
INDEPENDENT; the gauge-sector velocity coefficient lambda_G read off from it is
gauge-invariant. Checks:
  (1) Euclidean Clifford {g_mu,g_nu}=2 delta.
  (2) lattice Ward identity khat_mu Pi_munu -> 0 with the seagull (transverse).
  (3) B4 isotropy at v=1: Pi_T(temporal) == Pi_T(spatial)  (c_t = c_s protected).
  (4) eta=v_F/v_b=1 is a fixed point: induced anisotropy vanishes at zero input.
  (5) gauge-sector finite-grid lambda_G proxy > 0 (log + finite split).
  (6) non-cancellation: fermion-half sign is opposite to lambda_G in BOTH Feynman
      and Landau gauge (the SIGN is gauge-robust), so the net relative-velocity
      drag does NOT cancel.

Class-A, deterministic. Expected: TOTAL: PASS=N FAIL=0.
"""
import numpy as np, math

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def banner(t): print("\n" + "=" * 76 + f"\n{t}\n" + "=" * 76)

# Euclidean gamma (4x4 Hermitian)
I2 = np.eye(2, dtype=complex); Z2 = np.zeros((2, 2), complex)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
blk = lambda A, B, C, D: np.block([[A, B], [C, D]])
g = np.array([blk(Z2, -1j*sx, 1j*sx, Z2), blk(Z2, -1j*sy, 1j*sy, Z2),
              blk(Z2, -1j*sz, 1j*sz, Z2), blk(I2, Z2, Z2, -I2)], complex)

banner("Clifford algebra of the Euclidean gammas")
cliff = all(np.allclose(g[a]@g[b] + g[b]@g[a], 2*(a == b)*np.eye(4)) for a in range(4) for b in range(4))
check("{gamma_mu, gamma_nu} = 2 delta_munu (Hermitian Euclidean set)", cliff)

def khat(qv): return 2*np.sin(np.array(qv)/2)

def pi_munu(qv, N, v, chunk=50000):
    """transverse vacuum polarization Pi_munu(q), chunked (memory-safe). color T_F=1/2 included."""
    q = np.array(qv, float); ax = (np.arange(N)+0.5)*2*np.pi/N - np.pi
    Pi = np.zeros((4, 4), complex); tot = N**4; i0 = 0
    while i0 < tot:
        idx = np.arange(i0, min(i0+chunk, tot)); i0 += chunk
        a, r = np.divmod(idx, N**3); b, r = np.divmod(r, N**2); c, d = np.divmod(r, N)
        k = np.stack([ax[a], ax[b], ax[c], ax[d]], 1); kq = k + q
        sk = np.sin(k)*v; skq = np.sin(kq)*v
        Dk = np.sum(sk**2, 1); Dkq = np.sum(skq**2, 1)
        Sk = (-1j*np.einsum('ca,aij->cij', sk, g))/Dk[:, None, None]
        Skq = (-1j*np.einsum('ca,aij->cij', skq, g))/Dkq[:, None, None]
        cmid = np.cos(k + q/2); sk_mu = np.sin(k)
        for mu in range(4):
            Vmu = 1j*cmid[:, mu][:, None, None]*g[mu]
            SV = Sk @ Vmu @ Skq
            for nu in range(4):
                Vnu = 1j*cmid[:, nu][:, None, None]*g[nu]
                Pi[mu, nu] += np.einsum('cii->', SV @ Vnu)
            Dmm = (-1j)*sk_mu[:, mu][:, None, None]*g[mu]
            Pi[mu, mu] += -np.einsum('cij,cji->', Sk, Dmm)
    return 0.5*Pi/tot   # T_F = 1/2

def ward(Pi, qv):
    return np.max(np.abs(khat(qv) @ Pi))/(np.max(np.abs(Pi)) + 1e-30)

def piT(qaxis, q, N, v):
    qv = [0., 0., 0., 0.]; qv[qaxis] = q
    Pi = np.real(pi_munu(qv, N, v)); b = (qaxis+1) % 4
    return Pi[b, b]/(khat(qv)[qaxis]**2)

iso = np.array([1., 1., 1., 1.])

banner("Ward identity: the seagull makes Pi transverse")
N = 16
wv = [ward(np.real(pi_munu(qv, N, iso)), qv)
      for qv in ([0., 0.4, 0., 0.], [0.3, 0.3, 0., 0.], [0., 0., 0., 0.5])]
check("lattice Ward khat_mu Pi_munu transverse to < 2% (bubble+seagull)",
      max(wv) < 0.02, f"violations = {[f'{w:.1e}' for w in wv]}")

banner("B4 isotropy at v=1: c_t = c_s protected")
qq = [0.5, 0.3, 0.18]
iso_ok = all(abs(piT(0, q, N, iso) - piT(1, q, N, iso)) < 1e-6 for q in qq)
check("Pi_T(temporal) == Pi_T(spatial) at v=1 (B4-isotropic)", iso_ok,
      f"max diff = {max(abs(piT(0,q,N,iso)-piT(1,q,N,iso)) for q in qq):.1e}")

banner("eta = v_F/v_b = 1 is a fixed point; lambda_G > 0 (finite-grid proxy)")
def induced(eps, q, N):
    v = np.array([1-eps/2, 1+eps/2, 1+eps/2, 1+eps/2])
    return piT(1, q, N, v) - piT(0, q, N, v)
check("induced anisotropy vanishes at eps=0 (eta=1 is a true fixed point)",
      abs(induced(0.0, 0.3, N)) < 1e-6, f"induced(eps=0) = {induced(0.0,0.3,N):.1e}")
qs = [0.5, 0.35, 0.25, 0.18]
slopes = [induced(0.10, q, N)/0.10 for q in qs]
X = np.array([math.log(1/q) for q in qs]); A_G, B_G = np.polyfit(X, slopes, 1)
check("gauge log attractor present (A_G>0) and finite-grid lambda_G proxy > 0",
      A_G > 0 and B_G > 0, f"A_G(log)={A_G:+.3f}  B_G=lambda_G={B_G:+.3f}")

banner("Non-cancellation: fermion-half sign is opposite to lambda_G in both gauges")
def sigma_kin_aniso(N, xi, dlt, eps=0.10, chunk=50000):
    """fermion velocity anisotropy (Sigma_s^kin - Sigma_t^kin) per unit gauge anisotropy eps.
       gauge boson anisotropic w=(1-eps/2,1+eps/2,...); gauge xi internal."""
    ax = (np.arange(N)+0.5)*2*np.pi/N - np.pi
    w = np.array([1-eps/2, 1+eps/2, 1+eps/2, 1+eps/2])
    out = {}
    for axis in (0, 1):
        p = [0., 0., 0., 0.]; p[axis] = dlt; p = np.array(p)
        Sig = np.zeros((4, 4), complex); tot = N**4; i0 = 0
        while i0 < tot:
            idx = np.arange(i0, min(i0+chunk, tot)); i0 += chunk
            a, r = np.divmod(idx, N**3); b, r = np.divmod(r, N**2); c, d = np.divmod(r, N)
            k = np.stack([ax[a], ax[b], ax[c], ax[d]], 1); pk = p - k
            s = np.sin(pk); Df = np.sum(s**2, 1)
            Sf = (-1j*np.einsum('ca,aij->cij', s, g))/Df[:, None, None]
            kh = 2*np.sin(k/2); K = np.sum(w*kh**2, 1); cmu = np.cos(p - k/2)
            for mu in range(4):
                VS = (cmu[:, mu][:, None, None]*g[mu]) @ Sf
                for nu in range(4):
                    Dmn = ((mu == nu)*1.0 - (1-xi)*kh[:, mu]*kh[:, nu]/K)/K
                    Sig += np.einsum('c,cij->ij', Dmn, (VS @ (cmu[:, nu][:, None, None]*g[nu])))
        Sig = -Sig/tot
        out[axis] = np.real(np.trace(g[axis] @ Sig)/(4j*np.sin(dlt)))
    return out[1] - out[0]
lamF_feyn = sigma_kin_aniso(N, 1.0, 0.30)
lamF_land = sigma_kin_aniso(N, 0.0, 0.30)
check("fermion-half velocity-anisotropy sign is NEGATIVE in both Feynman and Landau",
      lamF_feyn < 0 and lamF_land < 0, f"Feynman={lamF_feyn:+.4f}  Landau={lamF_land:+.4f}")
check("opposite sign to lambda_G>0  =>  net relative-velocity drag does NOT cancel",
      (lamF_feyn < 0) and (B_G > 0), "fermion<0, gauge>0 -> contributions add in the net")

banner("SUMMARY")
print("The two-gluon seagull tadpole restores transversality of the one-loop")
print("vacuum polarization (Ward identity satisfied), which a bubble-only assembly")
print("violates. On the transverse Pi: at v=1 the gauge sector is B4-isotropic")
print("(c_t=c_s); eta=v_F/v_b=1 is a fixed point; the gauge-sector finite-grid")
print("lambda_G proxy > 0 sits on top of the IR velocity-RG log attractor.")
print("The fermion-half velocity anisotropy has the OPPOSITE sign in both Feynman")
print("and Landau gauge (sign gauge-robust), so the cross-sector net does NOT")
print("cancel: residual D is a nonzero finite-grid proxy obstruction (quantified,")
print("not closed). The PRECISE net needs a gauge-invariant fermion-velocity")
print("prescription (the bare self-energy Z is gauge-dependent); proxy-level")
print("magnitudes and the taste/doubler normalization stay open.")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
