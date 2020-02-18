# -*-python-*-
#--------------------------------------------------------------------------------
#
#       OpenAlea.SConsX: SCons extension package for building platform
#                        independant packages.
#
#       Copyright 2006-2009 INRIA - CIRAD - INRA
#
#       File author(s): Christophe Pradal <christophe.prada@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
#--------------------------------------------------------------------------------
""" QHull configure environment. """

__license__ = "Cecill-C"
__revision__ = "$Id$"

import os, sys
from openalea.sconsx.config import *


class Qhull:
   def __init__(self, config):
      self.name = 'qhull'
      self.config = config
      self._default = {}


   def default(self):

      self._default['libs_suffix'] = '$compiler_libs_suffix'

      if CONDA_ENV:
            base_dir = CONDA_LIBRARY_PREFIX
            self._default['include'] = pj(base_dir, 'include')
            self._default['libpath'] = pj(base_dir, 'lib')

      elif isinstance(platform, Win32):
         try:
            # Try to use openalea egg
            from openalea.deploy import get_base_dir
            base_dir = get_base_dir("qhull")
            self._default['include'] = pj(base_dir, 'include')
            self._default['libpath'] = pj(base_dir, 'lib')

         except:
            try:
                import openalea.config as conf
                self._default['include'] = conf.include_dir
                self._default['libpath'] = conf.lib_dir

            except ImportError as e:
                self._default['include'] = 'C:'+os.sep
                self._default['libpath'] = 'C:'+os.sep

      elif isinstance(platform, Posix):
           defdir = detect_posix_project_installpath('include/libqhull')
           self._default['include'] = join(defdir,'include')
           self._default['libpath']     = join(defdir,'lib') 


   def option( self, opts):

      self.default()

      opts.AddVariables(
         ('qhull_includes',
           'Qhull include files',
           self._default['include']),

         (('qhull_libpath','qhull_lib'),
           'Qhull library path',
           self._default['libpath']),

         ('qhull_libs_suffix',
           'Qhull library suffix name like -vc80 or -mgw',
           self._default['libs_suffix']),

         BoolVariable('WITH_QHULL',
           'Specify whether you want to compile your project with QHULL', True)
     )


   def update(self, env):
      """ Update the environment with specific flags """

      if env['WITH_QHULL'] :
        def_qhull_inc = env['qhull_includes']
        qhull_inc = pj(def_qhull_inc, 'libqhull')
        if not os.path.exists(os.path.join(qhull_inc, "qhull_a.h")) :
          import openalea.sconsx.errormsg as em
          em.error("Error: QHull headers not found. QHull disabled ...")
          env['WITH_QHULL'] = False

      if env['WITH_QHULL'] :
        env.AppendUnique(CPPPATH=[env['qhull_includes']])
        env.AppendUnique(LIBPATH=[env['qhull_libpath']])

        env.AppendUnique( CPPDEFINES = ['WITH_QHULL_2011'] )
        env.AppendUnique( CPPDEFINES = ['WITH_QHULL'] )

        qhull_name = 'qhull'+env['qhull_libs_suffix']
        env.AppendUnique(LIBS=[qhull_name])


   def configure(self, config):
      if not config.conf.CheckCHeader('qhull/qhull_a.h'):
         print("Error: qhull headers not found.")
         sys.exit(-1)


def create(config):
   " Create qhull tool "
   qhull = Qhull(config)

   return qhull
