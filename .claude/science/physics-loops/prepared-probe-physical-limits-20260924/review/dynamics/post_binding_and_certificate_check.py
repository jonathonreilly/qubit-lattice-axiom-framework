"""Released-source POST binding and independent saved-certificate arithmetic.

Does not import or execute either author control. Reads every root certificate
word and applies only the selected original mark using a new sparse charge map.
The full H4 pair enumeration is not repeated. All PRE members stay unchanged.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from collections import defaultdict
import ast
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOTS = [
    ('prepared-probe-dynamics-personal',
     '70c96cb1ce304408760dbf698a119a8468d9ca466438b4ce1aa8fd5f5ce42af4',
     'PREPARED_PROBE_ENERGY_AND_FINITE_SCALE_WINDOW_ROOT.md',
     '867d9b04e2023cdf3280382840e1f98fe1cd9061bf529ca94a84390c888bedc1'),
    ('prepared-probe-output-energy-personal',
     '51b08bce5a0bbfefff5b6125164cf9a00510deda5fe0da11acb06b25623941bb',
     'SELECTED_PROBE_OUTPUT_ENERGY_ROOT.md',
     '57d3e1c06396db01957536224d7c03d0b3a04908a34ae01bb56a37ea5250ff35'),
]


def sha(data):
    return sha256(data).hexdigest()


def copy_source(folder, name, expected=None):
    assert Path(name).name == name
    origin = BASE / folder / name
    data = origin.read_bytes()
    if expected is not None:
        assert sha(data) == expected, (folder, name)
    copied = HERE / 'post_sources' / folder / name
    copied.parent.mkdir(parents=True,exist_ok=True)
    copied.write_bytes(data)
    return {'origin':str(origin),'copy':str(copied.relative_to(HERE)),
            'sha256':sha(data),'bytes':len(data)}


def canonical(minus, occupied):
    return tuple(sorted(minus)), tuple(sorted(occupied.items()))


def initial(side):
    minus = {(1,1,0),(2,2,0)}
    occupied = {(0,side-1,0):1,(0,0,1):1,(0,0,side-1):1}
    return (canonical(minus,{**occupied,(1,0,0):1}),
            canonical(minus,{**occupied,(0,1,0):1}))


def mark(vector, side, sigma):
    a=(0,0,0); b=(side-1,0,0)
    destinations=[(1,0,0),(0,side-1,0),(0,1,0),(0,0,side-1),(0,0,1)]
    result=defaultdict(int)
    for (minus_tuple, occupied_tuple), coefficient in vector.items():
        minus=set(minus_tuple); occupied=dict(occupied_tuple)
        if b in occupied:
            continue
        old_charge=-1 if a in minus else 1
        for dst in destinations:
            if dst in occupied:
                continue
            new_minus=minus-{a}
            if sigma==-1:
                new_minus.add(a)
            new_occupied={**occupied,dst:old_charge,b:-sigma}
            result[canonical(new_minus,new_occupied)]+=coefficient
    return {q:c for q,c in result.items() if c}


def read_certificate(side, row):
    path=HERE/'post_sources/prepared-probe-dynamics-personal'/f'FLAT_ACTION_SIDE_{side}.json'
    assert sha(path.read_bytes())==row['action_certificate_sha256']
    data=json.loads(path.read_text()); vector={}
    for item in data:
        minus=[tuple(v) for v in item['A_minus']]
        occupied=[(tuple(v),q) for v,q in item['B_occupied']]
        assert len(minus)==len(set(minus))
        assert len(occupied)==len(dict(occupied))==4
        assert all(len(v)==3 and all(0<=x<side for x in v) and sum(v)%2==0 for v in minus)
        assert all(len(v)==3 and all(0<=x<side for x in v) and sum(v)%2==1 and q in (-1,1) for v,q in occupied)
        assert sum(q for v,q in occupied)==2*len(minus)
        coefficient=item['amplitude']
        assert isinstance(coefficient,int) and coefficient!=0
        key=canonical(minus,dict(occupied))
        assert key not in vector
        vector[key]=coefficient
    assert len(vector)==row['shifted_action_words']
    ic,ie=initial(side)
    shifted_mean=Fraction(vector.get(ic,0)-vector.get(ie,0),2)
    shifted_second=Fraction(sum(c*c for c in vector.values()),2)
    variance=shifted_second-shifted_mean**2
    assert shifted_mean==Fraction(row['mean_minus_background'])
    assert variance==Fraction(row['variance_H4'])
    assert shifted_mean+row['all_B_empty_flat_scalar']==Fraction(row['mean_H4'])
    # Count pair types directly from local displacements, without any author graph function.
    A=side**3//2
    axial_pairs=3*A
    face_diagonal_pairs=6*A
    assert axial_pairs+face_diagonal_pairs==row['overlap_pairs']
    empty=-2*(35*axial_pairs+36*face_diagonal_pairs)
    assert empty==row['all_B_empty_flat_scalar']
    birth_rows=[]
    for sigma in (-1,1):
        assert not mark({ic:1,ie:-1},side,sigma)
        out=mark(vector,side,sigma)
        norm=Fraction(sum(c*c for c in out.values()),2)
        expected=row['selected_mark_leakage'][str(sigma)]
        assert norm==Fraction(expected['norm_squared']) and len(out)==expected['output_words']
        assert all(len(occupied)==6 and sum(q for v,q in occupied)==2*len(minus)
                   for minus,occupied in out)
        birth_rows.append({'sigma':sigma,'gamma':int(norm),'output_words':len(out),
                           'initial_dark_map_directly_zero':True,
                           'all_output_charge_and_record_counts_checked':True})
    return {'side':side,'certificate_words_read':len(data),'shifted_mean':str(shifted_mean),
            'shifted_second':str(shifted_second),'variance':str(variance),
            'all_B_empty_scalar':empty,'pair_types':{'r=1':axial_pairs,'r=2':face_diagonal_pairs},
            'birth_rows':birth_rows,'all_rows_unique_P_words_with_correct_global_charge_and_record_count':True}


def nested_functions(path):
    tree=ast.parse(path.read_text())
    outer=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='control')
    return {n.name:ast.dump(n,include_attributes=False) for n in outer.body if isinstance(n,ast.FunctionDef)}


def assertions(path):
    tree=ast.parse(path.read_text())
    return [ast.unparse(n.test) for n in ast.walk(tree) if isinstance(n,ast.Assert)]


def main():
    pre_seal_path=HERE/'PRE_SEAL.json'
    assert sha(pre_seal_path.read_bytes())=='c6686cc03d195af4487e3df90cd64e152869c608d5170cd70c5dd81f544b9fdc'
    pre_seal=json.loads(pre_seal_path.read_text())
    for member in pre_seal['members']:
        data=(HERE/member['path']).read_bytes()
        assert len(data)==member['bytes'] and sha(data)==member['sha256']
    assert sha((HERE/'PRE.md').read_bytes())=='3f9bae4b8de40697dce8ddd0d12382fd7b505156922ed8f713cc26de5e3a9a27'
    copies=[]; seals=[]
    for folder,seal_hash,note,note_hash in ROOTS:
        copies.append(copy_source(folder,'AUTHOR_SEAL.json',seal_hash))
        seal=json.loads((BASE/folder/'AUTHOR_SEAL.json').read_text())
        assert seal['files'][note]['sha256']==note_hash
        for name,identity in seal['files'].items():
            copied=copy_source(folder,name,identity['sha256'])
            assert copied['bytes']==identity['bytes']
            copies.append(copied)
        seals.append({'folder':folder,'seal_sha256':seal_hash,'sealed_members_checked':len(seal['files']),
                      'created_utc':seal['created_utc']})
    copies.append(copy_source('prepared-probe-output-energy-personal','ROOT_EDITORIAL_QUALIFICATION.md'))
    source_pins={'phase':'POST released-source copies','PRE_seal_sha256':sha(pre_seal_path.read_bytes()),
                 'records':copies,'author_seals':seals,'pin_checker_sha256':sha(Path(__file__).read_bytes())}
    (HERE/'POST_SOURCE_PINS.json').write_text(json.dumps(source_pins,indent=2)+'\n')
    dyn=HERE/'post_sources/prepared-probe-dynamics-personal'
    out=HERE/'post_sources/prepared-probe-output-energy-personal'
    dyn_result=json.loads((dyn/'FLAT_MATTER_RESULTS.json').read_text())
    out_result=json.loads((out/'OUTPUT_ENERGY_RESULTS.json').read_text())
    for directory,code,result,stderr in [(dyn,'flat_matter_controls.py','FLAT_MATTER_RESULTS.json','FLAT_MATTER.stderr'),
                                         (out,'output_energy_controls.py','OUTPUT_ENERGY_RESULTS.json','OUTPUT_ENERGY.stderr')]:
        execution=json.loads((directory/'EXECUTION.json').read_text())
        assert execution['code_sha256']==sha((directory/code).read_bytes())
        assert execution['result_sha256']==sha((directory/result).read_bytes())
        assert execution['exit_code']==0 and execution['stderr_bytes']==0
        assert (directory/stderr).read_bytes()==b''
    out_execution=json.loads((out/'EXECUTION.json').read_text())
    assert out_execution['reused_source_sha256']==sha((dyn/'flat_matter_controls.py').read_bytes())
    certs=[read_certificate(row['side'],row) for row in dyn_result['rows']]
    first=json.loads((HERE/'PRIMITIVE_DYNAMICS_RESULTS.json').read_text())['rows'][0]
    own_eight=json.loads((HERE/'TOPOLOGY_GRAM_RESULTS.json').read_text())['rows'][1]
    own_outputs=json.loads((HERE/'OUTPUT_ENERGY_RESULTS.json').read_text())['rows']
    root_six=dyn_result['rows'][0];root_sixteen=dyn_result['rows'][1]
    assert Fraction(root_six['mean_H4'])==frac(first['flat_moments']['all_angles_zero']['mean_H4'])
    assert Fraction(root_six['variance_H4'])==frac(first['flat_moments']['all_angles_zero']['variance_H4'])
    for b in first['selected_birth_rows']:
        assert Fraction(root_six['selected_mark_leakage'][str(b['sigma'])]['norm_squared'])==frac(b['gamma_all_angles_zero'])
    assert Fraction(root_sixteen['variance_H4'])==frac(own_eight['flat_moments']['harmonic_averaged']['variance_H4'])
    for b in own_eight['selected_birth_rows']:
        assert Fraction(root_sixteen['selected_mark_leakage'][str(b['sigma'])]['norm_squared'])==frac(b['gamma_harmonic_averaged'])
    output_comparison=[]
    for row in out_result['rows'][0]['selected_output_matter_rows']:
        own=next(r for r in own_outputs if r['side']==8 and r['sigma']==row['sigma'])
        assert row['variance_H4']==frac(own['flat_moments']['harmonic_averaged']['variance_H4'])
        assert row['mean_H4']-int(root_sixteen['mean_H4'])==2012
        assert row['mean_minus_empty']==7152 and row['record_number']==2054
        assert row['mean_H4']+1314816==row['mean_minus_empty']
        assert int(root_sixteen['mean_minus_background'])==5140
        output_comparison.append({'sigma':row['sigma'],'root_side16_variance':row['variance_H4'],
                                  'PRE_side8_harmonic_variance':int(frac(own['flat_moments']['harmonic_averaged']['variance_H4'])),
                                  'mean_shift_above_empty':row['mean_minus_empty'],
                                  'output_minus_input_mean':row['mean_H4']-int(root_sixteen['mean_H4'])})
    f1=nested_functions(dyn/'flat_matter_controls.py')
    f2=nested_functions(out/'output_energy_controls.py')
    reused=['near','location','hop','step','pair_action']
    assert all(f1[k]==f2[k] for k in reused)
    a1=assertions(dyn/'flat_matter_controls.py');a2=assertions(out/'output_energy_controls.py')
    diagonal=next(x for x in a1 if x.startswith('out.get(q, 0) =='))
    assert diagonal in a2
    assert len(a1)==3 and len(a2)==2
    # These are explanatory exact arithmetic identities, not a numerical optimization scan.
    assert Fraction(4**2,48)==Fraction(1,3)
    assert Fraction(4**2,24)==Fraction(2,3)
    report={'scope':__doc__,'PRE_members_hash_verified_unchanged':len(pre_seal['members']),
            'source_copies':len(copies),'author_seals':seals,
            'certificate_arithmetic':certs,'side6_comparison':'Root flat moments and both leakage norms equal the PRE all-zero-angle comparator, not the PRE physical harmonic average.',
            'side16_vs_PRE_side8':'Variance and both leakage norms agree with the PRE side-eight harmonic averages. This cross-graph agreement is corroboration, not an independently proved universal volume formula.',
            'normalized_output_comparison':output_comparison,
            'AST_identical_reused_nested_functions':reused,
            'root_dynamics_assertions':a1,'root_output_assertions':a2,
            'editorial_qualification':'Only the diagonal-norm assertion is retained from the old assertions. Two-input Hermiticity and initial-dark-map assertions were removed; a new output charge/record-count assertion was added.',
            'beta_to_PRE_eta':'beta=4 eta; beta^2/48=eta^2/3 and beta^2/24=2 eta^2/3.',
            'limits':'No author runner execution; no new H4 pair enumeration. Output root has no saved full action certificate, so its moments are reviewed from complete source/result plus PRE side-eight agreement, not reconstructed from an output certificate.',
            'checker_sha256':sha(Path(__file__).read_bytes())}
    print(json.dumps(report,indent=2))


def frac(x):
    return Fraction(x['numerator'],x['denominator'])


if __name__=='__main__':
    main()
