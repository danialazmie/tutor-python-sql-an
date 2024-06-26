# Setting up the environment

## Git

In order to use Git, you need to have Git installed on your Windows. Get it [here](https://git-scm.com/downloads)

Once you have it installed, you _might_ need to restart your computer to have it work properly.

Most of the Git features will be used in VSCode which will handle most of the commands for you.

## Anaconda3

- Download and install Anaconda3 [here](https://www.anaconda.com/download/success)

### Setting up virtual environments

- For Windows, search and run `Anaconda Prompt (Anaconda3)` program from Windows Search
```shell
(base) C:\Users\user> 
```
- Create a virtual environment `conda create --name <env-name> python=3.11.9`
- Once it's set up, activate the new environment `conda activate <env-name>`
- Execute `conda install anaconda` to install a set of libraries that are commonly used for Data Science
- You can run `jupyter lab` to see if it's working correctly.

## Visual Studio Code (Optional)

You can also use VSCode as your integrated development environment (IDE) which is more intuitive and production-ready. You can download it [here](https://code.visualstudio.com/)

VSCode should be able to detect your environments from Anaconda once you have the Python and Jupyter extensions installed. You can check this by:

- Press `F1` or `CTRL+Shift+P`
- You should be able to type and find `Jupyter: Select Interpreter to Start Jupyter Server`
- This allows you to choose your kernel environment to run your Jupyter notebook in VSCode

### Recommended extensions for VSCode

```
Name: Python
Id: ms-python.python
Description: Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.
Version: 2024.8.1
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python
```
```
Name: Jupyter
Id: ms-toolsai.jupyter
Description: Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.
Version: 2024.5.0
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
```

```
Name: git-autoconfig
Id: shyykoserhiy.git-autoconfig
Description: Automatic git config user.email and user.name setting for vscode
Version: 0.0.2
Publisher: shyykoserhiy
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=shyykoserhiy.git-autoconfig
```

```
Name: Codeium: AI Coding Autocomplete and Chat for Python, Javascript, Typescript, Java, Go, and more
Id: Codeium.codeium
Description: The modern coding superpower: free AI code acceleration plugin for your favorite languages. Type less. Code more. Ship faster.
Version: 1.8.66
Publisher: Codeium
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=Codeium.codeium
```

## Notes

- A virtual environment is an isolated Python environment that allows you to create a separate instance of Python with its own set of installed packages and dependencies.
- Example:
  - Environment A has Python 3.6, pandas v1.5.3
  - Environment B has Python 3.11, pandas v2.2.2, Matplotlib v3.5.3
- This is important as sometimes you'll find yourself working on projects with different requirements. Say you work on a legacy system that requires Python 2 with older libraries, and at the same time you need to work on an ongoing project using Python 3 with new libraries.
- This allows you to switch environments faster and avoid conflicts when working on different projects.
