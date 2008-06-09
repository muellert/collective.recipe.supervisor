# -*- coding: utf-8 -*-
"""
Doctest runner for 'plone.recipe.cluster'.
"""
__docformat__ = 'restructuredtext'
import sys
import unittest
import zc.buildout.tests
import zc.buildout.testing

from zope.testing import doctest, renormalizing

optionflags =  (doctest.ELLIPSIS |
                doctest.NORMALIZE_WHITESPACE |
                doctest.REPORT_ONLY_FIRST_FAILURE)

def setUp(test):
    zc.buildout.testing.buildoutSetUp(test)

    # Install the recipe in develop mode
    zc.buildout.testing.install_develop('plone.recipe.cluster', test)

    # Install any other recipes that should be available in the tests
    #zc.buildout.testing.install('collective.recipe.foobar', test)
    if sys.platform != 'win32':
        from plone.recipe.cluster import ctl
        ctl.DEBUG = True

def test_suite():
    if sys.platform == 'win32':
        doctest_file = '../README-win32.txt'
    else:
        doctest_file = '../README.txt'

    suite = unittest.TestSuite((
            doctest.DocFileSuite(
                doctest_file,
                setUp=setUp,
                tearDown=zc.buildout.testing.buildoutTearDown,
                optionflags=optionflags,
                checker=renormalizing.RENormalizing([
                        # If want to clean up the doctest output you
                        # can register additional regexp normalizers
                        # here. The format is a two-tuple with the RE
                        # as the first item and the replacement as the
                        # second item, e.g.
                        # (re.compile('my-[rR]eg[eE]ps'), 'my-regexps')
                        zc.buildout.testing.normalize_path,
                        ]),
                ),
            ))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')