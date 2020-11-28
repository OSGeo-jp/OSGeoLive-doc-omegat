#!/usr/bin/python3
# coding=utf-8

# Referred mint-check-translations, but changed much
# https://github.com/linuxmint/mint-dev-tools/blob/master/usr/bin/mint-check-translations

import argparse
import polib
import os
from attrdict import AttrDict
from docutils.parsers.rst.states import Inliner, Struct
from docutils.utils import Reporter, new_document
from io import StringIO

PO_EXT = ".po"

# GOOD = 0
# RST_SCHAR_MISMATCH = 200


class Po:
    def __init__(self, inst, file, path):
        self.inst = inst
        self.file = file.replace(".po", "")
        self.current_index = 1


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Check translation files')
        parser.add_argument('directory', nargs='?', default=os.getcwd(), help="A directory to check (default is to check the current working directory)")
        self.args = parser.parse_args()
        self.type = PO_EXT
        self.load_files()

    def print_issue(self, po, msgid, msgstr, issue, current_index):
        # print("po: %s" % po)
        print("==========================")
        print("file: %s" % po.file)
        print("msgid: %s" % msgid)
        print("msgstr: %s" % msgstr)
        print("issue: %s" % issue)
        # print("current_index: %s" % current_index)

    def load_files(self):
        num_files = 0
        for root, subFolders, files in os.walk(self.args.directory, topdown=False):
            for file in files:
                if file.endswith(PO_EXT):
                    num_files += 1

        count_files = 0
        for root, subFolders, files in os.walk(self.args.directory, topdown=False):
            for file in files:
                if file.endswith(PO_EXT):
                    po_inst = polib.pofile(os.path.join(root, file))
                    po = Po(po_inst, file, os.path.join(root, file))
                else:
                    continue
                count_files += 1
                self.check_file(po)

    def check_file(self, po):
        for entry in po.inst:
            if entry.obsolete:
                continue  # skip obsolete translations (prefixed with #~ in po file)
            issue_found = False
            msgid = entry.msgid
            msgstr = entry.msgstr
            if ".rst" in str(entry):
                # restructuredtext
                # for special_char in ["``", "<", ">", "_", "-->", ":kbd:", ":guilabel:", "`"]:
                #     if msgstr != "" and msgid.count(special_char) != msgstr.count(special_char):
                #         issue_found = True
                #         res = "Mismatch in RST special chars"
                #         break
                # Sphinx build equivalent
                res = self.check_docutils_inliner(po, msgstr)
                if len(res) > 0:
                    issue_found = True

            if issue_found:
                self.print_issue(po, msgid, msgstr, res, po.current_index)
            po.current_index += 1

    def check_docutils_inliner(self, po, msgstr):
        inliner = Inliner()
        settings = AttrDict({'character_level_inline_markup': False, 'pep_references': None, 'rfc_references': None})
        inliner.init_customizations(settings)
        document = new_document(None)
        document.settings.syntax_highlight = 'long'
        stream = StringIO()
        reporter = Reporter(po.file, report_level=Reporter.WARNING_LEVEL,
                            halt_level=Reporter.SEVERE_LEVEL, stream=stream)
        memo = Struct(document=document, reporter=reporter, language=None, inliner=inliner)
        inliner.parse(msgstr, po.current_index, memo, None)
        return stream.getvalue()


if __name__ == "__main__":
    Main()
