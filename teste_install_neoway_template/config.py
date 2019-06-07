from os import path

import teste_install_neoway_template

base_path = path.dirname(path.dirname(teste_install_neoway_template.__file__))
workspace_path = path.join(base_path, 'workspace')
data_path = path.join(workspace_path, 'data')
models_path = path.join(workspace_path, 'models')
