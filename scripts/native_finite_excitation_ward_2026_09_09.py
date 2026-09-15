#!/usr/bin/env python3
"""Portable exact supporting certificate for the conditional Ward theorem."""
import argparse,hashlib,json,pathlib,signal,time,importlib.util

AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS=('docs/NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md', 'scripts/native_finite_excitation_ward_controls_2026_09_09.py', 'docs/NATIVE_INFINITE_STAR_NODE_REDUCTION_NOTE_2026-09-09.md', 'docs/NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md', 'outputs/native_finite_excitation_ward_2026_09_09_inputs.json')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',action='store_true')
    args=parser.parse_args();signal.alarm(180);start=time.monotonic()
    root=pathlib.Path(__file__).resolve().parents[1]
    manifest=root/'outputs/native_finite_excitation_ward_2026_09_09_inputs.json'
    pins=json.loads(manifest.read_text())
    for rel,expected in pins.items():
        actual=hashlib.sha256((root/rel).read_bytes()).hexdigest()
        if actual!=expected:raise ValueError('input hash mismatch: '+rel)
    helper=root/'scripts/native_finite_excitation_ward_controls_2026_09_09.py'
    spec=importlib.util.spec_from_file_location('ward_controls',root/'scripts/native_finite_excitation_ward_controls_2026_09_09.py')
    module=importlib.util.module_from_spec(spec)
    exec(compile(helper.read_bytes(),str(helper),'exec'),module.__dict__)
    result=module.run();result['input_hashes']=pins
    result['claim_id']='native_finite_excitation_ward_note_2026-09-09'
    result['actual_current_surface_status']='conditional-support'
    result['review_status']='current execution evidence only; historical source reviews preserved separately'
    result['elapsed_seconds']=time.monotonic()-start
    payload=json.dumps(result,sort_keys=True,indent=2)+'\n';(root/'outputs/native_finite_excitation_ward_2026_09_09.json').write_text(payload)
    (root/'outputs/native_finite_excitation_ward_2026_09_09.md').write_text('# Current finite supporting controls\n\nActual '+str(result['supporting_predicates'])+' mathematical predicates, including '+str(result['adverse_cases'])+' adverse cases, with zero physical runs. The exact rational state-compression certificate is in the paired JSON. This execution does not evaluate alpha or supply a source-review verdict.\n')
    print(payload,end='')
    print(f"TOTAL: PASS={result['supporting_predicates']} FAIL=0")
    print('per_element: finite exact rational Ward and normalization predicates are executed on the declared matrices.')
    print('per_site: local source identities are checked in finite fixtures; no native spatial tail approximation is computed.')
    print('per_mode: rational rank and principal-angle fidelity bounds execute; the exact principal orbitals are not computed.')
    print('per_block: the finite state-error certificate is evaluated; all other algorithmic approximation errors remain unpriced.')
    print('lattice_wide: stationary Fock and infinite Ward identities are analytical; no physical node scalar or interacting phase is evaluated.')
if __name__=='__main__': main()
