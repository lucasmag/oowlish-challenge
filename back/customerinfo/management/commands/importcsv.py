import csv
from django.core.management import BaseCommand, CommandError
from customerinfo.models import Customer
import os

from customerinfo.utils import get_coordinates_from_address, Coordinates


def validade_path_to_csv(csv_path: str) -> None:
    if not csv_path:
        raise CommandError(
            "Invalid Invocation. You must pass the path to .csv customers file."
        )

    if not os.path.exists(csv_path):
        raise CommandError(f"{csv_path} doesn't exist.")


def import_csv_to_database(csv_path: str) -> None:
    validade_path_to_csv(csv_path)

    with open(csv_path) as csv_file:
        csv_rows = csv.DictReader(csv_file)

        for row in csv_rows:
            coordinates: Coordinates = get_coordinates_from_address(row["city"])

            customer = Customer(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row.get("last_name", ""),
                email=row["email"],
                gender=row["gender"],
                company=row["company"],
                city=row["city"],
                title=row.get("title", ""),
                latitude=coordinates.latitude,
                longitude=coordinates.longitude,
            )
            customer.save()


class Command(BaseCommand):
    help = "Import a .csv file into `Customers` database."

    def add_arguments(self, parser):
        parser.add_argument(
            "customers_path", type=str, help="Path to .csv customers file"
        )

    def handle(self, *args, **options):
        csv_path = options["customers_path"]

        self.stdout.write("Importing customers...")
        import_csv_to_database(csv_path)
        self.stdout.write(self.style.SUCCESS("Import completed"))
