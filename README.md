# sphinx-traceability-example
example implementation of requirements and test cases using 
[the melexis for of the sphinx-traceability-extension](https://github.com/melexis/sphinx-traceability-extension).
For an older version of this example (using 
[the original extension](https://github.com/ociu/sphinx-traceability-extension) see 
[this release](https://github.com/0x6d64/sphinx-traceability-example/releases/tag/v1.0)).

The built documentation can be viewed here: https://0x6d64.github.io/sphinx-traceability-example/

[![CI](https://github.com/0x6d64/sphinx-traceability-example/actions/workflows/main.yml/badge.svg)
](https://github.com/0x6d64/sphinx-traceability-example/actions/workflows/main.yml)

## motivation
The sphinx traceability extension contains the required building blockst to document requirements 
and associate test cases with them. The example included in the project showcases how these blocks 
work, but I needed an example that showed how documentation of a real project with formal 
requirements, implementation if those requirements and tests work.

## requirements
This example was tested using version 3.4.1 of the mlx.traceability package. This means that we also need python3.

## the example project
This project contains the fictional `exemplum` package. The package is tested in `exemplum_test` 
and its documentation resides in the `doc` directory. The requirements are defined in 
`requirements.rst` in the documenation folder. The test cases are documentend in their docstrings; 
the test cases are linked to the requirement using the `tests` relationship.

The requirement chapter uses a item-list and item-matrix to create overviews of all requirements, 
but also show which requirements are covered by test cases.
 
## how it works
All configuration is done in the `conf.py` of your sphinx documenation: we define two new 
`ItemDirective`: `requirement` and `testcase`. Additionally we add a new relationship 
`tests`/`tested_by` to link test cases to requirements.

We also use the config value `traceability_item_template` to modify how `requirement` and `testcase` 
items are rendered: they now all get their own small traceability matrix; we filter for the id in 
source to only get the linked items for that requrement or testcase. We also check if a caption 
is given to insert a prettier caption for requirements.


## prerequisites
To build the example you need to have a working sphinx installation and the 
[sphinx-traceability-extension](https://github.com/ociu/sphinx-traceability-extension) has to be 
installed. You may also need to adapt the `'sphinxcontrib.traceability'` value in `doc/config.py` 
to adapt to match the location where the extension is installed on your system. 

## known issues / missing features
There are several issues that I was not able to solve quickly:

* customize the format of the item-matrix tables: I want the table to have a better heading than 
"source" and "target". It would be nice if there was something like traceability_matrix_template 
similar to traceability_item_template. With this feature we could have tables labeled "requirement",
"tested by" to make more sense to the reader. This feature is planned in a future version of 
original extensions.
* permit items without an explicit identifier when inside a docstring. Reasoning: when documenting 
test cases or implementation you constantly have to come up with an identifier when the method name
could be used automatically instead.
