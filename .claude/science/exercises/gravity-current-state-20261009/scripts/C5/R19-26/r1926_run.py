"""R19-26: run an UNMODIFIED R19-9 script from orig/ against the RE-PLACED kernel (lib1916 repairs R0/R1/R2 + lib1926 placement).
Usage: python3 r1926_run.py <script in orig/> [args...]"""
import os, sys, runpy
import lib1926
lib1926.patch()
HERE = os.path.dirname(os.path.abspath(__file__))
script = os.path.join(HERE, 'orig', sys.argv[1])
sys.argv = [script] + sys.argv[2:]
print(f'[r1926_run] {os.path.basename(script)} {" ".join(sys.argv[1:])} with the RE-PLACED kernel (lib1916 R0/R1/R2 + lib1926 F(q_i)F(q_j) on off-diagonal VW)', flush=True)
runpy.run_path(script, run_name='__main__')
