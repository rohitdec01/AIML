import pkgutil, sys
print('pkgutil_file=', getattr(pkgutil, '__file__', None))
print('has_ImpImporter=', 'ImpImporter' in dir(pkgutil))
print('dir_sample=', [n for n in dir(pkgutil) if n.startswith('Imp') or n.startswith('find')][:20])
print('sys_path0=', sys.path[0])
print('python_executable=', sys.executable)
