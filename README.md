# Pywirt - Python Windows Incident Response Toolkit

Tested on Windows 10

## Overview

Pywirt is a toolkit designed to speed up incident response processes by collecting various types of information from Windows operating systems using winrm. 

## Features

Pywirt can collect the following information:

- IP Configuration
- Users and groups
- Tasks and services
- Task Scheduler
- Registry control
- Active TCP and UDP ports
- File sharing
- Files
- Firewall configuration
- Sessions with other systems
- Open sessions
- Log entries

## Installation

To install Pywirt, follow these steps:

1. Clone the repository: `git clone https://github.com/anil-yelken/pywirt`
2. Change into the Pywirt directory: `cd pywirt`
3. Install the pywinrm package: `pip3 install pywinrm`

## Usage

To use Pywirt, you will need to specify the following information in a file called `cred_list.txt`:

IP|Username|Password

Here is an example of what the `cred_list.txt` file might look like:

![cred_list.jpg](https://github.com/anil-yelken/pywirt/blob/main/cred_list.jpg)

Here is an example of the Pywirt interface:

![pywint.jpg](https://github.com/anil-yelken/pywirt/blob/main/pywint.jpg)

## Contact

- Twitter: https://twitter.com/anilyelken06
- Medium: https://medium.com/@anilyelken
