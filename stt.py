import whisper
model = whisper.load_model("large-v2")      
result = model.transcribe(audio= "audios/2_Your First HTML Website ｜ Sigma Web Development Course - Tutorial #2 [kJEsTjH5mVg].webm.mp3",
                          language="hi",
                          task="translate")
print(result["text"])