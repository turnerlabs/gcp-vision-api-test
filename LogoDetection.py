import base64
import requests
import os
import json
import time
import csv
import sys
import pandas as pd

def list_images(resultFileName, TOKEN):
    """detect logos of every image in directory"""
    for img in os.listdir('./images'):
        detect_logos('./images/' + img, resultFileName, TOKEN)

def detect_logos(fileName,resultFileName, TOKEN):
    colNames = ['ImagName','Logo','Confidence','TopLeft(x,y)','TopRight(x,y)','BottomRight(x,y)','BottomLeft(x,y)']
    df = pd.DataFrame(columns=colNames)
    imageName = fileName.rsplit("/")[-1]
    with open(fileName,"rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    body = {
      "requests":[
        {
          "image":{
            "content":encoded_string
          },
          "features":[
            {
              "type":"LOGO_DETECTION",
              "maxResults":10
            }
          ]
        }
      ]
    }

    headers = {"Content-Type": "application/json","Authorization": "Bearer %s"%TOKEN}

    body = json.dumps(body)
    data = requests.post("https://vision.googleapis.com/v1/images:annotate",data=body,headers=headers)
    result = data.text
    result = json.loads(result)

    if "error" in result:
        print(result["error"])
        print("ERROR. Going to exit.")
        sys.exit(1)
        
    if "logoAnnotations" in result["responses"][0]:
        for i in range(0,len(result["responses"][0]["logoAnnotations"])):
            logo = result["responses"][0]["logoAnnotations"][i]["description"]
            confidence = result["responses"][0]["logoAnnotations"][i]["score"]
            topLeft = str(result["responses"][0]["logoAnnotations"][i]["boundingPoly"]["vertices"][0]["x"]) + ", " + str(result["responses"][0]["logoAnnotations"][i]["boundingPoly"]["vertices"][0]["y"])
            topRight = str(result["responses"][0]["logoAnnotations"][i]["boundingPoly"]["vertices"][1]["x"]) + ", " + str(result["responses"][0]["logoAnnotations"][i]["boundingPoly"]["vertices"][1]["y"])
            bottomRight = str(result["responses"][0]["logoAnnotations"][i]["boundingPoly"]["vertices"][2]["x"]) + ", " + str(result["responses"][0]["logoAnnotations"][i]["boundingPoly"]["vertices"][2]["y"])
            bottomLeft = str(result["responses"][0]["logoAnnotations"][i]["boundingPoly"]["vertices"][3]["x"]) + ", " + str(result["responses"][0]["logoAnnotations"][i]["boundingPoly"]["vertices"][3]["y"])
            print imageName + " : " + logo + " : " + str(confidence)
            df_toAppend = pd.DataFrame([[imageName,logo,confidence,topLeft,topRight,bottomRight,bottomLeft]],columns = colNames)
            df = df.append(df_toAppend)

    else:
        logo = " "
        confidence = " "
        topLeft = " "
        topRight = " "
        bottomRight = " "
        bottomLeft = " "
        print imageName + " : No Results"
        df_toAppend = pd.DataFrame([[imageName,logo,confidence,topLeft,topRight,bottomRight,bottomLeft]],columns = colNames)
        df = df.append(df_toAppend)

    df.reset_index(inplace=True,drop=True)

    if os.path.exists("%s"%resultFileName):
        with open("%s"%resultFileName,"a") as f:
            df.to_csv(f,header=False,index=False)
    else:
        with open("%s"%resultFileName,"w+") as f:
            df.to_csv(f,header=True,index=False)


if __name__ == '__main__':
    TOKEN = str(os.environ.get("TOKEN", False))

    if TOKEN == "False":
        print("Must pass in TOKEN as Environment variable")
        sys.exit(1)
    
    if not os.path.exists("results"):
        os.makedirs("results")

    date = str(time.strftime("%x"))
    date = date.replace("/","-")
    pcTime = str(time.strftime("%X"))
    pcTime = pcTime.rsplit(".")[0]
    GCPName = date + "--" + pcTime + ".csv"
    resultFileName = "results/" + date + "--" + pcTime + ".csv"
    list_images(resultFileName, TOKEN)
    
