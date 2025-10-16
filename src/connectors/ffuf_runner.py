import subprocess, shlex, os, datetime

def run_ffuf(target_url: str, wordlist: str, outdir='./logs'):
    os.makedirs(outdir, exist_ok=True)
    ts = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
    out = f"{outdir}/ffuf_{ts}.json"
    cmd = f"ffuf -u {target_url} -w {wordlist} -o {out} -of json"
    proc = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
    return proc.returncode, out, proc.stdout, proc.stderr
