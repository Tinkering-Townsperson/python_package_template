import os
import shutil
import subprocess
import sys

# DEPENDENCIES =
DEV_DEPENDENCIES = '{{cookiecutter.dev_dependencies}}'
INCLUDE_GITHUB_ACTIONS = {% if cookiecutter.include_github_actions %}True{% else %}False{% endif %}
INCLUDE_DEPENDABOT = {% if cookiecutter.include_dependabot %}True{% else %}False{% endif %}
PACKAGE_SLUG = "{{cookiecutter.__package_slug}}"

remove_paths = set([])
CHECK_FOR_EMPTY_DIRS = ['.github']

if not INCLUDE_GITHUB_ACTIONS:
	remove_paths.add('.github/workflows')

if not INCLUDE_DEPENDABOT:
	remove_paths.add('.github/dependabot.yml')


for path in remove_paths:
	path = path.strip()
	if path and os.path.exists(path):
		if os.path.isdir(path):
			shutil.rmtree(path)
		else:
			os.unlink(path)

# Check for empty directories
for path in CHECK_FOR_EMPTY_DIRS:
	path = path.strip()
	if path and os.path.exists(path) and os.path.isdir(path) and len(os.listdir(path)) == 0:
		shutil.rmtree(path)


def run_command(command):
	print(f"\x1b[1;3;97mRunning '{command}'\x1b[0m")
	process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, )
	for c in iter(lambda: process.stdout.read(1), b""):
		sys.stdout.buffer.write(c)

	returncode = process.wait()
	if returncode != 0:
		print(f"\x1b[1;3;33mFailed to run command '{command}': {returncode}\x1b[0m")
		sys.exit(returncode)

run_command("git init")
run_command("make venv")

# if DEPENDENCIES and DEPENDENCIES != " ":
# 	run_command(f"poetry add {DEPENDENCIES} --no-interaction")
# if DEPENDENCIES and DEV_DEPENDENCIES != " ":
# 	run_command(f"poetry add {DEV_DEPENDENCIES} --group=dev --no-interaction")

match DEV_DEPENDENCIES:
	case "Default":
		for pkg in ("build", "flake8", "pytest", "twine", "wheel"):
			run_command(f"poetry add {pkg} --group=dev --no-interaction")

run_command("make install-dev clean")
