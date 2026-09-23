def _finite(value):
    if isinstance(value, float) and (not math.isfinite(value)):
        raise AssertionError('nonfinite output')
    if isinstance(value, dict):
        for item in value.values():
            _finite(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _finite(item)

def _emit(out, expected, scopes):
    assert out['TOTAL'] == expected == len(set(out['checks']))
    assert 0 < _rss() < AUDIT_RSS_LIMIT_MIB
    assert time.monotonic() - _started < AUDIT_TIMEOUT_SEC
    assert sum((v['checks'] for v in scopes.values())) == expected
    out['N5_scopes'] = scopes
    out['resource_limits'] = {'seconds': AUDIT_TIMEOUT_SEC, 'rss_MiB': AUDIT_RSS_LIMIT_MIB}
    out['input_sha256'] = _input_sha256
    _finite(out)
    _sidecar = os.environ.get('AUDIT_RESULT_SIDECAR')
    if _sidecar:
        _result_path = Path(_sidecar)
        if not _result_path.is_absolute() or _result_path.resolve().is_relative_to(_REPO_ROOT.resolve()):
            raise ValueError('AUDIT_RESULT_SIDECAR must be an absolute path outside the repository')
        with _result_path.open('x') as _result_file:
            json.dump(out, _result_file, sort_keys=True, indent=2, allow_nan=False)
            _result_file.write('\n')
    if sys.argv[1:] == ['--json']:
        print(json.dumps(out, sort_keys=True, indent=2, allow_nan=False))
    else:
        print('PASS ' + Path(__file__).name)
        for key, item in scopes.items():
            print(key + ': ' + str(item['checks']) + ' checks; ' + item['scope'])
        print('TOTAL: ' + str(expected))
        print('seconds: ' + str(out['seconds']) + '; rss_MiB: ' + str(out['rss_MiB']))
        print('source_sha256: ' + out['source_sha256'])
    signal.alarm(0)
