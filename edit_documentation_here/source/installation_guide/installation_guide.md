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

## MacOS

This guide is based on **High Sierra**.

### Prerequisites

The first step is the installation of **homebrew**.
Access the homebrew site to know how to [install it](http://brew.sh/).

We recommend installing Python 3 from brew, and also installing **OpenMP** (we use it):

```sh
brew install python3 libomp
```

If you are working with an Apple Silicon Mac, you also have to install `hdf5`:

```sh
brew install hdf5
```

Clone **InVesalius 3** using git:

```sh
git clone --recurse-submodules https://github.com/invesalius/invesalius3
```

### Installation

To run the following commands, ensure your shell is inside the `InVesalius` folder:

```sh
cd invesalius3
```

#### Preferred Installation Method (Using `uv`)

We have transitioned to using `uv` for dependency management and `scikit-build-core` with CMake for compiling Cython modules.

1. Install `uv`:

   ```sh
   brew install uv
   ```

2. Sync dependencies:

   ```sh
   uv sync
   ```

3. Build and install InVesalius (including compiling Cython modules):

   ```sh
   uv pip install -e .
   ```

#### Alternative Installation Method (Legacy `pip` Workflow)

Install dependencies using:

```sh
pip3 install -r requirements.txt
```

##### Compiling InVesalius (Legacy)

If you are using a Mac with Apple Silicon, export the following environment variables before compiling:

```sh
export CFLAGS="-I/opt/homebrew/opt/libomp/include"
export CPPFLAGS="-I/opt/homebrew/opt/libomp/include"
export LDFLAGS="-L/opt/homebrew/opt/libomp/lib"
```

Compile the Cython packages used by InVesalius:

```sh
python3 setup.py build_ext --inplace
```

### Running InVesalius

#### Preferred Method (Using `uv`)

After installation, launch InVesalius with:

```sh
uv run app.py
```

#### Alternative Method (Using Python Directly)

```sh
python3 app.py
```

If you encounter the following error:

```
This program needs access to the screen. Please run with a
Framework build of python, and only when you are logged in
on the main display of your Mac.
```

Run InVesalius using:

```sh
pythonw app.py
```
