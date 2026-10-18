#!/usr/bin/env python3
"""Exact native correction coefficients; no native resonance certification."""
from pathlib import Path
from fractions import Fraction as F
import json,os,subprocess,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_third.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_fourth_diagonal.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_fourth_kernel.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_fourth_kernel_y.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_fourth_local_independent.py']
def main():
 data={}
 for name in AUDIT_INPUT_PATHS:
  path=ROOT/name
  subprocess.run([sys.executable,str(path)],check=True,capture_output=True,text=True,timeout=150)
  data[path.stem]=json.loads(path.with_suffix('.json').read_text())
 third=data['neutral_slow_third']['rows']
 assert [F(r['coefficient']) for r in third]==[F(-1,4)]*4+[F(0)]*5
 for r in data['neutral_slow_fourth_diagonal']:assert F(r['excess'])==F(r['ell'],8)+F(29,192)
 assert [F(r['coefficient']) for r in data['neutral_slow_fourth_kernel']]==[F(19,64),F(-13,256),F(0),F(0)]*2
 assert [F(r['coefficient']) for r in data['neutral_slow_fourth_kernel_y']]==[F(-19,64),F(-13,256),F(0),F(0)]
 assert [F(r['coefficient']) for r in data['neutral_slow_fourth_local_independent']]==[F(19,64),F(-13,256)]
 h1,h2=F(19,32),F(-13,128);assert F(29,192)+2*h1+2*h2==F(109,96);assert -h1-4*h2==F(-3,16)
 out=ROOT/'outputs/native_slow_composite_control/result.json';out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(dict(source_hashes={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in AUDIT_INPUT_PATHS},controls=data,scope='Exact finite-order native coefficients with local all-length proofs; native lifetime and physical scalar remain open'),indent=2)+'\n')
 print('per_site: unchanged one-qubit directional Hamiltonian')
 print('per_mode: support and grading remove long-feature odd-order mixing')
 print('per_block: K3 boundary and full long-row K4 coefficients checked')
 print('lattice_wide: uniform remainder, corrected fast resolvent and physical bridge open')
if __name__=='__main__':main()
