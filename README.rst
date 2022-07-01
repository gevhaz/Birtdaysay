Birthdaysay
===========

A small script that says when it's someone's birthday, through desktop
notifications. Birthday and name information is taken from a vCard (.vcf) file
which you can easily obtain by exporting the contacts on your phone. It's meant
to be run daily or so with e.g. a cron job.

Dependencies
------------

The two Python dependencies will be installed automatically and are ``PyGObject``
for desktop notifications and ``vobject`` for reading vCard files. ``PyGObject``
also relies on some non-Python dependencies, which can be installed on Arch
Linux like so:

.. code-block:: shell

    sudo pacman -S python cairo pkgconf gobject-introspection gtk3

You can see installation instructions for more systems on ``PyGObject``'s
website: https://pygobject.readthedocs.io/en/latest/getting_started.html

Installation
------------

There are two ways to install this project:

1. Clone this repository and run ``poetry install`` in it's catalog (assuming you
   have Poetry installed)
2. Download the wheel or tarball from Github and install with ``pip``.

Usage
-----

Use Birthdaysay by running it and providing a path to the vCard file, e.g:

.. code-block:: shell

    birthdaysay --contacts your_contacts.vcf

It will show birthdays coming up within a week from when you've run it. For this
to be useful, you have to set up a way to run it regularly, e.g. with cron,
anacron or systemd.
