# setup.py
from setuptools import setup

setup(
     name='ADFR_bundle',
     scripts=['bin_scripts/adfr', 
              'bin_scripts/agfr', 'bin_scripts/agfrgui', 
              'bin_scripts/autosite', 'bin_scripts/pmv2', 
              'bin_scripts/pythonsh', 
              'bin_scripts/reduce_wwPDB_het_dict.txt'],
     data_files = [('bin',['bin_scripts/autogrid4', 
                           'bin_scripts/reduce']),
                   ('lib',['lib_files/libnlopt.so.0']),
                   ],
     package_dir = {
            'AutoSite': 'src/AutoSite',
            'ADFR': 'src/ADFR',
            'AppFramework': 'src/AppFramework',
            'MolKit2': 'src/MolKit2',
            'PmvApp': 'src/PmvApp',
            'pyglf': 'src/pyglf',},
     packages=['AutoSite',
               'ADFR', 'AppFramework',  
               'MolKit2',  
               'PmvApp', 'pyglf' ],
    # install_requires =['pybel==0.15.0', 'biopython==1.76','colorama','numpy==1.18.5'],


)
