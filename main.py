from process_csvs import pickup_csv, pickup_csv_prev

# , invoice_csv, sales_order_csv
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from datetime import datetime


# def listener(event):
#     if not event.exception:
#         job = scheduler.get_job(event.job_id)
#         if job.name == "pickupCSV":
#             now = datetime.now()
#             print(now)
#     if event.exception:
#         print("woops something broke")
#         scheduler.shutdown()


# scheduler = BlockingScheduler()
# scheduler.add_listener(listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# scheduler.add_job(pickupCSV, "interval", hours=24, start_date="2021-04-02 17:50:00")
# scheduler.add_job(invoiceCSV, "interval", hours=24, start_date="2021-04-02 17:50:20")
# scheduler.add_job(salesOrderCSV, "interval", hours=24, start_date="2021-04-02 17:50:40")
# scheduler.start()

pickup_csv()
pickup_csv_prev()
# invoice_csv()
# sales_order_csv()
