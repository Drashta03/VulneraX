import subprocess, shlex, os, datetime

def run_nuclei(target_file: str, templates_dir: str, outdir='./logs'):
    os.makedirs(outdir, exist_ok=True)
    ts = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
    out = f"{outdir}/nuclei_{ts}.json"
    cmd = f"nuclei -l {target_file} -t {templates_dir} -o {out} -json"
    proc = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
    return proc.returncode, out, proc.stdout, proc.stderr
