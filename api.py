from dateutil.parser import parse
from pycti import OpenCTIApiClient
from stix2 import TLP_GREEN
import json
"""
OPENCTI_ADMIN_EMAIL=admin@opencti.io
OPENCTI_ADMIN_PASSWORD=ChangeMePlease
OPENCTI_ADMIN_TOKEN=9c265786-44b9-4437-8084-4fa02c041872
MINIO_ROOT_USER=6ecd4550-a175-47fa-b030-94bd9a616134
MINIO_ROOT_PASSWORD=d3f6eb00-b4dc-4ec1-b6c6-950f2a9559c1
RABBITMQ_DEFAULT_USER=guest
RABBITMQ_DEFAULT_PASS=guest
ELASTIC_MEMORY_SIZE=4G
CONNECTOR_HISTORY_ID=9eedead5-7c36-475b-97f3-9b6682a22b59
CONNECTOR_EXPORT_FILE_STIX_ID=f19433e5-1242-43c8-95f4-a268daf94945
CONNECTOR_EXPORT_FILE_CSV_ID=643759d0-1592-4a5d-a447-db96ae6b5d8f
CONNECTOR_IMPORT_FILE_STIX_ID=e11d6c8c-eb2c-4fc7-8de1-a13f6159f658
CONNECTOR_IMPORT_REPORT_ID=536605bd-d202-4544-9b49-ef75593d2e88
"""
# OpenCTI API client initialization
opencti_api_client = OpenCTIApiClient("http://127.0.01:8080", "9c265786-44b9-4437-8084-4fa02c041872")

def get_all_report():
    # Get all reports using the pagination
    custom_attributes = """
        id
        name
        published
        description
    """

    final_reports = []
    data = {"pagination": {"hasNextPage": True, "endCursor": None}}
    while data["pagination"]["hasNextPage"]:
        after = data["pagination"]["endCursor"]
        if after:
            print("Listing reports after " + after)
        data = opencti_api_client.report.list(
            first=50,
            after=after,
            customAttributes=custom_attributes,
            withPagination=True,
            orderBy="created_at",
            orderMode="asc",
        )
        final_reports = final_reports + data["entities"]

    # Print
    for report in final_reports:
        # print("[" + report["id"] +"] "+" ["+ report["published"] + "] " + report["name"])
        pass
    return report["id"]

def export_report():
    report_id = get_all_report()
    # 匯出報告
    # Create the bundle
    bundle = opencti_api_client.stix2.export_entity("Report", report_id, "simple")
    json_bundle = json.dumps(bundle, indent=4)

    # Write the bundle
    f = open("report.json", "w")
    f.write(json_bundle)
    f.close()

