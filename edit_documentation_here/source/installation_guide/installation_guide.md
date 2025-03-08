# Installation

The developer version of InVesalius runs on Windows, macOS, and Linux operating systems.
On this page, instructions for installing and running InVesalius on these systems can be found.

## Windows

These instructions are tested on Windows 10 64-bit.
The packages required by InVesalius can be installed either through a Python system
installation, the Anaconda package manager, or using `uv`.
In all cases, the following prerequisites apply:

### Prerequisites

- Visual Studio (We are using the 2019 community edition).
  - It's possible to install using [chocolatey](https://chocolatey.org/):
    ```shell
     choco install -y visualstudio2019buildtools
     choco install -y visualstudio2019-workload-vctools
    ```
- Download InVesalius source code.
  ```bash
  git clone --recurse-submodules https://github.com/invesalius/invesalius3
  ```

## Installation Options

### Option 1: Using `uv` (Recommended)

`uv` is a modern Python package manager that ensures better dependency management. Follow these steps:

1. Install `uv` on Windows using:

   ```shell
   scoop install main/uv
   ```

2. Navigate to the cloned InVesalius directory:

   ```shell
   cd invesalius3
   ```

3. Install dependencies and compile Cython extensions automatically:

   ```shell
   uv pip install -e .
   ```

4. To install additional dependencies, use:

   ```shell
   uv add <dependency-name>
   ```

5. Run InVesalius:
   ```shell
   uv run app.py
   ```

### Option 2: Python System Installation

1. Download and install Python 3.8 from the [Python website](https://www.python.org/downloads/).

2. Install InVesalius main dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

3. If you are going to use the neuronavigation features, install the wrappers for tracking devices:

   ```shell
   pip install pyclaron polhemusFT polhemus pypolaris pypolarisP4
   ```

4. **Optional:** To enable real-time tractography computation, install [Trekker](https://dmritrekker.github.io/):
   ```shell
   pip install https://github.com/dmritrekker/trekker/raw/master/binaries/Trekker-0.9-cp38-cp38-win_amd64.whl
   ```

### Option 3: Anaconda Installation

1. Install [Anaconda](https://www.anaconda.com/products/individual), preferably the 64-bit version.

2. In the Anaconda Powershell, navigate to the cloned InVesalius source code folder:

   ```shell
   cd C:\Users\%USERNAME%\repository\invesalius3\
   ```

3. Install the required packages:

   ```shell
   conda env create -f environment.yml --name invesalius
   ```

4. Activate the virtual environment:
   ```shell
   conda activate invesalius
   ```

### Compiling InVesalius (For Python System & Anaconda Installations)

Some algorithms of InVesalius are written in Cython for performance. These need to be compiled manually.
Open the Visual Studio command prompt, navigate to the InVesalius directory, and compile:

```shell
python setup.py build_ext --inplace
```

(Note: If using `uv`, this step is not required as `scikit-build-core` and `cmake` handle it automatically.)

### Running InVesalius

Inside the InVesalius source code directory, run:

```shell
python app.py
```

If using `uv`, simply run:

```shell
uv run app.py
```

**Warning:** If using Anaconda, always open the Anaconda Powershell and activate the environment before running the command.
