import wolframalpha

input = raw_input("Question: ")
app_id = "VRU983-Q6P7962YGL"
client = wolframalpha.Client(app_id)

result = client.query(input)
answer = next(result.results).text

print answer
