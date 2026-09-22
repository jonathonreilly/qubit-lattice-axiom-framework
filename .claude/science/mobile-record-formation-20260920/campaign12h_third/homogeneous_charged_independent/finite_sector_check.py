"""Independently assemble complete physical square sectors and low blocks.

The four square vertices retain their cubic outside occupation environment.
Outside links and sites are frozen.  Only internal square hops are used, so the
test checks actual denominators, folded terms, finite-spin weights and charge
transport without claiming to diagonalize the full cubic torus.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product, combinations
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent


def physical_sector(spin, ambient_d, background):
    cs = spin*(spin+1)
    alpha = 2*ambient_d-1
    states = []
    for electric in product(range(-spin, spin+1), repeat=4):
        charge = tuple(background[x]+electric[x]-electric[(x-1)%4] for x in range(4))
        if all(abs(x) <= 1 for x in charge) and sum(x*x for x in charge) == 2:
            states.append((electric, charge))
    index = {s:i for i,s in enumerate(states)}
    count = len(states)
    hop = sp.zeros(count)
    energies = []
    for col, (electric, charge) in enumerate(states):
        occ = [x*x for x in charge]
        energy = sum((occ[i]+occ[(i+1)%4]-1)**2 for i in range(4))
        energy += (2*ambient_d-2)*sum((1-occ[i])**2 if i%2 == 0 else occ[i]**2 for i in range(4))
        energies.append(sp.Rational(energy,2))
        for edge in range(4):
            tail, head = edge, (edge+1)%4
            for source, dest, sign in ((tail,head,1),(head,tail,-1)):
                q = charge[source]
                if q == 0 or charge[dest] != 0:
                    continue
                shift = -sign*q
                m = electric[edge]
                if not -spin <= m+shift <= spin:
                    continue
                new_e = list(electric);new_e[edge] += shift
                new_q = list(charge);new_q[source] = 0;new_q[dest] = q
                target = (tuple(new_e),tuple(new_q))
                assert target in index
                factor = sp.sqrt(1-sp.Rational(m*(m+shift),cs))
                hop[index[target],col] -= factor
    assert hop == hop.T
    low = [i for i,s in enumerate(states) if energies[i] == 0]
    assert all(tuple(q*q for q in states[i][1]) == (1,0,1,0) for i in low)
    assert hop.extract(low,low) == sp.zeros(len(low))
    resolvent = sp.diag(*[1/e if e else 0 for e in energies])
    h2 = sp.simplify(-(hop*resolvent*hop).extract(low,low))
    ar = (hop*resolvent*hop).extract(low,low)
    ar2 = (hop*resolvent**2*hop).extract(low,low)
    irreducible = -(hop*resolvent*hop*resolvent*hop*resolvent*hop).extract(low,low)
    folded = (ar*ar2+ar2*ar)/2
    h4 = sp.simplify(irreducible+folded)

    low_index = {states[i]:j for j,i in enumerate(low)}
    ring = sp.zeros(len(low))
    diag4 = []
    expected2 = []
    for source_col, state_index in enumerate(low):
        electric, charge = states[state_index]
        ae = []
        for edge in range(4):
            occupied = edge if edge%2 == 0 else (edge+1)%4
            traversal = 1 if occupied == edge else -1
            q = charge[occupied]
            ae.append(1-sp.Rational(electric[edge]**2-traversal*q*electric[edge],cs))
        expected2.append(-sum(ae)/alpha)
        meeting = sum(ae[e]*ae[f] for e,f in combinations(range(4),2)
                      if (e-f)%4 in (1,3))
        opposite = ae[0]*ae[2]+ae[1]*ae[3]
        diag4.append((sum(x*x for x in ae)+2*meeting-sp.Rational(4,2*alpha-2)*opposite)/alpha**3)
        q, r = charge[0], charge[2]
        shifts = [-q,-q,-r,-r]
        new_e = tuple(m+s for m,s in zip(electric,shifts))
        if all(-spin <= m <= spin for m in new_e):
            factor = sp.prod(sp.sqrt(1-sp.Rational(m*(m+s),cs)) for m,s in zip(electric,shifts))
            target = (new_e,(r,0,q,0))
            assert target in low_index
            ring[low_index[target],source_col] += factor
    expected4 = sp.diag(*diag4)-sp.Rational(2,alpha**2*(alpha-1))*(ring+ring.T)
    assert sp.simplify(h2-sp.diag(*expected2)) == sp.zeros(len(low))
    assert sp.simplify(h4-expected4) == sp.zeros(len(low))

    origin = low_index[((0,0,0,0),background)]
    q, r = background[0],background[2]
    target = ((-q,-q,-r,-r),(r,0,q,0))
    target_index = low_index[target]
    expected_entry = -sp.Rational(2 if q == r else 4,alpha**2*(alpha-1))
    assert h4[target_index,origin] == expected_entry
    if q != r:
        assert ring == ring.T
    result = {
        'spin':spin,'ambient_dimension':ambient_d,'fixed_outside_charge':list(background),
        'complete_physical_dimension':count,'code_dimension':len(low),
        'occupation_energy_levels':sorted(set(map(str,energies))),
        'single_hop_energy':alpha,'opposite_two_hop_energy':2*alpha-2,
        'h2_exact':[[str(x) for x in h2.row(i)] for i in range(len(low))],
        'h4_exact':[[str(x) for x in h4.row(i)] for i in range(len(low))],
        'selected_origin':{'E':[0]*4,'charge':list(background)},
        'selected_target':{'E':list(target[0]),'charge':list(target[1])},
        'selected_h4_entry':str(h4[target_index,origin]),
        'equal_oriented_routes_on_opposite_charge_sector':bool(ring == ring.T) if q != r else None,
        'diagonal_formula_and_all_offdiagonals_match':True,
        'folded_term_needed':bool(h4 != irreducible),
    }
    return result


def main():
    rows = [physical_sector(1,d,background) for d in (2,3)
            for background in ((1,0,1,0),(1,0,-1,0))]
    result={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'controls':rows,'method':'Exact SymPy complete constrained-sector matrices; no author code read/imported.',
            'scope':'Frozen cubic outside occupation/field; all legal internal square states and hopping channels. Full-torus combinatorics checked separately.'}
    data=json.dumps(result,indent=2)+'\n'
    p=HERE/'FINITE_SECTOR_RESULTS.json';assert not p.exists();p.write_text(data);print(data,end='')


if __name__ == '__main__':main()
