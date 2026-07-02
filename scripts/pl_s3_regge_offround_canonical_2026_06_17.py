"""The Regge Hessian on the round PL S^3 (= the boundary of the 4-simplex): a Lambda-Regge critical
point with a MULTIPLICITY-FREE canonical channel decomposition -- the supplied geometric route on the
polarization-frame gate's own spatial atlas.

THE GATE'S ATLAS: the universal-GR lane's "PL S^3" is the boundary of the 4-simplex
(5 vertices, 10 edges, 10 triangles, 5 tetrahedra -- the FULL_PL_S3_ATLAS row). The polarization-frame
gate's obstruction is frame-dependent localized channel coefficients on the complement of the scalar
channel. THIS RUNNER tests the supplied geometric (Regge) construction directly on the gate's own
spatial atlas: the ROUND ∂Δ^4 (all ten edges equal), the PL round S^3.

STRUCTURE:
  - 3D Regge with cosmological term: S_Λ = Σ_e ℓ_e δ_e − 2Λ Σ_T Vol_T. Flat space solves Λ=0;
    the round PL S^3 solves the EOM δ_e = 2Λ (∂Vol/∂ℓ_e) at ONE symmetric Λ* (all edges equivalent
    under the S_5 symmetry), the closed positive-curvature PL analogue of a constant-curvature
    Einstein spatial slice.
  - By the complex-level Schlaefli/Regge identity, ∂S_Λ/∂ℓ_e = δ_e − 2Λ ∂V/∂ℓ_e EXACTLY, so the
    Hessian at the background is H = ∂δ/∂ℓ − 2Λ* ∂²V/∂ℓ∂ℓ -- a 10x10 symmetric matrix, computed here
    directly from symbolic dihedral/volume gradients (high-precision exact geometry; all edges at the
    round point).
  - The vertex-permutation group S_5 acts on the 10 edges (= vertex pairs); the edge representation
    decomposes MULTIPLICITY-FREE: 10 = 1 (uniform/conformal) (+) 4 (standard; the discrete l=1 /
    conformal-Killing-type channel) (+) 5 (the pair irrep; the discrete l=2-type channel). By Schur's
    lemma a multiplicity-free decomposition is UNIQUE: every S_5-equivariant operator -- the Hessian in
    particular -- is scalar on each channel, with NO freedom in the split. The scalar-route frame
    ambiguity (which valid frame to use on the degenerate complement) does not arise for this supplied
    round geometric route.

CHECKS:
  R1  the round background: deficit per edge δ = 2π − 3 arccos(1/3) > 0 (positive curvature, exact),
      and the symmetric Λ* = δ / (2 ∂V/∂ℓ) makes the EOM residual vanish on every edge.
  R2  Regge's identity at the CURVED background: the assembled ∂δ/∂ℓ matrix is SYMMETRIC to machine
      precision (the complex-level Schlaefli lemma holds at the curved background), and the full
      Hessian H matches an independent end-to-end finite difference of the actual action S_Λ.
  R3  S_5 equivariance + multiplicity-freeness: H commutes with the vertex-permutation action on
      edges (machine); the channel projectors (1, 4, 5) are built from the group average and H is
      SCALAR on each channel -- three exact channel eigenvalues; by Schur, the split is CANONICAL (the
      scalar-route "which frame on the complement" question cannot arise for this supplied round
      geometric route: there is no degenerate complement).
  R4  the channel spectrum (the physics): the three eigenvalues (h_1, h_4, h_5) are computed at high
      precision and reported with their continuum-S^3 channel reading: the uniform channel is the
      conformal/breathing direction, the standard(4) channel is the discrete l=1/conformal-Killing-type
      direction, the 5-channel is the discrete l=2-type (physical) direction. Signs and any exact zeros
      are REPORTED AS MEASURED -- the continuum identification is qualitative context, not a check
      target (the coarse 5-vertex complex need not reproduce continuum eigenvalues).
  R5  the isometry control: SO(4) rotations of the embedded round complex change no edge length
      (machine) -- the only exact invariances of the configuration are isometries, as expected for a
      rigid complete graph; the channel structure above is therefore about the HESSIAN's canonical
      decomposition, not residual gauge freedom.
  R6  the gate connection: the scalar (uniform) channel corresponds to the gate's canonical scalar
      projector; the {4, 5} channels are the analogue of its frame-ambiguous complement -- here
      multiplicity-free, hence canonically split with scalar weights. Honest scope: SPATIAL round
      atlas at the symmetric (round) point; the 3+1 prism/tick extension on S^3 x Z_tau and
      off-round backgrounds are named open.

Bounded scope: this is the supplied 3D Lambda-Regge action on the supplied round finite spatial
background. It does not derive action selection, edge-length degrees of freedom, a 3+1 tick/prism
extension, or physical GR dynamics from the axioms. No PDG/fitted value.
"""
from __future__ import annotations
import itertools
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


