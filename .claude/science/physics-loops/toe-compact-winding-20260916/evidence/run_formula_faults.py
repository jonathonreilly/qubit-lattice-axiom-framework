#!/usr/bin/env python3
"""Declared finite formula faults; all sources and raw failures are preserved."""
AUDIT_TIMEOUT_SEC=120
from pathlib import Path
import hashlib,json,subprocess,sys,time


def main():
    root=Path(__file__).resolve().parent;dest=root.parent/'review'/'formula_faults'
    dest.mkdir(parents=True,exist_ok=True)
    faults=[
      ('loop_boundary','sparse_loop_counterexample_check.py','(x,j):-coefficient','(x,j):coefficient'),
      ('sign_environment','sparse_loop_counterexample_check.py','for nu in range(4)) for x in sites]','for nu in range(3)) for x in sites]'),
      ('fourth_moment','sparse_loop_counterexample_check.py','formula=rho/N+3*rho*rho','formula=rho/N+2*rho*rho'),
      ('haar_normalization','compact_cover_source_check.py','mp.sqrt(2*mp.pi/(g*g*T))*Z','mp.sqrt(1/(g*g*T))*Z'),
      ('winding_cubic','compact_cover_source_check.py','third=third/(g**4*T**3)','third=-third/(g**4*T**3)'),
      ('ground_ward_factor','compact_cover_source_check.py','abs(2*inverse_moment-contact)','abs(inverse_moment-contact)'),
      ('source_phase','compact_score_check.py','math.cos(b)*A+math.sin(b)*S','math.cos(b)*A-math.sin(b)*S'),
      ('thermal_time_measure','compact_score_check.py','return variance,beta*expectation','return variance,expectation'),
      ('curl_premise','compact_score_check.py',"np.array([1.,-.4,.2,-.8])","np.array([1.,-.4,.2,-.7])"),
    ]
    rows=[]
    for name,filename,old,new in faults:
        original=(root/filename).read_text();assert original.count(old)==1,(name,original.count(old))
        changed=original.replace(old,new);folder=dest/name;folder.mkdir(exist_ok=True)
        source=folder/filename;source.write_text(changed)
        start=time.monotonic()
        result=subprocess.run([sys.executable,str(source)],capture_output=True,timeout=120)
        (folder/'stdout.txt').write_bytes(result.stdout);(folder/'stderr.txt').write_bytes(result.stderr)
        assert result.returncode!=0 and b'AssertionError' in result.stderr,(name,result.returncode,result.stderr.decode())
        rows.append(dict(name=name,source=source.relative_to(root.parent).as_posix(),
                         sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                         original_sha256=hashlib.sha256((root/filename).read_bytes()).hexdigest(),
                         returncode=result.returncode,elapsed_seconds=time.monotonic()-start,
                         stderr_sha256=hashlib.sha256(result.stderr).hexdigest()))
    print(json.dumps(dict(status='DECLARED_FORMULA_FAULTS_REJECTED',faults=rows,
                         harness_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))


if __name__=='__main__':main()
