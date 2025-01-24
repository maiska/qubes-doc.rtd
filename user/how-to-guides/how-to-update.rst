=============
How to update
=============


*This page is about updating your system while staying on the same*
:ref:`supported version of Qubes OS <user/downloading-installing-upgrading/supported-releases:qubes os>` *. If you’re instead looking to upgrade from your current version of Qubes OS to a newer version, see* :doc:`Upgrade guides </user/downloading-installing-upgrading/upgrade/upgrade>` *.*

It is important to keep your Qubes OS system up-to-date to ensure you
have the latest security updates, as well as the latest non-security
enhancements and bug fixes.

Fully updating your Qubes OS system means updating:

- :ref:`dom0 <user/reference/glossary:dom0>`

- :ref:`templates <user/reference/glossary:template>`

- :ref:`standalones <user/reference/glossary:standalone>` (if you have any)



Security updates
----------------


Security updates are an extremely important part of keeping your Qubes
installation secure. When there is an important security incident, we
will issue a `Qubes Security Bulletin (QSB) <https://www.qubes-os.org/security/qsb/>`__ via the
`Qubes Security Pack (qubes-secpack) <https://www.qubes-os.org/security/pack/>`__. It is
very important to read each new QSB and follow any user instructions it
contains. Most of the time, simply updating your system normally, as
described below, will be sufficient to obtain security updates. However,
in some cases, special action may be required on your part, which will
be explained in the QSB.

Checking for updates
--------------------


By default, the **Qubes Update** tool will appear as an icon in the
Notification Area when updates are available.

|Qube Updates Available|

However, you can also start the tool manually by selecting it in the
Applications Menu under “Qubes Tools.” Even if no updates have been
detected, you can use this tool to check for updates manually at any
time by selecting all desired items from the list and clicking “Update”.

.. note::
      
      For information about how templates download updates, please see :ref:`Why don’t templates have network access? <user/how-to-guides/how-to-install-software:why don't templates have network access?>`       and the :ref:`Updates proxy <user/how-to-guides/how-to-install-software:updates proxy>`      .

By default, most qubes that are connected to the internet will
periodically check for updates for their parent templates. You can check
the date of the last update check in the “last checked” column. If
updates are available for any qube, you will receive a notification as
described above, and in the “Updates available” column you will see
“YES” for that qube(s). If the update check did not find any new
updates, “NO” will appear in the column. Respectively, for qubes that
are no longer supported, “OBSOLETE” will be displayed. However, if you
have any templates that do *not* have any online child qubes, you will
*not* receive update notifications for them. By default, after a week,
if updates for a given qube have not been checked, the value in the
“Updates available” column will be set to “MAYBE”.

Installing updates
------------------


The standard way to install updates is with the **Qubes Update** tool.
(However, you can also perform the same action via the `command-line interface <#command-line-interface>`__.)

|Qubes Update|

You can easily decide which qubes to update by clicking on the checkbox
in the column header. At startup, only the qubes for which updates are
known are selected for updating, but clicking on the mentioned checkbox
will also select all qubes with the “MAYBE” status. It is recommended to
update all qubes with the statuses “YES” and “MAYBE”.

Then simply follow the on-screen instructions, and the tool will
download and install all available updates for you. Note that if you are
downloading updates over Tor (``sys-whonix``), this can take a very long
time, especially if there are a lot of updates available.

Restarting after updating
-------------------------


Certain updates require certain components to be restarted in order for
the updates to take effect:

- QSBs may instruct you to restart certain components after installing
  updates.

- Dom0 should be restarted after all **Xen** and **kernel** updates.

- On Intel systems, dom0 should be restarted after all
  ``microcode_ctl`` updates.

- On AMD systems, dom0 should be restarted after all ``linux-firmware``
  updates.

- After updating a template, first shut down the template, then restart
  all running qubes based on that template. The updater will try to do
  this for you automatically in the last step of updating. Remember to
  save all your data before restarting!



AEM resealing after updating
----------------------------


If you use :doc:`Anti Evil Maid (AEM) </user/security-in-qubes/anti-evil-maid>`, you’ll have
to “reseal” after certain updates. It’s common for QSBs to contain
instructions to this effect. See the relevant QSB and the `AEM
README <https://github.com/QubesOS/qubes-antievilmaid/blob/main/README>`__
for details.

Command-line interface
----------------------


.. DANGER::
      
      **Warning:** Updating with direct commands such as dnf update, and apt update is not recommended, since these bypass built-in Qubes OS update security measures. Instead, we strongly recommend using the **Qubes Update** tool or its command-line equivalents, as described below. (By contrast, :doc:`installing </user/how-to-guides/how-to-install-software>`       packages using direct package manager commands is fine.)

Advanced users may wish to perform updates via the command-line
interface. To update templates and standalones non-interactively, use
the command ``qubes-vm-update``, and to update dom0, use
``qubes-dom0-update``. If you want to perform an update with more
advanced user-configurable options (e.g., custom pre- or post-update
scripts, custom workarounds), see:
:ref:`update.qubes-dom0 <user/advanced-topics/salt:\`\`update.qubes-dom0\`\`>` and
:ref:`update.qubes-vm <user/advanced-topics/salt:\`\`update.qubes-vm\`\`>`.

Advanced users may also be interested in learning :doc:`how to enable the testing repos </user/downloading-installing-upgrading/testing>`.

Upgrading to avoid EOL
----------------------


The above covers updating *within* a given operating system (OS)
release. Eventually, however, most OS releases will reach **end-of-life (EOL)**, after which point they will no longer be supported. This
applies to Qubes OS itself as well as OSes used in
:doc:`templates </user/templates/templates>` (and
:doc:`standalones </user/advanced-topics/standalones-and-hvms>`, if you have any).

**It’s very important that you use only supported releases so that you continue to receive security updates.** This means that you *must*
periodically upgrade Qubes OS and your templates before they reach EOL.
You can always see which versions of Qubes OS and select templates are
supported on :doc:`Supported releases </user/downloading-installing-upgrading/supported-releases>`.

In the case of Qubes OS itself, we will make an
`announcement <https://www.qubes-os.org/news/categories/>`__ when a supported Qubes OS
release is approaching EOL and another when it has actually reached EOL,
and we will provide :doc:`instructions for upgrading to the next stable supported Qubes OS release </user/downloading-installing-upgrading/upgrade/upgrade>`.

Periodic upgrades are also important for templates. For example, you
might be using a :doc:`Fedora template </user/templates/fedora/fedora>`. The
`Fedora Project <https://getfedora.org/>`__ is independent of the Qubes
OS Project. They set their own
`schedule <https://fedoraproject.org/wiki/Fedora_Release_Life_Cycle#Maintenance_Schedule>`__
for when each Fedora release reaches EOL. You can always find out when
an OS reaches EOL from the upstream project that maintains it. We also
pass along any EOL notices we receive for official template OSes as a
convenience to Qubes users (see the :ref:`supported template releases <user/downloading-installing-upgrading/supported-releases:templates>`).

The one exception to all this is the specific release used for dom0 (not
to be confused with Qubes OS as a whole), which :ref:`doesn’t have to be upgraded <user/downloading-installing-upgrading/supported-releases:note on dom0 and eol>`.

.. |Qube Updates Available| image:: /attachment/doc/r4.2-qube-updates-available.png
   

.. |Qubes Update| image:: /attachment/doc/r4.2-software-update.png
   
