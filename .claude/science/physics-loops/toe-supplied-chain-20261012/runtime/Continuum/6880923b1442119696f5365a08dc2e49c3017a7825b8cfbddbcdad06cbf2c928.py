"""Compact-packet continuum, moving-residual, translations and Fock diagnostics."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre


def quadrature(radius, points):
    x, w = roots_legendre(points)
    return radius*x, radius*w


def norm(z, w):
    return float(np.sqrt(np.dot(w, abs(z)**2)))


def packet(center=0.0, width=0.7, eta=0.41):
    x, w = roots_legendre(800)
    normalization = np.sqrt(width*np.dot(w, np.exp(-2/(1-x*x))))
    def values(q):
        q = np.asarray(q)
        x = (q-center)/width
        inside = abs(x) < 1
        f = np.zeros_like(q, dtype=complex)
        fp = np.zeros_like(q, dtype=complex)
        z = x[inside]
        f[inside] = np.exp(-1/(1-z*z)+1j*eta*q[inside])/normalization
        fp[inside] = f[inside]*(-2*z/(width*(1-z*z)**2)+1j*eta)
        return f, fp
    return values


def line(q, s, m, v, packet_values):
    E = np.sqrt(m*m+v*v*q*q)
    F = q*np.cosh(v*s)+E*np.sinh(v*s)/v
    EF = E*np.cosh(v*s)+v*q*np.sinh(v*s)
    J = EF/E
    f, fp = packet_values(F)
    out = np.sqrt(J)*f
    Ep = v*v*q/E
    EFp = v*v*F/EF
    derivative = np.sqrt(J)*(J*fp+(EFp-Ep)*f/(2*E))
    return out, derivative


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location("candidate_under_test", args.candidate)
    target = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(target)
    predicates = []
    def check(label, observed, bound, slack=2e-9):
        predicates.append({"label": label, "observed": float(observed),
                           "bound": float(bound), "slack": slack,
                           "ok": bool(observed <= bound+slack)})
    m, v, R, S = 1.2, 0.83, 0.7, 0.35
    M = (R+m/v)*np.exp(v*S)-m/v
    E = lambda q: np.sqrt(m*m+v*v*np.asarray(q)**2)
    Ep = lambda q: v*v*np.asarray(q)/E(q)
    fpair = packet(width=R)
    f = lambda q: fpair(q)[0]
    q0, w0 = quadrature(R, 800)
    f0, fp0 = fpair(q0)
    fnorm = norm(f0, w0)
    bnorm = norm(1j*(E(q0)*fp0+Ep(q0)*f0/2), w0)
    D = bnorm/m+v*fnorm/(4*m)
    c0 = v*v*M**4/(24*m)
    c1 = v*v*M**3/(6*m)+v**4*M**5/(24*m**3)
    q, w = quadrature(M, 900)
    tx, tw = roots_legendre(36)
    rows = []
    for a in [0.4, 0.2, 0.1, 0.05]:
        sigma = np.sqrt(m*m/4+v*v/a**2)
        g, coupling = sigma/2+m/4, sigma/2-m/4
        # Parent kernel route, not candidate.energy or target derivative.
        Ea = 2*np.sqrt(g*g+coupling*coupling-2*g*coupling*np.cos(a*q))
        Eap = 4*g*coupling*a*np.sin(a*q)/Ea
        check(f"coefficient_E_a_{a}", np.max(E(q)-Ea), a*a*c0)
        check(f"coefficient_Eprime_a_{a}", np.max(abs(Ep(q)-Eap)), a*a*c1)
        for s in [S, -S]:
            psi, _ = line(q, s, m, v, fpair)
            residual_integrals = {True: 0.0, False: 0.0}
            max_derivative = 0.0
            for tau, weight in zip(s*(tx+1)/2, abs(s)*tw/2):
                moving, derivative = line(q, tau, m, v, fpair)
                max_derivative = max(max_derivative, norm(derivative, w))
                centered_residual = 1j*((Ea-E(q))*derivative+(Eap-Ep(q))*moving/2)
                original_residual = centered_residual-a*Ea*moving/2
                residual_integrals[True] += weight*norm(centered_residual, w)
                residual_integrals[False] += weight*norm(original_residual, w)
            check(f"moving_derivative_a_{a}_s_{s}", max_derivative, D)
            for centered in [True, False]:
                actual, endpoint, ode = target.transport(q, s, a, m, v, f, centered=centered)
                error = norm(actual-psi, w)
                majorant = abs(s)*a*a*(c0*D+c1*fnorm/2)
                if not centered:
                    majorant += abs(s)*a*E(M)*fnorm/2
                integ = residual_integrals[centered]
                label = f"{'centered' if centered else 'original'}_a_{a}_s_{s}"
                check(label+"_group_error_le_actual_Duhamel_integral", error, integ)
                check(label+"_group_error_le_analytic_bound", error, majorant)
                check(label+"_actual_Duhamel_integral_le_analytic_bound", integ, majorant)
                check(label+"_norm", abs(norm(actual, w)-fnorm), 0)
                rows.append({"a": a, "s": s, "centered": centered,
                             "group_error": error, "duhamel_residual_integral": integ,
                             "analytic_majorant": float(majorant),
                             "error_over_a2" if centered else "error_over_a": error/(a*a if centered else a),
                             "max_moving_derivative_norm": max_derivative,
                             "transport_norm": norm(actual, w), "ode": ode,
                             "lift_endpoint_range": [float(endpoint.min()), float(endpoint.max())]})
    shifts = []
    for a in [0.37, 0.2, 0.1]:
        for y in [0.63, -0.63, 0.731]:
            sample = np.linspace(-R, R, 1001)
            actual = target.geometric_phase(sample, a, y)
            expected = np.exp(-1j*y*sample)
            error = float(np.max(abs(actual-expected)))
            endpoints = target.geometric_phase(np.array([-np.pi/a, np.pi/a]), a, y)
            trace_error = float(abs(endpoints[1]-endpoints[0]))
            check(f"rounded_translation_bound_a_{a}_y_{y}", error, a*R/2)
            check(f"actual_integer_translation_trace_a_{a}_y_{y}", trace_error, 0, slack=2e-12)
            shifts.append({"a": a, "y": y, "uniform_patch_phase_error": error,
                           "bound": a*R/2, "endpoint_trace_error": trace_error})
    # A mixed finite word: W(.23) A(.31) T(.57) W(-.19).
    words = []
    sleft, sright, etime, distance = 0.23, -0.19, 0.31, 0.57
    MW = (R+m/v)*np.exp(v*(abs(sleft)+abs(sright)))-m/v
    qw, ww = quadrature(MW, 1000)
    def limit_inner(x):
        return np.exp(-1j*etime*E(x)-1j*distance*x)*line(x, sright, m, v, fpair)[0]
    # Outer line transport only needs the values of its inner packet.
    Fw = qw*np.cosh(v*sleft)+E(qw)*np.sinh(v*sleft)/v
    EwF = E(qw)*np.cosh(v*sleft)+v*qw*np.sinh(v*sleft)
    line_word = np.sqrt(EwF/E(qw))*limit_inner(Fw)
    K = bnorm+(v*v*MW*abs(etime)+E(MW)*abs(distance))*fnorm
    DW = K/m+v*fnorm/(4*m)
    c0W = v*v*MW**4/(24*m)
    c1W = v*v*MW**3/(6*m)+v**4*MW**5/(24*m**3)
    for a in [0.2, 0.1, 0.05]:
        def lattice_inner(x):
            inside = target.transport(x, sright, a, m, v, f, centered=False)[0]
            raw_energy = np.sqrt(m*m+4*v*v*np.sin(a*x/2)**2/a**2)
            return np.exp(-1j*etime*raw_energy)*target.geometric_phase(x, a, distance)*inside
        value = target.transport(qw, sleft, a, m, v, lattice_inner, centered=False)[0]
        error = norm(value-line_word, ww)
        bound = (abs(sleft)+abs(sright))*(a*a*(c0W*DW+c1W*fnorm/2)+a*E(MW)*fnorm/2)
        bound += abs(etime)*a*a*c0W*fnorm+a*MW*fnorm/2
        check(f"mixed_finite_word_a_{a}", error, bound)
        words.append({"a": a, "error": error, "analytic_majorant": float(bound)})
    # Two-particle antisymmetric tensor: direct 2D integration versus Gram determinants.
    fock = []
    qf, wf = quadrature(3.0, 2000)
    pair1, pair2 = packet(center=-0.5, width=0.26, eta=0.23), packet(center=0.5, width=0.26, eta=-0.32)
    sf = 0.27
    l1, _ = line(qf, sf, m, v, pair1)
    l2, _ = line(qf, sf, m, v, pair2)
    line_tensor = (l1[:, None]*l2[None, :]-l2[:, None]*l1[None, :])/np.sqrt(2)
    w2 = wf[:, None]*wf[None, :]
    check("fock_line_unitarity", abs(np.sum(w2*abs(line_tensor)**2)-1), 0, slack=2e-10)
    for a in [0.2, 0.1]:
        z1 = target.transport(qf, sf, a, m, v, lambda x: pair1(x)[0])[0]
        z2 = target.transport(qf, sf, a, m, v, lambda x: pair2(x)[0])[0]
        lattice_tensor = (z1[:, None]*z2[None, :]-z2[:, None]*z1[None, :])/np.sqrt(2)
        check(f"fock_actual_unitarity_a_{a}", abs(np.sum(w2*abs(lattice_tensor)**2)-1), 0, slack=2e-10)
        direct_squared = float(np.sum(w2*abs(lattice_tensor-line_tensor)**2))
        def gram(xs, ys):
            return np.array([[np.dot(wf, x.conj()*y) for y in ys] for x in xs])
        gram_squared = float(np.real(np.linalg.det(gram([z1,z2],[z1,z2]))+
                                     np.linalg.det(gram([l1,l2],[l1,l2]))-
                                     2*np.linalg.det(gram([z1,z2],[l1,l2]))))
        check(f"fock_Gram_vs_direct_a_{a}", abs(direct_squared-gram_squared), 0)
        tensor_error = np.sqrt(max(direct_squared, 0))
        epsilon_sum = norm(z1-l1, wf)+norm(z2-l2, wf)
        check(f"fock_two_particle_telescoping_a_{a}", tensor_error, epsilon_sum)
        fock.append({"a": a, "direct_error_squared": direct_squared,
                     "gram_error_squared": gram_squared, "two_particle_error": float(tensor_error),
                     "sum_one_particle_errors": epsilon_sum,
                     "line_tensor_norm_squared": float(np.sum(w2*abs(line_tensor)**2)),
                     "lattice_tensor_norm_squared": float(np.sum(w2*abs(lattice_tensor)**2))})
    result = {"candidate": str(Path(args.candidate).resolve()),
              "candidate_sha256": hashlib.sha256(Path(args.candidate).read_bytes()).hexdigest(),
              "fixture": {"m":m,"v":v,"R":R,"S":S,"M":float(M),"norm_f":fnorm,"norm_bf":bnorm,"D_f":D},
              "packet_rows": rows, "translation_rows": shifts, "word_rows": words, "fock_rows": fock,
              "predicates": predicates,
              "limits": "Non-interval quadrature and ODE diagnostics. Fock example is finite-sector only; analytic proofs carry infinite-space quantifiers."}
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0 if all(p["ok"] for p in predicates) else 1


if __name__ == "__main__":
    raise SystemExit(main())