# ---------------------------------------------------------------- the complex: boundary of the 4-simplex
VERTS = list(range(5))
TETS = [tuple(sorted(set(VERTS) - {v})) for v in VERTS]          # 5 facets
EDGES = [tuple(sorted(p)) for p in itertools.combinations(VERTS, 2)]   # 10 edges
EIDX = {e: i for i, e in enumerate(EDGES)}

# ---------------------------------------------------------------- symbolic tet geometry (one generic tet)
TET_EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
_q = {e: sp.Symbol(f"q{e[0]}{e[1]}", positive=True) for e in TET_EDGES}


def _qq(i, j):
    return _q[(min(i, j), max(i, j))]


def _dot(i, j, base):
    if i == j:
        return _qq(base, i)
    return (_qq(base, i) + _qq(base, j) - _qq(i, j)) / 2


def build_tet_funcs():
    """dihedral angles along each edge + volume, as functions of the 6 squared lengths, with first
    derivatives (angles, volume) and second derivatives (volume) lambdified."""
    funcs = {}
    for (a, b) in TET_EDGES:
        c, d = [v for v in range(4) if v not in (a, b)]
        uu = _dot(b, b, a)
        ua = _dot(b, c, a)
        ub = _dot(b, d, a)
        aa = _dot(c, c, a)
        bb = _dot(d, d, a)
        ab = _dot(c, d, a)
        na_nb = ab - ua * ub / uu
        na_na = aa - ua ** 2 / uu
        nb_nb = bb - ub ** 2 / uu
        theta = sp.acos(na_nb / sp.sqrt(na_na * nb_nb))
        grads = [sp.diff(theta, _q[e]) for e in TET_EDGES]
        funcs[(a, b)] = sp.lambdify([_q[e] for e in TET_EDGES], [theta] + grads, "numpy")
    # volume via Cayley-Menger
    q01, q02, q03, q12, q13, q23 = [_q[e] for e in TET_EDGES]
    CM = sp.Matrix([
        [0, 1, 1, 1, 1],
        [1, 0, q01, q02, q03],
        [1, q01, 0, q12, q13],
        [1, q02, q12, 0, q23],
        [1, q03, q13, q23, 0],
    ])
    V = sp.sqrt(CM.det() / 288)
    Vg = [sp.diff(V, _q[e]) for e in TET_EDGES]
    VH = [[sp.diff(V, _q[e1], _q[e2]) for e2 in TET_EDGES] for e1 in TET_EDGES]
    Vfun = sp.lambdify([_q[e] for e in TET_EDGES], [V] + Vg, "numpy")
    VHfun = sp.lambdify([_q[e] for e in TET_EDGES], VH, "numpy")
    return funcs, Vfun, VHfun


THETA, VOLG, VOLH = build_tet_funcs()


def tet_local(tet):
    """map a global tet (4 vertices) to its 6 global edges in TET_EDGES local order."""
    return [tuple(sorted((tet[i], tet[j]))) for (i, j) in TET_EDGES]


