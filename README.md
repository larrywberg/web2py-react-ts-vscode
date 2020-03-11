
## Web2py . Visual Studio Code . React . Typescript  . Webpack

This is a **web2py** example application and **Visual Studio Code setup** that supports building and debugging a modern **React** style client interface using **Typescript** and **Webpack** while simultaneously being able to debug the python server in one environment.  Please feel free to send me feedback if you think there are better ways to set things up.  The web2py admin interface can also be used to edit the same files as Visual Studio Code when run locally.

## Quickstart:

```
1. Install python3, node, npm, Visual Studio Code. Use Chrome as your browser.  
```

- node: [https://nodejs.org/en/](https://nodejs.org/en/)
- python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Visual Studio Code: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
- Install VSCode extensions for python and typescript and Chrome Debugger.  
- Select a recent Python 3 version as the default python for VS Code  

```
2. Install python requests library (used by some of the contollers in this sample app)
```

- pip3 install requests

```
3. Download a source archive of web2py and unzip it locally:
```

- web2py: [https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip](https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip)

```
4. Copy the reactAndWeb2py folder inside the download you got from this github repo to the applications folder of your local copy of web2py
```

- cp -r reactAndWeb2py web2py_src/applications/

```
4.5 optionally set the default route to this application by changing routes.py
    to contain the line below:
```

- default_application = "reactAndWeb2py"

```
5. Open the Visual Studio Code code-workspace file in VS Code:
```

- cd web2py_src/applications/reactAndWeb2py  
- code reactAndWeb2py.code-workspace

```
6. Install the node modules needed for this project.  
```

There are two ways to do this:  

- run the pre-configured "Install Node Modules" task (Terminal>Run Task...),  
or:    
- run "npm install" in the reactAndWeb2py folder in the VSCode terminal or in a shell window
  

```
7. Launch the web2py server using the pre-configured VS Code launch task  
```

- Go to the "Run and Debug" tab in VS Code.
- Select the "Launch Web2py" task
- Click the run button at the start of the task label
- Type a password that you will use to get to the admin panel

```
8. Log in to the chrome window that has launched  
```

- If you didn't set the default route you will be running some other web2py application.  
  If so navigate  to  [http://127.0.0.1:8000/reactAndWeb2py/default/user/login](http://127.0.0.1:8000/reactAndWeb2py/default/user/login)
- Use this login to have the admin menu:
- Username:  admin@example.com  
- password:  **password**  

```
9. You are already debugging the python server.  
  If you want to debug the javascript as well:
```

- run the "Launch and Debug ..." task.

```
10. You are up and running
```

- Choose the react example from the top menu
- You should also log in to the web2py admin panel so that you can edit the application in its entirety in web2py. Use the password you set when you launched the web2py window. 
- <a href="http://127.0.0.1:8000/admin" target="_blank">web2py admin</a>
- The react source code is in the ***static/reactsrc/*** folder
- The react application can be edited at: [http://127.0.0.1:8000/admin/default/design/reactAndWeb2py](http://127.0.0.1:8000/admin/default/design/reactAndWeb2py)
- Examine the ***prebuilt launch tasks and npm scripts*** in the Visual Studio Code project.
    - One Launch configuration will allow you to attach to a chrome window from VSCode
    - There is an npm script that will start a live webpack dev server to allow live changes in a single view.
    - Other npm scripts exist for building debug and release versions of the react source.
- The user athentication and authorization is provided by web2py.
- There is an admin menu (if logged in as admin) in the app that can recompile typescript changes so that the react elements can be updated
- There are other web2py api examples as well
- Some folders are marked hidden to make working with web2py in Visual Studio friendlier (settings, excludes).
- Map files are generated so both python and javascript can be debugged at the same time in the same environment.
- You can edit the server side files through the web2py admin interface or from VS Code when using this setup locally.

## Notes:
A number of web2py, and other, folders are set to be hidden for a clean experience.  You can changed what's hidden by
changing the exclude settings of the workspace in VS Code  

Before packing up the web2py application to move to a server it would be wise to delete the node_modules folder (I don't know how to tell web2py not to pack everything)  

For real deployment you would want to remove the static/reactsrc folder.  It's needed for debugging as it contains the source and map files.  
