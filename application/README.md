# Application Folder

## Purpose
The purpose of this folder is to store all the source code and related files for your team's application. Source code MUST NOT be in any of folder. <strong>YOU HAVE BEEN WARNED</strong>

You are free to organize the contents of the folder as you see fit. But remember your team is graded on how you use Git. This does include the structure of your application. Points will be deducted from poorly structured application folders.

## Please use the rest of the README.md to store important information for your team's application.

## How to run the application locally
```
$ devenv up
```

In order to run this command, you need `nix` and `devenv` installed.

If you are using Apple Scillicon machine:
```
curl -L https://raw.githubusercontent.com/NixOS/experimental-nix-installer/main/nix-installer.sh | sh -s install
nix-env -iA devenv -f https://github.com/NixOS/nixpkgs/tarball/nixpkgs-unstable
```

If you are using Windows machine, you need WSL2:
```
sh <(curl -L https://nixos.org/nix/install) --no-daemon
nix-env -iA devenv -f https://github.com/NixOS/nixpkgs/tarball/nixpkgs-unstable
```

The instruction on how to install these tools is documented here:
https://devenv.sh/getting-started

How to deploy:


1. SSH into server

    `ssh -i path/to/your_key ubuntu@{Server URL or IP}`

2. navigate to application directory

   `cd csc648-fa24-03-team01/application/`

3. Pull the main branch

    `git pull origin main`

4. Identify the running python server process if running

    `ps aux | grep "python app.py"`

    * note the PID of the process if exist

5. Stop the python server process if exist

    `kill {PID of process}`

6. Enter virtual enviroment

    `source ~/projectenv/bin/activate`

7. Run the server in background 

    `python app.py &`


# What is devenv

`devenv` is the development environment for a setup with the necessary tools and configurations.  

# What is wsl

wsl is Windows Subsystem for Linux to run a full Linux distribution on a Window machine without the overhead of a traditional virtual machine. We need WSL2 on the window machine to install nix and devenx.

# What is `devenv shell` command

The `devenv shell` is the framework that intialize our developer environment `devenv`.  

# What is `devenv up` command

The `devenv up` starts processes required for development. It could start up a full development stack such as databases, web servers, backend services. 

# What is nix 

Nix is part of the Nix package manager to create isolated development environments. Anyone using the same configuration of nix will have the same setup across different machines. 
The nix-shell and devenv shell are similar here because it is to set up the isolated development environment. We use `devenv shell` here because nix is tightly controlled and difficult to use.