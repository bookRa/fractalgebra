# FractAlgebra
A simple fraction calculator CLI

## Features
* Accepts arbitrarily many fractions, not just two at a time
* returns the answer in lowest common denominator

## Installing

 ### Using `pipx` (simple and quick 🚀)
 [pipx](https://github.com/pypa/pipx#pipx--install-and-run-python-applications-in-isolated-environments) allows you to install (or just test out using the `run` command) python CLIs safely using Isolated Environments
 
 1. Follow the [instructions to install pipx](https://pypa.github.io/pipx/installation/) on your system 
 2. ```bash
    > pipx install fractalgebra
        installed package fractalgebra 0.1.1, installed using Python 3.9.7
        These apps are now globally available
        - fa
        done! ✨ 🌟 ✨
    > fa 1/2 + -3_3/2
        4
    
### Build From Source

### `TODO:` Downloadable Binary
 > time-permitting, I would use a tool like [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/operating-mode.html)
in combination with GitHub Actions to publish an executable (or folder) which any user can simply drop into their file 
system and easily begin using fractalgebra. 

## Usage

1. Provide a space-delimeted math string using rational numbers and math operators to the `fa` command
    * A rational number can be a whole number (`3`), a fraction  a mixed fraction formatted with an
    underscore (`3_3/4`) or a fraction (`-9/4`).
    * Negative signs are allowed anywhere 
    __except on the fraction part of a mixed fraction__. Mathematically, this is ambiguous
    (at least based on my research)
    * The only math operations currently supported are add (`+`), subtract (`-`),
     multiply (`*`), and divide(`/`) 


## Contributing

### Building the Project
### Environment Setup