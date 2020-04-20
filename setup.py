# -*- coding: utf-8 -*-
__revision__ = "$Id$"

import os, sys
from setuptools import setup, find_packages

pj= os.path.join


# from openalea.deploy.metainfo import read_metainfo
# metadata = read_metainfo('metainfo.ini', verbose=True)
# for key,value in metadata.items():
#     exec("%s = '%s'" % (key, value))

name = 'OpenAlea.SConsX'
project = 'openalea'
namespace = 'openalea'
pkg_name = 'openalea.sconsx'
version = '3.0.1'
release = '3.0'
package = 'sconsx'
description = 'Scons Extension to build multi-platform packages for OpenAlea and others.'
authors = 'Christophe Pradal'
authors_email = 'christophe.pradal@cirad.fr'
url = 'http://openalea.gforge.inria.fr'
license = 'Cecill-C'



long_description = \
"""
Scons Configuration Utilities for OpenAlea.

SConsX is a set of tools to enhance multi platform configuration,
build and installation.
This package extends scons with:
    * automatic dependency between tools,
    * default path for library depending on the platform ( Linux, Windows or Cygwin )
    * automatic option settings
    * Support for different compilers on Linux and Windows (e.g. gcc, msvc, mingw)
"""

packages=find_packages('src')
package_dir={'': 'src'}

setup(name = name,
      version = version,
      description = description,
      long_description = long_description,
      author = authors,
      author_email = authors_email,
      license = license,

      namespace_packages = ['openalea'],
      create_namespaces = True,
      zip_safe = False,

      packages=packages,
      package_dir= package_dir,

      # Dependencies
      #setup_requires = ['openalea.deploy'],
      #install_requires = [],
      #dependency_links = ['http://openalea.gforge.inria.fr/pi'],

      )
