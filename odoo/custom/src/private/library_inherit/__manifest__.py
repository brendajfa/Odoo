# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Library Herencia",
    "summary": "Library base",
    "version": "16.0.1.0.0",
    "category": "Sistema DOQ",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ['sale', 'library_base'],
    "data": [
        'views/library_book.xml'
        # ,'security/ir.model.access.csv'
    ],
}
