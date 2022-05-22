*You may also be interested in the article*\ `Introducing the Qubes
Admin API <https://www.qubes-os.org/news/2017/06/27/qubes-admin-api/>`__\ *.*

Goals
-----

The goals of the Admin API system is to provide a way for the user to
manage the domains without direct access to dom0.

Foreseen benefits include:

-  Ability to remotely manage the Qubes OS.
-  Possibility to create multi-user system, where different users are
   able to use different sets of domains, possibly overlapping. This
   would also require to have separate GUI domain.

The API would be used by:

-  Qubes OS Manager (or any tools that would replace it)
-  CLI tools, when run from another VM (and possibly also from dom0)
-  remote management tools
-  any custom tools

Threat model
------------

TBD

Components
----------

.. figure:: /attachment/doc/admin-api-architecture.svg
   :alt: Admin API Architecture

   Admin API Architecture

A central entity in the Qubes Admin API system is a ``qubesd`` daemon,
which holds information about all domains in the system and mediates all
actions (like starting and stopping a qube) with ``libvirtd``. The
``qubesd`` daemon also manages the ``qubes.xml`` file, which stores all
persistent state information and dispatches events to extensions. Last
but not least, ``qubesd`` is responsible for querying the RPC policy for
qrexec daemon.

The ``qubesd`` daemon may be accessed from other domains through a set
of qrexec API calls called the “Admin API”. This API is the intended
management interface supported by the Qubes OS. The API is stable. When
called, the RPC handler performs basic validation and forwards the
request to the ``qubesd`` via UNIX domain socket. The socket API is
private, unstable, and not yet documented.

The calls
---------

The API should be implemented as a set of qrexec calls. This is to make
it easy to set the policy using current mechanism.

:doc:`View this table on a fullscreen page. </developer/services/admin-api-table>`

