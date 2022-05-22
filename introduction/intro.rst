.. raw:: html

   <h2>

What is Qubes OS?

.. raw:: html

   </h2>

.. container:: row

   .. container:: col-lg-12 col-md-12

      ::

         <p>
           Qubes OS is a free and open-source, security-oriented operating system for
           single-user desktop computing. Qubes OS leverages
           <a href="https://wiki.xen.org/wiki/Xen_Project_Software_Overview">
           Xen-based virtualization</a> to allow for the creation and management of
           isolated compartments called <a href="/doc/glossary#qube">qubes</a>.
         </p>

.. container:: row

   .. container:: col-lg-3 col-md-3 text-left

      ::

         <p>
           These qubes, which are implemented as <a href="/doc/glossary#vm">virtual
           machines (VMs)</a>, have specific:
           <ul>
             <li class="more-bottom">
               <b>Purposes:</b> with a predefined set of one or many isolated
               applications, for personal or professional projects, to manage the
               <a href="/doc/networking/">network stack</a>,
               <a href="/doc/firewall/">the firewall</a>, or to fulfill other
               user-defined purposes.
             </li>
             <li class="more-bottom">
               <b>Natures:</b> <a href="/doc/standalone-and-hvm/">full-fledged</a> or
               <a href="/doc/getting-started/">
               stripped-down</a> virtual machines based on popular operating systems,
               such as <a href="/doc/templates/fedora/">Fedora</a>,
               <a href="/doc/templates/debian/">Debian</a>, and
               <a href="/doc/windows/">Windows</a>.
             </li>
             <li class="more-bottom">
               <b>Levels of trust:</b> from complete to non-existent. All windows are
               displayed in a unified desktop environment with
               <a href="/doc/getting-started/">unforgeable colored window borders</a> so
               that different security levels are easily identifiable.
             </li>
           </ul>
         </p>

   .. container:: col-lg-9 col-md-9

      ::

         <a href="/attachment/site/qubes-trust-level-architecture.png">
           <img src="/attachment/site/qubes-trust-level-architecture.png"
                class="center-block more-bottom" alt="Qubes system diagram">
         </a>

.. container:: alert alert-info more-bottom

   Note: See our glossary and FAQ for more information.

.. raw:: html

   <h2 class="more-bottom">

Features

.. raw:: html

   </h2>

.. container:: row

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Strong isolation</h3>
         <p>
           Isolate different pieces of software as if they were installed on separate
           physical machines using advanced virtualization techniques.
         </p>

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Template system</h3>
         <p>
           Use <a href="/doc/glossary/#app-qube">app qubes</a> to
           share a root file system without sacrificing security using the innovative
           <a href="/doc/templates/">Template system</a>.
         </p>

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Multiple operating systems</h3>
         <p>
           Use multiple operating systems at the same time, including
           <a href="/doc/templates/fedora/">Fedora</a>,
           <a href="/doc/templates/debian/">Debian</a>, and
           <a href="/doc/windows/">Windows.</a>
         </p>

.. raw:: html

   <hr>

.. container:: row

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Disposables</h3>
         <p>
           Create <a href="/doc/how-to-use-disposables/">disposables</a> on the fly that
           self-destruct when shut down.
         </p>

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Whonix integration</h3>
         <p>
           Run <a href="https://www.torproject.org/">Tor</a> securely system-wide
           using <a href="https://www.whonix.org/wiki/Qubes">Whonix with Qubes</a>.
         </p>

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Device isolation</h3>
         <p>
           Secure <a href="/doc/device-handling/">device handling</a> through
           isolation of network cards and USB controllers.
         </p>

.. raw:: html

   <hr>

.. container:: row

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Split GPG</h3>
         <p>
           Utilize <a href="/doc/split-gpg/">Split GPG</a> to keep your private keys
           safe.
         </p>

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>U2F proxy</h3>
         <p>
           Operate <a href="/doc/u2f-proxy/">Qubes U2F proxy</a> to use your
           two-factor authentication devices without exposing your web browser to the
           full USB stack.
         </p>

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Open-source</h3>
         <p>
           Users are free to use, copy, and modify Qubes OS and
           <a href="/doc/contributing/">are encouraged to do so!</a>
         </p>

.. container:: alert alert-info more-bottom

   Note: Given the technical nature of Qubes OS, prior experience with
   Linux can be helpful.

.. raw:: html

   <h2 class="more-bottom">

Why Qubes OS?

.. raw:: html

   </h2>

.. raw:: html

   <h3>

Physical isolation is a given safeguard that the digital world lacks

.. raw:: html

   </h3>

.. container:: row

   .. container:: col-lg-6 col-md-6 text-left

      ::

         <p>
           Throughout our lives, we engage in various activities, such as going to
           school, working, voting, taking care of our families, and visiting with
           friends. These activities are spatially and temporally bound: They happen
           in isolation from one another, in their own compartments, which often
           represent an essential safeguard, as in the case of voting.
         </p>
         <p>
           In our digital lives, the situation is quite different: All of our
           activities typically happen on a single device. This causes us to worry
           about whether it's safe to click on a link or install an app, since being
           hacked imperils our entire digital existence.
         </p>
         <p>
           Qubes eliminates this concern by allowing us to divide a device into many
           compartments, much as we divide a physical building into many rooms.
           Better yet, it allows us to create new compartments whenever we need them,
           and it gives us sophisticated tools for securely managing our activities
           and data across these compartments.
         </p>

   .. container:: col-lg-6 col-md-6

      ::

         <a href="/attachment/doc/r4.0-qubes-manager.png">
           <img src="/attachment/doc/r4.0-qubes-manager.png"
                class="center-block more-bottom" alt="Qube Manager">
         </a>

