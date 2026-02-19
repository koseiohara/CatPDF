# CatPDF
LaTeX based figure concatenation tool


## Test Environment
- macOS 15.1
    - latexmk 4.86
    - Python 3.9.6

## Install
Install the source code from GitHub
```sh
$ git clone https://github.com/koseiohara/CatPDF.git
$ cd CatPDF
$ make install
```
Source files will be copied to the directory specified by `INSTALL` in the `Makefile`.
Add this directory to the environment variables `PATH` and `PYTHONPATH`.  

The `Makefile` can also be used to uninstall the tool
```sh
$ make uninstall
```
To change the version of this tool, execute `make update`.

## Usage
This tool automatically generates and compiles LaTeX source code.
Input files can be any figure formats supported by LaTeX's `includegraphics` command.
The output file is generated only in PDF format.


### Command
```sh
$ catpdf <options> input1.pdf input2.pdf ... output.pdf
```

### Options
#### -tile
Default: `h`.  
`horizontal`/`h`, `vertical`/`v`, or `<columns>x<rows>` format.
If `-tile horizontal` is specified, all figures are arranged horizontally.
Similarly, if `-tile vertical` is specified, all figures are arranged vertically.
If `-tile <columns>x<rows>` (e.g., `-tile 2x3`) is specified, figures are arranged in a `<columns>` x `<rows>` grid.

#### -margin
Default: `0`.  
Margin between figures.
If an integer `n` is specified (e.g., `-margin 100`), the margin between figures is set to `n` pixels.
If margin is specified as `nxm` like `-margin 30x40`, the horizontal margin between adjacent figures is set to `n` pixels, and the vertical margin between figures above and below is set to `m` pixels.

#### -align
Default: `l`.  
Horizontal alignment.  
`left`/`l`, `center`/`c`, or `right`/`r`.

#### -f
Default: `None`  
If `-f` is not specified, the program will confirm the input and output files and prompt the user to enter `y` before executing the script.


