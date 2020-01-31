import json

import numpy as np

data_file = 'data/scraper/data.json'
with open(data_file, 'r') as file:
    data_content = file.read()
    data = json.loads(data_content)
    post_count = []
    for item in data['data']:
        post_count.append(len(item.get("posts")))
    avg = sum(post_count) / len(post_count)
    percentile_75 = np.percentile(post_count, 75)
    max_threshold = avg + 1.5 * (percentile_75 - avg)
    count = 0
    for item in data['data']:
        if len(item.get("posts")) > max_threshold:
            print(data['data'][data['data'].index(item)].get("id") + " with " + str(
                len(item.get("posts"))) + " post number deleted!")
            del data['data'][data['data'].index(item)]
            count += 1
    print("Number of outliers: " + str(count))
    open(data_file, "w").write(
        json.dumps(data, sort_keys=True, indent=4)
    )

    # comment_count = []
    # for item in data['data']:
    #     comment_count.append(len(item.get("comments")))
    # avg = sum(comment_count) / len(comment_count)
    # percentile_75 = np.percentile(comment_count, 75)
    # max_threshold = avg + 1.5 * (percentile_75 - avg)
    # count = 0
    # for item in data['data']:
    #     if len(item.get("comments")) > max_threshold:
    #         print(data['data'][data['data'].index(item)].get("id") + " with " + str(
    #             len(item.get("comments"))) + " comment number deleted!")
    #         del data['data'][data['data'].index(item)]
    #         count += 1
    # print("Number of outliers: " + str(count))
    # open(data_file, "w").write(
    #     json.dumps(data, sort_keys=True, indent=4)
    # )
