"""Launch a disjoint full INNER/OUTER reproduction with fixed source anchors."""
from pathlib import Path
import argparse,re,subprocess,sys
e=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--job',required=True,choices=['baseline','wrong_frame_sign','omit_continuum_unrotation','half_angle'])
p.add_argument('--label',required=True);a=p.parse_args()
if not re.fullmatch('[A-Za-z0-9_]+',a.label):raise SystemExit('label must contain only letters, digits and underscores')
py=sys.executable
if a.job=='half_angle':
 manifest=e/'half_angle_reproduction_manifest.json';anchor='8ff486417a03cb983c0fc233315c38c78b3fa13b67e526cf977a7c821f0ad35d'
 scientific=[py,str(e/'check_half_angle.py')]
else:
 manifest=e/'reproduction_manifest.json';anchor='e232c9e4cc4ebcba1f4a60ebdd845c7d5349b034180f3b84dd46810a2e8a2224'
 candidate=e/'candidate.py' if a.job=='baseline' else e/'variants'/(a.job+'.py')
 scientific=[py,str(e/'check_controls.py'),'--candidate',str(candidate)]
shared=[py,str(e/'record_process.py')]
inner=[*shared,'--record',str(e/'runs'/(a.label+'_inner')),'--timeout','60','--manifest',str(manifest),'--manifest-sha',anchor,'--',*scientific]
outer=[*shared,'--record',str(e/'runs'/(a.label+'_outer')),'--timeout','70','--manifest',str(manifest),'--manifest-sha',anchor,'--',*inner]
raise SystemExit(subprocess.call(outer,cwd=e))
