# Matif Covid19

A simple python script to complete Matif 4 Covid19 Task.

## Prerequisites

This module requires `JDK` and `virtualenv`. Please refer to their respective documentation for installation.

## Installation

Create new `virtualenv` and install depedencies:

- Windows:

    ```
    virtualenv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

- Linux / MacOS:

    ```bash
    virtualenv venv &&
    . venv/bin/activate && 
    pip install -r requirements.txt
    ```

## Usage

Always use `virtualenv` when interacting with these modules

- Windows:

  ```
  venv\Scripts\activate
  ```

- Linux / MacOS:

  ```bash
  . venv/bin/activate
  ```



### Basic Usage

Download the [PDF Source](https://v-class.gunadarma.ac.id/pluginfile.php/507173/mod_resource/content/1/Relasi%20Rekursi%20Covid19%20VClass%204.pdf), then rename it to `source.pdf`, and put the PDF inside the same directory as `app.py`

```
Matifcovid19
├───app.py
├───covid19.py
├───...
└───source.pdf
```

Then run the script with:

```bash
python app.py
```

This will create a new directory called `Grafik` with all the required graphs inside the folder, and prints out a Table inside the terminal.

```
Matifcovid19
├───Grafik
│   ├───pcbk1.png
│   ├───...
│   └───pcbk20.png
├───app.py
├───covid19.py
├───...
└───source.pdf
```

> _If there's an error in Java command, refer to `Java not recognized` in this documentation._

### Standalone command

If you only need one case to be solved, you could use `covid19.py`:

```DOS
python covid19.py
```

This will run an interactable prompt to gives out total cases at x day.


### Java not recognized

This mostly happens on Windows, somehow virtualenv PATH is purely isolated from the machine, other than that, you need to set your JDK into PATH by doing:


```DOS
SET PATH=%PATH%JAVA_BIN_PATH;
```

Change `JAVA_BIN_PATH` into your JDK bin path

Example:

`C:\Program Files\Java\jdk-11.0.7\bin`

```DOS
SET PATH=%PATH%C:\Program Files\Java\jdk-11.0.7\bin;
```