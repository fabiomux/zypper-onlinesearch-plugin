# Zypper-Onlinesearch-Plugin

Zypper plugin which make use of the [zypper-onlinesearch][zypper_onlinesearch] gem to find packages
through the popular *software.opensuse.org* search engine inside a terminal session.

## Installation

There are several options to install this plugin.

### From the openSUSE Build Service repository

This application has been packaged in my personal OBS repository so you can install It
as a common RPM package:
- Add the repository URL in your list;
- install the package from Yast or Zypper.

Being the repository URL slightly changing from a version to another, I included all the steps
in the related [project page][project_page] on Freeaptitude blog.

Installing this plugin the package *rubygem-zypper-onlinesearch* will be automatically selected.

### Cloning this repo

After cloning the repo:
```shell
$ git clone https://github.com/fabiomux/zypper-upgraderepo-plugin.git
```

To install, execute the command:
```shell
$ make install
```

And to uninstall:
```shell
$ make uninstall
```

Make sure to have the *zypper-onlinesearch* gem installed or install it manually.

## Usage

Any operaton performed with *zypper-onlinesearch* gem is now available as:
```
$ zypper onlinesearch <operation> <options>
```

## Get help

When this plugin is correctly installed you can see it in the list of subcommands:
```
$ zypper help subcommand
```

Read the man page with:
```
$ zypper help onlinesearch
```

For a quick help:
```
$ zypper onlinesearch --help
```

## More help

More info is available at:
- the [Zypper-Onlinesearch README file][zypper_onlinesearch_readme].


[project_page]: https://freeaptitude.altervista.org/projects/zypper-onlinesearch.html "Zypper-Onlinesearch project page"
[zypper_onlinesearch]: https://github.com/fabiomux/zypper-onlinesearch "Zypper-Onlinesearch Github project page"
[zypper_onlinesearch_readme]: https://github.com/fabiomux/zypper-onlinesearch#readme "Zypper-Onlinesearch README"
