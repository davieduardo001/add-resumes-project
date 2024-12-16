@echo off

python --version >nul 2>&1

IF %ERRORLEVEL% NEQ 0 (
    echo Python not found. Opening the Microsoft Store...
    start python
) ELSE (
    echo Python is already installed.

    IF NOT EXIST "venv\Scripts\activate" (
        echo Virtual environment not found. Creating and activating the virtual environment...
        python -m venv venv
    ) ELSE (
        echo Virtual environment already exists. Activating the virtual environment...
    )

    call venv\Scripts\activate

    python -m pip install --upgrade pip

    python -m pip install playwright openpyxl

    python -m playwright install

    echo Dependencies successfully installed in the virtual environment!

    echo Running main.py...
    python main.py
)

pause
