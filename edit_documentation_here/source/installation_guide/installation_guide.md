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
   winget install --id=astral-sh.uv  -e
   ```

2. Navigate to the cloned InVesalius directory:

   ```shell
   cd invesalius3
   ```

3. Install dependencies and compile Cython extensions automatically:

   ```shell
   uv sync
   ```

4. Run InVesalius:

   ```shell
   uv run app.py
   ```

5. **Tip**: To install additional dependencies, use:

   ```shell
   uv add <dependency-name>
   ```

### Option 2: Python System Installation

1. Download and install Python 3.8 from the [Python website](https://www.python.org/downloads/).

2. Create a virtual environment using

   ```shell
   python3 -m venv .venv
   ```

3. Activate the virtual environment using

   ```shell
   .venv\bin\activate
   ```

4. Install InVesalius main dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

5. If you are going to use the neuronavigation features, install the wrappers for tracking devices:

   ```shell
   pip install pyclaron polhemusFT polhemus pypolaris pypolarisP4
   ```

6. **Optional:** To enable real-time tractography computation, install [Trekker](https://dmritrekker.github.io/):

   ```shell
   pip install https://github.com/dmritrekker/trekker/raw/master/binaries/Trekker-0.9-cp38-cp38-win_amd64.whl
   ```

7. Compile cython files:
   ```shell
   pip install .
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

**Warning:** If using Anaconda or pip , always activate the environment before running the command.

If using `uv`, simply run:

```shell
uv run app.py
```

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
   OpenMP_ROOT=$(brew --prefix)/opt/libomp uv sync
   ```

3. Build and install InVesalius (including compiling Cython modules):

   ```sh
   uv sync
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

## Linux

### Packages Debian and Ubuntu

InVesalius is already packaged and is in the main repos from Debian and Ubuntu. Install it using this command:

```shell
sudo apt install invesalius
```

If you want the most updated packages, there is
also a [PPA](https://launchpad.net/~tfmoraes/+archive/ubuntu/invesalius) to Ubuntu:

```shell
sudo add-apt-repository ppa:tfmoraes/invesalius
sudo apt-get update
sudo apt install invesalius
```

After the installation, InVesalius appears in your system menu. You can also run it from the command line:

```shell
invesalius3
```

### Other Distros

InVesalius is packaged as [Flatpak](https://flathub.org/apps/details/br.gov.cti.invesalius).
First, you need to add the Flathub repo:

```shell
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

Then install InVesalius:

```shell
flatpak install flathub br.gov.cti.invesalius
```

After the installation, InVesalius appears in your system menu. You can also run it from the command line:

```shell
flatpak run br.gov.cti.invesalius
```

### Source Code

Use this command to get InVesalius source code from GitHub:

```bash
git clone --recurse-submodules https://github.com/invesalius/invesalius3
```

#### Installing Dependencies

##### Using PIP Packages (recommended)

First, you have to install some system packages to compile wxPython and H5py:

- Fedora (tested on Fedora 34)

```bash
sudo dnf -y install \
    gcc-c++ \
    python3-devel \
    freeglut-devel \
    gstreamer1-devel \
    gstreamer1-plugins-base-devel \
    gtk3-devel \
    libjpeg-turbo-devel \
    libnotify-devel \
    libpng-devel \
    libSM-devel \
    libtiff-devel \
    libXtst-devel \
    SDL-devel \
    webkit2gtk3-devel \
    which \
    hdf5-devel
```

- Ubuntu (tested on Ubuntu 20.10 and 21.04)

```bash
sudo apt install -y \
    freeglut3 \
    freeglut3-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libgstreamer-plugins-base1.0-dev \
    libgtk-3-dev \
    libjpeg-dev \
    libnotify-dev \
    libsdl2-dev \
    libsm-dev \
    libtiff-dev \
    libwebkit2gtk-4.0-dev \
    libxtst-dev \
    python3-dev \
    libhdf5-dev \
    build-essential \
    python3-venv
```

- Arch

```bash
sudo pacman -syu \
    wxgtk3 \
    glu \
    mesa \
    webkit2gtk
```

It's recommended to create a virtualenv

1.  using `uv`:

    ```bash
    # Go to InVesalius folder
    cd invesalius3
    # Create my_env environment
    uv venv
    # Install dependencies and build cython extensions
    uv sync
    ```

    Tip: To add extra dependencies to the project use:

    ```bash
    uv add <dependency-name>
    ```

2.  using `pip`:
    ```bash
    # Go to InVesalius folder
    cd invesalius3
    # Create my_env environment
    python3 -m venv my_env
    # Activate it every time you want to run InVesalius
    source my_env/bin/activate
    pip install -r requirements.txt
    ```

##### Using System Packages

###### Debian and Ubuntu (Tested in Ubuntu 20.04)

`sudo apt install python3-wxgtk4.0 python3-numpy python3-scipy python3-pil python3-matplotlib python3-skimage python3-nibabel python3-serial python3-psutil python3-vtk7 python3-vtkgdcm python3-gdcm cython3 python3-h5py python3-imageio python3-keras python3-pubsub`

Ubuntu don't have PlaidML in their repositories, so install it using **pip**:

`pip3 install --user plaidml-keras`

##### Fedora (Tested in Fedora 32)

`sudo dnf install gcc gcc-g++ python3-wxpython4 python3-numpy python3-scipy python3-matplotlib python3-scikit-image python3-nibabel python3-pyserial python3-psutil python3-vtk python3-gdcm python3-Cython python3-h5py python3-pypubsub`

Unfortunately, Fedora doesn't have **python3-imageio** package. But it's possible to install it using **pip**:

`pip3 install --user imageio`

Fedora don't have PlaidML in their repositories, so install it using **pip**:

`pip3 install --user plaidml-keras`

##### Arch Linux

`sudo pacman -S cython python-pip python-numpy python-scipy python-scikit-learn python-wxpython python-pyserial python-psutil python-h5py python-pypubsub python-mpi4py python-matplotlib vtk clinfo opencl-headers gdal glew hdf5 jsoncpp netcdf pdal pugixml proj`

You have to install some packages from AUR, I'm using Pikaur to install them:

`pikaur -S --noconfirm gdcm python-nibabel python-scikit-image python-imageio python-plaidml python-plaidml-keras`

#### Building the Cython Modules

Enter on invesalius3 folder and execute: `python3 setup.py build_ext --inplace`

#### Running InVesalius

To run InVesalius, enter the InVesalius folder and run the command:

`python3 app.py`

You can pass a DICOM folder as parameter to make InVesalius starts with the DICOM loaded.

`python3 app.py -i /dicom/folder`

It's possible to make InVesalius load a DICOM folder,
create a surface (mesh) with the given threshold and export the surface to an STL file without loading any GUI:

`python3 app.py --no-gui -i /media/thiago/Documentos/dcm/0051 -t 200,3033 -e /tmp/0051.stl`
