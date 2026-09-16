#!/usr/bin/env python3
"""Finite author challenges; no numerical phase or infinite-volume proof."""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse


TOL = 2e-10
results = {}


def must(condition, message):
    if not bool(condition):
        raise AssertionError(message)


def theta_challenges():
    # Two literal adjacent squares, sharing a link with opposite orientations.
    vertices = [(x, y) for y in range(2) for x in range(3)]
    edges = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]
    D = np.zeros((6, 7), dtype=int)
    for e, (x, y) in enumerate(edges):
        D[x, e], D[y, e] = 1, -1
    R = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [-1, 0],
                  [1, -1], [0, 1]], dtype=int)
    must(np.array_equal(D @ R, np.zeros((6, 2))), "literal Gauss constraint")
    must(np.linalg.matrix_rank(R) == 7 - np.linalg.matrix_rank(D), "cycle rank")
    weights = np.array([1, 2, 3, 1, 2, 4, 3], dtype=float) / 2
    G = R.T @ (weights[:, None] * R)
    out = []
    for t in [0.07, 0.23, 0.9, 2.6]:
        def gaussian_data(Q, coefficient):
            # Discarded terms start beyond exp(-90) in the Euclidean-radius
            # lower bound. Direct/dual agreement is a challenge, not a proof
            # of an infinite sum or a rigorous interval certificate.
            cutoff = math.ceil(math.sqrt(90 / (coefficient * np.linalg.eigvalsh(Q)[0])))
            axis = np.arange(-cutoff, cutoff + 1)
            n = np.stack(np.meshgrid(axis, axis, indexing="ij"), axis=-1).reshape(-1, 2)
            quadratic = np.einsum("ni,ij,nj->n", n, Q, n)
            w = np.exp(-coefficient * quadratic)
            return n, quadratic, w, cutoff
        n, q, wt, cutoff = gaussian_data(G, t)
        z = wt.sum()
        moment = (q @ wt) / z
        _, qd, wd, dual_cutoff = gaussian_data(np.linalg.inv(G), math.pi**2 / t)
        z_poisson = (math.pi / t) / math.sqrt(np.linalg.det(G)) * wd.sum()
        moment_poisson = 1 / t - math.pi**2 / t**2 * (qd @ wd) / wd.sum()
        overlap_rows = []
        for shift in [np.array([1, 0]), np.array([0, 1]), np.array([1, 1])]:
            moved = n - shift
            qp = np.einsum("ni,ij,nj->n", moved, G, moved)
            direct_overlap = np.exp(-0.5 * t * (q + qp)).sum() / z
            lower = math.exp(-0.5 * t * (shift @ G @ shift))
            must(lower <= direct_overlap + TOL <= 1 + 2 * TOL, "shift overlap/Jensen")
            overlap_rows.append(dict(shift=shift.tolist(), overlap=float(direct_overlap), lower=lower))
        must(abs(z_poisson / z - 1) < TOL, "Poisson normalization")
        must(abs(moment - moment_poisson) < TOL, "Poisson derivative sign")
        must(moment <= 1 / t + TOL, "rank-two moment bound")
        out.append(dict(t=t, cutoff=cutoff, dual_cutoff=dual_cutoff,
                        normalization_error=float(abs(z_poisson / z - 1)),
                        moment=float(moment), moment_bound=1/t,
                        moment_identity_error=float(abs(moment-moment_poisson)),
                        overlaps=overlap_rows))
    # A ring with no faces has a genuine harmonic cycle. A face-only trial
    # would omit this rank-one electric direction.
    ring_D = np.zeros((4, 4), dtype=int)
    for e in range(4):
        ring_D[e, e] = 1
        ring_D[(e+1) % 4, e] = -1
    harmonic = np.ones(4, dtype=int)
    must(np.array_equal(ring_D @ harmonic, np.zeros(4)), "harmonic Gauss direction")
    results["theta_trial"] = dict(gram=G.tolist(), cases=out,
                                   harmonic_rank=4-int(np.linalg.matrix_rank(ring_D)))


def annihilator(mode, modes):
    size = 1 << modes
    a = np.zeros((size, size), dtype=complex)
    for n in range(size):
        if n & (1 << mode):
            sign = -1 if (n & ((1 << mode)-1)).bit_count() % 2 else 1
            a[n ^ (1 << mode), n] = sign
    return a


