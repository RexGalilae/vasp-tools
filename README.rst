VASP Tools
==========

|Build Status| |Documentation Status|

VASP Tools is a set of modules and scripts that automate routine tasks
involving VASP files using a very intuitive CLI. The ``/scripts``
directory contains the scripts that implement the ``/vasp`` module to
perform routine tasks on VASP files. This project is still a WIP and new
scripts/modules will be added regularly over the next few weeks.

Requirements
------------

As of now, this package is only supported on ``Python>=3.5``. Since
support for ``Python 2.7`` is set to be pulled by 2020, updates in the
near future extending support to ``Python<=3.0`` seems unlikely.

The following libraries are required to run all the scripts and modules.

* `numpy <https://pypi.org/project/numpy/>`__

* `argparse <https://pypi.org/project/argparse/>`__

* `sympy <https://pypi.org/project/sympy/>`__

* `ujson <https://pypi.org/project/ujson/>`__

* `jsonschema <https://pypi.org/project/jsonschema/>`__

* `tabulate <https://pypi.org/project/tabulate/>`__

For a full list of requirements, read requirements.txt. If not already
present within the environment, they'll be installed as dependencies
during setup.

Installation
------------

The installation process is quite simple, ensure you have a working
version of ``Python>=3.5`` installed and type the following into the
console,

::

    pip install vasp-tools

Any required libraries that aren't installed in the current environment
will be automatically installed. This will also automatically install
the scripts and add them to $PATH for easy access.

Compatibility
-------------

The package, so far, was only tested within a Linux environment and
isn't officially compatible with Windows yet. The scripts can be
compiled into executables using
`PyInstaller <https://pypi.org/project/PyInstaller/>`__ to work
independently of python on any system, though it should be run in an
environment with an identical OS. Use of VMs/Containers is suggested,
though not tested as of yet.

Usage
-----

The code present in ``/vasp`` can be imported in the form of standard
modules. However, the primary purpose of this project was the creation
of scripts (present in ``/scripts``) to automate daily tasks faced by
the Computational Chemist/Material Scientist. With this in mind, the
scripts were designed to be extremely modular and user-friendly by
implementing a
`dplyr <https://style.tidyverse.org/pipes.html>`__ -esque piping
paradigm. For example, the process of:

1. Importing a molecule from a ``POSCAR`` file.
2. Rotating it into a certain configuration (90 degrees wrt the x-axis)
3. Positioning it at a specified point above a crystal taken from
   another ``POSCAR`` file
4. Fixing atomic positions within the crystal below a certain cutoff
   height
5. Converting the coordinates to ``Direct`` from ``Cartesian`` or vice
   versa
6. Save to a new ``POSCAR`` file.

can be implemented in a single line like so.

::

    cat POSCAR1 | ./rotate.py -x 90 -y 10 | ./place-at.py "POSCAR2" 0.5 0.5 2.0 | ./fix-upto.py 10.0 | ./cart-direct > POSCARnew

Alternatively, you can also call each script individually or pass
"POSCAR1" as one of the positional arguments. For example,

``./place-at.py "POSCAR2" "POSCAR1" 0.5 0.5 2.0``

is perfectly equivalent to

``cat POSCAR1 | ./place-at.py "POSCAR2" 0.5 0.5 2.0``

Detailed instructions on how to use the scripts are available in
`docs <https://vasp-tools.readthedocs.io/en/latest/>`__.

--------------

Written with `StackEdit <https://stackedit.io/>`__

.. |Build Status| image:: https://travis-ci.com/RexGalilae/vasp-tools.svg?branch=master
   :target: https://travis-ci.com/RexGalilae/vasp-tools
.. |Documentation Status| image:: https://readthedocs.org/projects/vasp-tools/badge/?version=latest
   :target: https://vasp-tools.readthedocs.io/en/latest/?badge=latest
