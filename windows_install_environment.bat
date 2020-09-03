@echo off

if "%ENV%"=="" (
    echo Variable no definida
) else (
    if not exist "%cd%/%ENV%" (
        pip install virtualenv
        virtualenv "%ENV%"
        "%ENV%/Scripts/activate"
        pip install -r requirements.txt
    )

    "%ENV%/Scripts/activate"
    python -m ipykernel install --user --name="%ENV%"
    jupyter notebook
    echo y | jupyter kernelspec uninstall "%ENV%"
    "%ENV%/Scripts/deactivate"
)

PAUSE