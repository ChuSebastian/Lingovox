import whisperx
import gc
import torch
"""
device = "cuda"
audio_file = "records/audio1.wav"
batch_size = 16 # reduce if low on GPU mem
compute_type = "int8" # change to "int8" if low on GPU mem (may reduce accuracy)

# 1. Transcribe with original whisper (batched)
model = whisperx.load_model("large-v2", device, compute_type=compute_type)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print(result["segments"]) # before alignment

# delete model if low on GPU resources
import gc; gc.collect(); torch.cuda.empty_cache(); del model

# 2. Align whisper output
model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

print(result["segments"]) # after alignment

# delete model if low on GPU resources
# import gc; gc.collect(); torch.cuda.empty_cache(); del model_a

token = "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"

# 3. Assign speaker labels
diarize_model = whisperx.DiarizationPipeline(use_auth_token=token, device=device)

# add min/max number of speakers if known
diarize_segments = diarize_model(audio)
# diarize_model(audio, min_speakers=min_speakers, max_speakers=max_speakers)

result = whisperx.assign_word_speakers(diarize_segments, result)
#print(diarize_segments)
print(result["segments"]) # segments are now assigned speaker IDs


#pasar resultados a archivo de texto
f = open("transcript.txt", "w")
for i in result["segments"]:
  f.write(i['text'])
  f.write('\n') 
  #a_traducir = i['text'] pasar esto a archivo de texto y eso lo al .py que traduce
  #print(f"{i['text']} -> start: {i['start']}, end: {i['end']}")
"""

device='cpu'
audio_file = "records/audio1.wav"
batch_size = 16 # reduce if low on GPU mem
compute_type = "float32" # change to "int8" if low on GPU mem (may reduce accuracy)

# 1. Transcribe with original whisper (batched)
model = whisperx.load_model("large-v2", device, compute_type=compute_type)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print(result["segments"]) # before alignment

token = "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"
# 3. Assign speaker labels
diarize_model = whisperx.DiarizationPipeline(use_auth_token=token, device=device)

# add min/max number of speakers if known
diarize_segments = diarize_model(audio)
# diarize_model(audio, min_speakers=min_speakers, max_speakers=max_speakers)

result = whisperx.assign_word_speakers(diarize_segments, result)

#pasar resultados a archivo de texto
f = open("transcript.txt", "w")
for i in result["segments"]:
  f.write(i['text'])
  f.write('\n') 