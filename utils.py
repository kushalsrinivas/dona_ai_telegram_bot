import requests


def join_meet(link):
    url = "http://localhost:8080/join"
    form_data = {"meetLink": link}

    try:
        response = requests.post(url, data=form_data, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response.raise_for_status()  # Raises an HTTPError if the response was an error

        data = response.json()
        return(data)
    except requests.exceptions.RequestException as error:
        print("Fetch error:", error)

def getOverveiw(id):
    url = "http://localhost:8080/overview"
    try:
        response = requests.get(url, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response.raise_for_status()  # Raises an HTTPError if the response was an error
        data = response.json()
        return (data)
    except requests.exceptions.RequestException as error:
        print("Fetch error:", error)


def getSerilisedText (textArray):
    result = ["> "+text+"\n" for text in textArray]
    return "".join(result)

def getMatchedContext(query):
    url = "http://localhost:8080/match"
    form_data = {"input": query}
    try:
        response = requests.post(url, data=form_data, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response.raise_for_status()  # Raises an HTTPError if the response was an error

        data = response.json()
        return (data)
    except requests.exceptions.RequestException as error:
        print("Fetch error:", error)
