# Description
A baseline laboratory project for "Numerical methods" course

## Workstation setup
### MacOSX
1. Install [__brew__](https://brew.sh/) `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install __python3__ tool `brew install python@3.13`
   Check if __python3__ exec comes from __brew__ `which python3`. Responce should be something like `/opt/homebrew/bin/python3`
3. Install [__VS Code__](https://code.visualstudio.com/) and recommended for this project extentions

### Windows
1. Install [__WSL__](https://learn.microsoft.com/en-us/windows/wsl/install) and __Ubuntu__ distro
    1. How to turn on Hyper Visor [video](https://www.youtube.com/watch?v=KEjr6mQ8rqg)
    2. Move __WSL__ installation to non-system drive `wsl --manage distro --move new-location` where `distro = Ubuntu` and `new-location = D:\wsl\`
    3. How to [reset user password](https://superuser.com/questions/1829481/how-to-reset-my-wsl-ubuntu-password)
        1. Start __Ubuntu__ terminal in as root user `wsl -d Ubuntu -u root`
        2. Reset password for your user `passwd {username}`
        3. Enter new password and confirm it. Note: in Unix like systems passwords typed in terminal are not visible
2. Install [__VS Code__](https://code.visualstudio.com/) and recommended for this project extentions
    1. Install [__WSL__](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) extention for __VS Code__
    2. In bottom left corner select _Open a Remote Window_ button and restart __VS Code__ in __WSL__ mode
3. Run __Ubuntu__ terminal from start menu or in VS Code
4. Update system packages `sudo apt update && sudo apt upgrade -y`
5. Install __python3__ `sudo apt install python3 python3-pip python3-venv`

### Windows (simplified)
1. Install __python3__ from [official website](https://www.python.org/downloads/) without Admin Privileges and/or adding to Path
2. Install [__VS Code__](https://code.visualstudio.com/) and recommended for this project extentions
3. In __VS Code__ open any file with _.py_ extention and in bottom right corner select correct python interpreter installed on previous step
4. Run file with __Run__ button in right top corner
5. If needed specify default Terminal application by pressing __F1__, typing _Terminal: Select Default Profile_ and choosing _Command Prompt_ (cmd.exe)

## Project development
1. Enter project directory `cd ~/path-to-your-projects/nummethods`
2. Create python virtual environment `python3 -m venv venv`
3. Activate virtual environment `source venv/bin/activate`
4. Install python requirements `pip3 install -r requirements.txt`
