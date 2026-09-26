#!/usr/bin/env python3
"""Post-seal source/evidence comparisons, without importing the author checkers.

Reads endpoint configurations and only the CSV final count fields. Does not
read/execute the production simulator or assess event times, sampling or phases.
All output is confined to the --out directory, which must already exist.
"""
import argparse
import csv
from collections import Counter
import hashlib
import io
import json
from pathlib import Path
import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OWN = {'__name__': 'independent_library', '__file__': str(HERE/'independent_check.py')}
exec(compile((HERE/'independent_check.py').read_text(), str(HERE/'independent_check.py'), 'exec'), OWN)
MANIFEST = {}


def read(path, kind):
    raw = path.read_bytes()
    MANIFEST[str(path.resolve())] = {'path':str(path.resolve()), 'bytes':len(raw),
                                    'sha256':hashlib.sha256(raw).hexdigest(), 'use':kind}
    return raw


def load(path, kind):
    return json.loads(read(path,kind))


def decode(array):
    n = array.shape[0]
    return {x:(i+1,(int(a)//2+1)*(1 if int(a)%2 == 0 else -1))
            for i,(x,a) in enumerate(zip(OWN['vertices'](n),array.ravel())) if a >= 0}


def symbolic_configuration(n):
    # Build the claimed matching directly as a signed-axis array; the two holes
    # are specified geometrically, not obtained by a simulated history.
    a = np.empty((n,n,n),dtype=int)
    a[:] = (np.arange(n)%2)[:,None,None]
    a[:2,:2,:2] = -1
    for x,axis in [((1,0,0),1),((0,1,0),2),((0,0,1),0)]:
        a[x] = 2*axis
        a[OWN['shift'](x,axis,1,n)] = 2*axis+1
    return a


def fft_readout(array):
    n = array.shape[0]
    s = decode(array)
    field6 = OWN['parity_gauss'](s,n)
    # Independent FFT, applied to the integer field first; author uses direct
    # complex phase sums and constructs the longitudinal vector from q.
    f = np.array([field6[x] for x in OWN['vertices'](n)],dtype=float).reshape(n,n,n,3)/6
    fhat = np.fft.fftn(f,axes=(0,1,2))/np.sqrt(n**3)
    sigma = (-1.0)**np.indices((n,n,n)).sum(axis=0)
    qhat = np.fft.fftn(-sigma*(array < 0))/np.sqrt(n**3)
    result = []
    for mode in [(1,0,0),(1,2,0),(1,1,1)]:
        d = 1-np.exp(-2j*np.pi*np.array(mode)/n)
        den = float(np.vdot(d,d).real)
        b = fhat[mode]
        q = qhat[mode]
        projection = np.outer(d.conjugate(),d)/den
        assert np.max(abs(projection-projection.conjugate().T)) < 1e-14
        assert np.max(abs(projection@projection-projection)) < 1e-14
        longitudinal = projection@b
        power = float(np.vdot(longitudinal,longitudinal).real)
        holes = int(np.sum(array < 0))
        bound = holes**2/(n**3*den)
        residual = float(abs(d@b-q))
        assert residual < 2e-12 and power <= bound+2e-13
        assert abs(power-abs(q)**2/den) < 2e-13
        result.append({'N':n,'mode':list(mode),'vacancies':holes,'longitudinal_power':power,
                       'bound':bound,'divergence_residual':residual})
    return s,result


def content_activity(s,n,rates,all_identity_channels=False):
    original = [len(OWN['births'](s,n)),len(OWN['translations'](s,n)),len(OWN['cube_exits'](s,n))]
    enabled = original[:]
    first = None
    for family,count,rate in zip(['birth','translation','original_cube'],original,rates[:3]):
        if count and rate > 0 and first is None:
            first = {'family':family,'count':count,'positive_rate_parameter':rate}
    accepted = identity = content_changes = 0
    first_identity = first_parallel = None
    if all_identity_channels or (first is None and rates[3] > 0):
        for edges in OWN['channels'](n):
            target = OWN['swap'](s,edges)
            if not OWN['valid'](target,n):
                continue
            accepted += 1
            if target != s:
                identity += 1
                if first_identity is None:
                    first_identity = edges
            if OWN['content'](target) != OWN['content'](s):
                content_changes += 1
                if first_parallel is None:
                    first_parallel = edges
                if not all_identity_channels:
                    break
        if first is None and content_changes and rates[3] > 0:
            first = {'family':'parallel_swaps','edges':first_parallel,'positive_rate_parameter':rates[3]}
    enabled.append(content_changes)
    return {'original_channels':original,'positive_content_activity_witness':first,
            'parallel_channels_fully_enumerated':all_identity_channels,
            'accepted_parallel_attempts':accepted if all_identity_channels else None,
            'identity_changing_parallel_attempts':identity if all_identity_channels else None,
            'content_changing_parallel_attempts':content_changes if all_identity_channels else None,
            'first_identity_channel':first_identity if all_identity_channels else None}


def run():
    seal = load(HERE/'PRE_COMPARISON_SEAL.json','pre-comparison independent seal')
    for row in seal['artifacts']:
        assert hashlib.sha256((HERE/row['path']).read_bytes()).hexdigest() == row['sha256']
    expected = {
        'PAIRED_RECORD_PERIODIC_JAM_AND_ESCAPE.md':'cf03eaff8ea4effc674881e5807fa3449b5211a487308360b0f0e448f19a0bdd',
        'PAIRED_RECORD_PARITY_AND_RESIDUAL_VACANCIES.md':'fe6f9a4f71bdeac7f971b233ce6def6ef918bf29476ea4e48641a881f2ee8257',
        'paired_record_periodic_check.py':'51a31337880a4613ebfc2981100f821d5410bc8299c178c117141e52aa545e05',
        'paired_record_parity_check.py':'30e503d581e77469a83b4be031aa9c101379d8cc80f80c3b281e6b395e6b64ba'}
    for name,digest in expected.items():
        assert hashlib.sha256(read(ROOT/name,'complete reviewed source')).hexdigest() == digest
    periodic = load(ROOT/'PAIRED_RECORD_PERIODIC_RESULTS.json','author recorded exact-support output')
    periodic_log = [json.loads(s) for s in read(ROOT/'PAIRED_RECORD_PERIODIC_RUN.log','complete author log').decode().splitlines()]
    assert periodic_log[:-1] == periodic['rows']
    assert periodic_log[-1]['groups'] == 7 and periodic_log[-1]['all_pass']
    assert all(row['pass'] for row in periodic['rows'])
    for name,digest in periodic['sources_sha256'].items():
        assert expected[name] == digest
    own = json.loads((HERE/'INDEPENDENT_RESULTS.json').read_text())
    for index,row in enumerate(own['periodic']):
        birth,cube = periodic['rows'][2*index:2*index+2]
        assert birth['side'] == row['N'] and list(birth['enabled_channels'].values()) == row['original_exits_birth_translation_cube']
        assert [cube['record_counts'][0],cube['record_counts'][-1]] == row['records_before_after']
        author_moves = sorted((x,y) for identity,x,y in periodic['witnesses'][index]['moved_id_displacements'])
        ours = sorted((x,y) for identity,x,y,a in row['moved_old_records'])
        assert author_moves == ours
    assert periodic['rows'][-1]['total_matchings'] == sum(own['cube_census']['matching_census'].values())
    assert periodic['rows'][-1]['one_each_matchings'] == own['cube_census']['one_dimer_per_axis']

    parity = load(ROOT/'PAIRED_RECORD_PARITY_RESULTS.json','author parity/Fourier output, every row compared')
    parity_log = load(ROOT/'PAIRED_RECORD_PARITY_RUN.log','complete author parity log')
    for name,digest in parity['sources_sha256'].items():
        assert expected[name] == digest
    assert parity_log['sources_sha256'] == parity['sources_sha256']
    rows, states, selected = [], [], []
    for row in parity['constructed']:
        n = row['N']
        s,computed = fft_readout(symbolic_configuration(n))
        assert OWN['counts'](s) == row['counts']
        assert sorted(set(OWN['vertices'](n))-set(s)) == [tuple(x) for x in row['vacancies']]
        rows += computed
    for phase in ['pilot','screen']:
        directory = ROOT/('paired_growth_'+phase)
        batch = load(directory/'BATCH_RESULTS.json','endpoint metadata only; kinetics not verified')
        for metadata in batch:
            stem,n = metadata['stem'],metadata['side']
            raw = read(directory/(stem+'.final.txt'),'complete endpoint state: reciprocity, counts, Gauss and Fourier only')
            array = np.loadtxt(io.StringIO(raw.decode()),dtype=int).reshape(n,n,n)
            assert n >= 4 and n % 2 == 0 and set(array.ravel()).issubset(set(range(-1,6)))
            s,computed = fft_readout(array)
            rows += computed
            c = OWN['counts'](s)
            holes = n**3-len(s)
            assert holes == n**3-metadata['occupied']
            # Authenticate the complete CSV, but use only its header and final
            # population/count row; no time series or kinetics claim is tested.
            raw_csv = read(directory/(stem+'.csv'),'hashed complete CSV; only final nx/ny/nz fields checked')
            lines = raw_csv.decode().splitlines()
            last = dict(zip(next(csv.reader([lines[0]])),next(csv.reader([lines[-1]]))))
            assert c == [int(last[k]) for k in ('nx','ny','nz')]
            obstruction = holes == 2 and all(a%2 for a in c)
            rates = [metadata[k] for k in ('beta','kappa','nu','mu')]
            assert all(r >= 0 for r in rates)
            weights = [rates[0],rates[1]/2,rates[2],rates[3]]
            reported_active = sum(a*b for a,b in zip(metadata['enabled_channel_counts'],weights))
            state_row = {'case':stem,'phase':phase,'N':n,'vacancies':holes,'counts':c,
                         'all_odd_two_vacancy_obstruction':obstruction,'zero_active_rate':reported_active == 0}
            states.append(state_row)
            target_pilot = stem == 'N4_jam_extended_s21092102'
            if target_pilot or obstruction:
                activity = content_activity(s,n,rates,all_identity_channels=target_pilot)
                assert not OWN['births'](s,n)
                if target_pilot:
                    assert c == [12,10,9] and not obstruction
                    assert activity['original_channels'] == [0,0,0]
                    assert activity['content_changing_parallel_attempts'] == 0
                    assert activity['identity_changing_parallel_attempts'] == 115
                else:
                    assert activity['positive_content_activity_witness'] is not None
                selected.append({'case':stem,'phase':phase,'N':n,'counts':c,**activity})
    assert states == parity['all_final_states']
    assert len(rows) == len(parity['fourier_rows']) == 255
    differences = []
    for ours,theirs in zip(rows,parity['fourier_rows']):
        for key in ('N','mode','vacancies'):
            assert ours[key] == theirs[key]
        assert theirs['divergence_residual'] < 2e-12
        for key in ('longitudinal_power','bound'):
            delta = abs(ours[key]-theirs[key]); differences.append(delta)
            assert delta < 2e-12
    assert parity_log['constructed_sizes'] == len(parity['constructed']) == 5
    assert parity_log['final_states_checked'] == len(states) == 80
    assert parity_log['fourier_cases'] == len(rows)
    assert parity_log['all_odd_two_vacancy_endpoints'] == sum(row['all_odd_two_vacancy_obstruction'] for row in states) == 11
    assert parity_log['max_divergence_residual'] == max(row['divergence_residual'] for row in parity['fourier_rows'])
    return {'source_hashes':expected,'author_runners':'read completely, not executed or imported',
            'independent_preseal_preserved':True,'periodic_exact_groups_compared':7,'endpoint_states_checked':len(states),
            'constructed_sizes_checked':[r['N'] for r in parity['constructed']],
            'FFT_rows_compared':len(rows),'max_power_or_bound_difference':max(differences),
            'max_independent_divergence_residual':max(r['divergence_residual'] for r in rows),
            'endpoint_count_and_parity_rows':states,'selected_activity_reconstruction':selected,
            'FFT_rows':rows,'finding':'Pilot has zero content-changing exits, but 115 identity-changing parallel-swap attempts if the optional identity-only channels are retained.',
            'limits':'No simulator source, trajectories, event-rate kinetics, phase/scaling inference or mutation campaign reviewed. Other endpoint activity flags are metadata arithmetic only, except the named pilot and the 11 obstructed endpoints checked independently.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    result = run()
    (args.out/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    (args.out/'INPUT_MANIFEST.json').write_text(json.dumps(list(MANIFEST.values()),indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('endpoint_count_and_parity_rows','FFT_rows')},indent=2))
    print('PASS: source identities, preserved independent evidence, endpoint parity/Gauss/readout and selected activity checks. One content-versus-identity scope clarification remains.')
