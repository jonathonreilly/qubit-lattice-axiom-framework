#!/usr/bin/env python3
"""Reproduce one exposed Cassini count conversion and conditional phase bounds.

Reads pinned public PDS ODF/ATDF bytes and labels, downloading them if absent.
These external scientific inputs are hash-checked against the tracked manifest.
Package-local integrity reads are the manifest and source hashes in helpers.
All writes are beneath outputs/cassini_doppler_* or a requested output directory.
This is precursor/processed-data consistency, not independent gravity evidence.
"""
import argparse
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import ssl
import sys
import urllib.request

import cassini_odf_decode as odf
import cassini_atdf_decode as atdf
import cassini_ramp_phase as ramp
import cassini_finite_count_endpoint_check as endpoint
import cassini_atdf_odf_reconcile as reconcile

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = [
    'docs/CASSINI_DOPPLER_COUNT_STATION_TIME_BOUNDED_THEOREM_NOTE_2026-10-14.md',
    'scripts/cassini_doppler_development_inputs.json',
    'scripts/cassini_odf_decode.py',
    'scripts/cassini_atdf_decode.py',
    'scripts/cassini_ramp_phase.py',
    'scripts/cassini_finite_count_endpoint_check.py',
    'scripts/cassini_atdf_odf_reconcile.py',
    '.claude/science/physics-loops/observations-backward-24h-20261014/RAW_DATA_PROTOCOL_v1.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/RAW_DATA_PROTOCOL_v2_ATDF.json',
]


def verified_input(cache, entry):
    path = cache/entry['filename']
    def valid(blob):
        return len(blob)==entry['bytes'] and hashlib.sha256(blob).hexdigest()==entry['sha256']
    if path.exists():
        if not valid(path.read_bytes()):
            raise ValueError('existing public input has unexpected bytes: '+path.name)
        return path
    context = ssl.create_default_context()
    try:
        import certifi
    except ImportError:
        pass
    else:
        context = ssl.create_default_context(cafile=certifi.where())
    if not entry['url'].startswith('https://atmos.nmsu.edu/pdsd/archive/'):
        raise ValueError('unexpected source host')
    with urllib.request.urlopen(entry['url'], context=context, timeout=60) as response:
        blob = response.read()
    if not valid(blob):
        raise ValueError('download does not match registered source '+path.name)
    temporary = path.with_suffix(path.suffix+'.partial')
    temporary.write_bytes(blob)
    temporary.replace(path)
    return path


def run_helper(module, arguments):
    previous = sys.argv
    try:
        sys.argv = [module.__file__]+[str(x) for x in arguments]
        with redirect_stdout(io.StringIO()):
            module.main()
    finally:
        sys.argv = previous


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-cache',type=Path,default=root/'outputs/cassini_doppler_inputs')
    parser.add_argument('--output-dir',type=Path,default=root/'outputs/cassini_doppler_bridge')
    args = parser.parse_args()
    args.input_cache.mkdir(parents=True,exist_ok=True)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    manifest_path = root/'scripts/cassini_doppler_development_inputs.json'
    manifest = json.loads(manifest_path.read_text())
    inputs = {name:verified_input(args.input_cache, entry) for name,entry in manifest['inputs'].items()}
    jobs = [
        (odf,['--odf',inputs['odf'],'--label',inputs['odf_label']],'odf_inventory.json'),
        (atdf,['--tdf',inputs['tdf'],'--label',inputs['tdf_label']],'atdf_inventory.json'),
        (ramp,['--odf',inputs['odf'],'--label',inputs['odf_label']],'ramp_integration.json'),
        (endpoint,[],'endpoint_controls.json'),
        (reconcile,['--tdf',inputs['tdf'],'--tdf-label',inputs['tdf_label'],'--odf',inputs['odf'],
                    '--rows-output',args.output_dir/'all_doppler_rows.jsonl'],'reconciliation.json')]
    products={}
    for module,arguments,filename in jobs:
        output=args.output_dir/filename
        run_helper(module,arguments+['--output',output])
        products[filename]=json.loads(output.read_text())
    rr=products['reconciliation.json']
    endpoints=products['endpoint_controls.json']
    ramps=products['ramp_integration.json']
    tests={
        'all_registered_doppler_rows_accounted':sum(rr['outcome_counts'].values())==91664,
        'all_rows_in_declared_conversion_domain':rr['outcome_counts']=={'reconstructed_conditional_lift':91664},
        'comparison_with_processed_data':rr['counters']['mismatches']==0,
        'wrong_label_scale_discriminated':rr['counters']['wrong_label_scale_mismatches']==999,
        'omitted_rollovers_discriminated':rr['counters']['omitted_rollover_mismatches']==21,
        'wrong_bias_discriminated':rr['counters']['wrong_bias_mismatches']==91664,
        'reverse_count_discriminated':rr['counters']['reverse_count_mismatches']==91664,
        'oneway_reference_discriminated':rr['counters']['omitted_oneway_reference_mismatches']==649,
        'finite_count_endpoint_controls':endpoints['failed']==0 and endpoints['passed']==526,
        'ramp_controls':all(ramps['self_checks'].values()),
        'count_controls':all(rr['self_checks'].values()),
    }
    boundaries=[b for st in ramps['ramp_stations'] for b in st['boundaries']]
    summary=dict(status='conditional-support',role='instrument reconstruction and conditional phase mathematics',
        source_manifest_sha256=hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        tests=tests,passed=sum(tests.values()),failed=sum(not value for value in tests.values()),
        processed_doppler_records=sum(rr['outcome_counts'].values()),
        measured_gravity_tests=0,fitted_parameters=0,
        endpoint_synthetic_checks=endpoints['passed'],ramp_synthetic_checks=len(ramps['self_checks']),
        count_synthetic_checks=len(rr['self_checks']),
        reconstruction_counters=rr['counters'],
        endpoint_occurrences_with_nonzero_slip_diagnostic=sum(
            row['occurrences'] for row in rr['endpoint_quality_occurrences']
            if row['values'][rr['mode_quality_field_order'].index(87)]!=0),
        endpoint_occurrences=sum(row['occurrences'] for row in rr['endpoint_quality_occurrences']),
        maximum_reconstruction_difference_hz=max(g['max_abs_error_hz']['approximate'] for g in rr['groups']),
        ramp_records=sum(st['records'] for st in ramps['ramp_stations']),
        ramp_gaps=sum(b['gap_ns']>0 for b in boundaries),
        nonzero_contiguous_frequency_jumps=sum(b['gap_ns']==0 and b['endpoint_frequency_difference_hz']['numerator']!=0 for b in boundaries),
        source_rows_sha256=rr['all_rows_sha256'],
        product_sha256={filename:hashlib.sha256((args.output_dir/filename).read_bytes()).hexdigest() for _,_,filename in jobs},
        scope=['Same-track precursor comparison is development reconstruction, not an independent experiment.',
               'Forward modulo lift retains a bounded increment/no-reset condition; multiple full wraps share endpoint bytes.',
               'Count differences at microhertz level do not establish instrumental accuracy.',
               'No scalar action, state, scale, source profile, trajectory, clock precision, or plasma correction is fitted or derived.'])
    (args.output_dir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    return int(summary['failed']!=0)


if __name__=='__main__':
    raise SystemExit(main())
