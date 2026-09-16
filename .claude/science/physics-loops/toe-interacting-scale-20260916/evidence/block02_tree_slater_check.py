#!/usr/bin/env python3
"""Literal axial trees, charge dressing, and many-fermion Slater curvature."""
import hashlib
import json
import math
from pathlib import Path

import numpy as np


TOL = 2e-9
report = {}
checks = 0


def demand(value, why):
    global checks
    if not bool(value):
        raise AssertionError(why)
    checks += 1


def box(R):
    sites = [(x, y, z) for x in range(R) for y in range(R) for z in range(R)]
    vertex = {x: n for n, x in enumerate(sites)}
    edges = [(x, d) for x in sites for d in range(3) if x[d] < R-1]
    edge = {e: n for n, e in enumerate(edges)}
    faces = [(x, i, j) for x in sites for i in range(3) for j in range(i+1, 3)
             if x[i] < R-1 and x[j] < R-1]
    face = {p: n for n, p in enumerate(faces)}
    def step(x, d):
        y = list(x)
        y[d] += 1
        return tuple(y)
    D = np.zeros((len(sites), len(edges)), dtype=int)
    boundary = np.zeros((len(edges), len(faces)), dtype=int)
    for n, (x, d) in enumerate(edges):
        D[vertex[x], n], D[vertex[step(x, d)], n] = 1, -1
    for n, (x, i, j) in enumerate(faces):
        for e, sign in [((x, i), 1), ((step(x, i), j), 1),
                        ((step(x, j), i), -1), ((x, j), -1)]:
            boundary[edge[e], n] += sign
    paths = np.zeros((len(edges), len(sites)), dtype=int)
    for n, destination in enumerate(sites):
        current = (0, 0, 0)
        for d in range(3):
            for _ in range(destination[d]):
                paths[edge[(current, d)], n] += 1
                current = step(current, d)
    expected_Dpaths = -np.eye(len(sites), dtype=int)
    expected_Dpaths[0, :] += 1
    demand(np.array_equal(D@paths, expected_Dpaths), "rooted path incidence sign")
    loop_vectors = []
    counts = []
    for n, (x, d) in enumerate(edges):
        loop = paths[:, vertex[x]]-paths[:, vertex[step(x, d)]]
        loop = loop.copy()
        loop[n] += 1
        filling = np.zeros(len(faces), dtype=int)
        if d == 0:
            for y in range(x[1]):
                filling[face[((x[0], y, 0), 0, 1)]] -= 1
            for z in range(x[2]):
                filling[face[((x[0], x[1], z), 0, 2)]] -= 1
        elif d == 1:
            for z in range(x[2]):
                filling[face[((x[0], x[1], z), 1, 2)]] -= 1
        demand(np.array_equal(boundary@filling, loop), "literal strip fills fundamental loop")
        loop_vectors.append(loop)
        counts.append(int(np.abs(filling).sum()))
    demand(max(counts) <= 2*(R-1), "linear strip length")
    tree_edges = np.flatnonzero(np.any(paths != 0, axis=1))
    demand(len(tree_edges) == len(sites)-1, "tree edge count")
    demand(int(paths.sum()) == sum(sum(x) for x in sites), "subtree-size distance identity")
    return sites, edges, D, paths, np.array(loop_vectors), tree_edges, counts


def explicit_charge_dressing():
    sites, edges, D, paths, loops, tree, counts = box(2)
    V, E = len(sites), len(edges)
    index = {x: n for n, x in enumerate(sites)}
    rng = np.random.default_rng(3403)
    theta = rng.normal(scale=0.8, size=E)
    hoppings = rng.normal(size=E)+1j*rng.normal(size=E)
    onsite = rng.normal(size=V)
    def one_particle(phases):
        h = np.diag(onsite).astype(complex)
        for l, (x, d) in enumerate(edges):
            y = list(x)
            y[d] += 1
            a, b = index[x], index[tuple(y)]
            h[a, b] = hoppings[l]*np.exp(1j*phases[l])
            h[b, a] = h[a, b].conjugate()
        return h
    h0 = one_particle(np.zeros(E))
    values, vectors = np.linalg.eigh(h0)
    phi = vectors[:, 0]
    pair = np.kron(phi, phi.conj())
    flows = np.array([-paths[:, a]+paths[:, b] for a in range(V) for b in range(V)])
    charges = np.array([np.eye(V, dtype=int)[:, a]-np.eye(V, dtype=int)[:, b]
                        for a in range(V) for b in range(V)])
    demand(np.array_equal(flows@D.T, charges), "exact integer charged Gauss sector")
    dressed = np.exp(1j*(flows@theta))*pair
    htheta = one_particle(theta)
    Htheta = np.kron(htheta, np.eye(V))+np.kron(np.eye(V), htheta.conj())
    direct_energy = float(np.vdot(dressed, Htheta@dressed).real)
    effective = one_particle(loops@theta)
    loop_energy = float(2*np.vdot(phi, effective@phi).real)
    demand(abs(direct_energy-loop_energy) < TOL, "dressed hopping loop phase")
    probabilities = np.abs(pair)**2
    mean_flow = probabilities@flows
    flow_square = probabilities@(flows*flows)
    demand(np.max(np.abs(mean_flow)) < TOL, "zero electric cross term")
    subtree_probabilities = np.abs(phi)**2@paths.T
    variance_formula = 2*subtree_probabilities*(1-subtree_probabilities)
    demand(np.max(np.abs(flow_square-variance_formula)) < TOL, "paired tree-charge variance")
    wrong_dressed = np.exp(-1j*(flows@theta))*pair
    wrong_energy = float(np.vdot(wrong_dressed, Htheta@wrong_dressed).real)
    demand(abs(wrong_energy-loop_energy) > 0.01, "tree dressing sign discriminator")
    report["literal_charged_dressing"] = dict(vertices=V, links=E,
        physical_matter_dimension=V*V, direct_energy=direct_energy, loop_energy=loop_energy,
        energy_error=abs(direct_energy-loop_energy), wrong_sign_discrepancy=abs(wrong_energy-loop_energy),
        maximal_mean_flow=float(np.max(np.abs(mean_flow))),
        variance_error=float(np.max(np.abs(flow_square-variance_formula))),
        sum_charge_variance=float(flow_square.sum()),
        subtree_size_sum=int(paths.sum()), maximal_filling_size=max(counts))


