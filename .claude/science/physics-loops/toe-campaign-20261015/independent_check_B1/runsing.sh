#!/bin/bash
# usage: runsing.sh file.sing  (runs Singular from the extracted passagemath wheel)
D=/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_check/sing
LD_LIBRARY_PATH=$D/passagemath_singular.libs SINGULARPATH=$D/sage_wheels/share/singular/LIB $D/sage_wheels/bin/Singular -q "$@"
