import requests
from config import config


def get_pickup(sites):
    site = "site%5B%5D" if sites == 1 else "site%5B%5D=3&site%5B%5D=6"
    csv = requests.get(
        f"https://krameramerica.locateinv.com/report/114/run?{site}=4&removelineswithnovalues=AND&orderby=1&includedeletedsites=AND&formatassinglepage=1&daterange=Current+Month&daterange2=Current+Month&format=csv",
        auth=(config["key"]),
    ).content

    return csv


def get_pickup_prev(sites):
    site = "site%5B%5D" if sites == 1 else "site%5B%5D=3&site%5B%5D=6"
    csv = requests.get(
        f"https://krameramerica.locateinv.com/report/114/run?{site}=4&removelineswithnovalues=AND&orderby=1&includedeletedsites=AND&formatassinglepage=1&daterange=Previous+Month&daterange2=Previous+Month&format=csv",
        auth=(config["key"]),
    ).content

    return csv


# def get_invoice(yesterday, today):
#     csv = requests.get(
#         f"https://krameramerica.locateinv.com/report/211/run?orderby=appinvoice.number&datefilter=appinvoice.invoice_date&createddate=1&customer1=0&customerponumber=0&duedate=0&formatassinglepage=1&invoicecost=0&invoicedate=0&invoicediscount=0&invoicediscountname=0&invoicemargin=0&invoicememo=0&invoicemethod=0&invoicenumber=1&invoicepacknumber=0&invoiceprofit=0&invoicestatus=0&invoicetax=0&invoicetotal=0&invoicetype=0&linecost=0&linediscounts=0&lineexpecteddeliverydate=0&linefees=0&linemargin=0&linenumber=0&lineprofit=0&lineqty=0&linereturnreason=0&linescheduledfulfillmentdate=0&linesite=0&linetotalprice=0&linetype=0&lineunitprice=0&partname=0&partnumber=0&parttype=0&paymentterms=0&payments=0&salesperson=0&sentdate=0&sonumber=1&daterange={yesterday}&daterange2={today}&daterange2_range=&customer%5B%5D=16&customer%5B%5D=2&customer%5B%5D=7&customer%5B%5D=13&customer%5B%5D=21&customer%5B%5D=8&invoicestatus1%5B%5D=13&format=csv",
#         auth=(config["key"]),
#     ).content

#     return csv


# def get_sales_order(yesterday, today):
#     csv = requests.get(
#         f"https://krameramerica.locateinv.com/report/115/run?datefilter=appsalesorder.issue_date&orderby=appsalesorder.%60number%60&includearchivedparts=--&showchildlines=AND&aliaspartname=0&aliaspartnumber=1&allowsaturdaydelivery=0&buyercontact=0&createdat=0&createdby=0&customerdefaultemail=0&customerdefaultphone=0&formatassinglepage=1&fulfillmentplan=0&invoicegroupingmethod=0&lineitemcustomfields=0&lineitemcustomerpartnumber=0&lineitemdatescheduled=0&lineitemdiscounts=0&lineitemduedate=0&lineitemfees=0&lineitemlinetype=0&lineitemmemo=0&lineitemnumber=0&lineitempartdescription=0&lineitempartname=0&lineitempartnumber=1&lineitemqtyfulfilled=0&lineitemqtyordered=1&lineitemqtyremaining=0&lineitemstatus1=0&lineitemtotalprice=0&lineitemtrackingvalues=0&lineitemunitprice=1&lineitemuom=0&msrp=0&ordercustomfields=0&ordertype=0&passthroughshipping=0&payments=0&prepaymentamount=0&revision=0&site1=0&sobilltoaddress=0&socarriername=0&socarrierservicelevel=0&socustomername=1&socustomerponumber=0&sodatecompleted=1&sodiscounts=0&soexpecteddelivery=0&sofees=0&soissuedate=1&somemo=0&sonumber=1&sopaymentterms=0&sopriority=0&sosalesperson=0&soscheduledfulfillment=0&soshiptoaddress=0&soshippingterms=0&sostatus=1&sotax=1&sototalprice=0&sofobpoint=0&updatedat=0&lineitemparttype=0&daterange={yesterday}&daterange2={today}&daterange2_range=&customer%5B%5D=7&customer%5B%5D=8&customer%5B%5D=2&customer%5B%5D=16&customer%5B%5D=21&customer%5B%5D=13&salesorderstatus%5B%5D=14&format=csv",
#         auth=(config["key"]),
#     ).content

#     return csv
