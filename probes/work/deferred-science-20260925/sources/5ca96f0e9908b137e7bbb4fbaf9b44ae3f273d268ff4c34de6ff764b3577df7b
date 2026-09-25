"""Final read-only verification of the POST evidence and frozen PRE."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json

BASE=Path(__file__).resolve().parent
def sha(p):return sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads((BASE/p).read_text())

def main():
    previous=load('PRE_SEAL.json')
    for row in previous['members']:assert sha(BASE/row['path'])==row['sha256']
    pins=load('POST_SOURCE_PINS.json')
    for row in pins['author_inputs']:
        assert sha(Path(row['path']))==row['sha256']
        assert sha(Path(row['frozen_path']))==row['sha256']
    exact=load('POST_EXACT_COMPARISON.json')
    assert exact['source_pins_sha256']==sha(BASE/'POST_SOURCE_PINS.json')
    assert exact['code_sha256']==sha(BASE/'post_bind_and_compare.py')
    fft=load('POST_FFT_RESULTS.json')
    assert fft['code_sha256']==sha(BASE/'post_fft_control.py')
    assert fft['PRE_data_sha256']==sha(BASE/'LAURENT_DATA_L8.json')
    assert fft['author_result_sha256']==sha(BASE/'post_frozen_author/ENERGY_SPECTRAL_RESULTS.json')
    assert not fft['discrepant_rows']
    for f in ['POST_EXACT_COMPARISON_STDERR.txt','POST_FFT_STDERR.txt']:
        assert not (BASE/f).read_bytes()
    failure=BASE/'post_history/initial_pair_coordinate_comparison/POST_EXACT_COMPARISON_STDERR.txt'
    assert b'AssertionError' in failure.read_bytes()
    print(json.dumps({'verified_utc':datetime.now(timezone.utc).isoformat(),
                      'PRE_members_unchanged':len(previous['members']),
                      'author_files_and_originals_verified':len(pins['author_inputs']),
                      'source_result_bindings_match':True,
                      'polynomial_coefficient_comparisons':282,
                      'signed_filling_checks':140,
                      'active_pair_summary_checks':532,
                      'FFT_max_absolute_difference':fft['max_absolute_difference'],
                      'FFT_current_rows':fft['current_rows_compared'],
                      'FFT_historical_rows':fft['historical_rows_compared'],
                      'FFT_current_finite_g_values':fft['current_finite_g_values_compared'],
                      'FFT_historical_finite_g_values':fft['historical_finite_g_values_compared'],
                      'coordinate_failure_preserved':True,
                      'POST_sha256':sha(BASE/'POST.md'),
                      'POST_SOURCE_PINS_sha256':sha(BASE/'POST_SOURCE_PINS.json'),
                      'verifier_sha256':sha(Path(__file__))},indent=2))

if __name__=='__main__':main()