def wilson_slater(R):
    sites, edges, D, paths, loops, tree, counts = box(R)
    V = len(sites)
    index = {x: n for n, x in enumerate(sites)}
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]], complex)
    sz = np.diag([1, -1]).astype(complex)
    bloch_shift = 0.37
    matrices = [np.exp(-1j*bloch_shift)*(-sz-1j*sx)/2,
                (-sz-1j*sy)/2, -sz/2]
    h = np.kron(np.eye(V), 2.5*sz)
    for x, d in edges:
        y = list(x)
        y[d] += 1
        a, b = index[x], index[tuple(y)]
        h[2*a:2*a+2, 2*b:2*b+2] = matrices[d]
        h[2*b:2*b+2, 2*a:2*a+2] = matrices[d].conj().T
    u_squared = np.exp(2j*bloch_shift*np.array([x[0] for x in sites]))
    antiunitary_matrix = np.kron(np.diag(u_squared), sx)
    ph_error = float(np.linalg.norm(antiunitary_matrix@h.conj()@antiunitary_matrix.conj().T+h))
    demand(ph_error < TOL, "open-block Wilson particle-hole symmetry")
    energies, vectors = np.linalg.eigh(h)
    occupied = vectors[:, :V]
    covariance = occupied@occupied.conj().T
    total_variance = 0.0
    largest_subtree = None
    for l in tree:
        members = np.flatnonzero(paths[l])
        orbitals = np.ravel(np.column_stack([2*members, 2*members+1]))
        restriction = covariance[np.ix_(orbitals, orbitals)]
        variance = float(2*np.trace(restriction-restriction@restriction).real)
        demand(-TOL <= variance <= 4*len(members)+TOL, "Slater subtree variance bound")
        total_variance += variance
        if largest_subtree is None or len(orbitals) > len(largest_subtree):
            largest_subtree = orbitals
    bound = 4*paths.sum()
    demand(total_variance <= bound+TOL, "total tree-charge cost")
    restriction = covariance[np.ix_(largest_subtree, largest_subtree)]
    exact_variance = float(2*np.trace(restriction-restriction@restriction).real)
    rows = []
    for step in [0.08, 0.04, 0.02]:
        phase = np.ones(2*V, dtype=complex)
        phase[largest_subtree] = np.exp(1j*step)
        determinant = np.linalg.det(occupied.conj().T@(phase[:, None]*occupied))
        paired_overlap = abs(determinant)**2
        finite_difference = 2*(1-paired_overlap)/step**2
        rows.append(dict(step=step, variance=finite_difference,
                         error=abs(finite_difference-exact_variance)))
    ratios = [rows[j]["error"]/rows[j+1]["error"] for j in range(2)]
    demand(min(ratios)>3.8, "determinant fidelity curvature convergence")
    return dict(R=R, sites=V, orbitals=2*V, particles_per_species=V,
        particle_hole_error=ph_error, nearest_single_particle_energy=float(np.min(np.abs(energies))),
        sum_charge_variance=total_variance, analytic_upper=int(bound),
        subtree_size_sum=int(paths.sum()), maximal_loop_filling=max(counts),
        determinant_variance=exact_variance, curvature_checks=rows, convergence_ratios=ratios)


def main():
    explicit_charge_dressing()
    report["half_filled_wilson_blocks"] = [wilson_slater(R) for R in [2, 3, 4]]
    report["scope"] = "Finite author checks of exact Gauss dressing and Slater identities; no interacting phase calculation."
    report["tolerance"] = TOL
    report["runner_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report["checks"] = checks
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2)+"\n")
    print("Literal axial tree, charge dressing, and Slater curvature challenges completed.")
    print(f"Wrong dressing sign discrepancy: {report['literal_charged_dressing']['wrong_sign_discrepancy']:.6g}")
    for row in report["half_filled_wilson_blocks"]:
        print(f"R={row['R']}: summed charge variance={row['sum_charge_variance']:.6g}, analytic upper={row['analytic_upper']}")
    print(f"TOTAL: PASS={checks} FAIL=0")


if __name__ == "__main__":
    main()
