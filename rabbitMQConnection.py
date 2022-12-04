import requests
r = requests.post("https://dm96p5t574.execute-api.us-east-2.amazonaws.com/testing/ec2", json = {'Object': '2.2'})
# And done.
print(r.text) # displays the result body.
