top2vec
=======


About
-----
Making top2vec work on deterrence corpora. 


Getting started
---------------
These instructions will get you a copy of the project up and running on 
your local machine for development and testing purposes.


Installation
^^^^^^^^^^^^
To use or contribute to this repository, first checkout the code. 
Then create a new virtual environment:

.. code-block:: console

    $ git clone https://github.com/hcss-utils/top2vec.git
    $ cd top2vec
    $ python -m venv env
    $ . env/Scripts/activate # Windows
    $ . env/bin/activate # Linux / MacOS
    $ pip install -r requirements.txt

Alternatevly, follow google colab shared at Rizzoma/Topic modeling

Usage
^^^^^
1. Put source files from GDrive (not sharing publicly here) into ``models/`` and ``data/``
2. Run ``notebooks/``

Project Organization
--------------------

.. code-block:: console

    ├── Makefile           <- Makefile with commands like `make clean`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0_hp_initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`
    