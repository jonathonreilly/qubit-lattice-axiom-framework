"""Root finite Galerkin probes of a separate two-component rotor instrument.

This is NOT a cubic-model simulation or a certified infinite-rotor enclosure.
It tests the larger sufficient window with noncommuting magnetic/electric
terms and full loss, alongside a cutoff comparison. The proof carries the
actual original-model assertion; these probes illustrate its mechanism.
"""
from pathlib import Path
import hashlib
import json
import math
import time

import numpy as np
import scipy
from scipy import sparse
from scipy.sparse.linalg import expm_multiply
from numpy.polynomial.legendre import leggauss


def probe(g, cutoff_width):
    n = math.ceil(cutoff_width / g) + 3
    m = np.arange(-n, n + 1, dtype=float)
    d = len(m)
    eye = sparse.eye(d, format="csc", dtype=complex)
    shift = sparse.diags(np.ones(d-1), -1, shape=(d, d), format="csc", dtype=complex)
    cosine = (shift + shift.getH()) / 2
    h0 = (g*g/2)*sparse.diags(m*m, format="csc") + (eye-cosine)/(g*g)
    v0 = np.exp(-g*g*m*m/2).astype(complex)
    v1 = -1j*g*m*v0
    v0 /= np.linalg.norm(v0)
    v1 /= np.linalg.norm(v1)
    states = expm_multiply(-0.23j*h0, np.column_stack([v0, v1]))
    norm_defects = np.sum(np.abs(states)**2, axis=0)-1
    assert np.max(np.abs(states.conj().T @ states - np.eye(2))) < 1e-11
    # Correct numerical unitary norm drift before resolving a small contrast
    # against the common constant background; the exact orbit is normalized.
    states /= np.linalg.norm(states, axis=0)
    h4 = sparse.bmat([
        [-3*eye+0.4*cosine, eye+0.2*cosine],
        [eye+0.2*cosine, -3*eye-0.4*cosine]], format="csc")
    # A finite Laurent jump with three terminal outputs. In the infinite
    # model L*L[0,0]=(23+2 cos(theta))/5 exactly.
    jump = sparse.bmat([
        [math.sqrt(21/5)*eye, None],
        [(eye+shift)/math.sqrt(5), 0.3*eye],
        [None, 2*eye]], format="csc")
    effect = jump.getH() @ jump
    loss = effect + sparse.eye(2*d, format="csc")
    electric = sparse.block_diag([
        sparse.diags(m*m), sparse.diags(m*(m-1))], format="csc")
    kappa = 0.3
    generator = -1j*((g*g/2)*electric + h4/(4*g*g)) - kappa*loss/2
    magnetic = -1j*h4/(4*g*g)
    eta = np.vstack([math.sqrt(5)*(shift @ states), np.zeros_like(states)])
    boundary = np.sum(eta.conj()*(effect @ eta), axis=0).real
    boundary_delta = boundary[1]-boundary[0]
    edge_mass = float(np.sum(np.abs(states[:3])**2)+np.sum(np.abs(states[-3:])**2))
    assert edge_mass < 1e-15
    nodes, weights = leggauss(20)
    rows = []
    for family, b in [("b_0.2_g3", 0.2*g**3),
                      ("b_0.2_g2", 0.2*g*g)]:
        full_values, magnetic_values, errors = [], [], []
        for z in nodes:
            u = b*(z+1)/2
            full = expm_multiply(u*generator, eta)
            mag = expm_multiply(u*magnetic, eta)
            assert np.max(np.linalg.norm(full, axis=0)-np.linalg.norm(eta,axis=0)) < 2e-11
            full_values.append(np.sum(full.conj()*(effect @ full),axis=0).real)
            magnetic_values.append(np.sum(mag.conj()*(effect @ mag),axis=0).real)
            errors.append(float(np.max(np.linalg.norm(full-mag,axis=0))/u))
        full_integral = b*np.dot(weights,np.array(full_values))/2
        magnetic_integral = b*np.dot(weights,np.array(magnetic_values))/2
        delta = full_integral[1]-full_integral[0]
        rows.append({
            "family":family, "b":b, "b_over_g2":b/g**2, "b_over_g4":b/g**4,
            "integrated_effect_vacuum":float(full_integral[0]),
            "integrated_effect_packet":float(full_integral[1]),
            "contrast_over_b_g2":float(delta/(b*g*g)),
            "boundary_contrast_over_g2":float(boundary_delta/(g*g)),
            "lag_contrast_remainder_over_b2":float((delta-b*boundary_delta)/(b*b)),
            "magnetic_contrast_over_b_g2":float((magnetic_integral[1]-magnetic_integral[0])/(b*g*g)),
            "maximum_sampled_full_minus_magnetic_norm_over_u":max(errors)})
    return {"g":g,"cutoff_width":cutoff_width,"fourier_cutoff":n,
            "component_dimension":d,"initial_orbit_edge_mass":edge_mass,
            "numerical_prebirth_squared_norm_defects_before_normalizing":norm_defects.tolist(),"rows":rows}


def main():
    start=time.perf_counter()
    probes=[probe(g,w) for g in (0.4,0.2,0.1,0.05) for w in (8,10)]
    comparisons=[]
    for coarse,fine in zip(probes[::2],probes[1::2]):
        diffs=[abs(a["contrast_over_b_g2"]-b["contrast_over_b_g2"])
               for a,b in zip(coarse["rows"],fine["rows"])]
        comparisons.append({"g":fine["g"],"scaled_contrast_cutoff_differences":diffs})
    last=probes[-1]["rows"][0]
    out={"scope":__doc__,"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "numpy":np.__version__,"scipy":scipy.__version__,"probes":probes,
         "cutoff_comparisons":comparisons,"probe_assertions_passed":True,
         "elapsed_seconds":time.perf_counter()-start}
    data=json.dumps(out,indent=2,allow_nan=False)+"\n"
    Path(__file__).with_name("CONTROL_RESULTS.json").write_text(data)
    print(data,end="")
    assert max(max(x["scaled_contrast_cutoff_differences"]) for x in comparisons)<2e-9
    assert abs(last["contrast_over_b_g2"]+1)<0.04


if __name__=="__main__":
    main()
