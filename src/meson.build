pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'skimp')
gnome = import('gnome')

gnome.compile_resources('skimp',
  join_paths('resources', 'skimp.gresource.xml'),
  source_dir: 'resources',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'skimp.in',
  output: 'skimp',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

skimp_sources = [
  '__init__.py',
  'main.py',
  'main_window.py',
]

install_data(skimp_sources, install_dir: moduledir)
