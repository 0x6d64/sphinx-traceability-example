.. _sec-versions:

Version history
===============
This chapter shows how to create items for certain tool versions, and then
assign implemented requirements to them.

List of versions
----------------

.. item:: exemplum-v0.0
    :implements: req_1 req_2

    Initial prototype.
    Features:

    * data storage

.. item:: exemplum-v0.1
    :implements: req_3 req_4 req_1 req_2

    Changes:

    * method to add data
    * method to get size of data storage in elements


requirements implemented per version
------------------------------------

.. item-matrix:: versions, requirements
    :source: exemplum
    :target: req
    :type: implements
    :sourcetitle: version
    :targettitle: requirement

