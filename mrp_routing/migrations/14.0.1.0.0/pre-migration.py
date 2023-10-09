from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_xmlids(
        env.cr,
        [
            ("mrp.sequence_mrp_route", "mrp_routing.sequence_mrp_route"),
        ],
    )
