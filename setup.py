from setuptools import setup, find_packages

def configuration(parent_package='danielsdatastructures',top_path="SixthFormDataStructures"):
    from numpy.distutils.system_info import get_info
    lapack_opt = get_info("lapack_opt")

    from numpy.distutils.misc_util import Configuration
    config = Configuration('danielsdatastructures',parent_package,top_path)
    config.add_subpackage('queues')
    config.make_config_py()
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration().todict())