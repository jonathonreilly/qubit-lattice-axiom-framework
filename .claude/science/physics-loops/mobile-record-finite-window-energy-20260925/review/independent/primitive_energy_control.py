"""Independent exact-small-graph control of post-record energy measurements.

Physical graph: a two-leaf A-centred star, disjoint from a single A--B edge.
All legal charge/electric words are retained. The full physical dimension is
12 for every integer spin S >= 1. Original resolved and coherent jumps are
built from local creation; no author module, data or runner is imported.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib
import json
import math
import time
import numpy as np
from scipy.linalg import expm


def component(leaves, spin):
    words = []
    for charges in product((-1, 0, 1), repeat=leaves+1):
        if sum(charges) == 1:
            fields = tuple(-q for q in charges[1:])
            if max(map(abs, fields), default=0) <= spin:
                assert sum(fields) == charges[0]-1
                assert all(-e == q for e, q in zip(fields, charges[1:]))
                words.append((charges, fields))
    index = {word: n for n, word in enumerate(words)}
    dim = len(words)
    F = np.zeros((dim, dim))
    jumps = {(b, sign): np.zeros((dim, dim))
             for b in range(leaves) for sign in (-1, 1)}
    dinf, dspin, D, number, penalty = [np.zeros(dim) for _ in range(5)]
    resource = spin*(spin+1)
    for col, (charges, fields) in enumerate(words):
        eta = charges[0]
        number[col] = sum(q != 0 for q in charges)
        penalty[col] = int(eta == 0)
        for b in range(leaves):
            if eta != 0 and charges[b+1] == 0:
                e = fields[b]
                dinf[col] += 1
                dspin[col] += 1-e*(e-eta)/resource
                D[col] += e*(e-eta)
                qnew, enew = list(charges), list(fields)
                qnew[0], qnew[b+1], enew[b] = 0, eta, e-eta
                if abs(enew[b]) <= spin:
                    row = index[(tuple(qnew), tuple(enew))]
                    F[row, col] += math.sqrt(1-e*(e-eta)/resource)
            if eta == 0 and charges[b+1] == 0:
                for sign in (-1, 1):
                    e = fields[b]
                    qnew, enew = list(charges), list(fields)
                    qnew[0], qnew[b+1], enew[b] = sign, -sign, e+sign
                    if abs(enew[b]) <= spin:
                        row = index[(tuple(qnew), tuple(enew))]
                        jumps[b, sign][row, col] += math.sqrt(1-e*(e+sign)/resource)
    compensation = F.T@F - np.diag(dspin) + np.diag(dinf)
    assert np.array_equal(compensation, F.T@F)
    assert np.array_equal(np.diag(F.T@F), dspin)
    initial = np.zeros(dim)
    initial[index[((1,)+(0,)*leaves, (0,)*leaves)]] = 1
    return dict(words=words, F=F, jumps=jumps, C=compensation,
                W=np.diag(penalty), D=np.diag(D), N=np.diag(number), initial=initial)


def nonzero_entries(matrix):
    return [[int(i), int(j), float(matrix[i, j])] for i, j in zip(*np.nonzero(matrix))]


def main():
    tic = time.perf_counter()
    moment_rows, layer_rows, structure_rows = [], [], []
    primitive = None
    delta = K = kappa = 1.
    left, right, readout = .1, .3, .4
    target_probability = (math.exp(-4*kappa*left)-math.exp(-4*kappa*right))/4
    largest_structure_residual = 0.
    for spin in (1, 2, 4, 8, 16, 32):
        c = spin*(spin+1)
        epsilon = math.sqrt(delta/(K*c))
        birth, spectator = component(2, spin), component(1, spin)
        d1, d2 = len(birth['words']), len(spectator['words'])
        I1, I2 = np.eye(d1), np.eye(d2)
        F1, F2 = np.kron(birth['F'], I2), np.kron(I1, spectator['F'])
        W = np.kron(birth['W'], I2)+np.kron(I1, spectator['W'])
        N = np.kron(birth['N'], I2)+np.kron(I1, spectator['N'])
        C = np.kron(birth['C'], I2)+np.kron(I1, spectator['C'])
        T = -F1-F1.T-F2-F2.T
        Jraw = [np.kron(j, I2) for j in birth['jumps'].values()]
        Jraw += [np.kron(I1, j) for j in spectator['jumps'].values()]
        coherent = [Jraw[0]+Jraw[1], Jraw[2]+Jraw[3], Jraw[4]+Jraw[5]]
        pidx = np.flatnonzero(np.diag(W) == 0)
        P = np.eye(d1*d2)[:, pidx]
        Pi1, Pi2 = np.diag(np.diag(W) == 1), np.diag(np.diag(W) == 2)
        A, C0 = Pi1@T@P, P.T@C@P
        M = A.T@A
        Z = Pi2@T@Pi1@T@P
        H4 = M@M-(M@C0+C0@M)/2+A.T@C@A-Z.T@Z/2
        fullD = np.kron(birth['D'], I2)+np.kron(I1, spectator['D'])
        residuals = [np.linalg.norm(C@W-W@C), np.linalg.norm(C@N-N@C),
                     np.linalg.norm(T@N-N@T), np.linalg.norm(C0-M),
                     np.linalg.norm(H4), np.linalg.norm(P.T@fullD@P)]
        for j in Jraw+coherent:
            residuals += [np.linalg.norm(W@j-j@W+j), np.linalg.norm(j@P),
                          np.linalg.norm(N@j-j@N-2*j)]
        assert max(residuals) < 1e-13
        largest_structure_residual = max(largest_structure_residual, max(residuals))
        assert all(np.count_nonzero(j) == 0 for j in spectator['jumps'].values())
        u1, u2 = birth['initial'], spectator['initial']
        chosen = birth['jumps'][(0, 1)]
        target_output = chosen@birth['F']@u1
        assert np.linalg.norm(target_output) == 1
        assert np.linalg.norm(birth['C']@target_output) == 0
        assert np.linalg.norm(birth['W']@target_output) == 0
        assert np.linalg.norm((birth['F']+birth['F'].T)@target_output) == 0
        H1 = delta*epsilon**-4*(birth['W']-epsilon*(birth['F']+birth['F'].T)+epsilon**2*birth['C'])
        H2 = delta*epsilon**-4*(spectator['W']-epsilon*(spectator['F']+spectator['F'].T)+epsilon**2*spectator['C'])
        Gamma1 = kappa*epsilon**-2*sum(j.T@j for j in birth['jumps'].values())
        generator = -1j*H1-Gamma1/2
        def noevent(t):
            return expm(generator*t)@u1
        va, vb = noevent(left), noevent(right)
        actual_probability = float((np.vdot(va, va)-np.vdot(vb, vb)).real/4)
        assert actual_probability > 0
        # Primitive symmetry gives each resolved mark one quarter of total loss.
        symmetry_residual = 0.
        for t in (left, .17, right):
            state = noevent(t)
            rates = [float(kappa*epsilon**-2*np.linalg.norm(j@state)**2) for j in birth['jumps'].values()]
            symmetry_residual = max(symmetry_residual, max(rates)-min(rates))
            jumped = chosen@state
            symmetry_residual = max(symmetry_residual, np.linalg.norm(jumped-target_output*np.vdot(target_output, jumped)))
        assert symmetry_residual < 1e-10
        # Event probability is computed from survival in the primitive six-state
        # no-event matrix. The event-conditioned first component is exactly dark.
        spectator_state = expm(-1j*H2*readout)@u2
        spectator_state /= np.linalg.norm(spectator_state)
        output = np.kron(target_output, spectator_state)
        H = np.kron(H1, I2)+np.kron(I1, H2)
        dimensionless = W+epsilon*T+epsilon**2*C
        eig, vec = np.linalg.eigh(dimensionless)
        weights = abs(vec.conj().T@output)**2
        predicted_high = delta*epsilon**-4*(1+epsilon**2)
        numerical_high_weight = float(sum(w for x, w in zip(eig, weights) if abs(x-(1+epsilon**2)) < 1e-8))
        predicted_weight = Fraction(1, c+1)
        mean = float(np.vdot(output, H@output).real)
        second = float(np.vdot(H@output, H@output).real)
        variance = second-mean**2
        expected_mean, expected_second, expected_variance = c, c*c*(c+1), c**3
        relative_residual = max(abs(mean-expected_mean)/max(1, expected_mean),
                                abs(second-expected_second)/max(1, expected_second),
                                abs(variance-expected_variance)/max(1, expected_variance))
        assert relative_residual < 1e-8
        assert abs(numerical_high_weight-float(predicted_weight)) < 1e-10
        tests = {}
        for name, f in [('resolvent_real', lambda x: 1/(1+x*x)),
                        ('gaussian', lambda x: math.exp(-x*x)),
                        ('characteristic', lambda x: complex(math.cos(.37*x), math.sin(.37*x)))]:
            value = (1-float(predicted_weight))*f(0)+float(predicted_weight)*f(predicted_high)
            error = abs(value-f(0))
            assert error <= 2*float(predicted_weight)+1e-14
            tests[name] = {'value': [float(complex(value).real), float(complex(value).imag)],
                           'limit': [float(complex(f(0)).real), float(complex(f(0)).imag)], 'error': error}
        moment_rows.append({'spin':spin,'epsilon':epsilon,'resource_C':c,
            'finite_bin':[left,right],'readout':readout,'actual_resolved_event_probability':actual_probability,
            'limiting_event_probability':target_probability,'probability_difference':actual_probability-target_probability,
            'exact_energy_law':{'low_energy':0,'high_energy':c*(c+1),
                                'high_probability_numerator':1,'high_probability_denominator':c+1},
            'numerical_high_weight':numerical_high_weight,'mean':mean,'exact_mean':expected_mean,
            'second_moment':second,'exact_second_moment':expected_second,
            'variance':variance,'exact_variance':expected_variance,
            'moment_max_relative_residual':relative_residual,
            'total_variation_to_delta_zero':float(predicted_weight),'bounded_tests':tests})
        structure_rows.append({'spin':spin,'dimension':d1*d2,'P_dimension':len(pidx),
            'resolved_channel_count_including_zero_channels':len(Jraw),
            'coherent_channel_count_including_zero_channels':len(coherent),
            'maximum_structural_residual':max(residuals),'first_channel_symmetry_residual':float(symmetry_residual),
            'spectator_original_jumps_identically_zero':True})
        for phase in (0., math.pi/2, math.pi, 2*math.pi):
            t = phase*epsilon**4/delta
            amplitude = chosen@noevent(t)
            rate = float(kappa*epsilon**-2*np.linalg.norm(amplitude)**2)
            predicted_layer_rate = kappa*abs(1-complex(math.cos(phase),-math.sin(phase)))**2
            layer_rows.append({'spin':spin,'phase':phase,'microscopic_time':t,
                               'actual_selected_intensity':rate,'boundary_layer_limit':predicted_layer_rate,
                               'effective_initial_intensity':kappa})
        if primitive is None:
            primitive = {'birth_component_words':birth['words'],'spectator_component_words':spectator['words'],
                'birth_F':nonzero_entries(birth['F']),'spectator_F':nonzero_entries(spectator['F']),
                'birth_resolved_jumps':{str(key):nonzero_entries(j) for key,j in birth['jumps'].items()},
                'spectator_resolved_jumps':{str(key):nonzero_entries(j) for key,j in spectator['jumps'].items()},
                'global_W_diagonal':np.diag(W).tolist(),'global_N_diagonal':np.diag(N).tolist(),
                'global_C':nonzero_entries(C),'global_T':nonzero_entries(T),
                'global_P_indices':pidx.tolist(),'H2_effective':(C0-M).tolist(),'H4_effective':H4.tolist(),
                'full_P_gated_D':(P.T@fullD@P).tolist()}
    return {'scope':__doc__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'parameters':{'delta':delta,'K':K,'kappa':kappa,'spin_scaling':'epsilon^2 S(S+1)=delta/K'},
        'primitive_data':primitive,'structure_rows':structure_rows,'energy_and_event_rows':moment_rows,
        'boundary_layer_rows':layer_rows,'largest_structure_residual':largest_structure_residual,
        'separate_abstract_operator_examples':[
            {'label':'moving atom, not a physical rotor control','operators':'A_n=(1/n)I on C',
             'state':'1','weak_limit':'delta_0','total_variation_distance_to_limit':1,
             'CDF_at_zero':0,'limit_CDF_at_zero':1},
            {'label':'vanishing lower atom, not a physical rotor control','operator':'diag(-1,0)',
             'state':'diag(1/n,1-1/n)','weak_limit':'delta_0','support_infimum_for_each_n':-1,
             'support_infimum_of_limit':0}],
        'author_sources_read_or_imported':[],'elapsed_seconds':time.perf_counter()-tic}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, allow_nan=False))
