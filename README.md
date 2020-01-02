# Asynchronous Addition Program

## Description
This is a basic program which adds two numbers asynchronously. It can be edited to run more complex tasks asynchronously as well. it runs on Python 3.7.

## Installation
IMPORTANT: This installation assumes Python 3.7 and pip are already installed.


First the directory of your preferred folder, the one where this repository will be cloned. Replace "/this/is/a/path/" with the path to your preferred folder.
```console
  # cd /this/is/a/path
```

Clone the repository.
```console
  $ git clone https://github.com/ethanparab/async_adder.git
```

Enter the directory.
```console
  # cd async_adder
```

(optional) Create a virtual environment.
```console
  $ mkdir .venv
  # python3 -m venv .venv
  # source .venv/bin/activate
```

Install the dependencies.
```console
  $ python3 -m pip install Django Celery redis django-extensions
```
The last dependency is only necessary to run the script provided additionally. If that functionality not necessary, it can be omitted if async_adder/async_adder/async_adder/settings.py file is edited slightly in "INSTALLED APPS" to omit it as well. However, if it is omitted here and not in the settings file or vice versa, an error will be returned. I recommend installation for the simplicity, but it may not be needed depending on usage.

Alternatively, you can install from the requirements.txt file, although this is not preferrable.
```console
  $ python3 -m pip install -r requirements.txt
```

Refer to https://redis.io/topics/quickstart for instructions for installing Redis.

## Usage

In one terminal window, start Redis.
```console
  # redis-server
```

In another terminal window, start a celery worker inside the /this/is/a/path/async_adder/async_adder/.
```console
  # cd /this/is/a/path/async_adder/async_adder/
  # celery worker -A async_adder
```
If an error is returned here, make sure the directory is correct and django-extensions was either omitted with the correct edits or installed earlier.

Minimize both windows. In a third, final terminal window, enter the same directory as the last one.
```console
  # cd /this/is/a/path/asunc_adder/async_adder/
```

Here, there are two options. The first is to run the script provided. This will only work with django-extensions installed. Substitute x and y with the two numbers you want to add. If x, y, or both are left blank, the blank argument will be given the value 0. A string passed will prompt an error.
```console
  # python3 manage.py runscript --script-args x y
```

Alternatively, if django-extensions was not installed, certain commands must be submitted to the shell of manage.py. To enter the shell, submit the following command instead.
```console
  # python3 manage.py shell
```

Submit the following commands in sequence, substituting x and y for the values you want to add. 
```pycon
>>> from thumbnailer.tasks import adding_task
>>> numsum = adding_task.delay(x, y)
>>> numsum.get()
```

In both courses of action, the line output is the result of the task.

## Credits
In this repo, code from the makers of Python, Redis, Django, and Celery were used. In addition, much of this was derived from a blog from Adam McQuistan (link: https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/)

## License
This project is licensed under AGPL v3, included in the file titled LICENSE.
