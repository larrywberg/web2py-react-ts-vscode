import subprocess
# import os


# This will install all of the necessary npm modules
@auth.requires_membership('admin')
def npminstall():
    proc = subprocess.Popen('npm install', cwd="applications/"+request.application, shell=True, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    output = output.decode("utf-8")
    output = output.replace('\n','<br>')
    return dict(buildOutput=output)

# This will launch webpack to build the debug build of the react and typescript code
@auth.requires_membership('admin')
def builddev():
    proc = subprocess.Popen('npm run-script dev', cwd="applications/"+request.application, shell=True, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    output = output.decode("utf-8")
    output = output.replace('\n','<br>')
    return dict(buildOutput=output)
