# VASP Tools
[![Build Status](https://travis-ci.com/RexGalilae/vasp-tools.svg?branch=master)](https://travis-ci.com/RexGalilae/vasp-tools) [![Documentation Status](https://readthedocs.org/projects/vasp-tools/badge/?version=latest)](https://vasp-tools.readthedocs.io/en/latest/?badge=latest) [![Requirements Status](https://pyup.io/repos/github/RexGalilae/vasp-tools/shield.svg?t=1563870347975)](https://pyup.io/account/repos/github/RexGalilae/vasp-tools/) [![Python 3](https://pyup.io/repos/github/RexGalilae/vasp-tools/python-3-shield.svg)](https://pyup.io/repos/github/RexGalilae/vasp-tools/)


VASP Tools is a set of modules and scripts that automate routine tasks involving VASP files using  a very intuitive CLI. The `/scripts` directory contains the scripts that implement the `/vasp` module to perform routine tasks on VASP files. This project is still a WIP and new scripts/modules will be added regularly over the next few weeks.

## Requirements
As of now, this package is only supported on `Python>=3.5`. Since support for `Python 2.7` is set to be pulled by 2020, updates in the near future extending support to `Python<=3.0` seems unlikely.

The following libraries are required to run all the scripts and modules.
 - [numpy](https://pypi.org/project/numpy/)
 - [argparse](https://pypi.org/project/argparse/)
 - [sympy](https://pypi.org/project/sympy/)
 - [ujson](https://pypi.org/project/ujson/)
 - [jsonschema](https://pypi.org/project/jsonschema/)
 - [tabulate](https://pypi.org/project/tabulate/)

For a full list of requirements, read requirements.txt. If not already present within the environment, they'll be installed as dependencies during setup.

## Installation
The installation process is quite simple, just ensure you have a working version of `Python>=3.5` installed.

**Note:** Since the package installs all its dependencies accurate to the exact versions used while developing it, it's highly recommended that you install it in a separate environment. 

### To create a new environment 
#### 1. Using Anaconda
```
conda create -n vasp_env python=3.x
conda activate vasp_env
``` 
#### 2. Using `virtualenv` (for non-Anaconda users)

In case you haven't already installed it, run `pip install virtualenv` in the terminal.

Type the following into your terminal:
```
virtualenv vasp_env
source vasp_env/bin/activate
```
### To install the package
#### Stable Release

To install `vasp_tools`, run this command in your terminal:
```
pip install vasp-tools
```
This is the preferred method to install `vasp_tools`, as it will always install the most recent stable release.
  
If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.

#### From Sources
The sources for `vasp_tools` can be downloaded from the  [Github repo](https://github.com/RexGalilae/vasp_tools).

You can either clone the public repository:
```
git clone git://github.com/RexGalilae/vasp_tools
```

Or download the  [tarball](https://github.com/RexGalilae/vasp_tools/tarball/master):
```
curl  -OL https://github.com/RexGalilae/vasp_tools/tarball/master
```

Once you have a copy of the source, you can install it with:
```
python setup.py install
```

Any required libraries that aren't installed in the current environment will be automatically installed.
This will also automatically install the scripts and add them to `$PATH` for easy access.

### Issues with Installation
If nothing works, navigate to the package directory and activate the pre-packaged environment `python_env` by running,
```
source python_env/bin/activate
```
## Compatibility
The package, so far, was only tested within a Linux environment and isn't officially compatible with Windows yet. The scripts can be compiled into executables using [PyInstaller](https://pypi.org/project/PyInstaller/)+Python3.x to work independently of python on any other system running an identical OS. Hence, using VMs/Containers is suggested, though not tested as of yet.

## Usage
The code present in `/vasp` can be imported in the form of standard modules. However, the primary purpose of this project was the creation of scripts (present in `/scripts`) to automate daily tasks faced by the Computational Chemist/Material Scientist. With this in mind, the scripts were designed to be extremely modular and user-friendly by implementing a [`dplyr`](https://style.tidyverse.org/pipes.html)-esque piping paradigm. For example, the process of:

 1. Importing a molecule from a `POSCAR` file.
 2. Rotating it into a certain configuration (90 degrees wrt the x-axis)
 3. Positioning it at a specified point above a crystal taken from another `POSCAR` file
 4. Fixing atomic positions within the crystal below a certain cutoff height
 5. Converting the coordinates to `Direct` from `Cartesian` or vice versa
 6. Save to a new `POSCAR` file.

can be implemented in a single line like so.

```
cat POSCAR1 | rotate.py -x 90 -y 10 | place-at.py "POSCAR2" 0.5 0.5 2.0 | fix-upto.py 10.0 | cart-direct.py > POSCARnew
```
Alternatively, you can also call each script individually or pass "POSCAR1" as one of the positional arguments. For example,

`place-at.py "POSCAR2" "POSCAR1" 0.5 0.5 2.0`

is perfectly equivalent to

`cat POSCAR1 | place-at.py "POSCAR2" 0.5 0.5 2.0`

Detailed instructions on how to use the scripts are available in [docs](https://vasp-tools.readthedocs.io/en/latest/) (WIP).

----------------------------------------------------------
*Written with [StackEdit](https://stackedit.io/)*
