"""Seal the blind reconstruction without accessing new author sources."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json

HERE=Path(__file__).resolve().parent


def identity(path):
    path=Path(path).resolve();data=path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':sha256(data).hexdigest()}


def check(row):assert identity(row['path'])==row,row['path']


def main():
    boundary=json.loads((HERE/'SOURCE_READ_BOUNDARY.json').read_text())
    for row in boundary['dependencies']:check(row)
    groups=[('finite_spin_check.py','FINITE_SPIN_CHECK','FINITE_SPIN_RESULTS.json'),
            ('boundary_and_bulk_check.py','BOUNDARY_BULK_CHECK','BOUNDARY_BULK_RESULTS.json'),
            ('circuit_gauge_check.py','CIRCUIT_GAUGE_CHECK','CIRCUIT_GAUGE_RESULTS.json')]
    for script,prefix,result in groups:
        r=json.loads((HERE/(prefix+'_RECEIPT.json')).read_text())
        assert r['exit_code']==0 and r['script_sha256']==identity(HERE/script)['sha256']
        for suffix in ['stdout','stderr']:
            p=HERE/(prefix+'.'+suffix);a=identity(p)
            assert {k:a[k] for k in ['bytes','sha256']}==r[p.name]
        assert (HERE/(prefix+'.stderr')).stat().st_size==0
        assert json.loads((HERE/result).read_text())['status']=='PASS'
        assert (HERE/result).read_bytes()==(HERE/(prefix+'.stdout')).read_bytes()
    artifacts=[identity(p) for p in sorted(HERE.rglob('*')) if p.is_file() and p.name not in ['PRE_COMPARISON_SEAL.json','CHECKPOINT.md']]
    packet={'created_utc':datetime.now(timezone.utc).isoformat(),
            'status':'Blind independent reconstruction complete before any new author large-spin access; no formal audit/publication status.',
            'sources':boundary['dependencies'],'artifacts':artifacts,
            'counts':{'sources':len(boundary['dependencies']),'artifacts':len(artifacts),'total':len(boundary['dependencies'])+len(artifacts)},
            'result':'Generated electric coefficient g=t^2/[Delta S(S+1)]>0 and magnetic coefficient J=2t^4/Delta^3; weighted fourth-order correction derived exactly.',
            'sufficient_limit':'At epsilon^2 S(S+1)=J/(2g), beta=beta_0 epsilon^(2d), and fixed local dressed preparation, bounded local field expectations converge uniformly over the stated finite tori for code densities with uniform fourth electric moments. Error O(epsilon+(1+log(S(S+1)))^d/[S(S+1)])=O(1/S).',
            'countercontrols':['Spin shifts fail operator-norm convergence at the electric boundary.',
                               'Saturated uniform-flux spin ice is frozen under the fourth-order spin plaquette Hamiltonian while rotor local parity has nonzero second derivative.',
                               'Birth loss is 2 beta P_vac(1-E^2/[S(S+1)]), not beta P_vac.',
                               'The nonconstant second-order block requires a separate circuit-identification check; it was proved and checked.'],
            'limits':['Prepared states and fixed time/support; beta vanishes but can remain positive at every finite S.',
                      'No unrestricted initial-spin-band, fixed-beta, bare-quench, or increasing-time theorem.',
                      'No thermodynamic phase, photon, native-site or energy-free apparatus claim.',
                      'Finite checks corroborate algebra; uniform locality and finite-cutoff/moment arguments are analytic.'],
            'source_boundary':boundary['new_author_read_boundary'],
            'failures':'No independent scientific execution failed. Full logs and receipts retained; inherited failed attempts remain in unchanged prior packets.'}
    p=HERE/'PRE_COMPARISON_SEAL.json';assert not p.exists()
    p.write_text(json.dumps(packet,indent=2)+'\n')
    for row in packet['sources']+packet['artifacts']:check(row)
    print(json.dumps({'seal':identity(p),'report':identity(HERE/'REPORT.md'),'counts':packet['counts']},indent=2))


if __name__=='__main__':main()
