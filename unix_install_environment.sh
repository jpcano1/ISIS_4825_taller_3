#!/bin/bash
if [ -z "$ENV" ]; then
  echo "No Existe ENV, por favor crear esta variable"
else
  if [ ! -d "$ENV" ]
  then
    pip install virtualenv
    virtualenv $ENV
    source $ENV/bin/activate
    pip install -r requirements.txt
  fi

  source $ENV/bin/activate
  if [[ ! $(pip list | grep -w "\<ipykernel\>") ]]; then
    pip install ipykernel
  fi
  python -m ipykernel install --user --name=$ENV
  jupyter notebook
  echo y | jupyter kernelspec uninstall $ENV
  deactivate
fi