+---------------+---+---+-----------------+-------------------------+---+
| call          | d | a | inside          | return                  | n |
|               | e | r |                 |                         | o |
|               | s | g |                 |                         | t |
|               | t | u |                 |                         | e |
|               |   | m |                 |                         |   |
|               |   | e |                 |                         |   |
|               |   | n |                 |                         |   |
|               |   | t |                 |                         |   |
+===============+===+===+=================+=========================+===+
| ``admin.v     | ` | - | -               | ``<class>\n``           |   |
| mclass.List`` | ` |   |                 |                         |   |
|               | d |   |                 |                         |   |
|               | o |   |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``ad          | ` | - | -               | ``<name> class=<c       |   |
| min.vm.List`` | ` |   |                 | lass> state=<state>\n`` |   |
|               | d |   |                 |                         |   |
|               | o |   |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | | |   |                 |                         |   |
|               | < |   |                 |                         |   |
|               | v |   |                 |                         |   |
|               | m |   |                 |                         |   |
|               | > |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| `             | ` | t | ``name=<name>   | -                       |   |
| `admin.vm.Cre | ` | e | label=<label>`` |                         |   |
| ate.<class>`` | d | m |                 |                         |   |
|               | o | p |                 |                         |   |
|               | m | l |                 |                         |   |
|               | 0 | a |                 |                         |   |
|               | ` | t |                 |                         |   |
|               | ` | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin       | ` | t | ``name=<n       | -                       | e |
| .vm.CreateInP | ` | e | ame> label=<lab |                         | i |
| ool.<class>`` | d | m | el>``\ \ ``pool |                         | t |
|               | o | p | =<pool> pool:<v |                         | h |
|               | m | l | olume>=<pool>`` |                         | e |
|               | 0 | a |                 |                         | r |
|               | ` | t |                 |                         | u |
|               | ` | e |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | = |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | : |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | = |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
+---------------+---+---+-----------------+-------------------------+---+
| ``a           | t | - | -               | name                    | C |
| dmin.vm.Creat | e |   |                 |                         | r |
| eDisposable`` | m |   |                 |                         | e |
|               | p |   |                 |                         | a |
|               | l |   |                 |                         | t |
|               | a |   |                 |                         | e |
|               | t |   |                 |                         | n |
|               | e |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | D |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | V |
|               |   |   |                 |                         | M |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | A |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | V |
|               |   |   |                 |                         | M |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | _ |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | T |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | 0 |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | _ |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | V |
|               |   |   |                 |                         | M |
|               |   |   |                 |                         | ; |
|               |   |   |                 |                         | V |
|               |   |   |                 |                         | M |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ; |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | C |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | D |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | V |
|               |   |   |                 |                         | M |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | ( |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | ) |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | . |
+---------------+---+---+-----------------+-------------------------+---+
| ``admi        | v | - | -               | -                       |   |
| n.vm.Remove`` | m |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin       | ` | - | -               | ``<property>\n``        |   |
| .label.List`` | ` |   |                 |                         |   |
|               | d |   |                 |                         |   |
|               | o |   |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.l     | ` | l | ``0xRRGGBB``    | -                       |   |
| abel.Create`` | ` | a |                 |                         |   |
|               | d | b |                 |                         |   |
|               | o | e |                 |                         |   |
|               | m | l |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admi        | ` | l | -               | ``0xRRGGBB``            |   |
| n.label.Get`` | ` | a |                 |                         |   |
|               | d | b |                 |                         |   |
|               | o | e |                 |                         |   |
|               | m | l |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.      | ` | l | -               | ``<label-index>``       |   |
| label.Index`` | ` | a |                 |                         |   |
|               | d | b |                 |                         |   |
|               | o | e |                 |                         |   |
|               | m | l |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.l     | ` | l | -               | -                       |   |
| abel.Remove`` | ` | a |                 |                         |   |
|               | d | b |                 |                         |   |
|               | o | e |                 |                         |   |
|               | m | l |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.pr    | ` | - | -               | ``<property>\n``        |   |
| operty.List`` | ` |   |                 |                         |   |
|               | d |   |                 |                         |   |
|               | o |   |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.p     | ` | p | -               | ``de                    | T |
| roperty.Get`` | ` | r |                 | fault={True|False}``\ \ | y |
|               | d | o |                 |  ``type={str|int|bool|v | p |
|               | o | p |                 | m|label|list} <value>`` | e |
|               | m | e |                 |                         | ` |
|               | 0 | r |                 |                         | ` |
|               | ` | t |                 |                         | l |
|               | ` | y |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | R |
|               |   |   |                 |                         | 4 |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | 1 |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | V |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | x |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | . |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.prop  | ` | - | -               | ``<prop                 | G |
| erty.GetAll`` | ` |   |                 | erty-name> <full-value- | e |
|               | d |   |                 | as-in-property.Get>\n`` | t |
|               | o |   |                 |                         | a |
|               | m |   |                 |                         | l |
|               | 0 |   |                 |                         | l |
|               | ` |   |                 |                         | t |
|               | ` |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | E |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | G |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | x |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | \ |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | \ |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | \ |
|               |   |   |                 |                         | \ |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | . |
+---------------+---+---+-----------------+-------------------------+---+
| ``a           | ` | p | -               | ``type={str|int|bool|v  | T |
| dmin.property | ` | r |                 | m|label|list} <value>`` | y |
| .GetDefault`` | d | o |                 |                         | p |
|               | o | p |                 |                         | e |
|               | m | e |                 |                         | ` |
|               | 0 | r |                 |                         | ` |
|               | ` | t |                 |                         | l |
|               | ` | y |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | R |
|               |   |   |                 |                         | 4 |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | 1 |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | V |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | x |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | . |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.pr    | ` | p | -               | ``help``                |   |
| operty.Help`` | ` | r |                 |                         |   |
|               | d | o |                 |                         |   |
|               | o | p |                 |                         |   |
|               | m | e |                 |                         |   |
|               | 0 | r |                 |                         |   |
|               | ` | t |                 |                         |   |
|               | ` | y |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.prope | ` | p | -               | ``help.rst``            |   |
| rty.HelpRst`` | ` | r |                 |                         |   |
|               | d | o |                 |                         |   |
|               | o | p |                 |                         |   |
|               | m | e |                 |                         |   |
|               | 0 | r |                 |                         |   |
|               | ` | t |                 |                         |   |
|               | ` | y |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.pro   | ` | p | -               | -                       |   |
| perty.Reset`` | ` | r |                 |                         |   |
|               | d | o |                 |                         |   |
|               | o | p |                 |                         |   |
|               | m | e |                 |                         |   |
|               | 0 | r |                 |                         |   |
|               | ` | t |                 |                         |   |
|               | ` | y |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.p     | ` | p | value           | -                       |   |
| roperty.Set`` | ` | r |                 |                         |   |
|               | d | o |                 |                         |   |
|               | o | p |                 |                         |   |
|               | m | e |                 |                         |   |
|               | 0 | r |                 |                         |   |
|               | ` | t |                 |                         |   |
|               | ` | y |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.pr | v | - | -               | ``<property>\n``        |   |
| operty.List`` | m |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.p  | v | p | -               | ``de                    | T |
| roperty.Get`` | m | r |                 | fault={True|False}``\ \ | y |
|               |   | o |                 |  ``type={str|int|bool|v | p |
|               |   | p |                 | m|label|list} <value>`` | e |
|               |   | e |                 |                         | ` |
|               |   | r |                 |                         | ` |
|               |   | t |                 |                         | l |
|               |   | y |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | R |
|               |   |   |                 |                         | 4 |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | 1 |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | E |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | x |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | . |
+---------------+---+---+-----------------+-------------------------+---+
| ``            | v | - | -               | ``<prop                 | G |
| admin.vm.prop | m |   |                 | erty-name> <full-value- | e |
| erty.GetAll`` |   |   |                 | as-in-property.Get>\n`` | t |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | E |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | G |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | x |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | \ |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | \ |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | \ |
|               |   |   |                 |                         | \ |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | . |
+---------------+---+---+-----------------+-------------------------+---+
| ``admi        | v | p | -               | ``type={str|int|bool|v  | T |
| n.vm.property | m | r |                 | m|label|type} <value>`` | y |
| .GetDefault`` |   | o |                 |                         | p |
|               |   | p |                 |                         | e |
|               |   | e |                 |                         | ` |
|               |   | r |                 |                         | ` |
|               |   | t |                 |                         | l |
|               |   | y |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | R |
|               |   |   |                 |                         | 4 |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | 1 |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | E |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | x |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | . |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.pr | v | p | -               | ``help``                |   |
| operty.Help`` | m | r |                 |                         |   |
|               |   | o |                 |                         |   |
|               |   | p |                 |                         |   |
|               |   | e |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | y |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``a           | v | p | -               | ``help.rst``            |   |
| dmin.vm.prope | m | r |                 |                         |   |
| rty.HelpRst`` |   | o |                 |                         |   |
|               |   | p |                 |                         |   |
|               |   | e |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | y |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| `             | v | p | -               | -                       |   |
| `admin.vm.pro | m | r |                 |                         |   |
| perty.Reset`` |   | o |                 |                         |   |
|               |   | p |                 |                         |   |
|               |   | e |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | y |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.p  | v | p | value           | -                       |   |
| roperty.Set`` | m | r |                 |                         |   |
|               |   | o |                 |                         |   |
|               |   | p |                 |                         |   |
|               |   | e |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | y |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.f  | v | - | -               | ``<feature>\n``         |   |
| eature.List`` | m |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.   | v | f | -               | value                   |   |
| feature.Get`` | m | e |                 |                         |   |
|               |   | a |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | u |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.f  | v | f | -               | value                   |   |
| eature.CheckW | m | e |                 |                         |   |
| ithTemplate`` |   | a |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | u |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.v     | v | f | -               | value                   |   |
| m.feature.Che | m | e |                 |                         |   |
| ckWithNetvm`` |   | a |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | u |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.   | v | f | -               | value                   |   |
| feature.Check | m | e |                 |                         |   |
| WithAdminVM`` |   | a |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | u |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.v     | v | f | -               | value                   |   |
| m.feature.Che | m | e |                 |                         |   |
| ckWithTemplat |   | a |                 |                         |   |
| eAndAdminVM`` |   | t |                 |                         |   |
|               |   | u |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| `             | v | f | -               | -                       |   |
| `admin.vm.fea | m | e |                 |                         |   |
| ture.Remove`` |   | a |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | u |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.   | v | f | value           | -                       |   |
| feature.Set`` | m | e |                 |                         |   |
|               |   | a |                 |                         |   |
|               |   | t |                 |                         |   |
|               |   | u |                 |                         |   |
|               |   | r |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.      | v | - | -               | ``<tag>\n``             |   |
| vm.tag.List`` | m |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin       | v | t | -               | ``0`` or ``1``          | r |
| .vm.tag.Get`` | m | a |                 |                         | e |
|               |   | g |                 |                         | t |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ? |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm    | v | t | -               | -                       |   |
| .tag.Remove`` | m | a |                 |                         |   |
|               |   | g |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin       | v | t | -               | -                       |   |
| .vm.tag.Set`` | m | a |                 |                         |   |
|               |   | g |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.f  | v | - | -               | ``<rule>\n``            | r |
| irewall.Get`` | m |   |                 |                         | u |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | x |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         |   |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | / |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | / |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | / |
|               |   |   |                 |                         | # |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | 4 |
|               |   |   |                 |                         | x |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | _ |
|               |   |   |                 |                         | _ |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | x |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | = |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | = |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | ; |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | = |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ( |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ) |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.f  | v | - | ``<rule>\n``    | -                       | s |
| irewall.Set`` | m |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | G |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | x |
+---------------+---+---+-----------------+-------------------------+---+
| ``            | v | - | -               | -                       | f |
| admin.vm.fire | m |   |                 |                         | o |
| wall.Reload`` |   |   |                 |                         | r |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | e |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.      | v | d | options         | -                       | ` |
| vm.device.<cl | m | e |                 |                         | ` |
| ass>.Attach`` |   | v |                 |                         | d |
|               |   | i |                 |                         | e |
|               |   | c |                 |                         | v |
|               |   | e |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | + |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | = |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | ; |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | = |
|               |   |   |                 |                         | T |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | “ |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | ” |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ( |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | ) |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.      | v | d | -               | -                       | ` |
| vm.device.<cl | m | e |                 |                         | ` |
| ass>.Detach`` |   | v |                 |                         | d |
|               |   | i |                 |                         | e |
|               |   | c |                 |                         | v |
|               |   | e |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | + |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
+---------------+---+---+-----------------+-------------------------+---+
| ``a           | v | d | ``True``        | -                       | ` |
| dmin.vm.devic | m | e | \ \|\ ``False`` |                         | ` |
| e.<class>.Set |   | v |                 |                         | d |
| .persistent`` |   | i |                 |                         | e |
|               |   | c |                 |                         | v |
|               |   | e |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | + |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
+---------------+---+---+-----------------+-------------------------+---+
| ``admi        | v | - | -               | `                       | o |
| n.vm.device.< | m |   |                 | `<device> <options>\n`` | p |
| class>.List`` |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | = |
|               |   |   |                 |                         | T |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | “ |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | ” |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | ( |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | ) |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.   | v | d | -               | ``<dev                  | o |
| device.<class | m | e |                 | ice-ident> <properties> | p |
| >.Available`` |   | v |                 |  description=<desc>\n`` | t |
|               |   | i |                 |                         | i |
|               |   | c |                 |                         | o |
|               |   | e |                 |                         | n |
|               |   | - |                 |                         | a |
|               |   | i |                 |                         | l |
|               |   | d |                 |                         | s |
|               |   | e |                 |                         | e |
|               |   | n |                 |                         | r |
|               |   | t |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | ( |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | ) |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | = |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | \ |
|               |   |   |                 |                         |   |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
+---------------+---+---+-----------------+-------------------------+---+
| ``admi        | ` | - | -               | ``<pool>\n``            |   |
| n.pool.List`` | ` |   |                 |                         |   |
|               | d |   |                 |                         |   |
|               | o |   |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.pool. | ` | - | -               | ``<pool-dri             | P |
| ListDrivers`` | ` |   |                 | ver> <property> ...\n`` | r |
|               | d |   |                 |                         | o |
|               | o |   |                 |                         | p |
|               | m |   |                 |                         | e |
|               | 0 |   |                 |                         | r |
|               | ` |   |                 |                         | t |
|               | ` |   |                 |                         | i |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | A |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
+---------------+---+---+-----------------+-------------------------+---+
| ``admi        | ` | p | -               | `                       |   |
| n.pool.Info`` | ` | o |                 | `<property>=<value>\n`` |   |
|               | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``adm         | ` | d | ``<proper       | -                       |   |
| in.pool.Add`` | ` | r | ty>=<value>\n`` |                         |   |
|               | d | i |                 |                         |   |
|               | o | v |                 |                         |   |
|               | m | e |                 |                         |   |
|               | 0 | r |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.po    | ` | p | ``<value>``     | -                       |   |
| ol.Set.revisi | ` | o |                 |                         |   |
| ons_to_keep`` | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.      | ` | p | -               | -                       |   |
| pool.Remove`` | ` | o |                 |                         |   |
|               | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.pool. | ` | p | -               | volume id               |   |
| volume.List`` | ` | o |                 |                         |   |
|               | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.pool. | ` | p | vid             | `                       |   |
| volume.Info`` | ` | o |                 | `<property>=<value>\n`` |   |
|               | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``ad          | ` | p | ``              | -                       |   |
| min.pool.volu | ` | o | <vid> <value>`` |                         |   |
| me.Set.revisi | d | o |                 |                         |   |
| ons_to_keep`` | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.p     | ` | p | vid             | ``<snapshot>\n``        |   |
| ool.volume.Li | ` | o |                 |                         |   |
| stSnapshots`` | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``ad          | ` | p | vid             | snapshot                |   |
| min.pool.volu | ` | o |                 |                         |   |
| me.Snapshot`` | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``            | ` | p | ``<vi           | -                       |   |
| admin.pool.vo | ` | o | d> <snapshot>`` |                         |   |
| lume.Revert`` | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``            | ` | p | ``<vid> <s      | -                       |   |
| admin.pool.vo | ` | o | ize_in_bytes>`` |                         |   |
| lume.Resize`` | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``            | ` | p | ``<vid>\n<raw   | -                       |   |
| admin.pool.vo | ` | o |  volume data>`` |                         |   |
| lume.Import`` | d | o |                 |                         |   |
|               | o | l |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``adm         | ` | p | vid             | token, to be used in    | o |
| in.pool.volum | ` | o |                 | ``admi                  | b |
| e.CloneFrom`` | d | o |                 | n.pool.volume.CloneTo`` | t |
|               | o | l |                 |                         | a |
|               | m |   |                 |                         | i |
|               | 0 |   |                 |                         | n |
|               | ` |   |                 |                         | a |
|               | ` |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ; |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ’ |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | C |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | T |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | s |
+---------------+---+---+-----------------+-------------------------+---+
| ``a           | ` | p | ``              | -                       | c |
| dmin.pool.vol | ` | o | <vid> <token>`` |                         | o |
| ume.CloneTo`` | d | o |                 |                         | p |
|               | o | l |                 |                         | y |
|               | m |   |                 |                         | v |
|               | 0 |   |                 |                         | o |
|               | ` |   |                 |                         | l |
|               | ` |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.   | v | - | -               | ``<volume>\n``          | ` |
| volume.List`` | m |   |                 |                         | ` |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | V |
|               |   |   |                 |                         | M |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ( |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | ) |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | - |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | q |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.   | v | v | -               | `                       |   |
| volume.Info`` | m | o |                 | `<property>=<value>\n`` |   |
|               |   | l |                 |                         |   |
|               |   | u |                 |                         |   |
|               |   | m |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``            | v | v | value           | -                       |   |
| admin.vm.volu | m | o |                 |                         |   |
| me.Set.revisi |   | l |                 |                         |   |
| ons_to_keep`` |   | u |                 |                         |   |
|               |   | m |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin       | v | v | -               | snapshot                | d |
| .vm.volume.Li | m | o |                 |                         | u |
| stSnapshots`` |   | l |                 |                         | p |
|               |   | u |                 |                         | l |
|               |   | m |                 |                         | i |
|               |   | e |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | s |
+---------------+---+---+-----------------+-------------------------+---+
| ``            | v | v | -               | snapshot                | i |
| admin.vm.volu | m | o |                 |                         | d |
| me.Snapshot`` |   | l |                 |                         | . |
|               |   | u |                 |                         |   |
|               |   | m |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.vo | v | v | snapshot        | -                       | i |
| lume.Revert`` | m | o |                 |                         | d |
|               |   | l |                 |                         | . |
|               |   | u |                 |                         |   |
|               |   | m |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.vo | v | v | size_in_bytes   | -                       | i |
| lume.Resize`` | m | o |                 |                         | d |
|               |   | l |                 |                         | . |
|               |   | u |                 |                         |   |
|               |   | m |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.vo | v | v | raw volume data | -                       | i |
| lume.Import`` | m | o |                 |                         | d |
|               |   | l |                 |                         | . |
|               |   | u |                 |                         |   |
|               |   | m |                 |                         |   |
|               |   | e |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.      | v | v | ``<size_        | -                       | n |
| vm.volume.Imp | m | o | in_bytes>\n<raw |                         | e |
| ortWithSize`` |   | l |  volume data>`` |                         | w |
|               |   | u |                 |                         | v |
|               |   | m |                 |                         | e |
|               |   | e |                 |                         | r |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | I |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | z |
|               |   |   |                 |                         | e |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.vm.v  | v | v | -               | -                       | c |
| olume.Clear`` | m | o |                 |                         | l |
|               |   | l |                 |                         | e |
|               |   | u |                 |                         | a |
|               |   | m |                 |                         | r |
|               |   | e |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
+---------------+---+---+-----------------+-------------------------+---+
| ``a           | v | v | -               | token, to be used in    | o |
| dmin.vm.volum | m | o |                 | ``ad                    | b |
| e.CloneFrom`` |   | l |                 | min.vm.volume.CloneTo`` | t |
|               |   | u |                 |                         | a |
|               |   | m |                 |                         | i |
|               |   | e |                 |                         | n |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ; |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | ’ |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | C |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | T |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | s |
+---------------+---+---+-----------------+-------------------------+---+
| `             | v | v | token, obtained | -                       | c |
| `admin.vm.vol | m | o | with            |                         | o |
| ume.CloneTo`` |   | l | ``admin.vm.vol  |                         | p |
|               |   | u | ume.CloneFrom`` |                         | y |
|               |   | m |                 |                         | v |
|               |   | e |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
+---------------+---+---+-----------------+-------------------------+---+
| ``adm         | v | - | -               | -                       |   |
| in.vm.Start`` | m |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.      | v | - | -               | -                       |   |
| vm.Shutdown`` | m |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``adm         | v | - | -               | -                       |   |
| in.vm.Pause`` | m |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin       | v | - | -               | -                       |   |
| .vm.Unpause`` | m |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``ad          | v | - | -               | -                       |   |
| min.vm.Kill`` | m |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.bac   | ` | c | -               | -                       | c |
| kup.Execute`` | ` | o |                 |                         | o |
|               | d | n |                 |                         | n |
|               | o | f |                 |                         | f |
|               | m | i |                 |                         | i |
|               | 0 | g |                 |                         | g |
|               | ` | i |                 |                         | i |
|               | ` | d |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | / |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | / |
|               |   |   |                 |                         | q |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | / |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | / |
|               |   |   |                 |                         | < |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | > |
|               |   |   |                 |                         | . |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         |   |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | ` |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | e |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.      | ` | c | -               | backup info             | i |
| backup.Info`` | ` | o |                 |                         | n |
|               | d | n |                 |                         | f |
|               | o | f |                 |                         | o |
|               | m | i |                 |                         | w |
|               | 0 | g |                 |                         | h |
|               | ` | i |                 |                         | a |
|               | ` | d |                 |                         | t |
|               |   |   |                 |                         | w |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | l |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | d |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | h |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | p |
+---------------+---+---+-----------------+-------------------------+---+
| ``admin.ba    | ` | c | -               | -                       | c |
| ckup.Cancel`` | ` | o |                 |                         | a |
|               | d | n |                 |                         | n |
|               | o | f |                 |                         | c |
|               | m | i |                 |                         | e |
|               | 0 | g |                 |                         | l |
|               | ` | i |                 |                         | r |
|               | ` | d |                 |                         | u |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | b |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | k |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | p |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | n |
+---------------+---+---+-----------------+-------------------------+---+
| ``a           | ` | - | -               | events                  |   |
| dmin.Events`` | ` |   |                 |                         |   |
|               | d |   |                 |                         |   |
|               | o |   |                 |                         |   |
|               | m |   |                 |                         |   |
|               | 0 |   |                 |                         |   |
|               | | |   |                 |                         |   |
|               | v |   |                 |                         |   |
|               | m |   |                 |                         |   |
|               | ` |   |                 |                         |   |
|               | ` |   |                 |                         |   |
+---------------+---+---+-----------------+-------------------------+---+
| ``adm         | ` | - | -               | ``vm-stats`` events,    | e |
| in.vm.Stats`` | ` |   |                 | see below               | m |
|               | d |   |                 |                         | i |
|               | o |   |                 |                         | t |
|               | m |   |                 |                         | V |
|               | 0 |   |                 |                         | M |
|               | | |   |                 |                         | s |
|               | v |   |                 |                         | t |
|               | m |   |                 |                         | a |
|               | ` |   |                 |                         | t |
|               | ` |   |                 |                         | i |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | c |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | ( |
|               |   |   |                 |                         | C |
|               |   |   |                 |                         | P |
|               |   |   |                 |                         | U |
|               |   |   |                 |                         | , |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | y |
|               |   |   |                 |                         | u |
|               |   |   |                 |                         | s |
|               |   |   |                 |                         | a |
|               |   |   |                 |                         | g |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | ) |
|               |   |   |                 |                         | i |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | r |
|               |   |   |                 |                         | m |
|               |   |   |                 |                         | o |
|               |   |   |                 |                         | f |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | v |
|               |   |   |                 |                         | e |
|               |   |   |                 |                         | n |
|               |   |   |                 |                         | t |
|               |   |   |                 |                         | s |
+---------------+---+---+-----------------+-------------------------+---+

:doc:`View this table on a fullscreen page. </developer/services/admin-api-table>`

Volume properties:

-  ``pool``
-  ``vid``
-  ``size``
-  ``usage``
-  ``rw``
-  ``source``
-  ``save_on_stop``
-  ``snap_on_start``
-  ``revisions_to_keep``
-  ``is_outdated``

Method ``admin.vm.Stats`` returns ``vm-stats`` events every
``stats_interval`` seconds, for every running VM. Parameters of
``vm-stats`` events:

-  ``memory_kb`` - memory usage in kB
-  ``cpu_time`` - absolute CPU time (in milliseconds) spent by the VM
   since its startup, normalized for one CPU
-  ``cpu_usage`` - CPU usage in percents

Returned messages
-----------------

First byte of a message is a message type. This is 8 bit non-zero
integer. Values start at 0x30 (48, ``'0'``, zero digit in ASCII) for
readability in hexdump. Next byte must be 0x00 (a separator).

This alternatively can be thought of as zero-terminated string
containing single ASCII digit.

OK (0)
~~~~~~

::

   30 00 <content>

Server will close the connection after delivering single message.

EVENT (1)
~~~~~~~~~

::

   31 00 <subject> 00 <event> 00 ( <key> 00 <value> 00 )* 00

Events are returned as stream of messages in selected API calls.
Normally server will not close the connection.

A method yielding events will not ever return a ``OK`` or ``EXCEPTION``
message.

When calling such method, it will produce an artificial event
``connection-established`` just after connection, to help avoiding race
conditions during event handler registration.

EXCEPTION (2)
~~~~~~~~~~~~~

::

   32 00 <type> 00 ( <traceback> )? 00 <format string> 00 ( <field> 00 )*

Server will close the connection.

Traceback may be empty, can be enabled server-side as part of debug
mode. Delimiting zero-byte is always present.

Fields are should substituted into ``%``-style format string, possibly
after client-side translation, to form final message to be displayed
unto user. Server does not by itself support translation.

Tags
----

The tags provided can be used to write custom policies. They are not
used in a default Qubes OS installation. However, they are created
anyway.

-  ``created-by-<vm>`` — Created in an extension to qubesd at the moment
   of creation of the VM. Cannot be changed via API, which is also
   enforced by this extension.
-  ``managed-by-<vm>`` — Can be used for the same purpose, but it is not
   created automatically, nor is it forbidden to set or reset this tag.

Backup profile
--------------

Backup-related calls do not allow (yet) to specify what should be
included in the backup. This needs to be configured separately in dom0,
with a backup profile, stored in ``/etc/qubes/backup/<profile>.conf``.
The file use yaml syntax and have following settings:

-  ``include`` - list of VMs to include, can also contains tags using
   ``$tag:some-tag`` syntax or all VMs of given type using
   ``$type:AppVM``, known from qrexec policy
-  ``exclude`` - list of VMs to exclude, after evaluating ``include``
   setting
-  ``destination_vm`` - VM to which the backup should be send
-  ``destination_path`` - path to which backup should be written in
   ``destination_vm``. This setting is given to ``qubes.Backup`` service
   and technically it’s up to it how to interpret it. In current
   implementation it is interpreted as a directory where a new file
   should be written (with a name based on the current timestamp), or a
   command where the backup should be piped to
-  ``compression`` - should the backup be compressed (default: True)?
   The value can be either ``False`` or ``True`` for default
   compression, or a compression command (needs to accept ``-d``
   argument for decompression)
-  ``passphrase_text`` - passphrase used to encrypt and integrity
   protect the backup
-  ``passphrase_vm`` - VM which should be asked what backup passphrase
   should be used. The asking is performed using
   ``qubes.BackupPassphrase+profile_name`` service, which is expected to
   output chosen passphrase to its stdout. Empty output cancel the
   backup operation. This service can be used either to ask the user
   interactively, or to have some automated passphrase handling (for
   example: generate randomly, then encrypt with a public key and send
   somewhere)

Not all settings needs to be set.

Example backup profile:

.. code:: yaml

   # Backup only selected VMs
   include:
     - work
     - personal
     - vault
     - banking

   # Store the backup on external disk
   destination_vm: sys-usb
   destination_path: /media/my-backup-disk

   # Use static passphrase
   passphrase_text: "My$Very!@Strong23Passphrase"

And slightly more advanced one:

.. code:: yaml

   # Include all VMs with a few exceptions
   include:
     - $type:AppVM
     - $type:TemplateVM
     - $type:StandaloneVM
   exclude:
     - untrusted
     - $tag:do-not-backup

   # parallel gzip for faster backup
   compression: pigz

   # ask 'vault' VM for the backup passphrase
   passphrase_vm: vault

   # send the (encrypted) backup directly to remote server
   destination_vm: sys-net
   destination_path: ncftpput -u my-ftp-username -p my-ftp-pass -c my-ftp-server /directory/for/backups

General notes
-------------

-  there is no provision for ``qvm-run``, but there already exists
   ``qubes.VMShell`` call
-  generally actions ``*.List`` return a list of objects and have
   “object identifier” as first word in a row. Such action can be also
   called with “object identifier” in argument to get only a single
   entry (in the same format).
-  closing qrexec connection normally does *not* interrupt running
   operation; this is important to avoid leaving the system in
   inconsistent state
-  actual operation starts only after caller send all the parameters
   (including a payload), signaled by sending EOF mark; there is no
   support for interactive protocols, to keep the protocol reasonable
   simple

Policy admin API
----------------

There is also an API to view and update :doc:`Qubes RPC policy
files </developer/services/qrexec>` in dom0. All of the following calls have dom0 as
destination:

+------------------+----------+------------------+------------------+
| call             | argument | inside           | return           |
+==================+==========+==================+==================+
| ``policy.List``  | -        | -                | ``<name1>        |
| ``polic          |          |                  | \n<name2>\n...`` |
| y.include.List`` |          |                  |                  |
+------------------+----------+------------------+------------------+
| ``policy.Get``   | name     | -                | ``<tok           |
| ``poli           |          |                  | en>\n<content>`` |
| cy.include.Get`` |          |                  |                  |
+------------------+----------+------------------+------------------+
| ``               | name     | ``<tok           | -                |
| policy.Replace`` |          | en>\n<content>`` |                  |
| ``policy.i       |          |                  |                  |
| nclude.Replace`` |          |                  |                  |
+------------------+----------+------------------+------------------+
| `                | name     | ``<token>``      | -                |
| `policy.Remove`` |          |                  |                  |
| ``policy.        |          |                  |                  |
| include.Remove`` |          |                  |                  |
+------------------+----------+------------------+------------------+

The ``policy.*`` calls refer to main policy files
(``/etc/qubes/policy.d/``), and the ``policy.include.*`` calls refer to
the include directory (``/etc/qubes/policy.d/include/``). The
``.policy`` extension for files in the main directory is always omitted.

The responses do not follow admin API protocol, but signal error using
an exit code and a message on stdout.

The changes are validated before saving, so that the policy cannot end
up in an invalid state (e.g. syntax error, missing include file).

In addition, there is a mechanism to prevent concurrent modifications of
the policy files:

-  A ``*.Get`` call returns a file along with a *token* (currently
   implemented as a hash of the file).
-  When calling ``Replace`` or ``Remove``, you need to include the
   current token as first line. If the token does not match, the
   modification will fail.
-  When adding a new file using ``Replace``, pass ``new`` as token. This
   will ensure that the file does not exist before adding.
-  To skip the check, pass ``any`` as token.

TODO
----

-  notifications

   -  how to constrain the events?
   -  how to pass the parameters? maybe XML, since this is trusted
      anyway and parser may be complicated

-  how to constrain the possible values for ``admin.vm.property.Set``
   etc, like “you can change ``netvm``, but you have to pick from this
   set”; this currently can be done by writing an extension
-  a call for executing ``*.desktop`` file from
   ``/usr/share/applications``, for use with appmenus without giving
   access to ``qubes.VMShell``; currently this can be done by writing
   custom qrexec calls
-  maybe some generator for ``.desktop`` for appmenus, which would wrap
   calls in ``qrexec-client-vm``

.. raw:: html

   <!-- vim: set ts=4 sts=4 sw=4 et : -->
