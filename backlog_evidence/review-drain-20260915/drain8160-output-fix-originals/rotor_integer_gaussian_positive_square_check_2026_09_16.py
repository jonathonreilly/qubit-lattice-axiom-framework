#!/usr/bin/env python3
"""Author challenges of topology, weighted metrics and compact positive squares."""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ROTOR_JOINT_GROUND_ENERGY_OSCILLATOR_DEFECT_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_UNIFORM_COMPACT_FIELD_SOFT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-16.md')
# Literal proof inputs are read below; the source self-hash is an integrity read.

_REPO = Path(__file__).resolve().parents[1]
for _input_path in AUDIT_INPUT_PATHS:
    _input_bytes = (_REPO / _input_path).read_bytes()
    if _input_path.endswith('.md'):
        assert ('claim_id: ' + Path(_input_path).stem.lower()).encode() in _input_bytes

assert 'A W_E A=C^* W_B C,' in (_REPO / AUDIT_INPUT_PATHS[0]).read_text()

TOL = 3e-9
out = {}
checks = 0


def require(condition, text):
    global checks
    if not bool(condition):
        raise AssertionError(text)
    checks += 1


def psd_functions(matrix):
    values, vectors = np.linalg.eigh(matrix)
    require(values.min() > -TOL, "positive semidefinite matrix")
    mask = values > 1e-10
    v = vectors[:, mask]
    t = values[mask]
    return (v*np.sqrt(t))@v.T, (v/np.sqrt(t))@v.T, v@v.T


def periodic_complex(L):
    cells = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    vertex = {x: n for n, x in enumerate(cells)}
    links = [(x, i) for x in cells for i in range(3)]
    link = {e: n for n, e in enumerate(links)}
    faces = [(x, i, j) for x in cells for i in range(3) for j in range(i+1, 3)]
    def step(x, i):
        y = list(x)
        y[i] = (y[i]+1) % L
        return tuple(y)
    D = np.zeros((len(cells), len(links)), dtype=int)
    for n, (x, i) in enumerate(links):
        D[vertex[x], n] = 1
        D[vertex[step(x, i)], n] = -1
    B = np.zeros((len(links), len(faces)), dtype=int)
    for n, (x, i, j) in enumerate(faces):
        B[link[(x, i)], n] += 1
        B[link[(step(x, i), j)], n] += 1
        B[link[(step(x, j), i)], n] -= 1
        B[link[(x, j)], n] -= 1
    winding = np.zeros((3, len(links)), dtype=int)
    for n, (_, i) in enumerate(links):
        winding[i, n] = 1
    return D, B, winding


def topology_and_metric():
    D, B, winding = periodic_complex(3)
    require(np.array_equal(D@B, np.zeros((27, 81))), "boundary squared")
    require(np.array_equal(winding@B, np.zeros((3, 81))), "zero winding of boundaries")
    smith = smith_normal_form(Matrix(B.tolist()), domain=ZZ)
    invariants = [abs(int(smith[i, i])) for i in range(min(smith.shape)) if smith[i, i]]
    rank_constraints = Matrix(np.vstack([D, winding]).tolist()).rank()
    require(len(invariants) == 81-rank_constraints == 52, "zero-winding cycle rank")
    require(set(invariants) == {1}, "primitive integer plaquette image")
    C = B.T.astype(float)
    e = np.tile([0.7, 1.1, 1.8], 27)
    b = np.tile([0.9, 1.4, 1.2], 27)
    S = np.sqrt(b)[:, None]*C*np.sqrt(e)[None, :]
    omega, omega_inverse, _ = psd_functions(S.T@S)
    omega_p, omega_p_inverse, _ = psd_functions(S@S.T)
    A = omega/np.sqrt(e)[:, None]/np.sqrt(e)[None, :]
    # Invert A on its positive range independently of the proposed formula.
    av, au = np.linalg.eigh(A)
    keep = av > 1e-10
    K = (au[:, keep]/av[keep])@au[:, keep].T
    U, singular, _ = np.linalg.svd(B.astype(float), full_matrices=False)
    basis = U[:, singular > 1e-10]
    projection = basis@basis.T
    K_formula = projection@(np.sqrt(e)[:, None]*omega_inverse*np.sqrt(e)[None, :])@projection
    errors = {
        "riccati": float(np.linalg.norm((A*e[None, :])@A-C.T@(b[:, None]*C))),
        "restricted_inverse": float(np.linalg.norm(K-K_formula)),
        "plaquette_metric": float(np.linalg.norm(C@K@C.T-omega_p/np.sqrt(b)[:, None]/np.sqrt(b)[None, :])),
        "trace": float(abs(np.trace(C@K@C.T*b[:, None])-np.trace(omega))),
    }
    require(max(errors.values()) < TOL, "weighted optimized metric")
    rng = np.random.default_rng(3402)
    c_lower = b.min()/math.sqrt(12*e.max()*b.max())
    dual_rows = []
    for _ in range(4):
        z = rng.integers(-2, 3, size=81)
        eta = projection@z
        q = C@z
        energy = float(eta@A@eta)
        alternative = float((np.sqrt(b)*q)@omega_p_inverse@(np.sqrt(b)*q))
        require(abs(energy-alternative) < TOL, "dual energy through integer curl")
        require(energy+TOL >= c_lower*(q@q), "dual curl coercivity")
        require(np.linalg.norm(C@eta-q) < TOL, "dual representative")
        dual_rows.append(dict(energy=energy, curl_formula=alternative,
                             coarse_lower=float(c_lower*(q@q))))
    out["periodic_integer_metric"] = dict(L=3, rank=52,
        nonzero_smith_invariants=invariants, constraints_rank=int(rank_constraints),
        errors=errors, dual=dual_rows)


