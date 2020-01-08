# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-BroadTech IT Solutions (<http://www.broadtech-innovations.com/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
##############################################################################


{
    'name' : 'Account Balance in Secondary Currency',
    'version' : '0.1',
    'summary': 'Account Balance in Secondary Currency',
    'sequence': 30,
    'license':'LGPL-3',
    'description': """
In the Odoo multi currency enviornment, account balance in secondary currency is not available by default. 
This module modifies General Ledger and Partner Ledger reports and shows account balance in secondary currency.
====================
""",
    'category': 'Accounting',
    'author': 'BroadTech IT Solutions Pvt Ltd',
    'website': 'http://www.broadtech-innovations.com/',
    'depends' : ['account'],
    'data': [
        'views/report_generalledger.xml',
        'views/report_partnerledger.xml',
        ],
        
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

