# Preserved orchestration parse failure

One pre-seal functions.exec call failed before execution. Its intended
operations were creating EVIDENCE_LOG.md, CHECKPOINT.md and seal_pre.py using
apply_patch, then invoking the new seal program. The JavaScript template
literal contained unescaped Markdown backticks. The tool's complete output:

    Script failed
    Wall time 0.0 seconds
    Output:
    Script error:
    SyntaxError: missing ) after argument list

No nested tool, patch or subprocess ran. No seal or scientific file was
created or modified by that failed call. The retry removes the offending
Markdown backticks and includes this failure record. This was not a
scientific control failure and no numerical row was discarded or rerun.
