from llama_cloud_services import LlamaParse
import json

from sqlalchemy import values

parser = LlamaParse(
    api_key="llx-********************",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    num_workers=4,       # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    language="en",
)

result = parser.parse("./files/cosentyx.pdf")
records = []
# this uses only the last heading line when multiple heading lines are present one after another
for page in result.pages :
    count = len(page.items)
    for i in range(len(page.items)):
        item = page.items[i]
        if i+1<len(page.items):
            if item.type == "heading"  and page.items[i + 1].type == "text":
                 records.append({"heading": item.value, "text": page.items[i+1].value, "page": page.page})


print(json.dumps(records,  indent=4))

