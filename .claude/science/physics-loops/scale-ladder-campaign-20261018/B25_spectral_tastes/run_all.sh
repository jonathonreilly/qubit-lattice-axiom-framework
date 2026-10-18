#!/bin/bash
# B25 runners in dependency order (census.pkl feeds pin_audit and fourier_check).  ~25 min on 4 cores.
cd "$(dirname "$0")"
python3 letter_rules.py > letter_rules.log 2>&1
python3 census.py 4 > census.log 2>&1
python3 pin_audit.py > pin_audit.log 2>&1
python3 kdep_mechanism.py > kdep_mechanism.log 2>&1
python3 fourier_check.py > fourier_check.log 2>&1
./run_screens.sh
grep -h TOTAL letter_rules.log census.log pin_audit.log kdep_mechanism.log fourier_check.log screen25_S.log screen25_S2.log screen25_S4.log
