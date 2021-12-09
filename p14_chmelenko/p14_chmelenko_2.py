import json
with open('image_info_test-dev2017.json') as file:
    for line in file:
        dict = json.loads(line)
        print("Picture number:", len(dict['images']))
        print("Category number:", len(dict['categories']))
        counter = 0
        for v in dict['picture']:
            if v["id"] == counter:
                print("The largest item has a picture:", v["file_name"])
        for v in dict['picture']:
            if v["id"] > counter:
                counter = v["id"]
            if v["file_name"] == "000000000001.jpg":
                print(
                'Link to photo 000000000001.jpg:', v["coco_url\n"], 
                'Photo height 000000000001.jpg:', v["height\n"], 
                'Photo width 000000000001.jpg:', v["width\n"],
                'Photo ID 000000000001.jpg:', v["id"]
                	 )

        