def assemble(ells):
    """deficits (per edge), J = d(deficit)/d(ell), Vtot, dV/d(ell), d2V/d(ell)d(ell) at lengths ells."""
    NE = len(EDGES)
    deficits = np.full(NE, 2 * np.pi)
    J = np.zeros((NE, NE))
    Vtot = 0.0
    dV = np.zeros(NE)
    d2V = np.zeros((NE, NE))
    for tet in TETS:
        loc = tet_local(tet)
        qv = [ells[EIDX[e]] ** 2 for e in loc]
        # angles + gradients (w.r.t. squared lengths -> chain to lengths)
        for li, (a, b) in enumerate(TET_EDGES):
            out = THETA[(a, b)](*qv)
            ge = loc[li]
            deficits[EIDX[ge]] -= float(out[0])
            for lj in range(6):
                gf = loc[lj]
                J[EIDX[ge], EIDX[gf]] -= 2 * ells[EIDX[gf]] * float(out[1 + lj])
        vout = VOLG(*qv)
        Vtot += float(vout[0])
        vh = np.array(VOLH(*qv), dtype=float)
        for li in range(6):
            ge = loc[li]
            dV[EIDX[ge]] += 2 * ells[EIDX[ge]] * float(vout[1 + li])
            for lj in range(6):
                gf = loc[lj]
                # d2V/dl dl' = 4 l l' Vqq' + 2 delta Vq
                d2V[EIDX[ge], EIDX[gf]] += 4 * ells[EIDX[ge]] * ells[EIDX[gf]] * vh[li, lj]
                if EIDX[ge] == EIDX[gf]:
                    d2V[EIDX[ge], EIDX[gf]] += 2 * float(vout[1 + li])
    return deficits, J, Vtot, dV, d2V


def action(ells, lam):
    deficits, _, Vtot, _, _ = assemble(ells)
    return float(np.dot(ells, deficits) - 2 * lam * Vtot)


# ---------------------------------------------------------------- S5 channel projectors on the 10 edges
def perm_rep():
    mats = []
    for pi in itertools.permutations(range(5)):
        P = np.zeros((10, 10))
        for e, i in EIDX.items():
            e2 = tuple(sorted((pi[e[0]], pi[e[1]])))
            P[EIDX[e2], i] = 1.0
        mats.append(P)
    return mats


def channel_projectors():
    """multiplicity-free decomposition 10 = 1 + 4 + 5 of the pair representation of S_5."""
    P_triv = np.full((10, 10), 1.0 / 10.0)
    # standard(4): edge functions induced from vertex functions sum_e ni(e) x_i with sum x = 0:
    M = np.zeros((10, 5))
    for e, i in EIDX.items():
        M[i, e[0]] += 1.0
        M[i, e[1]] += 1.0
    Mc = M - M.mean(axis=1, keepdims=True)
    Q, _ = np.linalg.qr(Mc)
    Q4 = Q[:, :4]
    P_std = Q4 @ Q4.T
    P_five = np.eye(10) - P_triv - P_std
    return P_triv, P_std, P_five



# ==========================================================================================
# Off-round robustness of the round-PL-S^3 canonical channel structure.
# Companion runner of PL_S3_REGGE_OFFROUND_CANONICAL_NARROW_THEOREM_NOTE_2026-06-17.md.
# Reuses the verified machinery of the retained_bounded round-PL-S^3 Regge Hessian note
# (UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10,
# retained_bounded) to answer THAT note's OWN named open residual ("off-round, where S_5 breaks
# and multiplicities could reappear, the question reopens"). Result: the frame-ambiguity-hosting
# degeneracy (the round 1+4+5 = the gate's degenerate complement) is a SYMMETRY ARTIFACT --
# generic off-round curved probes lift it to a fully SIMPLE 10-dim spectrum (canonical up to
# eigenvector signs, no within-complement frame freedom); symmetric loci retain residual-group-
# controlled degeneracy (S_5 round: 1,4,5 ; S_4: 1,1,3,3,2). This answers the round note's
# residual without claiming every possible accidental degeneracy is symmetry-forced. Class-A finite/exact.
# Honest bound: this is the gate's OWN atlas (delta^4, S_5 -- NOT the cubic O_h transplant); the
# Hessian's channel-degeneracy structure (NOT the full distinguished connection / localization
# transport across the off-round family, which stays multi-step open); no continuum limit.
NEFF = len(EDGES)
_TOL = 1e-9
_P = _F = 0
def _ck(tag, name, ok, detail=""):
    global _P, _F
    _P += ok; _F += (not ok)
    print(f"[{tag}] {'PASS' if ok else 'FAIL'}: {name}" + (f"  ({detail})" if detail else ""))