def wilson_hopping_challenge():
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]], complex)
    sz = np.diag([1, -1]).astype(complex)
    matrices = [(-sz-1j*sx)/2, (-sz-1j*sy)/2, -sz/2]
    # One species on two sites, two orbitals each: literal 16-dimensional CAR.
    aa = [annihilator(i, 4) for i in range(4)]
    rows = []
    for T in matrices:
        hopping = sum(T[i, j]*aa[i].conj().T@aa[2+j] for i in range(2) for j in range(2))
        spectrum = np.linalg.eigvalsh(hopping+hopping.conj().T)
        nuclear = np.linalg.svd(T, compute_uv=False).sum()
        must(abs(nuclear-1) < TOL, "Wilson nuclear norm")
        must(abs(spectrum[0]+nuclear) < TOL and abs(spectrum[-1]-nuclear) < TOL,
             "literal hopping extremal energies")
        rows.append(dict(singular_values=np.linalg.svd(T, compute_uv=False).tolist(),
                         fock_extrema=[float(spectrum[0]), float(spectrum[-1])]))
    must(np.linalg.norm(matrices[2], 2) < 1, "operator norm differs from nuclear norm")
    results["wilson_hopping"] = rows


def cubic_curl(L):
    sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    index = {x: i for i, x in enumerate(sites)}
    pairs = [(0, 1), (0, 2), (1, 2)]
    def shifted(x, direction, amount=1):
        y = list(x)
        y[direction] = (y[direction]+amount) % L
        return tuple(y)
    rows, cols, data = [], [], []
    for x in sites:
        n = index[x]
        for p, (i, j) in enumerate(pairs):
            entries = [(x, i, 1), (shifted(x, i), j, 1),
                       (shifted(x, j), i, -1), (x, j, -1)]
            for y, direction, sign in entries:
                rows.append(3*n+p)
                cols.append(3*index[y]+direction)
                data.append(sign)
    C = sparse.csr_matrix((data, (rows, cols)), shape=(3*L**3, 3*L**3), dtype=float)
    return sites, C


def wavepacket_challenges():
    out = []
    for R in [3, 4, 7, 12]:
        L = R+3
        sites, C = cubic_curl(L)
        h = np.zeros(L)
        for n in range(R+1):
            h[n] = math.sqrt(8/(3*R))*math.sin(math.pi*n/R)**2
        v = np.zeros(3*L**3)
        for n, (x, y, z) in enumerate(sites):
            v[3*n] = h[x]*h[y]*h[z]
        cv = C @ v
        s2 = float(cv @ cv)
        w = cv / math.sqrt(s2)
        t2 = float(np.linalg.norm(C.T @ w)**2)
        expected_s2 = 8/3*math.sin(math.pi/R)**2
        expected_t2 = (20/3-4/R)*math.sin(math.pi/R)**2
        errors = [abs(np.linalg.norm(v)-1), abs(s2-expected_s2), abs(t2-expected_t2)]
        must(max(errors) < TOL, "literal compact wavepacket geometry")
        out.append(dict(R=R, L=L, s2=s2, t2=t2, max_error=max(errors)))
    results["wavepacket_geometry"] = out


def magnetic_mode_challenges():
    out = []
    for L in [3, 4, 5, 6]:
        sites, C = cubic_curl(L)
        V = L**3
        k = 2*math.pi/L
        s = 2*math.sin(k/2)
        v = np.zeros(3*V)
        w = np.zeros(3*V)
        for n, (x, y, z) in enumerate(sites):
            v[3*n] = -math.sqrt(2/V)*math.sin(k*(z-0.5))
            w[3*n+1] = math.sqrt(2/V)*math.cos(k*z)
        must(np.linalg.norm(C@v-s*w) < TOL, "plane-wave curl phase")
        # Translate one deterministic bounded plaquette configuration through
        # all sites. This is an exactly translation-invariant classical
        # ensemble, sufficient to challenge the geometric identity (17).
        coords = np.indices((L, L, L))
        theta = 0.7*np.cos(2*math.pi*coords[0]/L)+2.1*np.sin(2*math.pi*coords[1]/L)
        theta += 0.9*np.cos(2*math.pi*(coords[2]+coords[0])/L)
        cosines = np.cos(theta)
        rho = float((1-cosines).mean())
        shifted_z = np.roll(cosines, 1, axis=2)
        shifted_x = np.roll(cosines, 1, axis=0)
        gamma_z = float((cosines*shifted_z).mean())
        difference_z = float(((cosines-shifted_z)**2).mean())
        difference_x = float(((cosines-shifted_x)**2).mean())
        e_x, e_z = 1.3, 0.7
        edge_weights = np.tile([e_x, 0.9, e_z], V)
        literal = 0.0
        for offset in sites:
            translated = np.roll(cosines, offset, axis=(0, 1, 2)).reshape(-1)
            wc = w.copy()
            wc[1::3] *= translated
            derivative = C.T @ wc
            literal += float((edge_weights*derivative) @ derivative)/V
        predicted = e_x*(s*s*gamma_z+difference_z)+e_z*difference_x
        upper = e_x*s*s+4*(e_x+e_z)*rho
        must(abs(literal-predicted) < TOL, "compact magnetic translation identity")
        must(predicted <= upper+TOL, "compact fluctuation bound")
        out.append(dict(L=L, rho=rho, literal=literal, identity=predicted,
                        upper=upper, error=abs(literal-predicted),
                        discrepancy_if_cosines_replaced_by_one=abs(literal-e_x*s*s)))
    results["magnetic_mode"] = out