.. raw:: html

   <h3>

Qubes allows you to compartmentalize your digital life

.. raw:: html

   </h3>

.. container:: row

   .. container:: col-lg-6 col-md-6

      ::

         <a href="/attachment/site/qubes-partition-data-flows.jpg">
           <img src="/attachment/site/qubes-partition-data-flows.jpg"
                class="center-block more-bottom" alt="Compartmentalization example">
         </a>

   .. container:: col-lg-6 col-md-6 text-left center-block

      ::

         <p>
           Many of us are initially surprised to learn that our devices do not
           support the kind of secure compartmentalization that our lives demand, and
           we're disappointed that software vendors rely on generic defenses that
           repeatedly succumb to new attacks.
         </p>
         <p>
           In building Qubes, our working assumption is that all software contains
           bugs. Not only that, but in their stampeding rush to meet deadlines, the
           world's stressed-out software developers are pumping out new code at a
           staggering rate &mdash; far faster than the comparatively smaller
           population of security experts could ever hope to analyze it for
           vulnerabilities, much less fix everything. Rather than pretend that we can
           prevent these inevitable vulnerabilities from being exploited, we've
           designed Qubes under the assumption that they <em>will</em> be exploited.
           It's only a matter of time until the next zero-day attack.
         </p>
         <p>
           In light of this sobering reality, Qubes takes an eminently practical
           approach: confine, control, and contain the damage. It allows you to keep
           valuable data separate from risky activities, preventing
           cross-contamination. This means you can do everything on the same
           physical computer without having to worry about a single successful
           cyberattack taking down your entire digital life in one fell swoop. In
           fact, Qubes has
           <a href="https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf">
           distinct advantages over physical air gaps</a>.
         </p>

.. raw:: html

   <h3>

Made to support vulnerable users and power users alike

.. raw:: html

   </h3>

.. container:: row

   .. container:: col-lg-6 col-md-6 text-left

      ::

         <p>
           Qubes provides practical, usable security to vulnerable and
           actively-targeted individuals, such as journalists, activists,
           whistleblowers, and researchers. Qubes is designed with the understanding
           that people make mistakes, and it allows you to protect yourself from your
           own mistakes. It's a place where you can click on links, open attachments,
           plug in devices, and install software free from worry. It's a place where
           <em>you</em> have control over your software, not the other way around.
         </p>
         <p>
           Qubes is also powerful. Organizations like the <a
           href="https://securedrop.org/news/piloting-securedrop-workstation-qubes-os/">Freedom
           of the Press Foundation</a>, <a
           href="https://twitter.com/mullvadnet/status/631010362083643392">Mullvad</a>,
           and <a
           href="https://twitter.com/letsencrypt/status/1239934557710737410">Let's
           Encrypt</a> rely on Qubes as they build and maintain critical privacy and
           security internet technologies that are in turn relied upon by countless
           users around the world every day. Renowned security <a
           href="/endorsements/">experts</a> like Edward Snowden, Daniel J. Bernstein,
           Micah Lee, Christopher Soghoian, Isis Agora Lovecruft, Peter Todd, Bill
           Budington, and Kenn White use and recommend Qubes.
         </p>
         <p>
           Qubes is one of the few operating systems that places the security of
           its users above all else. It is, and always will be, free and open-source
           software, because the fundamental operating system that constitutes the
           core infrastructure of our digital lives <em>must</em> be free and
           open-source in order to be trustworthy.
         </p>

   .. container:: col-lg-6 col-md-6

      ::

         <a href="/attachment/doc/r4.0-snapshot12.png">
           <img src="/attachment/doc/r4.0-snapshot12.png"
                class="center-block more-bottom" alt="Qubes desktop screenshot">
         </a>

.. raw:: html

   <hr class="add-top more-bottom">

.. container:: row more-bottom

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Video Tours</h3>
         <p>
           Want to see Qubes OS in action? Sit back and watch a guided tour!
         </p>
         <a href="/video-tours/" class="btn btn-primary more-bottom">
           <i class="fa fa-play-circle"></i> Video Tours
         </a>

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Screenshots</h3>
         <p>
           See what using Qubes actually looks like with these screenshots of various
           applications running in Qubes.
         </p>
         <a href="/screenshots/" class="btn btn-primary more-bottom">
           <i class="fa fa-picture-o"></i> Screenshots
         </a>

   .. container:: col-lg-4 col-md-4 col-xs-12

      ::

         <h3>Getting Started</h3>
         <p>
           Ready to get started with Qubes? Here's what you need to know after
           installing.
         </p>
         <a href="/doc/getting-started/" class="btn btn-primary more-bottom">
           <i class="fa fa-cubes"></i> Getting Started
         </a>

.. raw:: html

   <h2>

More information

.. raw:: html

   </h2>

.. raw:: html

   <p>

This page is just a brief introduction to what Qubes is all about, and
many technical details have been omitted here for the sake of
presentation.

.. raw:: html

   <ul>

.. raw:: html

   <li>

If you’re a current or potential Qubes user, you may want to check out
the documentation and the user FAQ.

.. raw:: html

   </li>

.. raw:: html

   <li>

If you’re a developer, there’s dedicated developer documentation and a
developer FAQ just for you.

.. raw:: html

   </li>

.. raw:: html

   <li>

Ready to give Qubes a try? Head on over to the downloads page, and read
the installation guide.

.. raw:: html

   </li>

.. raw:: html

   <li>

Need help, or just want to join the conversation? Learn more about help,
support, the mailing lists, and the forum.

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. raw:: html

   </p>
