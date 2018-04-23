# optimoida

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

## :page_facing_up: Overview

The **optimoida** is a command line application to **optimize image file** (`jpg`, `png` only) by [**TinyPNG**](https://tinypng.com/)

### DEMO

[![asciicast](https://asciinema.org/a/177778.png)](https://asciinema.org/a/177778)

## :hourglass: Prepare to use optimoida

### 1. Get TinyPNG API Key

You have to get TinyPNG API Key at [here](https://tinypng.com/developers).

### 2. Write optimoida.ini

Please write API Key you got to `optimoida.ini`.
And move `optimoida.ini` to `~/.optimoida.ini`

```
$ mv optimoida.ini ~/.optimoida.ini
```

## :pencil2: Usage

```
optimoida [PATH [PATH ...]]
```

### argument

* **PATH** - The image file or directory path. allowed multiple argument.

## :inbox_tray: Installation

```
$ pip install optimoida
```

or

```
$ git clone git@github.com:alice1017/optimoida.git
$ cd optimoida
$ python setup.py build install
```

## :eyes: Contribution

1. Forks on [Github](https://github.com/alice1017/optimoida)
2. Find a bug? Send a pull request to get it merged and published.
