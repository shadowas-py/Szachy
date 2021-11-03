rmdir VEnv\ /S /Q
python -m venv VEnv\
call VEnv\Scripts\activate.bat

pip install pygame

call deactivate
