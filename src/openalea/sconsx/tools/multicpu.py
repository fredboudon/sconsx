# -*-python-*-
#--------------------------------------------------------------------------------
#
#       OpenAlea.SConsX: SCons extension package for building platform
#                        independant packages.
#
#       Copyright 2008 INRIA - CIRAD - INRA  
#
#       File author(s): Samuel Dufour-Kowalski <samuel.dufour@sophia.inria.fr>
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
from openalea.sconsx.util.env_check import is_continuous_integration
import SCons.Script


class MultiCPU:
    def __init__(self, config):
        self.name = 'multicpu'
        self.config = config
        self.num_cpu = 1


    def option( self, opts):
        """ Add Options to opts """
        default_num_jobs = 1
        if is_continuous_integration() and 'CPU_COUNT' in os.environ:
                default_num_jobs = os.environ['CPU_COUNT']

        opts.AddVariables(('num_jobs', 'Number of jobs', default_num_jobs),)


    def update(self, env):
        """ Update the environment with specific flags """
        self.num_cpu = env['num_jobs']
        SCons.Script.SetOption( 'num_jobs', self.num_cpu )

 
    def configure(self, config):
        pass


def create(config):
     mcpu = MultiCPU(config)

     return mcpu