def spectral_challenges():
    H = np.diag([0., 0., 0.35, 0.8, 1.9, 3.1])
    rng = np.random.default_rng(3401)
    X = rng.normal(size=H.shape)
    F = (X+X.T)/2
    B = 1j*(H@F-F@H)
    rho = np.diag([0.5, 0.5, 0, 0, 0, 0])
    def comm(A, B):
        return A@B-B@A
    mF = float((np.trace(rho@comm(F, comm(H, F)))/2).real)
    mB = float((np.trace(rho@comm(B, comm(H, B)))/2).real)
    c = float(abs(np.trace(rho@comm(F, B))))
    energies = np.diag(H)[2:]
    muF = np.abs(F[2:, :2])**2 @ np.array([0.5, 0.5])
    muB = np.abs(B[2:, :2])**2 @ np.array([0.5, 0.5])
    must(abs(mF-energies@muF) < TOL and abs(mB-energies@muB) < TOL, "spectral first moments")
    rows = []
    for cutoff in [0.2, 0.35, 0.6, 0.8, 1.9, 2.6, 3.1, 8., 20.]:
        actual = float((muF+muB)[energies<=cutoff].sum())
        bound = c-2*math.sqrt(mF*mB)/cutoff
        must(actual+TOL >= bound, "inelastic two-observable inequality")
        rows.append(dict(cutoff=cutoff, actual=actual, lower=bound))
    # Necessary failure control: a pure vector in a degenerate ground space
    # can have a nonzero *elastic* commutator and zero inelastic measures.
    F0 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex)
    B0 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex)
    pure_elastic = float(abs(comm(F0, B0)[0, 0]))
    trace_elastic = float(abs(np.trace(np.diag([0.5, 0.5, 0])@comm(F0, B0))))
    must(pure_elastic == 2 and trace_elastic == 0, "degenerate-ground failure control")
    # The coefficient two on the high-energy cross term is necessary.
    # With H=diag(0,1), F=sigma_x and B=sigma_y, c=2 and M_F=M_B=1.
    # Below energy one there is zero inelastic weight; omitting that factor
    # would falsely force positive weight at lambda=3/4.
    H2 = np.diag([0., 1.])
    rho2 = np.diag([1., 0.])
    F2, B2 = F0[:2, :2], B0[:2, :2]
    mF2 = float((np.trace(rho2@comm(F2, comm(H2, F2)))/2).real)
    mB2 = float((np.trace(rho2@comm(B2, comm(H2, B2)))/2).real)
    c2 = float(abs(np.trace(rho2@comm(F2, B2))))
    eigenvalues2, eigenvectors2 = np.linalg.eigh(H2)
    low2 = eigenvectors2[:, (eigenvalues2>0) & (eigenvalues2<=0.75)]
    projection2 = low2@low2.conj().T
    actual2 = float(np.trace(rho2@(F2@projection2@F2+B2@projection2@B2)).real)
    wrong_factor_lower = c2-math.sqrt(mF2*mB2)/0.75
    correct_factor_lower = c2-2*math.sqrt(mF2*mB2)/0.75
    must(wrong_factor_lower > actual2 and correct_factor_lower <= actual2,
         "missing-factor failure control")
    results["spectral_inequality"] = dict(commutator=c, moments=[mF, mB], cases=rows,
                                         pure_elastic_counterexample=pure_elastic,
                                         ground_trace_elastic=trace_elastic,
                                         wrong_factor_control={"actual": actual2,
                                             "wrong_lower": wrong_factor_lower,
                                             "correct_lower": correct_factor_lower})


def main():
    theta_challenges()
    wilson_hopping_challenge()
    wavepacket_challenges()
    magnetic_mode_challenges()
    spectral_challenges()
    results["scope"] = "Finite author checks only; no independent review or phase proof."
    results["tolerance"] = TOL
    results["runner_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps({"checks": list(results)[:-3], "scope": results["scope"],
                      "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()
