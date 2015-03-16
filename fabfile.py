from fabric.api import local

def update_to(version):
    local('rm -rf fonts/')
    local('rm katex.min.css')
    local('rm katex.min.js')
    local('wget https://github.com/Khan/KaTeX/releases/download/{0}/katex.zip'.format(version))
    local('unzip katex.zip')
    local('rm katex.zip')
    local('rm katex/README.md')
    local('mv katex/* .')
    local('rmdir katex')
