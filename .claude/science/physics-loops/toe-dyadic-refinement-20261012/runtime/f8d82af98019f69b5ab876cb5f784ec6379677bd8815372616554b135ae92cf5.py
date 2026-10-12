"""Run a source-pinned job with distinct protected INNER/OUTER record names."""
import argparse,hashlib,re,subprocess,sys
from pathlib import Path

E=Path(__file__).resolve().parent
JOBS={
 'exact':('check_exact.py','candidate.py',[]),
 'state':('check_state.py','candidate.py',[]),
 'missing_normalization':('check_exact.py','variants/missing_normalization.py',['--suite','normalization']),
 'tensor_shortcut':('check_exact.py','variants/tensor_shortcut.py',['--suite','tensor']),
 'missing_state_formfactor':('check_state.py','variants/missing_state_formfactor.py',[])}
p=argparse.ArgumentParser();p.add_argument('job',choices=JOBS)
p.add_argument('--label',required=True);a=p.parse_args()
if not re.fullmatch(r'[A-Za-z0-9_]+',a.label):p.error('label must contain only letters, digits and underscores')
manifest=E/'reproduction_manifest.json'
anchor='e3fb00cfd543ecb7b09624b4fc366df1dd5cd3a6f41d198d7071434365fa4ad2'
if hashlib.sha256(manifest.read_bytes()).hexdigest()!=anchor:raise RuntimeError('reproduction manifest anchor changed')
outer=E/'runs'/(a.label+'_outer');inner=E/'runs'/(a.label+'_inner')
for base in (outer,inner):
 for suffix in ('.receipt.json','.stdout.txt','.stderr.txt'):
  if base.with_suffix(suffix).exists():raise RuntimeError('refusing to overwrite '+str(base.with_suffix(suffix)))
rec=[sys.executable,str(E/'record_process.py')]
shared=['--manifest',str(manifest),'--manifest-sha',anchor]
script,candidate,extra=JOBS[a.job]
science=[sys.executable,str(E/script),'--candidate',str(E/candidate),*extra]
inner_cmd=rec+['--record',str(inner),'--timeout','60',*shared,'--',*science]
outer_cmd=rec+['--record',str(outer),'--timeout','70',*shared,'--',*inner_cmd]
sys.exit(subprocess.run(outer_cmd,check=False).returncode)
