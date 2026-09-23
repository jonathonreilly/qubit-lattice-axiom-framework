"""Validate actual execution evidence and source binding without rerunning science."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stream_objects(path):
    stream=Path(path).read_text();objects=[];decoder=json.JSONDecoder()
    while stream.strip():
        obj,end=decoder.raw_decode(stream.lstrip());objects.append(obj);stream=stream.lstrip()[end:]
    return objects


def main():
    assert not (HERE/'VALIDATION_RESULTS.json').exists()
    sources=json.loads((HERE/'SOURCE_IDENTITIES.json').read_text())
    for row in sources['science_sources']+sources['instruction_snapshots']:
        data=Path(row['path']).read_bytes()
        assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'],row['path']
    receipt_rows=[]
    for stem,exitcode in [('FILTER',0),('EXACT_INSTRUMENT',1),('EXACT_FIXED',0),('EXACT_CROSS',0),('SOURCE',0)]:
        receipt=json.loads((HERE/(stem+'_RECEIPT.json')).read_text())
        assert receipt['exit_code']==exitcode
        assert receipt['stdout_sha256']==digest(HERE/(stem+'.stdout'))
        assert receipt['stderr_sha256']==digest(HERE/(stem+'.stderr'))
        source=Path(receipt['command'][1])
        if stem=='EXACT_INSTRUMENT':source=HERE/'failed_attempts/sympy_json/exact_instrument_control.py'
        assert receipt['script_sha256']==digest(source)
        if exitcode==0:assert (HERE/(stem+'.stderr')).read_bytes()==b''
        else:assert 'TypeError: Object of type Integer is not JSON serializable' in (HERE/(stem+'.stderr')).read_text()
        receipt_rows.append({'stem':stem,'exit_code':exitcode,'source_version_verified':str(source),
                             'elapsed_seconds':receipt['elapsed_seconds']})
    filt=json.loads((HERE/'FILTER_RESULTS.json').read_text());fobjs=stream_objects(HERE/'FILTER.stdout')
    assert len(fobjs)==5 and fobjs[-1]==filt and fobjs[:-1]==filt['finite_filters']['rows']
    exact=json.loads((HERE/'EXACT_INSTRUMENT_RESULTS.json').read_text());eobjs=stream_objects(HERE/'EXACT_FIXED.stdout')
    assert len(eobjs)==2 and eobjs[-1]==exact
    assert eobjs[0]=={k:exact[k] for k in ('spin1_dimension','exact_shifted_Hamiltonian_factors')}
    cross=json.loads((HERE/'EXACT_CROSS_RESULTS.json').read_text())
    assert stream_objects(HERE/'EXACT_CROSS.stdout')==[cross]
    assert stream_objects(HERE/'SOURCE.stdout')==[sources]
    assert filt['source_sha256']==digest(HERE/'filter_controls.py')
    assert exact['source_sha256']==digest(HERE/'exact_instrument_control.py')
    assert cross['source_sha256']==digest(HERE/'exact_cross_gram.py')
    output={'source_sha256':digest(Path(__file__)),
            'science_source_bindings_verified':len(sources['science_sources']),
            'instruction_snapshots_verified':len(sources['instruction_snapshots']),
            'actual_receipts':receipt_rows,
            'complete_stdout_json_objects_verified':{'FILTER':len(fobjs),'EXACT_FIXED':len(eobjs),'EXACT_CROSS':1,'SOURCE':1},
            'numeric_counterexample_max_sharp_loss_difference':max(r['sharp_total_coherent_resolved_loss_difference_norm'] for r in filt['finite_filters']['rows']),
            'exact_counterexample_nonzero_entries':len(cross['coherent_minus_resolved_loss_without_kappa']),
            'source_read_boundary':'No new author or unrelated root research opened; only declared prior source identities checked.',
            'status':'Evidence consistency verified; this does not substitute for the analytic proof or an independent formal audit.'}
    (HERE/'VALIDATION_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':main()
