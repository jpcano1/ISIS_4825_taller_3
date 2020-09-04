@echo off

if "%ENV%"=="" (
    echo Por favor, crear la variable ENV
) else (
    :: Vamos a activar el entorno virtual de anaconda
    :: Si la siguiente no es la ruta de su instalación
    :: Por favor cambiarla
    :: "%HOMEPATH%/anaconda3/Scripts/activate"
    
    if not exist "%cd%/%ENV%" (
        pip install virtualenv
        virtualenv "%ENV%"
        "%ENV%/Scripts/activate"
        pip install -r requirements.txt
    )

    "%ENV%/Scripts/activate"
    python -m ipykernel install --user --name="%ENV%"
    jupyter notebook
    :: echo y | jupyter kernelspec uninstall "%ENV%"
    "%ENV%/Scripts/deactivate"
    conda deactivate
)

PAUSE