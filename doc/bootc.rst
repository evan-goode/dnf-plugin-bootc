..
  Copyright David Cantrell <dcantrell@redhat.com>
  SPDX-License-Identifier: GPL-2.0-or-later

=================
 DNF bootc Plugin
=================

Manage software on a bootc-based system.

--------
Synopsis
--------

``dnf bootc [options] <pkg-spec>...``

---------
Arguments
---------

``<pkg-spec>``
    Package specification for the package to download.
    Local RPMs can be specified as well. This is useful with the ``--source``
    option or if you want to download the same RPM again.

-------
Options
-------

All general DNF options are accepted, see `Options` in :manpage:`dnf(8)` for details.

``--help-cmd``
    Show this help.

``--arch <arch>[,<arch>...]``
    Limit the query to packages of given architectures (default is all compatible architectures with
    your system). To download packages with arch incompatible with your system use
    ``--forcearch=<arch>`` option to change basearch.

``--source``
    Download the source rpm. Enables source repositories of all enabled binary repositories.

``--debuginfo``
    Download the debuginfo rpm. Enables debuginfo repositories of all enabled binary repositories.

``--downloaddir``
    Download directory, default is the current directory (the directory must exist).

``--url``
    Instead of downloading, print list of urls where the rpms can be downloaded.

``--urlprotocol``
    Limit the protocol of the urls output by the --url option. Options are http, https, rsync, ftp.

``--resolve``
    Resolves dependencies of specified packages and downloads missing dependencies in the system.

``--alldeps``
    When used with ``--resolve``, download all dependencies (do not skip already installed ones).

--------
Examples
--------
``dnf download dnf``
    Download the latest dnf package to the current directory.

``dnf download --url dnf``
    Just print the remote location url where the dnf rpm can be downloaded from.

``dnf download --url --urlprotocols=https --urlprotocols=rsync dnf``
    Same as above, but limit urls to https or rsync urls.

``dnf download dnf --destdir /tmp/dnl``
    Download the latest dnf package to the /tmp/dnl directory (the directory must exist).

``dnf download dnf --source``
    Download the latest dnf source package to the current directory.

``dnf download rpm --debuginfo``
    Download the latest rpm-debuginfo package to the current directory.

``dnf download btanks --resolve``
    Download the latest btanks package and the uninstalled dependencies to the current directory.
