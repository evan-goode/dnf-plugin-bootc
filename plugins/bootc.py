# bootc.py, implements the 'bootc' command
#
# Copyright David Cantrell <dcantrell@redhat.com>
# SPDX-License-Identifier: GPL-2.0-or-later

from __future__ import absolute_import
from __future__ import unicode_literals

import dnf
import logging

_, P_ = dnf.i18n.translation('dnf-plugin-bootc')
logger = logging.getLogger('dnf.plugin')
rpm_logger = logging.getLogger('dnf.rpm')


@dnf.plugin.register_command
class BootcCommand(dnf.cli.Command):
    aliases = ['bootc']
    summary = _('Modify software on a bootc-based system')

    def __init__(self, cli):
        super(BootcCommand, self).__init__(cli)
        self.opts = None
        self.parser = None

    @staticmethod
    def set_argparser(parser):
        parser.add_argument('subcommand', nargs=1,
                            choices=['help', 'install'])

        install_option = parser.add_mutually_exclusive_group()
        install_option.add_argument('-A', '--apply-live', action='store_true',
                                    help=_('Apply changes to both pending deployment and running filesystem tree'))
        install_option.add_argument('--force-replacefiles', action='store_true',
                                    help=_('Allow package to replace files from other packages'))
        install_option.add_argument('-r', '--reboot', action='store_true',
                                    help=_('Initiate a reboot after operation is complete'))

#        parser.add_argument('-q', '--quiet', action='store_true',
#                            help=_('In combination with a non-interactive command, shows just the relevant content. Suppresses messages notifying about the current state or actions of dnf.'))
#        parser.add_argument('-C', '--cacheonly', action='store_true',
#                            help=_('Run entirely from system cache, don\'t update the cache and use it even in case it is expired.'))
#        parser.add_argument('-y', '--assumeyes', action='store_true',
#                            help=_('automatically answer yes for all questions'))
#        parser.add_argument('--assumeno', action='store_true',
#                            help=_('automatically answer no for all questions'))
#        parser.add_argument('--releasever==RELEASEVER', action='append',
#                            help=_('override the value of $releasever in config and repo files'))
#        parser.add_argument('--enablerepo=REPO_ID,...', action='append',
#                            help=_('Enable additional repositories. List option. Supports globs, can be specified multiple times.')
#        parser.add_argument('--disablerepo=REPO_ID,...', action='append',
#                            help=_('Disable plugins by name. List option. Supports globs, can be specified multiple times.'))
#        parser.add_argument('--installroot=ABSOLUTE_PATH', action='append',
#                            help=_('set install root'))

    def configure(self):
        if self.cli.command.opts.command != 'bootc':
            return

    def run(self):
        subcommand = self.opts.subcommand[0]

        if subcommand == "install":
            return
