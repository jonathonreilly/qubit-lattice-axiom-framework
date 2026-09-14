#!/usr/bin/env python3
"""Actual source mutations against the self-contained public runner."""
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time


def main():
    source=Path(sys.argv[1]).resolve()
    original=source.read_text()
    changes=[
        ('full_fourth_payload','rotated = np.r_[z[0], frame@z[1:]]',
                              'rotated = np.r_[0, frame@z[1:]]'),
        ('payload_frame','frame@z[1:]', 'frame.T@z[1:]'),
        ('matrix_measure_jacobian','2*np.log(EPS)-5*np.log(d)',
                                  '2*np.log(EPS)-4*np.log(d)'),
        ('closed_boundary_assignment','return CLOSED_EPS if r==1 else ordinary(r-1)',
                                      'return ordinary(r) if r==1 else ordinary(r-1)'),
        ('complex_relay_sign','cross[1,h-1]=(-1)**h*sp.conjugate(aa)',
                              'cross[1,h-1]=sp.conjugate(aa)'),
        ('distinct_edge_type_planes','e_index*self.colors+self.color_id(n)',
                                    '0*self.colors+self.color_id(n)'),
        ('coarse_color_columns','index = self.color_id(n)*len(self.payloads)+h',
                                'index = h'),
        ('plane_above_both_endpoints','max(n[2],destination[2])*self.side',
                                      'n[2]*self.side'),
        ('crossing_slot_identity','slot = registry[local_site].index(key)',
                                  'slot = 0'),
        ('whole_action_terminal_sign','z[-1].conjugate()*(-1)**h*a*v',
                                      'z[-1].conjugate()*(-1)**(h+1)*a*v'),
        ('spectral_lower_bound','lower=min(mass,1)/(1+h*(1+b))**2',
                                'lower=min(mass,1)'),
    ]
    out=Path(__file__).resolve().parent/'block4_mutations'
    out.mkdir(exist_ok=True)
    rows=[]
    with tempfile.TemporaryDirectory(prefix='toe-periodic-codec-mutations-') as directory:
        for label,old,new in changes:
            count=original.count(old)
            assert count==1,(label,count)
            mutated=original.replace(old,new,1)
            path=Path(directory)/(label+'.py')
            path.write_text(mutated)
            start=time.monotonic()
            result=subprocess.run([sys.executable,str(path)],capture_output=True,text=True,timeout=180)
            for suffix,value in [('py',mutated),('stdout',result.stdout),('stderr',result.stderr)]:
                (out/(label+'.'+suffix+'.gz')).write_bytes(gzip.compress(value.encode(),mtime=0))
            row=dict(mutation=label,old=old,new=new,returncode=result.returncode,
                     caught_by_assertion=result.returncode!=0 and 'AssertionError' in result.stderr,
                     seconds=time.monotonic()-start,stderr_tail=result.stderr.splitlines()[-5:],
                     mutant_sha256=hashlib.sha256(mutated.encode()).hexdigest())
            rows.append(row)
            print(json.dumps(row),flush=True)
            evidence=dict(primary=str(source),primary_sha256=hashlib.sha256(original.encode()).hexdigest(),
                          mutations=rows,finished=len(rows)==len(changes),
                          all_caught=all(r['caught_by_assertion'] for r in rows))
            (out/'SUMMARY.json').write_text(json.dumps(evidence,indent=2)+'\n')
    assert evidence['all_caught'] and evidence['finished']


if __name__=='__main__':
    main()
