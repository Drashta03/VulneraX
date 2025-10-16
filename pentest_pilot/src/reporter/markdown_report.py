import json, os

def generate_markdown_report(results_file: str, out_md: str):
    lines = []
    with open(results_file) as f:
        for l in f:
            lines.append(json.loads(l))
    with open(out_md, 'w') as o:
        o.write('# Pentest Pilot Report\n\n')
        for r in lines:
            o.write('## Command\n')
            o.write('```\n')
            o.write(r.get('command','') + '\n')
            o.write('```\n\n')
            o.write('### Output\n')
            o.write('```\n')
            o.write((r.get('output') or '')[:2000] + '\n')
            o.write('```\n\n')
