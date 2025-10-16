# Pentest Pilot — AI-Assisted Penetration Testing (Complete Scaffold)

**Owner:** Mysterio
**Assistant:** Hagrid

This repo is a development scaffold for an AI-assisted penetration testing tool.
It is intended for development and authorized testing only (DVWA, Juice Shop, or isolated lab VMs).

## Quickstart (development)

1. Copy `.env.example` to `.env` and add your OpenAI API key.
   ```bash
   cp .env.example .env
   # edit .env and set OPENAI_API_KEY and LOG_DIR
   ```
2. Create a Python 3.12 virtual environment and install dependencies:
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the app (interactive mode):
   ```bash
   python start.py
   ```

## Pushing to GitHub
I cannot push to your GitHub for you. Follow these steps locally to publish:

1. Create a new repo on GitHub (via web UI or `gh repo create`).
2. Initialize git, add remote and push:
   ```bash
   git init
   git add .
   git commit -m "Initial Pentest Pilot scaffold"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo>.git
   git push -u origin main
   ```
3. (Optional) Enable GitHub Actions -> the included workflow will run tests on push.

## Recommended next tasks
- Review `prompts.py` and ensure they align with safe, authorized testing.
- Install external tool dependencies when integrating connectors (nmap, ffuf, nuclei).
- Run unit tests: `pytest -q`.

## Warning
Never run this tool against systems you don't own or have written authorization to test.
