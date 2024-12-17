import subprocess
import re


policies_that_work = ["RemoteSigned", "Unrestricted", "Bypass"]

def find_python_versions():
    command = "py -0"
    result = subprocess.run(command, capture_output=True, text=True).stdout
    version_pattern = r'\d+\.\d+'

    versions = list(set(re.findall(version_pattern, result)))
    return versions

def check_execution_policy():
    command = "powershell Get-ExecutionPolicy"
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

def change_execution_policy():
    command = "set-executionpolicy remotesigned -Scope CurrentUser -Force"
    subprocess.run(["powershell", "-Command", command], check=True)
    print(f"Execution Policy changed")

def create_venv(version, venv_name, venv_directory):
    command = f"cd {venv_directory} && py -{version} -m venv {venv_name}"
    subprocess.run(command, shell=True, check=True)
    print(f"Created {venv_name} Python version {version} at {venv_directory}")