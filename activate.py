import os
import subprocess
import sys

def create_and_activate_venv():
  sys_exec = sys.executable
  venv_dir = '.venv'

  # Determine the correct command for creating a virtual environment
  venv_command = [sys_exec, '-m', 'venv', venv_dir]

  # Create the virtual environment
  subprocess.run(venv_command, check=True)

  # Install the requirements
  # Install the requirements inside the virtual environment
  if os.name == 'nt':  # Windows
    pip_install_command = rf'.\{venv_dir}\Scripts\python.exe -m pip install --upgrade -r requirements.txt'
  else:  # Linux and MacOS
    pip_install_command = f'./{venv_dir}/bin/python -m pip install --upgrade -r requirements.txt'

  subprocess.run(pip_install_command, shell=True, check=True)

  # Determine the correct activation command based on the OS
  if os.name == 'nt':  # Windows
    activate_command = rf'.\{venv_dir}\Scripts\activate'
  else:  # Linux and MacOS
    activate_command = f'. ./{venv_dir}/bin/activate'

  # Print the activation command for the user to run manually
  print(f"\nRun the following command to activate the virtual environment:\n{activate_command}\n")


if __name__ == '__main__':
  create_and_activate_venv()