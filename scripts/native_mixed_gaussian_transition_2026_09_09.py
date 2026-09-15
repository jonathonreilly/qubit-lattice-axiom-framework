#!/usr/bin/env python3
"""Portable supporting checks; no physical evolution or matrix evaluation."""
import os,sys
if __name__=='__main__' and not (sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site and sys.flags.optimize==2):
 os.execv(sys.executable,[sys.executable,'-I','-B','-S','-OO',__file__,*sys.argv[1:]])
import argparse, contextlib, hashlib, io, json, importlib.util
from pathlib import Path

AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS=('docs/NATIVE_CERTIFIED_IMAGINARY_TIME_NOTE_2026-09-09.md', 'docs/NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md', 'docs/NATIVE_MIXED_GAUSSIAN_TRANSITION_NOTE_2026-09-09.md', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/provenance/FAST_CONTROL_RESULT.json', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/provenance/FAST_FREEZE.json', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/provenance/FAST_PROOF.md', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/provenance/FAST_REVIEW.md', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/provenance/FIXED_DEGREE.md', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/provenance/MIXED_CONTROL_RESULT.json', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/provenance/MIXED_FREEZE.json', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/provenance/MIXED_PROOF.md', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/provenance/MIXED_REVIEW.md', 'scripts/native_mixed_gaussian_transition_2026_09_09_fast.py', 'scripts/native_mixed_gaussian_transition_2026_09_09_fock.py', 'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/SOURCE_MANIFEST.json')

def _capture_fock(root):
 path=root/'scripts/native_mixed_gaussian_transition_2026_09_09_fock.py'
 out=io.StringIO()
 with contextlib.redirect_stdout(out):
  spec=importlib.util.spec_from_file_location('__main__',root/'scripts/native_mixed_gaussian_transition_2026_09_09_fock.py');module=importlib.util.module_from_spec(spec)
  exec(compile((root/'scripts/native_mixed_gaussian_transition_2026_09_09_fock.py').read_bytes(),str(path),'exec'),module.__dict__)
 return json.loads(out.getvalue())

def _capture_fast(root):
 path=root/'scripts/native_mixed_gaussian_transition_2026_09_09_fast.py'
 out=io.StringIO()
 with contextlib.redirect_stdout(out):
  spec=importlib.util.spec_from_file_location('__main__',root/'scripts/native_mixed_gaussian_transition_2026_09_09_fast.py');module=importlib.util.module_from_spec(spec)
  exec(compile((root/'scripts/native_mixed_gaussian_transition_2026_09_09_fast.py').read_bytes(),str(path),'exec'),module.__dict__)
 return json.loads(out.getvalue())

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--json',action='store_true');args=p.parse_args()
 root=Path(__file__).resolve().parents[1]
 manifest=root/'outputs/native_mixed_gaussian_transition_2026_09_09_inputs/SOURCE_MANIFEST.json'
 pins=json.loads(manifest.read_text())['inputs']
 for rel,digest in pins.items():
  if hashlib.sha256((root/rel).read_bytes()).hexdigest()!=digest:raise ValueError('source binding: '+rel)
 reports=[]
 for loader,count in [(_capture_fock,716),(_capture_fast,16)]:
  row=loader(root)
  if row['predicates']!=count or row['physical_calls']!=0 or not row['status'].startswith('PASS'):raise ValueError('supporting control result')
  row.pop('seconds',None);row.pop('rss_bytes',None);reports.append(row)
 result={'status':'PASS_SUPPORTING_CONTROLS','claim_status':'conditional-support','physical_calls':0,'controls':reports,'input_hashes':pins,'scope':'Synthetic literal CAR and exact finite arithmetic only; no native overlap or alpha certificate.'}
 payload=json.dumps(result,sort_keys=True,indent=2)+'\n';(root/'outputs/native_mixed_gaussian_transition_2026_09_09.json').write_text(payload);print(payload,end='')
 print('TOTAL: PASS='+str(sum(row['predicates'] for row in reports))+' FAIL=0')
 print('per_element: literal synthetic ordered CAR and rational identities are checked; no native matrix is evaluated.')
 print('per_site: only declared two-mode and four-mode synthetic fixtures execute; no native spatial propagation is performed.')
 print('per_mode: relative pairing frames and Majorana signs are analytical obligations and synthetic finite controls, not computed native orbitals.')
 print('per_block:716 Fock predicates include one resource predicate;16 exact fast controls check finite arithmetic, not physical solver mutants.')
 print('lattice_wide: infinite overlap positivity and tail estimates are conditional analytical results; no alpha value, amplitude floor or native evolution is computed.')
if __name__=='__main__':main()