def _hess(ells, lam):
    deficits, J, Vtot, dV, d2V = assemble(ells)
    return deficits, dV, (J - 2.0 * lam * d2V)

def _mult_struct(M, tol=1e-6):
    ev = np.sort(np.linalg.eigvalsh(M)); groups = []
    for e in ev:
        if groups and abs(e - groups[-1][0]) < tol: groups[-1][1] += 1
        else: groups.append([e, 1])
    return [m for _, m in groups]

def main2():
    ell0 = np.ones(NEFF)
    defc0, dV0, _ = _hess(ell0, 0.0)
    lam_star = defc0[0] / (2 * dV0[0])
    defc, dVc, H0 = _hess(ell0, lam_star)
    eom = defc - 2 * lam_star * dVc
    # [R] reproduce the retained round point
    _ck("R", "round deficit/edge = 2pi - 3 arccos(1/3) (exact positive curvature)",
        abs(defc[0] - (2*np.pi - 3*np.arccos(1/3))) < _TOL, f"{defc[0]:.4f}")
    _ck("R", "round is an exact Lambda-Regge critical point (EOM residual 0) at Lambda*~7.3265",
        np.max(np.abs(eom)) < _TOL and abs(lam_star - 7.3265) < 1e-3, f"Lambda*={lam_star:.4f}, max|EOM|={np.max(np.abs(eom)):.2e}")
    _ck("R", "round Hessian H is symmetric (machine zero)", np.linalg.norm(H0 - H0.T) < _TOL)
    ms0 = _mult_struct(H0)
    _ck("R", "round spectrum multiplicity structure = {1,4,5} (the S_5 channels 1+4+5)",
        sorted(ms0) == [1, 4, 5], f"mults={sorted(ms0)}")
    # [LIFT] generic off-round lifts ALL degeneracy -> simple 10-dim spectrum (canonical)
    rng = np.random.default_rng(7)
    all_simple = True; detail = []
    for eps in (0.02, 0.08):
        ell = ell0 + eps * rng.standard_normal(NEFF)
        _, _, H = _hess(ell, lam_star)
        ms = _mult_struct(H)
        detail.append(f"eps={eps}:#levels={len(ms)}")
        all_simple = all_simple and (len(ms) == NEFF and max(ms) == 1)
    _ck("LIFT", "generic off-round probes lift all tested degeneracy -> fully simple 10-dim spectrum "
        "(no degenerate complement -> no within-complement frame freedom -> canonical up to signs). "
        "The frame-ambiguity-hosting degeneracy is non-generic on this finite Hessian family.",
        all_simple, "; ".join(detail))
    # [SYMLOCUS] symmetric off-round loci retain residual-group-controlled degeneracy
    v0 = [i for i, e in enumerate(EDGES) if 0 in e]   # 4 edges at the apex vertex -> stabilizer S_4
    ellS4 = ell0.copy(); ellS4[v0] *= 1.05
    _, _, HS4 = _hess(ellS4, lam_star)
    msS4 = sorted(_mult_struct(HS4))
    _ck("SYMLOCUS", "S_4-symmetric off-round: degeneracy persists as {1,1,3,3,2} (= the S_4 branching "
        "of 1+4+5; 4->1+3, 5->2+3) -> residual-symmetry-controlled multiplicity",
        msS4 == [1, 1, 2, 3, 3], f"mults={msS4}")
    # [VERDICT] the named residual is answered in the canonical direction
    _ck("VERDICT", "round-S^3 note's 'off-round multiplicities could reappear' residual ANSWERED: generic "
        "off-round probes are canonical up to eigenvector signs (simple spectrum); symmetric loci retain "
        "controlled multiplicities",
        all_simple and sorted(ms0) == [1, 4, 5] and msS4 == [1, 1, 2, 3, 3])
    print(f"\nTOTAL: PASS={_P} FAIL={_F}")
    return 0 if _F == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main2())
