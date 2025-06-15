from llama_cloud_services import LlamaParse
import json

from sqlalchemy import values

parser = LlamaParse(
    api_key="llx-gOez8nY6tPiauNFiQOwA9cLm1yjGIaIUw4EWzty3dLmkpz5q",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    num_workers=4,       # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    language="en",
)

result = parser.parse("C:\\Personal\\Girish\study\\aws-chatbot-poc\\testfiles\\cosentyx.pdf")
records = []
# this does not work when there are multiple heading lines one after another
for page in result.pages :
    count = len(page.items)
    for i in range(len(page.items)):
        item = page.items[i]
        if i+1<len(page.items):
            if item.type == "heading"  and page.items[i + 1].type == "text":
                 records.append({"heading": item.value, "text": page.items[i+1].value, "page": page.page})


print(json.dumps(records,  indent=4))

