#!/bin/sh

# Install Jupyter kernel for Python 3.12
pip install ipykernel
python -m ipykernel install --name=spilli --display-name="SpiLLI"
pip install jupyterlab
# Start Jupyter server with VS Code compatible settings
jupyter lab --ip='*' --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.iopub_data_rate_limit=10000000