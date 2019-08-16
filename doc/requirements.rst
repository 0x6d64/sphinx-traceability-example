.. _sec-requirements:

Requirements
============

List of requirements
--------------------

.. item-list::
    :filter: req

Version to implement requirement
--------------------------------

.. item-matrix::
    :source: req
    :target: exemplum
    :type: implemented_by

Testcases for requirements
--------------------------

.. item-matrix::
    :source: req
    :target:
    :type: tested_by


Requirement details
-------------------

.. requirement:: req_1

    The :py:class:`~exemplum.exemplum.Exemplum` class shall provide storage for data.

.. requirement:: req_2

    The data storage from :item:`req_1` shall be initialized with an empty list.

.. requirement:: req_3

    The :py:class:`~exemplum.exemplum.Exemplum` class shall provide a method :py:meth:`~exemplumexemplum.Exemplum.add_data` to fill the data storage.

.. requirement:: req_4

    The :py:class:`~exemplum.exemplum.Exemplum` class shall provide a method :py:meth:`~exemplum.exemplum.Exemplum.__len__` that returns the element count in the data storage.


