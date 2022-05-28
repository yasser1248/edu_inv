import frappe
# from erpnext.controllers.accounts_controller import AccountsController

# class override_fees (AccountsController):
#     def make_gl_entries(): 
#         print("nothing")
        # return


def create_customer(doc, name):
    new_customer = frappe.get_doc({
        "doctype": "Customer",
        "customer_name":doc.title,
        "email_id": doc.student_email_id, })
    new_customer.insert()


def create_item(doc, name):
    new_item = frappe.get_doc({
        "doctype": "Item",
        "item_code": doc.category_name,
        "item_name": doc.category_name,
        "description": doc.description,
    })
    new_item.insert()


def make_sales_invoice(self, name):
    if not self.grand_total:
        return
    record = frappe.new_doc("Sales Invoice")
    record.update({
        "doctype": "Sales Invoice",
        "customer":self.student_name,
        "is_pos": 0,
        "is_return": 0,
        "posting_date": self.posting_date,
        "company": self.company,
        "update_stock": 0,

    })

    for x in self.components:
        record.append("items", {
            # "doctype":"Sales Invoice Item",
            "item_code": x.fees_category,
            # "item_name": 'item_name',
            "description": x.description,
            "qty": 1,
            # "stock_uom": 'stock_uom',
            "rate": x.amount,
            "amount": x.amount,
            "base_rate": x.amount,
            "base_amount": x.amount,
            # "income_account": 'income_account',
            # "cost_center": 1,
            # "warehouse": 'warehouse',
        })
    record.set_missing_values()
    record.flags.ignore_permissions = 1
    record.save()

