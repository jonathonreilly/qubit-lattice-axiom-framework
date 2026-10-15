#!/usr/bin/env python3
"""Count-derived energy requirements and exposed nominal window inventory.
Reads only the pinned day169 ODF and label, downloading absent public inputs.
Package-local integrity reads hash the source closure and paired note. Outputs
are written only below the requested output directory and public-input cache.
No physical scalar residual, energy budget, or held-out data are supplied.
"""
import argparse
import hashlib
import json
from pathlib import Path
import ssl
import urllib.request
import scalar_count_energy_controls as count
import scalar_inertial_energy_controls as inertial
import cassini_count_window_controls as timing

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_COUNT_KERNEL_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_count_energy_controls.py',
    'scripts/scalar_inertial_energy_controls.py',
    'scripts/cassini_count_window_controls.py',
    'scripts/cassini_odf_decode.py',
    'scripts/cassini_count_window_inputs.json',
]

def verified_input(cache,entry):
    path=cache/entry['filename']
    def valid(blob):
        return len(blob)==entry['bytes'] and hashlib.sha256(blob).hexdigest()==entry['sha256']
    if path.exists():
        if not valid(path.read_bytes()):raise ValueError('unexpected public input bytes: '+path.name)
        return path
    if not entry['url'].startswith('https://atmos.nmsu.edu/pdsd/archive/'):
        raise ValueError('unexpected source host')
    context=ssl.create_default_context()
    try:import certifi
    except ImportError:pass
    else:context=ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(entry['url'],context=context,timeout=60) as response:blob=response.read()
    if not valid(blob):raise ValueError('download differs from pinned source: '+path.name)
    tmp=path.with_suffix(path.suffix+'.partial');tmp.write_bytes(blob);tmp.replace(path)
    return path

def main():
    root=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser()
    parser.add_argument('--input-cache',type=Path,default=root/'outputs/cassini_doppler_inputs')
    parser.add_argument('--output-dir',type=Path,default=root/'outputs/scalar_count_kernel_energy')
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True);args.input_cache.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((root/'scripts/cassini_count_window_inputs.json').read_text())
    inputs={name:verified_input(args.input_cache,entry) for name,entry in manifest['inputs'].items()}
    results={'count_energy':count.run_checks(),'inertial_energy':inertial.run_checks(),'development_timing':timing.run_checks(inputs,args.output_dir,manifest)}
    inv=results['development_timing'];groups=inv['groups']
    controls={
        'orbit_accounting':sum(inv['type_counts'].values())==inv['orbit_records']==91863,
        'doppler_accounting':inv['doppler_records_accounted']==91664 and not inv['unsupported'],
        'static_strata':inv['streams']==8 and len(groups)==8,
        'chain_accounting':inv['chains']==sum(g['chains'] for g in groups)==36,
        'nominal_duration':inv['duration_cs_counts']=={100:91664},
        'adjacency_and_gaps':sum(g['sorted_neighbor_relations'].get('adjacent',0) for g in groups)==91628 and sum(g['sorted_neighbor_relations'].get('gap',0) for g in groups)==28,
        'overlap_diagnostics':sum(g['sorted_neighbor_relations'].get('overlap_or_duplicate',0) for g in groups)==0,
        'synthetic_partition_controls':all(inv['self_checks'].values()),
    }
    assert all(controls.values()),controls
    products={}
    for name,result in results.items():
        dest=args.output_dir/(name+'.json');dest.write_text(json.dumps(result,indent=2)+'\n');products[name]=hashlib.sha256(dest.read_bytes()).hexdigest()
    sources=[Path(__file__).resolve()]+[root/p for p in AUDIT_INPUT_PATHS]
    summary={
        'actual_current_surface_status':'conditional-support','claim_type':'bounded_theorem',
        'checks':{'count_energy':results['count_energy']['checks_passed'],'inertial_energy':results['inertial_energy']['checks_passed']},
        'nominal_inventory_controls':controls,'nominal_inventory_controls_passed':sum(controls.values()),
        'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'product_sha256':products,'chain_ledger_sha256':inv['full_chain_ledger_sha256'],
        'exposed_development_doppler_rows':inv['doppler_records_accounted'],'exposed_development_chains':inv['chains'],
        'measured_gravity_tests':0,'fitted_parameters':0,'physical_energy_estimates':0,
        'scope':['Calibrated count kernels and a stable free scalar operator remain supplied.',
                 'Initial velocity and nuisance shapes are removed by derived contrasts, without selecting the field.',
                 'Mass and constant-velocity enclosures retain the full conformal time-derivative force.',
                 'Raw frequency variance is descriptive only; actual radio-to-force calibration is not inferred.',
                 'Accelerated/retarded geometry, field energy upper budgets and actual error bounds remain open.'],
    }
    (args.output_dir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
