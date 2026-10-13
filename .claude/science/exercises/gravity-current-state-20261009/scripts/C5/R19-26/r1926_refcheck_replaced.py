"""R19-26: the R19-16 referee's script (ref_cut_check.py = scratchpad/C5/ref_R19-16/independent_R19_16_check.py, unmodified copy)
run against the RE-PLACED kernel.  Its 'kernel jump' is the RAW max over all (mu, nu) of the tilde kernel and so includes the
sign flips that R9-9's placement REQUIRES of M^{0x}, M^{xy}, M^{xz} at the q_x cut (see r1926_diag.out); its 'M02' (= M^{0y},
placement sign +1 at a q_x cut) is a valid continuity test."""
import runpy, lib1926
lib1926.patch()
runpy.run_path('ref_cut_check.py', run_name='__main__')
