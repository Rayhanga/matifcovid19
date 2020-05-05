# Matif Covid19

Sebuah script python untuk mengerjakan tugas Vclass Matif 4 Topik 4.

## Installation

Install `virtualenv`:

```bash
pip install virtualenv
```

Create new `virtualenv` and install depedencies:

- Windows:

    ```
    virtualenv venv
    venv\Scripts\activate &&
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

```bash
python app.py
```

This will create a new directory called `Grafik` with all the required graphs inside the folder, and prints out a Table inside the terminal.