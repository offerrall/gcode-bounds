from setuptools import setup, find_packages, Extension


name = "gcode_bounds"

nc_parser_extension = Extension(
    f'{name}._gcode_parser',
    sources=[
        'c_src/gcode_parser.c',        
        'c_src/python_wrapper.c'    
    ],
    include_dirs=['c_src'],         
    extra_compile_args=['-std=c99', '-O3'],     
)

setup(
    name=name,
    version="1.0.0",
    packages=find_packages(),
    ext_modules=[nc_parser_extension],
)