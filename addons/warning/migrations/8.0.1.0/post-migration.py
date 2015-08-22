# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, an open source suite of business apps
# This module copyright (C) 2015 bloopark systems (<http://bloopark.de>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.openupgrade import openupgrade
from openerp.modules.registry import RegistryManager


def update_product_warn_fields(cr, pool):
    for warn_field in ('purchase_line_warn', 'sale_line_warn'):
        openupgrade.logged_query(cr, """
            UPDATE product_product
            SET %(field)s='no-message'
            WHERE %(field)s is null
        """ % {'field': warn_field})


@openupgrade.migrate()
def migrate(cr, version):
    pool = RegistryManager.get(cr.dbname)
    update_product_warn_fields(cr, pool)
    openupgrade.move_field_m2o(
        cr, pool,
        'product.product', 'purchase_line_warn', 'product_tmpl_id',
        'product.template', 'purchase_line_warn')
    openupgrade.move_field_m2o(
        cr, pool,
        'product.product', 'purchase_line_warn_msg', 'product_tmpl_id',
        'product.template', 'purchase_line_warn_msg')
    openupgrade.move_field_m2o(
        cr, pool,
        'product.product', 'sale_line_warn', 'product_tmpl_id',
        'product.template', 'sale_line_warn')
    openupgrade.move_field_m2o(
        cr, pool,
        'product.product', 'sale_line_warn_msg', 'product_tmpl_id',
        'product.template', 'sale_line_warn_msg')
