import datetime
import time

from schedule import repeat, every, run_pending
from mercado_bitcoin.ingestors import DataIngestor,AWSDaySummaryIngestor
from mercado_bitcoin.writers import DataWriter, S3Writter


if __name__ == "__main__":
    day_summary_ingestor = AWSDaySummaryIngestor(
        writer=S3Writter,
        coins=["BTC", "ETH", "LTC", "BCH"],
        default_start_date=datetime.date(2020, 1, 1)
    )


    @repeat(every(1).seconds)
    def job():
        day_summary_ingestor.ingest()


    while True:
        run_pending()
        time.sleep(0.5)
