"""Exact finite lemma controls supporting the analytical all-even flux theorem."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_EVEN_TORUS_FLUX_ISOLATION_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'scripts/native_even_torus_flux_isolation_controls_2026_09_08.py')
EXPECTED_INPUT_SHA256={'docs/NATIVE_EVEN_TORUS_FLUX_ISOLATION_NOTE_2026-09-08.md': 'da1849644f34f729eda9f8fe8c1fc19602d775404f6c85c6ac365e7fa540c7d0', 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md': 'fc9d6059643cb4468b6cdbaf4134c5c311d1e9d44622b97d5d71d407544fe3dd', 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md': '810b11457e8646aee9b67077fa0c78c31a5fd7101627b2985ba6974ef8f70550', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md': '277c1b112119e5ac54aa21d63b0ee66ea129c1d6329bee0182cefc3dc7d52c70', 'scripts/native_even_torus_flux_isolation_controls_2026_09_08.py': 'c36f54a436c04143c512526ce38deda4929a7bf10fc8bb0a8676c48781775c99'}
import argparse,hashlib,json,os,resource,importlib.util,signal,time
from pathlib import Path

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args();signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic()
 root=Path(__file__).resolve().parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();inputs={n:sha(root/n) for n in AUDIT_INPUT_PATHS}
 if inputs!=EXPECTED_INPUT_SHA256:raise RuntimeError('declared input hash changed')
 spec=importlib.util.spec_from_file_location('isolation_controls',root / 'scripts' / 'native_even_torus_flux_isolation_controls_2026_09_08.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 checks=module.run()
 if checks!=5955:raise RuntimeError('control coverage')
 seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
 if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
 result={'executed_predicates':checks+2,'lemma_predicates':checks,'coverage_guard':1,'resource_guard':1,'half_widths':list(range(2,9)),'transverse_extents':[4,6],'elapsed_seconds':seconds,'peak_rss_mib':rss,'source_sha256':sha(Path(__file__)),'input_sha256':inputs,'scope':'Exact finite controls for complex SVD equality, paired-channel kernel positivity and structural layer/gauge induction. The linked analytical proof establishes all even sizes; finite tested widths do not prove the theorem by extrapolation.'}
 (root/'outputs/native_even_torus_flux_isolation_2026_09_08.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
 if not args.json:
  print('per_element: executed exact complex-rational channel and phase controls in the declared finite examples.')
  print('per_site: finite boundary and inward-frontier propagation controls support the separately proved analytical induction.')
  print('per_mode: finite CAR-kernel and reflected-matrix identities are checked with exact arithmetic.')
  print('per_block: the declared rectangular half-slab widths and transverse extents receive finite structural controls.')
  print('lattice_wide: analytical induction in the linked note; finite controls only.')
  print(f'TOTAL: PASS={checks+2} FAIL=0')
  print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
if __name__=='__main__':main()
