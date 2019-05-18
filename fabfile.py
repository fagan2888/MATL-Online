from fabistrano import deploy
from fabric.api import env

env.git_branch = 'js_fabistrano'
env.hosts = ['matl.suever.net']
env.forward_agent = True
env.remote_owner = 'matl'
env.remote_group = 'matl'
env.base_dir = '/opt'
env.app_name = 'matl-online'
env.git_clone = 'git@github.com:suever/matl-online'

env.restart_cmd = 'sudo systemctl restart matl-online.target'
