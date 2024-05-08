from langchain_openai import OpenAI
from dotenv import load_dotenv
import json
import api

load_dotenv()

def read_report():
    api.export_report()
    with open('report.json','r') as handle:
        report = json.load(handle)
        try:
            print("delete unnessacesery elements")
            del report["objects"][2]["external_references"]
            del report["objects"][2]["object_refs"]
        except:
            print("clean report")

    report = json.dumps(report,indent=4)
    # Write the bundle
    f = open("report.json", "w")
    f.write(report)
    f.close()
    return report 

def generate_suricata_rule(report):
   
    llm = OpenAI(temperature=0.7)

    rule = llm(report + "\n use the above report to generate the Suricata rules. Just print out the rule.")
    return rule

# if __name__ == '__main__':
#     print(generate_suricata_rule)
