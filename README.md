# flask-cicd-lab

Flask demo app for the GitHub Actions CI/CD labs (Dr. Prashant Dey).

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -v          # 5 tests
python app.py      # http://localhost:5000
```

Reference answers (copy into `.github/workflows/` during the labs):
- `1-ssh-connect.yml`   - SSH connection test (manual run)
- `2-deploy-ec2.yml`    - test, then deploy with gunicorn on port 5000
- `3-deploy-docker.yml` - test, build + push to Docker Hub, run container on port 80
