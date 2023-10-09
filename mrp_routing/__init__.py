# Copyright 2021 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from . import models

from openupgradelib.openupgrade import rename_xmlids


def pre_init_hook(cr):
    rename_xmlids(
        cr,
        [
            ("mrp.sequence_mrp_route", "mrp_routing.sequence_mrp_route"),
        ],
    )
