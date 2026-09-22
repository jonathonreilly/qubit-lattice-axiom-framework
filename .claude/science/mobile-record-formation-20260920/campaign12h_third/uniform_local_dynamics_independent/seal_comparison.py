"""Authenticate the immutable PRE and author packet and seal this comparison."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def identity(path):
    path = Path(path).resolve(); b = path.read_bytes()
    return {'path':str(path),'bytes':len(b),'sha256':sha256(b).hexdigest()}


def check(row):
    assert identity(row['path']) == row, row['path']


def main():
    prepath=HERE/'PRE_COMPARISON_SEAL.json'
    authorpath=BASE/'UNIFORM_LOCAL_RING_AUTHOR_SEAL.json'
    assert identity(prepath)['sha256']=='928e25108e5482c4a8d555323e55cda2a6f3b0a5b9cbdcf4e0c1b2550e84fd6b'
    assert identity(authorpath)['sha256']=='4b52f52f820ed5efbe01b18d47c0166018f0c421cd507fb55f171d893f8a7ce5'
    pre=json.loads(prepath.read_text());author=json.loads(authorpath.read_text())
    old=pre['sources']+pre['artifacts'];auth=author['artifacts']
    for row in old+auth:check(row)
    result=json.loads((HERE/'COMPARISON_RESULTS.json').read_text())
    assert result['status']=='PASS'
    receipt=json.loads((HERE/'COMPARISON_CHECK_RECEIPT.json').read_text())
    assert receipt['exit_code']==0
    assert identity(HERE/'comparison_check.py')['sha256']==receipt['script_sha256']
    for name in ['COMPARISON_CHECK.stdout','COMPARISON_CHECK.stderr']:
        a=identity(HERE/name); assert a['bytes']==receipt[name]['bytes'] and a['sha256']==receipt[name]['sha256']
    extra_dependencies=result['authentication']['prior_context_dependencies']
    for row in extra_dependencies:check(row)
    new_names=['COMPARISON.md','comparison_check.py','COMPARISON_RESULTS.json',
               'COMPARISON_CHECK.stdout','COMPARISON_CHECK.stderr','COMPARISON_CHECK_RECEIPT.json',
               'COMPARISON_LITERATURE_RECEIPT.json','literature/Barthel_Kliesch_1111_4210v2.html',
               'seal_comparison.py']
    failure=HERE/'failed_attempts/dissipator_structural_equality'
    new_names += [str(p.relative_to(HERE)) for p in sorted(failure.iterdir()) if p.is_file()]
    new=[identity(HERE/name) for name in new_names]
    rows={r['path']:r for r in old+auth+extra_dependencies+new+[identity(prepath),identity(authorpath)]}
    packet={'created_utc':datetime.now(timezone.utc).isoformat(),
            'status':'Bounded source comparison complete; no mathematical correction requested. No formal audit or publication status.',
            'preserved_PRE_seal':identity(prepath),'author_seal':identity(authorpath),
            'disposition':'Finite circuit proof and full state-dependent dissipator source support beta=beta_0 epsilon^(2d) and O(epsilon) local error at fixed times uniformly over the stated tori and prepared ice densities.',
            'counts':{'PRE_rows_verified':len(old),'author_rows_verified':len(auth),'new_comparison_rows':len(new),'unique_bindings':len(rows)},
            'bindings':[rows[k] for k in sorted(rows)],
            'coverage':{'author_arguments':'Complete note and runners; all stored rational matrices recomposed independently.',
                        'numerical_tables':'All fields read and ratio arithmetic independently checked; high-precision author exponentials authenticated, not rerun.',
                        'primary_import':'Barthel-Kliesch 1111.4210v2 finite-range time-dependent Lindblad locality; Sections II-III, V and Appendices A-D read.',
                        'unopened':'Later large-spin, weak-field, one-dimensional transport, ramp, checkpoint and registry files.'},
            'failed_attempts':'Author threshold failure retained in its original packet; independent symbolic structural-equality failure retained with exact diagnosis.',
            'limitations':['Prepared initial family and polynomially decreasing births only; no fixed-beta/bare-quench theorem.',
                           'Fixed support and time horizon; no thermodynamic phase, photon, native compiler or practical constant claim.',
                           'Finite controls corroborate algebra; analytic locality and source estimates establish uniformity.']}
    final=HERE/'FINAL_SEAL.json';assert not final.exists()
    final.write_text(json.dumps(packet,indent=2)+'\n')
    # Fresh post-write verification, with no mutable checkpoint included.
    for row in packet['bindings']:check(row)
    print(json.dumps({'final_seal':identity(final),'comparison':identity(HERE/'COMPARISON.md'),
                      'comparison_results':identity(HERE/'COMPARISON_RESULTS.json'),'counts':packet['counts']},indent=2))


if __name__=='__main__':main()
