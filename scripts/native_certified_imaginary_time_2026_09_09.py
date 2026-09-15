"""Small exact supporting controls only; never a native propagation."""
import argparse, contextlib, hashlib, io, json, importlib.util
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'outputs'/'native_certified_imaginary_time_2026_09_09_inputs'

AUDIT_TIMEOUT_SEC=5
AUDIT_INPUT_PATHS=('docs/NATIVE_CERTIFIED_IMAGINARY_TIME_NOTE_2026-09-09.md', 'scripts/native_certified_imaginary_time_2026_09_09_algebra.py', 'outputs/native_certified_imaginary_time_2026_09_09_inputs/provenance/RATIONAL_TIME.md', 'outputs/native_certified_imaginary_time_2026_09_09_inputs/provenance/RATIONAL_TIME_REVIEW.md', 'outputs/native_certified_imaginary_time_2026_09_09_inputs/provenance/RICCATI.md', 'outputs/native_certified_imaginary_time_2026_09_09_inputs/provenance/RICCATI_REVIEW.md', 'docs/NATIVE_PAIR_VACUUM_CHART_NOTE_2026-09-09.md', 'docs/NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md', 'outputs/native_certified_imaginary_time_2026_09_09_inputs/MANIFEST.json')

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--json',action='store_true')
 args=parser.parse_args()
 manifest=json.loads((P/'MANIFEST.json').read_text())
 for name,digest in manifest.items():
  if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
   raise RuntimeError('source pin '+name)
 source=(ROOT/'scripts/native_certified_imaginary_time_2026_09_09_algebra.py').read_bytes()
 capture=io.StringIO()
 with contextlib.redirect_stdout(capture):
  spec=importlib.util.spec_from_file_location('__main__',ROOT/'scripts/native_certified_imaginary_time_2026_09_09_algebra.py');module=importlib.util.module_from_spec(spec)
  exec(compile(source,str(ROOT/'scripts/native_certified_imaginary_time_2026_09_09_algebra.py'),'exec'),module.__dict__)
 algebra=json.loads(capture.getvalue())
 if algebra['exact_predicates']!=11 or algebra['status']!='PASS':raise RuntimeError('algebra receipt')
 budget=6*F(3)**25*F(2,3)**129
 if not budget<F(1,10**10):raise RuntimeError('degree128 budget')
 if 6*F(3)**25*F(2,3)**65<F(1,10**10):raise RuntimeError('adverse reduced degree')
 r=F(99,100)
 margin=2*r-99*(1-r*r)
 if margin!=F(99,10000):raise RuntimeError('margin')
 if 2*F(9,10)-99*(1-F(9,10)**2)>=0:raise RuntimeError('adverse smaller disk')
 out={'status':'SUPPORTING_CONTROLS_PASS','scope':'exact synthetic algebra and rational bounds; no native propagation','algebra_predicates':11,'additional_rational_predicates':4,'degree128_upper':str(budget),'disk_margin':str(margin),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'inputs':manifest}
 payload=json.dumps(out,sort_keys=True,indent=2)+'\n';(ROOT/'outputs/native_certified_imaginary_time_2026_09_09.json').write_text(payload);print(payload,end='')
 (ROOT/'outputs/native_certified_imaginary_time_2026_09_09.md').write_text('# Current finite supporting controls\n\nActual15 predicates:11 synthetic algebra and4 rational comparisons. No native propagation, kernel, node scalar or source-review verdict is computed.\n')
 print(f"TOTAL: PASS={out['algebra_predicates']+out['additional_rational_predicates']} FAIL=0")
 print('per_element:11 exact synthetic algebra predicates execute on declared two-mode and four-mode fixtures.')
 print('per_site: no native spatial propagation or local kernel is executed; spatial approximation remains a separate input.')
 print('per_mode: four exact rational comparisons check polynomial budgets and disk margins, not total algorithmic error.')
 print('per_block: reference Riccati and exact positive-band charts are distinguished analytically; Gram and initial-tail premises remain.')
 print('lattice_wide: all-time chart control is analytical; no imaginary-time native evolution or node scalar is evaluated.')
if __name__=='__main__':main()
