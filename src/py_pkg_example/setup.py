from setuptools import find_packages, setup

package_name = 'py_pkg_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dilmac',
    maintainer_email='dilmacc@todo.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = py_pkg_example.py_node_example:main", # {name} = {pkg folder name}.{node file name}:{function that we want to call in node file}
            "py_oop_node = py_pkg_example.py_oop_node:main",
            "robot_news_station = py_pkg_example.news_station:main" #there was some problem in running the code, deleting build/ install/ log 
                                                                    #and rebuilding the ws with colcon build solved it {rm -rf build/ install/ log/}
        ],
    },
)
