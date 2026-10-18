#!/usr/bin/env python3
"""Exact K2 controls and plaquette counts for the closed-arm argument."""
from pathlib import Path
import sys,json,io,contextlib
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_second_other.py']
sys.path.insert(0,str(ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_bulk_second_other import run

def main():
 rows=[]
 for ell,rx,ry in [(3,1,1),(5,1,1),(3,3,0),(5,3,0),(4,2,1),(6,3,2)]:
  with contextlib.redirect_stdout(io.StringIO()):r=run(ell,rx,ry)
  assert len(r['rows'])==1 and r['rows'][0]['coefficient']=='-4'
  sites=r['rows'][0]['sites'];assert sites==[[0,0,list(range(ell))],[rx,ry,list(range(ell))]]
  rows.append(dict(ell=ell,rx=rx,ry=ry,diagonal='-4',offdiagonal_count=0))
 def plaquettes(x,y):return {(x+dx,y+dy) for dx in [-1,0] for dy in [-1,0]}
 counts=[]
 for x in range(-5,6):
  for y in range(-5,6):
   if (x,y)==(0,0) or abs(x)+abs(y)==1 or (abs(x),abs(y)) in [(2,0),(0,2)]:continue
   n=len(plaquettes(0,0)^plaquettes(x,y));assert n>=6;counts.append(n)
 result=dict(status='PASS',K2_controls=rows,minimum_changed_plaquettes=min(counts),minimum_tension_coefficient=min(counts)/64,scope='Finite exact examples supplement all-length/locality proof. No explicit fixed-order small-lambda threshold, full-H pole or unconditional retained-host stability.')
 out=ROOT/'outputs/native_frozen_arm_control/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