def ladder_data():
    # Columns are literal boundaries of two adjacent squares.
    R = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [-1, 0],
                  [1, -1], [0, 1]], dtype=float)
    e = np.array([1, 2, 3, 1, 2, 4, 3], dtype=float)/2
    b = np.array([0.8, 1.4])
    S = np.sqrt(b)[:, None]*R.T*np.sqrt(e)[None, :]
    omega, _, _ = psd_functions(S.T@S)
    omega_p, omega_p_inverse, _ = psd_functions(S@S.T)
    A = omega/np.sqrt(e)[:, None]/np.sqrt(e)[None, :]
    av, au = np.linalg.eigh(A)
    good = av > 1e-10
    K = (au[:, good]/av[good])@au[:, good].T
    return R, e, b, S, omega, omega_p, omega_p_inverse, A, K


def exact_square():
    R, e, b, S, omega, omega_p, omega_p_inverse, A, K = ladder_data()
    M = S.T@omega_p_inverse
    cutoff = 7
    axis = np.arange(-cutoff, cutoff+1)
    nn = np.stack(np.meshgrid(axis, axis, indexing="ij"), axis=-1).reshape(-1, 2)
    index = {tuple(n): j for j, n in enumerate(nn)}
    dim = len(nn)
    eye = sparse.eye(dim, format="csr", dtype=complex)
    shifts = []
    for direction in range(2):
        rows, cols = [], []
        for col, n in enumerate(nn):
            shifted = n.copy()
            shifted[direction] += 1
            if tuple(shifted) in index:
                rows.append(index[tuple(shifted)])
                cols.append(col)
        shifts.append(sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(dim, dim), dtype=complex))
    cosines = [(u+u.getH())/2 for u in shifts]
    sines = [(u-u.getH())/(2j) for u in shifts]
    g = 0.37
    Ps = [sparse.diags(g*math.sqrt(e[l])*(nn@R[l])) for l in range(7)]
    Zs = [math.sqrt(b[p])/g*sines[p] for p in range(2)]
    Qs = [Ps[l]-1j*sum(M[l, p]*Zs[p] for p in range(2)) for l in range(7)]
    gauge = sum(P@P/2 for P in Ps)+sum(b[p]/g**2*(eye-cosines[p]) for p in range(2))
    rhs = sum(Q.getH()@Q/2 for Q in Qs)
    rhs += sum(omega_p[p, p]*cosines[p]/2 for p in range(2))
    rhs += sum(b[p]/(2*g**2)*(eye-cosines[p])@(eye-cosines[p]) for p in range(2))
    # M^*M=I here because the two plaquettes are independent.
    require(np.linalg.norm(M.T@M-np.eye(2)) < TOL, "ladder polar range")
    difference = gauge-rhs
    core = np.flatnonzero(np.all(np.abs(nn)<=cutoff-2, axis=1))
    core_error = float(sparse.linalg.norm(difference[core][:, core]))
    boundary_expected = sum(b[p]/(2*g**2)*(eye-sines[p]@sines[p]-cosines[p]@cosines[p]) for p in range(2))
    boundary_error = float(sparse.linalg.norm(difference-boundary_expected))
    full_difference = float(sparse.linalg.norm(difference))
    require(core_error < TOL, "positive-square identity on padded Fourier core")
    require(boundary_error < TOL and full_difference > 1, "retained hard-cutoff defect")
    # An incorrect sign for the cosine divergence must fail on the core.
    wrong = difference+sum(omega_p[p, p]*cosines[p] for p in range(2))
    wrong_error = float(sparse.linalg.norm(wrong[core][:, core]))
    require(wrong_error > 1, "divergence sign discriminator")
    out["positive_square"] = dict(cutoff=cutoff, dimension=dim, g=g,
        core_error=core_error, full_cutoff_discrepancy=full_difference,
        exact_boundary_formula_error=boundary_error, wrong_sign_core_error=wrong_error)


