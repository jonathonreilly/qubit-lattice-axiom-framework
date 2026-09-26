"""Author controls of initial formation and energy injection in the supplied model.

The cubic source calculation enumerates actual allowed local moves from ice
fields. The full square uses an exact finite Hamiltonian eigenvector and all
birth channels, including the anticommutator energy contribution.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import itertools
import json
import math
from fractions import Fraction
import numpy as np

HERE = Path(__file__).resolve().parent


def identity(path):
    path = Path(path).resolve()
    b = path.read_bytes()
    return {"path": str(path), "bytes": len(b), "sha256": sha256(b).hexdigest()}


def graph(d, side):
    vertices = list(itertools.product(range(side), repeat=d))
    lookup = {x: i for i, x in enumerate(vertices)}
    edges = []
    for x in vertices:
        for mu in range(d):
            y = list(x); y[mu] = (y[mu]+1) % side
            edges.append((lookup[x], lookup[tuple(y)], mu))
    parity = [sum(x) % 2 for x in vertices]
    return vertices, edges, parity


def field_charge(word, edges, parity):
    # 2*divergence, followed by background +1 on A.
    dv = [0]*len(parity)
    for e, (x, y, _) in enumerate(edges):
        z = 1 if (word >> e) & 1 else -1
        dv[x] += z; dv[y] -= z
    assert all(v % 2 == 0 for v in dv)
    return tuple(v//2+int(parity[x] == 0) for x, v in enumerate(dv))


def source_control(d, side=6):
    vertices, edges, parity = graph(d, side)
    volume = len(vertices)
    adjacent = [[] for _ in vertices]
    for e, (x, y, _) in enumerate(edges):
        adjacent[x].append((e, y)); adjacent[y].append((e, x))
    # Staggered xy circulation and constant remaining directions form exact ice.
    word = 0
    for e, (x, _, mu) in enumerate(edges):
        z = 1
        if d >= 2 and mu < 2:
            z = (-1)**sum(vertices[x]) * (1 if mu == 0 else -1)
        if z == 1:
            word |= 1 << e
    initial_q = tuple(int(p == 0) for p in parity)
    assert field_charge(word, edges, parity) == initial_q
    words = [word]
    if d >= 2:
        lookup = {x: i for i, x in enumerate(vertices)}
        zero = (0,)*d
        ex = (1,)+(0,)*(d-1)
        ey = (0,1)+(0,)*(d-2)
        face_edges = [d*lookup[zero], d*lookup[ex]+1,
                      d*lookup[ey], d*lookup[zero]+1]
        other = word
        for e in face_edges:
            other ^= 1 << e
        assert field_charge(other, edges, parity) == initial_q
        words.append(other)

    source_vectors = []
    r_values = {}
    for initial_word in words:
        source = {}
        eligible_hops = 0
        for e, (x, y, _) in enumerate(edges):
            a, b = (x, y) if parity[x] == 0 else (y, x)
            # Positive A-to-B hop lowers outward A flux by one.
            delta = -1 if a == x else 1
            bit = (initial_word >> e) & 1
            if bit+delta not in (0, 1):
                continue
            eligible_hops += 1
            moved = initial_word ^ (1 << e)
            q = list(initial_q); q[a] = 0; q[b] = 1
            assert field_charge(moved, edges, parity) == tuple(q)
            for f, other_b in adjacent[a]:
                if other_b == b:
                    continue
                u, v, _ = edges[f]
                oldbit = (moved >> f) & 1
                change = 1 if oldbit == 0 else -1
                qa = change if a == u else -change
                after = list(q); after[a] = qa; after[other_b] = -qa
                final_word = moved ^ (1 << f)
                assert field_charge(final_word, edges, parity) == tuple(after)
                # Bond f is the observed jump label; coherent charge refinements
                # have orthogonal output charges and are represented together.
                key = (f, final_word, tuple(after))
                source[key] = source.get(key, 0)+1
                r = sum((z-int(parity[i] == 0))**2 for i, z in enumerate(after))//2
                assert r in (1, 3)
                assert sum(z != 0 for i, z in enumerate(after) if parity[i] == 1) == 2
                r_values[key] = r
        assert eligible_hops == d*volume//2
        source_vectors.append(source)

    size = len(words)
    gram = np.zeros((size, size), dtype=np.int64)
    power = np.zeros_like(gram)
    split = []
    for i, a in enumerate(source_vectors):
        counts = {r: sum(amplitude**2 for key, amplitude in a.items() if r_values[key] == r) for r in (1,3)}
        split.append(counts)
        for j, b in enumerate(source_vectors):
            gram[i,j] = sum(amplitude*b.get(key,0) for key, amplitude in a.items())
            power[i,j] = sum(amplitude*b.get(key,0)*r_values[key] for key, amplitude in a.items())
    m = d*volume//2
    assert np.array_equal(gram, m*(2*d-1)*np.eye(size, dtype=np.int64))
    assert np.array_equal(power, m*(4*d-3)*np.eye(size, dtype=np.int64))
    assert all(c[1] == m*d and c[3] == m*(d-1) for c in split)
    conditional_moments=[]
    for c in split:
        total=c[1]+c[3]
        mean=Fraction(c[1]+3*c[3],total)
        variance=Fraction(c[1]+9*c[3],total)-mean**2
        assert variance == Fraction(4*d*(d-1),(2*d-1)**2)
        conditional_moments.append({'mean_penalty':str(mean),'variance_penalty':str(variance)})
    return {"dimension":d,"side":side,"volume":volume,"tested_ice_vectors":size,
            "eligible_hops":m,"source_rate_gram":gram.tolist(),
            "star_energy_source_gram":power.tolist(),"penalty_resolved_source_counts":split,
            "star_energy_per_birth_over_Delta":(4*d-3)/(2*d-1),
            "star_penalty_variance_per_birth_over_Delta2":4*d*(d-1)/(2*d-1)**2,
            "exact_conditional_penalty_moments":conditional_moments,
            "sublattice_energy_per_birth_over_Delta":2,
            "scope":"Finite exact source controls; the all-ice identity follows from the local injectivity/counting proof."}


def full_square():
    edges = [(i,(i+1)%4,0) for i in range(4)]
    parity = [0,1,0,1]
    states = []
    qs = []
    for word in range(16):
        q = field_charge(word, edges, parity)
        if all(z in (-1,0,1) for z in q):
            states.append(word);qs.append(q)
    lookup = {w:i for i,w in enumerate(states)}
    dim = len(states)
    assert dim == 9
    hop = np.zeros((dim,dim))
    birth = [np.zeros_like(hop) for _ in edges]
    for col,(word,q) in enumerate(zip(states,qs)):
        for e,(x,y,_) in enumerate(edges):
            target = word ^ (1 << e)
            if target not in lookup:
                continue
            row = lookup[target]; after = qs[row]
            if (q[x] != 0 and q[y] == 0 and after[x] == 0 and after[y] == q[x]) or (q[y] != 0 and q[x] == 0 and after[y] == 0 and after[x] == q[y]):
                hop[row,col] = -1
            if q[x] == q[y] == 0 and after[x] == -after[y] and abs(after[x]) == 1:
                birth[e][row,col] = 1
    assert np.array_equal(hop,hop.T)
    loss = sum(j.T@j for j in birth)
    n = np.array([sum(z != 0 for z in q) for q in qs])
    number = np.diag(n)
    assert np.array_equal(number@hop, hop@number)
    assert all(np.array_equal(number@j-j@number,2*j) for j in birth)
    assert np.array_equal(number@loss,loss@number)
    original = np.flatnonzero(n == 2)
    penalties = {
        'sublattice':np.array([sum(z != 0 for i,z in enumerate(q) if parity[i] == 1) for q in qs]),
        'star':np.array([sum((z-int(parity[i]==0))**2 for i,z in enumerate(q))/2 for q in qs])}
    cases=[]
    for name,r in penalties.items():
        for epsilon in (.16,.08,.04,.02,.01):
            delta = 1/(2*epsilon**4)
            t = delta*epsilon
            ham = delta*np.diag(r)+t*hop
            ev,vec = np.linalg.eigh(ham[np.ix_(original,original)])
            psi = np.zeros(dim);psi[original]=vec[:,0]
            energy = float(psi@ham@psi)
            rate = float(psi@loss@psi)
            dissipator_energy = sum(j.T@ham@j-.5*(j.T@j@ham+ham@j.T@j) for j in birth)
            power = float(psi@dissipator_energy@psi)
            gain_minus_ground = sum(float((j@psi)@(ham-energy*np.eye(dim))@(j@psi)) for j in birth)
            assert abs(power-gain_minus_ground) < 1e-7*max(1,abs(power))
            expected = 2 if name == 'sublattice' else 1
            offsets=[]
            for mu_over_delta in (-1.,-.5,0.,.75):
                mu=mu_over_delta*delta
                shifted=ham+mu*number
                shifted_source=sum(j.T@shifted@j-.5*(j.T@j@shifted+shifted@j.T@j) for j in birth)
                shifted_power=float(psi@shifted_source@psi)
                error=abs(shifted_power-(power+2*mu*rate))
                assert error < 1e-7*max(1,abs(power))
                offsets.append({'mu_over_Delta':mu_over_delta,'shifted_power_over_beta':shifted_power,
                                'offset_identity_error':error})
            cases.append({'penalty':name,'epsilon':epsilon,'Delta':delta,'ground_energy':energy,
                          'birth_rate_over_beta':rate,'rate_over_beta_epsilon2':rate/epsilon**2,
                          'power_over_beta':power,'power_over_beta_Delta_epsilon2':power/(delta*epsilon**2),
                          'power_over_Delta_birth_rate':power/(delta*rate),
                          'leading_energy_per_birth_over_Delta':expected,
                          'full_dissipator_vs_eigenstate_formula_difference':abs(power-gain_minus_ground),
                          'ground_eigenvector_residual':float(np.linalg.norm(ham@psi-energy*psi))})
            cases[-1]['number_energy_offsets']=offsets
    return {'dimension':dim,'original_number_dimension':len(original),'cases':cases,
            'number_commutes_H_and_loss_exactly':True,'every_birth_raises_number_by_two_exactly':True,
            'scope':'Exact finite matrices with floating eigenvectors. The square is d=1 coordination and has one loop; cubic coefficient checks are separate.'}


def main():
    out={'created_utc':datetime.now(timezone.utc).isoformat(),'script':identity(__file__),
         'cubic_source':[source_control(d) for d in (1,2,3)],'full_square':full_square(),
         'status':'Initial-source tradeoff in the supplied prepared model, not a no-go for record formation or an integrated heating theorem.'}
    data=json.dumps(out,indent=2)+'\n';(HERE/'RECORD_FORMATION_ENERGY_RESULTS.json').write_text(data);print(data,end='')


if __name__ == '__main__':
    main()
