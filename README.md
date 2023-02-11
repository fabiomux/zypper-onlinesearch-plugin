# Zypper-Onlinesearch-Plugin
Zypper plugin which make use of the [zypper-onlinesearch](https://github.com/fabiomux/zypper-onlinesearch) gem
to check and upgrade repositories.

## Installation
This project can be easily installed as a normal RPM package from 
[openSUSE Build Service](https://build.opensuse.org/package/show/home:FabioMux/zypper-onlinesearch-plugin).

Add the repository using the right version:
```
$ sudo zypper ar https://download.opensuse.org/repositories/home:/FabioMux/openSUSE_Leap_15.1/home:FabioMux.repo
```

Install the rpm:
```
$ sudo zypper in zypper-onlinesearch-plugin
```

The package zypper-onlinesearch is a dependence and will be automatically installed.

## Usage
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

All the commands available as `zypper-onlinesearch <options>` are now available as `zypper onlinesearch <options>`.

## More help
zypper-onlinesearch wiki: https://github.com/fabiomux/zypper-onlinesearch/wiki