def optimized_theta():
    R, e, b, S, omega, omega_p, omega_p_inverse, A, K = ladder_data()
    metric = R.T@K@R
    electric_metric = R.T@(e[:, None]*R)
    dual_metric = np.sqrt(b)[:, None]*omega_p_inverse*np.sqrt(b)[None, :]
    require(np.linalg.norm(np.linalg.inv(metric)-dual_metric) < TOL, "dual coordinate metric")
    rows = []
    for g in [0.18, 0.4, 0.8]:
        cutoff = math.ceil(math.sqrt(90/(g*g*np.linalg.eigvalsh(metric)[0])))
        axis = np.arange(-cutoff, cutoff+1)
        n = np.stack(np.meshgrid(axis, axis, indexing="ij"), axis=-1).reshape(-1, 2)
        form = np.einsum("ni,ij,nj->n", n, metric, n)
        probabilities = np.exp(-g*g*form)
        normalization = probabilities.sum()
        probabilities /= normalization
        electric = 0.5*g*g*(probabilities@np.einsum("ni,ij,nj->n", n, electric_metric, n))
        beta = math.pi**2/g**2
        dual_cutoff = math.ceil(math.sqrt(90/(beta*np.linalg.eigvalsh(dual_metric)[0])))
        da = np.arange(-dual_cutoff, dual_cutoff+1)
        q = np.stack(np.meshgrid(da, da, indexing="ij"), axis=-1).reshape(-1, 2)
        qform = np.einsum("ni,ij,nj->n", q, dual_metric, q)
        dual = np.exp(-beta*qform)
        dual /= dual.sum()
        magnetic = 0.0
        max_overlap_error = 0.0
        for p in range(2):
            shifted = n.copy()
            shifted[:, p] -= 1
            shifted_form = np.einsum("ni,ij,nj->n", shifted, metric, shifted)
            overlap = np.exp(-g*g*(form+shifted_form)/2).sum()/normalization
            poisson_overlap = math.exp(-g*g*metric[p, p]/4)*(dual@np.where(q[:, p] % 2, -1., 1.))
            max_overlap_error = max(max_overlap_error, abs(overlap-poisson_overlap))
            magnetic += b[p]/g**2*(1-overlap)
        egamma = np.trace(omega)/2
        dual_error_bound = 2*b.max()/g**2*(dual@np.sum(q*q, axis=1))
        require(max_overlap_error < TOL, "exact parity-inserted dual overlap")
        require(electric <= egamma/2+TOL, "optimized electric bound")
        require(electric+magnetic <= egamma+dual_error_bound+TOL, "optimized trial total bound")
        rows.append(dict(g=g, cutoff=cutoff, dual_cutoff=dual_cutoff,
            electric=float(electric), magnetic=float(magnetic), free_energy=float(egamma),
            upper=float(egamma+dual_error_bound), overlap_error=float(max_overlap_error)))
    out["optimized_theta_trial"] = rows


def main():
    topology_and_metric()
    exact_square()
    optimized_theta()
    out["scope"] = "Finite author checks; the positive-square rotor identity is tested on a padded core, not at a hard boundary."
    out["tolerance"] = TOL
    out["runner_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out["checks"] = checks
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(out, indent=2)+"\n")
    print("Integer boundary lattice, weighted Gaussian, and positive-square challenges completed.")
    print(f"Full hard-cutoff discrepancy (expected): {out['positive_square']['full_cutoff_discrepancy']:.6g}")
    print(f"Wrong divergence sign discrepancy: {out['positive_square']['wrong_sign_core_error']:.6g}")
    print('per_element: executed — integer Smith invariants, weighted metrics and parity sums')
    print('per_site: executed — literal periodic 3-cube incidence and plaquette boundaries')
    print('per_mode: executed — positive-range matrix calculus and finite Fourier cutoff7')
    print('per_block: executed — padded-core square identity with full-cutoff discrepancy retained')
    print('lattice_wide: checked and not executed — uniform bounds and joint-limit/time arguments are written proofs; finite fixtures do not execute an infinite lattice')
    print(f"TOTAL: PASS={checks} FAIL=0")


if __name__ == "__main__":
    main()
