from pydub import AudioSegment
import json
import os

def split_mp3_by_segments(mp3_file, json_file_time, json_file_transcript, output_folder):
    print(mp3_file,json_file_time,json_file_transcript)
    
    with open(json_file_time, 'r') as f:
        time_data = json.load(f)

    with open(json_file_transcript, 'r') as f:
        transcript_data = json.load(f)

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
        output_folder_path = os.path.join(output_folder, f"{week}_{page}")
        os.makedirs(output_folder_path, exist_ok=True)

        # Save the segment as WAV file
        output_wav_file = os.path.join(output_folder_path, f"{week}_{page}.wav")
        segment.export(output_wav_file, format="wav")

        # Write transcript information to text file
        text_file_path = os.path.join(output_folder_path, "transcript.txt")
        with open(text_file_path, 'a') as text_file:
            text_file.write(f"{output_wav_file}/{transcript}\n")

if __name__ == "__main__":
    mp3_file_path = "D:\\Yeshiva\Spring24\AI_of_Application\CoMoSpeech_VC\VQA\week_5.mp3"
    json_file_time_path = "D:\\Yeshiva\Spring24\AI_of_Application\CoMoSpeech_VC\VQA\week_5_timestamp.json"
    json_file_transcript_path = "D:\\Yeshiva\Spring24\AI_of_Application\CoMoSpeech_VC\VQA\week_5_transcript.json"
    output_folder_path = "D:\\Yeshiva\Spring24\AI_of_Application\CoMoSpeech_VC\out"

    split_mp3_by_segments(mp3_file_path, json_file_time_path, json_file_transcript_path, output_folder_path)
