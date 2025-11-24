# Release Instructions

Complete guide for building, testing, and publishing pyDefine to PyPI.

---

## 📋 Pre-Release Checklist

- [ ] All tests passing locally: `pytest`
- [ ] Code formatted: `black pydefine/ tests/`
- [ ] Linting clean: `ruff check pydefine/`
- [ ] Type checking: `mypy pydefine/`
- [ ] Documentation updated
- [ ] CHANGELOG.md updated with version and date
- [ ] Version bumped in `pyproject.toml` and `pydefine/version.py`
- [ ] All examples tested
- [ ] README.md accurate

---

## 🔢 Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR:** Breaking changes
- **MINOR:** New features (backward compatible)
- **PATCH:** Bug fixes

**Examples:**
- `1.0.0` → `1.0.1` (bug fix)
- `1.0.1` → `1.1.0` (new feature)
- `1.1.0` → `2.0.0` (breaking change)

---

## 🛠️ Step 1: Update Version

### Update `pydefine/version.py`

version = "1.0.1" # Update version

### Update `pyproject.toml`
[project]
version = "1.0.1" # Update version


### Update `CHANGELOG.md`

[1.0.1] - 2025-11-25
Fixed
Fixed bug in exception parsing

Improved error messages

Added
New exception type support


---

## 🧪 Step 2: Test Locally

Run full test suite
pytest -v

Run with coverage
pytest --cov=pydefine --cov-report=html

Test examples
python examples/example_usage.py
python examples/example_safe_run.py

Test CLI
pydefine --help
pydefine --list


---

## 📦 Step 3: Build Distribution

### Clean Previous Builds

rm -rf build/ dist/ *.egg-info

### Build Wheel and Source Distribution


python -m pip install --upgrade build
python -m build

This creates:
- `dist/pydefine-1.0.1-py3-none-any.whl` (wheel)
- `dist/pydefine-1.0.1.tar.gz` (source)

### Verify Build


ls -lh dist/

Should see .whl and .tar.gz files
Check package contents
tar -tzf dist/pydefine-1.0.1.tar.gz | head -20

---

## 🧪 Step 4: Test on TestPyPI

### Install Twine


pip install --upgrade twine

### Upload to TestPyPI


python -m twine upload --repository testpypi dist/*

**Credentials:**
- Username: `__token__`
- Password: Your TestPyPI API token

### Test Installation from TestPyPI


Create fresh environment
python -m venv test_env
source test_env/bin/activate

Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ pydefine

Test it works
python -c "import pydefine; print(pydefine.version)"

Test basic functionality
python -c "import pydefine; print(pydefine.explain('1/0'))"

Deactivate and remove test environment
deactivate
rm -rf test_env


---

## 🚀 Step 5: Upload to PyPI

### Upload to Production PyPI


python -m twine upload dist/*


**Credentials:**
- Username: `__token__`
- Password: Your PyPI API token

### Verify Upload

Check on PyPI
open https://pypi.org/project/pydefine/

Install from PyPI
pip install pydefine

Test installation
python -c "import pydefine; print(pydefine.version)"


---

## 🏷️ Step 6: Git Tagging

### Commit Changes


git add .
git commit -m "Release version 1.0.1"


### Create Git Tag


git tag -a v1.0.1 -m "Release version 1.0.1"
git push origin main
git push origin v1.0.1


### Create GitHub Release

1. Go to: https://github.com/mdyahhya/pydefine/releases/new
2. Tag: `v1.0.1`
3. Title: `pyDefine v1.0.1`
4. Description: Copy from CHANGELOG.md
5. Attach `dist/` files
6. Publish release

---

## 🤖 Step 7: Automated Publishing (Optional)

### GitHub Actions Auto-Publish

Create `.github/workflows/publish.yml`:

name: Publish to PyPI

on:
release:
types: [published]

jobs:
deploy:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v3
- name: Set up Python
uses: actions/setup-python@v4
with:
python-version: '3.10'
- name: Install dependencies
run: |
python -m pip install --upgrade pip
pip install build twine
- name: Build package
run: python -m build
- name: Publish to PyPI
env:
TWINE_USERNAME: token
TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
run: twine upload dist/*


**Setup:**
1. Generate PyPI API token
2. Add to GitHub Secrets as `PYPI_API_TOKEN`
3. Push tag to trigger workflow

---

## 📢 Step 8: Announce Release

### Update Documentation

- [ ] Update README badges if needed
- [ ] Update documentation site (if exists)
- [ ] Update examples if API changed

### Social Media

- [ ] Twitter/X announcement
- [ ] LinkedIn post
- [ ] Dev.to article
- [ ] Reddit r/Python post

### Community

- [ ] Update project website
- [ ] Notify contributors
- [ ] Email notification list
- [ ] Discord/Slack announcement

---

## 🔥 Rollback Procedure

If critical bug found after release:

### 1. Yank Bad Release

pip install --upgrade twine
twine upload --skip-existing dist/* # Re-upload if needed


On PyPI web interface: Mark release as "yanked"

### 2. Release Hotfix

Fix the bug
Update version to 1.0.2
Follow release process
Mark as hotfix in CHANGELOG


### 3. Notify Users

- GitHub issue
- Release notes
- Social media
- Email if critical security issue

---

## 📊 Post-Release Monitoring

### Check Metrics

- PyPI download statistics
- GitHub stars/forks
- Issue reports
- User feedback

### Monitor for Issues


Check PyPI status
curl https://pypi.org/pypi/pydefine/json | python -m json.tool

Monitor GitHub issues
open https://github.com/mdyahhya/pydefine/issues


---

## 🔑 API Token Setup

### Create PyPI Token

1. Visit: https://pypi.org/manage/account/token/
2. Create token with scope for `pydefine` project
3. Save securely (you can't see it again!)

### Create TestPyPI Token

1. Visit: https://test.pypi.org/manage/account/token/
2. Create token with scope for `pydefine` project
3. Save securely

### Configure `~/.pypirc` (Optional)


[distutils]
index-servers =
pypi
testpypi

[pypi]
username = token
password = pypi-YOUR_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = token
password = pypi-YOUR_TESTPYPI_TOKEN_HERE


**⚠️ Security:** Never commit `.pypirc` to git!

---

## ✅ Release Verification Checklist

After release:

- [ ] Package visible on PyPI
- [ ] `pip install pydefine` works
- [ ] Version number correct
- [ ] README displays correctly on PyPI
- [ ] All files included in package
- [ ] CLI commands work
- [ ] Examples run without errors
- [ ] Documentation links work
- [ ] GitHub release created
- [ ] Git tag pushed

---

**✨ Congratulations on releasing pyDefine! ✨**

Created by Yahya

