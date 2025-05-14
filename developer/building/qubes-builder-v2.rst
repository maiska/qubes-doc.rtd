================
Qubes builder v2
================


This is a brief introduction to using Qubes Builder v2 to work with Qubes OS sources. It will walk you through installing and configuring Builder v2, and using it to fetch and build Qubes OS packages.

For details and customization, use `Qubes OS v2 builder documentation <https://github.com/QubesOS/qubes-builderv2/>`__.

Overview
--------


In the second generation of Qubes OS builder, container or disposable qube isolation is used to perform every stage of the build and release process. From fetching sources to building, everything is executed inside an isolated *cage* (either a disposable or a container) using an *executor*. For every command that needs to perform an action on sources, like cloning and verifying Git repos, rendering a SPEC file, generating SRPM or Debian source packages, a new cage is used. Only the signing, publishing, and uploading stages are executed locally outside a cage.

Setup
-----


This is a simple setup using a docker executor. This is a good default choice; if you don’t know which executor to use, use docker.

1. First, decide what qube you are going to use when working with Qubes Builder v2. It can be an AppVM or a Standalone qube, with some steps different between the two.

2. Installing dependencies
   If you want to use an app qube for developing, install dependencies in the template. If you are using a standalone, install them in the qube itself. Dependencies are specified in ``dependencies-*. txt`` files in the main builder directory, and you can install them easily in the following ways:

   1. for Fedora, use:



   .. code:: bash

         $ sudo dnf install $(cat dependencies-fedora.txt)
         $ test -f /usr/share/qubes/marker-vm && sudo dnf install qubes-gpg-split


   2. for Debian (note: some Debian packages require Debian version 13 or later), use:





   .. code:: bash

         $ sudo apt install $(cat dependencies-debian.txt)
         $ test -f /usr/share/qubes/marker-vm && sudo apt install qubes-gpg-split

   If you have installed dependencies in the template, close it, and (re)start the development qube.

3. Clone the qubes-builder v2 repository into a location of your choice: ``shell     git clone https://github.com/QubesOS/qubes-builderv2     cd qubes-builderv2/``

4. If you haven’t previously used docker in the current qube, you need to set up some permissions. In particular, the user has to be added to the ``docker`` group: ``shell    $ sudo usermod -aG docker user`` Next, **restart the qube**.

5. Finally, you need to generate a docker image: ``shell    $ tools/generate-container-image.sh docker``
   In an app qube, as ``/var/lib/docker`` is not persistent by default, you also need to use :doc:`bind-dirs </user/advanced-topics/bind-dirs>` to avoid repeating this step after reboot, adding the following to the ``/rw/config/qubes-bind-dirs.d/docker.conf`` file in this qube:

   .. code:: bash

         binds+=( '/var/lib/docker' )





Configuration
-------------


To use Qubes OS Builder v2, you need to have a ``builder.yml`` configuration file. You can use one of the sample files from the ``example-configs/`` directory; for a more readable ``builder.yml``, you can also include one of the files from that directory in your ``builder.yml``. An example ``builder.yml`` is:

.. code:: bash

:inline-0:`# include configuration relevant for the current release` :inline-1:`
` :inline-2:`include` :inline-3:`:` :inline-1:`
` :inline-4:`-` :inline-1:` ` :inline-5:`example-configs/qubes-os-r4.2.yml` :inline-1:`

` :inline-0:`# which repository to use to fetch sources` :inline-1:`
` :inline-2:`use-qubes-repo` :inline-3:`:` :inline-1:`
  ` :inline-2:`version` :inline-3:`:` :inline-1:` ` :inline-5:`4.2` :inline-1:`
  ` :inline-2:`testing` :inline-3:`:` :inline-1:` ` :inline-5:`true` :inline-1:`

` :inline-0:`# each package built will have local build number appended to package release` :inline-1:`
` :inline-0:`# number. It makes it easier to update in testing environment` :inline-1:`
` :inline-2:`increment-devel-versions` :inline-3:`:` :inline-1:` ` :inline-5:`true` :inline-1:`

` :inline-0:`# reduce output` :inline-1:`
` :inline-2:`debug` :inline-3:`:` :inline-1:` ` :inline-5:`false` :inline-1:`

` :inline-0:`# this can be set to true if you do not want sources to be automatically` :inline-1:`
` :inline-0:`# fetched from git` :inline-1:`
` :inline-2:`skip-git-fetch` :inline-3:`:` :inline-1:` ` :inline-5:`false` :inline-1:`

` :inline-0:`# executor configuration` :inline-1:`
` :inline-2:`executor` :inline-3:`:` :inline-1:`
  ` :inline-2:`type` :inline-3:`:` :inline-1:` ` :inline-5:`docker` :inline-1:`
  ` :inline-2:`options` :inline-3:`:` :inline-1:`
    ` :inline-2:`image` :inline-3:`:` :inline-1:` ` :inline-6:`"qubes-builder-fedora:latest"` 


Using Builder v2
----------------


To fetch sources - in this example, for the ``core-admin-client`` package, you can use the following command:

.. code:: bash

      $ ./qb -c core-admin-client package fetch


This will fetch the sources for the listed package and place them in ``artifacts/sources`` directory.

To build a package (from sources in the ``artifacts/sources`` directory), use:

.. code:: bash

      $ ./qb -c core-admin-client package fetch prep build


or, if you want to build for a specific target (``host-fc37`` is a ``dom0`` using Fedora 37, ``vm-fc40`` would be a qube using Fedora 40 etc.), use:

.. code:: bash

      $ ./qb -c core-admin-client -d host-fc37 package fetch prep build


If you want to fetch the entire Qubes OS source use the following:

.. code:: bash

      $ ./qb package fetch


**caution**: some repositories might have additional requirements. You can disable repositories that are not needed in the ``example-configs/*.yml`` file you are using by commenting them out. In particular, ``python-fido2``, ``lvm`` and ``windows``-related repositories have special requirements.


.. role:: inline-0
   :class: comment single

.. role:: inline-1
   :class: whitespace

.. role:: inline-2
   :class: name tag

.. role:: inline-3
   :class: punctuation

.. role:: inline-4
   :class: indicator punctuation

.. role:: inline-5
   :class: literal plain scalar

.. role:: inline-6
   :class: literal string

