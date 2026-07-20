import whisper
import json 
model = whisper.load_model("large-v2")      
result = model.transcribe(audio= "audios/output.mp3",
                          language="hi",
                          task="translate",
                           word_timestamps=False)
print(result["segments"])

chunks=[]
for segment in result["segments"]:
    chunks.append({'start':segment["start"], "end":segment["end"],"text":segment["text"]})
print(chunks)

# this will put the text of the video in the json file
with open ("outout.json","w") as f:
    json.dump(chunks, f)
