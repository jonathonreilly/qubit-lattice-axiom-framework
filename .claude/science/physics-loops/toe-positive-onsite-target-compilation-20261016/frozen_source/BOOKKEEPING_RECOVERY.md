# Preserved documentation bookkeeping failure

A direct shell-tool `python3 -` documentation/context construction command returned exit1 with the complete tool-returned output below. This was after successful payload build and inspection. The command read and hash-checked the two exact actual parent publication/attachment files, copied them under parent_publication_context, and wrote OBSERVED_PARENT_PUBLICATION.json. It then read BODY_MAP, attempted to format a table using `r['source_alias']`, and failed because the actual key is `source`. SOURCE_BODY_READ_MAP.md had not yet been written. Existing proposal bytes, code and build/inspection receipts were untouched.

```
Traceback (most recent call last):
  File "<stdin>", line 23, in <module>
KeyError: 'source_alias'
```

The tool reported chunk97a2a6, wall_time_seconds0.121914292, exit_code1. This direct bookkeeping command did not use the metadata recorder: no separate stdout/stderr files, launch-source capture or precise start/end times were recorded, and none are reconstructed or claimed. The tool supplied the above combined output. Its relevant executed line was:

```python
lines.append('| '+r['name']+' | `'+r['source_alias']+'` | '+str(r['bytes'])+' | `'+r['sha256']+'` | ['+str(r['start_byte_inclusive'])+','+str(r['end_byte_exclusive'])+') |')
```

The complete issued stdin is preserved in bookkeeping_failure/issued_python_stdin.txt and the exact returned tool fields in bookkeeping_failure/TOOL_RESULT.json. This is a record copied from the actual tool invocation, explicitly not a retrospective launch-time source capture.

Recovery read the complete actual BODY_MAP and wrote SOURCE_BODY_READ_MAP.md directly from those identities; there was no rerun of the failed context-copy command and no overwrite of its two copied records or observation JSON. The sealer subsequently pins the complete final documentation/context contents. This event is distinct from the original failed root acceptance metadata recorder, whose actual full source capture and streams are preserved in the scientific source archive.
