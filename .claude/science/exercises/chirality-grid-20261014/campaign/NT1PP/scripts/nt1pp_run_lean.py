"""NT-1'' driver: run an E2-type script with the lean dq_dA patched in. usage: python3 nt1pp_run_lean.py script.py args..."""
import sys, runpy
import nt1pp_lean; nt1pp_lean.patch()
sys.argv = sys.argv[1:]
runpy.run_path(sys.argv[0], run_name='__main__')
