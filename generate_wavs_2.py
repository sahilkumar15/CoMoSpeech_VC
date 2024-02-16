from pydub import AudioSegment
import json
import os
import platform
from pathlib import Path
import tempfile

# platform_name = platform.system()

# def path_to_ffmpeg():
#     SCRIPT_DIR = Path(__file__).parent 
#     if platform_name == 'Windows':
#         return str(Path(SCRIPT_DIR, "win", "ffmpeg", "ffmpeg.exe"))
#     elif platform_name == 'Darwin':
#         return str(Path(SCRIPT_DIR, "mac", "ffmpeg", "ffmpeg"))
#     else:
#         return str(Path(SCRIPT_DIR, "linux", "ffmpeg", "ffmpeg"))

# AudioSegment.ffmpeg = path_to_ffmpeg()
    
# if platform_name == 'Windows':
#     os.environ["PATH"] += os.pathsep + str(Path(path_to_ffmpeg()).parent)
# else:
#     os.environ["LD_LIBRARY_PATH"] += ":" + str(Path(path_to_ffmpeg()).parent)

# path = os.path.dirname(os.path.realpath(__file__))
# tempfile.tempdir = path
# os.environ["PATH"] += os.pathsep + os.path.join(path, "bin")
# AudioSegment.converter = "D:\\Yeshiva\Spring24\AI_of_Application\CoMoSpeech_VC\ffmpeg\bin\ffmpeg.exe"
# AudioSegment.ffmpeg = "D:\\Yeshiva\Spring24\AI_of_Application\CoMoSpeech_VC\ffmpeg\bin\ffmpeg.exe"
#sound = AudioSegment.from_mp3("test.mp3")

def split_mp3_by_segments(mp3_file, json_file_time, json_file_transcript, output_folder):
    json_file_time = Path(json_file_time)
    json_file_transcript = Path(json_file_transcript)
    mp3_file = Path(mp3_file)
    output_folder = Path(output_folder)

    print("MP3 File:", mp3_file)
    print("JSON Time File:", json_file_time)
    print("JSON Transcript File:", json_file_transcript)
    print("Output Folder:", output_folder)
    
    with open(json_file_time, 'r') as f:
        time_data = json.load(f)

    with open(json_file_transcript, 'r') as f:
        transcript_data = json.load(f)

    # Output transcript file path
    transcript_file_path = os.path.join(output_folder, "transcript.txt")
    
    for time_segment, transcript_segment in zip(time_data, transcript_data):
        start_time = time_segment["segment_start"]
        end_time = time_segment["segment_end"]
        week = time_segment["week"]
        page = time_segment["page"]

        transcript = transcript_segment["transcript"]

        # Convert start and end timestamps to milliseconds
        start_ms = int(start_time.split(":")[0]) * 60 * 60 * 1000 + \
                   int(start_time.split(":")[1]) * 60 * 1000 + \
                   int(start_time.split(":")[2]) * 1000

        end_ms = int(end_time.split(":")[0]) * 60 * 60 * 1000 + \
                 int(end_time.split(":")[1]) * 60 * 1000 + \
                 int(end_time.split(":")[2]) * 1000

        # Load the MP3 file
        audio = AudioSegment.from_mp3(mp3_file)

        # Extract the segment
        segment = audio[start_ms:end_ms]

        # Create output folder if it doesn't exist
        #output_folder_path = os.path.join(output_folder, f"{week}_{page}")
        os.makedirs(output_folder_path, exist_ok=True)

        # Save the segment as WAV file
        output_wav_file = os.path.join(output_folder_path, f"{week}_{page}.wav")
        segment.export(output_wav_file, format="wav")

        # Append transcript information to the common transcript file
        with open(transcript_file_path, 'a') as transcript_file:
            transcript_file.write(f"{output_wav_file}/{transcript}\n")
            
        print("-"*100)
        print(f"DONE=>{week}_{page}")

if __name__ == "__main__":
    base_folder = r"D:\Yeshiva\Spring24\AI_of_Application\CoMoSpeech_VC"
    json_file_time_path = r"D:\Yeshiva\Spring24\AI_of_Application\CoMoSpeech_VC\week_5_timestamp.json"
    json_file_transcript_path = r"D:\Yeshiva\Spring24\AI_of_Application\CoMoSpeech_VC\week_5_transcript.json"
    output_folder_path = r"./out"
   
    mp3_file_path = "week_5.mp3"
    json_file_time_path = "week_5_timestamp.json"
    
    json_file_transcript_path = "week_5_transcript.json"
    output_folder_path = "out"
    
    split_mp3_by_segments(mp3_file_path, json_file_time_path, json_file_transcript_path, output_folder_path)
