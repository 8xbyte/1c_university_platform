for /d /r %%i in (__pycache__) do (
    rd /s /q "%%i"
)

rd /s /q ".venv"

pip uninstall poetry -y
pip install poetry

install.bat